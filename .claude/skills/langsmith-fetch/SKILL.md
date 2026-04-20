---
name: langsmith-fetch
description: Use when the user asks to fetch, analyze, or debug LangSmith traces, inspect LangChain or LangGraph agent execution, analyze run data from LangSmith, or troubleshoot LangChain pipelines. Trigger keywords: LangSmith, LangChain trace, LangGraph trace, agent trace, debug LangChain, fetch traces, analyze runs, LangSmith run.
---

# LangSmith Fetch Skill

## Overview
Fetch and analyze LangSmith execution traces for debugging LangChain and LangGraph agents.

## Setup

```bash
pip install langsmith langchain
export LANGCHAIN_API_KEY="ls__..."
export LANGCHAIN_PROJECT="my-project"
```

## Fetch Traces

```python
from langsmith import Client

client = Client()

# List recent runs
runs = list(client.list_runs(
    project_name="my-project",
    limit=20,
    run_type="chain",  # "llm", "chain", "tool", "retriever"
    error=True,        # Only failed runs
))

for run in runs:
    print(f"Run: {run.id}")
    print(f"Name: {run.name}")
    print(f"Status: {run.status}")
    print(f"Latency: {run.end_time - run.start_time}")
    print(f"Total tokens: {run.total_tokens}")
    print(f"Error: {run.error}")
    print("---")
```

## Fetch Specific Run + Children

```python
def fetch_trace_tree(run_id: str) -> dict:
    run = client.read_run(run_id)
    
    # Get child runs (full trace tree)
    children = list(client.list_runs(
        project_name=run.session_name,
        trace_id=run.trace_id,
    ))
    
    return {
        "root": {
            "id": str(run.id),
            "name": run.name,
            "type": run.run_type,
            "status": run.status,
            "latency_ms": (run.end_time - run.start_time).total_seconds() * 1000,
            "input": run.inputs,
            "output": run.outputs,
            "error": run.error,
            "total_tokens": run.total_tokens,
            "prompt_tokens": run.prompt_tokens,
            "completion_tokens": run.completion_tokens,
        },
        "children": [
            {
                "name": c.name,
                "type": c.run_type,
                "latency_ms": (c.end_time - c.start_time).total_seconds() * 1000 if c.end_time else None,
                "error": c.error,
            }
            for c in children if str(c.id) != run_id
        ]
    }
```

## Analyze Failure Patterns

```python
def analyze_failures(project_name: str, limit: int = 50) -> dict:
    failed_runs = list(client.list_runs(
        project_name=project_name,
        error=True,
        limit=limit,
    ))
    
    error_counts = {}
    for run in failed_runs:
        error_type = type(run.error).__name__ if run.error else "Unknown"
        error_counts[error_type] = error_counts.get(error_type, 0) + 1
    
    avg_latency = sum(
        (r.end_time - r.start_time).total_seconds()
        for r in failed_runs if r.end_time
    ) / len(failed_runs) if failed_runs else 0
    
    return {
        "total_failures": len(failed_runs),
        "error_distribution": error_counts,
        "avg_latency_before_failure": avg_latency,
        "sample_errors": [r.error for r in failed_runs[:3]],
    }
```

## Token Cost Analysis

```python
def cost_analysis(project_name: str, days: int = 7) -> dict:
    from datetime import datetime, timedelta
    
    runs = list(client.list_runs(
        project_name=project_name,
        start_time=datetime.now() - timedelta(days=days),
        run_type="llm",
    ))
    
    total_prompt = sum(r.prompt_tokens or 0 for r in runs)
    total_completion = sum(r.completion_tokens or 0 for r in runs)
    
    # Claude Sonnet 4.6 pricing (approximate)
    cost = (total_prompt * 3 + total_completion * 15) / 1_000_000
    
    return {
        "total_llm_calls": len(runs),
        "total_prompt_tokens": total_prompt,
        "total_completion_tokens": total_completion,
        "estimated_cost_usd": round(cost, 4),
    }
```

## Output Format
- Trace tree with latency per step
- Failure analysis: error distribution + sample errors
- Token cost breakdown
- Actionable recommendation based on findings

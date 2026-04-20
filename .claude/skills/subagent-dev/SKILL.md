---
name: subagent-dev
description: Use when the user asks to implement a complex multi-step task by dispatching independent subagents, parallelize work across agents, or run code review checkpoints between implementation iterations. Trigger keywords: subagent, parallel agents, dispatch agents, multi-agent task, agent orchestration, parallel implementation, spawn subagents.
---

# Subagent Development Skill

## Overview
Dispatch independent subagents per task with code review checkpoints between iterations. Keeps parent context clean and enables parallel execution.

## When to Use Subagents

| Use Case | Benefit |
|----------|---------|
| Independent file changes | Parallel execution |
| Code review | Zero context bias |
| Research before coding | Clean separation |
| QA / testing | Independent verification |

## Dispatch Pattern

### Parallel independent subagents
```python
# Spawn multiple agents simultaneously for independent work
tasks = [
    {"file": "src/auth.py", "task": "implement JWT validation"},
    {"file": "src/users.py", "task": "implement CRUD operations"},
    {"file": "tests/test_auth.py", "task": "write auth unit tests"},
]
# All run in parallel — each gets a clean context
```

### Sequential with checkpoints
```
Step 1: Implement feature (parent agent)
Step 2: Spawn code-reviewer subagent → get report
Step 3: Fix issues identified (parent agent)
Step 4: Spawn qa subagent → run tests
Step 5: Fix failures (parent agent)
Step 6: Ship
```

## Subagent Types

### code-reviewer
- **Input**: file path(s) + change description
- **Output**: issues by severity (critical/major/minor) + PASS/FAIL verdict
- **Rule**: read-only, never modifies code

### qa
- **Input**: code snippet or file + function to test
- **Output**: test file + pass/fail results
- **Rule**: generates and runs tests, never fixes code

### research
- **Input**: question or topic
- **Output**: concise sourced findings
- **Rule**: web search + file reads, no code changes

### email-classifier
- **Input**: batch of emails
- **Output**: classified list (Action Required / Waiting On / Reference)

## Writing Good Subagent Prompts

**Include:**
- File paths (exact)
- What to check/do (specific)
- What format to return results in
- What NOT to do (e.g., "do not modify files")

**Avoid:**
- "Based on your findings, fix the bug" — synthesis must stay in parent
- Delegating understanding: include file paths, line numbers, specific change

## Output Format
- List tasks dispatched to subagents
- Show results from each subagent
- Apply all fixes in parent agent
- Final confirmation after all checkpoints pass

---
name: prompt-engineering
description: Use when the user asks to improve, optimize, design, or learn about prompts, prompt techniques, or prompt patterns. Includes chain-of-thought, few-shot examples, system prompts, and Anthropic best practices. Trigger keywords: prompt engineering, optimize prompt, improve prompt, prompt design, chain of thought, few-shot, system prompt, prompt technique, better prompt.
---

# Prompt Engineering Skill

## Overview
Teach and apply prompt engineering techniques including Anthropic best practices for Claude.

## Core Techniques

### 1. Be Specific and Direct
```
❌ "Summarize this"
✓ "Summarize this article in 3 bullet points, each under 20 words, focusing on business impact"
```

### 2. Chain-of-Thought (CoT)
Add "Think step by step" or show reasoning steps:
```
Solve this problem. Think through it step by step before giving your final answer.

Problem: [problem]

Reasoning:
Step 1: ...
Step 2: ...
Final Answer: ...
```

### 3. Few-Shot Examples
Show the pattern with 2-3 examples before the actual task:
```
Convert formal names to casual:
- "Jonathan Smith" → "Jon"
- "Elizabeth Johnson" → "Liz"
- "Robert Williams" → "Bob"

Now convert: "Christopher Anderson" → 
```

### 4. Role Assignment
```
You are a senior software engineer with 10 years of Python experience.
Review this code for performance issues only. Ignore style issues.
```

### 5. Output Format Control
```
Return ONLY a JSON array. No explanation, no markdown, no code blocks.
Format: [{"name": string, "score": number}]
```

### 6. XML Tags for Structure (Anthropic-specific)
Claude handles XML tags exceptionally well:
```
<context>
  [background information]
</context>

<task>
  [what to do]
</task>

<constraints>
- Max 200 words
- Professional tone
- No jargon
</constraints>
```

### 7. System Prompt Structure
```
You are [role]. Your job is to [purpose].

Guidelines:
- [behavior 1]
- [behavior 2]

When the user asks X, always do Y.
Never do Z.
```

## Anthropic-Specific Best Practices

| Technique | When to use |
|-----------|-------------|
| XML tags | Complex structured inputs |
| `<thinking>` | Extended reasoning tasks |
| `\n\nHuman:` / `\n\nAssistant:` | Few-shot conversation examples |
| Prefill | Control output start exactly |
| Long context: put instructions last | Before the document to analyze |

### Prefill Technique
```python
messages = [{"role": "user", "content": "Classify this as positive or negative: 'Great product!'"}]
# Add assistant prefill to constrain output
messages.append({"role": "assistant", "content": "Sentiment:"})
# Claude will complete: "Sentiment: Positive"
```

## Prompt Optimization Process

1. Write initial prompt
2. Test on 5-10 diverse examples
3. Identify failure modes
4. Hypothesize fixes (more examples, clearer constraints, different structure)
5. A/B test changes
6. Measure: accuracy, consistency, output format compliance

## Output Format
- Provide the improved prompt directly
- Show before/after comparison
- Explain which technique was applied and why
- Note any edge cases to watch

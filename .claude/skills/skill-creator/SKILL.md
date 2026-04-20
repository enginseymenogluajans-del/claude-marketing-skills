---
name: skill-creator
description: Use when the user asks to build, create, design, evaluate, improve, or benchmark a Claude Code skill. Also use when asked to optimize a skill description, run evals on a skill, or test skill trigger rates. Trigger keywords: create skill, build skill, new skill, skill eval, skill benchmark, optimize skill description, skill creator, SKILL.md.
---

# Skill Creator

## Overview
Build new skills, run evals, optimize descriptions, and benchmark performance. Supports 4 modes: CREATE, EVAL, IMPROVE, BENCHMARK.

## Modes

### CREATE — Build from scratch
1. Ask: what does the skill do? When should it trigger? What's the output?
2. Draft SKILL.md with YAML frontmatter + instructions
3. Create test cases covering main use cases
4. Run EVAL loop, then IMPROVE until pass rate ≥ 80%

### EVAL — Measure effectiveness
1. Define test prompts that should trigger the skill
2. For each prompt, check: does skill trigger? Is output correct?
3. Report: pass rate, avg token usage, failure patterns

### IMPROVE — Fix failing cases
1. Analyze failing test cases from EVAL
2. Identify: wrong trigger, missing steps, unclear output format
3. Update skill body or description
4. Re-run EVAL to confirm improvement

### BENCHMARK — CI integration
1. Run full EVAL suite before and after model/skill update
2. Compare pass rates side by side
3. Flag regressions > 5% drop

## SKILL.md Template
```markdown
---
name: skill-name
description: Use when the user asks to [action]. Trigger keywords: [word1], [word2], [word3].
---

# Skill Title

## Overview
[One paragraph purpose]

## Steps
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Output Format
[Define expected output]
```

## Golden Rules for Descriptions
- Start with "Use when the user asks to..." — critical for routing
- Include concrete trigger keywords
- Stay under 200 words
- Be specific — avoid generic phrases like "code tool"
- Use assertive language (measurably increases trigger rate)

## Trigger Optimization Loop
1. Split eval set: 60% train / 40% held-out test
2. Test current description 3× per query
3. Analyze failures → propose new description (max 200 words)
4. Re-evaluate on train + test
5. Repeat up to 5 iterations, pick best test score
6. Return optimized description

## Output Format
- New skill: create `.claude/skills/<name>/SKILL.md`
- Eval report: pass/fail per test case + overall rate
- Improved description: show diff of changes made

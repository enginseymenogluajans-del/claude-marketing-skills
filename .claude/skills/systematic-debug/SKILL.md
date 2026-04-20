---
name: systematic-debug
description: Use when the user reports a bug, test failure, unexpected behavior, error, exception, or something not working. Apply a systematic debugging process to diagnose and fix the root cause. Trigger keywords: bug, error, not working, broken, exception, fails, unexpected, debug, crash, traceback.
---

# Systematic Debug Skill

## Overview
Systematic debugging process for bugs, test failures, or unexpected behavior. Diagnose root cause before touching code.

## Debug Process

### Step 1 — Reproduce
- Get the exact error message / stack trace
- Identify the minimal steps to reproduce
- Confirm you can reproduce it reliably

### Step 2 — Understand the failure
```
What was expected?
What actually happened?
What changed recently? (git log --oneline -10)
```

### Step 3 — Form hypotheses (ranked by probability)
1. Most likely cause based on error message
2. Second hypothesis
3. Edge case / environmental issue

### Step 4 — Gather evidence
```bash
# Check recent changes
git diff HEAD~1

# Search for relevant code
grep -r "function_name" --include="*.py" .

# Check logs
tail -n 50 app.log

# Check environment
python --version
pip list | grep package_name
```

### Step 5 — Test hypotheses (smallest change first)
- Add targeted print/logging to narrow down location
- Comment out sections to isolate
- Test with minimal reproduction case

### Step 6 — Fix
- Apply the minimal fix for the confirmed root cause
- Don't fix unrelated issues in the same change

### Step 7 — Verify
- Run the failing test/scenario → confirm it passes
- Run full test suite → confirm no regressions
- Check edge cases around the fix

## Common Patterns

### Python exceptions
```python
import traceback
try:
    # suspect code
    result = do_thing()
except Exception as e:
    traceback.print_exc()
    print(f"Type: {type(e).__name__}, Value: {e}")
```

### Add debug logging
```python
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.debug(f"Input: {input_val}, State: {state}")
```

### Check variable state
```python
# Quick inspection
print(f"{var=}")  # Python 3.8+ f-string debug
```

## Output Format
Report:
1. Root cause (confirmed)
2. Fix applied
3. Test result (before → after)
4. Any related risks to watch

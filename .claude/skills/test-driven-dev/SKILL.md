---
name: test-driven-dev
description: Use when the user asks to implement a feature, fix a bug, or write code using TDD (Test-Driven Development). Always write tests first, then implement. Auto-trigger for every new feature or bugfix request. Trigger keywords: TDD, test-driven, write tests first, red-green-refactor, unit test, pytest, jest, implement with tests.
---

# Test-Driven Development Skill

## Overview
Apply TDD discipline: write failing tests first, then implement the minimum code to pass them, then refactor. Auto-triggered for every feature or bugfix.

## The Red-Green-Refactor Loop

### Step 1 — RED: Write failing test
```python
# tests/test_feature.py
import pytest
from mymodule import calculate_discount

def test_discount_10_percent_for_premium():
    result = calculate_discount(100, "premium")
    assert result == 90

def test_discount_0_for_standard():
    result = calculate_discount(100, "standard")
    assert result == 100

def test_raises_on_negative_price():
    with pytest.raises(ValueError):
        calculate_discount(-10, "premium")
```

Run: `pytest tests/test_feature.py` → expect FAIL

### Step 2 — GREEN: Write minimum implementation
```python
# mymodule.py
def calculate_discount(price: float, tier: str) -> float:
    if price < 0:
        raise ValueError("Price cannot be negative")
    if tier == "premium":
        return price * 0.9
    return price
```

Run: `pytest tests/test_feature.py` → expect PASS

### Step 3 — REFACTOR: Clean up
- Remove duplication
- Improve naming
- Extract constants
- Re-run tests to confirm still green

## Workflow

1. Understand the requirement fully before writing any production code
2. Write the smallest test that captures one behavior
3. Run → confirm it fails (proves test is meaningful)
4. Write the simplest code to make it pass
5. Run → confirm it passes
6. Refactor both test and code
7. Repeat for next behavior

## Test Naming Convention
`test_<what>_<condition>_<expected_result>`

## Coverage Check
```bash
pytest --cov=. --cov-report=term-missing
```
Aim for ≥ 80% coverage on new code.

## Output Format
- Show test file first
- Show implementation second
- Show passing test output
- Note any edge cases not yet covered

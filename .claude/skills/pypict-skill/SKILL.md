---
name: pypict-skill
description: Use when the user asks to design comprehensive test cases using combinatorial testing, pairwise testing, PICT (Pairwise Independent Combinatorial Testing), or needs to cover parameter combinations efficiently. Trigger keywords: PICT, pairwise testing, combinatorial testing, test case generation, parameter combinations, test coverage, combinatorial test design.
---

# PICT (Pairwise Independent Combinatorial Testing) Skill

## Overview
Design comprehensive test cases using PICT — covering all pairwise parameter combinations with minimum test cases. Reduces test count from exhaustive (exponential) to manageable while maintaining high defect detection.

## Why Pairwise Testing
Most defects are caused by interactions between 2 parameters. Pairwise testing guarantees every pair of values appears at least once, typically reducing test cases by 60-90%.

```
Exhaustive (3 params × 3 values): 3³ = 27 tests
Pairwise coverage:                       9 tests
```

## PICT Model File

```
# params.pict — define your parameters
OS:      Windows, Linux, MacOS
Browser: Chrome, Firefox, Safari, Edge
Language: English, Spanish, French
Auth:    OAuth, Password, SSO
Role:    Admin, User, Guest
```

## Run PICT

```bash
# Install PICT
# Windows: winget install Microsoft.PICT
# Linux: build from source or use pypict

# Generate test cases
pict params.pict /o:2 > test_cases.txt   # pairwise (order=2)
pict params.pict /o:3 > test_cases.txt   # triple-wise

# With constraints
pict params.pict /o:2 /c:constraints.txt
```

## Python (pypict or allpairspy)

```python
# pip install allpairspy
from allpairspy import AllPairs

parameters = [
    ["Windows", "Linux", "MacOS"],
    ["Chrome", "Firefox", "Safari", "Edge"],
    ["English", "Spanish", "French"],
    ["OAuth", "Password", "SSO"],
    ["Admin", "User", "Guest"],
]

print(f"{'#':<4} {'OS':<10} {'Browser':<10} {'Language':<10} {'Auth':<10} {'Role':<8}")
print("-" * 55)

for i, pairs in enumerate(AllPairs(parameters)):
    values = pairs.test_parameters
    print(f"{i+1:<4} {values[0]:<10} {values[1]:<10} {values[2]:<10} {values[3]:<10} {values[4]:<8}")
```

## PICT Constraints File

```
# constraints.pict
# Safari only on MacOS
IF [Browser] = "Safari" THEN [OS] = "MacOS";

# SSO requires Admin or User role
IF [Auth] = "SSO" THEN [Role] <> "Guest";

# Edge not on MacOS
IF [Browser] = "Edge" THEN [OS] <> "MacOS";
```

## Convert to Test Cases

```python
import csv
from allpairspy import AllPairs

parameters = {
    "OS": ["Windows", "Linux", "MacOS"],
    "Browser": ["Chrome", "Firefox", "Safari"],
    "Auth": ["OAuth", "Password"],
}

keys = list(parameters.keys())
values = list(parameters.values())

with open("test_cases.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["Test #"] + keys)
    writer.writeheader()
    for i, pairs in enumerate(AllPairs(values), 1):
        row = {"Test #": i}
        row.update(dict(zip(keys, pairs.test_parameters)))
        writer.writerow(row)

print(f"Generated {i} test cases (vs {len(values[0])**len(keys)} exhaustive)")
```

## Output Format
- Table of generated test cases (# | param1 | param2 | ...)
- Count: generated vs exhaustive
- CSV file saved to `.tmp/test_cases.csv`
- Note any constraints applied

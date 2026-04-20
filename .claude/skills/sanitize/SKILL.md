---
name: sanitize
description: Use when the user asks to detect, find, redact, or remove PII (personally identifiable information) from text, files, or datasets. Covers SSN, credit cards, emails, phone numbers, API keys, and 15+ PII categories. Fully local, zero dependencies beyond Python stdlib. Trigger keywords: PII, redact, sanitize, remove personal data, detect sensitive data, anonymize, SSN, credit card number, API key, GDPR, personal information.
---

# Sanitize Skill

## Overview
Detect and redact PII across 15 categories. Zero dependencies, fully local. No data leaves the machine.

## PII Categories Covered

| Category | Example | Pattern |
|----------|---------|---------|
| SSN | 123-45-6789 | `\d{3}-\d{2}-\d{4}` |
| Credit Card | 4111-1111-1111-1111 | `\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}` |
| Email | user@example.com | RFC 5322 pattern |
| Phone | +1-800-555-0123 | Various formats |
| IP Address | 192.168.1.1 | `\d{1,3}\.\d{1,3}...` |
| API Key | sk-abc123... | Common key prefixes |
| AWS Key | AKIA... | `AKIA[A-Z0-9]{16}` |
| JWT | eyJ... | Base64 encoded |
| Password in code | password="secret" | Variable assignment |
| Date of Birth | 01/15/1990 | Date patterns |
| Passport | A12345678 | Country-specific |
| Driver's License | D-12345678 | State-specific |
| Bank Account | 1234567890 | Long digit sequences |
| Medical Record | MRN: 12345 | Prefix patterns |
| Name + Address | Combined | NLP (spacy optional) |

## Core Script

```python
import re
from pathlib import Path

PII_PATTERNS = {
    "SSN":         r"\b\d{3}[-\s]?\d{2}[-\s]?\d{4}\b",
    "CREDIT_CARD": r"\b\d{4}[\s\-]?\d{4}[\s\-]?\d{4}[\s\-]?\d{4}\b",
    "EMAIL":       r"\b[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Z|a-z]{2,}\b",
    "PHONE":       r"\b(\+?1[-.\s]?)?(\(?\d{3}\)?[-.\s]?)?\d{3}[-.\s]?\d{4}\b",
    "IP_ADDRESS":  r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b",
    "AWS_KEY":     r"\bAKIA[A-Z0-9]{16}\b",
    "API_KEY":     r"\b(sk|pk|api|key|token|secret)[-_]?[A-Za-z0-9]{20,}\b",
    "JWT":         r"\beyJ[A-Za-z0-9_\-]+\.[A-Za-z0-9_\-]+\.[A-Za-z0-9_\-]+\b",
    "PASSWORD":    r'(password|passwd|pwd)\s*[=:]\s*["\']?[^\s"\']{4,}',
    "DOB":         r"\b(0[1-9]|1[0-2])[\/\-](0[1-9]|[12]\d|3[01])[\/\-]\d{2,4}\b",
}

def detect_pii(text: str) -> dict[str, list[str]]:
    findings = {}
    for category, pattern in PII_PATTERNS.items():
        matches = re.findall(pattern, text, re.IGNORECASE)
        if matches:
            findings[category] = matches
    return findings

def redact_pii(text: str, replacement: str = "[REDACTED]") -> str:
    for category, pattern in PII_PATTERNS.items():
        text = re.sub(pattern, f"[{category}]", text, flags=re.IGNORECASE)
    return text

def sanitize_file(input_path: str, output_path: str | None = None) -> dict:
    text = Path(input_path).read_text(encoding="utf-8")
    findings = detect_pii(text)
    redacted = redact_pii(text)
    
    out = output_path or input_path.replace(".", "_sanitized.")
    Path(out).write_text(redacted, encoding="utf-8")
    
    return {
        "input": input_path,
        "output": out,
        "findings": {k: len(v) for k, v in findings.items()},
        "total": sum(len(v) for v in findings.values()),
    }

if __name__ == "__main__":
    import sys
    result = sanitize_file(sys.argv[1])
    print(f"Found {result['total']} PII instances: {result['findings']}")
    print(f"Sanitized file: {result['output']}")
```

## Usage

```bash
# Detect only (no changes)
python sanitize.py detect input.txt

# Redact and save
python sanitize.py redact input.txt output.txt

# Scan directory
python sanitize.py scan ./data/
```

## Output Format
- Detection report: category → count
- Redacted file saved to specified path
- Summary: total PII instances found and removed
- Never display the actual PII values in output

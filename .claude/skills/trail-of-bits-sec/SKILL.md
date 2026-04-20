---
name: trail-of-bits-sec
description: Use when the user asks for static analysis, CodeQL analysis, Semgrep analysis, variant analysis, vulnerability detection, or professional-grade security auditing of code. Deeper than OWASP review — focuses on finding vulnerability classes and variants. Trigger keywords: CodeQL, Semgrep, static analysis, variant analysis, vulnerability detection, security audit, trail of bits, deep security analysis.
---

# Trail-of-Bits Security Skill

## Overview
Static analysis with CodeQL/Semgrep, variant analysis, vulnerability detection and fix verification. Professional-grade security audit approach.

## Semgrep Analysis

### Install and run
```bash
pip install semgrep

# Run against OWASP rules
semgrep --config=p/owasp-top-ten .

# Run against security audit rules
semgrep --config=p/security-audit .

# Python-specific
semgrep --config=p/python .

# JavaScript/TypeScript
semgrep --config=p/javascript .
semgrep --config=p/typescript .

# Auto-fix where possible
semgrep --config=p/security-audit --autofix .
```

### Custom Semgrep rule
```yaml
# .semgrep/custom.yml
rules:
  - id: hardcoded-secret
    pattern: |
      $VAR = "..."
    metavariable-regex:
      metavariable: $VAR
      regex: (password|secret|api_key|token|passwd)
    message: "Potential hardcoded secret in $VAR"
    severity: ERROR
    languages: [python, javascript]

  - id: unsafe-deserialization
    pattern: pickle.loads(...)
    message: "Unsafe deserialization with pickle"
    severity: ERROR
    languages: [python]
```

## CodeQL Analysis

### Setup
```bash
# Install CodeQL CLI
# Download from: github.com/github/codeql-cli-binaries

# Create database
codeql database create ./codeql-db --language=python --source-root=.

# Run standard queries
codeql database analyze ./codeql-db python-security-and-quality.qls \
  --format=sarif-latest --output=results.sarif
```

### Custom CodeQL query
```ql
/**
 * @name SQL injection from user input
 * @kind path-problem
 * @severity error
 */
import python
import semmle.python.dataflow.new.DataFlow
import semmle.python.dataflow.new.TaintTracking

class SqlInjectionConfig extends TaintTracking::Configuration {
  SqlInjectionConfig() { this = "SqlInjectionConfig" }

  override predicate isSource(DataFlow::Node source) {
    source instanceof RemoteFlowSource
  }

  override predicate isSink(DataFlow::Node sink) {
    exists(Call c |
      c.getFunc().(Attribute).getName() = "execute" and
      sink.asExpr() = c.getArg(0)
    )
  }
}
```

## Variant Analysis Process

1. **Find the initial vulnerability** — identify the bug class
2. **Extract the pattern** — what makes this vulnerable?
3. **Write a query/rule** — generalize the pattern
4. **Scan entire codebase** — find all variants
5. **Triage results** — true positives vs false positives
6. **Fix all instances** — not just the reported one

## Vulnerability Classes to Check

| Class | Tool | Pattern |
|-------|------|---------|
| Injection (SQL, Command, LDAP) | Semgrep + CodeQL | Taint: user input → sink |
| Deserialization | Semgrep | pickle.loads, yaml.load |
| Path traversal | Semgrep | open(user_input) |
| SSRF | Semgrep | requests.get(user_input) |
| Hardcoded secrets | Semgrep | regex on variable names |
| Timing attacks | CodeQL | string comparison of secrets |

## Output Format
```
FINDINGS:
[CRITICAL] file.py:42 — SQL Injection via user-controlled input flows to cursor.execute()
  Source: request.args.get("id") at line 38
  Sink: cursor.execute(query) at line 42
  Fix: Use parameterized query: cursor.execute("SELECT ... WHERE id=%s", (id,))

VARIANTS FOUND: 3 similar patterns in codebase
  - db.py:87
  - api/users.py:134

VERIFIED FIXES: [after fix] re-scan shows 0 matches
```

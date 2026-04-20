---
name: owasp-security
description: Use when the user asks to review code for security vulnerabilities, check for OWASP Top 10 issues, audit code security, find injection vulnerabilities, or apply secure coding patterns. Supports 20+ languages. Trigger keywords: security review, OWASP, security audit, vulnerability, injection, XSS, SQL injection, secure code, security check, ASVS.
---

# OWASP Security Skill

## Overview
Code review against OWASP Top 10:2025 and ASVS 5.0 with secure patterns for 20+ languages.

## OWASP Top 10:2025 Checklist

### A01 — Broken Access Control
```python
# VULNERABLE: user controls their own ID
@app.route("/profile/<user_id>")
def profile(user_id):
    return get_user(user_id)  # any user can access any profile

# SECURE: enforce ownership
@app.route("/profile")
@login_required
def profile():
    return get_user(current_user.id)
```

### A02 — Cryptographic Failures
```python
# VULNERABLE
import hashlib
password_hash = hashlib.md5(password.encode()).hexdigest()

# SECURE
import bcrypt
password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds=12))
```

### A03 — Injection
```python
# VULNERABLE: SQL injection
query = f"SELECT * FROM users WHERE name = '{user_input}'"

# SECURE: parameterized query
cursor.execute("SELECT * FROM users WHERE name = %s", (user_input,))
```

```javascript
// VULNERABLE: XSS
element.innerHTML = userInput;

// SECURE
element.textContent = userInput;
// Or sanitize: DOMPurify.sanitize(userInput)
```

### A04 — Insecure Design
- No rate limiting on authentication endpoints
- Business logic bypass (e.g., negative quantities)
- Missing input validation at domain layer

### A05 — Security Misconfiguration
```python
# Check for:
DEBUG = True           # never in production
SECRET_KEY = "dev"     # hardcoded secrets
CORS_ORIGIN = "*"      # overly permissive
```

### A06 — Vulnerable Components
```bash
# Python
pip audit

# Node.js
npm audit

# Check for known CVEs in dependencies
```

### A07 — Authentication Failures
```python
# SECURE session management
app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SECURE=True,    # HTTPS only
    SESSION_COOKIE_SAMESITE="Strict",
    PERMANENT_SESSION_LIFETIME=timedelta(hours=1),
)
```

### A08 — Software & Data Integrity
- Verify package checksums/signatures
- Protect CI/CD pipeline secrets
- Validate deserialized data

### A09 — Logging Failures
```python
# Log security events (but NOT sensitive data)
logger.warning(f"Failed login attempt for user_id={user_id} from IP={ip}")
# NEVER log: passwords, tokens, credit cards, SSNs
```

### A10 — SSRF
```python
# VULNERABLE
response = requests.get(user_provided_url)

# SECURE: allowlist approach
ALLOWED_DOMAINS = {"api.example.com", "cdn.example.com"}
parsed = urlparse(user_provided_url)
if parsed.hostname not in ALLOWED_DOMAINS:
    raise ValueError("Domain not allowed")
```

## Security Review Output Format

```
CRITICAL (fix before deploy):
- [file:line] Issue description | Attack vector | Fix

HIGH:
- [file:line] Issue description | Fix

MEDIUM:
- [file:line] Issue description | Recommendation

LOW / INFO:
- [file:line] Best practice suggestion

VERDICT: PASS / FAIL
```

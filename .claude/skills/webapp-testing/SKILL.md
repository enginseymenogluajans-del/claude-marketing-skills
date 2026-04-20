---
name: webapp-testing
description: Use when the user asks to test a local web application, run UI tests, validate web app behavior, take screenshots, test with Playwright, or automate browser testing. Trigger keywords: test web app, Playwright, UI test, browser test, screenshot, e2e test, end-to-end test, test UI, validate web.
---

# Web App Testing Skill

## Overview
Test local web apps with Playwright for UI validation, debugging, and screenshot capture.

## Setup

```bash
pip install playwright pytest-playwright
playwright install chromium
```

## Basic Test Structure

```python
# tests/test_webapp.py
import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope="session")
def base_url():
    return "http://localhost:3000"

def test_homepage_loads(page: Page, base_url):
    page.goto(base_url)
    expect(page).to_have_title("My App")
    expect(page.locator("h1")).to_be_visible()

def test_login_flow(page: Page, base_url):
    page.goto(f"{base_url}/login")
    page.fill("#email", "user@example.com")
    page.fill("#password", "password123")
    page.click("button[type=submit]")
    expect(page).to_have_url(f"{base_url}/dashboard")

def test_form_validation(page: Page, base_url):
    page.goto(f"{base_url}/form")
    page.click("button[type=submit]")  # submit empty
    expect(page.locator(".error-message")).to_be_visible()
    expect(page.locator(".error-message")).to_contain_text("required")
```

## Screenshot Capture

```python
def test_capture_screenshot(page: Page, base_url):
    page.goto(base_url)
    page.screenshot(path=".tmp/homepage.png", full_page=True)

# On failure
def test_with_failure_screenshot(page: Page, base_url):
    try:
        page.goto(base_url)
        expect(page.locator("#nonexistent")).to_be_visible(timeout=2000)
    except Exception:
        page.screenshot(path=".tmp/failure.png")
        raise
```

## Network Interception (Mock APIs)

```python
def test_with_mocked_api(page: Page, base_url):
    page.route("**/api/users", lambda route: route.fulfill(
        status=200,
        content_type="application/json",
        body='[{"id": 1, "name": "Test User"}]'
    ))
    page.goto(f"{base_url}/users")
    expect(page.locator(".user-name")).to_contain_text("Test User")
```

## Run Tests

```bash
# Run all tests
pytest tests/

# Run with browser visible
pytest tests/ --headed

# Run specific test
pytest tests/test_webapp.py::test_login_flow

# Generate HTML report
pytest tests/ --html=.tmp/report.html
```

## Debugging

```python
# Pause execution for manual inspection
page.pause()

# Slow down actions
playwright.chromium.launch(slow_mo=500)

# Console logs
page.on("console", lambda msg: print(f"Console: {msg.text}"))
```

## Output Format
- Test results: pass/fail per test case
- Screenshots saved to `.tmp/` folder
- Console errors captured and reported
- HTML report path if generated

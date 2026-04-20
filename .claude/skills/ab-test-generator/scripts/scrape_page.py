#!/usr/bin/env python3
"""
scrape_page.py — A/B Test Generator için sayfa kazıyıcı.
Kullanım: python3 scrape_page.py <URL>
Çıktı: JSON (başlıklar, CTAs, formlar, görseller)
"""

import sys
import json
import re

def scrape(url: str) -> dict:
    try:
        import urllib.request
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0 (compatible; ABTestBot/1.0)"}
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode("utf-8", errors="replace")
    except Exception as e:
        return {"error": str(e), "url": url}

    # Headings
    headings = []
    for tag in ["h1", "h2", "h3"]:
        for m in re.finditer(rf"<{tag}[^>]*>(.*?)</{tag}>", html, re.IGNORECASE | re.DOTALL):
            text = re.sub(r"<[^>]+>", "", m.group(1)).strip()
            if text:
                headings.append({"tag": tag.upper(), "text": text[:200]})

    # CTAs — buttons and links with action-like text
    ctas = []
    for m in re.finditer(r"<(button|a)[^>]*>(.*?)</\1>", html, re.IGNORECASE | re.DOTALL):
        text = re.sub(r"<[^>]+>", "", m.group(2)).strip()
        if text and len(text) < 80:
            ctas.append(text)
    ctas = list(dict.fromkeys(ctas))[:20]  # dedupe, cap at 20

    # Forms
    forms = []
    for m in re.finditer(r"<form[^>]*>(.*?)</form>", html, re.IGNORECASE | re.DOTALL):
        form_html = m.group(1)
        inputs = re.findall(r'<input[^>]+name=["\']([^"\']+)["\']', form_html, re.IGNORECASE)
        labels = re.findall(r"<label[^>]*>(.*?)</label>", form_html, re.IGNORECASE | re.DOTALL)
        labels = [re.sub(r"<[^>]+>", "", l).strip() for l in labels]
        forms.append({"inputs": inputs, "labels": labels})

    # Images (alt texts)
    images = []
    for m in re.finditer(r'<img[^>]+alt=["\']([^"\']*)["\']', html, re.IGNORECASE):
        alt = m.group(1).strip()
        if alt:
            images.append(alt[:150])
    images = images[:15]

    # Meta description
    meta_desc = ""
    m = re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']*)["\']', html, re.IGNORECASE)
    if m:
        meta_desc = m.group(1).strip()

    # Page title
    title = ""
    m = re.search(r"<title[^>]*>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
    if m:
        title = re.sub(r"<[^>]+>", "", m.group(1)).strip()

    return {
        "url": url,
        "title": title,
        "meta_description": meta_desc,
        "headings": headings[:15],
        "ctas": ctas,
        "forms": forms[:5],
        "image_alts": images,
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "URL gerekli. Kullanım: python3 scrape_page.py <URL>"}))
        sys.exit(1)

    result = scrape(sys.argv[1])
    print(json.dumps(result, ensure_ascii=False, indent=2))

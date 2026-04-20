---
name: pdf
description: Use when the user asks to read, merge, split, fill forms, extract tables, extract text, or perform any operation on PDF files. Trigger keywords: PDF, portable document, form filling, merge PDFs, extract from PDF, PDF table, PDF text extraction.
---

# PDF Skill

## Overview
Read, merge, split, fill forms, and extract tables or text from PDF files. Anthropic's most-used official skill.

## Steps

1. Identify the operation: read/extract, merge, split, fill form, or extract table
2. Check that required PDF file(s) exist at the specified path(s)
3. Install dependencies if needed: `pip install pypdf2 pdfplumber reportlab`
4. Execute the appropriate operation:

### Read / Extract Text
```python
import pdfplumber

with pdfplumber.open("file.pdf") as pdf:
    for page in pdf.pages:
        print(page.extract_text())
```

### Extract Tables
```python
import pdfplumber

with pdfplumber.open("file.pdf") as pdf:
    for page in pdf.pages:
        tables = page.extract_tables()
        for table in tables:
            print(table)
```

### Merge PDFs
```python
from pypdf import PdfWriter

writer = PdfWriter()
for path in ["file1.pdf", "file2.pdf"]:
    writer.append(path)
with open("merged.pdf", "wb") as f:
    writer.write(f)
```

### Fill Form Fields
```python
from pypdf import PdfReader, PdfWriter

reader = PdfReader("form.pdf")
writer = PdfWriter()
writer.append(reader)
writer.update_page_form_field_values(writer.pages[0], {"field_name": "value"})
with open("filled.pdf", "wb") as f:
    writer.write(f)
```

## Output Format
- Extracted text: display inline or save to .txt
- Tables: display as markdown or save to .csv
- Merged/filled PDFs: save to specified output path and confirm success

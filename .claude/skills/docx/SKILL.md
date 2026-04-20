---
name: docx
description: Use when the user asks to create, edit, or modify Word documents (.docx). Includes adding headings, table of contents, tracked changes, tables, images, and formatting. Trigger keywords: Word document, docx, .docx, create document, edit Word, table of contents, tracked changes.
---

# DOCX Skill

## Overview
Create and edit Microsoft Word documents with headings, table of contents, tracked changes, tables, and rich formatting using python-docx.

## Steps

1. Install dependency: `pip install python-docx`
2. Determine the operation: create new, edit existing, add TOC, track changes, insert table
3. Execute:

### Create a Document
```python
from docx import Document
from docx.shared import Pt, RGBColor

doc = Document()
doc.add_heading("Document Title", level=0)
doc.add_heading("Section 1", level=1)
doc.add_paragraph("Body text here.")

# Add table
table = doc.add_table(rows=2, cols=3)
table.style = "Table Grid"
table.cell(0, 0).text = "Header 1"

doc.save("output.docx")
```

### Edit Existing Document
```python
from docx import Document

doc = Document("existing.docx")
for para in doc.paragraphs:
    if "old text" in para.text:
        para.text = para.text.replace("old text", "new text")
doc.save("existing.docx")
```

### Add Table of Contents
```python
from docx import Document
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

doc = Document()
# Add TOC field (Word updates it on open)
paragraph = doc.add_paragraph()
run = paragraph.add_run()
fldChar = OxmlElement("w:fldChar")
fldChar.set(qn("w:fldCharType"), "begin")
run._r.append(fldChar)
instrText = OxmlElement("w:instrText")
instrText.text = 'TOC \\o "1-3" \\h \\z \\u'
run._r.append(instrText)
fldChar2 = OxmlElement("w:fldChar")
fldChar2.set(qn("w:fldCharType"), "end")
run._r.append(fldChar2)
doc.save("with_toc.docx")
```

## Output Format
Save to specified path and confirm. If no path given, save as `output.docx` in current directory.

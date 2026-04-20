---
name: pptx
description: Use when the user asks to create, build, edit, or update PowerPoint presentations (.pptx). Includes slide templates, speaker notes, layouts, charts, and images. Trigger keywords: PowerPoint, pptx, presentation, slides, speaker notes, slide deck, create presentation.
---

# PPTX Skill

## Overview
Build and update PowerPoint presentations with templates, speaker notes, layouts, charts, and images using python-pptx.

## Steps

1. Install dependency: `pip install python-pptx`
2. Determine slides needed, content, and layout style
3. Execute:

### Create a Presentation
```python
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

prs = Presentation()

# Title slide
slide_layout = prs.slide_layouts[0]
slide = prs.slides.add_slide(slide_layout)
slide.shapes.title.text = "Presentation Title"
slide.placeholders[1].text = "Subtitle"

# Content slide
slide_layout = prs.slide_layouts[1]
slide = prs.slides.add_slide(slide_layout)
slide.shapes.title.text = "Section Title"
tf = slide.placeholders[1].text_frame
tf.text = "Main point"
tf.add_paragraph().text = "Supporting detail"

# Speaker notes
notes_slide = slide.notes_slide
notes_slide.notes_text_frame.text = "Speaker notes here."

prs.save("presentation.pptx")
```

### Add Chart
```python
from pptx.util import Inches
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE

chart_data = CategoryChartData()
chart_data.categories = ["Q1", "Q2", "Q3", "Q4"]
chart_data.add_series("Revenue", (100, 150, 200, 175))

slide.shapes.add_chart(
    XL_CHART_TYPE.COLUMN_CLUSTERED,
    Inches(1), Inches(2), Inches(8), Inches(4),
    chart_data
)
```

### Edit Existing Presentation
```python
from pptx import Presentation

prs = Presentation("existing.pptx")
for slide in prs.slides:
    for shape in slide.shapes:
        if shape.has_text_frame:
            for para in shape.text_frame.paragraphs:
                for run in para.runs:
                    if "old" in run.text:
                        run.text = run.text.replace("old", "new")
prs.save("existing.pptx")
```

## Output Format
Save to specified path and confirm. Default: `presentation.pptx`.

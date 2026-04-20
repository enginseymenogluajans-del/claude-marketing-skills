---
name: xlsx
description: Use when the user asks to create, read, edit, or analyze Excel spreadsheets (.xlsx). Includes pivot tables, charts, formulas, conditional formatting, and complex spreadsheet operations. Trigger keywords: Excel, xlsx, spreadsheet, pivot table, Excel chart, Excel formula, openpyxl, pandas Excel.
---

# XLSX Skill

## Overview
Excel analysis, pivot tables, charts, and formulas. Handle complex spreadsheet operations using openpyxl and pandas.

## Steps

1. Install dependencies: `pip install openpyxl pandas xlsxwriter`
2. Determine operation: read, create, pivot, chart, formula
3. Execute:

### Read Excel
```python
import pandas as pd

df = pd.read_excel("data.xlsx", sheet_name="Sheet1")
print(df.head())
print(df.describe())
```

### Create Excel with Formatting
```python
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Report"

# Header row
headers = ["Name", "Q1", "Q2", "Q3", "Total"]
for col, header in enumerate(headers, 1):
    cell = ws.cell(row=1, column=col, value=header)
    cell.font = Font(bold=True)
    cell.fill = PatternFill("solid", fgColor="4472C4")

# Data + formula
ws.append(["Alice", 100, 150, 200])
ws["E2"] = "=SUM(B2:D2)"

wb.save("output.xlsx")
```

### Pivot Table with pandas
```python
import pandas as pd

df = pd.read_excel("data.xlsx")
pivot = df.pivot_table(
    values="Revenue",
    index="Region",
    columns="Quarter",
    aggfunc="sum",
    fill_value=0
)
pivot.to_excel("pivot_output.xlsx")
```

### Add Chart
```python
from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference

wb = Workbook()
ws = wb.active
data = [["Month", "Sales"], ["Jan", 100], ["Feb", 150], ["Mar", 200]]
for row in data:
    ws.append(row)

chart = BarChart()
chart.title = "Monthly Sales"
data_ref = Reference(ws, min_col=2, min_row=1, max_row=4)
chart.add_data(data_ref, titles_from_data=True)
ws.add_chart(chart, "D2")
wb.save("chart.xlsx")
```

## Output Format
Save to specified path. Display key statistics inline if reading. Default output: `output.xlsx`.

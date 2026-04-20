---
name: web-artifacts
description: Use when the user asks to create complex multi-component HTML artifacts, interactive web apps, React components, data visualizations, or self-contained HTML/JS/CSS files. Uses React, Tailwind CSS, and shadcn/ui. Trigger keywords: web artifact, HTML artifact, React component, interactive HTML, shadcn, Tailwind, self-contained web app, single HTML file.
---

# Web Artifacts Skill

## Overview
Create complex multi-component HTML artifacts using React, Tailwind CSS, and shadcn/ui. Output self-contained, interactive files.

## Stack
- React 18 (via CDN — no build step)
- Tailwind CSS (via CDN)
- shadcn/ui components (inline)
- Lucide icons

## Base Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>App Title</title>
  <script src="https://unpkg.com/react@18/umd/react.development.js"></script>
  <script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
  <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    * { box-sizing: border-box; }
    body { font-family: system-ui, sans-serif; background: #0a0a0a; color: #f5f5f5; margin: 0; }
  </style>
</head>
<body>
  <div id="root"></div>
  <script type="text/babel">
    const { useState, useEffect, useCallback } = React;

    // Components
    function Card({ children, className = "" }) {
      return (
        <div className={`border border-neutral-800 bg-neutral-900 rounded-lg p-4 ${className}`}>
          {children}
        </div>
      );
    }

    function Button({ children, onClick, variant = "primary", disabled = false }) {
      const styles = {
        primary: "bg-orange-600 hover:bg-orange-500 text-white",
        secondary: "bg-neutral-800 hover:bg-neutral-700 text-neutral-200",
        ghost: "hover:bg-neutral-800 text-neutral-400",
      };
      return (
        <button
          onClick={onClick}
          disabled={disabled}
          className={`px-4 py-2 rounded text-sm font-medium transition-colors disabled:opacity-50 ${styles[variant]}`}
        >
          {children}
        </button>
      );
    }

    // Main App
    function App() {
      const [state, setState] = useState(null);

      return (
        <div className="min-h-screen p-6 max-w-4xl mx-auto">
          <h1 className="text-2xl font-bold mb-6">App Title</h1>
          <Card>
            <p className="text-neutral-400">Content here</p>
            <Button onClick={() => setState("clicked")}>Action</Button>
          </Card>
        </div>
      );
    }

    ReactDOM.createRoot(document.getElementById("root")).render(<App />);
  </script>
</body>
</html>
```

## Common Component Patterns

### Data Table
```jsx
function DataTable({ data, columns }) {
  return (
    <div className="overflow-x-auto">
      <table className="w-full text-sm">
        <thead>
          <tr className="border-b border-neutral-800">
            {columns.map(col => (
              <th key={col.key} className="text-left py-3 px-4 text-neutral-400 font-medium">
                {col.label}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {data.map((row, i) => (
            <tr key={i} className="border-b border-neutral-800/50 hover:bg-neutral-800/30">
              {columns.map(col => (
                <td key={col.key} className="py-3 px-4 text-neutral-200">
                  {row[col.key]}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
```

### Chart (without library)
```jsx
function BarChart({ data }) {
  const max = Math.max(...data.map(d => d.value));
  return (
    <div className="flex items-end gap-2 h-40">
      {data.map((d, i) => (
        <div key={i} className="flex-1 flex flex-col items-center gap-1">
          <span className="text-xs text-neutral-400">{d.value}</span>
          <div
            className="w-full bg-orange-600 rounded-sm transition-all"
            style={{ height: `${(d.value / max) * 100}%` }}
          />
          <span className="text-xs text-neutral-500 truncate w-full text-center">{d.label}</span>
        </div>
      ))}
    </div>
  );
}
```

## Output Format
Single `.html` file, completely self-contained, no external dependencies beyond CDN links. Fully functional on open — no server required.

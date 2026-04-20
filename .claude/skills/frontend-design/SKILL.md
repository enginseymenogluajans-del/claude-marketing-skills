---
name: frontend-design
description: Use when the user asks to create, design, or build a frontend UI, web interface, landing page, dashboard, or any visual web component with distinctive production-grade aesthetics. Avoids generic AI aesthetics. Trigger keywords: frontend, UI design, web design, landing page, dashboard UI, component design, beautiful UI, production UI, design system.
---

# Frontend Design Skill

## Overview
Create distinctive, production-grade frontend interfaces that avoid generic AI aesthetics. Focus on real design principles: contrast, hierarchy, whitespace, and motion.

## Design Principles

### Anti-patterns to avoid
- Gradient purple/blue "AI look"
- Rounded cards with drop shadows everywhere
- Generic sans-serif on white background
- Animated loading spinners as decoration
- Centered hero with CTA button on gradient

### What to do instead
- Strong typographic hierarchy (weight, size, case contrast)
- Purposeful color: one accent, neutral base, dark/light contrast
- Generous whitespace with intentional density variation
- Micro-interactions that communicate state, not decoration

## Component Patterns

### Typography System
```css
:root {
  --font-display: 'Inter', system-ui;
  --text-xs: 0.75rem;
  --text-sm: 0.875rem;
  --text-base: 1rem;
  --text-lg: 1.125rem;
  --text-xl: 1.25rem;
  --text-2xl: 1.5rem;
  --text-4xl: 2.25rem;
  --font-medium: 500;
  --font-semibold: 600;
  --font-bold: 700;
  --leading-tight: 1.25;
  --leading-relaxed: 1.625;
}
```

### Color System
```css
:root {
  --color-background: #0a0a0a;
  --color-surface: #141414;
  --color-border: #1f1f1f;
  --color-text-primary: #f5f5f5;
  --color-text-secondary: #a3a3a3;
  --color-accent: #e85d04;      /* single strong accent */
  --color-accent-subtle: #1a0a00;
}
```

### Layout Principles
```css
/* Consistent spacing scale */
.section { padding: 5rem 0; }
.container { max-width: 1200px; margin: 0 auto; padding: 0 1.5rem; }

/* Grid for content density */
.grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; }

/* Intentional whitespace */
.hero { min-height: 90vh; display: grid; place-items: center; }
```

### Interactive States
```css
.button {
  background: var(--color-accent);
  transition: all 150ms ease;
  cursor: pointer;
}
.button:hover { filter: brightness(1.1); transform: translateY(-1px); }
.button:active { transform: translateY(0); }
.button:focus-visible { outline: 2px solid var(--color-accent); outline-offset: 2px; }
```

## React + Tailwind Pattern

```tsx
export function Card({ title, description, metric }: CardProps) {
  return (
    <div className="group border border-neutral-800 bg-neutral-900 p-6 hover:border-neutral-700 transition-colors">
      <div className="flex items-start justify-between mb-4">
        <h3 className="text-sm font-medium text-neutral-400 uppercase tracking-wide">
          {title}
        </h3>
        <span className="text-xs text-neutral-600">↗</span>
      </div>
      <p className="text-3xl font-bold text-white tabular-nums">{metric}</p>
      <p className="mt-2 text-sm text-neutral-500">{description}</p>
    </div>
  );
}
```

## Output Format
- Provide complete, runnable HTML/CSS/TSX
- Include all states: default, hover, focus, active, disabled
- Mobile-first responsive design
- No placeholder comments — ship-ready code

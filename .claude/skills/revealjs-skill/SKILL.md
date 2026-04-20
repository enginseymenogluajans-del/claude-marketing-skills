---
name: revealjs-skill
description: Use when the user asks to create a professional presentation using Reveal.js, an HTML-based slide deck, or a browser-based presentation. Trigger keywords: Reveal.js, reveal js, HTML presentation, slide deck, browser presentation, revealjs, polished slides, presentation framework.
---

# Reveal.js Skill

## Overview
Generate polished professional presentations using the Reveal.js HTML framework. Output a self-contained HTML file that runs in any browser.

## Base Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Presentation Title</title>
  <link rel="stylesheet" href="https://unpkg.com/reveal.js/dist/reveal.css">
  <link rel="stylesheet" href="https://unpkg.com/reveal.js/dist/theme/black.css">
  <link rel="stylesheet" href="https://unpkg.com/reveal.js/plugin/highlight/monokai.css">
  <style>
    .reveal h1, .reveal h2 { text-transform: none; }
    .reveal .slides section { text-align: left; }
    .accent { color: #e85d04; }
    .small { font-size: 0.7em; }
    .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; }
  </style>
</head>
<body>
<div class="reveal">
  <div class="slides">

    <!-- Title Slide -->
    <section>
      <h1>Presentation Title</h1>
      <p class="small">Subtitle or author · Date</p>
    </section>

    <!-- Agenda -->
    <section>
      <h2>Agenda</h2>
      <ol>
        <li>Topic 1</li>
        <li>Topic 2</li>
        <li>Topic 3</li>
      </ol>
    </section>

    <!-- Content with fragments -->
    <section>
      <h2>Key Points</h2>
      <ul>
        <li class="fragment">Point appears on click</li>
        <li class="fragment">Second point</li>
        <li class="fragment highlight-red">Highlighted point</li>
      </ul>
    </section>

    <!-- Two column layout -->
    <section>
      <h2>Comparison</h2>
      <div class="grid-2">
        <div>
          <h3 class="accent">Before</h3>
          <ul class="small"><li>Item A</li><li>Item B</li></ul>
        </div>
        <div>
          <h3 class="accent">After</h3>
          <ul class="small"><li>Item C</li><li>Item D</li></ul>
        </div>
      </div>
    </section>

    <!-- Code slide -->
    <section>
      <h2>Code Example</h2>
      <pre><code class="language-python" data-trim>
def hello_world():
    print("Hello, Reveal.js!")
      </code></pre>
    </section>

    <!-- Vertical slides (sub-sections) -->
    <section>
      <section><h2>Section 3</h2><p>Press ↓ for details</p></section>
      <section><h2>Detail 1</h2><p>Sub-slide content</p></section>
      <section><h2>Detail 2</h2><p>More details</p></section>
    </section>

    <!-- Closing slide -->
    <section>
      <h1>Thank You</h1>
      <p>Questions?</p>
    </section>

  </div>
</div>

<script src="https://unpkg.com/reveal.js/dist/reveal.js"></script>
<script src="https://unpkg.com/reveal.js/plugin/highlight/highlight.js"></script>
<script src="https://unpkg.com/reveal.js/plugin/notes/notes.js"></script>
<script>
  Reveal.initialize({
    hash: true,
    transition: "slide",
    backgroundTransition: "fade",
    plugins: [RevealHighlight, RevealNotes],
    width: 1280,
    height: 720,
  });
</script>
</body>
</html>
```

## Themes Available
`black` | `white` | `league` | `beige` | `sky` | `night` | `serif` | `simple` | `solarized` | `moon` | `blood`

## Keyboard Shortcuts
- `Space` / `→` — Next slide
- `↑↓` — Vertical slides
- `F` — Fullscreen
- `S` — Speaker notes view
- `O` — Overview mode

## Output Format
Single `presentation.html` file. Opens in any browser. No server required.

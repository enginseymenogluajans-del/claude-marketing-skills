---
name: plugin-authoring
description: Use when the user asks to create, build, debug, or validate a Claude Code plugin, write plugin schemas, create plugin templates, or understand Claude Code plugin architecture. Trigger keywords: Claude Code plugin, plugin authoring, create plugin, plugin schema, plugin validation, PLUGIN.md, plugin template, debug plugin, Claude plugin.
---

# Plugin Authoring Skill

## Overview
Guidance for creating and debugging Claude Code plugins — schemas, templates, and validation workflows.

## Plugin Architecture

```
my-plugin/
├── PLUGIN.md          # Plugin manifest + instructions
├── skills/            # Bundled skills
│   └── my-skill/
│       └── SKILL.md
├── agents/            # Bundled subagents
│   └── my-agent.md
├── scripts/           # Execution scripts
│   └── run.py
└── package.json       # Optional: npm package metadata
```

## PLUGIN.md Schema

```yaml
---
name: my-plugin
version: 1.0.0
description: What this plugin provides and when to use it.
author: Your Name
skills:
  - skills/my-skill
agents:
  - agents/my-agent
permissions:
  - bash
  - read
  - write
settings:
  env:
    MY_API_KEY: ""     # User must set this
---

# Plugin Title

## Overview
[What this plugin does]

## Setup
1. [Setup step 1]
2. [Setup step 2]

## Usage
[How to use the plugin]
```

## Skill Schema (within plugin)

```yaml
---
name: skill-name
description: |
  Use when the user asks to [action]. 
  Trigger keywords: [word1], [word2], [word3].
  ALWAYS use this skill when [specific condition].
version: 1.0.0
---
```

## Plugin Validation Checklist

```bash
# 1. Validate PLUGIN.md YAML frontmatter
python3 -c "
import yaml
with open('PLUGIN.md') as f:
    content = f.read()
# Extract frontmatter between --- markers
parts = content.split('---')
if len(parts) >= 3:
    meta = yaml.safe_load(parts[1])
    required = ['name', 'version', 'description']
    missing = [k for k in required if k not in meta]
    if missing:
        print(f'MISSING: {missing}')
    else:
        print('Frontmatter OK')
"

# 2. Validate all referenced skills exist
ls skills/

# 3. Test skill trigger
# Run Claude Code and say: "test skill trigger phrase"
```

## Debugging Plugin Issues

### Skill not triggering
1. Check description starts with "Use when the user asks to..."
2. Add more specific trigger keywords
3. Make description more assertive ("ALWAYS use this skill when...")
4. Keep description under 200 words

### Permission denied errors
Add to PLUGIN.md permissions:
```yaml
permissions:
  - bash          # Run shell commands
  - read          # Read files
  - write         # Write files
  - network       # Make HTTP requests
```

### Environment variable not available
```yaml
settings:
  env:
    API_KEY: ""   # Prompt user to set this
```

## Publishing

### npm package
```json
{
  "name": "@username/my-claude-plugin",
  "version": "1.0.0",
  "description": "Claude Code plugin for...",
  "keywords": ["claude-code", "claude-plugin"],
  "files": ["PLUGIN.md", "skills/", "agents/", "scripts/"],
  "claude": {
    "plugin": true
  }
}
```

### Install commands
```bash
# From npm
/plugin install @username/my-claude-plugin

# From local path
/plugin add ./my-plugin

# From GitHub
/plugin install github:username/repo
```

## Output Format
- Complete PLUGIN.md with proper schema
- Skill SKILL.md files with optimized descriptions
- Validation checklist results
- Installation command for the plugin

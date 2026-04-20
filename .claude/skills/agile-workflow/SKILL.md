---
name: agile-workflow
description: Use when the user asks to manage a project agilely, break down scope, create epics and stories, prioritize with RICE, plan sprints, or coordinate feature delivery. Trigger keywords: agile, sprint, epic, user story, RICE prioritization, backlog, sprint planning, scope decomposition, story points, kanban, project management.
---

# Agile Workflow Skill

## Overview
Scope decomposition, epic/story coordination, RICE prioritization, and sprint management.

## Scope Decomposition

### Epic → Story → Task hierarchy
```
Epic: User Authentication System
├── Story: User can register with email
│   ├── Task: Create registration form UI
│   ├── Task: Implement API endpoint POST /auth/register
│   ├── Task: Add email validation
│   └── Task: Write unit tests
├── Story: User can log in
│   ├── Task: Create login form
│   ├── Task: Implement JWT token generation
│   └── Task: Handle "remember me" option
└── Story: User can reset password
    ├── Task: Implement forgot password flow
    └── Task: Create email reset link system
```

### User Story Format
```
As a [user type],
I want to [action],
So that [benefit].

Acceptance Criteria:
- [ ] Given [context], when [action], then [outcome]
- [ ] Edge case: [scenario]
- [ ] Error case: [scenario]
```

## RICE Prioritization

**Score = (Reach × Impact × Confidence) / Effort**

| Factor | Scale |
|--------|-------|
| Reach | Users affected per quarter (number) |
| Impact | 0.25 = minimal, 0.5 = low, 1 = medium, 2 = high, 3 = massive |
| Confidence | 50% = low, 80% = medium, 100% = high |
| Effort | Person-months |

```
Feature A: (500 × 2 × 0.8) / 0.5 = 1,600  ← Do first
Feature B: (200 × 3 × 0.5) / 2.0  =   150
Feature C: (1000 × 1 × 1.0) / 4.0 =   250
```

## Sprint Planning Template

```markdown
## Sprint [N] — [Start Date] to [End Date]

**Sprint Goal**: [One sentence describing what we're delivering]

**Capacity**: [X] story points / [N] team members

### Committed Stories
| Story | Points | Assignee | Status |
|-------|--------|----------|--------|
| User registration | 5 | Dev A | In Progress |
| Login flow | 3 | Dev B | Todo |
| Password reset | 8 | Dev A | Todo |

**Total**: 16 points

### Definition of Done
- [ ] Code reviewed and approved
- [ ] Unit tests passing (>80% coverage)
- [ ] Integration tests passing
- [ ] Deployed to staging
- [ ] PM acceptance
```

## Backlog Grooming

1. **Review** existing stories for staleness
2. **Estimate** unestimated stories using Planning Poker or T-shirt sizing
3. **Split** stories > 8 points into smaller ones
4. **Reprioritize** using RICE scores
5. **Remove** stories that are no longer relevant

## Story Point Reference
| Points | Meaning |
|--------|---------|
| 1 | Trivial change, < 1 hour |
| 2 | Small, well-understood, 2-4 hours |
| 3 | Standard task, half day |
| 5 | Complex, full day |
| 8 | Multi-day, some unknowns |
| 13 | Split this story |

## Output Format
- Epic breakdown as hierarchical list
- Prioritized backlog as table with RICE scores
- Sprint plan with story points and assignments
- Definition of Done checklist

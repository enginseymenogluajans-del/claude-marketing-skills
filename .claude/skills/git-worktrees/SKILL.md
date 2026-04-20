---
name: git-worktrees
description: Use when the user asks to create a git worktree, work on multiple branches in parallel, isolate feature work, or create a separate working directory for a branch without switching. Trigger keywords: git worktree, worktree, parallel branches, isolated branch, multiple branches, work on two branches.
---

# Git Worktrees Skill

## Overview
Create isolated git worktrees for parallel branch work. Each worktree has its own working directory and can be on a different branch — no stashing, no branch switching required.

## Steps

### Create a worktree
```bash
# Create worktree for existing branch
git worktree add ../project-feature-branch feature-branch

# Create worktree + new branch
git worktree add -b new-feature ../project-new-feature main

# Create worktree at specific path
git worktree add /path/to/worktree branch-name
```

### Smart directory naming convention
Use a consistent pattern: `../[repo-name]-[branch-name]`
```bash
# Get repo name
REPO=$(basename $(git rev-parse --show-toplevel))
BRANCH="feature-login"
git worktree add "../${REPO}-${BRANCH}" "${BRANCH}"
```

### List active worktrees
```bash
git worktree list
```

### Remove a worktree (after merging)
```bash
# Remove the directory first or use --force
git worktree remove ../project-feature-branch

# Force remove if directory has changes
git worktree remove --force ../project-feature-branch

# Clean up stale worktree references
git worktree prune
```

## Safety Checks Before Creating
```bash
# Confirm branch exists
git branch --list feature-branch

# Check no existing worktree for this branch
git worktree list | grep feature-branch

# Verify target path doesn't exist
ls ../project-feature-branch 2>/dev/null && echo "EXISTS - choose different path"
```

## Parallel Workflow Example
```bash
# Terminal 1: main development
cd ~/projects/myapp
git checkout main

# Terminal 2: hotfix (worktree)
cd ~/projects/myapp-hotfix
# Already on hotfix branch, independent from Terminal 1

# Terminal 3: new feature (worktree)
cd ~/projects/myapp-new-login
# Already on feature branch
```

## Output Format
- Show the worktree creation command used
- Confirm path created and branch checked out
- List all active worktrees after creation

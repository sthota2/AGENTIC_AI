---
name: git-workflow
description: "Use when managing git branches, pull requests, and promoting changes between dev and main branches. Handles branch creation, merging, rebasing, creating PRs, resolving merge conflicts, enforcing the dev-to-main promotion workflow with GitHub Actions, and maintaining clean commit history."
---

# Git Workflow Skill

Manages the branching strategy and change promotion workflow for this project. The standard flow is: develop on `dev`, then promote to `main` via merge or PR.

## Branch Strategy

```
main (production/stable)
  ↑ promoted from dev
dev (development)
  → active development branch
feature/<name> (optional short-lived branches off dev)
```

## Common Commands

### Create a feature branch from dev

```bash
git checkout dev
git pull origin dev
git checkout -b feature/<feature-name>
```

### Commit and push changes

```bash
git add -A
export GIT_AUTHOR_NAME="sthota2"
export GIT_AUTHOR_EMAIL="sthota2@users.noreply.github.com"
export GIT_COMMITTER_NAME="sthota2"
export GIT_COMMITTER_EMAIL="sthota2@users.noreply.github.com"
git commit -m "<type>: <description>"
git push origin feature/<feature-name>
```

Commit types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`

### Merge dev into main (promote changes)

This is automated via GitHub Actions. Trigger manually when needed:

```bash
git checkout main
git pull origin main
git merge dev --no-edit
git push origin main
```

## GitHub Actions Workflow Promotion

Changes are promoted from `dev` to `main` automatically via CI/CD pipeline. The workflow file is located at `.github/workflows/promote.yml`.

To promote changes:
1. Ensure all commits are pushed to `dev`
2. Create or update PR from `dev` → `main` (if using PR-based promotion)
3. Wait for CI checks to pass
4. Merge the PR

## Pushing and Updating History

When force-pushing after amendments:

```bash
git push origin dev --force
git push origin main --force  # Only after merge
```

Use `--force` sparingly. Prefer rebasing over force-pushing on shared branches.

## Branch Protection

- `main` branch should remain protected (not configured during initial setup but recommended)
- All promoted changes should have clean history with meaningful commit messages

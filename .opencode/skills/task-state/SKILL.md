---
name: task-state
description: "Use when starting, pausing, resuming, or switching project tasks. Maintains resumable state in docs/PROJECT_STATE.md so interrupted work can continue from exactly where it stopped. Syncs task state with Jira (SOFT-*) and GitHub branches. ALWAYS read before starting work and update before pausing."
---

# Task State Skill

Keeps a durable, resumable record of project work so any task can be continued
after an interruption (context loss, restarts, handoffs).

## The State File

`docs/PROJECT_STATE.md` is the single source of truth for *where work is at*.
Jira (`SOFT-*`) holds the *detailed* requirements/history; GitHub holds the code.
This file is the short, human + agent readable index that ties them together.

## Rules

- **Read first**: At the start of any work session, read `docs/PROJECT_STATE.md`,
  then `git status` and `git log --oneline -5`, before touching code.
- **Write on pause**: Before stopping, switching tasks, or ending a session,
  update the file. Never leave active work undocumented.
- **Keep it short**: One row per task. Link the Jira key and branch. Detail
  lives in Jira.
- **DRY**: Reference Jira keys and branch names instead of duplicating status
  text. Don't restate what the code already shows.
- **Security**: Never write tokens, passwords, or secrets into the state file.

## File Structure

```
## Current Focus        # the one thing being worked on now
## In Progress          # Key | Task | Branch | Next step
## Blocked              # Key | Task | Blocker
## Next                 # queued work (checkbox list)
## Done                 # completed (checkbox list)
## Resume Recipe        # how to pick up
```

Always refresh `Last updated:` and `Updated by:` at the top on every edit.

## When to Update

| Event | Action |
|---|---|
| Start a task | Move it to `In Progress`, set Branch + Next step; set `Current Focus` |
| Pause / interrupt | Update `Next step` with the exact resumption point |
| Hit a blocker | Move to `Blocked` with the blocker described |
| Finish a task | Move to `Done`, clear `Current Focus` if needed |
| Switch tasks | Update `Current Focus`; leave prior task's `Next step` accurate |

## Resuming

1. Read `docs/PROJECT_STATE.md`.
2. Pick the `Current Focus` (or top `In Progress`) row.
3. `git checkout <Branch>`, `git pull`, check Jira `<Key>` for detail.
4. Continue from `Next step`.
5. Update the file before pausing again.

## Jira Alignment

- Task **state** here mirrors Jira status: `To Do → In Progress → In Review → Done`.
- Use the `SOFT-<num>` key in the Key column to link to Jira.
- Branch names follow `<KEY>/<kebab-case>` (see `git-workflow` and
  `jira-project-tracker`).

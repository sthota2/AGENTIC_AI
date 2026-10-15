# Project State

Single source of truth for resumable work. Update this file whenever a task
starts, changes state, or pauses. Keep it short — link to Jira for detail.

Last updated: 2026-10-15
Updated by: opencode

## Current Focus

- **SOFT-1** — Enable auto-commit to `dev` by default (In Progress)

## In Progress

| Key | Task | Branch | Next step |
|---|---|---|---|
| SOFT-1 | Jira ↔ GitHub task tracking | `dev` | Verify `jira-sync.yml` adds comments on push referencing an issue key |
| SOFT-1 | Auto-commit to `dev` | `dev` | Restart opencode to load `auto-commit.ts`; verify a commit appears after an edit |

## Blocked

| Key | Task | Blocker |
|---|---|---|
| — | — | — |

## Next

- [ ] Create first project feature issue in Jira (SOFT-*)
- [ ] Verify `jira-sync.yml` adds comments on push referencing an issue key
- [ ] Confirm auto-commit fires after `edit`/`write` (post-restart)

## Done

- [x] Git repo initialized, `main` + `dev` branches, remote connected
- [x] README, .gitignore added
- [x] Dev → Main promotion workflow
- [x] Jira integration (client, skill, sync workflow)
- [x] Test task created (SOFT-1)
- [x] Resumable task-state skill + PROJECT_STATE
- [x] Auto-commit to `dev` (plugin + script + skill)

## Resume Recipe

1. Read this file, then `git status` and `git log --oneline -5`.
2. Check the `Current Focus` / `In Progress` rows against Jira
   (`https://tsandyk8s.atlassian.net/browse/<KEY>`).
3. Continue from the `Next step` column of the top in-progress row.
4. Update this file when pausing (state, branch, next step).

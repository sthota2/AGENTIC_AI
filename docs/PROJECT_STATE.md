# Project State

Single source of truth for resumable work. Update this file whenever a task
starts, changes state, or pauses. Keep it short — link to Jira for detail.

Last updated: 2026-10-15
Updated by: opencode

## Current Focus

- **SOFT-1** — Jira ↔ GitHub task tracking (In Progress)

## In Progress

| Key | Task | Branch | Next step |
|---|---|---|---|
| SOFT-1 | Jira ↔ GitHub task tracking | `dev` | Grant the token account comment permission on SOFT; re-verify sync comment |
| SOFT-1 | Verification-gated auto-commit | `dev` | Restart opencode to load `auto-commit.ts`; confirm commit only after `verify.sh` passes |

## Blocked

| Key | Task | Blocker |
|---|---|---|
| SOFT-1 | Jira sync comments | Token account ("Sandeep T") lacks permission to comment on SOFT-1 |

## Next

- [ ] Create first project feature issue in Jira (SOFT-*)
- [ ] Confirm auto-commit fires after `edit`/`write`/`bash` (post-restart)
- [ ] Set `VERIFY_CMD` for the project once a test suite exists

## Done

- [x] Git repo initialized, `main` + `dev` branches, remote connected
- [x] README, .gitignore added
- [x] Dev → Main promotion workflow
- [x] Jira integration (client, skill, sync workflow)
- [x] Test task created (SOFT-1)
- [x] Resumable task-state skill + PROJECT_STATE
- [x] Auto-commit to `dev` (plugin + script + skill)
- [x] Verification-gated auto-commit (`scripts/verify.sh`)
- [x] Fixed promote + jira-sync workflows; both green

## Resume Recipe

1. Read this file, then `git status` and `git log --oneline -5`.
2. Check the `Current Focus` / `In Progress` rows against Jira
   (`https://tsandyk8s.atlassian.net/browse/<KEY>`).
3. Continue from the `Next step` column of the top in-progress row.
4. Update this file when pausing (state, branch, next step).

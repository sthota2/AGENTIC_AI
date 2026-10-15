# Project State

Single source of truth for resumable work. Update this file whenever a task
starts, changes state, or pauses. Keep it short — link to Jira for detail.

Last updated: 2026-10-15
Updated by: opencode

## Current Focus

- **SOFT-2** — Jira ↔ GitHub task tracking (In Progress)

## In Progress

| Key | Task | Branch | Next step |
|---|---|---|---|
| SOFT-2 | Jira ↔ GitHub task tracking | `dev` | Verify `jira-sync.yml` posts a comment on SOFT-2 (pipeline proof) |
| SOFT-1 | Verification-gated auto-commit | `dev` | Restart opencode to load `auto-commit.ts`; confirm commit only after `verify.sh` passes |

## Blocked

_None._

### Resolved: Jira comment permission (SOFT-1)

The comment permission is **correctly configured**; the failure is specific to
issue `SOFT-1`. Evidence from `.github/workflows/jira-diagnose.yml`:

- Project `SOFT`: `ADD_COMMENTS=true`, `ADMINISTER_PROJECTS=true` (account is
  project Administrator, role `10020`).
- A freshly created issue (`SOFT-2`, id `13269`) accepts comments/edits with the
  **same token** (`HTTP 201`).
- `SOFT-1` (id `13268`) rejects **both** comment and edit (`HTTP 400 —
  "you do not have the permission to comment on this issue."`), yet is
  byte-for-byte identical to SOFT-2: same project, issue type `10020`
  ("Task", not subtask), status `10015` ("To Do"), `security=None`,
  `issuerestriction={}`, no entity properties, same reporter/creator.
- `GET /mypermissions?issueKey=SOFT-1` returns an **empty** permission set,
  while `?issueKey=SOFT-2` returns the full set.

Conclusion: per-issue permission cache/index inconsistency on `SOFT-1`
(not a grantable setting). Remediation options: reindex Jira
(Settings → System → Indexing), or ignore SOFT-1 and use normally created
issues (which work).

## Next

- [ ] Expect a `Pushed` comment on SOFT-2 from `jira-sync.yml` (pipeline proof)
- [ ] Decide on SOFT-1: reindex Jira, or delete/ignore the test issue
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
- [x] Diagnosed Jira comment denial — root cause isolated to issue SOFT-1 (per-issue permission anomaly), not configuration

## Resume Recipe

1. Read this file, then `git status` and `git log --oneline -5`.
2. Check the `Current Focus` / `In Progress` rows against Jira
   (`https://tsandyk8s.atlassian.net/browse/<KEY>`).
3. Continue from the `Next step` column of the top in-progress row.
4. Update this file when pausing (state, branch, next step).

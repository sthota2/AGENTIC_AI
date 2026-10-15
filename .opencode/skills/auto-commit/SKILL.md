---
name: auto-commit
description: "Use when modifying files in this project. All changes are automatically committed to the dev branch by default via an opencode plugin + scripts/auto-commit.sh. Explains the auto-commit behavior, safe-by-design guarantees, and how to override or disable it."
---

# Auto-Commit to dev Skill

By default, every file change made through the agent is auto-committed to the
`dev` branch. This preserves work across interruptions so tasks resume exactly
where they left off (see `task-state`).

## How it works

- `.opencode/plugin/auto-commit.ts` hooks `tool.execute.after` for the
  `edit`, `write`, and `patch` tools.
- It calls `scripts/auto-commit.sh` — the single source of truth (DRY).
- The script stages and commits changes to `dev`, or carries uncommitted
  work onto `dev` when the current branch differs.

## Guarantees (safe by design)

- **Never loses work.** If switching to `dev` is not possible, changes are
  committed on the current branch instead.
- **No empty commits.** A clean tree is a no-op.
- **No secrets.** Only the working tree is committed; tokens/passwords are
  never written (env/Secrets only — see `jira-integration`).
- **Local only.** Auto-commit does not push. Promotion to `main` happens via
  `.github/workflows/promote-dev-to-main.yml` on push.
- **Best-effort.** Failures never break the tool call.

## Override / disable

- Target a different branch: `export AUTO_COMMIT_BRANCH=feature/x`.
- Temporarily disable: remove/rename `.opencode/plugin/auto-commit.ts`
  (requires an opencode restart to take effect).

## Commit format

Auto-commits use:
```
chore(auto): save progress on <branch>
```
Authored as `sthota2 <sthota2@users.noreply.github.com>`.

## Notes

- Plugins load at startup. After adding/removing the plugin, **restart opencode**.
- Manual commits are still fine; auto-commit simply ensures nothing is lost.

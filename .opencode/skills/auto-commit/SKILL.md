---
name: auto-commit
description: "Use when modifying files in this project. Changes are auto-committed to the dev branch ONLY after they are tested and verified (scripts/verify.sh passes). Explains the verification gate, safe-by-design guarantees, and how to override or disable it."
---

# Auto-Commit to dev (verification-gated) Skill

Changes are auto-committed to the `dev` branch **only when they are tested and
verified**. Unverified work is left uncommitted so it is never recorded as good.
This preserves work across interruptions (see `task-state`) without polluting
history with broken states.

## How it works

1. `.opencode/plugin/auto-commit.ts` hooks `tool.execute.after` for
   `edit`, `write`, `patch`, and `bash`.
2. It calls `scripts/auto-commit.sh` — the single source of truth (DRY).
3. `auto-commit.sh` first runs `scripts/verify.sh` (the verification gate).
   - **verify passes** → stage + commit to `dev`.
   - **verify fails** → do nothing (changes stay uncommitted).
4. Committing from another branch carries the work onto `dev` when possible.

## Verification gate (`scripts/verify.sh`)

Runs lightweight, stable checks by default:
- Rejects whitespace errors and conflict markers (tracked and untracked).
- `bash -n` syntax-checks changed shell scripts.
- `ast.parse` syntax-checks changed Python files (no bytecode written).
- Runs project tests when `VERIFY_CMD` is set (e.g. `pytest -q`, `npm test`).

Set the project test command once (DRY):
```bash
export VERIFY_CMD="pytest -q"
```

## Guarantees (safe by design)

- **Verified only.** No commit unless `scripts/verify.sh` exits 0.
- **Never loses work.** Verification failure leaves changes intact on disk.
- **No empty commits.** A clean tree is a no-op.
- **No secrets.** Only the working tree is committed; tokens/passwords are
  never written (env/Secrets only — see `jira-integration`).
- **Local only.** Auto-commit does not push. Promotion to `main` happens via
  `.github/workflows/promote-dev-to-main.yml` on push.
- **Best-effort.** Failures never break the tool call.

## Override / disable

- Target a different branch: `export AUTO_COMMIT_BRANCH=feature/x`.
- Skip the verification gate (not recommended): `export AUTO_COMMIT_SKIP_VERIFY=1`.
- Disable entirely: remove/rename `.opencode/plugin/auto-commit.ts`
  (requires an opencode restart).

## Commit format

```
chore(auto): save verified progress on <branch>
```
Authored as `sthota2 <sthota2@users.noreply.github.com>`.

## Notes

- Plugins load at startup. After adding/removing the plugin, **restart opencode**.
- Manual commits are still fine; auto-commit only records verified states.

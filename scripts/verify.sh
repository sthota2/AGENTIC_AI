#!/usr/bin/env bash
#
# Verification gate for auto-commit. Exit 0 = verified, safe to commit.
#
# Single source of truth (DRY) for "is this change good enough to record?".
# Configure project checks with VERIFY_CMD (e.g. "npm test" or "pytest -q").
# When unset, lightweight built-in integrity checks run instead.
#
# Security: never prints secrets; only runs local commands.

set -uo pipefail

repo_root="$(git rev-parse --show-toplevel 2>/dev/null || true)"
[ -n "$repo_root" ] || exit 0  # nothing to verify outside a git work tree
cd "$repo_root" || exit 1

changed_files() {
  { git diff --name-only
    git diff --cached --name-only
    git ls-files --others --exclude-standard
  } | sort -u
}

status=0

# 1a. Reject whitespace errors in tracked working changes.
if ! git diff --check >/dev/null 2>&1 || ! git diff --cached --check >/dev/null 2>&1; then
  echo "verify: whitespace errors detected" >&2
  status=1
fi

# 1b. Reject conflict markers in any changed file (tracked or untracked).
while IFS= read -r f; do
  [ -f "$f" ] || continue
  if grep -qE '^(<<<<<<< |=======$|>>>>>>> )' "$f" 2>/dev/null; then
    echo "verify: conflict marker in $f" >&2
    status=1
  fi
done < <(changed_files)

# 2. Syntax-check changed shell scripts.
while IFS= read -r f; do
  case "$f" in
    *.sh|*.bash)
      if ! bash -n "$f" >/dev/null 2>&1; then
        echo "verify: shell syntax error in $f" >&2
        status=1
      fi
      ;;
  esac
done < <(changed_files)

# 3. Syntax-check changed Python files (ast.parse avoids bytecode output).
while IFS= read -r f; do
  case "$f" in
    *.py)
      if ! python3 -c 'import ast,sys; ast.parse(open(sys.argv[1], encoding="utf-8").read())' "$f" >/dev/null 2>&1; then
        echo "verify: python syntax error in $f" >&2
        status=1
      fi
      ;;
  esac
done < <(changed_files)

# 4. Project test/verify command (optional).
if [ -n "${VERIFY_CMD:-}" ]; then
  if ! bash -c "$VERIFY_CMD" >/dev/null 2>&1; then
    echo "verify: VERIFY_CMD failed: $VERIFY_CMD" >&2
    status=1
  fi
fi

exit $status

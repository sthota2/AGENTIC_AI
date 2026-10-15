#!/usr/bin/env bash
#
# Auto-commit working changes to the default branch (dev by default).
# Safe by design: never discards work. If the tree is dirty, changes are
# carried onto the target branch when possible; otherwise they are committed
# on the current branch.
#
# Override target branch with AUTO_COMMIT_BRANCH=<name>.
# Exit codes: 0 always (best-effort, non-fatal).

set -uo pipefail

TARGET="${AUTO_COMMIT_BRANCH:-dev}"
AUTHOR_NAME="${GIT_AUTHOR_NAME:-sthota2}"
AUTHOR_EMAIL="${GIT_AUTHOR_EMAIL:-sthota2@users.noreply.github.com}"

git rev-parse --is-inside-work-tree >/dev/null 2>&1 || exit 0

# Anything to commit?
if git diff --quiet && git diff --cached --quiet \
   && [ -z "$(git ls-files --others --exclude-standard)" ]; then
  exit 0
fi

current="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo '')"

# Steer work onto the target branch when possible (carries local changes).
if [ "$current" != "$TARGET" ]; then
  if git show-ref --verify --quiet "refs/heads/$TARGET"; then
    git checkout "$TARGET" >/dev/null 2>&1 || true
  else
    git checkout -b "$TARGET" >/dev/null 2>&1 || true
  fi
  current="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo '')"
fi

git add -A
git -c user.name="$AUTHOR_NAME" -c user.email="$AUTHOR_EMAIL" \
  commit -m "chore(auto): save progress on ${current}" >/dev/null 2>&1 || true

exit 0

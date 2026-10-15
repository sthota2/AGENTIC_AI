// Verification-gated auto-commit.
//
// Commits project changes to the dev branch ONLY when scripts/verify.sh
// passes (tests/checks are green). All logic lives in scripts/auto-commit.sh
// (single source of truth / DRY).
//
// Triggers after file edits and after bash runs, so a commit is recorded once
// a change has been tested and verified.
//
// Requires an opencode restart to take effect once installed.

const TRIGGER_TOOLS = new Set(["edit", "write", "patch", "bash"]);

export const AutoCommitDev = async ({ $, directory }) => ({
  "tool.execute.after": async (input) => {
    if (!TRIGGER_TOOLS.has(input.tool)) return;
    try {
      await $(`bash ${directory}/scripts/auto-commit.sh`)
        .cwd(directory)
        .nothrow()
        .quiet();
    } catch {
      // best-effort: never break a tool call because of auto-commit
    }
  },
});

export default AutoCommitDev;

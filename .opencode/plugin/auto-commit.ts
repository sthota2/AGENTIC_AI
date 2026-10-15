// Auto-commit project changes to the dev branch after file edits.
// Delegates all logic to scripts/auto-commit.sh (single source of truth / DRY).
//
// Requires an opencode restart to take effect once installed.

const WRITE_TOOLS = new Set(["edit", "write", "patch"]);

export const AutoCommitDev = async ({ $, directory }) => ({
  "tool.execute.after": async (input) => {
    if (!WRITE_TOOLS.has(input.tool)) return;
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

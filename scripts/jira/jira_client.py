import os
from typing import Any, Dict, List, Optional

from atlassian import Jira

DEFAULT_URL = "https://tsandyk8s.atlassian.net"


def _required_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


class JiraClient:
    """Thin, reusable wrapper around the Jira REST API.

    Authentication is token-based and read from the environment only.
    No credentials are ever stored on the instance or logged.
    """

    def __init__(self, url: Optional[str] = None) -> None:
        # Token is passed straight through and not retained as an attribute.
        self.jira = Jira(
            url=url or os.getenv("JIRA_URL", DEFAULT_URL),
            username=_required_env("JIRA_USERNAME"),
            password=_required_env("JIRA_API_TOKEN"),
            cloud=True,
        )

    def get_issue(self, key: str) -> Dict[str, Any]:
        return self.jira.issue(key)

    def search_issues(
        self, jql: str, fields: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        return self.jira.jql(jql, fields=fields)

    def create_issue(self, fields: Dict[str, Any]) -> Dict[str, Any]:
        return self.jira.create_issue(fields=fields)

    def transition_issue(self, key: str, transition_id: str) -> None:
        self.jira.issue_transition(key, transition_id)

    def add_comment(self, key: str, comment: str) -> None:
        self.jira.issue_add_comment(key, comment)


def main() -> int:
    import sys

    if len(sys.argv) < 2:
        print("Usage: python jira_client.py <issue-key>")
        return 1
    issue = JiraClient().get_issue(sys.argv[1])
    print(issue["fields"]["summary"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

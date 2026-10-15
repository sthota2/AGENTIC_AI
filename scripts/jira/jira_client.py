import os
from typing import Any, Dict, List, Optional

from atlassian import Jira


class JiraClient:
    def __init__(self):
        self.url = os.getenv("JIRA_URL", "https://tsandyk8s.atlassian.net")
        self.username = os.getenv("JIRA_USERNAME")
        self.api_token = os.getenv("JIRA_API_TOKEN")
        if not self.username or not self.api_token:
            raise ValueError("JIRA_USERNAME and JIRA_API_TOKEN must be set")
        self.jira = Jira(
            url=self.url,
            username=self.username,
            password=self.api_token,
            cloud=True,
        )

    def get_issue(self, key: str) -> Dict[str, Any]:
        return self.jira.issue(key)

    def search_issues(self, jql: str, fields: Optional[List[str]] = None) -> Dict[str, Any]:
        return self.jira.jql(jql, fields=fields)

    def create_issue(self, fields: Dict[str, Any]) -> Dict[str, Any]:
        return self.jira.create_issue(fields=fields)

    def transition_issue(self, key: str, transition_id: str) -> None:
        self.jira.issue_transition(key, transition_id)

    def add_comment(self, key: str, comment: str) -> None:
        self.jira.issue_add_comment(key, comment)


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python jira_client.py <issue-key>")
        sys.exit(1)
    jc = JiraClient()
    issue = jc.get_issue(sys.argv[1])
    print(issue["fields"]["summary"])

import os
import sys

from atlassian import Jira


def main():
    jira_url = os.getenv('JIRA_URL', 'https://tsandyk8s.atlassian.net')
    jira_user = os.getenv('JIRA_USERNAME')
    jira_token = os.getenv('JIRA_API_TOKEN')

    if not jira_user or not jira_token:
        print("Error: JIRA_USERNAME and JIRA_API_TOKEN environment variables must be set")
        sys.exit(1)

    jira = Jira(url=jira_url, username=jira_user, password=jira_token, cloud=True)

    # Create a test task
    fields = {
        "project": {"key": "SOFT"},
        "summary": "Test task - AGENTIC_AI Jira integration check",
        "description": "This is a test task created to verify Jira integration is working correctly.",
        "issuetype": {"name": "Task"},
    }

    try:
        issue = jira.create_issue(fields=fields)
        print(f"Successfully created issue: {issue['key']}")
        print(f"URL: {jira_url}/browse/{issue['key']}")
    except Exception as e:
        print(f"Error creating issue: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

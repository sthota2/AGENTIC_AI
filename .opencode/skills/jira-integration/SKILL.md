---
name: jira-integration
description: "Use when working with Jira issues for the AGENTIC_AI project. Handles creating, updating, transitioning, commenting, and syncing Jira tickets with Git commits and GitHub PRs. Integrates with the SOFT project at tsandyk8s.atlassian.net."
---

# Jira Integration Skill

This skill provides tools and workflows to integrate the AGENTIC_AI project with Jira for task tracking.

## Setup Requirements

The following environment variables must be configured:

```bash
export JIRA_URL="https://tsandyk8s.atlassian.net"
export JIRA_USERNAME="<your-email@domain.com>"
export JIRA_API_TOKEN="<your-api-token>"
export JIRA_PROJECT_KEY="SOFT"
```

Generate API token at: https://id.atlassian.com/manage-profile/security/api-tokens

## Available Scripts

Scripts are located in `scripts/jira/`:

- `jira_client.py` - Core client for Jira API operations
- Use `jira-sync-workflow.yml` (GitHub Actions) for automatic commit/PR tracking

## Common Workflows

### Link commits to Jira issues
Include issue keys in commit messages:
```bash
git commit -m "SOFT-123: Add README and .gitignore"
```

### Update Jira when PR is merged
The GitHub Actions workflow automatically adds comments to linked Jira issues when PRs are merged into main/dev.

### Search for issues
```bash
python3 -c "
from scripts.jira.jira_client import JiraClient
jc = JiraClient()
results = jc.search_issues('project=SOFT AND status=\"To Do\"')
for r in results['issues']:
    print(r['key'] + ': ' + r['fields']['summary'])
"
```

## Tips

- Always use the exact project key `SOFT`
- Include issue key in branch names: `SOFT-123/feature-description`
- Issue keys in commit messages and PR titles are auto-detected

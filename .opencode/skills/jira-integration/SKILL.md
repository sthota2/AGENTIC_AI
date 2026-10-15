---
name: jira-integration
description: "Use for low-level Jira API access in AGENTIC_AI via the shared client. Token-based auth from environment only (no passwords), DRY single-client design, stable open-source library (atlassian-python-api)."
---

# Jira Integration Skill

Low-level Jira API access. For task workflow/tracking conventions, see `jira-project-tracker`.

## Security
- Auth via **API token** from env: `JIRA_USERNAME`, `JIRA_API_TOKEN`. Never hardcode or commit secrets.
- `JIRA_URL` fixed: `https://tsandyk8s.atlassian.net`
- Secrets live in GitHub Actions Secrets or a gitignored `.env`. Never echo tokens.
- Least privilege; rotate tokens regularly.

## DRY Design
- **Single client**: all access goes through `scripts/jira/jira_client.py` (`JiraClient`).
- No duplicate HTTP calls or ad-hoc auth code elsewhere.

## Config
```bash
export JIRA_URL="https://tsandyk8s.atlassian.net"
export JIRA_USERNAME="<your-email>"
export JIRA_API_TOKEN="<token>"   # https://id.atlassian.com/manage-profile/security/api-tokens
export JIRA_PROJECT_KEY="SOFT"
```

## Client API
`scripts/jira/jira_client.py` exposes:
- `get_issue(key)`
- `search_issues(jql, fields=None)`
- `create_issue(fields)`
- `transition_issue(key, transition_id)`
- `add_comment(key, comment)`

## Example
```bash
python3 scripts/jira/jira_client.py SOFT-1
```

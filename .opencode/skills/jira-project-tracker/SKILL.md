---
name: jira-project-tracker
description: "Secure Jira↔GitHub integration for task tracking. Uses API tokens via environment variables (no stored passwords), follows DRY/simplistic design, and leverages stable open-source tools (atlassian-python-api)."
---

# Jira Project Tracker Skill (Secure)

## Security Principles
- **No hardcoded secrets**: Use env vars only (`JIRA_API_TOKEN`, `JIRA_USERNAME`, `JIRA_URL`). Never commit credentials.
- **Least privilege**: Use API tokens with minimal required scopes. Rotate tokens periodically.
- **No password storage**: API token-based auth only. Avoid Basic auth with raw passwords in scripts/config.
- **Secret management**: Store in GitHub Actions Secrets, local shell env, or `.env` (gitignored). Never log tokens.
- **Secure defaults**: Fail if required secrets missing. No echo of sensitive values.

## Design Principles (DRY, Simple)
- **DRY**: Reuse `scripts/jira/jira_client.py` as single source of truth for Jira operations.
- **Simplicity**: Minimal abstractions, clear workflows, predictable conventions.
- **Stable OSS**: `atlassian-python-api` (actively maintained, stable). Standard Python stdlib only where possible.
- **Stateless**: Scripts read from env, avoid global mutable state.

## Config
- Project: SOFT (https://tsandyk8s.atlassian.net/jira/software/projects/SOFT)
- Env: `JIRA_URL`, `JIRA_USERNAME`, `JIRA_API_TOKEN`, `JIRA_PROJECT_KEY=SOFT`

## Workflow (Traceable)
| State | Jira Status | Trigger |
|---|---|---|
| To Do | To Do | Issue created |
| In Progress | In Progress | Branch created with key (`SOFT-XXX/description`) |
| In Review | In Review | PR opened with key in title |
| Done | Done/Resolved | PR merged to main/dev |

## Conventions
- **Branches**: `SOFT-<num>/<kebab-case>`
- **Commits**: `SOFT-<num>: <concise message>` (imperative)
- **PRs**: Title must include `SOFT-<num>: ...`

## Automation (Secure)
- `jira-sync.yml`: Detects issue keys in commits/PRs; adds non-sensitive audit comments only.
- `jira-test-task.yml`: Manual dispatch; uses Secrets only.
- `promote-dev-to-main.yml`: Branch promotion; no credentials logged.

## Usage
1. Create/fetch SOFT-* in Jira → To Do
2. Branch with key → In Progress
3. Commits with key → auto-tracked
4. PR with key → In Review
5. Merge → tracked; close/Done per policy

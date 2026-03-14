# dev.to Publishing Schedule

Drip-feed: 2 articles per day over 3 days.

| Date       | Article                          | dev.to ID | Status    |
|------------|----------------------------------|-----------|-----------|
| 2026-03-15 | 001 Filesystem MCP Server        | 3351860   | published |
| 2026-03-15 | 002 GitHub MCP Server            | 3351862   | published |
| 2026-03-16 | 003 Brave Search MCP Server      | 3351905   | scheduled |
| 2026-03-16 | 004 Slack MCP Server             | 3351906   | scheduled |
| 2026-03-17 | 005 Docker MCP Server            | 3351920   | scheduled |
| 2026-03-17 | 006 Sentry MCP Server            | 3351927   | scheduled |

## How to publish

Each run, check this schedule. If today's date matches a scheduled article, publish it by:
1. `sed 's/published: false/published: true/'` the local .md file into /tmp
2. PUT to `https://dev.to/api/articles/{ID}` with the updated body_markdown
3. Update the local .md file to `published: true`
4. Update this schedule to mark it as `published`

Once all 6 are published, update `.current_social_task` to 139 (Hashnode).

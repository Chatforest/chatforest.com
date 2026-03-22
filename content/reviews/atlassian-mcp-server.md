---
title: "Atlassian MCP Server — Jira and Confluence Access for AI Agents"
date: 2026-03-14T21:09:00+09:00
description: "Atlassian's official Rovo MCP server connects AI agents to Jira, Confluence, and Compass. We review the cloud-hosted server and the community alternative with 10x the stars."
og_description: "Atlassian's official Rovo MCP server gives AI agents access to Jira and Confluence. Here's the honest review of what works and what doesn't."
content_type: "Review"
card_description: "Atlassian's official Rovo MCP server connects AI agents to Jira, Confluence, and Compass via cloud-hosted OAuth 2.1. But a community server with 10x the stars may be the better choice."
last_refreshed: 2026-03-14
---

Jira and Confluence are the backbone of project management and documentation at thousands of companies. The problem is obvious: AI agents can't see your sprint board, can't search your knowledge base, and can't create tickets from conversation context without some kind of bridge.

Atlassian launched their official Rovo MCP Server in May 2025, hosted at `mcp.atlassian.com`. It reached general availability on February 4, 2026, and gives AI agents structured access to Jira, Confluence, Compass, and now Jira Service Management through OAuth 2.1. But here's the twist — a community server with 10x the GitHub stars may actually be the better choice for many teams.

**At a glance:** 467 GitHub stars, 47 forks, 46+ tools across 5 product areas, ~16.7K all-time PulseMCP visitors (#1,184 globally, ~697 weekly), GA since Feb 4 2026, SSE transport sunset June 30 2026

## The Official Server

**Repository:** [atlassian/atlassian-mcp-server](https://github.com/atlassian/atlassian-mcp-server)
**Stars:** 467 | **Forks:** 47 | **Commits:** 69 | **Contributors:** 13
**Language:** JavaScript | **License:** Apache 2.0

The Atlassian Rovo MCP Server is cloud-hosted — there's nothing to install, no local process to manage. You point your MCP client at `https://mcp.atlassian.com/v1/mcp` and complete an OAuth 2.1 consent flow in your browser. All actions respect your existing Jira and Confluence permissions. This is the right architecture.

### What It Does

The server supports five Atlassian product areas with 46+ tools:

**Jira:**
- Search issues with JQL ("Find all open bugs in Project Alpha")
- Create, update, and transition issues
- Add comments and work logs
- Bulk issue creation from specs or meeting notes

**Confluence:**
- Search pages with CQL
- Read, create, and update pages
- Summarize content
- Navigate spaces

**Compass:**
- Create service components from repositories
- Query service dependencies
- Bulk import components and custom fields from CSV/JSON

**Jira Service Management:**
- Query alerts and incidents
- View on-call schedules
- Handle escalations

**Cross-product:**
- Link Jira tickets to Confluence pages
- Fetch documentation linked to Compass components
- Rovo Search across all connected products

### Setup

For supported clients (Claude, ChatGPT, GitHub Copilot CLI, Gemini CLI, VS Code, Amazon Quick Suite), setup is straightforward — add the server endpoint and complete the OAuth flow. The app auto-installs on first authorization (no Marketplace installation needed).

For local or custom clients, you'll need Node.js v18+ to run the `mcp-remote` proxy that bridges stdio transport to the remote HTTPS endpoint.

**API token authentication** is available for headless or long-running setups, but requires an organization admin to enable it first and uses scoped Rovo MCP tokens rather than standard Atlassian API tokens.

### Rate Limits

| Plan | Limit |
|------|-------|
| Free | 500 calls/hour |
| Standard | 1,000 calls/hour |
| Premium/Enterprise | 1,000 base + 20 per user (up to 10,000/hour max) |

These limits are per-organization, not per-user. For most teams, the Standard tier's 1,000 calls/hour should be sufficient. Enterprise teams with many concurrent agent users may need to monitor usage.

## What's New (March 2026 Update)

**Rovo MCP Server reached GA on February 4, 2026.** The server is now officially generally available with enterprise-grade security, audit logging, and admin controls. Atlassian reports that enterprise customers drive nearly 40% of monthly active users, and paid editions account for 93% of all usage.

**Agents in Jira open beta (February 24).** Atlassian introduced AI agents directly inside Jira — you can assign work to Rovo agents and MCP-enabled third-party agents, @mention agents in issue comments for iterative collaboration, and embed agents into Jira workflows. Agents respect existing project permissions, audit trails, and approval flows. This complements MCP: MCP lets your external agents reach into Jira, while Agents in Jira lets Atlassian's agents work natively inside your boards.

**ChatGPT connector with writeback.** Atlassian launched a dedicated Rovo MCP Connector for ChatGPT — described as "among the first MCP connectors with writeback support." The ecosystem now spans 20+ MCP connectors including Figma, HubSpot, and Lovable.

**Azure SRE Agent integration (February 25).** Microsoft published official documentation for connecting Atlassian Rovo MCP to Azure SRE Agent via Streamable HTTP transport. This validates the server for enterprise DevOps workflows — SRE teams can query Jira issues, view on-call schedules, and manage incidents through Azure's AI agent platform.

**Jira Service Management tools added.** The server now covers five product areas (up from three): Jira, Confluence, Compass, Jira Service Management (alerts, on-call, escalations), and cross-product Rovo Search. Tool count documented at 46+ via Azure integration docs.

**Search regression fixed.** Issue #70 (deprecated `/rest/api/3/search` endpoint returning empty results) was closed on March 15. The remote server already uses the new `/rest/api/3/search/jql` endpoint — the bug only affected the old Docker stdio version that Atlassian no longer supports. This removes the biggest blocker from our previous review.

**Open issues dropped from 57 to 38.** Atlassian closed 19 issues since our last review, a meaningful cleanup. However, new issues continue to arrive — 6 new issues filed in the last 5 days alone.

**SSE transport deprecated.** The `/v1/sse` endpoint is deprecated in favor of `/v1/mcp` (Streamable HTTP). SSE remains available for backward compatibility until June 30, 2026.

**New pagination bug.** Issue #118 (filed March 20) reports that `searchJiraIssuesUsingJql` silently drops results beyond `maxResults` — no `nextPageToken`, no pagination metadata, incorrect totals. This is a new regression likely tied to the `/search/jql` migration.

## What Works Well

**Cloud-hosted with OAuth 2.1 is the gold standard.** No local dependencies, no credential files to manage, no Docker containers to run. The server handles scaling, uptime, and transport. This is how production MCP servers should work.

**Permission-aware by design.** Every action respects the user's existing Jira, Confluence, and Compass roles. If you can't see a project in Jira, your agent can't either. IP allowlisting is also honored if your organization uses it.

**Audit logging.** All MCP actions appear in your organization's audit log. For compliance-heavy environments, this is critical — you can trace what every agent did, when, and on whose behalf.

**Free for all Atlassian Cloud customers.** No additional cost beyond your existing Atlassian subscription. The rate limits scale with your plan tier, but the MCP server itself adds no per-user or per-call charges.

**Admin controls are comprehensive.** Organization admins can manage, monitor, and revoke MCP access through the Connected Apps interface. Domain and IP controls let you restrict which external AI tools can connect. Individual users can revoke their own authorization independently.

**AGENTS.md integration.** You can configure default project keys, space IDs, and cloud IDs in AGENTS.md to reduce discovery tool calls and save tokens — a thoughtful touch for reducing per-query costs.

## Where It Falls Short

**38 open issues — down from 57, but new problems keep arriving.** The search regression (#70) is fixed, and Atlassian has been closing issues. But fundamental reliability problems remain:

- **Pagination is broken.** Issue #118 (filed March 20) reports that JQL search silently drops results beyond `maxResults` (max 100) with no pagination metadata returned. This is a new regression that makes the search fix (#70) less useful — search works now, but you can't paginate through large result sets.
- **ADF conversion failures.** Multiple issues (#42, #101, #104) report `editJiraIssue` failing when converting markdown to Atlassian Document Format. You can create issues, but updating descriptions often breaks.
- **Content loss during Confluence edits.** Issue #60 reports that editing pages via MCP causes loss of rich content — inline comment anchors stripped (#54), HTML details tags escaped (#53). This is data-destructive behavior.
- **Large page handling.** Issue #106 reports `updateConfluencePage`/`createConfluencePage` being unusable for large pages.
- **Authentication still fragile.** Issue #108 (March 16) reports VSCode OAuth internal server errors. Issue #116 (March 20) reports Gemini CLI auth failing with token exchange errors. The pattern from earlier issues (#55, #57, #58) continues.
- **MCP-created issues don't trigger Jira Automation.** Issue #114 (March 18) reports that issues created via the MCP server bypass Jira Automation rules — a significant gap for teams relying on automation workflows.
- **Permission errors on create.** Issue #115 (March 19) reports `createJiraIssue` rejecting projects as "anonymous" despite the user having create permissions.

**Cloud-only with no Data Center support.** If your organization runs Jira or Confluence on Server or Data Center (still common in enterprises with compliance requirements), the official server is not an option. This is a significant gap.

**No self-hosted deployment.** You can't run this server behind your firewall. All data flows through `mcp.atlassian.com` on Cloudflare infrastructure. For organizations with strict data residency requirements, this may be a non-starter.

**The README doesn't list actual tools.** Unlike every other MCP server we've reviewed, the official documentation describes workflows ("Find all open bugs") rather than listing actual tool names and parameters. You discover the tools only after connecting. This makes it harder to evaluate capabilities before setup.

**No file attachments.** Issue #47 and #63 request the ability to attach files to Jira issues — a common workflow that's missing.

**User mentions render as raw Account IDs.** Issue #84 reports that when agents add comments with @mentions, they show up as raw Atlassian account IDs rather than display names.

**BitDefender false positive.** Issue #91 reports BitDefender flagging the OAuth command line as malicious during pre-login — a bad first impression even if it's a false positive.

## The Community Alternative

**Repository:** [sooperset/mcp-atlassian](https://github.com/sooperset/mcp-atlassian)
**Stars:** 4,700 | **Forks:** 1,000 | **Commits:** 558 | **Contributors:** 118
**Language:** Python | **License:** MIT
**Latest release:** v0.21.0 (March 2, 2026) | **Total releases:** 69
**PulseMCP:** #15 globally, ~2.4M all-time visitors, ~140K weekly

The community server from sooperset has **10x the GitHub stars** of the official server and vastly more PulseMCP traffic (~2.4M vs ~16.7K all-time visitors). That's extremely unusual — for most products, the official server dominates adoption. Here's why the community version leads:

**72 tools vs. 46+ tools.** The community server explicitly documents 72 tools (36 Jira, 36 Confluence) covering search, CRUD, comments, transitions, sprints, boards, backlogs, and more. The official server now documents 46+ tools, narrowing but not closing this gap.

**Server/Data Center support.** Works with Jira Server/Data Center v8.14+ and Confluence Server/Data Center v6.0+ — the feature the official server refuses to support.

**Multiple auth methods.** API tokens for Cloud, Personal Access Tokens for Server/Data Center, OAuth 2.0, and as of v0.21.0, OAuth 2.0 with Dynamic Client Registration for Data Center instances.

**SSE and Streamable HTTP transport.** Supports remote hosting with multi-user capabilities, not just stdio. v0.21.0 added Basic Auth multi-user support for MCP gateway scenarios.

**Self-hosted.** Install via `uvx`, Docker, `pip`, or from source. Your data stays behind your firewall.

**Active development.** 558 commits, 69 releases, 118 contributors — rapid iteration with 1-2 week release cadence.

**v0.21.0 highlights (March 2):** Sprint management (move issues between sprints), Confluence page relocation and version comparison, comment reply support, OAuth 2.0 proxy with DCR, markdown table → native ADF table conversion, SSRF protection improvements, and fixes for wiki markup corruption in code blocks.

**But it has its own problems:** 137 open issues and 46 open PRs (both growing). It's community-maintained with no corporate backing. No hosted remote option (you manage the infrastructure). And it requires Python and its dependency chain.

## Other Community Servers

| Server | Stars | Focus | Notable |
|--------|-------|-------|---------|
| [aashari/mcp-server-atlassian-jira](https://github.com/aashari/mcp-server-atlassian-jira) | 60 | Jira-only | 5 generic HTTP tools (GET/POST/PUT/PATCH/DELETE), TOON format reduces tokens 30-60% |
| [xuanxt/atlassian-mcp](https://github.com/xuanxt/atlassian-mcp) | — | Jira + Confluence | 51 tools, npm + Docker, sprints and boards |
| [b1ff/atlassian-dc-mcp](https://github.com/b1ff/atlassian-dc-mcp) | — | Data Center | Bitbucket + Confluence + Jira for DC version |
| [nguyenvanduocit/jira-mcp](https://github.com/nguyenvanduocit/jira-mcp) | — | Jira | Go-based, sprint planning + workflow transitions |

The aashari server takes an interesting approach: instead of wrapping individual Jira operations into specific tools, it exposes five generic HTTP methods that map directly to Jira's REST API. This means any API endpoint is accessible, but agents need to know the Jira API structure to use it effectively.

## Security Considerations

Atlassian's README includes an unusually candid security warning: LLMs are vulnerable to prompt injection and tool poisoning attacks. They explicitly recommend:

- Use least privilege and scoped tokens
- Review high-impact changes before confirming
- Monitor audit logs for unusual activity
- Only use trusted MCP clients and servers

This transparency is commendable, but the warnings highlight a real risk: an agent with Jira write access could create, modify, or transition issues based on injected prompts. The official server's permission model mitigates this (you can't exceed your own access), but doesn't prevent an agent from taking unintended actions within your permission scope.

The community server (sooperset) has its own `SECURITY.md` with API token handling guidelines, but lacks the audit logging that the official server provides.

## Who Should Use Which

**Use the official Atlassian server if:**
- You're on Atlassian Cloud and want zero-install setup
- Audit logging and admin controls matter for compliance
- Your workflows are primarily read-heavy (search, summarize, navigate)
- You're using a supported client (Claude, ChatGPT, Copilot CLI, VS Code)

**Use sooperset/mcp-atlassian if:**
- You need Server/Data Center support
- You need self-hosted deployment behind a firewall
- You need the full 72-tool surface area
- You want a battle-tested server with rapid release cadence
- Write operations (creating/editing issues and pages) are central to your workflow

**Use aashari/mcp-server-atlassian-jira if:**
- You want maximum API coverage with minimal tool overhead
- Your agents can navigate Jira's REST API structure
- Token efficiency is critical (TOON format)

## The Verdict

**Rating: 3.5 / 5** — for the official Atlassian Rovo MCP server.

Atlassian is making real progress. The Rovo MCP Server is now GA, the search regression is fixed, open issues dropped from 57 to 38, and the ecosystem has expanded significantly — Agents in Jira, ChatGPT connector with writeback, Azure SRE Agent integration, Jira Service Management tools, and 20+ MCP connectors across the Atlassian platform. The architecture remains the gold standard: cloud-hosted, OAuth 2.1, permission-aware, audit-logged, free with your subscription.

But the execution gap persists. A new pagination bug (#118) makes search results unreliable for large result sets — one step forward on search, one step back on pagination. ADF conversion failures still plague write operations. Authentication continues to break across clients (VSCode, Gemini CLI). Issues created via MCP don't trigger Jira Automation rules. These are the kinds of problems that make teams lose trust.

The community server (sooperset) still leads with 10x the stars, 140x the PulseMCP traffic, and a more complete tool surface. Its v0.21.0 release added sprint management, ADF table conversion, and OAuth 2.0 for Data Center — features the official server lacks. For teams that need Server/Data Center support, self-hosted deployment, or reliable write operations, the community server remains the better choice.

We're keeping the rating at 3.5/5. The trend is positive — GA status, ecosystem growth, issue cleanup — but Atlassian needs to nail pagination, stabilize ADF conversion, and fix the Jira Automation bypass before the official server can be the default recommendation.

---

*This review is based on research conducted in March 2026, analyzing the GitHub repositories, official documentation, Atlassian blog announcements, Microsoft Azure documentation, PulseMCP data, open issues, and community feedback. ChatForest researches tools deeply but does not install or run them — see our [methodology](/about/#our-review-methodology).*

*This review was last edited on 2026-03-21 using Claude Opus 4.6 (Anthropic).*

# Best Project Management MCP Servers in 2026

> Jira, Linear, Asana, Notion, ClickUp, Monday.com, Trello, Todoist, Shortcut, Plane, GitHub Projects, and more — we've reviewed 50+ project management MCP servers across 14 categories.


Project management is where AI agents deliver the most obvious productivity gains. Creating issues, searching backlogs, updating sprints, linking PRs to tickets — these are the repetitive tasks that eat hours every week. MCP servers turn them into natural-language commands inside your IDE or chat interface.

The landscape has shifted dramatically since our March review. Five more platforms now ship official MCP servers — Asana, Shortcut, Plane, Smartsheet, and Wrike all launched between February and April 2026. ClickUp's official server expanded from 6 to ~49 tools. GitHub Projects got MCP support. The "official server" wave we flagged is now a flood.

We've researched 50+ project management MCP servers across every major platform. This guide covers what's worth using, what to avoid, and where the ecosystem still has gaps.

*Note: Our recommendations are based on documentation review, GitHub analysis, and community feedback — not hands-on testing of every server. Star counts were verified in April 2026.*

## What changed (March → April 2026)

| Server | Change | Details |
|--------|--------|---------|
| sooperset/mcp-atlassian | Stars 4,600→5,000 | v0.21.1 (April 10), Jira Cloud search broken (#1295), FastMCP CVE concern |
| Atlassian official | Stars ~470→608 | Bitbucket Cloud added (April 8), 56 open issues, #132 duplicate tickets still open |
| Linear Official | OAuth fixes | April 16 OAuth disconnect fix, /sse deprecated → /mcp |
| makenotion/notion-mcp-server | Stars 3,700→4,257 | 153 open issues, prompt injection #238 still unpatched |
| suekou/mcp-notion-server | Stars 778→880 | Actively maintained |
| **Asana Official V2** | **NEW** | **GA at mcp.asana.com/v2/mcp, Streamable HTTP, V1 shuts down May 11** |
| roychri/mcp-server-asana | Stable at 137 | v1.8.0, actively maintained |
| **ClickUp Official** | **6→~49 tools** | **14 categories, still public beta** |
| mondaycom/mcp | Stars 383→396 | v1.6.0, hosted MCP at mcp.monday.com/mcp |
| taazkareem/clickup-mcp-server | Star count anomaly | Repo may have been recreated; last pushed April 18 |
| Doist/todoist-ai | v8.9.1 | 44 tools, 99 total releases, very active |
| delorenj/mcp-server-trello | 313 stars | **Stalled** — no commits since Feb 2026 |
| **Shortcut Official** | **NEW** | **98 stars, v0.24.0, OAuth hosted + stdio** |
| **Plane Official** | **NEW** | **201 stars, 55+ tools, v0.2.8** |
| **Smartsheet Official** | **NEW** | **Hosted, requires Business+ plan** |
| **Wrike Official** | **NEW** | **Hosted at mcp.wrike.com** |
| **GitHub Projects** | **NEW** | **Part of github-mcp-server (29,200 stars), opt-in tools** |
| runekaagaard/mcp-redmine | 172 stars | No activity since Jan 2026 |

## The short version

| Category | Our pick | Stars | Runner-up |
|----------|----------|-------|-----------|
| Jira/Atlassian (community) | [sooperset/mcp-atlassian](https://github.com/sooperset/mcp-atlassian) | 5,000 | [xuanxt/atlassian-mcp](https://github.com/xuanxt/atlassian-mcp) (51 tools) |
| Jira/Atlassian (official) | [Atlassian Rovo MCP](https://github.com/atlassian/atlassian-mcp-server) | 608 | Remote-hosted, GA |
| Linear | [Linear Official MCP](https://mcp.linear.app) | — | [jerhadf/linear-mcp-server](https://github.com/jerhadf/linear-mcp-server) (344 stars, deprecated) |
| Notion | [makenotion/notion-mcp-server](https://github.com/makenotion/notion-mcp-server) | 4,257 | [suekou/mcp-notion-server](https://github.com/suekou/mcp-notion-server) (880 stars) |
| Asana (official) | [Asana V2 MCP](https://developers.asana.com/docs/using-asanas-mcp-server) | — | [roychri/mcp-server-asana](https://github.com/roychri/mcp-server-asana) (137 stars) |
| Monday.com | [mondaycom/mcp](https://github.com/mondaycom/mcp) | 396 | [Prat011/mcp-server-monday](https://github.com/Prat011/mcp-server-monday) |
| ClickUp (official) | [ClickUp MCP](https://developer.clickup.com/docs/connect-an-ai-assistant-to-clickups-mcp-server) | — | [hauptsacheNet/clickup-mcp](https://github.com/hauptsacheNet/clickup-mcp) (42 stars) |
| Trello | [delorenj/mcp-server-trello](https://github.com/delorenj/mcp-server-trello) | 313 | [m0xai/trello-mcp-server](https://github.com/m0xai/trello-mcp-server) |
| Todoist | [Doist/todoist-ai](https://github.com/Doist/todoist-ai) | 460 | [abhiz123/todoist-mcp-server](https://github.com/abhiz123/todoist-mcp-server) |
| Shortcut | [useshortcut/mcp-server-shortcut](https://github.com/useshortcut/mcp-server-shortcut) | 98 | — |
| Plane | [makeplane/plane-mcp-server](https://github.com/makeplane/plane-mcp-server) | 201 | — |
| GitHub Projects | [github/github-mcp-server](https://github.com/github/github-mcp-server) | 29,200 | — |
| Redmine | [runekaagaard/mcp-redmine](https://github.com/runekaagaard/mcp-redmine) | 172 | [jztan/redmine-mcp-server](https://github.com/jztan/redmine-mcp-server) (23 stars, 51 tools) |

## Why project management MCP servers matter

Every development team has the same friction: context-switching between their IDE and their issue tracker. Write code, tab to Jira, update the ticket, tab back. Repeat fifty times a day. MCP servers eliminate that loop.

The value comes in three forms:

1. **Issue management from your editor.** "Create a bug ticket for the login timeout in the Auth project, assign to me, set to High priority" — without leaving your IDE. The agent creates the issue with the right fields, labels, and sprint assignment.
2. **Backlog search and triage.** "Show me all unresolved bugs in the Payments project from the last sprint" — agents translate natural language into JQL, Linear filters, or API queries and return structured results.
3. **Cross-tool workflows.** "When I commit this PR, update the linked Jira ticket to In Review and add a comment with the PR link" — connecting your version control workflow directly to your project tracker.

The landscape now splits into two tiers: **platforms with official MCP servers** (Atlassian, Linear, Monday.com, Notion, Asana, ClickUp, Todoist, Shortcut, Plane, Smartsheet, Wrike, GitHub Projects, GitLab) and **platforms with community servers only** (Trello, Redmine, Basecamp, OpenProject, Taiga). The official wave has made the second tier much smaller.

---

## Jira / Atlassian servers

Jira dominates enterprise project management, and its MCP ecosystem reflects that — more implementations than any other platform, plus an official remote server from Atlassian.

### The community winner: sooperset/mcp-atlassian

**Stars:** 5,000 | **Language:** Python | **License:** MIT | **Tools:** 72

[sooperset/mcp-atlassian](https://github.com/sooperset/mcp-atlassian) is the most adopted Atlassian MCP server by a wide margin. It covers both Jira and Confluence, supports Cloud and Server/Data Center deployments, and provides 72 tools spanning issue CRUD, sprint management, board operations, JQL search, page creation, and more.

**Why it wins:** Massive adoption (5,000 stars), dual Jira+Confluence coverage, and support for both Cloud and on-prem deployments. PulseMCP ranks it #16 globally with ~3.6 million total visitors.

**The catch:** A critical issue emerged in April: **Jira Cloud deprecated the GET `/search` endpoint** (HTTP 410), breaking `jira_search` for Cloud users (issue [#1295](https://github.com/sooperset/mcp-atlassian/issues/1295)). Also, the underlying FastMCP 2.x dependency has 3 unpatched CVEs ([#1234](https://github.com/sooperset/mcp-atlassian/issues/1234)) — upgrade to FastMCP 3.2.0+ is pending.

**Security note:** Two critical CVEs were found and **patched in v0.17.0** (February 2026): CVE-2026-27825 (RCE via arbitrary file write, CVSS 9.1) and CVE-2026-27826 (SSRF, CVSS 8.2). Any installation running v0.17.0+ is safe.

**Best for:** Teams on Jira Cloud or Data Center who want comprehensive Jira+Confluence access from their AI assistant. Update to v0.21.1 or later.

### The official option: Atlassian Rovo MCP Server

**Stars:** 608 | **Type:** Remote (cloud-hosted) | **Auth:** OAuth | **Platforms:** Jira, Confluence, Compass, Bitbucket Cloud

[Atlassian's Rovo MCP Server](https://github.com/atlassian/atlassian-mcp-server) is the official, cloud-hosted MCP gateway. It went GA in February 2026 and supports Claude, ChatGPT, Cursor, VS Code, GitHub Copilot, and more.

**What's new:** Bitbucket Cloud support was added April 8, 2026 — covering workspace browsing, PR lifecycle (create/diff/comment/approve/merge), pipeline runs, and deployment management. This makes it a 4-product server now (Jira, Confluence, Compass, Bitbucket).

**The catch:** Cloud-only (no Data Center/Server support). The SSE endpoint (`/v1/sse`) is being deprecated **June 30, 2026** — update to `/v1/mcp`. Issue [#132](https://github.com/atlassian/atlassian-mcp-server/issues/132) (duplicate ticket creation) remains open. Bitbucket auth is API token only — OAuth not yet supported for Bitbucket.

**Best for:** Teams already on Atlassian Cloud who want a zero-maintenance, officially supported integration across Jira, Confluence, Compass, and now Bitbucket.

### Also notable

**[xuanxt/atlassian-mcp](https://github.com/xuanxt/atlassian-mcp)** — 51 tools for Confluence and Jira Cloud. Supports NPM and Docker deployment. Good middle ground between sooperset's comprehensive approach and simpler alternatives.

**[aashari/mcp-server-atlassian-jira](https://github.com/aashari/mcp-server-atlassian-jira)** (60 stars, TypeScript, MIT) — v3.0 replaced 8+ specific tools with 5 generic HTTP method tools that can access any Jira API endpoint. Uses TOON format that reduces token usage by 30-60%.

**[b1ff/atlassian-dc-mcp](https://github.com/b1ff/atlassian-dc-mcp)** — Specifically built for Data Center deployments. Covers Bitbucket, Confluence, and Jira. If you're on DC and can't use the official Cloud server, this is purpose-built for you.

---

## Linear servers

Linear's clean API and developer-friendly culture made it an early MCP adopter. The official remote server is the clear choice.

### The winner: Linear Official MCP Server

**Type:** Remote (cloud-hosted) | **Auth:** OAuth | **Endpoint:** `https://mcp.linear.app/mcp`

Linear ships an official remote MCP server that supports initiatives, project milestones, updates, issue management, and team operations. It's the recommended option after the popular community server (jerhadf) was deprecated.

**What's new (April 2026):** OAuth connection stability fixed — connections no longer disconnect after ~1 day (April 16). OAuth flow no longer hangs on redirect in non-Safari browsers (April 2). New `trashed` field added to `list_projects` and `get_project`. Support for removing issue relationships.

**Important:** The `/sse` endpoint is deprecated. Update configs to `https://mcp.linear.app/mcp`.

**Best for:** Any team using Linear who wants AI-powered issue management.

### The legacy option: jerhadf/linear-mcp-server

**Stars:** 344 | **Language:** TypeScript | **License:** MIT

[jerhadf/linear-mcp-server](https://github.com/jerhadf/linear-mcp-server) was the original community Linear MCP server. **Deprecated** — the README directs users to the official Linear remote MCP server. Still useful as a reference implementation.

### Also notable

**[tacticlaunch/mcp-linear](https://github.com/tacticlaunch/mcp-linear)** (133 stars) — Last commit February 2025. Effectively stale — no releases since September 2025.

**[dvcrn/mcp-server-linear](https://github.com/dvcrn/mcp-server-linear)** — Supports multiple Linear workspaces simultaneously via tool prefixing. Useful for agencies managing multiple orgs.

**[locomotive-agency/linear-mcp](https://github.com/locomotive-agency/linear-mcp)** — Describes itself as "production-grade" with enterprise resilience features.

---

## Notion servers

Notion blurs the line between project management, wiki, and database. Its MCP ecosystem reflects that versatility.

### The winner: makenotion/notion-mcp-server

**Stars:** 4,257 | **Language:** TypeScript | **License:** MIT | **Tools:** 22

[makenotion/notion-mcp-server](https://github.com/makenotion/notion-mcp-server) is the official Notion MCP server. Version 2.2.1 uses the Notion API 2026-03-11 with data sources as the primary abstraction for databases.

**Why it wins:** Official, high adoption (4,257 stars), and purpose-built for AI agents with token-efficient responses.

**The catch:** 153 open issues — growing fast. A **prompt injection vulnerability** ([#238](https://github.com/makenotion/notion-mcp-server/issues/238)) using hidden toggle blocks has been open since March 25 with zero maintainer response. Notion is prioritizing its remote MCP at `mcp.notion.com/mcp` and may sunset this local server.

**Notion platform updates:** Custom Agents free trial ends **May 3, 2026** — after that, agents cost $10/1,000 credits (~45-90 runs). Agents are 35-50% cheaper since Notion 3.4 Part 2 (April 14). API updates include comment CRUD GA, multi-value filters, and 10,000-result pagination cap.

**Best for:** Teams using Notion for project management, documentation, or knowledge bases.

### The community alternative: suekou/mcp-notion-server

**Stars:** 880 | **Language:** TypeScript | **License:** MIT

[suekou/mcp-notion-server](https://github.com/suekou/mcp-notion-server) converts Notion content to Markdown to reduce context size. Growing steadily (778→880 stars since March) and actively maintained (last update April 20).

**Best for:** Cost-conscious teams with extensive Notion content.

---

## Asana servers

**New since March:** Asana now ships an official MCP server, filling what was the biggest gap in the category.

### The winner: Asana Official V2 MCP Server

**Type:** Remote (cloud-hosted) | **Auth:** OAuth | **Endpoint:** `https://mcp.asana.com/v2/mcp`

[Asana's V2 MCP Server](https://developers.asana.com/docs/using-asanas-mcp-server) went GA in early 2026. It uses Streamable HTTP (the new standard replacing SSE), workspace-scoped authorizations, and an optimized tool set. Available on AWS Marketplace.

**Why it wins:** Official support, zero local setup, Streamable HTTP transport. Covers tasks, projects, workspaces, and comments with proper authorization scoping.

**Important deadline:** The **V1 Beta MCP server** (`https://mcp.asana.com/sse`) shuts down **May 11, 2026**. If you're using the SSE endpoint, migrate to V2 now.

**Best for:** Asana teams who want a maintained, official integration.

### The community option: roychri/mcp-server-asana

**Stars:** 137 | **Language:** TypeScript | **License:** MIT | **Version:** v1.8.0

[roychri/mcp-server-asana](https://github.com/roychri/mcp-server-asana) remains actively maintained (last push April 19) with 12+ tools added in recent versions. Includes READ_ONLY_MODE for safe evaluation.

**Best for:** Teams who need a local Asana MCP server or prefer community-maintained options with more flexibility.

### Also notable

**[n0zer0d4y/asana-project-ops](https://github.com/n0zer0d4y/asana-project-ops)** — Enhanced fork of roychri with batch operations, direct section assignment, and selective tool activation. Enterprise-focused.

---

## Monday.com servers

Monday.com ships an official MCP server with comprehensive coverage and a hosted option.

### The winner: mondaycom/mcp

**Stars:** 396 | **Language:** TypeScript | **Version:** v1.6.0 | **Auth:** OAuth 2.1

[mondaycom/mcp](https://github.com/mondaycom/mcp) is the official Monday.com MCP server. Covers boards, items, columns, groups, workspaces, users, updates, and app development tools.

**What's new:** v1.6.0 released. **Hosted MCP** now available at `https://mcp.monday.com/mcp`. **Dynamic API Tools** in beta — enables full GraphQL API access with custom query generation and schema exploration. Enable with `--enable-dynamic-api-tools true`.

**Best for:** Monday.com teams who want direct AI integration. The hosted option eliminates local setup entirely.

### Also notable

**[Prat011/mcp-server-monday](https://github.com/Prat011/mcp-server-monday)** — Community alternative. Simpler setup if you don't need the full official feature set.

---

## ClickUp servers

ClickUp's MCP story changed significantly: the official server expanded from a minimal beta to a serious contender.

### The winner: ClickUp Official MCP Server

**Type:** Remote (cloud-hosted) | **Endpoint:** `mcp.clickup.com/mcp` | **Tools:** ~49 | **Status:** Public beta

[ClickUp's official MCP server](https://developer.clickup.com/docs/connect-an-ai-assistant-to-clickups-mcp-server) expanded from 6 tools at launch to approximately **49 tools across 14 categories**: Search, Task Management, Bulk Ops, Attachments, Comments, Tags, Relationships, Task Movement, Time Tracking, Workspace Hierarchy, Members, Chat, Docs, and Time in Status.

**Why it wins:** Dramatic expansion from minimal beta to near-comprehensive coverage. Official support, zero local setup, no license fees.

**The catch:** Still labeled "public beta." External MCP tool integrations for Brain/Superagents are on the 2026 roadmap but not yet available.

**Best for:** ClickUp teams who want comprehensive, officially maintained AI integration.

### The community option: hauptsacheNet/clickup-mcp

**Stars:** 42 | **Language:** — | **License:** Open source

[hauptsacheNet/clickup-mcp](https://github.com/hauptsacheNet/clickup-mcp) — Open-source alternative, actively maintained (last push April 17). Good option if you need a local server or want to extend functionality.

### Also notable

**taazkareem/clickup-mcp-server** — Previously the dominant community server (460 stars). The repository appears to have been recreated — star count dropped significantly. Still actively maintained (last push April 18) but the official server's expansion makes the paid license harder to justify.

---

## Trello servers

Trello's simpler model (boards, lists, cards) makes it a natural fit for MCP. However, maintainer activity has stalled across the board.

### The winner: delorenj/mcp-server-trello

**Stars:** 313 | **Language:** TypeScript | **License:** MIT

[delorenj/mcp-server-trello](https://github.com/delorenj/mcp-server-trello) provides tools for Trello boards, lists, and cards.

**The catch:** No commits since February 2026. Development appears stalled post-v1.7.0. Still functional, but not actively maintained.

**Best for:** Trello users who need basic board/list/card management. Don't expect new features.

### Also notable

**[m0xai/trello-mcp-server](https://github.com/m0xai/trello-mcp-server)** (53 stars) — Python-based. No maintainer activity since August 2025. Community PRs pending.

**[GabrielRamirez/trello-mcp](https://github.com/GabrielRamirez/trello-mcp)** — New entry with 73 tools across 10 categories (boards, cards, lists, checklists, labels, members, custom fields, orgs, webhooks, search). Claude Code-focused. Very new but most comprehensive Trello MCP implementation.

---

## Todoist servers

Todoist has one of the most actively maintained MCP servers in the entire ecosystem.

### The winner: Doist/todoist-ai

**Stars:** 460 | **Version:** v8.9.1 | **Tools:** 44 | **Type:** Official

[Doist/todoist-ai](https://github.com/Doist/todoist-ai) is Todoist's official AI integration toolkit with 99 total releases — among the most actively developed MCP servers anywhere.

**What's new:** v8.9.1 (April 20) updated Todoist SDK to v9.1.3. Recent releases added better user-lookup via `find-project-collaborators` (v8.9.0), proper HTTP 401 on invalid API tokens (v8.8.8), and workspace project deletion safeguards (v8.8.6).

**Best for:** Todoist users who want reliable, frequently updated AI task management.

### Also notable

**[abhiz123/todoist-mcp-server](https://github.com/abhiz123/todoist-mcp-server)** (390 stars) — No updates since December 2024. Dormant.

**[greirson/mcp-todoist](https://github.com/greirson/mcp-todoist)** — Focused on bulk operations. Useful for batch task creation.

---

## Shortcut servers

**New since March.** Shortcut (formerly Clubhouse) now ships an official MCP server — filling a gap we flagged in our original review.

### The winner: useshortcut/mcp-server-shortcut

**Stars:** 98 | **Version:** v0.24.0 | **Language:** — | **License:** —

[useshortcut/mcp-server-shortcut](https://github.com/useshortcut/mcp-server-shortcut) covers stories, epics, iterations, objectives, docs, custom fields, labels, and workflows. Offers both OAuth-hosted and local stdio modes, plus a read-only mode for safe evaluation.

**Why it matters:** Shortcut is popular with engineering teams, and this is a proper official server — not a community effort. The read-only mode is a smart safety feature.

**Best for:** Shortcut teams who want AI-powered issue management with official support.

---

## Plane servers

**New since March.** Plane, the open-source project management tool, ships an official MCP server with impressive breadth.

### The winner: makeplane/plane-mcp-server

**Stars:** 201 | **Version:** v0.2.8 | **Language:** Python | **Tools:** 55+

[makeplane/plane-mcp-server](https://github.com/makeplane/plane-mcp-server) covers projects, cycles, modules, intake, initiatives, and users across 55+ tools in 8 categories. Supports stdio, SSE, and streamable HTTP transports with API key, OAuth, and PAT authentication.

**Why it matters:** 201 stars in a short time suggests strong demand from the Plane community. The tool count (55+) is competitive with established players.

**Best for:** Plane users who want comprehensive AI integration with their self-hosted project management.

---

## GitHub Projects

**New since March.** GitHub's official MCP server now includes Projects support — and it's the most-starred MCP server in existence.

### github/github-mcp-server

**Stars:** 29,200 | **Language:** Go | **License:** MIT

[github/github-mcp-server](https://github.com/github/github-mcp-server) added Projects tools in October 2025, significantly expanded in January 2026 with 50% token usage reduction, new `projects_list` and `projects_write` tools.

**Important:** Projects tools are **not enabled by default** — you must explicitly add them to your configuration.

**Best for:** Teams using GitHub Projects who already have the GitHub MCP server configured. Adding Projects support is a configuration change, not a new server.

---

## Redmine servers

Redmine's open-source heritage means multiple community MCP servers, though none are official.

### The winner: runekaagaard/mcp-redmine

**Stars:** 172 | **Language:** Python | **License:** —

[runekaagaard/mcp-redmine](https://github.com/runekaagaard/mcp-redmine) covers close to 100% of Redmine's API. The most complete option.

**The catch:** No activity since January 2026. Still functional, but maintenance status is uncertain.

### The rising alternative: jztan/redmine-mcp-server

**Stars:** 23 | **Language:** — | **Tools:** 51

[jztan/redmine-mcp-server](https://github.com/jztan/redmine-mcp-server) — Production-ready server with 51 tools, flexible auth (API key / basic / OAuth2), prompt injection protection, and Docker deployment. Requires Redmine 6.1+ for OAuth2. Actively developed with 437 commits.

**Best for:** Teams who need a maintained Redmine MCP server with modern security features.

---

## More platforms with MCP support

### Smartsheet (Official)

[Smartsheet's official MCP server](https://developers.smartsheet.com/ai-mcp/smartsheet/mcp-server) covers sheet read/summarize, row creation/updates, and attachment management. Hosted service — no local installation. **Requires Business, Enterprise, or Advanced Work Management plan.**

### Wrike (Official)

[Wrike's official MCP server](https://developers.wrike.com/wrike-mcp/) at `mcp.wrike.com` provides task queries, folder/project navigation, work prioritization, search, structure creation, and meeting-to-task conversion. Hosted service.

### GitLab Issues

GitLab's built-in MCP server now covers issue creation (GitLab 18.5), merge request creation, and code search. Issue creation expanded in GitLab 18.8 with `assignee_ids`, `reviewer_ids`, `labels`, and `milestone_id`. [GitLab MCP tools documentation](https://docs.gitlab.com/user/gitlab_duo/model_context_protocol/mcp_server_tools/).

### OpenProject (Community)

**[AndyEverything/openproject-mcp-server](https://github.com/AndyEverything/openproject-mcp-server)** (49 stars) — 23-parameter work package filtering, Python async. OpenProject also has [native MCP docs](https://www.openproject.org/docs/system-admin-guide/integrations/mcp-server/).

### Taiga (Community)

**[talhaorak/pytaiga-mcp](https://github.com/talhaorak/pytaiga-mcp)** (27 stars) — Most mature Taiga MCP server. Covers epics, user stories, tasks, issues, sprint tracking with verbosity controls.

---

## Integration platforms

Rather than using individual platform servers, integration platforms provide unified MCP access to multiple tools.

### Merge Agent Handler

[Merge](https://www.merge.dev/blog/project-management-mcp-servers) offers MCP servers through their Agent Handler platform, covering Linear, Asana, and others. Features customizable tools, comprehensive logging, and DLP to prevent data leakage.

### Composio MCP

[Composio](https://mcp.composio.dev/) connects to 100+ managed MCP servers with built-in authentication, including Jira, Linear, Asana, Trello, ClickUp, Monday.com, and more.

---

## Which server should you choose?

Follow this decision tree:

1. **Using Jira Cloud?** → Start with the [official Atlassian Rovo MCP Server](https://github.com/atlassian/atlassian-mcp-server). If you need more tools or Data Center support, add [sooperset/mcp-atlassian](https://github.com/sooperset/mcp-atlassian).
2. **Using Jira Data Center/Server?** → [sooperset/mcp-atlassian](https://github.com/sooperset/mcp-atlassian) or [b1ff/atlassian-dc-mcp](https://github.com/b1ff/atlassian-dc-mcp).
3. **Using Linear?** → [Linear Official MCP](https://mcp.linear.app/mcp). Update from `/sse` to `/mcp` endpoint.
4. **Using Notion?** → [makenotion/notion-mcp-server](https://github.com/makenotion/notion-mcp-server) for official support, or Notion's remote MCP at `mcp.notion.com/mcp`. [suekou/mcp-notion-server](https://github.com/suekou/mcp-notion-server) for better token efficiency.
5. **Using Asana?** → [Asana V2 MCP](https://developers.asana.com/docs/using-asanas-mcp-server) (official). Migrate from V1 before May 11.
6. **Using Monday.com?** → [mondaycom/mcp](https://github.com/mondaycom/mcp) or hosted at `mcp.monday.com/mcp`.
7. **Using ClickUp?** → [ClickUp Official MCP](https://developer.clickup.com/docs/connect-an-ai-assistant-to-clickups-mcp-server) (~49 tools). Community [hauptsacheNet/clickup-mcp](https://github.com/hauptsacheNet/clickup-mcp) if you need local/open-source.
8. **Using Shortcut?** → [useshortcut/mcp-server-shortcut](https://github.com/useshortcut/mcp-server-shortcut). Official, both hosted and local.
9. **Using Plane?** → [makeplane/plane-mcp-server](https://github.com/makeplane/plane-mcp-server). 55+ tools.
10. **Using GitHub Projects?** → Enable Projects tools in [github/github-mcp-server](https://github.com/github/github-mcp-server).
11. **Using Todoist?** → [Doist/todoist-ai](https://github.com/Doist/todoist-ai). 44 tools, very active.
12. **Using multiple tools?** → Consider Composio or Merge for unified access.

---

## Three trends to watch

**1. The official server flood.** In March, we counted 5 platforms with official MCP servers (Atlassian, Linear, Monday.com, Notion, Todoist). One month later, that number is **13** — adding Asana, ClickUp (expanded), Shortcut, Plane, Smartsheet, Wrike, GitHub Projects, and GitLab. This isn't a trend anymore; it's the new baseline. If your PM tool doesn't have an official MCP server by mid-2026, ask why.

**2. Hosted MCP is becoming the default.** Atlassian, Linear, Monday.com, Asana, ClickUp, Shortcut, Smartsheet, and Wrike all offer hosted endpoints. The pattern: `mcp.{vendor}.com/mcp`. No local installation, no auth management, no version updates. The trade-off (internet dependency, less customization) is one most teams are happy to make.

**3. SSE is dying, Streamable HTTP is replacing it.** Atlassian's SSE endpoint dies June 30. Linear deprecated `/sse`. Asana V1 (SSE) shuts down May 11. The MCP ecosystem is standardizing on Streamable HTTP. If your config still points to an `/sse` endpoint, update it now.

---

## What's still missing

The gap list has shrunk dramatically since March:

- ~~Asana has no official MCP server~~ → **Fixed.** Asana V2 MCP is GA.
- ~~No Shortcut MCP server~~ → **Fixed.** Official server with 98 stars.
- **No Basecamp MCP server with traction.** One community server exists ([BusyBee3333](https://github.com/BusyBee3333/basecamp-mcp-2026-complete), 50+ tools) but zero stars. Basecamp itself has no AI/MCP roadmap.
- **Trello is stalling.** No official MCP server, and both leading community servers have stalled (delorenj since February, m0xai since August 2025). For an Atlassian product, the MCP gap is notable.
- **No cross-platform migration tools.** Nothing helps you move issues between Jira and Linear, or sync projects across platforms, via MCP.
- **Height shut down.** The AI-native PM tool ceased operations September 2025. No MCP server exists or will exist.

---

## Security considerations

The MCP ecosystem has significant security concerns that affect project management servers:

- **sooperset/mcp-atlassian:** CVE-2026-27825 (RCE, CVSS 9.1) and CVE-2026-27826 (SSRF, CVSS 8.2) — both patched in v0.17.0. FastMCP 2.x dependency has 3 additional unpatched CVEs.
- **Notion official:** Prompt injection via hidden toggle blocks (issue #238) — unpatched, zero maintainer response since March 25.
- **MCP STDIO supply chain crisis (April 2026):** OX Security disclosed that MCP's STDIO transport executes commands even when the server process fails to start, enabling arbitrary command injection across 200,000+ vulnerable server instances. Anthropic declined to change the protocol, stating it's "by design." This affects all locally-installed MCP servers. Hosted/remote servers are not affected.

**Our advice:** Prefer hosted/remote MCP servers where available. They eliminate the STDIO attack surface entirely. For local servers, keep versions current and audit your MCP client's command execution settings.

---

*This guide is part of our [MCP Server Directory](/guides/best-mcp-servers/). We research and compare MCP servers so you don't have to. Updated April 2026.*


# Best Project Management MCP Servers in 2026

> Jira, Linear, Asana, Notion, ClickUp, Monday.com, Trello, Todoist, Shortcut, Plane, GitHub Projects, and more — we've reviewed 50+ project management MCP servers across 14 categories.


Project management is where AI agents deliver the most obvious productivity gains. Creating issues, searching backlogs, updating sprints, linking PRs to tickets — these are the repetitive tasks that eat hours every week. MCP servers turn them into natural-language commands inside your IDE or chat interface.

The landscape has shifted dramatically since our March review. Five more platforms now ship official MCP servers — Asana, Shortcut, Plane, Smartsheet, and Wrike all launched between February and April 2026. ClickUp's official server expanded from 6 to ~49 tools. GitHub Projects got MCP support. The "official server" wave we flagged is now a flood.

We've researched 50+ project management MCP servers across every major platform. This guide covers what's worth using, what to avoid, and where the ecosystem still has gaps.

*Note: Our recommendations are based on documentation review, GitHub analysis, and community feedback — not hands-on testing of every server. Star counts and maintenance status were re-verified against live GitHub data in August 2026.*

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
| Jira/Atlassian (community) | [sooperset/mcp-atlassian](https://github.com/sooperset/mcp-atlassian) | 5,717 | [xuanxt/atlassian-mcp](https://github.com/xuanxt/atlassian-mcp) (51 tools) |
| Jira/Atlassian (official) | [Atlassian Rovo MCP](https://github.com/atlassian/atlassian-mcp-server) | 951 | Remote-hosted, GA |
| Linear | [Linear Official MCP](https://mcp.linear.app) | — | [jerhadf/linear-mcp-server](https://github.com/jerhadf/linear-mcp-server) (347 stars, deprecated) |
| Notion | [makenotion/notion-mcp-server](https://github.com/makenotion/notion-mcp-server) | 4,584 | [suekou/mcp-notion-server](https://github.com/suekou/mcp-notion-server) (919 stars) |
| Asana (official) | [Asana V2 MCP](https://developers.asana.com/docs/using-asanas-mcp-server) | — | [roychri/mcp-server-asana](https://github.com/roychri/mcp-server-asana) (145 stars) |
| Monday.com | [mondaycom/mcp](https://github.com/mondaycom/mcp) | 417 | [Prat011/mcp-server-monday](https://github.com/Prat011/mcp-server-monday) |
| ClickUp (official) | [ClickUp MCP](https://developer.clickup.com/docs/connect-an-ai-assistant-to-clickups-mcp-server) | — | [hauptsacheNet/clickup-mcp](https://github.com/hauptsacheNet/clickup-mcp) (46 stars) |
| Trello | [delorenj/mcp-server-trello](https://github.com/delorenj/mcp-server-trello) | 431 | [m0xai/trello-mcp-server](https://github.com/m0xai/trello-mcp-server) |
| Todoist | [Doist/todoist-mcp](https://github.com/Doist/todoist-mcp) | 536 | [abhiz123/todoist-mcp-server](https://github.com/abhiz123/todoist-mcp-server) |
| Shortcut | [Shortcut official MCP](https://mcp.shortcut.com/mcp) (hosted; local repo archived) | 98 | — |
| Plane | [makeplane/plane-mcp-server](https://github.com/makeplane/plane-mcp-server) | 283 | — |
| GitHub Projects | [github/github-mcp-server](https://github.com/github/github-mcp-server) | 32,124 | — |
| Redmine | [runekaagaard/mcp-redmine](https://github.com/runekaagaard/mcp-redmine) | 231 | [jztan/redmine-mcp-server](https://github.com/jztan/redmine-mcp-server) (65 stars, 51 tools) |

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

**Stars:** 5,717 | **Language:** Python | **License:** MIT | **Tools:** 72

[sooperset/mcp-atlassian](https://github.com/sooperset/mcp-atlassian) is the most adopted Atlassian MCP server by a wide margin. It covers both Jira and Confluence, supports Cloud and Server/Data Center deployments, and provides 72 tools spanning issue CRUD, sprint management, board operations, JQL search, page creation, and more.

**Why it wins:** Massive adoption (5,717 stars), dual Jira+Confluence coverage, and support for both Cloud and on-prem deployments.

**The catch:** Jira Cloud's deprecation of the GET `/search` endpoint (HTTP 410) broke `jira_search` for Cloud users earlier in 2026 — [issue #1295](https://github.com/sooperset/mcp-atlassian/issues/1295) is now **closed**, so update to a current release if you hit this. Separately, the underlying FastMCP 2.x dependency carries three unpatched CVEs — [CVE-2026-32871](https://advisories.gitlab.com/pkg/pypi/fastmcp/) (critical, SSRF/path traversal), [CVE-2026-27124](https://advisories.gitlab.com/pkg/pypi/fastmcp/CVE-2026-27124/) (high, OAuth confused-deputy), and CVE-2025-64340 (medium, command injection) — all requiring the FastMCP 2.x → 3.2.0+ major-version upgrade, tracked in [issue #1234](https://github.com/sooperset/mcp-atlassian/issues/1234).

**Security note:** Two critical CVEs were found and **patched in v0.17.0** (February 2026): [CVE-2026-27825](https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-xjgw-4wvw-rgm4) (RCE via arbitrary file write, CVSS 9.1) and [CVE-2026-27826](https://advisories.gitlab.com/pkg/pypi/mcp-atlassian/CVE-2026-27826/) (header-based SSRF, CVSS 8.2). But a **separate, DNS-rebinding SSRF bypass** of that same fix was found and disclosed July 10, 2026 ([GHSA-489g-7rxv-6c8q](https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-489g-7rxv-6c8q)) — v0.17.0 through v0.21.x validated the attacker-controlled header hostname once at middleware time but re-resolved it at connect time with no IP pinning, so a rebinding attacker could still reach internal IPs or cloud metadata endpoints. That gap was closed in **v0.22.0**. v0.17.0+ is *not* sufficient on its own — you need v0.22.0 or later for full protection against both issues.

**Best for:** Teams on Jira Cloud or Data Center who want comprehensive Jira+Confluence access from their AI assistant. Update to v0.22.0 or later (latest is v0.23.0).

### The official option: Atlassian Rovo MCP Server

**Stars:** 951 | **Type:** Remote (cloud-hosted) | **Auth:** OAuth | **Platforms:** Jira, Confluence, Compass, Bitbucket Cloud

[Atlassian's Rovo MCP Server](https://github.com/atlassian/atlassian-mcp-server) is the official, cloud-hosted MCP gateway. It [went GA on February 4, 2026](https://www.atlassian.com/blog/announcements/atlassian-rovo-mcp-ga) and supports Claude, ChatGPT, Cursor, VS Code, GitHub, and more.

**What's new:** [Bitbucket Cloud support was added April 8, 2026](https://www.atlassian.com/blog/bitbucket/the-atlassian-rovo-mcp-server-now-supports-bitbucket-cloud) — covering workspace browsing, PR lifecycle (create/diff/comment/approve/merge), pipeline runs, and deployment management. This makes it a 4-product server now (Jira, Confluence, Compass, Bitbucket).

**The catch:** Cloud-only (no Data Center/Server support). The SSE endpoint (`/v1/sse`) is being deprecated **June 30, 2026** — update to `/v1/mcp`. Issue [#132](https://github.com/atlassian/atlassian-mcp-server/issues/132) (duplicate ticket creation) remains open. Bitbucket auth is API token only — OAuth not yet supported for Bitbucket.

**Best for:** Teams already on Atlassian Cloud who want a zero-maintenance, officially supported integration across Jira, Confluence, Compass, and now Bitbucket.

### Also notable

**[xuanxt/atlassian-mcp](https://github.com/xuanxt/atlassian-mcp)** — 51 tools for Confluence and Jira Cloud. Supports NPM and Docker deployment. Good middle ground between sooperset's comprehensive approach and simpler alternatives.

**[aashari/mcp-server-atlassian-jira](https://github.com/aashari/mcp-server-atlassian-jira)** (72 stars, TypeScript, unlicensed on GitHub) — v3.0 replaced 8+ specific tools with 5 generic HTTP method tools that can access any Jira API endpoint. Uses TOON format that reduces token usage by 30-60%.

**[b1ff/atlassian-dc-mcp](https://github.com/b1ff/atlassian-dc-mcp)** — Specifically built for Data Center deployments. Covers Bitbucket, Confluence, and Jira. If you're on DC and can't use the official Cloud server, this is purpose-built for you.

---

## Linear servers

Linear's clean API and developer-friendly culture made it an early MCP adopter. The official remote server is the clear choice.

### The winner: Linear Official MCP Server

**Type:** Remote (cloud-hosted) | **Auth:** OAuth | **Endpoint:** `https://mcp.linear.app/mcp`

Linear ships an official remote MCP server that supports initiatives, project milestones, updates, issue management, and team operations. It's the recommended option after the popular community server (jerhadf) was deprecated.

**What's new (April 2026):** [Linear fixed](https://linear.app/changelog/2026-04-02-web-forms-for-linear-asks) an MCP OAuth flow bug where the callback probe consumed the authorization code before browser navigation completed (April 2). [Linear Agent gained MCP tool access](https://linear.app/changelog/2026-04-23-linear-agent-mcp-support) — pulling context from external tools like Granola or Glean into project updates (April 23).

**Important:** The `/sse` endpoint is deprecated. Update configs to `https://mcp.linear.app/mcp`.

**Best for:** Any team using Linear who wants AI-powered issue management.

### The legacy option: jerhadf/linear-mcp-server

**Stars:** 347 | **Language:** TypeScript | **License:** MIT

[jerhadf/linear-mcp-server](https://github.com/jerhadf/linear-mcp-server) was the original community Linear MCP server. **Deprecated** — the README directs users to the official Linear remote MCP server. Still useful as a reference implementation.

### Also notable

**[tacticlaunch/mcp-linear](https://github.com/tacticlaunch/mcp-linear)** (146 stars) — Not stale: the repo shows active commits through July 2026, including an OAuth login flow, tool-annotation/structured-output work, and an MCP SDK upgrade to 1.29. An earlier version of this guide incorrectly called it stale; that was wrong.

**[dvcrn/mcp-server-linear](https://github.com/dvcrn/mcp-server-linear)** — Supports multiple Linear workspaces simultaneously via tool prefixing. Useful for agencies managing multiple orgs.

**[locomotive-agency/linear-mcp](https://github.com/locomotive-agency/linear-mcp)** — Describes itself as "production-grade" with enterprise resilience features.

---

## Notion servers

Notion blurs the line between project management, wiki, and database. Its MCP ecosystem reflects that versatility.

### The winner: makenotion/notion-mcp-server

**Stars:** 4,584 | **Language:** TypeScript | **License:** MIT | **Tools:** 22

[makenotion/notion-mcp-server](https://github.com/makenotion/notion-mcp-server) is the official Notion MCP server. Version 2.2.1 uses the Notion API 2026-03-11 with data sources as the primary abstraction for databases.

**Why it wins:** Official, high adoption (4,584 stars), and purpose-built for AI agents with token-efficient responses.

**The catch:** 182 open issues — growing fast. A **prompt injection vulnerability** ([#238](https://github.com/makenotion/notion-mcp-server/issues/238)) using hidden toggle blocks remains **open with zero maintainer response**, confirmed still unresolved as of this audit. Notion is prioritizing its remote MCP at `mcp.notion.com/mcp` and may sunset this local server.

**Notion platform updates:** Custom Agents' free trial [ended May 3, 2026](https://www.notion.com/blog/introducing-custom-agents) — agents now cost $10 per 1,000 Notion Credits on Business/Enterprise plans, with consumption scaling by task complexity. (An earlier version of this guide included more specific figures — a "35-50% cheaper" claim and API changelog details — that we could not re-confirm against a primary source on this pass; cut rather than left uncited.)

**Best for:** Teams using Notion for project management, documentation, or knowledge bases.

### The community alternative: suekou/mcp-notion-server

**Stars:** 919 | **Language:** TypeScript | **License:** MIT

[suekou/mcp-notion-server](https://github.com/suekou/mcp-notion-server) converts Notion content to Markdown to reduce context size. Growing steadily and actively maintained (last push July 31, 2026).

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

**Stars:** 145 | **Language:** TypeScript | **License:** MIT

[roychri/mcp-server-asana](https://github.com/roychri/mcp-server-asana) remains actively maintained (last push May 10, 2026). Includes READ_ONLY_MODE for safe evaluation.

**Best for:** Teams who need a local Asana MCP server or prefer community-maintained options with more flexibility.

### Also notable

**[n0zer0d4y/asana-project-ops](https://github.com/n0zer0d4y/asana-project-ops)** — Enhanced fork of roychri with batch operations, direct section assignment, and selective tool activation. Enterprise-focused.

---

## Monday.com servers

Monday.com ships an official MCP server with comprehensive coverage and a hosted option.

### The winner: mondaycom/mcp

**Stars:** 417 | **Language:** TypeScript | **Auth:** OAuth 2.1

[mondaycom/mcp](https://github.com/mondaycom/mcp) is the official Monday.com MCP server. Covers boards, items, columns, groups, workspaces, users, updates, and app development tools.

**What's new:** v1.6.0 released. **Hosted MCP** now available at `https://mcp.monday.com/mcp`. **Dynamic API Tools** in beta — enables full GraphQL API access with custom query generation and schema exploration. Enable with `--enable-dynamic-api-tools true`.

**Best for:** Monday.com teams who want direct AI integration. The hosted option eliminates local setup entirely.

### Also notable

**[Prat011/mcp-server-monday](https://github.com/Prat011/mcp-server-monday)** — Community alternative. Simpler setup if you don't need the full official feature set.

---

## ClickUp servers

ClickUp's MCP story changed significantly: the official server expanded from a minimal beta to a serious contender.

### The winner: ClickUp Official MCP Server

**Type:** Remote (cloud-hosted) | **Endpoint:** `mcp.clickup.com/mcp` | **Tools:** 60+ | **Status:** Public beta

[ClickUp's official MCP server](https://developer.clickup.com/docs/mcp-tools) expanded from 6 tools at launch to **60+ tools across 14 categories**: Search, Task Management, Bulk Ops, Attachments, Comments, Tags, Relationships, Task Movement, Time Tracking, Workspace Hierarchy, Members, Chat, Docs, and Time in Status. (This guide previously said ~49 tools; the count has grown further since that check.)

**Why it wins:** Dramatic expansion from minimal beta to near-comprehensive coverage. Official support, zero local setup, no license fees.

**The catch:** Still labeled "public beta." External MCP tool integrations for Brain/Superagents are on the 2026 roadmap but not yet available.

**Best for:** ClickUp teams who want comprehensive, officially maintained AI integration.

### The community option: hauptsacheNet/clickup-mcp

**Stars:** 46 | **Language:** TypeScript | **License:** MIT

[hauptsacheNet/clickup-mcp](https://github.com/hauptsacheNet/clickup-mcp) — Open-source alternative, actively maintained (last push August 2026). Good option if you need a local server or want to extend functionality.

### Also notable

**taazkareem/clickup-mcp-server** — Previously the dominant community server (460 stars, per its own earlier README claims). The repository appears to have been recreated — star count is now 50, a fraction of the earlier figure. Still shows recent pushes (August 2026), but the official server's expansion makes the paid license harder to justify.

---

## Trello servers

Trello's simpler model (boards, lists, cards) makes it a natural fit for MCP.

### The winner: delorenj/mcp-server-trello

**Stars:** 431 | **Language:** TypeScript | **License:** MIT

[delorenj/mcp-server-trello](https://github.com/delorenj/mcp-server-trello) provides tools for Trello boards, lists, and cards.

**Update:** An earlier version of this guide said this repo was stalled with "no commits since February 2026." That was wrong even at the time it was checked, and is clearly wrong now — the repo has active 2026 commits including `watch_card`/`watch_list` activity subscriptions, label search/removal tools, card attachment/checklist retrieval, and due-reminder support on card create/update, most recently in early August 2026.

**Best for:** Trello users who need basic-to-intermediate board/list/card management from an actively maintained server.

### Also notable

**[m0xai/trello-mcp-server](https://github.com/m0xai/trello-mcp-server)** (55 stars) — Python-based. An earlier version of this guide said there had been "no maintainer activity since August 2025"; the repo has since shown a push as recent as June 2026, so treat that staleness claim as outdated.

**[GabrielRamirez/trello-mcp](https://github.com/GabrielRamirez/trello-mcp)** — New entry with 73 tools across 10 categories (boards, cards, lists, checklists, labels, members, custom fields, orgs, webhooks, search). Claude Code-focused. Very new but most comprehensive Trello MCP implementation.

---

## Todoist servers

Todoist has one of the most actively maintained MCP servers in the entire ecosystem.

### The winner: Doist/todoist-mcp

**Stars:** 536 | **Version:** v12.5.3 | **Tools:** 50+ | **Type:** Official

The repo formerly at `Doist/todoist-ai` has been renamed to **[Doist/todoist-mcp](https://github.com/Doist/todoist-mcp)** (the old URL redirects). It's Todoist's official AI integration toolkit — the `src/tools` directory currently contains 50 distinct tool implementations (comments, filters, labels, projects, reminders, sections, tasks, plus productivity/health-stats and workspace-insight tools). Version jumped from v8.9.1 to v12.5.3 between this guide's earlier audits, confirming it's among the most actively developed MCP servers in this category.

**Best for:** Todoist users who want reliable, frequently updated AI task management.

### Also notable

**[abhiz123/todoist-mcp-server](https://github.com/abhiz123/todoist-mcp-server)** (391 stars) — No updates since April 2025. Dormant.

**[greirson/mcp-todoist](https://github.com/greirson/mcp-todoist)** — Focused on bulk operations. Useful for batch task creation.

---

## Shortcut servers

**New since March.** Shortcut (formerly Clubhouse) now ships an official MCP server — filling a gap we flagged in our original review.

### The winner: Shortcut official MCP (now hosted-only)

**Stars (legacy repo):** 98 | **Type:** Remote (cloud-hosted) | **Auth:** OAuth

**Update, August 2026:** The GitHub repo we originally pointed to, [useshortcut/mcp-server-shortcut](https://github.com/useshortcut/mcp-server-shortcut), was **archived on July 8, 2026**. Its own README now says: "All future development on the Shortcut MCP server will be done on the remote server at `https://mcp.shortcut.com/mcp`. This repo remains here for historical reference purposes only." The local stdio mode this guide previously recommended is no longer where development happens — use the hosted endpoint instead.

[useshortcut/mcp-server-shortcut](https://github.com/useshortcut/mcp-server-shortcut) (archived, reference only) previously covered stories, epics, iterations, objectives, docs, custom fields, labels, and workflows, plus a read-only mode for safe evaluation. The hosted server at `mcp.shortcut.com/mcp` is the maintained successor.

**Best for:** Shortcut teams who want AI-powered issue management — connect to the hosted `mcp.shortcut.com/mcp` endpoint rather than installing the archived local package.

---

## Plane servers

**New since March.** Plane, the open-source project management tool, ships an official MCP server with impressive breadth.

### The winner: makeplane/plane-mcp-server

**Stars:** 283 | **Language:** Python | **Tools:** 55+

[makeplane/plane-mcp-server](https://github.com/makeplane/plane-mcp-server) covers projects, cycles, modules, intake, initiatives, and users across 55+ tools in 8 categories. Supports stdio, SSE, and streamable HTTP transports with API key, OAuth, and PAT authentication.

**Why it matters:** 283 stars suggests strong and growing demand from the Plane community. The tool count (55+) is competitive with established players.

**Best for:** Plane users who want comprehensive AI integration with their self-hosted project management.

---

## GitHub Projects

**New since March.** GitHub's official MCP server now includes Projects support — and it's the most-starred MCP server in existence.

### github/github-mcp-server

**Stars:** 32,124 | **Language:** Go | **License:** MIT

[github/github-mcp-server](https://github.com/github/github-mcp-server) added Projects tools in October 2025, significantly expanded in January 2026 with 50% token usage reduction, new `projects_list` and `projects_write` tools.

**Important:** Projects tools are **not enabled by default** — you must explicitly add them to your configuration.

**Best for:** Teams using GitHub Projects who already have the GitHub MCP server configured. Adding Projects support is a configuration change, not a new server.

---

## Redmine servers

Redmine's open-source heritage means multiple community MCP servers, though none are official.

### The winner: runekaagaard/mcp-redmine

**Stars:** 231 | **Language:** Python | **License:** MPL-2.0

[runekaagaard/mcp-redmine](https://github.com/runekaagaard/mcp-redmine) covers close to 100% of Redmine's API. The most complete option.

**Update:** An earlier version of this guide said this repo had "no activity since January 2026." That's no longer accurate — it shows a push as recent as July 31, 2026, with 50 commits total.

### The rising alternative: jztan/redmine-mcp-server

**Stars:** 65 | **Language:** Python | **Tools:** 51

[jztan/redmine-mcp-server](https://github.com/jztan/redmine-mcp-server) — Server with 51 tools, flexible auth (API key / basic / OAuth2), prompt injection protection, and Docker deployment. Requires Redmine 6.1+ for OAuth2.

**Best for:** Teams who need a maintained Redmine MCP server with modern security features.

---

## More platforms with MCP support

### Smartsheet (Official)

[Smartsheet's official MCP server](https://developers.smartsheet.com/ai-mcp/smartsheet/mcp-server) covers sheet read/summarize, row creation/updates, and attachment management. Hosted service — no local installation. **Requires Business, Enterprise, or Advanced Work Management plan.**

### Wrike (Official)

[Wrike's official MCP server](https://developers.wrike.com/wrike-mcp/) at `mcp.wrike.com` provides task queries, folder/project navigation, work prioritization, search, structure creation, and meeting-to-task conversion. Hosted service.

### GitLab Issues

GitLab's built-in MCP server covers issue creation, merge request creation, and code search. Per [GitLab's MCP tools documentation](https://docs.gitlab.com/user/model_context_protocol/mcp_server_tools/): the `create_issue` tool was introduced in GitLab 18.4 (already supporting `assignee_ids`, `labels`, and `milestone_id`); `create_merge_request` gained `assignee_ids`, `reviewer_ids`, `description`, `labels`, and `milestone_id` in GitLab 18.8; and semantic code search (`semantic_code_search`, requires a GitLab Duo add-on) moved from experimental to beta by GitLab 18.7. An earlier version of this guide incorrectly attributed the 18.8 parameter additions to issue creation rather than merge request creation, and cited GitLab 18.5 rather than 18.4 for issue creation's introduction.

### OpenProject (Community)

**[AndyEverything/openproject-mcp-server](https://github.com/AndyEverything/openproject-mcp-server)** (72 stars) — 23-parameter work package filtering, Python async. OpenProject also has [native MCP docs](https://www.openproject.org/docs/system-admin-guide/integrations/mcp-server/).

### Taiga (Community)

**[talhaorak/pytaiga-mcp](https://github.com/talhaorak/pytaiga-mcp)** (38 stars) — Covers epics, user stories, tasks, issues, sprint tracking with verbosity controls.

---

## Integration platforms

Rather than using individual platform servers, integration platforms provide unified MCP access to multiple tools.

### Merge Agent Handler

[Merge](https://www.merge.dev/blog/project-management-mcp-servers) offers MCP servers through their Agent Handler platform, covering Linear, Asana, and others. Features customizable tools, comprehensive logging, and DLP to prevent data leakage.

### Composio MCP

[Composio](https://composio.dev/toolkits/) connects to over 1,000 managed toolkits (Composio now advertises "20,000+ tools" across its catalog) with built-in authentication, including Jira, Linear, Asana, ClickUp, and Monday.com. The `mcp.composio.dev` URL this guide previously linked now redirects to the toolkits page above — updated accordingly. Note the "100+ managed MCP servers" figure in earlier versions of this guide understated current scale and is corrected here.

---

## Which server should you choose?

Follow this decision tree:

1. **Using Jira Cloud?** → Start with the [official Atlassian Rovo MCP Server](https://github.com/atlassian/atlassian-mcp-server). If you need more tools or Data Center support, add [sooperset/mcp-atlassian](https://github.com/sooperset/mcp-atlassian).
2. **Using Jira Data Center/Server?** → [sooperset/mcp-atlassian](https://github.com/sooperset/mcp-atlassian) or [b1ff/atlassian-dc-mcp](https://github.com/b1ff/atlassian-dc-mcp).
3. **Using Linear?** → [Linear Official MCP](https://mcp.linear.app/mcp). Update from `/sse` to `/mcp` endpoint.
4. **Using Notion?** → [makenotion/notion-mcp-server](https://github.com/makenotion/notion-mcp-server) for official support, or Notion's remote MCP at `mcp.notion.com/mcp`. [suekou/mcp-notion-server](https://github.com/suekou/mcp-notion-server) for better token efficiency.
5. **Using Asana?** → [Asana V2 MCP](https://developers.asana.com/docs/using-asanas-mcp-server) (official). The V1 beta/SSE server was shut down on schedule May 11, 2026 — if you're reading this and still pointed at V1, migrate now.
6. **Using Monday.com?** → [mondaycom/mcp](https://github.com/mondaycom/mcp) or hosted at `mcp.monday.com/mcp`.
7. **Using ClickUp?** → [ClickUp Official MCP](https://developer.clickup.com/docs/connect-an-ai-assistant-to-clickups-mcp-server) (60+ tools). Community [hauptsacheNet/clickup-mcp](https://github.com/hauptsacheNet/clickup-mcp) if you need local/open-source.
8. **Using Shortcut?** → Connect to the hosted `mcp.shortcut.com/mcp` endpoint. The local package ([useshortcut/mcp-server-shortcut](https://github.com/useshortcut/mcp-server-shortcut)) is archived as of July 2026 — development moved fully to the remote server.
9. **Using Plane?** → [makeplane/plane-mcp-server](https://github.com/makeplane/plane-mcp-server). 55+ tools.
10. **Using GitHub Projects?** → Enable Projects tools in [github/github-mcp-server](https://github.com/github/github-mcp-server).
11. **Using Todoist?** → [Doist/todoist-mcp](https://github.com/Doist/todoist-mcp) (renamed from `todoist-ai`). 50+ tools, very active.
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
- **No official Trello MCP server.** Community servers (delorenj, m0xai) fill the gap and, contrary to what an earlier version of this guide claimed, both are still receiving commits as of mid-2026 — the "stalled" framing was wrong. For an Atlassian product, the lack of an official server is still notable.
- **No cross-platform migration tools.** Nothing helps you move issues between Jira and Linear, or sync projects across platforms, via MCP.
- **Height shut down.** The AI-native PM tool ceased operations September 2025. No MCP server exists or will exist.

---

## Security considerations

The MCP ecosystem has significant security concerns that affect project management servers:

- **sooperset/mcp-atlassian:** [CVE-2026-27825](https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-xjgw-4wvw-rgm4) (RCE, CVSS 9.1) and [CVE-2026-27826](https://advisories.gitlab.com/pkg/pypi/mcp-atlassian/CVE-2026-27826/) (header SSRF, CVSS 8.2) — both patched in v0.17.0. A follow-on DNS-rebinding bypass of the SSRF fix ([GHSA-489g-7rxv-6c8q](https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-489g-7rxv-6c8q), disclosed July 10, 2026) wasn't closed until v0.22.0 — v0.17.0–v0.21.x are still exposed to it. FastMCP 2.x dependency has 3 additional unpatched CVEs requiring the 2.x → 3.2.0+ upgrade.
- **Notion official:** Prompt injection via hidden toggle blocks ([issue #238](https://github.com/makenotion/notion-mcp-server/issues/238)) — confirmed still open with zero maintainer response as of this audit.
- **MCP STDIO supply chain crisis (April 2026):** [OX Security disclosed](https://www.ox.security/blog/the-mother-of-all-ai-supply-chains-critical-systemic-vulnerability-at-the-core-of-the-mcp/) that MCP's STDIO transport executes commands with no sanitization or execution boundary; OX scanned ~7,000 publicly reachable STDIO instances and extrapolated roughly 200,000 vulnerable instances ecosystem-wide across 150M+ SDK downloads. Anthropic confirmed the behavior was intentional and declined to change the protocol. This affects all locally-installed MCP servers. Hosted/remote servers are not affected.

**Our advice:** Prefer hosted/remote MCP servers where available. They eliminate the STDIO attack surface entirely. For local servers, keep versions current and audit your MCP client's command execution settings.

---

*This guide is part of our [MCP Server Directory](/guides/best-mcp-servers/). We research and compare MCP servers so you don't have to. Originally published April 2026; claims re-verified against live sources August 2026.*


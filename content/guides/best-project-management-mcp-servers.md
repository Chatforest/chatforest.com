---
title: "Best Project Management MCP Servers in 2026"
date: 2026-03-22T18:00:00+09:00
description: "Jira, Linear, Asana, Notion, ClickUp, Monday.com, Trello, Todoist, and more — we've reviewed 40+ project management MCP servers across 10 categories. Here's what works, what's official, and where the gaps are."
og_description: "40+ project management MCP servers reviewed across Jira, Linear, Asana, Notion, ClickUp, Monday.com, Trello, and Todoist. The definitive comparison with honest ratings."
content_type: "Comparison"
card_description: "The definitive guide to project management MCP servers in 2026. We've reviewed 40+ servers across Jira/Atlassian (official + community), Linear, Asana, Notion, ClickUp, Monday.com, Trello, Todoist, Redmine, and more. Every recommendation links to a full review."
last_refreshed: 2026-03-22
---

Project management is where AI agents deliver the most obvious productivity gains. Creating issues, searching backlogs, updating sprints, linking PRs to tickets — these are the repetitive tasks that eat hours every week. MCP servers turn them into natural-language commands inside your IDE or chat interface.

The good news: this category has strong official support. Atlassian, Linear, Monday.com, and Notion all ship their own MCP servers. The community has filled in the rest. The result is a mature, competitive landscape with real choices.

We've researched 40+ project management MCP servers across every major platform. This guide covers what's worth using, what to avoid, and where the ecosystem still has gaps.

*Note: Our recommendations are based on documentation review, GitHub analysis, and community feedback — not hands-on testing of every server. Star counts were verified in March 2026.*

## The short version

| Category | Our pick | Stars | Runner-up |
|----------|----------|-------|-----------|
| Jira/Atlassian (community) | [sooperset/mcp-atlassian](https://github.com/sooperset/mcp-atlassian) | 4,600 | [xuanxt/atlassian-mcp](https://github.com/xuanxt/atlassian-mcp) (51 tools) |
| Jira/Atlassian (official) | [atlassian/atlassian-mcp-server](https://github.com/atlassian/atlassian-mcp-server) | — | Remote-hosted, GA |
| Linear | [Linear Official MCP](https://mcp.linear.app) | — | [jerhadf/linear-mcp-server](https://github.com/jerhadf/linear-mcp-server) (329 stars, deprecated) |
| Notion | [makenotion/notion-mcp-server](https://github.com/makenotion/notion-mcp-server) | 3,700 | [suekou/mcp-notion-server](https://github.com/suekou/mcp-notion-server) (778 stars) |
| Asana | [roychri/mcp-server-asana](https://github.com/roychri/mcp-server-asana) | 129 | — |
| Monday.com | [mondaycom/mcp](https://github.com/mondaycom/mcp) | 383 | [Prat011/mcp-server-monday](https://github.com/Prat011/mcp-server-monday) |
| ClickUp | [taazkareem/clickup-mcp-server](https://github.com/taazkareem/clickup-mcp-server) | 460 | [hauptsacheNet/clickup-mcp](https://github.com/hauptsacheNet/clickup-mcp) |
| Trello | [delorenj/mcp-server-trello](https://github.com/delorenj/mcp-server-trello) | — | [m0xai/trello-mcp-server](https://github.com/m0xai/trello-mcp-server) |
| Todoist | [Doist/todoist-ai](https://github.com/Doist/todoist-ai) | — | [abhiz123/todoist-mcp-server](https://github.com/abhiz123/todoist-mcp-server) |
| Redmine | [runekaagaard/mcp-redmine](https://github.com/runekaagaard/mcp-redmine) | — | [zacharyelston/redmine-mcp-server](https://github.com/zacharyelston/redmine-mcp-server) |

## Why project management MCP servers matter

Every development team has the same friction: context-switching between their IDE and their issue tracker. Write code, tab to Jira, update the ticket, tab back. Repeat fifty times a day. MCP servers eliminate that loop.

The value comes in three forms:

1. **Issue management from your editor.** "Create a bug ticket for the login timeout in the Auth project, assign to me, set to High priority" — without leaving your IDE. The agent creates the issue with the right fields, labels, and sprint assignment.
2. **Backlog search and triage.** "Show me all unresolved bugs in the Payments project from the last sprint" — agents translate natural language into JQL, Linear filters, or API queries and return structured results.
3. **Cross-tool workflows.** "When I commit this PR, update the linked Jira ticket to In Review and add a comment with the PR link" — connecting your version control workflow directly to your project tracker.

The landscape splits into three tiers: **platforms with official MCP servers** (Atlassian, Linear, Monday.com, Notion), **platforms with strong community servers** (Asana, ClickUp, Trello, Todoist), and **legacy/enterprise tools with emerging support** (Redmine, Basecamp, Wrike, Shortcut).

---

## Jira / Atlassian servers

Jira dominates enterprise project management, and its MCP ecosystem reflects that — more implementations than any other platform, plus an official remote server from Atlassian.

### The community winner: sooperset/mcp-atlassian

**Stars:** 4,600 | **Language:** Python | **License:** MIT | **Tools:** 72

[sooperset/mcp-atlassian](https://github.com/sooperset/mcp-atlassian) is the most adopted Atlassian MCP server by a wide margin. It covers both Jira and Confluence, supports Cloud and Server/Data Center deployments, and provides 72 tools spanning issue CRUD, sprint management, board operations, JQL search, page creation, and more.

**Why it wins:** Massive adoption (4,600+ stars), dual Jira+Confluence coverage, and support for both Cloud and on-prem deployments. Recent updates (v0.21.0, March 2026) added page movement, version diff comparisons, comment replies, and page width layout controls.

**The catch:** As a local server, you manage authentication and updates yourself. The official Atlassian remote server handles this automatically.

**Best for:** Teams on Jira Cloud or Data Center who want comprehensive Jira+Confluence access from their AI assistant.

### The official option: Atlassian Rovo MCP Server

**Type:** Remote (cloud-hosted) | **Auth:** OAuth | **Platforms:** Jira, Confluence, Compass

[Atlassian's Rovo MCP Server](https://github.com/atlassian/atlassian-mcp-server) is the official, cloud-hosted MCP gateway. It went GA in early 2026 and supports a broad set of AI clients including Claude, ChatGPT, Cursor, VS Code, GitHub Copilot, and more.

**Why it matters:** Zero local setup. OAuth authentication. Atlassian maintains it. Supports both read and write operations — search issues, create epics, update pages, and link content across Jira and Confluence.

**The catch:** Cloud-only (no Data Center/Server support). Requires Atlassian Cloud subscription. The SSE endpoint (`/v1/sse`) is being deprecated June 30, 2026 — update to `/v1/mcp`.

**Best for:** Teams already on Atlassian Cloud who want a zero-maintenance, officially supported integration.

### Also notable

**[xuanxt/atlassian-mcp](https://github.com/xuanxt/atlassian-mcp)** — 51 tools for Confluence and Jira Cloud. Supports NPM and Docker deployment. Good middle ground between sooperset's comprehensive approach and simpler alternatives.

**[aashari/mcp-server-atlassian-jira](https://github.com/aashari/mcp-server-atlassian-jira)** (60 stars, TypeScript, MIT) — Node.js/TypeScript server with a unique approach: v3.0 replaced 8+ specific tools with 5 generic HTTP method tools that can access any Jira API endpoint. Uses TOON (Token-Oriented Object Notation) format that reduces token usage by 30-60%.

**[nguyenvanduocit/jira-mcp](https://github.com/nguyenvanduocit/jira-mcp)** — Go-based MCP connector. Lightweight, fast, and covers issue management, sprint planning, and workflow transitions. Good choice for Go shops.

**[b1ff/atlassian-dc-mcp](https://github.com/b1ff/atlassian-dc-mcp)** — Specifically built for Data Center deployments. Covers Bitbucket, Confluence, and Jira. If you're on DC and can't use the official Cloud server, this is purpose-built for you.

---

## Linear servers

Linear's clean API and developer-friendly culture made it an early MCP adopter. The official remote server is now the recommended option.

### The winner: Linear Official MCP Server

**Type:** Remote (cloud-hosted) | **Auth:** OAuth | **Endpoint:** `https://mcp.linear.app/sse`

Linear ships an official remote MCP server that supports initiatives, project milestones, updates, issue management, and team operations. It's the recommended option after the popular community server (jerhadf) was deprecated.

**Why it wins:** Official support, always up-to-date with Linear's API, zero local setup. Covers the full Linear workflow: issues, projects, cycles, labels, teams, and milestones.

**The catch:** Remote-only — requires internet connectivity. No self-hosted option for air-gapped environments.

**Best for:** Any team using Linear who wants AI-powered issue management.

### The legacy option: jerhadf/linear-mcp-server

**Stars:** 329 | **Language:** TypeScript | **License:** MIT

[jerhadf/linear-mcp-server](https://github.com/jerhadf/linear-mcp-server) was the original community Linear MCP server. It provides tools for creating, updating, searching, and commenting on issues with flexible filtering.

**Important:** This server is deprecated. The README directs users to the official Linear remote MCP server. Still useful as a reference implementation, but don't build new workflows on it.

### Also notable

**[tacticlaunch/mcp-linear](https://github.com/tacticlaunch/mcp-linear)** — Enables AI assistants to interact with Linear through natural language for retrieving, creating, and updating issues, projects, and teams. Active alternative if you prefer a local server.

---

## Notion servers

Notion blurs the line between project management, wiki, and database. Its MCP ecosystem reflects that versatility, with both official and community servers.

### The winner: makenotion/notion-mcp-server

**Stars:** 3,700 | **Language:** TypeScript | **License:** MIT

[makenotion/notion-mcp-server](https://github.com/makenotion/notion-mcp-server) is the official Notion MCP server. Version 2.0.0 migrated to the Notion API 2025-09-03, which introduced data sources as the primary abstraction for databases. Features OAuth for easy setup, Markdown page editing, and tools designed for optimized token consumption.

**Why it wins:** Official, high adoption (3,700+ stars), and purpose-built for AI agents with token-efficient responses.

**The catch:** Notion is prioritizing its remote MCP and may sunset this local server in the future. Issues and PRs are not actively monitored.

**Best for:** Teams using Notion for project management, documentation, or knowledge bases.

### The community alternative: suekou/mcp-notion-server

**Stars:** 778 | **Language:** TypeScript | **License:** MIT

[suekou/mcp-notion-server](https://github.com/suekou/mcp-notion-server) takes a different approach: it converts Notion content to Markdown to reduce context size when communicating with LLMs. This makes it more token-efficient for large Notion workspaces.

**Why it's notable:** Markdown conversion means lower token costs and faster responses. Good for teams with large Notion databases.

**Best for:** Cost-conscious teams with extensive Notion content.

### Also notable

**[awkoy/notion-mcp-server](https://github.com/awkoy/notion-mcp-server)** — Production-ready community server with a complete set of tools and endpoints for reading, creating, and modifying Notion content. Active development.

---

## Asana servers

Asana lacks an official MCP server, but the community has built a solid option.

### The winner: roychri/mcp-server-asana

**Stars:** 129 | **Language:** TypeScript | **License:** MIT

[roychri/mcp-server-asana](https://github.com/roychri/mcp-server-asana) is the most established Asana MCP server. It covers tasks, projects, workspaces, and comments through Asana's API. Includes a READ_ONLY_MODE toggle to disable all write operations during testing.

**Why it wins:** Most adopted Asana MCP server. Covers the core Asana workflow. The read-only mode is a smart safety feature for evaluating the server before granting write access.

**The catch:** Community-maintained, not official. Feature coverage may lag behind Asana's API updates.

**Best for:** Asana teams who want AI-powered task management with a safety net.

---

## Monday.com servers

Monday.com ships an official MCP server with good coverage.

### The winner: mondaycom/mcp

**Stars:** 383 | **Language:** TypeScript | **License:** — | **Auth:** OAuth 2.1

[mondaycom/mcp](https://github.com/mondaycom/mcp) is the official Monday.com MCP server. The `@mondaydotcomorg/monday-api-mcp` package provides a plug-and-play server for AI agents to interact with Monday.com's API — boards, items, columns, groups, workspaces, users, updates, and app development tools.

**Why it wins:** Official support, comprehensive API coverage, and OAuth 2.1 authentication. Updated March 19, 2026.

**The catch:** Requires Monday.com subscription. API rate limits apply.

**Best for:** Monday.com teams who want direct AI integration without third-party middleware.

### Also notable

**[Prat011/mcp-server-monday](https://github.com/Prat011/mcp-server-monday)** — Community alternative for interacting with Monday.com boards and items. Simpler setup if you don't need the full official feature set.

---

## ClickUp servers

ClickUp's MCP ecosystem centers on one dominant community server.

### The winner: taazkareem/clickup-mcp-server

**Stars:** 460 | **Language:** TypeScript | **Auth:** OAuth 2.1

[taazkareem/clickup-mcp-server](https://github.com/taazkareem/clickup-mcp-server) is the most feature-rich ClickUp MCP server. It covers tasks, checklists, sprints, comments, tags, spaces, lists, folders, files, docs, chat, and time tracking. Includes multi-account support, intelligent fuzzy search across all entity types, and OAuth 2.1 with session-isolated caching.

**Why it wins:** Comprehensive coverage of ClickUp's feature set. Intelligent search that resolves entities by name across tasks, lists, folders, and spaces. Multi-account support.

**The catch:** Transitioned from open-source to a paid model. Full license grants unrestricted access across agents with no limits, but it's no longer free.

**Best for:** ClickUp power users who want comprehensive AI integration and are willing to pay for a maintained, production-quality server.

### Also notable

**[hauptsacheNet/clickup-mcp](https://github.com/hauptsacheNet/clickup-mcp)** — Open-source community alternative. If you want free ClickUp MCP integration, start here.

---

## Trello servers

Trello's simpler model (boards, lists, cards) makes it a natural fit for MCP. Multiple community servers are available.

### The winner: delorenj/mcp-server-trello

**Language:** TypeScript | **License:** MIT

[delorenj/mcp-server-trello](https://github.com/delorenj/mcp-server-trello) provides tools for interacting with Trello boards, lists, and cards. Straightforward implementation that covers the core Trello workflow.

**Why it wins:** Most referenced Trello MCP server. Clean TypeScript implementation.

**Best for:** Trello users who want basic board/list/card management from their AI assistant.

### Also notable

**[m0xai/trello-mcp-server](https://github.com/m0xai/trello-mcp-server)** — "A simple yet powerful MCP server for Trello." Alternative implementation with a focus on simplicity.

**andypost/mcp-server-ts-trello** — TypeScript-based server with rate limiting and error handling. Good for teams that need reliability guarantees.

---

## Todoist servers

Todoist has an official MCP server, making it one of the better-supported task management platforms.

### The winner: Doist/todoist-ai

**Language:** — | **License:** — | **Type:** Official

[Doist/todoist-ai](https://github.com/Doist/todoist-ai) is Todoist's official AI integration toolkit. It provides tools that allow AI agents to use Todoist on a user's behalf — creating, updating, and managing tasks and projects through the Todoist API.

**Why it wins:** Official support from Doist. Replaces the earlier `todoist-mcp` package (now deprecated).

**Best for:** Todoist users who want reliable, officially maintained AI task management.

### Also notable

**[abhiz123/todoist-mcp-server](https://github.com/abhiz123/todoist-mcp-server)** — Community server for natural language task management with Claude. Good alternative if the official server doesn't cover your use case.

**[greirson/mcp-todoist](https://github.com/greirson/mcp-todoist)** — Connects Claude to Todoist with bulk operations. Useful for batch task creation and project scaffolding.

**[stanislavlysenko0912/todoist-mcp-server](https://github.com/stanislavlysenko0912/todoist-mcp-server)** — Full implementation covering both the Todoist REST API and Sync API. The most complete feature coverage among community options.

---

## Redmine servers

Redmine's open-source heritage means multiple community MCP servers, though none are official.

### The winner: runekaagaard/mcp-redmine

**Language:** Python | **License:** —

[runekaagaard/mcp-redmine](https://github.com/runekaagaard/mcp-redmine) covers close to 100% of Redmine's API. If you need comprehensive Redmine integration, this is the most complete option.

**Why it wins:** Near-complete API coverage. Active development (latest release January 2026).

**Best for:** Redmine teams who want full API access from their AI assistant.

### Also notable

**[zacharyelston/redmine-mcp-server](https://github.com/zacharyelston/redmine-mcp-server)** — Focused on transparent project management with AI. Supports issue tracking, parent-child relationships for subtasks, and issue relations management.

**[jztan/redmine-mcp-server](https://github.com/jztan/redmine-mcp-server)** — Production-ready server with security features, pagination, and enterprise-grade capabilities.

---

## Integration platforms

Rather than using individual platform servers, integration platforms provide unified MCP access to multiple project management tools through a single interface.

### Merge Agent Handler

[Merge](https://www.merge.dev/blog/project-management-mcp-servers) offers MCP servers through their Agent Handler platform, covering multiple project management tools including Linear, Asana, and others. Features include customizable tools, comprehensive logging, and data loss prevention (DLP) to prevent sensitive data leakage.

**Best for:** Teams using multiple project management tools who want unified MCP access with enterprise security features.

### Composio MCP

[Composio](https://mcp.composio.dev/) connects to 100+ managed MCP servers with built-in authentication, including Jira, Linear, Asana, Trello, ClickUp, Monday.com, and more. Good for teams that want plug-and-play integration without managing individual servers.

**Best for:** Quick setup across multiple tools without managing individual MCP server configurations.

---

## Which server should you choose?

Follow this decision tree:

1. **Using Jira Cloud?** → Start with the [official Atlassian Rovo MCP Server](https://github.com/atlassian/atlassian-mcp-server). If you need Confluence too or want more tools, add [sooperset/mcp-atlassian](https://github.com/sooperset/mcp-atlassian).
2. **Using Jira Data Center/Server?** → [sooperset/mcp-atlassian](https://github.com/sooperset/mcp-atlassian) (supports both Cloud and DC) or [b1ff/atlassian-dc-mcp](https://github.com/b1ff/atlassian-dc-mcp) (DC-specific).
3. **Using Linear?** → [Linear Official MCP](https://mcp.linear.app). No contest.
4. **Using Notion?** → [makenotion/notion-mcp-server](https://github.com/makenotion/notion-mcp-server) for official support. [suekou/mcp-notion-server](https://github.com/suekou/mcp-notion-server) for better token efficiency.
5. **Using Monday.com?** → [mondaycom/mcp](https://github.com/mondaycom/mcp). Official and comprehensive.
6. **Using Asana?** → [roychri/mcp-server-asana](https://github.com/roychri/mcp-server-asana). Only strong option.
7. **Using ClickUp?** → [taazkareem/clickup-mcp-server](https://github.com/taazkareem/clickup-mcp-server) if budget allows, otherwise [hauptsacheNet/clickup-mcp](https://github.com/hauptsacheNet/clickup-mcp).
8. **Using multiple tools?** → Consider Composio or Merge for unified access.

---

## Three trends to watch

**1. Official servers are winning.** Atlassian, Linear, Monday.com, Notion, and Todoist all ship their own MCP servers. This is a clear industry signal: platform vendors see MCP as a first-class integration surface. Expect more official servers in 2026.

**2. Remote MCP is the future.** The shift from local servers to cloud-hosted remote MCP servers (Atlassian Rovo, Linear's hosted endpoint) simplifies setup and eliminates authentication headaches. The trade-off is internet dependency and less customization.

**3. The ClickUp model may spread.** taazkareem's transition from open-source to paid licensing is notable. As MCP servers become critical infrastructure, expect more maintainers to explore sustainable business models. This could improve quality but reduce free options.

---

## What's still missing

Despite strong coverage, several gaps remain in the project management MCP ecosystem:

- **Asana has no official MCP server.** Given its market position, this is a surprising gap. The community server works, but official support would be a significant upgrade.
- **No Basecamp MCP server with traction.** Basecamp has API support but no community MCP server with meaningful adoption.
- **Wrike and Smartsheet are underserved.** Enterprise-popular tools with minimal MCP representation.
- **No cross-platform migration tools.** Nothing helps you move issues between Jira and Linear, or sync projects across platforms, via MCP.
- **GitLab Issues MCP is fragmented.** GitLab's issue tracker is widely used but MCP support is scattered across generic GitLab servers rather than purpose-built project management tools.
- **No Shortcut (formerly Clubhouse) server with adoption.** Despite its popularity with engineering teams, MCP support is minimal.

---

*This guide is part of our [MCP Server Directory](/guides/best-mcp-servers/). We research and compare MCP servers so you don't have to. Updated March 2026.*

---
title: "Product Management & Roadmapping MCP Servers — Jira, Linear, Productboard, Aha!, Monday.com, and More"
date: 2026-04-26T20:00:00+09:00
description: "Product management MCP servers reviewed: Atlassian Jira official remote MCP + sooperset community (5K stars, 72 tools), Linear official hosted (OAuth 2.1, Streamable HTTP, initiatives + milestones), Productboard community (20+ tools, features + objectives + OKRs), Aha! official (3 tools read-only + cedricziel 12 tools with vector embeddings), Monday.com official (15+ tools + dynamic API, hosted MCP), Asana official hosted + community (50+ tools), ClickUp community (150+ tools, OAuth 2.1), Shortcut official (60+ tools, 11 categories, hosted), Notion official (4.3K stars, 22 tools, hosted), Plane official (55+ tools, Python), Fibery official (27 stars, dynamic schema), Canny (37 tools, feedback triage), PostHog official (27+ tools, product analytics), LaunchDarkly official (28 tools, feature flags), Mixpanel official (hosted, beta), Amplitude official (hosted, skills-based). Rating: 4.5/5."
og_description: "Product management MCP servers: Jira (official remote + 5K-star community), Linear (official hosted, OAuth 2.1), Productboard (20+ tools), Aha! (official + vector embeddings), Monday.com (official hosted), Asana (official hosted), ClickUp (150+ tools), Shortcut (60+ tools), Notion (4.3K stars), Plane (55+ tools). Rating: 4.5/5."
content_type: "Review"
card_description: "Product management MCP servers are among the most mature and well-served categories in the MCP ecosystem. Nearly every major PM tool now ships an official MCP server — Atlassian (Jira + Confluence), Linear, Monday.com, Asana, Shortcut, Notion, Aha!, and Plane all have official implementations. The community ecosystem is equally strong: sooperset/mcp-atlassian has 5,000 stars and 72 tools covering Jira + Confluence, roychri/mcp-server-asana offers 50+ tools, and taazkareem/clickup-mcp-server provides 150+ enterprise-grade tools. The trend toward hosted remote MCP is dominant — Atlassian, Linear, Monday.com, Asana, Shortcut, and Notion all offer zero-config hosted endpoints with OAuth. Feature request management (Canny with 37 tools and built-in PM prompts), product analytics (PostHog 27+ tools, Mixpanel hosted, Amplitude hosted), and feature flag management (LaunchDarkly 28 tools) round out the PM workflow. Productboard is the notable gap among dedicated PM tools — only community servers exist despite its market position. The dedicated roadmapping tools (Roadmunk, airfocus, Craft.io) have no MCP servers at all, though general-purpose PM tools with roadmapping features (Linear initiatives, Monday.com, Aha!) fill much of that gap. Rating: 4.5/5 — the strongest vendor participation of any enterprise software category, with comprehensive tool coverage and mature auth patterns."
last_refreshed: 2026-04-26
---

Product management is one of the **best-served categories in the entire MCP ecosystem**. Nearly every major PM tool now ships an official MCP server, and the community ecosystem is deep. **Atlassian** (Jira + Confluence), **Linear**, **Monday.com**, **Asana**, **Shortcut**, **Notion**, **Aha!**, and **Plane** all have official MCP servers. The community adds heavyweight implementations for **ClickUp** (150+ tools) and **Jira** (5,000 stars). **Hosted remote MCP** is the dominant pattern — most vendors offer zero-config endpoints with OAuth. Part of our **[Business & Productivity](/categories/business-productivity/)** category.

This review covers **issue tracking and project management** (Jira, Linear, Asana, Monday.com, ClickUp, Shortcut, Plane), **dedicated product management** (Productboard, Aha!, Fibery), **knowledge and documentation** (Notion), **feature request management** (Canny), **product analytics** (PostHog, Mixpanel, Amplitude), and **feature flag management** (LaunchDarkly). For CRM platforms, see our [CRM MCP Servers](/reviews/crm-mcp-servers/) review. For IT service management, see [ITSM MCP Servers](/reviews/itsm-it-service-management-mcp-servers/).

The headline finding: **vendor participation is extraordinary** — 8+ vendors ship official MCP servers, most with hosted remote endpoints. **Atlassian leads on ecosystem depth** with an official remote MCP plus a 5,000-star community server. **Linear leads on product-management-specific features** with initiatives, milestones, and project updates built into its official MCP. **Monday.com differentiates with dynamic API tools** that give AI agents access to the full GraphQL surface. **The biggest gap: dedicated roadmapping tools** — Roadmunk, airfocus, and Craft.io have zero MCP presence.

## Issue Tracking & Project Management

### Atlassian Jira + Confluence (Official + Community)

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| [Atlassian Remote MCP](https://www.atlassian.com/platform/remote-mcp-server) | — | Hosted | Proprietary | Rovo Search + CRUD | Yes |
| [sooperset/mcp-atlassian](https://github.com/sooperset/mcp-atlassian) | ~5,000 | Python | MIT | 72 | No |

**Atlassian** offers both an official hosted remote MCP and the most popular community PM MCP server in the ecosystem.

The **official Rovo MCP server** provides secure, OAuth-authenticated access to Jira and Confluence. Key capabilities include Rovo Search across all Atlassian products, bulk creation of Confluence pages and Jira issues, data summarization, and full CRUD operations. Access respects user-level permissions — the AI agent can only access what the authenticated user can access. Free for all Atlassian Cloud customers. Rate limits vary by plan: 500/hr (Free), 1,000/hr (Standard), up to 10,000/hr (Enterprise). No FedRAMP or HIPAA support yet.

The community **sooperset/mcp-atlassian** server is a powerhouse — **72 tools** covering both Jira and Confluence, supporting Cloud and Server/Data Center (Confluence v6.0+, Jira v8.14+). Authentication via API tokens, Personal Access Tokens, or OAuth 2.0. Supports HTTP transport (SSE + Streamable HTTP). MIT license. At ~5,000 stars, it's one of the most starred MCP servers of any category.

The Jira ecosystem extends further: **blue7wings/mcp-jira-server** focuses on time tracking and version/release management, **guanghuang/jira-mcp** provides lightweight access, and **cfdude/mcp-jira** covers core issue operations. Multiple enterprise-grade MCP gateway solutions (MintMCP, Workato, CData) also provide managed Jira integration.

### Linear (Official + Community)

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| [Linear Official MCP](https://mcp.linear.app/mcp) | — | Hosted | Proprietary | Issues + Projects + Initiatives | Yes |
| [tacticlaunch/mcp-linear](https://github.com/tacticlaunch/mcp-linear) | 133 | TypeScript | MIT | Multiple | No |
| [jerhadf/linear-mcp-server](https://github.com/jerhadf/linear-mcp-server) | 344 | JavaScript | MIT | 5 | No (deprecated) |

**Linear** expanded its official MCP server in **February 2026** with product-management-specific features that go beyond basic issue tracking:

- **Create and edit initiatives** — strategic themes that group projects
- **Create and edit initiative updates** — communicate progress on strategic goals
- **Create and edit project milestones** — track delivery checkpoints
- **Issues, projects, comments** — find, create, update across workspaces

The official server at `mcp.linear.app/mcp` uses **OAuth 2.1** with dynamic client registration (also supports Bearer token). Streamable HTTP transport. Works natively in Claude and Cursor; other clients via `mcp-remote` module.

The community ecosystem includes **tacticlaunch/mcp-linear** (133 stars, TypeScript, MIT, issue/project/team management) and the now-deprecated **jerhadf/linear-mcp-server** (344 stars, which explicitly recommends migrating to the official server). **dvcrn/mcp-server-linear** adds multi-workspace support.

### Asana (Official + Community)

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| [Asana Official MCP](https://mcp.asana.com/v2/mcp) | — | Hosted | Proprietary | Task + Project management | Yes |
| [roychri/mcp-server-asana](https://github.com/roychri/mcp-server-asana) | 137 | TypeScript | MIT | 50+ | No |
| [adlio/asanamcp](https://github.com/adlio/asanamcp) | — | Rust | — | — | No |
| [n0zer0d4y/asana-project-ops](https://github.com/n0zer0d4y/asana-project-ops) | — | TypeScript | — | Batch ops | No |

**Asana** provides an official hosted MCP at `mcp.asana.com/v2/mcp` with OAuth authentication and Streamable HTTP transport. The deprecated V1 Beta SSE endpoint at `mcp.asana.com/sse` shuts down **May 11, 2026**. Works with Claude, ChatGPT, and other MCP clients.

The community **roychri/mcp-server-asana** is excellent — **50+ tools** with read-only mode option, advanced task filtering with custom fields, resource templates, and a comprehensive prompt system. MIT license. **n0zer0d4y/asana-project-ops** adds batch operations, direct section assignment, and selective tool activation for high-efficiency AI workflows. **adlio/asanamcp** provides a Rust implementation for teams that want STDIO transport.

### Monday.com (Official)

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| [mondaycom/mcp](https://github.com/mondaycom/mcp) | 396 | TypeScript | MIT | 15+ standard + dynamic API | Yes |

**Monday.com** ships an official MCP server with two modes of operation:

1. **Standard tools** (15+) — boards, items, columns, groups, updates, custom activities, user search, workflow automation
2. **Dynamic API tools** (beta) — unlocks the **full Monday.com GraphQL API surface** dynamically, letting AI agents execute any API operation without hardcoded tool definitions

The hosted MCP at `mcp.monday.com/mcp` is the recommended zero-config option (OAuth authentication). Local installation also available via npm with API token. Read-only mode supported. Apps Framework tools included for developers building Monday.com integrations. MIT license. 396 stars.

### ClickUp (Community)

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| [taazkareem/clickup-mcp-server](https://github.com/taazkareem/clickup-mcp-server) | ~460+ | JavaScript/TS | Proprietary | 150+ | No |
| [Nazruden/clickup-mcp-server](https://github.com/Nazruden/clickup-mcp-server) | — | TypeScript | — | — | No |
| [hauptsacheNet/clickup-mcp](https://github.com/hauptsacheNet/clickup-mcp) | — | TypeScript | — | Search + CRUD | No |

**ClickUp** has no official MCP server but has the largest community server by tool count. **taazkareem/clickup-mcp-server** provides **150+ enterprise-grade tools** covering tasks, checklists, sprints, comments, tags, spaces, lists, folders, files, docs, chat, and time tracking. Features OAuth 2.1 + API key hybrid auth, fuzzy search, OKR tracking, document management, file attachments, multi-workspace support, and Docker deployment. The previous public repo had 460+ stars and thousands of weekly npm downloads. Note: this is a **proprietary/paid** offering, unlike most PM MCP servers.

Multiple other community implementations exist from Nazruden, hauptsacheNet, DiversioTeam, and Leanware-io, all offering varying levels of ClickUp integration.

### Shortcut (Official)

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| [useshortcut/mcp-server-shortcut](https://github.com/useshortcut/mcp-server-shortcut) | 98 | TypeScript | MIT | 60+ | Yes |

**Shortcut** (formerly Clubhouse) ships one of the most comprehensive official PM MCP servers. **60+ tools across 11 categories** covering stories, epics, docs, iterations, milestones, labels, members, workflows, and more. The hosted server requires **no setup** — authentication handled via OAuth with no API token or local installation needed. Local installation also available with API token for teams that prefer it.

Notable features: read-only mode, tool limiting via environment variable (useful for restricting AI agent scope), and very active development (401 commits). MIT license. 98 stars.

### Plane (Official)

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| [makeplane/plane-mcp-server](https://github.com/makeplane/plane-mcp-server) | 204 | Python | MIT | 55+ | Yes |

**Plane** — the open-source project management tool — ships an official MCP server with **55+ tools across 8 categories**: projects, issues, cycles, modules, initiatives, work logs, labels, and states. Built with FastMCP and Pydantic models for type safety. Supports stdio, SSE, and Streamable HTTP transports.

Authentication via API Key + Workspace Slug (stdio) or OAuth/PAT (remote HTTP). The server replaced an earlier Node.js implementation with a Python+FastMCP rewrite. MIT license. 204 stars. Active development with April 2026 updates.

## Dedicated Product Management Tools

### Productboard (Community)

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| [Enreign/productboard-mcp](https://github.com/Enreign/productboard-mcp) | 8 | TypeScript | MIT | 20+ | No |
| [kenjihikmatullah/productboard-mcp](https://github.com/kenjihikmatullah/productboard-mcp) | 11 | TypeScript | MIT | 10 | No |

**Productboard** — one of the most popular dedicated product management platforms — has **no official MCP server**. Two community implementations fill the gap:

**Enreign/productboard-mcp** is the more comprehensive option with **20+ tools** covering features, product hierarchy, customer notes, objectives, key results, and release management. Supports Bearer token (default) and OAuth2 authentication. Includes configurable rate limiting, retry logic, and response caching. MIT license.

**kenjihikmatullah/productboard-mcp** is a lighter alternative with **10 tools** focused on company, component, feature, note, and product retrieval plus status management. MIT license.

The absence of an official Productboard MCP server is a notable gap given the platform's market position in dedicated product management. Productboard is available through **Zapier MCP** and **Composio** as managed integrations.

### Aha! (Official + Community)

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| [aha-develop/aha-mcp](https://github.com/aha-develop/aha-mcp) | 6 | TypeScript | ISC | 3 | Yes |
| [cedricziel/aha-mcp](https://github.com/cedricziel/aha-mcp) | 6 | TypeScript | MIT | 12 | No |
| [popand/aha-mcp](https://github.com/popand/aha-mcp) | 2 | TypeScript | ISC | 4 | No |

**Aha!** ships an official MCP server, though it's **read-only and minimal** — just 3 tools (`get_record`, `get_page`, `search_documents`). Supports stdio and SSE transport. API token authentication. The official blog promotes integration with GitHub Copilot, Cursor, Claude Code, OpenAI Codex, and Devin — passing feature titles, descriptions, and to-dos to AI coding tools.

The community **cedricziel/aha-mcp** is significantly more capable with **12 tools** and a standout feature: **vector embeddings for semantic search**. Uses sentence transformers + SQLite vector extensions to enable offline semantic queries against Aha! data. Includes offline database sync to local SQLite, hybrid live API + cached queries, incremental updates, and three transport modes (stdio, SSE, HTTP). MIT license. OAuth 2.0 and Bearer token support.

**popand/aha-mcp** is a fork of the official server that adds `create_feature` capability — the one write tool the official server is missing.

### Fibery (Official)

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| [Fibery-inc/fibery-mcp-server](https://github.com/Fibery-inc/fibery-mcp-server) | 27 | Python | — | Dynamic | Yes |

**Fibery** takes a schema-driven approach similar to Planhat. Instead of hardcoded tools, the MCP server **dynamically discovers your Fibery workspace structure** — databases, fields, types, and relationships. You can query entities using natural language, create new entities, and update existing ones through conversational interfaces. The server retrieves database schemas and provides flexible access through the Fibery API.

Python-based, available on PyPI. 27 stars, 2.2K downloads. Works with Claude Desktop and any MCP-compatible client.

## Knowledge & Documentation

### Notion (Official)

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| [makenotion/notion-mcp-server](https://github.com/makenotion/notion-mcp-server) | ~4,300 | TypeScript | — | 22 | Yes |
| [Notion Remote MCP](https://mcp.notion.com/mcp) | — | Hosted | Proprietary | — | Yes |

**Notion** has the **most starred PM MCP server** at ~4,300 stars. Version 2.0 introduced "data sources" as the primary abstraction for databases (migrating from API 2025-09-03). 22 tools covering pages, databases, blocks, users, comments, and search. Docker support.

**Important:** Notion is prioritizing the **hosted remote MCP** at `mcp.notion.com/mcp` with OAuth one-click install, and may sunset the local server repository. Issues and PRs on the local repo are not actively monitored. Teams should plan to migrate to the hosted endpoint.

The community ecosystem is extensive: **suekou/mcp-notion-server**, **awkoy/notion-mcp-server**, **ramidecodes/mcp-server-notion**, and others provide alternative implementations with varying feature sets.

## Feature Request Management

### Canny (Official + Community)

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| Canny Official MCP | — | Hosted | Proprietary | Multiple | Yes |
| [opensourceops/canny-mcp-server](https://github.com/opensourceops/canny-mcp-server) | — | TypeScript | — | 37 | No |

**Canny** provides both an official MCP server and a feature-rich community implementation. The official server works with ChatGPT and Claude, available to teams on the **Pro plan** and above (Ideas beta). Recent updates added portal data alongside idea data, List Insights and List Idea Comments tools, and the ability to **merge ideas directly via MCP** for deduplication.

The community **opensourceops/canny-mcp-server** is impressive — **37 tools** with Jira linking, batch operations, ETA management, company MRR tracking, and PM-focused workflows. Runs in **read-only mode by default** (19 read-only tools). Ships with **5 built-in prompts**: `weekly_triage`, `sprint_planning`, `executive_summary`, `jira_sync_status`, and `customer_impact` — making it one of the few PM MCP servers with opinionated workflow support.

## Product Analytics

### PostHog (Official)

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| [PostHog/mcp](https://github.com/PostHog/mcp) | ~140 | — | — | 27+ | Yes |

**PostHog** ships an official MCP server with **27+ tools** covering analytics, feature flags, experiments, error tracking, and prompt management. Read-only mode available. One-command installation into 6+ IDEs. The standalone repo was archived January 2026 — the server now lives in the PostHog monorepo. Hosted MCP at `mcp.posthog.com`.

### Mixpanel (Official)

| Server | Transport | Auth | Tools | Official |
|--------|-----------|------|-------|----------|
| Mixpanel MCP Server | Hosted HTTP | OAuth | Events + Funnels + Flows + Retention | Yes |

**Mixpanel** provides an official hosted MCP server (beta) giving AI assistants direct access to query events, funnels, flows, retention, and session replays using natural language. Positioned as "conversational product analytics."

### Amplitude (Official)

| Server | Transport | Auth | Tools | Official |
|--------|-----------|------|-------|----------|
| Amplitude MCP Server | Hosted HTTP (`mcp-server.prod.us-west-2.amplitude.com/v1/mcp`) | — | Skills-based | Yes |

**Amplitude** ships an official hosted MCP with a **skills-based architecture** — reusable analysis and instrumentation skills covering charts, dashboards, experiments, session replays, reliability, AI agent analytics, and tracking workflows. Configurable in Claude Code, Cursor, Claude, and Codex. Community server **silviorodrigues/amplitude-mcp** also available for direct API access.

## Feature Flag Management

### LaunchDarkly (Official)

| Server | Stars | Language | License | Tools | Official |
|--------|-------|----------|---------|-------|----------|
| [launchdarkly/mcp-server](https://github.com/launchdarkly/mcp-server) | 20 | TypeScript | MIT | 28 | Yes |

**LaunchDarkly** ships an official MCP server for feature flag management — essential infrastructure for product managers controlling gradual rollouts. **28 tools** covering flag creation, configuration, targeting rules, toggle management, AI configs, and gradual rollouts across multiple environments. Hosted MCP also available. MIT license. Works with Cursor, Claude Code, and other compatible editors.

## What's Missing

Several notable product management tools have **no MCP servers** (official or community):

- **Roadmunk** — dedicated roadmapping tool, no MCP server
- **airfocus** — product management and prioritization platform, no MCP server
- **Craft.io** — product management platform, no MCP server
- **Pivotal Tracker** — approaching end-of-life, no MCP server
- **Rally (Broadcom)** — enterprise agile, no MCP server
- **Targetprocess (IBM)** — SAFe/enterprise agile, no MCP server
- **Height** — modern project management, no MCP server found
- **Wrike** — only community "2026 Complete" series servers via third-party bundles
- **Teamwork** — official GitHub repo exists ([Teamwork/mcp](https://github.com/Teamwork/mcp)) but limited documentation

The **dedicated roadmapping tools** are the most conspicuous absence. Teams needing AI-powered roadmapping must use general-purpose PM tools with roadmapping features (Linear initiatives, Monday.com, Aha! roadmaps) rather than specialized roadmapping software.

**Productboard** having only community servers — despite being one of the top dedicated PM platforms — is also notable. Compare this to Aha!, which ships an official server (albeit minimal).

## Key Trends

1. **Hosted remote MCP is the default** — Atlassian, Linear, Monday.com, Asana, Shortcut, Notion, PostHog, Mixpanel, and Amplitude all offer hosted endpoints. Local installation is becoming the fallback, not the primary path.

2. **OAuth is standard** — most vendors use OAuth 2.0/2.1 for hosted servers, with API tokens as fallback for local installations. This is more mature than many other MCP categories where API keys dominate.

3. **Dynamic tools are emerging** — Monday.com (dynamic API tools), Planhat (3 meta-tools), and Fibery (schema-driven) all let AI agents discover and interact with arbitrary data structures rather than using hardcoded tool definitions. This pattern reduces maintenance burden and adapts to custom configurations.

4. **PM-specific features beyond CRUD** — Linear's initiatives and milestones, Canny's built-in PM prompts (weekly triage, sprint planning), and PostHog's experiment management show vendors tailoring MCP tools for product management workflows rather than just exposing generic APIs.

5. **Read-only modes are common** — Shortcut, Asana, ClickUp, PostHog, and Canny all offer read-only modes. This reflects enterprise caution about AI agents making changes to production project management data.

## Bottom Line

**Rating: 4.5/5** — Product management has the strongest vendor participation of any enterprise software category in the MCP ecosystem. Eight or more vendors ship official MCP servers, most with hosted remote endpoints and OAuth authentication. The community ecosystem adds depth where vendors haven't gone far enough (ClickUp's 150+ tools, Asana's 50+ tools, Canny's 37 tools with PM prompts). Product analytics coverage is excellent with PostHog, Mixpanel, and Amplitude all offering official servers. The only gaps are dedicated roadmapping tools (Roadmunk, airfocus, Craft.io) and Productboard's lack of an official server. For product managers, the MCP ecosystem is production-ready.

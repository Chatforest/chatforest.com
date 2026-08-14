---
title: "BI & Reporting MCP Servers — Tableau, Power BI, Grafana, Metabase, Looker, and Superset"
date: 2026-03-17T19:40:00+09:00
description: "BI and reporting platform MCP servers reviewed: Grafana official (3,350+ stars, Go, 100+ tools, hosted remote MCP + gcx CLI), Power BI official (1,060+ stars, MIT, 21 tool categories + remote server), Tableau (322 stars, v4.3+), Metabase NOW OFFICIAL built-in MCP in v60, Looker managed MCP at Next '26, Superset NATIVE MCP in 5.0. Rating: 5/5."
og_description: "BI & Reporting MCP servers: Grafana (3,350+ stars, 100+ tools, hosted remote MCP), Power BI (1,060+ stars, 21 tool categories), Tableau (322 stars), Metabase NOW OFFICIAL (v60 built-in MCP), Looker managed MCP, Superset native MCP (5.0+). Rating: 5/5."
content_type: "Review"
card_description: "Business intelligence now has the strongest MCP coverage of any category — every major BI platform ships official MCP server support. Grafana leads with 3,350+ stars and 100+ tools plus a hosted remote MCP server. Metabase shipped a built-in MCP server in v60 (April 2026). Apache Superset 5.0 includes native MCP. Google announced a managed Looker MCP server at Next '26. Microsoft Power BI passed 1,000 stars. Tableau passed 300 stars and continues shipping releases multiple times per week. The former gap — no official Metabase or Superset servers — is now fully closed."
last_refreshed: 2026-08-14
sources_audited: 2026-08-14
---

Business intelligence and reporting platforms have become the single strongest MCP category we track. Every major BI vendor — Grafana, Microsoft Power BI, Salesforce Tableau, Google Looker, Metabase, and Apache Superset — now ships official MCP server support. The last two gaps closed in April 2026: Metabase shipped a built-in MCP server in v60, and Apache Superset 5.0 includes native MCP integration. Combined with Grafana's hosted remote MCP server announced at GrafanaCON 2026 and Google's managed Looker MCP at Next '26, this category has gone from "strong" to "complete."

The landscape is now **all vendor-backed**: six out of six major BI platforms have official MCP servers, with community servers providing additional breadth. Part of our **[Data & Analytics](/categories/data-analytics/)** category.

## Grafana — Official Server

| Detail | Info |
|--------|------|
| [grafana/mcp-grafana](https://github.com/grafana/mcp-grafana) | 3,350+ stars |
| Language | Go |
| Transport | stdio, HTTP, hosted remote |
| Tools | 100+ |

The official Grafana MCP server remains the most popular BI-related MCP server by a wide margin, and it has expanded significantly since our initial review — from 40+ tools to 70+ by April 2026, and to **100+ tools** as of this update (August 2026), across dashboards, datasources, Prometheus, Loki, InfluxDB, ClickHouse, CloudWatch, Athena, Elasticsearch/OpenSearch, Quickwit, Snowflake, alerting, OnCall, admin, incidents, Sift investigations, Pyroscope profiling, Agent Observability, annotations, snapshots, provisioning, navigation, and rendering — see the full [tool table](https://github.com/grafana/mcp-grafana#tools) in the repo README.

### What's New (April 2026)

**Hosted remote MCP server.** At [GrafanaCON 2026](https://grafana.com/blog/2025/11/25/save-the-date-grafanacon-2026-is-coming-to-barcelona-in-april/) (April 20–22, 2026), Grafana [launched a hosted remote MCP server](https://grafana.com/blog/grafana-assistant-everywhere/) at `mcp.grafana.com/mcp` — no local installation required, documented at [grafana.com/docs](https://grafana.com/docs/grafana-cloud/machine-learning/assistant/configure/cloud-mcp/). Point any MCP client at the endpoint to get access to metrics, logs, traces, dashboards, alerts, incidents, and more from your Grafana Cloud instance. This eliminates the biggest friction point of the self-hosted approach.

**gcx CLI tool.** Grafana also shipped [gcx](https://github.com/grafana/gcx) (announced in the same [GrafanaCON 2026 roundup](https://grafana.com/blog/grafanacon-2026-announcements/)), a new CLI that surfaces Grafana Cloud data inside agentic development environments (Claude Code, Cursor, GitHub Copilot). The motivation: engineers shouldn't have to context-switch out of their editor to check dashboards when something breaks. gcx collapses the editor↔Grafana loop.

**o11y-bench.** Grafana open-sourced [grafana/o11y-bench](https://github.com/grafana/o11y-bench), a benchmark for evaluating AI agents on observability workflows. It runs agents against a real Grafana stack with access to the MCP server — useful for teams evaluating how well their agents handle production monitoring.

**Tool count nearly doubled, then kept growing.** From 40+ to 70+ tools by April 2026, with new coverage for InfluxDB, ClickHouse, CloudWatch, Elasticsearch, and expanded Sift investigation capabilities. By August 2026 the [tool table in the README](https://github.com/grafana/mcp-grafana#tools) lists 100+ tools, adding Athena, Snowflake, Quickwit, Pyroscope profiling, and a new Agent Observability category. Dashboard patch operations allow targeted modifications without full JSON replacement.

### What Works Well

**Comprehensive tool coverage.** 100+ tools make this the deepest BI MCP tool set available. Dashboard discovery, retrieval, modification, and patch operations. Datasource querying across Prometheus, Loki, ClickHouse, CloudWatch, Athena, InfluxDB, Snowflake, Quickwit, and Elasticsearch/OpenSearch. Alert rule management, notification routing, incident response, annotation management, and Sift investigation.

**Context-window optimization.** Dashboard content is optimized for LLM consumption — large Grafana dashboards that would blow up a context window are intelligently summarized. JSONPath-based property extraction lets agents pull specific data without loading entire dashboards.

**Configurable tool loading.** You can choose which tools to expose to the MCP client. If you only need dashboard queries and don't want alerting tools taking up context window space, you can disable them. This is best-practice MCP server design.

**Observability ecosystem integration.** A separate official MCP server exists for [Loki](https://github.com/grafana/loki-mcp) (log querying), and an [experimental one for k6](https://github.com/grafana/mcp-k6) (load testing). Tracing is different from when we last checked: the standalone [grafana/tempo-mcp-server](https://github.com/grafana/tempo-mcp-server) repo was archived on June 5, 2026 in favor of an [MCP server built directly into Tempo](https://grafana.com/docs/tempo/latest/api_docs/mcp-server/) itself (enabled via `--query-frontend.mcp-server.enabled=true`), announced in the [Tempo 2.9 release](https://grafana.com/blog/grafana-tempo-2-9-release-mcp-server-support-traceql-metrics-sampling-and-more/). Together with the core Grafana MCP, this still gives AI agents access to the entire Grafana observability stack — just via an embedded server for traces rather than a separate repo.

**Admin capabilities.** Team, user, and role management tools with RBAC permission support. Useful for automating Grafana administration, not just querying.

### What Doesn't Work Well

**Requires Grafana 9.0+.** Older Grafana installations won't work with the full feature set. Given Grafana's rapid release cycle, many production deployments may still be on earlier versions.

**RBAC complexity.** The service account token needs the right permissions for each tool category. Misconfiguration can lead to confusing partial failures where some tools work and others silently fail.

## Power BI — Official Microsoft Servers

Microsoft offers **two** official MCP servers for Power BI, each targeting a different use case:

### Modeling MCP Server

| Detail | Info |
|--------|------|
| [microsoft/powerbi-modeling-mcp](https://github.com/microsoft/powerbi-modeling-mcp) | 1,060+ stars |
| License | MIT |
| Transport | stdio |
| Tool categories | 21 |

The Modeling MCP server runs locally and gives AI agents full semantic modeling capabilities — creating and modifying tables, columns, measures, relationships, DAX queries, security roles, calculation groups, and hierarchies. Stars grew from 507 to 702 (+38%) between our initial review and April 2026, and have kept climbing — 1,060+ as of this update (August 2026), per the [repo's star count](https://github.com/microsoft/powerbi-modeling-mcp). The [README's tool table](https://github.com/microsoft/powerbi-modeling-mcp#%EF%B8%8F-available-tools) lists 21 tool categories (not 22, as we previously stated). The [VS Code Marketplace listing](https://marketplace.visualstudio.com/items?itemName=analysis-services.powerbi-modeling-mcp) shows the extension at v0.5.12 (up from the v0.1.9 example in the docs at our last check), with 52+ commits on the repo, and it remains in Public Preview.

**What stands out:** Bulk operations on hundreds of objects simultaneously with transaction support. Best-practice enforcement lets agents evaluate and apply modeling standards automatically. Supports Power BI Desktop, Fabric workspaces, and PBIP project files. Safety defaults use the MCP Elicitation protocol requiring user confirmation before modifications, with explicit `--skipconfirmation`, `--readonly`, and `--readwrite` flags. Also available as a [VS Code extension](https://marketplace.visualstudio.com/items?itemName=analysis-services.powerbi-modeling-mcp).

### Remote MCP Server (Preview)

The Remote MCP server is a hosted Microsoft endpoint for querying Power BI semantic models. It generates and executes DAX queries using Copilot's intelligence — the same query generation engine behind Copilot for Power BI.

**What stands out:** No local installation required. Schema-aware querying means agents automatically learn model structure. Uses the authenticated user's Entra ID permissions, so data access controls are enforced. Works with any MCP client (VS Code/GitHub Copilot, Claude Desktop, etc.).

**The split makes sense:** Use Modeling for development workflows (building and modifying models), use Remote for analysis workflows (querying existing models). Most teams will want both.

### What Doesn't Work Well

**Preview status for Remote server.** The remote endpoint is still in preview, which means breaking changes are possible.

**Windows-centric for Modeling.** The local modeling server connects to Power BI Desktop, which only runs on Windows. Cross-platform developers working on Macs or Linux need the Remote server or Fabric workspace mode.

**Entra ID requirement.** Both servers require Microsoft Entra ID (Azure AD) authentication. Teams not already in the Microsoft ecosystem face a higher setup barrier.

## Tableau — Official Server

| Detail | Info |
|--------|------|
| [tableau/tableau-mcp](https://github.com/tableau/tableau-mcp) | 322 stars |
| Language | TypeScript |
| License | Apache-2.0 |
| Transport | stdio, HTTP |

Tableau's official MCP server focuses on three capabilities: data querying, content discovery, and visual rendering. It's designed to help AI agents "see and understand data" through Tableau's semantic layer. Branded as "Tableau Next MCP," it grounds AI in Tableau's semantic context with admin-controlled allowlists per agent.

### What's New (April 2026)

**Steady growth.** Stars grew from 202 to 248 (+23%), commits from 159 to 186, and releases from ~17 to 33 between our initial review and April 2026, going from v1.17.12 to v1.18.5, showing consistent investment.

**Still shipping fast (August 2026 update).** The pace has only picked up: [322 stars](https://github.com/tableau/tableau-mcp), 311 commits, and the version scheme jumped from the v1.x line to v4.x — the [most recent tag is v4.3.3](https://github.com/tableau/tableau-mcp/tags), released August 10, 2026, with several releases shipping most weeks.

**SVG download support.** Agents can now download view images as SVGs using the Get View Image endpoint — useful for rendering Tableau visualizations in agent responses.

**Product telemetry.** v1.15.0 introduced product telemetry that sends tool usage data to Tableau. Enabled by default but can be disabled via the `PRODUCT_TELEMETRY_ENABLED` environment variable. Worth noting for privacy-conscious deployments.

### What Works Well

**Multiple deployment options.** NPX for quick setup, Heroku one-click deploy for teams, Docker for production, and Single Executable Applications (SEA) for Windows/Linux that need no Node.js installation. The SEA approach is particularly thoughtful for enterprise IT teams that want to deploy without dependency management.

**Claude Desktop Extension.** Tableau provides a Desktop Extension file that can be installed with a single click — no JSON config editing required. This is the lowest-friction MCP server installation we've seen for any BI platform.

**Active development.** 311 commits and counting, now on the v4.x release line (v4.3.3 as of August 2026). The team is clearly investing in this, with releases shipping multiple times most weeks.

**Content discovery.** Agents can locate and retrieve workbook information and metadata, making it possible to navigate a Tableau Server or Cloud deployment programmatically.

### What Doesn't Work Well

**Limited tool count.** Compared to Grafana's 100+ tools or Power BI's 21 categories, Tableau's MCP server focuses on a narrower set of capabilities. It's read-oriented — querying data and discovering content — rather than a full platform management interface.

**Requires Node.js 22.7.5+.** Unless you use the SEA, the Node.js version requirement is relatively high. Many systems still run Node 18 or 20 LTS.

## Metabase — NOW Official Built-in MCP Server

| Detail | Info |
|--------|------|
| Built-in MCP server | Metabase v60+ |
| Transport | HTTP |
| Authentication | OAuth 2.0 (embedded) |
| Tools | 13 official (per [current docs](https://www.metabase.com/docs/latest/ai/mcp)) |
| Endpoint | `/api/metabase-mcp` |

**This is the biggest change since our initial review.** Metabase shipped a built-in MCP server in [Metabase 60](https://www.metabase.com/releases/metabase-60) (released April 16, 2026), closing the most notable gap in this category. The MCP server is part of Metabase itself — no separate installation, no community dependency, no version mismatch concerns.

### What's New (April 2026)

**Official built-in MCP server.** Metabase v60 introduced a native MCP server that lets AI clients (Claude, ChatGPT, Cursor, VS Code) connect directly. Admins enable it in settings, and users authenticate via Metabase's embedded OAuth 2.0 server — no external OAuth provider needed.

**Permission-scoped access.** The MCP server respects the connecting user's Metabase permissions. Agents see exactly what the user would see in the Metabase UI — no permission escalation, no separate access control layer to manage.

**AI goes open source.** Metabase 60 also made all AI features open source, including natural language querying, SQL code generation, and the Agent API. The MCP server is available across all Metabase plans.

### Update (August 2026): tool set has grown, and it's no longer read-only

At launch the server shipped a small, curated read-only tool set. Checking the [current official docs](https://www.metabase.com/docs/latest/ai/mcp) as of this update, the server now lists **13 tools** and the endpoint path is `/api/metabase-mcp` (not `/api/mcp`, which we previously cited):

- *Interactive:* `render_drill_through`, `visualize_query`
- *Read-only:* `construct_query`, `execute_query`, `query`, `read_resource`, `search`
- *Write/delete:* `create_collection`, `create_dashboard`, `create_question`, `execute_sql`, `update_dashboard`, `update_question`

This is a meaningful change from the original 8-tool, read-only design we described at launch — the official server can now create and update dashboards, questions, and collections, and run raw SQL (an admin can disable `execute_sql` instance-wide). That narrows the gap with the community servers described below, though the community servers still cover more ground (deletion, database/table administration).

### Community Servers Still Valuable

| Detail | Info |
|--------|------|
| [CognitionAI/metabase-mcp-server](https://github.com/CognitionAI/metabase-mcp-server) | 56 stars |
| Language | TypeScript |
| License | MIT |
| Transport | stdio |
| Tools | 81+ |

The CognitionAI server (43→56 stars) and other community servers remain valuable for teams that need deeper API coverage than the official server provides — dashboard CRUD (23 tools), card management (21 tools), database management (13 tools), table management (16 tools), and admin operations. The official server is now better rounded for read/write query and dashboard workflows since its August 2026 tool expansion (above); community servers are still ahead on database/table administration and deletion.

### What Doesn't Work Well

**Official server is still narrower than the community's.** 13 tools vs. the community's 81+ means the official server can create and update dashboards and questions but still can't manage databases/tables or handle admin operations. Teams needing that deeper coverage will still need community servers.

**Requires Metabase v60+.** Teams on older Metabase versions must upgrade to get the official MCP server. The community servers work with older versions.

## Looker — NOW Managed MCP Server + MCP Toolbox

| Detail | Info |
|--------|------|
| Managed MCP server | Native to Looker (Next '26) |
| [Google MCP Toolbox for Databases](https://docs.cloud.google.com/looker/docs/connect-ide-to-looker-using-mcp-toolbox) | Open source |
| [z3z1ma/lookerctl](https://github.com/z3z1ma/lookerctl) | 5 stars |

### What's New (April 2026)

**Managed MCP server native to Looker.** At [Google Cloud Next '26](https://cloud.google.com/blog/products/business-intelligence/looker-updates-for-agentic-bi-at-next26), Google announced a managed MCP server that's native to Looker — not a wrapper around the MCP Toolbox. This is the clearest path to Looker MCP integration: Google hosts it, manages it, and it inherits Looker's security model with admin-defined access controls per agent. This addresses our previous criticism about the fragmented ecosystem.

**MCP Toolbox enhanced.** The MCP Toolbox for Databases (the earlier approach) now includes Looker Health Tools (`health_pulse`, `health_analyze`, `health_vacuum`) for monitoring and administration, plus tools for building visualizations, creating saved Looks (`make_look`), and creating dashboards (`make_dashboard`, `add_dashboard_element`). As of this update, [Google's docs](https://docs.cloud.google.com/looker/docs/connect-ide-to-looker-using-mcp-toolbox) specify MCP Toolbox v0.14.0+ (up from the v0.12.0 release that first added these tools). The Toolbox remains the open-source option for teams wanting more control.

### What Works Well

**Two clear official paths.** The fragmentation concern from our initial review is mostly resolved. Teams now choose between: (1) the managed MCP server for zero-config Looker querying, or (2) the MCP Toolbox for open-source flexibility with visualization building and health monitoring. Both are Google-backed.

**Natural language querying.** Looker's Conversational Analytics API enables asking questions grounded in Looker's semantic layer with automatic SQL generation. Available through both the managed server and the Toolbox.

**LookML development automation.** `lookerctl` (4→5 stars) provides 20 MCP tools focused on LookML development workflows — 66x faster local validation, usage analysis, AB testing, and dependency mapping. Different focus from the query-oriented servers.

**Security model integration.** The managed server inherits Looker's robust security — admins define which AI applications can access what data at what granularity, with audit trails for compliance.

### What Doesn't Work Well

**Managed server details still emerging.** Announced at Next '26 but specific tool lists, transport details, and availability timeline aren't fully documented yet.

**Google Cloud dependency.** The managed MCP server is tightly coupled to Google Cloud. Teams using Looker but hosting elsewhere may need the Toolbox approach.

## Apache Superset — NOW Native MCP Server

| Detail | Info |
|--------|------|
| Native MCP server | Superset 5.0+ |
| Transport | HTTP/HTTPS (JSON-RPC 2.0) |
| Framework | FastMCP |
| Authentication | JWT (JWKS, static key, symmetric, custom) |
| Requires | Python 3.11+ |

**[SIP-187](https://github.com/apache/superset/issues/35498) has landed.** Apache Superset 5.0 includes a [native MCP server](https://superset.apache.org/admin-docs/configuration/mcp-server/) — the proposal we flagged as "on the roadmap" in our initial review is now shipping. This is the most architecturally sophisticated BI MCP integration we've seen: it implements MCP as a standalone FastMCP service that uses Superset as a library, with three deployment options (single process, Docker Compose, Kubernetes with Redis session sharing).

### What's New (April 2026)

**Native MCP server in Superset 5.0.** The server lets AI assistants (Claude, ChatGPT, and other MCP clients) explore data, build charts, create dashboards, and run SQL through natural language. It's built into Superset itself — no external server to install.

**Production-grade security.** Four JWT authentication modes (JWKS, static key, symmetric, custom provider). Full RBAC enforcement — agents have exactly the same permissions as the connecting user in the web UI. Audit logging of all MCP operations to Superset's event logger.

**Response size guards.** Configurable token limits (default 25,000) prevent MCP responses from overwhelming LLM context windows. This shows the team understands the practical constraints of MCP-to-LLM integration.

**Exploration mode.** Unlike traditional APIs that persist immediately, MCP tools default to exploration mode — charts can be previewed and iterated without database persistence, then explicitly saved when ready. Clever design for iterative agent workflows.

**5-layer validation.** Schema → Business Logic → Dataset → Superset Compatibility → Runtime validation catches errors early and provides helpful feedback to LLM agents.

**Redis caching.** Optional Redis-backed response caching for read-heavy workloads, with offset-based pagination for list operations.

### Community Server Still Available

The community [Winding2020/superset-mcp](https://github.com/Winding2020/superset-mcp) (24 stars, 28 tools) remains available for teams not yet on Superset 5.0. Also see [aptro/superset-mcp](https://github.com/aptro/superset-mcp) which bridges 50+ data stores via Superset.

### What Doesn't Work Well

**Requires Superset 5.0+.** Teams on Superset 4.x must upgrade to get the native MCP server. The community servers work with older versions.

**More complex deployment than peers.** The Kubernetes/Redis option is powerful but has more moving parts than Grafana's hosted endpoint or Metabase's built-in server. Single-process mode is simpler but doesn't scale.

## How They Compare

| Platform | Server | Stars | Tools | Official? | Transport | Key Strength |
|----------|--------|-------|-------|-----------|-----------|-------------|
| Grafana | mcp-grafana | 3,350+ | 100+ | Yes | stdio, HTTP, hosted remote | Deepest tool set + hosted remote MCP |
| Power BI | powerbi-modeling-mcp | 1,060+ | 21 categories | Yes | stdio | Semantic modeling + remote DAX querying |
| Tableau | tableau-mcp | 322 | ~10 | Yes | stdio, HTTP | Easiest install (SEA + Claude extension) |
| Metabase | Built-in (v60+) | — | 13 official | Yes | HTTP | Built-in, OAuth 2.0, zero-install |
| Looker | Managed (Next '26) | — | Varies | Yes | Managed | Native to Looker, admin controls |
| Superset | Native (5.0+) | — | Multiple | Yes | HTTP/HTTPS | Exploration mode, 5-layer validation |

## Who Should Use What

**If you use Grafana** — `mcp-grafana` is the best BI MCP server available. 100+ tools cover dashboards, data querying, alerting, incidents, and admin, with a separate official Loki server (Tempo tracing is now built into Tempo itself) for deep observability. New: try the hosted remote MCP server at `mcp.grafana.com/mcp` for zero-install access, or `gcx` CLI for editor integration.

**If you're in the Microsoft ecosystem** — install both Power BI servers. Use Modeling for development, Remote for querying. The Copilot-powered DAX generation in the Remote server is genuinely useful for non-technical users.

**If you use Tableau** — the official server is polished and easy to install, now on the v4.x release line and shipping frequently. The Claude Desktop Extension is a nice touch. Just know that it's more read-oriented than the Grafana or Power BI servers.

**If you use Metabase** — start with the built-in MCP server in Metabase v60+. Its 13 tools now cover query, dashboard, and question workflows, read and write. If you need database/table administration or deletion, supplement with the CognitionAI community server (56 stars, 81+ tools).

**If you use Looker** — the new managed MCP server (announced at Next '26) is the simplest path. For open-source flexibility with visualization building, use the MCP Toolbox. For LookML development, check out `lookerctl`.

**If you use Superset** — upgrade to Superset 5.0 for the native MCP server. Its exploration mode and 5-layer validation are genuinely thoughtful design for AI agent workflows.

## Bottom Line

**Rating: 5 / 5** — This is the strongest MCP category we track, and it just got stronger. The main gap from our initial review — no official Metabase or Superset MCP servers — is now fully closed. Metabase shipped a built-in MCP server in v60 (April 2026), and by August 2026 had expanded it from 8 read-only tools to 13 tools including dashboard/question writes. Apache Superset 5.0 includes native MCP with the most architecturally sophisticated integration in the category. Grafana announced a hosted remote MCP server and gcx CLI at GrafanaCON 2026, and its open-source server's tool count has grown past 100. Google announced a managed Looker MCP server at Next '26. Power BI's modeling server passed 1,000 stars, more than double its count at our initial review. All six major BI platforms now have vendor-backed official MCP support — a clean sweep that no other MCP category has achieved. Upgraded from 4.5 to 5/5.

## Related Guides

- [Domo MCP Server and AI Agent Builder](/guides/domo-mcp-server-enterprise-ai-agents/) — deep dive into Domo's enterprise AI orchestration, interactive dashboard rendering in chat, and the AI Toolkit architecture
- [MCP and Data Visualization / Business Intelligence](/guides/mcp-data-visualization-business-intelligence/) — comprehensive guide covering 80+ servers across the analytics stack

*[ChatForest](/) independently researches MCP servers — we are not affiliated with any of the projects listed. See our [methodology](/about/) for how we evaluate servers. Review written by an AI agent and published transparently.]*

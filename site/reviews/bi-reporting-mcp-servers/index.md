# BI & Reporting MCP Servers — Tableau, Power BI, Grafana, Metabase, Looker, and Superset

> BI and reporting platform MCP servers reviewed: Grafana official (2,900 stars, Go, 70+ tools, hosted remote MCP + gcx CLI), Power BI official (702 stars, MIT, 22 tool categories + remote server), Tableau (248 stars, v1.18.5), Metabase NOW OFFICIAL built-in MCP in v60, Looker managed MCP at Next '26, Superset NATIVE MCP in 5.0. Rating: 5/5.


Business intelligence and reporting platforms have become the single strongest MCP category we track. Every major BI vendor — Grafana, Microsoft Power BI, Salesforce Tableau, Google Looker, Metabase, and Apache Superset — now ships official MCP server support. The last two gaps closed in April 2026: Metabase shipped a built-in MCP server in v60, and Apache Superset 5.0 includes native MCP integration. Combined with Grafana's hosted remote MCP server announced at GrafanaCON 2026 and Google's managed Looker MCP at Next '26, this category has gone from "strong" to "complete."

The landscape is now **all vendor-backed**: six out of six major BI platforms have official MCP servers, with community servers providing additional breadth. Part of our **[Data & Analytics](/categories/data-analytics/)** category.

## Grafana — Official Server

| Detail | Info |
|--------|------|
| [grafana/mcp-grafana](https://github.com/grafana/mcp-grafana) | 2,900 stars |
| Language | Go |
| Transport | stdio, HTTP, hosted remote |
| Tools | 70+ |

The official Grafana MCP server remains the most popular BI-related MCP server by a wide margin, and it has expanded significantly since our initial review — from 40+ tools to **70+ tools** across dashboards (7), datasources (3), Prometheus (6), Loki (4), InfluxDB, ClickHouse (3), CloudWatch (4), Elasticsearch, alerting (5), OnCall (6), admin (8), incidents (4), Sift investigations (5), annotations (6), navigation, and rendering.

### What's New (April 2026)

**Hosted remote MCP server.** At GrafanaCON 2026 (April 21), Grafana launched a hosted remote MCP server at `mcp.grafana.com/mcp` — no local installation required. Point any MCP client at the endpoint to get access to metrics, logs, traces, dashboards, alerts, incidents, and more from your Grafana Cloud instance. This eliminates the biggest friction point of the self-hosted approach.

**gcx CLI tool.** Grafana also shipped [gcx](https://github.com/grafana/gcx), a new CLI that surfaces Grafana Cloud data inside agentic development environments (Claude Code, Cursor, GitHub Copilot). The motivation: engineers shouldn't have to context-switch out of their editor to check dashboards when something breaks. gcx collapses the editor↔Grafana loop.

**o11y-bench.** Grafana open-sourced [grafana/o11y-bench](https://github.com/grafana/o11y-bench), a benchmark for evaluating AI agents on observability workflows. It runs agents against a real Grafana stack with access to the MCP server — useful for teams evaluating how well their agents handle production monitoring.

**Tool count nearly doubled.** From 40+ to 70+ tools, with new coverage for InfluxDB, ClickHouse (3 tools), CloudWatch (4 tools), Elasticsearch, and expanded Sift investigation capabilities. Dashboard patch operations allow targeted modifications without full JSON replacement.

### What Works Well

**Comprehensive tool coverage.** 70+ tools across 16 categories make this the deepest BI MCP tool set available. Dashboard discovery, retrieval, modification, and patch operations. Datasource querying across Prometheus, Loki, ClickHouse, CloudWatch, InfluxDB, and Elasticsearch. Alert rule management, notification routing, incident response, annotation management, and Sift investigation.

**Context-window optimization.** Dashboard content is optimized for LLM consumption — large Grafana dashboards that would blow up a context window are intelligently summarized. JSONPath-based property extraction lets agents pull specific data without loading entire dashboards.

**Configurable tool loading.** You can choose which tools to expose to the MCP client. If you only need dashboard queries and don't want alerting tools taking up context window space, you can disable them. This is best-practice MCP server design.

**Observability ecosystem integration.** Separate official MCP servers exist for [Loki](https://github.com/grafana/loki-mcp) (log querying), [Tempo](https://github.com/grafana/tempo-mcp-server) (distributed tracing), and [k6](https://github.com/grafana/mcp-k6) (load testing). Together with the core Grafana MCP, this gives AI agents access to the entire Grafana observability stack.

**Admin capabilities.** Team, user, and role management tools (8 tools) with RBAC permission support. Useful for automating Grafana administration, not just querying.

### What Doesn't Work Well

**Requires Grafana 9.0+.** Older Grafana installations won't work with the full feature set. Given Grafana's rapid release cycle, many production deployments may still be on earlier versions.

**RBAC complexity.** The service account token needs the right permissions for each tool category. Misconfiguration can lead to confusing partial failures where some tools work and others silently fail.

## Power BI — Official Microsoft Servers

Microsoft offers **two** official MCP servers for Power BI, each targeting a different use case:

### Modeling MCP Server

| Detail | Info |
|--------|------|
| [microsoft/powerbi-modeling-mcp](https://github.com/microsoft/powerbi-modeling-mcp) | 702 stars |
| License | MIT |
| Transport | stdio |
| Tool categories | 22 |

The Modeling MCP server runs locally and gives AI agents full semantic modeling capabilities — creating and modifying tables, columns, measures, relationships, DAX queries, security roles, calculation groups, and hierarchies. Stars have grown from 507 to 702 (+38%) since our initial review, reflecting strong adoption in the Power BI community. The server is at v0.1.9 with 50 commits and remains in Public Preview.

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
| [tableau/tableau-mcp](https://github.com/tableau/tableau-mcp) | 248 stars |
| Language | TypeScript |
| License | Apache-2.0 |
| Transport | stdio, HTTP |

Tableau's official MCP server focuses on three capabilities: data querying, content discovery, and visual rendering. It's designed to help AI agents "see and understand data" through Tableau's semantic layer. Branded as "Tableau Next MCP," it grounds AI in Tableau's semantic context with admin-controlled allowlists per agent.

### What's New (April 2026)

**Steady growth.** Stars grew from 202 to 248 (+23%), commits from 159 to 186, and releases from ~17 to 33. Now at v1.18.5 (up from v1.17.12), showing consistent investment.

**SVG download support.** Agents can now download view images as SVGs using the Get View Image endpoint — useful for rendering Tableau visualizations in agent responses.

**Product telemetry.** v1.15.0 introduced product telemetry that sends tool usage data to Tableau. Enabled by default but can be disabled via the `PRODUCT_TELEMETRY_ENABLED` environment variable. Worth noting for privacy-conscious deployments.

### What Works Well

**Multiple deployment options.** NPX for quick setup, Heroku one-click deploy for teams, Docker for production, and Single Executable Applications (SEA) for Windows/Linux that need no Node.js installation. The SEA approach is particularly thoughtful for enterprise IT teams that want to deploy without dependency management.

**Claude Desktop Extension.** Tableau provides a Desktop Extension file that can be installed with a single click — no JSON config editing required. This is the lowest-friction MCP server installation we've seen for any BI platform.

**Active development.** 186 commits, v1.18.5, 33 releases. The team is clearly investing in this with nearly weekly releases.

**Content discovery.** Agents can locate and retrieve workbook information and metadata, making it possible to navigate a Tableau Server or Cloud deployment programmatically.

### What Doesn't Work Well

**Limited tool count.** Compared to Grafana's 70+ tools or Power BI's 22 categories, Tableau's MCP server focuses on a narrower set of capabilities. It's read-oriented — querying data and discovering content — rather than a full platform management interface.

**Requires Node.js 22.7.5+.** Unless you use the SEA, the Node.js version requirement is relatively high. Many systems still run Node 18 or 20 LTS.

## Metabase — NOW Official Built-in MCP Server

| Detail | Info |
|--------|------|
| Built-in MCP server | Metabase v60+ |
| Transport | Streamable HTTP |
| Authentication | OAuth 2.0 (embedded) |
| Tools | 8 official |
| Endpoint | `/api/mcp` |

**This is the biggest change since our initial review.** Metabase shipped a built-in MCP server in [Metabase 60](https://www.metabase.com/releases/metabase-60) (released April 16, 2026), closing the most notable gap in this category. The MCP server is part of Metabase itself — no separate installation, no community dependency, no version mismatch concerns.

### What's New (April 2026)

**Official built-in MCP server.** Metabase v60 includes a native MCP server at `/api/mcp` that lets AI clients (Claude, ChatGPT, Cursor, VS Code) connect directly. Admins enable it in settings, and users authenticate via Metabase's embedded OAuth 2.0 server — no external OAuth provider needed.

**Permission-scoped access.** The MCP server respects the connecting user's Metabase permissions. Agents see exactly what the user would see in the Metabase UI — no permission escalation, no separate access control layer to manage.

**8 focused tools.** The official server provides: `search`, `get_table`, `get_table_field_values`, `get_metric`, `get_metric_field_values`, `construct_query`, `execute_query`, and `query`. This is deliberately more curated than the community servers' 81+ tools — Metabase chose quality over quantity.

**AI goes open source.** Metabase 60 also made all AI features open source, including natural language querying, SQL code generation, and the Agent API. The MCP server is available across all Metabase plans.

### Community Servers Still Valuable

| Detail | Info |
|--------|------|
| [CognitionAI/metabase-mcp-server](https://github.com/CognitionAI/metabase-mcp-server) | 55 stars |
| Language | TypeScript |
| License | MIT |
| Transport | stdio |
| Tools | 81+ |

The CognitionAI server (43→55 stars, +28%) and other community servers remain valuable for teams that need deeper API coverage than the official 8 tools provide — dashboard CRUD (23 tools), card management (21 tools), database management (13 tools), table management (16 tools), and admin operations. The official server is better for read/query workflows; community servers are better for automation and administration.

### What Doesn't Work Well

**Official server is intentionally limited.** 8 tools vs. the community's 81+ means the official server can't do dashboard creation, card management, or admin operations. Teams needing write access to Metabase objects will still need community servers.

**Requires Metabase v60+.** Teams on older Metabase versions must upgrade to get the official MCP server. The community servers work with older versions.

## Looker — NOW Managed MCP Server + MCP Toolbox

| Detail | Info |
|--------|------|
| Managed MCP server | Native to Looker (Next '26) |
| [Google MCP Toolbox for Databases](https://googleapis.github.io/genai-toolbox/how-to/connect-ide/looker_mcp/) | Open source |
| [z3z1ma/lookerctl](https://github.com/z3z1ma/lookerctl) | 5 stars |

### What's New (April 2026)

**Managed MCP server native to Looker.** At Google Cloud Next '26, Google announced a managed MCP server that's native to Looker — not a wrapper around the MCP Toolbox. This is the clearest path to Looker MCP integration: Google hosts it, manages it, and it inherits Looker's security model with admin-defined access controls per agent. This addresses our previous criticism about the fragmented ecosystem.

**MCP Toolbox enhanced.** The MCP Toolbox for Databases (the earlier approach) now includes Looker Health Tools for monitoring and administration, plus tools for building visualizations, creating saved Looks, and creating dashboards (added in v0.12.0). The Toolbox remains the open-source option for teams wanting more control.

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
| Requires | Python 3.10+ |

**SIP-187 has landed.** Apache Superset 5.0 includes a native MCP server — the proposal we flagged as "on the roadmap" in our initial review is now shipping. This is the most architecturally sophisticated BI MCP integration we've seen: it implements MCP as a standalone FastMCP service that uses Superset as a library, with three deployment options (single process, Docker Compose, Kubernetes with Redis session sharing).

### What's New (April 2026)

**Native MCP server in Superset 5.0.** The server lets AI assistants (Claude, ChatGPT, and other MCP clients) explore data, build charts, create dashboards, and run SQL through natural language. It's built into Superset itself — no external server to install.

**Production-grade security.** Four JWT authentication modes (JWKS, static key, symmetric, custom provider). Full RBAC enforcement — agents have exactly the same permissions as the connecting user in the web UI. Audit logging of all MCP operations to Superset's event logger.

**Response size guards.** Configurable token limits (default 25,000) prevent MCP responses from overwhelming LLM context windows. This shows the team understands the practical constraints of MCP-to-LLM integration.

**Exploration mode.** Unlike traditional APIs that persist immediately, MCP tools default to exploration mode — charts can be previewed and iterated without database persistence, then explicitly saved when ready. Clever design for iterative agent workflows.

**5-layer validation.** Schema → Business Logic → Dataset → Superset Compatibility → Runtime validation catches errors early and provides helpful feedback to LLM agents.

**Redis caching.** Optional Redis-backed response caching for read-heavy workloads, with offset-based pagination for list operations.

### Community Server Still Available

The community [Winding2020/superset-mcp](https://github.com/Winding2020/superset-mcp) (22 stars, 27 tools) remains available for teams not yet on Superset 5.0. Also see [aptro/superset-mcp](https://github.com/aptro/superset-mcp) which bridges 50+ data stores via Superset.

### What Doesn't Work Well

**Requires Superset 5.0+.** Teams on Superset 4.x must upgrade to get the native MCP server. The community servers work with older versions.

**More complex deployment than peers.** The Kubernetes/Redis option is powerful but has more moving parts than Grafana's hosted endpoint or Metabase's built-in server. Single-process mode is simpler but doesn't scale.

## How They Compare

| Platform | Server | Stars | Tools | Official? | Transport | Key Strength |
|----------|--------|-------|-------|-----------|-----------|-------------|
| Grafana | mcp-grafana | 2,900 | 70+ | Yes | stdio, HTTP, hosted remote | Deepest tool set + hosted remote MCP |
| Power BI | powerbi-modeling-mcp | 702 | 22 categories | Yes | stdio | Semantic modeling + remote DAX querying |
| Tableau | tableau-mcp | 248 | ~10 | Yes | stdio, HTTP | Easiest install (SEA + Claude extension) |
| Metabase | Built-in (v60+) | — | 8 official | Yes | Streamable HTTP | Built-in, OAuth 2.0, zero-install |
| Looker | Managed (Next '26) | — | Varies | Yes | Managed | Native to Looker, admin controls |
| Superset | Native (5.0+) | — | Multiple | Yes | HTTP/HTTPS | Exploration mode, 5-layer validation |

## Who Should Use What

**If you use Grafana** — `mcp-grafana` is the best BI MCP server available. 70+ tools cover dashboards, data querying, alerting, incidents, and admin, with separate Loki and Tempo servers for deep observability. New: try the hosted remote MCP server at `mcp.grafana.com/mcp` for zero-install access, or `gcx` CLI for editor integration.

**If you're in the Microsoft ecosystem** — install both Power BI servers. Use Modeling for development, Remote for querying. The Copilot-powered DAX generation in the Remote server is genuinely useful for non-technical users.

**If you use Tableau** — the official server is polished and easy to install at v1.18.5 with 33 releases. The Claude Desktop Extension is a nice touch. Just know that it's more read-oriented than the Grafana or Power BI servers.

**If you use Metabase** — start with the built-in MCP server in Metabase v60+. Its 8 tools cover the most common query workflows. If you need dashboard CRUD or admin operations, supplement with the CognitionAI community server (55 stars, 81+ tools).

**If you use Looker** — the new managed MCP server (announced at Next '26) is the simplest path. For open-source flexibility with visualization building, use the MCP Toolbox. For LookML development, check out `lookerctl`.

**If you use Superset** — upgrade to Superset 5.0 for the native MCP server. Its exploration mode and 5-layer validation are genuinely thoughtful design for AI agent workflows.

## Bottom Line

**Rating: 5 / 5** — This is the strongest MCP category we track, and it just got stronger. The main gap from our initial review — no official Metabase or Superset MCP servers — is now fully closed. Metabase shipped a built-in MCP server in v60 (April 2026). Apache Superset 5.0 includes native MCP with the most architecturally sophisticated integration in the category. Grafana announced a hosted remote MCP server and gcx CLI at GrafanaCON 2026. Google announced a managed Looker MCP server at Next '26. Power BI grew 38% in stars. All six major BI platforms now have vendor-backed official MCP support — a clean sweep that no other MCP category has achieved. Upgraded from 4.5 to 5/5.

## Related Guides

- [Domo MCP Server and AI Agent Builder](/guides/domo-mcp-server-enterprise-ai-agents/) — deep dive into Domo's enterprise AI orchestration, interactive dashboard rendering in chat, and the AI Toolkit architecture
- [MCP and Data Visualization / Business Intelligence](/guides/mcp-data-visualization-business-intelligence/) — comprehensive guide covering 80+ servers across the analytics stack

*[ChatForest](/) independently researches MCP servers — we are not affiliated with any of the projects listed. See our [methodology](/about/) for how we evaluate servers. Review written by an AI agent and published transparently.]*


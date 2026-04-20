# BI & Reporting MCP Servers — Tableau, Power BI, Grafana, Metabase, Looker, and Superset

> BI and reporting platform MCP servers reviewed: Grafana official (2,600 stars, Go, 40+ tools, Prometheus/Loki/dashboards), Power BI official (507 stars, MIT, 22 tool categories +


Business intelligence and reporting platforms have rapidly become one of the best-supported MCP categories. Every major BI vendor — Grafana, Microsoft Power BI, Salesforce Tableau, Google Looker, and the open-source Metabase and Apache Superset — now offers official or high-quality MCP server support. This makes sense: BI platforms sit between raw data and business decisions, and connecting AI agents to dashboards, metrics, and semantic models is a high-value use case.

The landscape splits into two tiers: **vendor-backed official servers** (Grafana, Power BI, Tableau, Looker) with deep platform integration, and **community-driven servers** (Metabase, Superset) with broad API coverage. The official servers tend to focus on curated, safe read operations; the community servers often expose more of the platform's write capabilities. Part of our **[Data & Analytics](/categories/data-analytics/)** category.

## Grafana — Official Server

| Detail | Info |
|--------|------|
| [grafana/mcp-grafana](https://github.com/grafana/mcp-grafana) | 2,600 stars |
| Language | Go |
| Transport | stdio, HTTP |
| Tools | 40+ |

The official Grafana MCP server is the most popular BI-related MCP server by a wide margin. It provides 40+ tools across dashboards, datasources, alerting, incidents, OnCall, and observability — effectively making Grafana a first-class MCP citizen.

### What Works Well

**Comprehensive tool coverage.** Dashboard discovery, retrieval, and modification. Datasource querying across Prometheus, Loki, ClickHouse, CloudWatch, and Elasticsearch. Alert rule management, notification routing, incident response, and annotation management. This is one of the deepest tool sets of any MCP server we've reviewed.

**Context-window optimization.** Dashboard content is optimized for LLM consumption — large Grafana dashboards that would blow up a context window are intelligently summarized. This is a thoughtful touch that shows the team understands how MCP servers actually get used.

**Configurable tool loading.** You can choose which tools to expose to the MCP client. If you only need dashboard queries and don't want alerting tools taking up context window space, you can disable them. This is best-practice MCP server design.

**Observability ecosystem integration.** Separate official MCP servers exist for [Loki](https://github.com/grafana/loki-mcp) (log querying), [Tempo](https://github.com/grafana/tempo-mcp-server) (distributed tracing), and [k6](https://github.com/grafana/mcp-k6) (load testing). Together with the core Grafana MCP, this gives AI agents access to the entire Grafana observability stack.

**Admin capabilities.** Team, user, and role management tools with RBAC permission support. Useful for automating Grafana administration, not just querying.

### What Doesn't Work Well

**Requires Grafana 9.0+.** Older Grafana installations won't work with the full feature set. Given Grafana's rapid release cycle, many production deployments may still be on earlier versions.

**RBAC complexity.** The service account token needs the right permissions for each tool category. Misconfiguration can lead to confusing partial failures where some tools work and others silently fail.

## Power BI — Official Microsoft Servers

Microsoft offers **two** official MCP servers for Power BI, each targeting a different use case:

### Modeling MCP Server

| Detail | Info |
|--------|------|
| [microsoft/powerbi-modeling-mcp](https://github.com/microsoft/powerbi-modeling-mcp) | 507 stars |
| License | MIT |
| Transport | stdio |
| Tool categories | 22 |

The Modeling MCP server runs locally and gives AI agents full semantic modeling capabilities — creating and modifying tables, columns, measures, relationships, DAX queries, security roles, calculation groups, and hierarchies.

**What stands out:** Bulk operations on hundreds of objects simultaneously with transaction support. Best-practice enforcement lets agents evaluate and apply modeling standards automatically. Supports Power BI Desktop, Fabric workspaces, and PBIP project files. Safety defaults require confirmation before first modification, with explicit `--skipconfirmation`, `--readonly`, and `--readwrite` flags.

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
| [tableau/tableau-mcp](https://github.com/tableau/tableau-mcp) | 202 stars |
| Language | TypeScript |
| License | Apache-2.0 |
| Transport | stdio, HTTP |

Tableau's official MCP server focuses on three capabilities: data querying, content discovery, and visual rendering. It's designed to help AI agents "see and understand data" through Tableau's semantic layer.

### What Works Well

**Multiple deployment options.** NPX for quick setup, Heroku one-click deploy for teams, Docker for production, and Single Executable Applications (SEA) for Windows/Linux that need no Node.js installation. The SEA approach is particularly thoughtful for enterprise IT teams that want to deploy without dependency management.

**Claude Desktop Extension.** Tableau provides a Desktop Extension file that can be installed with a single click — no JSON config editing required. This is the lowest-friction MCP server installation we've seen for any BI platform.

**Active development.** 159 commits, v1.17.12 as of March 2026, with regular releases. The team is clearly investing in this.

**Content discovery.** Agents can locate and retrieve workbook information and metadata, making it possible to navigate a Tableau Server or Cloud deployment programmatically.

### What Doesn't Work Well

**Limited tool count.** Compared to Grafana's 40+ tools or Power BI's 22 categories, Tableau's MCP server focuses on a narrower set of capabilities. It's read-oriented — querying data and discovering content — rather than a full platform management interface.

**Requires Node.js 22.7.5+.** Unless you use the SEA, the Node.js version requirement is relatively high. Many systems still run Node 18 or 20 LTS.

## Metabase — Community Servers

| Detail | Info |
|--------|------|
| [CognitionAI/metabase-mcp-server](https://github.com/CognitionAI/metabase-mcp-server) | 43 stars |
| Language | TypeScript |
| License | MIT |
| Transport | stdio |
| Tools | 81+ |

Metabase doesn't have an official MCP server yet, but the community has filled the gap thoroughly. The CognitionAI server (from the Devin team) is the most comprehensive, with 81+ tools across dashboard management (23), card/question management (21), database management (13), table management (16), and additional utilities (9).

### What Works Well

**Massive tool coverage.** 81+ tools cover nearly the entire Metabase API surface — CRUD operations on dashboards, cards, databases, tables, and users. Public sharing, query execution with parameter handling, pivot queries, and schema synchronization are all supported.

**Flexible loading modes.** Essential, all, read-only, and write-only tool loading modes let you control what the AI agent can do. The read-only mode is important for connecting to production Metabase instances safely.

**Multiple community options.** Beyond CognitionAI, there are servers from [Codewalnut](https://github.com/CW-Codewalnut/metabase-mcp-server) (Python, Docker-focused), [easecloudio](https://github.com/easecloudio/mcp-metabase-server) (enterprise-oriented), and [jerichosequitin](https://github.com/jerichosequitin/metabase-mcp) (performance-optimized). Competition drives quality.

### What Doesn't Work Well

**No official backing.** All Metabase MCP servers are community-maintained. If the Metabase API changes in a new release, there's no guarantee these servers will be updated promptly.

**Lower star counts.** The most popular Metabase MCP server has 43 stars. This is a signal of a younger, less battle-tested ecosystem compared to Grafana or Power BI.

## Looker — Google MCP Toolbox + Community

| Detail | Info |
|--------|------|
| [Google MCP Toolbox for Databases](https://googleapis.github.io/genai-toolbox/how-to/connect-ide/looker_mcp/) | Managed |
| [datadaddy89/looker-mcp](https://github.com/datadaddy89/looker-mcp) | Community |
| [z3z1ma/lookerctl](https://github.com/z3z1ma/lookerctl) | 4 stars |

Looker's MCP story is split between Google's official integration (via the MCP Toolbox for Databases) and community servers with different focuses.

### What Works Well

**Google's official path.** The MCP Toolbox for Databases is an open-source MCP server from Google that handles authentication, connection pooling, and secure access to Looker data. It integrates with Looker's Conversational Analytics API for natural language querying. This is the recommended approach for teams already on Google Cloud.

**Natural language querying.** The community `looker-mcp` server enables asking questions like "What are the top 10 products by revenue?" and gets answers grounded in Looker's semantic layer with automatic SQL generation. Supports up to 5 simultaneous Looker Explores per query.

**LookML development automation.** `lookerctl` provides 20 MCP tools focused on LookML development workflows — 66x faster local validation, usage analysis, AB testing, and dependency mapping. Different focus from the query-oriented servers.

**Multiple transports.** The community server supports stdio (Claude Desktop), HTTP Streamable (Claude Web), and Cloud Run deployment for team access.

### What Doesn't Work Well

**Fragmented ecosystem.** There's no single "Looker MCP server" — Google's path uses the MCP Toolbox (generic database connector), community servers target different use cases, and none have significant star counts. It's harder to choose the right one than for other BI platforms.

**Google Cloud dependency.** The official Toolbox path works best within Google Cloud. Teams using Looker but hosting elsewhere face more friction.

## Apache Superset — Community Server

| Detail | Info |
|--------|------|
| [Winding2020/superset-mcp](https://github.com/Winding2020/superset-mcp) | 22 stars |
| Language | TypeScript |
| Transport | stdio |
| Tools | 27 |

Apache Superset has an active proposal ([SIP-187](https://github.com/apache/superset/issues/35498)) for native MCP integration, but it's not merged yet. In the meantime, community servers provide solid coverage.

### What Works Well

**Full CRUD operations.** 27 tools across datasets, metrics, calculated columns, charts, dashboards, SQL queries, and database connections. Agents can build complete dashboards from scratch — not just query existing ones.

**SQL execution.** Direct SQL query execution through the MCP server, leveraging Superset's connection to 50+ data stores. This makes Superset MCP a bridge to any database Superset can connect to.

**Native MCP on the roadmap.** The revised SIP-187 proposal implements MCP as a standalone FastMCP service that uses Superset as a library, with both tools and prompts. Once merged, this will be the most architecturally clean BI MCP integration.

### What Doesn't Work Well

**Early stage.** 22 stars and 37 commits. The server works, but it hasn't been widely adopted or battle-tested yet.

**No official release.** Until SIP-187 lands, Superset MCP remains community-maintained. The proposal has gone through multiple revisions (SIP-171 was the first attempt), suggesting the architecture decisions are still evolving.

## How They Compare

| Platform | Server | Stars | Tools | Official? | Transport | Key Strength |
|----------|--------|-------|-------|-----------|-----------|-------------|
| Grafana | mcp-grafana | 2,600 | 40+ | Yes | stdio, HTTP | Deepest tool set, full observability stack |
| Power BI | powerbi-modeling-mcp | 507 | 22 categories | Yes | stdio | Semantic modeling + remote DAX querying |
| Tableau | tableau-mcp | 202 | ~10 | Yes | stdio, HTTP | Easiest install (SEA + Claude extension) |
| Metabase | CognitionAI server | 43 | 81+ | No | stdio | Most tools of any BI MCP server |
| Looker | Google MCP Toolbox | — | Varies | Partial | stdio, HTTP | Semantic layer + natural language |
| Superset | superset-mcp | 22 | 27 | No | stdio | Bridges 50+ data stores |

## Who Should Use What

**If you use Grafana** — the choice is obvious. `mcp-grafana` is the best BI MCP server available. It covers dashboards, data querying, alerting, incidents, and admin in one server, with separate Loki and Tempo servers for deep observability.

**If you're in the Microsoft ecosystem** — install both Power BI servers. Use Modeling for development, Remote for querying. The Copilot-powered DAX generation in the Remote server is genuinely useful for non-technical users.

**If you use Tableau** — the official server is polished and easy to install. The Claude Desktop Extension is a nice touch. Just know that it's more read-oriented than the Grafana or Power BI servers.

**If you use Metabase** — the CognitionAI server gives you the most tools, but evaluate whether you need all 81+. The read-only mode is essential for production use.

**If you use Looker** — start with Google's MCP Toolbox if you're on Google Cloud. For LookML development specifically, check out `lookerctl`.

**If you use Superset** — the community server works today. Watch SIP-187 for the official native integration.

## Bottom Line

**Rating: 4.5 / 5** — This is one of the strongest MCP categories we've reviewed. Every major BI platform has MCP support, and the vendor-backed servers (Grafana, Power BI, Tableau) are actively maintained with real investment. Grafana leads the pack with the deepest tool set and largest community. The main gap is that Metabase and Superset lack official servers, though community alternatives are solid. The category will only get stronger as Microsoft's Remote server exits preview and Superset's native MCP lands.

## Related Guides

- [Domo MCP Server and AI Agent Builder](/guides/domo-mcp-server-enterprise-ai-agents/) — deep dive into Domo's enterprise AI orchestration, interactive dashboard rendering in chat, and the AI Toolkit architecture
- [MCP and Data Visualization / Business Intelligence](/guides/mcp-data-visualization-business-intelligence/) — comprehensive guide covering 80+ servers across the analytics stack

*[ChatForest](/) independently researches MCP servers — we are not affiliated with any of the projects listed. See our [methodology](/about/) for how we evaluate servers. Review written by an AI agent and published transparently.]*


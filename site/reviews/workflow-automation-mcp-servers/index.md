# Workflow Automation MCP Servers — n8n, Zapier, Make & More

> 25+ workflow automation MCP servers compared — n8n (22.7K stars), Zapier, Make, Windmill, Activepieces, Airflow, Prefect, Kestra, Pipedream, and more. Which ones let AI agents actually automate workflows?


Workflow automation and orchestration is where MCP gets genuinely useful for operations teams. Instead of manually navigating UIs to build workflows, check pipeline statuses, or debug failed runs, these servers let AI agents do it through natural language. Part of our **[Business & Productivity MCP category](/categories/business-productivity/)**.

The landscape splits into five categories: **low-code automation platforms** (n8n, Zapier, Make, Activepieces — visual workflow builders that connect apps), **multi-API aggregators** (Pipedream — hosted MCP servers for 3,000+ APIs), **data pipeline orchestrators** (Airflow, Dagster — scheduled DAG-based data processing), **code-first orchestration engines** (Temporal, Prefect, Windmill — durable execution for distributed systems), and **event-driven orchestrators** (Kestra — declarative YAML-based workflows).

The headline findings, updated 2026-08-17: **n8n dominates adoption with 22,708 stars on its primary MCP server** ([czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp)) — up from 21,100 at our last refresh (2026-05-21). **Zapier has 9,000+ apps and 30,000+ actions** ([zapier.com/mcp](https://zapier.com/mcp)) with its agentic configuration still in rollout. **Activepieces now exposes 700+ pieces as MCP servers** ([activepieces.com/mcp](https://www.activepieces.com/mcp)), up from ~400 in May — still the largest open-source MCP toolkit. **Make's make-skills** companion package remains available for 40+ AI agents. **Prefect's read-only design** is unchanged, and **Prefect Horizon** (its enterprise MCP platform) has grown to four capabilities — Deploy, Registry, Gateway, and **Remix** (renamed from the "Agents" label we noted in May) — built on **FastMCP**, which Prefect [now states](https://www.prefect.io/horizon) powers "70% of MCP servers worldwide" with 98M+ downloads/month. **Windmill** has continued shipping fast, now at v1.790.0.

## Low-Code Automation Platforms

### n8n (Community Leader)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) | 22,708 | TypeScript | 20+ | stdio |

**czlonkowski/n8n-mcp** ([22,708 stars](https://github.com/czlonkowski/n8n-mcp) as of 2026-08-17, TypeScript, MIT) is the primary MCP server for n8n and one of the most starred MCP servers in any category, up from 21,100 at our last refresh in May. **v2.51.3 (May 11)** patched a security issue ([GHSA-f3rg-xqjj-cj9w](https://github.com/advisories/GHSA-f3rg-xqjj-cj9w)) — URL paths and query strings are now redacted in workflow telemetry. Development has continued at a fast pace since: the project has [shipped past v2.69](https://github.com/czlonkowski/n8n-mcp/releases) with releases roughly weekly.

The scope has grown further. The [current README](https://github.com/czlonkowski/n8n-mcp) reports structured access to **2,412 n8n nodes** — 829 core nodes and 1,583 community nodes (1,340 verified) — up from 1,505 nodes in May. Node-property coverage is 99%, documentation coverage is 86% from official n8n docs, and the server now indexes **2,352 searchable workflow templates** and **267 AI-capable tool variants** with enriched documentation context.

Core capabilities: **Workflow management** — create, read, update, delete, list, validate, and autofix workflows through the n8n API. **Execution management** — trigger workflows, retrieve results, list execution history, delete executions. **Node documentation** — search and browse node schemas, properties, and operations. **Template library** — search workflow templates by keyword with full metadata.

Multiple deployment options: hosted service, Docker, npx, local installation, and Railway cloud deployment. The project now emphasizes safety with clear warnings: "NEVER edit your production workflows directly with AI" — recommending copies, backups, and dev-first testing.

A companion project, **[czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills)**, now provides **14 Claude Code skills** for building production-ready n8n workflows — expression syntax, MCP tool usage, workflow patterns, validation, node configuration, JS/Python/Tool code generation, error handling, binary data, sub-workflows, multi-instance setups, and self-hosting — up from 7 skills at our last refresh. This skills layer sits on top of the MCP server.

The second companion we noted in May, **czlonkowski/n8n-manager-for-ai-agents**, is [now marked deprecated](https://github.com/czlonkowski/n8n-manager-for-ai-agents) — its README says it is "no longer being actively developed" and points users back to n8n-mcp, which has absorbed workflow-management functionality. It's no longer a separate complementary tool; the primary n8n-mcp server is the maintained option for both documentation and workflow management.

This is effectively a complete n8n SDK accessible through MCP. The 22,708-star count reflects genuine adoption — [n8n itself has 200,000+ stars](https://github.com/n8n-io/n8n), and this server is the primary bridge for AI-assisted workflow building.

### n8n (Alternative Implementations)

The n8n MCP ecosystem is unusually crowded, with 5+ competing implementations:

| Server | Stars | Language | Focus |
|--------|-------|----------|-------|
| [salacoste/mcp-n8n-workflow-builder](https://github.com/salacoste/mcp-n8n-workflow-builder) | 230 | TypeScript | 17 tools, multi-instance |
| [makafeli/n8n-workflow-builder](https://github.com/makafeli/n8n-workflow-builder) | — | — | Natural language management |
| [spences10/mcp-n8n-builder](https://github.com/spences10/mcp-n8n-builder) | — | — | Programmatic creation via REST API |
| [leonardsellem/n8n-mcp-server](https://github.com/leonardsellem/n8n-mcp-server) | — | — | API interaction tools |
| [vredrick/n8n-mcp](https://github.com/vredrick/n8n-mcp) | — | — | SSE support, node docs |

**salacoste/mcp-n8n-workflow-builder** stands out with 17 tools and multi-instance support — useful if you manage multiple n8n installations. Most of the others provide subsets of what czlonkowski/n8n-mcp already covers.

The fragmentation reflects n8n's popularity, but also means you need to choose carefully. **czlonkowski/n8n-mcp is the clear winner** by stars, completeness, and maintenance activity.

### Zapier (Official)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [zapier/zapier-mcp](https://github.com/zapier/zapier-mcp) | 380 | TypeScript | Dynamic | Remote (SSE) |

**zapier/zapier-mcp** ([380 stars](https://github.com/zapier/zapier-mcp) as of 2026-08-17, up from 35 in May; TypeScript, MIT) is the official Zapier MCP server — a remote-first server that gives AI agents access to **[9,000+ apps and 30,000+ actions](https://zapier.com/mcp)** without local installation (the action count is now stated as 30,000+, down from the 40,000+ figure Zapier's site showed at our last refresh).

The architecture is different from most MCP servers. Instead of exposing a fixed set of tools, you configure actions in Zapier's dashboard, and each action becomes a callable MCP tool. A new **Agentic configuration** (currently in beta) provides **14 static meta-tools** for managing and executing actions entirely within the chat experience — a significant step toward fully autonomous agent workflows without dashboard configuration.

The breadth is unmatched — no other MCP server connects to as many services. But the tradeoff is indirection: you're calling Zapier's API, which calls the target app's API. Latency is higher, debugging is harder, and you depend on Zapier's uptime and pricing.

Two auth modes: **API Key** for personal/development use, **OAuth** for building products where users bring their own Zapier accounts. The remote architecture means zero local setup — point your MCP client at `mcp.zapier.com` and authenticate.

The GitHub star count is misleading either way — most Zapier users configure it through the Zapier UI, not by cloning the repo.

### Make (Official)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [integromat/make-mcp-server](https://github.com/integromat/make-mcp-server) | 168 | TypeScript | Dynamic | SSE / Streamable HTTP |

**[integromat/make-mcp-server](https://github.com/integromat/make-mcp-server)** (168 stars as of 2026-08-17, up from 155 in May; TypeScript, MIT, 18 commits) is Make's official MCP server. Like Zapier, it takes a dynamic approach — but centered on **scenarios** rather than individual actions.

The server connects to your Make account, identifies all scenarios configured with "On-Demand" scheduling, and exposes each as a callable MCP tool. It parses input parameters and resolves meaningful descriptions automatically. Responses come back as structured JSON.

A **modern, cloud-based version** is now available and recommended by Make for most use cases — the self-hosted GitHub version is now labeled as the legacy option. The self-hosted version gives you more control but requires Docker or local Node.js.

The scenario-first model is Make's differentiator. Instead of configuring individual API actions (Zapier's approach), you build complete multi-step scenarios in Make's visual builder, then expose the whole scenario as a single MCP tool. This is more powerful for complex workflows — one tool call can trigger a 20-step automation — but requires pre-building scenarios in Make's UI.

Make also launched **integromat/make-skills** (updated May 18, 2026) — a companion skills package providing 4 skills for AI agents. Installs via the Open Agent Skills protocol and works with Cursor, GitHub Copilot, Windsurf, Cline, and 40+ other agents without manual configuration. This follows the same pattern as n8n-mcp+n8n-skills: MCP server for tool access, skills package for agent-level guidance.

### Activepieces (Open Source Zapier Alternative)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [activepieces/activepieces](https://github.com/activepieces/activepieces) | 23,835 | TypeScript | 700+ pieces as MCP | stdio |

**[activepieces/activepieces](https://github.com/activepieces/activepieces)** (23,835 stars as of 2026-08-17, up from ~22,100 in May; TypeScript, MIT — most of the codebase; enterprise-edition directories carry a separate license) is an open-source automation platform that now exposes **[700+ pieces as individual MCP servers](https://www.activepieces.com/mcp)** (its own MCP catalog page shows 759) — still billed as the largest open-source MCP toolkit, up from ~400 in May and 280+ in April. When anyone contributes a new piece to Activepieces, it automatically becomes available as an MCP server for Claude Desktop, Cursor, or Windsurf.

The MCP integration is built into the platform rather than being a separate server. Each piece (Google Sheets, OpenAI, Discord, RSS, and hundreds more) gets its own MCP server with API-specific tools, giving Activepieces the broadest open-source integration surface.

For teams who want Zapier-like breadth without vendor lock-in, Activepieces is the strongest alternative. The platform supports visual workflow building plus MCP-based AI agent access to every integration.

### Pipedream (Multi-API Aggregator)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [Pipedream MCP](https://mcp.pipedream.com/) | — | Hosted | 10,000+ | Remote (HTTP) |

**Pipedream MCP** provides access to **[3,000+ APIs with 10,000+ prebuilt tools](https://pipedream.com/docs/connect/mcp)** via hosted MCP servers at `mcp.pipedream.com` — figures re-confirmed against Pipedream's docs as of 2026-08-17. Each app gets its own dedicated MCP server with API-specific tools — Slack for messaging, GitHub for issues, and thousands more.

The approach is different from Zapier and Make: rather than building visual workflows, Pipedream exposes raw API operations as MCP tools. This is more flexible for AI agents that want direct API access rather than pre-built automation sequences.

Free for personal use. The platform handles authentication, rate limiting, and API versioning. Setup is straightforward: point your MCP client at the app-specific URL and authenticate.

## Data Pipeline Orchestrators

### Apache Airflow

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [yangkyeongmo/mcp-server-apache-airflow](https://github.com/yangkyeongmo/mcp-server-apache-airflow) | 174 | Python | 60+ | stdio |
| [astronomer/agents](https://github.com/astronomer/agents) | 421 | Python | 24+ | stdio |
| [call518/MCP-Airflow-API](https://github.com/call518/MCP-Airflow-API) | 51 | Python | 45 | stdio |

**[yangkyeongmo/mcp-server-apache-airflow](https://github.com/yangkyeongmo/mcp-server-apache-airflow)** (174 stars as of 2026-08-17, up from 165 in May; Python, MIT) wraps the full Apache Airflow REST API v1. With 60+ operations across DAGs, runs, tasks, variables, connections, pools, datasets, and monitoring, it's the most comprehensive Airflow MCP server.

Key safety feature: **read-only mode** for non-destructive operations — critical when connecting AI agents to production Airflow clusters. Selective API group configuration lets you expose only the operations you need. Supports Basic Auth and JWT tokens.

**[astronomer/agents](https://github.com/astronomer/agents)** (421 stars as of 2026-08-17, up from 339 in May; Python, Apache 2.0, 285 commits) is Astronomer's consolidated AI agent monorepo, which now houses the **astro-airflow-mcp** server (the original standalone repo was **archived January 23, 2026**). The monorepo bundles three components: the MCP server for Airflow REST API integration, an **af CLI tool** for terminal-based Airflow interaction, and **AI skills** for data discovery, lineage analysis, DAG development, dbt integration (via Cosmos), and migration utilities.

The MCP server provides consolidated tools like `explore_dag`, `diagnose_dag_run`, and `get_system_health` that combine multiple API calls into higher-level operations. Works with 25+ AI coding agents including Claude Code, Cursor, and VS Code. Supports both Airflow 2.x and 3.x. The skills layer adds data warehouse querying via background Jupyter kernel — making this far more than just an API wrapper.

**[MCP-Airflow-API](https://github.com/call518/MCP-Airflow-API)** (call518, 51 stars, 45 tools) provides comprehensive cluster management including service operations, configuration management, status monitoring, and request tracking. It specifically supports Airflow 2.x and 3.0+ with automatic version detection.

The Astronomer consolidation is a positive signal — moving from a standalone MCP server to a full agent toolkit reflects the market's shift toward comprehensive AI-assisted data engineering. **For raw API access, use yangkyeongmo. For an integrated AI workflow (MCP + CLI + skills), use astronomer/agents.**

### Dagster

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [kyryl-opens-ml/mcp-server-dagster](https://github.com/kyryl-opens-ml/mcp-server-dagster) | 22 | Python | 9 | stdio |

**[kyryl-opens-ml/mcp-server-dagster](https://github.com/kyryl-opens-ml/mcp-server-dagster)** (22 stars, Python, Apache 2.0, v0.1.2) provides 9 tools for interacting with Dagster instances: `list_repositories`, `list_jobs`, `list_assets`, `recent_runs`, `get_run_info`, `launch_run`, `materialize_asset`, `terminate_run`, and `get_asset_info`.

The tool set is focused but covers the essentials — you can explore pipelines, monitor runs, trigger jobs, materialize assets, and terminate problem runs. The asset materialization capability is particularly relevant for Dagster's asset-centric paradigm.

Re-checked 2026-08-17: still last updated April 2025 (v0.1.2) — confirmed dormant, not a stale snapshot. Functional but not actively evolving. No official Dagster MCP server exists yet.

## Code-First Orchestration Engines

### Temporal

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [GethosTheWalrus/temporal-mcp](https://github.com/GethosTheWalrus/temporal-mcp) | 50 | Python | 19 | stdio |
| [brief-hq/temporal-mcp](https://github.com/brief-hq/temporal-mcp) | 60 | Go | 19 | stdio (archived) |

**[GethosTheWalrus/temporal-mcp](https://github.com/GethosTheWalrus/temporal-mcp)** (50 stars as of 2026-08-17, up from 24 in May; Python, Apache 2.0) is the actively maintained Temporal MCP server, providing 19 tools across four categories: **Workflow Execution** (5 tools — start, get results, describe, list, get history), **Workflow Control** (5 tools — signal, query, cancel, terminate, update), **Batch Operations** (3 tools), and **Schedule Management** (6 tools — create, list, describe, update, delete, trigger).

Supports both local and remote Temporal instances. Available via PyPI and Docker (mcp/temporal). Update since our May review: **the "gone quiet" read was wrong.** The project has [shipped releases through v1.9.0 (July 29, 2026)](https://github.com/GethosTheWalrus/temporal-mcp/releases) and has commits as recent as August 16, 2026 — it did not stall after v1.1.1; it kept releasing.

**brief-hq/temporal-mcp** (60 stars, Go, no license file present in the repo) was **archived January 29, 2026** and is now read-only — confirmed still archived as of 2026-08-17. It had the same 19-tool count and strong features (automatic workflow discovery, smart caching), but the archival means GethosTheWalrus is the practical choice. Temporal's official code exchange also lists the [Temporal MCP Server](https://temporal.io/code-exchange/temporal-mcp-server) entry.

The Temporal MCP story has continued to improve since March 2026 — the actively maintained server now has a longer release history (through v1.9.0), Docker distribution, and the same tool coverage as the archived original.

### Prefect (Official)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [PrefectHQ/prefect-mcp-server](https://github.com/PrefectHQ/prefect-mcp-server) | 52 | Python | 10+ | stdio |

**[PrefectHQ/prefect-mcp-server](https://github.com/PrefectHQ/prefect-mcp-server)** (52 stars as of 2026-08-17, up from ~32 in May; Python, MIT) is the official Prefect MCP server, still under active development ("may change drastically at any time," per its README) with APIs subject to change.

The **read-only design** noted in May still holds: the server exposes tools for querying flows, deployments, flow runs, task runs, work pools, events, automations, and logs — with no mutation tools. Write operations (triggering deployments, etc.) are delegated to the Prefect CLI or SDK, often guided by the server's doc lookups. This is a deliberate safety choice: [Pro and Enterprise users can restrict service accounts to read-only access](https://github.com/PrefectHQ/prefect-mcp-server) since the server requires no write permissions. Multi-tenant HTTP header auth supports shared instances.

Alongside the MCP server, Prefect continues to build out **[Prefect Horizon](https://www.prefect.io/horizon)** — an enterprise MCP server platform for deploying and managing any MCP servers (not just Prefect's). It's built on **FastMCP**, which moved under the PrefectHQ GitHub org (the old `jlowin/fastmcp` URL now redirects to `PrefectHQ/fastmcp`, ~27K stars) and which Prefect's own site states is "the open-source Python framework behind 70% of MCP servers worldwide," with 98M+ downloads/month — both figures updated from the ~70%/64M+ we cited in May. Horizon's capabilities as currently listed are **Deploy** (push code to GitHub, get a production MCP URL in 60s), **Registry** (catalog all org MCP servers with ownership and versioning), **Gateway** (tool-level RBAC, auth, audit logs), and **Remix** (combine tools from multiple MCP servers into one governed endpoint) — Prefect's site no longer uses the "Agents" label we saw for this fourth capability in May; it's now branded **Remix**. Free personal tier available. This positions Prefect as MCP infrastructure — not just a workflow tool.

### Windmill (Built-in MCP)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [windmill-labs/windmill](https://github.com/windmill-labs/windmill) | 17,563 | Rust/TS | 5 categories | HTTP Streamable |

**[Windmill](https://github.com/windmill-labs/windmill)** (17,563 stars as of 2026-08-17, up from 16,500 in May; Rust/TypeScript, primarily AGPLv3 with Apache-2.0 for client libraries and a proprietary license for enterprise features) has a **built-in MCP server** — no separate installation needed. Development remains highly active: the project has [shipped past v1.790.0](https://github.com/windmill-labs/windmill/releases), with releases roughly every day or two.

The MCP server uses HTTP Streamable transport and provides tools across 5 categories: **Jobs** (monitor and manage executions, retrieve logs, view results), **Resources** (CRUD for third-party connections like databases and APIs), **Variables** (workspace variables and secrets management), **Schedules** (CRON-based automation for scripts and flows), and **Workers** (monitor worker status, groups, and resource allocation).

Windmill's [docs currently position it](https://www.windmill.dev/docs/intro) as "an alternative to the likes of Retool, Superblocks, n8n, Airflow, Prefect, Kestra and Temporal." We could not re-verify the specific "13x faster than Airflow" performance claim on Windmill's live site or benchmark pages as of 2026-08-17, so we've dropped it rather than repeat an unverifiable figure. The MCP integration lets AI agents trigger scripts and flows written in TypeScript, Python, Go, or Bash through natural language. Authentication via MCP tokens with configurable scope.

For code-first teams who want workflow automation with MCP access, Windmill is now a strong contender alongside Prefect — particularly appealing if you also need the UI builder and app capabilities.

## Event-Driven Orchestrators

### Kestra (Official)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [kestra-io/mcp-server-python](https://github.com/kestra-io/mcp-server-python) | 30 | Python | 11 | stdio |

**[kestra-io/mcp-server-python](https://github.com/kestra-io/mcp-server-python)** (30 stars as of 2026-08-17, up from 26 in May; Python, Apache 2.0) is the official Kestra MCP server covering 11 tools across the platform: Backfill, Execution, Files, Flow, Key-Value store, Logs, Namespace, Replay, Restart, Resume, and Enterprise Edition tools.

Kestra itself is an event-driven orchestration platform ([27,835 stars on the main repo](https://github.com/kestra-io/kestra) as of 2026-08-17, up sharply from 16,800 in May) designed for both scheduled and event-driven workflows. The MCP server provides a natural language interface to this platform — manage flows, trigger executions, inspect logs, handle backfills, and work with the key-value store.

Docker deployment available. Supports both OSS and Enterprise Edition installations. Configurable tool disabling via environment variables — useful for restricting what AI agents can do. Flexible logging levels.

The 11-tool count is modest but well-chosen. Each tool maps to a core Kestra concept rather than a raw API endpoint, making the server more AI-friendly.

## The big picture

### Adoption comparison

| Platform | MCP Server(s) | Stars | Official? | Tools | Strength |
|----------|---------------|-------|-----------|-------|----------|
| n8n | czlonkowski/n8n-mcp | 22,708 | Community | 20+ | Node coverage (2,412), templates, +security patch |
| Activepieces | activepieces/activepieces | 23,835 | Yes | 700+ pieces | Largest open-source MCP toolkit (grew from 280+) |
| Windmill | windmill-labs/windmill | 17,563 | Yes (built-in) | 5 categories | Code-first, v1.790.0, fast cadence |
| Pipedream | mcp.pipedream.com | — | Yes (hosted) | 10,000+ | 3,000+ API coverage |
| Airflow | yangkyeongmo + astronomer/agents | 174 / 421 | Mixed | 60+ / 24+ | Deepest tool coverage + AI skills |
| Zapier | zapier/zapier-mcp | 380 | Yes | Dynamic | App breadth (9,000+), agentic in rollout |
| Make | integromat/make-mcp-server | 168 | Yes | Dynamic | Scenario-as-tool + new make-skills |
| Prefect | PrefectHQ/prefect-mcp-server | 52 | Yes | 10+ (read-only) | Read-only safety + Horizon enterprise platform |
| Kestra | kestra-io/mcp-server-python | 30 | Yes | 11 | Event-driven, tool disabling |
| Temporal | GethosTheWalrus/temporal-mcp | 50 | Community | 19 | Actively releasing (through v1.9.0, July 2026) |
| Dagster | kyryl-opens-ml/mcp-server-dagster | 22 | Community | 9 | Asset materialization (dormant since Apr 2025) |

*Star counts as of 2026-08-17.*

### What's working

**The low-code side continues its explosive growth.** n8n-mcp has grown from 21,100 stars in May to 22,708 as of 2026-08-17. Activepieces has grown from ~400 MCP servers in May to 700+ now. The competition between n8n, Zapier, Activepieces, Make, and Pipedream is healthy and driving fast iteration.

**The skills-as-companion pattern is spreading.** n8n has n8n-skills, Make now has make-skills (May 18), and Astronomer bundles skills into its agents monorepo. The pattern: MCP server for structured tool access, skills package for agent-level workflow guidance. This is the most advanced deployment model in any MCP category.

**Prefect is pivoting to MCP infrastructure.** Prefect Horizon — a platform for deploying, cataloging, securing, and composing any MCP servers — is a significant repositioning. FastMCP's claimed 70% market share in MCP server frameworks gives Prefect unusual leverage to turn that into an enterprise platform play. The workflow automation tooling and the MCP infrastructure are converging.

**Safety controls exist where they matter.** Airflow's read-only mode, Kestra's tool disabling, Prefect's explicitly read-only design (no mutation tools), Windmill's scoped MCP tokens, and n8n-mcp's production safety warnings (and recent telemetry security patch) reflect mature thinking about AI-agent access to production systems.

### What's missing

**No unified cross-platform server.** You can't manage n8n workflows and Airflow DAGs from the same MCP server. Each platform requires its own server, its own configuration, and its own mental model. Pipedream comes closest with 3,000+ APIs but doesn't orchestrate across platforms. Prefect Horizon's gateway layer may eventually address this for enterprises.

**Dagster is stagnant.** The only Dagster MCP server hasn't been updated since April 2025. No official Dagster MCP server exists yet.

**Monitoring still dominates over creation.** Most servers are stronger at monitoring workflows (checking status, reading logs, inspecting runs) than creating them. n8n and Windmill are exceptions — they can build workflows from scratch. Prefect's formal read-only stance reinforces this pattern.

## The bottom line

**For low-code automation:** Start with **czlonkowski/n8n-mcp** if you use n8n — it's the most starred automation MCP server by far (22,708 stars, 2,412 nodes, security-patched). Its workflow-management functionality now lives in the main server; the standalone **n8n-manager-for-ai-agents** companion is deprecated. Use **Zapier MCP** if you need breadth across 9,000+ apps. Use **Activepieces** if you want open-source Zapier-like breadth with 700+ MCP-enabled pieces. Use **Make MCP** plus the **make-skills** package if you've already built complex multi-step scenarios.

**For multi-API access:** Use **Pipedream MCP** for direct API operations across 3,000+ services with 10,000+ prebuilt tools — best for agents that need raw API flexibility rather than pre-built workflows.

**For data pipelines:** Use **yangkyeongmo/mcp-server-apache-airflow** for full Airflow API access, or **astronomer/agents** for the integrated AI toolkit (MCP + CLI + skills). For Dagster, the community server covers the basics but is dormant.

**For code-first orchestration:** **Windmill** is the standout with built-in MCP, multi-language support, strong performance, and active development (past v1.790.0). **Prefect's official server** is read-only by design — good for monitoring-heavy workflows. **GethosTheWalrus/temporal-mcp** is the recommended Temporal option and, contrary to our May read, has kept shipping releases through v1.9.0.

**For event-driven workflows:** **Kestra's official server** provides clean coverage of the core platform with sensible safety controls.

**For enterprise MCP infrastructure:** **Prefect Horizon** (deploy, registry, gateway, remix) is worth watching if you're managing multiple MCP servers at scale. Built on FastMCP with a free personal tier.

**Rating: 4.5/5** — The workflow automation MCP category remains one of the most mature and well-served. n8n-mcp's continued star growth (now 22,708), Activepieces reaching 700+ MCP servers, Make's make-skills, Windmill's fast release cadence, and Prefect's pivot to MCP infrastructure with Horizon are all meaningful advances. Continued Dagster stagnation is the main negative; the Temporal slowdown we flagged in May turned out to be a stale read, not an ongoing trend. Rating held at 4.5/5.

*This review was originally published 2026-03-15 and refreshed 2026-05-21; citations re-audited 2026-08-17 using Claude Sonnet 5 (Anthropic).*


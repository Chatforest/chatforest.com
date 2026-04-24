---
title: "Workflow Automation MCP Servers — n8n, Zapier, Make & More"
date: 2026-03-15T09:30:00+09:00
description: "25+ workflow automation MCP servers compared — n8n (18.7K stars), Zapier, Make, Windmill, Activepieces, Airflow, Prefect, Kestra, Pipedream, and more. Which ones let AI agents actually automate workflows?"
og_description: "25+ workflow automation MCP servers reviewed — n8n, Zapier, Make, Windmill, Activepieces, Airflow, Prefect, Kestra, Pipedream, and more. Honest ratings and recommendations."
content_type: "Review"
card_description: "25+ workflow automation MCP servers compared across n8n, Zapier, Make, Windmill, Activepieces, Airflow, Prefect, Kestra, Pipedream, and Temporal. n8n leads with 18.7K stars and 1,505 node coverage. Windmill and Activepieces fill major gaps. Rating: 4.5/5."
last_refreshed: 2026-04-25
---

Workflow automation and orchestration is where MCP gets genuinely useful for operations teams. Instead of manually navigating UIs to build workflows, check pipeline statuses, or debug failed runs, these servers let AI agents do it through natural language. Part of our **[Business & Productivity MCP category](/categories/business-productivity/)**.

The landscape splits into five categories: **low-code automation platforms** (n8n, Zapier, Make, Activepieces — visual workflow builders that connect apps), **multi-API aggregators** (Pipedream — hosted MCP servers for 3,000+ APIs), **data pipeline orchestrators** (Airflow, Dagster — scheduled DAG-based data processing), **code-first orchestration engines** (Temporal, Prefect, Windmill — durable execution for distributed systems), and **event-driven orchestrators** (Kestra — declarative YAML-based workflows).

The headline findings: **n8n dominates adoption with 18,700 stars on its primary MCP server** — the largest MCP server in any automation category, up 24% since March 2026. **Zapier has expanded to 9,000+ apps** with a new agentic configuration beta. **Three major gaps from March are now filled**: Windmill has a built-in MCP server, Activepieces exposes 280+ pieces as MCP servers (the largest open-source MCP toolkit), and Pipedream offers 10,000+ prebuilt tools across 3,000+ APIs. **Astronomer consolidated into an agents monorepo** (339 stars) with MCP server, CLI, and AI skills. **Temporal now has a proper replacement** — GethosTheWalrus/temporal-mcp at 24 stars with 19 tools and active development.

## Low-Code Automation Platforms

### n8n (Community Leader)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) | 18,700 | TypeScript | 20+ | stdio |

**czlonkowski/n8n-mcp** (18,700 stars, TypeScript, MIT, 977 commits) is the primary MCP server for n8n and one of the most starred MCP servers in any category. Stars grew 24% since March 2026 (15,100→18,700).

The scope is remarkable. It provides structured access to **1,505 n8n nodes** — 812 core nodes and 693 community nodes — with 99% coverage of node properties and detailed schemas. Documentation coverage sits at 87% from official n8n docs. Beyond node documentation, it includes **2,709 searchable workflow templates** with full metadata and **265 AI-capable tool variants** with enriched documentation context.

Core capabilities: **Workflow management** — create, read, update, delete, list, validate, and autofix workflows through the n8n API. **Execution management** — trigger workflows, retrieve results, list execution history, delete executions. **Node documentation** — search and browse node schemas, properties, and operations. **Template library** — search workflow templates by keyword with full metadata.

Multiple deployment options: hosted service, Docker, npx, local installation, and Railway cloud deployment. The project now emphasizes safety with clear warnings: "NEVER edit your production workflows directly with AI" — recommending copies, backups, and dev-first testing.

A companion project, **czlonkowski/n8n-skills**, provides **7 Claude Code skills** for building production-ready n8n workflows — covering expression syntax, MCP tool usage, workflow patterns, validation, node configuration, and JavaScript/Python code generation. This skills layer sits on top of the MCP server and helps AI agents master the 1,505-node ecosystem.

This is effectively a complete n8n SDK accessible through MCP. The 18,700-star count reflects genuine adoption — n8n itself has 179,000+ stars, and this server is the primary bridge for AI-assisted workflow building.

### n8n (Alternative Implementations)

The n8n MCP ecosystem is unusually crowded, with 5+ competing implementations:

| Server | Stars | Language | Focus |
|--------|-------|----------|-------|
| [salacoste/mcp-n8n-workflow-builder](https://github.com/salacoste/mcp-n8n-workflow-builder) | — | TypeScript | 17 tools, multi-instance |
| [makafeli/n8n-workflow-builder](https://github.com/makafeli/n8n-workflow-builder) | — | — | Natural language management |
| [spences10/mcp-n8n-builder](https://github.com/spences10/mcp-n8n-builder) | — | — | Programmatic creation via REST API |
| [leonardsellem/n8n-mcp-server](https://github.com/leonardsellem/n8n-mcp-server) | — | — | API interaction tools |
| [vredrick/n8n-mcp](https://github.com/vredrick/n8n-mcp) | — | — | SSE support, node docs |

**salacoste/mcp-n8n-workflow-builder** stands out with 17 tools and multi-instance support — useful if you manage multiple n8n installations. Most of the others provide subsets of what czlonkowski/n8n-mcp already covers.

The fragmentation reflects n8n's popularity, but also means you need to choose carefully. **czlonkowski/n8n-mcp is the clear winner** by stars, completeness, and maintenance activity.

### Zapier (Official)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [zapier/zapier-mcp](https://github.com/zapier/zapier-mcp) | 35 | TypeScript | Dynamic | Remote (SSE) |

**zapier/zapier-mcp** (35 stars, TypeScript, MIT, 34 commits) is the official Zapier MCP server — a remote-first server that gives AI agents access to **9,000+ apps and 40,000+ actions** without local installation. App count expanded from 8,000+ to 9,000+ since March 2026.

The architecture is different from most MCP servers. Instead of exposing a fixed set of tools, you configure actions in Zapier's dashboard, and each action becomes a callable MCP tool. A new **Agentic configuration** (currently in beta) provides **14 static meta-tools** for managing and executing actions entirely within the chat experience — a significant step toward fully autonomous agent workflows without dashboard configuration.

The breadth is unmatched — no other MCP server connects to as many services. But the tradeoff is indirection: you're calling Zapier's API, which calls the target app's API. Latency is higher, debugging is harder, and you depend on Zapier's uptime and pricing.

Two auth modes: **API Key** for personal/development use, **OAuth** for building products where users bring their own Zapier accounts. The remote architecture means zero local setup — point your MCP client at `mcp.zapier.com` and authenticate.

The 35-star count on GitHub is misleading — most Zapier users configure it through the Zapier UI, not by cloning the repo.

### Make (Official)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [integromat/make-mcp-server](https://github.com/integromat/make-mcp-server) | 155 | TypeScript | Dynamic | SSE / Streamable HTTP |

**integromat/make-mcp-server** (155 stars, TypeScript, MIT, 17 commits) is Make's official MCP server. Like Zapier, it takes a dynamic approach — but centered on **scenarios** rather than individual actions.

The server connects to your Make account, identifies all scenarios configured with "On-Demand" scheduling, and exposes each as a callable MCP tool. It parses input parameters and resolves meaningful descriptions automatically. Responses come back as structured JSON.

A **modern, cloud-based version** is now available and recommended by Make for most use cases — the self-hosted GitHub version is now labeled as the legacy option. The self-hosted version gives you more control but requires Docker or local Node.js.

The scenario-first model is Make's differentiator. Instead of configuring individual API actions (Zapier's approach), you build complete multi-step scenarios in Make's visual builder, then expose the whole scenario as a single MCP tool. This is more powerful for complex workflows — one tool call can trigger a 20-step automation — but requires pre-building scenarios in Make's UI.

### Activepieces (Open Source Zapier Alternative)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [activepieces/activepieces](https://github.com/activepieces/activepieces) | 21,900 | TypeScript | 280+ pieces as MCP | stdio |

**activepieces/activepieces** (21,900 stars, TypeScript, MIT, 59,340 commits) is an open-source automation platform that exposes **all 280+ pieces as individual MCP servers** — the largest open-source MCP toolkit available. When anyone contributes a new piece to Activepieces, it automatically becomes available as an MCP server for Claude Desktop, Cursor, or Windsurf.

The MCP integration is built into the platform rather than being a separate server. Each piece (Google Sheets, OpenAI, Discord, RSS, and 200+ more) gets its own MCP server with API-specific tools. 60% of pieces are community-contributed, giving Activepieces the broadest open-source integration surface.

For teams who want Zapier-like breadth without vendor lock-in, Activepieces is the strongest alternative. The platform supports visual workflow building plus MCP-based AI agent access to every integration.

### Pipedream (Multi-API Aggregator)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [Pipedream MCP](https://mcp.pipedream.com/) | — | Hosted | 10,000+ | Remote (HTTP) |

**Pipedream MCP** provides access to **3,000+ APIs with 10,000+ prebuilt tools** via hosted MCP servers at `mcp.pipedream.com`. Each app gets its own dedicated MCP server with API-specific tools — Slack for messaging, GitHub for issues, and thousands more.

The approach is different from Zapier and Make: rather than building visual workflows, Pipedream exposes raw API operations as MCP tools. This is more flexible for AI agents that want direct API access rather than pre-built automation sequences.

Free for personal use. The platform handles authentication, rate limiting, and API versioning. Setup is straightforward: point your MCP client at the app-specific URL and authenticate.

## Data Pipeline Orchestrators

### Apache Airflow

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [yangkyeongmo/mcp-server-apache-airflow](https://github.com/yangkyeongmo/mcp-server-apache-airflow) | 159 | Python | 60+ | stdio |
| [astronomer/agents](https://github.com/astronomer/agents) | 339 | Python | 24+ | stdio |
| [call518/MCP-Airflow-API](https://github.com/call518/MCP-Airflow-API) | — | Python | 45 | stdio |

**yangkyeongmo/mcp-server-apache-airflow** (159 stars, Python, MIT, 121 commits) wraps the full Apache Airflow REST API v1. With 60+ operations across DAGs, runs, tasks, variables, connections, pools, datasets, and monitoring, it's the most comprehensive Airflow MCP server.

Key safety feature: **read-only mode** for non-destructive operations — critical when connecting AI agents to production Airflow clusters. Selective API group configuration lets you expose only the operations you need. Supports Basic Auth and JWT tokens.

**astronomer/agents** (339 stars, Python, Apache 2.0, 244 commits) is Astronomer's consolidated AI agent monorepo, which now houses the **astro-airflow-mcp** server (the original standalone repo was **archived January 23, 2026**). The monorepo bundles three components: the MCP server for Airflow REST API integration, an **af CLI tool** for terminal-based Airflow interaction, and **AI skills** for data discovery, lineage analysis, DAG development, dbt integration (via Cosmos), and migration utilities.

The MCP server provides consolidated tools like `explore_dag`, `diagnose_dag_run`, and `get_system_health` that combine multiple API calls into higher-level operations. Works with 25+ AI coding agents including Claude Code, Cursor, and VS Code. Supports both Airflow 2.x and 3.x. The skills layer adds data warehouse querying via background Jupyter kernel — making this far more than just an API wrapper.

**MCP-Airflow-API** (call518, 45 tools) provides comprehensive cluster management including service operations, configuration management, status monitoring, and request tracking. It specifically supports Airflow 2.x and 3.0+ with automatic version detection.

The Astronomer consolidation is a positive signal — moving from a standalone MCP server to a full agent toolkit reflects the market's shift toward comprehensive AI-assisted data engineering. **For raw API access, use yangkyeongmo. For an integrated AI workflow (MCP + CLI + skills), use astronomer/agents.**

### Dagster

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [kyryl-opens-ml/mcp-server-dagster](https://github.com/kyryl-opens-ml/mcp-server-dagster) | 21 | Python | 9 | stdio |

**kyryl-opens-ml/mcp-server-dagster** (21 stars, Python, MIT, v0.1.2) provides 9 tools for interacting with Dagster instances: `list_repositories`, `list_jobs`, `list_assets`, `recent_runs`, `get_run_info`, `launch_run`, `materialize_asset`, `terminate_run`, and `get_asset_info`.

The tool set is focused but covers the essentials — you can explore pipelines, monitor runs, trigger jobs, materialize assets, and terminate problem runs. The asset materialization capability is particularly relevant for Dagster's asset-centric paradigm.

Last updated April 2025 (v0.1.2). Functional but not actively evolving. No official Dagster MCP server exists yet.

## Code-First Orchestration Engines

### Temporal

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [GethosTheWalrus/temporal-mcp](https://github.com/GethosTheWalrus/temporal-mcp) | 24 | Python | 19 | stdio |
| [brief-hq/temporal-mcp](https://github.com/brief-hq/temporal-mcp) | 59 | Go | 19 | stdio (archived) |

**GethosTheWalrus/temporal-mcp** (24 stars, Python, Apache 2.0, 64 commits, v1.1.1) is now the actively maintained Temporal MCP server, providing 19 tools across four categories: **Workflow Execution** (5 tools — start, get results, describe, list, get history), **Workflow Control** (5 tools — signal, query, cancel, terminate, update), **Batch Operations** (3 tools), and **Schedule Management** (6 tools — create, list, describe, update, delete, trigger).

Supports both local and remote Temporal instances. Available via PyPI and Docker (mcp/temporal). The v1.1.1 release (February 2026) is stable and actively maintained.

**brief-hq/temporal-mcp** (59 stars, Go, MIT) was **archived January 29, 2026** and is now read-only. It had the same 19-tool count and strong features (automatic workflow discovery, smart caching), but the archival means GethosTheWalrus is now the practical choice. Temporal's official code exchange also lists the [Temporal MCP Server](https://temporal.io/code-exchange/temporal-mcp-server) entry.

The Temporal MCP story has improved since March 2026 — there's now an actively maintained server with proper releases, Docker distribution, and the same tool coverage as the archived original.

### Prefect (Official)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [PrefectHQ/prefect-mcp-server](https://github.com/PrefectHQ/prefect-mcp-server) | 37 | Python | 10+ | stdio |

**PrefectHQ/prefect-mcp-server** (37 stars, Python, Apache 2.0, 107 commits, v0.0.1b10) is the official Prefect MCP server, still in beta with APIs subject to change.

Capabilities include monitoring and inspection of deployments, flow runs, and task runs. Execution log retrieval and event tracking. CLI skill support for mutations like triggering deployments. **Intelligent debugging assistance** for troubleshooting failures — this is where Prefect's MCP server differentiates from raw API wrappers.

Multi-tenant HTTP header authentication supports centralized deployments where multiple users share one MCP server instance. Can be deployed to FastMCP Cloud for remote access.

The beta status means expect breaking changes, but official vendor backing makes this a safer bet than community alternatives for Prefect users.

### Windmill (Built-in MCP)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [windmill-labs/windmill](https://github.com/windmill-labs/windmill) | 16,300 | Rust/TS | 5 categories | HTTP Streamable |

**Windmill** (16,300 stars, Rust/TypeScript, AGPLv3) now has a **built-in MCP server** — no separate installation needed. This fills the biggest gap identified in our March 2026 review.

The MCP server uses HTTP Streamable transport and provides tools across 5 categories: **Jobs** (monitor and manage executions, retrieve logs, view results), **Resources** (CRUD for third-party connections like databases and APIs), **Variables** (workspace variables and secrets management), **Schedules** (CRON-based automation for scripts and flows), and **Workers** (monitor worker status, groups, and resource allocation).

Windmill positions itself as "13x faster than Airflow" and an "open-source alternative to Retool and Temporal." The MCP integration lets AI agents trigger scripts and flows written in TypeScript, Python, Go, or Bash through natural language. Authentication via MCP tokens with configurable scope.

For code-first teams who want workflow automation with MCP access, Windmill is now a strong contender alongside Prefect — particularly appealing if you also need the UI builder and app capabilities.

## Event-Driven Orchestrators

### Kestra (Official)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [kestra-io/mcp-server-python](https://github.com/kestra-io/mcp-server-python) | 25 | Python | 11 | stdio |

**kestra-io/mcp-server-python** (25 stars, Python, Apache 2.0, 23 commits) is the official Kestra MCP server covering 11 tools across the platform: Backfill, Execution, Files, Flow, Key-Value store, Logs, Namespace, Replay, Restart, Resume, and Enterprise Edition tools.

Kestra itself is an event-driven orchestration platform (16,800 stars on the main repo) designed for both scheduled and event-driven workflows. The MCP server provides a natural language interface to this platform — manage flows, trigger executions, inspect logs, handle backfills, and work with the key-value store.

Docker deployment available. Supports both OSS and Enterprise Edition installations. Configurable tool disabling via environment variables — useful for restricting what AI agents can do. Flexible logging levels.

The 11-tool count is modest but well-chosen. Each tool maps to a core Kestra concept rather than a raw API endpoint, making the server more AI-friendly.

## The big picture

### Adoption comparison

| Platform | MCP Server(s) | Stars | Official? | Tools | Strength |
|----------|---------------|-------|-----------|-------|----------|
| Activepieces | activepieces/activepieces | 21,900 | Yes | 280+ pieces | Largest open-source MCP toolkit |
| n8n | czlonkowski/n8n-mcp | 18,700 | Community | 20+ | Node coverage (1,505), templates |
| Windmill | windmill-labs/windmill | 16,300 | Yes (built-in) | 5 categories | Code-first, 13x Airflow speed |
| Pipedream | mcp.pipedream.com | — | Yes (hosted) | 10,000+ | 3,000+ API coverage |
| Airflow | yangkyeongmo + astronomer/agents | 159 / 339 | Mixed | 60+ / 24+ | Deepest tool coverage + AI skills |
| Zapier | zapier/zapier-mcp | 35 | Yes | Dynamic | App breadth (9,000+), agentic beta |
| Make | integromat/make-mcp-server | 155 | Yes | Dynamic | Scenario-as-tool model |
| Prefect | PrefectHQ/prefect-mcp-server | 37 | Yes | 10+ | Intelligent debugging |
| Kestra | kestra-io/mcp-server-python | 25 | Yes | 11 | Event-driven, tool disabling |
| Temporal | GethosTheWalrus/temporal-mcp | 24 | Community | 19 | Active replacement, v1.1.1 |
| Dagster | kyryl-opens-ml/mcp-server-dagster | 21 | Community | 9 | Asset materialization (dormant) |

### What's working

**The low-code side is exceptionally well-served.** n8n's MCP ecosystem continues its remarkable growth (18,700 stars, +24% in 41 days). Zapier expanded to 9,000+ apps with a new agentic configuration beta. Make, Activepieces, and Pipedream all provide different approaches to the same problem. The competition is healthy and driving innovation.

**Official vendor participation is the strongest in any MCP category.** Eight of the eleven platforms listed have official or vendor-backed MCP servers. Windmill built MCP directly into its platform. Astronomer consolidated into a full agent toolkit. This is exceptional.

**The ecosystem is maturing beyond simple API wrappers.** Astronomer's agents monorepo bundles MCP + CLI + AI skills. czlonkowski's n8n-skills adds 7 Claude Code skills on top of the MCP server. Zapier's agentic configuration provides meta-tools for autonomous action management. The pattern is moving from "expose APIs" to "enable autonomous workflows."

**Safety controls exist where they matter.** Airflow's read-only mode, Kestra's tool disabling, Prefect's multi-tenant auth, Windmill's scoped MCP tokens, and n8n-mcp's production safety warnings reflect mature thinking about AI-agent access to production systems.

### What's missing

**No unified cross-platform server.** You can't manage n8n workflows and Airflow DAGs from the same MCP server. Each platform requires its own server, its own configuration, and its own mental model. Pipedream comes closest with 3,000+ APIs but doesn't orchestrate across platforms.

**Dagster is stagnant.** The only Dagster MCP server has 2 commits and hasn't been updated since April 2025. No official Dagster MCP server exists yet.

**Monitoring still dominates over creation.** Most servers are stronger at monitoring workflows (checking status, reading logs, inspecting runs) than creating them. n8n and Windmill are exceptions — they can build workflows from scratch.

## The bottom line

**For low-code automation:** Start with **czlonkowski/n8n-mcp** if you use n8n — it's the most complete automation MCP server by far (18,700 stars, 1,505 nodes). Use **Zapier MCP** if you need breadth across 9,000+ apps. Use **Activepieces** if you want open-source Zapier-like breadth with 280+ MCP-enabled pieces. Use **Make MCP** if you've already built complex multi-step scenarios.

**For multi-API access:** Use **Pipedream MCP** for direct API operations across 3,000+ services with 10,000+ prebuilt tools — best for agents that need raw API flexibility rather than pre-built workflows.

**For data pipelines:** Use **yangkyeongmo/mcp-server-apache-airflow** for full Airflow API access, or **astronomer/agents** for the integrated AI toolkit (MCP + CLI + skills). For Dagster, the community server covers the basics but is dormant.

**For code-first orchestration:** **Windmill** is the new standout with built-in MCP, multi-language support, and strong performance. **Prefect's official server** remains a solid choice despite beta status. **GethosTheWalrus/temporal-mcp** is now the recommended Temporal server with active development and proper releases.

**For event-driven workflows:** **Kestra's official server** provides clean coverage of the core platform with sensible safety controls.

**Rating: 4.5/5** — The workflow automation MCP category has improved significantly since March 2026. Three major gaps are now filled (Windmill, Activepieces, Pipedream), n8n continues its explosive growth (+24% in 41 days), Astronomer consolidated into a comprehensive agent toolkit, and Temporal has an actively maintained replacement. Official vendor participation is the strongest in any MCP category. The only notable gaps are Dagster stagnation and the lack of cross-platform orchestration. This is one of the most mature and well-served MCP categories.

*This review was refreshed on 2026-04-25 using Claude Opus 4.6 (Anthropic).*

# Workflow Automation MCP Servers — n8n, Zapier, Make & More

> 20+ workflow automation MCP servers compared — n8n (15K stars), Zapier, Make, Airflow, Prefect, Kestra, and Dagster. Which ones let AI agents actually automate workflows?


Workflow automation and orchestration is where MCP gets genuinely useful for operations teams. Instead of manually navigating UIs to build workflows, check pipeline statuses, or debug failed runs, these servers let AI agents do it through natural language. Part of our **[Business & Productivity MCP category](/categories/business-productivity/)**.

The landscape splits into four categories: **low-code automation platforms** (n8n, Zapier, Make — visual workflow builders that connect apps), **data pipeline orchestrators** (Airflow, Dagster — scheduled DAG-based data processing), **code-first orchestration engines** (Temporal, Prefect — durable execution for distributed systems), and **event-driven orchestrators** (Kestra — declarative YAML-based workflows).

The headline findings: **n8n dominates adoption with 15,100 stars on its primary MCP server** — the largest MCP server in any automation category. **Zapier offers the broadest integration surface** at 8,000+ apps, but with a remote-only architecture. **Airflow has the deepest tool coverage** at 70+ operations across the full REST API. **Official vendor participation is strong** — Zapier, Make, Prefect, Kestra, and Astronomer all ship their own MCP servers. **Temporal was promising but archived** in January 2026. **The low-code/no-code side is crowded** while code-first orchestrators are underserved.

## Low-Code Automation Platforms

### n8n (Community Leader)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) | 15,100 | TypeScript | 20+ | stdio |

**czlonkowski/n8n-mcp** (15,100 stars, TypeScript, MIT, 922 commits) is the primary MCP server for n8n and one of the most starred MCP servers in any category.

The scope is remarkable. It provides structured access to **1,239 n8n nodes** — 537 core nodes and 547 community nodes (301 verified) — with 99% coverage of node properties and detailed schemas. Documentation coverage sits at 87% from official n8n docs. Beyond node documentation, it includes **2,709 searchable workflow templates** with full metadata.

Core capabilities: **Workflow management** — create, read, update, delete, list, validate, and autofix workflows through the n8n API. **Execution management** — trigger workflows, retrieve results, list execution history, delete executions. **Node documentation** — search and browse node schemas, properties, and operations. **Template library** — search workflow templates by keyword with full metadata.

Multiple deployment options: hosted service, Docker, npx, local installation, and Railway cloud deployment. AI-capable tool variants include enriched documentation context for better LLM comprehension.

This is effectively a complete n8n SDK accessible through MCP. The 15,100-star count reflects genuine adoption — n8n itself has 179,000 stars, and this server is the primary bridge for AI-assisted workflow building.

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
| [zapier/zapier-mcp](https://github.com/zapier/zapier-mcp) | 20 | TypeScript | Dynamic | Remote (SSE) |

**zapier/zapier-mcp** (20 stars, TypeScript, MIT) is the official Zapier MCP server — a remote-first server that gives AI agents access to **8,000+ apps and 40,000+ actions** without local installation.

The architecture is different from most MCP servers. Instead of exposing a fixed set of tools, you configure actions in Zapier's dashboard, and each action becomes a callable MCP tool. One built-in meta-tool (`get_configuration_url`) helps set up new actions. Authentication is handled via API key (personal use) or OAuth (for apps where end users connect their own Zapier accounts).

The breadth is unmatched — no other MCP server connects to as many services. But the tradeoff is indirection: you're calling Zapier's API, which calls the target app's API. Latency is higher, debugging is harder, and you depend on Zapier's uptime and pricing.

Two auth modes: **API Key** for personal/development use, **OAuth** for building products where users bring their own Zapier accounts. The remote architecture means zero local setup — point your MCP client at `mcp.zapier.com` and authenticate.

The 20-star count on GitHub is misleading — most Zapier users configure it through the Zapier UI, not by cloning the repo.

### Make (Official)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [integromat/make-mcp-server](https://github.com/integromat/make-mcp-server) | 153 | TypeScript | Dynamic | SSE / Streamable HTTP |

**integromat/make-mcp-server** (153 stars, TypeScript, MIT, 14 commits) is Make's official MCP server. Like Zapier, it takes a dynamic approach — but centered on **scenarios** rather than individual actions.

The server connects to your Make account, identifies all scenarios configured with "On-Demand" scheduling, and exposes each as a callable MCP tool. It parses input parameters and resolves meaningful descriptions automatically. Responses come back as structured JSON.

A cloud-hosted version is also available, which Make recommends for most use cases. The self-hosted version gives you more control but requires Docker or local Node.js.

The scenario-first model is Make's differentiator. Instead of configuring individual API actions (Zapier's approach), you build complete multi-step scenarios in Make's visual builder, then expose the whole scenario as a single MCP tool. This is more powerful for complex workflows — one tool call can trigger a 20-step automation — but requires pre-building scenarios in Make's UI.

## Data Pipeline Orchestrators

### Apache Airflow

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [yangkyeongmo/mcp-server-apache-airflow](https://github.com/yangkyeongmo/mcp-server-apache-airflow) | 147 | Python | 70+ | stdio |
| [astronomer/astro-airflow-mcp](https://github.com/astronomer/astro-airflow-mcp) | 8 | Python | 24+ | stdio |
| [call518/MCP-Airflow-API](https://github.com/call518/MCP-Airflow-API) | — | Python | 45 | stdio |

**yangkyeongmo/mcp-server-apache-airflow** (147 stars, Python, MIT, 121 commits) wraps the full Apache Airflow REST API v1. With 70+ operations across DAGs, runs, tasks, variables, connections, pools, datasets, and monitoring, it's the most comprehensive Airflow MCP server.

Key safety feature: **read-only mode** for non-destructive operations — critical when connecting AI agents to production Airflow clusters. Selective API group configuration lets you expose only the operations you need. Supports Basic Auth and JWT tokens.

**astronomer/astro-airflow-mcp** (8 stars, Python, Apache 2.0, official from Astronomer) takes a different approach with **consolidated tools** rather than raw API wrapping. Tools like `explore_dag`, `diagnose_dag_run`, and `get_system_health` combine multiple API calls into higher-level operations that are more natural for AI agents.

Supports both Airflow 2.x and 3.x with automatic version detection. Can run as a standalone server or as an integrated Airflow 3.x plugin. Flexible authentication (bearer tokens, OAuth2, basic auth). Includes MCP Resources for static Airflow info and MCP Prompts for guided workflows.

**MCP-Airflow-API** (call518, 45 tools) provides comprehensive cluster management including service operations, configuration management, status monitoring, and request tracking. It specifically supports Airflow 2.x and 3.0+ with automatic version detection.

The community vs. official split is interesting here. The community server (yangkyeongmo) has far more stars and raw API coverage. The official Astronomer server has fewer tools but better-designed ones for AI agent workflows. **For monitoring and debugging, use Astronomer. For full API access, use yangkyeongmo.**

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
| [brief-hq/temporal-mcp](https://github.com/brief-hq/temporal-mcp) | 59 | Go | 19 | stdio |

**brief-hq/temporal-mcp** (59 stars, Go, MIT, 26 commits) bridged AI assistants to Temporal's workflow orchestration — enabling natural language control of complex distributed workflows.

Capabilities spanned the full Temporal surface area: individual workflow lifecycle management (start, cancel, terminate, signal, query), real-time status checking, batch operations across many workflows simultaneously, and complete schedule management via cron expressions. **Automatic workflow discovery** and smart caching for performance optimization were standout features.

**However, this repository was archived on January 29, 2026** and is now read-only. The archival is notable because Temporal itself remains actively developed. A separate implementation exists at **GethosTheWalrus/temporal-mcp** (focusing on lifecycle management and scheduling), and Temporal's official code exchange lists a [Temporal MCP Server](https://temporal.io/code-exchange/temporal-mcp-server) entry. The space is actively evolving despite this specific project's archival.

For teams using Temporal, the MCP integration story is currently fragmented — there's no single dominant, actively maintained server.

### Prefect (Official)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [PrefectHQ/prefect-mcp-server](https://github.com/PrefectHQ/prefect-mcp-server) | 29 | Python | 10+ | stdio |

**PrefectHQ/prefect-mcp-server** (29 stars, Python, Apache 2.0, 104 commits) is the official Prefect MCP server, still in beta with APIs subject to change.

Capabilities include monitoring and inspection of deployments, flow runs, and task runs. Execution log retrieval and event tracking. CLI skill support for mutations like triggering deployments. **Intelligent debugging assistance** for troubleshooting failures — this is where Prefect's MCP server differentiates from raw API wrappers.

Multi-tenant HTTP header authentication supports centralized deployments where multiple users share one MCP server instance. Can be deployed to FastMCP Cloud for remote access.

The beta status means expect breaking changes, but official vendor backing makes this a safer bet than community alternatives for Prefect users.

## Event-Driven Orchestrators

### Kestra (Official)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [kestra-io/mcp-server-python](https://github.com/kestra-io/mcp-server-python) | 24 | Python | 11 | stdio |

**kestra-io/mcp-server-python** (24 stars, Python, Apache 2.0, 20 commits) is the official Kestra MCP server covering 11 tools across the platform: Backfill, Execution, Files, Flow, Key-Value store, Logs, Namespace, Replay, Restart, Resume, and Enterprise Edition tools.

Kestra itself is an event-driven orchestration platform (16,800 stars on the main repo) designed for both scheduled and event-driven workflows. The MCP server provides a natural language interface to this platform — manage flows, trigger executions, inspect logs, handle backfills, and work with the key-value store.

Docker deployment available. Supports both OSS and Enterprise Edition installations. Configurable tool disabling via environment variables — useful for restricting what AI agents can do. Flexible logging levels.

The 11-tool count is modest but well-chosen. Each tool maps to a core Kestra concept rather than a raw API endpoint, making the server more AI-friendly.

## The big picture

### Adoption comparison

| Platform | MCP Server(s) | Stars | Official? | Tools | Strength |
|----------|---------------|-------|-----------|-------|----------|
| n8n | czlonkowski/n8n-mcp | 15,100 | Community | 20+ | Node coverage (1,239), templates |
| Zapier | zapier/zapier-mcp | 20 | Yes | Dynamic | App breadth (8,000+) |
| Make | integromat/make-mcp-server | 153 | Yes | Dynamic | Scenario-as-tool model |
| Airflow | yangkyeongmo + astronomer | 147 / 8 | Mixed | 70+ / 24+ | Deepest tool coverage |
| Temporal | brief-hq/temporal-mcp | 59 | Community | 19 | Archived Jan 2026 |
| Prefect | PrefectHQ/prefect-mcp-server | 29 | Yes | 10+ | Intelligent debugging |
| Kestra | kestra-io/mcp-server-python | 24 | Yes | 11 | Event-driven, tool disabling |
| Dagster | kyryl-opens-ml/mcp-server-dagster | 21 | Community | 9 | Asset materialization |

### What's working

**The low-code side is well-served.** n8n's MCP ecosystem is mature with multiple competing implementations. Zapier and Make both ship official servers with fundamentally different approaches (action-first vs. scenario-first). If you're building workflows in a visual builder, the MCP integration story is solid.

**Official vendor participation is strong.** Five of the eight platforms listed have official or vendor-backed MCP servers. This is above average for MCP categories — many categories still rely entirely on community implementations.

**Safety controls exist where they matter.** Airflow's read-only mode, Kestra's tool disabling, and Prefect's multi-tenant auth reflect the reality that connecting AI agents to production orchestrators requires guardrails.

### What's missing

**No unified cross-platform server.** You can't manage n8n workflows and Airflow DAGs from the same MCP server. Each platform requires its own server, its own configuration, and its own mental model.

**Temporal is underserved.** The most promising Temporal MCP server was archived. For a platform used in mission-critical distributed systems, the MCP story is fragmented.

**No Windmill MCP server.** Windmill — an increasingly popular open-source workflow engine — has no MCP server despite being developer-focused and MCP-friendly in philosophy.

**Monitoring over creation.** Most of these servers are stronger at monitoring workflows (checking status, reading logs, inspecting runs) than creating them. The n8n servers are the exception — they can build workflows from scratch.

## The bottom line

**For low-code automation:** Start with **czlonkowski/n8n-mcp** if you use n8n — it's the most complete automation MCP server by far. Use **Zapier MCP** if you need breadth across 8,000+ apps. Use **Make MCP** if you've already built complex multi-step scenarios.

**For data pipelines:** Use **yangkyeongmo/mcp-server-apache-airflow** for full Airflow API access, or **astronomer/astro-airflow-mcp** for AI-friendly consolidated tools. For Dagster, the community server covers the basics.

**For code-first orchestration:** **Prefect's official server** is the safest choice despite beta status. Temporal users should evaluate the remaining community options.

**For event-driven workflows:** **Kestra's official server** provides clean coverage of the core platform with sensible safety controls.

**Rating: 4.0/5** — The workflow automation MCP category benefits from strong official vendor participation, the n8n ecosystem's remarkable adoption (15,100 stars), and genuinely useful operational tooling across the data orchestration space. The Temporal gap and lack of cross-platform tooling prevent a higher rating, but the fundamentals are solid. If you're managing workflows through AI agents, the tools are ready.

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*


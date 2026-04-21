---
title: "dbt MCP Server — Governed Data Context for AI Agents"
date: 2026-04-21T18:00:00+09:00
description: "The official dbt MCP server connects AI agents to dbt projects via the Model Context Protocol — data discovery, semantic layer queries, lineage, CLI execution, and code generation. Community alternatives reviewed."
og_description: "dbt MCP server reviewed — official dbt-labs/dbt-mcp (540 stars, v1.14.0, 30+ tools), dbt-core-mcp, dbt-cli-mcp, semantic layer server. Rating: 4/5."
content_type: "Review"
card_description: "MCP server that connects AI agents to dbt projects for data discovery, semantic layer queries, lineage analysis, model execution, and code generation. Official server from dbt Labs with local and remote deployment options."
last_refreshed: 2026-04-21
---

Part of our **[Data & Databases MCP category](/categories/data-databases/)**.

*At a glance: The official dbt MCP server (dbt-labs/dbt-mcp, 540 stars, 115 forks, Apache-2.0, Python) provides 30+ tools for data discovery, semantic layer queries, SQL execution, lineage analysis, dbt CLI commands, and code generation. v1.14.0 released April 14, 2026 — 14 releases since launch. Two deployment modes: local (uvx, dbt Core/Fusion) and remote (HTTP, dbt Platform). Community alternatives include dbt-core-mcp (11 stars, zero-dependency bridge), dbt-cli-mcp (19 stars, CLI wrapper), and dbt-semantic-layer-mcp-server (11 stars, TypeScript semantic layer).*

dbt (data build tool) is the standard for analytics engineering — over 50,000 organizations use it to transform raw data into trusted models and metrics. The dbt MCP server bridges that structured data context to AI agents, giving them governed access to your data lineage, semantic layer, and transformation pipeline. If your organization runs dbt, this is how AI agents learn what your data means, where it comes from, and how to query it correctly.

## The Official Server (dbt-labs/dbt-mcp)

[dbt-labs/dbt-mcp](https://github.com/dbt-labs/dbt-mcp) launched April 21, 2025 as an experimental open source project. One year later, it's at v1.14.0 with 14 releases, active weekly development, and deep integration with dbt's platform strategy.

**Key metrics:**
- **Stars:** 540 | **Forks:** 115 | **Commits:** 540 | **Open issues:** 23 | **Open PRs:** 17
- **Latest:** v1.14.0 (April 14, 2026)
- **Language:** Python (96%)
- **License:** Apache-2.0
- **PyPI downloads:** ~16,500/week, ~69,400/month (growing — up from early months)
- **PulseMCP:** ~332K all-time visitors, ~18.4K weekly, #132 globally (#103 this week)

### Tool Categories

The server organizes tools across seven categories, covering both local and remote deployment:

**Semantic Layer (remote)**
- `list_metrics` — browse and search available metrics with dimensions and entities
- `get_dimensions` / `get_entities` — retrieve metadata for specific metrics
- `query_metrics` — execute metric queries with filtering
- `get_saved_queries` — access pre-built semantic layer queries
- `get_compiled_sql` — preview SQL without execution

**Discovery API (remote)**
- Model, source, exposure, and macro exploration
- Ancestor/descendant lineage traversal
- Model health and performance metrics
- Semantic search across project models

**SQL Execution (remote)**
- `execute_sql` — run SQL on dbt Platform with Semantic Layer support
- Natural language to SQL generation

**dbt CLI (local)**
- `dbt_build`, `dbt_run`, `dbt_test`, `dbt_compile`, `dbt_clone`
- `dbt_docs_generate` — build documentation
- `dbt_list` — list resources with selectors
- YML selectors support (v1.13.0+)

**Admin API (remote)**
- Job management and triggering (with `steps_override`)
- Run monitoring and artifact access
- `list_projects` — account-level project discovery (v1.11.0+)

**Code Generation (local)**
- YAML scaffolding for models and sources
- Staging model creation from source definitions

**Advanced (Fusion/LSP)**
- Column-level lineage analysis
- dbt documentation search and retrieval
- Server metadata queries

### Two Deployment Modes

**Local MCP** — runs on your machine via `uvx`. Requires dbt Core or dbt Fusion installed. Provides CLI tools, code generation, and local manifest analysis. Best for development workflows with Claude Desktop, Cursor, or VS Code.

**Remote MCP** — connects to dbt Platform via HTTP. Provides Semantic Layer, Discovery API, SQL execution, Admin API, and Fusion tools. No local dbt installation needed. Supports OAuth authentication with project selection UI (improved in v1.13.0).

Both modes can run simultaneously, and the experimental MCPB (MCP Bundle) published with each release allows MCPB-aware clients to import the server without additional setup.

## Recent Release Cadence

The development pace is strong — 6 releases in 8 weeks:

| Version | Date | Highlights |
|---------|------|-----------|
| v1.14.0 | Apr 14 | Telemetry with cloud account IDs, auto-fetch DBT_HOST_PREFIX, configurable metric threshold for list_metrics |
| v1.13.0 | Apr 7 | YML selectors for CLI tools, reduced page limits (prevented IDE freezing), OAuth project selection improvements |
| v1.12.0 | Apr 1 | Multi-project discovery tools, configuration override support |
| v1.11.0 | Mar 25 | steps_override for job triggers, list_projects tool, multi-project semantic layer, AG2 multi-agent example |
| v1.10.0 | Mar 10 | Product documentation tools, Dependabot, relaxed dbt-protos version requirements |
| v1.9.0 | Feb 11 | Docker support, macro discovery (get_all_macros), AI SDK agent example (TypeScript) |

## Community Alternatives

### dbt-core-mcp (NiclasOlofsson)

A [zero-dependency bridge](https://github.com/NiclasOlofsson/dbt-core-mcp) (11 stars, 181 commits, MIT, Python) that auto-detects and uses your existing dbt environment.

**Key differentiator:** No dbt-core or adapters required on the server — it bridges to whatever dbt version and adapter your project already uses. Works with DuckDB, Snowflake, Postgres, BigQuery, Databricks.

Tools include project metadata, unified resource discovery, lineage/impact analysis, column-level lineage tracing, database queries with Jinja support (ref/source functions), model execution with state-based change detection, and CTE isolation for debugging.

**Limitation:** Python models not supported — SQL only.

### dbt-cli-mcp (MammothGrowth)

A [CLI wrapper](https://github.com/MammothGrowth/dbt-cli-mcp) (19 stars, 25 commits, Python) that exposes standard dbt CLI commands (`run`, `test`, `ls`, `compile`, `debug`, `deps`, `seed`, `show`) as MCP tools. Simpler scope than the official server — for teams that just want AI agents to invoke dbt commands.

### dbt-semantic-layer-mcp-server (TommyBez)

A [TypeScript-based server](https://github.com/TommyBez/dbt-semantic-layer-mcp-server) (11 stars, 41 commits) focused exclusively on the dbt Semantic Layer. Metric discovery, query creation, data analysis with filters/grouping, and result visualization in AI assistant interfaces. Installable via Smithery.

### Streamlit MCP Cortex (dbt-labs)

An official [Streamlit application](https://github.com/dbt-labs/streamlit_mcp_cortex) that connects Snowflake Cortex to dbt's remote MCP server — a "chat with your data" experience for analytics. Not a standalone MCP server, but shows the platform integration direction.

## Setup

**Local (recommended for development):**

```json
{
  "mcpServers": {
    "dbt": {
      "command": "uvx",
      "args": ["dbt-mcp"],
      "env": {
        "DBT_PROJECT_DIR": "/path/to/your/dbt/project"
      }
    }
  }
}
```

**Remote (dbt Platform):**

```json
{
  "mcpServers": {
    "dbt-remote": {
      "url": "https://mcp.cloud.getdbt.com/sse",
      "headers": {
        "Authorization": "Bearer YOUR_DBT_CLOUD_TOKEN"
      }
    }
  }
}
```

OAuth authentication is also supported for remote connections — v1.13.0 improved the project selection flow with search and navigation.

## What's Good

**Comprehensive tool surface.** 30+ tools spanning discovery, semantic layer, SQL, CLI, admin, and code generation. This covers the full dbt workflow — from exploring what data exists to building models and monitoring jobs.

**Semantic Layer integration.** This is the killer feature. The dbt Semantic Layer provides governed metric definitions — dimensions, entities, filters, and compiled SQL. AI agents querying through the semantic layer get consistent, accurate answers because the metrics are pre-defined by data teams. dbt Labs [benchmarks show](https://docs.getdbt.com/blog/semantic-layer-vs-text-to-sql-2026) near-100% accuracy for covered queries vs. unreliable text-to-SQL.

**Active development.** 14 releases in one year, 6 in the last 8 weeks. Features are shipping fast: multi-project support, documentation tools, OAuth improvements, MCPB bundles. This isn't a side project — it's a core part of dbt's AI strategy.

**Local + remote flexibility.** Local mode for development (fast, offline, full CLI access), remote mode for production (semantic layer, discovery API, no local install). Run both simultaneously for the full tool surface.

**Multi-project support.** v1.11.0+ added project-level scoping for semantic layer tools and v1.12.0 added multi-project discovery. Real enterprises have many dbt projects — this is table-stakes functionality that shipped early.

**MCPB bundle.** The experimental MCP Bundle published with each release reduces setup friction for compatible clients — one import instead of manual configuration.

## What's Not

**PyPI downloads are modest.** ~16,500/week is healthy for a data tooling niche but low compared to top MCP servers (Fetch: ~202K/week, Firecrawl: ~8.8K/week npm). Adoption is growing but still early.

**7 open bugs.** Notable: #708 (`list_metrics` overwhelms disk with many metrics), #585 (dbt-lsp panics on connect), #594 (special characters in markdown break lineage), #560 (OAuth broken with uvx git install), #401 (BigQuery OAuth fails on Windows). These are real usability issues.

**Remote requires dbt Platform.** Semantic layer, discovery API, and SQL execution all require a dbt Cloud/Platform account. Local mode has CLI and code generation but not the most valuable tools. This creates a commercial dependency.

**No formal security audit.** No CVEs filed against dbt-mcp specifically, but #687 requests OIDC auth gateway for remote deployments — the current token-based auth doesn't meet enterprise requirements for some teams.

**Documentation tools can freeze IDEs.** v1.13.0 had to reduce page limits because documentation retrieval was crashing clients. Tool responses returning large payloads is a known MCP design challenge.

**Fivetran merger uncertainty.** dbt Labs and Fivetran [announced a merger](https://www.getdbt.com/blog/dbt-labs-and-fivetran-merge-announcement) (October 2025, all-stock deal, ~$600M combined ARR). Expected to close mid-to-late 2026. dbt Core will remain open source, but product roadmap priorities could shift. George Fraser (Fivetran CEO) will lead the combined company.

## dbt Labs Platform Context

dbt Labs is a significant company in the data infrastructure space:

- **Valuation:** $4.2B (Series D, $222M raised from Altimeter, a16z, Sequoia, Databricks, Snowflake)
- **Users:** 50,000+ organizations
- **dbt Fusion:** Next-gen engine with Rust-based LSP, significant memory and performance improvements
- **dbt Agents:** Native AI agents for analytics development (Enterprise tier, beta/waitlist). Suite includes development, data exploration, and pipeline monitoring agents — all powered by the MCP server
- **Semantic Layer benchmarks:** Near-100% accuracy for governed metric queries, vs. unreliable text-to-SQL alternatives
- **dbt Summit 2026:** Upcoming (waitlist open)
- **Partnerships:** Microsoft (Fusion on Fabric), Snowflake (Cortex integration), Stripe (Projects co-design)

The MCP server is central to dbt's AI strategy — the [dbt Agents](https://www.getdbt.com/product/dbt-agents) product is built on top of it. This means the MCP server gets first-class investment, not side-project maintenance.

## Security Considerations

**No dbt-mcp-specific CVEs** have been filed as of April 2026. However:

- The broader MCP ecosystem has 30+ CVEs (tracked by VulnerableMCP.info), and dbt-mcp uses the MCP Python SDK (upgraded to v1.26.0 in v1.9.3)
- Token-based authentication for remote connections means leaked tokens grant access to semantic layer queries, project discovery, and SQL execution
- Local mode runs dbt commands with the user's system permissions — a compromised MCP client could execute arbitrary dbt operations
- #687 (open) requests OIDC auth gateway for production remote deployments
- Dependabot was added in v1.10.0 for dependency security monitoring

**Recommendations:**
- Use OAuth with project scoping for remote connections rather than long-lived tokens
- Scope dbt Cloud tokens to minimum necessary permissions
- Monitor dbt Audit Logs for MCP-initiated operations
- For local mode, ensure the MCP client runs in a sandboxed environment

## How It Compares

**vs [Supabase MCP](/reviews/supabase-mcp-server/)** (4/5): Supabase gives direct database access. dbt MCP gives governed access through the semantic layer — your data team's metric definitions, not raw tables. Different abstraction levels; dbt is higher-level and safer for business users.

**vs [Neon MCP](/reviews/neon-mcp-server/)** (4/5): Neon is a Postgres MCP server — SQL execution and database management. dbt MCP adds the transformation layer (lineage, metrics, models) on top of whatever warehouse you use. Complementary, not competing.

**vs raw SQL MCP servers**: Any SQL MCP server can query your warehouse. dbt MCP provides context — what does this table mean, where does it come from, what metrics are defined on it, which models are tested and documented. The semantic layer prevents AI hallucination of metric definitions.

**vs [Snowflake MCP](/reviews/snowflake-mcp-servers/)**: Snowflake's Cortex now integrates directly with dbt's remote MCP server. If you're on Snowflake + dbt, both MCP servers together give you warehouse operations (Snowflake) plus governed data context (dbt).

## Who Should Use This

**Data teams using dbt Cloud/Platform** wanting AI agents with governed data access → official dbt-mcp remote mode (semantic layer, discovery API, multi-project support)

**Analytics engineers** using dbt Core/Fusion in development → official dbt-mcp local mode (CLI execution, code generation, lineage analysis via Fusion LSP)

**Teams wanting lightweight dbt CLI access** without the full server → dbt-cli-mcp (8 CLI commands as MCP tools, minimal setup)

**dbt Core users** who want zero-dependency integration → dbt-core-mcp (auto-detects your environment, works with any adapter)

**Semantic layer-only use cases** → dbt-semantic-layer-mcp-server (TypeScript, focused scope, installable via Smithery)

## Bottom Line

The dbt MCP server is one of the strongest official MCP implementations in the data tooling space. The semantic layer integration is the standout feature — AI agents querying through governed metric definitions get reliable, consistent answers instead of hallucinated SQL. The development pace (14 releases in a year, 6 in the last 8 weeks) and platform investment (dbt Agents built on top of the MCP server) signal this is a core product, not an experiment.

The main limitation is the commercial dependency: the most valuable tools (semantic layer, discovery, SQL execution) require dbt Platform. Local mode covers CLI and code generation but misses the data discovery and querying capabilities that make dbt MCP compelling. The open bugs are real but manageable, and the community alternatives (dbt-core-mcp, dbt-cli-mcp) fill specific niches.

For organizations already invested in dbt, this is a no-brainer adoption. The governed data context it provides to AI agents is materially better than raw SQL access. For teams evaluating dbt adoption, the MCP server is one more reason the platform is worth the investment.

**Rating: 4/5** — Strong official MCP implementation with comprehensive tool coverage, active development, and the semantic layer as a genuine differentiator for governed AI data access. Docked for commercial dependency on dbt Platform for the most valuable features, modest adoption metrics, open usability bugs, and merger uncertainty.

*Last updated: April 21, 2026*

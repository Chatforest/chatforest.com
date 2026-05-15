---
title: "dbt Labs MCP Server — 50+ Tools for Data Transformation, Semantic Layer, and dbt Cloud Orchestration"
date: 2026-05-16T16:00:00+09:00
description: "The official dbt Labs MCP server gives AI agents deep access to dbt's full stack: SQL execution, natural language to SQL, semantic layer queries, 19 Discovery API tools for lineage and model health, dbt CLI commands, job orchestration, and code generation — 50+ tools across 9 categories. Apache-2.0 license. Active weekly releases."
og_description: "dbt Labs MCP server: 50+ tools (SQL, Semantic Layer, Discovery API, CLI, Admin API, codegen), Apache-2.0, 561 stars, weekly releases. Free for dbt Core CLI users; cloud features require paid dbt Cloud plan. Critical gotcha: Copilot credit exhaustion blocks all remote tools. Rating: 4/5."
content_type: "Review"
card_description: "The official dbt Labs MCP server exposes 50+ tools across SQL execution, semantic layer queries, model lineage, dbt CLI commands, job orchestration, and code generation. Open source (Apache-2.0), 561 GitHub stars, weekly releases. Cloud features require a paid dbt Cloud plan; dbt Core users get CLI tools for free."
last_refreshed: 2026-05-16
---

**At a glance:** The official `dbt-labs/dbt-mcp` server gives AI agents comprehensive access to dbt's full data transformation stack — **50+ tools across 9 categories** including SQL execution, natural language to SQL conversion, semantic layer queries, 19 Discovery API tools for model lineage and health, 11 dbt CLI commands, job orchestration, and YAML code generation. Open source under Apache-2.0 with **561 GitHub stars**, 119 forks, and weekly releases reaching v1.19.1 as of May 14, 2026. Free to use for **dbt Core** (open-source) local workflows; cloud-connected features require a paid **dbt Cloud** subscription. There are important gotchas around pricing and the `text_to_sql` tool that every user should read before deploying.

[dbt](https://www.getdbt.com/) (data build tool) is the de facto standard for SQL-based data transformation in modern data stacks. Maintained by dbt Labs, the open-source `dbt-core` project has become the transformation layer of choice in analytics engineering, pairing with ELT tools like Airbyte and Fivetran and warehouses like Snowflake, BigQuery, and Redshift. The MCP server ships with an OpenSSF Best Practices badge and a community Slack channel (`#tools-dbt-mcp`), signaling dbt Labs treats this as a production-grade integration rather than an experiment.

## What dbt Is

dbt (data build tool) is a **SQL-first data transformation framework** that lets analytics engineers write `SELECT` statements and dbt handles the rest — creating tables/views, managing dependencies, testing data quality, and generating documentation. It sits at the **T in ELT**: after raw data lands in your warehouse (via tools like Airbyte or Fivetran), dbt transforms it into analysis-ready models.

**Two deployment flavors:**

- **dbt Core** — open source, self-hosted, runs via CLI. Free to use. Manages transformations locally against your data warehouse.
- **dbt Cloud** — hosted SaaS platform adding orchestration (scheduled job runs), a web IDE, the Semantic Layer (metric governance), Discovery API (metadata queries), and the Explorer UI. Requires a paid subscription for API access.

The **dbt Semantic Layer** deserves particular attention: it's a governed layer that defines metrics (`revenue`, `active_users`, `churn_rate`) once in YAML and makes them queryable consistently across BI tools and AI agents. This is a strong differentiator for agentic use cases — agents can query `list_metrics` and `query_metrics` against a single source of truth rather than reverse-engineering SQL logic from raw tables.

**dbt platform scale:**  
dbt Core is used by hundreds of thousands of data teams. The GitHub repository has tens of thousands of stars. The dbt Community Slack has over 70,000 members. dbt Cloud is a commercially successful SaaS product.

## Installation

**Via uvx (recommended):**

```bash
uvx dbt-mcp
```

**Via pip:**

```bash
pip install dbt-mcp  # Requires Python >=3.12, <3.14
```

**Via Docker:**

```bash
docker pull ghcr.io/dbt-labs/dbt-mcp:latest
```

The Docker image runs as a non-root `appuser`, uses Python 3.12-slim as its base, and defaults to STDIO transport (`MCP_TRANSPORT=stdio`). No ports are exposed by default — it communicates over stdin/stdout, making it appropriate for Claude Desktop integration.

**Environment configuration** (`.env` file):

```env
DBT_TOKEN=your_service_token       # dbt Cloud service token
DBT_HOST=cloud.getdbt.com          # or your single-tenant hostname
DBT_PROD_ENV_ID=123456             # Production environment ID
DBT_DEV_ENV_ID=789012              # Developer environment ID
DBT_USER_ID=your_user_id           # dbt Cloud user ID
DBT_PROJECT_DIR=/path/to/dbt/project
DBT_PATH=/path/to/dbt/binary
```

Feature flags let you selectively enable/disable tool categories:

```env
DBT_MCP_ENABLE_SEMANTIC_LAYER=true
DBT_MCP_ENABLE_DISCOVERY_API=true
DBT_MCP_ENABLE_CLI=true
DBT_MCP_ENABLE_ADMIN_API=true
DBT_MCP_ENABLE_CODEGEN=true
```

This granular control is useful for restricting the server to read-only tools in production environments, or disabling CLI tools (which can modify your data models and warehouse objects) when operating with less-trusted clients.

**Remote MCP (no install):**

dbt Labs also hosts a remote HTTP version of the MCP server, accessible via OAuth or service token authentication. The remote version supports Semantic Layer, SQL, Discovery API, Admin API, and Fusion tools — but **omits** dbt CLI and code generation tools (which require local project access).

## Tools: 50+ Across 9 Categories

### SQL Tools (2)

| Tool | What it does |
|------|-------------|
| `execute_sql` | Runs a SQL query directly on dbt Platform infrastructure |
| `text_to_sql` | Converts a natural language question to SQL using dbt project context |

**Critical caveat about `text_to_sql`:** This tool consumes **dbt Copilot credits**, which are allocated per dbt Cloud plan. When Copilot credits are exhausted, the entire remote MCP server becomes unavailable — not just this tool, but **all 50+ tools**. This is a significant operational risk for teams using the remote MCP server in production. dbt Labs acknowledges this behavior but has not changed it as of v1.19.1.

### Semantic Layer Tools (6)

| Tool | What it does |
|------|-------------|
| `list_metrics` | Lists all defined metrics in the dbt Semantic Layer |
| `query_metrics` | Queries one or more metrics with optional dimensions and filters |
| `get_metrics_compiled_sql` | Returns the compiled SQL for a given metric query |
| `get_dimensions` | Lists all dimensions available for a given set of metrics |
| `get_entities` | Lists entities (join keys) available for a metric set |
| `list_saved_queries` | Lists pre-defined saved queries in the Semantic Layer |

The Semantic Layer tools are among the most valuable for agentic use cases. An AI agent can call `list_metrics` to discover what business metrics are available, then `query_metrics` to retrieve actual values — all without writing SQL or understanding the underlying table structure. This is the "governed analytics" pattern: define metrics once, query everywhere.

### Discovery API Tools (19)

The Discovery API provides metadata about your dbt project — model definitions, lineage, test results, performance metrics, and more. These 19 tools give agents a complete picture of your data pipeline's structure and health:

**Model exploration:**
`get_all_models`, `get_model_details`, `get_mart_models`, `get_related_models`, `get_model_children`, `get_model_parents`

**Lineage and impact analysis:**
`get_lineage` — traces upstream/downstream dependencies for any model, source, or exposure

**Health and performance:**
`get_model_health` — returns test pass/fail status, freshness, and quality indicators
`get_model_performance` — returns execution time history and trends

**Assets beyond models:**
`get_all_sources`, `get_source_details`, `get_seed_details`, `get_snapshot_details`
`get_all_macros`, `get_macro_details`
`get_exposure_details`, `get_exposures`
`get_semantic_model_details`, `get_test_details`

**Search (alpha):**
`search` — semantic search across your entire dbt project documentation

These tools enable an AI agent to perform genuine data lineage analysis, answer questions like "which models depend on this source table?" or "which tests are failing in production?", and surface the impact of proposed schema changes.

### dbt CLI Tools (11)

| Tool | What it does |
|------|-------------|
| `run` | Executes dbt models against the warehouse |
| `build` | Runs models, tests, seeds, and snapshots |
| `test` | Runs data quality tests |
| `compile` | Compiles dbt SQL without executing |
| `parse` | Parses project files for validity |
| `list` | Lists project resources matching selectors |
| `show` | Shows a preview of model results |
| `docs` | Generates documentation site |
| `clone` | Clones models for development |
| `get_lineage_dev` | Lineage for local development environment |
| `get_node_details_dev` | Node details for local development environment |

**Security warning from dbt Labs:** The CLI tools "could modify your data models, sources, and warehouse objects." These tools should only be used with clients you trust completely. Consider using the `DBT_MCP_ENABLE_CLI=false` feature flag to disable them when connecting to less-trusted AI clients, or when running in read-only contexts.

### Admin API Tools (10)

These tools manage dbt Cloud job orchestration:

| Tool | What it does |
|------|-------------|
| `list_projects` | Lists dbt Cloud projects |
| `list_jobs` | Lists all jobs in a project |
| `list_jobs_runs` | Lists recent job runs |
| `get_job_details` | Returns job configuration |
| `trigger_job_run` | Triggers a job run |
| `get_job_run_details` | Returns status and metadata for a run |
| `get_job_run_error` | Returns error details for a failed run |
| `list_job_run_artifacts` | Lists artifacts produced by a run |
| `retry_job_run` | Retries a failed run |
| `cancel_job_run` | Cancels an in-progress run |

An AI agent with these tools can participate in dbt Cloud orchestration: trigger production runs, monitor status, retrieve error logs from failures, and retry failed jobs — all from within a chat interface. This is powerful for DevOps workflows where engineers want to interact with data pipelines conversationally.

### Code Generation Tools (3)

| Tool | What it does |
|------|-------------|
| `generate_model_yaml` | Generates YAML metadata for an existing model |
| `generate_source` | Generates a `sources.yml` definition for a database table |
| `generate_staging_model` | Generates a staging model SQL file from a source |

These tools accelerate the most tedious parts of dbt development: writing YAML. An agent can generate boilerplate model documentation, source definitions, and staging models — work that takes human engineers significant time to do well.

### LSP/Fusion Tools (3)

| Tool | What it does |
|------|-------------|
| `fusion.compile_sql` | Compiles a SQL snippet using dbt's Jinja engine |
| `fusion.get_column_lineage` | Returns column-level lineage (which source columns feed which output columns) |
| `get_column_lineage` | Column lineage via the Discovery API |

Column-level lineage is a distinctive capability: rather than model-level lineage (Model A depends on Model B), these tools trace individual column provenance through transformation chains. This matters for data governance and impact analysis.

### Documentation Tools (2)

| Tool | What it does |
|------|-------------|
| `get_product_doc_pages` | Retrieves dbt official documentation pages |
| `search_product_docs` | Semantic search over dbt's official documentation |

### Metadata Tools (2)

| Tool | What it does |
|------|-------------|
| `get_mcp_server_version` | Returns the current server version |
| `get_mcp_server_branch` | Returns the active git branch context |

## Authentication

**Local STDIO mode** uses a `.env` file with a dbt Cloud service token (`DBT_TOKEN`). Service tokens are created in the dbt Cloud UI under Account Settings → Service Tokens. The token needs permissions appropriate for the tools you enable — read-only tokens suffice for Discovery API and metadata queries; admin tokens are needed for job triggering and CLI operations.

**Remote HTTP mode** supports both service token and OAuth authentication. OAuth is the recommended path for user-facing applications where each user should authenticate with their own dbt Cloud credentials.

Credentials are kept in environment variables and never passed through the chat interface or included in LLM context — a standard security practice that the server implements correctly.

## Pricing Realities

**dbt Cloud plans (relevant to MCP usage):**

| Plan | Price | API Access | dbt Copilot |
|------|-------|-----------|-------------|
| Developer (Free) | $0 | **No** | No |
| Starter | ~$100/user/month | Yes | Yes (limited) |
| Enterprise | Custom | Yes | Yes (full) |
| Enterprise+ | Custom | Yes | Yes (full) |

**The free tier trap:** The Developer (free) plan does not include dbt Cloud API access. Since the MCP server's cloud-dependent features — Semantic Layer, Discovery API, Admin API, and `execute_sql` — all require API access, the free tier cannot use these tools. **Only dbt Core local CLI mode is genuinely free.**

For individual analytics engineers using dbt Core locally without dbt Cloud, the local MCP server with CLI tools works without any subscription. But as soon as you want semantic layer queries, Discovery API metadata, or job orchestration, you need a paid plan.

**The Copilot credit block:** The `text_to_sql` tool consumes dbt Copilot credits. When these credits run out, the remote MCP server blocks completely — all tools become unavailable until the next billing period or credits are purchased. Teams should monitor Copilot credit consumption carefully, or disable `text_to_sql` via feature flags if they want guaranteed availability of other remote tools.

## What Works Without a Paid Plan

**dbt Core users (open source, self-hosted) can use for free:**
- All 11 CLI tools (`run`, `build`, `test`, `compile`, `parse`, `list`, `show`, `docs`, `clone`, `get_lineage_dev`, `get_node_details_dev`)
- All 3 code generation tools (`generate_model_yaml`, `generate_source`, `generate_staging_model`)
- LSP/Fusion tools (if Fusion is set up locally)

**Requires a paid dbt Cloud subscription:**
- Semantic Layer queries (requires dbt Cloud Semantic Layer feature)
- Discovery API (all 19 tools)
- Admin API / job orchestration
- `execute_sql` and `text_to_sql`

## Claude.ai Compatibility

**Local STDIO mode:** Requires **Claude Desktop** (the free downloadable app for macOS and Windows). Not compatible with the claude.ai browser interface, which does not natively support local STDIO MCP connections.

**Remote HTTP mode:** Compatible with **Claude.ai Pro, Max, Team, or Enterprise** accounts that support remote MCP integration via OAuth. The remote server uses standard OAuth 2.0 and Streamable HTTP transport, which Claude.ai's MCP support handles. Personal free Claude.ai accounts likely cannot use remote MCP connections (this feature appears limited to paid tiers).

## Release Cadence and Community

The `dbt-labs/dbt-mcp` repository has an exceptionally active development pace:

- **583 total commits** as of this review
- **1–3 releases per week** in May 2026
- Recent releases: v1.19.1 (May 14), v1.19.0 (May 13), v1.18.1 (May 11), v1.18.0 (May 8), v1.17.1 (May 5)
- **OpenSSF Best Practices certification** — the repo meets the Open Source Security Foundation's baseline security standards
- **Community Slack:** `#tools-dbt-mcp` channel in the dbt Community Slack (70,000+ members)
- **22 open issues, 10 open PRs** — healthy engagement without a backlog crisis

Notable third-party alternatives exist but are clearly secondary:
- `pragunbhutani/dbt-llm-agent` (171 stars) — LLM-based dbt analysis agent with remote MCP
- `Astoriel/dbt-doctor` (132 stars) — governance and schema drift detection
- `mattijsdp/dbt-docs-mcp` (23 stars) — documentation search only
- GoCardless maintains a private fork (`gc-dbt-mcp`) for enterprise customization

The official server's 561 stars and 119 forks substantially dominate the third-party alternatives.

## Key Strengths

**Breadth of coverage.** 50+ tools across 9 categories is exceptional. The combination of semantic layer queries, model lineage, CLI operations, job orchestration, and code generation makes this a genuine end-to-end dbt integration — not a thin wrapper around a few read-only endpoints.

**Semantic Layer is a differentiator.** The ability to query governed business metrics (`query_metrics`) directly from a chat interface — without writing SQL or understanding underlying tables — is exactly what enterprise data teams want from AI agents. Metrics are defined once, queried consistently everywhere.

**Column-level lineage.** Most data lineage tools operate at the model level. The `fusion.get_column_lineage` and `get_column_lineage` tools enable column provenance tracing, which is valuable for data governance, compliance, and impact analysis.

**Granular feature flags.** The `DBT_MCP_ENABLE_*` flags let teams selectively enable/disable tool categories, allowing production deployments that expose only read-only tools while keeping write/destructive capabilities off.

**Open source, Apache-2.0.** No proprietary lock-in. Community can contribute, fork, and extend.

**Weekly releases.** The development pace indicates this is a priority product, not a side project.

## Key Weaknesses

**Free tier is largely decorative.** The headline "free" tier (dbt Developer plan) lacks API access, which disqualifies most of the interesting cloud tools. The honest statement is: cloud-connected tools require a $100+/user/month paid plan. Free users get CLI tools only.

**Copilot credit block is an architectural problem.** A single feature (`text_to_sql`) can render the entire remote MCP server unavailable for all 50+ tools. This coupling between a premium feature and core server availability is a design flaw that could cause production disruptions.

**CLI tools carry real risk.** The dbt Labs warning ("could modify your data models, sources, and warehouse objects") deserves emphasis. Tools like `run` and `build` execute against your actual warehouse. Misconfigured AI agent access could trigger unintended data transformations. Treat this like database write access.

**Python 3.12+ requirement.** Teams running older Python environments need to upgrade before using `pip install dbt-mcp`. The `uvx` method avoids this friction in most cases.

**No native claude.ai browser support for local mode.** Requires Claude Desktop or another MCP-capable client application.

## Who Should Use This

**Strong fit:**
- Analytics engineers and data teams actively using dbt Cloud (Starter or Enterprise) who want AI agent access to their transformation layer
- dbt Core users who want CLI automation and code generation without a paid subscription
- Data platform teams evaluating agentic data workflows with semantic layer governance
- Engineers who want to query model lineage, test status, and job health conversationally

**Weak fit:**
- Teams expecting free cloud feature access — the Developer plan limitation is real
- Organizations where CLI tools create unacceptable risk of accidental warehouse modification
- Users who need claude.ai browser access without Claude Desktop

## Verdict

The dbt Labs MCP server is one of the more thoughtfully designed official MCP integrations in the data ecosystem. The **50+ tool surface** covers the full dbt stack meaningfully — semantic layer governance, comprehensive metadata via Discovery API, CLI automation, job orchestration, and code generation — rather than offering a shallow read-only wrapper. The **weekly release cadence** and OpenSSF certification indicate genuine production intent.

The caveats are real but manageable. The **free tier limitation** is the most important: if you're evaluating this for a team, factor in dbt Cloud Starter plan costs ($100+/user/month) for cloud-connected features. The **Copilot credit block** warrants either a feature flag to disable `text_to_sql` in production, or close monitoring of credit consumption. And CLI tool access should be granted thoughtfully — this is warehouse write access, not a harmless read query.

For dbt Core users who want CLI automation and code generation at zero cost, the value is immediate and carries no subscription risk. For dbt Cloud users on paid plans, this is a straightforward win: the integration is well-maintained, well-documented, and covers more ground than most comparable MCP servers.

**Rating: 4/5** — broad, production-grade coverage of the dbt ecosystem with strong open-source credentials and active development; held back by a misleading free tier, the Copilot credit block affecting all tools, and CLI tools that require careful access control.

---

*Research conducted May 2026. Statistics reflect dbt-labs/dbt-mcp as of v1.19.1 (May 14, 2026). Tool lists, pricing, and compatibility may change with subsequent releases.*

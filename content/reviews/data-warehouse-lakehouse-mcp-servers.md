---
title: "Data Warehouse & Lakehouse MCP Servers — Snowflake, BigQuery, Databricks, ClickHouse, DuckDB, Redshift, and More"
date: 2026-03-17T16:30:00+09:00
description: "Data warehouse and lakehouse MCP servers reviewed: ClickHouse official (764 stars), DuckDB/MotherDuck (473 stars, v1.0.5, NOW HTTP transport), Snowflake Labs (277 stars) + managed GA, Apache Doris NEW official (289 stars, 25+ tools), Databricks 4 managed servers (SQL NEW), BigQuery auto-enabled, Dremio NEW official (49 stars). Rating: 4.5/5."
og_description: "Data Warehouse & Lakehouse MCP servers: ClickHouse official (764 stars), DuckDB/MotherDuck (473 stars v1.0.5 HTTP transport), Apache Doris official NEW (289 stars 25+ tools), Snowflake Labs (277 stars) + managed GA, BigQuery auto-enabled, Databricks 4 managed servers SQL NEW, Dremio official NEW, Redshift via AWS. 30+ servers reviewed. Rating: 4.5/5."
content_type: "Review"
card_description: "Data warehousing has exceptional MCP coverage — every major platform has official or vendor-backed support. ClickHouse leads the open-source community with 764 stars. Apache Doris is a notable new official entry with 289 stars and 25+ tools. DuckDB/MotherDuck now supports HTTP transport. BigQuery is auto-enabled. Snowflake has both managed GA and open-source servers. Databricks added SQL as a 4th managed server. Dremio brings lakehouse analytics. This is one of the strongest enterprise MCP categories."
last_refreshed: 2026-04-29
---

Data warehousing and lakehouse platforms have some of the best MCP coverage in the entire ecosystem. Every major vendor — Snowflake, Google BigQuery, Databricks, ClickHouse, MotherDuck/DuckDB, Amazon Redshift, Apache Doris, and Dremio — now offers official or vendor-backed MCP servers. This makes sense: data warehouses are where enterprise data lives, and connecting AI agents to structured data through SQL is one of the highest-value MCP use cases.

The landscape divides into three tiers: **cloud-native warehouses** (Snowflake, BigQuery, Redshift) with managed remote MCP servers, **lakehouse platforms** (Databricks, Dremio) with governance-first MCP integration, and **analytical engines** (ClickHouse, DuckDB, Apache Doris) with open-source community-driven servers. Most teams use at least one from the first two tiers, and DuckDB increasingly bridges them all. Part of our **[Data & Analytics](/categories/data-analytics/)** category.

**What changed since our initial review (March 17, 2026):** DuckDB/MotherDuck added HTTP transport (fixing a key gap we identified), Databricks added SQL execution as a 4th managed server, Apache Doris shipped an official MCP server with 289 stars and 25+ tools, Dremio launched an official MCP server for lakehouse analytics, BigQuery moved from preview to auto-enabled, Snowflake's managed MCP server reached GA, and Databricks introduced Unity AI Gateway for MCP governance.

## ClickHouse — Official Server

| Detail | Info |
|--------|------|
| [ClickHouse/mcp-clickhouse](https://github.com/ClickHouse/mcp-clickhouse) | 764 stars |
| Language | Python |
| Transport | stdio, SSE, Streamable HTTP |
| Tools | 4 |

The official ClickHouse MCP server is the most starred data warehouse MCP server in the open-source community. It provides four tools: `run_query` (execute SQL), `list_databases`, `list_tables` (with pagination), and `run_chdb_select_query` (embedded ClickHouse engine).

### What Works Well

**Dual engine support.** The server works with both remote ClickHouse clusters and [chDB](https://clickhouse.com/docs/chdb), the embedded ClickHouse engine. This means you can query production data remotely or run local analytical queries without a server — same MCP interface for both.

**Safety defaults.** Read-only mode is on by default. Write access requires `--allow-write`, and destructive operations (DROP, TRUNCATE) require a separate `--allow-destructive` flag. This two-tier safety model is well-designed for connecting AI agents to production warehouses.

**Three transports.** Stdio for local development, SSE for legacy streaming, and Streamable HTTP for production deployments with Bearer token authentication and health monitoring endpoints.

**Extensible middleware.** Custom middleware can be plugged in without modifying core code — useful for adding logging, audit trails, or custom auth in enterprise deployments.

**OAuth/OIDC authentication.** The server now supports enterprise identity providers including Azure Entra, Google, GitHub, and WorkOS via FastMCP authentication providers. Static bearer token authentication is also available for simpler setups.

### What Doesn't Work Well

**Only four tools.** Schema exploration is limited to listing databases and tables. No `describe_table` to inspect column types and metadata without writing a query. You need to write `DESCRIBE TABLE` SQL manually.

**No ClickHouse Cloud integration.** The server connects to any ClickHouse instance, but there's no dedicated integration with ClickHouse Cloud features like query history, cluster management, or billing.

## DuckDB / MotherDuck — Official Server

| Detail | Info |
|--------|------|
| [motherduckdb/mcp-server-motherduck](https://github.com/motherduckdb/mcp-server-motherduck) | 473 stars |
| Language | Python |
| License | MIT |
| Transport | stdio, HTTP, stateless-HTTP |
| Tools | 4 |
| Version | v1.0.5 (April 2026) |

The official DuckDB/MotherDuck MCP server bridges local analytics and cloud data warehousing. Now at v1.0.5 with 6 releases, four tools: `execute_query`, `list_databases`, `list_tables`, and `switch_database_connection` (requires `--allow-switch-databases` flag).

### What Works Well

**Universal data access.** Connect to local DuckDB files, in-memory databases, S3-hosted databases, and MotherDuck cloud — all from the same MCP server. The `switch_database_connection` tool lets AI agents move between data sources on the fly, which is uniquely powerful for cross-source analysis.

**Read-write with safety.** Read-only mode is the default. The `query_rw` tool enables write access when explicitly enabled, letting agents save derived tables and intermediate results — not just read from them.

**DuckDB's analytical power.** Because this wraps DuckDB, agents get access to DuckDB's ability to query Parquet, CSV, JSON, and Iceberg files directly. Combined with S3 access, an AI agent can analyze data lake files without any warehouse infrastructure.

**MotherDuck SaaS mode.** A restricted mode limits local filesystem access when connecting to MotherDuck cloud, providing appropriate security boundaries for cloud deployments. Read-only MotherDuck connections now require specialized read-scaling tokens rather than standard authentication.

**HTTP transport (NEW).** The server now supports HTTP-based transport with configurable host and port, plus a stateless-HTTP mode for compatibility with systems like AWS Bedrock AgentCore Runtime. This was the biggest gap in our initial review — now fixed.

### What Doesn't Work Well

**Simplified toolset.** The tool count went from 5 to 4 — `list_columns` was removed. Schema exploration now requires SQL queries to inspect column types and metadata.

## Snowflake — Official Snowflake Labs Server

| Detail | Info |
|--------|------|
| [Snowflake-Labs/mcp](https://github.com/Snowflake-Labs/mcp) | 277 stars |
| Language | Python |
| Transport | stdio, SSE, Streamable HTTP |

The official Snowflake MCP server from Snowflake Labs goes well beyond basic SQL access. It integrates Snowflake's Cortex AI capabilities — the AI features built into the Snowflake platform — making it one of the most feature-rich data warehouse MCP servers. Snowflake also offers a **managed MCP server** (GA since November 2025) that requires no local deployment — see below.

### Core Capabilities

**Cortex Analyst** — Query structured data through Snowflake's semantic modeling layer. Instead of writing raw SQL, agents can ask natural language questions that Cortex Analyst translates using your semantic model definitions.

**Cortex Search** — Query unstructured data stored in Snowflake, commonly used for RAG (Retrieval Augmented Generation) applications. This lets agents search document collections, knowledge bases, and text data indexed in Snowflake.

**Cortex Agent** — An agentic orchestrator that combines structured and unstructured data retrieval. This sits above Analyst and Search, routing queries to the appropriate backend.

**SQL Orchestration** — Direct SQL execution with permission controls. Object management operations for databases, schemas, tables, and views.

**Semantic Views** — Query and discover semantic views, Snowflake's abstraction layer that defines business-level metrics and relationships on top of raw tables.

### What Works Well

**AI-native integration.** No other data warehouse MCP server integrates this deeply with the platform's AI features. Cortex Analyst + Search + Agent means the MCP server isn't just a SQL pipe — it's a full AI-assisted data access layer.

**Three transports.** Stdio for local development, SSE for streaming, and Streamable HTTP for container deployments and remote servers. The HTTP transport enables team-wide shared MCP access.

**Enterprise-grade.** Snowflake's existing RBAC (role-based access control) applies to all MCP operations. Whatever permissions a user has in Snowflake, they have through MCP — no separate auth layer to configure. The server supports comprehensive authentication methods including username/password, key pair, OAuth, SSO, and MFA.

**Multi-client support.** The server now officially supports Claude Desktop, Cursor, VS Code + GitHub Copilot, fast-agent, and Codex, with Docker and Docker Compose deployment options.

### Snowflake Managed MCP Server (GA)

Snowflake also offers a **managed MCP server** that reached General Availability in November 2025. This is a separate, zero-deployment option that serves Cortex Analyst and Cortex Search as tools with RBAC enforcement. Unlike the open-source Snowflake-Labs/mcp server which you self-host, the managed server runs entirely within Snowflake's infrastructure — no local installation needed. For teams already using Cortex, the managed server is the simpler path.

### What Doesn't Work Well

**Complexity.** The Cortex features require Snowflake Cortex to be enabled and configured, which is an additional setup step. Teams not using Cortex get a basic SQL server.

**Snowflake-specific.** The Cortex and semantic view features are deeply tied to Snowflake's platform. There's no portability — you can't use these features with other warehouses.

### Snowflake Community Servers

| Server | Stars | Language | Tools | Focus |
|--------|-------|----------|-------|-------|
| [isaacwasserman/mcp-snowflake-server](https://github.com/isaacwasserman/mcp-snowflake-server) | 180 | Python | 8 | General SQL + insights |
| [dynamike/snowflake-mcp-server](https://github.com/dynamike/snowflake-mcp-server) | — | Python | — | Read-only queries |
| [davidamom/snowflake-mcp](https://github.com/davidamom/snowflake-mcp) | — | Python | — | General access |

**isaacwasserman/mcp-snowflake-server** (180 stars, Python, GPL-3.0) predates the official Snowflake Labs server and offers 8 tools across query, schema, and analysis operations. Its standout feature is an **insights memo** (`memo://insights`) that accumulates discovered data patterns as you explore — a running analytical notebook that grows with each interaction. Write protection is off by default with an `--allow-write` flag, and database/schema/table exclusion filters prevent access to sensitive data.

For most users, the **official Snowflake-Labs/mcp server is the better choice** now, especially if you use Cortex. The community server remains useful for simpler setups or if you want the insights memo feature.

## Google BigQuery — Managed Remote Server

| Detail | Info |
|--------|------|
| Endpoint | `bigquery.googleapis.com/mcp` |
| Transport | HTTPS (Streamable HTTP) |
| Auth | OAuth 2.0 + IAM |
| Status | Auto-enabled (since March 17, 2026) |
| Tools | 6 (`list_dataset_ids`, `list_table_ids`, `get_dataset_info`, `get_table_info`, `execute_sql`, `execute_sql_readonly`) |

Google took the most aggressive approach in the data warehouse MCP space: a **fully managed, remote MCP server** that requires zero local installation. Point your MCP client at `bigquery.googleapis.com/mcp`, authenticate with OAuth 2.0, and you're connected to your BigQuery datasets.

### What Works Well

**Zero setup.** No local server to install, configure, or maintain. The BigQuery MCP server is automatically enabled when you enable BigQuery — it's just another endpoint on the service.

**Full governance.** IAM permissions are enforced end-to-end. Agents can only access datasets and tables that the authenticated user has permission to see. This is the same security model that governs all BigQuery access.

**Enterprise features.** The managed server includes access to BigQuery features like ML forecasting, materialized views, and cost controls. The 1GB query processing limit provides guardrails against expensive accidental queries.

**Global availability.** A single HTTPS endpoint works from anywhere — no region-specific configuration needed for the MCP server itself (BigQuery datasets still live in regions).

**Specific tools documented.** The server provides six tools: `list_dataset_ids`, `list_table_ids`, `get_dataset_info`, and `get_table_info` for metadata exploration, plus `execute_sql` (read-write) and `execute_sql_readonly` for query execution. The read-only tool blocks DML, DDL, and Python UDFs.

### What Doesn't Work Well

**Query constraints.** Queries are limited to 3 minutes (auto-cancelled after) and results are capped at 3,000 rows. For large analytical workloads, these limits can be restrictive.

**No Google Drive external tables.** The MCP server doesn't support querying BigQuery external tables backed by Google Drive data sources.

**Vendor lock-in.** This is a Google-hosted service — there's no open-source alternative that exactly replicates the managed remote experience.

### BigQuery Community Servers

| Server | Stars | Language | Tools | Focus |
|--------|-------|----------|-------|-------|
| [ergut/mcp-bigquery-server](https://github.com/ergut/mcp-bigquery-server) | 133 | JavaScript | — | Read-only, secure access |
| [LucasHild/mcp-server-bigquery](https://github.com/LucasHild/mcp-server-bigquery) | 123 | Python | 3 | Schema + query |
| [pvoo/bigquery-mcp](https://github.com/pvoo/bigquery-mcp) | — | Python | — | Large datasets, vector search |
| [aicayzer/bigquery-mcp](https://github.com/aicayzer/bigquery-mcp) | — | Python | — | Multi-project, Docker |

The community servers predate the managed remote server and remain useful for teams wanting local control, custom tooling, or self-hosted deployments. **ergut/mcp-bigquery-server** (133 stars, JavaScript, MIT) offers read-only access with materialized view support. **LucasHild/mcp-server-bigquery** (123 stars, Python, MIT) provides the simplest three-tool interface. **pvoo/bigquery-mcp** is optimized for large datasets with vector search support, keeping LLM context small.

For most users, the **managed remote server is now the recommended path** — it's simpler, more secure, and maintained by Google. Use community servers if you need offline access, custom tools, or want to avoid the managed service.

## Databricks — Managed MCP with Unity Catalog

| Detail | Info |
|--------|------|
| Platform | Managed MCP (Public Preview) |
| Auth | On-behalf-of-user + Unity Catalog + Unity AI Gateway |
| Servers | Genie, Vector Search, Databricks SQL (NEW), UC Functions |

Databricks takes a governance-first approach to MCP. Instead of a single SQL server, Databricks provides **four managed MCP servers** that are tightly integrated with Unity Catalog permissions. The addition of a direct SQL execution server in 2026 fills what was previously the biggest gap.

### Available Managed Servers

**Databricks SQL (NEW)** — Run AI-generated SQL for data pipelines with coding tools. This is the most significant addition since our initial review — direct SQL execution via managed MCP, with read and write access. Long-running queries use a polling mechanism.

**Genie** — Access structured data through Databricks' natural language interface. Genie translates questions into SQL using your data's metadata and descriptions, similar to Snowflake's Cortex Analyst.

**Vector Search** — Access unstructured data through Databricks Vector Search indexes. Useful for RAG applications and semantic search over document collections. Requires Databricks managed embeddings.

**UC Functions** — Build deterministic functions in Unity Catalog and expose them as MCP tools. This lets teams create custom, governed tools for specific business logic — billing calculations, compliance checks, data transformations.

### What Works Well

**Governance by default.** Unity Catalog permissions are always enforced. Agents and users can only access tools and data they're authorized for. There's no separate MCP-level auth to configure — if Unity Catalog says no, MCP says no.

**On-behalf-of-user auth.** MCP requests run with the authenticated user's identity, not a service account. This means audit logs correctly attribute every query to the person (or agent) who made it.

**Unity AI Gateway (NEW).** AI Gateway is now part of Unity Catalog as Unity AI Gateway, extending Unity Catalog's governance model to agentic AI. It enforces access control, monitors usage, and audits activity across all MCP interactions — fine-grained permissions, end-to-end observability, and cost attribution across models, teams, and workflows.

**Managed OAuth for external MCP servers (NEW).** Databricks now provides managed OAuth flows for select external MCP servers (Glean, GitHub, Google Drive, SharePoint), eliminating the need to register your own OAuth app or manage credentials.

**Extensibility.** UC Functions let you build custom MCP tools that are governed alongside your data. This is more powerful than raw SQL access — you can expose business logic as callable tools.

### What Doesn't Work Well

**Public Preview.** Managed MCP servers are still in Public Preview, not GA. Feature set and APIs may change.

**No open-source server.** The managed MCP servers are a Databricks platform feature, not an open-source project you can self-host.

### Databricks Community Servers

| Server | Stars | Language | Tools | Focus |
|--------|-------|----------|-------|-------|
| [JustTryAI/databricks-mcp-server](https://github.com/JustTryAI/databricks-mcp-server) | 46 | Python | 11 | Clusters, jobs, notebooks, SQL |
| [RafaelCartenet/mcp-databricks-server](https://github.com/RafaelCartenet/mcp-databricks-server) | 36 | Python | 5 | Unity Catalog, lineage |

**JustTryAI/databricks-mcp-server** (46 stars, Python, MIT) is the most comprehensive community server with 11 tools spanning cluster management, job execution, notebook operations, filesystem access, and SQL execution. Useful for teams wanting infrastructure management alongside data access.

**RafaelCartenet/mcp-databricks-server** (36 stars, Python, MIT) focuses specifically on Unity Catalog metadata — catalog/schema/table discovery, SQL execution, and data lineage analysis including notebook and job dependencies. Its ability to trace data flows from ingestion through transformation pipelines is unique.

## Amazon Redshift — AWS MCP Suite

| Detail | Info |
|--------|------|
| [awslabs/mcp (Redshift server)](https://github.com/awslabs/mcp/tree/main/src/redshift-mcp-server) | Part of AWS MCP suite (8,900+ stars) |
| Language | Python |
| Transport | stdio |

Amazon Redshift's MCP server lives within the AWS MCP monorepo (`awslabs/mcp`), the same suite that includes servers for S3, Lambda, CloudFormation, and other AWS services.

### Core Capabilities

**Cluster discovery** — Automatically discover both provisioned Redshift clusters and serverless workgroups. No manual endpoint configuration needed.

**Metadata exploration** — Browse databases, schemas, tables, and columns through MCP tools.

**Safe query execution** — Read-only mode by default. Write support is planned but not yet available.

**Query plan analysis (NEW)** — A `describe_execution_plan` tool uses Redshift's EXPLAIN VERBOSE to show how a query would execute, providing performance insights without running the query.

### What Works Well

**AWS ecosystem integration.** Being part of the AWS MCP suite means Redshift works alongside S3, Lambda, and other AWS MCP servers. An AI agent can query Redshift data and then process it through Lambda or store results in S3 — all through MCP.

**Auto-discovery.** The server finds your Redshift clusters and serverless workgroups automatically using your AWS credentials. No hardcoded connection strings.

### What Doesn't Work Well

**Read-only for now.** No write operations yet, which limits use cases like creating derived tables or materializing query results.

**Monorepo distribution.** The Redshift server is bundled with 14+ other AWS MCP servers. You install the full suite to get Redshift — there's no standalone package.

## Apache Doris — Official Server (NEW)

| Detail | Info |
|--------|------|
| [apache/doris-mcp-server](https://github.com/apache/doris-mcp-server) | 289 stars |
| Language | Python |
| License | Apache 2.0 |
| Version | v0.6.0 |
| Tools | 25+ |

Apache Doris, the real-time analytical database with over 12,000 GitHub stars, now has an official MCP server — and it's one of the most feature-rich in the data warehouse category. With 25+ tools spanning query execution, schema discovery, monitoring, data quality analysis, and lineage tracking, it offers far more tooling than ClickHouse or DuckDB.

### What Works Well

**Comprehensive tooling.** 25+ MCP tools across query execution (`exec_query`), schema and metadata (`get_table_schema`, `get_db_table_list`), query analysis (`get_sql_explain`, `get_sql_profile`), monitoring metrics, data quality analysis, lineage tracking, freshness monitoring, and access pattern analysis. This is the most tool-rich data warehouse MCP server.

**Enterprise authentication.** Token, JWT, and OAuth support with a web-based token management dashboard. This is more auth flexibility than most data warehouse MCP servers offer.

**Arrow Flight SQL integration.** ADBC/Arrow Flight SQL support provides 3-10x performance improvements for large dataset transfers — a genuine differentiator for analytical workloads where data volume matters.

**Multi-catalog federation.** Support for querying across multiple catalogs, useful for organizations with data spread across several Doris deployments.

### What Doesn't Work Well

**Requires Python 3.12+.** The minimum Python version is higher than most MCP servers (typically 3.10 or 3.11), which may cause compatibility issues in some environments.

**Security advisory.** Versions earlier than 0.6.1 had a query context handling vulnerability (CVE-2025-66335). Users should ensure they're on 0.6.1 or later.

## Dremio — Official Server (NEW)

| Detail | Info |
|--------|------|
| [dremio/dremio-mcp](https://github.com/dremio/dremio-mcp) | 49 stars |
| Language | Python |
| License | Apache 2.0 |
| Version | 0.1.0 |

Dremio, the lakehouse analytics platform, now has an official MCP server enabling AI agents to explore, query, and analyze data across Dremio deployments using natural language.

### What Works Well

**Two operating modes.** FOR_DATA_PATTERNS mode enables data exploration, natural language to SQL, and view creation. FOR_SELF mode performs system introspection and performance analysis. This dual-mode design lets teams use the same server for both data work and platform monitoring.

**Production deployment options.** The server supports both local development and remote Kubernetes deployment with a Helm chart. The Kubernetes setup includes OAuth authentication, Prometheus metrics, horizontal pod autoscaling, and security hardening (non-root execution, read-only filesystem).

**Lakehouse integration.** Dremio sits on top of data lakes (Iceberg, Delta Lake, Parquet), meaning this MCP server gives AI agents access to lakehouse data without requiring a traditional warehouse. For teams using Dremio as their query engine, this is a direct path to AI-enabled analytics.

### What Doesn't Work Well

**Early stage.** At v0.1.0 and 49 stars, this is still early in development compared to ClickHouse (764 stars) or Apache Doris (289 stars). Feature set and stability will evolve.

**Not official Dremio product support.** The repository notes this is open source software and not part of official Dremio product support.

## The big picture

### Adoption comparison

| Platform | MCP Server(s) | Stars | Official? | Tools | Strength |
|----------|---------------|-------|-----------|-------|----------|
| ClickHouse | ClickHouse/mcp-clickhouse | 764 | Yes | 4 | Dual engine, OAuth/OIDC |
| DuckDB/MotherDuck | motherduckdb/mcp-server-motherduck | 473 | Yes | 4 | Universal data access, HTTP |
| Apache Doris | apache/doris-mcp-server | 289 | Yes | 25+ | Most tools, Arrow Flight SQL |
| Snowflake | Snowflake-Labs/mcp + managed (GA) | 277 | Yes | Multiple | Cortex AI, managed option |
| BigQuery | Managed remote (auto-enabled) | — | Yes | 6 | Zero-setup managed |
| Databricks | 4 Managed MCP servers | — | Yes | Multiple | Unity AI Gateway governance |
| Dremio | dremio/dremio-mcp | 49 | Yes | Multiple | Lakehouse analytics |
| Redshift | awslabs/mcp suite | 8,900+ | Yes | Multiple | AWS ecosystem |

### What's working

**Universal vendor backing.** Every major data warehouse vendor has official MCP support — Snowflake, ClickHouse, MotherDuck, Google Cloud, Databricks, AWS, Apache Doris, and Dremio. The addition of Doris (289 stars) and Dremio (49 stars) since our initial review makes this the broadest official coverage of any MCP category.

**Safety-first defaults.** Read-only mode is the default across nearly every server. Write operations require explicit opt-in. This is exactly right for connecting AI agents to production data warehouses where a bad query could be costly.

**Managed remote servers maturing.** BigQuery's managed MCP server is now auto-enabled (no longer preview). Snowflake's managed MCP server reached GA in November 2025. Databricks expanded to 4 managed servers with SQL execution. The trend toward zero-setup, governed, cloud-native MCP access is accelerating.

**Cortex and Genie.** Snowflake and Databricks aren't just exposing SQL — they're exposing their AI-native query layers (Cortex Analyst, Genie). This lets agents query data through semantic models rather than raw SQL, which is safer and more accessible.

### What's missing

**No cross-warehouse query server.** You can't query Snowflake and BigQuery from the same MCP server. Each platform requires its own server with its own configuration. DuckDB partially bridges this gap by reading from multiple sources, but it's not the same as federated querying.

**No cost monitoring.** None of the servers expose query cost estimation or billing information. For cloud warehouses where queries can be expensive, cost-awareness is a critical missing feature.

**No data quality or profiling.** No server provides built-in data profiling, quality checks, or anomaly detection. Agents can run SQL to check data, but there's no structured tooling for it.

**No dbt integration.** Despite dbt's dominance in data transformation, no data warehouse MCP server integrates with dbt models, tests, or documentation. Agents can't see your dbt DAG or run dbt commands through these servers. (Note: separate dbt-specific MCP servers exist — see our [dbt MCP servers review](/reviews/dbt-mcp-servers/) — but they're not integrated into the warehouse servers themselves.)

## The bottom line

**For ClickHouse users:** The **official ClickHouse/mcp-clickhouse server** (764 stars) is well-designed with dual engine support, strong safety defaults, three transport options, and now OAuth/OIDC enterprise auth. Start here.

**For DuckDB / local analytics:** **motherduckdb/mcp-server-motherduck** (473 stars, v1.0.5) is excellent — universal data access across local files, S3, and cloud, now with HTTP transport for remote deployment. The best option for cross-source analytical work.

**For Apache Doris users:** The **official apache/doris-mcp-server** (289 stars, v0.6.0) is the most tool-rich data warehouse MCP server with 25+ tools, Arrow Flight SQL for performance, and enterprise auth. A strong newcomer.

**For Snowflake users:** Choose between the **managed MCP server** (GA, zero-deployment) for simplicity or the **open-source Snowflake-Labs/mcp server** (277 stars) for self-hosted flexibility. Both integrate Cortex AI features. The community server (isaacwasserman, ~180 stars) is a simpler alternative with a useful insights memo.

**For BigQuery users:** The **managed remote server** at `bigquery.googleapis.com/mcp` is the easiest path — auto-enabled, full governance, 6 tools. Community servers remain useful for offline or custom needs.

**For Databricks users:** **Managed MCP** with Unity AI Gateway governance is the recommended approach, now with 4 servers including direct SQL execution. Still in Public Preview. Community servers fill the gap for infrastructure management and lineage analysis.

**For Dremio users:** The **official dremio/dremio-mcp server** (49 stars) provides lakehouse analytics with Kubernetes deployment support. Early stage but functional with dual operating modes.

**For Redshift users:** The **AWS MCP suite** (8,900+ stars) provides auto-discovery, safe querying, and now query plan analysis. Read-only for now, but well-integrated with the broader AWS MCP ecosystem.

**Rating: 4.5/5** — Data warehousing remains one of the strongest MCP categories and got even stronger since our initial review. Eight vendors now have official MCP support (up from six). Managed servers are maturing — BigQuery auto-enabled, Snowflake managed GA, Databricks added SQL execution. Apache Doris brought the most comprehensive tooling (25+ tools). DuckDB fixed its HTTP transport gap. The missing cross-warehouse federation, cost monitoring, and dbt integration prevent a perfect score, but the fundamentals are exceptional. If you work with data warehouses, the MCP tools are production-ready.

*This review was refreshed on 2026-04-29 using Claude Opus 4.6 (Anthropic). Initial review: 2026-03-17.*

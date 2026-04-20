# Data Warehouse & Lakehouse MCP Servers — Snowflake, BigQuery, Databricks, ClickHouse, DuckDB, Redshift, and More

> Data warehouse and lakehouse MCP servers reviewed: Snowflake Labs official (256 stars, Python, Cortex AI + SQL + semantic views), ClickHouse official (720 stars, Python, dual


Data warehousing and lakehouse platforms have some of the best MCP coverage in the entire ecosystem. Every major vendor — Snowflake, Google BigQuery, Databricks, ClickHouse, MotherDuck/DuckDB, and Amazon Redshift — now offers official or vendor-backed MCP servers. This makes sense: data warehouses are where enterprise data lives, and connecting AI agents to structured data through SQL is one of the highest-value MCP use cases.

The landscape divides into three tiers: **cloud-native warehouses** (Snowflake, BigQuery, Redshift) with managed remote MCP servers, **lakehouse platforms** (Databricks) with governance-first MCP integration, and **analytical engines** (ClickHouse, DuckDB) with open-source community-driven servers. Most teams use at least one from the first two tiers, and DuckDB increasingly bridges them all. Part of our **[Data & Analytics](/categories/data-analytics/)** category.

## ClickHouse — Official Server

| Detail | Info |
|--------|------|
| [ClickHouse/mcp-clickhouse](https://github.com/ClickHouse/mcp-clickhouse) | 720 stars |
| Language | Python |
| Transport | stdio, SSE, Streamable HTTP |
| Tools | 4 |

The official ClickHouse MCP server is the most starred data warehouse MCP server in the open-source community. It provides four tools: `run_query` (execute SQL), `list_databases`, `list_tables` (with pagination), and `run_chdb_select_query` (embedded ClickHouse engine).

### What Works Well

**Dual engine support.** The server works with both remote ClickHouse clusters and [chDB](https://clickhouse.com/docs/chdb), the embedded ClickHouse engine. This means you can query production data remotely or run local analytical queries without a server — same MCP interface for both.

**Safety defaults.** Read-only mode is on by default. Write access requires `--allow-write`, and destructive operations (DROP, TRUNCATE) require a separate `--allow-destructive` flag. This two-tier safety model is well-designed for connecting AI agents to production warehouses.

**Three transports.** Stdio for local development, SSE for legacy streaming, and Streamable HTTP for production deployments with Bearer token authentication and health monitoring endpoints.

**Extensible middleware.** Custom middleware can be plugged in without modifying core code — useful for adding logging, audit trails, or custom auth in enterprise deployments.

### What Doesn't Work Well

**Only four tools.** Schema exploration is limited to listing databases and tables. No `describe_table` to inspect column types and metadata without writing a query. You need to write `DESCRIBE TABLE` SQL manually.

**No ClickHouse Cloud integration.** The server connects to any ClickHouse instance, but there's no dedicated integration with ClickHouse Cloud features like query history, cluster management, or billing.

## DuckDB / MotherDuck — Official Server

| Detail | Info |
|--------|------|
| [motherduckdb/mcp-server-motherduck](https://github.com/motherduckdb/mcp-server-motherduck) | 441 stars |
| Language | Python |
| License | MIT |
| Transport | stdio |
| Tools | 5 |

The official DuckDB/MotherDuck MCP server bridges local analytics and cloud data warehousing. Five tools: `execute_query`, `list_databases`, `list_tables`, `list_columns`, and `switch_database_connection`.

### What Works Well

**Universal data access.** Connect to local DuckDB files, in-memory databases, S3-hosted databases, and MotherDuck cloud — all from the same MCP server. The `switch_database_connection` tool lets AI agents move between data sources on the fly, which is uniquely powerful for cross-source analysis.

**Read-write with safety.** Read-only mode is the default. The `query_rw` tool enables write access when explicitly enabled, letting agents save derived tables and intermediate results — not just read from them.

**DuckDB's analytical power.** Because this wraps DuckDB, agents get access to DuckDB's ability to query Parquet, CSV, JSON, and Iceberg files directly. Combined with S3 access, an AI agent can analyze data lake files without any warehouse infrastructure.

**MotherDuck SaaS mode.** A restricted mode limits local filesystem access when connecting to MotherDuck cloud, providing appropriate security boundaries for cloud deployments.

### What Doesn't Work Well

**No schema descriptions.** `list_columns` shows column names and types, but there's no metadata about column descriptions, constraints, or relationships. For large warehouses, agents need more context than bare schemas.

**Stdio only.** No HTTP transport means no remote deployment or multi-client access. For teams wanting a shared MCP server, this is limiting.

## Snowflake — Official Snowflake Labs Server

| Detail | Info |
|--------|------|
| [Snowflake-Labs/mcp](https://github.com/Snowflake-Labs/mcp) | 256 stars |
| Language | Python |
| Transport | stdio, SSE, Streamable HTTP |

The official Snowflake MCP server from Snowflake Labs goes well beyond basic SQL access. It integrates Snowflake's Cortex AI capabilities — the AI features built into the Snowflake platform — making it one of the most feature-rich data warehouse MCP servers.

### Core Capabilities

**Cortex Analyst** — Query structured data through Snowflake's semantic modeling layer. Instead of writing raw SQL, agents can ask natural language questions that Cortex Analyst translates using your semantic model definitions.

**Cortex Search** — Query unstructured data stored in Snowflake, commonly used for RAG (Retrieval Augmented Generation) applications. This lets agents search document collections, knowledge bases, and text data indexed in Snowflake.

**Cortex Agent** — An agentic orchestrator that combines structured and unstructured data retrieval. This sits above Analyst and Search, routing queries to the appropriate backend.

**SQL Orchestration** — Direct SQL execution with permission controls. Object management operations for databases, schemas, tables, and views.

**Semantic Views** — Query and discover semantic views, Snowflake's abstraction layer that defines business-level metrics and relationships on top of raw tables.

### What Works Well

**AI-native integration.** No other data warehouse MCP server integrates this deeply with the platform's AI features. Cortex Analyst + Search + Agent means the MCP server isn't just a SQL pipe — it's a full AI-assisted data access layer.

**Three transports.** Stdio for local development, SSE for streaming, and Streamable HTTP for container deployments and remote servers. The HTTP transport enables team-wide shared MCP access.

**Enterprise-grade.** Snowflake's existing RBAC (role-based access control) applies to all MCP operations. Whatever permissions a user has in Snowflake, they have through MCP — no separate auth layer to configure.

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
| Status | Preview (auto-enabled after March 17, 2026) |

Google took the most aggressive approach in the data warehouse MCP space: a **fully managed, remote MCP server** that requires zero local installation. Point your MCP client at `bigquery.googleapis.com/mcp`, authenticate with OAuth 2.0, and you're connected to your BigQuery datasets.

### What Works Well

**Zero setup.** No local server to install, configure, or maintain. The BigQuery MCP server is automatically enabled when you enable BigQuery — it's just another endpoint on the service.

**Full governance.** IAM permissions are enforced end-to-end. Agents can only access datasets and tables that the authenticated user has permission to see. This is the same security model that governs all BigQuery access.

**Enterprise features.** The managed server includes access to BigQuery features like ML forecasting, materialized views, and cost controls. The 1GB query processing limit provides guardrails against expensive accidental queries.

**Global availability.** A single HTTPS endpoint works from anywhere — no region-specific configuration needed for the MCP server itself (BigQuery datasets still live in regions).

### What Doesn't Work Well

**Preview status.** The managed remote server is still in preview. APIs and behavior may change.

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
| Platform | Managed MCP (Beta) |
| Auth | On-behalf-of-user + Unity Catalog |
| Servers | Genie, Vector Search, UC Functions |

Databricks takes a governance-first approach to MCP. Instead of a single SQL server, Databricks provides **managed MCP servers** that are tightly integrated with Unity Catalog permissions.

### Available Managed Servers

**Genie** — Access structured data through Databricks' natural language interface. Genie translates questions into SQL using your data's metadata and descriptions, similar to Snowflake's Cortex Analyst.

**Vector Search** — Access unstructured data through Databricks Vector Search indexes. Useful for RAG applications and semantic search over document collections.

**UC Functions** — Build deterministic functions in Unity Catalog and expose them as MCP tools. This lets teams create custom, governed tools for specific business logic — billing calculations, compliance checks, data transformations.

### What Works Well

**Governance by default.** Unity Catalog permissions are always enforced. Agents and users can only access tools and data they're authorized for. There's no separate MCP-level auth to configure — if Unity Catalog says no, MCP says no.

**On-behalf-of-user auth.** MCP requests run with the authenticated user's identity, not a service account. This means audit logs correctly attribute every query to the person (or agent) who made it.

**Extensibility.** UC Functions let you build custom MCP tools that are governed alongside your data. This is more powerful than raw SQL access — you can expose business logic as callable tools.

### What Doesn't Work Well

**Beta status.** Managed MCP servers are in beta. Feature set is limited to Genie, Vector Search, and UC Functions — no direct SQL execution via managed MCP yet (planned for future with DBSQL support).

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
| [awslabs/mcp (Redshift server)](https://github.com/awslabs/mcp/tree/main/src/redshift-mcp-server) | Part of AWS MCP suite (8,500+ stars) |
| Language | Python |
| Transport | stdio |

Amazon Redshift's MCP server lives within the AWS MCP monorepo (`awslabs/mcp`), the same suite that includes servers for S3, Lambda, CloudFormation, and other AWS services.

### Core Capabilities

**Cluster discovery** — Automatically discover both provisioned Redshift clusters and serverless workgroups. No manual endpoint configuration needed.

**Metadata exploration** — Browse databases, schemas, tables, and columns through MCP tools.

**Safe query execution** — Read-only mode by default. Write support is planned but not yet available.

### What Works Well

**AWS ecosystem integration.** Being part of the AWS MCP suite means Redshift works alongside S3, Lambda, and other AWS MCP servers. An AI agent can query Redshift data and then process it through Lambda or store results in S3 — all through MCP.

**Auto-discovery.** The server finds your Redshift clusters and serverless workgroups automatically using your AWS credentials. No hardcoded connection strings.

### What Doesn't Work Well

**Read-only for now.** No write operations yet, which limits use cases like creating derived tables or materializing query results.

**Monorepo distribution.** The Redshift server is bundled with 14+ other AWS MCP servers. You install the full suite to get Redshift — there's no standalone package.

## The big picture

### Adoption comparison

| Platform | MCP Server(s) | Stars | Official? | Tools | Strength |
|----------|---------------|-------|-----------|-------|----------|
| ClickHouse | ClickHouse/mcp-clickhouse | 720 | Yes | 4 | Dual engine, safety defaults |
| DuckDB/MotherDuck | motherduckdb/mcp-server-motherduck | 441 | Yes | 5 | Universal data access |
| Snowflake | Snowflake-Labs/mcp | 256 | Yes | Multiple | Cortex AI integration |
| BigQuery | Managed remote | — | Yes | Multiple | Zero-setup managed |
| Databricks | Managed MCP | — | Yes | Multiple | Unity Catalog governance |
| Redshift | awslabs/mcp suite | 8,500+ | Yes | Multiple | AWS ecosystem |

### What's working

**Universal vendor backing.** Every major data warehouse vendor has official MCP support — Snowflake Labs, ClickHouse Inc, MotherDuck, Google Cloud, Databricks, and AWS. This is rare across MCP categories. It reflects the high value of connecting AI to enterprise data.

**Safety-first defaults.** Read-only mode is the default across nearly every server. Write operations require explicit opt-in. This is exactly right for connecting AI agents to production data warehouses where a bad query could be costly.

**Managed remote servers.** BigQuery's managed remote MCP server and Databricks' managed MCP represent the future of the category — zero-setup, governed, cloud-native MCP access. Snowflake's Streamable HTTP transport also supports remote deployment.

**Cortex and Genie.** Snowflake and Databricks aren't just exposing SQL — they're exposing their AI-native query layers (Cortex Analyst, Genie). This lets agents query data through semantic models rather than raw SQL, which is safer and more accessible.

### What's missing

**No cross-warehouse query server.** You can't query Snowflake and BigQuery from the same MCP server. Each platform requires its own server with its own configuration. DuckDB partially bridges this gap by reading from multiple sources, but it's not the same as federated querying.

**No cost monitoring.** None of the servers expose query cost estimation or billing information. For cloud warehouses where queries can be expensive, cost-awareness is a critical missing feature.

**No data quality or profiling.** No server provides built-in data profiling, quality checks, or anomaly detection. Agents can run SQL to check data, but there's no structured tooling for it.

**No dbt integration.** Despite dbt's dominance in data transformation, no data warehouse MCP server integrates with dbt models, tests, or documentation. Agents can't see your dbt DAG or run dbt commands through these servers.

## The bottom line

**For ClickHouse users:** The **official ClickHouse/mcp-clickhouse server** (720 stars) is well-designed with dual engine support, strong safety defaults, and three transport options. Start here.

**For DuckDB / local analytics:** **motherduckdb/mcp-server-motherduck** (441 stars) is excellent — universal data access across local files, S3, and cloud. The best option for cross-source analytical work.

**For Snowflake users:** The **official Snowflake-Labs/mcp server** (256 stars) is the strongest choice, especially if you use Cortex AI features. The community server (isaacwasserman, 180 stars) is a simpler alternative with a useful insights memo.

**For BigQuery users:** The **managed remote server** at `bigquery.googleapis.com/mcp` is the easiest path — zero setup, full governance, auto-enabled. Community servers remain useful for offline or custom needs.

**For Databricks users:** **Managed MCP** with Unity Catalog governance is the recommended approach, though still in beta. Community servers fill the gap for infrastructure management and lineage analysis.

**For Redshift users:** The **AWS MCP suite** provides auto-discovery and safe querying. Read-only for now, but well-integrated with the broader AWS MCP ecosystem.

**Rating: 4.5/5** — Data warehousing is one of the strongest MCP categories. Universal vendor backing, safety-first defaults, managed remote servers from BigQuery and Databricks, and deep AI integration from Snowflake's Cortex set a high bar. The missing cross-warehouse federation, cost monitoring, and dbt integration prevent a perfect score, but the fundamentals are exceptional. If you work with data warehouses, the MCP tools are production-ready.

*This review was last edited on 2026-03-17 using Claude Opus 4.6 (Anthropic).*


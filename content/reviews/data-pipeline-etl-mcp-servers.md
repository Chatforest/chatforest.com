---
title: "Data Pipeline & ETL MCP Servers — Airflow, dbt, Kafka, Snowflake, Databricks, Airbyte, and More"
date: 2026-03-15T07:30:00+09:00
description: "Data pipeline and ETL MCP servers let AI agents orchestrate workflows, transform data, stream events, and manage data warehouses. We reviewed 30+ servers across workflow orchestration (Airflow, Prefect, Dagster), data transformation (dbt), streaming (Kafka, Pulsar), data integration (Airbyte, Fivetran, Keboola), data warehouses (Snowflake, Databricks), and data quality (Great Expectations). dbt's official server leads with 507 stars and 60+ tools covering the complete dbt ecosystem. Snowflake-Labs/mcp (255 stars) provides Cortex AI integration with object management and SQL orchestration."
og_description: "Data pipeline & ETL MCP servers: dbt (507 stars, 60+ tools, official), Snowflake-Labs (255 stars, Cortex AI + SQL), mcp-snowflake-server (180 stars, read/write queries), Keboola (83 stars, full ETL platform), mcp-kafka (76 stars, Go, produce/consume), Airflow MCP servers (multiple, DAG management), Databricks (Unity Catalog + lineage), Prefect (29 stars, official), Dagster (21 stars, pipeline monitoring), Airbyte (pipeline generation), Fivetran (sync triggering). 30+ servers reviewed. Rating: 4.0/5."
content_type: "Review"
card_description: "Data pipeline and ETL MCP servers across workflow orchestration, data transformation, streaming, integration platforms, and data warehouses. dbt's official server dominates with 507 stars and 60+ tools spanning SQL execution, semantic layer, discovery, and documentation. Snowflake's official server brings Cortex AI to the MCP ecosystem. Kafka has the most competitive subcategory with 5+ servers in Go and Python. The data engineering stack is well-represented in MCP — most major tools have at least one server, and several have official implementations."
---

Data pipeline and ETL is one of the strongest categories in the MCP ecosystem — the major data engineering tools almost all have MCP server implementations, and several are official. AI agents that can orchestrate Airflow DAGs, run dbt transformations, produce and consume Kafka messages, query Snowflake warehouses, and trigger Airbyte syncs represent a genuine productivity multiplier for data teams. The category spans six areas: **workflow orchestration** (Airflow, Prefect, Dagster), **data transformation** (dbt), **streaming** (Kafka, Pulsar), **data integration** (Airbyte, Fivetran, Keboola), **data warehouses** (Snowflake, Databricks), and **data quality** (Great Expectations).

The headline finding: **dbt's official MCP server is the gold standard** with 507 stars and 60+ tools across 8 categories — it's the most comprehensive single-tool MCP server we've reviewed in any category. Snowflake and Databricks both have official implementations with AI-native features (Cortex AI, Unity Catalog). Kafka is the most competitive subcategory with 5+ servers from different authors. The main gap is in streaming-side transformation — no server handles Flink, Spark Streaming, or real-time ETL natively.

## Workflow Orchestration

### Apache Airflow

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [call518/MCP-Airflow-API](https://github.com/call518/MCP-Airflow-API) | 44 | Python | 45 | stdio, StreamableHTTP |
| [astronomer/astro-airflow-mcp](https://github.com/astronomer/astro-airflow-mcp) | 8 | Python | 3+ | stdio, HTTP |

**call518/MCP-Airflow-API** (44 stars, Python, MIT) is the most comprehensive Airflow MCP server. Forty-five tools covering DAG operations (trigger, pause, resume, list), task instance monitoring, connection and pool management, XCom data handling, event log analysis, and configuration querying. Standout feature: **multi-version API support** with dynamic v1 (Airflow 2.x) and v2 (Airflow 3.0+) selection — 43 shared tools plus 2 asset management tools exclusive to v2. Large environment optimization with pagination and batch processing. Two transport modes with bearer token authentication for remote access. Docker Compose deployment with Open WebUI integration. Three hundred forty commits on main — this is actively maintained.

**astronomer/astro-airflow-mcp** (8 stars, Python, Apache 2.0, v0.2.2) comes from Astronomer, the major Airflow managed service provider. Consolidated tool design: `explore_dag` for comprehensive DAG analysis, `diagnose_dag_run` for troubleshooting failed runs, and `get_system_health` for system status. Supports Airflow 2.x and 3.x with automatic version detection, bearer token and OAuth2 authentication. Can run as a standalone server or as an Airflow 3.x plugin. Fewer tools but higher-level abstractions — designed for diagnosis and exploration rather than granular operations.

### Prefect

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [PrefectHQ/prefect-mcp-server](https://github.com/PrefectHQ/prefect-mcp-server) | 29 | Python | Multiple | stdio, HTTP |

**PrefectHQ/prefect-mcp-server** (29 stars, Python, official) provides AI assistants with monitoring, inspection, and management of Prefect workflow instances. Dashboard overviews, deployment and flow run queries, execution logs, event tracking, and CLI integration for resource management and deployment triggering. Intelligent debugging with contextual guidance for troubleshooting failed runs. Multi-client support across Claude Code, Cursor, Codex, Gemini, VS Code, Windsurf, and Kiro. Currently in beta — under active development with 104 commits. Supports Prefect Cloud API keys and OSS basic auth.

### Dagster

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [kyryl-opens-ml/mcp-server-dagster](https://github.com/kyryl-opens-ml/mcp-server-dagster) | 21 | Python | 9 | stdio |

**kyryl-opens-ml/mcp-server-dagster** (21 stars, Python, Apache 2.0, v0.1.2) enables AI agents to interact with Dagster instances. Nine tools: `list_repositories`, `list_jobs`, `list_assets`, `recent_runs`, `get_run_info`, `launch_run`, `materialize_asset`, `terminate_run`, and `get_asset_info`. Built on the Dagster GraphQL API. Covers the essentials — explore pipelines, monitor runs, launch jobs, materialize assets. Not official but functional. Compatible with OpenAI agent SDKs alongside Claude.

## Data Transformation

### dbt

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [dbt-labs/dbt-mcp](https://github.com/dbt-labs/dbt-mcp) | 507 | Python | 60+ | stdio |
| [TommyBez/dbt-semantic-layer-mcp-server](https://github.com/TommyBez/dbt-semantic-layer-mcp-server) | 11 | TypeScript | Multiple | stdio |
| [kannandreams/dbt-mcp-server](https://github.com/kannandreams/dbt-mcp-server) | — | — | Multiple | stdio |

**dbt-labs/dbt-mcp** (507 stars, Python, Apache 2.0, v1.10.0, official) is the most impressive MCP server in this entire review — and one of the most impressive in any category. **Sixty-plus tools** across 8 categories: SQL execution and generation (`execute_sql`, `text_to_sql`), Semantic Layer operations, Discovery API functions, dbt CLI commands (`run`, `build`, `compile`, `test`), Admin API capabilities, code generation, LSP/Fusion engine tools, and product documentation search. Works across dbt Core, dbt Fusion, and dbt Platform environments. The `text_to_sql` tool generates SQL from natural language using project context — this is what AI-native data transformation looks like. Over 105K downloads on PyPI. If you use dbt, this server is essential.

**TommyBez/dbt-semantic-layer-mcp-server** (11 stars, TypeScript, MIT) focuses specifically on querying the dbt Semantic Layer through AI assistants. Metric discovery, natural language query generation, dimensional data analysis with filtering. Useful if you only need Semantic Layer access without the full dbt CLI integration. Installable via Smithery.

**kannandreams/dbt-mcp-server** provides a minimal, extensible interface for triggering dbt models, tests, and operations via CLI, API, or AI interface. Good for teams wanting a simpler, focused dbt integration.

## Streaming

### Apache Kafka

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [kanapuli/mcp-kafka](https://github.com/kanapuli/mcp-kafka) | 76 | Go | 5+ | stdio |
| [tuannvm/kafka-mcp-server](https://github.com/tuannvm/kafka-mcp-server) | 45 | Go | 7+ | stdio, HTTP |
| [streamnative/streamnative-mcp-server](https://github.com/streamnative/streamnative-mcp-server) | 22 | Go | Multiple | stdio |
| [Joel-hanson/kafka-mcp-server](https://github.com/Joel-hanson/kafka-mcp-server) | 1 | Python | 5 | stdio |
| [pavanjava/kafka_mcp_server](https://github.com/pavanjava/kafka_mcp_server) | — | Python | — | stdio |

**kanapuli/mcp-kafka** (76 stars, Go, MIT) is the most popular Kafka MCP server. Create topics with configurable partitions, list and delete topics, describe topic details, produce messages with key and header support, consume messages with configurable timeout. Built with the MCP Golang library, requires Go 1.24+. Supports PLAINTEXT and SASL_PLAINTEXT authentication. Fifty-eight commits — actively maintained.

**tuannvm/kafka-mcp-server** (45 stars, Go, MIT) takes a more comprehensive approach. Seven-plus tools: produce, consume, list brokers, describe topics, list consumer groups, describe consumer groups, and describe configs. Standout: **dual transport** (stdio + HTTP) with optional OAuth 2.1 authentication for the HTTP endpoint (Okta, Google, Azure AD, HMAC providers). Kafka authentication via SASL (PLAIN, SCRAM-SHA-256, SCRAM-SHA-512) and TLS. If you need remote access with enterprise auth, this is the one.

**streamnative/streamnative-mcp-server** (22 stars, Go) bridges both **Kafka and Pulsar** — the only server covering both streaming platforms. StreamNative Cloud integration, Schema Registry, Kafka Connect management, producer/consumer operations for both protocols. Multi-session Pulsar mode for per-user authentication. Installable via Homebrew, Docker, or Kubernetes Helm charts. Commercial backing from StreamNative.

**Joel-hanson/kafka-mcp-server** (1 star, Python, Apache 2.0) provides basic Kafka operations: initialize connection, list/create/delete topics, get topic info. Early-stage but functional for Python-centric teams.

## Data Integration

### Airbyte

Airbyte's MCP story is spread across multiple components rather than one unified server. The **PyAirbyte MCP server** (official, hosted on Heroku) provides the `generate_pyairbyte_pipeline` tool for creating data pipelines from natural language prompts. Safe mode enabled by default restricts destructive operations to objects created within the same session. The **Airbyte Knowledge MCP** connects AI agents to Airbyte's documentation, OpenAPI specs, YouTube content, and GitHub discussions. The **connector-builder-mcp** helps AI robots build Airbyte connectors. It's a fragmented story — no single server gives you full Airbyte control — but the pipeline generation tool is genuinely useful for bootstrapping integrations.

### Fivetran

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [andrewkkchan/mcp_fivetran](https://github.com/andrewkkchan/mcp_fivetran) | 2 | Python | 3 | stdio |

**andrewkkchan/mcp_fivetran** (2 stars, Python) is a community implementation — not official. Three tools: `invite_fivetran_user`, `list_connections`, and `sync_connection`. Minimal but covers the core operations data teams need: see what connections exist and trigger syncs. Fivetran doesn't have an official MCP server yet, which is surprising given the platform's popularity.

### Keboola

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [keboola/mcp-server](https://github.com/keboola/mcp-server) | 83 | Python | Multiple | stdio, StreamableHTTP |

**keboola/mcp-server** (83 stars, Python, official) is one of the most complete data platform MCP servers. Storage access and table/bucket management, component inspection (extractors, writers, data apps), SQL transformation creation with natural language, job execution and monitoring, workflow pipeline building (conditional and orchestrator flows), Streamlit data app deployment, project metadata management, and development branch operations. Tool authorization via HTTP headers with read-only mode and allowlists/denylists. Three thousand three hundred seven commits — extremely active development. Requires Python 3.10+ and the `uv` package manager. If you use Keboola, this is a first-class integration.

## Data Warehouses

### Snowflake

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [Snowflake-Labs/mcp](https://github.com/Snowflake-Labs/mcp) | 255 | Python | Multiple | stdio |
| [isaacwasserman/mcp-snowflake-server](https://github.com/isaacwasserman/mcp-snowflake-server) | 180 | Python | Multiple | stdio |
| [CDataSoftware/snowflake-mcp-server-by-cdata](https://github.com/CDataSoftware/snowflake-mcp-server-by-cdata) | — | — | — | stdio |
| [dynamike/snowflake-mcp-server](https://github.com/dynamike/snowflake-mcp-server) | — | Python | — | stdio |

**Snowflake-Labs/mcp** (255 stars, Python, official) is the flagship. Cortex Search for RAG over unstructured data, Cortex Analyst for structured data querying via semantic models, Cortex Agent for agentic orchestration, object management (create, drop, update Snowflake objects), SQL execution with permissions, and semantic view querying. Deployable via Docker, Docker Compose, or `uvx`. Works with Claude Desktop, Cursor, VS Code with Copilot, and Codex. This is **AI-native data warehousing** — the Cortex AI integration means your agent isn't just running SQL, it's leveraging Snowflake's built-in ML capabilities.

**isaacwasserman/mcp-snowflake-server** (180 stars, Python, GPL-3.0, v0.4.0) takes a more traditional approach: query execution (SELECT, INSERT, UPDATE, DELETE), table creation, database/schema/table listing, table description, and a data insight management system via a memo resource. Write operations toggled via `--allow-write` flag. TOML configuration for multiple connections. Exclusion patterns for filtering databases/schemas/tables. Higher community adoption than most unofficial servers — 180 stars is significant.

### Databricks

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [RafaelCartenet/mcp-databricks-server](https://github.com/RafaelCartenet/mcp-databricks-server) | 36 | Python | 7 | stdio |
| [JustTryAI/databricks-mcp-server](https://github.com/JustTryAI/databricks-mcp-server) | — | Python | Multiple | stdio |
| [alexxx-db/databricks-genie-mcp](https://github.com/alexxx-db/databricks-genie-mcp) | — | Python | 2 | stdio |

**Databricks official MCP support** is built into the platform — Databricks provides ready-to-use MCP servers for querying data and accessing tools in Unity Catalog, with permissions always enforced. This is the most integrated approach we've seen — MCP is a first-class citizen in the Databricks ecosystem.

**RafaelCartenet/mcp-databricks-server** (36 stars, Python, MIT) is the strongest community server. Seven tools for Unity Catalog interaction: `execute_sql_query`, `list_uc_catalogs`, `describe_uc_catalog`, `describe_uc_schema`, `describe_uc_table`, plus lineage discovery and code-level analysis. End-to-end data flow analysis tracing data from ingestion through transformation. The lineage tracking — identifying notebooks and jobs that process data — is particularly valuable for data governance.

**alexxx-db/databricks-genie-mcp** exposes the Databricks Genie API as MCP tools (`start_conversation`, `create_message`). Useful for conversational data exploration through Genie's natural language interface.

## Data Quality

### Great Expectations

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [davidf9999/gx-mcp-server](https://github.com/davidf9999/gx-mcp-server) | — | Python | Multiple | stdio |

**davidf9999/gx-mcp-server** (Python) exposes Great Expectations data validation as MCP tools. Load datasets from various sources, define data quality rules (Expectations) on the fly, run validation checks, and interpret results. Listed in awesome-mcp-servers and available on Smithery. Early-stage but fills a critical gap — data quality is often the most neglected part of data pipelines, and having AI agents run validation checks inline is genuinely useful.

## What's Missing

The data pipeline MCP category is strong but has notable gaps:

1. **Stream processing**: No Flink, Spark Streaming, or Kafka Streams MCP servers. Real-time transformation is unserved.
2. **Data catalogs**: No dedicated servers for Alation, Collibra, Amundsen, or DataHub (though Databricks Unity Catalog partially fills this role).
3. **Data lakehouse beyond Databricks**: No Delta Lake, Apache Iceberg, or Apache Hudi MCP servers for direct lakehouse management.
4. **Change data capture**: No Debezium or similar CDC tool MCP servers.
5. **Data observability**: No Monte Carlo, Bigeye, or Soda MCP servers for proactive data monitoring.
6. **Notebook integration**: No Jupyter, Zeppelin, or notebook-first MCP servers for data exploration workflows.

## The Bottom Line

**Rating: 4.0 / 5** — Data pipeline and ETL is one of the strongest MCP categories. dbt's official server (507 stars, 60+ tools) is a showcase for what MCP integration should look like. Snowflake and Databricks bring AI-native warehouse capabilities. Kafka has healthy competition with 5+ servers. Airflow, Prefect, and Dagster cover orchestration. The main weakness is on the streaming transformation side and data observability — but for batch ETL and warehouse operations, the ecosystem is mature and well-supported.

---

*Last updated: March 15, 2026. Star counts and tool details reflect the state of each project at time of research and may have changed since publication. ChatForest researches MCP servers through documentation review and community analysis — we do not test servers hands-on.*

# Data Pipeline & ETL MCP Servers — Airflow, dbt, Kafka, Snowflake, Databricks, Airbyte, and More

> Data pipeline and ETL MCP servers let AI agents orchestrate workflows, transform data, stream events, and manage data warehouses.


Data pipeline and ETL is one of the strongest categories in the MCP ecosystem — the major data engineering tools almost all have MCP server implementations, and several are official. AI agents that can orchestrate Airflow DAGs, run dbt transformations, produce and consume Kafka messages, query Snowflake warehouses, and trigger Airbyte syncs represent a genuine productivity multiplier for data teams. The category spans six areas: **workflow orchestration** (Airflow, Prefect, Dagster), **data transformation** (dbt), **streaming** (Kafka, Pulsar), **data integration** (Airbyte, Fivetran, Keboola), **data warehouses** (Snowflake, Databricks), and **data quality** (Great Expectations).

The headline finding: **dbt's official MCP server is the gold standard** with [533 stars](https://github.com/dbt-labs/dbt-mcp/stargazers) and [65 tools across 9 categories](https://github.com/dbt-labs/dbt-mcp#available-tools) — it's the most comprehensive single-tool MCP server we've reviewed in any category. Snowflake and Databricks both have official implementations with AI-native features (Cortex AI, Unity Catalog). Kafka is the most competitive subcategory with 5+ servers from different authors. The main gap is in streaming-side transformation — no server handles Flink, Spark Streaming, or real-time ETL natively. Part of our **[Data & Analytics](/categories/data-analytics/)** category.

## Workflow Orchestration

### Apache Airflow

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [call518/MCP-Airflow-API](https://github.com/call518/MCP-Airflow-API) | [43](https://github.com/call518/MCP-Airflow-API/stargazers) | Python | 45 | stdio, StreamableHTTP |
| [astronomer/astro-airflow-mcp](https://github.com/astronomer/agents/tree/main/astro-airflow-mcp) | [10](https://github.com/astronomer/astro-airflow-mcp/stargazers) | Python | 30+ | stdio, HTTP |

**call518/MCP-Airflow-API** ([43 stars](https://github.com/call518/MCP-Airflow-API/stargazers), Python, MIT, [v3.6.1](https://github.com/call518/MCP-Airflow-API/releases/tag/v3.6.1)) is the most comprehensive Airflow MCP server. Forty-five tools covering DAG operations (trigger, pause, resume, list), task instance monitoring, connection and pool management, XCom data handling, event log analysis, and configuration querying. Standout feature: **multi-version API support** with dynamic v1 (Airflow 2.x) and v2 (Airflow 3.0+) selection — 43 shared tools plus 2 asset management tools exclusive to v2. Large environment optimization with pagination and batch processing. Two transport modes with bearer token authentication for remote access. Docker Compose deployment with Open WebUI integration. Actively maintained with frequent releases through March 2026.

**astronomer/astro-airflow-mcp** ([10 stars](https://github.com/astronomer/astro-airflow-mcp/stargazers), Python, Apache 2.0) comes from Astronomer, the major Airflow managed service provider. **Note:** the original repository was [archived in January 2026](https://github.com/astronomer/astro-airflow-mcp) and the project relocated to the [Astronomer agents monorepo](https://github.com/astronomer/agents/tree/main/astro-airflow-mcp), where it has expanded significantly to **30+ core MCP tools**, 3 consolidated agent-optimized tools, 4 MCP Resources, and 3 MCP Prompts. Supports Airflow 2.x and 3.x with automatic version detection, bearer token and OAuth2 authentication. Can run as a standalone server or as an Airflow 3.x plugin. The new monorepo version is substantially more capable than the original 3-tool release.

### Prefect

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [PrefectHQ/prefect-mcp-server](https://github.com/PrefectHQ/prefect-mcp-server) | [33](https://github.com/PrefectHQ/prefect-mcp-server/stargazers) | Python | Multiple | stdio, HTTP |

**PrefectHQ/prefect-mcp-server** ([33 stars](https://github.com/PrefectHQ/prefect-mcp-server/stargazers), Python, official) provides AI assistants with monitoring, inspection, and management of Prefect workflow instances. Dashboard overviews, deployment and flow run queries, execution logs, event tracking, and CLI integration for resource management and deployment triggering. Intelligent debugging with contextual guidance for troubleshooting failed runs. Multi-client support across Claude Code, Cursor, Codex, Gemini, VS Code, Windsurf, and Kiro. Currently in beta (0.0.1-beta.10) — under active development. Supports Prefect Cloud API keys and OSS basic auth, plus multi-tenant HTTP header auth via FastMCP Cloud.

### Dagster

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [kyryl-opens-ml/mcp-server-dagster](https://github.com/kyryl-opens-ml/mcp-server-dagster) | [21](https://github.com/kyryl-opens-ml/mcp-server-dagster/stargazers) | Python | 9 | stdio |

**kyryl-opens-ml/mcp-server-dagster** ([21 stars](https://github.com/kyryl-opens-ml/mcp-server-dagster/stargazers), Python, Apache 2.0, v0.1.2) enables AI agents to interact with Dagster instances. Nine tools: `list_repositories`, `list_jobs`, `list_assets`, `recent_runs`, `get_run_info`, `launch_run`, `materialize_asset`, `terminate_run`, and `get_asset_info`. Built on the Dagster GraphQL API. Covers the essentials — explore pipelines, monitor runs, launch jobs, materialize assets. Not official but functional. Compatible with OpenAI agent SDKs alongside Claude. Note: the repository has been dormant since April 2025.

## Data Transformation

### dbt

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [dbt-labs/dbt-mcp](https://github.com/dbt-labs/dbt-mcp) | [533](https://github.com/dbt-labs/dbt-mcp/stargazers) | Python | [65](https://github.com/dbt-labs/dbt-mcp#available-tools) | stdio |
| [TommyBez/dbt-semantic-layer-mcp-server](https://github.com/TommyBez/dbt-semantic-layer-mcp-server) | [11](https://github.com/TommyBez/dbt-semantic-layer-mcp-server/stargazers) | TypeScript | Multiple | stdio |
| [kannandreams/dbt-mcp-server](https://github.com/kannandreams/dbt-mcp-server) | — | — | Multiple | stdio |

**dbt-labs/dbt-mcp** ([533 stars](https://github.com/dbt-labs/dbt-mcp/stargazers), Python, Apache 2.0, [v1.13.0](https://github.com/dbt-labs/dbt-mcp/releases/tag/v1.13.0), official) is the most impressive MCP server in this entire review — and one of the most impressive in any category. **[65 tools](https://github.com/dbt-labs/dbt-mcp#available-tools)** across 9 categories: SQL (2), Semantic Layer (6), Discovery API (18), dbt CLI (10), Admin API (10), code generation (3), LSP (3), product documentation (2), and server metadata (2). Works across dbt Core, dbt Fusion, and dbt Platform environments. The `text_to_sql` tool generates SQL from natural language using project context — this is what AI-native data transformation looks like. Recent releases added multi-project discovery ([v1.11.0](https://github.com/dbt-labs/dbt-mcp/releases/tag/v1.11.0)), config overrides ([v1.12.0](https://github.com/dbt-labs/dbt-mcp/releases/tag/v1.12.0)), and YML selector support ([v1.13.0](https://github.com/dbt-labs/dbt-mcp/releases/tag/v1.13.0)). 525 commits, 61 releases — extremely active development. If you use dbt, this server is essential.

**TommyBez/dbt-semantic-layer-mcp-server** ([11 stars](https://github.com/TommyBez/dbt-semantic-layer-mcp-server/stargazers), TypeScript, MIT) focuses specifically on querying the dbt Semantic Layer through AI assistants. Metric discovery, natural language query generation, dimensional data analysis with filtering. Useful if you only need Semantic Layer access without the full dbt CLI integration. Installable via Smithery.

**kannandreams/dbt-mcp-server** provides a minimal, extensible interface for triggering dbt models, tests, and operations via CLI, API, or AI interface. Good for teams wanting a simpler, focused dbt integration.

## Streaming

### Apache Kafka

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [kanapuli/mcp-kafka](https://github.com/kanapuli/mcp-kafka) | [75](https://github.com/kanapuli/mcp-kafka/stargazers) | Go | 6 | stdio |
| [tuannvm/kafka-mcp-server](https://github.com/tuannvm/kafka-mcp-server) | [48](https://github.com/tuannvm/kafka-mcp-server/stargazers) | Go | [9](https://github.com/tuannvm/kafka-mcp-server#features) | stdio, HTTP |
| [streamnative/streamnative-mcp-server](https://github.com/streamnative/streamnative-mcp-server) | [24](https://github.com/streamnative/streamnative-mcp-server/stargazers) | Go | Multiple | stdio |
| [Joel-hanson/kafka-mcp-server](https://github.com/Joel-hanson/kafka-mcp-server) | [1](https://github.com/Joel-hanson/kafka-mcp-server/stargazers) | Python | 5 | stdio |
| [pavanjava/kafka_mcp_server](https://github.com/pavanjava/kafka_mcp_server) | — | Python | — | stdio |

**kanapuli/mcp-kafka** ([75 stars](https://github.com/kanapuli/mcp-kafka/stargazers), Go, MIT) is the most popular Kafka MCP server. Six tools: create topics with configurable partitions, list and delete topics, describe topic details, produce messages with key and header support, consume messages with configurable timeout. Built with the MCP Golang library, requires Go 1.24+. Supports PLAINTEXT and SASL_PLAINTEXT authentication. Note: the repository has been dormant since March 2025.

**tuannvm/kafka-mcp-server** ([48 stars](https://github.com/tuannvm/kafka-mcp-server/stargazers), Go, MIT, [v2.0.2](https://github.com/tuannvm/kafka-mcp-server/releases/tag/v2.0.2)) takes a more comprehensive approach. Nine tools: produce, consume, list brokers, describe topics, list consumer groups, describe consumer groups, describe configs, cluster overview, and list topics. Standout: **dual transport** (stdio + HTTP) with optional OAuth 2.1 authentication for the HTTP endpoint (Okta, Google, Azure AD, HMAC providers). Kafka authentication via SASL (PLAIN, SCRAM-SHA-256, SCRAM-SHA-512) and TLS. The [v2.0.0 release](https://github.com/tuannvm/kafka-mcp-server/releases/tag/v2.0.0) (October 2025) was a major upgrade adding OAuth 2.1 and security features. If you need remote access with enterprise auth, this is the one.

**streamnative/streamnative-mcp-server** ([24 stars](https://github.com/streamnative/streamnative-mcp-server/stargazers), Go) bridges both **Kafka and Pulsar** — the only server covering both streaming platforms. StreamNative Cloud integration, Schema Registry, Kafka Connect management, producer/consumer operations for both protocols. Multi-session Pulsar mode for per-user authentication. Installable via Homebrew, Docker, or Kubernetes Helm charts. Commercial backing from StreamNative. Actively maintained with [April 2026 commits](https://github.com/streamnative/streamnative-mcp-server/commits/main) — the only Kafka MCP server with recent 2026 development activity.

**Joel-hanson/kafka-mcp-server** ([1 star](https://github.com/Joel-hanson/kafka-mcp-server/stargazers), Python, Apache 2.0) provides basic Kafka operations: initialize connection, list/create/delete topics, get topic info. Early-stage with only 3 commits; planned features (message production/consumption) have not materialized.

## Data Integration

### Airbyte

Airbyte's MCP story is spread across multiple components rather than one unified server. The **PyAirbyte MCP server** (official, hosted on Heroku) provides the `generate_pyairbyte_pipeline` tool for creating data pipelines from natural language prompts. Safe mode enabled by default restricts destructive operations to objects created within the same session. The **Airbyte Knowledge MCP** connects AI agents to Airbyte's documentation, OpenAPI specs, YouTube content, and GitHub discussions. The **connector-builder-mcp** helps AI robots build Airbyte connectors. It's a fragmented story — no single server gives you full Airbyte control — but the pipeline generation tool is genuinely useful for bootstrapping integrations.

### Fivetran

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [andrewkkchan/mcp_fivetran](https://github.com/andrewkkchan/mcp_fivetran) | [2](https://github.com/andrewkkchan/mcp_fivetran/stargazers) | Python | 3 | stdio |

**andrewkkchan/mcp_fivetran** ([2 stars](https://github.com/andrewkkchan/mcp_fivetran/stargazers), Python) is a community implementation — not official. Three tools: `invite_fivetran_user`, `list_connections`, and `sync_connection`. Minimal but covers the core operations data teams need: see what connections exist and trigger syncs. Fivetran doesn't have an official MCP server yet, which is surprising given the platform's popularity.

### Keboola

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [keboola/mcp-server](https://github.com/keboola/mcp-server) | [83](https://github.com/keboola/mcp-server/stargazers) | Python | [31](https://github.com/keboola/mcp-server/blob/main/TOOLS.md) | stdio, StreamableHTTP |

**keboola/mcp-server** ([83 stars](https://github.com/keboola/mcp-server/stargazers), Python, [v1.49.1](https://github.com/keboola/mcp-server/releases/tag/v1.49.1), official) is one of the most complete data platform MCP servers. [31 documented tools](https://github.com/keboola/mcp-server/blob/main/TOOLS.md) across storage, components, SQL, jobs, flows, data apps, documentation, OAuth, search, and project management. SQL transformation creation with natural language, job execution and monitoring, workflow pipeline building (conditional and orchestrator flows), Streamlit data app deployment, project metadata management, and development branch operations. Tool authorization via HTTP headers with read-only mode and allowlists/denylists. Over 3,400 commits — extremely active development with multiple releases in March–April 2026. Requires Python 3.10+ and the `uv` package manager. If you use Keboola, this is a first-class integration.

## Data Warehouses

### Snowflake

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [Snowflake-Labs/mcp](https://github.com/Snowflake-Labs/mcp) | [271](https://github.com/Snowflake-Labs/mcp/stargazers) | Python | Multiple | stdio |
| [isaacwasserman/mcp-snowflake-server](https://github.com/isaacwasserman/mcp-snowflake-server) | [180](https://github.com/isaacwasserman/mcp-snowflake-server/stargazers) | Python | 8 | stdio |
| [CDataSoftware/snowflake-mcp-server-by-cdata](https://github.com/CDataSoftware/snowflake-mcp-server-by-cdata) | — | — | — | stdio |
| [dynamike/snowflake-mcp-server](https://github.com/dynamike/snowflake-mcp-server) | — | Python | — | stdio |

**Snowflake-Labs/mcp** ([271 stars](https://github.com/Snowflake-Labs/mcp/stargazers), Python, Apache 2.0, official) is the flagship. Cortex Search for RAG over unstructured data, Cortex Analyst for structured data querying via semantic models, Cortex Agent for agentic orchestration, object management (create, drop, update Snowflake objects), SQL execution with permissions, and semantic view querying. Deployable via Docker, Docker Compose, or `uvx`. Works with Claude Desktop, Cursor, VS Code with Copilot, and Codex. This is **AI-native data warehousing** — the Cortex AI integration means your agent isn't just running SQL, it's leveraging Snowflake's built-in ML capabilities.

**isaacwasserman/mcp-snowflake-server** ([180 stars](https://github.com/isaacwasserman/mcp-snowflake-server/stargazers), Python, GPL-3.0, v0.4.0) takes a more traditional approach: [8 tools](https://github.com/isaacwasserman/mcp-snowflake-server#readme) — `read_query`, `write_query`, `create_table`, `list_databases`, `list_schemas`, `list_tables`, `describe_table`, and `append_insight`. Write operations toggled via `--allow-write` flag. TOML configuration for multiple connections. Exclusion patterns for filtering databases/schemas/tables. Higher community adoption than most unofficial servers — 180 stars is significant. Note: the repository has been inactive since October 2025.

### Databricks

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [RafaelCartenet/mcp-databricks-server](https://github.com/RafaelCartenet/mcp-databricks-server) | [40](https://github.com/RafaelCartenet/mcp-databricks-server/stargazers) | Python | [5](https://github.com/RafaelCartenet/mcp-databricks-server#readme) | stdio |
| [JustTryAI/databricks-mcp-server](https://github.com/JustTryAI/databricks-mcp-server) | — | Python | Multiple | stdio |
| [alexxx-db/databricks-genie-mcp](https://github.com/alexxx-db/databricks-genie-mcp) | — | Python | 2 | stdio |

**Databricks official MCP support** is built into the platform — Databricks provides ready-to-use MCP servers for querying data and accessing tools in Unity Catalog, with permissions always enforced. This is the most integrated approach we've seen — MCP is a first-class citizen in the Databricks ecosystem.

**RafaelCartenet/mcp-databricks-server** ([40 stars](https://github.com/RafaelCartenet/mcp-databricks-server/stargazers), Python, MIT) is the strongest community server. [Five tools](https://github.com/RafaelCartenet/mcp-databricks-server#readme) for Unity Catalog interaction: `execute_sql_query`, `list_uc_catalogs`, `describe_uc_catalog`, `describe_uc_schema`, and `describe_uc_table`. Supports OAuth M2M authentication via service principal. The Unity Catalog integration — browsing catalogs, schemas, and tables with SQL execution — is particularly valuable for data governance workflows.

**alexxx-db/databricks-genie-mcp** exposes the Databricks Genie API as MCP tools (`start_conversation`, `create_message`). Useful for conversational data exploration through Genie's natural language interface.

## Data Quality

### Great Expectations

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [davidf9999/gx-mcp-server](https://github.com/davidf9999/gx-mcp-server) | — | Python | Multiple | stdio |

**davidf9999/gx-mcp-server** ([4 stars](https://github.com/davidf9999/gx-mcp-server/stargazers), Python, MIT) exposes Great Expectations data validation as MCP tools. Load datasets from various sources, define data quality rules (Expectations) on the fly, run validation checks, and interpret results. Listed in awesome-mcp-servers and available on Smithery. Early-stage but fills a critical gap — data quality is often the most neglected part of data pipelines, and having AI agents run validation checks inline is genuinely useful.

## What's Missing

The data pipeline MCP category is strong but has notable gaps:

1. **Stream processing**: No Flink, Spark Streaming, or Kafka Streams MCP servers. Real-time transformation is unserved.
2. **Data catalogs**: No dedicated servers for Alation, Collibra, Amundsen, or DataHub (though Databricks Unity Catalog partially fills this role).
3. **Data lakehouse beyond Databricks**: No Delta Lake, Apache Iceberg, or Apache Hudi MCP servers for direct lakehouse management.
4. **Change data capture**: No Debezium or similar CDC tool MCP servers.
5. **Data observability**: No Monte Carlo, Bigeye, or Soda MCP servers for proactive data monitoring.
6. **Notebook integration**: No Jupyter, Zeppelin, or notebook-first MCP servers for data exploration workflows.

## The Bottom Line

**Rating: 4.0 / 5** — Data pipeline and ETL is one of the strongest MCP categories. dbt's official server ([533 stars](https://github.com/dbt-labs/dbt-mcp/stargazers), [65 tools](https://github.com/dbt-labs/dbt-mcp#available-tools)) is a showcase for what MCP integration should look like. Snowflake and Databricks bring AI-native warehouse capabilities. Kafka has healthy competition with 5+ servers. Airflow, Prefect, and Dagster cover orchestration. The main weakness is on the streaming transformation side and data observability — but for batch ETL and warehouse operations, the ecosystem is mature and well-supported.

---

*Last updated: April 11, 2026. Star counts and tool details reflect the state of each project at time of research and may have changed since publication. ChatForest researches MCP servers through documentation review and community analysis — we do not test servers hands-on.*

*This review was last edited on 2026-04-11 using Claude Opus 4.6 (Anthropic).*


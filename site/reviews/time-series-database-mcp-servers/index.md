# Time-Series Database MCP Servers — Grafana, ClickHouse, Prometheus, InfluxDB, VictoriaMetrics, SigNoz, and More

> Time-series database MCP servers let AI agents query metrics, write data points, inspect schemas, and analyze performance trends through natural language.


Time-series data — metrics, logs, traces, IoT sensor readings, financial ticks — is one of the most common workloads AI agents encounter in production environments. The MCP ecosystem for time-series databases is surprisingly mature, with official servers from Grafana, ClickHouse, InfluxData, VictoriaMetrics, Apache IoTDB, and CrateDB. Part of our **[Databases MCP category](/categories/databases/)**.

The landscape divides into six areas: **observability platforms** (Grafana — the hub that queries multiple backends), **column-oriented databases** (ClickHouse — analytics-first with time-series capabilities), **Prometheus-compatible systems** (Prometheus, VictoriaMetrics — metrics monitoring), **time-series databases** (InfluxDB, TimescaleDB — purpose-built for time-series), **IoT and industrial** (Apache IoTDB, TDengine — high-write-throughput engines), and **specialized engines** (CrateDB, QuestDB — SQL-first time-series).

The headline finding: **Grafana's MCP server is the single most comprehensive time-series MCP server** (2,900 stars, 30+ tools, Go, Apache 2.0). It doesn't just query Grafana dashboards — it directly queries Prometheus, Loki, ClickHouse, CloudWatch, and Elasticsearch backends, manages alerting rules, creates incidents, and renders dashboard panels as images. If you use Grafana, this one server replaces the need for most individual database MCP servers. **ClickHouse's official server** (761 stars) is the strongest standalone database server with read-only defaults and an embedded chDB engine — and now offers a Cloud Remote MCP server on the AWS Marketplace. **SigNoz is a major new open-source entrant** (88 stars, 30+ tools) — the first comprehensive open-source observability platform with a dedicated MCP server covering metrics, traces, logs, alerts, and dashboards. **VictoriaMetrics has the broadest ecosystem** — separate MCP servers for metrics, logs, traces, and anomaly detection, now promoted from the Community org to the main VictoriaMetrics org with a hosted MCP server in VictoriaMetrics Cloud. **The Prometheus subcategory is the most competitive** — five servers with different trade-offs. **Read-only defaults are the norm** — ClickHouse, TDengine, and VictoriaMetrics all enforce read-only access by default, a mature safety pattern. **The hosted remote MCP trend is accelerating** — Grafana, ClickHouse Cloud, VictoriaMetrics Cloud, and SigNoz Cloud all offer managed MCP endpoints, eliminating the need to deploy local servers.

## Observability Platforms

### Grafana

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [grafana/mcp-grafana](https://github.com/grafana/mcp-grafana) | 2,900 | Go | 30+ | stdio, remote |

**grafana/mcp-grafana** (2,900 stars, Go, Apache 2.0, 563 commits) is the most feature-rich time-series MCP server in the entire ecosystem. Originally written in Python, it was rewritten in Go for performance.

Thirty-plus tools span a dozen categories: **Dashboard** — search, retrieve, patch dashboards, and get panel queries. **Prometheus** — execute PromQL queries, retrieve metric metadata, compute histogram percentiles. **Loki** — LogQL queries, log pattern detection, volume statistics. **ClickHouse** — list tables, describe schemas, execute SQL. **CloudWatch** — list namespaces, metrics, and dimensions, execute CloudWatch queries. **Elasticsearch** — Lucene and Query DSL search. **Alerting** — create, update, and delete alert rules, notification policies, and contact points. **Incidents** — list and create incidents, add activity timelines. **OnCall** — schedule and alert group management. **Rendering** — dashboard and panel PNG rendering. **Annotations** — create, update, patch, and query time-series annotations. **RBAC** — teams, users, roles, and permission management. **Sift** — AI-powered investigation capabilities.

The key architectural choice: tool categories are configurable. Disable what you don't need with `--disable-<category>` flags to keep the tool surface manageable. Template variable substitution and Grafana macro expansion work automatically. Batch multi-panel queries reduce round-trips. Requires Grafana 9.0+.

This is effectively a universal time-series MCP gateway. If your observability stack runs through Grafana, this single server provides AI agent access to all your time-series backends.

**April 2026 update:** At GrafanaCON 2026, Grafana Labs announced a **remote hosted MCP server** — external agents can connect to Grafana's MCP endpoint without deploying anything locally. They also open-sourced **[o11y-bench](https://grafana.com/blog/o11y-bench-open-benchmark-for-observability-agents/)**, a benchmark that evaluates AI agents on observability workflows against a real Grafana stack with MCP access. AI Observability entered public preview in Grafana Cloud, and the new **gcx CLI** simplifies agent-to-Grafana connectivity. Grafana Tempo 2.9 shipped with an **embedded MCP server** for distributed tracing (the standalone [tempo-mcp-server](https://github.com/grafana/tempo-mcp-server) repo was archived). A standalone **[Loki MCP server](https://github.com/grafana/loki-mcp)** (Go, 31 commits) also exists for teams using Loki without Grafana dashboards.

### Grafana (Community)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [DrDroidLab/grafana-mcp-server](https://github.com/DrDroidLab/grafana-mcp-server) | 6 | Python | 6 | stdio |

**DrDroidLab/grafana-mcp-server** (6 stars, Python, MIT, 46 commits) is a simpler alternative for teams that don't need the full official feature set. Six tools: `test_connection`, `grafana_promql_query`, `grafana_loki_query`, `grafana_get_dashboard_config`, `grafana_query_dashboard_panels`, `grafana_fetch_label_values`. Docker Compose support for quick deployment. Useful if you only need Prometheus and Loki querying through Grafana and want a lighter-weight server.

### SigNoz

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [SigNoz/signoz-mcp-server](https://github.com/SigNoz/signoz-mcp-server) | 88 | Go | 30+ | stdio, HTTP, remote |

**SigNoz/signoz-mcp-server** (88 stars, Go, Apache 2.0, 110 commits) is the official MCP server for SigNoz, the open-source Datadog alternative built on OpenTelemetry. Thirty-plus tools covering:

**Metrics** — discovery and querying with smart aggregation defaults that automatically apply the right timeAggregation and spaceAggregation based on metric type (gauge, counter, histogram). **Traces** — search and aggregation with span breakdowns. **Logs** — search, filter, and analysis with time-series aggregations. **Alerts** — list, create, update, and delete alert rules. **Dashboards** — operations and management. **Services** — monitoring and discovery. **Notification channels** — management. **Explorer views** — saved filters.

Three deployment modes: **SigNoz Cloud** (hosted MCP endpoint — no installation, just authenticate), **self-hosted stdio** (local binary), or **self-hosted HTTP** (standalone server with optional OAuth). Docker containers and binary downloads for macOS/Linux. Compatible with Claude, Cursor, Gemini, Codex, and other MCP clients.

SigNoz is the first comprehensive **open-source** observability platform with a dedicated MCP server. While Grafana's MCP server is more feature-rich for the Grafana ecosystem, SigNoz offers a unified metrics-traces-logs experience in a single tool for teams using SigNoz as their observability stack.

## Column-Oriented Databases

### ClickHouse

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [ClickHouse/mcp-clickhouse](https://github.com/ClickHouse/mcp-clickhouse) | 761 | Python | 4 | stdio, HTTP/SSE, remote |

**ClickHouse/mcp-clickhouse** (761 stars, Python, Apache 2.0, 74 commits) is ClickHouse's official MCP server. Four tools:

`run_query` — SQL execution, **read-only by default** with explicit write opt-in. DROP and TRUNCATE require a separate, additional opt-in. `list_databases` — enumerate all databases. `list_tables` — browse tables with pagination, filtering, and column metadata. `run_chdb_select_query` — execute queries via the embedded chDB engine, running ClickHouse locally without any ETL or server connection.

The chDB integration is unique — it means AI agents can run ClickHouse SQL against local data (Parquet, CSV, JSON) without needing a ClickHouse server at all. Combined with the tiered write protection (read-only → writes → destructive writes), this is one of the safest database MCP servers in any category.

FastMCP middleware support. Token-based auth for HTTP/SSE transport. Development mode available. Several community alternatives exist (burakdirin, ThomAub, izaitsevfb with docs semantic search), but the official server covers most use cases.

**April 2026 update:** ClickHouse Cloud launched a **[Remote MCP Server](https://clickhouse.com/blog/clickhouse-cloud-joins-aws-ai-agents-and-tools-mcp)** (private preview) — a managed, read-only MCP endpoint for ClickHouse Cloud services, available in the new AWS Marketplace "AI Agents and Tools" category. No local server to deploy; enable it via the Connect menu in ClickHouse Cloud. The remote server is intentionally limited to read-only operations. Join the waitlist at clickhouse.ai.

## Prometheus-Compatible Systems

### Prometheus (pab1it0)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [pab1it0/prometheus-mcp-server](https://github.com/pab1it0/prometheus-mcp-server) | 427 | Python | 6 | stdio, HTTP, SSE |

**pab1it0/prometheus-mcp-server** (427 stars, Python, MIT, 209 commits, v1.6.0) is the most mature Prometheus MCP server. Six tools: `execute_query` (instant PromQL), `execute_range_query` (range queries with time parameters), `list_metrics` (with pagination), `get_metric_metadata` (including bulk retrieval), `get_targets` (scrape target information), and `health_check`.

The standout features are operational: **authentication** — basic, bearer, mutual TLS, and custom headers. **Deployment** — Docker, Kubernetes with Helm chart. **Multi-instance** — tool prefix customization so you can run multiple Prometheus servers without name conflicts. **Multi-tenant** — Org ID header for Cortex/Mimir compatibility. **DDoS protection** — configurable request timeouts. Actively maintained with 201 commits through March 2026.

### Prometheus (giantswarm)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [giantswarm/mcp-prometheus](https://github.com/giantswarm/mcp-prometheus) | 7 | Go | 15+ | stdio, SSE, HTTP |

**giantswarm/mcp-prometheus** (7 stars, Go, 117 commits) has the deepest feature set of any Prometheus MCP server despite its low star count. Fifteen-plus tools covering:

**Core queries** — instant and range queries with optimization. **Discovery** — metrics listing, label enumeration. **Monitoring** — target health and status, active alerts, AlertManager discovery, recording and alerting rule inspection. **Infrastructure** — build, runtime, config, and TSDB info. **Advanced** — exemplar queries for trace correlation (correlate metrics with distributed traces), multi-tenant support for Cortex, Mimir, and Thanos. **Observability** — OpenTelemetry tracing integration and Prometheus metrics endpoint for self-monitoring.

Dynamic per-query client configuration and result truncation for large datasets. If you're running a multi-tenant metrics infrastructure (Cortex, Mimir, or Thanos), this is the right choice — pab1it0's server doesn't natively support querying across tenants or inspecting alerting rules.

**April 2026 update:** The commit count nearly doubled (62→117) since our initial review, reflecting major development. New **OAuth 2.1 support** via mcp-oauth with Dex as the OIDC identity provider. All tools now accept optional `prometheus_url` and `org_id` parameters for per-call overrides, enabling multi-instance querying from a single server.

### VictoriaMetrics

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [VictoriaMetrics/mcp-victoriametrics](https://github.com/VictoriaMetrics/mcp-victoriametrics) | 160 | Go | 10+ | stdio, SSE, HTTP, remote |

**VictoriaMetrics/mcp-victoriametrics** (160 stars, Go, Apache 2.0, 351 commits) is the official MCP server for VictoriaMetrics — **promoted from the Community org to the main VictoriaMetrics org** since our initial review, reflecting its elevated status. Ten-plus tools covering:

**Querying** — metric queries with graph rendering. **Discovery** — series listing, exporting, label enumeration. **Analysis** — cardinality analysis and usage statistics (critical for cost management in large deployments). **Rule testing** — validate alert and recording rules before deployment. **Query tools** — query analysis, tracing, prettification, and explanation. **Config debugging** — relabeling, downsampling, and retention configuration inspection. **Documentation** — embedded searchable docs for offline reference.

Works with both single-node and cluster deployments. VictoriaMetrics Cloud integration via API keys. Multi-tenant support with accountID/projectID. **Public testing instance** at `https://play-mcp.victoriametrics.com/mcp` — you can try the MCP server without deploying anything.

The broader VictoriaMetrics MCP ecosystem is unique: **mcp-victorialogs** for log analysis, **mcp-victoriatraces** for distributed tracing, and **mcp-vmanomaly** for anomaly detection. No other time-series vendor offers four coordinated MCP servers covering metrics, logs, traces, and anomaly detection.

**April 2026 update:** VictoriaMetrics Cloud Q1 2026 shipped a **hosted MCP server** — connect agents to your metrics without deploying anything locally. VictoriaLogs reached GA. The vmanomaly MCP server added dynamic presets with metric-subset discovery for Kubernetes, VictoriaMetrics, and node-exporter sources, improving onboarding. Hosted MCP for VictoriaLogs is planned next.

## Time-Series Databases

### InfluxDB (Official v3)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [influxdata/influxdb3_mcp_server](https://github.com/influxdata/influxdb3_mcp_server) | 30 | TypeScript | 10+ | stdio |

**influxdata/influxdb3_mcp_server** (30 stars, TypeScript, MIT/Apache 2.0 dual-licensed, 69 commits) is InfluxData's official MCP server for InfluxDB 3. Ten-plus tools:

**Data operations** — SQL query execution and Line Protocol data writing. **Schema** — measurement listing and schema inspection. **Admin** — database CRUD, admin token creation and listing (Core/Enterprise only), resource token management with granular permissions, cloud-specific database token operations, operator token regeneration, health status checking. **Context** — custom context loading via markdown and JSON files.

Version-aware tool availability — some tools are exclusive to Core, Enterprise, or Cloud editions. Docker and npm deployment. The InfluxDB 3 engine represents a major architectural shift from InfluxDB 2 (Apache Arrow-based columnar storage), so this server targets the modern InfluxDB stack.

### InfluxDB (Community v2)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [idoru/influxdb-mcp-server](https://github.com/idoru/influxdb-mcp-server) | 37 | JavaScript | 4+ | stdio, HTTP, Streamable HTTP |

**idoru/influxdb-mcp-server** (37 stars, JavaScript, MIT, 36 commits, v0.2.0) targets InfluxDB v2 with Flux queries. Four tools: `write-data` (Line Protocol ingestion), `query-data` (Flux query execution), `create-bucket`, `create-org`. Also provides resources (org listings, bucket management, measurement discovery) and prompts (Flux query templates, Line Protocol formatting).

If you're still on InfluxDB 2 (many organizations are), this is the server to use. The official v3 server doesn't support Flux — it's SQL-only.

### InfluxDB (AWS Timestream)

AWS also maintains an InfluxDB MCP server in the [awslabs/mcp](https://github.com/awslabs/mcp) monorepo (~4,700 stars total) at `/src/timestream-for-influxdb-mcp-server`. Python, Apache 2.0, stdio transport. Manages InfluxDB 2 buckets and orgs, writes and queries data, and manages tags for AWS Timestream resources. Use this if your InfluxDB runs on AWS Timestream for InfluxDB.

### TimescaleDB

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [brunoprela/timescaledb-mcp](https://github.com/brunoprela/timescaledb-mcp) | 0 | Python | 6 | stdio |

**brunoprela/timescaledb-mcp** (0 stars, Python, MIT, 9 commits, v0.1.0) is the most capable TimescaleDB MCP server. Six tools: `execute_query` (SQL with parameter binding), `list_tables`, `describe_table`, `list_hypertables` (TimescaleDB-specific), `describe_hypertable` (dimensions, chunks, compression settings), `query_timeseries` (time-series data with bucketing and aggregation).

The hypertable-specific tools are the key differentiator — `list_hypertables` and `describe_hypertable` expose TimescaleDB's partitioning, chunk management, and compression configuration, which generic PostgreSQL MCP servers can't surface. Async support via asyncpg with connection pooling. Resources via URI schema. Three pre-configured prompts for common workflows.

TimescaleDB is notably underserved — Timescale's own pg-aiguide project focuses on PostgreSQL documentation, not direct database access. Since TimescaleDB is a PostgreSQL extension, generic Postgres MCP servers (like crystaldba/postgres-mcp at 2,300 stars) can query TimescaleDB data, but they won't understand hypertables, continuous aggregates, or compression policies.

## IoT and Industrial

### Apache IoTDB

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [apache/iotdb-mcp-server](https://github.com/apache/iotdb-mcp-server) | 38 | Python | 7 | stdio |

**apache/iotdb-mcp-server** (38 stars, Python, Apache 2.0, 10 commits) is the official Apache IoTDB MCP server. Supports two SQL dialects:

**Tree Model** (3 tools) — `metadata_query`, `select_query`, `export_query`. IoTDB's traditional tree-structured device/measurement hierarchy. **Table Model** (4 tools) — `read_query`, `list_tables`, `describe_table`, `export_table_query`. The newer relational-style interface.

Aggregation functions include SUM, COUNT, MAX_VALUE, MIN_VALUE, AVG, VARIANCE, and more. Export to CSV or Excel. Session pool management supports up to 100 concurrent connections. ISO 8601 timestamps. Docker deployment.

Apache IoTDB is designed for massive-scale IoT time-series with millions of devices and billions of data points per day. The MCP server is minimal (10 commits) but functional for querying and exporting data. No write operations — this is read-only.

### TDengine

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [Abeautifulsnow/tdengine-mcp](https://github.com/Abeautifulsnow/tdengine-mcp) | 10 | Python | 3 | stdio, SSE |

**Abeautifulsnow/tdengine-mcp** (10 stars, Python, MIT, 56 commits, v0.0.9) is the primary MCP server for TDengine. Three tools: `query` (SELECT), `info` (DESCRIBE), and database/stable enumeration (SHOW).

**Strictly read-only** — blocks INSERT, UPDATE, DELETE, CREATE, and ALTER statements at the server level. This is the strongest read-only enforcement of any time-series MCP server. Available on PyPI (`tdengine_mcp_server`). Smithery integration. Configurable 30-second timeout.

TDengine is popular in China for IoT and industrial time-series with extremely high write throughput. The MCP server is community-maintained, not official from TDEngine Inc.

## Specialized Engines

### CrateDB

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [crate/cratedb-mcp](https://github.com/crate/cratedb-mcp) | 7 | Python | 5 | stdio |

**crate/cratedb-mcp** (7 stars, Python, Apache 2.0, 156 commits, v0.1.0) is the official CrateDB MCP server. Five tools in two families:

**Text-to-SQL** — `query_sql`, `get_table_columns`, `get_table_metadata`, `get_health`. **Documentation** — `get_cratedb_documentation_index`, `fetch_cratedb_docs` (retrieves documentation from cratedb.com/docs).

The natural-language Text-to-SQL focus is unique — CrateDB positions this server for agents that need to translate user questions into CrateDB SQL rather than executing pre-written queries. Beta stage but actively developed with 141 commits and 11 releases.

CrateDB combines SQL, full-text search, geospatial, and time-series in a single distributed database. The MCP server's documentation retrieval tools help agents generate correct CrateDB-specific SQL syntax.

### QuestDB

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [brunoprela/questdb-mcp](https://github.com/brunoprela/questdb-mcp) | 1 | TypeScript | 4 | stdio, HTTP |

**brunoprela/questdb-mcp** (1 star, TypeScript, 6 commits) provides basic QuestDB access. Four tools: `query` (SELECT with JSON/CSV output), `insert` (InfluxDB Line Protocol writes with automatic schema creation), `list_tables`, `describe_table`. Zod schema validation. Full TypeScript support. Custom tool registration.

QuestDB's PostgreSQL-compatible interface on port 8812 means generic PostgreSQL MCP servers can also query QuestDB. This dedicated server adds Line Protocol write support and QuestDB-specific schema handling.

## Time-Series Forecasting

### FAIM

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [S-FM/faim-mcp](https://github.com/S-FM/faim-mcp) | 8 | TypeScript | 2 | stdio |

**S-FM/faim-mcp** (8 stars, TypeScript, MIT, 26 commits) is not a database server — it provides time-series forecasting using foundation models. Two tools: `list_models` and `forecast` (point and probabilistic forecasting). Supports Chronos2 and TiRex models. Remote server available. Useful as a complement to time-series database MCP servers: query historical data from InfluxDB/Prometheus/ClickHouse, then forecast with FAIM.

## Other Notable Servers

**Hydrolix** — [hydrolix/mcp-hydrolix](https://github.com/hydrolix/mcp-hydrolix) (9 stars, Python, Apache 2.0, 137 commits). Fork of ClickHouse MCP adapted for Hydrolix's time-series datalake. Four tools (run_select_query, list_databases, list_tables, get_table_info). Bearer token auth.

**GigAPI** — [gigapi/gigapi-mcp](https://github.com/gigapi/gigapi-mcp) (6 stars, Python, 14 commits). Timeseries lake with six tools including InfluxDB Line Protocol writes and health checks. NDJSON format. Hive partitioning.

**Datadog** — Datadog's official remote MCP server ([docs](https://docs.datadoghq.com/bits_ai/mcp_server/)) launched GA in March 2026 with 16+ core tools covering metrics, logs, traces, dashboards, monitors, incidents, hosts, services, and events, plus optional toolsets for APM, Error Tracking, Feature Flags, DBM, Security, and LLM Observability. Fully managed — no local server needed. Covered more fully in our [Observability & Monitoring review](/categories/observability-monitoring/).

## What's missing

**No unified time-series query language** — agents must know PromQL for Prometheus, Flux for InfluxDB v2, SQL for ClickHouse/TimescaleDB/QuestDB/CrateDB, and LogQL for Loki. No MCP server abstracts across these.

**No official TimescaleDB server** — the community servers have zero stars. Timescale's own MCP effort (pg-aiguide) focuses on documentation, not data access. Generic PostgreSQL MCP servers work but miss hypertable-specific features.

**No official QuestDB server** — the community server has 1 star and 6 commits. QuestDB's PostgreSQL compatibility means generic PG servers work, but dedicated time-series features (Line Protocol writes, partitioning metadata) require the dedicated server.

**No write-side safety for metrics** — most servers allow writing time-series data (InfluxDB, QuestDB). Only TDengine's MCP server enforces strict read-only at the server level. ClickHouse requires explicit opt-in for writes, which is the right pattern. The hosted remote MCP servers (ClickHouse Cloud, VictoriaMetrics Cloud) trend toward read-only by default.

**No cross-database migration or comparison tools** — no MCP server helps agents migrate data between time-series databases or compare query performance across engines.

**Alerting improving but uneven** — Grafana and SigNoz MCP servers now both support creating and managing alert rules. Prometheus, VictoriaMetrics, and ClickHouse MCP servers can query existing rules but can't create new ones.

## The verdict

**Rating: 4.0/5** — strong official vendor support, mature safety patterns (read-only defaults), a maturing trend toward hosted remote MCP servers, and genuine utility for observability and time-series workflows.

**The standout: Grafana mcp-grafana** (2,900 stars, 30+ tools). If your time-series data flows through Grafana — and most production time-series data does — this single server provides comprehensive access to Prometheus, Loki, ClickHouse, CloudWatch, and Elasticsearch. It's also the only server with alerting rule management, incident creation, and OnCall schedule access. Now available as a remote hosted MCP endpoint. Start here.

**Best standalone database server: ClickHouse** (761 stars, 4 tools). Read-only by default with tiered write protection. The chDB integration for local queries is unique and valuable. The new Cloud Remote MCP server (private preview) brings managed, zero-deploy access to ClickHouse Cloud data via the AWS Marketplace.

**Best open-source observability: SigNoz** (88 stars, 30+ tools). The first comprehensive open-source observability platform with a dedicated MCP server. Unified metrics, traces, logs, alerts, and dashboards in one tool. Smart aggregation defaults based on metric type. SigNoz Cloud offers a hosted MCP endpoint.

**Best Prometheus server: depends on your stack.** For single-instance Prometheus, pab1it0's server (427 stars) is battle-tested with Helm chart deployment and mutual TLS. For multi-tenant setups (Cortex, Mimir, Thanos), giantswarm's server (7 stars but 117 commits) has deeper multi-tenant support, OAuth 2.1, exemplar queries, and OpenTelemetry integration.

**Best ecosystem: VictoriaMetrics** (160 stars) — the only vendor offering coordinated MCP servers for metrics, logs, traces, and anomaly detection, now promoted to the main VictoriaMetrics org. The hosted MCP server in VictoriaMetrics Cloud and the public testing instance lower the barrier to evaluation.

**For InfluxDB:** Use the official v3 server if you're on InfluxDB 3, idoru's server for InfluxDB v2 with Flux queries, or the AWS server if you're on Timestream for InfluxDB.

**For niche databases:** Apache IoTDB's official server (38 stars) is functional for read-only IoT data access. TDengine's community server is the most safety-conscious with strict read-only enforcement. CrateDB's official server (156 commits) focuses on Text-to-SQL for natural language querying. TimescaleDB and QuestDB are underserved — use generic PostgreSQL MCP servers as a fallback.

The time-series MCP category earns 4.0/5 because of the breadth of official vendor support (seven vendors maintain official servers, up from six), mature safety patterns, the exceptional quality of Grafana's server, and the emerging trend toward hosted remote MCP endpoints. The gap is in cross-database abstraction — agents still need to know which query language to use for which backend.

*This review was refreshed on 2026-04-27 using Claude Opus 4.6 (Anthropic). [See what changed.](#april-2026-refresh-summary)*

## April 2026 refresh summary

**What changed since March 15, 2026:**

- **SigNoz MCP Server — NEW** (88 stars, Go, 30+ tools). First comprehensive open-source observability platform with a dedicated MCP server. Metrics, traces, logs, alerts, dashboards.
- **Grafana GrafanaCON 2026** — Remote hosted MCP server, o11y-bench agent benchmark (open source), AI Observability in public preview, gcx CLI. Tempo 2.9 shipped embedded MCP server (standalone repo archived). Stars 2,500→2,900 (+16%), commits 473→563.
- **ClickHouse Cloud Remote MCP** — Managed read-only MCP endpoint in private preview, AWS Marketplace "AI Agents and Tools" category. Stars 715→761.
- **VictoriaMetrics promoted to main org** — From VictoriaMetrics-Community to VictoriaMetrics. Hosted MCP in VictoriaMetrics Cloud. VictoriaLogs GA. Stars 130→160 (+23%), commits 302→351.
- **giantswarm/mcp-prometheus** — OAuth 2.1 support, per-call URL/org overrides. Commits nearly doubled: 62→117 (+89%).
- **pab1it0/prometheus-mcp-server** — Stars 379→427 (+13%).
- **Datadog** — Official remote MCP server GA (March 2026), 16+ tools. Mentioned here; covered fully in Observability review.
- **Star updates:** idoru/influxdb 32→37, Apache IoTDB 35→38, Hydrolix 8→9, CrateDB 141→156 commits.
- **Hosted remote MCP trend** — Grafana, ClickHouse Cloud, VictoriaMetrics Cloud, SigNoz Cloud, and Datadog all now offer managed MCP endpoints.
- **Rating holds at 4.0/5** — Meaningful growth in hosted/remote options and SigNoz as a new open-source entrant, but core gaps (no unified query language, underserved TimescaleDB/QuestDB) persist.


---
title: "Time-Series Database MCP Servers — Grafana, ClickHouse, Prometheus, InfluxDB, VictoriaMetrics, and More"
date: 2026-03-15T08:38:00+09:00
description: "Time-series database MCP servers let AI agents query metrics, write data points, inspect schemas, and analyze performance trends through natural language. We reviewed 25+ servers across observability platforms (Grafana official with 30+ tools across Prometheus/Loki/ClickHouse/CloudWatch/Elasticsearch), column-oriented databases (ClickHouse official with read-only defaults and chDB embedded engine), Prometheus-compatible systems (pab1it0 at 379 stars with Helm chart deployment, giantswarm at 15+ tools with multi-tenant Cortex/Mimir/Thanos support), time-series databases (InfluxDB official for v3, community for v2, AWS Timestream), VictoriaMetrics (official community project with public testing instance and companion logs/traces/anomaly servers), and specialized engines (Apache IoTDB official with dual SQL dialects, CrateDB official with Text-to-SQL, TimescaleDB community with hypertable tools, QuestDB community, TDengine with read-only enforcement). Grafana's mcp-grafana leads with 2,500 stars and 473 commits as the most comprehensive time-series MCP server."
og_description: "Time-Series Database MCP servers: Grafana mcp-grafana (official, 2,500 stars, Go, 30+ tools across dashboards/Prometheus/Loki/ClickHouse/CloudWatch/Elasticsearch/alerting/incidents/OnCall/rendering/annotations/RBAC), ClickHouse (official, 715 stars, Python, 4 tools with read-only defaults and chDB embedded engine), pab1it0/prometheus-mcp-server (379 stars, Python, 6 tools with Helm chart and mutual TLS), VictoriaMetrics (official community, 130 stars, Go, 10+ tools with query analysis/cardinality/graph rendering and public testing instance), DrDroidLab/grafana-mcp-server (70 stars, Python, 6 tools), Apache IoTDB (official, 35 stars, Python, dual Tree/Table SQL models), idoru/influxdb-mcp-server (32 stars, JavaScript, InfluxDB v2 with Flux queries), influxdata/influxdb3_mcp_server (official, 29 stars, TypeScript, 10+ tools for Core/Enterprise/Cloud), giantswarm/mcp-prometheus (5 stars, Go, 15+ tools with multi-tenant Cortex/Mimir/Thanos and OpenTelemetry tracing), TDengine MCP (10 stars, Python, read-only enforcement), CrateDB (official, 8 stars, Python, Text-to-SQL), TimescaleDB community (hypertable inspection), QuestDB community (Line Protocol writes). 25+ servers reviewed. Rating: 4.0/5."
content_type: "Review"
card_description: "Time-series database MCP servers across observability platforms, column-oriented databases, Prometheus-compatible systems, time-series engines, and specialized databases. Grafana's mcp-grafana (2,500 stars, 473 commits, Go) is the undisputed leader — 30+ tools spanning Prometheus queries, Loki log searches, ClickHouse SQL, CloudWatch metrics, Elasticsearch search, alerting rules, incident management, OnCall schedules, dashboard rendering, and annotations. For standalone ClickHouse access, the official mcp-clickhouse (715 stars) provides read-only-by-default SQL execution with an embedded chDB engine for local queries without ETL. The Prometheus ecosystem is the most competitive subcategory — pab1it0's server (379 stars) offers the most mature Python implementation with Helm chart deployment, while giantswarm's Go implementation (5 stars but 62 commits) has the deepest feature set with 15+ tools including exemplar queries for trace correlation and multi-tenant support for Cortex, Mimir, and Thanos. VictoriaMetrics stands out with a public testing instance and the broadest companion ecosystem (separate servers for logs, traces, and anomaly detection). The category earns 4.0/5 — strong official vendor support, read-only defaults as a common safety pattern, and genuine utility for observability workflows."
last_refreshed: 2026-03-15
---

Time-series data — metrics, logs, traces, IoT sensor readings, financial ticks — is one of the most common workloads AI agents encounter in production environments. The MCP ecosystem for time-series databases is surprisingly mature, with official servers from Grafana, ClickHouse, InfluxData, VictoriaMetrics, Apache IoTDB, and CrateDB.

The landscape divides into six areas: **observability platforms** (Grafana — the hub that queries multiple backends), **column-oriented databases** (ClickHouse — analytics-first with time-series capabilities), **Prometheus-compatible systems** (Prometheus, VictoriaMetrics — metrics monitoring), **time-series databases** (InfluxDB, TimescaleDB — purpose-built for time-series), **IoT and industrial** (Apache IoTDB, TDengine — high-write-throughput engines), and **specialized engines** (CrateDB, QuestDB — SQL-first time-series).

The headline finding: **Grafana's MCP server is the single most comprehensive time-series MCP server** (2,500 stars, 30+ tools, Go, Apache 2.0). It doesn't just query Grafana dashboards — it directly queries Prometheus, Loki, ClickHouse, CloudWatch, and Elasticsearch backends, manages alerting rules, creates incidents, and renders dashboard panels as images. If you use Grafana, this one server replaces the need for most individual database MCP servers. **ClickHouse's official server** (715 stars) is the strongest standalone database server with read-only defaults and an embedded chDB engine. **VictoriaMetrics has the broadest ecosystem** — separate MCP servers for metrics, logs, traces, and anomaly detection, plus a public testing instance. **The Prometheus subcategory is the most competitive** — five servers with different trade-offs. **Read-only defaults are the norm** — ClickHouse, TDengine, and VictoriaMetrics all enforce read-only access by default, a mature safety pattern.

## Observability Platforms

### Grafana

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [grafana/mcp-grafana](https://github.com/grafana/mcp-grafana) | 2,500 | Go | 30+ | stdio |

**grafana/mcp-grafana** (2,500 stars, Go, Apache 2.0, 473 commits) is the most feature-rich time-series MCP server in the entire ecosystem. Originally written in Python, it was rewritten in Go for performance.

Thirty-plus tools span a dozen categories: **Dashboard** — search, retrieve, patch dashboards, and get panel queries. **Prometheus** — execute PromQL queries, retrieve metric metadata, compute histogram percentiles. **Loki** — LogQL queries, log pattern detection, volume statistics. **ClickHouse** — list tables, describe schemas, execute SQL. **CloudWatch** — list namespaces, metrics, and dimensions, execute CloudWatch queries. **Elasticsearch** — Lucene and Query DSL search. **Alerting** — create, update, and delete alert rules, notification policies, and contact points. **Incidents** — list and create incidents, add activity timelines. **OnCall** — schedule and alert group management. **Rendering** — dashboard and panel PNG rendering. **Annotations** — create, update, patch, and query time-series annotations. **RBAC** — teams, users, roles, and permission management. **Sift** — AI-powered investigation capabilities.

The key architectural choice: tool categories are configurable. Disable what you don't need with `--disable-<category>` flags to keep the tool surface manageable. Template variable substitution and Grafana macro expansion work automatically. Batch multi-panel queries reduce round-trips. Requires Grafana 9.0+.

This is effectively a universal time-series MCP gateway. If your observability stack runs through Grafana, this single server provides AI agent access to all your time-series backends.

### Grafana (Community)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [DrDroidLab/grafana-mcp-server](https://github.com/DrDroidLab/grafana-mcp-server) | 70 | Python | 6 | stdio |

**DrDroidLab/grafana-mcp-server** (70 stars, Python, MIT) is a simpler alternative for teams that don't need the full official feature set. Six tools: `test_connection`, `grafana_promql_query`, `grafana_loki_query`, `grafana_get_dashboard_config`, `grafana_query_dashboard_panels`, `grafana_fetch_label_values`. Docker Compose support for quick deployment. Useful if you only need Prometheus and Loki querying through Grafana and want a lighter-weight server.

## Column-Oriented Databases

### ClickHouse

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [ClickHouse/mcp-clickhouse](https://github.com/ClickHouse/mcp-clickhouse) | 715 | Python | 4 | stdio, HTTP/SSE |

**ClickHouse/mcp-clickhouse** (715 stars, Python, Apache 2.0, 67 commits) is ClickHouse's official MCP server. Four tools:

`run_query` — SQL execution, **read-only by default** with explicit write opt-in. DROP and TRUNCATE require a separate, additional opt-in. `list_databases` — enumerate all databases. `list_tables` — browse tables with pagination, filtering, and column metadata. `run_chdb_select_query` — execute queries via the embedded chDB engine, running ClickHouse locally without any ETL or server connection.

The chDB integration is unique — it means AI agents can run ClickHouse SQL against local data (Parquet, CSV, JSON) without needing a ClickHouse server at all. Combined with the tiered write protection (read-only → writes → destructive writes), this is one of the safest database MCP servers in any category.

FastMCP middleware support. Token-based auth for HTTP/SSE transport. Development mode available. Several community alternatives exist (burakdirin, ThomAub, izaitsevfb with docs semantic search), but the official server covers most use cases.

## Prometheus-Compatible Systems

### Prometheus (pab1it0)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [pab1it0/prometheus-mcp-server](https://github.com/pab1it0/prometheus-mcp-server) | 379 | Python | 6 | stdio, HTTP, SSE |

**pab1it0/prometheus-mcp-server** (379 stars, Python, MIT, 201 commits, v1.6.0) is the most mature Prometheus MCP server. Six tools: `execute_query` (instant PromQL), `execute_range_query` (range queries with time parameters), `list_metrics` (with pagination), `get_metric_metadata` (including bulk retrieval), `get_targets` (scrape target information), and `health_check`.

The standout features are operational: **authentication** — basic, bearer, mutual TLS, and custom headers. **Deployment** — Docker, Kubernetes with Helm chart. **Multi-instance** — tool prefix customization so you can run multiple Prometheus servers without name conflicts. **Multi-tenant** — Org ID header for Cortex/Mimir compatibility. **DDoS protection** — configurable request timeouts. Actively maintained with 201 commits through March 2026.

### Prometheus (giantswarm)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [giantswarm/mcp-prometheus](https://github.com/giantswarm/mcp-prometheus) | 5 | Go | 15+ | stdio, SSE, HTTP |

**giantswarm/mcp-prometheus** (5 stars, Go, 62 commits) has the deepest feature set of any Prometheus MCP server despite its low star count. Fifteen-plus tools covering:

**Core queries** — instant and range queries with optimization. **Discovery** — metrics listing, label enumeration. **Monitoring** — target health and status, active alerts, AlertManager discovery, recording and alerting rule inspection. **Infrastructure** — build, runtime, config, and TSDB info. **Advanced** — exemplar queries for trace correlation (correlate metrics with distributed traces), multi-tenant support for Cortex, Mimir, and Thanos. **Observability** — OpenTelemetry tracing integration and Prometheus metrics endpoint for self-monitoring.

Dynamic per-query client configuration and result truncation for large datasets. If you're running a multi-tenant metrics infrastructure (Cortex, Mimir, or Thanos), this is the right choice — pab1it0's server doesn't natively support querying across tenants or inspecting alerting rules.

### VictoriaMetrics

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [VictoriaMetrics-Community/mcp-victoriametrics](https://github.com/VictoriaMetrics-Community/mcp-victoriametrics) | 130 | Go | 10+ | stdio, SSE, HTTP |

**VictoriaMetrics-Community/mcp-victoriametrics** (130 stars, Go, Apache 2.0, 302 commits) is the official community MCP server for VictoriaMetrics. Ten-plus tools covering:

**Querying** — metric queries with graph rendering. **Discovery** — series listing, exporting, label enumeration. **Analysis** — cardinality analysis and usage statistics (critical for cost management in large deployments). **Rule testing** — validate alert and recording rules before deployment. **Query tools** — query analysis, tracing, prettification, and explanation. **Config debugging** — relabeling, downsampling, and retention configuration inspection. **Documentation** — embedded searchable docs for offline reference.

Works with both single-node and cluster deployments. VictoriaMetrics Cloud integration via API keys. Multi-tenant support with accountID/projectID. **Public testing instance** at `https://play-mcp.victoriametrics.com/mcp` — you can try the MCP server without deploying anything.

The broader VictoriaMetrics MCP ecosystem is unique: **mcp-victorialogs** for log analysis, **mcp-victoriatraces** for distributed tracing, and **mcp-vmanomaly** for anomaly detection. No other time-series vendor offers four coordinated MCP servers covering metrics, logs, traces, and anomaly detection.

## Time-Series Databases

### InfluxDB (Official v3)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [influxdata/influxdb3_mcp_server](https://github.com/influxdata/influxdb3_mcp_server) | 29 | TypeScript | 10+ | stdio |

**influxdata/influxdb3_mcp_server** (29 stars, TypeScript, MIT/Apache 2.0 dual-licensed, 38 commits) is InfluxData's official MCP server for InfluxDB 3. Ten-plus tools:

**Data operations** — SQL query execution and Line Protocol data writing. **Schema** — measurement listing and schema inspection. **Admin** — database CRUD, admin token creation and listing (Core/Enterprise only), resource token management with granular permissions, cloud-specific database token operations, operator token regeneration, health status checking. **Context** — custom context loading via markdown and JSON files.

Version-aware tool availability — some tools are exclusive to Core, Enterprise, or Cloud editions. Docker and npm deployment. The InfluxDB 3 engine represents a major architectural shift from InfluxDB 2 (Apache Arrow-based columnar storage), so this server targets the modern InfluxDB stack.

### InfluxDB (Community v2)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [idoru/influxdb-mcp-server](https://github.com/idoru/influxdb-mcp-server) | 32 | JavaScript | 4+ | stdio, HTTP, Streamable HTTP |

**idoru/influxdb-mcp-server** (32 stars, JavaScript, MIT, 36 commits, v0.2.0) targets InfluxDB v2 with Flux queries. Four tools: `write-data` (Line Protocol ingestion), `query-data` (Flux query execution), `create-bucket`, `create-org`. Also provides resources (org listings, bucket management, measurement discovery) and prompts (Flux query templates, Line Protocol formatting).

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
| [apache/iotdb-mcp-server](https://github.com/apache/iotdb-mcp-server) | 35 | Python | 7 | stdio |

**apache/iotdb-mcp-server** (35 stars, Python, Apache 2.0, 10 commits) is the official Apache IoTDB MCP server. Supports two SQL dialects:

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
| [crate/cratedb-mcp](https://github.com/crate/cratedb-mcp) | 8 | Python | 5 | stdio |

**crate/cratedb-mcp** (8 stars, Python, Apache 2.0, 141 commits, v0.1.0) is the official CrateDB MCP server. Five tools in two families:

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

**Hydrolix** — [hydrolix/mcp-hydrolix](https://github.com/hydrolix/mcp-hydrolix) (8 stars, Python, Apache 2.0, 120 commits). Fork of ClickHouse MCP adapted for Hydrolix's time-series datalake. Four tools (run_select_query, list_databases, list_tables, get_table_info). Bearer token auth.

**GigAPI** — [gigapi/gigapi-mcp](https://github.com/gigapi/gigapi-mcp) (6 stars, Python, 14 commits). Timeseries lake with six tools including InfluxDB Line Protocol writes and health checks. NDJSON format. Hive partitioning.

**Grafana Loki** — [grafana/loki-mcp](https://github.com/grafana/loki-mcp) (Go). Dedicated Loki MCP server separate from the main mcp-grafana. For teams that use Loki without Grafana dashboards.

**Grafana Tempo** — [grafana/tempo-mcp-server](https://github.com/grafana/tempo-mcp-server) (Go). Distributed tracing from Grafana Tempo. Complements the metrics and logs capabilities in mcp-grafana.

## What's missing

**No unified time-series query language** — agents must know PromQL for Prometheus, Flux for InfluxDB v2, SQL for ClickHouse/TimescaleDB/QuestDB/CrateDB, and LogQL for Loki. No MCP server abstracts across these.

**No official TimescaleDB server** — the community servers have zero stars. Timescale's own MCP effort (pg-aiguide) focuses on documentation, not data access. Generic PostgreSQL MCP servers work but miss hypertable-specific features.

**No official QuestDB server** — the community server has 1 star and 6 commits. QuestDB's PostgreSQL compatibility means generic PG servers work, but dedicated time-series features (Line Protocol writes, partitioning metadata) require the dedicated server.

**No write-side safety for metrics** — most servers allow writing time-series data (InfluxDB, QuestDB). Only TDengine's MCP server enforces strict read-only at the server level. ClickHouse requires explicit opt-in for writes, which is the right pattern.

**No cross-database migration or comparison tools** — no MCP server helps agents migrate data between time-series databases or compare query performance across engines.

**Limited alerting integration** — only Grafana's MCP server supports creating and managing alert rules. Prometheus, VictoriaMetrics, and ClickHouse MCP servers can query existing rules but can't create new ones.

## The verdict

**Rating: 4.0/5** — strong official vendor support, mature safety patterns (read-only defaults), and genuine utility for observability and time-series workflows.

**The standout: Grafana mcp-grafana** (2,500 stars, 30+ tools). If your time-series data flows through Grafana — and most production time-series data does — this single server provides comprehensive access to Prometheus, Loki, ClickHouse, CloudWatch, and Elasticsearch. It's also the only server with alerting rule management, incident creation, and OnCall schedule access. Start here.

**Best standalone database server: ClickHouse** (715 stars, 4 tools). Read-only by default with tiered write protection. The chDB integration for local queries is unique and valuable. If you use ClickHouse for analytics or time-series, the official server is well-designed.

**Best Prometheus server: depends on your stack.** For single-instance Prometheus, pab1it0's server (379 stars) is battle-tested with Helm chart deployment and mutual TLS. For multi-tenant setups (Cortex, Mimir, Thanos), giantswarm's server (5 stars but 62 commits) has deeper multi-tenant support, exemplar queries, and OpenTelemetry integration.

**Best ecosystem: VictoriaMetrics** — the only vendor offering coordinated MCP servers for metrics, logs, traces, and anomaly detection. The public testing instance lowers the barrier to evaluation.

**For InfluxDB:** Use the official v3 server if you're on InfluxDB 3, idoru's server for InfluxDB v2 with Flux queries, or the AWS server if you're on Timestream for InfluxDB.

**For niche databases:** Apache IoTDB's official server is functional for read-only IoT data access. TDengine's community server is the most safety-conscious with strict read-only enforcement. CrateDB's official server focuses on Text-to-SQL for natural language querying. TimescaleDB and QuestDB are underserved — use generic PostgreSQL MCP servers as a fallback.

The time-series MCP category earns 4.0/5 because of the breadth of official vendor support (six vendors maintain official servers), mature safety patterns, and the exceptional quality of Grafana's server. The gap is in cross-database abstraction — agents still need to know which query language to use for which backend.

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*

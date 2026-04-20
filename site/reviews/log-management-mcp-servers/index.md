# Log Management MCP Servers — Splunk, Elasticsearch, Loki, Datadog, CloudWatch, and Beyond

> Log management MCP servers let AI agents search, analyze, and correlate logs across Splunk, Elasticsearch, Grafana Loki, Graylog, AWS CloudWatch, Datadog, Dynatrace, New Relic, and Sumo Logic.


Logs are the ground truth of every production system — **error traces, access records, audit trails, performance data**. Log management MCP servers let AI agents search, correlate, and analyze logs across enterprise platforms without developers manually copy-pasting stack traces into chat windows or writing ad hoc queries.

The headline finding: **this is one of the strongest MCP categories**. Nearly every major log management platform has at least one MCP server — many have official ones. Grafana's mcp-grafana dominates at 2,500 stars with Loki, Elasticsearch, and CloudWatch log querying built in. Splunk has both an official Splunkbase app and active community servers. Datadog ships a managed remote MCP endpoint. The gap isn't coverage — it's fragmentation, with some platforms having 5+ competing community servers.

## The Landscape

### Grafana + Loki

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [grafana/mcp-grafana](https://github.com/grafana/mcp-grafana) | ~2,500 | Go | 50+ (6 Loki) | stdio |
| [grafana/loki-mcp](https://github.com/grafana/loki-mcp) | ~98 | Go | 1 | stdio, SSE |

**Grafana's official mcp-grafana is the most comprehensive observability MCP server available.** 2,500 stars, 61 open issues, 41 open PRs — heavily active development. Covers dashboards, datasources, Prometheus, Loki, ClickHouse, CloudWatch, Elasticsearch, incidents, alerting, OnCall, annotations, and rendering.

The 6 Loki-specific tools:

| Tool | What it does |
|------|-------------|
| `query_loki_logs` | Execute LogQL queries for log and metric retrieval |
| `list_loki_label_names` | Enumerate available log labels |
| `list_loki_label_values` | Retrieve values for specific log labels |
| `query_loki_stats` | Obtain log stream statistics |
| `query_loki_patterns` | Identify detected log patterns and anomalies |
| `search_logs` | High-level log search across ClickHouse (OTel) and Loki datasources |

Install: `uvx mcp-grafana` with `GRAFANA_URL` and `GRAFANA_SERVICE_ACCOUNT_TOKEN` environment variables.

The dedicated **grafana/loki-mcp** (98 stars, MIT, Go) provides a single `loki_query` tool for querying Loki directly. Supports multi-tenant org IDs, SSE transport, and Docker deployment. Simpler if you only need Loki without the full Grafana stack. 31 commits, 8 issues, 16 PRs.

Community alternatives include [tumf/grafana-loki-mcp](https://github.com/tumf/grafana-loki-mcp) (FastMCP/Python), [mo-silent/loki-mcp-server](https://github.com/mo-silent/loki-mcp-server), and [lexfrei/mcp-loki](https://github.com/lexfrei/mcp-loki) — all provide basic LogQL querying.

### Elasticsearch / ELK Stack

| Server | Stars | Language | Tools | Status |
|--------|-------|----------|-------|--------|
| [elastic/mcp-server-elasticsearch](https://github.com/elastic/mcp-server-elasticsearch) | ~626 | Rust | 5 | Deprecated |
| [cr7258/elasticsearch-mcp-server](https://github.com/cr7258/elasticsearch-mcp-server) | — | Python | — | Active |
| [awesimon/elasticsearch-mcp](https://github.com/awesimon/elasticsearch-mcp) | — | — | — | Active |

**Elastic's official MCP server is deprecated** — superseded by the Elastic Agent Builder MCP endpoint available in Elastic 9.2.0+ and Elasticsearch Serverless. The existing server (626 stars, Rust, Apache-2.0, v0.4.6) still works via Docker (`docker.elastic.co/mcp/elasticsearch`) with stdio and streamable-HTTP protocols.

5 tools before deprecation:

| Tool | What it does |
|------|-------------|
| `list_indices` | Display all available Elasticsearch indices |
| `get_mappings` | Retrieve field mappings for specific indices |
| `search` | Execute queries using Query DSL |
| `esql` | Run ES\|QL queries |
| `get_shards` | Access shard information |

Several community alternatives fill the gap: [cr7258/elasticsearch-mcp-server](https://github.com/cr7258/elasticsearch-mcp-server) (Python, OpenSearch compatible), [awesimon/elasticsearch-mcp](https://github.com/awesimon/elasticsearch-mcp) (natural language to Elasticsearch queries), and [sonirico/mcp-elasticsearch](https://github.com/sonirico/mcp-elasticsearch) (Go, multiple auth methods).

The Logstash MCP Server also exists for ELK stack log pipeline management, though details are limited.

### Splunk

| Server | Stars | Language | Tools | Auth |
|--------|-------|----------|-------|------|
| [CiscoDevNet/Splunk-MCP-Server-official](https://github.com/CiscoDevNet/Splunk-MCP-Server-official) | ~2 | — | 7+ | Splunk mgmt port |
| [livehybrid/splunk-mcp](https://github.com/livehybrid/splunk-mcp) | ~94 | Python | 13 | API token |
| [splunk/splunk-mcp-server2](https://github.com/splunk/splunk-mcp-server2) | ~29 | Python/TS | 7 | API token |
| [deslicer/mcp-for-splunk](https://github.com/deslicer/mcp-for-splunk) | ~20 | Python | 20+ | API token |

**Splunk has the most fragmented MCP ecosystem — four+ servers, each with a different approach.**

The **official Splunkbase app** (CiscoDevNet, v1.0.1, Feb 2026, beta) runs inside your Splunk instance on the management port (8089). Tools include `generate_spl` (natural language to SPL), `run_splunk_query`, `get_splunk_info`, `get_indexes`, `get_index_info`, and `get_saved_searches`. Minimal GitHub presence (2 stars) since it's distributed via Splunkbase.

The **community leader** is livehybrid/splunk-mcp (94 stars, Python, Apache-2.0). 13 tools across search, index management, KV store operations, health checks, and user management. Supports SSE transport and Docker deployment. 6 issues, 9 PRs, actively maintained.

splunk/splunk-mcp-server2 (29 stars, MIT) adds SPL risk scoring (0-100 scale), automatic sensitive data masking, and multiple output formats (JSON, CSV, Markdown). 7 tools with a security-first approach.

deslicer/mcp-for-splunk (20 stars, Apache-2.0) offers 20+ tools with 16 resources, AI workflow builders, and natural language to SPL conversion.

### Datadog

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [datadog-labs/mcp-server](https://github.com/datadog-labs/mcp-server) | ~10 | — | 16+ | Remote HTTP |
| [winor30/mcp-server-datadog](https://github.com/winor30/mcp-server-datadog) | ~139 | TypeScript | 20 | stdio |

**Datadog offers both an official managed remote MCP server and a popular community server.**

The **official server** (datadog-labs, MIT, Preview) is a managed remote endpoint at `mcp.datadoghq.com` — no self-hosting needed. Core toolset covers logs, metrics, traces, dashboards, monitors, incidents, hosts, services, events, and notebooks. Additional opt-in toolsets for alerting, APM, Database Monitoring, Error Tracking, feature flags, LLM Observability, networking, security, software delivery, and Synthetic tests. Paginates by token budget with cursor-based continuation.

Install for Claude Code: `claude mcp add --transport http datadog https://mcp.datadoghq.com/api/unstable/mcp-server/mcp`

The **community leader** winor30/mcp-server-datadog (139 stars, TypeScript, Apache-2.0) provides 20 named tools:

| Tool | What it does |
|------|-------------|
| `get_logs` | Search and retrieve Datadog logs |
| `query_metrics` | Query metric data |
| `list_traces` | Search distributed traces |
| `list_incidents` / `get_incident` | Incident management |
| `get_monitors` | Monitor status and configuration |
| `list_dashboards` / `get_dashboard` | Dashboard access |
| `list_hosts` / `get_active_hosts_count` | Host inventory |
| `mute_host` / `unmute_host` | Host maintenance |
| `list_downtimes` / `schedule_downtime` / `cancel_downtime` | Downtime management |
| `get_rum_applications` / `get_rum_events` / `get_rum_grouped_event_count` / `get_rum_page_performance` / `get_rum_page_waterfall` | Real User Monitoring |

8 open issues, 14 open PRs, npm/Smithery install.

### AWS CloudWatch

| Server | Stars | Language | Tools | Source |
|--------|-------|----------|-------|--------|
| CloudWatch MCP Server (awslabs/mcp) | — | Python | 4+ | Official monorepo |
| [awslabs/Log-Analyzer-with-MCP](https://github.com/awslabs/Log-Analyzer-with-MCP) | ~153 | Python | 5 | Official standalone |

**AWS provides two official CloudWatch log analysis servers.**

The **CloudWatch MCP Server** inside the awslabs/mcp monorepo (4,700+ stars total) offers alarm troubleshooting, metric analysis, and log analysis tools including `get_metric_data`, `get_metric_metadata`, and `get_recommended_metric_alarms`. PyPI: `awslabs.cloudwatch-mcp-server`. Note: the older `cloudwatch-logs-mcp-server` package is deprecated in favor of the unified CloudWatch server.

The standalone **Log-Analyzer-with-MCP** (153 stars, Python, Apache-2.0, 11 contributors) focuses specifically on CloudWatch Logs analysis — log group discovery, CloudWatch Logs Insights query execution, log summaries, error pattern identification, and multi-service log correlation. A solid demo project that shows MCP log analysis patterns.

### Dynatrace

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [dynatrace-oss/dynatrace-mcp](https://github.com/dynatrace-oss/dynatrace-mcp) | ~92 | TypeScript | 15+ | stdio, HTTP |

**Dynatrace's official open-source MCP server bridges AI assistants to the Dynatrace observability platform.** 92 stars, MIT license, 7 issues, 11 PRs.

Install: `npx -y @dynatrace-oss/dynatrace-mcp-server` (stdio) or `--http` for server mode.

Key tools:

| Tool | What it does |
|------|-------------|
| `execute_dql` | Run Dynatrace Query Language statements |
| `list_problems` / `get_problem_details` | Problem investigation |
| `list_vulnerabilities` / `get_vulnerability_details` | Security vulnerability data |
| `get_entity_details` / `get_entity_ownership` | Entity monitoring |
| `list_documents` / `read_document` / `create_document` | Notebooks and dashboards |
| `send_event` | Transmit event data |
| `send_slack_message` / `send_email` | Notification integration |
| `setup_notification_workflow` | Configure automation |

Also includes **Davis CoPilot** tools for natural language to DQL conversion.

### New Relic

| Server | Stars | Language | Tools | Status |
|--------|-------|----------|-------|--------|
| [newrelic/mcp-server](https://github.com/newrelic/mcp-server) | ~3 | — | — | Public Preview |

**New Relic's official MCP server launched in November 2025 as a Public Preview.** Connects AI agents to New Relic's observability data for natural language querying of telemetry data, alert investigation, and performance analysis.

Tool categories include entity/account management, alerting/monitoring, incident response, performance analytics (golden metrics, logs, thread analysis), NRQL queries, and deployment impact assessment. Low GitHub presence (3 stars, 1 contributor, no releases published) suggests the real product lives behind the New Relic platform.

Community alternatives: [cloudbring/newrelic-mcp](https://github.com/cloudbring/newrelic-mcp) (NerdGraph API integration), [ulucaydin/mcp-server-newrelic](https://github.com/ulucaydin/mcp-server-newrelic) (unofficial NerdGraph MCP).

### Graylog

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [AI-enthusiasts/mcp-graylog](https://github.com/AI-enthusiasts/mcp-graylog) | ~1 | Python | 11 | stdio |
| [lcaliani/graylog-mcp](https://github.com/lcaliani/graylog-mcp) | — | JavaScript | 1 | stdio |

**Graylog has built-in MCP support** — the platform itself can act as an MCP endpoint with API token authentication. But the standalone community servers provide different integration approaches.

AI-enthusiasts/mcp-graylog (Python, MIT) is the most complete with 11 tools:

| Tool | What it does |
|------|-------------|
| `search_logs` | Query logs using Elasticsearch syntax |
| `search_stream_logs` | Target-specific stream searching |
| `get_last_event_from_stream` | Retrieve most recent stream events |
| `list_streams` / `search_streams_by_name` / `get_stream_info` | Stream management |
| `get_log_statistics` | Generate aggregations and pattern analysis |
| `get_error_logs` | Extract error messages by timeframe |
| `get_log_count_by_level` | Aggregate logs by severity level |
| `get_system_info` | Graylog infrastructure status |
| `test_connection` | Validate server connectivity |

Docker deployment recommended. Other community servers: [mothlike/mcp_graylog](https://github.com/mothlike/mcp_graylog) (Elasticsearch query syntax, statistics), [Pranavj17/mcp-server-graylog](https://github.com/Pranavj17/mcp-server-graylog) (focused on production debugging).

### Sumo Logic

| Server | Stars | Language | Tools |
|--------|-------|----------|-------|
| [samwang0723/mcp-sumologic](https://github.com/samwang0723/mcp-sumologic) | — | TypeScript | — |
| [vinit-devops/sumologic_mcp](https://github.com/vinit-devops/sumologic_mcp) | — | Python | 37 |

**Sumo Logic has community-only MCP coverage — no official server yet.** vinit-devops/sumologic_mcp stands out with 37 tools. samwang0723/mcp-sumologic (TypeScript) and greyaperez/mcp-sumologic (natural language to Sumo queries) provide lighter alternatives. Sumo Logic itself has published MCP documentation suggesting an official server may be in development.

### OpenTrace (Self-Hosted)

| Server | Stars | Language | Tools | Storage |
|--------|-------|----------|-------|---------|
| [adham90/opentrace](https://github.com/adham90/opentrace) | ~13 | Go | 75+ | SQLite |

**OpenTrace is the only self-hosted, vendor-neutral observability MCP server.** 13 stars, MIT, Go 1.25+, 308 commits — substantial codebase despite low adoption.

75+ tools across 8 categories: overview/triage, log intelligence (full-text search, distributed traces, performance analysis, period comparisons), database introspection (Postgres read-only — query stats, table metrics, lock analysis, index optimization), errors (grouping, investigation, user impact), analytics/journeys, uptime/watches, agent memory (persistent notes across sessions), and settings/admin.

Single binary deployment with SQLite storage. Docker: `docker run ghcr.io/adham90/opentrace:latest`. One-click deploy on DigitalOcean, Railway, and Render. Includes a web UI with live log streaming. Designed for small-to-medium teams that want observability without vendor lock-in.

### Standalone Log Analyzers

Several MCP servers focus on local log file analysis rather than connecting to a platform:

| Server | Stars | Focus |
|--------|-------|-------|
| [Fato07/log-analyzer-mcp](https://github.com/Fato07/log-analyzer-mcp) | — | Parse 9+ log formats (Syslog, Apache, Nginx, JSON, Docker, Python, Java/Log4j, K8s) |
| [djm81/log_analyzer_mcp](https://github.com/djm81/log_analyzer_mcp) | ~8 | CLI + MCP server for test log summarization and unit test execution |
| [klara-research/MCP-Analyzer](https://github.com/klara-research/MCP-Analyzer) | — | Read and debug MCP protocol logs |
| [Alcyone-Labs/simple-mcp-logger](https://github.com/Alcyone-Labs/simple-mcp-logger) | — | Drop-in replacement logger that suppresses output in MCP mode |

Fato07/log-analyzer-mcp handles the widest range of formats for local debugging. klara-research/MCP-Analyzer is a meta-tool — it analyzes MCP logs themselves to debug MCP server integrations.

### Papertrail

[vovka/papertrail-mcp-server](https://github.com/vovka/papertrail-mcp-server) provides basic log search capabilities for Papertrail with rate limiting and Docker support. Community-only, minimal adoption.

## What's Missing

- **No Logstash pipeline management MCP** — the ELK stack's ingest layer has no dedicated MCP server for pipeline CRUD
- **No Fluentd/Fluent Bit MCP servers** — the CNCF log collectors have zero MCP presence
- **No official Sumo Logic MCP** — despite publishing MCP documentation
- **Elasticsearch deprecation** — Elastic is pushing toward Agent Builder, leaving a gap for self-hosted Elasticsearch users
- **No cross-platform log correlation** — no MCP server queries multiple log backends simultaneously (OpenTrace comes closest but requires log ingestion)
- **No log alerting via MCP** — you can query logs but can't create log-based alerts through most servers
- **No Papertrail/Logtail/Axiom official servers**

## The Bottom Line

**Rating: 4.0 / 5** — Strong official support from major vendors (Grafana, Splunk, Datadog, Dynatrace, AWS, Elastic, New Relic). Grafana's mcp-grafana is the clear ecosystem leader with 2,500 stars and multi-backend log querying. The category loses points for fragmentation (Splunk has 4+ competing servers), Elasticsearch's deprecation creating uncertainty, and the absence of log pipeline management (Fluentd/Logstash) and cross-platform correlation tools.

**Best for enterprise teams:** Grafana mcp-grafana (if you use Grafana) or Datadog's managed endpoint (if you use Datadog) — both provide the smoothest experience with official backing.

**Best for self-hosted/vendor-neutral:** OpenTrace offers a unique single-binary approach with 75+ tools and SQLite storage, though it requires log ingestion rather than querying existing platforms.

**Best for Splunk shops:** livehybrid/splunk-mcp (94 stars, 13 tools) or the official Splunkbase app depending on your deployment model.

---

*This review covers publicly available information as of March 2026. ChatForest researches MCP servers thoroughly through documentation, GitHub repositories, and community discussions — we do not test servers hands-on. Star counts are approximate and change over time. Always check the linked repositories for the latest status.*

**Category**: [Observability & Monitoring](/categories/observability-monitoring/)

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*


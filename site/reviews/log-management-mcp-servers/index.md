# Log Management MCP Servers — Splunk, Elasticsearch, Loki, Datadog, CloudWatch, and Beyond

> Log management MCP servers let AI agents search, analyze, and correlate logs across Splunk, Elasticsearch, Grafana Loki, Graylog, AWS CloudWatch, Datadog, Dynatrace, New Relic, Axiom, and Sumo Logic.


Logs are the ground truth of every production system — **error traces, access records, audit trails, performance data**. Log management MCP servers let AI agents search, correlate, and analyze logs across enterprise platforms without developers manually copy-pasting stack traces into chat windows or writing ad hoc queries.

The headline finding: **this is one of the strongest MCP categories**. Nearly every major log management platform has at least one MCP server — many have official ones. Grafana's mcp-grafana dominates at 2,907 stars with Loki, Elasticsearch, and CloudWatch log querying built in. Splunk has both an official Splunkbase app and active community servers. Datadog ships a managed remote MCP endpoint. The gap isn't coverage — it's fragmentation, with some platforms having 5+ competing community servers.

**April 2026 update:** Several important developments since our initial review. AWS's MCP monorepo nearly doubled to 8,864 stars with CloudWatch expanding to 11 tools. Dynatrace hit v1.8.3 with 21 tools and rapid release cadence. Axiom launched an official hosted MCP server at mcp.axiom.co. The first Fluent Bit/Fluentd MCP server appeared via OpAMP integration. Sumo Logic entered limited beta with their official MCP as part of the Dojo AI platform. Meanwhile, the AI-enthusiasts/mcp-graylog server appears to have been removed.

## The Landscape

### Grafana + Loki

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [grafana/mcp-grafana](https://github.com/grafana/mcp-grafana) | ~2,907 | Go | 60+ (5 Loki) | stdio |
| [grafana/loki-mcp](https://github.com/grafana/loki-mcp) | ~128 | Go | 1 | stdio, SSE |

**Grafana's official mcp-grafana is the most comprehensive observability MCP server available.** 2,907 stars, 343 forks, 76 open issues/PRs — heavily active development with multiple daily commits. v0.12.0 (April 23, 2026) added InfluxDB datasource support (Flux + InfluxQL), Graphite datasource support, legacy `d-solo` render mode, security fixes (reject embedded credentials, reject malformed headers), and schema token cost reduction. Covers dashboards, datasources, Prometheus, Loki, InfluxDB, Graphite, ClickHouse, CloudWatch, Elasticsearch, incidents, alerting, OnCall, annotations, and rendering.

The 5 Loki-specific tools:

| Tool | What it does |
|------|-------------|
| `query_loki_logs` | Execute LogQL queries for log and metric retrieval |
| `list_loki_label_names` | Enumerate available log labels |
| `list_loki_label_values` | Retrieve values for specific log labels |
| `query_loki_stats` | Obtain log stream statistics |
| `query_loki_patterns` | Identify detected log patterns and anomalies |

Install: `uvx mcp-grafana` with `GRAFANA_URL` and `GRAFANA_SERVICE_ACCOUNT_TOKEN` environment variables.

The dedicated **grafana/loki-mcp** (128 stars, MIT, Go) provides a single `loki_query` tool for querying Loki directly. Supports multi-tenant org IDs, SSE transport, and Docker deployment. Simpler if you only need Loki without the full Grafana stack. However, **this repo has been dormant since July 2025** (10 months) — given that mcp-grafana already includes 5 Loki tools with richer functionality, the standalone server may be effectively superseded.

Community alternatives include [tumf/grafana-loki-mcp](https://github.com/tumf/grafana-loki-mcp) (FastMCP/Python), [mo-silent/loki-mcp-server](https://github.com/mo-silent/loki-mcp-server), and [lexfrei/mcp-loki](https://github.com/lexfrei/mcp-loki) — all provide basic LogQL querying.

### Elasticsearch / ELK Stack

| Server | Stars | Language | Tools | Status |
|--------|-------|----------|-------|--------|
| [elastic/mcp-server-elasticsearch](https://github.com/elastic/mcp-server-elasticsearch) | ~648 | Rust | 5 | Deprecated |
| [cr7258/elasticsearch-mcp-server](https://github.com/cr7258/elasticsearch-mcp-server) | — | Python | — | Active |
| [awesimon/elasticsearch-mcp](https://github.com/awesimon/elasticsearch-mcp) | — | — | — | Active |

**Elastic's official MCP server is deprecated** — superseded by the Elastic Agent Builder MCP endpoint available in Elastic 9.2.0+ and Elasticsearch Serverless. The existing server (648 stars, Rust, Apache-2.0, v0.4.6) still works via Docker (`docker.elastic.co/mcp/elasticsearch`) with stdio and streamable-HTTP protocols. Last commit was October 2025; the repo will only receive critical security updates going forward.

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
| [CiscoDevNet/Splunk-MCP-Server-official](https://github.com/CiscoDevNet/Splunk-MCP-Server-official) | ~3 | — | 7+ | Splunk mgmt port |
| [livehybrid/splunk-mcp](https://github.com/livehybrid/splunk-mcp) | ~98 | Python | 14 | API token |
| [splunk/splunk-mcp-server2](https://github.com/splunk/splunk-mcp-server2) | ~31 | Python/TS | 7 | API token |
| [deslicer/mcp-for-splunk](https://github.com/deslicer/mcp-for-splunk) | ~22 | Python | 20+ | API token |

**Splunk has the most fragmented MCP ecosystem — four+ servers, each with a different approach.**

The **official Splunkbase app** (CiscoDevNet, v1.0.1, Feb 2026, beta) runs inside your Splunk instance on the management port (8089). Tools include `generate_spl` (natural language to SPL), `run_splunk_query`, `get_splunk_info`, `get_indexes`, `get_index_info`, and `get_saved_searches`. 5,029+ Splunkbase downloads with a 5-star rating. Supports Splunk 8.0-10.2. Minimal GitHub presence (3 stars) since it's distributed via Splunkbase.

The **community leader** is livehybrid/splunk-mcp (98 stars, Python, Apache-2.0). 14 tools across search, index management, KV store operations (including KVStore collections), health checks, and user management. Supports SSE transport and Docker deployment.

splunk/splunk-mcp-server2 (31 stars, MIT) adds SPL risk scoring (0-100 scale), automatic sensitive data masking, and multiple output formats (JSON, CSV, Markdown). 7 tools with a security-first approach. Low activity — single contributor, no releases published.

deslicer/mcp-for-splunk (22 stars, Apache-2.0, 374 commits) is the most actively developed Splunk MCP server. 20+ tools with 16 resources including CIM data models, 174 passing tests, AI-powered troubleshooting workflows, and natural language to SPL conversion.

### Datadog

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [datadog-labs/mcp-server](https://github.com/datadog-labs/mcp-server) | ~33 | — | 16+ | Remote HTTP |
| [winor30/mcp-server-datadog](https://github.com/winor30/mcp-server-datadog) | ~142 | TypeScript | 20 | stdio |

**Datadog offers both an official managed remote MCP server and a popular community server.**

The **official server** (datadog-labs, MIT, Preview, 33 stars — up from 10, +230%) is a managed remote endpoint at `mcp.datadoghq.com` — no self-hosting needed. Regional endpoint guidance added in April 2026. Core toolset covers logs, metrics, traces, dashboards, monitors, incidents, hosts, services, events, and notebooks. Additional opt-in toolsets for alerting, APM, Database Monitoring, Error Tracking, feature flags, LLM Observability, networking, security, software delivery, and Synthetic tests. Paginates by token budget with cursor-based continuation.

Install for Claude Code: `claude mcp add --transport http datadog https://mcp.datadoghq.com/api/unstable/mcp-server/mcp`

The **community leader** winor30/mcp-server-datadog (142 stars, TypeScript, Apache-2.0) provides 20 named tools. Development has slowed in 2026 — last feature release was v1.7.0 (October 2025), with mostly dependency bumps since then:

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
| CloudWatch MCP Server (awslabs/mcp) | ~8,864 | Python | 11 | Official monorepo |
| [awslabs/Log-Analyzer-with-MCP](https://github.com/awslabs/Log-Analyzer-with-MCP) | ~157 | Python | 5 | Official standalone |

**AWS provides two official CloudWatch log analysis servers.**

The **CloudWatch MCP Server** inside the awslabs/mcp monorepo (8,864 stars — nearly doubled from 4,700 in March) now provides **11 tools** across three categories:
- **Metrics** (4 tools): `get_metric_data`, `get_metric_metadata`, `get_recommended_metric_alarms`, `analyze_metric`
- **Alarms** (2 tools): `get_active_alarms`, `get_alarm_history`
- **Logs** (5 tools): `describe_log_groups`, `analyze_log_group`, `execute_log_insights_query`, `get_logs_insight_query_results`, `cancel_logs_insight_query`

Multi-profile support added for all tools in 2026. A separate `cloudwatch-appsignals-mcp-server` also exists in the monorepo. An RFC is in progress to add Performance Insights (Database Insights) tools. PyPI: `awslabs.cloudwatch-mcp-server`. Note: the older `cloudwatch-logs-mcp-server` package is deprecated in favor of the unified CloudWatch server.

The standalone **Log-Analyzer-with-MCP** (157 stars, Python, Apache-2.0) focuses specifically on CloudWatch Logs analysis — log group discovery, CloudWatch Logs Insights query execution, log summaries, error pattern identification, and multi-service log correlation. Now in maintenance-only mode with only dependency bumps in 2026.

### Dynatrace

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [dynatrace-oss/dynatrace-mcp](https://github.com/dynatrace-oss/dynatrace-mcp) | ~111 | TypeScript | 21 | stdio, HTTP |

**Dynatrace's official open-source MCP server bridges AI assistants to the Dynatrace observability platform.** 111 stars (up from 92), MIT license, 18 open issues. **Rapid release cadence** — v1.8.3 (April 24, 2026), with v1.8.2 (April 21) and v1.8.1 (April 15). Requires Node.js v22.10+.

Install: `npx -y @dynatrace-oss/dynatrace-mcp-server` (stdio) or `--http` for server mode.

Key tools (~21):

| Tool | What it does |
|------|-------------|
| `execute_dql` / `verify_dql` | Run and validate Dynatrace Query Language statements |
| `generate_dql_from_natural_language` / `explain_dql_in_natural_language` | Natural language ↔ DQL conversion |
| `list_problems` | Problem investigation |
| `list_vulnerabilities` | Security vulnerability data |
| `list_exceptions` | Exception tracking |
| `get_kubernetes_events` | Kubernetes event monitoring |
| `find_entity_by_name` | Entity discovery |
| `chat_with_davis_copilot` | Davis CoPilot AI interaction |
| `list_davis_analyzers` / `execute_davis_analyzer` | Davis AI analysis |
| `list_documents` / `read_document` / `create_document` | Notebooks and dashboards |
| `create_dynatrace_notebook` | Notebook creation |
| `send_event` | Transmit event data |
| `send_slack_message` / `send_email` | Notification integration |
| `create_workflow_for_notification` | Configure automation workflows |

### New Relic

| Server | Stars | Language | Tools | Status |
|--------|-------|----------|-------|--------|
| [newrelic/mcp-server](https://github.com/newrelic/mcp-server) | ~5 | — | — | Public Preview |

**New Relic's official MCP server launched in November 2025 as a Public Preview.** Still no GA announcement as of April 2026. Connects AI agents to New Relic's observability data for natural language querying of telemetry data, alert investigation, and performance analysis.

Tool categories include entity/account management, alerting/monitoring, incident response, performance analytics (golden metrics, logs, thread analysis), NRQL queries, and deployment impact assessment. Very low GitHub presence (5 stars, 1 contributor, 2 commits on main, no releases published) — the real product lives behind the New Relic platform.

Community alternatives: [cloudbring/newrelic-mcp](https://github.com/cloudbring/newrelic-mcp) (NerdGraph API integration), [ulucaydin/mcp-server-newrelic](https://github.com/ulucaydin/mcp-server-newrelic) (unofficial NerdGraph MCP).

### Graylog

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [lcaliani/graylog-mcp](https://github.com/lcaliani/graylog-mcp) | — | JavaScript | 1 | stdio |
| [mothlike/mcp_graylog](https://github.com/mothlike/mcp_graylog) | — | Python | — | stdio |
| [Pranavj17/mcp-server-graylog](https://github.com/Pranavj17/mcp-server-graylog) | — | — | — | stdio |

**Graylog has built-in MCP support** — the platform itself can act as an MCP endpoint with API token authentication. But the standalone community servers provide different integration approaches.

**Note:** The previously most-complete standalone server, AI-enthusiasts/mcp-graylog (11 tools), appears to have been removed (404 as of April 2026). The remaining community servers are more limited: [lcaliani/graylog-mcp](https://github.com/lcaliani/graylog-mcp) (JavaScript, single tool), [mothlike/mcp_graylog](https://github.com/mothlike/mcp_graylog) (Elasticsearch query syntax, statistics), and [Pranavj17/mcp-server-graylog](https://github.com/Pranavj17/mcp-server-graylog) (focused on production debugging). Graylog's built-in MCP support is now the recommended path.

### Sumo Logic

| Server | Stars | Language | Tools |
|--------|-------|----------|-------|
| [samwang0723/mcp-sumologic](https://github.com/samwang0723/mcp-sumologic) | ~10 | TypeScript | 1 |
| [vinit-devops/sumologic_mcp](https://github.com/vinit-devops/sumologic_mcp) | ~4 | Python | 37 |
| Sumo Logic Official (Dojo AI) | — | — | — |

**Sumo Logic now has an official MCP server in limited beta**, part of the "Dojo AI" platform expansion announced in early 2026. It extends Dojo AI into the agentic ecosystem, connecting customer-owned copilots, proprietary models, and third-party AI systems. Includes SOC Analyst Agent, Knowledge Agent, and Query Agent capabilities. GA planned for 2026 but no confirmed date yet.

For community options, vinit-devops/sumologic_mcp (4 stars, Python, PyPI: `sumologic-mcp-python`) stands out with 37 tools across six categories (Search & Analytics, Dashboard Management, Metrics & Monitoring, Collector & Source Management, Monitor Management, utilities). samwang0723/mcp-sumologic (10 stars, TypeScript) provides a single search tool but has been stale since February 2025.

### OpenTrace (Self-Hosted)

| Server | Stars | Language | Tools | Storage |
|--------|-------|----------|-------|---------|
| [adham90/opentrace](https://github.com/adham90/opentrace) | ~15 | Go | 13 tools (90+ actions) | SQLite |

**OpenTrace is the only self-hosted, vendor-neutral observability MCP server.** 15 stars, MIT, Go 1.25+, 407 commits (up from 308) — substantial and growing codebase despite low adoption.

13 tools with 90+ actions across 8 categories: overview/triage, log intelligence (full-text search, distributed traces, performance analysis, period comparisons), database introspection (Postgres read-only — query stats, table metrics, lock analysis, index optimization), errors (grouping, investigation, user impact), analytics/journeys, uptime/watches, agent memory (persistent notes across sessions), and settings/admin. New features include PII scrubbing, SQL validation for read-only Postgres access, automatic deploy detection via git commit hashing, and per-user auth tokens. Targets 200-500K entries/sec write throughput with ~260KB runtime memory.

Single binary deployment with SQLite storage. Docker: `docker run ghcr.io/adham90/opentrace:latest`. One-click deploy on DigitalOcean, Railway, and Render. Includes a web UI with live log streaming. Designed for small-to-medium teams that want observability without vendor lock-in.

### Axiom

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [axiomhq/mcp](https://github.com/axiomhq/mcp) | ~11 | TypeScript | multiple | Remote HTTP |

**Axiom now has an official hosted MCP server at mcp.axiom.co**, replacing the deprecated [axiomhq/mcp-server-axiom](https://github.com/axiomhq/mcp-server-axiom) (61 stars, archived March 2, 2026). The new server runs on Cloudflare Workers with 151 commits and active development (9 forks, 9 open PRs). Features CSV formatting, auto time-series binning, and smart field prioritization.

The deprecated server had 6 tools (`queryApl`, `listDatasets`, `getDatasetSchema`, `getSavedQueries`, `getMonitors`, `getMonitorsHistory`) in Go. The replacement is fully hosted — no self-hosting needed.

### Fluent Bit / Fluentd

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [mp3monster/fluent-opamp](https://github.com/mp3monster/fluent-opamp) | ~1 | Python | MCP+OpAMP | stdio |

**The first MCP server for Fluent Bit and Fluentd** — arrived via OpAMP (OpenTelemetry Agent Management Protocol) integration rather than direct log access. Implements the OpAMP specification for managing and monitoring Fluent Bit/Fluentd agents, with an MCP server layer exposing the OpAMP control plane to AI assistants. Release 0.4 (April 11, 2026). Minimal adoption so far but fills a previously complete gap.

### Logstash

| Server | Stars | Language | Tools | Status |
|--------|-------|----------|-------|--------|
| [mashhurs/logstash-mcp-server](https://github.com/mashhurs/logstash-mcp-server) | ~1 | Python | 12 | Prototype |

**The first Logstash-specific MCP server** — covers connectivity verification, node stats, pipeline performance, hot thread analysis, health assessments, and JVM diagnostics. 12 tools total. However, the author explicitly describes it as "vibe coded, AI generated and not tested properly" — treat as prototype quality only. Last commit June 2025.

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

- **Logstash pipeline management is prototype-only** — mashhurs/logstash-mcp-server exists but is self-described as untested; no production-quality Logstash CRUD MCP server yet
- **Fluent Bit/Fluentd MCP is indirect** — mp3monster/fluent-opamp manages agents via OpAMP but doesn't provide direct log access tools
- **Sumo Logic official MCP still in limited beta** — no GA date confirmed
- **Elasticsearch deprecation** — Elastic is pushing toward Agent Builder, leaving a gap for self-hosted Elasticsearch users
- **No cross-platform log correlation** — no MCP server queries multiple log backends simultaneously (OpenTrace comes closest but requires log ingestion)
- **No log alerting via MCP** — you can query logs but can't create log-based alerts through most servers
- **Graylog community coverage weakened** — AI-enthusiasts/mcp-graylog (the most complete standalone server) was removed; Graylog's built-in MCP is the main path now
- **No Papertrail/Logtail official servers** — Papertrail has a minimal community server (1 tool, dormant); no Logtail standalone MCP exists (use Better Stack official instead)

## The Bottom Line

**Rating: 4.0 / 5** — Strong official support from major vendors (Grafana, Splunk, Datadog, Dynatrace, AWS, Elastic, New Relic, Axiom). Grafana's mcp-grafana is the clear ecosystem leader at 2,907 stars with v0.12.0 adding InfluxDB and Graphite support. AWS CloudWatch nearly doubled its monorepo presence (8,864 stars) and expanded to 11 tools. Dynatrace's rapid release cadence (v1.8.3) shows strong investment. Axiom launching an official hosted MCP fills a previous gap. The category still loses points for fragmentation (Splunk has 4+ competing servers), Elasticsearch's deprecation creating uncertainty, and log pipeline management tools remaining at prototype quality.

**Best for enterprise teams:** Grafana mcp-grafana (if you use Grafana) or Datadog's managed endpoint (if you use Datadog) — both provide the smoothest experience with official backing.

**Best for self-hosted/vendor-neutral:** OpenTrace offers a unique single-binary approach with 13 tools (90+ actions) and SQLite storage, though it requires log ingestion rather than querying existing platforms.

**Best for Splunk shops:** livehybrid/splunk-mcp (98 stars, 14 tools) or the official Splunkbase app (5,029+ downloads) depending on your deployment model.

---

*This review covers publicly available information as of March 2026. ChatForest researches MCP servers thoroughly through documentation, GitHub repositories, and community discussions — we do not test servers hands-on. Star counts are approximate and change over time. Always check the linked repositories for the latest status.*

**Category**: [Observability & Monitoring](/categories/observability-monitoring/)

*This review was last edited on 2026-04-25 using Claude Opus 4.6 (Anthropic).*


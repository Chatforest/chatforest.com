# Log Management MCP Servers — Splunk, Elasticsearch, Loki, Datadog, CloudWatch, and Beyond

> Log management MCP servers let AI agents search, analyze, and correlate logs across Splunk, Elasticsearch, Grafana Loki, Graylog, AWS CloudWatch, Datadog, Dynatrace, New Relic, Axiom, and Sumo Logic.


Logs are the ground truth of every production system — **error traces, access records, audit trails, performance data**. Log management MCP servers let AI agents search, correlate, and analyze logs across enterprise platforms without developers manually copy-pasting stack traces into chat windows or writing ad hoc queries.

The headline finding: **this is one of the strongest MCP categories**. Nearly every major log management platform has at least one MCP server — many have official ones. Grafana's mcp-grafana dominates at ~3,000 stars with Loki, Elasticsearch, and CloudWatch log querying built in. Splunk has both an official Splunkbase app and active community servers. Datadog ships a managed remote MCP endpoint. The gap isn't coverage — it's fragmentation, with some platforms having 5+ competing community servers.

**May 2026 update:** A significant month for this category. SigNoz launched an official MCP server on May 1 (hosted for Cloud users, self-hosted for OSS) — the first major open-source unified observability platform to ship native MCP support. OpenObserve added built-in MCP in v0.80.0 (April 23). Grafana mcp-grafana hit v0.14.0 (May 8) crossing ~3,000 stars. Dynatrace added a dedicated `dynatrace-managed-mcp` server for self-hosted deployments. New Relic expanded from Public Preview to GA integrations with Atlassian Rovo Ops, Azure SRE Agent, and Amazon Q. Elastic's Agent Builder reached GA status, clarifying the Elasticsearch MCP path. AWS released an updated cloudwatch-mcp-server package on May 20. Sumo Logic advanced from limited beta to Preview.

## The Landscape

### Grafana + Loki

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [grafana/mcp-grafana](https://github.com/grafana/mcp-grafana) | ~3,000 | Go | 60+ (5 Loki) | stdio |
| [grafana/loki-mcp](https://github.com/grafana/loki-mcp) | ~128 | Go | 1 | stdio, SSE |

**Grafana's official mcp-grafana is the most comprehensive observability MCP server available.** ~3,000 stars, heavily active development with multiple daily commits. v0.13.1 (April 30, 2026) added VictoriaMetrics PromQL support and recording rules in datasource ruler listings. **v0.14.0 (May 8, 2026)** added Pyroscope profiling support, GCP Cloud Monitoring datasource, SSO header forwarding, and on-behalf-of authentication. Security-related fixes continue to land regularly (TLS and credential handling improvements). Grafana documentation now has an [official MCP server guide](https://grafana.com/docs/grafana/latest/developer-resources/mcp/) with Grafana Cloud MCP configuration. Covers dashboards, datasources, Prometheus, Loki, InfluxDB, Graphite, ClickHouse, GCP Cloud Monitoring, Pyroscope, CloudWatch, Elasticsearch, incidents, alerting, OnCall, annotations, and rendering.

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

**Elastic's path is now clear: the deprecated community server gives way to the officially GA Agent Builder MCP.** Elastic announced general availability of Agent Builder in 2026, with native MCP and A2A protocol support. The Agent Builder MCP server is the recommended approach for Elastic 9.2+ and Elasticsearch Serverless, providing access to built-in and custom tools through a standardized MCP interface. Integrations with Microsoft Foundry, Azure SRE Agent, and third-party agents (Claude Desktop, Cursor, LangChain) are confirmed.

The deprecated standalone server (648 stars, Rust, Apache-2.0, v0.4.6) still works via Docker (`docker.elastic.co/mcp/elasticsearch`) with stdio and streamable-HTTP. Last commit October 2025; critical security updates only.

5 tools in the standalone server (before deprecation):

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

**Splunk has the most fragmented MCP ecosystem — four+ servers, each with a different approach.** Splunk launched its AI GA in 2026 with notable security enhancements: required encrypted tokens, rotating encryption keys, and granular admin controls to enable or disable specific tools server-side.

The **official Splunkbase app** (CiscoDevNet, v1.0.1, Feb 2026, GA in 2026) runs inside your Splunk instance on the management port (8089). Tools include `generate_spl` (natural language to SPL), `run_splunk_query`, `get_splunk_info`, `get_indexes`, `get_index_info`, and `get_saved_searches`. 5,029+ Splunkbase downloads with a 5-star rating. Supports Splunk 8.0-10.2. Minimal GitHub presence (3 stars) since it's distributed via Splunkbase.

The **community leader** is livehybrid/splunk-mcp (~93 stars, Python, Apache-2.0). 14 tools across search, index management, KV store operations (including KVStore collections), health checks, and user management. Supports SSE transport and Docker deployment.

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
| [dynatrace-oss/dynatrace-mcp](https://github.com/dynatrace-oss/dynatrace-mcp) | ~173 | TypeScript | 21 | stdio, HTTP |
| [dynatrace-oss/dynatrace-managed-mcp](https://github.com/dynatrace-oss/dynatrace-managed-mcp) | — | TypeScript | — | stdio, HTTP/SSE |

**Dynatrace now ships two official MCP servers.** The SaaS server (dynatrace-mcp) hit 173 stars (up from 111) with continued rapid release cadence through May 2026. Ongoing development; Azure SRE Agent integration confirmed. Requires Node.js v22.10+.

**NEW: dynatrace-oss/dynatrace-managed-mcp** — a dedicated MCP server for **Dynatrace Managed** (self-hosted) deployments, filling a gap previously noted in our review. Supports multiple environments via JSON or YAML configuration, natural language querying of problems, logs, and events, and both local and remote (HTTP/SSE) connection modes. Works with Claude, Cursor, VS Code, GitHub Copilot, Windsurf, Kiro, and ChatGPT.

Install (SaaS): `npx -y @dynatrace-oss/dynatrace-mcp-server` (stdio) or `--http` for server mode.

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

**New Relic's MCP server is expanding rapidly via platform integrations while its core GitHub server remains in Public Preview.** The real story in May 2026 is the ecosystem expansion:

- **Atlassian Rovo Ops GA** (February 23, 2026) — New Relic MCP went GA as a Rovo Ops integration, enabling natural language observability queries inside Jira Service Management and Confluence.
- **Azure SRE Agent integration** (April 29, 2026) — Microsoft added a native New Relic connector in the Azure SRE Agent portal for AI-assisted incident response.
- **Amazon Q integration** (May 5, 2026) — AWS's enterprise AI assistant can now connect to New Relic via MCP for production observability.

The pattern is clear: New Relic is prioritizing integration partnerships over self-service GitHub releases. The GitHub repo remains at low star count (5 stars, minimal commits), with the actual product living behind the New Relic platform. Tool categories include entity/account management, alerting/monitoring, incident response, performance analytics (golden metrics, logs, thread analysis), NRQL queries, and deployment impact assessment.

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

**Sumo Logic's official MCP server advanced from limited beta to Preview** (March 2026), part of the Dojo AI platform. The broader Dojo AI expansion has been significant this spring:

- **Query Agent** (GA) — converts intent into precise Sumo Logic searches, eliminating complex query writing
- **Knowledge Agent** (GA) — answers product questions using official documentation inside the workflow
- **SOC Analyst Agent** (expanded March 23, 2026) — now recommends specific remediation actions, not just alerts; intent is to turn SIEM into a decision engine
- **MCP Server** (Preview) — extends Dojo AI across tools so product boundaries don't become process boundaries

The MCP server connects customer-owned copilots, proprietary models, and third-party AI systems to Sumo Logic's scale and security. GA timeline not yet confirmed.

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

### SigNoz

| Server | Stars | Language | Transport | Hosting |
|--------|-------|----------|-----------|---------|
| [SigNoz/signoz-mcp-server](https://github.com/SigNoz/signoz-mcp-server) | ~86 | Go | stdio | Hosted (Cloud) + self-hosted |

**NEW (May 1, 2026): SigNoz launched an official MCP server** — the first major open-source unified observability platform (logs + metrics + traces) to ship native MCP support. Hosted automatically for all SigNoz Cloud users with zero configuration. Self-hosted teams can run the open-source server themselves.

Capabilities: natural language log search and filtering (no query syntax required), trace reconstruction from trace IDs, pre/post-deployment metric comparisons for regression detection, alert management with state filtering, and dashboard querying. Works with Claude Code, Cursor, Codex, Gemini CLI, and any MCP-compatible agent.

SigNoz is notable because it covers logs, metrics, and traces in a single server — similar to Grafana's mcp-grafana breadth but as a dedicated observability platform rather than a visualization layer.

### OpenObserve

**OpenObserve v0.80.0 (April 23, 2026) added native MCP support** — upgraded to the 2025-11-25 MCP specification, with expanded RBAC covering report folders, incidents, and log patterns. The built-in MCP makes querying logs, metrics, and traces available to any MCP-compatible agent without a separate server. OpenObserve's MCP roadmap targets gateway patterns, SSO-integrated auth, and audit trails for enterprise readiness.

Community servers:
- [mdfranz/openobserve-oss-mcp](https://github.com/mdfranz/openobserve-oss-mcp) — read-only query MCP for local OpenObserve instances
- [alilxxey/openobserve-community-mcp](https://github.com/alilxxey/openobserve-community-mcp) — stdio MCP using the standard REST API (updated March 2026)

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
- **Sumo Logic official MCP still in Preview** — advanced from limited beta but GA date not yet confirmed
- **Elasticsearch path requires 9.2+** — Elastic's GA Agent Builder MCP clarifies direction, but self-hosted users on older versions remain in limbo with the deprecated standalone server
- **No cross-platform log correlation** — no MCP server queries multiple log backends simultaneously (OpenTrace comes closest but requires log ingestion)
- **No log alerting via MCP** — you can query logs but can't create log-based alerts through most servers
- **Graylog community coverage weakened** — AI-enthusiasts/mcp-graylog (the most complete standalone server) was removed; Graylog's built-in MCP is the main path now
- **No Papertrail/Logtail official servers** — Papertrail has a minimal community server (1 tool, dormant); no Logtail standalone MCP exists (use Better Stack official instead)

## The Bottom Line

**Rating: 4.5 / 5** — This category has matured meaningfully in May 2026. SigNoz's official MCP launch adds the first full-stack open-source observability platform (logs + metrics + traces) to the category. OpenObserve added built-in MCP support. Elastic's Agent Builder reaching GA resolves the Elasticsearch uncertainty gap — the deprecation created a clear upgrade path rather than just a dead end. New Relic's integration partnerships (Atlassian, Azure, AWS) show a platform-first strategy that's working. Dynatrace now covers both SaaS and Managed deployments with dedicated servers. Grafana mcp-grafana crossed 3,000 stars with v0.14.0 adding Pyroscope and GCP Cloud Monitoring. Remaining weaknesses: Splunk fragmentation (4+ competing servers), log pipeline management at prototype quality, and no cross-platform correlation.

**Best for enterprise teams:** Grafana mcp-grafana (if you use Grafana) or Datadog's managed endpoint (if you use Datadog) — both provide the smoothest experience with official backing.

**Best for open-source observability:** SigNoz's new official MCP server (hosted free for Cloud users) is the fastest path to AI-assisted log + trace + metric querying in a unified platform.

**Best for self-hosted/vendor-neutral:** OpenTrace offers a unique single-binary approach with 13 tools (90+ actions) and SQLite storage, though it requires log ingestion rather than querying existing platforms.

**Best for Splunk shops:** livehybrid/splunk-mcp (~93 stars, 14 tools) or the official Splunkbase app (5,029+ downloads) depending on your deployment model.

---

*This review covers publicly available information as of May 2026. ChatForest researches MCP servers thoroughly through documentation, GitHub repositories, and community discussions — we do not test servers hands-on. Star counts are approximate and change over time. Always check the linked repositories for the latest status.*

**Category**: [Observability & Monitoring](/categories/observability-monitoring/)

*This review was last edited on 2026-05-21 using Claude Sonnet 4.6 (Anthropic).*


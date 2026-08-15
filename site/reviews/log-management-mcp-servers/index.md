# Log Management MCP Servers — Splunk, Elasticsearch, Loki, Datadog, CloudWatch, and Beyond

> Log management MCP servers let AI agents search, analyze, and correlate logs across Splunk, Elasticsearch, Grafana Loki, Graylog, AWS CloudWatch, Datadog, Dynatrace, New Relic, Axiom, and Sumo Logic.


Logs are the ground truth of every production system — **error traces, access records, audit trails, performance data**. Log management MCP servers let AI agents search, correlate, and analyze logs across enterprise platforms without developers manually copy-pasting stack traces into chat windows or writing ad hoc queries.

The headline finding: **this is one of the strongest MCP categories**. Nearly every major log management platform has at least one MCP server — many have official ones. Grafana's mcp-grafana dominates at ~3,350 stars with Loki, Elasticsearch, and CloudWatch log querying built in. Splunk has both an official Splunkbase app and active community servers. Datadog ships a managed remote MCP endpoint. The gap isn't coverage — it's fragmentation, with some platforms having 5+ competing community servers.

**May 2026 update:** A significant month for this category. SigNoz launched an official MCP server on May 1 (hosted for Cloud users, self-hosted for OSS), covering logs, metrics, and traces in one open-source platform. OpenObserve added built-in MCP in v0.80.0 (April 23). Grafana mcp-grafana hit v0.14.0 (May 8) crossing ~3,000 stars. Dynatrace added a dedicated `dynatrace-managed-mcp` server for self-hosted deployments. New Relic expanded from Public Preview to GA integrations with Atlassian Rovo Ops, Azure SRE Agent, and Amazon Q. Elastic's Agent Builder reached GA status, clarifying the Elasticsearch MCP path. AWS released an updated cloudwatch-mcp-server package on May 20. Sumo Logic advanced from limited beta to Preview.

**August 2026 re-audit — several things have shifted since May:** Grafana mcp-grafana crossed 1.0 (v1.0.0 July 28, v1.1.0 August 10) and now sits at ~3,350 stars. Dynatrace **deprecated** its original SaaS `dynatrace-mcp` server (final release v2.1.2), splitting the replacement into Dynatrace-for-AI + `dtctl` for local dev and a hosted Dynatrace Remote MCP Server for agent-to-agent use; `dynatrace-managed-mcp` is unaffected. livehybrid/splunk-mcp, previously the Splunk community leader, was **archived** on June 20, 2026 in favor of Splunk's official first-party app (now v1.3.1, 19,759+ Splunkbase downloads). The CloudWatch MCP Server grew from 11 to 16 tools, adding a PromQL category. OpenObserve shipped v0.91.0 (June 23) adding AI-agent observability and MCP-based agent tracing on top of the v0.80.0 baseline in the May note. Datadog's install endpoint moved from an unstable path to a stable `/v1/mcp` URL.

## The Landscape

### Grafana + Loki

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [grafana/mcp-grafana](https://github.com/grafana/mcp-grafana) | ~3,350 | Go | 60+ (5 Loki) | stdio |
| [grafana/loki-mcp](https://github.com/grafana/loki-mcp) | ~164 | Go | 1 | stdio, SSE |

**Grafana's official mcp-grafana is the most comprehensive observability MCP server available.** ~3,350 stars as of August 2026, heavily active development with multiple daily commits. **[v0.14.0 (May 8, 2026)](https://github.com/grafana/mcp-grafana/releases/tag/v0.14.0)** added a generic API request tool for arbitrary Grafana API calls and OpenSearch datasource support. Development has since accelerated further: the project crossed the 1.0 line with **[v1.0.0 (July 28, 2026)](https://github.com/grafana/mcp-grafana/releases/tag/v1.0.0)**, adding Agent Observability conversation management and inline panel viewing, and **[v1.1.0 (August 10, 2026)](https://github.com/grafana/mcp-grafana/releases/tag/v1.1.0)** added bearer-token authentication and Grafana Assistant integration. Security-related fixes continue to land regularly (recent releases added DNS-rebinding protection and credential binding to configured Grafana URLs). Grafana documentation now has an [official MCP server guide](https://grafana.com/docs/grafana/latest/developer-resources/mcp/) with Grafana Cloud MCP configuration. Covers dashboards, datasources, Prometheus, Loki, InfluxDB, Graphite, ClickHouse, GCP Cloud Monitoring, Pyroscope, CloudWatch, Elasticsearch, incidents, alerting, OnCall, annotations, and rendering.

The 5 Loki-specific tools:

| Tool | What it does |
|------|-------------|
| `query_loki_logs` | Execute LogQL queries for log and metric retrieval |
| `list_loki_label_names` | Enumerate available log labels |
| `list_loki_label_values` | Retrieve values for specific log labels |
| `query_loki_stats` | Obtain log stream statistics |
| `query_loki_patterns` | Identify detected log patterns and anomalies |

Install: `uvx mcp-grafana` with `GRAFANA_URL` and `GRAFANA_SERVICE_ACCOUNT_TOKEN` environment variables.

The dedicated **[grafana/loki-mcp](https://github.com/grafana/loki-mcp)** (164 stars, MIT, Go) provides a single `loki_query` tool for querying Loki directly. Supports multi-tenant org IDs, SSE transport, and Docker deployment. Simpler if you only need Loki without the full Grafana stack. As of August 2026 the repo is active again (recent commits, open issues and PRs) after a quiet period — mcp-grafana still includes 5 Loki-specific tools with richer functionality, so loki-mcp remains the choice mainly for teams that want Loki-only scope without the full Grafana stack dependency.

Community alternatives include [tumf/grafana-loki-mcp](https://github.com/tumf/grafana-loki-mcp) (FastMCP/Python), [mo-silent/loki-mcp-server](https://github.com/mo-silent/loki-mcp-server), and [lexfrei/mcp-loki](https://github.com/lexfrei/mcp-loki) — all provide basic LogQL querying.

### Elasticsearch / ELK Stack

| Server | Stars | Language | Tools | Status |
|--------|-------|----------|-------|--------|
| [elastic/mcp-server-elasticsearch](https://github.com/elastic/mcp-server-elasticsearch) | ~704 | Rust | 5 | Deprecated |
| [cr7258/elasticsearch-mcp-server](https://github.com/cr7258/elasticsearch-mcp-server) | ~303 | Python | — | Active |
| [awesimon/elasticsearch-mcp](https://github.com/awesimon/elasticsearch-mcp) | ~23 | — | — | Stale (last push Aug 2025) |

**Elastic's path is now clear: the deprecated community server gives way to the officially GA Agent Builder MCP.** Elastic [announced general availability of Agent Builder on January 22, 2026](https://www.elastic.co/search-labs/blog/agent-builder-elastic-ga), with native MCP and A2A protocol support (GA in Elastic Cloud Serverless and in the 9.3 Stack release; external MCP connection is preview). The Agent Builder MCP server is the recommended approach for Elastic 9.2+ and Elasticsearch Serverless, providing access to built-in and custom tools through a standardized MCP interface. Integrations with [Microsoft Foundry](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/announcing-elastic-mcp-server-in-microsoft-foundry-tool-catalog/4469302), [Azure SRE Agent](https://techcommunity.microsoft.com/blog/appsonazureblog/get-started-with-elasticsearch-mcp-server-in-azure-sre-agent/4492896), and third-party agents (Claude Desktop, Cursor) are confirmed.

The deprecated standalone server (704 stars, Rust, Apache-2.0, [v0.4.6](https://github.com/elastic/mcp-server-elasticsearch/releases/tag/v0.4.6)) still works via Docker (`docker.elastic.co/mcp/elasticsearch`) with stdio and streamable-HTTP. Last release October 2025 (v0.4.6, which added the deprecation notice); critical security updates only since.

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
| [CiscoDevNet/Splunk-MCP-Server-official](https://github.com/CiscoDevNet/Splunk-MCP-Server-official) | ~4 | — | 7+ | Splunk mgmt port |
| [livehybrid/splunk-mcp](https://github.com/livehybrid/splunk-mcp) | ~107 | Python | 14 | API token |
| [splunk/splunk-mcp-server2](https://github.com/splunk/splunk-mcp-server2) | ~37 | Python/TS | 7 | API token |
| [deslicer/mcp-for-splunk](https://github.com/deslicer/mcp-for-splunk) | ~27 | Python | 20+ | API token |

**Splunk has the most fragmented MCP ecosystem — four+ servers, each with a different approach.** Splunk's [official MCP Server for Splunk platform](https://community.splunk.com/t5/Product-News-Announcements/What-s-New-in-Splunk-AI-Vol-01-MCP-Hosted-Models-amp-SPL-AI/ba-p/758587) shipped with notable security enhancements, [documented by Splunk](https://help.splunk.com/en/splunk-cloud-platform/mcp-server-for-splunk-platform/1.3/about-mcp-server-for-splunk-platform): required encrypted tokens (usable only for MCP auth, not direct Splunk API calls), rotating/invalidatable encryption keys, and granular admin controls to enable or disable specific tools server-side.

**Update, August 2026 — the community MCP landscape here has consolidated around the official app.** livehybrid/splunk-mcp, formerly the community leader, was **[archived by its owner on June 20, 2026](https://github.com/livehybrid/splunk-mcp)**; its README states Splunk now ships "a first-party, fully supported MCP server that has grown beyond what this community project provides" and points users to the official app. It's still readable (107 stars, Python, Apache-2.0, 14 tools across search, index management, KV store operations, health checks, and user management) but should be treated as historical/reference-only, not an active choice for new deployments.

The **[official Splunkbase app](https://splunkbase.splunk.com/app/7931)** (CiscoDevNet) runs inside your Splunk instance on the management port (8089). Tools include `generate_spl` (natural language to SPL), `run_splunk_query`, `get_splunk_info`, `get_indexes`, `get_index_info`, and `get_saved_searches`. As of August 2026 it's at version 1.3.1 (released August 3, 2026) with 19,759+ Splunkbase downloads and a 5-star rating (15 ratings), supporting Splunk Enterprise/Cloud versions 9.3-10.5. Minimal GitHub presence (4 stars) since it's distributed via Splunkbase.

splunk/splunk-mcp-server2 (37 stars, MIT) adds SPL risk scoring (0-100 scale), automatic sensitive data masking, and multiple output formats (JSON, CSV, Markdown). 7 tools with a security-first approach. Low activity — single contributor, no releases published since mid-2025.

deslicer/mcp-for-splunk (27 stars, Apache-2.0) is the most actively developed independent Splunk MCP server, with commits as recently as mid-August 2026. 20+ tools with 16 resources including CIM data models, AI-powered troubleshooting workflows, and natural language to SPL conversion.

### Datadog

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [datadog-labs/mcp-server](https://github.com/datadog-labs/mcp-server) | ~43 | — | 16+ | Remote HTTP |
| [winor30/mcp-server-datadog](https://github.com/winor30/mcp-server-datadog) | ~143 | TypeScript | 20 | stdio |

**Datadog offers both an official managed remote MCP server and a popular community server.**

The **[official server](https://docs.datadoghq.com/mcp_server/)** (datadog-labs, MIT, 43 stars as of August 2026) is a managed remote endpoint at `mcp.datadoghq.com` — no self-hosting needed. Core toolset covers logs, metrics, traces, dashboards, monitors, incidents, hosts, services, events, and notebooks. Additional opt-in toolsets for alerting, APM, Database Monitoring, Error Tracking, feature flags, LLM Observability, networking, security, software delivery, and Synthetic tests. Paginates by token budget with cursor-based continuation.

Install for Claude Code: `claude mcp add --transport http datadog https://mcp.datadoghq.com/v1/mcp` (the endpoint moved from an `/api/unstable/` path to this stable `/v1/mcp` path in 2026 — update existing configs that still point at the old unstable URL).

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
| [CloudWatch MCP Server (awslabs/mcp)](https://github.com/awslabs/mcp/tree/main/src/cloudwatch-mcp-server) | ~9,600 | Python | 16 | Official monorepo |
| [awslabs/Log-Analyzer-with-MCP](https://github.com/awslabs/Log-Analyzer-with-MCP) | ~167 | Python | 5 | Official standalone |

**AWS provides two official CloudWatch log analysis servers.**

The **CloudWatch MCP Server** inside the awslabs/mcp monorepo (~9,600 stars as of August 2026, up from ~4,700 in March) has grown to **16 tools** across four categories:
- **Metrics** (4 tools): `get_metric_data`, `get_metric_metadata`, `get_recommended_metric_alarms`, `analyze_metric`
- **PromQL** (5 tools, added since the original review): `execute_promql_query`, `execute_promql_range_query`, `get_promql_label_values`, `get_promql_series`, `get_promql_labels`
- **Alarms** (2 tools): `get_active_alarms`, `get_alarm_history`
- **Logs** (5 tools): `describe_log_groups`, `analyze_log_group`, `execute_log_insights_query`, `execute_cwl_insights_batch`, `get_logs_insight_query_results`, `cancel_logs_insight_query`

A separate `cloudwatch-appsignals-mcp-server` also exists in the monorepo. PyPI: [`awslabs.cloudwatch-mcp-server`](https://pypi.org/project/awslabs.cloudwatch-mcp-server/) (latest 0.1.8, August 10, 2026). Note: the older `cloudwatch-logs-mcp-server` package is deprecated in favor of the unified CloudWatch server.

The standalone **Log-Analyzer-with-MCP** (167 stars, Python, Apache-2.0) focuses specifically on CloudWatch Logs analysis — log group discovery, CloudWatch Logs Insights query execution, log summaries, error pattern identification, and multi-service log correlation.

### Dynatrace

| Server | Stars | Language | Tools | Transport | Status |
|--------|-------|----------|-------|-----------|--------|
| [dynatrace-oss/dynatrace-mcp](https://github.com/dynatrace-oss/dynatrace-mcp) | ~134 | TypeScript | 21 | stdio, HTTP | **Deprecated** |
| [dynatrace-oss/dynatrace-managed-mcp](https://github.com/dynatrace-oss/dynatrace-managed-mcp) | ~27 | TypeScript | — | stdio, HTTP/SSE | Active |

**Update, August 2026 — Dynatrace has restructured its MCP offering since this review was written.** The original SaaS local server, **dynatrace-oss/dynatrace-mcp**, is now **[deprecated](https://github.com/dynatrace-oss/dynatrace-mcp)**: "Version 2.1.2 was the final release — no further updates will be made." (134 stars at time of audit.) Dynatrace's migration guidance splits the replacement by use case:
- **Local development** (VS Code, IntelliJ, Claude Code, Cursor, etc.): [Dynatrace-for-AI](https://github.com/Dynatrace/dynatrace-for-ai/) combined with [`dtctl`](https://github.com/dynatrace-oss/dtctl).
- **Agent-to-agent / remote scenarios** (Atlassian Rovo, GitHub Coding Agent, Azure SRE Agent, etc.): the hosted **[Dynatrace Remote MCP Server](https://www.dynatrace.com/hub/detail/dynatrace-mcp-server/)** ("no local setup"), reachable via the platform endpoint documented at [docs.dynatrace.com](https://docs.dynatrace.com/docs/dynatrace-intelligence/dynatrace-mcp).

**dynatrace-oss/dynatrace-managed-mcp** remains active and unaffected by the above — it's the dedicated MCP server for **Dynatrace Managed** (self-hosted) deployments, filling a gap previously noted in our review. Supports multiple environments via JSON or YAML configuration, natural language querying of problems, logs, and events, and both local and remote (HTTP/SSE) connection modes. Works with Claude, Cursor, VS Code, GitHub Copilot, Windsurf, Kiro, and ChatGPT.

The tools below reflect the now-final v2.1.2 release of dynatrace-mcp; new SaaS deployments should follow the migration paths above instead of installing this package directly.

Key tools (~21, dynatrace-mcp v2.1.2 — deprecated):

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
| [newrelic/mcp-server](https://github.com/newrelic/mcp-server) | ~7 | — | — | Public Preview |

**New Relic's MCP server is expanding rapidly via platform integrations while its core GitHub server remains in Public Preview.** The real story in 2026 is the ecosystem expansion:

- **[Atlassian Rovo Ops GA](https://community.atlassian.com/forums/Jira-Service-Management-articles/Announcing-GA-of-New-Relic-MCP-for-Rovo-Ops-Bring-observability/ba-p/3195727)** (February 23, 2026) — New Relic MCP went GA as a Rovo Ops integration, enabling natural language observability queries inside Jira Service Management and Confluence.
- **[Azure SRE Agent integration](https://www.businesswire.com/news/home/20260602845055/en/New-Relic-Celebrates-Strategic-Partnership-with-Microsoft-at-Build-2026)** (June 2026) — Microsoft announced a native New Relic connector in the Azure SRE Agent portal for AI-assisted incident response at Microsoft Build 2026.
- **[Amazon Q / AWS integration](https://newrelic.com/press-release/aws-reinvent-2025)** (announced at AWS re:Invent, December 2025; [second source](https://www.businesswire.com/news/home/20251202302253/en/New-Relic-Announces-Integrations-with-AWS-to-Accelerate-AI-Driven-Business-by-Predicting-Preventing-and-Orchestrating-Issues)) — New Relic's MCP server connects to AWS DevOps Agent and Amazon Quick Suite, bringing the Amazon Q enterprise-data index into New Relic AI for incident root-cause work.

The pattern is clear: New Relic is prioritizing integration partnerships over self-service GitHub releases. The GitHub repo remains at low star count (~7 stars, minimal commits), with the actual product living behind the New Relic platform. Tool categories include entity/account management, alerting/monitoring, incident response, performance analytics (golden metrics, logs, thread analysis), NRQL queries, and deployment impact assessment.

Community alternatives: [cloudbring/newrelic-mcp](https://github.com/cloudbring/newrelic-mcp) (NerdGraph API integration), [ulucaydin/mcp-server-newrelic](https://github.com/ulucaydin/mcp-server-newrelic) (unofficial NerdGraph MCP).

### Graylog

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [lcaliani/graylog-mcp](https://github.com/lcaliani/graylog-mcp) | ~9 | JavaScript | 1 | stdio |
| [mothlike/mcp_graylog](https://github.com/mothlike/mcp_graylog) | ~10 | Python | — | stdio |
| [Pranavj17/mcp-server-graylog](https://github.com/Pranavj17/mcp-server-graylog) | ~6 | — | — | stdio |

**Graylog has built-in MCP support** — the platform itself can act as an MCP endpoint with API token authentication. But the standalone community servers provide different integration approaches.

**Note:** The previously most-complete standalone server, AI-enthusiasts/mcp-graylog (11 tools), appears to have been removed (404 as of April 2026). The remaining community servers are more limited: [lcaliani/graylog-mcp](https://github.com/lcaliani/graylog-mcp) (JavaScript, single tool), [mothlike/mcp_graylog](https://github.com/mothlike/mcp_graylog) (Elasticsearch query syntax, statistics), and [Pranavj17/mcp-server-graylog](https://github.com/Pranavj17/mcp-server-graylog) (focused on production debugging). Graylog's built-in MCP support is now the recommended path.

### Sumo Logic

| Server | Stars | Language | Tools |
|--------|-------|----------|-------|
| [samwang0723/mcp-sumologic](https://github.com/samwang0723/mcp-sumologic) | ~11 | TypeScript | 1 |
| [vinit-devops/sumologic_mcp](https://github.com/vinit-devops/sumologic_mcp) | ~5 | Python | 37 |
| Sumo Logic Official (Dojo AI) | — | — | — |

**Sumo Logic's official MCP server advanced from limited beta to Preview** (March 2026), part of the Dojo AI platform. The broader Dojo AI expansion has been significant, per Sumo Logic's own announcements:

- **[Query Agent](https://www.sumologic.com/solutions/dojo-ai)** (GA) — converts intent into precise Sumo Logic searches, eliminating complex query writing
- **Knowledge Agent** (GA) — answers product questions using official documentation inside the workflow
- **[SOC Analyst Agent](https://www.prnewswire.com/news-releases/sumo-logic-extends-soc-analyst-agent-to-recommend-remediation-actions-accelerating-and-enhancing-threat-detection-investigation-and-response-302721762.html)** (expanded March 23, 2026 to recommend specific remediation actions, not just alerts) has since reached **general availability** per Sumo Logic's Dojo AI product page — intent is to turn SIEM into a decision engine
- **MCP Server** (Preview as of August 2026) — extends Dojo AI across tools so product boundaries don't become process boundaries

The MCP server connects customer-owned copilots, proprietary models, and third-party AI systems to Sumo Logic's scale and security. GA timeline not yet confirmed.

For community options, vinit-devops/sumologic_mcp (5 stars, Python, PyPI: `sumologic-mcp-python`) stands out with 37 tools across six categories (Search & Analytics, Dashboard Management, Metrics & Monitoring, Collector & Source Management, Monitor Management, utilities); last pushed October 2025. samwang0723/mcp-sumologic (11 stars, TypeScript) provides a single search tool; last pushed March 2026.

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
| Axiom MCP Server ([docs](https://axiom.co/docs/console/intelligence/mcp-server)) | — | TypeScript | multiple | Remote HTTP |

**Axiom now has an official hosted MCP server at [mcp.axiom.co](https://axiom.co/docs/console/intelligence/mcp-server)**, replacing the deprecated [axiomhq/mcp-server-axiom](https://github.com/axiomhq/mcp-server-axiom) (60 stars, archived March 2, 2026 — its README now reads "This repository is deprecated and no longer maintained" and points users to `mcp.axiom.co`). **Correction, August 2026:** the source repo previously linked here (`github.com/axiomhq/mcp`) no longer resolves (404) and is not listed among Axiom's public repositories — it appears to have been made private or renamed since this review was written, so we can no longer verify commit/fork/PR counts for it independently. The hosted endpoint itself is confirmed live and current via Axiom's own docs.

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
| [SigNoz/signoz-mcp-server](https://github.com/SigNoz/signoz-mcp-server) | ~114 | Go | stdio | Hosted (Cloud) + self-hosted |

**[May 1, 2026](https://signoz.io/changelog/2026-05-01-introducing-the-signoz-mcp-server-r5iwnkpxtsz88akwt6abqddn/): SigNoz launched an official MCP server** covering logs, metrics, and traces in one open-source platform. Hosted automatically for all SigNoz Cloud users with zero configuration. Self-hosted teams can run the open-source server themselves. (Our earlier draft called this "the first major open-source unified observability platform to ship native MCP support" — we could not find a primary source substantiating that "first" claim, so we've removed it; the factual launch details above are confirmed directly by SigNoz's own changelog.)

Capabilities: natural language log search and filtering (no query syntax required), trace reconstruction from trace IDs, pre/post-deployment metric comparisons for regression detection, alert management with state filtering, and dashboard querying. Works with Claude Code, Cursor, Codex, Gemini CLI, and any MCP-compatible agent.

SigNoz is notable because it covers logs, metrics, and traces in a single server — similar to Grafana's mcp-grafana breadth but as a dedicated observability platform rather than a visualization layer.

### OpenObserve

**OpenObserve v0.80.0 (April 23, 2026) added native MCP support** — upgraded to the 2025-11-25 MCP specification, with expanded RBAC covering report folders, incidents, and log patterns. The built-in MCP makes querying logs, metrics, and traces available to any MCP-compatible agent without a separate server.

**Update, August 2026:** OpenObserve has continued shipping on this front. **[v0.91.0 (June 23, 2026)](https://openobserve.ai/whats-new/2026-06-23-v0910-release/)** added AI-agent observability — MCP protocol support plus agent traces that "correlate LLM calls, tool calls, and multi step reasoning inside the same trace view that backend services use." OpenObserve's [MCP server documentation](https://openobserve.ai/mcp-server/) describes ongoing work on gateway patterns and RBAC that spans both the MCP gateway layer and OpenObserve's native stream/query-level permissions.

Community servers:
- [mdfranz/openobserve-oss-mcp](https://github.com/mdfranz/openobserve-oss-mcp) — read-only query MCP for local OpenObserve instances
- [alilxxey/openobserve-community-mcp](https://github.com/alilxxey/openobserve-community-mcp) — stdio MCP using the standard REST API (updated March 2026)

### Standalone Log Analyzers

Several MCP servers focus on local log file analysis rather than connecting to a platform:

| Server | Stars | Focus |
|--------|-------|-------|
| [Fato07/log-analyzer-mcp](https://github.com/Fato07/log-analyzer-mcp) | — | Parse 9+ log formats (Syslog, Apache, Nginx, JSON, Docker, Python, Java/Log4j, K8s) |
| [djm81/log_analyzer_mcp](https://github.com/djm81/log_analyzer_mcp) | ~12 | CLI + MCP server for test log summarization and unit test execution |
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

**Rating: 4.5 / 5** — This category has matured meaningfully since this review was first written, and continued shifting through the August 2026 re-audit. SigNoz's official MCP launch adds a full-stack open-source observability platform (logs + metrics + traces) to the category. OpenObserve added built-in MCP support and has since expanded it further (v0.91.0, June 2026). Elastic's Agent Builder reaching GA resolves the Elasticsearch uncertainty gap — the deprecation created a clear upgrade path rather than just a dead end. New Relic's integration partnerships (Atlassian, Azure, AWS) show a platform-first strategy that's working. Dynatrace's coverage of both SaaS and Managed deployments has consolidated: the original SaaS local server is now deprecated in favor of a hosted Remote MCP Server plus Dynatrace-for-AI, while the Managed server continues unchanged. Grafana mcp-grafana crossed 3,000 stars and, more recently, crossed v1.0 (now v1.1.0). Splunk's community MCP fragmentation has started resolving in the official app's favor — the former community leader (livehybrid/splunk-mcp) was archived in June 2026. Remaining weaknesses: log pipeline management at prototype quality and no cross-platform correlation.

**Best for enterprise teams:** Grafana mcp-grafana (if you use Grafana) or Datadog's managed endpoint (if you use Datadog) — both provide the smoothest experience with official backing.

**Best for open-source observability:** SigNoz's official MCP server (hosted free for Cloud users) is a fast path to AI-assisted log + trace + metric querying in a unified platform.

**Best for self-hosted/vendor-neutral:** OpenTrace offers a unique single-binary approach with 13 tools (90+ actions) and SQLite storage, though it requires log ingestion rather than querying existing platforms.

**Best for Splunk shops:** the official [Splunkbase app](https://splunkbase.splunk.com/app/7931) (v1.3.1, 19,759+ downloads) — now the clear default since livehybrid/splunk-mcp, the former community leader, was archived in June 2026 in favor of Splunk's first-party server.

---

*This review covers publicly available information; a claim-level citation and staleness audit was last performed 2026-08-15. ChatForest researches MCP servers thoroughly through documentation, GitHub repositories, and community discussions — we do not test servers hands-on. Star counts are approximate and change over time. Always check the linked repositories for the latest status.*

**Category**: [Observability & Monitoring](/categories/observability-monitoring/)

*This review was last edited on 2026-05-21 using Claude Sonnet 4.6 (Anthropic).*


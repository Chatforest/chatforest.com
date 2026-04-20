# Best Observability MCP Servers (2026) — 40+ Compared

> Grafana, Datadog, Sentry, New Relic, Prometheus, and 35+ more observability MCP servers compared. See which ones are worth installing and which to skip.


Monitoring and observability is the most vendor-invested category in the MCP ecosystem. Every major platform — [Datadog](https://www.datadoghq.com/about/latest-news/press-releases/datadog-launches-mcp-server/), [Grafana](https://github.com/grafana/mcp-grafana), [Sentry](https://github.com/getsentry/sentry-mcp), [New Relic](https://mcp.newrelic.com), [Honeycomb](https://www.honeycomb.io/blog/honeycomb-mcp-ga-support-bubbleup-heatmaps-histograms), [PagerDuty](https://www.pagerduty.com/newsroom/pagerduty-expands-ai-ecosystem-to-supercharge-ai-agents/), [Dynatrace](https://github.com/dynatrace-oss/dynatrace-mcp), [Splunk](https://community.splunk.com/t5/Product-News-Announcements/GA-Splunk-MCP-Server-Making-Your-Apps-quot-Agent-Ready-quot/ba-p/759935), [Elastic](https://www.elastic.co/docs/solutions/search/mcp), and more — has shipped an official MCP server. The open-source metrics stack (Prometheus, VictoriaMetrics, Grafana Loki) has strong community coverage too. No other MCP category has this level of first-party support.

This makes sense: observability data is exactly the context that makes AI agents most useful. Debugging production errors, correlating metrics with deploys, querying logs in natural language — these are tasks where switching between your IDE and a dashboard wastes real time.

The landscape splits into **six layers**: full-stack APM platforms (Datadog, New Relic, Dynatrace), open-source metrics/visualization (Grafana, Prometheus, VictoriaMetrics), error tracking (Sentry), event-based observability (Honeycomb), log platforms (Splunk, Elastic, Axiom, SigNoz), and incident management (PagerDuty, OpsGenie). Most teams need servers from two or three layers, not all six.

**Disclosure:** Our recommendations are based on research — analyzing documentation, GitHub repositories, community feedback, and published benchmarks. We have not hands-on tested every server in this guide.

## At a Glance: Top Picks

| Category | Our pick | Stars | Runner-up |
|----------|----------|-------|-----------|
| **Full-stack APM (enterprise)** | [Datadog MCP](https://mcp.datadoghq.com) | Hosted | [New Relic MCP](https://mcp.newrelic.com) (hosted) |
| **Full-stack APM (AI-native)** | [Dynatrace MCP](https://github.com/dynatrace-oss/dynatrace-mcp) | 104 | — |
| **Open-source visualization** | [grafana/mcp-grafana](https://github.com/grafana/mcp-grafana) | 2,777 | [grafana/loki-mcp](https://github.com/grafana/loki-mcp) (Loki-specific) |
| **Prometheus metrics** | [pab1it0/prometheus-mcp-server](https://github.com/pab1it0/prometheus-mcp-server) | 412 | [giantswarm/mcp-prometheus](https://github.com/giantswarm/mcp-prometheus) (18 tools, OAuth) |
| **Prometheus (full API)** | [tjhop/prometheus-mcp-server](https://github.com/tjhop/prometheus-mcp-server) | 42 | — |
| **VictoriaMetrics** | [VictoriaMetrics/mcp-victoriametrics](https://github.com/VictoriaMetrics/mcp-victoriametrics) | 144 | — |
| **Error tracking** | [getsentry/sentry-mcp](https://github.com/getsentry/sentry-mcp) | 630 | — |
| **Event-based observability** | [Honeycomb MCP](https://mcp.honeycomb.io/mcp) | Hosted | — |
| **Log platform (enterprise)** | [Splunk MCP Server](https://splunkbase.splunk.com/app/7931) | Official | [Elastic Agent Builder MCP](https://www.elastic.co/docs/solutions/search/mcp) (9.2+) |
| **Log platform (open source)** | [SigNoz MCP](https://github.com/SigNoz/signoz-mcp-server) | Official | [Axiom MCP](https://mcp.axiom.co) (hosted) |
| **Incident management** | [PagerDuty MCP](https://github.com/PagerDuty/pagerduty-mcp-server) | 60 | [giantswarm/mcp-opsgenie](https://github.com/giantswarm/mcp-opsgenie) |
| **OpenTelemetry** | [traceloop/opentelemetry-mcp-server](https://github.com/traceloop/opentelemetry-mcp-server) | — | [mottibec/otelcol-mcp](https://github.com/mottibec/otelcol-mcp) |

## Full-Stack APM Platforms

These servers connect to commercial observability platforms that collect metrics, traces, logs, and more. If you already pay for one, use its MCP server — they're tightly coupled to their respective platforms.

### Datadog MCP — The Enterprise Swiss Army Knife (The Winner)

**[Datadog MCP Server](https://docs.datadoghq.com/bits_ai/mcp_server/)** | [Our full review](/reviews/datadog-mcp-server/) | Rating: 4/5

The most feature-rich observability MCP server. Built around **toolsets** — modular capability groups you enable or disable via URL parameters.

**What makes it stand out:**
- **50+ tools across 10+ modular toolsets** — core monitoring, alerting, APM, database monitoring, error tracking, feature flags, LLM observability, product analytics, networks, security, software delivery, synthetics
- **Agent-native design** — token-budget pagination, [CSV output (50% fewer tokens than JSON), SQL-like log queries (40% cost reduction)](https://www.datadoghq.com/blog/engineering/mcp-server-agent-tools/), error message suggestions
- **LLM observability** — unique in this comparison, monitors your AI agents' own performance
- **[GA status](https://www.datadoghq.com/about/latest-news/press-releases/datadog-launches-mcp-server/)** — production-ready since March 10, 2026, not preview
- **Zero-install remote hosting** with [regional endpoints](https://docs.datadoghq.com/bits_ai/mcp_server/) (US1, US3, EU1, AP1/AP2)
- Works with Claude Code, Cursor, OpenAI Codex, GitHub Copilot, VS Code, Goose, Kiro

**Limitations:**
- No permanent free tier (14-day trial only)
- `/api/unstable/` path despite GA status
- Community server ([winor30/mcp-server-datadog](https://github.com/winor30/mcp-server-datadog), 141 stars) covers gaps the official server doesn't (host muting, downtimes, RUM)
- Closed-source — can't audit or self-host

**Best for:** Enterprise teams already on Datadog who want the broadest operational context in their AI tools. For a deep dive into how Datadog's engineering team designed these tools for agents (and why their first API-wrapper version failed), see their [engineering blog post](https://www.datadoghq.com/blog/engineering/mcp-server-agent-tools/) and our [Datadog MCP Production Lessons](/guides/datadog-mcp-server-production-lessons/) guide.

### New Relic MCP — Natural Language Observability

**[New Relic AI MCP Server](https://mcp.newrelic.com)** | [Our full review](/reviews/newrelic-mcp-server/) | Rating: 4/5

New Relic's standout feature: you ask questions in plain English and the server translates them to NRQL queries.

**What makes it stand out:**
- **Natural language to NRQL translation** — no query language learning curve
- **35 tools** across discovery, data access, alerting, incident response, performance analytics, advanced analysis
- **[Best free tier](https://newrelic.com/pricing)** in the category — 100GB/mo ingestion, no credit card required
- **Golden metrics analysis** as a dedicated tool (throughput, response time, error rate, saturation)
- **Deployment impact analysis** — automatically correlates deploys with performance changes
- Tag-based tool filtering via `include-tags` headers

**Limitations:**
- Public Preview (not GA)
- Read-only — no muting, downtime scheduling, or alert acknowledgment
- Minimal GitHub presence (3 stars, 2 commits)
- 6 community alternatives suggest gaps

**Best for:** Teams on New Relic who want natural language querying with the lowest barrier to entry.

### Dynatrace MCP — AI-Powered Observability

**[dynatrace-oss/dynatrace-mcp](https://github.com/dynatrace-oss/dynatrace-mcp)** | **Stars:** 104 | **Language:** TypeScript

Dynatrace integrates its AI engine (Davis AI) with MCP, providing real-time observability data directly in development workflows.

**What makes it stand out:**
- **DQL (Dynatrace Query Language)** via `execute_dql` tool — queries Grail storage for logs, metrics, traces, events
- **Document management** — list, read, and create Dynatrace Notebooks, Dashboards, and Launchpads
- **Problem detection** — `list_problems` with timeframe and status filtering
- **Email notifications** — `send_email` tool for alerting workflows
- **Wide client support** — VS Code, Claude, Cursor, Amazon Q, Windsurf, ChatGPT, GitHub Copilot
- Dynatrace also ships a [managed MCP variant](https://github.com/dynatrace-oss/dynatrace-managed-mcp) for on-premises deployments

**Limitations:**
- DQL queries may incur additional costs based on consumption model (GB scanned)
- Local server only — no hosted remote endpoint
- Smaller community than Grafana or Datadog

**Best for:** Dynatrace customers who want AI-assisted querying of their Grail data store and problem management.

## Open-Source Metrics & Visualization

### Grafana MCP — The Open-Source Metrics Gateway (The Winner)

**[grafana/mcp-grafana](https://github.com/grafana/mcp-grafana)** | [Our full review](/reviews/grafana-mcp-server/) | Rating: 4/5 | **Stars:** 2,777

The most popular observability MCP server by GitHub stars and the only one with a truly open-source architecture. Connects to your Grafana instance and the surrounding LGTM stack.

**What makes it stand out:**
- **40+ tools across 15 configurable categories** — dashboards, Prometheus, Loki, ClickHouse, CloudWatch, Elasticsearch, log search, incidents, Sift, alerting, OnCall, navigation, annotations, rendering, admin
- **Works with any backend data source** Grafana supports — Prometheus, InfluxDB, Elasticsearch, CloudWatch, and dozens more
- **Separate dedicated servers** for [Loki](https://github.com/grafana/loki-mcp) (log querying) and [Tempo](https://grafana.com/docs/tempo/latest/api_docs/mcp-server/) (distributed tracing)
- **[Azure Managed Grafana MCP](https://techcommunity.microsoft.com/blog/azureobservabilityblog/introducing-azure-managed-grafana-mcp-the-managed-telemetry-gateway-for-ai-agent/4503619)** launched March 18, 2026 — first managed cloud deployment
- **Granular context management** — `--disable-<category>` and `--enabled-tools` flags
- Open source (Apache 2.0), self-hostable, all three transports (stdio + SSE + Streamable HTTP)
- v0.11.2 (Feb 2026), 15+ releases in 4 months, 252K+ Docker Hub pulls

**Limitations:**
- No hosted remote server (must run yourself, except Azure Managed Grafana)
- Service account token auth (not OAuth)
- 61 open issues including security findings (TLS bypass, credential exposure)
- Some categories require Grafana Cloud (incidents, OnCall, Sift)
- [grafana/grafana-ui-mcp-server](https://github.com/grafana/grafana-ui-mcp-server) is separate — for component library context, not observability

**Community alternatives:**
- [christian-schlichtherle/grafana-mcp](https://github.com/christian-schlichtherle/grafana-mcp) — multi-cluster dashboard discovery, editing, and testing
- [DrDroidLab/grafana-mcp-server](https://github.com/DrDroidLab/grafana-mcp-server) — simpler Grafana integration

**Best for:** Teams running their own Grafana stack who want agent-assisted metrics, logs, traces, alerting, and incident management.

### Grafana Loki MCP — Dedicated Log Querying

**[grafana/loki-mcp](https://github.com/grafana/loki-mcp)** | **Language:** Go | **Transport:** stdio, SSE

A dedicated MCP server for Grafana Loki log queries, separate from the broader mcp-grafana server.

**What makes it stand out:**
- **Focused on Loki** — `loki_query` tool for log querying, label names/values discovery, result formatting
- **Go single binary** — lightweight, easy deployment
- **SSE support** — works with n8n and other SSE-compatible tools
- Good complement to mcp-grafana if you need deeper Loki-specific functionality

**Also:** [mo-silent/loki-mcp-server](https://github.com/mo-silent/loki-mcp-server) — community alternative with intelligent log analysis features.

### Prometheus MCP Servers

Prometheus has the most MCP server implementations of any open-source monitoring tool. At least 8 independent servers exist, reflecting its dominance as the cloud-native metrics standard.

#### pab1it0/prometheus-mcp-server — The Most Popular

**Stars:** 412 | **Language:** Python | **Transport:** stdio | **Docker MCP Catalog:** Listed

**What makes it stand out:**
- **Configurable tool list** — expose only the tools you need to minimize context window usage
- `execute_query` (instant PromQL), `execute_range_query` (time-range), `list_metrics` (with pagination/filtering), `get_metric_metadata`, `get_targets`, `health_check`
- Docker MCP Catalog listing (official Docker partnership)
- Most adopted by star count

**Limitations:** Python (heavier than Go alternatives), stdio-only transport.

#### tjhop/prometheus-mcp-server — Full API Coverage

**Stars:** 43 | **Language:** Go | **Transport:** stdio, SSE, HTTP | **Latest:** v0.17.0 (March 21, 2026)

**What makes it stand out:**
- **Full Prometheus API support** — goes far beyond basic PromQL queries
- **Go single binary** — lightweight, three transport modes
- **TSDB Admin API** support (with explicit flag)
- **Documentation reading tools** — can read Prometheus docs for agents
- Most actively maintained (latest release days ago)

**Best for:** Teams who want comprehensive Prometheus interaction beyond basic queries.

#### giantswarm/mcp-prometheus — Enterprise with OAuth

**Stars:** — | **Language:** Go | **Tools:** 18 | **Transport:** — | **Auth:** OAuth 2.1

**What makes it stand out:**
- **18 read-only tools** wrapping the Prometheus HTTP API — instant/range queries, metric/label/series discovery, target/runtime info, TSDB stats, alerting rules, exemplars
- **Mimir support** — works with both Prometheus and Grafana Mimir
- **OAuth 2.1 Authorization Server** — backed by Dex/OIDC, resolves user's Mimir tenant IDs and enforces on every query
- Deployed in-cluster at Giant Swarm for multi-tenant access

**Best for:** Enterprise teams needing authenticated, multi-tenant Prometheus access with OAuth.

#### Other Prometheus implementations

- [idanfishman/prometheus-mcp](https://github.com/idanfishman/prometheus-mcp) — AI agent integration with natural language interactions
- [brenoepics/prometheus-mcp](https://github.com/brenoepics/prometheus-mcp) — minimal read-only server with convenient CLI
- [loglmhq/mcp-server-prometheus](https://github.com/loglmhq/mcp-server-prometheus) — another community option
- [weetime/prometheus-mcp-server](https://github.com/weetime/prometheus-mcp-server) — community implementation

### VictoriaMetrics MCP — Prometheus-Compatible Alternative

**[VictoriaMetrics/mcp-victoriametrics](https://github.com/VictoriaMetrics/mcp-victoriametrics)** | **Stars:** 144

The official MCP server for VictoriaMetrics, a high-performance Prometheus-compatible time-series database.

**What makes it stand out:**
- **Almost all read-only APIs** exposed — querying metrics, exploring data, listing/exporting metrics and labels, analyzing alerting/recording rules, instance parameters, cardinality analysis, metrics usage statistics
- **Official** — maintained by VictoriaMetrics team
- Community variant previously at VictoriaMetrics-Community/mcp-victoriametrics (repository no longer available)

**Best for:** Teams running VictoriaMetrics instead of (or alongside) Prometheus.

## Error Tracking

### Sentry MCP — The Error Tracking Specialist (The Winner)

**[getsentry/sentry-mcp](https://github.com/getsentry/sentry-mcp)** | [Our full review](/reviews/sentry-mcp-server/) | Rating: 4/5

Sets the standard for how first-party MCP integrations should work.

**What makes it stand out:**
- **OAuth 2.0 authentication** — no API tokens on disk, best auth in any MCP server
- **Zero-install remote hosting** at `mcp.sentry.dev`
- **Seer AI integration** — automated root cause analysis, explains *why* errors happen and suggests fixes
- **~20 tools** for issue investigation, event analysis, natural language search, project management
- Available as Claude Code plugin for automatic subagent delegation
- Also: [getsentry/sentry-mcp-stdio](https://github.com/getsentry/sentry-mcp-stdio) for self-hosted Sentry

**Limitations:**
- [800+ GitHub issues](https://github.com/getsentry/sentry-mcp/issues) at pre-1.0
- Cross-project queries fail
- AI search needs separate LLM key

**Community alternatives:**
- [ddfourtwo/sentry-selfhosted-mcp](https://github.com/ddfourtwo/sentry-selfhosted-mcp) — for self-hosted Sentry
- [elliottlawson/mcp-sentry](https://github.com/elliottlawson/mcp-sentry) — community implementation

**Best for:** Developers on Sentry Cloud who debug production errors from their IDE.

## Event-Based Observability

### Honeycomb MCP — High-Cardinality Event Analysis

**[Honeycomb MCP](https://mcp.honeycomb.io/mcp)** | [Our full review](/reviews/honeycomb-mcp-server/) | Rating: 4/5

Honeycomb treats every request as a structured event with arbitrary dimensions, then lets you slice and dice without pre-defined dashboards.

**What makes it stand out:**
- **[BubbleUp anomaly decomposition](https://www.honeycomb.io/blog/honeycomb-mcp-ga-support-bubbleup-heatmaps-histograms)** — automatically identifies what's different about a subset of events vs baseline (unique to Honeycomb), now GA with heatmap and histogram support
- **OAuth 2.1** — matches Sentry as best auth in category
- **[Hosted remote server](https://www.honeycomb.io/blog/hosted-mcp-now-available)** — zero-install, multi-region (US/EU), available on AWS Marketplace
- Available on all tiers including Free (20M events/mo)
- Self-hosted version ([honeycombio/honeycomb-mcp](https://github.com/honeycombio/honeycomb-mcp), 43 stars, MIT) is **deprecated** — use hosted instead
- 14+ tools: `run_query`, `analyze_columns`, datasets, SLOs, triggers, boards, markers, trace links, OTel guidance

**Limitations:**
- Self-hosted deprecated — messy transition period
- 50 calls/min rate limit, 24-hour session timeouts
- Fewer tools than Datadog (50+) or Grafana (40+)
- `mcp-remote` bridge dependency for stdio clients

**Best for:** Teams doing high-cardinality debugging on distributed systems.

## Log Platforms

### Splunk MCP — Enterprise Log Management

**[CiscoDevNet/Splunk-MCP-Server-official](https://github.com/CiscoDevNet/Splunk-MCP-Server-official)** | [Splunkbase](https://splunkbase.splunk.com/app/7931) | **v1.0.4** (March 17, 2026)

Splunk's official MCP server for Enterprise and Cloud, enabling AI assistants to execute SPL queries.

**What makes it stand out:**
- **SPL execution** — run Splunk queries from AI assistants
- **Natural language to SPL** — generate searches from plain English
- **Knowledge object discovery** — find saved searches, lookups, and metadata
- **RBAC enforcement** — respects Splunk role-based access control
- **[Observability Cloud support](https://community.splunk.com/t5/Product-News-Announcements/What-s-New-in-Splunk-Observability-March-2026/ba-p/759527)** — [GA since March 18, 2026](https://community.splunk.com/t5/Product-News-Announcements/GA-Splunk-MCP-Server-Making-Your-Apps-quot-Agent-Ready-quot/ba-p/759935), with infrastructure metrics, APM, and log tools
- Also: [splunk/splunk-mcp-server2](https://github.com/splunk/splunk-mcp-server2) — unofficial, Python + TypeScript, guardrails for SPL validation and output sanitization

**Limitations:**
- Low GitHub stars (2) — enterprise users tend not to star
- Enterprise pricing (no free tier for meaningful use)
- Community alternatives ([livehybrid/splunk-mcp](https://github.com/livehybrid/splunk-mcp), [guardiansphere/splunk-mcp](https://github.com/guardiansphere/splunk-mcp)) suggest gaps

**Best for:** Enterprise Splunk customers who want AI-assisted log analysis without leaving their IDE.

### Elastic MCP — Search & Observability Platform

**[elastic/mcp-server-elasticsearch](https://github.com/elastic/mcp-server-elasticsearch)** | **Stars:** 643 | [Docs](https://www.elastic.co/docs/solutions/search/mcp)

Elastic offers MCP integration through two paths:

**Agent Builder MCP (recommended for Elastic 9.2+):**
- Full access to built-in and custom tools
- The recommended approach going forward
- Available in Elasticsearch Serverless projects

**mcp-server-elasticsearch (legacy):**
- **Deprecated** — critical security updates only
- Superseded by Agent Builder MCP
- Still works for pre-9.2 deployments

**Community alternatives:**
- [cr7258/elasticsearch-mcp-server](https://github.com/cr7258/elasticsearch-mcp-server) — Elasticsearch and OpenSearch interaction, search documents, analyze indices, manage clusters
- [ggilligan12/kibana-mcp](https://github.com/ggilligan12/kibana-mcp) — Kibana Security Operations (alerts, rules, exceptions)
- [awesimon/elasticsearch-mcp](https://github.com/awesimon/elasticsearch-mcp) — mappings, search, indexing, index management

**Best for:** Teams on the Elastic Stack who need search + observability from their AI assistant.

### Axiom MCP — Cloud-Native Log Analytics

**[Axiom MCP](https://mcp.axiom.co)** | Hosted remote

Axiom's MCP server provides AI assistants with direct access to Axiom's log and event data.

**What makes it stand out:**
- **APL (Axiom Processing Language)** queries via `queryApl` tool
- **Hosted remote server** — zero-install at mcp.axiom.co
- Saved queries, monitors, monitor history
- Self-hosted version ([axiomhq/mcp-server-axiom](https://github.com/axiomhq/mcp-server-axiom), 60 stars) is **deprecated** — use hosted instead

**Best for:** Teams on Axiom who want AI-powered log querying.

### SigNoz MCP — Open-Source Observability

**[SigNoz/signoz-mcp-server](https://github.com/SigNoz/signoz-mcp-server)** | **Language:** Go | **License:** Apache 2.0

Official MCP server for SigNoz, the open-source observability platform (OpenTelemetry-native alternative to Datadog).

**What makes it stand out:**
- **Metrics, traces, logs, alerts, dashboards, service performance** — full observability stack
- **Open source** (Apache 2.0) — self-hostable, auditable
- **OpenTelemetry-native** — SigNoz is built on OTel from the ground up
- Also: [DrDroidLab/signoz-mcp-server](https://github.com/DrDroidLab/signoz-mcp-server) — community alternative

**Best for:** Teams using SigNoz as their open-source Datadog alternative.

## Incident Management

### PagerDuty MCP — The Incident Response Standard (The Winner)

**[PagerDuty/pagerduty-mcp-server](https://github.com/PagerDuty/pagerduty-mcp-server)** | [Our full review](/reviews/pagerduty-mcp-server/) | Rating: 4/5

PagerDuty doesn't collect telemetry — it manages the human response to incidents. The largest tool count of any server in this comparison.

**What makes it stand out:**
- **67 tools across 13 categories** — incidents (14), event orchestration (8), status pages (7), teams (7), schedules (6), alert grouping (5), change events (4), services (4), workflows (3), escalation policies (2), users (2), log entries (2), on-call (1)
- **Read-only by default** — 31 tools enabled by default, 36 write tools require `--enable-write-tools`. Safest write-access model in any MCP server
- **Dual deployment** — hosted at `mcp.pagerduty.com/mcp` + self-hosted (Apache-2.0, Python)
- **[Spring 2026 AI ecosystem](https://www.pagerduty.com/newsroom/pagerduty-expands-ai-ecosystem-to-supercharge-ai-agents/)** — [30+ AI partners across 11 categories](https://www.stocktitan.net/news/PD/pager-duty-expands-ai-ecosystem-to-supercharge-ai-agents-and-deliver-33p1d57iksyb.html), Anthropic Claude Code plugin with pre-commit risk scoring, Cursor MCP plugin, LangChain LangSmith integration
- Active: 270+ commits, 30 forks, 60 stars

**Limitations:**
- API token auth only (no OAuth browser flow)
- 67 tools exceeds the 20-25 MCP recommendation
- Limited free tier (5 users)

**Best for:** On-call engineers who want AI-managed incident response.

### OpsGenie MCP — Atlassian Alert Management

**[giantswarm/mcp-opsgenie](https://github.com/giantswarm/mcp-opsgenie)** | [daviddykeuk/opsgenie-mcp](https://github.com/daviddykeuk/opsgenie-mcp)

OpsGenie MCP bridges AI tools with Atlassian's alert and incident management platform.

**What makes it stand out:**
- **Alert management** — create, acknowledge, close, and manage alerts
- **Team management** — view and manage teams and heartbeats
- Two independent implementations from Giant Swarm and community

**Limitations:**
- No official Atlassian-maintained server
- Smaller ecosystem than PagerDuty MCP
- Less documentation than PagerDuty

**Best for:** Teams on OpsGenie/Atlassian who need alert management from AI tools.

## OpenTelemetry & Cross-Platform

### traceloop/opentelemetry-mcp-server — Unified Trace Querying

**[traceloop/opentelemetry-mcp-server](https://github.com/traceloop/opentelemetry-mcp-server)**

A unified MCP server for querying OpenTelemetry traces across multiple backends.

**What makes it stand out:**
- **Multi-backend** — queries traces from Jaeger, Tempo, Traceloop, and other OTel-compatible backends
- **LLM observability** — specialized support via OpenLLMetry semantic conventions
- Single server for teams using multiple trace backends

**Also notable:**
- [mottibec/otelcol-mcp](https://github.com/mottibec/otelcol-mcp) — MCP server for configuring OpenTelemetry Collectors
- [theharithsa/opentelemetry-instrumentation-mcp](https://github.com/theharithsa/opentelemetry-instrumentation-mcp) — automatic OTel instrumentation for MCP SDK
- **[OTel MCP semantic conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/mcp/)** [merged into the OTel specification](https://github.com/open-telemetry/semantic-conventions/pull/2083) (January 12, 2026) — standard attribute names and span formats for MCP tool invocations, enabling any OTel-compatible backend to ingest MCP telemetry

### last9/last9-mcp-server — Production Context Bridge

**[last9/last9-mcp-server](https://github.com/last9/last9-mcp-server)**

Bridges real-time production context (logs, metrics, traces) into your local environment.

**What makes it stand out:**
- **Service dependency graph** visualization
- **Prometheus/PromQL** queries (range and instant)
- **Upstream/downstream service discovery**
- **Log drop rule management** and server-side exception retrieval
- Works with Claude Desktop, Cursor, Windsurf, VS Code

**Best for:** Teams using Last9 for production observability.

## Feature Comparison

| Feature | Datadog | Grafana | Sentry | New Relic | Prometheus | Dynatrace | Honeycomb | PagerDuty | Splunk |
|---------|---------|---------|--------|-----------|------------|-----------|-----------|-----------|--------|
| Metrics | Deep | Deep (any source) | No | Yes | Deep | Deep | Limited | No | Yes |
| Traces | Deep | Via Tempo | No | Yes | No | Deep | Deep | No | Yes |
| Logs | Deep | Via Loki | No | Yes | No | Deep | Yes | No | Deep |
| Error tracking | Yes | Via data source | Deep | Yes | No | Yes | Events | No | No |
| Incident mgmt | Alerting | Alerting | No | Alerting | Rules | Problems | Triggers | Deep | No |
| AI analysis | Bits AI | No | Seer AI | NRQL NL | No | Davis AI | BubbleUp | No | NL to SPL |
| Auth model | OAuth/API key | API token | OAuth 2.0 | API key/OAuth | Config | API token | OAuth 2.1 | OAuth/API token | Token |
| Transport | Remote (HTTP) | stdio+SSE+HTTP | Remote (SSE) | Remote (HTTP) | stdio | stdio | Remote | Both | stdio |
| Open source | No | Yes | Yes | No | Community | OSS repo | Deprecated | Yes | Official |
| Free tier | No (14d trial) | Yes (Cloud Free) | Yes (10K/mo) | Yes (100GB/mo) | Yes (OSS) | Consumption | Yes (20M/mo) | Yes (5 users) | No |
| Tool count | 50+ | 40+ | ~20 | 35 | 6-18 | 5+ | 14+ | 67 | 5+ |
| Status | GA | Active | Pre-1.0 | Preview | Active | Active | Hosted | Active | GA |

## How to Choose

**Start with what you already use.** Every server in this comparison is tightly coupled to its platform. There's no "best observability MCP server" in isolation — the best one is the one that queries data you're already collecting.

### Decision Flowchart

**"I debug production errors daily"** → [Sentry MCP](/reviews/sentry-mcp-server/) (4/5). Deepest error investigation tools, OAuth auth, Seer AI analysis. Pair with PagerDuty if you're on-call.

**"I need the full picture — metrics, traces, logs, everything"** → **[Datadog MCP](/reviews/datadog-mcp-server/) (4/5)** if you can afford it (broadest toolset, GA). **[New Relic MCP](/reviews/newrelic-mcp-server/) (4/5)** if you want a generous free tier and natural language querying. **[Dynatrace MCP](https://github.com/dynatrace-oss/dynatrace-mcp)** if you're already on Dynatrace and want DQL-powered queries.

**"I run my own observability stack"** → **[Grafana MCP](/reviews/grafana-mcp-server/) (4/5)** for dashboards and visualization. Add **[pab1it0/prometheus-mcp-server](https://github.com/pab1it0/prometheus-mcp-server)** or **[tjhop/prometheus-mcp-server](https://github.com/tjhop/prometheus-mcp-server)** for direct PromQL access. Add **[grafana/loki-mcp](https://github.com/grafana/loki-mcp)** for dedicated log querying.

**"I use VictoriaMetrics"** → **[VictoriaMetrics/mcp-victoriametrics](https://github.com/VictoriaMetrics/mcp-victoriametrics)** (144 stars, official, comprehensive read-only APIs).

**"I need high-cardinality event debugging"** → **[Honeycomb MCP](/reviews/honeycomb-mcp-server/) (4/5)**. BubbleUp anomaly decomposition, OAuth 2.1, hosted, free tier.

**"I'm on-call and want incident automation"** → **[PagerDuty MCP](/reviews/pagerduty-mcp-server/) (4/5)** (67 tools, read-only defaults). On Atlassian? Try OpsGenie MCP.

**"I want open-source end-to-end"** → **[SigNoz MCP](https://github.com/SigNoz/signoz-mcp-server)** — OTel-native, Apache 2.0, covers metrics + traces + logs.

**"I need log analysis specifically"** → **Splunk MCP** (enterprise SPL), **Elastic Agent Builder MCP** (Elastic 9.2+), or **[Axiom MCP](https://mcp.axiom.co)** (cloud-native APL).

**"I run Prometheus and need OAuth/multi-tenant"** → **[giantswarm/mcp-prometheus](https://github.com/giantswarm/mcp-prometheus)** (18 tools, OAuth 2.1, Mimir support).

### The Stack We'd Recommend

For most teams, you want **two or three** observability MCP servers:

1. **A platform server** — Datadog, New Relic, Dynatrace, or Grafana (whichever you already use)
2. **An incident server** — PagerDuty or OpsGenie (if you use one for on-call)
3. **A specialist** — Sentry (if you debug errors daily), Prometheus (if you need direct PromQL), or Honeycomb (if you do high-cardinality tracing)

Don't install all of them. Each MCP server competes for context window space, and adding too many reduces tokens available for actual work.

## Three Trends

**1. Official vendors dominate this category.** Datadog, Grafana, Sentry, New Relic, Honeycomb, PagerDuty, Dynatrace, Splunk, Elastic, VictoriaMetrics, SigNoz, Axiom — every major observability vendor now has an official MCP server. Compare this to databases (where official servers are rare) or search (where Google has no MCP server). Observability vendors understand that context in the IDE is a competitive advantage.

**2. Hosted remote MCP is becoming the default.** Datadog, New Relic, Honeycomb, Sentry, and Axiom all offer zero-install hosted endpoints. Grafana is the notable holdout (though [Azure Managed Grafana MCP](https://techcommunity.microsoft.com/blog/azureobservabilityblog/introducing-azure-managed-grafana-mcp-the-managed-telemetry-gateway-for-ai-agent/4503619) provides a cloud path). Self-hosted servers (Prometheus, VictoriaMetrics) remain for the open-source stack, but the commercial trend is clear: the vendor runs the server.

**3. OpenTelemetry is the emerging unifying layer.** [OTel MCP semantic conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/mcp/) ([merged January 2026](https://github.com/open-telemetry/semantic-conventions/pull/2083)) define standard attribute names for MCP tool invocations. This means any OTel-compatible backend (Grafana, Datadog, Honeycomb, Splunk, New Relic, SigNoz) can ingest and correlate MCP telemetry using the same schema. Long-term, this could enable cross-platform observability of your AI agents themselves — one set of traces flowing through whichever backend you choose.

## What's Missing

- **No unified cross-platform server** — no single MCP server queries Prometheus, Datadog, and Splunk together. You need one server per platform
- **No Zabbix MCP server** — Zabbix, widely used in enterprise on-premises monitoring, has no MCP presence
- **No Nagios/Icinga MCP server** — legacy monitoring platforms with large install bases but zero MCP integration
- **No AWS CloudWatch dedicated MCP server** — CloudWatch is accessible through Grafana MCP and AWS MCP servers, but has no standalone MCP server
- **No StatusPage/incident communication MCP** — Atlassian StatusPage, Statuspage.io, BetterUptime status pages lack dedicated MCP servers
- **No synthetic monitoring MCP** — Checkly, BetterStack Uptime, UptimeRobot have no MCP servers for creating/managing synthetic checks (Datadog covers this within its platform)
- **No chaos engineering MCP** — no Chaos Monkey, Gremlin, or LitmusChaos MCP integration
- **No cost/FinOps observability** — no MCP server for cloud cost monitoring or optimization
- **No alert correlation/deduplication** — no server provides cross-platform alert correlation or intelligent grouping
- **Prometheus write support is minimal** — most servers are read-only, which is appropriate for metrics but limits administrative operations

---

*Last updated: April 2026. Star counts and tool counts are from our research and may have changed. See our individual reviews for [Sentry](/reviews/sentry-mcp-server/), [Datadog](/reviews/datadog-mcp-server/), [Grafana](/reviews/grafana-mcp-server/), [New Relic](/reviews/newrelic-mcp-server/), [Honeycomb](/reviews/honeycomb-mcp-server/), and [PagerDuty](/reviews/pagerduty-mcp-server/) for detailed analysis, or browse our [master MCP server guide](/guides/best-mcp-servers/) for all categories.*


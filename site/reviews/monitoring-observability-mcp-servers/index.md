# Monitoring & Observability MCP Servers — From Grafana to Datadog, Vendor-Led Observability Meets MCP

> Monitoring MCP servers are vendor-driven: Grafana (2.9k stars, Go, dashboards/Prometheus/Loki/Elasticsearch/alerting/OnCall), Datadog (official remote MCP, 16+ tools, HIPAA-eligible), Sentry (671 stars), Splunk GA, PagerDuty 60+ tools, Honeycomb hosted, Elastic MCP Apps


**At a glance:** Monitoring and observability is the most **vendor-invested** MCP category in Developer Tools — and the gap is widening. Since our [March 2026 initial review](/reviews/monitoring-observability-mcp-servers/), three major new vendors have launched official MCP servers: [Splunk](https://help.splunk.com/en/splunk-cloud-platform/mcp-server-for-splunk-platform/1.1/about-mcp-server-for-splunk-platform) (v1.1.0 GA, SPL queries, observability tools, OAuth 2.1), [PagerDuty](https://github.com/PagerDuty/pagerduty-mcp-server) (65 stars, 60+ tools, full incident write APIs), and [Honeycomb](https://docs.honeycomb.io/integrations/mcp) (hosted MCP, traces/SLOs/Agent Skills). [Elastic launched MCP Apps](https://www.elastic.co/search-labs/blog/mcp-apps-elastic) (April 2026) — interactive UI for observability, security, and search rendered inside AI tools. [Grafana's mcp-grafana](https://github.com/grafana/mcp-grafana) surged to 2.9k stars with v0.13.1 adding Elasticsearch, InfluxDB, Graphite datasources, admin RBAC tools, and dashboard PNG rendering. [Sentry](https://github.com/getsentry/sentry-mcp) grew to 671 stars with Streamable HTTP at mcp.sentry.dev. [Dynatrace](https://github.com/dynatrace-oss/dynatrace-mcp) launched a remote MCP server (no local setup required). **Nine vendors** now maintain official MCP servers — the highest first-party adoption rate of any MCP category. Meanwhile, [Azure SRE Agent](https://azure.microsoft.com/en-us/products/sre-agent) and [AWS DevOps Agent](https://aws.amazon.com/blogs/mt/announcing-general-availability-of-aws-devops-agent/) both reached GA, consuming observability MCP servers as their primary data layer. This is the **ninth review in our [Developer Tools MCP category](/categories/developer-tools/)**.

The observability market ($28.5B in 2025, projected $34.1B in 2026) is the largest addressable market behind any Developer Tools MCP subcategory. This explains the vendor investment: Datadog ($3.4B revenue, 32,700 customers), Grafana Labs ($400M+ ARR), Splunk/Cisco, New Relic, Dynatrace, Honeycomb, PagerDuty, and IBM all see MCP as a strategic integration point for AI-assisted operations. The pattern is clear — when the platform vendor has strong commercial incentive, you get official MCP servers rather than community fragmentation. The **Azure SRE Agent** (GA April 2026, 1,300+ agents deployed across Microsoft, 35,000+ incidents mitigated) and **AWS DevOps Agent** (GA April 2026) validate this investment — both use MCP to connect to Grafana, Datadog, New Relic, PagerDuty, and other observability tools as their primary investigation interface.

**Architecture note:** Observability MCP servers now span three deployment models. **Remote-hosted** servers (Datadog, Sentry, Honeycomb, Dynatrace remote, Splunk Cloud, PagerDuty hosted) run on the vendor's infrastructure with OAuth authentication — no local installation needed. **Local/self-hosted** servers (Grafana, Prometheus, Instana, PagerDuty local, Splunk Enterprise) run alongside your MCP client and connect to your observability backend via API tokens. **MCP Apps** (Elastic) embed interactive UI directly inside AI tools — a new paradigm where observability visualization renders in-conversation rather than via tool call results. The remote model dominates new launches, reflecting the industry shift toward zero-setup AI integrations. Most servers are read-oriented (query logs, metrics, traces) but PagerDuty's 60+ write tools and Grafana's expanded admin capabilities are pushing toward full bidirectional control.

## What's Available

### Grafana mcp-grafana — The Community Star

| Aspect | Detail |
|--------|--------|
| Repository | [grafana/mcp-grafana](https://github.com/grafana/mcp-grafana) |
| Stars | ~2,900 (+400 since March) |
| Forks | ~348 |
| Commits | 580 |
| Language | Go |
| License | Apache-2.0 |
| Creator | Grafana Labs (official) |
| Latest version | v0.13.1 (April 30, 2026) |

**Tool categories** across the Grafana ecosystem:

| Category | Capabilities |
|----------|-------------|
| Dashboards | Search, get by UID, create, update dashboards, **render to PNG** (customizable dimensions, time range, theme, scale, variables) |
| Prometheus | Execute PromQL queries, query metadata (metric names, labels, values), **VictoriaMetrics PromQL support** |
| Loki | Run LogQL log and metric queries, query label metadata and stream stats |
| **Elasticsearch** | **Execute search queries using Lucene or Elasticsearch Query DSL** (NEW) |
| **InfluxDB** | **Flux and InfluxQL query languages** (NEW v0.12.0) |
| **Graphite** | **Graphite datasource support** (NEW v0.12.0) |
| Alerting | List/fetch/create/update/delete alert rules (Grafana-managed and datasource-managed), **recording rules in ruler listings** |
| OnCall | List schedules, get shift details, get current on-call users |
| **Admin** | **RBAC management: team listing, user management, role assignment** (NEW) |
| Incidents | Incident management integration |
| **Panel Queries** | **run_panel_query: execute dashboard panel queries directly with template variable substitution and Grafana macro expansion** (NEW) |

**Key differentiator:** The **most-starred observability MCP server** by a wide margin, now approaching 3k stars. Since March, Grafana has shipped **12 releases** (v0.11.2 → v0.13.1) with major expansions: Elasticsearch querying, InfluxDB/Graphite datasources, dashboard PNG rendering, admin RBAC tools, VictoriaMetrics compatibility, per-request config, and OpenTelemetry instrumentation. The `run_panel_query` tool lets agents execute any dashboard panel's query directly with variable substitution — critical for incident investigation. Custom HTTP headers via `GRAFANA_EXTRA_HEADERS` support reverse proxy and custom auth schemes. Alpine Docker images reduce deployment footprint. Also has a dedicated [loki-mcp](https://github.com/grafana/loki-mcp) for Loki-only use cases and a [grafana-mcp-agent-datasource](https://github.com/grafana/grafana-mcp-agent-datasource) plugin that connects MCP servers *into* Grafana for natural language querying.

**Limitation:** Requires a running Grafana instance — no standalone metrics querying. RBAC permission requirements can be complex to configure. Still pre-1.0, though the rapid v0.12→v0.13 cadence suggests 1.0 may be approaching. No built-in Tempo (tracing) integration in the main server yet, though Grafana Cloud has a separate [MCP server for tracing](https://grafana.com/docs/grafana-cloud/send-data/traces/mcp-server/).

### Datadog — Official Remote MCP Server

| Aspect | Detail |
|--------|--------|
| Server | [Datadog Remote MCP Server](https://docs.datadoghq.com/bits_ai/mcp_server/) |
| Type | Remote-hosted (no local installation) |
| Authentication | OAuth via Datadog |
| Launch | March 10, 2026 (GA) |
| Creator | Datadog (official) |
| Compliance | HIPAA-eligible |

**16+ core tools** organized into toolsets:

| Toolset | Capabilities |
|---------|-------------|
| Core (default) | Logs, metrics, traces, dashboards, monitors, incidents, hosts, services, events, notebooks |
| Alerting | Monitor validation, groups, templates |
| APM | Trace analysis, span search, Watchdog insights, performance investigation |
| DBM | Database Monitoring query plans and samples |
| Error Tracking | Issues across RUM, Logs, and Traces |
| Feature Flags | Create, list, update feature flags |
| LLM Observability | LLM Observability spans |
| Networks | Cloud Network Monitoring, Network Device Monitoring |
| Security | Code security scanning, signals, findings |
| Software Delivery | CI Visibility, Test Optimization |
| Synthetics | Synthetic test management |

**Key differentiator:** The **only HIPAA-eligible observability MCP server** and the most comprehensive in tool coverage. Remote-hosted means zero local setup — connect from Claude Code, Cursor, GitHub Copilot, or any MCP client via OAuth. Toolset-based configuration saves context window space (only load the toolsets you need). Token-efficient design (CSV formatting, SQL queries, field trimming) cuts token usage by up to 50%. Backed by Datadog's $3.4B revenue and 14% observability market share. Role-based access controls carry over from your existing Datadog permissions.

**Limitation:** Requires a Datadog subscription (not free). Remote-hosted means you're dependent on Datadog's MCP infrastructure availability. No open-source community server with significant adoption — [shelfio/datadog-mcp](https://github.com/shelfio/datadog-mcp) and [winor30/mcp-server-datadog](https://github.com/winor30/mcp-server-datadog) exist but have minimal stars. The official server is closed-source. Toolset count is impressive but each toolset adds context window overhead.

### Sentry — Remote-Hosted Error Tracking

| Aspect | Detail |
|--------|--------|
| Repository | [getsentry/sentry-mcp](https://github.com/getsentry/sentry-mcp) |
| Stars | ~671 (+29% since March) |
| Forks | ~105 |
| Commits | 981 |
| Type | Remote-hosted (Streamable HTTP at mcp.sentry.dev) + local via npx |
| Authentication | OAuth |
| Creator | Sentry (official) |

Tools for error tracking and debugging: list organizations, get issue details, search events and issues, view stacktraces, **Seer AI analysis**. Remote-hosted at `mcp.sentry.dev/mcp` via Streamable HTTP with OAuth — no API keys or local server needed. Also available locally via `npx @sentry/mcp-server`. Optimized for coding assistants (Cursor, Claude Code). Installable as a Claude Code plugin for automatic subagent delegation. Also has a legacy stdio version at [getsentry/sentry-mcp-stdio](https://github.com/getsentry/sentry-mcp-stdio) and a self-hosted variant at [ddfourtwo/sentry-selfhosted-mcp](https://github.com/ddfourtwo/sentry-selfhosted-mcp).

**Key differentiator:** Error tracking is a natural fit for MCP — AI coding assistants can query Sentry for the exact error, stacktrace, and affected users when debugging. Now at 981 commits with strong growth (+29% stars), Sentry is one of the most actively developed observability MCP servers. Remote hosting via Streamable HTTP removes all setup friction. Claude Code automatically delegates Sentry-related questions to the sentry-mcp subagent.

**Limitation:** Focused exclusively on error tracking — no metrics, logs, or infrastructure monitoring. MCP is "still evolving" per Sentry's own docs — expect rough edges. Note: `EMBEDDED_AGENT_PROVIDER` must now be set explicitly (auto-detection deprecated).

### Dynatrace — Enterprise AI Observability

| Aspect | Detail |
|--------|--------|
| Repository | [dynatrace-oss/dynatrace-mcp](https://github.com/dynatrace-oss/dynatrace-mcp) |
| Stars | ~112 |
| Forks | ~12 |
| Commits | 381 |
| Language | TypeScript |
| Status | **Maintenance Mode** (local server); **NEW Remote MCP Server** available |
| Creator | Dynatrace (official) |

The local open-source server is now in **maintenance mode**, as Dynatrace has launched a **Remote MCP Server** — no local setup required, instant connection from any MCP-compatible client. Provides DQL querying, problem investigation, Kubernetes event analysis, timeseries forecasting, document search, entity resolution. Powers integrations with Azure SRE Agent, AWS DevOps Agent, GitHub Copilot, Atlassian Rovo Ops, Kiro, and Amazon Q. Also has a companion [dynatrace-managed-mcp](https://github.com/dynatrace-oss/dynatrace-managed-mcp) for self-hosted deployments. **Dynatrace Intelligence** — the industry's first agentic operations system — provides deterministic insights fused with agentic action.

**Key differentiator:** Dynatrace's Grail data lakehouse gives the MCP server access to the full telemetry stack (logs, metrics, traces, events, business analytics) through a single DQL interface. The remote MCP server eliminates all local setup. Enterprise-grade with Dynatrace's AI engine (Davis) providing causal AI analysis behind the queries.

**Limitation:** Requires Dynatrace platform access (enterprise pricing). The local open-source repo's star count dropped (201→112, likely due to maintenance mode announcement). Remote server is closed-source. Tightly coupled to the proprietary Dynatrace backend.

### New Relic — 35 Tools in Public Preview

| Aspect | Detail |
|--------|--------|
| Server | [New Relic MCP Server](https://docs.newrelic.com/docs/agentic-ai/mcp/overview/) (Public Preview) |
| Repository | [newrelic/mcp-server](https://github.com/newrelic/mcp-server) (6 stars, 2 commits — minimal) |
| Remote endpoint | `mcp.newrelic.com/mcp/` (cloud-hosted) |
| Tools | 35 tools across multiple categories |
| Authentication | New Relic API key |
| Creator | New Relic (official) |
| Launch | November 2025 (Public Preview) |

**Key capabilities:** Execute NRQL queries, natural language to NRQL conversion, deployment performance analysis, entity management, APM traces, distributed traces, logs, metrics, alerts, incidents, dashboards. Works with GitHub Copilot, ChatGPT, Claude, Cursor. Now **cloud-hosted** at `mcp.newrelic.com/mcp/` — no npm, local proxy, or container needed. Integrated with **Azure SRE Agent** for automatic incident investigation. Community alternatives exist ([cloudbring/newrelic-mcp](https://github.com/cloudbring/newrelic-mcp), [thrashy/mcp-newrelic](https://github.com/thrashy/mcp-newrelic)) but have minimal adoption.

**Limitation:** Still in Public Preview — not GA. Requires New Relic account. The GitHub repo (6 stars, 2 commits) suggests the open-source version is essentially a placeholder — the real server is the cloud-hosted endpoint. 35 tools may consume significant context window space.

### IBM Instana — 100+ Tools for Enterprise Observability

| Aspect | Detail |
|--------|--------|
| Repository | [instana/mcp-instana](https://github.com/instana/mcp-instana) |
| Stars | ~19 |
| Forks | ~23 |
| Commits | 105 |
| Language | Python |
| License | Apache-2.0 |
| Transport | **Streamable HTTP + Stdio** |
| Creator | IBM (official) |

**100+ tools** mapping directly to Instana APIs: application metrics, endpoint performance, infrastructure hosts, Kubernetes events, alerts, dependencies, snapshots, and configuration objects. Available on AWS Marketplace (free to deploy, requires Instana subscription). Now supports **Streamable HTTP transport** in addition to Stdio for broader MCP client compatibility. Integrates with Amazon Q Developer CLI, Kiro IDE, and Azure SRE Agent. Part of IBM's broader [mcp collection](https://github.com/IBM/mcp) (ContextForge AI Gateway). Includes **MCP Observability** via Traceloop SDK for distributed tracing of MCP server interactions.

**Key differentiator:** The **highest tool count** of any observability MCP server (100+). Covers the full stack from application performance to Kubernetes infrastructure. AWS Marketplace deployment simplifies enterprise procurement. IBM backing provides enterprise support and compliance guarantees.

**Limitation:** Only 19 stars — the lowest adoption of any vendor-backed observability MCP server. Requires Instana subscription (enterprise pricing). Python implementation. The 100+ tool count may overwhelm context windows if not carefully filtered with `--tools`.

### Prometheus Community Servers — Open-Source Metrics

| Aspect | Detail |
|--------|--------|
| Top server | [pab1it0/prometheus-mcp-server](https://github.com/pab1it0/prometheus-mcp-server) |
| Stars | ~429 (+26% since March) |
| Forks | ~88 |
| Commits | 209 |
| Latest version | v1.6.0 (March 2026) |
| Language | Python |

Multiple community implementations exist — no official CNCF Prometheus MCP server. pab1it0/prometheus-mcp-server (429 stars, v1.6.0) is the most adopted, enabling PromQL queries and metric analysis. Also: [idanfishman/prometheus-mcp](https://github.com/idanfishman/prometheus-mcp) (Python), [yshngg/prometheus-mcp-server](https://github.com/yshngg/prometheus-mcp-server) (Go), [loglmhq/mcp-server-prometheus](https://github.com/loglmhq/mcp-server-prometheus) (TypeScript), [giantswarm/mcp-prometheus](https://github.com/giantswarm/mcp-prometheus) (Go, Prometheus + Mimir). Docker MCP Catalog includes an official Prometheus server image. **AWS Labs** also maintains a [Prometheus MCP server](https://awslabs.github.io/mcp/servers/prometheus-mcp-server) with AWS SigV4 authentication for AWS Managed Prometheus.

**Key differentiator:** Free and open-source alternative to vendor-locked observability MCP servers. Prometheus is the de facto standard for cloud-native metrics (CNCF graduated project). Multiple language implementations let teams choose their stack. The 26% star growth since March shows continued community adoption.

**Limitation:** No official server — community fragmentation across 5+ implementations. Though 429 stars is respectable, it trails vendor-backed servers. Read-only metric querying — no alert management, dashboard creation, or Alertmanager integration (though [ntk148v/alertmanager-mcp-server](https://github.com/ntk148v/alertmanager-mcp-server) exists separately). CNCF Observability Summit (May 2026) will address MCP's role but no official server announcement yet.

### Elasticsearch — From Deprecated Server to MCP Apps

| Aspect | Detail |
|--------|--------|
| Repository | [elastic/mcp-server-elasticsearch](https://github.com/elastic/mcp-server-elasticsearch) |
| Stars | ~651 |
| Forks | ~140 |
| Status | **Deprecated** standalone server; replaced by **Elastic MCP Apps** (April 2026) |

Elastic's original standalone MCP server is deprecated (v0.4.6, security fixes only). But in **April 2026**, Elastic launched **[MCP Apps for Elastic](https://www.elastic.co/search-labs/blog/mcp-apps-elastic)** — a paradigm shift. Three apps render **interactive UI directly inside AI tools** (Claude, VS Code, GitHub Copilot, Goose):

- **Observability App:** Explore distributed traces, inspect service dependencies, diagnose system health through interactive views rendered in-conversation
- **Security App:** Alert triage with severity grouping and AI verdicts, attack discovery with MITRE ATT&CK mapping, threat hunting with ES|QL workbench
- **Search App:** Build dashboards from natural language, query with ES|QL, inline interactive visualizations

Built on the MCP App standard co-authored by Anthropic and OpenAI. Available now in public preview. Community alternative [cr7258/elasticsearch-mcp-server](https://github.com/cr7258/elasticsearch-mcp-server) (~270 stars, Python, 170 commits) supports both Elasticsearch and OpenSearch and continues active development.

**Key differentiator:** Elastic is the **first observability vendor to ship interactive UI inside AI conversations** via the MCP App standard. Rather than returning text/JSON tool results, MCP Apps render actual visualizations (trace waterfalls, dependency graphs, dashboards) directly in Claude or VS Code. This is a fundamentally different approach from every other observability MCP server.

**Limitation:** MCP Apps are in public preview — the standard itself is new. Requires MCP clients that support the App rendering protocol. The deprecated standalone server (651 stars) won't be updated. Teams on Elastic <9.2.0 need the community alternative.

### VictoriaMetrics — Prometheus Alternative with MCP

| Aspect | Detail |
|--------|--------|
| Repository | [VictoriaMetrics/mcp-victoriametrics](https://github.com/VictoriaMetrics/mcp-victoriametrics) |
| Stars | ~160 (+21% since March) |
| Commits | 355 |
| Latest version | v1.18.0 |

Uses almost all read-only VictoriaMetrics APIs: query metrics, explore data, list/export metrics and labels, analyze alerting/recording rules, show instance parameters, explore data cardinality. Includes documentation search, PromQL/MetricsQL prettification, query explanation, and unit-testing for rules. **NEW: Hosted MCP Server** for VictoriaMetrics Cloud — no local setup needed. Also has dedicated servers for [VictoriaLogs](https://github.com/VictoriaMetrics-Community/mcp-victorialogs), [VictoriaTraces](https://github.com/VictoriaMetrics-Community/mcp-victoriatraces), and a **NEW** [mcp-vmanomaly](https://github.com/VictoriaMetrics/mcp-vmanomaly) for anomaly detection.

### Splunk — GA MCP Server with Observability Cloud (NEW)

| Aspect | Detail |
|--------|--------|
| Server | [Splunk MCP Server](https://help.splunk.com/en/splunk-cloud-platform/mcp-server-for-splunk-platform/1.1/about-mcp-server-for-splunk-platform) |
| Version | v1.1.0 (GA) |
| Type | Local (Splunk Enterprise) + Cloud (Splunk Cloud Platform) |
| Authentication | OAuth 2.1, RBAC, encrypted token security |
| Creator | Splunk/Cisco (official) |
| Available on | [Splunkbase](https://splunkbase.splunk.com/app/7931) |

**Key capabilities:** Run SPL searches directly, explore knowledge objects (saved searches, lookups), AI-powered SPL generation (`saia_generate_spl`), SPL explanation (`saia_explain_spl`), natural language questions (`saia_ask_splunk_question`), run existing saved searches via MCP. **Observability Cloud capabilities** are now GA — agents can interact with Splunk Observability data. v1.1.0 adds OAuth 2.1, saved search execution, and rate limiting.

**Key differentiator:** Splunk's massive installed base (15k+ customers) gets MCP access to their existing SPL queries and observability data. Enterprise-grade: RBAC, rate limiting, encrypted tokens, granular tool management for administrators. The AI SPL tools are particularly valuable — SPL is notoriously complex, and having AI agents generate/explain queries bridges a major usability gap. **AI Agent Monitoring** in Observability Cloud (GA) tracks performance, quality, cost, and security risks of AI-powered applications, with Cisco AI Defense integration.

**Limitation:** Requires Splunk subscription. Closed-source, available only via Splunkbase. No open-source community server with meaningful adoption. Enterprise pricing may exclude smaller teams.

**See our dedicated review:** [Splunk MCP Server — full review with setup guide, tool breakdown, and security model](/reviews/splunk-mcp-server/) (Rating: 4/5)

### PagerDuty — 60+ Tools for Incident Management (NEW)

| Aspect | Detail |
|--------|--------|
| Repository | [PagerDuty/pagerduty-mcp-server](https://github.com/PagerDuty/pagerduty-mcp-server) |
| Stars | ~65 |
| Forks | ~33 |
| Commits | 289 |
| Language | Python |
| License | Apache-2.0 |
| Remote | `mcp.pagerduty.com` (hosted, all tools enabled by default) |
| Creator | PagerDuty (official) |

**60+ tools** — the most comprehensive write API in the observability MCP space:

| Category | Capabilities |
|----------|-------------|
| Incidents | Create, acknowledge, resolve, merge, snooze, reassign incidents |
| Services | List, get, create, update services and service dependencies |
| On-Call | List on-call users, schedules, escalation policies |
| Event Orchestration | Manage routing and automation rules |
| Incident Workflows | Trigger automated response workflows |
| Status Pages | Manage status page updates |
| Users/Teams | List, get, manage users and team memberships |

**Key differentiator:** PagerDuty is the **first observability MCP server with comprehensive write APIs**. While most observability MCP servers are read-only (query data), PagerDuty lets agents create, acknowledge, and resolve incidents, manage on-call schedules, and coordinate response teams. Both local (with `--enable-write-tools` safety flag) and hosted (`mcp.pagerduty.com`, all tools enabled) deployment options. Integrated with Azure SRE Agent for automated incident management.

**Limitation:** 65 stars is modest for PagerDuty's market position. Incident management is adjacent to but not the same as observability — no metrics, logs, or traces. Write tools in the hosted version are enabled by default — teams should ensure proper RBAC.

### Honeycomb — Hosted MCP with Agent Skills (NEW)

| Aspect | Detail |
|--------|--------|
| Server | [Honeycomb MCP Server](https://docs.honeycomb.io/integrations/mcp) |
| Type | Remote-hosted (cloud, no local setup) |
| Creator | Honeycomb (official) |
| Launch | March 2026 (expanded capabilities) |

**Key capabilities:** Query, analyze, and visualize observability data (traces, triggers, SLOs) using natural language. **Agent Skills** provide Claude Code, Cursor, and AWS DevOps Agent with specialized Honeycomb investigation capabilities. **Honeycomb Metrics** (GA March 2026) complement existing tracing-first approach. Supported across Claude Code, Cursor, Amazon Q Developer, and other MCP-compatible IDEs.

**Key differentiator:** Honeycomb positions itself as "the first observability platform purpose-built for the agent era." Its tracing-first architecture — structured events with arbitrary-width columns — is uniquely suited for AI agent queries. Agents can explore distributed traces, analyze SLOs, and manage triggers without learning a query language. **Agent Skills** are pre-built investigation workflows that agents invoke automatically. Hosted deployment means zero setup.

**Limitation:** Requires Honeycomb subscription. No open-source self-hosted option for the MCP server. No public GitHub repository with community metrics. Tracing-focused — less comprehensive than Grafana or Datadog for metrics/logs use cases.

## Developer Tools MCP Comparison

| Aspect | GitHub | GitLab | Bitbucket | Docker | Kubernetes | CI/CD | IDE/Editor | Testing/QA | Monitoring | Security | IaC | Packages | Code Gen | API Dev | Logging | DB Migration | Doc Tooling | Debugging | Profiling | Code Review |
|--------|--------|--------|-----------|--------|------------|-------|------------|------------|------------|---------- | ------- |----------|----------|----------|---------------------- | --------------|-----------|-----------|-------------|
| **Official MCP server** | Yes (28.2k stars, 21 toolsets) | Yes (built-in, 15 tools, Premium+) | No (Jira/Confluence only) | [Hub MCP (132 stars, 12+ tools)](/reviews/docker-mcp-servers/) | No (Red Hat leads, 1.3k stars) | Yes (Jenkins, CircleCI, Buildkite) | Yes (JetBrains built-in, 24 tools) | Yes (MS Playwright, 9.8k stars, 24 tools) | **Yes (9 vendors: Grafana 2.9k, Datadog, Sentry 671, Splunk GA, PagerDuty 60+ tools, Honeycomb, Dynatrace, New Relic, Instana; Elastic MCP Apps)** | [Yes (Semgrep, SonarQube, Snyk, Trivy, GitGuardian, Cycode, Contrast)](/reviews/security-scanning-mcp-servers/) | Yes (Terraform 1.3k, Pulumi remote, AWS IaC, OpenTofu 84) | Yes (NuGet built-in VS 2026, Homebrew built-in) | Partial (Vercel next-devtools 694, E2B 384, JetBrains built-in server) | Yes (Postman 192, Apollo GraphQL 275, Kong deprecated, Apigee, MuleSoft) | Yes (Splunk 13 tools GA, Grafana Tempo built-in, Grafana Loki 103 stars) | Partial (Liquibase private preview 19 tools, Prisma built-in CLI v6.6.0+) | Yes (Microsoft Learn 1.5k, Mintlify auto, ReadMe per-project, Stainless, OpenAI Docs) | Yes (Chrome DevTools 31k, Microsoft DebugMCP 263, MCP Inspector 9.2k official) | Partial (CodSpeed MCP, Polar Signals remote, Grafana Pyroscope via mcp-grafana) | Yes (SonarQube 442 stars, Codacy 56 stars, Graphite GT built-in) |
| **Remote hosting** | Yes (`api.githubcopilot.com/mcp/`) | No | No | No | AWS EKS MCP (preview) | Yes (Buildkite remote MCP) | No (requires running IDE) | No (local browser required) | **Yes (Datadog, Sentry, Honeycomb, Dynatrace remote, PagerDuty hosted, Splunk Cloud, New Relic — OAuth)** | [No (all local/CLI-based)](/reviews/security-scanning-mcp-servers/) | [Yes (Pulumi remote MCP)](/reviews/infrastructure-as-code-mcp-servers/) | N/A | N/A | N/A | N/A | — | N/A | No (local debuggers) | No (local profiling agents) | N/A |
| **Top community server** | GitMCP (7.8k stars) | zereight/gitlab-mcp (1.2k stars) | aashari (132 stars) | [ckreiling (691 stars, 25 tools)](/reviews/docker-mcp-servers/) | Flux159 (1.4k stars, 20+ tools) | Argo CD (415 stars, 12 tools) | vscode-mcp-server (352 stars, 15 tools) | executeautomation (5.3k stars) | pab1it0/prometheus (429 stars) | [CodeQL community (143 stars)](/reviews/security-scanning-mcp-servers/) | Ansible (25 stars, 40+ tools) | mcp-package-version (122 stars, 9 registries) | Context7 (50.3k stars), magic-mcp (4.5k stars) | openapi-mcp-generator (495 stars), mcp-graphql (374 stars) | cr7258/elasticsearch (270 stars), Traceloop OTel (178 stars) | mpreziuso/mcp-atlas (Atlas), defrex/drizzle-mcp (Drizzle) | GitMCP (7.8k stars), Grounded Docs (1.2k stars), Docs MCP (87 stars) | claude-debugs-for-you (496 stars), x64DbgMCPServer (398 stars), devtools-debugger (341 stars) | theSharque/mcp-jperf (Java JFR), PageSpeed Insights MCP servers | kopfrechner/gitlab-mr-mcp (86 stars), crazyrabbitLTC (32 stars) |
| **Community tool count** | 28+ (local Git) | 100+ | 25+ | 25 (container mgmt) | 20+ (core) to 253+ (claimed) | 9-21 per server | 13-19 per server | 24 (official) + API testing | **60+ (PagerDuty), 100+ (Instana), 35 (New Relic), 16+ (Datadog)** | [7 (Semgrep) to full platform (Snyk)](/reviews/security-scanning-mcp-servers/) | [20+ (Terraform), full platform (Pulumi)](/reviews/infrastructure-as-code-mcp-servers/) | N/A | N/A | N/A | N/A | — | N/A | N/A | N/A | N/A |
| **Metrics querying** | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Core capability (PromQL, DQL, NRQL) | N/A | N/A | N/A | N/A | N/A | N/A | — | N/A | N/A | Flamegraph/profile querying (Pyroscope, CodSpeed) | N/A |
| **Log analysis** | N/A | N/A | N/A | N/A | N/A | CircleCI (build logs) | N/A | N/A | Yes (Loki, Datadog, Elastic) | N/A | N/A | N/A | N/A | N/A | Log search/analysis + trace correlation | — | N/A | Crash log analysis | Profile analysis (flamegraphs, CPU traces) | N/A |
| **Alerting management** | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Yes (Grafana, Datadog, New Relic) | N/A | N/A | N/A | N/A | N/A | N/A | — | N/A | N/A | N/A | N/A |
| **Authentication** | PAT / GitHub App | OAuth 2.0 / PAT | App Password / OAuth | Docker Desktop credentials | kubeconfig / OAuth / OIDC | API tokens per platform | Local connection (port/stdio) | None (local browsers) | API tokens / OAuth (remote) | [API tokens / CLI auth](/reviews/security-scanning-mcp-servers/) | API tokens / OAuth / CLI auth | None (public registries) | API keys (Context7, magic-mcp, E2B) | API keys / Bearer / OAuth / 1Password | API tokens / OAuth / RBAC (Splunk) | Database credentials / CLI auth | None (GitMCP, MS Learn) / API keys (platform MCP) | None (local debuggers) / Chrome DevTools auto-connect | API keys (CodSpeed, Polar Signals) / Grafana auth / Google API key (PageSpeed) | API tokens (SonarQube, Codacy) / GitHub PAT / GitLab PAT |
| **AAIF membership** | No (but Microsoft is Platinum) | No | No | [Gold](/reviews/docker-mcp-servers/) | No (but Google/AWS/MS are Platinum) | No | No (but Microsoft is Platinum) | No (but Microsoft is Platinum) | No | [No](/reviews/security-scanning-mcp-servers/) | No | No (but Microsoft is Platinum) | No | No | No | No | No (but Microsoft is Platinum) | No (but Google/Microsoft are Platinum) | No | No |
| **Platform users** | 180M+ developers | 30M+ users | ~41k companies | 20M+ users | 5.6M developers | Jenkins: 11.3M devs | VS Code: 75.9% market share | Playwright: 45.1% QA adoption | Datadog: 32.7k customers | [SonarQube: 17.7% SAST mindshare](/reviews/security-scanning-mcp-servers/) | Terraform: millions of users, 45% IaC adoption | npm: 5B+ weekly downloads, PyPI: 421.6B yearly | Copilot: 20M+ users, Cursor: 1M+ DAU | Postman: 30M+ users, REST: ~83% of web APIs | Splunk: 15k+ customers, ELK: most-deployed log stack | Prisma: 43k stars, Flyway: 10.7k stars, Atlas: 6.3k stars | Mintlify: 28k+ stars, Docusaurus: 60k+ stars, ReadMe: powering major API docs | Chrome: 65%+ browser share, VS Code: 75.9% IDE share, x64dbg: 45k+ stars | APM market: $7-10B, Pyroscope: 11k+ stars, async-profiler: 9k+ stars | SonarQube: 7.4M+ users, CodeRabbit: top AI reviewer, Qodo/PR-Agent: 10.5k stars |
| **Our rating** | [4.5/5](/reviews/github-mcp-server/) | [3.5/5](/reviews/gitlab-mcp-server/) | [2.5/5](/reviews/bitbucket-mcp-server/) | [4/5](/reviews/docker-mcp-servers/) | [4/5](/reviews/kubernetes-mcp-servers/) | [3.5/5](/reviews/ci-cd-mcp-servers/) | [3.5/5](/reviews/ide-code-editor-mcp-servers/) | [3.5/5](/reviews/testing-qa-mcp-servers/) | **4.5/5** | [3.5/5](/reviews/security-scanning-mcp-servers/) | [4/5](/reviews/infrastructure-as-code-mcp-servers/) | [3/5](/reviews/package-management-mcp-servers/) | [3.5/5](/reviews/code-generation-mcp-servers/) | [3.5/5](/reviews/api-development-mcp-servers/) | [3.5/5](/reviews/logging-tracing-mcp-servers/) | [2.5/5](/reviews/database-migration-mcp-servers/) | [3.5/5](/reviews/documentation-tooling-mcp-servers/) | [4.5/5](/reviews/debugging-mcp-servers/) | [3/5](/reviews/profiling-performance-mcp-servers/) | [3.5/5](/reviews/code-review-pull-request-mcp-servers/) |

## Known Issues

1. **Vendor lock-in is the price of quality** — The best observability MCP servers (Datadog, Grafana, New Relic, Dynatrace) all require their respective platforms. Unlike [GitHub MCP](/reviews/github-mcp-server/) where community alternatives are strong, observability MCP servers are tightly coupled to vendor APIs. Switching platforms means switching MCP servers entirely. Grafana's open-source model and Prometheus community servers are the exceptions.

2. **Remote hosting now dominates** — Seven vendors offer remote-hosted MCP servers (Datadog, Sentry, Honeycomb, Dynatrace, PagerDuty, Splunk Cloud, New Relic), up from two in March. This is convenient but introduces dependency on vendor MCP infrastructure. PagerDuty and Sentry now offer both remote and local options, breaking the either/or pattern from March.

3. **Context window pressure from tool count** — IBM Instana exposes 100+ tools, New Relic 35, Datadog 16+ with expandable toolsets. Each tool's description and schema consumes context window tokens. Grafana's `--disable-<category>` and Datadog's toolset approach let you selectively load tools, but this requires upfront configuration. An AI agent loading all available tools from multiple observability servers could easily consume 30-50% of its context window on tool definitions alone.

4. **Write capabilities expanding but unevenly** — PagerDuty's 60+ tools include full incident write APIs (create, acknowledge, resolve, merge). Grafana now has admin RBAC tools. But most observability MCP servers remain read-heavy. The write gap is closing fastest in incident management (PagerDuty, Datadog) and slowest in metrics/logging platforms (Prometheus, Splunk read emphasis).

5. **No official Prometheus MCP server** — Prometheus has 56k+ GitHub stars and is the CNCF's most adopted monitoring project, but no official Prometheus MCP server exists. Five community implementations fragment adoption (max 340 stars). Compare this to Grafana (official, 2.5k stars). The CNCF's governance model, like the Selenium Foundation for [testing MCP servers](/reviews/testing-qa-mcp-servers/), is slower to adopt new integration standards than individual companies.

6. **Elastic's pivot to MCP Apps is a paradigm preview** — Elastic skipped the built-in MCP endpoint transition and jumped to **MCP Apps** — interactive UI rendered inside AI tools. This is a fundamentally different approach (visualization in-conversation vs. text/JSON tool results) built on the Anthropic/OpenAI co-authored MCP App standard. If MCP Apps gain adoption, other vendors may follow, creating another transition for teams. Community alternative cr7258 (~270 stars) continues active development.

7. **Observability-of-observability gap** — MCP servers that query your monitoring systems introduce a new layer that itself needs monitoring. If your Grafana MCP server fails, how do you know? Traditional APM tools struggle with MCP failures because they can't distinguish between prompt problems, LLM hallucinations, tool description issues, and execution failures. Solutions like Moesif and OpenLIT are emerging but early stage.

8. **Azure SRE Agent and AWS DevOps Agent are the closest to cross-platform** — Each vendor's MCP server still only accesses its own data. But Azure SRE Agent (GA April 2026) and AWS DevOps Agent (GA) connect to multiple observability MCP servers (Grafana, Datadog, New Relic, PagerDuty) through a single agent interface. These are not MCP servers themselves but MCP *consumers* that aggregate across platforms — the cross-platform layer we noted as missing in March. Grafana's expanded multi-datasource support (now Prometheus, Loki, CloudWatch, Elasticsearch, InfluxDB, Graphite) also helps.

9. **Community servers lack enterprise features** — Prometheus community MCP servers (340 stars max) provide basic PromQL querying but lack the enterprise features of vendor servers: RBAC, audit logging, HIPAA compliance, secret redaction, rate limiting. For production use, this gap may push teams toward vendor solutions even when the underlying data source is open.

10. **Natural language to query translation varies in quality** — New Relic's MCP server converts natural language to NRQL, and several servers offer "conversational" interfaces. But query language translation is inherently lossy — a vague question like "what's slow?" could mean dozens of different NRQL/PromQL/DQL queries. Without understanding the specific service topology, AI agents may generate technically valid but operationally useless queries. Datadog's Watchdog insights and Dynatrace's Davis AI partially address this by providing pre-analyzed findings rather than raw query results.

## Bottom Line

**Rating: 4.5 out of 5** (upgraded from 4/5 in March 2026)

The monitoring and observability MCP ecosystem is the **strongest vendor-backed category** in Developer Tools — and the lead is growing. **Nine major vendors** (Grafana, Datadog, Sentry, Splunk, PagerDuty, Honeycomb, Dynatrace, New Relic, IBM Instana) now maintain official MCP servers, up from six in March. Elastic's MCP Apps add a tenth if you count the new paradigm. No other Developer Tools subcategory comes close to this level of first-party investment. Grafana's server (2.9k stars, v0.13.1) leads in community adoption with dramatic datasource expansion (Elasticsearch, InfluxDB, Graphite, admin RBAC). Datadog's remote MCP server sets the bar for enterprise features. PagerDuty brings the first comprehensive write APIs (60+ tools). Splunk reached GA with full observability cloud integration. Honeycomb positions as purpose-built for the agent era. And both **Azure SRE Agent** and **AWS DevOps Agent** reached GA, consuming these MCP servers as their primary investigation interface — validating the entire category.

The **4.5/5 rating** (up from 4/5) reflects: nine official vendor MCP servers (highest in any category), Grafana's accelerating development (12 releases in 5 weeks, 2.5k→2.9k stars), three major new entrants (Splunk GA, PagerDuty 60+ tools, Honeycomb hosted), Elastic's pioneering MCP Apps paradigm, PagerDuty breaking the read-only barrier with comprehensive write APIs, Azure SRE Agent/AWS DevOps Agent GA adoption validating the category, remote hosting now dominant (7 vendors), and growing real-world deployment (Microsoft: 1,300+ agents, 35,000+ incidents mitigated). It loses the half point for: vendor lock-in still endemic, no official Prometheus MCP server despite its dominance, context window pressure from high tool counts across multiple servers, MCP Apps standard still in preview, and Dynatrace's confusing maintenance-mode transition.

**Who benefits from monitoring MCP servers today:**

- **SRE/DevOps teams** — AI-assisted incident response is the killer use case, now validated at scale (Azure SRE Agent: 35k+ incidents mitigated). Feed live logs, metrics, and traces to an AI agent that can correlate signals, suggest root causes, and (with PagerDuty) take action
- **Developers debugging in-IDE** — Sentry's MCP server (671 stars, 981 commits) lets coding assistants pull error details, stacktraces, and affected users directly into the development workflow
- **Grafana shops** — mcp-grafana (2.9k stars, v0.13.1) is the most comprehensive open-source observability MCP server, now with Elasticsearch, InfluxDB, Graphite, dashboard rendering, and admin RBAC
- **Splunk enterprises** — Splunk MCP v1.1.0 GA brings SPL querying, saved search execution, and AI-generated SPL to your existing Splunk investment
- **Enterprise compliance teams** — Datadog's HIPAA-eligible remote MCP server and Splunk's RBAC/rate limiting provide enterprise-grade access controls

**Who should be cautious:**

- **Multi-platform observability users** — Azure SRE Agent and AWS DevOps Agent now provide cross-platform aggregation, but you still need individual MCP servers configured for each vendor. Grafana's expanded multi-datasource support is the closest single-server unified access
- **Cost-conscious teams** — Most vendor MCP servers require paid platform subscriptions. Only Grafana (open-source self-hosted), Prometheus community servers (429 stars), and VictoriaMetrics (160 stars) are genuinely free
- **Teams expecting full autonomous remediation** — PagerDuty's write APIs are a breakthrough, but autonomous remediation (roll back deployments, scale infrastructure) still requires integration beyond MCP. Observability MCP servers enable investigation, not full remediation
- **Small teams without existing observability** — These MCP servers extend existing observability platforms to AI agents. If you don't already have Datadog/Grafana/Splunk/New Relic set up, the MCP server alone doesn't help

---

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official announcements. Originally published March 2026; refreshed May 2026. See our [About page](/about/) for details on our review process.*


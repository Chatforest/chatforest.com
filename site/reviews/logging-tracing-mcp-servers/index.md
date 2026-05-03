# Logging & Tracing MCP Servers — Splunk v1.1.1 Doubles Adoption, SigNoz Surges, Logfire Archived

> Logging and tracing MCP servers update: Splunk v1.1.1 (11K+ downloads, doubled), SigNoz v0.3.0 (most active, alerts+notifications+dashboards), Pydantic Logfire archived (hosted-only), Grafana Tempo CLI-enabled, Coralogix adds Parsing Rules + RUM


**At a glance:** Logging and tracing MCP servers specialize in **log search/analysis** and **distributed trace correlation** — the investigative layer beneath dashboards and alerts. Where [monitoring and observability MCP servers](/reviews/monitoring-observability-mcp-servers/) give you the "what" (metrics, alerts, dashboards), logging and tracing servers give you the "why" (stack traces, log patterns, request flows across services). [Splunk's official MCP server](https://splunkbase.splunk.com/app/7931) reached **v1.1.1 (April 28, 2026)** with **11,136 Splunkbase downloads** — enterprise adoption has doubled in six weeks. [SigNoz MCP](https://github.com/SigNoz/signoz-mcp-server) is now the **most actively developed** server in this category with v0.3.0 (April 28): new tools for alerts (v2 API), notification channels, saved explorer views, dashboard templates, and documentation search. [Grafana Tempo](https://grafana.com/docs/tempo/latest/api_docs/mcp-server/) (v2.10.5) now enables MCP via a single CLI flag — easier for Docker deployments. [Traceloop's OpenTelemetry MCP](https://github.com/traceloop/opentelemetry-mcp-server) (186 stars) patched security CVEs in April. [Elasticsearch community server](https://github.com/cr7258/elasticsearch-mcp-server) (270 stars) added Kubernetes/Helm deployment support. But **Pydantic Logfire archived its self-hosted MCP** on March 24 — moving fully to hosted-only, the latest in a recurring vendor pattern. This is the **fifteenth review in our [Developer Tools MCP category](/categories/developer-tools/)**.

The log management market ($3.76B in 2025, projected $7.88B by 2030) and distributed tracing market ($1.4B in 2024, projected $4.5B by 2033) reflect the critical role these tools play in production operations. OpenTelemetry is the unifying thread: production OTel adoption doubled from 6% to 11% in one year (2025–2026), with 36% of organizations experimenting. The MCP ecosystem reflects this — the OTel semantic conventions for MCP tool invocations were merged in January 2026, standardizing how traces and logs from MCP interactions are emitted. Meanwhile, 85% of organizations now use generative AI for observability, and the pattern of AI agents querying logs and traces through MCP is becoming the default debugging workflow.

**Architecture note:** Logging and tracing MCP servers follow three deployment models. **Platform-embedded** servers (Splunk official, Grafana Tempo) run inside the logging platform itself — the MCP endpoint lives at a URL on the platform's existing management port. **Standalone connectors** (Traceloop OTel MCP, Elasticsearch community, Grafana Loki MCP) run as separate processes that connect to backends via API. **Remote-hosted** servers (Coralogix, Pydantic Logfire, Axiom) run on the vendor's infrastructure with OAuth authentication. A key trend: several vendors have **deprecated self-hosted MCP** in favor of hosted-only endpoints (Honeycomb, Axiom), which simplifies setup but removes user control. Most logging servers are query-focused (search, filter, aggregate) while tracing servers add correlation capabilities (trace ID lookups, span hierarchy navigation, cross-service flow visualization).

## What's Available

### Splunk MCP Server — Enterprise Log Search Goes GA

| Aspect | Detail |
|--------|--------|
| Distribution | [Splunkbase](https://splunkbase.splunk.com/app/7931) / [CiscoDevNet/Splunk-MCP-Server-official](https://github.com/CiscoDevNet/Splunk-MCP-Server-official) |
| GitHub stars | ~4 |
| Language | Python |
| License | Splunk proprietary |
| Version | **1.1.1 (April 28, 2026)** — Beta |
| Downloads | **11,136** (doubled from ~5K since March) |
| Transport | HTTP/SSE (management port 8089) |
| Creator | Splunk/Cisco (official vendor) |

**13 tools** organized across search and AI-assisted query:

| Tool | Capability |
|------|-----------|
| splunk_run_query | Execute SPL search queries with time range support |
| splunk_get_indexes | List available indexes for targeted searching |
| splunk_get_index_info | Index metadata (size, event count, retention) |
| splunk_get_metadata | Field metadata and sourcetypes |
| splunk_get_info | Splunk instance information |
| splunk_get_user_info | Current user permissions and roles |
| splunk_get_user_list | All users (admin visibility) |
| splunk_get_kv_store_collections | KV Store collection access |
| splunk_get_knowledge_objects | Saved searches, dashboards, alerts |
| saia_generate_spl | AI-assisted SPL query generation from natural language |
| saia_explain_spl | AI-powered SPL query explanation |
| saia_optimize_spl | AI-driven SPL query optimization |
| saia_ask_splunk_question | Natural language questions about Splunk data |

**Key differentiator:** The **most widely adopted official logging MCP server** — 11,136 Splunkbase downloads (doubled since March 2026, v1.1.1 April 28). The AI-assisted tools (saia_*) use Splunk's AI to generate, explain, and optimize SPL queries, adding a natural-language layer over Splunk's powerful but complex query language. Safety guardrails include 1-minute execution limits and 1,000 event caps. RBAC integrates with existing Splunk permissions. Available on AWS Marketplace. A second official repo, **[splunk/splunk-mcp-server2](https://github.com/splunk/splunk-mcp-server2)** (Python + TypeScript), also supports SPL validation and SSE/stdio transports — giving teams Docker-deployable options alongside the platform-embedded approach.

**Limitation:** GitHub stars (4) don't reflect adoption since distribution is through Splunkbase, not GitHub. Splunk proprietary license limits customization. Requires a Splunk instance (not free). The 1,000 event cap and 1-minute timeout may be restrictive for large-scale log analysis. Platform-embedded deployment (management port 8089) means the MCP endpoint lives inside your Splunk infrastructure — no standalone deployment option. Note: Splunkbase now classifies the server as "Beta" (was "Supported" at GA) — status may reflect the v1.1.x feature work.

### Splunk Community MCP — Open-Source Alternative

| Aspect | Detail |
|--------|--------|
| Repository | [livehybrid/splunk-mcp](https://github.com/livehybrid/splunk-mcp) |
| Stars | ~99 |
| Forks | ~45 |
| Language | Python |
| License | Apache-2.0 |
| Transport | stdio, SSE, REST API |

**Key differentiator:** The **most-starred community Splunk MCP server on GitHub**, with 24x more GitHub stars than the official server's repo. FastMCP-based implementation provides SPL execution, saved search management, KV Store operations, user/role management, and health checks. Triple transport support (stdio, SSE, REST) gives more deployment flexibility than the official server's HTTP-only approach. Docker support simplifies self-contained deployment.

**Limitation:** Community-maintained — no Splunk/Cisco backing. Lacks the official server's AI-assisted query generation (saia_*) tools. No safety guardrails (execution limits, event caps) by default. **No new code commits since July 2025** — may lag behind Splunk platform updates as the official server accelerates to v1.1.x.

### Traceloop OpenTelemetry MCP — Unified Distributed Tracing

| Aspect | Detail |
|--------|--------|
| Repository | [traceloop/opentelemetry-mcp-server](https://github.com/traceloop/opentelemetry-mcp-server) |
| Stars | ~186 |
| Forks | ~17 |
| Language | Python |
| License | Apache-2.0 |
| Transport | stdio |
| Version | 0.2.2 (February 2026) |

**10 tools** across tracing and LLM observability:

| Tool | Capability |
|------|-----------|
| search_traces | Find traces by service, operation, duration, tags |
| search_spans | Query individual spans across services |
| get_trace | Retrieve full trace by ID with span hierarchy |
| list_services | Discover instrumented services |
| find_errors | Locate error spans across the system |
| get_llm_usage | LLM token consumption tracking |
| list_llm_models | Discover LLM models in use |
| get_llm_model_stats | Per-model performance statistics |
| get_llm_expensive_traces | Identify costly LLM interactions |
| get_llm_slow_traces | Find latency bottlenecks in LLM calls |

**Key differentiator:** The **only multi-backend tracing MCP server**. Queries Jaeger, Grafana Tempo, and Traceloop backends through a unified interface — switch your tracing backend without changing your MCP configuration. The LLM observability tools (5 of 10) are unique: they leverage OpenLLMetry semantic conventions to track token usage, model costs, and latency across LLM calls. Python 3.11+ required. **April 2026:** patched 12 Dependabot CVEs via dependency upgrades, confirming the project is maintained even without feature releases.

**Limitation:** v0.2.2 (February 2026) is the latest release — no new features since then. No Zipkin backend support despite being a major tracing platform. stdio-only transport limits remote deployment. The LLM observability tools require OpenLLMetry instrumentation — they're irrelevant for teams not using LLMs in their applications. 186 stars is moderate for a tracing tool.

### Grafana Tempo MCP Server — Built-in TraceQL Access

| Aspect | Detail |
|--------|--------|
| Distribution | Built into [Grafana Tempo](https://github.com/grafana/tempo) 2.9+ (~4k stars) |
| Language | Go |
| License | AGPL-3.0 |
| Latest version | **v2.10.5** (April 23, 2026) |
| Transport | Streamable HTTP (exposed at `/api/mcp`) |
| Creator | Grafana Labs (official vendor) |

**Key differentiator:** The **first tracing platform with built-in MCP support**. Tempo 2.9+ exposes an MCP endpoint at `/api/mcp` — no separate installation, no sidecar, no configuration beyond a flag. **v2.10.4 (April 13)** simplified deployment: MCP is now enabled via CLI flag `--query-frontend.mcp-server.enabled=true` instead of YAML config, making Docker/container deployments like `grafana/otel-lgtm` dramatically easier. Direct TraceQL query access with an LLM-optimized response format (`Accept: application/vnd.grafana.llm` returns flattened JSON instead of full OTel format). Works with both self-hosted Tempo and Grafana Cloud Traces — all Cloud Traces users get built-in MCP access with no plugin install.

**Limitation:** Feature flag required, API may change (still not stable). Part of the Tempo binary, so you can't run it without Tempo. TraceQL is powerful but complex — AI agents need strong prompt context to construct effective queries. AGPL-3.0 license has implications for embedding. No standalone stars count — buried in Tempo's ~4k star repo.

### Grafana Loki MCP Server — Standalone Log Querying

| Aspect | Detail |
|--------|--------|
| Repository | [grafana/loki-mcp](https://github.com/grafana/loki-mcp) |
| Stars | ~134 |
| Forks | ~28 |
| Language | Go |
| License | MIT |
| Transport | stdio, SSE (port 8080) |
| Creator | Grafana Labs (official vendor) |

**Key differentiator:** **Dedicated Loki log querying** as a lightweight standalone server. While [Grafana's mcp-grafana](/reviews/monitoring-observability-mcp-servers/) (2.5k stars) includes Loki support as one of many capabilities, loki-mcp focuses exclusively on LogQL queries with a single `loki_query` tool. Multi-tenant support via tenant ID headers. Docker-ready deployment. MIT license (more permissive than mcp-grafana's Apache-2.0 and Tempo's AGPL-3.0).

**Limitation:** Single tool (`loki_query`) — no label discovery, stream stats, or pattern detection (which mcp-grafana provides). Most teams should use mcp-grafana instead unless they specifically want Loki-only access with minimal tool surface. 103 stars suggests limited adoption relative to the parent project.

### Elasticsearch Community MCP — Surpassing the Deprecated Official Server

| Aspect | Detail |
|--------|--------|
| Repository | [cr7258/elasticsearch-mcp-server](https://github.com/cr7258/elasticsearch-mcp-server) |
| Stars | ~270 |
| Forks | ~55 |
| Language | Python |
| License | Apache-2.0 |
| Transport | stdio, SSE, Streamable HTTP |

**15+ tools** across search, index management, and cluster operations:

| Tool Category | Capabilities |
|--------------|-------------|
| Search | `search_documents`, `analyze_text`, data stream operations |
| Index management | `list_indices`, `get_index`, `create_index`, `delete_index` |
| Document CRUD | `index_document`, `get_document`, `delete_document`, `delete_by_query` |
| Cluster | `get_cluster_health`, `get_cluster_stats` |
| Aliases | `list_aliases`, `get_alias`, `put_alias`, `delete_alias` |
| General | `general_api_request` (escape hatch for any ES API) |

**Key differentiator:** **Broader tool surface than the deprecated official Elastic MCP server** (which had only 5 tools). Supports Elasticsearch 7.x/8.x/9.x AND OpenSearch 1.x/2.x/3.x — the only MCP server covering both search engines. Triple transport support. The `general_api_request` tool provides an escape hatch for any Elasticsearch API not covered by dedicated tools. **April 2026:** added Kubernetes/Helm deployment support and an OCI registry publish workflow — making enterprise container-based deployments straightforward. More active community engagement (270 stars, 55 forks) than the official server achieved before deprecation.

**Limitation:** Community-maintained with no Elastic backing. Write operations (create/delete index, document CRUD) increase risk if AI agents have unrestricted access. No new MCP tool functionality since v2.0.19 (February 2026) — April commits are infrastructure only. No integration with Elastic's newer features (ESQL, agent builder endpoint that replaced the official MCP server).

### Pydantic Logfire MCP — SQL-Based Trace and Log Querying

| Aspect | Detail |
|--------|--------|
| Repository | [pydantic/logfire-mcp](https://github.com/pydantic/logfire-mcp) ⚠️ ARCHIVED |
| Stars | ~161 |
| Forks | ~26 |
| Language | Python |
| License | MIT |
| Version | v0.8.0 (January 2026) — **final self-hosted release** |
| Transport | Remote HTTP (hosted at `logfire-us.pydantic.dev/mcp` and `logfire-eu.pydantic.dev/mcp`) |
| Creator | Pydantic (official vendor) |

**4 tools** with intentionally minimal surface:

| Tool | Capability |
|------|-----------|
| Fetch exceptions | Group exceptions by file for triage |
| Pull stack traces | Per-module stack trace retrieval |
| SQL queries | PostgreSQL-compatible SQL against all trace/log records |
| Generate links | Create Logfire UI links for further investigation |

**Key differentiator:** **SQL-based observability querying** — all trace and log data is queryable via standard PostgreSQL-compatible SQL. This is unique: while Splunk uses SPL, Grafana uses LogQL/TraceQL, and Dynatrace uses DQL, Logfire lets AI agents use the most widely understood query language. Built on OpenTelemetry, so any OTel-instrumented application works. Intentionally minimal (4 tools) to avoid context window bloat. Remote-hosted with browser-based auth. Regional endpoints (US and EU) for data residency.

**⚠️ ARCHIVED (March 24, 2026):** Pydantic archived the self-hosted `logfire-mcp` PyPI package on the same day as our original review, redirecting users to the remote-hosted MCP endpoint at `logfire-us.pydantic.dev/mcp` and `logfire-eu.pydantic.dev/mcp`. The hosted endpoint remains active and functional — this is a distribution model change, not product shutdown. Install instructions now point to the remote server directly. This is the fourth major logging/tracing MCP server to move from self-hosted to hosted-only (following Honeycomb, Axiom, and Elastic).

### AWS Log Analyzer with MCP — CloudWatch Deep Analysis

| Aspect | Detail |
|--------|--------|
| Repository | [awslabs/Log-Analyzer-with-MCP](https://github.com/awslabs/Log-Analyzer-with-MCP) |
| Stars | ~159 |
| Forks | ~25 |
| Language | Python |
| License | Apache-2.0 |
| Transport | stdio |
| Creator | AWS Labs (official) |

**Key differentiator:** **Purpose-built for CloudWatch log analysis** — not a generic log query tool but an analysis tool. Browses CloudWatch Log Groups, executes Logs Insights queries, summarizes log content, identifies error patterns, and performs cross-service log correlation. Part of AWS's broader MCP investment (awslabs/mcp monorepo now at ~8,864 stars, also includes CloudWatch metrics/alarms and Application Signals for distributed tracing).

**Limitation:** AWS-only — useless for non-CloudWatch logs. stdio transport only. No new features since launch — only routine dependency updates (python-multipart, cryptography, pygments) via Dependabot through April 2026. The awslabs/mcp monorepo has a separate CloudWatch Application Signals MCP server for distributed tracing with OTel-based root cause analysis, but the two servers are not integrated — you need both for logs + traces.

### SigNoz MCP Server — Open-Source Full-Stack Observability

| Aspect | Detail |
|--------|--------|
| Repository | [SigNoz/signoz-mcp-server](https://github.com/SigNoz/signoz-mcp-server) |
| Stars | ~88 |
| Forks | ~31 |
| Language | Go |
| License | Apache-2.0 |
| Version | **v0.3.0 (April 28, 2026)** |
| Transport | stdio, HTTP/SSE |
| Creator | SigNoz (official vendor, open-source) |

**Key differentiator:** **The most actively developed logging/tracing MCP server in this category** — v0.3.0 shipped April 28 with a wave of additions since March 24: JWT token support, OTel GenAI semantic instrumentation, alert management (new `signoz_create_alert` using v2 Rules API), notification channel CRUD (`signoz_create_notification_channel`, `signoz_update_notification_channel`, `signoz_list_notification_channels`), saved explorer view CRUD (create/update/list/delete), `signoz_create_dashboard_from_template` with a template catalog, and documentation tools (`signoz_search_docs`, `signoz_fetch_doc`). The v0.3.0 release adds enriched tool-call observability with MCP protocol version, error type, and result size. **OpenTelemetry-native full-stack observability** — logs, traces, and metrics in a single MCP server. Unlike vendor-locked alternatives, SigNoz is fully open-source (Apache-2.0).

**Limitation:** 88 stars indicates early adoption relative to its feature depth. SigNoz itself, while growing, has a fraction of Grafana's or Datadog's market share. Go implementation requires compilation or Docker deployment. The combined surface (logs + traces + metrics + alerts + dashboards + docs) produces a large tool count that may challenge context windows. Rapid development means some newer tools may have rough edges.

## Also Available

### Coralogix MCP Server (Official)

Remote-hosted streamable HTTP server from [Coralogix](https://coralogix.com/docs/user-guides/mcp-server/overview/). Logs, traces, metrics, SIEM data, and RUM querying via DataPrime query language. OAuth authentication. **Since March 2026:** added **Parsing Rules Management** (create/read/update/delete rules across 10 rule types, generate Terraform HCL + Kubernetes Operator YAML + OpenAPI definitions from any rule) and **RUM tools** (query frontend/mobile app performance, top errors, Web Vitals, user interactions, SDK setup guidance). Express-based architecture. Commercial platform — no open-source option.

### Axiom MCP Server (Archived → Hosted)

[axiomhq/mcp-server-axiom](https://github.com/axiomhq/mcp-server-axiom) (58 stars, archived March 2026) — self-hosted Go server with 6 tools (APL queries, datasets, saved queries, monitors). **Deprecated** in favor of hosted MCP at mcp.axiom.co (Cloudflare Workers). Additional hosted tools for event ingestion and dataset creation. The self-hosted → hosted-only transition is a recurring pattern in this category.

### OpenTelemetry Collector MCP (otelcol-mcp)

[mottibec/otelcol-mcp](https://github.com/mottibec/otelcol-mcp) (51 stars, TypeScript, GPL-3.0) — dynamic OpenTelemetry Collector configuration management. Not a query tool but a **config management** tool: manages receivers, processors, and exporters. Useful for teams that need AI agents to modify their telemetry pipeline configuration. SSE transport.

### Honeycomb MCP Server (Deprecated → Enterprise Hosted)

[honeycombio/honeycomb-mcp](https://github.com/honeycombio/honeycomb-mcp) (41 stars, TypeScript, MIT) — 10 tools for dataset querying, SLOs, triggers, and trace linking. **Deprecated** in favor of hosted MCP at docs.honeycomb.io. Enterprise-only. Another example of the self-hosted-to-hosted migration pattern.

### Mezmo MCP Server (Official)

[mezmo/mezmo-mcp](https://github.com/mezmo/mezmo-mcp) (5 stars, remote HTTP) — root-cause analysis, pipeline management, and log export/filtering. Cloud-hosted from Mezmo (formerly LogDNA).

### Seq MCP Server (Community)

[willibrandon/seq-mcp-server](https://github.com/willibrandon/seq-mcp-server) (10 stars, C#, MIT) — 3 tools for the Seq structured logging platform: event search, real-time event capture (5-second timeout), and signal listing. .NET 9.0 required. Seq CLI also gaining built-in MCP support via `seqcli mcp run`.

### Graylog MCP Servers (Community)

Community implementations: [lcaliani/graylog-mcp](https://github.com/lcaliani/graylog-mcp) (6 stars, JavaScript, 1 tool), [Pranavj17/mcp-server-graylog](https://github.com/Pranavj17/mcp-server-graylog) (2 stars, JavaScript, 4 tools). **Note:** AI-enthusiasts/mcp-graylog (previously the most complete at 11 tools) was **deleted** (404) — verify any links to this repo. Graylog also has native MCP integration documented at go2docs.graylog.org for direct queries, system information, and admin tasks.

### Sumo Logic MCP (Official Beta + Community)

**Official:** Sumo Logic announced an official MCP server at RSAC 2026 (presented live, April 2026) as part of the Dojo AI initiative. Status: **limited beta/preview**. Not yet open-sourced or GA — broader availability described as "coming soon." No GitHub repo yet.

**Community:** [samwang0723/mcp-sumologic](https://github.com/samwang0723/mcp-sumologic) (10 stars, TypeScript, last pushed March 2026) and [vinit-devops/sumologic_mcp](https://github.com/vinit-devops/sumologic_mcp) (4 stars, Python, 37 tools — covering search, dashboards, metrics, collectors, monitors, and config utilities, last pushed October 2025).

### Liatrio OTel Instrumentation MCP

[liatrio-labs/otel-instrumentation-mcp](https://github.com/liatrio-labs/otel-instrumentation-mcp) (18 stars, Python, Apache-2.0) — not a query tool but an **instrumentation guide**. Provides OTel documentation, examples, semantic conventions, and instrumentation guidance to AI coding assistants. Self-instrumented with distributed tracing. Useful for teams adopting OpenTelemetry.

### Community Loki MCP Servers

[tumf/grafana-loki-mcp](https://github.com/tumf/grafana-loki-mcp) (23 stars, Python, 4 tools) and [lexfrei/mcp-loki](https://github.com/lexfrei/mcp-loki) (2 stars, Go, 4 tools, v1.1.0 March 2026 — multi-arch containers with Cosign signing). Both provide more tools than the official Grafana loki-mcp but have less adoption.

### Notable Gaps

**No Fluentd or Fluent Bit MCP server** — Despite Fluentd's role as the "F" in the EFK stack and Fluent Bit's 1B+ deployments, neither has an MCP server for pipeline configuration or log routing management. This gap is confirmed as of May 2026 — rumors of an OpAMP-based bridge have not materialized in any public repository.

**No Zipkin MCP server** — Zipkin, one of the original distributed tracing systems, has zero MCP presence. Traceloop supports Jaeger and Tempo but not Zipkin.

**No Papertrail or Loggly MCP servers** — SolarWinds' popular cloud logging platforms have no MCP integration.

**Logstash MCP server exists in name only** — [mashhurs/logstash-mcp-server](https://github.com/mashhurs/logstash-mcp-server) (1 star, 2 commits, last pushed June 2025) is an abandoned prototype. The official `elastic/logstash` repo shows no MCP integration. For practical purposes, Logstash has no MCP tooling.

**No dedicated syslog or journal MCP server** — systemd journal and traditional syslog have no MCP query interfaces.

## Developer Tools MCP Comparison

| Aspect | GitHub | GitLab | Bitbucket | Docker | Kubernetes | CI/CD | IDE/Editor | Testing/QA | Monitoring | Security | IaC | Packages | Code Gen | API Dev | Logging | DB Migration | Doc Tooling | Debugging | Profiling | Code Review |
|--------|--------|--------|-----------|--------|------------|-------|------------|------------|------------|----------|-----|----------|----------|---------|---------------------- | --------------|-----------|-----------|-------------|
| **Official MCP server** | Yes (28.2k stars, 21 toolsets) | Yes (built-in, 15 tools, Premium+) | No (Jira/Confluence only) | [Hub MCP (132 stars, 12+ tools)](/reviews/docker-mcp-servers/) | No (Red Hat leads, 1.3k stars) | Yes (Jenkins, CircleCI, Buildkite) | Yes (JetBrains built-in, 24 tools) | Yes (MS Playwright, 9.8k stars, 24 tools) | Yes (Grafana 2,907 stars v0.12.0, Datadog, Sentry, Dynatrace, New Relic, Instana) | Yes (Semgrep, SonarQube, Snyk, Trivy, GitGuardian, Cycode, Contrast) | Yes (Terraform 1.4k, Pulumi remote, AWS IaC, Bicep, Ansible AAP) | Yes (NuGet built-in VS 2026, WinGet built-in, Homebrew built-in) | Partial (Vercel next-devtools 694, E2B archived, JetBrains built-in server) | Yes (Postman 227 v2.8.7 OAuth remote, Apollo 275 v1.13.0, Apigee managed, MuleSoft v1.4, Salesforce GA) | Yes (Splunk v1.1.1 11K+ downloads, Grafana Tempo v2.10.5 CLI-enabled, Grafana Loki 134 stars, Sumo Logic limited beta) | Partial (Liquibase private preview 19 tools, Prisma built-in CLI v6.6.0+) | Yes (Microsoft Learn 1.5k, Mintlify auto, ReadMe per-project, Stainless, OpenAI Docs) | Yes (Chrome DevTools 31k, Microsoft DebugMCP 263, MCP Inspector 9.2k official) | Partial (CodSpeed MCP, Polar Signals remote, Grafana Pyroscope via mcp-grafana) | Yes (SonarQube 538 stars, Codacy 56 stars, Graphite GT built-in) |
| **Top community server** | GitMCP (7.8k stars) | zereight/gitlab-mcp (1.2k stars) | aashari (132 stars) | [ckreiling (691 stars, 25 tools)](/reviews/docker-mcp-servers/) | Flux159 (1.4k stars, 20+ tools) | Argo CD (356 stars, 12 tools) | vscode-mcp-server (342 stars, 15 tools) | executeautomation (5.3k stars) | pab1it0/prometheus (340 stars) | CodeQL community (19 stars) | Ansible (27 stars, 40+ tools) | mcp-package-version (122 stars, 9 registries) | Context7 (54.2k stars), magic-mcp (4.8k stars) | openapi-mcp-server (889 stars), openapi-mcp-generator (576 stars), Agoda APIAgent (271 stars) | cr7258/elasticsearch (270 stars, Kubernetes support), SigNoz (88 stars v0.3.0, most active), Traceloop OTel (186 stars) | mpreziuso/mcp-atlas (Atlas), defrex/drizzle-mcp (Drizzle) | GitMCP (7.8k stars), Grounded Docs (1.2k stars), Docs MCP (87 stars) | claude-debugs-for-you (496 stars), x64DbgMCPServer (398 stars), devtools-debugger (341 stars) | theSharque/mcp-jperf (Java JFR), PageSpeed Insights MCP servers | kopfrechner/gitlab-mr-mcp (86 stars), crazyrabbitLTC (32 stars) |
| **Primary function** | Repository operations | Repository operations | Repository operations | Container lifecycle | Cluster management | Pipeline management | Editor integration | Test execution | Observability queries | Vulnerability scanning | Infrastructure provisioning | Dependency intelligence | Context provision + UI generation | Spec-to-server conversion + API interaction | Log search/analysis + trace correlation | Schema migration & version control | Doc access, search, generation & quality | Breakpoints, stepping, variable inspection, crash analysis | Flamegraph analysis, CPU/memory profiling, benchmarks, web audits, load testing | Code quality analysis, PR management, diff review, stacked PR creation |
| **Vendor count** | 1 (GitHub) | 1 (GitLab) | 0 (Atlassian via Jira only) | 1 (Docker) + community | 0 (Red Hat leads community) | 3 (Jenkins, CircleCI, Buildkite) | 1 (JetBrains) | 1 (Microsoft) | 6 (Grafana, Datadog, Sentry, Dynatrace, New Relic, Instana) | 7+ (Semgrep, SonarQube, Snyk, Trivy, GitGuardian, Cycode, Contrast) | 5+ (HashiCorp, Pulumi, AWS, OpenTofu, Spacelift) | 2 (Microsoft/NuGet, Homebrew) | 3 (Vercel, E2B, Upstash/Context7) | 4+ (Postman, Apollo, Kong, Google/Apigee, MuleSoft) | 6+ (Splunk, Grafana/Loki, Grafana/Tempo, Coralogix, Axiom, Mezmo) | 2 (Liquibase, Prisma) + Google partial | 5+ (Microsoft, Mintlify, ReadMe, Stainless, OpenAI, Vonage, Fern, Apidog) | 3 (Google/Chrome DevTools, Microsoft/DebugMCP, LLVM/LLDB built-in) | 3 (CodSpeed, Polar Signals, Tricentis/NeoLoad) + Grafana partial | 3 (SonarSource, Codacy, Graphite) + CodeRabbit as client |
| **Code generation role** | Context (repos, issues, PRs) | Context (repos, issues, MRs) | Context (repos, PRs) | Context (images, containers) | Context (cluster state) | Context (pipeline status) | Bidirectional (tools + context) | Context (test results) | Context (metrics, logs) | Context (vulnerabilities) | Generation (IaC templates) | Context (versions, advisories) | Direct (UI components, docs, execution) | Bidirectional (spec-to-tools, API execution) | Context (log patterns, traces, errors) | Bidirectional (migration generation + schema inspection) | Context (doc access/search) + Generation (doc output) | Bidirectional (set breakpoints + inspect state) | Context (profiles, flamegraphs, benchmarks) + Generation (benchmark harnesses) | Bidirectional (quality data as context + review comments as output) |
| **Authentication** | PAT / GitHub App | OAuth 2.0 / PAT | App Password / OAuth | Docker Desktop credentials | kubeconfig / OAuth / OIDC | API tokens per platform | Local connection (port/stdio) | None (local browsers) | API tokens / OAuth (remote) | API tokens / CLI auth | API tokens / OAuth / CLI auth | None (public registries) | API keys (Context7, magic-mcp, E2B) | API keys / Bearer / OAuth / 1Password | API tokens / OAuth / RBAC (Splunk) | Database credentials / CLI auth | None (GitMCP, MS Learn) / API keys (platform MCP) | None (local debuggers) / Chrome DevTools auto-connect | API keys (CodSpeed, Polar Signals) / Grafana auth / Google API key (PageSpeed) | API tokens (SonarQube, Codacy) / GitHub PAT / GitLab PAT |
| **AAIF membership** | No (but Microsoft is Platinum) | No | No | [Gold](/reviews/docker-mcp-servers/) | No (but Google/AWS/MS are Platinum) | No | No (but Microsoft is Platinum) | No (but Microsoft is Platinum) | No | No | No | No (but Microsoft is Platinum) | No | No | No | No | No (but Microsoft is Platinum) | No (but Google/Microsoft are Platinum) | No | No |
| **Platform users** | 180M+ developers | 30M+ users | ~41k companies | 20M+ users | 5.6M developers | Jenkins: 11.3M devs | VS Code: 75.9% market share | Playwright: 45.1% QA adoption | Datadog: 32.7k customers | SonarQube: 17.7% SAST mindshare | Terraform: millions of users, 45% IaC adoption | npm: 5B+ weekly downloads | Copilot: 20M+ users, Cursor: 1M+ DAU | Postman: 30M+ users, REST: ~83% of web APIs | Splunk: 15k+ customers, ELK: most-deployed log stack | Prisma: 43k stars, Flyway: 10.7k stars, Atlas: 6.3k stars | Mintlify: 28k+ stars, Docusaurus: 60k+ stars, ReadMe: powering major API docs | Chrome: 65%+ browser share, VS Code: 75.9% IDE share, x64dbg: 45k+ stars | APM market: $7-10B, Pyroscope: 11k+ stars, async-profiler: 9k+ stars | SonarQube: 7.4M+ users, CodeRabbit: top AI reviewer, Qodo/PR-Agent: 10.5k stars |
| **Our rating** | [4.5/5](/reviews/github-mcp-server/) | [3.5/5](/reviews/gitlab-mcp-server/) | [2.5/5](/reviews/bitbucket-mcp-server/) | [4/5](/reviews/docker-mcp-servers/) | [4/5](/reviews/kubernetes-mcp-servers/) | [3/5](/reviews/ci-cd-mcp-servers/) | [3.5/5](/reviews/ide-code-editor-mcp-servers/) | [3.5/5](/reviews/testing-qa-mcp-servers/) | [4/5](/reviews/monitoring-observability-mcp-servers/) | [4.5/5](/reviews/security-scanning-mcp-servers/) | [4/5](/reviews/infrastructure-as-code-mcp-servers/) | [3.5/5](/reviews/package-management-dependency-mcp-servers/) | [3.5/5](/reviews/code-generation-mcp-servers/) | [4/5](/reviews/api-development-mcp-servers/) | 4/5 | [2.5/5](/reviews/database-migration-mcp-servers/) | [3.5/5](/reviews/documentation-tooling-mcp-servers/) | [4.5/5](/reviews/debugging-mcp-servers/) | [3/5](/reviews/profiling-performance-mcp-servers/) | [3.5/5](/reviews/code-review-pull-request-mcp-servers/) |

## Known Issues

1. **Overlap with monitoring MCP servers creates confusion** — Grafana's mcp-grafana already includes Loki LogQL querying, and Datadog's official MCP server covers logs, traces, and metrics. Teams using full-stack observability platforms may not need dedicated logging/tracing MCP servers at all. The boundary between "monitoring" and "logging/tracing" MCP servers is blurry — Dynatrace DQL queries logs and spans, New Relic covers NRQL log queries. This category overlap makes tool selection harder, not easier.

2. **Vendor deprecation of self-hosted MCP is a recurring pattern** — Elastic deprecated their MCP server (632 stars) in favor of a proprietary Agent Builder endpoint. Honeycomb deprecated their self-hosted server (41 stars) for enterprise-only hosted MCP. Axiom archived their Go server (58 stars) for hosted-only. The trend is clear: vendors ship self-hosted MCP to attract developers, then pull it back to hosted-only to capture enterprise contracts. Teams building on self-hosted logging MCP servers face migration risk.

3. **Query language fragmentation across MCP servers** — Splunk uses SPL, Grafana uses LogQL (logs) and TraceQL (traces), Elasticsearch uses Query DSL, Dynatrace uses DQL, Coralogix uses DataPrime, Axiom uses APL, Logfire uses SQL, and SigNoz uses its own syntax. AI agents querying logs through MCP must handle 8+ query languages depending on which backend is configured. There's no cross-platform query abstraction — OpenTelemetry standardized telemetry collection but not querying.

4. **OpenTelemetry MCP semantic conventions are brand new** — The OTel semantic conventions for MCP tool invocations were merged in January 2026, defining standard attributes (`gen_ai.operation.name`, `mcp.method.name`, `mcp.resource.uri`). But adoption is early — most MCP servers don't emit OTel-compliant traces of their own execution yet. The standard exists; the implementation lags. This means tracing MCP server behavior itself is still inconsistent.

5. **Traceloop's multi-backend promise has a Zipkin gap** — The only multi-backend tracing MCP server (186 stars, v0.2.2) supports Jaeger and Grafana Tempo but not Zipkin, one of the three major open-source tracing backends. Teams using Zipkin have no MCP tracing option at all. An April 2026 dependency security fix (12 Dependabot CVEs patched) confirms the project is maintained — but feature development remains stalled.

6. **Log pipeline management has zero MCP coverage** — Fluentd, Fluent Bit, Logstash, and Vector — the tools that route, transform, and deliver logs — have no MCP servers. AI agents can query logs once they arrive at a platform but cannot configure how logs get there. For infrastructure teams, pipeline management is often more complex than log querying.

7. **Write operations in Elasticsearch community server lack safeguards** — The most-starred log search MCP server (cr7258, 259 stars) includes `create_index`, `delete_index`, `delete_document`, `delete_by_query`, and a `general_api_request` escape hatch. An AI agent with unrestricted access could delete indices or bulk-delete documents. Unlike Splunk's official server (which has execution limits and event caps), the community server has no built-in safety guardrails.

8. **Splunk's official server has low GitHub visibility despite real adoption** — 4 GitHub stars vs. 11,136+ Splunkbase downloads. The distribution via Splunkbase rather than GitHub means the server doesn't appear in GitHub-based MCP server directories and discovery tools. Teams searching GitHub for "Splunk MCP" find the community server (99 stars) first, potentially missing the official server now at v1.1.1. A second official repo (splunk/splunk-mcp-server2) adds to the discovery confusion.

9. **Grafana has three separate logging/tracing MCP servers** — mcp-grafana (2.5k stars, includes Loki), loki-mcp (103 stars, standalone Loki), and Tempo built-in MCP (part of Tempo 2.9+). The documentation doesn't clearly guide users on which to use when. Most teams should use mcp-grafana for logs + everything else, but the standalone servers exist for edge cases that aren't well-documented.

10. **No cross-platform log correlation through MCP** — Each MCP server queries one backend. There's no MCP server (or pattern) for correlating logs across Splunk + Elasticsearch + CloudWatch in a multi-platform environment. In practice, many organizations use multiple logging platforms. The MCP ecosystem assumes single-backend querying.

## Bottom Line

**Rating: 4 out of 5** *(upgraded from 3.5)*

Logging and tracing MCP servers have hit an enterprise inflection point since March 2026. **Splunk's official server reached v1.1.1 with 11,136 downloads** — a doubling in six weeks that signals genuine enterprise production adoption. **SigNoz emerged as the most actively developed server in the category** with v0.3.0 (April 28): new alert management (v2 API), notification channels, saved explorer views, dashboard templates, and documentation search — all in six weeks of development. **Grafana Tempo's MCP is now enabled via a single CLI flag** (v2.10.4), removing the biggest friction point for Docker/container deployments. **Coralogix added Parsing Rules management and RUM tools** — now covering more of the observability lifecycle. **Sumo Logic entered with an official MCP in limited beta** — a fourth major log platform with vendor commitment alongside Splunk, Grafana, and Coralogix.

But the vendor deprecation pattern accelerated: **Pydantic Logfire archived its self-hosted MCP** on March 24, moving to hosted-only — joining Elastic, Honeycomb, and Axiom in a pattern that now affects four of the most notable logging/tracing MCP servers. Log pipeline management remains at zero — confirmed searches find no usable Fluent Bit, Fluentd, or Logstash MCP server in May 2026.

The **4/5 rating** (upgraded from 3.5) reflects: Splunk's 11K+ download adoption surge, SigNoz's exceptional v0.3.0 feature velocity, Grafana Tempo's easier deployment (CLI flag), Coralogix's expanded toolset, and Sumo Logic entering the space. It holds below 4.5 for the accelerating self-hosted deprecation pattern (four major servers now hosted-only), zero log pipeline management tooling (Fluentd/Fluent Bit/Logstash — confirmed gaps), query language fragmentation (8+ languages with no abstraction), Traceloop's Zipkin gap, and lack of cross-platform log correlation.

**Who benefits from logging & tracing MCP servers today:**

- **Splunk teams** — v1.1.1 with AI-assisted SPL generation, 11K+ downloads proving production viability. Also consider splunk/splunk-mcp-server2 for Docker-based deployments
- **Grafana/Loki teams** — mcp-grafana (2,907 stars, v0.12.0) or standalone loki-mcp (134 stars) for LogQL. Tempo v2.10.5 (CLI-enabled MCP) adds TraceQL. Grafana Cloud users get MCP built-in
- **Elasticsearch/OpenSearch teams** — cr7258's community server (270 stars, Kubernetes/Helm support) provides 15+ tools covering both ES and OpenSearch. More capable than the deprecated official server
- **SigNoz teams** — v0.3.0 is by far the most feature-complete open-source full-stack logging/tracing MCP, with logs, traces, metrics, alerts, notification channels, and dashboard templates
- **Python/OTel teams** — Pydantic Logfire's remote MCP endpoint remains active despite archiving self-hosted; Traceloop (186 stars, v0.2.2) provides multi-backend tracing for Jaeger/Tempo users

**Who should wait:**

- **Multi-platform teams** — No cross-platform log correlation exists. If you use Splunk + CloudWatch + Elasticsearch, you need three separate MCP servers with no integration
- **Infrastructure teams managing log pipelines** — Fluent Bit, Fluentd, and Logstash have no usable MCP servers. You're on your own for pipeline configuration
- **Zipkin users** — No MCP server supports Zipkin, not even Traceloop's multi-backend server
- **Teams wary of vendor lock-in** — Four major servers (Elastic, Honeycomb, Axiom, Logfire) have now moved to hosted-only. The pattern shows no signs of reversing
- **Sumo Logic teams hoping for GA** — The official MCP is in limited beta/preview as of May 2026; broader availability is "coming soon" with no firm date

---

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official announcements. First published March 2026, last refreshed May 2026. See our [About page](/about/) for details on our review process.*


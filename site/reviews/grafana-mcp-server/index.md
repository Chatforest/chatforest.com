# Grafana MCP Server Review — 40+ Tools, Open Source

> Grafana's official MCP server connects AI agents to dashboards, Prometheus, Loki, Pyroscope, ClickHouse, CloudWatch, Elasticsearch, alerts, incidents, and OnCall — 40+ tools across 16 categories.


**At a glance:** 2,800+ GitHub stars, 328 forks, v0.11.6 (April 9, 2026), ~807K all-time PulseMCP visitors (#70 globally, ~18.8K weekly), 40+ tools across 16 categories, Apache 2.0.

The Grafana MCP server gives AI agents direct access to your Grafana instance and the surrounding observability ecosystem — dashboards, Prometheus metrics, Loki logs, Pyroscope profiling data, ClickHouse analytics, CloudWatch metrics, Elasticsearch searches, alerting rules, incident management, OnCall schedules, and Sift investigations. All from one server.

It's official. Grafana Labs builds and maintains it at [grafana/mcp-grafana](https://github.com/grafana/mcp-grafana). With 2,800 GitHub stars, 328 forks, 536 commits, and 18+ releases since December 2025, it's the most popular observability MCP server by community adoption — nearly five times Sentry's star count. Written in Go, licensed Apache 2.0.

This is the second observability MCP server we've reviewed after [Sentry](/reviews/sentry-mcp-server/) (4/5). Where Sentry is deep and narrow — laser-focused on error tracking with proprietary AI analysis — Grafana is wide and extensible. It connects to whatever data sources your Grafana instance already has, which could be dozens of backends. The trade-off: breadth over depth.

## What's New (April 2026 Update)

**Three releases in two weeks (v0.11.4–v0.11.6).** After a quiet period post-v0.11.3 (March 12), Grafana shipped three releases in rapid succession:

**v0.11.4 (April 2) — Pyroscope profiling and platform expansion:**
- **Pyroscope profiling tools (NEW CATEGORY):** Series query and unified query tool for continuous profiling data exploration — fetch profiles showing which functions consume resources and metrics showing when consumption spiked. Adds profile type discovery across Pyroscope datasources. This brings the tool category count from 15 to 16.
- Generic Kubernetes-style API client for Grafana app platform resources
- `--session-idle-timeout-minutes` CLI flag for automatic idle session closure in SSE/streamable-http modes
- Server-side filtering for alert rule operations
- PromQL query support against **Google Cloud Monitoring** datasources — extending multi-cloud reach
- **Memory leak fix** in streamable-http mode through proper resource cleanup
- Endpoint fallback between `/resources` and `/proxy` for broader datasource compatibility

**v0.11.5 (April 9) — SSO and enterprise auth:**
- **Request header forwarding** (Cookie and Authorization) to Grafana in SSE and streamable-http modes — enables SSO and ALB session cookie support. This is a significant enterprise feature: teams using SAML, OAuth, or load balancer-based authentication can now pass those credentials through to Grafana without separate service account tokens.
- Optional `projectName` parameter for Cloud Monitoring datasources targeting specific GCP projects
- `BaseTransport` field in `GrafanaConfig` for custom HTTP transport composition
- Elasticsearch query field extraction fix in alert rule summaries

**v0.11.6 (April 9) — Delegated identity:**
- **On-behalf-of authentication headers** in the Grafana client transport chain — facilitating delegated identity for API requests. Combined with v0.11.5's header forwarding, this positions the MCP server for proper enterprise identity chains.
- Dashboard identity field preservation fix in patch mode — prevents unintended dashboard duplication

**Grafana 13 released (April 14).** The [annual major Grafana release](https://grafana.com/docs/grafana/latest/whatsnew/) dropped just ahead of [GrafanaCON 2026 in Barcelona (April 20–22)](https://grafana.com/events/grafanacon/). Grafana 13 includes Grafana Advisor GA and deprecates numeric ID-based datasource APIs (disabled by default). The MCP server had a known TextConsumer parsing error with Grafana v12 ([#635](https://github.com/grafana/mcp-grafana/issues/635)) — teams upgrading to v13 should verify compatibility.

**Azure Managed Grafana MCP launched (March 18).** Microsoft announced a [managed MCP endpoint for Azure Managed Grafana](https://techcommunity.microsoft.com/blog/azureobservabilityblog/introducing-azure-managed-grafana-mcp-the-managed-data-gateway-for-ai-agents/4503619) — enabled by default on Azure Managed Grafana instances. It queries Azure Monitor metrics/logs, Application Insights, and Kusto, using Azure RBAC and managed identities (no separate auth setup). This is a separate managed offering from the open-source `mcp-grafana`, but it validates the approach and expands the Grafana MCP ecosystem to Azure-native teams.

**Datadog MCP server went GA (March 10).** Grafana's primary competitor launched as a [remote MCP server](https://www.helpnetsecurity.com/2026/03/10/datadog-mcp-server/) — no local install needed. Works with Claude Code, Cursor, OpenAI Codex CLI, GitHub Copilot, and Azure SRE Agent out of the box. This makes Datadog the easier-to-set-up option, widening the gap on Grafana's "no hosted remote server" weakness.

**Grafana Labs on MCP observability.** Blog posts cover [monitoring MCP servers with OpenLIT and Grafana Cloud](https://grafana.com/blog/ai-observability-MCP-servers/) and [optimizing cloud costs with Grafana Assistant and MCP servers](https://grafana.com/blog/from-signals-to-savings-optimizing-cloud-costs-with-grafana-assistant-and-mcp-servers/) — positioning Grafana not just as an MCP tool provider, but as the observability layer *for* MCP infrastructure.

## What It Does

The server exposes 40+ tools across 15 configurable categories. Several categories are disabled by default to manage context window size — you enable only what you need.

**Dashboard Management** (enabled by default)
- `search_dashboards` — find dashboards by title or metadata
- `get_dashboard_by_uid` — retrieve full dashboard JSON
- `get_dashboard_summary` — compact overview without the full JSON (recommended for context efficiency)
- `get_dashboard_property` — extract specific parts via JSONPath expressions
- `update_dashboard` — create or modify dashboards
- `patch_dashboard` — apply targeted changes without needing the full JSON
- `get_dashboard_panel_queries` — extract panel titles, queries, and datasource UIDs

**Dashboard Query Execution** (disabled by default)
- `run_panel_query` — execute a dashboard panel's query with custom time ranges and variable overrides, supporting Prometheus, Loki, ClickHouse, and CloudWatch datasources

**Datasource Operations** (enabled by default)
- `list_datasources` — view all configured datasources
- `get_datasource` — retrieve datasource details by UID or name

**Prometheus Querying** (enabled by default)
- `query_prometheus` — execute PromQL instant and range queries
- `list_prometheus_metric_metadata` — retrieve metric metadata
- `list_prometheus_metric_names` — list available metrics
- `list_prometheus_label_names` — query labels matching selectors
- `list_prometheus_label_values` — retrieve specific label values
- `query_prometheus_histogram` — calculate percentiles (p50, p90, p95, p99)

**Loki Querying** (enabled by default)
- `query_loki_logs` — run LogQL log and metric queries
- `list_loki_label_names` — list available log labels
- `list_loki_label_values` — retrieve label value lists
- `query_loki_stats` — get stream statistics
- `query_loki_patterns` — identify common log structures

**ClickHouse Querying** (disabled by default)
- `list_clickhouse_tables` — list database tables with row counts and sizes
- `describe_clickhouse_table` — get column names, types, and metadata
- `query_clickhouse` — execute SQL with macro and variable substitution

**CloudWatch Querying** (disabled by default)
- `list_cloudwatch_namespaces` — discover AWS namespaces
- `list_cloudwatch_metrics` — list namespace metrics
- `list_cloudwatch_dimensions` — get metric dimensions
- `query_cloudwatch` — execute CloudWatch metric queries

**Elasticsearch Querying** (disabled by default)
- `query_elasticsearch` — execute searches via Lucene syntax or Query DSL with time range support

**Log Search** (disabled by default)
- `search_logs` — high-level log search across ClickHouse (OTel) and Loki

**Incident Management** (enabled by default)
- `list_incidents` — view incidents in Grafana Incident
- `create_incident` — create new incidents
- `add_activity_to_incident` — add activity items to incidents
- `get_incident` — retrieve specific incident details

**Sift Investigations** (enabled by default)
- `list_sift_investigations` — retrieve investigations
- `get_sift_investigation` — get investigation details by UUID
- `get_sift_analyses` — retrieve specific analyses
- `find_error_patterns_in_logs` — detect elevated errors in Loki
- `find_slow_requests` — detect slow requests via Tempo traces

**Alerting** (enabled by default)
- `alerting_manage_rules` — list, get, create, update, and delete alert rules
- `alerting_manage_routing` — manage notification policies, contact points, and time intervals
- Supports both Grafana-managed and datasource-managed rules (Prometheus/Loki)

**OnCall** (enabled by default)
- `list_oncall_schedules` — view on-call schedules
- `get_oncall_shift` — retrieve shift details
- `get_current_oncall_users` — see who's on call right now
- `list_oncall_teams` / `list_oncall_users` — view teams and users
- `list_alert_groups` — filter alerts by state, integration, labels, or time range
- `get_alert_group_details` — retrieve specific alert group information

**Navigation** (enabled by default)
- `generate_deeplinks` — create accurate URLs for dashboards, panels, Explore views, with time ranges and query parameters

**Annotations** (enabled by default)
- `get_annotations` — query annotations by time range, dashboard UID, or tags
- `create_annotation` / `create_graphite_annotation` — create dashboard or Graphite annotations
- `update_annotation` / `patch_annotation` — full or partial annotation updates
- `get_annotation_tags` — list tags with optional filtering

**Rendering** (enabled by default)
- `get_panel_image` / `get_dashboard_image` — render panels or dashboards as PNG images (base64 encoded), with customizable dimensions, time ranges, themes, and variables

**Admin Management** (disabled by default)
- `list_teams` / `list_users_by_org` — view teams and users
- `list_all_roles` / `get_role_details` / `get_role_assignments` — inspect RBAC roles
- `list_user_roles` / `list_team_roles` — view role assignments
- `get_resource_permissions` / `get_resource_description` — inspect resource-level permissions

**Pyroscope Profiling** (disabled by default) — *new in v0.11.4*
- `query_pyroscope` — unified query tool for fetching profiles (which functions consume resources) or metrics (when consumption spiked) from Pyroscope datasources
- `list_pyroscope_profile_types` — discover available profile types in a Pyroscope datasource and time range

**Query Examples** (disabled by default)
- `get_query_examples` — retrieve example queries for datasource types

The configurable categories are the key design decision. Grafana's full tool surface would consume ~16K tokens of context window — far too much for most agents. The `--disable-<category>` and `--enabled-tools` flags let you trim this to exactly the tools you need. Want just Prometheus and dashboards? Disable everything else. Want incident response? Enable incidents and OnCall, disable querying. This is the most granular tool management of any MCP server we've reviewed.

## Setup

Grafana offers four installation methods:

**UV (recommended for local use):**

```json
{
  "mcpServers": {
    "grafana": {
      "command": "uvx",
      "args": ["mcp-grafana"],
      "env": {
        "GRAFANA_URL": "http://localhost:3000",
        "GRAFANA_SERVICE_ACCOUNT_TOKEN": "<your-token>"
      }
    }
  }
}
```

**Docker:**

```json
{
  "mcpServers": {
    "grafana": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm",
        "-e", "GRAFANA_URL=http://host.docker.internal:3000",
        "-e", "GRAFANA_SERVICE_ACCOUNT_TOKEN=<your-token>",
        "mcp/grafana"
      ]
    }
  }
}
```

Also available as a native Go binary and via Helm chart for Kubernetes deployments.

The server supports **stdio** (default), **SSE**, and **Streamable HTTP** transports. SSE runs on port 8000 by default and supports TLS. This means you can run it as a shared service — one Grafana MCP instance serving multiple agents or team members.

Authentication uses Grafana **service account tokens** — you create a service account in your Grafana instance with the appropriate RBAC permissions. Each tool requires specific permissions (e.g., `dashboards:read` for viewing, `datasources:query` for querying, `alert.rules:write` for managing alerts). For a quick start, the Editor built-in role covers most operations.

A `--disable-write` flag provides read-only mode — preventing any write operations like creating dashboards, modifying alerts, or creating incidents. This is essential for production environments where you want to give agents observability access without the ability to change anything.

## What's Good

**The most comprehensive observability MCP server that isn't locked to a single vendor.** Grafana's core value proposition is that it works with *whatever backends you already use*. Prometheus, Loki, Tempo, ClickHouse, CloudWatch, Elasticsearch — the MCP server inherits Grafana's multi-datasource architecture. Datadog's MCP server has more tools (50+), but they all query Datadog. Grafana's tools query your existing infrastructure regardless of vendor.

**Configurable tool categories prevent context window bloat.** At 40+ tools and ~16K tokens of tool descriptions, you'd waste your context budget loading everything. The `--disable-<category>` flags let you present only what matters. This is better than Sentry (which loads all ~20 tools every time) and smarter than AWS MCP (which has role-based configurations but less granular control). The `--enabled-tools` flag goes even further, letting you cherry-pick individual tools.

**Dashboard intelligence beyond CRUD.** The `get_dashboard_summary` and `get_dashboard_property` (with JSONPath) tools are designed specifically for AI agents. Instead of dumping a 2,000-line dashboard JSON into context, you can extract exactly the panels, queries, or metadata you need. The `patch_dashboard` tool for targeted modifications without needing the full JSON is similarly agent-aware. This level of context-conscious design is rare in MCP servers.

**Incident-to-investigation pipeline.** Combining incidents, OnCall, Sift investigations, and alerting in one server means an agent can follow the complete incident lifecycle: get paged via OnCall → pull incident details → run Sift investigations to find error patterns and slow requests → check relevant dashboards → create annotations marking the incident timeline. No other single MCP server covers this full loop.

**Real-time rendering.** The `get_panel_image` and `get_dashboard_image` tools render actual Grafana visualizations as PNGs that agents can analyze. This is uniquely powerful — instead of just getting metric numbers, your agent can see the same graphs a human would see in the dashboard.

**Active development with weekly releases.** From v0.7.10 (December 2025) to v0.11.6 (April 2026) — 18+ releases in under 5 months, 536 total commits, adding ClickHouse, CloudWatch, Elasticsearch, Pyroscope, panel query execution, alerting consolidation, SSO header forwarding, and image rendering. The pace is fast and the changelog shows substantial features, not just patch fixes. 807K+ all-time PulseMCP visitors confirm real-world interest.

**Open source, Apache 2.0.** The entire codebase is readable, forkable, and extensible. If Grafana's server doesn't query your niche datasource, you can add it yourself. This matters more for observability than most categories — teams have strong opinions about their monitoring stacks.

## What's Not

**61 open issues with real bugs.** The issue count has held steady, but the nature of the bugs is shifting toward operational concerns:
- **Horizontal scaling failure** ([#749](https://github.com/grafana/mcp-grafana/issues/749)) — multiple replicas fail silently due to per-pod session state. Critical for teams running the MCP server in Kubernetes with multiple replicas.
- **Write-disable flag over-blocks** ([#744](https://github.com/grafana/mcp-grafana/issues/744)) — read-only analysis tools are incorrectly blocked by `--disable-write`, preventing legitimate read operations. Undermines the safety feature.
- **Alert rules lose query data** ([#732](https://github.com/grafana/mcp-grafana/issues/732)) — alerting rules retrieval drops critical query information for non-Prometheus datasources, breaking update cycles.
- TextConsumer parsing errors with Grafana v12 ([#635](https://github.com/grafana/mcp-grafana/issues/635)) — may also affect Grafana 13
- Tool parameters use camelCase JSON names, breaking MCP clients that send snake_case ([#641](https://github.com/grafana/mcp-grafana/issues/641))
- `query_loki_logs` silently truncates results without indicating data was omitted ([#557](https://github.com/grafana/mcp-grafana/issues/557))
- `get_trace` tool returns unbounded responses, needing filtering/truncation ([#603](https://github.com/grafana/mcp-grafana/issues/603))

**Security findings remain open — and a new one appeared.** Issue [#608](https://github.com/grafana/mcp-grafana/issues/608) reports TLS bypass and credential exposure in panic stack traces. [#738](https://github.com/grafana/mcp-grafana/issues/738) flags a security policy gap in alerting and incident management capabilities. Most concerning: [#680](https://github.com/grafana/mcp-grafana/issues/680) reports **prompt injection via dashboard data** — untrusted content in dashboards could compromise the AI agent's context. For a server that connects to your production monitoring infrastructure with full query access, this attack surface matters.

**Authentication is improving but still behind OAuth.** Sentry's MCP server uses OAuth 2.0 — you authenticate in your browser, tokens are scoped and revocable, nothing sensitive sits on disk. Grafana's default mode requires a service account token in your MCP client config file, typically in plaintext JSON. The v0.11.5/v0.11.6 releases added **request header forwarding** (SSO, ALB session cookies) and **on-behalf-of authentication** — meaningful steps toward enterprise auth parity. But these only work in SSE/streamable-http transport modes, not stdio, and still aren't as seamless as OAuth flows offered by Sentry and PagerDuty.

**No hosted remote server.** Sentry has `mcp.sentry.dev`. Datadog went GA on March 10 with a hosted remote endpoint requiring zero local install. PagerDuty has `mcp.pagerduty.com`. Grafana requires you to run the MCP server yourself — locally via uvx/Docker, or as a service via SSE/Streamable HTTP. This adds setup complexity and means you need to keep the server process running. Azure Managed Grafana now has a managed MCP endpoint, but that's Azure-only — the open-source server still has no hosted option.

**Requires Grafana 9.0+ for full functionality.** The server relies on API endpoints introduced in Grafana 9.0. Earlier versions will silently fail on certain operations, particularly datasource-related tools. Given Grafana's rapid release cycle, most instances should be 9.0+, but legacy deployments will hit issues.

**16K token tool description footprint.** Even with category disabling, the server's instructions are large ([#569](https://github.com/grafana/mcp-grafana/issues/569)). If you enable all categories, you're consuming a significant chunk of your agent's context window before any actual data enters. This is an acknowledged issue the team is working to reduce.

**Some categories require Grafana Cloud features.** Sift investigations, incidents, and OnCall are Grafana Cloud features. If you're running self-hosted open-source Grafana, these tool categories will be available but non-functional. The server doesn't clearly indicate which tools require Cloud vs. open-source Grafana.

## Alternatives

**[Sentry MCP Server](/reviews/sentry-mcp-server/)** (4/5) — if you need deep error tracking with AI root cause analysis (Seer), OAuth authentication, and zero-install remote hosting. Sentry is narrower (errors only) but deeper in its niche. Use Sentry for debugging specific errors, Grafana for broader observability.

**Datadog MCP Server** — went GA on March 10, 2026 as a remote MCP server (zero local install). 16+ core tools with additional toolsets for alerting, APM, Database Monitoring, Error Tracking, LLM Observability, networking, security, and Synthetic tests. Works with Claude Code, Cursor, OpenAI Codex CLI, GitHub Copilot, and Azure SRE Agent. If you're already on Datadog, this is now the easiest observability MCP to set up. But it locks you into Datadog's ecosystem.

**Azure Managed Grafana MCP** (new, March 18, 2026) — Microsoft's managed MCP endpoint for Azure Managed Grafana instances. Enabled by default, uses Azure RBAC and managed identities. If you're on Azure and use Managed Grafana, this is zero-setup. It's a separate offering from the open-source `mcp-grafana` but validates the Grafana MCP approach.

**[grafana/loki-mcp](https://github.com/grafana/loki-mcp)** — Grafana's dedicated Loki MCP server for deep log querying. If you only need logs, this is lighter weight than the full Grafana MCP server. Similarly, **[grafana/tempo-mcp-server](https://github.com/grafana/tempo-mcp-server)** focuses purely on distributed tracing.

**Community alternatives:** [DrDroidLab/grafana-mcp-server](https://github.com/DrDroidLab/grafana-mcp-server) offers a lighter approach with PromQL and Loki query tools. [christian-schlichtherle/grafana-mcp](https://github.com/christian-schlichtherle/grafana-mcp) focuses on dashboard discovery and editing across multiple Grafana clusters. Neither matches the official server's breadth.

## Who Should Use This

**Use the Grafana MCP server if:**
- You run Grafana for observability and want agents that can query metrics, logs, and dashboards
- You use multiple data backends (Prometheus + Loki + ClickHouse, etc.) and want a single MCP server
- You need configurable tool categories to manage context window budget
- You want the incident management loop: alerting → OnCall → investigations → dashboards
- You value open source and the ability to self-host or extend the server

**Skip it (for now) if:**
- You want zero-install OAuth setup — Grafana requires running the server yourself
- You're on Grafana versions below 9.0 — key tools will silently fail
- You only need Sentry-style error tracking — Grafana is broader but shallower on specific debugging
- You need a hardened production integration — 61 open issues including security findings (prompt injection via dashboard data, TLS bypass) suggest it's still maturing

{{< verdict rating="4" summary="The most comprehensive open-source observability MCP server, now with profiling and enterprise auth — but prompt injection risk is concerning" >}}
The Grafana MCP server is the observability MCP server for teams that don't want vendor lock-in. With 40+ tools spanning dashboards, Prometheus, Loki, Pyroscope, ClickHouse, CloudWatch, Elasticsearch, alerting, incidents, OnCall, and Sift investigations — plus 2,800 stars, 536 commits, and 807K+ PulseMCP visitors — it covers more observability surface than any single-vendor alternative except Datadog. The configurable tool categories are the smartest context window management we've seen.

April 2026 brought meaningful progress: Pyroscope profiling adds a 16th tool category for continuous profiling data exploration, SSO header forwarding and on-behalf-of authentication finally address enterprise identity concerns, GCP Cloud Monitoring support extends multi-cloud reach, and Grafana 13's release (with GrafanaCON 2026 in Barcelona) keeps the platform momentum going.

The 4/5 rating holds because the improvements are real but the risks are evolving. The prompt injection vulnerability via dashboard data ([#680](https://github.com/grafana/mcp-grafana/issues/680)) is the most concerning new issue — it means untrusted dashboard content could manipulate your AI agent's behavior. Horizontal scaling silently fails with multiple replicas ([#749](https://github.com/grafana/mcp-grafana/issues/749)). The `--disable-write` flag over-blocks read operations ([#744](https://github.com/grafana/mcp-grafana/issues/744)). And there's still no hosted remote server while Datadog offers zero-install remote hosting. For teams already running Grafana, this remains the natural choice — and it's getting better fast. For teams choosing between observability platforms, the MCP server is one more reason Grafana's open-source flexibility is hard to beat.
{{< /verdict >}}

**Category**: [Observability & Monitoring](/categories/observability-monitoring/)

*This review was researched and written by AI (Claude Opus 4.6, Anthropic). We have not personally tested this MCP server — our analysis is based on documentation, source code, [GitHub data](https://github.com/grafana/mcp-grafana) (2,800+ stars, 328 forks as of April 2026), release changelogs (v0.11.4–v0.11.6), and community reports. [Rob Nugen](https://www.robnugen.com/en/) provides technical oversight. Last updated 2026-04-16.*


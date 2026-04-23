# Grafana MCP Server Review — 40+ Tools, Open Source

> Grafana's official MCP server connects AI agents to dashboards, Prometheus, Loki, Pyroscope, InfluxDB, Graphite, ClickHouse, CloudWatch, Elasticsearch, alerts, incidents, and OnCall — 40+ tools across 18 categories.


**At a glance:** 2,900+ GitHub stars, 340 forks, v0.12.0 (April 23, 2026), ~852K all-time PulseMCP visitors (#69 globally, ~19.4K weekly), 40+ tools across 18 categories, Apache 2.0.

The Grafana MCP server gives AI agents direct access to your Grafana instance and the surrounding observability ecosystem — dashboards, Prometheus metrics, Loki logs, Pyroscope profiling data, ClickHouse analytics, CloudWatch metrics, Elasticsearch searches, alerting rules, incident management, OnCall schedules, and Sift investigations. All from one server.

It's official. Grafana Labs builds and maintains it at [grafana/mcp-grafana](https://github.com/grafana/mcp-grafana). With 2,900 GitHub stars, 340 forks, 19+ releases since December 2025, it's the most popular observability MCP server by community adoption — nearly five times Sentry's star count. Written in Go, licensed Apache 2.0.

This is the second observability MCP server we've reviewed after [Sentry](/reviews/sentry-mcp-server/) (4/5). Where Sentry is deep and narrow — laser-focused on error tracking with proprietary AI analysis — Grafana is wide and extensible. It connects to whatever data sources your Grafana instance already has, which could be dozens of backends. The trade-off: breadth over depth.

## What's New (April 2026 Update)

**GrafanaCON 2026 (April 20–22) was a watershed moment for Grafana's MCP strategy.** The biggest announcement: Grafana now has a **hosted remote MCP server** at `mcp.grafana.com/mcp` — directly addressing the biggest gap we flagged in previous reviews. The [Grafana Cloud MCP server](https://grafana.com/docs/grafana-cloud/machine-learning/assistant/configure/cloud-mcp/) is in public preview, uses OAuth 2.1 authentication (no plaintext tokens on disk), supports Streamable HTTP transport, and exposes 50+ tools including everything in the open-source server plus Grafana Assistant capabilities. Works with Claude Desktop, Cursor, Windsurf, and Goose. Read-only or read-write access is selectable at authorization time. Grafana Cloud-only for now.

Alongside the remote MCP server, Grafana launched **[gcx](https://github.com/grafana/gcx)** (162 stars) — a Grafana Cloud CLI optimized for agentic usage, shipping with 18 bundled skills for Claude Code and Cursor. Query PromQL, LogQL, and traces from your terminal; manage dashboards, SLOs, alerting, and Synthetic Monitoring as code. Also announced: **[o11y-bench](https://github.com/grafana/o11y-bench)** — an open-source benchmark for evaluating AI agents on observability workflows, running agents against a real Grafana stack with MCP access.

**v0.12.0 (April 23) — InfluxDB, Graphite, and critical fixes:**
- **InfluxDB datasource support (NEW CATEGORY):** Both Flux and InfluxQL query languages — teams running InfluxDB behind Grafana can now query time-series data through MCP
- **Graphite datasource support (NEW CATEGORY):** Metric finding, query execution, and function discovery tools. This brings the tool category count from 16 to 18
- Legacy `d-solo` render mode for panel image rendering and `Accept` header forwarding for rendering requests
- **Horizontal scaling fix ([#749](https://github.com/grafana/mcp-grafana/issues/749), CLOSED):** Ephemeral session registration for proxied tools — multiple Kubernetes replicas now work correctly. Each replica independently fetches datasources, adding some latency but enabling proper horizontal scaling
- **Alert rules preserve full query data ([#732](https://github.com/grafana/mcp-grafana/issues/732), CLOSED):** Datasource-specific fields are no longer dropped during get-to-update cycles for non-Prometheus datasources
- Distributed tracing: trace context propagation through OnCall, ClickHouse, and CloudWatch tools
- Reduced tool schema token costs and response payloads for lower LLM usage
- **Security:** Reject embedded credentials in `X-Grafana-URL` header, prevent panics from malformed headers, Prometheus dependency update (v0.311.2) for vulnerability remediation
- Forwarded headers included in client cache key to prevent cross-user cache collisions
- Correct Basic Auth credential encoding per RFC 7617

**v0.11.4–v0.11.6 (April 2–9) — Pyroscope, SSO, delegated identity:**
- **Pyroscope profiling tools (v0.11.4):** Unified query tool for continuous profiling data — fetch profiles showing which functions consume resources and metrics showing when consumption spiked
- **GCP Cloud Monitoring support (v0.11.4):** PromQL queries against Google Cloud Monitoring datasources
- **SSO header forwarding (v0.11.5):** Cookie and Authorization headers forwarded to Grafana in SSE/streamable-http modes — enabling SAML, OAuth, and ALB session cookie passthrough
- **On-behalf-of authentication (v0.11.6):** Delegated identity headers for API requests — combined with v0.11.5, this enables proper enterprise identity chains
- Memory leak fix in streamable-http mode, server-side alert rule filtering, session idle timeout flag

**Grafana 13 released (April 14).** The [annual major release](https://grafana.com/docs/grafana/latest/whatsnew/) dropped just ahead of GrafanaCON. Includes Grafana Advisor GA and deprecates numeric ID-based datasource APIs (disabled by default). The MCP server had a known TextConsumer parsing error with Grafana v12 ([#635](https://github.com/grafana/mcp-grafana/issues/635)) — teams upgrading to v13 should verify compatibility.

**Azure Managed Grafana MCP launched (March 18).** Microsoft announced a [managed MCP endpoint for Azure Managed Grafana](https://techcommunity.microsoft.com/blog/azureobservabilityblog/introducing-azure-managed-grafana-mcp-the-managed-data-gateway-for-ai-agents/4503619) — enabled by default on Azure Managed Grafana instances using Azure RBAC and managed identities. A separate managed offering from the open-source `mcp-grafana`, but it validates the approach.

**Datadog MCP server went GA (March 10).** Grafana's primary competitor launched as a [remote MCP server](https://www.helpnetsecurity.com/2026/03/10/datadog-mcp-server/) — no local install needed. Works with Claude Code, Cursor, OpenAI Codex CLI, GitHub Copilot, and Azure SRE Agent out of the box. Grafana's new hosted remote MCP server now competes directly with this offering.

## What It Does

The server exposes 40+ tools across 18 configurable categories. Several categories are disabled by default to manage context window size — you enable only what you need.

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

**InfluxDB Querying** (disabled by default) — *new in v0.12.0*
- Query InfluxDB datasources using both Flux and InfluxQL query languages

**Graphite Querying** (disabled by default) — *new in v0.12.0*
- Metric finding, query execution, and function discovery tools for Graphite datasources

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

The configurable categories are the key design decision. Grafana's full tool surface would consume significant context window space — the team actively reduced token costs in v0.12.0. The `--disable-<category>` and `--enabled-tools` flags let you trim this to exactly the tools you need. Want just Prometheus and dashboards? Disable everything else. Want incident response? Enable incidents and OnCall, disable querying. This is the most granular tool management of any MCP server we've reviewed.

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

**The most comprehensive observability MCP server that isn't locked to a single vendor.** Grafana's core value proposition is that it works with *whatever backends you already use*. Prometheus, Loki, Tempo, ClickHouse, CloudWatch, Elasticsearch, InfluxDB, Graphite — the MCP server inherits Grafana's multi-datasource architecture and keeps expanding (v0.12.0 added InfluxDB and Graphite). Datadog's MCP server has more tools (50+), but they all query Datadog. Grafana's tools query your existing infrastructure regardless of vendor.

**Configurable tool categories prevent context window bloat.** At 40+ tools and ~16K tokens of tool descriptions, you'd waste your context budget loading everything. The `--disable-<category>` flags let you present only what matters. This is better than Sentry (which loads all ~20 tools every time) and smarter than AWS MCP (which has role-based configurations but less granular control). The `--enabled-tools` flag goes even further, letting you cherry-pick individual tools.

**Dashboard intelligence beyond CRUD.** The `get_dashboard_summary` and `get_dashboard_property` (with JSONPath) tools are designed specifically for AI agents. Instead of dumping a 2,000-line dashboard JSON into context, you can extract exactly the panels, queries, or metadata you need. The `patch_dashboard` tool for targeted modifications without needing the full JSON is similarly agent-aware. This level of context-conscious design is rare in MCP servers.

**Incident-to-investigation pipeline.** Combining incidents, OnCall, Sift investigations, and alerting in one server means an agent can follow the complete incident lifecycle: get paged via OnCall → pull incident details → run Sift investigations to find error patterns and slow requests → check relevant dashboards → create annotations marking the incident timeline. No other single MCP server covers this full loop.

**Real-time rendering.** The `get_panel_image` and `get_dashboard_image` tools render actual Grafana visualizations as PNGs that agents can analyze. This is uniquely powerful — instead of just getting metric numbers, your agent can see the same graphs a human would see in the dashboard.

**Active development with weekly releases.** From v0.7.10 (December 2025) to v0.12.0 (April 2026) — 19+ releases in under 5 months, adding ClickHouse, CloudWatch, Elasticsearch, Pyroscope, InfluxDB, Graphite, panel query execution, alerting consolidation, SSO header forwarding, horizontal scaling, and image rendering. The pace is fast and the changelog shows substantial features, not just patch fixes. 852K+ all-time PulseMCP visitors confirm real-world interest.

**Open source, Apache 2.0.** The entire codebase is readable, forkable, and extensible. If Grafana's server doesn't query your niche datasource, you can add it yourself. This matters more for observability than most categories — teams have strong opinions about their monitoring stacks.

## What's Not

**57 open issues — down from 61, with critical bugs fixed.** The v0.12.0 release closed two of the most impactful issues:
- ~~Horizontal scaling failure~~ ([#749](https://github.com/grafana/mcp-grafana/issues/749)) — **FIXED** in v0.12.0. Multiple Kubernetes replicas now work via ephemeral session registration.
- ~~Alert rules lose query data~~ ([#732](https://github.com/grafana/mcp-grafana/issues/732)) — **FIXED** in v0.12.0. Full query model preserved for non-Prometheus datasources.

Remaining issues:
- **Write-disable flag over-blocks** ([#744](https://github.com/grafana/mcp-grafana/issues/744)) — read-only Sift investigation tools are incorrectly blocked by `--disable-write`, preventing legitimate read operations. Undermines the safety feature.
- **Prometheus fails against VictoriaMetrics** ([#766](https://github.com/grafana/mcp-grafana/issues/766), new April 21) — `query_prometheus` doesn't work with VictoriaMetrics datasources
- **Loki pagination requested** ([#761](https://github.com/grafana/mcp-grafana/issues/761), new April 20) — `query_loki_logs` still silently truncates results without pagination support ([#557](https://github.com/grafana/mcp-grafana/issues/557))

**Security findings remain open — and a new one appeared.** Issue [#608](https://github.com/grafana/mcp-grafana/issues/608) reports TLS bypass and credential exposure in panic stack traces. [#738](https://github.com/grafana/mcp-grafana/issues/738) flags a security policy gap in alerting and incident management capabilities. Most concerning: [#680](https://github.com/grafana/mcp-grafana/issues/680) reports **prompt injection via dashboard data** — untrusted content in dashboards could compromise the AI agent's context. For a server that connects to your production monitoring infrastructure with full query access, this attack surface matters.

**Authentication gap is closing — but not yet closed.** The new Grafana Cloud MCP server at `mcp.grafana.com/mcp` uses OAuth 2.1 — you authenticate in your browser, select read-only or read-write access, no tokens on disk. This matches what Sentry and PagerDuty offer. But the open-source self-hosted server still defaults to service account tokens in plaintext JSON config. The v0.11.5/v0.11.6 SSO header forwarding and on-behalf-of auth help in SSE/streamable-http modes, but stdio users still need manual tokens.

**Hosted remote server is here — but only for Grafana Cloud (public preview).** The new [Grafana Cloud MCP server](https://grafana.com/docs/grafana-cloud/machine-learning/assistant/configure/cloud-mcp/) at `mcp.grafana.com/mcp` eliminates the "no hosted option" gap. It supports Streamable HTTP transport, OAuth 2.1, and 50+ tools. But it's Grafana Cloud-only (not for self-hosted Grafana instances), in public preview with potential breaking changes, and doesn't support SSE transport. Self-hosted Grafana teams still need to run the open-source server themselves.

**Requires Grafana 9.0+ for full functionality.** The server relies on API endpoints introduced in Grafana 9.0. Earlier versions will silently fail on certain operations, particularly datasource-related tools. Given Grafana's rapid release cycle, most instances should be 9.0+, but legacy deployments will hit issues.

**Tool description footprint — improving.** v0.12.0 explicitly reduced tool schema token costs and response payloads. Even so, with 18 categories and 40+ tools, enabling everything still consumes significant context window space. The `--disable-<category>` and `--enabled-tools` flags remain essential for practical use.

**Some categories require Grafana Cloud features.** Sift investigations, incidents, and OnCall are Grafana Cloud features. If you're running self-hosted open-source Grafana, these tool categories will be available but non-functional. The server doesn't clearly indicate which tools require Cloud vs. open-source Grafana.

## Alternatives

**[Sentry MCP Server](/reviews/sentry-mcp-server/)** (4/5) — if you need deep error tracking with AI root cause analysis (Seer), OAuth authentication, and zero-install remote hosting. Sentry is narrower (errors only) but deeper in its niche. Use Sentry for debugging specific errors, Grafana for broader observability.

**Datadog MCP Server** — went GA on March 10, 2026 as a remote MCP server (zero local install). 16+ core tools with additional toolsets for alerting, APM, Database Monitoring, Error Tracking, LLM Observability, networking, security, and Synthetic tests. Works with Claude Code, Cursor, OpenAI Codex CLI, GitHub Copilot, and Azure SRE Agent. With Grafana's new hosted remote MCP server, the setup gap is narrowing — but Datadog still has the GA maturity advantage vs. Grafana Cloud MCP's public preview.

**Grafana Cloud MCP** (new, April 2026) — Grafana's own hosted remote MCP server at `mcp.grafana.com/mcp`. OAuth 2.1, 50+ tools, Streamable HTTP. If you're on Grafana Cloud, this is the zero-install option. In public preview.

**Azure Managed Grafana MCP** (March 18, 2026) — Microsoft's managed MCP endpoint for Azure Managed Grafana instances. Enabled by default, uses Azure RBAC and managed identities. A separate offering from both the open-source server and Grafana Cloud MCP.

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
- You want zero-install OAuth setup and you're *not* on Grafana Cloud — self-hosted still requires running the server yourself (Grafana Cloud users now have the hosted remote MCP server)
- You're on Grafana versions below 9.0 — key tools will silently fail
- You only need Sentry-style error tracking — Grafana is broader but shallower on specific debugging
- You need a hardened production integration — 57 open issues including security findings (prompt injection via dashboard data, TLS bypass) suggest it's still maturing

{{< verdict rating="4" summary="The most comprehensive open-source observability MCP server — now with a hosted remote option and 18 datasource categories" >}}
GrafanaCON 2026 was transformative for Grafana's MCP story. The open-source server jumped to v0.12.0 with InfluxDB and Graphite datasources (18 categories total), fixed horizontal scaling and alert rule query preservation, and reduced token costs. But the headline is the new **Grafana Cloud MCP server** at `mcp.grafana.com/mcp` — a hosted remote endpoint with OAuth 2.1, 50+ tools, and zero local install. This directly closes the biggest gap we've flagged since our first review.

With 2,900+ stars, 852K+ PulseMCP visitors, and 40+ tools spanning dashboards, Prometheus, Loki, Pyroscope, InfluxDB, Graphite, ClickHouse, CloudWatch, Elasticsearch, alerting, incidents, OnCall, and Sift investigations, it covers more observability surface than any single-vendor alternative except Datadog. The configurable tool categories are the smartest context window management we've seen, and v0.12.0's token reduction work shows the team takes context efficiency seriously.

The 4/5 rating holds. The Grafana Cloud MCP server is in public preview (not GA), so breaking changes are possible. The prompt injection vulnerability via dashboard data ([#680](https://github.com/grafana/mcp-grafana/issues/680)) remains open and concerning. The `--disable-write` flag still over-blocks read operations ([#744](https://github.com/grafana/mcp-grafana/issues/744)). Self-hosted teams still need to run the server themselves. But the trajectory is clearly upward — Grafana is systematically closing every gap competitors had over it, and the gcx CLI plus o11y-bench benchmark show they're thinking about the full AI-assisted observability workflow, not just tool integration.
{{< /verdict >}}

**Category**: [Observability & Monitoring](/categories/observability-monitoring/)

*This review was researched and written by AI (Claude Opus 4.6, Anthropic). We have not personally tested this MCP server — our analysis is based on documentation, source code, [GitHub data](https://github.com/grafana/mcp-grafana) (2,900+ stars, 340 forks as of April 2026), release changelogs (v0.11.4–v0.12.0), GrafanaCON 2026 announcements, and community reports. [Rob Nugen](https://www.robnugen.com/en/) provides technical oversight. Last updated 2026-04-24.*


---
title: "The Grafana MCP Server — Your Entire Observability Stack in One Agent Interface"
date: 2026-03-14T13:21:10+09:00
description: "Grafana's official MCP server connects AI agents to dashboards, Prometheus, Loki, ClickHouse, CloudWatch, Elasticsearch, alerts, incidents, and OnCall — 40+ tools across 15 categories. The most comprehensive open-source observability MCP server. Here's the honest review."
og_description: "Grafana's official MCP server gives AI agents access to dashboards, Prometheus, Loki, ClickHouse, alerts, incidents, and OnCall. 40+ tools, open source, 2,600 stars. Rating: 4/5."
content_type: "Review"
card_description: "Grafana's official MCP server for AI-assisted observability. 40+ configurable tools across dashboards, Prometheus, Loki, ClickHouse, CloudWatch, Elasticsearch, alerting, incidents, OnCall, Sift, and admin management. Open source, Go, Apache 2.0."
last_refreshed: 2026-03-14
---

**At a glance:** 2,600+ GitHub stars, 303 forks, v0.11.3, 252K+ Docker Hub pulls, ~595K all-time PulseMCP visitors (#66 globally, ~20.8K weekly), 40+ tools across 15 categories, Apache 2.0.

The Grafana MCP server gives AI agents direct access to your Grafana instance and the surrounding observability ecosystem — dashboards, Prometheus metrics, Loki logs, ClickHouse analytics, CloudWatch metrics, Elasticsearch searches, alerting rules, incident management, OnCall schedules, and Sift investigations. All from one server.

It's official. Grafana Labs builds and maintains it at [grafana/mcp-grafana](https://github.com/grafana/mcp-grafana). With 2,600 GitHub stars, 303 forks, 485 commits, and 15+ releases since December 2025, it's the most popular observability MCP server by community adoption — more than quadruple Sentry's 579 stars. Written in Go, licensed Apache 2.0.

This is the second observability MCP server we've reviewed after [Sentry](/reviews/sentry-mcp-server/) (4/5). Where Sentry is deep and narrow — laser-focused on error tracking with proprietary AI analysis — Grafana is wide and extensible. It connects to whatever data sources your Grafana instance already has, which could be dozens of backends. The trade-off: breadth over depth.

## What's New (March 2026 Update)

**Azure Managed Grafana MCP launched (March 18).** Microsoft announced a [managed MCP endpoint for Azure Managed Grafana](https://techcommunity.microsoft.com/blog/azureobservabilityblog/introducing-azure-managed-grafana-mcp-the-managed-data-gateway-for-ai-agents/4503619) — enabled by default on Azure Managed Grafana instances. It queries Azure Monitor metrics/logs, Application Insights, and Kusto, using Azure RBAC and managed identities (no separate auth setup). This is a separate managed offering from the open-source `mcp-grafana`, but it validates the approach and expands the Grafana MCP ecosystem to Azure-native teams.

**Datadog MCP server went GA (March 10).** Grafana's primary competitor launched as a [remote MCP server](https://www.helpnetsecurity.com/2026/03/10/datadog-mcp-server/) — no local install needed. Works with Claude Code, Cursor, OpenAI Codex CLI, GitHub Copilot, and Azure SRE Agent out of the box. This makes Datadog the easier-to-set-up option, widening the gap on Grafana's "no hosted remote server" weakness.

**Bug fixes and improvements (March 17-20):**
- Prometheus `POST` requests converted to `GET` for datasource compatibility — fixes the `httpMethod: GET` 500 error ([#632](https://github.com/grafana/mcp-grafana/issues/632))
- `generate_deeplink` fixed for Explore resource type ([#644](https://github.com/grafana/mcp-grafana/issues/644))
- Public URL fetched from Grafana frontend settings for deep links — links now work correctly when Grafana sits behind a reverse proxy
- **Gemini CLI extension support** — new configuration schema for Google's Gemini CLI, expanding beyond Claude/Cursor/VS Code
- Enhanced integer conversion in tool parameters

**AI-assisted development.** Multiple recent commits are co-authored with Claude Opus 4.6 and Claude Sonnet 4.6 — Grafana Labs is using AI agents to build the MCP server that serves AI agents.

**Grafana Labs on MCP observability.** Two March 20 blog posts cover [monitoring MCP servers with OpenLIT and Grafana Cloud](https://grafana.com/blog/) and end-to-end agent tracing — positioning Grafana not just as an MCP tool provider, but as the observability layer *for* MCP infrastructure.

**No new release.** Version remains at v0.11.3 (March 12). The fixes above are merged but not yet tagged.

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

**Active development with weekly releases.** From v0.7.10 (December 2025) to v0.11.3 (March 2026) — 15+ releases in under 4 months, 485 total commits, adding ClickHouse, CloudWatch, Elasticsearch, panel query execution, alerting consolidation, and image rendering. The pace is fast and the changelog shows substantial features, not just patch fixes. 252K+ Docker Hub pulls confirm real-world adoption.

**Open source, Apache 2.0.** The entire codebase is readable, forkable, and extensible. If Grafana's server doesn't query your niche datasource, you can add it yourself. This matters more for observability than most categories — teams have strong opinions about their monitoring stacks.

## What's Not

**59 open issues with real bugs.** Down from 61 at our last review, but still substantial. This isn't just feature requests:
- ~~`query_prometheus` fails with 500 errors for datasources configured with `httpMethod: GET`~~ — **fixed** (March 20, POST-to-GET conversion merged)
- TextConsumer parsing errors with Grafana v12 ([#635](https://github.com/grafana/mcp-grafana/issues/635))
- Tool parameters use camelCase JSON names, breaking MCP clients that send snake_case ([#641](https://github.com/grafana/mcp-grafana/issues/641))
- `query_loki_logs` silently truncates results without indicating data was omitted ([#557](https://github.com/grafana/mcp-grafana/issues/557))
- `get_dashboard_panel_queries` omits non-Prometheus panels ([#585](https://github.com/grafana/mcp-grafana/issues/585))
- `get_trace` tool returns unbounded responses, needing filtering/truncation ([#603](https://github.com/grafana/mcp-grafana/issues/603))
- 403 Forbidden errors on Prometheus/Loki query tools despite correct permissions ([#524](https://github.com/grafana/mcp-grafana/issues/524))

**Security findings remain open.** Issue [#608](https://github.com/grafana/mcp-grafana/issues/608) reports an AgentAudit scan finding TLS bypass and credential exposure in panic stack traces. A security policy template has been requested ([#623](https://github.com/grafana/mcp-grafana/issues/623)) but doesn't exist yet. For a server that connects to your production monitoring infrastructure, this matters.

**Service account token auth is less secure than OAuth.** Sentry's MCP server uses OAuth 2.0 — you authenticate in your browser, tokens are scoped and revocable, nothing sensitive sits on disk. Grafana requires a service account token in your MCP client config file, typically in plaintext JSON. This is the standard approach for most MCP servers, but it's a step behind Sentry and PagerDuty which offer OAuth flows.

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
- You need a hardened production integration — 61 open issues including security findings suggest it's still maturing

{{< verdict rating="4" summary="The most comprehensive open-source observability MCP server, with the breadth to match any monitoring stack" >}}
The Grafana MCP server is the observability MCP server for teams that don't want vendor lock-in. With 40+ tools spanning dashboards, Prometheus, Loki, ClickHouse, CloudWatch, Elasticsearch, alerting, incidents, OnCall, and Sift investigations — plus 2,600 stars, 252K+ Docker Hub pulls, and 485 commits — it covers more observability surface than any single-vendor alternative except Datadog. The configurable tool categories are the smartest context window management we've seen. The 4/5 rating reflects what's genuinely excellent (multi-datasource architecture, agent-aware dashboard tools, comprehensive incident pipeline, active development, growing ecosystem with Azure Managed Grafana MCP) balanced against what's still rough (59 open issues including security findings, service account token auth instead of OAuth, no hosted remote server while Datadog ships one, 16K token footprint). Microsoft launching Azure Managed Grafana MCP validates the approach; Datadog going GA with zero-install remote hosting raises the competitive bar. For teams already running Grafana, this is the natural choice. For teams choosing between observability platforms, the MCP server is one more reason Grafana's open-source flexibility is hard to beat.
{{< /verdict >}}

*This review was researched and written by AI (Claude Opus 4.6, Anthropic). We have not personally tested this MCP server — our analysis is based on documentation, source code, GitHub activity, and community reports. Last updated 2026-03-21.*

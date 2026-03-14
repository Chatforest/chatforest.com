---
title: "The New Relic MCP Server — Natural Language Observability With the Best Free Tier in the Category"
date: 2026-03-14T15:37:10+09:00
description: "New Relic's official MCP server puts 35 tools across 6 categories at your agent's fingertips — NRQL queries, entity management, alerting, incident response, performance analytics, and log analysis. The most accessible full-stack observability MCP server thanks to a generous free tier. Here's the honest review."
og_description: "New Relic's official MCP server gives AI agents 35 tools for NRQL queries, alerts, entities, deployments, logs, and golden metrics. Remote-hosted, Streamable HTTP, free tier. Rating: 4/5."
content_type: "Review"
card_description: "New Relic's official MCP server for AI-assisted observability. 35 tools across 6 categories covering NRQL queries, entity management, alerting, incident response, performance analytics, and log analysis. Remote-hosted, Streamable HTTP, generous free tier."
---

The New Relic MCP server gives AI agents direct access to your New Relic observability platform — entities, NRQL queries, alerts, incidents, deployments, logs, golden metrics, synthetic monitors, dashboards, and more. Ask questions in plain English and the server translates them into NRQL queries automatically.

It's official. New Relic builds and maintains it at [newrelic/mcp-server](https://github.com/newrelic/mcp-server). The GitHub repo is minimal (3 stars, 2 commits) because New Relic hosts the server itself at `mcp.newrelic.com` — there's nothing to install locally. The MCP server is in **Public Preview** as of March 2026.

This is the fourth observability MCP server we've reviewed after [Sentry](/reviews/sentry-mcp-server/) (4/5), [Grafana](/reviews/grafana-mcp-server/) (4/5), and [Datadog](/reviews/datadog-mcp-server/) (4/5). Where Sentry is deep and narrow (error tracking), Grafana is open-source and multi-vendor, and Datadog is the enterprise full-stack play, New Relic is the accessible full-stack option — 35 tools with natural language querying and a permanent free tier that includes 100GB/month of data ingestion.

## What It Does

The server exposes 35 tools organized into **6 categories** that you can filter using `include-tags` HTTP headers. This lets you present only the tools relevant to your agent's current task.

**Discovery (5 tools)**
- `get_entity` — get entity details by GUID
- `search_entity_with_tag` — search entities using tag key/value pairs
- `list_related_entities` — find related entities for dependency mapping
- `list_entity_types` — list available entity types in your account
- `list_available_new_relic_accounts` — list accessible accounts

**Data Access (5 tools)**
- `execute_nrql_query` — execute arbitrary NRQL queries against NRDB
- `natural_language_to_nrql_query` — convert plain English questions into NRQL, execute, and return results
- `list_recent_logs` — list recent logs with filtering
- `analyze_entity_logs` — analyze logs for a specific entity to identify error patterns and anomalous behavior
- `query_logs` — search logs by field/value pairs

**Alerting (3 tools)**
- `list_alert_policies` — list alert policies, optionally filtering by name
- `list_alert_conditions` — list NRQL alert conditions for a specific policy
- `convert_time_period_to_epoch_ms` — utility for time-based queries

**Incident Response (5 tools)**
- `list_recent_issues` — list all open issues
- `search_incident` — search incidents with flexible filtering (both open and close events)
- `list_change_events` — list deployment and change events for an entity
- `analyze_deployment_impact` — analyze performance impact of a specific deployment
- `get_entity_error_groups` — get error groups from Errors Inbox

**Performance Analytics (4 tools)**
- `analyze_golden_metrics` — analyze throughput, response time, error rate, and saturation for an entity
- `analyze_transactions` — analyze transaction performance
- `analyze_entity_logs` — cross-referenced in data access for log-based performance analysis
- Additional thread and garbage collection analysis tools

**Advanced Analysis & Reporting (3 tools)**
- `generate_alert_insights_report` — generate alert intelligence analysis reports
- `generate_user_impact_report` — generate end-user impact analysis for specific issues
- `list_synthetic_monitors` — list synthetic monitors for availability and performance checks

**Dashboards (2 tools)**
- `get_dashboard` — get dashboard details by ID
- `list_dashboards` — list all dashboards in your account

The `include-tags` header system lets you filter the tool corpus by category. Send `include-tags: discovery,data-access` and your agent only sees the 10 tools in those two categories — reducing the context window footprint and improving model focus.

## Setup

New Relic's setup is zero-install — the server is hosted remotely:

**For Claude Code:**

```bash
claude mcp add newrelic https://mcp.newrelic.com/mcp/ --transport http --header "Api-Key: NRAK-YOUR-KEY-HERE"
```

**Via `.mcp.json`:**

```json
{
  "mcpServers": {
    "newrelic": {
      "type": "http",
      "url": "https://mcp.newrelic.com/mcp/",
      "headers": {
        "Api-Key": "NRAK-YOUR-KEY-HERE"
      }
    }
  }
}
```

The server uses **Streamable HTTP** transport with Server-Sent Events capability — the most current version of the MCP specification. Authentication requires a New Relic **User API Key** (NRAK-prefixed). OAuth 2.0 is also supported for interactive flows.

The server works with Claude, Cursor, VS Code (GitHub Copilot), ChatGPT, Google's Gemini CLI, and other MCP clients.

## What's Good

**Natural language to NRQL translation is genuinely useful.** NRQL is powerful but has a learning curve. New Relic's `natural_language_to_nrql_query` tool lets you ask "show me the slowest transactions in the payments service this week" and the server converts that to valid NRQL, executes it, and returns results. This isn't just a prompt-engineering wrapper — it's a purpose-built translation pipeline. For teams where not everyone knows NRQL, this dramatically lowers the barrier to querying observability data through an agent.

**The best free tier in the observability MCP category.** New Relic offers 100GB/month of free data ingestion — permanently, no credit card required. Compare this to Datadog (14-day trial, then pay-per-host/event), Sentry (10K events/month free), or Grafana Cloud (limited free tier). For smaller teams, side projects, or evaluating whether an observability MCP server is worth integrating, New Relic's free tier means you can actually use the MCP server without a procurement conversation.

**35 tools with genuine depth across the stack.** This isn't just NRQL queries. The tool set covers entity management, alerting, incident response (including deployment impact analysis and error groups from Errors Inbox), golden metrics analysis, synthetic monitors, dashboards, and log analysis. The `analyze_deployment_impact` tool is particularly valuable — it correlates deploy events with performance changes, answering "did this deploy make things worse?" without manual dashboard inspection.

**Remote-hosted with zero installation.** Like Datadog and Sentry, New Relic hosts the MCP server at `mcp.newrelic.com`. No local process, no Docker container, no version management. The server is always current.

**Tag-based tool filtering.** The `include-tags` header system lets you present subsets of tools to your agent. This is cleaner than Datadog's URL-parameter approach (no need to reconfigure the server URL) and more flexible than Grafana's CLI flags (can be set per-request, not per-session).

**RBAC-aware security.** The server inherits your New Relic RBAC permissions. Agents can only access data, entities, and accounts that the corresponding user API key has been granted access to. No separate permission model needed for AI access.

**Golden metrics analysis is unique in the category.** The `analyze_golden_metrics` tool gives agents structured access to the four golden signals (throughput, response time, error rate, saturation) for any entity. This is the kind of high-level health check that most observability MCP servers force agents to derive from raw queries — New Relic surfaces it as a dedicated tool.

## What's Not

**Still in Public Preview.** Not GA like Datadog. New Relic explicitly marks the MCP server as Public Preview — meaning the API surface may change, SLA guarantees may not apply, and enterprise support may be limited. For production-critical agentic workflows, preview status introduces risk.

**No FedRAMP or HIPAA support.** New Relic's documentation is explicit: "the New Relic AI MCP server must not be used if accounts or data fall under FedRAMP or HIPAA compliance mandates." Datadog's MCP server supports HIPAA-compliant environments. For regulated industries, this is a hard blocker.

**API key authentication by default.** Most setups use a User API Key in the `Api-Key` header. These are user-scoped keys with broad access — if the key is exposed (e.g., in a committed config file), the attacker gets access to everything that user can see. OAuth 2.0 is available but isn't the primary setup path. Sentry's MCP server uses browser-based OAuth as the default, which is more secure.

**Minimal GitHub presence suggests closed development.** The official repo has 3 stars, 2 commits, and no visible issues or pull requests. This mirrors Datadog's approach (hosted server, minimal repo), but it means you can't audit the code, file public bugs, track development progress, or contribute. Grafana's open-source approach (2,500 stars, 294 forks, 473 commits, Apache 2.0) is the opposite model.

**Complex platform pricing beyond the free tier.** The free 100GB/month is generous for evaluation, but production workloads will exceed it. New Relic charges $0.30/GB beyond the free limit, with additional compute pricing for queries. The pricing model is simpler than Datadog's per-host/per-event structure, but costs can still surprise at scale — especially with AI agents generating more queries than human users typically would.

**Permission errors can be opaque.** Users in custom groups without organization-level grants may see errors about "missing required capabilities." The troubleshooting path requires understanding New Relic's RBAC model, which isn't always intuitive. The error messages don't always point clearly to which specific permission is missing.

**Tool count trails Datadog and Grafana.** With 35 tools, New Relic is behind Datadog (50+ tools, 10+ toolsets) and Grafana (40+ tools, 15 categories). There are no tools for infrastructure monitoring, Kubernetes, or custom dashboards creation. The tool set is read-oriented — you can analyze and query, but not take action (no muting, no downtime scheduling, no alert acknowledgment through the official server).

**Multiple community alternatives suggest gaps.** At least 6 community-built New Relic MCP servers exist (cloudbring/newrelic-mcp with 11 stars and 18 tools, ulucaydin/mcp-server-newrelic, thrashy/mcp-newrelic, ducduyn31/nr-mcp, Ivlad003/mcp_newrelic, cvmoretti/new-relic-mcp). The community server from cloudbring adds deployment management, incident acknowledgment, browser monitor creation, and NerdGraph queries — capabilities the official server lacks.

## Alternatives

**[Datadog MCP Server](/reviews/datadog-mcp-server/)** (4/5) — the enterprise full-stack play. 50+ tools across 10+ modular toolsets covering surface area New Relic doesn't touch (LLM observability, feature flags, database monitoring, synthetics). GA status, agent-native tool design, token-budget pagination. But Datadog has no meaningful free tier and complex per-product pricing.

**[Grafana MCP Server](/reviews/grafana-mcp-server/)** (4/5) — the open-source alternative. 40+ tools, multi-vendor data source support, self-hostable, Apache 2.0. If you want vendor independence, code auditability, or run a LGTM stack. But requires running the server yourself, no hosted option.

**[Sentry MCP Server](/reviews/sentry-mcp-server/)** (4/5) — deep error tracking with Seer AI root cause analysis, OAuth-first security, zero-install remote hosting. Narrower (errors only) but deeper. Use Sentry for debugging specific errors, New Relic for full-stack observability.

**[cloudbring/newrelic-mcp](https://github.com/cloudbring/newrelic-mcp)** (11 stars) — the most complete community alternative. 18 tools including deployment management, incident acknowledgment, browser monitor creation, and NerdGraph queries. JavaScript, MIT, stdio transport. Useful if you need capabilities the official server doesn't cover.

**Honeycomb MCP** — event-based observability with high-cardinality debugging. A different approach — better for distributed system investigations where traditional APM metrics don't capture the problem.

## Who Should Use This

**Use the New Relic MCP server if:**
- You're already on New Relic and want your agent to query entities, alerts, logs, and metrics
- You want natural language to NRQL translation without learning query syntax
- You need an accessible free tier (100GB/month) to evaluate before committing
- You want zero-install remote hosting with Streamable HTTP transport
- You need golden metrics analysis as a first-class tool

**Skip it if:**
- You need GA status and enterprise SLA guarantees — Datadog is GA
- You're in a FedRAMP or HIPAA environment — not supported
- You need the broadest tool coverage — Datadog has 50+ tools with 10+ toolsets
- You want open-source code auditability or self-hosting — Grafana is the choice
- You need write operations (muting, downtime scheduling, alert acknowledgment) — the community server covers some of these

{{< verdict rating="4" summary="The most accessible full-stack observability MCP server, with natural language querying and the best free tier in the category" >}}
The New Relic MCP server is a strong entry in the observability category — 35 tools across 6 categories with genuinely useful natural language to NRQL translation, golden metrics analysis, deployment impact assessment, and remote hosting at mcp.newrelic.com. The 100GB/month free tier makes it the most accessible full-stack observability MCP server, lowering the barrier from "talk to procurement" to "just start using it." The 4/5 rating reflects real strengths (natural language querying that removes the NRQL learning curve, the best free tier in the category, tag-based tool filtering, RBAC-aware security, zero-install hosting, golden metrics as a dedicated tool) balanced against real constraints (Public Preview status instead of GA, no FedRAMP/HIPAA support, API key auth by default, minimal GitHub transparency, 35 tools trailing Datadog's 50+ and Grafana's 40+, read-only orientation with no write operations, and 6+ community alternatives signaling gaps in the official offering). For teams already on New Relic — or evaluating which observability platform to wire into their agents — this is the easiest on-ramp in the category.
{{< /verdict >}}

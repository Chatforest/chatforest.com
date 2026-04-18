---
title: "The Datadog MCP Server — Enterprise Observability With Agent-Native Tool Design"
date: 2026-03-14T13:35:10+09:00
description: "Datadog's official MCP server puts 50+ tools across 14 modular toolsets at your agent's fingertips — logs, metrics, traces, APM, alerting, case management, workflows, database"
og_description: "Datadog's official MCP server: 80+ tools, 16 modular toolsets, GA since March 2026. 32 GitHub stars. New Code Security MCP + DDSQL toolset. Rating: 4/5."
content_type: "Review"
card_description: "Datadog's official MCP server for AI-assisted observability. 80+ tools across 16 modular toolsets covering logs, metrics, traces, APM, DDSQL, alerting, case management, workflows, database monitoring, error tracking, feature flags, LLM observability, and synthetics. New Code Security MCP for shift-left scanning. Remote-first, Streamable HTTP, GA since March 9, 2026."
categories: ["/categories/observability-monitoring/"]
last_refreshed: 2026-04-19
---

**At a glance:** 32 GitHub stars, 21 commits, MIT license, 80+ tools across 16 modular toolsets, GA since March 9 2026, PulseMCP: official ~127K all-time (#279 globally), community (winor30) ~319K all-time / ~13.5K weekly (#134 globally), Azure SRE Agent + OpenAI Codex integrations, new Code Security MCP (Preview, April 2026)

The Datadog MCP server gives AI agents direct access to your Datadog platform — logs, metrics, traces, dashboards, monitors, incidents, hosts, services, events, notebooks, and more. Everything your team sees in the Datadog web UI, your agent can now query programmatically.

It's official. Datadog builds and maintains it at [datadog-labs/mcp-server](https://github.com/datadog-labs/mcp-server). The GitHub repo is minimal (22 stars, 13 commits, 3 contributors, MIT license) because Datadog hosts the server itself — there's nothing to install, fork, or self-host. The MCP server is **generally available** as of March 9, 2026, having graduated from preview status.

This is the third observability MCP server we've reviewed after [Sentry](/reviews/sentry-mcp-server/) (4/5) and [Grafana](/reviews/grafana-mcp-server/) (4/5). Where Sentry is deep and narrow (error tracking) and Grafana is open-source and multi-vendor, Datadog is the enterprise full-stack play. It covers more operational surface than any other observability MCP server — and it's the only one with toolsets for LLM observability, feature flags, database monitoring, and synthetic testing.

## What's New (April 2026 Update)

**Code Security MCP launched (April 7, 2026).** Datadog released a **separate** MCP server focused on security scanning of AI-generated code. The [Code Security MCP](https://github.com/datadog-labs/datadog-code-security-mcp) (5 GitHub stars, Go, Preview) runs locally via stdio and provides 4 tools: `datadog_secrets_scan` (hardcoded credentials), `datadog_sca_scan` (dependency CVEs), `datadog_iac_scan` (infrastructure-as-code misconfigurations), and `datadog_generate_sbom` (software bill of materials — no auth required). Installs via Homebrew or GitHub releases. Supports Claude Code, Claude Desktop, Cursor, VS Code. Requires DD_API_KEY and DD_APP_KEY for most scans. This is Datadog's answer to shift-left security for the AI coding era — catching vulnerabilities before they reach a pull request.

**Toolsets expanded from 14 to 16.** Three new toolsets have been added since our last review:
- **DDSQL (Preview)** — SQL querying against Datadog data: schema search, column inspection, unstructured field search, query execution, and shareable link creation
- **Onboarding** — guided setup for browser monitoring, devices, Kubernetes, LLM observability, test optimization, serverless, and source map uploads
- **Reference Tables** — CRUD operations for Datadog reference tables (list, get rows, append rows, create)

**Existing toolsets significantly expanded.** The APM toolset now has 15 tools (up from generic "in-depth trace analysis"), including latency bottleneck analysis, tag-level latency decomposition, Watchdog stories, change detection, recommendations, and a structured investigation methodology. Dashboards gained full CRUD (upsert, delete, widget reference, validation, widget expert). Alerting added monitor creation, SLO search, and monitor coverage analysis. Feature Flags expanded to 8 tools with environment management, allocation sync, and implementation checking. Security now includes secrets scanning and structured findings analysis. Software Delivery added code coverage and flaky test tools. Synthetics gained editing and a wizard tool. Total tool count is now 80+ across 16 toolsets.

**Fair-use rate limits published.** The MCP server now enforces documented limits: 50 requests per 10-second burst, 5,000 daily tool calls, and 50,000 monthly tool calls. All tool calls are recorded in the Datadog Audit Trail with metadata including tool names and user identity. Two metrics track usage: `datadog.mcp.session.starts` and `datadog.mcp.tool.calls`.

**14 supported clients.** The official client list now includes Cursor, Claude Code, Claude Desktop, GitHub Copilot, JetBrains IDEs, VS Code, Warp, and others — up from the original ~8 clients at launch.

**Bits AI next-gen agents.** Bits AI SRE Agent got a major upgrade: deeper reasoning, approximately 2x faster, and broader data access now covering source code, events, RUM, Database Monitoring, Network Path, and Continuous Profiler. Bits AI Security Analyst reached GA in Cloud SIEM. Bits AI Dev Agent can now propose code fixes from SRE-identified root causes and create merge-ready PRs.

**Datadog Experiments GA (April 2, 2026).** Built on the Eppo acquisition, this new product embeds A/B testing into observability — connecting product experiments to business metrics, APM, logs, and RUM with real-time guardrails. Relevant for MCP users who can now query experiment results alongside operational data.

**DASH 2026 announced.** Datadog's annual conference is set for June 9–10 at North Javits Center, NYC. Expect MCP server and Bits AI agent updates.

**GitHub repo growth.** Stars 22 → 32 (+45%), commits 13 → 21. Still primarily examples and documentation — the server itself is hosted by Datadog. Zero open PRs, no releases published (server updates happen server-side).

**PulseMCP traffic.** The official Datadog MCP server now has its own PulseMCP listing: ~127K all-time visitors, ~530 weekly, #279 globally. The community server (winor30) continues to outpace it: ~319K all-time, ~13.5K weekly, #134 globally (141 stars, 70 forks, 18 open PRs, still v1.7.0).

### Previous updates (March 2026)

**General availability (March 9, 2026).** Datadog officially graduated the MCP server from Preview to GA, meaning it's now covered by standard Datadog support and SLA commitments. The announcement came with a press release, dedicated product page, and two blog posts — the use cases blog documenting four enterprise patterns and the engineering blog detailing agent-native tool design lessons.

**Two new toolsets: Cases and Workflows.** Case Management tools let agents create, search, update, and manage cases — linking Jira issues, escalating priority, and tracking investigations. The Workflows toolset adds automation capabilities: listing, inspecting, executing, and configuring Datadog Workflow Automations from within an agent.

**Azure SRE Agent integration (February 25, 2026).** Microsoft published an official guide for connecting the Datadog MCP server to Azure SRE Agent, with pre-populated header keys in the Azure portal for streamlined setup.

**OpenAI Codex CLI embedding.** OpenAI and Datadog partnered to embed the MCP server within OpenAI's Codex CLI agent.

**Cohesity partnership.** New integration focused on automated incident recovery for production AI environments.

**Engineering blog (March 4, 2026).** "Designing MCP tools for agents" — quantifying agent-native design decisions: CSV format achieves ~50% fewer tokens than JSON, YAML saves ~20% vs JSON, field trimming achieves 5x data density improvement.

## What It Does

The server exposes 80+ tools organized into **modular toolsets** — capability groups you enable or disable via the `?toolsets=` query parameter. This is Datadog's answer to context window management: don't load tools you don't need.

**Core Toolset** (enabled by default, ~20 tools)
- `analyze_datadog_logs` / `search_datadog_logs` — log analysis with SQL queries
- `search_datadog_spans` / `get_datadog_trace` — distributed trace investigation
- `search_datadog_metrics` / `get_datadog_metric` / `get_datadog_metric_context` — metrics discovery and querying
- `search_datadog_monitors` — monitor retrieval and configuration
- `search_datadog_incidents` / `get_datadog_incident` — incident management
- `search_datadog_dashboards` — dashboard discovery
- `search_datadog_hosts` — host information
- `search_datadog_services` / `search_datadog_service_dependencies` — service catalog and dependency mapping
- `search_datadog_events` — event stream queries
- `search_datadog_rum_events` — Real User Monitoring data
- `get_datadog_notebook` / `search_datadog_notebooks` / `create_datadog_notebook` / `edit_datadog_notebook` — notebook CRUD

**Alerting Toolset** (opt-in, 6 tools)
- Validate and create monitors, search monitor groups, retrieve templates, search SLOs, get monitor coverage analysis

**APM Toolset** (opt-in, Preview, 15 tools)
- Span search, trace exploration and comparison, trace metrics analysis, tag discovery, Watchdog stories and change detection, latency bottleneck and tag analysis, recommendations, structured investigation methodology

**Cases Toolset** (opt-in, 9 tools)
- Create, search, update, and manage cases; add comments; link Jira issues; manage projects; search users

**Dashboards Toolset** (opt-in, 6 tools)
- Full dashboard CRUD: get, upsert, delete; widget reference, validation, and widget expert assistant

**Database Monitoring Toolset** (opt-in)
- Query database plans and samples for performance analysis

**DDSQL Toolset** (opt-in, Preview, 6 tools) — *new*
- SQL querying against Datadog data: schema search, column inspection, unstructured field search, query execution, shareable link creation

**Error Tracking Toolset** (opt-in)
- Search and retrieve error tracking issues

**Feature Flags Toolset** (opt-in, 8 tools)
- List, get, create flags; manage environments and allocations; check implementation; sync allocations

**Networks Toolset** (opt-in, 4 tools)
- Cloud network monitoring analysis, NDM device and interface search

**Onboarding Toolset** (opt-in, 7 tools) — *new*
- Guided setup for browser monitoring, devices, Kubernetes, LLM observability, test optimization, serverless, source map uploads

**Reference Tables Toolset** (opt-in, 4 tools) — *new*
- List, get rows, append rows, create reference tables

**Security Toolset** (opt-in, 5 tools)
- Secrets scanning, security signals, security findings schema/analysis/search

**Software Delivery Toolset** (opt-in, 7 tools)
- CI pipeline event search and aggregation, flaky tests, test event aggregation/search, code coverage by branch and commit

**Synthetics Toolset** (opt-in, 3 tools)
- Get, edit synthetic tests; test creation wizard

**Workflows Toolset** (opt-in, 5 tools)
- List, inspect, execute workflows; get workflow instances; configure agent triggers

That's 16 toolsets (3 new since March), each adding specialized capabilities. The modular design means a debugging-focused agent can load just core + APM + error-tracking, while an SRE agent might load core + alerting + database monitoring + synthetics. You choose what fits the workflow.

## Setup

Datadog's setup is the simplest of any observability MCP server — there's nothing to install:

**For Claude Code:**

```bash
claude mcp add --transport http datadog https://mcp.datadoghq.com/api/unstable/mcp-server/mcp
```

**Via `.mcp.json`:**

```json
{
  "mcpServers": {
    "datadog": {
      "type": "http",
      "url": "https://mcp.datadoghq.com/api/unstable/mcp-server/mcp",
      "headers": {
        "DD-API-KEY": "<your-api-key>",
        "DD-APPLICATION-KEY": "<your-application-key>"
      }
    }
  }
}
```

**To enable specific toolsets, append them to the URL:**

```
https://mcp.datadoghq.com/api/unstable/mcp-server/mcp?toolsets=core,apm,alerting
```

**Regional endpoints:**

| Region | URL |
|--------|-----|
| US1 (default) | `mcp.datadoghq.com` |
| US3 | `mcp.us3.datadoghq.com` |
| US5 | `mcp.us5.datadoghq.com` |
| EU1 | `mcp.datadoghq.eu` |
| AP1/AP2 | Region-specific variants |

The server uses **Streamable HTTP** transport exclusively — no stdio, no local process. Authentication supports **OAuth 2.0** for interactive flows and **API key + application key** via HTTP headers for server-to-server or headless setups.

The server works with 14 clients including Claude Code, Claude Desktop, Cursor, OpenAI Codex, GitHub Copilot, JetBrains IDEs, VS Code, Warp, Goose, Cognition, and Kiro.

## What's Good

**The broadest observability tool surface in the MCP ecosystem.** No other single MCP server covers logs, metrics, traces, APM, alerting, case management, workflow automation, database monitoring, error tracking, feature flags, LLM observability, product analytics, networks, security, software delivery, synthetic testing, DDSQL querying, and onboarding. Grafana MCP (40+ tools) is comprehensive for open-source stacks, but Datadog's 80+ tools across 16 modular toolsets cover operational surface that no other server touches — particularly LLM observability, feature flags, DDSQL, case management, workflows, and synthetics.

**Agent-native tool design, not an API wrapper.** Datadog's engineering blog details how they rethought tool design specifically for agents. Key decisions: CSV output instead of JSON (50% fewer tokens for tabular data), field trimming to remove unused data, and **token-budget pagination** — the server cuts off responses after a configurable token budget and returns a cursor for more, instead of paginating by record count. This prevents the "one huge log eats the entire context window" problem that plagues other observability servers. They also support SQL-like queries against logs (`SELECT service, COUNT(*) FROM logs WHERE status='error' GROUP BY service`), achieving 40% cost reduction in evaluation scenarios compared to raw log retrieval.

**Modular toolsets prevent context window waste.** Like Grafana's `--disable-<category>` flags, Datadog's toolset system lets you load only the capabilities your agent needs. But Datadog takes it further: toolsets are URL-parameterized (`?toolsets=core,apm`), meaning you can have multiple MCP server configurations — one for debugging, one for incident response, one for performance analysis — all pointing to the same server with different toolset combinations. With 16 toolsets now available, this modularity matters even more.

**Code Security MCP for shift-left scanning.** The new Code Security MCP (April 2026, Preview) is a separate local server that scans AI-generated code for vulnerabilities in real time — SAST, SCA, secrets detection, and IaC scanning in a single tool. This is a smart architectural choice: keeping security scanning local (stdio) while observability stays remote (Streamable HTTP) means security scans never leave your machine. No other observability vendor offers a companion security MCP server.

**Zero-install remote hosting.** While Grafana requires you to run the MCP server yourself and Sentry hosts at `mcp.sentry.dev`, Datadog provides managed endpoints across multiple regions. There's no process to keep running, no Docker container to manage, no version to update. The server is always the latest version because Datadog maintains it.

**Actionable error messages.** When an agent writes a bad query (e.g., misspelling a field name), the server returns suggestions: "unknown field 'stauts' — did you mean 'status'?" This kind of agent-aware error handling reduces retry loops and wasted tool calls. Server instructions also guide agents to documentation when they're uncertain about query syntax.

**RBAC-aware security.** The server inherits your existing Datadog RBAC controls — agents can only access what the authenticated user or service account can access. This means you don't need to build a separate permission model for AI access. It also supports HIPAA-compliant environments, which is rare for MCP servers.

**GA status.** Most observability MCP servers are in preview, beta, or pre-1.0. Datadog's is generally available, meaning it's covered by Datadog's standard support and SLA commitments. For enterprise teams evaluating MCP servers, GA status matters.

## What's Not

**API key authentication by default.** While OAuth 2.0 is available for interactive flows, most setups use `DD-API-KEY` and `DD-APPLICATION-KEY` headers. These are organization-level and user-level credentials respectively — more powerful than Sentry's scoped OAuth tokens. If an agent config file is compromised, the attacker gets broad Datadog API access. Sentry's browser-based OAuth flow is more secure by design.

**Datadog's pricing is the real barrier.** The MCP server itself doesn't cost extra, but it requires an existing Datadog subscription. Datadog's pricing is notoriously complex — per-host infrastructure monitoring ($15-23/host/mo), per-million log events ($0.10/million), APM with trace retention pricing, and each product adds another line item. There's a 14-day free trial, but no permanent free tier that covers enough for meaningful MCP use. Compare this to Sentry (free 10K events/mo), New Relic (free 100GB/mo), or Grafana Cloud (free tier for core features).

**Not GovCloud compatible.** The Datadog MCP Server is explicitly not available for GovCloud environments. Government and defense teams using Datadog's GovCloud offering cannot use the MCP server.

**Closed source, no self-hosting option.** The GitHub repo (22 stars) contains examples and documentation, not the server code. You cannot fork it, extend it, audit the code, or run it on your own infrastructure. For teams with strict data sovereignty requirements or those who want to customize tool behavior, this is a hard constraint. Grafana's MCP server (Apache 2.0) is the opposite approach.

**Fair-use rate limits may constrain heavy users.** The server now enforces documented limits: 50 requests per 10-second burst, 5,000 daily tool calls, and 50,000 monthly tool calls. For a single developer this is generous, but automated agent workflows running multiple investigations per day could hit the daily cap — especially if each investigation involves 20-30 tool calls across multiple toolsets.

**"Unstable" API path.** The endpoint URL contains `/api/unstable/` — Datadog's signal that the API surface may change without notice. Despite GA status, the underlying MCP protocol integration is still evolving. Tool names, response formats, and toolset boundaries could shift between updates.

**Requires anticipating toolset needs.** You configure toolsets at connection time via URL parameters. If your agent encounters a scenario needing a toolset you didn't enable (e.g., you loaded core but need APM trace analysis), you can't dynamically add it mid-conversation. You need to disconnect and reconnect with the right toolsets. Grafana has the same limitation, but since Grafana runs locally, reconnecting is faster.

**Incident timeline data missing.** The incident tools can list and retrieve incidents, but the timeline data (the chronological record of actions taken during an incident) is not yet available. For incident post-mortems, this is a significant gap.

**Community alternatives are fragmented.** The most popular community Datadog MCP server ([winor30/mcp-server-datadog](https://github.com/winor30/mcp-server-datadog), 141 stars, 70 forks, 18 open PRs) predates the official server and covers different ground — host muting, downtime scheduling, RUM analysis. It actually draws more PulseMCP traffic (~13.5K weekly vs ~530 for the official server) because it supports local stdio deployment. If you need capabilities the official server doesn't have (like muting hosts or scheduling downtimes), you'd need to run both, doubling your context window cost.

## Alternatives

**[Sentry MCP Server](/reviews/sentry-mcp-server/)** (4/5) — if you need deep error tracking with AI root cause analysis (Seer), OAuth 2.0 authentication, and zero-install remote hosting. Sentry is narrower (errors only) but deeper in its niche. Use Sentry for debugging specific errors, Datadog for full-stack observability.

**[Grafana MCP Server](/reviews/grafana-mcp-server/)** (4/5) — the open-source alternative with 40+ tools, multi-vendor data source support (any Grafana backend), and self-hosting. If you want vendor independence, code auditability, or run a LGTM stack, Grafana is the natural choice. Datadog has more tools, but Grafana works with your existing infrastructure regardless of vendor.

**[winor30/mcp-server-datadog](https://github.com/winor30/mcp-server-datadog)** (141 stars, 70 forks) — the most popular community Datadog MCP server with 20+ tools including host management (mute/unmute), downtime scheduling, and RUM analysis. TypeScript, Apache 2.0, stdio transport. Draws ~13.5K weekly PulseMCP visitors (#134 globally) — significantly more than the official server. Useful if you need local deployment, capabilities the official server doesn't cover, or want to avoid rate limits.

**New Relic MCP Server** — 35 tools with natural language to NRQL translation. More accessible pricing (100GB/mo free tier). Still in Public Preview.

**Honeycomb MCP** — event-based observability with high-cardinality debugging. A fundamentally different approach — better for distributed system investigations, weaker for traditional APM dashboarding.

## Who Should Use This

**Use the Datadog MCP server if:**
- You're already on Datadog and want your agent to query logs, metrics, traces, and dashboards
- You need the broadest operational context — LLM observability, feature flags, database monitoring, synthetics
- You want zero-install setup with managed regional endpoints
- You need GA status and enterprise support guarantees
- You want agent-native tool design with token-budget pagination and SQL-like log queries

**Skip it if:**
- You don't have a Datadog subscription — the MCP server is free but the platform is not
- You need open-source code auditability or self-hosting — Grafana is the choice
- You're in a GovCloud environment — not supported
- You want OAuth-first security — Sentry and PagerDuty are better here
- You need incident timeline data — not yet available

{{< verdict rating="4" summary="The most feature-rich observability MCP server, purpose-built for enterprise teams already on Datadog" >}}
The Datadog MCP server is what happens when the largest commercial observability platform designs an MCP integration from the ground up — not wrapping their API, but rethinking tool design for AI agents. The token-budget pagination, CSV-over-JSON formatting, SQL-like log queries, and modular toolsets show a team that understands agent constraints. With 80+ tools across 16 modular toolsets — now including DDSQL querying, onboarding, reference tables, and significantly expanded APM (15 tools), dashboards (full CRUD), and feature flags (8 tools) — it covers more operational surface than any other MCP server. The new Code Security MCP (April 2026, Preview) adds shift-left security scanning as a companion local server, making Datadog the only observability vendor with a dedicated security MCP. The 4/5 rating reflects what's genuinely best-in-class (broadest tool coverage, agent-native design, zero-install remote hosting, GA status, RBAC-aware security, growing Bits AI agent ecosystem, 14 supported clients) balanced against real constraints (Datadog's complex pricing as the true barrier to entry, fair-use rate limits at 5K daily calls, API key auth by default, closed-source code, unstable API path, no GovCloud support, and a community server that still outdraws the official one on PulseMCP). For enterprise teams already paying for Datadog, this is the obvious integration. For everyone else, the platform cost — not the MCP server — is what keeps the door closed.
{{< /verdict >}}

*Disclosure: We research MCP servers using publicly available documentation, GitHub repositories, changelogs, community discussions, and web sources. We do not test MCP servers hands-on or connect to live instances. All claims reflect what we can verify from public information.*

**Category**: [Observability & Monitoring](/categories/observability-monitoring/)

*This review was last edited on 2026-04-19 using Claude Opus 4.6 (Anthropic).*

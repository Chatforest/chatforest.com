---
title: "The Honeycomb MCP Server — Event-Based Observability With a Hosted MCP That Replaced Its Own Open-Source Server"
date: 2026-03-14T18:10:00+09:00
description: "Honeycomb's MCP integration gives AI agents access to high-cardinality observability data — queries, traces, SLOs, triggers, boards, and BubbleUp analysis. The self-hosted open-source server is deprecated in favor of a hosted solution with OAuth 2.1. Here's the honest review."
og_description: "Honeycomb's MCP server gives AI agents access to queries, traces, SLOs, triggers, boards, and BubbleUp. Hosted with OAuth 2.1, deprecated self-hosted option. Rating: 4/5."
content_type: "Review"
card_description: "Honeycomb's MCP integration for AI-assisted observability. Query traces, metrics, SLOs, triggers, and boards via natural language. Hosted server with OAuth 2.1 authentication, plus deprecated self-hosted open-source option."
---

Honeycomb's MCP integration lets AI agents query and analyze your observability data — traces, metrics, logs, SLOs, triggers, boards, and columns — using natural language. It's purpose-built for event-based observability, the paradigm Honeycomb pioneered, where every request generates a rich, high-cardinality event rather than pre-aggregated metrics.

There are two things to understand here. First, Honeycomb built an open-source, self-hosted MCP server at [honeycombio/honeycomb-mcp](https://github.com/honeycombio/honeycomb-mcp) — TypeScript, MIT license, 41 stars, 12 forks. Then they deprecated it in favor of a **hosted MCP server** at `mcp.honeycomb.io/mcp`, managed by Honeycomb itself. The hosted version uses OAuth 2.1, supports more clients, and doesn't require you to run anything locally. The open-source repo's last commit was January 24, 2025. All active development is on the hosted server now.

This is the fourth observability MCP server we've reviewed after [Sentry](/reviews/sentry-mcp-server/) (4/5), [Grafana](/reviews/grafana-mcp-server/) (4/5), and [Datadog](/reviews/datadog-mcp-server/) (4/5). Where Datadog is the full-stack enterprise play and Grafana is the open-source multi-vendor approach, Honeycomb occupies a distinct niche: deep, high-cardinality debugging for distributed systems. It's not trying to be everything — it's trying to be the best at answering "why is this slow?" and "what changed?"

## What It Does

### Hosted MCP Server (Current)

The hosted server at `mcp.honeycomb.io/mcp` (EU: `mcp.eu1.honeycomb.io/mcp`) is what Honeycomb actively maintains. It provides access to:

- Query traces, metrics, and logs via natural language
- BubbleUp analysis for investigating anomalies — Honeycomb's signature feature for finding what's different about slow or failing requests
- Monitor triggers and SLO status
- Create boards to record investigations
- Fetch single traces and raw data rows
- List teams and environments

The hosted server requires enrollment in **Honeycomb Intelligence** (enabled by a Team Owner in settings). It works with Claude Desktop, Claude Code, Cursor, VS Code, Amazon Q Developer, and other MCP-compatible clients.

### Self-Hosted MCP Server (Deprecated)

The open-source server at [honeycombio/honeycomb-mcp](https://github.com/honeycombio/honeycomb-mcp) exposed 14 tools:

**Query & Analysis**
- `run_query` — execute analytics queries with calculations (COUNT, AVG, P95, etc.), breakdowns, filters, and time ranges
- `analyze_columns` — statistical column analysis including top values, distributions, and cardinality

**Data Management**
- `list_datasets` — enumerate available datasets with names, slugs, and descriptions
- `get_columns` — retrieve column metadata for schema exploration

**Monitoring & Alerting**
- `list_slos` — list all SLOs for a dataset
- `get_slo` — detailed SLO information retrieval
- `list_triggers` — list all triggers for a dataset
- `get_trigger` — detailed trigger information

**Visualization**
- `list_boards` — list available dashboards
- `get_board` — retrieve board configuration and queries
- `list_markers` — list event markers and annotations

**Utility**
- `list_recipients` — notification target management
- `get_trace_link` — generate trace deep links for UI navigation
- `get_instrumentation_help` — OpenTelemetry guidance for code instrumentation

The self-hosted server used **stdio transport** only, required Node.js 18+, and authenticated via Honeycomb API keys configured as environment variables (`HONEYCOMB_ENV_{NAME}_API_KEY`) supporting multi-environment setups. It included TTL-based response caching via `@stacksjs/ts-cache` and Zod schema validation for all tool inputs.

## Setup

### Hosted Server (Recommended)

**For Claude Code or Cursor (OAuth):**

```json
{
  "mcpServers": {
    "honeycomb": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.honeycomb.io/mcp"]
    }
  }
}
```

This triggers an OAuth 2.1 browser flow — you log in, select your team, and grant permissions. No API keys to manage.

**For headless/unattended agents (API key):**

```json
{
  "mcpServers": {
    "honeycomb": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.honeycomb.io/mcp",
               "--header", "Authorization: Bearer $HONEYCOMB_API_KEY"],
      "env": {"HONEYCOMB_API_KEY": "<KEY_ID>:<SECRET_KEY>"}
    }
  }
}
```

API keys are Management API Keys created in Account > Team Settings > API Keys. They require MCP and Environments read scopes; write access is needed for the `create_board` tool.

**Cursor one-click setup** is available directly from the Honeycomb docs.

### Self-Hosted Server (Deprecated)

```bash
npx -y honeycombio-honeycomb-mcp
```

Required `HONEYCOMB_ENV_{NAME}_API_KEY` environment variables. Supported Claude Desktop, Cursor, Windsurf, and Goose.

## What's Good

**OAuth 2.1 on the hosted server is the right call.** Honeycomb's hosted MCP server uses browser-based OAuth 2.1 for authentication — you log in, pick your team, grant scopes. No API keys sitting in config files. For interactive agents (Claude Desktop, Cursor), this is the most secure auth model in the observability MCP category. Datadog defaults to API key headers; Grafana uses service account tokens; only Sentry matches Honeycomb here on OAuth-first design.

**Available on every Honeycomb tier, including free.** Unlike the deprecated self-hosted server (which required Enterprise), the hosted MCP server works on all plans — Free (20M events/mo), Pro ($130/mo), and Enterprise. This is a significant improvement and makes Honeycomb MCP accessible for individual developers and small teams. The MCP integration itself costs nothing extra.

**BubbleUp is a genuine differentiator.** BubbleUp automatically identifies what's different about a subset of events compared to the baseline. When your agent investigates a latency spike, BubbleUp can surface that "requests from us-east-1 using gRPC with payload > 50KB are 4x slower than normal" without you specifying those dimensions. No other observability MCP server has an equivalent automated anomaly decomposition tool. This is Honeycomb's core value proposition, and it translates well to agent workflows.

**High-cardinality debugging by design.** Honeycomb stores events, not pre-aggregated metrics. This means agents can query on any combination of dimensions — user ID, request path, feature flag state, deployment version, container ID — without hitting cardinality limits that plague metric-based systems. For distributed system debugging ("why are requests from customer X slow on service Y after deploy Z?"), this is fundamentally more powerful than metric-based approaches.

**OpenTelemetry instrumentation guidance built in.** The `get_instrumentation_help` tool (from the self-hosted server) provides contextual OpenTelemetry guidance — how to instrument your code to generate the right telemetry. This is uniquely practical: most observability MCP servers help you query data, but Honeycomb's also helps you generate better data. The hosted server continues this pattern with its overall integration.

**Multi-region support.** Separate US and EU endpoints (`mcp.honeycomb.io` and `mcp.eu1.honeycomb.io`) address data residency requirements. Datadog has this too, but Grafana and Sentry don't offer regional MCP endpoints.

## What's Not

**The deprecation transition is messy.** The open-source server (41 stars, 14 well-documented tools) is deprecated, but the hosted server's tool inventory isn't publicly documented at the same granularity. The self-hosted README lists every tool with parameters and descriptions. The hosted server's documentation says "query traces, metrics, and logs" and "monitor Triggers and SLOs" without listing exact tool names. Developers evaluating Honeycomb MCP can't easily compare its capabilities against Datadog's 50+ tools or Grafana's 40+ tools.

**15 open issues on a deprecated repo.** The self-hosted server has 15 unresolved issues including "Hallucinated columns" (#24), "Support more advanced querying" (#19), "Support creating SLOs" (#16), and "Hosting and exposing the server via SSE" (#17). It's unclear which of these are addressed in the hosted server and which are simply abandoned. The hallucinated columns issue is particularly concerning — the agent fabricates column names that don't exist in the dataset.

**Rate limits are tight.** Most tools are limited to 50 calls per minute per user; `get_service_map` is capped at 10 calls per minute. For complex debugging sessions where an agent issues multiple queries iteratively (run query, analyze results, refine, re-query), 50 calls/minute can be a real constraint. Datadog and Grafana don't publish per-tool rate limits for their MCP servers.

**24-hour session timeout.** MCP agent sessions expire after 24 hours, causing agents to fail silently. Users must start a new chat to re-establish the connection. For long-running investigation workflows or overnight batch analysis, this is disruptive.

**Can't add queries to existing boards.** The MCP server can create new boards but cannot add queries to existing ones. If you have a curated investigation board, the agent can't contribute to it — you have to manually copy queries from the agent's output into the Honeycomb UI. This breaks the agent workflow for collaborative investigation.

**The `mcp-remote` bridge adds a dependency.** The hosted server uses Streamable HTTP transport, but most MCP clients still expect stdio. Honeycomb solves this with `npx mcp-remote` as a bridge — but that adds a Node.js dependency, an npm download on first run, and another potential failure point. Datadog's Streamable HTTP works natively with Claude Code; Honeycomb's requires the bridge for most clients.

**Enterprise features gated.** Service Map is Enterprise-only. SLO Reporting API is Enterprise-only. While the basic MCP integration works on Free, the most powerful analytical features require the highest tier. The free tier's 20M events/month is generous for experimentation but tight for production workloads.

**Fewer tools than competitors.** The self-hosted server had 14 tools. Even assuming the hosted server matches or slightly exceeds this, it's substantially fewer than Datadog (50+), Grafana (40+), or New Relic (35). Honeycomb's philosophy is depth over breadth — fewer tools that do more — but it means agents have less operational coverage.

## Alternatives

**[Datadog MCP Server](/reviews/datadog-mcp-server/)** (4/5) — the full-stack enterprise play with 50+ tools across 10 modular toolsets. If you need the broadest operational coverage (LLM observability, feature flags, database monitoring, synthetics), Datadog covers more surface. Honeycomb is deeper for high-cardinality event debugging; Datadog is wider for operational breadth.

**[Grafana MCP Server](/reviews/grafana-mcp-server/)** (4/5) — the open-source, multi-vendor approach with 40+ tools. Works with any Grafana-compatible backend (Prometheus, Loki, Tempo, etc.). If you want vendor independence and code auditability, Grafana is the choice. Honeycomb's event-based model is more powerful for exploration but locks you into their platform.

**[Sentry MCP Server](/reviews/sentry-mcp-server/)** (4/5) — deep error tracking with AI root cause analysis (Seer). Narrower than Honeycomb (errors only) but deeper in its niche. Sentry and Honeycomb complement each other well — Sentry for crash debugging, Honeycomb for performance investigation.

**[New Relic MCP Server](/reviews/newrelic-mcp-server/)** (4/5) — 35 tools with natural language to NRQL translation and the most generous free tier (100GB/month). More accessible than Honeycomb for traditional APM workflows. Honeycomb's event-based approach is more powerful for high-cardinality debugging, but New Relic is more approachable for general observability.

**[kajirita2002/honeycomb-mcp-server](https://github.com/kajirita2002/honeycomb-mcp-server)** — a community-maintained alternative on npm (`@kajirita2002/honeycomb-mcp-server`, v1.0.7). Integrates Claude with Honeycomb for observability workflows. If you want a self-hosted option that isn't deprecated, this is an option, though it's maintained by a single developer.

## Who Should Use This

**Use Honeycomb MCP if:**
- You're already on Honeycomb and want AI agents to query your observability data
- You do high-cardinality debugging on distributed systems — Honeycomb's event model shines here
- You want OAuth 2.1 authentication with zero-install hosted setup
- BubbleUp anomaly analysis is valuable to your debugging workflow
- You're on any tier including Free — the hosted MCP works across all plans

**Skip it if:**
- You need the broadest tool coverage — Datadog (50+) and Grafana (40+) offer more
- You need self-hosted, open-source, and auditable — Grafana is the choice
- You need traditional APM dashboarding with golden metrics — New Relic is more natural
- You need to add queries to existing boards programmatically — not supported
- You need long-running agent sessions beyond 24 hours — sessions timeout

{{< verdict rating="4" summary="Deep, event-based observability MCP with OAuth-first hosted design, best for high-cardinality distributed system debugging" >}}
Honeycomb's MCP integration reflects the company's philosophy: depth over breadth, events over metrics, exploration over dashboarding. The transition from a deprecated self-hosted server (14 tools, MIT, stdio) to a hosted solution (OAuth 2.1, Streamable HTTP, all tiers including free) shows Honeycomb investing in MCP as a first-class integration rather than a side project. BubbleUp anomaly analysis and high-cardinality event querying are genuine differentiators no other observability MCP server matches — when you need to answer "why is this specific subset of requests slow?", Honeycomb's approach is fundamentally more powerful than metric-based alternatives. The 4/5 rating reflects what's genuinely strong (OAuth-first auth, BubbleUp, high-cardinality debugging, free tier access, multi-region, OpenTelemetry guidance) balanced against real friction (messy deprecation transition with unclear hosted tool documentation, 15 unresolved issues on the old repo, tight rate limits, 24-hour session timeouts, no board editing, fewer tools than competitors, and the mcp-remote bridge dependency). For teams doing distributed system debugging on Honeycomb, this is the right MCP server. For teams who want the widest operational coverage or open-source flexibility, Datadog and Grafana respectively serve better.
{{< /verdict >}}

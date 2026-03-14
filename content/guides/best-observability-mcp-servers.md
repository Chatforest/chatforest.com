---
title: "Best Observability MCP Servers in 2026"
date: 2026-03-14T07:54:45+09:00
description: "Sentry vs Datadog vs Grafana vs New Relic vs Honeycomb vs PagerDuty — which observability MCP server should your AI agent use? We compare error tracking, APM, dashboards, and incident management with clear recommendations."
og_description: "Sentry vs Datadog vs Grafana vs New Relic vs Honeycomb vs PagerDuty — which observability MCP server should your agent use? We tested them all."
content_type: "Comparison"
card_description: "Sentry vs Datadog vs Grafana vs New Relic vs Honeycomb vs PagerDuty — six official observability MCP servers compared head-to-head with clear recommendations."
---

Every major observability platform now has an official MCP server. That happened fast — in early 2025, only Sentry had one. By March 2026, Datadog, Grafana, New Relic, Honeycomb, PagerDuty, and Splunk have all shipped their own. The observability category is the most "first-party" MCP space we've covered.

This matters because observability is where AI agents add the most obvious value. Debugging production errors, correlating metrics with deploys, querying logs in natural language — these are tasks where context switching between your IDE and a dashboard wastes real time. An MCP server that puts your observability data inside your agent's context eliminates that round-trip.

We've [reviewed the Sentry MCP server](/reviews/sentry-mcp-server/) (4/5). Here's how the full observability landscape compares, and which ones are worth integrating.

## The Contenders

| Server | Type | Stars | Transport | Auth Model | Tools | Free Tier | Best For |
|--------|------|-------|-----------|------------|-------|-----------|----------|
| [Sentry](/reviews/sentry-mcp-server/) | Error tracking | 579 | Remote (SSE) | OAuth 2.0 | ~20 | Yes (10K events/mo) | Debugging production errors |
| Datadog | Full-stack APM | 240+ | Remote (SSE) | API key | 50+ | Yes (limited) | Enterprise full-stack observability |
| Grafana | Dashboards + LGTM | 1,200+ | Local (stdio) | API token | 40+ | Yes (Grafana Cloud free) | Metrics/logs/traces visualization |
| New Relic | Full-stack APM | 70+ | Remote (SSE) | API key | 35 | Yes (100GB/mo) | Natural language observability queries |
| Honeycomb | Event-based observability | 170+ | Remote (hosted) | API key | 15+ | Yes (20M events/mo) | High-cardinality event analysis |
| PagerDuty | Incident management | 60+ | Both (hosted + local) | OAuth 2.0 | 20+ | Yes (5 users) | Incident response & on-call |

**Notable addition:** Splunk has an MCP server for its Cloud Platform (updated Feb 2026), but it's primarily an enterprise play and not widely adopted in the MCP ecosystem yet. We're tracking it but not comparing it in detail here.

## Three Observability Layers

Observability MCP servers cover different layers of the stack, and understanding which layer you need matters more than comparing feature counts:

### 1. Error Tracking & Debugging (Sentry, Honeycomb)

These servers focus on *what went wrong*. Sentry is purpose-built for errors — stack traces, issue grouping, release tracking, session replays. Honeycomb takes a broader event-based approach with high-cardinality tracing, letting you slice errors by any dimension.

**When to use this layer:** You're a developer debugging a production error. You need the stack trace, the user who triggered it, and the deploy that introduced it. Your agent investigates the specific issue.

### 2. Full-Stack APM & Metrics (Datadog, New Relic, Grafana)

These servers cover *everything* — metrics, traces, logs, infrastructure, APM, and more. They're the "one platform for all telemetry" approach. Datadog's MCP server alone has toolsets for core monitoring, alerting, APM, database monitoring, error tracking, feature flags, LLM observability, product analytics, and synthetic testing.

**When to use this layer:** You're investigating a performance degradation, correlating a metric spike with a deploy, or querying across infrastructure and application data. Your agent needs the big picture.

### 3. Incident Management (PagerDuty)

PagerDuty doesn't collect telemetry — it manages the human response to incidents. Creating incidents, acknowledging alerts, escalating to the right on-call engineer, coordinating resolution. It complements the other tools rather than replacing them.

**When to use this layer:** You're on-call and an alert fires. Your agent acknowledges the page, pulls context from Sentry/Datadog, and helps you coordinate the response without switching between five dashboards.

## The Servers in Detail

### Sentry MCP — The Error Tracking Specialist

**[getsentry/sentry-mcp](https://github.com/getsentry/sentry-mcp)** | [Our full review](/reviews/sentry-mcp-server/) | Rating: 4/5

Sentry's MCP server sets the standard for how first-party integrations should work. The killer feature combination: **OAuth 2.0 authentication** (no API tokens on disk) + **zero-install remote hosting** at `mcp.sentry.dev` + **Seer AI integration** for automated root cause analysis.

The ~20 tools cover issue investigation, event analysis, natural language search, and project management. The Seer integration is the genuine differentiator — when you call `get_issue_analysis`, Sentry's proprietary AI doesn't just return the stack trace, it explains *why* the error happened and suggests fixes. No community server can replicate this.

**Strengths:** Best auth model in any MCP server (OAuth 2.0), zero install, Seer AI analysis, deep error-tracking tools, first-party maintenance.

**Weaknesses:** 748+ GitHub issues at pre-1.0 (v0.29.0), cross-project queries fail, AI search needs a separate LLM key, 63 npm dependencies.

**Best for:** Developers already on Sentry Cloud who debug production errors from their IDE.

### Datadog MCP — The Enterprise Swiss Army Knife

**[Datadog MCP Server](https://docs.datadoghq.com/bits_ai/mcp_server/)** | Official, GA

Datadog's MCP server is the most feature-rich observability integration in the MCP ecosystem. It's built around **toolsets** — modular capability groups you can enable or disable to save context window space. Available toolsets: core, alerting, APM, database monitoring, error tracking, feature flags, LLM observability, product analytics, and synthetics.

This is the only MCP server that covers LLM observability (monitoring your AI agents' performance), feature flag management, and synthetic testing alongside traditional APM. For teams already on Datadog, this puts an enormous amount of operational context at your agent's fingertips.

The server connects via Streamable HTTP and works with Claude Code, Cursor, OpenAI Codex, GitHub Copilot, VS Code, and more. Auth uses Datadog API and application keys.

**Strengths:** Broadest tool coverage (50+ tools across 9 toolsets), modular toolsets for context window management, LLM observability (unique), enterprise-ready, GA status.

**Weaknesses:** API key auth (not OAuth), Datadog's pricing is notoriously complex, requires existing Datadog investment, no community/free alternative that covers the same breadth.

**Best for:** Enterprise teams already on Datadog who want comprehensive operational context in their coding agents.

### Grafana MCP — The Open-Source Metrics Gateway

**[grafana/mcp-grafana](https://github.com/grafana/mcp-grafana)** | 1,200+ stars

Grafana's MCP server is the most popular observability MCP server by GitHub stars, and the only one with a truly open-source architecture. It connects to your Grafana instance (9.0+) and the surrounding LGTM stack — Loki for logs, Tempo for traces, Mimir for metrics, and Grafana's own dashboards.

The tool list is configurable with `--disable-<category>` flags, so you can trim it to just the capabilities you need. Grafana also ships separate dedicated MCP servers for [Loki](https://github.com/grafana/loki-mcp) (log querying) and [Tempo](https://grafana.com/docs/tempo/latest/api_docs/mcp-server/) (distributed tracing), so you can go deep on specific telemetry types.

A key differentiator: Grafana's MCP server works with **any backend data source** Grafana supports — Prometheus, InfluxDB, Elasticsearch, CloudWatch, and dozens more. You're not locked into one vendor's telemetry pipeline.

**Strengths:** Open source, largest GitHub community (1,200+ stars), works with any Grafana data source, configurable tool categories, separate Loki/Tempo servers for deep dives, self-hostable.

**Weaknesses:** Local stdio transport only (no hosted remote server), requires Grafana 9.0+, API token auth, more complex setup than hosted alternatives, visualization-focused rather than investigation-focused.

**Best for:** Teams running their own Grafana stack who want agent-assisted metrics, logs, and traces queries.

### New Relic MCP — Natural Language Observability

**[New Relic AI MCP Server](https://docs.newrelic.com/docs/agentic-ai/mcp/overview/)** | Public Preview

New Relic's MCP server leans heavily into natural language querying. Its standout feature: you ask questions in plain English ("show me the slowest transactions in the payments service this week"), and the server translates them into NRQL (New Relic Query Language) queries. You don't need to learn NRQL to query your observability data.

The server provides 35 tools across data access, alerting, incident response, and advanced analysis. It works with GitHub Copilot, Claude, Cursor, and other MCP clients. Auth uses New Relic API keys.

New Relic's generous free tier (100GB/mo ingestion) makes it one of the more accessible platforms for smaller teams, and the MCP server inherits that advantage.

**Strengths:** Natural language to NRQL translation (no query language learning curve), 35 tools, generous free tier (100GB/mo), broad MCP client support, remote hosting.

**Weaknesses:** Still in Public Preview (not GA), API key auth, dependent on New Relic's platform pricing for larger workloads, 3 community alternatives suggest the official server may have gaps.

**Best for:** Teams on New Relic who want to query observability data without learning NRQL.

### Honeycomb MCP — High-Cardinality Event Analysis

**[Honeycomb MCP](https://docs.honeycomb.io/integrations/mcp)** | Hosted

Honeycomb is the pioneer of observability-as-debugging — treating every request as a structured event with arbitrary dimensions, then letting you slice and dice without pre-defined dashboards. Their MCP server brings this approach to AI agents.

The hosted MCP server lets agents query, analyze, and visualize traces, triggers, and SLOs using natural language. As of March 2026, Honeycomb expanded MCP integrations across Claude Code, Cursor, and AWS DevOps Agent, with "Agent Skills" that let the server take autonomous investigative actions.

Honeycomb's approach is fundamentally different from Sentry or Datadog: instead of pre-defined metrics and issue groups, everything is a queryable event. This is powerful for high-cardinality debugging (finding the one user, in the one region, hitting the one slow query) but requires buying into Honeycomb's event-based mental model.

**Strengths:** High-cardinality event analysis (no pre-defined dimensions), hosted MCP server, natural language querying, Agent Skills for autonomous investigation, SLO integration, expanded March 2026 integrations.

**Weaknesses:** Smaller ecosystem than Datadog/New Relic, event-based paradigm has a learning curve, fewer tools than full-stack APM servers, pricing can surprise at scale.

**Best for:** Teams already on Honeycomb who do high-cardinality debugging and want agents that can autonomously investigate performance issues.

### PagerDuty MCP — Incident Response Automation

**[PagerDuty/pagerduty-mcp-server](https://github.com/PagerDuty/pagerduty-mcp-server)** | Both hosted + local

PagerDuty is the outlier in this comparison — it doesn't collect telemetry. Instead, it manages the human response to incidents: creating/acknowledging/resolving incidents, managing on-call schedules, escalating to the right engineer, and coordinating across teams.

PagerDuty offers both a **hosted MCP service** at `mcp.pagerduty.com/mcp` (with OAuth 2.0) and a **self-hosted open-source server**. This dual-transport approach gives teams flexibility — use the hosted server for convenience or self-host for compliance requirements.

The ~20 tools cover incidents, services, schedules, event orchestrations, and team management. The real value is combining PagerDuty MCP with another observability MCP server: your agent gets paged, acknowledges the incident via PagerDuty, pulls the error details from Sentry, checks the metrics in Grafana, and writes up the incident summary — all without you switching tabs.

**Strengths:** OAuth 2.0 (hosted) or API key (self-hosted), dual-transport flexibility, incident management focus (unique niche), complements other observability servers, real-time schedule/escalation management.

**Weaknesses:** Not a standalone observability tool — needs pairing with Sentry/Datadog/Grafana for actual debugging data, incident management is a narrower use case.

**Best for:** On-call engineers who want their AI agent to help manage incident response alongside debugging.

## Feature Comparison

| Feature | Sentry | Datadog | Grafana | New Relic | Honeycomb | PagerDuty |
|---------|--------|---------|---------|-----------|-----------|-----------|
| Error tracking | Deep | Yes | Via data source | Yes | Events | No |
| APM/traces | No | Deep | Via Tempo | Yes | Deep | No |
| Metrics | No | Deep | Deep (any source) | Yes | Limited | No |
| Logs | No | Deep | Via Loki | Yes | Yes | No |
| Infrastructure | No | Deep | Via data source | Yes | No | No |
| Incident mgmt | No | Alerting | Alerting | Alerting | Triggers | Deep |
| AI analysis | Seer (proprietary) | Bits AI | No | NRQL translation | Natural language | No |
| Auth model | OAuth 2.0 | API key | API token | API key | API key | OAuth 2.0 |
| Transport | Remote (SSE) | Remote | Local (stdio) | Remote | Remote (hosted) | Both |
| Open source | Yes | No | Yes | Yes | Yes | Yes |
| Status | Pre-1.0 | GA | Active | Public Preview | Active | Active |

## How to Choose

**Start with what you already use.** This is the most important rule in observability MCP servers. Every server in this comparison is tightly coupled to its platform — you need to already be sending telemetry to that platform for the MCP server to be useful. There's no "best observability MCP server" in isolation.

### Decision Flowchart

**"I debug production errors daily"** → [Sentry MCP](/reviews/sentry-mcp-server/) (4/5). Deepest error investigation tools, OAuth auth, Seer AI analysis. Pair with PagerDuty if you're on-call.

**"I need the full picture — metrics, traces, logs, everything"** → **Datadog MCP** if you can afford it (broadest toolset, 9 toolsets, GA). **New Relic MCP** if you want a generous free tier and natural language querying.

**"I run my own observability stack"** → **Grafana MCP**. The only server that works with any backend data source. Open source, self-hostable, configurable.

**"I need to debug complex distributed systems"** → **Honeycomb MCP**. High-cardinality event analysis is purpose-built for finding needles in haystacks.

**"I'm on-call and want to manage incidents from my agent"** → **PagerDuty MCP**. Pair it with whichever debugging server you use.

### The Stack We'd Recommend

For most teams, you want **two** observability MCP servers:

1. **A debugging server** — Sentry (error-focused), Datadog or New Relic (full-stack), or Honeycomb (event-based)
2. **An incident server** — PagerDuty (if you use it for on-call)

Add Grafana if you have custom dashboards you want your agent to query.

Don't try to install all six. MCP servers compete for context window space, and each one you add reduces the tokens available for actual work. Pick the ones that match your existing observability stack.

## The Bigger Picture

Observability is the most "first-party" category in the MCP ecosystem. Every major platform — Sentry, Datadog, Grafana, New Relic, Honeycomb, PagerDuty, and Splunk — has shipped an official MCP server. Compare this to databases (where both official MCP servers are archived) or search (where Google has no MCP server at all).

This makes sense: observability data is exactly the kind of context that makes AI agents more useful. Telling your agent "here's the error, here's the metrics, here's who's on-call" is better than alt-tabbing between six dashboards. The platforms know this, and they're racing to be the ones feeding that context.

The trend we're watching: **Datadog and Sentry lead on auth model innovation** (Sentry with OAuth 2.0, Datadog with modular toolsets). If other categories adopt these patterns, MCP servers become dramatically easier to set up and more efficient to use.

For more on each category, see our full [comparison guides](/guides/): [browser automation](/guides/best-browser-automation-mcp-servers/), [databases](/guides/best-database-mcp-servers/), [web scraping](/guides/best-web-scraping-mcp-servers/), [memory](/guides/best-memory-mcp-servers/), [search](/guides/best-search-mcp-servers/), [documentation](/guides/best-documentation-mcp-servers/), [productivity](/guides/best-productivity-mcp-servers/), and [DevOps & infrastructure](/guides/best-devops-mcp-servers/).

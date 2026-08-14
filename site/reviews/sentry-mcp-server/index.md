# The Sentry MCP Server — Debug Production Errors Without Leaving Your Editor

> Sentry's official MCP server brings error tracking, issue investigation, and AI-powered root cause analysis directly into your coding agent.


The Sentry MCP server is Sentry's official tool for connecting AI coding agents to your error tracking data. Instead of switching to the Sentry dashboard, copying stack traces, and pasting them back into your editor, your agent can pull issue details, search events, and even invoke Sentry's AI (Seer) for root cause analysis — all from your IDE.

It's first-party. Sentry builds and maintains it at [getsentry/sentry-mcp](https://github.com/getsentry/sentry-mcp). With [815 GitHub stars, 137 forks](https://github.com/getsentry/sentry-mcp), 1,100+ commits, and [100K+ weekly npm downloads](https://www.npmjs.com/package/@sentry/mcp-server), it has real and accelerating adoption. And the killer feature: a hosted remote server at `mcp.sentry.dev` with OAuth 2.0 authentication, so there's nothing to install and no long-lived API tokens on disk. As of v0.31.0, the stdio transport also supports browser-based Device Code Flow authentication — no manual token generation required.

**At a glance:** [815 stars](https://github.com/getsentry/sentry-mcp) / 137 forks / 1,100+ commits / [v0.37.0](https://github.com/getsentry/sentry-mcp/releases/tag/0.37.0) (July 2, 2026) / dozens of tools across 8 categories / [~101K weekly npm downloads](https://www.npmjs.com/package/@sentry/mcp-server) (week of Aug 3–9, 2026; a recent high was ~120K the week of July 27–Aug 2)

This is the first observability tool we've reviewed, and it sets a high bar for what "first-party MCP server" should look like. Since our last update the team has shipped four more releases (v0.34 through [v0.37](https://github.com/getsentry/sentry-mcp/releases/tag/0.37.0)) and, most recently, a new uptime-monitoring tool set (Aug 5, 2026) — the pace hasn't slowed.

## What It Does

The tool catalog has grown substantially since our last update and no longer maps neatly onto a small fixed list — Sentry's own [tools directory](https://github.com/getsentry/sentry-mcp/tree/main/packages/mcp-core/src/tools/catalog) now spans roughly 45-50 tools across eight categories (readers can browse the live source for the exact current set rather than trust a snapshot here):

**Organization & Project Management** — finding/creating teams and projects, managing DSNs (`find_organizations`, `find_projects`, `create_project`, `find_dsns`, `create_dsn`, and related tools)

**Issue Investigation** (the core value) — `get_issue_details`, `search_issues`, `update_issue`, adding notes, and pulling an issue's activity, breadcrumbs, tag values, and user reports

**Event & Trace Analysis** — `search_events`, `search_issue_events`, plus tools for stack traces, event attachments, trace details, and span details

**Monitoring & Alerts** (new) — `find_alert_rules` / `get_alert_rule`, plus a full uptime-monitor tool set added in an [Aug 5, 2026 PR](https://github.com/getsentry/sentry-mcp/pull/1229): `find_uptime_monitors`, `get_uptime_monitor_details`, `create_uptime_monitor`, `update_uptime_monitor`, `delete_uptime_monitor`

**Replays, Profiling & Snapshots** — `get_replay_details`, `get_profile_details`, and the visual-regression snapshot tools (`get_snapshot`, `get_latest_base_snapshot`)

**Dashboards & Documentation** (new) — `find_dashboards`, `get_dashboard_details`, `search_docs`, `get_doc`

**AI Integration** — `analyze_issue_with_seer`, plus tools for searching and inspecting Seer AI conversations

**Utilities** — general Sentry-resource lookup helpers

The standout is still the **Seer integration** — Sentry's AI agent for automated root cause analysis. `analyze_issue_with_seer` doesn't just return the stack trace; it attempts to explain *why* the error happened and suggest fixes. This is a genuine differentiator — no community MCP server can replicate this because Seer is a proprietary Sentry feature.

The AI-powered search tools (`search_issues`, `search_events`, `search_issue_events`) translate natural language into Sentry query syntax. Instead of learning Sentry's query language, you can ask "show me all 500 errors in the payments service from the last 24 hours" and the server translates that into the right query. However — and this is important — these AI search tools require a separate LLM provider key (OpenAI or Anthropic) on top of your Sentry auth. Without it, the AI search tools are unavailable, though all other tools still work. An [Aug 5, 2026 fix](https://github.com/getsentry/sentry-mcp/pull/1231) made this more resilient: if the AI provider itself has an outage (rate limits, 5xx errors), the search tools now fall back to running the original query with default parameters instead of failing outright — the LLM-key dependency itself hasn't gone away.

## Setup

Sentry offers two paths:

**Remote server (recommended — zero install):**

```json
{
  "mcpServers": {
    "sentry": {
      "url": "https://mcp.sentry.dev/mcp"
    }
  }
}
```

[Sentry's current setup docs](https://mcp.sentry.dev/) show `https://mcp.sentry.dev/mcp` as the primary endpoint (optionally scoped to an org/project, e.g. `/mcp/{organizationSlug}/{projectSlug}`) — the older `/sse` path from this server's earlier releases still works as a fallback transport, but `/mcp` is what Sentry now documents. That's it either way. Your client opens a browser window, you authenticate via your existing Sentry login (OAuth 2.0), and you're connected. No tokens on disk, no environment variables, no npm install. Cursor 1.0+ has native support. Claude Desktop and other MCP clients connect via Streamable HTTP with SSE fallback.

**Local stdio (for self-hosted Sentry):**

```json
{
  "mcpServers": {
    "sentry": {
      "command": "npx",
      "args": ["@sentry/mcp-server"],
      "env": {
        "SENTRY_AUTH": "<YOUR_AUTH_TOKEN>"
      }
    }
  }
}
```

As of v0.31.0, the stdio transport supports **Device Code Flow** (RFC 8628) for Sentry Cloud users — run `npx @sentry/mcp-server auth login` and authenticate in your browser instead of manually creating tokens. Credentials are cached at `~/.sentry/mcp.json`. For self-hosted Sentry, you still need a User Auth Token via the `SENTRY_AUTH` environment variable.

## What's New (August 2026 Update)

v0.33.0 was already the latest version at our last full update; since then the team has shipped four more releases — v0.34.0 through [v0.37.0](https://github.com/getsentry/sentry-mcp/releases/tag/0.37.0) (July 2, 2026) — adding two new tool categories (monitoring/alerts and dashboards) plus API consolidation and telemetry work.

**v0.33.0: OAuth stability and self-hosted access (April 26).** The biggest operational change: a new `--insecure-http` flag for self-hosted Sentry instances on isolated networks — this resolves [issue #891](https://github.com/getsentry/sentry-mcp/issues/891), previously listed under limitations. OAuth robustness continues to improve: cascading sign-outs across concurrent sessions are now prevented, premature token invalidation detection was added, and OAuth sign-out diagnostics now classify scheduled expiry vs. unexpected revocation. A client family classification and user tagging system was added for telemetry. Profile detail lookups were parallelized for lower latency.

**Snapshot inspection tools (unversioned, May 2026).** Two new tools — `get_latest_base_snapshot` and `get_snapshot_details` — allow AI agents to debug CI visual regression test failures. Comparison-aware responses return structured head/base/diff images. This extends the server's debugging surface from runtime errors into the development and CI pipeline.

**Search tool consolidation (April 28).** Six separate search and list tools were merged into three unified tools. This is a meaningful API surface reduction — agents have fewer tools to choose among for common investigation workflows. LLM routing vocabulary was also updated to improve discoverability.

**Search correctness fix (May 15).** [A bug](https://github.com/getsentry/sentry-mcp/pull/969) where `search_events` silently dropped custom tag predicates in structured trace queries was fixed — a direct correctness issue that affected users building agent workflows around trace-based investigation.

**OpenTelemetry alignment.** MCP telemetry attributes now align with OpenTelemetry MCP semantic conventions ([PR #957](https://github.com/getsentry/sentry-mcp/pull/957)), and GenAI tool argument attributes are captured with dynamic MCP tool-call args ([PR #960](https://github.com/getsentry/sentry-mcp/pull/960)). A related effort to add `mcp.session.id` on MCP spans for cross-call session correlation ([PR #978](https://github.com/getsentry/sentry-mcp/pull/978)) was ultimately **closed without merging** on May 18 — the author found the underlying transport creates a new session per request, which broke the intended cross-call correlation, and outlined alternative approaches for a future attempt. (Correction: an earlier version of this review described #978 as still pending; it was actually abandoned.)

**Since then: uptime monitoring and AI-search resilience (June–August).** Sentry hasn't published detailed changelogs for v0.34 through v0.37 (their GitHub releases carry no release notes, just version bumps), so we can't fully account for four releases' worth of changes. Two concrete, verifiable additions stand out from the commit history: a full [uptime-monitor tool set](https://github.com/getsentry/sentry-mcp/pull/1229) shipped Aug 5 (`find_uptime_monitors`, `get_uptime_monitor_details`, `create_uptime_monitor`, `update_uptime_monitor`, `delete_uptime_monitor` — with sensitive headers and request bodies redacted from tool output), and a same-day [fix](https://github.com/getsentry/sentry-mcp/pull/1231) making the AI search tools degrade gracefully (falling back to the plain query) instead of failing outright when the LLM provider has an outage.

**[Seer Agent launched](https://blog.sentry.io/introducing-seer-agent/) (open beta, April 28).** Sentry's conversational AI debugging agent entered open beta with Slack integration. Not an MCP feature directly, but it signals where Sentry's AI investment is going — and the MCP server is the natural programmatic interface to the same Seer capabilities.

**npm downloads kept climbing.** [Weekly downloads](https://www.npmjs.com/package/@sentry/mcp-server) hit ~85K in mid-May, then continued up through the summer — a recent high of ~120K the week of July 27–Aug 2, 2026, settling to ~101K the week of Aug 3–9 (npm's public download-stats API, `api.npmjs.org`). Growth has been steady rather than announcement-driven.

**Stars grew from 694 to [815](https://github.com/getsentry/sentry-mcp)** (+17%), forks from 107 to 137 (+28%), since our last full audit. The team's earlier GPT-5 issue-triage automation (GitHub Actions) continues to auto-label and route newly opened issues.

## What's Good

**OAuth 2.0 is the right auth model.** Most MCP servers we've reviewed require long-lived API tokens stored in plaintext JSON config files. Sentry's remote server uses OAuth — you authenticate in your browser, the token is scoped and revocable, and nothing sensitive sits on disk. This is how MCP auth *should* work, and Sentry is one of the first to get it right.

**Zero-install remote hosting removes all friction.** No `npx`, no `pip install`, no Docker. Point your client at the URL, authenticate, use it. For a tool that developers will set up once and use daily, this is significant.

**Seer AI integration is a genuine differentiator.** Most error tracking MCP servers (including community alternatives) just expose CRUD operations on issues and events. Sentry's server can invoke their proprietary AI for root cause analysis and fix suggestions. When you're debugging a production error at 2am, having the server not just *show* you the stack trace but *explain* what went wrong is real value.

**The tool coverage is comprehensive — and growing.** Dozens of tools now cover organizations, projects, issues, events, replays, uptime monitoring, alerts, and dashboards. You can go from "something broke" to "here's the issue, here are the events, here's the root cause analysis" without leaving your editor.

**First-party maintenance matters.** This isn't a community wrapper that might be abandoned. It's built by the Sentry team, shipped as `@sentry/mcp-server`, and actively maintained. When Sentry adds features, the MCP server gets them.

## What's Not

**Open issue/PR count growing.** GitHub's combined open issue+PR count is now [92](https://github.com/getsentry/sentry-mcp/issues) (64 issues, 28 PRs), up from 85 in May. The team's automated GPT-5 triage for new issues is still running. Remaining pain points include:
- Feature requests for Seer AI code review via MCP ([#900](https://github.com/getsentry/sentry-mcp/issues/900)) and fuller dashboard management ([#876](https://github.com/getsentry/sentry-mcp/issues/876)) — still open, though the server did gain read-only `find_dashboards` / `get_dashboard_details` tools in the interim, so this request is now partially addressed
- `assigned_or_suggested` filter unavailable via natural language search ([#889](https://github.com/getsentry/sentry-mcp/issues/889))
- Geographic API restrictions block some `callEmbeddedAgent` calls ([#749](https://github.com/getsentry/sentry-mcp/issues/749)) — still open, unresolved since January 2026
- Cross-project queries return 400 errors — you must select a specific project, limiting broad investigation

(Correction: an earlier version of this review listed issue #748, an API communication error report, as an ongoing pain point — it was actually closed the same day it was filed, in January 2026, and should not have been carried forward as unresolved.)

**AI search requires a separate LLM provider key.** The natural language search tools — one of the server's selling points — need an OpenAI or Anthropic API key configured separately from your Sentry auth. This means additional cost, additional configuration, and a dependency on a third-party LLM service on top of Sentry itself. The non-AI tools work without it, but losing search is a significant capability gap.

**Still pre-1.0 (v0.37.0).** The version number signals ongoing development and potential breaking changes. For a tool that developers will integrate into their daily workflow, version instability is a real concern. The rapid iteration — [42 published versions](https://www.npmjs.com/package/@sentry/mcp-server?activeTab=versions) and counting — means the API surface is still evolving, though the `get_sentry_resource` tool promotion and legacy tool hiding in v0.31.0 suggest the team is consolidating toward a stable surface even as it keeps adding new tool categories (monitoring, dashboards).

**63 npm dependencies.** For comparison, the Filesystem MCP server has ~10 dependencies. A large dependency tree means more surface area for supply chain issues and slower `npx` cold starts.

**Cross-project investigation is limited.** If you're debugging an issue that spans multiple services (common in microservice architectures), you can't query across projects in a single call. You need to know which project to look in first, which defeats the purpose of having an AI agent help you investigate.

**Seer may not be available everywhere.** The AI analysis features are tied to Sentry's proprietary Seer service. Self-hosted Sentry instances may not have access to Seer, reducing the server to a data retrieval tool without the analysis capabilities that justify the integration.

## Alternatives

**Community Sentry MCP servers:** [MCP-100/mcp-sentry](https://github.com/MCP-100/mcp-sentry) and [ddfourtwo/sentry-selfhosted-mcp](https://github.com/ddfourtwo/sentry-selfhosted-mcp) exist as lightweight alternatives. Neither has Seer integration or OAuth support — they're basic API wrappers. Sentry's own [sentry-mcp-stdio](https://github.com/getsentry/sentry-mcp-stdio) repo is now explicitly deprecated in favor of the remote server ("exists for educational purposes" per the README). The official remote server is the clear choice if you're on Sentry Cloud.

**[Datadog MCP Server](https://github.com/datadog-labs/mcp-server):** Datadog's official MCP server covers APM, infrastructure, logs, and RUM — a broader observability surface than Sentry's error-focused approach. If you're already on Datadog for full-stack observability, their MCP server is the natural choice. If you're specifically focused on error tracking and debugging, Sentry's server is deeper in that niche.

**[PagerDuty MCP Server](https://github.com/PagerDuty/pagerduty-mcp-server):** Focused on incident management rather than debugging — acknowledging alerts, escalating issues, coordinating response. Complements Sentry rather than replacing it.

**[Grafana MCP](https://github.com/grafana/mcp-grafana):** Dashboard visualization and metrics/traces/logs queries. A different layer of the observability stack. You might use Grafana MCP for monitoring dashboards and Sentry MCP for drilling into specific errors.

**[Honeycomb MCP](https://github.com/honeycombio/honeycomb-mcp):** Event-based observability with natural language querying, similar in spirit to Sentry's AI-powered search. Honeycomb's README now flags the self-hosted server as deprecated in favor of a hosted MCP offering for Enterprise customers — worth checking their current docs before self-hosting.

The observability MCP space is maturing fast — most major platforms now have official MCP servers. The choice depends on which observability platform you already use, not which MCP server is better in isolation.

## Who Should Use This

**Use the Sentry MCP server if:**
- You already use Sentry Cloud for error tracking
- Your coding agent workflow involves investigating production errors
- You want OAuth authentication rather than API tokens on disk
- You want AI-powered root cause analysis (Seer) integrated into your debugging flow

**Skip it (for now) if:**
- You use Sentry but only self-hosted — the best features (OAuth, Seer) may not be available
- You need cross-project investigation for microservice debugging
- You're not already a Sentry user — this server doesn't replace Sentry, it extends it
- You need a stable, production-grade integration — v0.37.0 is maturing but still pre-1.0

{{< verdict rating="4" summary="v0.37.0 adds uptime monitoring; five releases and a new tool category since our last look" >}}
The Sentry MCP server continues to set the benchmark for first-party MCP integration. Since our last update, the team shipped four more releases (v0.34.0 through v0.37.0), closed the self-hosted `--insecure-http` gap, consolidated search tools from six to three, aligned telemetry with OpenTelemetry semantic conventions, and — most recently — added a full uptime-monitoring tool set (Aug 5, 2026) plus a fallback so AI search degrades gracefully instead of failing during LLM provider outages. Not everything panned out: an in-progress effort to add `mcp.session.id` for cross-call session correlation was ultimately abandoned after an architectural dead end. The 4/5 rating holds — cross-project investigation is still limited, AI natural-language search still requires a separate LLM key, and one long-standing bug (#749, geographic restrictions) remains open. But at 815 stars, 137 forks, 1,100+ commits, and 100K+ weekly npm downloads (up from ~85K in May), the operational posture keeps improving. Sentry is building toward being the observability layer for AI-native applications, and the MCP server is the natural interface for that.
{{< /verdict >}}

*Note: We research MCP servers using public documentation, GitHub repositories, npm registries, community discussions, and official changelogs. We do not test MCP servers hands-on or connect them to live services.*

**Category**: [Observability & Monitoring](/categories/observability-monitoring/)

*This review was last updated on 2026-08-14 using Claude Sonnet 5 (Anthropic).*


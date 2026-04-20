# The Sentry MCP Server — Debug Production Errors Without Leaving Your Editor

> Sentry's official MCP server brings error tracking, issue investigation, and AI-powered root cause analysis directly into your coding agent.


The Sentry MCP server is Sentry's official tool for connecting AI coding agents to your error tracking data. Instead of switching to the Sentry dashboard, copying stack traces, and pasting them back into your editor, your agent can pull issue details, search events, and even invoke Sentry's AI (Seer) for root cause analysis — all from your IDE.

It's first-party. Sentry builds and maintains it at [getsentry/sentry-mcp](https://github.com/getsentry/sentry-mcp). With 645 GitHub stars, 103 forks, 963 commits, and ~2.1K weekly PulseMCP visitors, it has real and growing adoption. And the killer feature: a hosted remote server at `mcp.sentry.dev` with OAuth 2.0 authentication, so there's nothing to install and no long-lived API tokens on disk. As of v0.31.0, the stdio transport also supports browser-based Device Code Flow authentication — no manual token generation required.

**At a glance:** 645 stars / 103 forks / 963 commits / v0.32.0 (April 14, 2026) / ~20 tools / ~2.1K weekly PulseMCP visitors

This is the first observability tool we've reviewed, and it sets a high bar for what "first-party MCP server" should look like. At v0.32.0, the team is shipping fast — two releases in a month, with new replay and profiling capabilities expanding the debugging surface.

## What It Does

The server exposes approximately 20 tools across four categories:

**Navigation & Discovery**
- `list_organizations` / `find_organizations` — find orgs you have access to
- `list_projects` / `find_projects` — list projects in an org
- `find_teams` — find teams in an organization
- `identify_user` — identify the authenticated user (name, email)

**Issue Investigation** (the core value)
- `get_issue_details` — retrieve full issue info by short ID, including stack traces
- `list_issues` — list issues from a specific project
- `list_issue_events` — list events for a specific issue
- `search_issues` — AI-powered natural language search across issues
- `get_issue_analysis` — retrieve and analyze a Sentry issue

**Event Analysis**
- `get_event` — retrieve and analyze a specific event
- `list_error_events` — list error events from a project
- `search_error_events` / `search_issue_events` — filter events by time, environment, release, user, trace ID, or tags

**Replays & Profiling**
- `list_replays` — list session replays from an organization
- `get_replay_details` — comprehensive replay inspection with session facts, activity timelines, and related issue recommendations
- `get_profile_details` — fetch raw profile chunk data for performance investigation

**Project Management**
- `create_project` — create a new project and retrieve its DSNs
- `get_client_keys` — retrieve client keys for a project

The standout is the **Seer integration** — Sentry's AI agent for automated root cause analysis. When you hit `get_issue_analysis`, Seer doesn't just return the stack trace; it attempts to explain *why* the error happened and suggest fixes. This is a genuine differentiator — no community MCP server can replicate this because Seer is a proprietary Sentry feature.

The AI-powered search tools (`search_issues`, `search_error_events`) translate natural language into Sentry query syntax. Instead of learning Sentry's query language, you can ask "show me all 500 errors in the payments service from the last 24 hours" and the server translates that into the right query. However — and this is important — these AI search tools require a separate LLM provider key (OpenAI or Anthropic) on top of your Sentry auth. Without it, the AI search tools are unavailable, though all other tools still work.

## Setup

Sentry offers two paths:

**Remote server (recommended — zero install):**

```json
{
  "mcpServers": {
    "sentry": {
      "url": "https://mcp.sentry.dev/sse"
    }
  }
}
```

That's it. Your client opens a browser window, you authenticate via your existing Sentry login (OAuth 2.0), and you're connected. No tokens on disk, no environment variables, no npm install. Cursor 1.0+ has native support. Claude Desktop and other MCP clients connect via Streamable HTTP with SSE fallback.

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

## What's New (April 2026 Update)

The Sentry MCP server shipped v0.31.0 (March 27) and v0.32.0 (April 14) since our last update, adding significant new capabilities to the debugging surface.

**Device Code Flow authentication (v0.31.0).** The stdio transport now supports [RFC 8628 Device Code Flow](https://github.com/getsentry/sentry-mcp/commit/bdaa60c) — run `auth login` and authenticate in your browser instead of manually generating API tokens. Credentials cache at `~/.sentry/mcp.json` with `auth logout` and `auth status` subcommands. Co-authored by David Cramer and Claude Opus 4.6, this eliminates the biggest friction point for stdio users on Sentry Cloud.

**Replay tools expanded.** A new [`get_replay_details`](https://github.com/getsentry/sentry-mcp/commit/) tool (April 3) provides comprehensive replay inspection with session facts, activity timelines, and related issue recommendations. Replay summaries now surface directly in `get_issue_details` (April 8), and replay lookups route correctly through org regions.

**Profile support added.** `get_profile_details` (March 26) fetches raw profile chunk data with improved formatting for Java/Android frames. V0.32.0 expanded profile and replay support into existing event search tools (April 16), and split V1/V2 profile sample schemas to fix parsing errors (April 17).

**Tracemetrics dataset support (April 15).** Span metrics are now queryable through the event search tools via the tracemetrics dataset, enabling raw metric aggregate expressions.

**OAuth hardening continued.** Scoped MCP resources preserved through OAuth flow with RFC 8707 resource parameter support (April 14). Stale OAuth grants missing refresh tokens are now detected and revoked (April 6). The upstream token refresh logic was simplified by removing ~450 lines of distributed KV lock code (March 23), and OAuth failure diagnostics now classify expected user denials vs. unexpected errors (April 10).

**Schema resilience.** Relaxed upstream response schemas across OAuth, replay, release, and flamegraph parsers to match actual Sentry API behavior (April 13). Nullable `firstSeen`/`lastSeen` fields now accepted on issues (April 17). User geo data now included in formatted event output (April 12).

**Issue management improvements.** `update_issue` ignore operations now align with Sentry's schema — explicit modes for forever, duration, occurrence count, and user count (April 15). Azure OpenAI separated into dedicated provider for predictable routing (April 14).

**Multi-agent AI observability.** Sentry published a [blog series on debugging multi-agent AI systems](https://blog.sentry.io/debugging-multi-agent-ai-when-the-failure-is-in-the-space-between-agents/) (April 2026), positioning the platform for tracing across agent boundaries. Alongside posts on AI trace sampling and agent monitoring, Sentry is building toward being the observability layer for AI-native applications — the MCP server is the natural interface for that.

**AI-native development continues.** Commits are co-authored by Claude Opus 4.6, OpenAI Codex, GPT-5 Codex, and Devin AI — the Sentry team continues dogfooding AI-assisted development extensively.

**Stars grew from 603 to 645** (+7%), forks from 93 to 103 (+11%), total commits reached 963. Open issues at 61 (up from 57), with 158 total closed — the team continues closing faster than new issues arrive.

## What's Good

**OAuth 2.0 is the right auth model.** Most MCP servers we've reviewed require long-lived API tokens stored in plaintext JSON config files. Sentry's remote server uses OAuth — you authenticate in your browser, the token is scoped and revocable, and nothing sensitive sits on disk. This is how MCP auth *should* work, and Sentry is one of the first to get it right.

**Zero-install remote hosting removes all friction.** No `npx`, no `pip install`, no Docker. Point your client at the URL, authenticate, use it. For a tool that developers will set up once and use daily, this is significant.

**Seer AI integration is a genuine differentiator.** Most error tracking MCP servers (including community alternatives) just expose CRUD operations on issues and events. Sentry's server can invoke their proprietary AI for root cause analysis and fix suggestions. When you're debugging a production error at 2am, having the server not just *show* you the stack trace but *explain* what went wrong is real value.

**The tool coverage is comprehensive.** ~20 tools covering organizations, projects, issues, events, replays, and project management. You can go from "something broke" to "here's the issue, here are the events, here's the root cause analysis" without leaving your editor.

**First-party maintenance matters.** This isn't a community wrapper that might be abandoned. It's built by the Sentry team, shipped as `@sentry/mcp-server`, and actively maintained. When Sentry adds features, the MCP server gets them.

## What's Not

**61 open GitHub issues — growing slightly, though triage is active.** The issue count ticked up from 57 to 61, while 158 total have been closed. Remaining pain points include:
- Feature requests for Seer AI code review via MCP ([#900](https://github.com/getsentry/sentry-mcp/issues/900)) and dashboard management ([#876](https://github.com/getsentry/sentry-mcp/issues/876))
- HTTP allowlist for self-hosted instances in isolated networks ([#891](https://github.com/getsentry/sentry-mcp/issues/891))
- `assigned_or_suggested` filter unavailable via natural language search ([#889](https://github.com/getsentry/sentry-mcp/issues/889))
- API communication errors where the connection works but queries fail ([#748](https://github.com/getsentry/sentry-mcp/issues/748))
- Cross-project queries return 400 errors — you must select a specific project, limiting broad investigation

**AI search requires a separate LLM provider key.** The natural language search tools — one of the server's selling points — need an OpenAI or Anthropic API key configured separately from your Sentry auth. This means additional cost, additional configuration, and a dependency on a third-party LLM service on top of Sentry itself. The non-AI tools work without it, but losing search is a significant capability gap.

**Still pre-1.0 (v0.32.0).** The version number signals ongoing development and potential breaking changes. For a tool that developers will integrate into their daily workflow, version instability is a real concern. The rapid iteration (32 versions and counting) means the API surface is still evolving, though the `get_sentry_resource` tool promotion and legacy tool hiding in v0.31.0 suggest the team is consolidating toward a stable surface.

**63 npm dependencies.** For comparison, the Filesystem MCP server has ~10 dependencies. A large dependency tree means more surface area for supply chain issues and slower `npx` cold starts.

**Cross-project investigation is limited.** If you're debugging an issue that spans multiple services (common in microservice architectures), you can't query across projects in a single call. You need to know which project to look in first, which defeats the purpose of having an AI agent help you investigate.

**Seer may not be available everywhere.** The AI analysis features are tied to Sentry's proprietary Seer service. Self-hosted Sentry instances may not have access to Seer, reducing the server to a data retrieval tool without the analysis capabilities that justify the integration.

## Alternatives

**Community Sentry MCP servers:** [MCP-100/mcp-sentry](https://github.com/MCP-100/mcp-sentry) and [ddfourtwo/sentry-selfhosted-mcp](https://github.com/ddfourtwo/sentry-selfhosted-mcp) exist as lightweight alternatives. Neither has Seer integration or OAuth support — they're basic API wrappers. Sentry's own [sentry-mcp-stdio](https://github.com/getsentry/sentry-mcp-stdio) repo is now explicitly deprecated in favor of the remote server ("exists for educational purposes" per the README). The official remote server is the clear choice if you're on Sentry Cloud.

**Datadog MCP Server:** Datadog's official MCP server covers APM, infrastructure, logs, and RUM — a broader observability surface than Sentry's error-focused approach. If you're already on Datadog for full-stack observability, their MCP server is the natural choice. If you're specifically focused on error tracking and debugging, Sentry's server is deeper in that niche.

**PagerDuty MCP Server:** Focused on incident management rather than debugging — acknowledging alerts, escalating issues, coordinating response. Complements Sentry rather than replacing it.

**Grafana MCP:** Dashboard visualization and metrics/traces/logs queries. A different layer of the observability stack. You might use Grafana MCP for monitoring dashboards and Sentry MCP for drilling into specific errors.

**Honeycomb MCP:** Event-based observability with natural language querying. Similar AI-powered query translation, different observability paradigm.

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
- You need a stable, production-grade integration — v0.32.0 is maturing but still pre-1.0

{{< verdict rating="4" summary="First-party quality keeps improving — Device Code Flow, replays, and profiles at v0.32" >}}
The Sentry MCP server remains the best example we've reviewed of how a first-party MCP integration should work. The v0.31.0–v0.32.0 releases extend its lead: Device Code Flow authentication eliminates the last manual token friction for stdio users, replay and profile tools expand the debugging surface beyond error investigation, and tracemetrics support opens span-level performance analysis. The OAuth story keeps getting cleaner — stale grants are auto-revoked, scoped resources survive auth flows, and ~450 lines of refresh lock complexity were removed. The 4/5 rating holds because the fundamentals haven't changed — cross-project investigation is still limited, AI search still requires a separate LLM key, and 61 open issues show there's work left. But at 645 stars, 963 commits, and active AI-assisted development (Claude, Codex, Devin), the project is shipping faster than most first-party MCP servers. Sentry's push into multi-agent observability signals that the MCP server will become the debugging interface for AI-native applications, not just traditional error tracking.
{{< /verdict >}}

*Note: We research MCP servers using public documentation, GitHub repositories, npm registries, community discussions, and official changelogs. We do not test MCP servers hands-on or connect them to live services.*

**Category**: [Observability & Monitoring](/categories/observability-monitoring/)

*This review was last updated on 2026-04-19 using Claude Opus 4.6 (Anthropic).*


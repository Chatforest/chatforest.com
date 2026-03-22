---
title: "The Sentry MCP Server — Debug Production Errors Without Leaving Your Editor"
date: 2026-03-14T02:14:39+09:00
description: "Sentry's official MCP server brings error tracking, issue investigation, and AI-powered root cause analysis directly into your coding agent. 603 GitHub stars, ~19.4K weekly npm downloads, ~302K all-time PulseMCP visitors, and v0.30.0 with security hardening and performance gains. Here's the honest review."
og_description: "Sentry's official MCP server lets AI agents investigate production errors with OAuth auth and AI-powered analysis. 603 stars, 19.4K npm weekly, v0.30.0 with parallelized API calls and security fixes. Rating: 4/5."
content_type: "Review"
card_description: "Sentry's first-party MCP server for AI-assisted debugging. 603 stars, ~19.4K npm weekly downloads, ~302K PulseMCP visitors. OAuth authentication, ~20 tools, Seer AI integration, and v0.30.0 with performance and security improvements."
last_refreshed: 2026-03-14
---

The Sentry MCP server is Sentry's official tool for connecting AI coding agents to your error tracking data. Instead of switching to the Sentry dashboard, copying stack traces, and pasting them back into your editor, your agent can pull issue details, search events, and even invoke Sentry's AI (Seer) for root cause analysis — all from your IDE.

It's first-party. Sentry builds and maintains it at [getsentry/sentry-mcp](https://github.com/getsentry/sentry-mcp). With 603 GitHub stars, 93 forks, ~19,400 weekly npm downloads, and ~302K all-time PulseMCP visitors (#113 globally), it has real and growing adoption. And the killer feature: a hosted remote server at `mcp.sentry.dev` with OAuth 2.0 authentication, so there's nothing to install and no long-lived API tokens on disk.

**At a glance:** 603 stars / 93 forks / ~19.4K npm weekly downloads / v0.30.0 (March 18, 2026) / ~20 tools / 41+ contributors / ~302K all-time PulseMCP visitors (#113 globally, ~8.3K weekly)

This is the first observability tool we've reviewed, and it sets a high bar for what "first-party MCP server" should look like. At v0.30.0, the team is shipping fast — and the recent focus on security hardening and performance shows maturation.

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

**Project Management & Replays**
- `create_project` — create a new project and retrieve its DSNs
- `get_client_keys` — retrieve client keys for a project
- `list_replays` — list session replays from an organization

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

The stdio transport requires generating a User Auth Token from your Sentry settings. This is the path for self-hosted Sentry instances that can't use the hosted MCP endpoint.

## What's New (March 2026 Update)

Since our initial review, the Sentry MCP server has shipped v0.30.0 (March 18, 2026) with a focus on security, performance, and OAuth compliance. Key developments:

**Performance: Parallelized API calls in `get_issue_details`.** The core debugging tool previously made 4 sequential HTTP requests to assemble issue data. A [February 25 optimization](https://github.com/getsentry/sentry-mcp/commit/) reduced this to 2-3 parallel requests, meaningfully speeding up the most-used tool in the server.

**Security hardening across multiple vectors.** The team shipped fixes for a JSON injection vulnerability in logging (February 18), OAuth URI scheme sanitization with an HTTP/HTTPS allowlist (March 17), improved CORS handling on OAuth endpoints with reflected-origin stripping (February 27), and hardened OAuth refresh token locking to prevent race conditions under concurrent refreshes (March 3).

**OAuth aligned with RFC 9728.** Protected resource metadata now conforms to the RFC 9728 specification for discovery and authorization consistency (March 14-15). The Cloudflare Workers OAuth provider was also upgraded to v0.3.0.

**Cloudflare deployment improvements.** Per-user MCP rate limiting (March 13) separates IP-based and authenticated-user rate limit bindings. Response and rate-limit metrics were added (March 19) for better operational visibility.

**Seer auto-triggering removed.** Previously, the server could implicitly auto-trigger Seer analysis via output steering. This was [removed on March 2](https://github.com/getsentry/sentry-mcp/commit/) to give users explicit control over when AI analysis runs — a welcome change for cost and latency management.

**Better LLM compatibility.** Fixes landed for handling Anthropic JSON responses wrapped in markdown (March 16), removing an unsupported `temperature` parameter for GPT-5 (February 24), and tolerating malformed event tags in issue details (March 4).

**Claude Code plugin support.** The server can now be installed as a Claude Code plugin for automatic subagent delegation — when you ask Claude Code about Sentry errors, it automatically routes to a sentry-mcp subagent.

**AI-native development.** Multiple recent commits are co-authored by AI coding agents (Claude, Codex, GPT-5 Codex, Cursor) — the Sentry team is dogfooding AI-assisted development on their own AI integration tool.

**Stars grew from 579 to 603** (+4.1%), npm weekly downloads from ~17,800 to ~19,400 (+9%), and the contributor count reached 41+.

## What's Good

**OAuth 2.0 is the right auth model.** Most MCP servers we've reviewed require long-lived API tokens stored in plaintext JSON config files. Sentry's remote server uses OAuth — you authenticate in your browser, the token is scoped and revocable, and nothing sensitive sits on disk. This is how MCP auth *should* work, and Sentry is one of the first to get it right.

**Zero-install remote hosting removes all friction.** No `npx`, no `pip install`, no Docker. Point your client at the URL, authenticate, use it. For a tool that developers will set up once and use daily, this is significant.

**Seer AI integration is a genuine differentiator.** Most error tracking MCP servers (including community alternatives) just expose CRUD operations on issues and events. Sentry's server can invoke their proprietary AI for root cause analysis and fix suggestions. When you're debugging a production error at 2am, having the server not just *show* you the stack trace but *explain* what went wrong is real value.

**The tool coverage is comprehensive.** ~20 tools covering organizations, projects, issues, events, replays, and project management. You can go from "something broke" to "here's the issue, here are the events, here's the root cause analysis" without leaving your editor.

**First-party maintenance matters.** This isn't a community wrapper that might be abandoned. It's built by the Sentry team, shipped as `@sentry/mcp-server`, and actively maintained. When Sentry adds features, the MCP server gets them.

## What's Not

**57 open GitHub issues (down from a higher total) show active triage, but friction remains.** The team has been closing issues aggressively — only 57 are currently open — but the remaining pain points are real:
- API communication errors where the connection works but queries fail ([#748](https://github.com/getsentry/sentry-mcp/issues/748))
- Invalid token errors during authentication ([#340](https://github.com/getsentry/sentry-mcp/issues/340))
- Cross-project queries return 400 errors — you must select a specific project, limiting broad investigation
- Compatibility issues with Gemini Code Assist ([#617](https://github.com/getsentry/sentry-mcp/issues/617))
- `search_events` failures on certain query types ([#553](https://github.com/getsentry/sentry-mcp/issues/553))

**AI search requires a separate LLM provider key.** The natural language search tools — one of the server's selling points — need an OpenAI or Anthropic API key configured separately from your Sentry auth. This means additional cost, additional configuration, and a dependency on a third-party LLM service on top of Sentry itself. The non-AI tools work without it, but losing search is a significant capability gap.

**Still pre-1.0 (v0.30.0).** The version number signals ongoing development and potential breaking changes. For a tool that developers will integrate into their daily workflow, version instability is a real concern. The rapid iteration (30 versions and counting) means the API surface is still evolving, though the recent focus on security and compliance over new features suggests stabilization.

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
- You need a stable, production-grade integration — v0.30.0 is maturing but still pre-1.0

{{< verdict rating="4" summary="First-party quality for Sentry users, now with security hardening and faster API calls at v0.30" >}}
The Sentry MCP server remains the best example we've reviewed of how a first-party MCP integration should work. OAuth 2.0 authentication, zero-install remote hosting, comprehensive tool coverage, and proprietary AI integration (Seer) set it apart from community alternatives and most official MCP servers. The v0.30.0 release shows the project maturing: parallelized API calls speed up the core `get_issue_details` tool, security hardening addresses JSON injection and OAuth vulnerabilities, and RFC 9728 compliance moves the auth story forward. The 4/5 rating holds because the fundamentals haven't changed — cross-project investigation is still limited, AI search still requires a separate LLM key, and 57 open issues show there's work left. But the trajectory is clearly upward: 603 stars, 41+ contributors (including AI co-authors), and a team that's closing issues faster than they open. The OAuth + remote hosting pattern is still something every MCP server should copy.
{{< /verdict >}}

*Note: We research MCP servers using public documentation, GitHub repositories, npm registries, community discussions, and official changelogs. We do not test MCP servers hands-on or connect them to live services.*

*This review was last updated on 2026-03-21 using Claude Opus 4.6 (Anthropic).*

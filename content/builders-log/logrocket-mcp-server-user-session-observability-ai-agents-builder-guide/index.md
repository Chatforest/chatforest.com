---
title: "LogRocket MCP Server: User Session Observability for AI Agents (Builder Guide)"
date: 2026-06-16
description: "LogRocket's MCP Server connects AI agents to real user session data, error signals, and product analytics via Galileo AI. Here is what builders need to know to wire Claude or any agent into frontend observability."
og_description: "LogRocket launched an MCP Server in June 2026 that gives AI agents direct access to user sessions, error data, and product analytics. Builders can build issue-resolution agents, product research agents, and customer support agents grounded in what real users actually experience."
content_type: "Builder's Log"
categories: ["MCP", "Observability", "Frontend", "AI Agents"]
tags: ["logrocket", "mcp", "observability", "session-replay", "galileo-ai", "user-experience", "claude", "claude-code", "cursor", "frontend-monitoring", "issue-detection", "builder-guide"]
---

Most AI agents are built with a specific blindspot: they know about code, about APIs, about infrastructure — but they do not know what users are actually experiencing in your product right now.

LogRocket's **Galileo AI** has spent years watching session replays, correlating error rates with user behavior, and surfacing friction in web and mobile products. On June 9, 2026, LogRocket launched an **MCP Server** that puts that observability layer directly in front of AI agents. Your coding agent, support agent, or product research agent can now query what real users are doing, where they are failing, and what is breaking — before you even open a ticket.

---

## The Problem: Agents That Cannot See Users

When an agent helps you debug a production issue, it has access to your codebase, your error logs, maybe your Datadog metrics. What it typically lacks is *behavioral context*: the session replay that shows the exact click sequence before an error, the support ticket that confirms five other users hit the same wall, the A/B test result that shows your new checkout flow is losing conversions.

LogRocket calls this the "blindfold." The MCP Server removes it.

---

## What Galileo AI Does Behind the MCP

The LogRocket MCP is not a raw database query layer. Queries route through **Galileo AI**, LogRocket's analysis engine, which:

- **Watches session replays** to identify friction patterns within user journeys
- **Ingests customer calls** from Zoom and Gong to capture user sentiment at scale
- **Reads support tickets** from Zendesk and Intercom to surface recurring issue themes
- **Tracks product changes** in GitHub, Linear, and Jira, then measures their downstream effect on user behavior
- **Analyzes A/B tests** from Optimizely, Qualtrics, and similar platforms against real session outcomes

When your agent asks "what are users struggling with in the checkout flow?", Galileo synthesizes across all of these signals and returns a grounded answer — not a guess from training data.

---

## Tools Available in the MCP Server

### Default Toolset

Three tools are available out of the box:

| Tool | Description |
|---|---|
| `list_organizations` | Lists all LogRocket organizations accessible to the authenticated user. Hidden when connecting with an org-scoped URL. |
| `list_projects` | Lists projects within an organization. Hidden when connecting with a project-scoped URL. |
| `use_logrocket` | Core natural language query tool. Sends prompts directly to Ask Galileo against your session and analytics data. |

`use_logrocket` is the primary tool most agents will call. It accepts natural language queries and returns synthesized answers grounded in your LogRocket data.

### Optional Toolsets

Builders can enable additional toolsets by appending a `?toolsets=` parameter to the connection URL:

| Toolset | Tools Enabled | Use When |
|---|---|---|
| `ask-galileo` | `use_logrocket` | Default; natural language only |
| `sessions` | `find_sessions`, `watch_sessions` | Direct session filtering and analysis |
| `metrics` | `build_metric` | Querying product analytics data |
| `all` | Everything | Full access for power workflows |

**`find_sessions`** accepts structured filters to locate specific sessions (user ID, time range, error type, URL path). **`watch_sessions`** runs behavioral analysis across a set of sessions. **`build_metric`** constructs analytics queries against LogRocket's product metrics layer.

---

## Connecting to the MCP Server

The LogRocket MCP is a hosted server — no local installation required. LogRocket handles the infrastructure.

### Connection URLs

```
# Full access (choose org and project at query time)
https://mcp.logrocket.com/mcp

# Org-scoped (skips organization selection)
https://mcp.logrocket.com/mcp/<organization_id>

# Project-scoped (fastest; skips both org and project selection)
https://mcp.logrocket.com/mcp/<organization_id>/<project_id>
```

For production agent workflows, use the project-scoped URL. It eliminates disambiguation overhead and narrows the data surface to the project your agent should be operating on.

### Authentication

**OAuth (recommended):** Most MCP clients will prompt for OAuth authentication after connecting. This grants access equivalent to your browser login — scoped to your organization's permissions.

**API key:** For programmatic or headless use, create an API key in the LogRocket dashboard settings and pass it as:

```
Authorization: Bearer <your-api-key>
```

API keys are project-scoped. One key per project gives you clean separation if you are operating across multiple products.

---

## Compatible Clients

The LogRocket MCP works with any client that supports the Model Context Protocol:

- **Claude Code** — wire it in for debugging workflows alongside your codebase
- **Claude Desktop** — conversational product research sessions
- **Cursor** — inline issue investigation while you code
- **VS Code** (with Copilot or other MCP-aware extensions)
- **Codex** and other MCP-compatible runtimes

---

## Builder Patterns

### Pattern 1: Issue Resolution Agent

The most direct use case. An agent monitors LogRocket for new error clusters, uses `use_logrocket` to understand the scope and user impact, then routes a fix to a coding agent (Claude Code, Cursor, Codex) with full session context attached.

**Rippling** is using this pattern in production: near-real-time issue identification with agent-driven routing.

**ShipStation Global** extended it: coding agents receive the session context and automatically generate pull requests, so the fix is proposed before a human even opens the ticket.

### Pattern 2: Product Research Agent

Connect the MCP to an agent that can also read your codebase and product specs. Ask it: "How are users actually using the new dashboard we shipped last week?" Galileo synthesizes session behavior, support tickets, and A/B data into a grounded answer — saving a PM a week of manual review.

### Pattern 3: Customer Support Agent

A support agent with access to LogRocket can pull the session replay for any user ID before responding to a ticket. Instead of asking the user to reproduce the issue, the agent already knows what happened: the exact click sequence, the error that fired, the network request that failed.

### Pattern 4: Pre-Deploy Regression Check

After a PR is merged, trigger an agent to query LogRocket for session anomalies in the affected user flows. If error rates spike or conversion drops in the related segment, the agent flags it before the on-call engineer notices.

---

## Integration with Backend Observability

LogRocket is a frontend observability tool. Users experience failures in the UI; root causes often live in the backend. For full-stack issue resolution, pair the LogRocket MCP with a backend observability MCP:

- **Datadog MCP Server** (launched March 9, 2026): infrastructure metrics, APM traces, log queries
- **New Relic, Dynatrace, Honeycomb**: check each for MCP server availability

An agent that can query both LogRocket (what the user experienced) and Datadog (what the server did) can correlate frontend symptoms with backend root causes without manual pivot-and-search.

---

## Availability and Access

- **Live as of June 9, 2026**
- Available to **existing LogRocket customers** — no separate SKU or waitlist mentioned at launch
- Connection URL: `mcp.logrocket.com/mcp`
- Docs: `docs.logrocket.com/docs/mcp`

LogRocket explicitly notes that MCP server tools are under active development and subject to change. Pin your tool references carefully and build with the expectation that the schema will evolve.

---

## What This Does Not Cover

**No raw session video.** The MCP returns Galileo's synthesized analysis, not the raw session replay file. You cannot stream video to an agent — you get structured insights.

**No write operations.** The LogRocket MCP is read-only. Agents can query and analyze but cannot modify sessions, create alerts, or configure LogRocket settings via MCP.

**Requires LogRocket subscription.** This is not a free observability layer. LogRocket is a paid product. If you are not already using it, evaluate whether your current error tracking and session tooling justifies the switch.

**API key scope is per-project.** For multi-product organizations, you will need separate API keys or OAuth sessions per project. Plan your credential management accordingly.

---

## Builder Checklist

- [ ] Confirm you have an active LogRocket account with Galileo AI enabled
- [ ] Identify which project to connect to; grab your `organization_id` and `project_id`
- [ ] Choose your connection URL: project-scoped is usually right for production
- [ ] Decide on auth: OAuth for interactive sessions, API key for headless agents
- [ ] Add `?toolsets=sessions,metrics` if your workflow needs structured session filtering or metric queries
- [ ] Test `use_logrocket` with a natural language question against a real user flow you know well — validate the quality of Galileo's synthesis
- [ ] If pairing with Datadog MCP, define the handoff point: LogRocket surfaces the user-facing symptom, Datadog supplies the server-side root cause
- [ ] Build session context retrieval into your support agent before it touches a ticket
- [ ] Set up a post-deploy monitoring workflow using `find_sessions` filtered to affected user segments
- [ ] Watch LogRocket's changelog — the MCP toolset is actively expanding

---

The LogRocket MCP Server closes a genuine gap in how AI agents understand production software: not just whether the server is healthy, but whether users are succeeding. For teams already invested in LogRocket, it is a direct path to grounding your agents in real user experience data rather than synthetic assumptions.

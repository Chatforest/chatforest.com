---
title: "X Launched a Hosted MCP Server Yesterday. Here's What Builders Get."
date: 2026-07-01
description: "On June 30, 2026, X launched a hosted MCP server at api.x.com/mcp, auto-generated from its OpenAPI spec. Any MCP-compatible AI client can now read timelines, search posts, look up users, and manage bookmarks and Articles — with no self-hosting required."
og_description: "X's hosted MCP server (OAuth via xurl, pay-per-use pricing) went live June 30. What it is, what it unlocks, and what builders need to watch."
tags: ["mcp", "x", "twitter", "social-data", "agents", "real-time", "api", "tools", "builders-log", "july-2026"]
sources_audited: 2026-07-31
---

Yesterday, X [shipped a hosted Model Context Protocol server](https://devcommunity.x.com/t/announcing-the-hosted-x-mcp/269558) at `https://api.x.com/mcp` ([confirmed independently by TechCrunch](https://techcrunch.com/2026/06/30/x-now-offers-an-mcp-server-to-make-its-platform-easier-for-ai-tools-to-use/)). Previously, connecting an agent to X data meant self-hosting [X's open-source `xmcp` reference server](https://github.com/xdevplatform/xmcp) yourself; this is the first time X has run the MCP endpoint for developers.

Any MCP-compatible client — [Grok Build, Cursor, Claude, VS Code, and others](https://docs.x.com/tools/mcp) — can now connect to the X API through a standard MCP endpoint using the user's own account permissions. No cloning a GitHub repo, no managing OAuth plumbing, no maintaining local infrastructure.

## What the Server Exposes

X [launched two MCP servers simultaneously](https://docs.x.com/tools/mcp):

**Primary server** (`api.x.com/mcp`) — tools auto-generated from X's OpenAPI spec. X has not published an exact tool count for the hosted server; its [open-source self-hosted reference implementation](https://github.com/xdevplatform/xmcp/blob/master/README.md) currently documents 119 individual tool calls, not the "200+" figure that circulated in early third-party coverage of the launch. Per [X's own announcement](https://devcommunity.x.com/t/announcing-the-hosted-x-mcp/269558), what models can do with your account's scopes:

- Fetch posts, their likers/reposters/quoters, and recent post counts
- Full-archive post search, user search, and news search
- Look up users by ID or handle, plus their posts, timeline, and mentions
- List, add, remove, and manage bookmark folders
- News stories and trends by location
- Create Article drafts and publish them

Note what's *not* on that list: creating or deleting ordinary posts. X [told TechCrunch](https://techcrunch.com/2026/06/30/x-now-offers-an-mcp-server-to-make-its-platform-easier-for-ai-tools-to-use/) "the MCP tool is not compatible with X's Write API endpoints, so it's not possible to use it to post autonomously (or at all) on X" — matching the official capability list above, where "Posts" only covers reads. Bookmarks and Articles are the exceptions where the hosted server does write.

Streaming and webhook endpoints are [excluded by design](https://github.com/xdevplatform/xmcp/blob/master/README.md): real-time stream subscriptions remain outside MCP scope.

**Docs server** — A second MCP server ([`docs.x.com/mcp`](https://docs.x.com/tools/mcp)) exposing X's developer documentation as a queryable tool source, with `search_x` and `get_page_x` tools. Agents can reference API specs and integration guides programmatically during build workflows, without fetching from the web.

## How Authentication Works

X solved the OAuth problem with a small open-source bridge called [`xurl`](https://github.com/xdevplatform/xurl), "[the official CLI for the X API](https://github.com/xdevplatform/xurl)." The flow, per [`xurl`'s documented MCP bridge](https://github.com/xdevplatform/xurl/blob/main/README.md):

1. Register an X developer app once (standard app creation in the X Developer Portal)
2. Configure `xurl mcp` as the local bridge — it performs a one-time OAuth 2.0 login and caches/auto-refreshes the token
3. `xurl` relays each MCP message to `https://api.x.com/mcp` with a fresh `Authorization: Bearer <token>` header on every call, eliminating token management in the agent

The actual MCP server is hosted — `xurl` only handles token injection locally. That means there is no local MCP server process to start or manage; `xurl` is a thin credential bridge, not a server.

For developers who want full control, [X also publishes a separate self-hosted server](https://github.com/xdevplatform/xmcp) that wraps the same OpenAPI spec. Per its README, [it supports configuration via environment variables (`MCP_HOST`, `MCP_PORT`, `X_API_TOOL_ALLOWLIST`, and others), starts at `http://127.0.0.1:8000/mcp` by default, and is configurable on host and port](https://github.com/xdevplatform/xmcp/blob/master/README.md).

## Pricing

X runs [pay-per-use API pricing](https://docs.x.com/x-api/getting-started/pricing), and the hosted MCP routes through the same billing:

| Operation | Cost |
|---|---|
| Read a post | [$0.005](https://docs.x.com/x-api/getting-started/pricing) |
| User lookup | [$0.010](https://docs.x.com/x-api/getting-started/pricing) |

There is no minimum subscription or fixed monthly tier — [X's pricing page states "no contracts, subscriptions, or minimum spend"](https://docs.x.com/x-api/getting-started/pricing), though reads are [hard-capped at 2 million posts per monthly billing cycle](https://docs.x.com/x-api/getting-started/pricing) before Enterprise pricing applies. Agent costs scale directly with call volume: an agent that reads 100 posts per run costs roughly $0.50 per run.

X's pricing page also lists write rates (standard post creation is $0.015/request, $0.20 if the post contains a link), but those apply to the general API — they aren't reachable through the hosted MCP's documented capabilities, since ordinary post creation isn't one of the tools X lists for it (see above).

## Tool Allowlisting

By default the hosted server exposes every available tool. For most agent use cases that is too broad. X [provides an allowlist mechanism via the `X_API_TOOL_ALLOWLIST` environment variable](https://github.com/xdevplatform/xmcp/blob/master/README.md):

```
X_API_TOOL_ALLOWLIST="searchPostsRecent,getUsersByUsername,createUsersBookmark,getUsersBookmarks"
```

This is not optional for production agents. An agent with unrestricted tool access to an authenticated X account can read, publish Articles, and manage bookmarks — everything the connected account's OAuth scopes permit, even though ordinary post creation is out of scope for the hosted server (see above). Scope down to exactly what the agent needs before deploying.

## What This Unlocks

**Real-time social data in agents.** Until now, connecting an agent to live X data meant self-hosting an MCP server, managing OAuth, and handling rate limits independently. The hosted server reduces that to: authenticate once, point your MCP client at the endpoint.

**Monitoring and alerting agents.** An agent can watch for posts matching a search query, extract content, and trigger downstream actions — all through standard MCP tool calls. No X API client library required.

**Brand and competitive intelligence.** Agents can track mentions, monitor competitor accounts, and summarize engagement data. These were possible before through direct API calls; MCP makes them composable with other tools in an agentic workflow without custom glue code.

**Grok native advantage.** Grok is xAI's own LLM, and [xAI acquired X in an all-stock deal in March 2025](https://techcrunch.com/2025/03/29/elon-musk-says-xai-acquired-x/) that [valued xAI at $80 billion and X at $33 billion](https://www.cnbc.com/2025/03/28/elon-musk-says-xai-has-acquired-x-in-deal-that-values-social-media-site-at-33-billion.html). The hosted MCP gives Grok first-party access to X's data in a way that is structurally ahead of any third-party integration. Builders who are evaluating Grok as an agent backbone should weight this: Grok + X MCP is a native integration, not a bolt-on.

## What to Watch

**Rate limits under load.** X's [pricing page](https://docs.x.com/x-api/getting-started/pricing) documents a monthly cap (2 million post reads per billing cycle) but not fine-grained per-minute rate limits for the MCP tools themselves — that gap is a cost visibility risk for agents that run on a schedule or in response to events. Monitor spend closely in early deployments.

**Tool surface area.** A large set of [auto-generated tools from an OpenAPI spec](https://github.com/xdevplatform/xmcp/blob/master/README.md) means the tool list will change as X updates its API — the spec is [fetched fresh from `api.twitter.com/2/openapi.json` at server startup](https://github.com/xdevplatform/xmcp/blob/master/README.md). Tools may appear or disappear between versions. Pin to a specific OpenAPI spec version if your agent depends on tool stability.

**Account permissions scope.** The hosted MCP acts with the permissions of the connected X account. A compromised or misconfigured agent has write access to the associated account. Treat the OAuth credentials for any MCP-connected X app as high-value secrets.

**xurl dependency.** The hosted server relies on `xurl` for credential injection. [`xurl` is published and maintained by X itself](https://github.com/xdevplatform/xurl) under the `xdevplatform` GitHub org and is billed as "the official CLI for the X API" — but it is still a separate, independently versioned open-source project from the API itself, distributed via Homebrew/npm/Go install rather than bundled with the platform. Track its release history and maintenance status like any external dependency.

---

X's hosted MCP is a significant expansion of X's developer surface in 2026. It removes the biggest friction point for AI integrations — credential management and local server operation — and makes X data a first-class tool in any MCP-aware agent stack. The broad, auto-generated tool surface, combined with pay-per-use pricing, means the default posture should be aggressive allowlisting rather than open access.

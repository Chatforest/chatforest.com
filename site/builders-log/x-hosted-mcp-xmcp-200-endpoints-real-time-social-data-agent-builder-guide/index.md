# X Launched a Hosted MCP Server Yesterday. Here's What Builders Get.

> On June 30, 2026, X launched a hosted MCP server at api.x.com/mcp, exposing 200+ tools auto-generated from its OpenAPI spec. Any MCP-compatible AI client can now read timelines, search posts, post, look up users, and manage bookmarks — with no self-hosting required.


Yesterday, X shipped a hosted Model Context Protocol server at `https://api.x.com/mcp`. It is the first time X has offered MCP access to its platform without requiring developers to run their own server.

Any MCP-compatible client — Claude Desktop, Cursor, Windsurf, or a custom agent — can now connect to the X API through a standard MCP endpoint using the user's own account permissions. No cloning a GitHub repo, no managing OAuth plumbing, no maintaining local infrastructure.

## What the Server Exposes

X launched two MCP servers simultaneously:

**Primary server** (`api.x.com/mcp`) — 200+ tools auto-generated from X's OpenAPI spec. Coverage includes:

- Search posts (recent and archive)
- Read and fetch user timelines
- Create and delete posts
- Look up users by username or ID
- Manage likes, bookmarks, and lists
- Read and write X Articles (long-form content)

Streaming and webhook endpoints are excluded by design. The server gives agents read/write access to X's data API; real-time stream subscriptions remain outside MCP scope.

**Docs server** — A second MCP server exposing X's developer documentation as a queryable tool source. Agents can reference API specs and integration guides programmatically during build workflows, without fetching from the web.

## How Authentication Works

X solved the OAuth problem with a small open-source bridge called `xurl`. The flow:

1. Register an X developer app once (standard app creation in the X Developer Portal)
2. Configure `xurl` as the local bridge — it handles the OAuth 2.0 authorization code flow
3. `xurl` injects a fresh Bearer token on every MCP call, eliminating token management in the agent

The actual MCP server is hosted — `xurl` only handles token injection locally. That means there is no local MCP server process to start or manage; `xurl` is a thin credential bridge, not a server.

For developers who want full control, the underlying server is also open source at `github.com/xdevplatform/xmcp` and can be self-hosted. The self-hosted version supports configuration via environment variables, starts at `http://127.0.0.1:8000/mcp` by default, and is configurable on host and port.

## Pricing

X moved to pay-per-use API pricing in January 2026. The hosted MCP routes through the same billing:

| Operation | Cost |
|---|---|
| Read a post | ~$0.005 |
| Post / user lookup | ~$0.01 |

There is no minimum subscription or fixed monthly tier. Agent costs scale directly with call volume. An agent that reads 100 posts per run costs roughly $0.50 per run.

No separate pricing has been announced for the hosted MCP layer itself — X is treating it as a delivery mechanism for standard API calls, not a premium product.

## Tool Allowlisting

By default the hosted server exposes every available tool. For most agent use cases that is too broad. X provides an allowlist mechanism via the `X_API_TOOL_ALLOWLIST` environment variable:

```
X_API_TOOL_ALLOWLIST="searchPostsRecent,getUsersByUsername,createPosts,likePost"
```

This is not optional for production agents. An agent with unrestricted tool access to an authenticated X account can post, delete, and interact with any endpoint the account can reach. Scope down to exactly what the agent needs before deploying.

## What This Unlocks

**Real-time social data in agents.** Until now, connecting an agent to live X data meant self-hosting an MCP server, managing OAuth, and handling rate limits independently. The hosted server reduces that to: authenticate once, point your MCP client at the endpoint.

**Monitoring and alerting agents.** An agent can watch for posts matching a search query, extract content, and trigger downstream actions — all through standard MCP tool calls. No X API client library required.

**Brand and competitive intelligence.** Agents can track mentions, monitor competitor accounts, and summarize engagement data. These were possible before through direct API calls; MCP makes them composable with other tools in an agentic workflow without custom glue code.

**Grok native advantage.** Grok is xAI's own LLM. xAI owns X. The hosted MCP gives Grok first-party access to X's data in a way that is structurally ahead of any third-party integration. Builders who are evaluating Grok as an agent backbone should weight this: Grok + X MCP is a native integration, not a bolt-on.

## What to Watch

**Rate limits under load.** Pay-per-use pricing without rate limit documentation is a cost visibility risk for agents that run on a schedule or in response to events. Monitor spend closely in early deployments.

**Tool surface area.** 200+ auto-generated tools from an OpenAPI spec means the tool list will change as X updates its API. Tools may appear or disappear between versions. Pin to a specific OpenAPI spec version if your agent depends on tool stability.

**Account permissions scope.** The hosted MCP acts with the permissions of the connected X account. A compromised or misconfigured agent has write access to the associated account. Treat the OAuth credentials for any MCP-connected X app as high-value secrets.

**xurl dependency.** The hosted server relies on `xurl` for credential injection. It is open source but not part of the official X Developer platform in the same way the API itself is. Track its maintenance status.

---

X's hosted MCP is the most significant expansion of X's developer surface in 2026. It removes the biggest friction point for AI integrations — credential management and local server operation — and makes X data a first-class tool in any MCP-aware agent stack. The 200+ tool surface, combined with pay-per-use pricing, means the default posture should be aggressive allowlisting rather than open access.


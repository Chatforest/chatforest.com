# Gemini Managed Agents July 7 Update: Background Tasks, Remote MCP, and the Production-Ready Feature Set — Builder's Guide

> Six weeks after launch, Google added four capabilities that move Gemini Managed Agents from prototype-grade to production-viable: background execution, remote MCP server integration, custom function calling, and in-session credential refresh. Here's what each does and what it means for builders.


Google expanded Gemini Managed Agents on July 7, 2026, adding four features that fill the biggest gaps between the original May 19 launch and what production deployments actually require. This is a research-based summary; we reviewed [Google's July 7 blog post](https://blog.google/innovation-and-ai/technology/developers-tools/expanding-managed-agents-gemini-api/) and [third-party technical coverage](https://the-decoder.com/google-deepmind-adds-background-execution-and-mcp-support-to-gemini-api-managed-agents/), but did not build with these APIs ourselves.

**Context**: If you haven't read our [original Gemini Managed Agents guide](/builders-log/gemini-api-managed-agents-antigravity-sandbox-builder-guide/), the short version is: one call to the Interactions API spins up an isolated cloud Linux sandbox running the Antigravity agent on Gemini 3.5 Flash. The sandbox handles reasoning, code execution, web search, and file management. State persists across calls within a session.

The July 7 update adds four production-oriented capabilities on top of that foundation.

---

## What Changed: Four New Capabilities

| Feature | What it does | Why it matters |
|---|---|---|
| Background execution | `background: true` — API returns job ID immediately, task runs async | Long jobs don't need an open connection |
| Remote MCP integration | Agents connect to remote MCP servers from inside the sandbox | No tunneling, no custom proxy middleware |
| Custom function calling | Mix custom tools alongside built-in sandbox tools | App-specific actions without a full MCP server |
| Credential refresh | Pass new network config with existing `environment_id` | Rotate keys mid-session without losing filesystem state |

---

## Background Execution

The original Managed Agents API was synchronous: you sent a request, kept the connection open, and waited. For short tasks that's fine. For a research agent that browses 50 URLs, or a data pipeline that processes a large file, you're holding a connection open for minutes.

The July 7 update adds a `background: true` parameter. With it, the API returns a job ID immediately. The task runs asynchronously on Google's infrastructure. Client code can then:
- **Poll** the job ID to check status
- **Stream progress** when results become available
- **Reconnect later** — useful if the user closes a browser tab or your server restarts

This makes long-running agentic tasks practical. A user can trigger a multi-step research job, close the tab, and come back 20 minutes later to pick up results. The agent keeps running on Google's servers regardless.

**Practical implication**: Agents that previously hit client-side timeouts or required the user to babysit a browser tab can now run as backend jobs. This is close to the "fire and forget" model that production job queues use.

---

## Remote MCP Server Integration

This is the most architecturally significant addition.

The original Managed Agents ran with built-in tools (code execution, web search, URL fetch). Any custom tools required the developer to handle the gap between the sandbox and external systems, typically through custom middleware.

The July 7 update lets agents connect directly to remote MCP servers from inside the cloud sandbox. An agent can now reach:
- Documentation systems
- Issue trackers and project management tools
- Internal databases exposed via MCP
- Browser automation services
- Any MCP-compatible tool

No tunneling. No custom proxy. The agent and the MCP server talk directly.

**Why this matters for builders**: Remote MCP integration means you can extend Managed Agents with your own tooling using the same protocol you'd use with Claude Code, Cursor, or any other MCP-capable client. One MCP server definition, multiple consumers.

The alternative — custom function calling (see below) — works for simple, app-specific operations. For anything that benefits from the MCP ecosystem or that you're already maintaining as an MCP server, remote MCP is cleaner.

---

## Custom Function Calling

Not every integration belongs in an MCP server. App-specific operations — validate a customer entitlement, calculate a quote, open a pull request against a specific repo — are often too narrow to warrant a full MCP server, but still need to run client-side.

The custom function calling feature handles this with the `requires_action` pattern (similar to OpenAI's function calling). The flow:

1. Developer declares custom tools alongside built-in sandbox tools
2. When the agent decides to use a custom tool, the API returns `requires_action` with the function name and arguments
3. The client executes the function locally and returns the result
4. The agent incorporates the result and continues

Built-in tools (code execution, web search) run server-side automatically, without interrupting the synchronous flow. Custom functions pause and wait for the client.

**Combining with background execution**: If you use `background: true` with custom functions, polling the job status also surfaces `requires_action` events so the client knows when a function call is waiting.

---

## Credential Refresh

The fourth feature solves a lifecycle problem: API keys and network credentials expire. In the original design, expiring credentials meant abandoning the session and losing the sandbox's filesystem state — installed packages, cloned repos, intermediate results.

The July 7 update lets you refresh credentials by passing a new network configuration alongside the existing `environment_id`. The sandbox keeps its filesystem state; only the network credentials are replaced. The new rules take effect immediately.

This is primarily relevant for sessions that span multiple hours or that access systems with short-lived tokens (OAuth sessions, temporary cloud credentials). For most short-lived tasks, it won't come up.

---

## What This Means for Production Deployments

The original Managed Agents were useful for prototyping and demos: low barrier to entry, free during preview, built-in tools. The gaps were the ones that matter for production: no way to run long jobs asynchronously, no standard protocol for external tools, no lifecycle management for credentials.

The July 7 update closes three of those four gaps directly:
- **Background execution** → long-running jobs without open connections
- **Remote MCP** → external tools via standard protocol
- **Credential refresh** → lifecycle management for auth

What's still missing: Google hasn't published pricing for Managed Agents beyond "free during preview." For production deployments, cost per interaction and cost per background task-hour matter a lot. Until Google publishes that, Managed Agents has an evaluation ceiling: you can build and test, but committing to production scale requires a pricing conversation that hasn't happened publicly yet.

---

## Comparison to Alternatives

| Platform | Background tasks | Remote MCP | Custom tools | Pricing |
|---|---|---|---|---|
| Gemini Managed Agents | Yes (July 7) | Yes (July 7) | Yes (requires_action) | Preview only |
| Anthropic Managed Agents | Yes | Via MCP tunnels | Yes | Published |
| AWS AgentCore | Yes | Via connectors | Yes | Published |
| OpenAI Responses API | No (sync only) | No | Yes (function_call) | Published |

The Gemini offering is now technically competitive on the feature axis. Pricing and long-term availability commitments are the remaining unknowns for builders evaluating a platform bet.

---

## What to Do Now

If you built on the original Managed Agents and have long-running tasks: test `background: true` before your next deployment. The async model changes the UX significantly — users can leave and come back.

If you have existing MCP servers (for Claude Code, Cursor, or other clients): point a Managed Agent at them to test compatibility. The integration uses the same MCP protocol, so it should work without modifications — but testing in preview is the time to find edge cases.

If you're evaluating Managed Agents for production but waiting on pricing: that wait is still rational. The feature set is now strong; the commercial terms are not yet public.

*This is a research-based guide. ChatForest did not run code against these APIs. Technical details are drawn from [Google's July 7 blog post](https://blog.google/innovation-and-ai/technology/developers-tools/expanding-managed-agents-gemini-api/) and [The Decoder's coverage](https://the-decoder.com/google-deepmind-adds-background-execution-and-mcp-support-to-gemini-api-managed-agents/). Test against Google's official documentation before building.*


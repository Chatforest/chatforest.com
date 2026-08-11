---
title: "MCP Notifications Explained: List Changes, Resource Subscriptions, and Dynamic Discovery"
date: 2026-03-28T23:00:00+09:00
description: "A practical guide to MCP notifications — how servers signal tool, resource, and prompt changes to clients, how resource subscriptions work, and how to build reactive MCP integrations."
content_type: "Guide"
card_description: "MCP servers don't just respond to requests — they push notifications when tools change, resources update, or prompt lists shift. Here's how the notification system works."
last_refreshed: 2026-08-11
sources_audited: 2026-08-11
---

MCP is a request-response protocol built on JSON-RPC — but it's not *only* request-response. Servers can push **notifications** to clients without being asked. This is how MCP supports dynamic environments where tools appear and disappear, resources change underneath you, and prompt templates evolve at runtime.

Understanding notifications is essential for building MCP integrations that stay in sync with their servers. Without them, a client's view of available capabilities goes stale the moment something changes on the server side.

**Spec note:** MCP's [2026-07-28 revision](https://modelcontextprotocol.io/specification/2026-07-28/changelog) made substantial breaking changes to how notifications are set up — it removed the `initialize` handshake and the `resources/subscribe`/`resources/unsubscribe` methods, replacing them with a single `subscriptions/listen` opt-in stream. This guide describes the current (2026-07-28) mechanics; where the older, still widely-deployed `2025-11-25` behavior differs, we call it out.

Our analysis is based on the [MCP specification](https://modelcontextprotocol.io/specification/2026-07-28) and published SDK documentation — we research and analyze rather than building production MCP systems ourselves.

## How Notifications Work in MCP

Notifications in MCP follow the [JSON-RPC 2.0 notification pattern](https://www.jsonrpc.org/specification#notification): they're messages sent **without an `id` field**, which means the receiver doesn't send a response. They're fire-and-forget.

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/tools/list_changed"
}
```

No `id`. No response expected. The sender doesn't know if the receiver got it or acted on it.

This design keeps notifications lightweight — servers don't block waiting for acknowledgment, and clients process them when they can. But it also means notifications can be lost (especially over unreliable transports), so clients should treat them as hints rather than guarantees of delivery.

## The Three List Changed Notifications

MCP defines three parallel notification types, one for each of the three server primitives:

| Notification | Primitive | Capability Flag |
|---|---|---|
| `notifications/tools/list_changed` | Tools | `tools.listChanged` |
| `notifications/resources/list_changed` | Resources | `resources.listChanged` |
| `notifications/prompts/list_changed` | Prompts | `prompts.listChanged` |

These method names and capability-flag names are unchanged across the `2025-11-25` and `2026-07-28` spec revisions — see the [tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools#list-changed-notification), [resources](https://modelcontextprotocol.io/specification/2026-07-28/server/resources#list-changed-notification), and [prompts](https://modelcontextprotocol.io/specification/2026-07-28/server/prompts#list-changed-notification) spec pages. What changed is *how a client starts receiving them*:

1. **Server advertises the capability** — the `{"tools": {"listChanged": true}}`-style flag, now reported in the (optional) [`server/discover`](https://modelcontextprotocol.io/specification/2026-07-28/server/discover) response rather than a stateful `initialize` handshake.
2. **Client opts in** by opening a [`subscriptions/listen`](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/subscriptions) stream that requests that specific notification type.
3. **Server sends the notification** on that stream when its list changes.
4. **Client re-fetches the full list** by calling `tools/list`, `resources/list`, or `prompts/list`.

The notification itself carries no payload — it doesn't say *what* changed, just *that* something changed. The client must re-list to find out.

### Declaring and Subscribing to the Capability

Servers still advertise support for list-changed notifications with the same flags as before. Here's a `server/discover` response declaring all three, plus resource subscriptions:

```json
{
  "jsonrpc": "2.0",
  "id": "discover-1",
  "result": {
    "resultType": "complete",
    "capabilities": {
      "tools": { "listChanged": true },
      "resources": { "subscribe": true, "listChanged": true },
      "prompts": { "listChanged": true }
    }
  }
}
```

Declaring the capability is not enough on its own, though. A client only starts *receiving* the notifications after it opens a `subscriptions/listen` stream naming the types it wants:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "subscriptions/listen",
  "params": {
    "notifications": {
      "toolsListChanged": true,
      "promptsListChanged": true,
      "resourcesListChanged": true
    }
  }
}
```

The server acknowledges with `notifications/subscriptions/acknowledged` (echoing which types it actually agreed to honor) before any notification is sent on that stream. See the [Subscriptions pattern](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/subscriptions) for the full request/acknowledgment/cancellation mechanics.

**Prior to the 2026-07-28 revision**, this worked differently: servers declared `listChanged: true` once, during a stateful `initialize` handshake, and clients were expected to listen for the bare notification on the same connection — there was no separate opt-in request. If you're integrating with a server or client that still speaks protocol version `2025-11-25` or earlier, expect the handshake-based flow instead of `subscriptions/listen`.

### When Servers Send List Changed

Servers send list changed notifications whenever the set of available items changes. Common triggers:

**Tools:**
- A plugin system loads or unloads a module
- Feature flags enable or disable tools
- The server connects to or disconnects from a backend service
- An admin adds a new tool definition at runtime

**Resources:**
- New files appear in a watched directory
- A database table is created or dropped
- A connected service exposes new endpoints
- Access permissions change, making resources visible or hidden

**Prompts:**
- New prompt templates are deployed
- Templates are updated or retired
- User-specific prompts become available after authentication

### Client Handling Pattern

When a client receives a list changed notification, the standard pattern is:

```python
# Conceptual pattern — exact API depends on your SDK
@client.on_notification("notifications/tools/list_changed")
async def handle_tools_changed():
    # Re-fetch the complete tool list
    tools = await client.list_tools()
    # Update internal state
    update_available_tools(tools)
    # Optionally inform the AI model about new/removed tools
    refresh_model_context(tools)
```

The key insight: **always re-fetch the full list**. Don't try to guess what changed. The notification is just a signal to refresh.

## Resource Subscriptions

Resources have a second notification mechanism beyond list changes: **subscriptions**. While `list_changed` tells you the *set* of resources changed, subscriptions tell you a *specific resource's content* changed.

### How Subscriptions Work

As of the [2026-07-28 spec](https://modelcontextprotocol.io/specification/2026-07-28/server/resources#subscriptions), per-resource subscriptions go through the same `subscriptions/listen` stream as list-changed notifications — there's no longer a standalone `resources/subscribe` RPC.

1. **Client opens a listen stream**, naming the specific resource URI(s) it wants updates for:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "subscriptions/listen",
  "params": {
    "notifications": {
      "resourceSubscriptions": ["file:///config/settings.json"]
    }
  }
}
```

2. **Server acknowledges** with `notifications/subscriptions/acknowledged`, tagging the stream with a `subscriptionId`.

3. **When the resource changes**, the server sends, on that same stream:

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/resources/updated",
  "params": {
    "_meta": { "io.modelcontextprotocol/subscriptionId": 1 },
    "uri": "file:///config/settings.json"
  }
}
```

4. **Client re-reads** the resource to get the new content:

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "resources/read",
  "params": {
    "uri": "file:///config/settings.json"
  }
}
```

5. **Client unsubscribes** by closing the stream — on Streamable HTTP that means closing the SSE response stream; on stdio it means sending `notifications/cancelled` referencing the `subscriptions/listen` request ID. There is no separate `resources/unsubscribe` request anymore.

**Prior to 2026-07-28**, subscribing and unsubscribing were dedicated RPCs, `resources/subscribe` and `resources/unsubscribe`, each targeting one URI at a time, with updates delivered as bare `notifications/resources/updated` messages (no `subscriptionId`). Some deployed servers and SDKs still speak that version.

### Subscribe vs. List Changed

These two notification types serve different purposes:

| Aspect | `list_changed` | `subscribe` / `updated` |
|---|---|---|
| Scope | The entire list of resources | One specific resource |
| What changed | Items added or removed | Content of an existing resource |
| Client action | Re-fetch the list | Re-read the resource |
| Setup required | `subscriptions/listen` with `resourcesListChanged: true` | `subscriptions/listen` with `resourceSubscriptions: [uri, ...]` |
| Capability flag | `resources.listChanged` | `resources.subscribe` |

A server can support one, both, or neither. A file server might support subscriptions (to watch file content) but not list changes (if the file list is static). A database server might support list changes (tables can be created) and subscriptions (table contents change).

### Subscription Use Cases

Resource subscriptions are particularly valuable for:

- **Configuration files** — update model behavior when config changes
- **Log files** — stream new entries as they appear
- **Database records** — react to data changes without polling
- **API responses** — cache and refresh external data
- **Shared documents** — collaborative editing contexts

## Built-in Utility Notifications

Beyond the three primitives, MCP defines several utility notifications.

### Progress Notifications

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/progress",
  "params": {
    "progressToken": "abc-123",
    "progress": 50,
    "total": 100,
    "message": "Processing records..."
  }
}
```

Servers send these during long-running operations, referencing a `progressToken` the client supplied in the original request's `_meta` field. This mechanism is unchanged in the [2026-07-28 spec](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/progress). Progress notifications flow on the response stream of the request they relate to — not on a `subscriptions/listen` stream. They're covered in more detail in our [MCP Lifecycle and Utilities guide](/guides/mcp-lifecycle-and-utilities-explained/).

### Cancellation Notifications

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/cancelled",
  "params": {
    "requestId": "req-456",
    "reason": "User cancelled the operation"
  }
}
```

The 2026-07-28 spec narrowed this notification's role considerably compared to earlier versions. Per the current [cancellation spec](https://modelcontextprotocol.io/specification/2026-07-28/basic/utilities/cancellation):

- **Client-initiated cancellation is transport-dependent.** On Streamable HTTP, closing the SSE response stream *is* the cancellation signal — no `notifications/cancelled` message is sent or expected. On stdio, where there's no per-request stream to close, the client sends `notifications/cancelled` referencing the request ID.
- **Server-initiated `notifications/cancelled` is now restricted to one purpose**: tearing down a `subscriptions/listen` stream. The spec states servers "MUST NOT send `notifications/cancelled` for any other purpose."

Either way, cancellation is best-effort — the operation may have already completed by the time the signal arrives, and both sides must tolerate that race.

### Logging Notifications

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/message",
  "params": {
    "level": "warning",
    "logger": "db-connector",
    "data": "Connection pool exhausted, creating new connections"
  }
}
```

Servers push log messages to clients this way. As of 2026-07-28, verbosity is no longer set with a `logging/setLevel` RPC — that method was removed. Instead, clients set `io.modelcontextprotocol/logLevel` in the `_meta` of the specific request they want log messages for, and the server **MUST NOT** emit `notifications/message` for a request that didn't include it. The [Logging feature itself is now deprecated](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/logging) (marked deprecated, not yet removed, under MCP's 12-month deprecation policy); new implementations are steered toward logging to `stderr` on stdio or OpenTelemetry instead. These are detailed further in our [Lifecycle and Utilities guide](/guides/mcp-lifecycle-and-utilities-explained/).

### The Roots Notification Was Removed

Earlier spec versions (`2025-11-25` and before) defined a client-to-server `notifications/roots/list_changed` notification, sent when a user's workspace roots changed so servers could re-request `roots/list`. **The 2026-07-28 revision removed this notification entirely**, along with the standalone server-initiated `roots/list` request — roots are now requested as part of the [Multi Round-Trip Requests pattern](https://modelcontextprotocol.io/specification/2026-07-28/client/roots) instead. The Roots feature as a whole is [now deprecated](https://modelcontextprotocol.io/specification/2026-07-28/client/roots), with the spec recommending servers pass directories via tool parameters, resource URIs, or server configuration instead. If you're working against an older server that still expects `notifications/roots/list_changed`, that's `2025-11-25`-or-earlier behavior, not current spec.

## Dynamic Tool Discovery

One of the most practical applications of notifications is **dynamic tool discovery** — where a server's available tools change at runtime and the client automatically adapts.

### The Pattern

```
Client opens subscriptions/listen (toolsListChanged: true)
  ↓
Server starts → exposes tools A, B, C
  ↓
Client connects → lists tools → gets A, B, C
  ↓
Server loads plugin → now has tools A, B, C, D
  ↓
Server sends notifications/tools/list_changed on the listen stream
  ↓
Client re-lists tools → gets A, B, C, D
  ↓
AI model can now use tool D
```

### Why This Matters

Without dynamic discovery, adding a new tool means restarting the server and reconnecting the client. With it, servers can:

- **Load plugins on demand** — install a new capability without downtime
- **Respond to environment changes** — detect a new database and expose query tools
- **Manage tool access** — show different tools based on authentication state
- **A/B test tools** — roll out new tool versions to specific clients

### Client Support Reality

Not all MCP clients handle `notifications/tools/list_changed` well, and support has been a moving target even among Anthropic's own clients:

- **Claude Code** documents support for `list_changed` notifications: per [Anthropic's Claude Code MCP docs](https://code.claude.com/docs/en/mcp), "Claude Code supports MCP `list_changed` notifications, allowing MCP servers to dynamically update their available tools, prompts, and resources without requiring you to disconnect and reconnect." That same page notes a related fix — before v2.1.214, a transient refresh error could wipe a server's tools/prompts/resources to an empty list instead of keeping the last-known-good set.
- **Claude Desktop does not currently act on `notifications/tools/list_changed`.** A filed and since-closed bug ([anthropics/claude-code#50339](https://github.com/anthropics/claude-code/issues/50339)) found the desktop app parses the notification but never wires up a handler for it — tool lists are captured once, at connection time, and stay frozen until the app is restarted. The issue was closed "not planned."
- **Gemini CLI** used to lack this support; a filed [feature request](https://github.com/google-gemini/gemini-cli/issues/13850) was resolved by a [merged pull request](https://github.com/google-gemini/gemini-cli/pull/14375) (merged December 2025) that added a `notifications/tools/list_changed` handler and dynamic tool refresh.

If you're building a server that relies on dynamic tools, test with your target clients rather than assuming support — even "supports it" clients have had rough edges around timing (e.g., a tool registered mid-turn not being usable until the next turn).

## Common Patterns and Best Practices

### Debounce Rapid Changes

If your server makes many changes in quick succession (e.g., bulk-loading tools), don't send a notification for each one. Batch them:

```python
# Bad: floods the client with notifications
for tool in new_tools:
    register_tool(tool)
    send_notification("notifications/tools/list_changed")

# Good: one notification after all changes
for tool in new_tools:
    register_tool(tool)
send_notification("notifications/tools/list_changed")
```

### Don't Rely on Notification Delivery

Notifications have no acknowledgment. They can be lost due to:

- Transport errors (network glitches, dropped WebSocket frames)
- Client not listening (busy processing another request)
- Client doesn't support the notification type

Design your system to work even if notifications are occasionally missed. Clients should periodically re-list as a fallback. Servers should always return the current state when asked, regardless of what notifications were sent.

### Use List Changed for Discoverability

Even if your tools are mostly static, consider supporting `listChanged` to enable graceful degradation. A monitoring tool can expose different tools based on what backends are healthy — and notify the client when availability changes.

### Resource Subscriptions: Subscribe Sparingly

Subscribing to hundreds of resources creates overhead on the server side (tracking subscriptions, detecting changes, sending notifications). Subscribe to resources the AI model is actively using, and unsubscribe when done.

## The Complete Notification Reference

Current as of MCP spec version [2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/changelog):

| Method | Direction | Purpose |
|---|---|---|
| `notifications/tools/list_changed` | Server → Client | Tool list has changed |
| `notifications/resources/list_changed` | Server → Client | Resource list has changed |
| `notifications/resources/updated` | Server → Client | Subscribed resource content changed |
| `notifications/prompts/list_changed` | Server → Client | Prompt list has changed |
| `notifications/subscriptions/acknowledged` | Server → Client | Confirms a `subscriptions/listen` request and reports which notification types will actually be delivered |
| `notifications/progress` | Server → Client | Progress update for a long operation |
| `notifications/cancelled` | Client → Server (stdio) / Server → Client (subscription teardown only) | Request or subscription cancellation |
| `notifications/message` | Server → Client | Log message (deprecated feature) |

Two notifications from earlier spec versions no longer exist as of 2026-07-28: `notifications/roots/list_changed` (removed along with the standalone Roots RPCs) and `notifications/initialized` (removed along with the `initialize` handshake itself, since MCP is now stateless). See the [full changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog) for the complete list of breaking changes.

## Common Mistakes

**Assuming a `subscriptions/listen` acknowledgment grants everything you asked for.** The server's acknowledgment only reflects the subset of notification types it agreed to honor — types it doesn't support are silently omitted, not rejected with an error. Check the acknowledgment before assuming a subscription is live.

**Including payload in list changed notifications.** The spec defines these as empty notifications (no `params` needed). Don't try to include the changed items — clients will ignore extra data and re-list anyway.

**Not declaring the capability.** If a server sends `notifications/tools/list_changed` without having advertised `tools.listChanged: true`, well-behaved clients won't have opened a `subscriptions/listen` stream for it in the first place, so the notification has nowhere to go.

**Assuming subscriptions survive reconnection.** On stdio, if the transport drops and the client reconnects, the server holds no subscription state across reconnections — the client must re-send `subscriptions/listen` to re-establish anything it was watching.

**Conflating the two roles of `notifications/cancelled`.** As of 2026-07-28, a server sending this notification is only allowed to use it to tear down a `subscriptions/listen` stream — not to cancel an arbitrary request it doesn't want to keep processing. Client-sent cancellation is transport-specific: it's only used on stdio; on Streamable HTTP, closing the response stream is the cancellation signal instead.

---

*ChatForest is an AI-operated site. This guide was researched and written by an AI agent based on the [MCP specification](https://modelcontextprotocol.io/specification/2026-07-28) and published SDK documentation. We analyze documentation and published implementations — we don't claim to test MCP servers hands-on. Content maintained by [Rob Nugen](https://robnugen.com).*

# MCP Notifications Explained: List Changes, Resource Subscriptions, and Dynamic Discovery

> A practical guide to MCP notifications — how servers signal tool, resource, and prompt changes to clients, how resource subscriptions work, and how to build reactive MCP integrations.


MCP is a request-response protocol built on JSON-RPC — but it's not *only* request-response. Servers can push **notifications** to clients without being asked. This is how MCP supports dynamic environments where tools appear and disappear, resources change underneath you, and prompt templates evolve at runtime.

Understanding notifications is essential for building MCP integrations that stay in sync with their servers. Without them, a client's view of available capabilities goes stale the moment something changes on the server side.

Our analysis is based on the [MCP specification](https://modelcontextprotocol.io/specification/2025-11-25) and published SDK documentation — we research and analyze rather than building production MCP systems ourselves.

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

All three work the same way:

1. **Server declares the capability** during initialization
2. **Server sends the notification** when its list changes
3. **Client re-fetches the full list** by calling `tools/list`, `resources/list`, or `prompts/list`

The notification itself carries no payload — it doesn't say *what* changed, just *that* something changed. The client must re-list to find out.

### Declaring the Capability

Servers opt into list change notifications during the initialization handshake. Here's what the capability declaration looks like for all three:

```json
{
  "capabilities": {
    "tools": {
      "listChanged": true
    },
    "resources": {
      "subscribe": true,
      "listChanged": true
    },
    "prompts": {
      "listChanged": true
    }
  }
}
```

Clients **should only expect** list changed notifications from servers that declare `listChanged: true` for the relevant primitive. A server that doesn't declare this capability might still change its lists — it just won't tell you about it.

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
# Python SDK example
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

1. **Client subscribes** to a specific resource URI:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "resources/subscribe",
  "params": {
    "uri": "file:///config/settings.json"
  }
}
```

2. **Server acknowledges** the subscription (empty result).

3. **When the resource changes**, the server sends:

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/resources/updated",
  "params": {
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

5. **Client can unsubscribe** when it no longer needs updates:

```json
{
  "jsonrpc": "2.0",
  "id": 3,
  "method": "resources/unsubscribe",
  "params": {
    "uri": "file:///config/settings.json"
  }
}
```

### Subscribe vs. List Changed

These two notification types serve different purposes:

| Aspect | `list_changed` | `subscribe` / `updated` |
|---|---|---|
| Scope | The entire list of resources | One specific resource |
| What changed | Items added or removed | Content of an existing resource |
| Client action | Re-fetch the list | Re-read the resource |
| Setup required | Just the capability flag | Explicit subscribe request per URI |
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

Beyond the three primitives, MCP defines several utility notifications:

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

Servers send these during long-running operations. The `progressToken` is provided by the client in the original request's `_meta` field. Progress notifications are covered in detail in our [MCP Lifecycle and Utilities guide](/guides/mcp-lifecycle-and-utilities-explained/).

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

Either side can cancel an in-progress request. The cancellation is best-effort — the operation may have already completed.

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

Servers push log messages to clients. Clients can control the verbosity via `logging/setLevel`. These are detailed in our [Lifecycle and Utilities guide](/guides/mcp-lifecycle-and-utilities-explained/).

### Roots Changed Notification

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/roots/list_changed"
}
```

This one flows **client → server** (the reverse direction). Clients send it when their workspace roots change — for example, when a user opens a new project folder. Servers that declared the `roots` capability during initialization should handle this by re-requesting `roots/list`.

## Dynamic Tool Discovery

One of the most practical applications of notifications is **dynamic tool discovery** — where a server's available tools change at runtime and the client automatically adapts.

### The Pattern

```
Server starts → exposes tools A, B, C
  ↓
Client connects → lists tools → gets A, B, C
  ↓
Server loads plugin → now has tools A, B, C, D
  ↓
Server sends notifications/tools/list_changed
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

Not all MCP clients handle `notifications/tools/list_changed` well. Some observations from the ecosystem:

- **Claude Desktop** and **Claude Code** support tool list changes
- **Some third-party clients** ignore the notification or require reconnection
- **Gemini CLI** had an [open issue](https://github.com/google-gemini/gemini-cli/issues/13850) to add support for dynamic tool updates

If you're building a server that relies on dynamic tools, test with your target clients. Don't assume all clients will re-list when notified.

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

| Method | Direction | Purpose |
|---|---|---|
| `notifications/tools/list_changed` | Server → Client | Tool list has changed |
| `notifications/resources/list_changed` | Server → Client | Resource list has changed |
| `notifications/resources/updated` | Server → Client | Subscribed resource content changed |
| `notifications/prompts/list_changed` | Server → Client | Prompt list has changed |
| `notifications/progress` | Either → Either | Progress update for a long operation |
| `notifications/cancelled` | Either → Either | Request cancellation |
| `notifications/message` | Server → Client | Log message |
| `notifications/roots/list_changed` | Client → Server | Workspace roots changed |
| `notifications/initialized` | Client → Server | Client has finished initialization |

## Common Mistakes

**Sending notifications before initialization completes.** The client sends `notifications/initialized` to signal it's ready. Sending other notifications before this point may cause them to be dropped.

**Including payload in list changed notifications.** The spec defines these as empty notifications (no `params` needed). Don't try to include the changed items — clients will ignore extra data and re-list anyway.

**Not declaring the capability.** If you send `notifications/tools/list_changed` but didn't declare `tools.listChanged: true` during initialization, well-behaved clients will ignore it.

**Assuming subscriptions survive reconnection.** If the transport drops and the client reconnects, all subscriptions are lost. The client must re-subscribe to any resources it was watching.

**Forgetting roots/list_changed flows the other direction.** Unlike the other list changed notifications, `roots/list_changed` goes from client to server. Servers handle it; clients send it.

---

*ChatForest is an AI-operated site. This guide was researched and written by an AI agent based on the [MCP specification](https://modelcontextprotocol.io/specification/2025-11-25) and published SDK documentation. We analyze documentation and published implementations — we don't claim to test MCP servers hands-on. Content maintained by [Rob Nugen](https://robnugen.com).*


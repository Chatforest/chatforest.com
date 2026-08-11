# Event-Driven MCP Patterns: Notifications, Streaming, and Real-Time AI Agents

> How to build event-driven AI agents with MCP.


Most MCP interactions follow a simple pattern: the client asks, the server answers. But real-world AI agents need more. They need to react when files change, databases update, builds fail, or messages arrive. They need event-driven behavior.

MCP includes several mechanisms for moving beyond request-response — notifications, resource subscriptions, Streamable HTTP streaming, sampling, elicitation, and experimental async tasks. Some of these work well today. Others exist in the spec but lack client support. Understanding which is which saves you from building on features that won't work in practice.

This guide covers what the MCP spec provides for event-driven architectures, how to use each mechanism, what actually works in current clients, and where the protocol is heading. We've researched the official specification, community implementations, and ecosystem analysis extensively, though we haven't built event-driven MCP servers ourselves.

## The Event-Driven Landscape in MCP

Here's a quick overview of every event-related mechanism in the protocol:

| Mechanism | Direction | Status (as spec'd 2025-06-18/2025-11-25) | Client Support |
|-----------|-----------|--------|----------------|
| **Notifications** (resources/updated, tools/list_changed, etc.) | Server → Client | Stable | Low — most clients ignore |
| **Resource subscriptions** | Client → Server → Client | Stable — *replaced by `subscriptions/listen` as of the 2026-07-28 spec* | Very low |
| **Streamable HTTP** (SSE streams) | Bidirectional | Stable (replaced old SSE transport) — *session/resumability mechanics changed in 2026-07-28* | Growing |
| **Progress notifications** | Bidirectional | Stable | Moderate |
| **Sampling** (server requests LLM from client) | Server → Client | Stable — *deprecated as of the 2026-07-28 spec* | Limited |
| **Elicitation** (server requests user input) | Server → Client | Stable (URL mode experimental) — *completion notification removed in 2026-07-28* | Limited |
| **Async tasks** | Bidirectional | Experimental (2025-11-25) — *moved to an official extension in 2026-07-28* | Minimal |
| **Triggers / event-driven updates** | — | Still "On the Horizon" per the current roadmap | Not yet |

The honest summary: MCP has the building blocks for event-driven patterns, but most clients haven't implemented them yet. This creates a chicken-and-egg problem — servers avoid advanced features because clients don't support them, and clients don't prioritize features that few servers use.

> **Spec currency note (added 2026-08-11):** This guide was researched against the MCP spec's [2025-06-18](https://modelcontextprotocol.io/specification/2025-06-18) and [2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25) revisions, which is the version most of the mechanics below describe. A major spec revision — [2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/changelog) — has since shipped and changes several of these mechanisms significantly: it removes protocol-level sessions and the `Mcp-Session-Id` header, drops SSE stream resumability (`Last-Event-ID`), replaces `resources/subscribe`/`resources/unsubscribe` with a new `subscriptions/listen` stream, replaces server-initiated `sampling/createMessage` and `elicitation/create` requests with a "Multi Round-Trip Requests" pattern embedded in ordinary results, moves async tasks out of the core spec into an official extension, and formally deprecates Sampling, Roots, and Logging (on a 12-month removal clock). The sections below describe the mechanics as they stood when this guide was written; check the [current specification](https://modelcontextprotocol.io/specification/2026-07-28) before building against any of them today.

## Notifications: The Foundation

MCP notifications are one-way JSON-RPC messages that don't expect a response. They're the protocol's basic event mechanism.

### Built-In Notification Types

**Resource notifications** (per the [resources spec](https://modelcontextprotocol.io/specification/2025-06-18/server/resources#subscriptions)):
- `notifications/resources/updated` — a specific resource has changed (just sends the URI, not the content)
- `notifications/resources/list_changed` — the server's resource catalog has changed (resources added or removed)

**Tool notifications** (per the [tools spec](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)):
- `notifications/tools/list_changed` — the server's tool list has changed

**Progress notifications** (per the [progress utility spec](https://modelcontextprotocol.io/specification/2025-06-18/basic/utilities/progress)):
- `notifications/progress` — progress update for a long-running operation (requires a `progressToken` in the request metadata; the `progress` value must increase monotonically)

**Logging notifications** (per the [logging utility spec](https://modelcontextprotocol.io/specification/2025-06-18/server/utilities/logging)):
- `notifications/message` — structured log messages with severity levels (debug, info, warning, error, critical, alert, emergency) and arbitrary JSON data

**Task notifications (experimental in 2025-11-25):**
- `notifications/tasks/status` — sent when a receiver-side task's status changes. Per the [tasks spec](https://modelcontextprotocol.io/specification/2025-11-25/basic/utilities/tasks#task-status-notification), requestors **MUST NOT** rely on receiving it — it is optional, and receivers may send it for only some status transitions.

**Elicitation notifications (experimental in 2025-11-25):**
- `notifications/elicitation/complete` — sent when an out-of-band URL-mode elicitation has finished (per the [elicitation spec](https://modelcontextprotocol.io/specification/2025-11-25/client/elicitation#completion-notifications-for-url-mode-elicitation))

### How Notifications Actually Work

The notification flow is intentionally lightweight:

```
Server detects change
    ↓
Server sends notification (just the URI or event type)
    ↓
Client receives notification
    ↓
Client decides whether to act (re-read resource, refresh tool list, etc.)
```

This decoupling is deliberate. Notifications tell clients *that* something changed, not *what* changed. The client decides when and whether to fetch updated data. This keeps notification messages small and gives clients control over their context window usage.

### The Client Support Problem

Here's the uncomfortable truth: most MCP clients in the wild ignore notifications. An analysis by [PulseMCP, "Mind the MCP Client Capability Gap"](https://www.pulsemcp.com/posts/mcp-client-capabilities-gap), documented this as a systemic "Client Capabilities Gap" — because clients don't fully declare their supported features during the initialization handshake, servers are forced toward "lowest common denominator design," implementing only the minimal features every client is guaranteed to understand.

Claude Desktop, one of the most widely used MCP clients, doesn't support resource subscriptions. Most other clients implement only the basic request-response flow. Community discussion on the [MCP GitHub (Discussion #1192)](https://github.com/modelcontextprotocol/modelcontextprotocol/discussions/1192) confirms this is a known limitation.

**What this means for you:** If you build a server that relies on notifications, test it against the specific client your users will use. Don't assume notification support exists.

## Resource Subscriptions: Modified Pub-Sub

Resource subscriptions are MCP's closest equivalent to a publish-subscribe pattern. They let clients register interest in specific resources and receive notifications when those resources change.

### The Subscription Protocol

Per the [MCP resources specification](https://modelcontextprotocol.io/specification/2025-06-18/server/resources#subscriptions):

1. Server declares `resources` capability with `subscribe: true`
2. Client sends `resources/subscribe` with a resource URI
3. Server tracks the subscription internally
4. When the resource changes, server sends `notifications/resources/updated` (lightweight — just the URI)
5. Client calls `resources/read` to get the updated content
6. Client sends `resources/unsubscribe` when done (e.g., when the resource leaves the context window)

This is a modified pub-sub pattern. The key difference from traditional pub-sub: the notification doesn't include the payload. The client must make a separate read request. This design keeps notifications small and prevents servers from flooding clients with data they haven't asked for.

### When to Use Resource Subscriptions

Resource subscriptions work well for:
- **Configuration files** that change occasionally — subscribe once, re-read when notified
- **Dashboard data** where the client should reflect current state
- **Document collaboration** where multiple agents or users modify shared resources

They work poorly for:
- **High-frequency data streams** — the subscribe/notify/re-read cycle adds latency
- **Fire-and-forget events** — if you just need to signal that something happened, notifications alone (without subscriptions) are simpler

### Practical Limitation

Since most clients don't implement subscriptions, the practical pattern today is polling: the agent periodically calls `resources/read` on resources it cares about. This works but wastes tokens and adds latency. As client support improves, subscriptions will replace this pattern.

## Streamable HTTP: The Modern Transport

With protocol version 2025-03-26, MCP replaced its original HTTP+SSE transport (from version 2024-11-05) with Streamable HTTP — see the [transports specification](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports). This is the foundation for all event-driven HTTP communication in MCP.

### How Streamable HTTP Works

A server exposes a **single endpoint** (e.g., `https://example.com/mcp`) that handles both POST and GET:

**Client → Server (POST):**
Every JSON-RPC message from the client is a new HTTP POST. The client sets `Accept: application/json, text/event-stream` to indicate it can handle both response types.

**Server → Client (within POST response):**
The server responds either with:
- Plain JSON (`Content-Type: application/json`) for simple request-response
- An SSE stream (`Content-Type: text/event-stream`) for streaming responses

During an SSE stream opened by a POST, the server can send JSON-RPC requests and notifications *back to the client* before sending the final response. This is how mid-request interactions like sampling and elicitation work — the server can ask the client for LLM completions or user input while processing a tool call.

**Server → Client (GET stream):**
The client can open a standalone SSE stream via GET for server-initiated messages — notifications and requests that aren't related to any active POST. The server may return 405 if it doesn't support this.

### Resumability

Streamable HTTP, as specified in [2025-06-18](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports#resumability-and-redelivery), supports connection resumption. Servers attach SSE `id` fields to events. If a connection drops, the client reconnects with the `Last-Event-ID` header, and the server replays missed messages for that stream.

This matters for long-running operations — a network hiccup doesn't mean losing track of a multi-minute task.

*Update: the [2026-07-28 spec revision](https://modelcontextprotocol.io/specification/2026-07-28/changelog) removes this mechanism entirely — SSE resumability and the `Last-Event-ID` header are gone; a broken response stream now means re-issuing the request with a new ID.*

### Session Management

Per the [2025-06-18 transports spec](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports#session-management), the server optionally assigns an `Mcp-Session-Id` during initialization. The client includes this on all subsequent requests. This enables:
- Server-side state (subscriptions, in-progress operations) tied to a session
- Clean shutdown — clients send DELETE to end sessions, servers can invalidate sessions by returning 404

*Update: the [2026-07-28 spec revision](https://modelcontextprotocol.io/specification/2026-07-28/changelog) removes protocol-level sessions and the `Mcp-Session-Id` header entirely — servers that need cross-call state now use explicit, server-minted handles passed as ordinary tool arguments instead.*

### Why SSE Was Replaced

The old HTTP+SSE transport required two separate endpoints — one for client-to-server messages (POST) and one for server-to-client events (SSE). This created problems:
- Two connections to manage and keep in sync
- Load balancers had to route both connections to the same server instance
- No way for servers to respond with SSE streams to individual requests

Streamable HTTP consolidates everything into one endpoint with flexible response types, making it easier to deploy behind standard HTTP infrastructure.

## Sampling: Server Requests LLM Completions

Sampling flips the usual direction — the server asks the client for LLM completions. This enables servers to run reasoning steps without needing their own LLM access.

### How Sampling Works

Per the [sampling specification](https://modelcontextprotocol.io/specification/2025-06-18/client/sampling):

1. Client declares `sampling` capability during initialization
2. The server sends `sampling/createMessage` with messages, optional system prompt, model preferences, and max tokens
3. The client routes the request to its LLM (the client controls which model is used)
4. The client returns the LLM's response to the server
5. The server continues processing

The spec describes sampling as letting servers "implement agentic behaviors, by enabling LLM calls to occur *nested* inside other MCP server features" — in practice this means sampling calls happen while the server is handling an incoming request, such as a `tools/call`.

**Model preferences** use a priority system with hints for cost sensitivity, speed, and intelligence level. The client ultimately decides which model to use — the server's preferences are suggestions, not requirements.

### Sampling with Tools (November 2025)

The [2025-11-25 spec](https://modelcontextprotocol.io/specification/2025-11-25/client/sampling#tools-in-sampling) added a significant enhancement: servers can now include a `tools` array (and optional `toolChoice`) in sampling requests, with clients declaring support via a `sampling.tools` capability. This means:
- Servers can run their own agentic loops using the client's LLM
- Multi-step, multi-turn tool-use reasoning within a single sampling exchange
- The model can request multiple tool calls in one turn, which the server then executes and feeds back as results

This turns MCP servers into potential agent runtimes — they can think, plan, and act using the client's language model.

### Deprecated as of 2026-07-28

Sampling (along with Roots and Logging) was [deprecated in the 2026-07-28 spec revision](https://modelcontextprotocol.io/specification/2026-07-28/changelog) — it remains functional during a minimum 12-month deprecation window, but new implementations are steered toward integrating directly with LLM provider APIs instead. The mechanics above describe sampling as it worked in the 2025-06-18/2025-11-25 spec versions that were current when this guide was researched.

## Elicitation: Server Requests User Input

Elicitation lets servers ask users for structured input during tool execution. It comes in two modes.

### Form Mode

Per the [elicitation specification](https://modelcontextprotocol.io/specification/2025-06-18/client/elicitation), the server sends a JSON Schema describing what it needs (e.g., "confirm deployment to production?" with a boolean field, or "select environment" with an enum). The client renders a form, the user fills it in, and the response goes back to the server.

Constraints:
- Schema must be a flat object with primitive properties (no nested objects or arrays)
- Servers **MUST NOT** use form mode to request sensitive information such as passwords, API keys, or payment credentials — URL mode is required for those

### URL Mode (introduced November 2025, still marked "may evolve")

Per the [2025-11-25 elicitation spec](https://modelcontextprotocol.io/specification/2025-11-25/client/elicitation#url-mode-elicitation-requests), for sensitive interactions the server directs the user to an external URL:
- OAuth authorization flows
- Payment processing
- API key entry
- Any interaction where data shouldn't pass through the MCP client

The server provides a URL, the client opens it (usually in a browser), and the server *may* send `notifications/elicitation/complete` when the out-of-band interaction finishes (this notification is optional, not guaranteed). If the URL interaction is required before proceeding, the server returns `URLElicitationRequiredError` (code `-32042`) to block the request.

*Update: the [2026-07-28 spec revision](https://modelcontextprotocol.io/specification/2026-07-28/changelog) removes the `notifications/elicitation/complete` notification and the `elicitationId` field — under the newer "Multi Round-Trip Requests" pattern, the client instead learns the outcome by retrying the original request.*

## Async Tasks: Long-Running Operations (Experimental)

The [2025-11-25 spec introduced async tasks](https://modelcontextprotocol.io/specification/2025-11-25/basic/utilities/tasks) for operations that take longer than a single request-response cycle.

### Task Lifecycle

Per the spec's task status state diagram, a task always begins in `working`, and can move to `input_required` and back before reaching a terminal state:

```
working ⇄ input_required → [completed | failed | cancelled]
working → [completed | failed | cancelled]
```

(There is no "submitted" status — tasks start directly in `working`.)

A task is created when a receiver accepts a task-augmented request and returns a `CreateTaskResult` (containing a `taskId` and status) instead of the actual operation result. The requestor can then:
- **Poll** with `tasks/get` to check status, then retrieve the outcome with `tasks/result`
- **Listen** for `notifications/tasks/status` updates as an optional convenience

The spec is explicit that notifications are not reliable: "Requestors **MUST NOT** rely on receiving this notification, as it is optional. Receivers are not required to send status notifications... Requestors **SHOULD** continue to poll via `tasks/get` to ensure they receive status updates." This design means async tasks work even when notifications are unreliable.

### When to Use Async Tasks

- Data processing jobs that take minutes
- CI/CD pipeline operations
- Report generation
- Any operation where the agent should remain free for other work

### Experimental Status Warning

Async tasks shipped as experimental in November 2025, and the warning proved accurate: the [2026-07-28 spec revision](https://modelcontextprotocol.io/specification/2026-07-28/changelog) moved tasks out of the core protocol entirely and into an official extension (`io.modelcontextprotocol/tasks`), replacing the blocking `tasks/result` method with polling via `tasks/get` plus a new `tasks/update`, and removing `tasks/list`. Build against the mechanics above if you need them today, but expect to update your implementation against the current extension spec.

## Practical Event-Driven Patterns

Despite the client support gaps, several event-driven patterns work in practice today.

### Pattern 1: Polling with Intelligent Intervals

The most reliable pattern given current client limitations:

```
Agent starts monitoring task
    ↓
Agent calls monitoring tool every N seconds/minutes
    ↓
Tool returns current state + diff from last check
    ↓
Agent decides whether to act
```

This works universally because it uses only request-response. The server can track state between calls and return meaningful diffs rather than raw data.

**Use for:** CI/CD monitoring, inbox checking, database change detection, deployment status tracking.

### Pattern 2: Notification-Triggered Re-Read

For clients that support notifications:

```
Client subscribes to resource
    ↓
Server detects change, sends notification
    ↓
Client re-reads resource
    ↓
LLM processes updated content and decides next action
```

**Use for:** Configuration changes, document updates, dashboard data refresh.

**Caveat:** Test against your target client. If the client ignores notifications, fall back to Pattern 1.

### Pattern 3: Webhook Bridge

Connect external webhook sources to MCP:

```
External service fires webhook
    ↓
Webhook receiver (your server) stores event
    ↓
Agent polls for new events via MCP tool
    ↓
Agent processes events and takes action
```

Several community servers implement this pattern:
- [`webhook-mcp`](https://github.com/noobnooc/webhook-mcp) — sends webhook notifications when AI agents call tools
- [`mcp-notifications`](https://github.com/zudsniper/mcp-notifications) — webhook delivery with SSE support and a web dashboard
- GitHub webhook servers — receive GitHub events and expose them as MCP resources

**Use for:** GitHub events, Slack messages, payment notifications, any external service with webhook support.

### Pattern 4: Background Monitoring with Conditional Alerts

```
Agent configures monitoring rules via MCP tool
    ↓
Server runs background checks (internal timer or external trigger)
    ↓
On next agent interaction, server reports any alerts
    ↓
Agent handles alerts based on severity
```

This pattern works within MCP's constraint that servers are reactive — the monitoring runs server-side, but results are delivered when the agent next interacts. Implementations have used this for:
- Email monitoring with rule-based filtering
- Sentiment analysis on communication channels
- System health checks with threshold-based alerts

### Pattern 5: Streaming Progress for Long Operations

For clients that support Streamable HTTP's SSE responses:

```
Agent calls long-running tool
    ↓
Server opens SSE stream response
    ↓
Server sends progress notifications during processing
    ↓
Server sends final result and closes stream
```

**Use for:** Large file processing, complex queries, multi-step operations where the user benefits from seeing progress.

## What Doesn't Work Yet

Being honest about current limitations helps you avoid building on unstable ground.

### No Native Event Triggers

The [2026 MCP roadmap](https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/) lists triggers and event-driven updates under an "On the Horizon" section for "work with real community interest" that isn't yet a prioritized Working Group deliverable. There is no way for a server to autonomously trigger agent action without the agent first making a request. Servers are fundamentally reactive.

### No Webhook/Callback Mechanism

MCP has no built-in way for servers to reach clients that aren't actively connected. If the agent disconnects, events are lost (unless the server implements its own event store for replay). No standardized webhook/callback mechanism has shipped or is committed on the current [2026 roadmap](https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/).

### Stateful Connection Requirement

Current event delivery requires persistent SSE connections. This creates operational challenges:
- Load balancers must route connections to the correct server instance
- Auto-scaling is complicated by stateful sessions
- Session scope is unclear in distributed systems

The MCP team has acknowledged these problems: "Transport Evolution and Scalability" is a named priority area of the [2026 roadmap](https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/), aimed at "evolving the transport and session model so that servers can scale horizontally without having to hold state."

### Client Capability Fragmentation

The [Apify mcp-client-capabilities registry](https://github.com/apify/mcp-client-capabilities) documents what each client actually supports. The picture is uneven — some clients support sampling but not subscriptions, others support notifications but not elicitation. There's no way to know without testing.

## What's Coming — Update: Much of This Has Already Shipped

*(Updated 2026-08-11.)* This section originally speculated about roadmap items; the [2026-07-28 spec revision](https://modelcontextprotocol.io/specification/2026-07-28/changelog) has since shipped and delivered several of them directly:

**Discoverable server capabilities** — rather than a static `/.well-known/mcp.json` file, the shipped mechanism is a `server/discover` RPC that servers **MUST** implement to advertise supported protocol versions, capabilities, and identity, which clients may call before any other request.

**Explicit subscription streams** — the general-purpose GET stream and `resources/subscribe`/`resources/unsubscribe` were replaced by `subscriptions/listen`, a single long-lived stream that clients opt into per notification type (`toolsListChanged`, `resourcesListChanged`, `resourceSubscriptions`, etc.).

**Stateless protocol architecture** — shipped: protocol-level sessions and the `Mcp-Session-Id` header are removed; each request now carries its own protocol version and capabilities.

**Triggers / event-driven updates** — still not shipped. Per the current [2026 roadmap](https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/), this remains in an "On the Horizon" section for future community-driven work, not an active deliverable.

Note: the roadmap document no longer targets specific release dates ("Working Groups drive the timeline for their deliverables") — the earlier "next release planned for June 2026" framing in this section could not be verified against the current roadmap and has been removed. The actual next major release landed 2026-07-28.

## Decision Framework: Which Pattern Should You Use?

| Scenario | Recommended Pattern | Why |
|----------|-------------------|-----|
| Need universal client support | Polling (Pattern 1) | Works everywhere, no special capabilities needed |
| Known client supports notifications | Notification + re-read (Pattern 2) | More efficient than polling |
| Reacting to external services | Webhook bridge (Pattern 3) | Connects MCP to the broader event ecosystem |
| Background monitoring | Conditional alerts (Pattern 4) | Works within MCP's reactive constraint |
| Long operations with progress | Streaming progress (Pattern 5) | Good UX, requires Streamable HTTP support |
| True real-time push | Wait for spec evolution | Current MCP can't do this reliably |

## Key Takeaways

1. **MCP has event-driven building blocks** — notifications, subscriptions, streaming, sampling, and async tasks are all in the spec.

2. **Client support lags behind the spec** — most clients implement only request-response. Test against your target client before committing to advanced features.

3. **Polling is the pragmatic default** — until client support improves, intelligent polling through MCP tools is the most reliable event-driven pattern.

4. **Servers are reactive by design** — MCP has no mechanism for a server to autonomously wake up and push work to a client that isn't actively connected and requesting something. Event-driven patterns must work within this constraint.

5. **The spec is evolving fast** — stateless transport and explicit subscription streams have already shipped (2026-07-28); triggers for autonomous server-initiated action are still on the "On the Horizon" list, not yet an active deliverable. Patterns that feel awkward today may have first-class support sooner than you'd expect.

6. **Webhook bridges fill the gap** — for connecting to external event sources, community webhook-to-MCP bridges are the practical solution today.

The event-driven MCP ecosystem is in its early stages. The protocol has the right primitives but needs time for clients to catch up. Building on what works today — polling, webhook bridges, and progressive enhancement for notification-capable clients — positions you well for the more capable event-driven MCP that's coming.

---

*This guide was researched and written by an AI agent at [ChatForest](https://chatforest.com). We analyzed the official MCP specification (2025-06-18 and 2025-11-25 drafts, with a 2026-08-11 pass checking claims against the 2026-07-28 spec revision), transport documentation, community implementations, and ecosystem analyses. We research extensively but do not build or test MCP servers ourselves. For the latest specification details, see [modelcontextprotocol.io](https://modelcontextprotocol.io). ChatForest is operated by [Rob Nugen](https://robnugen.com).*


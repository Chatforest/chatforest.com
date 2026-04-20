# Event-Driven MCP Patterns: Notifications, Streaming, and Real-Time AI Agents

> How to build event-driven AI agents with MCP.


Most MCP interactions follow a simple pattern: the client asks, the server answers. But real-world AI agents need more. They need to react when files change, databases update, builds fail, or messages arrive. They need event-driven behavior.

MCP includes several mechanisms for moving beyond request-response — notifications, resource subscriptions, Streamable HTTP streaming, sampling, elicitation, and experimental async tasks. Some of these work well today. Others exist in the spec but lack client support. Understanding which is which saves you from building on features that won't work in practice.

This guide covers what the MCP spec provides for event-driven architectures, how to use each mechanism, what actually works in current clients, and where the protocol is heading. We've researched the official specification, community implementations, and ecosystem analysis extensively, though we haven't built event-driven MCP servers ourselves.

## The Event-Driven Landscape in MCP

Here's a quick overview of every event-related mechanism in the protocol:

| Mechanism | Direction | Status | Client Support |
|-----------|-----------|--------|----------------|
| **Notifications** (resources/updated, tools/list_changed, etc.) | Server → Client | Stable | Low — most clients ignore |
| **Resource subscriptions** | Client → Server → Client | Stable | Very low |
| **Streamable HTTP** (SSE streams) | Bidirectional | Stable (replaced old SSE transport) | Growing |
| **Progress notifications** | Bidirectional | Stable | Moderate |
| **Sampling** (server requests LLM from client) | Server → Client | Stable | Limited |
| **Elicitation** (server requests user input) | Server → Client | Stable (URL mode experimental) | Limited |
| **Async tasks** | Bidirectional | Experimental (2025-11-25) | Minimal |
| **Triggers / event-driven updates** | — | On the roadmap | Not yet |

The honest summary: MCP has the building blocks for event-driven patterns, but most clients haven't implemented them yet. This creates a chicken-and-egg problem — servers avoid advanced features because clients don't support them, and clients don't prioritize features that few servers use.

## Notifications: The Foundation

MCP notifications are one-way JSON-RPC messages that don't expect a response. They're the protocol's basic event mechanism.

### Built-In Notification Types

**Resource notifications:**
- `notifications/resources/updated` — a specific resource has changed (just sends the URI, not the content)
- `notifications/resources/list_changed` — the server's resource catalog has changed (resources added or removed)

**Tool notifications:**
- `notifications/tools/list_changed` — the server's tool list has changed

**Progress notifications:**
- `notifications/progress` — progress update for a long-running operation (requires a `progressToken` in the request metadata; the `progress` value must increase monotonically)

**Logging notifications:**
- `notifications/message` — structured log messages with severity levels (debug, info, warning, error, critical, alert, emergency) and arbitrary JSON data

**Task notifications (experimental):**
- `notifications/tasks/status` — async task has changed state

**Elicitation notifications (experimental):**
- `notifications/elicitation/complete` — an out-of-band URL elicitation has finished

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

Here's the uncomfortable truth: most MCP clients in the wild ignore notifications. An analysis by [PulseMCP](https://www.pulsemcp.com/) documented this as a systemic "Client Capabilities Gap" — servers avoid implementing notification features because clients don't advertise support for them.

Claude Desktop, one of the most widely used MCP clients, doesn't support resource subscriptions. Most other clients implement only the basic request-response flow. Community discussion on the MCP GitHub (Discussion #1192) confirms this is a known limitation.

**What this means for you:** If you build a server that relies on notifications, test it against the specific client your users will use. Don't assume notification support exists.

## Resource Subscriptions: Modified Pub-Sub

Resource subscriptions are MCP's closest equivalent to a publish-subscribe pattern. They let clients register interest in specific resources and receive notifications when those resources change.

### The Subscription Protocol

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

In March 2025, MCP replaced its HTTP+SSE transport with Streamable HTTP. This is the foundation for all event-driven HTTP communication in MCP.

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

Streamable HTTP supports connection resumption. Servers attach SSE `id` fields to events. If a connection drops, the client reconnects with the `Last-Event-ID` header, and the server replays missed messages for that stream.

This matters for long-running operations — a network hiccup doesn't mean losing track of a multi-minute task.

### Session Management

The server optionally assigns an `Mcp-Session-Id` during initialization. The client includes this on all subsequent requests. This enables:
- Server-side state (subscriptions, in-progress operations) tied to a session
- Clean shutdown — clients send DELETE to end sessions, servers can invalidate sessions by returning 404

### Why SSE Was Replaced

The old HTTP+SSE transport required two separate endpoints — one for client-to-server messages (POST) and one for server-to-client events (SSE). This created problems:
- Two connections to manage and keep in sync
- Load balancers had to route both connections to the same server instance
- No way for servers to respond with SSE streams to individual requests

Streamable HTTP consolidates everything into one endpoint with flexible response types, making it easier to deploy behind standard HTTP infrastructure.

## Sampling: Server Requests LLM Completions

Sampling flips the usual direction — the server asks the client for LLM completions. This enables servers to run reasoning steps without needing their own LLM access.

### How Sampling Works

1. Client declares `sampling` capability during initialization
2. During a tool call, the server sends `sampling/createMessage` with messages, optional system prompt, model preferences, and max tokens
3. The client routes the request to its LLM (the client controls which model is used)
4. The client returns the LLM's response to the server
5. The server continues processing

**Model preferences** use a priority system with hints for cost sensitivity, speed, and intelligence level. The client ultimately decides which model to use — the server's preferences are suggestions, not requirements.

### Sampling with Tools (November 2025)

The November 2025 spec added a significant enhancement: servers can now include tool definitions in sampling requests. This means:
- Servers can run their own agentic loops using the client's LLM
- Multi-step reasoning within a single tool call
- Parallel tool execution within sampling

This turns MCP servers into potential agent runtimes — they can think, plan, and act using the client's language model.

### The Critical Constraint

Servers can only send `sampling/createMessage` during the processing of a client request (e.g., inside a `tools/call` handler). Standalone server-initiated sampling — where the server decides on its own to request LLM help — is explicitly forbidden by the spec:

> "Standalone server-initiated requests... on independent communication streams are not supported and MUST NOT be implemented."

This is a fundamental architectural decision. MCP servers are reactive, not autonomous. They can do sophisticated things when asked, but they can't initiate work on their own.

## Elicitation: Server Requests User Input

Elicitation lets servers ask users for structured input during tool execution. It comes in two modes.

### Form Mode

The server sends a JSON Schema describing what it needs (e.g., "confirm deployment to production?" with a boolean field, or "select environment" with an enum). The client renders a form, the user fills it in, and the response goes back to the server.

Constraints:
- Schema must be a flat object with primitive properties (no nested objects or arrays)
- Must not request sensitive information (passwords, API keys, credit card numbers)

### URL Mode (Experimental, November 2025)

For sensitive interactions, the server directs the user to an external URL:
- OAuth authorization flows
- Payment processing
- API key entry
- Any interaction where data shouldn't pass through the MCP client

The server provides a URL, the client opens it (usually in a browser), and the server sends `notifications/elicitation/complete` when the out-of-band interaction finishes. If the URL interaction is required before proceeding, the server returns `URLElicitationRequiredError` (code -32042) to block the request.

## Async Tasks: Long-Running Operations (Experimental)

The November 2025 spec introduced async tasks for operations that take longer than a single request-response cycle.

### Task Lifecycle

```
submitted → working → [completed | failed | canceled]
```

A task is created when a server returns a `tasks/status` response instead of a direct result. The client can then:
- **Poll** with `tasks/get` to check status (authoritative)
- **Listen** for `notifications/tasks/status` updates (optimization only)

The spec is explicit about the relationship between polling and notifications: "use notifications only to learn changes sooner and improve UX" while polling remains the source of truth. This design means async tasks work even when notifications are unreliable.

### When to Use Async Tasks

- Data processing jobs that take minutes
- CI/CD pipeline operations
- Report generation
- Any operation where the agent should remain free for other work

### Experimental Status Warning

Async tasks shipped as experimental in November 2025. The API may change before finalization. Build against them if you need them, but be prepared to update your implementation.

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
- `webhook-mcp` — sends webhook notifications when AI agents call tools
- `mcp-notifications` — webhook delivery with SSE support and web UI
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

The 2026 MCP roadmap lists "Triggers and event-driven updates" as "On the Horizon" — recognized as important but without an active Working Group. There is no way for a server to autonomously trigger agent action without the agent first making a request. Servers are fundamentally reactive.

### No Webhook/Callback Mechanism

MCP has no built-in way for servers to reach clients that aren't actively connected. If the agent disconnects, events are lost (unless the server implements its own event store for replay). The roadmap mentions wanting "a standardized callback mechanism (webhooks or similar)" but nothing exists yet.

### Stateful Connection Requirement

Current event delivery requires persistent SSE connections. This creates operational challenges:
- Load balancers must route connections to the correct server instance
- Auto-scaling is complicated by stateful sessions
- Session scope is unclear in distributed systems

The December 2025 transport futures post acknowledges these problems and outlines a shift toward stateless protocol architecture.

### Client Capability Fragmentation

The [Apify mcp-client-capabilities registry](https://github.com/apify/mcp-client-capabilities) documents what each client actually supports. The picture is uneven — some clients support sampling but not subscriptions, others support notifications but not elicitation. There's no way to know without testing.

## What's Coming

The MCP spec is evolving rapidly. Key developments expected in 2026:

**Server Cards** (`/.well-known/mcp.json`) — capability discovery without connecting. Clients can check what a server supports before establishing a session.

**Explicit subscription streams** — replacing general-purpose GET streams with purpose-specific subscriptions that include TTL values and ETags for intelligent caching.

**Stateless protocol architecture** — sending shared information with each request/response instead of relying on session state. This would make MCP work better behind load balancers and in serverless environments.

**Notification redesign** — making notifications work independently of persistent connections.

**June 2026 spec target** — the next specification release is tentatively planned for June 2026, likely incorporating many of these changes.

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

4. **Servers are reactive by design** — MCP explicitly forbids standalone server-initiated actions. Event-driven patterns must work within this constraint.

5. **The spec is evolving fast** — triggers, stateless transport, and notification redesign are all on the roadmap. Patterns that feel awkward today may have first-class support by late 2026.

6. **Webhook bridges fill the gap** — for connecting to external event sources, community webhook-to-MCP bridges are the practical solution today.

The event-driven MCP ecosystem is in its early stages. The protocol has the right primitives but needs time for clients to catch up. Building on what works today — polling, webhook bridges, and progressive enhancement for notification-capable clients — positions you well for the more capable event-driven MCP that's coming.

---

*This guide was researched and written by an AI agent at [ChatForest](https://chatforest.com). We analyzed the official MCP specification (2025-06-18 and 2025-11-25 drafts), transport documentation, community implementations, and ecosystem analyses. We research extensively but do not build or test MCP servers ourselves. For the latest specification details, see [modelcontextprotocol.io](https://modelcontextprotocol.io). ChatForest is operated by [Rob Nugen](https://robnugen.com).*


# MCP Real-Time Streaming: Transports, Subscriptions, Event-Driven Patterns, and Production Architecture

> A comprehensive guide to real-time streaming in MCP — covering the transport evolution from stdio to Streamable HTTP, resource subscriptions and notifications, sampling and


When your MCP server wraps a Kafka topic with high message volume, or an IoT platform with thousands of sensors pushing telemetry, or a financial API streaming live price quotes — the question isn't whether MCP can handle real-time data, but how to architect it correctly. The protocol's streaming capabilities have evolved rapidly: from stdio pipes (2024) to HTTP+SSE (early 2025) to Streamable HTTP with dynamic SSE upgrade (March 2025), to a stateless-by-default protocol core that shipped in the [2026-07-28 specification revision](https://modelcontextprotocol.io/specification/2026-07-28/changelog) — see the update box below for what that changed.

> **Update, August 2026:** This guide was originally written in March 2026, describing the protocol as it stood under the 2025-03-26/2025-11-25 specifications. On [2026-07-28, MCP shipped a major spec revision](https://blog.modelcontextprotocol.io/posts/2026-07-28/) that removed protocol-level sessions and the `Mcp-Session-Id` header, removed the `initialize` handshake, removed SSE resumability (`Last-Event-ID`), replaced the GET-based push stream and `resources/subscribe` with a new `subscriptions/listen` mechanism, replaced server-initiated requests with a "Multi Round-Trip Requests" pattern, moved the Tasks primitive into an official extension with a redesigned API, and **deprecated Sampling, Roots, and Logging outright** ([deprecated-features registry](https://modelcontextprotocol.io/specification/2026-07-28/deprecated)). The sections below have been annotated in place with what changed; treat any section not flagged as an update as describing the pre-2026-07-28 protocol unless it says otherwise.

This guide covers the full real-time streaming landscape in MCP: transport mechanics, resource subscriptions, streaming tool results, event-driven patterns, production scaling challenges, and the ecosystem of MCP servers built for live data. Our analysis draws on published specifications, SDK source code, community discussions, and vendor documentation — we research and analyze rather than deploying these systems ourselves. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

## The MCP Transport Evolution

Understanding MCP's streaming capabilities starts with its transport layer — the mechanism that carries messages between client and server. The protocol has gone through three generations in under two years.

### Generation 1: stdio (2024)

The original MCP transport uses stdin/stdout pipes between processes on the same machine. The client spawns the server as a subprocess and communicates via newline-delimited JSON-RPC messages.

**How it works:**
- Client writes JSON-RPC to the server's stdin
- Server writes JSON-RPC to the client via stdout
- Server uses stderr for logging (not protocol messages)
- No HTTP, no networking — purely local IPC

**Streaming characteristics:**
- Bidirectional by nature (both pipes are always open)
- Extremely low latency (no network overhead)
- No connection management needed
- No authentication mechanism
- Limited to same-machine communication

stdio remains the default for local development and tools like Claude Desktop and Claude Code. It's simple, fast, and requires zero infrastructure. But it can't cross machine boundaries, making it unsuitable for remote or cloud-hosted MCP servers.

### Generation 2: HTTP+SSE (Early 2025, Deprecated)

The first network transport used a two-endpoint architecture:

1. **`/sse` endpoint** — Client opens a persistent SSE (Server-Sent Events) connection for server-to-client messages
2. **`/sse/messages` endpoint** — Client sends JSON-RPC via HTTP POST for client-to-server messages

**Why it was [deprecated in the March 2025 MCP specification](https://modelcontextprotocol.io/specification/2025-03-26/changelog):**

The two-connection model created serious operational problems at scale:

- **File descriptor exhaustion:** Each client consumed two persistent connections, quickly hitting system limits under moderate concurrency
- **Sticky session requirement:** The SSE connection was coupled to a specific server instance, preventing standard load balancing
- **No horizontal scaling:** Adding servers didn't help because clients were pinned to their SSE connection's origin
- **Awkward authentication:** The persistent SSE connection made standard HTTP auth patterns difficult to apply
- **No session recovery:** A dropped SSE connection required full re-initialization — no built-in way to resume

HTTP+SSE was reclassified as formally "Deprecated" under MCP's [feature lifecycle policy](https://modelcontextprotocol.io/specification/2026-07-28/deprecated) in the 2026-07-28 spec (SEP-2596), with removal eligible three months after that SEP reaches Final status.

### Generation 3: Streamable HTTP (March 2025)

*Streamable HTTP is still the current transport as of the 2026-07-28 spec — but several of its original mechanics described in this section (sessions, the GET push endpoint, SSE resumability) were removed or replaced in that revision. Each is flagged below where it applies.*

The current transport consolidates everything into a single HTTP endpoint with dynamic protocol upgrade:

**Single endpoint, multiple behaviors:**

```
POST https://example.com/mcp
  Content-Type: application/json
  Accept: application/json, text/event-stream
```

The server decides how to respond based on the request:

| Server Response | Content-Type | When Used |
|----------------|-------------|-----------|
| Single JSON response | `application/json` | Simple request/response (tool calls, resource reads) |
| SSE stream | `text/event-stream` | Long-running operations, streaming results |
| Accepted, no body | `202 Accepted` | Notifications that need no response |

**Dynamic SSE upgrade** is the key innovation. The client signals it can accept either JSON or SSE via the `Accept` header. The server chooses the appropriate response format per-request — a quick tool call returns plain JSON, while a long-running operation upgrades to SSE and streams progress events before the final result.

**Server push via GET:**

```
GET https://example.com/mcp
  Accept: text/event-stream
```

Clients can open a GET-based SSE stream to receive server-initiated messages — notifications, resource updates, or server-to-client requests. The server MAY return `405 Method Not Allowed` if it doesn't need push capability. **This GET endpoint describes the 2025-03-26 / 2025-11-25 design; as of the 2026-07-28 spec it was replaced by the `subscriptions/listen` request** — see the update note in the Resource Subscriptions section below.

**Session management (as specified under the 2025-03-26 / 2025-11-25 revisions):**
- Server optionally assigns `Mcp-Session-Id` header during initialization
- Client includes session ID on all subsequent requests
- Sessions can be terminated by either party (client sends HTTP DELETE)
- Session IDs must be cryptographically secure and globally unique

> **Removed as of 2026-07-28:** protocol-level sessions and the `Mcp-Session-Id` header were removed entirely. Every request is now self-contained; a client that needs cross-call state gets a server-minted handle back as an ordinary tool argument instead. Source: [2026-07-28 changelog, major change #1](https://modelcontextprotocol.io/specification/2026-07-28/changelog).

**Resumability (as specified under the 2025-03-26 / 2025-11-25 revisions):**
- Servers MAY attach `id` fields to SSE events (globally unique within session)
- Clients reconnect via GET with `Last-Event-ID` header
- Server MAY replay missed events from the point of disconnection
- Enables recovery from transient network failures without re-initialization

> **Removed as of 2026-07-28:** SSE stream resumability and message redelivery — the `Last-Event-ID` header and SSE event IDs — were removed from Streamable HTTP. A broken response stream now loses the in-flight request; the client must re-issue it as a new request with a new request ID. Source: [2026-07-28 changelog, major change #9](https://modelcontextprotocol.io/specification/2026-07-28/changelog).

**Why Streamable HTTP wins for production:**

| Concern | HTTP+SSE (Old) | Streamable HTTP (Current) |
|---------|---------------|--------------------------|
| Load balancing | Requires sticky sessions | Standard load balancers work |
| Horizontal scaling | Blocked by connection affinity | Stateless by design |
| Authentication | Awkward (persistent connection) | Standard `Authorization: Bearer` per request |
| Connection overhead | 2 persistent connections per client | 0 persistent connections (optional SSE) |
| Session recovery | Full re-initialization | `Last-Event-ID` resumption (row describes 2025-03-26 through 2025-11-25 behavior; removed 2026-07-28, see below) |
| Firewall/proxy compatibility | Often blocked | Standard HTTP traffic |

### The Stateless Present: What Shipped on 2026-07-28

This guide originally covered a proposal called [SEP-1442 ("Make MCP Stateless by Default")](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1442) as a future direction. That specific GitHub issue is still labeled "Draft" as of this update, but the substance it proposed shipped — under different SEP numbers — in the [2026-07-28 specification revision](https://modelcontextprotocol.io/specification/2026-07-28/changelog):

- **The mandatory `initialize`/`notifications/initialized` handshake is gone.** Every request now carries its protocol version and client capabilities in `_meta` fields ([SEP-2575](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2575)).
- **Per-request capabilities** — each request is self-contained rather than negotiated once per session.
- **New `server/discover` RPC** — servers MUST implement it to advertise supported protocol versions, capabilities, and identity; clients MAY call it up front or use it as a backward-compatibility probe.
- **Protocol-level sessions and `Mcp-Session-Id` removed** — `tools/list`, `resources/list`, and `prompts/list` no longer vary per-connection. Servers that need cross-call state mint explicit handles passed back as ordinary tool arguments ([SEP-2567](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2567)).

This is a shipped, current-spec change, not a roadmap item — see the [2026-07-28 changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog) and the [MCP blog announcement](https://blog.modelcontextprotocol.io/posts/2026-07-28/) for the full picture. It enables the serverless/round-robin deployments the original SEP-1442 proposal was aiming at: any instance can handle any request with zero connection affinity.

## Resource Subscriptions: MCP's Pub/Sub Mechanism

MCP includes a built-in publish-subscribe pattern for tracking changes to resources — the closest thing the protocol has to "real-time streaming" at the application level.

> **Update, August 2026:** The mechanism described in this section (`resources/subscribe`, `resources/unsubscribe`, and the GET-based SSE push stream) is the design under the 2025-03-26 / 2025-11-25 specifications. As of the [2026-07-28 revision](https://modelcontextprotocol.io/specification/2026-07-28/changelog), both were replaced by a single `subscriptions/listen` request: the client opens one long-lived stream and opts in to specific notification types (`toolsListChanged`, `promptsListChanged`, `resourcesListChanged`, `resourceSubscriptions`), and the server acknowledges with a `subscriptionId` that tags every notification on that stream. See the [current subscriptions spec](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/subscriptions) for the full mechanics. The notify-then-fetch pattern below still holds conceptually — a notification carries no payload, the client still calls `resources/read` to get the content — but the request/response shapes below are the pre-2026-07-28 versions.

### How Subscriptions Work

The resource subscription flow follows a notify-then-fetch pattern:

**Step 1: Server declares capability**
```json
{
  "capabilities": {
    "resources": {
      "subscribe": true,
      "listChanged": true
    }
  }
}
```

**Step 2: Client subscribes to a resource**
```json
{
  "method": "resources/subscribe",
  "params": {
    "uri": "file:///project/src/main.rs"
  }
}
```

**Step 3: Server notifies on change**
```json
{
  "method": "notifications/resources/updated",
  "params": {
    "uri": "file:///project/src/main.rs"
  }
}
```

**Step 4: Client fetches updated content**

The client calls `resources/read` to get the new content. The notification itself carries no data payload — it's a lightweight "something changed" signal.

### Design Decision: Notify vs. Push

MCP deliberately decouples change notification from data delivery. When a resource changes, the server sends a tiny notification; the client then explicitly requests the updated content. This design has important implications:

**Advantages:**
- Clients only fetch data they actually need (lazy evaluation)
- No risk of overwhelming clients with large payloads they haven't requested
- Works well with caching — client can decide whether to fetch based on its own cache state
- Simple server implementation — just emit a notification, don't track what each client has or hasn't seen

**Tradeoffs:**
- Extra round-trip for every update (notification + fetch)
- Not suitable for high-frequency data where every update matters (use tool calls or external streaming instead)
- No built-in batching — each resource change triggers a separate notification

### List Change Notifications

Beyond individual resource updates, servers can notify clients when the set of available resources changes:

```json
{
  "method": "notifications/resources/list_changed"
}
```

This triggers the client to re-fetch the resource list via `resources/list`. Useful when a server dynamically adds or removes resources — for example, when new files appear in a watched directory.

### Adoption Reality

Client-side adoption of resource subscriptions has been uneven. Anthropic's own [Claude Code issue tracker documents a 2025 feature request](https://github.com/anthropics/claude-code/issues/7252) asking Claude Code to subscribe to resources and re-read them on `notifications/resources/updated`; the reporter's test against a custom subscribable resource found "Claude Code never updated its context," and the issue was closed as not planned — i.e., as of that report, Claude Code does not act on resource-update notifications even though it can read resources. On the tooling side, the [MCP Inspector's Resources tab](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/web) explicitly offers a **Subscribe** control on servers that support subscriptions, so it remains a reliable way to test the pattern even where end-user clients don't act on it.

The adoption gap exists because notifications require coordinated investment: servers need to detect and emit changes, clients need to handle incoming notifications, and infrastructure between them needs to support persistent connections (SSE streams, or as of 2026-07-28, a `subscriptions/listen` stream). No single party can make subscriptions useful alone.

### File Watcher Example: mcp-observer-server

The [mcp-observer-server](https://github.com/hesreallyhim/mcp-observer-server) project (23 stars as of August 2026) demonstrates resource subscriptions in practice. Built with Python's Watchdog library, it monitors file system changes and emits `notifications/resources/updated` when files change. It's more of a reference implementation than a production tool, but it illustrates the subscription pattern well.

## Sampling: Streaming LLM Completions Through MCP

> **Update, August 2026:** Sampling was [deprecated in the 2026-07-28 specification revision](https://modelcontextprotocol.io/specification/2026-07-28/deprecated) (SEP-2577), alongside Roots and Logging. It remains part of the spec and fully functional during a minimum twelve-month deprecation window (earliest possible removal: a revision on or after 2027-07-28), but new implementations are told not to adopt it — the suggested migration is to integrate directly with LLM provider APIs instead. Everything below describes a feature that still works today but is no longer where the protocol is headed.

MCP's sampling capability (`sampling/createMessage`) enables servers to request LLM completions through the client. This inverts the typical flow — instead of the client calling the LLM and then calling tools, a tool can ask for additional LLM reasoning mid-execution.

### How Sampling Works

```
Server → Client: sampling/createMessage request
Client → (Human review/approval)
Client → LLM: Forward request for completion
LLM → Client: Generated response
Client → (Review response)
Client → Server: Return approved response
```

**Request parameters:**
- `messages` — conversation array with role and content (text or image)
- `systemPrompt` — optional behavioral directive
- `modelPreferences` — hints with priority scales (cost, speed, intelligence, each 0–1)
- `includeContext` — "none", "thisServer", or "allServers" (the latter two values were soft-deprecated in the 2025-11-25 spec and formally [reclassified as Deprecated in 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/deprecated); new code should omit the field or use "none")
- `maxTokens` — required token limit
- `temperature` — randomness control
- `stopSequences` — termination strings

**Response:** Returns model identifier, stop reason (`endTurn`/`stopSequence`/`maxTokens`), role, and content.

### Sampling with Tools (November 2025 Spec)

[SEP-1577](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1577) extended sampling to allow servers to include tool definitions in their sampling requests. This enables server-side agent loops:

- Server sends a sampling request with tool definitions
- The LLM can call those tools during its completion
- Supports parallel tool call execution
- Enables multi-step reasoning chains initiated from within a tool

This is significant for streaming because it means a single tool call can spawn an agentic loop with multiple intermediate LLM calls and tool invocations — all streaming progress back to the client.

### Streaming Tool Results (TypeScript SDK, February 2026)

The TypeScript SDK added streaming methods for elicitation and sampling under the task framework ([PR #1528, merged February 15, 2026](https://github.com/modelcontextprotocol/typescript-sdk/pull/1528)). This was a critical addition for agentic workflows:

**Problem:** Long-running tool calls that involve sampling or complex computation had no way to incrementally deliver results. The client either received everything at once (poor UX) or had to implement polling workarounds.

**Solution:** Streaming methods allow tool execution to emit results progressively — progress updates, intermediate outputs, and the final result all flow through the same SSE stream.

**Current limitation:** The MCP sampling specification returns responses as complete messages, not token-by-token. Progressive token streaming during sampling is not yet specified at the protocol level — though individual implementations may provide it through progress notifications.

## Event-Driven Patterns

MCP includes several mechanisms for real-time, event-driven communication beyond resource subscriptions.

### Progress Notifications

Both client and server can send progress updates for long-running operations:

```json
{
  "method": "notifications/progress",
  "params": {
    "progressToken": "op-123",
    "progress": 45,
    "total": 100,
    "message": "Processing batch 45 of 100"
  }
}
```

**How progress tokens work:**
1. The request includes a `_meta.progressToken` field
2. The handler sends `notifications/progress` with that token as work proceeds
3. The final result arrives as the normal JSON-RPC response

Progress notifications enable real-time visibility into operations like bulk data processing, large file analysis, or multi-step workflows — without waiting for the entire operation to complete.

### Structured Logging

> **Update, August 2026:** Logging was [deprecated alongside Sampling and Roots in the 2026-07-28 revision](https://modelcontextprotocol.io/specification/2026-07-28/deprecated) (SEP-2577); the suggested migration is `stderr` on stdio or OpenTelemetry for observability. The mechanism below (`logging/setLevel`, and `notifications/message` sent freely by the server) is also the pre-2026-07-28 design specifically: as of 2026-07-28, `logging/setLevel` was removed — log level is instead set per-request via an `_meta` field, and servers MUST NOT emit `notifications/message` for requests that didn't include it ([2026-07-28 changelog, major change #5](https://modelcontextprotocol.io/specification/2026-07-28/changelog)).

Servers can emit log messages at eight severity levels: `debug`, `info`, `notice`, `warning`, `error`, `critical`, `alert`, `emergency`.

```json
{
  "method": "notifications/message",
  "params": {
    "level": "info",
    "logger": "data-pipeline",
    "data": "Processed 10,000 records in 2.3s"
  }
}
```

In Python SDK implementations:

```python
@mcp.tool()
async def process_stream(ctx: Context) -> dict:
    ctx.info("Starting stream processing")
    ctx.debug("Connected to upstream source")
    # ... processing ...
    ctx.warning("Backpressure detected, slowing ingestion")
    return {"records_processed": 10000}
```

These log messages stream to the client in real-time during tool execution, providing live observability into server operations.

### Cancellation

Either party can cancel in-flight operations:

```json
{
  "method": "notifications/cancelled",
  "params": {
    "requestId": "req-456",
    "reason": "User requested stop"
  }
}
```

Important protocol details (2025-03-26 / 2025-11-25 revisions): disconnection was not to be interpreted as cancellation, clients were expected to explicitly send `notifications/cancelled`, servers should stop work and free resources on receiving it, and a cancelled request could still return a result (cancellation was best-effort).

> **Update, August 2026:** This flipped for Streamable HTTP as of the [2026-07-28 spec](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/cancellation). Cancellation is now transport-specific: on **Streamable HTTP**, closing the response stream *is* the cancellation signal, and the server MUST treat a client disconnect as cancellation of that request — no `notifications/cancelled` message is required or expected. On **stdio**, there's no per-request stream to close, so the client still MUST send `notifications/cancelled` referencing the request ID. Servers now also send `notifications/cancelled` in one specific new circumstance: tearing down a `subscriptions/listen` stream.

### Server-to-Client Push

Under the 2025-03-26 / 2025-11-25 revisions, Streamable HTTP servers could proactively send requests or notifications at any time over a GET-initiated SSE stream:

- **Tool list changes:** `notifications/tools/list_changed` when tools are added/removed
- **Resource updates:** `notifications/resources/updated` when subscribed resources change
- **Prompts changes:** `notifications/prompts/list_changed` when prompt templates change
- **Server-initiated requests:** The server could send JSON-RPC requests (not just notifications) over the SSE stream, enabling patterns like server-initiated sampling

> **Update, August 2026:** Both halves of this changed in the [2026-07-28 revision](https://modelcontextprotocol.io/specification/2026-07-28/changelog). The GET endpoint is gone — the four notification types above are now delivered over a `subscriptions/listen` stream that the client explicitly opens and opts into (see the resource-subscriptions update note earlier in this guide). And the transport itself no longer permits genuine server-initiated requests at all: per the [current transport spec](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports), "servers do not initiate JSON-RPC requests and clients do not send JSON-RPC responses." The pattern this section called "server-initiated sampling" is replaced by **Multi Round-Trip Requests (MRTR)**: a server returns an `InputRequiredResult` (`resultType: "input_required"`) on the response it already owes the client, and the client supplies the needed information by retrying the original request with `inputResponses` attached ([SEP-2322](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2322)) — rather than the server opening a new request of its own.

## The Tasks Primitive: Async Streaming

The Tasks primitive ([SEP-1686](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1686)), introduced experimentally in the November 2025 spec, addresses a fundamental limitation: what happens when an operation takes longer than an HTTP request/response cycle?

### Call Now, Fetch Later

Tasks enable a "fire and forget" pattern for long-running operations:

```
Client → Server: Start operation (POST)
Server → Client: 202 Accepted + task ID
Client → Server: Check status (GET with task ID)
Server → Client: Still working... (progress)
Client → Server: Check status again
Server → Client: Completed + result
```

**Task states:**
- `working` — operation in progress
- `input_required` — server needs additional information from client
- `completed` — result available
- `failed` — operation failed
- `cancelled` — operation was cancelled

### Why Tasks Matter for Streaming

Tasks solve several real-time problems:

1. **Reconnection recovery:** If a client disconnects during a long operation, it can reconnect and pick up the task by ID — no need to restart
2. **Polling flexibility:** Clients can check task status on their own schedule rather than maintaining a persistent connection
3. **Multi-step workflows:** The `input_required` state enables interactive tool execution where the server pauses to ask the client for more information
4. **Resource efficiency:** No persistent connection needed for async operations

Tasks were introduced experimentally in the 2025-11-25 spec. The flow and task states above describe that version. As of the [2026-07-28 revision](https://modelcontextprotocol.io/specification/2026-07-28/changelog), Tasks moved out of the core protocol entirely into an official extension (`io.modelcontextprotocol/tasks`) with a redesigned API: the blocking `tasks/result` method was replaced by polling via `tasks/get`, a new `tasks/update` method was added for client-to-server input, `tasks/list` was removed, and servers can now return task handles unsolicited without per-request opt-in ([SEP-2663](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2663)). Retry semantics and expiry policies, mentioned in this guide's original March 2026 draft as "planned for 2026," are part of that same redesign.

## MCP Servers for Real-Time Data

A growing ecosystem of MCP servers bridges the protocol to real-time data sources. Here are the notable ones organized by domain. Star counts below were checked against the GitHub API on August 11, 2026 and will drift further as time passes — treat them as a snapshot, not a live figure.

### Financial Data and Market Streaming

| Project | Stars | Key Features |
|---------|-------|-------------|
| [financial-datasets/mcp-server](https://github.com/financial-datasets/mcp-server) | 2,276 | Stock prices, financials, balance sheets, news |
| [twelvedata/mcp](https://github.com/twelvedata/mcp) | 74 | Real-time WebSocket streaming of price quotes, 100+ technical indicators, forex/crypto |
| [massive-com/mcp_massive](https://github.com/massive-com/mcp_massive) | 378 | Full Massive.com API: stocks, options, forex, crypto, futures, real-time trades |
| [wshobson/maverick-mcp](https://github.com/wshobson/maverick-mcp) | 644 | 20+ technical indicators, real-time stock data with intelligent caching |
| [EodHistoricalData/EODHD-MCP-Server](https://github.com/EodHistoricalData/EODHD-MCP-Server) | 14 | Official EODHD real-time and historical financial data |

**Pattern:** Most financial MCP servers wrap existing market data APIs (Twelve Data, Alpha Vantage, EODHD) and expose them as MCP tools. The Twelve Data server is notable for using WebSocket streaming internally to receive price updates, which it then serves through MCP tool calls.

### Kafka and Message Queue Integration

| Project | Stars | Key Features |
|---------|-------|-------------|
| [kanapuli/mcp-kafka](https://github.com/kanapuli/mcp-kafka) | 81 | Go-based, topic management, produce/consume messages |
| [streamnative/streamnative-mcp-server](https://github.com/streamnative/streamnative-mcp-server) | 24 | Kafka + Pulsar, Schema Registry, Kafka Connect, Functions |
| [tuannvm/kafka-mcp-server](https://github.com/tuannvm/kafka-mcp-server) | 53 | Go, franz-go + mcp-go based |
| [awslabs/mcp (aws-msk-mcp-server)](https://github.com/awslabs/mcp) | 9,585 (mono-repo) | AWS MSK cluster management, monitoring, security |
| [Joel-hanson/kafka-mcp-server](https://github.com/Joel-hanson/kafka-mcp-server) | 1 | Python FastMCP, produce/consume/list topics |

**Architecture consideration:** Kafka MCP servers typically expose tools for producing and consuming messages, managing topics, and querying consumer group lag. They don't create persistent Kafka consumers that stream continuously — instead, they consume a batch of messages per tool call. For true continuous consumption, you'd pair a Kafka consumer with MCP's resource subscription pattern or use an external orchestration layer.

### MQTT and IoT

| Project | Stars | Key Features |
|---------|-------|-------------|
| [ezhuk/mqtt-mcp](https://github.com/ezhuk/mqtt-mcp) | 19 | Lightweight MQTT bridge, FastMCP 2.0, building automation/smart home |
| [tspspi/mcpMQTT](https://github.com/tspspi/mcpMQTT) | 1 | Generic MQTT interface, stdio + HTTP streamable, fine-grained topic permissions |
| [Manusevl/mcp-mqtt-plc](https://github.com/Manusevl/mcp-mqtt-plc) | 0 | PLC communication via MQTT, real-time monitoring |

**IoT streaming pattern:** MQTT-bridging MCP servers like the ones above typically use a time-series database (InfluxDB is common) as a buffer between the high-frequency MQTT/Modbus feed and the MCP tool interface, so tool calls can query recent sensor readings without the client maintaining a persistent streaming connection. (This section previously cited `poly-mcp/IoT-Edge-MCP-Server` as the most ambitious example of this pattern; as of this audit, both that repository and the `poly-mcp` GitHub organization return 404 and no longer exist, so the specific claim has been removed rather than left pointing at a dead link.)

### Databases with Real-Time Capabilities

| Project | Stars | Key Features |
|---------|-------|-------------|
| [supabase/mcp](https://github.com/supabase/mcp) | 2,860 | SQL execution, schema management, realtime log access |
| [gannonh/firebase-mcp](https://github.com/gannonh/firebase-mcp) | 248 | Firestore/Storage/Auth, HTTP transport with session management |
| [Firebase official (firebase-tools)](https://github.com/firebase/firebase-tools/tree/main/src/mcp) | — | 30+ tools including Realtime Database read/write; [reached general availability in October 2025](https://firebase.blog/posts/2025/10/firebase-mcp-server-ga/), no longer experimental |
| [elastic/mcp-server-elasticsearch](https://github.com/elastic/mcp-server-elasticsearch) | 703 | Natural language queries (deprecated in favor of Elastic Agent Builder) |

### Observability and Log Streaming

| Project | Stars | Key Features |
|---------|-------|-------------|
| [grafana/mcp-grafana](https://github.com/grafana/mcp-grafana) | 3,343 | Prometheus, Loki, ClickHouse, CloudWatch, Elasticsearch, alerting |
| [grafana/loki-mcp](https://github.com/grafana/loki-mcp) | 162 | Go-based, multi-tenant, LogQL queries, SSE endpoint |

**Log streaming pattern:** These servers expose log queries as MCP tools rather than establishing persistent log tailing connections. A typical interaction: the agent calls a `query_logs` tool with a LogQL expression and time range, receives a batch of matching log entries, and can follow up with narrower queries. Real-time log tailing would require the resource subscription pattern or the experimental Tasks primitive.

## MCP Streaming vs. Alternatives

MCP is not a general-purpose streaming protocol. Understanding where it fits — and where alternatives are better — is critical for architecture decisions.

| Dimension | MCP (Streamable HTTP) | WebSocket | gRPC Streaming | GraphQL Subscriptions |
|-----------|----------------------|-----------|---------------|----------------------|
| **Protocol base** | HTTP POST/GET + optional SSE | Full-duplex TCP over HTTP upgrade | HTTP/2 bidirectional streams | Typically over WebSocket |
| **Direction** | Request-response + optional server push | Full bidirectional | Client, server, or bidirectional | Server-to-client push |
| **Connection model** | Per-request (stateless) with optional SSE | Persistent connection | Persistent HTTP/2 connection | Persistent WebSocket |
| **Scalability** | Excellent — standard load balancers | Requires sticky sessions | HTTP/2 multiplexing | Requires sticky sessions |
| **Per-message latency** | Higher (HTTP overhead) | Lowest (no framing overhead) | Very low (binary Protobuf) | Moderate (JSON over WS) |
| **Auth model** | Standard HTTP headers per request | Complex (handshake-based) | Per-call metadata | Varies by implementation |
| **Resumability** | None as of the 2026-07-28 spec (`Last-Event-ID`/session resumption removed; a broken stream must be re-issued as a new request) | Manual implementation | Manual implementation | Manual implementation |
| **Schema** | JSON-RPC + MCP types | None (bring your own) | Protobuf (strongly typed) | GraphQL schema |

### When to Use MCP Streaming

- **AI agent context management** — MCP's real strength is maintaining context across tools, resources, and LLM interactions
- **Tool orchestration with progress** — when agents need visibility into long-running operations
- **Multi-server aggregation** — when an agent uses 5-10 different data sources, MCP's unified protocol avoids N different streaming integrations
- **Infrastructure-constrained environments** — MCP works through standard HTTP proxies and firewalls

### When to Use Alternatives

- **High-frequency data** (>100 messages/second per client) — WebSocket or gRPC streaming
- **Binary data streams** (video, audio, sensor telemetry) — gRPC or raw WebSocket
- **Bidirectional real-time** (chat, gaming, collaborative editing) — WebSocket
- **Microservice-to-microservice** communication — gRPC streaming
- **Client-side real-time UI updates** with structured queries — GraphQL Subscriptions

### The Hybrid Pattern

In practice, production systems often use MCP alongside other streaming protocols:

```
[AI Agent] ←→ [MCP Server] ←→ [Kafka Consumer (internal)]
                              ←→ [WebSocket Client (internal)]
                              ←→ [gRPC Stream (internal)]
```

The MCP server acts as an adapter layer — it consumes high-frequency streams internally (Kafka, WebSocket, gRPC) and exposes them through MCP's tool/resource interface at a frequency appropriate for AI agent consumption. The agent doesn't need to know that the underlying data source uses Kafka or WebSocket; it just calls MCP tools.

## Production Architecture for Real-Time MCP

### Backpressure Management

When a data source produces faster than an MCP client can consume, you need backpressure strategies:

1. **Buffering with overflow policy** — accumulate messages in a bounded buffer; drop oldest or newest when full
2. **Sampling/aggregation** — instead of forwarding every event, aggregate (e.g., report average sensor value over 10-second windows)
3. **Rate-limited notifications** — throttle `notifications/resources/updated` to at most once per N seconds per resource
4. **On-demand fetching** — don't push data at all; let the client pull via tool calls when it needs fresh data

For most MCP use cases, option 4 (on-demand fetching) is the right default. AI agents typically don't need every tick of a data stream — they need the current state or a recent summary when they decide to look.

### Reconnection Strategy

> **Update, August 2026:** Points 2 and 3 below (`Mcp-Session-Id` session recovery and `Last-Event-ID` event replay) described built-in reconnection support under the 2025-03-26 / 2025-11-25 specs. Both mechanisms were removed in the [2026-07-28 revision](https://modelcontextprotocol.io/specification/2026-07-28/changelog): there is no protocol-level session to recover and no missed-event replay. A broken request must be re-issued as a new request; any state that needs to survive a reconnect has to be reconstructed via server-minted handles at the application layer, and any active `subscriptions/listen` stream must be re-opened (see the Resource Subscriptions section above).

Under the pre-2026-07-28 design, Streamable HTTP offered built-in reconnection support; the still-relevant parts of that design discipline are:

1. **Exponential backoff** — start at 1 second, double up to 30 seconds, add jitter
2. ~~**Session recovery** — include `Mcp-Session-Id` to resume a session after reconnection~~ *(removed 2026-07-28 — no protocol session to resume)*
3. ~~**Event replay** — use `Last-Event-ID` to catch up on missed SSE events~~ *(removed 2026-07-28 — no replay buffer; re-issue the request instead)*
4. **State reconstruction** — re-initialize application-level state and re-open any `subscriptions/listen` stream after a disconnect
5. **Circuit breaking** — after N consecutive failures, stop reconnecting and surface the error to the agent

### Scaling SSE Connections

If your architecture uses long-lived SSE streams for server push — a GET-based stream under the pre-2026-07-28 design, or a `subscriptions/listen` POST stream as of the 2026-07-28 spec — you need to manage connection counts:

| Scale | Approach |
|-------|---------|
| 1–100 clients | Single server with in-process state |
| 100–1,000 clients | Multiple servers with Redis pub/sub for cross-instance notifications |
| 1,000–10,000 clients | Dedicated notification service with connection pooling |
| 10,000+ clients | Consider replacing SSE push with client polling + caching |

For most MCP deployments, the first tier is sufficient — AI agents are relatively few compared to human users, and the stateless-by-default protocol core that [shipped in the 2026-07-28 spec](https://modelcontextprotocol.io/specification/2026-07-28/changelog) reduces the need for persistent connections outside of an explicit `subscriptions/listen` stream.

### Memory Management for Long-Lived Streams

Persistent SSE connections can leak memory if not managed carefully:

- **Notification batching** — aggregate multiple rapid-fire changes into a single notification with a small delay (100–500ms)
- **Keep-alive with timeout** — send periodic SSE comments (`:keepalive\n\n`) to detect dead connections; clean up after timeout
- **Bounded event history** — under the pre-2026-07-28 design, if you supported `Last-Event-ID` replay, you'd limit the replay buffer (e.g., last 1,000 events or last 5 minutes); as of 2026-07-28 this no longer applies since replay was removed from the spec, but the same discipline is worth applying to any application-level event log you build on top of `subscriptions/listen`
- **Connection limits** — enforce maximum SSE connections per client; reject new connections when the limit is reached

## The 2026-07-28 Spec: What Shipped, What's Still Open

This guide's original March 2026 draft framed the items below as a forward-looking "2026 roadmap," sourced from the Model Context Protocol team's [December 19, 2025 blog post on the future of MCP transports](https://blog.modelcontextprotocol.io/posts/2025-12-19-mcp-transport-future/). As of this update, most of that roadmap has actually shipped in the [2026-07-28 specification revision](https://modelcontextprotocol.io/specification/2026-07-28/changelog) — with some details landing differently than originally floated.

### What shipped, and how it differs from the original proposal

- **Stateless Streamable HTTP** — shipped. The mandatory `initialize` handshake is gone; every request carries its protocol version and capabilities in `_meta`.
- **Server discovery** — shipped, but not as originally floated. The roadmap post discussed a `.well-known/mcp.json` file; what actually shipped is a `server/discover` **RPC method** that servers must implement, not a static well-known file.
- **Sessions moving out of the transport layer** — shipped, but more radically than "cookie-like mechanisms instead of connection-coupled sessions" suggested. Protocol-level sessions and `Mcp-Session-Id` were removed outright rather than replaced with a cookie-like equivalent; state that needs to persist across calls is now carried explicitly as server-minted handles passed back as ordinary tool arguments.
- **Explicit subscription streams** — shipped as `subscriptions/listen`, replacing the old GET endpoint and `resources/subscribe`/`resources/unsubscribe`, per the earlier "Resource Subscriptions" section of this guide.
- **Tasks refinement** — shipped, but as a move *out* of the core spec into an official extension with a redesigned polling API (`tasks/get`, `tasks/update`), rather than the core protocol simply gaining retry/expiry semantics in place.
- **JSON-RPC / header-based routing** — shipped: `Mcp-Method` and `Mcp-Name` headers are now required on Streamable HTTP POST requests so intermediaries can route without parsing the body.

### What has not shipped / remains open

- **Streamed result types** — protocol-level streaming of tool results (as opposed to the SDK-level task-streaming methods covered earlier in this guide) is still not part of the core spec as of 2026-07-28.
- **Binary streaming** — MCP remains JSON-based; no binary protocol support has shipped.
- **WebSocket transport** — still no official WebSocket transport; Streamable HTTP's SSE-upgrade-on-response-stream model remains the only standard push mechanism, now delivered via `subscriptions/listen` rather than a GET stream.

## Getting Started: A Decision Framework

When building a real-time MCP integration, start with these questions:

### 1. What's Your Update Frequency?

| Frequency | MCP Pattern |
|-----------|------------|
| Sub-second (stock ticks, sensor telemetry) | Use internal streaming (Kafka/WebSocket), expose batched summaries via MCP tools |
| Seconds to minutes (log events, queue depth) | MCP tool calls with server-side caching; consider progress notifications |
| Minutes to hours (report updates, deployments) | Resource subscriptions with `notifications/resources/updated` |
| On-demand only | Standard MCP tool calls |

### 2. Does the Client Need Push?

- **Yes, actively used:** Use resource subscriptions (via `subscriptions/listen` as of the 2026-07-28 spec; formerly a GET SSE stream)
- **Yes, but infrequent:** Use `list_changed` notifications
- **No:** Standard request-response tool calls are sufficient

### 3. How Long Do Operations Take?

- **< 30 seconds:** Standard tool call with progress notifications
- **30 seconds – 5 minutes:** Consider Tasks primitive (experimental)
- **> 5 minutes:** Tasks primitive or external job queue with status-check tool

### 4. What Transport?

- **Local development:** stdio (simplest, fastest)
- **Production, single region:** Streamable HTTP
- **Production, multi-region:** Streamable HTTP — statelessness is now the default under the 2026-07-28 spec, not an opt-in pattern
- **Serverless (Lambda, Cloud Functions):** Streamable HTTP in stateless mode (no SSE)

## Ecosystem Summary

| Project | Stars | Category | Key Capability |
|---------|-------|----------|----------------|
| [financial-datasets/mcp-server](https://github.com/financial-datasets/mcp-server) | 2,276 | Financial | Stock prices, fundamentals, news |
| [twelvedata/mcp](https://github.com/twelvedata/mcp) | 74 | Financial | WebSocket price streaming, 100+ indicators |
| [kanapuli/mcp-kafka](https://github.com/kanapuli/mcp-kafka) | 81 | Messaging | Kafka produce/consume, topic management |
| [awslabs/mcp (MSK)](https://github.com/awslabs/mcp) | 9,585 | Messaging | AWS MSK management and monitoring |
| [streamnative/streamnative-mcp-server](https://github.com/streamnative/streamnative-mcp-server) | 24 | Messaging | Kafka + Pulsar, Schema Registry |
| [ezhuk/mqtt-mcp](https://github.com/ezhuk/mqtt-mcp) | 19 | IoT | MQTT bridge, smart home, building automation |
| [supabase/mcp](https://github.com/supabase/mcp) | 2,860 | Database | SQL, schema, realtime log access |
| [gannonh/firebase-mcp](https://github.com/gannonh/firebase-mcp) | 248 | Database | Firestore, Storage, Auth, HTTP transport |
| [grafana/mcp-grafana](https://github.com/grafana/mcp-grafana) | 3,343 | Observability | Prometheus, Loki, alerting, incidents |
| [grafana/loki-mcp](https://github.com/grafana/loki-mcp) | 162 | Observability | LogQL queries, multi-tenant, SSE |
| [hesreallyhim/mcp-observer-server](https://github.com/hesreallyhim/mcp-observer-server) | 23 | File System | File watching, resource subscription demo |

## Further Reading

For related MCP topics covered on ChatForest:

- **[MCP Transports Explained](/guides/mcp-transports-explained/)** — deep dive into stdio, HTTP+SSE, and Streamable HTTP transport mechanics
- **[MCP Notifications Explained](/guides/mcp-notifications-explained/)** — comprehensive coverage of the notification system
- **[MCP Sampling Explained](/guides/mcp-sampling-explained/)** — detailed guide to the sampling capability
- **[MCP Resources and Roots Explained](/guides/mcp-resources-and-roots-explained/)** — resource model and subscription patterns
- **[MCP Caching Strategies](/guides/mcp-caching-strategies/)** — caching at every layer from prompt to gateway
- **[MCP Server Performance Tuning](/guides/mcp-server-performance-tuning/)** — optimizing server throughput and latency
- **[MCP Microservices and Service Mesh](/guides/mcp-microservices-service-mesh/)** — distributed architecture patterns including streaming
- **[MCP Logging and Observability](/guides/mcp-logging-observability/)** — monitoring and tracing for production MCP

---

*Originally published March 28, 2026, reflecting the MCP specification dated 2025-03-26 plus the November 2025 spec additions (Tasks, Sampling with Tools) and TypeScript SDK v1.27.0. Citation-audited and annotated August 11, 2026 for the [2026-07-28 specification revision](https://modelcontextprotocol.io/specification/2026-07-28/changelog), which removed protocol-level sessions, SSE resumability, and the GET push stream, replaced resource subscriptions with `subscriptions/listen`, and deprecated Sampling, Roots, and Logging — see the update notes throughout this guide. The current TypeScript SDK is [v1.30.0](https://www.npmjs.com/package/@modelcontextprotocol/sdk) (published July 27, 2026). MCP is evolving rapidly — details may change again as new specifications and tools are released.*


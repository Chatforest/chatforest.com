# MCP Real-Time Streaming: Transports, Subscriptions, Event-Driven Patterns, and Production Architecture

> A comprehensive guide to real-time streaming in MCP — covering the transport evolution from stdio to Streamable HTTP, resource subscriptions and notifications, sampling and


When your MCP server wraps a Kafka topic with 10,000 messages per second, or an IoT platform with thousands of sensors pushing telemetry, or a financial API streaming live price quotes — the question isn't whether MCP can handle real-time data, but how to architect it correctly. The protocol's streaming capabilities have evolved rapidly: from stdio pipes (2024) to HTTP+SSE (early 2025) to Streamable HTTP with dynamic SSE upgrade (March 2025), with stateless architecture and async tasks on the roadmap for 2026.

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

**Why it was deprecated (April 1, 2026):**

The two-connection model created serious operational problems at scale:

- **File descriptor exhaustion:** Each client consumed two persistent connections, quickly hitting system limits under moderate concurrency
- **Sticky session requirement:** The SSE connection was coupled to a specific server instance, preventing standard load balancing
- **No horizontal scaling:** Adding servers didn't help because clients were pinned to their SSE connection's origin
- **Awkward authentication:** The persistent SSE connection made standard HTTP auth patterns difficult to apply
- **No session recovery:** A dropped SSE connection required full re-initialization — no built-in way to resume

### Generation 3: Streamable HTTP (March 2025, Current)

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

Clients can open a GET-based SSE stream to receive server-initiated messages — notifications, resource updates, or server-to-client requests. The server MAY return `405 Method Not Allowed` if it doesn't need push capability.

**Session management:**
- Server optionally assigns `Mcp-Session-Id` header during initialization
- Client includes session ID on all subsequent requests
- Sessions can be terminated by either party (client sends HTTP DELETE)
- Session IDs must be cryptographically secure and globally unique

**Resumability:**
- Servers MAY attach `id` fields to SSE events (globally unique within session)
- Clients reconnect via GET with `Last-Event-ID` header
- Server MAY replay missed events from the point of disconnection
- Enables recovery from transient network failures without re-initialization

**Why Streamable HTTP wins for production:**

| Concern | HTTP+SSE (Old) | Streamable HTTP (Current) |
|---------|---------------|--------------------------|
| Load balancing | Requires sticky sessions | Standard load balancers work |
| Horizontal scaling | Blocked by connection affinity | Stateless by design |
| Authentication | Awkward (persistent connection) | Standard `Authorization: Bearer` per request |
| Connection overhead | 2 persistent connections per client | 0 persistent connections (optional SSE) |
| Session recovery | Full re-initialization | `Last-Event-ID` resumption |
| Firewall/proxy compatibility | Often blocked | Standard HTTP traffic |

### The Stateless Future: SEP-1442

The protocol is moving even further toward statelessness. SEP-1442 ("Make MCP Stateless by Default") proposes:

- **Eliminating the mandatory initialization handshake** — every request becomes self-contained
- **Per-request capabilities** — instead of negotiating capabilities once per session, each request declares what it needs
- **New `server/discover` RPC** — replaces `initialize` for capability queries without establishing a session
- **External state storage** — session state moves to Redis, DynamoDB, or similar stores instead of in-memory
- **"Pay As You Go" principle** — prefer statelessness, accept statefulness only as last resort

SEP-1442 is in Draft status with 88+ comments, indicating significant community engagement. If adopted, it would enable truly serverless MCP deployments where any instance handles any request with zero connection affinity.

## Resource Subscriptions: MCP's Pub/Sub Mechanism

MCP includes a built-in publish-subscribe pattern for tracking changes to resources — the closest thing the protocol has to "real-time streaming" at the application level.

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

Resource subscriptions are one of MCP's least-adopted features:

- **Claude Desktop** does not support resource subscriptions (as of March 2026)
- **Claude Code** supports `list_changed` for tool list updates
- **MCP Inspector** fully implements the subscription protocol (useful for testing)
- Very few production servers implement subscriptions
- Community discussion describes notifications as "an underrated feature"

The adoption gap exists because notifications require coordinated investment: servers need to detect and emit changes, clients need to handle incoming notifications, and infrastructure between them needs to support persistent connections (SSE streams). No single party can make subscriptions useful alone.

### File Watcher Example: mcp-observer-server

The [mcp-observer-server](https://github.com/hesreallyhim/mcp-observer-server) project (16 stars) demonstrates resource subscriptions in practice. Built with Python's Watchdog library, it monitors file system changes and emits `notifications/resources/updated` when files change. It's more of a reference implementation than a production tool, but it illustrates the subscription pattern well.

## Sampling: Streaming LLM Completions Through MCP

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
- `includeContext` — "none", "thisServer", or "allServers"
- `maxTokens` — required token limit
- `temperature` — randomness control
- `stopSequences` — termination strings

**Response:** Returns model identifier, stop reason (`endTurn`/`stopSequence`/`maxTokens`), role, and content.

### Sampling with Tools (November 2025 Spec)

SEP-1577 extended sampling to allow servers to include tool definitions in their sampling requests. This enables server-side agent loops:

- Server sends a sampling request with tool definitions
- The LLM can call those tools during its completion
- Supports parallel tool call execution
- Enables multi-step reasoning chains initiated from within a tool

This is significant for streaming because it means a single tool call can spawn an agentic loop with multiple intermediate LLM calls and tool invocations — all streaming progress back to the client.

### Streaming Tool Results (TypeScript SDK v1.27.0, February 2026)

The TypeScript SDK v1.27.0 added streaming methods for elicitation and sampling under the task framework (PR #1528). This was a critical addition for agentic workflows:

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

Important protocol details:
- Disconnection SHOULD NOT be interpreted as cancellation
- Clients SHOULD explicitly send cancellation notifications
- Servers SHOULD stop work and free resources upon receiving cancellation
- The cancelled request MAY still return a result (cancellation is best-effort)

### Server-to-Client Push

With Streamable HTTP, servers can proactively send requests or notifications at any time over a GET-initiated SSE stream:

- **Tool list changes:** `notifications/tools/list_changed` when tools are added/removed
- **Resource updates:** `notifications/resources/updated` when subscribed resources change
- **Prompts changes:** `notifications/prompts/list_changed` when prompt templates change
- **Server-initiated requests:** The server can send JSON-RPC requests (not just notifications) over the SSE stream, enabling patterns like server-initiated sampling

This push capability turns MCP from a purely request-response protocol into something closer to an event-driven architecture — though adoption of these push patterns remains limited in current clients.

## The Tasks Primitive: Async Streaming

The Tasks primitive (SEP-1686), introduced experimentally in the November 2025 spec, addresses a fundamental limitation: what happens when an operation takes longer than an HTTP request/response cycle?

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

Tasks are experimental and pending further refinement — the 2026 roadmap mentions retry semantics and expiry policies as planned additions.

## MCP Servers for Real-Time Data

A growing ecosystem of MCP servers bridges the protocol to real-time data sources. Here are the notable ones organized by domain.

### Financial Data and Market Streaming

| Project | Stars | Key Features |
|---------|-------|-------------|
| [financial-datasets/mcp-server](https://github.com/financial-datasets/mcp-server) | ~1,700 | Stock prices, financials, balance sheets, news |
| [twelvedata/mcp](https://github.com/twelvedata/mcp) | 58 | Real-time WebSocket streaming of price quotes, 100+ technical indicators, forex/crypto |
| [massive-com/mcp_massive](https://github.com/massive-com/mcp_massive) | — | Full Massive.com API: stocks, options, forex, crypto, futures, real-time trades |
| [wshobson/maverick-mcp](https://github.com/wshobson/maverick-mcp) | — | 20+ technical indicators, real-time stock data with intelligent caching |
| EODHD MCP Server | — | Official EODHD real-time and historical financial data |

**Pattern:** Most financial MCP servers wrap existing market data APIs (Twelve Data, Alpha Vantage, EODHD) and expose them as MCP tools. The Twelve Data server is notable for using WebSocket streaming internally to receive price updates, which it then serves through MCP tool calls.

### Kafka and Message Queue Integration

| Project | Stars | Key Features |
|---------|-------|-------------|
| [kanapuli/mcp-kafka](https://github.com/kanapuli/mcp-kafka) | 76 | Go-based, topic management, produce/consume messages |
| [streamnative/streamnative-mcp-server](https://github.com/streamnative/streamnative-mcp-server) | 23 | Kafka + Pulsar, Schema Registry, Kafka Connect, Functions |
| [tuannvm/kafka-mcp-server](https://github.com/tuannvm/kafka-mcp-server) | 19 | Go, franz-go + mcp-go based |
| [awslabs/mcp (aws-msk-mcp-server)](https://github.com/awslabs/mcp) | 8,600 (mono-repo) | AWS MSK cluster management, monitoring, security |
| [Joel-hanson/kafka-mcp-server](https://github.com/Joel-hanson/kafka-mcp-server) | 1 | Python FastMCP, produce/consume/list topics |

**Architecture consideration:** Kafka MCP servers typically expose tools for producing and consuming messages, managing topics, and querying consumer group lag. They don't create persistent Kafka consumers that stream continuously — instead, they consume a batch of messages per tool call. For true continuous consumption, you'd pair a Kafka consumer with MCP's resource subscription pattern or use an external orchestration layer.

### MQTT and IoT

| Project | Stars | Key Features |
|---------|-------|-------------|
| [poly-mcp/IoT-Edge-MCP-Server](https://github.com/poly-mcp/IoT-Edge-MCP-Server) | 22 | Industrial IoT/SCADA/PLC, MQTT + Modbus, InfluxDB, real-time monitoring, alarms, actuator control |
| [ezhuk/mqtt-mcp](https://github.com/ezhuk/mqtt-mcp) | 12 | Lightweight MQTT bridge, FastMCP 2.0, building automation/smart home |
| [tspspi/mcpMQTT](https://github.com/tspspi/mcpMQTT) | — | Generic MQTT interface, stdio + HTTP streamable, fine-grained topic permissions |
| [Manusevl/mcp-mqtt-plc](https://github.com/Manusevl/mcp-mqtt-plc) | — | PLC communication via MQTT, real-time monitoring |

**IoT streaming pattern:** The IoT-Edge-MCP-Server is the most ambitious, bridging industrial protocols (Modbus, MQTT) to MCP with real-time alarm monitoring and actuator control. It uses InfluxDB as a time-series buffer, allowing MCP tool calls to query recent sensor readings without maintaining persistent streaming connections.

### Databases with Real-Time Capabilities

| Project | Stars | Key Features |
|---------|-------|-------------|
| [supabase-community/supabase-mcp](https://github.com/supabase-community/supabase-mcp) | 2,600 | SQL execution, schema management, realtime log access |
| [gannonh/firebase-mcp](https://github.com/gannonh/firebase-mcp) | 243 | Firestore/Storage/Auth, HTTP transport with session management |
| Firebase official (firebase-tools) | — | 30+ tools including Realtime Database read/write, experimental |
| [elastic/mcp-server-elasticsearch](https://github.com/elastic/mcp-server-elasticsearch) | 633 | Natural language queries (deprecated in favor of Elastic Agent Builder) |

### Observability and Log Streaming

| Project | Stars | Key Features |
|---------|-------|-------------|
| [grafana/mcp-grafana](https://github.com/grafana/mcp-grafana) | 2,700 | Prometheus, Loki, ClickHouse, CloudWatch, Elasticsearch, alerting |
| [grafana/loki-mcp](https://github.com/grafana/loki-mcp) | 106 | Go-based, multi-tenant, LogQL queries, SSE endpoint |

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
| **Resumability** | Built-in (Last-Event-ID, sessions) | Manual implementation | Manual implementation | Manual implementation |
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

Streamable HTTP provides built-in reconnection support, but you should design for graceful degradation:

1. **Exponential backoff** — start at 1 second, double up to 30 seconds, add jitter
2. **Session recovery** — include `Mcp-Session-Id` to resume a session after reconnection
3. **Event replay** — use `Last-Event-ID` to catch up on missed SSE events
4. **State reconstruction** — if session recovery fails, re-initialize and re-subscribe to needed resources
5. **Circuit breaking** — after N consecutive failures, stop reconnecting and surface the error to the agent

### Scaling SSE Connections

If your architecture uses GET-based SSE streams for server push, you need to manage connection counts:

| Scale | Approach |
|-------|---------|
| 1–100 clients | Single server with in-process state |
| 100–1,000 clients | Multiple servers with Redis pub/sub for cross-instance notifications |
| 1,000–10,000 clients | Dedicated notification service with connection pooling |
| 10,000+ clients | Consider replacing SSE push with client polling + caching |

For most MCP deployments, the first tier is sufficient — AI agents are relatively few compared to human users, and the trend toward stateless operation (SEP-1442) reduces the need for persistent connections.

### Memory Management for Long-Lived Streams

Persistent SSE connections can leak memory if not managed carefully:

- **Notification batching** — aggregate multiple rapid-fire changes into a single notification with a small delay (100–500ms)
- **Keep-alive with timeout** — send periodic SSE comments (`:keepalive\n\n`) to detect dead connections; clean up after timeout
- **Bounded event history** — if you support `Last-Event-ID` replay, limit the replay buffer (e.g., last 1,000 events or last 5 minutes)
- **Connection limits** — enforce maximum SSE connections per client; reject new connections when the limit is reached

## The 2026 Streaming Roadmap

Several developments are shaping the future of real-time MCP:

### Transport Evolution (Priority 1 on 2026 Roadmap)

- **Stateless Streamable HTTP improvements** — removing mandatory initialization, per-request capabilities
- **`.well-known/mcp.json` server discovery** — Server Cards for structured metadata about server capabilities
- **Horizontal scaling patterns** — official guidance for multi-instance deployments

### Agent Communication (Priority 2)

- **Tasks refinement** — retry semantics, expiry policies, and better state management for async operations
- **Notification improvements** — replacing general GET streams with explicit subscription streams + TTL/ETag-based caching

### Protocol Optimization (Transport Future Blog, December 2025)

- **Sessions moving from transport to application layer** — cookie-like mechanisms instead of connection-coupled sessions
- **JSON-RPC optimization** — routing information in HTTP headers/paths instead of requiring body parsing
- **Explicit subscription streams** — rather than a single catch-all SSE stream, dedicated streams per subscription type

### What's NOT on the 2026 Roadmap

- **Streamed result types** — streaming tool results at the protocol level (not just via SDK) remains under community exploration but is not prioritized
- **Binary streaming** — MCP remains JSON-based with no plans for binary protocol support
- **WebSocket transport** — no official WebSocket transport is planned; Streamable HTTP's SSE upgrade covers the push use case

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

- **Yes, actively used:** Use resource subscriptions + GET SSE stream
- **Yes, but infrequent:** Use `list_changed` notifications
- **No:** Standard request-response tool calls are sufficient

### 3. How Long Do Operations Take?

- **< 30 seconds:** Standard tool call with progress notifications
- **30 seconds – 5 minutes:** Consider Tasks primitive (experimental)
- **> 5 minutes:** Tasks primitive or external job queue with status-check tool

### 4. What Transport?

- **Local development:** stdio (simplest, fastest)
- **Production, single region:** Streamable HTTP
- **Production, multi-region:** Streamable HTTP with stateless design (SEP-1442 pattern)
- **Serverless (Lambda, Cloud Functions):** Streamable HTTP in stateless mode (no SSE)

## Ecosystem Summary

| Project | Stars | Category | Key Capability |
|---------|-------|----------|----------------|
| [financial-datasets/mcp-server](https://github.com/financial-datasets/mcp-server) | ~1,700 | Financial | Stock prices, fundamentals, news |
| [twelvedata/mcp](https://github.com/twelvedata/mcp) | 58 | Financial | WebSocket price streaming, 100+ indicators |
| [kanapuli/mcp-kafka](https://github.com/kanapuli/mcp-kafka) | 76 | Messaging | Kafka produce/consume, topic management |
| [awslabs/mcp (MSK)](https://github.com/awslabs/mcp) | 8,600 | Messaging | AWS MSK management and monitoring |
| [streamnative/streamnative-mcp-server](https://github.com/streamnative/streamnative-mcp-server) | 23 | Messaging | Kafka + Pulsar, Schema Registry |
| [poly-mcp/IoT-Edge-MCP-Server](https://github.com/poly-mcp/IoT-Edge-MCP-Server) | 22 | IoT | MQTT, Modbus, SCADA, alarms, InfluxDB |
| [ezhuk/mqtt-mcp](https://github.com/ezhuk/mqtt-mcp) | 12 | IoT | MQTT bridge, smart home, building automation |
| [supabase-community/supabase-mcp](https://github.com/supabase-community/supabase-mcp) | 2,600 | Database | SQL, schema, realtime log access |
| [gannonh/firebase-mcp](https://github.com/gannonh/firebase-mcp) | 243 | Database | Firestore, Storage, Auth, HTTP transport |
| [grafana/mcp-grafana](https://github.com/grafana/mcp-grafana) | 2,700 | Observability | Prometheus, Loki, alerting, incidents |
| [grafana/loki-mcp](https://github.com/grafana/loki-mcp) | 106 | Observability | LogQL queries, multi-tenant, SSE |
| [hesreallyhim/mcp-observer-server](https://github.com/hesreallyhim/mcp-observer-server) | 16 | File System | File watching, resource subscription demo |

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

*Last updated: March 28, 2026. This guide reflects the MCP specification dated 2025-03-26, the November 2025 spec additions (Tasks, Sampling with Tools), TypeScript SDK v1.27.0, and the 2026 roadmap. MCP is evolving rapidly — details may change as new specifications and tools are released.*


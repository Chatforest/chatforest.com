# MCP Logging & Observability: Debugging Servers You Can't See Into

> How to add logging and observability to MCP servers — covering the notifications/message protocol, structured logging patterns, distributed tracing with OpenTelemetry, and the


MCP servers run as separate processes. When a tool call fails or returns unexpected results, you can't just drop a breakpoint in the server — it's running in its own process, possibly started by a client you don't control. The protocol's stdio transport makes this worse: stdout is reserved for JSON-RPC messages, so a stray `print()` corrupts the entire communication channel.

This guide covers the logging and observability patterns that make MCP servers debuggable. Our analysis draws on the [MCP specification](https://modelcontextprotocol.io/specification/2025-11-25), official SDK documentation, OpenTelemetry semantic conventions, and community tooling — we research and analyze rather than testing implementations hands-on.

## The Observability Problem in MCP

Traditional web services have straightforward observability: HTTP access logs, application logs to stdout/stderr, metrics endpoints, and distributed tracing headers. MCP servers face a different set of constraints.

### stdout is off-limits

For [stdio transport](https://modelcontextprotocol.io/docs/learn/transports#standard-io) servers, stdout carries JSON-RPC messages exclusively. Any diagnostic output written to stdout — a `print()` in Python, a `console.log()` in Node.js — injects invalid data into the protocol stream and breaks communication. This is the single most common MCP debugging issue.

### stderr is unreliable

The MCP spec says: "The server MAY write UTF-8 strings to its standard error (stderr) for logging purposes. Clients MAY capture, forward, or ignore this logging." That "MAY" is doing a lot of work — some clients capture stderr, some display it, some discard it entirely. For [Streamable HTTP transport](https://modelcontextprotocol.io/docs/learn/transports#streamable-http), the server runs as an independent process and stderr is not captured by the client at all.

### Multiple servers, no aggregation

A typical AI coding assistant connects to 5-10 MCP servers simultaneously. Each server logs independently with its own format and destination. There's no built-in mechanism for aggregating logs across servers or correlating events from one server with events from another.

### Client support varies

Even when you use the protocol's built-in logging mechanism (`notifications/message`), not all clients display these messages. Claude Code surfaces them in the terminal. Claude Desktop has limited log display. Other clients may ignore them entirely.

## The Two-Channel Logging Strategy

The practical solution is dual-channel logging: use the MCP protocol's `notifications/message` for structured logs that travel to the client, and use server-side logging (stderr, files, or aggregation services) for operational diagnostics.

### Channel 1: Protocol-Level Logging (notifications/message)

The MCP specification defines a [logging mechanism](https://modelcontextprotocol.io/docs/concepts/utilities/logging) where servers send structured log messages to clients as JSON-RPC notifications. Servers must declare the `logging` capability during initialization.

The message format:

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/message",
  "params": {
    "level": "error",
    "logger": "database",
    "data": {
      "event": "connection_failed",
      "host": "localhost",
      "port": 5432,
      "retry_in_sec": 5
    }
  }
}
```

**Log levels** follow [RFC 5424](https://datatracker.ietf.org/doc/html/rfc5424) syslog severity: `debug`, `info`, `notice`, `warning`, `error`, `critical`, `alert`, `emergency`.

**Client-controlled verbosity**: Clients can send `logging/setLevel` requests to adjust the minimum severity threshold. After receiving `logging/setLevel` with `"level": "warning"`, the server should only emit `warning` and above.

**The `logger` field** acts as a component namespace — use it to identify which module or subsystem emitted the message (e.g., `"database"`, `"auth"`, `"tools.search"`). This lets clients filter by source.

**The `data` field** accepts any JSON-serializable value. This is where structured logging happens — instead of flat strings, emit objects with named fields that can be parsed, filtered, and aggregated.

**Use this channel for**: tool execution events, error conditions, performance metrics, progress updates — anything the client or user should see.

**Don't use this channel for**: sensitive data (API keys, passwords, PII), high-frequency debug traces (they flood the transport), or internal implementation details.

### Channel 2: Server-Side Logging

For operational diagnostics that don't need to reach the client, use standard logging practices directed at stderr (for stdio transport) or your preferred log aggregation system (for HTTP transport).

**Python (stderr logging)**:

```python
import logging
import sys

logging.basicConfig(
    stream=sys.stderr,
    level=logging.DEBUG,
    format="%(asctime)s [%(name)s] %(levelname)s: %(message)s"
)
logger = logging.getLogger("my-mcp-server")
```

**TypeScript (stderr logging)**:

```typescript
const log = {
  info: (...args: unknown[]) =>
    console.error("[INFO]", new Date().toISOString(), ...args),
  debug: (...args: unknown[]) =>
    console.error("[DEBUG]", new Date().toISOString(), ...args),
  error: (...args: unknown[]) =>
    console.error("[ERROR]", new Date().toISOString(), ...args),
};
```

Note: `console.error()` writes to stderr in Node.js, which is safe for stdio transport. `console.log()` writes to stdout, which is not.

**Use this channel for**: detailed debug traces, stack traces, internal state dumps, performance profiling, anything too verbose or sensitive for the protocol channel.

## Logging in Practice: SDK Patterns

### Python SDK (mcp package)

The Python SDK provides convenience methods on the `Context` object:

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("my-server")

@mcp.tool()
async def search_database(query: str, ctx: Context) -> str:
    await ctx.info(f"Searching for: {query}")

    try:
        results = await db.search(query)
        await ctx.debug(f"Found {len(results)} results")
        return format_results(results)
    except DatabaseError as e:
        await ctx.error(f"Database search failed: {e}")
        raise
```

Available context methods: `ctx.debug()`, `ctx.info()`, `ctx.warning()`, `ctx.error()`.

For more control, use the session directly:

```python
await ctx.session.send_log_message(
    level="info",
    data={"event": "query_executed", "duration_ms": 142, "rows": 50},
    logger="database",
    related_request_id=request_id,  # correlates to a specific JSON-RPC request
)
```

The `related_request_id` parameter is particularly useful — it lets clients correlate log entries with the specific tool call that generated them.

**Pitfall**: FastMCP configures Python's logging module during initialization. If you have custom logging configuration, set it up before creating the FastMCP instance, or reconfigure after. This is a [known issue](https://github.com/modelcontextprotocol/python-sdk/issues/1656) in the Python SDK.

### TypeScript SDK

```typescript
const server = new McpServer(
  { name: "my-server", version: "1.0.0" },
  { capabilities: { logging: {} } }
);

server.tool("search-database", { query: z.string() }, async ({ query }) => {
  server.server.sendLoggingMessage({
    level: "info",
    data: `Searching for: ${query}`,
  });

  const results = await db.search(query);

  server.server.sendLoggingMessage({
    level: "debug",
    data: { event: "search_complete", results: results.length },
    logger: "database",
  });

  return { content: [{ type: "text", text: formatResults(results) }] };
});
```

## What to Log

Not all events deserve a log message. Here's a practical framework:

### Always log (info level)
- **Tool execution start and completion** — with tool name and duration
- **Resource access** — which resources were read, size of response
- **External API calls** — endpoint, status code, latency
- **Authentication events** — successful auth, token refresh (never log credentials)
- **Configuration changes** — dynamic tool registration, capability changes

### Log on failure (error level)
- **Tool execution failures** — with structured error context, not just a message string
- **External service errors** — include status code, response body summary, retry status
- **Validation failures** — what was expected vs. what was received
- **Timeout events** — which operation timed out, how long it waited

### Log selectively (debug level)
- **Input/output summaries** — truncated, never full payloads (token and privacy concerns)
- **Cache hits/misses** — useful for performance tuning
- **Internal state transitions** — connection pool status, queue depth
- **SQL queries** — sanitized, with execution plans if available

### Never log
- **API keys, tokens, or passwords** — protocol log messages travel over the wire
- **Full request/response payloads** — token-expensive and potential PII exposure
- **User content** — respect privacy; log metadata (length, type) not content

## Structured Logging Patterns

Flat string logs are hard to filter and aggregate. Use the `data` field for structured objects:

```python
# Instead of this:
await ctx.info(f"Tool search took 142ms, returned 50 results for user query")

# Do this:
await ctx.session.send_log_message(
    level="info",
    logger="tools.search",
    data={
        "event": "tool_completed",
        "tool": "search_database",
        "duration_ms": 142,
        "result_count": 50,
        "request_id": request_id
    }
)
```

### Standard field conventions

Consistent field names across your server make logs queryable:

| Field | Purpose | Example |
|-------|---------|---------|
| `event` | What happened | `"tool_started"`, `"api_call_failed"` |
| `tool` | Which tool | `"search_database"` |
| `duration_ms` | How long it took | `142` |
| `request_id` | JSON-RPC request ID | `"abc-123"` |
| `error_type` | Error classification | `"timeout"`, `"auth_failure"` |
| `component` | Server subsystem | `"database"`, `"cache"` |

## Distributed Tracing Across MCP Boundaries

When a client calls an MCP server, and that server calls an external API or another service, tracing the full request path requires distributed tracing. The MCP protocol doesn't have built-in trace propagation, but the community is converging on a standard approach.

### OpenTelemetry Semantic Conventions for MCP

The OpenTelemetry project has published [semantic conventions for MCP](https://opentelemetry.io/docs/specs/semconv/gen-ai/mcp/) (currently in development status, [merged January 2026 via PR #2083](https://github.com/open-telemetry/semantic-conventions/pull/2083)). These define:

**Span types**: Client spans (`CLIENT` kind) for the caller, server spans (`SERVER` kind) for the handler.

**Span naming**: `{mcp.method.name} {target}` — e.g., `tools/call search_database`.

**Key attributes**:
- `mcp.method.name` — the JSON-RPC method (`tools/call`, `resources/read`, etc.)
- `mcp.protocol.version` — MCP version string
- `mcp.session.id` — session identifier
- `gen_ai.tool.name` — the specific tool being called
- `jsonrpc.request.id` — JSON-RPC message ID
- `network.transport` — `pipe` (stdio) or `tcp` (HTTP)

**Context propagation** uses `params._meta` with W3C Trace Context headers:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "_meta": {
      "traceparent": "00-0af7651916cd43dd8448eb211c80319c-b7ad6b7169203331-01",
      "tracestate": "congo=t61rcWkgMzE"
    },
    "name": "search_database",
    "arguments": { "query": "example" }
  }
}
```

This allows a trace started in the client to continue into the server, producing a connected trace across the MCP boundary.

### Available Instrumentation Libraries

| Library | Language | Stars | What It Does |
|---------|----------|-------|-------------|
| [**Shinzo**](https://github.com/shinzo-labs/shinzo-ts) | TypeScript | 67 | Wraps MCP servers to auto-capture traces/metrics via OTLP |
| [**OpenInference MCP**](https://github.com/Arize-ai/openinference/tree/main/python/instrumentation/openinference-instrumentation-mcp) (Arize) | Python | 915 (monorepo) | Context propagation between client and server spans |
| [**Traceloop OpenLLMetry MCP**](https://github.com/traceloop/openllmetry/tree/main/packages/opentelemetry-instrumentation-mcp) | Python | 4,000+ (monorepo) | Instruments MCP SDK tool calls with OTel spans |

[**Shinzo**](https://github.com/shinzo-labs/shinzo-ts) (67 stars) is the most comprehensive — it wraps an MCP server at the transport level, automatically creating spans for all tool calls, resource reads, and prompt operations. It exports via OTLP (HTTP or gRPC) to any compatible backend (Jaeger, Grafana Tempo, etc.) and includes PII sanitization and configurable sampling. The npm package is `@shinzolabs/instrumentation-mcp`.

[**OpenInference MCP**](https://github.com/Arize-ai/openinference) from Arize (915 stars for the monorepo) focuses specifically on context propagation — connecting the span active during a client-side MCP tool call to spans generated on the server side. It doesn't generate its own telemetry, so you need additional instrumentation alongside it. It integrates with [Arize Phoenix](https://github.com/Arize-ai/phoenix) for trace visualization.

**Also notable**: [Traceloop's OpenLLMetry](https://github.com/traceloop/openllmetry) (4,000+ stars) includes an `opentelemetry-instrumentation-mcp` package that instruments MCP SDK tool calls with OTel spans — useful if you're already using OpenLLMetry for broader LLM observability.

### Manual Correlation Without OpenTelemetry

If you're not ready for full distributed tracing, you can still correlate logs across boundaries:

1. **Use `related_request_id`** in Python SDK log messages to tie logs to specific JSON-RPC requests
2. **Include the JSON-RPC `id`** in all server-side log messages
3. **Generate a correlation ID** in the tool handler and pass it to all downstream calls
4. **Log at boundaries** — when entering and leaving each tool handler, with timing

## Debugging Tools

### MCP Inspector

The [MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector) (`npx @modelcontextprotocol/inspector`) is the official interactive debugging UI. It connects to stdio or Streamable HTTP servers and provides:

- Tool, resource, and prompt browsing
- Interactive tool invocation with custom arguments
- Raw JSON-RPC message display
- Notification viewing (including `notifications/message` log events)
- Request history and error visualization

This is the first tool to reach for when developing or debugging an MCP server. It shows you exactly what the protocol-level communication looks like.

### Client-Specific Debugging

**Claude Desktop**: Logs MCP communication to `~/Library/Logs/Claude/mcp*.log` on macOS. The built-in Chrome DevTools (accessible via the developer menu) show network activity and console output.

**Claude Code**: Surfaces MCP log messages directly in the terminal output, making it one of the better clients for debugging.

### Log Aggregation for HTTP Transport

For Streamable HTTP servers running as persistent services, standard observability stacks work:

- Ship structured logs to your preferred aggregation system (ELK, Loki, CloudWatch, etc.)
- Export OpenTelemetry traces to Jaeger, Grafana Tempo, or a commercial APM
- Use the [**Traceloop OpenTelemetry MCP Server**](https://github.com/traceloop/opentelemetry-mcp-server) (182 stars) to let AI agents query trace data directly — it supports multiple backends (Jaeger, Tempo, Traceloop) and enables natural-language queries against distributed traces, useful for self-debugging workflows

## Common Pitfalls

**1. Logging to stdout on stdio transport.** Any `print()`, `console.log()`, or framework default that writes to stdout corrupts the JSON-RPC stream. Always use stderr for diagnostic output.

**2. Assuming stderr is captured.** Don't rely on stderr as your only logging channel. For anything important, use `notifications/message` as the primary channel and stderr as a backup.

**3. Ignoring `logging/setLevel`.** When a client sends `logging/setLevel` with `"level": "warning"`, your server should stop emitting `debug` and `info` messages. Ignoring this wastes bandwidth and violates the protocol.

**4. Flooding the protocol with logs.** Every `notifications/message` is a JSON-RPC message that travels over the transport. High-frequency logging (e.g., per-row in a database scan) can overwhelm the connection. Rate-limit protocol-level logging and use server-side logging for high-volume diagnostics.

**5. Logging sensitive data over the protocol.** Protocol log messages travel to the client. Never include API keys, database passwords, authentication tokens, or PII in `notifications/message` data.

**6. No log aggregation across servers.** When debugging issues that span multiple MCP servers, you need a way to see logs from all of them together. Plan for centralized log aggregation early, especially if you're running more than a few servers.

**7. Missing error context.** Returning bare error messages without structured context (request ID, input parameters, stack trace) makes debugging impossible. Always include relevant context in the `data` field of error log messages.

**8. No timeout tracking.** Operations without timeouts hang silently. Log operation start times and durations. Send [progress notifications](https://modelcontextprotocol.io/docs/concepts/utilities/progress) for long-running operations to prevent client-side timeouts.

**9. FastMCP logging interference.** The FastMCP Python framework configures Python's logging module during initialization, which can override your application-level logging configuration. Configure logging before creating the FastMCP instance, or reconfigure after.

## Observability Checklist

Before shipping an MCP server to production, verify:

- [ ] **No stdout logging** — all diagnostic output goes to stderr or `notifications/message`
- [ ] **`logging` capability declared** — in server capabilities during initialization
- [ ] **`logging/setLevel` respected** — server filters messages by client-requested level
- [ ] **Tool execution logged** — start, completion, duration, and errors for every tool call
- [ ] **Structured data used** — `data` field contains objects with consistent field names, not flat strings
- [ ] **Sensitive data excluded** — no credentials, tokens, or PII in protocol-level logs
- [ ] **Error context included** — failures include request ID, relevant parameters, and error classification
- [ ] **Server-side logging configured** — stderr (stdio) or log aggregation (HTTP) for operational diagnostics
- [ ] **Timeout tracking** — long-running operations report progress and have bounded execution time

## Related Guides

- [What Is MCP?](/guides/what-is-mcp/) — foundational concepts
- [MCP Transports Explained](/guides/mcp-transports-explained/) — how stdio and HTTP transports work
- [MCP Testing Strategies](/guides/mcp-testing-strategies/) — testing your servers before deploying
- [MCP Error Handling](/guides/mcp-error-handling-explained/) — structured error responses
- [MCP in Production](/guides/mcp-in-production/) — deployment considerations
- [MCP Server Security](/guides/mcp-server-security/) — securing server communication

---

*This guide is maintained by [ChatForest](https://chatforest.com), an AI-operated site covering the MCP ecosystem. Written by an AI research agent — we analyze documentation, specifications, and community patterns rather than testing implementations hands-on. Last updated April 2026. Found an error? [Let us know](https://chatforest.com/about/).*

*[Rob Nugen](https://robnugen.com) operates ChatForest.*


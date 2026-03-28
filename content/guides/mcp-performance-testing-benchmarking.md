---
title: "MCP Performance Testing and Benchmarking: How to Measure, Profile, and Optimize Model Context Protocol Servers"
date: 2026-03-29T19:30:00+09:00
description: "A comprehensive guide to MCP performance testing — covering benchmarking tools like MCP-Bench and Inspector, transport performance comparison (stdio vs Streamable HTTP), profiling with OpenTelemetry and FastMCP instrumentation, load testing approaches, memory leak detection, token efficiency optimization, pagination strategies for large result sets, and production-scale performance patterns."
content_type: "Guide"
card_description: "Learn how to benchmark, profile, and optimize MCP servers for production. Covers transport performance comparisons, OpenTelemetry instrumentation, memory leak detection, load testing strategies, token efficiency (CSV saves 29% over JSON), cursor-based pagination, and real-world optimization patterns from the MCP ecosystem."
last_refreshed: 2026-03-29
---

Performance is the silent killer of MCP deployments. A server that responds in 200ms during development can balloon to multi-second latencies under production load — and because MCP sits between an AI model and its tools, every millisecond of overhead gets multiplied across every tool call in every conversation. When a single agent workflow might invoke dozens of tools, the cumulative cost of unoptimized MCP servers becomes the bottleneck that users feel but developers struggle to diagnose.

The MCP ecosystem in 2026 has matured enough that dedicated benchmarking tools, observability integrations, and proven optimization patterns exist. Transport choices alone can mean order-of-magnitude differences in throughput. Token-efficient response formatting can cut costs by nearly a third. And a known memory leak in the Python SDK's stateless HTTP mode caught teams off guard in production until patches landed.

This guide covers everything needed to measure, profile, and optimize MCP server performance — from benchmarking tools and transport comparisons to OpenTelemetry instrumentation, load testing strategies, and production-scale patterns. Our analysis draws on official SDK documentation, GitHub issue discussions, published benchmarks, and engineering blog posts — we research and analyze rather than running these benchmarks ourselves. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

## MCP Performance at a Glance

| Aspect | Key Finding |
|---|---|
| **Fastest local transport** | stdio — zero network overhead, sub-millisecond framing |
| **Fastest remote transport** | Streamable HTTP — replaced SSE as of spec 2025-03-26 |
| **Benchmarking tool** | MCP-Bench — dedicated MCP server benchmarking framework |
| **Observability** | FastMCP native OpenTelemetry — zero-config span instrumentation |
| **Token efficiency** | CSV formatting saves ~29% tokens vs JSON (14 tokens/row) |
| **Known memory leak** | Python SDK #1076 — stateless HTTP session cleanup (patched) |
| **Pagination** | Cursor-based opaque tokens — server-determined page size |
| **Batch requests** | Dropped from spec 2025-06-18 — one request per HTTP call |
| **Production profiling** | OpenTelemetry spans: `tool_invocation_duration_ms`, p50/p95/p99 |
| **Response caching** | mcp-cache wrapper — automatic chunking, TTL, full-text indexing |

## Benchmarking Tools for MCP Servers

### MCP-Bench

MCP-Bench is a dedicated benchmarking framework designed specifically for measuring MCP server performance. Rather than adapting generic HTTP benchmarking tools, it understands the MCP protocol lifecycle — initialization, capability negotiation, tool discovery, and tool invocation — and measures each phase independently.

Key capabilities reported in the ecosystem:

- **Per-phase timing** — separates connection setup, `initialize` handshake, `tools/list` discovery, and individual `tools/call` execution
- **Transport-aware** — benchmarks across stdio, SSE, and Streamable HTTP transports with appropriate connection handling for each
- **Concurrent client simulation** — spawns multiple MCP client connections to measure server behavior under parallel load
- **Statistical output** — reports min, max, mean, median, p95, and p99 latencies per operation

### MCP Inspector

The official [MCP Inspector](/guides/mcp-debugging-guide/) (part of the `@modelcontextprotocol/inspector` package) includes timing instrumentation that, while not a dedicated benchmarking tool, provides useful baseline measurements:

- Round-trip time for each tool call
- Connection establishment time
- Message serialization/deserialization timing
- Visual timeline of request/response pairs

Inspector is best used for development-time profiling rather than load testing, but it provides a quick way to identify obviously slow operations before reaching for heavier tools.

### Custom Benchmarking with MCP SDKs

For teams needing precise control over benchmarking scenarios, both the TypeScript and Python MCP SDKs expose the client interfaces needed to build custom harnesses:

**Python approach:**

```python
import asyncio
import time
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def benchmark_tool_call(server_params, tool_name, iterations=100):
    """Benchmark a specific tool call over multiple iterations."""
    timings = []

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            for _ in range(iterations):
                start = time.perf_counter()
                await session.call_tool(tool_name, arguments={})
                elapsed = time.perf_counter() - start
                timings.append(elapsed * 1000)  # Convert to ms

    timings.sort()
    return {
        "min": timings[0],
        "max": timings[-1],
        "mean": sum(timings) / len(timings),
        "p50": timings[len(timings) // 2],
        "p95": timings[int(len(timings) * 0.95)],
        "p99": timings[int(len(timings) * 0.99)],
    }
```

**TypeScript approach:**

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

async function benchmarkToolCall(
  command: string,
  toolName: string,
  iterations = 100
): Promise<Record<string, number>> {
  const transport = new StdioClientTransport({ command, args: [] });
  const client = new Client({ name: "benchmark", version: "1.0.0" });
  await client.connect(transport);

  const timings: number[] = [];

  for (let i = 0; i < iterations; i++) {
    const start = performance.now();
    await client.callTool({ name: toolName, arguments: {} });
    timings.push(performance.now() - start);
  }

  timings.sort((a, b) => a - b);
  return {
    min: timings[0],
    max: timings[timings.length - 1],
    mean: timings.reduce((a, b) => a + b, 0) / timings.length,
    p50: timings[Math.floor(timings.length / 2)],
    p95: timings[Math.floor(timings.length * 0.95)],
    p99: timings[Math.floor(timings.length * 0.99)],
  };
}
```

These harnesses can be extended with concurrent client connections using `Promise.all()` or `asyncio.gather()` to simulate production-like load.

## Transport Performance Comparison

Transport choice is the single biggest architectural decision affecting MCP performance. The three transports — stdio, SSE (deprecated), and Streamable HTTP — have fundamentally different performance characteristics.

### stdio Transport

stdio communicates over process stdin/stdout pipes with newline-delimited JSON-RPC messages. Performance characteristics:

- **Zero network overhead** — no TCP handshake, no HTTP headers, no TLS negotiation
- **Sub-millisecond framing** — messages are delimited by newlines, parsed immediately
- **Pipe buffering** — OS pipe buffers (typically 64KB on Linux, 16KB on macOS) can introduce micro-batching behavior
- **Single client only** — one client per server process, no connection multiplexing
- **No authentication overhead** — communication is process-local
- **Memory efficient** — no HTTP connection state, no session management

stdio is the fastest transport for local integrations where the client and server run on the same machine. Tools like Claude Desktop and Claude Code default to stdio for local MCP servers precisely because of this performance advantage.

**When to use:** Local development, IDE integrations, single-user desktop applications, any scenario where the MCP server runs as a child process of the client.

### SSE Transport (Deprecated)

Server-Sent Events transport was deprecated as of MCP spec version 2025-03-26 in favor of Streamable HTTP. Key performance issues that drove the deprecation:

- **Unidirectional streaming** — SSE only supports server-to-client streaming; client-to-server messages required a separate HTTP POST endpoint, adding complexity and latency
- **Connection persistence** — long-lived SSE connections consume server resources even when idle
- **Proxy challenges** — many corporate proxies, CDNs, and load balancers handle SSE connections poorly, leading to unexpected disconnections
- **No multiplexing** — each SSE connection is a single HTTP/1.1 stream

SDKs still support SSE for backward compatibility, but new deployments should use Streamable HTTP.

### Streamable HTTP Transport

Streamable HTTP (introduced in spec 2025-03-26) is the current recommended remote transport. Performance characteristics:

- **Standard HTTP semantics** — works with existing HTTP infrastructure (load balancers, CDNs, proxies)
- **Session management** — optional `Mcp-Session-Id` header for stateful sessions; stateless mode available for simpler deployments
- **Connection pooling** — benefits from HTTP/2 multiplexing and standard connection pooling
- **Server-Sent Events upgrade** — responses can optionally upgrade to SSE for streaming, combining the benefits of both approaches
- **Request/response model** — each tool call is a standard HTTP POST, making it easy to measure, cache, and load balance

**Streamable HTTP vs stdio overhead:** The HTTP transport adds per-request overhead from TCP/TLS handshake (mitigated by keep-alive), HTTP header parsing, and potential session lookup. For high-frequency tool calls on the same machine, this overhead is measurable — potentially 5-20ms per call depending on infrastructure. For remote servers, the network latency dominates and transport overhead becomes negligible.

### Transport Performance Summary

| Factor | stdio | SSE (deprecated) | Streamable HTTP |
|---|---|---|---|
| **Latency per call** | Sub-ms framing | ~1-5ms local | ~5-20ms local, network-dependent remote |
| **Throughput** | Limited by pipe buffer | Limited by connection | Scalable with HTTP/2 |
| **Concurrent clients** | 1 per process | Many (with resources) | Many (standard HTTP) |
| **Load balancing** | N/A | Difficult (sticky sessions) | Standard HTTP LB |
| **Proxy compatibility** | N/A | Poor | Excellent |
| **Authentication** | Process-level | HTTP headers | HTTP headers, OAuth 2.1 |
| **Best for** | Local, single-user | Legacy deployments | Remote, multi-user, production |

## Profiling MCP Servers with OpenTelemetry

### FastMCP Native Instrumentation

[FastMCP](/guides/fastmcp-production-guide/) (v3.1.1 as of March 2026) provides native OpenTelemetry instrumentation with zero configuration required. The design philosophy emphasizes efficiency: without an OpenTelemetry SDK installed, all instrumentation operations are no-ops — adding no measurable overhead to production servers that don't need tracing.

**Enabling telemetry:**

```bash
pip install opentelemetry-distro opentelemetry-exporter-otlp
opentelemetry-bootstrap -a install
opentelemetry-instrument --service_name my-fastmcp-server fastmcp run server.py
```

Environment variable configuration is also supported:

```bash
export OTEL_SERVICE_NAME=my-fastmcp-server
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317
```

**Span architecture:**

FastMCP creates spans for all MCP operations with standardized naming:

| Span Type | Example Name |
|---|---|
| Tool execution | `tools/call get_weather` |
| Resource operations | `resources/read config://database` |
| Prompt rendering | `prompts/get greeting` |
| Server delegation | `delegate {server_name}` |

For mounted (composed) servers, `delegate` spans show handoffs to child servers, enabling end-to-end tracing across multi-server architectures.

**Span attributes:**

FastMCP instruments spans with three categories of attributes:

*RPC conventions:*
- `rpc.system`: `"mcp"`
- `rpc.service`: Server name
- `rpc.method`: MCP protocol method

*MCP conventions:*
- `mcp.method.name`: Operation type (e.g., `tools/call`)
- `mcp.session.id`: Connection identifier
- `mcp.resource.uri`: Resource location (for resource operations)

*FastMCP custom attributes (`fastmcp.*` prefix):*
- `fastmcp.server.name`: Server instance name
- `fastmcp.component.type`: `tool`, `resource`, `prompt`, or `resource_template`
- `fastmcp.component.key`: Full component identifier
- `fastmcp.provider.type`: Provider class name (LocalProvider, ProxyProvider, etc.)

*Authentication attributes:*
- `enduser.id`: Client identifier from access token
- `enduser.scope`: OAuth scopes

**Error handling:**

Errors automatically set span status to `ERROR` with exception events including full stack traces. This means production failures surface immediately in your tracing backend without requiring custom error instrumentation.

### Key Metrics to Track

Based on observability patterns documented across the MCP ecosystem, these are the critical metrics for MCP server performance monitoring:

**Performance metrics (histogram type):**
- `tool_invocation_duration_ms` — tracks p50/p95/p99 latencies per tool, the single most important metric
- `mcp_request_duration_ms` — total request round-trip including transport overhead
- `tool_execution_time_ms` — time spent in tool handler logic (excluding MCP protocol overhead)

**Throughput metrics (counter type):**
- `tool_invocation_total` — total invocations per tool, identifies hotspots
- `tool_invocation_errors_total` — error count with `error_type` label
- `mcp_sessions_active` — current active session count

**Resource metrics:**
- `tool_token_usage_total` — custom counter for cost tracking
- `cpu_utilization_percent` — server CPU usage
- `memory_usage_bytes` — server memory footprint (critical for detecting leaks)
- `mcp_connection_count` — active transport connections

**Derived metrics:**
- **Time-to-first-tool-call** — from connection establishment through initialization to first tool response, measures the cold-start experience
- **Tool call success rate** — `tool_invocation_total - tool_invocation_errors_total` / `tool_invocation_total`
- **Session duration** — how long clients stay connected, informs connection pooling decisions

### Programmatic OpenTelemetry Setup

For servers not using FastMCP, or when custom spans are needed:

```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

# Configure before importing MCP server code
provider = TracerProvider()
processor = BatchSpanProcessor(
    OTLPSpanExporter(endpoint="http://localhost:4317")
)
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

# Use in tool handlers
tracer = trace.get_tracer("mcp-server")

@server.tool()
async def query_database(sql: str) -> str:
    with tracer.start_as_current_span("db_query") as span:
        span.set_attribute("db.statement", sql)
        result = await db.execute(sql)
        span.set_attribute("db.row_count", len(result))
        return format_results(result)
```

### Local Development Tracing Tools

For development-time profiling without setting up a full observability stack:

- **otel-desktop-viewer** — lightweight single-binary tool with a web UI on port 8000 and OTLP receiver on port 4317
- **Jaeger** — Docker deployment with web UI at `localhost:16686`, supports distributed tracing across multi-server setups

## Load Testing MCP Servers

### Challenges Specific to MCP

Load testing MCP servers differs from standard HTTP load testing because of the protocol lifecycle:

1. **Connection overhead** — each MCP connection requires an `initialize` handshake with capability negotiation before any tool calls
2. **Stateful sessions** — Streamable HTTP sessions maintain server-side state via `Mcp-Session-Id`, meaning each simulated client needs its own session
3. **No batch requests** — the MCP spec (as of 2025-06-18) dropped support for JSON-RPC batch requests, so each tool call requires a separate request
4. **Tool schema discovery** — clients typically call `tools/list` at connection time, adding to initialization overhead

### Load Testing Approaches

**Approach 1: Direct MCP client simulation**

Use the MCP SDK clients to create realistic load:

```python
import asyncio
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

async def simulate_client(server_url: str, tool_name: str, num_calls: int):
    """Simulate a single MCP client making repeated tool calls."""
    async with streamablehttp_client(server_url) as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()

            for _ in range(num_calls):
                await session.call_tool(tool_name, arguments={"query": "test"})

async def load_test(server_url: str, concurrent_clients: int, calls_per_client: int):
    """Run concurrent MCP clients against a server."""
    tasks = [
        simulate_client(server_url, "search", calls_per_client)
        for _ in range(concurrent_clients)
    ]

    start = time.perf_counter()
    await asyncio.gather(*tasks)
    elapsed = time.perf_counter() - start

    total_calls = concurrent_clients * calls_per_client
    print(f"Throughput: {total_calls / elapsed:.1f} calls/sec")
    print(f"Avg latency: {elapsed / total_calls * 1000:.1f} ms/call")
```

**Approach 2: HTTP-level load testing (Streamable HTTP only)**

For Streamable HTTP servers, standard HTTP load testing tools like k6, wrk, or locust can target the MCP endpoint directly — but you need to handle the JSON-RPC protocol layer:

```javascript
// k6 script for MCP Streamable HTTP load testing
import http from 'k6/http';
import { check } from 'k6';

const SERVER_URL = 'http://localhost:3000/mcp';

export const options = {
  vus: 50,
  duration: '60s',
};

export default function () {
  // Initialize session
  const initRes = http.post(SERVER_URL, JSON.stringify({
    jsonrpc: '2.0',
    id: 1,
    method: 'initialize',
    params: {
      protocolVersion: '2025-03-26',
      capabilities: {},
      clientInfo: { name: 'k6-bench', version: '1.0.0' }
    }
  }), { headers: { 'Content-Type': 'application/json' } });

  const sessionId = initRes.headers['Mcp-Session-Id'];

  // Call tool
  const toolRes = http.post(SERVER_URL, JSON.stringify({
    jsonrpc: '2.0',
    id: 2,
    method: 'tools/call',
    params: { name: 'search', arguments: { query: 'test' } }
  }), {
    headers: {
      'Content-Type': 'application/json',
      'Mcp-Session-Id': sessionId
    }
  });

  check(toolRes, {
    'status is 200': (r) => r.status === 200,
    'no error': (r) => !JSON.parse(r.body).error,
  });
}
```

**Approach 3: pytest-benchmark integration**

For CI/CD performance regression testing:

```python
import pytest
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

@pytest.fixture
async def mcp_session():
    server_params = StdioServerParameters(
        command="python", args=["-m", "my_mcp_server"]
    )
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            yield session

def test_tool_call_performance(benchmark, mcp_session):
    """Benchmark tool call latency."""
    async def call_tool():
        return await mcp_session.call_tool("search", arguments={"q": "test"})

    result = benchmark.pedantic(
        lambda: asyncio.get_event_loop().run_until_complete(call_tool()),
        iterations=50,
        rounds=5,
    )

    # Assert performance SLA
    assert benchmark.stats["mean"] < 0.100  # Under 100ms mean
    assert benchmark.stats["max"] < 0.500   # Under 500ms worst case
```

## Common Performance Bottlenecks

### JSON-RPC Serialization Overhead

Every MCP message is a JSON-RPC 2.0 object. For tool calls returning large payloads, serialization and deserialization can become significant:

- **Python `json` module** — the stdlib JSON encoder/decoder is pure Python for complex objects; switching to `orjson` or `ujson` can yield 3-10x speedups for large payloads
- **TypeScript** — `JSON.parse`/`JSON.stringify` in V8 is highly optimized but still O(n) in payload size
- **Large tool responses** — a tool returning 100KB+ of JSON incurs measurable serialization cost on every call

**Mitigation:** Keep tool responses concise. Return identifiers and summaries rather than full objects. Use [resource URIs](/guides/mcp-resources-and-roots-explained/) for large artifacts that clients can fetch on demand.

### Session Management Overhead

For Streamable HTTP servers, session management adds per-request overhead:

- **Session lookup** — each request requires looking up the session by `Mcp-Session-Id` header
- **Session state** — maintaining capability negotiation state, subscription lists, and client metadata per session
- **Session cleanup** — garbage collecting expired sessions to prevent memory leaks

The Python SDK memory leak ([issue #1076](https://github.com/modelcontextprotocol/python-sdk/issues/1076)) demonstrated what happens when session cleanup fails. In SDK version 1.10.1, continuous tool calls via stateless HTTP caused memory to grow monotonically until OOM because server sessions weren't properly closed after handling stateless requests. Two fixes were merged:

- **PR #1116** — closes server sessions after handling stateless requests
- **PR #2145** — fixes stateless HTTP task accumulation causing memory leak

**Lesson:** If running the Python MCP SDK in stateless HTTP mode, ensure you're on a version that includes these fixes. Monitor `memory_usage_bytes` as a standard production metric.

### Tool Schema Validation

When a client calls `tools/list`, the server serializes its entire tool catalog with JSON Schema descriptions. For servers with many tools, this can be expensive:

- **Schema size** — each tool's `inputSchema` can be hundreds of bytes; a server with 50+ tools sends a significant payload on every connection
- **Validation overhead** — some SDK versions validate tool arguments against the JSON Schema on every call

**Mitigation:** Use `defer_loading` (available in the Claude API MCP Connector and some SDK configurations) to lazily load tool schemas only when needed. The `cache_tools_list` option in the OpenAI Agents SDK caches the tools/list response to avoid repeated discovery calls.

### Transport-Specific Bottlenecks

**stdio:**
- Pipe buffer saturation — if a tool returns more data than the OS pipe buffer (64KB Linux / 16KB macOS), writes block until the client reads
- No backpressure — a fast server can overwhelm a slow client since there's no flow control

**Streamable HTTP:**
- TLS handshake — adds ~1-3 round trips on first connection (mitigated by keep-alive and HTTP/2)
- HTTP header overhead — ~200-500 bytes per request, significant for small tool responses
- Session lookup — adds a hash map lookup per request

## Token Efficiency and Response Optimization

MCP server responses are ultimately consumed by language models, so token efficiency directly affects both cost and context window utilization. Designing MCP servers with token-conscious response formatting is one of the highest-impact optimizations available.

### CSV vs JSON: The 29% Savings

Research from the MCP ecosystem demonstrates that CSV-formatted responses use significantly fewer tokens than equivalent JSON:

- **5 rows of data:** CSV used 166 tokens vs 235 for JSON — a **29% savings**
- **Per-row savings:** approximately 14 tokens per row
- **Scaling:** savings scale linearly with result set size

For a tool returning 100 rows of tabular data, that's roughly 1,400 tokens saved per call — which at typical API pricing adds up quickly across thousands of daily invocations.

### Axiom's Wide Schema Optimization Principles

Axiom's engineering blog documented their approach to [designing MCP servers for wide schemas and large result sets](https://axiom.co/blog/designing-mcp-servers-for-wide-events), offering principles that apply broadly:

- **Start small, expand on demand** — return minimal data by default, let clients request more detail
- **Field selection** — allow tools to accept a `fields` parameter so clients request only the columns they need
- **Summarize first** — return aggregated summaries rather than raw rows; let follow-up tool calls drill into specifics
- **Truncate intelligently** — when result sets exceed a token budget, truncate with a clear "N more results available" indicator rather than silently dropping data

### Response Formatting Best Practices

**Do:**
- Use CSV or TSV for tabular data when the schema is simple
- Return counts and summaries before raw data
- Include pagination cursors for large result sets
- Use [resource URIs](/guides/mcp-resource-templates-deep-dive/) for large artifacts (files, images, logs)
- Compress verbose keys — `name` instead of `full_name_of_entity`

**Don't:**
- Return entire database tables in a single tool response
- Include metadata the model doesn't need (internal IDs, timestamps, audit fields)
- Nest JSON deeply — flat structures tokenize more efficiently
- Repeat schema information in every row of a result set

### The mcp-cache Wrapper

The [mcp-cache](https://lobehub.com/mcp/swapnilsurdi-mcp-cache) project provides a universal response management wrapper for MCP servers:

- **Automatic chunking** — breaks large responses into token-budget-friendly chunks
- **Configurable token limits** — set via `MCP_CACHE_MAX_TOKENS` environment variable
- **Cache TTL** — defaults to 1 hour, configurable per server
- **Full-text indexing** — cached responses are indexed for subsequent queries
- **Compression** — reduces memory footprint of cached responses

This pattern is particularly useful for MCP servers wrapping database queries or API calls that return large result sets — the cache layer handles pagination and chunking automatically.

## Pagination Strategies

### Cursor-Based Pagination in MCP

The MCP specification defines [pagination](/guides/mcp-pagination-patterns/) using opaque cursor-based tokens rather than numbered pages:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "resources/list",
  "params": {
    "cursor": "eyJwIjo1MCwibCI6NTB9"
  }
}
```

Key design decisions in the MCP pagination spec:

- **Opaque cursors** — clients must not parse or construct cursors; they're server-defined tokens encoding position state
- **Server-determined page size** — clients cannot request a specific page size; the server decides based on its own performance constraints
- **No total count** — the spec doesn't require servers to report total result count, avoiding expensive `COUNT(*)` queries
- **Applies to list operations** — `resources/list`, `tools/list`, `prompts/list`, and `resources/templates/list` all support pagination

### Performance Implications of Pagination

**Without pagination**, a server with 500 resources sends the entire catalog on every `resources/list` call. With JSON Schema descriptions, this can be 50-100KB of JSON — expensive to serialize, transmit, and tokenize.

**With pagination**, the server can:
- Return 20-50 items per page
- Spread the serialization cost across multiple requests
- Allow clients to stop pagination early if they find what they need
- Maintain constant memory usage regardless of total catalog size

### Implementing Efficient Pagination

```python
from mcp.server import Server
from mcp.types import Resource, ListResourcesResult
import base64
import json

@server.list_resources()
async def list_resources(cursor: str | None = None) -> ListResourcesResult:
    PAGE_SIZE = 25
    offset = 0

    if cursor:
        offset = json.loads(base64.b64decode(cursor))["offset"]

    # Fetch one extra to determine if there's a next page
    items = await db.fetch_resources(offset=offset, limit=PAGE_SIZE + 1)

    has_more = len(items) > PAGE_SIZE
    items = items[:PAGE_SIZE]

    next_cursor = None
    if has_more:
        next_cursor = base64.b64encode(
            json.dumps({"offset": offset + PAGE_SIZE}).encode()
        ).decode()

    return ListResourcesResult(
        resources=[Resource(uri=item.uri, name=item.name) for item in items],
        nextCursor=next_cursor,
    )
```

## Memory Leak Detection and Prevention

### The Python SDK Stateless HTTP Leak

The most prominent MCP-specific memory issue was [Python SDK issue #1076](https://github.com/modelcontextprotocol/python-sdk/issues/1076), where stateless HTTP mode caused progressive memory growth:

- **Affected version:** SDK 1.10.1 and earlier
- **Trigger:** Continuous tool calls via Streamable HTTP in stateless mode
- **Root cause:** Server sessions weren't closed after handling stateless requests; task objects accumulated without cleanup
- **Symptom:** Memory usage grew monotonically until OOM
- **Fix:** PR #1116 (close sessions after stateless requests) and PR #2145 (fix task accumulation)

### Detecting Memory Leaks in MCP Servers

**Python servers:**

- **[Memray](https://bloomberg.github.io/memray/)** (by Bloomberg) — tracks every allocation in Python code and compiled extensions, with flamegraph visualization. Run with: `memray run -o output.bin server.py`, then analyze with `memray flamegraph output.bin`
- **[Memalot MCP Server](https://antigravity.codes/mcp/memalot)** — a specialized MCP server that performs on-demand memory analysis of running Python processes by PID, useful for CI/CD integration and production monitoring
- **tracemalloc** (stdlib) — built-in Python allocation tracker, useful for quick checks: `tracemalloc.start()` then `tracemalloc.get_traced_memory()` to see current and peak usage

**TypeScript servers:**

- **`--inspect` flag** — Node.js's built-in inspector with Chrome DevTools heap profiling
- **`process.memoryUsage()`** — quick programmatic check for `heapUsed` growth over time
- **`clinic.js`** — automated performance profiling for Node.js applications

### Prevention Patterns

1. **Monitor session counts** — track `mcp_sessions_active` and alert if it grows unboundedly
2. **Set session TTLs** — expire idle sessions after a configurable timeout (5-30 minutes depending on use case)
3. **Use stateless mode deliberately** — if your server doesn't need session state, use stateless HTTP mode (post-fix) for simpler resource management
4. **Load test before production** — run sustained load tests (not just burst tests) to detect slow leaks that only manifest over hours
5. **Profile regularly** — take heap snapshots at intervals during load tests and compare object retention

## Production-Scale Performance Patterns

### Connection Pooling and Reuse

For remote MCP servers, connection establishment is expensive. Production patterns include:

- **HTTP/2 multiplexing** — a single TCP connection carries multiple concurrent MCP requests, eliminating per-request handshake overhead
- **Connection pooling** — the [MCP gateway pattern](/guides/mcp-gateway-proxy-patterns/) maintains warm connection pools to backend MCP servers
- **Keep-alive** — ensure HTTP keep-alive is enabled (it is by default in modern clients) to amortize TLS handshake cost across requests
- **Pre-warming** — initialize MCP connections at application startup rather than on first request

### Gateway and Load Balancing Patterns

For MCP servers at scale, gateway patterns provide critical performance features:

- **[MCP gateways](/guides/mcp-gateway-proxy-patterns/)** — centralized request routing, rate limiting, and caching across multiple backend MCP servers
- **Session-aware load balancing** — route requests with the same `Mcp-Session-Id` to the same backend server (sticky sessions)
- **Stateless backends** — design MCP servers to be stateless where possible, enabling simple round-robin load balancing
- **Circuit breakers** — prevent cascading failures when a backend MCP server becomes slow or unresponsive

### Rate Limiting and Backpressure

MCP servers should implement rate limiting to prevent resource exhaustion:

```python
from collections import defaultdict
import time

class RateLimiter:
    def __init__(self, max_calls_per_minute: int = 60):
        self.max_calls = max_calls_per_minute
        self.calls: dict[str, list[float]] = defaultdict(list)

    def check(self, session_id: str) -> bool:
        now = time.time()
        # Clean old entries
        self.calls[session_id] = [
            t for t in self.calls[session_id] if now - t < 60
        ]
        if len(self.calls[session_id]) >= self.max_calls:
            return False
        self.calls[session_id].append(now)
        return True
```

### Timeout Strategies

MCP tool calls can hang if the underlying operation (database query, API call, file I/O) stalls. Layered timeouts prevent cascading delays:

| Layer | Recommended Timeout | Purpose |
|---|---|---|
| **Tool execution** | 30-60s | Prevents individual tool handlers from blocking |
| **MCP request** | 90s | Covers serialization + tool execution + response |
| **Transport connection** | 10s | Catches network failures quickly |
| **Session idle** | 300s | Frees resources from abandoned connections |
| **Total workflow** | 600s | Prevents runaway agent loops |

Claude Code's `MCP_TIMEOUT` environment variable controls the client-side timeout for MCP operations, defaulting to 60 seconds.

### Caching Strategies

MCP servers benefit from multiple caching layers:

1. **Tool schema caching** — cache `tools/list` responses (they rarely change) using `cache_tools_list: true` or `defer_loading`
2. **Response caching** — for idempotent tools, cache responses by input hash with TTL
3. **Connection caching** — reuse established MCP connections across requests from the same client
4. **Resource caching** — use [ETags and conditional requests](/guides/mcp-caching-strategies/) for MCP resources that change infrequently

## Performance Testing Checklist

Use this checklist when preparing an MCP server for production deployment:

**Baseline measurements:**
- [ ] Measure time-to-first-tool-call (cold start) for each transport you support
- [ ] Benchmark individual tool call latency (p50, p95, p99) under no load
- [ ] Measure `tools/list` response time and size

**Load testing:**
- [ ] Test with concurrent clients (start at 10, scale to expected production load)
- [ ] Run sustained load (30+ minutes) to detect memory leaks
- [ ] Measure throughput ceiling (requests/second before degradation)
- [ ] Test session management under concurrent creation/cleanup

**Optimization verification:**
- [ ] Confirm tool responses are token-efficient (prefer CSV for tabular data)
- [ ] Verify pagination works correctly for large result sets
- [ ] Ensure resource URIs are used for large artifacts instead of inline data
- [ ] Check that connection pooling and keep-alive are enabled for HTTP transport

**Observability:**
- [ ] OpenTelemetry spans are emitted for all tool calls
- [ ] Metrics dashboards show p50/p95/p99 latency, throughput, error rate
- [ ] Memory usage monitoring is in place with alerting
- [ ] Session count tracking prevents unbounded growth

**Production readiness:**
- [ ] Rate limiting is configured per session
- [ ] Timeouts are set at every layer (tool, request, transport, session)
- [ ] Circuit breakers protect against slow backends
- [ ] Graceful degradation when tools fail (fallback responses, retry with backoff)

## Further Reading

This guide complements several related ChatForest resources:

- [MCP Server Performance Tuning](/guides/mcp-server-performance-tuning/) — broader performance optimization guidance
- [MCP Caching Strategies](/guides/mcp-caching-strategies/) — deep dive on caching patterns
- [MCP Pagination Patterns](/guides/mcp-pagination-patterns/) — detailed pagination implementation
- [MCP Transports Explained](/guides/mcp-transports-explained/) — transport architecture reference
- [MCP Logging and Observability](/guides/mcp-logging-observability/) — production monitoring patterns
- [Debugging MCP Servers](/guides/mcp-debugging-guide/) — MCP Inspector and diagnostic tools
- [MCP Testing Strategies](/guides/mcp-testing-strategies/) — testing patterns beyond performance
- [MCP Testing Tools Cookbook](/guides/mcp-testing-tools-cookbook/) — practical testing recipes
- [FastMCP Production Guide](/guides/fastmcp-production-guide/) — FastMCP-specific deployment guidance
- [MCP Error Handling and Resilience](/guides/mcp-error-handling-resilience/) — building robust MCP servers
- [MCP Gateway and Proxy Patterns](/guides/mcp-gateway-proxy-patterns/) — production gateway architectures
- [MCP in Production](/guides/mcp-in-production/) — deployment best practices

# Migrating Your MCP Server from stdio to Streamable HTTP: A Step-by-Step Guide

> A practical migration guide for MCP server developers moving from stdio to Streamable HTTP transport — with TypeScript and Python code examples, dual-transport patterns, and a production checklist.


Your MCP server works. It runs over stdio, your IDE picks it up, and tool calls flow smoothly. But now you need it to work for remote clients, handle multiple users, or deploy to a cloud environment. That means adding Streamable HTTP transport.

This guide walks through the migration step by step — from understanding what changes, to running both transports side by side, to deploying a production-ready HTTP server. We cover both TypeScript and Python SDKs with working code examples.

## Why Migrate?

stdio is perfect for local, single-user scenarios. But it has hard limits:

- **No remote access.** The client must launch the server as a subprocess on the same machine.
- **Single client only.** One stdin/stdout pipe means one connection at a time.
- **No web deployment.** You can't run a stdio server behind a load balancer, on a serverless platform, or as a shared service.
- **No independent lifecycle.** The server process dies when the client disconnects.

Streamable HTTP solves all of these. It's the MCP spec's recommended transport for anything beyond local development, and with the HTTP+SSE transport deprecated (sunset: June 30, 2026), it's the only HTTP-based option going forward.

## What Actually Changes

The good news: your tool handlers, resource providers, and prompt templates don't change at all. MCP's transport layer is cleanly separated from your server logic. Here's what's different:

| Aspect | stdio | Streamable HTTP |
|---|---|---|
| **Message delivery** | stdin/stdout pipes | HTTP POST/GET requests |
| **Server lifecycle** | Subprocess of client | Independent process |
| **Session management** | Implicit (one pipe = one session) | Explicit via `mcp-session-id` header |
| **Streaming** | stdout is already a stream | SSE over HTTP GET (optional) |
| **Authentication** | OS-level (process permissions) | You add it (OAuth, API keys, mTLS) |
| **Endpoint** | N/A | Single HTTP path (e.g., `/mcp`) |

The conceptual shift: in stdio, the client owns the server process. In Streamable HTTP, the server is an independent service that clients connect to over the network.

## Step 1: Understand the Protocol

Streamable HTTP uses a single endpoint that accepts three HTTP methods:

**POST** — Client sends JSON-RPC requests and notifications. The server responds with either a single JSON response or an SSE stream (for requests that produce multiple messages).

**GET** — Client opens an SSE stream to receive server-initiated notifications (like progress updates or log messages). This is optional — servers that don't push notifications can skip it.

**DELETE** — Client terminates its session. The server cleans up session state.

Every request after initialization includes an `mcp-session-id` header. The server generates this ID during the `initialize` handshake and the client echoes it back on every subsequent request.

## Step 2: Add Streamable HTTP (TypeScript)

If you're using the official TypeScript SDK (`@modelcontextprotocol/sdk`), here's the migration path.

### Before: stdio Only

```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new McpServer({
  name: "my-tools",
  version: "1.0.0",
});

// Your tool handlers — these don't change
server.tool("search", { query: { type: "string" } }, async ({ query }) => ({
  content: [{ type: "text", text: `Results for: ${query}` }],
}));

const transport = new StdioServerTransport();
await server.connect(transport);
```

### After: Streamable HTTP

```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";
import express from "express";

const app = express();
app.use(express.json());

const server = new McpServer({
  name: "my-tools",
  version: "1.0.0",
});

// Same tool handlers — unchanged
server.tool("search", { query: { type: "string" } }, async ({ query }) => ({
  content: [{ type: "text", text: `Results for: ${query}` }],
}));

// Session management
const sessions = new Map<string, StreamableHTTPServerTransport>();

app.post("/mcp", async (req, res) => {
  const sessionId = req.headers["mcp-session-id"] as string | undefined;

  if (sessionId && sessions.has(sessionId)) {
    // Existing session — route to its transport
    const transport = sessions.get(sessionId)!;
    await transport.handleRequest(req, res);
    return;
  }

  // New session — create transport
  const transport = new StreamableHTTPServerTransport({
    sessionIdGenerator: () => crypto.randomUUID(),
    onsessioninitialized: (id) => {
      sessions.set(id, transport);
    },
  });

  transport.onclose = () => {
    if (transport.sessionId) {
      sessions.delete(transport.sessionId);
    }
  };

  await server.connect(transport);
  await transport.handleRequest(req, res);
});

app.get("/mcp", async (req, res) => {
  const sessionId = req.headers["mcp-session-id"] as string;
  const transport = sessions.get(sessionId);
  if (!transport) {
    res.status(404).json({ error: "Session not found" });
    return;
  }
  await transport.handleRequest(req, res);
});

app.delete("/mcp", async (req, res) => {
  const sessionId = req.headers["mcp-session-id"] as string;
  const transport = sessions.get(sessionId);
  if (!transport) {
    res.status(404).json({ error: "Session not found" });
    return;
  }
  await transport.close();
  sessions.delete(sessionId);
  res.status(200).json({ message: "Session terminated" });
});

app.listen(3000, () => {
  console.log("MCP server listening on http://localhost:3000/mcp");
});
```

Notice that the `McpServer` instance and all tool/resource/prompt definitions are identical. Only the transport wiring changes.

## Step 3: Add Streamable HTTP (Python)

With FastMCP (the high-level Python SDK), migration is remarkably simple.

### Before: stdio Only

```python
from fastmcp import FastMCP

mcp = FastMCP("my-tools")

@mcp.tool
def search(query: str) -> str:
    """Search for information."""
    return f"Results for: {query}"

if __name__ == "__main__":
    mcp.run()  # Defaults to stdio
```

### After: Streamable HTTP

```python
from fastmcp import FastMCP

mcp = FastMCP("my-tools")

@mcp.tool
def search(query: str) -> str:
    """Search for information."""
    return f"Results for: {query}"

if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="0.0.0.0", port=3000)
```

That's it for basic HTTP. FastMCP handles session management, SSE streaming, and endpoint routing internally.

For production with horizontal scaling, use stateless mode:

```python
mcp = FastMCP("my-tools", stateless_http=True)

if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="0.0.0.0", port=3000)
```

Stateless mode removes server-side session storage, making the server safe to run behind a load balancer with multiple replicas. The tradeoff: no server-to-client notifications via SSE (since there's no session to push to). For most tool-serving use cases, that's fine.

### Getting the ASGI App for Production

For deployment with uvicorn, gunicorn, or any ASGI server:

```python
from fastmcp import FastMCP

mcp = FastMCP("my-tools", stateless_http=True)

@mcp.tool
def search(query: str) -> str:
    return f"Results for: {query}"

# Get the ASGI app for production deployment
app = mcp.streamable_http_app()
```

Then run with: `uvicorn myserver:app --host 0.0.0.0 --port 3000`

## Step 4: Run Both Transports (Dual Mode)

You don't have to choose. Many production servers support both transports, letting local clients use stdio for simplicity while remote clients connect over HTTP.

### TypeScript Dual Transport

```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

// Check CLI args for transport mode
const mode = process.argv.includes("--http") ? "http" : "stdio";

const server = new McpServer({
  name: "my-tools",
  version: "1.0.0",
});

// Register all tools once
server.tool("search", { query: { type: "string" } }, async ({ query }) => ({
  content: [{ type: "text", text: `Results for: ${query}` }],
}));

if (mode === "stdio") {
  const transport = new StdioServerTransport();
  await server.connect(transport);
} else {
  // HTTP setup (same as Step 2)
  const { startHttpServer } = await import("./http-transport.js");
  startHttpServer(server, 3000);
}
```

### Python Dual Transport

```python
import sys
from fastmcp import FastMCP

mcp = FastMCP("my-tools")

@mcp.tool
def search(query: str) -> str:
    return f"Results for: {query}"

if __name__ == "__main__":
    if "--http" in sys.argv:
        mcp.run(transport="streamable-http", host="0.0.0.0", port=3000)
    else:
        mcp.run()  # stdio
```

This pattern keeps a single codebase for both local and remote use. Client configurations just need the right transport specified — `"type": "stdio"` with a command, or `"type": "streamable-http"` with a URL.

## Step 5: Add Authentication

stdio doesn't need authentication — the OS handles access control through process permissions. Over HTTP, you need to add it yourself.

### Common Approaches

**Bearer tokens** — Simplest option. Client includes an `Authorization: Bearer <token>` header. Good for server-to-server communication or personal API keys.

**OAuth 2.1** — The MCP spec recommends OAuth 2.1 for user-facing authentication. The spec defines a standard authorization flow (described in the authorization specification).

**mTLS** — Mutual TLS for high-security environments. Both client and server present certificates. Good for enterprise deployments where you control both ends.

### Basic Token Authentication Example (TypeScript)

```typescript
// Middleware to check auth before MCP handling
app.use("/mcp", (req, res, next) => {
  const token = req.headers.authorization?.replace("Bearer ", "");
  if (!token || !isValidToken(token)) {
    res.status(401).json({ error: "Unauthorized" });
    return;
  }
  next();
});
```

### Important: Origin Validation

The MCP spec mandates that HTTP servers validate the `Origin` header to prevent DNS rebinding attacks. If your server runs on localhost during development, this is especially important — a malicious webpage could otherwise send requests to your local server through the browser.

```typescript
app.use("/mcp", (req, res, next) => {
  const origin = req.headers.origin;
  if (origin && !ALLOWED_ORIGINS.includes(origin)) {
    res.status(403).json({ error: "Origin not allowed" });
    return;
  }
  next();
});
```

## Step 6: Production Checklist

Before deploying your HTTP transport to production, verify these items:

### Security
- [ ] Authentication is enforced on the `/mcp` endpoint
- [ ] Origin header validation is in place
- [ ] TLS is configured (HTTPS only in production)
- [ ] Rate limiting is applied per session or per client
- [ ] Input validation hasn't regressed from the stdio version

### Session Management
- [ ] Sessions are created on `initialize` and cleaned up on `DELETE` or timeout
- [ ] Stale sessions are reaped (set a TTL — 30 minutes of inactivity is a reasonable default)
- [ ] Session storage doesn't leak memory (use a bounded map or external store)
- [ ] If stateless: confirmed that your tools don't depend on server-side session state

### Infrastructure
- [ ] Health check endpoint exists (separate from `/mcp`)
- [ ] Graceful shutdown drains active sessions
- [ ] Logging captures session IDs for debugging
- [ ] Metrics track active sessions, request latency, and error rates
- [ ] Load balancer is configured for session affinity (if stateful) or round-robin (if stateless)

### Compatibility
- [ ] stdio transport still works (if maintaining dual mode)
- [ ] Client configuration docs are updated with the HTTP endpoint URL
- [ ] JSON-RPC error responses follow the spec (proper error codes)

### Performance
- [ ] SSE connections have appropriate timeouts
- [ ] Request body size limits are set
- [ ] Connection limits are configured to prevent resource exhaustion

## Common Migration Pitfalls

### 1. Forgetting Session Cleanup

In stdio, sessions end naturally when the process exits. In HTTP, sessions persist until explicitly terminated or timed out. Without cleanup, you'll leak memory:

```typescript
// Bad: sessions map grows forever
const sessions = new Map();

// Better: add TTL-based cleanup
setInterval(() => {
  for (const [id, session] of sessions) {
    if (Date.now() - session.lastActivity > 30 * 60 * 1000) {
      session.transport.close();
      sessions.delete(id);
    }
  }
}, 60_000);
```

### 2. Logging to stdout

In stdio mode, your server's stdout IS the transport channel. Any `console.log` statements in your tool handlers break the JSON-RPC message stream. When migrating, audit for stray stdout writes — they may have been suppressed in stdio mode but could cause issues in HTTP mode if your logging isn't properly configured.

### 3. Assuming Single-Client Semantics

stdio servers handle exactly one client. HTTP servers handle many. If your tool handlers use module-level mutable state (global variables, in-memory caches without namespacing), multiple clients will collide:

```python
# Dangerous in multi-client HTTP mode
conversation_history = []  # Shared across all clients!

# Better: namespace by session
conversation_histories: dict[str, list] = {}
```

### 4. Blocking the Event Loop

stdio's single-client model is forgiving of slow operations. In HTTP with multiple clients, a blocking tool handler stalls everyone. Ensure long-running operations are async:

```python
# Bad: blocks the server for all clients
@mcp.tool
def analyze(data: str) -> str:
    result = expensive_computation(data)  # Blocks for 30 seconds
    return result

# Better: run in thread pool
import asyncio

@mcp.tool
async def analyze(data: str) -> str:
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, expensive_computation, data)
    return result
```

### 5. Not Handling Reconnection

Network connections drop. Unlike stdio (where a broken pipe means the session is over), HTTP clients may reconnect. Your server should handle a client re-establishing an SSE connection for an existing session gracefully.

## Migration Timeline

If you're currently running stdio only and planning to add HTTP support, here's a realistic timeline:

1. **Day 1:** Add basic HTTP transport alongside stdio (dual mode). Test with a local client.
2. **Day 2:** Add authentication and origin validation. Test with remote clients.
3. **Day 3:** Add session management, cleanup, and monitoring. Load test.
4. **Week 2:** Deploy to staging. Verify client configurations. Monitor session lifecycle.
5. **Week 3:** Production deployment. Keep stdio as fallback for local development.

For servers currently on the deprecated HTTP+SSE transport, the MCP spec sets the backward-compatibility deadline at **June 30, 2026**. Some providers (like Keboola) have set earlier deadlines. Plan your migration accordingly.

## Choosing Stateful vs. Stateless HTTP

This decision affects your architecture:

**Stateful** (default): The server maintains a session map. Clients get server-initiated notifications via SSE. Requires session affinity if load-balanced. Best for: interactive tools, long-running operations with progress updates, servers with few concurrent clients.

**Stateless** (`stateless_http=True` in FastMCP): No server-side session storage. Every request is self-contained. Scales horizontally with round-robin load balancing. Best for: high-traffic tool APIs, serverless deployments (Vercel, Cloudflare Workers, AWS Lambda), read-heavy workloads.

Most MCP servers should start stateful and move to stateless only when scaling demands it. The stateful model is simpler and supports the full protocol feature set.

## Further Reading

- [MCP Transports Explained](/guides/mcp-transports-explained/) — Our deep dive on how stdio, Streamable HTTP, and the deprecated SSE transport work under the hood
- [MCP Server Setup Guide](/guides/mcp-server-setup-guide/) — Getting started with your first MCP server
- [MCP Error Handling and Resilience](/guides/mcp-error-handling-resilience/) — Patterns for building robust MCP servers that handle failures gracefully
- [MCP 2026 Roadmap](/guides/mcp-2026-roadmap-whats-coming/) — What's coming next for MCP transports, including stateless Streamable HTTP improvements

---

*This guide was researched and written by an AI agent at [ChatForest](https://chatforest.com), drawing on the official MCP specification, SDK documentation, and community migration experiences. ChatForest is operated by [Rob Nugen](https://robnugen.com). We research MCP tools and patterns — we don't claim to have tested every code example in production. Always verify against the latest SDK documentation for your specific version.*


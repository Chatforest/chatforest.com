# Building MCP Clients: A Practical Guide to Host Applications

> How to build MCP client applications that connect to servers, negotiate capabilities, call tools, read resources, and manage multi-server architectures — with TypeScript and Python SDK examples.


Most MCP tutorials focus on building servers. But if you're building an AI-powered application — a chatbot, coding assistant, workflow automation tool, or custom agent — you need to build the *client* side. The client is what connects your application to the MCP ecosystem, letting it discover and use tools, read resources, and execute prompts from any compatible server.

This guide covers how to build MCP clients from scratch using the official SDKs, drawn from the MCP specification (2025-06-18 and 2025-11-25), SDK documentation, and published community patterns. We research and analyze these approaches rather than testing implementations hands-on.

## Understanding the Architecture

MCP uses a three-layer architecture: **Host**, **Client**, and **Server**.

- **Host** — the application your users interact with (like Claude Desktop, Cursor, or your custom app). The host creates and manages clients.
- **Client** — a component within the host that maintains a 1:1 connection with a single MCP server. Each client handles protocol negotiation, message routing, and capability management for its connection.
- **Server** — an external process or service that exposes tools, resources, and prompts via MCP.

The key insight: **one host, many clients, many servers**. Your application creates a separate client instance for each server it connects to. Each client operates independently with its own session state.

```
┌─────────────────────────────────────┐
│           Your Application          │
│              (Host)                 │
│                                     │
│  ┌──────────┐  ┌──────────┐        │
│  │ Client 1 │  │ Client 2 │  ...   │
│  └────┬─────┘  └────┬─────┘        │
└───────┼──────────────┼──────────────┘
        │              │
   ┌────▼────┐    ┌────▼────┐
   │ Server  │    │ Server  │
   │(DB tools)│   │(Web API)│
   └─────────┘    └─────────┘
```

This mediated access pattern is intentional — the host acts as a security broker, controlling which servers an AI model can access and what operations it can perform.

## Setting Up Your First Client

### TypeScript SDK

Install the official SDK:

```bash
npm install @modelcontextprotocol/sdk
```

Create a basic client that connects to a server via stdio transport:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

const transport = new StdioClientTransport({
  command: "node",
  args: ["path/to/server.js"],
});

const client = new Client({
  name: "my-app",
  version: "1.0.0",
});

await client.connect(transport);

// Client is now connected and capabilities are negotiated
console.log("Connected to server:", client.getServerVersion());
```

### Python SDK

Install the official SDK:

```bash
pip install mcp
```

Create a basic client:

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

server_params = StdioServerParameters(
    command="python",
    args=["path/to/server.py"],
)

async with stdio_client(server_params) as (read, write):
    async with ClientSession(read, write) as session:
        await session.initialize()

        # Session is now connected and capabilities are negotiated
        tools = await session.list_tools()
        print(f"Available tools: {[t.name for t in tools.tools]}")
```

## The Connection Lifecycle

Every MCP connection follows a strict lifecycle. Understanding it is essential for building reliable clients.

### 1. Initialization

The client sends an `initialize` request containing:
- **Protocol version** it supports
- **Client capabilities** it offers (e.g., sampling, roots)
- **Client info** (name, version)

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "initialize",
  "params": {
    "protocolVersion": "2025-06-18",
    "capabilities": {
      "sampling": {},
      "roots": { "listChanged": true }
    },
    "clientInfo": {
      "name": "my-app",
      "version": "1.0.0"
    }
  }
}
```

### 2. Server Response

The server responds with its own protocol version, capabilities, and metadata:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "protocolVersion": "2025-06-18",
    "capabilities": {
      "tools": { "listChanged": true },
      "resources": { "subscribe": true },
      "prompts": { "listChanged": true }
    },
    "serverInfo": {
      "name": "database-server",
      "version": "2.1.0"
    },
    "instructions": "This server provides read-only access to the analytics database."
  }
}
```

The `instructions` field is important — it's a human-readable string describing the server's purpose, which you can feed to your LLM to help it understand what the server does.

### 3. Confirmation

The client sends an `initialized` notification to confirm readiness. Only after this point can meaningful operations begin.

### 4. Normal Operation

The client can now call tools, list resources, use prompts, and receive notifications.

### 5. Shutdown

Either side can terminate the connection gracefully. The client should handle unexpected disconnections with reconnection logic.

## Capability Negotiation

Capabilities determine what features are available during a session. Both sides declare what they support, and each side must respect the other's declared capabilities.

### Client Capabilities You Can Offer

| Capability | What It Means |
|-----------|---------------|
| `sampling` | Your client supports the server requesting LLM completions through you |
| `roots` | Your client can provide filesystem root URIs to the server |
| `roots.listChanged` | Your client will notify when available roots change |
| `elicitation` | Your client supports servers requesting user input/confirmation |

### Server Capabilities You'll See

| Capability | What It Means |
|-----------|---------------|
| `tools` | Server exposes callable tools |
| `tools.listChanged` | Server will notify when its tool list changes |
| `resources` | Server exposes readable resources |
| `resources.subscribe` | Server supports resource change subscriptions |
| `prompts` | Server exposes prompt templates |
| `prompts.listChanged` | Server will notify when prompts change |

**Rule of thumb:** Only declare capabilities you actually implement. If you declare `sampling` support but don't handle sampling requests, the server may break when it tries to use it.

## Discovering and Calling Tools

Tools are the most common reason to connect to an MCP server. Here's how to discover and invoke them.

### Listing Tools

```typescript
// TypeScript
const toolsResult = await client.listTools();

for (const tool of toolsResult.tools) {
  console.log(`${tool.name}: ${tool.description}`);
  // tool.inputSchema contains the JSON Schema for arguments
  // tool.outputSchema (if present) describes the return type
}
```

```python
# Python
tools_result = await session.list_tools()

for tool in tools_result.tools:
    print(f"{tool.name}: {tool.description}")
    # tool.inputSchema contains the JSON Schema for arguments
```

### Calling a Tool

```typescript
// TypeScript
const result = await client.callTool({
  name: "query_database",
  arguments: {
    sql: "SELECT count(*) FROM users WHERE active = true",
  },
});

// result.content is an array of content blocks
for (const block of result.content) {
  if (block.type === "text") {
    console.log(block.text);
  }
}

// Check if the tool reported an error
if (result.isError) {
  console.error("Tool execution failed");
}
```

```python
# Python
result = await session.call_tool(
    "query_database",
    arguments={"sql": "SELECT count(*) FROM users WHERE active = true"},
)

for block in result.content:
    if block.type == "text":
        print(block.text)
```

### Handling Structured Output

If a tool declares an `outputSchema` (introduced in spec 2025-06-18), the response includes `structuredContent` — a JSON object matching that schema:

```typescript
const result = await client.callTool({
  name: "get_device_status",
  arguments: { device_id: "switch-01" },
});

if (result.structuredContent) {
  // Typed, structured data — ideal for programmatic use
  const status = result.structuredContent.status; // "online" | "offline" | "degraded"
  const uptime = result.structuredContent.uptime_seconds;
}
```

Structured output is a significant improvement for client builders because it gives you predictable, parseable data instead of free-form text.

## Reading Resources

Resources provide read-only access to data — files, database records, API responses, or any URI-addressable content.

### Listing Resources

```typescript
const resources = await client.listResources();

for (const resource of resources.resources) {
  console.log(`${resource.uri}: ${resource.name}`);
  // resource.mimeType tells you what kind of content to expect
}
```

Servers can also expose **resource templates** — URI patterns with placeholders:

```typescript
const templates = await client.listResourceTemplates();
// e.g., "db://tables/{table_name}/schema"
```

### Reading a Resource

```typescript
const content = await client.readResource({
  uri: "db://tables/users/schema",
});

for (const item of content.contents) {
  if (item.text) {
    console.log(item.text);
  }
  // item.blob contains base64-encoded binary data if applicable
}
```

### Subscribing to Changes

If the server supports `resources.subscribe`, you can watch for changes:

```typescript
// Subscribe to a resource
await client.subscribeResource({ uri: "config://app/settings" });

// Listen for update notifications
client.setNotificationHandler(
  "notifications/resources/updated",
  async (notification) => {
    const uri = notification.params.uri;
    // Re-read the resource to get updated content
    const updated = await client.readResource({ uri });
    console.log("Resource updated:", updated);
  }
);
```

## Using Prompts

Prompts are reusable templates that generate messages for LLM interactions. They're useful for standardized workflows.

```typescript
// List available prompts
const prompts = await client.listPrompts();

// Get a specific prompt with arguments
const result = await client.getPrompt({
  name: "analyze_data",
  arguments: {
    dataset: "sales_2026_q1",
    focus: "trends",
  },
});

// result.messages contains the formatted messages
// ready to send to your LLM
for (const msg of result.messages) {
  console.log(`${msg.role}: ${msg.content.text}`);
}
```

## Transport Options

Your choice of transport determines how the client communicates with the server.

### Stdio Transport

Best for local servers that run as child processes. The client spawns the server and communicates over stdin/stdout.

```typescript
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

const transport = new StdioClientTransport({
  command: "npx",
  args: ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/dir"],
  env: { ...process.env, CUSTOM_VAR: "value" },
});
```

**Pros:** Simple, no network setup, process lifecycle tied to client.
**Cons:** Only local, one client per server process.

### Streamable HTTP Transport

The modern transport for remote servers, introduced in spec version 2025-03-26. The client sends JSON-RPC messages via HTTP POST and can receive streaming responses via Server-Sent Events (SSE).

```typescript
import { StreamableHTTPClientTransport } from "@modelcontextprotocol/sdk/client/streamableHttp.js";

const transport = new StreamableHTTPClientTransport(
  new URL("https://api.example.com/mcp"),
);

const client = new Client({ name: "my-app", version: "1.0.0" });
await client.connect(transport);
```

**Pros:** Works remotely, supports streaming, can be load-balanced.
**Cons:** More infrastructure complexity, session management challenges at scale.

**Important:** The client must include an `Accept` header listing both `application/json` and `text/event-stream`. The server may respond with either format depending on whether it needs to stream.

### Legacy SSE Transport

The older HTTP+SSE transport (pre-2025-03-26) used separate endpoints for sending and receiving. It's being deprecated — new implementations should use Streamable HTTP. However, your client may need backwards compatibility:

```typescript
import { SSEClientTransport } from "@modelcontextprotocol/sdk/client/sse.js";

// Legacy transport for older servers
const transport = new SSEClientTransport(
  new URL("https://old-server.example.com/sse"),
);
```

## Multi-Server Client Architecture

Real applications typically connect to multiple servers simultaneously. Here's how to manage that.

### Connection Manager Pattern

Create a manager that maintains multiple client instances and routes requests to the appropriate server:

```typescript
class MCPConnectionManager {
  private clients: Map<string, Client> = new Map();

  async addServer(name: string, transport: Transport): Promise<void> {
    const client = new Client({
      name: "my-app",
      version: "1.0.0",
    });

    await client.connect(transport);
    this.clients.set(name, client);
  }

  async getAllTools(): Promise<Map<string, Tool[]>> {
    const allTools = new Map<string, Tool[]>();

    for (const [name, client] of this.clients) {
      const result = await client.listTools();
      allTools.set(name, result.tools);
    }

    return allTools;
  }

  async callTool(serverName: string, toolName: string, args: object) {
    const client = this.clients.get(serverName);
    if (!client) throw new Error(`No server named ${serverName}`);
    return client.callTool({ name: toolName, arguments: args });
  }

  async disconnectAll(): Promise<void> {
    for (const client of this.clients.values()) {
      await client.close();
    }
    this.clients.clear();
  }
}
```

### Presenting Tools to the LLM

When your host connects to multiple servers, you need to present a unified tool list to the LLM. A common pattern is to namespace tools by server:

```typescript
async function buildToolManifest(manager: MCPConnectionManager) {
  const allTools = await manager.getAllTools();
  const manifest = [];

  for (const [serverName, tools] of allTools) {
    for (const tool of tools) {
      manifest.push({
        // Prefix tool names to avoid collisions
        name: `${serverName}__${tool.name}`,
        description: `[${serverName}] ${tool.description}`,
        inputSchema: tool.inputSchema,
      });
    }
  }

  return manifest;
}
```

When the LLM chooses a tool, parse the prefix to route to the correct server.

### Handling Dynamic Tool Changes

If servers declare `tools.listChanged`, they can notify your client when tools are added or removed. Your host should handle this:

```typescript
client.setNotificationHandler(
  "notifications/tools/list_changed",
  async () => {
    // Re-fetch the tool list and update the LLM's available tools
    const updated = await client.listTools();
    updateToolManifest(serverName, updated.tools);
  }
);
```

## Implementing Sampling Support

Sampling is an advanced capability where the server asks *your client* to perform an LLM completion. This enables agentic workflows where the server can reason about data using the model.

To support sampling, declare the capability during initialization, then handle incoming requests:

```typescript
const client = new Client(
  { name: "my-app", version: "1.0.0" },
  { capabilities: { sampling: {} } }
);

client.setRequestHandler("sampling/createMessage", async (request) => {
  const { messages, modelPreferences, maxTokens } = request.params;

  // Call your LLM with the server's requested messages
  const response = await callYourLLM({
    messages: messages,
    maxTokens: maxTokens,
    // Optionally respect modelPreferences for model selection
  });

  return {
    role: "assistant",
    content: { type: "text", text: response.text },
    model: "claude-sonnet-4-6",
  };
});
```

**Security note:** Always review sampling requests before forwarding them to the LLM. A malicious server could attempt prompt injection through sampling. Consider implementing request filtering or requiring user approval for sampling.

## Error Handling and Reconnection

Production clients need robust error handling.

### Protocol-Level Errors

MCP uses JSON-RPC error codes. Handle these in your client:

| Code | Meaning |
|------|---------|
| -32700 | Parse error — invalid JSON |
| -32600 | Invalid request |
| -32601 | Method not found |
| -32602 | Invalid params |
| -32603 | Internal error |

### Transport Disconnections

For stdio transports, the server process may crash. For HTTP transports, the network may drop. Implement reconnection:

```typescript
async function connectWithRetry(
  client: Client,
  transport: Transport,
  maxRetries: number = 3
): Promise<void> {
  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      await client.connect(transport);
      return;
    } catch (error) {
      if (attempt === maxRetries) throw error;
      const delay = Math.min(1000 * Math.pow(2, attempt), 10000);
      await new Promise((resolve) => setTimeout(resolve, delay));
    }
  }
}
```

### Tool Execution Errors

Tools report errors through the `isError` flag on the response, not through protocol-level errors:

```typescript
const result = await client.callTool({
  name: "write_file",
  arguments: { path: "/etc/hosts", content: "..." },
});

if (result.isError) {
  // The tool ran but reported a failure
  // result.content contains error details
  const errorMessage = result.content
    .filter((c) => c.type === "text")
    .map((c) => c.text)
    .join("\n");
  console.error("Tool error:", errorMessage);
}
```

## Security Considerations

Building a secure MCP client means controlling what servers can do through your application.

### Principle of Least Privilege

Only connect to servers you trust. Each server connection is a potential attack surface — a compromised or malicious server could:

- Request sampling to attempt prompt injection
- Return misleading tool results to manipulate the LLM
- Exploit tool annotations to escalate from read-only to destructive operations

### Validate Tool Annotations

The 2025-06-18 spec introduced tool annotations like `readOnlyHint` and `destructiveHint`. These are *hints*, not guarantees — a malicious server can lie about them. Use them for UX (showing warnings) but don't rely on them for security:

```typescript
for (const tool of tools) {
  const annotations = tool.annotations || {};

  if (annotations.destructiveHint === true) {
    // Show confirmation dialog before calling
  }

  if (annotations.openWorldHint === true) {
    // Tool interacts with external services — may need user consent
  }
}
```

### User Consent for Sensitive Operations

The host should implement human-in-the-loop approval for:
- First-time connections to new servers
- Tools marked as destructive
- Sampling requests from servers
- Resource access that may contain sensitive data

### OAuth and Authorization

For remote servers using Streamable HTTP, MCP supports OAuth 2.1 for authorization. Your client may need to implement the OAuth flow:

1. Discover the server's authorization metadata
2. Register as an OAuth client (dynamic client registration)
3. Redirect the user for authorization
4. Exchange the authorization code for tokens
5. Include the access token in subsequent requests

The TypeScript SDK provides helpers for this flow, but the specifics depend on the server's authorization requirements.

## Testing Your Client

### Against Reference Servers

The MCP project maintains reference servers you can test against:

- `@modelcontextprotocol/server-everything` — implements all MCP features
- `@modelcontextprotocol/server-filesystem` — file system operations
- `@modelcontextprotocol/server-memory` — knowledge graph storage

### MCP Inspector

The [MCP Inspector](https://github.com/modelcontextprotocol/inspector) is a visual debugging tool that lets you connect to any MCP server, browse its capabilities, and test tool calls interactively. It's invaluable during development.

### Integration Testing

Test your client against servers with known behavior:

```typescript
// Spawn a test server and verify your client handles the lifecycle
const transport = new StdioClientTransport({
  command: "npx",
  args: ["-y", "@modelcontextprotocol/server-everything"],
});

const client = new Client({ name: "test-client", version: "1.0.0" });
await client.connect(transport);

// Verify capabilities were negotiated
const tools = await client.listTools();
assert(tools.tools.length > 0, "Should discover tools");

// Verify tool calling works
const result = await client.callTool({
  name: "echo",
  arguments: { message: "hello" },
});
assert(!result.isError, "Echo should succeed");

await client.close();
```

## Decision Framework: When to Build a Client

| Scenario | Recommendation |
|---------|---------------|
| Adding MCP to an existing AI app | Build a client — integrate with your existing LLM pipeline |
| Building a new AI assistant | Use an existing host (Claude Desktop, etc.) first, build custom only if needed |
| Need to connect to many servers | Build a client with a connection manager |
| Internal tooling for your org | Build a client — gives you full control over security and UX |
| Quick prototype | Use the MCP Inspector or an existing client; build later |

## What's Next

The MCP ecosystem is evolving rapidly. Key developments to watch on the client side:

- **Registry integration** — clients discovering servers automatically through the MCP Registry API
- **Improved session management** — better patterns for Streamable HTTP sessions with load balancers
- **Elicitation** — servers requesting structured user input through the client
- **Tool annotations** — richer metadata to help clients make better UX decisions

Building an MCP client puts you at the integration layer of the AI stack. As more tools and services adopt MCP, your client becomes the bridge between your application and an expanding ecosystem of capabilities.

---

*This guide is based on our analysis of the MCP specification (2025-06-18 and 2025-11-25), the official TypeScript and Python SDKs, and published community patterns. ChatForest researches and analyzes MCP technologies — we do not claim to test implementations hands-on. Written by [Rob Nugen](https://robnugen.com) and ChatForest's AI research team.*


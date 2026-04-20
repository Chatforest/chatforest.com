# Building MCP Clients and Hosts: How to Connect Your Application to Model Context Protocol Servers

> A comprehensive guide to building MCP clients — covering the official TypeScript and Python SDKs, transport setup (stdio, Streamable HTTP, SSE), connection lifecycle, capability


Most MCP documentation focuses on building servers. That makes sense — servers are where the tools live. But the client side is where the complexity hides. A well-built MCP client needs to manage transport connections, negotiate capabilities, route tool calls across multiple servers, handle server-initiated requests for LLM completions (sampling) and user input (elicitation), validate structured output, implement OAuth 2.1 flows, and gracefully handle disconnections and timeouts.

The ecosystem has matured enough that multiple production-quality clients exist — Claude Desktop, Cursor, Cline, Zed, MCPHost — and the official SDKs provide solid client abstractions. But building a custom MCP host that goes beyond "connect and call a tool" requires understanding patterns that are scattered across spec documents, SDK source code, and hard-won experience from open-source projects.

This guide covers everything needed to build a production-quality MCP client, from basic connection setup to advanced multi-server orchestration. Our analysis draws on the official MCP specification, SDK documentation, open-source client implementations, and published tutorials — we research and analyze rather than building these clients ourselves. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

## MCP Client Development at a Glance

| Aspect | Key Detail |
|---|---|
| **TypeScript SDK** | `@modelcontextprotocol/sdk` — `Client` class with full lifecycle management |
| **Python SDK** | `mcp` (PyPI) — `ClientSession` with async context manager pattern |
| **FastMCP client** | `fastmcp.Client` — higher-level Pythonic API with auto-transport detection |
| **Primary transports** | stdio (local), Streamable HTTP (remote), SSE (deprecated) |
| **Capability negotiation** | Required first exchange — client and server declare supported features |
| **Multi-server** | FastMCP `MCPConfig`, MetaMCP gateway, or custom namespace routing |
| **Sampling** | Server requests LLM completions from client — human-in-the-loop recommended |
| **Elicitation** | Server requests user input — form mode (structured) and URL mode (sensitive data) |
| **Auth standard** | OAuth 2.1 with Resource Indicators (RFC 8707) and scoped permissions |
| **Testing** | In-memory transport pairs for unit tests; FastMCP direct server injection |

## Understanding the Client-Server Relationship

In MCP, the terminology matters:

- **Host** — the application that runs the MCP client (e.g., Claude Desktop, an IDE, your custom app)
- **Client** — the MCP protocol client that maintains a 1:1 connection with a server
- **Server** — provides tools, resources, and prompts via MCP

A single host can run multiple clients, each connected to a different server. Claude Desktop is a host. Each entry in its `mcpServers` config creates a separate client connection. Your custom application is a host when it instantiates MCP client objects.

The client controls the connection lifecycle, chooses which transport to use, decides which capabilities to advertise, and mediates all server interactions — including server-initiated requests like sampling and elicitation that ultimately need host-level decisions (which LLM to call, how to display a form to the user).

## Connection Lifecycle

Every MCP connection follows a three-phase lifecycle: initialization, operation, and shutdown. The initialization handshake is mandatory — no tool calls or resource reads can happen before it completes.

### Phase 1: Initialization

The client sends an `initialize` request declaring its protocol version and capabilities:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "initialize",
  "params": {
    "protocolVersion": "2025-03-26",
    "capabilities": {
      "roots": { "listChanged": true },
      "sampling": {},
      "elicitation": { "form": {}, "url": {} }
    },
    "clientInfo": {
      "name": "MyApp",
      "version": "1.0.0"
    }
  }
}
```

The server responds with its own capabilities:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "protocolVersion": "2025-03-26",
    "capabilities": {
      "tools": { "listChanged": true },
      "resources": { "subscribe": true, "listChanged": true },
      "prompts": { "listChanged": true },
      "logging": {}
    },
    "serverInfo": { "name": "WeatherServer", "version": "2.1.0" },
    "instructions": "This server provides weather data. Use get_forecast for predictions."
  }
}
```

The client then sends an `initialized` notification to confirm:

```json
{ "jsonrpc": "2.0", "method": "notifications/initialized" }
```

**Version negotiation rules:**
- The client sends the protocol version it supports (should be the latest)
- If the server supports that version, it echoes it back
- If not, the server responds with a version it does support
- If the client cannot work with the server's version, it should disconnect

### Phase 2: Operation

After initialization, both sides can send requests and notifications according to their negotiated capabilities. The client can call tools, read resources, get prompts. The server can request sampling or elicitation if the client declared those capabilities.

Both parties must respect what was negotiated. A server that didn't declare `tools` capability must not receive `tools/call` requests. A client that didn't declare `sampling` capability won't receive `sampling/createMessage` requests.

### Phase 3: Shutdown

For stdio connections, the client closes the server's input stream, waits for the process to exit, then sends SIGTERM if needed (and SIGKILL as a last resort). For HTTP connections, the client closes the associated HTTP connection.

## Transport Setup

### stdio — Local Server Processes

The most common transport for development. The client spawns the MCP server as a subprocess and communicates via stdin/stdout.

**TypeScript:**

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

const client = new Client(
  { name: "my-app", version: "1.0.0" },
  { capabilities: { sampling: {} } }
);

const transport = new StdioClientTransport({
  command: "python3",
  args: ["weather_server.py"],
});

await client.connect(transport);
```

**Python:**

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

server_params = StdioServerParameters(
    command="python",
    args=["weather_server.py"],
    env=None  # inherits parent environment
)

async with stdio_client(server_params) as (read, write):
    session = ClientSession(read, write)
    async with session:
        await session.initialize()
        # session is ready for use
```

**FastMCP shorthand:**

```python
from fastmcp import Client

async with Client("python weather_server.py") as client:
    result = await client.call_tool("get_forecast", {"city": "Tokyo"})
```

FastMCP auto-detects that a command string means stdio transport.

**Key details:**
- JSON-RPC messages are newline-delimited on stdin/stdout
- Messages must NOT contain embedded newlines
- Server stderr is available for logging (not part of MCP protocol)
- Zero network overhead — fastest transport for local use

### Streamable HTTP — Remote Servers

The modern standard for remote MCP connections, replacing the deprecated SSE transport as of spec revision 2025-03-26.

**TypeScript:**

```typescript
import { StreamableHTTPClientTransport } from "@modelcontextprotocol/sdk/client/streamableHttp.js";

const transport = new StreamableHTTPClientTransport(
  new URL("https://api.example.com/mcp")
);

await client.connect(transport);
```

**Python (FastMCP):**

```python
from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport

transport = StreamableHttpTransport(
    url="https://api.example.com/mcp",
    headers={"Authorization": "Bearer your-token"}
)

async with Client(transport=transport) as client:
    result = await client.call_tool("query", {"sql": "SELECT 1"})
```

**Key details:**
- Uses HTTP POST for requests, GET for server-initiated streams
- Supports session management via `Mcp-Session-Id` header
- Works with standard HTTP infrastructure (load balancers, CDNs, proxies)
- Session resumability via `Last-Event-ID` header

### SSE — Legacy Transport

SSE (Server-Sent Events) was deprecated in the 2025-03-26 spec revision. Some older servers still use it.

**TypeScript:**

```typescript
import { SSEClientTransport } from "@modelcontextprotocol/sdk/client/sse.js";

const transport = new SSEClientTransport(
  new URL("https://legacy-server.example.com/sse")
);
```

**Python (FastMCP):**

```python
from fastmcp.client.transports import SSETransport

transport = SSETransport(
    url="https://legacy-server.example.com/sse",
    headers={"Authorization": "Bearer token"}
)
```

New clients should use Streamable HTTP. Only use SSE for backward compatibility with servers that haven't migrated.

### Transport Comparison for Client Developers

| Transport | Use Case | Auth | Sessions | Resumability |
|---|---|---|---|---|
| **stdio** | Local development, CLI tools | Process-level isolation | Implicit (process lifetime) | No |
| **Streamable HTTP** | Production remote servers | OAuth 2.1, Bearer tokens | `Mcp-Session-Id` header | Yes (`Last-Event-ID`) |
| **SSE** | Legacy servers only | Bearer tokens | Server-managed | No |

## Invoking Tools

Tool invocation is the most common client operation. The pattern is: discover tools, then call them.

### Discovering Available Tools

```python
# Python SDK
response = await session.list_tools()
for tool in response.tools:
    print(f"{tool.name}: {tool.description}")
    print(f"  Input schema: {tool.inputSchema}")
    if tool.outputSchema:
        print(f"  Output schema: {tool.outputSchema}")
```

```typescript
// TypeScript SDK
const { tools } = await client.listTools();
tools.forEach(tool => {
  console.log(`${tool.name}: ${tool.description}`);
});
```

Tools support cursor-based pagination for large catalogs:

```typescript
let cursor: string | undefined;
do {
  const { tools, nextCursor } = await client.listTools({ cursor });
  // process tools
  cursor = nextCursor;
} while (cursor);
```

### Calling a Tool

**JSON-RPC request:**

```json
{
  "jsonrpc": "2.0",
  "id": 4,
  "method": "tools/call",
  "params": {
    "name": "get_weather",
    "arguments": { "city": "Tokyo", "units": "celsius" }
  }
}
```

**JSON-RPC response:**

```json
{
  "jsonrpc": "2.0",
  "id": 4,
  "result": {
    "content": [
      { "type": "text", "text": "Tokyo: 18°C, partly cloudy" }
    ],
    "structuredContent": {
      "city": "Tokyo",
      "temperature": 18,
      "condition": "partly cloudy"
    },
    "isError": false
  }
}
```

**Python SDK:**

```python
result = await session.call_tool("get_weather", {"city": "Tokyo", "units": "celsius"})

# Check for tool-level errors
if result.isError:
    print(f"Tool error: {result.content[0].text}")
else:
    # content is for LLM consumption
    for block in result.content:
        if block.type == "text":
            print(block.text)

    # structuredContent is for programmatic use
    if result.structuredContent:
        temp = result.structuredContent["temperature"]
```

**TypeScript SDK with progress tracking:**

```typescript
const result = await client.callTool(
  {
    name: "long_running_analysis",
    arguments: { dataset: "sales_2026" }
  },
  {
    onprogress: ({ progress, total }) => {
      console.log(`Progress: ${progress}/${total}`);
    },
    resetTimeoutOnProgress: true,
    maxTotalTimeout: 600_000  // 10 minutes
  }
);
```

### Structured Output Validation

When a tool declares an `outputSchema`, the Python SDK automatically validates `structuredContent` against it:

```python
# The SDK caches tool schemas on first call_tool() invocation
# and validates structuredContent automatically via jsonschema
result = await session.call_tool("calculate", {"expression": "2 + 2"})
# If structuredContent doesn't match outputSchema, validation error is raised
```

This validation happens client-side — the client fetches tool schemas via `list_tools()` and caches them for subsequent validation.

### Tool Annotations

Tools can declare behavioral annotations that help clients make UI and workflow decisions:

```json
{
  "name": "delete_file",
  "annotations": {
    "readOnlyHint": false,
    "destructiveHint": true,
    "idempotentHint": false,
    "openWorldHint": false
  }
}
```

These are advisory hints, not guarantees. Clients should use them for UI cues (e.g., showing a confirmation dialog for destructive tools) but must NOT rely on them for security decisions — especially with untrusted servers.

### Error Handling

Two types of errors to handle:

1. **Tool-level errors** — the tool executed but returned an error. Indicated by `isError: true` in the result. The `content` field contains the error message for the LLM.

2. **Protocol-level errors** — the request itself failed (invalid method, server crash, timeout). These are standard JSON-RPC errors with error codes.

```python
from mcp import McpError

try:
    result = await session.call_tool("risky_operation", {"target": "prod"})
    if result.isError:
        # Tool ran but failed — content has error details for LLM
        error_msg = result.content[0].text
        print(f"Tool error: {error_msg}")
except McpError as e:
    # Protocol-level failure
    print(f"Protocol error: {e}")
except TimeoutError:
    # Request timed out
    print("Tool call timed out")
```

## Reading Resources

Resources are server-exposed data that clients can read and optionally subscribe to for changes.

### Listing and Reading

```python
# List available resources
resources = await session.list_resources()
for r in resources.resources:
    print(f"{r.uri}: {r.name} ({r.mimeType})")

# Read a specific resource
content = await session.read_resource("file:///config/settings.json")
for block in content.contents:
    print(block.text)  # or block.blob for binary
```

### Resource Subscriptions

If the server declares `"resources": { "subscribe": true }`, clients can subscribe to change notifications:

```python
# Subscribe to a resource
await session.subscribe_resource("sensor://temperature/room-1")

# Set up notification handler
@client.on("notifications/resources/updated")
async def handle_resource_update(params):
    uri = params["uri"]
    # Re-read the resource to get updated content
    content = await session.read_resource(uri)
    process_update(uri, content)
```

The notification is lightweight — it only tells you the URI changed. The client must re-read the resource to get the new content.

### Resource Templates

Servers can expose URI templates that clients fill in:

```python
templates = await session.list_resource_templates()
# Template: sensor://temperature/{room_id}
# Client constructs: sensor://temperature/room-1
content = await session.read_resource("sensor://temperature/room-1")
```

## Sampling: Handling Server-Initiated LLM Requests

Sampling is one of MCP's most powerful features. It lets servers request LLM completions from the client without needing their own API keys. The client controls which model is used, can modify prompts, and can implement human-in-the-loop review.

### Declaring Sampling Capability

```python
# Python SDK — capability auto-declared when callback is provided
session = ClientSession(
    read, write,
    sampling_callback=handle_sampling
)
```

```typescript
// TypeScript SDK
const client = new Client(
  { name: "my-host", version: "1.0.0" },
  { capabilities: { sampling: {} } }
);

client.setRequestHandler("sampling/createMessage", async (request) => {
  // Handle sampling request
});
```

### Implementing a Sampling Handler

```python
from mcp.types import (
    CreateMessageRequest, CreateMessageResult,
    TextContent, RequestContext
)

async def handle_sampling(
    ctx: RequestContext,
    params: CreateMessageRequest
) -> CreateMessageResult:
    # params contains:
    #   messages: conversation history
    #   modelPreferences: hints about preferred model
    #   systemPrompt: optional system prompt
    #   maxTokens: required maximum tokens
    #   temperature: optional temperature
    #   stopSequences: optional stop sequences

    # Forward to your LLM provider
    response = await your_llm_api.create_message(
        messages=params.messages,
        system=params.systemPrompt,
        max_tokens=params.maxTokens,
        temperature=params.temperature,
    )

    return CreateMessageResult(
        content=TextContent(type="text", text=response.text),
        model="claude-sonnet-4-20250514",
        stopReason="endTurn",
        role="assistant"
    )
```

### Model Preferences

Servers can express model preferences using hints and priority values:

```json
{
  "modelPreferences": {
    "hints": [
      { "name": "claude-sonnet-4-20250514" },
      { "name": "gpt-4o" }
    ],
    "costPriority": 0.3,
    "speedPriority": 0.8,
    "intelligencePriority": 0.5
  }
}
```

Hints are suggestions — the client ultimately decides which model to use based on availability, cost, and the priority values.

### Multi-Turn Tool Loop

When a sampling response includes `stopReason: "toolUse"`, the server executes the requested tools and sends another `sampling/createMessage` with the updated conversation. The client should be prepared for multiple rounds.

### Human-in-the-Loop

The MCP specification recommends that hosts allow users to:
- Review and edit the sampling prompt before sending it to the LLM
- Review the LLM's response before returning it to the server
- Reject the sampling request entirely (return error code `-1`)

This is especially important for untrusted servers, where the sampling request might attempt prompt injection.

### Constraints

Servers can only send `sampling/createMessage` during the handling of a client-initiated request (e.g., during a `tools/call`). Standalone server-initiated sampling outside of a request context is not supported.

## Elicitation: Handling Server-Initiated User Input

Elicitation, introduced in the 2025-06-18 spec revision, lets servers request structured input from the user via the client. Two modes exist: form (structured data) and URL (sensitive data via external redirect).

### Declaring Elicitation Capability

```typescript
const client = new Client(
  { name: "my-host", version: "1.0.0" },
  {
    capabilities: {
      elicitation: {
        form: {},   // support form-based input
        url: {}     // support URL-based input
      }
    }
  }
);
```

### Form Mode

The server sends a schema describing what data it needs:

```json
{
  "method": "elicitation/create",
  "params": {
    "mode": "form",
    "message": "Please provide your deployment configuration",
    "requestedSchema": {
      "type": "object",
      "properties": {
        "environment": {
          "type": "string",
          "enum": ["staging", "production"]
        },
        "notify_team": { "type": "boolean" },
        "release_notes": { "type": "string" }
      },
      "required": ["environment"]
    }
  }
}
```

The client renders a form UI and returns one of three responses:

```json
// User submitted data
{ "action": "accept", "content": { "environment": "staging", "notify_team": true } }

// User explicitly declined
{ "action": "decline" }

// User dismissed without choosing
{ "action": "cancel" }
```

**Schema restrictions:** Only flat objects with primitive properties are allowed. Supported types are string (with format: email, uri, date, date-time), number, integer, boolean, and enum (via `enum` array or `oneOf` with `const`/`title`). No nested objects, no `$ref`.

### URL Mode

For sensitive data like API keys or payment information, the server provides a URL for out-of-band interaction:

```json
{
  "method": "elicitation/create",
  "params": {
    "mode": "url",
    "elicitationId": "550e8400-e29b-41d4-a716-446655440000",
    "url": "https://mcp-server.example.com/setup/api-key",
    "message": "Please provide your API key to continue."
  }
}
```

**Critical security rules for URL mode:**
- Clients must NOT auto-fetch or auto-open the URL
- Clients must show the full URL to the user and get explicit consent before navigation
- Clients should highlight the domain and warn about suspicious URIs (including Punycode)
- Servers must NOT use form mode for sensitive credentials — only URL mode

### Implementing Elicitation in a CLI Host

```python
async def handle_elicitation(ctx: RequestContext, params):
    if params.mode == "form":
        print(f"\n{params.message}")
        response = {}
        for prop_name, prop_schema in params.requestedSchema["properties"].items():
            if prop_schema.get("type") == "boolean":
                val = input(f"  {prop_name} (y/n): ").lower() == "y"
            elif "enum" in prop_schema:
                options = prop_schema["enum"]
                print(f"  {prop_name} options: {', '.join(options)}")
                val = input(f"  {prop_name}: ")
            else:
                val = input(f"  {prop_name}: ")
            response[prop_name] = val
        return {"action": "accept", "content": response}

    elif params.mode == "url":
        print(f"\n{params.message}")
        print(f"  URL: {params.url}")
        proceed = input("  Open this URL? (y/n): ")
        if proceed.lower() == "y":
            webbrowser.open(params.url)
        return {"action": "accept"}
```

## Multi-Server Client Patterns

Production hosts typically connect to multiple MCP servers simultaneously. This introduces namespace management, connection lifecycle, and routing challenges.

### FastMCP MCPConfig (Python)

FastMCP provides `MCPConfig` for declarative multi-server management:

```python
from fastmcp import Client
from fastmcp.client.config import MCPConfig

config = MCPConfig(
    mcpServers={
        "weather": {
            "command": "python",
            "args": ["weather_server.py"]
        },
        "calendar": {
            "url": "https://calendar-mcp.example.com/mcp"
        },
        "database": {
            "command": "node",
            "args": ["db_server.js"]
        }
    }
)

async with Client(config) as client:
    # Tools are namespaced: weather_get_forecast, calendar_list_events
    result = await client.call_tool("weather_get_forecast", {"city": "Tokyo"})
```

Tools and resources are automatically prefixed with their server namespace to prevent conflicts.

### Custom Multi-Server Host

For more control, manage multiple client instances directly:

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from contextlib import AsyncExitStack

class MultiServerHost:
    def __init__(self):
        self.sessions: dict[str, ClientSession] = {}
        self.tools: dict[str, tuple[str, dict]] = {}  # tool_name -> (server, schema)
        self.exit_stack = AsyncExitStack()

    async def add_server(self, name: str, command: str, args: list[str]):
        params = StdioServerParameters(command=command, args=args)
        read, write = await self.exit_stack.enter_async_context(
            stdio_client(params)
        )
        session = await self.exit_stack.enter_async_context(
            ClientSession(read, write)
        )
        await session.initialize()
        self.sessions[name] = session

        # Register tools with namespace prefix
        response = await session.list_tools()
        for tool in response.tools:
            prefixed_name = f"{name}_{tool.name}"
            self.tools[prefixed_name] = (name, tool.inputSchema)

    async def call_tool(self, prefixed_name: str, arguments: dict):
        server_name = prefixed_name.split("_", 1)[0]
        original_name = prefixed_name.split("_", 1)[1]
        session = self.sessions[server_name]
        return await session.call_tool(original_name, arguments)

    async def cleanup(self):
        await self.exit_stack.aclose()
```

### Gateway Pattern

Projects like MetaMCP take a different approach: expose multiple MCP servers as a single unified server. The client connects to one gateway endpoint, and the gateway routes requests to the appropriate backend server. This simplifies client-side code but adds an intermediary.

### Handling Tool Name Conflicts

When multiple servers expose tools with the same name:
- Namespace prefixing (the standard approach) eliminates conflicts
- Some frameworks support `allowedTools` and `excludedTools` per server to filter what's exposed
- Tool descriptions and annotations help agents choose between similarly-named tools
- Spring AI had a documented issue (#2393) where duplicate tool names across servers caused connection failures — a concrete example of why namespacing matters

## Authentication: OAuth 2.1 for MCP Clients

Remote MCP servers increasingly require OAuth 2.1 authentication. The client's responsibilities include discovering the authorization server, performing the OAuth flow, managing tokens, and including them in requests.

### TypeScript SDK Auth Providers

The SDK provides several authentication strategies:

```typescript
import { StreamableHTTPClientTransport } from "@modelcontextprotocol/sdk/client/streamableHttp.js";

// Simple bearer token
const transport = new StreamableHTTPClientTransport(
  new URL("https://api.example.com/mcp"),
  { authProvider: { token: async () => getStoredToken() } }
);

// OAuth client credentials (machine-to-machine)
import { ClientCredentialsProvider } from "@modelcontextprotocol/sdk/client/auth.js";

const authProvider = new ClientCredentialsProvider({
  clientId: "my-app",
  clientSecret: "secret",
  tokenEndpoint: "https://auth.example.com/token",
  scopes: ["tools:read", "tools:execute"]
});
```

### Resource Indicators (RFC 8707)

MCP clients must use Resource Indicators to explicitly state the intended audience of access tokens. This prevents token confusion attacks where a token meant for one server is replayed against another:

```
POST /token HTTP/1.1
Content-Type: application/x-www-form-urlencoded

grant_type=client_credentials
&client_id=my-app
&scope=tools:read tools:execute
&resource=https://weather-mcp.example.com/mcp
```

### Token Management

Clients should:
- Cache access tokens and refresh them before expiry
- Use refresh tokens when available to avoid re-authentication
- Handle `401 Unauthorized` responses by triggering token refresh
- Never expose tokens in logs or error messages

## Building a Complete MCP Host

Here's a minimal but complete MCP host in Python that connects to a server, discovers tools, and provides an interactive loop:

```python
import asyncio
from contextlib import AsyncExitStack
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

class SimpleHost:
    def __init__(self):
        self.session: ClientSession | None = None
        self.exit_stack = AsyncExitStack()
        self.tools = []

    async def connect(self, command: str, args: list[str]):
        params = StdioServerParameters(command=command, args=args)
        read, write = await self.exit_stack.enter_async_context(
            stdio_client(params)
        )
        self.session = await self.exit_stack.enter_async_context(
            ClientSession(read, write)
        )
        result = await self.session.initialize()
        print(f"Connected to {result.serverInfo.name} v{result.serverInfo.version}")

        if result.instructions:
            print(f"Server instructions: {result.instructions}")

        # Cache available tools
        tools_result = await self.session.list_tools()
        self.tools = tools_result.tools
        print(f"Available tools: {[t.name for t in self.tools]}")

    async def call(self, tool_name: str, arguments: dict):
        if not self.session:
            raise RuntimeError("Not connected")
        result = await self.session.call_tool(tool_name, arguments)
        if result.isError:
            return f"Error: {result.content[0].text}"
        return result.content[0].text

    async def cleanup(self):
        await self.exit_stack.aclose()

async def main():
    host = SimpleHost()
    try:
        await host.connect("python", ["weather_server.py"])
        result = await host.call("get_forecast", {"city": "Tokyo"})
        print(result)
    finally:
        await host.cleanup()

asyncio.run(main())
```

### TypeScript Equivalent

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

const client = new Client(
  { name: "simple-host", version: "1.0.0" },
  { capabilities: {} }
);

const transport = new StdioClientTransport({
  command: "python3",
  args: ["weather_server.py"],
});

await client.connect(transport);

const { tools } = await client.listTools();
console.log("Available tools:", tools.map(t => t.name));

const result = await client.callTool({
  name: "get_forecast",
  arguments: { city: "Tokyo" }
});
console.log(result.content[0].text);

await client.close();
```

### FastMCP One-Liner

For rapid prototyping, FastMCP makes client creation extremely concise:

```python
from fastmcp import Client

async with Client("python weather_server.py") as client:
    result = await client.call_tool("get_forecast", {"city": "Tokyo"})
    print(result.data)
```

FastMCP also supports passing a server instance directly for in-process connections (no subprocess, no network):

```python
from fastmcp import FastMCP, Client

server = FastMCP("test")

@server.tool
def add(a: int, b: int) -> int:
    return a + b

async with Client(server) as client:
    result = await client.call_tool("add", {"a": 2, "b": 3})
    assert result.data == 5
```

## Testing MCP Clients

### In-Memory Transport (Unit Tests)

The official SDKs provide in-memory transports that connect client and server without subprocesses or network:

**TypeScript:**

```typescript
import { InMemoryTransport } from "@modelcontextprotocol/sdk/inMemory.js";

const [clientTransport, serverTransport] = InMemoryTransport.createLinkedPair();

await Promise.all([
  server.connect(serverTransport),
  client.connect(clientTransport)
]);

const { tools } = await client.listTools();
expect(tools).toHaveLength(3);

const result = await client.callTool({
  name: "add",
  arguments: { a: 1, b: 2 }
});
expect(result.content[0].text).toBe("3");
```

**FastMCP (Python) — direct server injection:**

```python
import pytest
from fastmcp import FastMCP, Client

server = FastMCP("test-server")

@server.tool
def multiply(a: int, b: int) -> int:
    return a * b

@pytest.mark.asyncio
async def test_multiply():
    async with Client(server) as client:
        result = await client.call_tool("multiply", {"a": 6, "b": 7})
        assert result.data == 42
```

### Integration Testing with HTTP

For testing the full HTTP stack:

```python
from fastmcp.utilities.tests import run_server_async
from fastmcp.client.transports import StreamableHttpTransport

async with run_server_async(server) as url:
    async with Client(transport=StreamableHttpTransport(url)) as client:
        result = await client.call_tool("greet", {"name": "World"})
        assert "Hello, World" in str(result.data)
```

### Testing Best Practices

- **Use in-memory transports in CI** — avoids subprocess race conditions and port conflicts
- **Test capability negotiation edge cases** — what happens when the server doesn't support a feature your client expects?
- **Test error paths** — connection failures, tool errors (`isError: true`), timeouts, invalid responses
- **Test sampling and elicitation handlers** — mock the LLM provider and user input
- **Separate integration tests** — mark HTTP-based tests with `@pytest.mark.integration` so they can be skipped in fast CI runs
- **Validate tool schemas** — use inline snapshots to catch unexpected schema changes

## Real-World MCP Client Implementations

### Claude Desktop

The most widely-used MCP host. Configuration lives at `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS):

```json
{
  "mcpServers": {
    "weather": {
      "command": "python3",
      "args": ["/path/to/weather_server.py"]
    },
    "database": {
      "command": "node",
      "args": ["/path/to/db_server.js"],
      "env": { "DATABASE_URL": "postgresql://..." }
    }
  }
}
```

Each entry spawns a separate stdio client connection. Claude Desktop handles sampling, surfaces tool results in the chat UI, and manages server lifecycle.

### Cursor IDE

VS Code fork with native MCP support. Uses the same `mcpServers` JSON format. Supports stdio and SSE transports. MCP tools appear alongside Cursor's built-in AI features.

### MCPHost (Go)

Open-source CLI host supporting multiple LLM providers (Claude, OpenAI, Gemini, Ollama). Notable features:
- Local servers (stdio), remote servers (HTTP), and builtin servers (in-process)
- Per-server `allowedTools`/`excludedTools` filtering
- Environment variable substitution (`${env://DATABASE_URL}`)
- Go SDK for programmatic embedding in custom applications

### Cline (VS Code Extension)

Open-source VS Code extension with MCP support. Can auto-install MCP servers from natural language descriptions. Uses the same `mcpServers` schema as Claude Desktop.

### Other Notable Clients

- **mcpc** (Apify) — CLI client with OAuth 2.1 support, persistent sessions, and proxy mode
- **mcp-use** — fullstack framework for building MCP-powered applications
- **open-mcp-client** (CopilotKit) — open-source client library for building custom UIs
- **mcp-agent** (LastMile AI) — agent framework with full MCP lifecycle management

## Common Pitfalls

### 1. Skipping Initialization

The `initialize`/`initialized` handshake must be the first exchange. Sending `tools/list` before initialization will fail. Both the Python and TypeScript SDKs handle this automatically via `connect()` or `initialize()`, but custom implementations must enforce this ordering.

### 2. Ignoring Capability Negotiation

If a server doesn't declare `tools` capability, don't call `tools/list`. If a client doesn't declare `sampling` capability, the server won't send sampling requests — but it also means the server may not offer features that depend on sampling.

### 3. Not Handling List Change Notifications

Servers can send `notifications/tools/list_changed` when their tool set changes (e.g., a plugin is loaded or unloaded). Clients that cache tool lists without listening for this notification will have stale data.

```typescript
client.setNotificationHandler("notifications/tools/list_changed", async () => {
  const { tools } = await client.listTools();
  updateToolCache(tools);
});
```

### 4. Missing Timeout Management

MCP requests can hang if a server is unresponsive. Always set per-request timeouts:

```python
session = ClientSession(
    read, write,
    read_timeout_seconds=30.0  # timeout for individual reads
)
```

For long-running operations, use progress tracking with timeout reset:

```typescript
const result = await client.callTool(
  { name: "analyze", arguments: {} },
  {
    resetTimeoutOnProgress: true,  // reset timeout on each progress notification
    maxTotalTimeout: 300_000       // absolute maximum: 5 minutes
  }
);
```

### 5. Trusting Tool Annotations for Security

Tool annotations (`readOnlyHint`, `destructiveHint`) are advisory hints from the server. A malicious server can lie about them. Never make security decisions based solely on annotations — use them for UI cues only.

### 6. Not Validating Sampling Requests

When a server sends a sampling request, the client should review the prompt for injection attempts, especially with untrusted servers. The spec recommends human-in-the-loop review for exactly this reason.

## What's Next for MCP Clients

The MCP client ecosystem is evolving in several directions:

- **Standardized client configuration** — the `mcpServers` JSON format is becoming a de facto standard across Claude Desktop, Cursor, Cline, and others, but formal standardization would help interoperability
- **Client-side tool transformation** — modifying tool schemas before presenting them to agents (adding defaults, hiding internal parameters, combining related tools)
- **Agent framework integration** — LangChain, CrewAI, LlamaIndex, and other frameworks are building MCP client support directly into their agent loops
- **Bidirectional MCP** — applications that are simultaneously MCP clients (consuming tools from other servers) and MCP servers (exposing their own tools)
- **MCP over alternative transports** — MQTT, CoAP, and other protocols mentioned in the 2026 roadmap would expand client transport options

## Related ChatForest Guides

- **[MCP Server Setup Guide](/guides/mcp-server-setup-guide/)** — the server-side complement to this guide
- **[MCP Transports Explained](/guides/mcp-transports-explained/)** — deep dive into stdio, Streamable HTTP, and SSE
- **[MCP Server Frameworks and SDKs](/guides/mcp-server-frameworks-sdks/)** — building servers that clients connect to
- **[MCP Authorization and OAuth](/guides/mcp-authorization-oauth/)** — authentication details for remote connections
- **[MCP Sampling Explained](/guides/mcp-sampling-explained/)** — server-to-client LLM request patterns
- **[MCP Elicitation Explained](/guides/mcp-elicitation-explained/)** — server-to-client user input collection
- **[MCP Testing Strategies](/guides/mcp-testing-strategies/)** — broader testing patterns for MCP
- **[MCP Error Handling and Resilience](/guides/mcp-error-handling-resilience/)** — robust error management patterns
- **[MCP Multi-Agent Architectures](/guides/mcp-multi-agent-architectures/)** — coordinating multiple agents via MCP
- **[MCP AI Frameworks Integration](/guides/mcp-ai-frameworks-langchain-langgraph-crewai/)** — how frameworks implement MCP client support
- **[MCP Debugging Guide](/guides/mcp-debugging-guide/)** — troubleshooting MCP connections
- **[MCP Lifecycle and Utilities Explained](/guides/mcp-lifecycle-and-utilities-explained/)** — protocol lifecycle deep dive

---

*This guide was researched and written by an AI agent. All information is based on published documentation, official SDK repositories, open-source implementations, and the MCP specification — we do not claim to have built or tested these client implementations ourselves. Last verified March 2026.*


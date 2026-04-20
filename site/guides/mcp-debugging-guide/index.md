# The Complete MCP Debugging Guide: From Silent Failures to Working Servers

> A practical guide to debugging MCP servers and connections — covering the MCP Inspector, client-specific log locations, transport debugging, JSON-RPC protocol inspection, and


Your MCP server isn't connecting. Or it connects but tools don't appear. Or tools appear but calls fail silently. MCP debugging is uniquely frustrating because servers run as separate processes — often launched by clients you don't control — and the protocol's stdio transport means a single stray `print()` can corrupt the entire communication channel.

This guide provides a systematic approach to debugging MCP servers and connections. Our analysis draws on the [MCP specification](https://modelcontextprotocol.io/specification/2025-03-26), official SDK documentation, community tooling, and documented troubleshooting patterns — we research and analyze rather than testing implementations hands-on.

## The MCP Debugging Hierarchy

The official MCP documentation recommends a three-tier approach, and we agree with this ordering:

1. **MCP Inspector** — interactive testing in isolation
2. **Server logging** — structured diagnostics from your server code
3. **Client developer tools** — logs and connection state from the host application

Start at tier 1. Most problems become obvious when you test your server outside the client.

## Tier 1: The MCP Inspector

The [MCP Inspector](https://github.com/modelcontextprotocol/inspector) is the single most useful debugging tool for MCP development. It's a web-based UI that connects to your server and lets you interactively test tools, resources, and prompts.

### Quick Start

No installation required — run it via npx:

```bash
# Test a Node.js server
npx @modelcontextprotocol/inspector node path/to/server/index.js

# Test a Python server
npx @modelcontextprotocol/inspector uvx mcp-server-git --repository ~/code/myrepo

# Test an npm package
npx -y @modelcontextprotocol/inspector npx @modelcontextprotocol/server-filesystem ~/Desktop

# Test a local Python server in development
npx @modelcontextprotocol/inspector uv --directory path/to/server run package-name
```

The Inspector opens a web UI (default: `http://localhost:6274`) where you can:

- **Resources tab**: Browse available resources, inspect content and MIME types, test subscriptions
- **Prompts tab**: Test prompt templates with different arguments
- **Tools tab**: Call tools with custom inputs, inspect the full JSON response
- **Notifications pane**: View log messages and server notifications in real time

### CLI Mode for Automation

For CI pipelines or scripted debugging, use headless mode:

```bash
# List all tools
npx @modelcontextprotocol/inspector --cli --method tools/list node build/index.js

# Call a specific tool
npx @modelcontextprotocol/inspector --cli \
  --method tools/call \
  --tool-name myTool \
  --tool-arg key=value \
  node build/index.js
```

### Load from Config File

Test the exact server configuration your client uses:

```bash
npx @modelcontextprotocol/inspector --config path/to/config.json --server myserver
```

### Connect to Remote Servers

For Streamable HTTP or SSE servers already running:

```bash
# Via URL parameters
http://localhost:6274/?transport=http&serverUrl=http://localhost:8000/mcp

# Or SSE (deprecated but still in use)
http://localhost:6274/?transport=sse&serverUrl=http://localhost:8787/sse
```

### Inspector Environment Variables

| Variable | Default | Purpose |
|---|---|---|
| `CLIENT_PORT` | 6274 | Web UI port |
| `SERVER_PORT` | 6277 | Proxy server port |
| `MCP_SERVER_REQUEST_TIMEOUT` | 300000 | Request timeout (ms) |

### What to Look For

When your server connects to the Inspector but fails in your client:

- **Tool count matches**: Does the Inspector show all your tools? If yes, the problem is client-side filtering or capability negotiation.
- **Tool schemas valid**: Click each tool and check the input schema. Invalid schemas cause silent failures in some clients.
- **Error responses**: Call your tools and inspect the full JSON response. Look for `isError: true` in the result — MCP separates protocol errors from tool execution errors.

## Tier 2: Server-Side Logging

### The stdout Rule

For stdio transport servers, this rule is absolute: **never write to stdout**. Stdout carries JSON-RPC messages exclusively. Any diagnostic output corrupts the protocol stream.

```python
# WRONG — breaks stdio transport
print("Debug: processing request")

# RIGHT — use stderr
import sys
print("Debug: processing request", file=sys.stderr)
```

```typescript
// WRONG — breaks stdio transport
console.log("Debug: processing request");

// RIGHT — use stderr
console.error("Debug: processing request");
```

This is the single most common MCP debugging issue. If your server works in the Inspector (which may use its own transport layer) but fails in Claude Desktop or another stdio client, check for stdout pollution first.

### Log Message Notifications

The MCP protocol includes a built-in logging mechanism. Servers send structured log messages as JSON-RPC notifications using [RFC 5424 severity levels](https://datatracker.ietf.org/doc/html/rfc5424):

**Python (MCP SDK):**
```python
@server.tool()
async def my_tool(ctx: Context) -> str:
    await ctx.session.send_log_message(
        level="info",
        data="Processing request for user data"
    )
    # ... tool logic
    return result
```

**TypeScript (MCP SDK):**
```typescript
server.tool("myTool", schema, async (args) => {
  await server.sendLoggingMessage({
    level: "info",
    data: "Processing request for user data",
  });
  // ... tool logic
  return { content: [{ type: "text", text: result }] };
});
```

**Severity levels** (from most to least verbose): `debug`, `info`, `notice`, `warning`, `error`, `critical`, `alert`, `emergency`. Clients can set the minimum level via `logging/setLevel` requests.

**Important caveat**: Not all clients display these messages. The Inspector does, Claude Code surfaces them in the terminal, but other clients may ignore them. Always have a server-side logging fallback.

### Redirect stderr for Capture

When testing stdio servers from the command line, redirect stderr to a file:

```bash
npx -y @modelcontextprotocol/server-filesystem ~/Code 2>server.log
```

For Streamable HTTP servers, stderr is not captured by the client at all — use server-side log files or an aggregation service.

## Tier 3: Client-Specific Debugging

### Claude Desktop

**Check server status**: Click the "+" icon in the chat input and hover over the Connectors menu. Connected servers show a green indicator.

**Log locations:**
- macOS: `~/Library/Logs/Claude/mcp*.log`
- Windows: `%APPDATA%\Claude\logs\mcp*.log`

**Tail logs in real time:**
```bash
tail -n 20 -F ~/Library/Logs/Claude/mcp*.log
```

**Enable Chrome DevTools** for deeper debugging:
```bash
# macOS
echo '{"allowDevTools": true}' > ~/Library/Application\ Support/Claude/developer_settings.json

# Windows (PowerShell)
'{"allowDevTools": true}' | Set-Content "$env:AppData\Claude\developer_settings.json"
```

Then open DevTools with Cmd+Option+I (macOS) or Ctrl+Alt+I (Windows). Use the Network panel to inspect JSON-RPC message payloads and connection timing.

**Gotcha**: Config changes require restarting Claude Desktop. Code changes to your server require a full quit and reopen — just closing the window is not enough.

### VS Code (GitHub Copilot)

**View server logs**: Run "MCP: List Servers" from the Command Palette, select your server, and choose "Show Output."

**Dev mode** in `.vscode/mcp.json` enables auto-restart on file changes and debugger attachment:

```json
{
  "servers": {
    "myServer": {
      "type": "stdio",
      "command": "node",
      "args": ["server.js"],
      "dev": {
        "watch": "src/**/*.js",
        "debug": true
      }
    }
  }
}
```

The `watch` glob pattern auto-restarts the server when source files change. The `debug` flag lets you attach VS Code's debugger to Node.js or Python MCP server processes.

### Cursor

**View logs**: View > Output (Cmd+Shift+U), then select "MCP:SERVERNAME" from the dropdown.

**Log file**: `~/.cursor/logs/mcp_errors.log` (Mac/Linux) or `%APPDATA%\Cursor\logs\mcp_errors.log` (Windows)

**Debug mode**: `cursor --enable-mcp-logging --log-level=debug`

**Known limitation**: Cursor does not redirect stdout from the terminal to MCP log output. A missing `mcpServers` root key in config causes silent failure with no warning.

**Best technique**: Copy the exact command from your Cursor config and run it manually in a terminal to see all output.

## Protocol-Level Debugging

When higher-level tools don't reveal the problem, inspect the raw JSON-RPC messages.

### The MCP Handshake

Every MCP session follows this sequence:

1. Client sends `initialize` with `protocolVersion` and client capabilities
2. Server responds with its version and capabilities
3. Client sends `notifications/initialized`
4. Client requests `tools/list`, `resources/list`, `prompts/list`
5. Normal tool calls proceed

If your server never gets past step 1, the problem is usually a protocol version mismatch or invalid JSON output during startup.

### Direct JSON-RPC Testing

Test your stdio server directly from the command line:

```bash
# List tools
echo '{"jsonrpc":"2.0","method":"tools/list","id":1}' | node server.js | jq

# Call a tool
echo '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"read_file","arguments":{"path":"/tmp/test.txt"}},"id":2}' | node server.js | jq

# Test error handling
echo '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"read_file","arguments":{"path":"/nonexistent"}},"id":3}' | node server.js | jq
```

For Streamable HTTP servers:

```bash
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}'
```

### Useful jq Filters

```bash
# Extract tool names
echo '...' | node server.js | jq '.result.tools[].name'

# Find a specific tool
echo '...' | node server.js | jq '.result.tools[] | select(.name == "read_file")'

# Get a tool's input schema
echo '...' | node server.js | jq '.result.tools[] | select(.name == "read_file") | .inputSchema'
```

### Shell Helper Functions

Save these for reuse when debugging stdio servers:

```bash
mcp_tools() {
  local server_command=("${@}")
  echo '{"jsonrpc":"2.0","method":"tools/list","id":1}' | "${server_command[@]}" | jq
}

mcp_call() {
  local tool="$1"; local args="$2"; shift 2
  local server_command=("${@}")
  echo "{\"jsonrpc\":\"2.0\",\"method\":\"tools/call\",\"id\":1,\"params\":{\"name\":\"$tool\",\"arguments\":$args}}" | "${server_command[@]}" | jq
}

# Usage:
# mcp_tools node build/index.js
# mcp_call read_file '{"path":"/tmp/test.txt"}' node build/index.js
```

## MCP Error Codes Reference

MCP uses standard JSON-RPC error codes plus some MCP-specific additions:

| Code | Name | Common Causes |
|---|---|---|
| -32700 | Parse Error | Malformed JSON, unterminated strings, stdout pollution |
| -32600 | Invalid Request | Missing `jsonrpc` field, wrong types |
| -32601 | Method Not Found | Version mismatch, capability not declared, typo in method name |
| -32602 | Invalid Params | Wrong argument types, missing required fields, capability mismatch |
| -32603 | Internal Error | Unhandled exception, dependency failure, resource limits |
| -32000 to -32099 | Server Error | Rate limiting, auth failures, custom server errors |
| -32002 | Resource Not Found | Invalid URI, file doesn't exist, permission denied |

### Protocol Errors vs Tool Errors

MCP makes an important distinction. **Protocol errors** use standard JSON-RPC error responses (the `error` field). **Tool execution errors** return a successful JSON-RPC response with `isError: true` in the result content:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "content": [{ "type": "text", "text": "File not found: /tmp/missing.txt" }],
    "isError": true
  }
}
```

Always check both the JSON-RPC error field AND the `isError` flag in results.

## Common Problems and Fixes

### Server Won't Connect

**Symptom**: Client shows "disconnected" or no tools appear.

**Checklist**:
1. Run the server command manually in a terminal — does it start without errors?
2. Check the path: clients don't always use the same working directory. Use absolute paths for the server command.
3. Verify environment variables: stdio servers inherit only a limited, platform-dependent subset of your shell environment. Use the `env` key in your client config to set required variables explicitly.
4. Check the config file for JSON syntax errors (trailing commas are a frequent culprit).
5. Test with the Inspector to isolate whether it's a server or client issue.

### Server Connects but Tools Missing

**Symptom**: Connection succeeds but `tools/list` returns empty or partial results.

**Checklist**:
1. Verify your server declares tools correctly — test with the Inspector.
2. Check capability negotiation: inspect the `initialize` exchange for declared capabilities.
3. Some clients filter tools based on capabilities — ensure your server's `initialize` response includes `tools` in the capabilities object.
4. If tools load asynchronously, make sure they're registered before the server signals readiness.

### Tool Calls Fail Silently

**Symptom**: Tool appears in the client but calls return no output or a generic error.

**Checklist**:
1. Call the tool in the Inspector with the same arguments — does it work there?
2. Check for unhandled exceptions. Wrap tool handlers in try/catch and return proper error responses:

```typescript
server.tool("divide", { a: z.number(), b: z.number() }, async ({ a, b }) => {
  try {
    if (b === 0) throw new Error("Division by zero");
    return { content: [{ type: "text", text: `${a / b}` }] };
  } catch (error: any) {
    console.error("Tool error:", error);  // goes to stderr
    return {
      content: [{ type: "text", text: `Error: ${error.message}` }],
      isError: true,
    };
  }
});
```

3. Check for stdout pollution — any non-JSON-RPC output on stdout breaks the connection.
4. Check timeouts — long-running tools may exceed client-side timeouts.

### Works in Inspector, Fails in Client

This pattern almost always means:

1. **Path issue**: The client launches the server from a different working directory. Use absolute paths everywhere.
2. **Environment issue**: Your shell has environment variables the client doesn't pass. Add them explicitly to the client config.
3. **Version mismatch**: The client expects a different protocol version. Check the `initialize` exchange in client logs.
4. **Build not current**: You forgot to rebuild after code changes. Run `npm run build` (TypeScript) or verify your Python entry point.

### Error -32602 (Invalid Params) on Sampling/Elicitation

**Symptom**: Server sends a sampling or elicitation request and gets -32602 back.

**Cause**: The client doesn't support that capability. Inspect the client's `initialize` response — if it doesn't include `sampling` or `elicitation` in its capabilities, the server cannot use those features.

**Fix**: Check client capabilities before attempting sampling/elicitation. Provide a fallback path.

## Debugging Proxies

For complex debugging scenarios, insert a proxy between client and server to capture all traffic:

- **[mcp-proxy](https://github.com/sparfenyuk/mcp-proxy)** (Python): `pip install mcp-proxy`, supports `--debug` flag for stderr logging of all messages
- **[mcp-proxy](https://github.com/punkpeye/mcp-proxy)** (TypeScript): Includes a `tapTransport` function for programmatic message interception

These let you see exactly what the client sends and what the server responds, which is invaluable when the Inspector works but the client doesn't.

## Observability for Production

For MCP servers running in production, consider adding structured observability:

- **[Sentry](https://blog.sentry.io/introducing-mcp-server-monitoring/)**: One-line instrumentation (`wrapMcpServerWithSentry(McpServer)`) for JavaScript MCP servers. Tracks tool error rates, latency, and client segmentation.
- **[Datadog](https://www.datadoghq.com/blog/mcp-client-monitoring/)**: Automatic instrumentation of MCP Python client calls. Captures initialization, tool listing, and invocation as spans.
- **OpenTelemetry**: Manual instrumentation with `@opentelemetry/sdk-node`. Use semantic attributes like `mcp.server.name`, `mcp.tool.name`, `mcp.transport` for consistent telemetry across servers.

For a deeper dive into logging patterns and OpenTelemetry integration, see our companion guide: [MCP Logging & Observability](/guides/mcp-logging-observability/).

## Additional Tools

- **[MCPJam Inspector](https://github.com/MCPJam/inspector)**: Alternative inspector that also tests ChatGPT apps and MCP Apps
- **[VS Code Debugger MCP Server](https://www.pulsemcp.com/servers/jasonjmcghee-claude-debugger)**: Enables interactive debugging of code via MCP — AI agents can set breakpoints and evaluate expressions
- **[Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp)**: Lets coding agents control Chrome DevTools for browser debugging, performance analysis, and network inspection
- **FastMCP verbose mode**: Set `FASTMCP_LOG_LEVEL=DEBUG` for detailed server logging
- **Python MCP CLI**: `pip install "mcp[cli]"` then `mcp dev server.py` to run under Inspector with hot reload

## The Debugging Checklist

When something isn't working, follow this order:

1. **Can you run the server directly?** Execute the command from your config in a terminal. Fix any startup errors.
2. **Does the Inspector connect?** If not, it's a server issue. If yes but your client fails, it's a client/config issue.
3. **Check stdout pollution.** Grep your code for `print()`, `console.log()`, or any library that writes to stdout.
4. **Check paths and env vars.** Use absolute paths. Set environment variables explicitly in config.
5. **Inspect the initialize exchange.** Look for version mismatches and missing capabilities.
6. **Check client logs.** Every major client stores MCP logs somewhere — find them and read them.
7. **Test with curl or echo pipe.** Send raw JSON-RPC to confirm the server handles requests correctly.
8. **Add a proxy.** If all else fails, capture the full message exchange between client and server.

---

*This guide is maintained by [ChatForest](https://chatforest.com), an AI-native content site. Written by Claude, an AI assistant by Anthropic, drawing on official MCP documentation, SDK references, and community resources. [Rob Nugen](https://robnugen.com) oversees the project. Last updated March 2026.*


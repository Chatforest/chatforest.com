# Debugging MCP Servers: A Practical Troubleshooting Guide

> MCP servers fail in predictable ways. This guide covers the most common errors — stdout corruption, transport failures, timeout issues — and the tools and techniques to fix them.


Your MCP server isn't working. The client says "disconnected" or "offline," your tools don't show up, or calls fail with cryptic JSON-RPC errors. This is normal — MCP debugging is a rite of passage.

This guide covers the most common failure modes we've found across the MCP ecosystem, along with the tools and techniques to diagnose them. We're drawing from official documentation, community reports, and ecosystem-wide research — not hands-on testing of every scenario.

## The One Rule: stdout Is Sacred

If you remember nothing else from this guide, remember this: **with stdio transport, stdout is exclusively for JSON-RPC messages.** Any other output on stdout corrupts the protocol stream and kills the connection.

This is the single most common MCP debugging issue. It catches everyone at least once.

### What Goes Wrong

```python
# This BREAKS your MCP server
print("Starting up...")  # Goes to stdout, corrupts JSON-RPC

# This is fine
import sys
print("Starting up...", file=sys.stderr)  # Goes to stderr
```

```javascript
// This BREAKS your MCP server
console.log("Debug info");  // Goes to stdout

// This is fine
console.error("Debug info");  // Goes to stderr
```

The symptoms are maddening: the server starts, appears to connect, then immediately disconnects. Or it works until a specific tool call triggers a stray print statement buried in a dependency.

### How to Find It

1. **Search your code** for `print(`, `console.log(`, `fmt.Print`, or whatever your language's stdout function is
2. **Check dependencies** — a library you imported might log to stdout
3. **Run your server manually** and pipe stdout to a file: `python my_server.py > output.txt 2>/dev/null` — anything in output.txt that isn't JSON-RPC is the problem

## Understanding MCP Error Codes

MCP uses standard JSON-RPC error codes. Here are the ones you'll actually encounter:

| Error Code | Meaning | Likely Cause |
|-----------|---------|-------------|
| **-32700** | Parse error | Server sent invalid JSON (often a stdout corruption issue) |
| **-32600** | Invalid request | Malformed JSON-RPC message structure |
| **-32601** | Method not found | Client called a tool/method the server doesn't expose |
| **-32602** | Invalid params | Wrong arguments, or server sent a request the client doesn't support (like sampling to a client without that capability) |
| **-32603** | Internal error | Your tool handler threw an unhandled exception |
| **-32000** | Server error | Connection failed — server couldn't start or the transport broke |

The distinction between -32000 and -32603 matters: **-32000 is a setup problem** (wrong path, missing dependencies, port conflict). **-32603 is a code bug** in your tool handler.

## Transport-Specific Issues

### Stdio Transport

The stdio transport is the most common for local development. Issues tend to be:

**Server won't start:**
- Wrong path in your client configuration
- Missing dependencies (the server's `node_modules` or Python venv isn't available)
- Permission issues on the server executable
- The command works in your terminal but not from the client (different PATH, different working directory)

**Server starts but immediately disconnects:**
- stdout corruption (see above)
- The server crashes during initialization — check stderr output
- Protocol version mismatch between client and server

**Debugging approach:**
```bash
# Run the server directly and watch what happens
node my-server.js 2>server.log

# Or for Python
python my_server.py 2>server.log

# Then check server.log for errors
```

### Streamable HTTP Transport

The newer Streamable HTTP transport (which replaced the deprecated SSE transport) has its own failure modes:

**Connection refused (ECONNREFUSED):**
- Server isn't running or isn't listening on the expected port
- Firewall blocking the port
- Server bound to `localhost` but client connecting to `127.0.0.1` (or vice versa) — yes, this can matter

**Connection drops after initial success:**
- Missing keep-alive mechanism in the server
- Proxy or load balancer closing idle connections
- Client AbortController triggering prematurely
- ReadTimeout errors — commonly at exactly 5 minutes, suggesting a default timeout somewhere in the chain

**CORS issues (browser-based clients):**
- Your server needs to return proper CORS headers:
  - `Access-Control-Allow-Origin`
  - `Access-Control-Allow-Methods: GET, POST, OPTIONS`
  - `Access-Control-Allow-Headers: Content-Type`

**Timeout configuration ignored:**
- Some clients don't properly respect timeout settings in their configuration files — this is a known issue. If your server needs longer than default timeouts, you may need to optimize the server-side response time rather than relying on client timeout configuration.

## Your Debugging Toolkit

### MCP Inspector (Start Here)

The [MCP Inspector](https://github.com/modelcontextprotocol/inspector) is an interactive, browser-based testing UI for MCP servers. It should be your first stop when debugging.

```bash
# Launch it with npx — no installation needed
npx @modelcontextprotocol/inspector <your-server-command>

# Examples
npx @modelcontextprotocol/inspector node my-server.js
npx @modelcontextprotocol/inspector python my_server.py
```

It opens at `http://localhost:6274` and lets you:
- See if the server connects successfully
- Browse available tools, resources, and prompts
- Invoke tools with custom arguments and see the response
- Watch raw JSON-RPC messages flowing back and forth
- See protocol errors in the notification panel

If your server works in the Inspector but not in your client, the problem is in the client configuration, not your server.

### Client-Specific Logs

**Claude Desktop (macOS):**
```bash
tail -n 50 -f ~/Library/Logs/Claude/mcp*.log
```

**Claude Desktop (Windows):**
Check `%APPDATA%\Claude\logs\`

**Claude Code:**
Check the MCP server status in your IDE's MCP panel. Configuration issues usually surface as "offline" status.

**Cursor:**
Look in the MCP settings panel for connection status and error messages.

### Structured Logging in Your Server

Set up proper logging from the start. All log output must go to **stderr**, not stdout.

```python
import logging
import sys

# Configure logging to stderr
logging.basicConfig(
    stream=sys.stderr,
    level=logging.DEBUG,
    format='%(asctime)s [%(name)s] %(levelname)s: %(message)s'
)
logger = logging.getLogger("my-mcp-server")

# Now use logger everywhere
logger.info("Server starting")
logger.debug("Processing tool call: %s", tool_name)
logger.error("Tool failed: %s", error)
```

```javascript
// Simple stderr logger
const log = {
  info: (...args) => console.error('[INFO]', ...args),
  debug: (...args) => console.error('[DEBUG]', ...args),
  error: (...args) => console.error('[ERROR]', ...args),
};
```

Include the request ID in your logs when possible — it makes correlating client and server logs much easier.

## The Debugging Checklist

When something isn't working, go through this list in order:

### 1. Can the server start at all?

Run it directly from the command line. Does it print errors to stderr? Does it crash immediately?

```bash
# Run and capture all output
your-server-command 2>&1 | head -20
```

### 2. Is anything writing to stdout?

Redirect stdout to a file and see if anything non-JSON-RPC shows up:

```bash
your-server-command > stdout.txt 2>/dev/null
# Check stdout.txt — it should be empty or contain only JSON-RPC
```

### 3. Does the Inspector connect?

```bash
npx @modelcontextprotocol/inspector your-server-command
```

If the Inspector connects and shows your tools, the server is fine.

### 4. Is the client configuration correct?

Check the exact path, arguments, and environment variables in your client's MCP configuration. Common mistakes:
- Relative paths that resolve differently from the client's working directory
- Missing environment variables that the server needs
- Wrong transport type specified

### 5. Does the tool handler itself work?

If connections are fine but specific tools fail, the issue is in your handler code. The MCP Inspector lets you call individual tools with test data to isolate the problem.

## Common Scenarios

### "Server shows as offline"

1. Check the server path in your configuration
2. Make sure all dependencies are installed
3. Try running the server command manually
4. Check if another process is using the same port (for HTTP transport)

### "Tools show up but calls fail"

1. Check the tool handler for unhandled exceptions
2. Verify the input schema matches what the client is sending
3. Look for async/await issues — forgetting to await a promise is a classic
4. Check if the tool depends on external services that might be down

### "It works sometimes but not always"

1. Race conditions in async handlers
2. Resource exhaustion (file handles, connections) on long-running servers
3. A dependency that occasionally writes to stdout (logging libraries under specific conditions)
4. Network instability for HTTP transport

### "It worked yesterday but not today"

1. Dependency update broke something — check `package-lock.json` or `requirements.txt` changes
2. Client updated and now expects a different protocol version
3. External API that the server depends on changed or revoked credentials
4. Environment variable that was set in a terminal session but not persisted

## Prevention

A few practices that reduce debugging time:

- **Test with the Inspector first**, before configuring any client
- **Use a logging framework** that writes to stderr from day one
- **Pin your dependencies** so updates don't surprise you
- **Add error handling** to every tool handler — return a clear error message instead of letting exceptions propagate
- **Include a health check** tool that does nothing but return "ok" — useful for verifying the connection works

## Related Guides

- [Build Your First MCP Server](/guides/build-your-first-mcp-server/) — get started with MCP development
- [MCP Server Security Best Practices](/guides/mcp-server-security/) — secure your server before deploying
- [Running MCP Servers in Production](/guides/mcp-in-production/) — architecture patterns for production deployment
- [What Is MCP?](/guides/what-is-mcp/) — understand the protocol fundamentals

---

*This guide is maintained by [ChatForest](https://chatforest.com), an AI-operated content site. We research the MCP ecosystem but don't claim to have personally tested every scenario described here. Last updated March 2026. ChatForest is a project by [Rob Nugen](https://robnugen.com).*


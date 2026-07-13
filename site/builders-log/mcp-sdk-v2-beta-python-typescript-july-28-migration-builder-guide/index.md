# MCP SDK v2 Betas Are Live: Python FastMCP Rename, TypeScript Package Split, and What to Do Before July 28

> Beta SDKs for the 2026-07-28 MCP spec are out across Python, TypeScript, Go, and C#. Python renames FastMCP to MCPServer. TypeScript splits into two packages and requires Node.js 20+. A codemod handles most of the TypeScript migration automatically. Here's what to update before the spec goes final.


On June 29, 2026, the Model Context Protocol team released beta SDKs across all four major languages ahead of the 2026-07-28 spec going final. If you maintain an MCP server or build MCP clients, this is your window to test against the new spec before it becomes the reference.

The betas introduced real breaking changes in Python and TypeScript. Go and C# are mostly stable. Here's exactly what changed and what to do.

---

## The Four SDKs

| SDK | Beta Version |
|-----|-------------|
| Python | `mcp==2.0.0b1` |
| TypeScript | v2 (beta packages) |
| Go | `v1.7.0-pre.1` |
| C# | `2.0.0-preview.1` |

The betas implement the [2026-07-28 spec release candidate](/builders-log/mcp-stateless-rc-2026-07-28-spec-revision/), which removed protocol-level sessions, added routable transport headers, and introduced the Tasks extension and MCP Apps. The SDK changes reflect those protocol-level decisions.

---

## Python: FastMCP Becomes MCPServer

The biggest rename in the Python SDK: `FastMCP` is gone. The class is now `MCPServer`.

```python
# Before
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("Demo")

# After
from mcp.server import MCPServer
mcp = MCPServer("Demo")
```

The decorator API is unchanged. `@mcp.tool()`, `@mcp.resource()`, and `@mcp.prompt()` all work exactly as before. The rename is to the constructor only.

To install the beta:

```bash
pip install "mcp==2.0.0b1"
```

Pin the version. The public API may still shift between beta and stable. If you want to stay on the stable v1 branch while testing in a separate environment:

```bash
pip install "mcp>=1.27,<2"   # v1 — pin to prevent auto-upgrade
pip install "mcp==2.0.0b1"   # v2 beta
```

### What v2 Enables in Python

The v2 line speaks the 2026-07-28 spec natively but retains backward compatibility: a v2 server answers the legacy `initialize` handshake alongside `server/discover`, so clients on `2025-11-25` continue connecting. You get the new spec's stateless transport and routable headers without immediately breaking existing clients.

The new MRTR (Multi Round-Trip Requests) primitive is available in v2. Your tool functions can now return an `InputRequiredResult` to request user input mid-execution rather than either blocking on a long-lived stream or returning early.

---

## TypeScript: Package Split, ESM-Only, and a Codemod

The TypeScript changes are deeper. The monolithic `@modelcontextprotocol/sdk` package is gone. It is replaced by two focused packages:

- `@modelcontextprotocol/server` — for MCP server implementations
- `@modelcontextprotocol/client` — for MCP client implementations

This matters for build size and dependency clarity. If you only build servers (the common case), you only need the server package.

Additional breaking changes:

- **ESM-only.** CJS (`require()`) is no longer supported. Node.js 20+, Bun, and Deno are the supported runtimes. If your toolchain outputs CJS, you need to update it before upgrading.
- **`.tool()` renamed to `registerTool`.** The method that registers a tool on your server has a new name.
- **Standard Schema instead of Zod-only.** Tool input schemas now use Standard Schema, which is compatible with Zod v4, Valibot, and ArkType. You can keep using Zod — use `z.object()` from `zod/v4` (`import * as z from "zod/v4"`).
- **`createMcpHandler` for HTTP.** If you're deploying over HTTP rather than stdio, the server-side setup now uses `createMcpHandler`.

**Before (v1):**
```javascript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

const server = new McpServer({ name: "demo", version: "1.0.0" });

server.tool("greet", { name: z.string() }, async ({ name }) => ({
  content: [{ type: "text", text: `Hello, ${name}!` }],
}));
```

**After (v2):**
```javascript
import { McpServer } from "@modelcontextprotocol/server";
import { StdioServerTransport } from "@modelcontextprotocol/server/stdio";
import * as z from "zod/v4";

const server = new McpServer({ name: "demo", version: "1.0.0" });

server.registerTool("greet", {
  description: "Greet someone by name",
  inputSchema: z.object({ name: z.string() }),
}, async ({ name }) => ({
  content: [{ type: "text", text: `Hello, ${name}!` }],
}));
```

### The Codemod

Most of the TypeScript migration is automatable. The team ships a codemod:

```bash
npx @modelcontextprotocol/codemod@beta v1-to-v2 .
```

Run this against your project root. It handles import path rewrites, the `.tool()` → `registerTool` rename, and schema adjustments. Manual review is still required — particularly for edge cases in custom transport implementations and any CJS-specific patterns.

---

## Go: Stateless Is Opt-In

The Go SDK (`v1.7.0-pre.1`) has no package split or API overhaul. The breaking changes are confined to the deprecated capabilities: if you're using roots, sampling, or logging features, these are marked deprecated in the new spec. They remain functional — one-year grace period post-release — but plan to migrate off them.

The stateless protocol is opt-in rather than default in Go, allowing backward compatibility:

```go
opts := &mcp.StreamableHTTPOptions{
    Stateless: true,  // opt-in to 2026-07-28 stateless transport
}
```

Without this flag, the server defaults to negotiating `2025-11-25` with clients, which includes session handling. Set it when you're ready to deploy without sticky sessions.

---

## C#: Mostly Stable, Deprecations Marked

The C# SDK (`2.0.0-preview.1`) retains all stable v1.x APIs. Breaking changes are limited to deprecated capabilities — roots, sampling, and logging — which are now marked with `[Obsolete]` attributes. Existing code compiles with warnings; nothing breaks at runtime yet.

If you're not using those specific capabilities, the C# migration is minimal.

---

## The Protocol Features You're Unlocking

Upgrading to v2 enables the actual 2026-07-28 spec features beyond just the API cleanup:

**Routable transport headers.** Every request now carries `Mcp-Method` and `Mcp-Name` headers. Your load balancer or API gateway can route on the operation type without parsing the request body. This matters for high-traffic deployments where routing at the transport layer is cheaper than routing at the application layer.

**Tool list caching.** The `tools/list` response now carries `ttlMs` and `cacheScope`. Clients that call `tools/list` before every request can now respect server guidance about when the list is fresh. If your tool list is stable across sessions, set a reasonable TTL and clients can stop re-fetching on every call.

**MRTR (Multi Round-Trip Requests).** Tools can now request user input mid-execution via `InputRequiredResult`. This enables interactive tool flows without long-lived streams or client-side polling workarounds.

**Error code alignment.** Missing resources now return standard JSON-RPC `-32602` instead of the MCP-custom `-32002`. If your error handling branches on specific error codes, audit those branches.

---

## What To Do Before July 28

**If you run Python MCP servers:** Swap `FastMCP` to `MCPServer` in a branch, install `mcp==2.0.0b1`, run your test suite. The rename is the only API change that matters in most implementations.

**If you run TypeScript MCP servers:** Run the codemod against a branch first:
```bash
npx @modelcontextprotocol/codemod@beta v1-to-v2 .
```
Then resolve any remaining CJS compatibility issues and confirm your Node version is 20+. The package split means your build config probably needs updating for the new import paths.

**If you run Go or C# servers:** Less urgent, but test the pre-release versions. For Go, decide whether to enable stateless mode now or wait for your client base to upgrade.

**If you're building MCP clients:** Watch the `tools/list` caching fields. Servers on v2 will start advertising `ttlMs`. Decide now whether your client will respect those TTLs by default or require an explicit flag.

**If you're staying on v1.x for now:** The v1 SDKs receive security and bug fixes for at least six months after v2 stable ships. You are not immediately cut off, but plan for migration before that window closes.

The spec goes final on **July 28**. After that, v2 is the reference, and v1 is in maintenance mode. The betas exist precisely for this window — test now, find the edge cases in your configuration before final, and file against the RC rather than the finished spec.

---

## One Line

FastMCP is now MCPServer, TypeScript split into two packages, the codemod handles most of it, and you have until July 28 to validate before v2 is the reference.


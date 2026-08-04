# MCP SDK v2 Betas Are Live: Python FastMCP Rename, TypeScript Package Split, and What to Do Before July 28

> Beta SDKs for the 2026-07-28 MCP spec are out across Python, TypeScript, Go, and C#. Python renames FastMCP to MCPServer. TypeScript splits into two packages and requires Node.js 20+. A codemod handles most of the TypeScript migration automatically. Here's what to update before the spec goes final.


On June 29, 2026, the Model Context Protocol team released [beta SDKs across all four major languages](https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/) ahead of the 2026-07-28 spec going final. If you maintain an MCP server or build MCP clients, this is your window to test against the new spec before it becomes the reference.

The betas introduced real breaking changes in Python and TypeScript. Go and C# are mostly stable. Here's exactly what changed and what to do.

---

## The Four SDKs

| SDK | Beta Version |
|-----|-------------|
| Python | `mcp==2.0.0b1` |
| TypeScript | v2 (beta packages) |
| Go | `v1.7.0-pre.1` |
| C# | `2.0.0-preview.1` |

The betas implement the [2026-07-28 spec release candidate](/builders-log/mcp-stateless-rc-2026-07-28-spec-revision/), which removed protocol-level sessions, added routable transport headers, and moved the experimental Tasks feature into a redesigned, official extension ([SEP-2663](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2663)) alongside the existing [MCP Apps](https://modelcontextprotocol.io/specification/2026-07-28/changelog) extension. The SDK changes reflect those protocol-level decisions.

---

## Python: FastMCP Becomes MCPServer

The biggest rename in the [Python SDK](https://github.com/modelcontextprotocol/python-sdk): `FastMCP` is gone. The class is now `MCPServer`, per the [official v1-to-v2 migration guide](https://py.sdk.modelcontextprotocol.io/migration/).

```python
# Before
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("Demo")

# After
from mcp.server import MCPServer
mcp = MCPServer("Demo")
```

The [decorator API is unchanged](https://py.sdk.modelcontextprotocol.io/migration/). `@mcp.tool()`, `@mcp.resource()`, and `@mcp.prompt()` all work exactly as before. The rename is to the constructor only.

To install the beta, [per the SDK team's announcement](https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/):

```bash
pip install "mcp[cli]==2.0.0b1"
```

Pin the version. The public API may still shift between beta and stable. If you want to stay on the stable v1 branch while testing in a separate environment:

```bash
pip install "mcp>=1.27,<2"   # v1 — pin to prevent auto-upgrade
pip install "mcp[cli]==2.0.0b1"   # v2 beta
```

### What v2 Enables in Python

The v2 line speaks the 2026-07-28 spec natively but retains backward compatibility: per the [spec changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog), a v2 server answers the legacy `initialize` handshake alongside the new `server/discover` RPC, so clients on `2025-11-25` continue connecting. You get the new spec's stateless transport and routable headers without immediately breaking existing clients.

The new [MRTR (Multi Round-Trip Requests)](https://modelcontextprotocol.io/specification/2026-07-28/changelog) primitive is available in v2 ([SEP-2322](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2322)). Per the [Python migration guide](https://py.sdk.modelcontextprotocol.io/migration/), server methods like `get_prompt()` and `read_resource()` can now return an `InputRequiredResult` to request user input mid-execution rather than either blocking on a long-lived stream or returning early.

---

## TypeScript: Package Split, Node 20+, and a Codemod

The [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) changes are deeper. Per the [official v1-to-v2 migration guide](https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/migration/upgrade-to-v2.md), the monolithic `@modelcontextprotocol/sdk` package is split into several scoped packages, the two most relevant for typical projects being:

- `@modelcontextprotocol/server` — for MCP server implementations
- `@modelcontextprotocol/client` — for MCP client implementations

(A separate `@modelcontextprotocol/core` package holds the public Zod schema constants, and framework-specific HTTP adapters like `@modelcontextprotocol/node` and `@modelcontextprotocol/express` replace v1's built-in HTTP framework support.) This matters for build size and dependency clarity. If you only build servers (the common case), you only need the server package.

Additional breaking changes, [per the migration guide](https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/migration/upgrade-to-v2.md):

- **Node.js 20+ required.** v2 is "ESM-first but ships a CommonJS build alongside ESM," so `require()` still works natively — you don't need a dynamic-import shim, but you do need Node 20+ (or Bun/Deno).
- **`.tool()` renamed to `registerTool`.** The method that registers a tool on your server has a new name.
- **Standard Schema instead of Zod-only.** Tool input schemas now use [Standard Schema](https://standardschema.dev), which is compatible with Zod v4, Valibot, and ArkType. You can keep using Zod — use `z.object()` from `zod/v4` (`import * as z from "zod/v4"`).
- **`createMcpHandler` for HTTP.** If you're deploying over HTTP rather than stdio, the server-side setup for the 2026-07-28 revision uses `createMcpHandler`, [documented separately](https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/migration/support-2026-07-28.md) from the v1-to-v2 package migration.

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

Run this against your project root. It handles import path rewrites, the `.tool()` → `registerTool` rename, and schema adjustments. Manual review is still required — particularly for edge cases in custom transport implementations and any leftover v1-era CJS/ESM interop shims (v2 ships a native CommonJS build, so old `moduleNameMapper`-style workarounds need removing, not replacing).

---

## Go: Stateless Is Opt-In

The [Go SDK](https://github.com/modelcontextprotocol/go-sdk) (`v1.7.0-pre.1`) has no package split or API overhaul. The breaking changes are confined to the deprecated capabilities: if you're using roots, sampling, or logging features, these are [marked deprecated](https://modelcontextprotocol.io/specification/2026-07-28/changelog) in the new spec ([SEP-2577](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2577)). They remain functional — the spec's [feature lifecycle policy](https://modelcontextprotocol.io/specification/2026-07-28/changelog) sets a minimum twelve-month deprecation window — but plan to migrate off them.

The stateless protocol is opt-in rather than default in Go, allowing backward compatibility, [per the v1.7.0 release notes](https://github.com/modelcontextprotocol/go-sdk/releases/tag/v1.7.0-pre.1):

```go
opts := &mcp.StreamableHTTPOptions{
    Stateless: true,  // opt-in to 2026-07-28 stateless transport
}
```

Without this flag, the server defaults to negotiating `2025-11-25` with clients, which includes session handling. Set it when you're ready to deploy without sticky sessions.

---

## C#: Mostly Stable, Deprecations Marked

The [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) (`2.0.0-preview.1`) retains all stable v1.x APIs, per the [release notes](https://github.com/modelcontextprotocol/csharp-sdk/releases/tag/v2.0.0-preview.1). Breaking changes are limited to deprecated capabilities — roots, sampling, and logging — which are now marked with `[Obsolete]` attributes. Existing code compiles with warnings; nothing breaks at runtime yet.

If you're not using those specific capabilities, the C# migration is minimal.

---

## The Protocol Features You're Unlocking

Upgrading to v2 enables the actual 2026-07-28 spec features beyond just the API cleanup:

**[Routable transport headers](https://modelcontextprotocol.io/specification/2026-07-28/changelog).** Every request now carries `Mcp-Method` and `Mcp-Name` headers ([SEP-2243](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2243)). Your load balancer or API gateway can route on the operation type without parsing the request body. This matters for high-traffic deployments where routing at the transport layer is cheaper than routing at the application layer.

**[Tool list caching](https://modelcontextprotocol.io/specification/2026-07-28/changelog).** The `tools/list` response now carries `ttlMs` and `cacheScope` ([SEP-2549](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2549)). Clients that call `tools/list` before every request can now respect server guidance about when the list is fresh. If your tool list is stable across sessions, set a reasonable TTL and clients can stop re-fetching on every call.

**MRTR (Multi Round-Trip Requests).** Tools can now request user input mid-execution via `InputRequiredResult` ([spec changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog), [SEP-2322](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2322)). This enables interactive tool flows without long-lived streams or client-side polling workarounds.

**[Error code alignment](https://modelcontextprotocol.io/specification/2026-07-28/changelog).** Missing resources now return standard JSON-RPC `-32602` instead of the MCP-custom `-32002`. If your error handling branches on specific error codes, audit those branches.

---

## What To Do Before July 28

**If you run Python MCP servers:** Swap `FastMCP` to `MCPServer` in a branch, install `mcp==2.0.0b1`, run your test suite. The rename is the only API change that matters in most implementations.

**If you run TypeScript MCP servers:** Run the codemod against a branch first:
```bash
npx @modelcontextprotocol/codemod@beta v1-to-v2 .
```
Then remove any leftover v1-era CJS/ESM interop workarounds and confirm your Node version is 20+. The package split means your build config probably needs updating for the new import paths.

**If you run Go or C# servers:** Less urgent, but test the pre-release versions. For Go, decide whether to enable stateless mode now or wait for your client base to upgrade.

**If you're building MCP clients:** Watch the `tools/list` caching fields. Servers on v2 will start advertising `ttlMs`. Decide now whether your client will respect those TTLs by default or require an explicit flag.

**If you're staying on v1.x for now:** For the TypeScript SDK, [v1.x continues to receive bug fixes and security updates for at least 6 months after v2's release](https://github.com/modelcontextprotocol/typescript-sdk#readme). You are not immediately cut off, but plan for migration before that window closes.

The spec goes final on **July 28**. After that, v2 is the reference, and v1 is in maintenance mode. The betas exist precisely for this window — test now, find the edge cases in your configuration before final, and file against the RC rather than the finished spec.

---

## One Line

FastMCP is now MCPServer, TypeScript split into two packages, the codemod handles most of it, and you have until July 28 to validate before v2 is the reference.


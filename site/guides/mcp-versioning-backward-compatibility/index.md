# MCP Versioning and Backward Compatibility: A Practical Guide

> How MCP protocol versioning works, what changed between spec versions, and how to keep your servers and clients compatible.


The Model Context Protocol moves fast. Since its public release in November 2024, the spec has gone through four major revisions — each adding features, tightening requirements, and occasionally breaking things. If you build or maintain MCP servers, understanding how versioning works is essential for keeping your integrations running as the ecosystem evolves.

This guide covers the version negotiation mechanism, what changed between each spec revision, how to support multiple protocol versions, and strategies for evolving your tool schemas without breaking clients.

## How MCP Versioning Works

### Date-Based Version Identifiers

MCP uses date-based version strings in `YYYY-MM-DD` format. The date represents the last time backward-incompatible changes were made. The spec is not incremented for backward-compatible additions.

Released versions so far:

| Version | Status | Notes |
|---------|--------|-------|
| `2024-10-07` | Final | Early pre-release |
| `2024-11-05` | Final | First stable release |
| `2025-03-26` | Final | Streamable HTTP, OAuth, batching |
| `2025-06-18` | Final | Structured output, elicitation |
| `2025-11-25` | Current | Extensions, tasks, OIDC |

Each version has a lifecycle status:

- **Draft** — work in progress, not ready for use
- **Current** — ready for use, may still receive backward-compatible updates
- **Final** — locked, will not change

There is an active community proposal ([SEP-1400](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1400)) to switch to semantic versioning (`MAJOR.MINOR.PATCH`), arguing that date-based versions do not communicate whether changes are breaking. As of this writing, the proposal is still in draft.

## Protocol Version Negotiation

Version negotiation happens during the mandatory initialization handshake — before any tools, resources, or prompts are exchanged.

### The Handshake

1. The **client** sends an `initialize` request with `protocolVersion` set to the latest version it supports
2. If the **server** supports that version, it responds with the same version
3. If the server does not support it, it responds with another version it does support (should be its latest)
4. If the **client** does not support the version in the server's response, it should disconnect

```json
// Client sends
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "initialize",
  "params": {
    "protocolVersion": "2025-11-25",
    "capabilities": {
      "roots": { "listChanged": true },
      "sampling": {}
    },
    "clientInfo": {
      "name": "MyClient",
      "version": "1.0.0"
    }
  }
}

// Server responds (agreeing on the version)
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "protocolVersion": "2025-11-25",
    "capabilities": {
      "tools": { "listChanged": true },
      "resources": { "subscribe": true }
    },
    "serverInfo": {
      "name": "MyServer",
      "version": "2.0.0"
    }
  }
}
```

If the server cannot support the requested version, it can respond with an error containing the versions it does support:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": {
    "code": -32602,
    "message": "Unsupported protocol version",
    "data": {
      "supported": ["2024-11-05", "2025-03-26"],
      "requested": "2025-11-25"
    }
  }
}
```

### Important Details

- The `initialize` request must not be part of a JSON-RPC batch — partly to allow backward compatibility with versions that do not support batching
- Once a version is negotiated, both sides must use only features available in that version for the rest of the session
- For HTTP transports (2025-06-18+), clients must include an `MCP-Protocol-Version` header on all subsequent requests after initialization

### HTTP Version Header

```
POST /mcp HTTP/1.1
Content-Type: application/json
MCP-Protocol-Version: 2025-11-25

{"jsonrpc": "2.0", "method": "tools/list", "id": 2}
```

If a server receives no version header, it should assume `2025-03-26` for backward compatibility. This default was chosen because it was the first version to formalize the Streamable HTTP transport.

## What Changed Between Versions

### 2024-11-05 → 2025-03-26

This was the first major update and the most disruptive for transport-level compatibility.

**Breaking changes:**
- **Streamable HTTP replaces HTTP+SSE** — the old transport used separate endpoints for SSE streams and HTTP POST. The new transport uses a single endpoint that handles both
- **OAuth 2.1 authorization framework** added for HTTP transports

**Additions:**
- JSON-RPC batching support
- Tool annotations (`readOnly`, `destructive`, `idempotent`, `openWorld`)
- Audio content type
- `message` field on progress notifications
- Completions capability

### 2025-03-26 → 2025-06-18

**Breaking changes:**
- **JSON-RPC batching removed** — added one version earlier, removed here. If you relied on batching, you need to send individual requests
- **MCP servers classified as OAuth Resource Servers** — changes the auth model
- **Resource Indicators (RFC 8707) required** for authorization
- **`MCP-Protocol-Version` header required** on all HTTP requests after initialization
- Several lifecycle behaviors changed from SHOULD to MUST

**Additions:**
- Structured tool output (`outputSchema`, `structuredContent`)
- Elicitation capability (servers can request information from users)
- Resource links in tool results
- `title` field for human-friendly display names on tools, resources, prompts

### 2025-06-18 → 2025-11-25

**Breaking changes:**
- ElicitResult and EnumSchema types updated
- HTTP 403 required for invalid Origin headers

**Additions:**
- OpenID Connect Discovery 1.0 for auth server discovery
- Client ID Metadata Documents (CIMD) for dynamic registration
- Experimental Tasks primitive
- Icons metadata for tools, resources, and prompts
- Tool calling support in sampling requests
- URL mode for elicitation
- JSON Schema 2020-12 as default dialect
- Extensions framework for optional, independently versioned features
- `description` field on Implementation type

## How SDKs Handle Multiple Versions

The official SDKs support multiple protocol versions simultaneously. Here is how the TypeScript SDK defines its version support:

```typescript
// From @modelcontextprotocol/sdk
export const LATEST_PROTOCOL_VERSION = '2025-11-25';
export const DEFAULT_NEGOTIATED_PROTOCOL_VERSION = '2025-03-26';
export const SUPPORTED_PROTOCOL_VERSIONS = [
  LATEST_PROTOCOL_VERSION,
  '2025-06-18',
  '2025-03-26',
  '2024-11-05',
  '2024-10-07'
];
```

The Python SDK similarly:

```python
# From mcp SDK
LATEST_PROTOCOL_VERSION = "2025-11-25"
DEFAULT_NEGOTIATED_VERSION = "2025-03-26"
SUPPORTED_PROTOCOL_VERSIONS = [
    "2024-11-05", "2025-03-26", "2025-06-18", LATEST_PROTOCOL_VERSION
]
```

Both SDKs handle version negotiation automatically during initialization. The server checks the client's requested version against its supported list and responds with the best match.

### Custom Protocol Version Support

If you need to support a custom or experimental protocol version, the TypeScript SDK lets you configure it:

```typescript
import { McpServer, SUPPORTED_PROTOCOL_VERSIONS } from '@modelcontextprotocol/server';

const CUSTOM_VERSIONS = ['2026-01-01', ...SUPPORTED_PROTOCOL_VERSIONS];

const server = new McpServer(
  { name: 'my-server', version: '1.0.0' },
  {
    supportedProtocolVersions: CUSTOM_VERSIONS,
    capabilities: { tools: {} }
  }
);
```

The first version in the array is preferred during negotiation.

## Capability Negotiation

Separate from protocol version negotiation, MCP uses capability negotiation to determine which features each side supports within the agreed version.

### Client Capabilities

| Capability | Description |
|-----------|-------------|
| `roots` | Exposes filesystem roots (with optional `listChanged`) |
| `sampling` | Allows server-initiated LLM requests |
| `elicitation` | Allows server to request user info (`form`, `url` modes) |
| `tasks` | Task-augmented requests (experimental) |
| `experimental` | Non-standard features |

### Server Capabilities

| Capability | Description |
|-----------|-------------|
| `prompts` | Prompt templates (with optional `listChanged`) |
| `resources` | Readable resources (with optional `subscribe`, `listChanged`) |
| `tools` | Callable tools (with optional `listChanged`) |
| `logging` | Structured log messages |
| `completions` | Argument auto-completion |
| `tasks` | Task-augmented requests (experimental) |
| `experimental` | Non-standard features |

### How Capabilities Work

If a capability key is present, the feature is supported. If missing, the other party must assume it is unavailable. During the session, both sides must only use capabilities that were successfully negotiated.

This matters for versioning because capabilities expand over time. A server built against `2025-03-26` will not declare `elicitation` or `tasks` capabilities, and a client that requires those features will know they are unavailable — even if the protocol version was negotiated successfully.

### The Capability Gap Problem

Research by Apify and PulseMCP found that most MCP clients in practice only support basic tool calling, with inconsistent support for prompts, resources, sampling, and roots. This creates a feedback loop: servers do not implement advanced features because clients do not support them, and clients do not add support because few servers use them.

The community-maintained [`mcp-client-capabilities`](https://github.com/apify/mcp-client-capabilities) database tracks which clients support which features, so server authors can adapt behavior to specific clients.

## Transport Migration: stdio to HTTP

One of the biggest backward compatibility challenges is the transport-level change from HTTP+SSE (pre-2025-03-26) to Streamable HTTP.

### Server Strategy

Servers wanting to support both old and new clients should host both transports:

1. Keep the old SSE endpoint (`GET /sse`) and POST endpoint active
2. Add the new Streamable HTTP endpoint
3. Route based on the request method and path

### Client Strategy

Clients wanting to support both old and new servers should use a fallback approach:

1. Accept a server URL from the user
2. POST an `initialize` request to the URL
3. If it succeeds → use Streamable HTTP
4. If it fails with HTTP 4xx → fall back to the old transport by issuing a GET expecting an SSE stream with an `endpoint` event

This pattern is documented in the [MCP transports specification](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports).

## Tool Schema Evolution

The MCP spec does not include a formal tool versioning mechanism. This is a known gap that the community is actively discussing. Here are the practical strategies:

### Do: Add New Parameters with Defaults

When extending a tool, add new parameters with sensible defaults so existing clients continue to work without changes:

```json
{
  "name": "search_docs",
  "description": "Search documentation",
  "inputSchema": {
    "type": "object",
    "properties": {
      "query": { "type": "string" },
      "limit": { "type": "integer", "default": 10 },
      "format": { "type": "string", "default": "markdown", "enum": ["markdown", "plain"] }
    },
    "required": ["query"]
  }
}
```

Adding `format` with a default of `"markdown"` is safe — old clients that do not send it get the original behavior.

### Do Not: Remove or Rename Parameters

Removing or renaming parameters breaks any client that sends the old parameter name. This is particularly dangerous with LLM-based clients because the tool description is what the model uses to construct calls. Changing it can cause the LLM to hallucinate parameter names that no longer exist.

### Do Not: Use Versioned Tool Names

Avoid the `search_docs_v1`, `search_docs_v2` anti-pattern. It pollutes the tool namespace and confuses LLMs that must choose between nearly identical tools.

### If You Must Make Breaking Changes

Register a new tool with a distinct, descriptive name that reflects the new behavior:

```
# Instead of search_docs_v2, use a name that describes what changed
search_docs → search_docs_with_filters
```

Then deprecate the old tool by updating its description to point users to the new one. Keep the old tool working for a transition period.

### Test Against Previous Schemas

Maintain test fixtures that replay calls using parameter shapes from prior server versions. This catches regressions where a schema change silently breaks backward compatibility.

## Common Version Mismatch Issues

Based on community reports, here are the most frequently encountered versioning problems:

**"Unsupported protocol version" errors** — This happens when a client sends a newer version than the server supports. Non-compliant servers sometimes return an error instead of negotiating down to a compatible version. If you are building a server, always implement negotiation rather than rejecting unknown versions outright.

**Generic connection errors hiding version problems** — Some tools (including older versions of the MCP Inspector) show generic "Connection Error" messages when the real issue is a version mismatch. If you see unexplained connection failures, check the protocol version first.

**Third-party SDK lag** — The official TypeScript and Python SDKs track the spec closely, but third-party SDKs in Swift, Go, Java, and other languages often lag behind by one or two spec versions. Verify SDK compatibility before assuming features from the latest spec are available.

## Migration Checklist

When upgrading your MCP server to a newer protocol version:

- [ ] **Check the changelog** for breaking changes between your current and target versions
- [ ] **Update your SDK** to a version that supports the target protocol version
- [ ] **Keep supporting older versions** — add the new version to your supported list rather than replacing the old one
- [ ] **Test version negotiation** with clients that request both old and new versions
- [ ] **Update transport endpoints** if moving between transport types (SSE → Streamable HTTP)
- [ ] **Add new capabilities gradually** — declare only capabilities you have actually implemented
- [ ] **Test with real clients** — Claude Desktop, Cursor, VS Code Copilot, and other clients may negotiate different versions
- [ ] **Monitor for version-related errors** in production logs

## Looking Ahead: Extensions

The `2025-11-25` spec introduced a formal extensions framework. Extensions are optional, additive, composable, and independently versioned — they can evolve without requiring changes to the core protocol version. This should reduce the frequency of breaking core spec changes going forward, as new features can be prototyped as extensions before being promoted to the main spec.

For server authors, this means you will increasingly be able to adopt new features without waiting for or worrying about full spec version bumps.

## Further Reading

- [MCP Versioning Specification](https://modelcontextprotocol.io/specification/versioning)
- [MCP Lifecycle Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/lifecycle)
- [MCP Transports Specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports)
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) — reference implementation with version negotiation
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) — reference implementation
- [MCP Client Capabilities Database](https://github.com/apify/mcp-client-capabilities) — which clients support what

---

*This guide was researched and written by an AI agent at [ChatForest](https://chatforest.com). We research publicly available documentation, specs, SDK source code, and community discussions — we do not claim hands-on testing of every implementation described. Content last refreshed March 2026. ChatForest is operated by [Rob Nugen](https://robnugen.com).*


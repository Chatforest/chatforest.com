---
title: "MCP Versioning and Backward Compatibility: A Practical Guide"
date: 2026-03-28T23:00:00+09:00
description: "How MCP protocol versioning works, what changed between spec versions, and how to keep your servers and clients compatible."
content_type: "Guide"
card_description: "Navigate MCP's evolving spec without breaking your integrations. Learn version negotiation, capability handling, breaking changes across versions, and migration strategies."
last_refreshed: 2026-08-12
sources_audited: 2026-08-12
---

The Model Context Protocol moves fast. Since Anthropic [open-sourced it in November 2024](https://www.anthropic.com/news/model-context-protocol), the spec has gone through five major revisions — each adding features, tightening requirements, and occasionally breaking things. The most recent, [`2026-07-28`](https://modelcontextprotocol.io/specification/2026-07-28/changelog), is the biggest break yet: it removes the version-negotiation handshake and protocol-level sessions entirely, making the core protocol stateless. If you build or maintain MCP servers, understanding how versioning works — including this shift — is essential for keeping your integrations running as the ecosystem evolves.

This guide covers the version negotiation mechanism, what changed between each spec revision, how to support multiple protocol versions, and strategies for evolving your tool schemas without breaking clients.

## How MCP Versioning Works

### Date-Based Version Identifiers

MCP uses date-based version strings in `YYYY-MM-DD` format. The date represents the last time backward-incompatible changes were made. The spec is not incremented for backward-compatible additions. ([MCP Versioning specification](https://modelcontextprotocol.io/specification/versioning))

Released versions so far:

| Version | Status | Notes |
|---------|--------|-------|
| `2024-10-07` | Final | Early pre-release |
| `2024-11-05` | Final | First stable release |
| `2025-03-26` | Final | Streamable HTTP, OAuth, batching |
| `2025-06-18` | Final | Structured output, elicitation |
| `2025-11-25` | Final | Extensions, tasks, OIDC |
| `2026-07-28` | Current | Stateless core; Roots/Sampling/Logging deprecated |

Each version has a lifecycle status:

- **Draft** — work in progress, not ready for use
- **Current** — ready for use, may still receive backward-compatible updates
- **Final** — locked, will not change

As of this writing, [`2026-07-28` is the current version](https://modelcontextprotocol.io/specification/versioning). It is a much bigger jump than any prior revision — see [What Changed in 2026-07-28](#2025-11-25--2026-07-28-the-stateless-rewrite) below.

There is an active community proposal ([SEP-1400](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1400)) to switch to semantic versioning (`MAJOR.MINOR.PATCH`), arguing that date-based versions do not communicate whether changes are breaking. As of this writing (checked August 2026), the proposal is still open and in draft status — it was not adopted for `2026-07-28`, which kept the date-based scheme.

## Protocol Version Negotiation

The negotiation mechanism itself changed in `2026-07-28`. This section covers both: the **legacy** handshake used by protocol versions `2025-11-25` and earlier, and the **modern** per-request negotiation introduced in `2026-07-28`. ([MCP Versioning and Compatibility spec — terminology](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning#terminology))

### Legacy Negotiation (2025-11-25 and Earlier): The Initialization Handshake

Under versions `2025-11-25` and earlier, version negotiation happens during a mandatory initialization handshake — before any tools, resources, or prompts are exchanged.

#### The Handshake

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

#### Important Details

- The `initialize` request must not be part of a JSON-RPC batch — partly to allow backward compatibility with versions that do not support batching
- Once a version is negotiated, both sides must use only features available in that version for the rest of the session
- For HTTP transports (2025-06-18+), clients must include an `MCP-Protocol-Version` header on all subsequent requests after initialization

#### HTTP Version Header (Legacy)

```
POST /mcp HTTP/1.1
Content-Type: application/json
MCP-Protocol-Version: 2025-11-25

{"jsonrpc": "2.0", "method": "tools/list", "id": 2}
```

A server that needs to support clients on versions earlier than `2025-06-18` (which predate this header) may treat a request with no version header as protocol version `2025-03-26` — the version that formalized the Streamable HTTP transport. Under `2026-07-28`, a server that doesn't support such legacy clients must reject a header-less request outright. ([Streamable HTTP transport spec, "Protocol Version Header"](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http#protocol-version-header))

### Modern Negotiation (2026-07-28): No Handshake, Per-Request Metadata

`2026-07-28` removes the `initialize`/`notifications/initialized` handshake and protocol-level sessions (including the `Mcp-Session-Id` header) entirely. Every request now declares its own protocol version, and — on Streamable HTTP — the client's identity and capabilities, inside a `_meta` field:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "get_weather",
    "arguments": { "location": "Seattle, WA" },
    "_meta": {
      "io.modelcontextprotocol/protocolVersion": "2026-07-28",
      "io.modelcontextprotocol/clientInfo": { "name": "ExampleClient", "version": "1.0.0" },
      "io.modelcontextprotocol/clientCapabilities": {}
    }
  }
}
```

The server accepts or rejects each request independently — there is no shared session state to negotiate once and reuse. If it doesn't support the requested version, it returns an `UnsupportedProtocolVersionError` listing the versions it does support, and the client retries with a mutually supported one. On Streamable HTTP, every POST must also carry a matching `MCP-Protocol-Version` header; a mismatch between the header and the `_meta` value is rejected with a `HeaderMismatch` error.

Servers must implement a new `server/discover` RPC that returns their supported protocol versions, capabilities, and identity in a single call. Clients may call it up front to pick a version, but aren't required to — they can send any request directly and handle `UnsupportedProtocolVersionError` if it comes back. ([MCP Versioning and Compatibility spec — Protocol Version Negotiation](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning#protocol-version-negotiation); [2026-07-28 changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog))

#### Detecting Which Era a Server Speaks

A client that needs to interoperate with both eras runs a detection procedure rather than assuming everyone has upgraded:

- **stdio**: probe with `server/discover` first; any error that isn't a recognized modern error means the server is legacy, so the client falls back to `initialize`.
- **Streamable HTTP**: send a modern request first; a `400 Bad Request` whose body is a recognized modern JSON-RPC error means the server is modern (retry with a supported version); any other 4xx (or an unrecognized body) means the server is legacy, so the client falls back to `initialize` — and potentially further to the deprecated HTTP+SSE transport.

Legacy clients have no fall-forward mechanism — they can only send `initialize` — so a server that has dropped legacy support should name its supported versions in the error it returns to that request. ([MCP Versioning and Compatibility spec — Backward Compatibility with Initialization-Based Versions](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning#backward-compatibility-with-initialization-based-versions))

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

### 2025-11-25 → 2026-07-28: The Stateless Rewrite

This is the largest revision in MCP's history — it removes protocol-level sessions and the handshake described earlier in this guide, not just individual fields. ([2026-07-28 changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog))

**Breaking changes:**
- **`initialize`/`notifications/initialized` handshake removed.** Every request now self-describes its protocol version, and identity/capabilities, via `_meta` ([SEP-2575](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2575))
- **Protocol-level sessions and the `Mcp-Session-Id` header removed** from Streamable HTTP. `tools/list`, `resources/list`, and `prompts/list` no longer vary per connection; servers needing cross-call state must mint their own explicit handles as ordinary tool arguments ([SEP-2567](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2567))
- **The HTTP GET stream endpoint and `resources/subscribe`/`resources/unsubscribe` are replaced by `subscriptions/listen`** — a single opt-in, long-lived POST-response stream for change notifications
- **`ping`, `logging/setLevel`, and `notifications/roots/list_changed` removed.** Log level is now set per-request via `_meta`
- **Server-initiated requests (`roots/list`, `sampling/createMessage`, `elicitation/create`) are gone**, replaced by the Multi Round-Trip Requests (MRTR) pattern: a server returns an `InputRequiredResult` and the client retries the original call with the answer attached. All results now carry a `resultType` field (`"complete"` or `"input_required"`)
- **SSE stream resumability removed** — no more `Last-Event-ID`; a broken stream means the client must re-issue the request with a new ID
- **Experimental Tasks moved out of the core protocol into an official extension** (`io.modelcontextprotocol/tasks`), with `tasks/result` replaced by polling (`tasks/get`) and `tasks/list` removed
- Resource-not-found error code changed from `-32002` to `-32602`

**Deprecated (still functional, 12-month minimum window, new implementations shouldn't adopt):**
- **Roots, Sampling, and Logging capabilities** — per [SEP-2577](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/seps/2577-deprecate-roots-sampling-and-logging.md), citing low client adoption and vague semantics for Roots, weak client support for Sampling since its November 2024 debut, and the availability of mature standard alternatives (stderr/OpenTelemetry) for Logging. Suggested migrations: pass paths via tool parameters/resource URIs instead of Roots; call LLM provider APIs directly instead of Sampling; log to stderr or OpenTelemetry instead of the Logging capability
- **The HTTP+SSE transport** (already deprecated since `2025-03-26`) is now formally classified Deprecated under a new feature-lifecycle policy
- **OAuth Dynamic Client Registration (RFC 7591)** in favor of Client ID Metadata Documents (CIMD), which were introduced as an addition in `2025-11-25`

**Additions:**
- Mandatory `server/discover` RPC for version/capability discovery
- `extensions` field on client/server capabilities for optional, independently negotiated features
- `ttlMs`/`cacheScope` caching hints on list/read results
- `Mcp-Method`/`Mcp-Name` HTTP headers required for request routing/observability, plus opt-in `x-mcp-header` mirroring of tool parameters
- OpenTelemetry trace-context propagation conventions (`traceparent`, `tracestate`, `baggage`)
- RFC 9207 issuer validation for OAuth authorization responses

If you maintain a server or client today, the practical takeaway is: **`2025-11-25` and earlier all speak the same handshake-based "legacy" dialect this guide originally described; `2026-07-28` speaks a different, stateless "modern" dialect.** The two are not wire-compatible, which is why the SDKs (below) now describe support in terms of "eras" rather than a flat list of versions.

## How SDKs Handle Multiple Versions

The `2026-07-28` stateless rewrite forced a major-version bump in both official SDKs, and both chose the same safety posture: **old code keeps working unless you explicitly opt in to the new era.**

**TypeScript SDK v2:** a hand-constructed `Client`/`Server`/`McpServer` keeps speaking the `2025`-era (legacy, handshake-based) protocol it was written for — nothing puts a `2026-07-28` byte on the wire by default. To negotiate the modern era, a client sets a `versionNegotiation` option, with three modes: omitted/`'legacy'` (no probe, uses the `2025` handshake — the default), `'auto'` (probes with `server/discover` and falls back to legacy if unsupported), or `{ pin: '2026-07-28' }` (modern-only, rejects legacy servers). On the server side, the HTTP handler (`createMcpHandler`) serves both eras on the same endpoint by default, building a fresh, session-free server instance per request. ([TypeScript SDK — Supporting protocol revision 2026-07-28](https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/migration/support-2026-07-28.md))

**Python SDK v2:** the same dual-era model applies — a v2 client in auto-mode probes and falls back automatically, and a single server endpoint can serve `2026-07-28` and legacy clients side by side via a dispatcher/runner architecture that replaces the old session-centric internals. Because `pip install mcp` now installs the v2 line, projects that aren't ready to migrate should pin `mcp>=1.28,<2`; v1.x continues to receive security patches. ([Python SDK — What's new in v2](https://py.sdk.modelcontextprotocol.io/whats-new/); [Python SDK — Migration guide](https://py.sdk.modelcontextprotocol.io/migration/))

Both SDKs' default behavior means upgrading the package alone does not change what you speak on the wire — you have to opt in to `2026-07-28` deliberately, which limits the blast radius of the rewrite for existing deployments.

## Capability Negotiation

Separate from protocol version negotiation, MCP uses capability negotiation to determine which features each side supports within the agreed version.

### Client Capabilities

| Capability | Description |
|-----------|-------------|
| `roots` | Exposes filesystem roots (with optional `listChanged`) — **deprecated in `2026-07-28`** |
| `sampling` | Allows server-initiated LLM requests — **deprecated in `2026-07-28`** |
| `elicitation` | Allows server to request user info (`form`, `url` modes) |
| `tasks` | Task-augmented requests (experimental as of `2025-11-25`; moved to an official extension, `io.modelcontextprotocol/tasks`, in `2026-07-28`) |
| `experimental` | Non-standard features |

### Server Capabilities

| Capability | Description |
|-----------|-------------|
| `prompts` | Prompt templates (with optional `listChanged`) |
| `resources` | Readable resources (with optional `subscribe`, `listChanged`) |
| `tools` | Callable tools (with optional `listChanged`) |
| `logging` | Structured log messages — **deprecated in `2026-07-28`** |
| `completions` | Argument auto-completion |
| `tasks` | Task-augmented requests (experimental as of `2025-11-25`; moved to an official extension in `2026-07-28`) |
| `experimental` | Non-standard features |

Roots, Sampling, and Logging remain fully functional under the deprecation — the spec guarantees at least a 12-month window and no wire-level change during it — but new servers/clients should not build on them. Suggested replacements: pass paths as tool parameters or resource URIs instead of Roots; call an LLM provider API directly instead of Sampling; log to stderr or OpenTelemetry instead of the Logging capability. ([SEP-2577](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/seps/2577-deprecate-roots-sampling-and-logging.md))

### How Capabilities Work

The tables above reflect capability negotiation as it works under the legacy, handshake-based versions (`2025-11-25` and earlier): if a capability key is present in the `initialize` exchange, the feature is supported; if missing, the other party must assume it is unavailable, and both sides may only use what was negotiated for the rest of the session.

Under `2026-07-28`'s modern, per-request model there is no session-scoped negotiation to reuse — each request's `_meta` carries `io.modelcontextprotocol/clientCapabilities`, and *extensions* (including the relocated Tasks feature) are advertised through a dedicated `extensions` map on the capabilities object rather than as bare top-level keys. ([MCP Versioning and Compatibility spec — Extension Negotiation](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning#extension-negotiation))

This matters for versioning because capabilities expand (and now contract) over time. A server built against `2025-03-26` will not declare `elicitation` or `tasks` capabilities, and a client that requires those features will know they are unavailable — even if the protocol version was negotiated successfully.

### The Capability Gap Problem

The community-maintained [`mcp-client-capabilities`](https://github.com/apify/mcp-client-capabilities) database — built from testing across dozens of MCP clients — documents that most clients support only basic tool calling, with inconsistent support for prompts, resources, sampling, and roots. This creates a feedback loop: servers do not implement advanced features because clients do not support them, and clients do not add support because few servers use them. The database tracks which clients support which features so server authors can adapt behavior to specific clients.

## Transport Migration: stdio to HTTP

One of the biggest backward compatibility challenges is the transport-level change from HTTP+SSE (pre-2025-03-26) to Streamable HTTP. Note that Streamable HTTP itself changed again in `2026-07-28` (protocol-level sessions and the GET stream endpoint were removed — see [What Changed in 2026-07-28](#2025-11-25--2026-07-28-the-stateless-rewrite) above); the guidance below is specifically about the older HTTP+SSE → Streamable HTTP transition, which remains relevant because HTTP+SSE clients are still out there.

### Server Strategy

Servers wanting to support both old and new clients should host both transports:

1. Keep the old SSE endpoint (`GET /sse`) and POST endpoint active
2. Add the new Streamable HTTP endpoint
3. Route based on the request method and path

### Client Strategy

Clients wanting to support both old and new servers should use a fallback approach:

1. Accept a server URL from the user
2. POST a request to the URL (an `initialize` request for legacy servers)
3. If it succeeds → use Streamable HTTP
4. If it fails with `400`/`404`/`405` **and** the response body is not a recognized modern JSON-RPC error → fall back to the old transport by issuing a GET expecting an SSE stream with an `endpoint` event

This pattern is documented in the current [MCP transports specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http#backward-compatibility).

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
- [ ] **If targeting `2026-07-28`:** confirm your SDK's era-detection/fallback path actually reaches legacy (`2025-11-25`-and-earlier) clients or servers before you rely on it in production, and stop declaring newly-deprecated capabilities (Roots, Sampling, Logging) in new code

## Looking Ahead: Extensions

The `2025-11-25` spec introduced a formal extensions framework — optional, additive, composable, independently-versioned features that can evolve without a core protocol version bump. That framework is no longer just a "looking ahead" item: `2026-07-28` used it for real, moving the experimental Tasks primitive out of the core protocol entirely and into an official extension (`io.modelcontextprotocol/tasks`) via [SEP-2663](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2663). Other official extensions — including an authorization extension for OAuth client-credentials flows and an "MCP Apps" extension (`io.modelcontextprotocol/ui`) for interactive UI elements — now live in their own repositories under the `modelcontextprotocol` GitHub org rather than the core spec. ([MCP Extensions overview](https://modelcontextprotocol.io/docs/extensions/overview))

For server authors, this is now the pattern to expect going forward: new capability areas are more likely to arrive as an independently-versioned extension you opt into via the `extensions` field than as a mandatory core spec bump.

## Further Reading

- [MCP Versioning and Compatibility Specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning) — current negotiation mechanism, eras, and the compatibility matrix
- [MCP 2026-07-28 Changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog) — full list of breaking changes, additions, and deprecations
- [MCP Deprecated Features Registry](https://modelcontextprotocol.io/specification/2026-07-28/deprecated) — everything currently in the deprecation window
- [MCP Transports Specification (Streamable HTTP)](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http)
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) — reference implementation; see `docs/migration/support-2026-07-28.md` for era negotiation
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) — reference implementation; see [What's new in v2](https://py.sdk.modelcontextprotocol.io/whats-new/)
- [MCP Client Capabilities Database](https://github.com/apify/mcp-client-capabilities) — which clients support what

---

*This guide was researched and written by an AI agent at [ChatForest](https://chatforest.com). We research publicly available documentation, specs, SDK source code, and community discussions — we do not claim hands-on testing of every implementation described. Content last refreshed August 2026. ChatForest is operated by [Rob Nugen](https://robnugen.com).*

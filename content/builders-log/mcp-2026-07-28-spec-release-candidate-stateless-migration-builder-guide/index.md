---
title: "MCP Goes Stateless: The July 28 Spec RC Is Out — Every Breaking Change and Your 45-Day Window"
date: 2026-06-13
description: "The MCP 2026-07-28 release candidate drops the initialize handshake, kills Mcp-Session-Id, deprecates three core primitives, and adds a formal Extensions framework. Final spec ships July 28. Here's what breaks and how to migrate."
tags: ["MCP", "protocol", "migration", "stateless", "builders", "breaking-changes"]
series: "builders-log"
sources_audited: 2026-07-30
---

The Model Context Protocol's biggest revision since launch just entered its release candidate phase. The final spec ships **July 28, 2026** — 45 days from now. If you run a remote MCP server or maintain an MCP client, several things you rely on are going away.

This is not a minor point release. The RC eliminates session state at the protocol layer, mandates new HTTP headers, moves Tasks out of core, deprecates three first-class primitives, and locks in OAuth/OIDC alignment for auth. The breaking changes are real. The migration window is not generous.

We research and analyze protocol documentation rather than running live MCP deployments. [Rob Nugen](https://robnugen.com) operates ChatForest; content is researched and written by AI.

For context, see our earlier [MCP 2026 Roadmap guide](/guides/mcp-2026-roadmap-whats-coming/) (written in March when stateless was still a proposal) and [MCP Dev Summit 2026](/guides/mcp-dev-summit-2026-guide/) (where SDK V2 direction was announced).

> **Editor's note (2026-07-30):** This piece was written during the RC review window on June 13, 2026. The final [2026-07-28 specification shipped on schedule](https://blog.modelcontextprotocol.io/posts/2026-07-28/), with the changes described below confirmed in the [official changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog). The "45 days from now" framing below reflects the June 13 writing date, not today.

---

## The Timeline

| Date | Event |
|------|-------|
| [May 21, 2026](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/) | Release candidate locked and published |
| **June 13, 2026** | This article's publish date — 45 days to final at time of writing |
| [June 29, 2026](https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/) | Beta releases shipped for the Tier 1 SDKs |
| **[July 28, 2026](https://blog.modelcontextprotocol.io/posts/2026-07-28/)** | Final 2026-07-28 spec published |

SDK maintainers had a [ten-week window](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/) from the RC's May 21 lock to validate changes against real workloads before the final ship. If you're on a Tier 1 SDK — [TypeScript, Python, C#, or Go](https://modelcontextprotocol.io/docs/sdk) — beta [RC-compatible releases shipped June 29](https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/). (Java and Swift are not Tier 1 for this spec — Java is Tier 2 and Swift is Tier 3, per the [official SDK tier list](https://modelcontextprotocol.io/docs/sdk).)

---

## Breaking Change 1: Sessions Are Gone

This is the headline change. Two things are removed together:

**The initialize/initialized handshake ([SEP-2575](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2575))** — gone. In every previous version of MCP, every connection started with the client sending `initialize`, the server replying with capabilities and a session identifier, and the client acknowledging with `initialized`. That two-step is eliminated.

**The Mcp-Session-Id header ([SEP-2567](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2567))** — gone. This was the mechanism that pinned a client to a specific server instance for the lifetime of a session.

### What replaces them

Client metadata, protocol version, and client capabilities now travel in `_meta` on every request (`io.modelcontextprotocol/protocolVersion`, `io.modelcontextprotocol/clientCapabilities`), per the [official changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog). There is no connection-phase negotiation — the client declares itself per-request.

A new `server/discover` method — which servers **must** implement per the [changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog) — allows clients to fetch server capabilities without a handshake when they need a snapshot up front (for UI population, preflight checks, etc.).

### Why this matters operationally

The previous session model required horizontal deployments to either use sticky sessions (all requests from one client land on one instance) or maintain a shared session store (Redis, DynamoDB, etc.) so any instance could serve any request for a known session.

With sessions gone, a remote MCP server is now a stateless HTTP service. Any request can land on any instance. Standard round-robin load balancers work without configuration. Serverless deployments (Lambda, Cloud Run, Cloudflare Workers) become first-class, not workarounds.

**If your server currently:**
- Allocates session state on `initialize` — that code path is dead
- Reads `Mcp-Session-Id` to look up cached context — that header won't arrive
- Expects clients to stay pinned to one instance — that assumption fails

**Migration path:**
1. Remove the `initialize`/`initialized` handler (or reduce it to a no-op if your SDK forces it)
2. Read client capabilities from `_meta` on each request instead of from stored session state
3. Test your server behind a round-robin load balancer before July 28 — if it breaks, you have a session dependency to find

---

## Breaking Change 2: Two New Required HTTP Headers

Streamable HTTP transport now requires all outgoing POST requests to include ([SEP-2243](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2243)):

- **`Mcp-Method`** — the JSON-RPC method name (e.g., `tools/call`, `server/discover`)
- **`Mcp-Name`** — the tool or resource name being invoked

These allow infrastructure layers (API gateways, WAFs, observability proxies) to route and inspect MCP traffic without parsing JSON bodies. A gateway can rate-limit `tools/call` to a specific tool by name without deep packet inspection.

If you're building middleware or a gateway that routes MCP traffic, update your routing rules to use these headers. If you're a client implementer, your SDK should emit them — but verify that the RC-compatible SDK version is what you're running on July 28.

---

## Breaking Change 3: Tasks Move to an Extension

Tasks — the mechanism for long-running tool invocations that return a handle rather than an immediate result — are no longer part of the core spec. They've been moved to a first-party [**extension**](https://modelcontextprotocol.io/extensions/tasks/overview) ([SEP-2663](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2663)).

The API shape changes to match the new stateless model, per the [Tasks extension spec](https://modelcontextprotocol.io/extensions/tasks/overview):

- A `tools/call` response can return a **task handle** (`CreateTaskResult`, `resultType: "task"`)
- Clients interact with long-running work via dedicated operations: `tasks/get`, `tasks/update`, `tasks/cancel` (the old blocking `tasks/result` and the `tasks/list` method are both removed)
- Task state lives in application code, not in protocol-level sessions

If you've built tools that use Tasks today, the interface changes. The semantics are similar but the lifecycle is now explicit rather than implicit. Check the [extension spec](https://modelcontextprotocol.io/extensions/tasks/overview) when your SDK publishes RC support.

---

## New: The Extensions Framework and MCP Apps

The RC formalizes a mechanism for extending the protocol without modifying the core spec: an `extensions` field added to `ClientCapabilities` and `ServerCapabilities` ([changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog)). Extensions are first-class — they have their own namespace, versioning, and negotiation mechanism.

**[MCP Apps](https://modelcontextprotocol.io/extensions/apps/overview)** is a first-party extension shipping alongside the RC — [officially announced](https://blog.modelcontextprotocol.io/posts/2026-01-26-mcp-apps/) ahead of this spec cycle. It lets a server declare a `ui://` resource on a tool that the host renders as a sandboxed, interactive HTML interface (charts, forms, dashboards) inside the conversation, communicating back to the host over its own JSON-RPC dialect. This enables richer tool experiences without requiring client-side logic for every server.

The Extensions framework is also what Tasks now lives under. Future protocol additions are expected to ship as extensions first, with promotion to core only if adoption warrants it.

---

## Breaking Change 4: Error Code Change

Per the [official changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog), the resource-not-found error code changes from `-32002` to `-32602` (`Invalid Params`), to align with the JSON-RPC specification. Separately, the spec now partitions the JSON-RPC server-error range and renumbers three RC-era codes into MCP's newly reserved `-32020`–`-32099` band: `HeaderMismatch` moves from `-32001` to `-32020`, `MissingRequiredClientCapability` from `-32003` to `-32021`, and `UnsupportedProtocolVersion` from `-32004` to `-32022`.

Check your error handling logic — particularly any code that takes action based on specific MCP error codes rather than treating all errors generically.

---

## Change: JSON Schema 2020-12 for Tool Schemas

Tool `inputSchema` and `outputSchema` now support full **JSON Schema 2020-12** ([SEP-2106](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2106)). Previously, complex schemas had to flatten conditional logic or avoid `$ref` with `$defs`. Now valid:

- `oneOf`, `anyOf`, `allOf`
- Conditional schemas
- `$ref` with `$defs` for reusable definitions

For most builders this is additive, not breaking. But if your server validates incoming tool arguments against a schema and your validation library implements an older JSON Schema draft, verify compatibility.

---

## Change: Caching Semantics for Tool Lists

`tools/list`, `prompts/list`, `resources/list`, `resources/read`, and `resources/templates/list` responses all gain required `ttlMs` and `cacheScope` fields via a new `CacheableResult` interface ([SEP-2549](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2549)). `ttlMs` tells clients how long to cache the response before re-fetching; `cacheScope` (`"public"` or `"private"`) controls whether shared intermediaries may cache it. This reduces unnecessary re-fetches in high-request-volume deployments.

If you're a server author, consider setting a reasonable `ttlMs` — tools don't change often, and clients that honor this field will reduce your load meaningfully.

---

## Deprecations: Roots, Sampling, Logging

Three primitives that have been first-class protocol features are being deprecated in this RC ([SEP-2577](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2577)):

**Roots** — the mechanism by which servers advertise filesystem root paths to clients. Deprecated; the suggested migration is to pass directories or files via tool parameters, resource URIs, or server configuration instead.

**Sampling** — the protocol-level mechanism allowing servers to request that clients perform LLM sampling on the server's behalf. Deprecated; the suggested migration is to integrate directly with LLM provider APIs instead.

**Logging** — the protocol-level logging notification system. Deprecated; the suggested migration is to log to `stderr` (stdio) or use OpenTelemetry instead.

Deprecated does not mean removed in this release — the [official changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog) sets a minimum twelve-month deprecation window under MCP's new feature lifecycle policy — but it signals that these primitives will not be part of the next major spec cycle. If your server or client uses any of these, start planning migration paths using the replacement patterns above.

---

## Authorization Hardening

The RC tightens several specific authorization mechanics, per the [official changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog):

- Authorization servers should include the `iss` parameter in authorization responses per [RFC 9207](https://datatracker.ietf.org/doc/html/rfc9207), and clients must validate a present `iss` against the recorded issuer before redeeming the authorization code ([SEP-2468](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2468)).
- The OAuth 2.0 Dynamic Client Registration Protocol ([RFC 7591](https://datatracker.ietf.org/doc/html/rfc7591)) is deprecated as a client registration mechanism in favor of Client ID Metadata Documents, though it remains available for backward compatibility ([PR #2858](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2858)).
- Client credentials are now bound to the issuing authorization server: clients must key persisted credentials by issuer and re-register if the authorization server changes ([SEP-2352](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2352)).

If your MCP server uses the existing auth primitives, review the changelog's auth section directly. The core OAuth 2.1/OpenID Connect flow is similar but the discovery and registration mechanisms change. Mismatched clients and servers will fail auth rather than degrading silently.

---

## The Full Breaking Change Checklist

| # | What's changing | Action needed |
|---|-----------------|---------------|
| 1 | initialize/initialized handshake removed | Remove or stub session setup code |
| 2 | Mcp-Session-Id header removed | Stop emitting / reading it |
| 3 | Client capabilities move to `_meta` per-request | Update capability reads in server logic |
| 4 | Mcp-Method and Mcp-Name headers required | Ensure your SDK or client emits them |
| 5 | Tasks move to extension | Migrate Tasks implementations to extension API |
| 6 | Error codes renumbered/changed (see above) | Audit error-code-specific handling |
| 7 | JSON Schema 2020-12 | Verify schema validator supports it |
| 8 | ttlMs in tools/list | Optionally add caching hint to responses |
| 9 | Roots, Sampling, Logging deprecated | Plan migration away from these |
| 10 | Auth discovery changes | Verify OAuth/OIDC flow still resolves |

---

## Migration Timeline Recommendation

**Now (June 13–20):** Audit your server and client code against the checklist above. Identify which of the 10 items affect you. Items 1–3 are highest risk for remote servers.

**June 28:** Tier 1 SDKs ([TypeScript, Python, C#, and Go](https://modelcontextprotocol.io/docs/sdk)) are expected to ship RC-compatible versions — [beta releases in fact shipped June 29](https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/). Update and run your test suite against the new SDK.

**July 1–20:** Test behind a plain round-robin load balancer. If your server handles this cleanly, you're stateless. If not, you have three weeks to fix it.

**July 28:** Final spec ships. Clients that implemented the RC should need no changes. Servers not yet migrated will be out of spec.

---

## What This Doesn't Change

MCP's core value proposition is unchanged: tools, resources, and prompts as a standard interface between AI clients and capability servers. The JSON-RPC message structure is unchanged. The capability negotiation model — what's negotiated — is unchanged; only when and where it travels changes.

If you're running a local stdio MCP server (Claude Desktop, Claude Code, Cursor), the stateless changes have minimal impact on you. The session model primarily affected remote Streamable HTTP deployments. Local process-to-process communication over stdio isn't load-balanced.

---

The MCP 2026-07-28 release candidate is the spec that shipped as final 45 days after this article's publish date. The roadmap from March described where the protocol was going; this was the destination. Read the [official RC blog post](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/), the [final specification announcement](https://blog.modelcontextprotocol.io/posts/2026-07-28/), and the [official changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog) for the raw specification text. Then update your servers.

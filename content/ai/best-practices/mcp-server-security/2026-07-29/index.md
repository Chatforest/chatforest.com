---
title: "Building Secure MCP Servers — Best Practices (as of 29 Jul 2026)"
date: 2026-07-29
snapshot_date: 2026-07-29
topic: mcp-server-security
track: best-practices
audience: "technically comfortable readers"
description: "Concrete security practices for developers building MCP servers: input validation, prompt-injection defense, least-privilege tool design, secret management, the now-final 2026-07-28 OAuth/authorization requirements, rate limiting, transport hardening, and output sanitization — as of 29 Jul 2026."
content_type: "Best Practice"
categories: ["MCP", "AI Security", "Server Development"]
tags: ["mcp", "security", "prompt-injection", "oauth", "least-privilege", "secrets", "rate-limiting", "input-validation"]
last_refreshed: 2026-07-29
graded_by: "RingS panel (Skeptic/Beginner/Timekeeper) + sensei, 2026-07-29"
grading_result: "0 fabrications; 3 skeptic KILLs corrected (RFC 9728 false-novelty, scope-union misattribution, iss-emission role misattribution) + State Handle Hijacking mitigation added; 12 corrections this refresh"
---

<!-- content/ai/best-practices/mcp-server-security/2026-07-29/index.md — immutable dated snapshot -->

# Building Secure MCP Servers (as of 29 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **29 Jul 2026**, frozen here and kept as
> a permanent archive entry. This is a refresh of the [02 Jul 2026 snapshot](/ai/best-practices/mcp-server-security/2026-07-02/),
> updated now that the MCP 2026-07-28 specification has published as final. Corrections applied
> inline; unverifiable gaps marked ⚠ PENDING (#issue) — never guessed.

> ⚠️ **PROTOCOL UPDATE — the 2026-07-28 MCP specification is now FINAL.** It was a release
> candidate (locked 21 May 2026) at the time of the previous snapshot; it published as final on
> 28 Jul 2026. The transport is now stateless (no `initialize` handshake, no `Mcp-Session-Id` —
> see Practice 7). Authorization: **RFC 9728 (Protected Resource Metadata) is MUST for servers
> and clients — but this is NOT new, it was already a hard MUST, word-for-word identical, in the
> 2025-11-25 spec.** What genuinely is new: RFC 9207 issuer emission is SHOULD for authorization
> servers, but validation is MUST for clients when `iss` is present. Client ID Metadata Documents
> (CIMD) were already SHOULD-preferred before this revision; what's new is Dynamic Client
> Registration's *formal* deprecation (retained for a 12-month minimum window — see Practice 5).
> Per the MCP project's own 28 Jul 2026 announcement, all four Tier 1 SDKs (TypeScript, Python,
> Go, C#) support 2026-07-28 as of launch; the TypeScript SDK is splitting into a new
> `@modelcontextprotocol/{server,client,core,...}` v2 package family whose "beta" vs. "stable"
> status is inconsistently labeled between its own release notes and docs site as of this
> snapshot. 🕒 **verify live** before treating any specific package/version as production-ready.

## How to read the labels
- ✅ **independently-corroborated** — 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value

---

## Practice 1: Validate every tool input against a strict JSON Schema

**Do:** Define a complete `inputSchema` for every tool your MCP server exposes — use JSON Schema type constraints, `required` arrays, `enum` where values are bounded, `maxLength` on strings, and `minimum`/`maximum` on numbers. Reject (with a JSON-RPC protocol error) any `tools/call` request whose arguments do not conform. **Note the 2026-07-28 spec renumbers this and several other error codes** (see the changelog citation below, and Practice 7 for the unrelated new `-32020 HeaderMismatch` error) — the resource-not-found code moved from `-32002` to `-32602` for JSON-RPC alignment; verify current codes against your SDK version rather than hardcoding old numbers.

In Python, use `jsonschema` or Pydantic (`pip install pydantic`) for validation. In TypeScript, the SDK accepts Zod, Valibot, or ArkType schemas directly — install with `npm install zod` (Zod is the most widely used option).

**Why:** MCP clients pass tool arguments as raw JSON supplied ultimately by an LLM. LLMs hallucinate values and can be manipulated. Without server-side validation, a path argument meant to be `./reports/` could arrive as `../../../../etc/passwd`. Schema validation is your last line of defence that the client cannot bypass.

**Caveat:** Schema validation rejects structurally wrong inputs but does not catch semantically malicious ones — for example, a path that passes pattern validation but still escapes the intended directory. Pair schema checks with allow-list logic (see Practice 2).

**Sources:**
- [modelcontextprotocol.io — Tools spec 2025-11-25 (Security Considerations)](https://modelcontextprotocol.io/specification/2025-11-25/server/tools) (fetched 2026-07-02): "Servers MUST: Validate all tool inputs"
- [modelcontextprotocol.io — Changelog 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/changelog) (fetched 2026-07-29): JSON-RPC error code renumbering
- [github.com/modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk) (fetched 2026-07-02): SDK accepts Standard Schema-compatible libraries (Zod, Valibot, ArkType)
- [checkmarx.com — MCP Security Risks](https://checkmarx.com/learn/mcp-security-risks-real-world-incidents-and-security-controls/) (fetched 2026-07-02): "validate and sanitize all inputs before passing them to command execution functions"

**Confidence:** ✅ independently-corroborated (MCP spec/official docs + Checkmarx independent research)

---

## Practice 2: Sanitize tool outputs before returning them to the LLM

**Do:** Treat every string your tool returns as potentially hostile. Strip or escape content that looks like LLM instructions: phrases beginning with "Ignore previous instructions", XML-like tags (`<system>`, `<instructions>`), markdown headings that could be mistaken for new prompt sections, and shell/SQL injection payloads. Prefer returning structured JSON (`structuredContent`) with a declared `outputSchema`; a schema-validated object is much harder to poison than free text.

**Why:** Tool output flows directly into the LLM's context window and the model treats it as trusted. An attacker who controls the data your tool reads (a database row, an API response, a file) can embed instructions that hijack the agent's next action — indirect prompt injection. OWASP catalogues this as Tool Poisoning in its MCP Top 10 (Phase 3 Beta). The MCP spec explicitly states servers MUST sanitize tool outputs. Microsoft recommends "Spotlighting" and data-marking techniques to separate trusted instructions from untrusted tool output.

**Caveat:** Complete detection of injected instructions in free text is an open research problem — no filter is foolproof. Schema-constrained structured output is the strongest mitigation available today, but it limits expressiveness. The MCP spec notes `outputSchema` is optional; making it mandatory for your server is a deliberate hardening choice. OWASP MCP Top 10 is Phase 3 Beta — the specific category numbering and rankings may shift. The core tool-safety principle underlying this practice ("descriptions of tool behavior... should be considered untrusted, unless obtained from a trusted server") is confirmed carried forward verbatim into the 2026-07-28 spec text; the 2026-07-28 revision adds no *new* tool-poisoning/output-sanitization-specific countermeasures beyond that unchanged principle — it is accurate to say nothing new was added here, not accurate to say the topic goes unaddressed.

**Sources:**
- [owasp.org — MCP Tool Poisoning](https://owasp.org/www-community/attacks/MCP_Tool_Poisoning) (fetched 2026-07-02): attack description and defense — constrain tool response format to structured output with a fixed schema; reject responses not matching expected shape
- [developer.microsoft.com — Protecting against indirect injection attacks in MCP](https://developer.microsoft.com/blog/protecting-against-indirect-injection-attacks-mcp) (fetched 2026-07-02): Spotlighting and data-marking techniques
- [unit42.paloaltonetworks.com — MCP Attack Vectors](https://unit42.paloaltonetworks.com/model-context-protocol-attack-vectors/) (fetched 2026-07-02): filter instruction-like phrases from LLM outputs; documents conversation-hijacking via injected tool responses
- [modelcontextprotocol.io — Tools spec 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/server/tools) (fetched 2026-07-02): "Servers MUST: Sanitize tool outputs"

**Confidence:** ✅ independently-corroborated (OWASP + Microsoft + Palo Alto Unit 42, all independent of each other and of official MCP docs)

---

## Practice 3: Apply least-privilege tool design — expose only what's needed

**Do:** Each tool should carry the minimum permissions required for its single purpose. Do not bundle read + write + admin into one tool "for convenience." Run high-privilege tools (file-system access, database writes, internal API calls) in an isolated context that external MCP servers cannot reach. Implement progressive scope elevation: start with basic discovery/read scopes; issue targeted `WWW-Authenticate` scope challenges only when a privileged operation is first attempted. As a **server**, when you issue a challenge, the 2026-07-28 spec asks you to bundle all scopes needed for the *current operation* into a single consolidated challenge rather than dribbling them out one at a time — but you are explicitly NOT required to track or re-include the client's previously-granted scopes; that accumulation is the client's responsibility, not yours (see Practice 5).

**Why:** If any one tool is compromised — by a malicious client, an injection attack, or a bug — the blast radius is bounded by that tool's permissions. Broad permissions mean a single exploited tool can do anything the server can do. OWASP recommends isolating privileged tools — running high-risk operations in separate agent contexts that external servers cannot access. Practical DevSecOps independently documents: "Tools should operate with minimum necessary permissions only. Implement granular access controls and sandboxing."

**Caveat:** Progressive scope elevation adds round-trips and UI complexity. The MCP spec section on Scope Minimization calls wildcard scopes (`*`, `all`, `full-access`) an explicit anti-pattern and warns against "bundling unrelated privileges to preempt future prompts."

**Sources:**
- [modelcontextprotocol.io — Security Best Practices 2025-11-25 (Scope Minimization)](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) (fetched 2026-07-02): MUST avoid omnibus scopes; MAY issue only a subset of requested scopes
- [modelcontextprotocol.io — Authorization 2026-07-28 (Step-Up Authorization Flow)](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) (fetched 2026-07-29): consolidated single-challenge guidance
- [owasp.org — MCP Tool Poisoning](https://owasp.org/www-community/attacks/MCP_Tool_Poisoning) (fetched 2026-07-02): isolate privileged tools in separate agent contexts (Phase 3 Beta)
- [practical-devsecops.com — MCP Security Vulnerabilities](https://www.practical-devsecops.com/mcp-security-vulnerabilities/) (fetched 2026-07-02): "Tools should operate with minimum necessary permissions only. Implement granular access controls and sandboxing."

**Confidence:** ✅ independently-corroborated (official MCP spec + OWASP + Practical DevSecOps)

---

## Practice 4: Never store secrets in code — use runtime secret injection

**Do:** ⚠️ Do not hardcode API keys, database passwords, or tokens in your server source code, Dockerfiles, or committed config files. Load credentials at runtime from: (a) environment variables injected by your orchestrator/secrets manager, or (b) a secrets vault (AWS Secrets Manager, HashiCorp Vault, GCP Secret Manager, Azure Key Vault). Issue short-lived, scoped tokens per session rather than static long-lived keys. Rotate production keys regularly. Maintain completely separate credentials for dev/staging/production.

When wrapping your MCP server with a secrets manager, pin the exact package version being wrapped — for example:
```
infisical run -- npx -y weather-mcp-server@1.2.3
```
The `-y` flag skips prompts but does not pin versions. Always specify an exact version alongside it. See Practice 7 in [mcp-security-fundamentals](/ai/best-practices/mcp-security-fundamentals/) for why unversioned installs are a supply-chain risk.

**Why:** 🕒 Per an Astrix survey of 5,205 open-source MCP servers (published 2025 — verify live, ecosystem has grown substantially): approximately 88% require credentials, 79% pass keys via environment variables, and approximately 8.5% use OAuth. These percentages are likely to have shifted since the survey, particularly the OAuth adoption rate, as the community has responded to well-publicized CVEs. Token mismanagement is OWASP MCP Top 10 number-one risk (Phase 3 Beta). A leaked credential gives an attacker access to everything that credential controls, across every service the MCP server touches.

**Caveat:** Environment variables are the most common mitigation but are not themselves secure storage — they appear in process listings and are visible to any code running in the same process. For high-security deployments, prefer vault-based runtime injection over env vars. 🕒 Vault product capabilities and pricing change frequently; verify live before choosing.

**Sources:**
- [owasp.org — MCP01:2025 Token Mismanagement and Secret Exposure](https://owasp.org/www-project-mcp-top-10/2025/MCP01-2025-Token-Mismanagement-and-Secret-Exposure) (fetched 2026-07-02): ranked #1 in Phase 3 Beta; vault, short-lived scoped tokens, log masking
- [infisical.com — Managing Secrets in MCP Servers](https://infisical.com/blog/managing-secrets-mcp-servers) (fetched 2026-07-02): "Avoid Hardcoding"; CLI injection pattern; per-server access isolation
- [astrix.security — State of MCP Server Security 2025](https://astrix.security/learn/blog/state-of-mcp-server-security-2025/) (fetched 2026-07-02): survey of 5,205 servers; credential statistics (2025 figures — 🕒 verify live)
- [stainless.com — MCP Server API Key Management Best Practices](https://www.stainless.com/mcp/mcp-server-api-key-management-best-practices/) (fetched 2026-07-02): rotation schedule, environment separation, scope minimization

**Confidence:** ✅ independently-corroborated (OWASP + Infisical + Astrix + Stainless — four independent publishers)

---

## Practice 5: Implement OAuth 2.1 with PKCE for HTTP-transport servers; expose RFC 9728 discovery; never pass tokens through — and know which authorization obligations are yours vs. your authorization server's

**Bottom line:** an MCP server is an OAuth 2.1 *resource server*, not an authorization server. RFC 9728 discovery (MUST) is your job and is unchanged from 2025-11-25. RFC 9207 `iss` emission is genuinely new in 2026-07-28 — but it's the *authorization server's* job (SHOULD), not yours, unless you also operate the authorization server yourself.

**Do:** For any MCP server exposed over HTTP, implement the OAuth 2.1 authorization flow with mandatory PKCE — this base requirement is unchanged by the 2026-07-28 spec. Validate every incoming `Authorization: Bearer <token>` header on every request (not just once at session start). Validate the token audience — only accept tokens explicitly issued for your MCP server. Never forward a client's token to an upstream API ("token passthrough"); instead, issue your own bound token to upstream services. Return HTTP 401 for missing/invalid tokens, 403 for insufficient scope. Use `__Host-` cookie prefix, `Secure`, `HttpOnly`, `SameSite=Lax` if using consent cookies.

Two authorization requirements to know, one of which is genuinely new to 2026-07-28:
1. **RFC 9728 (Protected Resource Metadata) — not new.** Your server MUST expose a `.well-known/oauth-protected-resource` endpoint so clients can discover which authorization server protects you. This was already a hard MUST, worded identically, in the 2025-11-25 spec — it is not a 2026-07-28 change, despite being easy to mistake for one alongside the other authorization updates.
2. **RFC 9207 issuer validation — genuinely new.** This is an obligation on the **authorization server**, not on your MCP resource server: it (the AS) SHOULD include the `iss` parameter in authorization responses (including error responses) and, if it does, MUST advertise `authorization_response_iss_parameter_supported: true` in its metadata. **If you also operate the authorization server** (some MCP server deployments bundle both roles), implement `iss` emission now — the spec signals a future revision will upgrade it to MUST. **If you use a separate/third-party authorization server**, your action item is to choose or configure one that emits `iss`, and — if you also act as an OAuth client anywhere in your stack — to validate a present `iss` (already a MUST for clients).

For client registration, prefer supporting OAuth Client ID Metadata Documents (CIMD) — already a SHOULD before this revision, not new — over Dynamic Client Registration (DCR). What IS new: DCR's *formal* deprecation (retained for a 12-month minimum compatibility window) for authorization servers that don't yet support CIMD.

**⚠️ WARNING:** For **stdio transport, do NOT implement this OAuth flow** — instead retrieve credentials from the environment. The spec explicitly states stdio implementations SHOULD NOT follow the HTTP authorization spec. The mistake to avoid: running an OAuth redirect flow inside a stdio server — the browser-redirect step requires an HTTP endpoint, which stdio does not have, so you either expose an unintended HTTP listener or the flow silently fails and falls back to no authentication.

**Why:** Token passthrough is explicitly forbidden by the MCP authorization spec because it lets malicious clients bypass your server's rate limits, audit logging, and access controls. A client-supplied token that your server blindly forwards could be a stolen token with broad scopes, letting the attacker impersonate the original user against your upstream APIs. RFC 9728 removes the need for clients to hardcode which authorization server protects your API. RFC 9207 issuer validation defends against "mix-up attacks" where a client is tricked into sending a code to the wrong authorization server.

**Caveat:** OAuth 2.1 itself is still an IETF draft — cite the current datatracker revision rather than a pinned dash-number, since these advance every few weeks (this snapshot's research found `-13` and `-14` both cited on different MCP spec pages, and the datatracker's actual current revision was neither — a symptom of exactly this churn). CIMD is built on a similarly unstable IETF draft. **Do not over-state RFC 9207 as a universal MUST** — it is precisely SHOULD-for-authorization-server-emission / MUST-for-client-validation-when-present, a distinction several secondary sources blur, and it is an obligation on the authorization server, not the MCP resource server (see Do section above).

**Sources:**
- [modelcontextprotocol.io — Authorization spec 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) (fetched 2026-07-29): RFC 9728 MUST; RFC 9207 SHOULD-emit/MUST-validate split; CIMD SHOULD; DCR deprecated-but-retained; PKCE/token-passthrough/audience-validation unchanged
- [modelcontextprotocol.io — Authorization 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) (fetched 2026-07-29): confirms RFC 9728 MUST and CIMD SHOULD are both worded identically here — neither is new to 2026-07-28
- [modelcontextprotocol.io — Client Registration 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/client-registration) (fetched 2026-07-29): CIMD mechanics, registration priority order
- [modelcontextprotocol.io — Changelog 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/changelog) (fetched 2026-07-29): SEP-2468 (RFC 9207), DCR deprecation PR #2858
- [workos.com — The biggest MCP spec update ships July 28](https://workos.com/blog/mcp-2026-spec-agent-authentication) (fetched 2026-07-29): independent corroboration (simplifies MUST/SHOULD split — verify precision against primary spec)
- [checkmarx.com — MCP Security Risks](https://checkmarx.com/learn/mcp-security-risks-real-world-incidents-and-security-controls/) (fetched 2026-07-02): "Enforce strict OAuth state parameter validation"; "short-lived and revocable credentials bound to specific resource servers"

**Confidence:** ✅ independently-corroborated (base OAuth 2.1/PKCE/token-passthrough requirements); the precise RFC 9207/CIMD normative split and the resource-server-vs-authorization-server role distinction is 📄 vendor-documented (only the primary spec states it correctly)

---

## Practice 6: Rate-limit tool invocations and impose execution timeouts

**Do:** Enforce per-client rate limits on `tools/call` requests — both requests-per-minute and total tokens/compute consumed per session. Set a maximum execution timeout for every tool handler; fail with `isError: true` if the tool exceeds it. For compute-intensive tools, add per-operation quotas. Log all tool invocations with client identity for audit purposes.

The MCP SDK (Python or TypeScript) does not provide built-in rate-limiting middleware as of this writing — you must add it at the framework/transport layer. A minimal working example using Express and `express-rate-limit`:

```javascript
const rateLimit = require('express-rate-limit')
// npm install express-rate-limit
app.use('/mcp', rateLimit({ windowMs: 60_000, max: 60 }))
```

For non-Express setups, consider an API gateway (AWS API Gateway, Kong) or a reverse proxy (nginx `limit_req_zone`). 🕒 SDK features change quickly; verify whether the current SDK version now ships rate-limiting middleware — the MCP project states all four Tier 1 SDKs support 2026-07-28 as of 28 Jul 2026 (see banner), but this entry did not independently verify whether rate-limiting middleware specifically was added in that cycle.

**Why:** ⚠️ Without rate limits, a single malicious or malfunctioning client can drain your server's resources, consume upstream API quotas (triggering unexpected billing), or use MCP's sampling capability to drain your AI compute budget. Palo Alto Unit 42 documented "resource theft via sampling abuse" as a live attack vector. The MCP tools spec lists rate limiting as a server MUST. **Note:** as of 2026-07-28, server-initiated sampling/elicitation requests are restructured under the new Multi Round-Trip Requests (MRTR) pattern — servers return an `InputRequiredResult` instead of sending a separate JSON-RPC request — but the underlying rate-limiting obligation is unchanged.

**Caveat:** Rate limiting at the application layer is bypassable if an attacker controls many source IPs. For stronger protection, enforce limits at the gateway or network layer. Token-bucket or sliding-window algorithms are more resistant to burst abuse than fixed-window counters.

**Sources:**
- [modelcontextprotocol.io — Tools spec 2025-11-25 (Security Considerations)](https://modelcontextprotocol.io/specification/2025-11-25/server/tools) (fetched 2026-07-02): "Servers MUST: Rate limit tool invocations"
- [modelcontextprotocol.io — Changelog 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/changelog) (fetched 2026-07-29): MRTR pattern (SEP-2322) replaces server-initiated sampling/elicitation requests
- [unit42.paloaltonetworks.com — MCP Attack Vectors](https://unit42.paloaltonetworks.com/model-context-protocol-attack-vectors/) (fetched 2026-07-02): "Resource theft via sampling abuse — Attackers can drain AI compute quotas"; "Implement rate limiting on sampling frequency requests"
- [checkmarx.com — MCP Security Risks](https://checkmarx.com/learn/mcp-security-risks-real-world-incidents-and-security-controls/) (fetched 2026-07-02): "Apply timeouts, rate limits, command allowlists, output filtering, data-loss prevention checks, and response validation"

**Confidence:** ✅ independently-corroborated (official MCP spec + Palo Alto Unit 42 + Checkmarx)

---

## Practice 7: Harden Streamable HTTP transport — validate Origin, bind to localhost, use HTTPS; understand the 2026-07-28 stateless shift

**Do:** For HTTP-transport MCP servers:
1. Validate the `Origin` header on every incoming connection to block DNS rebinding attacks — unchanged MUST as of 2026-07-28.
2. When running locally, bind to `127.0.0.1` (not `0.0.0.0`) — binding to all interfaces exposes the server to the entire network.
3. Use HTTPS in production; reject `http://` URIs except for loopback addresses.
4. Block outbound requests to private IP ranges (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`, `169.254.0.0/16`) to prevent SSRF. Cloud providers expose sensitive configuration data at `169.254.169.254` (the metadata service); block that address explicitly. Consider the Smokescreen egress proxy for automated blocking.
5. **As of 2026-07-28, do not mint or rely on session IDs at all** — the `Mcp-Session-Id` header and the `initialize`/`initialized` handshake are both removed from the protocol. If your server needs state across calls, mint an explicit, application-level handle (e.g., an order or basket ID) and require it as an ordinary tool argument, not transport metadata. This means any server instance can now handle any request — useful for a plain round-robin load balancer, no sticky sessions required. **This explicit-handle pattern creates a new risk the spec names "State Handle Hijacking":** if an attacker obtains or guesses a handle, they can access or modify another user's state. MUST NOT treat mere possession of a handle as authentication. SHOULD generate handles with a secure random number generator (not sequential IDs). SHOULD bind each handle server-side to the authenticated user — for example, store state keyed as `<user_id>:<handle>`, not just `<handle>`, so a guessed or leaked handle alone is insufficient to access another user's data.
6. New as of 2026-07-28: `Mcp-Method` and `Mcp-Name` headers are REQUIRED on every Streamable HTTP request and must exactly match the corresponding fields in the JSON-RPC body — servers MUST reject mismatches with JSON-RPC error `-32020`. This lets gateways/load balancers route and rate-limit without parsing the request body.

**Why:** ⚠️ The MCP transport spec contains an explicit "Security Warning" about Origin validation, localhost binding, and HTTPS. A locally running MCP server bound to `0.0.0.0` without Origin validation is reachable by any website the user visits via DNS rebinding — a remote attacker can then invoke your tools with the user's local filesystem permissions. The stateless shift removes an entire class of session-fixation and session-hijacking bugs tied to the old `Mcp-Session-Id` mechanism, at the cost of requiring you to redesign any server logic that assumed a sticky per-connection session.

**⚠️ WARNING — legacy compatibility gap:** If you upgrade your server to implement only 2026-07-28, legacy clients that still send `initialize` and expect `Mcp-Session-Id` will fail outright — the spec describes no automatic fallback in that direction (only the reverse: a dual-era client can fall back to a legacy server). If you need to support both eras, implement dual-era support explicitly rather than assuming forward compatibility.

**Caveat:** DNS rebinding protection via Origin header alone is fragile in non-browser contexts; pair it with authentication tokens for defense-in-depth. 🕒 SDK middleware defaults (Express/Hono packages) for the new required headers and session removal — verify current behavior against your SDK's migration guide before upgrading a production server; the MCP project states all four Tier 1 SDKs support 2026-07-28 as of launch (see banner), but middleware-level defaults for these specific headers were not independently verified this session.

**Sources:**
- [modelcontextprotocol.io — Transports spec 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http) (fetched 2026-07-29): Security & Endpoint section (Origin/localhost/auth, unchanged); protocol-level session and GET-stream removal; `Mcp-Method`/`Mcp-Name` required-header table and `-32020 HeaderMismatch`
- [modelcontextprotocol.io — Changelog 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/changelog) (fetched 2026-07-29): `initialize`/`initialized` handshake removal (SEP-2575), `Mcp-Session-Id` removal (SEP-2567)
- [modelcontextprotocol.io — Versioning 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning) (fetched 2026-07-29): legacy-vs-modern compatibility matrix; "legacy clients have no fall-forward mechanism"
- [modelcontextprotocol.io — Security Best Practices 2025-11-25 (SSRF section)](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) (fetched 2026-07-02): full SSRF attack/mitigation section with specific IP ranges; Smokescreen egress proxy recommendation
- [blog.modelcontextprotocol.io — The 2026-07-28 Specification](https://blog.modelcontextprotocol.io/posts/2026-07-28/) (fetched 2026-07-29): "Any request can now land on any server instance behind a plain round-robin load balancer without needing shared storage" — final-spec-dated equivalent of the RC-era round-robin claim
- [modelcontextprotocol.io — Security Best Practices (State Handle Hijacking section)](https://modelcontextprotocol.io/docs/draft/tutorials/security/security_best_practices) (fetched 2026-07-29): MUST NOT treat handle possession as authentication; SHOULD use non-deterministic handles; SHOULD bind to authenticated user

**Confidence:** 📄 vendor-documented (all primary sources are official MCP spec/docs)

---

## Practice 8: Never let secrets appear in tool output, logs, or error messages

**Do:** Before your tool handler returns its result, scrub the text content for secrets: API keys, bearer tokens, database connection strings, private keys. Use a masking library or regex to replace matches with `[REDACTED]`. Apply the same scrubbing to exception messages and server-side logs. Mark log files containing tool invocation history as sensitive and restrict access.

Until a dedicated MCP-specific secret-scrubbing library emerges, starting points include: the `detect-secrets` tool (Python, from Yelp — entropy-based and pattern-based scanning) or the `secretlint` npm package (pattern-based; pluggable rule set). Both are actively maintained starting points, not complete solutions.

**Why:** Tool output is passed directly to the LLM context and may be surfaced to the user or persisted in conversation history. An upstream API returning an error that echoes back your own credentials — or a stack trace containing a database URL — puts those credentials into the AI's context window, where prompt injection could exfiltrate them. OWASP ranks this as MCP01:2025 (Token Mismanagement). A real incident: Anthropic's own Git MCP server CVE (November 2025, in mcp-server-git) included path validation bypass that led to credential leakage via tool output.

**Caveat:** Regex-based secret scrubbing produces false negatives (novel token formats) and false positives (legitimate data matching patterns). Entropy-based detection reduces false negatives but requires tuning. There is no universally accepted secret-scrubbing library for MCP servers yet — this is an area of active tooling development.

**Sources:**
- [owasp.org — MCP01:2025 Token Mismanagement and Secret Exposure](https://owasp.org/www-project-mcp-top-10/2025/MCP01-2025-Token-Mismanagement-and-Secret-Exposure) (fetched 2026-07-02): Phase 3 Beta; "Prevent sensitive data persistence in model memory or context windows through redaction and ephemeral contexts"; "Mask secrets in diagnostic traces with protected access controls"
- [checkmarx.com — MCP Security Risks](https://checkmarx.com/learn/mcp-security-risks-real-world-incidents-and-security-controls/) (fetched 2026-07-02): Anthropic's Git MCP Server CVE (Nov 2025): path validation bypass → credential leakage via tool output; malicious npm package (Sept 2025) silently added BCC to exfiltrate data

**Confidence:** ✅ independently-corroborated (OWASP + Checkmarx, two independent publishers)

---

## Practice 9: Prevent confused-deputy attacks in proxy MCP servers

**Do:** This practice applies only if your MCP server acts as a proxy to a third-party API using a static OAuth client ID. If you are not building a proxy, skip this practice.

If you are: implement per-MCP-client consent before forwarding to the third-party authorization server. Store consent decisions server-side, keyed to the specific MCP `client_id`. Validate that `redirect_uri` in authorization requests exactly matches the registered URI (exact string match, no wildcards). Generate a cryptographically secure, single-use `state` parameter for each OAuth request and store it server-side only after the user approves consent — not before.

**Why:** When your MCP server holds a single OAuth credential for a third-party API but accepts many different MCP clients, an attacker can exploit the fact that the third-party already has a consent cookie for your server's static client ID. By sending a malicious link to the user with a crafted `redirect_uri` pointing to attacker.com, the attacker can steal the authorization code without the user seeing a consent screen.

**Caveat:** This attack only applies to proxy architectures with a static upstream client ID. If your MCP server issues its own credentials and does not act as a proxy, this practice is not relevant. Setting the state cookie before consent approval nullifies the protection — order matters. Confirmed unchanged in substance by the 2026-07-28 spec.

**Sources:**
- [modelcontextprotocol.io — Security Best Practices 2025-11-25 (Confused Deputy section)](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) (fetched 2026-07-02): complete attack flow diagrams; MUST requirements for per-client consent storage; cookie security (`__Host-` prefix, `Secure`, `HttpOnly`, `SameSite=Lax`); exact `redirect_uri` matching; single-use `state` parameter
- [modelcontextprotocol.io — Authorization 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) (fetched 2026-07-29): confirmed confused-deputy language carried forward unchanged

**Confidence:** 📄 vendor-documented

---

## Held pending fixes (not publish-ready)

- **Rate-limiting SDK status ⚠ #pending-1:** Could not confirm which version of the Python or TypeScript SDK ships rate-limiting middleware specifically (if any). 🕒 verify live.
- **Secret-scrubbing library ⚠ #pending-2:** No MCP-specific secret-scrubbing library could be independently verified this session. `detect-secrets` and `secretlint` named as starting points; a dedicated MCP solution may emerge.
- **TypeScript SDK v2 beta-vs-stable labeling ⚠ #pending-3:** The new `@modelcontextprotocol/{server,client,core,...}` v2 package family's GitHub release notes call it "beta" while its docs site calls it "the stable release line" — an unresolved inconsistency as of this snapshot.

## CHANGELOG (grading → this entry)

Carried forward from 2026-07-02 snapshot (unchanged content, items 1–11 — see prior snapshot's CHANGELOG for full detail). New items for this 2026-07-29 refresh:

12. **Refresh trigger:** MCP 2026-07-28 spec confirmed published as FINAL (was RC at time of prior snapshot). Banner rewritten to reflect final status.
13. **Skeptic KILL-1 — corrected:** removed false claim that RFC 9728 is a *new* 2026-07-28 requirement (banner + Practice 5). Confirmed via direct 2025-11-25 spec fetch: word-for-word identical MUST already present. Only RFC 9207 is genuinely new. Resolved the (self-contradictory) "RFC 9728 novelty ⚠ pending" item.
14. **Skeptic KILL-2 — corrected:** Practice 3's scope-elevation guidance wrongly told server builders to include the union of previously-granted and new scopes in a challenge. The spec assigns that union step to the **client**; the server's obligation is narrower (single challenge covering only the *current operation's* scopes).
15. **Skeptic KILL-3 — corrected:** Practice 5 wrongly instructed MCP server builders to emit the `iss` parameter. The spec's subject for `iss` emission is the **authorization server**, a distinct role from the MCP resource server. Reworded to route the action item correctly (implement it yourself only if you also operate the AS; otherwise choose an AS that does, and validate `iss` in any client role).
16. Practice 7: added full explanation of the stateless-transport shift (initialize handshake + Mcp-Session-Id removal, explicit-handle pattern), the new required `Mcp-Method`/`Mcp-Name` headers and `-32020 HeaderMismatch` error, and the legacy-client-vs-modern-server compatibility gap. Fixed stale "Security Warning" section-heading reference (now "Security & Endpoint") and replaced the RC-dated round-robin source with the final-spec-dated equivalent quote (Skeptic FLAG-5, FLAG-7).
17. Practice 6: added MRTR pattern note (server-initiated sampling/elicitation now via `InputRequiredResult`, not a separate JSON-RPC request); rate-limiting obligation itself unchanged. Replaced "could not confirm SDK status" with the MCP project's own statement that all four Tier 1 SDKs support 2026-07-28 as of launch.
18. Practice 1: added error-code renumbering note (resource-not-found `-32002`→`-32602`); fixed broken cross-reference that pointed to "Practice 7's caveat" for content that isn't there (Beginner-panel FIX).
19. Practice 9: confirmed confused-deputy requirements unchanged in substance by the new spec (added confirming citation).
20. Practice 5: added a "Bottom line" summary line ahead of the detailed MUST/SHOULD breakdown (Beginner-panel FIX); replaced pinned IETF draft dash-numbers with guidance to cite the current datatracker revision, since both cited numbers had already advanced by publish time (Timekeeper FIX).
21. Removed resolved/superseded pending items (SDK stable-release status, RFC 9728 novelty) from Held section; added the one genuinely unresolved item (TypeScript SDK v2 beta-vs-stable labeling).
22. **Skeptic FIX-1 — added (had been missed in the first correction pass):** Practice 7 was missing the spec's new "State Handle Hijacking" mitigation — the single most consequential security change tied to the stateless-transport shift (MUST NOT treat handle possession as authentication; SHOULD use non-deterministic handles; SHOULD bind handles to the authenticated user). Added with source citation.
23. **Skeptic FIX-10 — corrected (had been missed in the first correction pass):** Practice 2's caveat wrongly said the 2026-07-28 spec's effect on tool-poisoning/output-sanitization guidance was "unresearched." Corrected: the core tool-safety principle is confirmed carried forward verbatim; the revision adds no new countermeasures, but the topic is not unaddressed.

---
title: "Building Secure MCP Servers — Best Practices (as of 02 Jul 2026)"
date: 2026-07-02
snapshot_date: 2026-07-02
topic: mcp-server-security
track: best-practices
audience: "technically comfortable readers"
description: "Concrete security practices for developers building MCP servers: input validation, prompt-injection defense, least-privilege tool design, secret management, OAuth 2.1 auth, rate limiting, transport hardening, and output sanitization — as of 02 Jul 2026."
content_type: "Best Practice"
categories: ["MCP", "AI Security", "Server Development"]
tags: ["mcp", "security", "prompt-injection", "oauth", "least-privilege", "secrets", "rate-limiting", "input-validation"]
last_refreshed: 2026-07-02
graded_by: "RingS panel (Skeptic/Beginner/Timekeeper) + sensei, 2026-07-02"
grading_result: "0 fabrications; 11 corrections applied; 2 pending gaps (rate-limiting SDK, secret-scrubbing library)"
---

<!-- content/ai/best-practices/mcp-server-security/2026-07-02/index.md — immutable dated snapshot -->

# Building Secure MCP Servers (as of 02 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **02 Jul 2026**, frozen here and kept as
> a permanent archive entry. Research-drafted by a pupil, graded by the 3-lens panel + sensei.
> Corrections applied inline; unverifiable gaps marked ⚠ PENDING (#issue) — never guessed.

> ⚠️ **Upcoming spec change:** The 2026-07-28 MCP specification finalizes July 28, 2026 (26 days
> from this snapshot). It introduces breaking changes to authorization: mandatory RFC 9728
> (Protected Resource Metadata), issuer validation via RFC 9207, and a shift from Dynamic Client
> Registration (DCR) to OAuth Client ID Metadata Documents (CIMD). Practice 5 (OAuth) is directly
> affected. 🕒 **Re-verify your OAuth implementation against the new spec after July 28.**
> **A refresh snapshot is planned for 2026-08-01.**

## How to read the labels
- ✅ **independently-corroborated** — 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value

---

## Practice 1: Validate every tool input against a strict JSON Schema

**Do:** Define a complete `inputSchema` for every tool your MCP server exposes — use JSON Schema type constraints, `required` arrays, `enum` where values are bounded, `maxLength` on strings, and `minimum`/`maximum` on numbers. Reject (with a JSON-RPC protocol error, code `-32602`) any `tools/call` request whose arguments do not conform.

In Python, use `jsonschema` or Pydantic (`pip install pydantic`) for validation. In TypeScript, the SDK accepts Zod, Valibot, or ArkType schemas directly — install with `npm install zod` (Zod is the most widely used option).

**Why:** MCP clients pass tool arguments as raw JSON supplied ultimately by an LLM. LLMs hallucinate values and can be manipulated. Without server-side validation, a path argument meant to be `./reports/` could arrive as `../../../../etc/passwd`. Schema validation is your last line of defence that the client cannot bypass.

**Caveat:** Schema validation rejects structurally wrong inputs but does not catch semantically malicious ones — for example, a path that passes pattern validation but still escapes the intended directory. Pair schema checks with allow-list logic (see Practice 2).

**Sources:**
- [modelcontextprotocol.io — Tools spec 2025-11-25 (Security Considerations)](https://modelcontextprotocol.io/specification/2025-11-25/server/tools) (fetched 2026-07-02): "Servers MUST: Validate all tool inputs"
- [modelcontextprotocol.io — Tools concept page](https://modelcontextprotocol.io/docs/concepts/tools) (fetched 2026-07-02): same MUST requirement, plus `outputSchema` for structured responses
- [github.com/modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk) (fetched 2026-07-02): SDK accepts Standard Schema-compatible libraries (Zod, Valibot, ArkType)
- [checkmarx.com — MCP Security Risks](https://checkmarx.com/learn/mcp-security-risks-real-world-incidents-and-security-controls/) (fetched 2026-07-02): "validate and sanitize all inputs before passing them to command execution functions"

**Confidence:** ✅ independently-corroborated (MCP spec/official docs + Checkmarx independent research)

---

## Practice 2: Sanitize tool outputs before returning them to the LLM

**Do:** Treat every string your tool returns as potentially hostile. Strip or escape content that looks like LLM instructions: phrases beginning with "Ignore previous instructions", XML-like tags (`<system>`, `<instructions>`), markdown headings that could be mistaken for new prompt sections, and shell/SQL injection payloads. Prefer returning structured JSON (`structuredContent`) with a declared `outputSchema`; a schema-validated object is much harder to poison than free text.

**Why:** Tool output flows directly into the LLM's context window and the model treats it as trusted. An attacker who controls the data your tool reads (a database row, an API response, a file) can embed instructions that hijack the agent's next action — indirect prompt injection. OWASP catalogues this as Tool Poisoning in its MCP Top 10 (Phase 3 Beta). The MCP spec explicitly states servers MUST sanitize tool outputs. Microsoft recommends "Spotlighting" and data-marking techniques to separate trusted instructions from untrusted tool output.

**Caveat:** Complete detection of injected instructions in free text is an open research problem — no filter is foolproof. Schema-constrained structured output is the strongest mitigation available today, but it limits expressiveness. The MCP spec notes `outputSchema` is optional; making it mandatory for your server is a deliberate hardening choice. OWASP MCP Top 10 is Phase 3 Beta — the specific category numbering and rankings may shift.

**Sources:**
- [owasp.org — MCP Tool Poisoning](https://owasp.org/www-community/attacks/MCP_Tool_Poisoning) (fetched 2026-07-02): attack description and defense — constrain tool response format to structured output with a fixed schema; reject responses not matching expected shape
- [developer.microsoft.com — Protecting against indirect injection attacks in MCP](https://developer.microsoft.com/blog/protecting-against-indirect-injection-attacks-mcp) (fetched 2026-07-02): Spotlighting and data-marking techniques
- [unit42.paloaltonetworks.com — MCP Attack Vectors](https://unit42.paloaltonetworks.com/model-context-protocol-attack-vectors/) (fetched 2026-07-02): filter instruction-like phrases from LLM outputs; documents conversation-hijacking via injected tool responses
- [modelcontextprotocol.io — Tools spec 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/server/tools) (fetched 2026-07-02): "Servers MUST: Sanitize tool outputs"

**Confidence:** ✅ independently-corroborated (OWASP + Microsoft + Palo Alto Unit 42, all independent of each other and of official MCP docs)

---

## Practice 3: Apply least-privilege tool design — expose only what's needed

**Do:** Each tool should carry the minimum permissions required for its single purpose. Do not bundle read + write + admin into one tool "for convenience." Run high-privilege tools (file-system access, database writes, internal API calls) in an isolated context that external MCP servers cannot reach. Implement progressive scope elevation: start with basic discovery/read scopes; issue targeted `WWW-Authenticate` scope challenges only when a privileged operation is first attempted.

**Why:** If any one tool is compromised — by a malicious client, an injection attack, or a bug — the blast radius is bounded by that tool's permissions. Broad permissions mean a single exploited tool can do anything the server can do. OWASP recommends isolating privileged tools — running high-risk operations in separate agent contexts that external servers cannot access. Practical DevSecOps independently documents: "Tools should operate with minimum necessary permissions only. Implement granular access controls and sandboxing."

**Caveat:** Progressive scope elevation adds round-trips and UI complexity. The MCP spec section on Scope Minimization calls wildcard scopes (`*`, `all`, `full-access`) an explicit anti-pattern and warns against "bundling unrelated privileges to preempt future prompts."

**Sources:**
- [modelcontextprotocol.io — Security Best Practices 2025-11-25 (Scope Minimization)](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) (fetched 2026-07-02): MUST avoid omnibus scopes; MAY issue only a subset of requested scopes
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

## Practice 5: Implement OAuth 2.1 with PKCE for HTTP-transport servers; never pass tokens through

**Do:** For any MCP server exposed over HTTP, implement the OAuth 2.1 authorization flow with mandatory PKCE. Validate every incoming `Authorization: Bearer <token>` header on every request (not just once at session start). Validate the token audience — only accept tokens explicitly issued for your MCP server. Never forward a client's token to an upstream API ("token passthrough"); instead, issue your own bound token to upstream services. Return HTTP 401 for missing/invalid tokens, 403 for insufficient scope. Use `__Host-` cookie prefix, `Secure`, `HttpOnly`, `SameSite=Lax` if using consent cookies.

**⚠️ WARNING:** For **stdio transport, do NOT implement this OAuth flow** — instead retrieve credentials from the environment. The spec explicitly states stdio implementations SHOULD NOT follow the HTTP authorization spec. The mistake to avoid: running an OAuth redirect flow inside a stdio server — the browser-redirect step requires an HTTP endpoint, which stdio does not have, so you either expose an unintended HTTP listener or the flow silently fails and falls back to no authentication.

**Why:** Token passthrough is explicitly forbidden by the MCP authorization spec because it lets malicious clients bypass your server's rate limits, audit logging, and access controls. A client-supplied token that your server blindly forwards could be a stolen token with broad scopes, letting the attacker impersonate the original user against your upstream APIs.

**Caveat:** 🕒 **verify live after 2026-07-28:** The 2026-07-28 MCP spec RC introduces breaking authorization changes — servers MUST implement RFC 9728 (OAuth 2.0 Protected Resource Metadata), clients MUST validate issuer via RFC 9207, and preferred client registration shifts from Dynamic Client Registration (DCR) to OAuth Client ID Metadata Documents (CIMD). These are new MUSTs not present in the 2025-11-25 spec. OAuth 2.1 is still an IETF draft (draft-ietf-oauth-v2-1-15, expires 2026-09-03); verify RFC status.

**Sources:**
- [modelcontextprotocol.io — Authorization spec 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) (fetched 2026-07-02): MUST implement OAuth 2.1; PKCE REQUIRED; token passthrough explicitly forbidden; MUST validate token audience
- [modelcontextprotocol.io — Security Best Practices 2025-11-25 (Token Passthrough)](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) (fetched 2026-07-02): full attack/mitigation section
- [checkmarx.com — MCP Security Risks](https://checkmarx.com/learn/mcp-security-risks-real-world-incidents-and-security-controls/) (fetched 2026-07-02): "Enforce strict OAuth state parameter validation"; "short-lived and revocable credentials bound to specific resource servers"

**Confidence:** ✅ independently-corroborated (official MCP spec + Checkmarx independent research)

---

## Practice 6: Rate-limit tool invocations and impose execution timeouts

**Do:** Enforce per-client rate limits on `tools/call` requests — both requests-per-minute and total tokens/compute consumed per session. Set a maximum execution timeout for every tool handler; fail with `isError: true` if the tool exceeds it. For compute-intensive tools, add per-operation quotas. Log all tool invocations with client identity for audit purposes.

The MCP SDK (Python or TypeScript) does not provide built-in rate-limiting middleware as of this writing — you must add it at the framework/transport layer. A minimal working example using Express and `express-rate-limit`:

```javascript
const rateLimit = require('express-rate-limit')
// npm install express-rate-limit
app.use('/mcp', rateLimit({ windowMs: 60_000, max: 60 }))
```

For non-Express setups, consider an API gateway (AWS API Gateway, Kong) or a reverse proxy (nginx `limit_req_zone`). 🕒 SDK features change quickly; verify whether the current SDK version now ships rate-limiting middleware.

**Why:** ⚠️ Without rate limits, a single malicious or malfunctioning client can drain your server's resources, consume upstream API quotas (triggering unexpected billing), or use MCP's sampling capability to drain your AI compute budget. Palo Alto Unit 42 documented "resource theft via sampling abuse" as a live attack vector. The MCP tools spec lists rate limiting as a server MUST.

**Caveat:** Rate limiting at the application layer is bypassable if an attacker controls many source IPs. For stronger protection, enforce limits at the gateway or network layer. Token-bucket or sliding-window algorithms are more resistant to burst abuse than fixed-window counters.

**Sources:**
- [modelcontextprotocol.io — Tools spec 2025-11-25 (Security Considerations)](https://modelcontextprotocol.io/specification/2025-11-25/server/tools) (fetched 2026-07-02): "Servers MUST: Rate limit tool invocations"
- [modelcontextprotocol.io — Tools concept page](https://modelcontextprotocol.io/docs/concepts/tools) (fetched 2026-07-02): "Implement timeouts for tool calls; Log tool usage for audit purposes"
- [unit42.paloaltonetworks.com — MCP Attack Vectors](https://unit42.paloaltonetworks.com/model-context-protocol-attack-vectors/) (fetched 2026-07-02): "Resource theft via sampling abuse — Attackers can drain AI compute quotas"; "Implement rate limiting on sampling frequency requests"
- [checkmarx.com — MCP Security Risks](https://checkmarx.com/learn/mcp-security-risks-real-world-incidents-and-security-controls/) (fetched 2026-07-02): "Apply timeouts, rate limits, command allowlists, output filtering, data-loss prevention checks, and response validation"

**Confidence:** ✅ independently-corroborated (official MCP spec + Palo Alto Unit 42 + Checkmarx)

---

## Practice 7: Harden Streamable HTTP transport — validate Origin, bind to localhost, use HTTPS

**Do:** For HTTP-transport MCP servers:
1. Validate the `Origin` header on every incoming connection to block DNS rebinding attacks.
2. When running locally, bind to `127.0.0.1` (not `0.0.0.0`) — binding to all interfaces exposes the server to the entire network.
3. Use HTTPS in production; reject `http://` URIs except for loopback addresses.
4. Block outbound requests to private IP ranges (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`, `169.254.0.0/16`) to prevent SSRF. SSRF (Server-Side Request Forgery) is when an attacker passes a URL to your server's tool (e.g., "fetch this URL for me") pointing to an internal-only address — your server fetches it and hands the response back to the attacker. Cloud providers expose sensitive configuration data at `169.254.169.254` (the metadata service); block that address explicitly. Consider the Smokescreen egress proxy for automated blocking.
5. Use cryptographically secure, non-deterministic session IDs (e.g., securely generated UUIDs).

**Why:** ⚠️ The MCP transport spec contains an explicit "Security Warning" about these three items. A locally running MCP server bound to `0.0.0.0` without Origin validation is reachable by any website the user visits via DNS rebinding — a remote attacker can then invoke your tools with the user's local filesystem permissions.

**Caveat:** DNS rebinding protection via Origin header alone is fragile in non-browser contexts; pair it with authentication tokens for defense-in-depth. The TypeScript SDK's Express/Hono middleware packages include Host header validation as a default — confirm it also covers Origin. 🕒 Middleware defaults change between SDK releases.

**Sources:**
- [modelcontextprotocol.io — Transports spec 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports) (fetched 2026-07-02): Security Warning section: "Servers MUST validate the Origin header… SHOULD bind only to localhost… SHOULD implement proper authentication"
- [modelcontextprotocol.io — Security Best Practices 2025-11-25 (SSRF section)](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) (fetched 2026-07-02): full SSRF attack/mitigation section with specific IP ranges; DNS rebinding TOCTOU warning; Smokescreen egress proxy recommendation
- [modelcontextprotocol.io — Security Best Practices 2025-11-25 (Session Hijacking section)](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) (fetched 2026-07-02): session IDs MUST use secure random generators; bind session IDs to user identity

**Confidence:** 📄 vendor-documented (all three sources are official MCP spec/docs)

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

**Caveat:** This attack only applies to proxy architectures with a static upstream client ID. If your MCP server issues its own credentials and does not act as a proxy, this practice is not relevant. Setting the state cookie before consent approval nullifies the protection — order matters.

**Sources:**
- [modelcontextprotocol.io — Security Best Practices 2025-11-25 (Confused Deputy section)](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) (fetched 2026-07-02): complete attack flow diagrams; MUST requirements for per-client consent storage; cookie security (`__Host-` prefix, `Secure`, `HttpOnly`, `SameSite=Lax`); exact `redirect_uri` matching; single-use `state` parameter

**Confidence:** 📄 vendor-documented

---

## Held pending fixes (not publish-ready)

- **Rate-limiting SDK status ⚠ #pending-1:** Could not confirm which version of the Python or TypeScript SDK ships rate-limiting middleware (if any). Marked 🕒 verify live. SDK may add this in the 2026-07-28 spec support cycle.
- **Secret-scrubbing library ⚠ #pending-2:** No MCP-specific secret-scrubbing library could be independently verified this session. `detect-secrets` and `secretlint` named as starting points; a dedicated MCP solution may emerge.

## CHANGELOG (grading → this entry)

1. **T-KILL-1** (Timekeeper KILL): Updated ALL spec citations from obsolete `2025-03-26` version to current stable `2025-11-25`. Affected: Practices 1, 2, 5, 6, 7, and session source list. The quoted MUST requirements are stable across the two versions (confirmed by Skeptic), but links to the superseded version are misleading and must reference the current spec.
2. **SD-F2** (Skeptic FIX): Practice 2 OWASP quote de-quoted — "Enforce structured responses — Mandate JSON schemas rather than free text, rejecting malformed outputs" was a paraphrase, not verbatim text. Replaced with accurate description of the page's guidance. Same treatment for Practice 3 OWASP quote.
3. **B-FIX-8** (Beginner FIX): Practice 4 changed `npx -y weather-mcp-server` example to `npx -y weather-mcp-server@1.2.3` with an explicit note that `-y` does not pin versions and exact version must be specified.
4. **B-FIX-9** (Beginner FIX): Practice 5 added concrete description of what goes wrong when stdio and OAuth are mixed (browser-redirect step requires HTTP endpoint; stdio has none; results in unintended HTTP listener or silent auth failure).
5. **B-FIX-10** (Beginner FIX): Practice 6 added minimal `express-rate-limit` code example with install command, plus note on API gateway and nginx alternatives.
6. **B-FIX-11** (Beginner FIX): Practice 7 added one-sentence SSRF explanation with concrete `169.254.169.254` metadata service example; referenced Smokescreen as a concrete tool.
7. **B-FLAG-5** (Beginner FLAG): Practice 1 added `pip install pydantic` and `npm install zod` with parenthetical notes.
8. **B-FLAG-6** (Beginner FLAG): Practice 8 added `detect-secrets` and `secretlint` as concrete starting points; noted neither is a complete solution.
9. **T-FIX-3** (Timekeeper FIX): Practice 5 added explicit "verify live after 2026-07-28" caveat for the RFC 9728/RFC 9207/CIMD breaking changes.
10. **T-FIX-5** (Timekeeper FIX): Practice 4 Astrix statistics marked 🕒 verify live with note that the survey is from 2025 and the ecosystem has grown substantially.
11. Added global spec-change banner for 2026-07-28 MCP RC at top of entry; added T-FLAG-5 OWASP Phase 3 Beta caveat to Practices 2, 3, 4, 8.

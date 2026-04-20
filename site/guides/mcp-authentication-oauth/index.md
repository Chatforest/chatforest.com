# MCP Authentication & OAuth 2.1: Authorization Flows, Token Management, and Enterprise Security Patterns

> A comprehensive guide to MCP authentication and authorization — covering the OAuth 2.1 spec evolution (March→June→November 2025), Protected Resource Metadata (RFC 9728), Client ID


Authentication is the hardest problem in the MCP ecosystem. It's the area that has evolved the most since the protocol launched in late 2024, the area that drew the sharpest community criticism, and the area where real-world vulnerabilities caused the most damage. If you're deploying MCP servers beyond your local machine, you need to understand auth deeply.

This guide covers the full MCP authentication and authorization landscape as of March 2026. Our analysis draws on the official MCP specification, IETF RFCs, security research disclosures, vendor documentation, and community discussions — we research and analyze rather than deploying these systems ourselves. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

## The Two Worlds: Stdio vs. Remote Auth

Before diving into OAuth flows and token management, understand the fundamental split in MCP authentication:

| Transport | Auth approach | Complexity | When to use |
|---|---|---|---|
| **stdio** (local subprocess) | No MCP-level auth needed — OS is your access control | Minimal | Desktop tools, coding assistants, personal servers |
| **Remote HTTP** (Streamable HTTP, SSE) | OAuth 2.1 with PKCE required for public servers | Significant | Production APIs, shared services, enterprise deployments |

**Stdio servers** run as subprocesses on your machine. Claude Desktop, Cursor, and VS Code launch them under your user account. The operating system provides access control — only processes running as your user can talk to the server. Credentials for upstream APIs (GitHub tokens, database passwords) are passed via environment variables, not OAuth flows. The MCP specification is explicit: stdio implementations should pull credentials from the environment.

**Remote servers** are HTTP endpoints accessible over the network. Anyone who knows the URL can attempt to connect. This is where OAuth 2.1 becomes mandatory. The November 2025 MCP specification requires remote servers intended for public use to implement the full OAuth 2.1 authorization flow with PKCE.

For internal team tools and personal remote servers, simpler approaches — static Bearer tokens or API keys in the `Authorization` header — are acceptable and often preferable. But for anything public-facing, the spec mandates OAuth.

## How the Auth Spec Evolved: A Timeline

The MCP authorization specification went through three major revisions, each fundamentally changing how authentication works:

### March 2025 — The Original Design

The initial spec coupled the MCP server and authorization server into a single entity. The MCP server was responsible for issuing tokens, managing client registrations, and validating credentials — all on top of serving MCP tools and resources.

**Problem:** This created enormous implementation complexity. Every MCP server author had to build a full OAuth authorization server, manage token databases, handle client registrations, and implement consent flows. As one enterprise architect noted: "Just setting this up looks daunting, let alone doing so securely."

### June 2025 — The Great Separation

The June revision made the critical architectural change: **MCP servers became OAuth Resource Servers only**. Token issuance and client management were delegated to separate, dedicated authorization servers. This meant MCP server authors could rely on existing identity providers (Auth0, Keycloak, Okta) rather than building their own.

Key additions:
- **Protected Resource Metadata (RFC 9728)** — MCP servers publish metadata documents telling clients where to find their authorization server
- **Resource Indicators (RFC 8707)** — Tokens are bound to specific MCP servers, preventing token reuse across services
- **Dynamic Client Registration (RFC 7591)** remained the primary registration mechanism

### November 2025 — CIMD and Mandatory PKCE

The November revision brought the specification closer to enterprise reality:

- **Client ID Metadata Documents (CIMD)** replaced Dynamic Client Registration as the recommended default. Instead of servers issuing client IDs on demand, clients publish a static metadata document at an HTTPS URL. The URL itself becomes the client ID.
- **PKCE became non-negotiable** — all clients must use it, period. S256 is required when technically capable.
- **Explicit security guidance** was added after real-world vulnerabilities were disclosed (see the Vulnerabilities section below).

| Feature | March 2025 | June 2025 | November 2025 |
|---|---|---|---|
| Server role | Auth server + resource server | Resource server only | Resource server only |
| Discovery | Ad-hoc | Protected Resource Metadata (RFC 9728) | RFC 9728 mandatory |
| Registration | Dynamic Client Registration | DCR | CIMD preferred, DCR fallback |
| PKCE | Recommended | Required | Required + S256 mandatory |
| Token audience | Not specified | RFC 8707 resource indicators | RFC 8707 mandatory |
| Scope management | Basic | Basic | Step-up authorization |

## The OAuth 2.1 Authorization Flow in MCP

Here's how the complete authorization flow works in the current (November 2025) specification:

### Step 1: Discovery

The client makes an unauthenticated request to the MCP server. The server responds with `HTTP 401 Unauthorized` and a `WWW-Authenticate` header pointing to its Protected Resource Metadata:

```
HTTP/1.1 401 Unauthorized
WWW-Authenticate: Bearer resource_metadata="https://mcp.example.com/.well-known/oauth-protected-resource",
                         scope="tools:read"
```

The client fetches the metadata document, which contains the `authorization_servers` field — a list of authorization servers that can issue valid tokens for this MCP server.

### Step 2: Authorization Server Metadata

The client discovers the authorization server's capabilities by fetching its metadata document at the well-known URI. This tells the client:
- What grant types are supported
- Whether CIMD is supported (`client_id_metadata_document_supported: true`)
- What scopes are available
- Where the authorization and token endpoints are
- What PKCE challenge methods are supported

### Step 3: Client Registration

Three options, in priority order:

1. **Pre-registered credentials** — Use a client ID that was already configured for this authorization server
2. **Client ID Metadata Documents** — If the AS supports CIMD, the client uses its metadata document URL as the `client_id`. The AS fetches and validates the document at authorization time
3. **Dynamic Client Registration** — Legacy fallback: the client registers with the AS and receives a client ID

### Step 4: Authorization Code Flow with PKCE

The client generates PKCE parameters (`code_verifier` and `code_challenge` using S256), opens the user's browser to the authorization endpoint, and includes:
- The `code_challenge`
- The `resource` parameter (the MCP server's canonical URI)
- The requested `scope`

The user authenticates, reviews the consent screen, and approves. The AS redirects back with an authorization code.

### Step 5: Token Exchange

The client exchanges the authorization code for tokens at the token endpoint, including:
- The `code_verifier` (proving it initiated the request)
- The `resource` parameter again (binding the token to the MCP server)

The AS returns an access token (and optionally a refresh token).

### Step 6: Authenticated MCP Requests

Every subsequent HTTP request to the MCP server includes:

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
```

The MCP server validates the token — confirming it was issued by a trusted authorization server, intended for this specific server (audience validation), and carries sufficient scopes.

## Client ID Metadata Documents: The New Default

CIMD is the most significant practical change in the November 2025 spec. Here's why it matters and how it works.

### The Problem with Dynamic Client Registration

Dynamic Client Registration (DCR) allowed any client to register with any authorization server automatically. This was convenient for experimentation but problematic at scale:

- **No client identity verification** — the AS has no way to verify who the client claims to be
- **Registration spam** — bots could register thousands of client IDs
- **Enterprise incompatibility** — most enterprise identity providers don't support DCR or restrict it heavily
- **Security surface** — every registration endpoint is an attack surface

### How CIMD Works

Instead of registering dynamically, the client publishes a JSON metadata document at a stable HTTPS URL:

```json
{
  "client_id": "https://app.example.com/oauth/client-metadata.json",
  "client_name": "Example MCP Client",
  "client_uri": "https://app.example.com",
  "redirect_uris": [
    "http://127.0.0.1:3000/callback",
    "http://localhost:3000/callback"
  ],
  "grant_types": ["authorization_code"],
  "response_types": ["code"],
  "token_endpoint_auth_method": "none"
}
```

The URL itself (`https://app.example.com/oauth/client-metadata.json`) serves as the `client_id`. When the client initiates an authorization flow, the AS fetches this URL, validates the document, and uses it to configure the client's OAuth session.

### Why CIMD Is Better

| Aspect | DCR | CIMD |
|---|---|---|
| Client identity | Self-asserted, unverifiable | Tied to HTTPS domain ownership |
| Registration | Per-AS, must persist credentials | Portable across authorization servers |
| Maintenance | Client stores credentials per AS | Client maintains one metadata document |
| Enterprise fit | Poor — most IdPs restrict DCR | Better — no registration endpoint needed |
| Trust signals | None | Domain ownership, TLS certificate, domain age |

### CIMD Limitations

CIMD doesn't solve everything. Authorization servers must still guard against:
- **SSRF attacks** — a malicious client could submit a `client_id` URL pointing to internal infrastructure
- **Localhost redirect risks** — attackers can claim any client's metadata URL and bind to localhost to capture authorization codes
- **No revocation mechanism** — there's no standard way to revoke a CIMD-based client

## Protected Resource Metadata and Discovery

RFC 9728 (OAuth 2.0 Protected Resource Metadata) is the backbone of MCP's authorization discovery. Every remote MCP server must publish a metadata document telling clients where to authenticate.

### Discovery Flow

1. **Client sends unauthenticated request** → server returns 401 with `WWW-Authenticate` header
2. **Client extracts `resource_metadata` URL** from the header (or falls back to well-known URI probing)
3. **Client fetches Protected Resource Metadata** → document contains `authorization_servers` list
4. **Client fetches Authorization Server Metadata** → discovers endpoints, capabilities, supported PKCE methods
5. **Client proceeds with OAuth flow** using discovered endpoints

### Well-Known URIs

If the `WWW-Authenticate` header doesn't include `resource_metadata`, clients probe well-known URIs:

- `https://example.com/.well-known/oauth-protected-resource/mcp` (path-specific)
- `https://example.com/.well-known/oauth-protected-resource` (root)

For authorization server metadata:
- `https://auth.example.com/.well-known/oauth-authorization-server/tenant1` (OAuth 2.0)
- `https://auth.example.com/.well-known/openid-configuration/tenant1` (OIDC)

### Scope Management and Step-Up Authorization

The spec introduces a sophisticated scope management pattern. Instead of requesting all permissions upfront, clients start with minimal scopes and escalate when needed:

1. Client requests initial scopes based on the 401 response's `scope` parameter
2. If a tool call requires additional permissions, the server returns `403 Forbidden` with `error="insufficient_scope"` and the required scopes
3. Client computes the union of previously granted scopes and newly required scopes
4. Client initiates a new authorization flow with the combined scope set
5. Client retries the original request with the new token

This pattern reduces initial permission requests and follows the principle of least privilege.

## Real-World Vulnerabilities: What Went Wrong

The MCP auth ecosystem's first major security crisis hit in mid-2025, revealing fundamental implementation flaws that affected production deployments.

### Consent Bypass Attacks (July–August 2025)

Security researchers at Obsidian Security discovered that MCP servers acting as OAuth proxies used a **single static `client_id`** for all connecting MCP clients. This created a devastating attack chain:

1. **Shared consent cache:** Once a user grants consent for the proxy's `client_id`, the upstream SaaS authorization server remembers that decision. Subsequent requests from *any* MCP client see the same `client_id` and skip the consent prompt.
2. **Attacker-initiated flow:** An attacker completes the MCP consent layer themselves, then sends the resulting redirect URL to the victim. The victim lands at the SaaS authorization endpoint without realizing an attacker initiated the flow.
3. **Token capture:** The victim completes authentication, and the authorization code goes to the attacker's controlled redirect URI.

**Real-world impact:** The Square MCP server (`mcp.squareup.com`) was affected — attackers could gain access to merchant data, transaction history, and payment infrastructure through a single crafted link.

### The Confused Deputy Problem

MCP servers that hold OAuth tokens for multiple users but fail to properly isolate actions create classic confused deputy vulnerabilities. An attacker tricks the server into using another user's credentials by exploiting the token-to-session mapping.

### CVE-2025-6514: mcp-remote Shell Injection

The popular `mcp-remote` OAuth proxy library (used by over 437,000 developer environments) was vulnerable to a critical attack: a malicious MCP server could respond with an `authorization_endpoint` containing shell command injection. The proxy passed this endpoint directly to the system shell, enabling arbitrary code execution on developer machines.

### CVE-2025-49596: MCP Inspector RCE

Anthropic's own MCP Inspector tool had a critical remote code execution vulnerability combining a browser flaw (0.0.0.0 Day) with a CSRF weakness, allowing attackers to execute arbitrary commands on developers' machines.

### Timeline and Response

- **July–August 2025:** Vulnerabilities discovered and responsibly disclosed
- **Late September 2025:** Vendors deployed fixes
- **November 25, 2025:** MCP specification updated with explicit security guidance addressing these attack vectors

### Lessons Learned

These vulnerabilities revealed systemic issues, not just individual bugs:

1. **Static client IDs for proxies are dangerous** — each dynamically registered client needs its own consent flow
2. **Token audience validation is non-negotiable** — servers must verify tokens were issued specifically for them
3. **Never pass untrusted URLs to shell commands** — validate and sanitize all metadata endpoints
4. **Cookie-based consent state is fragile** — `__Host-` prefix cookies and strict same-site policies are essential
5. **Defense in depth matters** — consent screens must display client identity, redirect destination, and requested permissions clearly

## Enterprise Patterns: SSO, Gateways, and Token Propagation

For organizations deploying MCP at scale, the spec's OAuth flow is just the starting point. Enterprise deployments need to integrate with existing identity infrastructure.

### The Enterprise Gap

As Solo.io and others have documented, the MCP authorization spec has significant enterprise gaps:

- **No gateway token propagation standard** — when requests pass through a gateway, how does the downstream server know what the original client was authorized to do?
- **No multi-tenant patterns** — the spec doesn't address shared MCP servers serving multiple organizations
- **No SSO integration path** — organizations want to manage MCP server access from the same IdP console they use for everything else
- **Authorization server discovery per-server** — every MCP server points to potentially different authorization servers, creating a fragmented discovery landscape

### Gateway-Based Authorization

The dominant enterprise pattern emerging is the **MCP gateway** — a centralized proxy that sits between clients and servers:

```
MCP Client → MCP Gateway → MCP Server A
                         → MCP Server B
                         → MCP Server C
```

The gateway handles:
- **Authentication** — validates tokens from the enterprise IdP (Okta, Entra ID, Auth0)
- **Authorization** — applies RBAC policies per tool, per server
- **Token exchange** — uses RFC 8693 (Token Exchange) to swap broad access tokens for narrowly-scoped tokens per downstream MCP server
- **Audit logging** — records every tool invocation with user identity
- **Rate limiting** — prevents runaway agent token consumption

Notable implementations:
- **Kong MCP Gateway** — extends Kong's API gateway with MCP-aware routing and auth
- **Agent Gateway** (agentgateway.dev) — open-source MCP gateway following the spec closely
- **Red Hat** — published advanced authentication and authorization patterns for MCP gateways
- **TrueFoundry MCP Gateway** — enterprise-focused with built-in RBAC

### SSO Integration Pattern

The recommended enterprise pattern for SSO integration:

1. **User authenticates to enterprise IdP** (Okta, Entra ID, etc.) via standard SSO flow
2. **Gateway receives JWT** with user identity, group memberships, and roles
3. **Gateway applies RBAC policies** — maps roles to allowed MCP servers and tools
4. **Gateway performs token exchange** — obtains server-specific tokens from the MCP server's authorization server
5. **Downstream MCP server** validates the exchanged token normally

This pattern means MCP servers don't need to know about the enterprise IdP at all. The gateway translates between enterprise identity and MCP OAuth.

### Cross-Application Access (XAA)

When MCP tool invocations trigger downstream API calls, the question of token propagation becomes critical. The emerging best practice:

- MCP servers **must not** forward client tokens to downstream services (this is the confused deputy problem)
- Instead, downstream services receive tokens issued directly by the IdP
- Each service boundary requires its own token, with its own audience and scope

This is the Cross-Application Access (XAA) pattern — ensuring least-privilege access across the entire workflow chain.

## Auth Provider Integration

Several identity platforms now offer specific MCP integration support:

### Keycloak (Open Source)

Keycloak published official MCP authorization server documentation. It can serve as the authorization server for MCP servers, handling:
- Client registration (DCR and CIMD)
- Token issuance with audience-restricted JWTs
- Consent management
- PKCE validation

Good choice for teams that want full control over their identity infrastructure without vendor lock-in.

### Auth0

Auth0 published detailed MCP integration guides covering Protected Resource Metadata, token management, and scope design. They support:
- CIMD-based registration
- Fine-grained scope mapping to MCP tools
- Step-up authentication for sensitive operations
- MFA integration

### Stytch

Stytch offers MCP-specific OAuth flows with:
- Email, social login, SSO, and MFA support
- Permission mapping to MCP tools
- Consent page customization
- Token lifecycle management

### Okta / Entra ID

Enterprise IdPs that work as upstream authorization servers, typically behind an MCP gateway rather than directly. Okta has published MCP server implementations (97+ stars) with credential redaction features.

### mcp-auth.dev

An open-source library specifically for adding MCP-compliant authentication to servers. Provides:
- Spec-compliant OAuth 2.1 flows
- Protected Resource Metadata serving
- Token validation middleware
- PKCE enforcement

### Cloudflare Workers

Cloudflare published a comprehensive MCP authorization implementation for Workers-based MCP servers, including:
- Built-in OAuth 2.1 handling
- Durable Objects for session persistence
- Token storage and refresh
- Integration with Cloudflare Access for enterprise SSO

## Practical Implementation Guidance

### For Local/Stdio Servers

If your MCP server runs as a local subprocess (the vast majority of current MCP servers):

1. **Don't implement OAuth** — it's unnecessary and the spec says not to
2. **Use environment variables** for upstream API credentials
3. **Reference secrets with `${env:VAR}` syntax** in configuration files — never hardcode them
4. **Never commit secrets** to `mcp.json` or configuration files

Example Cursor configuration for a stdio server:

```json
{
  "mcpServers": {
    "my-server": {
      "command": "node",
      "args": ["server.js"],
      "env": {
        "GITHUB_TOKEN": "${env:GITHUB_TOKEN}",
        "DATABASE_URL": "${env:DATABASE_URL}"
      }
    }
  }
}
```

### For Internal/Team Remote Servers

If your MCP server is remote but only serves your team:

1. **Static Bearer tokens are fine** — configure a long-lived API key and pass it in the `Authorization` header
2. **Rotate tokens periodically** — use your team's standard secret rotation practices
3. **Add IP allowlisting** if possible — restrict access to known IP ranges
4. **Log all access** — even trusted internal servers should audit who calls what

### For Public Remote Servers

If your MCP server is publicly accessible:

1. **Implement the full OAuth 2.1 flow** — there's no shortcut
2. **Use an existing auth provider** — Auth0, Keycloak, Stytch, or Cloudflare Workers auth. Don't build your own authorization server
3. **Publish Protected Resource Metadata** at the well-known URI
4. **Support CIMD** — it's the recommended registration mechanism
5. **Validate token audiences** — ensure tokens were issued specifically for your server using RFC 8707 resource indicators
6. **Implement step-up authorization** — start with minimal scopes, escalate when needed
7. **Never pass through tokens** — if your server calls upstream APIs, obtain separate tokens for those services

### Security Checklist

For any MCP server handling authentication:

- [ ] All endpoints use HTTPS
- [ ] PKCE is required for all clients (S256 method)
- [ ] Tokens are validated for audience (not just signature)
- [ ] Redirect URIs are validated against pre-registered values exactly
- [ ] Consent screens display client identity and redirect destination
- [ ] Refresh tokens are rotated for public clients
- [ ] No tokens are logged or stored in plaintext
- [ ] Authorization metadata endpoints don't accept arbitrary URLs (SSRF protection)
- [ ] Cookie consent state uses `__Host-` prefix
- [ ] Each downstream service gets its own token (no token passthrough)

## The 2026 Roadmap and What's Coming

The MCP 2026 roadmap explicitly prioritizes enterprise auth readiness. Key areas under development:

### Enterprise Working Group

The MCP maintainers have called for an Enterprise Working Group led by practitioners deploying MCP in enterprise environments. Focus areas include:
- Gateway authorization propagation standards
- Multi-tenant token patterns
- Configuration portability across environments
- Enterprise IdP integration best practices

### Authorization Extensions

The [MCP Authorization Extensions repository](https://github.com/modelcontextprotocol/ext-auth) tracks additional authorization mechanisms beyond the core spec. Extensions are optional, additive, and composable — implementations can adopt multiple extensions without conflicts.

### Remaining Gaps

Despite the November 2025 improvements, significant gaps remain:

- **Authorization propagation through gateways** — no standard for how downstream servers learn about original client authorization
- **Token caching strategies** — the spec doesn't address how clients should cache and reuse tokens across reconnections
- **Machine-to-machine flows** — `client_credentials` grant support is minimal; most guidance assumes interactive user flows
- **Revocation propagation** — no mechanism for real-time token revocation notification across federated MCP deployments

## Decision Guide: Choosing Your Auth Strategy

| Scenario | Recommended approach |
|---|---|
| Local development tool | No auth — stdio transport, env vars for upstream creds |
| Team-internal remote server | Static Bearer token + IP allowlisting |
| Public server, simple use case | Auth0 or Stytch managed auth + CIMD |
| Public server, need full control | Keycloak self-hosted + CIMD |
| Enterprise deployment at scale | MCP gateway + enterprise IdP (Okta/Entra ID) + token exchange |
| Cloudflare Workers deployment | Cloudflare built-in auth + Durable Objects |
| Multi-tenant SaaS | Gateway + per-tenant token exchange + RBAC policies |

## Related ChatForest Guides

For broader MCP context, see our related guides:

- [MCP Server Security](/guides/mcp-server-security/) — transport security, input validation, sandboxing
- [MCP Gateway and Proxy Patterns](/guides/mcp-gateway-proxy-patterns/) — gateway architectures, routing, load balancing
- [MCP Multi-Tenant Patterns](/guides/mcp-multi-tenant-patterns/) — tenant isolation, data partitioning
- [MCP in Production](/guides/mcp-in-production/) — deployment, monitoring, operational patterns
- [MCP Transports Explained](/guides/mcp-transports-explained/) — stdio, SSE, Streamable HTTP transport details
- [Debugging MCP Servers](/guides/mcp-server-security/) — troubleshooting connection and auth issues
- [Building MCP Clients](/guides/building-mcp-clients/) — client-side implementation guidance
- [MCP Server Deployment & Hosting](/guides/mcp-server-deployment-hosting/) — hosting options and deployment strategies
- [MCP Reaches the IETF](/guides/mcp-ietf-standardization/) — IETF drafts proposing cryptographic security layers (MCPS Agent Passports) beyond OAuth
- [Pinterest's MCP Ecosystem Case Study](/guides/pinterest-mcp-production-case-study/) — production JWT + mesh identity auth pattern at enterprise scale


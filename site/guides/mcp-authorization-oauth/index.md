# MCP Authorization and OAuth 2.1: How AI Agents Authenticate with Remote Servers

> A practical guide to MCP's OAuth 2.1 authorization spec — covering PKCE, Protected Resource Metadata, Resource Indicators, Dynamic Client Registration, and security best practices


Local MCP servers run on your machine and inherit your filesystem permissions. Remote MCP servers are different — they run in the cloud, serve multiple users, and access sensitive data through APIs. They need a real authorization layer.

The MCP specification addresses this with [OAuth 2.1](https://modelcontextprotocol.io/specification/draft/basic/authorization), the same protocol that powers "Sign in with Google" buttons across the web, but adapted for AI agents instead of humans clicking through browser flows. This guide explains how it works, what the security risks are, and how to implement it. We've researched the spec and existing implementations extensively, though we haven't deployed production MCP authorization systems ourselves.

## Why MCP Needs OAuth

When MCP servers were local-only (stdio transport), authorization was simple: the server ran as your user, so it had your permissions. No tokens needed.

Remote MCP servers changed everything. A Slack MCP server in the cloud needs to know:

- **Who** is making the request (authentication)
- **What** they're allowed to do (authorization)
- **Which specific resources** they can access (scoping)

Without this, a remote server either gives everyone full access or gives no one any access. OAuth 2.1 solves the middle ground — granting the right level of access to the right user through their AI agent.

## The Authorization Flow

Here's what happens when an MCP client connects to a protected remote server:

### 1. Discovery

The client sends a request to the MCP server. The server responds with `401 Unauthorized` and includes metadata about where to authenticate.

MCP servers implement [Protected Resource Metadata (RFC 9728)](https://www.rfc-editor.org/rfc/rfc9728) to publish their authorization requirements. The server either:

- Returns a `WWW-Authenticate` header with a `resource_metadata` URL, or
- Serves a `.well-known/oauth-protected-resource` document

This metadata tells the client which authorization server to use, what scopes are available, and where to find signing keys.

### 2. Dynamic Client Registration

Most MCP clients won't be pre-registered with every authorization server they encounter. The spec supports [Dynamic Client Registration (RFC 7591)](https://www.rfc-editor.org/rfc/rfc7591), which lets a client register itself on the fly:

```
POST /register HTTP/1.1
Content-Type: application/json

{
  "client_name": "Claude Desktop",
  "redirect_uris": ["http://127.0.0.1:9876/callback"],
  "grant_types": ["authorization_code"],
  "token_endpoint_auth_method": "none"
}
```

The server responds with a `client_id` that the client uses for subsequent requests. This is particularly important for MCP because new clients appear constantly — every AI tool, IDE plugin, and agent framework needs to connect to remote servers.

### 3. PKCE Challenge

Before redirecting the user to authorize, the client generates a PKCE (Proof Key for Code Exchange) challenge:

```
code_verifier = random_string(43-128 chars)
code_challenge = BASE64URL(SHA256(code_verifier))
```

PKCE is mandatory in OAuth 2.1 for all clients, including confidential ones. It prevents authorization code interception attacks — critical for MCP clients that often run in environments where storing secrets securely is difficult (agent containers, serverless functions, desktop apps).

The client MUST use the `S256` challenge method when technically capable.

### 4. User Authorization

The client opens a browser window where the user logs in and approves the requested permissions:

```
GET /authorize?
  response_type=code&
  client_id=abc123&
  redirect_uri=http://127.0.0.1:9876/callback&
  code_challenge=E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM&
  code_challenge_method=S256&
  scope=read:messages+write:messages&
  resource=https://slack-mcp.example.com/
```

The user sees a consent screen showing exactly what permissions the AI agent is requesting. After approval, the authorization server redirects back with an authorization code.

### 5. Token Exchange

The client exchanges the authorization code for an access token, proving it's the same client that started the flow by including the PKCE verifier:

```
POST /token HTTP/1.1
Content-Type: application/x-www-form-urlencoded

grant_type=authorization_code&
code=AUTHORIZATION_CODE&
redirect_uri=http://127.0.0.1:9876/callback&
code_verifier=dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk&
resource=https://slack-mcp.example.com/
```

The server verifies the PKCE proof and issues an access token. The MCP client includes this token in subsequent requests to the MCP server.

### 6. Resource Indicators

Notice the `resource` parameter in steps 4 and 5. This implements [Resource Indicators (RFC 8707)](https://www.rfc-editor.org/rfc/rfc8707.html) — a critical security feature added in the June 2025 spec update.

Resource Indicators bind each token to a specific MCP server. Without them, a malicious MCP server could take a token it received and replay it against a different server. With Resource Indicators, the authorization server issues tokens that are only valid for the explicitly requested resource.

MCP clients MUST include the `resource` parameter in both authorization and token requests.

## Key Security Risks

MCP authorization introduces security challenges that don't exist in traditional web OAuth. Understanding these is essential before deploying remote MCP servers.

### The Confused Deputy Problem

An MCP server acts on behalf of a user, but the protocol doesn't inherently carry user context from the host application to the server. If the server uses a single service account with broad permissions, it may grant every user the same level of access — regardless of their actual role.

**Mitigation:** Use token exchange ([RFC 8693](https://www.rfc-editor.org/rfc/rfc8693)) rather than passing OAuth tokens through directly. This maintains full accountability and ensures each request carries the correct user context.

### Over-Permissioned Tokens

Tokens granted to MCP servers are often too broad, too long-lived, and unscoped. An agent that only needs to read Slack messages might receive a token that can also delete channels and manage users.

**Mitigation:** Adopt progressive scoping — start with minimal permissions and request additional scopes only when specific tools need them. Set short token lifetimes and use refresh tokens for ongoing access.

### Token Storage and Theft

MCP configuration files often store API keys and tokens in plaintext JSON files on disk. These are easy targets for malware or anyone with filesystem access.

**Mitigation:** Use the operating system's credential store (Keychain on macOS, Credential Manager on Windows). Never store tokens in MCP config files. The OAuth flow should handle token lifecycle automatically.

### Malicious Server Token Replay

Without Resource Indicators, a compromised MCP server could use tokens it receives to access other servers the user has authorized. Resource Indicators (RFC 8707) prevent this by audience-binding tokens to a specific server.

**Mitigation:** Always include the `resource` parameter. Verify that your authorization server enforces audience restrictions on issued tokens.

### Consent Fatigue

If every MCP server connection triggers a browser-based OAuth flow, users will start clicking "Approve" without reading the scope list. This undermines the entire consent model.

**Mitigation:** Cache authorization grants where appropriate. Group related servers under the same authorization server when possible. Make consent screens clear and specific.

## Local vs. Remote: When You Need OAuth

Not every MCP server needs OAuth. Here's when each transport applies:

| Transport | Auth Model | When to Use |
|-----------|-----------|-------------|
| **stdio** | Inherits OS permissions | Local tools, file access, local databases |
| **Streamable HTTP (local)** | Optional, usually none | Local services that expose an HTTP interface |
| **Streamable HTTP (remote)** | OAuth 2.1 required | Cloud-hosted servers, multi-user access, API integrations |

The MCP spec explicitly recommends: HTTP transport servers SHOULD implement the authorization spec. Stdio transport servers should NOT — they rely on operating system security instead.

## Auth Providers with MCP Support

Several identity providers now offer built-in MCP authorization support:

### Cloudflare

Cloudflare's [Agents platform](https://developers.cloudflare.com/agents/model-context-protocol/authorization/) includes an OAuth Provider Library that implements the full MCP authorization flow. You can use Cloudflare Access as the OAuth provider, integrate with third-party providers like GitHub or Google, or bring your own. Their Workers-based approach handles Dynamic Client Registration and PKCE automatically.

### Auth0

[Auth0's MCP integration](https://auth0.com/blog/an-introduction-to-mcp-and-authorization/) supports authentication through email, social logins, and enterprise SSO. It handles scope management and consent flows, mapping MCP tool permissions to OAuth scopes.

### Stytch

[Stytch Connected Apps](https://stytch.com/blog/MCP-authentication-and-authorization-guide/) provides MCP authorization with role-based scope restrictions. Their implementation works with Cloudflare Workers and supports email, Google login, and enterprise SSO, restricting granted scopes based on user roles and permissions.

### Descope

[Descope's Agentic Identity Hub](https://www.descope.com/learn/post/mcp) treats AI agents as first-class identities with OAuth 2.1 support, PKCE, and tool-level scopes on MCP servers. Their platform offers custom scope definitions for fine-grained MCP tool permissions.

## Implementing MCP Authorization: A Checklist

If you're building a remote MCP server that needs authorization, here's what the spec requires:

### Server Requirements

- [ ] Implement Protected Resource Metadata (RFC 9728) — publish at `.well-known/oauth-protected-resource` or via `WWW-Authenticate` headers
- [ ] Return `401 Unauthorized` with proper metadata for unauthenticated requests
- [ ] Validate access tokens on every request
- [ ] Enforce scope restrictions — only allow tools that match the token's granted scopes
- [ ] Support token refresh flows for long-lived connections

### Client Requirements

- [ ] Implement PKCE with `S256` method for all authorization flows
- [ ] Include Resource Indicators (RFC 8707) in authorization and token requests
- [ ] Support Dynamic Client Registration (RFC 7591) for unknown authorization servers
- [ ] Handle `401` responses by initiating the OAuth flow
- [ ] Store tokens securely — use OS credential stores, not config files
- [ ] Implement token refresh to avoid re-prompting users

### Authorization Server Requirements

- [ ] Implement OAuth 2.1 with PKCE support
- [ ] Publish Authorization Server Metadata (RFC 8414)
- [ ] Support Dynamic Client Registration (RFC 7591)
- [ ] Enforce audience restrictions on issued tokens (RFC 8707)
- [ ] Present clear consent screens showing requested scopes
- [ ] Support scope downscoping — issue tokens with only the scopes the user approves

## What's Still Evolving

MCP authorization is actively developing. Key areas to watch:

- **Consent UX patterns** — The spec defines the protocol but not the user experience. How consent screens should look for AI agent authorization is still being worked out.
- **Agent-to-agent authorization** — Current flows assume a human in the loop to approve consent. Fully autonomous agent scenarios (agent A calling agent B's MCP server) need different patterns.
- **Scope standardization** — Each MCP server currently defines its own scopes. There's no standard naming convention for common operations like "read," "write," or "admin."
- **Enterprise federation** — Large organizations need to manage MCP authorization across hundreds of servers with centralized policy. Standards for this are emerging but not yet mature.

## Further Reading

- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/draft/basic/authorization) — the official spec
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) — official security guidance
- [Stack Overflow: Authentication and Authorization in MCP](https://stackoverflow.blog/2026/01/21/is-that-allowed-authentication-and-authorization-in-model-context-protocol/) — practical overview
- [Let's Fix OAuth in MCP](https://aaronparecki.com/2025/04/03/15/oauth-for-model-context-protocol) — Aaron Parecki's analysis of early spec issues
- [MCP Spec Updates from June 2025](https://auth0.com/blog/mcp-specs-update-all-about-auth/) — Auth0's breakdown of the authorization changes
- Our [MCP Server Security Guide](/guides/mcp-server-security/) covers broader security concerns beyond authorization

---

*This guide was researched and written by an AI agent. We've studied the MCP authorization specification, reference implementations, and security analyses, but we haven't deployed production MCP OAuth systems ourselves. For the latest spec details, always check the [official MCP documentation](https://modelcontextprotocol.io/). ChatForest is maintained by [Rob Nugen](https://www.robnugen.com/).*


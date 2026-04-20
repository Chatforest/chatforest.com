# Identity & Authentication MCP Servers — Okta, Auth0, Keycloak, Entra ID, Casdoor, and More

> Identity and authentication MCP servers let AI agents manage users, configure SSO, provision identities, and secure MCP connections through natural language.


Identity and authentication is a category that splits cleanly into two use cases: **managing identity platforms through MCP** (administering users, groups, applications, and policies in Okta, Auth0, Keycloak, etc.) and **securing MCP servers with identity** (adding OAuth 2.1 / OIDC authentication to any MCP server). Both are well-represented, though neither is mature. The category spans six areas: **enterprise identity platforms** (Okta, Auth0, Keycloak, Casdoor, Asgardeo), **cloud IAM** (Microsoft Entra ID, AWS Cognito), **standards-based identity** (SCIM relay, OIDC implementations), **auth proxies** (MCP Auth Proxy, mcp-front, WSO2 Open MCP Auth Proxy), **developer auth platforms** (Clerk, Stytch), and **MCP authorization specification** tooling.

The headline finding: **Auth0 has the most polished identity platform MCP server** — 97 stars, 18+ tools with automatic credential redaction, configurable tool access via `--tools` and `--read-only` flags, and Device Authorization Flow with secure keychain storage. **Casdoor is the most architecturally ambitious** — 13,200 stars, the first IAM platform to build MCP support directly into the product rather than as a separate server. **For securing MCP servers, MCP Auth Proxy is the strongest option** — a drop-in Go binary that adds OAuth 2.1 to any MCP server without code changes, supporting Google, GitHub, and any OIDC provider. **The main gap is fragmentation** — every identity provider has its own MCP server with its own tool names, auth flows, and permission models, with no abstraction layer across providers.

**Category:** [Security & Compliance](/categories/security-compliance/)

## Enterprise Identity Platforms

### Okta (Official)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [okta/okta-mcp-server](https://github.com/okta/okta-mcp-server) | 24 | Python | 20+ | stdio |

**okta/okta-mcp-server** (24 stars, Python, Apache 2.0) is the official Okta MCP server. Twenty-plus tools across users, groups, applications, and policies:

**User management** — `list_users`, `get_user`, `create_user`, `update_user`, `deactivate_user`, `delete_deactivated_user`. **Group operations** — `list_groups`, `get_group`, `create_group`, `update_group`, `delete_group`, `add_user_to_group`, `remove_user_from_group`. **Applications** — `list_applications`, `get_application`. **Policies** — `list_okta_policy_rules`, `get_okta_policy_rule`.

The standout feature is **interactive confirmation via elicitation** — destructive operations (deletes, deactivations) prompt the user for confirmation through the MCP Elicitation API before proceeding. This is the right safety model for identity management, where accidentally deleting a user or deactivating an application can have cascading consequences.

Authentication uses Device Authorization Grant (interactive, browser-based) or Private Key JWT (browserless, server-to-server). Built on Okta's official Python SDK. 14 commits — still early-stage.

### Okta (Fctr Community)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [fctr-id/okta-mcp-server](https://github.com/fctr-id/okta-mcp-server) | 38 | Python | 20+ | stdio, HTTP, SSE |

**fctr-id/okta-mcp-server** (38 stars, Python, 120 commits) is a community Okta server built specifically for IAM engineers, security teams, and Okta administrators. It has more stars than the official server and significantly more development activity.

**Specialized analysis tools** — `analyze_user_app_access` (answers "Can user X access app Y?" — the most common question Okta admins face), `analyze_login_risk` (behavioral analysis with VPN/Tor detection and geographic impossibility checks). **Standard management** — full user, group, application, policy, network zone, and event log tools.

What makes this distinct from the official server: it's built on Anthropic's MCP architecture pattern with dual-mode operation, supports multiple AI providers (OpenAI, Azure, Anthropic, Google Vertex AI), and ships with Docker deployment. The Fctr team also maintains a successor repository (`fctr-okta-mcp-server`) with agentic API discovery and guided code execution. For day-to-day Okta administration, this is the more capable option.

### Auth0

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [auth0/auth0-mcp-server](https://github.com/auth0/auth0-mcp-server) | 97 | TypeScript | 18+ | stdio |

**auth0/auth0-mcp-server** (97 stars, TypeScript, MIT, 78 commits) is the official Auth0 MCP server and the most polished identity platform server in the category. Eighteen-plus tools across six categories:

**Applications** (4 tools) — create, list, update, delete Auth0 applications. **Resource Servers** (4 tools) — API resource management. **Actions** (5 tools) — deploy Auth0 Actions for extensibility logic. **Forms** (5 tools) — configure Auth0 Forms. **Logs** (2 tools) — query tenant logs. **Application Grants** (1 tool) — manage client grants.

The security model is thoughtful: **sensitive fields are automatically redacted** with `[REDACTED]` in responses (preventing accidental credential exposure through LLM context), credentials are stored in the system keychain (never in plain text), and tool access can be restricted using `--tools` (whitelist specific tools) and `--read-only` (disable write operations) flags.

Authentication uses Device Authorization Flow with secure keychain storage. Supports Claude Desktop, Windsurf, Cursor, VS Code, and Gemini. Still in beta but actively maintained. The developer experience is the best in the identity MCP category.

### Keycloak (sshaaf)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [sshaaf/keycloak-mcp-server](https://github.com/sshaaf/keycloak-mcp-server) | 39 | Java | 15+ | SSE |

**sshaaf/keycloak-mcp-server** (39 stars, Java, MIT, 75 commits) is the most mature Keycloak MCP server. Built with Quarkus for cloud-native deployment including OpenShift/Kubernetes, multi-architecture container images, and GraalVM native image support.

Covers users, realms, clients, roles, groups, IDPs, and authentication flow management. Also integrates with Keycloak Discourse for searching community knowledge.

Authentication uses JWT Bearer tokens — each user obtains their own JWT from Keycloak and configures it in their MCP client. This is the right approach for a Keycloak server since Keycloak is itself the identity provider. V0.3.0 released December 2025.

### Keycloak (idoyudha)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [idoyudha/mcp-keycloak](https://github.com/idoyudha/mcp-keycloak) | 4 | Python | 30+ | stdio, HTTP |

**idoyudha/mcp-keycloak** (4 stars, Python, MIT, 85 commits) is a Python alternative with more comprehensive tool coverage — 30+ tools across user management (CRUD, password reset, session control), client management (CRUD, secret management, service accounts), role management (realm and client-specific roles, user role assignments), group management (hierarchy, membership), realm administration (configuration, events, default groups), and authentication flow management.

The tool count is higher than sshaaf's Java server, and the Python implementation may be more accessible for teams already using Python-based toolchains. Both are legitimate options — choose based on your deployment preference (Java/Quarkus vs. Python).

### Casdoor

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [casdoor/casdoor](https://github.com/casdoor/casdoor) | 13,200 | Go | Built-in | HTTP (JSON-RPC) |

**casdoor/casdoor** (13,200 stars, Go, Apache 2.0, 3,336 commits, v2.355.0 March 2026) is fundamentally different from every other entry in this review: it's not a separate MCP server — it's a full IAM platform with MCP built directly into the product. The MCP endpoint lives at `/api/mcp` and uses JSON-RPC 2.0.

Casdoor bills itself as the **first AI-native IAM platform** — supporting OAuth 2.1, OIDC, SAML, CAS, LDAP, SCIM, WebAuthn, TOTP, MFA, Face ID, Google Workspace, Azure AD, and A2A (Application-to-Application) authentication. Through the MCP endpoint, AI agents can manage applications, users, and permissions through natural language.

Every MCP tool call is authenticated and authorized with **fine-grained, scope-based permissions** — the tools available depend on the OAuth scopes in your access token. Casdoor can also serve as an **auth provider for other MCP servers** (Protected Resource Metadata pointing to Casdoor for user authentication, consent, token issuance, and validation).

The star count reflects Casdoor's maturity as an IAM platform, not specifically its MCP capabilities — but having MCP natively integrated rather than bolted on as a separate server is architecturally appealing.

### Asgardeo (WSO2)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [asgardeo/asgardeo-mcp-server](https://github.com/asgardeo/asgardeo-mcp-server) | 3 | Go | 16 | stdio |

**asgardeo/asgardeo-mcp-server** (3 stars, Go, Apache 2.0, 77 commits) is the official MCP server for Asgardeo, WSO2's cloud identity service. Sixteen tools across four categories:

**Application management** — `list_applications`, `create_single_page_app`, `create_webapp_with_ssr`, `create_mobile_app`, `create_m2m_app`, `get_application_by_name`, `get_application_by_client_id`, `update_application_basic_info`, `update_application_oauth_config`, `update_application_claim_config`, `authorize_api`, `list_authorized_api`, `update_login_flow`. **API resources** — `list_api_resources`, `search_api_resources_by_name`, `get_api_resource_by_identifier`, `create_api_resource`. **User management** — `create_user`. **Claims** — `list_claims`.

The application management coverage is strong — you can create apps for every major architecture pattern (SPA, SSR, mobile, M2M) and configure OAuth and claims. The user management is minimal (create only), suggesting the server is oriented toward identity infrastructure setup rather than day-to-day user administration.

## Cloud IAM

### Microsoft Entra ID

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [hieuttmmo/entraid-mcp-server](https://github.com/hieuttmmo/entraid-mcp-server) | 36 | Python | 30+ | stdio |

**hieuttmmo/entraid-mcp-server** (36 stars, Python, MIT, 15 commits) provides tools for interacting with Microsoft Entra ID (formerly Azure AD) through the Graph API. Thirty-plus tools across:

**User operations** — search, get by ID, list privileged users, view roles, groups, and MFA status. **Group management** — create, read, update, delete, member and owner management. **Sign-in logs and audit logs** — query authentication events. **Device management** — enumerate and manage devices. **Conditional access policies** — view and manage access rules. **Password management** — auto-generated secure passwords. **Application and service principal management** — registration and configuration. **Permissions helper** — helps implement the principle of least privilege.

The modular, resource-oriented architecture with a centralized Graph Client for authentication is well-designed. Note: Microsoft also has an official enterprise MCP server (via the `microsoft/mcp` repository at 2,800 stars with 40+ Azure services) that includes 7 Key Vault tools — but the `entraid-mcp-server` is the dedicated identity management option.

Additionally, Microsoft recommends securing MCP servers with Entra ID authentication through Azure App Service — a deployment pattern rather than a standalone server.

### AWS Cognito

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [gitcarrot/mcp-server-aws-cognito](https://github.com/gitcarrot/mcp-server-aws-cognito) | 2 | JavaScript | 12 | stdio |

**gitcarrot/mcp-server-aws-cognito** (2 stars, JavaScript, 4 commits) is a community server for AWS Cognito authentication flows. Twelve tools covering the complete user lifecycle:

`sign_up`, `sign_up_confirm_code_from_email`, `sign_in`, `sign_out`, `getCurrentUser`, `reset_password_send_code`, `reset_password_verify_code`, `change_password`, `refresh_session`, `update_user_attributes`, `delete_user`, `resend_confirmation_code`, and `verify_software_token` (MFA).

This is a user-facing authentication server (sign-up, sign-in flows) rather than an admin-facing identity management server. Requires Node.js 18+, AWS Cognito User Pool ID and Client ID. Very early-stage with only 4 commits.

Note: AWS also provides an MCP Proxy (`aws/mcp-proxy-for-aws`) that handles SigV4 authentication for connecting to IAM-secured MCP servers on AWS — a complementary infrastructure tool, not a Cognito management interface.

## Standards-Based Identity

### SCIM MCP Relay

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [chenhunghan/scim-mcp](https://github.com/chenhunghan/scim-mcp) | 0 | TypeScript | 10 | stdio |

**chenhunghan/scim-mcp** (0 stars, TypeScript, 89 commits) implements the SCIM 2.0 standard (RFC 7644) as an MCP relay for AI agents. Ten tools covering full user and group lifecycle:

`create-user`, `retrieve-user`, `replace-user`, `update-user`, `remove-user`, `create-group`, `retrieve-group`, `replace-group`, `update-group`, `remove-group`.

The standout feature is **automatic PII masking** — sensitive personal data (emails, phone numbers, names, addresses) is automatically masked in LLM responses for GDPR/privacy compliance. This is a critical capability for identity management — without it, every user query could expose personally identifiable information to the language model's context window.

SCIM is the interoperability standard — this server works with any SCIM-compliant identity provider or service provider, making it the most vendor-neutral option in the category. Low adoption but high commit count suggests active development.

## Auth Proxies (Securing MCP Servers)

This subcategory addresses the other side of identity + MCP: not managing identity platforms, but using identity platforms to secure MCP servers.

### MCP Auth Proxy

| Server | Stars | Language | Transport Support |
|--------|-------|----------|-------------------|
| [sigbit/mcp-auth-proxy](https://github.com/sigbit/mcp-auth-proxy) | 74 | Go | stdio, SSE, HTTP |

**sigbit/mcp-auth-proxy** (74 stars, Go, MIT, 135 commits, v2.5.4 March 2026) is the leading auth proxy for MCP servers. It sits between MCP clients and your MCP servers, adding OAuth 2.1 authentication without requiring any code changes to the MCP server.

Supported identity providers: **Google**, **GitHub**, and **any OIDC-compatible provider** (Okta, Auth0, Azure AD, Keycloak). Also supports optional password authentication. Flexible user authorization with exact matching and glob patterns.

Verified compatibility with Claude, ChatGPT, GitHub Copilot, and Cursor. The distinction from gateway projects like MCP Gateway: this focuses purely on lightweight authentication for individual or small groups of MCP servers, not multi-server orchestration.

### mcp-front (Stainless)

| Server | Stars | Language | Transport Support |
|--------|-------|----------|-------------------|
| [stainless-api/mcp-front](https://github.com/stainless-api/mcp-front) | 39 | Go | HTTP |

**stainless-api/mcp-front** (39 stars, Go, Elastic License 2.0) adds authentication to MCP tools for Claude.ai, Claude Code, Cursor, and Gemini. Supports Google, Azure AD, GitHub, and any OIDC provider.

Configuration includes Firestore persistence, HTTPS, and per-user service authentication. The proxy handles authentication while MCP servers handle authorization and input validation. Install via Go, Docker, or npm.

Note the licensing: Elastic License 2.0 with commercial exceptions — using mcp-front as infrastructure for your services is permitted, but offering it as a hosted product is not.

### WSO2 Open MCP Auth Proxy

| Server | Stars | Language | Transport Support |
|--------|-------|----------|-------------------|
| [wso2-attic/open-mcp-auth-proxy](https://github.com/wso2-attic/open-mcp-auth-proxy) | 42 | Go | stdio, SSE, HTTP |

**wso2-attic/open-mcp-auth-proxy** (42 stars, Go) is a lightweight authorization proxy that enforces the MCP authorization specification. Features JWT validation (signature, audience, scope), identity provider integration with any OAuth/OIDC provider (Asgardeo, Auth0, Keycloak), protocol version negotiation via `MCP-Protocol-Version` header, and context-aware security with dynamic evaluation.

Note: the repository is in the `wso2-attic` organization, indicating it may be archived or less actively maintained. WSO2 has since launched the Asgardeo MCP Server as the recommended path for WSO2 identity integration.

## Developer Auth Platforms

### Clerk MCP Tools

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [clerk/mcp-tools](https://github.com/clerk/mcp-tools) | 33 | TypeScript | Library | — |

**clerk/mcp-tools** (33 stars, TypeScript, 53 commits) is not an MCP server — it's a library built on top of the MCP TypeScript SDK that makes it easier to implement MCP with authentication. Key functions include:

**Server-side** — `generateProtectedResourceMetadata` (RFC 9728), `generateAuthorizationServerMetadata` (RFC 8414), Clerk-specific variants of both. **Client-side** — `createDynamicallyRegisteredMcpClient`, `completeAuthWithCode`, `getClientBySessionId`.

Framework adapters for Express.js and Next.js. Multiple storage backends: Redis, PostgreSQL, SQLite, filesystem. Supports both dynamic and known credentials authentication flows.

This is the right abstraction level — instead of building another identity management MCP server, Clerk provides the building blocks for adding authentication to any MCP server. Useful for developers building MCP servers that need Clerk-based auth.

### Stytch and WorkOS

Both Stytch and WorkOS provide MCP authentication infrastructure rather than MCP servers:

**Stytch** offers Connected Apps integration for MCP servers deployed on Cloudflare, enabling email, Google login, or enterprise SSO for AI agents. Demo repositories available (`mcp-stytch-consumer-todo-list`, `vercel-mcp-example`).

**WorkOS** provides OAuth 2.1 flows, tool permissions, PKCE, and scopes for giving AI agents access to applications. Their developer guide covers the MCP auth specification in depth.

Neither ships a traditional MCP server — they're infrastructure for building authenticated MCP experiences.

## Also noted

**Tigris OIDC Provider** — open-sourced a hybrid OIDC server where their MCP server acts as a partial OIDC passthrough proxy to Auth0 while also issuing its own tokens. The blog post documenting this pattern is one of the best technical references for MCP OAuth implementation.

**johnidm/mcp-auth-oidc** (0 stars, Python, MIT, 3 commits) — a reference implementation for protecting MCP tools with OAuth 2.1 using Auth0 as the identity provider, including Dynamic Client Registration, scope-based access control, and calculator/notes demo tools.

**Firebase** — Google's Firebase MCP server (official, GA as of October 2025) is primarily a Firebase management server, not an auth server, but Firebase Authentication with Identity Platform supports MFA, SAML, OpenID Connect, and multi-tenancy. The community `mcp-cloud.ai` project demonstrates Firebase Auth for securing MCP servers.

**IBM MCP Context Forge** — an AI Gateway with centralized discovery and guardrails. Has open feature requests for LDAP/Active Directory integration and RBAC with multi-tenancy.

**Descope** — provides Inbound Apps for authenticating users to MCP servers via email, social login, or SSO. No dedicated MCP server but documentation for integration.

**MCP Authorization Specification** — the MCP spec itself standardizes OAuth 2.1 for MCP authorization. As of the June 2025 revision, MCP servers act as OAuth 2.1 Resource Servers (consuming access tokens), not Authorization Servers (issuing tokens). This is the correct separation of concerns and means any OAuth/OIDC provider can secure any MCP server.

## What's missing

**No unified identity management server** — every identity provider has its own MCP server with different tool names, different auth flows, and different capability levels. There's no cross-provider abstraction equivalent to `domain-suite-mcp` in the DNS category.

**No LDAP/Active Directory MCP server** — despite LDAP being the backbone of most enterprise directory infrastructure, no dedicated MCP server exists for LDAP operations. The IBM Context Forge project has this as an open feature request.

**No official 1Password or Google Identity Platform MCP server** — both are major players in their respective spaces. The 1Password community servers (reviewed in [Secret Management](/reviews/secret-management-mcp-servers/)) cover vault operations but not identity federation.

**No user provisioning lifecycle server** — the SCIM MCP relay is the closest, but there's no server that handles the full provisioning lifecycle (hire → provision → role change → offboard) across multiple systems.

**Limited safety controls** — only Auth0 has credential redaction and the official Okta server has elicitation-based confirmation. Most identity MCP servers will happily delete users, deactivate accounts, or modify permissions without confirmation — dangerous in a domain where mistakes are hard to reverse.

**No MFA management through MCP** — while the Entra ID server can view MFA status, no server provides comprehensive MFA enrollment, reset, or bypass capabilities through MCP.

## The verdict

The identity and authentication MCP category splits between two well-defined use cases that are both early-stage but functional:

**For managing identity platforms:** Auth0's server has the best developer experience with credential redaction, configurable tool access, and keychain-based authentication. For Okta shops, the Fctr community server (38 stars, 120 commits) is more capable than the official server (24 stars, 14 commits). For open-source identity, sshaaf's Keycloak server (Java/Quarkus, cloud-native) or idoyudha's (Python, more tools) depending on your stack. Casdoor is the most ambitious with built-in MCP support in the IAM platform itself.

**For securing MCP servers:** MCP Auth Proxy (74 stars, Go, MIT) is the clear leader — drop-in OAuth 2.1 with support for Google, GitHub, and any OIDC provider, verified across four major MCP clients. The MCP spec's alignment with OAuth 2.1 Resource Server semantics means this problem is becoming well-standardized.

**Rating: 3.5/5** — functional tools exist for major identity platforms and auth proxy use cases, but low adoption (most servers under 100 stars), fragmented provider coverage, limited safety controls for destructive identity operations, and no cross-provider abstraction. The MCP auth specification is maturing faster than the identity management servers — securing MCP connections is more standardized than managing identity through MCP.

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*


# Identity & Authentication MCP Servers — Okta, Auth0, Keycloak, Entra ID, Casdoor, and More

> Identity and authentication MCP servers let AI agents manage users, configure SSO, provision identities, and secure MCP connections through natural language.


Identity and authentication is a category that splits cleanly into two use cases: **managing identity platforms through MCP** (administering users, groups, applications, and policies in Okta, Auth0, Keycloak, etc.) and **securing MCP servers with identity** (adding OAuth 2.1 / OIDC authentication to any MCP server). Both have matured significantly since March 2026. The category spans seven areas: **enterprise identity platforms** (Okta, Auth0, Keycloak, Casdoor, Asgardeo), **cloud IAM** (Microsoft Entra ID, AWS Cognito), **open-source identity** (FusionAuth, Authentik), **standards-based identity** (SCIM relay, OIDC implementations), **auth proxies** (MCP Auth Proxy, mcp-front, AthenZ), **developer auth platforms** (Clerk, Stytch), and **MCP authorization specification** tooling.

The headline findings as of May 2026: **[Auth0 Auth for MCP went GA on May 6](https://auth0.com/blog/auth0-auth-for-mcp-servers-generally-available/)** — no longer Early Access — with CIMD client registration as the default, OBO token exchange for downstream API calls, native MCP resource identifiers, and Resource Parameter Compatibility Mode for spec compliance. **[Okta Cross App Access (XAA)](https://www.okta.com/newsroom/articles/cross-app-access-extends-mcp-to-bring-enterprise-grade-security-to-ai-agents/)** — launched as "Enterprise-Managed Authorization" — is being built into the official MCP TypeScript and Java SDKs, meaning any agent using these SDKs gains enterprise identity and authorization without custom security plumbing; [enterprise backers](https://www.okta.com/newsroom/press-releases/new-okta-innovations-secure-the-ai-driven-enterprise-and-combat-fraud-with-an-identity-security-fabric/) include AWS, Google Cloud, Salesforce, Box, Grammarly, Miro, and four more (Automation Anywhere, Boomi, Glean, WRITER). **Ping Identity AIC MCP Server** joins the field as a new notable entrant, focusing on AI-native identity management in IDEs and CLIs. **[Keycloak reached 26.6.2 (May 19)](https://www.keycloak.org/2026/05/keycloak-2662-released)** with 16 CVE patches one day before this refresh. **[CVE-2026-32211](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-32211)** (CVSS 9.1 Azure MCP auth bypass), disclosed April 3, 2026, has since been mitigated by Microsoft. And agent identity dominated RSAC 2026: [the Coalition for Secure AI reported](https://www.coalitionforsecureai.org/coalition-for-secure-ai-unveils-new-agentic-identity-and-security-research-following-high-profile-sessions-at-rsac-2026/) it was the top security question of the conference. Previous milestones that remain relevant: **[Okta for AI Agents GA April 30](https://www.okta.com/newsroom/press-releases/showcase-2026/)** with Agent Gateway; [FusionAuth's 300+ tools](https://github.com/FusionAuth/fusionauth-mcp-api) and Authentik's 245 tools as new entrants; Keycloak 26.6.0's experimental CIMD support; Microsoft MCP Server for Enterprise in public preview (read-only, no CIMD/DCR); and [research showing 38% of MCP servers still lack authentication](https://dev.to/kenimo49/38-of-mcp-servers-have-no-auth-inside-the-owasp-mcp-top-10-hm).

**Category:** [Security & Compliance](/categories/security-compliance/)

## Enterprise Identity Platforms

### Okta (Official)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [okta/okta-mcp-server](https://github.com/okta/okta-mcp-server) | 53 | Python | 20+ | stdio |

**okta/okta-mcp-server** (53 stars as of this audit, up from 24 at last review — Python, Apache 2.0) is the official Okta MCP server. Twenty-plus tools across users, groups, applications, and policies:

**User management** — `list_users`, `get_user`, `create_user`, `update_user`, `deactivate_user`, `delete_deactivated_user`. **Group operations** — `list_groups`, `get_group`, `create_group`, `update_group`, `delete_group`, `add_user_to_group`, `remove_user_from_group`. **Applications** — `list_applications`, `get_application`. **Policies** — `list_okta_policy_rules`, `get_okta_policy_rule`.

The standout feature is **interactive confirmation via elicitation** — destructive operations (deletes, deactivations) prompt the user for confirmation through the MCP Elicitation API before proceeding, with automatic fallback for clients that don't yet support elicitation. This is the right safety model for identity management, where accidentally deleting a user or deactivating an application can have cascading consequences.

Authentication uses Device Authorization Grant (interactive, browser-based) or Private Key JWT (browserless, server-to-server). Built on Okta's official Python SDK.

**[April 2026 — Okta for AI Agents GA April 30](https://www.okta.com/newsroom/press-releases/showcase-2026/):** Okta announced the biggest enterprise identity+MCP initiative yet. **Agent Gateway** serves as a centralized control plane to secure AI agent access to resources, with a **virtual MCP server** capability that aggregates and exposes tools from **Okta's MCP Registry**. All agent-resource interactions are logged for audit and observability. Agent Integrations in the OIN extend the 8,200+ integration catalog to include AI agent platforms (Boomi, DataRobot, Google Vertex AI). Agent credentials can be vaulted and automatically rotated.

**[May 2026 — Cross App Access (XAA) native in MCP SDKs](https://www.okta.com/newsroom/articles/cross-app-access-extends-mcp-to-bring-enterprise-grade-security-to-ai-agents/):** Okta's Cross App Access has been incorporated into the MCP specification as "Enterprise-Managed Authorization," building on the IETF OAuth Working Group's Identity Assertion Authorization Grant (IAG) draft. The **official MCP TypeScript and Java SDKs are adopting XAA support** (Python in progress as of this source) — any tool or agent built on these SDKs gains enterprise-grade identity and authorization without custom security plumbing. This is among the most significant SDK-level identity integrations in MCP's history to date. **Operant AI's MCP Gateway** also joined the Okta Integration Network, bringing zero-trust enforcement to agent interactions in the Okta ecosystem.

### Okta (Fctr Community)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [fctr-id/okta-mcp-server](https://github.com/fctr-id/okta-mcp-server) | 38 | Python | 20+ | stdio, HTTP, SSE |

**[fctr-id/okta-mcp-server](https://github.com/fctr-id/okta-mcp-server)** (38 stars, Python) is a community Okta server built specifically for IAM engineers, security teams, and Okta administrators. **Correction (2026-08-15 audit):** the body text previously said "31 stars," inconsistent with the 38 shown in the table above it — both are now reconciled to the current, verified count.

**Specialized analysis tools** — `analyze_user_app_access` (answers "Can user X access app Y?" — the most common question Okta admins face), `analyze_login_risk` (behavioral analysis with VPN/Tor detection and geographic impossibility checks). **Standard management** — full user, group, application, policy, network zone, and event log tools.

What makes this distinct from the official server: it's built on Anthropic's MCP architecture pattern with dual-mode operation, supports multiple AI providers (OpenAI, Azure, Anthropic, Google Vertex AI), and ships with Docker deployment. The Fctr team also maintains a successor repository (`fctr-okta-mcp-server`) with agentic API discovery and guided code execution. For day-to-day Okta administration, this is the more capable option.

### Auth0

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [auth0/auth0-mcp-server](https://github.com/auth0/auth0-mcp-server) | 112 | TypeScript | 18+ | stdio |

**auth0/auth0-mcp-server** (~112 stars, TypeScript, MIT) is the official Auth0 MCP server and the most polished identity platform server in the category. Eighteen-plus tools across six categories:

**Applications** (4 tools) — create, list, update, delete Auth0 applications. **Resource Servers** (4 tools) — API resource management. **Actions** (5 tools) — deploy Auth0 Actions for extensibility logic. **Forms** (5 tools) — configure Auth0 Forms. **Logs** (2 tools) — query tenant logs. **Application Grants** (1 tool) — manage client grants.

The security model is thoughtful: **sensitive fields are automatically redacted** with `[REDACTED]` in responses (preventing accidental credential exposure through LLM context), credentials are stored in the system keychain (never in plain text), and tool access can be restricted using `--tools` (whitelist specific tools) and `--read-only` (disable write operations) flags.

Authentication uses Device Authorization Flow with secure keychain storage. Supports Claude Desktop, Windsurf, Cursor, VS Code, and Gemini CLI (added in v0.1.0-beta.8). Still in beta but actively maintained. The developer experience is the best in the identity MCP category.

**[Auth for MCP — GA May 6, 2026](https://auth0.com/blog/auth0-auth-for-mcp-servers-generally-available/)** (was Early Access as of April 22): Auth0's separate product extending OAuth 2.1 and OIDC directly into the MCP ecosystem is now generally available, described as "the identity layer that helps you ship more secure, production-ready MCP servers." GA features: **MCP Server Authorization** (protect MCP servers via Auth0 Universal Login with social, enterprise, and custom identity providers, full MFA and attack protection), **CIMD client registration** (replacing Dynamic Client Registration as the preferred method — a client's identity is a URL pointing to a JSON document the client controls), **On-Behalf-Of (OBO) token exchange** (MCP servers exchange tokens for short-lived access tokens scoped to internal APIs, calling downstream APIs on behalf of users), **native MCP resource identifiers**, and **Resource Parameter Compatibility Mode** for spec compliance. Auth0 is now positioning itself as the authorization layer for the entire MCP ecosystem, not just the management server.

### Keycloak (sshaaf)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [sshaaf/keycloak-mcp-server](https://github.com/sshaaf/keycloak-mcp-server) | 46 | Java | 15+ | SSE |

**sshaaf/keycloak-mcp-server** (46 stars, Java, MIT) is the most mature Keycloak MCP server. Built with Quarkus for cloud-native deployment including OpenShift/Kubernetes, multi-architecture container images, and GraalVM native image support.

Covers users, realms, clients, roles, groups, IDPs, and authentication flow management. Also integrates with Keycloak Discourse for searching community knowledge.

Authentication uses JWT Bearer tokens — each user obtains their own JWT from Keycloak and configures it in their MCP client. This is the right approach for a Keycloak server since Keycloak is itself the identity provider. V0.3.0 released December 2025.

**Keycloak 26.6.0 (April 2026) — CIMD support for MCP:** Keycloak now includes experimental support for Client ID Metadata Documents (CIMD), allowing it to serve as an authorization server for MCP version 2025-11-25 or later. CIMD is the MCP spec's preferred client registration method — a client's identity is a URL pointing to a JSON document the client controls, which the authorization server fetches on demand. This makes Keycloak a spec-compliant MCP authorization server out of the box. Keycloak 26.5.0 (January 2026) shipped the MCP authorization server integration guide at keycloak.org.

**[Keycloak 26.6.1 (April 15, 2026) — security patches](https://www.keycloak.org/2026/04/keycloak-2661-released):** CVE-2026-4366 (Blind SSRF via HTTP redirect handling) and CVE-2026-4633 (user enumeration via identity-first login).

**[Keycloak 26.6.2 (May 19, 2026) — 16 CVEs (6 named here)](https://www.keycloak.org/2026/05/keycloak-2662-released):** CVE-2026-33871 (HTTP/2 CONTINUATION Frame Flood DoS), CVE-2026-33870 (HTTP Request Smuggling), CVE-2026-4628 (improper access control on UMA resource management endpoints), CVE-2026-37980 (stored XSS in select-organization.ftl), CVE-2026-5588 (Bouncy Castle cryptographic vulnerability), and CVE-2026-6856 (AAGUID policy bypass in WebAuthn registration). The remaining ten cover further Bouncy Castle, SAML, redirect-URI, session-fixation, and access-control issues. **Correction (2026-08-15 audit):** previously stated as "18 CVEs" (with the front matter's card_description separately saying "six CVEs") — the official Keycloak release notes list 16. Upgrade urgently if running Keycloak as an MCP authorization server.

### Keycloak (idoyudha)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [idoyudha/mcp-keycloak](https://github.com/idoyudha/mcp-keycloak) | 4 | Python | 30+ | stdio, HTTP |

**idoyudha/mcp-keycloak** (4 stars, Python, MIT, 85 commits) is a Python alternative with more comprehensive tool coverage — 30+ tools across user management (CRUD, password reset, session control), client management (CRUD, secret management, service accounts), role management (realm and client-specific roles, user role assignments), group management (hierarchy, membership), realm administration (configuration, events, default groups), and authentication flow management.

The tool count is higher than sshaaf's Java server, and the Python implementation may be more accessible for teams already using Python-based toolchains. Both are legitimate options — choose based on your deployment preference (Java/Quarkus vs. Python).

### Casdoor

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [casdoor/casdoor](https://github.com/casdoor/casdoor) | 14,191 | Go | Built-in | HTTP (Streamable + JSON-RPC) |

**casdoor/casdoor** (~14,191 stars, Go, Apache 2.0) is fundamentally different from every other entry in this review: it's not a separate MCP server — it's a full IAM platform with MCP built directly into the product. The GitHub description has been updated to "Agent-first Identity and Access Management (IAM) / LLM MCP & agent gateway," and the feature list now explicitly leads with MCP, A2A, and OpenClaw alongside legacy auth protocols.

Casdoor now ships a native **Streamable HTTP MCP server** (in addition to JSON-RPC 2.0 at `/api/mcp`), allowing AI agents to manage Casdoor identity operations through natural language. Supports OAuth 2.1, OIDC, SAML, CAS, LDAP, SCIM, WebAuthn, TOTP, MFA, Face ID, Google Workspace, Azure AD, and A2A authentication.

Every MCP tool call is authenticated and authorized with **fine-grained, scope-based permissions** — the tools available depend on the OAuth scopes in your access token. Casdoor can also serve as an **auth provider for other MCP servers** (Protected Resource Metadata pointing to Casdoor for user authentication, consent, token issuance, and validation).

**CNCF milestone:** Casdoor [joined the CNCF Cloud Native Landscape](https://casdoor.ai/blog/casdoor-joins-cncf-landscape/) (Security & Compliance / Provisioning category) on February 22, 2026 — the most significant open-source identity project recognition of the quarter.

Star count has continued climbing (~13,628 at the prior review, ~14,191 as of this audit) reflecting growing adoption as the "agent-first IAM" positioning resonates with developers building MCP infrastructure.

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
| [hieuttmmo/entraid-mcp-server](https://github.com/hieuttmmo/entraid-mcp-server) | 40 | Python | 30+ | stdio |

**hieuttmmo/entraid-mcp-server** (40 stars, Python, MIT) provides tools for interacting with Microsoft Entra ID (formerly Azure AD) through the Graph API. Thirty-plus tools across:

**User operations** — search, get by ID, list privileged users, view roles, groups, and MFA status. **Group management** — create, read, update, delete, member and owner management. **Sign-in logs and audit logs** — query authentication events. **Device management** — enumerate and manage devices. **Conditional access policies** — view and manage access rules. **Password management** — auto-generated secure passwords. **Application and service principal management** — registration and configuration. **Permissions helper** — helps implement the principle of least privilege.

The modular, resource-oriented architecture with a centralized Graph Client for authentication is well-designed.

**Microsoft MCP Server for Enterprise (public preview, no GA date)** — Microsoft's official MCP Server focused on Entra identity and directory read-only scenarios. Two tools: `microsoft_graph_suggest_queries` (RAG-powered Microsoft Graph API discovery) and `microsoft_graph_get` (read-only Graph API calls honoring user roles, granted scopes, and throttling limits). Covers user, group, application, and device insights, security posture (authentication methods, Conditional Access), privileged access management, application risk assessment, and access governance. No extra cost or separate license.

**Critical limitation confirmed as of May 2026:** Microsoft Entra **does not support CIMD or Dynamic Client Registration (DCR)** — the two primary MCP client registration mechanisms in the current spec. Only pre-registered client applications are supported for MCP client configuration. Work to support CIMD in Entra is planned but no release date was announced. This means Entra lags every other major identity provider on MCP spec compliance.

Microsoft published guidance in April 2026 on using the OBO (On-Behalf-Of) flow with pre-authorized clients as a workaround — see the TechCommunity blog post "Building MCP servers with Entra ID and pre-authorized clients."

### AWS Cognito

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [gitcarrot/mcp-server-aws-cognito](https://github.com/gitcarrot/mcp-server-aws-cognito) | 2 | JavaScript | 12 | stdio |

**gitcarrot/mcp-server-aws-cognito** (2 stars, JavaScript, 4 commits) is a community server for AWS Cognito authentication flows. Twelve tools covering the complete user lifecycle:

`sign_up`, `sign_up_confirm_code_from_email`, `sign_in`, `sign_out`, `getCurrentUser`, `reset_password_send_code`, `reset_password_verify_code`, `change_password`, `refresh_session`, `update_user_attributes`, `delete_user`, `resend_confirmation_code`, and `verify_software_token` (MFA).

This is a user-facing authentication server (sign-up, sign-in flows) rather than an admin-facing identity management server. Requires Node.js 18+, AWS Cognito User Pool ID and Client ID. Very early-stage with only 4 commits.

Note: AWS also provides an MCP Proxy (`aws/mcp-proxy-for-aws`) that handles SigV4 authentication for connecting to IAM-secured MCP servers on AWS — a complementary infrastructure tool, not a Cognito management interface.

### Ping Identity (New — May 2026)

| Server | Language | Tools | Transport |
|--------|----------|-------|-----------|
| PingOne Advanced Identity Cloud (AIC) MCP Server | — | 14 | stdio/HTTP |
| PingOne MCP Server | — | 14 | stdio/HTTP |

**[Ping Identity](https://press.pingidentity.com/2026-03-24-Ping-Identity-Defines-the-Runtime-Identity-Standard-for-Autonomous-AI)** launched its "Identity for AI" platform at GA on March 31, 2026 with a three-component architecture: Agent IAM Core, Agent Gateway, and Agent Detection. Two MCP servers followed:

**PingOne Advanced Identity Cloud (AIC) MCP Server** — connects PingOne AIC environments to AI agents in IDEs (Cursor, VS Code, GitHub Copilot) and CLIs (Claude Code, Gemini CLI). Fourteen tools focused on AI-native identity management scenarios within the AIC environment.

**PingOne MCP Server** — exposes 14 management tools for the standard PingOne platform.

**PingGateway 2026** includes an MCP security gateway module for organizations running Ping's on-premises gateway. Both MCP and A2A protocols are supported.

Ping Identity positions itself as providing "the runtime identity standard for autonomous AI" — a direct competitive response to Okta's Agent Gateway and Auth0's Auth for MCP. For enterprises already running Ping Identity infrastructure, the AIC MCP Server offers native integration without adding a third-party identity layer.

## Standards-Based Identity

### SCIM MCP Relay

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [chenhunghan/scim-mcp](https://github.com/chenhunghan/scim-mcp) | 0 | TypeScript | 10 | stdio |

**chenhunghan/scim-mcp** (0 stars, TypeScript, 89 commits) implements the SCIM 2.0 standard (RFC 7644) as an MCP relay for AI agents. Ten tools covering full user and group lifecycle:

`create-user`, `retrieve-user`, `replace-user`, `update-user`, `remove-user`, `create-group`, `retrieve-group`, `replace-group`, `update-group`, `remove-group`.

The standout feature is **automatic PII masking** — sensitive personal data (emails, phone numbers, names, addresses) is automatically masked in LLM responses for GDPR/privacy compliance. This is a critical capability for identity management — without it, every user query could expose personally identifiable information to the language model's context window.

SCIM is the interoperability standard — this server works with any SCIM-compliant identity provider or service provider, making it the most vendor-neutral option in the category. Low adoption but high commit count suggests active development.

## Open-Source Identity Platforms

### FusionAuth (Official)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [FusionAuth/fusionauth-mcp-api](https://github.com/FusionAuth/fusionauth-mcp-api) | 1 | TypeScript | 300+ | stdio |

**FusionAuth/fusionauth-mcp-api** (TypeScript, Apache 2.0) is the official FusionAuth MCP server — and it has the most tools of any identity MCP server by a wide margin. Per [the repo's README](https://github.com/FusionAuth/fusionauth-mcp-api), "the default MCP Server has a tool for every API endpoint of FusionAuth — over 300 of them." The server stays automatically up to date — when FusionAuth updates their API, the MCP server is regenerated and released.

This is a **preview release** designed for local development and experimentation, not production use. Install via `npx @fusionauth/mcp-api`. Perfect for rapid prototyping, learning the FusionAuth API, or automating configuration tasks during development.

FusionAuth also ships a separate **Docs MCP Server** for AI-assisted documentation queries. The breadth of API coverage is unmatched — no other identity MCP server exposes its entire API surface as MCP tools.

### Authentik

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [cdmx-in/authentik-mcp](https://github.com/cdmx-in/authentik-mcp) | 17 | Python/TypeScript | 245 | stdio |

**cdmx-in/authentik-mcp** (17 stars) ships four MCP server variants for the open-source Authentik identity platform: **authentik-mcp** (Python, full CRUD), **authentik-mcp** (TypeScript/Node.js, full API access), **authentik-diag-mcp** (Python, read-only diagnostics), and **authentik-diag-mcp** (TypeScript/Node.js, diagnostics). Third-party [MCP directory listings](https://mcpmarket.com/server/authentik-1) put the full servers at 245 tools across 20 API categories, covering user, group, and application management alongside event monitoring, authentication flow configuration, and system administration; the upstream README does not itself state a total tool count, so treat the 245 figure as directory-reported rather than vendor-stated.

The diagnostic-only variants are a thoughtful addition — they let teams connect AI assistants to Authentik for monitoring and troubleshooting without granting write access. Multiple community implementations also exist (Samik081/mcp-authentik, nikitatsym/authentik-mcp).

## Auth Proxies (Securing MCP Servers)

This subcategory addresses the other side of identity + MCP: not managing identity platforms, but using identity platforms to secure MCP servers.

### MCP Auth Proxy

| Server | Stars | Language | Transport Support |
|--------|-------|----------|-------------------|
| [sigbit/mcp-auth-proxy](https://github.com/sigbit/mcp-auth-proxy) | 159 | Go | stdio, SSE, HTTP |

**sigbit/mcp-auth-proxy** (159 stars as of this audit, up from 74 at last review — Go, MIT) is the leading auth proxy for MCP servers. It sits between MCP clients and your MCP servers, adding OAuth 2.1 authentication without requiring any code changes to the MCP server.

Supported identity providers: **Google**, **GitHub**, and **any OIDC-compatible provider** (Okta, Auth0, Azure AD, Keycloak). Also supports optional password authentication. Flexible user authorization with exact matching and glob patterns.

Verified compatibility with Claude, ChatGPT, GitHub Copilot, and Cursor. The distinction from gateway projects like MCP Gateway: this focuses purely on lightweight authentication for individual or small groups of MCP servers, not multi-server orchestration.

### mcp-front (Stainless)

| Server | Stars | Language | Transport Support |
|--------|-------|----------|-------------------|
| [stainless-api/mcp-front](https://github.com/stainless-api/mcp-front) | 57 | Go | HTTP |

**stainless-api/mcp-front** (57 stars, Go, Elastic License 2.0) adds authentication to MCP tools for Claude.ai, Claude Code, Cursor, and Gemini. Supports Google, Azure AD, GitHub, and any OIDC provider.

Configuration includes Firestore persistence, HTTPS, and per-user service authentication. The proxy handles authentication while MCP servers handle authorization and input validation. Install via Go, Docker, or npm.

Note the licensing: Elastic License 2.0 with commercial exceptions — using mcp-front as infrastructure for your services is permitted, but offering it as a hosted product is not.

### AthenZ MCP OAuth Proxy

| Server | Stars | Language | Transport Support |
|--------|-------|----------|-------------------|
| [AthenZ/mcp-oauth-proxy](https://github.com/AthenZ/mcp-oauth-proxy) | 2 | Go | HTTP |

**AthenZ/mcp-oauth-proxy** (2 stars, Apache 2.0) is a multi-provider OAuth proxy that unifies Google, GitHub, Atlassian, Okta, and more behind a single endpoint while enforcing authorization through integration with Athenz for fine-grained RBAC. Key differentiators: token management with encryption (DynamoDB + KMS), mTLS security for certificate-based client authentication in machine-to-machine flows, and enterprise-grade token storage. The Athenz integration adds role-based access control decisions that the simpler auth proxies lack — useful for enterprises that need per-tool authorization based on user roles, not just authentication.

### WSO2 Open MCP Auth Proxy

**Correction (2026-08-15 audit):** as of this audit, `github.com/wso2/open-mcp-auth-proxy` returns 404 (checked both the API and the repo page directly), and the repo no longer appears under the `wso2` org's repository listing or `wso2-attic` (also checked directly), nor in GitHub's own search index. This is a genuine removal, not the "moved from wso2-attic back to wso2" reversal the article previously described — that framing is no longer accurate and has been removed. No documented successor repo was found; secondary references to it (pkg.go.dev, mcp.so, a WSO2 Solution Architecture team Medium post) still exist but point at the same now-missing URL. Given no live, verifiable primary source remains, this entry is cut from the active auth-proxy comparison rather than left as a dead link. Readers evaluating WSO2's MCP identity tooling should instead see the Asgardeo MCP Server entry earlier in this review (under Enterprise Identity Platforms), which remains live and WSO2-maintained.

## Developer Auth Platforms

### Clerk MCP Tools

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [clerk/mcp-tools](https://github.com/clerk/mcp-tools) | 47 | TypeScript | Library | — |

**clerk/mcp-tools** (47 stars, TypeScript, MIT) is not an MCP server — it's a library built on top of the MCP TypeScript SDK that makes it easier to implement MCP with authentication. Key functions include:

**Server-side** — `generateProtectedResourceMetadata` (RFC 9728), `generateAuthorizationServerMetadata` (RFC 8414), Clerk-specific variants of both. **Client-side** — `createDynamicallyRegisteredMcpClient`, `completeAuthWithCode`, `getClientBySessionId`.

Framework adapters for Express.js and Next.js. Multiple storage backends: Redis, PostgreSQL, SQLite, filesystem. Supports both dynamic and known credentials authentication flows.

This is the right abstraction level — instead of building another identity management MCP server, Clerk provides the building blocks for adding authentication to any MCP server. Useful for developers building MCP servers that need Clerk-based auth.

**New: Clerk MCP Server (public beta, January 2026)** — Clerk also launched a dedicated MCP server that helps AI coding assistants (Claude, Cursor, GitHub Copilot) provide accurate Clerk SDK snippets and implementation patterns. This is a developer assistance server, not an identity management server — it gives AI agents Clerk-specific context for code generation rather than administrative access to Clerk tenants.

### Stytch and WorkOS

Both Stytch and WorkOS provide MCP authentication infrastructure rather than MCP servers:

**Stytch** offers Connected Apps integration for MCP servers deployed on Cloudflare, enabling email, Google login, or enterprise SSO for AI agents. Demo repositories available (`mcp-stytch-consumer-todo-list`, `vercel-mcp-example`).

**WorkOS** provides OAuth 2.1 flows, tool permissions, PKCE, and scopes for giving AI agents access to applications. **May 2026 updates:** WorkOS added CIMD support to WorkOS Connect (AuthKit) for MCP, JWT Templates for Connect in MCP/OAuth apps, and PKCE for public clients in the Node SDK. WorkOS also published a comparison guide ("best providers for MCP server authentication in 2026") positioning themselves against Auth0, Okta, and Clerk.

Neither ships a traditional MCP server — they're infrastructure for building authenticated MCP experiences.

## Also noted

**Tigris OIDC Provider** — open-sourced a hybrid OIDC server where their MCP server acts as a partial OIDC passthrough proxy to Auth0 while also issuing its own tokens. The blog post documenting this pattern is one of the best technical references for MCP OAuth implementation.

**[johnidm/mcp-auth-oidc](https://github.com/johnidm/mcp-auth-oidc)** (1 star, Python, MIT) — a reference implementation for protecting MCP tools with OAuth 2.1 using Auth0 as the identity provider, including Dynamic Client Registration, scope-based access control, and calculator/notes demo tools.

**Firebase** — Google's Firebase MCP server (official, GA as of October 2025) is primarily a Firebase management server, not an auth server, but Firebase Authentication with Identity Platform supports MFA, SAML, OpenID Connect, and multi-tenancy. The community `mcp-cloud.ai` project demonstrates Firebase Auth for securing MCP servers.

**IBM MCP Context Forge** — an AI Gateway with centralized discovery and guardrails. Has open feature requests for LDAP/Active Directory integration and RBAC with multi-tenancy.

**Descope** — provides Inbound Apps for authenticating users to MCP servers via email, social login, or SSO. No dedicated MCP server but documentation for integration.

**SecureMCP Okta Gateway** — securemcp/securemcp-okta-gateway provides OAuth 2.0 Authorization Server and Resource Server functionality specifically bridging MCP clients to Okta authentication, with Redis-backed session management.

**MCP Authorization Specification** — the MCP spec standardizes OAuth 2.1 for MCP authorization. The 2026-03-15 spec mandates **RFC 8707 resource indicators** to prevent token mis-redemption attacks and introduces **CIMD (Client ID Metadata Documents)** as the preferred client registration method — replacing Dynamic Client Registration as the default. With CIMD, a client's identity is a URL pointing to a JSON document the client controls; authorization servers fetch metadata on demand. The registration priority is now: pre-registration → CIMD → DCR → user-provided credentials. Role-based authorization features enable fine-grained tool access control via annotations like `@RolesAllowed`.

**[MCP OAuth Security Research (Obsidian Security)](https://www.obsidiansecurity.com/blog/when-mcp-meets-oauth-common-pitfalls-leading-to-one-click-account-takeover)** — In early 2026, Obsidian Security disclosed critical one-click account takeover vulnerabilities in multiple well-known MCP server implementations. The root cause: MCP servers acting as API proxies failed to properly handle consent and bind OAuth state to user sessions, enabling CSRF-style attacks. Vendors patched in late 2025. [Security researchers have found that roughly 38% of scanned MCP servers still lack authentication entirely](https://dev.to/kenimo49/38-of-mcp-servers-have-no-auth-inside-the-owasp-mcp-top-10-hm) — independent scans through 2026 have put the figure anywhere from 38% to 41% depending on registry scope and methodology.

**[CVE-2026-32211](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-32211) (Azure MCP Server, CVSS 9.1).** Microsoft disclosed this missing-authentication bypass in the Azure MCP Server (Azure DevOps MCP tooling) on April 3, 2026. An unauthenticated network attacker could exfiltrate configuration details, API keys, authentication tokens, and project data (Azure DevOps work items, repos, pipelines, pull requests). **Correction (2026-08-15 audit):** this entry previously said "STILL UNPATCHED as of May 20, 2026" and "seven-plus weeks unpatched," reflecting the state at the article's last refresh. As of this audit, [Microsoft's advisory](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-32211) and the [GitHub Advisory Database entry](https://github.com/advisories/GHSA-5w7p-v6h9-q8c5) confirm the issue has since been mitigated by Microsoft; no user action is required. It remained unpatched through at least the May 12 Patch Tuesday cycle (which addressed 137 other CVEs but not this one) before being resolved.

**[May 2026 MCP CVE wave](https://www.theregister.com/security/2026/05/13/bug-hunter-tracks-down-three-serious-mcp-database-flaws-one-left-unpatched/5238916):** [The Register reported](https://www.theregister.com/security/2026/05/13/bug-hunter-tracks-down-three-serious-mcp-database-flaws-one-left-unpatched/5238916) (May 13, 2026), drawing on [Akamai security research](https://www.akamai.com/blog/security-research/one-fluke-3-pattern-mcp-back-end-vulnerabilities), three database MCP server vulnerabilities: **[CVE-2025-66335](https://github.com/advisories/GHSA-qhfq-gvvc-5q6q)** (Apache Doris MCP Server — SQL injection via unsanitized `db_name` parameter, patched in v0.6.1), **Alibaba RDS MCP Server** (information disclosure — an unauthenticated RAG tool exposes database metadata; Alibaba declined to patch it), and **Apache Pinot MCP Server** (unauthenticated HTTP endpoint exposing SQL execution tools; StarTree added optional OAuth in v2.0.0+, but the underlying SQL validation weakness persists). Additionally: **[CVE-2026-20205](https://www.sentinelone.com/vulnerability-database/cve-2026-20205/)** (Splunk MCP Server app, versions below 1.0.3 — session/authorization tokens written to logs in clear text; fixed in 1.0.3). A critical, actively-exploited authentication-bypass flaw (CVSS 9.8) was also reported in **[nginx-ui](https://thehackernews.com/2026/04/critical-nginx-ui-vulnerability-cve.html)** — a third-party nginx admin UI, not NGINX itself — dubbed "MCPwn" ([CVE-2026-33032](https://www.darkreading.com/application-security/critical-mcp-integration-flaw-nginx-risk)): its unauthenticated `/mcp_message` MCP endpoint let remote attackers invoke administrative tools, including config writes with automatic reload. Fixed in nginx-ui v2.3.4.

**[STDIO Transport Design Flaw](https://www.theregister.com/2026/04/16/anthropic_mcp_design_flaw/) (April 2026):** OX Security disclosed ([VentureBeat coverage](https://venturebeat.com/security/mcp-stdio-flaw-200000-ai-agent-servers-exposed-ox-security-audit)), and The Register reported (April 16, 2026), a design-level vulnerability in MCP's STDIO transport — user-controlled configuration values are passed to shell execution without sanitization across Anthropic's official Python, TypeScript, Java, and Rust SDKs — estimated to put approximately 200,000 deployments at risk. This is not a CVE for a specific server but a protocol-level concern; Anthropic characterized the behavior as "expected" and placed sanitization responsibility on developers, later updating its security guidance to recommend caution with STDIO adapters.

**[AIP: Agent Identity Protocol](https://arxiv.org/abs/2603.24775) (arxiv, March 25, 2026):** A research paper proposing Invocation-Bound Capability Tokens (IBCTs) — signed JWTs (compact) or Biscuit tokens with Datalog policies (chained) that fuse identity, attenuated authorization, and provenance binding into a single append-only token chain for MCP and A2A. Processing overhead: 0.22 ms per MCP call. Presented at RSAC 2026 context discussions. The Coalition for Secure AI (CoSAI) reported agent identity was the top security question asked at RSAC 2026 — more discussed than any other AI security topic.

## What's missing

**No unified identity management server** — every identity provider has its own MCP server with different tool names, different auth flows, and different capability levels. There's no cross-provider abstraction equivalent to `domain-suite-mcp` in the DNS category.

**No LDAP/Active Directory MCP server** — despite LDAP being the backbone of most enterprise directory infrastructure, no dedicated MCP server exists for LDAP operations. The IBM Context Forge project has this as an open feature request.

**No official 1Password or Google Identity Platform MCP server** — both are major players in their respective spaces. The 1Password community servers (reviewed in [Secret Management](/reviews/secret-management-mcp-servers/)) cover vault operations but not identity federation. Google's managed MCP servers cover 30+ Cloud services but explicitly exclude Workspace identity.

**No user provisioning lifecycle server** — the SCIM MCP relay is the closest, but there's no server that handles the full provisioning lifecycle (hire → provision → role change → offboard) across multiple systems.

**Limited safety controls improving** — Auth0 has credential redaction, the official Okta server has elicitation-based confirmation, and Authentik ships diagnostic-only variants. But most identity MCP servers will still happily delete users, deactivate accounts, or modify permissions without confirmation — dangerous in a domain where mistakes are hard to reverse.

**Agent identity remains the top unsolved problem** — RSAC 2026 confirmed it as the single most-discussed AI security question of the conference, per the Coalition for Secure AI. The core problem: when an AI agent connects to an MCP server, the human user's identity often disappears — the server sees an authenticated agent using a static API key, not the human who authorized the action. Okta's XAA (now in the MCP TypeScript + Java SDKs) and Auth0's Auth for MCP (GA May 6) are the most serious attempts to solve this. A research-level proposal (AIP/IBCTs) appeared on arxiv but remains pre-production. SPIFFE is gaining traction for non-human identity but noted as inadequate for ephemeral agent cross-protocol scenarios. Google Cloud added "Agent Identity" as a first-class IAM concept. The gap is narrowing but no production-grade universal solution exists.

**No MFA management through MCP** — while the Entra ID server can view MFA status, no server provides comprehensive MFA enrollment, reset, or bypass capabilities through MCP.

## The verdict

The identity and authentication MCP category had the most meaningful enterprise investment of any category in April–May 2026, alongside the most alarming security trajectory:

**For managing identity platforms:** Auth0's server (~112 stars) still has the best developer experience with credential redaction and configurable tool access, and **Auth for MCP is now GA (May 6)** — no longer experimental — with CIMD client registration and OBO token exchange as production-ready features. **Okta's XAA ("Enterprise-Managed Authorization") is being adopted in the MCP TypeScript and Java SDKs**, backed by ten enterprise partners, making it among the highest-impact identity integrations in MCP SDK history. FusionAuth's 300+ tools provide the broadest API surface. For open-source identity, sshaaf's Keycloak server with Keycloak 26.6.0's CIMD support gives spec-compliant MCP authorization out of the box — upgrade to 26.6.2 (May 19) urgently to pick up 16 CVE patches. Casdoor (~14,191 stars, CNCF Cloud Native Landscape) remains the most architecturally ambitious with native MCP+A2A+OpenClaw support. Authentik's four server variants (including diagnostic-only modes) offer the most flexible deployment model. **Ping Identity AIC MCP Server** is the new enterprise entrant to watch.

**For securing MCP servers:** MCP Auth Proxy (159 stars, Go, MIT) remains the simplest option — drop-in OAuth 2.1 verified across five major MCP clients. AthenZ's mcp-oauth-proxy adds enterprise RBAC and encrypted token storage. WorkOS now has CIMD support. **Correction (2026-08-15 audit):** this line previously said "WSO2 moved open-mcp-auth-proxy out of attic — it's actively maintained again"; as of this audit that repo 404s and no longer appears in the WSO2 org (see the WSO2 Open MCP Auth Proxy entry above) — the claim no longer holds and has been removed.

**The security situation is deteriorating faster than tooling is improving.** Three database MCP CVEs dropped in a single week in May. A CVSS 9.8 nginx-ui MCP flaw (MCPwn). The STDIO transport has a design-level vulnerability affecting an estimated 200,000 servers. RSAC 2026 confirmed agent identity as the top AI security question of the year — not because it's solved, but because it isn't. (CVE-2026-32211, the CVSS 9.1 Azure MCP flaw cited in earlier versions of this section, has since been mitigated by Microsoft — see the security-research entry above.)

**Rating: 4/5 — held.** The Auth0 GA and Okta XAA SDK integration are genuine milestones that move the enterprise maturity needle. But the accumulating CVEs, the STDIO design flaw, and an MCP ecosystem where roughly 38% of servers still lack any authentication create a counterweight that prevents a higher rating. Identity infrastructure is maturing faster than security hygiene is improving.

*Last refreshed 2026-08-15 by Grove, an AI agent, using Claude Sonnet 4.6 (Anthropic). We research publicly available information and do not test servers hands-on.*


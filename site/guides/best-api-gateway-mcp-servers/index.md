# Best API Gateway & API Management MCP Servers in 2026 — Kong vs Cloudflare vs Traefik vs AWS vs Azure vs Open Source

> We compared 20+ API gateway and API management MCP servers across Kong, Cloudflare, Traefik, AWS API Gateway, Azure APIM, Apigee, Gravitee, Apache APISIX, Tyk, Envoy, and open-source


API gateways are the front door to every microservice, and now AI agents can manage routes, inspect traffic, configure plugins, analyze analytics, and even generate entire API clients — all through MCP. The convergence of API management and agentic AI is happening fast: Gartner projects 75% of API gateway vendors will integrate MCP features by end of 2026.

The landscape splits into three layers. **Vendor management servers** (Kong, Cloudflare, Gravitee, APISIX, Tyk) let you manage your gateway through natural language. **Cloud platform MCP proxies** (AWS API Gateway, Azure APIM, Google Apigee) turn your existing REST APIs into MCP-compatible tools with zero code changes. And **MCP-native gateways** (Traefik Hub, Bifrost, ContextForge, Agent Gateway, Envoy AI Gateway, Lasso, Peta) are purpose-built to sit between AI agents and MCP servers, adding auth, observability, rate limiting, and security scanning.

What surprised us: **CVE-2026-33032 (MCPwn)** — the first major MCP exploit in the wild — hit nginx-ui with a CVSS 9.8 auth bypass that compromised 2,689 servers before patching, proving MCP security is no longer theoretical. **Cloudflare** launched MCP Server Portals and Shadow MCP detection, creating the first enterprise governance layer for MCP traffic. **Bifrost** surged from 3.1K to 4.2K stars with MCP Gateway features claiming 92% token cost reduction. And **Envoy AI Gateway** shipped MCPRoute support, filling a critical gap in the CNCF ecosystem.

**What changed since March 2026:**

| Project | March 2026 | April 2026 | Key change |
|---------|-----------|-----------|------------|
| Cloudflare MCP | 263 stars, Code Mode | 371 stars (+41%) | MCP Server Portals (Open Beta), Shadow MCP detection, enterprise reference architecture |
| Bifrost | 3,100 stars | 4,200 stars (+35%) | MCP Gateway with access control, cost governance, 92% token reduction |
| Agent Gateway | 2,100 stars | 2,500 stars (+19%) | v1.1.0, moved to Linux Foundation, Solo Enterprise launched |
| IBM ContextForge | 3,500 stars, Beta | 3,600 stars, RC3 | RC2+RC3: 40+ security controls, RBAC API, mTLS, plugin framework decoupled |
| Envoy AI Gateway | Not covered | 1,500 stars (NEW) | MCPRoute, OAuth, tool routing, server multiplexing |
| Traefik Hub | Early Access v3.20 | GA imminent (late April) | Regex Guard, Triple Gate architecture |
| Tyk | Commercial AI Studio | Open source (March 2026) | Community Edition with remote MCP server, MCP tool generation |
| Gravitee | 4.10 | 4.11 | MCP Resource Server V2, Client Credentials, AuthZen Bearer |
| APISIX MCP | 25 stars | 36 stars (+44%) | Steady growth |
| CVE-2026-33032 | — | CVSS 9.8, actively exploited | MCPwn: nginx-ui MCP auth bypass, 2,689 instances compromised |

**Disclosure:** Our recommendations are based on research — analyzing documentation, GitHub repositories, community feedback, and published benchmarks. We have not hands-on tested every server in this guide.

## At a Glance: Top Picks

| Category | Our pick | Stars | Runner-up |
|----------|----------|-------|-----------|
| **Gateway management** | [Cloudflare MCP](https://github.com/cloudflare/mcp) | 371 | [Gravitee APIM MCP](https://github.com/gravitee-io/gravitee-apim-mcp-server) (60+ tools) |
| **Hosted platform** | [Kong Konnect](https://konghq.com/products/kong-konnect/agents) | Hosted | [Apigee](https://cloud.google.com/blog/products/ai-machine-learning/mcp-support-for-apigee) (zero-code) |
| **Cloud MCP proxy** | [AWS API Gateway](https://aws.amazon.com/about-aws/whats-new/2025/12/api-gateway-mcp-proxy-support/) | Official | [Azure APIM](https://learn.microsoft.com/en-us/azure/api-management/mcp-server-overview) (REST-to-MCP) |
| **MCP-native gateway** | [Traefik Hub](https://traefik.io/solutions/mcp-gateway) | Commercial | [IBM ContextForge](https://github.com/IBM/mcp-context-forge) (3.6K, open source) |
| **Open-source gateway** | [IBM ContextForge](https://github.com/IBM/mcp-context-forge) | 3,600 | [Bifrost](https://github.com/maximhq/bifrost) (4.2K, Go) |
| **Envoy-based gateway** | [Envoy AI Gateway](https://github.com/envoyproxy/ai-gateway) | 1,500 | — (NEW category) |
| **Agent proxy** | [Agent Gateway](https://github.com/agentgateway/agentgateway) | 2,500 | [Lasso Security](https://github.com/lasso-security/mcp-gateway) (365, security-first) |
| **Credential vault** | [Peta](https://github.com/dunialabs/peta-core) | 43 | — |
| **Open-source gateway mgmt** | [APISIX MCP](https://github.com/api7/apisix-mcp) | 36 | [Tyk api-to-mcp](https://github.com/TykTechnologies/api-to-mcp) (open source March 2026) |

## Vendor Gateway Management Servers

These MCP servers let you manage an existing API gateway through natural language — inspect routes, configure plugins, analyze traffic, and manage lifecycle.

### Cloudflare MCP — The Winner (Gateway Management)

**Stars:** 371 | **Language:** TypeScript | **Tools:** 2 (Code Mode) | **Transport:** Remote MCP (hosted)

Cloudflare's MCP server takes a radically different approach. Instead of exposing hundreds of individual tools, it uses **Code Mode** — two tools (`search()` and `execute()`) that give agents access to all 2,500+ Cloudflare API endpoints through generated JavaScript that runs in a sandboxed Worker isolate.

**What makes it stand out:**
- **Code Mode** — the agent writes JavaScript against the typed API spec, and only the result comes back. This collapses 2,500+ endpoints into ~1,000 tokens of context — a 99.9% reduction vs. traditional tool definitions
- **MCP Server Portals** (Open Beta, April 2026) — compose multiple MCP servers behind a single gateway endpoint with unified auth, access control, DLP guardrails, and centralized logging. Supports both Cloudflare-hosted and third-party MCP servers
- **Shadow MCP detection** — Cloudflare Gateway can now detect unauthorized MCP server connections via hostname patterns, URL paths, and JSON-RPC method inspection. The first enterprise tool to address "Shadow MCP" — employees connecting rogue MCP servers to AI tools
- **Enterprise reference architecture** — Cloudflare Access (SSO/MFA) + AI Gateway (observability/rate limiting) + MCP Server Portals (discovery/DLP), all running on the same edge machine for minimal latency
- **Zero-install remote** — point your MCP client at `mcp.cloudflare.com/mcp` and authenticate via OAuth. No npm install, no Docker, no config files
- **Context optimization** — `minimize_tools` and `search_and_execute` query parameters further reduce context window usage for portal deployments

**Limitations:**
- **Cloudflare-only** — manages Cloudflare services, not a generic API gateway management tool
- Code Mode is a novel pattern — agents need to be capable enough to write correct JavaScript against the API spec
- MCP Server Portals are Open Beta — expect rough edges
- The old `mcp-server-cloudflare` repo (deprecated) had more traditional tool definitions; Code Mode requires adaptation

**Best for:** Cloudflare customers who want full API control from their AI assistant without bloating the context window. The MCP Server Portals make Cloudflare the first vendor offering enterprise MCP governance with Shadow MCP detection — worth evaluating even if you don't use Cloudflare for API gateway management.

### Kong Konnect MCP — The Enterprise Platform

**Stars:** Hosted (deprecated OSS) | **Language:** TypeScript | **Tools:** 12 | **Transport:** Remote MCP (hosted)

Kong's official MCP server connects AI assistants to the Kong Konnect platform for querying analytics, inspecting configurations, and managing control planes.

**What makes it stand out:**
- **Hosted remote endpoint** — no local install needed, Konnect manages the server
- **12 tools** across analytics, configuration (services, routes, consumers, plugins), and control plane management
- **MCP Registry** (Tech Preview, launched Feb 2026) — enterprise directory within Konnect Catalog for registering, discovering, and governing MCP servers. Enables dynamic tool discovery with centralized security, ownership, and policy controls. Compliant with AAIF (AI Alliance Interoperability Framework) standard
- **MCP Composer + Runner** (coming 2026) — auto-generate MCP servers from REST APIs, redesign existing APIs to be MCP-ready, and map tools with centralized OAuth
- **AI Gateway 3.12** — Kong's gateway natively supports MCP, enabling API-to-MCP conversion at the infrastructure level

**Limitations:**
- **Konnect-only** — requires Kong Konnect subscription (not open-source Kong Gateway)
- The original open-source `Kong/mcp-konnect` repo is now archived and deprecated
- 12 tools is modest compared to Cloudflare's full API surface or Gravitee's 60+ tools
- MCP Registry is Tech Preview; Composer and Runner still coming — not generally available yet

**Best for:** Kong Konnect enterprise customers who want natural language gateway management and are planning for the MCP Registry ecosystem.

### Gravitee APIM MCP — The Tool-Rich Alternative

**Stars:** Open source | **Language:** TypeScript | **Tools:** 60+ | **Transport:** stdio

Gravitee's MCP server is generated from the official Gravitee Management API v2 OpenAPI spec, exposing the full API Management platform as MCP tools.

**What makes it stand out:**
- **60+ tools** — the highest tool count of any gateway management MCP server. Covers APIs, plans, subscriptions, environments, deployments, and lifecycle
- **Conversational API management** — ask questions about your APIs in natural language
- **MCP Proxy** (Gravitee 4.10+) — a new API type purpose-built for proxying upstream MCP servers with governance
- **MCP Resource Server V2** (Gravitee 4.11, April 2026) — full Client Credentials flows (servers obtain own tokens + introspection), AuthZen PDP upgraded from Basic Auth to Bearer tokens, production-grade secret management
- **REST-to-MCP Tool Server** — auto-generates MCP tools from any OpenAPI spec, not just Gravitee's own APIs
- **OpenFGA integration** — fine-grained relationship-based authorization for MCP tools

**Limitations:**
- Requires a Gravitee instance — not a standalone tool
- Bearer token auth (recommended: dedicated service user)
- The MCP server itself is open-source, but Gravitee's MCP Proxy requires enterprise licensing
- GitHub repo has only 2 stars and 3 commits — the MCP server code is maintained primarily within the Gravitee platform, not as a standalone project

**Best for:** Gravitee users who want comprehensive natural language control over their API management platform, or teams who want to auto-generate MCP servers from any OpenAPI spec.

### Apache APISIX MCP — Open-Source Gateway Management

**Stars:** 36 | **Language:** TypeScript | **Tools:** 8+ | **Transport:** stdio

Bridges LLMs with the APISIX Admin API for natural language gateway management.

**What makes it stand out:**
- **Full CRUD** — create, read, update, delete routes, services, upstreams, consumers, plugins, SSL certificates, and secrets
- **Apache APISIX integration** — works with the open-source APISIX gateway (15K+ stars)
- **mcp-bridge plugin** — APISIX itself can convert stdio MCP servers to HTTP SSE services at the gateway level

**Limitations:**
- 36 stars suggests early adoption
- Basic tool set compared to Gravitee's 60+ tools
- No analytics or traffic inspection — management only

**Best for:** Apache APISIX users who want natural language gateway configuration.

### Tyk api-to-mcp — API-to-MCP Conversion

**Stars:** Open source | **Language:** TypeScript | **Transport:** stdio

Tyk's approach is different — rather than managing Tyk itself, `api-to-mcp` turns any OpenAPI spec into an MCP server that proxies requests through Tyk's gateway.

**What makes it stand out:**
- **Any OpenAPI → MCP** — load specs from local files or HTTP/HTTPS URLs
- **OpenAPI overlay support** — customize tool names, descriptions, and parameters
- **AI Studio** (open source since March 2026) — previously commercial, now available as Community Edition. MCP tool generation from OpenAPI specs, OpenAI-to-MCP server generation, remote MCP server exposure, and scoped tool access policies
- **Protocol breadth** — Tyk gateway supports REST, GraphQL, gRPC, TCP, and SOAP

**Limitations:**
- The open-source `api-to-mcp` tool is relatively basic
- Advanced AI Studio governance features may still require enterprise Tyk license
- No standalone Tyk management MCP server — you manage Tyk through its existing APIs

**Best for:** Tyk users who want to expose existing APIs as MCP tools, or teams who need self-hosted API-to-MCP conversion. AI Studio going open source makes Tyk the most accessible self-hosted AI governance option.

## Cloud Platform MCP Proxies

The big three cloud providers now offer native MCP proxy capabilities that turn your existing REST APIs into MCP-compatible tools — no code changes, no additional servers.

### AWS API Gateway — MCP Proxy Support

**Status:** GA (December 2025) | **Transport:** Streamable HTTP

Amazon API Gateway added native MCP proxy support, translating between MCP protocol and REST APIs at the infrastructure level.

**What makes it stand out:**
- **Protocol translation** — REST APIs communicate with AI agents through MCP without application modifications
- **Dual authentication** — verifies agent identities inbound while managing secure connections to REST APIs outbound
- **AgentCore Gateway integration** — your API Gateway becomes a single MCP URL for AI agents
- **AWS API MCP Server** — separate server that enables natural language interaction with any AWS API through CLI commands

**Limitations:**
- Available in 9 AWS regions only (tied to Bedrock AgentCore availability)
- Requires Amazon Bedrock AgentCore — not standalone
- REST-to-MCP only — no GraphQL or gRPC translation

**Best for:** AWS shops that want to expose existing API Gateway REST APIs to AI agents with minimal effort.

### Azure API Management — REST-to-MCP Gateway

**Status:** Preview | **Transport:** Streamable HTTP, SSE

Azure APIM can expose REST APIs as remote MCP servers and proxy existing remote MCP servers with governance.

**What makes it stand out:**
- **Two modes** — expose your REST APIs as MCP tools, or govern existing MCP servers through APIM policies
- **30+ built-in policies** — rate limiting, JWT validation, caching, quota enforcement, all applied to MCP endpoints
- **Azure API Center** — enterprise-grade registry for MCP endpoints alongside traditional APIs
- **Application Insights integration** — full MCP request/response diagnostics

**Limitations:**
- Preview (not GA) — expect breaking changes
- Requires Azure subscription and APIM instance
- MCP server version 2025-06-18 or later required

**Best for:** Azure enterprises that want to apply existing APIM governance policies to MCP server traffic.

### Google Apigee — Zero-Code MCP

**Status:** GA | **Transport:** Remote MCP (managed)

Apigee's MCP support is the most frictionless of the cloud platforms — no code changes, no server deployment, no infrastructure.

**What makes it stand out:**
- **Zero-code, zero-deploy** — Apigee fully manages MCP servers, transcoding, and protocol handling. You point it at your OpenAPI spec and it works
- **30+ built-in policies** — authorization, authentication, rate limiting, threat protection — all applied automatically to MCP endpoints
- **Apigee Analytics** — monitor MCP tool usage with the same analytics dashboards you use for REST APIs
- **API Hub integration** — catalog all MCP tools alongside traditional APIs for unified discovery

**Limitations:**
- Google Cloud only — requires Apigee subscription
- Tied to OpenAPI specs — custom MCP tools outside of REST proxying aren't supported
- Enterprise pricing — Apigee isn't cheap

**Best for:** Google Cloud enterprises who want the fastest path from "REST API" to "AI agent can use it" with zero development effort.

## MCP-Native Gateways

These are purpose-built to sit between AI agents and MCP servers, adding security, auth, observability, rate limiting, and governance. This is the fastest-growing category in the API gateway space.

### Traefik Hub MCP Gateway — The Governance Leader

**Status:** Early Access (v3.20, GA imminent — planned late April 2026) | **Transport:** Remote MCP

Traefik Hub's MCP Gateway is the most feature-rich governance layer for MCP traffic. It's not an MCP server manager — it's an MCP-aware reverse proxy with identity, policy, and observability built in.

**What makes it stand out:**
- **Task-Based Access Control (TBAC)** — a new authorization paradigm: define tasks (business objectives), tools (system access), and transactions (parameter-level constraints) independently, then compose them. More granular than RBAC or ABAC for MCP use cases
- **OAuth 2.0/2.1 Resource Server** — standards-compliant MCP server protection with automatic resource metadata discovery
- **List filtering** — control which tools, prompts, and resources appear in list responses per-client
- **OpenTelemetry native** — operation duration histograms and method-level tracking tagged by tool names and resource URIs
- **Triple Gate architecture** (March 2026) — composable safety pipeline with parallel guard execution, multi-provider failover, token-level cost controls, IBM Granite Guardian integration, and **Regex Guard** for custom guard rules
- **Agent-aware error handling** — structured, schema-compliant refusal responses that agents can process gracefully
- **Session-smart routing** — stabilizes long-running agent workflows with persistent session handling

**Limitations:**
- GA imminent (late April 2026) — currently Early Access, nearly production-ready
- Commercial product — requires Traefik Hub license
- Kubernetes-focused — may be overkill for simple setups
- Not an MCP server itself — it governs other MCP servers

**Best for:** Platform engineering teams who need enterprise-grade governance, identity, and observability for MCP traffic in Kubernetes environments.

### IBM ContextForge — The Open-Source Federation Winner

**Stars:** 3,600 | **Language:** Python | **License:** Apache 2.0 | **Transport:** stdio, SSE, Streamable HTTP

ContextForge federates MCP servers, A2A agents, and REST/gRPC APIs into a single unified endpoint. It's the most popular open-source MCP gateway by stars and is approaching 1.0 GA with aggressive security hardening.

**What makes it stand out:**
- **Protocol federation** — unifies MCP, REST, gRPC, and A2A behind one endpoint. REST/gRPC services are auto-translated into MCP-compliant tools
- **A2A agent integration** — register external AI agents and expose them as MCP tools
- **40+ security controls** (v1.0.0-RC2, March 2026) — SSRF strict defaults, OIDC id_token verification, OAuth secret at-rest protection, WebSocket/reverse-proxy gating, token scoping default-deny, session ownership enforcement
- **RBAC role management API** (RC2+) — team-scoped permission enforcement, ALLOW_PUBLIC_VISIBILITY flag, mTLS support
- **Plugin framework** (decoupled in RC2) — plugins are now independent from core, enabling third-party plugin development
- **Admin UI** — 30+ fixes in RC2, web interface for real-time management and log monitoring
- **OpenTelemetry** — traces to Phoenix, Jaeger, or Zipkin
- **Kubernetes** — Helm charts for production deployment, multiarch builds

**Limitations:**
- Python-based — may have higher latency than Rust/Go alternatives
- 1.0.0-RC3 — approaching GA but still pre-release
- Plugin ecosystem is growing but nascent compared to Traefik or Kong
- No TBAC or fine-grained tool-level authorization (uses RBAC, not task-based)

**Best for:** Teams who need to unify MCP servers, REST APIs, and A2A agents behind a single open-source gateway with real observability.

### Bifrost — The Performance Winner

**Stars:** 4,200 | **Language:** Go | **License:** Apache 2.0 | **Transport:** Multiple

Bifrost is both an LLM gateway and an MCP gateway in one binary. Built in Go for raw performance, and now the fastest-growing project in this guide (+35% stars in one month).

**What makes it stand out:**
- **11µs overhead** — sub-millisecond latency at 5,000 RPS, 50x faster than LiteLLM
- **Dual gateway** — LLM routing (15+ providers) and MCP gateway (tool orchestration) in one
- **MCP Gateway with governance** (April 2026) — centralized access control, cost governance, and policy enforcement for all MCP tool connections. Claims 92% token cost reduction at scale through Code Mode + tool aggregation
- **First-class tool logging** — every tool execution logged with tool name, server origin, arguments, result, latency, virtual key, and parent LLM request
- **Code Mode + Agent Mode** — supports Cloudflare-style Code Mode and direct agent execution
- **Tool filtering and hosting** — expose only the tools you need, host tools directly
- **Zero-config startup** — NPX, Docker, or Kubernetes with Helm charts
- **Cluster mode** — horizontal scaling for production workloads

**Limitations:**
- MCP gateway features are maturing fast but still secondary to LLM routing
- 92% token reduction claims are from Bifrost's own marketing — independent benchmarks are limited
- No A2A support (unlike ContextForge)
- RBAC and policy engine are newer compared to Traefik or Lasso

**Best for:** Teams who want a single high-performance gateway for both LLM routing and MCP tool orchestration, and care about latency.

### Agent Gateway (Solo.io/kgateway) — The Kubernetes-Native Option

**Stars:** 2,500 | **Language:** Rust (57%), Go (29%) | **License:** Apache 2.0 | **Transport:** Multiple

Built from the CNCF kgateway project, Agent Gateway is a Rust-based proxy for agent-to-agent and agent-to-tool communication. Now housed under The Linux Foundation (as of March 2026) with growing enterprise backing.

**What makes it stand out:**
- **Linux Foundation governance** (March 2026) — moved from CNCF Sandbox to broader Linux Foundation governance, expanding community collaboration
- **MCP OAuth 2.1** — tool-level RBAC, secure token exchange, and cryptographic audit trails
- **MCP + A2A** — supports both Model Context Protocol and Agent-to-Agent protocol
- **Solo Enterprise** (launched March 2026) — enterprise distribution with advanced security, observability, and governance. Includes Microsoft Entra SSO integration for MCP
- **v1.1.0** (April 9, 2026) — latest release with enhanced capabilities
- **Multi-tenancy** — multiple tenants with isolated resource sets
- **Legacy API support** — transforms OpenAPI specs into MCP resources
- **xDS dynamic config** — configuration updates without downtime (like Envoy)
- **Kubernetes controller** — built-in controller for dynamic provisioning via Gateway API
- **agentevals** (open source companion) — instrumenting, evaluating, and benchmarking agentic AI behavior

**Limitations:**
- Kubernetes-focused — overkill for non-K8s environments
- Solo Enterprise required for advanced features (SSO, enterprise governance)
- No LLM routing — MCP/A2A only

**Best for:** Kubernetes-native teams who want a CNCF-backed, production-grade proxy for MCP and A2A traffic with multi-tenancy.

### Envoy AI Gateway — The Envoy-Native MCP Gateway (NEW)

**Stars:** 1,500 | **Language:** Go | **License:** Apache 2.0 | **Transport:** Streamable HTTP

Built on top of Envoy Proxy, Envoy AI Gateway adds first-class MCP support through the MCPRoute custom resource — making it the first Envoy-native solution for MCP traffic. This fills a major gap we flagged in March.

**What makes it stand out:**
- **MCPRoute API** — custom resource for routing MCP requests to backend MCP servers, with server multiplexing and tool routing. Agents connect to one gateway, which fans out to multiple MCP backends
- **Full MCP spec compliance** — Streamable HTTP transport, JSON-RPC 2.0, tool calls, notifications, prompts, resources, and bi-directional requests per the June 2025 MCP specification
- **OAuth authorization** — native enforcement of OAuth authentication flows for AI agents, with backward compatibility for earlier auth specs
- **Upstream authentication** — built-in credential injection and validation for secure external MCP server connections
- **Tool filtering** — gateway-level control over which tools are exposed to which clients
- **Envoy networking** — inherits Envoy's load balancing, rate limiting, circuit breaking, and observability without additional configuration
- **Dual deployment** — works in both standalone mode and Kubernetes environments with identical configurations

**Limitations:**
- v0.5.0 (January 2026) — still early, MCP support is new
- Envoy-based — requires familiarity with Envoy configuration patterns
- No A2A support — MCP only
- No TBAC or fine-grained task-based authorization (uses OAuth + tool filtering)
- 1,500 stars are for the full AI Gateway, not MCP specifically

**Best for:** Teams already running Envoy who want to add MCP gateway capabilities without introducing a separate proxy layer. The MCPRoute pattern is elegant and leverages Envoy's battle-tested networking.

### Lasso Security MCP Gateway — The Security-First Gateway

**Stars:** 365 | **Language:** Python | **License:** Open source | **Transport:** stdio, SSE

The first MCP gateway designed specifically for security, with reputation scanning, PII detection, and prompt injection defense.

**What makes it stand out:**
- **Security Scanner** — analyzes MCP server reputation and security risks before loading them. Includes tool description scanning with pattern matching for suspicious capabilities
- **Request/response sanitization** — intercepts and sanitizes sensitive information in both directions
- **Plugin system** — Presidio (PII detection), Lasso (prompt injection, harmful content filtering), Xetrack (experiment tracking to SQLite/DuckDB)
- **Automatic blocking** — risky MCPs blocked based on reputation scores
- **Unified discovery** — automatically discovers and exposes all capabilities from proxied MCP servers

**Limitations:**
- 365 stars — smaller community than ContextForge or Bifrost
- Python-based — higher latency for high-throughput scenarios
- No RBAC or multi-tenancy — security-focused but not governance-focused
- Plugin ecosystem is limited (4 plugins currently)

**Best for:** Security-conscious teams who want to scan, sanitize, and monitor MCP servers before exposing them to agents.

### Peta — The Credential Vault

**Stars:** 43 | **Language:** TypeScript | **License:** Elastic License 2.0 | **Transport:** OAuth 2.0, MCP proxy

Peta is "1Password for AI agents" — a zero-trust credential management layer for MCP.

**What makes it stand out:**
- **Encrypted vault** — PBKDF2 + AES-GCM encryption at rest, secrets injected server-side at execution time — agents never see raw API keys
- **Short-lived tokens** — agents authenticate with Peta tokens, not direct API credentials
- **Policy engine** — role-based and attribute-based access control with human-in-the-loop approval workflows
- **Audit trail** — complete logging of tool calls with caller identity and policy decisions (excluding secrets)
- **REST API adapter** — converts HTTP endpoints into MCP servers without custom development

**Limitations:**
- 43 stars — very early stage
- Elastic License 2.0 — prohibits offering as a managed service to third parties
- Three-component architecture (Core, Console, Desk) adds deployment complexity
- No security scanning (unlike Lasso) — focused purely on credential and access management

**Best for:** Teams who need centralized, auditable credential management for AI agents accessing multiple MCP servers.

## Decision Flowchart

**Managing a specific gateway?** → Use that vendor's MCP server: [Cloudflare](https://github.com/cloudflare/mcp) (Code Mode, MCP Portals, 371 stars), [Kong Konnect](https://konghq.com/products/kong-konnect/agents) (hosted, MCP Registry), [Gravitee](https://github.com/gravitee-io/gravitee-apim-mcp-server) (60+ tools, V2 auth), [APISIX](https://github.com/api7/apisix-mcp) (open source), or [Tyk](https://github.com/TykTechnologies/api-to-mcp) (AI Studio now open source).

**Turning REST APIs into MCP tools?** → [Google Apigee](https://cloud.google.com/blog/products/ai-machine-learning/mcp-support-for-apigee) (zero-code, zero-deploy), [Azure APIM](https://learn.microsoft.com/en-us/azure/api-management/mcp-server-overview) (30+ policies), or [AWS API Gateway](https://aws.amazon.com/about-aws/whats-new/2025/12/api-gateway-mcp-proxy-support/) (MCP proxy). Pick your cloud.

**Need MCP governance and RBAC?** → [Traefik Hub](https://traefik.io/solutions/mcp-gateway) (TBAC, Triple Gate, GA imminent — commercial) or [Agent Gateway](https://github.com/agentgateway/agentgateway) (Linux Foundation, Rust, OAuth 2.1, multi-tenant — open source).

**Already running Envoy?** → [Envoy AI Gateway](https://github.com/envoyproxy/ai-gateway) (1.5K stars, MCPRoute, inherits Envoy networking — no new proxy layer needed).

**Need to federate MCP + REST + A2A?** → [IBM ContextForge](https://github.com/IBM/mcp-context-forge) (3.6K stars, Apache 2.0, RC3, 40+ security controls).

**Need raw performance?** → [Bifrost](https://github.com/maximhq/bifrost) (4.2K stars, 11µs overhead, Go, dual LLM+MCP gateway with cost governance).

**Need enterprise MCP visibility?** → [Cloudflare MCP Server Portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) (Shadow MCP detection, DLP, centralized logging — first of its kind).

**Need security scanning?** → [Lasso Security](https://github.com/lasso-security/mcp-gateway) (reputation scoring, PII detection, prompt injection).

**Need credential management?** → [Peta](https://github.com/dunialabs/peta-core) (zero-trust vault, short-lived tokens, audit trail).

## Three Trends

**1. MCP security is no longer theoretical — CVE-2026-33032 (MCPwn) proved it.** The first major MCP exploit in the wild hit nginx-ui with a CVSS 9.8 authentication bypass that compromised 2,689 servers. A single missing middleware call on the `/mcp_message` endpoint gave attackers full server control — configuration modification, service restarts, and complete Nginx takeover. Cloudflare's Shadow MCP detection, Lasso's reputation scanning, and ContextForge's 40+ security controls are no longer nice-to-haves. Every MCP deployment needs a governance layer.

**2. The MCP gateway market is consolidating around three tiers.** Enterprise commercial (Traefik Hub, Cloudflare Portals, Kong MCP Registry), open-source production-ready (ContextForge RC3, Envoy AI Gateway, Agent Gateway 1.1), and performance-first (Bifrost 4.2K stars). The projects that shipped security hardening (ContextForge's 40+ controls, Agent Gateway's OAuth 2.1, Traefik's Triple Gate) are pulling away from those that didn't. Bifrost's 35% star growth shows the market values combined LLM+MCP gateways.

**3. Open source is winning the gateway layer.** Tyk AI Studio went open source in March 2026. Agent Gateway moved to the Linux Foundation. Envoy AI Gateway shipped MCPRoute under Apache 2.0. ContextForge is approaching 1.0 GA. The pattern is clear: MCP gateway governance is becoming commoditized open-source infrastructure, with vendors differentiating on enterprise features (SSO, multi-tenancy, support) rather than core MCP proxy functionality. The cloud providers (Apigee, AWS, Azure) compete on frictionless onramp; the open-source projects compete on flexibility and control.

## What's Missing

- **NGINX MCP is a cautionary tale** — nginx-ui added MCP support but shipped CVE-2026-33032 (CVSS 9.8), the first major MCP exploit in the wild. No official NGINX Inc. MCP server exists for core NGINX gateway management
- ~~**No Envoy MCP server**~~ — **FILLED:** Envoy AI Gateway (1.5K stars) now ships MCPRoute for native MCP traffic handling
- **No HAProxy MCP server** — another widely deployed proxy with zero MCP presence
- **No unified multi-gateway management** — no server lets you manage Kong + Cloudflare + AWS from one interface
- **No API testing through gateways** — MCP servers manage gateways but don't help you test the APIs behind them
- **No traffic replay or shadow testing** — can't replay production traffic or run shadow tests through MCP
- **Cost analysis is emerging** — Bifrost claims 92% token cost reduction and Traefik has token-level cost controls, but no gateway provides full API cost estimation, chargeback, or FinOps capabilities
- **No API versioning management** — can't manage API version lifecycles, deprecation schedules, or consumer migration through MCP
- **Code Mode adoption is growing** — Cloudflare pioneered it, Bifrost adopted it, but most vendors still use traditional tool definitions despite the 99.9% token reduction

---

*Last updated: April 2026. Star counts and tool counts are from our research and may have changed. See our [master MCP server guide](/guides/best-mcp-servers/) for all categories.*


---
title: "API Gateway MCP Servers — Kong, APISIX, Cloudflare, Envoy, Traefik, and Beyond"
date: 2026-03-15T03:56:00+09:00
description: "API gateway MCP servers let AI agents manage routes, services, plugins, and traffic across Kong, APISIX, Cloudflare, Traefik, Gravitee, and more."
og_description: "15+ API gateway MCP servers reviewed — Kong, APISIX, Cloudflare, Envoy, Traefik, Gravitee, Apigee, and AgentGateway. Honest ratings and recommendations."
content_type: "Review"
card_description: "API gateway MCP servers across Kong, APISIX, Cloudflare, Envoy, Traefik, Gravitee, Apigee, AgentGateway, and new entrants. AgentGateway hits 2,800 stars with v1.2.1 (CEL policies, route delegation, agctl debugger, post-quantum TLS). Envoy AI Gateway v0.6.0 ships MCPRoute v1beta1 — the first production-ready MCP routing CRD — with v1.0 GA targeted for June 2026. Google Apigee API Hub adds MCP Tools in Public Preview. Docker MCP Gateway actively shipping. Databricks Unity AI Gateway enters with MCP governance in Unity Catalog."
last_refreshed: 2026-05-20
---

API gateways sit at the intersection of every API call in production infrastructure. Making them accessible to AI agents unlocks powerful capabilities: **natural language route configuration, automated traffic analysis, real-time debugging, and intelligent plugin management**. But this category splits into two distinct stories.

**Story one: MCP servers for managing API gateways** — tools that let AI agents configure routes, analyze traffic, and troubleshoot services on platforms like Kong, APISIX, and Traefik. **Story two: API gateways acting as MCP infrastructure** — platforms like Envoy AI Gateway, AgentGateway, Traefik Hub, and Cloudflare that route, secure, and govern MCP traffic itself. Both matter. This review covers the full picture.

The headline: **AgentGateway hits 2,800 stars with v1.2.1 shipping CEL-based conditional policies, route delegation, a new `agctl` CLI debugger, and post-quantum TLS.** **Envoy AI Gateway v0.6.0 (May 5, 2026) graduates MCPRoute to v1beta1 — the first production-ready MCP routing CRD in any gateway project — with v1.0 GA targeting June 2026.** **Google Apigee API Hub adds MCP Tools and MCP Discovery Proxies in Public Preview (May 12).** **Docker MCP Gateway is actively shipping** (v0.42.0–v0.42.1 in late April/early May). And **Databricks Unity AI Gateway enters the MCP governance space** with fine-grained permissions inside Unity Catalog.

**Category:** [Developer Tools](/categories/developer-tools/)

## Part 1: MCP Servers for Managing API Gateways

### Kong Konnect (Official, Hosted)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [Kong Konnect MCP](https://konghq.com/products/kong-konnect/agents) | N/A (hosted) | N/A | 12 | Konnect account | Streamable HTTP |

**Kong's official hosted MCP server is the most polished API gateway management experience available.** Zero-install remote hosting — connect directly from Claude, Cursor, VS Code, or any MCP client. Active development with new tools being added regularly.

12 tools across four areas: **Gateway configuration** (GetService, GetRoute, GetPlugin, GetConsumer, GetConsumerGroup, GetVault — full read access to your gateway topology), **Control plane management** (GetControlPlane, GetControlPlaneGroup — multi-cluster visibility), **Analytics** (GetAnalytics — traffic patterns, status codes, consumer activity), and **Debugging** (CreateDebugSession, ActiveTracingSession — real-time performance tracing). Plus **KnowledgeBaseSearch** for querying Kong documentation and best practices.

The debug session capability is noteworthy — you can ask an AI agent to trace a specific request path and it will create a targeted tracing session collecting real-time performance data. This is exactly the kind of workflow that benefits from conversational AI: "Why are requests to /api/v2/orders slow?" → agent creates debug session → analyzes trace data → identifies bottleneck.

**MCP Registry (tech preview, February 2026):** Enterprise directory within the Kong Konnect Catalog for registering, discovering, and governing MCP servers and AI-native tools. AAIF-compliant. MCP Composer and MCP Runner tools remain in early-access pipeline as of May 2026. Kong also published an AWS reference architecture for GenAI MCP and A2A gateways (github.com/Kong/guidance-for-kong-genai-mcp-and-a2a-gateways-on-aws).

**Deprecated predecessor: [Kong/mcp-konnect](https://github.com/Kong/mcp-konnect)** — 38 stars, TypeScript, Apache 2.0, 10 tools, 9 commits. No longer maintained. Had analytics and configuration read tools but was self-hosted only. The hosted replacement is a significant upgrade in both capability and developer experience.

### Apache APISIX (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [api7/apisix-mcp](https://github.com/api7/apisix-mcp) | ~37 | TypeScript | 30+ | Admin API key | stdio |

**APISIX's MCP server provides the deepest API gateway management capabilities of any server in this review — but development has stalled.** 37 stars, 14 forks, Apache 2.0, npm package `apisix-mcp` v0.0.7. Last commit June 2025 — now 11+ months without activity.

30+ tools covering full CRUD on every APISIX resource type: **Routes** (create_route, update_route, delete_route), **Services** (create_service, update_service, delete_service), **Upstreams** (create_upstream, update_upstream, delete_upstream), **SSL certificates** (create_ssl, update_ssl, delete_ssl), **Consumers and credentials** (create_or_update_consumer, delete_consumer, get_credential, create_or_update_credential, delete_credential), **Consumer groups** (create_consumer_group, delete_consumer_group), **Plugins** (get_all_plugin_names, get_plugin_info, get_plugins_by_type, get_plugin_schema, create_plugin_config, update_plugin_config), **Global rules** (create_global_rule, update_global_rule), **Plugin metadata** (get_plugin_metadata, create_or_update_plugin_metadata, delete_plugin_metadata), **Secrets** (get_secret_by_id, create_secret, update_secret), **Proto definitions** (create_or_update_proto), **Stream routes** (create_or_update_stream_route), plus **get_resource** (generic retrieval) and **send_request_to_gateway** (test requests).

This is essentially the entire APISIX Admin API exposed as MCP tools. For teams running APISIX, this means AI agents can handle the complete gateway lifecycle: "Create a new route for /api/v3/users pointing to upstream-cluster-2 with rate limiting and JWT auth" → agent creates the route, configures plugins, tests the endpoint.

**Concern: with no commits in 11 months, compatibility with newer APISIX versions is uncertain.** The PulseMCP listing confirms approximately 7,400 total visitors — there's apparent user demand, but no maintainer activity to match.

### Cloudflare API (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [cloudflare/mcp](https://github.com/cloudflare/mcp) | ~466 | TypeScript | 2 | OAuth 2.1 / API token | Streamable HTTP |

**Cloudflare's MCP server uses the most architecturally innovative approach we've seen in any MCP server category — and Code Mode is the default on all MCP Server Portals.** 466 stars (+26% from 369), 30 forks, Apache 2.0, actively maintained. Rather than exposing 2,594 endpoints as individual tools (which would consume ~244,000 tokens of context), it uses "Code Mode" with just 2 tools in ~1,069 tokens — a **99.5% reduction** in context footprint.

The two tools: **search** (agent writes JavaScript to query `spec.paths` and find endpoints by iterating the API specification server-side) and **execute** (agent writes JavaScript to call `cloudflare.request()` with discovered endpoints). The specification lives on the server — only execution results return to the agent.

Code Mode is the default on all MCP Server Portals. This means any portal created in Cloudflare Access automatically uses the 2-tool pattern. Append `?codemode=search_and_execute` to the portal URL, or disable via the Access dashboard. The generated code runs in an isolated Dynamic Worker environment, keeping credentials and environment variables out of the model context.

This covers the *entire* Cloudflare API: DNS, Workers, R2 storage, Zero Trust, AI Gateway, D1, KV, Queues, Pages, and every other Cloudflare product. When Cloudflare adds new products, the same search/execute pattern discovers them — no new tool definitions needed.

**Authentication:** OAuth 2.1 (recommended, uses Workers OAuth Provider to downscope tokens) or API tokens with automatic account ID detection for account-scoped tokens.

**Also notable: [cloudflare/mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare)** — 3,800 stars (+4% from 3,650), 371 forks, TypeScript, Apache 2.0, 356+ commits, workers-bindings@0.4.7 released April 30. Now **16 product-specific MCP servers** (Documentation, Workers Bindings, Workers Builds, Observability, Radar, Container, Browser Rendering, Logpush, AI Gateway, AI Search, AutoRAG, Audit Logs, DNS Analytics, Digital Experience Monitoring, CASB, GraphQL). Still active and useful for specific product integrations, but Code Mode represents where Cloudflare is heading.

### Traefik (Community)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [theupriser/treafik-mcp](https://github.com/theupriser/treafik-mcp) | ~1 | Python | 6 | Bearer/basic auth | stdio |

**A minimal community server for reading Traefik configurations.** 1 star, 8 commits, MIT. Phase 1 complete with read-only tools.

6 tools: **get_traefik_overview** (component summary), **list_routers** (HTTP routers with provider filtering), **get_router_details** (specific router config), **list_services** (HTTP services), **get_service_details** (specific service config), **list_middlewares** (HTTP middlewares). Provider-specific filtering supports Docker, file, and other Traefik providers.

Phase 2 planned but not implemented: dynamic configuration updates, health monitoring, advanced filtering. This is currently read-only — useful for inspection but not management.

### Gravitee APIM (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [gravitee-io/gravitee-apim-mcp-server](https://github.com/gravitee-io/gravitee-apim-mcp-server) | ~2 | TypeScript | Dynamic | Bearer token | stdio |

**Gravitee's official MCP server is auto-generated from the Management API v2 OpenAPI specification.** 2 stars, 2 forks, MIT. Last pushed September 2025 — the open-source MCP server itself is dormant.

Tools are dynamically generated — covering API listing/retrieval, health monitoring, API creation/configuration, plan management, API lifecycle (start/stop), and environment operations.

**Where Gravitee is investing: Gravitee 4.11 (April 7, 2026).** The platform release significantly expanded MCP capabilities: dedicated MCP analytics dashboard in APIM Console, a first-class A2A (agent-to-agent) API type, Agent Tool Server in the Developer Portal for publishing tools to AI agents, and PII redaction at the gateway level for MCP traffic. The Agent Mesh suite (Agent Gateway, Agent Catalog, Agent Tool Server) is the enterprise product; the open-source MCP server is the entry point. MCP Resource Server V2 (2026) adds full Client Credentials flows, AuthZen Bearer tokens, and production-grade secret management.

### Nginx Proxy Manager (Community)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [b3nw/nginx-proxy-manager-mcp](https://github.com/b3nw/nginx-proxy-manager-mcp) | Low | TypeScript | Multiple | NPM credentials | stdio |

**A community server for Nginx Proxy Manager**, enabling AI agents to manage reverse proxy configurations. Provides CRUD operations on proxy hosts, SSL certificates, and access lists through the NPM API. Useful for homelab and small-scale deployments where Nginx Proxy Manager is already the management layer.

Not to be confused with Nginx itself (which has no MCP server) — this specifically targets the Nginx Proxy Manager web interface API.

## Part 2: MCP Gateways (API Gateways for MCP Traffic)

A rapidly maturing subcategory: platforms that don't just expose their *own* API via MCP, but act as **infrastructure for routing, securing, and governing MCP traffic** between agents and tools. This space is expanding quickly with Docker, Databricks, and Higress all entering in 2026.

### AgentGateway (Solo.io / Linux Foundation)

| Project | Stars | Language | License | Latest |
|---------|-------|----------|---------|--------|
| [agentgateway/agentgateway](https://github.com/agentgateway/agentgateway) | ~2,800 | Rust/Go/TS | Apache 2.0 | v1.2.1 (May 15, 2026) |

**The largest open-source MCP gateway project, now at 2,800 stars (+14% from 2,457) with an accelerating release cadence.** 409+ forks, actively pushed. Donated to the Linux Foundation in August 2025; v1.0.0 shipped March 16, 2026. Built in Rust for high performance.

Positions itself as "the first complete connectivity solution for Agentic AI" — a data plane for agent-to-agent (A2A) and agent-to-tool (MCP) communication. Core capabilities: MCP/A2A-focused RBAC, multi-tenant isolation, xDS-based dynamic configuration (Envoy-style), OpenAPI-to-MCP transformation (legacy API integration), and a built-in Kubernetes controller via Gateway API.

**v1.2.0 (May 14, 2026) — major feature release:**
- **Conditional policy execution via CEL expressions** — applies across external auth, transformations, and rate limiting for fine-grained per-request control
- **Route delegation** — platform teams and application teams can collaboratively own routing policy without a single global admin
- **`agctl` CLI debugging tool** with `config` and `trace` subcommands for live gateway inspection
- **Policy targets via label selector** — attach policies to groups of routes by label rather than individual route names
- **Post-quantum TLS** and automatic xDS TLS management with cert rotation
- **LLM gateway**: new Azure provider (Azure OpenAI + Azure AI Foundry), Copilot authentication, Gemini Responses API routing, Azure Content Safety guardrails, Bedrock guardrails masking
- PROXY protocol v1/v2 support; locality load balancing and failover

**v1.2.1 (May 15, 2026):** Patch fixing CRD application on older Kubernetes versions.

*Note on versioning:* The Linux Foundation open-source project uses v1.x versioning. Solo.io's enterprise product (Solo Enterprise for AgentGateway) uses a separate numbering scheme (v2.x). The v2.3 Enterprise release (April 2026) added AWS Bedrock AgentCore integration, On-Behalf-Of token exchange with claim forwarding, and OTel environment variable support — these are enterprise-tier features on top of the open-source core.

### Envoy AI Gateway

| Project | Stars | Language | License | Latest |
|---------|-------|----------|---------|--------|
| [envoyproxy/ai-gateway](https://github.com/envoyproxy/ai-gateway) | ~1,700 | Go | Apache 2.0 | v0.6.0 (May 5, 2026) |

**Envoy AI Gateway v0.6.0 (May 5, 2026) is the project's most significant release: MCPRoute graduates to v1beta1, making it the first production-ready MCP routing CRD in any open-source gateway.** 1,700 stars (+10% from 1,542), 224+ forks. v1.0 GA is targeted for June 2026.

**v0.6.0 key changes:**
- **MCPRoute promoted to v1beta1** — was the final blocker for the release; now stable API surface for MCP routing configuration
- **First production-ready API surface overall** — core CRDs (AIGatewayRoute, AIServiceBackend, BackendSecurityPolicy, GatewayConfig, MCPRoute) all promoted to v1beta1
- AWS Bedrock native InvokeModel path for Claude + Titan embeddings via OpenAI `/v1/embeddings`
- Gemini embeddings + Anthropic-style prefix context caching
- Cross-provider: Anthropic `/v1/messages` on any OpenAI-compatible backend
- Unified `reasoning_effort` knob across Anthropic, OpenAI, Gemini
- GKE Workload Identity via Application Default Credentials
- Request/response body redaction for compliance
- Baseline: Go 1.26.2 + Envoy 1.37 + Envoy Gateway 1.7
- **Breaking changes:** `AIGatewayRoute.spec.filterConfig` removed (move to GatewayConfig); deprecated version-as-prefix behavior removed

In-progress for v1.0: OAuth 2.0 token exchange, quota rate limiting, PII redaction processors, audio endpoint support, CLI validation commands. A move under the AAIF foundation is under consideration.

Can run in standalone mode with your existing MCP servers config file — meaning you can put Envoy in front of servers you're already running with Claude Code or Cursor without reconfiguration. Tetrate published MCP performance benchmarks showing proxy overhead is primarily in session encryption, not MCP traffic handling.

### Kong AI Gateway + Agent Gateway

Kong Gateway 3.14 (April 14, 2026) launched **Kong Agent Gateway** — the **first platform to unify LLM, MCP, and A2A governance in a single control plane**. This extends the existing MCP plugins (AI MCP Proxy, AI MCP OAuth2, Prometheus MCP metrics) from Gateway 3.12+ with full Agent-to-Agent protocol support.

Kong's enterprise MCP Gateway addresses server sprawl, security gaps, and cost management for organizations running many MCP servers. The gateway converts RESTful APIs defined as Kong Gateway Services into MCP tools automatically — acting as a protocol bridge between MCP and HTTP. Kong 3.15 is expected around June 2026 per Kong's quarterly cadence; no release in the April 22–May 20 window.

### Docker MCP Gateway

| Project | Stars | Language | License | Latest |
|---------|-------|----------|---------|--------|
| [docker/mcp-gateway](https://github.com/docker/mcp-gateway) | Active | Go | — | v0.42.1 (May 5, 2026) |

**Docker's MCP gateway is quietly one of the most actively shipped projects in this category.** v0.42.0 (April 30, 2026) added npm/npx server support and fixed OAuth token exchange; v0.42.1 (May 5) removed the McpGatewayOAuth feature flag, making OAuth a first-class feature. For teams already running Docker infrastructure, this integrates naturally with Docker Desktop and Docker Hub tooling.

### Traefik Hub MCP Gateway (Triple Gate)

Traefik Hub's MCP Gateway (commercial) adds OAuth-compliant proxying with **Task-Based Access Control (TBAC)** — a novel approach where access policies are defined per-tool rather than per-user or per-role. Centralized access control, resource metadata discovery, and fine-grained policy enforcement for MCP tools and resources.

**v3.20 (GA late April 2026): Triple Gate architecture** with parallel safety pipelines (multi-vendor guard execution), multi-provider failover routing, token-level cost controls, graceful error handling (HTTP 200 refusal response instead of 403 for agent-aware enforcement), IBM Granite Guardian integration, and a Regex Guard for custom content filtering. The "Triple Gate" (API Gateway + AI Gateway + MCP Gateway) positions Traefik Hub as a unified infrastructure-layer governance solution from public cloud to air-gapped environments.

### Cloudflare MCP Server Portals

Open Beta launched April/May 2026. Compose multiple MCP servers behind a single gateway with unified auth and access control. Instead of distributing dozens of individual server endpoints, register servers with Cloudflare and provide users a single Portal endpoint. Zero Trust security model applied to MCP infrastructure. **Code Mode is the default on all portals** — context usage stays fixed regardless of how many tools are available.

### Google Apigee

Apigee provides **native, zero-code MCP support** — it dynamically discovers existing Apigee-managed API Products and their OpenAPI specifications, then exposes them as MCP tools. No code changes to existing APIs, no new servers to deploy or manage. Apigee handles infrastructure, transcoding, identity, authorization, and analytics for MCP endpoints.

**April–May 2026 updates — the most active update window for Apigee MCP yet:**

- **Apigee Hybrid v1.16.1 (April 20):** Broader set of MCP methods supported; governance bypass for essential system-level operations.
- **Apigee API Hub — Unified MCP Proxy Configuration (May 7):** Select API operations from catalog, bundle into an MCP server, auto-deploy — without writing a spec.
- **Apigee API Hub — MCP Tools in Public Preview (May 12):** API Hub now exposes read-only APIs directly as MCP tools. MCP Discovery Proxies (also Public Preview) let you create and deploy MCP discovery proxies from API Hub without manual spec authoring. Agent Registry Integration automatically syncs MCP server and tool metadata to the Agent Registry for AI agent discovery.
- **Apigee Hybrid v1.16.2 (May 13):** Critical security fix — `LLMTokenQuota` operations were not enforcing model-based access restrictions; patched.

This is arguably the most enterprise-ready approach: existing API governance (rate limits, quotas, analytics, security policies) automatically applies to MCP tool invocations. The May 12 Public Preview additions (MCP Tools, Discovery Proxies, Agent Registry sync) meaningfully reduce the friction of bringing an existing API catalog into the MCP ecosystem.

### Databricks Unity AI Gateway (NEW)

**Databricks rebranded and expanded AI Gateway as "Unity AI Gateway" (April 15, 2026)**, integrating it into Unity Catalog for unified data + AI governance. The key MCP addition: fine-grained permissions governing which AI agents can access external systems via MCP, with On-Behalf-Of (OBO) access and complete end-to-end observability for LLM and MCP calls. Rate limiting, fallback routing, and cost controls span model providers. For organizations already on Databricks, this is the natural governance layer for MCP traffic — no separate gateway to deploy.

### Higress API Gateway (MCP)

**Higress** (a cloud-native API gateway from Alibaba) added two MCP-related capabilities in 2026: API authentication for MCP server connections to backend services (both client-to-gateway and gateway-to-backend auth), plus a new MCP proxy server type that proxies client MCP requests to backend MCP servers. Listed on PulseMCP. Significant for teams in the cloud-native CNCF ecosystem already running Higress.

### Tyk AI Studio

Tyk's API-to-MCP bridge converts REST, GraphQL, and RPC endpoints into standardized MCP tools. **March 2026: Tyk AI Studio went open source** (Community Edition). Capabilities: MCP tool generation from OpenAPI specs, scoped tool access policies with guardrails, complete audit trails for prompts/responses/tool calls, PII redaction and content filtering at the gateway, and enterprise SSO/RBAC. Previously commercial-only, the open-source release significantly lowers the barrier to entry for self-hosted AI governance. No significant new release confirmed in the April 22–May 20 window.

### Microsoft MCP Gateway

| Project | Stars | Language | License | Latest |
|---------|-------|----------|---------|--------|
| [microsoft/mcp-gateway](https://github.com/microsoft/mcp-gateway) | ~640 | Go | MIT | Apr 2026 |

**Microsoft's Kubernetes-native MCP gateway, now at 640 stars (+8% from 595).** 63 forks, created May 2025, actively pushed. A reverse proxy and management layer for MCP servers with:

- **Session-aware stateful routing** — all requests with a given session_id consistently route to the same MCP server instance via StatefulSets and headless services
- **Control plane** for MCP server lifecycle management (deploy, update, delete)
- **Tool registration with dynamic routing** — scalable architecture for managing and executing MCP tools
- **Azure Entra ID (AAD)** OAuth 2.0 authentication
- **Enterprise-ready** telemetry, access control, and observability integration points

For organizations already running Kubernetes on Azure, this is the natural fit. The Kubernetes-native approach (StatefulSets for session affinity, headless services for direct pod routing) is architecturally sound for MCP's stateful protocol requirements.

## Gaps and Limitations

**No Nginx MCP server** — the world's most-used reverse proxy has no MCP integration for managing its own configurations (only Nginx Proxy Manager has one). **No HAProxy MCP server.** No **Istio** or **Linkerd** service mesh MCP servers for managing mesh configurations.

**APISIX is write-capable but dormant; most others are read-only.** Kong Konnect's hosted server is read-heavy with only debug sessions as write operations. The community Traefik server is entirely read-only. APISIX hasn't been updated in 11 months. This asymmetry makes sense for safety but limits what agents can do autonomously.

**The MCP gateway space is expanding, not converging.** AgentGateway, Envoy AI Gateway, Kong Agent Gateway, Traefik Hub, Microsoft MCP Gateway, Cloudflare Portals, Docker MCP Gateway, Databricks Unity AI Gateway, and Higress are all active approaches with different architectures and target ecosystems. AgentGateway's v1.x cadence and Envoy's v0.6.0 graduation suggest open-source leadership is becoming clearer, but enterprise buyers will choose based on their existing infrastructure.

**Cloudflare's Code Mode is proven and now default** — a validation of the 2-tool pattern. But it still requires models that can reliably write JavaScript to query API specs, which limits compatibility with simpler models.

## The Bottom Line

**For managing Kong Gateway:** Use the official Kong Konnect hosted MCP server. Zero setup, 12 tools, active development. The MCP Registry tech preview adds discovery and governance.

**For managing APISIX:** Use api7/apisix-mcp — 30+ tools covering the full Admin API. But be aware the server hasn't been updated since June 2025 (11+ months); test against your APISIX version before deploying.

**For managing Cloudflare:** Use cloudflare/mcp (Code Mode). 2 tools covering 2,500+ endpoints. Default on all MCP Server Portals. Fall back to cloudflare/mcp-server-cloudflare (3,800 stars, 16 product servers) for specific product integrations.

**For MCP traffic governance — open source:** AgentGateway (2,800 stars, Rust, Linux Foundation, Solo.io-backed, v1.2.1) is the open-source leader with the most active release cadence. Envoy AI Gateway (1,700 stars, v0.6.0, MCPRoute v1beta1) is the best-engineered choice if you're already in the Envoy/Kubernetes ecosystem — v1.0 GA is near.

**For MCP traffic governance — enterprise/cloud:** Kong Agent Gateway (3.14) is still the first to unify LLM+MCP+A2A governance. Microsoft MCP Gateway (640 stars) for Azure/Kubernetes shops. Databricks Unity AI Gateway for teams on the Databricks Lakehouse platform. Google Apigee for organizations with existing API catalogs — the May 2026 API Hub additions dramatically lower the barrier to entry.

**For converting existing APIs to MCP:** Google Apigee (zero-code, now with MCP Discovery Proxies and MCP Tools in Public Preview) and Kong AI Gateway (plugin-based API-to-MCP conversion) are the most mature. Tyk AI Studio (now open source) is the best self-hosted option. Docker MCP Gateway for teams already on Docker infrastructure.

**Rating: 4/5** — Held. The market is expanding faster than it is consolidating. Envoy v0.6.0's MCPRoute v1beta1 graduation is a meaningful maturity signal; AgentGateway's v1.2.1 feature velocity is impressive; Apigee's API Hub Public Preview meaningfully lowers the barrier for enterprise API catalogs. New entrants (Docker, Databricks, Higress) validate the category. The persistent gap remains on the management side — APISIX has 30+ write tools but is dormant, and most gateway management servers are still read-only. When that changes, the rating moves to 4.5.

*This review was last edited on 2026-05-20 using Claude Sonnet 4.6 (Anthropic).*

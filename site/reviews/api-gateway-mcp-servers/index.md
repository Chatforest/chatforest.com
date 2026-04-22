# API Gateway MCP Servers — Kong, APISIX, Cloudflare, Envoy, Traefik, and Beyond

> API gateway MCP servers let AI agents manage routes, services, plugins, and traffic across Kong, APISIX, Cloudflare, Traefik, Gravitee, and more.


API gateways sit at the intersection of every API call in production infrastructure. Making them accessible to AI agents unlocks powerful capabilities: **natural language route configuration, automated traffic analysis, real-time debugging, and intelligent plugin management**. But this category splits into two distinct stories.

**Story one: MCP servers for managing API gateways** — tools that let AI agents configure routes, analyze traffic, and troubleshoot services on platforms like Kong, APISIX, and Traefik. **Story two: API gateways acting as MCP infrastructure** — platforms like Envoy AI Gateway, AgentGateway, Traefik Hub, and Cloudflare that route, secure, and govern MCP traffic itself. Both matter. This review covers the full picture.

The headline: **Kong Agent Gateway (April 14, 2026) is the first platform to unify LLM, MCP, and A2A governance in a single control plane.** **Cloudflare's Code Mode is now the default on all MCP Server Portals** — 2 tools covering 2,500+ API endpoints in ~1,000 tokens, versus the 244K+ tokens a traditional MCP implementation would require. **AgentGateway has surged to 2,457 stars with 1M+ image pulls**, solidifying its position as the open-source MCP gateway leader. And **Microsoft has entered the space** with a Kubernetes-native MCP Gateway already at 595 stars.

**Category:** [Developer Tools](/categories/developer-tools/)

## Part 1: MCP Servers for Managing API Gateways

### Kong Konnect (Official, Hosted)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [Kong Konnect MCP](https://konghq.com/products/kong-konnect/agents) | N/A (hosted) | N/A | 12 | Konnect account | Streamable HTTP |

**Kong's official hosted MCP server is the most polished API gateway management experience available.** Zero-install remote hosting — connect directly from Claude, Cursor, VS Code, or any MCP client. Active development with new tools being added regularly.

12 tools across four areas: **Gateway configuration** (GetService, GetRoute, GetPlugin, GetConsumer, GetConsumerGroup, GetVault — full read access to your gateway topology), **Control plane management** (GetControlPlane, GetControlPlaneGroup — multi-cluster visibility), **Analytics** (GetAnalytics — traffic patterns, status codes, consumer activity), and **Debugging** (CreateDebugSession, ActiveTracingSession — real-time performance tracing). Plus **KnowledgeBaseSearch** for querying Kong documentation and best practices.

The debug session capability is noteworthy — you can ask an AI agent to trace a specific request path and it will create a targeted tracing session collecting real-time performance data. This is exactly the kind of workflow that benefits from conversational AI: "Why are requests to /api/v2/orders slow?" → agent creates debug session → analyzes trace data → identifies bottleneck.

**New in 2026: Kong MCP Registry** — launched in tech preview (February 2026), this is an enterprise directory within the Kong Konnect Catalog for registering, discovering, and governing MCP servers and AI-native tools. AAIF-compliant. Automated server generation turns existing API catalogs into AI-ready toolsets. MCP Composer and MCP Runner tools announced for early 2026 early access.

**Deprecated predecessor: [Kong/mcp-konnect](https://github.com/Kong/mcp-konnect)** — 38 stars, TypeScript, Apache 2.0, 10 tools, 9 commits. No longer maintained. Had analytics and configuration read tools but was self-hosted only. The hosted replacement is a significant upgrade in both capability and developer experience.

### Apache APISIX (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [api7/apisix-mcp](https://github.com/api7/apisix-mcp) | ~36 | TypeScript | 30+ | Admin API key | stdio |

**APISIX's MCP server provides the deepest API gateway management capabilities of any server in this review — but development has stalled.** 36 stars, 14 forks, Apache 2.0, npm package `apisix-mcp` v0.0.7. Last push June 2025 — nearly 10 months without a commit.

30+ tools covering full CRUD on every APISIX resource type: **Routes** (create_route, update_route, delete_route), **Services** (create_service, update_service, delete_service), **Upstreams** (create_upstream, update_upstream, delete_upstream), **SSL certificates** (create_ssl, update_ssl, delete_ssl), **Consumers and credentials** (create_or_update_consumer, delete_consumer, get_credential, create_or_update_credential, delete_credential), **Consumer groups** (create_consumer_group, delete_consumer_group), **Plugins** (get_all_plugin_names, get_plugin_info, get_plugins_by_type, get_plugin_schema, create_plugin_config, update_plugin_config), **Global rules** (create_global_rule, update_global_rule), **Plugin metadata** (get_plugin_metadata, create_or_update_plugin_metadata, delete_plugin_metadata), **Secrets** (get_secret_by_id, create_secret, update_secret), **Proto definitions** (create_or_update_proto), **Stream routes** (create_or_update_stream_route), plus **get_resource** (generic retrieval) and **send_request_to_gateway** (test requests).

This is essentially the entire APISIX Admin API exposed as MCP tools. For teams running APISIX, this means AI agents can handle the complete gateway lifecycle: "Create a new route for /api/v3/users pointing to upstream-cluster-2 with rate limiting and JWT auth" → agent creates the route, configures plugins, tests the endpoint.

The trade-off is complexity — 30+ tools means more for the AI model to navigate. But APISIX's plugin ecosystem (200+ plugins in the main project, which has 14,000+ stars) makes this breadth valuable. **Concern: with no commits in 10 months, compatibility with newer APISIX versions is uncertain.**

### Cloudflare API (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [cloudflare/mcp](https://github.com/cloudflare/mcp) | ~369 | TypeScript | 2 | OAuth 2.1 / API token | Streamable HTTP |

**Cloudflare's MCP server uses the most architecturally innovative approach we've seen in any MCP server category — and Code Mode is now the default on all MCP Server Portals.** 369 stars (up 40% from 263), 30 forks, Apache 2.0, actively pushed April 21, 2026. Rather than exposing 2,594 endpoints as individual tools (which would consume ~244,000 tokens of context), it uses "Code Mode" with just 2 tools in ~1,069 tokens — a **99.5% reduction** in context footprint.

The two tools: **search** (agent writes JavaScript to query `spec.paths` and find endpoints by iterating the API specification server-side) and **execute** (agent writes JavaScript to call `cloudflare.request()` with discovered endpoints). The specification lives on the server — only execution results return to the agent.

**March 26, 2026 milestone: Code Mode became the default on all MCP Server Portals.** This means any portal created in Cloudflare Access automatically uses the 2-tool pattern. Append `?codemode=search_and_execute` to the portal URL, or disable via the Access dashboard. The generated code runs in an isolated Dynamic Worker environment, keeping credentials and environment variables out of the model context.

This covers the *entire* Cloudflare API: DNS, Workers, R2 storage, Zero Trust, AI Gateway, D1, KV, Queues, Pages, and every other Cloudflare product. When Cloudflare adds new products, the same search/execute pattern discovers them — no new tool definitions needed.

**Authentication:** OAuth 2.1 (recommended, uses Workers OAuth Provider to downscope tokens) or API tokens with automatic account ID detection for account-scoped tokens.

**Also notable: [cloudflare/mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare)** — 3,650 stars (up from 3,500), 371 forks, TypeScript, Apache 2.0, 349+ commits. The older, traditional approach with 15 separate per-product MCP servers (Documentation, Workers Bindings, Workers Builds, Observability, Radar, Container, Browser Rendering, Logpush, AI Gateway, AutoRAG, Audit Logs, DNS Analytics, Digital Experience Monitoring, CASB, GraphQL). Still active and useful for specific product integrations, but Code Mode represents where Cloudflare is heading.

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

Tools are dynamically generated — covering API listing/retrieval, health monitoring, API creation/configuration, plan management, API lifecycle (start/stop), and environment operations. The auto-generation approach means it tracks the Management API automatically, but also means the tooling is generic rather than purpose-built for AI agent workflows.

**Where Gravitee is investing: Agent Mesh and MCP Resource Server V2.** Gravitee 4.8 shipped Agent Mesh — a suite of features including Agent Gateway, Agent Catalog, and Agent Tool Server. The MCP Resource Server V2 (2026) adds full Client Credentials flows, AuthZen Bearer tokens, and production-grade secret management. Convert any HTTP proxy API into an MCP-compatible server directly at the gateway level using your OpenAPI spec as input. The open-source MCP server is the entry point; Agent Mesh is the enterprise product.

### Nginx Proxy Manager (Community)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [b3nw/nginx-proxy-manager-mcp](https://github.com/b3nw/nginx-proxy-manager-mcp) | Low | TypeScript | Multiple | NPM credentials | stdio |

**A community server for Nginx Proxy Manager**, enabling AI agents to manage reverse proxy configurations. Provides CRUD operations on proxy hosts, SSL certificates, and access lists through the NPM API. Useful for homelab and small-scale deployments where Nginx Proxy Manager is already the management layer.

Not to be confused with Nginx itself (which has no MCP server) — this specifically targets the Nginx Proxy Manager web interface API.

## Part 2: MCP Gateways (API Gateways for MCP Traffic)

A rapidly maturing subcategory: platforms that don't just expose their *own* API via MCP, but act as **infrastructure for routing, securing, and governing MCP traffic** between agents and tools. This space consolidated significantly in Q1 2026.

### AgentGateway (Solo.io / Linux Foundation)

| Project | Stars | Language | License | Latest |
|---------|-------|----------|---------|--------|
| [agentgateway/agentgateway](https://github.com/agentgateway/agentgateway) | ~2,457 | Rust/Go/TS | Apache 2.0 | Enterprise v2.3 (Apr 2026) |

**The largest open-source MCP gateway project, now with 2,457 stars (+29% from 1,900) and 1M+ image pulls.** 409 forks, 203 open issues, actively pushed April 21. Donated to the Linux Foundation in August 2025. Built in Rust for high performance.

Positions itself as "the first complete connectivity solution for Agentic AI" — a data plane for agent-to-agent (A2A) and agent-to-tool (MCP) communication. Key capabilities: MCP/A2A-focused RBAC, multi-tenant isolation, xDS-based dynamic configuration (Envoy-style), OpenAPI-to-MCP transformation (legacy API integration), and a built-in Kubernetes controller via Gateway API.

**Solo Enterprise for AgentGateway v2.3 (April 2026):** AWS Bedrock AgentCore integration (inline OpenAPI schemas make REST APIs available as MCP tools without a live MCP server), intelligent failover routing, deeper MCP authentication and token exchange (On-Behalf-Of flows with claim forwarding), and OTel environment variable support for drop-in observability. The Solo.io backing means enterprise support is available — the same company that built Gloo and contributed to Istio.

### Envoy AI Gateway

| Project | Stars | Language | License | Latest |
|---------|-------|----------|---------|--------|
| [envoyproxy/ai-gateway](https://github.com/envoyproxy/ai-gateway) | ~1,542 | Go | Apache 2.0 | v0.5.0 (Jan 2026) |

**Envoy's official AI gateway includes first-class MCP support, leveraging Envoy's battle-tested networking stack.** 1,542 stars (up 10% from 1,400), 224 forks, actively pushed April 20.

The MCP Gateway is implemented as a lightweight proxy within the Envoy AI Gateway sidecar: session management, stream multiplexing, and bridging between MCP's stateful JSON-RPC protocol and Envoy's extension mechanisms. Features include MCP session-aware load balancing, full OAuth authentication, server multiplexing, and fine-grained CEL-based MCP authorization (v0.5.0).

Can run in standalone mode with your existing MCP servers config file — meaning you can put Envoy in front of servers you're already using with Claude Code or Cursor without reconfiguration. Streamable HTTP transport aligned with the MCP standard. Tetrate published MCP performance benchmarks showing proxy overhead is primarily in session encryption, not MCP traffic handling.

Still on v0.5.0 since January 2026 — 3 months without a release, though commits continue.

### Kong AI Gateway + Agent Gateway

Kong Gateway 3.14 (April 14, 2026) launched **Kong Agent Gateway** — the **first platform to unify LLM, MCP, and A2A governance in a single control plane**. This extends the existing MCP plugins (AI MCP Proxy, AI MCP OAuth2, Prometheus MCP metrics) from Gateway 3.12+ with full Agent-to-Agent protocol support.

Kong's enterprise MCP Gateway addresses server sprawl, security gaps, and cost management for organizations running many MCP servers. The gateway converts RESTful APIs defined as Kong Gateway Services into MCP tools automatically — acting as a protocol bridge between MCP and HTTP. With Agent Gateway, organizations can enforce consistent policies across all AI traffic types from a single control point.

### Traefik Hub MCP Gateway (Triple Gate)

Traefik Hub's MCP Gateway (commercial) adds OAuth-compliant proxying with **Task-Based Access Control (TBAC)** — a novel approach where access policies are defined per-tool rather than per-user or per-role. Centralized access control, resource metadata discovery, and fine-grained policy enforcement for MCP tools and resources.

**March 2026 update: Triple Gate architecture extended** with parallel safety pipelines (multi-vendor guard execution), multi-provider failover routing, token-level cost controls, graceful error handling for agent-aware enforcement, IBM Granite Guardian integration, and a new Regex Guard for custom content filtering. The "Triple Gate" (API Gateway + AI Gateway + MCP Gateway) positions Traefik Hub as a unified infrastructure-layer governance solution from public cloud to air-gapped environments.

### Cloudflare MCP Server Portals

Announced March 2026. Compose multiple MCP servers behind a single gateway with unified auth and access control. Instead of distributing dozens of individual server endpoints, register servers with Cloudflare and provide users a single Portal endpoint. Zero Trust security model applied to MCP infrastructure. **Code Mode is now the default on all portals** — context usage stays fixed regardless of how many tools are available.

### Google Apigee

Apigee provides **native, zero-code MCP support** — it dynamically discovers existing Apigee-managed API Products and their OpenAPI specifications, then exposes them as MCP tools. No code changes to existing APIs, no new servers to deploy or manage. Apigee handles infrastructure, transcoding, identity, authorization, and analytics for MCP endpoints.

**2026 updates:** Fully-managed remote MCP servers now available — just deploy an MCP proxy and Apigee manages the rest. API Hub now treats MCP as a first-class API style, with automatic registration of deployed MCP proxies. Apigee hybrid v1.16.1 released April 20. This is arguably the most enterprise-ready approach: existing API governance (rate limits, quotas, analytics, security policies) automatically applies to MCP tool invocations.

### Tyk AI Studio

Tyk's API-to-MCP bridge converts REST, GraphQL, and RPC endpoints into standardized MCP tools. **Major March 2026 development: Tyk AI Studio went open source.** This makes it the most accessible self-hosted AI governance option, with MCP tool generation from OpenAPI specs, scoped tool access policies with guardrails, complete audit trails for prompts/responses/tool calls, PII redaction and content filtering at the gateway, and enterprise SSO/RBAC. Previously commercial-only, the open-source release significantly lowers the barrier to entry.

### Microsoft MCP Gateway (NEW)

| Project | Stars | Language | License | Latest |
|---------|-------|----------|---------|--------|
| [microsoft/mcp-gateway](https://github.com/microsoft/mcp-gateway) | ~595 | Go | MIT | Apr 2026 |

**Microsoft's entry into the MCP gateway space is Kubernetes-native from the ground up.** 595 stars, 63 forks, created May 2025, actively pushed April 16. A reverse proxy and management layer for MCP servers with:

- **Session-aware stateful routing** — all requests with a given session_id consistently route to the same MCP server instance via StatefulSets and headless services
- **Control plane** for MCP server lifecycle management (deploy, update, delete)
- **Tool registration with dynamic routing** — scalable architecture for managing and executing MCP tools
- **Azure Entra ID (AAD)** OAuth 2.0 authentication
- **Enterprise-ready** telemetry, access control, and observability integration points

For organizations already running Kubernetes on Azure, this is the natural fit. The Kubernetes-native approach (StatefulSets for session affinity, headless services for direct pod routing) is architecturally sound for MCP's stateful protocol requirements.

## Gaps and Limitations

**No Nginx MCP server** — the world's most-used reverse proxy has no MCP integration for managing its own configurations (only Nginx Proxy Manager has one). **No HAProxy MCP server.** No **Istio** or **Linkerd** service mesh MCP servers for managing mesh configurations.

**APISIX is write-capable but dormant; most others are read-only.** Kong Konnect's hosted server is read-heavy with only debug sessions as write operations. The community Traefik server is entirely read-only. APISIX hasn't been updated in 10 months. This asymmetry makes sense for safety but limits what agents can do autonomously.

**The MCP gateway space is consolidating but still fragmented.** AgentGateway, Envoy AI Gateway, Kong Agent Gateway, Traefik Hub, Microsoft MCP Gateway, and Cloudflare Portals are all competing approaches with different architectures. Kong's unification of LLM+MCP+A2A and AgentGateway's Linux Foundation governance suggest the leaders are emerging, but no single standard has won.

**Cloudflare's Code Mode is proven and now default** — a validation of the 2-tool pattern. But it still requires models that can reliably write JavaScript to query API specs, which limits compatibility with simpler models.

## The Bottom Line

**For managing Kong Gateway:** Use the official Kong Konnect hosted MCP server. Zero setup, 12 tools, active development. The MCP Registry tech preview adds discovery and governance.

**For managing APISIX:** Use api7/apisix-mcp — 30+ tools covering the full Admin API. But be aware the server hasn't been updated since June 2025; test against your APISIX version.

**For managing Cloudflare:** Use cloudflare/mcp (Code Mode). 2 tools covering 2,500+ endpoints. Now the default on all MCP Server Portals. Fall back to cloudflare/mcp-server-cloudflare for specific product integrations.

**For MCP traffic governance:** AgentGateway (2,457 stars, Rust, Linux Foundation, Solo.io-backed) is the open-source leader. Envoy AI Gateway (1,542 stars) is the choice if you're already in the Envoy ecosystem. Kong Agent Gateway (3.14) is the first to unify LLM+MCP+A2A governance. Microsoft MCP Gateway (595 stars) is the Kubernetes-native option for Azure shops.

**For converting existing APIs to MCP:** Google Apigee (zero-code, enterprise governance, fully-managed MCP servers) and Kong AI Gateway (plugin-based API-to-MCP conversion) are the most mature. Tyk AI Studio (now open source) is the best self-hosted option.

**Rating: 4/5** — Upgraded from 3.5. The space has matured significantly since March: Kong unifying LLM+MCP+A2A governance is a genuine milestone, Microsoft's entry validates the category, AgentGateway hitting 2,457 stars and 1M image pulls shows real adoption, Tyk going open source expands accessibility, and Cloudflare's Code Mode becoming the default proves the pattern works. Gateway management servers (Kong, Cloudflare) are production-ready. The remaining gap is gateway management tool breadth — APISIX has it but is dormant, and most alternatives are read-only.

*This review was last edited on 2026-04-22 using Claude Opus 4.6 (Anthropic).*


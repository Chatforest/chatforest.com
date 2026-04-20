# API Gateway MCP Servers — Kong, APISIX, Cloudflare, Envoy, Traefik, and Beyond

> API gateway MCP servers let AI agents manage routes, services, plugins, and traffic across Kong, APISIX, Cloudflare, Traefik, Gravitee, and more.


API gateways sit at the intersection of every API call in production infrastructure. Making them accessible to AI agents unlocks powerful capabilities: **natural language route configuration, automated traffic analysis, real-time debugging, and intelligent plugin management**. But this category splits into two distinct stories.

**Story one: MCP servers for managing API gateways** — tools that let AI agents configure routes, analyze traffic, and troubleshoot services on platforms like Kong, APISIX, and Traefik. **Story two: API gateways acting as MCP infrastructure** — platforms like Envoy AI Gateway, AgentGateway, Traefik Hub, and Cloudflare that route, secure, and govern MCP traffic itself. Both matter. This review covers the full picture.

The headline: **Cloudflare's Code Mode is the most architecturally innovative approach** — 2 tools covering 2,500+ API endpoints in ~1,000 tokens, versus the 244K+ tokens a traditional MCP implementation would require. **Kong Konnect offers the most polished official gateway management experience** with a hosted 12-tool server. And **APISIX provides the deepest gateway CRUD** with 30+ tools for routes, services, upstreams, plugins, consumers, SSL, and secrets.

**Category:** [Developer Tools](/categories/developer-tools/)

## Part 1: MCP Servers for Managing API Gateways

### Kong Konnect (Official, Hosted)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [Kong Konnect MCP](https://konghq.com/products/kong-konnect/agents) | N/A (hosted) | N/A | 12 | Konnect account | Streamable HTTP |

**Kong's official hosted MCP server is the most polished API gateway management experience available.** Zero-install remote hosting — connect directly from Claude, Cursor, VS Code, or any MCP client. Active development with new tools being added regularly.

12 tools across four areas: **Gateway configuration** (GetService, GetRoute, GetPlugin, GetConsumer, GetConsumerGroup, GetVault — full read access to your gateway topology), **Control plane management** (GetControlPlane, GetControlPlaneGroup — multi-cluster visibility), **Analytics** (GetAnalytics — traffic patterns, status codes, consumer activity), and **Debugging** (CreateDebugSession, ActiveTracingSession — real-time performance tracing). Plus **KnowledgeBaseSearch** for querying Kong documentation and best practices.

The debug session capability is noteworthy — you can ask an AI agent to trace a specific request path and it will create a targeted tracing session collecting real-time performance data. This is exactly the kind of workflow that benefits from conversational AI: "Why are requests to /api/v2/orders slow?" → agent creates debug session → analyzes trace data → identifies bottleneck.

**Deprecated predecessor: [Kong/mcp-konnect](https://github.com/Kong/mcp-konnect)** — 38 stars, TypeScript, Apache 2.0, 10 tools, 9 commits. No longer maintained. Had analytics and configuration read tools but was self-hosted only. The hosted replacement is a significant upgrade in both capability and developer experience.

### Apache APISIX (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [api7/apisix-mcp](https://github.com/api7/apisix-mcp) | ~34 | TypeScript | 30+ | Admin API key | stdio |

**APISIX's MCP server provides the deepest API gateway management capabilities of any server in this review.** 34 stars, 13 forks, 37 commits, Apache 2.0, npm package `apisix-mcp` v0.0.7.

30+ tools covering full CRUD on every APISIX resource type: **Routes** (create_route, update_route, delete_route), **Services** (create_service, update_service, delete_service), **Upstreams** (create_upstream, update_upstream, delete_upstream), **SSL certificates** (create_ssl, update_ssl, delete_ssl), **Consumers and credentials** (create_or_update_consumer, delete_consumer, get_credential, create_or_update_credential, delete_credential), **Consumer groups** (create_consumer_group, delete_consumer_group), **Plugins** (get_all_plugin_names, get_plugin_info, get_plugins_by_type, get_plugin_schema, create_plugin_config, update_plugin_config), **Global rules** (create_global_rule, update_global_rule), **Plugin metadata** (get_plugin_metadata, create_or_update_plugin_metadata, delete_plugin_metadata), **Secrets** (get_secret_by_id, create_secret, update_secret), **Proto definitions** (create_or_update_proto), **Stream routes** (create_or_update_stream_route), plus **get_resource** (generic retrieval) and **send_request_to_gateway** (test requests).

This is essentially the entire APISIX Admin API exposed as MCP tools. For teams running APISIX, this means AI agents can handle the complete gateway lifecycle: "Create a new route for /api/v3/users pointing to upstream-cluster-2 with rate limiting and JWT auth" → agent creates the route, configures plugins, tests the endpoint.

The trade-off is complexity — 30+ tools means more for the AI model to navigate. But APISIX's plugin ecosystem (200+ plugins in the main project, which has 14,000+ stars) makes this breadth valuable.

### Cloudflare API (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [cloudflare/mcp](https://github.com/cloudflare/mcp) | ~263 | TypeScript | 2 | OAuth 2.1 / API token | Streamable HTTP |

**Cloudflare's MCP server uses the most architecturally innovative approach we've seen in any MCP server category.** 263 stars, 19 forks, 50 commits, Apache 2.0. Rather than exposing 2,594 endpoints as individual tools (which would consume ~244,000 tokens of context), it uses "Code Mode" with just 2 tools in ~1,069 tokens — a **99.5% reduction** in context footprint.

The two tools: **search** (agent writes JavaScript to query `spec.paths` and find endpoints by iterating the API specification server-side) and **execute** (agent writes JavaScript to call `cloudflare.request()` with discovered endpoints). The specification lives on the server — only execution results return to the agent.

This covers the *entire* Cloudflare API: DNS, Workers, R2 storage, Zero Trust, AI Gateway, D1, KV, Queues, Pages, and every other Cloudflare product. When Cloudflare adds new products, the same search/execute pattern discovers them — no new tool definitions needed.

**Authentication:** OAuth 2.1 (recommended, uses Workers OAuth Provider to downscope tokens) or API tokens with automatic account ID detection for account-scoped tokens.

**Also notable: [cloudflare/mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare)** — 3,500 stars, TypeScript, Apache 2.0, 349 commits. The older, traditional approach with 15 separate per-product MCP servers (Documentation, Workers Bindings, Workers Builds, Observability, Radar, Container, Browser Rendering, Logpush, AI Gateway, AutoRAG, Audit Logs, DNS Analytics, Digital Experience Monitoring, CASB, GraphQL). Still active and useful for specific product integrations, but the Code Mode server represents where Cloudflare is heading.

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
| [gravitee-io/gravitee-apim-mcp-server](https://github.com/gravitee-io/gravitee-apim-mcp-server) | ~1 | TypeScript | Dynamic | Bearer token | stdio |

**Gravitee's official MCP server is auto-generated from the Management API v2 OpenAPI specification.** 1 star, 2 forks, 3 commits, MIT. Very early stage.

Tools are dynamically generated — covering API listing/retrieval, health monitoring, API creation/configuration, plan management, API lifecycle (start/stop), and environment operations. The auto-generation approach means it tracks the Management API automatically, but also means the tooling is generic rather than purpose-built for AI agent workflows.

Gravitee's broader AI story is more interesting: **Gravitee Agent Mesh** (commercial) enables MCP-enabling any API as a tool for autonomous agents, with agent discovery and A2A protocol support. The APIM MCP server is the open-source entry point; the Agent Mesh is where the enterprise investment is going.

### Nginx Proxy Manager (Community)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [b3nw/nginx-proxy-manager-mcp](https://github.com/b3nw/nginx-proxy-manager-mcp) | Low | TypeScript | Multiple | NPM credentials | stdio |

**A community server for Nginx Proxy Manager**, enabling AI agents to manage reverse proxy configurations. Provides CRUD operations on proxy hosts, SSL certificates, and access lists through the NPM API. Useful for homelab and small-scale deployments where Nginx Proxy Manager is already the management layer.

Not to be confused with Nginx itself (which has no MCP server) — this specifically targets the Nginx Proxy Manager web interface API.

## Part 2: MCP Gateways (API Gateways for MCP Traffic)

A rapidly growing subcategory: platforms that don't just expose their *own* API via MCP, but act as **infrastructure for routing, securing, and governing MCP traffic** between agents and tools.

### AgentGateway (Solo.io)

| Project | Stars | Language | License | Latest |
|---------|-------|----------|---------|--------|
| [agentgateway/agentgateway](https://github.com/agentgateway/agentgateway) | ~1,900 | Rust/Go/TS | Apache 2.0 | v1.0.0-rc.2 (Mar 2026) |

**The largest open-source MCP gateway project.** 1,900 stars, 315 forks, 1,402 commits, 115 contributors. Backed by Solo.io (Gloo Gateway makers). Built in Rust for high performance.

Positions itself as "the first complete connectivity solution for Agentic AI" — a data plane for agent-to-agent (A2A) and agent-to-tool (MCP) communication. Key capabilities: MCP/A2A-focused RBAC, multi-tenant isolation, xDS-based dynamic configuration (Envoy-style), OpenAPI-to-MCP transformation (legacy API integration), and a built-in Kubernetes controller via Gateway API.

The Solo.io backing means enterprise support is available. Solo Enterprise for agentgateway adds high availability, scaling, and governance features. This is the closest thing to "Envoy for AI agents" — the same company that built Gloo and contributed to Istio is now building the agent connectivity layer.

### Envoy AI Gateway

| Project | Stars | Language | License | Latest |
|---------|-------|----------|---------|--------|
| [envoyproxy/ai-gateway](https://github.com/envoyproxy/ai-gateway) | ~1,400 | Go | Apache 2.0 | v0.5.0 (Jan 2026) |

**Envoy's official AI gateway now includes first-class MCP support.** 1,400 stars, 186 forks, 1,264 commits. Leverages Envoy's battle-tested networking stack for connection handling.

The MCP Gateway is implemented as a lightweight proxy within the Envoy AI Gateway sidecar: session management, stream multiplexing, and bridging between MCP's stateful JSON-RPC protocol and Envoy's extension mechanisms. Features include MCP session-aware load balancing, full OAuth authentication, server multiplexing, and fine-grained MCP authorization (v0.5.0).

Can run in standalone mode with your existing MCP servers config file — meaning you can put Envoy in front of servers you're already using with Claude Code or Cursor without reconfiguration.

### Kong AI Gateway

Kong Gateway 3.12+ (October 2025) includes three MCP-specific plugins: **AI MCP Proxy** (routes MCP traffic), **AI MCP OAuth2** (MCP-scoped authentication), and **Prometheus MCP metrics** (observability). The gateway can convert RESTful APIs defined as Kong Gateway Services into MCP tools automatically — acting as a protocol bridge between MCP and HTTP.

Kong's enterprise MCP Gateway addresses server sprawl, security gaps, and cost management for organizations running many MCP servers. This is the "API-to-MCP" conversion approach: bring your existing Kong-managed APIs and expose them as tools to AI agents without writing MCP server code.

### Traefik Hub MCP Gateway

Traefik Hub's MCP Gateway (commercial) adds OAuth-compliant proxying with **Task-Based Access Control (TBAC)** — a novel approach where access policies are defined per-tool rather than per-user or per-role. Centralized access control, resource metadata discovery, and fine-grained policy enforcement for MCP tools and resources.

### Cloudflare MCP Server Portals

Announced March 2026. Compose multiple MCP servers behind a single gateway with unified auth and access control. Instead of distributing dozens of individual server endpoints, register servers with Cloudflare and provide users a single Portal endpoint. Zero Trust security model applied to MCP infrastructure.

### Google Apigee

Apigee provides **native, zero-code MCP support** — it dynamically discovers existing Apigee-managed API Products and their OpenAPI specifications, then exposes them as MCP tools. No code changes to existing APIs, no new servers to deploy or manage. Apigee handles infrastructure, transcoding, identity, authorization, and analytics for MCP endpoints.

This is arguably the most enterprise-ready approach: existing API governance (rate limits, quotas, analytics, security policies) automatically applies to MCP tool invocations.

### Tyk AI Studio

Tyk's API-to-MCP bridge converts REST, GraphQL, and RPC endpoints into standardized MCP tools. Developers specify which endpoints to expose and configure access control. Relatively new (circa 2025) with documentation still catching up to the core platform.

## Gaps and Limitations

**No Nginx MCP server** — the world's most-used reverse proxy has no MCP integration for managing its own configurations (only Nginx Proxy Manager has one). **No HAProxy MCP server.** No **Istio** or **Linkerd** service mesh MCP servers for managing mesh configurations.

**APISIX is write-capable; most others are read-only.** Kong Konnect's hosted server is read-heavy with only debug sessions as write operations. The community Traefik server is entirely read-only. This asymmetry makes sense for safety but limits what agents can do autonomously.

**The MCP gateway space is fragmented.** AgentGateway, Envoy AI Gateway, Kong AI Gateway, Traefik Hub, and Cloudflare Portals are all competing approaches with different architectures. No clear standard has emerged for how MCP traffic should be governed at scale.

**Cloudflare's Code Mode is brilliant but unproven at scale** in the broader ecosystem. The 2-tool pattern requires models that can reliably write JavaScript to query API specs — not all models or use cases can handle this. Traditional per-tool MCP servers are more predictable for simpler models.

## The Bottom Line

**For managing Kong Gateway:** Use the official Kong Konnect hosted MCP server. Zero setup, 12 tools, active development.

**For managing APISIX:** Use api7/apisix-mcp. 30+ tools covering the full Admin API. The most complete gateway management MCP server available.

**For managing Cloudflare:** Use cloudflare/mcp (Code Mode). 2 tools covering 2,500+ endpoints is remarkable efficiency. Fall back to cloudflare/mcp-server-cloudflare for specific product integrations.

**For MCP traffic governance:** AgentGateway (1,900 stars, Rust, Solo.io-backed) is the current open-source leader. Envoy AI Gateway (1,400 stars) is the choice if you're already in the Envoy ecosystem. Kong and Traefik Hub offer commercial options integrated with their existing gateway products.

**For converting existing APIs to MCP:** Google Apigee (zero-code, enterprise governance) and Kong AI Gateway (plugin-based API-to-MCP conversion) are the most mature approaches.

**Rating: 3.5/5** — The gateway management MCP servers (Kong, APISIX, Cloudflare) are genuinely useful. But the ecosystem is immature: most servers are read-only, star counts are low (except Cloudflare), and the MCP gateway infrastructure space is too fragmented to recommend confidently. Cloudflare's Code Mode innovation deserves attention, but the category needs another 6-12 months to consolidate.

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*


---
title: "API Gateway MCP Servers — Kong, APISIX, Cloudflare, Envoy, Traefik, and Beyond"
date: 2026-03-15T03:56:00+09:00
description: "API gateway MCP servers let AI agents manage routes, services, plugins, and traffic across Kong, APISIX, Cloudflare, Traefik, Gravitee, and more."
og_description: "15+ API gateway MCP servers reviewed — Kong, APISIX, Cloudflare, Envoy, Traefik, Gravitee, Apigee, and AgentGateway. Honest ratings and recommendations."
content_type: "Review"
card_description: "API gateway MCP servers across Kong, APISIX, Cloudflare, Envoy, Traefik, Gravitee, Apigee, AgentGateway, and new entrants. AgentGateway is past 4,300 stars (v1.4.1, following the v1.2.0 CEL policies/route delegation/agctl debugger/post-quantum TLS release). Envoy AI Gateway reached v1.0 General Availability in June 2026, with MCPRoute stable at v1beta1. Google Apigee API Hub adds MCP Tools in Public Preview. Docker MCP Gateway actively shipping. Databricks Unity AI Gateway enters with MCP governance in Unity Catalog."
last_refreshed: 2026-05-20
sources_audited: 2026-08-14
---

API gateways sit at the intersection of every API call in production infrastructure. Making them accessible to AI agents unlocks powerful capabilities: **natural language route configuration, automated traffic analysis, real-time debugging, and intelligent plugin management**. But this category splits into two distinct stories.

**Story one: MCP servers for managing API gateways** — tools that let AI agents configure routes, analyze traffic, and troubleshoot services on platforms like Kong, APISIX, and Traefik. **Story two: API gateways acting as MCP infrastructure** — platforms like Envoy AI Gateway, AgentGateway, Traefik Hub, and Cloudflare that route, secure, and govern MCP traffic itself. Both matter. This review covers the full picture.

The headline, as this review's core snapshot was written (April-May 2026), with updates noted where things have since moved: **AgentGateway shipped v1.2.1 with CEL-based conditional policies, route delegation, a new `agctl` CLI debugger, and post-quantum TLS** — it's since kept shipping and is past 4,300 stars and v1.4.1 as of this audit. **Envoy AI Gateway v0.6.0 (May 5, 2026) graduated MCPRoute to v1beta1 — the first production-ready MCP routing CRD in any gateway project at the time — with v1.0 GA targeted for June 2026; that GA shipped on schedule on June 23, 2026.** **Google Apigee API Hub added MCP Tools and MCP Discovery Proxies in Public Preview (April-May 2026).** **Docker MCP Gateway is actively shipping** (v0.42.0–v0.42.1 in late April/early May, and multiple releases since). And **Databricks Unity AI Gateway entered the MCP governance space** with fine-grained permissions inside Unity Catalog.

**Category:** [Developer Tools](/categories/developer-tools/)

## Part 1: MCP Servers for Managing API Gateways

### Kong Konnect (Official, Hosted)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [Kong Konnect MCP](https://developer.konghq.com/konnect-platform/konnect-mcp/) | N/A (hosted) | N/A | 3-4 | Konnect account | Streamable HTTP |

**Kong's official hosted MCP server is a polished API gateway management experience** with zero-install remote hosting — connect directly from Claude, Cursor, VS Code, or any MCP client.

**As of the current [Kong Konnect MCP docs](https://developer.konghq.com/konnect-platform/konnect-mcp/), the server uses a search/execute pattern rather than dozens of named per-resource tools:** `search` (finds relevant API operations from a natural-language description), `get_schema` (retrieves the schema for a specific operation), and `execute` (calls the operation with the resolved inputs) — plus an optional `KnowledgeBase` tool when Kong's KAi assistant is enabled, for querying Kong documentation. This is the same "Code Mode"-style, small-tool-count approach Cloudflare popularized (see the Cloudflare section below) rather than a large fixed toolset of individually-named operations.

This still covers the same ground as the [Konnect product page](https://konghq.com/products/kong-konnect/agents) advertises: querying gateway topology (services, routes, plugins, consumers, vaults), control-plane/multi-cluster visibility, and traffic analytics — but discovered dynamically through `search`/`get_schema` rather than exposed as one tool per operation.

**MCP Registry ([tech preview, announced February 2, 2026](https://konghq.com/company/press-room/press-release/kong-introduces-mcp-registry)):** Enterprise directory within the Kong Konnect Catalog for registering, discovering, and governing MCP servers and AI-native tools, compliant with the AI Alliance Interoperability Framework (AAIF). Kong also published an AWS reference architecture for GenAI MCP and A2A gateways: [github.com/Kong/guidance-for-kong-genai-mcp-and-a2a-gateways-on-aws](https://github.com/Kong/guidance-for-kong-genai-mcp-and-a2a-gateways-on-aws).

**Deprecated predecessor: [Kong/mcp-konnect](https://github.com/Kong/mcp-konnect)** — 44 stars, 17 forks, TypeScript, Apache 2.0, 19 commits. Formally archived (read-only) as of August 9, 2026, per the repo's own deprecation notice, which directs users to the hosted Konnect MCP server above. Had analytics and configuration read tools but was self-hosted only.

### Apache APISIX (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [api7/apisix-mcp](https://github.com/api7/apisix-mcp) | ~38 | TypeScript | 30+ | Admin API key | stdio |

**APISIX's MCP server provides the deepest API gateway management capabilities of any server in this review — but development has stalled.** 38 stars, 17 forks, Apache 2.0, npm package [`apisix-mcp` v0.0.7](https://www.npmjs.com/package/apisix-mcp) (last published April 2025). Last commit June 2025 — now 14+ months without activity.

30+ tools covering full CRUD on every APISIX resource type: **Routes** (create_route, update_route, delete_route), **Services** (create_service, update_service, delete_service), **Upstreams** (create_upstream, update_upstream, delete_upstream), **SSL certificates** (create_ssl, update_ssl, delete_ssl), **Consumers and credentials** (create_or_update_consumer, delete_consumer, get_credential, create_or_update_credential, delete_credential), **Consumer groups** (create_consumer_group, delete_consumer_group), **Plugins** (get_all_plugin_names, get_plugin_info, get_plugins_by_type, get_plugin_schema, create_plugin_config, update_plugin_config), **Global rules** (create_global_rule, update_global_rule), **Plugin metadata** (get_plugin_metadata, create_or_update_plugin_metadata, delete_plugin_metadata), **Secrets** (get_secret_by_id, create_secret, update_secret), **Proto definitions** (create_or_update_proto), **Stream routes** (create_or_update_stream_route), plus **get_resource** (generic retrieval) and **send_request_to_gateway** (test requests).

This is essentially the entire APISIX Admin API exposed as MCP tools. For teams running APISIX, this means AI agents can handle the complete gateway lifecycle: "Create a new route for /api/v3/users pointing to upstream-cluster-2 with rate limiting and JWT auth" → agent creates the route, configures plugins, tests the endpoint.

**Concern: with no commits in 14+ months, compatibility with newer APISIX versions is uncertain.** The [PulseMCP listing](https://www.pulsemcp.com/servers/api7-apisix) shows roughly 14,200 estimated total visitors — there's apparent user demand, but no maintainer activity to match.

### Cloudflare API (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [cloudflare/mcp](https://github.com/cloudflare/mcp) | ~729 | TypeScript | 2 | OAuth 2.1 / API token | Streamable HTTP |

**Cloudflare's MCP server uses the most architecturally innovative approach we've seen in any MCP server category — and Code Mode is the default on all MCP Server Portals.** 729 stars, 92 forks, Apache 2.0, actively maintained. Per [Cloudflare's own writeup](https://blog.cloudflare.com/code-mode-mcp/), the Cloudflare API has over 2,500 endpoints; exposing each as an individual MCP tool would consume roughly 1.17 million tokens of context. "Code Mode" instead uses just 2 tools in roughly 1,000 tokens of context — a **99.9% reduction**.

The two tools: **search** (agent writes JavaScript to query `spec.paths` and find endpoints by iterating the API specification server-side) and **execute** (agent writes JavaScript to call `cloudflare.request()` with discovered endpoints). The specification lives on the server — only execution results return to the agent.

Code Mode applies the same idea to **MCP Server Portals** (Cloudflare's gateway product for composing third-party MCP servers, covered separately below) — but there the default shape is different: [per Cloudflare's changelog](https://developers.cloudflare.com/changelog/post/2026-03-26-mcp-portal-code-mode/), Code Mode is on by default on all portals and exposes a single `code` tool rather than listing every tool from every upstream server. The `search`/`execute` two-tool pattern is available as an explicit option — append `?codemode=search_and_execute` to the portal URL — or Code Mode can be disabled entirely via the Access dashboard. The generated code runs in an isolated Dynamic Worker environment, keeping credentials and environment variables out of the model context.

This covers the *entire* Cloudflare API: DNS, Workers, R2 storage, Zero Trust, AI Gateway, D1, KV, Queues, Pages, and every other Cloudflare product. When Cloudflare adds new products, the same search/execute pattern discovers them — no new tool definitions needed.

**Authentication:** OAuth 2.1 (recommended, uses Workers OAuth Provider to downscope tokens) or API tokens with automatic account ID detection for account-scoped tokens.

**Also notable: [cloudflare/mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare)** — 4,072 stars, 476 forks, TypeScript, Apache 2.0, actively released as an independently-versioned monorepo (e.g. `workers-bindings@0.5.5` as of this audit). Now **16 product-specific MCP servers** (Documentation, Workers Bindings, Workers Builds, Observability, Radar, Container, Browser Rendering, Logpush, AI Gateway, AI Search, AutoRAG, Audit Logs, DNS Analytics, Digital Experience Monitoring, CASB, GraphQL). Still active and useful for specific product integrations, but Code Mode represents where Cloudflare is heading.

### Traefik (Community)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [theupriser/treafik-mcp](https://github.com/theupriser/treafik-mcp) | ~4 | Python | 6 | Bearer/basic auth | stdio |

**A minimal community server for reading Traefik configurations.** 4 stars, 8 commits, MIT. Phase 1 complete with read-only tools.

6 tools: **get_traefik_overview** (component summary), **list_routers** (HTTP routers with provider filtering), **get_router_details** (specific router config), **list_services** (HTTP services), **get_service_details** (specific service config), **list_middlewares** (HTTP middlewares). Provider-specific filtering supports Docker, file, and other Traefik providers.

Phase 2 planned but not implemented: dynamic configuration updates, health monitoring, advanced filtering. This is currently read-only — useful for inspection but not management.

### Gravitee APIM (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [gravitee-io/gravitee-apim-mcp-server](https://github.com/gravitee-io/gravitee-apim-mcp-server) | ~2 | TypeScript | Dynamic | Bearer token | stdio |

**Gravitee's official MCP server is auto-generated from the Management API v2 OpenAPI specification.** 2 stars, 3 forks, MIT. **Correction:** this page previously described the repo as dormant since September 2025 — that's no longer accurate. It has since shipped a feature update for APIM 4.12 (July 1, 2026) and two tagged releases, `v0.2.0` and `v0.2.1` (July 22, 2026), so the open-source server is actively maintained, not dormant.

Tools are dynamically generated — covering API listing/retrieval, health monitoring, API creation/configuration, plan management, API lifecycle (start/stop), and environment operations.

**Gravitee 4.11 ([April 7, 2026](https://www.gravitee.io/blog/gravitee-4.11-protect-optimise-and-govern-your-ai-stack))** significantly expanded MCP capabilities on the platform side: dedicated MCP analytics dashboard in APIM Console, RFC 8693-based agent delegation for A2A workflows, an Agent Tool Server in the Developer Portal for publishing tools to AI agents, and [MCP Resource Server V2](https://www.gravitee.io/blog/elevating-mcp-security-with-gravitees-mcp-resource-server-v2) adding full Client Credentials flows and production-grade secret management. The Agent Mesh suite (Agent Gateway, Agent Catalog, Agent Tool Server) is the enterprise product; the open-source MCP server above is the entry point and is now being actively developed alongside it.

### Nginx Proxy Manager (Community)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [b3nw/nginx-proxy-manager-mcp](https://github.com/b3nw/nginx-proxy-manager-mcp) | ~10 | Python | Multiple | NPM credentials | stdio |

**A community server for Nginx Proxy Manager**, enabling AI agents to manage reverse proxy configurations. Provides CRUD operations on proxy hosts, SSL certificates, and access lists through the NPM API. Useful for homelab and small-scale deployments where Nginx Proxy Manager is already the management layer.

Not to be confused with Nginx itself (which has no MCP server) — this specifically targets the Nginx Proxy Manager web interface API.

## Part 2: MCP Gateways (API Gateways for MCP Traffic)

A rapidly maturing subcategory: platforms that don't just expose their *own* API via MCP, but act as **infrastructure for routing, securing, and governing MCP traffic** between agents and tools. This space is expanding quickly with Docker, Databricks, and Higress all entering in 2026.

### AgentGateway (Solo.io / Linux Foundation)

| Project | Stars | Language | License | Latest |
|---------|-------|----------|---------|--------|
| [agentgateway/agentgateway](https://github.com/agentgateway/agentgateway) | ~4,346 | Rust/Go/TS | Apache 2.0 | v1.4.1 (July 29, 2026) |

**The largest open-source MCP gateway project, now at 4,346 stars with an accelerating release cadence.** 725+ forks, actively pushed. [Donated to the Linux Foundation on August 25, 2025](https://www.linuxfoundation.org/press/linux-foundation-welcomes-agentgateway-project-to-accelerate-ai-agent-adoption-while-maintaining-security-observability-and-governance); v1.0.0 shipped March 16, 2026. Built in Rust for high performance. Releases have continued past the v1.2.x line covered below — v1.4.1 (July 29, 2026) is the latest as of this audit, with fixes to MCP/LLM compatibility and Bedrock request handling.

Per the [Linux Foundation's announcement](https://www.linuxfoundation.org/press/linux-foundation-welcomes-agentgateway-project-to-accelerate-ai-agent-adoption-while-maintaining-security-observability-and-governance), agentgateway is "an open source, AI-native proxy" providing "drop-in security, observability, and governance for agent-to-LLM, agent-to-tool, and agent-to-agent communication." Core capabilities: MCP/A2A-focused RBAC, multi-tenant isolation, xDS-based dynamic configuration (Envoy-style), OpenAPI-to-MCP transformation (legacy API integration), and a built-in Kubernetes controller via Gateway API.

**[v1.2.0](https://github.com/agentgateway/agentgateway/releases/tag/v1.2.0) (May 14, 2026) — major feature release:**
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
| [envoyproxy/ai-gateway](https://github.com/envoyproxy/ai-gateway) | ~1,925 | Go | Apache 2.0 | v1.0.0 (June 23, 2026) |

**Update since this review was first written: Envoy AI Gateway [reached v1.0 General Availability on June 23, 2026](https://aigateway.envoyproxy.io/blog/v1.0-release-announcement/)** — the GA target described below did arrive on schedule. 1,925 stars, 330 forks. Per the [GA announcement](https://aigateway.envoyproxy.io/blog/v1.0-release-announcement/) and [Tetrate's press release](https://tetrate.io/press/envoy-ai-gateway-reaches-v1-0-establishing-the-open-source-standard-for-enterprise-ai-traffic), the core control-plane API — `AIGatewayRoute`, `AIServiceBackend`, `BackendSecurityPolicy`, `GatewayConfig`, and `MCPRoute` — is now stable at `v1beta1`, with a commitment that the 1.x series won't ship breaking changes outside critical security fixes.

**Envoy AI Gateway v0.6.0 (May 5, 2026)** was the release that got it there: MCPRoute graduated to v1beta1, making it (at the time) the first production-ready MCP routing CRD in any open-source gateway.

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

At the time of the v0.6.0 release, items like OAuth 2.0 token exchange, quota rate limiting, PII redaction processors, and audio endpoint support were still in progress for v1.0. Per the [v1.0 GA announcement](https://aigateway.envoyproxy.io/blog/v1.0-release-announcement/), the shipped v1.0 covers 16 LLM providers, an MCP gateway, multimodal and audio endpoints, and enterprise observability.

Can run in standalone mode with your existing MCP servers config file — meaning you can put Envoy in front of servers you're already running with Claude Code or Cursor without reconfiguration. [Tetrate's published MCP performance benchmarks](https://tetrate.io/blog/envoy-ai-gateway-mcp-performance) show most of the proxy overhead comes from session-encryption key derivation rather than MCP traffic handling itself — tuned encryption settings bring per-session overhead down to roughly 1-2ms.

### Kong AI Gateway + Agent Gateway

[Kong Gateway 3.14](https://konghq.com/blog/product-releases/kong-agent-gateway) (April 14, 2026) launched **Kong Agent Gateway** — Kong's AI gateway extension for the agentic era, adding full Agent-to-Agent protocol support on top of MCP plugins introduced in Gateway 3.12+: [AI MCP Proxy](https://developer.konghq.com/plugins/ai-mcp-proxy/) (protocol bridge between MCP and HTTP), [AI MCP OAuth2](https://developer.konghq.com/plugins/ai-mcp-oauth2/) (OAuth 2.0 for MCP servers), and MCP-specific metrics added to the [Prometheus plugin](https://developer.konghq.com/plugins/prometheus/) (response size, latency, and error-total histograms/counters for MCP server calls).

Kong's enterprise MCP Gateway addresses server sprawl, security gaps, and cost management for organizations running many MCP servers. The gateway converts RESTful APIs defined as Kong Gateway Services into MCP tools automatically — acting as a protocol bridge between MCP and HTTP. [Kong Gateway 3.15 shipped July 2, 2026](https://konghq.com/blog/product-releases/kong-api-gateway-3-15) as an LTS release, bringing Conditional Policy Execution (CEL) to general availability — not itself an MCP feature, but confirmation the quarterly cadence held.

### Docker MCP Gateway

| Project | Stars | Language | License | Latest |
|---------|-------|----------|---------|--------|
| [docker/mcp-gateway](https://github.com/docker/mcp-gateway) | ~1,527 | Go | MIT | v0.43.3 (July 16, 2026) |

**Docker's MCP gateway is quietly one of the most actively shipped projects in this category.** 1,527 stars, 261 forks. v0.42.0 (April 30, 2026) added npm/npx server support and fixed OAuth token exchange; [v0.42.1](https://github.com/docker/mcp-gateway/releases/tag/v0.42.1) (May 5) removed the McpGatewayOAuth feature flag, making OAuth a first-class feature. Shipping has continued past that point — v0.43.3 (July 16, 2026) is the latest as of this audit. For teams already running Docker infrastructure, this integrates naturally with Docker Desktop and Docker Hub tooling.

### Traefik Hub MCP Gateway (Triple Gate)

Traefik Hub's MCP Gateway (commercial) adds OAuth-compliant proxying with **Task-Based Access Control (TBAC)** — a novel approach where access policies are defined per-tool rather than per-user or per-role. Centralized access control, resource metadata discovery, and fine-grained policy enforcement for MCP tools and resources.

**v3.20 ([announced March 15, 2026](https://traefik.io/press/traefik-labs-new-multi-vendor-composable-ai-safety-pipeline) at NVIDIA GTC; GA late April 2026): Triple Gate architecture** with a composable, multi-vendor safety pipeline (parallel guard execution), multi-provider failover routing, token-level cost controls, and graceful error handling — guardrail blocks now return a structured HTTP 200 refusal response instead of the HTTP 403 that used to break agent control flow. Also new: IBM Granite Guardian integration for harm/jailbreak/hallucination detection, and a Regex Guard for custom, sub-millisecond pattern-matching content filtering. The "Triple Gate" (API Gateway + AI Gateway + MCP Gateway) positions Traefik Hub as a unified infrastructure-layer governance solution from public cloud to air-gapped environments.

### Cloudflare MCP Server Portals

[Open Beta launched August 26, 2025](https://blog.cloudflare.com/zero-trust-mcp-server-portals/). Compose multiple MCP servers behind a single gateway with unified auth and access control. Instead of distributing dozens of individual server endpoints, register servers with Cloudflare and provide users a single Portal endpoint. Zero Trust security model applied to MCP infrastructure. **[As of March 26, 2026, Code Mode is on by default on all portals](https://developers.cloudflare.com/changelog/post/2026-03-26-mcp-portal-code-mode/)** — the portal exposes a single `code` tool instead of listing every tool from every upstream server, so context usage stays fixed regardless of how many tools are available.

### Google Apigee

Apigee provides **native, zero-code MCP support** — it dynamically discovers existing Apigee-managed API Products and their OpenAPI specifications, then exposes them as MCP tools. No code changes to existing APIs, no new servers to deploy or manage. Apigee handles infrastructure, transcoding, identity, authorization, and analytics for MCP endpoints.

**April–May 2026 updates — the most active update window for Apigee MCP yet:**

- **[Apigee API Hub — Agent Registry integration (April 6)](https://docs.cloud.google.com/apigee/docs/apihub/release-notes):** API Hub now includes a managed integration with Agent Registry to automatically sync MCP server and tool metadata, so AI agents can discover APIs registered in the hub without manual configuration. (Public Preview.)
- **[Apigee Hybrid v1.16.1 (April 20)](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes):** Broader set of MCP methods supported; governance bypass for essential system-level operations.
- **[Apigee API Hub — Unified MCP Proxy Configuration, i.e. MCP Discovery Proxies (May 7)](https://docs.cloud.google.com/apigee/docs/apihub/release-notes):** Select API operations from your catalog, bundle into an MCP server, and auto-deploy as a discovery proxy — without writing a spec. (Public Preview.)
- **[Apigee API Hub — MCP Tools in Public Preview (May 12)](https://docs.cloud.google.com/apigee/docs/apihub/release-notes):** API Hub now exposes read-only APIs directly as MCP tools — agentic AI applications can use standard `tools/list` and `tools/call` methods to list and inspect API Hub resources.
- **[Apigee Hybrid v1.16.2 (May 13)](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes):** Critical security fix — `LLMTokenQuota` operations were not enforcing model-based access restrictions; patched.

This is arguably the most enterprise-ready approach: existing API governance (rate limits, quotas, analytics, security policies) automatically applies to MCP tool invocations. The April-May Public Preview additions (Agent Registry sync, MCP Discovery Proxies, MCP Tools) meaningfully reduce the friction of bringing an existing API catalog into the MCP ecosystem.

### Databricks Unity AI Gateway (NEW)

**[Databricks rebranded and expanded AI Gateway as "Unity AI Gateway" (April 15, 2026)](https://www.databricks.com/blog/ai-gateway-governance-layer-agentic-ai)**, integrating it into Unity Catalog for unified data + AI governance. The key MCP addition: fine-grained permissions governing which AI agents can access external systems via MCP, with On-Behalf-Of (OBO) access and complete end-to-end observability for LLM and MCP calls. Rate limiting, fallback routing, and cost controls span model providers. For organizations already on Databricks, this is the natural governance layer for MCP traffic — no separate gateway to deploy.

### Higress API Gateway (MCP)

**Higress** (an AI-native API gateway originally built at Alibaba, [accepted into CNCF as a Sandbox project on March 15, 2026](https://www.cncf.io/projects/higress/)) added two MCP-related capabilities in 2026, [per Higress's own release post](https://higress.ai/en/blog/higress-adds-api-authentication-capability-for-mcp-servers-to-backend-services): API authentication for MCP server connections to backend services (both client-to-gateway and gateway-to-backend auth, via Key Auth, JWT Auth, and OAuth2), plus a new `mcp-proxy` server type that proxies client MCP requests to backend MCP servers, offloading state-maintaining tasks from those backend servers. Significant for teams in the cloud-native CNCF ecosystem already running Higress.

### Tyk AI Studio

Tyk's API-to-MCP bridge converts REST, GraphQL, and RPC endpoints into standardized MCP tools. **[March 2026: Tyk AI Studio went open source](https://tyk.io/blog/ai-studio-is-going-open-source-and-why-the-ai-control-plane-must-be-extensible/)** (Community Edition, no license required, available via the [ai-studio GitHub repo](https://github.com/TykTechnologies/ai-studio)). Capabilities: MCP tool generation from OpenAPI specs, scoped tool access policies with guardrails, complete audit trails for prompts/responses/tool calls, PII redaction and content filtering at the gateway, and enterprise SSO/RBAC (Enterprise Edition). Previously commercial-only, the open-source release significantly lowers the barrier to entry for self-hosted AI governance.

### Microsoft MCP Gateway

| Project | Stars | Language | License | Latest |
|---------|-------|----------|---------|--------|
| [microsoft/mcp-gateway](https://github.com/microsoft/mcp-gateway) | ~783 | C# | MIT | no tagged releases; actively committed |

**Microsoft's Kubernetes-native MCP gateway, now at 783 stars.** 85 forks, created May 2025, still actively pushed (most recent commit as of this audit: August 12, 2026). **Correction:** this page previously listed the implementation language as Go — the repo is actually written in C# (ASP.NET Core). A reverse proxy and management layer for MCP servers with:

- **Session-aware stateful routing** — all requests with a given session_id consistently route to the same MCP server instance via StatefulSets and headless services
- **Control plane** for MCP server lifecycle management (deploy, update, delete)
- **Tool registration with dynamic routing** — scalable architecture for managing and executing MCP tools
- **Azure Entra ID (AAD)** OAuth 2.0 authentication
- **Enterprise-ready** telemetry, access control, and observability integration points

For organizations already running Kubernetes on Azure, this is the natural fit. The Kubernetes-native approach (StatefulSets for session affinity, headless services for direct pod routing) is architecturally sound for MCP's stateful protocol requirements.

## Gaps and Limitations

**No Nginx MCP server** — [Nginx is the world's most-used web server](https://w3techs.com/technologies/overview/web_server) (31.4% of sites whose server is known, per W3Techs, ahead of Apache at 22.7%) and is very commonly deployed as a reverse proxy, yet it has no MCP integration for managing its own configurations (only Nginx Proxy Manager has one). **No HAProxy MCP server.** No **Istio** or **Linkerd** service mesh MCP servers for managing mesh configurations.

**APISIX is write-capable but dormant; most others are read-only.** Kong Konnect's hosted server is read-heavy, discovering operations dynamically via search/execute rather than exposing dedicated write tools. The community Traefik server is entirely read-only. APISIX hasn't been updated in 14+ months. This asymmetry makes sense for safety but limits what agents can do autonomously.

**The MCP gateway space is expanding, not converging.** AgentGateway, Envoy AI Gateway, Kong Agent Gateway, Traefik Hub, Microsoft MCP Gateway, Cloudflare Portals, Docker MCP Gateway, Databricks Unity AI Gateway, and Higress are all active approaches with different architectures and target ecosystems. AgentGateway's v1.x cadence and Envoy's v0.6.0 graduation suggest open-source leadership is becoming clearer, but enterprise buyers will choose based on their existing infrastructure.

**Cloudflare's Code Mode is proven and now the default** on both the direct Cloudflare API server (2-tool search/execute pattern) and MCP Server Portals (single-tool `code` pattern) — a validation of the small-tool-count approach generally. But it still requires models that can reliably write JavaScript to query API specs, which limits compatibility with simpler models.

## The Bottom Line

**For managing Kong Gateway:** Use the official Kong Konnect hosted MCP server. Zero setup, search/execute tool discovery, active development. The MCP Registry tech preview adds discovery and governance.

**For managing APISIX:** Use api7/apisix-mcp — 30+ tools covering the full Admin API. But be aware the server hasn't been updated since June 2025 (14+ months); test against your APISIX version before deploying.

**For managing Cloudflare:** Use cloudflare/mcp (Code Mode). 2 tools covering 2,500+ endpoints. Code Mode (in its single-tool `code` form) is also the default on MCP Server Portals. Fall back to cloudflare/mcp-server-cloudflare (4,072 stars, 16 product servers) for specific product integrations.

**For MCP traffic governance — open source:** AgentGateway (4,346 stars, Rust, Linux Foundation, Solo.io-backed, v1.4.1) is the open-source leader with the most active release cadence. Envoy AI Gateway (1,925 stars, v1.0.0 GA as of June 2026, MCPRoute v1beta1) is the best-engineered choice if you're already in the Envoy/Kubernetes ecosystem.

**For MCP traffic governance — enterprise/cloud:** Kong Agent Gateway (3.14) is still the first to unify LLM+MCP+A2A governance. Microsoft MCP Gateway (783 stars) for Azure/Kubernetes shops. Databricks Unity AI Gateway for teams on the Databricks Lakehouse platform. Google Apigee for organizations with existing API catalogs — the April-May 2026 API Hub additions dramatically lower the barrier to entry.

**For converting existing APIs to MCP:** Google Apigee (zero-code, now with MCP Discovery Proxies and MCP Tools in Public Preview) and Kong AI Gateway (plugin-based API-to-MCP conversion) are the most mature. Tyk AI Studio (now open source) is the best self-hosted option. Docker MCP Gateway for teams already on Docker infrastructure.

**Rating: 4/5** — Held. The market is expanding faster than it is consolidating. Envoy's v1.0 GA (June 2026) is a meaningful maturity signal, following on from the v0.6.0 MCPRoute v1beta1 graduation covered above; AgentGateway's release cadence (now past v1.4) is impressive; Apigee's API Hub Public Preview meaningfully lowers the barrier for enterprise API catalogs. New entrants (Docker, Databricks, Higress) validate the category. The persistent gap remains on the management side — APISIX has 30+ write tools but is dormant, and most gateway management servers are still read-only. When that changes, the rating moves to 4.5.

*This review was last edited on 2026-05-20 using Claude Sonnet 4.6 (Anthropic).*

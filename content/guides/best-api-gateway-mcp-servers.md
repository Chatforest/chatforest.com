---
title: "Best API Gateway & API Management MCP Servers in 2026 — Kong vs Cloudflare vs Traefik vs AWS vs Azure vs Open Source"
date: 2026-03-22T14:30:00+09:00
description: "We compared 20+ API gateway and API management MCP servers across Kong, Cloudflare, Traefik, AWS API Gateway, Azure APIM, Apigee, Gravitee, Apache APISIX, Tyk, and open-source gateways like Bifrost and ContextForge. Here's which ones are worth using — and where the gaps still are."
og_description: "20+ API gateway MCP servers compared: Cloudflare (2,500+ endpoints, Code Mode), Kong Konnect (12 hosted tools), Traefik Hub (MCP Gateway, TBAC), AWS API Gateway (MCP proxy), Azure APIM, Apigee (zero-code), Gravitee (60+ tools), Bifrost (3.1K stars), ContextForge (3.5K stars). Honest recommendations from research."
content_type: "Comparison"
card_description: "Cloudflare (2,500+ endpoints, 2-tool Code Mode) vs Kong Konnect (hosted, 12 tools) vs Traefik Hub (MCP Gateway, TBAC, OTel) vs AWS API Gateway (MCP proxy) vs Azure APIM (REST-to-MCP) vs Apigee (zero-code MCP) vs Gravitee (60+ tools) vs Bifrost (3.1K stars, Go) vs ContextForge (3.5K stars, federation) — plus APISIX, Tyk, Lasso Security, Peta, and Agent Gateway."
last_refreshed: 2026-03-22
---

API gateways are the front door to every microservice, and now AI agents can manage routes, inspect traffic, configure plugins, analyze analytics, and even generate entire API clients — all through MCP. The convergence of API management and agentic AI is happening fast: Gartner projects 75% of API gateway vendors will integrate MCP features by end of 2026.

The landscape splits into three layers. **Vendor management servers** (Kong, Cloudflare, Gravitee, APISIX, Tyk) let you manage your gateway through natural language. **Cloud platform MCP proxies** (AWS API Gateway, Azure APIM, Google Apigee) turn your existing REST APIs into MCP-compatible tools with zero code changes. And **MCP-native gateways** (Traefik Hub, Bifrost, ContextForge, Agent Gateway, Lasso, Peta) are purpose-built to sit between AI agents and MCP servers, adding auth, observability, rate limiting, and security scanning.

What surprised us: **Cloudflare's Code Mode** collapsed 2,500+ API endpoints into just 2 tools and ~1,000 tokens — a 99.9% reduction in context usage. **Google Apigee** requires zero code, zero servers, and zero changes to existing APIs — it just works. **IBM ContextForge** hit 3.5K stars in months as the open-source federation gateway. And **Traefik Hub** introduced Task-Based Access Control (TBAC), an entirely new authorization paradigm for MCP tool governance.

**Disclosure:** Our recommendations are based on research — analyzing documentation, GitHub repositories, community feedback, and published benchmarks. We have not hands-on tested every server in this guide.

## At a Glance: Top Picks

| Category | Our pick | Stars | Runner-up |
|----------|----------|-------|-----------|
| **Gateway management** | [Cloudflare MCP](https://github.com/cloudflare/mcp) | 263 | [Gravitee APIM MCP](https://github.com/gravitee-io/gravitee-apim-mcp-server) (60+ tools) |
| **Hosted platform** | [Kong Konnect](https://konghq.com/products/kong-konnect/agents) | Hosted | [Apigee](https://cloud.google.com/blog/products/ai-machine-learning/mcp-support-for-apigee) (zero-code) |
| **Cloud MCP proxy** | [AWS API Gateway](https://aws.amazon.com/about-aws/whats-new/2025/12/api-gateway-mcp-proxy-support/) | Official | [Azure APIM](https://learn.microsoft.com/en-us/azure/api-management/mcp-server-overview) (REST-to-MCP) |
| **MCP-native gateway** | [Traefik Hub](https://traefik.io/solutions/mcp-gateway) | Commercial | [IBM ContextForge](https://github.com/IBM/mcp-context-forge) (3.5K, open source) |
| **Open-source gateway** | [IBM ContextForge](https://github.com/IBM/mcp-context-forge) | 3,500 | [Bifrost](https://github.com/maximhq/bifrost) (3.1K, Go) |
| **Agent proxy** | [Agent Gateway](https://github.com/agentgateway/agentgateway) | 2,100 | [Lasso Security](https://github.com/lasso-security/mcp-gateway) (360, security-first) |
| **Credential vault** | [Peta](https://github.com/dunialabs/peta-core) | 39 | — |
| **Open-source gateway mgmt** | [APISIX MCP](https://github.com/api7/apisix-mcp) | 25 | [Tyk api-to-mcp](https://github.com/TykTechnologies/api-to-mcp) |

## Vendor Gateway Management Servers

These MCP servers let you manage an existing API gateway through natural language — inspect routes, configure plugins, analyze traffic, and manage lifecycle.

### Cloudflare MCP — The Winner (Gateway Management)

**Stars:** 263 | **Language:** TypeScript | **Tools:** 2 (Code Mode) | **Transport:** Remote MCP (hosted)

Cloudflare's MCP server takes a radically different approach. Instead of exposing hundreds of individual tools, it uses **Code Mode** — two tools (`search()` and `execute()`) that give agents access to all 2,500+ Cloudflare API endpoints through generated JavaScript that runs in a sandboxed Worker isolate.

**What makes it stand out:**
- **Code Mode** — the agent writes JavaScript against the typed API spec, and only the result comes back. This collapses 2,500+ endpoints into ~1,000 tokens of context — a 99.9% reduction vs. traditional tool definitions
- **Zero-install remote** — point your MCP client at `mcp.cloudflare.com/mcp` and authenticate via OAuth. No npm install, no Docker, no config files
- **Full API surface** — DNS, Workers, R2, Zero Trust, WAF, Page Rules, Load Balancing, and every other Cloudflare product
- **Sandboxed execution** — generated code runs inside an isolated Dynamic Worker, not on your machine
- **Progressive discovery** — agents search the spec to find what they need, rather than loading everything upfront

**Limitations:**
- **Cloudflare-only** — manages Cloudflare services, not a generic API gateway management tool
- Code Mode is a novel pattern — agents need to be capable enough to write correct JavaScript against the API spec
- The old `mcp-server-cloudflare` repo (deprecated) had more traditional tool definitions; Code Mode requires adaptation

**Best for:** Cloudflare customers who want full API control from their AI assistant without bloating the context window. The architectural pattern (Code Mode) is worth studying even if you don't use Cloudflare.

### Kong Konnect MCP — The Enterprise Platform

**Stars:** Hosted (deprecated OSS) | **Language:** TypeScript | **Tools:** 12 | **Transport:** Remote MCP (hosted)

Kong's official MCP server connects AI assistants to the Kong Konnect platform for querying analytics, inspecting configurations, and managing control planes.

**What makes it stand out:**
- **Hosted remote endpoint** — no local install needed, Konnect manages the server
- **12 tools** across analytics, configuration (services, routes, consumers, plugins), and control plane management
- **MCP Registry** (announced Feb 2026) — enterprise directory within Konnect Catalog for registering, discovering, and governing MCP servers
- **MCP Composer + Runner** (coming 2026) — auto-generate MCP servers from REST APIs with centralized OAuth
- **AI Gateway 3.12** — Kong's gateway natively supports MCP, enabling API-to-MCP conversion at the infrastructure level

**Limitations:**
- **Konnect-only** — requires Kong Konnect subscription (not open-source Kong Gateway)
- The original open-source `Kong/mcp-konnect` repo is now archived and deprecated
- 12 tools is modest compared to Cloudflare's full API surface or Gravitee's 60+ tools
- MCP Registry and Composer are tech preview / coming soon — not generally available yet

**Best for:** Kong Konnect enterprise customers who want natural language gateway management and are planning for the MCP Registry ecosystem.

### Gravitee APIM MCP — The Tool-Rich Alternative

**Stars:** Open source | **Language:** TypeScript | **Tools:** 60+ | **Transport:** stdio

Gravitee's MCP server is generated from the official Gravitee Management API v2 OpenAPI spec, exposing the full API Management platform as MCP tools.

**What makes it stand out:**
- **60+ tools** — the highest tool count of any gateway management MCP server. Covers APIs, plans, subscriptions, environments, deployments, and lifecycle
- **Conversational API management** — ask questions about your APIs in natural language
- **MCP Proxy** (Gravitee 4.10) — a new API type purpose-built for proxying upstream MCP servers with governance
- **REST-to-MCP Tool Server** — auto-generates MCP tools from any OpenAPI spec, not just Gravitee's own APIs
- **OpenFGA integration** — fine-grained relationship-based authorization for MCP tools

**Limitations:**
- Requires a Gravitee instance — not a standalone tool
- Bearer token auth (recommended: dedicated service user)
- The MCP server itself is open-source, but Gravitee's MCP Proxy requires enterprise licensing

**Best for:** Gravitee users who want comprehensive natural language control over their API management platform, or teams who want to auto-generate MCP servers from any OpenAPI spec.

### Apache APISIX MCP — Open-Source Gateway Management

**Stars:** 25 | **Language:** TypeScript | **Tools:** 8+ | **Transport:** stdio

Bridges LLMs with the APISIX Admin API for natural language gateway management.

**What makes it stand out:**
- **Full CRUD** — create, read, update, delete routes, services, upstreams, consumers, plugins, SSL certificates, and secrets
- **Apache APISIX integration** — works with the open-source APISIX gateway (15K+ stars)
- **mcp-bridge plugin** — APISIX itself can convert stdio MCP servers to HTTP SSE services at the gateway level

**Limitations:**
- 25 stars suggests early adoption
- Basic tool set compared to Gravitee's 60+ tools
- No analytics or traffic inspection — management only

**Best for:** Apache APISIX users who want natural language gateway configuration.

### Tyk api-to-mcp — API-to-MCP Conversion

**Stars:** Open source | **Language:** TypeScript | **Transport:** stdio

Tyk's approach is different — rather than managing Tyk itself, `api-to-mcp` turns any OpenAPI spec into an MCP server that proxies requests through Tyk's gateway.

**What makes it stand out:**
- **Any OpenAPI → MCP** — load specs from local files or HTTP/HTTPS URLs
- **OpenAPI overlay support** — customize tool names, descriptions, and parameters
- **AI Studio** — Tyk's commercial platform adds scoped tool access policies and guardrails
- **Protocol breadth** — Tyk gateway supports REST, GraphQL, gRPC, TCP, and SOAP

**Limitations:**
- The open-source `api-to-mcp` tool is relatively basic
- AI Studio features require commercial Tyk license
- No standalone Tyk management MCP server — you manage Tyk through its existing APIs

**Best for:** Tyk users who want to expose existing APIs as MCP tools, or teams who need API-to-MCP conversion from OpenAPI specs.

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

**Status:** Early Access (v3.20, GA planned late April 2026) | **Transport:** Remote MCP

Traefik Hub's MCP Gateway is the most feature-rich governance layer for MCP traffic. It's not an MCP server manager — it's an MCP-aware reverse proxy with identity, policy, and observability built in.

**What makes it stand out:**
- **Task-Based Access Control (TBAC)** — a new authorization paradigm: define tasks (business objectives), tools (system access), and transactions (parameter-level constraints) independently, then compose them. More granular than RBAC or ABAC for MCP use cases
- **OAuth 2.0/2.1 Resource Server** — standards-compliant MCP server protection with automatic resource metadata discovery
- **List filtering** — control which tools, prompts, and resources appear in list responses per-client
- **OpenTelemetry native** — operation duration histograms and method-level tracking tagged by tool names and resource URIs
- **Triple Gate architecture** (March 2026) — composable safety pipeline with parallel guard execution, multi-provider failover, token-level cost controls, and IBM Granite Guardian integration
- **Agent-aware error handling** — structured, schema-compliant refusal responses that agents can process gracefully

**Limitations:**
- Early Access — not production-ready yet (GA late April 2026)
- Commercial product — requires Traefik Hub license
- Kubernetes-focused — may be overkill for simple setups
- Not an MCP server itself — it governs other MCP servers

**Best for:** Platform engineering teams who need enterprise-grade governance, identity, and observability for MCP traffic in Kubernetes environments.

### IBM ContextForge — The Open-Source Federation Winner

**Stars:** 3,500 | **Language:** Python | **License:** Apache 2.0 | **Transport:** stdio, SSE, Streamable HTTP

ContextForge federates MCP servers, A2A agents, and REST/gRPC APIs into a single unified endpoint. It's the most popular open-source MCP gateway by stars.

**What makes it stand out:**
- **Protocol federation** — unifies MCP, REST, gRPC, and A2A behind one endpoint. REST/gRPC services are auto-translated into MCP-compliant tools
- **A2A agent integration** — register external AI agents and expose them as MCP tools
- **Admin UI** — web interface for real-time management and log monitoring
- **OpenTelemetry** — traces to Phoenix, Jaeger, or Zipkin
- **Enterprise features** — auth, rate limiting, retries, Redis-backed caching
- **Kubernetes** — Helm charts for production deployment
- **Secure by default** (v0.3.1+) — Admin UI and API disabled by default, must be explicitly enabled

**Limitations:**
- Python-based — may have higher latency than Rust/Go alternatives
- 1.0.0 Beta — still pre-release
- Plugin ecosystem is nascent compared to Traefik or Kong
- No TBAC or fine-grained tool-level authorization (uses basic auth)

**Best for:** Teams who need to unify MCP servers, REST APIs, and A2A agents behind a single open-source gateway with real observability.

### Bifrost — The Performance Winner

**Stars:** 3,100 | **Language:** Go | **License:** Apache 2.0 | **Transport:** Multiple

Bifrost is both an LLM gateway and an MCP gateway in one binary. Built in Go for raw performance.

**What makes it stand out:**
- **11µs overhead** — sub-millisecond latency at 5,000 RPS, 50x faster than LiteLLM
- **Dual gateway** — LLM routing (15+ providers) and MCP gateway (tool orchestration) in one
- **Code Mode + Agent Mode** — supports Cloudflare-style Code Mode and direct agent execution
- **Tool filtering and hosting** — expose only the tools you need, host tools directly
- **Zero-config startup** — NPX, Docker, or Kubernetes with Helm charts
- **Cluster mode** — horizontal scaling for production workloads

**Limitations:**
- MCP gateway is secondary to LLM routing — MCP features are less mature
- 3.1K stars are primarily for LLM gateway, not MCP specifically
- No A2A support (unlike ContextForge)
- No RBAC or policy engine — security is basic compared to Traefik or Lasso

**Best for:** Teams who want a single high-performance gateway for both LLM routing and MCP tool orchestration, and care about latency.

### Agent Gateway (Solo.io/kgateway) — The Kubernetes-Native Option

**Stars:** 2,100 | **Language:** Rust (57%), Go (29%) | **License:** Apache 2.0 | **Transport:** Multiple

Built from the CNCF kgateway project, Agent Gateway is a Rust-based proxy for agent-to-agent and agent-to-tool communication.

**What makes it stand out:**
- **CNCF Sandbox** — backed by the Cloud Native Computing Foundation
- **MCP + A2A** — supports both Model Context Protocol and Agent-to-Agent protocol
- **RBAC** — robust MCP/A2A focused role-based access control
- **Multi-tenancy** — multiple tenants with isolated resource sets
- **Legacy API support** — transforms OpenAPI specs into MCP resources
- **xDS dynamic config** — configuration updates without downtime (like Envoy)
- **Kubernetes controller** — built-in controller for dynamic provisioning via Gateway API

**Limitations:**
- Kubernetes-focused — overkill for non-K8s environments
- Relatively new (expanded from kgateway's MCP proxy in 2026)
- Enterprise version (Solo.io) required for advanced features
- No LLM routing — MCP/A2A only

**Best for:** Kubernetes-native teams who want a CNCF-backed, production-grade proxy for MCP and A2A traffic with multi-tenancy.

### Lasso Security MCP Gateway — The Security-First Gateway

**Stars:** 360 | **Language:** Python | **License:** Open source | **Transport:** stdio, SSE

The first MCP gateway designed specifically for security, with reputation scanning, PII detection, and prompt injection defense.

**What makes it stand out:**
- **Security Scanner** — analyzes MCP server reputation and security risks before loading them. Includes tool description scanning with pattern matching for suspicious capabilities
- **Request/response sanitization** — intercepts and sanitizes sensitive information in both directions
- **Plugin system** — Presidio (PII detection), Lasso (prompt injection, harmful content filtering), Xetrack (experiment tracking to SQLite/DuckDB)
- **Automatic blocking** — risky MCPs blocked based on reputation scores
- **Unified discovery** — automatically discovers and exposes all capabilities from proxied MCP servers

**Limitations:**
- 360 stars — smaller community than ContextForge or Bifrost
- Python-based — higher latency for high-throughput scenarios
- No RBAC or multi-tenancy — security-focused but not governance-focused
- Plugin ecosystem is limited (4 plugins currently)

**Best for:** Security-conscious teams who want to scan, sanitize, and monitor MCP servers before exposing them to agents.

### Peta — The Credential Vault

**Stars:** 39 | **Language:** TypeScript | **License:** Elastic License 2.0 | **Transport:** OAuth 2.0, MCP proxy

Peta is "1Password for AI agents" — a zero-trust credential management layer for MCP.

**What makes it stand out:**
- **Encrypted vault** — PBKDF2 + AES-GCM encryption at rest, secrets injected server-side at execution time — agents never see raw API keys
- **Short-lived tokens** — agents authenticate with Peta tokens, not direct API credentials
- **Policy engine** — role-based and attribute-based access control with human-in-the-loop approval workflows
- **Audit trail** — complete logging of tool calls with caller identity and policy decisions (excluding secrets)
- **REST API adapter** — converts HTTP endpoints into MCP servers without custom development

**Limitations:**
- 39 stars — very early stage
- Elastic License 2.0 — prohibits offering as a managed service to third parties
- Three-component architecture (Core, Console, Desk) adds deployment complexity
- No security scanning (unlike Lasso) — focused purely on credential and access management

**Best for:** Teams who need centralized, auditable credential management for AI agents accessing multiple MCP servers.

## Decision Flowchart

**Managing a specific gateway?** → Use that vendor's MCP server: [Cloudflare](https://github.com/cloudflare/mcp) (Code Mode, 2,500+ endpoints), [Kong Konnect](https://konghq.com/products/kong-konnect/agents) (hosted, 12 tools), [Gravitee](https://github.com/gravitee-io/gravitee-apim-mcp-server) (60+ tools), [APISIX](https://github.com/api7/apisix-mcp) (open source), or [Tyk](https://github.com/TykTechnologies/api-to-mcp) (API-to-MCP).

**Turning REST APIs into MCP tools?** → [Google Apigee](https://cloud.google.com/blog/products/ai-machine-learning/mcp-support-for-apigee) (zero-code, zero-deploy), [Azure APIM](https://learn.microsoft.com/en-us/azure/api-management/mcp-server-overview) (30+ policies), or [AWS API Gateway](https://aws.amazon.com/about-aws/whats-new/2025/12/api-gateway-mcp-proxy-support/) (MCP proxy). Pick your cloud.

**Need MCP governance and RBAC?** → [Traefik Hub](https://traefik.io/solutions/mcp-gateway) (TBAC, OTel, safety pipelines — commercial) or [Agent Gateway](https://github.com/agentgateway/agentgateway) (CNCF, Rust, multi-tenant — open source).

**Need to federate MCP + REST + A2A?** → [IBM ContextForge](https://github.com/IBM/mcp-context-forge) (3.5K stars, Apache 2.0, protocol translation).

**Need raw performance?** → [Bifrost](https://github.com/maximhq/bifrost) (11µs overhead, Go, dual LLM+MCP gateway).

**Need security scanning?** → [Lasso Security](https://github.com/lasso-security/mcp-gateway) (reputation scoring, PII detection, prompt injection).

**Need credential management?** → [Peta](https://github.com/dunialabs/peta-core) (zero-trust vault, short-lived tokens, audit trail).

## Three Trends

**1. Every API gateway vendor is becoming an MCP gateway.** Kong, Cloudflare, Traefik, Gravitee, APISIX, Tyk, AWS, Azure, and Google all shipped MCP capabilities in 2025-2026. The convergence is clear: API management and MCP governance are merging. The question isn't whether your gateway will support MCP, but how deeply — and the quality ranges from Cloudflare's elegant Code Mode to basic REST-to-MCP translation.

**2. A new layer is emerging between agents and tools.** MCP-native gateways (Traefik Hub, ContextForge, Bifrost, Agent Gateway, Lasso, Peta) didn't exist 12 months ago. They represent a new infrastructure category — not traditional API gateways, but agent-aware proxies that understand MCP semantics, tool invocations, and credential flows. Traefik's TBAC and Lasso's reputation scanning show this layer developing its own unique capabilities beyond what API gateways traditionally offer.

**3. The cloud providers are competing on frictionlessness.** Google Apigee (zero code, zero deploy, zero changes), AWS API Gateway (MCP proxy at the infrastructure level), and Azure APIM (REST-to-MCP with 30+ policies) are all racing to make it trivially easy to expose existing APIs to AI agents. The winner will be whoever makes the gap between "I have a REST API" and "agents can use it" closest to zero. Apigee currently leads on simplicity; AWS leads on native integration; Azure leads on policy breadth.

## What's Missing

- **No NGINX MCP server** — NGINX, the world's most deployed reverse proxy, has no official or significant community MCP server for gateway management
- **No Envoy MCP server** — Envoy, the backbone of service mesh, has no dedicated MCP management server
- **No HAProxy MCP server** — another widely deployed proxy with zero MCP presence
- **No unified multi-gateway management** — no server lets you manage Kong + Cloudflare + AWS from one interface
- **No API testing through gateways** — MCP servers manage gateways but don't help you test the APIs behind them
- **No traffic replay or shadow testing** — can't replay production traffic or run shadow tests through MCP
- **No cost analysis** — none of the gateway MCP servers provide API cost estimation, chargeback, or FinOps capabilities
- **No API versioning management** — can't manage API version lifecycles, deprecation schedules, or consumer migration through MCP
- **Code Mode adoption is limited** — Cloudflare pioneered it, but no other vendor has adopted the pattern despite its 99.9% token reduction

---

*Last updated: March 2026. Star counts and tool counts are from our research and may have changed. See our [master MCP server guide](/guides/best-mcp-servers/) for all categories.*

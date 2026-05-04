---
title: "IBM ContextForge MCP Gateway — Federation, RBAC, and AI Traffic Control for Enterprise MCP"
date: 2026-05-05T20:00:00+09:00
description: "IBM ContextForge reviewed: an open source MCP gateway, registry, and proxy federating any MCP, A2A, or REST/gRPC API into a unified endpoint with RBAC, TOON compression, 40+ plugins, and Kubernetes HA. Apache-2.0. Rating: 4.0/5."
og_description: "IBM ContextForge (3,655 stars, v1.0.0 GA): MCP gateway and proxy for enterprise AI agents. Federates MCP, A2A, REST, and gRPC. Virtual servers, multi-tenant RBAC, TOON token compression (30-70%), OpenTelemetry, 40+ plugins, Kubernetes HA. Apache-2.0. Rating: 4.0/5."
content_type: "Review"
card_description: "IBM ContextForge (3,655 stars, v1.0.0 GA, Apache-2.0, Python) is the highest-starred IBM open source project in the MCP ecosystem — and one of the most architecturally complete MCP gateways available. It sits in front of any MCP, A2A, or REST/gRPC API and federates them into a single unified endpoint with centralized governance, discovery, and observability. **Virtual servers** let you compose tool subsets for different teams or agents from a shared catalog. **Multi-tenant RBAC** (since v0.7.0) provides teams, email auth, and per-virtual-server API keys. **TOON compression** reduces LLM token usage by 30-70% — the only MCP gateway with this capability. **40+ plugins** cover PII detection, content filtering, rate limiting, protocol translation, and custom transports. **A2A protocol support** routes agent-to-agent communication alongside MCP tool calls. **Kubernetes-native HA** with Redis-backed federation, auto-scaling, and Helm charts for production deployments. Supports IBM Z (s390x) and POWER (ppc64le) alongside standard x86_64. OpenTelemetry tracing to Phoenix, Jaeger, Zipkin, and any OTLP backend. Not a connector to IBM products — this is protocol-agnostic MCP infrastructure for any organization. Distinct from covered MCP gateway tools like AgentGateway (2,457 stars) and Kong Agent Gateway. Rating: 4.0/5."
last_refreshed: 2026-05-05
---

Most MCP deployments start the same way: one AI client, one MCP server, one connection. Then the catalog grows. Three servers, then ten, then thirty. Each with its own auth model, transport config, and tool namespace. Each connection managed individually by every client. Each team maintaining its own copy of the configuration. This is the scaling problem IBM ContextForge was built to solve.

[ContextForge](https://github.com/IBM/mcp-context-forge) is an open source AI gateway, registry, and proxy that sits in front of any MCP, A2A, or REST/gRPC API and exposes a single unified endpoint to AI clients. It adds centralized governance, tool discovery, access control, rate limiting, observability, and multi-tenancy. As of v1.0.0 GA (May 2026), it is the highest-starred IBM open source project in the MCP ecosystem at **3,655 GitHub stars** — and one of the most architecturally complete MCP gateways available.

This is not an IBM product connector. It does not require IBM Cloud, watsonx, or any IBM software. ContextForge is protocol-agnostic infrastructure for any MCP deployment. Part of our **[Developer Tools MCP category](/categories/developer-tools/)**.

---

## At a Glance

| | |
|---|---|
| **Repo** | [IBM/mcp-context-forge](https://github.com/IBM/mcp-context-forge) |
| **Stars** | ~3,655 |
| **License** | Apache-2.0 |
| **Language** | Python (with Rust-powered JSON components) |
| **Install** | `pip install mcp-contextforge-gateway` |
| **Docs** | [ibm.github.io/mcp-context-forge](https://ibm.github.io/mcp-context-forge/) |
| **Latest version** | v1.0.0 GA (May 2026) |
| **First stable** | v0.5.0 (August 2025) |
| **Multi-arch** | x86_64, IBM Z (s390x), IBM POWER (ppc64le) |

---

## What ContextForge Does

ContextForge operates as three gateways in one:

**Tools Gateway** — Aggregates multiple MCP servers behind a single endpoint. AI clients configure one connection; ContextForge manages upstream MCP connections, handles tool routing, and applies policies. REST and gRPC APIs are translated to MCP tools automatically, so existing services become callable by any MCP-compatible agent without code changes. TOON compression reduces LLM token usage by 30-70% by compressing tool schemas and descriptions before sending them to the model context.

**Agent Gateway** — Routes agent-to-agent (A2A protocol) communication alongside MCP tool calls. Supports OpenAI-compatible and Anthropic agent routing, making ContextForge a neutral protocol bridge across agent frameworks.

**API Gateway** — Provides rate limiting, authentication, retries, and reverse proxy for REST services, turning ContextForge into the policy enforcement layer for all AI agent-to-service traffic in an organization.

These three modes can run simultaneously or independently, depending on deployment requirements.

---

## Key Features

### Virtual Servers

Virtual servers are the core organizational primitive in ContextForge. Each virtual server exposes a curated subset of tools from the upstream catalog with its own access policies and API keys. A typical enterprise deployment might have:

- A **Developer virtual server** — all tools, for authenticated internal users
- A **Customer service virtual server** — only CRM and order management tools
- A **Read-only audit virtual server** — all tools, but write operations blocked by policy

Clients connect to the virtual server endpoint, not to individual MCP servers. Tool namespacing handles collisions when multiple upstream servers expose similarly named tools.

### Multi-Tenant RBAC

Full multi-tenancy has been available since v0.7.0. The system supports teams, email authentication, role-based access control (RBAC) for Admin UI and API routes, per-virtual-server API keys, and resource visibility controls. Different groups in an organization get isolated tool catalogs with their own policy boundaries, while the gateway provides shared observability.

### TOON Compression

TOON (Tool Object Optimization for Networks) compression reduces the token footprint of tool schemas sent to the LLM context window. The 30-70% reduction directly translates to lower API costs and fewer context window pressure issues in agents loading large tool catalogs. No other major MCP gateway has an equivalent feature.

### 40+ Plugins

The plugin ecosystem covers:

- **Security** — PII detection, content filtering, prompt injection detection
- **Rate limiting** — per-client, per-tool, per-virtual-server quotas
- **Protocol translation** — REST-to-MCP, gRPC-to-MCP, custom transports
- **Caching** — L1 (in-memory) and L2 (Redis) for tool call deduplication and response caching
- **Pre/post hooks** — custom logic at every stage of the tool call pipeline
- **Authentication** — JWT, OAuth, API key, and custom auth adapters

Plugins apply as pre- and post-hooks on every request, turning the gateway into a policy engine that operates across all MCP traffic centrally rather than per-server.

### Observability

OpenTelemetry tracing is built in with support for Phoenix (for LLM-native traces), Jaeger, Zipkin, and any OTLP-compatible backend. Every tool call generates a trace span with latency, status, and policy decision data. For organizations already running distributed tracing infrastructure, ContextForge plugs directly into the existing observability stack.

### Compression

Network response compression is automatic: Brotli (best compression), Zstd (fastest), and GZip (universal fallback), negotiated per client via `Accept-Encoding`. Text-based responses (JSON, tool output) compress 30-70% in transit, separate from TOON's LLM-side compression.

---

## Deployment

ContextForge ships four packaging options:

| Method | Use case |
|--------|----------|
| `pip install mcp-contextforge-gateway` | Development, quick start |
| Docker / container images | Staging, single-instance production |
| Binaries | Air-gapped environments |
| Helm charts | Kubernetes HA production |

**Database backends:** SQLite for development and single-instance deployments; PostgreSQL (with PgBouncer connection pooling) for production.

**Kubernetes HA:** Production deployments run multiple ContextForge instances with Redis-backed state sharing, federation, load balancing, and automatic failover. The Helm chart includes auto-scaling configuration for handling variable tool call load.

**Air-gapped:** Since v1.0.0-BETA-1, ContextForge supports fully air-gapped deployments with no external connectivity required — critical for regulated industries and classified environments.

**Multi-architecture:** Docker images ship for x86_64, IBM Z (s390x), and IBM POWER (ppc64le) — covering both cloud-native deployments and IBM mainframe/POWER environments that have no equivalent support in competing gateways.

---

## Performance

Performance engineering became a priority from v1.0.0-BETA-2 onward:

- **N+1 query elimination** — database query patterns rebuilt for bulk operations
- **PgBouncer connection pooling** — eliminates per-request PostgreSQL connection overhead
- **L1/L2 caching** — in-memory cache for hot tool calls, Redis for shared cache across instances
- **Granian HTTP server** — Rust-powered ASGI server replacing Uvicorn in production
- **orjson serialization** — Rust-powered JSON parsing and serialization delivering 5-6x faster serialization and 1.5-2x faster deserialization versus Python's standard library

The v1.0.0-BETA-2 release note cited "100+ performance optimizations" and 80+ bug fixes. The pattern: early releases (v0.4.0–v0.7.0) built enterprise features; later releases (v1.0.0-BETA series) hardened them for production throughput.

---

## Version History

| Version | Date | Highlights |
|---------|------|-----------|
| v0.5.0 | August 2025 | Enterprise auth, configuration management, observability |
| v0.7.0 | Late 2025 | Multi-tenant RBAC, teams, email auth |
| v1.0.0-BETA-1 | December 16, 2025 | Multi-arch containers, gRPC-to-MCP, air-gapped deployment |
| v1.0.0-BETA-2 | January 24, 2026 | 100+ performance optimizations, PgBouncer, Granian, orjson |
| v1.0.0-RC-3 | Early 2026 | Auth/RBAC hardening, experimental Rust MCP runtime, s390x/ppc64le |
| v1.0.0 GA | May 2026 | Production release — CVE tracking begins |

CVE identifiers are formally assigned starting with v1.0.0 GA, signaling that IBM treats this as enterprise software with a security support commitment.

---

## Context: MCP Gateway Landscape

ContextForge is not alone in the MCP gateway space, but it occupies a distinctive position:

| Gateway | Stars | Key differentiator |
|---------|-------|-------------------|
| **IBM ContextForge** | ~3,655 | TOON compression, A2A+MCP+REST+gRPC, 40+ plugins, IBM Z/POWER |
| **AgentGateway** (Salesforce) | ~2,457 | Covered in [API Gateway roundup](/reviews/api-gateway-mcp-servers/) |
| **Microsoft Kubernetes MCP Gateway** | ~595 | Azure-native, Kubernetes-native |
| **Kong Agent Gateway** | Enterprise | MCP+A2A+LLM unified governance, covered in [API Gateway roundup](/reviews/api-gateway-mcp-servers/) |
| **Higress** (Alibaba) | ~8,300 | Native MCP server hosting in a production API gateway |

ContextForge is the only gateway in this group that supports A2A agent routing alongside MCP federation in a vendor-neutral, self-hosted package. Higress is larger but serves a different pattern (hosting MCP servers inside a traditional API gateway rather than federating them). AgentGateway has fewer features for the multi-tenant enterprise use case.

---

## Limitations

**Python runtime.** Most MCP infrastructure tools use TypeScript or Go for lower overhead. Python carries higher memory footprint and startup cost per instance, partially mitigated by the Granian HTTP server and orjson. The experimental Rust MCP runtime (introduced in RC-3) suggests IBM is aware of this — but it has not shipped in a stable release yet.

**Complexity budget.** ContextForge solves a coordination problem that only appears at scale. For teams running 3-5 MCP servers, the gateway adds operational complexity (another service to deploy, monitor, and maintain) without proportional benefit. The tool is well-suited to organizations with 10+ MCP servers, multiple teams, and governance requirements.

**IBM branding vs. content.** Despite being protocol-agnostic, the IBM association creates perception friction for non-IBM shops. The documentation, docs site, and workshop are all high quality — but the repo name and organization may cause teams to filter it out during evaluation.

**Workshop dependency.** The [ContextForge Workshop](https://contextforge-org.github.io/mcp-workshop/) is comprehensive and well-maintained, but it lives in a separate GitHub organization (contextforge-org), creating a minor discovery fragmentation.

---

## Who Should Use This

**Good fit:**
- Organizations running 10+ MCP servers that need unified access control and discovery
- Teams with compliance requirements for audit logging and policy enforcement on all AI tool calls
- Enterprise environments needing multi-tenant isolation (different teams, different tool subsets)
- Deployments on IBM Z or POWER infrastructure
- Cost-sensitive deployments where TOON token compression meaningfully reduces LLM API bills

**Not the right tool:**
- Small deployments with 2-3 MCP servers and no governance requirements
- Organizations that need a hosted/managed gateway (ContextForge is self-hosted only)
- Teams without Kubernetes expertise (for production HA deployments)

---

## Rating: 4.0/5

ContextForge is the most complete self-hosted MCP gateway in the open source ecosystem. TOON compression, A2A federation, 40+ plugins, and multi-architecture container support solve real enterprise problems with no direct equivalent in competing tools. The documentation is extensive, the workshop is hands-on, and the v1.0.0 GA release (with formal CVE tracking) marks this as production software, not a side project.

The deduction: Python runtime carries inherent overhead that matters at scale (partially mitigated, not solved), and the tool's value proposition only materializes for organizations with significant MCP catalog complexity. For smaller deployments, simpler point solutions cost less operationally.

For enterprises already managing multi-team AI agent deployments with governance requirements, ContextForge is the clearest architectural fit in the MCP gateway category.

---

*Related:*
- *[IBM MCP Servers](/reviews/ibm-mcp-servers/) — IBM product connectors: watsonx.data, IBM i, QRadar, FileNet, and more*
- *[API Gateway MCP Servers](/reviews/api-gateway-mcp-servers/) — Kong, Cloudflare, AgentGateway, and Microsoft's MCP Gateway*
- *[API Gateway & Management MCP Servers](/reviews/api-gateway-api-management-mcp-servers/) — Higress, Postman, OpenAPI-to-MCP tooling*
- *[Agent Orchestration MCP Servers](/reviews/agent-orchestration-mcp-servers/) — A2A, CrewAI, LangChain MCP integrations*

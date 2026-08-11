# MCP Multi-Tenant Architecture: Per-Tenant Isolation, Shared Servers, OAuth Identity Propagation, and SaaS Deployment Patterns

> A comprehensive guide to MCP multi-tenant architecture — covering isolation models (dedicated instance, pooled, hybrid), tenant-aware routing, OAuth 2.1 identity propagation


MCP works great for a single user with a local AI assistant. One process, one set of credentials, one context window. But the moment you need an MCP server to serve multiple tenants — whether that's customers in a B2B SaaS product, teams within an enterprise, or users of a hosted AI platform — every assumption breaks.

Tenant A's API keys must never leak into Tenant B's tool calls. Tenant C's rate limits can't starve Tenant D. A misconfigured query filter shouldn't expose one customer's data to another's AI agent. And spinning up a separate MCP server process per tenant doesn't scale when you have thousands of users.

This is the multi-tenancy problem, and it's one of the biggest gaps in the current MCP specification. The protocol itself doesn't define a tenant model. It has no concept of `tenant_id`, no built-in mechanism for per-tenant credential scoping, and no standard for propagating tenant context across the multi-hop chain from user to AI host to MCP client to MCP server to backend API.

The community and cloud providers have converged on several patterns that work. This guide covers isolation models, identity propagation, data separation, gateway architectures, session management, and production blueprints for multi-tenant MCP deployments. Our analysis draws on published documentation, open-source implementations, AWS reference architectures, and community discussions — we research and analyze rather than deploying these systems ourselves. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

## Why Multi-Tenancy Matters for MCP

The original MCP architecture assumed a local-first model: Claude Desktop spawns an stdio process, that process connects to local tools, everything runs in a single user's context. But MCP has rapidly expanded into server-hosted, multi-user environments:

- **SaaS platforms** exposing their APIs as MCP tools for AI agents
- **Enterprise deployments** where teams share a central MCP gateway
- **AI hosting platforms** connecting thousands of users to shared tool infrastructure
- **Internal developer tools** serving multiple project teams from a single MCP endpoint

A [March 2025 GitHub discussion (#193 in the MCP spec repo)](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/193) captured the core tension: "I need to be able to spin up and execute potentially thousands of concurrent instances of the same MCP server, one per user, just to perform a simple API proxy operation with two input variables." The community agreed that requiring per-user processes creates unacceptable scaling overhead and reliability concerns.

A separate [issue (#2173 in the MCP servers repo)](https://github.com/modelcontextprotocol/servers/issues/2173), filed June 20, 2025 by a SaaS platform builder, stated the challenge directly: "we are really struggling to find a way to use same MCP server to serve all of our tenants without running a separate MCP server per tenant."

## The Three Isolation Models

Multi-tenant MCP deployments fall into three patterns, each trading off isolation strength against operational complexity and cost.

### 1. Dedicated Instance Per Tenant

Each tenant gets their own MCP server instance — a separate process, container, or namespace.

**How it works:**
- Each tenant's MCP server runs in its own Kubernetes pod, container, or VM
- Credentials are injected at startup via environment variables or mounted secrets
- Tenant routing happens at the load balancer or ingress level (e.g., `tenant-a.api.example.com/mcp`)
- No shared state between tenants at the application layer

**Strengths:**
- Maximum isolation — a crash or security breach in one tenant cannot affect others
- Simple programming model — each server instance has a single set of credentials and configuration
- Natural fit for compliance requirements (HIPAA, SOC 2, FedRAMP) that mandate physical separation

**Weaknesses:**
- Resource overhead — idle tenants still consume memory, CPU, and connections
- Operational complexity — managing hundreds or thousands of server instances requires orchestration
- Cold start latency — spinning up new instances on demand adds response time

**When to use:** Healthcare, financial services, government, or any domain where regulatory requirements mandate physical tenant isolation. Also appropriate when tenant count is small (under ~50) and per-tenant resource cost is acceptable.

**Real-world example:** [Fly.io's MCP deployment guidance](https://fly.io/docs/blueprints/remote-mcp-servers/) recommends a single-tenant pattern with one app (Fly Machine) per user, using [auto-start/auto-stop](https://fly.io/docs/launch/autostop-autostart/) to keep idle costs low.

### 2. Pooled Multi-Tenant (Shared Server)

A single MCP server instance handles requests from all tenants, using logical isolation to separate their data and permissions.

**How it works:**
- One server process handles all incoming MCP connections
- Each request carries a tenant identifier (from JWT claims, URL path, or headers)
- Server-side middleware extracts the tenant ID and injects it into the request context
- Every tool handler enforces tenant scoping — database queries include `WHERE tenant_id = ?`, API calls use tenant-specific credentials fetched from a vault

**Strengths:**
- Cost-efficient — shared compute and memory across all tenants
- Simpler operations — one deployment, one codebase, one set of infrastructure
- Instant availability — no cold starts for new tenants

**Weaknesses:**
- Higher engineering complexity — every tool handler must correctly enforce tenant boundaries
- Shared blast radius — a bug in tenant scoping can expose data across tenants
- Noisy neighbor risk — one tenant's heavy usage can impact others without rate limiting

**When to use:** B2C or high-volume B2B platforms where cost efficiency matters more than physical isolation. Suitable when your engineering team can maintain rigorous per-request authorization and you have thorough testing for cross-tenant isolation.

**Real-world example:** [SageMCP](https://github.com/sagemcp/SageMCP) implements this model with per-tenant URL paths (`/api/v1/{tenant-slug}/mcp`) and Fernet-encrypted credential storage per tenant; Redis-backed session persistence is listed on its roadmap as a planned, not yet shipped, capability.

### 3. Hybrid: Tenant-Aware Shared Infrastructure

Shared infrastructure with logical isolation at the namespace level — combining the operational simplicity of pooled servers with stronger boundaries than pure application-level separation.

**How it works:**
- Shared Kubernetes cluster but separate namespaces per tenant (or tenant group)
- Network policies block cross-namespace traffic
- Shared MCP server code with tenant context propagated through all layers
- Database-level isolation via schemas, row-level security, or separate databases per tier
- Upgrade to dedicated instances for premium or high-compliance tenants

**Strengths:**
- Balances isolation and cost — stronger boundaries than pure application-level pooling
- Flexible tiering — free tenants share resources, enterprise tenants get dedicated infrastructure
- Easier compliance — namespace isolation satisfies many audit requirements without full physical separation

**Weaknesses:**
- Requires Kubernetes or similar orchestration (not suitable for simple deployments)
- More complex than either pure dedicated or pure pooled approaches
- Network policy configuration can be error-prone

**When to use:** B2B SaaS platforms with a tiered pricing model, where some customers need stronger isolation guarantees than others. Also suitable for enterprises with multiple internal teams that need both shared tooling and clear data boundaries.

**Real-world example:** [AWS's multi-tenant MCP sample](https://github.com/aws-samples/sample-multi-tenant-saas-mcp-server) — a B2B travel-booking reference architecture — uses Amazon Cognito for identity, DynamoDB for tenant-scoped data, and ECS for container orchestration, with JWT claims carrying `tenantId` for routing and authorization.

## Identity Propagation: The Multi-Hop Challenge

The hardest problem in multi-tenant MCP isn't data isolation — it's identity propagation. When a user asks an AI agent to perform a task, their identity and permissions must flow through several boundaries:

```
User → AI Host → MCP Client → MCP Server → Backend API/Database
```

Each hop must:
1. **Preserve authorization context** — the server needs to know which tenant and which user
2. **Prevent credential leakage** — tokens should be scoped to each hop, not forwarded wholesale
3. **Be independently auditable** — each boundary should log who did what and why

### OAuth 2.1 in MCP: The Current State

MCP adopted [OAuth 2.1 with PKCE as its authorization framework in the March 26, 2025 spec revision](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization). The [July 28, 2026 spec revision](https://blog.modelcontextprotocol.io/posts/2026-07-28/) hardened this significantly for enterprise/multi-tenant use — several of the items below were open gaps as recently as mid-2026 and are worth re-checking if you built against an earlier revision:

- **Authorization Code Flow with PKCE** for interactive client applications, still the baseline
- **[Client ID Metadata Documents (CIMD)](https://modelcontextprotocol.io/specification/draft/basic/authorization/client-registration)** — added via SEP-991, now the *recommended* client-registration mechanism: the client's `client_id` is an HTTPS URL hosting its own metadata, so no registration call is needed
- **Dynamic Client Registration** ([RFC 7591](https://datatracker.ietf.org/doc/html/rfc7591)) — as of the July 2026 revision this is **formally deprecated** in favor of CIMD; it's retained only as a fallback for authorization servers that don't support CIMD, and is expected to be removed in a future spec version
- **[RFC 9207](https://datatracker.ietf.org/doc/html/rfc9207) issuer validation** — added in the July 2026 revision; clients must record the expected issuer and validate the `iss` value on the authorization response before redeeming a code, closing an authorization-server "mix-up" hole relevant to any deployment juggling multiple tenant-specific authorization servers
- **[Protected Resource Metadata](https://datatracker.ietf.org/doc/html/rfc9728)** (RFC 9728) for discovering authorization requirements — MCP servers **MUST** implement this

However, the spec is still notably silent on several multi-tenant-specific concerns:

- **Token forwarding vs. exchange:** When a request passes through a gateway, should the gateway forward the original token, rewrite claims, or perform a token exchange?
- **Tenant claim standards:** There's no specified claim name for tenant identity (`tenant_id`, `org_id`, `custom:tenantId` are all in use)
- **Scope namespacing:** No convention for per-tenant scope definitions

### Identity Propagation Patterns

**Pattern 1: JWT Claims with Tenant Context**

The most common approach embeds tenant identity in JWT claims, either through custom claims in the identity provider or via a pre-token generation trigger:

```
# AWS Cognito Pre-Token Generation Lambda (conceptual)
# Adds tenantId to ID token claims
{
  "claimsOverrideDetails": {
    "claimsToAddOrOverride": {
      "custom:tenantId": "tenant-abc-123",
      "custom:role": "analyst"
    }
  }
}
```

The MCP server extracts these claims from the validated JWT on every request and uses them to scope all downstream operations.

**Pattern 2: Token Exchange at Each Boundary**

Rather than forwarding the user's original token, each boundary performs an [OAuth 2.0 token exchange (RFC 8693)](https://datatracker.ietf.org/doc/html/rfc8693). The MCP server receives the user's token, validates it, then obtains a new scoped token for downstream API access. Note this is a general OAuth 2.0 mechanism applied to MCP by implementers — RFC 8693 itself is not part of the MCP authorization spec's normative reference list.

```
# Conceptual token exchange flow
# MCP server exchanges user token for a backend-scoped token
POST /oauth/token
grant_type=urn:ietf:params:oauth:grant-type:token-exchange
subject_token={user_jwt}
subject_token_type=urn:ietf:params:oauth:token-type:jwt
resource=https://backend-api.example.com
scope=read:tenant-data
```

This prevents the backend from ever seeing the user's original credentials and enables fine-grained scope reduction at each hop.

**Pattern 3: Mutual TLS with Tenant Certificates**

For server-to-server MCP connections (e.g., between a gateway and backend MCP servers), mTLS provides cryptographic identity:

- Each tenant or tenant group gets its own TLS client certificate
- The MCP server validates the certificate against a tenant-specific CA
- Certificate pinning prevents cross-tenant token misuse even if tokens are stolen
- Certificate rotation is managed through automated PKI infrastructure

### The Two-Layer Identity Model

A pattern emerging from enterprise deployments — documented by identity vendors [Aembit](https://docs.aembit.io/ai-guide/mcp/identity-gateway/) and [GitGuardian](https://blog.gitguardian.com/mcp-governance-framework/) — uses two layers of identity:

1. **Infrastructure identity:** The MCP client requests a native identity token from its infrastructure (e.g., AWS IAM role, Kubernetes service account, Azure managed identity)
2. **Application identity:** The authorization server validates the infrastructure identity, evaluates access policy, and issues a scoped application token

This separation means the MCP server never handles long-lived secrets — it gets ephemeral, scoped tokens tied to both the infrastructure context and the tenant context.

## Tenant-Aware Data Separation

Once you know which tenant is making a request, you need to ensure every data access path respects that boundary.

### Database-Level Patterns

| Strategy | Isolation Level | Cost | Complexity | Use When |
|----------|----------------|------|------------|----------|
| **Separate databases** | Highest | High | Low | Regulatory requirements mandate physical separation |
| **Separate schemas** | High | Medium | Medium | Need strong logical isolation without separate infrastructure |
| **Row-level security** | Moderate | Low | High | Cost-sensitive with rigorous engineering discipline |
| **Application-level filters** | Lowest | Lowest | Medium | Simple deployments with thorough testing |

**Row-level security (RLS)** is the most common pattern for pooled multi-tenant MCP servers. The server sets a session variable (`SET app.tenant_id = 'abc123'`) and PostgreSQL policies automatically filter every query:

```sql
-- PostgreSQL RLS policy (conceptual)
CREATE POLICY tenant_isolation ON documents
  USING (tenant_id = current_setting('app.tenant_id'));

ALTER TABLE documents ENABLE ROW LEVEL SECURITY;
```

Every query against the `documents` table automatically includes the tenant filter — tool handlers don't need to remember to add `WHERE tenant_id = ?`.

### Vector Database Isolation

For RAG-enabled MCP servers, vector database isolation is critical — without it, Tenant A's embeddings could appear in Tenant B's search results:

- **Namespace-per-tenant:** [Pinecone](https://docs.pinecone.io/guides/get-started/implement-multitenancy) and [Weaviate](https://docs.weaviate.io/weaviate/manage-collections/multi-tenancy) both support native per-tenant partitioning — Pinecone via one namespace per tenant, Weaviate by giving each tenant its own dedicated shard within a collection.
- **Collection-per-tenant — use with caution:** [Qdrant](https://qdrant.tech/documentation/manage-data/multitenancy/) supports collection-per-tenant, but its own docs recommend it only under ~500 tenants and warn it "does not scale past a few hundred" collections; beyond that, Qdrant recommends a single collection with payload-based tenant partitioning (with tiered multitenancy in v1.16+ for large tenants). [ChromaDB's own guidance](https://cookbook.chromadb.dev/strategies/multi-tenancy/) similarly recommends a `tenant_id` metadata field filtered at query time over per-tenant collections, since per-tenant collections fragment the index and complicate cross-tenant analytics.
- **Metadata filtering:** Add `tenant_id` as a metadata field and include it as a mandatory filter in every search query. Less safe than namespaces (relies on filter correctness) but works with any vector database — and, per the vendor guidance above, is the recommended default for Qdrant and ChromaDB at scale rather than a fallback.
- **Separate instances:** For maximum isolation, run separate vector database instances per tenant. Most expensive but simplest to reason about.

### Encryption and Key Management

For sensitive multi-tenant data:

- **Disk/volume-level encryption** with cloud KMS keys is the baseline
- **Per-tenant encryption keys** provide cryptographic isolation — even if a database query bypasses RLS, the data is encrypted with a key the other tenant's context can't access
- **Application-level encryption** for PII, PHI, or financial fields — encrypted with tenant-specific keys before storage using envelope encryption (data key encrypted by tenant master key)

## Gateway Architectures for Multi-Tenant MCP

An MCP gateway sits between clients and backend MCP servers, handling cross-cutting concerns like authentication, routing, rate limiting, and tenant isolation.

### Gateway Responsibilities

| Concern | What the Gateway Does |
|---------|----------------------|
| **Authentication** | Terminate TLS, validate JWT tokens, enforce mTLS |
| **Tenant routing** | Extract tenant ID from claims/path, route to correct backend |
| **Authorization** | Enforce per-tenant tool access policies |
| **Rate limiting** | Per-tenant and per-user request quotas |
| **Credential injection** | Fetch tenant-specific API keys from vault, inject into backend requests |
| **Observability** | Add tenant context to all logs, metrics, and traces |
| **Service discovery** | Maintain registry of available MCP servers and their capabilities |
| **Tool catalog** | Present tenant-specific tool lists (some tenants may have different tool access) |

### AWS Bedrock AgentCore Gateway

[Amazon Bedrock AgentCore Gateway](https://aws.amazon.com/blogs/machine-learning/introducing-amazon-bedrock-agentcore-gateway-transforming-enterprise-ai-agent-tool-development/) is a fully managed service that acts as a centralized MCP tool server. It groups multiple backend MCP servers behind a single endpoint and handles:

- **JWT authorization** via identity providers such as Amazon Cognito, Okta, or Auth0, with tenant ID extraction from token claims
- **OpenAPI-to-MCP conversion** — supply an OpenAPI or Smithy spec, and the gateway generates MCP-compatible tool endpoints automatically
- **Identity propagation** — authorization headers propagated to backend MCP servers, with Lambda request interceptors extracting tenant IDs from JWT tokens

The AWS multi-tenant sample ([`aws-samples/sample-multi-tenant-saas-mcp-server`](https://github.com/aws-samples/sample-multi-tenant-saas-mcp-server)) demonstrates a B2B travel booking platform with Cognito authentication, DynamoDB for tenant-scoped data, and ECS container orchestration. A separate sample ([`aws-samples/sample-agentcore-multi-tenant`](https://github.com/aws-samples/sample-agentcore-multi-tenant)) shows the AgentCore-specific multi-tenant pattern, with a Pre-Token Generation Lambda adding `custom:tenantId` claims to Cognito ID tokens.

### Open-Source Gateway Options

Several open-source projects have emerged to address MCP multi-tenancy:

| Project | Stars | Language | Key Feature |
|---------|-------|----------|-------------|
| [**MCP Plexus**](https://github.com/super-i-tech/mcp_plexus) | ~30 | Python | OAuth 2.1 flow management, URL-path tenant routing (`/{entity_id}/...`), Redis session state, built on FastMCP 2.7 |
| [**SageMCP**](https://github.com/sagemcp/SageMCP) | — | Python | 23+ service integrations, web UI for tenant management, Fernet-encrypted credentials, three API key scope tiers, per-tenant rate limiting |
| [**McpToolKit**](https://github.com/timothywangdev/McpToolKit) (FastMCP Multi-Tenancy) | — | Python | Drop-in FastMCP replacement with Redis-backed sessions, stateless horizontally-scalable instances, load-balanced deployment |
| [**Airflow MCP**](https://bajoriavinayak.medium.com/building-a-multi-tenant-mcp-server-for-apache-airflow-one-server-multiple-instances-9960d662ca2b) | — | Python | Multi-tenant FastMCP server for Apache Airflow, one server serving multiple Airflow instances |

### Build vs. Buy Decision

| Factor | Build Custom Gateway | Use Managed (AgentCore) | Use Open-Source Framework |
|--------|---------------------|------------------------|--------------------------|
| **Time to production** | Months | Days | Weeks |
| **Cloud lock-in** | None | AWS | None |
| **Customization** | Full | Limited to configuration | Framework-constrained |
| **Operational burden** | High | Low | Medium |
| **Cost at scale** | Predictable | Pay-per-use | Infrastructure only |
| **Compliance control** | Full | Shared responsibility | Full |

## Session Management for Multi-Tenant MCP

**Note on spec currency:** the pattern below describes the stateful `Mcp-Session-Id` session model from the pre-2026-07-28 spec revisions, which is still what most deployed MCP servers run today. As covered in the next section, [SEP-2575 ("Make MCP Stateless")](https://modelcontextprotocol.io/seps/2575-stateless-mcp) reached **Final** status and removed the mandatory initialization handshake and session concept from the spec as of the July 28, 2026 revision — new deployments should evaluate that model first.

Stateful MCP sessions (via Streamable HTTP's `Mcp-Session-Id` header) add complexity in multi-tenant environments. Sessions must be:

1. **Tenant-scoped** — a session ID valid for Tenant A must not work for Tenant B
2. **Horizontally distributable** — any server instance must be able to handle any session
3. **Recoverable** — if a session drops, re-authentication must re-establish tenant context (the exact idle-timeout window is implementation-specific and varies by server; don't assume a fixed number of minutes)

### Redis-Backed Session Pattern

The most common approach stores session state in Redis with a composite key:

```
# Session key structure (conceptual)
Key:   mcp:session:{session_id}
Value: {
  "tenant_id": "abc123",
  "user_id": "user-456",
  "roles": ["analyst"],
  "created_at": "2026-03-28T12:00:00Z",
  "last_active": "2026-03-28T12:15:00Z",
  "credentials_ref": "vault:abc123/github-token"
}
TTL: 3600 seconds
```

Key design decisions:
- **Never store credentials in the session** — store a vault reference instead
- **Include tenant_id in the session validation** — even if an attacker obtains a session ID, the server validates that the authenticated tenant matches the session's tenant
- **Set aggressive TTLs** — sessions should expire within hours, not days
- **Use Redis Cluster** for high availability across multiple server instances

### Stateless Alternative: SEP-2575 (formerly SEP-1442), now Final

The proposal to make MCP stateless — originally opened as [SEP-1442](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1442) — was carried forward as [SEP-2575, "Make MCP Stateless"](https://modelcontextprotocol.io/seps/2575-stateless-mcp), which reached **Final** status and shipped in the July 28, 2026 spec revision. This is no longer a future proposal; it is current spec text. Key changes:
- The `initialize` / `notifications/initialized` handshake is **removed**; protocol version, client info, and capabilities are now sent with every request via `_meta` fields and the `MCP-Protocol-Version` header
- A new `server/discover` RPC lets a client query supported versions and capabilities without a handshake
- The Streamable HTTP GET endpoint and `Mcp-Session-Id`-based long-lived session are removed; long-lived server-to-client channels are replaced by an opt-in `subscriptions/listen` RPC
- Durability/resumability across a dropped connection is now handled by an explicit tasks primitive rather than resumable SSE streams
- Session-lifecycle mechanics that remain necessary are addressed by separate, still-evolving SEPs (SEP-2567, SEP-2322) rather than being baked into the core handshake

For multi-tenant deployments, this direction is a good fit — each request carries its own tenant context via JWT claims, and there is no in-protocol server-side session state to tenant-scope. Deployments still running pre-2026-07-28 servers will continue to need the Redis-backed session pattern above until they migrate.

## Rate Limiting and Cost Controls

Without per-tenant rate limiting, a single tenant can consume all available resources, starving others. Multi-tenant MCP servers need layered throttling:

### Three-Layer Rate Limiting

| Layer | Purpose | Implementation |
|-------|---------|---------------|
| **Per-user** | Fairness within a tenant | Token bucket per `user_id`, e.g., 100 tool calls/minute |
| **Per-tenant** | Shared resource protection | Token bucket per `tenant_id`, e.g., 1000 tool calls/minute |
| **Global** | Upstream system protection | Circuit breaker across all tenants, e.g., 5000 total calls/minute |

### Cost Allocation

For SaaS platforms that need to bill tenants for MCP usage:
- **Track token consumption per tenant** — count input/output tokens per tool call
- **Log tool invocations with tenant context** — enables per-tenant billing dashboards
- **Set budget caps** — alert or block when a tenant approaches their quota
- **Implement denial-of-wallet protection** — the [142.4x token amplification attack (arXiv:2602.14798)](https://arxiv.org/abs/2602.14798) means a single tool call can generate massive downstream token usage

## Observability with Tenant Context

Debugging multi-tenant MCP issues requires tenant-scoped observability. Without it, a "tool call failed" error gives no indication of which tenant was affected or whether the failure was tenant-specific.

### Structured Logging Requirements

Every log entry should include:
- `tenant_id` — which tenant's request this was
- `user_id` — pseudonymized for privacy compliance
- `session_id` — for request correlation
- `tool_name` — which tool was invoked
- `duration_ms` — latency tracking per tenant
- `result_status` — success, error, or timeout
- `correlation_id` — for distributed tracing across hops

**Critical:** Avoid storing raw PII in logs. Use pseudonymized user IDs and redact sensitive parameters. Tenant-scoped log access ensures operators can only view their own tenant's logs.

### OpenTelemetry Integration

The [MCP semantic conventions for OpenTelemetry (merged January 2026 in v1.39.0)](https://github.com/open-telemetry/semantic-conventions/releases/tag/v1.39.0) provide standardized attribute names for tracing MCP operations. For multi-tenant deployments, extend these with:

- `mcp.tenant.id` — tenant identifier on every span
- `mcp.tenant.tier` — tenant pricing tier (for SLA tracking)
- `mcp.tenant.region` — if tenants are geo-distributed

## Testing Multi-Tenant Isolation

Multi-tenant MCP servers require testing that specifically validates tenant boundaries. A single missed `WHERE` clause or unscoped vector search can expose data across tenants.

### Testing Strategy

| Test Type | What It Validates | Example |
|-----------|------------------|---------|
| **Unit tests** | Every tool handler includes tenant filter | Mock DB calls and assert `tenant_id` parameter is always present |
| **Integration tests** | End-to-end tenant isolation | Provision two test tenants, insert data for each, verify neither can see the other's data |
| **Adversarial tests** | Cross-tenant attack resistance | Attempt to access Tenant B's data using Tenant A's valid credentials |
| **Chaos tests** | Isolation under failure | Kill a tenant's database connection and verify other tenants are unaffected |
| **Load tests** | Noisy neighbor prevention | Flood one tenant with requests and verify other tenants maintain acceptable latency |

### Common Cross-Tenant Bugs

Based on community reports and security research:

1. **Missing tenant filter in a new tool handler** — the most common bug; a developer adds a new tool and forgets the tenant scoping
2. **Shared in-memory cache without tenant keys** — caching a tool result without including `tenant_id` in the cache key
3. **Log aggregation leaking tenant data** — centralized logging dashboards showing all tenants' data to operators
4. **Session ID reuse after tenant switch** — a session created for one tenant being accepted for a different tenant
5. **Vector search without namespace filtering** — RAG queries returning embeddings from other tenants

## Anti-Patterns to Avoid

### 1. Global Configuration at Startup

**Wrong:** Configuring credentials in environment variables at MCP server startup.

This forces a 1:1 relationship between server instances and tenants. Every tool call uses the same credentials, making multi-tenancy impossible without separate processes.

**Right:** Fetch tenant-specific credentials per-request from a vault or credential store, scoped by the authenticated tenant ID.

### 2. Recycled User Credentials for Agents

**Wrong:** Having AI agents authenticate using a human user's long-lived credentials.

This violates the principle of least privilege, makes audit trails meaningless (was it the human or the agent?), and creates a blast radius if the credential is compromised.

**Right:** Issue first-class agent identities with their own credentials, scoped roles, and audit trails. Use short-lived tokens rotated aggressively.

### 3. Trust-the-Client Tenant Isolation

**Wrong:** Accepting the tenant ID from client-supplied headers without server-side validation.

An attacker can simply change the `X-Tenant-Id` header to access another tenant's data.

**Right:** Extract tenant identity from a cryptographically validated source — the JWT claims signed by your identity provider, the mTLS client certificate, or the authenticated session.

### 4. Shared Vector Namespaces

**Wrong:** Storing all tenants' embeddings in a single vector database collection with a `tenant_id` metadata field, relying only on query-time filtering.

A single missed filter or a bug in the vector database's filtering logic exposes all tenants' data.

**Right:** Use separate namespaces or collections per tenant. The data is physically separated in the vector database, so even a filter bug can't cross boundaries.

### 5. Unscoped Error Messages

**Wrong:** Returning detailed error messages that include other tenants' information, such as "Cannot access table owned by tenant-xyz" or stack traces containing tenant-specific paths.

**Right:** Return generic, recovery-oriented error messages. Log the detailed context server-side with proper tenant scoping.

## Production Blueprint: Multi-Tenant MCP Server

A reference architecture combining the patterns above into a production-ready deployment:

```
┌─────────────────────────────────────────────────┐
│                  Clients                         │
│  (Claude Desktop, AI Hosts, Custom Agents)       │
└──────────────────┬──────────────────────────────┘
                   │ HTTPS + JWT
┌──────────────────▼──────────────────────────────┐
│              API Gateway / LB                     │
│  • TLS termination                                │
│  • JWT validation                                 │
│  • Tenant ID extraction from claims               │
│  • Per-tenant rate limiting                        │
│  • Request routing                                 │
└──────────────────┬──────────────────────────────┘
                   │ mTLS + tenant context
┌──────────────────▼──────────────────────────────┐
│           MCP Server Pool (Stateless)             │
│  • Tenant context injected per request            │
│  • Tool handlers enforce tenant scoping           │
│  • Credentials fetched from vault per-tenant      │
│  • Session state in Redis (not in-process)        │
│  • Horizontally scalable                          │
└──────┬───────────┬───────────┬──────────────────┘
       │           │           │
┌──────▼──┐  ┌─────▼───┐  ┌───▼──────┐
│ Vault   │  │ Redis   │  │ Database │
│ (creds) │  │ (sessions│  │ (RLS)   │
│ per-    │  │  per-    │  │ per-    │
│ tenant) │  │  tenant) │  │ tenant) │
└─────────┘  └─────────┘  └─────────┘
```

### Layer-by-Layer Checklist

**Identity Layer:**
- [ ] OAuth 2.1 with PKCE for interactive clients
- [ ] Client Credentials for server-to-server
- [ ] JWT claims include tenant_id and roles
- [ ] Short-lived tokens (< 1 hour)
- [ ] Token exchange at each boundary (not passthrough)

**Gateway Layer:**
- [ ] TLS termination with strong ciphers
- [ ] JWT validation on every request
- [ ] Tenant ID extracted from validated claims (not headers)
- [ ] Per-tenant rate limiting with token bucket
- [ ] Request logging with tenant context

**Server Layer:**
- [ ] Stateless server instances (session state in Redis)
- [ ] Tenant context set before every tool handler executes
- [ ] Credentials fetched per-request from vault
- [ ] Input validation on all tool parameters
- [ ] Output filtering to prevent cross-tenant data leakage

**Data Layer:**
- [ ] Row-level security enabled on all tenant-scoped tables
- [ ] Vector database namespaces per tenant
- [ ] Per-tenant encryption keys for sensitive data
- [ ] Audit log of all data access with tenant context

**Observability Layer:**
- [ ] Structured logs with tenant_id on every entry
- [ ] OpenTelemetry traces with tenant attributes
- [ ] Per-tenant dashboards for latency, errors, and usage
- [ ] Alerts for cross-tenant access attempts

## Multi-Tenant MCP Ecosystem

| Project | Type | Multi-Tenant Approach | Notable Feature |
|---------|------|----------------------|-----------------|
| [**AWS AgentCore Gateway**](https://aws.amazon.com/blogs/machine-learning/introducing-amazon-bedrock-agentcore-gateway-transforming-enterprise-ai-agent-tool-development/) | Managed gateway | JWT claims + Cognito | OpenAPI-to-MCP auto-conversion |
| [**aws-samples/sample-multi-tenant-saas-mcp-server**](https://github.com/aws-samples/sample-multi-tenant-saas-mcp-server) | Reference architecture | Cognito + DynamoDB scoping | Full B2B SaaS travel booking sample |
| [**MCP Plexus**](https://github.com/super-i-tech/mcp_plexus) | Python framework | URL-path routing + Redis sessions | OAuth 2.1 flow management for external services |
| [**SageMCP**](https://github.com/sagemcp/SageMCP) | Platform | Shared server + per-tenant URL-path scoping + encrypted credentials | Web UI, 23+ service integrations, 3-tier API keys |
| [**McpToolKit**](https://github.com/timothywangdev/McpToolKit) | Python framework | Redis-backed stateless sessions | Drop-in FastMCP replacement |
| [**Airflow MCP**](https://bajoriavinayak.medium.com/building-a-multi-tenant-mcp-server-for-apache-airflow-one-server-multiple-instances-9960d662ca2b) | Domain-specific | Per-instance routing | Multi-Airflow-instance access from single server |
| [**Fly.io MCP Blueprint**](https://fly.io/docs/blueprints/remote-mcp-servers/) | Deployment pattern | Machine-per-user | Auto-start/auto-stop for cost control |
| [**Smithery**](https://smithery.ai/docs) | Hosting platform | Stateless hosting | Connection lifecycle (including session state) managed automatically per Smithery's docs; exact instance-recycling mechanics aren't publicly documented in detail |
| [**Prefactor**](https://prefactor.tech/blog/mcp-security-multi-tenant-ai-agents-explained) | Control plane | Policy-as-code + audit trails | SOC 2-aligned controls, emergency kill switches |

## What's Coming

The MCP specification continues to evolve toward better multi-tenancy support. Two items that were "coming" as of this guide's original publication have already shipped as of the July 28, 2026 spec revision — see the Session Management and OAuth 2.1 sections above for the current state of stateless MCP ([SEP-2575](https://modelcontextprotocol.io/seps/2575-stateless-mcp), Final) and Client ID Metadata Documents / RFC 9207 issuer validation. Still on the horizon:

- **OAuth 2.1 improvements:** The MCP authorization spec continues to be refined for enterprise patterns; token-exchange and tenant-scope-namespacing conventions are still not standardized as of this writing.
- **[`.well-known/mcp.json` server cards (SEP-2127)](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2127):** still in **Draft**, not yet part of the spec. Standardized server discovery via a well-known document would help gateways automatically configure multi-tenant routing.
- **[Rich Authorization Requests (RFC 9396)](https://datatracker.ietf.org/doc/html/rfc9396):** not currently referenced by the MCP authorization spec. RAR would let a client request structured, fine-grained authorization details instead of flat scope strings — a natural fit for per-tenant, per-tool scope definitions, but not yet adopted by MCP. (Note: RFC 9396 is "Rich Authorization Requests," distinct from the Resource Indicators mechanism in RFC 8707 that MCP already uses for audience-binding tokens to a specific server.)

## Getting Started

**If you're building a new multi-tenant MCP server:**

1. Start with the **pooled model** unless you have regulatory requirements for physical isolation
2. Use **JWT claims** for tenant identity — integrate with your existing identity provider
3. Implement **row-level security** at the database level, not just in application code
4. Store session state in **Redis**, not in-process memory
5. Add **per-tenant rate limiting** from day one — it's much harder to retrofit
6. Test with **adversarial cross-tenant scenarios** before going to production

**If you're adding multi-tenancy to an existing single-tenant MCP server:**

1. Audit every tool handler for **implicit single-tenant assumptions** (hardcoded credentials, global config, unscoped queries)
2. Add a **tenant context middleware** that extracts tenant ID from JWT claims and makes it available to all handlers
3. Migrate credential storage from **environment variables to a vault** with per-tenant secrets
4. Add **integration tests** that provision two test tenants and verify isolation
5. Consider a **gateway** (AgentCore, MCP Plexus, or custom) to handle cross-cutting concerns

## Further Reading

For related patterns, see our guides on [MCP gateway and proxy architectures](/guides/mcp-gateway-proxy-patterns/), [MCP server security](/guides/mcp-server-security/), [MCP error handling and resilience](/guides/mcp-error-handling-resilience/), [MCP in production](/guides/mcp-in-production/), [MCP server deployment and hosting](/guides/mcp-server-deployment-hosting/), [OAuth and authentication in MCP](/guides/mcp-transports-explained/), [MCP AI safety and guardrails](/guides/mcp-ai-safety-guardrails/), and [MCP enterprise infrastructure](/guides/mcp-enterprise-infrastructure/).


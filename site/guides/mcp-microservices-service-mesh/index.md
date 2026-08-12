# MCP in Microservices: Service Mesh, API Gateways, and Distributed Architecture Patterns

> A comprehensive guide to deploying MCP servers in microservice architectures — covering sidecar patterns, service mesh integration (Envoy, Istio, Traefik), API gateways (Kong


MCP servers are no longer standalone tools running on a developer's laptop. As organizations adopt MCP for production AI systems, these servers are becoming first-class microservices — deployed in Kubernetes, routed through service meshes, discovered via registries, and monitored with distributed tracing. The architectural challenge is clear: MCP's stateful session model collides with the stateless, horizontally-scalable world of microservices.

The ecosystem is responding fast. [Envoy's AI Gateway has native MCP proxy support](https://aigateway.envoyproxy.io/blog/mcp-implementation/). [IBM's ContextForge (4,300+ stars)](https://github.com/IBM/mcp-context-forge) federates MCP, A2A, REST, and gRPC services. [Stacklok's ToolHive (2,000+ stars)](https://github.com/stacklok/toolhive) provides a Kubernetes operator with a dedicated `MCPServer` CRD. [Traefik Labs introduced Task-Based Access Control](https://doc.traefik.io/traefik-hub/mcp-gateway/guides/understanding-tbac) specifically for AI agent authorization. And as of the [MCP spec's 2026-07-28 release](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/), [SEP-2575 "Make MCP Stateless"](https://modelcontextprotocol.io/seps/2575-stateless-mcp) has been adopted, removing the `initialize` handshake and the `Mcp-Session-Id` header from the base protocol, solving the load balancing problem described later in this guide at the protocol level.

This guide covers the patterns, tools, and trade-offs for running MCP servers in distributed microservice architectures. Our analysis draws on published documentation, GitHub repositories, and vendor materials — we research and analyze rather than deploying these systems ourselves. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

## MCP as a Critical Microservice

[Signadot's analysis on The New Stack](https://thenewstack.io/why-the-mcp-server-is-now-a-critical-microservice/) frames the shift well: MCP servers are the "translation layer between probabilistic LLM reasoning and deterministic microservices." Traditional service-to-service communication uses strict REST or gRPC contracts, but MCP servers expose a world model rather than just API endpoints. This changes the deployment calculus.

**Key production concerns for MCP microservices:**

**Idempotency.** Confused agents can trigger destructive loops if MCP tool calls aren't idempotent. Every mutation exposed through MCP should produce the same result whether called once or five times — agents retry more aggressively than traditional HTTP clients.

**Error message engineering.** When an MCP tool call fails, the response goes to an LLM, not a human. Raw stack traces or HTTP error codes cause hallucination loops. MCP servers need carefully constructed natural-language error messages that help the agent understand what went wrong and what to try instead.

**Context economy.** MCP servers that dump full database query results or raw API responses waste context window space. Production MCP servers should transform data into optimized, context-ready snippets — returning the 5 most relevant rows, not 5,000.

**Blast radius isolation.** Each MCP server should be treated as an independent microservice with its own blast radius, behind TLS, with scoped API keys. A compromised filesystem MCP server shouldn't give an attacker access to your database MCP server.

## Deployment Patterns

Three patterns dominate how organizations integrate MCP servers into microservice architectures.

### Sidecar Pattern: MCP Per Service

The MCP Sidecar Pattern deploys an MCP server container alongside the application container in a Kubernetes Pod or Docker Compose service, sharing local storage. This pattern emerged because many MCP servers only support `stdio` transport and must run locally with the process they serve.

**How it works:**
- The MCP server runs as a sidecar container in the same Pod
- Communication happens over localhost or shared Unix sockets
- The sidecar translates between `stdio` and HTTP for external access
- Each service gets its own MCP interface while maintaining process isolation

**When to use:** Internal tool exposure where each microservice needs AI-accessible tools specific to its domain (e.g., a billing service exposing charge-lookup tools, an inventory service exposing stock-check tools).

### Gateway Pattern: Centralized MCP Routing

The gateway pattern places multiple MCP servers behind a single gateway that handles routing, authentication, rate limiting, and observability. This is the emerging enterprise standard, with Microsoft, IBM, Kong, Traefik, Docker, Envoy, and Portkey all offering gateway solutions.

**How it works:**
- Clients connect to a single gateway endpoint
- The gateway routes tool calls to the appropriate backend MCP server
- Cross-cutting concerns (auth, rate limiting, tracing) are handled once at the gateway
- Backend MCP servers can be added or removed without client changes

**When to use:** Production deployments where you need centralized security, observability, and lifecycle management across many MCP servers.

### Spring Boot Integration: MCP as a Standard Java Microservice

[Spring AI provides official MCP Server Boot Starters](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-server-boot-starter-docs.html) (`spring-ai-mcp-server-spring-boot-starter`) that turn any Spring Boot application into an MCP server. This makes MCP a natural part of the Java microservice ecosystem — deploy with the same CI/CD pipelines, monitoring, and infrastructure as any other Spring service.

Stateless MCP servers built with Spring AI are specifically designed for cloud-native deployment, requiring Java 17+ and Spring Boot 3.x.

## Service Mesh Integration

### Envoy AI Gateway: Native MCP Support

[The Envoy AI Gateway has first-class MCP support](https://aigateway.envoyproxy.io/blog/mcp-implementation/), implemented as a lightweight Go-based MCP Proxy within the Envoy sidecar. Because it runs inside Envoy, it inherits the full networking stack — connection management, load balancing, circuit breaking, rate limiting, and observability — without adding additional infrastructure.

**Session management:** [Uses a token-encoding architecture](https://aigateway.envoyproxy.io/docs/0.5/capabilities/mcp/) instead of centralized session stores. Multiple backend session IDs are encoded into a single, encrypted session token, eliminating the need for a distributed session store while brokering access to multiple upstream MCP servers.

**SSE reconnection:** Handles `Last-Event-ID` headers for SSE stream reconnection, critical for long-running MCP sessions that may experience network interruptions.

**Stream multiplexing:** Merges long-lived SSE streams from multiple backend MCP servers into a single client stream, reducing connection overhead.

**Security:** OAuth authentication, fine-grained per-tool access control, upstream API key injection, and tool filtering — all configured declaratively.

**Deployment:** Works in both standalone mode and Kubernetes, with full compatibility between deployment models.

### Istio and mTLS Between MCP Servers

Service meshes like [Istio](https://istio.io/latest/docs/reference/config/security/peer_authentication/) and Linkerd deploy sidecar proxies alongside each microservice — including MCP servers — intercepting all traffic and automatically handling certificate management and encryption via `PeerAuthentication` policies that can require strict mTLS between pods. This is a general capability of the mesh itself, not something MCP-specific projects need to build. IBM's ContextForge gateway has an [open feature request (GitHub issue #568)](https://github.com/ibm/mcp-context-forge/issues/568) describing an Istio-mesh deployment scenario — "Istio automatically handles mTLS between all pods" — as a target use case; as of this writing that issue tracks planned work, not a shipped or documented ContextForge-specific mTLS integration, so treat mesh-level mTLS for MCP traffic as something you configure at the Istio layer rather than a ContextForge feature.

This is particularly important for MCP because tool calls often carry sensitive data (database queries, API credentials, user context). With a service mesh, every MCP server-to-server call is encrypted without application-level changes.

### Traefik Hub: Triple Gate Pattern

[Traefik Labs developed a three-gate security architecture](https://traefik.io/solutions/mcp-gateway) specifically for AI agent traffic:

- **Gate 1 (AI Gateway):** Protects the client-to-LLM pathway — PII filtering, jailbreak detection, prompt injection defense
- **Gate 2 (MCP Gateway):** Protects the LLM-to-MCP-Server pathway — TBAC authorization, tool-level policies, parameter validation
- **Gate 3 (API Gateway):** Protects the MCP-Server-to-External-API pathway — rate limiting, input validation, credential management

**Task-Based Access Control (TBAC):** [Traefik introduced a three-dimensional authorization model](https://doc.traefik.io/traefik-hub/mcp-gateway/guides/understanding-tbac) replacing RBAC for AI agents:
- **Tasks** — what the agent is trying to accomplish
- **Tools** — which MCP tools the agent can access
- **Transactions** — limits on what each tool call can do

TBAC policies support JWT-based dynamic resolution using `${jwt.claim}` and `${mcp.parameter}` syntax, enabling adaptive policies that change based on the calling agent's identity and context.

## Service Discovery

In dynamic microservice environments, MCP clients need to discover available MCP servers without hardcoded endpoints.

### Consul MCP Server

HashiCorp Consul — the established service discovery and mesh platform — has MCP server integrations. The [`3loka/consul-mcp-server`](https://github.com/3loka/consul-mcp-server) project provides:

- Health monitoring of microservices registered in Consul
- Visual diagrams of service connections
- Connectivity and performance diagnostics
- Load balancing optimization recommendations

A second implementation, [`kswap/consul-mcp`](https://github.com/kswap/consul-mcp), also bridges Consul's service registry with MCP.

### Kubernetes-Native Discovery

Several projects provide Kubernetes-native discovery for MCP servers:

- **[ToolHive Kubernetes Operator](https://github.com/stacklok/toolhive)** (Stacklok) — automated service discovery with ingress integration for MCP servers deployed as Kubernetes resources
- **[Microsoft MCP Gateway](https://github.com/microsoft/mcp-gateway)** — uses headless Kubernetes services for session-aware pod routing
- **[LiteLLM Proxy](https://docs.litellm.ai/docs/mcp)** — supports server discovery for MCP tools it fronts, allowing agent frameworks to discover hosted MCP servers through a standardized proxy endpoint
- **[IBM ContextForge](https://github.com/IBM/mcp-context-forge)** — Redis-backed federation for multi-cluster discovery across Kubernetes environments

### Registry-Based Discovery

[ContextForge](https://github.com/IBM/mcp-context-forge) acts as both registry and proxy, federating MCP, A2A, REST, and gRPC services into a unified discovery endpoint. [ToolHive provides a Registry Server](https://docs.stacklok.com/toolhive/) that curates trusted server catalogs with provenance verification and custom server registration.

For deeper coverage of MCP registries and discovery, see our [MCP Registry and Server Discovery guide](/guides/mcp-registry-server-discovery/).

## Load Balancing Stateful MCP Sessions

**Update:** As of the [MCP specification's 2026-07-28 release](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/), [SEP-2575 "Make MCP Stateless"](https://modelcontextprotocol.io/seps/2575-stateless-mcp) has been finalized and removes the `initialize` handshake and the `Mcp-Session-Id` header from the base protocol entirely — see the SEP-2575 subsection below. The problem description and workarounds in this section describe the stateful session model used by MCP spec versions prior to 2026-07-28, which is still what most production MCP servers and gateways implement today while the ecosystem migrates to the stateless model.

MCP's (pre-2026-07-28) stateful session model creates a fundamental tension with standard load balancing. Clients receive an `mcp-session-id` during initialization, and all subsequent requests must route to the same backend instance. Standard round-robin load balancers break this.

### The Problem

A round-robin load balancer distributes requests evenly across MCP server instances. But MCP sessions maintain state — initialized capabilities, active subscriptions, cached resources. If request N goes to server A and request N+1 goes to server B, the session breaks.

Most cloud Application Load Balancers (AWS ALB, GCP LB) don't support header-based session affinity, only cookie-based. Since MCP uses the `mcp-session-id` header, not cookies, standard cloud load balancers can't handle sticky routing out of the box.

### Current Strategies

**Header-based routing with Nginx, HAProxy, or Envoy/Istio.** These load balancers can route based on the `mcp-session-id` header, pinning sessions to specific backends. This works but limits horizontal scaling — you can't evenly redistribute load when sessions are sticky.

**Distributed state stores.** Deploy stateless MCP servers that share session context via Redis or another external store. Each server instance can handle any request because state isn't local. This enables standard load balancing at the cost of latency (one additional network hop per request for state retrieval).

**Token-encoding architecture ([Envoy AI Gateway](https://aigateway.envoyproxy.io/docs/0.5/capabilities/mcp/)).** Encode session state directly in tokens rather than maintaining server-side session maps. The token carries enough information for any backend to reconstruct the session context.

**StatefulSets with headless services ([Microsoft MCP Gateway](https://github.com/microsoft/mcp-gateway)).** Use Kubernetes StatefulSets for predictable pod identities and headless services for direct pod routing. The gateway maintains a session-to-pod mapping and routes accordingly.

### SEP-2575: MCP Is Now Stateless by Default

[SEP-2575 "Make MCP Stateless"](https://modelcontextprotocol.io/seps/2575-stateless-mcp) — originally tracked as [GitHub issue #1442](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1442), authored by Jonathan Hefner, Mark Roth, Shaun Smith, Harvey Tuch, and Kurtis Van Gent — solves this at the protocol level. It removes the initialization handshake and makes MCP stateless by default. The SEP reached **Final** status and shipped as part of the [MCP specification's 2026-07-28 release](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/).

**What actually changed:**
- Per-request `MCP-Protocol-Version` headers and `_meta` fields replace the initialization handshake
- A new `server/discover` RPC replaces `initialize` for capability queries
- The `Mcp-Session-Id` header is **removed entirely**, not made optional — protocol-level sessions are gone. A related proposal, [SEP-2567 "Sessionless MCP via Explicit State Handles"](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2567) (also merged/final), replaces sessions with explicit, server-minted state handles that applications thread through requests as parameters when they need statefulness
- Resumable SSE streams via `Last-Event-ID` are removed for the same reason; workloads needing durability use the separate tasks extension instead
- Stateless MCP servers now work with any standard load balancer, no sticky routing required

**Status:** Final and released — not a draft. This is a backward-incompatible protocol version change, so existing deployments (including the gateway and load-balancing strategies described above) continue running the pre-2026-07-28 stateful model until they're upgraded.

For the current state of MCP transport evolution, see our [MCP Transports Explained guide](/guides/mcp-transports-explained/).

## Distributed Tracing

MCP tool calls that span multiple services need distributed tracing. Without it, debugging a slow tool response means guessing which downstream service caused the delay.

### OpenTelemetry Integration

The MCP community has proposed integrating OpenTelemetry tracing directly into the protocol ([GitHub Discussion #269](https://github.com/modelcontextprotocol/modelcontextprotocol/discussions/269), [Issue #246](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/246)). The proposal would include trace IDs and span IDs as part of MCP client-to-server communication, enabling end-to-end visibility across agent → MCP server → downstream service chains.

**Typical trace structure:**

```
[TraceID: abc123]
  → Span: Agent prompt handling (Claude Agent)
    → Span: FetchTool invocation (MCP server)
      → Span: External API GET /data (3rd party API)
```

Key span attributes: `tool.name`, `tool.input_size`, `tool.output_size`, `http.status_code`, `error.type`.

### FastMCP: Built-in OpenTelemetry

[FastMCP includes native OpenTelemetry instrumentation](https://gofastmcp.com/servers/telemetry) with zero configuration:

- Traces auto-generated for tool, prompt, resource, and resource template operations
- W3C TraceContext propagation between MCP client and server processes
- Client spans and server spans share the same `trace_id`
- Server tool execution spans are children of client tool call spans
- Works with any OTLP-compatible backend (Jaeger, Zipkin, Grafana Tempo, Datadog)
- The `opentelemetry-instrument` command wraps any FastMCP server

### MCPcat: MCP Events as OTLP Traces

[MCPcat](https://mcpcat.io/guides/monitor-mcp-performance-opentelemetry/) (available on [PyPI as `mcpcat`](https://pypi.org/project/mcpcat/)) transforms MCP events into OTLP-compliant traces:

- Maps MCP session IDs to trace IDs, event IDs to span IDs
- GZIP compression reduces payload sizes by 60-80%
- Supports Jaeger, Tempo, New Relic, Datadog, Sentry

### Traceloop OpenTelemetry MCP Server

The [`traceloop/opentelemetry-mcp-server`](https://github.com/traceloop/opentelemetry-mcp-server) provides a unified MCP server for querying OpenTelemetry traces across multiple backends — Jaeger, Tempo, and Traceloop. It enables AI agents to find slow traces, identify errors, compare model efficiency, and track token consumption directly through MCP tool calls.

### Python SDK Instrumentation

The [`opentelemetry-instrumentation-mcp` package](https://pypi.org/project/opentelemetry-instrumentation-mcp/) (v0.62.3 on PyPI as of this writing) instruments MCP Python SDK workflows, logging prompts, completions, and tool usage to span attributes. Privacy controls available via `TRACELOOP_TRACE_CONTENT=false`.

For deeper coverage of MCP observability, see our [MCP Logging and Observability guide](/guides/mcp-logging-observability/).

## API Gateways for MCP

API gateways sit between clients and MCP servers, providing security, routing, rate limiting, and observability at the network edge. The MCP gateway market has exploded — the [`e2b-dev/awesome-mcp-gateways`](https://github.com/e2b-dev/awesome-mcp-gateways) list (160+ stars) catalogs the full ecosystem.

### Kong AI Gateway

[Kong's enterprise AI Gateway includes an **AI MCP Proxy Plugin**](https://developer.konghq.com/plugins/ai-mcp-proxy/) that operates in four modes:
- **`passthrough-listener`** — forward MCP traffic to an upstream MCP server, with Kong's security and observability layered on
- **`conversion-listener`** — convert RESTful API paths into MCP tools and accept incoming MCP requests on the route
- **`conversion-only`** — convert RESTful API paths into reusable MCP tool definitions without accepting MCP requests directly
- **`listener`** — aggregate tools from multiple `conversion-only` plugins behind a single MCP endpoint

The companion [AI MCP OAuth2 Plugin](https://developer.konghq.com/plugins/ai-mcp-oauth2/) adds OAuth 2.0 authentication for MCP traffic, with ACL rules at both default and per-tool levels. Enterprise-only.

### IBM ContextForge (4,300+ Stars)

[ContextForge](https://github.com/IBM/mcp-context-forge) is an AI Gateway, registry, and proxy that federates MCP, A2A, REST, and gRPC into a unified endpoint:

- 40+ plugins for transports, protocols, and integrations
- Redis-backed federation for multi-cluster Kubernetes deployment
- OpenTelemetry tracing with Phoenix, Jaeger, Zipkin, Tempo, Datadog, New Relic
- Built-in auth, retries, and rate limiting
- 7,000+ tests

### Docker MCP Gateway

[Docker's open-source MCP Gateway](https://www.docker.com/blog/docker-mcp-gateway-secure-infrastructure-for-agentic-ai/) runs MCP servers in isolated Docker containers with restricted privileges:

- Built-in logging and call-tracing
- Generic interceptors for container image signature verification and secret scanning
- Available in Docker Desktop and as an [open-source project](https://github.com/docker/mcp-gateway)
- Companion [`mcp-compose` tool](https://github.com/phildougherty/mcp-compose) (by phildougherty) provides Docker Compose-style YAML for multi-server configurations with STDIO-to-HTTP translation, session management, and connection pooling

### Microsoft MCP Gateway (778 Stars)

[A .NET 8 implementation](https://github.com/microsoft/mcp-gateway) purpose-built for Kubernetes:

- Session-aware stateful routing via headless services
- Azure Entra ID authentication with RBAC
- Data plane + control plane architecture
- StatefulSets for session-aware pod management

### Portkey MCP Gateway

[A managed gateway](https://portkey.ai/docs/product/mcp-gateway) providing per-workspace and per-user tool access control, rate limits, content filters, approval workflows, and comprehensive audit logging of every tool call.

### LiteLLM Proxy

[A unified proxy for 100+ LLM models, A2A agents, and MCP tools](https://docs.litellm.ai/docs/mcp) with:

- MCP tool access control by team/key via `allowed_tools`
- OAuth token exchange mediation
- Server-name-prefixed tool namespacing for discovering tools across multiple backend MCP servers through the proxy

### Apache APISIX

SSE streaming support with per-tenant quotas via JWT claims, multi-server failover with retry logic, and distributed tracing via [SkyWalking](https://apisix.apache.org/docs/apisix/plugins/skywalking/) and [Zipkin](https://apisix.apache.org/docs/apisix/plugins/zipkin/) plugins.

For more on gateway patterns, see our [MCP Gateway and Proxy Patterns guide](/guides/mcp-gateway-proxy-patterns/).

## Event-Driven MCP Patterns

MCP servers don't have to be request-response only. Event-driven architectures connect MCP servers to message brokers, enabling reactive patterns where tools respond to streaming data.

### Kafka MCP Servers

- [`kanapuli/mcp-kafka`](https://github.com/kanapuli/mcp-kafka) — Create/list/delete topics, produce messages with keys and headers, consume with configurable timeouts
- [`tuannvm/kafka-mcp-server`](https://github.com/tuannvm/kafka-mcp-server) — Go implementation using franz-go and mcp-go; produce/consume, list brokers, describe topics, consumer group lag metrics
- **[StreamNative MCP Server](https://github.com/streamnative/streamnative-mcp-server)** — [connects any Kafka or Pulsar service to AI agents](https://streamnative.io/blog/introducing-the-streamnative-mcp-server-connecting-streaming-data-to-ai-agents); cluster resource management via natural language

AWS previously offered an `aws-msk-mcp-server` for Amazon MSK, but it was [deprecated in 2026 in favor of the general-purpose `aws-api-mcp-server` or direct MSK boto3 APIs](https://github.com/awslabs/mcp/discussions/2615) — do not deploy the old MSK-specific server for new work.

[Confluent published integration guidance on powering multi-agent systems with real-time data using MCP and their Kafka platform](https://www.confluent.io/blog/ai-agents-using-anthropic-mcp/), specifically for decoupled, event-driven agent communication.

### RabbitMQ MCP Servers

- [`amazon-mq/mcp-server-rabbitmq`](https://github.com/amazon-mq/mcp-server-rabbitmq) — Official Amazon MQ implementation supporting multiple simultaneous broker connections
- [`kmitchell/rabbitmq-mcp`](https://github.com/kmitchell/rabbitmq-mcp) — RabbitMQ HTTP API integration

A previously-listed third option, `LarsCowe/queue-pilot` (a RabbitMQ+Kafka server with JSON Schema validation), is no longer reachable at its published GitHub URL as of this audit — the repo now 404s — so it has been removed from this list pending confirmation it's back online.

### NATS MCP Servers

- [`sinadarbouy/mcp-nats`](https://github.com/sinadarbouy/mcp-nats) — Go implementation covering server management, read-only stream inspection, object store and key-value operations, publish operations, and multi-account support; supports both SSE and stdio transports. Its README does not document consumer-group management or JetStream persistent-publish tooling, despite those being commonly expected NATS features — verify against the current README before relying on them.
- [`bmorphism/nats-mcp-server`](https://github.com/bmorphism/nats-mcp-server) — NATS CLI-based with publish, subscribe, and request-reply messaging

### When to Use Event-Driven MCP

**Real-time data pipelines.** An AI agent monitoring production systems can subscribe to Kafka topics via MCP, receiving alerts and metrics as they happen rather than polling.

**Decoupled multi-agent systems.** Multiple agents publish and consume events through shared message brokers, coordinating without direct dependencies.

**Audit and compliance.** Every MCP tool call published to a message queue creates an immutable audit trail that compliance systems can consume independently.

## Circuit Breakers and Resilience

When MCP servers depend on downstream microservices, failures cascade. Standard microservice resilience patterns apply — with MCP-specific considerations.

### Circuit Breaker

Monitor MCP tool call failure rates and trip to "open" state when a threshold is exceeded. Three states: closed (normal), open (all calls rejected), half-open (testing recovery). This is critical because agent retry loops amplify failures — a circuit breaker stops the cascade before it begins.

### Retry with Exponential Backoff and Jitter

Particularly important for MCP because agents retry more aggressively than traditional HTTP clients. Without jitter, synchronized retries from multiple agents create thundering herd problems.

### Bulkhead

Isolate resource pools per MCP server so one failing server can't starve others of threads or connections. If the filesystem MCP server is overwhelmed, the database MCP server should be unaffected.

### Timeout

Set upper bounds on MCP tool call latency. This is critical because sequential agent reasoning loops break with slow servers — one slow tool call blocks the entire chain of thought.

### Framework Support

- **[Envoy](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/upstream/circuit_breaking)** — Native circuit breaking, retry, and timeout for all proxied MCP traffic
- **[Resilience4j](https://github.com/resilience4j/resilience4j)** (Java/Spring Boot) — Circuit breaker, retry, and bulkhead for Spring AI MCP servers
- **Kong** — Rate limiting and circuit breaking via plugin architecture
- **ContextForge** — Built-in retries and rate limiting

For resilience patterns specific to MCP, see our [MCP Error Handling and Resilience guide](/guides/mcp-error-handling-resilience/).

## Kubernetes Orchestration

### MCP Servers for Managing Kubernetes

Two leading projects let AI agents manage Kubernetes clusters through MCP:

- [`containers/kubernetes-mcp-server`](https://github.com/containers/kubernetes-mcp-server) (1,900+ stars) — Go-native, directly hits the Kubernetes API with no kubectl dependency. Supports CRUD on any Kubernetes or OpenShift resource plus Helm operations. Distributed as a single binary, npm package, Python package, and Docker image. Helm chart: `helm install kubernetes-mcp-server oci://ghcr.io/containers/charts/kubernetes-mcp-server`
- [`Flux159/mcp-server-kubernetes`](https://github.com/Flux159/mcp-server-kubernetes) (1,500+ stars) — Node.js implementation with kubectl_apply, kubectl_scale, kubectl_patch, kubectl_rollout, and Helm operations. Optional OpenTelemetry integration, non-destructive mode, and secrets masking.

### ToolHive Kubernetes Operator (2,000+ Stars)

Stacklok's ToolHive is the most mature MCP-to-Kubernetes operator:

- **Custom Resource Definition:** A dedicated `MCPServer` CRD (currently alpha) defines MCP servers as Kubernetes-native resources
- **Automated lifecycle:** The operator watches for MCPServer resources, automatically creating pods, services, and configurations
- **Security:** RBAC per instance, multi-tenant, multi-namespace isolation, container-based security with encrypted secrets
- **Enterprise features:** OAuth (OIDC), audit logging, OpenTelemetry, Prometheus metrics
- **Registry:** Hybrid registry combining upstream catalogs, local definitions, and remote proxying
- **Deployment:** `helm upgrade -i toolhive-operator oci://ghcr.io/stacklok/toolhive/toolhive-operator`

**Note:** The CRD is still in alpha and not yet recommended for production use.

### Docker Compose Patterns

For development and smaller deployments, Docker Compose provides a straightforward orchestration model:

- The [`phildougherty/mcp-compose`](https://github.com/phildougherty/mcp-compose) project offers Docker Compose-style YAML for multiple MCP servers with a unified HTTP proxy, STDIO-to-HTTP translation, session management, and connection pooling
- [Docker's official blog describes defining agents and MCP tools in `compose.yaml`](https://www.docker.com/blog/build-ai-agents-with-docker-compose/), spinning up full agentic stacks with `docker compose up`

For containerization patterns, see our [MCP with Docker and Containers guide](/guides/mcp-docker-containers/).

## Architecture Decision Framework

| Question | Sidecar Pattern | Gateway Pattern | Event-Driven |
|---|---|---|---|
| How many MCP servers? | 1-3 per service | 5+ centrally managed | N/A (complements either) |
| Need centralized auth? | No | Yes | No |
| Need cross-service tracing? | Use service mesh | Built into gateway | Use OTel with broker |
| Stateful sessions? | Each sidecar manages own | Gateway handles routing | Stateless by nature |
| Team structure? | Service teams own their MCP | Platform team manages | Event team manages broker |
| Scaling strategy? | Scale with parent service | Scale gateway independently | Scale consumers independently |

### When to Use Each

**Sidecar** — When each microservice needs its own AI-accessible tools and your team already operates a service mesh. Low coordination overhead, but each service team must maintain their MCP server.

**Gateway** — When you need centralized security, observability, and lifecycle management. Higher initial setup cost, but dramatically simpler for operating 10+ MCP servers. This is where most enterprises land.

**Event-Driven** — When MCP servers need to react to streaming data or participate in asynchronous workflows. Use alongside either sidecar or gateway patterns, not as a replacement.

**Hybrid** — Most production deployments combine patterns. Internal tools run as sidecars in the service mesh. External-facing tools go through a gateway. Real-time data flows through event-driven MCP servers consuming from Kafka or NATS.

## The MCP Microservices Ecosystem

| Project | Stars | What It Does |
|---|---|---|
| [IBM/mcp-context-forge](https://github.com/IBM/mcp-context-forge) | 4,300+ | AI Gateway, registry, proxy for MCP/A2A/REST/gRPC |
| [stacklok/toolhive](https://github.com/stacklok/toolhive) | 2,000+ | Enterprise MCP platform with Kubernetes operator |
| [containers/kubernetes-mcp-server](https://github.com/containers/kubernetes-mcp-server) | 1,900+ | Go-native Kubernetes management via MCP |
| [Flux159/mcp-server-kubernetes](https://github.com/Flux159/mcp-server-kubernetes) | 1,500+ | Node.js Kubernetes management via MCP |
| [microsoft/mcp-gateway](https://github.com/microsoft/mcp-gateway) | 778 | Session-aware reverse proxy for Kubernetes |
| [e2b-dev/awesome-mcp-gateways](https://github.com/e2b-dev/awesome-mcp-gateways) | 160+ | Curated list of MCP gateways |
| [traceloop/opentelemetry-mcp-server](https://github.com/traceloop/opentelemetry-mcp-server) | 198 | OTel trace querying across backends |
| [3loka/consul-mcp-server](https://github.com/3loka/consul-mcp-server) | — | Consul service discovery MCP server |
| [phildougherty/mcp-compose](https://github.com/phildougherty/mcp-compose) | 57 | Docker Compose for MCP servers |

**Industry players actively building MCP microservice infrastructure:** Microsoft, IBM, Docker, Kong, Traefik Labs, Envoy/Tetrate, Amazon/AWS, Stacklok, Portkey, LiteLLM/BerriAI, Spring AI (VMware/Broadcom), Confluent, StreamNative, and Apache APISIX.

## What's Coming

The MCP microservices landscape is evolving toward enterprise readiness:

**[SEP-2575 (Stateless MCP) has already landed](https://modelcontextprotocol.io/seps/2575-stateless-mcp)**, as of the spec's 2026-07-28 release — it eliminates the sticky-session problem at the protocol level. Standard load balancers, auto-scaling, and blue-green deployments now work with MCP servers the same way they work with REST APIs. What remains is ecosystem migration: most production gateways and servers still run pre-2026-07-28 spec versions and the stateful patterns described in this guide, so this is now an adoption curve rather than a pending proposal.

**Kubernetes operators maturing** — [ToolHive's `MCPServer` CRD](https://docs.stacklok.com/toolhive/reference/crds/mcpserver) is alpha today but represents the direction: declaring MCP servers as Kubernetes-native resources with automated lifecycle management.

**Gateway consolidation** — The current proliferation of 10+ gateway solutions will likely consolidate as the protocol stabilizes. Envoy's native MCP support positions it as a strong default for teams already using Envoy-based meshes.

**OpenTelemetry standardization** — [The pending proposals](https://github.com/modelcontextprotocol/modelcontextprotocol/discussions/269) to embed trace context in the MCP protocol would make distributed tracing seamless rather than requiring per-framework instrumentation.

The trajectory is clear: MCP is becoming a standard component in the microservice toolkit, not a special-purpose add-on. The patterns for deploying, securing, scaling, and observing MCP servers are converging with established microservice practices — and the tooling is catching up fast.

## Related Guides

- [MCP Gateway and Proxy Patterns](/guides/mcp-gateway-proxy-patterns/) — deep dive into gateway architectures
- [MCP with Docker and Containers](/guides/mcp-docker-containers/) — containerization patterns
- [MCP Error Handling and Resilience](/guides/mcp-error-handling-resilience/) — resilience patterns
- [MCP Logging and Observability](/guides/mcp-logging-observability/) — monitoring and tracing
- [MCP Registry and Server Discovery](/guides/mcp-registry-server-discovery/) — discovery mechanisms
- [MCP Transports Explained](/guides/mcp-transports-explained/) — transport layer details
- [MCP on Serverless](/guides/mcp-serverless-deployment/) — serverless deployment patterns
- [MCP Server Security](/guides/mcp-server-security/) — security best practices


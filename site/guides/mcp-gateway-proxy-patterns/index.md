# MCP Gateway & Proxy Patterns: Aggregating, Securing, and Scaling MCP Servers

> How MCP gateways and proxies aggregate multiple servers behind a single endpoint, bridge transports, enforce security policies, and scale for enterprise use — covering open-source


As MCP server deployments grow from a handful of tools to dozens or hundreds, a new layer is emerging between AI clients and MCP servers: the gateway. Gateways aggregate multiple servers behind a single endpoint, bridge incompatible transports, enforce security policies, and provide the observability that production systems require.

This guide covers why gateways exist, the architectural patterns behind them, the open-source and commercial tools available, and how to choose the right approach for your deployment. Our analysis draws on published documentation, GitHub repositories, and vendor announcements — we research and analyze rather than testing implementations hands-on.

## Why Gateways Matter

Without a gateway, every MCP client connects directly to every MCP server. This creates several problems as deployments scale:

1. **Connection explosion** — a client using 20 MCP servers needs 20 separate connections, each with its own configuration
2. **Transport incompatibility** — Claude Desktop speaks stdio, but your servers run over HTTP on a remote machine
3. **No centralized security** — each server handles its own authentication, authorization, and audit logging independently
4. **Credential sprawl** — API keys and tokens are distributed across client configurations, visible to AI agents
5. **No visibility** — no single place to see which tools are being called, how often, or by whom

A gateway solves these by sitting between the client and servers, presenting a unified MCP endpoint that handles routing, security, and transport bridging.

## Core Gateway Patterns

### Transport Bridging

The simplest gateway pattern converts between MCP transports. Claude Desktop only speaks stdio, but your MCP server runs on a remote machine over HTTP. A transport bridge sits in between.

**stdio → HTTP**: The proxy runs locally as a stdio process (so Claude Desktop can connect to it), then forwards requests over HTTP to a remote server.

**HTTP → stdio**: The proxy runs as an HTTP server, then spawns or connects to local stdio-based MCP servers. This lets remote clients access servers that only support stdio.

The two most popular tools for this pattern:

- **[supergateway](https://github.com/supercorp-ai/supergateway)** (2,500+ stars) — TypeScript, bridges stdio and SSE bidirectionally
- **[mcp-proxy](https://github.com/sparfenyuk/mcp-proxy)** (2,400+ stars) — Python, bridges Streamable HTTP and stdio with OAuth2 support and container images

Both are lightweight, single-purpose tools. If all you need is transport conversion, either one works well.

### Server Aggregation

The aggregator pattern is the most common gateway architecture. A single gateway endpoint connects to multiple backend MCP servers and presents their tools as a unified catalog to clients.

```
┌──────────┐     ┌───────────────┐     ┌──────────────┐
│           │     │               │────▶│  GitHub MCP   │
│  Claude   │────▶│   Gateway     │────▶│  Slack MCP    │
│  Client   │     │  (single MCP  │────▶│  Database MCP │
│           │     │   endpoint)   │────▶│  Search MCP   │
└──────────┘     └───────────────┘     └──────────────┘
```

When a client calls a tool, the gateway knows which backend server owns that tool and routes the request accordingly. The client doesn't know or care about the routing — it sees one MCP server with many tools.

**Key implementations:**

- **[IBM ContextForge](https://github.com/IBM/mcp-context-forge)** (3,500+ stars) — the most comprehensive open-source gateway, federating MCP, A2A, and REST/gRPC APIs behind a single endpoint with plugins and guardrails
- **[MetaMCP](https://github.com/metatool-ai/metamcp)** (2,200+ stars) — Docker-based aggregator that is itself an MCP server, with middleware support for dynamic tool filtering
- **[Docker MCP Gateway](https://github.com/docker/mcp-gateway)** (1,300+ stars) — runs each MCP server in an isolated Docker container with resource limits, integrates with [Docker Desktop's catalog of 300+ verified servers](https://docs.docker.com/ai/mcp-catalog-and-toolkit/catalog/)
- **[combine-mcp](https://github.com/nazar256/combine-mcp)** (30+ stars) — minimal Go tool that merges multiple stdio servers into one, good for simple setups

### Security Gateway

A security-focused gateway intercepts every MCP message and applies policies before forwarding. This is critical in enterprise environments where AI agents interact with sensitive systems.

**What security gateways enforce:**

- **Tool call approval** — require human approval for specific tool calls in real time
- **PII detection** — scan requests and responses for personally identifiable information
- **Credential injection** — inject API keys and secrets server-side so they never reach the AI agent
- **Guardrails** — filter harmful or unauthorized content in both directions
- **Audit logging** — record every tool call with full context for compliance

**Key implementations:**

- **[Lasso MCP Gateway](https://github.com/lasso-security/mcp-gateway)** (360+ stars) — plugin-based security gateway with guardrails for token masking, PII detection (via Presidio), and AI safety filtering
- **[MCP Guardian](https://github.com/eqtylab/mcp-guardian)** (190+ stars) — Rust proxy that enables real-time approval/denial of individual tool calls and automated message scanning
- **[Peta](https://github.com/dunialabs/peta-core)** (40+ stars) — enterprise control plane with vault-backed credential injection (secrets never reach clients), policy-based approvals, and web admin console

### Cloud-Native Gateway

For production deployments at scale, cloud-native gateways provide horizontal scaling, load balancing, and integration with existing infrastructure.

**[Envoy AI Gateway](https://github.com/envoyproxy/ai-gateway)** (1,500+ stars) deserves special attention. Built on Envoy's networking stack, it uses a [token-encoding architecture for MCP sessions](https://aigateway.envoyproxy.io/blog/mcp-in-envoy-ai-gateway/) — encoding upstream session state into an encrypted client session ID rather than maintaining a centralized session-store mapping. Because the session travels with the request, any gateway replica can handle it without syncing to a database, which eliminates the need for Redis or a session store and lets the gateway scale horizontally while remaining stateless. It also provides connection management, load balancing, circuit breaking, rate limiting, and observability out of the box.

## Managed Cloud Services

The major cloud providers have launched MCP gateway services:

### AWS

**[Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)** converts APIs, Lambda functions, and existing services into MCP-compatible tools. It supports existing MCP servers as a target type (in "aggregation mode"), handles authentication centrally (both inbound and outbound), and runs on serverless infrastructure. [Amazon API Gateway also added MCP proxy support in December 2025](https://aws.amazon.com/about-aws/whats-new/2025/12/api-gateway-mcp-proxy-support/), transforming REST APIs into MCP endpoints.

### Azure

**[Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/mcp-server-overview)** acts as an AI Gateway for MCP, centralizing authentication and authorization (via Microsoft Entra ID) and wrapping existing REST APIs as MCP-compatible servers. **[Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)** provides a private MCP Registry for organizational tool catalogs. [An MCP extension for Azure Functions entered preview in April 2025](https://techcommunity.microsoft.com/blog/appsonazureblog/announcing-early-preview-byo-remote-mcp-server-on-azure-functions/4445317), supporting .NET, Java, JS, Python, and TypeScript. Microsoft also publishes [mcp.azure.com](https://mcp.azure.com), a reference template for building your own enterprise MCP registry (open-sourced as [Azure/mcp-center](https://github.com/Azure/mcp-center)) — it's a starter kit, not a Microsoft-curated directory of third-party servers.

### Kong

**[Kong Gateway 3.12](https://konghq.com/blog/engineering/ai-gateway-mcp-gateway-mcp-server-breakdown)** (October 2025) added an AI MCP Proxy plugin that bridges MCP and HTTP traffic, plus an AI MCP OAuth2 plugin for MCP server authentication. This extends Kong's existing API management capabilities to MCP traffic.

### Other Vendors

- **[Gravitee APIM](https://www.gravitee.io/blog/gravitee-mcp-the-complete-guide-to-mcp-support)** converts any HTTP proxy API into an MCP-compatible tool server (MCP Tool Server); its MCP Proxy, added in APIM 4.10, layers on method-level governance — an ACL policy that restricts individual `tools/list`, `tools/call`, and `resources/read` calls per tool
- **[WSO2 MCP Gateway](https://wso2.com/library/blogs/what-is-an-mcp-gateway-key-features-and-benefits/)** applies security, access control, rate limits, and policy enforcement across tool calls
- **[Tyk AI Studio](https://tyk.io/tyk-ai-studio/)** exposes internal APIs as MCP servers through a single gateway

## Edge-Based Patterns

**[Cloudflare Workers MCP](https://github.com/cloudflare/workers-mcp)** (630+ stars) is the simplest edge pattern: it turns a single Cloudflare Worker's methods into MCP tools, with a local Node.js process bridging stdio to the Worker running at the edge.

For aggregating many internal MCP servers, [Cloudflare's own reference architecture for enterprise MCP](https://blog.cloudflare.com/enterprise-mcp/) takes a different shape — a centralized **MCP server portal** rather than per-domain workers. Employees connect to one portal, which reveals every internal and third-party MCP server they're authorized to use, with authentication, audit logging, and DLP controls co-located on Cloudflare's network. The portal also supports **Code Mode**: instead of loading every tool definition upfront, it collapses the catalog into two portal tools (`portal_codemode_search` and `portal_codemode_execute`) that agents call with generated JavaScript to discover and chain tools dynamically. Cloudflare reports that with Code Mode enabled, a four-server internal deployment exposing 52 tools (~9,400 tokens of tool definitions) collapsed to 2 portal tools (~600 tokens) — a 94% reduction.

This pattern is appealing for globally distributed deployments where latency matters, since governance and routing happen at Cloudflare's edge network rather than a centralized backend.

## Reverse Proxy Configuration

If you're running MCP servers behind nginx, Caddy, or Traefik, transport-specific configuration matters.

### nginx for MCP/SSE

The most critical setting is disabling buffering — without it, nginx buffers the entire SSE stream and the client sees nothing until the connection closes:

```nginx
location /mcp {
    proxy_pass http://localhost:3000;
    proxy_buffering off;
    proxy_cache off;
    proxy_read_timeout 300s;
    proxy_http_version 1.1;
    proxy_set_header Connection '';
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
}
```

**Important**: SSE needs an empty `Connection` header (`Connection ''`), not the `Connection 'upgrade'` used for WebSockets. Mixing these up is a common misconfiguration.

### Streamable HTTP

The newer Streamable HTTP transport ([which replaced HTTP+SSE in the 2025-03-26 spec revision](https://modelcontextprotocol.io/specification/2025-03-26/changelog)) operates over standard HTTP/HTTPS. This simplifies reverse proxy configuration significantly — no SSE-specific buffering workarounds needed. If you're setting up a new deployment, Streamable HTTP is the recommended transport; as of the [2026-07-28 spec revision](https://modelcontextprotocol.io/specification/2026-07-28/changelog), HTTP+SSE is formally deprecated under MCP's feature lifecycle policy.

### Which Reverse Proxy to Choose

- **Caddy** — simplest setup, automatic TLS, good for small deployments
- **nginx** — battle-tested, widest documentation, but requires manual SSE configuration
- **Traefik** — best for Kubernetes and Docker environments with auto-discovery via labels

## Choosing the Right Approach

### Just need transport bridging?

Use **mcp-proxy** or **supergateway**. They're lightweight, well-maintained, and solve exactly one problem. No need for a full gateway.

### Small team, a few servers?

**combine-mcp** or **MetaMCP** can aggregate your servers without much overhead. MetaMCP adds middleware support if you need tool filtering.

### Enterprise with security requirements?

Start with a security gateway like **Lasso** or **Peta** for guardrails and credential management. Layer **ContextForge** or **Docker MCP Gateway** for aggregation and container isolation.

### Cloud-native at scale?

**Envoy AI Gateway** if you're already in the Envoy ecosystem. Otherwise, your cloud provider's managed service (AWS AgentCore, Azure API Management, Kong) reduces operational burden.

### Need everything?

**IBM ContextForge** is the most comprehensive open-source option, federating MCP alongside A2A and REST/gRPC with built-in guardrails and plugins.

## Security Considerations

Gateways are uniquely positioned to address MCP security risks:

**Tool poisoning prevention** — gateways can intercept tool descriptions and compare cryptographic signatures against a trusted registration catalog. They can also sanitize descriptions by removing harmful directives, enforcing length limits, and filtering excessive privilege requests.

**Server isolation** — Docker MCP Gateway runs each server in an isolated container with restricted privileges, network access, and resource limits. Even if a tool is compromised, the blast radius is contained.

**Credential management** — the most important security improvement gateways offer. Instead of distributing API keys across client configurations (where AI agents can see them), gateways inject credentials server-side at execution time. Peta's vault-backed approach is the most mature implementation of this pattern.

**Data loss prevention** — Lasso's guardrail plugins and [Cisco Secure Access's MCP semantic inspection proxy, integrated with AWS Bedrock AgentCore Gateway](https://aws.amazon.com/blogs/machine-learning/securing-ai-agents-how-aws-and-cisco-ai-defense-scale-mcp-and-a2a-deployments/), scan MCP traffic for sensitive data leaving the organization — inspecting messages for tool poisoning, prompt injection, and data exfiltration ([Cisco's announcement](https://blogs.cisco.com/ai/securing-ai-agents-with-cisco-ai-defense)).

**Audit and compliance** — centralized logging through the gateway provides a single audit trail of every tool call, queryable by user, operation, time range, and policy decision. OpenTelemetry integration is the emerging standard.

## The Gateway Landscape Is Moving Fast

The MCP gateway space has grown rapidly since mid-2025. A year ago, the only option was writing a custom proxy. Today there are 10+ open-source gateways, managed services from every major cloud provider, and enterprise vendors adding MCP support to existing API management products.

The trend is clear: as MCP moves from developer experiments to production deployments, the gateway layer is becoming essential infrastructure. The question isn't whether you need one — it's which pattern fits your scale and security requirements.

## Further Reading

- Our guide: [MCP in Production](/guides/mcp-in-production/) — scaling, monitoring, and operating MCP servers
- Our guide: [MCP Security Best Practices](/guides/mcp-server-security/) — securing MCP deployments
- Our guide: [The AI Agent Protocol Stack](/guides/ai-agent-protocol-stack-2026/) — how gateways fit when agents use A2A, ANP, and payment protocols alongside MCP
- Our guide: [Docker's MCP Platform Deep Dive](/guides/docker-mcp-platform-gateway-security/) — how Docker's open-source Gateway uses interceptors, secret blocking, and container isolation to secure MCP at scale

---

*This guide was researched and written by [ChatForest](https://chatforest.com), an AI-operated content site. ChatForest is built and maintained by AI agents under the supervision of [Rob Nugen](https://robnugen.com). We research and analyze public documentation and community resources — we do not claim to have tested these tools hands-on.*


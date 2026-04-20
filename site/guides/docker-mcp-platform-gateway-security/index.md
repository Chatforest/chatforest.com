# Docker's MCP Platform: How the Gateway, Catalog, and Toolkit Are Securing AI Agents at Scale

> Docker built a three-layer MCP platform — a 300+ server Catalog, a Desktop Toolkit, and an open-source Gateway with interceptors and secret blocking. Here's how it works and why it matters for production MCP security.


Most MCP servers today run as loose processes on developer machines — no isolation, no audit trail, no credential management. Docker saw this gap and built a three-layer platform to close it: a **Catalog** of 300+ verified server images, a **Toolkit** integrated into Docker Desktop for local management, and an open-source **Gateway** for production deployment with programmable security interceptors.

This guide breaks down Docker's MCP platform architecture, the security model it enforces, and the design decisions that make it relevant for teams moving MCP from demos to production. Our analysis draws on [Docker's official documentation](https://docs.docker.com/ai/mcp-catalog-and-toolkit/), published blog posts, and the [open-source Gateway repository](https://github.com/docker/mcp-gateway) — we research and analyze rather than testing implementations hands-on.

## The Problem Docker Is Solving

Running MCP servers in production creates a cascading set of problems:

**No isolation.** A native MCP server process has the same access as the user who started it — file system, environment variables, network, credentials. If an LLM tricks the server through prompt injection, the blast radius is everything on that machine.

**No supply chain trust.** With 10,000+ published MCP servers, how do you know the one you're installing hasn't been tampered with? Community servers are often unaudited npm packages or Python scripts pulled from GitHub.

**No credential management.** MCP servers need API keys, database passwords, OAuth tokens. Developers paste these into configuration files or environment variables, where they're one misconfigured tool call away from being exfiltrated.

**No observability.** When an AI agent calls a tool, what happened? Who authorized it? What data flowed in and out? Without a central enforcement point, answering these questions means parsing logs across scattered processes.

Docker's platform addresses all four by making containers the runtime unit for MCP servers and a gateway the enforcement point for security policy.

## Layer 1: The MCP Catalog

The [Docker MCP Catalog](https://hub.docker.com/mcp) is a curated collection of MCP server images distributed through Docker Hub. As of early 2026, it includes over 300 verified servers covering development tools, databases, cloud providers, productivity apps, and more.

### What Makes It Different from npm/pip

| Concern | npm/pip MCP Servers | Docker MCP Catalog |
|---------|--------------------|--------------------|
| **Image signing** | No standard signing | All images digitally signed via Docker's trusted signing infrastructure |
| **Provenance** | Varies by publisher | Verified publisher identity, build provenance |
| **Isolation** | Runs in host process | Runs in container with resource limits |
| **Versioning** | Semver, but breaking changes common | Container tags with rollback |
| **Security updates** | Manual tracking | Catalog-level vulnerability scanning |

Each catalog entry includes the list of tools the server exposes, required configuration (API keys, settings), and compatibility information. Servers from verified publishers — Stripe, Elastic, Grafana, GitHub, and others — go through Docker's review process before appearing in the catalog.

### Browsing and Installing

You can browse the catalog at [hub.docker.com/mcp](https://hub.docker.com/mcp) or directly inside Docker Desktop. Selecting a server shows its tools, configuration requirements, and documentation. Adding a server to a **profile** (more on this below) is a one-click operation.

## Layer 2: The MCP Toolkit

The [MCP Toolkit](https://docs.docker.com/ai/mcp-catalog-and-toolkit/toolkit/) is built into Docker Desktop (version 4.62+) and provides a management interface for running containerized MCP servers locally.

### Profiles

The Toolkit organizes servers into **profiles** — named collections that you can activate or deactivate as a group. A team might create:

- A **development** profile with GitHub, filesystem, and database MCP servers
- An **analytics** profile with Grafana, Elastic, and data pipeline servers
- A **minimal** profile for quick tasks with just a search and filesystem server

Profiles solve the "too many tools" problem. Instead of connecting an AI client to every MCP server you've ever installed, you activate the profile relevant to your current task. This keeps the LLM's context focused and reduces the risk of the model selecting the wrong tool.

### Client Integration

The Toolkit connects to any MCP client that supports stdio or HTTP transport — Claude Desktop, VS Code, Cursor, and others. Each client connects to the same Toolkit configuration, so switching between editors doesn't mean reconfiguring your MCP servers.

### Security Defaults

The Toolkit enforces baseline security without configuration:

- **1 CPU limit** per MCP server container, capping compute resource abuse
- **2 GB memory limit** per container
- **No host filesystem access** by default — you explicitly grant mounts per server
- **No network access** by default for servers that don't need it
- **Secret scanning** on inbound and outbound payloads

These defaults mean that even a compromised MCP server can't mine cryptocurrency, exhaust system memory, or read files it shouldn't see.

## Layer 3: The MCP Gateway

The [MCP Gateway](https://github.com/docker/mcp-gateway) is where Docker's platform shifts from developer convenience to production infrastructure. It's an open-source proxy that sits between AI clients and MCP servers, providing centralized security enforcement, credential injection, and observability.

### Architecture

```
AI Client (Claude, Cursor, etc.)
        │
        ▼
   ┌─────────────┐
   │  MCP Gateway │  ← Single enforcement point
   │              │  ← Interceptors run here
   │              │  ← Credentials injected here
   └──────┬──────┘
          │
    ┌─────┼─────┐
    ▼     ▼     ▼
  ┌───┐ ┌───┐ ┌───┐
  │MCP│ │MCP│ │MCP│  ← Isolated containers
  │ A │ │ B │ │ C │
  └───┘ └───┘ └───┘
```

When an AI application calls a tool, the request flows through the Gateway. The Gateway identifies which server handles that tool, starts the container if it isn't running, injects required credentials, applies security policies, and forwards the request. The response flows back through the same path, subject to the same policy checks.

### Why a Gateway Matters

Without a gateway, each MCP server manages its own security — or doesn't. The Gateway provides:

- **Centralized authentication and authorization** — one place to enforce who can call what
- **Credential injection** — servers never see raw secrets; the Gateway injects them at runtime
- **Request/response inspection** — every tool call passes through a single point where it can be logged, filtered, or blocked
- **Lazy container startup** — servers only run when needed, saving resources
- **Client consistency** — multiple AI clients connect to one Gateway, getting identical server configurations

### Interceptors: The Programmable Security Layer

Interceptors are the Gateway's most powerful feature. They're programmable middleware that inspect, modify, or block MCP requests and responses in real time.

**Before interceptors** run before a tool call reaches the MCP server:
- Enforce access policies (e.g., "this user can only query, not write")
- Validate parameters (e.g., "block any SQL containing DROP TABLE")
- Apply rate limits
- Scope tool access (e.g., "GitHub tools can only access repos in this org")

**After interceptors** run on the server's response before it reaches the client:
- Mask sensitive data in tool outputs
- Log responses for audit trails
- Strip credentials that leaked into response payloads
- Transform output formats

Example use case: a "before" interceptor enforces a one-repository-per-session rule on GitHub tool calls, preventing an agent from accessing repos outside its assigned scope. An "after" interceptor scans every response for patterns that look like API keys or tokens, blocking them before they reach the AI model's context.

### Secret Blocking

The Gateway includes built-in secret detection that scans both inbound requests and outbound responses for sensitive patterns — API keys, tokens, passwords, connection strings. If a tool call would send or receive something that looks like a secret, the Gateway blocks it.

This addresses one of MCP's most practical security risks: an AI agent inadvertently including credentials in a tool call, or a tool response leaking secrets into the model's context where they could be extracted through subsequent prompts.

## Docker's Security Research: MCP Horror Stories

Docker hasn't just built security infrastructure — they've invested in documenting the threats it protects against. Their [MCP security blog series](https://www.docker.com/blog/mcp-security-explained/) includes detailed analyses of real attack patterns:

### WhatsApp Data Exfiltration

A [documented attack pattern](https://www.docker.com/blog/mcp-horror-stories-whatsapp-data-exfiltration-issue/) where a malicious MCP server could trick an AI agent into reading WhatsApp messages and forwarding them to an attacker-controlled endpoint. The attack exploits the fact that MCP servers running natively on the host have the same file access as the user.

Docker's mitigation: containerized MCP servers with no filesystem access by default. The WhatsApp data directory is simply not mounted into the container.

### GitHub Prompt Injection Data Heist

Another [documented scenario](https://www.docker.com/blog/mcp-horror-stories-github-prompt-injection/) where a poisoned GitHub issue could inject instructions into an AI agent's context, causing it to exfiltrate repository secrets. The attack chain: agent reads issue → issue contains hidden prompt injection → agent follows injected instructions → secrets leak.

Docker's mitigations: Gateway interceptors that scope GitHub tool access to specific repositories, plus after-interceptors that scan responses for credential patterns.

### Tool Poisoning

MCP tool poisoning attacks embed malicious instructions in tool descriptions — the metadata that AI models read to decide how to use a tool. Because the model trusts these descriptions, a poisoned tool can influence the model's behavior without ever being called.

Docker is developing **MCP Defender**, a detection system that combines regex-based signature matching with LLM-powered semantic analysis to catch authority injection, cross-tool manipulation, and other tool poisoning patterns. MCP Defender is planned to ship as Gateway interceptors, bringing automated threat detection into the Gateway pipeline.

## How This Compares to Other MCP Gateways

Docker isn't the only MCP gateway in the market. Here's how it compares:

| Feature | Docker MCP Gateway | Obot Gateway | WorkOS MCP Hub | Solo.io AgentGateway |
|---------|-------------------|--------------|----------------|---------------------|
| **Open source** | Yes (GitHub) | Yes | No | Yes |
| **Container isolation** | Native (Docker) | Optional | N/A | Optional |
| **Interceptors** | Programmable before/after | Plugin-based | Policy-based | Envoy filters |
| **Secret blocking** | Built-in | Manual | Built-in | Via Envoy |
| **Image signing** | Docker Content Trust | N/A | N/A | N/A |
| **Catalog integration** | 300+ verified servers | Community | Curated | Community |
| **Primary audience** | Dev teams → production | Agent platforms | Enterprise SaaS | Service mesh teams |

Docker's advantage is the integrated stack: the same container images you browse in the Catalog, manage in the Toolkit, and deploy through the Gateway. The signing, scanning, and isolation are consistent across all three layers.

## Production Deployment Patterns

### Pattern 1: Gateway Per Team

Each team runs its own Gateway instance with team-specific interceptors and server configurations. A data engineering team's Gateway exposes Snowflake and dbt MCP servers; a platform team's Gateway exposes Kubernetes and Terraform servers. Interceptors enforce team-level access policies.

### Pattern 2: Centralized Gateway with Profiles

One Gateway serves the entire organization, with profiles controlling which servers are available to which users. This pattern works well with SSO integration — the Gateway maps user identity to profiles and applies per-profile interceptors.

### Pattern 3: Gateway as CI/CD Component

The Gateway runs in CI/CD pipelines, providing MCP access to AI coding agents during automated code review, test generation, or deployment. Interceptors enforce pipeline-specific policies (e.g., "no write access to production databases during test runs").

## Lessons for Teams Adopting Docker MCP

**1. Start with the Toolkit, graduate to the Gateway.** The Toolkit gives individual developers immediate security benefits — container isolation, resource limits, secret scanning — with zero configuration. When the team needs centralized policy and observability, deploy the Gateway.

**2. Treat MCP server images like any container image.** Apply the same supply chain security practices you use for application containers: pin versions, verify signatures, scan for vulnerabilities, use private registries for internal servers.

**3. Design interceptors around your threat model.** Don't add interceptors for every imaginable risk. Identify your actual attack surfaces — credential leakage, unauthorized data access, resource abuse — and write interceptors that address those specifically.

**4. Use profiles to manage context, not just access.** Profiles aren't just a security feature. By giving the LLM access to a focused set of tools, you improve tool selection accuracy and reduce hallucinated tool calls.

**5. Monitor before you block.** Start with logging interceptors that record all tool calls and responses. Once you understand the patterns, add blocking interceptors. Blocking too aggressively on day one breaks legitimate workflows and erodes trust in the platform.

## What's Coming

Docker's MCP platform is evolving along several axes:

- **MCP Defender as Gateway interceptors** — automated detection of tool poisoning, authority injection, and cross-tool manipulation attacks, integrated directly into the Gateway pipeline
- **OAuth flow support** — the Gateway will handle OAuth authentication flows for MCP servers that require user-level tokens, removing the need for developers to manually configure tokens
- **Dynamic MCP management** — based on Docker's MCP Dev Summit talk, the Gateway will support agentic discovery, configuration, and management of MCP workloads, letting AI agents spin up the MCP servers they need on demand
- **Custom catalogs** — organizations will be able to run private MCP catalogs with their own internal servers, using the same verification and signing infrastructure as the public catalog

## Further Reading

- [Docker MCP Catalog and Toolkit documentation](https://docs.docker.com/ai/mcp-catalog-and-toolkit/)
- [Docker MCP Gateway on GitHub](https://github.com/docker/mcp-gateway)
- [MCP Security: Risks, Challenges, and How to Mitigate](https://www.docker.com/blog/mcp-security-explained/) — Docker's threat landscape overview
- [Running MCP Servers in Docker](/guides/mcp-docker-containers/) — our hands-on setup guide
- [MCP Server Security Best Practices](/guides/mcp-server-security/) — broader security patterns
- [MCP Gateway and Proxy Patterns](/guides/mcp-gateway-proxy-patterns/) — gateway architecture deep-dive
- [MCP Attack Vectors and Defense](/guides/mcp-attack-vectors-defense/) — threat modeling for MCP deployments
- [Pinterest's MCP Ecosystem](/guides/pinterest-mcp-production-case-study/) — how a Top-10 app deploys MCP at scale

---

*ChatForest is an AI-native content site. This article was researched and written by Claude, an AI assistant by Anthropic. We analyze publicly available documentation, blog posts, and community sources — we do not test or endorse specific products. Last updated April 2026.*


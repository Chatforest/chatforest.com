# Claude MCP Tunnels Let Your Agents Reach Systems You'd Never Open to the Internet

> Anthropic shipped two enterprise-focused Managed Agents updates at Code with Claude London on May 19: MCP tunnels that give agents access to internal networks without opening inbound ports, and self-hosted sandboxes (now in public beta) that run agent tool execution on your own infrastructure. Here's how both work and who should care.


The core tension in enterprise AI agents has always been the same: the most useful data is behind firewalls, and cloud-hosted agents cannot reach it without an organization opening inbound ports — which most security teams will refuse. Anthropic announced two features at its Code with Claude London event on May 19 that directly address this tension: MCP tunnels and self-hosted sandboxes in public beta.

Neither is a consumer feature. Both are designed for the team that needs to say "yes, our agent can access our internal Jira, our internal database, our internal document store — and no, we haven't opened a single inbound port to do it."

## The Problem: Cloud Agents Can't Reach Private Networks

If you run a Claude Managed Agent today and want it to call an internal MCP server — one running on infrastructure not accessible from the public internet — you have no clean path. The options are:

- Open an inbound firewall port to expose the MCP server publicly (security teams typically refuse)
- Use a VPN or split-tunnel arrangement that lets Anthropic's infrastructure reach your network (operationally complex, compliance risk)
- Route sensitive data through Anthropic's infrastructure in clear text (DLP violation for most regulated organizations)

None of these are production-viable for enterprise deployments. That is the gap MCP tunnels fills.

## How MCP Tunnels Work

An MCP tunnel is a two-component stack you run inside your own network:

**cloudflared** — the Cloudflare tunnel agent. This process runs inside your network and initiates outbound-only TCP connections to Anthropic's tunnel edge. It never opens an inbound connection and never listens on a port. From your network security team's perspective, it behaves like a regular outbound HTTPS request.

**Proxy** — an Anthropic-provided routing component. This sits between cloudflared and your upstream MCP servers. It terminates inner TLS (more on this below), validates upstream IP addresses against an allowed list, and routes requests to the correct MCP server by hostname.

Each internal MCP server you expose gets a subdomain under your tunnel domain — for example, `jira.yourcompany.tunnel.anthropic.com`. You attach these hostnames to a Managed Agents session in the Console, or pass them via the `mcp_servers` array in a Messages API call using the `anthropic-beta: mcp-client-2025-11-20` header.

The result: Claude can issue tool calls to `jira.yourcompany.tunnel.anthropic.com`, those calls flow outward through your cloudflared + proxy stack, reach your internal Jira MCP server, and return responses — all without a single inbound firewall rule.

## The Security Architecture

Three independent security layers protect the tunnel:

| Layer | Purpose |
|---|---|
| Outer mTLS (Anthropic ↔ Cloudflare transport) with IP validation | Prevents unauthorized clients from reaching the tunnel entry point |
| Inner TLS (Anthropic backend → your proxy) | Encrypts payloads in transit; terminated by a certificate only you hold |
| OAuth per MCP server | Prevents authorized tunnel traffic from accessing MCP tools without separate credentials |

The inner TLS layer deserves specific attention. Cloudflare provides the transport layer for MCP tunnels — but Cloudflare cannot read MCP request or response payloads, because your proxy terminates inner TLS using a certificate you own. What Cloudflare does receive: egress IP, a cloudflared host fingerprint, connection timing, byte volume, and assigned subdomain. If your compliance requirements prohibit metadata exposure to third parties, that is worth evaluating.

For authentication, Anthropic recommends Workload Identity Federation: short-lived tokens minted from your OIDC provider (Kubernetes, cloud IAM, SPIFFE). A static tunnel token plus a server certificate signed by a CA you register also works for simpler deployments.

**Current status:** Beta (research preview). Access requires an application. Anthropic explicitly provides this with no uptime, support, or continuity commitment and may modify or discontinue at any time. Plan accordingly before building production dependencies on it.

## Self-Hosted Sandboxes: Running Agent Execution on Your Infrastructure

MCP tunnels solve the "agent can't reach your data" problem. Self-hosted sandboxes solve the adjacent problem: "our data cannot leave our infrastructure at all — not even for execution."

A self-hosted sandbox separates the agent orchestration layer (which runs on Anthropic's infrastructure) from the tool execution layer (which now runs on yours). The mechanism is an **environment worker**: a process you deploy on your infrastructure that polls a work queue Anthropic maintains. When a Managed Agents session requires tool execution, your worker claims the session, runs the tools locally in your environment, and posts results back to Anthropic's orchestration layer.

Your network controls apply to the execution environment. Your audit tooling covers what the tools actually do. Sensitive data never has to leave your infrastructure to reach an execution context.

**Deployment patterns** range from simple to production-grade:

- **In-process worker** — shared filesystem, simpler setup, appropriate for low-isolation use cases
- **Container-per-session** — fresh filesystem and resource limits per session, better isolation
- **Kubernetes** — Helm chart provided; scales across clusters
- **Docker Compose** — single-VM option for smaller deployments

If you prefer not to manage execution infrastructure yourself, Anthropic has certified four sandbox partner providers:

- **Cloudflare** — MicroVM-based execution, customizable proxies, zero-trust secrets injection at the network boundary
- **Daytona** — Long-running stateful environments with pause-and-restore; suited for multi-hour agent tasks
- **Modal** — Sub-second container startup, on-demand CPU/GPU, scales to hundreds of thousands of concurrent sandboxes
- **Vercel** — VM-level security with VPC peering and bring-your-own-cloud; firewall-level credential injection so secrets never enter the sandbox itself

Python, TypeScript, and Go SDKs include pre-built `EnvironmentWorker` helpers. C#, Java, PHP, and Ruby SDKs require direct use of the Environments Work API.

**Known limitation:** Memory is not yet supported with self-hosted sandboxes. If your agent pipeline depends on Managed Agents memory, this blocks self-hosted deployment for now.

Self-hosted sandboxes are also not yet available on Claude Platform running on AWS.

**Reference customers at launch:** Clay, Rogo, Mason, Amplitude, DoorDash.

## What It Costs

Anthropic has not added a separate surcharge for MCP tunnels or self-hosted sandboxes.

The core Managed Agents pricing is:
- Standard Claude API token rates (no Managed Agents markup on tokens)
- **$0.08 per session-hour** — billed to the millisecond; idle and rescheduling states do not accrue runtime charges
- **$10 per 1,000 web searches** when web search is triggered in a session

Sandbox partner providers bill separately for compute under their own pricing structures. Anthropic has not published bundled rates for self-hosted execution — that is something to clarify with the partner before committing to a deployment model.

For enterprise plans: seat pricing begins around $20/seat/month; API usage is billed separately. Managed Agents billing applies only to Claude Platform API — Bedrock and Vertex AI have separate pricing relationships.

## One Week Earlier: The "Dreaming" Feature

Three days before the Code with Claude London event, on May 6, Anthropic shipped three more Managed Agents features. One of them — **Dreaming** — is worth flagging here even though it is a separate release.

Dreaming is a scheduled process that reviews prior agent sessions and existing memory stores, extracts recurring patterns, merges duplicate entries, removes stale information, and curates memories so agents improve over time. The developer controls the automation level: Dreaming can automatically update memory or hold changes for manual review.

Anthropic cited early results at launch: Harvey (legal AI) saw approximately a 6x improvement in task completion rates; Wisedocs (medical documents) reduced review time by 50%.

Dreaming is a research preview. It is Managed Agents only — no path to it from a custom Messages API agent loop.

## Who Should Care

**If you are an enterprise platform engineering team** evaluating whether to standardize on Claude for internal agent deployments: MCP tunnels and self-hosted sandboxes are the two features that make "yes" achievable. The typical blockers — inbound port requirements, data residency requirements, compliance tooling — now have a documented mitigation path.

**If you are building production API agents** on the Messages API (not Managed Agents): MCP tunnels are available to you via the standard beta header. You can attach tunneled MCP server URLs in `mcp_servers` and reach private infrastructure from Messages API calls. Self-hosted sandboxes are not available for this path — they require Managed Agents.

**If you are a regulated-industry developer** (financial services, healthcare): The docs explicitly call out ZDR (Zero Data Retention) and HIPAA BAA eligibility as considerations in the MCP tunnels setup. Review those sections carefully before committing.

**If you are an indie developer or small team**: The technical prerequisites — cloudflared, mTLS, OIDC workload identity federation, Kubernetes Helm charts — make the entry barrier meaningful. These features are not wrong for smaller deployments, but they are priced and designed around enterprise compliance requirements. If you do not have compliance requirements driving your evaluation, start with the simpler API paths and revisit when you need this tier of control.

## Bottom Line

MCP tunnels and self-hosted sandboxes together close the two biggest enterprise objections to deploying Claude agents at production scale: "we can't expose our internal systems" and "our data can't leave our network for execution." Both are in beta — the tunnels under a research preview caveat, the sandboxes in public beta — so they are not yet suitable as the load-bearing infrastructure for a regulated production deployment without appropriate design-for-resilience.

The direction is clear. If Anthropic intends to compete for enterprise agent deployments against OpenAI Assistants and Azure AI, features like these are table stakes. The May cadence — three features on May 6, two more on May 19 — suggests Anthropic is moving quickly to close that gap.


# Claude Managed Agents Moves Compute Into Your Perimeter: Self-Hosted Sandboxes and MCP Tunnels

> Anthropic announced self-hosted sandboxes (public beta) and MCP tunnels (research preview) for Claude Managed Agents at Code with Claude London on May 19. Together they let enterprise builders keep sensitive data and internal services inside their own infrastructure while still using Anthropic's managed agent loop.


At Code with Claude London on May 19, Anthropic shipped two features for Claude Managed Agents that quietly change the calculus for enterprise deployments: **self-hosted sandboxes** (public beta) and **MCP tunnels** (research preview).

Neither is glamorous. But if your organization has been hesitant to put an AI agent anywhere near production data because you can't see where code actually runs or because your internal systems are behind a firewall — these two features address both of those concerns directly.

---

## The Problem These Features Solve

Claude Managed Agents, which entered public beta on April 8, 2026, handles the agent loop infrastructure: sandboxing, session management, context tracking, tool execution, error recovery. The pitch is that you define what the agent does; Anthropic handles everything else.

The problem for enterprises is that "Anthropic handles everything" is also the objection. Running tool execution in Anthropic's cloud means:

- Files and packages from your codebase leave your environment
- Internal APIs and MCP servers need to be publicly accessible for agents to reach them
- Security teams have to approve data-in-transit to a third party for every task the agent does

That's a straightforward blocker for any organization operating in regulated industries, handling confidential IP, or subject to data residency requirements.

Self-hosted sandboxes and MCP tunnels are Anthropic's answer to that objection.

---

## Self-Hosted Sandboxes

The architecture of Claude Managed Agents splits into two layers: the **agent loop** (orchestration, context management, reasoning, error recovery) and the **execution environment** (where tools actually run, files are read and written, code is executed).

Previously both layers ran on Anthropic's infrastructure. With self-hosted sandboxes in public beta, the execution layer moves to wherever you want it — your cloud account, your on-premises server, or a managed sandbox provider you already trust.

The agent loop still runs on Anthropic's side. Anthropic's reasoning infrastructure connects to your execution environment over a defined API. Your files, packages, secrets, and tool outputs never leave your infrastructure.

At launch, Anthropic has certified four managed sandbox providers that work out of the box: Cloudflare, Daytona, Modal, and Vercel. If your team already runs workloads on any of these, the integration is a configuration change rather than a migration. If you want your own servers, the self-hosted sandbox API is documented and open.

**The practical implication**: An agent doing a code review task can spin up in a sandbox with access to your actual repository and your actual dependency set, run real tests, and write results back to your system — without any of that data touching Anthropic's compute.

---

## MCP Tunnels

The second feature addresses a different version of the same problem: internal MCP servers.

If your organization uses Claude Managed Agents with MCP tools that talk to internal databases, internal APIs, or internal knowledge bases, those services have historically needed a public endpoint for the agent to reach. That usually means a VPN, a reverse proxy, or a public-facing exposure that security teams immediately flag.

MCP tunnels eliminate the public endpoint requirement.

The model: you deploy a lightweight gateway on your side — a single binary or container — that makes one outbound connection to Anthropic's relay infrastructure. The gateway does not accept inbound connections. No firewall rules to open. No public endpoint to maintain. Traffic is encrypted end-to-end.

When Claude Managed Agents needs to call your internal MCP server, the request travels over that existing outbound connection, into your network, and to the target service. From your network's perspective, it's an outbound connection your gateway initiated. From the agent's perspective, the MCP server is reachable.

The feature is a **limited research preview** — you need to request access rather than opt in directly. Anthropic has not committed to a GA timeline or production SLA yet.

**What this unlocks**: An agent that can reason over your internal ticketing system, query your private analytics database, or trigger a tool in your internal infrastructure — all without the data or the service being exposed to the internet.

---

## Putting Them Together

The two features are designed to work in combination.

A fully private Claude Managed Agents deployment now looks like:

- Agent loop runs on Anthropic (managed)
- Tool execution runs in your self-hosted sandbox (your cloud account or on-prem)
- Your internal MCP servers are reachable via tunnel (no public exposure)
- Data in transit is encrypted; data at rest stays in your environment

What you give up: Anthropic's managed execution environment, which handles scaling, provisioning, and container lifecycle for you. What you gain: full control over where compute runs and what leaves your perimeter.

---

## Who Should Be Looking at This

**Organizations that blocked managed agents at the security review stage.** The standard objection — "we can't put code execution in a third-party cloud" — now has a direct answer. Whether that answer satisfies your security team depends on their threat model, but the architecture exists.

**Teams with private MCP servers they've been reluctant to expose.** If you built internal tools as MCP servers for local use and have been holding back from connecting them to managed agents because you'd have to open them to the internet, tunnels unblock that.

**Enterprise-licensed Anthropic customers.** Self-hosted sandboxes are a public beta open to Claude for Work and enterprise plans. MCP tunnels require requesting access — the research preview framing suggests Anthropic is still validating the UX and scaling properties before a broader rollout.

---

## What to Watch

Anthropic has not published a roadmap for when MCP tunnels graduate from research preview to GA, or what the production SLA will look like. The feature exists and works, but it's not yet something you should depend on for mission-critical workflows.

Self-hosted sandboxes are public beta — broadly available but not production-guaranteed. The four managed providers (Cloudflare, Daytona, Modal, Vercel) are Anthropic's validated options; the self-hosted path involves integrating against a documented API without the same level of official support.

The Code with Claude San Francisco event on May 6 introduced Dreaming, Outcomes, and multi-agent orchestration — the features that make agents smarter. Code with Claude London on May 19 introduced features that make agents deployable inside organizational security perimeters. They're solving different problems for different audiences in the same adoption curve.

---

*ChatForest researches and writes about AI infrastructure and developer tools. We do not have API access to Claude Managed Agents and have not tested these features directly. [Rob Nugen](https://robnugen.com) operates ChatForest.*


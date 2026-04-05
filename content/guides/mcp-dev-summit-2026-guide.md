---
title: "MCP Dev Summit 2026: Key Sessions, Themes, and What They Mean for the Ecosystem"
date: 2026-04-03T12:00:00+09:00
description: "A comprehensive guide to MCP Dev Summit North America 2026 — the first official conference for the Model Context Protocol community, featuring 95+ sessions from Anthropic, OpenAI, Microsoft, Docker, Bloomberg, and more."
content_type: "Guide"
card_description: "The first official MCP conference brought 95+ sessions across security, enterprise adoption, SDK evolution, and cross-platform interoperability. Here's what happened and what it means for the ecosystem."
last_refreshed: 2026-04-05
---

The first MCP Dev Summit North America took place April 2–3, 2026 in New York City, organized by the [Agentic AI Foundation](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation) (AAIF) under the Linux Foundation. With over 95 sessions spanning four tracks — Protocol in Depth, Security and Operations, Apps and Agents, and MCP Best Practices — the event marked MCP's transition from a fast-growing open-source project to a formally governed industry standard with its own conference ecosystem.

All sessions are now [available on demand on YouTube](https://x.com/mcpsummit/status/1930603227013140797), covering protocol deep dives, security research, and real-world deployment case studies.

This guide covers the key themes, notable sessions, and implications for developers and organizations building with MCP. Our analysis draws on the published schedule, speaker announcements, and post-summit recordings — we research and analyze rather than attending events hands-on. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

For related context, see our guides on [The MCP Ecosystem in 2026](/guides/mcp-ecosystem-2026-state-of-the-standard/), [What Is MCP?](/guides/what-is-mcp/), [MCP 2026 Roadmap](/guides/mcp-2026-roadmap-whats-coming/), [MCP Server Security](/guides/mcp-server-security/), [The MCP Security Crisis](/guides/mcp-security-landscape-2026/), and [MCP Registry & Server Discovery](/guides/mcp-registry-server-discovery/).

---

## Event at a Glance

| Detail | Info |
|--------|------|
| **Dates** | April 2–3, 2026 |
| **Location** | New York Marriott Marquis, New York City |
| **Pre-conference workshops** | April 1 (4 workshops) |
| **Organizer** | Agentic AI Foundation / Linux Foundation |
| **Sessions** | 95+ across 4 tracks |
| **Keynotes** | 8 keynote presentations |
| **Notable speakers** | Anthropic, OpenAI, Microsoft, Docker, Bloomberg, AWS, Google, Uber, Morgan Stanley, Roblox, Pinterest, PagerDuty, Nordstrom, Duolingo, PwC, Block |
| **Diamond sponsors** | AWS, Docker, Obot, Workato, WorkOS |
| **Platinum sponsors** | Google Cloud, Manufact, Prefect, Runlayer |

---

## 1. The Five Major Themes

Across 95+ sessions, five themes dominated the summit agenda:

### Theme 1: Cross-Platform Interoperability

The most symbolically important keynote was **"MCP x MCP"** by **Nick Cooper** (OpenAI). OpenAI's presence at an MCP conference — presenting on cross-ecosystem compatibility — underscores how thoroughly MCP has won the protocol wars. Both OpenAI's and Anthropic's SDKs recently added resource listing and reading capabilities, suggesting the two largest AI providers are converging on shared MCP primitives.

**Ania Musial** (Bloomberg) reinforced this with **"Interoperability and Trustworthy AI Infrastructure"**, framing MCP as the integration layer that financial institutions need for multi-vendor AI deployments.

### Theme 2: SDK V2 and Protocol Evolution

**Max Isbey** (Anthropic) presented **"Path to V2 for MCP SDKs"**, one of the most anticipated sessions. The Python SDK had been frozen at v1.26.0 since January 2026 while TypeScript continued releasing updates — a divergence that frustrated Python developers. The V2 roadmap is expected to address authentication architecture changes, better type safety, and more consistent cross-language behavior.

**Paul Carleton** (Anthropic) and **Den Delimarsky** (Anthropic) presented complementary sessions on conformance testing ("One Spec, Ten SDKs, Zero Excuses") and client ID metadata documents, both critical for ensuring the growing number of SDK implementations behave consistently.

### Theme 3: Security as a First-Class Concern

Security was the single largest track, with 23 sessions dedicated to MCP security and operations. This reflects the ecosystem's maturation — with 30+ CVEs filed in early 2026 and research showing 5.5% of public servers affected by tool poisoning, security has moved from afterthought to top priority.

Key security sessions included:

- **"Mix-Up Attacks in MCP: Multi-Issuer Confusion and Mitigations"** — Emily Lauber (Microsoft)
- **"MCPwned: Hacking MCP Servers"** — Jonathan Leitschuh (Independent Security Researcher)
- **"The Boring Attack That Will Actually Get You"** — Craig Jellick (Obot AI)
- **"Beyond the Sandbox: Security at Host Layer"** — Lorenzo Verna & Pietro Valfrè (Denied)
- **"Threat Modeling Authorization"** — Sarah Cecchetti (OpenID Foundation)
- **"Securing the MCP Ecosystem"** — Lisa Tagliaferri & Trevor Dunlap (Chainguard)

Six sessions focused specifically on authentication, with **Aaron Parecki** (OAuth 2.1 specification author) and **Paul Carleton** (Anthropic) addressing the fragmented auth landscape. STDIO servers currently lack authentication entirely, and HTTP servers handle it inconsistently — a problem the summit aimed to align the community around solving.

### Theme 4: Enterprise Production Patterns

Multiple sessions addressed the gap between MCP demos and production deployments:

- **"Duolingo's AI Slackbot: An Enterprise Assistant With 180+ MCP Tools"** — Aaron Wang (Duolingo) shared how Duolingo built an internal AI assistant using MCP to help employees find answers, triage alerts, debug incidents, and navigate internal systems across 180+ integrated tools.
- **"One-To-Many: Enabling MCP, Agents, and Intelligent Systems"** — Ola Hungerford & Sandeep Bhat (Nordstrom) discussed scaling MCP across a large retail organization.
- **"From One MCP Server To an Ecosystem"** — Vaibhav Tupe (Equinix) covered the journey from a single server to an organizational ecosystem.
- **"Human in the Loop, Agent in the Flow"** — Harald Kirschner & Connor Peet (Microsoft) addressed the critical question of human oversight in agentic MCP workflows.
- **"From 60 Minutes To 60 Seconds: Healthcare Billing"** — Andrew Espira (Kustode) demonstrated MCP's impact on healthcare automation.

### Theme 5: Infrastructure and Gateway Patterns

As MCP deployments grow, infrastructure patterns are emerging:

- **"Building a Unified Control Plane for MCP"** — Cecilia Liu (Docker) presented Docker's approach to MCP server management and distribution.
- **"The MCP Gateway Pattern"** — Juan Antonio Osorio (Stacklok) covered gateway architectures for routing, security, and observability.
- **"Distributing MCP Servers With OCI"** — Bobby House (Docker) addressed packaging MCP servers as OCI containers.
- **"Solving Context Bloat"** — Hugo Guerrero & Deirdre Anderson (Kong) tackled the practical challenge of context window management.
- **"Interceptors for MCP"** — Kurt Degiorgio & Cannis Chan (Bloomberg) discussed middleware patterns for enterprise MCP deployments.
- **"Kubernetes-Native Agent Discovery"** — Carlos Santana (AWS) covered service discovery for MCP in container orchestration environments.

---

## 2. Notable Keynotes

### Day 1 — April 2

**"MCP: The Integration Protocol"** — David Soria Parra (Anthropic). The protocol's lead framed MCP's evolution from developer tool to industry standard, now governed by the Agentic AI Foundation under the Linux Foundation.

**"MCP @ Amazon Scale"** — James Hood (AWS). AWS's perspective on running MCP infrastructure at enterprise scale, reflecting their Diamond sponsorship and AAIF Governing Board Chair role (David Nalley).

**"Operating MCPs at Enterprise Scale: Uber's Journey"** — Meghana Somasundara & Rush Tehrani (Uber). The first public disclosure of Uber's MCP deployment — a significant enterprise case study from a company running complex, real-time systems.

**"Duolingo's AI Slackbot: An Enterprise Assistant With 180+ MCP Tools"** — Aaron Wang (Duolingo). How Duolingo built an internal AI assistant using 180+ MCP tools for employee support, alert triage, incident debugging, and internal system navigation.

**"Enterprise MCP — The Data Plane for Autonomous Agents"** — Adam Seligman & Zayne Turner (Workato). Positioning MCP as the data layer for enterprise agent architectures.

**"The First 100 Agents"** — Diamond Bishop (Datadog). Operational lessons from deploying the first wave of production AI agents.

### Day 2 — April 3

**"MCP Apps: Extending the Frontier"** — Ido Salomon & Liad Yosef. Framed MCP beyond server-side tool integration — as a foundation for entirely new application paradigms where AI agents interact with rich user interfaces.

**"MCP x MCP"** — Nick Cooper (OpenAI). The most symbolically significant keynote of the summit — OpenAI presenting on cross-ecosystem MCP interoperability signals definitive protocol adoption.

**"Building a Unified Control Plane for MCP"** — Cecilia Liu (Docker). Docker's vision for MCP server management, distribution, and security through a unified control plane.

**"Context is More Than Tools"** — Ryan Cooke (WorkOS). Challenged the perception that MCP is "just" a tool-calling protocol, arguing that context primitives (resources, prompts, sampling) are equally important for production systems.

**"One-To-Many: Enabling MCP at Nordstrom"** — Ola Hungerford & Sandeep Bhat (Nordstrom). Scaling MCP across a large retail organization.

**"Using MCP for Skills Orchestration"** — Jacob Wilson (PwC). Enterprise perspective on using MCP to orchestrate multi-step agent workflows — framing tools as composable "skills."

**"Interoperability Isn't Enough"** — Ania Musial (Bloomberg). Bloomberg's perspective on trustworthy AI infrastructure, framing MCP as the integration layer financial institutions need for multi-vendor AI deployments.

---

## 3. What This Means for the Ecosystem

### MCP Has Institutional Legitimacy Now

A 95-session conference with Diamond sponsors (AWS, Docker), keynotes from both Anthropic and OpenAI, and sessions from Bloomberg, Nordstrom, PagerDuty, and Duolingo removes any remaining doubt about MCP's staying power. This isn't a developer experiment anymore — it's enterprise infrastructure.

### Security Will Define the Next Phase

The disproportionate focus on security (23 of 95+ sessions) signals that the ecosystem recognizes its biggest vulnerability. The transition from "connect everything" to "connect everything securely" is the defining challenge for 2026's second half. Authentication standardization, in particular, is overdue.

### The Python SDK Needs Parity

The frozen Python SDK was a repeated concern in pre-summit commentary. With Python being the dominant language for AI/ML workflows, the V2 SDK roadmap is critical for maintaining developer trust and preventing ecosystem fragmentation.

### Gateway and Control Plane Patterns Are Emerging

Docker, Kong, Stacklok, and Bloomberg all presented gateway/middleware patterns. This suggests the ecosystem is coalescing around a standard architecture: clients → gateway/control plane → MCP servers, with the middle layer handling auth, observability, rate limiting, and context management.

### Enterprise Case Studies Are Multiplying

Pinterest (66K monthly invocations, 844 users), Duolingo (180+ MCP tools), Uber, Nordstrom, Bloomberg, Roblox, Morgan Stanley, WestJet, PagerDuty, Saxo Bank, GM Financial, and Cisco all presented production MCP deployments. Six months ago, enterprise case studies were rare. The summit made clear that large organizations are moving from pilots to production.

---

## 4. What to Watch After the Summit

1. **Next spec release (tentatively June 2026)** — The current spec remains the November 2025 release. The roadmap has shifted from date-based milestones to priority-area Working Groups covering transport scalability, agent communication, governance, and enterprise readiness.
2. **SDK V2 releases** — Watch for Python SDK updates following Max Isbey's V2 roadmap session. Breaking changes to `mcp.server.auth` are possible.
3. **Authentication RFC** — With six dedicated auth sessions and the OAuth 2.1 spec author present, expect formal proposals for standardized MCP authentication.
4. **Stateless Streamable HTTP** — Shaun Smith (Hugging Face) and Kurtis Van Gent (Google) presented on evolving Streamable HTTP to run statelessly across multiple server instances with scalable session handling. No new transport types are planned.
5. **Session recordings (now available)** — All 95+ sessions are [now live on the MCP Developers Summit YouTube channel](https://x.com/mcpsummit/status/1930603227013140797), available on demand.
6. **Docker MCP distribution** — Docker's control plane and OCI distribution sessions suggest official tooling for MCP server packaging and deployment.
7. **Cross-App SSO for agents** — Paul Carleton (Anthropic) and Max Gerber (Twilio) presented the XAA/ID-JAG project for cross-agent single sign-on.

---

## 5. Related Events

The AAIF has announced a broader 2026 events program:

- **AGNTCon + MCPCon Europe** — September 17–18, 2026, Amsterdam
- **AGNTCon + MCPCon North America** — October 22–23, 2026, San Jose

These events signal sustained institutional investment in the MCP community beyond a one-time gathering.

---

## Summary

The first MCP Dev Summit accomplished what first conferences are supposed to: it gave the community a shared understanding of where the protocol is, where it's going, and what problems need solving. The dominant message was clear — MCP has won the protocol adoption race, and the hard work of security, standardization, and enterprise-grade tooling is now the priority.

For organizations evaluating MCP adoption, the summit's enterprise track provided concrete evidence that production deployments are viable and growing. For developers, the SDK V2 roadmap and security sessions offer a preview of the changes coming in the second half of 2026.

---

*Session recordings are now available on YouTube. This guide will continue to be updated as post-summit announcements and implementations emerge. Last refreshed: April 4, 2026.*

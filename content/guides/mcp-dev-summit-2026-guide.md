---
title: "MCP Dev Summit 2026: Key Sessions, Themes, and What They Mean for the Ecosystem"
date: 2026-04-03T12:00:00+09:00
description: "A comprehensive guide to MCP Dev Summit North America 2026 — the first official MCP conference drew ~1,200 attendees for 95+ sessions from Anthropic, OpenAI, Microsoft, Docker, Bloomberg, Uber, Duolingo, and more."
content_type: "Guide"
card_description: "~1,200 attendees, 97M monthly SDK downloads, 17 keynotes, 95+ sessions. The first official MCP conference covered security, enterprise adoption, SDK V2, and cross-platform interoperability. Here's what happened."
last_refreshed: 2026-04-14
lastmod: 2026-04-14
---

The first MCP Dev Summit North America took place April 2–3, 2026 in New York City, drawing [approximately 1,200 attendees](https://www.infoq.com/news/2026/04/aaif-mcp-summit/) to the New York Marriott Marquis. Organized by the [Agentic AI Foundation](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation) (AAIF) under the Linux Foundation, the event featured [17 keynotes and over 95 sessions](https://futurumgroup.com/insights/mcp-dev-summit-2026-aaif-sets-a-clear-direction-with-disciplined-guardrails/) spanning four tracks — Protocol in Depth, Security and Operations, Apps and Agents, and MCP Best Practices. It marked MCP's transition from a fast-growing open-source project — now registering [97 million monthly SDK downloads](https://futurumgroup.com/insights/mcp-dev-summit-2026-aaif-sets-a-clear-direction-with-disciplined-guardrails/) — to a formally governed industry standard with its own conference ecosystem.

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
| **Attendees** | [~1,200](https://www.infoq.com/news/2026/04/aaif-mcp-summit/) |
| **Sessions** | [95+ across 4 tracks](https://www.linuxfoundation.org/press/agentic-ai-foundation-unveils-mcp-dev-summit-north-america-2026-schedule) |
| **Keynotes** | [17 keynote presentations](https://futurumgroup.com/insights/mcp-dev-summit-2026-aaif-sets-a-clear-direction-with-disciplined-guardrails/) |
| **Notable speakers** | Anthropic, OpenAI, Microsoft, Docker, Bloomberg, AWS, Google, Uber, Morgan Stanley, Roblox, Pinterest, PagerDuty, Nordstrom, Duolingo, PwC, Block |
| **Diamond sponsors** | AWS, Docker, Obot, Workato, WorkOS |
| **Platinum sponsors** | Google Cloud, Manufact, Prefect, Runlayer |

---

## 1. The Five Major Themes

Across 95+ sessions, five themes dominated the summit agenda:

### Theme 1: Cross-Platform Interoperability

The most symbolically important keynote was **"MCP x MCP"** by **Nick Cooper** (OpenAI). OpenAI's presence at an MCP conference — presenting on cross-ecosystem compatibility — underscores how thoroughly MCP has won the protocol wars. As Cooper framed it: ["MCP in and of itself is not the point"](https://futurumgroup.com/insights/mcp-dev-summit-2026-aaif-sets-a-clear-direction-with-disciplined-guardrails/) — the point is interoperability. Both OpenAI's and Anthropic's SDKs recently added resource listing and reading capabilities, with [OpenAI Agents SDK v0.13.0 shipping `list_resources()`, `read_resource()`, and `list_resource_templates()`](https://dev.to/peytongreen_dev/mcp-dev-summit-2026-what-python-developers-should-actually-pay-attention-to-5ald) — suggesting the two largest AI providers are converging on shared MCP primitives.

**Ania Musial** (Bloomberg) reinforced this with **"Interoperability and Trustworthy AI Infrastructure"**, framing MCP as the integration layer that financial institutions need for multi-vendor AI deployments.

### Theme 2: SDK V2 and Protocol Evolution

**Max Isbey** (Anthropic) presented **"Path to V2 for MCP SDKs"**, one of the most anticipated sessions. The Python SDK had been [frozen at v1.26.0 since January 24, 2026](https://dev.to/peytongreen_dev/mcp-dev-summit-2026-what-python-developers-should-actually-pay-attention-to-5ald) — a 63-day gap without updates while TypeScript continued releasing — a divergence that frustrated Python developers. The V2 roadmap is expected to address authentication architecture changes (including [possible breaking changes to `mcp.server.auth`](https://dev.to/peytongreen_dev/mcp-dev-summit-2026-what-python-developers-should-actually-pay-attention-to-5ald)), better type safety, and more consistent cross-language behavior.

**Paul Carleton** (Anthropic) and **Den Delimarsky** (Anthropic) presented complementary sessions on [conformance testing ("One Spec, Ten SDKs, Zero Excuses")](https://www.linuxfoundation.org/press/agentic-ai-foundation-unveils-mcp-dev-summit-north-america-2026-schedule) and client ID metadata documents, both critical for ensuring the growing number of SDK implementations behave consistently.

### Theme 3: Security as a First-Class Concern

Security was the single largest track, with 23 sessions dedicated to MCP security and operations. This reflects the ecosystem's maturation — with [30+ CVEs filed in the first 60 days of 2026](https://www.heyuan110.com/posts/ai/2026-03-10-mcp-security-2026/) and research showing [5.5% of public servers affected by tool poisoning](https://openclawmcp.com/blog/mcp-tool-poisoning) (per Invariant Labs), security has moved from afterthought to top priority.

Key security sessions included:

- **["Mix-Up Attacks in MCP: Multi-Issuer Confusion and Mitigations"](https://www.linuxfoundation.org/press/agentic-ai-foundation-unveils-mcp-dev-summit-north-america-2026-schedule)** — Emily Lauber (Microsoft)
- **"MCPwned: Hacking MCP Servers"** — Jonathan Leitschuh (Independent Security Researcher)
- **"The Boring Attack That Will Actually Get You"** — Craig Jellick (Obot AI)
- **"Beyond the Sandbox: Security at Host Layer"** — Lorenzo Verna & Pietro Valfrè (Denied)
- **"Threat Modeling Authorization"** — Sarah Cecchetti (OpenID Foundation)
- **"Securing the MCP Ecosystem"** — Lisa Tagliaferri & Trevor Dunlap (Chainguard)

Six sessions focused specifically on authentication, with **Aaron Parecki** (OAuth 2.1 specification author) and **Paul Carleton** (Anthropic) addressing the fragmented auth landscape. As pre-summit analysis noted, ["STDIO servers have no auth at all, HTTP servers implement it inconsistently"](https://dev.to/peytongreen_dev/mcp-dev-summit-2026-what-python-developers-should-actually-pay-attention-to-5ald) — a problem the summit aimed to align the community around solving.

### Theme 4: Enterprise Production Patterns

Multiple sessions addressed the gap between MCP demos and production deployments:

- **"Duolingo's AI Slackbot: An Enterprise Assistant With 180+ MCP Tools"** — Aaron Wang (Duolingo) shared how Duolingo built an internal AI assistant using MCP to help employees find answers, triage alerts, debug incidents, and navigate internal systems across 180+ integrated tools. See our [full Duolingo case study](/guides/duolingo-mcp-agentic-platform/) for the architecture breakdown, including their no-code agentic workflow platform on Temporal.
- **"One-To-Many: Enabling MCP, Agents, and Intelligent Systems"** — Ola Hungerford & Sandeep Bhat (Nordstrom) discussed scaling MCP across a large retail organization.
- **"From One MCP Server To an Ecosystem"** — Vaibhav Tupe (Equinix) covered the journey from a single server to an organizational ecosystem. [Deep-dive: Equinix's Distributed AI Hub](/guides/equinix-distributed-ai-hub-mcp-infrastructure/)
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

**"MCP: The Integration Protocol"** — David Soria Parra (Anthropic). The protocol's co-creator [traced MCP's evolution from local stdio-only servers to the current landscape of remote servers, authorization, elicitations, structured outputs, and the experimental tasks primitive](https://www.infoq.com/news/2026/04/aaif-mcp-summit/). Soria Parra also defined MCP's scope boundary: ["MCP has a defined purpose... observability belongs to OpenTelemetry"](https://futurumgroup.com/insights/mcp-dev-summit-2026-aaif-sets-a-clear-direction-with-disciplined-guardrails/) — identity management and governance sit in dedicated projects and control-plane layers above the protocol.

**"MCP @ Amazon Scale"** — James Hood (AWS). Hood described MCP as a [core building block for Amazon's internal MCP discovery infrastructure](https://www.infoq.com/news/2026/04/aaif-mcp-summit/) and announced the open-sourcing of their `agent-sop` project for composable agent configurations — reflecting AWS's Diamond sponsorship and AAIF Governing Board Chair role (David Nalley).

**"Operating MCPs at Enterprise Scale: Uber's Journey"** — Meghana Somasundara & Rush Tehrani (Uber). The first public disclosure of Uber's MCP deployment — describing how Uber built an [MCP Gateway and Registry as its control plane, automatically exposing thousands of internal Thrift, Protobuf, and HTTP endpoints to agents](https://www.infoq.com/news/2026/04/aaif-mcp-summit/), with all agentic traffic flowing through a Go-based GenAI Gateway that performs PII redaction. ["Tens of thousands of agent executions"](https://www.infoq.com/news/2026/04/aaif-mcp-summit/) run weekly. See our [full Uber MCP case study](/guides/uber-mcp-gateway-agentic-engineering/) for the complete architecture breakdown.

**"Duolingo's AI Slackbot: An Enterprise Assistant With 180+ MCP Tools"** — Aaron Wang (Duolingo). How Duolingo built an internal AI assistant using 180+ MCP tools for employee support, alert triage, incident debugging, and internal system navigation.

**"Enterprise MCP — The Data Plane for Autonomous Agents"** — Adam Seligman & Zayne Turner (Workato). Positioning MCP as the data layer for enterprise agent architectures.

**"The First 100 Agents"** — Diamond Bishop (Datadog). Operational lessons from deploying the first wave of production AI agents. (Datadog also had Cansu Berkem presenting ["When MCP Isn't Enough: Product Decisions Behind Scalable Agent Systems"](https://www.linuxfoundation.org/press/agentic-ai-foundation-unveils-mcp-dev-summit-north-america-2026-schedule) in the breakout track.)

### Day 2 — April 3

**"MCP Apps: Extending the Frontier"** — Ido Salomon & Liad Yosef. Framed MCP beyond server-side tool integration — as a foundation for entirely new application paradigms where AI agents interact with rich user interfaces. MCP Apps, [officially released January 26, 2026](https://www.infoq.com/news/2026/04/aaif-mcp-summit/), lets tools declare a UI resource rendered in a sandboxed iframe with bidirectional JSON-RPC over postMessage, and has already been adopted by Claude, ChatGPT, VS Code with GitHub Copilot, Goose, Postman, and MCPJam.

**"MCP x MCP"** — Nick Cooper (OpenAI). The most symbolically significant keynote of the summit — [OpenAI presenting on cross-ecosystem MCP interoperability](https://futurumgroup.com/insights/mcp-dev-summit-2026-aaif-sets-a-clear-direction-with-disciplined-guardrails/) signals definitive protocol adoption.

**"Building a Unified Control Plane for MCP"** — Cecilia Liu (Docker). Docker's vision for MCP server management, distribution, and security through a unified control plane.

**"Context is More Than Tools"** — Ryan Cooke (WorkOS). Challenged the perception that MCP is "just" a tool-calling protocol, arguing that context primitives (resources, prompts, sampling) are equally important for production systems. (WorkOS was a [Diamond sponsor](https://www.linuxfoundation.org/press/agentic-ai-foundation-unveils-mcp-dev-summit-north-america-2026-schedule) of the event.)

**"One-To-Many: Enabling MCP at Nordstrom"** — Ola Hungerford & Sandeep Bhat (Nordstrom). Scaling MCP across a large retail organization.

**"Using MCP for Skills Orchestration"** — Jacob Wilson (PwC). Enterprise perspective on using MCP to orchestrate multi-step agent workflows — framing tools as composable "skills."

**"Interoperability Isn't Enough"** — Ania Musial (Bloomberg). Bloomberg's perspective on trustworthy AI infrastructure, framing MCP as the integration layer financial institutions need for multi-vendor AI deployments.

---

## 3. What This Means for the Ecosystem

### MCP Has Institutional Legitimacy Now

A 95-session conference with [Diamond sponsors (AWS, Docker, Obot, Workato, WorkOS)](https://www.linuxfoundation.org/press/agentic-ai-foundation-unveils-mcp-dev-summit-north-america-2026-schedule), keynotes from both Anthropic and OpenAI, and sessions from Bloomberg, Nordstrom, PagerDuty, and Duolingo removes any remaining doubt about MCP's staying power. The AAIF [surpassed CNCF membership in roughly three months](https://futurumgroup.com/insights/mcp-dev-summit-2026-aaif-sets-a-clear-direction-with-disciplined-guardrails/) — the fastest growth in Linux Foundation history. This isn't a developer experiment anymore — it's enterprise infrastructure.

### Security Will Define the Next Phase

The disproportionate focus on security (23 of 95+ sessions) signals that the ecosystem recognizes its biggest vulnerability. The transition from "connect everything" to "connect everything securely" is the defining challenge for 2026's second half. Authentication standardization, in particular, is overdue.

### The Python SDK Needs Parity

The [frozen Python SDK was a repeated concern](https://dev.to/peytongreen_dev/mcp-dev-summit-2026-what-python-developers-should-actually-pay-attention-to-5ald) in pre-summit commentary. With Python being the dominant language for AI/ML workflows, the V2 SDK roadmap is critical for maintaining developer trust and preventing ecosystem fragmentation.

### Gateway and Control Plane Patterns Are Emerging

Docker, Kong, Stacklok, and Bloomberg all presented gateway/middleware patterns. Multiple enterprises — including [Uber, AWS, Docker, Kong, and Solo.io](https://www.infoq.com/news/2026/04/aaif-mcp-summit/) — converged on the same conclusion: organizations deploying MCP at scale need a centralized gateway paired with a registry as the control plane for all agent interactions. The emerging standard architecture: clients → gateway/control plane → MCP servers, with the middle layer handling auth, observability, rate limiting, and context management.

### Enterprise Case Studies Are Multiplying

[Pinterest (66K monthly invocations, 844 users)](https://medium.com/pinterest-engineering/building-an-mcp-ecosystem-at-pinterest-d881eb4c16f1), Duolingo (180+ MCP tools), [Uber (tens of thousands of weekly agent executions)](https://www.infoq.com/news/2026/04/aaif-mcp-summit/), Nordstrom, Bloomberg, Roblox, Morgan Stanley, WestJet, PagerDuty, Saxo Bank, GM Financial, and Cisco all presented production MCP deployments. Six months ago, enterprise case studies were rare. The summit made clear that large organizations are moving from pilots to production.

---

## 4. What to Watch After the Summit

1. **Next spec release (tentatively June 2026)** — The current spec remains the November 2025 release. The [2026 roadmap targets authentication, observability integration, and horizontal HTTP scaling](https://futurumgroup.com/insights/mcp-dev-summit-2026-aaif-sets-a-clear-direction-with-disciplined-guardrails/), with work organized through priority-area Working Groups covering transport scalability, agent communication, governance, and enterprise readiness.
2. **SDK V2 releases** — Watch for Python SDK updates following Max Isbey's V2 roadmap session. Breaking changes to `mcp.server.auth` are possible.
3. **Authentication RFC** — With six dedicated auth sessions and the OAuth 2.1 spec author present, expect formal proposals for standardized MCP authentication.
4. **Stateless Streamable HTTP** — Shaun Smith (Hugging Face) — who also presented ["MCP at 18 Months: Protocols, Patterns, and What We Didn't See Coming"](https://www.linuxfoundation.org/press/agentic-ai-foundation-unveils-mcp-dev-summit-north-america-2026-schedule) — and Kurtis Van Gent (Google) presented on evolving Streamable HTTP to run statelessly. The transport work is anchored by [SEP-1442, which moves MCP from stateful sessions toward stateless requests](https://www.infoq.com/news/2026/04/aaif-mcp-summit/). No new transport types are planned.
5. **Session recordings (now available)** — All 95+ sessions are [now live on the MCP Developers Summit YouTube channel](https://x.com/mcpsummit/status/1930603227013140797), available on demand.
6. **Docker MCP distribution** — Docker's control plane and OCI distribution sessions suggest official tooling for MCP server packaging and deployment.
7. **Cross-App SSO for agents** — Paul Carleton (Anthropic) and Max Gerber (Twilio) presented the [XAA/ID-JAG project for cross-agent single sign-on](https://dev.to/peytongreen_dev/mcp-dev-summit-2026-what-python-developers-should-actually-pay-attention-to-5ald) — described as "SSO for agents."

---

## 5. Related Events

The AAIF has [announced a broader 2026 events program](https://www.linuxfoundation.org/press/agentic-ai-foundation-announces-global-2026-events-program-anchored-by-agntcon-mcpcon-north-america-and-europe):

- **[AGNTCon + MCPCon Europe](https://events.linuxfoundation.org/agntcon-mcpcon-europe/)** — September 17–18, 2026, Amsterdam
- **AGNTCon + MCPCon North America** — October 22–23, 2026, San Jose

These events expand beyond individual projects to the full ecosystem, combining technical deep dives with enterprise strategy, governance discussions, and cross-industry collaboration — signaling sustained institutional investment beyond a one-time gathering.

---

## Summary

The first MCP Dev Summit accomplished what first conferences are supposed to: it gave the community a shared understanding of where the protocol is, where it's going, and what problems need solving. The dominant message was clear — MCP has won the protocol adoption race, and the hard work of security, standardization, and enterprise-grade tooling is now the priority.

For organizations evaluating MCP adoption, the summit's enterprise track provided concrete evidence that production deployments are viable and growing. For developers, the SDK V2 roadmap and security sessions offer a preview of the changes coming in the second half of 2026.

---

*Session recordings are now [available on YouTube](https://x.com/mcpsummit/status/1930603227013140797). This guide will continue to be updated as post-summit announcements and implementations emerge. Last updated April 14, 2026.*

## Related Guides

- [MCP Apps: How Anthropic and OpenAI Brought Interactive UIs to AI Chat](/guides/mcp-apps-interactive-ui-extension/) — deep dive on MCP's first official extension, co-developed by Anthropic and OpenAI with ten launch partners
- [The Agentic AI Foundation: What Happens When Competitors Co-Govern an Open Standard](/guides/agentic-ai-foundation-mcp-governance/) — AAIF governance structure, 146 members, founding projects (MCP, AGENTS.md, goose)
- [Gemma 4: 13x Agentic Performance Jump](/guides/gemma-4-agentic-open-model/) — Google's open-weights models with native function calling, released the same week as the summit

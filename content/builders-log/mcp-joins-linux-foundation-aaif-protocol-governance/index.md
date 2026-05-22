---
title: "The Protocol Layer Settles: MCP Joins the Linux Foundation"
date: 2026-05-22
description: "MCP crossed 97 million monthly installs and moved to a neutral Linux Foundation entity co-founded with Block and OpenAI. While the platform race is about owning the layers above — runtime, governance, context, deployment — the protocol layer just became commons. That changes the game for every builder working with AI agents."
content_type: "Builder's Log"
categories: ["MCP", "Agent Infrastructure", "Open Standards", "Industry Analysis"]
tags: ["mcp", "model-context-protocol", "linux-foundation", "aaif", "anthropic", "openai", "block", "agents-md", "goose", "open-standards", "protocol-governance", "analysis"]
---

In November 2024, Anthropic released the Model Context Protocol as an open standard. It was their protocol — their spec, their GitHub repo, their call whether to accept or reject contributions. Eighteen months later, MCP crossed 97 million monthly SDK downloads and Anthropic handed the keys to a neutral foundation.

That is the story. The implications take longer to unpack.

## What the AAIF Actually Is

The Linux Foundation announced the Agentic AI Foundation (AAIF) in December 2025, structured as a directed fund — the same model used for the Cloud Native Computing Foundation (CNCF) and the OpenJS Foundation. Three companies co-founded it with anchor project contributions:

- **Anthropic** contributed the Model Context Protocol
- **Block** contributed goose, an open-source local-first AI agent framework
- **OpenAI** contributed AGENTS.md, a project-context specification for AI coding agents

The AAIF's mandate: provide a vendor-neutral home for open-source agentic AI projects, with formal governance via Working Groups and Spec Enhancement Proposals (SEPs). Funding goes to community programs and interoperability research. No single company has veto authority over the spec.

This is the same governance pattern that made HTTP, Linux, and Kubernetes durable. A company or companies pioneer something useful, the ecosystem converges on it, and then — if the founders are strategically literate — they move it to neutral governance before the question of "who owns this" becomes a dealbreaker for adoption.

## The Growth Numbers Behind the Decision

MCP launched in November 2024 with roughly 2 million monthly SDK downloads. By March 2026 — sixteen months — that figure crossed 97 million. That is one of the fastest open-source protocol adoption curves on record.

By the time of the AAIF announcement, every major AI provider was shipping MCP-compatible tooling. The count of published MCP servers crossed 10,000. Enterprise deployments at Fortune 500 companies had moved from pilots to production. The [Atlassian Teamwork Graph](/builders-log/atlassian-teamwork-graph-context-layer/) runs over MCP. Microsoft's [Agent 365 governance layer](/builders-log/microsoft-agent-365-enterprise-governance-layer/) ships MCP-compatible tooling. Notion's External Agent API uses it.

At 97 million monthly installs, MCP had already won. The Linux Foundation move was not a pivot — it was the ratification of a fait accompli. You don't move something to neutral governance unless it's valuable enough that other parties will contribute to its upkeep.

The number also explains the timing. Early in a standard's life, keeping control is useful — you can iterate the spec quickly without committee overhead. At 97 million monthly installs, keeping control becomes a liability. Every enterprise legal team that asks "who controls this protocol?" now gets an answer that doesn't name Anthropic.

## The Three Projects: What Each One Does

**MCP** is the core. It defines how AI models connect to tools, data sources, and external systems. The 2026 roadmap under AAIF governance focuses on four areas: transport scalability (handling the volume), agent-to-agent communication (multi-agent workflows), governance maturation (SEP process, working groups), and enterprise readiness (security, audit trails, compliance primitives). The spec now evolves through public Spec Enhancement Proposals — like IETF RFCs, but for the agentic layer.

**goose**, from Block, is an open-source agent runtime that builds on MCP. It is local-first, extensible, and explicitly designed as a reference implementation for what an MCP-native agent looks like. The AAIF contribution positions goose as the canonical example of building on the protocol rather than around it.

**AGENTS.md** is the quieter contribution, and arguably the most immediately practical for most builders. It is a file-based convention — you put an `AGENTS.md` in your repository root, and AI coding agents that support it read it for project-specific context: how to run tests, which directories to avoid, how the codebase is organized, what conventions apply. More than 60,000 open-source projects had adopted it by the time it moved to AAIF. Agent frameworks that support it include Amp, Codex, Cursor, Devin, Factory, Gemini CLI, GitHub Copilot, Jules, and VS Code.

The parallel to `.gitignore` or `.editorconfig` is apt. A simple file format that solves a coordination problem, adopted fast because it costs nothing to add and immediately helps any agent that reads the repo.

## Governance Structure: What SEPs Actually Mean

The Spec Enhancement Proposal process is worth understanding in detail because it is where the protocol's future gets decided.

SEPs work like this: anyone can propose a spec change by opening a formal proposal. Working groups — composed of contributors from multiple organizations, not Anthropic's team alone — review, debate, and eventually accept or reject changes. There is a public record of every decision. There is no backroom veto.

For builders, this has one practical implication: if MCP is missing something your use case needs, you now have a legitimate path to propose it. The transport scalability work, the agent-to-agent communication primitives, the enterprise compliance features — these are not Anthropic's roadmap decisions anymore. They are the community's.

The AAIF is also running MCPCon events: AGNTCon + MCPCon North America and MCPCon Europe in 2026. These are where the working groups convene in person, where the de facto interpretations of ambiguous spec language get settled, and where the next two years of the protocol's evolution will be sketched out. If you are building a product that depends on MCP, you want to be in those rooms or following the outputs closely.

## The Connection to the Platform Race

The [platform race series](/builders-log/) has been tracking seven companies staking out different layers of the enterprise AI stack: Anthropic at the runtime layer, Google at vertical integration, Microsoft at governance, Atlassian at context, Notion at workspace coordination, IBM at the enterprise operating model, and OpenAI at deployment.

Here is the thing about the AAIF: Anthropic donated the protocol that every one of those companies depends on to ship their layer.

Atlassian's Teamwork Graph opens to external agents via MCP. Microsoft's Agent 365 requires MCP-compatible tooling to be governable. Google's agent ecosystem needs MCP to integrate with the developer tools already in the market. Notion's External Agent API is MCP-native. OpenAI's Deployment Company is building on a protocol their Deployment Company clients have already adopted.

Every platform racer's moat requires MCP to be neutral, open, and stable. A proprietary MCP owned by Anthropic would have been rejected by every other player in the stack. A vendor-neutral MCP under Linux Foundation governance is infrastructure everyone can build on without conceding strategic ground to a competitor.

Anthropic's move is also a competitive calculation. The AAIF governance ensures that no competitor can fork MCP into a proprietary alternative and drain developer attention. The standard is settled. The race is above it — at the runtime layer, the context layer, the deployment layer — where Anthropic is also competing. Giving up the protocol layer costs nothing because the value is elsewhere. Keeping it would have created friction that slowed universal adoption.

The result: the protocol layer is now commons. The seven-player platform race is racing over settled ground at the protocol layer, with the winner being determined by who builds the most valuable thing on top of it.

## What This Means If You Are Building

**MCP is now infrastructure, not a vendor feature.** When you adopt MCP as the integration layer for your product, you are not adopting Anthropic's proprietary standard. You are adopting a Linux Foundation-governed open protocol with 97 million monthly installs and working groups that include contributors from across the industry. The procurement objection — "this is controlled by one company" — no longer applies.

**The SEP process is your path to influencing the spec.** If MCP is missing something — a transport mechanism, a security primitive, a multi-agent workflow pattern — you can propose it through the formal SEP process. You cannot be told no by a single company's roadmap team. This is meaningful for builders who need the protocol to do something specific and are currently working around its gaps.

**AGENTS.md is worth adopting today.** If you maintain an open-source project or work in a repository where AI coding agents are used, adding an `AGENTS.md` costs ten minutes and immediately makes every agent that reads your repo more accurate. The 60,000-project adoption number is high enough that major agent frameworks treat it as a default. It is the lowest-friction contribution the AAIF has produced.

**MCPCon is where the spec gets built.** If your product's architecture depends on MCP — if you are building an MCP server, an MCP-native agent framework, or a product that integrates over MCP — the working groups and events run by the AAIF are where the de facto standard gets interpreted and where the next version gets designed. Following these closely is more valuable than most technical conferences.

**The protocol is settled; the race is above it.** Every builder working in the agent ecosystem is now working on settled infrastructure at the protocol layer. The competitive questions — which runtime, which context provider, which deployment model — are being fought out at higher layers. Understanding where the protocol ends and the proprietary layer begins is the architecture decision that matters now.

## The Gaps Worth Noting

The AAIF is new. SEP processes sound good in theory and can move slowly in practice — the IETF has RFCs that have been pending for years. The enterprise readiness roadmap items (security, audit, compliance) are still in progress. MCP server quality varies enormously; governance of the protocol does not mean quality control of the ecosystem.

The 97 million install figure is SDK downloads, not unique deployments. The relationship between download volume and active production deployments is not public. The 10,000 MCP servers number covers a wide range from "hello world" implementations to enterprise-grade tools.

And the AAIF's long-term funding model is an open question. CNCF-style foundations work when the ecosystem is large enough that contributions from many companies sustain the governance work. The agentic AI ecosystem is large, but whether the AAIF funding structure is durable is worth watching.

## One More Thing

In sixteen months, MCP went from an Anthropic blog post to a Linux Foundation-governed standard with 97 million monthly installs, three anchor projects, 10,000 servers, and a global event program.

The other protocols that moved at anything like this speed — TCP/IP, HTTP, Bluetooth, OAuth — became the foundation for industries. The question for MCP is not whether it will be important. It already is important. The question is whether the governance structure is robust enough to handle the next phase: enterprise compliance requirements, multi-agent coordination at scale, and the version 2.0 decisions that will either extend its durability or fragment the ecosystem.

The Linux Foundation bet is that neutral governance handles that better than single-company control. History suggests they are right. The builders who treat MCP as permanent infrastructure — not a dependency that might get deprecated or forked — are making the safer architectural bet.

The protocol layer has settled. Everything above it is still very much in play.

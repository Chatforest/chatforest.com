---
title: "Microsoft Build 2026: What Builders Should Watch For (June 2-3)"
date: 2026-05-26
description: "Microsoft Build 2026 runs June 2-3 in San Francisco. Here's what matters for AI builders: GitHub Copilot SDK in public preview, Foundry Agent Service GA, memory billing starting June 1, and a full MCP push across the stack."
content_type: "Builder's Log"
categories: ["Microsoft", "Developer Tools", "AI Infrastructure"]
tags: ["microsoft", "github-copilot", "azure", "mcp", "foundry", "agent-service", "developer-tools", "build-2026"]
---

Microsoft Build 2026 runs **June 2–3** at Fort Mason Center in San Francisco — and this year the developer conference is arriving with a fully assembled agent platform underneath it. Not a roadmap. Not a preview. A GA platform with memory, MCP integration, private networking, and billing that starts the day before the conference doors open.

If you're building with AI agents, here's what you need to know before June 2.

## What Build 2026 Is Actually About

Microsoft has been quietly assembling the pieces of an enterprise-grade agent stack for 18 months. Build 2026 is the moment they put the assembled picture on the wall.

The centerpiece is **Microsoft Foundry** — the rebrand and expansion of Azure AI Foundry into a unified platform for building, testing, and deploying agents. Foundry Agent Service is now GA. The REST API and SDK 2.0.0 (stable) shipped in February. The message this year isn't "here's what's coming" — it's "here's the production system, here are the prices, here's how to migrate your workloads."

That's a different kind of Build than the last few years.

## The Four Things Builders Should Watch

### 1. GitHub Copilot SDK

The Copilot SDK shipped in public preview on April 2, 2026. It gives builders a way to **embed GitHub Copilot's agentic capabilities directly into their own applications, workflows, and platform services** — not just use Copilot as a developer tool, but deploy Copilot-style AI as an infrastructure layer inside whatever you're building.

The session catalog includes "GitHub Copilot in Visual Studio: Agents That Debug, Profile, and Test," which previews both `/fleet` mode and `autopilot` mode — where the Copilot CLI can operate autonomously on narrow, bounded tasks without developer intervention per step.

For builders, the question the SDK raises is interesting: if you can embed Copilot's reasoning and tool-use inside your own product, where does the line between "your agent" and "Microsoft's agent" go? Build 2026 is likely to push that question further.

### 2. Foundry Agent Service: The Platform Is Now GA

Foundry Agent Service is the managed platform for deploying, hosting, and scaling agents. The GA release (February 2026) shipped with:

- **Responses API-based architecture** replacing the older Assistants API surface
- **End-to-end private networking** — MCP servers, AI Search indexes, and data agents all route over private network paths; no public MCP endpoints required
- **MCP auth expansion** including OAuth passthrough, so agents can authenticate through to enterprise data sources without credential management in application code
- **Hosted agents** — compute managed by Microsoft, available in 6 regions, replacing the need to provision and scale your own agent runtime
- **Toolbox** — define a curated set of tools once, manage them centrally, expose through a single MCP-compatible endpoint consumable by any MCP-compatible agent runtime

The unified SDK is now `AIProjectClient`, and the `azure-ai-agents` dependency is gone. If you've been building against the preview API surface, plan a migration.

### 3. Foundry Memory — and the Billing Cliff on June 1

This is the most immediately actionable item for anyone running Foundry agents in production.

Foundry memory is in public preview and provides **managed long-term memory** across agent sessions: it extracts facts and preferences from each conversation turn, consolidates them across sessions using LLM merging (resolving duplicates and conflicts), and retrieves relevant context at the start of each new session via hybrid search.

**Memory billing starts June 1, 2026** — the day before Build opens. The pricing:

| Service | Price |
|---------|-------|
| Short-term memory storage | $0.25 per 1K events stored |
| Long-term memory (monthly) | $0.25 per 1K memories per month |
| Memory retrieval | $0.50 per 1K retrievals |

If you've been using Foundry memory in preview without metering, that ends on June 1. Build 2026 sessions will almost certainly cover how to optimize memory usage — which means the conference is also a just-in-time cost-management resource for builders already running memory in their agents.

The four-phase memory pipeline (Extract → Consolidate → Retrieve → Customize) is also where Foundry's architecture is most opinionated. It's worth understanding before billing turns on.

### 4. MCP Across the Entire Stack

Microsoft has gone from MCP-curious to MCP-committed. The signals are everywhere:

- **Foundry MCP Server** at `mcp.ai.azure.com` (in preview since December 3, 2025): connect from VS Code, Visual Studio, or the Foundry portal with Entra auth and zero local process management
- **Visual Studio 2026** has dedicated sessions on building and using MCP servers — the IDE itself is becoming an MCP authoring and consumption environment
- **Oracle's session at Build 2026** ("Build AI Apps with Oracle AI Database@Azure, MCP, and GitHub Copilot") demonstrates that MCP has become the enterprise interoperability protocol of record, not just a developer toy
- Private networking for MCP server connections inside Foundry resolves the enterprise blocker Anthropic also addressed with MCP tunnels in May — the pattern of "MCP over private paths" is converging across vendors

The through-line: MCP is no longer a protocol you "add" to an agent. It's the substrate your agent platform is built on.

## The Broader Signal

What Microsoft is doing at Build 2026 isn't fundamentally about new model capability. The major models — GPT-5.5, Phi-4.5, Mistral, Llama — are already in the Foundry model catalog. Build is about **operationalization**: turning experimental agent infrastructure into something with SLAs, pricing, security architecture, and enterprise support contracts.

That operationalization push has a few builder implications:

**Cost surfaces that didn't exist six months ago.** Memory billing on June 1. Hosted agents priced by compute. MCP retrieval metered per call. The "build for free in preview" window is closing across the Microsoft stack. Budget accordingly.

**Private networking as a standard expectation.** Enterprise agents can now route MCP connections, data agent calls, and AI Search queries entirely over private network paths. If you're building for enterprise buyers, "no public endpoints required" is no longer a differentiator — it's a table stake.

**GitHub Copilot SDK as an integration surface.** Microsoft is building distribution into the SDK. If your product puts agents in front of developers, you now have to decide whether to build on top of GitHub's distribution or compete with it.

## Logistics

- **Dates**: June 2–3, 2026, 8:00 AM – 7:30 PM Pacific each day
- **Location**: Fort Mason Center for Arts & Culture, San Francisco
- **Livestream**: Free at build.microsoft.com — keynotes and select sessions
- **In-person**: $1,099

Build sessions go live on the conference website in the days after the event. If you can't attend live, the session recordings are typically the more useful resource anyway — pre-filtered for what actually shipped versus what was demoed.

---

*Builders using Foundry Agent Service should check memory billing status at the Azure portal before June 1. Memory consumption from public preview will begin generating charges on that date.*

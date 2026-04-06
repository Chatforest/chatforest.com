---
title: "Conway: Anthropic's Always-On Agent Platform Turns Claude Into a Persistent Digital Worker"
date: 2026-04-07T14:00:00+09:00
description: "Anthropic is testing Conway, a persistent always-on agent platform that transforms Claude from a reactive chatbot into a 24/7 autonomous worker. Conway features webhook-triggered activation, a .cnw.zip extension ecosystem, Chrome browser integration, and a standalone UI — positioning it as Anthropic's most ambitious agent infrastructure play yet."
content_type: "Guide"
card_description: "On April 1, 2026, TestingCatalog broke the news that Anthropic is internally testing Conway — a persistent agent platform that transforms Claude from a chat-based assistant into an always-on autonomous worker. Unlike standard Claude sessions that end when you close the tab, Conway runs continuously, responds to external events via webhooks, operates Chrome directly, executes code through Claude Code integration, and supports a new .cnw.zip extension format for third-party tools and UI customizations. The platform features a standalone sidebar UI with Search, Chat, and System sections, plus a Connectors system for managing external service integrations. References to a related system called Epitaxy suggest a complementary operator interface. If launched, Conway would represent Anthropic's most ambitious infrastructure play — moving beyond conversational AI into persistent agent infrastructure that competes directly with OpenAI's and Google's agent frameworks. This guide covers what we know about Conway's architecture, its extension ecosystem, competitive positioning, and what it signals about the future of always-on AI agents."
last_refreshed: 2026-04-07
---

On April 1, 2026, [TestingCatalog reported](https://www.testingcatalog.com/exclusive-anthropic-tests-its-own-always-on-conway-agent/) that Anthropic is internally testing Conway — a persistent agent platform that transforms Claude from a conversational assistant into an always-on autonomous worker. The leak reveals a system designed to run 24/7, respond to external events via webhooks, and support third-party extensions through a new package format.

If Conway ships, it represents a fundamental shift: Claude stops being a tool you use and becomes a worker that runs alongside you.

This guide covers what's known about Conway's architecture, its extension ecosystem, competitive implications, and what it means for the broader agent landscape. Our analysis draws on reporting from [TestingCatalog](https://www.testingcatalog.com/exclusive-anthropic-tests-its-own-always-on-conway-agent/), [Dataconomy](https://dataconomy.com/2026/04/03/anthropic-tests-conway-platform-for-continuous-claude/), [TechBriefly](https://techbriefly.com/2026/04/03/anthropic-explores-extension-based-agent-system-with-conway/), [AIBase](https://news.aibase.com/news/26796), and [36Kr](https://eu.36kr.com/en/p/3749600504660739) — we research and analyze rather than testing products hands-on. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

---

## What Conway Is

Conway is a standalone Claude agent environment — not a chat window, not a coding assistant, but a persistent runtime where Claude operates independently. Where Claude Code gives you an AI pair programmer in your terminal, Conway gives you an AI worker that stays active even when you're not watching.

The core architecture, based on leaked interface elements, includes:

**Standalone UI.** Conway gets its own dedicated sidebar in Claude's interface, separate from standard chat. The sidebar organizes into three sections: Search (with experimental hotkeys), Chat (the main conversation view), and System (a configuration hub for managing the agent's behavior and connections).

**Always-on operation.** Unlike session-based interactions that end when you close the browser, Conway instances persist. They can remain active continuously, processing tasks, monitoring external systems, and maintaining state across sessions.

**Webhook activation.** Conway exposes public URLs that external services can call to wake the instance. This enables event-driven operation — a GitHub push, a Slack message, a monitoring alert, or a cron job can trigger Conway to act without human intervention. Service-level toggles control which triggers are active.

**Chrome integration.** Direct browser connectivity allows Conway to operate Chrome, navigate websites, fill forms, extract data, and interact with web applications — extending its capabilities beyond API calls into visual web interaction.

**Claude Code integration.** Conway incorporates Claude Code's code execution capabilities, enabling multi-step task automation, repository management, and autonomous development workflows within the persistent environment.

## The Extension Ecosystem

Perhaps the most significant revelation is Conway's extension system, built around a new `.cnw.zip` package format. This is Anthropic building an app-store-like ecosystem for agent capabilities:

**What extensions can provide:**
- **Custom tools** — new capabilities that Conway can invoke during its operation
- **UI tabs** — additional interface panels within the Conway sidebar
- **Context handlers** — processors that shape how Conway interprets and responds to information

**How it works:** Users can install extensions through a dedicated Extensions management area, including drag-and-drop support for `.cnw.zip` files. The format appears designed to be self-contained packages that bundle tools, UI components, and configuration together.

**Why it matters:** The `.cnw.zip` standard would create a portable extension format specific to Anthropic's agent ecosystem. If widely adopted, it could establish Conway as a platform rather than just a product — the way VS Code's extension marketplace transformed it from an editor into an ecosystem.

## The Connectors System

Conway includes a Connectors infrastructure for managing external service integrations:

- **Connected clients** — a management interface showing which external services and tools are linked to the Conway instance
- **Tool exposure tracking** — visibility into which tools are available through each connector
- **Service-level controls** — granular toggles for enabling or disabling specific integration points

This suggests Conway is designed to sit at the center of an organization's tool ecosystem, maintaining persistent connections to services like GitHub, Slack, databases, monitoring systems, and internal APIs.

## Epitaxy: The Operator Interface

References to a previously spotted system called "Epitaxy" appear within Conway's interface, hinting that Epitaxy serves as the operator or management layer for the Conway environment. The relationship suggests a separation of concerns:

- **Conway** — the agent runtime (what Claude does)
- **Epitaxy** — the operator interface (how you manage what Claude does)

This architecture pattern mirrors how container orchestration separates the runtime (Docker) from the management plane (Kubernetes). If accurate, it suggests Anthropic is thinking about Conway at enterprise scale — where administrators need control planes separate from the agents themselves.

## Competitive Landscape: The Always-On Agent Race

Conway enters a rapidly evolving competitive field where every major AI lab is building persistent agent infrastructure:

### OpenAI Agents SDK
OpenAI replaced the experimental Swarm framework with a production-grade Agents SDK (v0.12.1) featuring agent handoffs, guardrails, tracing, and tool integration. It's designed for building multi-agent systems but doesn't yet offer Conway's always-on persistent runtime model.

### Google ADK (Agent Development Kit)
Google's ADK launched with SDKs in four languages (Python, TypeScript, Java, Go), native A2A protocol support, and a visual Agent Designer in the Google Cloud console. It's optimized for the Gemini ecosystem and emphasizes agent development as software development — but again focuses on building agents rather than providing a persistent runtime.

### Microsoft Copilot Studio
Microsoft's approach embeds agent capabilities within the Microsoft 365 ecosystem, offering persistent agents through Teams and the Copilot platform. It has the enterprise distribution advantage but is tightly coupled to the Microsoft stack.

### What Makes Conway Different
Conway's distinguishing features are the combination of:
1. **Persistence** — always-on rather than session-based
2. **Event-driven activation** — webhooks rather than manual invocation
3. **Extension ecosystem** — a standardized package format for third-party capabilities
4. **Browser integration** — direct Chrome operation for visual web tasks
5. **Standalone UI** — a dedicated agent workspace, not embedded in another product

Where competitors focus on frameworks for *building* agents, Conway appears to be a *hosted runtime* — the agent itself, ready to work, extensible through packages.

## What Conway Signals About the Industry

### From tools to workers
The shift from "AI assistant you talk to" to "AI worker that runs alongside you" is the defining transition of 2026. Conway makes this explicit: it's not a chatbot with extra features, it's an autonomous agent with a management interface.

### Platform economics
The `.cnw.zip` extension format signals Anthropic's intent to build platform lock-in through ecosystem effects. If Conway becomes popular, the extension marketplace becomes a moat — just as npm packages keep developers in the Node ecosystem and VS Code extensions keep them in that editor.

### Enterprise agent management
The Epitaxy operator interface, the Connectors system, and the service-level toggles all point toward enterprise deployment. Anthropic is designing for organizations that will run dozens or hundreds of Conway instances, each connected to different services and performing different roles.

### The "OS for AI" vision
Some coverage frames Conway as Anthropic's attempt to build "an operating system for AI" — a runtime environment where agents live, receive events, access tools, and extend their capabilities through installable packages. Whether that's hyperbole or prophecy depends on execution.

## What We Don't Know

Conway is still in internal testing, and significant questions remain:

- **Launch timeline** — no public release date has been announced
- **Pricing** — whether Conway will be a premium tier, usage-based, or bundled with existing plans
- **Resource limits** — how Anthropic will handle the compute costs of always-on agent instances
- **Security model** — how webhook endpoints are authenticated and how extension permissions are sandboxed
- **Enterprise features** — whether Conway will support team management, audit logging, and compliance controls
- **Extension review process** — whether `.cnw.zip` packages will be curated or open
- **Reliability** — uptime guarantees for a persistent agent that organizations might depend on for critical workflows
- **MCP integration** — whether Conway will natively support Model Context Protocol servers as connectors, which would be a natural fit given Anthropic's role in developing MCP

## Honest Assessment

Conway is ambitious and architecturally interesting, but it's important to note what we're looking at: leaked interface elements from an internal test. The gap between "Anthropic is testing this" and "Anthropic ships this" can be significant. Features get cut, architectures change, and timelines slip.

The always-on agent concept also introduces operational challenges that session-based AI avoids entirely. Persistent agents need error recovery, state management, cost controls, and security boundaries that are harder to get right than one-shot interactions. An agent that runs 24/7 and can be triggered by external webhooks has a much larger attack surface than one that only responds to direct user input.

That said, the direction is clear. Whether it's Conway specifically or something that evolves from it, Anthropic is building toward persistent agent infrastructure. The extension ecosystem and operator interface suggest they're thinking about this as a platform play, not just a product feature.

For organizations already using Claude for agent workflows, Conway is worth watching. For the broader industry, it confirms that the always-on agent runtime is becoming the next competitive frontier — after model quality, after tool use, after multi-agent orchestration.

---

*Published April 7, 2026. Based on leaked interface elements and reporting; Anthropic has not officially announced Conway. We will update this guide when official details are available.*

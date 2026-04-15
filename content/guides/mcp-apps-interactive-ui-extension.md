---
title: "MCP Apps: How Anthropic and OpenAI Brought Interactive UIs to AI Chat"
date: 2026-04-06T20:00:00+09:00
description: "MCP's first official extension lets servers render interactive dashboards, forms, and visualizations inside AI conversations. Ten launch partners shipped on day one. Here's how it works, who's using it, and what it means for MCP's future."
content_type: "Guide"
card_description: "MCP Apps (SEP-1865) is the first official extension to the Model Context Protocol, released January 26, 2026. It allows MCP servers to return interactive HTML interfaces — dashboards, forms, 3D visualizations, multi-step workflows — that render directly inside AI conversations via sandboxed iframes. Anthropic and OpenAI co-developed the specification with MCP-UI community maintainers, preventing fragmentation between competing implementations. Ten launch partners shipped on day one: Figma, Amplitude, Asana, Box, Canva, Clay, Hex, monday.com, Slack, and Salesforce. Client support includes Claude, ChatGPT, VS Code GitHub Copilot, Goose, Postman, and MCPJam. The ext-apps repository (1.9K GitHub stars, SDK v1.1.2) provides the specification and TypeScript SDK. This guide explains the architecture, security model, enterprise use cases, and what MCP Apps means for the protocol's evolution from tool-calling standard to application platform."
last_refreshed: 2026-04-15
---

Until January 2026, every [MCP](https://modelcontextprotocol.io/) interaction followed the same pattern: an AI agent calls a tool, gets back text or structured data, and renders it as chat messages. Need a chart? The agent describes it in words. Need a form? The agent asks questions one at a time. Need to approve an infrastructure change? You read a wall of JSON.

MCP Apps changed that. On [January 26, 2026](https://blog.modelcontextprotocol.io/posts/2026-01-26-mcp-apps/), the Model Context Protocol project shipped its first official extension, allowing MCP servers to return interactive HTML interfaces that render directly inside AI conversations. Dashboards with drilldowns. Forms with validation. 3D visualizations. Multi-step approval workflows. All inside the chat window, all governed by the same security model.

The more notable aspect: [Anthropic](https://www.anthropic.com/) and [OpenAI](https://openai.com/) built it together. Two companies in direct competition co-authored an [open specification](https://modelcontextprotocol.io/extensions/apps/overview) rather than fragmenting the ecosystem with proprietary approaches. Ten companies shipped MCP Apps integrations on launch day.

This guide explains how MCP Apps works, who's using it, and what it signals about where MCP is heading. Our analysis draws on the [official specification](https://modelcontextprotocol.io/extensions/apps/overview), [engineering blog posts](https://blog.modelcontextprotocol.io/posts/2026-01-26-mcp-apps/), launch partner announcements, and trade press coverage — we research and analyze rather than testing implementations hands-on. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

---

## The Problem MCP Apps Solves

[MCP](https://modelcontextprotocol.io/)'s original design handles tool-calling well: agents discover tools, call them with structured parameters, and get results back. But production deployments kept hitting the same wall — many workflows need visual output or complex input that text can't handle efficiently.

Consider these scenarios before MCP Apps:

- **Data analysis**: An agent queries a database and returns numbers. To explore the data — filter, sort, drill down — the user has to ask follow-up questions, burning tokens and patience with each round trip.
- **Design review**: A design tool returns a description of a layout. The user can't see it, manipulate it, or approve it without switching to another application.
- **Infrastructure approval**: A deployment tool returns a diff of changes. The approver reads raw config, hoping they don't miss a critical security group change buried in the output.

Each of these works in MCP today. None of them works well. The protocol could move data but couldn't present it.

---

## How MCP Apps Works

MCP Apps extends the protocol with two primitives that compose naturally with existing MCP concepts.

### The Core Pattern: Tools + UI Resources

An MCP App combines two things:

1. **A tool** that declares a reference to a UI resource in its metadata
2. **A UI resource** with a `ui://` URI scheme that renders data as interactive HTML

When a tool's result includes a UI reference, the host application renders the interface in place — right in the conversation, not in a separate window.

### Communication via postMessage

Rather than inventing a custom protocol, MCP Apps reuse the existing MCP [JSON-RPC](https://www.jsonrpc.org/) base protocol over the browser's [`postMessage` API](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage). The UI component runs in a sandboxed [iframe](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe) and communicates with the host through structured messages. This means MCP Apps inherit the same request-response patterns that MCP servers and clients already understand.

### Pre-declared Templates

UI templates are declared upfront as resources, not generated dynamically from arbitrary HTML. This is a deliberate security decision — hosts can inspect and audit what interfaces a server will present before rendering anything. The templates reference the `ui://` URI scheme and are part of the server's capability declaration.

### Lifecycle

The flow looks like this:

1. Server declares UI resources during capability negotiation
2. Agent calls a tool that references a UI resource
3. Host renders the UI in a sandboxed iframe within the conversation
4. User interacts with the UI (clicks, filters, inputs)
5. UI communicates changes back through postMessage
6. Server processes interactions and updates state

The key insight is that the UI is *served by the MCP server*, not generated by the AI model. The model orchestrates when to show a UI, but the server controls what the UI contains and how it behaves. The concept was [first proposed in November 2025](https://blog.modelcontextprotocol.io/posts/2025-11-21-mcp-apps/) and iterated through community feedback before the January 2026 launch.

---

## Security Model

MCP Apps run in sandboxed iframes with strict isolation. The sandbox prevents the app from:

- Accessing the parent window's DOM
- Reading the host's cookies or local storage
- Navigating the parent page
- Executing scripts in the parent context

All communication between the app and host goes through the `postMessage` API, which the host can monitor, filter, and audit.

Additional protections include:

- **Pre-declared templates** — hosts know what UIs a server will present before any tool is called
- **Auditable messages** — every interaction between the UI and host is a structured JSON-RPC message that can be logged
- **User consent** — hosts can require explicit user approval before rendering a UI

This layered approach means a compromised MCP server can't use MCP Apps to escalate privileges beyond what the iframe sandbox allows. It's defense in depth: even if the content inside the iframe is malicious, it's contained.

---

## Who Shipped on Day One

Ten launch partners had MCP Apps integrations ready for the January 26 release:

| Partner | What Their MCP App Does |
|---|---|
| **[Figma](https://www.figma.com/)** | Turns text descriptions into flow charts and Gantt diagrams in [FigJam](https://www.figma.com/figjam/), rendered in-conversation |
| **[Hex](https://hex.tech/)** | Answers data questions with interactive charts and source citations |
| **[Amplitude](https://amplitude.com/)** | Builds analytics dashboards with adjustable parameters directly in chat |
| **[Box](https://www.box.com/)** | Searches files, previews documents inline, enables Q&A about document content |
| **[Canva](https://www.canva.com/)** | Design creation and editing within the conversation |
| **[Asana](https://asana.com/)** | Project management interfaces with task visualization |
| **[monday.com](https://monday.com/)** | Workflow and board interactions embedded in chat |
| **[Slack](https://slack.com/)** | Message composition and channel interaction |
| **[Clay](https://www.clay.com/)** | Contact and relationship data exploration |
| **[Salesforce](https://www.salesforce.com/)** | CRM data visualization and record management |

These are not demo integrations. [Figma](https://www.figma.com/)'s implementation renders editable diagrams. [Hex](https://hex.tech/) returns charts you can hover over for data points. [Amplitude](https://amplitude.com/) lets you drag date ranges and toggle metrics. The interactions happen inside the conversation — no context-switching to separate applications.

---

## Client Support

As of April 2026, these clients support MCP Apps:

- **[Claude](https://claude.ai/)** (web and [desktop](https://claude.ai/download)) — [Anthropic](https://www.anthropic.com/) built support directly into the chat experience
- **[ChatGPT](https://chatgpt.com/)** — [OpenAI](https://openai.com/) rolled out support following the joint specification work
- **[VS Code](https://code.visualstudio.com/) [GitHub Copilot](https://github.com/features/copilot)** — available in [Insiders builds](https://code.visualstudio.com/insiders/)
- **[Goose](https://github.com/block/goose)** ([Block](https://block.xyz/)'s open-source agent) — [shipped support on January 6, 2026](https://block.github.io/goose/blog/2026/01/06/mcp-apps/), before the official launch
- **[Postman](https://www.postman.com/)** — integrated into their API development workflow
- **[MCPJam](https://mcpjam.com/)** — community MCP client

The specification is open, so any chatbot or agent framework can adopt it. The cross-platform support was intentional — [Anthropic](https://www.anthropic.com/) and [OpenAI](https://openai.com/) co-developing the standard meant both ecosystems had buy-in from day one.

---

## The GitHub Repository

The official implementation lives at [modelcontextprotocol/ext-apps](https://github.com/modelcontextprotocol/ext-apps) on GitHub:

- **1.9K stars** as of April 2026
- **SDK version**: v1.1.2
- **Language**: [TypeScript](https://www.typescriptlang.org/)
- **License**: Open source

The repository includes working examples that demonstrate the range of what's possible:

- **threejs-server** — [Three.js](https://threejs.org/) 3D visualization rendered in conversation
- **map-server** — interactive maps with location data
- **pdf-server** — document viewing and annotation
- **system-monitor-server** — real-time system dashboards
- **sheet-music-server** — music notation rendering

---

## Enterprise Use Cases

The enterprise value becomes clear when you consider workflows that previously required switching between AI chat and specialized applications.

### Financial Dashboards

An analyst asks about quarterly performance. Instead of getting a text summary, they see an interactive dashboard with bar charts showing revenue by product line, a heat map of regional performance, and a sortable table with drill-down capabilities. They filter by region, compare quarters, and identify underperforming products — all without leaving the conversation.

### Infrastructure Approvals

A DevOps engineer requests a deployment. The approver sees a structured interface showing infrastructure changes with visual network diagrams, security group rules in tables, IAM policy comparisons, and cost estimates. Invalid configurations are highlighted. The security team can audit exactly what was presented at approval time because every interaction is logged as a JSON-RPC message.

### Configuration Management

An IT admin provisions access for a new team. MCP Apps presents a multi-step form showing available applications, group hierarchies with permission previews, and MFA policy options with security implications. Invalid combinations are disabled with explanations, preventing misconfigurations before they happen.

### Compliance and Auditing

A compliance officer reviews database access patterns. An interactive audit dashboard shows all access requests, approvers, data accessed, and policy violations. They filter by date range, user, or database — generating the same audit trail that previously required exporting data to a BI tool.

---

## How This Relates to MCP's Evolution

MCP Apps represents a significant shift in what MCP is becoming. The protocol started as a way for AI agents to call tools — essentially, a standardized function-calling interface. MCP Apps extends it into an *application platform*.

This matters for three reasons:

### 1. It Addresses the Context Bloat Problem Differently

One of MCP's biggest production pain points is [context window waste](/guides/mcp-growing-pains-2026/) — tool descriptions consuming 40-70% of available tokens before a conversation begins. MCP Apps partially sidesteps this by moving complexity from token-heavy text exchanges into interactive UIs. Instead of five rounds of "show me this filtered by that" (each burning tokens), one UI handles the exploration locally.

### 2. It Makes the Anthropic-OpenAI Collaboration Concrete

The joint specification work ([SEP-1865](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/1865)) with [OpenAI](https://openai.com/) is more than a press release. Both companies' flagship products ship MCP Apps support. This is the strongest signal yet that MCP's governance model — now under the [Linux Foundation](https://www.linuxfoundation.org/)'s [Agentic AI Foundation](https://agenticaifoundation.org/) — actually produces cross-vendor collaboration.

### 3. It Creates a New Category of MCP Server

Before MCP Apps, building an MCP server meant writing tool handlers that return data. Now it means building interactive experiences. The skill set shifts from API design to application design — server developers need to think about UI/UX, not just data schemas. This will attract a different set of contributors and use cases to the MCP ecosystem.

---

## Limitations and Open Questions

MCP Apps is production-ready, but it's still early:

- **HTML rendering variability** — different clients may render the same HTML slightly differently, since each implements its own iframe sandboxing. There's no pixel-perfect consistency guarantee across [Claude](https://claude.ai/), [ChatGPT](https://chatgpt.com/), and [VS Code](https://code.visualstudio.com/).
- **Offline and mobile** — the current specification assumes a client capable of rendering sandboxed iframes. Mobile clients and CLI tools may have limited or no MCP Apps support.
- **Complexity ceiling** — how complex can an in-conversation UI get before users prefer the dedicated application? [Figma](https://www.figma.com/)-in-chat is impressive, but will people actually design in it vs. switching to Figma?
- **Accessibility** — the specification mentions sandboxing and security, but accessibility standards for embedded UIs in chat interfaces are not yet addressed in the spec.
- **Server-side state** — interactive UIs often need persistent state. MCP's stateful session model is already a [scaling challenge](/guides/mcp-growing-pains-2026/); adding UI state to that may compound the problem.

---

## What This Means for Builders

If you're building MCP servers, MCP Apps changes the calculus:

- **Existing servers** can add UI resources incrementally — you don't have to rebuild. A data query tool that currently returns JSON can add a chart UI as an enhancement.
- **New servers** should consider UI-first design for workflows that involve exploration, approval, or complex input.
- **The [TypeScript](https://www.typescriptlang.org/) SDK** at [modelcontextprotocol/ext-apps](https://github.com/modelcontextprotocol/ext-apps) provides the reference implementation and working examples to start from.

For enterprises evaluating MCP adoption, MCP Apps strengthens the case by addressing one of the biggest user experience gaps — the text-only interaction model that makes sophisticated workflows feel like working through a command line.

---

## Sources

- [MCP Apps: Bringing UI Capabilities to MCP Clients](https://blog.modelcontextprotocol.io/posts/2026-01-26-mcp-apps/) — Official MCP Blog, January 26, 2026
- [MCP Apps: Extending servers with interactive user interfaces](https://blog.modelcontextprotocol.io/posts/2025-11-21-mcp-apps/) — Official MCP Blog, November 21, 2025 (initial proposal)
- [Anthropic extends MCP with an app framework](https://thenewstack.io/anthropic-extends-mcp-with-an-app-framework/) — The New Stack, January 27, 2026
- [Anthropic and OpenAI Join Forces to Standardize Interactive AI Interfaces](https://inkeep.com/blog/anthropic-openai-mcp-apps-extension) — Inkeep
- [MCP Apps Extension: Interactive UI for Enterprise AI Agents](https://webrix.ai/blog/mcp-apps-extension-enterprise-use-cases) — Webrix
- [MCP Apps Official Release](https://technyanai.com/articles/en/20260126/mcp-apps-official-extension) — Technyan's AI Digests
- [Claude supports MCP Apps, presents UI within chat window](https://www.theregister.com/2026/01/26/claude_mcp_apps_arrives/) — The Register, January 26, 2026
- [Goose Lands MCP Apps](https://block.github.io/goose/blog/2026/01/06/mcp-apps/) — Goose Blog, January 6, 2026
- [MCP Apps Guide: Build Interactive UI Inside Claude, ChatGPT, and VS Code](https://bytebot.io/articles/mcp-apps) — Bytebot
- [SEP-1865: MCP Apps Pull Request](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/1865) — GitHub
- [modelcontextprotocol/ext-apps](https://github.com/modelcontextprotocol/ext-apps/) — Official GitHub repository
- [MCP Apps Overview](https://modelcontextprotocol.io/extensions/apps/overview) — Official specification

---

## Further Reading

- [MCP's Growing Pains: Context Bloat, Security Gaps, and the Companies Walking Away](/guides/mcp-growing-pains-2026/) — the production challenges MCP Apps partially addresses
- [The Agentic AI Foundation: What Happens When Competitors Co-Govern an Open Standard](/guides/agentic-ai-foundation-mcp-governance/) — AAIF governance structure, 146 members, founding projects (MCP, AGENTS.md, goose)

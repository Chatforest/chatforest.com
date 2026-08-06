# Microsoft MCP Dev Days Is July 29–30 — Here Is the Session-by-Session Builder Preview

> A builder-focused preview of Microsoft's free virtual MCP Dev Days (July 29–30, 2026): what each session covers, which ones to prioritize if you're building production MCP servers, and how the event differs from the April Linux Foundation summit.


Microsoft's **MCP Dev Days** runs July 29–30, 2026 as a [free, two-day virtual event](https://developer.microsoft.com/blog/join-us-for-mcp-dev-days-july-29-30) through the Microsoft Reactor program. Registration is at [aka.ms/mcpdevdays](https://aka.ms/mcpdevdays). The event streams live starting 9:00 AM Pacific / 4:00 PM UTC each day, and sessions are [recorded for on-demand viewing](https://developer.microsoft.com/en-us/reactor/series/s-1563/) afterward.

This is not a repeat of the April Linux Foundation [MCP Dev Summit North America](/guides/mcp-dev-summit-2026-guide/). That event was a community-organized in-person conference with [approximately 1,200 attendees](https://www.infoq.com/news/2026/04/aaif-mcp-summit/) and [17 keynotes and over 95 sessions](https://futurumgroup.com/insights/mcp-dev-summit-2026-aaif-sets-a-clear-direction-with-disciplined-guardrails/) across four tracks. MCP Dev Days is a Microsoft-produced virtual event focused on tooling, Azure implementation patterns, and the growing community registry — a tighter scope with a hands-on, builder-first framing.

The two events complement rather than overlap. If you watched the April summit recordings, you still have reason to attend this one.

---

## What each day covers

**[Day 1 — DevTools (July 29)](https://developer.microsoft.com/en-us/reactor/events/26140/):** Ecosystem-level topics. How VS Code, GitHub Copilot, and Visual Studio surface MCP. Community registry discoverability. The MCP authorization specification (OAuth 2.1). NLWeb. [Community partners Arcade, Block, Okta, and Neon](https://developer.microsoft.com/blog/join-us-for-mcp-dev-days-july-29-30).

**[Day 2 — Builders (July 30)](https://developer.microsoft.com/en-us/reactor/events/26141/):** Implementation depth. Building remote MCP servers. The C# SDK. Production security patterns. Azure building blocks (Functions, Container Apps, API Management) for scalable deployments. Agents talking to agents via MCP. On-demand self-paced training available alongside live sessions.

---

## Day 1 sessions — DevTools (July 29, 9am–1pm PST)

*Full agenda, times, and speaker list verified against [Microsoft Reactor's Day 1 event page](https://developer.microsoft.com/en-us/reactor/events/26140/).*

### [9:00am — Keynote: Building the Future of AI Development Together](https://developer.microsoft.com/en-us/reactor/events/26140/)
**Speakers:** Jay Parikh (Microsoft EVP, CoreAI), James Montemagno, Linda Li, Drew Hodun, Burke Holland, Donald Thompson

Jay Parikh leads Microsoft's [CoreAI group](https://developer.microsoft.com/en-us/reactor/events/26140/), the team behind Copilot, GitHub, and Microsoft's AI infrastructure; he [set the platform-first keynote theme at Microsoft Build 2026](https://developer.microsoft.com/blog/build-recap/) in June ("AI models alone aren't enough — you need the whole system around them"). The keynote includes lightning demos across VS Code, GitHub Copilot, Azure AI Foundry, and Windows. Parikh's role means this is the closest you'll get to an official roadmap statement on where Microsoft is taking MCP at the platform level.

Worth watching for: any announcement about MCP support in Azure AI Foundry or the Windows Copilot Runtime that didn't make Build's formal announcements.

### [9:30am — MCP Power-User Mode: Revealing Every MCP Feature in VS Code](https://developer.microsoft.com/en-us/reactor/events/26140/)
**Speaker:** Liam Hampton

A demo-heavy walkthrough of what VS Code can actually do with MCP that most users haven't found. The session description promises shortcuts, settings, and insider tips — the kind of content that doesn't surface in documentation until months later.

Worth watching for: hidden configuration options, multi-server orchestration patterns inside the editor, and anything around MCP tool approval workflows that changes the security posture of local development.

### [10:00am — Discoverability Unlocked: Publishing and Finding Servers in the MCP Community Registry](https://developer.microsoft.com/en-us/reactor/events/26140/)
**Speakers:** Toby Padilla, Tadas Antanavicius

Toby Padilla is [GitHub's Principal Product Manager for MCP](https://developer.microsoft.com/en-us/reactor/events/26140/) and one of the [Registry Maintainers who built and launched](https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/) the community registry at modelcontextprotocol.io (alongside Tadas Antanavicius of PulseMCP, who spearheaded the initial effort, and Anthropic's Adam Jones). This session covers both sides of the registry: how builders publish their servers and how users discover them.

Worth watching for: the registry's quality signals, verification tiers, and how the community registry interacts with private enterprise registries.

### [10:30am — Chat With the Web: Inside NLWeb's Journey to a Conversational Internet](https://developer.microsoft.com/en-us/reactor/events/26140/)
**Speakers:** Ramanathan Guha, Jennifer Marsman, Chelsea Carter, James Montemagno

This is the session most likely to change how you think about MCP surface area. **Ramanathan Guha** is [CVP and Technical Fellow at Microsoft](https://developer.microsoft.com/en-us/reactor/events/26140/) and [conceived and developed NLWeb](https://news.microsoft.com/source/features/company-news/introducing-nlweb-bringing-conversational-interfaces-directly-to-the-web/) — the Microsoft Research project that turns any website's existing structured data into an MCP endpoint without writing a custom server. Microsoft [credits him as a creator of RSS and Schema.org](https://news.microsoft.com/source/features/company-news/introducing-nlweb-bringing-conversational-interfaces-directly-to-the-web/). If you've been watching NLWeb from a distance, this is the session where the creator explains the design choices.

NLWeb's approach: websites expose an [`/ask` endpoint (NLWeb also runs as an MCP server)](https://github.com/nlweb-ai/NLWeb) built on their existing Schema.org or RSS metadata. AI assistants then treat the site as a native MCP server — browsing, filtering, and querying its content in natural language rather than scraping HTML. The implication for builders is that any data-driven site can become an MCP source with one endpoint addition, not a full server implementation.

Worth watching for: which content types NLWeb handles well, which require a custom MCP server despite NLWeb's existence, and the roadmap for NLWeb's spec status within the broader MCP ecosystem.

### [11:00am — The Future of User Interaction](https://developer.microsoft.com/en-us/reactor/events/26140/)
**Speaker:** Kent C. Dodds

Kent Dodds, creator of [EpicWeb.dev](https://www.epicweb.dev/) and its Epic Stack, is listed on the [Reactor speaker page](https://developer.microsoft.com/en-us/reactor/events/26140/) under Kent C. Dodds Tech LLC. The [session description promises](https://developer.microsoft.com/en-us/reactor/events/26140/) to show "how this AI assistant user interaction model is shaping out to be," with a focus on what role developers play in determining what that future looks like.

This is less an implementation session and more a design vision talk. Worth watching if you're making architectural decisions about how users interact with your AI features — the shift from command-driven to natural-language-driven UI patterns, and what that means for how you structure tool definitions.

### [11:30am — MCP Gets OAuth: Understanding the New Authorization Specification](https://developer.microsoft.com/en-us/reactor/events/26140/)
**Speakers:** Den Delimarsky (Microsoft), Aaron Parecki

**Aaron Parecki** is [Director of Identity Standards at Okta](https://developer.microsoft.com/en-us/reactor/events/26140/), author of the [OAuth 2.0 Simplified guide](https://aaronparecki.com/oauth-2-simplified/), and an [editor of specifications in the OAuth working group at the IETF](https://aaronparecki.com/about/), including OAuth 2.1. Den Delimarsky is a [Principal Product Engineer at Microsoft](https://developer.microsoft.com/en-us/reactor/events/26140/) who [co-authored the MCP authorization specification](https://den.dev/blog/new-mcp-authorization-spec/) with Anthropic.

The spec standardizes how remote MCP servers authenticate clients using [OAuth 2.1 with mandatory PKCE, and — in its current revision — Protected Resource Metadata for zero-config discovery](https://den.dev/blog/mcp-november-authorization-spec/). Before the spec, builders implementing auth on remote servers had to invent their own patterns — often HTTP bearer tokens outside any formal grant flow, without token rotation or scoping. The spec closes that gap.

Worth watching for: which grant flows are in-scope, how token lifetimes work, the spec's treatment of multi-tenant servers, and which existing implementations lag the current spec revision.

**This is the most technically dense Day 1 session.** If your MCP servers are remote (HTTP transport, not local stdio), understanding this spec is not optional.

### [12:00pm — MCP Workflow: I Stopped Using SQL for Database Management](https://developer.microsoft.com/en-us/reactor/events/26140/)
**Speaker:** Bobur Umurzokov

A practical case study session on using MCP to replace manual SQL workflows in database management tasks. Worth watching if you're building MCP servers that front databases — the session likely covers prompt-to-query patterns, context window management for large schemas, and error-handling patterns when queries fail.

### [12:30pm — Boost Your Productivity With Visual Studio & MCP Servers](https://developer.microsoft.com/en-us/reactor/events/26140/)
**Speaker:** Allie Barry

Visual Studio (not VS Code) MCP integration for .NET and enterprise development workflows. If your team uses VS rather than Code, this is the session that covers what's available.

---

## Day 2 sessions — Builders (July 30, 9am–1pm PST)

*Full agenda, times, and speaker list verified against [Microsoft Reactor's Day 2 event page](https://developer.microsoft.com/en-us/reactor/events/26141/).*

### [9:00am — Day 2 Keynote: From Concept to Code](https://developer.microsoft.com/en-us/reactor/events/26141/)
**Speakers:** Marc Baiza, Katie Savage, Julia Kasper, Matthew Henderson

The Day 2 keynote frames the Azure building blocks for scalable MCP server deployment: Azure Functions, Azure Container Apps (ACA), and Azure API Management (APIM). The title "From Concept to Code" positions this as the bridge between "I understand MCP" and "I have a production-grade server running in Azure."

Worth watching for: which Azure tier is the right default for a new MCP server, how APIM fits into the MCP auth story (APIM has native OAuth support), and whether any new Azure-native MCP tooling was announced alongside the event.

### [9:30am — Vibe Code Your First MCP Server With GitHub Copilot](https://developer.microsoft.com/en-us/reactor/events/26141/)
**Speaker:** Burke Holland

An AI-assisted, prompt-driven workflow for writing your first MCP server using GitHub Copilot as the development environment. "Vibe coding" in this context means using natural language to generate the server scaffold, tool definitions, and connection boilerplate — then iterating from there.

Worth watching for: which parts of MCP server construction Copilot handles well out of the box, which parts require manual spec knowledge, and the session's advice on when to use AI-generated scaffolding versus working directly from the SDK.

### [10:00am — MCP C# SDK Deep Dive](https://developer.microsoft.com/en-us/reactor/events/26141/)
**Speaker:** Mike Kistler

The [official C# SDK for MCP](https://github.com/modelcontextprotocol/csharp-sdk) is maintained in collaboration with Microsoft alongside the TypeScript and Python SDKs; Mike Kistler is [Principal Product Manager at Microsoft](https://developer.microsoft.com/en-us/reactor/events/26141/). If your team is building MCP servers in .NET — which is the likely path for organizations already running .NET microservices — this session provides an implementation reference straight from the SDK team.

### [10:30am — Practical Introduction to Building Remote MCP Servers](https://developer.microsoft.com/en-us/reactor/events/26141/)
**Speakers:** Toby Padilla, Joe Zhou

The ground-level implementation session for remote servers. Toby Padilla returns from Day 1's registry session to cover the server side: HTTP transport, session management, streaming SSE responses, and the full request-response cycle for a remote server over HTTPS.

Remote servers are architecturally different from local stdio servers — they run in the cloud, handle concurrent sessions from multiple clients, require auth, and must manage connection state across tool calls. Most MCP tutorials cover local stdio. This session covers what changes when you need remote.

### [11:00am — MCP In Production: Building Secure and Agent-Ready Model Context Protocol Servers](https://developer.microsoft.com/en-us/reactor/events/26141/)
**Speakers:** Den Delimarsky, Nate Barbettini, Wils Dawson

**This is the highest-value session for builders already running MCP in production.**

Nate Barbettini is a [Founding Engineer at Arcade.dev](https://developer.microsoft.com/en-us/reactor/events/26141/) who previously worked in developer relations at Okta; Den Delimarsky is [Microsoft's Principal Product Engineer](https://developer.microsoft.com/en-us/reactor/events/26141/) and [co-author of the MCP authorization spec](https://den.dev/blog/new-mcp-authorization-spec/); Wils Dawson is a [Founding Software Engineer at Arcade.dev](https://developer.microsoft.com/en-us/reactor/events/26141/), previously at Okta, Kong, and ngrok.

The session's framing — "secure and agent-ready" — covers two distinct problems. "Secure" addresses tool injection, prompt injection via tool results, transport-layer attacks, and over-permissioned tool definitions. "Agent-ready" addresses design patterns that make your server usable by autonomous agents without human approval on every tool call — tool definition clarity, idempotency, bounded side-effects, and error responses that agents can reason about.

Worth watching for: specific threat models with examples, recommended server design checklists, and whether the team covers any published CVEs or real-world attack demonstrations.

### [11:30am — Building Your Own MCP Registry With API Center and API Management](https://developer.microsoft.com/en-us/reactor/events/26141/)
**Speakers:** Julia Kasper, Anish Tallapureddy

[Azure API Center now tracks MCP server metadata](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server) — version history, ownership, and custom properties — as part of its registry schema; Julia Kasper is [Program Manager for Azure API Center at Microsoft](https://developer.microsoft.com/en-us/reactor/events/26141/). This session covers building a private enterprise MCP registry — the equivalent of the community registry but inside your organizational boundary, with access control, version management, and audit logging.

For enterprise teams managing dozens of internal MCP servers across teams, this is the architecture session. APIM's position here is as the auth gateway and rate limiter in front of the registry.

### [12:00pm — Agents Talking to Agents: Harnessing MCP for Seamless Inter-Agent Collaboration](https://developer.microsoft.com/en-us/reactor/events/26141/)
**Speakers:** Adam Kaplan, Victor Dibia

The inter-agent collaboration session. MCP's tool definition format is increasingly used as the interface contract between agents — an orchestrator agent calls a worker agent via MCP rather than via a proprietary function call. This session covers what that pattern looks like in practice: how agents expose their capabilities as MCP tools, how routing works, and how you maintain context across the agent-to-agent boundary.

Victor Dibia is a [Principal Research Software Engineer at Microsoft Research](https://www.microsoft.com/en-us/research/people/victordibia/) and a founding developer on [AutoGen, Microsoft's open-source multi-agent framework](https://www.microsoft.com/en-us/research/people/victordibia/).

Worth watching for: whether the session presents this as an alternative to A2A protocol or as a complement, and the practical debugging story when an inter-agent MCP chain fails mid-workflow.

### [12:30pm — Unlocking Your Agent's Potential With Model Context Protocol](https://developer.microsoft.com/en-us/reactor/events/26141/)
**Speaker:** Dave Glover

A closing synthesis session covering how to connect the MCP pieces covered throughout both days — from server design through registry to agent integration. Worth watching as a summary and integration guide if you've missed individual sessions.

---

## Sessions to prioritize if your time is limited

**If you're building remote MCP servers:** 11:30am Day 1 (OAuth spec), 10:30am Day 2 (remote server fundamentals), 11:00am Day 2 (production security).

**If you're on .NET:** 9:00am Day 2 keynote (Azure building blocks), 10:00am Day 2 (C# SDK), 11:30am Day 2 (private registry with APIM).

**If you're building multi-agent systems:** 11:00am Day 1 (Kent Dodds, user interaction design), 12:00pm Day 2 (agents talking to agents).

**If you've never written an MCP server:** 9:30am Day 2 (Copilot-assisted build), 10:30am Day 2 (remote server intro), and the pre-event workshops below.

**If you're making content or data available via MCP:** 10:30am Day 1 (NLWeb — it may render your custom server unnecessary).

**If you manage a team with many MCP servers:** 10:00am Day 1 (registry and discoverability), 11:30am Day 2 (private enterprise registry).

---

## Pre-event resources

Microsoft has published a [self-paced "MCP for Beginners" course](https://aka.ms/mcp-for-beginners) alongside the event announcement, a 12+ module curriculum with a database-integrated MCP server as the capstone project. The course is designed to bring new builders up to protocol literacy before the live sessions. Microsoft has also run a separate ["Let's Learn MCP" 90-minute livestream workshop series](https://developer.microsoft.com/blog/join-us-for-mcp-dev-days-july-29-30). If the sessions above read as advanced content — tool definitions, transports, auth flows — the self-paced course is the right starting point.

---

## What this event is not

MCP Dev Days will not cover the [July 28 MCP spec revision](https://github.com/modelcontextprotocol/csharp-sdk) — the largest revision of the protocol since it launched — which drops the day before the event and is unlikely to appear in prepared session content. Expect the community conversation around it to happen on the sidelines in Discord and X during the event, not on stage.

The event is Microsoft-produced, which means the implementation context skews Azure. If you're deploying on AWS Lambda or GCP Cloud Run, the patterns from the Day 2 keynote and the ACA-specific sessions translate but require translation work. The C# SDK and APIM registry sessions are Azure-native.

---

## How to register

Free virtual event. Register at [aka.ms/mcpdevdays](https://aka.ms/mcpdevdays). The event page lists both days as part of the same registration.

Both days stream live at 9:00 AM Pacific / 4:00 PM UTC and are recorded. On-demand access is available after the live stream ends.

---

*ChatForest is operated by [Rob Nugen](https://robnugen.com). Research and writing by AI. We analyze sessions from publicly available schedules and speaker announcements — we don't attend events hands-on.*

*For related reading: [MCP Dev Summit North America 2026 (April)](/guides/mcp-dev-summit-2026-guide/), [What Is MCP?](/guides/what-is-mcp/), [MCP Server Security](/guides/mcp-server-security/), [MCP Registry and Server Discovery](/guides/mcp-registry-server-discovery/), [MCP 2026 Roadmap](/guides/mcp-2026-roadmap-whats-coming/).*


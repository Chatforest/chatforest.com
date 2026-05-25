# Salesforce Headless 360 Review — The Entire CRM Platform Is Now an MCP Server

> Salesforce Headless 360, launched at TDX 2026, exposes every capability of the world's largest CRM as an API, MCP tool, or CLI command. AI agents can now operate Salesforce — creating accounts, running DevOps pipelines, querying data — without a browser or human login. 60+ new MCP tools, free Developer Edition access. Here's what changed and why it matters.


**At a glance:** Salesforce Headless 360. Announced April 15, 2026, TDX developer conference. Entire Salesforce platform exposed as API, MCP tools, and CLI for AI agents. 60+ new MCP tools. Free Developer Edition. Part of our **[AI Tools & Companies reviews](/categories/ai-tools/)**.

---

Every major software platform eventually faces the same pressure: the interfaces that worked for humans need to be rebuilt for the things replacing human workflows. Salesforce just made its call.

On April 15, 2026, at its annual TDX developer conference in San Francisco, Salesforce unveiled Headless 360 — an initiative the company calls the most significant platform shift in its 27-year history. The premise is blunt: every Salesforce capability, across all of its clouds, is now an API endpoint, a Model Context Protocol (MCP) tool, or a CLI command. AI agents can operate the full Salesforce platform without a browser, without a user interface, and — depending on how you configure it — without human intervention.

This is not a feature update. It is an architectural reclassification of what Salesforce is.

---

## What Salesforce Headless 360 Actually Is

The word "headless" in software usually means "without a graphical interface" — a content management system that stores content and exposes it via API without caring how it's rendered. Salesforce is applying that concept to an entire enterprise platform.

Headless 360 reorganizes the Salesforce stack into four programmable layers:

**Data 360 (system of context)** — Every data object, record, relationship, and schema Salesforce stores is now queryable via REST and GraphQL APIs, and exposed as MCP resources. An AI agent can ask about customer account history, open opportunities, support tickets, and contract terms through the same protocol it uses to query anything else — no SOQL knowledge required.

**Customer 360 apps (system of work)** — Sales Cloud, Service Cloud, Marketing Cloud, Commerce Cloud: the applications themselves are now exposed as structured API surfaces. Workflows, business logic, and approval processes can be invoked by agents via API rather than triggered by human clicks through the UI.

**Agentforce (system of agency)** — Salesforce's agent platform, now on version 2.0, becomes the orchestration layer. Agentforce Vibes 2.0 ships with multi-model support (Claude Sonnet and GPT-5 both available), full organizational context from session start, and an AI development partner that understands business-specific configuration. It replaces Agentforce Vibes 1.0's limited context model with something closer to what enterprise developers actually need: an agent that knows your org.

**Slack (system of engagement)** — Slack remains the primary human-facing surface, but it now receives structured outputs from agents via the new Experience Layer, rather than requiring agents to compose freeform messages. The same agent action renders as an interactive card in Slack, a response in ChatGPT, a panel in Claude, or a component in Teams.

---

## 60+ New MCP Tools

The headline developer number is the MCP toolset: more than **60 new MCP tools and 30+ preconfigured coding skills** shipped immediately at launch.

The tools span six categories:

- **Metadata** — read, create, and modify Salesforce schema, fields, objects, validation rules, page layouts
- **Data** — query records, run SOQL, aggregate and export
- **Testing** — run Apex unit tests, view coverage, invoke test suites
- **LWC development** — scaffold, modify, and deploy Lightning Web Components
- **Code analysis** — static analysis, performance analysis, dependency mapping
- **DevOps** — access the DevOps Center programmatically; describe what you want to deploy in natural language, and agents execute

The toolset is directly integrated with the AI coding environments most enterprise developers already use: **Claude Code, Cursor, Codex, and Windsurf** are all confirmed as first-class integration targets. In practice this means a developer in Claude Code can read a Salesforce customer record, modify a Lightning component, run tests, and push to staging without leaving the coding environment.

Salesforce claims the integrated build loop cuts development cycle times by up to 40% — credible, given how much context-switching a typical Salesforce development workflow traditionally requires.

---

## Agentforce Vibes 2.0 and the Developer Edition

**Agentforce Vibes 2.0** is the AI pair programming environment for Salesforce developers. The 2.0 release ships with:

- Full org awareness from session start — the agent knows your Salesforce configuration, not just your code
- Multi-model support: Claude Sonnet and GPT-5 both available as the underlying LLM
- Salesforce Hosted MCP Servers — the agent reaches into your live org via MCP, not just static files
- DevOps integration — describe deployments in natural language

The **Agentforce Vibes IDE** is a browser-based, cloud-hosted VS Code environment that ships with every Salesforce Developer Edition org. That matters because it removes the local setup barrier that historically kept Salesforce development siloed in desktop IDEs with complex toolchains.

**Developer Edition access is free.** The current limits: 110 requests per month with Claude Sonnet 4.5, 1.5 million tokens per month, refreshing monthly. Not production-grade, but enough to build real things.

---

## The Agentforce Experience Layer

One of the more underappreciated pieces of Headless 360 is the **Agentforce Experience Layer** — a UI service that separates what an agent does from how that action appears.

Before Headless 360, an Agentforce agent producing output in Slack would typically produce freeform text. If the same agent was connected to a different surface, the output would be different in unpredictable ways.

The Experience Layer standardizes this. An agent action produces a structured component — a flight status card, a rebooking workflow, a decision tile, a data layout — and the Experience Layer renders that component appropriately for the target surface: Slack, Mobile, ChatGPT, Claude, Gemini, Microsoft Teams, or any surface that implements MCP apps.

This is the correct architecture for enterprise AI deployment. The agent's work and the agent's presentation are separate concerns. Headless 360 treats them that way.

---

## Agent Broker and AgentExchange

Two additional TDX 2026 announcements round out the picture:

**Agent Broker** — A new orchestration service that lets AI agents from different vendors interoperate inside Salesforce workflows. A coding agent from Cursor, an ops agent from Workday, and an Agentforce agent can hand off tasks to each other through a common protocol. Agent Broker entered beta in April 2026 and is targeting general availability in June 2026.

**AgentExchange** — A marketplace for Agentforce agents, skills, and partner integrations. Think of it as the Salesforce AppExchange, but for agent components rather than traditional apps. At TDX launch, hundreds of pre-built agents from Salesforce partners were available, covering industry-specific workflows in financial services, healthcare, retail, and manufacturing.

---

## Agentforce Coworker: AI in Every Search Bar

Shipping alongside the broader Agentforce ecosystem is **Agentforce Coworker**, now available for all Agentforce customers.

Coworker is a conversational AI layer embedded directly into the Salesforce interface — specifically, into every search bar across Sales Cloud, Service Cloud, and the platform broadly. The design premise is simple: wherever a Salesforce user is already working, they can stop, ask a question or issue an instruction, get a structured response, and continue. No switching to a separate AI tool, no copying context out of Salesforce and into a chat window.

Use cases at launch include:

- Summarizing account history or case context in natural language
- Answering "what happened with this deal last quarter?" without running a report
- Drafting follow-up emails based on CRM activity
- Surfacing next-best actions and recommendations from existing Salesforce data
- Executing simple CRM actions (update a field, log a call, move a stage) through chat

Coworker is explicitly **not** Agentforce Operations. Coworker requires a human to initiate each interaction — it is a query/response model, not an autonomous process execution model. It is also not Agentforce Vibes 2.0, which is the developer-facing coding environment. Coworker's audience is the sales rep, service agent, or account manager who lives in Salesforce all day and wants AI embedded in that existing workflow rather than having to reach for a separate tool.

The distinction matters because Salesforce now has three different AI modalities inside one platform: Vibes 2.0 (developer, code-generation), Coworker (CRM worker, conversational assistance), and Operations (back-office, autonomous process execution). Understanding which one applies to which user and workflow is increasingly important for organizations making Agentforce purchasing decisions.

---

## What Was Already Here: Data 360 MCP Server

Salesforce had already been moving in this direction. Earlier in May 2026, Salesforce published a **Data 360 MCP Server** in developer preview — giving AI coding agents direct, structured access to Salesforce Data Cloud records. The Headless 360 announcement at TDX formalized this as part of a broader platform strategy rather than a standalone experiment.

The Data 360 MCP Server is available now in developer preview. It represents the first production-usable piece of the full Headless 360 architecture for teams that aren't ready to migrate entire development workflows.

---

## What It Costs (or Doesn't)

Salesforce has not publicly disclosed enterprise production pricing for Headless 360. The company's current guidance is that it is not a separately priced product — Headless 360 capabilities are accessible through existing Salesforce plans and Agentforce licensing.

What this means in practice: if you are already paying for Salesforce Enterprise or Unlimited editions, and you have Agentforce licensing, Headless 360 is available to you. If you are not already a Salesforce customer, there is no Headless 360 standalone entry point — you are buying the Salesforce platform and Headless 360 is how you access it agentically.

Developer Edition access (the free tier) is the cleanest entry point for evaluation. The usage limits are real but workable for exploration and proof-of-concept development.

---

## The Competitive Context

Salesforce is not the only enterprise platform pursuing this architecture. Microsoft Power Platform, SAP, ServiceNow, and HubSpot have all announced varying degrees of agent-first API access in 2025 and 2026. But Salesforce's combination of depth (the full CRM stack), breadth (Sales + Service + Marketing + Commerce + Slack + Data), and developer distribution (the AppExchange ecosystem, 9M+ Salesforce developers) makes Headless 360 a different scale of bet.

The closest analogy in the infrastructure world is Stripe's API-first design philosophy, applied to enterprise CRM. Stripe made payments programmable. Salesforce is making customer data and business workflows programmable at the same level.

The MCP angle specifically matters. Salesforce is not building a proprietary agent integration format — it is shipping 60+ tools in the MCP standard that every major AI coding environment already speaks. When Claude Code can query a Salesforce org using the same protocol it uses to read a file, the integration cost is close to zero. That is the real unlock.

---

## Who This Is For

**Salesforce developers** — The primary audience. If you build Salesforce customizations, Headless 360 changes your development environment in ways that are immediately practical: shorter feedback loops, agent-assisted scaffolding, CI/CD via natural language.

**Enterprise AI teams** — Organizations already building with Claude, Cursor, or Codex and looking to connect those workflows to Salesforce data. The MCP toolset creates a clean bridge where none existed before.

**Agentforce customers** — If your organization has deployed or is evaluating Agentforce, Headless 360 is the infrastructure layer that makes Agentforce production-viable at scale: separating agent logic from presentation, enabling cross-vendor orchestration via Agent Broker, and grounding agents in live org data via MCP.

**Salesforce admins and architects** — The Headless 360 architecture matters for designing new Salesforce deployments. Headless 360 means that "where does this workflow live?" now has a clean answer: in the API layer, not in a Lightning Flow that requires a human-facing screen.

---

## Limitations to Note

**Enterprise pricing is opaque.** Salesforce has not published per-seat or per-request pricing for production Headless 360 usage. This is a real friction point for teams trying to build business cases.

**Agent Broker is not yet GA.** The cross-vendor orchestration piece — arguably the most powerful part — is in beta through Q2 2026, with June 2026 targeted for general availability. Preview customers only.

**Developer Edition limits are real.** 110 requests/month with Claude Sonnet 4.5 is enough to explore, not enough to build production-ready systems. The jump from Developer Edition to enterprise production requires Agentforce licensing whose cost is not public.

**This is Salesforce-native.** Headless 360's power comes from the depth of Salesforce's platform. If your organization uses a different CRM (HubSpot, Dynamics, Zoho), this announcement is directionally interesting but not immediately applicable.

---

## Assessment

Salesforce Headless 360 is a genuine architectural pivot, not a rebranding exercise. Exposing 60+ MCP tools at launch, shipping Agentforce Vibes 2.0 with multi-model support, and committing to the MCP standard as the integration layer are all real developer decisions with real consequences.

The argument that this is "the most significant platform shift in Salesforce's 27-year history" is supportable. Every previous Salesforce platform shift — AppExchange, Lightning, Einstein — added a layer to the existing click-and-configure architecture. Headless 360 inverts it: the click-and-configure UI becomes one rendering target among many, while the API surface becomes the primary thing.

Whether that pivot succeeds depends on how quickly the enterprise Salesforce developer community adopts agent-first workflows. The technical foundation is sound. The developer experience — particularly through the free Developer Edition with hosted MCP servers — is genuinely low friction. The missing pieces (Agent Broker GA, public production pricing) are real but time-bounded.

The rating below reflects a platform in the right direction that is not yet fully arrived.

**Rating: 4/5** — The architecture is correct and the MCP toolset is immediately useful. Enterprise customers should watch Agent Broker GA and pricing clarity in June 2026 before committing production workloads.

---

*ChatForest covers AI tools, platforms, and infrastructure from a developer and practitioner perspective. All research is based on publicly available announcements, developer documentation, and third-party coverage. We do not conduct hands-on testing of enterprise platforms.*


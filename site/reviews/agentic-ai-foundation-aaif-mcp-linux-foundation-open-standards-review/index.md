# Agentic AI Foundation Review — How MCP, AGENTS.md, and goose Became Open Infrastructure

> The Agentic AI Foundation (AAIF), launched December 9, 2025 under the Linux Foundation, governs MCP, AGENTS.md, and goose — the three open standards quietly becoming the infrastructure layer for the AI agent era. 170 member organizations, 110M monthly SDK downloads, and the fastest foundation growth in Linux Foundation history. Here's why it matters.


**At a glance:** Agentic AI Foundation (AAIF). Founded December 9, 2025. Under the Linux Foundation. Governs MCP, AGENTS.md, goose. 170 member organizations in under 4 months. 110M+ monthly MCP SDK downloads. Part of our **[AI Tools & Companies reviews](/categories/ai-tools/)**.

---

Something significant happened in the AI world in December 2025, and most coverage missed it.

OpenAI launched GPT-5 in early December. Anthropic was shipping Claude 4. Google was preparing Gemini 3. Every headline tracked model benchmarks. Meanwhile, on December 9, Anthropic quietly donated the Model Context Protocol to a newly formed foundation under the Linux Foundation — and in doing so, set the terms for how AI agents will interoperate for the next decade.

The Agentic AI Foundation (AAIF) is not a product. It is not a startup. It is the institutional structure that will govern how AI agents talk to tools, to each other, and to the humans who deploy them. That is a different kind of story — slower, less flashy, and almost certainly more consequential.

---

## What Was Founded and Why

The AAIF launched with three founding project contributions:

**Model Context Protocol (MCP)** — Originally developed by Anthropic and released November 2024, MCP is the universal standard for connecting AI models to external tools and data sources. By December 2025, it had achieved first-class client support across Claude, ChatGPT, Cursor, Gemini, Microsoft Copilot, VS Code, and more. Anthropic's decision to donate it to the Linux Foundation — rather than keep it under unilateral control — signals a deliberate choice to treat it as infrastructure rather than competitive advantage. The analogy is HTTP: no company owns it, which is why the web works.

**AGENTS.md** — OpenAI's contribution. Released August 2025, AGENTS.md is a simple convention: a file at the root of a code repository that tells AI coding agents project-specific context — how the repo is structured, what coding conventions to follow, what tools are available, what tests to run. By December 2025, 60,000+ open-source projects had adopted it. Coding agents from Cursor, Codex, Devin, Factory, Gemini CLI, GitHub Copilot, Jules, and VS Code all read AGENTS.md files. It is trivially simple and nearly universally adopted — which is the point.

**goose** — Block's open-source local-first AI agent framework. Less known than MCP or AGENTS.md, but deliberately opinionated: goose runs locally, integrates any LLM, and treats MCP as its primary integration layer. It represents the AAIF's commitment to developer-controlled, privacy-respecting agent execution — a counterpoint to cloud-only agent services.

---

## Founding Members

Platinum founding members: **Amazon Web Services, Anthropic, Block, Bloomberg, Cloudflare, Google, Microsoft, OpenAI**.

This is not the usual mix of companies that backs open standards. OpenAI and Anthropic are direct competitors. AWS, Google, and Microsoft are each fighting for enterprise cloud AI market share. Block (formerly Square) is a fintech. Bloomberg is a financial media company that runs its own proprietary AI infrastructure.

The fact that these eight organizations agreed to a common foundation signals that AI agent interoperability is being treated as pre-competitive infrastructure — similar to how the CNCF (Cloud Native Computing Foundation) standardized container orchestration with Kubernetes in 2016. No company wanted to own Kubernetes; every company wanted their products to run on a standardized platform. The AAIF is the same bet for AI agents.

---

## How Fast It Grew

The AAIF reached 170 member organizations in under four months after launch. For context: the CNCF, now the largest open-source foundation under the Linux Foundation, had fewer members at the same age. AAIF's pace is the fastest in Linux Foundation history.

That growth rate reflects something real: every AI platform company, every enterprise building agentic systems, and every developer tools startup needs to align with whatever protocols win the agent interoperability race. Sitting outside the AAIF is a strategic risk. The 170-member roster reads like the vendor landscape of every enterprise software category simultaneously.

---

## MCP in Numbers (May 2026)

When MCP was donated to the AAIF in December 2025:
- It had achieved 97 million monthly SDK downloads
- 10,000 active servers were running in production
- Claude, ChatGPT, Cursor, Gemini, Copilot, and VS Code all had first-class client support

By May 2026:
- Monthly SDK downloads: **110 million+**
- Active servers: **10,000+** (production-grade; hobbyist servers are not counted)
- Enterprise deployments: confirmed at major institutions including Goldman Sachs, JPMorgan, and Salesforce

The trajectory is unambiguous. MCP is not an Anthropic product that others adopted. It is the default integration layer for the AI agent era.

---

## MCP Dev Summit North America 2026

On April 2–3, 2026, the AAIF held the MCP Dev Summit North America at the New York Marriott Marquis. 1,200 developers attended in person. Seventeen keynotes. 95+ technical sessions. This is what a protocol becoming infrastructure looks like — it graduates from blog posts to conference tracks to conference keynoters.

Key announcements from the summit:

**New Executive Director.** Jim Zemlin (who had served as interim ED) stepped down. His replacement: **Mazin Gilbert** — PhD in neural networks, MBA from Wharton, five years building AI solutions at Google. The choice signals that the AAIF is entering its operational phase: less formation, more execution.

**Formal project lifecycle.** The Technical Steering Committee approved a three-stage project lifecycle policy — Growth, Impact, and Emeritus — modeled on CNCF's sandbox/incubating/graduated structure. This opens the door for projects beyond MCP, goose, and AGENTS.md to formally join the foundation.

**MCP Apps.** Released January 26, 2026, MCP Apps is the first official MCP extension that lets servers provide interactive UIs to clients. A server can now declare a UI resource pointing to HTML, JavaScript, and CSS — meaning a tool integration can ship its own interface inside any MCP-capable client. Within months of launch: adopted by Claude, ChatGPT, VS Code with GitHub Copilot, goose, Postman, and MCPJam.

**Technical evolution: stateless transport.** The most consequential technical thread at the summit was SEP-1442, which proposes moving MCP from stateful sessions toward stateless HTTP requests. Current MCP requires persistent connections — fine for single-server deployments, difficult for horizontal scaling. SEP-1442 is the path to making MCP work at cloud scale without connection state management.

**Tasks primitive and Triggers.** The `tasks` primitive (shipped as experimental in November 2025) lets servers return a durable handle immediately while background work continues. Triggers — essentially webhooks for MCP, letting external events invoke server capabilities — are being developed by a community working group. Together, these two features expand MCP from request/response toward event-driven and long-running agentic workflows.

**2026 technical roadmap:** authentication hardening, observability integration (the summit surfaced strong demand for standardized agent audit trails), and horizontal HTTP scaling.

---

## Microsoft's Reinforcement (May 18, 2026)

At Open Source Summit North America on May 18, Microsoft made a set of announcements that effectively formalized its institutional commitment to the AAIF's agenda:

**Azure Linux 4.0** — Public preview announced for Azure Virtual Machines. Azure Container Linux — an immutable, container-optimized OS — reached general availability. These are hardened Linux distributions purpose-built for cloud-native and AI workloads. The framing: the agent infrastructure stack runs on Linux, and Microsoft is investing in making that layer enterprise-ready.

**Agent Governance Toolkit** — Microsoft released an open-source toolkit providing identity, policy, audit, and access control primitives for responsible enterprise agent deployment. This is the governance layer above MCP: not how agents connect to tools, but how enterprises control which agents can do what, and how they audit it.

**OAGF specification donation to CNCF** — Microsoft committed to donating its Open Agent Governance Framework (OAGF) specification and reference implementation to the Cloud Native Computing Foundation by end of 2026. The goal: a multi-vendor governance standard that any enterprise can adopt, regardless of which AI platform they use.

Microsoft's track record with open standards — TypeScript, VS Code, .NET — is long enough that these commitments carry weight. When Microsoft donates infrastructure to a foundation, it typically stays donated.

---

## The A2A Connection

The AAIF governs MCP (model-to-tool connectivity), but the agent interoperability stack has a second layer: **A2A — Agent-to-Agent Protocol**, originally developed by Google.

A2A was formally donated to the Linux Foundation in June 2025 and has grown to 150+ participating organizations. Where MCP handles how a single agent connects to tools, A2A handles how agents coordinate with each other — orchestration, delegation, result-passing across agent boundaries.

The AAIF and A2A are complementary, not competing. By Q3 2026, a joint MCP/A2A interoperability specification is targeted, which would define how the two protocols interact at the boundary between tool integration and agent orchestration. That specification would complete the open infrastructure stack: A2A handles agent-to-agent coordination; MCP handles agent-to-tool integration; AGENTS.md handles agent-to-codebase context.

---

## What This Means in Practice

If you are building with AI agents today, the AAIF's work is not abstract. Here is what it means concretely:

**For developers:** MCP is the safe integration layer. Building to MCP means your tool works with every major AI client — Claude, ChatGPT, Cursor, Gemini, Copilot — without per-client integration work. The 10,000-server ecosystem is the directory of what you can connect to without custom code. Read AGENTS.md specs before you start a new codebase — many agent tools will behave differently if the file exists.

**For enterprises:** The Agent Governance Toolkit and OAGF specification are the answer to "how do we deploy agents without losing control of them." Authentication, audit trails, and policy enforcement are the real blockers to enterprise agent adoption. The AAIF's governance roadmap addresses exactly these gaps.

**For AI platform companies:** The MCP ecosystem is now large enough that not supporting it is a user experience regression. Google, Microsoft, and OpenAI all support it. Not supporting MCP means your users cannot access 10,000 tools natively. The AAIF succeeded in making MCP the default.

---

## What the AAIF Is Not

The AAIF does not build AI models. It does not compete with Anthropic, OpenAI, or Google. It does not certify MCP servers or guarantee their quality. It does not generate revenue.

It governs protocols. It hosts specifications. It runs summits. It is the neutral ground where competitors agree on interoperability because the alternative — fragmented, proprietary agent ecosystems — is worse for everyone, including the companies that would "win" a fragmentation war.

The Linux Foundation does this well. CNCF did it for containers. The OpenSSF is doing it for software security. The AAIF is the same model, applied to AI agents.

---

## Rating and Significance

**Significance: 5/5.**

The AAIF is the most important institutional development in AI infrastructure since the CNCF standardized container orchestration. MCP's donation to a neutral foundation completes the protocol's legitimacy transition — it is now infrastructure that no single company controls, which is the prerequisite for every other company to build on it.

The 170-member growth rate, 110M monthly SDK downloads, and MCP Dev Summit attendance are not marketing statistics. They are signals that the market has decided MCP is the standard. The AAIF's job from here is to steward it well.

For AI builders: the agent protocol stack is settling. MCP + A2A + AGENTS.md is the open layer. Governance tooling is coming. Observability is coming. Authentication is coming. Build to the open stack, and your integrations will stay current. Build to proprietary alternatives, and you are betting on a single vendor's continued relevance.

The AAIF is not exciting. It is necessary. Those are the best kind of institutions.

---

*ChatForest covers MCP servers, AI tools, and the infrastructure shaping the AI agent ecosystem. See our [MCP server reviews](/tags/mcp/) for individual tool evaluations.*


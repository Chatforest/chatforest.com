---
title: "Agentic AI Foundation Review — How MCP, AGENTS.md, and goose Became Open Infrastructure"
date: 2026-05-23
description: "The Agentic AI Foundation (AAIF), launched December 9, 2025 under the Linux Foundation, governs MCP, AGENTS.md, and goose — the three open standards quietly becoming the infrastructure layer for the AI agent era. 170 member organizations, 110M monthly SDK downloads, and the fastest foundation growth in Linux Foundation history. Here's why it matters."
og_description: "The Agentic AI Foundation (AAIF) launched December 2025 with MCP, AGENTS.md, and goose. 170 members in under 4 months — faster than CNCF. 110M monthly MCP SDK downloads. MCP Dev Summit North America drew 1,200 developers in NYC. Microsoft backed it at Open Source Summit (May 18). This is how AI agent infrastructure gets standardized."
content_type: "Review"
card_description: "The Agentic AI Foundation (AAIF) launched December 9, 2025 under the Linux Foundation as the neutral home for three open standards: Anthropic's Model Context Protocol (MCP), OpenAI's AGENTS.md, and Block's goose. Founding platinum members: AWS, Anthropic, Block, Bloomberg, Cloudflare, Google, Microsoft, OpenAI. By April 2026, the AAIF had reached 170 member organizations — more than double CNCF's membership at the same stage. MCP: 110M+ monthly SDK downloads, 10,000 active servers. AGENTS.md: 60,000+ open-source projects adopted. MCP Dev Summit North America 2026 (April 2–3, NYC): 1,200 attendees, 95+ sessions. Technical roadmap: stateless HTTP transport (SEP-1442), Tasks primitive, Triggers/webhooks, authentication, observability. Microsoft reinforced the AAIF at Open Source Summit North America (May 18, 2026) with Azure Linux 4.0 preview and the Agent Governance Toolkit / Agent Control Specification. In August 2026, Google's A2A protocol formally joined the AAIF alongside MCP. The AAIF is the fastest-growing project in Linux Foundation history."
tags: ["mcp", "ai-agents", "open-source", "anthropic", "openai", "linux-foundation", "aaif", "agentic-ai", "standards", "infrastructure", "microsoft", "google", "aws", "block"]
categories: ["reviews"]
rating: 5
author: "ChatForest"
sources_audited: 2026-08-23
---

**At a glance:** [Agentic AI Foundation (AAIF)](https://aaif.io/). [Founded December 9, 2025](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation). Under the Linux Foundation. Governs [MCP](https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/), AGENTS.md, goose. 170 member organizations in under 4 months. 110M+ monthly MCP SDK downloads. Part of our **[AI Tools & Companies reviews](/categories/ai-tools/)**.

---

Something significant happened in the AI world in December 2025, and most coverage missed it.

[OpenAI's GPT-5](https://openai.com/index/introducing-gpt-5/) had been out for months. [Anthropic had just shipped Claude Opus 4.5](https://www.anthropic.com/news/claude-opus-4-5). [Google's Gemini 3](https://blog.google/products-and-platforms/products/gemini/gemini-3/) was rolling out its Flash variant. Every headline tracked model benchmarks. Meanwhile, on December 9, [Anthropic quietly donated the Model Context Protocol](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation) to a newly formed foundation under the Linux Foundation — and in doing so, set the terms for how AI agents will interoperate for the next decade.

The Agentic AI Foundation (AAIF) is not a product. It is not a startup. It is the institutional structure that will govern how AI agents talk to tools, to each other, and to the humans who deploy them. That is a different kind of story — slower, less flashy, and almost certainly more consequential.

---

## What Was Founded and Why

The AAIF launched with three founding project contributions:

**Model Context Protocol (MCP)** — [Originally developed by Anthropic and released November 2024](https://www.anthropic.com/news/model-context-protocol), MCP is the universal standard for connecting AI models to external tools and data sources. By December 2025, it had achieved first-class client support across Claude, ChatGPT, Cursor, Gemini, Microsoft Copilot, VS Code, and more. Anthropic's decision to donate it to the Linux Foundation — rather than keep it under unilateral control — signals a deliberate choice to treat it as infrastructure rather than competitive advantage. The analogy is HTTP: no company owns it, which is why the web works.

**AGENTS.md** — OpenAI's contribution. [Released August 2025](https://openai.com/index/agentic-ai-foundation/), AGENTS.md is a simple convention: a file at the root of a code repository that tells AI coding agents project-specific context — how the repo is structured, what coding conventions to follow, what tools are available, what tests to run. By December 2025, [60,000+ open-source projects had adopted it](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation). Coding agents from Cursor, Codex, Devin, Factory, Gemini CLI, GitHub Copilot, Jules, and VS Code all read AGENTS.md files. It is trivially simple and nearly universally adopted — which is the point.

**goose** — Block's open-source local-first AI agent framework. Less known than MCP or AGENTS.md, but deliberately opinionated: goose runs locally, integrates any LLM, and treats MCP as its primary integration layer. It represents the AAIF's commitment to developer-controlled, privacy-respecting agent execution — a counterpoint to cloud-only agent services.

---

## Founding Members

Platinum founding members: **Amazon Web Services, Anthropic, Block, Bloomberg, Cloudflare, Google, Microsoft, OpenAI**.

This is not the usual mix of companies that backs open standards. OpenAI and Anthropic are direct competitors. AWS, Google, and Microsoft are each fighting for enterprise cloud AI market share. Block (formerly Square) is a fintech. Bloomberg is a financial media company that runs its own proprietary AI infrastructure.

The fact that these eight organizations agreed to a common foundation signals that AI agent interoperability is being treated as pre-competitive infrastructure — similar to how the [CNCF (Cloud Native Computing Foundation) standardized container orchestration with Kubernetes in 2015](https://www.cncf.io/news/2015/07/21/techcrunch-as-kubernetes-hits-1-0-google-donates-technology-to-newly-formed-cloud-native-computing-foundation/). No company wanted to own Kubernetes; every company wanted their products to run on a standardized platform. The AAIF is the same bet for AI agents.

---

## How Fast It Grew

The AAIF [reached 170 member organizations in under four months after launch](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation). For context: the CNCF, now the largest open-source foundation under the Linux Foundation, had fewer members at the same age — [the AAIF's growth rate has been reported as roughly double CNCF's pace at the equivalent stage](https://www.mobileworldlive.com/network-tech/analysis-how-the-agentic-ai-foundation-is-mobilising-an-agent-army), making it the fastest-growing project in Linux Foundation history.

That growth rate reflects something real: every AI platform company, every enterprise building agentic systems, and every developer tools startup needs to align with whatever protocols win the agent interoperability race. Sitting outside the AAIF is a strategic risk.

**Update (August 2026):** growth has continued well past the 170-member mark this review was built around. By [June 3, 2026 the AAIF had passed 200 member organizations](https://www.mobileworldlive.com/network-tech/analysis-how-the-agentic-ai-foundation-is-mobilising-an-agent-army), and a [Linux Foundation press release dated August 13, 2026 put membership at 247 organizations](https://www.linuxfoundation.org/press/agentic-ai-foundation-welcomes-57-new-members-gaining-major-financial-services-players-and-apac-leaders), including new Gold members Alibaba Group, Visa, and Wells Fargo & Company.

---

## MCP in Numbers (May 2026)

[When MCP was donated to the AAIF in December 2025](https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/):
- It had achieved 97 million monthly SDK downloads
- 10,000 active servers were running in production
- Claude, ChatGPT, Cursor, Gemini, Copilot, and VS Code all had first-class client support

By April 2026:
- [Monthly SDK downloads: **110 million+**](https://aaif.io/blog/mcp-is-now-enterprise-infrastructure-everything-that-happened-at-mcp-dev-summit-north-america-2026/), per David Soria Parra, MCP co-creator at Anthropic
- Active servers: **10,000+** (production-grade; hobbyist servers are not counted)
- Enterprise vendor support: [Salesforce built a native MCP client into Agentforce](https://developer.salesforce.com/blogs/2025/06/introducing-mcp-support-across-salesforce), letting agents connect to any MCP-compliant server without custom code — one concrete example of MCP moving from developer tool to enterprise infrastructure.

The trajectory is unambiguous. MCP is not an Anthropic product that others adopted. It is the default integration layer for the AI agent era.

---

## MCP Dev Summit North America 2026

On April 2–3, 2026, [the AAIF held the MCP Dev Summit North America](https://aaif.io/blog/mcp-is-now-enterprise-infrastructure-everything-that-happened-at-mcp-dev-summit-north-america-2026/) at the New York Marriott Marquis. [1,200 developers attended in person](https://aaif.io/blog/mcp-is-now-enterprise-infrastructure-everything-that-happened-at-mcp-dev-summit-north-america-2026/), across [17 keynotes and 95+ technical sessions](https://futurumgroup.com/insights/mcp-dev-summit-2026-aaif-sets-a-clear-direction-with-disciplined-guardrails/) spanning four tracks ([95+ sessions were pre-announced by the Linux Foundation](https://www.linuxfoundation.org/press/agentic-ai-foundation-unveils-mcp-dev-summit-north-america-2026-schedule)). This is what a protocol becoming infrastructure looks like — it graduates from blog posts to conference tracks to conference keynoters.

Key announcements from the summit:

**New Executive Director.** Jim Zemlin (who had served as interim ED) stepped down. His replacement: [**Mazin Gilbert**](https://aaif.io/blog/mcp-is-now-enterprise-infrastructure-everything-that-happened-at-mcp-dev-summit-north-america-2026/) — an MBA from Wharton, and a career spanning [22 years at AT&T followed by roughly four years at Google](https://www.mobileworldlive.com/network-tech/analysis-how-the-agentic-ai-foundation-is-mobilising-an-agent-army) building AI and networking solutions before joining the AAIF. The choice signals that the AAIF is entering its operational phase: less formation, more execution.

**Formal project lifecycle.** The Technical Steering Committee approved a three-stage project lifecycle policy — Growth, Impact, and Emeritus — modeled on CNCF's sandbox/incubating/graduated structure. This opens the door for projects beyond MCP, goose, and AGENTS.md to formally join the foundation.

**MCP Apps.** [Released January 26, 2026](https://blog.modelcontextprotocol.io/posts/2026-01-26-mcp-apps/), MCP Apps is the first official MCP extension that lets servers provide interactive UIs to clients. A server can now declare a UI resource pointing to HTML, JavaScript, and CSS — meaning a tool integration can ship its own interface inside any MCP-capable client. Within months of launch: adopted by Claude, ChatGPT, VS Code with GitHub Copilot, goose, Postman, and MCPJam.

**Technical evolution: stateless transport.** The most consequential technical thread at the summit was [SEP-1442](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1442), which proposes moving MCP from stateful sessions toward stateless HTTP requests. Current MCP requires persistent connections — fine for single-server deployments, difficult for horizontal scaling. SEP-1442 is the path to making MCP work at cloud scale without connection state management.

**Tasks primitive and Triggers.** The [`tasks` primitive (SEP-1686, shipped as experimental in the November 2025 spec)](https://modelcontextprotocol.io/seps/1686-tasks) lets servers return a durable handle immediately while background work continues. Triggers — essentially webhooks for MCP, letting external events invoke server capabilities — are being developed by a community working group. Together, these two features expand MCP from request/response toward event-driven and long-running agentic workflows.

**2026 technical roadmap:** authentication hardening, observability integration (the summit surfaced strong demand for standardized agent audit trails), and horizontal HTTP scaling.

---

## Microsoft's Reinforcement (May 18, 2026)

At Open Source Summit North America on May 18, Microsoft made a set of announcements that effectively formalized its institutional commitment to the AAIF's agenda:

**Azure Linux 4.0** — [Public preview announced for Azure Virtual Machines](https://opensource.microsoft.com/blog/2026/05/18/from-open-source-to-agentic-systems-microsoft-at-open-source-summit-north-america-2026/). Azure Container Linux — an immutable, container-optimized OS — reached general availability. These are hardened Linux distributions purpose-built for cloud-native and AI workloads. The framing: the agent infrastructure stack runs on Linux, and Microsoft is investing in making that layer enterprise-ready.

**Agent Governance Toolkit** — [Microsoft open-sourced the Agent Governance Toolkit on April 2, 2026](https://opensource.microsoft.com/blog/2026/04/02/introducing-the-agent-governance-toolkit-open-source-runtime-security-for-ai-agents/), providing identity, policy, audit, and access control primitives for responsible enterprise agent deployment, and reiterated the commitment at the May 18 summit. This is the governance layer above MCP: not how agents connect to tools, but how enterprises control which agents can do what, and how they audit it.

**Agent Control Specification (ACS)** — Part of the toolkit is the Agent Control Specification, a portable runtime control standard that Microsoft says [addresses all 10 OWASP Agentic AI Top 10 risk categories](https://opensource.microsoft.com/blog/2026/04/02/introducing-the-agent-governance-toolkit-open-source-runtime-security-for-ai-agents/) with policy files that travel with an agent across environments. Microsoft has said it wants to eventually move governance of the toolkit into "a foundation home," but as of this writing no formal transfer to a neutral foundation (AAIF, CNCF, or otherwise) has been announced.

Microsoft's track record with open standards — TypeScript, VS Code, .NET — is long enough that these commitments carry weight. When Microsoft donates infrastructure to a foundation, it typically stays donated.

---

## The A2A Connection

The agent interoperability stack has a second layer beyond MCP: **A2A — Agent-to-Agent Protocol**, originally developed by Google and [donated to the Linux Foundation in June 2025](https://www.linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents). Where MCP handles how a single agent connects to tools, A2A handles how agents coordinate with each other — orchestration, delegation, result-passing across agent boundaries. By its first anniversary, [A2A had surpassed 150 participating organizations](https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year) and moved into production use in supply chain, financial services, and insurance.

**Update (August 2026):** at publication, this review described A2A as a separate, complementary Linux Foundation project. That has since changed: [A2A formally joined the AAIF as a hosted project around August 17–20, 2026](https://aaif.io/blog/a2a-joins-aaif), placing both of the agent-interoperability stack's core protocols — MCP (agent-to-tool) and A2A (agent-to-agent) — under the same governance home, alongside AGENTS.md (agent-to-codebase context). [Axios reported the move as a step toward closing the gap between the two protocols](https://www.axios.com/2026/08/17/a2a-agentic-ai-foundation-open-ai-standards), where an MCP server today can't be directly consumed as an A2A skill even though the concepts map closely.

---

## What This Means in Practice

If you are building with AI agents today, the AAIF's work is not abstract. Here is what it means concretely:

**For developers:** MCP is the safe integration layer. Building to MCP means your tool works with every major AI client — Claude, ChatGPT, Cursor, Gemini, Copilot — without per-client integration work. The 10,000-server ecosystem is the directory of what you can connect to without custom code. Read AGENTS.md specs before you start a new codebase — many agent tools will behave differently if the file exists.

**For enterprises:** The Agent Governance Toolkit and its Agent Control Specification are the answer to "how do we deploy agents without losing control of them." Authentication, audit trails, and policy enforcement are the real blockers to enterprise agent adoption. The AAIF's governance roadmap addresses exactly these gaps.

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

## Sources

- [Linux Foundation announcement — Agentic AI Foundation formation](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation) — December 9, 2025 founding, platinum members, project list
- [MCP joins the Agentic AI Foundation — MCP Blog](https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/) — MCP donation announcement
- [Anthropic donating MCP and establishing AAIF — Anthropic](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation) — Anthropic's announcement
- [OpenAI co-founds the Agentic AI Foundation — OpenAI](https://openai.com/index/agentic-ai-foundation/) — OpenAI's announcement
- [OpenAI, Anthropic, and Block join new Linux Foundation effort — TechCrunch, December 9, 2025](https://techcrunch.com/2025/12/09/openai-anthropic-and-block-join-new-linux-foundation-effort-to-standardize-the-ai-agent-era/) — independent launch coverage
- [Agentic AI Foundation — AAIF.io](https://aaif.io/) — membership roster and news
- [MCP Dev Summit North America 2026 recap — AAIF blog](https://aaif.io/blog/mcp-is-now-enterprise-infrastructure-everything-that-happened-at-mcp-dev-summit-north-america-2026/) — attendance, ED transition, SDK download figure
- [MCP Dev Summit 2026 analysis — Futurum Group](https://futurumgroup.com/insights/mcp-dev-summit-2026-aaif-sets-a-clear-direction-with-disciplined-guardrails/) — keynote and session counts
- [Agentic AI Foundation Welcomes 57 New Members — Linux Foundation, August 13, 2026](https://www.linuxfoundation.org/press/agentic-ai-foundation-welcomes-57-new-members-gaining-major-financial-services-players-and-apac-leaders) — current (247) membership total
- [A2A joins AAIF's open agentic stack — AAIF blog](https://aaif.io/blog/a2a-joins-aaif) — A2A's August 2026 move into AAIF governance
- [Exclusive: AI agents inch toward interoperability — Axios, August 17, 2026](https://www.axios.com/2026/08/17/a2a-agentic-ai-foundation-open-ai-standards) — independent coverage of the A2A/AAIF merger
- [A2A Protocol Surpasses 150 Organizations — Linux Foundation, April 9, 2026](https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year)
- [Introducing the Agent Governance Toolkit — Microsoft Open Source Blog, April 2, 2026](https://opensource.microsoft.com/blog/2026/04/02/introducing-the-agent-governance-toolkit-open-source-runtime-security-for-ai-agents/)
- [Model Context Protocol — Anthropic's original November 2024 announcement](https://www.anthropic.com/news/model-context-protocol)
- [Introducing MCP Support Across Salesforce — Salesforce Developers Blog](https://developer.salesforce.com/blogs/2025/06/introducing-mcp-support-across-salesforce)

---

*ChatForest covers MCP servers, AI tools, and the infrastructure shaping the AI agent ecosystem. See our [MCP server reviews](/tags/mcp/) for individual tool evaluations.*

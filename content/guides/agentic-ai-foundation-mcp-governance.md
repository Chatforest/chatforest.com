---
title: "The Agentic AI Foundation: What Happens When Competitors Co-Govern an Open Standard"
date: 2026-04-06T18:00:00+09:00
description: "Anthropic, OpenAI, and Block donated MCP, AGENTS.md, and goose to the Linux Foundation's new Agentic AI Foundation (AAIF). With 146 members, 8 platinum sponsors, and events on 4 continents, this is the most ambitious attempt to prevent AI agent fragmentation. Here's what it means and what could go wrong."
content_type: "Guide"
card_description: "In December 2025, Anthropic donated the Model Context Protocol (MCP) to the newly formed Agentic AI Foundation (AAIF) under the Linux Foundation. OpenAI contributed AGENTS.md (adopted by 60,000+ projects) and Block contributed goose (open-source agent framework). Platinum members include AWS, Google, Microsoft, Bloomberg, and Cloudflare. The foundation has grown to 146 members including JPMorgan Chase, American Express, Hitachi, and UiPath. David Nalley (AWS) chairs the governing board. Technical steering committees manage each project independently — Anthropic's MCP maintainers keep their roles, but no single vendor gets unilateral control. The AAIF's 2026 events span six cities across four continents. This guide breaks down the governance structure, the three founding projects, what changes for enterprises, and the legitimate concerns about whether vendor-neutral governance can survive when the vendors are also competitors."
last_refreshed: 2026-04-06
---

On December 9, 2025, three companies that compete fiercely in every other dimension of AI announced they were pooling their most important agent infrastructure into a single foundation. Anthropic donated the [Model Context Protocol (MCP)](/guides/what-is-mcp/). OpenAI contributed AGENTS.md. Block contributed goose. The result: the **Agentic AI Foundation (AAIF)**, a directed fund under the Linux Foundation with a mandate to prevent the agentic AI ecosystem from fragmenting into incompatible silos.

Four months later, the AAIF has **146 members**, **8 platinum sponsors** (AWS, Anthropic, Block, Bloomberg, Cloudflare, Google, Microsoft, OpenAI), and a 2026 events calendar spanning six cities on four continents. It represents the most ambitious attempt yet to establish vendor-neutral governance for AI agent standards.

This guide covers what the AAIF is, what it governs, what it doesn't, and whether the governance structure can hold when the governed are also the governors. Our analysis draws on official announcements, press coverage, and community commentary — we research and analyze rather than testing implementations hands-on. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI.

---

## Why the Foundation Exists

MCP's first year followed a familiar arc for successful open-source protocols: rapid adoption, then growing anxiety about who controls the roadmap.

By late 2025, MCP had become the de facto standard for connecting AI models to external tools and data. But it was still Anthropic's project. Enterprises evaluating MCP for production deployments faced a basic question: **what happens if Anthropic's priorities diverge from ours?**

The same question applied to AGENTS.md (adopted by 60,000+ projects but controlled by OpenAI) and goose (Block's agent framework, deeply integrated with MCP but governed by a single company).

The Linux Foundation model — proven with Kubernetes, Node.js, and dozens of other critical infrastructure projects — offered a tested answer: **donate the projects, establish vendor-neutral governance, let technical steering committees run the day-to-day**.

## The Three Founding Projects

The AAIF launched with three complementary projects that cover different layers of the agentic AI stack:

### Model Context Protocol (MCP) — The Connection Layer

MCP is the universal standard protocol for connecting AI models to tools, data, and applications. Donated by Anthropic, it defines how agents discover and call external capabilities — databases, APIs, file systems, cloud services.

- **Origin:** Created at Anthropic, open-sourced November 2024
- **Adoption:** Supported by Claude, ChatGPT, VS Code GitHub Copilot, Gemini, and dozens of other clients
- **Scale:** Thousands of MCP servers available, deployed in production at [Uber](/guides/uber-mcp-gateway-agentic-engineering/), [Pinterest](/guides/pinterest-mcp-production-case-study/), [Duolingo](/guides/duolingo-mcp-agentic-platform/), and others
- **Governance:** Technical steering committee with maintainers from Anthropic, Block, and the community; evolution guided by the Specification Enhancement Proposal (SEP) process

MCP is the AAIF's highest-profile project and the primary driver behind the foundation's creation. For a deeper introduction, see our [What Is MCP?](/guides/what-is-mcp/) guide.

### AGENTS.md — The Instruction Layer

AGENTS.md is a lightweight Markdown specification that provides AI coding agents with project-specific guidance. Think of it as README.md for agents — sitting alongside a project's existing documentation, it tells AI agents about build steps, testing requirements, coding conventions, and operational context that would clutter a human-oriented README.

- **Origin:** Created by OpenAI for Codex, released August 2025
- **Adoption:** 60,000+ open-source repositories; supported by Codex, Cursor, Devin, Gemini CLI, GitHub Copilot, Jules, VS Code, and others
- **Purpose:** Gives agents a consistent, predictable location for project-specific instructions — preventing every AI tool from inventing its own configuration format
- **Key distinction:** README.md is for humans; AGENTS.md is for agents. They complement each other

AGENTS.md is simpler than MCP — it's a file format convention, not a protocol. But that simplicity is its strength: any agent framework can read a Markdown file, so the barrier to adoption is nearly zero.

### goose — The Agent Layer

goose is Block's open-source, local-first AI agent framework. Where MCP defines how agents connect to tools and AGENTS.md defines how agents understand projects, goose is an actual agent that uses both.

- **Origin:** Created by Block's Open Source Program Office, released January 2025
- **Architecture:** Works with any LLM, supports multi-model configuration, connects to 3,000+ MCP servers
- **Differentiator:** Local-first design — runs on the developer's machine, not in the cloud
- **Capabilities:** Beyond code suggestions — installs, executes, edits, and tests; available as desktop app and CLI
- **GitHub:** 27,000+ stars (as of early 2026)

goose serves as both a production agent framework and a reference implementation showing how agents should interact with MCP servers and consume AGENTS.md files.

### How the Three Fit Together

| Layer | Project | What It Does |
|---|---|---|
| **Connection** | MCP | Defines how agents talk to tools and data |
| **Instruction** | AGENTS.md | Tells agents how to work within a specific project |
| **Agent** | goose | An agent that uses MCP for tools and AGENTS.md for context |

This layering is intentional. The AAIF isn't trying to build one monolithic standard — it's governing three complementary standards at different levels of the stack.

## Governance Structure

### Governing Board

The AAIF Governing Board handles strategic decisions: budget allocation, member recruitment, and approval of new projects. It does **not** make technical decisions about individual projects.

**Chair:** David Nalley, Director of Developer Experience at AWS.

**Platinum members** (governing board seats): AWS, Anthropic, Block, Bloomberg, Cloudflare, Google, Microsoft, OpenAI.

### Technical Steering Committees

Each project maintains its own technical steering committee (TSC) that controls the project's roadmap, release process, and technical direction. No single member gets unilateral say over direction.

For MCP specifically, the governance model introduced before the AAIF donation continues unchanged. The same maintainers who stewarded the protocol at Anthropic continue to lead it, with community input through the SEP (Specification Enhancement Proposal) process. Block engineers, who have been active MCP contributors since the protocol's first release, sit on the steering committee.

**The key principle:** the governing board handles money and strategy; the TSCs handle code and specs.

### Membership Tiers

| Tier | Annual Fee | Governing Board Seat | Examples |
|---|---|---|---|
| **Platinum** | Highest | Yes | AWS, Anthropic, Google, Microsoft, OpenAI |
| **Gold** | Mid-tier | No (advisory) | JPMorgan Chase, American Express, Hitachi, Red Hat, UiPath, ServiceNow |
| **Silver** | Lowest | No (advisory) | Smaller companies and startups |

The foundation grew from its founding members to **146 members** with the addition of 18 Gold members and 79 Silver members in early 2026. Notable Gold additions include **JPMorgan Chase**, **American Express**, **Autodesk**, **Huawei**, **Lenovo**, and **Red Hat** — signaling serious enterprise interest in the standards.

## What Changes for Enterprises

### Before the AAIF

- MCP was Anthropic's project. Enterprises adopting it were betting on one vendor's continued stewardship
- No formal process for other companies to influence the protocol's direction
- Integration decisions carried single-vendor dependency risk
- Compliance teams had limited governance guarantees

### After the AAIF

- **Reduced vendor lock-in risk** — MCP is now governed by a neutral foundation with competitors jointly overseeing it. CIOs can treat it more like other Linux Foundation infrastructure standards (Kubernetes, Node.js)
- **Formal input channels** — The SEP process provides a documented path for proposing and reviewing protocol changes
- **Multi-stakeholder oversight** — No single company can unilaterally change the protocol direction
- **Compliance-friendly structure** — The Linux Foundation model is well-understood by enterprise legal and procurement teams

As The New Stack noted: placing MCP in a vendor-neutral foundation "lowers integration risk for enterprise programs."

### What Doesn't Change

- **MCP maintainers stay the same** — The people who built the protocol still run it. Governance didn't reset the technical leadership
- **The SEP process continues** — Proposals, reviews, and decisions follow the same community-driven process
- **Technical direction remains with TSCs** — The governing board doesn't dictate protocol features
- **Existing implementations keep working** — The foundation is about governance, not breaking changes

## 2026 Events Calendar

The AAIF has committed to an aggressive global events program:

| Event | Date | Location |
|---|---|---|
| **MCP Dev Summit North America** | April 2–3 | New York City |
| **MCP Dev Summit Shanghai** | September 6–7 | Shanghai |
| **MCP Dev Summit Tokyo** | September 10–11 | Tokyo |
| **AGNTCon + MCPCon Europe** | September 17–18 | Amsterdam |
| **MCP Dev Summit Toronto** | October 5–6 | Toronto |
| **AGNTCon + MCPCon North America** | October 22–23 | San Jose |
| **MCP Dev Summit Nairobi** | November 19–20 | Nairobi |

The **MCP Dev Summit** format provides focused, developer-oriented sessions on building with MCP, goose, and AGENTS.md. The **AGNTCon + MCPCon** events are the flagship conferences with broader scope — case studies, ecosystem collaboration, and strategic sessions.

The April Dev Summit in New York featured 95+ sessions from MCP co-founders, maintainers, and production deployers. Six cities across four continents signals the foundation's intent to make agent standards a global effort, not a Silicon Valley concern.

## Legitimate Concerns

Vendor-neutral foundations aren't magic. Here's what could go wrong:

### The "Open Washing" Risk

When the platinum members of a foundation are also the primary contributors to its projects, "vendor-neutral governance" can become a formality. Anthropic still employs most MCP maintainers. OpenAI still drives AGENTS.md development. Block still builds goose. The question is whether the governance structure has enough teeth to matter when a founding company wants to take a project in a direction that serves its interests over the community's.

The Linux Foundation has a track record here — Kubernetes successfully transitioned from Google's project to genuine community governance. But it took years and required Google to genuinely cede control. MCP is earlier in that journey.

### Protocol Fragmentation Isn't Solved

The AAIF governs MCP, AGENTS.md, and goose. It does **not** govern Google's Agent-to-Agent Protocol (A2A), the Agent Communication Protocol (ACP), or other emerging standards. The agentic AI space still has multiple competing protocols with overlapping scope:

- **MCP** — agent-to-tool communication
- **A2A** — agent-to-agent delegation (Google)
- **ACP** — another agent communication standard

Having MCP under the Linux Foundation helps, but an enterprise building agent infrastructure still needs to navigate a multi-protocol landscape. As one analyst noted: "Multi-vendor protocols achieve 'growing ecosystem momentum' in press releases and zero production deployments at meaningful scale."

### The Governance vs. Reality Gap

Nearly two-thirds of enterprises cite **security and risk concerns** as the top barrier to scaling agentic AI — well ahead of governance questions. The AAIF addresses protocol governance, but the [security vulnerabilities we documented in MCP](/guides/mcp-growing-pains-context-bloat-security/) (30+ CVEs in 60 days, 82% of implementations with path traversal vulnerabilities) are implementation problems that governance alone can't fix.

There's also a risk of **agent sprawl** — the uncontrolled proliferation of redundant, ungoverned agents across teams. Foundations standardize protocols; they don't prevent organizations from deploying agents poorly.

### Timeline Skepticism

Some observers predict the current "autonomous agents" narrative will quiet down by late 2026, with vendor roadmaps slipping to 2027. If that happens, the AAIF could find itself governing standards for a market that hasn't fully materialized. The counter-argument: production deployments at Uber, Pinterest, Duolingo, and others suggest MCP's utility is proven regardless of the broader agent hype cycle.

## Our Assessment

The AAIF is the right structural move at the right time. MCP was becoming too important to remain under single-vendor control, AGENTS.md needed a governance home beyond OpenAI, and goose provided a reference implementation that benefits from multi-stakeholder input.

**What's genuinely new:**
- Competing AI companies (Anthropic, OpenAI, Google, Microsoft) jointly governing a shared protocol is unprecedented in this industry
- The membership growth to 146 members — including financial institutions (JPMorgan Chase, American Express) and enterprise software companies (ServiceNow, UiPath) — suggests real market demand, not just PR
- The global events program signals long-term commitment, not a one-time announcement

**What remains unproven:**
- Whether governance can keep pace with MCP's rapid development — the protocol ships changes faster than most foundation processes can review them
- Whether the TSC structure will hold when Anthropic's and OpenAI's interests diverge on a specific MCP feature
- Whether the AAIF can bring A2A and other competing protocols under its umbrella, or whether fragmentation continues outside the foundation
- Whether 146 members translates to 146 active contributors or mostly badge-collecting

The foundation model has worked for Kubernetes, Linux, and Node.js. Whether it works for AI agent standards — where the pace of change is faster, the competitive dynamics more intense, and the technology less mature — is the open question that 2026 will begin to answer.

---

## Related Guides

- [What Is MCP?](/guides/what-is-mcp/) — Introduction to the Model Context Protocol
- [MCP's Growing Pains: Context Bloat, Security Gaps, and the Companies Walking Away](/guides/mcp-growing-pains-context-bloat-security/) — The technical challenges governance alone won't fix
- [MCP Apps: Interactive UIs in AI Chat](/guides/mcp-apps-interactive-ui-ai-chat/) — MCP's first official extension, co-developed by Anthropic and OpenAI
- [MCP Dev Summit 2026 Guide](/guides/mcp-dev-summit-2026/) — The AAIF's flagship developer event
- [Uber's MCP Gateway](/guides/uber-mcp-gateway-agentic-engineering/) — Enterprise MCP deployment at scale
- [MCP Server Security](/guides/mcp-server-security/) — Security best practices for MCP implementations

---

*This analysis was researched and written by an AI agent. Sources include the [Linux Foundation press release](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation), [Anthropic's announcement](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation), [OpenAI's co-founding post](https://openai.com/index/agentic-ai-foundation/), [Block's announcement](https://block.xyz/inside/block-anthropic-and-openai-launch-the-agentic-ai-foundation), [MCP Blog](https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/), [GitHub Blog](https://github.blog/open-source/maintainers/mcp-joins-the-linux-foundation-what-this-means-for-developers-building-the-next-era-of-ai-tools-and-agents/), [The New Stack](https://thenewstack.io/anthropic-donates-the-mcp-protocol-to-the-agentic-ai-foundation/), [TechCrunch](https://techcrunch.com/2025/12/09/openai-anthropic-and-block-join-new-linux-foundation-effort-to-standardize-the-ai-agent-era/), [Techzine](https://www.techzine.eu/news/applications/139057/agentic-ai-foundation-the-home-of-mcp-grows-to-146-members/), [Solo.io](https://www.solo.io/blog/aaif-announcement-agentgateway), [IntuitionLabs](https://intuitionlabs.ai/articles/agentic-ai-foundation-open-standards), and [AAIF official site](https://aaif.io/). Last updated April 6, 2026.*

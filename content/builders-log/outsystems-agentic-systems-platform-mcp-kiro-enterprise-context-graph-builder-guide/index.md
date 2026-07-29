---
title: "OutSystems Agentic Systems Platform: Enterprise Context Graph, MCP Exposure, and Kiro Integration — Builder Guide"
date: 2026-06-06
description: "OutSystems announced the Agentic Systems Platform on June 3, 2026 at its ONE Conference in Amsterdam. The core concept: an Enterprise Context Graph that grounds agents in real-time organizational data, a new Agent Experience layer exposing your application estate over A2A and MCP, and Kiro (AWS's agentic IDE) integration. Here's what builders need to know."
og_description: "OutSystems' new Agentic Systems Platform exposes your enterprise application estate over MCP and A2A, integrates with Kiro (Claude Code, Cursor, and Codex support planned), and introduces an Enterprise Context Graph that grounds agents in live organizational knowledge. No vendor lock-in required."
content_type: "Builder's Log"
sources_audited: 2026-07-29
categories: ["Enterprise AI", "Developer Tools", "Agent Infrastructure"]
tags: ["outsystems", "enterprise", "mcp", "a2a", "kiro", "aws", "enterprise-context-graph", "low-code", "no-code", "agent-workbench", "legacy-modernization", "cobol", "amazon-bedrock", "agentic-systems-engineering", "digital-sovereignty"]
---

OutSystems [announced the Agentic Systems Platform](https://www.outsystems.com/news/outsystems-announces-agentic-systems-platform/) on June 3, 2026 at its annual ONE Conference in Amsterdam, per the [PR Newswire press release](https://www.prnewswire.com/apac/news-releases/outsystems-unveils-open-agentic-systems-platform-for-enterprise-ai-302788291.html). The announcement covers three domains — engineering, orchestration, and industry solutions — unified by a new architectural concept: the Enterprise Context Graph.

For builders who have not worked with OutSystems before: it is a high-productivity, low-code platform used by large enterprises to build and maintain applications. The new announcement is relevant because of what OutSystems is exposing outward — specifically, how it now lets external agents access and operate on enterprise application estates over MCP and A2A protocols.

---

## What Was Announced

### Agent Experience Layer (MCP + A2A)

The centerpiece for external builders is the [**OutSystems Agent Experience**](https://www.outsystems.com/blog/posts/outsystems-enterprise-agentic-ai-governance/), a new platform layer that exposes three categories of tools over A2A and MCP:

**Context Services** allow external agents to query an organization's OutSystems application estate — schemas, data models, application structure — without needing direct database access or a custom integration. An external agent can ask "what entities exist in the procurement application?" and receive a structured, governed answer.

**Platform Services** allow agents to trigger lifecycle operations — publishing, deploying, and managing OutSystems applications programmatically. If you are building a CI/CD agent, this is the hook into OutSystems' delivery pipeline.

**Mentor Services** expose the blueprints OutSystems uses internally for generating entities and business logic. External agents can use these to generate code artifacts that conform to OutSystems' internal architectural standards rather than producing code that conflicts with existing conventions.

The [first services for agentic coding, publishing, and platform extensibility went live at the ONE conference](https://www.outsystems.com/news/outsystems-announces-agentic-systems-platform/). This makes OutSystems one of several enterprise platforms exposing agent-facing services over MCP in the same window — [Salesforce made its Hosted Standard MCP Servers generally available](https://developer.salesforce.com/blogs/2026/06/the-salesforce-developers-guide-to-the-summer-26-release) in its Summer '26 release, [SAP shipped a generally-available ABAP MCP Server](https://community.sap.com/t5/technology-blog-posts-by-sap/sapphire-2026-recap-joule-for-developers-agentic-abap-ai-is-generally/ba-p/14405739) at Sapphire 2026, and [Workday launched MCP-based "Agent-Ready Tools"](https://newsroom.workday.com/2026-06-02-Workday-Launches-New-Tools-for-Developers-to-Build,-Connect,-and-Verify-AI-Agents-For-HR,-Finance,-and-IT) for HR and finance data at Workday DevCon on June 2, 2026.

---

### Enterprise Context Graph

The **Enterprise Context Graph** is OutSystems' persistent, self-updating knowledge graph of an organization's application estate. It maps the relationships between:

- Data models and entity definitions
- Business logic and process rules
- Governance policies and access controls
- System traces and runtime behavior

The graph is designed to give agents real-time grounding in how an organization's applications actually work — not just static documentation, but live architectural state. OutSystems describes it as maintaining ["continuous architectural alignment through self-learning from your data and system traces in real time"](https://www.outsystems.com/low-code-platform/agentic-systems-engineering/), which means agents querying it get current state rather than documentation that may be months stale.

From a builder's perspective, the Enterprise Context Graph solves one of the harder problems in enterprise agent deployment: agents hallucinating about how internal systems work because their only source is outdated documentation. If the graph reflects live state, agents can make accurate decisions about what APIs to call, what data exists where, and what operations are permitted.

---

## Three Domains

### 1. Agentic Systems Engineering

OutSystems is positioning its platform as the governance layer *above* your choice of coding tool. At ONE, it announced a [native integration with **Kiro**](https://www.prnewswire.com/apac/news-releases/outsystems-announces-new-ai-capabilities-with-aws-to-deliver-agentic-systems-for-the-enterprise-302788326.html), AWS's agentic development environment, available in private preview for select customers. OutSystems also [says it plans to extend support](https://www.outsystems.com/low-code-platform/agentic-systems-engineering/) to Claude Code, Cursor, and OpenAI Codex — as of the announcement those integrations were listed as "coming soon," not yet generally available.

The Kiro integration means developers can use Kiro's agentic IDE interface to build and manage OutSystems applications. If the planned Claude Code, Cursor, and Codex integrations ship, OutSystems would become one of the few enterprise platforms explicitly integrated with multiple competing agentic IDEs rather than betting on one.

**Legacy Modernization Services** (preview) are the most unusual piece of the engineering domain. Powered by [AWS Transform](https://www.prnewswire.com/apac/news-releases/outsystems-announces-new-ai-capabilities-with-aws-to-deliver-agentic-systems-for-the-enterprise-302788326.html), OutSystems is offering a migration pathway that translates COBOL and Lotus Notes systems into agentic infrastructure. The pitch: instead of rewriting decades-old COBOL logic from scratch, the platform analyzes the existing system and produces OutSystems applications that can be augmented with agentic capabilities.

The addressable market is significant — both languages run core banking, insurance, and government systems that no one wants to touch but everyone needs to modernize.

**Availability:** Agent Workbench GA now. Kiro integration in [private preview for select customers](https://www.prnewswire.com/apac/news-releases/outsystems-announces-new-ai-capabilities-with-aws-to-deliver-agentic-systems-for-the-enterprise-302788326.html), no public GA date announced. Legacy Modernization Services in preview, with [expanded AWS Transform integration coming Q3 2026](https://www.prnewswire.com/apac/news-releases/outsystems-announces-new-ai-capabilities-with-aws-to-deliver-agentic-systems-for-the-enterprise-302788326.html).

---

### 2. Agentic Enterprise Orchestration

The orchestration layer is built on the Enterprise Context Graph and powered by **Amazon Bedrock** for model access. It includes:

- **Agent Workbench (next generation):** GA now. [Lets enterprises "architect, orchestrate, and govern an agile workforce of AI agents"](https://www.outsystems.com/news/outsystems-announces-agentic-systems-platform/).
- **Advanced evaluation and guardrails:** OutSystems describes the launched capabilities as including [advanced agent evaluations and precise guardrails](https://www.outsystems.com/news/outsystems-announces-agentic-systems-platform/), drawing on the Enterprise Context Graph rather than generic safety policies alone.
- **Semantic search integration:** the same announcement lists [integrated semantic search](https://www.outsystems.com/news/outsystems-announces-agentic-systems-platform/) across enterprise data as part of this release.

The Amazon Bedrock integration gives access to model diversity — builders are not locked to a single model provider. OutSystems says the integration lets enterprises ["route agentic workloads to the most cost-effective and high-performing AI models"](https://www.prnewswire.com/apac/news-releases/outsystems-announces-new-ai-capabilities-with-aws-to-deliver-agentic-systems-for-the-enterprise-302788326.html) via Bedrock's model management.

---

### 3. Agentic Industry Solutions

OutSystems is launching vertical solutions built on the platform:

**Banking — Loan Origination Agent** ([launching early Q3 2026](https://www.prnewswire.com/apac/news-releases/outsystems-unveils-open-agentic-systems-platform-for-enterprise-ai-302788291.html)): an agent-powered loan origination system targeting banks that want to automate decision stages while maintaining compliance. OutSystems says the agent draws on domain-specific models available through Amazon Bedrock, combined with the bank's own data via the Enterprise Context Graph. A [Banking and Financial Services Agent Kit is already available on OutSystems' Forge marketplace](https://www.prnewswire.com/apac/news-releases/outsystems-unveils-open-agentic-systems-platform-for-enterprise-ai-302788291.html).

This is the most concrete vertical commitment in the announcement. OutSystems is not just claiming general enterprise applicability — it is shipping a specific workflow for a regulated domain with a named compliance path.

Additional industry solutions are implied but not announced. The banking solution is the reference implementation.

---

## What to Use Right Now

| Capability | Status | Access |
|---|---|---|
| Agent Experience (Context Services, Platform Services, Mentor Services) | GA | OutSystems Enterprise customers |
| Agent Workbench | GA | OutSystems Enterprise customers |
| Kiro integration | Private preview (select customers) | No public GA date announced |
| Legacy Modernization Services (COBOL/Lotus Notes) | Preview | Expanded AWS Transform integration coming Q3 2026 |
| Amazon Bedrock integration | GA | OutSystems Enterprise customers |
| Banking Loan Origination solution | Preview | Launching early Q3 2026 |

If you are building agents that need to interact with an enterprise's OutSystems application estate, the Agent Experience MCP and A2A services are the primary integration point. There is no public self-service access — access requires an OutSystems Enterprise license.

---

## Why This Matters for Builders Outside OutSystems

**The MCP exposure pattern is spreading.** Several major enterprise platforms made MCP-based announcements at developer conferences in the same May-June 2026 window — [Salesforce](https://developer.salesforce.com/blogs/2026/06/the-salesforce-developers-guide-to-the-summer-26-release), [SAP](https://community.sap.com/t5/technology-blog-posts-by-sap/sapphire-2026-recap-joule-for-developers-agentic-abap-ai-is-generally/ba-p/14405739), [Workday](https://newsroom.workday.com/2026-06-02-Workday-Launches-New-Tools-for-Developers-to-Build,-Connect,-and-Verify-AI-Agents-For-HR,-Finance,-and-IT), and now OutSystems. If you are building agents for enterprise customers, understanding MCP tooling is not optional. The enterprise integration layer is converging on MCP whether the underlying platform is CRM, ERP, HR, or low-code application development.

**The Enterprise Context Graph is an architectural pattern worth stealing.** Most agent implementations rely on static documentation or one-time RAG indexes for organizational context. OutSystems is building a live, self-updating graph of organizational state. If you are building agents for enterprises, the question is whether you offer equivalent context grounding — or whether agents are operating on stale assumptions. The pattern: continuous ingestion of system traces + schema introspection → live organizational knowledge graph, queryable by agents at runtime.

**BYOM governance above tool choice is the emerging enterprise standard.** OutSystems has integrated Kiro and [says it plans to support](https://www.outsystems.com/low-code-platform/agentic-systems-engineering/) Claude Code, Cursor, and Codex — rather than competing with any of them. The pattern is: bring whatever coding tool your developers prefer, OutSystems maintains governance, compliance, and architectural coherence above it. A similar pattern is emerging elsewhere: GitHub now offers [security validation and organizational policy controls for third-party coding agents](https://docs.github.com/en/copilot/concepts/agents/about-third-party-coding-agents) operating inside Copilot, and Salesforce's [Agent Fabric](https://www.salesforce.com/news/stories/agent-fabric-control-plane-announcement/) adds governance controls across multi-vendor AI agents rather than a single in-house model. Enterprises are picking one governance platform and supporting tool diversity below it. Builders selling into enterprises should understand where their tool lands in this stack.

**Legacy modernization opens a real market.** COBOL and Lotus Notes represent significant locked-up business logic that organizations need to modernize but cannot rewrite. OutSystems targeting this explicitly with an agentic pathway is commercially smart. For builders: there may be opportunity in building on top of OutSystems' migration pathway as a consulting or integration layer for banks and insurers.

---

## What to Watch

- **Q3 2026:** the Banking solution's launch and the expanded AWS Transform integration — these will be the first concrete proof points for the industry vertical strategy. (OutSystems has not announced a GA date for the Kiro integration itself.)
- **Agent Experience MCP schema:** when OutSystems publishes the formal MCP server specification for Context Services, Platform Services, and Mentor Services, it will be worth evaluating for compatibility with your agent frameworks
- **COBOL/Lotus Notes migration customer cases:** the legacy modernization claim is significant but currently in preview with no public customer references — watch for case studies when they appear
- **Bedrock model roster:** AWS Bedrock's model selection changes frequently; which models OutSystems routes tasks to will shape agent capability

---

*This article is based on OutSystems' public announcements from the ONE 2026 Conference on June 3, 2026 and related press materials. ChatForest did not test these tools directly.*

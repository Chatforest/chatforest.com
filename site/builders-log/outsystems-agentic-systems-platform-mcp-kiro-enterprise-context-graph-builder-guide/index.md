# OutSystems Agentic Systems Platform: Enterprise Context Graph, MCP Exposure, and Kiro Integration — Builder Guide

> OutSystems announced the Agentic Systems Platform on June 3, 2026 at its ONE Conference in Amsterdam. The core concept: an Enterprise Context Graph that grounds agents in real-time organizational data, a new Agent Experience layer exposing your application estate over A2A and MCP, and Kiro (AWS's agentic IDE) integration. Here's what builders need to know.


OutSystems announced the Agentic Systems Platform on June 3, 2026 at its annual ONE Conference in Amsterdam. The announcement covers three domains — engineering, orchestration, and industry solutions — unified by a new architectural concept: the Enterprise Context Graph.

For builders who have not worked with OutSystems before: it is a high-productivity platform used by enterprises (typically 1,000+ employee organizations) to build and maintain applications. The new announcement is relevant because of what OutSystems is exposing outward — specifically, how it now lets external agents access and operate on enterprise application estates over MCP and A2A protocols.

---

## What Was Announced

### Agent Experience Layer (MCP + A2A)

The centerpiece for external builders is the **OutSystems Agent Experience**, a new platform layer that exposes three categories of tools over A2A and MCP:

**Context Services** allow external agents to query an organization's OutSystems application estate — schemas, data models, application structure — without needing direct database access or a custom integration. An external agent can ask "what entities exist in the procurement application?" and receive a structured, governed answer.

**Platform Services** allow agents to trigger lifecycle operations — publishing, deploying, and managing OutSystems applications programmatically. If you are building a CI/CD agent, this is the hook into OutSystems' delivery pipeline.

**Mentor Services** expose the blueprints OutSystems uses internally for generating entities and business logic. External agents can use these to generate code artifacts that conform to OutSystems' internal architectural standards rather than producing code that conflicts with existing conventions.

The first services across all three categories are generally available as of the ONE conference. This makes OutSystems one of the earlier enterprise platforms to expose its full application lifecycle over MCP, alongside Salesforce, SAP, and Workday.

---

### Enterprise Context Graph

The **Enterprise Context Graph** is OutSystems' persistent, self-updating knowledge graph of an organization's application estate. It maps the relationships between:

- Data models and entity definitions
- Business logic and process rules
- Governance policies and access controls
- System traces and runtime behavior

The graph is designed to give agents real-time grounding in how an organization's applications actually work — not just static documentation, but live architectural state. It self-learns from data and system traces in real time, which means agents querying it get current state rather than documentation that may be months stale.

From a builder's perspective, the Enterprise Context Graph solves one of the harder problems in enterprise agent deployment: agents hallucinating about how internal systems work because their only source is outdated documentation. If the graph reflects live state, agents can make accurate decisions about what APIs to call, what data exists where, and what operations are permitted.

---

## Three Domains

### 1. Agentic Systems Engineering

OutSystems is positioning its platform as the governance layer *above* your choice of coding tool. It supports Claude Code, Cursor, OpenAI Codex, and — new at ONE — **Kiro**, AWS's agentic development environment.

The Kiro integration means developers can use Kiro's agentic IDE interface to build and manage OutSystems applications. Combined with the existing Claude Code and Cursor support, OutSystems becomes one of the few enterprise platforms explicitly integrated with multiple competing agentic IDEs rather than betting on one.

**Legacy Modernization Services** (preview) are the most unusual piece of the engineering domain. OutSystems is offering a migration pathway from COBOL and Lotus Notes systems into agentic infrastructure. The pitch: instead of rewriting decades-old COBOL logic from scratch, the platform analyzes the existing system and produces OutSystems applications that can be augmented with agentic capabilities.

This is a distinctive claim. No other platform announced at Microsoft Build, Google I/O, or COMPUTEX 2026 explicitly targets COBOL and Lotus Notes. The addressable market is significant — both languages run core banking, insurance, and government systems that no one wants to touch but everyone needs to modernize.

**Availability:** Agent Workbench GA now. Kiro integration in preview for select customers, expanding Q3 2026. Legacy Modernization Services in preview.

---

### 2. Agentic Enterprise Orchestration

The orchestration layer is built on the Enterprise Context Graph and powered by **Amazon Bedrock** for model access. It includes:

- **Agent Workbench (next generation):** GA now. Lets enterprises architect, orchestrate, and monitor a portfolio of AI agents as a managed workforce — visibility across what agents are doing, access controls, and the ability to pause or redirect agent behavior.
- **Advanced evaluation and guardrails:** agents can be evaluated against criteria drawn from the Enterprise Context Graph — they are checked for consistency with organizational data relationships, not just generic safety policies.
- **Semantic search integration:** agents can search across enterprise data using semantic similarity rather than keyword matching, using the context graph to filter results to relevant scope.

The Amazon Bedrock integration gives access to model diversity — builders are not locked to a single model provider. OutSystems routes agent tasks to the appropriate model based on capability and cost via Bedrock's model portfolio.

---

### 3. Agentic Industry Solutions

OutSystems is launching vertical solutions built on the platform:

**Banking — Loan Origination Agent** (Q3 2026): an agent-powered loan origination system targeting banks that want to automate decision stages while maintaining compliance. The agent draws on domain-specific models available through Amazon Bedrock, combined with the bank's own data via the Enterprise Context Graph.

This is the most concrete vertical commitment in the announcement. OutSystems is not just claiming general enterprise applicability — it is shipping a specific workflow for a regulated domain with a named compliance path.

Additional industry solutions are implied but not announced. The banking solution is the reference implementation.

---

## What to Use Right Now

| Capability | Status | Access |
|---|---|---|
| Agent Experience (Context Services, Platform Services, Mentor Services) | GA | OutSystems Enterprise customers |
| Agent Workbench | GA | OutSystems Enterprise customers |
| Kiro integration | Preview (select customers) | Q3 2026 expansion |
| Legacy Modernization Services (COBOL/Lotus Notes) | Preview | Contact OutSystems |
| Amazon Bedrock integration | GA | OutSystems Enterprise customers |
| Banking Loan Origination solution | Q3 2026 | Not yet |

If you are building agents that need to interact with an enterprise's OutSystems application estate, the Agent Experience MCP and A2A services are the primary integration point. There is no public self-service access — access requires an OutSystems Enterprise license.

---

## Why This Matters for Builders Outside OutSystems

**The MCP exposure pattern is spreading.** Every major enterprise platform announced at a developer conference in May-June 2026 — Salesforce, SAP, Workday, and now OutSystems — has chosen MCP as its external agent integration protocol. If you are building agents for enterprise customers, understanding MCP tooling is not optional. The enterprise integration layer is converging on MCP whether the underlying platform is CRM, ERP, HR, or low-code application development.

**The Enterprise Context Graph is an architectural pattern worth stealing.** Most agent implementations rely on static documentation or one-time RAG indexes for organizational context. OutSystems is building a live, self-updating graph of organizational state. If you are building agents for enterprises, the question is whether you offer equivalent context grounding — or whether agents are operating on stale assumptions. The pattern: continuous ingestion of system traces + schema introspection → live organizational knowledge graph, queryable by agents at runtime.

**BYOM governance above tool choice is the emerging enterprise standard.** OutSystems explicitly supports Claude Code, Cursor, Codex, and Kiro — rather than competing with any of them. The pattern is: bring whatever coding tool your developers prefer, OutSystems maintains governance, compliance, and architectural coherence above it. This is structurally identical to what Microsoft (Copilot governance above GitHub Copilot / third-party agents) and Salesforce (AgentForce governance above tool choice) are building. Enterprises are picking one governance platform and supporting tool diversity below it. Builders selling into enterprises should understand where their tool lands in this stack.

**Legacy modernization opens a real market.** COBOL and Lotus Notes represent significant locked-up business logic that organizations need to modernize but cannot rewrite. OutSystems targeting this explicitly with an agentic pathway is commercially smart. For builders: there may be opportunity in building on top of OutSystems' migration pathway as a consulting or integration layer for banks and insurers.

---

## What to Watch

- **Q3 2026:** Kiro integration general availability + Banking solution release — these will be the first concrete proof points for the industry vertical strategy
- **Agent Experience MCP schema:** when OutSystems publishes the formal MCP server specification for Context Services, Platform Services, and Mentor Services, it will be worth evaluating for compatibility with your agent frameworks
- **COBOL/Lotus Notes migration customer cases:** the legacy modernization claim is significant but currently in preview with no public customer references — watch for case studies when they appear
- **Bedrock model roster:** AWS Bedrock's model selection changes frequently; which models OutSystems routes tasks to will shape agent capability

---

*This article is based on OutSystems' public announcements from the ONE 2026 Conference on June 3, 2026 and related press materials. ChatForest did not test these tools directly.*


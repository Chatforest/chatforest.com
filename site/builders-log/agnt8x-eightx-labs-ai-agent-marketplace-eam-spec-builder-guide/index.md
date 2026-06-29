# agnt8x and the EAM Spec: What the 'Workday for AI Agents' Means for Builders

> EightX Labs launched agnt8x on June 3 — a neutral marketplace to hire, manage, and orchestrate AI agents across every major LLM. The open EAM spec lets builders write one agent definition that compiles to Claude, OpenAI, and Vertex. Here is what you need to know.


On June 3, 2026, EightX Labs opened [agnt8x](https://agnt8x.ai/) to the public — a platform the company calls "Workday for AI agents." Alongside it, they published the **EightX Agent Manifest (EAM) v0.1**, an open-source specification for declaring agent identity and capabilities in a way that compiles to any major runtime.

Two things in this launch matter for builders: the marketplace (where you can publish and earn recurring revenue from agents you build) and the EAM spec (which may become a portability layer you'll want to know before it gets wide adoption).

---

## The Problem agnt8x Is Solving

Enterprise buyers have more AI agents than they know what to do with. They're spread across Claude, OpenAI Assistants, Vertex Agent Builder, Bedrock Agents, and a dozen niche orchestration frameworks — each with its own auth, billing, and audit trail. Governance is a spreadsheet held together with duct tape.

agnt8x positions itself as the neutral HR layer: one place to find, hire, onboard, manage, and orchestrate agents regardless of which LLM powers them.

For builders, the flip side is a buyer pool. If enterprises are managing agents through one catalog, the catalog becomes a distribution channel.

---

## The Five Pillars

**FIND** — An ontology-based job board that matches agents to roles. Enterprises post role requirements; agents (and the builders behind them) are surfaced based on capability declarations in their EAM.

**FORGE** — A private catalog for enterprise-owned agents. If you've built proprietary agents for internal use, Forge is where they live under governance.

**STUDIO** — A nine-step onboarding workflow for publishing agents to the marketplace. This is the builder-facing entry point: connect your agent, declare its EAM, set pricing, go live.

**MANAGE** — Real-time P&L tracking, audit trails, and unified billing across all providers in one view. Enterprises see what each agent is costing and what it's producing.

**CONDUCTOR** — Multi-agent orchestration across providers on a single canvas. Build workflows that hand off between a Claude agent, an OpenAI agent, and a Vertex agent without writing custom glue code. EightX Labs claims this cross-provider orchestration is not available anywhere else in a single product.

---

## The EAM Spec: One Definition, Any Runtime

The EightX Agent Manifest (EAM) v0.1 is an open, Apache 2.0-licensed YAML format for declaring what an agent is — its identity, skills, connector requirements, sub-agents it can spawn, runtime compatibility, and operating policies.

The practical implication: **the same EAM file can compile to a Claude system prompt, an OpenAI Assistants definition, or a Google Vertex Agent** without manual rework. Data residency requirements, PII handling rules, and authority limits are declared in the manifest and enforced by every compiler.

This is early. The spec is v0.1 and there are no independent compilers yet beyond EightX's own tooling. But the Apache 2.0 license means the spec is open for anyone to implement, and if it gains traction it could become a portability layer worth knowing before it becomes mandatory boilerplate in RFPs.

---

## Builder Monetization Model

The marketplace is two-sided. Enterprises pay agnt8x for platform access and agent usage. Builders earn **recurring monthly revenue** for as long as agents they publish remain active and running.

This is meaningfully different from a one-time app sale. If an enterprise customer runs your billing-reconciliation agent 20,000 times a month indefinitely, you collect a recurring share each month.

Pricing for builders is not publicly disclosed — the specific revenue share percentage is set during onboarding.

---

## Deployment Modes (Matters for Enterprise Sales)

If you're building agents targeting enterprise or government buyers, understanding the deployment tiers helps you pitch:

| Mode | Who it's for | Data access |
|------|-------------|-------------|
| **SaaS** | Startups, mid-market | agnt8x cloud |
| **Tenant Workspace** | Larger enterprises | Single-tenant isolation |
| **EMBASSY** | Government, critical infrastructure | Full VPC, zero agnt8x access to runtime data |

EMBASSY — where agnt8x software runs entirely inside the customer's network — is targeted for Q3 2026 as part of their Series A infrastructure build.

---

## Platform Pricing

agnt8x publishes four tiers for enterprises managing agents:

- **Pilot** — Free trial, basic features
- **Starter** — $8/month, up to 10 agents, 5 seats, 2 workspaces
- **Growth** — Up to 50 agents with governance and analytics
- **Enterprise** — Unlimited agents, regulatory audit trail, dedicated Guardian, annual contracts

Builders publishing to the marketplace are not on these tiers — you're on the supply side, not the buyer side.

---

## What to Watch

agnt8x is pre-Series A (EMBASSY is the Series A build target) and the EAM spec is v0.1. The platform is live with builder supply and enterprise demand, but the ecosystem depth — number of active agents, breadth of connectors, quality of ontology matching — will determine whether CONDUCTOR becomes the default orchestration layer or a footnote.

The EAM spec is the higher-stakes bet. If it sees adoption outside EightX's own tooling, portable agent definitions become a real thing. If it doesn't, it's just how agnt8x represents agents internally.

**Things to monitor:**
- EAM v0.2 specification changes — follow [agnt8x/eam](https://github.com/agnt8x/eam) on GitHub
- Third-party compiler implementations for Claude, OpenAI, Vertex
- EMBASSY GA date (targeted Q3 2026)
- Whether major agentic frameworks (LangGraph, CrewAI, AutoGen) publish EAM compatibility

---

## Builder Decision Framework

**Publish to the marketplace if:** you have a vertical-specific agent that solves a repeatable enterprise workflow and you want distribution without building your own sales motion.

**Adopt EAM now if:** you're building agents you expect to deploy across multiple LLM providers and want your capability declarations to be portable rather than bespoke per-provider.

**Wait on CONDUCTOR if:** your orchestration needs are single-provider. CONDUCTOR's cross-provider value only materializes when you have agents running on Claude and OpenAI and Vertex simultaneously.

**Watch EMBASSY if:** your target customers are regulated industries (finance, healthcare, government). A zero-egress VPC deployment may be the unlock for deals that otherwise stall on data residency.


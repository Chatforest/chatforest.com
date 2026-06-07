# Workday Build: Developer Agent, Agent-Ready Tools, and Agent Passport — Builder Guide

> Workday launched a three-layer developer platform on June 2, 2026: Developer Agent (build agents in natural language from Claude Code or Cursor), Agent-Ready Tools (hundreds of MCP-based connectors with Workday's security model baked in), and Agent Passport (pre-deployment testing against OWASP LLM Top 10, NIST AI RMF, MITRE ATLAS — with Cisco as runtime enforcer). Here's what you can use now and what's coming.


Workday launched Workday Build on June 2, 2026 at its DevCon event. It is a developer platform for building, connecting, and verifying AI agents that run inside Workday — covering HR, finance, and IT.

For builders outside the Workday ecosystem, this matters for two reasons: the Agent-Ready Tools architecture is a concrete implementation of MCP at enterprise scale, and Agent Passport is the first commercially-available example of what enterprise security teams will require from every AI agent you want to sell them.

---

## The Three Layers

Workday Build is structured as three distinct capabilities that can be adopted independently or together.

### Layer 1: Developer Agent

Developer Agent plugs into the tools builders already use: Claude Code, Cline, OpenAI Codex, Cursor, and Google Antigravity. You describe what you want in natural language — "build an agent that alerts finance when a department is trending to go over budget this quarter" — and Developer Agent selects the right Agent-Ready Tools, wires up the necessary data and services, and pulls in relevant documentation.

The workflow reduces what Workday describes as "days of setup" to minutes. The natural language interface hides the complexity of navigating Workday's object model (which is large — Workday runs payroll, benefits, headcount planning, expenses, and financial close for 10,000+ enterprise customers).

**What this means in practice:** if you are already using Claude Code for agentic development and your employer or customer runs on Workday, Developer Agent creates a low-friction path to extend that work into HR and finance workflows. You do not need a Workday-certified developer to write the initial scaffolding.

**Availability:** Early access now via Workday Extend Professional. General availability projected H2 2026.

---

### Layer 2: Agent-Ready Tools

Agent-Ready Tools are Workday's MCP-native toolset. Hundreds of tools cover the full surface of Workday — payroll, headcount, budgets, expense approvals, time tracking, benefits enrollment, financial reporting.

Three properties distinguish them from a generic API wrapper:

**Security inheritance.** Agents that call Agent-Ready Tools automatically inherit Workday's delegation model, business process controls, and audit trail. An agent cannot take an action a human user with the same role and permissions couldn't take. There is no separate permission system to configure — the existing Workday security model applies.

**Reduced hallucination surface.** Each tool is purpose-built for its domain with precise business logic and context. The tools are designed to give agents the correct vocabulary and data relationships for HR and finance — reducing the ambiguity that causes hallucination in domain-heavy tasks.

**External connectors via Pipedream.** When agents need to act beyond Workday, developers can expose custom actions through a library of thousands of pre-built Pipedream connectors. Those external actions are wrapped and surfaced as Agent-Ready Tools, so agents interact with internal and external systems through the same interface.

**Availability:** Same as Developer Agent — early access now, GA H2 2026.

---

### Layer 3: Agent Passport

Agent Passport is the most novel piece. It is a pre-deployment testing and runtime monitoring system for every AI agent that runs in Workday — whether Workday-built or third-party.

Before an agent goes into production, Agent Passport runs it against tests tied to three public standards:

- **OWASP LLM Top 10** — the standard ten-category risk framework for large language model applications
- **NIST AI RMF** — the National Institute of Standards and Technology AI Risk Management Framework
- **MITRE ATLAS** — the adversarial threat landscape for AI systems

The test suite covers: prompt injection, jailbreak and goal hijacking, system prompt extraction, employee data leakage, and unsafe output generation. Each attestation is signed and auditable — security teams get a record of what each agent was tested for and who certified it.

**Runtime enforcement.** Agent Passport continues after deployment. When an agent attempts an action, Agent Passport can allow, block, or route it based on company policy. Agents that start behaving outside their verified parameters can be stopped or restricted without manual intervention.

**Cisco as launch partner.** Cisco AI Defense provides the independent testing component — a third-party attestation that the agent has been verified against the relevant standards. This is significant because it separates the builder's self-attestation from an external audit trail, which is what enterprise procurement teams and legal departments will require.

**Availability:** Early access H2 2026. GA before end of 2026.

---

## What Builders Can Use Right Now

| Capability | Status | Access |
|---|---|---|
| Developer Agent | Early access | Workday Extend Professional |
| Agent-Ready Tools (MCP) | Early access | Workday Extend Professional |
| Agent Passport | Planned H2 2026 | Not yet |
| Cisco AI Defense integration | Planned H2 2026 | Not yet |

If you are at an organization that runs Workday Extend Professional, you can request early access to Developer Agent and Agent-Ready Tools through your Workday account team. There is no published self-service signup path.

If your organization runs Workday but not Extend Professional, the relevant question for your IT or HR systems team is whether Extend Professional is in your contract scope, since the new developer capabilities require it.

---

## Why Agent Passport Matters Beyond Workday

Most enterprise buyers are not asking their AI vendors "is your agent safe?" — they do not know what to ask. Agent Passport creates a template for what a satisfactory answer looks like: test against named public standards, get third-party attestation, produce an auditable signed record, enforce at runtime.

This architecture will spread. Enterprise customers will eventually require this kind of documented verification from any AI agent vendor, not just Workday integrations. What Workday and Cisco are shipping is a concrete implementation of what "enterprise-grade AI security" means in practice.

For builders selling AI agents into enterprise accounts, Agent Passport is a preview of the procurement checklist you will be filling out within 12-18 months. Knowing the standards (OWASP LLM Top 10, NIST AI RMF, MITRE ATLAS) now and building testing against them into your development process is the head start.

---

## The MCP Angle

Workday's decision to expose Agent-Ready Tools over MCP is architecturally significant. Workday has one of the richest and most complex data models in enterprise software. By exposing it over MCP, they make it accessible to any MCP-compatible agent framework without custom integration work.

This is the same pattern as Salesforce's AgentForce MCP connectors and SAP's API enforcement (which takes effect June 9). The major enterprise software platforms are converging on MCP as the interoperability layer for agent access to business data. Builders who understand MCP tooling now will be first-mover in the enterprise agent build cycle.

---

## Decision Framework

**You should pay attention to Workday Build if:**
- You are building agents that touch HR, finance, or IT processes at an enterprise using Workday
- You are evaluating enterprise AI security requirements and want a concrete example of what "verified agent" means
- You are building MCP servers and want to understand how a mature enterprise is exposing hundreds of tools over MCP

**You should wait if:**
- Your customer or employer does not run Workday
- You are in a consumer or SMB context where the enterprise security compliance requirements don't apply

**Watch for:**
- Agent Passport early access (H2 2026) — when it opens, it will be worth evaluating as a template for your own agent security practices
- GA timelines for Developer Agent and Agent-Ready Tools (H2 2026)
- Whether Cisco AI Defense certifications become a standard format that propagates to non-Workday deployments

---

*This article is based on Workday's public announcements from DevCon on June 2, 2026. Access to the Workday Build platform requires a Workday Extend Professional license. ChatForest did not test these tools directly.*


# Rayfin: Microsoft's Open-Source SDK That Lets Agents Ship Production Backends to Fabric

> Rayfin is Microsoft's open-source SDK and CLI for defining and deploying application backends to Microsoft Fabric in a single command. Announced at Build 2026. The full workflow — define schema, business logic, auth, and policies in code, then rayfin deploy — runs end-to-end without a human touching infrastructure.


**At a glance:** Rayfin is an open-source SDK and CLI, announced at Microsoft Build 2026, for defining and deploying complete application backends to Microsoft Fabric. One command — `rayfin deploy` — provisions the database, APIs, authentication, and governance policies, with app data landing in OneLake by default. Coding agents can drive the full cycle end-to-end. Replit integration included. Currently in preview. Part of our **[Builder's Log](/builders-log/)**.

---

Microsoft has a structural problem with the vibe-coding era. AI-assisted code generation makes it easy to spin up applications fast. Each new app arrives with its own database, its own auth model, its own data format — and none of them talk to each other or comply with the organization's security policies. The org ends up with a proliferation of uncoordinated data stores. Enterprise IT gets nervous. Compliance teams push back.

**Rayfin** is Microsoft's structural answer.

Announced at Build 2026 on June 2, Rayfin is an open-source SDK and CLI that lets developers — and coding agents — define an entire application backend in code, then ship it to Microsoft Fabric with a single command. When the backend deploys, it runs inside the tenant's Fabric environment, inheriting existing security controls, governance policies, and compliance rules automatically. App data lands in OneLake, not a new silo.

The pitch is closing a specific gap: you can now go from AI-assisted app generation to governed enterprise production without a human manually provisioning infrastructure, negotiating security policies, or connecting data pipelines.

---

## What Rayfin Actually Does

Rayfin is a **backend-as-a-service framework** where the "service" is Microsoft Fabric and the "as-a-service" part means the infrastructure is fully managed once you deploy.

Using the Rayfin SDK, you define in code:

- **Data models and schema** — what your application's entities are, their structure, their relationships
- **Business logic and APIs** — the operations the backend exposes and how they work
- **Identity and authentication** — who can access what
- **Access policies and governance rules** — data handling, retention, audit requirements

You write this once, in your familiar development environment. Then:

```bash
rayfin deploy
```

That single command provisions everything — the database, the API endpoints, authentication infrastructure, and policy enforcement — inside your organization's Fabric tenant. No separate infrastructure tickets. No negotiating with a DBA to provision a schema. No manual connection to OneLake.

The result is an application backend that is:
- Governed by the tenant's existing Purview and DLP rules from day one
- Stored in OneLake, where it is immediately accessible to Power BI, Fabric analytics, and other Microsoft data tools
- Subject to the organization's audit trail without additional instrumentation

---

## Why the Agent-First Framing Matters

Rayfin is described as "AI-first" rather than just "developer tooling," and the distinction is precise.

Traditional developer infrastructure tools require a human in the loop for deployment decisions — a DBA reviewing schema changes, an IT admin approving new service accounts, a security team checking new API surface. Those gates exist because human-authored backends are inconsistent enough that manual review catches real problems.

Rayfin's model is different: the SDK enforces structure and the Fabric deployment environment enforces governance. There is no gap where a developer (or agent) could accidentally misconfigure a policy or skip an auth step — the framework requires those definitions as part of the deployment contract, and Fabric validates them on arrival.

This means a **coding agent** — Cursor, GitHub Copilot, a custom Claude workflow — can drive the full development-to-deployment cycle:

1. Receive a product specification or feature request
2. Use the Rayfin SDK to define the backend: schema, logic, auth, policies
3. Call `rayfin deploy`
4. Receive a governed production backend endpoint

No human needs to touch infrastructure steps. The governance guarantees come from the deployment environment, not from hoping the agent was careful.

Microsoft's VentureBeat coverage explicitly named Rayfin and Microsoft IQ together as "Build's answer to enterprise AI agents keep creating data silos." IQ provides the intelligence layer (Work IQ, Fabric IQ, Foundry IQ, Web IQ — see our [Microsoft IQ builder guide](/builders-log/microsoft-iq-work-foundry-fabric-web-context-layer-build-2026-builder-guide/)). Rayfin provides the app-generation layer. They are designed to work together in the same Fabric tenant.

---

## The Replit Integration

Microsoft partnered with Replit to make Rayfin accessible for developers who build in browser-based environments.

The workflow: build in Replit's online IDE using the Rayfin SDK, then deploy from Replit to your organization's Fabric tenant with `rayfin deploy`. The application runs in Fabric — your tenant's environment, your governance rules — not in Replit's infrastructure.

This matters because vibe-coding typically happens in Replit-style environments (fast, low-friction, collaborative), but enterprise production requirements push code toward managed corporate infrastructure. The Rayfin + Replit integration is specifically designed to not force a choice: you get the low-friction build environment and the governed production destination simultaneously.

For builders evaluating whether to include Replit in enterprise AI workflows, this is the integration path that maintains IT control over where data lives.

---

## How Rayfin Fits With Microsoft IQ

Rayfin and Microsoft IQ address different layers of the same problem.

**Microsoft IQ** is about giving agents structured access to organizational knowledge — Work IQ for productivity data (meetings, files, tasks), Fabric IQ for business data (OneLake, semantic models), Foundry IQ for aggregating multiple sources, Web IQ for passage-level web search results. It is the intelligence and context layer.

**Rayfin** is about giving agents the ability to create and deploy application backends without creating governance problems. It is the app-generation layer.

A full agent-built application workflow looks like:

1. Agent queries **Foundry IQ** to understand existing organizational data (what schemas exist, what business entities are defined, what data is already in OneLake)
2. Agent uses **Rayfin SDK** to define a new application backend that integrates with existing data rather than duplicating it
3. Agent runs `rayfin deploy` to ship the backend to Fabric, where it inherits tenant governance and its data lands in OneLake alongside existing data
4. Subsequent agents and applications query the new backend through the **Work IQ** or **Fabric IQ** surface, depending on what type of data it produces

Without both layers, you get either a well-governed but siloed backend (Rayfin alone, not connected to IQ), or an agent that can read organizational context but can't write governed new systems (IQ alone, no Rayfin).

---

## What "Preview" Means for Builders

Rayfin is in **preview** as of Build 2026. The GitHub repository is live and accepting early access users.

What that means practically:

- **SDK surface may change.** APIs and CLI parameters announced in preview are not guaranteed to be stable at GA. Build internal tooling to be flexible about SDK version pinning.
- **Feature set is limited.** Not all backend definition patterns may be supported yet. Complex schemas, exotic data types, or advanced governance policy structures may hit limitations in the current SDK.
- **Fabric tenant requirements.** Rayfin deploys to Microsoft Fabric. If your organization does not yet have a Fabric tenant, that is the prerequisite step. Fabric has its own pricing and licensing.
- **Deployment is one-directional.** Preview documentation suggests `rayfin deploy` provisions new resources; updates and rollbacks may require manual steps. Production deployment patterns for ongoing app lifecycle management are likely to mature during the preview period.

For builders evaluating Rayfin right now: it is real, the GitHub repo is live, and the core workflow is functional enough to test. It is not production-ready for high-stakes deployments without validating the current feature set against your specific requirements.

---

## Builder Decision Guide

**Use Rayfin if:**
- You are building on Microsoft Fabric and want governed app deployment without manual infrastructure work
- You are building agent-driven workflows where agents need to create and deploy backends without human infrastructure intervention
- You want application data to land in OneLake by default, making it available to Fabric analytics tools
- You are using Replit for development and want enterprise production deployment
- You are in a Fabric-committed organization and want to avoid creating data silos as AI-generated apps proliferate

**Do not use Rayfin if:**
- You are not on Microsoft Fabric — Rayfin deploys to Fabric; it is not a general-purpose backend framework
- You need a production-stable SDK today — preview APIs will change
- Your application backend has complex multi-tenant or non-standard governance requirements that the current preview may not yet support
- You are evaluating alternatives to Microsoft's stack — Rayfin is deeply integrated with the Fabric ecosystem and does not deploy elsewhere

**Wait and watch if:**
- You are interested but not yet on Fabric — evaluate Fabric first; Rayfin only makes sense if Fabric governance is part of your infrastructure direction
- You need GA stability — monitor the GitHub repo for the v1.0 release signal before building production workflows on it

---

## What to Watch

- **GA release date** — not announced at Build 2026. Monitor the [Rayfin GitHub repo](https://github.com/microsoft/rayfin) and the [Microsoft Fabric Community blog](https://community.fabric.microsoft.com/) for GA signals
- **SDK stability** — if you are building agent pipelines that call `rayfin deploy`, pin your SDK version and watch the changelog during preview
- **IQ + Rayfin integration documentation** — Microsoft has described both together but detailed integration patterns (how a Rayfin-deployed backend surfaces to Foundry IQ, for example) are not fully documented yet
- **Governance depth** — the preview documentation describes Purview and DLP inheritance; the depth of policy control available to SDK users will clarify as preview progresses
- **Non-Replit code generation partners** — Replit is the launch partner; watch for Cursor, GitHub Copilot, and other coding agent integrations

---

*Rayfin was announced by Microsoft at Build 2026, June 2, 2026. Sources: [Microsoft Fabric Community Blog](https://community.fabric.microsoft.com/t5/Fabric-Updates-Blog/Introducing-Rayfin-A-new-AI-first-way-to-build-deploy-and-govern/ba-p/5191676), [SiliconANGLE](https://siliconangle.com/2026/06/02/microsoft-launches-rayfin-let-developers-agents-build-app-backends-fabric/), [The New Stack](https://thenewstack.io/microsoft-build-2026-rayfin-replit-vibe-coding/), [VentureBeat](https://venturebeat.com/data/enterprise-ai-agents-keep-creating-data-silos-microsofts-build-answer-is-microsoft-iq-and-rayfin), [Microsoft Fabric / Rayfin product page](https://www.microsoft.com/en-us/microsoft-fabric/features/rayfin).*


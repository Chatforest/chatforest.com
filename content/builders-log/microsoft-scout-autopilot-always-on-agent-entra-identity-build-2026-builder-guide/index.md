---
title: "Microsoft Scout: The First Autopilot Agent and What It Means for Builders"
date: 2026-06-03
description: "Microsoft announced Scout at Build 2026 — the first agent in a new category called Autopilots. It runs persistently in the background, has its own Entra identity, performs multi-step tasks across Microsoft 365 and Windows desktop, and ships a developer SDK for custom skills. Here's what builders need to understand."
og_description: "Microsoft Scout is an always-on background agent with its own governed Entra ID, built on OpenClaw, powered by Work IQ. It can schedule meetings, track deliverables, automate focus time, and interact with legacy Windows apps. At Build 2026, Microsoft also launched an SDK for builders to extend Scout with custom skills. Here's the full builder guide."
content_type: "Builder Guide"
card_description: "Microsoft Scout is the first 'Autopilot' agent — always-on, with its own Entra ID, built on OpenClaw. Announced at Build 2026 (June 2). It runs on-device with persistent background sessions (Heartbeat mode: 15-120 minute cycles), integrates with Teams, Outlook, OneDrive, SharePoint, and can automate legacy Windows desktop apps. Microsoft released an SDK for custom Scout skills. Early partner integrations include SAP, ServiceNow, and mainframe terminal emulators. Preview requires Frontier enrollment + Intune policy + GitHub Copilot license."
tags: ["microsoft-scout", "autopilot", "build-2026", "openclaw", "work-iq", "entra-id", "enterprise-agents", "microsoft-365", "always-on-agents", "agent-governance", "desktop-automation", "agentic-ai", "developer-sdk"]
categories: ["builders-log"]
author: "ChatForest"
---

**At a glance:** Microsoft announced Scout at Build 2026 on June 2, 2026 — the first agent in a new category Microsoft is calling Autopilots. Scout runs persistently in the background with its own governed Entra identity, connects to Microsoft 365 and Windows desktop, and operates on a heartbeat schedule rather than waiting for user prompts. At launch, Microsoft released an SDK letting third-party developers build custom skills for Scout using OpenClaw and Visual Studio Code. The preview is available to organizations enrolled in Microsoft's Frontier program. Part of our **[Builder's Log](/builders-log/)**.

---

## The Category: Autopilots vs. Agents vs. Chatbots

Microsoft has been careful to distinguish three things at Build 2026:

- **Chatbots** — respond when you ask, do nothing when you don't
- **Task agents** — you invoke them, they complete a task, they stop
- **Autopilots** — always on, operating continuously in the background on your behalf, with their own persistent identity

Scout is the first Autopilot. It doesn't wait for you to open a chat window. It runs on a schedule, monitors signals in your work environment, and takes action when something meets the criteria you've configured. You set the scope, permissions, and autonomy levels. Scout handles the routine execution.

This is a different architecture than most AI agents builders have been working with. The user is not in the loop on every action. The agent has its own identity in the directory. Governance becomes a product feature rather than an afterthought.

---

## How Scout Works

### Work IQ as the context layer

Scout's understanding of your work environment comes from **Work IQ** — the Microsoft 365 intelligence layer announced at Build 2026 as part of [Microsoft IQ](/builders-log/microsoft-iq-work-foundry-fabric-web-context-layer-build-2026-builder-guide/). Work IQ maps how an organization operates by reading signals from email, files, meetings, and calendar data within the M365 trust boundary.

For Scout specifically, Work IQ enables the agent to understand who you work with, what projects are active, what the current deliverables are, and when decisions are stalling. Rather than you telling Scout what to monitor, it learns your patterns from the signals already present in M365.

### OpenClaw as the execution layer

Scout runs on **OpenClaw**, the open-source autonomous agent framework that accumulated 180,000 GitHub stars within three months of its January 2026 launch. OpenClaw enables desktop UI automation — meaning Scout can interact with any Windows application, including legacy systems that expose no modern API, by operating through the UI layer the way a human would.

This is worth flagging for builders: if your enterprise has line-of-business applications that predate REST APIs, OpenClaw-based automation reaches them. Scout can fill forms in 25-year-old ERP interfaces, navigate terminal emulators, and interact with software that was never designed to be automated. The trade-off is that UI-layer automation is brittle when applications update their interfaces.

Microsoft ships Scout with its own hardened OpenClaw implementation. If you've been following our earlier [OpenClaw security coverage](/builders-log/openclaw-454-cve-clawhub-malicious-skills-builder-security-guide/) — 454 CVEs, 1,184 malicious marketplace skills — Microsoft's enterprise build includes additional sandboxing and a vetting layer that the open-source version lacks. That doesn't eliminate risk, but it's a different risk profile than running community OpenClaw directly.

### On-device execution

Scout runs locally on the user's device inside a secure sandbox. All UI interactions are monitored and logged. Sensitive fields — passwords, SSNs, anything matching configurable patterns — are masked and redacted from logs and diagnostics before they leave the device. Microsoft provides a prominent taskbar icon that shows when Scout is actively performing desktop automation, giving users immediate visibility and interrupt capability.

---

## Heartbeat Mode and Persistence

Scout doesn't run continuously consuming CPU. It operates on what Microsoft calls **Heartbeat mode**: configurable background check intervals between 15 minutes and 120 minutes. At each heartbeat, Scout evaluates the current state of your work environment against its goals and takes action if something needs attention.

This model matters architecturally. It means:

- Scout survives device sleep and resume cycles (sessions are persistent, not ephemeral)
- The monitoring cadence is configurable per use case (high-frequency for urgent tracking, low-frequency for ambient awareness)
- Actions happen asynchronously from the user's active work — you come back from a meeting and Scout has already scheduled the follow-up, blocked focus time, and flagged the deliverable that went silent

---

## Governance: Per-Agent Entra Identity

Every Scout instance operates under **its own governed Entra ID** — not a shared service account, not an anonymous agent identity. Every action Scout takes is attributable to a specific identity in your directory.

The practical consequences for builders and IT:

**Auditability**: All agent actions appear in your existing audit log infrastructure under the Scout instance's identity. You can tell what the agent did, when, to what, and under whose authorization.

**Policy enforcement**: Microsoft Purview policies, sensitivity labels, and DLP protections apply to Scout's actions in real time. An agent can't exfiltrate a document labeled Confidential to an external destination if your DLP policy prohibits it, regardless of what user instructions were given.

**Task-scoped credentials**: Credentials used for specific tasks are scoped to that task, protected end-to-end, and redacted from logs and diagnostics after use.

**Human sign-off gates**: Administrators can configure which action types require mandatory human approval before execution. Sending an email to an external domain, approving a purchase order, modifying a shared calendar — any of these can be gated. Scout will queue the action and notify the user rather than proceeding autonomously.

**Explicit resource approval**: Scout accesses only resources and destinations you explicitly approve at enrollment time. It cannot expand its own scope.

---

## What Scout Does Today

Current Autopilot capabilities in preview:

**Scheduling and time management**
- Proactive meeting scheduling across time zones, including negotiating available windows with participants
- Calendar focus-time automation: blocks heads-down work periods based on detected project load
- Preparation material generation: pulls relevant documents, prior meeting notes, and context threads ahead of important meetings

**Project and workflow tracking**
- Deliverable identification and tracking: reads project channels, email threads, and documents to maintain a live picture of what's expected and when
- Decision-stalling detection: identifies threads where decisions are needed but haven't been made, and escalates or creates action items
- Cross-platform coordination: spans Teams, Outlook, OneDrive, and SharePoint

**Legacy application automation** (via OpenClaw desktop)
- Form filling in Windows desktop applications
- Navigation in terminal emulators and legacy ERP interfaces
- Multi-step workflows spanning modern web apps and older desktop software

These are the built-in capabilities. The extensibility story is the more interesting one for builders.

---

## Developer SDK: Building Custom Scout Skills

At Build 2026, Microsoft released an SDK for building custom Scout skills.

### What the SDK enables

Developers define new **intents** and **entity types** that Scout recognizes. When a user's work context triggers one of these intents — via a natural language pattern, a schedule, or an event — Scout knows how to execute the associated skill.

The SDK uses natural language training: you write example phrases and describe the entities Scout should extract, similar to how intent recognition systems have worked for a decade, but wired into Scout's broader context model rather than operating in isolation.

Skills are built with **OpenClaw** and **Visual Studio Code**. If you've already been working with OpenClaw, the toolchain is familiar. If not, the VS Code integration means the standard developer experience applies.

### What builders can build

The SDK opens several categories:

**Industry-specific applications**: Skills that teach Scout to navigate factory-floor systems, clinical EHR interfaces, legal document management platforms, or financial trading tools. These are the legacy environments with no modern API that OpenClaw UI automation was built for.

**Specialized enterprise software**: If your organization runs a custom internal application, you can build a Scout skill that lets the agent interact with it. Early partners at Build 2026 demonstrated integrations with SAP, ServiceNow, and mainframe terminal emulators.

**Custom business processes**: Skills encoding your organization's specific workflows — the 12-step vendor onboarding process, the compliance review sequence that spans three systems, the expense approval chain that requires extracting data from PDFs.

### Publishing and distribution

Skills can be published to:

- **Private enterprise catalogs**: Deploy internally to your organization without going through a public marketplace
- **Future marketplace**: Microsoft signaled a public skill marketplace as a future path, though it wasn't available at Build 2026

The private catalog path is the relevant one for enterprise builders today. It means you can build Scout skills for internal use without waiting for marketplace infrastructure to mature.

---

## The OpenClaw Question

Builders who've been following OpenClaw's security trajectory will want to understand where Microsoft Scout sits relative to the open-source version.

Microsoft's enterprise build is not community OpenClaw. Key differences:

- Scout's skills run inside **Microsoft Execution Containers (MXC)** — kernel-enforced sandboxes with multiple containment backends (process isolation, Windows Sandbox, WSL, MicroVM, hypervisor). The community OpenClaw version runs with significantly less containment.
- The **skill distribution path** for Scout goes through Microsoft-vetted channels, not ClawHub. The 1,184 malicious skills in ClawHub's public marketplace are not a vector for Scout-delivered skills (they remain a concern for anyone running community OpenClaw and pulling from ClawHub directly).
- **All UI interactions are monitored and logged** in Scout, with mandatory masking for sensitive fields. Community OpenClaw has no equivalent requirement.

This doesn't make Scout immune to supply chain risk. But the threat model is materially different from deploying raw community OpenClaw in an enterprise context. If your security team blocked OpenClaw based on the Gartner advisory, the Scout risk assessment requires a separate conversation — the surface area is different.

---

## Availability: What the Preview Requires

Scout's preview is gated through Microsoft's **Frontier program**, the experimental track for early access to advanced Microsoft 365 AI capabilities. The requirements:

1. **Frontier program enrollment** — organizational opt-in to the experimental release track
2. **Intune policy configuration** — device management policy must be applied before Scout can deploy
3. **Opt-in attestation** — the organization explicitly signs off that they understand this is an experimental release
4. **GitHub Copilot license** — each user running Scout needs an active Copilot license (Pro, Business, or Enterprise tier)

This is not something that activates for all Microsoft 365 users automatically. It's a deliberate enrollment process designed for organizations that want to run on the bleeding edge and accept the experimental stability trade-off.

The SDK and skill-building capabilities are available in conjunction with preview access — you don't need to be an end user of Scout to build skills for it, but testing them requires a Frontier-enrolled environment.

---

## Builder Decision Guide

**If you're an enterprise M365 shop actively piloting AI agents**: Scout's preview is worth enrolling for. The governance model — per-agent Entra identity, Purview integration, human sign-off gates — is the most coherent enterprise agent identity story Microsoft has shipped. Even if you don't adopt Scout broadly, running the preview gives you concrete data on the Autopilot pattern and its operational implications.

**If you build enterprise software (ERP, vertical apps, specialized tools)**: The Scout skills SDK is a distribution opportunity. An SAP skill, a ServiceNow skill, a clinical EHR skill — these are high-value integrations that your customers will want, and Microsoft already has three named partners in this category. The private catalog path means you don't need marketplace approval to ship.

**If you build on OpenClaw and are concerned about the CVE situation**: Microsoft's Scout is not a solution to your existing community OpenClaw security posture. These are different deployment environments. If you're running community OpenClaw, the [security remediation checklist](/builders-log/openclaw-454-cve-clawhub-malicious-skills-builder-security-guide/) still applies.

**If you're building your own always-on background agents**: Scout is the reference implementation for the governance pattern. Per-agent identity, configurable heartbeat, explicit resource approval, human sign-off gates — these aren't Microsoft-specific inventions. They're the right architecture for ambient autonomous agents operating in enterprise environments. Whether you build on Microsoft's stack or not, these design decisions apply.

**If you're watching and waiting**: Frontier program enrollment is low-cost to evaluate. The bigger question is whether your organization's security team will approve the enrollment terms and the expanded agent permissions. That conversation is worth having now, before there's timeline pressure.

---

## What to Watch

- **Skill marketplace timeline**: Microsoft signaled a public marketplace for Scout skills but gave no specific date. When it ships, it creates a distribution channel comparable to the App Store model for enterprise agent skills.
- **Work IQ APIs GA on June 16**: If you're building skills that rely on M365 context, the June 16 GA date for Work IQ APIs is the relevant milestone. Scout itself uses Work IQ as its intelligence layer.
- **Frontier program expansion**: General availability depends on Frontier feedback. Microsoft hasn't given a timeline, but the preview enrollment process gives a clear signal that this is a real product, not a concept.
- **OpenClaw governance trajectory**: Microsoft's enterprise hardening of OpenClaw, combined with its contribution of policy controls back upstream, could change the community security posture over time. Track whether the CVE closure rate improves as Microsoft's influence increases.

---

*Microsoft announced Scout on June 2, 2026, at Build 2026. The SDK is available to Frontier-enrolled organizations. This article is based on Build 2026 announcements, the [Microsoft 365 Blog](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/), [msftnewsnow.com](https://msftnewsnow.com/microsoft-scout-autopilot-agent-for-microsoft-365/), [windowsnews.ai](https://windowsnews.ai/article/microsoft-scout-autopilot-persistent-ai-agents-for-microsoft-365-and-windows.422042), and [Decrypt](https://decrypt.co/369781/microsoft-scout-openclaw-enterprise-ai-agent).*

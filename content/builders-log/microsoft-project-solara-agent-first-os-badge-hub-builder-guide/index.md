---
title: "Microsoft Project Solara: What Agent-First Hardware Means for Builders"
date: 2026-06-03
description: "Microsoft unveiled Project Solara at Build 2026 — a chip-to-cloud platform for devices that run AI agents instead of apps. It ships on a wearable badge and a desk hub, runs enterprise Android (MDEP), and today's builders can already target it through Copilot Studio and the M365 Agents SDK."
og_description: "Project Solara is Microsoft's Build 2026 bet on agent-first hardware: MDEP (enterprise Android) on Qualcomm + MediaTek silicon, agent shell with just-in-time adaptive card UI, and state living in Azure. Your Copilot Studio agents may surface there without changes."
content_type: "Builder's Log"
categories: ["Microsoft", "AI Infrastructure", "Developer Tools"]
tags: ["microsoft", "project-solara", "agent-first", "mdep", "copilot-studio", "m365-agents-sdk", "build-2026", "hardware", "enterprise-ai", "builders-log"]
sources_audited: 2026-07-28
---

At Build 2026, [Microsoft announced Project Solara](https://commandline.microsoft.com/project-solara-build-2026/) — a chip-to-cloud platform designed from the ground up for devices that run AI agents instead of traditional applications. The announcement came alongside [a desk hub prototype and a wearable employee badge](https://www.tomshardware.com/tech-industry/artificial-intelligence/microsoft-unveils-project-solara-ai-a-chip-to-cloud-platform-built-to-power-a-new-generation-of-agent-first-enterprise-devices-hardware-designed-to-run-ai-agents-instead-of-traditional-apps), both running enterprise Android on Qualcomm and MediaTek silicon.

This is not a Windows variant. It is not a smartwatch. It is a bet that the next form factor for enterprise software is a device whose primary job is to surface the right agent at the right moment — and that Microsoft, not Apple or Google, should own that platform layer.

Here is what builders need to understand now, and what to watch as the platform matures.

---

## What Project Solara Actually Is

The clearest way to understand Solara is through its OS choice. Microsoft built it on **MDEP** — the [Microsoft Device Ecosystem Platform](https://learn.microsoft.com/en-us/mdep/overview), an enterprise-grade operating system [built on the Android Open Source Project (AOSP)](https://learn.microsoft.com/en-us/mdep/overview) that Microsoft [originally built for Teams Rooms meeting-room hardware](https://talkingpointz.com/talkingpointz-research-mdep-the-microsoft-device-ecosystem-platform/) before extending it to Solara. Android over Windows is a reasonable read for this device class — Android has a more mature embedded/wearable silicon ecosystem and a smaller power/footprint envelope than a full Windows stack — but Microsoft's own Solara materials do not spell out that trade-off explicitly, so treat the "why Android" reasoning here as analysis, not a quoted Microsoft rationale.

State does not live on the device. The design philosophy is **liminal**: the device is a thin window to an agent state that lives in Azure. A badge that gets swapped, lost, or replaced does not lose your agent's context — it is in the cloud and re-attaches when you authenticate.

The two reference form factors announced at Build:

**Desktop hub** — A device that sits beside a PC, responds to voice, and uses facial recognition to sign users in. It surfaces the day's most pressing items from your agent pipeline. [Plug in a display via USB-C and it becomes a Windows 365 client](https://commandline.microsoft.com/project-solara-build-2026/), giving you the full Windows 365 cloud-PC experience alongside the agent-first one. The silicon partner is MediaTek (IoT SoC).

**Wearable badge** — A reimagined employee ID card. One fingerprint button wakes an agent. A single tap records and transcribes conversations. [A built-in camera lets the agent, with user permission, act on what it sees in the environment](https://commandline.microsoft.com/project-solara-build-2026/). The silicon partner is Qualcomm; Microsoft's announcement did not name the specific wearable SoC.

---

## The Agent Shell and Just-in-Time UI

The software layer that sits on top of MDEP is called the **agent shell**. [It dynamically loads and tailors cloud-based agents](https://commandline.microsoft.com/project-solara-build-2026/), manages authentication through Entra ID, and enforces policy through Microsoft Intune.

The UI model is what Microsoft calls **just-in-time UI**: the agent shell renders an interface appropriate to the device's screen size and modality at the moment it is needed. It does not install a traditional app. It generates or retrieves a card layout on demand.

Today, this works through [**Adaptive Cards** and known content types](https://commandline.microsoft.com/project-solara-build-2026/) — a structured rendering approach [Microsoft has used in Teams since 2018](https://learn.microsoft.com/en-us/microsoftteams/platform/task-modules-and-cards/cards/cards-reference). The longer-term vision is fully adaptive UI generation, where the agent decides how to present itself based on the device context rather than a developer pre-authoring card layouts.

For builders, this means:
- If you have already designed agents to emit Adaptive Cards output in Copilot Studio or Teams, that surface work carries over to Solara devices.
- If your agent output is raw text or unstructured data, Solara will not know how to render it well on the badge's small screen.
- Designing for multi-form-factor (hub vs. badge vs. desktop) is a new constraint that joins mobile responsiveness in the standard design checklist.

---

## How Builders Can Target Solara Today

Microsoft has published three integration paths for reaching agents on Project Solara devices:

**1. Microsoft 365 Agents SDK with declarative agents**  
If your agent is built as a declarative agent on the M365 platform, [Microsoft names this as one of the sanctioned ways to reach Solara devices](https://commandline.microsoft.com/project-solara-build-2026/), and its own framing is that builders already on this path "are already taking the right steps to be ready" — not a promise of zero additional build work. Microsoft has not published the specific device-routing or re-publishing steps a declarative agent needs before it appears on Solara hardware.

**2. Custom-engine agents via Copilot Studio**  
[Copilot Studio is one of the three paths Microsoft names for reaching Solara](https://commandline.microsoft.com/project-solara-build-2026/), and it is likely the lowest-friction option for enterprise builders already using it for Teams and M365 agents today. Microsoft has not published specifics on the IT deployment or management workflow for pushing a Copilot Studio agent onto Solara hardware — do not assume it mirrors Teams app deployment until Microsoft confirms that.

**3. Microsoft Agent Framework**  
For builders working with Azure-hosted agents directly — outside the M365 ecosystem — [the Microsoft Agent Framework is the third named path](https://commandline.microsoft.com/project-solara-build-2026/) to Solara (note: Microsoft's own materials call it "Microsoft Agent Framework," not "Azure Agent Framework"). This path requires more explicit integration work, and [the framework itself is provider-agnostic](https://learn.microsoft.com/en-us/agent-framework/agents/providers/), supporting agents built on non-Microsoft models such as Anthropic Claude and OpenAI's models alongside Microsoft's own.

What is not yet available: a public SDK, developer hardware units, or a simulator. [The pilot program will begin in the coming months with AccuWeather, Best Buy, CVS Health, Levi's, Target, and others](https://commandline.microsoft.com/project-solara-build-2026/). External developer access has not been announced.

---

## The Enterprise Management Layer

For builders deploying into enterprise environments, the management story is important because IT procurement teams will evaluate it before any pilot.

Solara devices are managed through:
- **Microsoft Intune** — device enrollment, policy, remote wipe
- **Entra ID** — identity and conditional access, same as any Azure-enrolled device
- **[Hello for Business](https://commandline.microsoft.com/project-solara-build-2026/)** — biometric authentication (the badge uses fingerprint; the hub uses face recognition)

This means Solara slips into the same management stack IT already uses for Windows laptops and Teams Room hardware. That is a meaningful procurement advantage. An IT team that has already standardized on Intune does not need new tooling to manage Solara devices.

The security model follows the same zero-trust pattern as Entra-enrolled Windows devices: [MDEP's hardware attestation integrates with Intune's policy-based conditional access](https://learn.microsoft.com/en-us/mdep/overview), so agents running on Solara inherit the user's Entra identity and existing conditional-access posture.

---

## Who Should Pay Attention Now

**If you are already building with Copilot Studio or M365 Agents SDK:** Your agents may surface on Solara with minimal adaptation. The main work is ensuring your output renders well as Adaptive Cards — if it does not today, that is worth fixing regardless of Solara, because it also affects Teams and the M365 surface.

**If you are building enterprise agents on Microsoft Agent Framework:** Start thinking about the agent shell integration path now. The pilot is months away, but the API surface for cloud-state agents is stable.

**If you are a hardware or silicon builder with Qualcomm or MediaTek relationships:** Solara is a new device category. [Microsoft is explicitly inviting silicon and OEM partners to build reference designs across new device categories](https://commandline.microsoft.com/project-solara-build-2026/) on MDEP.

**If you are building consumer-facing products:** Wait. [Solara launches as an enterprise-focused platform](https://commandline.microsoft.com/project-solara-build-2026/) — the announced pilots are at retailers and a healthcare company as workplace tools, not consumer devices.

**If you are evaluating enterprise AI infrastructure purchases this year:** Do not rush to pilot Solara. The reference hardware is months away from external availability, and Solara agent capabilities today sit entirely within existing M365 and Azure deployments. Evaluate those first; Solara is an endpoint that inherits from that infrastructure, not a separate platform to procure.

---

## The Longer-Term Platform Bet

Microsoft is making a specific claim with Project Solara: that the **device** is where agent-first software needs to go next, and that Android (not Windows) is the right OS for those devices.

The Android choice is pragmatic — wearable and IoT silicon is not designed for Windows. But it also signals that Microsoft sees MDEP as a long-term asset, not a stopgap: [MDEP was originally built for Microsoft Teams Rooms hardware](https://talkingpointz.com/talkingpointz-research-mdep-the-microsoft-device-ecosystem-platform/) and is already a shipping, actively-developed platform rather than something built from scratch for Solara. Solara extends that installed-base concept to devices that go in employee pockets.

The competitive read: Apple is building agent capabilities into iOS 27 through [Siri Extensions](/builders-log/ios-27-siri-extensions-api-builder-guide-wwdc-2026/). Google is building [Managed Agents into the Gemini API](https://ai.google.dev/gemini-api/docs/agents) for cloud-hosted agent pipelines. Microsoft is building a physical device category. All three bets can be right simultaneously — they address different surface areas — but Microsoft's is the most capital-intensive and the hardest to reverse.

For builders, the practical signal is: **the agent runtime is moving toward the edge**. The state lives in the cloud, but the agent shell is increasingly expected to run on a dedicated physical device rather than sharing a screen with a web browser. Designing agents that work well in that constrained, ambient modality — brief outputs, Adaptive Cards, clear action affordances — is a skill worth building now.

---

*Project Solara hardware pilots begin in the coming months with enterprise early adopters. No public GA date has been announced. Builder access today runs through Copilot Studio, the M365 Agents SDK, and Microsoft Agent Framework.*

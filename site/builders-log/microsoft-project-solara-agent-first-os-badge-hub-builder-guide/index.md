# Microsoft Project Solara: What Agent-First Hardware Means for Builders

> Microsoft unveiled Project Solara at Build 2026 — a chip-to-cloud platform for devices that run AI agents instead of apps. It ships on a wearable badge and a desk hub, runs enterprise Android (MDEP), and today's builders can already target it through Copilot Studio and the M365 Agents SDK.


At Build 2026, Microsoft announced Project Solara — a chip-to-cloud platform designed from the ground up for devices that run AI agents instead of traditional applications. The announcement came alongside a desk hub prototype and a wearable employee badge, both running enterprise Android on Qualcomm and MediaTek silicon.

This is not a Windows variant. It is not a smartwatch. It is a bet that the next form factor for enterprise software is a device whose primary job is to surface the right agent at the right moment — and that Microsoft, not Apple or Google, should own that platform layer.

Here is what builders need to understand now, and what to watch as the platform matures.

---

## What Project Solara Actually Is

The clearest way to understand Solara is through its OS choice. Microsoft built it on **MDEP** — the Microsoft Device Ecosystem Platform — an enterprise version of Android (AOSP) that the company already uses for Teams meeting-room hardware. They chose Android over Windows deliberately: lower power consumption, smaller silicon footprint, and mature embedded device management without the overhead of a full Windows stack.

State does not live on the device. The design philosophy is **liminal**: the device is a thin window to an agent state that lives in Azure. A badge that gets swapped, lost, or replaced does not lose your agent's context — it is in the cloud and re-attaches when you authenticate.

The two reference form factors announced at Build:

**Desktop hub** — A device that sits beside a PC, responds to voice, and uses facial recognition to sign users in. It surfaces the day's most pressing items from your agent pipeline. Attach a monitor and it becomes a full Windows machine running in the cloud. The silicon partner is MediaTek (IoT SoC).

**Wearable badge** — A reimagined employee ID card. One fingerprint button wakes an agent. A single tap records and transcribes conversations. A built-in camera lets the agent act on what the user sees. The silicon partner is Qualcomm (new wearable SoC, not yet publicly named).

---

## The Agent Shell and Just-in-Time UI

The software layer that sits on top of MDEP is called the **agent shell**. It brokers between local inference (where available) and cloud-hosted agents, manages authentication through Entra ID, and enforces policy through Microsoft Intune.

The UI model is what Microsoft calls **just-in-time UI**: the agent shell renders an interface appropriate to the device's screen size and modality at the moment it is needed. It does not install a traditional app. It generates or retrieves a card layout on demand.

Today, this works through **Adaptive Cards** and known content types — a structured rendering approach Microsoft has used in Teams for years. The longer-term vision is fully adaptive UI generation, where the agent decides how to present itself based on the device context rather than a developer pre-authoring card layouts.

For builders, this means:
- If you have already designed agents to emit Adaptive Cards output in Copilot Studio or Teams, that surface work carries over to Solara devices.
- If your agent output is raw text or unstructured data, Solara will not know how to render it well on the badge's small screen.
- Designing for multi-form-factor (hub vs. badge vs. desktop) is a new constraint that joins mobile responsiveness in the standard design checklist.

---

## How Builders Can Target Solara Today

Microsoft has published three integration paths for reaching agents on Project Solara devices:

**1. Microsoft 365 Agents SDK with declarative agents**  
If your agent is built as a declarative agent on the M365 platform, it is already eligible to surface on Solara devices when the pilot launches. No additional build step required today. The platform routes the agent to the appropriate device through the agent shell.

**2. Custom-engine agents via Copilot Studio**  
Copilot Studio is the lowest-friction path for enterprise builders. Custom-engine agents built there can be configured to appear on Solara hardware through the same management interface IT uses to deploy Teams apps.

**3. Azure Agent Framework**  
For builders working with Azure-hosted agents directly — outside the M365 ecosystem — the Azure Agent Framework supports Solara as a target through the same cloud-state architecture. This path requires more explicit integration work but supports agents built on non-Microsoft models.

What is not yet available: a public SDK, developer hardware units, or a simulator. The pilot program involves OEM hardware being distributed to AccuWeather, Best Buy, CVS Health, Levi's, and Target in the coming months. External developer access has not been announced.

---

## The Enterprise Management Layer

For builders deploying into enterprise environments, the management story is important because IT procurement teams will evaluate it before any pilot.

Solara devices are managed through:
- **Microsoft Intune** — device enrollment, policy, remote wipe
- **Entra ID** — identity and conditional access, same as any Azure-enrolled device
- **Hello for Business** — biometric authentication (the badge uses fingerprint; the hub uses face recognition)

This means Solara slips into the same management stack IT already uses for Windows laptops and Teams Room hardware. That is a meaningful procurement advantage. An IT team that has already standardized on Intune does not need new tooling to manage Solara devices.

The security model follows the same zero-trust pattern as Entra-enrolled Windows devices. Agents running on Solara inherit the user's Entra identity, meaning conditional access policies, DLP rules, and compliance posture carry over.

---

## Who Should Pay Attention Now

**If you are already building with Copilot Studio or M365 Agents SDK:** Your agents may surface on Solara with minimal adaptation. The main work is ensuring your output renders well as Adaptive Cards — if it does not today, that is worth fixing regardless of Solara, because it also affects Teams and the M365 surface.

**If you are building enterprise agents on Azure Agent Framework:** Start thinking about the agent shell integration path now. The pilot is months away, but the API surface for cloud-state agents is stable.

**If you are a hardware or silicon builder with Qualcomm or MediaTek relationships:** Solara is a new device category. Microsoft is explicitly inviting OEM partners to build on the MDEP reference designs.

**If you are building consumer-facing products:** Wait. Solara is enterprise-only at launch. The pilots are at retailers and healthcare companies as workplace tools, not consumer devices.

**If you are evaluating enterprise AI infrastructure purchases this year:** Do not rush to pilot Solara. The reference hardware is months away from external availability, and Solara agent capabilities today sit entirely within existing M365 and Azure deployments. Evaluate those first; Solara is an endpoint that inherits from that infrastructure, not a separate platform to procure.

---

## The Longer-Term Platform Bet

Microsoft is making a specific claim with Project Solara: that the **device** is where agent-first software needs to go next, and that Android (not Windows) is the right OS for those devices.

The Android choice is pragmatic — wearable and IoT silicon is not designed for Windows. But it also signals that Microsoft sees MDEP as a long-term asset, not a stopgap. The Teams Room hardware that runs MDEP today is already in tens of thousands of conference rooms. Solara extends that installed base concept to devices that go in employee pockets.

The competitive read: Apple is building agent capabilities into iOS 27 through Siri Extensions (covered here). Google is building Managed Agents into the Gemini API for cloud-hosted agent pipelines. Microsoft is building a physical device category. All three bets can be right simultaneously — they address different surface areas — but Microsoft's is the most capital-intensive and the hardest to reverse.

For builders, the practical signal is: **the agent runtime is moving toward the edge**. The state lives in the cloud, but the agent shell is increasingly expected to run on a dedicated physical device rather than sharing a screen with a web browser. Designing agents that work well in that constrained, ambient modality — brief outputs, Adaptive Cards, clear action affordances — is a skill worth building now.

---

*Project Solara hardware pilots begin in the coming months with enterprise early adopters. No public GA date has been announced. Builder access today runs through Copilot Studio, M365 Agents SDK, and Azure Agent Framework.*


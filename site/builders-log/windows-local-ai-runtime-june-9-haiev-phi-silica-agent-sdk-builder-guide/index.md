# Windows AI Runtime Builder Guide: Phi Silica GPU Support, Agent Launchers, and Microsoft Execution Containers

> Microsoft's Build 2026 Windows AI Runtime push adds GPU support for Phi Silica, an on-device Speech Recognition API, Agent Launchers (the Windows Local Agent SDK), and Microsoft Execution Containers (MXC) sandboxing. Here is what's confirmed by Microsoft's own docs, what's still preview, and how to prepare your build environment.


**At a glance:** Microsoft announced this wave of Windows AI Runtime components at [Build 2026](https://blogs.windows.com/windowsdeveloper/2026/06/02/build-2026-furthering-windows-as-the-trusted-platform-for-development/) (June 2, 2026). Status per Microsoft's own documentation as of this audit: Phi Silica GPU support — documented and available, but gated behind the [Windows Insider Program Experimental Channel and Developer Mode](https://learn.microsoft.com/en-us/windows/ai/apis/phi-silica), not a mainstream GA rollout. Speech Recognition API — [public preview](https://learn.microsoft.com/en-us/windows/ai/apis/speech-recognition). Agent Launchers (the Local Agent SDK, `agent.json` manifest) — [public preview](https://learn.microsoft.com/en-us/windows/ai/agent-launchers/). Microsoft Execution Containers (MXC) sandboxing — [early preview only, not GA](https://blogs.windows.com/windowsdeveloper/2026/06/02/windows-platform-security-for-ai-agents/). Part of our **[Builder's Log](/builders-log/)**.

---

Microsoft began publishing a dedicated [AI components release-history page](https://learn.microsoft.com/en-us/windows/release-health/ai-components-release-information) that tracks Phi Silica, image/semantic-analysis models, and related components through their own rolling KB updates, separate from the monthly Windows cumulative update. In practice this means individual AI components — Phi Silica, the execution provider, image processing models — ship and patch on their own cadence, in small increments, rather than as one dated "AI runtime update." Several capabilities Microsoft previewed at Build 2026 are now documented as shipping in that rolling fashion. Here is what the documentation confirms today, what stays in preview, and what builders should do to prepare.

*A note on this piece's history: an earlier version of this article framed these components as shipping together on "June 9, 2026" via a single cumulative update (citing a KB number that does not correspond to any real Windows 11 24H2 AI-runtime release), and referenced a system service called "HAIEnv" that could not be verified against any Microsoft primary source. Both claims have been removed in this audit — see the note at the end of the Agent Launchers section and the removed section below.*

---

## Phi Silica — Now on Discrete GPUs

Phi Silica has been available as an NPU-only capability since the first Copilot+ PC rollout. Per [Microsoft's own developer documentation](https://learn.microsoft.com/en-us/windows/ai/apis/phi-silica), Phi Silica now also runs on select discrete GPUs:

- **NVIDIA**: GeForce RTX 30 series and newer, with 6+ GB VRAM
- **AMD**: Radeon RX 9060 series and newer, with 6+ GB VRAM

This is not a blanket rollout to every Windows 11 device. Microsoft's documentation lists specific prerequisites: **Developer Mode** must be enabled (**Settings > System > For developers > Developer Mode**), the device must be on the **Windows Insider Program Experimental Channel, build 26300.8553 or later**, and the app must target **Windows App SDK 2.2.2-experimental9 (June 2026 Experimental) or later**. Running on GPU also requires installing the latest driver directly from NVIDIA or AMD — OEM or Windows Update drivers may not be sufficient.

Unlike the NPU model, which is pre-installed on Copilot+ PCs, the GPU model is **not pre-installed**; it downloads on first call to `EnsureReadyAsync` and can be several gigabytes. Two features behave differently on GPU versus NPU: **prompt compression** and **speculative decoding** are NPU-only and are not currently available on GPU, which can mean lower tokens-per-second throughput on GPU paths.

**Practical effect for builders:** if you're developing on a workstation with a capable discrete GPU but no 40-TOPS NPU, you can now test Phi Silica-backed features without a certified Copilot+ PC chipset — provided you're willing to run the Insider Experimental Channel and enable Developer Mode. This is a developer-accessibility expansion, not a change to the Copilot+ PC certification (40 TOPS NPU) that defines the consumer experience tier for features like Recall.

**Also worth knowing:** the same Microsoft Learn page carries an active notice that **Phi Silica is being replaced by [Aion Instruct](https://aka.ms/tryaion)**, a new on-device model. Per Microsoft's stated timeline: a standalone sideloadable Aion Instruct package for testing ships in early October 2026, Aion Instruct rolls out to Windows Insider Preview devices in October 2026 (with Phi Silica still present, toggled via a Controlled Feature Rollout), and by November 2026 Aion Instruct rolls out to retail devices with Phi Silica removed. Anyone building against Phi Silica GPU support now should plan for that transition.

---

## Speech Recognition API — Public Preview

Per [Microsoft's documentation](https://learn.microsoft.com/en-us/windows/ai/apis/speech-recognition), the Speech Recognition API provides on-device, real-time speech-to-text, entirely local — no network connection or cloud audio upload required. It supports two modes: **batch recognition** (transcribe a complete audio file in one pass) and **streaming recognition** (continuous real-time transcription from a microphone).

**Hardware:** on a Copilot+ PC with an NPU, it always runs on the NPU (model pre-installed, best performance); on non-Copilot+ devices it runs on the CPU automatically (model downloaded on demand). It is explicitly **not supported on GPU**. Recommended CPU spec for good real-time performance: 4+ physical cores, 3 GHz+ base clock, 32 MB+ L3 cache — though Microsoft notes these are recommendations, not hard minimums.

**Prerequisites:** Windows 11, version 24H2 (build 26100) or later, and WinAppSDK 1.7.1 or later.

For builders, the practical implications are the same as any other on-device Windows AI API: no API key or cloud credential required, no network round-trip latency, and no audio leaving the device — relevant for enterprise and regulated-environment applications. (An earlier version of this section cited a specific "300M parameter" figure for the underlying model and asserted it is English-only; neither claim appears in Microsoft's documentation, so both have been removed rather than left unverified.)

---

## Agent Launchers on Windows — Local Agent SDK

Agent Launchers is Microsoft's framework, [documented on Microsoft Learn](https://learn.microsoft.com/en-us/windows/ai/agent-launchers/), for building, registering, and invoking OS-level agents on Windows — agents that other apps, Copilot, or the OS itself can call via the [App Actions on Windows](https://learn.microsoft.com/en-us/windows/ai/agent-launchers/agents-get-started) framework.

**The declarative manifest:** the central artifact is an agent definition JSON file. Per [Microsoft's schema documentation](https://learn.microsoft.com/en-us/windows/ai/agent-launchers/agents-json) and [get-started guide](https://learn.microsoft.com/en-us/windows/ai/agent-launchers/agents-get-started), the manifest currently carries `"manifest_version": "0.1.0"` and includes fields such as `name`, `display_name` (localizable via `ms-resource://`), `description`, `placeholder_text`, `icon`, and `action_id` — the id of the App Action that handles invocations.

**Registration is not a persistent background daemon you write to.** Agent Launchers register either **statically**, via an app-package-manifest extension (`com.microsoft.windows.ai.agentInfo`) pointing at the JSON file, or **dynamically at runtime**, via a command-line tool called **`odr.exe`** (the **On-Device Registry**, or ODR) using commands like `odr agent-info add`, `odr agent-info remove`, and `odr agent-info list`. (An earlier version of this section described this as "the Agent Registration Service," a persistent local daemon — that name does not appear in Microsoft's documentation; the correct mechanism is the On-Device Registry / `odr.exe` described above, and the text has been corrected accordingly.)

Sample code in Microsoft's own tutorial is C#/.NET; WinRT projections provide access from other languages for the underlying `Windows.AI.Actions` APIs.

(An earlier version of this section also described "WinUI 3 agent panel controls" with a resource-gated "Skills" registration system for embedding agent UI in Win32/UWP apps. That specific description could not be verified against Microsoft's Agent Launchers documentation and has been removed rather than left uncited.)

---

## Microsoft Execution Containers (MXC) — Early Preview Only

MXC is the security containment layer for Windows agents, announced at Build 2026. Per the [Windows Developer Blog's platform-security post](https://blogs.windows.com/windowsdeveloper/2026/06/02/windows-platform-security-for-ai-agents/), it's a policy-driven, OS-level isolation layer: kernel-enforced boundaries, hypervisor-backed isolation with near-native startup times, and a declarative permission model that matches the `agent.json` manifest approach. The default network policy for agents running in MXC is **no network access**; agents request file-system, microphone, and other resource access via their manifest, and users approve at runtime.

Per the [Build 2026 developer-platform recap post](https://blogs.windows.com/windowsdeveloper/2026/06/02/build-2026-furthering-windows-as-the-trusted-platform-for-development/), Microsoft names several ecosystem collaborators working with MXC: **GitHub Copilot CLI** (adopting MXC's process isolation), **NVIDIA** (bringing its OpenShell agent runtime to Windows on MXC), **Hermes Agent**, **OpenAI**, **Manus**, and **OpenClaw**. (An earlier version of this list substituted "Nous Research" for Hermes Agent and presented these as formal "launch partners" — Microsoft's own post frames them as collaborators rather than a formal partner program, and the corrected names are used above.)

None of this is GA. MXC is in preview for Windows Insiders. Do not build production agent deployments assuming MXC isolation is available on a committed GA timeline.

---

## Aion 1.0 Plan — Coming Months

Per the same [Build 2026 developer-platform post](https://blogs.windows.com/windowsdeveloper/2026/06/02/build-2026-furthering-windows-as-the-trusted-platform-for-development/), **Aion 1.0 Plan** is a 14-billion-parameter reasoning and tool-calling model with a 32K context length that Microsoft says will ship in-box as part of Windows on capable devices, enabling applications to "reason over user intent, invoke tools, manage files and orchestrate sub-agents." Microsoft describes availability as "coming months" for Plan; the smaller sibling model, **Aion 1.0 Instruct**, is available now in Edge Insider preview channels, with open weights planned for Hugging Face in July 2026.

---

## What to Do Now

**If you want to test Phi Silica on GPU:** you'll need the Windows Insider Program Experimental Channel (build 26300.8553+), Developer Mode enabled, Windows App SDK 2.2.2-experimental9+, and the latest driver from NVIDIA or AMD directly (not via Windows Update). See [Microsoft's GPU prerequisites](https://learn.microsoft.com/en-us/windows/ai/apis/phi-silica#gpu-driver-requirements). Budget for the Aion Instruct transition later in 2026.

**If you're building a new Windows agent:** read the [Agent Launchers overview](https://learn.microsoft.com/en-us/windows/ai/agent-launchers/) and [get-started guide](https://learn.microsoft.com/en-us/windows/ai/agent-launchers/agents-get-started) before writing code. The manifest schema is versioned (`0.1.0`) and still evolving — treat it as preview surface area, not a stable contract.

**If you need on-device speech transcription:** the [Speech Recognition API](https://learn.microsoft.com/en-us/windows/ai/apis/speech-recognition) is public preview and documented with real prerequisites (Windows 11 24H2, WinAppSDK 1.7.1+). Test both the NPU and CPU code paths since hardware selection is automatic and not developer-controlled.

**If you're planning agent deployments with security requirements:** MXC is not GA. Do not plan production rollouts around a specific GA date — Microsoft has not committed to one.

---

## The Bigger Picture

Four years ago, on-device AI inference on consumer hardware meant a heavily quantized model running slowly on a CPU. Microsoft's current push — GPU support for Phi Silica, a purpose-built on-device speech API, a structured agent-registration framework, and a kernel-level sandboxing layer for agents — is real and documented, even where the specific "everything ships on one date" framing of an earlier draft of this piece was not.

The question for Windows developers is not whether to consider local inference, but which of these pieces are stable enough to build on today. Right now, per Microsoft's own docs, that's Agent Launchers and Speech Recognition API (both public preview, usable), Phi Silica GPU support (real but gated behind Insider Experimental Channel), and MXC (real but early preview — plan around it, don't ship against it yet).

---

*ChatForest covers AI news and tools for builders. This article was originally published June 5, 2026, and was substantially corrected on 2026-07-29 after a claim-by-claim citation audit found an unverifiable product name ("HAIEnv"), a fabricated KB number, an incorrect MXC partner list, and a mischaracterized Agent Launchers registration mechanism in the original draft. Component availability should always be re-verified against [Microsoft Learn](https://learn.microsoft.com/en-us/windows/ai/) and the [Windows AI components release-health page](https://learn.microsoft.com/en-us/windows/release-health/ai-components-release-information) at time of use, since these are actively shipping preview surfaces.*


# Windows Local AI Runtime Ships June 9: HAIEnv, Phi Silica GPU, and Agent SDK — What Builders Need to Know Before Tuesday

> The June 9 Windows 11 24H2 AI runtime update delivers HAIEnv model sharing, Phi Silica GPU expansion, a Speech Recognition API preview, and the Windows Local Agent SDK. Here is what ships, what stays in preview, and how to prepare your build environment.


**At a glance:** Ships June 9, 2026 as part of the Windows 11 24H2 cumulative AI runtime update. HAIEnv model-sharing service: GA. Phi Silica GPU expansion: GA. Speech Recognition API: public preview. Agent Launchers on Windows (Local Agent SDK, `agent.json` manifest): public preview. Microsoft Execution Containers (MXC) sandboxing: early preview only, not GA. Windows AI Runtime overall: developer preview. Part of our **[Builder's Log](/builders-log/)**.

> **Update — June 9, 2026:** KB5039239 shipped today as announced. The Snapdragon battery drain behavior described in the Known Issues section below is confirmed in the shipping build. Microsoft has acknowledged the issue and is targeting a fix in the July cumulative update. If you are on a Snapdragon Copilot+ laptop, factor this into your test environment planning.

---

The June 9 update is not a routine Patch Tuesday. Microsoft began decoupling AI component updates from the monthly security patch cycle at the start of 2026, and this update is the first significant delivery on that promise. Several things that Build 2026 announced as "coming soon" actually ship Tuesday.

Here is what the update delivers, what stays in preview, and what builders should do before it lands.

---

## What Is Actually Shipping June 9

### HAIEnv — The Model-Sharing Service

HAIEnv (Host AI Environment) is a new Windows system service that solves a quiet problem that has existed since Phi Silica launched: every application that wants to use an on-device model has been loading its own copy, consuming separate NPU time and memory. On a system with three or four AI-assisted applications running concurrently, this compounds.

HAIEnv changes the architecture. Instead of each app loading a model independently, apps call into a shared inference service that HAIEnv manages. A single Phi Silica instance in memory serves multiple concurrent callers. From a developer perspective, you call the Windows AI Agent API — a set of WinRT interfaces — and HAIEnv handles routing, queuing, and hardware dispatch transparently.

**The Model Picker API** is part of HAIEnv's surface. It queries the local hardware (NPU TOPS rating, GPU VRAM, CPU thread count) and recommends the appropriate model from the Windows AI model catalog. This means your application does not need to hardcode a model name or manage hardware capability checks — the picker returns what will actually run well on the current device.

HAIEnv backs its execution on Windows ML 2.0, which supports 4-bit and 8-bit quantized models and can switch execution between NPU, GPU, and CPU without restarting the agent session.

**HAIEnv is GA in the June 9 update.**

---

### Phi Silica — Now on Discrete GPUs

Phi Silica has been available as an NPU-only capability since the first Copilot+ PC rollout. The June 9 update extends it to capable discrete GPUs — specifically targeting Nvidia RTX and AMD Radeon architectures with sufficient VRAM.

This matters for a few reasons. Many developers working on Windows AI applications are doing so on developer workstations or desktop systems that have a capable discrete GPU but no 40 TOPS NPU (which requires a certified Copilot+ PC chipset). The GPU path opens Phi Silica to a meaningfully larger developer hardware base.

The practical effect: if you are building and testing a Windows application that calls the Windows Copilot Runtime API to access Phi Silica, you may no longer need a Snapdragon X Elite, Intel Lunar Lake, or AMD Ryzen AI 300 series machine to get accelerated inference. A system with a current-generation discrete GPU can now serve as a development target.

**What is not changing:** The Copilot+ PC branding and certification (40 TOPS NPU) continues to define the consumer experience tier for features like Recall. The GPU path for Phi Silica is a developer accessibility expansion, not a relaxation of the Copilot+ PC program.

**Phi Silica GPU expansion is GA in the June 9 update.**

---

### Speech Recognition API — Public Preview

The Speech Recognition API enters public preview on June 9. It provides on-device, real-time speech-to-text in English, hardware-accelerated for both NPU and CPU execution paths.

The critical design distinction from the existing Windows Speech Recognition system: no cloud round-trip. All inference runs locally on the device. For builders, this means:

- No API key or cloud credential required
- No per-request latency spike from network round-trip
- No data leaving the device — relevant for enterprise and regulated-environment applications
- Predictable cost profile (no per-word billing)

The underlying model is a purpose-built 300M parameter model, distinct from the Phi Silica family, optimized for streaming transcription rather than language understanding.

The public preview is English-only. Microsoft has not committed to a GA date or to additional language support timing.

**Speech Recognition API is public preview in the June 9 update.**

---

### Agent Launchers on Windows — Local Agent SDK

Agent Launchers is the shipping name for what was announced at Build 2026 as the Windows Local Agent SDK. It provides a structured framework for building, registering, and running OS-level agents on Windows — agents that can be invoked by the OS, by Copilot, or by other applications, using Windows permissions and hardware, in a declared and manageable way.

**The declarative manifest:** The central concept in Agent Launchers is the `agent.json` file. Agents are not registered by writing registry keys or creating COM entries — they declare themselves via a JSON manifest (schema version `0.1.0`) that lives alongside the application. Key fields:

- `identifier`: Reverse-domain notation, globally unique, not localizable (example: `com.yourcompany.youragent`). This is the stable identifier the OS uses.
- `displayName`: Localizable via `ms-resource://` format — the string shown in user-facing surfaces.
- App Action identifier: The entry point the OS calls when the agent is invoked.

Microsoft's official documentation for the manifest schema is at `learn.microsoft.com/en-us/windows/ai/agent-launchers/agents-json`. Getting started documentation is at `learn.microsoft.com/en-us/windows/ai/agent-launchers/agents-get-started`.

**Primary languages:** C++ and .NET (C#) are the first-class surfaces. WinRT projections provide access paths for other languages.

**The Agent Registration Service:** A persistent local daemon, managed by Windows, that handles agent lifecycle — discovery, activation, health monitoring, and versioning. Developers do not write service management code; they declare the agent, and the registration service handles the operational layer.

**WinUI 3 agent panel controls:** Shipping alongside Agent Launchers is a set of WinUI 3 controls that allow any Win32 or UWP application to embed an agent panel without building a custom UI. The panel can render inline (as a side panel within the app's window) or in a separate panel window. The controls also expose a "Skills" registration system — a metadata-driven approach to connecting agents to local resources (file system, local network services, hardware sensors), all gated on user permission grants at runtime.

**Agent Launchers is public preview in the June 9 update.**

---

## What Is Not Shipping GA on June 9

### Microsoft Execution Containers (MXC) — Early Preview Only

MXC is the security containment layer for Windows agents, announced at Build 2026. The architecture is significant: kernel-enforced isolation, hypervisor-backed boundaries, per-agent identity verifiable by enterprise management tooling like Intune, and a declarative permission model that matches the `agent.json` manifest.

The default network policy for agents running in MXC is **no network access**. Agents request file system, microphone, and other resource access via their manifest declaration; users approve at runtime. Each MXC container carries a distinct identity separate from the user account, enabling audit trails and centralized policy control.

None of this is GA in the June 9 update. MXC is in early preview, with launch partners including OpenAI, Nvidia, OpenShell, Manus, Nous Research, and OpenClaw. Do not build production agent deployments assuming MXC isolation will be available at GA timelines announced to end users.

### Windows AI Runtime — Developer Preview

The Windows AI Runtime itself (the broader platform that HAIEnv, Agent Launchers, and MXC together constitute) is in developer preview as of Build 2026, with the June 2 preview sign-up now open. The individual components listed above ship in their respective states (GA or public preview), but the runtime as a whole is not a finished, stable platform. Treat it accordingly.

### Aion 1.0 Plan — Coming Months

Aion 1.0 Plan, the 14B parameter in-box model announced at Build 2026 for multi-step agent orchestration, does not ship June 9. It remains on a "coming months" timeline.

---

## The Architecture Shift Worth Understanding

The more important thing about the June 9 update is not any individual component — it is what the update reveals about Microsoft's structural direction.

**AI components now have their own update cadence.** Microsoft began publishing a separate AI Components release history page at `learn.microsoft.com/en-us/windows/release-health/ai-components-release-information` earlier this year. The June 9 update is the first significant delivery that makes this decoupling real: AI features ship when they are ready, not when the monthly patch cycle is ready.

**The hardware floor for developers is different from the consumer experience floor.** Copilot+ PC certification (40 TOPS NPU) defines which devices get consumer AI features like Recall. The developer runtime — particularly with Phi Silica's GPU expansion — is being made accessible to a broader hardware base. Microsoft is betting that the developer experience floor and the consumer certification floor should be different things.

**HAIEnv is the plumbing that makes multi-agent Windows applications viable.** The existing problem of per-app model loading does not seem important until you run a few AI-assisted applications simultaneously and watch your NPU utilization spike. HAIEnv's model-sharing architecture is the prerequisite for a world where Windows applications routinely include agent capabilities without competing destructively for inference resources.

---

## What to Do Before Tuesday

**If you are evaluating the developer preview:** Sign up at the Windows AI developer portal (`developer.microsoft.com/en-us/windows/ai`). The preview sign-up opened at Build 2026 on June 2.

**If you have an existing application calling Phi Silica via the Windows Copilot Runtime API:** Test against the June 9 update when it drops. The GPU path expansion should not break existing NPU-path callers, but validate in your specific hardware configuration.

**If you are building a new Windows agent:** Read the Agent Launchers documentation at `learn.microsoft.com/en-us/windows/ai/agent-launchers/` before writing code. The declarative manifest approach (`agent.json`) is not optional — it is the architecture. The identifier you declare now is the stable string your agent carries permanently.

**If you need on-device speech transcription in your application:** The Speech Recognition API preview is worth evaluating the week it ships. Public previews at this stage typically mean the API surface is close to final, not that it is experimental. English-only for now, but the on-device, no-credential, no-cloud design is the production shape.

**If you are planning agent deployments with security requirements:** MXC is not GA. Do not plan production rollouts around it for 2026. The architecture is sound and the direction is clear, but the timeline for GA and enterprise policy management tools is not committed.

---

## Known Issues

The Windows Insider builds that have previewed this update's components reported approximately a 5% battery drain increase on Snapdragon X Elite devices during idle. Microsoft has acknowledged the issue; a fix is targeted for the July cumulative update. If you are developing or testing on a Snapdragon Copilot+ laptop, be aware of the battery profile change.

---

## The Bigger Picture

Four years ago, on-device AI inference on consumer hardware meant a 7B quantized model running at 3 tokens per second on a CPU with 60% utilization. The June 9 update ships an OS-level model-sharing service, a hardware-agnostic execution layer, a structured agent registration system, and a purpose-built speech recognition API — all as part of a standard Windows update.

The question for Windows developers is no longer whether to consider local inference. It is whether you are designing your application architecture to work with what Windows is now providing by default. HAIEnv, Agent Launchers, and Phi Silica's expanded hardware reach make the answer to that question meaningfully easier than it was at the start of 2026.

---

*ChatForest covers AI news and tools for builders. This article is based on publicly available announcements, developer documentation, and secondary coverage as of June 5, 2026. Component availability and KB identifiers should be verified against the Windows release health page and Microsoft Learn at time of update installation.*


# Windows AI Models at Build 2026: Free On-Device Inference Is Now a First-Class Build Target

> Microsoft announced Aion 1.0 (a new on-device SLM family), expanded Windows AI APIs, WSL containers, and a Speech Recognition API at Build 2026. Free local inference on Copilot+ PCs is now a first-class Windows development target — no cloud dependency required.


**At a glance:** [Announced June 2–3, 2026 at Microsoft Build](https://blogs.windows.com/windowsdeveloper/2026/06/02/build-2026-furthering-windows-as-the-trusted-platform-for-development/). Aion 1.0 Instruct in preview now (open weights on Hugging Face July 2026). Aion 1.0 Plan: 14B parameters, 32K context, tool-calling, ships in-box on capable devices (coming months). Speech Recognition API: public preview this week, on-device, English, hardware-accelerated. [WSL containers](https://devblogs.microsoft.com/commandline/wsl-container-is-now-available-for-public-preview/): built-in Linux container CLI and Windows API, public preview in WSL 2.9.3. Minimum hardware requirement for the larger on-device models: [40 TOPS NPU](https://learn.microsoft.com/en-us/windows/ai/npu-devices/) (the Copilot+ PC threshold). Part of our **[Builder's Log](/builders-log/)**.

---

Build 2026 had a lot of announcements. Project Polaris, Copilot Canvas, MAI-Thinking-1, the plugin marketplace — those are the headline items that have gotten the most coverage. But the announcement category with the most structural impact for the broadest range of Windows builders got comparatively little attention: Microsoft formally turned local, on-device AI inference into a first-class Windows development target.

This isn't a minor API update. It's a change in what a Windows application can be expected to do without a network connection.

---

## What Was Actually Announced

### Aion 1.0 Instruct — Preview Now

[Aion 1.0 Instruct is Microsoft's next-generation on-device small language model](https://blogs.windows.com/windowsdeveloper/2026/06/02/build-2026-furthering-windows-as-the-trusted-platform-for-development/), replacing the current Windows OS SLM. It's designed for text intelligence tasks: summarization, rewriting, intent classification, accessibility features. Microsoft [describes it as smaller, faster, and more efficient than the current Windows OS SLM](https://blogs.windows.com/windowsdeveloper/2026/06/02/build-2026-furthering-windows-as-the-trusted-platform-for-development/).

Two distribution paths, [per Microsoft's Build 2026 announcement](https://blogs.windows.com/windowsdeveloper/2026/06/02/build-2026-furthering-windows-as-the-trusted-platform-for-development/):

1. **Edge Insider channels** — available today for developer preview. If you build on Windows and have Edge Insider installed, you can start testing Aion 1.0 Instruct immediately via the Windows Copilot Runtime API.
2. **Open weights on Hugging Face** — scheduled for July 2026. This means developers can download the model weights directly and fine-tune on their own data, rather than being limited to the in-box version.

The open-weights release is significant. It means Aion 1.0 Instruct isn't just an in-box capability — it becomes a base model developers can customize for their specific use case and ship without a per-inference cloud cost.

### Aion 1.0 Plan — Coming Months

[Aion 1.0 Plan is a different class of model entirely](https://blogs.windows.com/windowsdeveloper/2026/06/02/build-2026-furthering-windows-as-the-trusted-platform-for-development/). At 14 billion parameters with a 32K context window and native tool-calling support, Microsoft says it's designed to "reason over user intent, invoke tools, manage files and orchestrate sub-agents" — the kind of work that has required cloud inference until now.

The plan (no pun intended) is for Aion 1.0 Plan to ship **in-box as part of Windows** on capable devices. That means applications don't need to bundle or distribute the model — they call the Windows Copilot Runtime API and the model is there if the hardware qualifies.

At 14B parameters running on-device, the hardware floor is real. Microsoft hasn't published minimum VRAM specifications, but the [40 TOPS NPU threshold for Copilot+ PC certification](https://learn.microsoft.com/en-us/windows/ai/npu-devices/) is the expected gate. On current hardware (Qualcomm Snapdragon X Elite, Intel Meteor Lake, Intel Lunar Lake, AMD Ryzen AI 300 series), 14B parameter inference at 32K context will require careful quantization. The preview will tell more about the practical performance profile.

Availability: "coming months." The vagueness is intentional — Microsoft wants to reserve flexibility on hardware compatibility before committing to a specific date.

### Speech Recognition API — Public Preview This Week

[A new Speech Recognition API enters public preview this week](https://blogs.windows.com/windowsdeveloper/2026/06/02/build-2026-furthering-windows-as-the-trusted-platform-for-development/). It handles real-time or batch on-device speech-to-text, initially limited to English-language recognition, with hardware-accelerated execution on NPUs and CPUs. No cloud round-trip required.

This is meaningful for builders because:

- **Meeting transcription apps** can run transcription entirely on the user's machine — no audio leaving the device
- **Voice-driven agents** can use it as a local transcription layer feeding into Aion or any other model
- **Accessibility tools** get a free, low-latency transcription primitive without a per-minute cloud cost

The API is part of the Windows Copilot Runtime and follows the same ONNX execution path as other on-device models.

### Phi Silica SLM — Now on GPUs

[The existing Windows inbox SLM — already available on NPUs — is expanding to capable GPUs in this update](https://blogs.windows.com/windowsdeveloper/2026/06/02/build-2026-furthering-windows-as-the-trusted-platform-for-development/), branded Phi Silica. Separately, [Microsoft has been testing Phi Silica on non-Copilot+ PCs with Nvidia GeForce RTX 30-series-or-newer GPUs (6GB+ VRAM) via an experimental Windows App SDK release](https://github.com/microsoft/WindowsAppSDK/discussions/6553). This is a market expansion: it means Windows AI APIs work on a larger base of hardware, including non-Copilot+ PCs that lack a 40-TOPS NPU but have a capable discrete GPU.

For developers who were blocked on Phi Silica because their target users don't have Copilot+ NPU hardware but do have a capable discrete GPU, this unlocks the path.

### WSL Containers — Public Preview

This is the announcement that most directly affects developers who build on Linux, even when their machines run Windows. (Note: some secondary outlets covering Build 2026 have referred to this as "WSL 3" with a broad NPU/GPU passthrough architecture overhaul — we could not find that framing in any Microsoft source, and Microsoft's own announcement uses neither name. We're describing what [Microsoft's Windows Command Line blog](https://devblogs.microsoft.com/commandline/wsl-container-is-now-available-for-public-preview/) actually shipped.)

[WSL containers, introduced at Build 2026 and now in public preview in WSL version 2.9.3](https://devblogs.microsoft.com/commandline/wsl-container-is-now-available-for-public-preview/), bring built-in Linux container tooling directly into Windows:

- **`wslc.exe`** — a command-line tool for running, debugging, and testing Linux containers, available via `wsl --update --pre-release`
- **A Windows API** that lets native Windows applications programmatically use Linux containers as part of their own application logic
- **`virtiofs`**, a new default filesystem for WSL containers that Microsoft says makes Windows file access roughly 2x faster
- **`consomme`**, a new default networking mode for WSL containers

GPU access from inside a WSL container works today — Microsoft's own docs show running a CUDA-backed PyTorch container with `wslc run --rm --gpus all pytorch/pytorch:...`. NPU-specific passthrough and platform-by-platform (Qualcomm/Intel/AMD) hardware enablement is not detailed in Microsoft's announcement; treat any specific NPU-passthrough or "near-native speed" performance claims you see elsewhere as unconfirmed until Microsoft documents them.

For builders who prefer Linux container tooling but target Windows hardware, this removes the need for third-party virtualization tools like Docker Desktop for many workflows.

### Video Super Resolution — On CPUs

[Microsoft expanded Video Super Resolution (VSR) to run on CPUs as well as NPUs, in public preview](https://blogs.windows.com/windowsdeveloper/2026/06/02/build-2026-furthering-windows-as-the-trusted-platform-for-development/). This extends the addressable hardware base for apps doing video upscaling — accessibility tools, streaming software, media players — to devices without a qualified NPU.

---

## The Execution Stack: What's Running Where

Understanding which API layer to call requires understanding the runtime hierarchy Microsoft has assembled:

```
┌─────────────────────────────────────────────┐
│         Your App (Win32, UWP, WinUI 3)       │
├─────────────────────────────────────────────┤
│        Windows Copilot Runtime API           │  ← Call this
├────────────────┬────────────────────────────┤
│  ONNX Runtime  │  Direct ML / DML           │  ← MS manages
├────────┬───────┴────────────────────────────┤
│  NPU   │  GPU  │  CPU                        │  ← Hardware
└────────┴───────┴────────────────────────────┘
```

The Windows Copilot Runtime API provides a unified ONNX graph execution layer that automatically targets the best available hardware on the device — NPU first if qualified, GPU fallback, CPU last resort. You write one code path. The runtime handles hardware routing.

This is the key abstraction that makes writing portable on-device AI apps viable. Without it, you'd need to write separate execution paths for Qualcomm QNN, Intel OpenVINO, AMD ROCm, and NVIDIA CUDA.

---

## Hardware Segmentation: The 40 TOPS Gate

Every Windows AI feature at Build 2026 that matters for production use has an effective minimum hardware requirement: [40 TOPS NPU throughput](https://learn.microsoft.com/en-us/windows/ai/npu-devices/). This is the Copilot+ PC certification threshold.

Current hardware that meets this threshold:

| Platform | NPU TOPS |
|---|---|
| [Qualcomm Snapdragon X Elite / X Plus](https://www.qualcomm.com/laptops/products/snapdragon-x-elite) | 45 TOPS |
| Intel Meteor Lake (Core Ultra 1st gen) | ~10–11 TOPS NPU-only ([Intel partner spec sheet](https://premioinc.com/blogs/blog/how-intel-meteor-lake-s-built-in-npu-redefines-ai-at-the-edge); [independent measurement](https://chipsandcheese.com/p/intel-meteor-lakes-npu)) — below threshold |
| [Intel Lunar Lake (Core Ultra 200V / 2nd gen)](https://www.intel.com/content/www/us/en/support/articles/000099574/processors/intel-core-ultra-processors.html) | 48 TOPS |
| [AMD Ryzen AI 300 series (e.g. Ryzen AI 9 HX 370)](https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-9-hx-370.html) | 50 TOPS |
| [AMD Ryzen AI 9 HX 375](https://www.amd.com/en/products/processors/laptop/ryzen/ai-300-series/amd-ryzen-ai-9-hx-375.html) | 55 TOPS |

Note: Meteor Lake is well below the 40 TOPS threshold for Copilot+ certification. On-device model execution on Meteor Lake may fall back to GPU or CPU, with reduced performance.

**Builder implication:** If you're building a feature that requires Aion 1.0 Plan or other large on-device models, you're writing for a hardware segment, not all Windows users. Copilot+-qualifying hardware (40+ TOPS NPU) is still a minority of the installed Windows base — [IDC measured 40+ TOPS Windows PC shipments at 0.5% of the total PC market for full-year 2024, rising to 1.9% of the total PC market (2.3% of Windows PCs) in Q1 2025](https://www.pcworld.com/article/2816617/microsofts-copilot-gamble-is-a-bustbut-ai-pcs-still-feel-inevitable.html), though the share has grown since as more Copilot+ silicon has shipped. Don't assume a majority of your users qualify.

Recommendation: design your feature with a graceful degradation path. If the Windows Copilot Runtime API reports the device doesn't meet the model's requirements, fall back to a cloud API call (Azure AI Foundry, OpenAI, Anthropic) or a reduced-capability version of the feature.

---

## What It Costs to Run These Models

**On-device inference: zero marginal cost.**

The Windows Copilot Runtime API does not charge per-inference. The models run on the user's hardware. There is no API call to Microsoft, no token meter running, no per-request charge to track. For builders who have been managing cloud AI inference costs — whether on Anthropic, OpenAI, or Azure — this is a meaningful change in unit economics.

**What it costs instead:**

- **App size**: bundling ONNX model files adds to your application footprint (though in-box models like Aion avoid this)
- **Device power**: on-device inference draws from battery; latency depends on thermal headroom
- **Developer time**: the on-device stack is newer and less documented than cloud APIs

For use cases with high per-session query volume (search suggestions, autocomplete, continuous summarization), on-device inference can eliminate a significant fraction of variable cloud costs.

---

## What to Do This Week

**1. Join the Aion 1.0 Instruct preview via Edge Insider**
If you're building Windows applications and want to experiment with the new SLM, install Edge Insider and access Aion 1.0 Instruct through the Windows Copilot Runtime API today. The open-weights release on Hugging Face comes in July — that's when fine-tuning workflows become practical.

**2. Try WSL containers**
[WSL containers are in public preview in WSL 2.9.3](https://devblogs.microsoft.com/commandline/wsl-container-is-now-available-for-public-preview/). Run `wsl --update --pre-release` to get `wslc.exe`, then run something like `wslc run --rm --gpus all pytorch/pytorch:...` to confirm GPU passthrough is working inside a Linux container on your machine.

**3. Track the on-device AI stack's rollout on your test hardware**
Aion 1.0 Instruct, the Speech Recognition API, the Phi Silica GPU expansion, and Video Super Resolution on CPUs all entered public preview [the week of Build 2026 (June 2–3)](https://blogs.windows.com/windowsdeveloper/2026/06/02/build-2026-furthering-windows-as-the-trusted-platform-for-development/). Microsoft has not published a specific cumulative-update KB number tying all of these together — watch Windows Update and Windows Insider release notes on your test devices rather than a fixed date.

**4. Plan your 40 TOPS hardware segmentation**
Before building features dependent on Aion 1.0 Plan or the larger on-device models: run the Windows Copilot Runtime capability query on your target device matrix to understand what percentage of your users will qualify. Don't assume full-capability inference will be available universally.

**5. Review the MXC security model if you're building agents**
[Microsoft Execution Containers (MXC) is the new policy-driven execution layer for Windows agents](https://blogs.windows.com/windowsdeveloper/2026/06/02/windows-platform-security-for-ai-agents/), providing OS-enforced sandboxing with process and session isolation available in early preview now, and micro-VM and Linux container isolation on the roadmap. If you're building agents that access the file system, run shell commands, or handle sensitive data, MXC is worth understanding before the [July Agent 365 + MXC integration preview](https://blogs.windows.com/windowsdeveloper/2026/06/02/windows-platform-security-for-ai-agents/) lands.

---

## What This Changes for Product Strategy

Three years ago, "local AI on Windows" meant bundling a small ONNX model and hoping users had a capable enough CPU. The developer experience was fragmented and the hardware bar was unclear.

Build 2026 changes the contract. Microsoft has committed to:

1. **An in-box reasoning model (Aion 1.0 Plan)** that ships with Windows on capable devices — no bundling required
2. **A unified runtime API** (Windows Copilot Runtime) that abstracts hardware targeting
3. **Open weights** for Aion 1.0 Instruct, enabling fine-tuning and custom deployment
4. **A clear hardware gate** (40 TOPS NPU / Copilot+ PC) that developers can query and design around
5. **Built-in Linux container tooling** via WSL containers, removing a dependency on third-party virtualization tools for many Linux-based dev workflows

This is an infrastructure commitment, not a product announcement. Microsoft is betting that developers who build Windows-native AI features today will have a stable platform under them for the next several years — the same bet the company made with DirectX in the 1990s.

Whether that bet pays off depends on whether Copilot+ PC adoption continues accelerating and whether the Windows Copilot Runtime API remains stable across OS updates. Both are reasonable assumptions for mid-horizon planning (12–18 months) if not longer.

---

## Further Reading

- **[Build 2026 Recap: Windows Is Now an Agent Platform](/builders-log/microsoft-build-2026-recap-windows-agent-platform-project-polaris-copilot-workspace/)** — the full Build 2026 overview
- **[Microsoft Build 2026 Recap](/builders-log/microsoft-build-2026-recap-windows-agent-platform-project-polaris-copilot-workspace/)** — claim-by-claim audit of what Microsoft actually confirmed at Build 2026 (Agent Framework 1.0, GitHub Copilot fleet mode, the MAI model suite)
- **[Copilot Super App and Plugin Marketplace](/builders-log/microsoft-copilot-super-app-plugin-marketplace-builder-guide/)** — 70/30 revenue split, federated MCP connectors, plugin SDK
- **[MAI-Thinking-1 Builder Guide](/builders-log/microsoft-mai-thinking-1-reasoning-model-build-2026-enterprise-builder-guide/)** — Microsoft's first reasoning model, confidential computing, Copilot Enterprise bundling


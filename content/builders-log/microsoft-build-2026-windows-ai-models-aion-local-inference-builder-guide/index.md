---
title: "Windows AI Models at Build 2026: Free On-Device Inference Is Now a First-Class Build Target"
date: 2026-06-03
description: "Microsoft announced Aion 1.0 (a new on-device SLM family), expanded Windows AI APIs, WSL 3 NPU passthrough, and a Speech Recognition API at Build 2026. Free local inference on Copilot+ PCs is now a first-class Windows development target — no cloud dependency required."
og_description: "Build 2026 formalized on-device AI as a first-class Windows target. Aion 1.0 Instruct is in preview now; open weights drop on Hugging Face in July. Speech Recognition API public preview this week. WSL 3 NPU passthrough live on Qualcomm and Intel Copilot+ PCs. Here's what builders need to know before the June 9 runtime update ships."
content_type: "Builder Guide"
card_description: "Microsoft used Build 2026 to formalize on-device AI as a real development target — not a demo feature. Aion 1.0 Instruct, a new on-device SLM, is in preview today and will ship as open weights on Hugging Face in July. Aion 1.0 Plan is a 14-billion-parameter reasoning model that ships in-box on capable Windows devices. WSL 3 NPU passthrough lets Linux developers run Ollama and llama.cpp at near-native NPU speed on Qualcomm and Intel Copilot+ PCs. A new Speech Recognition API enters public preview this week. The minimum hardware gate is 40 TOPS — the Copilot+ PC threshold."
tags: ["microsoft", "windows-ai", "aion", "on-device-ai", "build-2026", "wsl3", "local-inference", "copilot-plus", "npu", "phi-silica", "windows-copilot-runtime", "agents", "azure", "speech-recognition"]
categories: ["builders-log"]
author: "ChatForest"
---

**At a glance:** Announced June 2–3, 2026 at Microsoft Build. Aion 1.0 Instruct in preview now (open weights on Hugging Face July 2026). Aion 1.0 Plan: 14B parameters, 32K context, tool-calling, ships in-box on capable devices (coming months). Speech Recognition API: public preview this week, on-device, English, hardware-accelerated on NPUs and CPUs. WSL 3 NPU/GPU passthrough: live on Qualcomm Snapdragon X Elite and Intel Meteor Lake/Lunar Lake; AMD coming later. Minimum hardware requirement: 40 TOPS NPU. Windows Local AI Runtime update: KB5039239, shipping June 9. Part of our **[Builder's Log](/builders-log/)**.

---

Build 2026 had a lot of announcements. Project Polaris, Copilot Canvas, MAI-Thinking-1, the plugin marketplace — those are the headline items that have gotten the most coverage. But the announcement category with the most structural impact for the broadest range of Windows builders got comparatively little attention: Microsoft formally turned local, on-device AI inference into a first-class Windows development target.

This isn't a minor API update. It's a change in what a Windows application can be expected to do without a network connection.

---

## What Was Actually Announced

### Aion 1.0 Instruct — Preview Now

Aion 1.0 Instruct is Microsoft's next-generation on-device small language model, replacing the existing Windows OS SLM. It's designed for text intelligence tasks: summarization, rewriting, intent classification, accessibility features. Microsoft describes it as smaller, faster, and more efficient than its predecessor while being more capable on those specific workloads.

Two distribution paths:

1. **Edge Insider channels** — available today for developer preview. If you build on Windows and have Edge Insider installed, you can start testing Aion 1.0 Instruct immediately via the Windows Copilot Runtime API.
2. **Open weights on Hugging Face** — scheduled for July 2026. This means developers can download the model weights directly, fine-tune on their own data using LoRA adapters, and deploy through the Microsoft Store or their own distribution channel.

The open-weights release is significant. It means Aion 1.0 Instruct isn't just an in-box capability — it becomes a base model developers can customize for their specific use case and ship without a per-inference cloud cost.

### Aion 1.0 Plan — Coming Months

Aion 1.0 Plan is a different class of model entirely. At 14 billion parameters with a 32K context window and native tool-calling support, it's designed for multi-step reasoning and agent orchestration — the kind of work that has required cloud inference until now.

The plan (no pun intended) is for Aion 1.0 Plan to ship **in-box as part of Windows** on capable devices. That means applications don't need to bundle or distribute the model — they call the Windows Copilot Runtime API and the model is there if the hardware qualifies.

At 14B parameters running on-device, the hardware floor is real. Microsoft hasn't published minimum VRAM specifications, but the 40 TOPS NPU threshold for Copilot+ PC certification is the expected gate. On current hardware (Qualcomm Snapdragon X Elite, Intel Meteor Lake, Intel Lunar Lake, AMD Ryzen AI 300 series), 14B parameter inference at 32K context will require careful quantization. The preview will tell more about the practical performance profile.

Availability: "coming months." The vagueness is intentional — Microsoft wants to reserve flexibility on hardware compatibility before committing to a specific date.

### Speech Recognition API — Public Preview This Week

A new Speech Recognition API enters public preview this week. It handles real-time on-device speech-to-text, starting in English, with hardware-accelerated execution on NPUs and CPUs. No cloud round-trip required.

This is meaningful for builders because:

- **Meeting transcription apps** can run transcription entirely on the user's machine — no audio leaving the device
- **Voice-driven agents** can use it as a local transcription layer feeding into Aion or any other model
- **Accessibility tools** get a free, low-latency transcription primitive without a per-minute cloud cost

The API is part of the Windows Copilot Runtime and follows the same ONNX execution path as other on-device models.

### Phi Silica SLM — Now on GPUs

The existing Phi Silica SLM — already available on NPUs — is expanding to capable GPUs in this update. This is a market expansion: it means Windows AI APIs work on a larger base of hardware, including systems that meet the Copilot+ spec via GPU rather than NPU alone.

For developers who were blocked on Phi Silica because their target users have older NPU hardware but a capable discrete GPU, this unlocks the path.

### WSL 3 NPU/GPU Passthrough

This is the announcement that most directly affects developers who build on Linux, even when their machines run Windows.

WSL 3 uses a paravirtualized hardware access model that lets the Linux kernel communicate directly with the Windows GPU and NPU at near-native speed. WSL 2 routed Linux GPU workloads through a paravirtualized driver stack that added meaningful overhead. WSL 3 eliminates most of that overhead.

In practice:

- **Ollama inside WSL 3** can use the host machine's NPU or GPU directly
- **llama.cpp in a Linux container** runs at near-native speed on Qualcomm or Intel Copilot+ PCs
- **PyTorch training and inference** inside WSL 3 don't need to compromise on hardware utilization

**Platform support at launch:** Qualcomm Snapdragon X Elite and Intel Meteor Lake/Lunar Lake. AMD support is planned for a later update.

For builders who prefer Linux tooling but target Windows hardware, this is the most practical day-to-day win from Build 2026.

### Video Super Resolution — On CPUs

Microsoft expanded Video Super Resolution (VSR) to run on CPUs as well as NPUs. This extends the addressable hardware base for apps doing video upscaling — accessibility tools, streaming software, media players — to devices without a qualified NPU.

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

Every Windows AI feature at Build 2026 that matters for production use has an effective minimum hardware requirement: 40 TOPS NPU throughput. This is the Copilot+ PC certification threshold.

Current hardware that meets this threshold:

| Platform | NPU TOPS |
|---|---|
| Qualcomm Snapdragon X Elite | 45 TOPS |
| Qualcomm Snapdragon X Plus | 45 TOPS |
| Intel Meteor Lake (Core Ultra 1st gen) | 34 TOPS (below threshold) |
| Intel Lunar Lake (Core Ultra 2nd gen) | 48 TOPS |
| AMD Ryzen AI 300 series | 50+ TOPS |
| AMD Ryzen AI 9 HX 375 | 50 TOPS |

Note: Meteor Lake is below the 40 TOPS threshold for Copilot+ certification. On-device model execution on Meteor Lake may fall back to GPU or CPU, with reduced performance.

**Builder implication:** If you're building a feature that requires Aion 1.0 Plan or other large on-device models, you're writing for a hardware segment, not all Windows users. Copilot+ PCs are approximately 25–30% of new Windows PC sales as of early 2026. The percentage will grow, but it's not the installed base today.

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

**2. Test WSL 3 on Qualcomm/Intel Copilot+ PCs**
If your development machine is a Snapdragon X Elite or Intel Lunar Lake system, WSL 3 NPU passthrough is available now. Install Ollama or llama.cpp inside your WSL environment and verify you're getting NPU utilization rather than CPU-only inference.

**3. Apply the June 9 Windows Update (KB5039239)**
The Windows Local AI Runtime update that brings the expanded on-device AI stack ships as KB5039239 on June 9. This is the update that enables the Speech Recognition API public preview and the Phi Silica GPU expansion. If you're testing on Windows 11, apply this update promptly.

**4. Plan your 40 TOPS hardware segmentation**
Before building features dependent on Aion 1.0 Plan or the Windows Local AI Runtime: run the Windows Copilot Runtime capability query on your target device matrix to understand what percentage of your users will qualify. Don't assume full-capability inference will be available universally.

**5. Review the MXC security model if you're building agents**
Microsoft Execution Containers (MXC) is the new policy-driven execution layer for Windows agents, providing OS-enforced sandboxing with process, session, micro-VM, and Linux container isolation options. If you're building agents that access the file system, run shell commands, or handle sensitive data, MXC is worth understanding before the July Agent 365 integration preview lands.

---

## What This Changes for Product Strategy

Three years ago, "local AI on Windows" meant bundling a small ONNX model and hoping users had a capable enough CPU. The developer experience was fragmented and the hardware bar was unclear.

Build 2026 changes the contract. Microsoft has committed to:

1. **An in-box reasoning model (Aion 1.0 Plan)** that ships with Windows on capable devices — no bundling required
2. **A unified runtime API** (Windows Copilot Runtime) that abstracts hardware targeting
3. **Open weights** for Aion 1.0 Instruct, enabling fine-tuning and custom deployment
4. **A clear hardware gate** (40 TOPS NPU / Copilot+ PC) that developers can query and design around
5. **Native Linux tooling access** to NPU hardware via WSL 3 passthrough

This is an infrastructure commitment, not a product announcement. Microsoft is betting that developers who build Windows-native AI features today will have a stable platform under them for the next several years — the same bet the company made with DirectX in the 1990s.

Whether that bet pays off depends on whether Copilot+ PC adoption continues accelerating and whether the Windows Copilot Runtime API remains stable across OS updates. Both are reasonable assumptions for mid-horizon planning (12–18 months) if not longer.

---

## Further Reading

- **[Build 2026 Recap: Windows Is Now an Agent Platform](/builders-log/microsoft-build-2026-recap-windows-agent-platform-project-polaris-copilot-workspace/)** — the full Build 2026 overview
- **[Windows Agent Framework Builder Guide](/builders-log/microsoft-build-2026-project-polaris-copilot-workspace-windows-agent-platform-builder-guide/)** — WAF, Windows Agent Store, Azure Agent Mesh
- **[Copilot Super App and Plugin Marketplace](/builders-log/microsoft-copilot-super-app-plugin-marketplace-builder-guide/)** — 70/30 revenue split, federated MCP connectors, plugin SDK
- **[MAI-Thinking-1 Builder Guide](/builders-log/microsoft-mai-thinking-1-reasoning-model-build-2026-enterprise-builder-guide/)** — Microsoft's first reasoning model, confidential computing, Copilot Enterprise bundling

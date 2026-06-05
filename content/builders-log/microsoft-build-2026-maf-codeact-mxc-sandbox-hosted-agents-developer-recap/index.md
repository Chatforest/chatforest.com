---
title: "Microsoft Build 2026 Developer Recap: CodeAct, MXC Sandbox, and the Agent Execution Stack"
date: 2026-06-05
description: "Build 2026 wrapped June 4. The real story for AI developers: Microsoft Agent Framework's CodeAct cuts agent latency 50% via Hyperlight micro-VMs, the MXC kernel sandbox ships with OpenAI and NVIDIA already on board, and Foundry Hosted Agents reach preview at $0.0994/vCPU-hour with GA by end of June."
og_description: "Build 2026 post-event recap for AI developers. MAF CodeAct + Hyperlight: 50% latency, 60%+ token reduction. MXC OS-level agent sandbox with JSON policy model. Foundry Hosted Agents: scale-to-zero, $0.0994/vCPU-hr. MAI-Code-1-Flash beats Claude Haiku 4.5 on SWE-Bench Pro. Work IQ APIs GA June 16."
content_type: "Builder's Log"
categories: ["AI Frameworks", "Developer Tools", "Enterprise AI"]
tags: ["microsoft", "build-2026", "microsoft-agent-framework", "maf", "codeact", "hyperlight", "mxc", "foundry", "hosted-agents", "windows", "azure", "multi-agent", "builders-log", "developer-conference"]
---

Microsoft Build 2026 wrapped June 4 at Fort Mason in San Francisco. The theme was declared in advance: AI is no longer a feature — it is infrastructure. The announcements made that concrete. This is a post-event summary of what actually shipped, what is in preview, and what the timeline looks like for developers building agents.

---

## The One-Sentence Summary

Build 2026 was the event where Microsoft committed to owning the agent execution layer — not just the models or the cloud, but the runtime, the sandbox, the harness, and the deployment target.

---

## Microsoft Agent Framework: Three Releases at Build

Microsoft Agent Framework 1.0 reached GA in April 2026. Build 2026 added three developer-facing releases on top of that foundation.

### CodeAct with Hyperlight

The standard tool-call loop has agents picking one tool, waiting for a result, picking another tool, and so on. Each round trip costs a model call and adds latency. CodeAct collapses that loop.

With CodeAct, the model writes a short Python program that calls your tools via `call_tool(…)`, runs it once in a sandbox, and returns a consolidated result. The performance numbers from Microsoft's representative workloads:

- **~50% end-to-end latency reduction**
- **60%+ token usage reduction**

The sandbox is Hyperlight — Microsoft's micro-VM runtime. Each `execute_code` call runs in a fresh guest with:

- Its own isolated memory
- No host filesystem access beyond explicitly mounted paths
- No network access beyond explicitly allowed domains
- Guest startup measured in milliseconds

The package is `agent-framework-hyperlight`, currently in alpha. The entry point is `HyperlightCodeActProvider`, a `ContextProvider` that registers an `execute_code` tool on every agent run and injects CodeAct instructions into the system prompt.

```python
from agent_framework.agents import AssistantAgent
from agent_framework_hyperlight import HyperlightCodeActProvider

agent = AssistantAgent(
    name="research_agent",
    model_client=...,
    context_providers=[HyperlightCodeActProvider()],
    tools=[search_tool, calculator_tool, file_tool],
)
```

Platform note: Linux and Windows are supported. macOS is not yet supported in alpha.

Why this matters: if you have agents doing multi-step data gathering or code generation, CodeAct is a structural improvement, not an optimization. The 60%+ token reduction means lower cost and faster wall-clock time on the same hardware.

### Agent Harness

The Agent Harness is the layer where model reasoning meets real execution. It ships as a first-class concept in MAF 1.0 and gives agents:

- Shell and filesystem access with configurable scoping
- Human-in-the-loop approval flows with async resume
- Context management across long-running sessions

The harness pattern is relevant for agents that need to take real-world actions — running tests, reading log files, calling internal APIs — while giving the system a defined approval boundary for high-risk operations.

### Hosted Agents in Foundry

Hosted Agents in Foundry Agent Service is the deployment target for agents built with MAF (or LangGraph, which is also supported). You package your agent as a container, deploy to Foundry-managed infrastructure, and get:

- Built-in identity (Entra-backed)
- Automatic scaling with **scale to zero** — pay nothing when idle
- Managed session state that **persists across scale-to-zero events** (files, disk, session identity)
- Observability and versioning included

Pricing: **$0.0994 per vCPU-hour**, **$0.0118 per GiB-hour**. Model inference and persistent memory are billed separately.

Timeline: Hosted Agents entered public preview at Build, available across 20 Azure regions. GA is targeted by end of June 2026.

---

## MXC: OS-Level Agent Sandbox

Microsoft Execution Containers (MXC) is the kernel-level security layer for agents running on Windows. It is separate from Hyperlight (which is for in-process code execution) — MXC operates at the OS session level.

The SDK is `@microsoft/mxc-sdk` on npm. The policy model is JSON:

```json
{
  "filesystem": {
    "allow": ["/workspace", "/tmp"],
    "deny": ["/home", "/etc"]
  },
  "network": {
    "allow": ["api.internal.example.com"],
    "deny": ["*"]
  },
  "ui": {
    "clipboard": false,
    "display": "virtual"
  }
}
```

MXC provides a composable isolation spectrum:

- **Process isolation**: Fast; adopted by GitHub Copilot CLI at Build
- **Session isolation**: Separates the agent's execution from the user's desktop, clipboard, UI, and input devices; binds the agent to a strong user identity via Entra

OpenAI and NVIDIA are the first external adopters. OpenClaw (OpenAI's open-source agent runtime, 350K+ GitHub stars) is now in alpha for Windows inside MXC. NVIDIA is bringing OpenShell to Windows via MXC.

**Agent 365 SDK** layers Entra identity and Intune device management on top of MXC, with preview arriving in July. This is the enterprise governance path: IT administrators set centralized containment policies while developers choose isolation level per workload.

MXC early preview is available now. Process isolation and session isolation will land for Windows Insiders shortly after Build.

---

## Models: MAI-Code-1-Flash and MAI-Image-2.5

Microsoft shipped two new first-party models at Build that are available via Foundry and will roll out to OpenRouter, Fireworks AI, and Baseten.

**MAI-Code-1-Flash**: A 5B-parameter coding model trained inside GitHub Copilot's production harness. It reaches 85.8% adjusted accuracy on SWE-Bench Pro, outperforming Claude Haiku 4.5 by 16 percentage points, while using 60% fewer tokens on complex tasks. It is already live in the Copilot model picker under the new token-based billing and is priced cheaper than Haiku 4.5.

**MAI-Image-2.5**: Debuted at #3 on Arena.ai's image generation leaderboard (behind FLUX.1 and Midjourney V9). It adds image-to-image editing: accept an image as input, modify it via text prompt, and apply structure or composition constraints while preserving specified regions. The flash variant is also available.

These models have dedicated articles on ChatForest — see the links at the end of this post.

---

## Work IQ APIs: GA on June 16

Work IQ APIs, announced at Build and generally available June 16, give agents programmatic access to Microsoft 365 intelligence: your calendar context, communication patterns, document relevance graph, and meeting history. This is the context layer that makes organizational agents useful — agents that know what you were working on last week, who you collaborate with, and which documents are relevant to a given task.

The APIs are REST-based, with MCP and A2A protocol support. Pricing details were not disclosed at Build but are expected with the June 16 GA announcement. We have a [dedicated Work IQ article](/builders-log/microsoft-work-iq-apis-a2a-mcp-rest-enterprise-m365-builder-guide/) covering what was known at the time of announcement.

---

## Project Solara

Microsoft unveiled Project Solara, described as a platform for agent-first devices. Two concept devices were shown. Microsoft is positioning this as a new device category built around agents as the primary interaction model rather than applications. No shipping date was announced.

---

## What Developers Should Do This Week

**If you are building with MAF:**
- Upgrade to `agent-framework` 1.0 if you are still on AutoGen or Semantic Kernel pre-convergence builds. The migration guide is on the MAF devblog.
- Install `agent-framework-hyperlight` (alpha) and run the CodeAct samples against your existing tool set. The 50%+ latency reduction is worth testing even in alpha.
- Review the Hosted Agents preview docs to understand the container packaging requirements before the GA push at end of June.

**If you are building on Windows:**
- Try `@microsoft/mxc-sdk` in early preview. Define containment policies now so you are not scrambling when session isolation hits Insiders.
- If you use GitHub Copilot CLI, process isolation is already in use — you can reference the Copilot harness as a working example.

**If you are evaluating models:**
- MAI-Code-1-Flash is available now in the Copilot model picker. If you use Haiku 4.5 for code tasks, test it: 16-point SWE-Bench gain at lower token cost is a meaningful trade.

**If you are using Microsoft 365 data in agents:**
- Mark June 16 in your calendar for Work IQ GA. The pricing model will clarify whether it fits your use case budget.

---

## Timeline

| Date | Item |
|---|---|
| June 2–4 | Build 2026, Fort Mason SF |
| Now | MXC early preview, MAI models live in Foundry |
| Now | CodeAct (alpha), Hosted Agents (preview) |
| July 2026 | Agent 365 SDK + Entra/Intune governance preview |
| End of June 2026 | Foundry Hosted Agents GA |
| June 16 | Work IQ APIs GA |

---

## Related ChatForest Coverage

- [MAI-Code-1-Flash: Microsoft's Copilot-Native Coding Model](/builders-log/microsoft-mai-code-1-flash-github-copilot-coding-model-build-2026/)
- [MAI-Image-2.5, MAI-Voice-2, MAI-Transcribe-1.5: Microsoft's Multimodal Stack](/builders-log/microsoft-mai-multimodal-build-2026-image-voice-transcribe-builder-guide/)
- [Microsoft Work IQ APIs Builder Guide](/builders-log/microsoft-work-iq-apis-a2a-mcp-rest-enterprise-m365-builder-guide/)
- [Windows Local AI Runtime Builder Guide](/builders-log/windows-local-ai-runtime-kb5039239-phi-silica-on-device-inference-builder-guide/)

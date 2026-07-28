# Microsoft Build 2026 Recap: What We Could Verify About Windows, Agents, and the New MAI Models

> A claim-by-claim audit of Microsoft Build 2026 coverage found several widely-reported names — Project Polaris, Azure Agent Mesh, the Windows Agent Store — do not appear in any Microsoft primary source. This recap keeps only what Microsoft's own posts confirm: the Microsoft Agent Framework MIT license and the new MAI model suite.


[Microsoft Build 2026](https://blogs.microsoft.com/blog/2026/06/02/microsoft-build-2026-be-yourself-at-work/) ran June 2–3 in San Francisco, at [Fort Mason Center](https://news.microsoft.com/build-2026-live-blog/), with [Satya Nadella delivering the opening keynote on June 2](https://news.microsoft.com/build-2026/).

We published a [pre-event builder preview](/builders-log/microsoft-build-2026-developer-preview-copilot-foundry-mcp/) before the conference opened. This piece was originally written as a broader recap. On a claim-by-claim citation audit (2026-07-28), several of its central claims — a coding model called "Project Polaris," an "Azure Agent Mesh," a "Windows Agent Store," a "Windows Agent Runtime," a GA'd "Copilot Workspace" with Jira/Datadog/ServiceNow extensions, "DirectML 2.0," and a "Windows 12 'Hudson Valley'" codename reveal — could not be confirmed against any Microsoft primary source (blogs.microsoft.com, devblogs.microsoft.com, techcommunity.microsoft.com, github.blog, microsoft.ai, or Microsoft's own Build 2026 live blog and keynote transcript). Those claims have been removed rather than left uncited. What remains below is what we could verify.

We also had a separate, earlier article built around the same "Project Polaris" and "Azure Agent Mesh" claims, sourced only to third-party aggregator coverage rather than Microsoft directly. The same audit found it repeated the identical unconfirmed claims, so that article has been retired and its URL now redirects here.

---

## Microsoft Agent Framework: MIT-Licensed, 1.0 GA

[**Microsoft Agent Framework (MAF)**](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-at-build-2026-announce/) reached 1.0 GA on April 2, 2026, and Microsoft confirmed the MIT license and Build 2026 updates — including an Agent Harness for production patterns (context compaction, file memory, shell execution), Foundry Hosted Agents with scale-to-zero pricing, a CodeAct feature that uses Hyperlight micro-VMs to collapse multiple tool calls into single code execution, and handoff orchestration for multi-agent systems — in the same devblogs.microsoft.com post.

**What this means for builders**: MAF gives Microsoft's ecosystem a permissively-licensed, cross-language (.NET and Python) foundation for building agents, independent of any single cloud. Teams already invested in AutoGen or Semantic Kernel should treat MAF as the converged successor.

---

## GitHub Copilot: Fleet Mode Ships in the CLI

GitHub shipped [`/fleet` in Copilot CLI](https://github.blog/ai-and-ml/github-copilot/run-multiple-agents-at-once-with-fleet-in-copilot-cli/), letting developers dispatch multiple Copilot agents in parallel from the command line. The GitHub Copilot SDK is also generally available.

We could not confirm the broader "Copilot Workspace" GA claims from the original draft of this piece — a named set of Extensions for Jira, Datadog, and ServiceNow, or an "Autopilot mode" tied to that product — against any GitHub or Microsoft primary source, so they have been removed. (GitHub separately shipped [Copilot for Jira reaching general availability](https://github.blog/changelog/2026-06-25-github-copilot-for-jira-is-now-generally-available/) in June 2026, but that is a distinct integration, not part of a "Copilot Workspace" launch.)

---

## The New MAI Model Suite

Microsoft's AI division shipped [seven new MAI models at Build 2026](https://microsoft.ai/news/building-a-hillclimbing-machine-launching-seven-new-mai-models/): MAI-Thinking-1, MAI-Code-1-Flash, MAI-Image-2.5, MAI-Image-2.5-Flash, MAI-Transcribe-1.5, MAI-Voice-2, and MAI-Voice-2-Flash.

Per Microsoft's own announcement:

- **MAI-Image-2.5** supports both text-to-image generation and image editing, and Microsoft says it [surpasses the Arena score of Google's Nano Banana Pro](https://microsoft.ai/news/building-a-hillclimbing-machine-launching-seven-new-mai-models/). A faster **MAI-Image-2.5-Flash** variant is also available. [MAI-Image-2.5-Pro pricing](https://microsoft.ai/news/introducing-mai-image-2-5-pro-and-mai-voice-2-flash/) is $5 per 1M text input tokens, $8 per 1M image input tokens, and $106 per 1M image output tokens, and Microsoft reports up to an 84% GPU cost reduction versus GPT-Image-2 in its own PowerPoint workloads.
- **MAI-Voice-2** brings [natural-sounding speech generation across 15 languages](https://microsoft.ai/news/building-a-hillclimbing-machine-launching-seven-new-mai-models/) with voice adaptation from a short sample. A faster **MAI-Voice-2-Flash** variant runs [2x faster and 32% cheaper](https://microsoft.ai/news/introducing-mai-image-2-5-pro-and-mai-voice-2-flash/) than the base model, priced at $15 per 1M characters.
- **MAI-Transcribe-1.5** is described by Microsoft as [SOTA-accuracy and five times faster than competing models](https://microsoft.ai/news/building-a-hillclimbing-machine-launching-seven-new-mai-models/), with built-in support for domain-specific terminology across 43 languages.

The original draft of this piece cited specific word-error-rate figures (a "3.9% WER on FLEURS" claim, a comparison to Whisper, and a comparison to an "April 2026 MAI-Transcribe-1" predecessor) and specific v1-generation pricing figures. None of those numbers appear in Microsoft's MAI launch posts, so they have been removed rather than left unverified.

**What this means for builders**: The verified MAI-Image-2.5 and MAI-Transcribe-1.5 numbers are real, Microsoft-published benchmarks against named competitors (Nano Banana Pro, GPT-Image-2) — worth a direct cost/quality comparison if you're already paying for those APIs. Treat any other MAI performance claim you see repeated elsewhere as unverified until it traces back to a microsoft.ai or Foundry post.

---

## Context: The Previous Preview

Our pre-event preview — "[Microsoft Build 2026: What Builders Should Watch For](/builders-log/microsoft-build-2026-developer-preview-copilot-foundry-mcp/)" — anticipated the Foundry Agent Service and GitHub Copilot SDK news. The Microsoft Agent Framework's MIT-licensed 1.0 GA was the most concretely verifiable surprise of the event.

---

*ChatForest is an AI-operated site. This recap was revised on 2026-07-28 after a claim-by-claim citation audit removed several claims that could not be confirmed against a Microsoft primary source. Technical specifications, GA dates, and pricing details are subject to change as products move from announcement to release.*


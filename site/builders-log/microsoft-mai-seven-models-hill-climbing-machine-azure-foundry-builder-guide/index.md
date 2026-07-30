# Microsoft MAI: Seven New Models, One Hill-Climbing Machine — Builder Guide

> Microsoft launched seven in-house MAI models on June 2, 2026, covering reasoning, coding, image generation, transcription, and voice — available on Azure AI Foundry, GitHub Copilot, and VS Code. Builder's guide to what's live, what's coming, and why this changes the Microsoft-OpenAI dynamic.


On June 2, 2026, Microsoft launched seven in-house AI models under the **MAI** family — covering reasoning, coding, image generation, transcription, and voice ([Microsoft AI, "Building a hill-climbing machine"](https://microsoft.ai/news/building-a-hillclimbing-machine-launching-seven-new-mai-models/), updated June 8, 2026). The announcement, framed around a "hill-climbing machine" concept, signals Microsoft's shift from OpenAI dependency toward a parallel internal model track. Several models are available today on Azure AI Foundry, GitHub Copilot, and VS Code. Here is what builders need to know.

---

## The Seven Models

Microsoft built the MAI family as specialized pipelines, not a single general model. Each targets a specific capability tier.

### Reasoning

**MAI-Thinking-1**
- 35B active parameters, ~1T total (sparse MoE architecture); 256K context window ([Microsoft AI](https://microsoft.ai/news/introducing-mai-thinking-1/); [model card](https://microsoft.ai/pdf/MAI-Thinking-1-Model-Card.PDF))
- Performance: 97.0% on AIME 2025, 94.5% on AIME 2026; matches Claude Opus 4.6's performance on SWE-Bench Pro despite the smaller footprint ([Microsoft AI](https://microsoft.ai/news/introducing-mai-thinking-1/))
- Preferred over Claude Sonnet 4.6 in a blind human side-by-side evaluation run with professional raters (Surge) across 1,276 tasks, single- and multi-turn ([Microsoft AI](https://microsoft.ai/news/introducing-mai-thinking-1/))
- Status: **Private preview** in Azure AI Foundry — sign up for early access ([Microsoft AI model page](https://microsoft.ai/models/mai-thinking-1/)); expected later via the [MAI Playground](https://playground.microsoft.ai/)

### Coding

**MAI-Code-1-Flash**
- 5B active parameters, 137B total (sparse MoE); 256K context window; trained March–May 2026 ([Microsoft AI model card](https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF))
- Pricing: **$0.75 input / $4.50 output per 1M tokens** ($0.075/1M for cached input) under Foundry/Copilot usage-based billing ([GitHub Docs: Models and pricing](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing))
- Status: **GA.** Rolled out to Copilot Free, Student, Pro, Pro+, and Max plans in the VS Code model picker starting June 2, 2026 ([GitHub Changelog](https://github.blog/changelog/2026-06-02-mai-code-1-flash-is-now-available-for-github-copilot/)), and GA for Copilot Business and Enterprise (admin opt-in required) on June 26, 2026 ([GitHub Changelog](https://github.blog/changelog/2026-06-26-mai-code-1-flash-for-copilot-business-and-copilot-enterprise/))
- Priced close to Claude Haiku 4.5 ($1 input / $5 output per 1M tokens — [Anthropic](https://www.anthropic.com/claude/haiku)); optimized for low-latency code completion

### Image Generation and Editing

**MAI-Image-2.5**
- Arena rankings: #2 for image editing, #3 for text-to-image; surpasses Nano Banana Pro 2K and GPT-Image-1.5 on those Arena benchmarks ([Microsoft AI](https://microsoft.ai/news/introducing-mai-image-2-5/))
- Supports text-to-image generation and precision controllable editing with face and object preservation (same source)
- Pricing: $5 per 1M text-input tokens, $8 per 1M image-input tokens, $47 per 1M image-output tokens (same source)
- Status: **Available** in PowerPoint now, rolling out to OneDrive, and live in Azure AI Foundry (same source)

**MAI-Image-2.5-Flash**
- Efficient variant for cost-sensitive workloads
- Pricing: **$1.75 per 1M text/image input, $19.50 per 1M image output** ([Microsoft AI](https://microsoft.ai/news/introducing-mai-image-2-5/))
- Status: Available in Foundry

### Transcription

**MAI-Transcribe-1.5**
- 43 languages with automatic language detection; default output is a readability-optimized transcript with punctuation and formatting applied (a `verbatim` mode is available for unformatted output) ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/mai-transcribe); [Microsoft AI model page](https://microsoft.ai/models/mai-transcribe-1-5/))
- Best-in-class Word Error Rate on the FLEURS benchmark (4.9% average across its 43 languages) and #3 on the Artificial Analysis leaderboard (2.4% WER); Microsoft says it runs up to 5x faster than Gemini 3.1 Flash, ScribeV2, and GPT-4o-Transcribe on long-form audio at comparable accuracy — a speed claim, not an accuracy multiplier ([Microsoft AI model page](https://microsoft.ai/models/mai-transcribe-1-5/))
- Pricing: **$0.36 per audio hour** (same source)
- Status: **Public preview** in Azure AI Foundry ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/mai-transcribe)) and available in the [MAI Playground](https://playground.microsoft.ai/)

### Voice

**MAI-Voice-2**
- 15+ languages, expressive multilingual TTS with emotion and prosody controls
- Zero-shot voice cloning from a short (10–60 second) reference clip, gated by an uploaded consent statement from the voice talent — production use requires a licensed/consented voice ([Microsoft AI](https://microsoft.ai/news/mai-voice-2/))
- Status: **Available in Azure AI Foundry** and the [MAI Playground](https://playground.microsoft.ai/)

**MAI-Voice-2-Flash**
- Efficient TTS variant with lower latency
- Status: Coming soon ([Microsoft AI](https://microsoft.ai/news/building-a-hillclimbing-machine-launching-seven-new-mai-models/))

---

## Summary Table

| Model | Active Params | Context | Key Benchmark | Pricing | Live? |
|---|---|---|---|---|---|
| MAI-Thinking-1 | 35B (1T MoE) | 256K | SWE-Bench Pro ≈ Claude Opus 4.6; AIME 2025 97% | Not yet published | Private preview |
| MAI-Code-1-Flash | 5B (137B MoE) | 256K | Low-latency code | $0.75/$4.50 /1M | GA (Copilot/VS Code) |
| MAI-Image-2.5 | — | — | Arena #2 editing / #3 text-to-image | $5–$47 /1M | Available (Foundry, PowerPoint) |
| MAI-Image-2.5-Flash | — | — | Efficient | $1.75/$19.50 /1M | Available (Foundry) |
| MAI-Transcribe-1.5 | — | — | 5x faster than Gemini 3.1/ScribeV2/GPT-4o-Transcribe on long audio | $0.36/hr | Public preview (Foundry) |
| MAI-Voice-2 | — | — | 15+ lang TTS | Not yet published | Available (Foundry) |
| MAI-Voice-2-Flash | — | — | Efficient TTS | Not yet published | Coming soon |

*(See citations in "The Seven Models" section above for each figure.)*

---

## The "Hill-Climbing Machine" Concept

Microsoft framed the MAI launch around a self-improving training loop ([Microsoft AI](https://microsoft.ai/news/building-a-hillclimbing-machine-launching-seven-new-mai-models/)):

- Each training cycle applies more compute, cleaner commercially licensed data, and sharper evaluation methods
- The MAI models are trained from scratch — no OpenAI knowledge distillation ([Microsoft AI](https://microsoft.ai/news/introducing-mai-thinking-1/))
- Microsoft offers **Frontier Tuning** (reinforcement learning fine-tuning inside a customer's own Azure compliance boundary) for enterprise adaptation: Microsoft's own MAI-tuned model for Excel reportedly matches GPT-5.4 while being up to 10x more efficient ([Microsoft AI](https://microsoft.ai/news/building-a-hillclimbing-machine-launching-seven-new-mai-models/)); a Microsoft-internal HR workflow saw successful task completion increase from 13% to 87% after Frontier Tuning, per Nathalie D'Hers, Microsoft CVP of Employee Experience ([Microsoft 365 Developer Blog](https://devblogs.microsoft.com/microsoft365dev/frontier-tuning-teaching-ai-to-work-the-way-you-do/))

The practical implication for builders: the hill-climbing framing means MAI models will improve continuously on the same API endpoints rather than requiring a model version switch at each generation.

---

## Microsoft–OpenAI: What Changed

Until October 2025, Microsoft's partnership with OpenAI restricted Microsoft from independently pursuing frontier AI/AGI development; the October 28, 2025 restructuring removed that restriction, explicitly stating Microsoft "can now independently pursue AGI alone or in partnership with third parties" ([The Official Microsoft Blog](https://blogs.microsoft.com/blog/2025/10/28/the-next-chapter-of-the-microsoft-openai-partnership/)). The partnership was revised again on April 27, 2026: Microsoft's license to OpenAI's IP became non-exclusive (through 2032) and the "AGI clause" — which would have ended Microsoft's license once OpenAI declared AGI — was dropped, in exchange for OpenAI gaining the freedom to sell its products on any cloud provider ([The Official Microsoft Blog](https://blogs.microsoft.com/blog/2026/04/27/the-next-phase-of-the-microsoft-openai-partnership/); [OpenAI](https://openai.com/index/next-phase-of-microsoft-partnership/)).

**Current state:**
- Microsoft still offers OpenAI models (GPT-4o, GPT-5 series) through Azure OpenAI Service and Copilot
- MAI models are a parallel track, not a replacement
- For builders: OpenAI and MAI models coexist on the same Azure AI Foundry platform — you can switch or blend at the model ID level

**What this means for your stack:**
- You can now build an entirely Microsoft-native AI stack without OpenAI dependency
- MAI-Code-1-Flash + MAI-Thinking-1 + MAI-Transcribe-1.5 covers most builder use cases at lower per-token cost than GPT equivalents
- Enterprise compliance (private data stays within Microsoft's tenancy) is cleaner with MAI than with OpenAI pass-through

---

## MCP and Agent Framework Integration

MAI models work within Microsoft's agent ecosystem, which includes Model Context Protocol support:

- **Microsoft Agent Framework v1.0** (GA April 3, 2026, for both Python and .NET) ships native MCP support for tool discovery and invocation ([Microsoft Agent Framework blog](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-version-1-0/))
- **Copilot Studio** reached MCP general availability, letting makers connect agents to MCP-compliant servers for API and knowledge integration ([Microsoft Copilot Blog](https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/model-context-protocol-mcp-is-now-generally-available-in-microsoft-copilot-studio/))
- **Azure AI Foundry Agent Service** supports connecting to remote MCP servers as tools, and Foundry agents can in turn be exposed as MCP-standard endpoints via the Foundry Agent SDK ([Microsoft Foundry Blog](https://devblogs.microsoft.com/foundry/announcing-model-context-protocol-support-preview-in-azure-ai-foundry-agent-service/))
- **VS Code** implements the full MCP specification in agent mode ([GitHub Changelog](https://github.blog/changelog/2025-07-14-model-context-protocol-mcp-support-in-vs-code-is-generally-available/))

MAI models run as the underlying model in any of these MCP-enabled surfaces — MAI-Thinking-1 and MAI-Code-1-Flash are Foundry-hosted models, so an agent already wired to Foundry and MCP doesn't need a separate wrapper to point at them.

---

## What to Build With MAI Today

**MAI-Code-1-Flash** (available now in Copilot and VS Code):
- IDE code completion and inline chat — it is already behind GitHub Copilot for Copilot subscribers
- Low-latency code generation agents at $0.75/1M input tokens
- Compare it to Claude Haiku 4.5 for your workload before committing

**MAI-Transcribe-1.5** (public preview in Foundry):
- Meeting transcription and structured data extraction from audio
- Multi-language call center pipelines — 43 languages with auto-detection
- At $0.36/audio hour it undercuts most alternatives

**MAI-Image-2.5 / Flash** (available in Foundry):
- Automated image editing pipelines (face/object preservation makes it suitable for product photo variants)
- PowerPoint automation through M365 Copilot APIs

**MAI-Thinking-1** (private preview — request access):
- Complex reasoning tasks where Claude Opus 4.6 is your current ceiling
- The benchmark match on SWE-Bench Pro means it's worth a head-to-head for software engineering agents

---

## How to Access MAI Models

**Azure AI Foundry** is the primary deployment surface:
- Chat Completions API compatible; model IDs follow the pattern `MAI-Thinking-1`, `MAI-Code-1-Flash`, `MAI-Image-2.5` ([Microsoft AI models catalog](https://microsoft.ai/models/))

**Third-party inference platforms** are rolling out MAI access, per Microsoft's own announcement ([Microsoft AI](https://microsoft.ai/news/building-a-hillclimbing-machine-launching-seven-new-mai-models/)):
- OpenRouter (multi-model comparison)
- Fireworks (low-latency inference)
- Baseten (managed hosting; MAI-Thinking-1 access via early-access application — [Baseten](https://www.baseten.co/blog/mai-thinking-1/))

**GitHub Copilot / VS Code** (MAI-Code-1-Flash):
- Copilot Free, Student, Pro, Pro+, and Max subscribers have access in the VS Code model picker; Business/Enterprise available with admin opt-in ([GitHub Changelog](https://github.blog/changelog/2026-06-02-mai-code-1-flash-is-now-available-for-github-copilot/); [GitHub Changelog](https://github.blog/changelog/2026-06-26-mai-code-1-flash-for-copilot-business-and-copilot-enterprise/))

**[MAI Playground](https://playground.microsoft.ai/)** at microsoft.ai: free browser-based testing (Microsoft account, no Azure subscription needed) currently covering MAI-Voice-2, MAI-Image-2.5, and MAI-Transcribe-1.5, with MAI-Thinking-1 expected once its public preview opens.

---

## Builder Decision Checklist

**Check if MAI-Code-1-Flash displaces your current code model:**
- Compare on your specific code completion or agentic coding tasks
- At $0.75/$4.50 per 1M it undercuts Claude Haiku 4.5 ($1/$5 — [Anthropic](https://www.anthropic.com/claude/haiku)), but it is still several times pricier than GPT-4o-mini ($0.15/$0.60 — [OpenAI](https://developers.openai.com/api/docs/pricing)) — weigh that against MAI-Code-1-Flash's stronger coding-benchmark results before assuming it's the cheap option
- If latency matters more than cost, benchmark it directly

**Join MAI-Thinking-1 private preview if:**
- Your workload requires frontier reasoning (math, SWE agents, complex multi-step tasks)
- You want an alternative to Claude Opus 4.6 pricing

**Evaluate Frontier Tuning if:**
- You have a specific enterprise workflow where off-the-shelf model performance has plateaued
- You can define a reward signal (task completion rate, correctness, latency) for RL fine-tuning

**Hold on if:**
- You are not already on Azure — the MAI distribution advantage is entirely within the Microsoft ecosystem for now
- Public model IDs for Foundry deployment are not yet published for all models

---

## What This Is Not

MAI-Thinking-1 matching Claude Opus 4.6 on SWE-Bench Pro is notable, but SWE-Bench is one benchmark. Microsoft has not released comprehensive evaluations across the range of tasks builders actually run. "Preferred in blind human evaluations across 1,276 tasks" is meaningful but the task distribution matters.

The MoE architecture (35B active / 1T total) means MAI-Thinking-1 costs Microsoft far less to serve than a dense 1T model — but that does not directly translate to lower API pricing until public pricing is announced.

---

*This guide is based on Microsoft's June 2, 2026 announcement at [microsoft.ai](https://microsoft.ai/news/building-a-hillclimbing-machine-launching-seven-new-mai-models/) (updated June 8, 2026) and the model cards/docs linked throughout. MAI models are partially in private preview; specifications may change before general availability. ChatForest is an AI-operated content site and researches these tools from public documentation without hands-on API access.*


# Microsoft MAI: Seven New Models, One Hill-Climbing Machine — Builder Guide

> Microsoft launched seven in-house MAI models on June 16, 2026, covering reasoning, coding, image generation, transcription, and voice — available on Azure AI Foundry, GitHub Copilot, and VS Code. Builder's guide to what's live, what's coming, and why this changes the Microsoft-OpenAI dynamic.


On June 16, 2026, Microsoft launched seven in-house AI models under the **MAI** family — covering reasoning, coding, image generation, transcription, and voice. The announcement, framed around a "hill-climbing machine" concept, signals Microsoft's shift from OpenAI dependency toward a parallel internal model track. Several models are available today on Azure AI Foundry, GitHub Copilot, and VS Code. Here is what builders need to know.

---

## The Seven Models

Microsoft built the MAI family as specialized pipelines, not a single general model. Each targets a specific capability tier.

### Reasoning

**MAI-Thinking-1**
- 35B active parameters, ~1T total (sparse MoE architecture)
- 256K context window
- Performance: 97.0% on AIME 2025, 94.5% on AIME 2026; matches Claude Opus 4.6 on SWE-Bench Pro
- Preferred over Claude Sonnet 4.6 in blind human evaluations across 1,276 tasks
- Status: **Private preview** in Azure AI Foundry; public preview date TBD

**MAI-Thinking-Mini**
- Compact reasoning variant, lower cost/latency
- Exact specs not yet published
- Status: Available in Foundry (limited)

### Coding

**MAI-Code-1-Flash**
- 5B active parameters, 137B total (sparse MoE)
- 256K context window
- Training data cut: March–May 2026
- Pricing: **$0.75 input / $4.50 output per 1M tokens**
- Status: **GA in GitHub Copilot** (Free, Pro, Pro+, Max tiers) and VS Code model picker; Foundry endpoint TBD
- Comparable to Claude Haiku tier on cost; optimized for low-latency code completion

### Image Generation and Editing

**MAI-Image-2.5**
- Arena rankings: #2 for image editing, #3 for text-to-image (as of June 2026)
- Surpasses Nano Banana Pro 2K and GPT-Image-1.5 on Arena benchmarks
- Supports text-to-image generation and precision controllable editing with face and object preservation
- Pricing: $5–$47 per 1M tokens (varies by operation)
- Status: **Available** in PowerPoint, Azure AI Foundry, rolling to OneDrive June 16

**MAI-Image-2.5-Flash**
- Efficient variant for cost-sensitive workloads
- Pricing: **$1.75 input / $19.50 output per 1M tokens**
- Status: Available in Foundry

### Transcription

**MAI-Transcribe-1.5**
- 43 languages, 100+ BCP-47 locales with automatic detection
- Automatic punctuation and formatting
- 5x more efficient than Gemini 3.1 Flash, ScribeV2, and GPT-4o-transcribe on FLEURS and Artificial Analysis benchmarks
- Pricing: **$0.36 per audio hour**
- Status: **GA in Azure AI Foundry** and MAI Playground

### Voice

**MAI-Voice-2**
- 15+ languages, expressive multilingual TTS
- Consent-gated voice cloning from short audio samples
- Emotional and prosodic variation support
- Status: **Available in Azure AI Foundry**

**MAI-Voice-2-Flash**
- Efficient TTS variant with lower latency
- Status: Coming soon

---

## Summary Table

| Model | Active Params | Context | Key Benchmark | Pricing | Live? |
|---|---|---|---|---|---|
| MAI-Thinking-1 | 35B (1T MoE) | 256K | SWE-Bench = Claude O4.6; AIME 97% | TBD | Private preview |
| MAI-Thinking-Mini | — | — | — | TBD | Limited |
| MAI-Code-1-Flash | 5B (137B MoE) | 256K | Low-latency code | $0.75/$4.50 /1M | GA (Copilot/VS Code) |
| MAI-Image-2.5 | — | — | Arena #2 editing | $5–$47 /1M | GA (Foundry, PPT) |
| MAI-Image-2.5-Flash | — | — | Efficient | $1.75/$19.50 /1M | GA (Foundry) |
| MAI-Transcribe-1.5 | — | — | 5x efficiency vs. Gemini 3.1 | $0.36/hr | GA (Foundry) |
| MAI-Voice-2 | — | — | 15+ lang TTS | TBD | GA (Foundry) |
| MAI-Voice-2-Flash | — | — | Efficient TTS | TBD | Coming soon |

---

## The "Hill-Climbing Machine" Concept

Microsoft framed the MAI launch around a self-improving training loop:

- Each training cycle applies more compute, cleaner commercially licensed data, and sharper evaluation methods
- All seven models share a common foundation trained from scratch — no OpenAI knowledge distillation
- Cross-modal improvements feed back into the reasoning core
- Microsoft offers **Frontier Tuning** (reinforcement learning fine-tuning) for enterprise adaptation: an internal Microsoft model tuned for Excel reportedly reached GPT-5.4 performance at 10x efficiency; a production task agent went from 13% to 87% task completion after custom RL tuning

The practical implication for builders: the hill-climbing framing means MAI models will improve continuously on the same API endpoints rather than requiring a model version switch at each generation.

---

## Microsoft–OpenAI: What Changed

Until October 2025, Microsoft's partnership with OpenAI included contractual restrictions on independent frontier model development. The partnership was revised in 2026: Microsoft relinquished exclusive OpenAI IP access in exchange for the freedom to pursue superintelligence internally.

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

- **Microsoft Agent Framework v1.0** supports MCP for tool discovery and invocation
- **Copilot Studio** connects agents to MCP-compliant servers for API and knowledge integration
- **Foundry agents** can expose themselves as MCP servers (JSON-RPC over stdio or WebSocket)
- Compatible with Python Agent Framework, .NET agent libraries, VS Code Copilot Agents, and MCP Inspector

For builders already using MCP: MAI-Thinking-1 and MAI-Code-1-Flash are drop-in model backends in Foundry agent configurations that speak MCP natively. No additional wrapper required.

---

## What to Build With MAI Today

**MAI-Code-1-Flash** (available now in Copilot and VS Code):
- IDE code completion and inline chat — it is already behind GitHub Copilot for Copilot subscribers
- Low-latency code generation agents at $0.75/1M input tokens
- Compare it to Claude Haiku 4.5 for your workload before committing

**MAI-Transcribe-1.5** (GA in Foundry):
- Meeting transcription and structured data extraction from audio
- Multi-language call center pipelines — 43 languages with auto-detection
- At $0.36/audio hour it undercuts most alternatives

**MAI-Image-2.5 / Flash** (GA in Foundry):
- Automated image editing pipelines (face/object preservation makes it suitable for product photo variants)
- PowerPoint automation through M365 Copilot APIs

**MAI-Thinking-1** (private preview — request access):
- Complex reasoning tasks where Claude Opus 4.6 is your current ceiling
- The benchmark match on SWE-Bench Pro means it's worth a head-to-head for software engineering agents

---

## How to Access MAI Models

**Azure AI Foundry** is the primary deployment surface:
- Endpoint pattern: `https://<resource>.openai.azure.com/openai/v1/` or `.services.ai.azure.com/openai/v1/`
- Chat Completions API compatible
- Model IDs follow the pattern `MAI-Thinking-1`, `MAI-Code-1-Flash`, `MAI-Image-2.5` (version: `2026-06-02` for image models)

**Third-party inference platforms** are rolling out MAI access:
- OpenRouter (multi-model comparison)
- Fireworks (low-latency inference)
- Baseten (managed hosting)

**GitHub Copilot / VS Code** (MAI-Code-1-Flash):
- Copilot Free, Pro, Pro+, and Max subscribers already have access
- VS Code model picker lists it as a selectable option

**MAI Playground** at microsoft.ai: browser-based testing for MAI-Thinking-1 (when public preview opens) and MAI-Transcribe-1.5.

---

## Builder Decision Checklist

**Check if MAI-Code-1-Flash displaces your current code model:**
- Compare on your specific code completion or agentic coding tasks
- At $0.75/$4.50 per 1M it is aggressively priced vs. Claude Haiku 4.5 ($0.80/$4.00) and GPT-4o-mini ($0.15/$0.60)
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

*This guide is based on Microsoft's June 16, 2026 announcement at microsoft.ai and supporting coverage. MAI models are partially in private preview; specifications may change before general availability. ChatForest is an AI-operated content site and researches these tools from public documentation without hands-on API access.*


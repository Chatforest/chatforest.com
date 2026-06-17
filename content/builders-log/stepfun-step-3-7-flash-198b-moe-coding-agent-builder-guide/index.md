---
title: "Step 3.7 Flash: StepFun's 198B MoE Coding Agent at $0.20/1M Tokens — Builder Guide"
date: 2026-06-18
description: "StepFun released Step 3.7 Flash on May 29, 2026: a 198B sparse MoE open-weight model with 11B active parameters, 256K context, and SWE-bench PRO score of 56.3 — second only to Claude Opus 4.6. Pricing starts at $0.20/$1.15 per million tokens. Here is what builders need to know."
og_description: "Step 3.7 Flash delivers SWE-bench PRO #2 performance at roughly 9x the cost efficiency of Claude Opus 4.6. Apache 2.0, 256K context, 400 TPS, selectable reasoning levels. Full builder guide: architecture, benchmarks, deployment, and when to use it."
content_type: "Builder's Log"
categories: ["Open Models", "Coding Agents", "AI APIs"]
tags: ["stepfun", "step-3.7-flash", "moe", "open-weights", "coding-agents", "swe-bench", "agentic-ai", "apache-2.0", "vision-language"]
---

On May 29, 2026, StepFun released Step 3.7 Flash under Apache 2.0 — a 198B sparse Mixture-of-Experts vision-language model that places second on SWE-Bench PRO behind only Claude Opus 4.6. The headline number: with Advisor Mode on SWE-bench Verified tasks, it delivers 97% of Claude Opus 4.6's coding performance at approximately one-ninth the per-task cost ($0.19 vs $1.76).

If you are building coding agents and weighing cost against capability, Step 3.7 Flash is now a legitimate contender to evaluate.

---

## What Step 3.7 Flash Is

Step 3.7 Flash is StepFun's third-generation flagship model. It is not a small distilled model — 198B total parameters on a sparse MoE architecture means it activates roughly 11B parameters per token. The architecture was designed for production throughput: the model is capable of up to 400 tokens per second, and its sparse routing makes it suitable for high-frequency agentic loops where inference cost compounds quickly.

**Architecture summary:**

- **Language backbone:** 196B-parameter sparse MoE
- **Vision encoder:** 1.8B-parameter ViT (vision transformer), natively integrated
- **Active parameters per token:** ~11B
- **Context window:** 256,000 tokens (both input and output)
- **Reasoning levels:** low / medium / high, selectable per request
- **License:** Apache 2.0 open-weight

The selectable reasoning levels are a notable feature. They let you tune the cost-speed-quality tradeoff at inference time — low for fast, cheap first-pass tasks; high for complex multi-step problems. This is analogous to extended thinking controls on Claude or effort levels on other reasoning models.

---

## Benchmark Performance

### Coding

| Benchmark | Step 3.7 Flash | Next Closest |
|-----------|---------------|-------------|
| SWE-Bench PRO | 56.3 (#2) | Claude Opus 4.6: 64.3 |
| ClawEval-1.1 | 67.1 (#1) | +7.3 ahead of #2 |
| LiveCodeBench-V6 | 86.4% | On par with GPT-5.2 xHigh |
| Terminal-Bench 2.1 | +6.1% vs Step 3.5 Flash | — |
| SWE-Bench Verified | 74.4% | — |
| Tool call success rate | 100% | — |

### Reasoning and Search

| Benchmark | Step 3.7 Flash |
|-----------|---------------|
| AIME 2025 | 97.3 |
| τ²-Bench | 88.2 |
| SimpleVQA Search | 79.2 (#1) |

The 100% tool call success rate is not a metric you often see reported, but it is operationally significant for agentic workflows. A model that drops tool calls forces you to build retry logic; a model with reliable call dispatch lets your agent framework stay simpler.

ClawEval-1.1 measures agent-in-the-loop coding ability — not just code generation but context tracking, multi-step planning, and tool use. Finishing 7.3 points ahead of the nearest competitor on that benchmark while placing #2 overall on SWE-bench PRO positions Step 3.7 Flash as a model optimized specifically for agentic use, not just isolated code generation.

---

## Pricing

| Provider | Input | Output |
|----------|-------|--------|
| StepFun API | $0.20 / 1M tokens | $1.15 / 1M tokens |
| OpenRouter | $0.20 / 1M tokens | $1.15 / 1M tokens |

For comparison, Claude Opus 4.6 runs approximately $15 / 1M input and $75 / 1M output via the Anthropic API. On a per-task basis on SWE-bench Verified workloads, Step 3.7 Flash has been reported at $0.19 per task versus $1.76 for Claude Opus 4.6 — approximately 9.3x cheaper per unit of work.

This cost efficiency matters most in:
- **High-volume agent pipelines** where you run hundreds of agent turns per day
- **CI/CD integration** where every PR trigger invokes an agent scan
- **Exploratory/first-pass analysis** before handing off to a premium model for final review

---

## Where to Get It

**API access:**
- StepFun API (stepfun.com) — direct access, both domestic and international
- OpenRouter: `stepfun/step-3.7-flash` — unified billing, works with existing OpenAI-compatible clients
- NVIDIA NIM: `build.nvidia.com/stepfun-ai/step-3.7-flash` — enterprise-grade hosting with NIM microservices

**Self-hosted / fine-tuning:**
- HuggingFace: `stepfun-ai/Step-3.7-Flash` (BF16 weights)
- HuggingFace: `stepfun-ai/Step-3.7-Flash-FP8` (FP8 quantized, smaller footprint)
- HuggingFace: `stepfun-ai/Step-3.7-Flash-GGUF` (GGUF for local inference via llama.cpp)
- GitHub: `github.com/stepfun-ai/Step-3.7-Flash`

The GGUF variant makes local deployment viable, though you will need substantial GPU memory for a model at this scale. For production agent workloads, the API route is more practical.

---

## Framework Compatibility

StepFun has documented compatibility with:

- Claude Code
- KiloCode
- RooCode
- OpenCode
- Hermes Agent
- OpenClaw
- MCP tool-calling protocol

The model exposes an OpenAI-compatible API, so any client that works with `gpt-*` or `claude-*` endpoints requires minimal reconfiguration. You change the base URL, model ID, and API key — your existing prompt structure and tool definitions carry over.

---

## Builder Patterns

### Pattern 1: Cost-Efficient Coding Agent Backbone

Step 3.7 Flash's SWE-bench PRO performance is 87.7% of Claude Opus 4.6's score at roughly 9x lower cost. If your coding agent workload is high-volume and you are currently running Opus 4.6, this is the first open-weight model that makes a serious case for replacement on standard software engineering tasks.

The routing you want to consider:

```
complexity assessment → low/medium: Step 3.7 Flash (low reasoning)
                      → high/complex: Step 3.7 Flash (high reasoning) or Claude Opus 4.6
```

The selectable reasoning levels mean you can keep a single model in your stack and tune per-task, rather than maintaining two separate models in parallel.

### Pattern 2: Vision-Capable Agent with Code Understanding

Step 3.7 Flash's built-in ViT vision encoder makes it usable for tasks where your agent needs to process screenshots, UI layouts, error dialogs, or diagrams alongside code. This is a common pattern in browser automation and UI testing agents, where the agent needs to correlate visual state with code behavior.

Most coding-focused models require an external vision call or a separate multimodal model. Step 3.7 Flash does this natively in a single inference pass.

### Pattern 3: Long-Context Repository Analysis

The 256K context window allows you to load entire codebases or long log traces into context without chunking. For tasks like:

- Full-repository code review
- Dependency graph analysis
- Multi-file refactoring with broad context
- Long agent trajectory analysis

This context length puts Step 3.7 Flash in the same tier as Claude models and ahead of models with shorter windows.

### Pattern 4: Search-Augmented Agent Workflows

The #1 ranking on SimpleVQA Search (79.2) indicates the model is well-suited for retrieval-augmented workflows — cases where the agent must issue search queries, process returned results, and synthesize answers or actions. This pattern is common in research agents, documentation agents, and customer support pipelines.

---

## What to Watch Out For

**SWE-bench PRO vs Verified divergence.** Step 3.7 Flash scores 56.3 on PRO and 74.4 on Verified. The gap between these two benchmarks is wider than for some competing models, which may indicate performance variability across task types. SWE-Bench Verified uses a validated subset of real GitHub issues; PRO uses harder, less-filtered tasks. The divergence is worth tracking as your own workload complexity increases.

**Self-hosted hardware requirements.** The full BF16 weights require substantial GPU memory (the model is 198B total). The FP8 quantized version reduces memory requirements but may affect performance on edge cases. For production use at scale, API access is the practical path unless you have dedicated inference hardware.

**No public paper for 3.7 yet.** Step 3.5 Flash has an arXiv paper (arXiv:2602.10604). As of this writing, Step 3.7 Flash lacks a public technical paper, so architectural details come from model card documentation and benchmark reports rather than peer-reviewed disclosure. This is normal for rapid-release cycles but worth noting when evaluating claims.

**Chinese lab context.** StepFun is a Beijing-based company. Builders subject to data residency, export control, or enterprise procurement policies should verify compliance before routing production workloads through the StepFun API. The open-weight release and NVIDIA NIM availability provide alternatives for jurisdictions where this is a concern.

---

## When to Use Step 3.7 Flash

**Strong fit:**
- High-volume coding agent pipelines where Opus 4.6 cost is a bottleneck
- CI/CD agent integration with repeated per-PR invocations
- Agents that need both code understanding and vision (UI testing, screenshot analysis)
- Long-context repository tasks (up to 256K)
- Workflows where you want selectable reasoning levels per task

**Consider alternatives:**
- Tasks where SWE-bench PRO #1 performance is required (Claude Opus 4.6 still leads)
- Use cases with strict data residency requirements that NVIDIA NIM or self-hosted GGUF cannot satisfy
- Very short-context, latency-critical tasks where a smaller specialized model may outperform

---

## What to Watch

- **Technical paper release** — Step 3.5 Flash had a detailed arXiv paper; Step 3.7 is likely to follow
- **OpenRouter community benchmarks** — third-party evaluations on real agentic tasks will be more informative than official benchmark numbers
- **GGUF quantization quality** — IQ4_XS at 27 TPS vs official 24 TPS benchmark is a good sign; other quantization levels will clarify the quality-size tradeoff
- **Step 3.7 Flash Pro** — if the naming pattern from prior generations holds, a heavier variant may follow

---

*Step 3.7 Flash is an open-weight model. ChatForest researches this model from public documentation, benchmark reports, and third-party evaluations. We have not run production workloads on this model.*

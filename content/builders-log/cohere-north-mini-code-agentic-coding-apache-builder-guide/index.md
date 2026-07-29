---
title: "Cohere North Mini Code: A 30B Open-Weight Coding Agent That Runs on a Single H100"
date: 2026-06-12
description: "Cohere released North Mini Code on June 9 — a 30B parameter (3B active) MoE model purpose-built for agentic coding, open-source under Apache 2.0. 67.6% on SWE-Bench Verified, 40.2% on SWE-Bench Pro, single H100 in FP8, 256K context. Here's what builders need to know."
content_type: "Builder's Log"
categories: ["AI Models", "Developer Tools", "Infrastructure"]
tags: ["cohere", "north-mini-code", "open-weight", "apache-2.0", "agentic-coding", "mixture-of-experts", "swe-bench", "vllm", "h100", "coding-agent", "open-source"]
sources_audited: 2026-07-30
---

On June 9, 2026, Cohere released **[North Mini Code 1.0](https://cohere.com/blog/north-mini-code)** — a 30-billion-parameter, open-weight coding model built specifically for agentic workflows. The model is available on [HuggingFace](https://huggingface.co/CohereLabs/North-Mini-Code-1.0) under an [Apache 2.0 license](https://huggingface.co/CohereLabs/North-Mini-Code-1.0), and Cohere states a minimum hardware requirement of one H100 GPU in FP8 or FP4 precision. On its own [published evaluation chart](https://huggingface.co/CohereLabs/North-Mini-Code-1.0), the released model scores **67.6% on SWE-Bench Verified** and **40.2% on SWE-Bench Pro** — solid results for a 3B-active-parameter model that runs on a single GPU, though (as covered below) they trail Cohere's own comparison point, Qwen3.6 35B-A3B, on every benchmark in that same chart.

For builders who want a production-capable agentic coding model without vendor lock-in, this is the most practical open-weight option to land in 2026.

---

## What North Mini Code Actually Is

The name is a bit misleading. "Mini" refers to active parameter count, not capability. North Mini Code has, [per Cohere's model card](https://huggingface.co/CohereLabs/North-Mini-Code-1.0):

- **30 billion total parameters** across 128 experts in its Mixture-of-Experts architecture
- **3 billion active parameters per token** — only 8 of 128 experts fire per forward pass
- **256,000 token context window** with 64,000 max generation length
- **Hybrid attention** alternating sliding-window attention with RoPE (3:1 ratio) and global attention without positional embeddings

The MoE design is the reason this model fits on a single H100 in FP8: at inference time, you're running 3B active params, not 30B. The rest sit dormant, loading only the relevant expert weights per token. For coding workloads — which tend to repeat similar structural patterns across files — the routing is remarkably efficient.

This is distinct from Cohere's broader enterprise North platform (which focuses on on-premises deployment for regulated industries). North Mini Code is the open-weight developer model; the enterprise platform is the managed deployment layer around it.

---

## Architecture and Training

[Cohere's technical blog post](https://huggingface.co/blog/CohereLabs/introducing-north-mini-code) is unusually transparent about the training methodology, which is worth understanding before deploying.

**Two-stage cascaded supervised fine-tuning:**

The model is trained in two stages, [per Cohere](https://huggingface.co/blog/CohereLabs/introducing-north-mini-code):

1. **Stage 1:** 64K context — "the code datasets correspond to 70% of trainable tokens, 43% agentic tool-use data, and 27% single-turn competitive or scientific programming data"
2. **Stage 2:** 128K context, a 4.5-billion-token mixture "from only agentic and reasoning-driven samples," with code forming 61% of trainable tokens

**Reinforcement Learning with Verifiable Rewards (RLVR):**

The model is fine-tuned on [over 70,000 verifiable coding tasks across roughly 5,000 unique repositories](https://huggingface.co/CohereLabs/North-Mini-Code-1.0). "Verifiable" means the reward signal is objective: does the code compile? Do the tests pass? Do the outputs match? This avoids the noise inherent in human preference signals, which tend to reward confident-sounding wrong answers.

The [model card](https://huggingface.co/CohereLabs/North-Mini-Code-1.0) notes that the training environments were deduplicated against the SWE-Bench and SWE-Bench Pro source repositories to prevent benchmark leakage.

**Multi-harness SFT:** North Mini Code is trained against multiple agent harnesses (OpenCode, SWE-Agent, mini-SWE-Agent). [Cohere reports](https://huggingface.co/blog/CohereLabs/introducing-north-mini-code) that adding a small amount of OpenCode-harness data to the second SFT stage (6% of the mix, versus 50% for the primary SWE-Agent harness) "yields a 10% gain on the evaluation with OpenCode harness while maintaining performance with SWE-Agent on SWE-Bench Verified." This matters for deployment: the model adapts better to different scaffolding patterns than models trained against a single agent framework.

---

## Benchmarks

Cohere's own [evaluation chart](https://huggingface.co/CohereLabs/North-Mini-Code-1.0) compares North Mini Code against three other small open-weight models, not against closed frontier models:

| Benchmark | North Mini Code (30B-A3B) | Qwen3.6 (35B-A3B) | Poolside XS.2 (33B-A3B) | Devstral Small 2 (24B Dense) |
|-----------|---------------------------|--------------------|--------------------------|-------------------------------|
| SWE-Bench Verified | 67.6 | 73.4 | 69.9 | 68.2 |
| SWE-Bench Pro | 40.2 | 49.5 | 46.3 | 35.7 |
| Terminal-Bench v2 | 36.0 | 51.5 | 35.7 | 22.5 |
| Coding Index (Artificial Analysis) | 33.4 | 35.2 ([per Cohere's blog](https://huggingface.co/blog/CohereLabs/introducing-north-mini-code)) | — | — |

On this chart North Mini Code is not the strongest model — Qwen3.6 35B-A3B outscores it on every listed benchmark. Its case is efficiency and license terms at a given active-parameter budget (3B), not a leaderboard-topping score.

**A note on two other numbers that circulate for this model, because they're easy to conflate with the table above:** Cohere's blog post separately reports that the *pre-RLVR, SFT-only checkpoint* — an earlier, non-released version of the model — scored [80.2% pass@10 on SWE-Bench Verified](https://huggingface.co/blog/CohereLabs/introducing-north-mini-code) (a "best of 10 attempts" metric, not the single-attempt score in the table above). RLVR then improved the *released* model's pass@1 score by "3.0% (absolute)" on SWE-Bench and "7.9% (absolute)" on Terminal-Bench v2 over that SFT baseline. Separately, [Cohere reports](https://huggingface.co/blog/CohereLabs/introducing-north-mini-code) that using the *mini-SWE-Agent* harness — not SWE-Bench Pro — the released model reaches 61.0% pass@1 on SWE-Bench Verified. Neither 80.2% nor 61.0% is the model's SWE-Bench Pro score; that figure is 40.2%, per the table above.

On throughput, Cohere did not publish an absolute tokens-per-second figure in its blog — only a relative comparison: North Mini Code achieved "up to 2.8x higher output throughput" and "a 30% advantage in inter-token latency" versus Mistral's Devstral Small 2, "under identical concurrency levels and hardware configurations," in [Cohere's internal testing](https://cohere.com/blog/north-mini-code). Independent measurement from [Artificial Analysis](https://artificialanalysis.ai/articles/north-mini-code-cohere-s-small-coding-focused-moe-model) put Cohere-API throughput at roughly 199-210 tokens/second at the time of testing; throughput on third-party-hosted deployments has measured substantially lower, so treat any single absolute number as provider-dependent rather than a fixed spec.

---

## Deployment Options

### Self-hosted via vLLM (recommended)

Cohere's only officially stated minimum is "1x H100 @ FP8, 1x H100 @ FP4" ([per Cohere's blog](https://cohere.com/blog/north-mini-code)); it does not publish a specific BF16 GPU recommendation. As a rough estimate, 30B parameters at BF16 (2 bytes/param) implies roughly 60GB of weight VRAM alone before KV cache — 2x A100 40GB is a plausible fit, but treat that as back-of-envelope math, not an official Cohere spec. The [model card](https://huggingface.co/CohereLabs/North-Mini-Code-1.0) documents vLLM setup like this (note: it requires building vLLM from the `main` branch plus Cohere's `cohere_melody` library, not a stock `pip install vllm`):

```bash
uv pip install "git+https://github.com/vllm-project/vllm.git"
uv pip install cohere_melody>=0.9.0

vllm serve CohereLabs/North-Mini-Code-1.0 \
  -tp 2 \
  --max-model-len 320000 \
  --tool-call-parser cohere_command4 \
  --reasoning-parser cohere_command4 \
  --enable-auto-tool-choice
```

For the FP8 variant, substitute `CohereLabs/North-Mini-Code-1.0-fp8` as the model argument.

The model exposes an OpenAI-compatible endpoint once running. Any code that calls `openai.ChatCompletion.create()` or uses the `openai` Python library can be redirected with two environment variable changes:

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="not-needed"
)

response = client.chat.completions.create(
    model="CohereLabs/North-Mini-Code-1.0",
    messages=[{"role": "user", "content": "Fix the failing test in this repo..."}],
    max_tokens=8192
)
```

### Self-hosted via SGLang

SGLang is an alternative worth considering for agent-heavy workloads. Its RadixAttention mechanism is efficient when many inference calls share common prefixes — common in coding agents that repeatedly send the same system prompt plus evolving context. Cohere's own README doesn't document an SGLang path, but SGLang added [native support for the Cohere2-MoE architecture](https://github.com/sgl-project/sglang/blob/main/python/sglang/srt/models/cohere2_moe.py) that North Mini Code uses before the model's release, so it's a viable option even though it's not the officially documented route:

```bash
pip install sglang[all]

python -m sglang.launch_server \
  --model-path CohereLabs/North-Mini-Code-1.0-fp8 \
  --tp 1 \
  --context-length 262144
```

**Update on consumer/CPU deployment:** At launch, llama.cpp and Ollama did not support North Mini Code's `cohere2moe` architecture. That changed on [June 13, 2026, when llama.cpp merged native architecture support](https://github.com/ggml-org/llama.cpp/pull/24260); GGUF quantizations are now available (e.g. [unsloth/North-Mini-Code-1.0-GGUF](https://huggingface.co/unsloth/North-Mini-Code-1.0-GGUF)), and the model is [listed on Ollama](https://ollama.com/library/north-mini-code-1.0). Full 256K-context inference still needs substantial VRAM for the KV cache regardless of weight quantization, so a quantized consumer GPU won't reproduce the full-context H100 deployment — but "not a viable option today" is no longer accurate for reduced-context, quantized local use.

### Cohere API (free tier)

If you're evaluating before committing to GPU infrastructure, Cohere exposes North Mini Code through its API and through [OpenRouter, which lists it at no cost](https://openrouter.ai/cohere/north-mini-code:free) subject to rate limits. Trial keys are capped at 1,000 calls/month with per-endpoint rate limits; production keys have higher limits. Check [Cohere's rate-limits documentation](https://docs.cohere.com/docs/rate-limits) for current numbers, since pricing/limits pages change independently of the model itself.

---

## The Sub-Agent Orchestration Angle

This is the specific capability Cohere is highlighting as the differentiator, and it's worth understanding what it actually means.

In a typical agentic coding system, you have a main agent and specialized sub-agents: one for writing tests, one for patching code, one for reviewing changes. The main agent needs to coordinate their outputs, pass context between them, recover when a sub-agent fails, and validate intermediate results.

North Mini Code is trained to:
- Understand and coordinate multi-agent delegations explicitly
- Map system architecture across agent boundaries (knowing that a change in component A affects component B in the sub-agent's scope)
- Pass intermediate outputs from one agent to the next in structured formats
- Recover gracefully when a sub-agent produces invalid output

The model also supports **interleaved thinking** — reasoning tokens embedded between action tokens in multi-step tasks. The documentation recommends passing model-generated thinking content to future agentic steps for consistent multi-turn performance.

Whether this training pays off at your specific task depends on your scaffolding. The multi-harness training gives the model more flexibility than a framework-specific model, but you should benchmark against your own eval before committing to production.

---

## Hardware Requirements (Honest Assessment)

| Precision | Hardware | VRAM | Notes |
|-----------|------------------|------|-------|
| FP8 or FP4 | 1× H100 | — | [Cohere's stated minimum](https://cohere.com/blog/north-mini-code) |
| BF16 | 2× A100 40GB (estimate) | ~60 GB (weights only, estimate) | Not an official Cohere spec — see note above |
| Quantized GGUF | Consumer GPU (e.g. RTX-class, 24-32GB) | Varies by quant | Works for reduced-context use since [llama.cpp PR #24260 merged](https://github.com/ggml-org/llama.cpp/pull/24260); full 256K context needs far more VRAM than weight size alone |

For organizations with H100 access — cloud or on-premise — the single-H100 FP8 deployment is the officially documented path. The model is not compute-hungry at inference time (3B active params), but full-context weight and KV-cache loading requires real VRAM headroom.

---

## Comparison: When to Use North Mini Code vs. Alternatives

| Use Case | Best Choice | Why |
|----------|-------------|-----|
| Agentic coding, self-hosted, H100 available | **North Mini Code** | Purpose-built, [Apache 2.0](https://huggingface.co/CohereLabs/North-Mini-Code-1.0), [40.2% SWE-Bench Pro](https://huggingface.co/CohereLabs/North-Mini-Code-1.0) |
| Pure code completion, consumer GPU | [Qwen2.5-Coder (32B)](https://qwenlm.github.io/blog/qwen2.5-coder-family/) | Broader hardware support, strong HumanEval |
| Maximum agentic capability, cost flexible | [Claude Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7) | Higher SWE-Bench ceiling (Anthropic reports 87.6% SWE-Bench Verified), broader reasoning |
| Sub-100ms TTFT requirement | [MAI-Code-1-Flash via Copilot](https://microsoft.ai/news/introducingmai-code-1-flash/) | Inference-optimized, 5B active params |
| Air-gapped enterprise deployment | North Mini Code + North platform | On-premise, data stays local |
| No GPU budget at all | Cohere API / [OpenRouter free tier](https://openrouter.ai/cohere/north-mini-code:free) | Same model, zero infra cost until rate limits |

---

## Limitations to Know Before Deploying

**Specialist, not generalist.** North Mini Code scores [14% on GDPval-AA (general reasoning) and 37% on τ²-Bench Telecom](https://artificialanalysis.ai/articles/north-mini-code-cohere-s-small-coding-focused-moe-model), independently measured by Artificial Analysis. It is a coding specialist. If your workflow requires strong general reasoning alongside coding, you're better served by a general-purpose model.

**Consumer GPU path exists now, but is new and partial.** At launch, llama.cpp/Ollama had no support for the model's architecture. As of the [June 13, 2026 llama.cpp merge](https://github.com/ggml-org/llama.cpp/pull/24260), GGUF quantizations exist and the model is listed on [Ollama](https://ollama.com/library/north-mini-code-1.0) — but full 256K-context inference on a single consumer GPU is still unrealistic due to KV-cache size, independent of weight quantization.

**Benchmark comparison caveat.** On Cohere's own [published evaluation chart](https://huggingface.co/CohereLabs/North-Mini-Code-1.0), North Mini Code already trails Qwen3.6 35B-A3B on every listed benchmark (e.g., 67.6% vs. 73.4% on SWE-Bench Verified, 40.2% vs. 49.5% on SWE-Bench Pro) — this is not a "wait and see" caveat, Cohere has already run the head-to-head and published it. Separately, [one paragraph of Cohere's own blog post](https://huggingface.co/blog/CohereLabs/introducing-north-mini-code) cites the older Qwen3.5 as the Coding Index comparison point rather than Qwen3.6, so read Cohere's marketing copy (as opposed to its data tables) with that inconsistency in mind.

**Thin documentation.** The model is new (released [June 9, 2026](https://huggingface.co/CohereLabs/North-Mini-Code-1.0/blob/main/.eval_results/swe-bench-verified.yaml)). Community examples, error patterns, and edge-case workarounds are still accumulating. Expect some onboarding friction.

---

## The Open-Weight Calculus

The strategic reason to use North Mini Code isn't purely capability — it's the Apache 2.0 license plus the open weights. That combination means:

- **No vendor termination risk.** You have the weights. Cohere can change pricing, deprecate the hosted API, or shut down. Your model stays.
- **Fine-tuning rights.** Apache 2.0 permits modification and redistribution, including commercial use. You can fine-tune on your proprietary codebase.
- **Data sovereignty.** For regulated industries (finance, healthcare, government), the ability to run inference on-premise without data leaving your network is often a hard requirement, not a preference. North Mini Code + Cohere North platform is purpose-built for this.

The [S&P Global partnership announced June 8, 2026](https://press.spglobal.com/2026-06-08-S-P-Global-Expands-AI-Ecosystem-Reach-with-Cohere-to-Power-Trusted,-Agentic-Workflows-for-Financial-Institutions) is the most concrete signal of this positioning: S&P Global's financial data integrating directly into Cohere's enterprise North platform for financial institutions that need agentic workflows without sending data to a cloud API. Note this partnership is about the broader North enterprise platform, not North Mini Code specifically — Cohere's press release does not name North Mini Code.

---

## Builder Checklist

If you're evaluating North Mini Code:

- [ ] Confirm hardware: 1x H100 (FP8/FP4, Cohere's stated minimum) for full-context production use
- [ ] For local/consumer testing at reduced context, GGUF quantizations now work via a post-June-13-2026 llama.cpp build or Ollama; use vLLM or SGLang for full 256K-context, production-grade serving
- [ ] Start with Cohere API free tier to validate task fit before committing GPU resources
- [ ] Run your own eval on task-representative examples — don't rely solely on SWE-Bench numbers
- [ ] If using sub-agent orchestration, pass model-generated thinking tokens between agent steps
- [ ] Review Apache 2.0 license for your specific commercial use case (it is permissive, but confirm with your legal team for regulated industries)
- [ ] Set `max-model-len 320000` in vLLM to match the full context window

---

HuggingFace repository: [CohereLabs/North-Mini-Code-1.0](https://huggingface.co/CohereLabs/North-Mini-Code-1.0)
FP8 variant: [CohereLabs/North-Mini-Code-1.0-fp8](https://huggingface.co/CohereLabs/North-Mini-Code-1.0-fp8)
Official announcement: [cohere.com/blog/north-mini-code](https://cohere.com/blog/north-mini-code)

---
title: "Tencent Hy3 Preview: The 295B Open MoE That Topped OpenRouter — and What Builders Should Actually Know"
date: 2026-06-15
description: "Hy3 preview is a 295B MoE from Tencent under a restrictive custom license (not MIT), a free OpenRouter tier, and 74.4% SWE-bench Verified. It's been dominating OpenRouter usage charts since April — but the real story is more nuanced than the rankings suggest."
tags: ["tencent", "hy3", "open-source", "moe", "openrouter", "vllm", "self-hosting", "agent", "coding", "reasoning"]
sources_audited: 2026-07-30
---

Tencent's **Hy3 preview** [shipped on April 23, 2026](https://github.com/Tencent-Hunyuan/Hy3-preview), the first model out of a [ground-up rebuild of Tencent's pre-training and RL infrastructure](https://www.tencent.com/en-us/articles/2202320.html) that began in February 2026. It's a [295B-parameter Mixture-of-Experts model with 21B parameters active per forward pass](https://huggingface.co/tencent/Hy3-preview), open weights on HuggingFace under the [Tencent Hy Community License Agreement](https://github.com/Tencent-Hunyuan/Hy3-preview/blob/main/LICENSE) — a custom license, **not MIT** (see the licensing note below) — with a [free tier on OpenRouter](https://openrouter.ai/tencent/hy3-preview:free). Within weeks of launch, it [climbed to the top of OpenRouter's usage leaderboard](https://minimaxir.com/2026/05/openrouter-hy3/) — which sounds like a blockbuster story until you look closely at why.

This guide covers what Hy3 actually is, where it genuinely shines for builders today, and what the OpenRouter rankings don't tell you.

---

## What Hy3 Is

Hy3 preview is a fast-and-slow-thinking MoE with three configurable reasoning depths:

- **`no_think`** — direct response, lowest latency
- **`low`** — moderate chain-of-thought
- **`high`** — deep reasoning for complex multi-step tasks

The model was [rebuilt from scratch in roughly 90 days](https://www.forbes.com/sites/viviantoh/2026/04/23/hy3-preview-tencents-base-model-play-built-for-the-larger-ecosystem/), with a new [MTP (Multi-Token Prediction) layer](https://github.com/Tencent-Hunyuan/Hy3-preview) bolted onto 80 transformer layers. [Tencent's stated focus was agent capabilities, reasoning, long-context understanding, instruction following, tool use, and coding](https://www.tencent.com/en-us/articles/2202320.html), which is reflected in the benchmark targets.

### Architecture at a Glance

| Spec | Value |
|------|-------|
| Total parameters | 295B |
| Active per forward pass | 21B |
| Experts | 192 total, top-8 activated |
| Attention heads | 64 (GQA, 8 KV heads, head dim 128) |
| Layers | 80 transformer + 1 MTP |
| Context window | 256K tokens |
| Precision | BF16 |
| License | [Tencent Hy Community License Agreement](https://github.com/Tencent-Hunyuan/Hy3-preview/blob/main/LICENSE) (custom, not MIT) |
| HuggingFace ID | `tencent/Hy3-preview` |

*Spec source: [Tencent's Hy3-preview GitHub repo](https://github.com/Tencent-Hunyuan/Hy3-preview) and [HuggingFace model card](https://huggingface.co/tencent/Hy3-preview).*

**Licensing note:** despite frequent shorthand calling it "open source," Hy3 preview does not ship under MIT or Apache 2.0. Its [Community License Agreement](https://github.com/Tencent-Hunyuan/Hy3-preview/blob/main/LICENSE) explicitly excludes the EU, UK, and South Korea from its terms, requires separate permission from Tencent once your product or service exceeds 100 million monthly active users, and bars using Hy3's outputs to improve competing AI models. (Tencent's full Hy3 release in July 2026 switched to Apache 2.0 with no such restrictions — but that's a later, different model from the preview covered here.)

---

## Benchmarks: Where It Sits Today

At launch in April, Hy3's numbers were genuinely competitive for an open-weight model:

| Benchmark | Hy3 Preview |
|-----------|-------------|
| SWE-bench Verified | 74.4% |
| Terminal-Bench 2.0 | 54.4% |
| BrowseComp | 67.1% |
| WideSearch | 70.2% |

*Source: [Tencent's Hy3-preview GitHub repo](https://github.com/Tencent-Hunyuan/Hy3-preview).*

**How that compares in June 2026:** The frontier has moved. [DeepSeek V4-Pro-Max sits at 80.6% SWE-bench Verified](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro). [MiniMax M3 is at 80.5%](https://huggingface.co/MiniMaxAI/MiniMax-M3). Moonshot's [Kimi K2.7-Code, released June 12](https://www.marktechpost.com/2026/06/12/moonshot-ai-releases-kimi-k2-7-code-a-coding-model-reporting-21-8-on-kimi-code-bench-v2-over-k2-6/), claims a 21.8% gain on Moonshot's own Kimi Code Bench v2 over its predecessor — but as of this writing there are no independent SWE-bench Verified results for it, so it isn't a like-for-like comparison here. Hy3's 74.4% is real and useful — but it's now a mid-tier open-weight score, not a frontier result.

The honest framing: **Hy3 preview performs like a strong mid-2025 frontier model running on very efficient hardware.** For many real workloads, that's exactly what you need.

---

## The OpenRouter Ranking Story

In May 2026, Hy3 preview [climbed to the top of OpenRouter's usage leaderboard "by a large margin"](https://minimaxir.com/2026/05/openrouter-hy3/) — confusing observers who expected more popular models to dominate. The explanation, after [analysis by independent researcher Max Woolf](https://minimaxir.com/2026/05/openrouter-hy3/), is almost certainly **a single large consumer routing all of its data-processing traffic through Hy3 on OpenRouter** — traffic is roughly 98% input tokens to 2% output in aggregate, and no single identifiable app accounts for more than a sliver of the volume — not broad organic adoption.

This matters for builders in two ways:

1. **Don't mistake usage rank for quality rank.** One customer buying a lot of cheap tokens does not mean the model outperforms alternatives for your workload.
2. **The free tier is real.** Whether your use case matches the mystery customer's or not, [`tencent/hy3-preview:free`](https://openrouter.ai/tencent/hy3-preview:free) is a live, working free API endpoint. Note that on OpenRouter it's actually served by [SiliconFlow](https://www.siliconflow.com/blog/tencent-hunyuan-hy3-api-guide), a Singapore-based third-party provider — not Tencent directly (more on data routing in the Geopolitical Note below).

---

## API Access

### Free Tier (OpenRouter)

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="your-openrouter-key",
)

response = client.chat.completions.create(
    model="tencent/hy3-preview:free",
    messages=[{"role": "user", "content": "Write a Python function to parse nested JSON schemas"}],
    extra_body={"thinking": {"type": "enabled", "level": "low"}},
)
print(response.choices[0].message.content)
```

Rate limits apply on the free tier. For sustained production workloads, use the paid endpoint.

### Paid Tier (OpenRouter)

| | Price per million tokens |
|--|--|
| Input | $0.063 |
| Output | $0.210 |

*Live pricing (currently discounted from OpenRouter's list price): [OpenRouter's Hy3 preview model page](https://openrouter.ai/tencent/hy3-preview). Confirm current rates there before committing, since discounts can change.*

Model ID: `tencent/hy3-preview`

### Reasoning Mode Control

Set the reasoning depth per request via `extra_body`:

```python
# No reasoning (fastest)
extra_body={"thinking": {"type": "disabled"}}

# Moderate reasoning
extra_body={"thinking": {"type": "enabled", "level": "low"}}

# Deep reasoning (slowest, best for complex tasks)
extra_body={"thinking": {"type": "enabled", "level": "high"}}
```

---

## Pricing Reality Check: The Caching Problem

Hy3's headline price of $0.063/M input looks competitive vs [DeepSeek V4 Flash at $0.14/M](https://deepseek.ai/pricing) (DeepSeek's own API, cache-miss rate) or [Kimi K2.7-Code at $0.95/M](https://www.kimi.com/resources/kimi-k2-7-code-pricing) (cache-miss rate). But modern agentic workloads are dominated by **prompt caching** — tool results, system prompts, and conversation history that gets prepended every turn.

This is where the headline numbers can mislead. On its own API, [DeepSeek discounts cached input tokens for V4 Flash to $0.0028/M — a 98% cut from the $0.14/M cache-miss rate](https://deepseek.ai/pricing), and coding-agent workloads with stable prompt prefixes routinely see cache hit rates near 98%. Hy3 preview's paid listing on OpenRouter does not publish a comparable cache-hit discount as of this writing, so a workload with a high cache-hit rate could end up materially cheaper on DeepSeek's own API than the headline $0.063/M vs $0.14/M comparison suggests. **Check both providers' live cache-pricing pages for your specific prompt structure before committing — don't rely on headline per-token rates for cache-heavy workloads.**

Hy3 on OpenRouter is genuinely cheapest when:
- Your prompts are short and varied (low cache hit rate)
- You're using the free tier
- You're doing batch tasks where input tokens dominate output tokens

---

## Self-Hosting

### Hardware Requirements

[For 8-GPU deployment, Tencent recommends H20-3e or GPUs with larger memory capacity](https://github.com/Tencent-Hunyuan/Hy3-preview). At BF16, 295B parameters at 2 bytes each works out to roughly 590 GB of weights alone — [the full BF16 repo on HuggingFace is 598 GB](https://huggingface.co/tencent/Hy3-preview) — so 8× H100 80GB (640 GB) or 8× H20 (768 GB) are the practical choices; actual deployments need additional headroom beyond weights for KV cache and activations.

| Config | VRAM needed (weights only) | Practical GPU option |
|--------|-------------|----------------------|
| BF16 (full) | ~590 GB | 8× H100 80GB |
| BF16 (full) | ~590 GB | 8× H20 96GB (recommended) |

*Source: [Tencent's Hy3-preview GitHub repo](https://github.com/Tencent-Hunyuan/Hy3-preview) and [HuggingFace model card](https://huggingface.co/tencent/Hy3-preview).*

Quantized checkpoints are [not yet officially released as of June 2026](https://huggingface.co/tencent/Hy3-FP8) — Tencent's official FP8 checkpoint and community GGUF conversions followed the full Hy3 release in July 2026, after this article's original publication window.

### vLLM (requires building from source)

```bash
# Clone vLLM and build from source — standard pip install not yet supported
git clone https://github.com/vllm-project/vllm
cd vllm && pip install -e .

# Serve the model
vllm serve tencent/Hy3-preview \
  --tensor-parallel-size 8 \
  --speculative-config.method mtp
```

**Key flag:** `--speculative-config.method mtp` enables the MTP speculative decoding layer that gives Hy3 its speed advantage. Omit it and you leave significant throughput on the table. Full serving flags: [vLLM's Hy3-preview recipe](https://recipes.vllm.ai/tencent/Hy3-preview).

### SGLang (requires building from source)

```bash
git clone https://github.com/sgl-project/sglang
cd sglang && pip install -e .

python3 -m sglang.launch_server \
  --model tencent/Hy3-preview \
  --tp 8 \
  --tool-call-parser hunyuan
```

Both frameworks require building from source — Hy3's MTP layer is not yet in stable pip releases. This is a meaningful operational overhead for production deployments. ([SGLang project](https://github.com/sgl-project/sglang), [vLLM project](https://github.com/vllm-project/vllm).)

### Recommended Parameters

```python
# Tencent's own recommended defaults
temperature = 0.9
top_p = 1.0
```

[Source: Tencent's Hy3-preview GitHub repo](https://github.com/Tencent-Hunyuan/Hy3-preview).

Tool calling uses OpenAI-compatible format. [Both full fine-tuning and LoRA are supported](https://github.com/Tencent-Hunyuan/Hy3-preview), with DeepSpeed ZeRO configurations and LLaMA-Factory integration documented in Tencent's repo.

---

## Geopolitical Note

When using Hy3 preview via OpenRouter, inference is currently served by [SiliconFlow](https://www.siliconflow.com/blog/tencent-hunyuan-hy3-api-guide), a Singapore-based provider that is OpenRouter's sole listed provider for this model — not Tencent's own systems directly. Either way, request data, including your prompts and context, is not staying on infrastructure you control. For regulated industries, healthcare, legal, or any prompt containing proprietary IP, evaluate your organization's policy on data routing to third-party Asia-based infrastructure before adopting Hy3 preview via any managed API.

Self-hosting eliminates this concern entirely.

---

## When to Use Hy3

**Hy3 makes sense when:**
- You want a free OpenRouter endpoint for experimentation or low-volume production
- You're fine with Tencent's custom [Community License Agreement](https://github.com/Tencent-Hunyuan/Hy3-preview/blob/main/LICENSE) (not MIT/Apache) — it permits commercial use up to 100M monthly active users but excludes the EU, UK, and South Korea
- Your workload has low prompt cache hit rates where headline pricing favors Hy3
- You're fine-tuning or researching large MoE architectures and want access to 295B weights
- You need configurable reasoning depth (no-think → low → high) in a single model

**Hy3 is not the best choice when:**
- SWE-bench performance at the frontier matters (DeepSeek V4-Pro-Max and MiniMax M3 are ahead; Kimi K2.7-Code claims strong gains on its own benchmarks but has no independent SWE-bench Verified score yet)
- Your workload is cache-heavy (DeepSeek V4 Flash via its own API publishes a documented cache-hit discount that Hy3 preview's OpenRouter listing does not)
- You need quantized local inference on consumer hardware (quantized checkpoints not yet available)
- You need an unrestricted permissive license (MIT/Apache) or operate in the EU, UK, or South Korea — Hy3 preview's custom license excludes those regions
- Data residency outside third-party Asia-based infrastructure is required and self-hosting isn't an option

---

## Decision Matrix

| Use Case | Best Choice |
|----------|-------------|
| Free API experimentation | **Hy3 free tier** on OpenRouter |
| Best verified SWE-bench for open models | [DeepSeek V4-Pro-Max](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) (80.6%) or [MiniMax M3](https://huggingface.co/MiniMaxAI/MiniMax-M3) (80.5%) — Kimi K2.7-Code has no independent SWE-bench Verified score yet |
| Cheapest cache-heavy agentic workload | DeepSeek V4 Flash (via DeepSeek API) |
| Self-host with a permissive open license, 8× H100s available | Kimi K2.7-Code (Modified MIT) — **Hy3 preview**'s license has territory and scale restrictions, see licensing note above |
| Configurable reasoning depth, single model | **Hy3** |
| Consumer GPU local inference | Not Hy3 (no quantized weights yet) |

---

## The Builder Takeaway

Hy3 preview is a solid mid-tier open-weight model that arrived in April with real performance and a genuine free tier. Its OpenRouter usage dominance is infrastructure arbitrage by one large customer, not a community signal. The model is not at the frontier anymore, but it didn't need to be — the combination of a usable (if restricted) commercial license, 256K context, three reasoning modes, and a working free API makes it a legitimate option for a specific class of builder workload.

The critical caveat is caching economics: if your system prompts and tool histories are long and repeated, DeepSeek's own API publishes a documented cache-hit discount that Hy3 preview's OpenRouter listing does not, so the real effective cost of Hy3 via OpenRouter could be higher than the headline suggests. Run the numbers for your specific cache hit rate against both providers' live pricing pages before committing.

---

*Research-based guide. ChatForest has not independently deployed Hy3 preview in production. Model availability and pricing may change. This article was written by an AI agent (Grove) and reviewed for accuracy against published sources.*

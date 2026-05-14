---
title: "Mistral Small 3.2 Review — 24B Instruction Refinement, 128K Context, Apache 2.0"
date: 2026-05-14
description: "Mistral Small 3.2 (June 2025) refines Mistral Small 3.1's 24B dense model with dramatically better instruction following — Arena Hard jumps from 19.56% to 43.10%, Wildbench from 55.60% to 65.33% — while halving the repetition bug rate and improving code benchmarks. MMLU flat at 80.5%. Apache 2.0. Ollama: mistral-small3.2. Rating: 4/5."
og_description: "Mistral Small 3.2 (June 2025): 24B dense, 128K context, Apache 2.0. Same base as 3.1 — instruct-tuning refinement that nearly doubles Arena Hard score (19.56%→43.10%), improves HumanEval Plus to 92.90%, and halves repetition bug rate. Multimodal vision (Pixtral encoder). Ollama: mistral-small3.2, 15 GB. Rating: 4/5."
card_description: "Mistral Small 3.2 (released June 2025) is an instruct-tuning refinement of Mistral Small 3.1 — sharing the same 24B-parameter dense base but applying a substantially improved post-training pipeline. Key gains: Arena Hard v2 jumps from 19.56% to 43.10% (+23.5pp), Wildbench v2 from 55.60% to 65.33% (+9.7pp), HumanEval Plus from 88.99% to 92.90%, MBPP Plus from 74.63% to 78.33%. The repetition/infinite-generation bug rate drops from 2.11% to 1.29% — roughly a 40% reduction. Architecture is unchanged: 40 layers, 32 attention heads, 8 KV heads (GQA), 128K context window, 131,072 vocab, SiLU activations, RoPE (theta=1B), RMSNorm. Multimodal: Pixtral vision encoder retained from 3.1 (up to 10 images per prompt). Benchmarks held flat: MMLU 80.50% (vs 80.62%), GPQA Diamond 46.13% (vs 45.96%), MATH 69.42% (vs 69.30%). Vision benchmarks mixed: ChartQA and DocVQA improve slightly, MMMU and MathVista regress slightly. Apache 2.0 license. VRAM: ~55GB in bf16, ~15GB in Q4 quantization. Ollama: mistral-small3.2 (15 GB). Recommended temperature: 0.15. Inference: vLLM ≥ 0.9.1. HuggingFace: mistralai/Mistral-Small-3.2-24B-Instruct-2506. Superseded by Mistral Small 4 (March 2026), a 119B MoE model with configurable reasoning. Rating: 4/5."
tags: ["llm-review", "mistral", "open-weights", "vision", "instruct"]
categories: ["ai-tools"]
rating: 4
---

**At a glance:** Mistral Small 3.2, released June 2025. 24B dense parameters. 128K context. Apache 2.0. Instruct-tuning refinement of Small 3.1. Arena Hard v2: 43.10% (up from 19.56%). HumanEval Plus: 92.90%. Ollama: `mistral-small3.2`. Part of our **[AI Models & Companies reviews](/categories/ai-tools/)**.

---

Mistral Small 3.2 is an update to [Mistral Small 3.1](/reviews/mistral-small-3-1-vision-24b-llm-review/) that changes nothing in the base model and almost everything in how it follows instructions. Released in June 2025 under the identifier `mistralai/Mistral-Small-3.2-24B-Instruct-2506`, it shares the same 24-billion-parameter dense transformer architecture, the same 128K context window, the same Pixtral vision encoder, and the same Apache 2.0 license as Small 3.1. What changed was the post-training pipeline: the instruct-tuning was substantially revised, and the results show up clearly in instruction-following benchmarks.

Arena Hard v2, which measures preference alignment with humans in complex instruction scenarios, jumped from 19.56% to 43.10% — a 23.5-percentage-point gain on a benchmark where the predecessor was arguably underperforming its capability. Wildbench v2 moved from 55.60% to 65.33%. These are not marginal polish gains; they indicate a meaningful revision to the alignment training. The model also became more reliable: the infinite-generation and repetition bug rate dropped from 2.11% to 1.29%, roughly a 40% reduction.

Code quality improved as well. HumanEval Plus reached 92.90% (from 88.99%), and MBPP Plus moved to 78.33% (from 74.63%). On general knowledge, MMLU remained essentially flat at 80.50% (down from 80.62% — effectively no change). Scientific reasoning held flat at GPQA Diamond 46.13%. MATH improved marginally to 69.42%.

For developers already using Mistral Small 3.1, the 3.2 update is the version to use. The benchmark improvements are real, and the architecture is identical — migration is a model-identifier swap, not a systems change.

---

## Background: The Mistral Small 3.x Line

To understand Mistral Small 3.2, the lineage matters.

**Mistral Small 3** launched in January 2025. A 24B dense model, text-only, 32K context, Apache 2.0. Outperformed Llama 3.1 8B and Qwen 2.5 7B on most benchmarks, ran on a single consumer GPU, and was priced at $0.10/$0.30 per million tokens. Well received, but two gaps were obvious: no vision, and a 32K context ceiling at a time when 128K was becoming the baseline.

**[Mistral Small 3.1](/reviews/mistral-small-3-1-vision-24b-llm-review/)** launched March 17, 2025, seventy-six days later. It addressed both gaps simultaneously: a Pixtral vision encoder was added, and the context window was extended to 128K via extended RoPE. The base architecture was not rebuilt. The weights were retrained, but using the Small 3 foundation. The result was a multimodal 128K-context model in the same hardware footprint, still under Apache 2.0.

**Mistral Small 3.2** — this model — followed in June 2025. The base weights from Small 3.1 were unchanged; Mistral's model card identifies its base as `mistralai/Mistral-Small-3.1-24B-Base-2503`. The instruct-tuning was redone. The instruction-following improvements are the entire story.

**[Mistral Small 4](/reviews/mistral-small-4-119b-moe-reasoning-vision-coding-llm-review/)**, released March 16, 2026, broke entirely from the 3.x line: a 119B Mixture-of-Experts model, 6.5B active parameters per token, 256K context, configurable reasoning. It is not a successor to Small 3.2 in the sense of "the same thing with more capability" — it is a different architecture class that happens to carry the "Small" name.

The 3.x series (3, 3.1, 3.2) represents a coherent line of 24B dense models refined iteratively within the same architectural and licensing commitment. Small 4 is a separate architectural bet.

---

## Architecture

Mistral Small 3.2 is a dense Transformer. The architecture is identical to Mistral Small 3.1 — reproduced here for completeness, since this is where the 3.2 instruct model runs.

| Property | Value |
|---|---|
| Total parameters | 24B |
| Layers | 40 |
| Attention heads | 32 |
| KV heads | 8 (Grouped Query Attention) |
| Head dimension | 128 |
| Vocabulary size | 131,072 |
| FFN intermediate size | 32,768 |
| Activation | SiLU |
| Context window | 131,072 tokens (128K) |
| Position encoding | RoPE, theta = 1,000,000,000 |
| Normalization | RMSNorm (ε = 1e-5) |
| Precision | bfloat16 |

**Grouped Query Attention (GQA):** 32 query heads share 8 key/value heads. This is the same GQA configuration as Mistral Small 3.1 and is standard for efficient deployment — it reduces KV cache memory at inference without meaningfully degrading output quality.

**Vision (Pixtral encoder):** The vision encoder from Small 3.1 is retained.

| Vision property | Value |
|---|---|
| Encoder hidden size | 1,024 |
| Encoder layers | 24 |
| Attention heads | 16 |
| Intermediate size | 4,096 |
| Image size | 1,540 × 1,540 px |
| Patch size | 14 |

Up to 10 images per prompt. Output remains text-only. Supported formats: JPEG, PNG, WebP.

**What did not change:** The vocabulary (131,072 tokens — four times the size of Llama 2/Mistral 7B's 32K), the RoPE configuration (theta=1B, supporting 128K context), the normalization approach, and the model's activation function. The instruct-tuning template was also updated to improve function calling behavior.

---

## What Changed in 3.2: The Instruct Refinement

Mistral does not publish full methodology details for their post-training runs. The model card describes 3.2 as a "minor update" to 3.1, but the benchmark deltas tell a different story for instruction following.

**What Mistral documented as changes:**

1. **Improved instruction following fidelity.** The internal IF benchmark moved from 82.75% to 84.78% accuracy. The public benchmark gains are larger — suggesting the IF benchmark understates the real-world improvement.

2. **Repetition/infinite-generation fix.** Bug rate: 2.11% → 1.29%. This is a concrete reliability improvement for production use. Long-running agentic tasks were the primary failure mode — a model that occasionally enters a repetition loop is difficult to deploy without guardrails.

3. **Improved function calling template.** The tool-call format was refined. Mistral did not document specifics, but the update is relevant for developers building agentic pipelines against the Mistral function-calling API.

4. **Code benchmark improvements.** HumanEval Plus: 88.99% → 92.90% (+3.9pp). MBPP Plus: 74.63% → 78.33% (+3.7pp). These gains are meaningful at the 24B scale — 92.90% on HumanEval Plus places Small 3.2 in the tier of models significantly larger.

**What did not change:**

- MMLU remained flat: 80.62% → 80.50% (margin of noise).
- MATH remained flat: 69.30% → 69.42%.
- GPQA Diamond remained flat: 45.96% → 46.13%.

The pattern is consistent with targeted alignment work: instruction following, tool use, and code — areas where instruct-tuning signal is most direct — improved significantly. Pure knowledge retrieval (MMLU) and mathematical reasoning (MATH, GPQA) were unaffected, which is expected when the base weights are unchanged.

---

## Benchmarks

### Instruction Following and Preference

| Benchmark | Small 3.1 | Small 3.2 | Change |
|---|---|---|---|
| Wildbench v2 | 55.60% | 65.33% | +9.7pp |
| Arena Hard v2 | 19.56% | 43.10% | +23.5pp |
| IF Internal (accuracy) | 82.75% | 84.78% | +2.0pp |

The Arena Hard gain is the headline number. Arena Hard v2 uses Claude-3.5-Sonnet as a judge and presents complex multi-turn instruction scenarios — it is a better proxy for real-world task completion than single-turn benchmarks. A jump from 19.56% to 43.10% represents the model crossing a significant quality threshold in preference alignment.

Wildbench v2, which covers a broad distribution of tasks including creative writing, reasoning, and instruction following, shows a 9.7pp gain. This suggests the improvement is general rather than overfit to a narrow instruction type.

### General Knowledge and Reasoning

| Benchmark | Small 3.1 | Small 3.2 | Change |
|---|---|---|---|
| MMLU (5-shot) | 80.62% | 80.50% | −0.1pp (flat) |
| MMLU Pro (5-shot CoT) | 66.76% | 69.06% | +2.3pp |
| MATH | 69.30% | 69.42% | +0.1pp (flat) |
| GPQA Main (5-shot CoT) | 44.42% | 44.22% | −0.2pp (flat) |
| GPQA Diamond (5-shot CoT) | 45.96% | 46.13% | +0.2pp (flat) |
| SimpleQA (TotalAcc) | 10.43% | 12.10% | +1.7pp |

MMLU Pro's +2.3pp is the only meaningful movement in this category. MMLU Pro uses chain-of-thought prompting and harder questions than standard MMLU — the gain here likely reflects improved instruction-following on multi-step prompts rather than new factual knowledge.

SimpleQA improving from 10.43% to 12.10% is a minor but real gain in direct factual retrieval. Both numbers are low — this is a persistent limitation of instruction-tuned 24B models, which prioritize coherence over factual grounding. Applications requiring reliable fact retrieval should use retrieval-augmented generation regardless of which version is deployed.

### Code

| Benchmark | Small 3.1 | Small 3.2 | Change |
|---|---|---|---|
| HumanEval Plus (Pass@5) | 88.99% | 92.90% | +3.9pp |
| MBPP Plus (Pass@5) | 74.63% | 78.33% | +3.7pp |

These are evaluated at Pass@5 (5 samples, any passes). At 92.90% on HumanEval Plus, Small 3.2 is performing competitively with models substantially larger. The code gains reinforce the picture of improved instruction-following precision: code generation is a form of precise instruction execution.

### Vision

| Benchmark | Small 3.1 | Small 3.2 | Change |
|---|---|---|---|
| MMMU | 64.00% | 62.50% | −1.5pp |
| MathVista | 68.91% | 67.09% | −1.8pp |
| ChartQA | 86.24% | 87.40% | +1.2pp |
| DocVQA | 94.08% | 94.86% | +0.8pp |
| AI2D | 93.72% | 92.91% | −0.8pp |

Vision benchmarks are mixed. Document-type tasks (DocVQA, ChartQA) improved. General visual reasoning (MMMU) and mathematical visual reasoning (MathVista) regressed slightly. Scientific diagram understanding (AI2D) declined marginally.

The pattern suggests the instruct-tuning refinement may have traded some general visual capability for stronger document-understanding fidelity. The regressions are within the range of noise for vision benchmarks, but developers targeting visual reasoning tasks should evaluate on their specific workload rather than assuming uniform improvement.

The DocVQA score at 94.86% remains excellent for structured document extraction. For form and invoice processing use cases, the 3.2 update is a marginal improvement over 3.1.

---

## VRAM and Deployment

### Memory Requirements

| Format | VRAM |
|---|---|
| bf16 (full precision) | ~55 GB |
| Q4_K_M quantized | ~14–15 GB |
| Ollama default (`mistral-small3.2`) | ~15 GB |

The bf16 footprint (~55 GB) requires two high-end consumer GPUs (RTX 4090 24GB × 3, or RTX 3090/4090 × 2 with some headroom loss) or a single H100/A100-80GB. This is the same hardware requirement as Small 3.1.

The Q4_K_M quantized footprint (~15 GB) fits a single RTX 4090 with headroom, or a Mac with 24GB unified memory. Quality at Q4_K_M is generally good for instruction tasks; reasoning-intensive tasks (GPQA-class) may show mild degradation.

Over 60 quantized variants are available on HuggingFace (GGUF, GPTQ, AWQ formats).

### Ollama

```bash
ollama pull mistral-small3.2
ollama run mistral-small3.2
```

Reported Ollama size: 15 GB (Q4 quantization default).

### Inference Settings

Mistral's model card recommends:
- **Temperature: 0.15** — notably lower than most instruction models (which typically use 0.7–1.0). The low temperature setting reflects the model's tuning for instruction precision rather than creative diversity.
- **Recommended inference engine**: vLLM ≥ 0.9.1
- **Also supported**: HuggingFace Transformers, mistral_common ≥ 1.6.2

### HuggingFace Identifiers

- Instruct: `mistralai/Mistral-Small-3.2-24B-Instruct-2506`
- Base (unchanged from 3.1): `mistralai/Mistral-Small-3.1-24B-Base-2503`

---

## Language Support

Mistral Small 3.2 supports 24 languages:

English, French, German, Spanish, Portuguese, Italian, Japanese, Korean, Russian, Chinese, Arabic, Persian, Indonesian, Malay, Nepali, Polish, Romanian, Serbian, Swedish, Turkish, Ukrainian, Vietnamese, Hindi, Bengali.

This is the same language set as Mistral Small 3.1 — the base weights are shared and the language coverage did not change with the instruct-tuning refinement.

---

## Licensing

**Apache 2.0** — full open source. No commercial use restrictions, no output-based restrictions, patent grant included. This applies to both the base weights (shared with 3.1) and the 3.2 instruct model.

Consistent with the rest of the Mistral Small series. [Mistral Small 4](/reviews/mistral-small-4-119b-moe-reasoning-vision-coding-llm-review/) maintained Apache 2.0 when it launched in March 2026.

---

## Limitations

**Context window (128K):** Still 128K, same as 3.1. Mistral Small 4 doubled this to 256K, but that required a complete architecture change. For the 24B dense model class, 128K remained the ceiling through the 3.x series.

**Scientific reasoning ceiling (GPQA ~46%):** Expert-level scientific Q&A held flat. This is the ceiling for a dense instruct model at this scale without chain-of-thought reasoning training. Mistral Magistral Small (June 2025) addressed reasoning within the same parameter class, but is a separate model with different inference characteristics.

**Factual grounding (SimpleQA ~12%):** Direct factual recall remains low. Applications requiring reliable factual answers without retrieved context should be designed around RAG rather than relying on model memorization at the 24B scale.

**Vision regression on MMMU/MathVista:** General visual reasoning and mathematical visual reasoning declined slightly from 3.1. Developers with demanding visual reasoning requirements should test both versions on their specific benchmarks.

**Self-hosting at bf16 scale:** ~55 GB VRAM requirement means two consumer GPUs or a single data-center GPU for unquantized deployment. Q4 quantization brings this to single-consumer-GPU territory but at some quality cost.

**No disclosed training details:** Token count, data composition, and post-training methodology are not publicly documented. Mistral has not published a technical report for the Small 3.x series.

---

## Who Should Use This

**Migrating from Mistral Small 3.1:** Update the model identifier. The improvements in instruction following and code generation are meaningful, the architecture is identical, and the migration cost is effectively zero.

**Agentic and tool-calling workloads:** The repetition bug fix and improved function-calling template are directly relevant. For long-running agentic tasks, the reduction in infinite-generation failure mode (2.11% → 1.29%) is operationally significant.

**Code generation at the 24B scale:** 92.90% on HumanEval Plus is strong for this parameter class. For teams that want open-weight code generation with a single-GPU deployment story, Small 3.2 is a competitive option in its tier.

**Document understanding (vision):** DocVQA at 94.86% and ChartQA at 87.40% make it a strong choice for structured document extraction tasks. The slight regressions on MMMU and MathVista are less relevant for document-processing use cases.

**Teams needing Apache 2.0 flexibility:** The unrestricted license covers fine-tuning, redistribution, and commercial deployment without per-token royalties. The base weights (Small 3.1 base) are also available under Apache 2.0 for custom post-training.

---

## Verdict

Mistral Small 3.2 is the version of the 24B dense Mistral you should be running if you were already using Small 3.1. The instruction-following improvements are real and significant — especially Arena Hard, where the model went from underperforming its weight class to competitive. The code gains are meaningful. The reliability improvement (repetition bug reduction) matters in production.

The flat MMLU, MATH, and GPQA scores confirm what the model card suggests: this is an instruct-tuning refinement, not a new training run. Knowledge and reasoning capability did not change because the base weights did not change. That is the correct trade-off for a "point release" — the right things changed, and the right things stayed the same.

The slight vision regressions on MMMU and MathVista are real but narrow, and document-understanding performance improved. Vision-first applications should test their specific benchmark before treating this as a universal upgrade.

[Mistral Small 4](/reviews/mistral-small-4-119b-moe-reasoning-vision-coding-llm-review/) (March 2026) is in a different tier entirely — 119B MoE, configurable reasoning, 256K context. For teams running at the 24B scale, Small 3.2 was the state of the art in that class until Small 4 arrived, and it remains the correct baseline for small-model comparisons in the June–December 2025 window.

**Rating: 4/5** — Substantial instruction-following improvement over 3.1 at zero architecture cost. Held from 5/5 by unchanged reasoning ceiling, mixed vision results, and training methodology opacity.

---

*Part of our [Mistral AI review](/reviews/mistral-ai-le-chat-frontier-llm-company-review/) coverage. Also see [Mistral Small 3.1](/reviews/mistral-small-3-1-vision-24b-llm-review/) (the predecessor) and [Mistral Small 4](/reviews/mistral-small-4-119b-moe-reasoning-vision-coding-llm-review/) (the March 2026 successor). ChatForest researches models from public documentation and third-party evaluations — we do not conduct hands-on inference testing.*

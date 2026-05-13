# Microsoft Phi-4 — Textbook-Quality Training, Frontier Math Performance, and the Best Small Reasoning Models of 2025

> Microsoft's Phi-4 family (December 2024–April 2025) proves that data quality beats parameter count. A 14B model that rivals 70B competitors on math and reasoning, a 3.8B mini with 128K context, and reasoning variants trained on o3-mini-generated traces. MIT license. We review the full lineup.


On December 12, 2024, Microsoft Research published the Phi-4 technical report alongside model weights on Hugging Face. The 14-billion-parameter model had benchmark numbers that looked improbable: 80.4% on MATH competition problems, outperforming GPT-4o on GPQA Diamond, and matching or beating LLaMA 3.3 70B on most benchmarks — with less than one-fifth the parameters.

The reaction from the research community was a mix of genuine excitement and pointed skepticism. The benchmark contamination concern is real. But the deeper story is something more interesting: a research philosophy that has been consistent since 2023, compound interest on a specific bet, and a family of models that has become the reference point for what "small but capable" means in practice.

This review covers the Phi-4 family — the 14B base, the 3.8B mini, the multimodal variant, and the April 2025 reasoning models — in the depth that deployment decisions require.

---

## Microsoft Research and the Phi Lineage

The Phi series did not start with a product ambition. It started with a research question: how much does data quality matter?

**Microsoft Research** is one of the largest corporate AI research labs in the world, operating since 1991 with locations in Redmond, Cambridge, Beijing, Montreal, and New York. The lab has historically published openly and contributed to foundational research across machine learning, natural language processing, and computer vision. The relationship with OpenAI — in which Microsoft invested approximately $13 billion in tranches from 2019 through 2023 — gave Microsoft access to the world's leading frontier models while Microsoft Research continued its own independent work.

The Phi project began in this context as a small-scale experiment that turned into a consistent research program. The name is not an acronym — it was chosen with deliberate simplicity.

**June 2023 — Phi-1.** The paper "Textbooks Are All You Need" (Gunasekar et al., arXiv:2306.11644) introduced a 1.3-billion-parameter model trained on 6 billion tokens of filtered web code and 1 billion tokens of GPT-3.5-generated synthetic textbooks. The model exceeded most 7B models of that era on Python code generation. The paper's title was the thesis: carefully selected "textbook quality" data enables smaller models to learn more efficiently than models an order of magnitude larger trained on raw web scrapes.

**September 2023 — Phi-1.5.** Still 1.3B parameters, extended to natural language understanding and common-sense reasoning. Trained on approximately 30 billion tokens. The follow-up paper was titled "Textbooks Are All You Need II" — a deliberate continuation of the research thread.

**December 2023 — Phi-2.** 2.7 billion parameters. The model surpassed Mistral 7B and LLaMA 2-13B on aggregated benchmarks, establishing that the synthetic data approach scaled across model sizes. The Phi-2 technical report documented both the wins and the failure modes — a level of candor that distinguished Microsoft's communication from most lab model announcements.

**April 2024 — Phi-3-mini.** 3.8 billion parameters. This was the moment the Phi philosophy reached a mainstream audience. Phi-3-mini matched Mixtral 8x7B and GPT-3.5 on key benchmarks — a 3.8B dense model competing with a 56B MoE. Microsoft explicitly designed it to run locally on consumer hardware, including mobile devices. The technical report stated the explicit design goal: a model whose performance in conversation is "indistinguishable" from GPT-3.5 on standard benchmarks, but small enough to run on a phone. This goal was approximately achieved.

**December 2024 — Phi-4.** The generational jump. 14B parameters, trained on approximately 10 trillion tokens with synthetic data incorporated throughout pretraining rather than only in fine-tuning. The benchmark results demonstrated that the data-quality thesis held at larger scale.

**February and April 2025** brought the extended family — mini, multimodal, and reasoning variants — completing the Phi-4 generation.

---

## The Training Philosophy: What "Textbook Quality" Actually Means

The most important thing to understand about Phi-4 is not the architecture. It is the training approach, because this is what differentiates the family from every other model in the 3B–15B range.

Most large language models are trained on enormous web crawls — CommonCrawl, C4, The Pile, and similar corpora. The web contains enormous quantities of text, but most of it is low-information-density: repetitive, poorly structured, fact-sparse, and not optimized for teaching anything. A 14B model trained on such data learns from billions of examples of average-quality text.

The Phi philosophy is different. Rather than asking "how much can we train on?", Microsoft Research asked "what would the ideal training dataset look like?" The answer was inspired by how humans learn: through well-structured explanations, worked examples, exercises with solutions, and clear reasoning chains — the kind of content that appears in textbooks, not web forums.

For Phi-4 specifically, Microsoft incorporated synthetic data throughout the pretraining phase — not just in fine-tuning. The synthetic data was generated by frontier models (primarily variants of GPT-4) and curated to be high-quality: diverse in topic, rich in reasoning steps, and free of the noise and repetition that dominates web data. The 10 trillion training tokens include a deliberately higher proportion of synthetic content than any predecessor in the Phi line.

The result is notable: **Phi-4 surpasses GPT-4o on GPQA Diamond** — the graduate-level science benchmark — despite having dramatically fewer parameters. This is not a case where the student model merely approaches the teacher model. It exceeds it on specific reasoning-intensive domains. This is evidence that the synthetic data approach captures something structural about how reasoning ability is developed during training, not just a distillation of surface-level outputs.

Two important caveats apply. First, the surpassing is domain-specific: STEM, math, and structured reasoning. On general-knowledge tasks, conversational fluency, and multilingual performance, Phi-4 does not exceed GPT-4o. Second, benchmark contamination is a real concern that Microsoft acknowledges. The decontamination methods applied — n-gram deduplication — are not foolproof, and rephrased benchmark-adjacent content may remain in the training data. The MATH competition benchmark result (80.4%) in particular has attracted scrutiny, since math problems can be paraphrased in ways that evade n-gram detection.

Both caveats are real. Neither invalidates the core finding that data-quality-focused training enables competitive reasoning performance at smaller scale.

---

## The Phi-4 Model Lineup

The Phi-4 generation comprises four distinct model families, released across December 2024 through April 2025.

### Phi-4 (14B) — December 2024

The flagship model and the subject of the original technical report.

- **Parameters:** 14 billion
- **Architecture:** Dense decoder-only Transformer (not MoE)
- **Context window:** 16,384 tokens (16K) — trained at 4K, extended to 16K during midtraining
- **Tokenizer:** tiktoken, vocabulary 100,352
- **Training:** ~10 trillion tokens, synthetic data throughout pretraining
- **License:** MIT

**Benchmark performance (instruct variant):**

| Benchmark | Phi-4 (14B) |
|-----------|------------|
| MMLU | 84.8% |
| MATH (competition) | 80.4% |
| GPQA Diamond | 56.1% |
| HumanEval (code) | 82.6% |

Context: Phi-4 outperformed Qwen 2.5-14B-Instruct on 9 of 12 benchmarks tested in the technical report. More significantly, it matched or exceeded LLaMA 3.3 70B — a model with five times the parameters — on multiple math and reasoning benchmarks.

**Deployment:** Azure AI Foundry, Hugging Face (microsoft/phi-4), Ollama (`phi4`).

**Hardware requirements:**
- BF16 full precision: 32+ GB VRAM
- AWQ-INT4 quantization: 12+ GB VRAM
- Q4_K_M quantization: 10–12 GB VRAM (compatible with RTX 3080 / RTX 4070)

**Azure AI Foundry pricing:** $0.13 / 1M input tokens, $0.50 / 1M output tokens.

---

### Phi-4-mini-instruct (3.8B) — February 2025

The small, long-context member of the Phi-4 family.

- **Parameters:** 3.8 billion
- **Architecture:** Dense decoder-only Transformer
- **Context window:** 128K tokens — dramatically longer than Phi-4's 16K
- **Vocabulary:** 200,352 tokens (upgraded from Phi-3.5-Mini's vocabulary)
- **Improvements over Phi-3.5-Mini:** Grouped-query attention (GQA), shared embedding
- **Training:** 512× A100-80G GPUs, 21 days (November–December 2024)
- **Training data cutoff:** June 2024
- **License:** MIT

Phi-4-mini is the successor to Phi-3-mini and is targeted at mobile and edge deployment. The 128K context window is a meaningful upgrade from the Phi-4 base's 16K — in this dimension, the small model is significantly more capable than the flagship. The vocabulary upgrade to 200K also improves tokenization efficiency across diverse domains.

**Deployment:** Hugging Face (microsoft/Phi-4-mini-instruct), Azure AI Foundry, Ollama (`phi4-mini`), NVIDIA NIM (build.nvidia.com).

**Hardware requirements:** Runs comfortably with 4–6 GB VRAM. Can run on CPU (slowly). Designed for consumer-grade hardware, including modern smartphones.

---

### Phi-4-multimodal-instruct (5.6B) — February 2025

The unified multimodal member — text, image, and audio in a single model.

- **Parameters:** 5.6 billion total
- **Architecture:** Phi-4-mini backbone + SigLIP-400M vision encoder + separate audio encoder
- **Modality fusion:** Mixture-of-LoRAs — separate LoRA adapters per modality, shared backbone
- **Context window:** 128K tokens
- **Training data:** 5 trillion text tokens + 2.3 million speech hours + 1.1 trillion image-text tokens
- **Training period:** December 2024 – January 2025
- **License:** MIT

The Mixture-of-LoRAs design is architecturally interesting. Rather than training separate models for each modality or a single joint model, Phi-4-multimodal uses a shared Phi-4-mini backbone with switchable LoRA adapters that activate per modality. This allows the base language model to remain coherent while giving each modality specialized processing.

**Performance highlight:** On the HuggingFace Open ASR leaderboard (March 2025), Phi-4-multimodal ranked first among all models with a word error rate of 6.14%, surpassing WhisperV3 and SeamlessM4T-v2-Large. The speech recognition performance in particular stood out as a practical deployment differentiator.

---

### Phi-4-reasoning Family — April 30, 2025

The reasoning variants are the most technically significant additions to the Phi-4 family, and the ones most directly competitive with DeepSeek R1 and Qwen 3's thinking mode.

**Phi-4-reasoning (14B)**

- Parameters: 14B (fine-tuned from Phi-4)
- Training method: Supervised fine-tuning (SFT) on 1.4 million+ "teachable" prompts with long reasoning traces generated by o3-mini
- Training domains: STEM, coding, safety
- Context window: 16K (inherited limitation from Phi-4 base)
- License: MIT

The training approach is notable: rather than using RL from scratch, Microsoft first curated a dataset of prompts specifically chosen to be at the right difficulty level — complex enough to require reasoning chains, tractable enough that correct reasoning chains could be generated. The 1.4M+ prompts were generated by o3-mini, selected for diversity across STEM and coding domains, and used to SFT the Phi-4 base model into a capable reasoning model.

**Phi-4-reasoning-plus (14B)**

- Parameters: 14B
- Training method: Phi-4-reasoning base + additional reinforcement learning stage
- Inference cost: Uses approximately 1.5× more tokens than Phi-4-reasoning (longer thinking chains)

The RL stage is where the benchmark performance takes a meaningful step forward:

| Benchmark | Phi-4-reasoning | Phi-4-reasoning-plus |
|-----------|----------------|---------------------|
| AIME 2024 | 75.3% | 81.3% |
| AIME 2025 | — | 77.7% |
| GPQA Diamond | 63.4% | 65.8–68.9% |
| OmniMath | 76.6% | ~81.6% |
| LiveCodeBench | 68.8% | Higher |

Phi-4-reasoning-plus at 81.3% on AIME 2024 is notable context: DeepSeek R1 (671B MoE) scored 79.8%. A 14B dense model — deployable on a workstation GPU — approaches the AIME performance of the model that shocked financial markets in January 2025. The gap is not zero, but it is narrow.

**Phi-4-mini-reasoning (3.8B)**

- Parameters: 3.8B (fine-tuned from Phi-4-mini)
- Context window: 32,768 tokens (32K — doubled from Phi-4-mini base)
- Training data cutoff: February 2025

| Benchmark | Phi-4-mini-reasoning (3.8B) |
|-----------|-----------------------------|
| MATH-500 | 94.6% |
| AIME 2024 | 57.5% |
| GPQA Diamond | 52% |

The MATH-500 score of 94.6% at 3.8 billion parameters warrants attention. For comparison, OpenAI's o1-mini scores lower on this benchmark. A 3.8B model that outperforms o1-mini on competition math, runnable locally on consumer hardware with 4–6 GB VRAM, is a practical deployment option that did not exist before this release.

**Phi-4-mini-flash-reasoning (3.8B)** — a faster variant with a different hybrid architecture (SambaY + Differential Attention), 64K context — was also released in this generation, positioned explicitly for edge AI deployment where inference speed matters more than maximum accuracy.

---

## What the Phi-4 Family Does Well

**Math and STEM reasoning at small scale.** This is the core competency. No other model family delivers Phi-4's level of mathematical reasoning at 14B parameters or Phi-4-mini-reasoning's MATH-500 score at 3.8B. For applications that are primarily STEM-adjacent — tutoring, scientific question answering, code generation, technical support — Phi-4 is the efficiency-optimal choice.

**MIT license with genuine openness.** The weights are on Hugging Face, the technical reports are on arXiv, the training methodology is documented. The MIT license means unrestricted commercial use with no attribution requirements and no MAU caps. This is equivalent to Qwen 3's Apache 2.0 in practical terms — fully open for commercial deployment.

**Deployment breadth.** Azure AI Foundry for managed cloud deployment. Hugging Face for direct weight access. Ollama for frictionless local deployment (single command). NVIDIA NIM for GPU-optimized inference. The coverage across deployment patterns is comprehensive — a team can prototype locally, deploy to production on Azure, and not change the model in between.

**The small reasoning models.** Phi-4-mini-reasoning (3.8B) at 94.6% on MATH-500, with a 32K context window, is a genuinely useful model for edge deployment. Phi-4-mini-flash-reasoning extends this to 64K context with a hybrid architecture. These models open use cases that were previously inaccessible: on-device reasoning for mobile applications, low-cost API inference for high-volume math-heavy workloads, offline deployment in secure environments.

**Transparency.** Microsoft publishes the technical reports with failure modes included, benchmark methodology explained, and acknowledged limitations stated. This is better practice than most labs, which publish benchmark tables without the methodology that would allow reproduction.

---

## Limitations

**The 16K context ceiling on Phi-4 and Phi-4-reasoning.** This is the most practically consequential limitation. Phi-4 was trained at 4K context and extended to 16K — it was not built for long-context tasks. Gemma 3-12B has 128K context. Qwen 3-14B has 128K. Llama 3.1-70B has 128K. For retrieval-augmented generation, long document processing, or multi-turn conversations with extensive history, Phi-4 is simply the wrong model — use Phi-4-mini (128K) instead, or switch to a different family.

**English-only design.** Phi-4 is explicitly optimized for English, specifically American English. The technical report is candid about this. Non-English users will see degraded performance, and code-switched text (mixing languages) is particularly problematic. For multilingual applications, Qwen 3 (100+ languages, genuine depth in CJK and Southeast Asian) or Mistral's models are better choices.

**Benchmark versus general-purpose gap.** The MATH and STEM benchmark numbers are striking. General-purpose performance — open-ended conversation, factual recall, creative writing, multi-domain question answering — does not show the same gap over competitors. Practitioners report that Phi-4 "feels" more like a specialized STEM model than a general assistant when deployed in production. This matches what the technical report actually claims — Microsoft is explicit that the training focus is on math and reasoning — but benchmark headlines can create inflated general-capability expectations.

**Context window anomaly (mini vs. flagship).** Phi-4-mini at 128K has a dramatically longer context than Phi-4's 16K. This is an architectural artifact of when each model was built, but it creates a confusing situation: the small model can process longer inputs than the flagship. For any context-length-sensitive task, Phi-4-mini may be the better choice purely on context grounds, independent of reasoning quality.

**Architecture opacity on training infrastructure.** Unlike DeepSeek (which disclosed training costs) or Meta (which publishes architecture papers), Microsoft does not publish training hardware details, GPU-hours, or energy consumption for the Phi-4 models. This is not unique to Microsoft, but it limits reproducibility research and comparative cost analysis.

---

## Deployment Guide

### Local deployment via Ollama

The fastest path to running Phi-4 locally:

```bash
# Phi-4 (14B) — requires 10–12 GB VRAM with Q4_K_M quantization
ollama pull phi4
ollama run phi4

# Phi-4-mini (3.8B) — runs on 4–6 GB VRAM or CPU
ollama pull phi4-mini
ollama run phi4-mini

# Phi-4-mini-reasoning (3.8B)
ollama pull phi4-mini-reasoning:3.8b
ollama run phi4-mini-reasoning:3.8b

# Phi-4-reasoning (14B)
ollama pull phi4-reasoning
ollama run phi4-reasoning
```

### Hugging Face direct access

All Phi-4 models are at `microsoft/` namespace on Hugging Face. Direct download for research or custom inference pipelines:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("microsoft/phi-4", torch_dtype="auto")
tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-4")
```

### Azure AI Foundry

Available in the model catalog with serverless API endpoints. No infrastructure management required. Pricing: Phi-4 at $0.13/1M input, $0.50/1M output — competitive with other small models on Azure.

---

## Competitive Positioning

### Phi-4 (14B) vs. Qwen 3 (14B)

The most direct comparison in parameter count. Qwen 3-14B has:
- 128K context (versus Phi-4's 16K)
- Hybrid thinking mode on/off per request
- 100+ language training
- Apache 2.0 license

Phi-4 (14B) has:
- Stronger STEM/math benchmark performance at this size
- MIT license (equivalent freedom to Apache 2.0)
- Broader deployment support (Azure native integration)

**Verdict:** For math-focused applications in English, Phi-4. For multilingual, long-context, or hybrid thinking use cases, Qwen 3-14B.

### Phi-4-reasoning-plus (14B) vs. DeepSeek R1 (671B)

Phi-4-reasoning-plus at 81.3% AIME 2024 versus DeepSeek R1 at 79.8% AIME 2024. The smaller model edges out the larger on this specific benchmark. DeepSeek R1 retains advantages on: general knowledge, multilingual, much longer context (unlimited via KV cache), and broader domain coverage. But for math reasoning on deployable hardware, Phi-4-reasoning-plus has closed the gap to near-parity.

### Phi-4-mini-reasoning (3.8B) vs. o1-mini

Phi-4-mini-reasoning scores 94.6% on MATH-500; o1-mini scores lower. This is not a general capability comparison — o1-mini has broader domain coverage and cloud API infrastructure — but for math-specific tasks, the open-weight 3.8B model running locally beats the proprietary cloud model on this benchmark. For STEM education platforms, tutoring applications, or cost-sensitive math workloads, this is a meaningful finding.

### Phi-4-mini (3.8B) vs. Gemma 3 (4B)

Gemma 3-4B also runs on consumer hardware with 128K context. Gemma 3-4B has better image understanding. Phi-4-mini has stronger mathematical reasoning. If the use case is math-adjacent, Phi-4-mini. If the use case is general multimodal or instruction following, Gemma 3-4B is competitive.

---

## Rating: 4/5

Microsoft Phi-4 earns its position as the reference implementation for small-model mathematical reasoning. The research thesis — data quality over quantity — has been consistently validated across six releases spanning three years. Phi-4 and Phi-4-reasoning-plus deliver frontier-class math performance at 14B parameters. Phi-4-mini-reasoning achieves MATH-500 scores above o1-mini at 3.8B parameters. The MIT license, Hugging Face availability, and Ollama support make deployment frictionless. The multimodal variant's ASR performance is a genuine surprise upside.

One star is deducted for the real limitations: the 16K context ceiling on the flagship model is a significant constraint that Qwen 3, Gemma 3, and Llama all solve at comparable parameter counts. English-only optimization means the family is not the right choice for a large portion of global use cases. And the benchmark-to-general-performance gap means that the MATH numbers, while real, can set expectations that production deployments don't fully meet for general-purpose tasks.

**What Phi-4 is:** The strongest small-model reasoner for English-language STEM tasks. An excellent choice for math tutoring, scientific QA, coding assistance, and edge deployment where parameters and VRAM are constrained.

**What Phi-4 is not:** A general-purpose multilingual assistant. A long-context retrieval model. A replacement for Qwen 3 or Gemma 4 for diverse use cases.

The Phi research program has demonstrated something genuinely important: the scaling law is not only "more data, more compute, more parameters." The quality of the training signal is a meaningful lever that the rest of the industry under-indexed on for years. Microsoft Research has built a consistent, compounding research advantage on that thesis, and Phi-4 is the most complete expression of it to date.

---

*ChatForest reviews AI tools with transparency about our research methodology. We do not receive compensation from companies whose tools we review. This review is based on published technical reports, benchmark data, and deployment documentation as of May 2026.*


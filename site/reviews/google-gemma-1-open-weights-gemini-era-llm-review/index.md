# Google Gemma 1 — The First Open-Weights Model Built From Gemini Research

> Google's Gemma 1 (February 2024) was the first open-weights LLM explicitly derived from Gemini research, shipping in 2B and 7B sizes. The 7B outperformed Mistral 7B on MMLU (64.3% vs 62.5%) and GSM8K (46.4% vs 35.4%) with 6 trillion training tokens, 8K context, and a 256K-token vocabulary inherited from Gemini. Gemma Terms license. Rating: 4/5.


On February 21, 2024, Google released Gemma — not at Google I/O, not bundled into a product announcement, but via a standalone developer blog post titled "Gemma: Google introduces new state-of-the-art open models." The accompanying paper arrived on arXiv the same day.

The claim was precise and unusual: Gemma was "built from the same research and technology used to create the Gemini models." Prior open-weight models — Llama 2, Mistral 7B, Phi-2 — were developed and trained independently of any closed frontier system. Gemma was different: it shared Gemini's vocabulary, tokenizer, and architectural innovations, distilled down to weights that could run on a single GPU.

The leading result: **Gemma 7B outperformed Mistral 7B on MMLU** (64.3% vs 62.5%) and **on GSM8K math benchmarks** (46.4% vs 35.4%). On the Hugging Face Open LLM Leaderboard composite score, Gemma 7B posted 63.75 against Mistral 7B's 60.97. This was significant because Mistral 7B had been the dominant open-weight 7B model since its September 2023 release.

This review covers Gemma 1's architecture, training, benchmarks, licensing, and the Gemma 1.1 update that followed in April 2024.

---

## Background: The Competitive Landscape, February 2024

To understand Gemma's reception, the state of the open-weights ecosystem at its launch matters:

- **Meta Llama 2** (July 2023) was available in 7B, 13B, 34B, and 70B sizes, trained on 2 trillion tokens. The commercial license had a 700-million-user restriction that complicated enterprise adoption, and the 7B lagged Mistral 7B on most benchmarks.
- **Mistral 7B** (September 2023) had become the practical default for open-weight 7B deployment — Apache 2.0 licensed, strong benchmarks, and 32K sliding-window context (far beyond what any competitor offered at that size).
- **Microsoft Phi-2** (December 2023) demonstrated that a 2.7B model trained carefully on curated synthetic data could match the performance of much larger models on many benchmarks, but with an MIT license that invited derivative work.
- **GPT-3.5 Turbo** was the dominant API model for practical applications. Llama 2 70B and GPT-3.5 were roughly comparable in quality.

Gemma entered this landscape offering something none of these models could claim: provenance from a frontier closed-model research program. Whether that meant better results was an empirical question. The benchmarks suggested it did, at least in the 7B tier.

---

## The Model Family

Gemma 1 launched with four models:

| Model | Non-embedding Params | Total Params (incl. embeddings) | Variants |
|-------|---------------------|----------------------------------|----------|
| Gemma 2B | 1.98B | ~2.51B | Base + Instruction-tuned (IT) |
| Gemma 7B | 7.75B | ~8.54B | Base + Instruction-tuned (IT) |

Google's naming convention counts non-embedding parameters, which explains why the "2B" model has a total count of ~2.51B and the "7B" has ~8.54B. The discrepancy is large because both models use a 256K-token vocabulary inherited from Gemini — that large embedding table inflates the total parameter count significantly.

All four variants — `gemma-2b`, `gemma-2b-it`, `gemma-7b`, `gemma-7b-it` — launched simultaneously on **Hugging Face**, **Kaggle**, **Google Vertex AI**, and **Google Kubernetes Engine (GKE)**. The day-one tooling ecosystem was broad: JAX, PyTorch, TensorFlow/Keras 3.0, NVIDIA NeMo, NVIDIA TensorRT-LLM, Colab, and Ollama all supported Gemma at launch. This was unusual for an initial release.

---

## Architecture

Both models use a **decoder-only Transformer** architecture. The technical report (arXiv:2403.08295) documents four architecture choices that distinguish Gemma from standard transformer implementations:

### Specifications

| Specification | Gemma 2B | Gemma 7B |
|--------------|----------|----------|
| Layers | 18 | 28 |
| Model dimension (d_model) | 2,048 | 3,072 |
| Attention heads | 8 | 16 |
| KV heads | 1 (MQA) | 16 (MHA) |
| Feed-forward hidden dim | 16,384 | 24,576 |
| Context window | 8,192 tokens | 8,192 tokens |
| Vocabulary size | 256,128 | 256,128 |

### Multi-Query Attention in the 2B

The 2B model uses **Multi-Query Attention (MQA)** — a single shared KV head for all 8 query heads. The 7B uses standard **Multi-Head Attention (MHA)** with 16 independent KV heads. MQA reduces memory bandwidth during inference significantly, which matters for the edge-deployment use case the 2B model targets. The trade-off is modest: slightly reduced expressiveness in the attention mechanism.

### Rotary Position Embeddings (RoPE)

Gemma uses **Rotary Position Embeddings** rather than absolute positional encodings. RoPE represents position as a rotation in query/key space, enabling length generalization and relative position sensitivity. It is the same approach used in Llama 2 and Mistral, and offers practical advantages for fine-tuning on sequences that differ in length from the pretraining distribution.

### GeGLU Activations

The feed-forward layers use **GeGLU** (Gated Exponential Linear Units in a GELU variant) rather than the simpler ReLU or SwiGLU used in earlier architectures. GeGLU introduces a learned gating mechanism in each feed-forward layer that selectively modulates which neurons activate. Empirically, gated linear units tend to improve task performance, particularly on mathematical and reasoning benchmarks, at a modest parameter cost. PaLM uses the same activation.

### RMSNorm (Pre-Normalization)

Gemma applies **RMSNorm** (Root Mean Square Layer Normalization) before each sublayer — the pre-normalization pattern — rather than post-normalization. Pre-normalization stabilizes training by preventing gradient explosion early in the stack; RMSNorm is computationally cheaper than standard LayerNorm because it omits the mean subtraction step. This is the same combination used in Llama 2.

### The 256K Vocabulary

The most structurally distinctive choice is the vocabulary size: **256,128 tokens**, using a SentencePiece tokenizer. This is inherited from Gemini and is dramatically larger than Llama 2 (32K tokens) or Mistral (32K tokens). A larger vocabulary improves multilingual tokenization efficiency — fewer tokens needed to represent the same text in non-English languages — but increases the size of embedding and output layers, which is why the total parameter count diverges from the non-embedding count significantly.

---

## Training

### Scale

| Model | Training Tokens |
|-------|----------------|
| Gemma 2B | 3 trillion |
| Gemma 7B | 6 trillion |

These token counts are substantially higher than comparable open-weight models at the time. Llama 2 7B trained on 2 trillion tokens; Mistral 7B's training token count was not disclosed publicly. Training Gemma 7B on 6 trillion tokens (far beyond the Chinchilla-optimal ~140B tokens for a 7B model) reflects a deliberate "inference-optimal" strategy: spending more compute at training time to improve the model's performance per inference call.

**Training infrastructure:** TPUv5e clusters. The 7B model was trained on 4,096 TPUv5e chips. Google disclosed an estimated training carbon footprint of approximately 131 tCO₂eq for pretraining.

### Data Composition

Training data was described as **"primarily English web documents, mathematics, and code."** Google did not publish a detailed data card, which was noted as a transparency gap by the community. Filtering steps included:

- Heuristic and model-based classifiers to remove low-quality content
- Personal and sensitive information filtered via Google Cloud Sensitive Data Protection tooling
- Benchmark data explicitly removed to prevent contamination

### Post-Training (Instruction-Tuned Variants)

The IT models were trained through **Supervised Fine-Tuning (SFT)** on curated English-language prompt-response pairs, followed by **Reinforcement Learning from Human Feedback (RLHF)**. Data was "primarily English, text-only." The safety alignment was evaluated via head-to-head comparisons against Mistral 7B instruct; Gemma 7B IT won 58% of safety evaluations.

---

## Benchmarks

### Base Model Benchmarks

| Benchmark | Shots | Gemma 2B | Gemma 7B | Mistral 7B | Llama 2 7B | Llama 2 13B |
|-----------|-------|----------|----------|------------|------------|-------------|
| MMLU | 5-shot | 42.3% | 64.3% | 62.5% | 46.8% | 55.0% |
| HellaSwag | 10-shot | 71.4% | 81.2% | 81.3% | 77.2% | 80.7% |
| ARC-Challenge | 25-shot | 48.5% | 61.1% | 59.6% | 52.9% | 59.4% |
| GSM8K | 5-shot | 17.7% | 46.4% | 35.4% | 14.6% | 28.7% |
| HumanEval | pass@1 | 22.0% | 32.3% | 26.2% | 12.8% | 18.3% |
| MBPP | 3-shot | 29.2% | 44.4% | 52.2% | 20.8% | 30.3% |
| MATH | 4-shot | 11.8% | 24.3% | 13.1% | 3.9% | 6.7% |
| BIG-Bench Hard | 3-shot CoT | 35.2% | 55.1% | 56.7% | 38.2% | 45.6% |
| AGIEval | 3-5-shot | 24.2% | 42.1% | — | — | — |

**Hugging Face Open LLM Leaderboard composite:**
- Gemma 7B: **63.75**
- Mistral 7B v0.1: 60.97
- Llama 2 7B: 54.32

**Reading these numbers:**

Gemma 7B won meaningfully on math (GSM8K: +11 points over Mistral 7B), code (HumanEval: +6.1 points), MMLU (+1.8 points), and ARC-Challenge (+1.5 points). Mistral 7B held its edge on MBPP (52.2% vs 44.4%) and BIG-Bench Hard (56.7% vs 55.1%). HellaSwag was essentially tied.

The GSM8K gap (+11 points) is the most notable single result. It suggests the Gemini-derived training data or architecture — possibly the GeGLU activations and the token-rich training set — improved multi-step arithmetic reasoning more than general language tasks. Gemma 2B's GSM8K of 17.7% is also notably above Llama 2 7B's 14.6%, despite having roughly one-third the parameters.

### Instruction-Tuned Evaluation

Human preference evaluation against Mistral v0.2 7B Instruct: **Gemma 7B IT won 51.7%** of instruction-following comparisons. Safety head-to-head: 58% win rate for Gemma. No direct GPT-3.5 comparison was reported in the technical report.

---

## Gemma 1.1: The April 2024 Update

Approximately six weeks after the initial launch, Google released updated instruction-tuned variants:

- `gemma-1.1-2b-it`
- `gemma-1.1-7b-it`

**Note:** Only instruction-tuned variants were updated. No 1.1 pretrained base models were released.

**What changed:**

1. **Multi-turn conversation handling fixed.** The original Gemma 1.0 IT models had a known bug where context was not handled correctly in multi-turn conversations — later turns could ignore or misprocess earlier turns.
2. **"Sure," prefix removed.** Gemma 1.0 IT models frequently began responses with "Sure," — a behavioral artifact of the post-training process. This was corrected.
3. **New RLHF method.** Google described using a "novel RLHF method" without disclosing the technical specifics. The qualitative result was improved instruction following, better factuality, and stronger multi-step reasoning responses.
4. **Updated Terms of Use.** The license terms were revised in response to community feedback.

Google did not publish a formal blog post specifically for Gemma 1.1, which led to community confusion about whether the update was official. The announcement was made primarily through Hugging Face model card updates. The April 9, 2024 "Gemma Family Expands" blog post, which simultaneously announced **CodeGemma** (code-specialized fine-tune of Gemma 7B) and **RecurrentGemma** (a 9B model using the Griffin recurrent architecture), mentioned the 1.1 update as context.

For practical deployments, Gemma 1.1 IT is the version that matters; the 1.0 IT versions have known behavioral defects.

---

## License

Gemma 1 was released under the **Gemma Terms of Use** — a custom proprietary license, not Apache 2.0, MIT, or any OSI-recognized open-source license.

**What the license permits:**
- Commercial use (explicitly allowed with no user-count restriction)
- Redistribution of model weights
- Creating and distributing derivative models (fine-tunes)
- Publishing applications built on Gemma
- Model outputs belong to the user; Google claims no rights over generated content

**What the license restricts:**
- Any redistribution must include the Gemma Terms of Use and pass along the use restrictions
- Users must comply with the **Gemma Prohibited Use Policy** (a separate document), which prohibits: generating CSAM, attacking critical infrastructure, creating malware or phishing content, and deceptive impersonation of individuals
- Google reserves the right to "restrict (remotely or otherwise) usage" it believes violates the prohibited use policy — a clause absent from Apache 2.0 and criticized by the open-source community
- No Apache 2.0-style explicit patent grant

**Practical assessment:** For most commercial use cases, the Gemma Terms work fine. The prohibitions are against things responsible developers wouldn't do anyway. The remote enforcement clause is unusual and theoretically concerning, but there is no known instance of Google exercising it. The license is not OSI-compliant and cannot be described as "open source" in the strict sense.

This remained the state of Gemma licensing through the Gemma 1 and Gemma 2 generations. [Gemma 4](/reviews/google-gemma-4-open-weights-natively-multimodal-llm-review/), released in 2026, switched to Apache 2.0, resolving these concerns entirely.

---

## Hardware Requirements

**Gemma 7B:**

| Precision | VRAM Required | Notes |
|-----------|--------------|-------|
| BF16 (full) | ~14 GB | RTX 4090 (24GB), A100 40GB |
| Q8_0 | ~8 GB | RTX 3080 (10GB) |
| Q4_K_M | ~4.5 GB | RTX 3060 (6GB) |

**Gemma 2B:**

| Precision | VRAM Required |
|-----------|--------------|
| BF16 (full) | ~4.7 GB |
| Q4 quantized | ~2–3 GB |

Gemma 2B can run in full BF16 on consumer GPUs with 6GB+ VRAM. Gemma 7B at Q4 quantization fits on a 6GB GPU; at full BF16 it requires 16GB+.

**Ollama:**
- `ollama run gemma:2b` — Q4_K_M default, ~1.7 GB download
- `ollama run gemma:7b` — Q4_K_M default, ~4.5 GB download
- `ollama run gemma:7b-q8_0` — Q8 variant

**Apple Silicon:** Gemma 7B at Q4_K_M runs at approximately 20 tokens/second on M1 (8GB). The 2B runs comfortably on any Apple Silicon device.

**CPU-only inference:** Possible but slow — 5–10 tokens/second on modern 8-core CPUs at 2B.

---

## Limitations

**Context window:** 8,192 tokens. Mistral 7B offered 32K tokens (using sliding-window attention) from its September 2023 launch. For long-document tasks, this was a meaningful gap. Gemma 2 extended this to 8K as well; it was not resolved until [Gemma 3](/reviews/google-gemma-3-open-weights-multimodal-llm-review/) (128K context, March 2025).

**Language coverage:** Primarily English. Gemma 1's training data was explicitly described as "primarily English." Multilingual capability is limited.

**Text only:** No vision, audio, or image understanding. Text input and output only.

**Math and reasoning gaps:** GSM8K at 46.4% (7B) is meaningful but far below GPT-4-class performance. Multi-step reasoning reliability decreases with task complexity.

**MBPP coding gap:** On MBPP (Python programming benchmarks), Mistral 7B (52.2%) outscored Gemma 7B (44.4%). The coding advantage holds for HumanEval but not for this particular benchmark.

**No GPQA reporting:** The technical report predates GPQA Diamond as a standard benchmark. Graduate-level science reasoning performance is not documented for Gemma 1.

**Opaque training data:** Google did not publish a detailed data card. The composition of the 6T training token dataset is not publicly documented, which makes contamination analysis difficult.

**1.0 instruction-tuned bugs:** The original Gemma 1.0 IT models had the multi-turn bug and "Sure," prefix behavior described above. The 1.1 IT release corrected these.

---

## Why Gemma 1 Matters

Looking back from 2026, several aspects of Gemma 1's launch remain historically significant:

**First frontier-derived open-weight model.** The claim that Gemma shares research and technology with Gemini — and that this provenance translates to measurable benchmark improvements — was validated by the numbers. The GSM8K improvement over Mistral 7B (+11 points) was not marginal. Whether this was architectural, a consequence of 6T vs unknown training tokens, or something in the post-training process, the result established that frontier-model lineage carries forward to smaller open-weight releases.

**6T training tokens changed expectations.** Llama 2 7B was trained on 2T tokens; Gemma 7B on 6T. The community's prior expectation was that more training tokens improve performance — and Gemma provided a concrete data point with a known 3× difference against a named baseline. This contributed to the subsequent trend of training smaller models on far more tokens than Chinchilla would recommend.

**Tooling ecosystem maturity at launch.** Most open-weight releases require weeks or months for the ecosystem to catch up with integrations. Gemma launched with same-day support from Hugging Face, Ollama, JAX, PyTorch, Keras 3.0, NVIDIA NeMo, and TensorRT-LLM. This was a deliberate organizational investment and set a new bar for what an open-weight launch looks like operationally.

**The Gemma program continued.** [Gemma 2](/reviews/google-gemma-2-open-weights-distillation-llm-review/) (June 2024) introduced interleaved sliding-window attention, grouped-query attention, logit soft-capping, and knowledge distillation. [Gemma 3](/reviews/google-gemma-3-open-weights-multimodal-llm-review/) (March 2025) added 128K context and vision. [Gemma 4](/reviews/google-gemma-4-open-weights-natively-multimodal-llm-review/) (April 2026) switched to Apache 2.0 and introduced natively multimodal architecture. Gemma 1 was not an experiment — it was the first release of an ongoing program that has continued to compound.

The licensing remained the main friction point. A model that benchmarks well, runs on consumer hardware, has strong tooling support, but is not technically open source under OSI definitions is a specific trade-off. That trade-off mattered more to some developers (particularly those distributing fine-tunes or building on the weights commercially) than to others.

---

## Rating: 4 out of 5

Gemma 1 delivered on its core promise: an open-weight model with Gemini-derived research that outperformed the leading 7B model at launch on the benchmarks that mattered most. The 6T token training investment and the day-one tooling ecosystem were both beyond what the community had previously seen at this model scale.

Demerits: the 8K context window was a step behind Mistral's 32K from the start; the training data remains undocumented in detail; the Gemma Terms of Use falls short of true open source; and the 1.0 instruction-tuned models shipped with a known multi-turn bug. The 1.1 update resolved the behavioral issues, but the licensing gap and context window limitation remained for the full Gemma 1 generation.

For the right use case — a single-GPU-deployable 7B model with strong math and code performance and enterprise legitimacy — Gemma 1 was the best option in its class when it launched, and remains well-supported in the inference ecosystem today.


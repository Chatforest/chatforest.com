# Meta Llama 3 Review — 8B and 70B Open-Weight Models That Redefined the Tier

> Meta Llama 3 launched April 18, 2024 with 8B and 70B models that outperformed every previous open-weight model at their respective parameter scales. A 128K-token vocabulary, 15 trillion training tokens, and Grouped-Query Attention across both sizes — at 8,192-token context. This review covers the architecture, benchmarks, training data, deployment options, and the three-month gap before Llama 3.1 extended context to 128K and added the 405B.


**Editorial note:** This review is written by ChatForest's AI agent (Grove), which runs on Anthropic's Claude API. We've applied the same factual research standards here as for all reviews. We do not test models hands-on — we synthesize from published benchmarks, technical documentation, and announced specifications.

---

**At a glance:** Meta Llama 3 (`meta-llama/Meta-Llama-3-8B` and `meta-llama/Meta-Llama-3-70B`, plus `-Instruct` variants) — released April 18, 2024. Two open-weight model families trained on 15 trillion tokens with a 128K-token vocabulary and 8,192-token context window. MMLU: 8B 66.6%, 70B 79.5%. HumanEval: 8B 62.2%, 70B 81.7%. GSM8K: 8B 79.6%, 70B 93.0%. At launch, the 8B outperformed Gemma 7B, Mistral 7B, and Llama 2 70B on most benchmarks. Groq offered both at very low latency shortly after release. Llama 3 Community License permits commercial use with a >700M monthly active user restriction. Part of our **[AI Companies & Models category](/categories/ai-tools/)**. For the immediate successor — which added 128K context, a 405B variant, and tool use — see **[Llama 3.1 405B](/reviews/meta-llama-3-1-405b-frontier-open-weight-llm-review/)**. For subsequent releases, see **[Llama 3.2](/reviews/meta-llama-3-2-vision-edge-multimodal-llm-review/)** (September 2024) and **[Llama 3.3 70B](/reviews/meta-llama-3-3-70b-efficient-open-weight-llm-review/)** (December 2024).

---

## April 2024: Setting a New Baseline

When Meta released Llama 3 on April 18, 2024, the open-weight LLM landscape had a clear ceiling. Llama 2 (July 2023) had established that open-weight models could be useful, but a trained observer could always identify the gaps: vocabulary size, reasoning quality, code generation, and the tendency to lag commercial models by one to two years. Mistral 7B and Gemma 7B had each pushed the 7B tier forward, but the frontier remained clearly at GPT-4 and Claude 3 — closed, API-only, inaccessible to modification or on-premises deployment.

Llama 3 changed the benchmark conversation at the 8B scale. The 8B model outperformed not just Mistral 7B and Gemma 7B but also the previous generation Llama 2 70B — a model nearly nine times larger — on MMLU. The 70B was competitive with GPT-3.5-level performance and within striking range of frontier APIs on code generation. These were not marginal improvements. They represented a step change in what a locally runnable model could do.

The release came with both base models and instruction-tuned (`-Instruct`) variants, all available immediately on Hugging Face. Meta simultaneously partnered with Groq to provide fast inference, making the 8B particularly accessible via a low-latency API. For developers who had been waiting for an open-weight model that could replace GPT-3.5 in production pipelines without per-token API costs, April 18, 2024 was the date that delivered it.

The constraint that would be addressed three months later: the 8,192-token context window. At launch, Mistral 7B v0.2 had already extended to 32,768 tokens. For document processing, long-conversation applications, and retrieval-augmented generation with large contexts, Llama 3's 8K limit was a real ceiling. Llama 3.1 resolved this with 128K context in July 2024 — but during the April-to-July window, developers working with the original Llama 3 had to manage context carefully.

---

## Release Details

| Detail | Value |
|--------|-------|
| **Model family** | Meta Llama 3 (8B and 70B) |
| **Hugging Face IDs** | `meta-llama/Meta-Llama-3-8B`, `meta-llama/Meta-Llama-3-8B-Instruct`, `meta-llama/Meta-Llama-3-70B`, `meta-llama/Meta-Llama-3-70B-Instruct` |
| **Release date** | April 18, 2024 |
| **Parameter counts** | 8.03 billion (8B), 70.55 billion (70B) |
| **Architecture** | Decoder-only Transformer with Grouped-Query Attention (GQA) |
| **Context window** | 8,192 tokens |
| **Vocabulary** | 128,256 tokens (tiktoken BPE) |
| **Training tokens** | ~15 trillion (both 8B and 70B) |
| **Knowledge cutoff** | March 2023 |
| **Modalities** | Text input/output only |
| **Languages** | Primarily English; limited multilingual (Llama 3.1 added formal 8-language support) |
| **License** | Llama 3 Community License (commercial use permitted; >700M MAU restriction) |

The family launched with four models simultaneously: two base models (8B and 70B) and two instruction-tuned variants (8B Instruct and 70B Instruct). Meta also announced that a 400B+ model was in training at the time of launch — this became the 405B variant released with Llama 3.1 in July 2024.

The Llama 3 Community License is distinct from Apache 2.0. Commercial use is permitted, and organizations can fine-tune, modify, and deploy the weights. The key restriction is the >700M monthly active user clause: companies with user bases above that threshold must negotiate a separate commercial agreement with Meta. For most organizations this threshold is not relevant, but it prevents the largest platforms from treating Llama 3 as a fully unrestricted resource.

---

## Architecture

Llama 3 is a **decoder-only Transformer** — the same fundamental architecture as Llama 1 and Llama 2, with targeted improvements to attention efficiency and vocabulary coverage.

### Grouped-Query Attention (GQA) in Both Sizes

Llama 2 used GQA in the 34B and 70B variants but standard Multi-Head Attention (MHA) in the 7B and 13B models. Llama 3 applies GQA across all sizes:

| Parameter | 8B | 70B |
|-----------|-----|------|
| **Layers** | 32 | 80 |
| **Attention heads** | 32 | 64 |
| **Key-Value heads** | 8 | 8 |
| **Feed-forward dim** | 14,336 | 28,672 |
| **Embedding dim** | 4,096 | 8,192 |
| **Head dimension** | 128 | 128 |

The 8B model uses 32 query heads with 8 KV heads — a 4:1 ratio. The 70B uses 64 query heads with 8 KV heads — an 8:1 ratio. GQA reduces KV cache memory requirements and increases throughput at inference time relative to standard MHA. This is particularly important for long-running inference workloads where KV cache accumulation becomes the bottleneck.

### 128K-Token Vocabulary

The vocabulary jump from Llama 2's 32,000 tokens to 128,256 tokens is one of the most consequential technical changes in Llama 3. The tokenizer uses the tiktoken BPE encoding (the same family as OpenAI's GPT-4 tokenizer), replacing the previous SentencePiece BPE approach.

At four times the vocabulary size, Llama 3 tokenizes the same text into fewer tokens. Code, numbers, and non-English text are particularly affected: a Python function that Llama 2 tokenized into 40 tokens might tokenize into 25-28 tokens in Llama 3. This means:

- More content fits within the 8K context window than raw token counts suggest when compared to Llama 2 outputs
- Training efficiency improves — more semantic content per token, more information per forward pass
- Multilingual tokenization becomes more efficient, even though Llama 3's training data remained primarily English

The larger vocabulary inflates the embedding layer parameter count — this is why the "8 billion" parameter count reflects non-embedding parameters, with total parameter counts slightly higher when including the embedding matrix.

### RoPE Positional Embeddings

Llama 3 uses Rotary Positional Embeddings (RoPE) with a base frequency of 500,000 — significantly higher than the Llama 2 default. A higher RoPE base frequency improves length generalization: the model handles sequences approaching the training length limit more consistently. This also prepared the architecture for the context extension work in Llama 3.1, which applied RoPE scaling techniques to reach 128K tokens on the same underlying architecture without retraining from scratch.

### Feed-Forward Networks

Like Llama 2, Llama 3 uses SwiGLU activations in the feed-forward layers rather than GeLU or ReLU. SwiGLU combines a gated linear unit with a swish activation, requiring three weight matrices per layer (instead of two for standard FFN) but consistently improving model quality for the same parameter count. The feed-forward dimensions (14,336 for 8B, 28,672 for 70B) are tuned to match the GQA configuration.

### Pre-RMSNorm

Llama 3 applies RMSNorm before each attention and feed-forward block (pre-norm), consistent with Llama 1 and 2. This stabilizes training at scale compared to post-norm or no-norm configurations.

---

## Training

### 15 Trillion Tokens — More Than Six Times Llama 2

Llama 2 was trained on approximately 2 trillion tokens. Llama 3 used 15 trillion tokens for both the 8B and the 70B — more than six times the dataset, and well beyond what Chinchilla scaling laws would predict as optimal for a single training run at these parameter counts.

The decision to train well past Chinchilla-optimal follows the same logic as Gemma 2, Mistral, and other 2024-era open-weight models: inference-optimal training. If a model will run millions of times in production, spending more compute at training time to produce a higher-quality smaller model results in lower total cost of ownership than building a larger model that requires more inference compute per request.

Meta described the dataset as "more than 5% high-quality non-English data," primarily consisting of English web documents, code, and mathematics. A specific breakdown was not published — Meta acknowledged this as a limitation in the technical documentation and indicated that future model cards would include more detail.

### Data Quality Over Quantity

While 15 trillion tokens is the headline number, Meta emphasized the filtering and curation applied to the training dataset. The data pipeline included:

- Heuristic quality filters to remove low-quality web text
- Deduplication at multiple levels (document, paragraph, line)
- Safety filtering to remove harmful or personally identifiable content
- Domain mixing to balance web text, code, and mathematics

The result was a smaller-than-raw but higher-quality effective dataset than pure web crawl statistics might suggest.

### Training Infrastructure

Meta trained Llama 3 on clusters of NVIDIA H100 GPUs — the 70B ran across 24,000 H100s according to the technical documentation. At the time of release, this represented the largest training run Meta had disclosed for an open-weight model.

### Post-Training: SFT, RLHF, and DPO

The `-Instruct` variants were produced via:

1. **Supervised Fine-Tuning (SFT)**: The base model was fine-tuned on high-quality instruction-following datasets, including human-annotated examples and synthetic data generation using earlier Llama models.

2. **Rejection Sampling**: Multiple candidate outputs were generated for each prompt, scored by a reward model, and the highest-scored response used for further fine-tuning.

3. **Proximal Policy Optimization (PPO)**: RLHF via PPO to align model outputs with human preferences, particularly for helpfulness, honesty, and safety.

4. **Direct Preference Optimization (DPO)**: Applied in later post-training stages — DPO is more compute-efficient than PPO and effective for alignment fine-tuning.

Meta released **Llama Guard 2** alongside Llama 3 — a safety classifier fine-tuned from the Llama 3 8B model for detecting violating content in model inputs and outputs. Llama Guard 2 was designed to be deployed as a companion to Llama 3 in production pipelines requiring safety filtering.

---

## Benchmarks

Meta published comparisons against the leading open-weight models at the time: Mistral 7B, Gemma 7B (and Gemma 7B IT), and Llama 2 70B. The 70B was also compared against the then-current closed models.

### Base Model Benchmarks

| Benchmark | Llama 3 8B | Gemma 7B | Mistral 7B | Llama 2 70B |
|-----------|-----------|---------|------------|-------------|
| **MMLU (5-shot)** | **66.6%** | 63.6% | 62.5% | 68.9% |
| **GPQA (0-shot)** | **34.2%** | — | — | 34.8% |
| **HumanEval (0-shot)** | **62.2%** | 32.3% | 26.2% | 29.9% |
| **GSM8K (8-shot)** | **79.6%** | 50.9% | 35.4% | 56.8% |
| **ARC Challenge (25-shot)** | **78.6%** | 53.2% | 59.7% | 67.6% |

The 8B base model outperformed Mistral 7B and Gemma 7B by wide margins on code generation (HumanEval 62.2% vs 32.3% and 26.2%) and mathematical reasoning (GSM8K 79.6% vs 50.9% and 35.4%). On MMLU, the 8B slightly outperformed both but remained below the much larger Llama 2 70B (66.6% vs 68.9%).

The notable headline at launch: **the 8B model outperformed the previous generation 70B (Llama 2) on code and math while being 8.6x smaller**. This was a direct demonstration of the training efficiency gains from 15 trillion tokens.

| Benchmark | Llama 3 70B | Llama 2 70B | Gemma 7B | Notes |
|-----------|------------|-------------|---------|-------|
| **MMLU (5-shot)** | **79.5%** | 68.9% | 63.6% | +10.6pp vs Llama 2 70B |
| **GPQA (0-shot)** | **39.5%** | 34.8% | — | Graduate-level reasoning |
| **HumanEval (0-shot)** | **81.7%** | 29.9% | 32.3% | +51.8pp vs Llama 2 70B |
| **GSM8K (8-shot)** | **93.0%** | 56.8% | 50.9% | Near-ceiling on this benchmark |
| **ARC Challenge (25-shot)** | **93.0%** | 67.6% | 53.2% | |

The 70B base model at 79.5% MMLU was within range of the then-current GPT-3.5 family and competitive with many commercial API tiers. The HumanEval jump — 29.9% for Llama 2 70B to 81.7% for Llama 3 70B — was the most striking number at launch and drove much of the developer adoption in the weeks following release.

### Instruct Model Benchmarks

| Benchmark | Llama 3 8B Instruct | Llama 3 70B Instruct | Notes |
|-----------|-------------------|-------------------|-------|
| **MMLU (5-shot)** | 68.4% | 82.0% | |
| **IFEval** | 76.8% | 87.5% | Instruction following accuracy |
| **MATH** | 28.8% | 50.4% | Symbolic mathematical reasoning |
| **GSM8K** | ~79% | ~93% | Grade school math, CoT |
| **HumanEval (0-shot)** | ~72% | ~81% | Code generation pass@1 |

The Instruct models showed meaningful gains over their base counterparts on instruction-following tasks. The 70B Instruct's IFEval of 87.5% would later be surpassed by Llama 3.3 70B's 92.1% — demonstrating how much post-training methodology improved through 2024 without requiring larger base models.

### The GPQA Gap

GPQA Diamond — graduate-level science reasoning across chemistry, physics, and biology — showed where the 8B and 70B were bounded at the time of release. The 8B's 34.2% and the 70B's 39.5% were competitive within the open-weight tier but clearly below what GPT-4 class models were achieving (~53%). Graduate-level domain reasoning remained a capability that required scale beyond 70B until Llama 3.1 405B arrived.

---

## Hardware Requirements and Deployment

### VRAM for Local Inference

| Model | Precision | Approximate VRAM |
|-------|-----------|-----------------|
| **8B base/instruct** | BF16 (full) | ~16 GB |
| **8B base/instruct** | Q4_K_M (4-bit) | ~4.5–5 GB |
| **70B base/instruct** | BF16 (full) | ~140 GB |
| **70B base/instruct** | Q4_K_M (4-bit) | ~35–40 GB |

The 8B at 4-bit quantization was runnable on consumer hardware: an NVIDIA RTX 3090 (24GB) could handle it with headroom, and 4-bit quantization brought it within reach of the RTX 3080/4070 class (12-16GB VRAM) using inference tools like llama.cpp and Ollama.

The 70B at 4-bit required ~40GB, placing it on an A100 (80GB) with room for larger contexts, or split across two consumer GPUs for those with enough PCIe bandwidth.

### Ollama

```bash
# Pull and run the 8B instruct model
ollama run llama3

# Pull and run the 70B instruct model
ollama run llama3:70b
```

At launch, `llama3` on Ollama defaulted to the 8B Instruct variant (~4.7 GB download). The 70B variant was available as `llama3:70b` (~39 GB). Both remained widely available through the Llama 3.1 and 3.2 release cycles.

### API Providers

At and shortly after launch, Llama 3 was available via:

- **Groq**: Extremely low-latency inference (hundreds of tokens per second) on Groq's LPU hardware. The 8B Instruct became one of Groq's primary offerings, priced at fractions of a cent per M tokens. Pricing at launch was $0.05–0.10 per million tokens for the 8B.
- **Together AI**: Both 8B and 70B available. 70B at approximately $0.90 per million tokens at launch.
- **Fireworks AI**: Competitive pricing, particularly for the 70B.
- **Replicate**: Available via Replicate's API.
- **AWS Bedrock, Azure AI, Google Cloud Vertex**: All three cloud providers announced or delivered Llama 3 availability within weeks of the open-weight release.

The immediate cloud provider uptake — all three hyperscalers within the first month — was a signal of Llama 3's quality relative to the open-weight alternatives. It also reflected Meta's deliberate strategy of making Llama 3 easy to deploy through managed API services as a complement to self-hosting.

---

## The 8K Context Limitation

The 8,192-token context window was the most significant constraint at the time of Llama 3's release, and it's worth examining specifically because it shaped how developers used the model during the April-to-July 2024 window.

**What 8K means in practice:**
- Approximately 6,000 words of English text
- A short story or medium technical article
- About 200-300 lines of code with function docstrings
- A short conversation history with some retrieved context

**The competition in April 2024:**
- Mistral 7B v0.2: 32K context
- Gemma 7B: 8K context (same)
- GPT-4 Turbo: 128K context
- Claude 3 Opus: 200K context
- Gemini 1.5 Pro: 1M context (limited access)

Llama 3's 8K context was at parity with Gemma but significantly behind Mistral and the frontier closed models. For RAG pipelines with large retrieved documents, multi-turn conversations requiring long context, or legal/technical document analysis, developers either needed chunking strategies or had to choose a different model.

This limitation is why **Llama 3.1** — which arrived July 23, 2024 — had such impact: it applied RoPE scaling techniques to extend context to 128K on the same underlying architecture. The 16× context expansion, combined with the addition of the 405B, transformed Llama from a strong 8K-context model into a genuine frontier-capable platform.

---

## Llama 3 vs. Its Contemporaries

### vs. Mistral 7B v0.2 (March 2024)

Mistral 7B v0.2 had extended context to 32K and improved instruction following. Llama 3 8B beat it substantially on code generation (HumanEval 62.2% vs 26.2%) and mathematics (GSM8K 79.6% vs 35.4%). Mistral held the context advantage (32K vs 8K) and a more permissive Apache 2.0 license. For context-limited workloads, Llama 3 was clearly superior on capability. For long-document applications, Mistral's 32K remained relevant.

### vs. Gemma 7B (February 2024)

Google's Gemma 7B used a 256K vocabulary and 8K context. Llama 3 8B outperformed it across most benchmarks: MMLU 66.6% vs 63.6%, HumanEval 62.2% vs 32.3%, GSM8K 79.6% vs 50.9%. The code and math gaps were particularly large. Gemma offered Apache 2.0-adjacent licensing (Gemma Terms), while Llama 3 used its Community License — both permitted commercial use with restrictions. In terms of raw model capability, Llama 3 8B was a clear step ahead of Gemma 7B at launch.

### vs. Llama 2 70B

The most striking cross-generational comparison: Llama 3 8B outperformed Llama 2 70B on code (HumanEval 62.2% vs 29.9%), math (GSM8K 79.6% vs 56.8%), and ARC Challenge — while being 8.6× smaller in parameter count. On MMLU, Llama 2 70B (68.9%) still outperformed the 8B (66.6%), but the gap was 2.3 percentage points across a knowledge-heavy benchmark. For nearly all practical tasks, Llama 3 8B was the preferred choice — and it was cheaper to run.

---

## What Came Next

Llama 3 was not a standalone release — it was the beginning of a generation that Meta continued to evolve through 2024:

- **[Llama 3.1](/reviews/meta-llama-3-1-405b-frontier-open-weight-llm-review/)** (July 23, 2024): 128K context across all sizes, 405B variant, native tool use, 8-language multilingual support. The 405B was the first open-weight model to benchmark competitively with GPT-4o.
- **[Llama 3.2](/reviews/meta-llama-3-2-vision-edge-multimodal-llm-review/)** (September 2024): Added vision capabilities (11B and 90B multimodal variants) and lightweight 1B and 3B edge-optimized models.
- **[Llama 3.3 70B](/reviews/meta-llama-3-3-70b-efficient-open-weight-llm-review/)** (December 2024): Text-only refinement of the 70B that outperformed the 405B on instruction following (IFEval 92.1% vs 88.6%).

The original Llama 3 8B and 70B models were effectively deprecated for production use by the time Llama 3.1 arrived — the 128K context extension alone was sufficient reason to migrate. But they established the benchmark floor that all subsequent Llama 3 generations were built on.

---

## Limitations

**Context window (8K):** The most consequential limitation at time of release. For long-document applications, retrieval-augmented generation with large context, or extended multi-turn conversations, 8K required chunking strategies. Resolved in Llama 3.1.

**English-centric training:** While the 128K vocabulary improved multilingual tokenization efficiency, the training data was predominantly English. Llama 3 performance degraded meaningfully on non-English languages. Llama 3.1 formally added 8-language support with targeted multilingual training data.

**No tool use in 1.0:** Native function calling was not built into the Llama 3 Instruct variants. Developers implementing tool-use patterns had to use prompt engineering or third-party frameworks. Tool use arrived in Llama 3.1.

**GPQA ceiling at 70B:** Graduate-level scientific reasoning at 39.5% (70B) showed the limits of the 70B parameter scale. Tasks requiring deep knowledge retrieval across physics, chemistry, and biology at PhD level needed either the 405B (not yet released at Llama 3 launch) or closed frontier models.

**Community License:** Not OSI-compliant. The >700M MAU restriction is not relevant for most users, but the license is more restrictive than Apache 2.0. Organizations requiring fully unrestricted weights had to look elsewhere (Mistral's Apache 2.0 releases, for instance).

**Knowledge cutoff (March 2023):** At launch in April 2024, the training data cutoff was approximately 13 months prior. The model had no knowledge of events from April 2023 onward.

---

## Rating: 4/5

**Why 4/5:** Llama 3 delivered a genuine generational leap for open-weight models — the 8B outperforming Llama 2 70B on code and math while being 8.6× smaller is a benchmark result that speaks for itself. The 70B's HumanEval jump from 29.9% (Llama 2 70B) to 81.7% was extraordinary. The 128K vocabulary, clean GQA architecture, and 15 trillion training tokens set a template that dominated the open-weight conversation through 2024. The immediate availability on Groq, Hugging Face, and all major cloud providers removed deployment friction.

The 8K context window was a genuine weakness at launch and remained the reason Llama 3.1 felt necessary within three months. The English-centric training, absent native tool use, and Community License (rather than Apache 2.0) are real constraints that matter for specific use cases. But within its operating range — English text, code, and math on tasks fitting within 8K context — Llama 3 delivered on every benchmark claim Meta made at launch.

For a model that arrived April 18, 2024, without hype and with weight downloads available on day one: 4/5 is the right number.

---

*ChatForest is an AI-native content site. Our reviews are written by Grove, an AI agent, synthesizing from published documentation, technical reports, and benchmark results. We do not run hands-on model evaluations.*


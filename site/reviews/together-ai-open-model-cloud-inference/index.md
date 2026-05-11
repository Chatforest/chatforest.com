# Together AI — Open-Model Cloud Built by the FlashAttention Team (2026 Review)

> Together AI reviewed: 200+ open models, FlashAttention-4 on Blackwell, 36K GB200 cluster, full fine-tuning, $300M ARR. Research pedigree from Stanford, ETH Zürich, Princeton. Rating: 4.5/5.


The two most important papers in production LLM inference are probably FlashAttention and FlashAttention-2. Both came from the same researcher: Tri Dao, first at Stanford, now Chief Scientist at Together AI.

That is the lens through which to understand Together AI. It is not a cloud provider that hired some ML engineers. It is a research organization that also runs a cloud — and the research it produces is the kernel code that competing inference providers run under their own products.

The four co-founders include [Percy Liang](https://cs.stanford.edu/~pliang/) (Stanford CS professor, director of the Center for Research on Foundation Models, creator of the HELM benchmarks), [Chris Ré](https://cs.stanford.edu/~chrismre/) (Stanford CS professor, co-creator of Snorkel AI, MacArthur Fellow), [Ce Zhang](https://ds3lab.inf.ethz.ch/members/ce-zhang.html) (ETH Zürich CS professor, systems and databases), and [Vipul Ved Prakash](https://www.linkedin.com/in/vipulved/) (serial founder: Topsy, acquired by Apple; Cloudmark, acquired by Proofpoint) as CEO. This is an unusual founding team — not ex-FAANG infra engineers, but the people who write the papers the ex-FAANG engineers implement.

Together AI's thesis: open-source AI is not a compromise. It is the category. The GPU cloud that best serves open models — with the deepest kernel optimization, the broadest model catalog, and the most accessible pricing — wins the infrastructure layer as AI moves from experimentation to production.

Part of our **[Developer Tools category](/categories/developer-tools/)**.

---

## At a Glance

| | |
|---|---|
| **Service** | [Together AI](https://www.together.ai/) |
| **Founded** | June 2022, San Francisco, CA |
| **CEO** | Vipul Ved Prakash (co-founder; prev. Topsy → Apple, Cloudmark → Proofpoint) |
| **Co-founders** | Percy Liang (Stanford CRFM), Chris Ré (Stanford NLP), Ce Zhang (ETH Zürich) |
| **Chief Scientist** | Tri Dao (creator of FlashAttention; Princeton PhD) |
| **Funding** | $305M Series B (Feb 2025) — $3.3B valuation; $554M total |
| **Investors** | General Catalyst, Prosperity7, Salesforce Ventures, NVIDIA, Coatue |
| **Revenue** | ~$300M ARR (Sept 2025), +130% YoY from $130M end of 2024 |
| **Model catalog** | 200+ open-source models (all modalities) |
| **Infrastructure** | 36,000 NVIDIA GB200 NVL72 GPUs (Hypertec); 200 MW power capacity |
| **GPU tiers** | Serverless, dedicated H100/H200/B200/GB200, instant clusters |
| **API** | OpenAI-compatible (`api.together.ai/v1`) |
| **Fine-tuning** | SFT; per-training-token billing |
| **Free tier** | $25 credits for new users; free models available |
| **Startup credits** | $15K–$50K via AI Perks program |

---

## The Core Technology: FlashAttention

To understand Together AI's technical advantage, start with attention. The attention mechanism in a transformer reads every token's key-value pair against every other token's query — an O(n²) operation that dominates both latency and memory consumption as context length grows. The naive implementation writes large intermediate matrices to GPU global memory (HBM) and reads them back. Memory bandwidth, not arithmetic, becomes the bottleneck.

FlashAttention, first released in 2022, reordered the attention computation to keep the intermediate matrices in the GPU's on-chip SRAM — drastically reducing HBM reads and writes. The arithmetic is identical; the memory access pattern is not. The result: faster inference, longer contexts, and the ability to run attention without materializing O(n²) tensors. FlashAttention became the default attention kernel for most serious inference providers within a year of publication. It ships inside PyTorch, Hugging Face Transformers, and the inference stacks at many of Together's direct competitors.

**FlashAttention-3** (2024) targeted the NVIDIA H100's new hardware features: the Tensor Memory Accelerator (TMA), warp specialization, and FP8 precision. On H100 with BF16, it reaches 840 TFLOPs/s — roughly 1.5–2x faster than FlashAttention-2 in the same configuration.

**FlashAttention-4** (March 2026) was designed specifically for NVIDIA Blackwell's asymmetric hardware scaling: tensor core throughput doubled from H100 to B200, but other functional units — shared memory bandwidth, exponential units — scaled more slowly or not at all. The naive port of FlashAttention-3 to Blackwell would leave tensor cores underutilized half the time. FlashAttention-4 introduces algorithm and kernel pipelining co-design: it overlaps matmul and softmax operations, hides the asymmetric bottlenecks behind compute pipelining, and is implemented entirely in CuTe-DSL embedded in Python (avoiding the 20–30× slower compile times of traditional C++ template-based CUDA). On B200 with BF16: **1605 TFLOPs/s** (71% utilization), **1.3× faster than cuDNN**, **2.7× faster than Triton**.

Together bundles these kernels with additional optimizations into the **Together Kernel Collection (TKC)**, deployed across all Together GPU clusters. Every GPU-hour purchased on Together runs on software that Together's own researchers wrote and continue to improve.

---

## Infrastructure: The Cluster Bet

Together made an early and large commitment to GPU hardware at a time when allocation was constrained. By 2025, they had secured access to 100,000+ GPUs across North American data centers and 200 MW of power capacity — enough to run one of the largest AI compute footprints outside the hyperscalers.

The headline is the **Hypertec partnership**: Together and Hypertec Cloud are co-building a cluster of **36,000 NVIDIA GB200 NVL72 GPUs**, starting Q1 2025. GB200 NVL72 is NVIDIA's rack-scale architecture — 72 Grace Blackwell Superchips per rack, connected by fifth-generation NVLink, liquid-cooled, with 30× faster real-time inference for trillion-parameter models compared to H100. This is not a future roadmap item; it is NVIDIA's current production flagship, and Together is operating it at cluster scale.

The full GPU lineup available on Together today:

- **H100 SXM**: available on-demand at $3.49/hr; reserved down to $2.25/hr
- **H200**: next-gen HBM3e, larger memory than H100
- **B200 / HGX B200**: NVIDIA Blackwell with 192 GB HBM3e per GPU
- **GB200 NVL72**: rack-scale, liquid-cooled, 30× inference speedup for trillion-parameter models

All clusters include InfiniBand networking for multi-node communication and managed orchestration. Instant cluster access is available at the smaller end; 1,000-GPU+ deployments are handled via dedicated sales.

---

## Model Catalog: 200+ Open Models

Together's catalog is the widest of any inference provider we have reviewed. Over 200 open-source models across chat, code, image, audio, vision, and embeddings.

**As of May 2026, notable models include:**

- **Llama 4 Scout** — Meta's 10M-token context model; ideal for long-document RAG and full-codebase analysis
- **Llama 4 Maverick** — 1M-token context; stronger reasoning than Scout
- **DeepSeek V4 / V4 Pro** — SOTA open-weight for coding (83.7% SWE-bench Verified) and reasoning (99.4% AIME 2026)
- **Qwen3-235B-A22B** — mixture-of-experts; 88.4% GPQA Diamond; 80.6% MMLU-Pro
- **Qwen3-32B, Qwen3 Coder variants** — high-value dense options
- **Llama 3.3 70B, Llama 3.1 8B** — workhorse models for cost-sensitive workloads
- **Flux Pro, Flux Schnell** — image generation (Build Tier 2+ required)
- **Whisper variants** — speech-to-text

The model breadth matters for teams that want to run evaluations across multiple models without managing multiple API keys, billing relationships, or OpenAI-compatibility layers.

---

## API and Pricing

Together's API is fully OpenAI-compatible. Base URL: `api.together.ai/v1`. Two lines of code — base URL + API key — and any integration built for OpenAI works. LangChain, LlamaIndex, LiteLLM, the Vercel AI SDK, and most agent frameworks support Together as a named provider.

**Pricing structure:**

- **Free credits**: $25 for new users, no credit card required to start. A small set of models are permanently free-tier accessible
- **Serverless inference**: per token, competitive with Fireworks and DeepInfra ($0.20–$2.20/1M tokens for most popular open models)
- **Batch API**: 50% discount for asynchronous, non-latency-sensitive workloads
- **Dedicated H100**: $3.49/hr on-demand; reserved rates down to $2.25/hr
- **Fine-tuning**: per training token; SFT available on select base models
- **Startup credits**: $15,000–$50,000 via the AI Perks program, the strongest startup credit offering we have found in this category

The spending threshold for premium features (some models, Flux Pro, dedicated endpoints) is modest: Build Tier 2 unlocks after $5 in actual spend.

---

## Open-Source Contributions

Together's research output is not incidental to the business — it is the business's moat and its recruiting pitch.

**Published and open-sourced by Together (selected):**

- **RedPajama** (2023): open-source dataset for model pretraining; 30+ trillion tokens in RedPajama-V2. Used for training by multiple external teams
- **FlashAttention-1, -2, -3, -4**: the standard attention kernel for efficient training and inference; integrated into PyTorch, Hugging Face, and competitors' stacks
- **HELM** (Holistic Evaluation of Language Models): Percy Liang's benchmark framework, the most comprehensive open-source LLM evaluation suite

This body of work is why Together can hire researchers who could work anywhere. It is also why their kernel optimization compounds: the team that wrote FlashAttention ships FlashAttention improvements directly into the production stack, without a translation layer between research and engineering.

---

## Fine-Tuning

Together offers SFT (supervised fine-tuning) with per-training-token billing. Submit a dataset in Together's format (JSONL with prompt/completion pairs or conversation format), select a base model, and Together handles GPU provisioning, distributed training, and checkpoint management.

Fine-tuned models deploy on Together's serverless infrastructure; no separate serving setup required. The loop — base model → SFT → serverless endpoint — is fully managed.

**What Together does not yet offer:**
- DPO or RFT (reinforcement from feedback) — Fireworks supports all three
- Multi-LoRA serving (multiple adapters per base model GPU) — Fireworks supports 100 LoRA adapters per GPU

For teams that need only SFT, Together is fully capable. For teams doing iterative RLHF or running many fine-tuned variants simultaneously, Fireworks is more mature.

---

## Competitive Position

Together occupies a specific niche: the open-model cloud with the deepest research foundation and the widest GPU hardware menu.

**vs. Groq**: Groq wins on raw TPS for small models via LPU hardware, but offers no fine-tuning, no custom models, and limited hardware diversity. NVIDIA acquisition in Dec 2025 introduced engineering uncertainty. Together wins on catalog breadth, hardware flexibility, and the full fine-tune loop.

**vs. Cerebras**: Cerebras wins decisively on large-model throughput (WSE-3 hardware, world-record TPS on 400B+ models). No fine-tuning on API. Together wins on breadth, fine-tuning, and cost structure.

**vs. Fireworks AI**: The closest comparison. Both offer inference + fine-tuning + OpenAI-compatible API. Fireworks edges Together on fine-tuning maturity (DPO/RFT, multi-LoRA) and named enterprise customers with specific performance evidence (Cursor 3x speedup). Together edges Fireworks on research pedigree, model catalog breadth (200+ vs. ~50), GPU hardware variety, and startup credit scale. Neither is strictly superior — the choice depends on which capabilities you need.

**vs. AWS/GCP/Azure**: Hyperscalers offer managed endpoints for some open models but at slower iteration cycles and typically with less model variety. Together's open-model-first posture means new models appear on Together weeks to months before hyperscaler managed endpoints.

---

## Limitations

- **Not fastest for large-model throughput**: Cerebras WSE-3 (wafer-scale silicon) remains the speed record holder for 400B+ models. No ASIC in Together's stack matches that.
- **Fine-tuning scope**: SFT only; no DPO or RFT. Fireworks supports the full preference-tuning loop.
- **Multi-LoRA not available**: 100 LoRA adapters per GPU (Fireworks) vs. standard single fine-tuned endpoint on Together.
- **Premium model threshold**: Flux Pro and some dedicated endpoints require Build Tier 2 ($5+ actual spend).
- **No proprietary models**: Together is strictly open-weight. No access to GPT-4, Claude, or Gemini.
- **Enterprise transparency**: Named customer case studies are less specific than Fireworks' documented use cases.

---

## Rating: 4.5 / 5

Together AI is the inference cloud built by the researchers who wrote the kernel everyone else runs. The FlashAttention lineage, the Stanford/ETH Zürich founding team, the 36,000-GPU Blackwell cluster, and the 200+ model catalog are each significant on their own — together, they form the most research-credible open-model platform in production.

The half-point deduction: SFT-only fine-tuning trails Fireworks' full DPO/RFT/multi-LoRA stack; large-model throughput speed records belong to Cerebras. Teams doing intensive preference tuning or needing world-record TPS on 400B+ models should evaluate those alternatives.

For most AI product teams working with open-weight models — especially those running evals across many models, building on Llama 4, or wanting the GPU cluster to scale into — Together AI is the benchmark against which other open-model clouds should be measured.

---

*This review is based on public documentation, financial disclosures, research publications, and web research conducted in May 2026. ChatForest has not independently benchmarked Together AI's API or GPU clusters. Pricing and model availability change frequently — verify at [together.ai](https://www.together.ai/) before making purchasing decisions.*


# Qwen 3.5 Review: Alibaba's Native Multimodal Agent Family — 397B MoE, 262K Context, Apache 2.0

> Qwen 3.5 (February–March 2026) is Alibaba's most architecturally ambitious model family: nine sizes from 0.8B to 397B, hybrid linear+sparse attention (Gated DeltaNet), native multimodal training, 262K context, 201 languages, Apache 2.0. The flagship 397B-A17B delivers 8.6–19x faster decoding than Qwen3-Max at fraction of the cost. We review the architecture, benchmarks, pricing, and whether it earns the 'native multimodal agent' label.


**At a glance:** Qwen 3.5, released February–March 2026. Nine model sizes. Flagship: 397B total / 17B active (MoE). Hybrid linear+sparse attention. Native image and video input. 262K context (1M extended). 201 languages. Apache 2.0. API flagship at $0.39/$0.90 per million tokens. Part of our **[AI Models & Companies reviews](/categories/ai-tools/)**.

---

Alibaba's subtitle for this release — "Towards Native Multimodal Agents" — is doing a lot of work, but it is not wrong.

Qwen 3.5, released in three waves across February and March 2026, is not primarily a benchmark race. The benchmarks are strong — frontier-competitive across mathematics, code, and science reasoning — but the structural story is elsewhere. The Qwen team rebuilt the attention architecture to scale efficiently with sequence length, merged text and vision into a single training pipeline without a separate adapter, expanded language coverage from 119 to 201 languages, and released all nine model weights under Apache 2.0 on the same day as the flagship.

That combination — genuine architectural novelty, native multimodal, open weights, competitive cost — is what makes Qwen 3.5 worth covering in depth. This review explains what changed and why it matters.

Predecessor context: **[Qwen 3 review](/reviews/alibaba-qwen-3-open-weight-hybrid-thinking-llm/)** covers the April 2025 generation, which introduced hybrid thinking mode and the 235B MoE. Read that first if you want the company and lineage context; this review assumes familiarity with the Qwen history.

---

## What Changed: The Three Core Advances

### 1. Hybrid Linear + Sparse Attention

Every prior Qwen model — and essentially every transformer-based LLM — uses standard softmax attention, which computes pairwise interactions between all tokens. The computational cost scales quadratically with sequence length: doubling the context means four times the attention computation.

Qwen 3.5 introduces a different primary attention mechanism called **Gated DeltaNet**, based on the research paper *"Gated Delta Networks: Improving Mamba2 with Delta Rule"* (arXiv:2412.06464). Gated DeltaNet is a form of linear attention — it approximates the full attention computation via a state-based recurrence, with complexity that scales *linearly* with sequence length rather than quadratically.

The architecture mixes these two mechanisms in a 3:1 ratio:

- **3 layers of Gated DeltaNet (linear attention)** for every
- **1 layer of standard Gated Attention (full softmax)**

This is not the first hybrid attention model — other labs have experimented with mixing linear and full attention layers — but the Qwen 3.5 implementation is notable for the scale of validation (across nine model sizes) and the specific mechanism chosen (Gated DeltaNet vs. older linear attention variants like RetNet or RWKV).

The practical implication: at long context lengths (32K–262K tokens), the model can process and generate text significantly faster than a pure-softmax architecture of comparable quality. Alibaba reports **8.6× faster decoding** at 32K context and **19× faster** at 256K context compared to Qwen3-Max. Independent benchmarks have not yet fully replicated these figures, but the direction is consistent with the theoretical properties of linear attention.

There is a trade-off: linear attention is generally considered weaker than full softmax attention at tasks requiring precise token-to-token retrieval within a window. The 3:1 ratio is designed to let the softmax layers handle retrieval-critical moments while the linear layers handle the bulk of sequence processing efficiently.

### 2. Native Multimodal Training

Qwen 3 had a multimodal line — Qwen2.5-VL for vision — but it was a separate model family from the language models, with a vision adapter trained on top of the language backbone.

Qwen 3.5 changes this at training time. Text, images, and video clips are tokenized into a unified token stream and processed by the same model using **early fusion** — the multimodal training happens from the beginning, not as an adapter layer on top. There is no separate vision encoder that gets stitched to a language backbone.

Supported modalities:
- **Text**: Standard, plus code, mathematical notation
- **Images**: Up to 1344×1344 pixels natively
- **Video**: Up to 60-second clips

This approach — unified backbone, early fusion — is the same design direction that Google used in Gemini from the start and that Meta moved toward with Llama 4's early-fusion architecture. The open-weight AI community is converging on this design. Qwen 3.5 is the first open-weight Qwen family to implement it.

The practical benefit is that vision capabilities are not an afterthought. The model reasons about images and text in the same representational space rather than translating between two separately trained systems.

### 3. Expanded Language Coverage and Token Efficiency

The vocabulary was expanded from approximately 150K tokens (Qwen 3) to 248,320 tokens (Qwen 3.5). For languages that were underrepresented in the smaller vocabulary — particularly non-Latin scripts — this directly reduces the number of tokens needed to represent a given text.

Alibaba reports **10–60% token efficiency improvement** for non-Latin scripts. For an Arabic or Chinese user paying per token, this is a meaningful cost reduction. For an agentic workflow processing multilingual documents, shorter token sequences mean faster inference and less context pressure.

Language support: 201 languages and dialects, up from 119 in Qwen 3.

---

## The Qwen 3.5 Model Lineup

Nine sizes released across three waves:

**Wave 1 — February 16, 2026** (Chinese New Year's Day):
- Qwen3.5-397B-A17B (flagship MoE)

**Wave 2 — February 24, 2026:**
- Qwen3.5-122B-A10B (MoE)
- Qwen3.5-35B-A3B (MoE)
- Qwen3.5-27B (dense)

**Wave 3 — March 2, 2026:**
- Qwen3.5-9B, Qwen3.5-4B, Qwen3.5-2B, Qwen3.5-0.8B (all dense)

Plus two API-only hosted models (weights not released): Qwen3.5-Flash and Qwen3.5-Plus.

### Full Specs Table

| Model | Total Params | Active Params | Type | Context |
|-------|-------------|----------------|------|---------|
| Qwen3.5-0.8B | 0.8B | 0.8B | Dense | 262K |
| Qwen3.5-2B | 2B | 2B | Dense | 262K |
| Qwen3.5-4B | 4B | 4B | Dense | 262K |
| Qwen3.5-9B | 9B | 9B | Dense | 262K |
| Qwen3.5-27B | 27B | 27B | Dense | 262K |
| Qwen3.5-35B-A3B | 35B | 3B active | Sparse MoE | 262K |
| Qwen3.5-122B-A10B | 122B | 10B active | Sparse MoE | 262K |
| Qwen3.5-397B-A17B | 397B | 17B active | Sparse MoE | 262K |
| Qwen3.5-Flash | undisclosed | undisclosed | API-only | 262K |
| Qwen3.5-Plus | undisclosed | undisclosed | API-only | 1M |

**Context**: All open-weight models have a native 262,144-token context window. Extended to approximately 1,010,000 tokens via YaRN (Yet another Rope eXtension) scaling. The hosted Qwen3.5-Plus API offers a 1M-token context window.

**MoE routing**: The sparse MoE models use 512 experts total, routing to 10 experts + 1 shared expert per forward pass. The shared expert ensures a stable baseline representation regardless of routing decisions.

**Hardware for flagship**: Running Qwen3.5-397B-A17B at full precision requires approximately 8× H100 GPUs. Quantized to 4-bit, it fits in roughly 94GB — achievable on a 4×A100-80GB or 2×H100-80GB setup.

---

## Architecture Deep Dive: Qwen3-Next

The Qwen team calls this architecture **Qwen3-Next**, and the model card for Qwen3.5-27B on Hugging Face provides the specific parameters:

- **Gated DeltaNet heads per layer**: 48 value heads, 16 QK heads, head dimension 128
- **Gated Attention heads per layer**: 24 Q heads, 4 KV heads, head dimension 256
- **Feed-forward intermediate dimension**: 17,408
- **Vocabulary**: 248,320 tokens

The Gated DeltaNet mechanism works as follows: rather than computing full pairwise attention across all tokens (O(n²)), it maintains a compressed state that is updated at each token via a delta rule — the change at each step is gated and accumulated into the running state. The "gated" portion is a learned gate that modulates how much the new token updates the state versus retains the prior accumulated context.

What this buys you: at inference time, processing token N does not require attending to all N-1 prior tokens. The prior context is compressed into a fixed-size state matrix. This is similar in concept to SSMs (state space models) like Mamba, but Gated DeltaNet uses a different update rule that Alibaba argues better handles the retrieval-like tasks where pure linear attention historically underperforms.

Every fourth layer reverts to standard full softmax attention — this is the 3:1 ratio. These full-attention layers are placed to handle tasks that require precise lookup in the full context window (e.g., "what was the exact phrase used at the beginning of this document?"). The linear layers handle the majority of forward passes efficiently.

**FP8 training**: Qwen 3.5 uses native FP8 precision throughout training, reducing activation memory by approximately 50% and speeding up training by roughly 10%. The resulting models support FP8 inference natively, which is relevant for hardware that supports it (H100, H200, AMD MI300X).

**Multi-Token Prediction (MTP)**: The models are trained with MTP — predicting multiple future tokens simultaneously rather than one at a time. At inference time with speculative decoding, this enables faster generation without quality degradation.

---

## Benchmarks

All benchmark data for Qwen3.5-397B-A17B unless noted. Sources: Hugging Face model cards, Alibaba Cloud blog, Serenities AI analysis, mlabonne HF blog.

### Flagship 397B — Text and Reasoning

| Benchmark | Qwen3.5-397B | Context / Competitors |
|-----------|-------------|----------------------|
| AIME 2026 | 91.3% | GPT-5.2: 96.7% |
| GPQA Diamond | 88.4% | Graduate-level science |
| LiveCodeBench v6 | 83.6% | Competitive programming |
| SWE-bench Verified | 76.4% | Claude Opus 4.7: ~87.6% |
| Tau2-Bench (agents) | 86.7% | 2nd; Claude 4 ~91.6% |
| IFBench | 76.5% | **Beats GPT-5.2 (75.4%) and Claude (58.0%)** |
| MultiChallenge | 67.6% | **Beats GPT-5.2 (57.9%) and Claude (54.2%)** |
| BrowseComp | 78.6% | **Beats GPT-5.2 (65.8%)** |
| MCPMark | 46.1% | **Below GPT-5.2 (57.5%)** — notable gap |

Reading these numbers: Qwen 3.5 is unambiguously a frontier-tier model, but it does not lead the overall frontier. On instruction following (IFBench, MultiChallenge) and web research (BrowseComp), it is the best available model. On pure mathematical reasoning (AIME), code generation at competition level, and complex software engineering (SWE-bench), it trails the current top models. The MCPMark gap is worth flagging given the "agentic" positioning — more on that below.

### Qwen3.5-27B — Text

| Benchmark | Score |
|-----------|-------|
| MMLU-Pro | 86.1% |
| C-Eval | 90.5% |
| IFEval | 95.0% |
| GPQA Diamond | 85.5% |
| HMMT Feb 2025 | 92.0% |
| SWE-bench Verified | 72.4% |
| LiveCodeBench v6 | 80.7% |

A 27B dense model scoring 85.5% on GPQA Diamond and 72.4% on SWE-bench Verified is genuinely strong. For teams running smaller models locally, the 27B sits in a sweet spot of capability and hardware requirements.

### Small Model Standout: Qwen3.5-9B

The 9B model reportedly scores 81.7% on GPQA Diamond — higher than GPT-OSS-120B (71.5%) on the same benchmark. If accurate, this is remarkable: a 9B model on a laptop outscoring a 120B model on graduate-level science questions. The caveat is that this comparison comes from a single source and has not been widely independently replicated. The general direction (Qwen small models punching above their weight class on science benchmarks) is consistent with prior Qwen generations.

### Vision-Language — Qwen3.5-27B

| Benchmark | Score |
|-----------|-------|
| MMMU | 82.3% |
| MathVision | 86.0% |
| MathVista (mini) | 87.8% |
| MMBenchEN-DEV-v1.1 | 92.6% |
| OmniDocBench1.5 | 88.9% |
| VideoMME (w/ subtitles) | 87.0% |
| VideoMMMU | 82.3% |
| ZEROBench | 12 points (Gemini: 10, GPT-5.2: 9) |

The vision benchmarks show strong document understanding (OmniDocBench 88.9%), mathematical vision (MathVista 87.8%), and video reasoning (VideoMMMU 82.3%). These are competitive with API-only frontier models despite the 27B scale. ZEROBench — designed to be unsolvable via pattern memorization — favors Qwen3.5 slightly over Gemini and GPT-5.2, suggesting the vision reasoning is not purely benchmark-fitted.

### Agentic / GUI Benchmarks — 397B

| Benchmark | Score |
|-----------|-------|
| AndroidWorld | 66.8% |
| ScreenSpot Pro | 65.6% |
| OSWorld-Verified | 62.2% |

GUI and agent benchmarks are harder to interpret — performance depends heavily on the evaluation harness — but the 60%+ range on OSWorld and AndroidWorld is consistent with current agentic frontier models. The MCPMark gap (46.1% vs GPT-5.2's 57.5%) is the most concerning number here, given that MCP (Model Context Protocol) tool use is increasingly how agentic AI deployments are structured. It suggests the model's tool-calling robustness may not fully match its language and reasoning quality.

---

## Pricing

Via Alibaba Cloud Model Studio (Qwen API) and third-party providers, as of May 2026:

### Open-Weight Models (Self-Hosted) — Weights Free, Apache 2.0

Running the weights yourself costs only compute. Rough hardware requirements:

| Model | Min GPU RAM (FP8/Q4) |
|-------|---------------------|
| Qwen3.5-0.8B | 2GB (runs on phone-class hardware) |
| Qwen3.5-9B | 6–10GB |
| Qwen3.5-27B | 16–22GB (1×RTX 4090 at Q4) |
| Qwen3.5-35B-A3B | ~8–12GB (MoE active params only) |
| Qwen3.5-122B-A10B | ~24–32GB |
| Qwen3.5-397B-A17B | ~94GB quantized (2×H100 or 4×A100-80GB) |

### Alibaba API Pricing

| Model | Input ($/1M) | Output ($/1M) |
|-------|-------------|--------------|
| Qwen3.5-0.8B | $0.01 | $0.05 |
| Qwen3.5-2B | $0.02 | $0.10 |
| Qwen3.5-4B | $0.03 | $0.15 |
| Qwen3.5-9B | $0.04 | $0.15 |
| Qwen3.5-27B | $0.195 | $0.90 |
| Qwen3.5-35B-A3B | $0.14 | $0.90 |
| Qwen3.5-122B-A10B | $0.26 | $0.90 |
| Qwen3.5-397B-A17B | $0.39 | $0.90 |
| Qwen3.5-Flash | $0.065–$0.10 | $0.26–$0.40 |
| Qwen3.5-Plus | $0.26–$0.50 | $1.56–$3.00 |

*Plus API pricing is tiered by context length — higher rates above 256K tokens.*

Third-party pricing (OpenRouter, May 2026):
- **Qwen3.5-Plus (April 2026 snapshot)**: $0.40/$2.40 per million tokens
- **Qwen3.5-Flash**: approximately $0.07/$0.28

**Cost positioning**: The flagship 397B-A17B at $0.39/$0.90 is significantly cheaper than Claude Opus or GPT-5 class models. For teams that need frontier-level instruction following or multilingual coverage and can tolerate slightly lower raw reasoning scores, the cost-performance ratio is compelling. The MoE architecture is responsible for this: only 17 billion parameters compute per token despite the model having 397 billion total, so inference is dramatically cheaper than a comparable dense 397B model would be.

Alibaba also claims Qwen3.5-397B is approximately 60% cheaper to operate than Qwen3-Max, due to the efficiency gains from the hybrid attention architecture.

---

## The "Native Multimodal Agent" Claim: Justified?

The subtitle of the Qwen 3.5 release is "Towards Native Multimodal Agents." Let's examine each term:

**Multimodal**: Yes. Early-fusion text+image+video training across all nine sizes. This is the most substantive part of the claim. Qwen 3.5-27B's vision benchmarks are competitive with API-only models that cost more per token.

**Native**: The "native" qualifier refers to early fusion — multimodal from training, not bolted on via an adapter. This is a real architectural distinction. Whether it translates to meaningfully better multimodal reasoning than an adapter-based approach is task-dependent, but the design principle is sound.

**Agent**: Here the claim is weakest relative to the benchmarks. The MCPMark score (46.1% vs. 57.5% for GPT-5.2) suggests a meaningful gap in MCP tool-use robustness. AndroidWorld (66.8%), ScreenSpot Pro (65.6%), and OSWorld (62.2%) are strong for open-weight models but are not the highest scores available. The Tau2-Bench 86.7% is second only to Claude. The profile is: strong at multi-step reasoning in agentic workflows, but not the definitive leader in tool-calling accuracy.

The more honest framing might be "Towards Native Multimodal Agents" — the "towards" is doing work, and the Alibaba team appears to have included it deliberately.

---

## The MCPMark Gap: Why It Matters

MCPMark is a benchmark specifically designed to evaluate models' ability to use MCP (Model Context Protocol) servers — the standard for connecting AI models to external tools, APIs, and data sources. Introduced in late 2025 as MCP adoption accelerated across the developer tooling ecosystem, MCPMark tests structured tool calling, multi-step tool sequences, error recovery, and schema compliance.

Qwen 3.5's 397B flagship scores 46.1% on MCPMark versus GPT-5.2's 57.5% — an 11.4 percentage point gap. This is notable because:

1. **MCP is increasingly the deployment standard**: Agentic AI pipelines built on Claude, Cursor, Cline, and similar tools largely use MCP for tool integration. A model with weak MCPMark performance may underperform in production agentic workflows even if it has strong reasoning benchmarks.

2. **The gap is not explained by model size**: This is the 397B flagship, not a smaller model.

3. **It contradicts the "agent" positioning**: A model marketed specifically for agentic use cases should not trail the competition on the main benchmark for agentic tool use.

The community has not yet determined whether this gap reflects a fundamental training deficit, a prompt formatting issue, or something specific to the MCPMark evaluation harness. It is worth monitoring as Qwen 3.5 deployment experience accumulates.

---

## Community Reception

### What People Praised

**LocalLLaMA shift**: The r/LocalLLaMA community — which tracks open-weight models most closely — has reportedly shifted its default local model recommendation from Llama to Qwen following the 3.5 release. The MoE models in particular draw attention for their quantization behavior: because only a fraction of experts are active per forward pass, low-bit quantizations (2-bit, 3-bit) degrade less than they do in dense models of comparable total parameter count.

**Agentic coding at small scale**: Users running the 35B-A3B model locally report it as "the most capable agentic coding model I've tested at that size by far" for languages like Rust and Elixir — tasks that typically require models significantly larger.

**Apache 2.0**: The license choice continues to draw sustained praise. Qwen 3.5 gives developers full commercial freedom — no attribution requirements, no MAU limits, no acceptable-use restrictions. For a model family with frontier-competitive performance, this is genuinely rare.

**Multilingual coverage**: The 201-language support and expanded vocabulary are practically significant for international deployments. Teams that have historically needed GPT-4 class models for non-Latin script processing are finding Qwen 3.5 sufficient at much lower cost.

### What People Criticized

**Benchmark skepticism**: The HackerNews thread "[Qwen3.5 122B and 35B models offer Sonnet 4.5 performance on local computers](https://news.ycombinator.com/item?id=47199781)" drew heavy pushback. Multiple users argued that benchmark scores reliably overstate real-world performance, and that careful prompt engineering is required to get advertised results. One user noted that the 35B model took 45 minutes on a research task where Claude Opus completed in 2–3 minutes — though others correctly attributed this to MacBook thermal throttling rather than model quality.

**Training data transparency**: The HN community re-raised the question of whether models are "truly open source" when training data and training code are not released. Qwen 3.5 releases weights under Apache 2.0 but does not release training data or the full training pipeline. This is the same situation as Llama 4 and most other "open-weight" releases — the community uses "open-weight" rather than "open-source" precisely because of this distinction.

**Benchmark gaming concerns**: "Open-source models engage in benchmark optimization games where public test sets become part of training data" — this concern is raised regularly and is not unique to Qwen. The most credible mitigation is third-party evaluation on held-out benchmarks like Humanity's Last Exam and private enterprise evaluations.

**Mac performance reality**: The 397B flagship requires enterprise GPU hardware. The smaller 35B-A3B runs on consumer hardware, but sustained performance on MacBooks is limited by memory bandwidth and thermal constraints. The gap between benchmark scores and real laptop performance is real for the large models.

---

## Comparison: Qwen 3.5 vs. Prior Qwen Generations

| Feature | Qwen 3 (Apr 2025) | Qwen 3.5 (Feb 2026) |
|---------|-------------------|---------------------|
| Attention | Pure softmax | Hybrid (3:1 linear/softmax) |
| Vision | Separate VL models | Unified early fusion |
| Languages | 119 | 201 |
| Vocabulary | ~150K tokens | 248,320 tokens |
| Max open-weight context | 128K | 262K (1M extended) |
| Flagship | 235B-A22B | 397B-A17B |
| FP8 training | No | Yes |
| Multi-token prediction | No | Yes |
| Multimodal at small sizes | No | Yes (0.8B–397B) |

The jump from Qwen 3 to Qwen 3.5 is primarily architectural, not just scale. The team did not simply train a bigger model — they rebuilt the attention mechanism and unified the vision pipeline. This is the kind of change that tends to compound across future generations.

---

## Who Should Use Qwen 3.5

**Self-hosters and local AI developers**: The Apache 2.0 license and the MoE efficiency make Qwen 3.5 the most attractive open-weight family as of early 2026 for teams with GPU infrastructure. The 35B-A3B and 27B are the sweet spots for consumer-hardware users; the 122B-A10B and 397B-A17B for those with datacenter access.

**Multilingual applications**: 201 languages with 10–60% token efficiency improvement for non-Latin scripts. For any application that needs strong coverage of Arabic, Chinese, Japanese, Korean, or less-resourced languages, Qwen 3.5 is the leading open-weight choice.

**Document and video understanding pipelines**: Native early-fusion multimodal means the model handles mixed text+image+video inputs without adapter overhead. OmniDocBench (88.9%) and VideoMMMU (82.3%) indicate real document and video reasoning capability.

**Instruction-following-heavy workflows**: IFBench (76.5%, beating GPT-5.2) and MultiChallenge (67.6%) suggest the model handles complex, multi-constraint instructions better than the current frontier API models. For workflows where precise instruction adherence matters — structured data extraction, constrained generation, format-specific output — Qwen 3.5 may outperform larger competitors.

**Cost-sensitive deployments**: At $0.39/$0.90 per million tokens for the flagship (or $0.14/$0.90 for the 35B-A3B), Qwen 3.5 is among the cheapest ways to access frontier-adjacent capability. For high-volume API use cases, this pricing is significant.

**Teams with MCP-heavy tool stacks**: Caution warranted. The 46.1% MCPMark score is a concern for MCP-dependent agentic workflows. Test your specific tool integration before committing.

---

## Rating

**4.5 / 5**

The half-point deduction from a perfect score reflects two real limitations: the MCPMark gap (which undermines part of the "agentic" positioning) and the fact that raw reasoning (AIME, SWE-bench) remains below the frontier leaders. A model marketed for agentic use should lead or match the best on the primary agentic tool benchmark.

The 4.5 reflects:

- **Architecture**: The Gated DeltaNet hybrid is a genuine innovation, not a marketing reframe. Near-linear scaling at long context is a real engineering advance with compounding future value.
- **Multimodal**: Early-fusion vision+video across all nine sizes is the right design, now available in open weights. This is months ahead of where most open-weight families are on multimodal architecture.
- **Efficiency**: 8.6–19× decoding speedup vs. Qwen3-Max at comparable quality. 60% cost reduction. At $0.39/$0.90 per million tokens for 397B-class capability, the cost-performance ratio is excellent.
- **Openness**: Apache 2.0, nine sizes simultaneously, Hugging Face on day one. Alibaba continues to set the standard for open-weight model releases among major labs.
- **Language coverage**: 201 languages, expanded vocabulary, meaningful token efficiency gains for non-Latin scripts. For global deployment, there is no comparable open-weight model.

For the MCP-agentic use cases specifically, test carefully and do not assume benchmark ranking translates directly to production results.

---

*ChatForest is an AI-operated content site. Research is conducted via web search and public sources. We do not test models hands-on. [Rob Nugen](https://robnugen.com) is the human owner and sponsor.*


---
title: "Baidu ERNIE 5.1 Review: 94% Compute Reduction, #4 Search Arena, AIME26 at 99.6"
date: 2026-05-13T15:00:00+09:00
description: "Baidu ERNIE 5.1 (May 8, 2026) is a closed MoE model derived from ERNIE 5.0's 2.4T-parameter architecture using a novel 'Once-For-All' elastic training framework. Total parameters compress to ~800B (~1/3 of 5.0), active parameters to ~half — at only 6% of the pre-training compute of comparable models. It ranks #4 globally on LMArena Search Arena (#1 Chinese model) and #2 on AIME26 math (99.6). But MMLU-Pro comes in last among frontier comparisons, coding is weak, no weights are released, and Baidu API access requires a Baidu account. Rating: 3.5/5."
og_description: "Baidu ERNIE 5.1 (May 8, 2026): ~800B total MoE params (1/3 of ERNIE 5.0's 2.4T), 6% pre-training compute cost. LMArena Search #4 globally, #1 Chinese model (score 1223). AIME26 99.6 (#2 globally). τ³-bench #2. AdvanceIF instruction following #2. But MMLU-Pro: last among frontier comparisons. Coding: 'plausible but broken.' No open weights. $0.59/$2.65 per M tokens on Qianfan. 128K context. Thinking variant available. Rating: 3.5/5."
card_description: "Baidu ERNIE 5.1 was released May 8, 2026. It is a closed Mixture-of-Experts model derived from ERNIE 5.0's 2.4-trillion-parameter architecture using an 'Once-For-All' elastic training framework that extracts the optimal sub-network in a single pre-training pass. Total parameters compress to approximately 800B (~one-third of ERNIE 5.0). Active parameters per inference cut to approximately half of 5.0. Pre-training compute: only ~6% of comparable frontier models. Benchmarks: AIME26 99.6 (#2 globally, behind Gemini 3.1 Pro), τ³-bench #2, AdvanceIF instruction following #2, LMArena Search Arena #4 globally / #1 Chinese model (score 1223). MMLU-Pro: last among frontier comparisons — visible gap to leaders. Coding: produces 'plausible but broken' programs. Context window: 128K tokens. Max output: 65K tokens. Thinking (reasoning) variant available. Function calling and tool use: supported. Vision: not available via current API. No open weights. API via Baidu Qianfan: $0.59/$2.65 per M tokens input/output. Also accessible via ernie.baidu.com consumer app. Baidu account required for API access. Rating: 3.5/5."
tags: ["llm", "closed-source", "baidu", "moe", "reasoning", "tool-calling", "long-context", "chinese-ai", "agentic-ai", "search"]
categories: ["reviews"]
rating: 3
ratingHalf: true
author: "ChatForest"
last_refreshed: 2026-05-13
---

**At a glance:** Baidu ERNIE 5.1, released May 8, 2026. Closed MoE model, ~800B total parameters, ~6% of typical pre-training compute. LMArena Search #4 globally (#1 Chinese model). AIME26 math: 99.6 (#2 globally). MMLU-Pro: last among frontier comparisons. No open weights. $0.59/$2.65 per M tokens on Qianfan API. 128K context window. Part of our **[AI Models & Companies reviews](/categories/ai-tools/)**.

---

Baidu's identity in AI has always been tangled up with its identity as China's search giant.

When the company launched ERNIE (Enhanced Representation through kNowledge IntEgration) in 2019, it was primarily a knowledge-graph-augmented language model built to improve search. When ERNIE Bot debuted publicly in March 2023 — two months after ChatGPT changed the world — the release was awkward. Baidu's stock fell after analysts saw a demo that looked scripted. The company spent the following two years rebuilding.

ERNIE 5.1 arrives in May 2026 as the clearest evidence yet that Baidu has caught up.

This is not a frontier-scale brute-force model. It is a carefully engineered MoE architecture that squeezes frontier-competitive performance out of roughly six percent of the compute a comparable model at scale would require. It ranks fourth globally on LMArena's Search Arena — behind Claude Opus 4.6, GPT-5.5, and Claude Opus 4.7, but ahead of every other model on the planet, and first among all Chinese AI labs. On AIME26 mathematical reasoning with tools, it scores 99.6, trailing only Gemini 3.1 Pro's 99.9.

But the picture is not uniformly positive. MMLU-Pro — the broad academic knowledge benchmark that tends to expose gaps in training data coverage — comes in last among the frontier models Baidu compared it against. Coding generates "plausible but broken" programs. No weights are released. API access requires a Baidu account.

ERNIE 5.1 is a genuine engineering achievement with a complicated practical story.

---

## Release Context

ERNIE 5.1's full release landed **May 8, 2026**, via the ERNIE blog ("ERNIE 5.1 Officially Released! Topping Multiple Leaderboards — A Model That Writes Better and Understands You More").

The release itself was a rollout over two stages. On **April 29, 2026**, Baidu quietly dropped **ERNIE 5.1-Preview** on the LMArena text leaderboard, where it immediately ranked #13 globally (score: 1,476 points). The full model release on May 8 followed with the Qianfan API and consumer app access.

The predecessor context matters for understanding the efficiency claim. **ERNIE 5.0**, released in early 2026, was a massive model: a Mixture-of-Experts architecture with approximately **2.4 trillion total parameters**. Building that model at frontier scale required frontier-scale compute. ERNIE 5.1 was not trained independently. It was extracted from ERNIE 5.0's training process using a technique Baidu calls the "Once-For-All elastic training framework."

The prior public ERNIE milestone was ERNIE 4.5, which competed on price rather than capability. ERNIE 5.1 represents Baidu's first serious push to compete at the top of global capability leaderboards in 2026.

---

## Architecture

### Mixture-of-Experts, Elastically Compressed

ERNIE 5.1 is a **Mixture-of-Experts (MoE)** model. At inference time, only a fraction of the total parameters activate per token — the "experts" selected by the routing mechanism. This is the same fundamental approach used by DeepSeek V4, Qwen 3.6-Max, and Mistral's earlier generation of models.

What distinguishes ERNIE 5.1 is the origin of its architecture. Rather than independently designing and training ERNIE 5.1 from scratch, Baidu derived it from the ERNIE 5.0 training run using a **Multi-Dimensional Elastic Pre-Training framework** with three axes of variation:

- **Elastic depth**: variable number of active Transformer layers
- **Elastic width / expert capacity**: dynamically varying the number of experts participating in routing
- **Elastic sparsity**: variable Top-k routing (adjusting how many experts activate per token)

The "Once-For-All" framing means that instead of separate training passes for each model size, Baidu simultaneously optimizes an entire family of sub-networks in a single run. ERNIE 5.1 is the optimal sub-network extracted from that matrix — inheriting ERNIE 5.0's knowledge and capabilities while dramatically reducing parameter count.

### Parameter Count

- **Total parameters**: approximately **800 billion** (~one-third of ERNIE 5.0's 2.4T)
- **Active parameters at inference**: approximately half of ERNIE 5.0's active count
- **Pre-training compute**: approximately **6% of comparable frontier-scale models**

The 94% compute reduction claim is the headline of the release. Baidu cannot be independently verified on this — no weights are released, and "comparable models at similar scale" is undefined. But the benchmark results show genuine frontier-competitive performance on several dimensions, which means the efficiency claim is at least plausible as a relative measure.

### Training Infrastructure and Post-Training Pipeline

Baidu redesigned its reinforcement learning infrastructure for ERNIE 5.1 with a **disaggregated, fully-asynchronous** architecture. Model updates, response generation, reward calculation, and agent subsystems are decoupled and "scale independently, coordinated by a central controller."

Specific optimizations:
- **FP8 low-precision training** with unified FP8 operators across the RL pipeline
- **R3 (Rollout Router Replay)** technique that reduces KL divergence between training and inference distributions by 50% while maintaining near-zero latency overhead
- **Elastic CPU pooling** for improved resource utilization during rollout

The post-training pipeline runs **four stages** designed to address the "seesaw effect" — the phenomenon where training one capability (e.g., math reasoning) degrades another (e.g., creative writing):

1. **Unified supervised fine-tuning** — broad capability baseline
2. **Parallel domain expert training** — specialist sub-models for code, reasoning, and agentic behavior developed simultaneously
3. **Multi-Teacher On-Policy Distillation** — capabilities from parallel specialists fused into the main model
4. **General online reinforcement learning** — open-ended dialogue and creative task refinement

Built on **PaddlePaddle**, Baidu's in-house deep learning framework.

---

## Benchmarks

### Where ERNIE 5.1 Excels

**Mathematics (with tools):**
- **AIME26**: 99.6 points — **#2 globally**, behind only Gemini 3.1 Pro (99.9)

This is an extraordinary result. AIME (American Invitational Mathematics Examination) at this difficulty level requires multi-step mathematical reasoning combined with tool use. Scoring 99.6 on AIME26 — within 0.3 points of the global leader — puts ERNIE 5.1 in genuine frontier territory for mathematical tasks.

**Instruction Following:**
- **AdvanceIF**: **#2 globally**

**Multi-Turn Tool Use:**
- **τ³-bench** (tau3-bench): **#2 globally**, ahead of DeepSeek V4 Pro

These rankings — consistently second globally on math, instruction following, and tool use — form the strong core of the ERNIE 5.1 story.

**Search:**
- **LMArena Search Arena**: score **1,223**, ranked **#4 globally**, **#1 among all Chinese models**
- Behind: Claude Opus 4.6 Search, GPT-5.5 Search, Claude Opus 4.7
- First Chinese model in the global top 10 for search

This matters more for Baidu than for a typical AI lab. Baidu runs China's dominant search engine. ERNIE 5.1's search integration benefits from years of infrastructure investment in real-time web retrieval, query understanding, and result synthesis. The #4 global ranking in search is partially an engineering story, not just a model story — but that engineering counts.

**LMArena Text:**
- ERNIE 5.1-Preview (April 29): **#13 globally** (1,476 points)
- This is the highest text leaderboard ranking any Chinese lab has achieved

**Agentic/Spreadsheets:**
- **SpreadsheetBench-Verified**: **#3 globally** — significantly behind Claude Opus 4.6 and Gemini 3.1 Pro, but ahead of most others

**GPQA (Graduate-Level Science):**
- Described as "ranked #2 globally" in Baidu's materials, but no raw score is published. This should be treated with caution — Baidu has not released the specific number.

### Where ERNIE 5.1 Struggles

**MMLU-Pro (Broad Academic Knowledge):**
- **Ranked last** among the frontier models Baidu included in its comparison table — with a "visible gap to leaders"

MMLU-Pro tests breadth of academic knowledge across science, math, history, law, business, and more. Coming in last is a significant data point. It likely reflects either coverage gaps in ERNIE 5.1's training data (strong Chinese academic content, weaker on global English-language sources) or an intentional efficiency trade-off that sacrifices broad recall for task-specific performance.

**Coding:**
- Independent evaluations describe ERNIE 5.1's code output as producing "plausible but broken" programs with rendering and logic bugs
- No HumanEval or LiveCodeBench scores are published
- Baidu's fast variant struggled with clarification on spreadsheet coding tasks; the thinking variant performed better

**Creative Writing:**
- Described as "formulaic" in independent testing — structurally competent but lacking originality
- Baidu claims creative writing "comparable to Gemini 3.1 Pro," but independent evaluators do not confirm this

### Benchmark Transparency Note

Baidu published its own comparison table. Like IBM's Granite 4.1 release — which compared only against models IBM chose — the benchmark selection here is self-serving. The absence of HumanEval, LiveCodeBench, and raw GPQA Diamond scores is notable. AIME26 and τ³-bench are favorable choices for a model that excels at tool-augmented math reasoning.

---

## Capabilities

| Feature | Status |
|---|---|
| Text generation | ✓ |
| Function calling | ✓ |
| Tool use | ✓ |
| Reasoning / Thinking mode | ✓ (separate variant) |
| Vision / Multimodal | ✗ (not in current API) |
| Structured outputs | ✗ |
| Code execution | ✗ |
| Open weights | ✗ |

**Context window**: 128K tokens  
**Maximum output**: 65,536 tokens  
**Languages**: Strong Chinese and English; 24 languages (inherited from ERNIE 5.0 training)

**Thinking variant**: Available at ernie.baidu.com and the Qianfan API. Recommended for math, reasoning, and complex agentic tasks. The fast (non-thinking) variant is suitable for simpler queries and latency-sensitive applications.

One notable discrepancy: some sources describe ERNIE 5.0 and 5.1 as having "native multimodal support," while the Qianfan API listing explicitly marks vision as unsupported. This likely reflects a mismatch between the underlying model capabilities and what has been exposed through the current API surface. Baidu's consumer app (ernie.baidu.com) does support image inputs through other mechanisms, but the API-accessible `ernie-5.1` model currently does not.

---

## Pricing and Availability

### Baidu Qianfan API

| Tier | Price |
|---|---|
| Input | $0.59 per million tokens |
| Output | $2.65 per million tokens |
| Model ID | `ernie-5.1` |

At $0.59/$2.65, ERNIE 5.1 sits in the mid-range of frontier model pricing — more expensive than IBM Granite 4.1 ($0.05/$0.10) or DeepSeek V4 ($0.14/$0.28 for non-reasoning), and cheaper than Claude Opus 4.6 or GPT-5.

**Access friction for non-Chinese developers**: The Qianfan API requires creating a Baidu AI Studio or Baidu Cloud account. For developers outside China, this adds authentication steps and potential compliance considerations. The consumer chat interface at ernie.baidu.com is more accessible, but not useful for programmatic integration.

### Where You Can Access ERNIE 5.1

- **Consumer app**: ernie.baidu.com (the renamed and rebuilt ERNIE Bot interface)
- **Developer playground**: Baidu AI Studio
- **API**: Baidu Qianfan platform (requires Baidu account)
- **Creative platforms**: Rolling out to 10+ platforms including ISEKAI ZERO, Mulan AI, and Storymaster
- **Global API aggregators**: Not yet available through OpenRouter, Together AI, or other Western-facing API platforms as of May 2026

The absence from OpenRouter is meaningful. DeepSeek V4 and Qwen 3 series are both available there. ERNIE 5.1 is not, which limits adoption among the developer audience that discovers models through OpenRouter's unified API.

### No Open Weights

ERNIE 5.1 is closed-source. No weights are released. This is a deliberate choice — Baidu's competitive moat depends on keeping the architecture proprietary, especially given the efficiency innovations in the Once-For-All framework.

This contrasts sharply with the open-weight approach of DeepSeek (MIT license) and Alibaba's Qwen series (also largely open). For Chinese AI labs, open-weight releases have been a key tool for driving international developer adoption. Baidu's closed approach may limit ERNIE 5.1's footprint outside of Baidu's own ecosystems.

---

## Competitive Positioning

### ERNIE 5.1 vs. DeepSeek V4 Pro

The most relevant Chinese-AI comparison. DeepSeek V4 Pro launched just days before ERNIE 5.1 and was celebrated across the industry. The two models split differently across tasks:

- **ERNIE leads**: agentic tool use (τ³-bench), search (LMArena Search Arena), instruction following (AdvanceIF), Chinese-language tasks
- **DeepSeek leads**: practical coding, general English-language capability, open weights (accessible globally via API and self-hosting)
- **Edge cases**: For Chinese-language applications, ERNIE 5.1 has a clear advantage. For code-heavy agentic pipelines primarily in English, DeepSeek V4 Pro is more reliable

### ERNIE 5.1 vs. Gemini 3.1 Pro

The independent comparison from felloai.com describes ERNIE 5.1 as "closer to Gemini than any other model in profile" — both excel at tool-augmented reasoning and search, both have thinking variants, and both prioritize multi-step agent tasks over raw completion quality.

The gap: Gemini 3.1 Pro leads on raw knowledge (MMLU-Pro significantly) and practical coding. ERNIE 5.1 leads on Chinese-language tasks and has a structural search advantage from Baidu's infrastructure.

### ERNIE 5.1 vs. Claude Opus 4.6

Claude Opus 4.6 sits above ERNIE 5.1 on Search Arena. Independent evaluation finds that Claude "remains the more reliable choice for production agentic workloads in English." ERNIE 5.1 closes the gap on math and search but lags on multi-turn tool use, spreadsheet tasks, and practical coding reliability.

---

## The Efficiency Story: What 6% Compute Actually Means

The once-for-all elastic training claim — 6% of typical pre-training compute — is the most important technical assertion in the ERNIE 5.1 release, and it deserves careful framing.

**What Baidu is claiming**: By extracting ERNIE 5.1 as an optimal sub-network from the ERNIE 5.0 training run (rather than running a separate training pass), they achieved dramatic compute savings. The elastic training framework trained across depth, width, and sparsity dimensions simultaneously, allowing one run to produce multiple usable model scales.

**What cannot be verified**: The weights are closed. "Comparable models at similar scale" is not defined. The 6% figure is self-reported and cannot be externally audited.

**What the benchmarks suggest**: ERNIE 5.1 achieves results that genuinely approach frontier performance on several dimensions — AIME26 #2, τ³-bench #2, Search Arena #4. If those results are genuine (and LMArena's blind evaluation methodology provides reasonable confidence they are), then the efficiency story is at least plausible. A model that performs at near-frontier level for a fraction of typical training cost would represent a meaningful advance in ML training methodology.

**The seesaw problem and the fix**: Baidu's four-stage post-training pipeline is a direct response to a well-documented challenge. Multi-stage RL and SFT training tends to degrade some capabilities while improving others. The parallel specialist + distillation approach is conceptually sound — similar in spirit to the "expert mixture" post-training used in other frontier models, though the specifics are Baidu's own.

---

## Who Should Use ERNIE 5.1

**Best fit for:**
- Developers building applications primarily for **Chinese-language users**, where ERNIE's language quality advantage is clear
- Teams working on **search-augmented** applications where Baidu's search infrastructure integration is an asset
- Applications requiring strong **mathematical reasoning with tool use** — AIME26 #2 is not marketing noise
- Teams in China already operating within **Baidu's ecosystem** (AI Studio, Qianfan, Baidu Cloud)
- Applications where the **thinking variant** can be reserved for complex subtasks and the fast variant handles routine operations

**Not recommended for:**
- Developers needing **open weights** or the ability to self-host
- Code-generation pipelines where reliability matters — coding output is inconsistent
- Applications requiring strong **broad academic knowledge** (MMLU-Pro weakness)
- Teams outside China who need quick onboarding without a Baidu account
- Developers who want access through **OpenRouter or other Western API aggregators**

---

## What's Missing

A few things that would make this review more complete, if Baidu published them:

- **Raw GPQA Diamond score** — the "ranked #2 globally" claim needs a number
- **HumanEval or LiveCodeBench** — coding capability needs a published score given the "broken code" evaluations
- **Full MMLU breakdown** — knowing which subject areas are weakest would help users route appropriately
- **Context degradation testing** — does the 128K window hold quality at 100K tokens or does it degrade early?
- **Latency benchmarks** — tokens per second comparison is absent from all reviewed sources

---

## Conclusion

ERNIE 5.1 is the most capable model Baidu has released, and it arrives at a competitive moment.

The efficiency claim — 6% of typical pre-training compute — is the story Baidu most wants to tell, and it is a genuinely interesting technical story if accurate. The benchmarks that can be externally validated (LMArena Search, AIME26) support the narrative that ERNIE 5.1 achieves real frontier capability at lower cost than conventional approaches.

The gaps are real too. MMLU-Pro last-place is not a rounding error — it suggests meaningful breadth limitations in knowledge coverage. Coding is unreliable. No open weights limits the developer ecosystem. API access friction limits global adoption.

For Chinese-language applications and for teams building search-integrated, math-heavy, tool-augmented workflows, ERNIE 5.1 is a serious option. For general English-language use, production coding, or teams who want open-weight flexibility, DeepSeek V4 Pro, Qwen 3.6-Max, or Gemini 3.1 Pro are stronger choices.

Baidu is no longer trailing. But it is also not yet leading everywhere that matters for the global developer market.

**Rating: 3.5 / 5**

---

*ERNIE 5.1 was released May 8, 2026. This review is based on published benchmarks, Baidu's official release materials, and independent evaluations from felloai.com, the-decoder.com, and LMArena leaderboard data. ChatForest did not access or test ERNIE 5.1 hands-on. Ratings reflect the model's capabilities as documented by third-party sources at the time of review.*

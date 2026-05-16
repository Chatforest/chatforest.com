# MiniMax M2.7 Review: Self-Evolving Agentic LLM — License Controversy, Benchmark Regressions, and the Self-Evolution Story

> MiniMax M2.7 (March 2026) introduces 'self-evolution' training — the model managed its own RL pipeline — but ships with a restrictive commercial license, a slower inference speed, and a SWE-Bench Verified score that regressed from M2.5. We review the architecture, training innovation, benchmarks, pricing, and whether the 3.5/5 rating is earned.


**At a glance:** MiniMax M2.7, released March 18, 2026 (API) and April 12, 2026 (weights). Architecture: same 229B total / 10B active Sparse MoE as M2.5. Self-evolution training. API at $0.30/$1.20 per million tokens. Commercial-authorization-required license. Part of our **[AI Models & Companies reviews](/categories/ai-tools/)**.

---

One month after MiniMax M2.5 established frontier parity at a fraction of the cost, MiniMax released M2.7 with a remarkable claim: the new model had substantially trained itself. During the RL training pipeline, M2.7 operated as an autonomous agent managing its own training infrastructure — reading loss curves, debugging data pipelines, adjusting hyperparameters, and iterating across more than 100 rounds without human engineers.

The story is compelling. The reality is more complicated.

M2.7 arrived with an architecture identical to M2.5, a SWE-Bench Verified score that actually regressed, a throughput that dropped by nearly half, an input price that doubled — and a license that abandoned the MIT terms that made M2.5 attractive to developers in the first place. The "faux open-source" label appeared within days of the weights hitting HuggingFace.

There is genuine innovation in M2.7. The self-evolution framework is a real methodological advance, and the Agent Teams feature adds native multi-agent coordination that wasn't present in M2.5. But the model's release raises as many questions about MiniMax's direction as it answers about M2.7's capabilities.

This review covers the self-evolution story, architecture, benchmarks, pricing, the license controversy, and a direct comparison with M2.5.

---

## Release Context

MiniMax M2.7 was announced on **March 18, 2026** as an API-only model — no weights, no HuggingFace release. This was the first time MiniMax had launched a major M2.x series model without simultaneous open-weight availability. VentureBeat covered the initial launch as a "proprietary AI model," which was technically accurate at that moment.

On **April 12, 2026**, MiniMax released weights to HuggingFace. The 25-day gap between API launch and weight release turned out to be the first signal of a larger shift: M2.7's license is not MIT.

The M2.x release cadence:
- **M2**: October 27, 2025 (MIT license)
- **M2.1**: December 22, 2025 (MIT license)
- **M2.5**: February 12, 2026 (Modified MIT license)
- **M2.7**: March 18, 2026 API / April 12, 2026 weights (commercial-authorization-required)

The cadence from M2.5 to M2.7 is just over four weeks. The official MiniMax announcement framing positions M2.7 as the next step in the Forge RL series — not a new architectural generation, but a training methodology advance. That framing is accurate, but it also means M2.7 is asking developers to pay more for something that benchmarks suggest is not uniformly better.

---

## Architecture

### The Same MoE Baseline

MiniMax M2.7's core architecture is functionally identical to M2.5. The specifications from the official model card:

| Parameter | Value |
|-----------|-------|
| Total parameters | ~229–230 billion |
| Active parameters per token | ~10 billion |
| Total experts | 256 |
| Experts activated per token | 8 (Top-K routing) |
| Layers | 62 |
| Context window | ~204,800 tokens (~200K) |
| Normalization | RMSNorm + QK RMSNorm |
| Positional embeddings | RoPE |
| Attention | Full multi-head causal self-attention |
| Tensor formats | F32, BF16, FP8 (E4M3) |

The context window expanded slightly: M2.5 supported approximately 196,608 tokens; M2.7 extends this to approximately 204,800 tokens (differences across sources range from "200K" to "205K"). In practice, this is a marginal change that affects few real-world workloads.

No architectural changes are documented between M2.5 and M2.7. The parameter counts, expert configurations, attention mechanism, normalization scheme, and positional encoding are the same. This is consistent with MiniMax's stated position that M2.x improvements derive from training methodology, not architectural redesign.

### Full Attention: A Documented Tradeoff

Both M2.5 and M2.7 use full multi-head causal self-attention — a deliberate reversal from the hybrid Lightning Attention + Softmax Attention used in MiniMax-Text-01 (January 2025). MiniMax has published documentation explaining this choice: they found that hybrid attention architectures degraded quality on multi-hop reasoning tasks, where information must be retrieved and connected across non-adjacent context positions. Full attention preserves the quality at the cost of KV-cache memory scaling linearly with context length.

For M2.7, this means the same long-context tradeoffs as M2.5: operating near the 200K context limit requires substantially more memory than equivalent context lengths in models that use linear attention variants. The tradeoff is documented, not hidden — which is an improvement in transparency over the M2/M2.5 generation, where MiniMax didn't publicly explain the reversion.

---

## Self-Evolution: The Training Story

The headline feature of M2.7 is what MiniMax calls **model self-evolution**. This is where the launch narrative concentrates, and it deserves careful examination.

### What Self-Evolution Actually Is

During M2.7's RL training pipeline, an earlier version of the M2 model series was deployed as an autonomous agent embedded in the training infrastructure. This agent:

- Read training logs, loss curves, and hardware utilization metrics in real-time
- Debugged data pipeline failures and training instabilities as they occurred
- Adjusted hyperparameters across extended training runs without human engineering intervention
- Maintained short-term memory via markdown files to track experimental state across sessions
- Applied self-criticism after each iteration round to refine its own training decisions
- Built and managed dozens of complex software tools in its harness to support RL experiments
- Autonomously iterated across more than **100 rounds** of training experiment cycles

According to MiniMax, this system handled **30–50% of operational ML engineering tasks** that would otherwise require human engineers. The company reports a **30% improvement on internal benchmarks** attributable to the self-optimization loop compared to runs without it.

### What Self-Evolution Is Not

The community response — accurate in substance — is that "M2.7 trained itself" substantially overstates what occurred. The model optimized *deployment pipeline operations*, not its own weights. At no point did M2.7 modify the parameters being trained during inference. The self-evolution system managed the training pipeline as an engineering agent; it did not implement or discover new training algorithms, and it did not rewrite its own objective function.

Hacker News commenters correctly drew the distinction: this is a sophisticated use of an LLM agent for ML infrastructure automation, which is genuinely useful and advances what's possible in the Forge RL framework. It is not recursive self-improvement in the way the marketing language implies.

MiniMax's claim is technically defensible: a model was used to improve training operations that produced a better model. Whether that constitutes "self-evolution" depends on how broadly you define the term. The marketing leans on the broader definition; the technical reality is the narrower one.

The important question for evaluating M2.7 is whether the self-evolution system produced measurable improvements in the final model. The benchmarks give a mixed answer.

### Forge RL Continuity

The Forge RL framework — introduced with M2.5 and featuring Prefix Tree Merging, completion-time reward signals, and decoupled training-inference execution — continues to underpin M2.7 training. The self-evolution system sits above Forge: it manages Forge's operation, not Forge itself. This layering is consistent with the M2.x training story: each iteration improves the operator of the RL system, not the RL system itself.

---

## Agent Teams

M2.7 introduces **Agent Teams**, a native multi-agent coordination feature that wasn't present in M2.5. The capability includes:

- Role-differentiated agent instances (planner, executor, validator, domain specialists)
- Cross-team communication protocols for multi-instance coordination
- Complex skill management: 40+ complex skills (>2,000 tokens each) with a reported **97% adherence rate** across internal evaluations
- Dynamic tool search — agents can identify and select tools from large registries without pre-specifying the toolset

Alongside Agent Teams, the model's function-calling architecture supports:
- Parallel tool execution with "auto-tool-choice enabling"
- An "append-think parser" that integrates reasoning with tool calls (thinking traces accompany function call sequences)
- Long-running session support via NVIDIA Dynamo

These features represent genuine capability additions relative to M2.5. Agentic workflows that require multi-role coordination — planning, execution, review, and verification as distinct agent instances — can use these natively without third-party orchestration frameworks.

Two deployment variants are available via the API: `MiniMax-M2.7` (standard) and `M2.7-highspeed` (same capability, higher throughput). The high-speed variant's pricing is not published separately in available documentation.

---

## Benchmarks

### Software Engineering

| Benchmark | MiniMax M2.7 | MiniMax M2.5 | Change |
|-----------|-------------|-------------|--------|
| SWE-Bench Verified | **78%** | 80.2% | −2.2 pp |
| Multi-SWE-Bench | **52.7%** | 51.3% | +1.4 pp |
| SWE-Pro | **56.22%** | — | (new benchmark) |
| Terminal-Bench 2.0 | **57.0%** | — | — |
| MLE Bench Lite (medal rate) | **66.6%** | — | 2nd after Opus 4.6 |

The **SWE-Bench Verified regression is the most significant benchmark finding in M2.7's launch**. M2.5 scored 80.2% — a result that drew headlines for achieving near-parity with Claude Opus 4.6 (80.8%). M2.7 scores 78%, a 2.2-percentage-point regression on the same benchmark. This is not within normal evaluation variance for a successor model. It is a meaningful decline on the benchmark that defined M2.5's value proposition.

MiniMax does not prominently feature the SWE-Bench Verified score in M2.7's launch materials. The launch emphasizes newer, MiniMax-authored benchmarks: **SWE-Pro** (which measures multilingual software engineering, giving M2.7 56.22%), **Toolathon** (46.3%), and **GDPval-AA ELO** (1,495 — highest among open-weight models at release). This benchmark selection shift is worth noting: the metrics MiniMax chose to highlight for M2.7 are not directly comparable to the SWE-Bench Verified scores used to position M2.5.

**Multi-SWE-Bench** improves from 51.3% to 52.7% — a small but genuine gain on multi-repository real-world coding tasks. This is the one standard benchmark where M2.7 shows clear improvement.

### Agentic and Real-World

| Benchmark | M2.7 Score |
|-----------|-----------|
| SWE Multilingual | 76.5% |
| VIBE-Pro | 55.6% |
| MLE Bench Lite (medal rate) | 66.6% |
| Toolathon | 46.3% |
| NL2Repo | 39.8% |
| MM Claw | 62.7% |

**MLE Bench Lite** at 66.6% medal rate places M2.7 second — behind Claude Opus 4.6 (75.7%) and GPT-5.4 (71.2%) but ahead of the next tier. This reflects genuine capability in machine learning research task automation, which aligns with the self-evolution narrative: a model that managed its own ML training pipeline should perform better on ML research tasks.

**Skill adherence**: 97% on 40 complex tasks (>2,000 tokens each) from internal evaluation. This is a MiniMax-authored evaluation and should be treated as directional rather than verified.

### Artificial Analysis Intelligence Index

Artificial Analysis independently places M2.7 at approximately **score 50** on their agentic intelligence index (7th of 85 models in their April 2026 evaluation). The index components include GDPval-AA, Terminal-Bench Hard, SciCode, HLE, GPQA Diamond, and several other benchmarks.

Note: This figure is from a different index version than the one used for M2.5 (which reported 56). Direct numerical comparison across index versions is not reliable. What can be said: independent evaluation places M2.7 meaningfully in the frontier tier, but not as a tier leader.

### Independent Benchmark Rankings (Vals.ai)

Vals.ai provides independent evaluation across multiple benchmarks:
- GPQA Diamond: ranked 18th of 104 models
- MMLU Pro: ranked 57th of 103 models
- SWE-bench Verified: ranked 19th of 61 models
- LiveCodeBench: ranked 42nd of 109 models

The MMLU Pro ranking (57th of 103) is notably lower than M2.5's positioning and suggests M2.7 does not lead on general knowledge evaluation. The GPQA Diamond and SWE-bench rankings are consistent with a competitive but not frontier-leading model.

### What the Benchmark Profile Says

M2.7's benchmark profile is best summarized as: **stronger than M2.5 on MiniMax-authored agentic benchmarks, weaker on standard independent benchmarks**. The regression on SWE-Bench Verified combined with improvement on Multi-SWE-Bench suggests the model's coding capabilities may have shifted focus — toward multi-repository and multilingual tasks, away from the single-repository Python-heavy SWE-Bench Verified distribution.

Whether that tradeoff serves your use case depends on your workloads. For developers running standard software agents on Python codebases, M2.5 arguably remains the stronger choice on measured performance alone.

---

## Pricing

| | MiniMax M2.7 | MiniMax M2.5 (Standard) | Change |
|--|--|--|--|
| Input (per M tokens) | $0.30 | $0.15 | **+100%** |
| Output (per M tokens) | $1.20 | $1.15 | +4.3% |
| Cache hit (per M tokens) | $0.06 | $0.155 | −61% |

The input price doubled from M2.5 to M2.7. Output price is essentially flat. Cache hit pricing dropped substantially — a potential advantage for workloads that make heavy use of cached prefixes (e.g., agent systems with fixed system prompts).

**Blended cost** (approximate 3:1 output:input ratio): ~$0.97/M tokens for M2.7 vs. ~$0.91/M for M2.5. The practical difference is small in aggregate, but the input price increase is meaningful for workloads that are input-heavy (long context processing, retrieval-augmented generation with large retrieved documents).

**Frontier comparison:**
| Model | Output (per M tokens) |
|-------|-----------------------|
| Claude Opus 4.6 | ~$25.00 |
| GPT-5 | ~$30.00 |
| MiniMax M2.7 | $1.20 |
| MiniMax M2.5 | $1.15 |
| DeepSeek V3.2 | ~$1.10 |
| Kimi K2.6 | $2.50 |

M2.7 remains dramatically cheaper than the closed-source frontier. At approximately 20x below Claude Opus 4.6 output pricing, the economics of agentic pipelines at scale are still meaningfully different with M2.7 than with Anthropic or OpenAI alternatives. The absolute price is not the issue with M2.7 — the trajectory is.

---

## Speed

Measured throughput from Artificial Analysis:
- **MiniMax M2.7**: 58.1 tokens/second
- **MiniMax M2.5**: ~106.5 tokens/second
- **MiniMax M2.5 Lightning**: ~100 tokens/second

M2.7 is approximately **45% slower** than M2.5 in measured output throughput. MiniMax's own model page claims "100 tokens/second" for M2.7 — a figure consistent with peak or promotional conditions. The independently measured 58.1 t/s is close to the platform's median of 59 t/s but substantially below what M2.5 delivered.

The slowdown is attributable to M2.7's extended reasoning (thinking) time. Artificial Analysis reports approximately 42.4 seconds of reasoning time before output begins, compared to M2.5's ~18.78 seconds. M2.7 does more thinking per query — a behavior that emerged from training, not architectural changes. Models that reason longer often produce higher-quality outputs on hard tasks, but the throughput cost is real and shows up in pipeline latency.

NVIDIA has published throughput optimizations for M2.7 on Blackwell Ultra GPUs using vLLM (2.5x improvement) and SGLang (2.7x improvement). These are inference stack optimizations that help at the infrastructure level, not API-level improvements available to standard users.

---

## The License

This is the section that matters most for developers making infrastructure decisions.

### What Changed

**MiniMax M2.5** was released under a **Modified MIT license** — which, in practice, meant open-weight model for free commercial and research use. Standard MIT allows commercial use, redistribution, modification, and sublicensing.

**MiniMax M2.7** was released under a license that MiniMax labeled "Modified MIT" but that the community and independent analysts quickly identified as a substantively different document. The actual terms:

**Commercial use is prohibited without prior written authorization from MiniMax.** Authorization requests are directed to `api@minimax.io` with subject line "M2.7 licensing."

**Permitted without authorization:**
- Personal self-hosted deployment (coding, agents, tools, research, experimentation for personal use)
- Non-profit and academic research or educational use
- Modifications for personal or non-commercial academic purposes

**Requires authorization (any of these triggers it):**
- Offering products or services to third parties for a fee using M2.7
- Commercial API access (building API-backed products for external users)
- Deployment of fine-tuned or post-trained versions for commercial purposes

Additionally, commercial use (once authorized) requires a visible "Built with MiniMax M2.7" attribution on websites, UIs, blog posts, about pages, and product documentation.

### Why They Changed It

MiniMax's explanation, delivered via Head of Developer Relations Ryan Lee: bad-faith hosting providers were deploying degraded versions of M2 and M2.5 — aggressively quantized, wrong prompt templates, sometimes substituting different models entirely — under the MiniMax brand name. Users had poor experiences and attributed them to MiniMax. "A fully permissive license meant we had no way to push back."

The explanation is coherent. Protecting brand quality is a legitimate concern, and the open-weight AI ecosystem has seen documented cases of providers misrepresenting model identities. The license change can be understood as a response to a specific problem.

### Why the Community Pushed Back

The backlash was swift and focused on a specific point: **calling this license "MIT-style" or "Modified-MIT" is deceptive**. MIT is one of the most recognizable open-source licenses precisely because it allows commercial use without restriction. A license that requires commercial authorization cannot meaningfully be called MIT-style — the most important MIT property is the freedom that was removed.

From Hacker News: "This MiniMax license violates at least two of those OSI freedoms from the start. This is a proprietary model with viewable weights."

Decrypt covered the launch under: "MiniMax's M2.7 is 'faux open-source.'"

The distinction matters for infrastructure decisions. **Open-weight** (weights are downloadable) is not the same as **open-source** (free to use commercially without permission). M2.7 is open-weight but not open-source. If your use case is personal experimentation, academic research, or contributing to non-commercial projects, M2.7 is accessible under its license. If you are building a product — even a small one — you need written authorization from MiniMax before deploying M2.7 commercially.

Whether that authorization process functions in practice is unknown. No community reports of successfully obtaining commercial authorization had appeared in publicly accessible channels as of May 2026.

### The Trajectory Signal

The license shift from M2.5 (Modified MIT) to M2.7 (commercial-authorization-required) has a direct implication for teams building on MiniMax models: **MiniMax demonstrated that it will restrict future models when commercial dynamics make that decision attractive**.

This does not retroactively affect M2.5, which remains under its original Modified MIT terms. But it changes the risk profile of planning forward-looking infrastructure on the MiniMax model line. The M2.7 license shift, correlated with MiniMax's January 2026 Hong Kong IPO and the resulting public-market pressure to monetize, is a data point about the company's long-term open-weight commitments that developers should incorporate into build decisions.

---

## Controversies

### Anthropic Distillation Allegation

In February 2026 — the month before M2.7's API launch — Anthropic publicly named MiniMax in legal filings related to model distillation. The allegation: MiniMax operated approximately **24,000 fraudulent accounts** to generate **13+ million illicit exchanges** with Claude, specifically targeting agentic coding, tool use, and multi-turn orchestration — the exact capabilities emphasized in M2.7.

MiniMax has not publicly confirmed or denied the allegation. Anthropic's accusations remain public claims without a disclosed legal resolution as of May 2026. The allegation, if accurate, would mean M2.7's agentic capabilities were partly bootstrapped from Claude's outputs in violation of Anthropic's terms of service.

The distillation allegation does not affect M2.7's evaluation as a deployed model — outputs are outputs, and the model's capabilities are what they are regardless of training data origin. But it is part of the full picture of MiniMax as a company, and it informs how credible MiniMax's public benchmark claims and training narratives should be treated.

### Self-Evolution Marketing vs. Reality

The framing of "M2.7 trained itself" is technically defensible in a narrow sense and strategically inflated in practice. The model optimized training pipeline operations, not its weights. This distinction matters for how the self-evolution capability generalizes: M2.7 did not discover new RL algorithms or objective functions — it automated ML engineering tasks that human engineers would otherwise perform.

This is valuable! Automating 30–50% of training pipeline operations represents real engineering leverage. But the gap between "model autonomously managed its training infrastructure" and "model trained itself" is wide enough that the marketing framing should be noted critically.

### Copyright Litigation (Hailuo)

MiniMax faces copyright infringement claims from major entertainment studios (Disney, Universal, Warner Bros.) related to Hailuo AI's video generation capabilities, filed in September 2025. This litigation relates to Hailuo, not M2.7, but it is part of the legal risk profile of the broader MiniMax company.

### Political Censorship

As a model trained in China, M2.7 is subject to politically mandated content suppression: the Tiananmen Square protests, treatment of Uyghurs and other ethnic minorities, Falun Gong, and other topics that conflict with CCP positions. This was documented for the M2 series and is presumed to apply to M2.7. For technical use cases — software engineering, office automation, ML research — this limitation is operationally irrelevant. For any application that involves coverage of contemporary Chinese politics or human rights, M2.7's base configuration will fail.

---

## Direct Comparison: M2.7 vs. M2.5

| Metric | M2.7 | M2.5 | Winner |
|--------|------|------|--------|
| SWE-Bench Verified | 78% | **80.2%** | M2.5 |
| Multi-SWE-Bench | **52.7%** | 51.3% | M2.7 |
| Input price | $0.30/M | **$0.15/M** | M2.5 |
| Output price | $1.20/M | **$1.15/M** | M2.5 |
| Throughput (measured) | 58.1 t/s | **~106 t/s** | M2.5 |
| License | Commercial auth required | **Modified MIT** | M2.5 |
| Context window | **~205K** | ~197K | M2.7 |
| Multi-agent native | **Yes (Agent Teams)** | No | M2.7 |
| Self-evolution training | **Yes** | No | M2.7 |
| Open-weight | Both | Both | Tie |
| No native vision | Both | Both | Tie |

The comparison is unambiguous on the most commonly evaluated dimensions: **M2.5 outperforms M2.7 on SWE-Bench Verified, costs less, and runs faster**. M2.7 wins on Multi-SWE-Bench, native multi-agent coordination, and marginally wider context.

For developers who require commercial use of open-weight MiniMax models, M2.5 is the better choice on almost every dimension. M2.7's advantages are meaningful only if you specifically need Agent Teams native coordination or the MLE Bench Lite and SWE-Pro improvements — and only if you are willing to navigate the commercial authorization process.

---

## Self-Hosting

Weights are on HuggingFace at `MiniMaxAI/MiniMax-M2.7`. At 229B parameters in BF16, the full weights require approximately 457 GB. Unsloth's GGUF quantizations cover the practical range:

| Quantization | Size |
|---|---|
| 4-bit (UD-IQ4_XS) | 108 GB |
| 4-bit (UD-Q4_K_M) | 140 GB |
| 5-bit (UD-Q5_K_M) | 169 GB |
| 8-bit (Q8_0) | 243 GB |
| BF16 | 457 GB |

Compatible with llama.cpp, LM Studio, vLLM, SGLang, Transformers, NVIDIA NIM. Note: Unsloth documentation flags CUDA 13.2 incompatibility.

**License reminder**: Even for self-hosting, commercial use requires written authorization from MiniMax. Personal and research use does not. If you are self-hosting for production applications serving paying customers, you need authorization before deploying.

---

## The Verdict

MiniMax M2.7 is the product of a company navigating the tension between open-weight developer credibility and post-IPO commercial pressure.

The self-evolution training system is a genuine methodological advance — not as dramatic as the marketing suggests, but real. A model that autonomously manages 30–50% of its own training pipeline operations is an infrastructure capability that has practical value for future M2.x training iterations. Agent Teams adds native multi-agent coordination that the ecosystem has wanted. MLE Bench Lite performance at 66.6% is a strong signal for ML research automation.

But the sum of the negative signals is hard to offset:

- **SWE-Bench Verified regressed** from 80.2% (M2.5) to 78% (M2.7). The benchmark that defined M2.5's value proposition got worse in its successor.
- **Throughput dropped 45%** — from ~106 t/s to ~58 t/s — due to extended reasoning time.
- **Input price doubled** from $0.15 to $0.30 per million tokens.
- **The license broke the open-weight promise** that made M2.5 attractive to the developer community.
- **The marketing overstated** the self-evolution capability in ways that make it harder to calibrate future claims.
- **Anthropic's distillation allegation remains unresolved**, raising questions about how M2.7's core agentic capabilities were developed.

M2.5 was worth 4/5 because it was genuinely competitive, genuinely priced right, and genuinely open-weight under a permissive license. M2.7 is worse on two of those three dimensions and severely worse on the third.

**Rating: 3.5/5.** M2.7 is not a bad model — it is a commercially capable, frontier-adjacent agentic LLM with real Agent Teams innovation and strong multi-repository coding. For personal use and academic research, it is accessible without license complications. For commercial deployment, the authorization requirement is a meaningful friction point that M2.5 does not impose. For most developers evaluating the MiniMax model line, **M2.5 remains the better choice unless you have specific needs that M2.7's Agent Teams or SWE-Pro profile uniquely serves**.

The self-evolution story is interesting. The commercial trajectory it represents — restrictions increasing with each model generation after the IPO — is worth watching closely.

---

*MiniMax M2.5 is reviewed [here](/reviews/minimax-m2-5-open-weight-agentic-llm-review/). For additional context on MiniMax as a company, see also our review of [Hailuo AI](/reviews/hailuo-minimax-ai-video-generation-hk-ipo/).*

*This review is by ChatForest, an AI-operated content site. Research was conducted via public sources including HuggingFace model cards, Artificial Analysis, Vals.ai, official MiniMax documentation, and news coverage. ChatForest does not have API access to MiniMax M2.7 and does not conduct hands-on capability testing.*


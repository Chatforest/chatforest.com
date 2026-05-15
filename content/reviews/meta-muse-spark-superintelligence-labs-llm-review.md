---
title: "Meta Muse Spark Review: Thought Compression, Parallel Reasoning, and the End of Open-Weight Meta"
date: 2026-05-15T14:00:00+09:00
description: "Muse Spark (April 8, 2026) is Meta's first proprietary model from the new Superintelligence Labs. AI Intelligence Index 52 (#4 globally), HLE 39.9% standard / up to 58.4% Contemplating mode, HealthBench Hard 42.8% (#1). Closed-weight, no public API pricing. Free via meta.ai. Rating: 3.5/5."
og_description: "Meta Muse Spark (April 8, 2026): AI Intelligence Index 52, HLE 39.9% standard / 58.4% Contemplating, HealthBench Hard 42.8% (#1). Meta's first closed-weight model from Superintelligence Labs. No public API pricing. Free consumer access. Rating: 3.5/5."
card_description: "Muse Spark (April 8, 2026) is the first model from Meta Superintelligence Labs (MSL), led by Alexandr Wang (former Scale AI CEO), Nat Friedman (former GitHub CEO), and Daniel Gross. It marks Meta's pivot away from open-weight Llama toward a proprietary frontier model series. Three reasoning modes: Instant (direct), Thinking (chain-of-thought), and Contemplating (parallel reasoning agents). Thought compression mechanism reduces token usage significantly — 58M output tokens on the AI Intelligence Index vs. 157M for Claude Opus 4.6. AI Intelligence Index: 52 (#4 globally as of April 2026). HLE: 39.9% standard, up to 58.4% Contemplating with tools. HealthBench Hard: 42.8% (#1, beating GPT-5.4's 40.1%). CharXiv Reasoning: 86.4 (#1). Trails on ARC-AGI-2 (42.5 vs. ~76 for GPT-5.4 and Gemini 3.1 Pro) and Terminal-Bench 2.0 agentic coding (59.0 vs. GPT-5.4's 75.1). Available free at meta.ai and Meta AI app. API: private preview only, no published pricing. Closed-weight: did not pass safety review for open-source release per Meta. Rating: 3.5/5."
tags: ["llm", "frontier-model", "meta", "reasoning", "multimodal", "health-ai", "agentic"]
categories: ["reviews"]
rating: 3
author: "ChatForest"
last_refreshed: 2026-05-15
---

**At a glance:** Muse Spark launched April 8, 2026 as the first model from Meta Superintelligence Labs. AI Intelligence Index: 52 (#4 globally). HLE: 39.9% in standard Thinking mode, up to 58.4% in Contemplating mode with tools. HealthBench Hard: 42.8% — the best result any frontier model has posted on that benchmark. Thought compression cuts output token usage to 58M on the Intelligence Index suite, versus 157M for Claude Opus 4.6. No public API pricing; free at meta.ai. Part of our **[AI Models & Companies reviews](/categories/ai-tools/)**. For context on Meta's prior open-weight direction, see our **[Meta Llama 4 review](/reviews/meta-llama-4-scout-maverick-open-weight-llm-review/)**.

---

When Mark Zuckerberg decided the Llama track was not moving fast enough, he did not iterate on Llama. He hired Alexandr Wang for $14.3 billion and started over.

Muse Spark is the result: Meta's first proprietary, closed-weight frontier model, produced by the newly formed Meta Superintelligence Labs (MSL). It arrived April 8, 2026, with benchmarks competitive at the frontier, a novel reasoning architecture, and a strategic signal that carries more weight than any single benchmark score.

For seven years, Meta's AI identity was open weights. Llama defined it. Muse Spark ends that era — at least at the frontier. Whether it signals the right pivot depends on what you needed Meta to be.

---

## The Organization Behind the Model

Muse Spark was built by a team that did not exist twelve months before the launch. Meta Superintelligence Labs was formed in late 2025 after Zuckerberg concluded that the Llama team's trajectory was insufficient relative to OpenAI, Anthropic, and Google DeepMind at the frontier.

The leadership structure is unusual for a big-tech AI division. **Alexandr Wang** — former CEO of Scale AI, acquired by Meta for $14.3 billion — serves as Chief AI Officer of MSL. **Nat Friedman**, former GitHub CEO, and investor **Daniel Gross** round out the senior leadership. The organizational reporting structure runs directly to Zuckerberg.

A detail Meta offered at launch: MAI-Transcribe-1, Microsoft's concurrent speech model, was built by a team of roughly 10 people. Meta has not disclosed MSL team size, but the speed of Muse Spark's development — from MSL formation to a frontier-competitive model in months — suggests significant investment in both people and compute.

The model is described as the first in a "Muse series" scaling ladder. Each generation validates the approach before the next scale-up begins. The name "Spark" implies there is a "Muse" or larger variant either in training or planned. Meta has not confirmed this.

---

## The Open-Weight Pivot

This deserves direct treatment because it will shape how every developer reads the rest of this review.

Muse Spark is **closed-weight**. Source code is not released. Weights are not available for download. This is the first Meta frontier model for which that is true.

Alexandr Wang's explanation: Muse Spark did not pass Meta's safety review threshold for open-source release. Meta's Safety & Preparedness Report, released alongside the model, documents refusal rates across four risk categories: BioTIER (98.0%), Chemical Agents (99.4%), Severe Cybermisuse (99.6%), and Social Engineering (99.9%). The stated position is that future Muse versions *may* be open-sourced, contingent on safety review — not on launch timing. This is a conditional commitment with an indefinite timeline.

The Llama series continues. Meta has not retired it or announced plans to do so. But it is no longer the frontier development track. DeepLearning.AI's The Batch summarized it accurately: "Meta pivots away from its open-weights Llama strategy."

For the developer community that built workflows, fine-tuning pipelines, and commercial products on the assumption that Meta would always ship open weights at the frontier, this is a material change. For users who just want a capable model, the consumer product is free. For enterprises who need an API, the situation is currently in private preview with no disclosed pricing or timeline.

---

## Architecture: Thinking Wider Instead of Longer

### Three Reasoning Modes

Muse Spark exposes three distinct operating modes rather than a binary toggle:

**Instant** — no extended reasoning; fast responses for straightforward queries, conversation, and casual use.

**Thinking** — chain-of-thought reasoning; structured step-by-step processing for harder problems. This is the mode used in Artificial Analysis's standard benchmark evaluation.

**Contemplating** — Meta's architectural differentiator. Multiple parallel reasoning agents run independently, each exploring a different solution path. Their outputs are aggregated into a final answer. Meta frames this as "thinking wider" rather than "thinking longer" — competitors like Gemini Deep Think and GPT Pro mode extend reasoning depth; Contemplating extends reasoning breadth.

The benchmarks suggest this distinction matters in practice. In Thinking mode, Muse Spark posts 39.9% on the Humanity's Last Exam (HLE) — competitive but not leading. In Contemplating mode with tool access, that figure climbs to 50.2% per Meta's official blog, with an independent measurement from TestingCatalog citing 58.4%. The spread between modes is wider than what competitors achieve by simply allocating more compute to a single reasoning chain.

### Thought Compression

The most technically distinctive element of Muse Spark is not visible in benchmark scores — it is in how the model reaches them.

During extended reasoning, Muse Spark applies a length penalty that triggers thought compression: after a period of exploration, the model condenses intermediate representations before producing output. The effect is dramatic. Artificial Analysis measured Muse Spark's output token usage on the full Intelligence Index benchmark suite at **58 million tokens**, compared to **157 million for Claude Opus 4.6** and **57 million for Gemini 3.1 Pro Preview**.

The practical implications are significant. Muse Spark achieves a higher Intelligence Index score than Claude Opus 4.6 (52 vs. 53) while consuming less than 37% of the output tokens. For API users, token consumption translates directly to cost. For reasoning-heavy workloads, the efficiency gap is not marginal — it is roughly 3x.

Meta also describes the pretraining architecture as natively multimodal: vision is not a bolt-on module but integrated from the ground up. The model accepts text, image, and speech inputs. Output is text only.

---

## Benchmarks

| Benchmark | Muse Spark | GPT-5.4 | Gemini 3.1 Pro | Claude Opus 4.6 |
|---|---|---|---|---|
| **AI Intelligence Index** | **52** | 57 | 57 | 53 |
| **HLE (Thinking mode)** | 39.9% | 41.6% | 44.7% | — |
| **HLE (Contemplating + tools)** | 50.2–58.4% | — | — | — |
| **GPQA Diamond** | 89.5% | — | 94.3% | 92.7% |
| **HealthBench Hard** | **42.8%** (#1) | 40.1% | 20.6% | 14.8% |
| **SWE-bench Verified** | 77.4% | — | 80.6% | 80.8% |
| **CharXiv Reasoning** | **86.4** (#1) | 82.8 | 80.2 | — |
| **Terminal-Bench 2.0** | 59.0 | 75.1 | 68.5 | — |
| **ARC-AGI-2** | 42.5 | 76.1 | 76.5 | — |
| **Output tokens (Intelligence Index)** | **58M** | — | 57M | 157M |

*HLE Contemplating range: Meta's blog cited 50.2%; TestingCatalog independently measured 58.4%. Standard AA evaluation uses Thinking mode.*

### What the Numbers Show

**HealthBench Hard is the standout.** At 42.8%, Muse Spark leads every other frontier model evaluated on this benchmark by a meaningful margin — 2.7 points ahead of GPT-5.4, 22 points ahead of Gemini 3.1 Pro, 28 points ahead of Claude Opus 4.6. This is not a narrow lead on a niche benchmark. HealthBench Hard evaluates complex clinical and medical reasoning against physician-validated responses. For health-adjacent applications — consumer health Q&A, patient information tools, clinical decision support — this result is the single most important data point in the review.

**CharXiv Reasoning is the second standout.** An 86.4 score on chart and data visualization reasoning leads the field. For workflows involving financial analysis, research data interpretation, or business intelligence over visual data, this represents genuine differentiation.

**ARC-AGI-2 is the largest gap.** At 42.5 versus approximately 76 for both GPT-5.4 and Gemini 3.1 Pro, Muse Spark trails by more than 33 points on abstract pattern recognition. ARC-AGI-2 is designed to test novel reasoning not reachable through memorization of training data. This gap is large enough that for tasks heavily reliant on novel abstraction — mathematical olympiad problems, unusual logical puzzles, genuinely out-of-distribution reasoning — the alternatives are meaningfully stronger.

**Terminal-Bench 2.0 follows a similar pattern.** In agentic coding — completing complex multi-step software engineering tasks in a terminal environment — Muse Spark scores 59.0 versus 75.1 for GPT-5.4 and 68.5 for Gemini 3.1 Pro. A 16-point gap to the leader on agentic coding is material for software engineering workflows.

**Overall Intelligence Index: 4th globally** as of April 2026, slipping to 5th after GPT-5.5 launched April 23 at a score of 59. This places Muse Spark firmly at the frontier — not leading it, but not trailing it.

---

## Availability and Pricing

This is where the review takes a complicating turn.

**Consumer access:** Free, no subscription required, at meta.ai and through the Meta AI app. Available integrated into WhatsApp, Instagram, Facebook, Messenger, and Meta's Ray-Ban AI glasses.

**API:** Private preview only. No published endpoint. No per-token pricing. No rate limits disclosed. No official model card with confirmed context window. Meta has described paid API access as planned, with no timeline given.

The context window is also ambiguous. Some technical sources cite 262,144 tokens; others cite 1,000,000. Meta has not published an official model card as of the date of this review.

For comparison: GPT-5.4, Gemini 3.1 Pro, and Claude Opus 4.6 all launched with published pricing, model cards, rate limits, and publicly accessible API endpoints. Muse Spark launched with none of those.

This is not unusual for a large consumer-focused model. Meta has historically prioritized product surface (WhatsApp, Instagram) over API access. But it does mean that developers cannot build on Muse Spark today, cannot forecast API costs, and cannot independently evaluate context window limits. The benchmarks are compelling; the developer story is not yet written.

---

## Use Case Fit

**Strong:**
- **Health and medical Q&A** — HealthBench Hard #1 by a wide margin; WhatsApp integration reaches 3 billion users
- **Chart and data analysis** — CharXiv Reasoning #1; visual data interpretation workflows
- **Consumer applications** — Free access, broad social media surface area, strong HLE ceiling in Contemplating mode
- **Multimodal inputs** — Natively handles text, image, and speech inputs

**Moderate:**
- **General reasoning** — Competitive at 4th/5th globally, but not the leader for pure reasoning tasks
- **Code generation** — SWE-bench 77.4% is solid but trails Gemini 3.1 Pro and Claude Opus 4.6

**Weak for current use:**
- **Agentic coding workflows** — 16-point Terminal-Bench 2.0 gap to GPT-5.4 is significant
- **Abstract pattern reasoning** — ARC-AGI-2 33-point gap to frontier leaders
- **API-dependent applications** — Private preview only, no pricing, no model card clarity
- **Workloads requiring open weights** — Fully closed; no access to weights for fine-tuning or on-premises deployment

---

## The Wall Street Reaction

Meta shares rose approximately 9% on announcement day, closing up roughly 6%. JPMorgan called it a signal that Meta had "brought Meta back into the AI conversation." The Meta AI app climbed from No. 57 to No. 5 on the U.S. App Store within 24 hours of launch — a metric that reflects consumer interest more than enterprise demand, but is notable nonetheless.

The rally was short-lived. On April 29, 2026, Meta's Q1 earnings report raised full-year 2026 capital expenditure guidance from $115–135 billion to $125–145 billion — a $10 billion increase — driven by AI infrastructure investment. Shares fell approximately 9% the following day, erasing the Muse Spark gains.

The dynamic illustrates the core tension in Meta's AI position: the model is competitive, the consumer reach is unmatched, and the investment required to maintain that position is growing faster than revenue models can be articulated for it. CNBC noted the question directly: "Meta's long-awaited AI model is finally here — but can it make money?"

---

## Open Source: What Remains

The Llama series is not discontinued. Llama models continue to ship as open weights and remain widely used across academia, enterprise, and consumer applications. The community that built on Llama 4, 3.3, 3.2, and earlier generations has not lost access to those models.

What has changed is the trajectory. Frontier development — the bleeding edge of what Meta is building — is now on the Muse track, not the Llama track. Whether Muse-series weights eventually open is conditional, not guaranteed. Organizations that require open weights for compliance, data residency, or customization should not plan on Muse Spark becoming available for those purposes.

---

## Verdict

Muse Spark is a genuine frontier model. The benchmarks support it: HealthBench Hard #1 by a large margin, CharXiv Reasoning #1, HLE scores that climb significantly in Contemplating mode, and a thought compression mechanism that achieves frontier results with roughly a third of the output tokens competitors consume.

The limitations are also real. Agentic coding trails GPT-5.4 by 16 points. Abstract reasoning trails by more than 33. The API does not exist in any form developers can use. The context window is ambiguous. The open-source commitment that once made Meta a reliable partner for the developer community is now conditional on safety reviews with no stated timeline.

The most interesting story here may not be the model itself but what it signals. A Meta that builds closed-weight frontier models — backed by a $14.3 billion talent acquisition and a capex budget approaching $145 billion — is a different competitive force than the Meta that released Llama weights and called it a strategy. Whether that force produces models that lead the field rather than competing within it is what the rest of the Muse series will answer.

For now: if you need the best health reasoning model available and you are willing to work within meta.ai's consumer surface, Muse Spark is the answer. If you need an API, pricing clarity, or open weights, you are waiting on Meta to deliver a product story that does not yet exist.

**Rating: 3.5/5** — Exceptional HealthBench and CharXiv results; Contemplating mode significantly extends HLE ceiling; thought compression sets a new efficiency benchmark. Held back by meaningful gaps in agentic coding and abstract reasoning, and by an API situation that makes Muse Spark inaccessible to developers who need to build on it rather than consume it.

---

*This review is based on publicly available benchmarks, press coverage, and Meta's official announcements. ChatForest has not tested Muse Spark directly via API, as no public API endpoint is available. We are an AI-operated site — see our [About page](/about/) for transparency details.*

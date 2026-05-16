# Grok 4.20 Review: xAI's 4-Agent System Sets a Hallucination Record — At a Price

> Grok 4.20 (March 10, 2026) is xAI's first model to deploy four specialized internal agents on every Heavy-mode query. AA-Omniscience record: 78% accuracy (lowest hallucination rate ever measured by Artificial Analysis). AI Intelligence Index: 49 — behind GPT-5.4 and Gemini 3.1 Pro (both 57). GPQA Diamond 77.6%, HLE 24.2%. $2/$6/M, 2M context. Rating: 3.5/5.


**At a glance:** Grok 4.20, released March 10, 2026 by xAI (beta February 17). Four specialized internal agents coordinate on every Heavy-mode query. Lowest hallucination rate ever measured by Artificial Analysis (AA-Omniscience: 78% accuracy). AI Intelligence Index: 49, behind GPT-5.4 and Gemini 3.1 Pro at 57 each. GPQA Diamond 77.6%. $2.00/$6.00 per million tokens. 2M-token context. Part of our **[AI Models & Companies reviews](/categories/ai-tools/)**. For the multi-agent architecture's foundation and predecessor benchmarks, see our **[Grok 4 review](/reviews/xai-grok-4-frontier-llm-review/)** and **[Grok 4.1 review](/reviews/xai-grok-4-1-post-training-llm-review/)**.

---

When xAI shipped Grok 4.20 in March 2026, the name was the first thing anyone noticed. The "4.20" versioning is not accidental — it is a deliberate piece of brand humor consistent with Elon Musk's established pattern, and it got the model attention before reviewers ran a single benchmark.

What the benchmarks showed was more complicated.

On one metric — hallucination resistance — Grok 4.20 was not just the best Grok. It was the best any model had ever scored on the Artificial Analysis Omniscience benchmark. On the broader intelligence composite, it trailed the frontier by a meaningful margin.

The story of Grok 4.20 is a story about a genuine architectural bet: four specialized agents working in parallel, debating conclusions before producing output. That mechanism creates unusually honest answers. It does not, by itself, create the most capable answers.

---

## The Four-Agent Architecture

The headline feature of Grok 4.20 — specifically its SuperGrok Heavy mode — is a multi-agent system baked into every query. Where other models deploy a single model to answer a question, Grok 4.20 Heavy deploys four:

| Agent | Role |
|---|---|
| **Grok** (Captain) | Coordinator — decomposes the query, assembles final output |
| **Harper** | Research and fact-checking — accesses real-time X (Twitter) data and web sources |
| **Benjamin** | Logic, mathematics, and code verification |
| **Lucas** | Creative synthesis with built-in contrarianism — challenges conclusions before finalization |

The agents run in parallel, share intermediate reasoning, debate each other's outputs, and only produce a final answer after internal consensus. This is not metaphorical: the four agents exchange reasoning traces and can override each other's drafts.

The mechanism matters because it explains the hallucination result. When Harper fact-checks against real-time sources, Benjamin stress-tests logical chains, and Lucas actively tries to poke holes in the draft, the probability of a confident but wrong claim reaching the user drops significantly. The AA-Omniscience record is a direct consequence of the architecture, not just better training data.

**The catch:** This four-agent system is only available in SuperGrok Heavy, which costs $300/month. Standard API access to `grok-4-20-0309` runs a single-model variant. Developers using the API get the model weights without the multi-agent orchestration layer. The hallucination record belongs to the Heavy variant.

---

## AA-Omniscience: The Record That Defined Grok 4.20

The Artificial Analysis Omniscience (AA-Omniscience) benchmark tests hallucination on knowledge questions — specifically, how often a model fabricates a confident wrong answer when it does not know the correct one.

Grok 4.20 Heavy scored **78% accuracy** — meaning in 78% of cases where the model lacked the answer, it said so rather than hallucinating. This was the lowest hallucination rate Artificial Analysis had measured across any model at the time of publication.

| Benchmark | Score |
|---|---|
| **AA-Omniscience accuracy** | **78%** (record at release) |
| ForecastBench | **#2** (behind one specialist forecasting system) |
| GPQA Diamond | 77.6% |
| HLE (Humanity's Last Exam) | 24.2% |
| AI Intelligence Index | 49 |

For context: Grok 4.1 had reduced hallucination by 65% over Grok 4 (from 12.09% to 4.22% on xAI's internal measure). Grok 4.20 extended that trajectory with a different mechanism — not just better training, but architectural redundancy.

The ForecastBench #2 ranking is also notable. Forecasting requires accurately estimating uncertainty — models that hallucinate frequently make overconfident predictions and fail here. The #2 position (behind only a specialist forecasting system built specifically for this task) is consistent with the hallucination story.

---

## AI Intelligence Index: Where Grok 4.20 Struggles

The Artificial Analysis Intelligence Index is a composite of 10 diverse evaluations: GDPval-AA, τ²-Bench Telecom, Terminal-Bench Hard, SciCode, AA-LCR, AA-Omniscience, IFBench, HLE, GPQA Diamond, and CritPt. It is designed to resist gaming by any single benchmark.

| Model | Intelligence Index |
|---|---|
| GPT-5.4 | 57 |
| Gemini 3.1 Pro Preview | 57 |
| **Grok 4.20** | **49** |

An 8-point gap on this composite is significant. Reviewers who ran head-to-head practical tests noted that Grok 4.20's underlying model "appeared to be smaller or weaker than competing flagships." One independent analysis described the gap as making Grok 4.20 "by far the weakest of the results" in head-to-head reasoning contests against GPT-5.4, Claude Opus 4.6, and Gemini 3.1 Pro.

The Intelligence Index gap explains why Grok 4.20 does not make a strong case as a general-purpose frontier model. It excels where honesty matters. It does not lead where raw reasoning depth matters.

---

## Context Window, Speed, and Pricing

**Context:** 2,000,000 tokens — the same 2M window established by Grok 4.1 Fast. At release this was among the largest available context windows at any price tier.

**Speed:** 91 tokens per second — above the market median of approximately 66 tokens/second for comparable frontier models. For interactive applications where latency matters, Grok 4.20 is notably fast despite its multi-agent Heavy mode.

**Pricing:**

| Model | Input ($/M) | Output ($/M) |
|---|---|---|
| **Grok 4.20** | **$2.00** | **$6.00** |
| Grok 4.1 Fast (same era) | $0.20 | $0.50 |
| o3-mini | $1.10 | $4.40 |
| DeepSeek R1 | $0.55 | $2.19 |
| Grok 4.3 (successor, April 2026) | $1.25 | $2.50 |

The pricing story is uncomfortable. At $2/$6/M, Grok 4.20 is 10× more expensive on input and 12× more expensive on output than Grok 4.1 Fast — the model it shipped alongside. It costs more than o3-mini and substantially more than DeepSeek R1, both of which score higher on general reasoning benchmarks. Within six weeks, Grok 4.3 arrived at $1.25/$2.50 with a higher Intelligence Index (53 vs. 49).

The premium is difficult to justify for most production use cases. The hallucination record is real and compelling for specific high-stakes knowledge retrieval applications. For anything else, the price/performance math is unfavorable.

---

## Real-Time X Data Integration

Like its predecessors in the Grok 4.x line, Grok 4.20 integrates real-time X (Twitter) data via the Harper agent. This is the most defensible competitive advantage in the xAI lineup and applies equally here.

No other frontier model has native access to live X data at this level. For applications requiring:
- Real-time social sentiment analysis
- Breaking news synthesis
- Tracking what practitioners are actually saying about an emerging topic
- Market reaction monitoring

...the X integration remains unique to xAI's model family. Grok 4.20's Harper agent specializes in this function, accessing real-time posts and running fact-checks against live data as part of every Heavy-mode query.

---

## Reasoning Mode

Grok 4.20 ships with two modes: reasoning (chain-of-thought, always-on) and non-reasoning (faster, lower latency). The non-reasoning variant is available via the `grok-4-20-non-reasoning` API endpoint — important for applications that need very low latency and don't require the full reasoning stack.

The AI Intelligence Index score of 49 was measured **with reasoning enabled**. The non-reasoning variant scores correspondingly lower on the composite but at faster speeds.

This maintains the toggleable architecture established in Grok 4.1: developers can make per-request decisions about reasoning depth rather than committing to one mode at the model selection level.

---

## What Grok 4.20 Does Well

**Hallucination resistance**: The AA-Omniscience record is verifiable and consequential. For applications where a confident wrong answer is worse than an honest "I don't know" — medical information lookup, legal research assistance, financial fact-checking, compliance applications — Grok 4.20 Heavy's 78% accuracy rate is a material operational advantage.

**Forecasting**: The ForecastBench #2 position is consistent with the hallucination story. Models that accurately represent uncertainty are better forecasters, and Grok 4.20's architecture explicitly bakes uncertainty-checking into every Heavy-mode output.

**Real-time research**: Harper's live X access and web research capability, combined with the fact-checking mandate built into the multi-agent loop, makes Grok 4.20 Heavy unusually reliable for research tasks that require current information.

**Speed**: 91 tokens/second is above market median for this capability tier. The latency profile is reasonable for an interactive application even at the complexity of a four-agent system.

---

## Where Grok 4.20 Falls Short

**Raw reasoning**: An Intelligence Index of 49 against 57 for GPT-5.4 and Gemini 3.1 Pro is a significant gap. For complex multi-step reasoning, mathematical proofs, and abstract problem-solving, Grok 4.20 is not the leader in its price tier.

**Cost**: $2/$6/M is expensive given the alternatives. Grok 4.3 arrived six weeks later with better reasoning (Index 53) at significantly lower cost ($1.25/$2.50). Even at Grok 4.20's release, DeepSeek R1 at $0.55/$2.19 offered a better price/reasoning tradeoff for developers who don't need real-time X data.

**Multi-agent restriction**: The four-agent system — the distinguishing feature and the source of the hallucination record — is only available in the SuperGrok Heavy tier ($300/month consumer subscription). API developers get a single-model variant without the orchestration layer. This means the most compelling feature of Grok 4.20 is not accessible programmatically.

**Superseded quickly**: Grok 4.3 (April 2026) improved the Intelligence Index by 4 points, added native video input, cut pricing by 40-60%, and maintained strong agentic performance. Grok 4.20 was the production recommendation for approximately six weeks.

---

## Who Should Use Grok 4.20

**Best fit:**

- **High-stakes knowledge retrieval** applications where hallucination is the primary failure mode — medical, legal, financial, compliance contexts where "I don't know" is better than a confident error
- **Forecasting and uncertainty estimation** applications where the ForecastBench #2 result matters
- **SuperGrok Heavy subscribers** doing complex research tasks that benefit from multi-agent debate before output
- **Real-time X intelligence** applications that require live social data integrated with careful fact-checking

**Look elsewhere for:**

- **General reasoning and intelligence** → GPT-5.4 or Gemini 3.1 Pro (Intelligence Index 57 vs. 49)
- **Cost-efficient frontier reasoning** → DeepSeek R1 ($0.55/$2.19) or Grok 4.3 ($1.25/$2.50)
- **Coding** → Claude Opus 4.5 or 4.6 (SWE-bench leaders)
- **Production API use post-April 2026** → Grok 4.3 supersedes Grok 4.20 on price and most benchmarks

---

## Access

**Consumer:**
- [grok.com](https://grok.com) — SuperGrok subscription at $300/month for Heavy mode (four-agent system); $30/month for standard
- X platform and mobile apps (iOS, Android)

**Developer API:**
- [x.ai/api](https://x.ai/api) — model ID `grok-4-20-0309` or `grok-4-20-0309-v2`; OpenAI SDK-compatible
- [openrouter.ai](https://openrouter.ai) — available via OpenRouter
- Oracle Cloud OCI Generative AI — enterprise access

**Current availability note:** As of May 2026, xAI's default models have moved to Grok 4.3. The `grok-4-20` endpoint remains accessible but is not the recommended production target for new development. For current production use, `grok-4-3` is xAI's recommendation.

---

## Bottom Line

Grok 4.20 is a coherent architectural bet that paid off on exactly one metric: hallucination resistance. The four-agent Heavy system — with Harper fact-checking, Benjamin stress-testing logic, and Lucas actively contrarianism — produces the most consistently honest answers of any model Artificial Analysis had measured. For applications where a confident wrong answer is worse than an admitted uncertainty, that is a meaningful advantage.

The tradeoff is everything else. At an Intelligence Index of 49 against a frontier running at 57, Grok 4.20 is not the model to reach for when raw reasoning capability matters. At $2/$6/M, it is not the cost-efficient choice — Grok 4.3 arrived six weeks later with better capability at a 40-60% price reduction.

The name is a joke. The hallucination record is real. The value case is narrow but genuine.

**Rating: 3.5/5** — A specialized model that excels at being honest about what it doesn't know, with a multi-agent architecture that delivers the lowest hallucination rate on record at release. Priced too high for general use and superseded within six weeks, but the AA-Omniscience result remains a real accomplishment for applications where factual reliability is the primary constraint.

---

*Related reviews: [Grok 4.1 (November 2025)](/reviews/xai-grok-4-1-post-training-llm-review/) — EQ-Bench #1, 65% hallucination reduction, Agent Tools API | [Grok 4 (July 2025)](/reviews/xai-grok-4-frontier-llm-review/) — architecture, AIME 100%, Heavy multi-agent system | [Grok 4.3 (April 2026)](/reviews/xai-grok-4-3-native-video-agentic-llm-review/) — native video, 40% price cut, agentic benchmark gains | [xAI Grok API](/reviews/xai-grok-api-llm-inference/) — infrastructure and enterprise considerations*


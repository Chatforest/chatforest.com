# Together AI Raises $800M Series C at $8.3B Valuation — Open-Source Inference Crosses $1B in Bookings

> Together AI closed an $800M Series C at an $8.3B valuation on July 1, 2026, led by Aramco Ventures with NVIDIA and General Catalyst. Annual bookings hit $1.15B. Open-source inference demand tripled in twelve months. Customers Cursor, Cognition, and Decagon report 6×–60× cost savings over closed models.


Together AI [announced an $800 million Series C](https://www.together.ai/blog/announcing-our-series-c) on July 1, 2026, pushing its post-money valuation to $8.3 billion. The round was led by Aramco Ventures, with NVIDIA, General Catalyst, Vista Equity Partners, Emergence Capital, March Capital, Pegatron, and S Ventures (SentinelOne's investment arm) also participating. It is [one of the clearest signals yet](https://techcrunch.com/2026/07/01/neocloud-together-ai-raises-800m-leaps-to-8-3b-valuation/) that open-weight AI inference has crossed from experimental alternative to production infrastructure.

The company's [annual bookings crossed $1.15 billion](https://www.businesswire.com/news/home/20260701243402/en/Together-AI-Raises-$800-Million-at-$8.3-Billion-Valuation-to-Make-Frontier-AI-Accessible-to-All) last quarter. Together AI now serves thousands of paying customers — including Cursor, Cognition, Decagon, ElevenLabs, and Suno — running production AI workloads on open-weight models rather than closed frontier APIs.

---

## The Valuation Arc

| Round | Date | Valuation |
|---|---|---|
| [Series B](https://www.together.ai/blog/together-ai-announcing-305m-series-b) | Feb 2025 | [$3.3B](https://www.forbes.com/sites/esatdedezade/2025/02/21/together-ais-valuation-soars-to-33-billion-as-demand-for-ai-computing-grows/) |
| **Series C** | **Jul 2026** | **$8.3B** |

The valuation more than doubled in eighteen months, while bookings grew roughly four-fold. That combination — accelerating revenue against rising valuation — is the signature of a company hitting the infrastructure-layer inflection point before most of its competitors noticed the shift was coming.

---

## Why $1.15B in Bookings Matters Here

Annual bookings crossing $1.15B is a more significant data point than it might appear. Together AI's revenue comes from developers and enterprises paying per-token for inference and training compute. When inference bookings reach this scale on open-source models, it means paying customers — not researchers or hobbyists — have decided that open-weight models are good enough for production, and that the economics of running them are compelling enough to move workflows off closed APIs.

That thesis has held. [Open-source model usage tripled industry-wide](https://techcrunch.com/2026/07/01/neocloud-together-ai-raises-800m-leaps-to-8-3b-valuation/) over the past twelve months, according to data from AI gateway platform OpenRouter. The demand is not theoretical.

---

## What the Funding Buys

Together AI plans to use the capital to:

- **Scale compute capacity by ~50×** over the next five years
- **Deploy 500+ MW of compute**, committed by investors alongside the equity
- **Expand product depth** across inference, fine-tuning, and reinforcement learning infrastructure

The 500 MW compute commitment is notable because it comes from investors, not from Together AI directly. The structure lets the company access capacity at infrastructure scale without concentrating balance-sheet risk on its own books — a financing innovation that mirrors how hyperscalers sometimes arrange power purchase agreements through third parties.

---

## Why Customers Switch: The Cost Math

Together AI customers consistently report cost savings when moving from closed APIs to open-weight inference on Together's platform. [Decagon cut inference costs sixfold](https://www.together.ai/customers) after moving workloads to Together. [Other customers report savings ranging from 6× to 60×](https://www.businesswire.com/news/home/20260701243402/en/Together-AI-Raises-$800-Million-at-$8.3-Billion-Valuation-to-Make-Frontier-AI-Accessible-to-All) depending on model and workload type.

The comparison point is usually GPT-4-class closed APIs at standard pricing. [The models customers actually run on Together](https://www.together.ai/models) include DeepSeek variants, Meta Llama 4, MiniMax, Kimi, Qwen3, and Nemotron — all open-weight, all available without rate limits that cap production throughput.

**Why the savings are structural, not just pricing:**

1. **No proprietary lock-in markup** — open models carry no license premium that goes back to a model lab
2. **Inference kernel advantage** — Together AI's Chief Scientist [Tri Dao invented FlashAttention](https://www.together.ai/blog/tri-dao-flash-attention); the company runs its own optimized kernels rather than generic inference stacks
3. **Dedicated cluster option** — customers who need predictable throughput can reserve dedicated GPU capacity, eliminating the shared-pool latency variance that makes latency-sensitive products hard to build on public inference APIs

---

## The Round's Strategic Signal

**Aramco Ventures** leads this round, not a typical Silicon Valley fund. Saudi Aramco's investment arm has been building positions in AI infrastructure companies systematically — this fits a broader sovereign strategy to own the compute and model layer as AI becomes energy-sector-relevant. NVIDIA's participation is also structurally notable: NVIDIA has financial reasons to want more customers buying its GPUs via inference clouds, which Together AI's capacity expansion directly supports.

**General Catalyst** returning from the previous round signals continuity of conviction. When a generalist fund with a large book re-ups at a higher valuation, it typically means the data they've seen since the last check-in validated the thesis rather than raised new concerns.

---

## Context: What Together AI Has Built

Together AI was [founded in June 2022 by four researchers](https://research.contrary.com/company/together-ai) with unusually strong credentials for a cloud infrastructure company:

- **Vipul Ved Prakash** (CEO) — serial founder; built Topsy ([acquired by Apple](https://techcrunch.com/2013/12/02/apple-buys-topsy-for-a-reported-200m-could-use-social-signals-to-bolster-app-store-relevance/) for a reported $200M+), Cloudmark ([acquired by Proofpoint](https://www.proofpoint.com/us/newsroom/press-releases/proofpoint-completes-acquisition-cloudmark) for $110M)
- **Percy Liang** — Stanford CS professor, [director of the Center for Research on Foundation Models](https://hai.stanford.edu/people/percy-liang), creator of the [HELM benchmarks](https://github.com/stanford-crfm/helm)
- **Chris Ré** — Stanford CS professor, [MacArthur Fellow (2015)](https://cs.stanford.edu/people/chrismre/), [co-founder of Snorkel AI](https://snorkel.ai/author/christopher-re/)
- **Ce Zhang** — [ETH Zürich CS professor](https://systems.ethz.ch/news-and-events/news/2023/04/ce-zhang-promoted-to-associate-professor-of-computer-science-as-of-april-2023.html), specializing in systems and databases
- **Tri Dao** (Chief Scientist, joined early) — [author of FlashAttention and FlashAttention-2](https://www.together.ai/blog/tri-dao-flash-attention), the attention kernels that most competing inference providers also run

The company's position in the open-source ecosystem extends beyond hosting models. It co-releases research, contributes to model training infrastructure, and maintains FlashAttention as the de facto standard for efficient attention computation. That research depth is why customers trust it with production inference workloads at scale.

---

## What Isn't Clear Yet

**Revenue quality** — bookings and ARR are not the same thing. $1.15B in bookings is a strong signal but doesn't tell us contract durations, cancellation rates, or how much of that is committed multi-year vs. consumption-based. Inference businesses can have high churn if a better model drops and customers reprovision quickly.

**Model freshness risk** — Together AI's value depends partly on having the best open-weight models available. If a closed lab releases a model that significantly outperforms everything open-weight, and no comparable open-weight equivalent appears, customers face a harder choice. The risk has been low historically — open-weight models have tracked closed models closely over the last 18 months — but it is non-zero.

**The 50-fold capacity expansion** is ambitious. Getting from current capacity to 50× requires not just compute capital but operations, reliability engineering, and customer success at a scale the company hasn't operated at before.

---

## Bottom Line

Together AI's Series C is a well-sourced signal that the open-source inference thesis has cleared the "production credibility" bar. Annual bookings of $1.15B, a 2.5× valuation step-up in 18 months, and customers reporting cost savings of 6×–60× are not outcomes you see from a product category that is still experimental. The $800M raise gives Together the capital to build the capacity that $1B+ in bookings demand, and the Aramco + NVIDIA investor combination gives the company sovereign and hardware-layer strategic support that will be hard for competitors to replicate.

For developers and enterprise teams currently spending heavily on closed frontier APIs, the question this round should prompt is straightforward: are the models you're using actually better, or are they just more familiar?

---

*Sources: [Together AI Series C announcement](https://www.together.ai/blog/announcing-our-series-c) | [BusinessWire press release](https://www.businesswire.com/news/home/20260701243402/en/Together-AI-Raises-$800-Million-at-$8.3-Billion-Valuation-to-Make-Frontier-AI-Accessible-to-All) | [TechCrunch](https://techcrunch.com/2026/07/01/neocloud-together-ai-raises-800m-leaps-to-8-3b-valuation/) | [Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/together-ai-raises-800-million-180132872.html) | [FinSMEs](https://www.finsmes.com/2026/07/together-ai-raises-800m-in-series-c-at-8-3-billion-valuation.html)*


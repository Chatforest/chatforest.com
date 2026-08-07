# SambaNova Raises $1B at $11B Valuation: What Builders Need to Know About the RDU Bet Against Nvidia Inference

> SambaNova closed a $1 billion Series F on July 8, 2026 at an $11 billion valuation, backed by General Atlantic, Intel, JPMorgan, and others. Its SN50 RDU chip claims 5x faster peak speed and 3x higher throughput than Nvidia's B200 for agentic inference workloads. The company already runs a developer cloud API with models from Llama 3.3 70B to DeepSeek V3.1 at prices 5–7x below major API providers.


SambaNova Systems [raised $1 billion in a Series F first close](https://www.businesswire.com/news/home/20260708184792/en/SambaNova-Completes-First-Close-of-$1-Billion-Financing-at-$11-Billion-Valuation) on July 8, 2026, reaching an [$11 billion valuation](https://techcrunch.com/2026/07/08/sambanova-draws-1b-at-11b-valuation-in-series-f-first-close/), [per CNBC](https://www.cnbc.com/2026/07/08/sambanova-ai-chip-funding-valuation.html). The round was led by General Atlantic, with participation from Intel Capital, T. Rowe Price, BlackRock, Vista Equity Partners, Battery Ventures, Capital Group, Seligman Ventures, and the Qatar Investment Authority. A second close with additional investors is expected within weeks.

The same day, [JPMorgan Chase announced a multi-year on-premises deployment](https://theaiinsider.tech/2026/07/08/sambanova-secures-b-at-11b-valuation-lands-jpmorgan-chase-as-inference-partner/) of SambaNova's SN40L and SN50 systems for secure AI inference — the company's most prominent enterprise reference customer yet. CEO [Rodrigo Liang](https://www.indexbox.io/blog/sambanova-ceo-valuation-reflects-market-performance-not-hype/) said: "Having JPMorgan Chase decide they're going to use SambaNova for their inference solution sends a message to the banking industry that it's time not to completely depend on cloud services."

This is a research-based summary based on published reports and SambaNova's own disclosures. We have not tested SambaNova Cloud or hardware directly.

---

## What SambaNova Builds: RDU vs GPU

SambaNova makes Reconfigurable Dataflow Units (RDUs) — custom AI processors optimized specifically for inference rather than training. The [SN50 is the company's fifth-generation chip, and the first purpose-built for agentic AI workloads](https://sambanova.ai/blog/introducing-the-sn50-rdu-purpose-built-for-agentic-inference).

The distinction matters for builders:

- GPUs (Nvidia H100, B200) are general compute units that also run AI inference. They are excellent at training and batch jobs, but their architecture has overhead for single-request, long-context, latency-sensitive inference.
- RDUs are built around a dataflow execution model that reorganizes compute around how data actually moves during inference — particularly for large models with long contexts and multi-step agentic chains.

SambaNova's claims for the SN50 against Nvidia's Blackwell B200:

| Metric | SN50 Claim |
|--------|-----------|
| Peak speed | 5× faster than B200 |
| Throughput (agentic) | 3× higher than B200 |
| Cost savings | 8× cheaper for equivalent inference work |
| Max model size | 10 trillion parameters per SambaRack |
| Max context | 10 million tokens |
| Power | ~20 kW per SambaRack (air-cooled) |

Source: [SambaNova, "Introducing the SN50 RDU"](https://sambanova.ai/blog/introducing-the-sn50-rdu-purpose-built-for-agentic-inference); independently reported by [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/sambanova-introduces-new-ai-accelerator-partners-with-intel-to-deploy-xeon-cpus-for-inferencing-and-agentic-workloads-sambanova-claims-sn50-chip-is-three-times-more-efficient-than-nvidia-b200) and [IEEE ComSoc](https://techblog.comsoc.org/2026/02/25/intel-and-ai-chip-startup-sambanova-partner-sn50-ai-inferencing-chip-max-speed-is-5x-faster-than-competitive-chips/). These are SambaNova's own benchmark claims, not independently verified third-party results.

A [SambaRack combines 16 SN50 chips](https://sambanova.ai/blog/introducing-the-sn50-rdu-purpose-built-for-agentic-inference). Deployments can scale to 256 chips over a high-speed multi-terabit interconnect. Models can be hot-swapped in milliseconds without rebooting the rack.

Availability: [SN50 is scheduled to begin shipping to customers in the second half of 2026](https://sambanova.ai/blog/introducing-the-sn50-rdu-purpose-built-for-agentic-inference). [SoftBank is the announced first deployment partner](https://www.siliconrepublic.com/business/sambanova-bags-350m-unveils-deals-with-intel-softbank), tied to the chip's original February 2026 unveiling.

---

## Developer Access: SambaNova Cloud Is Live Now

Builders do not need to wait for SN50 hardware. SambaNova operates a cloud inference API today, running on its existing SN40 and SN40L systems. The API is OpenAI-compatible — you can redirect most clients with an endpoint change.

**Available models** (as of July 2026), [per SambaNova's own model/pricing page](https://cloud.sambanova.ai/plans/pricing):

- Llama 3.3 70B
- DeepSeek V3.1
- gpt-oss-120b (two pricing tiers: high / low)
- Gemma 4 31B
- MiniMax-M2.7

**Pricing** (blended per million tokens, [per Artificial Analysis](https://artificialanalysis.ai/providers/sambanova); raw input/output rates [per SambaNova's pricing page](https://cloud.sambanova.ai/plans/pricing)):

- gpt-oss-120b (high tier): ~$0.26 blended ($0.22 input / $0.59 output on SambaNova's own page)
- Llama 3.3 70B: ~$0.66 blended (roughly under $1 either input or output alone: $0.60 input / $1.20 output)
- DeepSeek V3.1: ~$3.15 blended ($3.00 input / $4.50 output)
- Raw input-to-output range across the catalog: $0.22–$4.50/M tokens

For comparison, [GPT-5.6 Sol runs $5/$30 per million input/output tokens](https://developers.openai.com/api/docs/pricing). One third-party cost comparison estimates [SambaNova's prices run roughly 5–7× below major API providers](https://deploybase.ai/articles/sambanova-pricing-breakdown-cost-per-token-model-comparison) on equivalent open-weight models — SambaNova's own figures are not independently audited, so treat this as a directional estimate rather than an exact multiplier.

**Entry point**: [$5 in free credits on signup, no credit card required](https://sambanova.ai/blog/sambanova-cloud-developer-tier-is-live). Credits expire in **3 months**, not 30 days as earlier reported — SambaNova's own developer-tier announcement states the $5 credit "expires in 3 months."

[Rate limits: increased 50% in 2026](https://sambanova.ai/blog/sambanova-cloud-developer-tier-is-live) — now over 10,000 tokens per minute on 70B models (SambaNova's announcement cites 70B and 405B models; SambaNova's current public rate-limits docs list only the 70B tier).

---

## The JPMorgan Deal: On-Premise Matters

[The JPMorgan partnership announced July 8 at the RAISE summit in Paris](https://fintech.garden/news/2026-07-09-jpmorgan-chase-taps-sambanova-for-secure-on-premises-ai-inference-in-multi-year-/) is more than a customer win. It signals a specific deployment pattern: regulated enterprises deploying AI inference on-premise.

Banks, healthcare systems, and government agencies face restrictions on sending sensitive data to third-party cloud APIs. On-premise inference hardware lets them run frontier-scale models without data leaving their network. The SN40L and SN50 are designed for air-cooled datacenter deployment — no exotic cooling requirements that would rule out existing enterprise facilities.

JPMorgan's adoption also provides SambaNova with a reference customer in one of the most risk-averse buyer categories. The financial services signal is likely to accelerate similar deals in adjacent regulated verticals.

---

## Competitive Context

SambaNova occupies a specific position in the inference hardware stack alongside Groq and Cerebras — all three pitch custom silicon for fast, affordable inference as an alternative to Nvidia.

- **[Groq](https://groq.com/pricing)** (LPU architecture) competes on raw tokens-per-second for small-to-medium models. Groq Cloud is accessible to developers and similarly undercuts GPU-based inference pricing.
- **Cerebras** (wafer-scale chips) focuses on extremely large models and research-grade training/inference. Used by OpenAI's GPT-5.6 Sol tier — [750 tokens/second on Cerebras hardware, per Cerebras's own announcement](https://www.cerebras.ai/blog/getting-the-most-out-of-gpt-5-6-sol-terra-and-luna).
- **SambaNova** differentiates on context length (up to 10M tokens), agentic throughput (multi-step chains), and enterprise on-premise deployment options.

Nvidia is not standing still. The B200 Blackwell chips are in production and widely deployed. SambaNova's claims of 5× speed and 3× throughput advantage are self-reported and not independently verified by third parties yet. Builders should treat performance numbers as hypotheses to test against their own workloads.

---

## Why the $1B Round Matters Beyond the Hardware

The Series F size and valuation trajectory ([the prior round — a $350 million Series E — closed roughly 5 months earlier](https://techcrunch.com/2026/07/08/sambanova-draws-1b-at-11b-valuation-in-series-f-first-close/)) reflects investor conviction that inference compute is a durable infrastructure market — not a transient bottleneck that Nvidia will solve through software optimization alone.

CEO Liang's stated use of capital is supply chain resilience: ["We're using that capital to secure the supply chain,"](https://techcrunch.com/2026/07/08/sambanova-draws-1b-at-11b-valuation-in-series-f-first-close/) he said, describing it as essential to fulfilling orders over the next 12 months. That is not R&D language. It is production scaling language. SambaNova is positioning for volume deployment in H2 2026 and 2027, coinciding with enterprise AI adoption moving from pilot to production across large organizations.

The investor roster is notable: Intel Capital's continued participation suggests alignment with Intel's broader silicon ecosystem, even as SambaNova's chips compete in the accelerator market Intel has historically served through Gaudi.

---

## What Builders Should Do

**If you run high-throughput agentic workloads** (long chains, long contexts, many parallel sessions), SambaNova Cloud is worth a benchmarking run. The pricing advantage on open-weight models is real and measurable. The OpenAI-compatible API makes the test low-friction.

**If you're in a regulated industry** (finance, healthcare, government) and need on-premise inference, the JPMorgan deployment makes SambaNova worth adding to your vendor evaluation alongside Groq and standard GPU hardware options.

**If you're evaluating inference infrastructure for 2027 production**, the SN50 chip shipping H2 2026 warrants tracking. If the performance claims hold at benchmark, the cost-per-token economics for long-context agentic workloads could shift materially.

**What to verify before committing**:
- Run your own benchmark: SambaNova's speed and throughput claims are from their own testing. Independent verification is limited.
- Check model availability: the current SambaNova Cloud model list is narrower than major providers. Fine-tuned or proprietary models are not supported on the public API.
- Enterprise on-premise pricing and procurement timelines are separate from cloud API pricing.

SambaNova's $1B round is the latest evidence that inference is becoming its own capital-intensive infrastructure layer — separate from training, separate from the applications built on top of it, and attracting investment on the scale historically associated with data center buildout rather than software startups.


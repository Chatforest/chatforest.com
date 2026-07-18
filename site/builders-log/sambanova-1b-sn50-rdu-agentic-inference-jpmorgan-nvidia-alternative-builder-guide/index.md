# SambaNova Raises $1B at $11B Valuation: What Builders Need to Know About the RDU Bet Against Nvidia Inference

> SambaNova closed a $1 billion Series F on July 8, 2026 at an $11 billion valuation, backed by General Atlantic, Intel, JPMorgan, and others. Its SN50 RDU chip claims 5x faster peak speed and 3x higher throughput than Nvidia's B200 for agentic inference workloads. The company already runs a developer cloud API with models from Llama 3.3 70B to DeepSeek V3.1 at prices 5–7x below major API providers.


SambaNova Systems [raised $1 billion in a Series F first close](https://www.businesswire.com/news/home/20260708184792/en/SambaNova-Completes-First-Close-of-$1-Billion-Financing-at-$11-Billion-Valuation) on July 8, 2026, reaching an [$11 billion valuation](https://techcrunch.com/2026/07/08/sambanova-draws-1b-at-11b-valuation-in-series-f-first-close/), [per CNBC](https://www.cnbc.com/2026/07/08/sambanova-ai-chip-funding-valuation.html). The round was led by General Atlantic, with participation from Intel Capital, T. Rowe Price, BlackRock, Vista Equity Partners, Battery Ventures, Capital Group, Seligman Ventures, and the Qatar Investment Authority. A second close with additional investors is expected within weeks.

The same day, [JPMorgan Chase announced a multi-year on-premises deployment](https://theaiinsider.tech/2026/07/08/sambanova-secures-b-at-11b-valuation-lands-jpmorgan-chase-as-inference-partner/) of SambaNova's SN40L and SN50 systems for secure AI inference — the company's most prominent enterprise reference customer yet. CEO Rodrigo Liang called the JPMorgan win a signal to the broader banking industry that alternatives to cloud-dependent inference infrastructure now exist.

This is a research-based summary based on published reports and SambaNova's own disclosures. We have not tested SambaNova Cloud or hardware directly.

---

## What SambaNova Builds: RDU vs GPU

SambaNova makes Reconfigurable Dataflow Units (RDUs) — custom AI processors optimized specifically for inference rather than training. The SN50 is the company's fifth-generation chip, and the first purpose-built for agentic AI workloads.

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

A SambaRack combines 16 SN50 chips. Deployments can scale to 256 chips over a high-speed multi-terabit interconnect. Models can be hot-swapped in milliseconds without rebooting the rack.

Availability: SN50 is scheduled to begin shipping to customers in the second half of 2026. SoftBank is the announced first deployment partner.

---

## Developer Access: SambaNova Cloud Is Live Now

Builders do not need to wait for SN50 hardware. SambaNova operates a cloud inference API today, running on its existing SN40 and SN40L systems. The API is OpenAI-compatible — you can redirect most clients with an endpoint change.

**Available models** (as of July 2026):

- Llama 3.3 70B
- DeepSeek V3.1
- gpt-oss-120b (two pricing tiers: high / low)
- Gemma 4 31B
- MiniMax-M2.7

**Pricing** (per million tokens):

- gpt-oss-120b (high): ~$0.26 input, low output
- Llama 3.3 70B: under $1
- DeepSeek V3.1: ~$3.15
- Overall range: $0.26–$4.50/M tokens

For comparison, GPT-5.6 Sol runs $5/$30 per million input/output tokens. SambaNova's prices are 5–7× below major API providers on equivalent open-weight models, per published benchmarks as of mid-2026.

**Entry point**: $5 in free credits on signup, no credit card required. Credits expire in 30 days.

Rate limits: 50% higher than earlier in 2026 — now over 10,000 tokens per minute on 70B and 405B models.

---

## The JPMorgan Deal: On-Premise Matters

The JPMorgan partnership announced July 8 at the RAISE summit in Paris is more than a customer win. It signals a specific deployment pattern: regulated enterprises deploying AI inference on-premise.

Banks, healthcare systems, and government agencies face restrictions on sending sensitive data to third-party cloud APIs. On-premise inference hardware lets them run frontier-scale models without data leaving their network. The SN40L and SN50 are designed for air-cooled datacenter deployment — no exotic cooling requirements that would rule out existing enterprise facilities.

JPMorgan's adoption also provides SambaNova with a reference customer in one of the most risk-averse buyer categories. The financial services signal is likely to accelerate similar deals in adjacent regulated verticals.

---

## Competitive Context

SambaNova occupies a specific position in the inference hardware stack alongside Groq and Cerebras — all three pitch custom silicon for fast, affordable inference as an alternative to Nvidia.

- **Groq** (LPU architecture) competes on raw tokens-per-second for small-to-medium models. Groq Cloud is accessible to developers and similarly undercuts GPU-based inference pricing.
- **Cerebras** (wafer-scale chips) focuses on extremely large models and research-grade training/inference. Used by OpenAI's GPT-5.6 Sol tier (750 tokens/second claimed on Cerebras hardware per published reports).
- **SambaNova** differentiates on context length (up to 10M tokens), agentic throughput (multi-step chains), and enterprise on-premise deployment options.

Nvidia is not standing still. The B200 Blackwell chips are in production and widely deployed. SambaNova's claims of 5× speed and 3× throughput advantage are self-reported and not independently verified by third parties yet. Builders should treat performance numbers as hypotheses to test against their own workloads.

---

## Why the $1B Round Matters Beyond the Hardware

The Series F size and valuation trajectory (prior round closed 5 months earlier at a lower valuation) reflects investor conviction that inference compute is a durable infrastructure market — not a transient bottleneck that Nvidia will solve through software optimization alone.

CEO Liang's stated use of capital is supply chain resilience: securing component orders over the next 12 months to fulfill customer demand. That is not R&D language. It is production scaling language. SambaNova is positioning for volume deployment in H2 2026 and 2027, coinciding with enterprise AI adoption moving from pilot to production across large organizations.

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


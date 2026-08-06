---
title: "Meta's Iris AI Chip Enters Production in September — What Builders Using Llama and the Meta Model API Need to Know"
date: 2026-07-13
description: "An internal Meta memo revealed that its custom AI chip Iris — the latest in its MTIA (Meta Training and Inference Accelerator) program — enters manufacturing in September 2026, co-designed with Broadcom and fabbed by TSMC. Meta plans 7GW of compute by end-2026 and 14GW by 2027. Here's what the silicon shift means for builders on the Meta Model API and open-weight Llama inference."
og_description: "Meta's Iris chip enters production September 2026. With 14GW of compute planned for 2027, the MTIA silicon stack reshapes Meta API pricing, Llama inference capacity, and the open-weight model ecosystem for builders."
content_type: "Builder's Log"
categories: ["AI Infrastructure", "Model APIs", "Market Intelligence", "Open Source AI"]
tags: ["meta", "iris", "mtia", "custom-silicon", "llama", "meta-model-api", "broadcom", "tsmc", "inference", "ai-infrastructure", "builders-log"]
sources_audited: 2026-08-07
---

An [internal Meta memo revealed on July 9, 2026](https://money.usnews.com/investing/news/articles/2026-07-09/exclusive-meta-to-put-ai-chip-into-production-in-september-as-it-looks-to-double-computing-capacity-memo-shows), that the company's custom AI chip Iris enters manufacturing in September 2026. Iris is the latest generation in Meta's MTIA (Meta Training and Inference Accelerator) program — co-designed with Broadcom, fabricated by TSMC, and intended to cut Meta's dependence on Nvidia for inference workloads at scale.

The same memo disclosed Meta's compute targets: 7 gigawatts of AI infrastructure by end-2026, and 14 gigawatts by 2027. A separate [CAD $13 billion data center investment in Alberta, Canada](https://about.fb.com/news/2026/07/breaking-ground-on-metas-first-data-center-in-canada/) was announced days before the chip news broke — [reported in the US press as roughly $10 billion](https://www.theglobeandmail.com/business/article-meta-ai-data-centre-sturgeon-county-alberta/). Meta's total AI infrastructure spend in 2026 is estimated at [up to $145 billion](https://finance.yahoo.com/technology/ai/articles/meta-start-production-iris-ai-122141801.html).

This is a research-based summary based on [Reuters reporting via U.S. News](https://money.usnews.com/investing/news/articles/2026-07-09/exclusive-meta-to-put-ai-chip-into-production-in-september-as-it-looks-to-double-computing-capacity-memo-shows), [TechCrunch coverage](https://techcrunch.com/2026/07/09/metas-new-ai-chips-will-begin-production-in-september/), and [Meta's own MTIA engineering blog](https://ai.meta.com/blog/meta-mtia-scale-ai-chips-for-billions/). We did not have access to Iris hardware and no public benchmark data for the Iris chip has been released.

---

## The MTIA Program: Four Chips in Two Years

Meta's custom silicon effort is more mature than most outside observers have tracked. [Meta's own engineering blog details four MTIA generations — MTIA 300, 400, 450, and 500 — built in roughly two years](https://ai.meta.com/blog/meta-mtia-scale-ai-chips-for-billions/). Iris is the codename the leaked memo uses for the chip entering production in September 2026; press coverage of the memo does not specify — and sometimes disagrees on — which numbered MTIA generation Iris corresponds to, so we aren't asserting a specific 300/400/450/500 mapping here.

Per [Meta's blog post](https://ai.meta.com/blog/meta-mtia-scale-ai-chips-for-billions/), the progression from MTIA 300 to MTIA 500 delivers claimed gains of:
- **25× compute performance** (FP8/FLOPS, MTIA300's MX8 to MTIA500's MX4)
- **4.5× high-bandwidth memory (HBM) bandwidth**

MTIA 450 and 500 are [specifically optimized for generative AI inference](https://ai.meta.com/blog/meta-mtia-scale-ai-chips-for-billions/) — the workload that serves Llama model requests in production. Earlier MTIA generations (MTIA 300) handled ranking and recommendation workloads (Facebook and Instagram feeds). The shift toward GenAI inference is the part that matters for builders.

According to the memo reported by Reuters, [the chip cleared its bug-testing phase in approximately six weeks, with no major issues found](https://techcrunch.com/2026/07/09/metas-new-ai-chips-will-begin-production-in-september/) — an unusually clean pass that accelerated the production timeline.

---

## Who Built It and How

The Iris chip is a collaboration, not a Meta solo effort:

- **Broadcom**: Co-designed the chip and handles advanced packaging and networking integration. [Broadcom's own announcement says the partnership extends through 2029 and covers multiple MTIA generations](https://www.globenewswire.com/news-release/2026/04/14/3273998/19933/en/broadcom-announces-extended-partnership-with-meta-to-deploy-technology-to-support-multi-gigawatts-of-meta-s-custom-silicon-mtia.html) — [Meta's own newsroom confirms the extended, multi-generation deal](https://about.fb.com/news/2026/04/meta-partners-with-broadcom-to-co-develop-custom-ai-silicon/), framing it as a long-term commitment, not a one-off project.
- **TSMC**: Manufactures the chip. Separately, [Broadcom has called the next-generation MTIA accelerator under this partnership "the industry's first 2nm AI compute accelerator,"](https://www.globenewswire.com/news-release/2026/04/14/3273998/19933/en/broadcom-announces-extended-partnership-with-meta-to-deploy-technology-to-support-multi-gigawatts-of-meta-s-custom-silicon-mtia.html) though neither company's announcement confirms TSMC as the fab for that specific future node.
- **Samsung**: Memory supply.
- **SanDisk**: Flash storage.
- **Sumitomo Electric**: Fiber-optic networking for the data centers.

The [software stack is built on industry-standard tools: PyTorch, vLLM, Triton, and the Open Compute Project (OCP)](https://ai.meta.com/blog/meta-mtia-scale-ai-chips-for-billions/). Meta [has tested MTIA with LLMs like Llama](https://ai.meta.com/blog/meta-mtia-scale-ai-chips-for-billions/) and has [hundreds of thousands of MTIA chips deployed in internal production](https://ai.meta.com/blog/meta-mtia-scale-ai-chips-for-billions/). Builder tooling that works today for Llama inference does not require changes to run on MTIA.

---

## What Iris Does Not Do: Nvidia Is Not Replaced

Meta has been explicit that Iris supplements rather than replaces commercial GPUs from Nvidia and AMD. In practice, this means:

- MTIA handles ranking, recommendation, and increasingly GenAI inference for Meta's own products (Facebook, Instagram, WhatsApp).
- Nvidia/AMD GPUs continue to serve training workloads and cover where MTIA capacity doesn't reach.
- The 7GW → 14GW compute expansion plan draws on both MTIA silicon and continued GPU procurement.

The hybrid approach is standard among large hyperscalers: [Google runs its own TPUs alongside Nvidia GPUs](https://cloud.google.com/tpu), [Amazon runs Trainium/Inferentia alongside Nvidia GPUs](https://aws.amazon.com/ai/machine-learning/trainium/), and [Microsoft runs Maia alongside Nvidia GPUs](https://azure.microsoft.com/en-us/blog/microsoft-unveils-two-custom-designed-chips-for-scaling-the-cloud/). Meta's addition to this list is significant — but it's a maturation, not a market exit from the GPU supply chain.

---

## The Alberta Data Center

Days before the July 9 memo on Iris's production timeline, [Meta announced a CAD $13 billion investment in a Canadian data center in Sturgeon County, Alberta](https://about.fb.com/news/2026/07/breaking-ground-on-metas-first-data-center-in-canada/). This is part of the 14GW buildout — not an addition to it.

Why Alberta: Meta and Alberta officials cited [the province's ample natural gas resources, power-generation capacity, and a favorable regulatory environment](https://www.theglobeandmail.com/business/article-meta-ai-data-centre-sturgeon-county-alberta/) — not proximity to hydro or wind power. The facility itself will draw primarily on a new natural-gas plant built to serve it, per that same reporting. Separately, [Meta has a standing company-wide commitment to match 100% of its global electricity use with clean and renewable energy purchases](https://sustainability.atmeta.com/energy/) — an accounting commitment across Meta's whole footprint, not a claim that the Alberta site itself runs on renewable generation.

For builders, this is logistics context — capacity is expanding, but the compute becomes available for Meta's internal workloads first.

---

## What This Means for Builders

**Meta Model API capacity and pricing.** The [Meta Model API entered public preview on July 9, 2026](https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/), [priced at $1.25/$4.25 per million tokens (input/output) for Muse Spark 1.1](https://ai.developer.meta.com/docs/pricing-rate-limits), positioning it to compete on cost. As MTIA chips come online through 2027, Meta gains direct control over its inference cost structure — reducing the pass-through from Nvidia GPU rental. This creates conditions for price reductions or throughput improvements, though Meta has not committed to either.

**Llama inference trajectory.** MTIA 450 and 500 are optimized for generative AI inference, which means future Llama model generations (Llama 5 and beyond) will likely be tuned for this architecture at internal scale. That doesn't affect how builders run Llama on their own hardware, but it does suggest the official Meta-hosted inference path will become more efficient relative to GPU-based alternatives over time.

**Open-weight model dynamics.** Meta's strategic case for releasing Llama as open weights partly depends on not needing API revenue to recover compute costs — because it builds the compute stack itself. As MTIA reduces Meta's per-inference cost, the business case for keeping Llama open remains strong. Builders betting on Llama open weights being available long-term should find this news supportive.

**Software stack: no changes needed.** MTIA runs on PyTorch, vLLM, and Triton — the same tools builders already use for Llama inference. If you're running Llama on vLLM today, your tooling is already compatible with MTIA's software environment. No migration work is implied.

**Custom silicon acceleration of inference pricing.** The broader trend across Google, Amazon, Microsoft, and now Meta is that purpose-built inference silicon at hyperscaler scale consistently drives per-token costs lower than GPU alternatives. Builders whose unit economics depend on inference costs should expect a continued downward trajectory — particularly on models served through APIs backed by custom silicon.

---

## Custom Silicon Landscape (July 2026)

| Company | Chip | Status | Primary Use |
|---------|------|--------|-------------|
| [Google](https://cloud.google.com/tpu) | TPU (v5 and newer) | Production | Training + inference (Gemini) |
| [Amazon](https://aws.amazon.com/ai/machine-learning/trainium/) | Trainium 2 / Inferentia 2 | Production | AWS AI services |
| [Microsoft](https://azure.microsoft.com/en-us/blog/microsoft-unveils-two-custom-designed-chips-for-scaling-the-cloud/) | Maia 100 | Production | Azure AI, Copilot |
| [Apple](https://www.apple.com/newsroom/) | M-series Neural Engine | Production | On-device (Core ML) |
| **Meta** | **Iris (MTIA)** | **September 2026** | **Facebook/Instagram + Llama API** |

Meta is the last of the major AI platform companies to bring a production-ready inference chip to scale. The hardware layer is now vertically integrated at every hyperscaler. (Note: several of these vendors have since announced newer chip generations — this table reflects the July 2026 snapshot relevant to the Iris news.)

---

## What to Watch

- **September 2026**: Iris manufacturing begins. Watch for Meta blog posts on MTIA deployment milestones.
- **End-2026 7GW target**: Meta's Q3 and Q4 earnings calls will reflect infrastructure spend; analyst calls may surface deployment rate data.
- **2027 14GW target**: The scale at which MTIA handles a meaningful portion of Llama inference demand. If this milestone is reached, expect pricing signals on the Meta Model API.
- **MTIA 2nm (next-gen)**: The chip after Iris — Broadcom has [called it "the industry's first 2nm AI compute accelerator"](https://www.globenewswire.com/news-release/2026/04/14/3273998/19933/en/broadcom-announces-extended-partnership-with-meta-to-deploy-technology-to-support-multi-gigawatts-of-meta-s-custom-silicon-mtia.html) (fab partner for that node not yet confirmed). No timeline disclosed, but the [Broadcom partnership through 2029](https://about.fb.com/news/2026/04/meta-partners-with-broadcom-to-co-develop-custom-ai-silicon/) implies at least one more generation.
- **Muse Spark and Llama 5 roadmap**: Whether Meta times a major model release to coincide with Iris production ramp will signal how tightly the model and hardware roadmaps are coordinated.

Meta moved from "experimenting with custom silicon" to "four chip generations in two years" quietly. Iris entering production in September puts it on a hardware trajectory that parallels Google, Amazon, and Microsoft — and directly supports the open-weight model distribution that defines Meta's AI strategy.

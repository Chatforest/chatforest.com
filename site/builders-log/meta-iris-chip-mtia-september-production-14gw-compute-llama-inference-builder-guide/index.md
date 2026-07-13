# Meta's Iris AI Chip Enters Production in September — What Builders Using Llama and the Meta Model API Need to Know

> An internal Meta memo revealed that its custom AI chip Iris — the latest in its MTIA (Meta Training and Inference Accelerator) program — enters manufacturing in September 2026, co-designed with Broadcom and fabbed by TSMC. Meta plans 7GW of compute by end-2026 and 14GW by 2027. Here's what the silicon shift means for builders on the Meta Model API and open-weight Llama inference.


An internal Meta memo revealed on July 9, 2026, that the company's custom AI chip Iris enters manufacturing in September 2026. Iris is the latest generation in Meta's MTIA (Meta Training and Inference Accelerator) program — co-designed with Broadcom, fabricated by TSMC, and intended to cut Meta's dependence on Nvidia for inference workloads at scale.

The same memo disclosed Meta's compute targets: 7 gigawatts of AI infrastructure by end-2026, and 14 gigawatts by 2027. A separate $10 billion data center investment in Alberta, Canada was announced alongside the chip news. Meta's total AI infrastructure spend in 2026 is estimated at up to $145 billion.

This is a research-based summary based on published reports and Meta's own blog disclosures. We did not have access to Iris hardware and no public benchmark data for the Iris chip has been released.

---

## The MTIA Program: Four Chips in Two Years

Meta's custom silicon effort is more mature than most outside observers have tracked. The MTIA program has run through four generations — MTIA 300, 400, 450, and 500 — in roughly two years, with Iris being the production name for the chips entering the market now.

The progression from MTIA 300 to MTIA 500 delivers claimed gains of:
- **25× compute performance**
- **4.5× high-bandwidth memory (HBM) bandwidth**

MTIA 450 and 500 are specifically optimized for generative AI inference — the workload that serves Llama model requests in production. Earlier MTIA generations handled ranking and recommendation workloads (Facebook and Instagram feeds). The shift toward GenAI inference is the part that matters for builders.

The chip cleared its bug-testing phase in approximately six weeks, with no major issues found — an unusually clean pass that accelerated the production timeline.

---

## Who Built It and How

The Iris chip is a collaboration, not a Meta solo effort:

- **Broadcom**: Co-designed the chip and handles advanced packaging and networking integration. The Broadcom partnership runs through 2029 and covers multiple MTIA generations — this is a long-term commitment, not a one-off project.
- **TSMC**: Manufactures the chip. Newer post-Iris generations are planned for TSMC's 2nm node, which would make them among the first custom AI chips on that process.
- **Samsung**: Memory supply.
- **SanDisk**: Flash storage.
- **Sumitomo Electric**: Fiber-optic networking for the data centers.

The software stack is built on industry-standard tools: **PyTorch, vLLM, Triton, and the Open Compute Project (OCP)**. Meta has tested MTIA with Llama models and has hundreds of thousands of MTIA chips deployed in internal production. Builder tooling that works today for Llama inference does not require changes to run on MTIA.

---

## What Iris Does Not Do: Nvidia Is Not Replaced

Meta has been explicit that Iris supplements rather than replaces commercial GPUs from Nvidia and AMD. In practice, this means:

- MTIA handles ranking, recommendation, and increasingly GenAI inference for Meta's own products (Facebook, Instagram, WhatsApp).
- Nvidia/AMD GPUs continue to serve training workloads and cover where MTIA capacity doesn't reach.
- The 7GW → 14GW compute expansion plan draws on both MTIA silicon and continued GPU procurement.

The hybrid approach is standard among large hyperscalers. Google runs TPU + Nvidia. Amazon runs Trainium/Inferentia + Nvidia. Microsoft runs Maia + Nvidia. Meta's addition to this list is significant — but it's a maturation, not a market exit from the GPU supply chain.

---

## The Alberta Data Center

The same July 9 memo that disclosed Iris's production timeline also announced a $10 billion investment in a Canadian data center in Alberta. This is part of the 14GW buildout — not an addition to it.

Why Alberta: proximity to renewable power (hydroelectric and wind) and a favorable regulatory environment for large-scale infrastructure. Meta has made public commitments to match 100% of its energy with renewable sources, and Alberta gives it geographic diversity away from the US concentration of existing capacity.

For builders, this is logistics context — capacity is expanding, but the compute becomes available for Meta's internal workloads first.

---

## What This Means for Builders

**Meta Model API capacity and pricing.** The Meta Model API, launched publicly in June 2026 at $1.25/$4.25 per million tokens (input/output for Muse Spark 1.1), is priced to compete. As MTIA chips come online through 2027, Meta gains direct control over its inference cost structure — reducing the pass-through from Nvidia GPU rental. This creates conditions for price reductions or throughput improvements, though Meta has not committed to either.

**Llama inference trajectory.** MTIA 450 and 500 are optimized for generative AI inference, which means future Llama model generations (Llama 5 and beyond) will likely be tuned for this architecture at internal scale. That doesn't affect how builders run Llama on their own hardware, but it does suggest the official Meta-hosted inference path will become more efficient relative to GPU-based alternatives over time.

**Open-weight model dynamics.** Meta's strategic case for releasing Llama as open weights partly depends on not needing API revenue to recover compute costs — because it builds the compute stack itself. As MTIA reduces Meta's per-inference cost, the business case for keeping Llama open remains strong. Builders betting on Llama open weights being available long-term should find this news supportive.

**Software stack: no changes needed.** MTIA runs on PyTorch, vLLM, and Triton — the same tools builders already use for Llama inference. If you're running Llama on vLLM today, your tooling is already compatible with MTIA's software environment. No migration work is implied.

**Custom silicon acceleration of inference pricing.** The broader trend across Google, Amazon, Microsoft, and now Meta is that purpose-built inference silicon at hyperscaler scale consistently drives per-token costs lower than GPU alternatives. Builders whose unit economics depend on inference costs should expect a continued downward trajectory — particularly on models served through APIs backed by custom silicon.

---

## Custom Silicon Landscape (July 2026)

| Company | Chip | Status | Primary Use |
|---------|------|--------|-------------|
| Google | TPU v5 | Production | Training + inference (Gemini) |
| Amazon | Trainium 2 / Inferentia 2 | Production | AWS AI services |
| Microsoft | Maia 100 | Production | Azure AI, Copilot |
| Apple | M-series Neural Engine | Production | On-device (Core ML) |
| **Meta** | **Iris (MTIA 450/500)** | **September 2026** | **Facebook/Instagram + Llama API** |

Meta is the last of the major AI platform companies to bring a production-ready inference chip to scale. The hardware layer is now vertically integrated at every hyperscaler.

---

## What to Watch

- **September 2026**: Iris manufacturing begins. Watch for Meta blog posts on MTIA deployment milestones.
- **End-2026 7GW target**: Meta's Q3 and Q4 earnings calls will reflect infrastructure spend; analyst calls may surface deployment rate data.
- **2027 14GW target**: The scale at which MTIA handles a meaningful portion of Llama inference demand. If this milestone is reached, expect pricing signals on the Meta Model API.
- **MTIA 2nm (next-gen)**: The chip after Iris — planned for TSMC 2nm. No timeline disclosed, but the Broadcom partnership through 2029 implies at least one more generation.
- **Muse Spark and Llama 5 roadmap**: Whether Meta times a major model release to coincide with Iris production ramp will signal how tightly the model and hardware roadmaps are coordinated.

Meta moved from "experimenting with custom silicon" to "four chip generations in two years" quietly. Iris entering production in September puts it on a hardware trajectory that parallels Google, Amazon, and Microsoft — and directly supports the open-weight model distribution that defines Meta's AI strategy.


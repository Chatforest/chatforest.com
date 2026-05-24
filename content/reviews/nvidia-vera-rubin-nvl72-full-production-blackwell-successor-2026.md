---
title: "Blackwell's Replacement Is Already in Production. NVIDIA's Vera Rubin Ships in July."
date: 2026-05-24
slug: nvidia-vera-rubin-nvl72-full-production-blackwell-successor-2026
tags: ["nvidia", "gpu", "ai-infrastructure", "compute", "hardware", "vera-rubin", "blackwell", "data-center"]
description: "NVIDIA's Vera Rubin platform entered full production in Q1 2026. At 5x Blackwell's inference throughput and up to 10x lower cost per token, it's the infrastructure the next wave of frontier models will be built on."
content_type: "Analysis"
author: "ChatForest"
---

Blackwell is barely a year old, and NVIDIA has already moved on.

At CES in January 2026, Jensen Huang announced that **Vera Rubin**, the successor to the Blackwell architecture, had entered **full production**. First shipments to AI customers are expected in **July 2026**. Cloud provider availability — AWS, Google Cloud, Microsoft Azure, Oracle, CoreWeave, and others — is targeted for the second half of this year.

Rubin is not an incremental spec bump. NVIDIA is claiming **5x inference performance** and **3.5x training throughput** over Blackwell's GB200, with a headline efficiency figure of **up to 10x lower cost per token** for large-scale inference workloads. OpenAI, Anthropic, Meta, xAI, Mistral, and Perplexity have all publicly committed to the platform.

Here's what it is, what it actually delivers, and what it means for where AI is going in the next 18 months.

---

## What Blackwell Was and Why Rubin Exists

Blackwell (the GB200/GB300 NVL72) became the reference infrastructure for frontier AI in 2025. Training runs for models like GPT-5.5, Claude 4.6, and Gemini 2.5 Pro all ran on Blackwell-class hardware. The constraint wasn't capability — it was cost and scale. At Blackwell prices, inference for the most capable models remained expensive enough to limit deployment.

Rubin's design goal was to break that constraint. Not just faster training, but radically cheaper inference — the metric that actually determines whether a model can be deployed at consumer scale, not just run in a lab.

The 10x cost claim needs context (more below), but the directional intent is clear: NVIDIA is building infrastructure that makes the next generation of frontier models economically viable to run at scale. That has direct implications for how AI products get built in 2027 and beyond.

---

## Six Chips, One Platform

The Vera Rubin platform is what NVIDIA calls an "extreme co-designed" system — not a GPU drop-in, but a full stack of six chips built to operate as an integrated unit:

1. **Rubin GPU (R100)** — the compute core
2. **Vera CPU** — NVIDIA's first custom server CPU
3. **NVLink 6 Switch** — the scale-up fabric
4. **ConnectX-9 SuperNIC** — networking
5. **BlueField-4 DPU** — data processing
6. **Spectrum-6 Ethernet Switch** — scale-out fabric

Previous NVIDIA platforms used third-party CPUs (Intel, AMD, or Arm). Vera is NVIDIA's own. It runs 88 custom Arm "Olympus" cores across 227 billion transistors, with 1.5 TB of LPDDR5X and 1.2 TB/s memory bandwidth. It connects to the Rubin GPUs via NVLink-C2C at 1.8 TB/s — memory-coherent, low-latency, fast enough that the CPU and GPU can operate as a unified system rather than separate components communicating over PCIe.

---

## Rubin GPU: The Core Numbers

The **Rubin R100** is fabricated on TSMC's 3nm N3 process, packs 336 billion transistors in a dual-reticle die design, and carries up to **288 GB of HBM4** per GPU with **22 TB/s memory bandwidth**. For reference, the GB200's HBM3e configuration tops out at 192 GB and roughly 8 TB/s.

Performance claims:
- **50 PFLOPS NVFP4 inference** (5x Blackwell GB200)
- **35 PFLOPS NVFP4 training** (3.5x Blackwell GB200)
- **~16 PFLOPS FP8**
- NVLink 6 scale-up: **3.6 TB/s per GPU** (double NVLink 5 in Blackwell)

Each Rubin GPU draws approximately **2,300W** — substantially higher than Blackwell per chip, but the efficiency gains mean the performance-per-watt story is more nuanced than the raw power figure suggests.

---

## The NVL72: NVIDIA's Primary Product

The commercial unit is the **Rubin NVL72 rack** — 72 Rubin GPUs paired with 36 Vera CPUs in a fully liquid-cooled system.

**System specs:**
- 72 R100 GPUs + 36 Vera CPUs
- Scale-up bandwidth: **260 TB/s** per rack (NVLink 6 fabric)
- Rack inference: **3.6 EFLOPS NVFP4**
- Rack training: **2.5 EFLOPS NVFP4** / **1.4 EFLOPS FP8**
- Power: approximately **125 kW** per rack
- Installation time: **5 minutes** (down from ~2 hours for Blackwell NVL72)

The 5-minute installation number is worth highlighting. Blackwell NVL72 installations required two hours of custom configuration. Rubin NVL72 is designed to drop in. At the scale where hyperscalers are deploying these systems — hundreds or thousands of racks — installation time is an operational cost that compounds.

---

## The 10x Token Cost Claim: What It Actually Means

NVIDIA's headline is "up to 10x lower cost per token versus Blackwell." That claim requires unpacking.

The 10x figure is specifically benchmarked on **MoE (Mixture-of-Experts) inference workloads at long sequence lengths** — specifically, models like Kimi-K2-Thinking at 32K input / 8K output context. Rubin's architecture is particularly well-suited to MoE because it requires only about **1/4 the GPUs** to train MoE models versus an equivalent Blackwell configuration, which drives the efficiency figure.

For **dense model inference at shorter contexts** — the workload of most everyday API calls — independent hardware analysts estimate a more realistic **2–3x improvement** over Blackwell.

Neither figure is misleading, but they describe different workloads. The 10x number is the ceiling you'd see running a large sparse MoE model at scale, not the baseline for all inference. The 2–3x range is a more conservative estimate for typical production deployments.

The practical takeaway: Rubin makes the economics of running frontier-scale MoE models substantially more viable. Most of the models being actively developed in 2026 — Meta's recent architectures, DeepSeek's MoE family, various Mistral variants — are MoE. The 10x claim isn't marketing math for a future product; it's describing the workloads that will dominate AI infrastructure in 2027.

---

## Who's Committed

Every major AI lab has publicly signed on to Rubin:

- **OpenAI** (Sam Altman): *"When we add more compute, models get more capable, solve harder problems and make a bigger impact for people. The NVIDIA Rubin platform helps us keep scaling this progress."*
- **Anthropic** (Dario Amodei): *"The efficiency gains in the NVIDIA Rubin platform represent the kind of infrastructure progress that enables longer memory, better reasoning and more reliable outputs."*
- **xAI** (Elon Musk): *"NVIDIA Rubin will be a rocket engine for AI. If you want to train and deploy frontier models at scale, this is the infrastructure you use — and Rubin will remind the world that NVIDIA is the gold standard."*
- **Meta**, **Mistral**, **Perplexity** — all confirmed

Cloud providers committed for H2 2026 availability: **AWS, Google Cloud, Microsoft Azure, Oracle Cloud Infrastructure (OCI), CoreWeave, Lambda, Nebius, Nscale**.

---

## The Rubin CPX That Didn't Happen

NVIDIA had originally planned a third member of the Rubin family: the **Rubin CPX** (Context Phase Accelerator), a specialized chip for long-context inference with 128 GB GDDR7 memory and dedicated hardware for million-token-scale attention.

At GTC 2026, NVIDIA removed it from the roadmap. The replacement: a **$20 billion licensing deal with Groq** for their LPU (Language Processing Unit) silicon. The Groq 3 LPX Rack (256 LPUs, 128 GB aggregate SRAM, 640 TB/s scale-up bandwidth) handles the decode phase of inference while Rubin GPUs handle prefill — a hybrid architecture that achieves the long-context efficiency the CPX was designed for, but via partnership rather than in-house silicon.

---

## What Comes After Rubin

**Rubin Ultra (H2 2027)** — The higher-end configuration uses a dual-die R200 GPU package with 100 PFLOPS FP4 per package and 1 TB HBM4E. The rack system, called **Kyber**, scales to 576 GPU chiplets and claims 14x the throughput of the Blackwell GB300 NVL72. At approximately 600 kW per rack, it will require significant power and cooling infrastructure — Kyber uses 800 VDC power delivery and full liquid cooling across vertical trays.

Note: Rubin Ultra was originally planned as a four-die design, scaled back to dual-die due to TSMC CoWoS-L yield challenges. NVIDIA says the redesign still achieves 3.5x inference throughput-per-watt over Blackwell B300.

**Feynman (2028)** — NVIDIA's next named generation, paired with the **Rosa CPU**, is scheduled for 2028. Key architectural novelty: 3D GPU die stacking, optical NVLink interconnects, and the next NVSwitch generation. The CPX long-context inference concept may re-emerge with Feynman.

---

## The Bigger Picture

There's an interesting compression happening in the AI infrastructure cycle. Blackwell shipped commercially in early 2025. By July 2026, its replacement is in customers' hands. By late 2027, Rubin Ultra will be shipping. Feynman is already on a roadmap for 2028.

The cadence of hardware generations has essentially matched the pace of model generations. GPT-5.5 was co-designed for GB200/GB300 hardware. The next wave of models will be designed around Rubin's 288 GB HBM4 per GPU, its NVLink 6 fabric, and its memory-coherent CPU integration. Models and hardware are co-evolving on roughly 12-to-18-month cycles.

That pace has implications for the economics of AI. The companies that can stay on the hardware frontier — or that have locked up future capacity (Anthropic's deal to pay SpaceX/xAI $1.25 billion per month for Colossus access being a recent example) — have meaningfully different capability and cost structures than those one generation behind.

Rubin is the next generation of that frontier. First deliveries: July 2026.

---

*Part of our [AI Infrastructure coverage](/categories/reviews/).*

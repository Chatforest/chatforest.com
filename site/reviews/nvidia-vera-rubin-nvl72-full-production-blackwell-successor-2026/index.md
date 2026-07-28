# Blackwell's Replacement Is Already in Production. NVIDIA's Vera Rubin Ships in July.

> NVIDIA's Vera Rubin platform entered full production in Q1 2026. At 5x Blackwell's inference throughput and up to 10x lower cost per token, it's the infrastructure the next wave of frontier models will be built on.


Blackwell is barely a year old, and NVIDIA has already moved on.

At [CES in January 2026](https://www.datacenterdynamics.com/en/news/nvidia-ceo-announces-vera-rubin-chips-are-in-full-production-during-ces-keynote/), Jensen Huang announced that **Vera Rubin**, the successor to the Blackwell architecture, had entered **full production**. [First shipments to major AI customers rolled out in July 2026](https://wccftech.com/nvidia-squashes-vera-rubin-rumors-first-shipments-rolling-out-in-july-to-ai-customers/), with [cloud provider availability](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/) — AWS, Google Cloud, Microsoft Azure, Oracle, CoreWeave, and others — targeted for the second half of 2026.

Rubin is not an incremental spec bump. NVIDIA is claiming [**5x inference performance** and **3.5x training throughput**](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/) over Blackwell's GB200, with a headline efficiency figure of **up to 10x lower cost per token** for large-scale inference workloads. [OpenAI, Anthropic, Meta, xAI, Mistral, and Perplexity have all publicly committed](https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer) to the platform.

Here's what it is, what it actually delivers, and what it means for where AI is going in the next 18 months.

---

## What Blackwell Was and Why Rubin Exists

Blackwell (the GB200/GB300 NVL72) became the reference infrastructure for frontier AI in 2025. [GPT-5.5 was co-designed alongside NVIDIA's GB200/GB300 NVL72 systems](https://www.mayhemcode.com/2026/04/nvidia-blackwell-gpus-and-frontier-ai.html), and recent Claude models run on a mix of Blackwell GPUs, Google TPUs, and AWS Trainium rather than a single platform — [Google's Gemini, by contrast, trains primarily on Google's own TPU silicon, not Nvidia GPUs](https://www.datacenterdynamics.com/en/news/training-gemini-tpus-multiple-data-centers-and-risks-of-cosmic-rays/). The constraint wasn't capability — it was cost and scale. At Blackwell prices, inference for the most capable models remained expensive enough to limit deployment.

Rubin's design goal was to break that constraint. Not just faster training, but radically cheaper inference — the metric that actually determines whether a model can be deployed at consumer scale, not just run in a lab.

The 10x cost claim needs context (more below), but the directional intent is clear: NVIDIA is building infrastructure that makes the next generation of frontier models economically viable to run at scale. That has direct implications for how AI products get built in 2027 and beyond.

---

## Six Chips, One Platform

The Vera Rubin platform is what NVIDIA calls an ["extreme co-designed"](https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/) system — not a GPU drop-in, but a full stack of six chips built to operate as an integrated unit:

1. **Rubin GPU (R100)** — the compute core
2. **Vera CPU** — NVIDIA's first custom server CPU
3. **NVLink 6 Switch** — the scale-up fabric
4. **ConnectX-9 SuperNIC** — networking
5. **BlueField-4 DPU** — data processing
6. **Spectrum-6 Ethernet Switch** — scale-out fabric

Previous NVIDIA platforms used third-party CPUs (Intel, AMD, or Arm). Vera is NVIDIA's own. It runs [88 custom Arm "Olympus" cores across 227 billion transistors](https://wccftech.com/nvidia-rubin-rubin-ultra-next-gen-vera-cpus-next-year-1-tb-hbm4-memory-4-reticle-sized-gpus-100pf-fp4-88-cpu-cores/), with [1.5 TB of LPDDR5X and 1.2 TB/s memory bandwidth](https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/). It connects to the Rubin GPUs via NVLink-C2C at 1.8 TB/s — memory-coherent, low-latency, fast enough that the CPU and GPU can operate as a unified system rather than separate components communicating over PCIe.

---

## Rubin GPU: The Core Numbers

The [**Rubin R100** is fabricated on TSMC's 3nm N3 process, packs 336 billion transistors in a dual-die design](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/), and carries up to **288 GB of HBM4** per GPU with **22 TB/s memory bandwidth**. For reference, [the GB200's HBM3e configuration tops out at 192 GB](https://www.hyperstack.cloud/nvidia-blackwell-gb200) and [roughly 8 TB/s](https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/).

[Performance claims](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/):
- **50 PFLOPS NVFP4 inference** (5x Blackwell GB200)
- **35 PFLOPS NVFP4 training** (3.5x Blackwell GB200)
- [**~16 PFLOPS FP8**](https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/)
- NVLink 6 scale-up: **3.6 TB/s per GPU** (double NVLink 5 in Blackwell)

[Each Rubin GPU draws up to approximately **2,300W** at max performance configuration](https://hashrateindex.com/blog/nvidia-vera-rubin-nvl72-specs-breakdown/) — substantially higher than Blackwell per chip, but the efficiency gains mean the performance-per-watt story is more nuanced than the raw power figure suggests.

---

## The NVL72: NVIDIA's Primary Product

The commercial unit is the **Rubin NVL72 rack** — 72 Rubin GPUs paired with 36 Vera CPUs in a fully liquid-cooled system.

**System specs** ([NVIDIA](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/) unless noted):
- 72 R100 GPUs + 36 Vera CPUs
- Scale-up bandwidth: **260 TB/s** per rack (NVLink 6 fabric)
- Rack inference: **3.6 EFLOPS NVFP4**
- Rack training: **2.5 EFLOPS NVFP4** / **~1.26 EFLOPS FP8/FP6**
- Power: [roughly **190–230 kW** per rack](https://hashrateindex.com/blog/nvidia-vera-rubin-nvl72-specs-breakdown/) depending on configuration (Supermicro's Rubin NVL72 reference design [is sized for ~227 kW](https://www.supermicro.com/en/accelerators/nvidia/vera-rubin)) — notably higher than Blackwell GB200 NVL72's ~120–130 kW
- [Compute tray assembly time: **~5 minutes**, down from roughly two hours for Blackwell](https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/)

The 5-minute assembly number is worth highlighting. Blackwell NVL72 trays required roughly two hours of cabled, hands-on configuration; Rubin's cable-free, hose-free tray design is built to drop in. At the scale where hyperscalers are deploying these systems — hundreds or thousands of racks — assembly time is an operational cost that compounds.

---

## The 10x Token Cost Claim: What It Actually Means

NVIDIA's headline is "up to 10x lower cost per token versus Blackwell." That claim requires unpacking.

The 10x figure is [specifically benchmarked on **MoE (Mixture-of-Experts) inference workloads at long sequence lengths**](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/) — specifically, the Kimi-K2-Thinking model at 32K input / 8K output context, comparing Rubin NVL72 against GB200 NVL72. Rubin's architecture is particularly well-suited to MoE because it [requires only about **1/4 the GPUs**](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/) to train MoE models versus an equivalent Blackwell configuration, which drives the efficiency figure.

For **dense model inference at shorter contexts** — the workload of most everyday API calls — [independent analysis from SemiAnalysis estimates a more realistic **2–3x improvement**](https://newsletter.semianalysis.com/p/vera-rubin-nvl72-vs-gb200-nvl72-inference) over Blackwell.

Neither figure is misleading, but they describe different workloads. The 10x number is the ceiling you'd see running a large sparse MoE model at scale, not the baseline for all inference. The 2–3x range is a more conservative estimate for typical production deployments.

The practical takeaway: Rubin makes the economics of running frontier-scale MoE models substantially more viable. Most of the models being actively developed in 2026 — Meta's recent architectures, DeepSeek's MoE family, various Mistral variants — are MoE. The 10x claim isn't marketing math for a future product; it's describing the workloads that will dominate AI infrastructure in 2027.

---

## Who's Committed

Every major AI lab has publicly signed on to Rubin, per [NVIDIA's own announcement](https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer):

- **OpenAI** (Sam Altman): *"When we add more compute, models get more capable, solve harder problems and make a bigger impact for people. The NVIDIA Rubin platform helps us keep scaling this progress."*
- **Anthropic** (Dario Amodei): *"The efficiency gains in the NVIDIA Rubin platform represent the kind of infrastructure progress that enables longer memory, better reasoning and more reliable outputs."*
- **xAI** (Elon Musk): *"NVIDIA Rubin will be a rocket engine for AI. If you want to train and deploy frontier models at scale, this is the infrastructure you use — and Rubin will remind the world that NVIDIA is the gold standard."*
- **Meta**, **Mistral**, **Perplexity** — all confirmed

Cloud providers committed for H2 2026 availability: **AWS, Google Cloud, Microsoft Azure, Oracle Cloud Infrastructure (OCI), CoreWeave, Lambda, Nebius, Nscale**.

---

## The Rubin CPX That Didn't Happen

NVIDIA had originally planned a third member of the Rubin family: the **Rubin CPX** (Context Phase Accelerator), a specialized chip for long-context inference with 128 GB GDDR7 memory and dedicated hardware for million-token-scale attention, [first announced at the AI Infra Summit in September 2025](https://www.spheron.network/blog/nvidia-rubin-cpx-long-context-inference/).

At GTC 2026, [NVIDIA removed it from the roadmap](https://www.tomshardware.com/pc-components/gpus/nvidia-removes-rubin-cpx-accelerators-from-its-roadmap-groq-3-lpus-take-center-stage-as-cpx-is-removed). The replacement: a [**$20 billion licensing deal with Groq**](https://markets.financialcontent.com/stocks/article/marketminute-2025-12-25-nvidia-consolidates-ai-supremacy-with-20-billion-groq-licensing-deal-ahead-of-ces-2026) for their LPU (Language Processing Unit) silicon. The [Groq 3 LPX Rack (256 LPUs, 128 GB aggregate SRAM, 640 TB/s scale-up bandwidth)](https://www.datacenterdynamics.com/en/news/nvidia-announces-groq-3-lpu-ai-inference-chip-plans-256-lpu-rack/) handles the decode phase of inference while Rubin GPUs handle prefill — a hybrid architecture that achieves the long-context efficiency the CPX was designed for, but via partnership rather than in-house silicon.

---

## What Comes After Rubin

**Rubin Ultra (H2 2027)** — At GTC 2026, NVIDIA [originally announced Rubin Ultra as a four-die R200 GPU package rated at 100 PFLOPS FP4 and 1 TB of HBM4E](https://wccftech.com/nvidia-rubin-rubin-ultra-next-gen-vera-cpus-next-year-1-tb-hbm4-memory-4-reticle-sized-gpus-100pf-fp4-88-cpu-cores/), with a rack system called **Kyber** scaling to 576 GPU chiplets and [claiming 14x the throughput of the Blackwell GB300 NVL72](https://www.tomshardware.com/pc-components/gpus/nvidia-shows-off-rubin-ultra-with-600-000-watt-kyber-racks-and-infrastructure-coming-in-2027) at roughly 600 kW per rack, using 800 VDC power delivery and full liquid cooling across vertical trays.

That four-die plan has since been scrapped. [Supply-chain reporting from SemiAnalysis and TSMC-packaging trade coverage indicates NVIDIA cut Rubin Ultra back to a dual-die design](https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-reportedly-cancels-quad-die-rubin-ultra-gpu-in-favor-of-dual-gpu-design-report-claims-complex-design-purportedly-scrapped-over-manufacturing-execution-concerns) after **substrate warpage and yield problems in TSMC's CoWoS-L packaging** made the four-die package unmanufacturable at scale. The dual-die version reportedly delivers **roughly half** the compute and memory of the original plan (eight HBM4E stacks instead of sixteen) — meaning the 100 PFLOPS / 1 TB HBM4E figures above describe the cancelled design, not what will actually ship. NVIDIA has not published revised per-package numbers for the dual-die version, though it maintains the redesign still delivers a [3.5x inference throughput-per-watt gain over Blackwell B300](https://www.trendforce.com/news/2026/04/01/news-nvidias-rubin-ultra-seen-sticking-to-dual-die-design-on-packaging-constraints-tsmc-3nm-demand-intact/).

**Feynman (2028)** — [NVIDIA's next named generation, paired with the **Rosa CPU**, is scheduled for 2028](https://www.tomshardware.com/pc-components/gpus/nvidia-updates-data-center-roadmap-with-rosa-cpu-and-stacked-feynman-gpus-optical-nvlink-groq-lpus-with-nvfp4-and-nvlink-also-on-deck). Key architectural novelty: 3D GPU die stacking, optical NVLink interconnects, and the next NVSwitch generation. The CPX long-context inference concept may re-emerge with Feynman.

---

## The Bigger Picture

There's an interesting compression happening in the AI infrastructure cycle. Blackwell shipped commercially in early 2025. By July 2026, its replacement is in customers' hands. By late 2027, Rubin Ultra will be shipping. Feynman is already on a roadmap for 2028.

The cadence of hardware generations has essentially matched the pace of model generations. GPT-5.5 was co-designed for GB200/GB300 hardware. The next wave of models will be designed around Rubin's 288 GB HBM4 per GPU, its NVLink 6 fabric, and its memory-coherent CPU integration. Models and hardware are co-evolving on roughly 12-to-18-month cycles.

That pace has implications for the economics of AI. The companies that can stay on the hardware frontier — or that have locked up future capacity ([Anthropic's deal to pay xAI/SpaceX $1.25 billion per month for access to the Colossus 1 data center](https://techcrunch.com/2026/05/20/anthropic-will-pay-xai-1-25-billion-per-month-for-compute/), disclosed in SpaceX's May 2026 IPO filing, being a recent example) — have meaningfully different capability and cost structures than those one generation behind.

Rubin is the next generation of that frontier. First deliveries: July 2026.

---

---

**Sources:** [NVIDIA — Vera Rubin NVL72 product page](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/) · [NVIDIA Newsroom — Rubin platform launch and partner quotes](https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer) · [NVIDIA Developer Blog — six-chip platform breakdown](https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/) · [Data Center Dynamics — Vera Rubin full production CES announcement](https://www.datacenterdynamics.com/en/news/nvidia-ceo-announces-vera-rubin-chips-are-in-full-production-during-ces-keynote/) · [Tom's Hardware — CES keynote production confirmation](https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-ceo-confirms-vera-rubin-nvl72-is-now-in-production-jensen-huang-uses-ces-keynote-to-announce-the-milestone) · [VideoCardz — full NVL72 spec breakdown](https://videocardz.com/newz/nvidia-vera-rubin-nvl72-detailed-72-gpus-36-cpus-260-tb-s-scale-up-bandwidth) · [Hashrate Index — NVL72 power and per-GPU specs](https://hashrateindex.com/blog/nvidia-vera-rubin-nvl72-specs-breakdown/) · [SemiAnalysis — Rubin vs. GB200 dense-inference analysis](https://newsletter.semianalysis.com/p/vera-rubin-nvl72-vs-gb200-nvl72-inference) · [Tom's Hardware — Rubin Ultra cut to dual-die](https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-reportedly-cancels-quad-die-rubin-ultra-gpu-in-favor-of-dual-gpu-design-report-claims-complex-design-purportedly-scrapped-over-manufacturing-execution-concerns) · [FinancialContent — $20B Groq licensing deal](https://markets.financialcontent.com/stocks/article/marketminute-2025-12-25-nvidia-consolidates-ai-supremacy-with-20-billion-groq-licensing-deal-ahead-of-ces-2026) · [TechCrunch — Anthropic's $1.25B/month xAI compute deal](https://techcrunch.com/2026/05/20/anthropic-will-pay-xai-1-25-billion-per-month-for-compute/)

*Part of our [AI Infrastructure coverage](/categories/reviews/).*


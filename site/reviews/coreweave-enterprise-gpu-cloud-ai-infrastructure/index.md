# CoreWeave Review: The Enterprise GPU Cloud That Frontier AI Runs On

> CoreWeave is the dominant specialized GPU cloud for frontier AI labs and large enterprises. We review its CUDA Cloud infrastructure, GB200 NVL72 availability, HPC InfiniBand networking, pricing, $66.8B contracted backlog, and how it compares to Lambda Labs, RunPod, and the hyperscalers. NASDAQ: CRWV.


CoreWeave reached $5.13 billion in revenue in 2025. In 2023, that number was $229 million. The trajectory is extraordinary: 730% growth from 2023 to 2024, then another 170% in 2025. No other cloud platform has crossed $5 billion annual revenue as fast. The company went public on Nasdaq in March 2025, carries a $66.8 billion contracted backlog, and is building toward $12 billion in 2026 guidance while simultaneously deploying $30–35 billion in new infrastructure capital.

That is not a startup story. That is a company that became critical infrastructure for the most compute-intensive AI labs on earth — OpenAI, Meta, Anthropic, Microsoft — before most of the industry understood what was happening.

This review explains what CoreWeave is, what it sells, who buys it, and where it fits in the GPU cloud landscape relative to Lambda Labs, RunPod, Vast.ai, and the hyperscalers. It is emphatically not a platform for individual developers spinning up a single GPU instance. It is the infrastructure where frontier AI models are trained.

---

## Company Background

CoreWeave was founded in 2017 as **Atlantic Crypto** — an Ethereum mining operation started by Michael Intrator (now CEO), Brian Venturo (now CTO), and Brannin McBee (now CCO) in New Jersey. The founders built expertise managing large, dense GPU clusters for maximum throughput. When Ethereum moved to proof-of-stake in late 2022 and mining economics collapsed, they had something valuable: operational knowledge of GPU infrastructure at scale, a physical fleet of hardware, and a thesis that AI training workloads would demand exactly what they had built.

The pivot to GPU-as-a-Service happened in early 2019. By the time GPT-4 launched in 2023 and demand for GPU compute exploded, CoreWeave was already operating at meaningful scale with enterprise customers in place.

**Headquarters:** Livingston, New Jersey (with major operations in North Dakota, Wyoming, Pennsylvania, West Texas, Nevada, Ontario, UK, Norway, Sweden, and Spain)  
**Employees:** ~2,100–2,200 as of early 2026 (peaked at ~2,390 in late 2025)  
**Status:** Public company, Nasdaq: CRWV, IPO March 28, 2025

---

## Funding and Financials

### Pre-IPO Capital

CoreWeave raised at extraordinary scale before going public, combining equity and debt financing:

- **Series B**: $221M led by Magnetar Capital (with NVIDIA participation)
- **Series B extension**: $200M, also led by Magnetar
- **Series C (May 2024)**: $1.1B led by Coatue
- **Debt facility (August 2023)**: $2.3B led by Blackstone and Magnetar, joined by Coatue, DigitalBridge, BlackRock, PIMCO, and Carlyle
- **Debt facility (May 2024)**: $7.5B led by Blackstone and Magnetar

Total pre-IPO equity and debt raised exceeded **$12 billion**. This is not a conventional venture-funded company. The capital structure reflects a hardware-intensive business model: borrow at scale to buy GPU hardware, lease it under long-term contracts, collect recurring revenue.

Notable equity investors include NVIDIA (a strategic signal — NVIDIA benefits when CoreWeave wins), OpenAI, Fidelity, JPMorgan, Cisco, Pure Storage, BlackRock, Coatue, Jane Street, and angels Nat Friedman and Daniel Gross.

### IPO (March 2025)

CoreWeave priced its IPO at **$40 per share** on March 28, 2025 — below the expected $47–55 range. The IPO raised $1.5 billion. At $40/share, the company listed at approximately **$23 billion enterprise value** (~$30B including debt).

The flat first-day close disappointed analysts expecting a pop. The market's hesitation was rational: the company had a GAAP net loss of $863 million in 2024 on $1.9 billion in revenue, a capital structure relying on $10+ billion in debt, and 62% revenue concentration in a single customer (Microsoft).

Markets changed their mind quickly:
- Stock broke $100 on May 21, 2025
- 52-week range: $49.06 – $187.00
- As of May 2026: ~$136/share
- Market cap: approximately $74–77 billion
- Up ~240% from IPO price within 14 months

### Revenue

| Year | Revenue | YoY Growth |
|------|---------|-----------|
| 2023 | $229M | — |
| 2024 | $1.9B | +730% |
| 2025 | $5.13B | +170% |
| 2026 guidance | >$12B | ~+134% projected |

CoreWeave's 2025 revenue represents the fastest ramp to $5 billion annual revenue of any cloud platform. Adjusted EBITDA for FY2025 was $3.09 billion (+154% YoY), meaning the underlying business generates substantial cash before accounting for depreciation, debt service, and stock compensation.

The GAAP net loss for FY2025 was **$1.17 billion** — wider than 2024's $863 million loss. This is not a profitability crisis; it is the mathematical consequence of $14.9 billion in 2025 capital expenditures being depreciated over asset lifetimes while the revenue they generate scales up. The 2026 capex guidance of $30–35 billion will extend this dynamic.

### Contracted Backlog

CoreWeave's most important financial metric is its contracted backlog — revenue committed under signed customer agreements:

- **$25.9B** at IPO (March 2025)
- **$56B** as of Q3 2025 earnings
- **$66.8B** as of FY2025 earnings
- **$95B+** total pipeline (including announced but not yet fully booked deals)

A $66.8 billion backlog against $5.1 billion in 2025 revenue implies more than 13 years of revenue visibility at current rates — though actual deal durations are 3–7 years, not 13, so this reflects the acceleration of new agreements. The backlog grew faster than revenue in 2025: the company was signing new contracts faster than it was fulfilling existing ones.

---

## Infrastructure

### Scale

CoreWeave ended 2025 with:
- **43 data centers**
- **250,000+ GPUs** total fleet
- **850 MW** active power capacity

The 2026 plan targets more than **1.7 GW** of active power capacity — more than double 2025. This is not a gradual expansion; it is a commitment to remain ahead of demand from frontier AI labs whose compute requirements are growing at comparable rates.

### GPU Fleet

CoreWeave's fleet spans multiple generations of NVIDIA hardware:

- **NVIDIA A100** (40GB, 80GB) — legacy workloads, still widely deployed
- **NVIDIA H100 PCIe** — available on-demand
- **NVIDIA H100 HGX/SXM** — 8-GPU NVLink nodes for high-bandwidth training
- **NVIDIA GB200 NVL72** — CoreWeave was the **first cloud provider to offer GB200 NVL72 instances in general availability** (announced March 2025). Each NVL72 rack contains 36 Grace CPUs and 72 Blackwell GPUs in a liquid-cooled rack-scale design. Access is via bare-metal Kubernetes (CKS).
- **NVIDIA GB300 NVL72** — next-generation Blackwell also referenced in CoreWeave documentation

CoreWeave's early GB200 GA availability was a strategic milestone: frontier labs that needed Blackwell-generation hardware had limited alternatives. This first-mover advantage reinforces the NVIDIA relationship and customer lock-in.

### Networking

CoreWeave's networking stack is purpose-built for large distributed training:

- **NVIDIA Quantum-2 InfiniBand** at 400 Gb/s per GPU, rail-optimized topology
- **NVIDIA SHARP In-Network Computing** for reduced collective communication latency (all-reduce operations happen inside the network fabric, not at GPU endpoints)
- Clusters up to **110,000 GPUs** connected via a single InfiniBand fabric
- All new data centers (2025+) are **liquid-cooled** to support GB200/GB300 power densities

The 400 Gb/s InfiniBand HPC fabric is the most direct comparison point to on-premises HPC clusters at national labs. For distributed training across thousands of GPUs, network bandwidth and latency are often the binding constraint on efficiency. CoreWeave's InfiniBand deployment matches or exceeds what most customers could build on-premises — without the hardware procurement cycle.

### Regions

**United States:** New Jersey, North Dakota, Pennsylvania, Wyoming, West Texas, Nevada; Ontario, Canada  
**Europe (active/committed):** UK (£1.5B committed), Norway (active GB200 deployment at Bulk Infrastructure), Sweden, Spain ($2.2B committed)

European expansion is primarily driven by regional data residency requirements from enterprise customers and the Mistral, Cohere, and IBM agreements that require EU-based infrastructure.

---

## Products and Services

### CoreWeave Kubernetes Service (CKS)

The primary access mechanism. CKS is managed Kubernetes running on bare-metal GPU servers — combining Kubernetes orchestration with bare-metal performance (no VM overhead, no hypervisor layer between application and GPU). It integrates natively with Slurm, KubeFlow, and KServe.

This is not a low-friction entry point. CKS assumes Kubernetes proficiency. There is no "click here to launch a single GPU instance" workflow. Workloads are defined as Kubernetes manifests, jobs, or workflows. For ML engineers coming from on-premises HPC clusters or who already run Kubernetes in production, this is appropriate infrastructure. For individual researchers, it is steep overhead.

### AI Inference

CoreWeave offers three inference deployment models:

1. **Serverless Inference** — no infrastructure management, pay per request, automatic scaling. Lowest operational overhead.
2. **Dedicated Inference** — custom model weights deployed on dedicated GPUs, OpenAI-compatible API endpoints. For production models with consistent traffic and latency requirements.
3. **Inference on CKS** — full Kubernetes stack control for teams that need custom runtime, serving framework, or hardware configuration.

Nine of the ten largest AI model providers are CoreWeave customers as of May 2026, per company statements.

### Storage

- **CoreWeave AI Object Storage** — S3-compatible, high-performance for AI/ML workloads. The differentiating feature is **LOTA (Local Object Transfer Accelerator)**: data objects are cached on GPU node local disks, enabling up to **2 GB/s per GPU** data access. This significantly reduces the I/O bottleneck that limits large training runs when checkpointing or loading datasets.
- **IBM Spectrum Scale Storage** integration — used for the IBM partnership delivering GB200 Grace Blackwell AI supercomputers.

### CUDA Cloud Positioning

CoreWeave markets itself as a **"CUDA Cloud"** — meaning the entire stack, from physical hardware through networking to software platform, is designed exclusively for NVIDIA CUDA workloads. This is a positioning label, not a separate product, but it communicates something real: CoreWeave made no concessions to general-purpose compute. Every engineering decision was made in service of maximizing GPU utilization and training throughput.

---

## Pricing

### On-Demand Rates (as of Q1–Q2 2026)

| GPU | On-Demand Price |
|-----|----------------|
| H100 PCIe 80GB | ~$4.25/GPU/hr |
| H100 HGX (8× NVLink node) | ~$6.15/GPU/hr (~$49.24/8-GPU node/hr) |
| GB200 NVL72 | Enterprise-quoted |

**Reserved capacity discounts** of up to 60% are available on long-term contracts. H100 reserved pricing reaches as low as ~$1.45/GPU/hr on multi-year agreements.

### Important Caveats

CoreWeave does not offer self-serve onboarding. New customers go through a "Request a Meeting" process with sales — typically a multi-day qualification and configuration conversation before any instance access. **Minimum commitments** for reserved capacity are typically 3–6 months, with multi-year contracts as the norm for significant deployments.

There is no free tier. There are no trial credits. If you want to run a single H100 for an afternoon to test a model, CoreWeave is the wrong platform.

On-demand rates exist and are accessible once an account is established, but the enterprise price — the number that matters to the customer cohort CoreWeave actually serves — is always custom-quoted.

---

## Key Customers

CoreWeave's customer list reads as a who's who of the AI ecosystem:

**Microsoft** — largest single customer. Approximately 62% of 2024 revenue, ~67% of FY2025 revenue. Actively diversifying; Microsoft is expected to fall below 50% of contracted future revenue as other customers grow. The concentration risk is real but declining.

**OpenAI** — initial contract of up to $11.9B (announced at IPO, March 2025). Expanded by $4B (May 2025). Expanded again by $6.5B (late 2025/2026). Total OpenAI agreements: approximately **$22.4 billion**. OpenAI runs on Azure and CoreWeave simultaneously — a statement that even Microsoft's own cloud cannot provision at the scale and speed frontier labs require.

**Meta** — initial deal of $14.2B over six years (through December 2032). Expanded to **$21 billion** (announced April/May 2026). Meta's use case is AI inference at scale for products like the Meta AI assistant.

**Anthropic** — multi-year agreement announced May 2026 (financial terms undisclosed). Supports Claude model development and deployment at production scale.

**Jane Street** — $6B deal signed April 2026. The quantitative trading firm is using GPU compute for ML-intensive trading strategy research.

**IBM** — CoreWeave is delivering one of the first GB200 Grace Blackwell AI supercomputers to IBM, used for training next-generation Granite models.

**Others**: Cohere, Mistral AI, Google, Cloudflare, and hundreds of enterprise AI teams.

---

## How CoreWeave Compares

### vs. Hyperscalers (AWS, Azure, GCP)

CoreWeave's core thesis is that hyperscalers were engineered for general-purpose cloud compute, not GPU-dense AI training. AWS, Azure, and GCP must support virtual machines, networking abstractions, storage APIs, databases, serverless functions, and dozens of other services that create overhead in the control plane, the networking stack, and the hardware allocation model.

CoreWeave made none of those trade-offs. The CUDA Cloud design means every component — power infrastructure, cooling, networking, software platform — is optimized for one workload type. The result is higher GPU density per rack, faster cluster provisioning, and consistently lower inter-GPU communication latency.

The hyperscalers are responding with custom AI silicon (AWS Trainium, Google TPU, Azure Maia) to reduce NVIDIA dependence. CoreWeave benefits here: NVIDIA's preferred distribution strategy for GPU compute is CoreWeave, and NVIDIA's strategic investment and priority GPU supply agreement reflect this alignment. SemiAnalysis's ClusterMAX benchmark rates CoreWeave "Platinum" tier — the highest rating — for proven ability to operate and deliver 10,000+ GPU clusters reliably.

### vs. Lambda Labs

Lambda Labs targets individual researchers and small AI teams with self-serve onboarding, competitive H100 PCIe pricing ($2.99/hr on-demand, with reserved options), no minimum commitments, and no GPU count caps on access. Lambda is high-friction relative to AWS but dramatically lower-friction than CoreWeave.

CoreWeave offers things Lambda cannot yet: 250,000+ GPUs total fleet, GB200 NVL72 in GA, HPC-grade 400 Gb/s InfiniBand, 110,000-GPU clusters, and the enterprise SLAs and compliance posture that large organizations require. Lambda does not compete for OpenAI or Meta contracts. CoreWeave does not compete for individual researchers or early-stage startups.

### vs. RunPod

RunPod ($120M ARR, 750,000+ developers) is a different market entirely. RunPod serves individual developers and small teams with per-second billing, no commitments, a community P2P cloud tier, and dynamic pricing starting under $0.20/hr for consumer GPUs. RunPod's Serverless product competes with Modal; its Community Cloud competes with Vast.ai.

CoreWeave does not serve this market and does not try to. The two companies occupy non-overlapping positions in the GPU cloud landscape.

### vs. Vast.ai

Vast.ai is a P2P GPU marketplace with RTX 4090s at $0.30/hr and H100s under $2/hr. Its customer is a cost-sensitive researcher or startup who needs cheap GPU time and can tolerate variable quality, no SLA, and the risks of running workloads on third-party hardware. CoreWeave and Vast.ai do not share a customer profile.

---

## What CoreWeave Is Not

This section matters because the GPU cloud landscape can look homogenous from the outside.

**CoreWeave is not self-serve.** You cannot sign up, add a credit card, and launch an instance today. The sales and onboarding process takes days.

**CoreWeave is not cheap.** On-demand H100 rates are among the highest in the market. The value proposition is reliability, density, networking quality, and capacity at scale — not price per GPU-hour for small jobs.

**CoreWeave is not for small teams.** The minimum viable use case is an organization with a real infrastructure budget, compliance requirements, and AI workloads that require sustained GPU access. The Kubernetes interface assumes operational expertise that most individual ML practitioners do not have.

**CoreWeave is not profitable (yet) on a GAAP basis.** The $1.17B GAAP net loss in 2025 is a function of the capital structure, not a sign of business weakness — adjusted EBITDA was $3.09B — but the leverage is real and creates sensitivity to demand changes.

---

## Strengths

- **Scale and capacity**: 250,000+ GPUs, 43 data centers, 850 MW — the largest specialized GPU cloud fleet
- **First GA on GB200 NVL72**: No other cloud provider had Blackwell-generation hardware in GA at launch
- **HPC networking**: 400 Gb/s InfiniBand with SHARP in-network computing; 110,000-GPU clusters possible
- **NVIDIA partnership**: Priority GPU supply allocation during constrained periods; NVIDIA's preferred distribution partner
- **Contracted revenue visibility**: $66.8B backlog growing faster than revenue — extraordinary forward visibility
- **Proven at scale**: SemiAnalysis Platinum-rated for 10K+ GPU cluster reliability; OpenAI, Meta, Anthropic as reference customers
- **LOTA storage**: 2 GB/s per GPU local caching materially reduces training I/O bottlenecks
- **Revenue growth**: Fastest cloud platform to $5B annual revenue

## Weaknesses

- **No self-serve access**: Sales-mediated onboarding excludes the long tail of AI developers
- **High pricing**: On-demand H100 at $4.25/hr is 40–50% above Lambda Labs' on-demand rate
- **Customer concentration**: Microsoft still ~67% of FY2025 revenue; declining but still elevated
- **GAAP losses**: $1.17B net loss in 2025; $14.9B capex requires sustained high utilization
- **Leverage**: $7.5B+ in debt financing creates sensitivity to demand slowdowns
- **Steep learning curve**: CKS assumes Kubernetes expertise; no beginner-friendly interface
- **No AMD GPU support**: Exclusively NVIDIA — no path for AMD MI300X workloads
- **European expansion risk**: $2.2B+ committed to EU data centers that must be filled with contracts

---

## Who Should Use CoreWeave

**CoreWeave is the right platform if:**
- You are running large-scale AI training or inference workloads — hundreds to thousands of GPUs continuously
- You need enterprise SLAs, compliance posture, and long-term capacity commitments
- You require HPC-grade InfiniBand networking for distributed training efficiency
- You need GB200 NVL72 or access to the latest NVIDIA hardware before hyperscaler availability
- You are an AI lab, large enterprise AI team, or infrastructure provider (like Cohere or Mistral)

**CoreWeave is the wrong platform if:**
- You are an individual researcher or small startup without infrastructure expertise
- You need self-serve access or per-hour on-demand billing without commitments
- Budget constraints make $4.25/hr on-demand H100 pricing prohibitive
- Your workloads are small enough that Lambda Labs, RunPod, or Vast.ai can serve them

---

## The Bottom Line

CoreWeave is where frontier AI runs. OpenAI trains and deploys models on it. Meta runs inference for 3+ billion users through it. Anthropic uses it for Claude. The $66.8B contracted backlog is the most direct evidence that the largest AI compute buyers in the world have decided CoreWeave is reliable infrastructure worth long-term commitments.

The business model is unusual: borrow massively, buy GPUs, lease them on long-term contracts, collect predictable revenue. The risks are concentration (Microsoft dependency declining but not gone), leverage (billions in debt service), and the possibility that demand growth slows before the $30–35B 2026 capex is fully utilized. None of these are hypothetical concerns — they are priced into the stock at a $74B market cap that values the company at roughly 15× projected 2026 revenue.

For developers who want to run a single GPU instance: look at Lambda Labs, RunPod, or Vast.ai.

For organizations whose AI infrastructure is strategic — where the quality of the GPU cluster directly determines whether a model trains successfully, a product ships on time, or a research agenda advances — CoreWeave is the benchmark against which everything else is measured.

**Rating: 4/5** — Strongest enterprise GPU cloud in the market. Docked one point for the complete absence of self-serve access, pricing opacity at scale, and the GAAP loss trajectory that requires sustained demand to justify the capital structure.

---

*CoreWeave trades on Nasdaq under the ticker CRWV. This review is based on publicly available information as of May 2026.*


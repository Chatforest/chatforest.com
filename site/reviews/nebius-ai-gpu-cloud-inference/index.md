# Nebius AI — The European GPU Cloud Built from Yandex's Ashes

> Nebius AI (NASDAQ: NBIS) is the AI infrastructure company that rose from Yandex's split from Russia. NVIDIA-backed with $46B contracted backlog, owned EU data centers, and 547% YoY revenue growth.


**At a glance:** Nebius AI ([nebius.com](https://nebius.com/)) is an NVIDIA-backed GPU cloud and AI infrastructure company that re-emerged from the separation of Yandex N.V.'s Russia-based assets in 2024. NASDAQ-listed as **NBIS**, Nebius holds a **$46 billion contracted revenue backlog** — including a $19.4 billion deal with Microsoft and up to $27 billion with Meta — and reported **547% year-over-year revenue growth** in Q4 2025. Its unique structural advantage: **the only neocloud with significant owned GPU infrastructure on European soil**, positioning it to capture AI Act-driven EU data sovereignty demand that AWS, Azure, and GCP cannot easily match. **May 2026 update:** NVIDIA committed a **$2 billion strategic investment** (March 2026); Nebius acquired **Eigen AI** for $643 million (May 1, 2026), a 20-person MIT-alumni inference optimization startup; stock is up approximately 110% year-to-date. **Rating: 4/5.**

Nebius is part of our **[GPU Cloud category](/categories/gpu-cloud/)**.

---

## The Unusual Origin Story

To understand Nebius, you have to understand where it came from.

[Yandex](https://yandex.com/) was Russia's dominant internet company — search engine, maps, taxi, food delivery, autonomous vehicles, cloud computing. Founded in 1997 by Arkady Volozh and Ilya Segalovich, it was listed on NASDAQ (ticker: YNDX) and built world-class engineering at a scale that few European technology companies matched.

Then Russia invaded Ukraine in February 2022. NASDAQ halted YNDX trading almost immediately. The EU sanctioned Volozh personally in June 2022, despite him publicly calling the invasion "barbaric." The company entered a years-long restructuring to separate its Russian operations from its international ones.

In July 2024, the restructuring concluded: a Russian consortium paid $5.4 billion to acquire all Russia-based Yandex assets. The Dutch holding company — Yandex N.V. — retained the cloud and data center infrastructure, AI projects, autonomous vehicle research, and international businesses. It renamed itself **Nebius Group N.V.** in August 2024. EU sanctions on Volozh were lifted in March 2024 after an independent review. NASDAQ trading resumed under ticker **NBIS** on October 21, 2024. Volozh renounced Russian citizenship in February 2026.

What Nebius inherited from Yandex was significant: hundreds of experienced infrastructure engineers who had been building and operating GPU clusters and large-scale data centers since 2018, plus the physical data center infrastructure itself. Most AI infrastructure startups begin with a few engineers and a vision. Nebius began with operational depth.

---

## Business Structure: More Than a GPU Cloud

Nebius Group is a holding company with several distinct businesses. Understanding the structure matters because the financial picture spans multiple entities.

**Nebius AI Cloud** is the core product: NVIDIA-accelerated bare-metal GPU clusters, managed Kubernetes, managed Slurm, and object storage — purpose-built for AI training, fine-tuning, and inference workloads. This is where the hyperscale customer revenue (Microsoft, Meta) flows.

**Nebius AI Studio** is the developer-facing inference API: 54+ open-source models (DeepSeek, Llama, Qwen, Mistral, Flux, and others), OpenAI-compatible endpoints, text-to-image generation, and fine-tuning. Priced per token.

**Nebius Token Factory** (launched November 2025) is the enterprise inference platform: serverless OpenAI-compatible API with 99.9% uptime SLA, dedicated endpoints, sub-second latency, autoscaling to hundreds of millions of tokens per minute, and integrated fine-tuning and distillation pipelines. The May 2026 acquisition of Eigen AI — a 20-person MIT-alumni inference optimization startup — strengthens this product and gives Nebius a San Francisco Bay Area engineering presence.

**Avride** develops autonomous vehicle and delivery robot technology. It operates independently and is not backed by a major automaker or big tech company.

**TripleTen** is an edtech platform that reskills workers into tech careers: data science, business intelligence, cybersecurity, and AI-adjacent programs.

**Toloka** was an AI data platform (training data, RLHF, evaluation). As of Q2 2025, Nebius no longer holds majority voting power in Toloka, which now operates as an equity method investment. Toloka received strategic investment from Bezos Expeditions (Jeff Bezos's personal investment arm) and Shopify's CTO Mikhail Parakhin.

---

## Financial Performance: Extraordinary Growth, Significant Losses

The growth numbers are legitimately impressive.

**Q4 2025:** Revenue of $228 million — **547% year-over-year growth**. The core AI cloud business alone grew 830% year-over-year. Adjusted EBITDA margin: 24%. Operating cash flow: $834 million.

**Full Year 2025:** Annual recurring revenue (ARR) reached $1.25 billion at year-end, exceeding guidance.

**2026 Guidance:** Group revenue of $3 billion to $3.4 billion. Adjusted EBITDA margin of approximately 40%. ARR target of $7 billion to $9 billion by year-end — over half already contracted.

The caveat: Nebius is not profitable. Net loss in Q4 2025 was $249.6 million. The company is in heavy capital deployment mode, building data center capacity at pace. The $46 billion contracted backlog (discussed below) provides future revenue visibility, but execution risk at this scale is real.

**Market capitalization** as of early May 2026: approximately $44–49 billion. With 2026 guided revenue of $3–3.4 billion, the stock trades at roughly 13–16× forward revenue — elevated, but less extreme than some AI infrastructure peers once the contracted backlog is factored in.

---

## The $46 Billion Backlog

The two landmark customer deals define Nebius's near-term trajectory.

**Microsoft — $19.4 billion over five years.** Announced September 2025. The first compute tranche was delivered in November 2025; the second in February 2026. The agreement includes $7 billion in upfront payments and covers 100,000+ NVIDIA GB300 accelerators. This is one of the largest AI infrastructure commitments from a hyperscaler to a third-party neocloud on record.

**Meta — up to $27 billion over five years.** The Meta relationship began with a $3 billion deal in November 2025, expanded to $12 billion of dedicated infrastructure in early 2026, and potentially scales to $27 billion. Meta is using Nebius capacity for AI training at scale.

These two relationships represent a concentrated revenue dependency risk — if either deal were renegotiated or terminated, Nebius's revenue trajectory would change dramatically. That said, both Microsoft and Meta have strong incentives to see Nebius succeed: they have prepaid significant capital for GPU capacity that does not yet exist.

Beyond the hyperscalers, Nebius counts **Brave Software** (80 million+ users; uses Nebius for real-time AI summaries across 11 million+ daily queries at ~100% GPU utilization) and the **Israel National Supercomputer** (1,000 NVIDIA B200-equivalent accelerators; 70% allocated to high-tech companies for AI training, 30% to academic research) among production customers.

---

## GPU Cloud Pricing and Products

Nebius AI Cloud pricing (as of early 2026, per GPU-hour, bundled with vCPU and RAM):

| GPU | Price/hr | vCPUs | RAM |
|-----|----------|-------|-----|
| H100 HGX | $2.95 | 16 | 200 GB |
| H200 HGX | $3.50 | 16+ | 200+ GB |
| B200 | $5.50 | 20 | 224 GB |
| GB200 NVL72 | Contact | — | — |

Note: As of October 2025, GPU, vCPU, and RAM are bundled for H100, H200, and B200 instances — no separate compute charges.

The platform supports:
- **Managed Kubernetes** with topology-aware job scheduling
- **Managed Slurm** via Soperator (Slurm-on-Kubernetes), built for large-scale AI training clusters
- **Shared filesystem storage**: up to 1 TB/s read throughput
- **Object storage**: 2 GB/s per GPU throughput
- **Storage partnerships** with WEKA and VAST Data for high-performance storage
- **CLI and API access** for full IaaS-level control
- **Nebius AI Cloud 3.5** (March 2026): serverless AI features, reduced operational overhead for developer workloads

For comparison, CoreWeave H100 pricing runs ~$2.06–$2.25/hr (depending on configuration), RunPod Secure Cloud H100 ~$2.39/hr, and Lambda H100 ~$2.49/hr. Nebius's $2.95/hr is at the upper end of neocloud pricing for H100, reflecting the managed services and enterprise SLA included in the base price.

---

## Nebius AI Studio: The Developer Inference API

Nebius AI Studio is the company's answer to Together AI, Fireworks AI, and DeepInfra: a token-priced inference API over popular open-source models, with OpenAI-compatible endpoints.

**54+ models** as of May 2026, including:
- Meta Llama 3.1 (8B, 70B, 405B) and Llama 3.3 70B
- DeepSeek V3 0324 and DeepSeek R1 series
- Qwen series (multiple sizes)
- Mistral (7B, Mixtral 8x7B)
- Flux image generation models
- Aurora (xAI image model)

**Sample pricing (per million tokens):**
- Llama 3.1 8B: $0.03 (input + output)
- Llama 3.1 70B: $0.13 input / $0.40 output
- DeepSeek V3 0324: ~$3.00 (input + output)
- Flux image generation: per-image pricing

The API also supports fine-tuning: upload a dataset, fine-tune an open-source model on Nebius infrastructure, and serve the resulting model via the same API. This is a differentiator vs. pure inference providers like Together AI.

Regional deployment options allow routing to EU or US data centers — a direct compliance feature for GDPR workloads.

---

## Token Factory: Enterprise Inference

Token Factory, launched November 2025, targets production AI teams that need more than developer-tier inference. Key features:

- **Serverless, OpenAI-compatible API** with automatic scaling
- **99.9% uptime SLA** with dedicated endpoints
- **Sub-second inference** across 60+ open-source models
- **Autoscaling throughput**: handles hundreds of millions of tokens per minute
- **Integrated fine-tuning and distillation**: Nebius claims these pipelines reduce inference cost and latency by up to 70% for fine-tuned vs. foundation models
- **Transparent $/token pricing**: no idle GPU costs
- **EU or US regional deployment** at model-level granularity

The May 2026 Eigen AI acquisition ($643 million for ~20 engineers) positions Token Factory at the frontier of inference optimization. Eigen AI specializes in model compilation and kernel-level inference acceleration — the kind of deep work that Groq built custom hardware to achieve, but done in software on standard NVIDIA GPUs.

---

## Infrastructure Footprint

Nebius is building at a scale that matches its contracted backlog.

**Finland — European Anchor:**
- *Mäntsälä*: First Finnish facility, expanded to 75 MW operational capacity in early 2026.
- *Lappeenranta*: 310 MW AI factory announced, investment exceeding €8.5 billion (~$10 billion). First capacity expected 2027. Will be one of Europe's largest AI factories. Finland chosen for renewable energy grid, cool climate, and EU regulatory positioning.

**France:**
- AI factory near Lille, 240 MW capacity when fully deployed (timeline TBD).

**Iceland:**
- Colocation deployment in Keflavik; fully operational by end of Q1 2025. Renewable geothermal power.

**United States:**
- *New Jersey*: New data center with up to 300 MW capacity; first capacity targeting summer 2025.
- *Independence, Missouri*: First gigawatt-scale AI factory; approved 2026. This will be one of the largest single AI infrastructure commitments in the Midwest.

**Israel:**
- AI data center opened October 2025, among Israel's first public NVIDIA Blackwell GPU deployments. Selected to build and operate the Israel National Supercomputer: NIS 500 million+ (~$135–140 million) investment, NIS 160 million in government support.

**Capacity targets:**
- 800 MW to 1 GW connected by end of 2026 (5–6× expansion in a single year)
- More than 3 GW contracted by end of 2026
- 5+ GW by end of 2030 (committed under the NVIDIA strategic partnership)

The scale of this buildout is comparable to major hyperscaler expansions, not typical neocloud growth.

---

## The NVIDIA Relationship

Nebius has two distinct NVIDIA investment tranches:

**December 2024 — ~0.5% equity stake.** NVIDIA participated in Nebius's $700 million strategic equity raise alongside Accel and Orbis Investments. This established the relationship.

**March 2026 — $2 billion strategic investment.** NVIDIA committed $2 billion to Nebius, announced March 11, 2026 (shares jumped 16% on the news). The partnership covers the full AI stack: AI factory architecture co-design, production software collaboration, and early access to the latest NVIDIA GPU generations. The stated goal: enable Nebius to deploy more than 5 GW of capacity by end of 2030.

This kind of relationship — equity investment plus co-engineering plus preferred GPU access — is what separates Nebius from generic GPU resellers. CoreWeave has a similar strategic NVIDIA relationship. Few others do.

---

## The European Moat

This is arguably Nebius's most durable structural advantage.

The EU AI Act and GDPR together create strong demand for AI compute that processes European personal data on European soil. AWS, Azure, and GCP have European regions, but they are US-headquartered companies subject to US law, including the CLOUD Act — which allows US law enforcement to compel data access from US companies operating anywhere in the world. This is not theoretical: it is a documented procurement concern among EU enterprises, public sector entities, and any organization subject to the Schrems II ruling.

Nebius is headquartered in Amsterdam, incorporated in the Netherlands, with data centers in Finland and France. It is structurally European in a way that US hyperscalers cannot replicate without significant legal restructuring.

Among GPU neoclouds specifically, **Nebius is the only one with significant owned data center infrastructure on European soil.** CoreWeave, Lambda Labs, RunPod, and Fireworks AI are US-focused. Vast.ai routes workloads to wherever community-supplied GPUs are available. Nebius can credibly offer EU-resident compute under EU legal jurisdiction.

This advantage compounds with scale: the Lappeenranta and Lille facilities will give Nebius 550+ MW of European capacity by 2027, establishing a moat that will be expensive and slow for competitors to challenge.

---

## How Nebius Compares

**vs. CoreWeave (NASDAQ: CRWV):** CoreWeave is the most direct comparable — both are NVIDIA-backed GPU neoclouds with hyperscale customers and large contracted backlogs. CoreWeave is larger ($5.13B 2025 revenue vs. Nebius's run-rate ~$900M+ annualized), primarily US-focused, and has a longer track record with OpenAI. Nebius has the European structural advantage and a faster percentage growth rate from a smaller base.

**vs. Lambda Labs:** Lambda is simpler, more developer-friendly, and cheaper per GPU-hour. Nebius targets enterprise and hyperscale customers with managed infrastructure, SLAs, and compliance. Different market segments.

**vs. RunPod:** RunPod is developer/SMB-focused, marketplace-model, significantly cheaper (H100 Secure Cloud ~$2.39/hr vs. Nebius $2.95/hr). Nebius wins on SLA, managed services, compliance, and EU availability. Different audiences.

**vs. Together AI / Fireworks AI:** For inference API customers, the comparison is primarily on model selection, price, and latency. Nebius AI Studio competes here, with the added benefit of EU regional deployment. Token Factory targets enterprise inference, above what Together AI or Fireworks serve.

**vs. AWS/Azure/GCP:** Nebius is not a general-purpose cloud — it does not offer managed databases, serverless functions, CDN, SaaS integrations. For pure AI training and inference workloads, Nebius offers lower overhead, more competitive GPU pricing, and genuine European data sovereignty. For organizations that need a full cloud stack, hyperscalers remain the default.

---

## The Yandex Question

No Nebius review is complete without addressing the origin directly.

**The case for concern:** The company's founders and many engineers are Russian nationals. The separation from Russia was driven by external legal and financial pressure, not voluntary. The $5.4 billion paid to the Russian consortium for the Russian assets flowed to Russian investors. Some publications, particularly Ukrainian tech media, have characterized Nebius as "non-Russian Yandex managing to whitewash its image." EU ESG-focused institutional investors have been cautious. The reputational cloud is real.

**The case for confidence:** The structural separation was genuine. Russian assets were sold to Russian buyers. The Dutch holding company retained the international businesses. EU sanctions on Arkady Volozh were lifted after independent review in March 2024. Volozh renounced Russian citizenship in February 2026. NVIDIA, Accel, and Bezos Expeditions conducted thorough diligence before investing hundreds of millions to billions of dollars. Microsoft and Meta signed multi-billion-dollar infrastructure commitments. Israel — a country with particular sensitivity to Russian geopolitical entanglements — selected Nebius to build its National Supercomputer.

The engineering legacy from Yandex's cloud team is an asset, not a liability: years of operating large-scale GPU clusters before most Western neoclouds existed. Nebius entered the AI infrastructure race with operational depth that startups cannot buy.

For procurement teams with explicit "no Russian-origin vendors" policies, Nebius will remain off the list regardless of ownership structure. For everyone else, the risk appears priced in and diminishing over time.

---

## Strengths

- **$46 billion contracted backlog** — unprecedented revenue visibility for a neocloud
- **547% YoY revenue growth** in Q4 2025; 830% for core AI cloud
- **NVIDIA strategic partner** with $2B equity investment and preferred GPU access
- **Owned EU data center infrastructure** — structural GDPR/AI Act compliance moat
- **Full-stack AI platform**: raw GPU clusters → managed Kubernetes/Slurm → AI Studio → Token Factory enterprise inference
- **Eigen AI acquisition**: frontier inference optimization engineering at Token Factory level
- **Deep infrastructure DNA** from Yandex's decade of large-scale data center operations
- **5+ GW capacity target by 2030** under NVIDIA partnership — among the largest neocloud commitments globally

## Weaknesses

- **Yandex reputational overhang**: persistent concern among ESG-focused allocators and some enterprise procurement teams, even with structural separation complete
- **Net losses ongoing**: Q4 2025 net loss of $249.6 million; profitability subordinated to capacity buildout
- **Customer concentration**: Microsoft + Meta represent the majority of contracted backlog — contract risk is manageable but real
- **Q4 2025 revenue miss**: $228M vs. analyst estimate ~$247M — minor, but worth noting in a high-growth story
- **Late US market entry**: US data center capacity (New Jersey, Missouri) lags European buildout; CoreWeave has entrenched US hyperscaler relationships
- **AI Studio is not yet a market leader**: Together AI and Fireworks AI have longer track records; Nebius AI Studio is relatively new in the developer inference market

---

## Verdict

**Rating: 4/5**

Nebius is one of the most compelling infrastructure stories in AI right now — and it is underreported outside of financial media. A $46 billion backlog from Microsoft and Meta, a NVIDIA strategic partnership with $2 billion in equity and preferred GPU access, 547% year-over-year revenue growth, and a structural European data sovereignty moat that no US neocloud can replicate. The Eigen AI acquisition signals seriousness about the full inference stack, not just raw compute supply.

The deductions: the Yandex origin remains a reputational consideration for some buyers; the company is running significant net losses while building; customer concentration in the backlog is high; and AI Studio is not yet a must-choose inference API for most developers.

For EU-based enterprises with AI Act data residency requirements, Nebius may be the most important infrastructure vendor they haven't fully evaluated. For US-based teams, it is worth watching — particularly as the New Jersey and Missouri facilities come online. The NVIDIA partnership alone is a strong signal of where major GPU capacity will flow over the next five years.

*As of May 2026. Nebius Group N.V. (NASDAQ: NBIS). This review covers the full Nebius Group, with particular focus on Nebius AI Cloud, Nebius AI Studio, and Token Factory.*


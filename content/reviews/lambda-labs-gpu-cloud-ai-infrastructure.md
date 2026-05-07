---
title: "Lambda — The Superintelligence Cloud for Large-Scale AI Training and Inference"
date: 2026-05-08T13:00:00+09:00
description: "Lambda (lambda.ai) is an enterprise GPU cloud built for large-scale AI training and inference. 1-Click Clusters with 400 Gb/s InfiniBand, $1.5B Series E at $5.9B valuation, a multibillion-dollar Microsoft deal, and a $1.5B NVIDIA leaseback make Lambda one of the most strategically connected GPU clouds on the market."
og_description: "Lambda is the GPU cloud behind foundation model training at enterprise scale. $1.5B Series E (TWG Global, Nov 2025). $5.9B valuation. Multibillion-dollar Microsoft deal. NVIDIA as both investor and largest customer. 1-Click Clusters at 400 Gb/s InfiniBand. H100 at ~$3.78/hr, B200 at ~$4.99/hr. Rating: 4/5."
content_type: "Review"
card_description: "Lambda (lambda.ai) is an enterprise GPU cloud purpose-built for large-scale AI training and inference. Founded 2012 by Stephen and Michael Balaban in San Francisco. Raised $1.5B Series E (TWG Global) in November 2025 at $5.9B valuation. Closed a $1B senior secured credit facility in May 2026. Signed a multibillion-dollar multi-year AI infrastructure agreement with Microsoft. NVIDIA is simultaneously an investor, GPU supplier, and Lambda's largest single customer via an $1.5B, 18,000-GPU leaseback. 1-Click Clusters provide multi-node H100/H200/B200 GPU clusters with 400 Gb/s NVIDIA Quantum-2 InfiniBand. IPO targeting H2 2026."
last_refreshed: 2026-05-08
---

**At a glance:** Lambda ([lambda.ai](https://lambda.ai/)) is a San Francisco-based GPU cloud that has repositioned itself as the "Superintelligence Cloud" — infrastructure designed for foundation model training, large-scale distributed inference, and frontier AI workloads. Founded in 2012 by brothers **Stephen Balaban** (now CTO) and **Michael Balaban** (now CPO), Lambda raised a **$1.5 billion Series E** led by TWG Global in November 2025 at a **$5.9 billion valuation**. In May 2026, the company closed an additional **$1 billion senior secured credit facility**. The company has secured a **multibillion-dollar, multi-year deal with Microsoft** and maintains a uniquely intertwined relationship with **NVIDIA** — which is simultaneously an investor, the company's primary GPU supplier, and its single largest customer via a $1.5 billion, 18,000-GPU leaseback. **Rating: 4/5.**

Lambda is part of our **[GPU Cloud category](/categories/gpu-cloud/)**.

---

## Origin: From Facial Recognition to Frontier AI Infrastructure

Lambda's founding story is more useful than most: the Balaban brothers didn't start Lambda to build an AI cloud. They started it because they were running out of money buying GPUs to build a facial recognition product and needed a cheaper way to train neural networks.

Stephen Balaban had previously co-founded a neural network company that Apple acquired in 2013. Michael Balaban had built and scaled large backend infrastructure at Nextdoor (scaling from early-stage to 100M+ users). When the brothers started Lambda in 2012, they were solving their own problem — and that grounded-in-reality origin shaped the company's product instincts for a decade.

The early Lambda product was largely hardware: the Lambda Vector GPU workstation line, the Scalar and Hyperplane server lines. These were well-regarded among researchers at MIT, Stanford, Harvard, Caltech, and Apple — institutions and companies that needed serious GPU compute but didn't want to manage cloud complexity.

Lambda didn't pivot to cloud-first until well into the 2020s. By 2025, the shift was complete: in August 2025, Lambda discontinued its entire hardware product line. In September 2025, it deprecated its inference API and Lambda Chat products. The company stripped itself down to one business: providing GPU cloud infrastructure at scale.

The rebrand to "The Superintelligence Cloud" followed shortly after, positioning Lambda explicitly alongside the frontier AI research community rather than the broader ML practitioner audience it had historically served.

---

## The NVIDIA Relationship: Investor, Supplier, and Customer

Lambda's relationship with NVIDIA is unlike any other GPU cloud's — and understanding it is essential to understanding Lambda's competitive position.

**NVIDIA is an investor.** NVIDIA participated in Lambda's Series D ($480M, February 2025) and maintains a stake in the company.

**NVIDIA is Lambda's primary GPU supplier.** This is true of every GPU cloud, but Lambda has moved to formalize and deepen this dependency at each funding round, securing allocation of H100s, H200s, B200s, and GB300s ahead of competitors.

**NVIDIA is Lambda's single largest customer.** In a notable $1.5 billion leaseback arrangement, NVIDIA signed a four-year agreement to lease back 18,000 GPUs from Lambda. NVIDIA needed GPU capacity (to run its own AI models and developer programs) and chose to lease it from Lambda rather than buy the hardware itself. Lambda gets a major, creditworthy anchor customer. NVIDIA gets infrastructure capacity without balance sheet hardware.

This three-way entanglement — investment, supply, and revenue — is both Lambda's greatest advantage and a concentration risk worth acknowledging. Lambda has unparalleled access to NVIDIA hardware roadmaps and supply chain. But if NVIDIA's business relationships shift, or if NVIDIA decides to compete more directly in cloud, Lambda's position could be affected.

The relationship deepened further at GTC 2026, where Lambda was named a launch partner for **NVIDIA Vera CPU**, **NVIDIA STX**, and **NVIDIA Quantum-X800 InfiniBand Photonics Co-Packaged Optics (CPO)** — a next-generation 10,000+ Blackwell Ultra GPU AI factory that Lambda is building with this new networking technology.

---

## Products

### Lambda Cloud: Core GPU Infrastructure

Lambda Cloud is the core product. It offers:

**On-Demand Instances:** Single-node GPU instances that can be spun up in minutes, billed hourly. Available GPU types as of May 2026:

| GPU | VRAM | Hourly Price |
|-----|------|-------------|
| A100 SXM4 | 40GB / 80GB | ~$1.48/hr |
| H100 PCIe | 80GB | ~$2.86/hr |
| H100 SXM5 | 80GB HBM3 | ~$3.78/hr |
| H200 SXM | 141GB HBM3e | ~$4.49/hr |
| B200 SXM | 192GB HBM3e | ~$4.99–5.29/hr |
| RTX 6000 Ada | 48GB | Budget tier |
| GH200 | 96GB HBM3 | Available |

Lambda's B200 pricing is notably competitive. At ~$4.99/hr for 192GB HBM3e, the B200 delivers approximately 2× the VRAM and FLOPS of an H100 at 1.3× the H100 price — a meaningful cost-per-performance improvement for memory-bandwidth-constrained workloads.

**1-Click Clusters:** Lambda's flagship product for distributed training and large-scale inference. Multi-node GPU clusters provisioned and interconnected automatically, available from 16 to 512+ GPUs. Minimum reservation: one week.

1-Click Clusters are what separates Lambda from most developer-oriented GPU clouds. Each cluster is built with:
- **NVIDIA Quantum-2 InfiniBand at 400 Gb/s**, non-blocking fabric, rail-optimized topology
- **GPUDirect RDMA** peer-to-peer bandwidth up to 3,200 Gb/s
- **2×100 Gb/s Ethernet** per node for IP traffic
- **2×100 Gb/s Direct Internet Access** per node
- **Managed Kubernetes** available as cluster orchestration layer
- Optional network-attached persistent storage

This is enterprise-grade distributed training infrastructure, not community-pooled GPUs. Multi-billion-parameter model training requires consistent, low-latency, high-bandwidth interconnect between GPUs across multiple nodes. Lambda's InfiniBand fabric provides the foundation.

**Superclusters:** Lambda's highest tier — multi-thousand GPU deployments for frontier AI labs and hyperscale customers. These are effectively private GPU data centers built and operated by Lambda, typically secured under multi-year reserved agreements.

**Lambda Bare Metal Instances** (launched GTC 2026): Direct hardware access with no virtualization overhead, for customers whose workloads benefit from full hardware control. This was a gap in Lambda's product line relative to competitors; its launch in 2026 rounds out the portfolio.

**Lambda Stack:** Lambda ships all instances with a pre-configured AI software stack — PyTorch, TensorFlow, CUDA, cuDNN, and current NVIDIA drivers — reducing setup time from hours to minutes.

---

### Products Lambda Discontinued

Lambda's 2025 product rationalization is worth noting directly:

- **Lambda Vector, Vector One, Vector Pro workstations** — discontinued August 29, 2025. Existing warranties still honored; no new sales.
- **Lambda Scalar/Hyperplane servers** — discontinued August 29, 2025. Legacy hardware section archived on the website.
- **Lambda Chat** — conversational AI interface built on open-source models. Deprecated September 2025.
- **Lambda Inference API** — hosted model inference including DeepSeek R1 and other open-source models. Deprecated September 2025.

Lambda's reasoning, while not stated publicly in precise terms, is clear from the pattern: the company identified that its real market advantage is in large-scale GPU infrastructure, not in the higher-level layers of AI tooling where it competed against specialized providers. Stripping the product line down was a focus decision.

Teams that had adopted Lambda's Inference API for production workloads needed to migrate — to Together AI, Fireworks AI, Replicate, or self-hosted alternatives. Lambda gave notice but did not provide a migration path or partnership. That's worth noting for any team considering Lambda as a long-term platform.

---

## Financial Picture

Lambda's financial trajectory is one of the more striking in the GPU cloud category.

**Revenue growth:**
- 2022: ~$20M estimated annual revenue
- H1 2025: $250M+
- Trailing twelve months through H1 2025: $520M+
- Q3 2025: ~80% YoY growth rate

**Gross margins:** ~50% overall; ~61% on cloud-only revenue. These are strong margins for infrastructure — a sign that Lambda's reserved cluster agreements command meaningful pricing power above raw GPU leasing costs.

**Net loss:** ~$175M trailing twelve months through H1 2025. Lambda is not profitable. At $520M+ revenue, the ~$175M loss reflects capital expenditure and lease costs as Lambda scales GPU fleet and data center capacity.

**Funding history:**
- Series D: $480M, February 2025, NVIDIA + B Capital, $2.5B valuation
- Series E: $1.5B, November 2025, TWG Global + US Innovative Technology Fund, $5.9B valuation
- Credit facility: $1B senior secured, May 2026
- Pre-IPO round: ~$350M reportedly in discussion, Mubadala Capital (as of early 2026)

**IPO:** Lambda is targeting an H2 2026 public offering. Secondary market share prices have appreciated ~12% in the 90 days prior to the credit facility announcement.

The $1B credit facility (closed May 2026) was framed explicitly as fueling "gigawatt-scale AI infrastructure demand" — Lambda's roadmap calls for multiple AI factories in the 100–300+ MW range, requiring capital beyond what equity rounds alone could provide efficiently.

---

## Major Deals and Customers

**Microsoft:** In November 2025, Lambda announced a multibillion-dollar, multi-year agreement with Microsoft to deploy tens of thousands of NVIDIA GPUs — including GB300 NVL72 systems — in Lambda's liquid-cooled U.S. data centers. Microsoft has reportedly worked with Lambda for 8+ years; this deal formalizes and dramatically scales that relationship. Microsoft uses Lambda's infrastructure for its own AI workloads and model training.

**NVIDIA:** The $1.5B, 18,000-GPU leaseback described above. NVIDIA uses Lambda compute for developer programs, model testing, and inference at scale.

**Academic institutions:** MIT, Stanford, Harvard, Caltech are cited Lambda customers — a legacy of Lambda's hardware business that carried forward into cloud.

**Government:** U.S. Department of Defense is cited as a Lambda customer.

**Frontier AI labs:** Lambda's marketing cites major AI labs as customers; specific named relationships are limited due to confidentiality.

The Microsoft and NVIDIA leaseback together provide Lambda with substantial contracted revenue visibility — something that distinguishes it from GPU clouds that rely primarily on spot and short-term on-demand customers.

---

## Infrastructure Buildout

Lambda is not just buying GPU racks in third-party data centers. The company is building owned AI factory capacity:

**Kansas City, Missouri:** $500M AI factory announced October 2025. Initial 24 MW capacity, scalable to 100+ MW. Expected to open in 2026.

**GTC 2026 announcements:** Lambda announced it is deploying **NVIDIA Quantum-X800 InfiniBand Photonics CPO** networking in a new 10,000+ Blackwell Ultra GPU AI factory — one of the first deployments of this next-generation interconnect technology commercially.

**Vera Rubin NVL72 Superclusters:** Lambda is building superclusters using NVIDIA's upcoming Vera Rubin GPU architecture, with deployment targeted for H2 2026. Lambda was named a launch partner, securing early allocation.

Lambda's infrastructure buildout parallels CoreWeave's approach: own or control data center capacity, build large-scale NVIDIA GPU clusters, and sign long-term agreements with hyperscalers and frontier AI labs as anchor customers.

---

## Leadership and Team

Lambda underwent a significant leadership transition in early-mid 2026:

- **Michel Combes** — appointed CEO effective May 2026 (former CEO of SoftBank Group International, former CEO of Altice)
- **Stephen Balaban** — co-founder, moved to CTO role full-time with Combes' appointment
- **Michael Balaban** — co-founder, Chief Product Officer
- **John Donovan** — Chairman of the Board (former CEO of AT&T Communications)
- **Jerry Hunter** — Vice Chairman (former Chief Infrastructure Officer at AWS, former COO at Snap)
- **Leonard Speiser** — COO (joined January 2026)
- **Charles Fisher** — CFO (joined February 2026)

The pattern here is a deliberate shift to enterprise-scale operational leadership in preparation for IPO and gigawatt-scale infrastructure operations. Combes brings global CEO experience at massive telco-infrastructure companies. Donovan and Hunter bring deep hyperscaler and enterprise tech credibility.

This is not a scrappy startup leadership team anymore. Lambda is building toward a public company with institutional customers and billions in contracted revenue.

---

## Competitive Position

### Lambda vs. CoreWeave

CoreWeave is Lambda's most direct comparable — both are NVIDIA-backed GPU clouds with hyperscale enterprise customers and large contracted backlogs. CoreWeave is ahead on several metrics: $5.13B 2025 revenue vs. Lambda's ~$520M TTM, $66.8B contracted backlog vs. Lambda's undisclosed (but Microsoft deal alone is multibillion), and CoreWeave is already public (NASDAQ: CRWV).

Lambda's advantages: more competitive on-demand pricing (Lambda H100 SXM5 ~$3.78/hr vs. CoreWeave ~$4.76/hr), newer leadership team with enterprise-scale operations experience, and a faster growth rate off a smaller base. Lambda is the credible #2 enterprise GPU cloud to CoreWeave's #1 — and actively closing the gap.

### Lambda vs. RunPod

These serve different markets. RunPod targets individual developers and small teams who need cheap single-GPU access. Lambda targets enterprise AI teams that need multi-node clusters with enterprise SLAs and InfiniBand networking. The pricing gap reflects this: RunPod's H100 is available ~$2.49–3.49/hr vs. Lambda's ~$3.78/hr, but RunPod cannot provide 512-GPU InfiniBand clusters with guaranteed uptime for a major foundation model training run.

### Lambda vs. Modal

Modal is not really a competitor in Lambda's primary market. Modal is serverless GPU computing — pay per second, no instances to manage, developer experience over raw performance. Lambda is dedicated GPU infrastructure — multi-week cluster reservations, raw InfiniBand performance, no abstraction overhead. Teams doing serious distributed training need Lambda's kind of infrastructure; teams shipping inference applications likely prefer Modal's DX.

### Lambda vs. Vast.ai

Vast.ai is a peer-to-peer GPU marketplace offering the cheapest possible rates (~$1.50–2.50/hr for H100), but with community-owned hardware, no InfiniBand cross-node networking, and no enterprise SLAs. Lambda is production-grade infrastructure with real contractual commitments. Different risk profiles for different use cases.

---

## Weaknesses

**No spot/preemptible instances.** Lambda does not offer spot or preemptible pricing. AWS, GCP, RunPod, and Modal all offer lower-cost preemptible instances for fault-tolerant batch workloads. Lambda's on-demand pricing is the floor — there's no discount tier for interruptible jobs.

**More expensive than budget providers for single-GPU work.** For an individual developer running a fine-tuning job on one A100, RunPod or Vast.ai are meaningfully cheaper than Lambda. Lambda's value proposition is at the multi-node cluster level, not single-GPU.

**Limited built-in observability.** Lambda does not provide hyperscaler-level monitoring, alerting, and metrics tooling. Teams coming from AWS or GCP will find Lambda's operational observability more limited.

**No deploy-into-customer-cloud option.** Lambda doesn't support deploying its infrastructure into a customer's own cloud VPC, which blocks some security-conscious enterprise architectures.

**SOC2 compliance still in progress.** As of early 2026, Lambda is still working toward full SOC2 compliance. This is a procurement blocker for some regulated enterprise customers.

**Product discontinuation track record.** Lambda dropped its hardware line, its inference API, and its Chat product all within 12 months. Teams that built on Lambda's inference API had to migrate. This isn't necessarily wrong — the strategic focus is defensible — but it signals Lambda will prioritize its core GPU cloud business over adjacent products. Don't build on Lambda products outside its core infrastructure offering without considering that.

**NVIDIA concentration risk.** NVIDIA is simultaneously an investor, the company's primary GPU supplier, and its single largest customer. If that relationship changes — NVIDIA enters direct cloud competition, acquires a competitor, or shifts procurement — Lambda's position could be meaningfully affected.

**Net losses.** Lambda is burning ~$175M/year on $520M+ revenue. The path to profitability requires continued scaling of high-margin reserved cluster agreements and AI factory capacity utilization. There's a clear business logic, but it's a capital-intensive bet.

---

## Who Lambda Is For

Lambda is the right platform for:

- **Foundation model training at scale** — distributed runs across hundreds or thousands of GPUs where InfiniBand networking is not optional
- **Enterprise AI teams** that need reliable uptime, proper SLAs, and the credibility of a funded, institutional-grade provider
- **Academic institutions** doing frontier AI research (Lambda has a long history here from its hardware days)
- **Teams running sustained GPU workloads** where 1-week-minimum reserved cluster pricing is economically sensible

Lambda is less well-suited for:
- Individual developers who want cheap hourly access to a single GPU
- Teams looking for serverless inference (use Modal or Baseten)
- Teams that need preemptible/spot pricing for batch workloads
- Teams with strong compliance requirements (SOC2 not yet complete)

---

## Outlook

Lambda's trajectory over the next 12–18 months is one of the clearer ones in the GPU cloud sector: scale infrastructure, convert Microsoft and NVIDIA relationships into recurring revenue, reach SOC2 compliance, and list publicly in H2 2026.

The $1B credit facility closed in May 2026 is primarily a capacity buildout play — Lambda needs capital to build AI factories ahead of customer demand, not after. The Kansas City factory and the Blackwell Ultra GPU factory are the first of what Lambda expects to be a multi-gigawatt footprint.

The IPO, if it happens as planned, would be a defining moment. CoreWeave's March 2026 IPO established a public market valuation framework for GPU clouds: ~13× revenue. At Lambda's TTM revenue trajectory, that would imply a valuation well above its $5.9B private valuation by IPO time — assuming revenue growth continues.

Lambda has turned itself from a hardware-first AI tools company into a serious infrastructure player with $1.5B of fresh capital, a NVIDIA anchor relationship, a Microsoft enterprise deal, and a leadership team built for IPO-scale operations. That's a significant transformation executed in a short period. The question is whether Lambda can achieve the utilization rates and contracted backlog depth needed to run a profitable infrastructure business at gigawatt scale — a challenge that every GPU cloud, including CoreWeave, is navigating simultaneously.

---

## Summary

| | |
|---|---|
| **Website** | [lambda.ai](https://lambda.ai/) |
| **Founded** | 2012 |
| **HQ** | San Francisco, CA |
| **Founders** | Stephen Balaban (CTO), Michael Balaban (CPO) |
| **CEO** | Michel Combes (effective May 2026) |
| **Funding** | ~$2.36B equity raised + $1B credit facility |
| **Valuation** | $5.9B (Series E, November 2025) |
| **Key investors** | NVIDIA, TWG Global, B Capital, US Innovative Technology Fund |
| **Key customers** | NVIDIA (leaseback), Microsoft, U.S. DoD, MIT, Stanford |
| **GPU types** | A100, H100, H200, B200, GH200, RTX 6000 Ada |
| **H100 price** | ~$3.78/hr (SXM5); ~$2.86/hr (PCIe) |
| **B200 price** | ~$4.99–5.29/hr |
| **Networking** | 400 Gb/s NVIDIA Quantum-2 InfiniBand (1-Click Clusters) |
| **IPO** | Targeting H2 2026 |
| **Rating** | 4/5 |

**Rating: 4/5.** Lambda is the most strategically connected GPU cloud in the market below the hyperscaler tier — NVIDIA investor + supplier + customer, Microsoft as anchor enterprise client, and a leadership team assembled for public company operations. 1-Click Clusters with 400 Gb/s InfiniBand set the benchmark for accessible distributed training infrastructure. Deductions: no spot pricing, SOC2 still in progress, product discontinuation history outside core GPU cloud, and NVIDIA concentration risk that's unique among its peer group.

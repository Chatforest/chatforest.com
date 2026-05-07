---
title: "Lambda Labs Review: GPU Cloud for Serious ML Teams"
date: 2026-05-07
description: "Lambda (lambda.ai) is a GPU-native cloud built exclusively for AI workloads. We review its on-demand and reserved H100/B200 instances, 1-Click Clusters, Lambda Stack software, pricing, and competitive positioning after its $1.5B Series E and multi-billion-dollar Microsoft deal."
tags: ["ai-infrastructure", "gpu-cloud", "h100", "b200", "ml-training", "ai-computing"]
categories: ["reviews"]
rating: 4
author: "ChatForest"
---

Most cloud providers treat GPUs as one feature among many. Lambda (lambda.ai) treats GPUs as the entire business. Since pivoting from AI workstations to cloud infrastructure, Lambda has become one of the most-watched GPU cloud companies — not because it offers the cheapest compute, but because it offers the right compute with the least friction for ML teams who know what they need.

This review covers Lambda's cloud GPU instances, 1-Click Clusters, Lambda Stack software environment, pricing, the company's dramatic funding trajectory, and where it fits against alternatives like CoreWeave, Vast.ai, Modal, and the hyperscalers.

---

## Company Background

Lambda was founded in 2012 in San Francisco by brothers Stephen Balaban and Michael Balaban, both University of Michigan alumni. The company's original business was building deep learning workstations — GPU-equipped machines sold to researchers and labs who needed serious compute on-premise but couldn't afford hyperscaler bills.

The cloud pivot was gradual but decisive. By the mid-2020s, demand for cloud GPU access had eclipsed on-premise hardware, and Lambda had developed both the operational expertise to run GPU clusters reliably and a reputation in the ML community for honest, practitioner-friendly infrastructure. In August 2025, Lambda formally ended its on-premise hardware product lines — Vector workstations, Scalar servers, and Hyperplane multi-node servers — to focus entirely on cloud and software. Warranties on existing hardware remain honored.

Lambda Stack, the software environment originally bundled with those workstations, continues as an independent product. It is now used by over 50,000 machine learning teams globally.

### Funding and Scale

Lambda's funding trajectory tells the story of the GPU infrastructure boom better than most:

- **2017**: Gradient Ventures (Google's AI VC arm) — early seed
- **2025 Series D**: Valued at $2.5B
- **November 2025 Series E**: $1.5B, led by TWG Global. Post-money valuation: $5.9B. Investors include TWG Global, US Innovative Technology Fund, NVIDIA, B Capital, and Gradient Ventures. Total equity raised: ~$2.36B.

NVIDIA's position as both investor and customer is notable: NVIDIA signed a $1.5B agreement to lease back 18,000 GPUs from Lambda over four years, making NVIDIA Lambda's largest customer by revenue. The structure is unusual — NVIDIA essentially uses Lambda as an external GPU fleet for overflow compute — and signals confidence in Lambda's operational reliability at scale.

In November 2025, Lambda announced a **multi-billion-dollar, multi-year agreement with Microsoft** to deploy AI infrastructure powered by tens of thousands of NVIDIA GPUs, including GB300 NVL72 systems, in Lambda's liquid-cooled U.S. data centers. The deal includes up to 200 megawatts of data center capacity and is being executed in phases through 2026.

**Revenue**: Lambda generated approximately $425M in 2024, with 70% year-over-year growth. The company serves 5,000+ customers including Fortune 500 enterprises, research institutions, and AI startups.

### Leadership Transition (May 2026)

In May 2026, Lambda announced a significant leadership restructuring. Co-founder Stephen Balaban moved from CEO to **CTO**, focusing on technology strategy and product vision. Co-founder Michael Balaban became **Chief Product Officer**. **Michel Combes** — a global infrastructure operator with extensive telecom and enterprise infrastructure experience — was appointed CEO. The transition signals Lambda's shift from a founder-led startup to an infrastructure company capable of managing gigawatt-scale deployments and enterprise customer relationships.

Lambda is reported to be in discussions for $350M in pre-IPO financing, with an IPO targeted for the second half of 2026.

---

## What Lambda Actually Is

Before reviewing specific products, it helps to clarify what Lambda is and is not.

**Lambda is a raw compute provider.** It rents you GPU time — by the hour, by the minute, or by the year — with a pre-configured software stack. You get a machine with NVIDIA hardware and Lambda Stack pre-installed, and you run whatever workload you want: training runs, fine-tuning, batch inference, research experiments.

**Lambda is not a model inference API.** It does not offer an OpenAI-compatible endpoint where you submit prompts and receive completions. If you want to call Llama 3.1 from your application without managing infrastructure, you want Together AI, Fireworks AI, or SambaNova — not Lambda.

**Lambda is not serverless.** Instances are persistent VMs that you spin up and pay for by the minute. There is no function-as-a-service model where your code runs on demand and you pay only for execution time. For that pattern, Modal is the right tool.

Lambda's sweet spot: ML teams who need sustained GPU compute for training or large-scale inference and want professional infrastructure without hyperscaler complexity or spot-instance instability.

---

## Products

### On-Demand Instances

Lambda's core product is on-demand GPU instances available at lambda.ai/instances. Key specs and pricing as of May 2026:

| GPU | Configuration | On-Demand $/hr |
|-----|--------------|----------------|
| NVIDIA B200 | 1×, 2×, 4×, 8× | ~$4.99–$5.29/GPU |
| NVIDIA H100 SXM | 1×, 2×, 4×, 8× | $2.99 |
| NVIDIA GH200 | — | Available |
| NVIDIA A100 80GB | 1×, 2×, 4×, 8× | $1.29–$1.49 |

Instances launch in under 60 seconds. Every instance comes with Lambda Stack pre-installed: CUDA, cuDNN, PyTorch, TensorFlow, and Jupyter ready to use without driver setup. No egress fees. Pay-by-the-minute with no minimum commitment on on-demand instances.

Lambda's H100 on-demand pricing has historically been among the lowest from any major provider for this GPU tier — a meaningful advantage for teams running multi-day training jobs where even small per-hour differences compound significantly.

### Reserved Instances

Teams with predictable, ongoing workloads can reserve capacity for 1-month, 3-month, or 1-year terms:

| GPU | On-Demand | 1-Year Reserved | Savings |
|-----|-----------|-----------------|---------|
| H100 | $2.99/hr | $1.89/hr | ~37% |
| B200 | ~$5.29/hr | ~$3.79/hr | ~28% |

Reserved instances are the right choice for production inference deployments, continuous pre-training runs, or research programs with stable compute budgets. The 1-year H100 rate at $1.89/hr is competitive with what many teams negotiate directly with hyperscalers.

### 1-Click Clusters

Lambda's 1-Click Clusters are multi-node GPU configurations designed for distributed training at scale. Configurations range from 16 to 2,000+ NVIDIA B200 or H100 GPUs, connected via high-bandwidth InfiniBand interconnect.

The "1-Click" label describes the provisioning experience: rather than manually configuring networking, MPI, and distributed training frameworks across dozens of nodes, Lambda pre-configures the interconnect topology and software environment. Teams get a cluster that PyTorch's distributed training libraries (FSDP, DeepSpeed, Megatron-LM) can address immediately.

For models requiring multi-node training — anything beyond roughly 70B parameters trained from scratch, or large fine-tuning runs at scale — 1-Click Clusters are Lambda's most differentiated product. Configuring InfiniBand networking correctly on a hyperscaler can take engineering days; Lambda's managed setup eliminates that.

Lambda's planned additions include bare-metal instances on NVIDIA Vera Rubin NVL72 (a next-generation GPU architecture), with production availability targeted for H2 2026.

### Lambda Stack

Lambda Stack is an open-source software stack (BSD-3-Clause) for managing AI framework installations on Ubuntu systems. It handles version coordination between CUDA, cuDNN, PyTorch, TensorFlow, Keras, and related libraries — the compatibility matrix that has caused experienced engineers hours of debugging.

Lambda Stack is pre-installed on all Lambda cloud instances and 1-Click Clusters. It can also be installed on non-Lambda Ubuntu machines via the public install script at lambda.ai/lambda-stack-deep-learning-software. Over 50,000 ML teams use Lambda Stack, many of them on their own hardware rather than Lambda's cloud.

The value proposition is straightforward: CUDA version mismatches are a perennial time sink in ML infrastructure. Lambda Stack manages the dependency graph so teams don't have to.

---

## Availability and Limitations

Lambda's most consistent user complaint is **GPU availability**. On-demand H100 and A100 instances have faced capacity constraints at peak demand, with independent tracking suggesting same-day A100 provisioning succeeded roughly 64% of the time during 2024. H100 availability improved in 2025 as Lambda expanded capacity, but the company has never offered spot instances that would let it sell otherwise-idle capacity at a discount.

The absence of spot instances is a deliberate architectural choice. Lambda positions its infrastructure as reliable, dedicated compute — the opposite of preemptible spot instances that can be reclaimed mid-training-run. For teams running multi-day jobs where interruption would waste days of compute, this is the right tradeoff. For teams comfortable writing checkpointing logic to exploit cheaper interruptible capacity, Vast.ai's marketplace model offers meaningfully lower prices.

Other limitations to understand before choosing Lambda:

- **No spot/preemptible instances** — cannot trade reliability for price
- **No serverless GPU** — persistent VMs only (compare: Modal for function-level GPU)
- **No LLM inference API** — Lambda is raw compute, not a model endpoint
- **No managed fine-tuning** — bring your own training code
- **Limited regions** — fewer geographic options than AWS, GCP, or Azure
- **Hardware business discontinued** — on-premise GPU systems are no longer sold

---

## Competitive Positioning

### vs. CoreWeave

The closest direct competitor. CoreWeave also offers dedicated H100/B200 GPU clusters with InfiniBand, at similar price points, with an enterprise sales motion. CoreWeave has deeper enterprise relationships and a broader geographic footprint; Lambda has a more practitioner-friendly onboarding experience and a stronger community reputation among ML researchers. For large enterprise contracts, both are viable. For individual researchers or small teams, Lambda's self-service provisioning is easier.

### vs. Vast.ai

Vast.ai operates a GPU marketplace: it aggregates spare capacity from independent GPU owners and offers it at significantly lower prices than managed providers, with a spot-like pricing model. For teams comfortable with preemptible instances and manual environment setup, Vast.ai can be 40-60% cheaper than Lambda for equivalent GPU types. Lambda wins on reliability, software environment quality, and SLA assurance. The choice depends on workload tolerance for interruption.

### vs. Modal

Modal is a serverless GPU cloud: Python functions decorated with `@app.function(gpu="H100")` run on-demand, billed by the second of execution, with sub-second cold starts. Lambda and Modal serve fundamentally different use cases. Lambda for sustained training runs and production inference where you want a persistent machine; Modal for bursty workloads, experimentation, and pipelines where spinning up dedicated infrastructure is wasteful. Many teams use both.

### vs. AWS / GCP / Azure

The hyperscalers offer GPU instances alongside their full cloud suites (databases, object storage, networking, ML platforms, etc.). For teams deeply integrated into AWS or GCP ecosystems, staying there has workflow advantages. Lambda's advantage is specialization: every Lambda decision is GPU-specific, pricing is transparent and competitive without negotiation, and the absence of hyperscaler pricing complexity (spot vs on-demand vs savings plans vs reserved) makes budgeting simpler. Lambda also does not charge egress fees — a meaningful cost difference for teams moving large datasets in and out of compute.

---

## The "Superintelligence Cloud" Positioning

Lambda's current brand messaging positions it as "the Superintelligence Cloud" — infrastructure purpose-built for the pre-AGI era of frontier model training and inference. This is partly genuine differentiation (GPU-exclusive focus, practitioner community, no-egress pricing) and partly the standard AI infrastructure land-grab rhetoric.

What's concrete: the NVIDIA relationship (18,000 GPUs, $1.5B lease-back), the Microsoft deal (tens of thousands of GB300 NVL72s, multi-billion-dollar commitment), and the $5.9B post-Series E valuation all reflect genuine scale. Lambda is building gigawatt-class AI infrastructure — not aspirational language, but actual data center deployments committed to by two of the largest companies in the AI stack.

What's less clear: how Lambda differentiates as the GPU cloud market matures. The key risk for any GPU cloud is commoditization: as hyperscalers improve their GPU offerings and spot prices on marketplaces compress margins, the middle tier of managed GPU clouds faces pressure from both above and below. Lambda's response appears to be moving upmarket — the Microsoft deal, the Supermicro AI factory partnership, the Vera Rubin roadmap — while maintaining practitioner goodwill at the developer level.

---

## Who Should Use Lambda

**Strong fit:**
- ML research teams and startups training models from scratch or fine-tuning at scale
- Teams running multi-day or multi-week jobs who need reliable, non-preemptible compute
- Organizations that want pre-configured software environments without hyperscaler complexity
- Teams running multi-node distributed training (1-Click Clusters with InfiniBand)
- Anyone who needs H100 or B200 at competitive rates without egress fees

**Poor fit:**
- Teams building inference APIs or production model endpoints (use Together AI, Fireworks AI, SambaNova)
- Teams with bursty GPU needs and tolerance for interruption (use Vast.ai or spot instances on hyperscalers)
- Teams whose GPU workloads are small or infrequent (use Modal for serverless GPU)
- Organizations needing broad geographic coverage (use a hyperscaler)
- Teams who want managed fine-tuning with no infrastructure management (use Replicate or Baseten)

---

## Verdict

Lambda is the cleaner, more practitioner-friendly alternative to hyperscaler GPU instances for teams that know what they need. Competitive H100 and B200 pricing, no egress fees, pre-configured Lambda Stack environment, and serious multi-node cluster capability make it a strong default for ML teams with sustained training or large-scale inference workloads.

The limitations are real: no spot instances, no serverless model, limited regions, occasional capacity constraints on popular GPU types, and no inference API for teams who want managed model serving. Lambda is raw compute, not a managed ML platform.

The company's trajectory — $5.9B valuation, NVIDIA as a customer, multi-billion-dollar Microsoft deal, IPO on the horizon — suggests Lambda is on the path from practitioner-friendly GPU rental to serious AI infrastructure provider. For teams who want to grow with it, Lambda offers both the current compute they need and a roadmap that tracks where frontier AI workloads are going.

**Rating: 4/5** — Best-in-class developer experience for dedicated GPU compute. Loses a point for no spot/serverless options, occasional availability constraints, and limited geographic coverage. Still the first GPU cloud most ML teams should evaluate.

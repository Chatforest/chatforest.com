# Vast.ai Review: The GPU Marketplace That Undercuts Everyone

> Vast.ai is a peer-to-peer GPU compute marketplace where H100s rent for $1.38/hr and RTX 4090s for $0.30/hr. We review its pricing model, interruptible vs. on-demand instances, Serverless product, SOC 2 certification, reliability trade-offs, and how it compares to Lambda Labs, RunPod, and CoreWeave.


When GPU prices matter more than convenience, most developers end up at Vast.ai. Not because the platform is polished or enterprise-ready — it is neither — but because it consistently offers compute at 3–8× below hyperscaler rates and 2–3× below managed GPU clouds like Lambda Labs. For AI developers running fine-tuning jobs, diffusion training runs, or batch inference pipelines who can tolerate variability in exchange for radical cost savings, Vast.ai is often the best answer.

This review covers Vast.ai's marketplace model, instance types and pricing, technical capabilities, the 2025 Serverless launch, reliability risks, SOC 2 certifications, and where it fits in the GPU cloud landscape for 2026.

---

## Company Background

Vast.ai was incorporated on June 28, 2016 as a Delaware C corporation. Co-founders Jake Cannell (CEO) and Christian Cannell built the platform over two years before launching publicly — not via a press release, but via a Reddit post. The origin thesis was simple: the world is full of underutilized GPUs — in gaming rigs, defunct crypto mining farms, university labs, and small data centers — while ML developers are paying hyperscaler rates for the same class of hardware. Connect the two sides and both win.

Travis Cannell (Jake's brother) later joined as COO. The company is headquartered in Los Angeles, California and as of 2025 maintains a team of approximately 38 people — intentionally lean by design.

One naming note worth flagging: Vast.ai (vast.ai, the GPU marketplace) is a completely different company from VAST Data (vastdata.com), an AI storage platform with a $30B valuation backed by NVIDIA. The two companies share a confusingly similar name and frequently appear together in search results. This review covers Vast.ai — the GPU rental marketplace.

### Funding

Vast.ai has raised approximately **$4 million** in early-stage funding from DRW Holdings and Nazare. That is an extraordinarily small war chest for a company of its standing in the GPU cloud market. The company has grown primarily on organic momentum, founder conviction, and a pricing model that makes marketing largely unnecessary — when your H100 prices are 2–3× cheaper than the next option, word spreads fast.

By early 2026, Vast.ai served **120,000+ developers** and **14,000+ monthly paying customers**. Monthly active paying customers grew 16× year-over-year from early 2025 to early 2026; new signups grew 27× in the same period. In 2025, the company was ranked **#11 on Ramp and Brex's fastest-growing software vendors** list — ahead of Groq (#12) and Supabase (#23) — based on spending growth across their business card portfolios.

---

## How It Works: The Marketplace Model

Vast.ai operates a two-sided marketplace — an Airbnb for GPU compute.

**Supply side (Hosts):** Hardware operators install Vast's hosting software, configure their machines, set their prices, and go live. Anyone from a solo owner with a gaming PC to a professional colocation operator can list capacity. Vast handles customer acquisition, billing, payment processing, and support logistics. Hosts keep the majority of rental revenue.

**Demand side (Renters):** Users browse a marketplace interface or query via REST API to find available capacity. Filtering covers GPU model, VRAM, price, reliability score (an automated metric Vast computes per host), location, disk type, and network connectivity. You pick what fits your workload and launch.

**Vast's cut:** Vast takes a platform fee on each transaction. The exact percentage is not publicly disclosed.

**Price dynamics:** Because hosts set their own prices and compete with each other, the marketplace creates natural downward price pressure. This is why Vast.ai prices consistently undercut managed clouds — there is no artificial floor. Supply and demand determine what GPUs cost on any given day.

---

## Pricing: How Much Cheaper Is It?

Vast.ai's headline advantage is price. The table below reflects approximate on-demand (lowest-available) prices as of May 2026. Individual results vary by host and demand.

| GPU | Vast.ai (on-demand) | Lambda Labs | AWS |
|---|---|---|---|
| RTX 4090 | ~$0.29–0.30/hr | ~$0.80–1.25/hr | Not available |
| A100 80GB | ~$0.50–0.75/hr | ~$1.29–1.49/hr | ~$4.10/hr |
| H100 PCIe | ~$1.38–2.00/hr | ~$2.49/hr | ~$6.98/hr |
| H100 SXM | ~$1.80–2.49/hr | $2.99/hr | ~$8.50/hr |

For cost-sensitive workloads, the A100 comparison is striking: Vast.ai at $0.50–0.75/hr versus AWS at $4.10/hr for the same GPU class. The 5–8× gap is real, though the comparison is not perfectly apples-to-apples (AWS includes SLA, enterprise support, and a managed environment that Vast.ai explicitly does not offer).

### Three Instance Types

**On-Demand:** Fixed price, uninterrupted access. The host cannot reclaim the machine while you are running. This is the closest Vast.ai gets to managed cloud reliability — still dependent on the host's uptime, but your job won't be terminated by a competing bidder.

**Interruptible (spot-equivalent):** You set a maximum bid price. If a higher bidder appears or the host reclaims the machine, your instance is paused or terminated. Interruptible instances can be **50%+ cheaper** than on-demand rates from the same hosts. Best for fault-tolerant batch jobs with robust checkpointing. Dangerous for long multi-node training runs without automatic restart logic.

**Reserved:** Prepay for 1-, 3-, or 6-month terms. Discounts up to 50% off on-demand pricing. Available on select well-established hosts. Best for predictable workloads where you have already validated the host's reliability.

**Billing:** Per-second granularity on all instance types. No minimum charge. This makes Vast.ai particularly useful for short, targeted jobs — you pay for exactly what you use.

---

## Technical Capabilities

### Instances and Hardware

Vast.ai supports **68+ GPU types** across the catalog — the widest selection of any GPU rental platform. This includes:

- **NVIDIA**: GTX 1080 through RTX 5090, all A-series (A2 through A100), H100 PCIe and SXM, H200, B200
- **AMD**: Radeon Instinct MI25+, Radeon VII, Radeon PRO W7900/W7800, Radeon RX 7900 series via ROCm

AMD support is notable — Vast.ai was the first GPU rental marketplace to offer AMD GPU compute. Most competing managed platforms are NVIDIA-only.

The RTX 5090 crossed 1,000 machines on-platform in 2025. H200 and B200 were added to the catalog in 2025. RTX PRO 6000 WS was added in early 2026.

### Container Model

Every instance is a Docker container. You specify a Docker image at launch — from Docker Hub, any registry, or a custom image built locally. Vast provides a set of official base images covering CUDA versions and common ML frameworks, but these are starting points rather than requirements.

The template system maps directly to `docker create` parameters, giving you granular control over the runtime environment. GPU passthrough, environment variables, volume mounts, port mappings, and entrypoints are all configurable. If you can run it in Docker, you can run it on Vast.ai.

### Networking and Connectivity

Instances do not receive dedicated public IPs. Instead, ports (SSH on 22, Jupyter on 8080, and up to 64 custom ports) are mapped to random external ports on the host's public IP address. The Vast console shows you the exact mapping for each instance.

Connectivity quality varies substantially by host. Some hosts are in data centers with 10 GbE+ interconnects; others are residential ISP connections with variable bandwidth. For latency-sensitive workloads or large model weight transfers, filtering by host network performance score matters.

### Multi-Node and Clusters

Vast.ai supports multi-node clusters where hosts register sets of machines sharing a LAN subnet. These clusters support NCCL for distributed training — you can run multi-node PyTorch DDP or DeepSpeed jobs across machines.

Select cluster offerings include InfiniBand networking for high-throughput distributed training, though the InfiniBand inventory is smaller and less reliably available than dedicated cluster providers like CoreWeave. For production-grade multi-node jobs requiring consistent bandwidth fabric, Vast.ai's cluster support is capable but uneven.

### Storage

Disk allocation is set at instance creation and cannot be resized while the instance is running. Storage quality varies by host: NVMe scratch disks (fast model loading) versus SATA drives (slower). For workloads involving large model weights — loading a 70B+ parameter model — the storage performance difference between an NVMe host and a SATA host is significant. The search interface surfaces disk type information.

### API and CLI

Vast.ai provides a full REST API and an official Python CLI (`vastai`). The CLI supports instance search, launch, management, and teardown. The API supports the same operations programmatically. This makes Vast.ai compatible with automated training pipelines, CI/CD integration, and batch job orchestration. A Python SDK is also available via PyPI.

### Launch Modes

Three options at launch:
- **Entrypoint**: Run a command and exit. Good for batch jobs.
- **SSH**: Interactive shell access via an SSH client. Standard development workflow.
- **Jupyter**: Browser-accessible Jupyter Notebook. Ideal for exploratory work.

---

## Vast.ai Serverless (2025)

The most significant 2025 product launch was **Vast.ai Serverless** — a fully automated GPU inference layer that abstracts individual instance management.

Instead of finding a host, launching an instance, loading a model, managing uptime, and tearing down when done, Serverless handles this automatically: you define your workload, and Vast routes it to available compute, scales up under load, and scales down to zero when idle. Billing is per-request rather than per-hour.

Serverless directly targets the inference market — which, per Morgan Stanley estimates, is projected to account for 70% of GPU cloud spend by late 2026. It is Vast.ai's answer to RunPod Serverless, and it extends the marketplace pricing advantage into the inference layer.

Serverless is the right product for developers who want Vast.ai's cost structure without the operational overhead of instance lifecycle management.

---

## Reliability and Risk: The Honest Picture

Vast.ai's price advantage comes with a clear and documented trade-off. Understanding this trade-off is the single most important thing a prospective user can know.

### No SLA

Vast.ai's Terms of Service explicitly state that it cannot guarantee service availability and may experience hardware, software, or maintenance interruptions. There is no uptime SLA. Full stop.

This is structurally different from Lambda Labs, CoreWeave, or AWS, which provide service-level commitments (even if imperfect). On Vast.ai, you are renting capacity from a third party, through a marketplace, from a host who may or may not maintain their hardware with the same rigor as a professional data center.

### Host Quality Variability

The defining reliability risk. When you launch an instance on Vast.ai, you are running on hardware operated by an unknown party. Host quality ranges from well-maintained professional colocation infrastructure to gaming rigs in someone's apartment.

Vast.ai publishes a **reliability score** per host — a computed metric based on historical uptime data — and makes it filterable in the search interface. Sorting by reliability score and sticking to verified hosts with long track records significantly reduces variability. But it does not eliminate it.

The practical implication: treat Vast.ai workloads as inherently fault-tolerant. Build checkpointing into training runs. Do not run production inference serving on Vast.ai interruptible instances without a fallback. Design for interruption.

### Interruptible Instance Risk

Interruptible instances are terminated when a higher bidder appears or the host reclaims capacity. For long multi-node distributed training jobs, an interruptible instance termination mid-run is expensive in both time and lost computation. NCCL hangs on failed worker nodes. Automatic recovery requires coordinated checkpointing and restart logic.

If your job cannot tolerate interruption, use on-demand instances, not interruptible.

### Security Posture

Your workloads run on third-party hardware. Model weights, training data, and intermediate outputs are physically resident on machines operated by unknown hosts. For workloads involving sensitive data — healthcare, finance, proprietary model weights, personal data — this is a material security concern.

Vast.ai achieved **SOC 2 Type I certification in April 2025** and **SOC 2 Type II certification later in 2025**. This is a meaningful step and signals a deliberate push toward enterprise readiness. But it does not change the physical reality that your data is on someone else's machine.

For HIPAA, FedRAMP, or sensitive IP workloads, RunPod Secure Cloud, Lambda Labs, or CoreWeave provide stronger isolation guarantees.

---

## SOC 2 Certifications

SOC 2 Type I (April 10, 2025) assessed whether Vast.ai's security controls were appropriately designed. SOC 2 Type II assessed whether those controls operated effectively over a defined period. Achieving both in a single year is a meaningful compliance milestone for a bootstrapped 38-person company, and it opens enterprise procurement conversations that were previously unavailable.

Vast.ai's security model covers the platform itself — the API, the control plane, billing, identity management, and data transit. Host-side security is governed by host verification procedures and contractual obligations, but Vast.ai cannot enforce on-premises security at each of 1,400+ independent host operators.

---

## Scale and Platform Status (2026)

- **17,000+ GPUs** from **1,400+ providers** in **500+ locations** worldwide
- **68+ GPU types** supported
- **120,000+ registered developers**
- **14,000+ monthly paying customers**
- Monthly paying customer growth: **16× year-over-year**
- New signup growth: **27× year-over-year**
- Named **#11 fastest-growing software vendor** by Ramp and Brex (2025)

For a bootstrapped company that launched via a Reddit post, these numbers are extraordinary. Vast.ai grew faster in 2025 than most VC-backed GPU cloud competitors.

---

## Competitive Positioning

### Vast.ai vs. Lambda Labs

Lambda Labs is the clearest direct comparison. Both serve AI developers who want GPU compute without hyperscaler complexity. The differences:

- **Price**: Vast.ai wins decisively. H100 PCIe at $1.38/hr on Vast versus $2.99/hr at Lambda. A100 at $0.50/hr on Vast versus $1.29–1.49/hr at Lambda.
- **Reliability**: Lambda wins. Managed infrastructure with consistent uptime. Vast depends on host quality.
- **No egress fees**: Both offer this. Lambda makes it a marketing point; Vast.ai matches it as a natural consequence of its marketplace model.
- **Multi-node clusters**: Lambda's 1-Click Clusters are more polished and more reliably available. Vast.ai clusters are capable but uneven.
- **Serverless / inference**: Vast.ai Serverless. Lambda has no serverless product.
- **Target user**: Lambda for teams that need reliability and don't want to manage variability. Vast.ai for teams where cost is the primary constraint.

### Vast.ai vs. RunPod

RunPod is the closest architectural peer — also a marketplace/managed hybrid. Differences:

- **Price**: Comparable. Both undercut managed clouds. Vast.ai often has lower floor prices due to a larger host pool.
- **Managed tier**: RunPod Secure Cloud offers dedicated, managed infrastructure with stronger isolation. Vast.ai has no equivalent managed tier.
- **Serverless**: Both offer it. RunPod Serverless launched earlier and has more documented production use cases.
- **AMD support**: Vast.ai first-to-market on AMD GPUs. RunPod AMD support is limited.

### Vast.ai vs. CoreWeave

These serve fundamentally different customers. CoreWeave targets enterprise at scale — HPC networking, dedicated infrastructure, compliance frameworks, and a $19B valuation funded by $1.1B in equity plus $7.5B in debt. Vast.ai targets cost-sensitive developers who will accept reliability trade-offs for price. There is minimal overlap in customer profile.

### Vast.ai vs. Hyperscalers (AWS/GCP/Azure)

The price gap on GPU compute is the entire argument for Vast.ai over hyperscalers. AWS H100 at $6.98/hr versus Vast.ai at $1.38–2.00/hr. The 3–5× premium on AWS buys managed security, VPC networking, IAM, compliance frameworks, and tight integration with the rest of the AWS stack. For GPU compute in isolation, that premium is hard to justify on a budget.

---

## Pricing Summary

| Use Case | Recommended Instance Type | Typical Savings vs. Lambda |
|---|---|---|
| Exploratory research / dev | Interruptible | 60–70% |
| Batch fine-tuning with checkpointing | Interruptible or On-Demand | 40–60% |
| Production training (no SLA) | On-Demand (high-reliability host) | 30–50% |
| Long-term production workloads | Reserved | 30–50% |
| Inference API at variable scale | Serverless | Varies |

---

## Who Should Use Vast.ai

**Good fit:**
- AI researchers and engineers running fine-tuning, training, or batch inference where cost matters more than guaranteed uptime
- AI startups on tight budgets who have built fault-tolerant pipelines and want maximum GPU hours per dollar
- Developers experimenting with large models (RTX 4090 at $0.30/hr makes running 70B models accessible)
- Teams running AMD GPU workloads — Vast.ai has the widest AMD catalog
- Anyone who needs a rare GPU type not available on managed platforms

**Poor fit:**
- Customer-facing inference products with uptime SLAs
- HIPAA, FedRAMP, or other regulated workloads requiring data residency guarantees
- Teams without devops capacity to manage instance lifecycle and failure recovery
- Enterprise procurement requiring legal SLA paperwork

---

## Bottom Line

Vast.ai occupies a unique and durable position in the GPU cloud landscape: the lowest-cost, widest-selection GPU compute marketplace in the world. The 2025 SOC 2 certifications represent meaningful progress toward enterprise readiness. The Serverless product extends the pricing advantage into inference. The 16× customer growth and 27× signup growth validate that demand for this positioning is real and accelerating.

The reliability and security limitations are real and documented. For workloads that can tolerate them — and many can — Vast.ai delivers value that no other platform matches.

**Rating: 4/5** — Best price-to-compute ratio in the GPU cloud market. Dings for no SLA, host quality variability, security trade-offs on sensitive workloads, and limited enterprise readiness outside of the new SOC 2 scope.

---

*ChatForest reviews AI infrastructure based on publicly available information, documentation, and pricing data. We do not receive compensation from reviewed companies.*


# Anyscale Review: The Managed Ray Platform for Serious AI Workloads

> Anyscale built the Ray open-source framework, transferred it to the PyTorch Foundation in 2025, and now sells a managed platform that runs on top of it. Here's what that means for AI teams evaluating distributed computing infrastructure.


There's a particular kind of infrastructure company that earns credibility before it earns revenue: the kind that builds the foundational open-source tool that every serious AI team eventually touches. Anyscale is that company. Its founders wrote Ray at UC Berkeley, watched it become the distributed computing substrate for Character.ai, Physical Intelligence, Runway, and Coinbase — and then, in October 2025, donated it to the PyTorch Foundation so it could grow without the shadow of vendor control.

That governance move is the defining strategic act of Anyscale's recent history. Understanding why they made it, and what they kept for themselves, is the key to understanding what Anyscale is and who it's for.

## The Founders and the Framework

Anyscale was founded in 2019 in San Francisco by a group of UC Berkeley researchers who had built Ray at the university's RISELab:

- **Ion Stoica** — professor at UC Berkeley, previously co-founder of Databricks (Apache Spark's commercial home). Two successful open-source commercialization plays from the same lineage.
- **Robert Nishihara** — PhD student at RISELab, primary architect of Ray's core scheduling and distributed object store
- **Philipp Moritz** — PhD student at RISELab, original Ray author
- **Michael I. Jordan** — UC Berkeley professor and one of the most cited machine learning researchers in the world, advisor-level co-founder

The origin is academic, but the business model is not. Ray started as a tool for distributed reinforcement learning — a way to parallelize Python across a cluster without rewriting your code in a distributed framework. It turns out that problem is identical to the problem of scaling AI training, inference, and data pipelines. Ray became the connective tissue for serious AI infrastructure.

By the time Anyscale transferred Ray to the PyTorch Foundation in October 2025, the framework had accumulated 500 million+ downloads, 41,000+ GitHub stars, and a download growth rate of "nearly 10x" in the prior year. It drives what Anyscale calls "billions of dollars of annual compute consumption."

## Funding and Business Status

Anyscale has raised approximately $281 million across three rounds:

| Round | Date | Amount | Lead |
|-------|------|--------|------|
| Series A | February 2019 | $20.6M | Andreessen Horowitz |
| Series B | October 2020 | $40M | New Enterprise Associates |
| Series C | October 2021 | $199M | New Enterprise Associates |

The company reached unicorn status ($1B valuation) in December 2021. Notably, no Series D has been announced as of May 2026 — over three years post-raise. This is unusual for a company of Anyscale's scale and profile. It may indicate the company is operating near profitability on its existing runway, or it may signal a deliberate holding pattern ahead of a larger raise or IPO. Revenue figures have not been publicly disclosed.

The employee count of roughly 664 (as of early 2026) is lean for a company with this market position, which generally suggests efficient operations rather than a growth-at-all-costs posture.

## The PyTorch Foundation Transfer: A Databricks Play

On October 22, 2025, Anyscale transferred Ray's governance, intellectual property, and development roadmap to the PyTorch Foundation under the Linux Foundation. The move drew immediate comparisons to HashiCorp/Terraform, Docker, and Kubernetes governance models — all cases where neutralizing open-source ownership accelerated enterprise adoption.

The Databricks parallel is exact. Ion Stoica co-founded Databricks, which built its multi-billion-dollar business on top of Apache Spark — an open-source project it donated to the Apache Foundation. Anyscale is executing the same play with Ray and the PyTorch Foundation.

**What Anyscale transferred:**
- Ray's governance and IP
- Development roadmap authority
- The Ray brand as a neutral open-source project

**What Anyscale retained:**
- RayTurbo (proprietary optimized Ray runtime — exclusively on Anyscale Platform)
- Anyscale Platform (managed Ray as a service)
- Agent Skills, observability tooling, and enterprise features
- Primary contributor status to Ray

The strategic logic: by making Ray truly vendor-neutral, Anyscale removes the primary enterprise objection to adoption ("what if Anyscale pivots or closes?"). A larger Ray ecosystem means more potential customers for Anyscale's managed platform. They don't need to own the open-source project to monetize it — they need it to succeed.

## Current Products

### Anyscale Platform

The core product. A fully managed environment for running Ray workloads. Two deployment modes:

**Hosted**: Anyscale manages compute in its own cloud. Limited regions, VM-based, business hours support. Good for teams wanting to get started without infrastructure commitment.

**BYOC (Bring Your Own Cloud)**: Run on your own AWS, GCP, or Azure account, within your own VPC, using your existing GPU reservations. Anyscale provides the orchestration layer, pooling resources across providers. Enterprise SLAs and 24/7 support. This is the serious enterprise offering — it preserves cloud discounts and data residency requirements while adding managed scheduling, observability, and RayTurbo performance.

**Anyscale on Azure** (Private Preview, November 2025): A first-party Azure service available through the Azure Portal with Entra ID authentication. GA expected in 2026. This is a significant distribution play — putting Anyscale in the Azure marketplace where enterprise procurement teams already operate.

### RayTurbo

The performance moat. RayTurbo is Anyscale's proprietary optimized Ray runtime, only available on the Anyscale Platform. Published performance claims compared to open-source Ray:

- Image batch inference: up to **6x cheaper**
- Feature preprocessing: up to **10x faster**
- Llama-3-70B end-to-end scale-up: up to **4.5x faster**
- LLM batch inference cost: up to **6x reduction**
- Video serving: **40% faster** per request
- High-throughput serving: **7x higher** requests per second

These numbers are from Anyscale's own benchmarks, so treat them as directional rather than absolute. But for teams running Ray at scale, even a fraction of these gains is material. This is the proprietary differentiation that makes the managed platform more than a convenience layer.

### LLM Inference

Anyscale supports both online (real-time) and batch inference via Ray Serve and vLLM integration:

- **Online inference**: Ray Serve as the serving framework, vLLM as the inference engine. Anyscale claims proprietary vLLM optimizations yielding up to 20% cost reduction vs. stock vLLM.
- **Batch inference**: `ray.data.llm` for large-scale offline workloads — data enrichment, model evaluation, embedding generation at petabyte scale.
- **Engine flexibility**: Supports vLLM, TensorRT-LLM, TGI, and other inference engines — not locked to any single backend.

Note: Anyscale launched a standalone "Endpoints" serverless LLM API in 2023, competing directly with Together AI and Fireworks. By mid-2024, Endpoints was folded into the broader platform. This was a strategic retreat from the commodity inference API race — Anyscale decided its platform play was more defensible than competing on token prices.

### Fine-Tuning

Fine-tune any open-source model available on HuggingFace: LLaMA, Mistral, BERT, and others. Billed at the compute rate (GPU-hours), not a fixed per-token fee. Historical pricing included a $5/job setup fee plus $4/M training tokens, but current pricing should be verified via documentation.

### Agent Skills (GA, 2025)

One of the more interesting recent launches. Anyscale Agent Skills are specialized integrations for Claude Code and Cursor that give coding agents deep knowledge of Ray and Anyscale. Three categories:

- **Workload Skills**: Generate production-ready code for LLM serving, multimodal processing, training pipelines, and batch inference
- **Platform Skills**: Debug, diagnose, and redeploy live workloads using live logs and metrics
- **Infra Skills**: Deploy Ray on Kubernetes or VMs with production-ready configuration

Anyscale claims 5x development speed for teams using these skills vs. using Claude Code or Cursor without them. This is a smart product: rather than building a generic MCP server, Anyscale built opinionated skills that encode Ray/Anyscale-specific knowledge that general-purpose agents lack.

## Compute Pricing

Usage-based billing, no monthly fixed fees. Committed contract discounts available.

**Hosted compute rates (from anyscale.com/pricing, May 2026):**

| Hardware | Hourly Rate |
|----------|------------|
| CPU only | $0.0135 |
| NVIDIA T4 | $0.5682 |
| NVIDIA L4 | $0.9542 |
| NVIDIA A10G | $1.3635 |
| NVIDIA A100 | $4.9591 |
| NVIDIA H100 | $9.2880 |
| NVIDIA H200 | $10.6812 |

New users receive $100 in Anyscale Credits to get started.

BYOC billing adds a platform management fee on top of your own cloud costs — specifics require contacting Anyscale's sales team.

## Who Uses Anyscale

Named enterprise customers on Anyscale's homepage:
- **Coinbase** — financial services at crypto scale
- **Character.ai** — consumer AI at hundreds of millions of users
- **Physical Intelligence (PI)** — robotics foundation model training
- **Runway ML** — video generation model training and serving

The pattern is clear: these are teams with serious distributed AI workloads. Character.ai runs inference for a consumer product at scale. PI trains robotics models that require massive compute coordination. Runway trains video diffusion models. These are not "I want to call an LLM API" use cases — they are "I am building or operating a serious AI system" use cases.

Ray's raw adoption numbers (500M downloads, 41K GitHub stars) paint a broader picture. The open-source framework serves a wide range of Python distributed computing users, from ML engineers to data platform teams. Anyscale's managed platform targets the subset that wants to avoid operating Ray infrastructure themselves.

## Competitive Position

**vs. AWS SageMaker**: SageMaker holds roughly 34% of the ML platform market and benefits from deep AWS integration. Anyscale is multi-cloud native, supports BYOC across all major providers, and has a more Python-native API. Teams not committed to AWS tend to prefer Anyscale's flexibility. Teams deeply embedded in AWS often stay in SageMaker.

**vs. Modal**: Modal is serverless-first — pay per function call, GPU cold starts. Better for event-driven inference and short-lived tasks. Anyscale is cluster-oriented — better for long-running distributed training and persistent serving. These products serve different workload patterns, and serious teams often use both.

**vs. Google Vertex AI**: Vertex AI is GCP-only with strong BigQuery/GCS integration. Anyscale is framework-agnostic and multi-cloud. For teams on GCP, Vertex AI is often the default choice by gravity rather than by deliberate comparison.

**Unique position**: No other company combines (a) the team that built and most deeply understands Ray, (b) a proprietary performance layer (RayTurbo) unavailable to open-source users, and (c) multi-cloud BYOC support. For teams already running Ray at scale, Anyscale's managed platform is a natural upgrade path with low switching cost.

## Security and Compliance

BYOC deployment means customer data stays within the customer's own cloud account and VPC — a strong compliance story for regulated industries. Anyscale has not published comprehensive compliance certifications (SOC 2, ISO 27001) on its public documentation, though enterprise contracts likely include appropriate security terms.

The November 2025 reports of a self-replicating botnet targeting open-source Ray clusters (reported by The Register) highlight a real risk for teams running Ray directly. Anyscale's managed platform with enterprise access controls mitigates this attack surface.

## What Anyscale Is Not

Anyscale is not the right tool if you want:

- **A simple managed inference API** — if you want to call an LLM with a token-priced API, use Together AI, Fireworks AI, Groq, or DeepInfra instead. Anyscale's inference is infrastructure for serving models, not a hosted model API.
- **A general-purpose serverless compute platform** — Modal and similar platforms are easier for teams without distributed computing background.
- **Transparent public pricing for enterprise features** — BYOC and committed contracts require engaging sales.

The required prior knowledge is real: Anyscale amplifies teams with Ray expertise. Without it, the learning curve is steep.

## Verdict

Anyscale is a technically credible, strategically sophisticated company that built the most important distributed computing framework in AI, donated it to the PyTorch Foundation in a move that should expand its long-term market, and now sells a managed platform layer that delivers meaningful performance gains over running the framework yourself.

The PyTorch Foundation transfer — echoing the Databricks/Spark playbook from Ion Stoica's prior company — is the right long-term move. The Microsoft Azure first-party integration entering GA in 2026 is a serious enterprise distribution channel. The Agent Skills product shows Anyscale is thinking ahead about the AI-native developer workflow.

The weaknesses are real: no public revenue metrics, no new funding round in three-plus years, a complex pricing model, and a product that requires substantial distributed computing experience to extract value from. The addressable market is narrower than the "everyone building AI" framing suggests — Anyscale is for teams running serious distributed workloads, not developers making their first API call.

For that buyer — the platform engineering team at a foundation model lab, a consumer AI company at scale, or an enterprise with genuine distributed training needs — Anyscale is among the strongest choices available.

**Rating: 4/5**

*Strongest for: Teams with existing Ray experience, multi-cloud GPU infrastructure, or distributed AI workloads at scale. Built by the people who understand Ray better than anyone.*

*Not for: Teams wanting a simple managed inference API, developers new to distributed computing, or projects where per-token pricing is the primary concern.*

---

*ChatForest researches AI infrastructure providers using publicly available information. We do not have hands-on access to Anyscale's platform and this review is based on documentation, public benchmarks, press releases, and third-party analysis.*


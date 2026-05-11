# Hyperbolic AI Review: The Math Olympian's Decentralized Inference Network

> Hyperbolic AI aggregates underutilized GPUs into a decentralized inference network, earns Andrej Karpathy's endorsement as his 'favorite' base model platform, and backs it with novel cryptographic verification from UC Berkeley researchers. We review the platform, its tradeoffs, and who it's actually built for.


The founding insight behind Hyperbolic AI comes from a math PhD thesis about three-dimensional topology.

Jasper Zhang's UC Berkeley dissertation studied hyperbolic manifolds — curved geometric spaces that expand exponentially. When Zhang finished his doctorate (in two years, a pace the company says is a Berkeley record) and started thinking about AI infrastructure, he saw a similar pattern: exponential expansion of AI compute demand, and exponential waste of idle compute capacity. The mathematical concept he'd spent years studying became a company metaphor, and eventually, its name.

That company, Hyperbolic, launched its public platform in 2024 with a simple premise: **"We already have enough GPUs. We just need to share them better."** Data centers sit partially idle at night. GPU clusters reserved for training jobs go unused during off-peak hours. Consumer machines with RTX 4090s wait dormant. Hyperbolic's thesis is that aggregating this underutilized capacity — rather than building new data centers — is the correct answer to AI infrastructure's scaling problem.

Whether that thesis proves out at scale is still an open question. But along the way, Hyperbolic has built something that Andrej Karpathy — the former Tesla AI Director and OpenAI co-founder — called his favorite place to interact with base language models. That's not a claim most inference startups can make.

---

## Company Background

Hyperbolic was incorporated in 2022 and launched publicly in 2024. It is headquartered in San Francisco.

**Jasper Zhang** (CEO and Co-founder) is the son of a Chinese mathematics tradition that breeds world-class competitors. He won gold medals at both the Chinese Mathematical Olympiad and the Russian Mathematical Olympiad in high school, then won first place in the Chinese Mathematics Competition for College Students. At UC Berkeley, he won back-to-back gold medals at the Alibaba Global Mathematics Competition — and reportedly celebrated one win with a rap performance.

His PhD thesis, "Guts, Dehn Fillings and Volumes of Hyperbolic Manifolds," was completed in two years rather than the standard five. Before starting Hyperbolic, Zhang worked as a quantitative researcher at Citadel Securities and as a senior blockchain researcher at Ava Labs (the team behind the Avalanche blockchain).

**Yuchen Jin** (CTO and Co-founder) brings the infrastructure counterpart to Zhang's mathematical background. Jin holds a PhD in Computer Science from the University of Washington, where he was advised by Arvind Krishnamurthy, an ACM Fellow and USENIX Vice President. His research centered on ML systems, networking, and distributed infrastructure. Before co-founding Hyperbolic, Jin worked at OctoAI, where he led the Relax project within Apache TVM — one of the leading open-source AI compilers.

The founding story involves a specific frustration Jin encountered: reading an article about running Llama 2 models on consumer AMD GPUs and realizing the infrastructure to democratize this kind of access simply didn't exist. The compute was already there. The coordination layer wasn't.

### Funding

Hyperbolic has raised $20 million across three rounds:

- **Pre-seed**: $725K (November 2022). Early backers included Chapter One, Samsung Next, and Modular Capital.
- **Seed**: $7 million (July 2024). Led by Polychain Capital and Lightspeed Faction, with angels including Balaji Srinivasan, Illia Polosukhin (NEAR Protocol), and Sandeep Nailwal (Polygon co-founder).
- **Series A**: $12 million (December 2024). Led by Variant Fund and Polychain Capital, with participation from Chapter One, Lightspeed Faction, Bankless Ventures, Alumni Ventures, and others.

One thing stands out in that investor list: it is heavily weighted toward Web3 and blockchain-native funds. Polychain Capital (crypto fund), Variant Fund (crypto/Web3 focus), Bankless Ventures (crypto media and investing), Wintermute Ventures (crypto market maker), and Balaji Srinivasan (former a16z partner, prominent crypto advocate) are not the typical backers of an AI infrastructure startup.

This isn't incidental. Hyperbolic has explicitly announced plans to launch its own blockchain and native governance token, intended to allow collective, decentralized ownership of the AI infrastructure network. As of May 2026, that token has not launched publicly. The delay raises questions about whether the blockchain ambition is commercially necessary or primarily driven by investor interest from crypto-native backers. Developers who just want cheap, fast inference may not care about on-chain governance.

That said, Hyperbolic has also attracted real AI credibility: Reynold Xin, co-founder of Databricks (which spun out of UC Berkeley's AMPLab), joined as an advisor. Raluca Ada Popa, a UC Berkeley associate professor and co-director of RISELab and SkyLab, joined to advance the company's confidential computing work. Popa is a serious researcher in security and cryptography — her involvement suggests the technical ambitions extend beyond marketing.

**Employee count:** Approximately 38 as of early 2026.

---

## The Technical Architecture: Hyper-dOS and Proof of Sampling

Hyperbolic's core architectural claim is its **decentralized operating system (Hyper-dOS)**, a hierarchical cluster management system that treats the global network of contributed GPUs as a unified compute resource. The system uses a solar-system-inspired naming convention: Sun Cluster (central governance), Mercury Cluster (single node), Mars Cluster (multi-node), Jupiter Cluster (multi-satellite). It supports auto-scaling, self-healing configurations, and what Hyperbolic calls "customizable cluster compositions."

The harder technical problem with decentralized compute is **verification**: how do you know that a GPU node in an unknown data center somewhere is actually running your model correctly and returning honest outputs? Traditional verification approaches — zero-knowledge machine learning (zkML) or optimistic machine learning (opML) — work but add substantial computational overhead, reportedly up to 300% cost increase for zkML.

Hyperbolic's answer is **Proof of Sampling (PoSP)**, a verification protocol co-developed with researchers at UC Berkeley and Columbia University. Rather than verifying every output, PoSP verifies a statistical sample at a rate calibrated to the node's reputation and stake. The underlying mechanism is game-theoretic: nodes that produce incorrect outputs face economic penalties sufficient to make honesty the rational choice, even knowing that not every output will be checked. The result is verification overhead of less than 1% — a dramatic improvement over zkML.

PoSP has attracted attention beyond Hyperbolic's own platform. EigenLayer (one of the major Ethereum restaking protocols) adopted PoSP for its Actively Validated Service (AVS) verification. Karak Network has also integrated it. Whether PoSP's full production implementation on Hyperbolic's mainnet is complete — versus a validated design — has been a point of external scrutiny. The Stanford Blockchain Review noted in 2024 that full mainnet deployment remained described as future work.

**BF16 precision**: Hyperbolic runs models at BF16 (Brain Float 16) full precision by default, rather than FP8 quantization. FP8 reduces compute cost but introduces some output quality degradation. Hyperbolic's deliberate choice to prioritize output quality over maximum throughput is meaningful for developers building research tools, base model evaluation, or quality-sensitive applications. It's the right call for certain use cases — and it's exactly why Karpathy favors Hyperbolic for base model access. Base models evaluated at reduced precision produce subtly different behavior than their full-precision equivalents, which matters when you're studying model capabilities rather than just building products.

---

## Infrastructure and GPU Products

Unlike DeepInfra or Fireworks, which own and operate their own data centers, Hyperbolic does not build centralized infrastructure. Its capacity comes from three sources:

1. **Spot marketplace**: Idle GPUs contributed by data centers, mining operations, and individual suppliers. Prices adjust weekly based on availability and demand.
2. **On-Demand GPUs**: Production-grade instances with instant provisioning, launched in 2025. H100 SXM priced at $1.49/hour — competitive with major cloud providers. Targeted at growing AI companies.
3. **Reserved Clusters**: Long-term, dedicated cluster commitments at discounted rates for enterprise customers.

**Available GPU hardware**: H100 SXM, A100, RTX 4090, and others through the marketplace.

**Pricing context**: H100 SXM spot pricing across GPU cloud providers in 2025 ranged from roughly $1.49/hour (Hyperbolic on-demand) to $6.98/hour on the high end. Hyperbolic's decentralized model allows it to undercut centralized providers on price — the tradeoff is variability in availability and reliability.

**Scale as of April 2025**: 6,500+ GPU rentals per month, 127,000+ GPU hours consumed. That's meaningful throughput but still well below leaders like Lambda Labs or CoreWeave.

**The reliability caveat**: Because GPU supply comes from heterogeneous, third-party sources, quality assurance varies across nodes. Third-party analysis from April 2026 explicitly recommends Hyperbolic for prototyping and research but cautions against using it for production workloads where reliability guarantees are required. This is the fundamental tension in the decentralized compute model — lower cost and more supply, but less uniform quality than owning the hardware yourself.

---

## Inference API

The serverless inference API is where most developers first encounter Hyperbolic. It offers a standard OpenAI-compatible REST interface — same base URL structure, same message format, easy drop-in for applications already using the OpenAI SDK.

### Models Available

As of May 2026, Hyperbolic's active inference model catalog includes:

| Model | Context Window | Input Price | Output Price |
|-------|---------------|-------------|--------------|
| DeepSeek R1 0528 | 164K tokens | $3.00/M | $3.00/M |
| DeepSeek R1 (January) | 164K tokens | $2.00/M | $2.00/M |
| DeepSeek V3 0324 | 164K tokens | $1.25/M | $1.25/M |
| Qwen3 Coder 480B (FP8) | 262K tokens | $2.00/M | $2.00/M |
| Llama 3.3 70B | 131K tokens | $0.40/M | $0.40/M |

*Pricing sourced from Artificial Analysis, May 2026.*

The catalog is notably smaller than competitors. DeepInfra supports 150+ models; Together AI and Fireworks each offer 100+. Hyperbolic's current active list is closer to 5 models on the serverless service. The company has explicitly posted "Inference Model Sunset" notices as it consolidates its catalog. This is an important limitation for developers who need access to a wide range of models — Hyperbolic isn't the right choice for that use case.

### Speed Benchmarks

| Model | Throughput | Time to First Token |
|-------|-----------|---------------------|
| DeepSeek R1 0528 | 111 tokens/sec | ~0.87s |
| DeepSeek R1 (January) | 95 tokens/sec | ~1.00s |
| Llama 3.3 70B | 80 tokens/sec | ~0.87s |

*Benchmarks from Artificial Analysis.*

Speed performance is competitive without being class-leading. Groq (LPU-based) and Cerebras (wafer-scale chip) both deliver faster throughput for comparable models. DeepInfra, at 97 tokens/sec for DeepSeek V3.2, runs at similar speeds for about the same price. Hyperbolic's real differentiation on inference is the BF16 precision and the early availability of new models — they were among the first to deploy DeepSeek R1 at full BF16 precision after its January 2025 release, which drove a 150% surge in Hyperbolic's inference usage.

### Integrations

Hyperbolic is an **official serverless inference provider on Hugging Face** (added in huggingface_hub v0.29.0). This is a meaningful distribution channel — developers using Hugging Face's transformers library can access Hyperbolic models with a single line of configuration. The platform is also integrated into LiteLLM and the Vercel AI SDK.

---

## Image Generation

Beyond language models, Hyperbolic offers an image generation API supporting Stable Diffusion models and FLUX.1 [dev] (via an official partnership with Black Forest Labs, the team behind the FLUX model family). The endpoint follows OpenAI's image generation API format.

Stable Diffusion generation is priced at approximately $0.01 per image, which is competitive for rapid prototyping and batch generation workloads.

---

## MCP Server

Hyperbolic launched an official MCP server in May 2025 — **`HyperbolicLabs/hyperbolic-mcp`** on GitHub.

This is noteworthy: rather than simply exposing inference endpoints, the MCP server enables AI agents to **manage GPU infrastructure** via natural language. The server exposes tools for:

- Listing available GPU types and current pricing
- Renting GPU instances (launching compute nodes)
- Monitoring active instances
- Terminating instances
- Establishing SSH connections to rented GPUs
- Executing remote commands over SSH

The practical implication: an AI agent working inside Claude Desktop or Cursor can autonomously provision a GPU cluster, launch a training job, check its status, and terminate the instance when complete — all without the user manually navigating a cloud dashboard.

Hyperbolic called it "the first platform that lets LLMs control GPU compute using natural language." Whether the claim is entirely accurate depends on how narrowly you define the category, but the capability itself is real and useful for AI-native workflows.

**Caveats**: The MCP server requires users to have an active Hyperbolic account with a balance. It also requires **unencrypted SSH private keys** — the repository documentation explicitly acknowledges this constraint, which is a security concern for enterprise deployments. This is the kind of design decision that's acceptable in a prototyping context but would need to be resolved before production enterprise adoption.

The MCP server targets Claude Desktop, Cursor, and similar AI-native development environments. Given the GPU management focus — rather than inference — it's particularly useful for teams running distributed training, hyperparameter sweeps, or batch inference jobs they want to orchestrate from within an AI assistant.

---

## Academic Partnerships and Endorsements

Hyperbolic's connections to research institutions are unusually deep for a startup at this funding level.

**UC Berkeley ties**: CEO Jasper Zhang completed his PhD there. Proof of Sampling was co-developed with UC Berkeley and Columbia University researchers. Raluca Ada Popa (UC Berkeley associate professor, RISELab/SkyLab co-director) joined the advisory board. Reynold Xin (Databricks co-founder, UC Berkeley AMPLab/RISELab veteran) joined as an advisor. The company has worked with LMSYS (the UC Berkeley-adjacent group behind Chatbot Arena and the SGLang inference framework) on DeepSeek inference optimization.

**University compute customers**: UC Berkeley, Stanford, Cornell, and NYU are listed as platform users — meaning Hyperbolic provides research compute to the same institutions that produced its founders and advisors.

**The Karpathy endorsement**: In a statement that circulates widely in developer communities, Andrej Karpathy named Hyperbolic his "favorite place" to interact with base language models. Karpathy is one of the most trusted voices in AI infrastructure — he built Tesla's Autopilot neural network stack, co-founded OpenAI, and now runs Eureka Labs. His endorsement specifically highlights Hyperbolic's base model access, which is directly tied to the BF16 precision commitment. For researchers doing model evaluation, interpretability work, or building on top of base models rather than instruction-tuned variants, that matters.

Other notable customers: **Hugging Face** (official inference provider), **Quora/Poe** (Llama and Hermes models), **Vercel** (AI SDK integration), and **Coinbase** (Hyperbolic was a launch partner for Coinbase's x402 protocol, which enables USDC-based per-API-call payments for AI services).

---

## Traction

Hyperbolic has published monthly recaps with specific metrics:

- **End of 2024**: 98,000 total users, 25,000+ inference users
- **January 2025**: ~57,000 monthly active users
- **February 2025**: 100,000+ total developers; 57,000 new users in that month alone (78% MoM growth); 32B tokens processed; 22,000 inference users
- **April 2025**: 195,000+ developers; 112B+ tokens processed (320% growth from March); 6,500+ GPU rentals; 127,000+ GPU hours

The 320% month-over-month token growth in March→April 2025 is striking. Much of that was driven by the DeepSeek R1 wave — Hyperbolic's position as an early BF16 R1 provider captured significant overflow demand from developers who couldn't get access through other providers during the R1 launch surge.

**Revenue is not disclosed.** With 38 employees and $20M raised, Hyperbolic is lean. The unit economics of the decentralized model — where Hyperbolic doesn't own the hardware and takes a margin — theoretically improve with scale, but the path to profitability is not publicly documented.

---

## Limitations and Who Should Not Use Hyperbolic

**Variable pricing**: GPU marketplace rates refresh weekly. This makes it difficult to budget for long-running training jobs that span multiple pricing periods. Providers that own their own hardware (Lambda Labs, CoreWeave) can offer stable pricing commitments that Hyperbolic cannot match.

**Limited inference model catalog**: Five active models as of May 2026 is thin. If you need access to a wide range of models — niche models, new releases, specialized variants — Hyperbolic's serverless inference API isn't the right choice. DeepInfra (150+ models), Together AI, or Fireworks offer far more breadth.

**Production reliability concerns**: The decentralized model introduces variability that centralized infrastructure avoids. Third-party benchmarks have identified reliability concerns sufficient to recommend Hyperbolic only for prototyping rather than production workloads. The company's on-demand H100 product addresses this somewhat — those are production-grade instances with claimed reliability — but the track record is still shorter than established cloud providers.

**Crypto/blockchain positioning**: The blockchain and token plans, and the crypto-heavy investor base, may be irrelevant or off-putting to developers who just want cheap, reliable GPU access. The technology underneath (PoSP, decentralized coordination) is legitimate — but the investor and community signals may confuse positioning. Hyperbolic has to attract mainstream AI developers while also serving a Web3 audience with different interests and expectations.

**Small team for large ambitions**: Thirty-eight employees building a global GPU operating system, inference API, image generation, fine-tuning services, an MCP server, a blockchain, and a token is an enormous scope for a lean organization.

**PoSP deployment status**: As of late 2024, PoSP's full production deployment on the mainnet was described by external reviewers as future work rather than fully live. If decentralized verification is central to why you'd choose Hyperbolic over a centralized alternative, it's worth understanding the current deployment status before making architectural decisions.

---

## Verdict

Hyperbolic is a platform with genuine technical credibility, unusual academic provenance, and a differentiated thesis about AI infrastructure. The Karpathy endorsement isn't marketing fluff — it reflects something real about Hyperbolic's commitment to BF16 precision and base model access that other inference providers have deprioritized in favor of throughput and breadth.

The GPU marketplace offers meaningful cost savings for research and prototyping workloads, and the H100 on-demand product at $1.49/hour is competitive for small-to-medium training jobs. The official MCP server — enabling AI agents to manage GPU compute via natural language — is ahead of what most inference providers have shipped.

Where Hyperbolic falls short: the inference model catalog is thin, production reliability remains a concern, pricing variability makes it hard to budget for long jobs, and the blockchain/token ambitions add complexity that most AI developers neither need nor want. The $20M total raise is modest for a company trying to build global decentralized infrastructure; compare it to DeepInfra's $133M+, Together AI's $100M+, or Fireworks AI's $52M+.

**Best fit**: AI researchers doing base model evaluation, developers who need BF16 precision for quality-sensitive applications, students and academics who want affordable GPU access (Hyperbolic offers $15 free credits for .edu emails), and teams building AI agent workflows that need programmatic GPU management via MCP.

**Not the best fit**: Production API deployments requiring high model breadth, teams with strict budget predictability requirements, or enterprise customers who need audited compliance and SLA guarantees.

**Rating: 4/5** — Strong technical foundations, notable endorsements, and a genuinely differentiated position in the market. Execution is still catching up to the vision, and the model catalog and reliability gaps are real. Worth watching closely.

---

*ChatForest reviews AI infrastructure products based on public information, technical documentation, and independent benchmarks. We research these platforms — we do not have commercial relationships with the companies we cover. Hyperbolic AI's website is [hyperbolic.ai](https://hyperbolic.ai).*


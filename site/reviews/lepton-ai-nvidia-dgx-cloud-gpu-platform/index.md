# Lepton AI → NVIDIA DGX Cloud Lepton: The Startup NVIDIA Acquired to Build Its Developer Platform

> Lepton AI (lepton.ai) was a Python-native GPU cloud startup founded by the creator of Caffe. NVIDIA acquired it in April 2025. It now operates as NVIDIA DGX Cloud Lepton — a multi-cloud GPU marketplace aggregating CoreWeave, Lambda, AWS, and 25+ providers under one API.


**At a glance:** Lepton AI ([lepton.ai](https://www.nvidia.com/en-us/data-center/dgx-cloud-lepton/)) no longer exists as an independent company. In April 2025, NVIDIA acquired the San Francisco–based startup for "several hundred million dollars" — one of the largest acqui-hires in AI infrastructure history on a per-employee basis. The platform, launched in 2023 by **Yangqing Jia** (creator of the Caffe deep learning framework) and **Junjie Bai** (former AI Platform Director at Alibaba Cloud), has been rebranded as **NVIDIA DGX Cloud Lepton**: a unified developer platform that aggregates GPU compute from more than 25 cloud providers, runs NVIDIA NIM microservices, and gives teams access to tens of thousands of GPUs — H100s, H200s, B200s — without committing to a single cloud. **Rating: 4/5.**

Lepton AI is part of our **[GPU Cloud category](/categories/gpu-cloud/)**.

---

## The Founding Story: Caffe's Creator Builds Developer Infrastructure

Lepton AI's founding story starts with a framework most AI engineers have heard of but rarely think about anymore: Caffe.

**Yangqing Jia** created Caffe during his PhD at UC Berkeley under Trevor Darrell. Released in December 2013, Caffe was the first deep learning framework to gain serious production adoption — it preceded PyTorch and TensorFlow in practical use, ran fast on GPUs, and became the framework behind a generation of computer vision research and industry deployments. Jia later contributed to ONNX and helped ship PyTorch 1.0 during his time at Facebook (Meta). He then became VP of Technology at Alibaba's DAMO Academy before leaving in March 2023 to co-found Lepton.

**Junjie Bai** served as AI Platform Director at Alibaba Cloud, building large-scale ML infrastructure. He has additional background from Meta's AI research environment and studied at the Technical University of Munich. After NVIDIA's acquisition, he became Senior Director of Physical AI at NVIDIA.

The founding premise was direct: AI infrastructure was still too hard. Every team building an LLM product had to learn Docker, Kubernetes, cloud networking, GPU drivers, and cluster management on top of the actual ML work. Jia and Bai had both spent years managing GPU infrastructure at hyperscaler scale; they knew the pain firsthand. Their answer was to abstract it away in Python — the language AI engineers already wrote.

Lepton AI was incorporated in early 2023 and raised an **$11 million seed round** led by CRV and Fusion Fund. A Series A followed later in 2023, estimated at $22–35 million (sources vary; YC and Andreessen Horowitz are mentioned in early coverage, though the lead investor was not publicly confirmed). Total VC raised before acquisition was likely in the $33–46 million range.

---

## The Product: LeptonAI Framework and the Photon Abstraction

Lepton AI's developer experience centered on a single abstraction: the **Photon**.

A Photon is a Python class that defines an AI service. Developers inherit from `Photon`, annotate handlers with `@Photon.handler`, and describe their compute requirements. Lepton handles everything else — containerization, GPU allocation, load balancing, scaling, and HTTP serving.

A minimal example deploying a language model:

```python
from leptonai.photon import Photon

class LLMService(Photon):
    requirement_dependency = ["vllm"]

    def init(self):
        from vllm import LLM
        self.llm = LLM(model="meta-llama/Llama-3.1-8B-Instruct")

    @Photon.handler
    def generate(self, prompt: str) -> str:
        return self.llm.generate(prompt)[0].outputs[0].text
```

Running `lep photon push` deploys this to Lepton's cloud on whatever GPU type the model requires. The `lep` CLI manages workspaces, secrets, and deployment lifecycle. The open-source **leptonai** Python package (Apache 2.0, 2,800+ GitHub stars, still maintained as of May 2026 at v0.27.2) handles local development and testing; the same abstraction works in both environments.

**The LeptonAI platform provided three main compute primitives:**

- **Inference Endpoints** — persistent serving endpoints for models, autoscaling with demand
- **Batch Jobs** — one-off tasks that run to completion and terminate
- **Dev Pods** — interactive GPU-attached development environments for exploration and prototyping

**LLM Inference API (pre-acquisition):** Lepton operated an OpenAI-compatible hosted inference API for open-source models — Llama 2 and 3 variants, Mistral, Mixtral, Qwen, Yi, Falcon, Starcoder, and others. The pricing was highly competitive: $0.07–$4 per million tokens depending on model. A drop-in replacement for the OpenAI SDK when targeting open weights. This inference layer was powered by Lepton's proprietary **Tuna engine**, which the team claimed delivered 4.5× faster deployment and 2× throughput versus a standard KServe baseline on equivalent hardware — 1,450 tokens/second on Mixtral-8x7B on A100 vs. 720 for KServe.

---

## The Viral Moment: search_with_lepton

In January 2024, Lepton's profile exploded when **search_with_lepton** — a conversational search engine built in under 500 lines of TypeScript and Python — topped GitHub's trending list. The project combined Lepton's LLM inference API with Bing/Google search results to produce a real-time AI-powered search interface.

It was a deliberately minimal demonstration: just enough code to be useful, small enough for any developer to read in an afternoon. The project gained 2,000+ stars in its first week. It positioned Lepton as a developer-first company at a moment when every AI team was thinking about building search products — and it drove a significant wave of signups to the platform.

The repository is now archived on GitHub (reflecting the acquisition), but it remains one of the cleaner examples of what a Lepton-powered product looked like.

---

## gpud: The Open-Source GPU Health Monitor

One of Lepton's most enduring technical contributions is **gpud** (GPU Daemon) — an open-source, Go-based GPU monitoring and diagnostics agent. Lepton published gpud based on hard-won operational experience running GPU clusters at Meta, Alibaba Cloud, and Uber-scale environments.

gpud monitors:

- GPU power states and temperature
- NVML Xid error events (GPU hardware faults)
- Kernel log messages related to GPU failures
- Memory errors and driver health

The team claimed gpud reduced GPU cluster unavailability by approximately 4× by catching hardware degradation early before it cascades into full node failures. After the NVIDIA acquisition, gpud was carried into NVIDIA's own DGX Cloud Lepton infrastructure — one of the clearest signals that NVIDIA was acquiring engineering capability, not just a customer list.

gpud remains open source (Apache 2.0) at its original GitHub repository, with 478 stars and active maintenance as of mid-2026.

---

## The NVIDIA Acquisition: April 2025

In April 2025, NVIDIA completed its acquisition of Lepton AI for **"several hundred million dollars"** — the exact figure was not publicly disclosed, though analysts placed estimates in the $300–500M range. The deal closed April 8, 2025, with reports surfacing roughly two weeks earlier.

For context: Lepton AI had approximately 20 employees at the time of acquisition. That implies a per-employee acquisition price of roughly $15–25M — a striking outcome for a two-year-old startup.

**Why NVIDIA wanted Lepton:**

NVIDIA is the dominant GPU hardware vendor, but it had historically been a component supplier rather than a cloud software provider. Its own DGX Cloud offering (running on Oracle, Microsoft Azure, Google Cloud, and CSPs) provided cloud access to DGX SuperPODs, but lacked a developer-facing abstraction layer. Lepton provided:

1. A Python-first developer experience (Photon, the `lep` CLI, the leptonai open-source framework)
2. A working LLM inference serving layer (the Tuna engine and OpenAI-compatible API)
3. A multi-cloud marketplace model that aggregated GPU supply from NVIDIA's CSP partners
4. The gpud cluster monitoring toolset, immediately deployable across NVIDIA's partner infrastructure
5. A founding team with deep ML infrastructure credibility — hard to hire at this level, impossible to manufacture

The strategic logic was also careful: a marketplace model where Lepton aggregated CoreWeave, Lambda, AWS, and others meant NVIDIA wasn't competing with its own cloud customers — it was sitting above them, providing the developer experience layer while hardware revenues continued to flow to its ecosystem.

Jensen Huang described the move in infrastructure terms: "Together with our NCPs, we're building a planetary-scale AI factory."

---

## NVIDIA DGX Cloud Lepton: What It Is Today

Since the May 2025 rebranding, **NVIDIA DGX Cloud Lepton** operates as NVIDIA's unified developer platform for multi-cloud GPU access. The platform is no longer positioned as a serverless compute abstraction in the Modal sense — it's closer to a compute broker and developer portal built on top of NVIDIA's partner ecosystem.

**Core features of DGX Cloud Lepton (as of mid-2026):**

- **25+ cloud provider partners** including CoreWeave, Lambda, AWS, Foxconn, Crusoe Energy, Firmus, Fluidstack, Andromeda, Nebius AI, Scaleway, GMI Cloud, Nscale, Hydra Host, SoftBank Corp., Yotta Data Services, Together AI, Mistral AI, Hugging Face, MLFoundry, and San Francisco Compute Company
- **GPU access across Hopper and Blackwell architectures** — H100, H200, B200, and future generations
- **NVIDIA NIM microservices** — prebuilt, optimized AI inference containers for foundation models (Llama, Mistral, Stable Diffusion, etc.) deployable with one command
- **Unified developer API** — single endpoint regardless of which underlying cloud partner is serving the request; applications are decoupled from specific compute providers
- **Data sovereignty controls** — specify which geographic regions or specific partner providers can handle workloads
- **Same developer workflow** across development, training, and inference use cases
- **Enterprise readiness** — the platform inherits NVIDIA's enterprise support agreements, security certifications, and procurement pathways

The platform does not publish public pricing directly. Rates depend on the underlying compute partner and are negotiated or surfaced at the point of provisioning through partner consoles. This is a meaningful shift from the pre-acquisition Lepton, which had explicit per-hour and per-token pricing published on its website.

---

## The Open-Source Legacy

The leptonai Python framework continues to be maintained on GitHub (v0.27.2 as of May 2026, 2,800+ stars, Apache 2.0). The Photon abstraction still works for local development and, in theory, deployment to DGX Cloud Lepton — though NVIDIA's public documentation emphasizes NIM microservices over the Photon pattern for new deployments.

gpud is also still active (478 stars, active Go development). It is genuinely useful for any team running GPU clusters who wants open-source visibility into hardware health — completely independent of whether you're using NVIDIA's cloud platform.

The **search_with_lepton** repository is archived but readable. It remains a well-crafted minimal example of a full-stack AI application for developers studying how to build search products.

---

## Competitive Context

**vs. Modal:** Modal remains an independent company (~$103M raised through Series B, Lux Capital October 2025) still building its Python-native serverless GPU platform. Modal has deepened its sandbox capabilities and secured the OpenAI Agents SDK partnership. As an independent developer-focused product, Modal is now the more direct heir to what Lepton AI was trying to be. DGX Cloud Lepton and Modal now serve different buyer profiles: Modal targets developers who want a serverless abstraction; DGX Cloud Lepton targets teams who want multi-cloud GPU access with NVIDIA's enterprise endorsement and NIM optimizations.

**vs. CoreWeave:** CoreWeave is DGX Cloud Lepton's biggest partner, not a competitor. CoreWeave's own infrastructure sits behind the Lepton marketplace. Teams choosing raw CoreWeave get more direct control; teams choosing DGX Cloud Lepton get a multi-provider abstraction.

**vs. Lambda:** Same relationship as CoreWeave — Lambda is a Lepton marketplace partner. The NVIDIA acquisition resolved what might have been a competitive tension between Lepton and larger GPU clouds by making them collaborators.

**vs. Baseten:** Baseten remains independent and focused on ML model serving with deeper MLOps tooling. Both now target the enterprise inference market, but Baseten has stronger tooling for custom model deployment workflows; DGX Cloud Lepton emphasizes NIM-standardized model serving.

---

## Strengths

- **NVIDIA's full institutional weight behind a developer platform** — access to upcoming GPU architectures (Vera Rubin, etc.) as a first-class platform launch partner
- **25+ compute partners** create genuine supply redundancy and geographic diversity
- **NIM microservices** deliver NVIDIA-optimized inference containers that are significantly harder for independent providers to replicate
- **gpud** and the leptonai framework remain genuinely useful open-source tools
- **Founding team's depth** — the Caffe lineage and Alibaba hyperscaler experience gave Lepton credibility that is now embedded in NVIDIA's platform engineering

## Weaknesses

- **No public pricing** — the shift to partner-dependent, non-published pricing adds friction for developers who want to evaluate cost before committing
- **Acquisition dependency** — the platform's developer-friendliness is now subject to NVIDIA's enterprise roadmap priorities, not an independent team's developer advocacy
- **Brand dissolution** — the Lepton identity is gone; developers searching for lepton.ai now land on an nvidia.com subdirectory page, which carries a different psychological weight
- **Marketplace model = no owned compute** — DGX Cloud Lepton does not operate any GPUs itself; reliability depends entirely on 25+ partners executing consistently
- **Post-acquisition roadmap opacity** — unlike independent startups that publish changelogs and blog posts about what they're building, NVIDIA's platform evolution is communicated through corporate press releases and developer conference announcements
- **Integration risk** — integrating a 20-person startup's Python framework and LLM API into a $3 trillion hardware company's cloud offering is genuinely complex engineering; the seams may show

---

## Who Should Use NVIDIA DGX Cloud Lepton

**DGX Cloud Lepton is well-suited for:**
- Enterprise ML teams who want to standardize on NVIDIA NIM microservices without locking into a single cloud provider
- Organizations with NVIDIA enterprise agreements that want unified GPU access across partner infrastructure
- Teams building AI applications on top of NVIDIA's partner ecosystem (CoreWeave, Lambda, Nebius, etc.) who want multi-cloud portability
- Developers who want NVIDIA-blessed inference containers for major foundation models with performance optimization baked in

**It may not be the best fit if:**
- You are an independent developer or small team that wants simple, transparent per-second pricing without sales conversations
- You need the developer experience autonomy of an independent platform (Modal, Baseten) whose roadmap reflects developer needs first
- You are evaluating GPU clouds based on public pricing comparison

---

## Verdict

Lepton AI was one of the more technically credible GPU cloud startups of the 2023–2024 cohort — a small team with genuine ML infrastructure depth, a clean developer abstraction, and a viral demonstration of what building on their platform looked like. The NVIDIA acquisition in April 2025 was a strong outcome for the founders and validation of the technical approach.

NVIDIA DGX Cloud Lepton, as the resulting platform, is a meaningful addition to the GPU cloud landscape: the only offering with NVIDIA's direct backing that spans 25+ cloud partners and delivers NIM microservices-optimized inference. For enterprise teams already in the NVIDIA orbit — whether through DGX hardware, NIM commitments, or CSP agreements — the platform offers genuine value.

What's been lost in the transition is the spirit of what Lepton was: a scrappy, developer-first, independent company with transparent pricing and an open-source community. What's been gained is scale, institutional support, and access to Blackwell compute pipelines that no independent startup could match.

**Rating: 4/5.** Strong technical foundation, NVIDIA-scale reach, and the only multi-cloud GPU marketplace with the hardware vendor's own endorsement. Docked one point for pricing opacity, post-acquisition roadmap uncertainty, and the fact that the most developer-accessible version of this product — the independent Lepton AI — no longer exists.

---

*ChatForest reviews AI infrastructure products based on public documentation, pricing pages, technical benchmarks, and industry coverage. We do not have a commercial relationship with NVIDIA, Lepton AI, or any products covered on this site. This review covers the platform as of May 2026.*


---
title: "Lepton AI → NVIDIA DGX Cloud Lepton: The Startup NVIDIA Acquired to Build Its Developer Platform"
date: 2026-05-08T13:00:00+09:00
description: "Lepton AI (lepton.ai) was a Python-native GPU cloud startup founded by the creator of Caffe. NVIDIA acquired it in April 2025. It now operates as NVIDIA DGX Cloud Lepton — a multi-cloud GPU marketplace aggregating CoreWeave, Lambda, AWS, and 18+ verified providers under one API. Both co-founders have since left NVIDIA (2026 update)."
og_description: "Lepton AI was acquired by NVIDIA in April 2025 for 'hundreds of millions.' Now NVIDIA DGX Cloud Lepton. Founded by Caffe creator Yangqing Jia and ex-Alibaba Cloud exec Junjie Bai — both have since left NVIDIA to found Intent Lab (2026). Open-source Photon framework. Viral search_with_lepton demo. gpud GPU monitoring. 18+ verified cloud partners. Rating: 3/5."
content_type: "Review"
card_description: "Lepton AI started in 2023 as a 'Heroku for AI' — a Python-native platform for deploying GPU-backed AI services with minimal infrastructure overhead. Its open-source Photon framework and viral search_with_lepton demo made it a developer darling. In April 2025, NVIDIA acquired the ~20-person team for hundreds of millions of dollars, rebranding the platform as NVIDIA DGX Cloud Lepton in May 2025. It now aggregates compute from 18+ verified cloud partners including CoreWeave, Lambda, AWS, Nebius, and Crusoe under a unified developer API backed by NVIDIA NIM microservices. As of an August 2026 audit, both co-founders have left NVIDIA to found a new startup, Intent Lab."
last_refreshed: 2026-08-25
sources_audited: 2026-08-25
---

**At a glance:** Lepton AI ([lepton.ai](https://www.nvidia.com/en-us/data-center/dgx-cloud-lepton/)) no longer exists as an independent company. In April 2025, NVIDIA acquired the San Francisco–based, ~20-person startup for a reported "several hundred million dollars" ([TechNode](https://technode.com/2025/04/09/nvidia-acquires-chinese-gpu-cloud-startup-lepton-ai-report/); [Yahoo Finance/Fortune](https://finance.yahoo.com/news/nvidia-just-bought-startup-renting-182743870.html); GPU-cloud analyst SemiAnalysis put the rumored range at [$300M–$900M](https://newsletter.semianalysis.com/p/clustermax-20-the-industry-standard)). The platform, launched in 2023 by **Yangqing Jia** (creator of the Caffe deep learning framework) and **Junjie Bai** (former AI Platform Director at Alibaba Cloud), was rebranded as **NVIDIA DGX Cloud Lepton**: a unified developer platform that aggregates GPU compute from 18+ named cloud providers ([NVIDIA, May 2025](https://nvidianews.nvidia.com/news/nvidia-announces-dgx-cloud-lepton-to-connect-developers-to-nvidias-global-compute-ecosystem); [NVIDIA, June 2025](https://nvidianews.nvidia.com/news/nvidia-dgx-cloud-lepton-connects-europes-developers-to-global-nvidia-compute-ecosystem)), runs NVIDIA NIM microservices, and gives teams access to tens of thousands of GPUs — H100s, H200s, B200s — without committing to a single cloud. **Update (as of this August 2026 audit):** both co-founders have since left NVIDIA — Jia departed in mid/late 2026 to found a new startup, Intent Lab, reportedly after a dispute over an open-source pledge NVIDIA did not follow through on; industry press citing semiconductor research firm SemiAnalysis also reported Jensen Huang's dissatisfaction with DGX Cloud Lepton's traction (see "The NVIDIA Acquisition" section below for sourcing and caveats). **Rating: 3/5** (revised down from 4/5 on this audit — see Verdict for why).

Lepton AI is part of our **[GPU Cloud category](/categories/gpu-cloud/)**.

---

## The Founding Story: Caffe's Creator Builds Developer Infrastructure

Lepton AI's founding story starts with a framework most AI engineers have heard of but rarely think about anymore: Caffe.

**Yangqing Jia** created Caffe during his PhD at UC Berkeley under advisor Trevor Darrell ([Caffe paper, arXiv](https://arxiv.org/abs/1408.5093); [caffe.berkeleyvision.org](https://caffe.berkeleyvision.org/)). Released in December 2013, Caffe was one of the first deep learning frameworks to gain serious production adoption — it preceded PyTorch and TensorFlow in practical use, ran fast on GPUs, and became the framework behind a generation of computer vision research and industry deployments. Jia later created Caffe2 and ONNX and was a co-lead of PyTorch 1.0 during his time at Facebook/Meta ([Synced profile](https://syncedreview.com/2019/03/05/caffe-pioneer-ai-infrastructure-director-leaves-facebook/)), then became Head of the System AI Lab / VP of Technology at Alibaba's DAMO Academy before leaving to co-found Lepton in 2023.

**Junjie Bai** served as Director of the AI Platform at Alibaba Group (2020–2023), with earlier experience on Facebook AI's technical team and a background from the Technical University of Munich ([The Org](https://theorg.com/org/nvidia/org-chart/junjie-bai); [Junjie Bai LinkedIn](https://www.linkedin.com/in/junjiebai/)). He held the Senior Director, Physical AI title at NVIDIA after the acquisition — but, like Jia, has since left; see the update below.

The founding premise was direct: AI infrastructure was still too hard. Every team building an LLM product had to learn Docker, Kubernetes, cloud networking, GPU drivers, and cluster management on top of the actual ML work. Jia and Bai had both spent years managing GPU infrastructure at hyperscaler scale; they knew the pain firsthand. Their answer was to abstract it away in Python — the language AI engineers already wrote.

Lepton AI was incorporated in early 2023 and raised an **$11 million seed round** backed by CRV and Fusion Fund ([Yahoo Finance/Fortune](https://finance.yahoo.com/news/nvidia-just-bought-startup-renting-182743870.html)). ChatForest could not independently verify reports of a subsequent Series A round against a reliable primary source, so no further-funding figure is stated here — a previous version of this page cited a $22–35M Series A estimate that could not be re-confirmed and has been removed.

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

Running `lep photon push` deploys this to Lepton's cloud on whatever GPU type the model requires. The `lep` CLI manages workspaces, secrets, and deployment lifecycle. The open-source **leptonai** Python package (Apache 2.0) remains actively maintained under NVIDIA's `leptonai` GitHub org — [2,824 stars and latest release v0.46.0 as of August 25, 2026](https://github.com/leptonai/leptonai); the same abstraction works in both environments.

**The LeptonAI platform provided three main compute primitives:**

- **Inference Endpoints** — persistent serving endpoints for models, autoscaling with demand
- **Batch Jobs** — one-off tasks that run to completion and terminate
- **Dev Pods** — interactive GPU-attached development environments for exploration and prototyping

**LLM Inference API (pre-acquisition):** Lepton operated an OpenAI-compatible hosted inference API for open-source models — Llama 2 and 3 variants, Mistral, Mixtral, Qwen, Yi, Falcon, Starcoder, and others — as a drop-in replacement for the OpenAI SDK when targeting open weights. This inference layer was powered by Lepton's proprietary **Tuna engine**. *Note: an earlier version of this page cited specific Tuna-vs-KServe throughput multipliers and a Mixtral-8x7B tokens/second figure; on this audit we could not locate an independent primary source (a Lepton blog post, benchmark repo, or third-party reproduction) for those numbers — every search result tracing back to them led only to this ChatForest page itself — so they have been removed per our citation policy rather than re-published unverified.*

---

## The Viral Moment: search_with_lepton

In January 2024, Lepton's profile exploded when **search_with_lepton** — a conversational search engine built in under 500 lines of TypeScript and Python — topped GitHub's trending list. The project combined Lepton's LLM inference API with Bing/Google search results to produce a real-time AI-powered search interface.

It was a deliberately minimal demonstration: just enough code to be useful, small enough for any developer to read in an afternoon. The project gained 2,000+ stars in its first week. It positioned Lepton as a developer-first company at a moment when every AI team was thinking about building search products — and it drove a significant wave of signups to the platform.

The [repository is now archived on GitHub](https://github.com/leptonai/search_with_lepton) (8,000+ stars as of this audit) reflecting the acquisition, but it remains one of the cleaner examples of what a Lepton-powered product looked like.

---

## gpud: The Open-Source GPU Health Monitor

One of Lepton's most enduring technical contributions is **gpud** (GPU Daemon) — an open-source, Go-based GPU monitoring and diagnostics agent. Lepton published gpud based on hard-won operational experience running GPU clusters at Meta, Alibaba Cloud, and Uber-scale environments.

gpud monitors:

- GPU power states and temperature
- NVML Xid error events (GPU hardware faults)
- Kernel log messages related to GPU failures
- Memory errors and driver health

The goal is catching hardware degradation early before it cascades into full node failures. *Note: an earlier version of this page cited a specific "~4x reduction in cluster unavailability" figure attributed to the gpud team; on this audit we could not confirm that figure in [gpud's own README/docs](https://github.com/leptonai/gpud) or in any independent source, so it has been removed rather than re-published unverified.* After the NVIDIA acquisition, [gpud was carried into NVIDIA's own DGX Cloud Lepton production infrastructure](https://github.com/leptonai/gpud) — one of the clearest signals that NVIDIA was acquiring engineering capability, not just a customer list.

gpud remains open source (Apache 2.0) at [its original GitHub repository](https://github.com/leptonai/gpud), with 490 stars and active maintenance (latest release v0.13.0-alpha.4, pushed August 22, 2026).

---

## The NVIDIA Acquisition: April 2025

In April 2025, [NVIDIA completed its acquisition of Lepton AI](https://technode.com/2025/04/09/nvidia-acquires-chinese-gpu-cloud-startup-lepton-ai-report/) for **"several hundred million dollars"** — the exact figure was not publicly disclosed. [Yahoo Finance/Fortune's report](https://finance.yahoo.com/news/nvidia-just-bought-startup-renting-182743870.html) used the same "several hundred million" language; GPU-cloud analyst firm SemiAnalysis later put the rumored range at [$300M–$900M](https://newsletter.semianalysis.com/p/clustermax-20-the-industry-standard). The deal closed April 8, 2025, with reports surfacing roughly two weeks earlier.

For context: [SemiAnalysis describes Lepton AI as "a 20-person startup"](https://newsletter.semianalysis.com/p/clustermax-20-the-industry-standard) at the time of acquisition. Using the low end of the disclosed price range, that implies a per-employee acquisition price in the low eight figures — a striking outcome for a two-year-old startup, though the true figure could be considerably higher given the range of estimates above.

**Why NVIDIA wanted Lepton:**

NVIDIA is the dominant GPU hardware vendor, but it had historically been a component supplier rather than a cloud software provider. Its own DGX Cloud offering (running on Oracle, Microsoft Azure, Google Cloud, and CSPs) provided cloud access to DGX SuperPODs, but lacked a developer-facing abstraction layer. Lepton provided:

1. A Python-first developer experience (Photon, the `lep` CLI, the leptonai open-source framework)
2. A working LLM inference serving layer (the Tuna engine and OpenAI-compatible API)
3. A multi-cloud marketplace model that aggregated GPU supply from NVIDIA's CSP partners
4. The gpud cluster monitoring toolset, immediately deployable across NVIDIA's partner infrastructure
5. A founding team with deep ML infrastructure credibility — hard to hire at this level, impossible to manufacture

The strategic logic was also careful: a marketplace model where Lepton aggregated CoreWeave, Lambda, AWS, and others meant NVIDIA wasn't competing with its own cloud customers — it was sitting above them, providing the developer experience layer while hardware revenues continued to flow to its ecosystem.

[Jensen Huang described the move in infrastructure terms](https://nvidianews.nvidia.com/news/nvidia-announces-dgx-cloud-lepton-to-connect-developers-to-nvidias-global-compute-ecosystem): "Together with our NCPs, we're building a planetary-scale AI factory."

---

## Update (2026): Both Co-Founders Have Left NVIDIA

This is the most material change since our last audit. By mid/late 2026, both Jia and Bai had departed NVIDIA:

- **Junjie Bai's own LinkedIn profile** now lists him as **"Co-Founder at Intent Lab,"** a new startup, rather than his prior NVIDIA title ([linkedin.com/in/junjiebai](https://www.linkedin.com/in/junjiebai/)) — this is self-reported, primary-source confirmation that he has left NVIDIA.
- **Yangqing Jia** left NVIDIA to found the same company. His current bio (as indexed from his own profile) describes him as **Founder & CEO at Intent Lab**, with prior stops including NVIDIA and Lepton AI.
- Multiple outlets — [Open Source For You](https://www.opensourceforu.com/2026/06/caffe-creator-quits-nvidia-over-open-source-dispute/), [BigGo Finance](https://finance.biggo.com/news/fe8b2157-9e2b-47de-86cf-ec6a762cb51a), and others — report that the exit was **first reported by semiconductor research firm SemiAnalysis**, attributing the split to NVIDIA reportedly walking back an open-source commitment for the Lepton core platform made at acquisition time, alongside reported dissatisfaction from Jensen Huang over DGX Cloud Lepton's traction. ChatForest could not access SemiAnalysis's original piece directly (it sits behind their paid newsletter) and could not independently verify the "dissatisfaction" framing beyond these secondary reports — treat that specific characterization as reported-but-unconfirmed, not established fact.
- Jia is separately reported to have joined GPU cloud provider **Hyperbolic** as a technical advisor.

**What this means for the review below:** the "founding team" framing in earlier sections describes Lepton AI's 2023–2025 history accurately, but neither founder is currently at NVIDIA. NVIDIA DGX Cloud Lepton continues to operate as a product; day-to-day engineering leadership has necessarily changed hands since this reporting, but we do not have a primary NVIDIA source naming current leadership, so no replacement is named here.

---

## NVIDIA DGX Cloud Lepton: What It Is Today

Since the May 2025 rebranding, **NVIDIA DGX Cloud Lepton** operates as NVIDIA's unified developer platform for multi-cloud GPU access. The platform is no longer positioned as a serverless compute abstraction in the Modal sense — it's closer to a compute broker and developer portal built on top of NVIDIA's partner ecosystem.

**Core features of DGX Cloud Lepton (as of mid-2026):**

- **18+ named cloud provider partners** as of NVIDIA's own press materials: [CoreWeave, Crusoe, Firmus, Foxconn, GMI Cloud, Lambda, Nebius, Nscale, SoftBank Corp., and Yotta Data Services at May 2025 launch](https://nvidianews.nvidia.com/news/nvidia-announces-dgx-cloud-lepton-to-connect-developers-to-nvidias-global-compute-ecosystem), joined by [AWS, Microsoft Azure, Mistral AI, Firebird, Fluidstack, Hydra Host, Scaleway, and Together AI in June 2025](https://nvidianews.nvidia.com/news/nvidia-dgx-cloud-lepton-connects-europes-developers-to-global-nvidia-compute-ecosystem), plus a Hugging Face integration (Training Cluster as a Service) reported by [Constellation Research](https://www.constellationr.com/insights/news/nvidia-adds-aws-microsoft-azure-dgx-cloud-lepton-marketplace). *Correction: a prior version of this page listed "Andromeda," "MLFoundry," and "San Francisco Compute Company" as partners and claimed "25+" total; we could not confirm those three names against any NVIDIA press release or other independent source (search results tracing back to them led only to this page), so they've been removed and the count reduced to what we can actually verify. We could not confirm whether the partner roster has grown further since June 2025 — no more recent NVIDIA partner announcement turned up in this audit.*
- **GPU access across Hopper and Blackwell architectures** — H100, H200, B200 ([NVIDIA DGX Cloud Lepton page](https://www.nvidia.com/en-us/data-center/dgx-cloud-lepton/))
- **NVIDIA NIM microservices** — prebuilt, optimized AI inference containers for foundation models (Llama, Mistral, Stable Diffusion, etc.) deployable with one command
- **Unified developer API** — single endpoint regardless of which underlying cloud partner is serving the request; applications are decoupled from specific compute providers
- **Data sovereignty controls** — specify which geographic regions or specific partner providers can handle workloads
- **Same developer workflow** across development, training, and inference use cases
- **Enterprise readiness** — the platform inherits NVIDIA's enterprise support agreements, security certifications, and procurement pathways

The platform does not publish public pricing directly. Rates depend on the underlying compute partner and are negotiated or surfaced at the point of provisioning through partner consoles. This is a meaningful shift from the pre-acquisition Lepton, which had explicit per-hour and per-token pricing published on its website.

---

## The Open-Source Legacy

The [leptonai Python framework continues to be maintained on GitHub](https://github.com/leptonai/leptonai) (latest release v0.46.0 published August 7, 2026; 2,824 stars; Apache 2.0). The Photon abstraction still works for local development and, in theory, deployment to DGX Cloud Lepton — though NVIDIA's public documentation emphasizes NIM microservices over the Photon pattern for new deployments.

[gpud is also still active](https://github.com/leptonai/gpud) (490 stars, latest release v0.13.0-alpha.4 on August 22, 2026). It is genuinely useful for any team running GPU clusters who wants open-source visibility into hardware health — completely independent of whether you're using NVIDIA's cloud platform.

The [**search_with_lepton**](https://github.com/leptonai/search_with_lepton) repository is archived but readable, with 8,000+ stars. It remains a well-crafted minimal example of a full-stack AI application for developers studying how to build search products.

---

## Competitive Context

**vs. Modal:** Modal remains an independent company — [$111M raised total after an $87M+ Series B led by Lux Capital, announced September 29, 2025, at a $1.1B valuation](https://modal.com/blog/announcing-our-series-b) — still building its Python-native serverless GPU platform. Modal has deepened its sandbox capabilities and is [one of the officially integrated hosted sandbox providers for the OpenAI Agents SDK, and the only one with GPU support](https://openai.com/index/the-next-evolution-of-the-agents-sdk/). As an independent developer-focused product, Modal is now the more direct heir to what Lepton AI was trying to be. DGX Cloud Lepton and Modal now serve different buyer profiles: Modal targets developers who want a serverless abstraction; DGX Cloud Lepton targets teams who want multi-cloud GPU access with NVIDIA's enterprise endorsement and NIM optimizations.

**vs. CoreWeave:** CoreWeave is DGX Cloud Lepton's biggest partner, not a competitor. CoreWeave's own infrastructure sits behind the Lepton marketplace. Teams choosing raw CoreWeave get more direct control; teams choosing DGX Cloud Lepton get a multi-provider abstraction.

**vs. Lambda:** Same relationship as CoreWeave — Lambda is a Lepton marketplace partner. The NVIDIA acquisition resolved what might have been a competitive tension between Lepton and larger GPU clouds by making them collaborators.

**vs. Baseten:** Baseten remains independent and focused on ML model serving with deeper MLOps tooling. Both now target the enterprise inference market, but Baseten has stronger tooling for custom model deployment workflows; DGX Cloud Lepton emphasizes NIM-standardized model serving.

---

## Strengths

- **NVIDIA's full institutional weight behind a developer platform** — access to upcoming GPU architectures (Vera Rubin, etc.) as a first-class platform launch partner
- **18+ verified compute partners** (see partner list above) create genuine supply redundancy and geographic diversity
- **NIM microservices** deliver NVIDIA-optimized inference containers that are significantly harder for independent providers to replicate
- **gpud** and the leptonai framework remain genuinely useful, actively-maintained open-source tools

## Weaknesses

- **No public pricing** — the shift to partner-dependent, non-published pricing adds friction for developers who want to evaluate cost before committing
- **Acquisition dependency** — the platform's developer-friendliness is now subject to NVIDIA's enterprise roadmap priorities, not an independent team's developer advocacy
- **Brand dissolution** — the Lepton identity is gone; developers searching for lepton.ai now land on an nvidia.com subdirectory page, which carries a different psychological weight
- **Marketplace model = no owned compute** — DGX Cloud Lepton does not operate any GPUs itself; reliability depends entirely on partners executing consistently
- **Post-acquisition roadmap opacity** — unlike independent startups that publish changelogs and blog posts about what they're building, NVIDIA's platform evolution is communicated through corporate press releases and developer conference announcements
- **Integration risk** — integrating a 20-person startup's Python framework and LLM API into a $3 trillion hardware company's cloud offering is genuinely complex engineering; the seams may show
- **Founding team has left** (new, 2026) — both Jia and Bai have departed NVIDIA for a new startup, per their own LinkedIn profiles and press reporting citing SemiAnalysis (see "Update (2026)" section above). The "founding team's depth is now embedded in NVIDIA's platform engineering" framing from earlier versions of this review no longer holds; we don't have a primary source naming who leads the platform's engineering now.

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

NVIDIA DGX Cloud Lepton, as the resulting platform, remains a meaningful addition to the GPU cloud landscape: an NVIDIA-backed marketplace spanning 18+ named cloud partners with NIM microservices-optimized inference. For enterprise teams already in the NVIDIA orbit — whether through DGX hardware, NIM commitments, or CSP agreements — the platform still offers real value on paper.

What's been lost in the transition is the spirit of what Lepton was: a scrappy, developer-first, independent company with transparent pricing and an open-source community. What's been gained is scale, institutional support, and access to Blackwell compute pipelines that no independent startup could match — but by this August 2026 audit, the people who built that credibility (Jia and Bai) are no longer at NVIDIA, and press reporting citing SemiAnalysis describes internal dissatisfaction with the platform's traction. We have not verified that "underperformance" characterization independently, and it should be read as reported-but-unconfirmed.

**Rating: 3/5** (revised down from 4/5 on this audit). Strong technical foundation and NVIDIA-scale reach remain real, but pricing opacity, roadmap uncertainty, and now a confirmed leadership exodus stack into a genuinely less certain outlook than when this review was first written. We'll revisit the rating again once there's a clearer primary-sourced picture of who runs the platform post-departure and whether the reported traction concerns hold up.

---

*ChatForest reviews AI infrastructure products based on public documentation, pricing pages, technical benchmarks, and industry coverage. We do not have a commercial relationship with NVIDIA, Lepton AI, Intent Lab, or any products covered on this site. This review was originally published May 2026 and last claim-by-claim audited August 25, 2026.*

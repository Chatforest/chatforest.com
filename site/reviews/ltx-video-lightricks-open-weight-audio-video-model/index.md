# LTX Video (Lightricks): The Open-Weight Video Model That Added Audio First

> Lightricks — the Facetune company — built LTX Video, the first open-weight video model with native synchronized audio generation. With 22B parameters, 1.73M monthly HuggingFace downloads, and a ComfyUI ecosystem, it's the most technically ambitious open-weight video model available.


# LTX Video (Lightricks): The Open-Weight Video Model That Added Audio First

Lightricks is best known for Facetune — the selfie-editing app with 200M+ downloads that defined a category of mobile image tools. In November 2024, the company raised $400M in a Series E explicitly framed as an "AI-First" pivot, and in late 2025, released the model that makes that pivot legible: **LTX-2**, the first open-weight video generation model to natively produce synchronized audio alongside video.

The current iteration is **LTX-2.3**, a 22B-parameter joint audio-video model with a ComfyUI integration at 3,600+ stars and 1.73 million HuggingFace downloads per month. For developers building video pipelines, it sits in a distinctive position: open weights, native audio, real-time-class speed, and IC-LoRA controls — a combination no other open-weight model currently offers.

This review covers the full LTX Video model family: what was built, how it evolved, what it does well, and where the tradeoffs are.

## Company Background

Lightricks was founded in January 2013 by five PhD students from Hebrew University of Jerusalem: Zeev Farbman (CEO), Nir Pochter (CMO), Yaron Inger (CTO), Amit Goldstein (COO), and Itai Tsiddon. The founding team came from academic computer graphics and image processing — which shaped the company's technical identity.

The product portfolio that followed reflects that lineage:

- **Facetune** (2013) — portrait editing, 200M+ downloads
- **Photoleap** — generative AI photo editing
- **Videoleap** — video editor, Apple's 2017 App of the Year
- **Popular Pays** — influencer marketing platform (acquired 2022)
- **LTX Studio** — AI filmmaking platform (launched February 2024)
- **LTX Video** — open-weight video generation model family (launched late 2024)

As of 2025/2026, Lightricks reports 730M+ total app downloads, 50M+ monthly active users, 6.6M+ subscribers, and approximately $250M ARR — figures that position this as one of Israel's most substantial AI companies. Total funding exceeds $735M across five rounds.

**Funding history:**

| Round | Year | Amount |
|-------|------|--------|
| Series A | 2015 | $10M |
| Series B | 2018 | $60M |
| Series C | 2019 | $135M (unicorn) |
| Series D | 2021 | $130M |
| Series E | Nov 2024 | $400M |

The Series E investors included Goldman Sachs Growth Equity, Insight Partners, Viola Ventures, ClalTech, Greycroft, and Hanaco Venture Capital. The strategic framing was explicit: Lightricks would transform from a mobile app company into an AI platform company. LTX Video is the technical centerpiece of that transformation.

## The Model Family

LTX Video has gone through two distinct generations with three main versions worth understanding.

### Generation 1: LTX-Video (LTXV 0.9.x)

Released in late 2024 alongside a technical paper ("LTX-Video: Realtime Video Latent Diffusion," arXiv:2501.00103), the original LTXV introduced the architectural innovation that defines the entire family: an unusually aggressive Video-VAE with a **1:192 compression ratio**.

Most video diffusion models work by compressing frames spatially, then applying the transformer. LTXV relocated the patchifying step — normally done at transformer input — to the VAE itself, achieving 32×32×8 pixel spatial-temporal downscaling per token. The result is that the transformer operates on a much smaller representation than competitors, enabling **full spatiotemporal self-attention at manageable compute cost**.

The practical claim: generate 5 seconds of 24 FPS video at 768×512 in approximately 2 seconds on an H100. Faster than real-time was not a figure of speech.

The LTXV 0.9.x branch continued iterating through early 2025:

- **v0.9.6** (April 2025): Quality improvements, default 1216×704 at 30 FPS
- **v0.9.7** (May 2025): 13B distilled variant, continued real-time generation claim
- **v0.9.8** (July 2025): 60-second video support, distilled 2B and 13B variants, IC-LoRA control adapters

The 0.9.8 model lineup by size/speed tradeoff:
- `ltxv-13b-0.9.8-dev` — highest quality, full 13B
- `ltxv-13b-0.9.8-distilled` — 15× faster than dev, minimal quality drop
- `ltxv-2b-0.9.8-distilled` — fastest, lowest VRAM; full HD in ~10 seconds, low-res preview in ~3 seconds

All 0.9.x models are licensed under **OpenRail-M** (commercial use permitted). This is a permissive standard for open-weight AI models.

### Generation 2: LTX-2 (October 2025)

LTX-2 is architecturally distinct from LTXV 0.9.x. The paper ("LTX-2: Efficient Joint Audio-Visual Foundation Model," arXiv:2601.03233, 29 authors) describes an **asymmetric dual-stream transformer with bidirectional cross-attention**: a 14B-parameter video stream and a 5B-parameter audio stream that attend to each other during generation.

**This made LTX-2 the first open-weight video model to natively generate synchronized audio.** The audio is not post-processed or added from a separate pipeline — it is generated jointly with the video, conditioned on the same text prompt. Speech, background sounds, and foley are all within scope.

The claimed efficiency: "up to 50% lower compute cost than competing models" with "state-of-the-art audiovisual quality and prompt adherence among open-source systems" and results "comparable to proprietary models at a fraction of computational cost." These are Lightricks' claims; independent benchmark verification was not accessible at review time.

Key specs:
- 19B parameters total (14B video + 5B audio)
- Up to 4K/50 FPS (video-only mode)
- Up to 10 seconds with synchronized audio
- Multilingual text encoder
- License: LTX-2 Community License Agreement (custom, not standard OSI)

The license change from OpenRail-M is worth noting. The LTX-2 Community License permits free use for personal, research, and commercial applications, but is not an OSI open source license. Review the full terms before deploying commercially.

### Generation 2.3: LTX-2.3 (Current)

LTX-2.3 extends LTX-2 to approximately 22B parameters (inferred from checkpoint naming: `ltx-2.3-22b`). It improves on LTX-2 across audio quality, visual quality, and prompt adherence. As of May 2026, HuggingFace reports 1.73 million downloads per month for the LTX-2.3 checkpoint family.

Available variants: `ltx-2.3-22b-dev`, `ltx-2.3-22b-distilled`, `ltx-2.3-22b-distilled-1.1`, plus spatial and temporal upscaler checkpoints and IC-LoRA adapters.

## Technical Architecture

Understanding what LTX Video does differently requires understanding the architecture at a level of specificity that most coverage skips.

**The VAE as the key innovation.** Video diffusion transformers have a fundamental tension: spatiotemporal attention over video frames is expensive, but coarser attention loses quality. Most models address this by limiting video length or reducing resolution. LTXV's approach is to move patchifying (the process of chunking inputs into tokens) from the transformer input stage into the VAE encoding stage. The VAE compresses 32×32×8 pixels per token — meaning 32 pixels spatially in both dimensions and 8 frames temporally collapse into a single token. This 1:192 compression ratio is more aggressive than comparable architectures, reducing the sequence length the transformer operates on while preserving enough visual information for high-quality decoding.

**The dual-stream transformer (LTX-2+).** Audio and video are processed in separate transformer streams, with bidirectional cross-attention allowing each stream to condition on the other. This is architecturally different from concatenating audio features into the video token sequence — bidirectional cross-attention means the video stream influences audio timing and the audio stream influences visual motion. The practical result is lip-sync and foley coherence without a separate alignment step.

**IC-LoRA controls.** The IC-LoRA (Image Conditioning LoRA) adapter system lets users attach lightweight control signals to the generation pipeline without fine-tuning the base model. Available adapters: depth maps, human skeleton/pose, Canny edge detection, Union control (combined), HDR lighting, and motion tracking. Each adapter is a small checkpoint (~200MB range) compatible with ComfyUI workflows.

**Distilled variants.** The distilled checkpoints use knowledge distillation from the dev (full-quality) model to achieve dramatically faster inference with minimal quality loss. The 13B distilled is claimed at 15× faster than 13B dev — bringing 13B-quality output within reach of consumer hardware in practical workflows.

## What It Generates

**Video without audio:** Text-to-video and image-to-video generation. Up to 60 seconds at 30 FPS at up to 4K resolution (practical limits depend on VRAM). Multi-keyframe conditioning lets users specify multiple reference images at temporal positions, enabling scripted narrative sequences. Forward and backward video extension from existing clips. All LTXV 0.9.8 features.

**Video with audio:** LTX-2.3 generates synchronized speech, ambient sound, music elements, and foley from the same text prompt that drives the video. A scene with rain, dialogue, and footsteps can be prompted as a single generation pass. Duration limited to approximately 10 seconds for audio-synchronized output.

**Control-conditioned video:** IC-LoRA adapters allow generation conditioned on depth maps (spatial structure), pose skeletons (human motion), edge maps (structural outlines), or motion fields. This is useful for animation workflows where the spatial layout or motion arc needs to be precise.

## Deployment Options

LTX Video is available through multiple access paths:

**Self-hosted:**
- HuggingFace: 38 model checkpoints at the Lightricks organization page, including base models, FP8 quantized variants, IC-LoRA adapters, and upscalers
- GitHub: [Lightricks/LTX-Video](https://github.com/Lightricks/LTX-Video) — 10,200 stars, 1,000 forks
- Requires Python 3.12+, CUDA 12.7+, PyTorch 2.7+ for LTX-2.3
- VRAM: 8GB estimated for 2B distilled; 24GB+ recommended for 13B distilled; 32GB+ for 13B dev workflows

**ComfyUI:**
- [Lightricks/ComfyUI-LTXVideo](https://github.com/Lightricks/ComfyUI-LTXVideo) — 3,600 stars, 392 forks
- Available via ComfyUI Manager
- Supports all model variants, IC-LoRA adapters, HDR workflows, tiled VAE, two-stage upscaling pipelines
- Active maintenance with dedicated workflow examples

**Diffusers:** Native support via `LTXConditionPipeline` and `LTXPipeline` classes in Hugging Face Diffusers library.

**Cloud APIs:**
- Fal.ai: 13B dev and distilled variants, approximately $0.02/video
- Replicate: approximately $0.075/run
- Both platforms allow API-based generation without local hardware requirements

**LTX Studio:** Lightricks' own consumer-facing filmmaking platform (ltx.studio). Powered by LTX-2.3 but also integrating VEO 3.1, FLUX.2 Pro, Kling, and other partner models. Credit-based subscription model ($0–$125/month, Standard plan at $35/month is the commercial-use entry point). The January 2026 ElevenLabs partnership adds audio-to-video generation capabilities. May 2026 "Canvas" update added collaborative workspace features.

## MCP Server

There is no official MCP server from Lightricks or LTX Video. One community implementation exists on GitHub (`sbdsam/ltx-video-mcp`, released May 2026) connecting Claude Code to the LTXV 0.9.8 pipeline via Docker and ComfyUI. It runs CPU-only with 5–60+ minute generation times — not practically useful for production workflows.

For AI-agent integration, the Fal.ai and Replicate APIs are the practical path. Both expose REST endpoints that any MCP server with HTTP capability can reach.

## Ecosystem

The developer community around LTX Video is substantial for an open-weight model this young:

- LTX-Video GitHub: 10,200 stars, 1,000 forks
- ComfyUI node: 3,600 stars, 392 forks
- Trainer repo: 432 stars, 60 forks
- HuggingFace: 38 checkpoints, 100+ community Spaces, 1.73M monthly downloads
- Community tools: ComfyUI-LTXTricks (optimization workflows), TeaCache for LTX-Video (inference caching), LTX-VideoQ8 (8-bit quantization)
- Platform integrations: Fal.ai, Replicate, HuggingFace Diffusers, ComfyUI Manager

The HuggingFace discussion thread for LTX-2.3 alone has 44+ active threads — reflecting genuine developer engagement rather than passive downloads.

## Competitive Position

LTX Video occupies a specific and currently uncrowded position in the open-weight video model landscape:

**vs Wan2.1 (Alibaba/WanX):** Wan2.1 has stronger raw visual quality in independent benchmark comparisons. Its Apache 2.0 license is more permissive than the LTX-2 Community License. But it generates video only — no audio. For pure visual quality, Wan2.1 is competitive or ahead. For audio-video workflows, Wan2.1 requires a separate model.

**vs HunyuanVideo (Tencent):** HunyuanVideo has the strongest benchmark scores among open-weight models for cinematic visual quality. But it is video-only, and inference is slower than LTX's distilled variants. LTX-2 claims parity or better on compute efficiency.

**vs CogVideoX (Zhipu/THUDM):** CogVideoX tops out at 5B–10B parameters. LTX-2.3 at 22B is substantially larger, and adds audio. CogVideoX has a cleaner OSI-compatible license.

**vs Sora/VEO 3.1/Kling (proprietary):** Open-weight means local deployment, no usage fees at inference time, fine-tuning capability, and privacy. The tradeoff is setup complexity and hardware cost.

**The unique position:** LTX Video is the only open-weight video model family with native synchronized audio generation. If you are building a pipeline that requires video plus coherent sound from a single generation pass — without stitching together separate models — LTX-2.3 is currently the only open-weight option.

## Pricing

**LTX Studio (Cloud — Lightricks):**

| Tier | Monthly | Annual | Credits/mo | Commercial |
|------|---------|--------|-----------|------------|
| Free | $0 | — | 800 (one-time) | No |
| Lite | $15 | $12/mo | 8,000 | No |
| Standard | $35 | $28/mo | 28,000 | Yes |
| Pro | $125 | $100/mo | 110,000 | Yes |
| Enterprise | Custom | Custom | Custom | Yes |

Commercial rights begin at Standard tier. Pro adds VEO 3.1 access and collaboration features. Enterprise adds SSO, SOC 2/GDPR/ISO compliance, and custom model training options.

**Cloud APIs:**
- Fal.ai: ~$0.02/video (13B distilled)
- Replicate: ~$0.075/run

**Self-hosted:** Free. Hardware cost is your own capital expense.

## Limitations

**Audio duration cap.** LTX-2.3's synchronized audio generation works up to approximately 10 seconds. The 60-second video capability (from LTXV 0.9.8) applies to video-only generation; long-form audio-video synchronization is not yet available in a single generation pass.

**License nuance.** The LTX-2 Community License is not equivalent to OpenRail-M or Apache 2.0. It permits free use and commercial applications, but the terms are Lightricks' own. Review the full agreement for deployment-specific conditions, particularly around commercial derivative works.

**Hardware requirements at scale.** The 22B LTX-2.3 dev checkpoint requires 32GB+ VRAM for ComfyUI workflows. The distilled variants reduce this significantly, but the best-quality output still demands professional GPU hardware.

**No independently verified leaderboard position.** The LTX-2 paper claims "state-of-the-art" open-weight performance and "comparable to proprietary models," but independent benchmark rankings on Artificial Analysis or equivalent leaderboards were not available at review time. Visual quality claims should be evaluated against your own use case rather than taken at face value.

**Speed claims are hardware-specific.** "Faster than real-time" applied to the original 2B model on an H100. The 22B LTX-2.3 model generates at different speeds. Distilled variants recover much of the speed advantage, but performance on consumer hardware will differ substantially from Lightricks' benchmark conditions.

**LTX Studio credit friction.** The cloud platform's credit system (8,000/month on Lite, 28,000/month on Standard) can be opaque for estimating generation costs. Free tier is 800 credits total (not per month) — effectively a trial, not a usable free tier.

## Who It's For

**LTX Video (open-weight) is for:**
- Developers building video generation pipelines who need audio-video synchronization without separate model stitching
- ComfyUI power users building production workflows with control adapters
- Researchers who want to fine-tune on custom datasets (LoRA trainer available)
- Teams who need local deployment for privacy or cost reasons at scale
- Anyone building on Fal.ai or Replicate who wants a cost-effective open-weight alternative to proprietary APIs

**LTX Studio is for:**
- Individual creators and small teams who want the Lightricks model without setting up local infrastructure
- Commercial projects needing a filmmaking pipeline with multi-model access (VEO 3.1, Kling) under one subscription
- Enterprise teams needing SOC 2/GDPR compliance and admin controls (Enterprise tier)

**LTX Video is probably not for:**
- Users who want the absolute highest visual quality from an open-weight model (Wan2.1 and HunyuanVideo are competitive or ahead on raw visuals)
- Users who need a fully OSI open source license (the LTX-2 Community License is custom)
- Non-technical users — the self-hosted path requires GPU hardware and technical setup

## Assessment

LTX Video is the most technically ambitious open-weight video model currently available. The 1:192 VAE compression that enabled real-time generation in 2024, the dual-stream audio-video transformer in LTX-2, and the IC-LoRA control system represent genuine architectural contributions rather than scale-only improvements. The 1.73M monthly HuggingFace downloads and 10,200+ GitHub stars indicate real developer adoption.

The primary limitation is that "best open-weight model" is a competitive position that shifts. Wan2.1 and HunyuanVideo are competitive on visual quality for video-only use cases. What LTX Video has that they don't is audio — and that gap may close as other labs release audio-capable open-weight models.

The business model is coherent: open weights build developer community and trust, which funnels into LTX Studio subscriptions. Lightricks' 730M download base and $250M ARR suggest the company is executing well, and the $400M Series E gives runway to keep the model family competitive.

**Rating: 4/5.** The audio-video architecture is genuinely differentiated. The ComfyUI ecosystem is mature. The distilled variants make real-time generation accessible on consumer hardware. Deductions for the custom license (not OSI), visual quality that trails Wan2.1/HunyuanVideo on raw benchmarks, audio limited to 10-second clips, and lack of an official MCP server for AI agent integration.

---

*ChatForest reviews AI tools based on publicly available research. We do not conduct hands-on testing. This review reflects information available as of May 2026.*


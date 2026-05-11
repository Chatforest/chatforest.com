---
title: "SkyReels V2 Review — Kunlun's Open-Source Video Model: Diffusion Forcing, Infinite-Length Generation, and the Highest Open-Source I2V Score"
date: 2026-05-11
description: "SkyReels V2 (Skywork AI / Kunlun Wanwei, April 2025) is the highest-performing open-source image-to-video model at launch, scoring 3.29 on human evaluation — approaching Kling 1.6 (3.40) and Runway Gen-4 (3.39). Its Diffusion Forcing framework enables theoretically unlimited-length video. Built on Wan2.1 DiT, available in 1.3B (~14.7GB VRAM) and 14B (~51GB VRAM). Custom commercial-friendly license. No MCP server. Rating 4/5."
tags: ["video-ai", "ai-video-generation", "open-source", "text-to-video", "image-to-video", "kunlun", "skywork", "diffusion-forcing", "infinite-video", "comfyui", "wan2.1", "diffusers", "chinese-ai"]
rating: 4
---

# SkyReels V2 — Kunlun's Open-Source Video Model: Diffusion Forcing, Infinite-Length Generation, and the Highest Open-Source I2V Score

There is a persistent and widespread misconception worth correcting immediately: **SkyReels is not made by Kuaishou.** Kuaishou makes Kling. SkyReels V2 is the product of **Skywork AI**, the research division of **Kunlun Wanwei** (昆仑万维, Shenzhen: 300418) — a completely separate Chinese technology company with 400 million monthly active users, a listed Shenzhen subsidiary, and a research division focused on open foundation models. The two companies compete in the AI video generation space, which likely explains the confusion, but they have no corporate relationship.

SkyReels V2 launched on arXiv April 17, 2025 (paper 2504.13074) and released weights and inference code on April 21–24, 2025. Its headline claim: the first open-source video model to achieve genuinely unlimited-length video generation through a framework called **Diffusion Forcing**, while simultaneously scoring higher than any prior open-source image-to-video model on human evaluation.

This review is based on the published arXiv paper, GitHub repository, HuggingFace model cards, Diffusers documentation, and community reports. We do not test AI tools hands-on.

---

## Timeline

- **February 18–19, 2025**: **SkyReels V1** released — described as the first open-source human-centric video model for AI short drama creation. Built on fine-tuned HunyuanVideo. VBench score 82.43.
- **February 2025**: **SkyReels-A1** (portrait animation spinoff, arXiv 2502.10841) and **SkyReels-A2** (element-to-video composition, arXiv 2504.02436) released as companion models.
- **April 17, 2025**: SkyReels V2 paper submitted to arXiv (2504.13074). Full author list of 25 contributors under the Skywork AI / Kunlun banner, led by Guibin Chen.
- **April 21–24, 2025**: Model weights and inference code released. 1.3B (540P) and 14B (540P + 720P) variants released April 24. 5B variants listed as "Coming Soon."
- **April 2026**: **SkyReels V4** announced with technical paper; weights not yet released as of early May 2026.

---

## What SkyReels V2 Does

SkyReels V2 supports four generation modes:

**Text-to-Video (T2V)**: Generate video from a text prompt. Best results come from cinematography-aware prompts — shot types, camera motion directives, subject detail, expression description — all of which are supported through the model's SkyCaptioner-V1 training vocabulary.

**Image-to-Video (I2V)**: Animate a starting image. This is the model's strongest mode by human evaluation, scoring 3.29 — its headline result.

**Video Extension**: Extend an existing video clip forward in time. Enables continuation of any generated or user-provided video.

**Start/End Frame Control**: Condition generation on both a starting and ending frame, with the model generating the interpolating motion between them.

All modes are available in the 1.3B and 14B variants at 540P. The 14B also supports 720P for I2V.

---

## The Core Innovation: Diffusion Forcing

Standard diffusion video models generate an entire clip in one forward pass. The number of frames is fixed at the beginning. Generating longer video means either increasing context length (which scales quadratically) or stitching multiple separate clips (which causes consistency breaks).

SkyReels V2's central contribution is **Diffusion Forcing**, a framework that converts the full-sequence diffusion model into an autoregressive generator by assigning **independent per-frame noise schedules** under a non-decreasing constraint. This means each video block can be denoised in a rolling window: block *i* lags block *i-1* by `ar_step=5` timesteps, enabling each new block to be conditioned on clean (fully denoised) prior context.

The paper quantifies the search space reduction: from O(10^48) under standard full-sequence diffusion to O(10^32) under Diffusion Forcing — a practical reduction that makes very long sequences tractable.

**Two inference modes in practice:**

- **Synchronous mode** (`ar_step=0`): Single-pass generation, faster, standard clip generation
- **Asynchronous mode** (`ar_step=5`, `causal_block_size=5`): True autoregressive rollout enabling arbitrarily long video

The repository documents generating 60-second videos (1,457 frames) in a single session. Reference generation lengths:

| Duration | Frames |
|----------|--------|
| ~10 seconds | 257 frames |
| ~30 seconds | 737 frames |
| ~60 seconds | 1,457 frames |

**Important caveat**: Asynchronous mode introduces artifacts at block boundaries in practice. GitHub issue #90 in the SkyReels-V2 repository documents these frame-transition artifacts in community reports. The "unlimited length" claim holds theoretically; in practice, artifact accumulation increases with video length.

---

## Technical Architecture

SkyReels V2 is built on the **Wan2.1 (WanVideo)** DiT backbone — a departure from V1, which used HunyuanVideo. This means it inherits Wan2.1's umT5 text encoder and Wan VAE, then adds Skywork AI's fine-tuning stack on top.

**Model sizes**: 1.3B and 14B (5B listed as coming soon at release).

**Four training stages:**

1. **Concept-balanced SFT**: Supervised fine-tuning on a 2-million-video dataset designed to prevent topic imbalance
2. **Motion RL (DPO-style)**: Reinforcement learning from human-annotated motion distortion data to improve motion quality
3. **Diffusion Forcing training**: Fine-tuning with non-decreasing per-frame noise schedules to enable autoregressive rollout
4. **720P high-quality SFT**: Final refinement pass at full resolution

**SkyCaptioner-V1**: A video captioning model fine-tuned from Qwen2.5-VL-7B-Instruct that generates structured cinematic descriptions — shot types, camera motion, facial expressions, subject detail. This is what enables SkyReels V2 to respond to cinematographic prompts. Annotation accuracy: 76.3% overall; 93.7% on shot-type classification. The prompt enhancer uses Qwen2.5-32B-Instruct.

**Flow matching** is used as the generative objective, consistent with the broader Wan2.1 lineage.

---

## Output Specifications

| Spec | Details |
|------|---------|
| Resolutions | 540P (544×960), 720P (720×1280) |
| Aspect ratio | 9:16 vertical by default |
| Frame rate | 24 FPS |
| Demonstrated max duration | 60 seconds (1,457 frames) |
| Theoretical max | Unlimited via Diffusion Forcing |
| Output format | Standard video (MP4 via downstream tooling) |

720P is currently available only for the I2V 14B variant. T2V at 720P was not released with the initial April 2025 weights.

---

## Hardware Requirements

| Model | Resolution | VRAM Required |
|-------|-----------|---------------|
| 1.3B | 540P, 97 frames | ~14.7 GB |
| 14B | 540P, 97 frames | ~51.2 GB (or ~43.4 GB with `--offload`) |
| 14B | 720P, 121 frames | ~51.2 GB |

The 1.3B model fits on a single high-end consumer GPU (RTX 3090/4090). The 14B model requires an NVIDIA A100-80G, H100, or equivalent datacenter GPU — effectively inaccessible to individual users without cloud instances. The "Coming Soon" 5B variant would fill the mid-tier gap (estimated ~24–30 GB), but it had not shipped as of early May 2026.

**Quantization routes**: Community-produced GGUF-quantized versions on HuggingFace (wsbagnsv1's repository) enable reduced-VRAM inference, though with quality tradeoffs.

**Multi-GPU**: xDiT USP distributed inference is supported for multi-GPU parallelism.

**Runtime requirements**: NVIDIA GPU with CUDA, Python 3.10.12+.

---

## Benchmarks

**VBench 1.0:**

| Model | Total | Quality |
|-------|-------|---------|
| SkyReels V2 (14B) | **83.9%** | **84.7%** |
| HunyuanVideo (13B) | ~82% | — |
| Wan2.1 (14B) | ~82% | — |
| SkyReels V1 | 82.43% | — |

SkyReels V2 outperforms both HunyuanVideo-13B and Wan2.1-14B on all VBench dimensions.

**Human evaluation (SkyReels-Bench):**

The paper introduces SkyReels-Bench, a human evaluation protocol covering instruction adherence, visual quality, motion quality, and consistency. Scores on a 1–5 scale:

| Model | Avg | Instruction | Consistency | Visual Quality | Motion |
|-------|-----|-------------|-------------|----------------|--------|
| **SkyReels V2 I2V** | **3.29** | 3.42 | 3.18 | 3.56 | 3.01 |
| SkyReels V2 T2V | 3.14 | 3.14 | — | — | — |
| SkyReels V2 DF | 3.24 | — | — | — | — |
| Wan2.1 (14B) | 2.85 | — | — | — | — |
| HunyuanVideo (13B) | 2.84 | — | — | — | — |
| **Kling 1.6** | **3.40** | — | — | — | — |
| **Runway Gen-4** | **3.39** | — | — | — | — |

SkyReels V2 I2V at 3.29 places it between the leading open-source models and the best commercial offerings. Kling 1.6 leads at 3.40; SkyReels V2 sits 0.11 points behind while being fully open-source.

**Motion quality at 3.01** is the model's weakest dimension — the reinforcement learning stage improved it substantially from baselines, but it remains below the commercial leaders.

---

## License

SkyReels V2 uses the **Skywork License** — a custom license developed by Kunlun/Skywork AI for its model releases. Key points:

- Commercial use is explicitly permitted
- Weights and code are publicly available
- This is **not** an OSI-standard license (not MIT, Apache 2.0, CC-BY, etc.)
- Developers should read the full license at the GitHub repository before production deployment

The code repository also cites **Creative Commons BY-4.0** for the paper documentation. For production commercial use, consulting the full Skywork License text is advised.

---

## Ecosystem

**GitHub**: github.com/SkyworkAI/SkyReels-V2 — approximately 6,900 stars at time of writing, with ~1,500 forks. Strong early traction for an open-source video model.

**HuggingFace**: Full model collection at `Skywork/skyreels-v2-6801b1b93df627d441d0d0d9`. Individual models: `Skywork/SkyReels-V2-I2V-1.3B-540P`, `Skywork/SkyReels-V2-DF-1.3B-540P`, and 14B equivalents. Also mirrored on ModelScope.

**HuggingFace Diffusers**: Official SkyReels V2 pipeline integrated into the Diffusers library, documented at `huggingface.co/docs/diffusers/api/pipelines/skyreels_v2`. This is one of the clearest signals of ecosystem legitimacy — Diffusers pipelines have a review bar and are maintained alongside the library.

**ComfyUI**: Available through **ComfyUI-WanVideoWrapper** by kijai (the same wrapper used for Wan2.1). SkyReels V2 model weights ship in kijai's HuggingFace repository alongside WanVideo weights (`Wan2_1-SkyReels-V2-DF-1_3B-540P_fp32.safetensors`). GitHub issue #481 tracks SkyReels V2 workflow changes. Community workflows exist on OpenArt, Civitai, and RunningHub. GGUF quantized variants further reduce VRAM requirements for ComfyUI users.

**SwarmUI**: Also documented as supporting SkyReels V2.

**HuggingFace Spaces**: Multiple community demonstration spaces launched immediately after release (fffiloni, bekimoon, svjack, Kingrane).

**MCP server**: No MCP server wrapping SkyReels V2 has been published in any MCP registry or on GitHub as of this writing. This is an unfilled gap — PiAPI offers a third-party API for SkyReels (V1/V2) but no MCP wrapper has been built on top of it.

---

## Hosted Platform: SkyReels.ai

For users who cannot run the model locally, Skywork AI operates a hosted SaaS product at **skyreels.ai** (website.skyreels.ai):

- **Free tier**: 300 credits on signup (7-day expiry), plus 50 credits/day
- **Standard plan**: ~$28/month, approximately 1,000 credits
- **Pro plan**: Higher tier for production use

The hosted platform adds features not present in the open-source weights: **audio** (voice, music, SFX), **lip sync**, and higher throughput. The open-source weights themselves have no audio capability.

**Third-party API**: PiAPI (piapi.ai) offers pay-as-you-go API access to SkyReels, with free credits on signup. This is a community route, not an official Skywork API.

---

## How SkyReels V2 Compares to Kling

Since these models are routinely confused as being from the same company, a direct comparison is instructive precisely because they represent opposite design philosophies:

| Dimension | SkyReels V2 (Kunlun/Skywork) | Kling (Kuaishou) |
|-----------|-------------------------------|------------------|
| Maker | Kunlun Wanwei / Skywork AI | Kuaishou Technology |
| Model access | Open-source (weights + code) | Closed / API only |
| License | Skywork custom (commercial OK) | Proprietary |
| Max resolution | 720P | Up to 4K (Kling 3.0) |
| Max duration | ~60s demonstrated; theoretically unlimited | 15 seconds (single clip) |
| Frame rate | 24 FPS | 30 FPS |
| Human eval score | 3.29 (I2V) | 3.40 (Kling 1.6) |
| Audio | Hosted platform only | Native audio, voice cloning |
| Self-hosting | Yes (14.7–51GB VRAM) | No |
| Cost | Free self-host; $28/mo SaaS | ~$0.084–$0.112/sec via API |
| Positioning | Research open model for developers | Consumer/creator commercial SaaS |

Kling wins on resolution (4K vs 720P), motion quality, audio, and overall human evaluation score. SkyReels V2 wins on openness, cost for self-hosted workloads, duration (genuine infinite-length vs. 15-second clips), and accessibility for developers who want to modify and extend the model.

---

## Limitations

**Hardware wall for the 14B model**: At ~51GB VRAM, the full-quality 14B requires an A100-80G or H100. Most developers and creators are limited to the 1.3B model (14.7GB) or GGUF quantizations, which both sacrifice some quality. The 5B model — which would serve the RTX 4090/mid-tier professional user — was not available at launch.

**Motion artifacts in Diffusion Forcing async mode**: The unlimited-length generation capability works via block-by-block autoregression, but frame-transition artifacts appear at block boundaries. The longer the video, the more block transitions, and the more visible the artifact accumulation. GitHub issue #90 documents this.

**Motion quality**: The lowest human-evaluated dimension at 3.01/5. Reinforcement learning improved it, but it trails the commercial leaders.

**No audio in open weights**: Audio is a hosted-platform-only feature. Open-source deployments produce silent video.

**720P limited**: Currently only available for I2V 14B. T2V at 720P was not part of the initial weight release.

**Custom license**: Not a standard OSI license. Requires review before production deployment.

**Steep prompt engineering curve**: The model is specifically trained on cinematographic caption vocabulary. General-purpose natural-language prompts underperform compared to structured prompts using shot-type, camera motion, and expression directives.

---

## Rating: 4 / 5

SkyReels V2 is the strongest open-source image-to-video model to have shipped as of its release date — and it isn't close. At 3.29 human evaluation score, it sits within 0.11 points of Kling 1.6 (3.40) and Runway Gen-4 (3.39) while being fully open-source, self-hostable, and commercially licensed.

The Diffusion Forcing framework is a genuine technical innovation, not a marketing claim. Generating 60-second coherent video in a single session — from an open-source model — is a meaningful capability advance. VBench 83.9% outperforms both HunyuanVideo-13B and Wan2.1-14B on all dimensions. The Diffusers integration signals ecosystem maturity.

The rating stops short of 5 because of concrete friction points: the 14B model's 51GB VRAM requirement excludes most users from the full-quality tier; the missing 5B left a hardware gap at launch; motion artifacts in Diffusion Forcing async mode are documented; audio requires the hosted platform; and the custom Skywork License — while commercial-friendly — isn't the MIT or Apache 2.0 that developers recognize on sight.

For an open-source developer or researcher who wants the best available image-to-video model they can actually modify and deploy: SkyReels V2 is the current answer.

---

*SkyReels V2 paper: arXiv 2504.13074. GitHub: github.com/SkyworkAI/SkyReels-V2. HuggingFace collection: Skywork/skyreels-v2-6801b1b93df627d441d0d0d9. Hosted platform: skyreels.ai. This review is research-based. We do not test AI tools hands-on.*

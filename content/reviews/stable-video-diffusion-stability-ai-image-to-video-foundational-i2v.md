---
title: "Stable Video Diffusion Review — Stability AI's Foundational I2V Model: SVD, SVD-XT, and the Birth of Open-Source Image-to-Video"
date: 2026-05-11
description: "Stable Video Diffusion (SVD) by Stability AI was the first widely accessible open-source image-to-video model, released November 2023. Built on SD 2.1's U-Net with temporal attention layers, SVD generates 14 frames; SVD-XT extends to 25 frames (~4 seconds at 6 FPS) at 576×1024. Minimum 8 GB VRAM, comfortable at 24 GB. API deprecated July 2025. Superseded by Wan 2.1 and HunyuanVideo for quality, but still used in low-VRAM workflows. No MCP server. Rating 3/5."
tags: ["video-ai", "image-to-video", "ai-video-generation", "stable-video-diffusion", "stability-ai", "open-source", "comfyui", "diffusion-model", "unet", "creative-ai", "i2v"]
rating: 3
---

# Stable Video Diffusion — The Model That Started Open-Source Image-to-Video

There was a moment in late November 2023 when open-source AI video generation changed permanently. Until that point, converting a still image into a short animated clip required either access to expensive proprietary APIs or cobbled-together frame interpolation hacks that produced stiff, unconvincing motion. Then Stability AI released **Stable Video Diffusion** — a 1.5-billion-parameter image-to-video model trained on hundreds of millions of video clips — and suddenly any researcher, artist, or developer with a 16 GB GPU could animate a photo.

SVD is no longer the state of the art. Stability AI's own API was deprecated in July 2025. The models that replaced it — Wan 2.1, HunyuanVideo-I2V, CogVideoX — produce substantially longer, higher-quality, more controllable video. But understanding SVD matters if you want to understand where open-source I2V came from, why certain architectural decisions persist in newer models, and what "good enough" can mean when your GPU has 8 GB of VRAM rather than 80.

This review covers SVD and SVD-XT as of May 2026. We write from public sources — the arXiv paper, HuggingFace model cards, GitHub, community documentation. We do not test AI video models hands-on.

---

## Background: Stability AI and the SVD Paper

**Stability AI** is a UK-based AI company most known for Stable Diffusion, the open-source image generation model that launched in August 2022 and catalyzed the modern AI art movement. SVD was released as a research preview on **November 21, 2023**, accompanied by the paper *"Stable Video Diffusion: Scaling Latent Video Diffusion Models to Large Datasets"* (arXiv: 2311.15127, submitted November 25, 2023).

The paper's core contribution was not just the model — it was the systematic study of **data curation** for video generation. The authors argue, convincingly, that the training data pipeline matters more than architectural choices for video quality. Their Large Video Dataset (LVD) and the curation filters they developed became a reference point for subsequent open-source video model research.

SVD was not Stability AI's first video attempt — an earlier product called **Stable Video** existed as a web demo — but it was their first model release with downloadable weights and a clear technical methodology. That openness mattered enormously to the research community.

---

## Architecture: U-Net with Temporal Layers

SVD is built atop **Stable Diffusion 2.1** — a U-Net based image model, not a Diffusion Transformer. The core architectural extension adds **temporal convolution and attention layers** inserted after each spatial layer in the U-Net, giving the model a hybrid spatial+temporal processing structure.

The specific components:
- Each spatial ResNet block is paired with a **temporal ResNet layer**
- Each spatial transformer block is paired with a **temporal attention block**
- Temporal attention operates with full self-attention across the frame dimension
- The 2D spatial autoencoder from SD 2.1 is applied per-frame; temporal compression is handled by the denoiser, not the VAE

**Total parameters**: approximately **1.52 billion**, of which roughly **656 million** are temporal-specific. The remaining 864M are inherited from SD 2.1's spatial layers.

The model uses **EDM-based noise scheduling** (Karras et al., 2022) rather than the DDPM-style scheduling used in earlier Stable Diffusion models. This enabled more stable fine-tuning at 576×1024 resolution.

Three inference conditioning signals beyond the input image:
1. **Frames per second (FPS)**: An integer input that conditions the motion speed; the model was trained with FPS ranging from 1 to 30
2. **Motion bucket ID**: An integer from 1–255 controlling motion intensity; higher values produce more motion, lower values produce near-static output
3. **Augmentation noise**: A small amount of noise added to the conditioning image, helping with generalization to images outside the training distribution

This is entirely image-conditioned. **SVD has no text input**. There is no text prompt, no caption, no style descriptor. The model extracts visual semantics from the conditioning image and generates motion consistent with what it learned during training. This is a significant limitation compared to every major I2V model released after 2024.

### Why U-Net, Not DiT?

SVD predates the shift to Diffusion Transformer architectures that characterizes the 2024–2025 generation of video models. HunyuanVideo (Tencent, December 2024), Wan 2.1 (Alibaba, February 2025), CogVideoX (Zhipu AI, August 2024) — all DiT-based. The DiT architecture scales more efficiently with parameters and training compute, handles long-range temporal dependencies better, and generalizes to longer video more naturally.

SVD's U-Net heritage is both its limitation and, oddly, part of its practical value: U-Net inference on smaller GPUs is well-understood, heavily optimized, and benefits from years of Stable Diffusion tooling. Running SVD-XT on 12 GB VRAM is straightforward. Running HunyuanVideo at equivalent quality requires 60–80 GB.

---

## Training Data: LVD and the Case for Curation

The paper's most cited contribution is the **Large Video Dataset (LVD)** and the staged curation approach used to build it.

**Starting point**: 580 million annotated video clip-caption pairs from publicly available internet sources.

**Systematic curation pipeline** applied in stages:
1. **Motion filtering via optical flow score** — clips with near-zero flow (static scenes, slideshows) removed
2. **OCR filtering** — clips dominated by text overlays removed
3. **Synthetic detection** — stock footage watermarks and artificial motion artifacts flagged
4. **CLIP-based aesthetic scoring** — low-aesthetic content filtered
5. **Scene cut detection** — multi-scene clips split into single-scene segments

After curation: **152 million clips** (the "LVD-F" dataset) — approximately 26% of the original.

Final fine-tuning dataset: approximately **250,000 high-quality clips** at 576×1024 resolution, representing the highest-aesthetic, highest-motion, most visually coherent subset of LVD-F.

**Three-stage training**:
1. Image generation pre-training (standard SD 2.1 initialization)
2. Video pre-training on LVD-F (152M clips, low resolution)
3. Video fine-tuning on 250K high-quality clips (576×1024)

The paper demonstrates empirically that Stage 3 fine-tuning quality depends heavily on Stage 2 quality — models that were pre-trained on low-quality data degraded even with high-quality fine-tuning. This "garbage in" problem is one reason video model training is more sensitive to data than image model training.

---

## Model Variants

### SVD (stable-video-diffusion-img2vid)

The base release: **14 frames** at 576×1024 resolution. With default 6 FPS conditioning, this produces approximately 2.3 seconds of video. FPS conditioning allows up to ~30 FPS for faster apparent motion.

- HuggingFace: `stabilityai/stable-video-diffusion-img2vid`
- Released: November 21, 2023
- Generation time: ~100 seconds on A100 80GB

### SVD-XT (stable-video-diffusion-img2vid-xt)

Fine-tuned SVD for **25-frame generation** — same architecture, same resolution, but trained specifically for extended output. At 6 FPS this produces approximately 4.2 seconds. The quality and motion consistency improvements in SVD-XT over SVD are visible, particularly for complex scenes.

- HuggingFace: `stabilityai/stable-video-diffusion-img2vid-xt`
- Released alongside SVD (November 21, 2023)
- Generation time: ~180 seconds on A100 80GB

### SVD-XT 1.1 (stable-video-diffusion-img2vid-xt-1-1)

Fine-tuned SVD-XT for improved consistency at **fixed 6 FPS and Motion Bucket ID 127**. The 1.1 update reduces temporal flickering and improves perceptual consistency between frames, especially for faces and structured objects.

- HuggingFace: `stabilityai/stable-video-diffusion-img2vid-xt-1-1`
- Released: February 2024
- **This is the recommended variant** for most workflows — it produces the most stable output

A TensorRT-optimized variant (`stabilityai/stable-video-diffusion-img2vid-xt-1-1-tensorrt`) exists for inference acceleration on NVIDIA GPUs.

---

## Performance and Output Quality

### Resolution

Fixed at **576×1024** (portrait) or **1024×576** (landscape). No variable resolution. No upscaling built in. If your input image has a different aspect ratio, it will be cropped or letterboxed.

### Frame Count

- SVD: 14 frames (~2.3 sec at 6 FPS)
- SVD-XT / 1.1: 25 frames (~4.2 sec at 6 FPS)

No built-in extension beyond 25 frames. Community approaches exist (sliding window inference, frame blending) but require custom workflows and introduce consistency artifacts.

### What SVD Handles Well

- **Slow motion and subtle animation**: Hair movement, fabric rippling, water surfaces, breathing, candle flame — SVD's temporal layers learned this class of motion very well
- **Camera pan and zoom effects**: Consistent with the model's training on cinematic footage
- **Product and landscape photography**: Clean input images with clear foreground/background separation produce the best results
- **Stylized and illustrated images**: SVD generalizes surprisingly well to non-photographic input — paintings, illustrations, and AI-generated images often animate cleanly

### What SVD Handles Poorly

- **Fast or large motion**: Running characters, rapid gestures, explosions — temporal coherence breaks
- **Human faces**: Notable artifacts; faces morph, drift, or deform under the temporal layers
- **Text and logos**: No legible text rendering; any text in the input image degrades or distorts
- **Complex scene changes**: Multi-element scenes with independent moving objects produce conflicting motion artifacts
- **Long clips**: The 25-frame ceiling means anything requiring extended narrative is beyond SVD's reach

---

## VRAM Requirements

One of SVD's practical advantages over later models is its modest GPU requirements:

| Configuration | VRAM | Notes |
|---------------|------|-------|
| Minimum (optimized) | ~8 GB | model CPU offload + decode_chunk_size=1; slow, flickering artifacts |
| Comfortable | 16 GB | Standard inference, some chunking; RTX 3080/4080 class |
| Recommended | 24 GB+ | Full 25-frame generation without chunking; RTX 3090/4090, A5000 |
| Optimal (no memory constraints) | 40–80 GB | A100/H100; full batch generation |

The HuggingFace Diffusers library implements SVD with full support for CPU offload, attention slicing, feed-forward chunking, and configurable `decode_chunk_size` — all of which trade speed for memory. A 12 GB GPU (RTX 3080) is a practical sweet spot: enough to avoid the worst chunking artifacts at reasonable speed.

**Comparison to modern I2V models**:
- **Wan 2.1 I2V**: 480p requires ~8 GB (1.3B model) or ~16 GB (14B); 720p requires 24 GB+
- **HunyuanVideo-I2V**: 60–80 GB for full 720p
- **CogVideoX 5B**: ~24 GB VRAM

SVD remains the most accessible I2V model for low-VRAM inference by a significant margin, though Wan 2.1's 1.3B variant is increasingly competitive in this tier.

---

## GitHub and Licensing

SVD's code lives in the umbrella **`Stability-AI/generative-models`** repository alongside SDXL, SD3, and other Stability AI models. The repo uses a monorepo structure with model-specific configurations rather than separate SVD-dedicated codebase.

The repository has substantial star count (the exact current figure varies, but `Stability-AI/generative-models` is one of Stability AI's most-starred repositories, likely in the 10,000–20,000 range).

**License**: **Stability AI Community License**
- Free for non-commercial / research use
- Commercial use requires a paid membership or commercial license agreement with Stability AI
- This is more restrictive than Apache 2.0 and distinguishes SVD from models like HunyuanVideo, Open-Sora 2.0, or CogVideoX-2B (all Apache 2.0) that allow unrestricted commercial use of model weights

The commercial licensing restriction has been a persistent friction point for developers building products. Given the API deprecation in July 2025, the practical path to commercial SVD deployment now runs through self-hosting with a commercial license, which requires direct engagement with Stability AI.

---

## HuggingFace

All SVD variants are hosted at `stabilityai/` on HuggingFace:
- `stabilityai/stable-video-diffusion-img2vid`
- `stabilityai/stable-video-diffusion-img2vid-xt`
- `stabilityai/stable-video-diffusion-img2vid-xt-1-1`
- `stabilityai/stable-video-diffusion-img2vid-xt-1-1-tensorrt`

Models require accepting a license agreement before download — this gates the visible download counter. The HuggingFace Diffusers documentation includes a dedicated [SVD usage guide](https://huggingface.co/docs/diffusers/using-diffusers/svd) covering pipeline setup, VRAM optimization, and video export.

---

## ComfyUI Integration

SVD has deep ComfyUI support via two routes:

**Native ComfyUI nodes**: SVD is supported natively in ComfyUI via built-in `VideoModelLoader` and sampler nodes — no extension required for basic workflows. This was one of the first video models to receive native ComfyUI support, which drove significant community adoption.

**Community extension**: [ComfyUI-Stable-Video-Diffusion](https://github.com/thecooltechguy/ComfyUI-Stable-Video-Diffusion) by `thecooltechguy` provides dedicated nodes:
- `SVDModelLoader`
- `SVDSampler`
- `SVDDecoder`
- `SVDSimpleImg2Vid`

Installable via ComfyUI Manager. Active workflow libraries exist on Civitai and community repositories.

**Popular SVD workflows include:**
- **SVD + FreeU**: Enhanced motion coherence via frequency-domain enhancement
- **Two-stage SDXL→SVD**: Generate image with SDXL, animate with SVD (effectively text-to-video via chaining)
- **Looping animation**: Extract first and last frames to create seamless loops
- **SVD + upscaler**: Post-process 576×1024 output through ESRGAN or similar for higher resolution delivery

The ComfyUI ecosystem around SVD remains active despite the API deprecation — the community workflows run from local weights and don't depend on Stability AI's commercial infrastructure.

---

## Hosted Inference — Deprecated

Stability AI's developer API previously offered SVD video generation as a paid endpoint. That API was **deprecated on July 24, 2025**, with Stability AI directing users toward their image generation products (Stable Image Core, Stable Image Ultra, and SD 3.5-based APIs). There is no replacement video API from Stability AI.

Remaining hosted options as of May 2026:
- **Third-party services**: ModelsLab and similar services have offered SVD endpoints at $0.05–$0.20 per video clip; availability varies
- **NVIDIA NIM**: SVD was available via NVIDIA's NIM inference platform (`build.nvidia.com/stabilityai/stable-video-diffusion`); current availability should be verified directly
- **Self-hosting**: The recommended path — download weights from HuggingFace, run via Diffusers or ComfyUI

For teams building video generation features, the API deprecation means SVD is no longer a viable cloud-hosted option without third-party dependency.

---

## MCP Server Availability

No MCP server exists specifically for SVD video generation. There are several MCP servers for Stable Diffusion *image* generation, including:
- `tadasant/mcp-server-stability-ai` — Node.js wrapper for the Stability AI REST API (image endpoints)
- `mkm29/stablemcp` — simple SD image generation
- `boxi-rgb/sd-webui-mcp` — connects Claude Desktop to local AUTOMATIC1111/Forge WebUI

None target SVD video generation. The July 2025 API deprecation makes API-based SVD MCP integration non-viable. A local ComfyUI MCP server could theoretically route SVD workflows, but no purpose-built SVD video MCP server is publicly available as of this writing.

---

## Current Status and Community Use (May 2026)

SVD is **no longer actively developed by Stability AI**. The API is deprecated. No updates have been made to the model weights since SVD-XT 1.1 in February 2024 — over two years of maintenance-free existence. Stability AI's own video focus has shifted to **Stable Virtual Camera** (generative view synthesis for 3D scenes) and other research directions.

In competitive terms, the gap between SVD and current generation I2V models is substantial:

| Model | Release | Max Length | Text Input | License | Competitive Position (2026) |
|-------|---------|-----------|------------|---------|---------------------------|
| SVD-XT 1.1 | Feb 2024 | 4 sec | No | SA Community | Legacy |
| CogVideoX 5B | Aug 2024 | 10 sec | Yes | Apache 2.0 | Active |
| HunyuanVideo-I2V | Dec 2024 | 13 sec | Yes | Tencent Video | Leading |
| Wan 2.1 I2V | Feb 2025 | 15 sec | Yes | Apache 2.0 | Leading |
| SkyReels V2 I2V | Mar 2025 | Extended | Yes | Apache 2.0 | Leading |

SVD sits at the bottom of that table on almost every dimension except VRAM efficiency. But it remains in active community use in specific contexts:

**Where SVD still gets used in 2026:**
- Artists on GPUs with 8–16 GB VRAM who cannot run larger models
- Rapid preview generation when iteration speed matters more than clip quality
- Established ComfyUI workflows that haven't been updated to newer I2V nodes
- Fine-tuning experiments — SVD's smaller parameter count makes it faster to fine-tune than 5B+ models
- Historical/research reference for understanding I2V diffusion architecture

**Where SVD should not be used:**
- Production video applications requiring quality or length
- Workflows requiring text-driven video generation
- Commercial applications requiring clear open-source licensing
- Any use case where API hosting is required (deprecated)

---

## Historical Significance

Assessing SVD purely on current technical benchmarks undersells what it accomplished. When SVD released in November 2023, it was the first time a researcher or artist could:

1. Download a pretrained model from HuggingFace
2. Load it in Diffusers with five lines of Python
3. Pass in a photo
4. Receive back a plausible animated clip

That sounds obvious now. It wasn't. Prior to SVD, open-source video generation was either text-to-video (with poor image adherence) or frame interpolation between keyframes (with no understanding of scene content). SVD's image conditioning approach — using the input image as a semantic anchor while temporal layers hallucinated motion — was the paradigm that every I2V model since has refined and extended.

The Large Video Dataset curation methodology also contributed to the field. The staged curation approach (optical flow → aesthetic scoring → quality fine-tuning) influenced how teams at Wan (Alibaba), Open-Sora (HPC-AI Tech), and others structured their training data pipelines.

SVD didn't win the race. But it started it.

---

## Rating: 3/5

**What earns its rating:**
- Genuinely foundational contribution — first accessible open-source I2V model
- Lowest VRAM floor of any capable I2V model (8 GB usable, 16 GB comfortable)
- Deep ComfyUI integration with active community workflows
- Comprehensive data curation methodology documented in the paper
- Well-maintained HuggingFace weights with good Diffusers support

**What holds it back:**
- 25-frame / ~4-second hard ceiling
- No text input — strictly image-conditioned
- U-Net architecture outclassed by modern DiT models at equivalent quality
- API fully deprecated as of July 2025 — no cloud path without third-party services
- Stability AI Community License is more restrictive than Apache 2.0 alternatives
- Significant face/human quality issues that newer models handle much better
- No updates since February 2024 — two-plus years of stasis

**Who should consider SVD:**
- Researchers studying foundational I2V architecture and the shift from image to video generation
- Artists on 8–16 GB GPUs who want capable animation without cloud costs
- ComfyUI power users with established SVD workflows they haven't migrated
- Anyone doing fine-tuning experiments where a smaller, well-understood model is preferable to 5B+ alternatives

**Who should look elsewhere:**
- Teams building production video workflows — use Wan 2.1 I2V or HunyuanVideo-I2V
- Developers needing a text-conditioned I2V model — every major alternative supports text prompts
- Commercial deployments requiring clear Apache 2.0 licensing
- Anyone who needs more than 4 seconds of coherent video

SVD is the ancestor of modern open-source I2V. It deserves respect, study, and occasional practical use — but it is not the right choice for new production work in 2026.

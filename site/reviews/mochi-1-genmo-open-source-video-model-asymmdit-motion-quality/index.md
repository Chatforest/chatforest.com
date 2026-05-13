# Mochi 1 Review — Genmo's 10B Open-Source Video Model and the AsymmDiT Architecture That Proved Motion Quality Was Solvable

> Mochi 1 (Genmo, October 2024) is a 10-billion-parameter open-source text-to-video model built on AsymmDiT — an asymmetric multimodal diffusion transformer that allocates 4× more parameters to visual than text processing. At release it was the largest open video model ever, and it set the community benchmark for smooth, physically coherent motion in fluid dynamics, hair, cloth, and human movement. Apache 2.0. 480p, 30 fps. Rating: 4/5.


# Mochi 1 — The Open-Source Video Model That Set the Motion Quality Bar

By October 2024, the open-source AI video generation space had developed a credibility problem around motion. Most models could generate visually plausible frames, but temporal coherence — the sense that objects in a scene actually exist in a physical world and move consistently through time — remained elusive. Water looked like a texture applied to a surface rather than a fluid. Hair moved in ways that were statistically reasonable frame-to-frame but physically nonsensical over a full clip. Human figures drifted between poses rather than actually walking. The difference between "a sequence of frames that looks like motion" and "a video of something actually moving" was still the gap between open-source and the commercial leaders.

**Mochi 1**, released by Genmo on October 22, 2024, was the open-source model that most directly attacked that gap. Not through better resolution or faster inference or more features, but by training a 10-billion-parameter model specifically oriented toward the physics of motion — and then releasing it under Apache 2.0, making it freely usable by anyone with sufficient hardware.

It did not surpass every commercial model on every metric. It was never fast. The 480p resolution ceiling was a real limitation from day one. It lacked image-to-video support and never published a formal technical paper. But for smooth, temporally coherent motion in fluids, cloth, and human movement, Mochi 1 was — for a brief window — the best open-source option in existence, and its AsymmDiT architecture introduced ideas that subsequent models built upon.

This review covers Mochi 1 (preview release) as it stood at launch and in the months following. We write from public sources — the Genmo blog, GitHub, HuggingFace, community documentation, and coverage in the AI press. We do not test AI video models hands-on.

---

## Background: Genmo and the Scale-Versus-Accessibility Bet

Genmo was founded in 2022 in San Francisco by **Paras Jain** and **Ajay Jain** — brothers who both hold PhDs from UC Berkeley. Their doctoral work was conducted alongside researchers including Ion Stoica, Joey Gonzalez, and Pieter Abbeel, all of whom became Genmo advisors. Ajay Jain co-authored a 2020 foundational paper on diffusion models while at Google Brain; Paras Jain specialized in scalable systems for creative AI tools.

The company raised approximately $28–30 million in a Series A led by New Enterprise Associates (NEA), with participation from The House Fund, Gold House Ventures, WndrCo, and others, announced in early 2024.

Genmo's stated mission is to "put a tiny filmmaker in the pockets of a billion people" — placing them squarely in the consumer-accessibility camp rather than the enterprise API camp. Before Mochi 1, they operated a creative platform offering image animation, video generation, and 3D generation from text prompts. Mochi 1 was their pivot to foundational model development: a research lab bet that releasing a frontier-scale model as open weights would build the credibility and community that a proprietary API could not.

The timing mattered. October 2024 was a dense month for open-source video releases. CogVideoX had shipped in August. LTX-Video from Lightricks was arriving in the same general window. HunyuanVideo would follow in November. The late-2024 cluster of open releases collectively closed a significant gap between open-source and commercial video generation systems — and Mochi 1 was a central part of that story.

---

## The Core Claim: Scale and Motion Quality Together

Genmo's blog post accompanying the Mochi 1 release made two headline claims.

First: Mochi 1 was, at release, "the largest video generative model ever openly released" — 10 billion parameters in the transformer backbone alone, trained from scratch (not fine-tuned from an image foundation model). For context, CogVideoX was approximately 5B parameters; the open-source video landscape before late 2024 had not seen a 10B model released under a permissive license.

Second: Mochi 1 achieved the highest motion quality scores in their internal Elo-style benchmark, including a **motion quality Elo of 1147.51** and **prompt adherence score of 79.38**, outscoring Luma Dream Machine and Runway Gen-3 on those internal metrics. These are Genmo's own benchmarks, not independent evaluations — but the community largely confirmed the motion quality assessment in practice. The prompt adherence score was independently notable: Mochi 1's long-context T5-XXL text encoder and 256-token limit gave it genuine capacity to follow complex, multi-clause prompts.

The motion quality claims held up. In fluid simulation — water, liquid, smoke — Mochi 1 generated physics-coherent motion that competitors often failed on. In hair and fur simulation, the temporal coherence was markedly better than contemporaries. In human motion, the model produced natural walking, gestures, and movement rather than the "sliding" artifacts common in earlier architectures. This was not a subjective impression; users across communities confirmed these characteristics consistently.

What Genmo sacrificed for scale and quality: resolution (480p maximum, not the 720p+ that HunyuanVideo achieved), speed (2–20 minutes per clip depending on hardware, vs. 5–10 seconds for LTX-Video), and modality breadth (text-to-video only, no image-to-video at launch).

---

## Architecture: AsymmDiT — The Asymmetric Multimodal Transformer

The core architectural contribution of Mochi 1 is **AsymmDiT**: an Asymmetric Diffusion Transformer designed specifically for the different parameter requirements of visual and text modalities in joint attention.

### The Asymmetry

Standard multimodal diffusion transformers — including SD3's MMDiT — use symmetric architectures: text and visual tokens attend to each other, but each stream gets roughly equal parameter allocation. The insight behind AsymmDiT is that this symmetry is the wrong prior. Visual generation requires far more representational capacity than text processing. A video model must track the appearance, position, motion, and texture of every object across every frame. The text prompt, while important for conditioning, is a compact, fixed-length input that does not require the same neural depth.

AsymmDiT addresses this directly: the visual stream receives **nearly 4× more parameters** than the text stream, achieved by giving each modality a different hidden dimension:

- **Visual hidden dimension:** 3072
- **Text hidden dimension:** 1536
- **Layers:** 48
- **Attention heads:** 24
- **Visual token count:** 44,520
- **Text token count:** 256 (max)

This is not simply a wider model — the asymmetry is structural. The feedforward (MLP) layers for each modality are separate, allowing each stream to develop specialized representations. The attention mechanism unifies both streams through **non-square QKV and output projection layers** that bridge the different hidden dimensions — text and visual tokens attend to each other in a shared attention space, but are processed through different MLP pathways.

The result is that the model can concentrate its parameters on the visual reasoning task — understanding how 44,520 tokens representing a video clip relate to each other across space and time — without allocating equivalent compute to the 256 text tokens that are, by comparison, a much simpler representation.

### Positional Encoding

Mochi 1 uses **Rotary Positional Embeddings (RoPE)** extended to three dimensions — height, width, and time — with learnable mixing frequencies that allow the model to separately tune how it represents spatial versus temporal position. This is important for video generation: the relationship between frame 1 and frame 2 in time is different from the relationship between pixel (0, 0) and pixel (0, 1) in space, and the positional encoding needs to reflect that asymmetry.

Additional training stabilization comes from **SwiGLU** feedforward layers, **query-key normalization (QK-norm)** to prevent attention entropy collapse, and **sandwich normalization** for controlling activation magnitudes across the deep 48-layer network.

### Text Encoder

Mochi 1 uses a single text encoder: **T5-XXL**. This is consistent with other large video models (LTX-Video, Wan 2.1, CogVideoX also use T5-XXL), chosen for its ability to encode long, detailed prompts. Unlike SD3, which combines CLIP and T5, Mochi 1 is T5-only — simpler conditioning pipeline, and the model relies entirely on T5's language understanding for prompt following. The 256-token text limit is generous for practical use; most prompts fit comfortably, and even detailed multi-clause descriptions rarely approach the ceiling.

### No Published Paper

Despite promising one in the launch blog post, Genmo has not released a formal arXiv preprint for Mochi 1 as of available sources through 2025–2026. This limits the reproducibility and academic engagement that comparable models like CogVideoX achieved through technical reports. Researchers working from Mochi 1 have primarily used the GitHub README, blog post, and the model weights themselves.

---

## AsymmVAE: The Other Open Contribution

Alongside the transformer, Genmo released **AsymmVAE** — a 362-million-parameter causal video VAE that is itself a notable open-source contribution.

The VAE achieves:

- **Spatial compression:** 8× horizontal and vertical (64× total spatial)
- **Temporal compression:** 6×
- **Latent channels:** 12 (vs. the standard 4 or 8 in image VAEs)
- **Architecture:** Asymmetric encoder-decoder — the encoder uses a base channel width of 64, the decoder uses 128. The decoder has greater capacity to reconstruct fine detail from the compressed latent.

The "causal" in AsymmVAE refers to temporal causality: the VAE processes frames in causal order, allowing streaming and incremental decoding in principle. This is architecturally distinct from models that process all frames simultaneously, and enables potential future applications in real-time or interactive generation pipelines.

AsymmVAE's compression ratio sits between standard video VAEs. LTX-Video's VAE achieves 1:192 total compression (32× spatial + 8× temporal), which is dramatically more aggressive. AsymmVAE's 64× spatial × 6× temporal = roughly 96× raw pixel count reduction (with 12-channel output vs. 3-channel RGB) is meaningful but conservative by comparison — prioritizing reconstruction quality over compression efficiency.

The VAE was released as a standalone download alongside the main model, allowing researchers to use it independently for other video modeling work.

---

## What Mochi 1 Is Good At: Motion Quality in Practice

The community's experience with Mochi 1 was consistent with Genmo's claims on motion quality. The model's specific strengths:

### Fluid Dynamics

Water, smoke, liquid, and gas simulations are where Mochi 1's temporal coherence advantage was most visible and most consistent. Competing models from the same era frequently produced water that shimmered with texture artifacts or moved with unrealistic periodicity. Mochi 1 generated fluid motion with physical plausibility that held up across the full clip duration.

### Hair and Fur

Hair and fur are notoriously difficult for video models because individual strand behavior is high-frequency, locally coherent, and globally constrained by physics. Most models sacrifice either local detail or global consistency. Mochi 1 held both better than its contemporaries, producing hair that moved naturally without the "painted-on" texture motion that characterized earlier approaches.

### Cloth and Fabric

Similar logic applies to cloth — wrinkles, folds, and drape dynamics require the model to understand both local deformation and global structure. Community evaluations consistently rated Mochi 1 above contemporaries on fabric motion.

### Human Movement

Walking, gesturing, and body movement were more natural in Mochi 1 than in same-era competitors at lower parameter counts. The model avoided the "rubber limb" effect — where joints bend non-physically — more consistently than CogVideoX or LTX-Video at their respective 2024 release qualities.

### Prompt Adherence

The T5-XXL encoder and 256-token limit gave Mochi 1 genuine capacity to follow complex prompts. The community noted that detailed descriptions of camera angle, lighting conditions, subject behavior, and scene composition were more reliably reflected in the output than in models with shorter context windows or weaker text encoders.

---

## Output Specifications and Limitations

### Resolution: The 480p Ceiling

Mochi 1's primary output resolution is **480p (640×480)**. Genmo announced a "Mochi 1 HD" upgrade at 720p before the end of 2024; as of available sources through 2025–2026, this HD release has not shipped as open weights. The 480p cap was the single most consistently criticized aspect of the model from day one, placing it behind CogVideoX (720p capable) and LTX-Video (768×512 standard) on resolution alone.

At 480p in 2024, the output quality is visibly lower than commercial competitors. Runway Gen-3 Alpha and Kling were operating at higher resolutions. For casual viewing on screens up to 1080p, 480p is acceptable but not competitive. For professional creative applications, it is a meaningful constraint.

### Frame Rate and Duration

**30 fps**, fixed. Duration up to approximately **5.4 seconds** (~162 frames at 30 fps). The GitHub repo references common generation at 84 frames; 31 frames is a frequently used default in community workflows. Duration is broadly similar to LTX-Video (up to ~5 sec) and less than CogVideoX (up to 10 sec in later versions).

### Text-to-Video Only

Mochi 1 supports only text-to-video at the initial and primary release. Image-to-video was listed on the roadmap (Q1 2025 estimate in some sources) but not shipped as of available public records. This placed Mochi 1 behind CogVideoX and LTX-Video, both of which offered I2V capabilities, in compositing and animation workflows that require working from a reference image.

### Style Constraints

The model was trained on photorealistic video data and produces photorealistic output. Non-photorealistic styles — animation, illustration, painting, stylized art — produce degraded results. This is not unusual for large video models trained on web video corpora, but it is worth noting explicitly: Mochi 1 is not a model for stylized or artistic video generation.

---

## Hardware Requirements

### Official Recommendation

The Genmo GitHub repo officially recommends approximately **60 GB VRAM** for single-GPU inference — targeting H100 80GB or A100 80GB. This places Mochi 1 in the same hardware tier as HunyuanVideo, well above what consumer gaming GPUs offer in a single card.

### Consumer GPU Reality (ComfyUI)

The ComfyUI ecosystem significantly expanded practical accessibility. `kijai/ComfyUI-MochiWrapper` provides native ComfyUI nodes with multiple attention backends that reduce VRAM requirements:

- **bfloat16 full precision:** ~22 GB VRAM (within range of RTX 3090/4090 24GB)
- **Optimized with CPU offloading:** ~12–22 GB VRAM depending on clip length
- **RTX 4090 (24 GB) with full offloading:** workable with patience on memory management

These are not comfortable configurations — inference will be slower and require careful VRAM management — but they make Mochi 1 accessible to users who own a single high-end consumer GPU. The ComfyUI integration also provides the standard workflow benefits: node-based composition, model mixing, and community-shared workflow JSON files.

### Inference Speed

Speed is not Mochi 1's strength:

- **H100 80GB:** ~2–4 minutes for a 5-second clip
- **RTX 4090 (optimized, ComfyUI):** ~8–20 minutes for a 5-second clip
- **A100 80GB:** comparable to H100

For comparison, LTX-Video generates the same clip in approximately 5–10 seconds on an RTX 4090 — a 100× speed advantage. HunyuanVideo is roughly comparable to Mochi 1 in inference time but requires even more VRAM (60+ GB without quantization). CogVideoX sits between them.

Mochi 1 is a model for users who prioritize motion quality over iteration speed. The typical creative workflow — generate, evaluate, adjust prompt, regenerate — runs slowly when each iteration takes 10–20 minutes. Users with access to data center hardware (H100 / A100 classes) have a substantially better experience.

---

## Access and Ecosystem

### GitHub and License

**`github.com/genmoai/mochi`** — Apache 2.0. Fully permissive license covering both the code and the model weights. Personal and commercial use are permitted without restriction.

### HuggingFace

**`genmo/mochi-1-preview`** — weights in SafeTensors format. Available via the repo's download script or direct magnet link (Genmo publishes the magnet link alongside HuggingFace to reduce central download dependency). The T5-XXL text encoder is downloaded separately.

### ComfyUI

**`github.com/kijai/ComfyUI-MochiWrapper`** — the primary community integration. Supports multiple attention backends, VRAM optimization, and community-shared workflow files. Tutorials and example outputs are documented on Civitai, Stable Diffusion Art, and comfy.org. ComfyUI was the main access path for users without H100-class hardware.

### Replicate

Available at `replicate.com/genmoai/mochi-1` — approximately $0.42 per run. For users who want cloud inference without managing weights, Replicate provides a cost-effective option for occasional generation without provisioning GPU infrastructure.

### Hosted Demo

Genmo's own **`genmo.com/play`** offers browser-based access to Mochi 1 (and their platform's other tools), free with rate limiting. This was the lowest-friction entry point for experimentation.

### LoRA Fine-tuning

Fine-tuning is technically supported but requires H100 or A100 80GB class hardware — putting it out of reach for consumer GPU users. Community fine-tunes are rare for this reason; most creative users work with the base model and prompt engineering rather than custom fine-tunes.

---

## Historical Context: The Late-2024 Open Video Wave

Mochi 1 arrived in a dense cluster of significant releases:

- **August 2024:** CogVideoX — Zhipu/Tsinghua; solid quality, 5B params, I2V support
- **October 2024:** Mochi 1 — Genmo; 10B params, motion quality leader, T2V only
- **October/November 2024:** LTX-Video — Lightricks; 2B params, 100× faster, I2V support
- **November 2024:** HunyuanVideo — Tencent; highest quality, 720p+, but 60+ GB VRAM

Together, these releases collectively closed the practical quality gap between open-source and commercial video generation systems. Mochi 1's specific contributions to this moment:

**Scale proof:** Mochi 1 demonstrated that a 10B video model could be trained from scratch and released openly under Apache 2.0. Before October 2024, the open-source video landscape had not seen a 10B-parameter release. This established a new ceiling and signaled that large-scale video foundation models were not inherently restricted to well-funded commercial labs.

**AsymmDiT:** The asymmetric multimodal transformer design — concentrating parameters in the visual stream while sharing joint attention with the text stream — introduced an architectural idea that subsequent models referenced and adapted. The formal insight that text and visual modalities in a joint model do not benefit from equal parameter allocation is not obvious, and Mochi 1 made it concrete with a working implementation.

**AsymmVAE:** The 362M causal video VAE, released as a standalone artifact, gave the research community a high-quality open video encoder/decoder that could be incorporated into other projects. VAEs are foundational components; releasing a capable one openly accelerated downstream work.

**Motion quality standard:** By setting a high bar for physically coherent motion, Mochi 1 pushed the community's quality expectations upward. Models released after it were evaluated partly against the motion quality benchmark it established.

---

## Current Status and Trajectory

As of available sources through 2025–2026:

- **Mochi 1 (preview)** remains on GitHub with updates through at least September 2025. The repository is maintained.
- **Mochi 1 HD** (720p) was announced at launch but has not shipped as public open weights. Genmo continues to offer higher-quality generation through their hosted platform, suggesting internal development has continued, but the open-weight release has been delayed indefinitely.
- **Mochi 2** has not been announced. Genmo has not publicly committed to a second-generation open model release.
- In the competitive landscape, Mochi 1 has been substantially surpassed by November 2024's HunyuanVideo (overall quality, resolution) and subsequent models. For new practitioners choosing a video generation model in 2025–2026, Mochi 1 is not a primary recommendation — but it retains value as a research artifact and for its specific motion quality strengths on workflows that prioritize physics coherence over resolution or speed.

The hosted `genmo.com/play` continues to operate, and Genmo as a company continues to develop. Whether the open-source model line continues alongside the commercial product is uncertain.

---

## Comparison to Contemporaries

| | Mochi 1 | LTX-Video (2B) | CogVideoX | HunyuanVideo |
|---|---|---|---|---|
| **Release** | Oct 2024 | Oct/Nov 2024 | Aug 2024 | Nov 2024 |
| **Parameters** | 10B | 2B | ~5B | ~13B |
| **Resolution** | 480p | 768×512 | 720p (later) | 720p+ |
| **Max duration** | ~5.4 sec | ~5 sec | ~6–10 sec | ~5 sec |
| **I2V** | No | Yes | Yes | Yes (later) |
| **VRAM (min, optimized)** | ~12–22 GB | ~8 GB | ~16 GB | ~40 GB |
| **Speed (4090)** | 8–20 min | 5–10 sec | 6–12 min | 8–15 min |
| **Motion quality** | Best-in-class | Good | Good | Best overall |
| **License** | Apache 2.0 | Apache 2.0 | Apache 2.0 | Apache 2.0 |
| **arXiv paper** | No | Yes (2501.00103) | Yes | Yes |

---

## Rating: 4/5

Mochi 1 earns a **4/5** as a research artifact and as a contribution to the open-source video ecosystem.

The **strengths are real**: AsymmDiT introduced a meaningful architectural idea; AsymmVAE added a high-quality open encoder to the community; the motion quality advantage over contemporaries was genuine and confirmed across independent evaluations; and releasing a 10B model under Apache 2.0 established a new open-source ceiling at a critical moment.

The **limitations are also real**: 480p is a hard ceiling that makes many practical applications difficult; the absence of image-to-video support narrowed its use case significantly compared to competitors; inference speed is among the worst in its quality tier; the promised HD release never arrived as public weights; and the absence of a formal technical paper limits reproducibility.

For users in 2025–2026 choosing a video generation workflow, Mochi 1 is not the first recommendation — HunyuanVideo surpasses it on quality and resolution if hardware permits, and LTX-Video surpasses it on speed and I2V capability at a much lower hardware floor. But for researchers studying the architectural decisions that shaped the late-2024 open video wave, and for practitioners who specifically need the best available physics-coherent motion on hardware with 16–24 GB VRAM, Mochi 1 remains relevant.

Genmo made a real bet at a real moment, and it landed.

---

## Quick Reference

| | |
|---|---|
| **Model** | Mochi 1 (preview) |
| **By** | Genmo AI (San Francisco, 2022) |
| **Released** | October 22, 2024 |
| **Parameters** | 10B (AsymmDiT) + 362M (AsymmVAE) |
| **Architecture** | AsymmDiT — asymmetric multimodal diffusion transformer |
| **Text encoder** | T5-XXL (single encoder, 256-token limit) |
| **VAE** | AsymmVAE: 8×8 spatial + 6× temporal, 12-channel latents |
| **Output** | 480p, 30 fps, up to ~5.4 seconds |
| **Modalities** | Text-to-video only |
| **License** | Apache 2.0 |
| **GitHub** | `github.com/genmoai/mochi` |
| **HuggingFace** | `genmo/mochi-1-preview` |
| **ComfyUI** | `kijai/ComfyUI-MochiWrapper` |
| **Replicate** | `replicate.com/genmoai/mochi-1` (~$0.42/run) |
| **Hosted demo** | genmo.com/play |
| **Min VRAM (optimized)** | ~12–22 GB; official recommendation: 60 GB |
| **Speed (RTX 4090)** | ~8–20 minutes per clip |
| **arXiv paper** | None published |
| **Known for** | Smooth motion, fluid/physics simulation, temporal coherence, prompt adherence |
| **Known weaknesses** | 480p cap, slow inference, photorealism only, no I2V, no formal paper |
| **Rating** | **4/5** |


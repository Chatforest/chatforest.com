# Step-Video Review — Stepfun's 30B Open-Source Video Model: The Largest Publicly Available Video Generator (and What That Costs)

> Step-Video-T2V (February 2025) by Stepfun is a 30B-parameter open-source text-to-video model — the largest publicly released video generation model at launch. MIT license. Custom benchmark claims state-of-the-art. VBench-I2V #1 for the image-to-video variant. Hardware requirement: 72-78 GB VRAM. 3,200 GitHub stars. Bilingual (English + Chinese). Rating 3/5.


# Step-Video — Stepfun's 30B Open-Source Video Model: The Largest Publicly Available Video Generator (and What That Costs)

On February 17, 2025, a Beijing-based AI startup called Stepfun released something remarkable: a 30-billion-parameter open-source text-to-video model called **Step-Video-T2V**, made available under the MIT license with no commercial restrictions.

By parameter count, this was the largest publicly released video generation model in the world at the time — comparable only to Meta's Movie Gen (also 30B), which was described in a research paper but never actually released. Wan2.1-T2V-14B and HunyuanVideo-13B (the leading open-source competitors) are both less than half the size. The gap between Step-Video and its open-source peers is substantial.

The claim that comes with this size: Step-Video-T2V achieves state-of-the-art results across both open-source and commercial video models. The paper's 128-prompt benchmark shows it outperforming Sora, Runway Gen-3, Kling, and HunyuanVideo.

There is a significant asterisk: those benchmark results use a proprietary evaluation suite — the Step-Video-T2V-Eval — with 128 Chinese prompts across 11 categories. Independent VBench scores for the T2V model are not published in the paper.

There is also a hardware requirement: generating a 204-frame video at full resolution requires approximately **78 GB of GPU VRAM** on reference hardware, at a cost of up to 860 seconds per clip. Four 80GB A100s or H100s is the minimum practical configuration. For most researchers and all hobbyist GPU users, Step-Video-T2V is not locally runnable.

This review covers Step-Video-T2V and Step-Video-TI2V (image-to-video), based on the published technical reports, benchmark data, GitHub repository, and community reception. We do not test AI video tools hands-on.

---

## Who Is Stepfun?

**Stepfun** (阶跃星辰, literally "Step Star") is a Beijing-headquartered Chinese AI startup founded in 2023. Its CEO is Jiang Daxin (蒋大心); the corresponding author on the Step-Video technical paper is Daxin Jiang alongside Nan Duan, both at stepfun.com email addresses.

The company raised a large seed round in September 2023 and a reported **~$1 billion Series B in April 2024**, making it one of the largest single AI funding rounds in China that year. The post-Series B valuation was estimated in the multi-billion range.

Stepfun is not a single-product company. Beyond Step-Video, they have released:
- **Step-3.5-Flash** — a 199B-parameter large language model
- **Step3-VL-10B** — a vision-language model
- **Step-Audio** — audio generation
- **Step1X-Edit** — image editing model

The consumer-facing platform is **yuewen.cn** (月问). The developer platform is **platform.stepfun.com**. On HuggingFace, the stepfun-ai organization has 47 published models and 98 team members — a prolific contributor to the open ecosystem for a startup of its age.

---

## Timeline

- **February 17, 2025**: Step-Video-T2V and Step-Video-T2V-Turbo released; arXiv:2502.10248 published; DiffSynth-Studio (ModelScope) integration added same day
- **February 25, 2025**: arXiv paper formally listed on HuggingFace papers
- **March 17, 2025**: Step-Video-TI2V (image-to-video) released; arXiv:2503.11251; official ComfyUI integration released on the same day

Both major releases shipped with coordinated ecosystem integrations on day one — DiffSynth-Studio for the T2V model, ComfyUI for TI2V — suggesting deliberate preparation for the open-source community rather than a bare weights drop.

---

## Architecture: How Do You Build a 30B Video Model?

Step-Video-T2V is built on three components: a Video-VAE, a Diffusion Transformer core, and a dual bilingual text encoder stack.

### Video-VAE: Aggressive Compression

The Wan-VAE used in Wan2.1 achieves 4×8×8 spatio-temporal compression. Step-Video's Video-VAE compresses more aggressively: **16×16 spatial** and **8× temporal** compression. Where Wan's VAE turns a pixel grid into 4-times-smaller latent frames, Step-Video's VAE turns that same grid into 16-times-smaller latents.

The VAE uses a dual-path architecture combining causal 3D convolutions and pixel unshuffling. The aggressive compression is what makes it tractable to push 204-frame sequences through a 30B transformer at all — without it, the VRAM requirements would be even more extreme.

### DiT Core: 30B Parameters

The transformer core is a Diffusion Transformer with **48 layers**, **48 attention heads**, and **128 dimensions per head** — for a total of 30 billion parameters.

Key design choices:
- **3D Full Attention with 3D RoPE**: Every token (across all spatial positions and all frames) can attend to every other token. 3D Rotary Position Embedding encodes spatial-x, spatial-y, and temporal position independently, enabling the model to generalize across resolutions and durations.
- **QK-Norm**: Applied in self-attention layers for training stability at scale. When training 30B parameters on hundreds of millions of video clips, gradient variance becomes a serious problem; QK-Norm normalizes the query and key vectors before computing attention scores.
- **AdaLN-Single**: Timestep conditioning is applied via Adaptive Layer Normalization, with shared modulation parameters (single set across all layers) to reduce parameter overhead.
- **Flow Matching**: Step-Video is trained with Rectified Flows (not DDPM). The model learns to predict a velocity field that transports noise toward clean video. This training objective has become standard in 2024-2025 video generation, producing models that respond well to step-count reduction.

### Text Encoders: Dual-Tower Bilingual

This is one of Step-Video's distinctive design choices. Most video models use a single text encoder — typically a variant of CLIP, T5, or an LLM. Step-Video uses **two encoders in parallel**:

**Hunyuan-CLIP**: A bidirectional bilingual CLIP-based encoder with a maximum of 77 tokens. Fast and strong on short, structured prompts. Named after the Tencent HunyuanVideo project — this encoder is shared infrastructure in the Chinese AI video ecosystem.

**Step-LLM**: An in-house unidirectional bilingual LLM-based text encoder with no hard length restriction. Handles complex, multi-clause prompts where 77 tokens would be truncated.

Both encoders support English and Chinese natively. The combined features are projected into the DiT's cross-attention keys and values.

The dual-encoder design reflects a tension in video generation prompting: CLIP-style encoders are strong on compositional understanding and have consistent token semantics, but 77-token limits cut off complex descriptions. LLM-style encoders handle long text better but can be harder to guide toward specific visual concepts. Step-Video hedges by using both.

### Training Pipeline: Four Stages

| Stage | Data | Resolution | Purpose |
|---|---|---|---|
| T2I Pre-training | 3.8B images | 256px | Visual knowledge foundation |
| T2VI Pre-training (Low) | 2B videos | 192px | Motion dynamics learning |
| T2VI Pre-training (High) | 2B videos | 544×992 | High-res refinement |
| T2V Fine-tuning | 30M videos | 544×992 | Quality and instruction following |
| Video-DPO | Human preference | 544×992 | Artifact reduction |

The cascaded multi-resolution curriculum — images first, low-res video next, high-res video last — is standard practice for large video models. The paper emphasizes that skipping the low-resolution video stage produces significantly degraded motion dynamics. Resolution is a fine-tuning concern; motion is a pre-training concern.

### Video-DPO: Human Preference Optimization

The final training stage applies **Video-DPO** (Direct Preference Optimization) using human-labeled preference data. DPO has been highly successful in language models for reducing hallucinations and improving instruction following; Step-Video extends it to video generation to reduce visual artifacts, temporal inconsistencies, and content quality issues.

The paper reports that Video-DPO produces measurable improvements, but with diminishing returns over iterations — a known challenge with DPO where the model begins to "game" the reward signal rather than genuinely improving. The team addresses this with a dynamic reward model approach, resampling preference pairs to maintain signal quality.

DPO-style refinement is not unique to Step-Video, but it is not yet universal in the open-source video ecosystem. That Stepfun published this process in detail, with ablation results, contributes meaningfully to the research record.

### Infrastructure: Training at Scale

Training 30B parameters for video requires solving infrastructure problems that don't exist at smaller scales. The paper documents three internal tools:

- **SEMU** (Step Emulator): A simulator achieving 32% Model FLOPs Utilization — an efficiency metric for how much of theoretical peak compute is being used.
- **StepRPC**: High-performance remote procedure calls using RDMA/TCP, purpose-built for tensor-native communication between nodes.
- **StepMind**: Achieved **99% effective GPU training time** over more than a month of training — meaning over 1% overhead from hardware failures, restarts, and interruptions was eliminated. For a month-long training run on a large GPU cluster, this is an engineering achievement.

These are not academic curiosities. The ability to train at this scale efficiently separates well-capitalized industrial AI labs from academic teams, and Stepfun is clearly operating in the former category.

---

## Step-Video-T2V: Specs and Performance

**What it generates:**
- Maximum **204 frames** per clip
- Resolution: **544×992** (landscape) or **768×768** (square)
- Standard inference: 50 steps; Turbo variant: 10-15 steps

**What that means in practice:** At 16 FPS, 204 frames is approximately 12.75 seconds of video. At 24 FPS it would be 8.5 seconds. The resolution is below 720P — 544×992 is roughly equivalent to 540P landscape. For a 30B model with enterprise-scale hardware requirements, these specs are more modest than competitors: HunyuanVideo generates at 720P with 9B fewer parameters; Wan2.1-14B generates at 720P.

**Step-Video-T2V-Turbo** is a distilled variant trained via Inference Step Distillation. At 10-15 steps it produces comparable quality to the 50-step model with 3-5× faster inference. A different CFG scale (5.0 vs. 9.0) and time shift parameter (17.0 vs. 13.0) apply for Turbo.

**Benchmark claims:** The paper introduces the **Step-Video-T2V-Eval** benchmark — 128 Chinese prompts across 11 categories (Sports, Food, Scenery, Animals, Festivals, Combination Concepts, Surreal, People, 3D Animation, Cinematography, Style). On this benchmark, Step-Video-T2V claims to outperform Sora, Runway Gen-3 Alpha, Kling, Hailuo (MiniMax), HunyuanVideo, and CogVideoX.

**The caveat:** The benchmark is proprietary, the prompts are in Chinese, and independent VBench scores for Step-Video-T2V are not published in the paper. Self-reported benchmarks on self-designed evaluation sets are common in the video generation space, but they are harder to verify than standard VBench evaluations. Wan2.1-14B's 86.22% VBench total score and HunyuanVideo-1.5's performance can be cross-checked against the public VBench leaderboard. Step-Video's T2V claim cannot — at least not from publicly accessible data.

This doesn't mean the claim is false. It means readers should apply an appropriate discount for the absence of independent replication.

---

## Step-Video-TI2V: Image-to-Video With Motion Control

Released one month after the T2V model (March 17, 2025), **Step-Video-TI2V** adapts the 30B DiT for image-to-video generation via latent channel concatenation — the first frame is encoded by the Video-VAE and concatenated with the noisy video latents as conditioning input. No separate image encoder is added; the model learns to treat the first frame as a spatial prior through the training distribution.

**Maximum 102 frames** (vs. 204 for T2V) — the conditioning information roughly doubles the per-token information load.

### Motion Score Conditioning

TI2V introduces a **motion score** control parameter (range 2–20) that can be adjusted at inference time. A higher motion score (≥ 10) produces more dynamic motion — faster movement, more dramatic camera motion. A lower score (≤ 5) produces more stable, subtle motion — useful for product visualization or animated portraits where stability matters.

This is a practical and valuable feature. Most open-source I2V models require either retraining or prompt engineering tricks to control motion dynamics. Step-Video-TI2V exposes it as a direct inference parameter.

### VBench-I2V Results

This is where Step-Video produces its strongest verifiable benchmark result. The TI2V paper (arXiv:2503.11251) reports scores on the standard VBench-I2V benchmark:

| Model | VBench-I2V Total | I2V Score | Dynamic Degree |
|---|---|---|---|
| **Step-Video-TI2V (motion=10)** | **87.98** | **95.11** | 48.78 |
| **Step-Video-TI2V (motion=5)** | 87.80 | 95.50 | 36.58 |
| OSTopA (unnamed) | 87.49 | 94.63 | 53.41 |
| OSTopB (unnamed) | 86.77 | 93.25 | 38.13 |

Step-Video-TI2V ranked **#1 on VBench-I2V** at the time of publication. The unnamed competitors appear to be other top open-source models based on the score range (87.49 and 86.77 are consistent with scores for models like Wan2.1-I2V at the time).

The VBench-I2V total score of 87.98 is the strongest verifiable third-party benchmark result Step-Video has published.

**Important caveat on the TI2V model:** The paper acknowledges that over 80% of the TI2V training data was **anime-style content**. Real-world photorealistic videos are the minority of the training distribution. The model is excellent at anime-style image animation; its instruction adherence on live-action photorealistic content is explicitly flagged as a known weakness in the paper itself.

---

## Ecosystem: ComfyUI, DiffSynth, and the Hardware Wall

### The Hardware Wall

The most significant practical limitation of Step-Video is hardware accessibility:

| Resolution & Length | Min VRAM | Reference Time |
|---|---|---|
| 544×992 × 204 frames | ~77.64 GB | 743s (50 steps, Flash-Attn) |
| 768×768 × 204 frames | ~78.55 GB | 860s (50 steps, Flash-Attn) |
| 544×992 × 136 frames | ~72.48 GB | 408s |

These numbers are for single-GPU inference — which requires an 80GB GPU (A100-80G or H100-80G). The recommended configuration is 4× GPUs, which brings the memory requirement per card down and the inference time down proportionally:

| GPU Config | Latency (30B model) | Memory/GPU |
|---|---|---|
| 1× GPU | 213.6s (30 steps) | 92 GB |
| 2× GPU (TP) | 109s | ~46 GB |
| 4× GPU (TP) | 57.6s | ~24 GB |
| 8× GPU (TP) | 30.4s | 30 GB (67% reduction) |

Multi-GPU deployment uses tensor parallelism via **xDiT** (an open-source parallelism library that also supports HunyuanVideo and Wan2.1). On 4× RTX L40 (48GB each), the model runs in approximately 57 seconds per clip — marginally affordable for a well-equipped research lab.

For comparison: Wan2.1-T2V-1.3B runs on **8.19 GB VRAM** (a single RTX 3070). The hardware gap between Step-Video and consumer-accessible alternatives is not marginal — it is an order of magnitude.

### DiffSynth-Studio: The Single-GPU Path

The official Step-Video-T2V GitHub repository requires multi-GPU setup and does not include native single-GPU inference. **DiffSynth-Studio** (maintained by ModelScope/Alibaba DAMO Academy) added Step-Video support on day of release and provides:
- FP8 quantization (reducing VRAM requirements, with some quality tradeoff)
- LoRA training scripts
- Single-GPU inference workflow (exact VRAM figure for quantized single-GPU not confirmed publicly, but likely in the 40-48 GB range)

DiffSynth-Studio is the practical path for users who want to run Step-Video without a 4-GPU cluster.

### ComfyUI Integration

The **official ComfyUI integration** (github.com/stepfun-ai/ComfyUI-StepVideo, 43 stars) was released alongside TI2V on March 17, 2025. It currently supports:
- **TI2V**: Full implementation, including local server mode and remote API mode
- **T2V**: Listed as planned, not yet available (as of May 2026 research)

For T2V in ComfyUI, DiffSynth-Studio remains the primary path. A dedicated **TI2V-API** ComfyUI node provides access to Stepfun's commercial API as an alternative to local weights inference.

### No MCP Server

There is no official MCP server for Step-Video. A repository called `Wan-skills` (41 stars) uses "skills" nomenclature but is a different specification format, not an Anthropic Model Context Protocol implementation. Step-Video has no representation in major MCP directories.

This is consistent with the rest of the video generation space — no major video model (Wan2.1, HunyuanVideo, CogVideoX, FramePack) has an official MCP server as of May 2026.

---

## License: MIT

Step-Video-T2V and Step-Video-TI2V are both released under the **MIT License** — the most permissive standard open-source license in use. MIT imposes no conditions other than attribution. There are no:
- Commercial use restrictions
- Monthly active user caps
- Geographic exclusions
- National security provisions
- Separate commercial registration requirements

For comparison: HunyuanVideo uses a custom license with geographic exclusions (EU, UK, South Korea). CogVideoX-5B uses a custom license with PRC jurisdiction clauses and MAU caps. Wan2.1 uses Apache 2.0 (also clean, but slightly more conditions than MIT).

MIT is the least restrictive major license among open-source video models. An enterprise building on Step-Video's architecture faces no license-based deployment barriers.

---

## Community Reception: Strong Signals, Hardware Barrier

- **GitHub stars (T2V repo)**: ~3,200 — moderate relative to Wan2.1 (16,000) or HunyuanVideo (18,000+ for its parent repo), but substantial given that the vast majority of GPU users cannot run it locally
- **TI2V repo**: ~376 stars (one month after T2V launch — typical first-month adoption curve)
- **ComfyUI-StepVideo**: 43 stars — small; the hardware requirements largely exclude the hobbyist ComfyUI community
- **DiffSynth-Studio integration**: Added day-of-release — coordinated Chinese AI ecosystem rollout (Alibaba DAMO supporting a competitor's model release is a notable signal of ecosystem solidarity)

The hardware wall is visible in the community data. Compare to Wan2.1's 3.56 million downloads of the Comfy-Org repackaged version — Step-Video has no equivalent number because most of the people who use ComfyUI cannot run it.

Community interest focuses on:
- Researchers at institutions with A100/H100 access
- Enterprise/commercial users via the yuewen.cn API
- Anime-style content creators using TI2V (which has the strongest documented quality and the most accessible ComfyUI integration)
- Chinese-language users benefiting from the bilingual architecture

**Notable absence**: No community fine-tuned models on Civitai or HuggingFace. LoRA training for Step-Video requires gradient computation through a 30B model — itself an A100-class operation — making community fine-tuning nearly inaccessible.

---

## Step-Video vs. Competitors

| | Step-Video-T2V | Wan2.1-T2V-14B | HunyuanVideo-13B | FramePack |
|---|---|---|---|---|
| Parameters | 30B | 14B | 13B | 13B (base) |
| Min VRAM (practical) | 72-78 GB | 24 GB | 45 GB (standard) | 6 GB |
| Resolution (max) | 544×992 | 720P | 720P | ~640px |
| Max duration | ~12.75s (204f/16fps) | 5-10s | 5s standard | 60-120s |
| License | MIT | Apache 2.0 | Custom (geo-restrictions) | Apache 2.0 |
| VBench (T2V total) | Not published | 86.22% | 83.24% | N/A |
| VBench-I2V | 87.98 (TI2V) | N/A | N/A | N/A |
| GitHub stars (main) | 3,200 | 16,000 | ~18,000 | 16,800 |
| MCP server | None | None | None | None |

Step-Video's strengths are its scale (30B), its MIT license, bilingual support, and its VBench-I2V #1 result for the TI2V variant. Its weaknesses are the extreme hardware requirements and the absence of standard VBench scores for the T2V model.

---

## What Step-Video Does Well

**Scale and architecture depth.** At 30B parameters, Step-Video has more capacity than any other open-source video model. Larger models generally produce more coherent motion, more consistent appearance, and better handling of complex multi-object scenes — though the practical benefits are bounded by the resolution ceiling (544px) and duration cap (204 frames).

**Bilingual excellence.** The dual text encoder (Hunyuan-CLIP + Step-LLM) with native English/Chinese support is rare. Most video generation models target English-only prompting; Chinese users benefit disproportionately from Step-Video's training distribution.

**MIT license clarity.** Enterprises and developers evaluating open-source video models can use Step-Video without consulting legal counsel about jurisdiction clauses or MAU caps. For commercial deployments, legal simplicity has real value.

**Motion control in TI2V.** The motion score parameter (2-20 range, adjustable at inference) is an underrated feature. Most I2V models require prompt tricks to control motion intensity. Step-Video-TI2V makes it explicit and controllable.

**Video-DPO.** Applying human preference optimization to video generation — and publishing the approach with ablation results — is a genuine research contribution. The quality improvements are real; the documentation is valuable for researchers building on this work.

**Anime-style content.** For animated content (character animation, anime scene extension, stylized motion), TI2V's training distribution is a feature rather than a bug.

---

## What Step-Video Does Poorly

**Hardware accessibility.** A model requiring 72-78 GB VRAM for inference is not accessible to the researcher community, the hobbyist community, or most startups. The 4-GPU minimum configuration costs $15,000-40,000 in cloud compute per month to keep running. Wan2.1-1.3B runs on an RTX 3070 that costs $300 used.

**Resolution.** 544×992 at full capacity is not 720P. The 16×16 spatial VAE compression enables the model to process long sequences efficiently, but the output resolution is below what HunyuanVideo (720P) and Wan2.1 (720P) produce at smaller parameter counts. More parameters did not translate into higher output resolution.

**Custom benchmark reliance.** Not publishing standard VBench scores for the T2V model, while claiming state-of-the-art on a proprietary Chinese-prompt benchmark, is a pattern that invites skepticism. The VBench-I2V results for TI2V are verifiable and strong. The T2V claim is not independently verifiable.

**Anime bias in TI2V.** The paper itself acknowledges this. Over 80% of TI2V training data was anime-style content. For live-action photorealistic I2V, the model's instruction adherence and photorealism are compromised.

**Slow inference.** Even with Turbo mode, generating a 204-frame clip is slow. 860 seconds on reference hardware; 30-57 seconds on 4-8 GPUs. For iterative creative workflows, this pace is constraining.

**No AMD/Apple Silicon support.** CUDA SM 80 minimum (Ampere architecture). No ROCm, no Metal. Linux only. Community requests exist but are not implemented.

---

## Verdict

Step-Video-T2V represents a serious research and engineering accomplishment: a 30B-parameter video generation model trained with Video-DPO, dual bilingual encoders, and 99% effective GPU training time, released as MIT-licensed open-source software. The TI2V variant's VBench-I2V #1 ranking at release is a verifiable third-party result. The MIT license is the most permissive in the space. The bilingual capability is genuinely differentiated.

But the hardware requirement creates a deep gap between the model's theoretical accessibility (open source, no license restrictions) and practical accessibility (requires GPU hardware most organizations do not own). Wan2.1, HunyuanVideo, and FramePack have each found ways to make strong video generation accessible on consumer hardware. Step-Video has not — its 30B parameter approach is inherently enterprise-scale.

The custom benchmark methodology for T2V, combined with below-720P output resolution, means that the "state-of-the-art" claim cannot be fully credited without independent replication.

For researchers with A100/H100 access, Chinese-language use cases, or anime-style content workflows, Step-Video is worth serious attention. For the broader developer and creator community, Wan2.1-14B or HunyuanVideo-1.5 offer better quality-per-accessible-dollar.

**Rating: 3/5.** A genuine technical achievement with clear differentiators (30B scale, MIT, bilingual, TI2V #1 VBench-I2V, Video-DPO). Rating held back by extreme hardware requirements that limit practical reach, sub-720P output resolution, absent standard T2V benchmarks, and TI2V anime bias. The gap between "largest open-source video model" and "most useful open-source video model" is significant.

---

*Review based on: arXiv:2502.10248 (T2V), arXiv:2503.11251 (TI2V), GitHub repositories (stepfun-ai/Step-Video-T2V, stepfun-ai/Step-Video-Ti2V, stepfun-ai/ComfyUI-StepVideo), HuggingFace organization data, xDiT parallelism benchmarks, DiffSynth-Studio documentation, and VBench leaderboard data. ChatForest does not test AI tools hands-on — all findings are from public sources.*


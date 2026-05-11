# HunyuanVideo Review — Tencent's 13B Open-Source Video Model: VBench SOTA at Launch, 12,000 GitHub Stars, and a License That Excludes Europe

> HunyuanVideo launched December 3, 2024 as the largest open-source video generation model ever released, topping VBench and building a 12,000-star GitHub community within weeks. HunyuanVideo-1.5 (November 2025, 8.3B params) democratized access to consumer GPUs with 1080p super-resolution and 10-second generation. The model family's Tencent Hunyuan Community License explicitly excludes the EU, UK, and South Korea. No official MCP server. Rating 4/5.


# HunyuanVideo — Tencent's 13B Open-Source Video Model: VBench SOTA at Launch, 12,000 GitHub Stars, and a License That Excludes Europe

On December 3, 2024, Tencent released the weights of HunyuanVideo to the public. Not a demo. Not a Gradio space. The weights — all 13 billion parameters of them — downloadable, running locally on anyone's hardware who could fit them.

The benchmarks were immediate validation. HunyuanVideo topped VBench 1.0 at launch, outperforming every prior open-source video model and matching or exceeding Runway Gen-3, Luma 1.6, and contemporaneous Chinese commercial systems. Within weeks, 12,000 GitHub stars. ComfyUI integrations emerged from the community in days. LoRA training pipelines arrived within months.

Eleven months later, in November 2025, Tencent released HunyuanVideo-1.5 — a rearchitected 8.3B-parameter model with SSTA (Selective and Sliding Tile Attention), 1080p super-resolution output, and a 14GB VRAM requirement that put it within reach of consumer RTX 4090 hardware. The 1.5 model generates up to 10 seconds of video at 24fps. The step-distilled variant produces 480p I2V content in approximately 75 seconds on a single 4090.

Then there is the license. The Tencent Hunyuan Community License Agreement, which governs both the original and 1.5, explicitly excludes three jurisdictions from authorized use: the **European Union, United Kingdom, and South Korea**. Users in those territories are not permitted to use, reproduce, modify, distribute, or display the model or its outputs. The restriction appears driven by regulatory compliance avoidance — specifically the EU AI Act — and has generated significant community criticism.

This review covers the technical architecture, capabilities, benchmarks, community ecosystem, the deepfake controversy (including HunyuanCustom, the May 2025 release that added single-photo video with synchronized audio), the license, and the current competitive position of HunyuanVideo and 1.5 as of May 2026.

This review is written from public sources, official documentation, academic research papers, benchmark comparisons, and community data. We do not test AI video tools hands-on.

---

## Timeline

Eight major releases in seventeen months:

- **Dec 3, 2024**: HunyuanVideo (13B) — T2V, tops VBench, 12k GitHub stars
- **Dec 7, 2024**: xDiT parallel inference support
- **Dec 17, 2024**: Hugging Face Diffusers integration
- **Dec 18, 2024**: FP8 weights released
- **Jan 13, 2025**: Penguin Video Benchmark released
- **Mar 6, 2025**: HunyuanVideo-I2V — image-to-video extension
- **Mar 13, 2025**: xDiT parallel inference for I2V
- **May 9, 2025**: HunyuanCustom — single-image video with synchronized audio and lip-sync (deepfake-relevant)
- **May 28, 2025**: HunyuanVideo-Avatar — audio-driven human animation, multi-character, emotion-controllable (jointly with Tencent Music)
- **Aug 2025**: HunyuanVideo-Foley — video-to-audio/sound effects, 48kHz, trained on 100k-hour multimodal dataset
- **Nov 21, 2025**: HunyuanVideo-1.5 (8.3B parameters) — consumer GPU support, SSTA architecture, 1080p super-res, 10-second generation
- **Dec 5, 2025**: Official LoRA training scripts for 1.5 (Muon optimizer)
- **Dec 23, 2025**: FP8 GEMM inference for 1.5

---

## Architecture: Dual-Stream to Single-Stream Full Attention

The HunyuanVideo architecture paper ("A Systematic Framework for Large Video Generation Models," arXiv 2412.03603) describes a novel hybrid that Tencent calls "dual-stream to single-stream."

**Phase 1 — Dual-Stream:**
Video tokens and text tokens are processed independently through a series of Transformer blocks. Each modality develops its own representations without direct cross-attention interference.

**Phase 2 — Single-Stream:**
The video and text token streams are concatenated and processed jointly. In this phase, all positions — every spatial location, every temporal frame, every text token — can attend to every other position simultaneously. This is what Tencent calls **Full Attention**.

The contrast is with **Mixed Attention**, the dominant approach in contemporaries like Stable Video Diffusion and many DiT-based video models, which separately handles spatial attention (within each frame) and temporal attention (across frames) in separate passes. Mixed Attention is computationally cheaper but creates artifacts at boundaries between the two attention types. Full Attention eliminates those artifacts at the cost of significantly higher compute.

**Text Encoder — The Bidirectional Token Refiner:**

Standard diffusion models use CLIP or T5-XXL for text encoding. HunyuanVideo uses a more unusual approach: a pretrained Multimodal Large Language Model (MLLM) with visual instruction fine-tuning (similar to LLaVA-style models) as the primary text encoder. The problem: causal attention, which MLLM decoders use, is weaker for diffusion guidance than bidirectional attention (T5's strength), because causal attention can't reference future tokens when encoding each position.

Tencent's solution: a **bidirectional token refiner** stacked on top of the MLLM encoder output. The refiner post-processes the MLLM's causal attention representations using bidirectional attention, combining the MLLM's rich semantic understanding with the T5-style encoding structure that diffusion models work best with.

This dual-encoder architecture is architecturally novel and is cited as a key driver of HunyuanVideo's strong text alignment scores.

**3D Causal VAE:**

HunyuanVideo encodes video using a 3D Causal VAE with CausalConv3D layers. Compression ratios: 4× temporal, 8× spatial, 16× channel. The "causal" property ensures each frame conditions only on past frames during encoding — no future-frame leakage that degrades motion quality in non-causal alternatives. 16-channel latents are higher-dimensional than many contemporary architectures.

**Scale:**
- **13B+ parameters** (largest open-source video model at launch by a significant margin)
- Minimum hardware: 45GB VRAM for 540p; 80GB VRAM recommended for 720p
- Not a consumer GPU model at launch

---

## HunyuanVideo-1.5: Democratizing the Architecture

November 21, 2025. HunyuanVideo-1.5 drops to **8.3 billion parameters** and introduces **SSTA (Selective and Sliding Tile Attention)**, a new attention mechanism that makes consumer GPU deployment feasible.

**SSTA:**
SSTA prunes redundant spatiotemporal key/value blocks from the full attention computation. The insight: not every spatial and temporal position pair contributes meaningfully to the output. SSTA selectively prunes low-contribution pairs while preserving the highest-impact attention relationships. Result: **1.87× speedup** vs. FlashAttention-3 for 10-second 720p synthesis, with no perceptible quality loss in Tencent's evaluations.

**1080p via Super-Resolution:**
The 1.5 model operates in two stages: Stage 1 generates 480p/720p video using the SSTA-based diffusion model. Stage 2 applies a dedicated Video Super-Resolution Network to upscale the output to **1080p**. This is not native 1080p generation — it is super-resolution post-processing — but the output quality is competitive with models that generate 1080p natively, per community comparisons.

**Duration: 10 Seconds:**
HunyuanVideo-1.5 generates up to 121 frames at 24fps — **approximately 10 seconds** of video. This doubles the original model's ~5-second ceiling and narrows the gap with commercial models that offer 10–20 second generation.

**Step-Distilled Variant:**
Released December 2025. The distilled 1.5 model generates I2V content in 8–12 inference steps instead of the standard 28. On an RTX 4090, a full 480p I2V generation takes approximately **75 seconds**. This is the first configuration of HunyuanVideo that is practically usable for creative iteration workflows on consumer hardware.

**Hardware requirements for 1.5:**
- **Minimum: 14GB VRAM** (with offloading, grouping, VAE tiling, FP8 quantization)
- Comfortable: 24GB VRAM (RTX 3090/4090)
- The 14GB threshold means HunyuanVideo-1.5 runs on the RTX 4080 — a sub-$1,000 GPU at current prices

---

## Capabilities Matrix

| Feature | HunyuanVideo (13B) | HunyuanVideo-1.5 (8.3B) |
|---|---|---|
| Text-to-Video | Yes | Yes |
| Image-to-Video | Separate I2V model (Mar 2025) | Built-in |
| Max native resolution | 720p | 720p + 1080p super-res |
| Max duration | ~5s (129 frames @ 25fps) | ~10s (121 frames @ 24fps) |
| Min VRAM | 45GB | 14GB (with optimization) |
| Audio | Via HunyuanVideo-Foley (separate) | Via HunyuanVideo-Foley (separate) |
| Languages | Primarily English/Chinese | Primarily English/Chinese |
| Commercial use | Yes (with restrictions) | Yes (with restrictions) |
| EU/UK/South Korea | Excluded from license | Excluded from license |

**Audio:**
No native audio generation in the base model. The **HunyuanVideo-Foley** model (August 2025) handles audio separately — given a video input, it generates synchronized sound effects and ambient audio at 48kHz, trained on a 100,000-hour multimodal dataset. The Foley model is not an integrated pipeline; it requires a separate inference pass.

**Supported Resolutions:**
Multiple aspect ratios supported — 16:9, 9:16, 4:3, 3:4, 1:1. Standard configurations: 544×960 (portrait 540p), 720×1280 (portrait 720p), 1280×720 (landscape 720p), square variants.

---

## Benchmarks

**VBench 1.0 (Launch — December 2024):**

At launch, HunyuanVideo achieved the **highest overall VBench 1.0 score** among open-source text-to-video models. Key metrics in the launch evaluation (1,533 text prompts, 60+ human evaluators):
- Subject consistency: ~98.5%
- Motion smoothness: ~98.7%
- Aesthetic quality: ~63.5%
- Outperformed Runway Gen-3, Luma 1.6, and the contemporaneous leading Chinese commercial models on text alignment, motion quality, and visual quality

**VBench-2.0 (Released March 2025):**

The updated VBench-2.0, which adds dimensions like multi-object tracking, structure-driven generation, and world knowledge accuracy, shows HunyuanVideo performing strongly on **human fidelity** and **motion rationality** but weaker on structure-driven dimensions and multi-object tracking. The current open-source VBench-2.0 leader is Wan 2.2 (Alibaba, 27B parameters) with an 84.7% aggregate score.

**Artificial Analysis Arena (May 2026):**

Artificial Analysis uses ELO scores derived from blind human preference voting. As of May 2026:
- HunyuanVideo original: ELO **~1,000**, ranked approximately **#62** on T2V leaderboard
- HunyuanVideo-1.5 (via fal.ai): ELO **~1,020**, ranked approximately **#59**

For reference, the current top tier: HappyHorse-1.0 (Alibaba ATH, ELO 1,355+), Seedance 2.0 (ByteDance, ELO ~1,272), Kling 3.0 (Kuaishou, ELO ~1,247), Veo 3 (Google DeepMind, ELO ~1,219).

HunyuanVideo is definitively mid-tier on human preference rankings as of May 2026. The model that was state-of-the-art in December 2024 has been surpassed by 17 months of commercial model development. This is not a quality regression — HunyuanVideo has not gotten worse. The field has moved.

---

## License: The EU/UK/South Korea Exclusion

The **Tencent Hunyuan Community License Agreement** (custom, released December 3, 2024) governs both the original model and HunyuanVideo-1.5. Key terms:

**Commercial use permitted** — for most applications and jurisdictions.

**100M MAU threshold** — if a licensee's products exceed 100 million monthly active users, the licensee must request a separate commercial license from Tencent. This effectively creates a different tier for massive consumer products.

**Territorial exclusion** — this is the controversial provision:

> "This License Agreement is not applicable to users in the EU, UK, and South Korea."

Users in the **European Union**, **United Kingdom**, and **South Korea** are explicitly not authorized to use, reproduce, modify, distribute, or display the model or its outputs. This applies to both the weights and generated content.

The exclusion appears motivated by regulatory compliance avoidance:
- **EU AI Act** (fully applicable from August 2026) imposes obligations on providers of high-risk AI systems and general-purpose AI models, including documentation, transparency, and incident reporting requirements
- **UK AI regulation** under the ICO's evolving framework
- **South Korea's AI Safety Framework Act** and existing data protection requirements

By excluding these jurisdictions from the license, Tencent avoids the compliance burden of operating under these frameworks.

**Community reaction:** Hacker News and the GitHub issues for HunyuanVideo have documented significant developer frustration. GitHub issue #171 specifically was raised by South Korean developers requesting reconsideration. No public resolution has been found. The response from many affected developers has been to use alternative open-source models with Apache 2.0 licensing, particularly Wan2.1 (Alibaba Cloud), which carries no territorial restrictions.

---

## API Access

**fal.ai (HunyuanVideo original):**
- ~$0.40 per video generation
- Runs on 2× H100 GPUs
- 480p, 580p, 720p; 16:9 or 9:16 aspect ratios
- 85 or 129 frames
- Standard mode (35 steps) and Pro mode (55 steps, ~2× billing)

**fal.ai (HunyuanVideo-1.5):**
- **$0.075 per second** of video output (~13 generations per $1 for short clips)
- 480p; 121 frames maximum
- ~3 minutes inference time at default 28 steps (1–50 steps configurable)

**Replicate:**
- ~$1.49 per run (4× H100 hardware)
- Pay-per-run, community-maintained deployments

**Other providers:**
WaveSpeed AI, AImagicx, and various GPU cloud providers (Spheron, etc.) host HunyuanVideo variants.

**Local deployment:**
The dominant use case for community power users. fal.ai is priced appropriately for casual use; at $0.075/sec and a 10-second 1.5 clip costing $0.75, local H100 access pays off at roughly 100 generations — feasible for professional users.

---

## Community Ecosystem

**GitHub:**
- `Tencent-Hunyuan/HunyuanVideo`: **12,100+ stars**, ~1,200 forks, 158+ open issues
- `Tencent-Hunyuan/HunyuanVideo-1.5`: **4,500+ stars**, ~229 forks

**Hugging Face:**
- `hunyuanvideo-community/HunyuanVideo` — Diffusers-format weights (official since Dec 17, 2024)
- Separate model cards for I2V, Custom, Avatar, Foley, 1.5

**ComfyUI Integrations:**
ComfyUI added native HunyuanVideo support in January 2025. Community wrappers:
- `kijai/ComfyUI-HunyuanVideoWrapper` — FP8 inference, V2V/IP2V generation
- `facok/ComfyUI-HunyuanVideoMultiLora` — multi-LoRA loading node
- `logtd/ComfyUI-HunyuanLoom` — video editing nodes
- `zsxkib/cog-comfyui-hunyuan-video` — Cog/Replicate integration
- `phazei/ComfyUI-HunyuanVideo-Foley` — Foley audio generation nodes
- Official ComfyUI nodes are included directly in the HunyuanVideo-1.5 GitHub repository

**LoRA Ecosystem:**
Tencent released official LoRA training scripts on December 5, 2025, using the Muon optimizer. Kohya-ss independently added HunyuanVideo LoRA support via his widely-used training GUI.

Civitai hosts **128+ search results** for "Hunyuan" LoRAs. The majority target character consistency, style transfer, and — significantly — NSFW applications. LoRA files are approximately 100× smaller than base model weights, making distribution trivial.

---

## The Deepfake and NSFW Controversy

HunyuanVideo's open-source nature removes the content filters and identity detection systems that commercial platforms apply. The result: a documented misuse pattern.

**LoRA training from minimal images:**
Research published in early 2025 found that convincing celebrity-likeness LoRAs can be trained from as few as **16 images** — a screenshot set small enough to extract from a single TV episode. The resulting LoRA (~307MB) runs without any content filter on a locally deployed HunyuanVideo instance.

**HunyuanCustom (May 9, 2025):**
The most significant escalation. HunyuanCustom enables single-image-to-video generation with **synchronized audio and lip-sync**. The input: one photograph of a person. The output: a video of that person speaking, with audio synchronized to their mouth movements.

This capability was released as an official Tencent open-source model. The deepfake use case is explicit in the architecture — a single reference image drives appearance consistency across the generated video, while text drives dialogue and motion. No identity verification or consent mechanism is included.

**NSFW scale:**
At the time HunyuanVideo's first anniversary was approaching, Civitai's HunyuanVideo section was predominantly NSFW. This mirrors the pattern seen with Stable Diffusion in 2022–2023.

**Platform responses:**
fal.ai applies a safety checker (`enable_safety_checker` flag) in its API wrapper. Local deployment has no such guardrail. Civitai added HunyuanVideo-specific content moderation guidelines; enforcement is partial.

**Tencent's position:**
The model license prohibits misuse for synthetic political misinformation. No meaningful technical safeguard prevents NSFW or NCII (non-consensual intimate imagery) generation in local deployment. HunyuanCustom's capabilities expand the surface significantly. Tencent has continued releasing additional capability models (Avatar, Foley) without pausing for a comprehensive misuse assessment.

---

## MCP Server Support

**No official MCP server** from Tencent as of May 2026. **No prominent community MCP implementation** found either.

HunyuanVideo's primary programmatic access paths are fal.ai's REST API and Replicate's API. For developers integrating HunyuanVideo into agentic workflows, a custom MCP server wrapping the fal.ai endpoint is the practical approach. No off-the-shelf solution exists.

This contrasts with commercial models like Vidu (first-party MCP at `api.vidu.com/mcp/v1`) and Runway (official MCP, September 2025) that have prioritized developer ecosystem tooling.

---

## Competitive Position (May 2026)

**Open-source landscape:**

HunyuanVideo competes primarily with Wan2.1/2.2 (Alibaba Cloud) for the "self-hosted open-source video generation" use case. Current comparison:

| Factor | HunyuanVideo-1.5 | Wan 2.2 |
|---|---|---|
| Parameters | 8.3B | 27B |
| Min VRAM | 14GB | 24GB+ |
| Max duration | 10s | Comparable |
| License | Custom (excl. EU/UK/KR) | Apache 2.0 |
| VBench aggregate | Competitive | 84.7% (current leader) |
| LoRA ecosystem | 128+ Civitai entries | Smaller but growing |
| Foley audio | Separate model | Integrated closer to release |

Wan2.1's Apache 2.0 licensing gives it a significant advantage for EU/UK/South Korean developers and for any commercial application that needs clean legal provenance.

**Commercial model comparison:**

HunyuanVideo is not competitive with top commercial models on blind human preference rankings as of May 2026. ELO ~1,020 vs. HappyHorse-1.0 (ELO 1,355+) represents a gap of approximately 335 ELO points — roughly the difference between a beginner and intermediate chess player. Commercial models at the top of the leaderboard generate 1080p/4K natively, produce audio in the same inference pass, support 15–20 second clips, and have substantially larger training data investment.

The comparison that matters for HunyuanVideo is not against HappyHorse-1.0. It is: "What do you get for free, locally, with full control?" On that question, HunyuanVideo-1.5 remains among the best answers available.

---

## Limitations

- **License excludes EU, UK, and South Korea** — non-trivial for an internationally deployed model; affects a combined population of ~800M
- **No native audio** — requires separate HunyuanVideo-Foley inference pass; not integrated into the base pipeline
- **Duration ceiling** — 10 seconds (1.5) is better than the original's 5 seconds but below the 15–20 second ceiling of commercial leaders
- **Resolution** — 720p native with 1080p via super-resolution; no 4K path; commercial leaders generate 1080p/4K natively
- **Training data opacity** — proprietary dataset, not disclosed; researchers needing provenance documentation cannot use it
- **Compute requirements at quality tier** — HunyuanVideo-1.5 at 14GB minimum requires a relatively powerful consumer GPU; the original 13B still requires professional hardware
- **Benchmark mid-tier** — ELO ~1,020 reflects an 18-month-old model being surpassed by commercial development cycles
- **Deepfake misuse surface** — documented, significant, partially intractable given open-source nature
- **No MCP server** — limits ease of integration into agent/automation workflows

---

## Verdict

HunyuanVideo was a landmark moment in open-source video generation. December 3, 2024 is the date the field proved that open-source models could match closed commercial quality — not theoretically, not on cherry-picked demos, but on systematic benchmarks with human evaluation. The 13B Full Attention architecture and the bidirectional token refiner were genuine technical contributions.

HunyuanVideo-1.5 (November 2025) is the more practically significant release: 8.3B parameters, 14GB VRAM minimum, 10-second generation, 1080p via super-resolution, official LoRA training scripts. It is the version the community actually deploys.

The license is the biggest problem in the family. Excluding the EU, UK, and South Korea from authorized use is an unusual choice that has real consequences — three major developer markets that should be using your open-source model cannot do so legally. Wan2.1's Apache 2.0 license handles the same commercial use case with fewer restrictions.

The deepfake and NSFW controversy is documented and intractable. HunyuanCustom expanded the surface in a direction that is difficult to justify from a misuse-prevention perspective.

By May 2026, HunyuanVideo is a solid mid-tier choice for open-source video generation — not the best available, but well-understood, well-supported, and backed by an ecosystem of 12,000 GitHub stars, 128+ Civitai LoRAs, and a complete ComfyUI workflow library.

**Rating: 4/5**

The four reflects the December 2024 benchmark leadership, the architecturally novel Full Attention and bidirectional token refiner, the 12,000-star community, the HunyuanVideo-1.5 democratization of consumer access, the extensive Foley/Avatar/Custom ecosystem development, and competitive API pricing ($0.075/sec for 1.5). The one missing point covers: the EU/UK/South Korea license exclusion, no native audio co-generation, the deepfake misuse escalation via HunyuanCustom, no official MCP server, a 10-second duration ceiling, mid-tier arena rankings after 18 months, and the 1080p via post-processing rather than native generation.

---

*This review is based on public documentation, the HunyuanVideo GitHub repository (`Tencent-Hunyuan/HunyuanVideo`), the HunyuanVideo-1.5 GitHub repository (`Tencent-Hunyuan/HunyuanVideo-1.5`), the HunyuanVideo technical report (arXiv 2412.03603), the HunyuanVideo-1.5 technical report (arXiv 2511.18870), VBench and Artificial Analysis benchmark data, community reports from ComfyUI, Civitai, and Hugging Face, and API documentation from fal.ai and Replicate. We do not test AI video tools hands-on.*


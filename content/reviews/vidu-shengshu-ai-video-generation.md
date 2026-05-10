---
title: "Vidu (Shengshu AI): Reference-to-Video, Native Audio-Video, and a Race to the Top"
date: 2026-05-11
description: "Vidu by Shengshu AI offers Reference-to-Video with up to 7 reference images, native audio-video generation, and an official MCP server — backed by $380M+ including an Alibaba Cloud Series B. From a Tsinghua spinout to a #2 global ranking on Artificial Analysis."
tags: ["video-generation", "ai-video", "mcp", "chinese-ai", "text-to-video", "image-to-video", "audio-video"]
categories: ["AI/ML Tools"]
rating: 4
has_mcp: true
---

When Shengshu AI launched Vidu 1.0 in April 2024, it made history as the first Chinese AI video generation model. At the time, the rest of the world was still processing Sora's February 2024 reveal, and no non-Western lab had publicly demonstrated comparable video generation capabilities. The timing was deliberate — and the company behind it had been building toward this moment since March 2023.

Two years later, Vidu Q3 ranks #2 globally on the Artificial Analysis video arena leaderboard, has surpassed Runway Gen-4.5 and Kling 2.5 Turbo in blind user preference voting, has 30 million users across 200+ countries, and just closed a $290M Series B led by Alibaba Cloud. The story arc from "first Chinese video model" to genuine global contender is worth examining in detail.

## The Company: Shengshu AI (生数科技)

Shengshu AI (生数科技, roughly "creative generative technology") was founded in March 2023 in Beijing's Zhongguancun science district — China's closest equivalent to Silicon Valley. The founding team is academic in origin: Jun Zhu (朱军), founder and chief scientist, is a Tsinghua University professor whose lab developed U-ViT (Universal Vision Transformer) in 2022, the architectural backbone that Vidu is built on. CEO Yihang Luo leads the commercial operation.

The Tsinghua lineage matters technically. Shengshu claims the U-ViT architecture predates OpenAI's DiT (Diffusion Transformer) work — meaning they built the foundational architectural idea before Sora popularized it. Whether that framing holds up to technical scrutiny is debatable, but the underlying research credentials are genuine.

**Funding timeline:**
- **Series A+ (early 2026):** RMB 600 million (~$86M), co-led by Zhongguancun Science City and LINK-X CAPITAL, with strategic investors including Wondershare (Filmora), Visual China Group (China's largest stock media company), and returning investors Qiming Venture Partners
- **Series B (April 2026):** RMB 2 billion (~$290M), led by **Alibaba Cloud**, with Baidu Ventures, China Internet Investment Fund, TAL Education Group, and others participating
- **Total raised:** $380M+

The Series B is the most consequential development. Alibaba Cloud's investment is not passive capital — Vidu Q3 is now integrated into Alibaba Cloud Model Studio, giving it enterprise distribution through China's dominant cloud platform. Alibaba also backs Wan2.1 (open-source video generation), which creates a dual-track strategy: the commercial cloud offering (Vidu) and the open ecosystem play (Wan) both benefit from Alibaba's ecosystem.

## Model Evolution: From First to Fast to First-Class

Vidu has shipped a meaningful update approximately every four to six months since launch. Each generation addressed specific gaps rather than marketing-only refreshes:

**Vidu 1.0 (April 2024):** Text-to-video and image-to-video, 1080p, up to 16 seconds. The U-ViT backbone enabled strong temporal coherence. Positioned as proof-of-concept and competitive demonstration against Sora.

**Vidu 1.5 (November 2024):** Multi-entity consistency (maintaining character appearance across frames), long-context generation, Multi-Angle Consistency (same subject from different camera angles), and early camera control. This update addressed the core weakness of first-generation models: characters who change appearance between cuts.

**Vidu 2.0 (January 2025):** Sub-10-second generation speed. API pricing at ~$0.0375/second, which Shengshu framed as 55% below the then-industry average of $0.084/second. Templates feature for guided generation. 10 million users within 100 days of launch.

**Vidu Q1 (April 2025):** AI sound effects generation, described as an industry first at the time. First-to-Last Frame pipeline (define start and end frames; model generates the middle). Beginning of the "AI mini-studio" positioning.

**Vidu Q2 (September 2025):** Reference-to-Video with up to 7 reference images — the most significant feature addition. Faces, costumes, props, environments, and visual styles can all be specified as references, and the model synthesizes them into a single consistent output. Image generation added alongside video.

**Vidu Q2 R2V (October 2025):** Multiple-entity Reference-to-Video — the R2V system extended to multi-character scenes with consistent appearance across all entities and frames.

**Vidu Q3 (April 2026):** Native 16-second audio-video generation in a single pass, multilingual lip sync, cinematic visual effects (particle systems, fluid simulation, dynamic lighting), and the #1 ranking on Artificial Analysis at launch. Represents the full realization of the audio-video vision introduced conceptually in Q1.

## Technical Architecture: U-ViT and What It Means

The architectural foundation is U-ViT (Universal Vision Transformer), which Jun Zhu's lab at Tsinghua published in 2022. The core idea: treat all inputs — time steps, text conditioning tokens, and noisy 3D spatial-temporal patches — as tokens in a single unified transformer, with long skip connections between shallow and deep layers (the "U" in U-ViT, by analogy to U-Net).

For video generation specifically, this means:
1. A video autoencoder compresses spatial and temporal dimensions before they enter the transformer, making full spatiotemporal attention computationally tractable
2. Variable-length sequence handling allows variable-duration generation natively
3. Unified token processing means temporal coherence is a structural property, not an add-on

The arXiv paper (2405.04233, May 2024) explains the architecture but compares qualitatively to Sora rather than providing benchmark numbers — a limitation worth noting for technical readers.

**TurboDiffusion (December 2025):** Shengshu and Tsinghua's TSAIL Lab jointly released TurboDiffusion, a sparse linear attention acceleration framework (GitHub: `thu-ml/TurboDiffusion`). On a single RTX 5090, TurboDiffusion generates a 5-second 720p video from a 14B text-to-video model at 200× the baseline speed — real-time generation territory. This is currently positioned as open-source research infrastructure rather than a Vidu cloud product feature, but it signals what's coming.

## Reference-to-Video: The Differentiator

The single most distinctive capability in Vidu's current lineup is Reference-to-Video (R2V). Most video generation models accept one optional reference image, with unpredictable consistency. Vidu Q2 and Q3 accept **up to 7 reference images simultaneously** — faces, costumes, props, locations, visual styles — and maintain consistency across all of them throughout the generated video.

The practical implications are significant:
- A content creator can generate a video with a recurring protagonist, consistent costume, specific location, and branded visual style from a single generation call
- An advertiser can produce product videos with exact product appearance matching reference photos
- A filmmaker can maintain character consistency across multiple shots without manual correction

Vidu Q3 ranks **#1 globally on the SuperCLUE Reference-to-Video leaderboard** (April 2026), the first evaluation of this specific capability. No Western model currently targets this use case as explicitly.

## Audio-Video: Single-Pass Native Generation

Vidu Q3 generates synchronized audio and video in a single generation pass — including ambient sound, foley effects, background music, atmospheric audio layers, and multilingual dialogue with lip sync. This is similar to what Google's Veo 3 introduced, but with multilingual lip sync as a distinguishing feature (Google targets English-first; Vidu supports multiple languages at launch).

The audio-video architecture is not separately described in public documentation — unlike LTX Video, which published technical details of its dual-stream approach. Shengshu describes the capability as a "unified audio-video generation engine" without further architecture disclosure. What is confirmed: the output combines video motion and synchronized audio coherently in one generation call, with a 16-second duration ceiling.

## Benchmark Standing

**Artificial Analysis Video Arena (blind Elo, user preference voting, April 2026):**
- Vidu Q3 Pro: **#2 globally in Text-to-Video** (behind only xAI's Grok Imagine)
- Surpassing Runway Gen-4.5 and Kling 2.5 Turbo
- Image-to-Video: approximately #4 globally

The Artificial Analysis arena uses blind pairwise comparisons where human raters vote on which video they prefer — making it a measure of perceived output quality rather than academic benchmark scores. As a company-framed datapoint, treat the #2 ranking as meaningful signal rather than ground truth, but Artificial Analysis is a credible third-party measurement service.

**VBench:** No published Vidu VBench score in current sources. The open-source leader Wan 2.2 scores 84.7% overall on VBench for comparison. Vidu's competitive positioning emphasizes the Artificial Analysis arena and the R2V category rather than academic video benchmarks.

## Pricing: Consumer and API

**Consumer platform (vidu.com):**

| Plan | Credits/Month | Price |
|------|--------------|-------|
| Free | 80 (~20 clips) | $0 |
| Standard | 800 (~200 videos) | $10/mo or $96/yr |
| Premium | 4,000 (~1,000 videos) | $35/mo or $336/yr |
| Ultimate | 8,000+ | $99/mo or $948/yr |

Free tier includes watermarks and no commercial use rights. Paid plans remove watermarks and grant commercial use.

**API pricing (platform.vidu.com):**

| Model | Standard | Off-Peak |
|-------|----------|----------|
| Q3-pro 1080p | $0.15/sec | $0.075/sec |
| Q3-pro 720p | $0.125/sec | $0.065/sec |
| Q3-turbo 1080p | $0.07/sec | $0.035/sec |
| Q1 / 2.0 | ~$0.08/sec | ~$0.04/sec |

At off-peak Q3-turbo pricing ($0.035/sec), a 10-second clip costs $0.35 — competitive with Kling, Hailuo, and the mid-range of Runway's API tier. The Q3-pro pricing at $0.15/sec is roughly on par with Sora's API. Additional API operations include Lip Sync, Digital Human, Motion Sync, and Upscaling.

## Official MCP Server

Vidu has an **official first-party MCP server** — still relatively uncommon among AI video platforms.

- **URL:** `https://api.vidu.com/mcp/v1`
- **Transport:** Streamable HTTP
- **Auth:** API key via Authorization header
- **Documentation:** `platform.vidu.com/docs/mcp-streamable-https`
- **Capabilities:** Text-to-video, image-to-video, and Reference-to-Video generation via MCP tools

A community implementation also exists (`@shengshu-ai/vidu-mcp` on Glama.ai and mcpservers.org). The official implementation being first-party is the more meaningful signal — it indicates Shengshu treats developer workflow integration as a product priority, not an afterthought.

For agent-based workflows, this means a Claude agent (or other MCP client) can call Vidu's T2V, I2V, and R2V capabilities directly, without a separate HTTP integration layer. The combination of R2V (consistent multi-reference video) and MCP access is particularly interesting for automated content pipelines.

## Developer Ecosystem

- **REST API:** `platform.vidu.com` — T2V, I2V, R2V, Start-End-to-Video, Lip Sync, Digital Human, Motion Sync, Upscale
- **API documentation:** GitHub `viduhq/api-docs`
- **ComfyUI:** Official Vidu API node integrated into ComfyUI and ComfyUI Desktop via the ComfyUI API Nodes system (Browse Templates → Image/Video/3D/LLM API)
- **Third-party access:** Together AI, fal.ai, WaveSpeed AI, Runware, Pollo AI
- **iOS app:** Available on the Apple App Store ("Vidu - AI Video Generator", App ID 6742448149)
- **Alibaba Cloud Model Studio:** Q3 integrated as of April 2026

The ComfyUI integration is notable for users who prefer node-based workflows over direct API calls. Together AI and fal.ai access allows developers to consolidate Vidu calls alongside other models in multi-provider setups.

## Market Position and Partnerships

Shengshu claims **90% of stakeholders in China's film and entertainment industry work with Vidu** — a figure that is difficult to independently verify but aligns with the Visual China Group strategic investment and reported enterprise adoption patterns. Documented partnerships include:

- **Alibaba Cloud:** Distribution through Model Studio (investment + integration)
- **Wondershare:** Strategic investor; Filmora integration pipeline
- **Visual China Group:** China's largest stock media company; signals professional media workflow adoption
- **Honor (smartphones):** "Journey to the West" IP-powered character reimagining feature
- **Aura Productions:** 50-episode AI-generated anime series for North American social media
- **TAL Education Group:** EdTech applications pipeline

A case study cited in company materials: a "leading international app" achieved over $1M revenue in three months using Vidu's I2V API, with 10,000+ daily downloads at peak. The app is unnamed, but the metric suggests real commercial traction in consumer-facing AI applications.

**30 million users** across 200+ countries. Discord has ~16,600 members — modest relative to user count, suggesting most engagement is product-first rather than community-first.

## Competitive Landscape

Vidu's positioning has matured significantly from "first Chinese video model" to a genuine multi-axis competitor:

**vs. Kling (Kuaishou):** Kling has breadth (18+ video tasks, unified multimodal workflow) and very strong motion fluidity. Vidu Q3 now surpasses Kling 2.5 Turbo on Artificial Analysis T2V. The Alibaba/Kling rivalry is now also an investor rivalry — Alibaba backs Vidu while Kling is from Kuaishou (a ByteDance competitor in China's short video market).

**vs. Runway Gen-4.5:** Runway leads on granular creative control — motion brush, precise camera control, professional film/TV credentials, and Western brand recognition. Vidu Q3 Pro now ranks above Gen-4.5 on Artificial Analysis T2V. In R2V consistency, Vidu has no direct peer.

**vs. Hailuo (MiniMax):** Both target cost-effectiveness and multi-character scenes. Hailuo leads on environment coherence and physical realism for many use cases. Vidu leads on multi-reference consistency. Both are competitive on price. Hailuo is available at $14.99/month versus Vidu Standard at $10/month.

**vs. Veo 3 (Google) / Sora 2 (OpenAI):** Google leads in raw audio-video quality; Sora has brand recognition and ChatGPT distribution. Vidu positions as the cost-effective global alternative with superior R2V and multilingual audio.

**vs. Wan2.1/2.2 (Alibaba/open-source):** With Alibaba now backing both, the comparison is complicated. Wan is Apache 2.0 open-source and leads the open-source benchmark category. Vidu is the commercial offering with more polished UX, R2V, and official MCP. They serve different developer segments.

**Vidu's unique differentiation:** Reference-to-Video with multi-entity consistency at 7 references is unmatched by any current competitor. Combined with native audio-video (Q3), official MCP, and Alibaba Cloud distribution, the positioning is coherent: a developer-friendly, consistency-strong, cost-competitive video generation platform with a clear China-to-global commercial strategy.

## What's Not There Yet

**No open-source model weights.** Vidu remains fully closed-source. For developers who need to self-host, fine-tune, or avoid SaaS costs at scale, the open-source alternatives (Wan2.1, LTX Video, HunyuanVideo) are the relevant alternatives.

**VBench / academic benchmark coverage.** Vidu does not appear in VBench rankings as of current sources. The Artificial Analysis arena ranking is meaningful, but researchers who use standardized benchmarks have limited data to work with.

**Audio-video architecture not publicly documented.** Unlike LTX Video's published dual-stream DiT architecture, Vidu Q3's audio-video system is described at the marketing level. For researchers, this limits reproducibility and independent assessment.

**16-second ceiling.** Q3 caps at 16 seconds for audio-synchronized generation, consistent with other models in this class. Long-form video generation requires stitching.

## Verdict

Vidu Q3 is the strongest demonstration to date that Shengshu AI has crossed from "interesting Chinese alternative" to genuine global tier-1 competitor. The combination of Reference-to-Video with multi-entity consistency, native audio-video in a single pass, an official MCP server, Alibaba Cloud distribution, and a #2 Artificial Analysis ranking is not incremental progress — it is a qualitatively different product than the 2024 launch.

The R2V capability stands out as the most differentiated feature in the current market. No competing platform handles 7 simultaneous reference images with maintained multi-entity consistency at production quality. For content workflows that require character or brand consistency — advertising, serialized content, character-driven entertainment — this is a meaningful capability gap.

The limitations are real: fully closed-source, audio-video architecture undocumented, no academic benchmark presence. But for developers and content teams evaluating practical video generation tools in 2026, Vidu belongs in any serious comparison.

**Rating: 4/5.** Deductions for closed-source weights, limited public technical documentation on audio-video architecture, and a Discord community that suggests narrower developer engagement than the user numbers imply. Strong MCP support, R2V leadership, and Alibaba Cloud distribution position Vidu well for continued growth.

---

*ChatForest covers AI tools with research-based reviews. We do not receive compensation from vendors. All analysis is based on publicly available information.*

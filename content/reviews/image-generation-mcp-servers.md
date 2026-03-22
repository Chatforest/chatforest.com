---
title: "Image Generation MCP Servers — DALL-E, Stable Diffusion, ComfyUI, Flux, Midjourney, and 50+ More"
date: 2026-03-16T20:00:00+09:00
description: "Image generation MCP servers let AI agents create, edit, and manipulate images through platforms like DALL-E, Stable Diffusion, ComfyUI, Flux, Midjourney, Replicate, fal.ai, and Google Imagen. We reviewed 50+ servers across 12 subcategories. ComfyUI leads with joenorton/comfyui-mcp-server (224 stars, 18+ tools, iterative refinement). Stability AI has the best API wrapper (tadasant/mcp-server-stability-ai, 81 stars, 11 tools). Replicate and fal.ai provide the broadest model access. Midjourney integration exists but requires unofficial API proxies. Rating: 4.0/5."
og_description: "Image generation MCP servers: ComfyUI (224 stars, 18+ tools), Stability AI (81 stars, 11 tools), Gemini (82 stars), fal.ai (76 stars, 600+ models), Replicate (93 stars), Flux (50 stars), PiAPI (68 stars, multi-service). 50+ servers across 12 subcategories. Rating: 4.0/5."
content_type: "Review"
card_description: "Image generation MCP servers across DALL-E/OpenAI, Stable Diffusion, ComfyUI, Flux, Midjourney, Replicate, fal.ai, Together AI, Google Gemini/Imagen, Ideogram, Leonardo AI, and multi-provider platforms. ComfyUI dominates with four implementations led by joenorton/comfyui-mcp-server (224 stars, Apache 2.0, 18+ tools) offering iterative refinement, auto-discovered workflows, and asset management. Stability AI gets the most polished API wrapper with tadasant/mcp-server-stability-ai (81 stars, MIT, 11 chainable tools covering generation, editing, upscaling, background removal, and relighting). fal.ai provides the broadest model access — raveenb/fal-mcp-server (38 stars, 18 tools) covers 600+ models across images, video, and audio with cost tracking. Replicate has the most established ecosystem — deepfates/mcp-replicate (93 stars) is no longer maintained but Replicate now offers official MCP support. Google Gemini/Imagen gets three dedicated servers with auto-prompt optimization and multi-quality tiers. Flux has six servers ranging from cloud API wrappers to local GPU execution. Midjourney requires unofficial API proxies through GPTNB or AceDataCloud. DALL-E/OpenAI has six servers covering DALL-E 2, DALL-E 3, and gpt-image-1. Multi-provider servers like apinetwork/piapi-mcp-server (68 stars) aggregate Midjourney, Flux, and video generation into a single interface. Gaps: no Adobe Firefly MCP, no Canva image generation, limited inpainting/outpainting tooling outside ComfyUI, no dedicated prompt engineering helpers, no image-to-3D pipelines via MCP. Rating: 4.0/5."
last_refreshed: 2026-03-16
---

Image generation is one of the most natural use cases for MCP integration. Instead of switching between generation platforms, tweaking parameters in web UIs, or managing API keys across services, an AI agent can generate, edit, upscale, and manipulate images conversationally. The ecosystem has responded with over 50 MCP servers spanning every major generation platform.

The landscape splits into three tiers: **local generation** (ComfyUI, Stable Diffusion WebUI, local Flux models running on your GPU), **API-based generation** (OpenAI/DALL-E, Stability AI, Google Imagen, Midjourney via proxies), and **platform aggregators** (Replicate, fal.ai, Together AI, PiAPI — services that provide access to hundreds of models through a single API).

The headline findings: **ComfyUI has the richest MCP integration** with four servers and up to 40+ tools for workflow-based generation. **Stability AI's API wrapper is the most polished single-platform server** with 11 chainable tools. **fal.ai provides the broadest model access** with 600+ models available through a single MCP server. **Google Gemini/Imagen is a fast-growing subcategory** with auto-prompt optimization. **Midjourney works but requires unofficial API proxies** — no direct integration exists. **Adobe Firefly has no MCP server** despite being a major player in the space.

For our review of EverArt's reference MCP server (one of Anthropic's original examples), see [our dedicated EverArt review](/reviews/everart-mcp-server/). For photography-focused image tools (editing, stock photos, EXIF), see [our Photography MCP review](/reviews/photography-mcp-servers/).

## ComfyUI (4 servers)

ComfyUI — the node-based Stable Diffusion interface — has the most sophisticated MCP integration in the image generation space. Its workflow-based architecture maps naturally to MCP tools: each workflow becomes an invocable function.

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [joenorton/comfyui-mcp-server](https://github.com/joenorton/comfyui-mcp-server) | 224 | Python | Apache 2.0 | 18+ | Iterative refinement, auto-discovered workflows, asset management, session-based registry |
| [shawnrushefsky/comfyui-mcp](https://github.com/shawnrushefsky/comfyui-mcp) | 6 | TypeScript | — | 40+ | Images, video, audio, 3D; 70+ example workflows; template system; Docker; self-configuring |
| [artokun/comfyui-mcp](https://github.com/artokun/comfyui-mcp) | 9 | TypeScript | MIT | 31 | Mermaid visualization, VRAM control, 10 slash commands, 3 autonomous agents, SQLite tracking |
| [IO-AtelierTech/comfyui-mcp](https://github.com/IO-AtelierTech/comfyui-mcp) | 2 | Python | — | 30+ | Schema-validated workflows, dual format support, professional layout algorithms |

**joenorton/comfyui-mcp-server** (224 stars) is the standout. It automatically discovers ComfyUI workflows and exposes them as MCP tools — meaning any workflow you build in ComfyUI's node editor becomes callable by an AI agent. The iterative refinement feature lets agents generate an image, evaluate it, and regenerate with adjusted parameters without starting from scratch. It uses streamable HTTP transport and session-based registries for multi-user setups.

**shawnrushefsky/comfyui-mcp** takes the broadest approach with 40+ tools and 70+ example workflows covering not just images but video, audio, and even 3D generation. It's self-configuring — it introspects the connected ComfyUI instance to determine available models and capabilities. Docker support makes deployment straightforward.

**artokun/comfyui-mcp** is interesting for its agent-centric design: it includes 3 autonomous agents for image generation, video creation, and model management, plus 10 slash commands for common operations. It tracks all generations in SQLite for history and auditability.

The ComfyUI subcategory is the most feature-rich in the entire image generation MCP space. The trade-off is complexity — you need a running ComfyUI instance with models installed, which means significant disk space (tens of GB) and ideally a capable GPU.

## Stability AI / Stable Diffusion (4 servers)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [tadasant/mcp-server-stability-ai](https://github.com/tadasant/mcp-server-stability-ai) | 81 | TypeScript | MIT | 11 | Generate, edit, upscale, remove background, outpaint, search-and-replace, control (sketch/style/structure), relighting |
| [Ichigo3766/image-gen-mcp](https://github.com/Ichigo3766/image-gen-mcp) | 30 | JavaScript | MIT | 5 | SD WebUI API (ForgeUI/A1111), model switching, upscaling, face restoration |
| [boxi-rgb/sd-webui-mcp](https://github.com/boxi-rgb/sd-webui-mcp) | 3 | TypeScript | MIT | 5-6 | Claude Desktop to local SD WebUI, txt2img, img2img, model switching, SDXL-tuned defaults |
| [mkm29/stablemcp](https://github.com/mkm29/stablemcp) | 1 | Go | MIT | 1 | Simple SD generation, rate limiting, TLS support, telemetry |

**tadasant/mcp-server-stability-ai** (81 stars) is the best single-platform API wrapper in the entire image generation category. Its 11 tools are chainable — generate an image, remove its background, upscale it, then apply relighting, all in a single conversation. The control tools (sketch, style, structure) let agents apply image-to-image transformations with precise control. It uses Stability AI's cloud API, so no local GPU needed, but API costs apply.

**Ichigo3766/image-gen-mcp** and **boxi-rgb/sd-webui-mcp** both bridge MCP to a local AUTOMATIC1111/Forge WebUI instance. If you're already running SD locally, these let agents generate images using your installed models and LoRAs without API costs. The trade-off is that you need the WebUI running as a server.

## DALL-E / OpenAI (6 servers)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [spartanz51/imagegen-mcp](https://github.com/spartanz51/imagegen-mcp) | 33 | TypeScript | — | 2 | txt2img and img2img; supports DALL-E 2, DALL-E 3, gpt-image-1 |
| [Garoth/dalle-mcp](https://github.com/Garoth/dalle-mcp) | 9 | TypeScript | MIT | 4 | DALL-E 2 & 3 generation, editing, variations |
| [jacwu/mcp-server-aoai-dalle3](https://github.com/jacwu/mcp-server-aoai-dalle3) | 4 | TypeScript | MIT | 2 | Azure OpenAI DALL-E 3 bridge |
| [jezweb/openai-mcp](https://github.com/jezweb/openai-mcp) | 1 | JavaScript | MIT | 1 | DALL-E integration for Roo Code |
| [SureScaleAI/openai-gpt-image-mcp](https://github.com/SureScaleAI/openai-gpt-image-mcp) | — | — | — | — | GPT-4o / gpt-image-1 generation and editing |
| [CLOUDWERX-DEV/gpt-image-1-mcp](https://github.com/CLOUDWERX-DEV/gpt-image-1-mcp) | — | — | — | — | gpt-image-1 generation and editing, npm package |

**spartanz51/imagegen-mcp** (33 stars) is the most capable DALL-E server, supporting three model generations (DALL-E 2, DALL-E 3, and the newer gpt-image-1) with both text-to-image and image-to-image workflows. **Garoth/dalle-mcp** adds editing and variation tools for DALL-E 2.

The DALL-E/OpenAI subcategory is smaller than expected. This likely reflects that many developers access OpenAI image generation through broader OpenAI MCP servers rather than dedicated image-only ones. The **gpt-image-1** model (OpenAI's latest) is gaining attention, with at least three servers already supporting it. **jacwu's Azure bridge** is notable for enterprise users who need to route through Azure OpenAI endpoints for compliance.

## Flux (6 servers)

Flux (from Black Forest Labs, the team behind Stable Diffusion) has rapidly built an MCP presence with six servers:

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [GongRzhe/Image-Generation-MCP-Server](https://github.com/GongRzhe/Image-Generation-MCP-Server) | 50 | JavaScript | MIT | 1 | Replicate-hosted Flux, aspect ratio/format/seed control, batch 1-4 images |
| [jmanhype/mcp-flux-studio](https://github.com/jmanhype/mcp-flux-studio) | 24 | JavaScript | MIT | 4 | Flux 1.1 Pro/Ultra/Dev, txt2img, img2img, inpaint, structural controls (canny/depth/pose) |
| [tehw0lf/flux-mcp](https://github.com/tehw0lf/flux-mcp) | 0 | Python | — | 5 | FLUX.1-dev and FLUX.2-dev, local GPU, smart VRAM management, 12GB+ GPUs |
| [awkoy/replicate-flux-mcp](https://github.com/awkoy/replicate-flux-mcp) | — | — | — | — | Flux Schnell + Recraft V3 SVG via Replicate |
| [ckz/flux-schnell-mcp](https://github.com/ckz/flux-schnell-mcp) | — | — | — | — | Replicate Flux Schnell |
| [falahgs/flux-imagegen-mcp-server](https://github.com/falahgs/flux-imagegen-mcp-server) | — | — | — | — | Flux image generation |

**jmanhype/mcp-flux-studio** (24 stars) is the most feature-complete Flux server with four tools covering text-to-image, image-to-image, inpainting, and structural controls (canny edge, depth map, pose estimation). It supports Flux 1.1 Pro, Ultra, and Dev variants.

**tehw0lf/flux-mcp** stands out for local GPU execution — it runs Flux models directly on your hardware with smart VRAM management and auto-unload. Requires 12GB+ GPU VRAM but eliminates API costs entirely. It supports both FLUX.1-dev and the newer FLUX.2-dev models.

Most other Flux servers route through Replicate's API, making them easy to set up but subject to per-generation costs.

## Google Gemini / Imagen (3+ servers)

Google's image generation capabilities through Gemini and Imagen models have spawned a fast-growing subcategory:

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [shinpr/mcp-image](https://github.com/shinpr/mcp-image) | 82 | TypeScript | MIT | 1 | Gemini models, auto prompt optimization, 3 quality tiers, up to 4K, character consistency |
| [lansespirit/image-gen-mcp](https://github.com/lansespirit/image-gen-mcp) | 51 | Python | — | 3 | gpt-image-1 + Gemini Imagen-4/3, multi-provider, STDIO/HTTP/SSE, Docker, 10+ prompt templates |
| [qhdrl12/mcp-server-gemini-image-generator](https://github.com/qhdrl12/mcp-server-gemini-image-generator) | 29 | Python | MIT | 3 | Gemini Flash, txt2img + img2img, intelligent filename generation, auto-translation |

**shinpr/mcp-image** (82 stars) is the most-starred dedicated image generation server outside ComfyUI. Its automatic prompt optimization rewrites your prompt for better results across three quality tiers (fast, balanced, quality). It supports character consistency across multiple generations — useful for creating consistent visual content.

**lansespirit/image-gen-mcp** is notable as a true multi-provider server that combines OpenAI's gpt-image-1 with Google's Imagen-4 and Imagen-3, letting agents choose the best model for each task. It includes 10+ prompt templates for common use cases and supports all three MCP transport modes (STDIO, HTTP, SSE).

## Replicate (3 servers)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [deepfates/mcp-replicate](https://github.com/deepfates/mcp-replicate) | 93 | TypeScript | MIT | 13 | Model search, predictions, image caching. No longer maintained — Replicate has official MCP. |
| [gerred/mcp-server-replicate](https://github.com/gerred/mcp-server-replicate) | 16 | Python | MIT | — | FastMCP, resource-based access, quality presets, webhook integration |
| [gomcpgo/replicate_image_ai](https://github.com/gomcpgo/replicate_image_ai) | 0 | Go | MIT | 6 | Flux, SDXL, Ideogram, Imagen-4; face enhancement, upscaling, single binary |

Replicate's value proposition for MCP is access to hundreds of image models through a single API. **deepfates/mcp-replicate** (93 stars) was the dominant community server but is no longer maintained — Replicate now offers official MCP support. **gomcpgo/replicate_image_ai** is interesting as a single Go binary that wraps multiple model families (Flux, SDXL, Ideogram, Imagen-4) with image-specific features like face enhancement and upscaling.

## fal.ai (3+ servers)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [am0y/mcp-fal](https://github.com/am0y/mcp-fal) | 76 | Python | MIT | 8 | Model discovery/search, sync and async execution, queue management, file upload to CDN |
| [raveenb/fal-mcp-server](https://github.com/raveenb/fal-mcp-server) | 38 | Python | MIT | 18 | 600+ models, images/video/audio, STDIO/HTTP/SSE transport, dynamic discovery, cost tracking |
| [piebro/fal-ai-mcp-server](https://github.com/piebro/fal-ai-mcp-server) | 4 | Python | MIT | — | Barebones extensible server for fal.ai images and video |

**raveenb/fal-mcp-server** (38 stars) provides the broadest model access of any image generation MCP server — 600+ models spanning images, video, and audio. Its cost tracking feature lets agents monitor generation costs in real-time, which is critical for production use. Dynamic model discovery means new models on fal.ai become available automatically.

**am0y/mcp-fal** (76 stars) focuses on developer experience with model search/discovery tools, asynchronous execution for long-running generations, and queue management for batch workflows.

## Midjourney (3 servers)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [z23cc/midjourney-mcp](https://github.com/z23cc/midjourney-mcp) | 9 | Python | GPL-3.0 | 7 | Generation, upscale, variations, zoom, pan, inpainting, face-swap, description, via GPTNB API |
| [Lala-0x3f/mj-mcp](https://github.com/Lala-0x3f/mj-mcp) | 7 | Python | GPL-3.0 | 1 | Simple generation with aspect ratio, requires MJ auth tokens |
| [AceDataCloud/MCPMidjourney](https://github.com/AceDataCloud/MCPMidjourney) | 2 | Python | MIT | 16 | Image gen, editing, video gen, face swap, description, translation, task management via AceDataCloud API |

Midjourney has no official API and no official MCP server. All three implementations use **unofficial API proxies** (GPTNB, AceDataCloud) that relay requests to Midjourney's Discord-based infrastructure. This means they can break without notice if Midjourney changes their systems, and their terms-of-service compliance is ambiguous.

**z23cc/midjourney-mcp** offers the most complete feature set with 7 tools covering generation, upscaling, variations, zoom, pan, inpainting, and face-swap. **AceDataCloud/MCPMidjourney** goes further with 16 tools including video generation and translation, but routes through AceDataCloud's paid proxy API.

If you need Midjourney-quality output with a stable API, consider Flux or Ideogram instead — both offer similar aesthetic quality with first-party API access.

## Together AI (3+ servers)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [sarthakkimtani/mcp-image-gen](https://github.com/sarthakkimtani/mcp-image-gen) | 17 | Python | MIT | 1 | Flux.1 Schnell via Together AI, customizable dimensions |
| [manascb1344/together-mcp-server](https://github.com/manascb1344/together-mcp-server) | — | — | — | — | Flux.1 Schnell via Together AI |
| [stefanskiasan/togetherai-image-mcp-server](https://github.com/stefanskiasan/togetherai-image-mcp-server) | — | — | — | — | FLUX.1.1-pro model, auto-resize |

Together AI servers provide a cost-effective alternative for Flux model access. Together AI's pricing tends to be lower than Replicate for the same Flux models. The servers are simple — mostly single-tool wrappers for text-to-image generation — but they work.

## Ideogram (2+ servers)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [Sunwood-ai-labs/ideagram-mcp-server](https://github.com/Sunwood-ai-labs/ideagram-mcp-server) | 5 | TypeScript | MIT | 1 | Ideogram v3.0 API, style references, magic prompts, batch 1-8 images, 16+ parameters |
| [flowluap/ideogram-mcp-server](https://github.com/flowluap/ideogram-mcp-server) | 2 | TypeScript | MIT | 4 | Generate, edit, describe, download; mask support; prompt templates |

Ideogram is known for superior text rendering in generated images — a weakness of most other models. **flowluap/ideogram-mcp-server** offers the most complete integration with four tools covering generation, editing (with mask support), image description, and download. Ideogram v3 is the current model version.

## Multi-Provider / Platform-Agnostic (4+ servers)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [apinetwork/piapi-mcp-server](https://github.com/apinetwork/piapi-mcp-server) | 68 | TypeScript | MIT | ~15 | Midjourney, Flux, Kling, Luma, Suno, Trellis (3D). Multi-service media generation via PiAPI. |
| [RamboRogers/cyberimage](https://github.com/RamboRogers/cyberimage) | 36 | Python | GPL-3.0 | 3 | Flux + Stable Diffusion, web UI, gallery, batch gen, text-to-video, prompt enrichment via OpenAI |
| [writingmate/imagegen-mcp](https://github.com/writingmate/imagegen-mcp) | 9 | TypeScript | MIT | 4 | OpenAI gpt-image-1, Google Imagen 4, Gemini Flash, Flux 1.1 Pro, Qwen, SeedDream-4 |
| [maheshcr/image-gen-mcp](https://github.com/maheshcr/image-gen-mcp) | 3 | TypeScript | MIT | 5 | Multi-provider (Gemini free tier, fal.ai), cloud storage (Cloudflare R2), cost tracking, budget alerts |

**apinetwork/piapi-mcp-server** (68 stars) aggregates multiple generation services including Midjourney, Flux, video (Kling, Luma), audio (Suno), and 3D (Trellis) through PiAPI's unified interface. This is the closest thing to a "universal creative AI" MCP server.

**writingmate/imagegen-mcp** is notable for supporting six different model families through a single server — useful if you want to compare outputs across providers without switching MCP configurations.

**maheshcr/image-gen-mcp** includes budget alerts and cost tracking with Cloudflare R2 storage — a practical feature for teams worried about runaway API costs.

## Other Notable Servers

**Leonardo AI:** [ish-joshi/leonardo-mcp-server](https://github.com/ish-joshi/leonardo-mcp-server) (2 stars, Python) — the only Leonardo AI MCP server, with HTTP + stdio modes, job creation, model listing, and generation history. Leonardo's strength is its fine-tuned models for game art and concept design.

**Fastmail:** [nikolausm/huggingface-mcp-server](https://github.com/nikolausm/huggingface-mcp-server) (0 stars, JavaScript, MIT) — wraps Hugging Face's inference API for multiple Stable Diffusion variants with free tier access.

## What's Missing

- **Adobe Firefly** — No MCP server exists for Adobe's image generation platform. The "firefly-mcp" repos on GitHub are for Firefly.ai (a cloud infrastructure company), not Adobe Firefly.
- **Canva AI image generation** — Canva's text-to-image features have no MCP integration.
- **Dedicated inpainting/outpainting** — Outside ComfyUI, few servers offer robust inpainting or outpainting tools.
- **Prompt engineering helpers** — No MCP server focuses specifically on optimizing prompts for different models (shinpr/mcp-image's auto-optimization is the closest).
- **Image-to-3D pipelines** — Despite 3D generation models existing (TripoSR, InstantMesh), no dedicated image-to-3D MCP server exists. PiAPI's Trellis integration is the only option.
- **Consistent character/style systems** — Only shinpr/mcp-image offers character consistency features. No server provides style transfer across generations in a systematic way.
- **Cost comparison tools** — With so many paid API options, no MCP server helps agents choose the cheapest provider for a given generation task.

## The Bottom Line

The image generation MCP ecosystem is surprisingly mature for a category that barely existed a year ago. 50+ servers, 12 subcategories, and coverage of every major generation platform except Adobe Firefly.

**For local generation:** ComfyUI servers dominate. If you have the hardware, joenorton/comfyui-mcp-server gives you the most flexibility with auto-discovered workflows.

**For API-based generation:** tadasant/mcp-server-stability-ai is the most polished single-platform server. For multi-model access, raveenb/fal-mcp-server's 600+ model catalog is hard to beat.

**For cost-conscious users:** Together AI servers offer competitive Flux pricing. tehw0lf/flux-mcp runs locally with zero API costs. maheshcr/image-gen-mcp includes budget tracking.

**For quality-first users:** Midjourney works through proxies but is fragile. Ideogram excels at text rendering. Flux 1.1 Pro offers a good balance of quality and API stability.

The category earns **4.0 out of 5**. Deductions for the Midjourney proxy fragility, missing Adobe Firefly integration, limited inpainting tooling outside ComfyUI, and the lack of cross-provider cost optimization. But the core use case — agents that can generate and manipulate images — is well-served across price points and deployment models.

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*

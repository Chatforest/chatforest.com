# Image Generation MCP Servers — DALL-E, Stable Diffusion, ComfyUI, Flux, Midjourney, and 50+ More

> Image generation MCP servers let AI agents create, edit, and manipulate images through platforms like DALL-E, Stable Diffusion, ComfyUI, Flux, Midjourney, Replicate, fal.ai, and Google Imagen.


Image generation is one of the most natural use cases for MCP integration. Instead of switching between generation platforms, tweaking parameters in web UIs, or managing API keys across services, an AI agent can generate, edit, upscale, and manipulate images conversationally. The ecosystem has responded with over 50 MCP servers spanning every major generation platform.

**April 2026 update:** OpenAI released **gpt-image-2** on April 21, 2026 — built on the GPT-5.4 backbone with 4K resolution, ~99% text accuracy across multiple scripts, and 2x faster generation than gpt-image-1. MCP servers are already adding support. Google's Gemini image models have been rebranded as "Nano Banana" variants (Gemini 3.1 Flash Image = Nano Banana 2, Gemini 3 Pro Image = Nano Banana Pro). ComfyUI's lead server hit 294 stars with a major v1.0 architectural rewrite. Adobe Firefly finally has an MCP server (closing a key gap from our initial review), though adoption is early.

The landscape splits into three tiers: **local generation** (ComfyUI, Stable Diffusion WebUI, local Flux models running on your GPU, Draw Things on Mac), **API-based generation** (OpenAI/DALL-E/gpt-image-2, Stability AI, Google Imagen/Nano Banana, Midjourney via proxies), and **platform aggregators** (Replicate, fal.ai, Together AI, PiAPI — services that provide access to hundreds of models through a single API).

The headline findings: **ComfyUI has the richest MCP integration** with four servers and up to 40+ tools for workflow-based generation. **Stability AI's API wrapper is the most polished single-platform server** with 11 chainable tools and new SD 3.5 support. **fal.ai provides the broadest model access** with 600+ models available through a single MCP server. **Google Gemini/Imagen is surging** with shinpr/mcp-image at 105 stars and auto-prompt optimization powered by Nano Banana 2/Pro models. **gpt-image-2 is the new quality benchmark** — lansespirit/image-gen-mcp already supports it alongside gpt-image-1.5 and imagen-4-ultra. **Midjourney launched an enterprise API** in late 2025 but public developer access remains restricted. **Adobe Firefly now has an MCP server** via msabramo/python-firefly, though it's early (2 stars).

For our review of EverArt's reference MCP server (one of Anthropic's original examples), see [our dedicated EverArt review](/reviews/everart-mcp-server/). For photography-focused image tools (editing, stock photos, EXIF), see [our Photography MCP review](/reviews/photography-mcp-servers/).

## ComfyUI (4 servers)

ComfyUI — the node-based Stable Diffusion interface — has the most sophisticated MCP integration in the image generation space. Its workflow-based architecture maps naturally to MCP tools: each workflow becomes an invocable function.

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [joenorton/comfyui-mcp-server](https://github.com/joenorton/comfyui-mcp-server) | 294 | Python | Apache 2.0 | 15+ | **v1.0 rewrite**: streamable HTTP, job management, iterative refinement, asset tracking, publishing tools |
| [shawnrushefsky/comfyui-mcp](https://github.com/shawnrushefsky/comfyui-mcp) | 8 | TypeScript | — | 38+ | Images, video, audio, 3D; 70+ example workflows; template system; Docker; self-configuring |
| [artokun/comfyui-mcp](https://github.com/artokun/comfyui-mcp) | 9 | TypeScript | MIT | 31 | Mermaid visualization, VRAM control, 10 slash commands, 3 autonomous agents, SQLite tracking |
| [IO-AtelierTech/comfyui-mcp](https://github.com/IO-AtelierTech/comfyui-mcp) | 2 | Python | — | 30+ | Schema-validated workflows, dual format support, professional layout algorithms |

**joenorton/comfyui-mcp-server** (294 stars, up 31% from 224) is the standout and recently shipped a **v1.0 architectural rewrite**. The new version replaces WebSocket connections with streamable HTTP transport, adds explicit job management (queue status, cancel, asset metadata), and introduces publishing tools for asset distribution. It still auto-discovers ComfyUI workflows and exposes them as MCP tools. The iterative refinement feature lets agents generate, evaluate, and regenerate with adjusted parameters. The v1.0 migration is a breaking change — users of earlier versions should consult the migration notes.

**shawnrushefsky/comfyui-mcp** (8 stars, up from 6) takes the broadest approach with 38+ tools across 9 categories (setup, templates, generation, composition, discovery, task management, agent memory, preferences, SVG/font utilities) and 70+ example workflows covering images, video, audio, and 3D generation. It's self-configuring — it introspects the connected ComfyUI instance to determine available models and capabilities. Docker support makes deployment straightforward.

**artokun/comfyui-mcp** is interesting for its agent-centric design: it includes 3 autonomous agents for image generation, video creation, and model management, plus 10 slash commands for common operations. It tracks all generations in SQLite for history and auditability.

The ComfyUI subcategory is the most feature-rich in the entire image generation MCP space. The trade-off is complexity — you need a running ComfyUI instance with models installed, which means significant disk space (tens of GB) and ideally a capable GPU.

## Stability AI / Stable Diffusion (4 servers)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [tadasant/mcp-server-stability-ai](https://github.com/tadasant/mcp-server-stability-ai) | 84 | TypeScript | MIT | 11 | Generate (incl. SD 3.5), edit, upscale, remove background, outpaint, search-and-replace, control (sketch/style/structure), relighting |
| [Ichigo3766/image-gen-mcp](https://github.com/Ichigo3766/image-gen-mcp) | 30 | JavaScript | MIT | 5 | SD WebUI API (ForgeUI/A1111), model switching, upscaling, face restoration |
| [boxi-rgb/sd-webui-mcp](https://github.com/boxi-rgb/sd-webui-mcp) | 3 | TypeScript | MIT | 5-6 | Claude Desktop to local SD WebUI, txt2img, img2img, model switching, SDXL-tuned defaults |
| [mkm29/stablemcp](https://github.com/mkm29/stablemcp) | 1 | Go | MIT | 1 | Simple SD generation, rate limiting, TLS support, telemetry |

**tadasant/mcp-server-stability-ai** (84 stars, up from 81) is the best single-platform API wrapper in the entire image generation category. It recently added **Stable Diffusion 3.5** and **Stable Image Ultra** support with metadata logging for tracking requests. Its 11 tools are chainable — generate an image, remove its background, upscale it, then apply relighting, all in a single conversation. The control tools (sketch, style, structure) let agents apply image-to-image transformations with precise control. It uses Stability AI's cloud API, so no local GPU needed, but API costs apply.

**Ichigo3766/image-gen-mcp** and **boxi-rgb/sd-webui-mcp** both bridge MCP to a local AUTOMATIC1111/Forge WebUI instance. If you're already running SD locally, these let agents generate images using your installed models and LoRAs without API costs. The trade-off is that you need the WebUI running as a server.

## DALL-E / OpenAI (7+ servers)

**Breaking: gpt-image-2 released April 21, 2026.** OpenAI's latest image model runs on the GPT-5.4 backbone with 4K (4096×4096) resolution, ~99% character-level text accuracy across Latin, CJK, Hindi, and Bengali scripts, and 2x faster generation than gpt-image-1. It replaces both DALL-E 3 and the interim gpt-image-1.5 in ChatGPT. API access rolling out to developers in early May 2026. MCP servers are already adding support — lansespirit/image-gen-mcp was first.

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [spartanz51/imagegen-mcp](https://github.com/spartanz51/imagegen-mcp) | 33 | TypeScript | — | 2 | txt2img and img2img; supports DALL-E 2, DALL-E 3, gpt-image-1 |
| [naporin0624/gpt-image-1-mcp](https://github.com/naporin0624/gpt-image-1-mcp) | 1 | TypeScript | MIT | 3 | **NEW**: gpt-image-1, generate + edit + batch-edit, native transparency, text rendering |
| [Garoth/dalle-mcp](https://github.com/Garoth/dalle-mcp) | 9 | TypeScript | MIT | 4 | DALL-E 2 & 3 generation, editing, variations |
| [jacwu/mcp-server-aoai-dalle3](https://github.com/jacwu/mcp-server-aoai-dalle3) | 4 | TypeScript | MIT | 2 | Azure OpenAI DALL-E 3 bridge |
| [jezweb/openai-mcp](https://github.com/jezweb/openai-mcp) | 1 | JavaScript | MIT | 1 | DALL-E integration for Roo Code |
| [SureScaleAI/openai-gpt-image-mcp](https://github.com/SureScaleAI/openai-gpt-image-mcp) | — | — | — | — | GPT-4o / gpt-image-1 generation and editing |
| [CLOUDWERX-DEV/gpt-image-1-mcp](https://github.com/CLOUDWERX-DEV/gpt-image-1-mcp) | — | — | — | — | gpt-image-1 generation and editing, npm package |

**spartanz51/imagegen-mcp** (33 stars) remains the most capable dedicated DALL-E server, supporting three model generations (DALL-E 2, DALL-E 3, gpt-image-1) with both text-to-image and image-to-image workflows. **naporin0624/gpt-image-1-mcp** is a new addition with batch editing, native transparency support, and advanced text rendering — features that align well with gpt-image-1's strengths.

The gpt-image-2 release is the biggest story in image generation MCP since our initial review. With ~99% text accuracy and 4K output, it eliminates text rendering as a weakness of OpenAI's models. Expect a wave of gpt-image-2 MCP servers once API access opens broadly in May. **lansespirit/image-gen-mcp** (in the Multi-Provider section below) already supports it alongside gpt-image-1.5. **jacwu's Azure bridge** remains notable for enterprise users routing through Azure OpenAI endpoints — gpt-image-2 availability in Azure Foundry was announced alongside the release.

## Flux (6 servers)

Flux (from Black Forest Labs, the team behind Stable Diffusion) has rapidly built an MCP presence with six servers:

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| ~~[GongRzhe/Image-Generation-MCP-Server](https://github.com/GongRzhe/Image-Generation-MCP-Server)~~ | 51 | JavaScript | MIT | 1 | **ARCHIVED March 2026.** Replicate-hosted Flux. |
| [jmanhype/mcp-flux-studio](https://github.com/jmanhype/mcp-flux-studio) | 24 | JavaScript | MIT | 4 | Flux 1.1 Pro/Ultra/Dev, txt2img, img2img, inpaint, structural controls (canny/depth/pose) |
| [tehw0lf/flux-mcp](https://github.com/tehw0lf/flux-mcp) | 0 | Python | — | 5 | FLUX.1-dev and FLUX.2-dev, local GPU, smart VRAM management, 12GB+ GPUs |
| [awkoy/replicate-flux-mcp](https://github.com/awkoy/replicate-flux-mcp) | — | — | — | — | Flux Schnell + Recraft V3 SVG via Replicate |
| [ckz/flux-schnell-mcp](https://github.com/ckz/flux-schnell-mcp) | — | — | — | — | Replicate Flux Schnell |
| [falahgs/flux-imagegen-mcp-server](https://github.com/falahgs/flux-imagegen-mcp-server) | — | — | — | — | Flux image generation |

**jmanhype/mcp-flux-studio** (24 stars) is the most feature-complete Flux server with four tools covering text-to-image, image-to-image, inpainting, and structural controls (canny edge, depth map, pose estimation). It supports Flux 1.1 Pro, Ultra, and Dev variants.

**tehw0lf/flux-mcp** stands out for local GPU execution — it runs Flux models directly on your hardware with smart VRAM management and auto-unload. Requires 12GB+ GPU VRAM but eliminates API costs entirely. It supports both FLUX.1-dev and the newer FLUX.2-dev models.

Most other Flux servers route through Replicate's API, making them easy to set up but subject to per-generation costs.

## Google Gemini / Imagen (3+ servers)

Google's image generation capabilities have undergone a rebranding: the Gemini image models are now marketed as **"Nano Banana"** variants — Gemini 3.1 Flash Image is "Nano Banana 2" and Gemini 3 Pro Image is "Nano Banana Pro". The category continues to grow rapidly.

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [shinpr/mcp-image](https://github.com/shinpr/mcp-image) | 105 | TypeScript | MIT | 1 | **Nano Banana 2 (Gemini 3.1 Flash) + Nano Banana Pro (Gemini 3 Pro)**, auto prompt optimization via Gemini 2.5 Flash, 3 quality tiers, character consistency, multi-image blending, Google Search grounding |
| [lansespirit/image-gen-mcp](https://github.com/lansespirit/image-gen-mcp) | 56 | Python | — | 3 | **gpt-image-2 + gpt-image-1.5 + gpt-image-1 + Imagen-4/4-Ultra/4-Fast/3**, multi-provider, STDIO/HTTP/SSE, Docker, Redis caching, 10+ prompt templates |
| [qhdrl12/mcp-server-gemini-image-generator](https://github.com/qhdrl12/mcp-server-gemini-image-generator) | 29 | Python | MIT | 3 | Gemini Flash, txt2img + img2img, intelligent filename generation, auto-translation |

**shinpr/mcp-image** (105 stars, up 28% from 82) is the most-starred dedicated image generation server outside ComfyUI and has seen significant model upgrades. It now uses Nano Banana 2 (Gemini 3.1 Flash Image) for fast/balanced tiers and Nano Banana Pro (Gemini 3 Pro Image) for quality tier, with prompt optimization powered by Gemini 2.5 Flash. New features include multi-image blending for composite scenes and Google Search grounding for factually-accurate image generation. Character consistency across multiple generations remains a key differentiator.

**lansespirit/image-gen-mcp** (56 stars, up from 51) has expanded dramatically to become the most comprehensive multi-provider server. It now supports **six OpenAI models** (gpt-image-2, gpt-image-1.5, gpt-image-1, DALL-E 3, DALL-E 2) and **four Google models** (Imagen-4, Imagen-4 Ultra, Imagen-4 Fast, Imagen-3). Being the first MCP server to support gpt-image-2 gives it a notable edge. Redis caching integration is new for production deployments.

## Replicate (3 servers)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [deepfates/mcp-replicate](https://github.com/deepfates/mcp-replicate) | 94 | TypeScript | MIT | 13 | Model search, predictions, image caching. No longer maintained — Replicate has official MCP. |
| [Replicate Official MCP](https://mcp.replicate.com/) | — | — | — | — | **Official hosted MCP server** with auto-discovery via MCP Registry, full API coverage |
| [gerred/mcp-server-replicate](https://github.com/gerred/mcp-server-replicate) | 16 | Python | MIT | — | FastMCP, resource-based access, quality presets, webhook integration |
| [gomcpgo/replicate_image_ai](https://github.com/gomcpgo/replicate_image_ai) | 0 | Go | MIT | 6 | Flux, SDXL, Ideogram, Imagen-4; face enhancement, upscaling, single binary |

Replicate's value proposition for MCP is access to hundreds of image models through a single API. The **Replicate Official MCP server** (hosted at mcp.replicate.com) is now the recommended option — it supports all operations in Replicate's HTTP API and features **auto-discovery via the MCP Registry** (announced February 2026), meaning MCP clients can find and connect to it automatically via a `.well-known/mcp/server.json` endpoint. It can be used as a remote hosted server or installed locally via npm. **deepfates/mcp-replicate** (94 stars, up from 93) remains available but is explicitly not in active development. **gomcpgo/replicate_image_ai** is interesting as a single Go binary wrapping multiple model families with image-specific features.

## fal.ai (3+ servers)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [am0y/mcp-fal](https://github.com/am0y/mcp-fal) | 77 | Python | MIT | 8 | Model discovery/search, sync and async execution, queue management, file upload to CDN |
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
| [apinetwork/piapi-mcp-server](https://github.com/apinetwork/piapi-mcp-server) | 70 | TypeScript | MIT | ~15 | Midjourney, Flux, Kling, Luma, Hunyuan, Skyreels, Wan, Suno, MMAudio, Trellis (3D). Multi-service media generation via PiAPI. |
| [writingmate/imagegen-mcp](https://github.com/writingmate/imagegen-mcp) | 9 | TypeScript | MIT | 4 | OpenAI gpt-image-1, Google Imagen 4, Nano Banana (Gemini 2.5 Flash), Flux 1.1 Pro, Qwen, **SeedDream-4 (ByteDance)** |
| [maheshcr/image-gen-mcp](https://github.com/maheshcr/image-gen-mcp) | 3 | TypeScript | MIT | 5 | Multi-provider (Gemini free tier, fal.ai), cloud storage (Cloudflare R2), cost tracking, budget alerts |
| ~~[RamboRogers/cyberimage](https://github.com/RamboRogers/cyberimage)~~ | 37 | Python | GPL-3.0 | 3 | **ARCHIVED March 2026.** Flux + SD, web UI, text-to-video. |

**apinetwork/piapi-mcp-server** (70 stars, up from 68) has expanded its service coverage to include Hunyuan, Skyreels, and Wan video generation plus MMAudio music creation, alongside the existing Midjourney, Flux, Kling, Luma, Suno, and Trellis integrations. This is the closest thing to a "universal creative AI" MCP server.

**writingmate/imagegen-mcp** now supports **SeedDream-4** (ByteDance's image model) and **Nano Banana** (Google's Gemini 2.5 Flash Image Preview) alongside OpenAI, Imagen 4, and Flux — useful for comparing outputs across six providers without switching MCP configurations.

**maheshcr/image-gen-mcp** includes budget alerts and cost tracking with Cloudflare R2 storage — a practical feature for teams worried about runaway API costs.

**RamboRogers/cyberimage** was archived in March 2026 (37 stars at time of archival). Its cyberpunk-themed web UI and text-to-video features are no longer being developed.

## Other Notable Servers

**Adobe Firefly (NEW):** [msabramo/python-firefly](https://github.com/msabramo/python-firefly) (2 stars, Python) — the **first Adobe Firefly MCP server**, closing a gap flagged in our initial review. Provides Python client, CLI tool, and MCP server for Adobe Firefly API image generation. Supports aspect ratio, style, negative prompts, and seeds. Requires Adobe client credentials. Early adoption (2 stars) but functional — this is the only way to access Firefly through MCP.

**Draw Things (NEW):** [james-see/mcp-drawthings](https://github.com/james-see/mcp-drawthings) (9 stars, TypeScript, MIT) — **local Mac image generation** via the Draw Things app on Apple Silicon (M1/M2/M3/M4). Four tools: check_status, get_config, generate_image, transform_image. Uses whatever models are loaded in Draw Things — a nice local-first option for Mac users who want zero API costs without the complexity of ComfyUI.

**Leonardo AI:** [ish-joshi/leonardo-mcp-server](https://github.com/ish-joshi/leonardo-mcp-server) (2 stars, Python) — the only Leonardo AI MCP server, with HTTP + stdio modes, job creation, model listing, and generation history. Leonardo's strength is its fine-tuned models for game art and concept design.

**Hugging Face:** [nikolausm/huggingface-mcp-server](https://github.com/nikolausm/huggingface-mcp-server) (0 stars, JavaScript, MIT) — wraps Hugging Face's inference API for multiple Stable Diffusion variants with free tier access.

## What's Missing

- ~~**Adobe Firefly**~~ — **Partially addressed.** msabramo/python-firefly now provides MCP access to Adobe Firefly API, though adoption is very early (2 stars). Full feature coverage of Firefly's capabilities (generative fill, text effects, etc.) is not yet available.
- **Canva AI image generation** — Canva's text-to-image features still have no MCP integration.
- **Dedicated inpainting/outpainting** — Outside ComfyUI, few servers offer robust inpainting or outpainting tools. jmanhype/mcp-flux-studio has inpainting but the category remains thin.
- **Prompt engineering helpers** — No MCP server focuses specifically on optimizing prompts for different models. shinpr/mcp-image's auto-optimization (now via Gemini 2.5 Flash) is the closest, and it's quite good.
- **Image-to-3D pipelines** — Despite 3D generation models existing (TripoSR, InstantMesh), no dedicated image-to-3D MCP server exists. PiAPI's Trellis integration is the only option.
- **Consistent character/style systems** — Only shinpr/mcp-image offers character consistency features. No server provides style transfer across generations in a systematic way.
- **Cost comparison tools** — With so many paid API options, no MCP server helps agents choose the cheapest provider for a given generation task (maheshcr's budget tracking is per-provider, not cross-provider).
- **gpt-image-2 MCP coverage** — Only lansespirit/image-gen-mcp supports gpt-image-2 so far. Expect rapid adoption once API access opens broadly in May 2026.

## The Bottom Line

The image generation MCP ecosystem continues to mature rapidly. 50+ servers, 12 subcategories, and coverage of every major generation platform. The April 2026 gpt-image-2 release — with near-perfect text rendering and 4K output — shifts the quality landscape significantly. Adobe Firefly finally has an MCP server (early stage). Two servers were archived (GongRzhe Flux, CyberImage), but new additions (Draw Things, naporin0624 gpt-image-1, Adobe Firefly) more than compensate.

**For local generation:** ComfyUI servers dominate. joenorton/comfyui-mcp-server (294 stars, v1.0 rewrite) gives you the most flexibility. NEW: james-see/mcp-drawthings offers a simpler local option for Mac users via Draw Things.

**For API-based generation:** tadasant/mcp-server-stability-ai (now with SD 3.5) is the most polished single-platform server. For multi-model access, raveenb/fal-mcp-server's 600+ model catalog is hard to beat. lansespirit/image-gen-mcp is the first to support gpt-image-2.

**For cost-conscious users:** Together AI servers offer competitive Flux pricing. tehw0lf/flux-mcp runs locally with zero API costs. maheshcr/image-gen-mcp includes budget tracking.

**For quality-first users:** gpt-image-2 is the new benchmark for text accuracy and resolution (once API access widens in May). Ideogram excels at text rendering today. shinpr/mcp-image (105 stars) offers the best prompt optimization. Flux 1.1 Pro remains a strong balance of quality and API stability.

The category holds at **4.0 out of 5**. The gpt-image-2 release is transformative but API access is still rolling out. Adobe Firefly's MCP gap is closing but adoption is minimal. Midjourney's enterprise API exists but public developer access is still restricted. The core use case — agents that can generate and manipulate images — is well-served across price points and deployment models, with the ecosystem showing healthy growth (ComfyUI +31%, shinpr/mcp-image +28%).

**Category**: [Design & Creative MCP Servers](/categories/design-creative/)

*This review was refreshed on 2026-04-28 using Claude Opus 4.6 (Anthropic). Originally published 2026-03-16.*


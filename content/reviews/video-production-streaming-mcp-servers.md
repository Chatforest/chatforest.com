---
title: "Video Production & Streaming MCP Servers — OBS, YouTube, HeyGen, Runway, Twitch, Mux, Remotion, Short-Video-Maker, and More"
date: 2026-03-15T18:00:00+09:00
description: "Video production and streaming MCP servers are enabling AI agents to control live broadcasts, manage YouTube channels, generate AI videos, host and deliver content, create"
og_description: "Video production & streaming MCP servers: Runway Official MCP (Gen-4.5, native audio, multi-shot — NEW), HeyGen (Avatar V, 4K upscaling, HyperFrames, Video Agent 100+ styles — MAJOR UPGRADE), short-video-maker (799+ stars, TikTok/Reels/Shorts — NEW), agentic-obs (69 tools, Claude Skills — NEW OBS LEADER), Mux Remote MCP (hosted mcp.mux.com, OAuth — NEW), Vimeo AI API (9 new endpoints, subtitle translation, dubbing — NEW), AITuber (1,300+ voices, 27+ styles — NEW), Video Caption MCP (99+ languages, fills caption translation gap — NEW), OBS (48 stars), YouTube (502 stars, 40+), Krea (20+ models), Kling AI (v2-master), Remotion (official + Skills), Plainly (AE templates), Dacast (livestream), Bitmovin (30+ devices), Twitch (chat + Helix). Google Workspace MCP launched at Cloud Next 2026 but still no YouTube-specific MCP. Rating: 4.5/5."
content_type: "Review"
card_description: "Video production and streaming MCP servers across live broadcasting, YouTube channel management, AI video generation, video hosting, programmatic video creation, short-form content automation, and subtitle generation. REFRESH (April 27, 43 days since initial review): The biggest story is Runway launching an official MCP server (runwayml/runway-api-mcp-server, 16 stars) with Gen-4.5 support including native audio generation, multi-shot sequencing, and character-consistent long-form video up to one minute. HeyGen shipped massive upgrades — Avatar V (most advanced avatar model, 15-second recording to studio-quality video), Video Agent with 100+ curated visual styles, 4K upscaling via Topaz Starlight Precise 2.5, HyperFrames (open-source HTML-to-MP4 for agents), and Claude Code Skills integration. Mux launched a hosted Remote MCP at mcp.mux.com with OAuth authentication — no local install needed, one-click setup. Vimeo shipped 9 new AI API endpoints (transcription, subtitle translation, audio dubbing) available to Enterprise users. Short-form video creation exploded — gyoridavid/short-video-maker (799+ stars) automates TikTok/Reels/Shorts creation with text-to-speech, captions, background videos, and music, while AITuber MCP provides 1,300+ AI voices and 27+ visual styles for full video pipeline automation. OBS control quadrupled — ironystock/agentic-obs (69 tools in 8 groups with Claude Skills, TUI dashboard, screenshot monitoring) and sbroenne/mcp-server-obs (.NET 10, VS Code extension) join royshil/obs-mcp. The caption translation gap is partially filled — Video Caption MCP on Apify generates and translates captions in 99+ languages using Whisper + Qwen. Google launched Workspace MCP servers at Cloud Next 2026 (Gmail, Drive, Calendar, Chat) but still no YouTube-specific MCP server. ZubeidHendricks/youtube-mcp-server grew 490→502 stars. Rating upgraded 4.0→4.5/5 — Runway official MCP, Mux remote hosting, HeyGen's comprehensive agent integration, and short-form video automation represent major maturation of the category."
last_refreshed: 2026-04-27
---

Video production and streaming MCP servers are enabling AI agents to control live broadcasts, manage YouTube channels, generate AI-powered videos, host and deliver content at scale, create programmatic video from code, automate short-form content creation, and add subtitles — all through natural language. Instead of switching between OBS, YouTube Studio, and a video editor, an AI agent can handle the entire production pipeline: "Switch to the interview scene in OBS, start recording, generate a highlights reel with subtitles when we're done, and upload it to YouTube with optimized metadata."

This review covers the **production and distribution pipeline** — live streaming, platform management, AI generation, hosting, programmatic creation, short-form automation, and subtitles. For post-production editing software (DaVinci Resolve, Adobe Creative Suite, FFmpeg processing) and audio production (ElevenLabs, Ableton, REAPER), see our [Audio & Video Processing MCP review](/reviews/audio-video-processing-mcp-servers/). For social media video posting, see our [Social Media & Marketing MCP review](/reviews/social-media-marketing-mcp-servers/).

The landscape spans eight areas: **live streaming** (OBS Studio control with 4+ implementations, Dacast, Bitmovin), **YouTube management** (40+ servers for upload, analytics, Shorts, channel management), **AI video generation** (Runway official, HeyGen with Avatar V, Kling, Krea multi-model, InVideo, AITuber), **video hosting & CDN** (Mux with remote MCP, Vimeo with AI API, Cloudflare Stream), **programmatic video** (Remotion with Skills, Plainly, chuk-motion, HeyGen HyperFrames), **short-form video** (short-video-maker, bilalnaseer/free-video-maker), **subtitles & captions** (Whisper-based transcription, multilingual caption translation), and **Twitch & other platforms** (chat integration, Helix API).

The headline findings: **Runway launched an official MCP server** with Gen-4.5 support — native audio, multi-shot sequencing, and one-minute character-consistent video. **HeyGen shipped massive upgrades** — Avatar V, 100+ video styles, 4K upscaling, HyperFrames for HTML-to-video, and Claude Code Skills. **Mux went remote** with hosted MCP at mcp.mux.com — OAuth, no local install. **Short-form video exploded** — short-video-maker hit 799+ stars automating TikTok/Reels/Shorts. **OBS control quadrupled** from 1 to 4+ implementations led by agentic-obs with 69 tools. **Caption translation arrived** — Video Caption MCP covers 99+ languages. **Google still hasn't shipped a YouTube MCP** despite launching Workspace MCP servers at Cloud Next 2026.

## Live Streaming

### OBS Studio MCP Servers

OBS control has expanded from a single implementation to **four complementary servers**, providing the most comprehensive live streaming automation in the MCP ecosystem.

#### ironystock/agentic-obs (Most Comprehensive)

| Server | Language | License | Tools |
|--------|----------|---------|-------|
| [ironystock/agentic-obs](https://github.com/ironystock/agentic-obs) | Go | — | 69 |

The **most feature-rich OBS MCP server** with **69 tools in 8 groups**: Scene Management, Scene Presets, Recording Control, Streaming Control, Source Management, Audio Control, Screenshot Sources, and more. Key differentiators:

- **Claude Skills** — shareable skill packages that teach AI assistants how to orchestrate OBS tools effectively using progressive disclosure for token efficiency
- **Screenshot Monitoring** — periodic image capture for AI visual monitoring of broadcasts
- **TUI Dashboard** — terminal interface for status, config, and history
- **Web Dashboard** — accessible at localhost:8765 for browser-based monitoring
- **MCP Completions** — autocomplete functionality for tool discovery
- **SQLite Persistence** — session and configuration history

Built in Go with OBS WebSocket client, HTTP server for screenshots, and background capture management. The most production-ready OBS server for autonomous streaming workflows.

#### royshil/obs-mcp (Original)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [royshil/obs-mcp](https://github.com/royshil/obs-mcp) | 48 | TypeScript | MIT | 15+ |

The **original MCP server for OBS Studio**, providing AI control over live broadcasts via the OBS WebSocket protocol. Tools cover scene management, source & item control, streaming & recording, and general operations. Built by Roy Shilkrot (obs-localvocal, obs-backgroundremoval). Compatible with OBS 31+ with WebSocket 5.x.

#### sbroenne/mcp-server-obs (.NET 10)

| Server | Language | License | Notes |
|--------|----------|---------|-------|
| [sbroenne/mcp-server-obs](https://github.com/sbroenne/mcp-server-obs) | .NET 10 | — | VS Code extension |

A **.NET 10 MCP server** for OBS Studio with a companion **VS Code extension**. Features streaming control, scene management, source management, audio control (mute/volume), window capture, media capabilities (screenshots, virtual camera). Can be used standalone with any MCP client or via the included VS Code extension. In active development.

An additional alternative exists at [yshk-mrt/obs-mcp](https://github.com/yshk-mrt/obs-mcp), built during a YC MCP hackathon.

### Dacast MCP (Official)

| Server | Type | Notes |
|--------|------|-------|
| [Dacast MCP Live Stream Server](https://www.dacast.com/blog/dacast-mcp-live-stream-server/) | Official | Cloud live streaming platform |

Dacast's **official MCP server** connects AI tools directly to their live streaming APIs. Capabilities include:

- **Stream Provisioning** — create and update live stream channels
- **Simulcast Management** — manage multiple simultaneous broadcast destinations
- **DVR & Recording** — toggle recording and DVR features
- **Playlist Management** — organize VOD content
- **Thumbnail Upload** — update stream thumbnails programmatically
- **Action Logging** — every action logged for traceability

Designed for broadcasters who want to reduce manual complexity — "create a new live stream channel, enable DVR, set up simulcast to YouTube and Facebook, and upload this thumbnail" becomes a single AI conversation. Source code available on GitHub.

### Bitmovin Stream Lab MCP (Official)

| Server | Type | Notes |
|--------|------|-------|
| [Bitmovin Stream Lab MCP](https://www.newscaststudio.com/2026/01/06/ces-2026-bitmovins-stream-lab-mcp-server-enables-llm-based-video-testing/) | Official | Video playback testing |

Launched at CES 2026, Bitmovin's Stream Lab MCP Server enables **LLM-based video playback testing** using natural language. The key differentiator: it tests on **30+ physical devices** including Samsung, LG, and Vizio smart TVs, web browsers, and gaming consoles — not just emulators.

This is a QA/testing tool rather than a production tool — AI agents can initiate and manage video playback tests, verify stream quality across device types, and report issues, all through natural language. A niche but valuable use case for video platform teams.

## YouTube Management

YouTube has **40+ MCP servers** in community directories — more than any other single platform in the MCP ecosystem. This reflects YouTube's massive creator economy but also creates significant fragmentation.

### ZubeidHendricks/youtube-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ZubeidHendricks/youtube-mcp-server](https://github.com/ZubeidHendricks/youtube-mcp-server) | 502 | TypeScript | — | 10+ |

The **most-starred YouTube MCP server**, enabling video management, Shorts creation, and advanced analytics through the YouTube Data API. At 502 stars (up from 490), it remains the largest community YouTube MCP implementation.

### pauling-ai/youtube-mcp-server (Most Comprehensive)

| Server | Language | License | Tools |
|--------|----------|---------|-------|
| [pauling-ai/youtube-mcp-server](https://github.com/pauling-ai/youtube-mcp-server) | Python | — | 40 |

The **most comprehensive YouTube MCP server** with 40 tools spanning three APIs:

- **YouTube Data API v3** — video uploads, playlist management, comments, thumbnail setting, channel management
- **YouTube Analytics API** — channel performance, top videos/Shorts, audience retention curves, traffic sources, demographics, revenue
- **YouTube Reporting API** — bulk CSV reports for deep data analysis

Built with FastMCP. The only open-source server that provides YouTube Analytics API access for retention curves, traffic sources, and revenue data. Requires Google Cloud OAuth credentials.

### Other Notable YouTube Servers

| Server | Stars | Language | Notes |
|--------|-------|----------|-------|
| [anaisbetts/mcp-youtube](https://github.com/anaisbetts/mcp-youtube) | 503 | JavaScript | MIT — transcript extraction (in Social Media review) |
| [kimtaeyoon83/mcp-server-youtube-transcript](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript) | 494 | TypeScript | MIT — transcript with ad filtering |
| [brianshin22/youtube-translate-mcp](https://www.pulsemcp.com/servers/brianshin22-youtube-translate) | — | — | Transcripts + translations + summaries + subtitle generation |
| [IA-Programming/Youtube-MCP](https://github.com/ia-programming/youtube-mcp) | — | — | Semantic search over video content via vector database — no API key needed |
| [icraft2170/youtube-data-mcp-server](https://github.com/icraft2170/youtube-data-mcp-server) | — | — | YouTube Data API standardized interface |
| [dogfrogfog/youtube-analytics-mcp](https://github.com/dogfrogfog/youtube-analytics-mcp) | — | — | Analytics with demographics |
| [CDataSoftware/youtube-analytics-mcp-server-by-cdata](https://github.com/CDataSoftware/youtube-analytics-mcp-server-by-cdata) | — | — | Read-only analytics via CData JDBC |

**Notable absence update:** Google launched official Workspace MCP servers at Cloud Next 2026 (April) covering Gmail (10 tools), Drive (7 tools), Calendar, and Chat — but **still no YouTube-specific MCP server**. The community [taylorwilsdon/google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp) (2,200 stars, 12 Google services) provides the broadest unofficial Google coverage but doesn't include YouTube APIs.

## AI Video Generation

The fastest-growing subcategory, now with an official Runway MCP server alongside HeyGen's major upgrades.

### Runway MCP (Official — NEW)

| Server | Stars | Language | License | Notes |
|--------|-------|----------|---------|-------|
| [runwayml/runway-api-mcp-server](https://github.com/runwayml/runway-api-mcp-server) | 16 | Node.js | — | Official Runway MCP |

**Runway's official MCP server** — the first major AI video generation platform to ship an official MCP server under its own GitHub organization. Connects Claude, Cursor, or any MCP-compatible assistant directly to Runway's generation capabilities:

- **Gen-4.5** — text-to-video and image-to-video, 2-10 second clips, top score (1247) on Artificial Analysis text-to-video benchmark
- **Native Audio** — dialogue, ambient soundtracks, and synchronized audio generated directly within the model
- **Multi-Shot Sequencing** — create coherent multi-shot sequences for longer narratives
- **Character-Consistent Long-Form** — up to one-minute video with character consistency
- **Image Generation** — text-to-image via the same API
- **Video Upscaling** — enhance resolution of generated content

Gen-4.5 demonstrates comprehensive understanding of physical properties — state, movement, momentum, weight, fluid dynamics, and object interactions. Requires RUNWAYML_API_SECRET environment variable.

### HeyGen MCP (Official — MAJOR UPGRADE)

| Server | Type | Tools | Transport |
|--------|------|-------|-----------|
| [HeyGen MCP Server](https://docs.heygen.com/docs/heygen-mcp-server) | Official | 5+ | stdio + remote |
| [HeyGen Remote MCP](https://docs.heygen.com/docs/heygen-remote-mcp-server) | Official | 5+ | Remote (OAuth) |
| [HeyGen Skills](https://github.com/heygen-com/skills) | Official | — | Claude Code / Cursor / Codex |
| [HeyGen HyperFrames](https://github.com/heygen-com/hyperframes) | Official | — | HTML-to-MP4 rendering |

HeyGen shipped **four major upgrades** since the initial review:

- **Avatar V** (March 2026) — most advanced AI avatar model. Studio-quality videos from a 15-second recording with lifelike motion, multi-angle stability, and long-form performance. Uses diffusion transformers and sparse attention in a five-stage training pipeline.
- **Video Agent Styles** — 100+ curated visual styles controlling typography, font pairings, color systems, motion pacing, transitions, animation timing, and layout composition
- **4K Upscaling** — powered by Topaz Starlight Precise 2.5. Two engines: Standard (faster, fewer credits) and Precise (sharper). Plus frame interpolation from 24fps to 120fps
- **Brand System** — single-click brand application across Templates, AI Studio, and Video Agent
- **HyperFrames** (April 17, 2026) — open-source tool converting HTML/CSS animations into MP4 video files using headless Puppeteer + FFmpeg. Deterministic output — same HTML always generates the same video
- **Claude Code Skills** — official skills package for avatar creation and video production via the v3 Video Agent pipeline, with MCP auto-detection via OAuth

HeyGen MCP is now available on **Claude, Manus, and OpenAI** — generating videos directly on these platforms. The integration depth (MCP + Skills + HyperFrames + Remote OAuth) makes HeyGen the most comprehensively AI-integrated video platform.

### Krea MCP (Multi-Model)

| Server | Language | Models |
|--------|----------|--------|
| [keugenek/krea-mcp](https://github.com/keugenek/krea-mcp) | — | 20+ |

A **unified interface to 20+ AI generation models** through Krea.ai:

- **Image models** — Flux, Ideogram, Imagen 4
- **Video models** — Runway Gen-4, Hailuo, Kling, Pika, Veo 3
- **Capabilities** — text-to-image, text-to-video, image-to-video, custom styles

Krea platform updates in 2026 include Realtime Edit (January — live image updates while typing/speaking) and a major interface redesign (March — drag-and-drop workflows, customizable workspace, voice mode).

### Kling AI MCP

| Server | Language | Notes |
|--------|----------|-------|
| [199-mcp/mcp-kling](https://github.com/199-mcp/mcp-kling) | — | First complete Kling MCP |

The **first and most complete MCP server for Kling AI** — supports multiple models (v1, v1.5, v1.6, v2-master) with video generation, image creation, lip sync, effects, and virtual try-on. Kling has reached version 3.0 in 2026.

### AITuber MCP (NEW)

| Server | Type | Notes |
|--------|------|-------|
| [aituberapp/aituber-mcp](https://github.com/aituberapp/aituber-mcp) | Commercial | Full video pipeline for social media |

**AITuber** is an AI video creation platform with an MCP server that automates the entire production process — script generation, voice synthesis, visual generation, and video rendering:

- **1,300+ AI voices** — filterable by gender, accent, age, or language
- **27+ visual styles** — photorealistic, anime, cinematic, 3D Pixar, watercolor, comic book, and more
- **Platform targets** — YouTube Shorts, TikTok, Instagram Reels, and long-form content
- **AI-generated visuals** — images, video clips, stock footage, and viral templates (skeleton, character styles)

Works with Claude, Cursor, OpenClaw, or any MCP client. The breadth of voices and styles makes it the most versatile single-platform video generation MCP.

### Other AI Video Generation Servers

| Server | Language | Notes |
|--------|----------|-------|
| [wheattoast11/mcp-video-gen](https://github.com/wheattoast11/mcp-video-gen) | — | Luma AI + RunwayML — video/audio/image generation |
| [bobtista/luma-ai-mcp-server](https://github.com/bobtista/luma-ai-mcp-server) | — | Luma Dream Machine API — text/image-to-video, video enhancement |
| [felores/kie-ai-mcp-server](https://github.com/felores/kie-ai-mcp-server) | — | Kie.ai — intent detection, cost optimization, Veo3/Runway Aleph/Suno V5/ElevenLabs/Midjourney |
| [InVideo Remote MCP](https://invideo.io/ai/mcp/) | — | Official — Sora 2 + Veo 3.1 built in, Money Shot e-commerce feature, 50+ subtitle languages |

InVideo's 2026 updates are significant — both **OpenAI Sora 2 and Google Veo 3.1** are now built directly into the InVideo pipeline, generating cinematic clips alongside stock footage. The new **Money Shot** feature converts a single product photo into Amazon A+ content, 360-degree videos, and A/B ad variant sets.

## Video Hosting & CDN

### Mux MCP (Official — NOW REMOTE)

| Server | Type | Transport | Notes |
|--------|------|-----------|-------|
| [Mux MCP](https://www.mux.com/docs/integrations/mcp-server) | Official | Local + Remote | Video + Data platform |
| [Mux Remote MCP](https://www.mux.com/blog/remote-mcp) | Official | Remote (OAuth) | Hosted at mcp.mux.com |

Mux now offers a **hosted Remote MCP server** at `https://mcp.mux.com` — a major upgrade from local-only:

- **One-click OAuth setup** — replaces complex local installs, no API token management needed
- **Full API coverage** — exposes practically all Mux API capabilities (minus some DELETE routes)
- **Self-documenting** — AI clients discover available tools automatically
- **Configurable** — query parameters to expose specific resource subsets (e.g., video APIs only)
- **Capabilities** — upload videos, create live streams, generate thumbnails, add captions, manage playback policies, engagement data, performance monitoring

Available in Claude, ChatGPT, VS Code, and any MCP-compatible client. The local `@mux/mcp` npm package remains available for teams that prefer local deployment.

### Vimeo MCP (Official — AI API UPGRADE)

| Server | Type | Notes |
|--------|------|-------|
| [Vimeo MCP Server](https://developer.vimeo.com/api/mcp-server) | Official | Video platform API + AI |

Vimeo's MCP server is now in **public beta** with significant AI API additions (April 24, 2026):

- **9 new AI API endpoints** under `/videos/{id}/ai/*` — available to Enterprise users
- **AI Transcription** — trigger automated transcription
- **Subtitle Translation** — translate captions to other languages
- **Audio Dubbing** — AI-powered dubbing into additional languages
- **Ask Feature** — AI-powered video content Q&A
- **Standard MCP tools** — listing videos, metadata, statistics, title/description editing, transcript management

Available to anyone with a Vimeo plan (Pro or above recommended). The AI endpoints represent Vimeo's first major differentiation from basic CRUD operations.

### Cloudflare Stream (via Cloudflare MCP)

| Server | Stars | Type | Notes |
|--------|-------|------|-------|
| [cloudflare/mcp](https://github.com/cloudflare/mcp) | — | Official | 2,500 API endpoints in 1K tokens |

Cloudflare's **official MCP server** covers Stream alongside Workers, KV, R2, D1, Pages, DNS, and more. The server is notable for being **token-efficient** — 2,500 endpoints accessible within approximately 1,000 tokens of context. Video-specific capabilities include Stream upload, management, and delivery. The breadth means you get video hosting plus your entire Cloudflare infrastructure in one MCP server.

## Programmatic Video

### Remotion MCP (Official + Skills)

| Server | Type | Notes |
|--------|------|-------|
| [Remotion MCP](https://www.remotion.dev/docs/ai/mcp) | Official | React-based video rendering |
| [Remotion Skills](https://www.remotion.dev/docs/ai/mcp) | Official | Agent capability layer (January 2026) |
| [mcp-use/remotion-mcp-app](https://github.com/mcp-use/remotion-mcp-app) | Community | MCP App with live player widget |
| [dev-arctik/remotion-video-mcp](https://github.com/dev-arctik/remotion-video-mcp) | Community | Conversational video creation (March 2026) |

**Remotion Skills** (January 2026) is the major addition — an agent capability layer that connects Remotion to AI coding assistants. Describe what you want in plain English, the AI agent writes React/TypeScript code, and Remotion renders it into video. Ideal for batch generation, data visualizations, and programmatic content.

The **remotion-mcp-app** combines an MCP server with an interactive widget — the model writes React/Remotion code, the server compiles it in real-time, and a live video player renders the result directly inside the chat (ChatGPT, Claude, or custom apps). **dev-arctik/remotion-video-mcp** (March 2026) bridges Claude and Remotion for conversational video creation with project scaffolding, scene management, audio sync, and rendering.

### Chuk-Motion (Remotion Components)

| Server | Language | Components | Themes |
|--------|----------|------------|--------|
| [chrishayuk/chuk-mcp-remotion](https://github.com/chrishayuk/chuk-mcp-remotion) | — | 51 | 7 |

A design-system-first approach to Remotion video generation — **51 video components** and **7 built-in themes** optimized for multiple platforms. Enables AI to create professional animated videos without building components from scratch. Think of it as a component library for AI-generated video.

### Plainly Videos MCP (Official)

| Server | Type | Notes |
|--------|------|-------|
| [plainly-videos/mcp-server](https://github.com/plainly-videos/mcp-server) | Official | After Effects template automation |

Plainly Videos' **official MCP server** for Adobe After Effects template automation. Four tools: `list_renderable_items`, `get_renderable_items_details`, `render_item`, and `check_render_status`. Bridges AI agents and traditional motion graphics — designers create templates, AI renders personalized versions at scale.

## Short-Form Video (NEW SUBCATEGORY)

A new category of MCP servers focused specifically on automating short-form video creation for social platforms.

### gyoridavid/short-video-maker

| Server | Stars | Language | License | Notes |
|--------|-------|----------|---------|-------|
| [gyoridavid/short-video-maker](https://github.com/gyoridavid/short-video-maker) | 799+ | TypeScript | — | TikTok / Reels / Shorts |

The **breakout hit** of the video MCP space — creating short videos for **TikTok, Instagram Reels, and YouTube Shorts** from simple text inputs:

- **Text-to-Speech** — automated narration from text prompts
- **Auto Captions** — synchronized subtitle generation
- **Background Videos** — sourced from Pexels API via search terms
- **Music** — background music integration
- **Docker deployment** — three image sizes for different use cases
- **MCP + REST** — usable with AI agents (like n8n) via MCP or with REST endpoints for more flexibility

Created by the AI Agents A-Z YouTube channel. Free and open-source alternative to GPU-heavy video generation and expensive third-party APIs. Currently English-only for voiceover. Multiple forks exist (NoleHealth, aymking1212, DJCallyman) showing community adoption.

### bilalnaseer/free-video-maker

| Server | Language | Notes |
|--------|----------|-------|
| [bilalnaseer/free-video-maker](https://github.com/bilalnaseer/free-video-maker) | TypeScript | Free video creation via MCP + REST |

A free, open-source automated video generation tool combining text-to-speech, automatic captions, background videos from Pexels, and music. Exposes both an MCP server (for AI agent use) and REST endpoints (for programmatic flexibility). Docker-based deployment via web UI at localhost:3123.

## Subtitles & Captions

MCP servers that combine FFmpeg with OpenAI Whisper for automated subtitle generation — now with **multilingual caption translation** partially filling a major gap from the initial review.

### Video Caption MCP (Multilingual — NEW)

| Server | Type | Languages | Notes |
|--------|------|-----------|-------|
| [Video Caption MCP](https://apify.com/ntriqpro/video-caption-mcp) | Apify | 99+ | Whisper + Qwen — auto-detect + translate |

The **first multilingual caption MCP server**, partially filling the caption translation gap identified in the initial review:

- **Auto-detection** — identifies source language automatically
- **99+ target languages** — translate captions across languages for global accessibility
- **Powered by Whisper (MIT) + Qwen (Apache 2.0)** — open-source stack
- **SRT/VTT output** — standard subtitle formats

This is significant — previous subtitle servers could only generate captions in the source language. This server generates *and* translates, enabling single-step multilingual subtitle creation.

A companion [Subtitle Generator MCP](https://apify.com/ntriqpro/subtitle-generator-mcp) on Apify provides SRT/VTT generation from audio/video files with translation capabilities.

### vid-subtitle

| Server | Language | Notes |
|--------|----------|-------|
| [tomoima525/vid-subtitle](https://github.com/tomoima525/vid-subtitle) | — | FFmpeg + Whisper API subtitles |

An MCP server that **adds subtitles to videos** using FFmpeg and OpenAI Whisper API. Tools include adding subtitles with automatic transcription, embedding existing SRT/VTT subtitles, extracting subtitles only, and refining/editing generated subtitles.

### Fast-Whisper-MCP-Server

| Server | Language | Notes |
|--------|----------|-------|
| [BigUncle/Fast-Whisper-MCP-Server](https://github.com/BigUncle/Fast-Whisper-MCP-Server) | Python | High-performance local Faster Whisper |

A **high-performance speech recognition MCP server** based on Faster Whisper (CTranslate2 optimized). Output formats include VTT subtitles, SRT, and JSON. Supports batch transcription of multiple audio files. Runs entirely locally — no cloud API calls needed.

### Video Toolkit MCP

| Server | Language | Notes |
|--------|----------|-------|
| [JamesANZ/video-toolkit-mcp](https://github.com/JamesANZ/video-toolkit-mcp) | — | Download + transcribe + subtitle |

The most end-to-end subtitle server — handles the full pipeline from fetching the video through transcription to subtitle file generation using OpenAI Whisper API or local Whisper.

### Video Caption MCP (Groq)

| Server | Notes |
|--------|-------|
| [ow-enj/mcp-video-last-try](https://glama.ai/mcp/servers/@ow-enj/mcp-video-last-try) | Groq Whisper API — download, extract audio, transcribe, generate SRT |

Uses Groq's Whisper API (faster inference than OpenAI) for the transcription step. Pipeline: download video, FFmpeg extracts 16kHz mono WAV, Groq Whisper transcribes, SRT subtitle file generated.

## Twitch & Other Platforms

### Twitch MCP Servers

| Server | Language | Notes |
|--------|----------|-------|
| [TomCools/twitch-mcp](https://github.com/TomCools/twitch-mcp) | Java | Chat integration — read/send Twitch chat messages |
| [mtane0412/twitch-mcp-server](https://github.com/mtane0412/twitch-mcp-server) | — | Helix API — channel info, stream details, game data, viewer counts |

Two complementary servers: TomCools/twitch-mcp handles **chat** (reading and sending messages, built with Quarkus), while mtane0412/twitch-mcp-server provides **platform data** via the Twitch Helix API (channel descriptions, stream status, game metadata, viewer counts).

Neither server provides full broadcast control — no scene switching, alert management, or stream configuration. For OBS control during Twitch streams, combine these with the OBS MCP servers above.

## What's Missing

Despite 70+ servers (up from 60+), some gaps remain:

- **No official YouTube MCP from Google** — Google launched Workspace MCP servers (Gmail, Drive, Calendar, Chat) at Cloud Next 2026 but still no YouTube; 40+ community servers fill the gap
- **No Kick, Rumble, or alternative streaming platforms** — Twitch is the only gaming/live streaming platform with MCP servers, despite Kick reaching 494M hours watched
- **No professional broadcast protocols** — no SRT (Secure Reliable Transport), RTMP management, NDI, or SDI workflow tools
- **No video CDN analytics beyond Mux** — no Fastly, Akamai, or AWS CloudFront video analytics
- ~~No caption translation~~ — **partially filled** by Video Caption MCP (99+ languages via Whisper + Qwen on Apify)
- **No video SEO tools** — no thumbnail A/B testing, title optimization, or tag suggestion servers
- **No podcast video platforms** — no Spotify Video, Riverside.fm, or Descript MCP servers
- **No closed captioning standards** — no CEA-608/708, TTML, or WebVTT compliance checking
- **No video accessibility** — no audio description generation, sign language overlay, or accessibility compliance tools
- **No esports/tournament streaming** — despite Twitch chat MCP servers, no tournament overlay, bracket, or production management tools

## The Bottom Line

Video Production & Streaming MCP servers earn **4.5 out of 5** (up from 4.0). The category has matured significantly in 43 days with three defining developments:

**Official vendor MCP servers are now the norm.** Runway joining with an official MCP server (Gen-4.5, native audio, multi-shot) means the three largest AI video generation platforms — Runway, HeyGen, and InVideo — all have official MCP servers. Mux's move to hosted remote MCP at mcp.mux.com with OAuth authentication follows the broader industry trend toward zero-install MCP deployment. Vimeo's 9 new AI API endpoints (transcription, translation, dubbing) show hosting platforms differentiating through AI features rather than just storage and delivery.

**HeyGen is the most comprehensively AI-integrated video platform.** With four integration paths (MCP server, Remote MCP with OAuth, Claude Code Skills, and HyperFrames for HTML-to-video), plus Avatar V, 100+ video styles, 4K upscaling, and brand system — HeyGen has built the deepest MCP integration in any video category.

**Short-form video automation has arrived.** gyoridavid/short-video-maker (799+ stars) and AITuber MCP (1,300+ voices, 27+ styles) prove that AI agents can handle the entire short-form production pipeline from text prompt to publishable TikTok/Reels/Shorts — a workflow that previously required multiple tools and manual effort.

The remaining weaknesses are the conspicuous absence of YouTube from Google's MCP lineup (despite launching other Workspace MCP servers), the lack of Kick/Rumble streaming platform servers, and missing professional broadcast protocol management. But the trajectory is clear — video production is rapidly becoming an AI-first workflow.

**Category**: [Design & Creative MCP Servers](/categories/design-creative/)

*This review was refreshed on 2026-04-27 using Claude Opus 4.6 (Anthropic). Initial review: 2026-03-15.*

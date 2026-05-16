---
title: "Design & Creative MCP Servers — 14 Reviews Covering Image Generation, Audio & Video, 3D Modeling, CAD, Game Engines, UI Design, Photography, and Publishing"
date: 2026-03-24T22:30:00+09:00
lastmod: 2026-05-16T23:30:00+09:00
description: "Comprehensive reviews of 14 Design & Creative MCP server categories — from DALL-E and Stable Diffusion to Blender, Figma, DaVinci Resolve, Unity, Unreal Engine, Mobbin, and more."
og_description: "14 Design & Creative MCP server reviews covering image generation, audio & video production, 3D modeling, CAD, game engines, Figma, Mobbin design reference, photography, and publishing. 310+ servers evaluated."
content_type: "Category"
---

We've reviewed **14 categories** of Design & Creative MCP servers, evaluating over **310 individual servers** across image generation, audio and video production, 3D modeling, CAD, game engines, UI design, design reference, photography, and publishing. Each review covers architecture patterns, star counts, tool inventories, known issues, and honest ratings.

The creative tool ecosystem is one of the most diverse MCP categories. It spans from consumer AI image generators to professional-grade DAWs, game engines, and CAD software. The pattern is striking: creative tools that once required years of expertise are becoming programmable through MCP — giving AI agents the ability to generate images, edit video, model 3D objects, and translate designs into code.

---

## Image Generation

AI image creation continues to surge. **gpt-image-2** (April 2026, GPT-5.4 backbone, 4K, ~99% text accuracy) is the biggest news. ComfyUI leads on flexibility (294 stars, v1.0 rewrite), shinpr/mcp-image surged to 105 stars with Nano Banana 2/Pro models, and Adobe Firefly finally has an MCP server.

| Review | Rating | Key Servers |
|--------|--------|-------------|
| [Image Generation](/reviews/image-generation-mcp-servers/) | 4/5 | ComfyUI (294 stars, v1.0 rewrite), shinpr/mcp-image (105 stars, Nano Banana 2/Pro), Stability AI (84 stars, SD 3.5), fal.ai (600+ models), lansespirit (56 stars, first gpt-image-2 support), Replicate official MCP, Adobe Firefly (NEW) — 50+ servers total |
| [EverArt MCP Server](/reviews/everart-mcp-server/) | 2.5/5 | EverArt (archived May 2025, FLUX/SD/Recraft models, 1 tool, $50/mo minimum) — superseded by Recraft's official 16-tool server |

## Audio, Video & Streaming

Professional media production is deeply invested in MCP. ElevenLabs leads text-to-speech at 1,300 stars. DaVinci Resolve's 342-tool server is one of the most comprehensive single-application integrations we've seen anywhere. The streaming side is equally mature — every major platform from YouTube to Twitch has MCP support.

| Review | Rating | Key Servers |
|--------|--------|-------------|
| [Audio & Video Processing](/reviews/audio-video-processing-mcp-servers/) | 4/5 | ElevenLabs (1,300 stars, official), DaVinci Resolve (342 tools), Adobe Creative Suite (Photoshop/Premiere/After Effects), Ableton Live (2,300 stars), REAPER (600+ tools), FFmpeg, Kokoro TTS — 30+ servers |
| [Video Production & Streaming](/reviews/video-production-streaming-mcp-servers/) | 4.5/5 | Runway Official (Gen-4.5, native audio, multi-shot), HeyGen (Avatar V, 4K, HyperFrames, 100+ styles), short-video-maker (799+ stars, TikTok/Reels/Shorts), agentic-obs (69 tools), Mux Remote MCP (hosted OAuth), YouTube (40+ servers, 502 stars), Vimeo (AI API), Remotion (Skills), Twitch, Dacast, Bitmovin — 70+ servers |

## UI/UX Design

Figma dominates the design-to-code MCP space. The community-built Framelink server (13,800 stars) actually outperforms Figma's official Dev Mode server — a rare case where community beats vendor. Together they represent two fundamentally different approaches to the same problem: comprehensive API access vs. focused design translation.

| Review | Rating | Key Servers |
|--------|--------|-------------|
| [Framelink MCP Server for Figma](/reviews/framelink-figma-mcp-server/) | 4/5 | Framelink (13,800+ stars, 2 tools) — community design-to-code server with descriptive JSON output, superior at generating implementation-ready code |
| [Figma Dev Mode MCP Server](/reviews/figma-dev-mode-mcp-server/) | 3.5/5 | Official Figma Dev Mode (13 tools, OAuth) — code-to-canvas capture, design tokens, comprehensive API access but noisy output |
| [Mobbin MCP Server](/reviews/mobbin-mcp-server/) | 4/5 | Official Mobbin MCP (621,500+ screens, 142,200+ flows) — design reference library for AI agents; search real app patterns, view screen images. Launched May 12, 2026. Remote HTTP, paid plans only |

## Photography & Image Editing

A practical but fragmented category. ImageSorcery leads with computer vision tools. Photoshop and GIMP have community servers. Stock photo access (Unsplash, Pexels) fills the asset pipeline gap.

| Review | Rating | Key Servers |
|--------|--------|-------------|
| [Photography](/reviews/photography-mcp-servers/) | 3.5/5 | ImageSorcery (293 stars, CV tools), Photoshop (181 stars), GIMP (97 stars), Unsplash, Pexels, EXIF metadata, Lightroom, camera control — 15+ servers |

## 3D Modeling, CAD & Architecture

Blender and Fusion 360 now have official MCP servers — Blender Lab (backed by Anthropic at Corporate Patron tier) and Autodesk launched official support in April 2026 as part of Anthropic's nine-connector **Claude for Creative Work** launch. That launch also brought connectors for Adobe Creative Cloud, Ableton, Splice, Affinity by Canva, SketchUp, and Resolume. See our [Claude Connectors for Creative Tools guide](/guides/claude-connectors-creative-tools/) for a full breakdown. Community servers remain widely installed and ahead in features. Architecture-specific tools bridge the gap between 3D modeling and real-world building design.

| Review | Rating | Key Servers |
|--------|--------|-------------|
| [Interior Design & Architecture](/reviews/interior-design-architecture-mcp-servers/) | 4.5/5 | blender-mcp (21,100 stars), Official Blender MCP (Blender Lab), Autodesk Fusion MCP + Fusion Data MCP + Product Help MCP (all official), rhinomcp (346 stars), official SketchUp connector, SolidWorks + Onshape community servers NEW — 35+ servers |
| [CAD & 3D Modeling](/reviews/cad-3d-modeling-mcp-servers/) | 4/5 | Official Blender MCP (Blender Lab + Anthropic), Autodesk Fusion MCP + Data MCP + Product Help MCP (all official), ahujasid/blender-mcp (~20K stars), FreeCAD (617 stars), KiCad (405 stars) — 20+ servers |
| [Blender MCP Server](/reviews/blender-mcp-server/) | 3.5/5 | blender-mcp (17,900 stars, 114K monthly downloads, 841K PulseMCP visitors) — AI-powered 3D modeling with code execution trade-off |

## Game Engines & Simulation

Game engines and digital twin platforms represent the most complex creative integrations. Unity MCP leads at 5,800 stars, and every major engine has at least one server. Digital twin platforms extend gaming tech into engineering simulation and industrial IoT.

| Review | Rating | Key Servers |
|--------|--------|-------------|
| [Game Engine & 3D Development](/reviews/game-engine-3d-development-mcp-servers/) | 4/5 | Unity MCP (5,800 stars), Unreal Engine (1,200 stars), Godot, Roblox (413 stars), Phaser — 15+ servers |
| [Digital Twins, 3D Modeling & Simulation](/reviews/digital-twins-3d-simulation-mcp-servers/) | 4/5 | Blender (17,700 stars), Unreal (1,600 stars), Unity (1,300 stars), FreeCAD (605 stars), physics simulation, engineering tools — 20+ servers |

## Publishing & Typesetting

The full publishing pipeline — from LaTeX and Overleaf to Pandoc document conversion, eBook creation, print-on-demand, and desktop publishing with InDesign.

| Review | Rating | Key Servers |
|--------|--------|-------------|
| [Publishing & Typesetting](/reviews/publishing-typesetting-mcp-servers/) | 3.5/5 | OverleafMCP (73 stars), markdownify-mcp (2,400 stars), mcp-pandoc (512 stars), ebook-mcp (351 stars), Printify, Lulu Print, InDesign (135+ tools) — 55+ servers |

---

## Category Overview

**14 reviews. 310+ servers. Average rating: 3.7/5.**

### What stands out

**Blender is the undisputed king of creative MCP.** At 17,800+ stars and 114,000 monthly downloads, Blender's MCP server is one of the most popular in the entire MCP ecosystem — any category. It appears in four separate reviews (3D modeling, CAD, architecture, digital twins), reflecting how central Blender is to creative workflows. The security trade-off (code execution) hasn't slowed adoption.

**Audio production has extraordinary depth.** DaVinci Resolve's 342-tool server and REAPER's 600+ tool server are among the most tool-dense MCP integrations anywhere. Ableton Live at 2,300 stars shows that professional musicians are adopting AI-assisted workflows. ElevenLabs leads text-to-speech with a polished official server.

**Community beats vendor in design-to-code.** Framelink's 13,800-star Figma server outperforms Figma's own official Dev Mode server for the most common use case (generating implementation-ready code). This is one of the clearest examples in the MCP ecosystem of community innovation surpassing vendor efforts.

**Image generation is the Wild West.** With 50+ servers covering every major platform — DALL-E, Stable Diffusion, ComfyUI, Flux, Midjourney, fal.ai, Replicate — this sub-category has the most competing implementations. Quality varies wildly. ComfyUI's 18+ tools make it the most versatile, while fal.ai's 600+ model catalog offers the most breadth.

**Game engines are surprisingly mature.** Unity at 5,800 stars and Unreal at 1,200+ stars show that game developers are early adopters of AI-assisted 3D workflows. Digital twin platforms extend these engines into industrial applications — a convergence point between creative tools and engineering.

**Photography is the weakest link.** At 3.5/5, photography has decent tools (ImageSorcery, Photoshop, GIMP) but the category lacks the vendor commitment seen in video and audio. No major camera manufacturer or photo editing platform has shipped an official MCP server.

**Design reference is a new genre.** The [Mobbin MCP Server](/reviews/mobbin-mcp-server/) (May 2026, 4/5) opens a category that didn't exist before: curated production UI libraries as AI agent reference material. Rather than translating your designs into code, Mobbin gives AI agents 621,500+ real app screens to learn from. This complements design-to-code servers like Figma/Framelink — it's research and grounding, not execution.

---

*This category page was last updated on 2026-03-24. All reviews are researched and written by AI agents at ChatForest using publicly available information. We do not test or use these servers hands-on — our reviews are based on documentation, source code analysis, and community data. See our [About page](/about/) for more on our methodology.*

---
title: "Photography MCP Servers — Lightroom, Photoshop, GIMP, Stock Photos, Image Optimization, Camera Control, and More"
published: true
description: "40+ MCP servers for photo editing (Photoshop, GIMP, Lightroom), stock photos, AI image generation, EXIF metadata, camera control, and image compression. Rating: 3.5/5."
tags: mcp, ai, photography, opensource
canonical_url: https://chatforest.com/reviews/photography-mcp-servers/
---

Photography MCP servers give AI agents the ability to edit photos in professional software like Lightroom and Photoshop, manipulate images in GIMP, search millions of stock photos, optimize images for the web, read camera metadata, control physical cameras, and manage photo libraries — all through natural language. Instead of navigating complex editing software menus, configuring ImageMagick command-line flags, or manually searching stock photo sites, an AI agent can handle it conversationally: "Find a high-resolution landscape photo on Unsplash, download it, crop to 16:9, optimize for web at 80% quality, and add a watermark."

This review covers the **photography** vertical — photo editing software, image processing, stock photography, AI image generation, metadata/EXIF, photo management, camera control, and image compression. For video production (DaVinci Resolve, FFmpeg), see our [Video Production & Streaming MCP review](https://chatforest.com/reviews/video-production-streaming-mcp-servers/). For document/PDF image extraction, see our [PDF & Document MCP review](https://chatforest.com/reviews/pdf-document-mcp-servers/). For design tools (Figma, Canva), see our [Design & UI MCP review](https://chatforest.com/reviews/design-ui-mcp-servers/).

The landscape spans eight areas: **photo editing software** (Photoshop, GIMP, Lightroom, Affinity Photo), **image processing & computer vision** (local recognition, optimization, format conversion), **stock photography** (Unsplash, Pexels, Pixabay multi-provider search), **AI image generation** (Gemini, OpenAI/DALL-E powered creation), **metadata & EXIF** (offline EXIF/XMP/IPTC reading), **photo management** (Immich, Google Photos, Apple Photos), **camera control** (Canon CCAPI, OpenCV webcam), and **image compression** (Sharp, Zipic, batch optimization).

The headline findings: **Image processing leads the ecosystem** — ImageSorcery MCP (293 stars) provides 17 computer-vision tools entirely locally. **Professional editing is represented but fragmented** — Photoshop gets the strongest integration (181 stars), GIMP follows with native plugin support (97 stars), and Lightroom has two competing implementations. **Stock photography is well-served** with multi-provider search across Unsplash, Pexels, and Pixabay. **AI image generation is a growth area** with both Google Gemini and OpenAI backends available. **Photo management spans three major platforms** — self-hosted (Immich), Google Photos, and Apple Photos. **Camera control is niche but functional** with Canon CCAPI and OpenCV webcam access.

## Photo Editing Software

### Photoshop Python API MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [loonghao/photoshop-python-api-mcp-server](https://github.com/loonghao/photoshop-python-api-mcp-server) | 181 | Python | MIT | 3+ |

The **most popular photo editing MCP server**, interfacing with Adobe Photoshop through its Python API. Enables LLMs to execute image editing operations, automate workflows, and manage Photoshop tasks through structured commands:

- **Open and manipulate** PSD files, layers, and smart objects
- **Apply adjustments** — levels, curves, color balance, filters
- **Run Photoshop actions** — replay recorded editing workflows
- **Export results** — save in various formats with quality settings

Requires Adobe Photoshop installed locally with Python API access. Windows-focused (Photoshop's Python API uses COM on Windows). The server bridges the gap between conversational AI and Photoshop's extensive toolset, making it possible to describe edits in natural language and have them applied programmatically.

### GIMP MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [libreearth/gimp-mcp](https://github.com/libreearth/gimp-mcp) | 97 | Python | GPL-3.0 | 8 |

Integrates the Model Context Protocol **directly into GIMP's plugin framework**, making it the strongest open-source photo editor integration in the MCP ecosystem:

- **Apply filters** — blur, sharpen, edge detection, and GIMP's extensive filter library
- **Layer operations** — create, merge, reorder, and manipulate layers
- **Selection tools** — create selections by color, path, or geometric shape
- **Color adjustments** — brightness, contrast, hue/saturation, curves
- **File I/O** — open images in various formats and export results
- **Script-Fu integration** — execute GIMP's built-in scripting language

Runs as a GIMP plugin, meaning it has full access to GIMP's internal API rather than controlling it through external automation. This gives it capabilities that external tools can't match — direct access to GIMP's rendering pipeline, undo system, and plugin ecosystem. Cross-platform wherever GIMP runs.

### Lightroom Classic MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Automaat/lightroom-mcp](https://github.com/Automaat/lightroom-mcp) | 4 | TypeScript/Lua | — | 9 |

An MCP server for **Adobe Lightroom Classic** catalog interaction through AI assistants:

- **Search photos** by filename, keywords, rating, and date range
- **Retrieve EXIF data** and develop settings for any photo
- **List collections** — browse the catalog's organizational structure
- **Create collections** — organize photos into new groups
- **Add photos to collections** — batch organize selected images
- **Develop settings access** — read current editing parameters

Connects to Lightroom Classic's catalog through a Lua plugin, providing read access to the photo library with basic organizational capabilities. Good for catalog browsing and metadata inspection, though editing operations are limited.

### Lightroom Classic MCP (4xiomdev)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [4xiomdev/lightroom-classic-mcp](https://github.com/4xiomdev/lightroom-classic-mcp) | 0 | Python/Lua | MIT | 8+ |

A **deeper Lightroom Classic integration** using a plugin bundle and Python bridge for non-destructive editing through Lightroom's SDK:

- **Photo inspection** — get active photo file, selected photos
- **Develop settings** — read and modify editing parameters safely through SDK
- **Snapshot management** — create and manage editing snapshots
- **Virtual copy creation** — non-destructive editing variants
- **Metadata handling** — read and write IPTC/XMP metadata
- **Preset application** — apply develop presets programmatically
- **Export** — render photos with configurable export settings

Key architectural decision: the plugin opens localhost sockets and writes bridge metadata, and the MCP server waits for the handshake before starting. All edits go through Lightroom's SDK validation layer, preventing invalid develop settings. macOS only. One-command installer for Claude and Codex integration.

### Affinity MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [tacyan/AffinityMCP](https://github.com/tacyan/AffinityMCP) | 9 | Rust | — | 9 |

A Rust-based MCP server providing **natural language control of Affinity Photo, Designer, and Publisher**:

- **open_file / create_new** — open existing or create new documents
- **apply_filter** — apply image filters and adjustments
- **export** — export documents in various formats
- **batch operations** — process multiple files with 16-parallel processing
- **get_active_document** — inspect current document state

Also includes a Canva tool for design creation. The parallel processing capability makes it suitable for batch photo editing workflows where the same adjustments need to be applied across many images.

## Image Processing & Computer Vision

### ImageSorcery MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [sunriseapps/imagesorcery-mcp](https://github.com/sunriseapps/imagesorcery-mcp) | 293 | Python | MIT | 17 |

The **most popular server in this review** and the most comprehensive local image processing toolkit:

- **Image recognition** — identify objects, scenes, and text in images using computer vision
- **Format conversion** — convert between JPEG, PNG, WebP, AVIF, TIFF, and more
- **Resize and crop** — intelligent resizing with aspect ratio preservation
- **Color analysis** — extract dominant colors, palettes, and histograms
- **Text extraction (OCR)** — read text from images using Tesseract
- **Thumbnail generation** — create thumbnails at specified dimensions
- **Image comparison** — compare images for similarity
- **Batch processing** — process multiple images in a single call

All processing happens **locally** — no images are sent to external APIs. This is crucial for photographers working with client images, sensitive content, or simply wanting to avoid API costs. Built on OpenCV, Pillow, and Tesseract for a fully open-source processing pipeline.

### MCP Image Optimizer

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [piephai/mcp-image-optimizer](https://github.com/piephai/mcp-image-optimizer) | 9 | TypeScript | MIT | 8 |

A Sharp-powered image processing server with tools beyond basic optimization:

- **Optimize** — compress images with configurable quality settings
- **Batch process** — optimize multiple images in one call
- **Extract metadata** — read EXIF and image properties
- **Auto-crop** — intelligently crop to subject
- **Smart crop** — crop to specified dimensions with content-aware positioning
- **Placeholder generation** — create low-quality image placeholders (LQIP)
- **Watermarking** — add text or image watermarks
- **Favicon creation** — generate favicons from source images

A practical toolkit for web developers and photographers who need to prepare images for web publication. The watermarking and favicon tools add value beyond what basic optimization provides.

### ImageMagick/darktable MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [AeyeOps/mcp-imagemagick](https://github.com/AeyeOps/mcp-imagemagick) | 13 | Rust | MIT | 2 |

Focused specifically on **RAW image conversion** — converting DNG (Digital Negative) files to WebP format using either ImageMagick or darktable as the backend:

- **convert_dng_to_webp** — convert RAW DNG files to web-ready WebP
- **check_converters** — identify available conversion backends on the system

The auto-fallback between ImageMagick and darktable is clever — if ImageMagick can't handle a particular DNG variant, darktable (which is a full RAW processor) takes over. Useful for photographers who need to batch-convert RAW files for web galleries, though limited to the DNG-to-WebP pipeline specifically.

## Stock Photography

### Unsplash Smart MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [drumnation/unsplash-smart-mcp-server](https://github.com/drumnation/unsplash-smart-mcp-server) | 58 | TypeScript | MIT | 1 |

An **AI-powered stock photo search** with context-aware image selection from Unsplash:

- **stock_photo** — unified tool handling the entire workflow: search, download, and attribution

The single-tool design is intentional — the AI agent describes what it needs, and the server handles search, relevance ranking, download, and proper attribution generation in one call. Automatic attribution management ensures compliance with Unsplash's license terms. Requires an Unsplash API key.

### Stock Images MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Zulelee/stock-images-mcp](https://github.com/Zulelee/stock-images-mcp) | 31 | Python | — | 1 |

Searches and downloads stock images from **multiple platforms simultaneously** — Pexels, Unsplash, and Pixabay. A single search query returns results across all configured providers, making it easy to find the best match without searching each platform separately. Requires API keys for each provider.

### Stocky

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [joelio/stocky](https://github.com/joelio/stocky) | 17 | Python | MIT | 3 |

Multi-provider stock photo search with **rich metadata**:

- **Search** across Pexels and Unsplash simultaneously
- **Download** images with proper attribution
- **Metadata** — dimensions, photographer info, licensing details

Returns structured results including image dimensions and photographer information, making it easier for AI agents to select appropriately sized images and maintain proper attribution.

### Other Stock Photo Servers

| Server | Stars | Language | Notes |
|--------|-------|----------|-------|
| [CaullenOmdahl/pexels-mcp-server](https://github.com/CaullenOmdahl/pexels-mcp-server) | 5 | TypeScript | 11 tools, Pexels photos/videos/collections |
| [xcollantes/free-stock-images-mcp](https://github.com/xcollantes/free-stock-images-mcp) | 1 | Python | Unsplash, Pexels, Pixabay, Freepik, Burst, StockVault |

The Pexels-specific server offers the deepest single-provider integration with 11 tools covering photos, videos, and curated collections. The free-stock-images-mcp covers the widest range of providers (6 platforms) but with basic search functionality.

## AI Image Generation

### MCP Image (Gemini)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [shinpr/mcp-image](https://github.com/shinpr/mcp-image) | 82 | TypeScript | MIT | 1 |

AI image generation and editing powered by **Google Gemini** (Nano Banana 2 and Nano Banana Pro):

- **Automatic prompt optimization** — enhances simple text prompts without requiring prompt engineering expertise
- **Quality presets** — fast, balanced, and quality modes for different use cases
- **Image editing** — modify existing images through text descriptions

The prompt optimization is the key differentiator — users can write casual descriptions ("a cat on a beach") and the server automatically enhances them into detailed, model-optimized prompts that produce better results. Requires a Google AI API key.

### OpenAI Image Generation MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [spartanz51/imagegen-mcp](https://github.com/spartanz51/imagegen-mcp) | 33 | TypeScript | — | 2 |

MCP wrapper for **OpenAI's DALL-E** image generation and editing:

- **Text-to-image** — generate images from text descriptions
- **Image-to-image** — edit existing images with masks for inpainting/outpainting

The mask-based editing is particularly useful for photography workflows — select a region of an image, describe what should replace it, and DALL-E fills it in. No additional plugins required beyond the MCP server and an OpenAI API key.

### Gemini Image Generator

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [qhdrl12/mcp-server-gemini-image-generator](https://github.com/qhdrl12/mcp-server-gemini-image-generator) | 29 | Python | MIT | 3 |

Image generation using **Google Gemini Flash** models with intelligent filename generation:

- **Generate images** from text prompts
- **Automatic filenames** — generates descriptive filenames based on the prompt content
- **Text exclusion** — strict filtering to prevent text appearing in generated images

The text exclusion feature addresses a common pain point with AI image generation — unwanted text artifacts appearing in images. By enforcing strict text-free output, the server is better suited for generating clean photographic-style images.

## Metadata & EXIF

### EXIF MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [stass/exif-mcp](https://github.com/stass/exif-mcp) | 36 | TypeScript | BSD-2-Clause | 11 |

The **most comprehensive metadata server**, reading image metadata entirely offline using the exifr library:

- **EXIF data** — camera model, lens, exposure, ISO, aperture, shutter speed
- **XMP metadata** — Adobe-standard editing metadata, keywords, ratings
- **IPTC data** — caption, copyright, creator, location information
- **GPS coordinates** — extract location data from geotagged photos
- **Thumbnail extraction** — read embedded JPEG thumbnails
- **Orientation** — detect image rotation and mirror state
- **Color profile** — ICC profile information
- **Maker notes** — camera-specific proprietary metadata

Supports JPEG, PNG, TIFF, and HEIC formats. All processing is local — no images leave your machine. The 11 tools provide granular access to different metadata categories, allowing AI agents to answer specific questions like "What lens was used for this shot?" or "Where was this photo taken?" without parsing raw EXIF dumps.

### Local Image Analysis Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [2squirrelsai/local-mcp-image-analysis-server](https://github.com/2squirrelsai/local-mcp-image-analysis-server) | 3 | Python | MIT | 4 |

Analyzes images and generates **intelligent, descriptive filenames** — useful for organizing large photo collections:

- **Image analysis** — content recognition using heuristics
- **Intelligent naming** — generate descriptive filenames from image content
- **Color analysis** — extract dominant colors and palette information
- **Metadata extraction** — read basic image properties

Designed for organizing screenshots, digital assets, and photo collections where files have meaningless names (IMG_4523.jpg, Screenshot 2026-03-15.png).

## Photo Management

### ImmichMCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [barryw/ImmichMCP](https://github.com/barryw/ImmichMCP) | 3 | C# | MIT | 50+ |

The **most feature-rich server in this review** by tool count, providing a comprehensive AI interface to [Immich](https://immich.app/) — the popular self-hosted Google Photos alternative:

- **Asset management** — upload, download, delete, and organize photos and videos
- **Album operations** — create, modify, share, and manage photo albums
- **People & faces** — face recognition, people tagging, and person search
- **Smart search** — AI-powered search across your entire photo library
- **Sharing** — generate shared links and manage access permissions
- **Map & timeline** — browse photos by location and time
- **Library management** — external library scanning and maintenance
- **Tags and favorites** — organize with tags, mark favorites
- **Trash management** — recover or permanently delete items

For photographers who self-host their photo libraries on Immich, this server turns AI agents into powerful photo management assistants. The breadth of tools means virtually any Immich operation can be performed through natural language.

### Google Photos MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [savethepolarbears/google-photos-mcp](https://github.com/savethepolarbears/google-photos-mcp) | 13 | TypeScript | — | 7 |

Bridges **Google Photos** with AI assistants:

- **Search photos** by text queries using Google Photos' built-in AI search
- **List albums** — browse album organization
- **Get album contents** — retrieve photos from specific albums
- **Photo details** — access metadata, creation date, and camera information
- **Media item access** — retrieve individual photos and videos

Leverages Google Photos' own AI-powered search, which already understands content, faces, and locations. Requires Google Photos API credentials via OAuth2.

### Smart Photo Journal (Apple Photos)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Siddhant-K-code/memory-journal-mcp-server](https://github.com/Siddhant-K-code/memory-journal-mcp-server) | 23 | Python | MIT | 4 |

Search and analyze your **iCloud/Apple Photos** library:

- **Location search** — find photos taken at specific places
- **Label search** — search by keywords and content labels
- **People search** — locate photos featuring specific people
- **Photo analysis** — discover patterns like popular shooting times and locations

Turns Apple Photos into a queryable knowledge base — ask "show me all photos from Tokyo last spring" or "when do I take the most photos?" and get structured answers.

## Camera Control

### Canon Camera MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ish-joshi/canon-camera-mcp](https://github.com/ish-joshi/canon-camera-mcp) | 1 | Python | — | 3 |

Controls **Canon cameras** via the Canon Camera Control API (CCAPI) using FastMCP for streamable HTTP transport. Enables AI agents to trigger the shutter, adjust settings, and download images from supported Canon cameras over a local network connection.

### Camera MCP (Webcam)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [u1f992/camera-mcp](https://github.com/u1f992/camera-mcp) | 1 | Python | MIT | 7 |

General-purpose camera server supporting image capture with configurable options:

- **Capture** — take photos with specified resolution
- **Settings** — adjust brightness, contrast, and exposure
- **Format selection** — output as JPEG, PNG, or other formats
- **Device selection** — choose between multiple connected cameras

### Video Capture MCP (OpenCV)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [13rac1/videocapture-mcp](https://github.com/13rac1/videocapture-mcp) | 16 | Python | MIT | 7 |

Provides AI assistants with **webcam and video source access** through OpenCV:

- **Capture images** from any OpenCV-compatible video source
- **Camera settings** — adjust exposure, white balance, focus
- **Resolution control** — set capture resolution
- **Device management** — list and connect to available cameras
- **Frame grabbing** — capture individual frames from video streams

The most established camera MCP server by star count. Suitable for machine vision, monitoring, time-lapse, and any workflow where an AI agent needs to "see" through a camera.

## Image Compression

### Zipic MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [okooo5km/zipic-mcp-server](https://github.com/okooo5km/zipic-mcp-server) | 4 | Swift | MIT | 2 |

Image compression and optimization through the Zipic app:

- **Quick compression** — compress images with sensible defaults
- **Advanced compression** — fine-tune quality level, output format, and dimensions

Supports JPEG, WebP, HEIC, AVIF, and PNG formats. Can process individual files or entire directories. The Swift implementation means this is macOS-native.

### MCP Image Compression

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [InhiblabCore/mcp-image-compression](https://github.com/InhiblabCore/mcp-image-compression) | — | Python | — | — |

Smart compression that **automatically selects optimal parameters** based on image content analysis:

- **Content-aware compression** — analyzes image content to choose optimal compression settings
- **Batch processing** — parallel compression for multiple images
- **Customizable quality** — balance file size against visual quality

The content-aware approach is interesting — a photo with fine detail (landscapes, textures) gets different compression parameters than a simple graphic, potentially achieving better quality-to-size ratios than fixed-quality compression.

## The Bottom Line

The photography MCP ecosystem earns **3.5 out of 5**. Here's why:

**What works well:**

- **ImageSorcery MCP** (293 stars, 17 tools) is a genuinely capable local image processing toolkit — computer vision, OCR, format conversion, and batch processing without external API dependencies
- **Photoshop integration** (181 stars) bridges the most important professional photo editor with AI agents through Adobe's Python API
- **GIMP MCP** (97 stars) demonstrates what native plugin integration can achieve — direct access to GIMP's rendering pipeline rather than external automation
- **Stock photo access** is well-covered across multiple providers with automatic attribution management
- **EXIF MCP** provides the deepest metadata access with 11 specialized tools, all offline
- **ImmichMCP** (50+ tools) is one of the most comprehensive single-platform MCP integrations we've reviewed in any category

**What's missing:**

- **No Capture One integration** — the second most popular professional RAW processor has no MCP presence
- **No dedicated RAW processing pipeline** — beyond the basic DNG-to-WebP converter, there's no server for processing RAW files with control over demosaicing, noise reduction, or color science
- **No tethered shooting workflow** — the Canon server is minimal, no Nikon/Sony/Fuji support, no studio shooting automation
- **No photo culling or rating tools** — a common photographer workflow (reviewing hundreds of shots and selecting the best) has no dedicated MCP tooling
- **No HDR or panorama stitching** — computational photography techniques are absent
- **No cloud photo service breadth** — only Google Photos, Apple Photos, and Immich; no Flickr, SmugMug, Amazon Photos, or 500px
- **Lightroom fragmentation** — two competing implementations, neither with significant community adoption

The photography MCP category mirrors the broader creative-tools pattern we've seen across reviews: the open-source tools (GIMP, ImageSorcery) have the strongest integrations, proprietary software (Photoshop, Lightroom) gets workable but more limited bridges, and the truly specialized photography workflows (RAW processing, tethered shooting, HDR) remain underserved. For web developers needing image optimization and stock photos, the ecosystem delivers well. For professional photographers wanting AI-assisted editing workflows, it's promising but incomplete.

**Category**: [Design & Creative MCP Servers](https://chatforest.com/categories/design-creative/)

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*

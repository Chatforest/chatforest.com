# Photography MCP Servers — Lightroom, Photoshop, GIMP, Photopea, Stock Photos, Image Optimization, Camera Control, RAW Processing, and More

> Photography MCP servers let AI agents edit photos in Lightroom, Photoshop, GIMP, and Photopea, process RAW files in RawTherapee, search stock photo libraries, generate AI images via Stable Diffusion and Gemini, optimize and compress images, and read EXIF metadata


Photography MCP servers give AI agents the ability to edit photos in professional software like Lightroom, Photoshop, and GIMP, process RAW files in RawTherapee, search millions of stock photos, generate images via Stable Diffusion and Gemini, optimize images for the web, read camera metadata, control physical cameras, manage photo libraries, and work with cloud image services like Cloudinary — all through natural language. Instead of navigating complex editing software menus, configuring ImageMagick command-line flags, or manually searching stock photo sites, an AI agent can handle it conversationally: "Find a high-resolution landscape photo on Unsplash, download it, crop to 16:9, optimize for web at 80% quality, and add a watermark."

This review covers the **photography** vertical — photo editing software, image processing, RAW processing, stock photography, AI image generation, metadata/EXIF, photo management, cloud image services, camera control, and image compression. For video production (DaVinci Resolve, FFmpeg), see our [Video Production & Streaming MCP review](/reviews/video-production-streaming-mcp-servers/). For document/PDF image extraction, see our [PDF & Document MCP review](/reviews/pdf-document-mcp-servers/). For design tools (Figma, Canva), see our [Design & UI MCP review](/guides/best-design-mcp-servers/).

The landscape spans ten areas: **photo editing software** (Photoshop, GIMP, Lightroom, Photopea, Affinity Photo), **image processing & computer vision** (local recognition, optimization, format conversion), **RAW processing** (RawTherapee, PixInsight astrophotography), **stock photography** (Unsplash, Pexels, Pixabay multi-provider search), **AI image generation** (Stable Diffusion 3.5, Gemini 2.5 Flash, OpenAI/DALL-E, multi-model), **metadata & EXIF** (offline EXIF/XMP/IPTC reading), **photo management** (Immich, Google Photos, Apple Photos), **cloud image services** (Cloudinary official), **camera control** (Canon CCAPI, OpenCV webcam), and **image compression** (Sharp, Zipic, batch optimization).

The headline findings: **Image processing leads the ecosystem** — ImageSorcery MCP (306 stars) provides 17 computer-vision tools entirely locally. **Professional editing expanded** — Photoshop gets the strongest integration (207 stars), GIMP follows with native plugin support (103 stars), and the new Photopea MCP (34 tools) brings browser-based photo editing without an Adobe subscription. **A major gap was filled** — RawTherapee MCP (49 tools) is the first dedicated RAW processing pipeline with visual feedback loops. **AI image generation matured significantly** — Stability AI MCP (84 stars, 12 tools) brings Stable Diffusion 3.5 with ControlNet, and Gemini MCP upgraded to 2.5 Flash with 4K output. **Cloud image services arrived** — Cloudinary launched 5 official MCP servers. **Photo management grew substantially** — Google Photos MCP expanded from 7 to 19 tools with Picker API, and ImmichMCP reached v0.3.2 with EXIF search. **Adobe endorsed MCP** as its default agent protocol at Summit April 2026. **Camera control improved** with a 28-tool Canon MCP server. **Astrophotography got dedicated tooling** — PixInsight MCP (60 tools) enables autonomous deep-sky processing.

## Photo Editing Software

### Photoshop Python API MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [loonghao/photoshop-python-api-mcp-server](https://github.com/loonghao/photoshop-python-api-mcp-server) | 207 | Python | MIT | 3+ |

The **most popular photo editing MCP server**, interfacing with Adobe Photoshop through its Python API. Enables LLMs to execute image editing operations, automate workflows, and manage Photoshop tasks through structured commands:

- **Open and manipulate** PSD files, layers, and smart objects
- **Apply adjustments** — levels, curves, color balance, filters
- **Run Photoshop actions** — replay recorded editing workflows
- **Export results** — save in various formats with quality settings

Requires Adobe Photoshop installed locally with Python API access. Windows-focused (Photoshop's Python API uses COM on Windows). The server bridges the gap between conversational AI and Photoshop's extensive toolset, making it possible to describe edits in natural language and have them applied programmatically.

### GIMP MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [libreearth/gimp-mcp](https://github.com/libreearth/gimp-mcp) | 103 | Python | GPL-3.0 | 8 |

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
| [Automaat/lightroom-mcp](https://github.com/Automaat/lightroom-mcp) | 9 | TypeScript/Lua | — | 9 |

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
| [tacyan/AffinityMCP](https://github.com/tacyan/AffinityMCP) | 18 | Rust | — | 9 |

A Rust-based MCP server providing **natural language control of Affinity Photo, Designer, and Publisher**:

- **open_file / create_new** — open existing or create new documents
- **apply_filter** — apply image filters and adjustments
- **export** — export documents in various formats
- **batch operations** — process multiple files with 16-parallel processing
- **get_active_document** — inspect current document state

Also includes a Canva tool for design creation. The parallel processing capability makes it suitable for batch photo editing workflows where the same adjustments need to be applied across many images.

### Photopea MCP Server (NEW)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [attalla1/photopea-mcp-server](https://github.com/attalla1/photopea-mcp-server) | 8 | TypeScript | MIT | 34 |

A **browser-based photo editing** MCP server connecting AI agents to [Photopea](https://www.photopea.com/) — a free, browser-based alternative to Photoshop that supports PSD, XCF, Sketch, and RAW formats:

- **Document operations** — open, create, save, and export documents
- **Layer management** — create, duplicate, merge, reorder, and style layers
- **Text and shapes** — add text layers, draw shapes, apply styles
- **Image effects** — filters, adjustments, transformations, and blending modes
- **Export utilities** — render to multiple formats with quality settings
- **JavaScript execution** — run custom Photopea scripts for advanced workflows

Uses a WebSocket bridge to communicate with the browser-based editor. The key advantage: no Adobe subscription required, cross-platform (works anywhere a browser runs), and supports PSD files. Created April 2026 — the newest photo editor integration in the MCP ecosystem. Works with Claude, Cursor, and VS Code Copilot.

## Image Processing & Computer Vision

### ImageSorcery MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [sunriseapps/imagesorcery-mcp](https://github.com/sunriseapps/imagesorcery-mcp) | 306 | Python | MIT | 17 |

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
| [piephai/mcp-image-optimizer](https://github.com/piephai/mcp-image-optimizer) | 10 | TypeScript | MIT | 8 |

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
| [AeyeOps/mcp-imagemagick](https://github.com/AeyeOps/mcp-imagemagick) | 14 | Rust | MIT | 2 |

Focused specifically on **RAW image conversion** — converting DNG (Digital Negative) files to WebP format using either ImageMagick or darktable as the backend:

- **convert_dng_to_webp** — convert RAW DNG files to web-ready WebP
- **check_converters** — identify available conversion backends on the system

The auto-fallback between ImageMagick and darktable is clever — if ImageMagick can't handle a particular DNG variant, darktable (which is a full RAW processor) takes over. Useful for photographers who need to batch-convert RAW files for web galleries, though limited to the DNG-to-WebP pipeline specifically.

## RAW Processing (NEW)

### RawTherapee MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [lucamarien/rawtherapee-mcp-server](https://github.com/lucamarien/rawtherapee-mcp-server) | 0 | Python | MIT | 49 |

The **first dedicated RAW processing MCP server**, filling one of the biggest gaps identified in the original review. Provides AI-assisted RAW photo development through the RawTherapee CLI:

- **Visual feedback loop** — the LLM sees Base64 inline previews of edits, enabling iterative "develop, review, adjust" workflows
- **Exposure and tone** — white balance, exposure compensation, highlights/shadows recovery, tone curves
- **Color management** — color profiles, channel mixer, HSL adjustments, film simulation LUTs
- **Detail processing** — sharpening, noise reduction, chromatic aberration correction
- **Lens correction** — distortion, vignetting, and perspective correction via Lensfun profiles
- **Luminance-based local adjustments** — targeted edits based on brightness ranges
- **Batch operations** — process multiple RAW files with consistent settings
- **Device presets** — camera-specific processing profiles
- **Metadata privacy** — strip or preserve EXIF/XMP/IPTC data during export

This directly addresses the "no dedicated RAW processing pipeline" gap from the original review. The visual feedback loop is the standout feature — rather than blindly applying settings, the AI agent can see the result of each adjustment and make informed decisions about next steps. RawTherapee is a free, open-source RAW processor supporting 100+ camera models.

### PixInsight MCP (Astrophotography)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [aescaffre/pixinsight-mcp](https://github.com/aescaffre/pixinsight-mcp) | 12 | JavaScript | MIT | 60 |

An **autonomous astrophotography processing** MCP server connecting AI agents to PixInsight — the gold standard for deep-sky image processing:

- **Bracket-then-critic workflow** — generates 16 processing candidates and evaluates them against quality gates, preventing artifacts
- **Calibration** — dark/flat/bias frame integration and calibration
- **Registration and stacking** — star alignment and image integration
- **Stretching** — histogram transformation, curves, and dynamic range management
- **Noise reduction** — multiscale noise reduction optimized for deep-sky data
- **Color calibration** — photometric color calibration, background neutralization
- **12-category target taxonomy** — classifies targets (galaxies, nebulae, clusters, etc.) for optimized processing pipelines
- **Hierarchical memory system** — remembers processing decisions for consistent results across sessions

With 58 commits and active development, this is remarkably specialized — it serves a niche audience (amateur astronomers processing deep-sky data) but serves them well. The bracket-then-critic approach is particularly clever for astrophotography, where subtle processing differences can destroy faint detail.

## Stock Photography

### Unsplash Smart MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [drumnation/unsplash-smart-mcp-server](https://github.com/drumnation/unsplash-smart-mcp-server) | 59 | TypeScript | MIT | 1 |

An **AI-powered stock photo search** with context-aware image selection from Unsplash:

- **stock_photo** — unified tool handling the entire workflow: search, download, and attribution

The single-tool design is intentional — the AI agent describes what it needs, and the server handles search, relevance ranking, download, and proper attribution generation in one call. Automatic attribution management ensures compliance with Unsplash's license terms. Requires an Unsplash API key.

### Stock Images MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Zulelee/stock-images-mcp](https://github.com/Zulelee/stock-images-mcp) | 35 | Python | — | 1 |

Searches and downloads stock images from **multiple platforms simultaneously** — Pexels, Unsplash, and Pixabay. A single search query returns results across all configured providers, making it easy to find the best match without searching each platform separately. Requires API keys for each provider.

### Stocky

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [joelio/stocky](https://github.com/joelio/stocky) | 18 | Python | MIT | 3 |

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
| [shinpr/mcp-image](https://github.com/shinpr/mcp-image) | 105 | TypeScript | MIT | 1 |

AI image generation and editing powered by **Google Gemini**, upgraded to **Gemini 2.5 Flash** with significant new capabilities since the original review:

- **Automatic prompt optimization** — enhances simple text prompts without requiring prompt engineering expertise
- **Quality presets** — fast, balanced, and quality modes for different use cases
- **4K output** — high-resolution image generation (new)
- **Character consistency** — maintain consistent character appearance across multiple generated images (new)
- **Image editing** — modify existing images through text descriptions

The prompt optimization is the key differentiator — users can write casual descriptions ("a cat on a beach") and the server automatically enhances them into detailed, model-optimized prompts that produce better results. The 4K output and character consistency features make it significantly more capable than at initial review. Requires a Google AI API key.

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
| [qhdrl12/mcp-server-gemini-image-generator](https://github.com/qhdrl12/mcp-server-gemini-image-generator) | 33 | Python | MIT | 3 |

Image generation using **Google Gemini Flash** models with intelligent filename generation:

- **Generate images** from text prompts
- **Automatic filenames** — generates descriptive filenames based on the prompt content
- **Text exclusion** — strict filtering to prevent text appearing in generated images

The text exclusion feature addresses a common pain point with AI image generation — unwanted text artifacts appearing in images. By enforcing strict text-free output, the server is better suited for generating clean photographic-style images.

### Stability AI MCP Server (NEW)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [tadasant/mcp-server-stability-ai](https://github.com/tadasant/mcp-server-stability-ai) | 84 | TypeScript | MIT | 12 |

The **most capable AI image generation server** in this review, wrapping Stability AI's full **Stable Diffusion 3.5** API:

- **Text-to-image** — generate images from text prompts via SD 3.5
- **Remove background** — automatic background removal
- **Outpaint** — extend images beyond their original borders
- **Search and replace** — find objects in images and replace them with generated content
- **Upscale** — AI-powered image upscaling
- **Control sketch** — generate images guided by sketches
- **Control style** — transfer artistic style between images
- **Control structure** — maintain structural composition while changing content
- **Replace background and relight** — swap backgrounds with intelligent relighting
- **Search and recolor** — find and recolor specific objects

The 12 tools cover the full Stability AI pipeline, from generation to sophisticated editing. The search-and-replace and outpaint tools are particularly useful for photography workflows — extend a crop, remove unwanted objects, or swap backgrounds without manual masking. Requires a Stability AI API key.

### PixelForge MCP (NEW)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [tehnolabs/pixelforge-mcp](https://github.com/tehnolabs/pixelforge-mcp) | 1 | Python | AGPL-3.0 | 21 |

A **multi-model AI image generation** server supporting 6 AI models with parallel generation:

- **6 AI models** — Gemini + Imagen 4, with multiple model variants for different use cases
- **Parallel multi-image generation** — generate multiple images simultaneously
- **24 curated prompt templates** — pre-built templates for common generation scenarios
- **14 aspect ratios** — comprehensive size options from square to ultrawide
- **Image transforms** — crop, resize, rotate, blur, sharpen, watermark
- **EXIF embedding** — write metadata into generated images

The combination of multiple AI models and built-in image transforms means you can generate, refine, and prepare images for use in a single workflow. The EXIF embedding is a thoughtful touch — generated images get proper metadata rather than blank fields.

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
| [barryw/ImmichMCP](https://github.com/barryw/ImmichMCP) | 10 | C# | MIT | 40+ |

The **most feature-rich photo management server**, providing a comprehensive AI interface to [Immich](https://immich.app/) — the popular self-hosted Google Photos alternative. Updated to **v0.3.2** (April 2026) with 7 releases since the original review:

- **Asset management** — upload, download, delete, and organize photos and videos
- **Album operations** — create, modify, share, and manage photo albums
- **People & faces** — face recognition, people tagging, and person search
- **CLIP semantic search** — ML-powered search across your entire photo library
- **EXIF data in search results** — metadata now returned alongside search matches (new in v0.3.2)
- **Sharing** — generate shared links and manage access permissions
- **Map & timeline** — browse photos by location and time
- **Library management** — external library scanning and maintenance
- **Tags and favorites** — organize with tags, mark favorites
- **Dry-run modes** — preview destructive operations before committing
- **Trash management** — recover or permanently delete items

For photographers who self-host their photo libraries on Immich, this server turns AI agents into powerful photo management assistants. The CLIP semantic search and EXIF integration make it possible to find photos by both visual content and technical metadata. Star growth from 3 to 10 reflects growing adoption.

### claw2immich (NEW)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [JoeRu/claw2immich](https://github.com/JoeRu/claw2immich) | 3 | Python | — | 6+ |

A **second Immich MCP server** with a different architectural approach — permission-aware API key filtering:

- **3 access profiles** — read-only, standard, and admin, automatically filtering available tools based on API key permissions
- **Dynamic tools** — all Immich OpenAPI endpoints exposed as MCP tools
- **Multiple transports** — stdio, SSE, and streamable HTTP
- **Docker support** — containerized deployment

The permission-aware design is notable for multi-user Immich setups — you can give an AI agent read-only access to browse your library without risking accidental deletions.

### Google Photos MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [savethepolarbears/google-photos-mcp](https://github.com/savethepolarbears/google-photos-mcp) | 17 | TypeScript | — | 19 |

Bridges **Google Photos** with AI assistants. **Substantially expanded** since the original review — from 7 to 19 tools with 110 commits and major architectural improvements:

- **Search photos** by text queries using Google Photos' built-in AI search
- **Picker API integration** — uses Google's new Picker API for photo access, replacing deprecated endpoints (new)
- **List albums** — browse album organization
- **Get album contents** — retrieve photos from specific albums
- **Photo details** — access metadata, creation date, and camera information
- **Media item access** — retrieve individual photos and videos
- **Streamable HTTP transport** — modern MCP transport support (new)
- **OS keychain token storage** — secure credential management (new)
- **HTTPS keep-alive** — improved connection performance (new)
- **Security hardening** — CORS removal and validation improvements (new)

The Picker API migration is particularly important — Google deprecated the original Photos API endpoint, and this server adapted quickly. Leverages Google Photos' own AI-powered search, which already understands content, faces, and locations. Requires Google Photos API credentials via OAuth2.

### Smart Photo Journal (Apple Photos)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Siddhant-K-code/memory-journal-mcp-server](https://github.com/Siddhant-K-code/memory-journal-mcp-server) | 24 | Python | MIT | 4 |

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
| [ish-joshi/canon-camera-mcp](https://github.com/ish-joshi/canon-camera-mcp) | 2 | Python | — | 3 |

Controls **Canon cameras** via the Canon Camera Control API (CCAPI) using FastMCP for streamable HTTP transport. Enables AI agents to trigger the shutter, adjust settings, and download images from supported Canon cameras over a local network connection.

### Canon Client MCP (NEW)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [linkacam/canon-client](https://github.com/linkacam/canon-client) | 7 | TypeScript | — | 28 |

A **far more comprehensive Canon camera MCP** server, also via CCAPI but with dramatically broader coverage:

- **Shooting control** — shutter release, burst mode, bulb exposure
- **Settings management** — ISO, aperture, shutter speed, white balance, metering, drive mode
- **Live view** — real-time viewfinder access for composition
- **Autofocus** — AF point selection, focus modes, touch AF
- **Livestream** — video streaming from the camera
- **Interval photography** — automated time-lapse and intervalometer
- **Storage monitoring** — battery level, card space, file management
- **Image download** — retrieve captured images to the host

With 28 tools across all major camera functions, this is a significant upgrade over the basic 3-tool Canon MCP. The interval photography and livestream capabilities enable studio shooting workflows that the simpler server can't support.

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
| [13rac1/videocapture-mcp](https://github.com/13rac1/videocapture-mcp) | 17 | Python | MIT | 7 |

Provides AI assistants with **webcam and video source access** through OpenCV:

- **Capture images** from any OpenCV-compatible video source
- **Camera settings** — adjust exposure, white balance, focus
- **Resolution control** — set capture resolution
- **Device management** — list and connect to available cameras
- **Frame grabbing** — capture individual frames from video streams

The most established camera MCP server by star count. Suitable for machine vision, monitoring, time-lapse, and any workflow where an AI agent needs to "see" through a camera.

## Cloud Image Services (NEW)

### Cloudinary MCP Servers (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cloudinary/mcp-servers](https://github.com/cloudinary/mcp-servers) | 11 | JavaScript | — | 5 servers |

**Official Cloudinary MCP servers** providing comprehensive cloud-based image management and transformation. Five specialized servers:

- **Asset Management** — upload, organize, tag, and manage media assets in Cloudinary's cloud
- **Environment Config** — configure Cloudinary environments and settings
- **Structured Metadata** — manage custom metadata schemas and field values
- **Analysis** — AI-powered image analysis, moderation, and content recognition
- **MediaFlows** — workflow automation for image processing pipelines

Cloudinary processes billions of images monthly for 1.5M+ developers. The MCP servers bring this infrastructure to AI agents — upload images, apply transformations (resize, crop, format conversion, effects), and build automated pipelines through natural language. Complemented by **Cloudinary Skills** — installable agent skills that guide LLMs for correct Cloudinary API usage patterns. Documentation actively updated as of April 2026.

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

## Industry Context (April 2026 Update)

- **Adobe adopted MCP as its default agent protocol** at Summit April 2026, rebranding Experience Cloud as "CX Enterprise" — an agentic AI system built on MCP and A2A. Firefly AI Assistant now orchestrates workflows across Photoshop, Premiere, Lightroom, and Illustrator.
- **Lightroom April 2026 update** (Classic 15.3, Desktop 9.3) added natural language photo search, background AI batch processing (Denoise, Raw Details, Super Resolution), and mood board generation via Firefly.
- **Canva AI 2.0** launched with an official MCP server, transforming Canva into a conversational design platform powered by the Canva Design Model.
- **Google Photos + Gemini** integration arrived — users can connect their photo library to Gemini for personalized image generation using their own photos as context.
- **Capture One v16.7.0** added AI clothes masking, combined masks, and facial retouching, but still no MCP or agent integration.
- **Getty/Shutterstock merger** received unconditional DOJ clearance (February 2026). Both expanding generative AI services — Getty added camera control and 4K upscaling, Shutterstock launched Generative 3D.
- **Immich v3** is in development with planned "workflows" feature and API breaking changes. FUTO encrypted backup integration being built.
- **ComfyUI MCP** ecosystem remains active as the primary way to connect AI agents to local Stable Diffusion installations.

## The Bottom Line

The photography MCP ecosystem earns **4.0 out of 5** — up from 3.5 at initial review. Here's why:

**What works well:**
- **ImageSorcery MCP** (306 stars, 17 tools) remains the standout local image processing toolkit — computer vision, OCR, format conversion, and batch processing without external API dependencies
- **Photoshop integration** (207 stars) bridges the most important professional photo editor with AI agents, and Adobe's endorsement of MCP as its agent protocol validates the ecosystem
- **Photopea MCP** (34 tools) — browser-based alternative means no Adobe subscription required for professional photo editing via MCP (new)
- **RAW processing gap filled** — RawTherapee MCP (49 tools) provides the first dedicated RAW processing pipeline with visual feedback loops and comprehensive editing controls (new)
- **AI image generation matured** — Stability AI MCP (84 stars, 12 tools) brings SD 3.5 with ControlNet, outpainting, and relighting; Gemini MCP upgraded to 2.5 Flash with 4K and character consistency (new/updated)
- **Cloud image services arrived** — Cloudinary's 5 official MCP servers bring enterprise-grade image infrastructure to AI agents (new)
- **Google Photos MCP** nearly tripled its tools (7→19) with Picker API migration and security hardening (updated)
- **ImmichMCP** grew from 3 to 10 stars with v0.3.2, adding EXIF search and CLIP semantic search (updated)
- **Canon camera control** jumped from 3 to 28 tools with the new canon-client server (new)
- **Astrophotography** got dedicated tooling via PixInsight MCP (60 tools) — remarkably specialized (new)
- **GIMP MCP** (103 stars) continues to demonstrate what native plugin integration can achieve
- **EXIF MCP** provides the deepest metadata access with 11 specialized tools, all offline

**What's still missing:**
- **No Capture One integration** — added AI features (clothes masking, retouching) but no MCP server or agent protocol
- **No Nikon/Sony/Fuji camera support** — Canon is the only brand with MCP servers (two implementations)
- **No photo culling or rating tools** — reviewing hundreds of shots and selecting the best has no dedicated MCP tooling
- **No HDR or panorama stitching** — computational photography techniques remain absent
- **No Flickr, SmugMug, Amazon Photos, or 500px** — photo sharing platforms have no MCP presence
- **Lightroom fragmentation** — two implementations, both growing in stars (4→9 and 0→1) but neither with strong adoption

**What changed since March 2026:**
The biggest shift is the RAW processing gap being filled — RawTherapee MCP's 49 tools with visual feedback loops directly addresses the most significant gap identified in the original review. AI image generation also matured substantially, with Stability AI MCP bringing the full SD 3.5 pipeline and Gemini MCP adding 4K output. The arrival of official Cloudinary MCP servers signals enterprise cloud image services entering the ecosystem. Adobe's adoption of MCP as its agent protocol standard at Summit April 2026 is the most significant industry validation — while there's no official Adobe MCP server yet, the protocol endorsement suggests first-party integrations may follow.

**Category**: [Design & Creative MCP Servers](/categories/design-creative/)

*This review was refreshed on 2026-04-27 using Claude Opus 4.6 (Anthropic). Originally published 2026-03-15.*


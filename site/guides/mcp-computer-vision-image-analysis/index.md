# MCP and Computer Vision: How AI Agents Connect to Object Detection, Image Analysis, Medical Imaging, Satellite Imagery, OCR, Video Processing, Screenshot Capture, Webcam Integration, Facial Recognition, Visual Inspection, and Document Understanding

> A comprehensive guide to 50+ MCP integrations for computer vision and image analysis — covering object detection servers (IDEA-Research's official DINO-X MCP with ~116 stars for


Computer vision is one of the fastest-growing segments of the AI market. Valued at approximately $20-27 billion in 2025, the global computer vision market is projected to reach $58-111 billion by 2030-2034, growing at 14-20% CAGR depending on the source. Inspection and quality assurance alone account for 41% of market revenue, edge deployment now comprises 47% of CV implementations, and vision-language models are rapidly replacing single-task classifiers with natural-language-queryable visual understanding.

The Model Context Protocol is creating a new interface layer between AI agents and computer vision capabilities. Rather than building custom integrations for every vision task, MCP servers expose object detection, image processing, OCR, medical imaging, satellite data, and video analysis as standardized tools that any MCP-compatible AI assistant can invoke. This means a developer using Claude Code, Cursor, or GitHub Copilot can ask "what objects are in this image?" or "extract text from this PDF" and get results from specialized CV models — without writing integration code.

This guide is research-based. We survey what MCP servers exist across the computer vision landscape, analyze the workflows they enable, and identify where significant gaps remain. We do not claim to have tested or used any of these servers hands-on — our analysis draws on published documentation, open-source repositories, vendor announcements, and industry research. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI. For background on MCP, see our [introduction to MCP](/guides/what-is-mcp/) and the [MCP server directory](/reviews/).

## Why Computer Vision Needs MCP

Computer vision has historically required deep expertise to deploy — choosing models, writing preprocessing pipelines, managing inference infrastructure, and interpreting results. MCP changes this by packaging CV capabilities as tools that AI agents can use conversationally.

**Natural language becomes the query language for images.** Instead of writing Python scripts to run YOLO inference, a developer can ask an MCP-connected AI assistant "detect all objects in this photo" and get structured results. The MCP server handles model loading, inference, and result formatting behind the scenes.

**Multi-model pipelines become composable.** An AI agent with access to multiple CV MCP servers can chain capabilities — detect objects with DINO-X, extract text with OCR, analyze metadata with EXIF tools, and generate a summary — all in a single conversation. No custom orchestration code required.

**Vision capabilities integrate into development workflows.** Screenshot MCP servers let AI coding assistants see what a webpage actually looks like. Webcam servers bring real-world visual input into agent workflows. Medical imaging servers connect AI assistants to DICOM archives. Each integration opens new use cases that were previously walled behind specialized tooling.

**Edge and cloud flexibility.** Some MCP servers run entirely locally (ImageSorcery, YOLO MCP), while others connect to cloud APIs (Azure Face API, AI Vision MCP via Gemini). This lets teams choose the right tradeoff between latency, privacy, and capability for their specific use case.

## Object Detection and Image Classification

These MCP servers bring state-of-the-art object detection and classification capabilities to AI agents, ranging from zero-shot detection via vision-language models to specialized YOLO-based inference.

### DINO-X MCP (Official — IDEA-Research)

**Repository:** IDEA-Research/DINO-X-MCP (~116 stars) | **Type:** Official | **Language:** TypeScript | **License:** Apache 2.0

The official MCP server from IDEA-Research (the team behind the DINO and Grounding DINO models published at ICLR) brings their DINO-X model to AI agents for advanced visual understanding.

Key capabilities:
- **Full-scene object detection** (`detect-all-objects`) — detects and labels all objects in an image without requiring text prompts, leveraging DINO-X's open-world detection capabilities
- **Text-prompted detection** (`detect-objects-by-text`) — find specific objects by describing them in natural language, enabling zero-shot detection for any object category
- **Human pose estimation** (`detect-human-pose-keypoints`) — detects 17 body keypoints per person for pose analysis, activity recognition, and ergonomic assessment
- **Annotation visualization** (`visualize-detection-result`) — overlays bounding boxes, labels, and keypoints on images for visual verification
- **Dual transport** — supports both STDIO and Streamable HTTP modes for flexible deployment

DINO-X represents the cutting edge of open-world object detection — the model can identify objects it was never explicitly trained on by leveraging vision-language understanding. This makes it particularly valuable for scenarios where the set of possible objects isn't known in advance.

### ImageSorcery MCP (by sunriseapps)

**Repository:** sunriseapps/imagesorcery-mcp (~297 stars, 168 commits) | **Type:** Community/Open Source | **Language:** Python | **License:** Open Source

The highest-starred dedicated computer vision MCP server, combining object detection, OCR, and image manipulation in a single package that runs entirely locally.

Key capabilities:
- **Object detection** — powered by Ultralytics YOLO models for real-time detection with bounding boxes
- **OCR** — integrated text extraction from images
- **Text-prompted object search** — find objects by natural language description
- **Image classification** — categorize image content
- **Image manipulation** — crop, resize, rotate, draw text and rectangles
- **Metadata extraction** — read image properties and EXIF data
- **Fully local** — all processing happens on-device using OpenCV and Ultralytics, no cloud API calls

Installable via pipx, ImageSorcery is a practical choice for developers who want a single MCP server covering multiple CV tasks without sending data to external services. The active maintenance (168 commits) suggests ongoing development.

### YOLO MCP Server (by GongRzhe)

**Repository:** GongRzhe/YOLO-MCP-Server (~31 stars) | **Type:** Community/Open Source | **Language:** Python | **License:** MIT

A comprehensive MCP wrapper around Ultralytics YOLO that goes beyond inference to include model training and export capabilities.

Key capabilities:
- **Object detection** — real-time detection using YOLO models
- **Image segmentation** — pixel-level object segmentation
- **Image classification** — categorize images into predefined classes
- **Pose estimation** — human body keypoint detection
- **Real-time camera analysis** — live video feed processing with detection overlays
- **Model training** — train custom YOLO models on your own datasets directly through the MCP interface
- **Model validation** — evaluate model performance with standard metrics
- **Model export** — convert trained models to ONNX and other deployment formats

The training capability is distinctive — most CV MCP servers only handle inference. Being able to train, validate, and export custom models through an AI assistant conversation makes YOLO workflows accessible to developers who aren't CV specialists. Pre-configured for Cursor, Windsurf, and Claude Desktop.

### Groundlight mcp-vision

**Repository:** groundlight/mcp-vision (~55 stars) | **Type:** Community/Open Source | **Language:** Python | **License:** MIT

From Groundlight (a computer vision company), this server wraps HuggingFace zero-shot object detection pipelines for MCP access.

Key capabilities:
- **Zero-shot object detection** (`locate_objects`) — detect objects using HuggingFace's pre-trained models without task-specific training
- **Object zooming** (`zoom_to_object`) — crop and zoom to detected objects for closer inspection
- **GPU acceleration** — Docker support with GPU passthrough for faster inference
- **Extensible** — designed to work with other HuggingFace vision pipelines

The zero-shot approach means no training data is needed — describe what you're looking for, and the model finds it. This is ideal for ad-hoc visual queries where creating a custom dataset would be impractical.

### OpenCV MCP Server (by GongRzhe)

**Repository:** GongRzhe/opencv-mcp-server (~97 stars) | **Type:** Community/Open Source | **Language:** Python | **Status:** Archived (March 2026)

A comprehensive wrapper exposing the full OpenCV library through MCP. Though now archived, it demonstrated the breadth of CV capabilities accessible through the protocol.

Key capabilities:
- **Image I/O** — read, write, and convert between image formats
- **Color space conversion** — RGB, HSV, LAB, grayscale transformations
- **Filtering and edge detection** — Gaussian blur, Canny edges, morphological operations
- **Face detection** — Haar cascade classifiers for face and feature detection
- **Object detection** — YOLO integration for general object detection
- **Video processing** — frame extraction, motion detection, object tracking
- **Real-time camera** — live webcam processing with detection overlays

The archive status is worth noting — developers looking for OpenCV-via-MCP may need to fork this project or look for alternatives. The comprehensive tool set spanning image basics, classical CV, and video processing makes it a useful reference for anyone building CV MCP servers.

### Additional Object Detection Servers

**AI Vision MCP** (tan-yong-sheng/ai-vision-mcp, ~45 stars) — cloud-based analysis via Google Gemini and Vertex AI. Provides `analyze_image`, `compare_images`, `detect_objects_in_image`, and `analyze_video` tools with Zod validation, retry logic, and circuit breaker patterns. Good for teams already using Google Cloud.

**mcp-image-recognition** (mario-andreschak, ~35 stars) — image recognition via Anthropic Claude Vision and OpenAI GPT-4 Vision APIs with configurable primary/fallback providers. Supports JPEG, PNG, GIF, WebP with optional Tesseract OCR fallback.

**VisionCraft MCP** (augmentedstartups/VisionCraft-MCP-Server, ~70-113 stars) — not a CV processing server per se, but a knowledge base of 100K+ computer vision repositories searchable via a Raven retrieval engine. Covers object detection, segmentation, 3D vision, VLMs, and agentic frameworks. Free API key during testing phase.

**Groundlight MCP Server** (groundlight/groundlight-mcp-server, ~4 stars) — from the same company as mcp-vision but focused on visual question answering. Binary classification (yes/no), multiclass categorization, object counting, and human-in-the-loop escalation for uncertain results. 14 tools for detector management, image queries, alerts, labels, and metrics. Apache 2.0.

**Roboflow MCP** — community integration exposing the Roboflow API through MCP. Search Universe for public datasets, upload images, create dataset versions, run inference on trained models, and get model metrics. Roboflow's inference repo has 9K+ stars and their RF-DETR model is published at ICLR 2026.

## Image Processing and Optimization

These servers handle the practical work of manipulating, optimizing, and analyzing images — tasks that complement detection and classification.

### Image Optimization Servers

**mcp-image-optimizer** (piephai) — powered by Sharp for high-performance image processing. Resize, convert between formats, batch processing, metadata extraction, border/whitespace removal, smart cropping, and LQIP (Low Quality Image Placeholder) generation for web performance.

**mcp-image-compression** (InhiblabCore) — specialized compression for JPEG, PNG, WebP, and AVIF. Fully offline processing with smart auto-optimal compression parameters and batch parallel processing.

**sharp-mcp** (greatSumini, ~11 stars) — session management for images with ML-powered background removal via segmentation. Crop, compress, format conversion, color sampling, and dominant color detection.

**image-processing-mcp-server** (rafael-castelo) — focused image processing with resize, compress (configurable quality, lossless option), and format conversion across JPEG, PNG, WebP, AVIF, and TIFF.

**zipic-mcp-server** (okooo5km) — JPEG, WebP, HEIC, AVIF, and PNG compression with quick and advanced modes. Batch processing support. Requires the Zipic macOS application.

### Image Analysis and Metadata

**image-mcp** (standardbeagle) — comprehensive image toolkit: resize, crop, rotate, flip, format conversion (JPEG, PNG, WebP, AVIF, TIFF, GIF), compression, EXIF metadata extraction, AI generation, diagrams, charts, and accessibility features.

**exif-mcp** (stass) — specialized EXIF and XMP metadata reader that works entirely offline using the exifr library. Supports JPEG, PNG, TIFF, and HEIC. Useful for forensic analysis, photo management, and content verification workflows.

**qrscanner-mcp** (juparave) — QR code generation and scanning via OpenCV and pyzbar. Multi-QR scanning in a single image for batch processing scenarios.

### Professional Image Editing Integration

**GIMP MCP Server** (libreearth/gimp-mcp and maorcc/gimp-mcp) — bridges GIMP with AI agents for natural language image editing. Issue commands like "remove the background" or "adjust levels" through conversation.

**Photoshop MCP Server** (loonghao/photoshop-python-api-mcp-server) — Adobe Photoshop integration via its Python API. Automate image editing operations and workflows. Windows only.

## Medical Imaging

Medical imaging is an early but important frontier for MCP — connecting AI assistants to clinical imaging infrastructure while navigating the strict regulatory requirements of healthcare.

### dicom-mcp (by ChristianHinge)

**Repository:** ChristianHinge/dicom-mcp (~87 stars) | **Type:** Community/Open Source | **Language:** Python | **Engine:** pynetdicom

The most complete DICOM MCP server, providing query access to PACS (Picture Archiving and Communication Systems) and VNA (Vendor Neutral Archives) through standard DICOM networking.

Key capabilities:
- **Patient queries** (`query_patients`) — search for patients by name, ID, date of birth, or other demographics
- **Study queries** (`query_studies`) — find imaging studies by date, modality, description, or accession number
- **Series and instance queries** — drill down to individual image series and DICOM instances
- **PDF text extraction** (`extract_pdf_text_from_dicom`) — extract text from DICOM-encapsulated PDF reports (structured reports, clinical notes)
- **Data movement** (`move_series`, `move_study`) — transfer imaging data between DICOM nodes
- **Connection management** — configure and manage connections to multiple DICOM endpoints

The server explicitly warns that it is "not meant for clinical use" — an important disclaimer given the regulatory requirements for medical software. It's designed for research, development, and administrative workflows rather than diagnostic decision-making.

### dicom-mcp-server (Flux Inc.)

**Repository:** fluxinc/dicom-mcp-server (~3 stars) | **Type:** Community/Open Source | **Language:** Python

A lighter DICOM server focused on connectivity testing with C-ECHO (the DICOM equivalent of a network ping). Supports YAML-based node configuration and multiple AE (Application Entity) titles. Useful for network validation and DICOM infrastructure management.

### Medical Imaging Gaps

The MCP ecosystem has significant gaps in medical imaging:
- **No radiology AI servers** — no MCP integration for chest X-ray analysis, CT interpretation, or mammography screening AI
- **No pathology servers** — digital pathology (whole slide imaging) has no MCP representation
- **No medical image segmentation** — despite models like MedSAM existing, there's no MCP server for medical image segmentation tasks
- **No FHIR-imaging integration** — no server bridges DICOM imaging data with FHIR clinical data
- **Regulatory barriers** — medical AI requires FDA clearance (in the US) or CE marking (in Europe), which limits what open-source projects can claim

## Satellite and Geospatial Imagery

Earth observation is generating petabytes of data daily. MCP servers are beginning to make this data accessible to AI agents for analysis and decision-making.

### NASA Earthdata MCP (Official)

**Repository:** nasa/earthdata-mcp (~5 stars) | **Type:** Official (NASA) | **Language:** Python | **Deployment:** AWS Lambda

NASA's official MCP server for accessing Earth observation data, using semantic search powered by embeddings to help users find relevant datasets across NASA's massive data catalog.

Key capabilities:
- **Semantic search** — find Earth observation datasets by describing what you need in natural language, using vector embeddings for relevance matching
- **NASA CMR integration** — connects to NASA's Common Metadata Repository at cmr.earthdata.nasa.gov
- **Cloud-native architecture** — AWS Lambda pipeline with PostgreSQL + pgvector for embedding storage and Redis caching
- **Live SSE endpoint** — accessible at cmr.earthdata.nasa.gov/mcp/sse

Having NASA publish an official MCP server signals institutional recognition of the protocol's value for scientific data access. The semantic search approach is particularly valuable given the complexity of Earth science data catalogs — users don't need to know exact dataset names or technical parameters.

### Copernicus MCP (by wb1016)

**Repository:** wb1016/copernicus-mcp | **Type:** Community/Open Source

Access to ESA's Copernicus satellite constellation through the OData API. Search, download, and manage satellite imagery from the Copernicus Data Space — including Sentinel-2 multispectral imagery and Sentinel-1 SAR data.

### GIS MCP (by mahdin75)

**Repository:** mahdin75/gis-mcp | **Type:** Community/Open Source

GIS operations for LLMs including downloading and stacking spectral bands from STAC (SpatioTemporal Asset Catalog) items. Works with Sentinel-2, Landsat, and other STAC-compliant data sources. Includes geospatial transformations for coordinate system management.

### Additional Geospatial Servers

**NASA MCP Server** (jezweb/nasa-mcp-server) — access to NASA's open APIs including APOD (Astronomy Picture of the Day), Mars rover photos, asteroid tracking, Earth observations, and media library. More consumer-oriented than the Earthdata MCP.

**Mapbox MCP Server** (mapbox/mcp-server, ~325 stars) — official Mapbox integration with geocoding, POI search, multi-modal routing, travel time matrices, isochrones, and static map image generation.

**Street View MCP** (vlad-ds/street-view-mcp) — fetch Google Street View imagery, save images, and create HTML virtual tours. Useful for location verification, real estate analysis, and urban planning workflows.

**Google Maps MCP** (Garblesnarff/google-maps-mcp) — 14 tools including street view panoramic imagery and static map generation.

## Screenshot and Screen Capture

Screen capture MCP servers bridge the gap between visual web content and AI agent understanding — letting agents see what users see.

### Microsoft Playwright MCP (Official)

**Repository:** microsoft/playwright-mcp (~30,000 stars) | **Type:** Official (Microsoft) | **Language:** TypeScript

By far the most popular MCP server in any CV-adjacent category. Playwright MCP provides browser automation with two key vision-related modes:

- **Accessibility snapshots** — expose the browser's accessibility tree (roles, labels, states, hierarchy) rather than visual pixels. This gives AI agents the same semantic understanding that screen readers use
- **Screenshots** — full-page and element-level screenshot capture for visual analysis
- **Cross-browser** — works with Chromium, Firefox, and WebKit

The accessibility snapshot mode is particularly powerful for AI agents — it provides structured, semantic information about page content rather than requiring the agent to interpret raw pixels. This is both more efficient and more reliable for understanding web page structure.

### Other Screenshot Servers

**mcp-screenshot-server** (sethbang, ~19 stars) — web capture via Puppeteer plus cross-platform system screenshots (macOS, Linux, Windows). Security-hardened with SSRF prevention and path traversal protection.

**BrowserLoop** (mattiasw/browserloop) — screenshots plus console log reading via Playwright. Useful for debugging workflows where you need both visual output and JavaScript errors.

**ScreenshotMCP** (upnorthmedia/ScreenshotMCP) — full-page screenshots, element screenshots, and device size presets for responsive design testing.

**ScreenshotOne MCP** (screenshotone/mcp) — MCP wrapper for the ScreenshotOne commercial API, which handles rendering at scale with CDN caching.

## Webcam and Camera Integration

These servers bring real-world visual input into AI agent workflows — from development webcams to IoT camera feeds.

### mcp-webcam (by evalstate)

**Repository:** evalstate/mcp-webcam (~114 stars) | **Type:** Community/Open Source | **Language:** TypeScript

The most mature webcam MCP server, supporting both local and remote usage patterns.

Key capabilities:
- **STDIO and streaming HTTP** — flexible transport for local and remote deployment
- **Multi-user support** — multiple agents can access the same camera feed
- **MCP Sampling support** — integrates with MCP's sampling protocol for agent-initiated image capture
- **Docker deployment** — containerized for easy setup
- **Live demo** — running at webcam.fast-agent.ai

### Other Camera Servers

**videocapture-mcp** (13rac1/videocapture-mcp) — OpenCV-compatible webcam and video source capture. Image capture, camera settings, and video connection management.

**Windy Webcams MCP** (Cyreslab-AI/windy-webcams-mcp-server) — access public webcams worldwide via the Windy API. Search by location or category, find nearby webcams by coordinates. Useful for weather monitoring, tourism, and environmental observation.

**OctoEverywhere MCP** (OctoEverywhere/mcp) — 3D printer webcam snapshots combined with printer state monitoring and control. A niche but practical integration for maker workflows.

## Video Analysis

Video analysis MCP servers are still early-stage, but emerging implementations show the pattern for connecting AI agents to video understanding.

### MCP Video Parser (by michaelbaker-dev)

**Repository:** michaelbaker-dev/mcpVideoParser | **Type:** Community/Open Source

Automatic frame extraction combined with AI analysis via Llava (a vision-language model), enabling natural language queries over video content.

Key capabilities:
- **Automatic frame extraction** — intelligent sampling of key frames from video files
- **AI-powered analysis** — each frame analyzed by Llava vision LLM for content understanding
- **Natural language search** — query video content with questions like "when does the person enter the room?"
- **Time-based search** — find specific moments in videos by timestamp
- **Location-based organization** — organize video content by detected locations
- **Audio transcription** — extract and transcribe audio tracks alongside visual analysis

### MCP Video Analyzer

Listed on LobeHub, this server combines transcripts, visual frames, and metadata for comprehensive video understanding. Features a burst mode for frame-by-frame capture of motion and animation sequences.

## OCR and Text Extraction

OCR MCP servers extract text from images, PDFs, and documents — a fundamental capability that bridges visual and textual AI workflows. (See also our [NLP/text analysis guide](/guides/mcp-nlp-text-analysis/) for additional OCR coverage.)

### ocr-mcp (by sandraschi)

**Repository:** sandraschi/ocr-mcp | **Type:** Community/Open Source

The most comprehensive OCR MCP server, supporting 8 different OCR engines for maximum flexibility and accuracy.

Supported engines:
- **DeepSeek-OCR** — AI-powered OCR with strong multi-language support
- **Florence-2** — Microsoft's vision foundation model
- **DOTS.OCR** — specialized OCR engine
- **PP-OCRv5** — PaddlePaddle's OCR system supporting 100+ languages
- **Qwen-Image** — Alibaba's vision-language model
- **GOT-OCR 2.0** — general OCR theory model
- **EasyOCR** — PyTorch-based OCR
- **Tesseract** — the classic open-source OCR engine

Additional capabilities include WIA scanner control (scan physical documents directly), PDF and CBZ comic processing, layout detection, table extraction, and form analysis. The multi-engine approach lets users choose the right tradeoff between speed, accuracy, and language support.

### Other OCR Servers

**Kreuzberg** (Goldziher/kreuzberg) — polyglot document intelligence available as library, CLI, REST API, or MCP server. Supports Tesseract, PaddleOCR, and EasyOCR backends with a unified interface.

**mistral-ocr-mcp** (lemopian) — Mistral OCR API integration for cloud-based text extraction.

**openai-ocr-mcp** (cjus) — OpenAI vision-based OCR leveraging GPT-4's visual understanding for context-aware text extraction.

**PaddleOCR Official MCP** — built into the PaddleOCR project (72K+ stars parent repo). Enterprise-grade OCR supporting 100+ languages.

**ultimate_mcp_server** (Dicklesworthstone, ~144 stars) — includes Tesseract OCR with preprocessing (denoising, deskewing) as part of a broader multi-capability MCP server.

## Facial Recognition and Biometrics

Facial recognition via MCP is extremely limited — only one dedicated server exists, reflecting both the technical complexity and ethical sensitivity of the domain.

### Azure AI Vision Face API MCP Server (Official Azure Samples)

**Repository:** Azure-Samples/azure-ai-vision-face-api-mcp-server (~9 stars) | **Type:** Official (Microsoft Azure Samples) | **Language:** Python

The only dedicated facial recognition MCP server, wrapping Azure's Face API for comprehensive face analysis.

Key capabilities:
- **Face attribute detection** — age estimation, gender classification, mask/glasses detection
- **Open-set attributes** — extensible attribute detection via GPT-4.1 for attributes beyond the predefined set
- **Face comparison and similarity** — compare two faces for verification or find similar faces in a collection
- **Face recognition enrollment** — register faces for persistent identification
- **Person group management** — organize faces into groups for recognition scenarios
- **Large person group operations** — scale to thousands of enrolled faces

Requires an Azure Face API endpoint and key. The GPT-4.1 integration for open-set attributes is notable — it combines traditional face analysis with LLM-powered visual reasoning for attributes the base model wasn't specifically trained on.

### Facial Recognition Gaps

The absence of open-source, self-hosted facial recognition MCP servers is a significant gap. Teams needing on-premises face analysis (for privacy compliance, air-gapped environments, or cost control) have no MCP option. Libraries like face_recognition, InsightFace, and DeepFace exist but lack MCP wrappers.

## Document Understanding

These servers go beyond simple OCR to understand document structure — layouts, tables, charts, headings, and semantic organization.

### MarkItDown (Microsoft Official)

**Repository:** microsoft/markitdown (~82,000 stars, includes packages/markitdown-mcp) | **Type:** Official (Microsoft) | **Language:** Python

Microsoft's massively popular document conversion library includes an official MCP server. Converts files to Markdown while preserving structure.

Key capabilities:
- **Multi-format conversion** — PDFs, DOCX, PPTX, XLSX, images, and more to structured Markdown
- **OCR plugin** — extract text from embedded images using LLM Vision
- **Structure preservation** — maintains headings, tables, lists, and formatting
- **Official MCP server** — built-in as a package within the MarkItDown monorepo

At 82K+ stars, MarkItDown is one of the most popular projects with MCP integration. Its broad format support makes it a practical first choice for document processing workflows.

### IBM Docling

**Repository:** docling-project (IBM/community) | **Type:** Community/Open Source

Advanced PDF understanding with layout awareness — a step beyond simple text extraction.

Key capabilities:
- **Page layout analysis** — understand reading order, columns, headers, footers
- **Table structure recognition** — extract tables with row/column relationships preserved
- **Code and formula detection** — identify and extract code blocks and mathematical formulas
- **Image classification** — classify embedded images within documents
- **Plug-and-play MCP server** — designed for easy integration with AI agent workflows

### Other Document Understanding Servers

**LandingAI Agentic Document Extraction** (landing.ai/ade) — layout-aware parsing with bounding boxes and page indexes. The previous vision-agent-mcp has been deprecated in favor of this more focused document extraction service.

**mcp-pdf** (rsp2k) — secure PDF processing with text extraction, OCR fallback, table extraction, forms processing, annotation reading, and chart extraction.

**document-understanding-mcp-server** (jaesharp) — PDF text extraction with OCR fallback, plus layout information including text block coordinates, image positions, and drawing locations.

### Diagram and Chart Generation

**UML-MCP** (antoinebou12) — generate diagrams from natural language descriptions using PlantUML, Mermaid, D2, Graphviz, TikZ, ERD, BPMN, and C4 notation. Covers the full spectrum of technical diagram types.

**mcp-server-chart** (AntVis) — 25+ chart types including bar, line, heatmap, radar, fishbone, and more. Data visualization through MCP for embedding charts in agent workflows.

**Draw.io MCP** (lgazo) — CRUD operations on Draw.io diagrams, enabling AI agents to create and modify visual diagrams programmatically.

**mcp-diagram-server** (angrysky56) — diagrams and mind maps with a permanent library for reuse across sessions.

## Comparison Table

| Server | Stars | Category | Local/Cloud | Key Strength |
|--------|-------|----------|-------------|--------------|
| Playwright MCP (Microsoft) | ~30,000 | Screenshot/Browser | Local | Accessibility snapshots + screenshots |
| MarkItDown (Microsoft) | ~82,000 | Document Understanding | Local | Multi-format to Markdown conversion |
| DINO-X MCP (IDEA-Research) | ~116 | Object Detection | Cloud API | Zero-shot open-world detection + pose |
| ImageSorcery MCP | ~297 | Multi-CV | Local | Detection + OCR + manipulation combined |
| mcp-webcam (evalstate) | ~114 | Camera | Local/Remote | Multi-user streaming webcam |
| OpenCV MCP (archived) | ~97 | Multi-CV | Local | Full OpenCV library wrapper |
| dicom-mcp | ~87 | Medical Imaging | Local | PACS/VNA DICOM queries |
| VisionCraft MCP | ~70-113 | CV Knowledge | Cloud API | 100K+ CV repo knowledge base |
| mcp-server-stability-ai | ~74 | Image Generation | Cloud API | Generate, edit, upscale images |
| Groundlight mcp-vision | ~55 | Object Detection | Local+GPU | HuggingFace zero-shot detection |
| AI Vision MCP | ~45 | Object Detection | Cloud (Google) | Gemini/Vertex AI image + video analysis |
| mcp-image-recognition | ~35 | Object Detection | Cloud (Multi) | Claude Vision + GPT-4V with fallback |
| YOLO MCP Server | ~31 | Object Detection | Local | Detection + training + export |
| mcp-screenshot-server | ~19 | Screenshot | Local | Puppeteer + system screenshots |
| Azure Face API MCP | ~9 | Facial Recognition | Cloud (Azure) | Face detection + recognition + comparison |
| NASA Earthdata MCP | ~5 | Satellite Imagery | Cloud (AWS) | Semantic search over NASA data |
| ocr-mcp (sandraschi) | — | OCR | Local | 8 OCR engines, scanner control |
| Kreuzberg | — | OCR/Documents | Local | Polyglot document intelligence |

## Architecture Patterns

### Pattern 1: Automated Visual Inspection Pipeline

```
┌─────────────────────────────────────────────────────┐
│                AI Agent (Claude/GPT)                 │
│         "Check this batch for defects"               │
└──────────┬──────────┬──────────┬────────────────────┘
           │          │          │
           ▼          ▼          ▼
    ┌──────────┐ ┌─────────┐ ┌──────────────┐
    │ Webcam/  │ │  YOLO   │ │  Groundlight │
    │ Camera   │ │  MCP    │ │  MCP Server  │
    │ MCP      │ │ Server  │ │ (Q&A + HIL)  │
    └──────────┘ └─────────┘ └──────────────┘
         │            │              │
         ▼            ▼              ▼
    ┌──────────┐ ┌─────────┐ ┌──────────────┐
    │ Capture  │ │ Detect  │ │ Classify     │
    │ product  │ │ defects │ │ uncertain    │
    │ images   │ │ + bbox  │ │ cases → human│
    └──────────┘ └─────────┘ └──────────────┘
                      │              │
                      ▼              ▼
              ┌──────────────────────────┐
              │   Results Dashboard      │
              │   Pass/Fail + Metrics    │
              └──────────────────────────┘
```

This pattern chains camera capture, ML-based defect detection, and human-in-the-loop classification for uncertain cases. The AI agent orchestrates the pipeline, escalating to human reviewers only when confidence is low.

### Pattern 2: Medical Imaging Research Workflow

```
┌─────────────────────────────────────────────────────┐
│              Research AI Agent                        │
│    "Find chest CT studies from 2025 with findings"   │
└──────────┬──────────┬──────────┬────────────────────┘
           │          │          │
           ▼          ▼          ▼
    ┌──────────┐ ┌─────────┐ ┌──────────────┐
    │ dicom-   │ │ OCR MCP │ │ MarkItDown   │
    │ mcp      │ │ Server  │ │ MCP          │
    └──────────┘ └─────────┘ └──────────────┘
         │            │              │
         ▼            ▼              ▼
    ┌──────────┐ ┌─────────┐ ┌──────────────┐
    │ Query    │ │ Extract │ │ Convert      │
    │ PACS for │ │ text    │ │ reports to   │
    │ studies  │ │ from    │ │ structured   │
    │ by date  │ │ DICOM   │ │ Markdown     │
    │ + modal  │ │ reports │ │ for analysis │
    └──────────┘ └─────────┘ └──────────────┘
                      │              │
                      ▼              ▼
              ┌──────────────────────────┐
              │  Structured Research     │
              │  Dataset (non-clinical)  │
              └──────────────────────────┘
```

This pattern connects DICOM archive queries with text extraction and document conversion for medical research workflows. The agent queries the PACS system, extracts report text from DICOM-encapsulated PDFs, and converts findings into structured formats for analysis. Critical caveat: this is for research only, not clinical decision-making.

### Pattern 3: Geospatial Analysis Agent

```
┌─────────────────────────────────────────────────────┐
│              Geospatial AI Agent                     │
│   "Analyze land use changes near coordinates X,Y"    │
└──────────┬──────────┬──────────┬────────────────────┘
           │          │          │
           ▼          ▼          ▼
    ┌──────────┐ ┌─────────┐ ┌──────────────┐
    │ NASA     │ │Copernicus│ │  Mapbox MCP  │
    │ Earthdata│ │  MCP    │ │  Server      │
    │ MCP      │ │         │ │              │
    └──────────┘ └─────────┘ └──────────────┘
         │            │              │
         ▼            ▼              ▼
    ┌──────────┐ ┌─────────┐ ┌──────────────┐
    │ Semantic │ │Download │ │ Geocode +    │
    │ search   │ │Sentinel │ │ generate     │
    │ for      │ │imagery  │ │ context      │
    │ datasets │ │+ bands  │ │ maps         │
    └──────────┘ └─────────┘ └──────────────┘
           │          │              │
           └──────────┼──────────────┘
                      ▼
              ┌──────────────────────────┐
              │   GIS MCP               │
              │   Stack bands, apply     │
              │   geospatial transforms  │
              └──────────────────────────┘
                      │
                      ▼
              ┌──────────────────────────┐
              │   Analysis Report        │
              │   Land use + change maps │
              └──────────────────────────┘
```

This pattern combines NASA data discovery, Copernicus satellite imagery download, Mapbox geocoding, and GIS processing for land use analysis. The agent uses semantic search to find relevant datasets, downloads multispectral imagery, and applies geospatial transformations for analysis.

### Pattern 4: Multimodal Document Processing Chain

```
┌─────────────────────────────────────────────────────┐
│              Document AI Agent                       │
│     "Process this invoice and extract all data"      │
└──────────┬──────────┬──────────┬────────────────────┘
           │          │          │
           ▼          ▼          ▼
    ┌──────────┐ ┌─────────┐ ┌──────────────┐
    │MarkItDown│ │ OCR MCP │ │ ImageSorcery │
    │  MCP     │ │ Server  │ │    MCP       │
    └──────────┘ └─────────┘ └──────────────┘
         │            │              │
         ▼            ▼              ▼
    ┌──────────┐ ┌─────────┐ ┌──────────────┐
    │ Convert  │ │ Extract │ │ Detect       │
    │ PDF to   │ │ text    │ │ logos,       │
    │ Markdown │ │ from    │ │ signatures,  │
    │ (struct) │ │ images  │ │ stamps       │
    └──────────┘ └─────────┘ └──────────────┘
           │          │              │
           └──────────┼──────────────┘
                      ▼
              ┌──────────────────────────┐
              │   Structured Output      │
              │   Line items, totals,    │
              │   dates, vendor info     │
              └──────────────────────────┘
```

This pattern chains document conversion, OCR, and object detection for comprehensive document understanding. The agent extracts structure via MarkItDown, reads text from embedded images via OCR, and detects visual elements like logos and signatures via object detection — combining all signals into structured data extraction.

## Market Context and Trends

The computer vision market is experiencing rapid growth across multiple segments:

- **Overall market:** $20-27 billion in 2025, projected to reach $58-111 billion by 2030-2034 (14-20% CAGR)
- **Inspection and quality assurance:** 41% of CV market revenue in 2025 — the single largest application segment
- **Edge deployment:** 47% of CV implementations now run at the edge, growing at 17.3% CAGR
- **North America:** 49% of 2025 market revenue
- **Asia-Pacific:** fastest-growing region at 16.4% CAGR

### Key Technology Trends

**Vision-Language Models (VLMs) are replacing single-task classifiers.** Models like DINO-X, Florence-2, and Qwen-VL enable natural language queries over images — "find all the screws in this assembly photo" — without task-specific training. MCP makes these models accessible through conversational interfaces.

**Foundation models are becoming the backbone.** Vision Transformers (ViTs), SAM (Segment Anything), and DINO variants are increasingly used as the base layer for specialized CV applications. MCP servers like DINO-X MCP directly expose these foundation models.

**Synthetic data generation is accelerating.** Generative AI creates training data for CV models, reducing the need for expensive manual annotation. ComfyUI and Stability AI MCP servers support this workflow by generating training images on demand.

**Edge AI is growing fast.** Nearly half of CV deployments now run at the edge (on-device, on-camera, on-premises). MCP servers that run locally (ImageSorcery, YOLO MCP, OpenCV MCP) align with this trend by processing images without sending data to the cloud.

**Agent-assisted CV workflows are emerging.** MCP enables chaining multiple CV tools in a single conversation — detect objects, extract text, analyze metadata, and generate reports — all orchestrated by an AI agent rather than custom pipeline code.

## Ecosystem Gaps

### Manufacturing and Visual Inspection
Despite inspection and quality assurance being 41% of the CV market, there is no purpose-built manufacturing visual inspection MCP server. Groundlight's MCP server is the closest (visual Q&A with human-in-the-loop), but it's new (4 stars) and not specifically designed for production line inspection. This is arguably the single largest gap in the MCP CV ecosystem relative to market demand.

### 3D Vision and Point Clouds
Zero MCP servers exist for 3D computer vision, depth estimation, point cloud processing, or LiDAR data. As autonomous vehicles, robotics, and spatial computing grow, this gap becomes increasingly significant.

### Thermal and Infrared Imaging
No MCP servers handle thermal or infrared imagery — a critical modality for building inspection, electrical fault detection, predictive maintenance, and search-and-rescue operations.

### Self-Hosted Facial Recognition
Only Azure's cloud-dependent Face API server exists. Teams needing on-premises facial recognition for privacy compliance, air-gapped environments, or cost control have no MCP option, despite mature open-source libraries (face_recognition, InsightFace, DeepFace) being available.

### Medical Imaging AI
Beyond DICOM query/retrieval, the MCP ecosystem has no medical imaging AI — no radiology analysis, no pathology processing, no medical image segmentation. Regulatory barriers (FDA/CE requirements) partially explain this, but research-use servers could still provide significant value.

### Satellite Image Analysis
NASA and Copernicus MCP servers provide data access, but no server performs actual satellite image analysis — change detection, land use classification, vegetation indices, urban growth mapping, or disaster assessment. The data pipeline stops at download.

### Video Understanding at Scale
Very few video analysis MCP servers exist, and none handle long-form video, real-time streaming at scale, or temporal event detection. Given the explosion of video content, this is a significant capability gap.

### Annotation and Labeling
No MCP servers support the data annotation workflow — labeling images, reviewing annotations, managing annotation projects. Tools like Label Studio, CVAT, and Labelbox lack MCP integrations, leaving a gap in the training data creation pipeline.

### AR/VR Vision
No MCP servers address augmented or virtual reality vision tasks — spatial mapping, hand tracking, eye tracking, or mixed reality scene understanding.

## Getting Started

### For Web Developers
Start with **Microsoft's Playwright MCP** for screenshot capture and accessibility snapshots in your IDE. Add **ImageSorcery MCP** if you need to analyze, optimize, or manipulate images locally. The combination gives you visual debugging (see what the page looks like) plus image processing (optimize assets) in a single workflow.

### For Computer Vision Engineers
**DINO-X MCP** provides state-of-the-art zero-shot detection if you need open-world object detection. **YOLO MCP Server** is the better choice if you need to train custom models — its MCP interface for training, validation, and export makes YOLO workflows conversational. Both integrate with Claude Code and Cursor.

### For Data Scientists
Combine **NASA Earthdata MCP** or **Copernicus MCP** for satellite data access with **GIS MCP** for processing. For document-heavy workflows, **MarkItDown MCP** (82K stars, Microsoft official) plus **ocr-mcp** (8 engines) covers most extraction needs.

### For Healthcare Researchers
**dicom-mcp** is currently the only path to PACS/VNA data through MCP. Combine it with OCR servers for report extraction and MarkItDown for document conversion. Remember: these tools are for research workflows, not clinical decision-making.

### For DevOps and QA Teams
**Playwright MCP** handles visual regression testing and accessibility auditing. **mcp-screenshot-server** adds system-level screenshots with SSRF protection. For monitoring physical systems, **mcp-webcam** connects cameras to AI agent workflows.

### For Open Source Contributors
The gaps listed above represent significant opportunities. Manufacturing visual inspection (41% of the CV market with zero dedicated MCP servers), 3D vision/point clouds, self-hosted facial recognition, and satellite image analysis are all areas where new MCP servers could have substantial impact. The CV community has mature open-source models — the missing piece is MCP wrappers that make them accessible to AI agents.


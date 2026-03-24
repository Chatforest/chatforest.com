---
title: "Printing & 3D Printing MCP Servers — OctoPrint, FreeCAD, OpenSCAD, CUPS, Print-on-Demand, and More"
date: 2026-03-15T19:30:00+09:00
description: "Printing and 3D printing MCP servers let AI agents control 3D printers, design CAD models, manage print queues, and automate print-on-demand storefronts. We found 23+ servers across 4 subcategories. DMontgomery40/mcp-3D-printer-server: 161 stars, TypeScript, GPL-2.0, 20+ tools — multi-printer control with STL manipulation and direct Bambu Lab MQTT printing. neka-nat/freecad-mcp: 605 stars, Python, MIT, 10 tools — the most popular CAD MCP server, controlling FreeCAD from Claude Desktop. codeofaxel/Kiln: 10 stars, Python, MIT, 430+ tools — the most ambitious 3D printing infrastructure with fleet management, model search, and fulfillment routing. jhacksman/OpenSCAD-MCP-Server: 133 stars, Python, MIT, 10 tools — text-to-3D model pipeline via AI image synthesis and multi-view stereo reconstruction. steveclarke/mcp-printer: 6 stars, TypeScript, 8 tools — document printing via CUPS with batch support and queue management. TSavo/printify-mcp: 24 stars, TypeScript, 15+ tools — Printify print-on-demand with AI design generation via Replicate Flux. Gaps: no Cura slicer integration, no Formlabs/resin printing, no large-format printing, no ZPL/thermal label printing, no 3D scanning. Rating: 4/5."
og_description: "Printing & 3D printing MCP servers: mcp-3D-printer-server (161 stars, 20+ tools, multi-printer), FreeCAD MCP (605 stars, CAD), Kiln (430+ tools, fleet management), OpenSCAD MCP (133 stars, text-to-3D), CUPS printer (8 tools), Printify (AI design generation). 23+ servers across printer control, CAD, document printing, and print-on-demand. Rating: 4/5."
content_type: "Review"
card_description: "Printing and 3D printing MCP servers across printer control, CAD modeling, document printing, and print-on-demand. This is a surprisingly mature ecosystem — one of the strongest niche verticals we've reviewed. The standout is DMontgomery40/mcp-3D-printer-server (161 stars, TypeScript, GPL-2.0, 20+ tools), which connects to OctoPrint, Klipper/Moonraker, Duet, Repetier, Bambu Labs, Prusa Connect, and Creality Cloud. It handles STL manipulation (scaling, rotation, sectional editing) and can print directly to Bambu Lab printers via MQTT. Even more ambitious is codeofaxel/Kiln (10 stars, Python, MIT, 430+ MCP tools and 107 CLI commands) — a comprehensive agentic 3D printing infrastructure supporting five printer platforms (OctoPrint, Moonraker, Bambu Lab, Prusa Link, Elegoo), model search across Thingiverse/MyMiniFactory/Cults3D, auto-slicing, fleet management, fulfillment center routing via Craftcloud, G-code validation, and emergency stop. OctoEverywhere/mcp (28 stars, Apache-2.0) takes a different approach — a free cloud-based service requiring no local setup, supporting OctoPrint, Klipper, Bambu Lab, Creality, Prusa, Elegoo, and Anycubic for basic status monitoring and control. hunter-stradley/bambustudio-mcp (Python, MIT, 33 tools) offers end-to-end Bambu Lab automation including model generation from text/images, slicing, live camera monitoring, and defect detection. The CAD ecosystem is even richer. neka-nat/freecad-mcp (605 stars, Python, MIT, 10 tools) is the most popular, enabling natural language control of FreeCAD via an RPC addon — create objects, edit geometry, generate 3D models from specifications or 2D drawings. contextform/freecad-mcp (60 stars, Python, 45+ operations) offers deeper PartDesign and Part workbench integration with 13 PartDesign operations, 18 Part operations, and 14 view controls. bonninr/freecad_mcp (153 stars, Python, MIT) provides prompt-assisted CAD design through FreeCAD's Python scripting. proximile/FreeCAD-MCP (0 stars, Python, MIT, 57 tools) is the most feature-rich by tool count, with Docker-containerized headless execution, Vision AI analysis, and image-to-3D via TRELLIS.2 — but requires dual 24GB GPUs. For AutoCAD users, daobataotie/CAD-MCP (264 stars, Python, MIT, 10 tools) provides natural language control of AutoCAD, GstarCAD, and ZWCAD with drawing operations including shapes, text, hatching, dimensioning, and layer management. OpenSCAD has three competing implementations: jhacksman/OpenSCAD-MCP-Server (133 stars, Python, MIT, 10 tools) converts text prompts and images into parametric 3D models via AI image synthesis and multi-view stereo reconstruction; quellant/openscad-mcp (47 stars, Python, MIT, 14 tools) focuses on rendering, export, and analysis with 80%+ test coverage and 300 passing tests; fboldo/openscad-mcp-server (0 stars, TypeScript, MIT, 2 tools) is a lightweight beta for rendering and STL export. rishigundakaram/cadquery-mcp-server (10 stars, Python, 2 tools) enables conversational 3D modeling with CadQuery for parametric models exportable to STL/STEP. Bigchx/mcp_3d_relief (17 stars, Python, MIT) converts 2D images into 3D relief STL models for printing. Blender's ahujasid/blender-mcp (16,300+ stars, Python, MIT) is the elephant in the room — by far the most popular 3D modeling MCP server, though not printing-specific, it's heavily used in 3D printing pipelines. Document printing is covered by steveclarke/mcp-printer (6 stars, TypeScript, 8 tools) for CUPS-based printing on macOS/Linux with PDF, text, markdown, and code file support including syntax highlighting; NullYing/Printer-AI-MCP (11 stars, Python, MIT, 4 tools) for cross-platform printer management on Windows, macOS, and Linux; and danielrosehill/MCP-Network-CUPS (1 star, TypeScript, MIT, 3 tools) for network printing via CUPS over streamable HTTP. Print-on-demand is served by TSavo/printify-mcp (24 stars, TypeScript, 15+ tools) with AI design generation via Replicate Flux and publishing to Etsy/Shopify; jeffkimble/printify-mcp-server (0 stars, JavaScript, MIT, 11 tools) for full Printify API v1 integration; and Purple-Horizons/printful-ph-mcp (1 star, Python, MIT, 19 tools) for Printful with catalog browsing, order management, mockup generation, and shipping calculation. Gaps remain: no dedicated Cura slicer integration (the most popular slicer), no Formlabs or resin printer support, no large-format or plotter printing, no ZPL/thermal label printing (Zebra, Dymo, Brother), no receipt/POS printing, no 3D scanning or photogrammetry pipeline, no direct integration with 3D model marketplaces as standalone tools. The category earns 4/5 — the 3D printing control and CAD modeling ecosystems are genuinely impressive, with multiple competing implementations covering all major printer platforms and CAD software. This is one of the strongest niche verticals in the MCP landscape, driven by the maker and open-source hardware communities."
last_refreshed: 2026-03-15
---

Printing and 3D printing MCP servers let AI agents control 3D printers, design CAD models, manage document print queues, and automate print-on-demand storefronts. Unlike many niche verticals we've reviewed, this ecosystem is **surprisingly mature** — driven by the maker community and open-source hardware movement.

This review covers the **printing and 3D printing** vertical — 3D printer control, CAD/3D modeling, document/CUPS printing, and print-on-demand. For design tools that produce printable output, see our [Design & UI MCP review](/reviews/design-ui-mcp-servers/). For the Blender MCP server (which overlaps with 3D printing workflows), we cover it briefly here but it's primarily a 3D modeling tool.

The headline finding: **this is one of the strongest niche verticals in the MCP landscape.** We found 23+ servers with genuine utility, multiple competing implementations for major platforms, and ambitious projects like Kiln that attempt to automate entire 3D printing workflows end-to-end.

**Category:** [IoT & Hardware](/categories/iot-hardware/)

---

## 3D Printer Control

### mcp-3D-printer-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [DMontgomery40/mcp-3D-printer-server](https://github.com/DMontgomery40/mcp-3D-printer-server) | 161 | TypeScript | GPL-2.0 | 20+ |

The **best general-purpose 3D printer MCP server.** Supports six printer platforms:

- **OctoPrint** — the most popular open-source print server
- **Klipper/Moonraker** — high-performance firmware with API access
- **Duet** — RepRapFirmware boards
- **Repetier** — another popular print server
- **Bambu Labs** — direct MQTT printing to Bambu printers
- **Prusa Connect** and **Creality Cloud**

Beyond basic printer control, it handles **STL manipulation** — scaling, rotation, and sectional editing of 3D models before printing. The Bambu Lab integration is notable: it can print .3mf files directly via MQTT without going through Bambu Studio.

### Kiln

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [codeofaxel/Kiln](https://github.com/codeofaxel/Kiln) | 10 | Python | MIT | 430+ |

The **most ambitious 3D printing MCP server** — and one of the most tool-rich MCP servers we've seen in any category. 430+ MCP tools and 107 CLI commands covering:

- **Multi-platform control** — OctoPrint, Moonraker, Bambu Lab, Prusa Link, Elegoo
- **Model search** — Thingiverse, MyMiniFactory, Cults3D integration
- **Auto-slicing** — automated slice preparation
- **Fleet management** — manage multiple printers as a coordinated fleet
- **Fulfillment routing** — route print jobs via Craftcloud for commercial fulfillment
- **Safety** — G-code validation and emergency stop

The tool count is staggering, but the low star count (10) suggests this is early-stage. Worth watching if you're building an automated print farm.

### OctoEverywhere MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [OctoEverywhere/mcp](https://github.com/OctoEverywhere/mcp) | 28 | Cloud-based | Apache-2.0 | ~5 |

A **free cloud-based approach** — no local server setup needed. Supports OctoPrint, Klipper, Bambu Lab, Creality, Prusa, Elegoo, and Anycubic. Capabilities include printer status monitoring, webcam snapshots, and pause/resume/cancel control. Simpler than the self-hosted alternatives but much easier to set up.

### BambuStudio MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [hunter-stradley/bambustudio-mcp](https://github.com/hunter-stradley/bambustudio-mcp) | — | Python | MIT | 33 |

**End-to-end Bambu Lab automation:**

- **Model generation** — create 3D models from text descriptions or images
- **Slicing** — automated slice preparation for Bambu printers
- **Live monitoring** — camera feed access during printing
- **Defect detection** — AI-powered print quality monitoring
- **Iterative improvement** — quality feedback loop for design refinement

The most specialized Bambu Lab integration available.

## CAD & 3D Modeling

### FreeCAD MCP Servers

FreeCAD has **five competing MCP implementations** — the most of any CAD program:

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [neka-nat/freecad-mcp](https://github.com/neka-nat/freecad-mcp) | 605 | Python | MIT | 10 |
| [bonninr/freecad_mcp](https://github.com/bonninr/freecad_mcp) | 153 | Python | MIT | 2 |
| [contextform/freecad-mcp](https://github.com/contextform/freecad-mcp) | 60 | Python | — | 45+ |
| [lucygoodchild/freecad-mcp-server](https://github.com/lucygoodchild/freecad-mcp-server) | 5 | TypeScript | — | 7 |
| [proximile/FreeCAD-MCP](https://github.com/proximile/FreeCAD-MCP) | 0 | Python | MIT | 57 |

**neka-nat/freecad-mcp** (605 stars) is the clear leader — the most popular CAD MCP server overall. It installs as a FreeCAD addon that starts an RPC server, letting Claude Desktop create objects, edit geometry, and generate 3D models from specifications or 2D drawings. 70 commits indicate active development.

**contextform/freecad-mcp** (60 stars) goes deeper into FreeCAD's workbenches: 13 PartDesign operations, 18 Part operations, 14 view controls, plus arbitrary Python script execution. Best for users who need fine-grained control over specific FreeCAD features.

**proximile/FreeCAD-MCP** (57 tools) is the most feature-rich by tool count, with Docker-containerized headless execution, Vision AI analysis, and image-to-3D conversion via TRELLIS.2 — but requires dual 24GB GPUs, making it impractical for most users.

**bonninr/freecad_mcp** (153 stars) takes a simpler approach with just 2 tools (get_scene_info, run_script) — prompt-assisted design through FreeCAD's Python scripting interface.

### CAD-MCP (AutoCAD)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [daobataotie/CAD-MCP](https://github.com/daobataotie/CAD-MCP) | 264 | Python | MIT | 10 |

**Natural language control of AutoCAD, GstarCAD, and ZWCAD.** Drawing operations include lines, circles, arcs, polylines, rectangles, text, hatching, dimensioning, and layer management. The multi-CAD support (three programs) is unusual — most MCP servers target a single application.

### OpenSCAD MCP Servers

Three implementations for the programmer's CAD tool:

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [jhacksman/OpenSCAD-MCP-Server](https://github.com/jhacksman/OpenSCAD-MCP-Server) | 133 | Python | MIT | 10 |
| [quellant/openscad-mcp](https://github.com/quellant/openscad-mcp) | 47 | Python | MIT | 14 |
| [fboldo/openscad-mcp-server](https://github.com/fboldo/openscad-mcp-server) | 0 | TypeScript | MIT | 2 |

**jhacksman/OpenSCAD-MCP-Server** (133 stars) is the most innovative — it converts text prompts and images into parametric 3D models using AI image synthesis + multi-view stereo reconstruction + OpenSCAD. GPU-accelerated remote processing available. This is a text-to-3D pipeline, not just an OpenSCAD wrapper.

**quellant/openscad-mcp** (47 stars) is the most production-ready — 14 tools across rendering, export, and analysis with 80%+ test coverage and 300 passing tests. Security features include path validation and injection prevention.

### Other CAD/Modeling Tools

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [rishigundakaram/cadquery-mcp-server](https://github.com/rishigundakaram/cadquery-mcp-server) | 10 | Python | — | 2 |
| [Svetlana-DAO-LLC/cad-agent](https://github.com/Svetlana-DAO-LLC/cad-agent) | 6 | Python | PolyForm SBL | 9 |
| [Bigchx/mcp_3d_relief](https://github.com/Bigchx/mcp_3d_relief) | 17 | Python | MIT | 1 |

**cadquery-mcp-server** enables conversational 3D modeling with CadQuery — validate and generate parametric CAD models, export to STL/STEP. CadQuery is Python-based, making it a natural fit for MCP integration.

**cad-agent** uses build123d + VTK rendering for AI-driven CAD modeling with visual feedback loops. Note the PolyForm Small Business License — not fully open source.

**mcp_3d_relief** fills a specific niche: convert 2D images into 3D relief models in STL format. Customizable dimensions, optional bases, invertible depth. Simple but useful for engraving and decorative printing.

### Blender MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp) | ~16,300 | Python | MIT | Many |

The **elephant in the room.** By far the most popular 3D modeling MCP server — and one of the most-starred MCP servers period. Not printing-specific, but heavily used in 3D printing pipelines for model creation and preparation. We mention it here for completeness; it deserves its own review.

## Document Printing

### mcp-printer (CUPS)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [steveclarke/mcp-printer](https://github.com/steveclarke/mcp-printer) | 6 | TypeScript | — | 8 |

**The best document printing MCP server.** Prints via CUPS on macOS and Linux:

- **Format support** — PDF, text, markdown, code files with syntax highlighting
- **Queue management** — view, cancel, and manage print jobs
- **Printer control** — list printers, get/set defaults, view configuration
- **Batch printing** — print multiple files in one operation
- **Security** — configurable allowed directories and file types

### Printer-AI-MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [NullYing/Printer-AI-MCP](https://github.com/NullYing/Printer-AI-MCP) | 11 | Python | MIT | 4 |

**Cross-platform printing** for Windows, macOS, and Linux. Simpler than mcp-printer but with broader OS support. Four tools: list printers, get status, get attributes, and print files.

### MCP-Network-CUPS

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [danielrosehill/MCP-Network-CUPS](https://github.com/danielrosehill/MCP-Network-CUPS) | 1 | TypeScript | MIT | 3 |

**Network printing via CUPS over streamable HTTP.** Discover printers on a CUPS print server, add them locally, and send print jobs remotely. Useful for Claude Code or other MCP clients that need to print to network printers.

## Print-on-Demand

### Printify MCP Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [TSavo/printify-mcp](https://github.com/TSavo/printify-mcp) | 24 | TypeScript | — | 15+ |
| [jeffkimble/printify-mcp-server](https://github.com/jeffkimble/printify-mcp-server) | 0 | JavaScript | MIT | 11 |

**TSavo/printify-mcp** is the more capable implementation — shop management, product CRUD, blueprint/variant handling, image upload, and **AI design generation via Replicate Flux.** Create designs with AI and publish directly to Etsy or Shopify. This is a genuine e-commerce automation tool.

**jeffkimble/printify-mcp-server** covers the full Printify API v1 across shops, catalog, uploads, products, and orders — a solid alternative without the AI design generation.

### Printful MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Purple-Horizons/printful-ph-mcp](https://github.com/Purple-Horizons/printful-ph-mcp) | 1 | Python | MIT | 19 |

**Printful** integration with catalog browsing, order management, mockup generation, and shipping calculation. Uses Printful API v2 with v1 fallback. Covers the other major print-on-demand platform alongside Printify.

## What's missing

The gaps are smaller than most verticals we review, but they exist:

- **Cura slicer** — the world's most popular slicer has no MCP server (PrusaSlicer and Bambu Studio have coverage through multi-printer servers)
- **Resin printing** — no Formlabs, Anycubic Photon, or Elegoo Mars-specific servers for resin/SLA workflows
- **Large-format printing** — no plotter, wide-format, or professional print management
- **Label printing** — no ZPL support for Zebra, Dymo, or Brother thermal label printers
- **Receipt/POS printing** — no ESC/POS thermal receipt printer support
- **3D scanning** — no photogrammetry or structured-light scanning pipeline
- **Model marketplaces** — Kiln integrates Thingiverse/MyMiniFactory, but no standalone marketplace browsing tools
- **SolidWorks/Fusion 360** — commercial CAD programs have no MCP integration

## The bottom line

**Rating: 4/5** — This is one of the strongest niche verticals in the MCP landscape.

The 3D printing control ecosystem is genuinely impressive. DMontgomery40/mcp-3D-printer-server covers six printer platforms with STL manipulation, Kiln attempts to automate entire print farm workflows, and OctoEverywhere offers a zero-setup cloud alternative. The CAD ecosystem is even richer — FreeCAD alone has five competing implementations, plus multiple OpenSCAD, AutoCAD, and CadQuery servers.

What elevates this category is the **depth of ambition.** These aren't thin API wrappers — servers like Kiln (430+ tools), the OpenSCAD text-to-3D pipeline, and the BambuStudio defect detection system represent genuine workflow automation. The maker and open-source hardware communities are clearly early adopters of MCP.

Document printing and print-on-demand round out the ecosystem with practical tools. The main gaps (Cura, resin printing, label printing) are notable but don't undermine the strength of what exists.

If you're a maker or run a 3D print operation, this is one of the few verticals where MCP servers can meaningfully automate your workflow today.

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*

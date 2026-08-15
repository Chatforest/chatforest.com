---
title: "Interior Design & Architecture MCP Servers — CAD, BIM, 3D Modeling, SketchUp, Blender, Rhino, and Floor Planning"
date: 2026-03-17T05:00:00+09:00
lastmod: 2026-08-15T09:00:00+09:00
description: "Interior design and architecture MCP servers let AI agents control CAD software, BIM tools, 3D modelers, and design platforms through the Model Context Protocol."
og_description: "Interior design & architecture MCP servers: blender-mcp (25.9k stars), OFFICIAL Blender MCP (Blender Lab), Autodesk Fusion MCP + Fusion Data MCP (official), rhinomcp (1,000+ stars), sketchup-mcp official connector, FreeCAD-MCP (57 tools), SolidWorks + Onshape gaps closed. Rating: 4.5/5."
content_type: "Review"
card_description: "Interior design and architecture MCP servers for CAD control, BIM automation, 3D modeling, and parametric design through AI assistants. **MAJOR UPDATE (April 2026)**: Autodesk launched THREE official MCP servers (Product Help + Fusion MCP + Fusion Data MCP), Blender Lab released the official Blender MCP server, and SketchUp got an official connector — all on April 28, 2026 as part of Anthropic's 'Claude for Creative Work' launch ([anthropic.com](https://www.anthropic.com/news/claude-for-creative-work)). **blender-mcp has grown to 25,900+ stars** as of August 2026 ([GitHub](https://github.com/ahujasid/blender-mcp)). **SolidWorks and Onshape gaps are now partially closed** — community servers eyfel/mcp-server-solidworks (46 tools + 13 resources) and jarvis-onshape-mcp (~60 tools) emerged in March–April 2026. **The biggest gap remains interior design itself** — no dedicated servers for room layout, furniture placement, color palette generation, or rendering engine integration. Rating upgraded 4→4.5/5 on the strength of official vendor momentum."
last_refreshed: 2026-08-15
sources_audited: 2026-08-15
---

Interior design and architecture MCP servers connect AI agents to CAD software, BIM platforms, 3D modelers, and design tools. Instead of manually navigating complex CAD interfaces or switching between modeling applications, these servers let you create, modify, and analyze designs through natural language via the Model Context Protocol.

This review covers **CAD control, BIM automation, 3D modeling, and architectural design tools** — AutoCAD, FreeCAD, Blender, SketchUp, Rhino/Grasshopper, Revit, Fusion 360, and OpenSCAD. For general-purpose 3D file processing, see our [3D Printing review](/reviews/printing-3d-printing-mcp-servers/) if available.

The headline findings: **[blender-mcp](https://github.com/ahujasid/blender-mcp) has grown to 25,900+ GitHub stars** as of August 2026 (up from 17,600 in March) — still one of the most popular MCP servers in existence. **April 28, 2026 was a watershed day for this category**: Autodesk launched three official MCP servers, Blender Lab released the official Blender MCP connector, and SketchUp got an official Anthropic connector — all part of Anthropic's ["Claude for Creative Work" launch](https://www.anthropic.com/news/claude-for-creative-work). **The SolidWorks and Onshape gaps are now partially closed** with community servers from March–April 2026. **The glaring gap remains actual interior design** — room layout, furniture placement, and color palette tools still don't exist.

## What's New (March–May 2026)

### April 28, 2026 — Autodesk Launches Three Official MCP Servers

**The single biggest development in this category's history.** Autodesk shipped three official MCP servers as part of Anthropic's "Claude for Creative Work" launch, directly closing the enterprise CAD gap we cited in our original review:

- **[Autodesk Product Help MCP](https://adsknews.autodesk.com/en/news/product-help-mcp-server/)** (April 9, 2026) — Read-only access to help documentation for 110+ Autodesk products: Fusion, AutoCAD, Revit, Civil 3D, and more. Free, no Autodesk license required. Claude can now look up any Autodesk product documentation directly.

- **[Autodesk Fusion MCP](https://aps.autodesk.com/blog/bringing-fusion-claude-creative-work)** (April 28, 2026) — Local MCP server, requires Fusion 360 running on the machine. Drives modeling operations and executes Fusion commands via AI. Compatible with Claude Desktop, Cursor, and any MCP HTTP client. Autodesk plans additional servers for Revit and more products.

- **Autodesk Fusion Data MCP** (April 28, 2026) — Remote MCP server, no local Fusion required. Queries and manages Fusion design data via Autodesk Platform Services (APS) cloud. Compatible with Claude Desktop and VS Code. Enables connecting Fusion to internal systems and automating multi-step engineering workflows without the desktop app running.

**Significance**: Our original review cited "no official vendor servers from Autodesk, Dassault, Siemens, or PTC" as the category's biggest enterprise gap. With Fusion MCP + Fusion Data MCP, Autodesk becomes the first major mechanical CAD vendor with production official MCP servers.

### April 28, 2026 — Official Blender MCP by Blender Lab

**[Blender Lab](https://www.blender.org/lab/mcp-server/)** (the Blender Foundation's experimental features program) released the **Official Blender MCP server** on April 28, 2026. This is the officially Blender Foundation-endorsed MCP bridge — not a community fork. Key points:

- Built on the open MCP standard — works with Claude and other MCP-capable LLMs, not just Anthropic products
- Provides a direct bridge to Blender's full Python API
- **[Anthropic announced it was joining the Blender Development Fund as Corporate Patron](https://www.cgchannel.com/2026/04/ai-developer-anthropic-becomes-blenders-latest-corporate-patron/)** at €240,000/year (the same tier as [Netflix](https://www.cgchannel.com/2026/01/netflix-donates-e240000year-to-the-blender-development-fund/) and Wacom). **Correction (2026-08-15 audit):** this page previously stated the Corporate Patron status as ongoing fact. It wasn't — the Blender Foundation [downgraded the arrangement to a one-off donation about a week later](https://www.cgchannel.com/2026/05/anthropics-patronage-of-blender-downgraded-to-one-off-donation/) after community backlash over generative AI; Anthropic's logo no longer appears on the Development Fund site and there is no formal Corporate Patron relationship. The MCP connector itself is unaffected — it remains the Blender Foundation's own officially released server.
- Long-term, the official server is the supported path; the community ahujasid/blender-mcp remains more widely installed for now

**[ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp)** has surged to **25,900+ stars** as of August 2026 (up from 17,600 in March) despite — or perhaps because of — the official release announcement.

### April 28, 2026 — SketchUp Official Connector

Anthropic's "Claude for Creative Work" launch on April 28 included an **official [SketchUp Connector for Claude](https://sketchup.trimble.com/en/blog/article/sketchup-claude-connector)** (built by Trimble, SketchUp's owner) — 3D architectural modeling driven directly from conversation, generating native .skp files in a cloud-based SketchUp environment. This is in addition to the community `mhyrr/sketchup-mcp` that has existed since early 2026. **Correction (2026-08-15 audit):** this page previously said the connector gives "zero-setup access for SketchUp users on Claude Free, Pro, and Team plans" — Trimble's own announcement says the opposite: it requires a Claude account, a Trimble ID, **and an active SketchUp subscription**; new users get a free SketchUp entitlement limited to saving up to 30 models before a paid entitlement is required. See our [Claude Connectors for Creative Tools guide](/guides/claude-connectors-creative-tools/) for full coverage of the April 28 launch.

### March–April 2026 — SolidWorks and Onshape Gaps Partially Closed

Two major gaps cited in our original review now have community solutions:

**SolidWorks MCP Servers** (both emerged March 2026):
- **[eyfel/mcp-server-solidworks](https://github.com/eyfel/mcp-server-solidworks)** — Python-based, 46 tools + 13 resources (self-titled "SolidPilot"; see correction below). Released March 17, 2026 — same day as our original review.
- **[vespo92/SolidworksMCP-TS](https://github.com/vespo92/SolidworksMCP-TS)** — Node.js/TypeScript, ~40+ documented tools (see correction below), intelligent COM bridge for SolidWorks automation.

**Onshape MCP Servers** (April 2026):
- **[jarvis-onshape-mcp](https://github.com/ReshefElisha/jarvis-onshape-mcp)** — ~60 tools: sketches, extrudes, fillets, mates, parametric variables, custom FeatureScript. Released April 13, 2026. Leverages Onshape's API-first cloud architecture.
- **[hedless/onshape-mcp](https://github.com/hedless/onshape-mcp)** — Programmatic CAD modeling with document discovery.

**Note**: These are early-stage community servers, not official vendor releases. But they represent the first MCP coverage for two of the world's most widely used mechanical CAD platforms.

### rhinomcp Star Growth

**[jingcheng-chen/rhinomcp](https://github.com/jingcheng-chen/rhinomcp)** has grown to **1,000+ stars** as of August 2026 (was 274 in March). **Correction (2026-08-15 audit):** the previous version of this page reported 346 stars and 55 forks as of the last refresh — growth has accelerated well past that since; current count is roughly 1.0k stars and 89 forks. Still the leading Rhino MCP server with active community use.

---

---

## Blender

### ahujasid/blender-mcp — The Most Popular MCP Server for 3D

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [blender-mcp](https://github.com/ahujasid/blender-mcp) | 25,900+ | Python | MIT | 18+ |

**The dominant Blender-to-AI bridge with massive community adoption** (17,600 → 25,900+ stars since March 2026):

- **Two-way communication** — connects Claude AI to Blender through a socket-based server
- **Object manipulation** — create, modify, and delete 3D objects with natural language
- **Material control** — apply and modify materials and colors
- **Scene inspection** — get detailed information about the current Blender scene
- **Geometry nodes** — status query, node info retrieval, node network creation
- **Asset libraries** — Polyhaven categories/search/download, Sketchfab model search/preview/download
- **AI 3D generation** — Hyper3D/Hunyuan3D model generation, polling, and import
- **Viewport screenshots** — capture and share what Blender is rendering
- **Code execution** — run arbitrary Python code in Blender from Claude

At 25.9k+ stars, this is one of the most popular MCP servers across all categories, period. The breadth of integrations — from Polyhaven assets to Hyper3D generation — makes it genuinely useful for both hobbyists and professionals.

### seehiong/blender-mcp-n8n — Blender via n8n Automation

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [blender-mcp-n8n](https://github.com/seehiong/blender-mcp-n8n) | 47 | — | MIT | 94 |

**Automates Blender 3D modeling from n8n workflows:**

- **94 tools** for modeling, materials, lighting, rendering, and animation
- **n8n integration** — trigger Blender operations from automation workflows
- **Comprehensive coverage** — goes beyond basic object creation into lighting and rendering

An interesting approach that connects Blender to the broader automation ecosystem rather than just direct AI chat.

### Official Blender MCP — Blender Lab (NEW April 2026)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Official Blender MCP](https://www.blender.org/lab/mcp-server/) | — | Python | — | Multiple |

**The officially Blender Foundation-endorsed MCP server** (April 28, 2026):

- **Blender Lab project** — the Blender Foundation's experimental features program
- **Open MCP standard** — works with Claude and any other MCP-compatible LLM
- **Full Python API access** — direct bridge to Blender's complete scripting interface
- **Anthropic briefly held Corporate Patron status** — [announced](https://www.cgchannel.com/2026/04/ai-developer-anthropic-becomes-blenders-latest-corporate-patron/) at €240K/year, then [downgraded to a one-off donation](https://www.cgchannel.com/2026/05/anthropics-patronage-of-blender-downgraded-to-one-off-donation/) about a week later after community backlash — see the correction above; doesn't affect the MCP connector itself
- **Long-term supported path** — vs. community ahujasid/blender-mcp (still more widely installed)

---

## AutoCAD

### puran-water/autocad-mcp — AutoLISP Execution and P&ID Symbols

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [autocad-mcp](https://github.com/puran-water/autocad-mcp) | 451 | Python | MIT | 8 |

**The most mature AutoCAD MCP server with industrial features:**

- **Freehand AutoLISP execution** — turns the server from a fixed command set into an extensible automation platform
- **8 consolidated tools** — drawing, undo/redo, file operations
- **P&ID symbol support** — integrates with the third-party [CAD Tools Online P&ID Symbols Library](https://www.cadtoolsonline.com/pid-symbols-library-autocad.htm) (335 symbols, ISA 5.1-2009 standard) for process and instrumentation diagrams. **Correction (2026-08-15 audit):** this page previously stated "600+ ISA 5.1-2009 standard symbols" as if bundled with the server itself — the server's own README doesn't state a symbol count, and the CAD Tools Online library it depends on actually ships 335 symbols, not 600+.
- **Dual backends** — File IPC (requires AutoCAD) or ezdxf (headless DXF generation without AutoCAD)
- **Focus-free dispatch** — operates without needing AutoCAD to be the active window
- **Robust IPC** — ESC prefix and UTF-8 fallback for reliable communication

The ezdxf headless backend is particularly notable — you can generate DXF files without having AutoCAD installed at all.

### AnCode666/multiCAD-mcp — One Server, Four CAD Platforms

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [multiCAD-mcp](https://github.com/AnCode666/multiCAD-mcp) | 85 | Python | Apache-2.0 | 7 |

**Cross-platform CAD control via AI assistants:**

- **7 unified MCP tools** covering 56 underlying CAD commands — comprehensive drawing, layer, entity, and file management
- **Multi-platform** — supports AutoCAD, ZWCAD, GstarCAD, and BricsCAD
- **Batch operations** (v0.1.1+) — 60-70% fewer API calls when managing multiple items
- **Natural language** — "Draw a red circle at 50,50 with radius 25" or complex instructions
- **Windows only** — uses COM technology for CAD communication

The cross-platform approach is smart — supporting 4 CAD platforms through one MCP server means you're not locked into a single vendor.

### daobataotie/CAD-MCP — Natural Language CAD Control

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [CAD-MCP](https://github.com/daobataotie/CAD-MCP) | 499 | — | MIT | Multiple |

**CAD control via natural language instructions:**

- **Multi-CAD support** — AutoCAD, GstarCAD (GCAD), and ZWCAD
- **Natural language processing** — combines NLP with CAD automation
- **Drawing operations** — create and modify drawings through conversational commands

### chichicaste/mcp-autocad-server — Learning-Focused AutoCAD Integration

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-autocad-server](https://github.com/chichicaste/mcp-autocad-server) | 0 | — | — | Multiple |

**Natural language interaction with AutoCAD:**

- **Create, modify, and analyze drawings** through LLMs like Claude
- **CAD element data storage** — stores and queries element data
- **Learning reference** — the author notes this is currently for learning reference, with basic communication implemented but tool functions not yet complete

---

## FreeCAD

### proximile/FreeCAD-MCP — The Most Feature-Rich CAD MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [FreeCAD-MCP](https://github.com/proximile/FreeCAD-MCP) | 4 | Python | MIT | 57 |

**A powerhouse CAD server with AI generation capabilities:**

- **57 MCP tools** — one of the highest tool counts among CAD MCP servers (only spkane/freecad-addon-robust-mcp-server, further down, claims more at 150+)
- **Docker headless execution** — containerized FreeCAD with optional VNC GUI access
- **Multi-AI support** — works with Claude, GPT-4o, and Gemini
- **TRELLIS.2 integration** — image-to-3D model generation
- **ComfyUI integration** — text-to-image generation for design concepts
- **Vision AI analysis** — Cosmos VLM for model analysis, SAM3 for segmentation
- **Gradio web interface** — debugging UI with request tracking and image gallery
- **Cloudflare tunnels** — public URL access without port forwarding
- **Dual GPU support** — optimized for dual 24GB 3090 setup with automatic quantization

This goes far beyond basic CAD control — it's essentially an AI-powered design studio with 3D generation, vision analysis, and headless rendering all in one package.

### bonninr/freecad_mcp — Direct Claude-FreeCAD Connection

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [freecad_mcp](https://github.com/bonninr/freecad_mcp) | 218 | Python | — | Multiple |

**Connects FreeCAD to Claude AI through MCP:**

- **Direct interaction** — Claude controls FreeCAD for prompt-assisted CAD 3D design
- **MCP-ready** — works with Claude and other MCP-compatible tools like Cursor

### lucygoodchild/freecad-mcp-server — Cross-Platform FreeCAD Basics

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [freecad-mcp-server](https://github.com/lucygoodchild/freecad-mcp-server) | 8 | Python | — | Multiple |

**Basic FreeCAD operations via MCP:**

- **Geometry creation** — basic 3D shapes and objects
- **Boolean operations** — union, intersection, subtraction
- **Custom script execution** — run FreeCAD Python scripts
- **Cross-platform** — Windows, macOS, and Linux

### spkane/freecad-addon-robust-mcp-server — MCP Bridge Workbench

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [freecad-addon-robust-mcp-server](https://github.com/spkane/freecad-addon-robust-mcp-server) | 183 | Python | — | 150+ |

**FreeCAD Robust MCP Suite with dedicated workbench:**

- **150+ MCP tools** — the highest tool count in the FreeCAD category, per the repo's own README
- **MCP Bridge Workbench** — integrates directly into FreeCAD's UI
- **Docker support** — available as a Docker image for containerized use
- **Addon architecture** — installs as a FreeCAD addon for tight integration

### contextform/freecad-mcp — Open-Source Automation

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [freecad-mcp](https://github.com/contextform/freecad-mcp) | 110 | — | — | 45+ |

**Open-source MCP server for FreeCAD automation**, offering 45+ operations across PartDesign, Part modeling, and view control. Another option in the growing FreeCAD MCP ecosystem.

---

## SketchUp

### mhyrr/sketchup-mcp — Architectural Modeling and Woodworking

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [sketchup-mcp](https://github.com/mhyrr/sketchup-mcp) | 375 | Ruby/Python | MIT | Multiple |

**SketchUp-to-AI bridge with unique woodworking tools:**

- **TCP socket connection** — two-way communication between Claude and SketchUp
- **Component manipulation** — create, modify, delete, and transform components
- **Material control** — apply and modify materials
- **Scene inspection** — detailed information about the current scene
- **Selection handling** — work with selected objects
- **Ruby code evaluation** — execute arbitrary Ruby code directly in SketchUp
- **Woodworking joints** — mortise and tenon, dovetail, finger joint (unique to this server)
- **Planned features** — lap joints, miter joints, dowel joints, pocket holes, grain direction, wood species libraries

The woodworking joinery tools make this uniquely valuable for furniture design and crafting — no other CAD MCP server offers this level of woodworking-specific functionality.

### BearNetwork-BRNKC/SketchUp-MCP — Traditional Chinese Localized

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [SketchUp-MCP](https://github.com/BearNetwork-BRNKC/SketchUp-MCP) | 24 | — | — | Multiple |

**SketchUp MCP integration with Traditional Chinese localization.** A community fork targeting Chinese-speaking users.

---

## Rhino & Grasshopper

### jingcheng-chen/rhinomcp — The Leading Rhino MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [rhinomcp](https://github.com/jingcheng-chen/rhinomcp) | 1,000+ | Python | MIT | ~30 |

**The most popular Rhino-to-AI bridge:**

- **Object manipulation** — create, modify, and delete 3D objects
- **Document inspection** — detailed information about the Rhino document
- **Script execution** — run Python scripts directly in Rhino
- **Object selection** — filter by name, color, category with logic operators
- **Layer management** — get, set, create, or delete layers
- **JSON-based TCP protocol** — clean, simple communication protocol
- **Available on PyPI** — easy installation via pip

At 1,000+ stars (89 forks) as of August 2026, this leads the Rhino MCP ecosystem with a clean, well-documented implementation.

### veoery/GH_mcp_server — Direct Rhino + Grasshopper Interaction

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [GH_mcp_server](https://github.com/veoery/GH_mcp_server) | 31 | Python | — | Multiple |

**LLM-to-Rhino/Grasshopper bridge for designers:**

- **3dm file analysis** — analyze existing Rhino files
- **3D modeling** — direct modeling in Rhino
- **GHPython generation** — automatically generate Grasshopper Python scripts based on user guidance
- **Designer-focused** — built for design workflows, not just technical CAD

### dongwoosuk/rhino-grasshopper-mcp — ML Auto-Layout

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [rhino-grasshopper-mcp](https://github.com/dongwoosuk/rhino-grasshopper-mcp) | 16 | Python | — | Multiple |

**AI-powered Rhino/Grasshopper with machine learning layout:**

- **ML-based automatic layout optimization** — uses machine learning for spatial arrangement
- **Direct AI integration** — brings AI capabilities into Rhino/Grasshopper workflows

### alfredatnycu/grasshopper-mcp — Component Creation and Intent Recognition

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [grasshopper-mcp](https://github.com/alfredatnycu/grasshopper-mcp) | 94 | — | — | Multiple |

**Bridging server between Grasshopper and Claude Desktop:**

- **Component creation** — create and connect Grasshopper components via MCP
- **High-level intent recognition** — understands design intent, not just commands
- **MCP standard** — follows the protocol specification for reliable integration

### reer-ide/rhino_mcp — Multi-Tool Rhino Integration

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [rhino_mcp](https://github.com/reer-ide/rhino_mcp) | 26 | — | — | Multiple |

**Connects Rhino, Grasshopper, and more to Claude AI:**

- **Prompt-assisted 3D modeling** — create and manipulate scenes through conversation
- **Multi-tool** — integrates Rhino, Grasshopper, and additional tools

---

## Revit / BIM

### revit-mcp/revit-mcp — Archived; Successor Is a Community Fork

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [revit-mcp](https://github.com/revit-mcp/revit-mcp) (ARCHIVED) | 453 | C#/Python | MIT | Multiple |
| [mcp-servers-for-revit](https://github.com/mcp-servers-for-revit/mcp-servers-for-revit) (successor) | 289 | TypeScript/C# | — | Multiple |

**Correction (2026-08-15 audit):** the original `revit-mcp/revit-mcp` repo has been **archived** (as of February 25, 2026) — its own README states it's "being archived in favour of the mono repo approach." The successor is [mcp-servers-for-revit/mcp-servers-for-revit](https://github.com/mcp-servers-for-revit/mcp-servers-for-revit), described in its README as "a fork of the original revit-mcp project with additional tools and functionality improvements," not an official Autodesk project. This page previously listed the archived repo at 18 stars with no archive notice; actual star count on the archived repo is 453, and the still-maintained successor has 289.

**Still the only major BIM platform with community MCP support:**

- **CRUD operations** — create, read, update, delete Revit elements through AI
- **Plugin architecture** — a Revit add-in receives AI commands within Revit
- **Command sets** — wraps Revit external events as executable commands
- **Extensible** — developers can add functionality to the command set or create custom work sets
- **MCP protocol clients** — works with Claude, Cline, and other MCP-compatible clients

Revit is the industry standard for BIM in architecture, and having MCP support — even early-stage and community-maintained — opens up AI-assisted building design workflows that were previously impossible.

---

## Fusion 360

### AuraFriday/Fusion-360-MCP-Server — Thread-Safe Fusion Control

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Fusion-360-MCP-Server](https://github.com/AuraFriday/Fusion-360-MCP-Server) | 118 | Python | — | Multiple |

**Thread-safe Fusion 360 control via MCP:**

- **Thread-safe architecture** — all API calls happen on main thread to prevent crashes
- **Multi-AI support** — works with Claude, ChatGPT, and other MCP clients
- **Parametric modeling** — leverages Fusion 360's parametric design capabilities

### mycelia1/fusion360-mcp-server — Script Generation and Execution

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [fusion360-mcp-server](https://github.com/mycelia1/fusion360-mcp-server) | 5 | Python | — | 13+ |

**Generate and execute Fusion 360 scripts via AI:**

- **Script generation** — AI creates Fusion 360 scripts from natural language
- **Direct execution** — runs generated scripts in Fusion 360
- **Multi-client** — works with Claude, Cursor, or any MCP client

### Joe-Spencer/fusion-mcp-server — Independent Community Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [fusion-mcp-server](https://github.com/Joe-Spencer/fusion-mcp-server) | 48 | — | — | Multiple |

**Provides Autodesk Fusion resources and tools to AI clients.** **Correction (2026-08-15 audit):** a previous version of this page claimed this was "the technical foundation for Autodesk's three official MCP servers" and that its author "is an Autodesk employee." Neither claim is supported by the repo's README, Autodesk's own announcement of the official servers, or any other source found — it's cut as unverifiable. This appears to be an independent, non-official community project. If you're on Fusion 360, prefer the official **Autodesk Fusion MCP** and **Autodesk Fusion Data MCP** now that they're available.

### Autodesk Fusion MCP — Official (NEW April 2026)

| Server | Source | Setup | Stars |
|--------|--------|-------|-------|
| Autodesk Fusion MCP | Official (Autodesk) | Local, requires Fusion running | Official |

**Drive Fusion 360 modeling through AI** (April 28, 2026):

- **Local server** — Fusion 360 must be running on the machine
- **Modeling commands** — create, modify, and execute Fusion operations via natural language
- **Compatible with** Claude Desktop, Cursor, any MCP HTTP client
- **Part of Anthropic's "Claude for Creative Work" launch**

### Autodesk Fusion Data MCP — Official (NEW April 2026)

| Server | Source | Setup | Stars |
|--------|--------|-------|-------|
| Autodesk Fusion Data MCP | Official (Autodesk) | Remote, no Fusion install needed | Official |

**Query and manage Fusion design data from the cloud** (April 28, 2026):

- **Remote server** — no local Fusion 360 installation required
- **Cloud data access** — queries Fusion design history, assemblies, and project data via Autodesk Platform Services
- **Compatible with** Claude Desktop and VS Code
- **Use cases** — connect Fusion data to internal systems, automate multi-step engineering workflows

### Autodesk Product Help MCP — Official (NEW April 2026)

| Server | Source | Setup | Coverage |
|--------|--------|-------|----------|
| Autodesk Product Help MCP | Official (Autodesk) | Hosted, free | 110+ products |

**Access Autodesk documentation for 110+ products** (April 9, 2026):

- **Read-only** — search and retrieve Autodesk help docs
- **110+ products covered** — Fusion 360, AutoCAD, Revit, Civil 3D, Maya, 3ds Max, and more
- **Free, no Autodesk license required**

---

## SolidWorks (NEW)

### eyfel/mcp-server-solidworks (SolidPilot) — Python Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-solidworks](https://github.com/eyfel/mcp-server-solidworks) | 212 | Python | AGPL-3.0 | 46 |

**Community SolidWorks MCP server**, self-titled "SolidPilot" in its own README, described there as "a working prototype / early alpha":

- **46 MCP tools + 13 MCP resources** — comprehensive SolidWorks automation coverage. **Correction (2026-08-15 audit):** this page previously claimed "90+ tools" — the repo's own README states 46 tools and 13 resources, roughly half the earlier figure.
- **Python-first implementation** — standard Python toolchain
- **Natural language CAD** — drive SolidWorks operations through AI assistants
- **AGPL-3.0 licensed**, with a separate commercial license offered for organizations that can't comply with the copyleft terms — worth checking before commercial use

### vespo92/SolidworksMCP-TS — TypeScript COM Bridge

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [SolidworksMCP-TS](https://github.com/vespo92/SolidworksMCP-TS) | 214 | TypeScript | MIT | ~40+ |

**Node.js/TypeScript SolidWorks MCP server** with intelligent COM bridge, described in its own README as "Alpha / Experimental":

- **~40+ documented tools** across modeling, sketching, drawing, export, analysis, VBA generation, and macro operations. **Correction (2026-08-15 audit):** this page previously claimed "88 working tools" — the repo's own README documents roughly 40+ tools and notes most remain untested against a live SolidWorks instance, so "working" overstated their maturity.
- **COM bridge architecture** — interfaces with SolidWorks via Windows COM/API
- **TypeScript implementation** — for teams preferring the Node.js ecosystem

**Note**: SolidWorks is the most widely used professional mechanical CAD platform. Both of these are early-stage community servers — no official SolidWorks MCP server exists. But the gap cited in our original review is now partially closed.

---

## Onshape (NEW)

### jarvis-onshape-mcp — Full Parametric Cloud CAD

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [jarvis-onshape-mcp](https://github.com/ReshefElisha/jarvis-onshape-mcp) | 158 | — | MIT | ~60 |

**A [Claude Code plugin](https://github.com/ReshefElisha/jarvis-onshape-mcp) for Onshape** (April 13, 2026) — **Correction (2026-08-15 audit):** this page previously called it a "Claude Opus 4.7 plugin"; the repo's own README describes it simply as a "Claude Code plugin that lets Claude drive real Onshape CAD," with no tie to a specific model version:

- **~60 tools** — sketches, extrudes, fillets, mates, parametric variables, custom FeatureScript
- **Onshape's API-first design** makes this the cloud CAD platform best positioned for MCP
- **Full parametric workflow** — create, modify, and query Onshape designs through conversation

### hedless/onshape-mcp — Document Discovery

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [hedless/onshape-mcp](https://github.com/hedless/onshape-mcp) | 126 | — | — | 45 |

**Programmatic CAD modeling** with Onshape document discovery, sketch/feature creation (extrude, revolve, fillet), assembly management with mates, and export — 45 tools across the Onshape REST API.

---

## OpenSCAD

### quellant/openscad-mcp — Multi-Perspective Rendering

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [openscad-mcp](https://github.com/quellant/openscad-mcp) | 126 | Python | MIT | 13 |

**Production-ready OpenSCAD rendering via MCP:**

- **13 tools** across rendering, export/model management, analysis/validation, and project support. **Correction (2026-08-15 audit):** this page previously said "3" tools — that undercounted the rendering-category tools alone; the repo exposes 13 total.
- **Single view rendering** — render individual perspectives with customizable camera
- **Multi-perspective rendering** — front, back, left, right, top, bottom, isometric views
- **Animation support** — turntable animations for model visualization
- **300 tests** — 80%+ code coverage, 100% integration test success (per the repo's own README/test suite — not independently re-run for this audit)
- **Base64 PNG output** — renders returned as encoded images
- **Async processing** — built on FastMCP for non-blocking operation

### fboldo/openscad-mcp-server — STL and PNG Output

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [openscad-mcp-server](https://github.com/fboldo/openscad-mcp-server) | 1 | Python | — | Multiple |

**Renders PNG previews and STL geometry from OpenSCAD code.** Focused on generating both visual previews and printable 3D files.

---

## Specialized Tools

### Svetlana-DAO-LLC/cad-agent — Self-Contained Rendering for 3D Printing

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cad-agent](https://github.com/Svetlana-DAO-LLC/cad-agent) | 32 | Python | — | Multiple |

**AI-driven CAD modeling for 3D printing:**

- **build123d** — uses the build123d Python library for parametric modeling
- **Self-contained rendering** — the container does all rendering work
- **Visual feedback** — returns images the agent can interpret
- **3D printing focused** — designed for printable model generation

### Bigchx/mcp_3d_relief — Image to 3D Relief Models

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp_3d_relief](https://github.com/Bigchx/mcp_3d_relief) | 22 | Python | — | Multiple |

**Converts 2D images into 3D relief models:**

- **Image-to-STL** — transforms flat images into 3D relief surfaces
- **3D printing ready** — outputs STL format suitable for printing or rendering

---

## What's Missing

### Gaps Closed Since March 2026

- **Autodesk/Fusion 360** — ✅ Three official MCP servers launched April 28, 2026
- **Blender (official)** — ✅ Blender Lab official server launched April 28, 2026
- **SketchUp (official)** — ✅ Official Anthropic connector launched April 28, 2026
- **SolidWorks** — ✅ Partially closed — community servers eyfel/mcp-server-solidworks (46 tools + 13 resources) and SolidworksMCP-TS (~40+ tools) emerged March 2026. No official SolidWorks server yet.
- **Onshape** — ✅ Partially closed — jarvis-onshape-mcp (~60 tools, April 2026). No official Onshape server yet.

### Gaps Still Open

The biggest remaining gap is **interior design itself**. Despite the strong CAD/3D modeling coverage, there are still no MCP servers for:

- **Room layout and space planning** — no automated furniture placement, no traffic flow analysis
- **Floor plan generation** — no text-to-floor-plan tools
- **Color palette and material selection** — no integration with paint brands, fabric libraries, or finish catalogs
- **Furniture catalogs** — no IKEA, Wayfair, Pottery Barn, or other retailer APIs
- **AR/VR visualization** — no augmented reality room preview tools
- **Rendering engines** — no V-Ray, Lumion, Enscape, or KeyShot MCP servers
- **Landscape architecture** — no garden design, hardscape planning, or plant databases
- **Building code compliance** — no zoning, ADA, or fire code checking
- **Lighting design** — no illumination calculations or fixture selection
- **Acoustics** — no room acoustic analysis or soundproofing recommendations
- **Structural engineering** — no load calculations or structural analysis
- **Cost estimation** — no material quantity takeoffs or budget planning
- **Dassault Systèmes (SOLIDWORKS, CATIA)** — still no official server
- **Siemens (NX, Solid Edge)** — still no official server
- **PTC (Creo)** — still no official server

---

## Bottom Line

April 28, 2026 was a watershed moment for this category. Autodesk launched three official MCP servers (Fusion MCP, Fusion Data MCP, Product Help), Blender Lab released the official Blender MCP connector, and SketchUp got an official Anthropic connector — all in a single day, all tied to Anthropic's "Claude for Creative Work" launch. This directly addressed the "no official vendor servers" critique from our original review.

The category is now **exceptional on the CAD/3D modeling side** with strong official vendor backing, community star growth (blender-mcp at 25,900+ stars), and newly partial coverage for SolidWorks and Onshape. Rhino/Grasshopper has 5+ active implementations. Every major 3D modeling platform now has at least one working MCP server, and the most important ones (Blender, Fusion 360) now have official servers.

But if you're looking for AI-assisted **interior design** — "help me arrange furniture in my living room" or "suggest a color palette for this bedroom" — MCP servers still can't help you. The gap between powerful CAD automation tools and accessible design decision tools remains completely unfilled. Rendering engines (V-Ray, Lumion, Enscape), building code compliance, lighting design, and furniture catalogs are all zero-coverage zones.

**Rating: 4.5/5** *(upgraded from 4/5)* — Official vendor momentum (Autodesk, Blender Lab, SketchUp) plus SolidWorks/Onshape partial coverage pushes this above a 4. The remaining half-point reflects the complete absence of interior design workflow tools, rendering engine integration, and the major industrial CAD vendors (Dassault, Siemens, PTC) still sitting on the sidelines.

**Category**: [Design & Creative MCP Servers](/categories/design-creative/)

*This review was last edited on 2026-08-15 using Claude Sonnet 5 (Anthropic).*

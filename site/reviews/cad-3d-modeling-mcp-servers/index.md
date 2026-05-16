# CAD & 3D Modeling MCP Servers — Blender, FreeCAD, AutoCAD, KiCad, SolidWorks, Fusion 360, OpenSCAD, and More

> CAD and 3D modeling MCP servers reviewed: Official Blender MCP (Blender Lab + Anthropic, April 2026), Autodesk official servers (Fusion MCP + Fusion Data MCP + Product Help), ahujasid/blender-mcp (20,000 stars), FreeCAD MCP (617 stars), KiCad (405 stars). Rating: 4/5.


CAD and 3D modeling MCP servers let AI agents create, modify, and analyze engineering designs and 3D models through natural language. The category spans **3D modeling** (Blender, OpenSCAD), **parametric CAD** (FreeCAD, Fusion 360, SolidWorks, Onshape), **2D drafting** (AutoCAD, GstarCAD, ZWCAD), and **electronic design automation** (KiCad PCB design).

**April 28, 2026 changed this category.** As part of Anthropic's "Claude for Creative Work" launch, both Blender and Autodesk moved from community-only to official MCP support in a single day. Anthropic announced an official Blender connector (developed by Blender Lab) and joined the Blender Development Fund as a Corporate Patron at €240,000/year. Autodesk simultaneously launched two official Fusion MCP servers — local for modeling and remote for cloud data — after having already released a Product Help MCP server on April 9. The biggest gap in this category — **no official vendor servers from Autodesk** — is now closed.

The headline: **ahujasid/blender-mcp** grew from 17,800 → ~20,000 stars and remains the most widely installed Blender integration. The official Blender Lab server is the long-term supported path. **FreeCAD MCP** (617 stars) and **KiCad MCP** (405 stars) show genuine demand from the open-source engineering community. **AutoCAD MCP** (177 stars) demonstrates surprisingly sophisticated architecture with dual backends and focus-free dispatch. Dassault Systèmes (SolidWorks), Siemens, and PTC remain the outstanding vendor gaps.

## 3D Modeling & Visualization

### Official Blender MCP (Blender Lab)

| Detail | Info |
|--------|------|
| [blender.org/lab/mcp-server](https://www.blender.org/lab/mcp-server/) | Official |
| Developer | Blender Foundation (Blender Lab) |
| Announced | April 28, 2026 |
| License | Open source |
| Sponsor | Anthropic (Corporate Patron, €240,000/year) |

On April 28, 2026, Blender announced an official MCP connector developed by Blender Lab — the Foundation's program for experimental features. Anthropic became a Blender Development Fund Corporate Patron at €240,000/year to support the integration. The connector is built on the open MCP standard, so it works with any MCP-capable LLM, not just Claude.

**What it offers:** A direct bridge to Blender's Python API from any MCP client. The same scene inspection, Python code execution, and automation capabilities as the community server — but developed and maintained by the Blender Foundation itself. For long-term production use, the official server is the supported path.

The community server (ahujasid/blender-mcp, below) remains more widely installed for now and includes third-party integrations (Poly Haven, Hyper3D Rodin, Sketchfab) that may not exist in the official version yet.

### Blender MCP (Community)

| Detail | Info |
|--------|------|
| [ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp) | ~20,000 stars |
| License | MIT |
| Language | Python |
| Transport | stdio (socket-based) |

The most widely installed CAD/3D MCP server. Connects Blender to Claude AI through a socket-based server running inside Blender as an addon. Grew from 17,800 → ~20,000 stars since March 2026 — boosted further by Anthropic's official Blender announcement and Corporate Patron news.

### What Works Well

**Breadth of integration.** Object creation, modification, deletion, material application, scene inspection, arbitrary Python code execution within Blender, viewport screenshots — this covers the full modeling workflow. The `execute_code` capability means anything Blender's Python API can do, the AI can do.

**Asset ecosystem integration.** Built-in Poly Haven integration for downloading HDRI environments, textures, and 3D models. Hyper3D Rodin integration for AI-generated 3D models — describe an object in text and get a 3D mesh. Sketchfab model search and download. These make it genuinely useful for rapid scene assembly.

**Community momentum.** 17,800 stars means extensive testing, active issue resolution, and a large user base discovering and reporting edge cases. This is one of the most battle-tested MCP servers in any category.

### What Doesn't Work Well

**Art-focused, not engineering-focused.** Blender's strength is organic modeling, animation, and rendering — not parametric engineering design. You won't get constraint-driven sketches, parametric dimensions, or manufacturing-ready output. For engineering CAD, look at FreeCAD or Fusion 360 servers below.

**Socket architecture limitations.** The Blender addon runs a socket server that the MCP server connects to. This means Blender must be running first, and network configuration can be finicky — especially in containerized or remote environments.

### OpenSCAD MCP

| Detail | Info |
|--------|------|
| [jhacksman/OpenSCAD-MCP-Server](https://github.com/jhacksman/OpenSCAD-MCP-Server) | ~135 stars |
| License | MIT |
| Language | Python |
| Tools | 10 |

Takes a unique approach: **text-to-3D via AI image generation and multi-view reconstruction.** Instead of directly scripting OpenSCAD geometry, it generates concept images using Google Gemini or Venice.ai, creates multi-view images for 3D reconstruction, and produces OpenSCAD-compatible output. Supports export to OBJ, STL, PLY, SCAD, CSG, AMF, and 3MF formats.

The standout feature is **direct 3D printer support** — network-based printer discovery and printing from within the MCP workflow. The image approval workflow lets you review AI-generated concepts before committing to 3D reconstruction, which is smart given how unpredictable generative 3D can be.

Three other OpenSCAD MCP servers exist ([rahulgarg123/openscad-mcp](https://github.com/rahulgarg123/openscad-mcp), [quellant/openscad-mcp](https://github.com/quellant/openscad-mcp), [fboldo/openscad-mcp-server](https://github.com/fboldo/openscad-mcp-server)) — these focus on rendering SCAD code to PNG/STL rather than the generative AI pipeline.

## Parametric CAD

### FreeCAD MCP

| Detail | Info |
|--------|------|
| [neka-nat/freecad-mcp](https://github.com/neka-nat/freecad-mcp) | ~617 stars |
| License | MIT |
| Language | Python |
| Tools | 10 |

The most popular open-source engineering CAD MCP server. Runs as a FreeCAD addon with an RPC server that communicates with Claude Desktop.

### What Works Well

**Parts library integration.** `insert_part_from_library` and `get_parts_list` let the AI browse and insert from FreeCAD's component library — useful for assembly workflows where you're combining standard parts.

**Remote operation.** Supports IP-based access control via CIDR whitelisting, binding to `0.0.0.0` for network access. This enables running FreeCAD on a powerful workstation while controlling it from a laptop.

**Code execution escape hatch.** `execute_code` runs arbitrary Python scripts within FreeCAD's environment, giving access to the full FreeCAD Python API. When the 10 built-in tools aren't enough, the AI can script anything FreeCAD can do.

### What Doesn't Work Well

**Limited built-in tools.** Only 10 tools — create/edit/delete objects, document management, parts library, and view capture. No direct tools for sketching constraints, boolean operations on bodies, or assembly mates. The `execute_code` tool compensates, but it requires the AI to generate correct FreeCAD Python API calls.

**Visual feedback only.** `get_view` captures viewport screenshots, but there's no structured way to query geometry dimensions, constraints, or topology. The AI sees the model visually but can't programmatically inspect it in detail.

A second FreeCAD server ([lucygoodchild/freecad-mcp-server](https://github.com/lucygoodchild/freecad-mcp-server), 5 stars, TypeScript) offers 7 tools with explicit boolean operations (union, cut, common) and primitive creation (box, cylinder, sphere) — more structured but less adopted.

### Autodesk Fusion MCP (Official)

| Detail | Info |
|--------|------|
| Autodesk Fusion MCP | Official, local |
| Autodesk Fusion Data MCP | Official, remote (cloud) |
| Autodesk Product Help MCP | Official, read-only docs |
| Announced | April 28, 2026 (Fusion); April 9 (Product Help) |
| Available | Autodesk App Store + autodesk.com/solutions/autodesk-ai/autodesk-mcp-servers |

On April 28, 2026 — as part of Anthropic's "Claude for Creative Work" launch ([full guide](/guides/claude-connectors-creative-tools/)) — Autodesk announced two official Fusion MCP servers:

**Autodesk Fusion MCP** runs locally alongside a running Fusion instance. It provides modeling capabilities and executes Fusion commands directly. Compatible with Claude Desktop, Cursor, and any MCP-capable HTTP client. This is the "do CAD work" server — AI agents can drive Fusion through natural language design intent.

**Autodesk Fusion Data MCP** runs remotely (no Fusion installation required). It queries and manages Fusion design data through Autodesk's cloud services. Compatible with Claude Desktop and VS Code. This is the "query CAD data" server — useful for downstream consumers of Fusion designs who don't need to run Fusion itself.

On April 9, Autodesk had already announced the **Autodesk Product Help MCP Server** — a read-only service providing AI agents access to help documentation across 110+ Autodesk products (Fusion, AutoCAD, Revit, Civil 3D, and more). Available at no cost.

Autodesk is a gold-level member of the Agentic AI Foundation and plans additional MCP servers for Revit and other products.

The **original community server** by [Joe-Spencer](https://github.com/Joe-Spencer/fusion-mcp-server) was developed by an Autodesk employee and served as the technical foundation for this work. **JustusBraitinger's server** (30+ tools — sketching, features, analysis, export) remains the most feature-complete Fusion MCP implementation for power users who need capabilities not yet in the official server.

### Fusion 360 (Community)

| Server | Stars | Language | Tools |
|--------|-------|----------|-------|
| [JustusBraitinger/Autodesk-Fusion-360-MCP-Server](https://github.com/JustusBraitinger/Autodesk-Fusion-360-MCP-Server) | 19 | Python | 30+ |
| [Joe-Spencer/fusion-mcp-server](https://github.com/Joe-Spencer/fusion-mcp-server) | — | Python | baseline |

**JustusBraitinger's server** is the most feature-complete community option: 30+ tools across sketching & creation, feature & modification, analysis & control, and export (STEP, STL). Uses an event-driven task queue to handle Fusion 360's non-thread-safe API. This remains valuable for capabilities not yet exposed by the official servers.

### SolidWorks

| Server | Stars | Language | License |
|--------|-------|----------|---------|
| [eyfel/mcp-server-solidworks](https://github.com/eyfel/mcp-server-solidworks) | ~67 | Python/C# | MIT |

**SolidPilot** — an open-source AI assistant for SolidWorks with a four-layer architecture: Claude UI → Python prompt generation → C# version-aware adapter → COM bridge via PythonNET. The version-aware design is thoughtful — SolidWorks COM APIs change between versions, and the C# adapter layer handles those differences.

Currently more of an architectural framework than a fully-featured tool — the COM bridge pattern is solid, but the tool surface is limited. SolidWorks' proprietary nature and COM-based API make MCP integration inherently harder than with open-source tools.

Two other SolidWorks servers exist: [vespo92/SolidworksMCP-TS](https://github.com/vespo92/SolidworksMCP-TS) (TypeScript, dynamic VBA macro generation) and an espocorp variant (VBA script generation, batch operations, drawing automation).

### Onshape

| Detail | Info |
|--------|------|
| [BLamy/onshape-mcp](https://github.com/BLamy/onshape-mcp) | ~11 stars |
| License | MIT |
| Language | TypeScript |
| Commits | 1 |

Minimal but architecturally interesting — Onshape's cloud-native, browser-based CAD platform has a comprehensive REST API, making it the easiest commercial CAD platform to integrate with MCP. Only 1 commit and 11 stars signal this is early proof-of-concept. Onshape's API-first design makes it the strongest candidate for a future official vendor MCP server.

## 2D Drafting (AutoCAD)

### CAD-MCP

| Detail | Info |
|--------|------|
| [daobataotie/CAD-MCP](https://github.com/daobataotie/CAD-MCP) | ~270 stars |
| License | MIT |
| Language | Python |
| Functions | 10 |

The most popular AutoCAD-family MCP server. Controls **AutoCAD, GstarCAD, and ZWCAD** through natural language commands. Ten drawing functions: `draw_line`, `draw_circle`, `draw_arc`, `draw_polyline`, `draw_rectangle`, `draw_text`, `draw_hatch`, `add_dimension`, `save_drawing`, `process_command`. Layer management and color recognition included.

The multi-CAD support is the differentiator — GstarCAD and ZWCAD are popular AutoCAD alternatives in China and other markets, and this server works across all three. Simple drawing operations only — no block editing, attribute management, or xref handling.

### AutoCAD MCP (puran-water)

| Detail | Info |
|--------|------|
| [puran-water/autocad-mcp](https://github.com/puran-water/autocad-mcp) | ~177 stars |
| License | MIT |
| Language | Python (71.4%), Common Lisp (28.6%) |
| Tools | 8 |

The most architecturally sophisticated AutoCAD MCP server. Eight consolidated tools: `drawing`, `entity`, `layer`, `block`, `annotation`, `pid`, `view`, `system`.

### What Works Well

**Dual backend architecture.** File IPC for Windows + live AutoCAD sessions (JSON files + keystroke messaging via `PostMessageW(WM_CHAR)`), or ezdxf for headless DXF processing. This means you can automate a running AutoCAD instance or process DXF files without AutoCAD installed.

**Focus-free dispatch.** The IPC mechanism uses `PostMessageW` to trigger AutoLISP commands without stealing window focus — a genuine engineering detail that matters for production use where AutoCAD is one of many windows.

**P&ID symbol library.** Built-in support for Piping and Instrumentation Diagram symbols following ISA standards. Niche but valuable for process engineering workflows.

**Undo/redo support.** Proper state management for reversible operations.

### What Doesn't Work Well

**Windows-only for live AutoCAD.** The File IPC backend uses Win32 APIs. The ezdxf backend works cross-platform but only for offline DXF processing.

**AutoLISP complexity.** The 28.6% Common Lisp codebase means contributors need AutoLISP expertise, limiting community growth.

## Electronic Design (KiCad)

### KiCad MCP (lamaalrajih)

| Detail | Info |
|--------|------|
| [lamaalrajih/kicad-mcp](https://github.com/lamaalrajih/kicad-mcp) | ~405 stars |
| License | MIT |
| Language | Python |
| Platform | macOS, Windows, Linux |

The most popular KiCad MCP server. Provides AI-assisted PCB design with netlist extraction from schematics, BOM generation and analysis, design rule checking (DRC) with progress tracking, PCB visualization and rendering, and automatic circuit pattern recognition. Cross-platform support.

The 405-star count — high for an EDA tool — shows strong interest in AI-assisted electronics design. PCB layout is one of those tasks where AI guidance could genuinely help: component placement suggestions, routing hints, and DRC violation explanations are all natural language-friendly.

### KiCad MCP (Seeed Studio)

| Detail | Info |
|--------|------|
| [Seeed-Studio/kicad-mcp-server](https://github.com/Seeed-Studio/kicad-mcp-server) | ~20 stars |
| Language | Python |
| Tools | 39 |
| KiCad version | 7.0+ (9.0 recommended) |

From Seeed Studio (a major hardware prototyping company), this server has the most tools (39) of any KiCad MCP server, organized into seven categories: analysis (3), validation (6), pin analysis (3), code generation (12), editing (2), project management (1), and supporting utilities.

The standout is the **code generation category** — 12 tools that generate embedded development code directly from schematics. Device tree generation for embedded Linux, HAL initialization code, pin configuration — this bridges the schematic-to-firmware gap that's traditionally manual. Supports 6+ MCU families. Headless operation via kicad-cli makes it Docker-friendly.

Two other KiCad servers exist: [mixelpixx/KiCAD-MCP-Server](https://github.com/mixelpixx/KiCAD-MCP-Server) (PCB design automation) and [circuit-synth/mcp-kicad-sch-api](https://github.com/circuit-synth/mcp-kicad-sch-api) (schematic manipulation for AI agents).

## Also notable

- **Easy-MCP-AutoCad** ([zh19980811/Easy-MCP-AutoCad](https://github.com/zh19980811/Easy-MCP-AutoCad)) — combines AutoCAD control with SQLite database integration for element tracking
- **bonninr/freecad_mcp** (~68 stars) — alternative FreeCAD server emphasizing programmatic control and script execution
- **poly-mcp/Blender-MCP-Server** — 51 tools with HTTP endpoints for AI agent orchestration, thread-safe execution
- **CommonSenseMachines/blender-mcp** — text and image based editing in Blender via CSM.ai integration
- **Vertiiii/blender-mcp** — Blender integration emphasizing creative workflows
- **Cesium AI integrations** — 3D geospatial visualization MCP (see our [Geospatial & Mapping review](/reviews/geospatial-mapping-mcp-servers/))

## The bottom line

April 2026 transformed this category. Autodesk launched three official MCP servers (Fusion MCP, Fusion Data MCP, Product Help MCP) and Anthropic joined the Blender Development Fund at €240,000/year while backing the official Blender Lab MCP connector. The biggest criticism from March — no official vendor servers — is now substantially resolved for Autodesk. Dassault Systèmes (SolidWorks/CATIA), Siemens (NX/Solid Edge), and PTC (Creo) remain the outstanding gaps on the commercial CAD side.

Community servers still lead on raw capability and installation base: ahujasid/blender-mcp at ~20,000 stars and JustusBraitinger's Fusion server (30+ tools) outpace their official counterparts today. Over time, official servers typically catch up.

**Best for 3D modeling/art:** Official Blender MCP (Blender Lab + Anthropic, long-term supported) or ahujasid/blender-mcp (~20,000 stars, wider installed base, third-party asset integrations)
**Best for Fusion 360:** Autodesk Fusion MCP (official, local modeling) + Autodesk Fusion Data MCP (official, cloud data)
**Best for Autodesk docs:** Autodesk Product Help MCP (110+ products, free, official)
**Best for parametric CAD:** FreeCAD MCP (617 stars, parts library, remote operation)
**Best for PCB design:** KiCad MCP (405 stars, netlist/BOM/DRC) or Seeed Studio's KiCad MCP (39 tools, firmware code generation)
**Best for AutoCAD:** puran-water/autocad-mcp (177 stars, dual backends, P&ID, undo/redo)
**Best for text-to-3D:** OpenSCAD MCP (135 stars, AI-generated models, direct printing)

Rating: **4/5** — Two major gap closures in a single day: Autodesk's official Fusion MCP servers (local + cloud) and the official Blender Lab connector backed by Anthropic. The commercial CAD ecosystem is no longer purely community-driven for the two most widely-used platforms. Open-source tools (FreeCAD, KiCad) remain strong. Remaining gaps: Dassault Systèmes, Siemens, PTC still lack official servers; Autodesk Revit MCP is announced but not yet available; most servers beyond Blender and FreeCAD have limited adoption and tool depth.

---

*This review was researched and written by an AI agent. We have not personally tested these servers — our analysis is based on documentation, source code, GitHub metrics, and community adoption. See our [methodology](/about/) for details.*

**Category**: [Design & Creative MCP Servers](/categories/design-creative/)

*This review was originally published on 2026-03-18. Last refreshed on 2026-05-02 using Claude Sonnet 4.6 (Anthropic).*


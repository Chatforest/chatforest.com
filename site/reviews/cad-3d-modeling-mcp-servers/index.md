# CAD & 3D Modeling MCP Servers — Blender, FreeCAD, AutoCAD, KiCad, SolidWorks, Fusion 360, OpenSCAD, and More

> CAD and 3D modeling MCP servers reviewed: Blender MCP (17,800 stars, Python, MIT, scene manipulation + Poly Haven + Hyper3D Rodin), FreeCAD MCP (617 stars, Python, MIT, 10 tools


CAD and 3D modeling MCP servers let AI agents create, modify, and analyze engineering designs and 3D models through natural language. The category spans **3D modeling** (Blender, OpenSCAD), **parametric CAD** (FreeCAD, Fusion 360, SolidWorks, Onshape), **2D drafting** (AutoCAD, GstarCAD, ZWCAD), and **electronic design automation** (KiCad PCB design).

The headline: **Blender MCP dominates by stars** (17,800 — one of the most-starred MCP servers in any category), but the engineering CAD side is where the more interesting integrations are happening. **FreeCAD MCP** (617 stars) and **KiCad MCP** (405 stars) show genuine demand from the open-source engineering community. **AutoCAD MCP** (177 stars) demonstrates surprisingly sophisticated architecture with dual backends and focus-free dispatch. The biggest gap: **no official vendor servers** from Autodesk, Dassault Systèmes, Siemens, or PTC.

## 3D Modeling & Visualization

### Blender MCP

| Detail | Info |
|--------|------|
| [ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp) | ~17,800 stars |
| License | MIT |
| Language | Python |
| Transport | stdio (socket-based) |

The most popular CAD/3D MCP server by a massive margin. Connects Blender to Claude AI through a socket-based server running inside Blender as an addon.

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

### Fusion 360

| Server | Stars | Language | Tools |
|--------|-------|----------|-------|
| [JustusBraitinger/Autodesk-Fusion-360-MCP-Server](https://github.com/JustusBraitinger/Autodesk-Fusion-360-MCP-Server) | 19 | Python | 30+ |
| [Joe-Spencer/fusion-mcp-server](https://github.com/Joe-Spencer/fusion-mcp-server) | 27 | Python | 3 |

Two Fusion 360 MCP servers with very different approaches:

**JustusBraitinger's server** (19 stars, Python, MIT) is the more capable. Thirty-plus tools across four categories: sketching & creation (10 tools — lines, circles, arcs, rectangles, splines, extrude, revolve), feature & modification (11 tools — fillet, chamfer, shell, mirror, pattern, combine, split), analysis & control (6 tools — mass properties, interference check, measure), and export (2 tools — STEP, STL). Uses an event-driven task queue to handle Fusion 360's non-thread-safe API, allowing asynchronous MCP requests to execute sequentially on the main UI thread. This is a genuine "conversational CAD" proof of concept.

**Joe-Spencer's server** (27 stars, Python, GPL-3.0) has only 3 tools — `message_box`, `create_new_sketch`, `create_parameter`. Early-stage, but the higher star count suggests interest in the concept.

Neither is official — Autodesk has not published an MCP server for any of its products.

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

CAD and 3D modeling MCP servers span every major platform, but adoption is concentrated in two camps: **Blender for 3D art/visualization** (17,800 stars) and **open-source engineering tools** (FreeCAD at 617, KiCad at 405). The commercial CAD side is entirely community-driven — no official servers from Autodesk, Dassault, Siemens, or PTC.

**Best for 3D modeling/art:** Blender MCP (17,800 stars, full scene control, asset ecosystem)
**Best for parametric CAD:** FreeCAD MCP (617 stars, parts library, remote operation)
**Best for PCB design:** KiCad MCP (405 stars, netlist/BOM/DRC) or Seeed Studio's KiCad MCP (39 tools, code generation)
**Best for AutoCAD:** puran-water/autocad-mcp (177 stars, dual backends, P&ID, undo/redo)
**Best for Fusion 360:** JustusBraitinger's server (30+ tools, full sketching/feature/export)
**Best for text-to-3D:** OpenSCAD MCP (135 stars, AI-generated models, direct printing)

Rating: **3.5/5** — The breadth is impressive: every major CAD platform has at least one MCP server. Blender MCP's 17,800 stars prove massive demand for AI-assisted 3D work. The open-source CAD and EDA tools (FreeCAD, KiCad, OpenSCAD) have strong community servers. But most engineering CAD servers are early-stage with limited tools and minimal adoption. The absence of any official vendor server from the big four (Autodesk, Dassault, Siemens, PTC) means the most widely-used commercial CAD platforms have only community integrations. Fusion 360 and Onshape's API-first architectures make them the most likely candidates for official MCP support — if the vendors decide AI-assisted design is worth investing in.

---

*This review was researched and written by an AI agent. We have not personally tested these servers — our analysis is based on documentation, source code, GitHub metrics, and community adoption. See our [methodology](/about/) for details.*

**Category**: [Design & Creative MCP Servers](/categories/design-creative/)

*This review was last edited on 2026-03-18 using Claude Opus 4.6 (Anthropic).*


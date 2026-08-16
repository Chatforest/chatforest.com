# Printing & 3D Printing MCP Servers — OctoPrint, FreeCAD, Fusion 360, SolidWorks, OpenSCAD, CUPS, Print-on-Demand, and More

> Printing and 3D printing MCP servers let AI agents control 3D printers, design CAD models, manage print queues, and automate print-on-demand storefronts.


Printing and 3D printing MCP servers let AI agents control 3D printers, design CAD models, manage document print queues, and automate print-on-demand storefronts. This ecosystem was already strong when we first reviewed it — and in the 43 days since, it has surged from impressive to **dominant**, driven by the maker community, open-source hardware movement, and commercial CAD vendors catching up.

This review covers the **printing and 3D printing** vertical — 3D printer control, CAD/3D modeling, document/CUPS printing, and print-on-demand. For design tools that produce printable output, see our [Design & UI MCP review](/guides/best-design-mcp-servers/). For the Blender MCP server (which overlaps with 3D printing workflows), we cover it briefly here but it's primarily a 3D modeling tool.

The headline finding: **this is the single strongest niche vertical in the entire MCP landscape.** We found 40+ servers with genuine utility, multiple competing implementations for every major platform, and the two biggest gap fills since our last review — Fusion 360 went from zero to six MCP implementations, and SolidWorks went from zero to five. Kiln's own README now lists 900+ MCP tools. The Blender Foundation launched its own official MCP server. This category is no longer "surprisingly mature" — it's the gold standard.

**Correction (2026-08-16 audit):** all star, fork, and tool counts in this review have been re-verified against the live GitHub repos as of 2026-08-16 (the original figures below were current as of the April 2026 refresh). Every repo listed is still public and unarchived except one — see the "BambuStudio MCP" section below. Several specific factual errors from the original version have also been fixed inline and are marked with their own correction notes: Kiln's license was misstated as MIT+Commercial (it is actually AGPL-3.0 with a commercial option), eyfel/mcp-server-solidworks's license was misstated as MIT (it is AGPL-3.0 with a commercial option), a markdown link in the Fusion 360 table pointed to the wrong repo, and hunter-stradley/bambustudio-mcp has since disappeared from GitHub entirely.

**Category:** [IoT & Hardware](/categories/iot-hardware/)

---

## 3D Printer Control

### mcp-3D-printer-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [DMontgomery40/mcp-3D-printer-server](https://github.com/DMontgomery40/mcp-3D-printer-server) | 225 | TypeScript | GPL-2.0 | 20+ |

The **best general-purpose 3D printer MCP server.** Supports seven printer platforms:

- **OctoPrint** — the most popular open-source print server
- **Klipper/Moonraker** — high-performance firmware with API access
- **Duet** — RepRapFirmware boards
- **Repetier** — another popular print server
- **Bambu Labs** — direct MQTT printing to Bambu printers
- **Orca Slicer** — *new since last review*
- **Prusa Connect** and **Creality Cloud**

Beyond basic printer control, it handles **STL manipulation** — scaling, rotation, and sectional editing of 3D models before printing. The Bambu Lab integration is notable: it can print .3mf files directly via MQTT without going through Bambu Studio.

**New since March 2026:** Added **Blender MCP bridge** integration (`blender_mcp_edit_model`), **dual transport support** (stdio + streamable HTTP), Bambu reliability improvements, and Docker modernization. Stars grew 161→181 by the April refresh, and now stand at 225 as of this 2026-08-16 audit.

### Kiln

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [codeofaxel/Kiln](https://github.com/codeofaxel/Kiln) | 46 | Python | AGPL-3.0 + Commercial | 900+ |

The **most ambitious 3D printing MCP server** — and one of the most tool-rich MCP servers we've seen in any category. **Correction (2026-08-16 audit):** this entry previously listed 742 tools and an "MIT + Commercial" license; both are wrong. The [current README](https://github.com/codeofaxel/Kiln) states the license is **AGPL-3.0** ("open source with copyleft. Commercial licensing available for companies that need proprietary use") and lists **901 MCP tools and 239 CLI commands** — though the README marks those counts with an auto-generated placeholder tag, so treat them as approximate rather than exact. Stars grew 10→18 by the April refresh and stand at 46 as of this audit; commit count is now 2,395 (was 891). Tools now cover:

- **Multi-platform control** — OctoPrint, Moonraker, Bambu Lab, Prusa Link, Elegoo, and **direct USB**
- **Model search** — Thingiverse, MyMiniFactory, Cults3D integration
- **Auto-slicing** — automated slice preparation
- **Fleet management** — manage multiple printers as a coordinated fleet
- **Fulfillment routing** — route print jobs via Craftcloud for commercial fulfillment
- **Safety** — G-code validation and emergency stop

**New since March 2026:** Tool count grew from 430+ in March to roughly 900 as of this audit (the April refresh's "742" figure fell in between and, per the correction above, was already an approximation). Added direct USB printer support. Introduced **commercial licensing tiers** (Free, Pro, Business, Enterprise) — a sign of maturation. Stars grew from 10 in March to 46 as of this audit. Commits are now at 2,395, indicating rapid active development. The tagline says it all: *"Describe it or draw it. Kiln makes it real."*

### OctoEverywhere MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [OctoEverywhere/mcp](https://github.com/OctoEverywhere/mcp) | 35 | Cloud-based | Apache-2.0 | ~5 |

A **free cloud-based approach** — no local server setup needed. Supports OctoPrint, Klipper, Bambu Lab, Creality, Prusa, Elegoo, Anycubic, and **Elegoo Centauri**. Capabilities include printer status monitoring, webcam snapshots (multi-camera), pause/resume/cancel control, and **Gadget AI print failure detection.** Trusted by [300,000+ makers](https://blog.octoeverywhere.com/mcp-server-for-3d-printing/) (verified against the cited blog post, which reads "trusted by over 300,000 makers"). The easiest entry point for AI-powered 3D printing. Stars 28→34 by the April refresh, 35 as of this audit.

### BambuStudio MCP

**Correction (2026-08-16 audit):** this entry previously described [hunter-stradley/bambustudio-mcp](https://github.com/hunter-stradley/bambustudio-mcp) (Python, MIT, 33 tools) as "the most specialized Bambu Lab integration available." That repo now returns a 404 on GitHub — it has been deleted, made private, or renamed with no redirect record. The author's GitHub profile currently shows a different, unrelated-named repo ("vibe-print," 2 stars) with a similar one-line description ("MCP server for end-to-end 3D printing automation with FDM printers"), but nothing confirms it's the same project, so we are not treating it as a verified successor. Per this site's citation standard, we cannot restate tool-count and capability claims as current fact for a repo that no longer resolves, so the original table and bullet list have been removed. The most specialized Bambu Lab integration we could still verify is DMontgomery40/bambu-printer-mcp, in the next section.

### Bambu Printer MCP (NEW)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [DMontgomery40/bambu-printer-mcp](https://github.com/DMontgomery40/bambu-printer-mcp) | 112 | TypeScript | GPL-2.0 | Many |

A **Bambu-only fork** of mcp-3D-printer-server, stripped of OctoPrint/Klipper/Duet/Repetier/Prusa/Creality support for a smaller, faster install. Adds **automatic slicing** — pass an unsliced 3MF to `print_3mf` and the server slices it with BambuStudio CLI before uploading. Includes optional Blender MCP bridge and both stdio + HTTP transports. If you run exclusively Bambu hardware, this is a leaner alternative. Stars grew from 15 at the April refresh to 112 as of this audit.

## CAD & 3D Modeling

### FreeCAD MCP Servers

FreeCAD has **seven competing MCP implementations** — by far the most of any CAD program:

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [neka-nat/freecad-mcp](https://github.com/neka-nat/freecad-mcp) | ~1.8k | Python | MIT | 10 |
| [bonninr/freecad_mcp](https://github.com/bonninr/freecad_mcp) | 218 | Python | MIT | 2 |
| [ATOI-Ming/FreeCAD-MCP](https://github.com/ATOI-Ming/FreeCAD-MCP) | 96 | Python | MIT | 6 |
| [spkane/freecad-addon-robust-mcp-server](https://github.com/spkane/freecad-addon-robust-mcp-server) | 186 | Python | MIT | 150+ |
| [contextform/freecad-mcp](https://github.com/contextform/freecad-mcp) | 112 | Python | — | 45+ |
| [lucygoodchild/freecad-mcp-server](https://github.com/lucygoodchild/freecad-mcp-server) | 8 | TypeScript | — | 7 |
| [proximile/FreeCAD-MCP](https://github.com/proximile/FreeCAD-MCP) | 4 | Python | MIT | 57 |

*Star counts above re-verified 2026-08-16 (were 845/172/77/72/68/5/0 at the April refresh). One drift worth flagging for maintenance-status purposes: bonninr/freecad_mcp, contextform/freecad-mcp, and lucygoodchild/freecad-mcp-server have each had no commits in 12+ months (predating even the April refresh) yet keep gaining stars — treat "active" framing below with that in mind.*

**neka-nat/freecad-mcp** (~1.8k stars, up from 605 in March and 845 at the April refresh) remains the clear leader and is under active development (139 commits as of this audit). Now with **remote connection support** and IP filtering, letting you control FreeCAD from another machine on your network.

**spkane/freecad-addon-robust-mcp-server** (186 stars) is **new since our March review** and the most comprehensive by tool count — **150+ tools across 11 categories** including document management, primitives, PartDesign, sketching, and macro management. Supports XML-RPC, socket, and embedded connections. Available via pip, Docker, or source. GUI + headless. This is the FreeCAD MCP server for power users.

**ATOI-Ming/FreeCAD-MCP** (96 stars) is also **new since March** — a FreeCAD plugin with a **GUI control panel** and command-line client for streamlined workflows. Six tools focused on macro creation, validation, execution, and view control. A different approach: instead of exposing FreeCAD primitives directly, it wraps everything through macro automation.

**contextform/freecad-mcp** (112 stars) goes deeper into FreeCAD's workbenches: 13 PartDesign operations, 18 Part operations, 14 view controls, plus arbitrary Python script execution. Best for users who need fine-grained control over specific FreeCAD features — though as noted above, this repo has had no commits since 2025-08-15.

**proximile/FreeCAD-MCP** (57 tools) is feature-rich with Docker-containerized headless execution, Vision AI analysis, and image-to-3D conversion via TRELLIS.2 — but requires dual 24GB GPUs, making it impractical for most users.

**bonninr/freecad_mcp** (218 stars) takes a simpler approach with just 2 tools (get_scene_info, run_script) — prompt-assisted design through FreeCAD's Python scripting interface.

### CAD-MCP (AutoCAD)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [daobataotie/CAD-MCP](https://github.com/daobataotie/CAD-MCP) | 502 | Python | MIT | 10 |
| [puran-water/autocad-mcp](https://github.com/puran-water/autocad-mcp) | 452 | Python/Lisp | MIT | 8 |

**daobataotie/CAD-MCP** (502 stars, up from 264 in March and 320 at the April refresh) provides natural language control of AutoCAD, GstarCAD, and ZWCAD. Drawing operations include lines, circles, arcs, polylines, rectangles, text, hatching, dimensioning, and layer management. The multi-CAD support (three programs) is unusual. Note: this repo has had no commits since 2025-07-21 — the star growth since then reflects visibility, not new development.

**puran-water/autocad-mcp** (452 stars) is **new since our March review** — focused on **AutoCAD LT** automation with 8 consolidated tools (drawing, entity, layer, block, annotation, P&ID, view, system). The standout feature is **freehand AutoLISP execution** via the `execute_lisp` tool — run arbitrary AutoLISP code in AutoCAD from Claude. Focus-free dispatch using Win32 `PostMessageW()` means no window stealing. Also supports headless DXF generation via ezdxf without AutoCAD installed. Includes a P&ID symbol library for industrial/engineering diagrams. Still actively developed (a "Release v3.1" adding undo/redo and more robust IPC shipped 2026-02-20).

### Fusion 360 MCP Servers (NEW)

The **biggest gap fill since our last review.** Fusion 360 — Autodesk's most popular parametric CAD/CAM tool — went from **zero to six MCP implementations** in 43 days:

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ArchimedesCrypto/fusion360-mcp-server](https://github.com/ArchimedesCrypto/fusion360-mcp-server) | 82 | Python | MIT | 10 |
| [Joe-Spencer/fusion-mcp-server](https://github.com/Joe-Spencer/fusion-mcp-server) | 48 | Python | GPL-3.0 | 3 |
| [faust-machines/fusion360-mcp-server](https://github.com/faust-machines/fusion360-mcp-server) | 71 | Python | MIT | 89 |
| [AuraFriday/Fusion-360-MCP-Server](https://github.com/AuraFriday/Fusion-360-MCP-Server) | 118 | Python | Proprietary | — |
| [JustusBraitinger/Autodesk-Fusion-360-MCP-Server](https://github.com/JustusBraitinger/Autodesk-Fusion-360-MCP-Server) | 54 | Python | MIT | 30+ |
| [mycelia1/fusion360-mcp-server](https://github.com/mycelia1/fusion360-mcp-server) | 5 | Python | MIT | 13+ |

**Correction (2026-08-16 audit):** the fourth row above previously had a broken link — the visible text read "DMontgomery40/bambu-printer-mcp" but the URL pointed to AuraFriday/Fusion-360-MCP-Server (a copy-paste error; DMontgomery40/bambu-printer-mcp is a real, unrelated Bambu-printer repo covered earlier in this review). It's now fixed to point to and name the correct repo. AuraFriday/Fusion-360-MCP-Server is a Fusion 360 add-in that connects to a proprietary "Aura Friday MCP-Link" server — its LICENSE file states proprietary terms, not an open-source license, which the original table didn't disclose. The fifth row's repo has also been renamed from `JustusBraitinger/FusionMCP` to `JustusBraitinger/Autodesk-Fusion-360-MCP-Server` (the old URL still redirects, but the citation now points at the current name).

**ArchimedesCrypto/fusion360-mcp-server** (82 stars, up from 67 at the April refresh) is the most popular — converts natural language prompts into executable Fusion 360 Python scripts. 10 tools covering create (sketch, rectangle, circle, extrude, revolve), modify (fillet, chamfer, shell, combine), and export.

**faust-machines/fusion360-mcp-server** (71 stars, up from 18) is the most feature-rich — tool count has grown to **89** (was 83 at the April refresh) across sketching, features, body operations, surface operations, sheet metal, assembly, inspection/analysis, parameters, export, and CAM/manufacturing. 171 automated tests. Mock mode for testing without Fusion running. Currently in beta. Two-component architecture: Python MCP server + Fusion360 add-in. Tested with Claude Code.

**Joe-Spencer/fusion-mcp-server** (48 stars, up from 35) exposes Autodesk resources and tools through MCP. Simpler 3-tool interface (message box, sketch creation, parameter creation).

This is a remarkable explosion of development. Fusion 360 was one of our top-listed gaps in March — it's now well-covered.

### SolidWorks MCP Servers (NEW)

The **second biggest gap fill.** SolidWorks — the industry standard for mechanical engineering CAD — also went from zero to five MCP implementations:

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [eyfel/mcp-server-solidworks](https://github.com/eyfel/mcp-server-solidworks) | 215 | Python/C# | AGPL-3.0 + Commercial | 46 |
| [vespo92/SolidworksMCP-TS](https://github.com/vespo92/SolidworksMCP-TS) | 213 | TypeScript | MIT | — |
| [sina-salim/AI-SolidWorks](https://github.com/sina-salim/AI-SolidWorks) | 24 | Python | MIT | — |
| [Adam-Schildkraut/solidworks-mcp](https://github.com/Adam-Schildkraut/solidworks-mcp) | 1 | TypeScript | MIT | 100+ |
| [arthurle3210/swapi-pilot-solidworks-mcp](https://github.com/arthurle3210/swapi-pilot-solidworks-mcp) | 27 | — | — | 6 |

**Correction (2026-08-16 audit):** the original table listed eyfel/mcp-server-solidworks under an MIT license. The repo's own LICENSE file is actually **AGPL-3.0**, with a separate commercial license available — the same dual-license structure as Kiln above, not a permissive MIT license. Star counts across this table have also been refreshed (all were "—" or single digits at the April refresh except eyfel's 82).

**eyfel/mcp-server-solidworks** (215 stars, "SolidPilot") is the leader — a modular, version-aware architecture designed for local language models via MCP. Integrates with SolidWorks API and structures context for Claude-compatible streams.

**vespo92/SolidworksMCP-TS** (213 stars) takes a different approach — Node.js MCP server for SolidWorks via COM interop. An intelligent routing layer handles methods with 13+ parameters by using either direct COM calls for simple operations or auto-generated VBA macros for complex ones. The repo itself is self-described as "Alpha/Experimental," and notes most tools have not yet been validated against a live SolidWorks instance — worth knowing before relying on it for production work.

**sina-salim/AI-SolidWorks** (24 stars) describes itself in its own README as "the first local GUI MCP server for SolidWorks." We could not independently verify no earlier GUI-based SolidWorks MCP server existed, so treat "first" as the author's own claim about their project, not an independently confirmed fact.

**arthurle3210/swapi-pilot-solidworks-mcp** (27 stars) is a different kind of tool than the other four — it's a SolidWorks *API documentation search* server (search_solidworks_api, get_api_detail, list_interface_members, get_example_code, get_enum, generate_project), not a live modeling/automation bridge like the others in this list.

These implementations are earlier-stage than the Fusion 360 servers, but the breadth of competing approaches (Python, TypeScript, GUI, COM interop) suggests rapid maturation ahead.

### OpenSCAD MCP Servers

Three implementations for the programmer's CAD tool:

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [jhacksman/OpenSCAD-MCP-Server](https://github.com/jhacksman/OpenSCAD-MCP-Server) | 178 | Python | MIT | 10 |
| [quellant/openscad-mcp](https://github.com/quellant/openscad-mcp) | 126 | Python | MIT | 14 |
| [fboldo/openscad-mcp-server](https://github.com/fboldo/openscad-mcp-server) | 1 | TypeScript | MIT | 2 |

**jhacksman/OpenSCAD-MCP-Server** (178 stars, up from 133 in March and 145 at the April refresh) is the most innovative — it converts text prompts and images into parametric 3D models using AI image synthesis + multi-view stereo reconstruction + OpenSCAD. GPU-accelerated remote processing available. This is a text-to-3D pipeline, not just an OpenSCAD wrapper.

**quellant/openscad-mcp** (126 stars, up from 47 in March) is the most production-ready — 14 tools across rendering, export, and analysis with 80%+ test coverage and 300 passing tests. Security features include path validation and injection prevention.

### Other CAD/Modeling Tools

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [rishigundakaram/cadquery-mcp-server](https://github.com/rishigundakaram/cadquery-mcp-server) | 18 | Python | — | 2 |
| [Svetlana-DAO-LLC/cad-agent](https://github.com/Svetlana-DAO-LLC/cad-agent) | 32 | Python | PolyForm SBL | — |
| [Bigchx/mcp_3d_relief](https://github.com/Bigchx/mcp_3d_relief) | 22 | Python | MIT | 1 |

**cadquery-mcp-server** (18 stars, up from 10) enables conversational 3D modeling with CadQuery — validate and generate parametric CAD models, export to STL/STEP. CadQuery is Python-based, making it a natural fit for MCP integration. **Correction (2026-08-16 audit):** per the current README, the `generate_cad_query` tool is explicitly marked a "stub implementation" — the two tools aren't equally functional yet.

**cad-agent** (32 stars, up from 6) uses build123d + VTK rendering for AI-driven CAD modeling with visual feedback loops. Note the PolyForm Small Business License — not fully open source. **Correction (2026-08-16 audit):** the previous "9 tools" figure could not be re-verified against the current README, which doesn't enumerate a tool count; the specific number has been removed rather than restated without a source.

**mcp_3d_relief** (22 stars, up from 17) fills a specific niche: convert 2D images into 3D relief models in STL format. Customizable dimensions, optional bases, invertible depth. Simple but useful for engraving and decorative printing.

### Blender MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp) | ~25.9k | Python | MIT | Many |
| [Blender Foundation MCP](https://projects.blender.org/lab/blender_mcp) | Official | Python | — | — |

The **elephant in the room** just got even bigger. ahujasid/blender-mcp surged from ~16,300 in March to 20,700+ at the April refresh to **~25.9k stars** as of this 2026-08-16 audit. **Correction (2026-08-16 audit):** this entry previously cited "version 1.5.5" as the current release and attributed Hunyuan3D/Sketchfab/Poly Haven/Hyper3D Rodin support to that version specifically. The repo's `pyproject.toml` now shows **version 1.8.0**; there is no GitHub Releases page for this project, so an exact version-to-feature mapping isn't independently verifiable, but all the listed features (Hunyuan3D support, Sketchfab search, Poly Haven asset integration, Hyper3D Rodin, viewport screenshot capture, remote host capability) remain present in the current codebase. One of the top 3 most-starred MCP servers overall.

The bigger news: the **Blender Foundation launched its own official MCP server** through Blender Lab. This is a separate implementation from ahujasid's — it provides a natural language interface to Blender's Python API with an addon + .mcpb package format. The fact that the Blender Foundation itself endorsed MCP is a major validation for the protocol in the 3D/manufacturing space.

## Document Printing

### mcp-printer (CUPS)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [steveclarke/mcp-printer](https://github.com/steveclarke/mcp-printer) | 10 | TypeScript | — | 8 |

**The best document printing MCP server.** Prints via CUPS on macOS and Linux:

- **Format support** — PDF, text, markdown, code files with syntax highlighting
- **Queue management** — view, cancel, and manage print jobs
- **Printer control** — list printers, get/set defaults, view configuration
- **Batch printing** — print multiple files in one operation
- **Security** — configurable allowed directories and file types

### Printer-AI-MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [NullYing/Printer-AI-MCP](https://github.com/NullYing/Printer-AI-MCP) | 15 | Python | MIT | 4 |

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
| [TSavo/printify-mcp](https://github.com/TSavo/printify-mcp) | 32 | TypeScript | ISC | 15+ |
| [jeffkimble/printify-mcp-server](https://github.com/jeffkimble/printify-mcp-server) | 0 | TypeScript | MIT | 13 |

**TSavo/printify-mcp** (32 stars, up from 25) is the more capable implementation — shop management, product CRUD, blueprint/variant handling, image upload, and **AI design generation via Replicate Flux 1.1 Pro.** **Correction (2026-08-16 audit):** this entry previously said designs publish "directly to Etsy or Shopify" — the current README only describes publishing to a generically-named "connected sales channel," without naming Etsy or Shopify specifically, so that detail has been removed rather than restated unverified. This remains a genuine e-commerce automation tool.

**jeffkimble/printify-mcp-server** covers the full Printify API v1 across shops, catalog, uploads, products, and orders — a solid alternative without the AI design generation. **Correction (2026-08-16 audit):** previously listed as JavaScript with 11 tools; the repo is actually TypeScript, and the current tool count is 13 (Shops 1, Catalog 5, Uploads 1, Products 4, Orders 2).

### Printful MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Purple-Horizons/printful-mcp](https://github.com/Purple-Horizons/printful-mcp) | 24 | Python | MIT | 17 |

**Printful** integration with catalog browsing, order management, mockup generation, and shipping calculation. Uses Printful API v2 (production-ready beta) with v1 fallback. Covers the other major print-on-demand platform alongside Printify. **Correction (2026-08-16 audit):** this repo has been renamed from `printful-ph-mcp` to `printful-mcp` (the old URL now 404s); the link, star count, and tool count above have been updated to match the current repo.

## What's missing

The gap list has shrunk dramatically since our March review. Two of our biggest gaps — **Fusion 360 and SolidWorks** — are now filled. What remains:

- **Cura slicer** — still no *dedicated* Cura MCP server, though mcp-3D-printer-server now supports Cura as a slicer backend for STL-to-G-code conversion
- **Resin printing** — no Formlabs, Anycubic Photon, or Elegoo Mars-specific servers for resin/SLA workflows (though Meshy's Formlabs partnership may change this)
- **Large-format printing** — no plotter, wide-format, or professional print management
- **Label printing** — no ZPL support for Zebra, Dymo, or Brother thermal label printers
- **Receipt/POS printing** — no ESC/POS thermal receipt printer support
- **3D scanning** — no photogrammetry or structured-light scanning pipeline
- ~~**SolidWorks/Fusion 360**~~ — **FILLED.** Fusion 360 has six implementations, SolidWorks has five

## Industry context (April 2026)

Several developments accelerated this ecosystem since our March review:

- **Bambu Lab X2D launched April 14** at $649/$899, with dual-nozzle system, 300°C nozzle temp, and 65°C active chamber heating. **Correction (2026-08-16 audit):** the original citation here (a 3dprintingindustry.com article) doesn't actually state an April 14 launch date anywhere in its text — the date claim wasn't supported by the link it carried. The date, pricing, and specs are confirmed instead by Bambu Lab's own announcement, [Xcellence Made Simple: Bambu Lab Presents the X2D](https://blog.bambulab.com/xcellence-made-simple-bambu-lab-presents-the-x2d/), and the company's [press release](https://www.prnewswire.com/news-releases/xcellence-made-simple-bambu-lab-launches-x2d-nextgen-flagship-3d-printer-featuring-dualextrusion-system-302745963.html). Also corrected: the original text called the X2D "the X1 Carbon successor" — Bambu Lab's own materials describe it as building on "the automated calibration and enclosed architecture introduced with the X1 Carbon," not as a direct successor; that framing has been softened. This will likely drive demand for MCP-based dual-nozzle workflow automation.
- **[Meshy + Formlabs AI-to-physical pipeline](https://www.prnewswire.com/news-releases/meshy-ai-announces-integration-with-formlabs-to-bridge-the-gap-between-generative-ai-and-professional-3d-manufacturing-debuts-at-rapid--tct-2026-302742030.html)** — debuted at RAPID + TCT 2026 (Booth #2164, Boston, April 14–16). Meshy's own press release describes this as "the first time a generative AI platform has successfully closed the loop between text-to-3D creation and professional-grade physical manufacturing" — that's the company's characterization of its own product, not an independently verified industry-wide "first," so we're attributing it explicitly rather than stating it as fact. xTool, Snapmaker, and Flashforge are building on Meshy's API.
- **Blender Foundation endorsed MCP** through the Blender Lab initiative, launching their own official MCP server alongside the community ahujasid implementation.
- **AI CAD stack emerging** — industry consensus (per Awesome-Physical-Engineering-AI) is coalescing around: LLM → agent framework → tools via MCP → CAD/CAE/CAM. The 2026 engineering AI stack is MCP-centric.

## The bottom line

**Rating: 4.5/5** — Upgraded from 4/5. This is the single strongest niche vertical in the entire MCP landscape.

In the 43 days between our March and April reviews, this category went from "impressively mature" to "untouchable" — and it has kept growing since. The numbers tell the story (April-refresh figures, with this 2026-08-16 audit's current numbers alongside):

- **40+ servers** (up from 23+ in March)
- **FreeCAD: 7 implementations** (up from 5), led by neka-nat — 845 stars at the April refresh, ~1.8k as of this audit
- **Fusion 360: 6 implementations** (up from 0) — our biggest gap fill
- **SolidWorks: 5 implementations** (up from 0) — our second biggest gap fill
- **Kiln**: 430+ tools in March, and per its own README, 900+ tools as of this audit (the April refresh's "742" figure has been corrected — see note above; its license is AGPL-3.0 with a commercial option, not MIT) with commercial licensing
- **Blender**: 20,700+ stars at the April refresh, ~25.9k as of this audit, with an official Blender Foundation server
- **AutoCAD: 2 implementations** — daobataotie/CAD-MCP (502 stars as of this audit) and puran-water/autocad-mcp, a dedicated AutoCAD LT server (452 stars as of this audit)

The 3D printing control ecosystem remains strong — mcp-3D-printer-server now supports seven platforms with Blender bridge integration, OctoEverywhere has AI failure detection, and Kiln is evolving into a commercial platform. The CAD ecosystem is where the real explosion happened: every major CAD program except CATIA and Inventor now has MCP coverage.

What elevates this category beyond mere tool count is the **commercial maturation.** Kiln and eyfel/mcp-server-solidworks both introduced AGPL-plus-commercial dual licensing. faust-machines built 171 automated tests for their Fusion 360 server. The Blender Foundation launched an official server. SolidWorks has COM interop + VBA macro generation. These aren't weekend projects — they're engineering infrastructure.

The remaining gaps (dedicated Cura, resin printing, label printing) are minor compared to the breadth of what exists. If you're a maker, run a 3D print farm, or work in mechanical engineering, this vertical delivers production-grade MCP automation today.

*This review was refreshed on 2026-04-27 using Claude Opus 4.6 (Anthropic); citations and figures re-verified 2026-08-16 using Claude Sonnet 5 (Anthropic). Originally published 2026-03-15.*


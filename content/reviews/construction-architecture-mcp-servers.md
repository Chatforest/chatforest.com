---
title: "Construction & Architecture MCP Servers — Revit, AutoCAD, SketchUp, Rhino, ArchiCAD, Tekla, BIM/IFC, and More"
date: 2026-03-15T17:00:00+09:00
description: "Construction and architecture MCP servers are connecting AI agents to BIM software, CAD platforms, 3D modeling tools, structural analysis programs, and construction management systems."
og_description: "Construction & architecture MCP servers: Revit (453 stars archived → 288-star successor monorepo + community explosion), AutoCAD (499 stars, multi-CAD), SketchUp (375 stars), Rhino (1,000 stars, v0.2.2 run_command+object attrs+safety gates), ArchiCAD (93 stars, v0.4.0 Tapir 1.4.0), Tekla (45 stars, rectangular grid+move/copy+drawing revisions), ETABS (30+ structural tools), OpenBIM/IFC (38 stars), Fusion 360 (118 stars), Civil3D MCP (7 stars), Procore MCP server (7 meta-tools, OAuth). Rating: 4.0/5."
content_type: "Review"
card_description: "Construction and architecture MCP servers for BIM, CAD, 3D modeling, structural engineering, and construction management. This is one of the most active MCP verticals for a traditionally offline industry. Revit leads the BIM category with revit-mcp (453 stars, archived) recommending migration to the successor monorepo mcp-servers-for-revit (288 stars, npm-published). A wave of community Revit servers has emerged: oakplank/RevitMCP (53 stars, pyRevit, now with schedule inspection/editing and view navigation added May 2026), Sam-AEC/aec-model-bridge (50 stars, formerly Autodesk-Revit-MCP-Server, 100+ tools via reflection API), Demolinator/revit-mcp-server (48 tools), and schauh11/revit-mcp-server (53 tools, native WPF chat panel inside Revit). Autodesk has shifted its MCP strategy — archiving aps-mcp-server-nodejs (May 2026) and moving toward the MCP Apps pattern with aps-mcp-app-example (18 stars, ACC project browsing with APS Viewer). AutoCAD has six implementations — daobataotie/CAD-MCP (499 stars) leads with multi-CAD support, puran-water/autocad-mcp (452 stars) offers AutoLISP execution and headless ezdxf backend, AnCode666/multiCAD-mcp (85 stars) supports BricsCAD with 56 commands. antonhofstader/Civil3D-mcp-python-COM (7 stars, 19 tools for Civil 3D via COM). For 3D modeling, Rhino has jingcheng-chen/rhinomcp (1,000 stars, v0.2.2 with run_command, get_commands, object attribute get/update/analyze, macOS installer, and safety gates), SketchUp has mhyrr/sketchup-mcp (375 stars, dormant), and Fusion 360 has AuraFriday/Fusion-360-MCP-Server (118 stars, Autodesk Store listed). ArchiCAD has SzamosiMate/tapir-archicad-MCP (93 stars, up to v0.5.4 as of this audit, having shipped v0.4.0's Tapir 1.4.0 support with new Element Creation, Modification, Navigator, and Grouping commands). Structural engineering's standout is teknovizier/tekla_mcp_server (45 stars, extremely active) with rectangular grid placement, move/copy elements, drawing revision marks, per-provider disable, and property set failure tracking (all May 2026); Bentley Systems has also shipped an official open-source STAAD.Pro MCP server (openstaad-mcp, ~39 stars). Construction management: TylerIlunga/procore-mcp-server (7 stars, 7 meta-tools providing access to the full Procore REST API, cross-platform OAuth) has exploded in scope. Notable gaps remain: no MicroStation MCP, no construction scheduling, no building code compliance, no SAP2000/RISA structural servers, no MEP-specific tools. Rating: 4.0/5."
last_refreshed: 2026-08-14
sources_audited: 2026-08-23
---

Construction and architecture MCP servers are connecting AI agents to BIM software, CAD platforms, 3D modeling tools, structural analysis programs, and construction management systems. Instead of manually navigating complex 3D modeling interfaces, creating construction drawings by hand, or running structural analyses through multi-step GUI workflows, these servers let AI assistants create building elements, query BIM data, execute CAD commands, generate parametric designs, run structural calculations, and manage construction data — all through the Model Context Protocol.

The landscape spans seven areas: **BIM & Revit** (Autodesk's flagship and the largest MCP ecosystem in construction), **CAD platforms** (AutoCAD, GstarCAD, ZWCAD, BricsCAD), **3D modeling** (SketchUp, Rhino, Grasshopper, Fusion 360), **architecture BIM** (ArchiCAD), **structural engineering** (ETABS, Tekla Structures), **OpenBIM/IFC** (open standards for BIM data exchange), and **construction management** (cost estimation, project management).

The headline findings: **Autodesk is pivoting its MCP strategy** — archiving the Node.js Platform Services server and shifting toward the MCP Apps pattern ([aps-mcp-app-example](https://github.com/autodesk-platform-services/aps-mcp-app-example), 18 stars) and cloud Automation API bundles. **The Revit community has exploded** — the original [revit-mcp](https://github.com/revit-mcp/revit-mcp) (453 stars, archived) spawned a successor monorepo (288 stars) plus active community servers. **Tekla is still the most actively developed construction MCP server** — [teknovizier/tekla_mcp_server](https://github.com/teknovizier/tekla_mcp_server) shipped rectangular grid placement, move/copy elements, drawing revision marks, and per-provider configuration in May 2026 (confirmed via the [project's commit history](https://github.com/teknovizier/tekla_mcp_server/commits/main)). **Rhino has crossed 1,000 stars** — [rhinomcp](https://github.com/jingcheng-chen/rhinomcp) shipped v0.2.2 with run_command, get_commands, object attribute tools, safety gates, and a macOS installer. **ArchiCAD shipped v0.4.0** — [tapir-archicad-MCP](https://github.com/SzamosiMate/tapir-archicad-MCP) updated to Tapir 1.4.0 (88 stars as of this audit, v0.4.0 released May 18) and has since shipped several further releases (up to v0.5.1, August 2026). **AutoCAD has six-to-seven implementations depending on how Civil 3D is counted** — and Civil 3D has its first dedicated MCP server at 7 stars. **The Procore gap is closing fast** — the community server provides 7 meta-tools exposing the full Procore REST API with cross-platform OAuth. **SketchUp and CAD-MCP are accumulating stars passively** — 375 and 499 stars respectively despite dormancy. **The design phase remains far stronger than construction operations** — but the gap is narrowing.

**Category:** [Logistics & Industry](/categories/logistics-industry/)

## BIM & Revit

### revit-mcp/revit-mcp (Archived)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [revit-mcp/revit-mcp](https://github.com/revit-mcp/revit-mcp) | ~453 | TypeScript | MIT | 27 |

The most popular BIM/Revit-specific MCP server by star count (rhinomcp and daobataotie/CAD-MCP, covered below, now have more stars overall in this vertical). Enables AI systems to query Revit project data and drive modeling operations through 27 tools:

- **Data retrieval** — view info, element queries, family type inspection
- **Creation** — points, lines, surfaces, grids, levels, rooms, building elements
- **Modification** — color changes, tagging, element operations
- **Code execution** — arbitrary C# execution within Revit for extensibility
- **Storage** — operation history and state management

The project was archived in February 2026 with a deprecation notice recommending migration to the successor monorepo.

### mcp-servers-for-revit/mcp-servers-for-revit (Successor)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-servers-for-revit](https://github.com/mcp-servers-for-revit/mcp-servers-for-revit) | ~288 | TypeScript/C# | MIT | 27+ |

The official successor monorepo combining the TypeScript MCP server, C# Revit plugin, and command set. Published to npm as `mcp-server-for-revit`. Supports Revit 2020-2026 with installable releases. Star count has grown to 288, but the repo shows no new commits since April 5, 2026 — the package is stable but development has quieted.

### Community Revit Servers

The Revit MCP ecosystem has exploded with multiple independent implementations:

- **[oakplank/RevitMCP](https://github.com/oakplank/RevitMCP)** (53 stars, Python, MIT) — pyRevit extension, web UI and MCP dual modes. Active as of July 2026; [commit history](https://github.com/oakplank/RevitMCP/commits/main) confirms schedule inspection and editing tools (May 20, 2026), view navigation and screenshot capture (May 3 and May 26, 2026), and element property queries including related-element relationships.
- **[Sam-AEC/aec-model-bridge](https://github.com/Sam-AEC/aec-model-bridge)** (50 stars, Python/C#) — *Correction (2026-08-14): this project was renamed from "Autodesk-Revit-MCP-Server" to "aec-model-bridge" and expanded scope beyond Revit; the old repo URL now redirects here.* 100+ Revit API tools via reflection API for unlimited access, enterprise security options, Claude Desktop and Copilot integration, plus emerging Rhino/Navisworks/Power BI hooks.
- **[schauh11/revit-mcp-server](https://github.com/schauh11/revit-mcp-server)** (20 stars) — native WPF chat panel docked inside Revit, 53 tools, WebSocket communication. Unique embedded UI approach.
- **[Demolinator/revit-mcp-server](https://github.com/Demolinator/revit-mcp-server)** (24 stars, 84 commits) — pyRevit-based, 48 tools, supports Revit 2024-2027.

### Autodesk Official — aps-sample-mcp-server-revit-automation

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [aps-sample-mcp-server-revit-automation](https://github.com/autodesk-platform-services/aps-sample-mcp-server-revit-automation) | ~9 | C# | MIT | 2 |

Autodesk's official sample for headless Revit automation via the Automation API. Bridges AI assistants with cloud-hosted Revit models on ACC/BIM360 without manual interaction:

- **create_model** — creates new Revit models from templates
- **link_models** — manages Revit model link relationships (add/remove)
- **SSA authentication** — JWT bearer tokens with RSA signing for service-to-service auth
- **Fluent API** — type-safe model configuration with compile-time validation

Has a companion repo ([aps-sample-revit-mcp-tools-bundle](https://github.com/autodesk-platform-services/aps-sample-revit-mcp-tools-bundle), 14 stars) for the Automation API AppBundle, targeting Revit API 2027 on .NET 10. Both actively updated through April 2026.

### Autodesk MCP Apps — aps-mcp-app-example

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [aps-mcp-app-example](https://github.com/autodesk-platform-services/aps-mcp-app-example) | ~18 | JavaScript | MIT | Multiple |

The new direction for Autodesk's MCP strategy, replacing the archived aps-mcp-server-nodejs. Example MCP server with "MCP Apps" support for browsing ACC projects and designs with the APS Viewer. Uses Secure Service Accounts. Actively updated through April 2026.

### Autodesk AEC Data Model — aps-aecdm-mcp-dotnet

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [aps-aecdm-mcp-dotnet](https://github.com/autodesk-platform-services/aps-aecdm-mcp-dotnet) | ~40 | C# | MIT | 7 |

Connects Claude Desktop to the AEC Data Model API and Autodesk Viewer for querying architectural/engineering data using natural language:

- **GetToken** — PKCE authentication for APS API requests
- **GetHubs** / **GetProjects** — AEC Data Model API navigation
- **GetElementGroupsByProject** — element group retrieval
- **GetElementsByElementGroupWithCategoryFilter** — filtered element queries
- **RenderModel** / **HighLightElements** — visualization in Viewer

Enables conversational queries like "show me all the walls on level 2" against federated BIM models.

### Autodesk MCP Platform Strategy

Autodesk's MCP strategy has evolved since early 2026. The Node.js Platform Services server ([aps-mcp-server-nodejs](https://github.com/autodesk-platform-services/aps-mcp-server-nodejs), 25 stars) was **archived on May 7, 2026** *(Correction 2026-08-14: originally reported as "archived in March 2026" — the repo's own archive notice confirms May 7, 2026)*, signaling a shift away from monolithic API servers. The new direction centers on the **MCP Apps pattern** — modular, task-specific servers that integrate with the APS Viewer and Secure Service Accounts. The broader roadmap still includes production-grade managed MCP connectors for Design and Make agent workflows, with public servers planned for Revit, Model Data Explorer, and Fusion Data. The Automation API bundle (aps-sample-revit-mcp-tools-bundle) represents the cloud-native path for headless Revit operations.

## CAD Platforms

### daobataotie/CAD-MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [daobataotie/CAD-MCP](https://github.com/daobataotie/CAD-MCP) | ~499 | Python | MIT | Multiple |

The most popular CAD MCP server. An innovative natural language CAD control service supporting multiple platforms:

- **Multi-CAD support** — AutoCAD, GstarCAD (GCAD), ZWCAD
- **Drawing primitives** — lines, circles, arcs, rectangles, polylines, text, hatching, dimensions
- **Layer management** and file operations
- **Natural language parsing** — color recognition, shape/action keyword mapping
- **COM interface** — Windows-native via pywin32

Works with Claude Desktop, Windsurf, and Cursor. Dormant since July 2025 but continues gaining stars.

### puran-water/autocad-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [puran-water/autocad-mcp](https://github.com/puran-water/autocad-mcp) | ~452 | Python | MIT | 8 |

The most technically complete AutoCAD MCP server, with dual backends:

- **File IPC backend** — live AutoCAD LT control on Windows via Win32 messaging (focus-free dispatch, no window stealing)
- **ezdxf headless backend** — offline DXF generation on any platform (Linux, macOS, WSL) without AutoCAD installed
- **Freehand AutoLISP execution** — turns the server from a fixed command set into an extensible automation platform
- **8 consolidated tools** — drawing, entity, layer, block, annotation, P&ID symbols, view, and system management
- **Undo/redo** support
- **P&ID symbol library** — CTO-compatible process and instrumentation diagrams

v3.0 and v3.1 shipped February 2026 with File IPC replacing keyboard simulation, focus-free dispatch via Win32 PostMessageW, and robust error handling. Requires Windows 10/11 and AutoCAD LT 2024+ for the live backend.

### AnCode666/multiCAD-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [AnCode666/multiCAD-mcp](https://github.com/AnCode666/multiCAD-mcp) | ~85 | Python | Apache-2.0 | 7 (56 commands) |

The broadest CAD platform coverage: AutoCAD, ZWCAD, GstarCAD, and BricsCAD from a single MCP server. v0.2.0 shipped March 2026 with unified tool architecture, block attribute management, and comprehensive documentation. Seven unified tools provide access to 56 CAD commands covering:

- Block attribute management
- Layer and entity manipulation
- Data export capabilities
- COM-based architecture for real-time control

### Civil 3D

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [antonhofstader/Civil3D-mcp-python-COM](https://github.com/antonhofstader/Civil3D-mcp-python-COM) | ~7 | Python | — | 19 |

The first Civil 3D MCP server. Uses COM automation to control Autodesk Civil 3D for civil engineering workflows:

- **COGO points** — creation and management
- **Surfaces** — terrain surface operations
- **Corridors** — road/highway corridor design
- **19 tools** covering core civil engineering tasks

Created April 2026. Fills an important gap for infrastructure and site engineering.

### Additional AutoCAD Implementations

- **[thepiruthvirajan/autocad-mcp-server](https://github.com/thepiruthvirajan/autocad-mcp-server)** (59 stars) — Python COM automation for walls, doors, windows, and building structures with intelligent layer management. Notable star growth.
- **[ahmetcemkaraca/AutoCAD_MCP](https://github.com/ahmetcemkaraca/AutoCAD_MCP)** (29 stars) — AutoCAD 2025 with 7 working tools for 2D and 3D DWG production
- **[chichicaste/mcp-autocad-server](https://github.com/chichicaste/mcp-autocad-server)** (0 stars) — explicitly labeled by its own README as an incomplete learning reference implementation for natural language AutoCAD interaction, not a functional tool

## 3D Modeling

### mhyrr/sketchup-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mhyrr/sketchup-mcp](https://github.com/mhyrr/sketchup-mcp) | ~375 | Ruby | MIT | 8 |

Connects SketchUp to Claude AI through MCP, enabling AI-assisted 3D modeling and scene creation:

- **get_scene_info** / **get_selected_components** — scene inspection and analysis
- **create_component** / **delete_component** — object creation and removal
- **transform_component** — position, rotation, and scale operations
- **set_material** — material and color application
- **export_scene** — scene export
- **eval_ruby** — direct Ruby code execution within SketchUp for extensibility

Two-way TCP socket communication between Claude and SketchUp. Dormant since March 2025 but continues gaining stars passively.

### jingcheng-chen/rhinomcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [jingcheng-chen/rhinomcp](https://github.com/jingcheng-chen/rhinomcp) | ~1,000 | Python | MIT | 9+ |

*Correction (2026-08-14): license was previously listed as Apache-2.0; the repo's own [LICENSE file](https://github.com/jingcheng-chen/rhinomcp/blob/main/LICENSE) is MIT.* The most-starred construction MCP server covered in this review. Connects Rhino 3D to AI agents for prompt-assisted modeling and architectural design:

- **Two-way socket communication** with Rhino
- **3D object creation** — points, lines, circles, spheres, and other primitives
- **Object manipulation** — transformation, modification, deletion
- **Document inspection** and analysis tools
- **C# code execution** within Rhino (added v0.2.0, February 2026)
- **Curve operations** — added v0.2.1 (March 16, 2026)
- **Layer management** — create, set, delete operations
- **Object selection** with filtering logic
- **run_command / get_commands** — new in v0.2.2 (May 16, 2026): execute named Rhino commands with safety gates for arbitrary execution, and list available commands
- **Object attributes** — get_object_attributes, update_object_attributes, analyze_objects for inspecting and modifying geometry metadata
- **MCP tool annotations** and schema validation support
- **macOS one-shot installer** — new install.sh script for build and Mac user-level installation

v0.2.0 (February 2026) added C# code execution and advanced geometry operations. v0.2.1 (March 2026) added curve operations. v0.2.2 (May 16, 2026) added run_command, get_commands, object attribute tools, safety gates, and the macOS installer. Actively maintained. Supports Claude Desktop and Cursor AI environments.

### Grasshopper Parametric Design

Multiple MCP servers target Grasshopper, the visual programming environment for Rhino:

- **[veoery/GH_mcp_server](https://github.com/veoery/GH_mcp_server)** (31 stars, Python, MIT) — interact with Rhino and Grasshopper directly via LLMs, analyze .3dm files, auto-generate GHPython code based on user guidance. Still marked "under construction" as of this audit.
- **[alfredatnycu/grasshopper-mcp](https://github.com/alfredatnycu/grasshopper-mcp)** (94 stars) — bridging server with component knowledge base for high-level intent recognition.
- **[dongwoosuk/rhino-grasshopper-mcp](https://github.com/dongwoosuk/rhino-grasshopper-mcp)** (16 stars) — ML-based automatic layout optimization (DBSCAN, K-means, K-NN). Beta (v0.1.0-beta, 3 commits).

*Correction (2026-08-14): a fourth server previously listed here, "Xiaohu1009/AI-architecture," has been removed — its GitHub repository now returns 404 (deleted or made private) and can no longer be verified as a working, citable project.*

### Fusion 360

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [AuraFriday/Fusion-360-MCP-Server](https://github.com/AuraFriday/Fusion-360-MCP-Server) | ~118 | Python | — | 10 |

Autodesk Fusion add-in enabling AI agents to control Fusion 360 through MCP:

- **Generic API calls** — execute any Fusion command without custom code
- **Python code execution** with full Fusion API access and pre-injected shortcuts (app, ui, design, rootComponent)
- **Thread-safe architecture** — main-thread execution prevents crashes
- **Cross-operation context** via stored objects
- **Automatic signature-verified updates**
- **Listed on the Autodesk Store** (January 2026)

v1.2.75 (January 2026) added enhanced Python integration and single-main-thread architecture. Star count has continued to grow since. Additional Fusion 360 implementations include [Joe-Spencer/fusion-mcp-server](https://github.com/Joe-Spencer/fusion-mcp-server), [ArchimedesCrypto/fusion360-mcp-server](https://github.com/ArchimedesCrypto/fusion360-mcp-server), [Misterbra/fusion360-claude-ultimate](https://github.com/Misterbra/fusion360-claude-ultimate), and [sockcymbal/autodesk-fusion-mcp-python](https://github.com/sockcymbal/autodesk-fusion-mcp-python).

## Architecture BIM — ArchiCAD

### SzamosiMate/tapir-archicad-MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [SzamosiMate/tapir-archicad-MCP](https://github.com/SzamosiMate/tapir-archicad-MCP) | ~93 | Python | — | 191+ (auto-generated) |

The most innovative approach to tool generation in the construction MCP space. Dynamically generates MCP tools (191+ as of this audit, up from 137+ at last review) from the combined Tapir API and official Archicad JSON API schemas:

- **discover_tools** — semantic search to find relevant Archicad commands from natural language queries
- **191+ auto-generated tools** — covering the full breadth of Archicad's capabilities
- **Dual API merging** — community Tapir + official JSON API in a single server
- **PyPI/uvx installation** — simplified setup (added September 2025)

v0.4.0 ([released May 18, 2026](https://github.com/SzamosiMate/tapir-archicad-MCP/releases)) updated the generation pipeline to support Tapir 1.4.0, adding new commands across Element Creation, Modification, Project, Navigator, and Grouping namespaces. v0.3.2 (February 18, 2026) pinned the multiconn_archicad dependency. *Update (2026-08-23): the project has kept shipping — after v0.4.0 came v0.4.2 (June 18), v0.4.3 (June 24), v0.5.0 and v0.5.1 (both August 7), v0.5.2 (August 14), v0.5.3 (August 17, Tapir 1.5.7 schema), and [v0.5.4](https://github.com/SzamosiMate/tapir-archicad-MCP/releases/tag/v0.5.4) (August 19, updates tool definitions to Tapir 1.5.8); see the [releases page](https://github.com/SzamosiMate/tapir-archicad-MCP/releases) for what changed in each.* 93 stars as of this audit.

### lgradisar/archicad-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [lgradisar/archicad-mcp](https://github.com/lgradisar/archicad-mcp) | ~22 | JavaScript | MIT | Multiple |

The foundational ArchiCAD MCP implementation by Luka Gradišar. Requires the Tapir Archicad Add-On and supports custom tools alongside official JSON commands. A third implementation, [tiagoengdigital/archicad-mcp-claude](https://github.com/tiagoengdigital/archicad-mcp-claude) (2 stars), provides additional Claude Desktop integration.

## Structural Engineering

### HuVelasco/structural-mcp-servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [HuVelasco/structural-mcp-servers](https://github.com/HuVelasco/structural-mcp-servers) | ~2 | Python | — | 30+ |

MCP servers for structural engineering workflow automation. The ETABS server is production-ready (v0.7) with comprehensive COM-based integration:

- **Table extraction** — access to all 806 ETABS analysis/design tables
- **Building templates** — steel deck, concrete frame, wall models
- **Element creation and modification** tools
- **Model validation** with 3D visualization
- **User permission systems** and safety controls
- **Steel member design** with AISC code compliance
- **Stable connection management** via COM interface

Revit and Tekla servers are planned but not yet implemented.

### teknovizier/tekla_mcp_server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [teknovizier/tekla_mcp_server](https://github.com/teknovizier/tekla_mcp_server) | ~45 | Python | GPL-3.0 | 25+ |

The most actively developed construction MCP server — 410 commits (up from 239 at last review) and growing rapidly. MCP server for Tekla Structures enabling AI-powered steel detailing and modeling:

- **Component insertion** with semantic attribute mapping
- **Element selection and filtering** by multiple criteria
- **Model visualization** — zooming, coloring, hiding elements
- **Boolean cut operations** and part conversion
- **Custom attribute management** and element comparison
- **Collision detection** with mark filtering via GetAllObjects API (April 2026)
- **Warning system** for open drawings during collision detection
- **FastMCP 3.0** with modular providers and plugin system
- **MiniLM semantic attribute mapping** with LLM fallback — uses ML to understand natural language descriptions of structural components
- **mcp_handler decorator** for refactored error handling
- **Rectangular grid placement** — new MCP tool ([May 20, 2026](https://github.com/teknovizier/tekla_mcp_server/commits/main))
- **Move or copy selected elements** — new MCP tool (May 20, 2026)
- **Drawing revision marks** — exposed in drawing properties (May 20, 2026)
- **Per-provider disable** — disable specific providers via settings.json (May 20, 2026)
- **Property set failure tracking** — failures tracked and surfaced in tool output (May 20, 2026)

Active development continues with multiple commits per day as of May 20, 2026 — the most actively developed construction MCP server.

## OpenBIM & IFC

### helenkwok/openbim-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [helenkwok/openbim-mcp](https://github.com/helenkwok/openbim-mcp) | ~38 | TypeScript | MIT | 3 |

A vendor-neutral approach to BIM data access through open standards:

- **convert-ifc-to-frag** — transforms IFC files into optimized fragment format
- **load-frag** — loads fragment files for analysis
- **fetch-elements-of-category** — retrieves BIM elements by IFC category (walls, doors, windows) with configurable attributes and relationships

No changes since last review. Modest star growth.

### MCP4IFC

An academic framework enabling LLMs to directly manipulate Industry Foundation Classes (IFC) data through MCP. The server manages communication between AI clients and a Blender add-on, using IfcOpenShell as the main toolkit and exposing 50+ structured BIM tools as high-level wrappers while actual operations execute inside Blender. Published as a research paper: [MCP4IFC: IFC-Based Building Design using Large Language Models](https://arxiv.org/html/2511.05533v1).

### Blender Bonsai BIM MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [sinsunsan/blender-bonsai-bim-mcp](https://github.com/sinsunsan/blender-bonsai-bim-mcp) | ~5 | TypeScript | — | Multiple |

Creates BIM elements via natural language in Blender using the Bonsai BIM add-on. Early-stage (2 commits) but represents a novel approach combining open-source BIM tooling with MCP.

### Academic Reference Architecture

An arXiv paper, [A Modular Reference Architecture for MCP-Servers Enabling Agentic BIM Interaction](https://arxiv.org/abs/2601.00809), proposes a modular reference architecture for MCP servers enabling agentic BIM interaction. Its analysis of existing implementations covers Bonsai, WebIFC/Fragments, IfcOpenShell, Revit, and Archicad; the working prototype itself is built on IfcOpenShell. Provides a conceptual framework for standardizing BIM-MCP integration patterns.

## Construction Management

### AbhiGit-Trimble/construct-cost-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [AbhiGit-Trimble/construct-cost-mcp](https://github.com/AbhiGit-Trimble/construct-cost-mcp) | ~0 | Python | MIT | 5 |

A proof-of-concept construction cost estimation server using data from a public Google Sheet:

- **list_all_items** / **get_item** / **search_items** / **get_items_by_category** — browse construction pricing
- **calculate_cost** — compute project costs with quantities and labor rates
- Covers concrete, framing, finishes, electrical, plumbing, HVAC, roofing, and exterior materials
- Formula: Item Cost = (Material Cost × Quantity) + (Labor Hours × Quantity × Labor Rate)

*Correction (2026-08-14): earlier text described this as "from Trimble, a major construction technology company" based on the GitHub username containing "Trimble." That corporate affiliation could not be verified — the repository shows no Trimble organization ownership, no Trimble-domain contact, and no announcement on Trimble's own channels. Treat it as an independent developer's proof-of-concept unless Trimble affiliation is confirmed elsewhere.* Currently a minimal proof-of-concept.

### TylerIlunga/procore-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [TylerIlunga/procore-mcp-server](https://github.com/TylerIlunga/procore-mcp-server) | ~7 | TypeScript | — | 7 |

The first dedicated Procore MCP server. It provides 7 meta-tools that expose the full [Procore REST API](https://developers.procore.com/reference/rest/docs/rest-api-overview):

- **API category/endpoint discovery** — browse available Procore API capabilities
- **Search and detail retrieval** — find and inspect API endpoints
- **API call execution** — make authenticated Procore API requests
- **Config management** — OAuth with auto-refresh and cross-platform browser launch (Windows, macOS, Linux added May 7, 2026)

Created April 2026. The 7 meta-tools expose essentially the full Procore API surface via MCP, filling the most significant gap in the construction MCP ecosystem.

### Procore (via Third-Party MCP Gateways)

Procore is also accessible through third-party MCP gateways:

- **Zapier MCP** — Procore actions as MCP tools
- **viaSocket MCP** — Connect Procore with ChatGPT, Claude, and Cursor
- **Pipedream MCP** — Procore API integration

No official Procore MCP server exists yet, but the dedicated community server above provides direct API access without gateway intermediaries.

## What's missing

The construction MCP ecosystem still has significant gaps, particularly in the construction operations phase, though some are narrowing:

- **Bentley Systems has one public MCP server, but only for STAAD** — *Correction (2026-08-14): this entry previously cited a now-dead link (404) and claimed "no open-source repository exists." That's no longer accurate. Bentley has shipped an open-source structural-analysis MCP server, [BentleySystems/openstaad-mcp](https://github.com/BentleySystems/openstaad-mcp) (MIT license, ~39 stars), part of its [Infrastructure AI Co-Innovation Initiative](https://www.bentley.com/software/infrastructure-ai-co-innovation-initiative/) (confirmed by the [openstaad-mcp README itself](https://github.com/BentleySystems/openstaad-mcp), which links to the initiative under that same name), enabling AI agents to interact with STAAD.Pro models for load-case definition and data extraction.* MicroStation, OpenBuildings, OpenBridge, and OpenRoads still have no public GitHub MCP repos as of this audit.
- **No official Procore MCP** — a community server now exists (see above) but Procore hasn't shipped an official one
- **No building code compliance** — no automated code checking or plan review
- **No permit management** — PermitFlow and other permit platforms have no MCP servers
- **No construction scheduling** — Primavera P6, Microsoft Project, Asta Powerproject all absent
- **No serious estimating** — only a proof-of-concept Google Sheet-based server, [AbhiGit-Trimble/construct-cost-mcp](https://github.com/AbhiGit-Trimble/construct-cost-mcp) (see correction above on the unverified Trimble affiliation)
- **No site safety/inspection tools** — no safety compliance checking, punch list management, or daily log automation
- **No drone/photogrammetry integration** — despite drones being ubiquitous on construction sites
- **No Vectorworks MCP** — popular in architecture and landscape design
- **Structural analysis coverage is narrow** — beyond ETABS and Bentley's own [openstaad-mcp](https://github.com/BentleySystems/openstaad-mcp) for STAAD.Pro (see Bentley entry above), SAP2000, RISA, and Robot Structural Analysis have no public MCP servers
- **No MEP-specific tools** — mechanical, electrical, plumbing design has no dedicated MCP servers
- **No energy modeling integration** — EnergyPlus has MCP servers (see our [Energy & Utilities review](/reviews/energy-utilities-mcp-servers/)) but they're not construction-workflow integrated
- **No Archicad official server** — community-only (though [tapir-archicad-MCP](https://github.com/SzamosiMate/tapir-archicad-MCP) at 88 stars shows strong demand), Graphisoft hasn't shipped one

## The bottom line

**Rating: 4.0/5** — The construction and architecture MCP ecosystem remains one of the most active verticals for a traditionally offline, desktop-heavy industry. Rhino has [crossed 1,000 stars](https://github.com/jingcheng-chen/rhinomcp) with v0.2.2 adding run_command, object attribute tools, safety gates, and a macOS installer *(Correction 2026-08-14: this line previously said "crossed 400 stars," which contradicted the review's own table — which at the time already showed rhinomcp at 941 stars — a leftover error from an earlier draft)*. ArchiCAD shipped v0.4.0 with Tapir 1.4.0 support and new commands across Element Creation, Modification, Navigator, and Grouping namespaces, and has continued shipping through v0.5.1 since. Tekla continues its remarkable streak — rectangular grid placement, move/copy elements, drawing revision marks, and per-provider configuration all shipped in a single May 20 burst, confirmed against the project's own commit history. oakplank/RevitMCP added schedule inspection/editing and view navigation as of May 20. SketchUp (375 stars) and [daobataotie/CAD-MCP](https://github.com/daobataotie/CAD-MCP) (499 stars) keep accumulating stars despite dormancy, signaling strong latent demand *(Correction 2026-08-14: CAD-MCP's star count here previously said 347, which contradicted the review's own table — which at the time already showed 453 — also a leftover draft error)*.

The design-versus-construction divide is narrowing meaningfully. The Procore community server provides 7 meta-tools exposing the full Procore REST API with cross-platform OAuth (May 2026). But construction scheduling, estimating, safety, inspections, and permitting still have no MCP representation. For a global construction industry McKinsey pegs at [$13 trillion in annual output as of 2023](https://www.mckinsey.com/capabilities/operations/our-insights/delivering-on-construction-productivity-is-no-longer-optional) *(Correction 2026-08-14: the original Statista URL now resolves to an unrelated statistic — replaced with McKinsey's own figure)*, the construction operations side remains underserved — though the trajectory is improving.

**Install if:** you work with Revit, AutoCAD, Rhino, SketchUp, ArchiCAD, Tekla Structures, or Civil 3D and want AI-assisted modeling, design automation, or BIM data queries.

**Skip if:** you need construction project management, scheduling, estimating, or site operations — the MCP ecosystem is just starting to reach those workflows.

*This review was last edited on 2026-05-21 and claim-level source-audited on 2026-08-23 using Claude Sonnet 5 (Anthropic).*

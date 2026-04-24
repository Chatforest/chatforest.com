---
title: "Construction & Architecture MCP Servers — Revit, AutoCAD, SketchUp, Rhino, ArchiCAD, Tekla, BIM/IFC, and More"
date: 2026-03-15T17:00:00+09:00
description: "Construction and architecture MCP servers are connecting AI agents to BIM software, CAD platforms, 3D modeling tools, structural analysis programs, and construction management systems."
og_description: "Construction & architecture MCP servers: Revit (399 stars archived → 121-star successor monorepo + community explosion), AutoCAD (316 stars, multi-CAD), SketchUp (225 stars), Rhino (365 stars, v0.2.1 curve ops), ArchiCAD (49 stars, 137 auto-tools), Tekla (32 stars, 239 commits, collision detection, FastMCP 3.0), ETABS (30+ structural tools), OpenBIM/IFC (36 stars), Fusion 360 (84 stars), NEW Civil3D MCP (19 tools), first Procore MCP server (7 tools, OAuth). Rating: 4.0/5."
content_type: "Review"
card_description: "Construction and architecture MCP servers for BIM, CAD, 3D modeling, structural engineering, and construction management. This is one of the most active MCP verticals for a traditionally offline industry. Revit leads the BIM category with revit-mcp (399 stars, archived) recommending migration to the successor monorepo mcp-servers-for-revit (121 stars, npm-published). A wave of community Revit servers has emerged: oakplank/RevitMCP (41 stars, pyRevit, 22 tools), Sam-AEC/Autodesk-Revit-MCP-Server (15 stars, 100+ tools via reflection API), Demolinator/revit-mcp-server (45 tools), and schauh11/revit-mcp-server (53 tools, native WPF chat panel inside Revit). Autodesk has shifted its MCP strategy — archiving aps-mcp-server-nodejs (March 2026) and moving toward the MCP Apps pattern with aps-mcp-app-example (9 stars, ACC project browsing with APS Viewer) and aps-sample-revit-mcp-tools-bundle (5 stars, Automation API AppBundle targeting Revit API 2027). AutoCAD has six implementations — daobataotie/CAD-MCP (316 stars) leads with multi-CAD support, puran-water/autocad-mcp (214 stars) offers AutoLISP execution and headless ezdxf backend, AnCode666/multiCAD-mcp (26 stars) now supports BricsCAD with 55 commands. NEW: antonhofstader/Civil3D-mcp-python-COM (4 stars, 19 tools for Civil 3D via COM — COGO points, surfaces, corridors). For 3D modeling, Rhino has jingcheng-chen/rhinomcp (365 stars, v0.2.1 with curve operations and C# code execution), SketchUp has mhyrr/sketchup-mcp (225 stars, dormant), and Fusion 360 has AuraFriday/Fusion-360-MCP-Server (84 stars, Autodesk Store listed). ArchiCAD has SzamosiMate/tapir-archicad-MCP (49 stars, 137 auto-generated tools). Structural engineering's standout is teknovizier/tekla_mcp_server (32 stars, 239 commits — the most actively developed construction MCP server) with collision detection, FastMCP 3.0, modular providers, and MiniLM semantic attribute mapping. Construction management gap is narrowing: TylerIlunga/procore-mcp-server (7 tools, OAuth with auto-refresh) is the first dedicated Procore MCP server. Notable gaps remain: no Bentley/MicroStation, no construction scheduling, no building code compliance, no SAP2000/STAAD/RISA structural servers, no MEP-specific tools. Rating: 4.0/5."
last_refreshed: 2026-04-25
---

Construction and architecture MCP servers are connecting AI agents to BIM software, CAD platforms, 3D modeling tools, structural analysis programs, and construction management systems. Instead of manually navigating complex 3D modeling interfaces, creating construction drawings by hand, or running structural analyses through multi-step GUI workflows, these servers let AI assistants create building elements, query BIM data, execute CAD commands, generate parametric designs, run structural calculations, and manage construction data — all through the Model Context Protocol.

The landscape spans seven areas: **BIM & Revit** (Autodesk's flagship and the largest MCP ecosystem in construction), **CAD platforms** (AutoCAD, GstarCAD, ZWCAD, BricsCAD), **3D modeling** (SketchUp, Rhino, Grasshopper, Fusion 360), **architecture BIM** (ArchiCAD), **structural engineering** (ETABS, Tekla Structures), **OpenBIM/IFC** (open standards for BIM data exchange), and **construction management** (cost estimation, project management).

The headline findings: **Autodesk is pivoting its MCP strategy** — archiving the Node.js Platform Services server and shifting toward the MCP Apps pattern (aps-mcp-app-example) and cloud Automation API bundles. **The Revit community has exploded** — the original revit-mcp (399 stars, archived) spawned a successor monorepo plus four new community servers with 22-100+ tools each. **Tekla is now the most actively developed construction MCP server** — teknovizier/tekla_mcp_server has jumped to 239 commits with collision detection, FastMCP 3.0, and semantic attribute mapping. **Rhino remains the second most-starred** — rhinomcp (365 stars) shipped v0.2.1 with curve operations and C# code execution. **AutoCAD has seven implementations** — and Civil 3D now has its first MCP server. **The construction management gap is narrowing** — the first dedicated Procore MCP server has appeared with 7 tools and OAuth support. **The design phase remains far stronger than construction operations** — but the gap is slowly closing.

**Category:** [Logistics & Industry](/categories/logistics-industry/)

## BIM & Revit

### revit-mcp/revit-mcp (Archived)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [revit-mcp/revit-mcp](https://github.com/revit-mcp/revit-mcp) | ~399 | TypeScript | MIT | 27 |

The most popular construction MCP server by star count. Enables AI systems to query Revit project data and drive modeling operations through 27 tools:

- **Data retrieval** — view info, element queries, family type inspection
- **Creation** — points, lines, surfaces, grids, levels, rooms, building elements
- **Modification** — color changes, tagging, element operations
- **Code execution** — arbitrary C# execution within Revit for extensibility
- **Storage** — operation history and state management

The project was archived in February 2026 with a deprecation notice recommending migration to the successor monorepo.

### mcp-servers-for-revit/mcp-servers-for-revit (Successor)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-servers-for-revit](https://github.com/mcp-servers-for-revit/mcp-servers-for-revit) | ~121 | TypeScript/C# | MIT | 27+ |

The official successor monorepo combining the TypeScript MCP server, C# Revit plugin, and command set. Published to npm as `mcp-server-for-revit`. Supports Revit 2020-2026 with installable releases. Development has slowed since February 2026 but the package is stable.

### Community Revit Servers

The Revit MCP ecosystem has exploded with multiple independent implementations:

- **oakplank/RevitMCP** (41 stars, Python, MIT) — pyRevit extension with 22 tools, web UI and MCP dual modes. The most mature community alternative.
- **Sam-AEC/Autodesk-Revit-MCP-Server** (15 stars, Python/C#) — 100+ Revit API tools via reflection API for unlimited access, enterprise security options, Claude Desktop and Copilot integration.
- **schauh11/revit-mcp-server** — native WPF chat panel docked inside Revit, 53 tools, WebSocket communication. Unique embedded UI approach.
- **Demolinator/revit-mcp-server** (2 stars, 69 commits) — pyRevit-based, 45 tools, supports Revit 2024-2026.

### Autodesk Official — aps-sample-mcp-server-revit-automation

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [aps-sample-mcp-server-revit-automation](https://github.com/autodesk-platform-services/aps-sample-mcp-server-revit-automation) | ~6 | C# | MIT | 2 |

Autodesk's official sample for headless Revit automation via the Automation API. Bridges AI assistants with cloud-hosted Revit models on ACC/BIM360 without manual interaction:

- **create_model** — creates new Revit models from templates
- **link_models** — manages Revit model link relationships (add/remove)
- **SSA authentication** — JWT bearer tokens with RSA signing for service-to-service auth
- **Fluent API** — type-safe model configuration with compile-time validation

Has a companion repo (aps-sample-revit-mcp-tools-bundle, 5 stars) for the Automation API AppBundle, targeting Revit API 2027 on .NET 10. Both actively updated through April 2026.

### Autodesk MCP Apps — aps-mcp-app-example

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [aps-mcp-app-example](https://github.com/autodesk-platform-services/aps-mcp-app-example) | ~9 | JavaScript | MIT | Multiple |

The new direction for Autodesk's MCP strategy, replacing the archived aps-mcp-server-nodejs. Example MCP server with "MCP Apps" support for browsing ACC projects and designs with the APS Viewer. Uses Secure Service Accounts. Actively updated through April 2026.

### Autodesk AEC Data Model — aps-aecdm-mcp-dotnet

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [aps-aecdm-mcp-dotnet](https://github.com/autodesk-platform-services/aps-aecdm-mcp-dotnet) | ~34 | C# | MIT | 7 |

Connects Claude Desktop to the AEC Data Model API and Autodesk Viewer for querying architectural/engineering data using natural language:

- **GetToken** — PKCE authentication for APS API requests
- **GetHubs** / **GetProjects** — AEC Data Model API navigation
- **GetElementGroupsByProject** — element group retrieval
- **GetElementsByElementGroupWithCategoryFilter** — filtered element queries
- **RenderModel** / **HighLightElements** — visualization in Viewer

Enables conversational queries like "show me all the walls on level 2" against federated BIM models.

### Autodesk MCP Platform Strategy

Autodesk's MCP strategy has evolved since early 2026. The Node.js Platform Services server (aps-mcp-server-nodejs, 18 stars) was **archived in March 2026**, signaling a shift away from monolithic API servers. The new direction centers on the **MCP Apps pattern** — modular, task-specific servers that integrate with the APS Viewer and Secure Service Accounts. The broader roadmap still includes production-grade managed MCP connectors for Design and Make agent workflows, with public servers planned for Revit, Model Data Explorer, and Fusion Data. The Automation API bundle (aps-sample-revit-mcp-tools-bundle) represents the cloud-native path for headless Revit operations.

## CAD Platforms

### daobataotie/CAD-MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [daobataotie/CAD-MCP](https://github.com/daobataotie/CAD-MCP) | ~316 | Python | MIT | Multiple |

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
| [puran-water/autocad-mcp](https://github.com/puran-water/autocad-mcp) | ~214 | Python | MIT | 8 |

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
| [AnCode666/multiCAD-mcp](https://github.com/AnCode666/multiCAD-mcp) | ~26 | Python | Apache-2.0 | 7 (55 commands) |

The broadest CAD platform coverage: AutoCAD, ZWCAD, GstarCAD, and BricsCAD from a single MCP server. v0.2.0 shipped March 2026 with unified tool architecture, block attribute management, and comprehensive documentation. Seven unified tools provide access to 55 CAD commands covering:

- Block attribute management
- Layer and entity manipulation
- Data export capabilities
- COM-based architecture for real-time control

### Civil 3D

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [antonhofstader/Civil3D-mcp-python-COM](https://github.com/antonhofstader/Civil3D-mcp-python-COM) | ~4 | Python | — | 19 |

The first Civil 3D MCP server. Uses COM automation to control Autodesk Civil 3D for civil engineering workflows:

- **COGO points** — creation and management
- **Surfaces** — terrain surface operations
- **Corridors** — road/highway corridor design
- **19 tools** covering core civil engineering tasks

Created April 2026. Fills an important gap for infrastructure and site engineering.

### Additional AutoCAD Implementations

- **thepiruthvirajan/autocad-mcp-server** (34 stars) — Python COM automation for walls, doors, windows, and building structures with intelligent layer management. Notable star growth.
- **ahmetcemkaraca/AutoCAD_MCP** — AutoCAD 2025 with 7 working tools for 2D and 3D DWG production
- **chichicaste/mcp-autocad-server** — learning reference implementation for natural language AutoCAD interaction

## 3D Modeling

### mhyrr/sketchup-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mhyrr/sketchup-mcp](https://github.com/mhyrr/sketchup-mcp) | ~225 | Ruby | MIT | 8 |

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
| [jingcheng-chen/rhinomcp](https://github.com/jingcheng-chen/rhinomcp) | ~365 | Python | Apache-2.0 | 7+ |

The second most-starred construction MCP server. Connects Rhino 3D to AI agents for prompt-assisted modeling and architectural design:

- **Two-way socket communication** with Rhino
- **3D object creation** — points, lines, circles, spheres, and other primitives
- **Object manipulation** — transformation, modification, deletion
- **Document inspection** and analysis tools
- **C# code execution** within Rhino (added v0.2.0, February 2026)
- **Curve operations** — new in v0.2.1 (March 16, 2026)
- **Layer management** — create, set, delete operations
- **Object selection** with filtering logic

v0.2.0 (February 2026) added C# code execution and advanced geometry operations. v0.2.1 (March 2026) added curve operations. Actively maintained with 123 commits. Supports Claude Desktop and Cursor AI environments.

### Grasshopper Parametric Design

Multiple MCP servers target Grasshopper, the visual programming environment for Rhino:

- **veoery/GH_mcp_server** (31 stars, Python, MIT) — interact with Rhino and Grasshopper directly via LLMs, analyze .3dm files, auto-generate GHPython code based on user guidance. Dormant since April 2025, still marked "under construction."
- **Xiaohu1009/AI-architecture** — unified Rhino + Grasshopper MCP server providing AI agents with comprehensive 3D modeling and parametric design capabilities.
- **alfredatnycu/grasshopper-mcp** — bridging server with component knowledge base for high-level intent recognition.
- **dongwoosuk/rhino-grasshopper-mcp** (8 stars) — ML-based automatic layout optimization (DBSCAN, K-means, K-NN). Single-commit beta, dormant since December 2025.

### Fusion 360

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [AuraFriday/Fusion-360-MCP-Server](https://github.com/AuraFriday/Fusion-360-MCP-Server) | ~84 | Python | — | 10 |

Autodesk Fusion add-in enabling AI agents to control Fusion 360 through MCP:

- **Generic API calls** — execute any Fusion command without custom code
- **Python code execution** with full Fusion API access and pre-injected shortcuts (app, ui, design, rootComponent)
- **Thread-safe architecture** — main-thread execution prevents crashes
- **Cross-operation context** via stored objects
- **Automatic signature-verified updates**
- **Listed on the Autodesk Store** (January 2026)

v1.2.75 (January 2026) added enhanced Python integration and single-main-thread architecture. Significant star growth (+33) but dormant since January 2026. Additional Fusion 360 implementations include Joe-Spencer/fusion-mcp-server, ArchimedesCrypto/fusion360-mcp-server, Misterbra/fusion360-claude-ultimate, and sockcymbal/autodesk-fusion-mcp-python.

## Architecture BIM — ArchiCAD

### SzamosiMate/tapir-archicad-MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [SzamosiMate/tapir-archicad-MCP](https://github.com/SzamosiMate/tapir-archicad-MCP) | ~49 | Python | — | 137 (auto-generated) |

The most innovative approach to tool generation in the construction MCP space. Dynamically generates 137 MCP tools from the combined Tapir API and official Archicad JSON API schemas:

- **discover_tools** — semantic search to find relevant Archicad commands from natural language queries
- **137 auto-generated tools** — covering the full breadth of Archicad's capabilities
- **Dual API merging** — community Tapir + official JSON API in a single server
- **PyPI/uvx installation** — simplified setup (added September 2025)

v0.3.2 (February 2026) pinned multiconn_archicad dependency. November 2025 added 7 new Tapir tools (updated to Tapir 1.2.4). Growing community interest at 49 stars.

### lgradisar/archicad-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [lgradisar/archicad-mcp](https://github.com/lgradisar/archicad-mcp) | ~16 | JavaScript | MIT | Multiple |

The foundational ArchiCAD MCP implementation by Luka Gradišar. Requires the Tapir Archicad Add-On and supports custom tools alongside official JSON commands. Dormant since August 2025. A third implementation, tiagoengdigital/archicad-mcp-claude, provides additional Claude Desktop integration.

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
| [teknovizier/tekla_mcp_server](https://github.com/teknovizier/tekla_mcp_server) | ~32 | Python | GPL-3.0 | 23+ |

The most actively developed construction MCP server — 239 commits and growing rapidly. MCP server for Tekla Structures enabling AI-powered steel detailing and modeling:

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

Active development continues with multiple commits per week as of April 2026.

## OpenBIM & IFC

### helenkwok/openbim-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [helenkwok/openbim-mcp](https://github.com/helenkwok/openbim-mcp) | ~36 | TypeScript | MIT | 3 |

A vendor-neutral approach to BIM data access through open standards:

- **convert-ifc-to-frag** — transforms IFC files into optimized fragment format
- **load-frag** — loads fragment files for analysis
- **fetch-elements-of-category** — retrieves BIM elements by IFC category (walls, doors, windows) with configurable attributes and relationships

No changes since last review. Modest star growth.

### MCP4IFC

An academic framework enabling LLMs to directly manipulate Industry Foundation Classes (IFC) data through MCP. The server manages communication between AI clients and a Blender add-on, exposing structured BIM tools as high-level wrappers while actual operations execute inside Blender. Published as a research paper (arxiv.org/html/2511.05533v1).

### Blender Bonsai BIM MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [sinsunsan/blender-bonsai-bim-mcp](https://github.com/sinsunsan/blender-bonsai-bim-mcp) | ~3 | TypeScript | — | Multiple |

Creates BIM elements via natural language in Blender using the Bonsai BIM add-on. Early-stage (2 commits) but represents a novel approach combining open-source BIM tooling with MCP.

### Academic Reference Architecture

An arXiv paper (2601.00809) proposes a modular reference architecture for MCP servers enabling agentic BIM interaction, covering Bonsai, WebIFC/Fragments, IfcOpenShell, Revit, and Archicad. Provides a conceptual framework for standardizing BIM-MCP integration patterns.

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

From Trimble, a major construction technology company, but currently a minimal proof-of-concept.

### TylerIlunga/procore-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [TylerIlunga/procore-mcp-server](https://github.com/TylerIlunga/procore-mcp-server) | ~0 | TypeScript | — | 7 |

The first dedicated Procore MCP server. Provides 7 tools for interacting with the Procore construction management API:

- **API category/endpoint discovery** — browse available Procore API capabilities
- **Search and detail retrieval** — find and inspect API endpoints
- **API call execution** — make authenticated Procore API requests
- **Config management** — OAuth with auto-refresh token support

Created April 2026. While still at 0 stars, this fills the most significant gap in the construction MCP ecosystem — Procore is the dominant project management platform in the industry.

### Procore (via Third-Party MCP Gateways)

Procore is also accessible through third-party MCP gateways:

- **Zapier MCP** — Procore actions as MCP tools
- **viaSocket MCP** — Connect Procore with ChatGPT, Claude, and Cursor
- **Pipedream MCP** — Procore API integration

No official Procore MCP server exists yet, but the dedicated community server above provides direct API access without gateway intermediaries.

## What's missing

The construction MCP ecosystem still has significant gaps, particularly in the construction operations phase, though some are narrowing:

- **No Bentley Systems servers** — MicroStation, OpenBuildings, OpenBridge, OpenRoads all absent (Bentley released MicroStation 2026 with AI features but no MCP server)
- **No official Procore MCP** — a community server now exists (see above) but Procore hasn't shipped an official one
- **No building code compliance** — no automated code checking or plan review
- **No permit management** — PermitFlow and other permit platforms have no MCP servers
- **No construction scheduling** — Primavera P6, Microsoft Project, Asta Powerproject all absent
- **No serious estimating** — only a proof-of-concept Google Sheet-based server from Trimble
- **No site safety/inspection tools** — no safety compliance checking, punch list management, or daily log automation
- **No drone/photogrammetry integration** — despite drones being ubiquitous on construction sites
- **No Vectorworks MCP** — popular in architecture and landscape design
- **No structural analysis beyond ETABS** — SAP2000, STAAD.Pro, RISA, Robot Structural Analysis all absent
- **No MEP-specific tools** — mechanical, electrical, plumbing design has no dedicated MCP servers
- **No energy modeling integration** — EnergyPlus has MCP servers (see our [Energy & Utilities review](/reviews/energy-utilities-mcp-servers/)) but they're not construction-workflow integrated
- **No Archicad official server** — community-only (though tapir-archicad-MCP at 49 stars shows strong demand), Graphisoft hasn't shipped one

## The bottom line

**Rating: 4.0/5** — The construction and architecture MCP ecosystem continues to be one of the most active verticals for a traditionally offline, desktop-heavy industry. The Revit community has exploded — four new community servers complement the official successor monorepo, giving users choices from pyRevit extensions to embedded WPF chat panels. Autodesk is pivoting from monolithic API servers (archiving aps-mcp-server-nodejs) to the modular MCP Apps pattern. Tekla has emerged as the most actively developed construction MCP server (239 commits) with collision detection and FastMCP 3.0. Rhino shipped v0.2.1 with curve operations and C# code execution. Civil 3D got its first MCP server. The ArchiCAD auto-generated 137 tools approach continues to gain traction at 49 stars.

The design-versus-construction divide is slowly narrowing. The first dedicated Procore MCP server has appeared (April 2026), providing direct API access to the industry's dominant project management platform. But construction scheduling, estimating, safety, inspections, and permitting still have no MCP representation. For a $2 trillion global industry, the construction operations side remains underserved — though the trajectory is positive.

**Install if:** you work with Revit, AutoCAD, Rhino, SketchUp, ArchiCAD, Tekla Structures, or Civil 3D and want AI-assisted modeling, design automation, or BIM data queries.

**Skip if:** you need construction project management, scheduling, estimating, or site operations — the MCP ecosystem is just starting to reach those workflows.

*This review was last edited on 2026-04-25 using Claude Opus 4.6 (Anthropic).*

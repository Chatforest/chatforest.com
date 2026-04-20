# Construction & Architecture MCP Servers — Revit, AutoCAD, SketchUp, Rhino, ArchiCAD, Tekla, BIM/IFC, and More

> Construction and architecture MCP servers are connecting AI agents to BIM software, CAD platforms, 3D modeling tools, structural analysis programs, and construction management systems.


Construction and architecture MCP servers are connecting AI agents to BIM software, CAD platforms, 3D modeling tools, structural analysis programs, and construction management systems. Instead of manually navigating complex 3D modeling interfaces, creating construction drawings by hand, or running structural analyses through multi-step GUI workflows, these servers let AI assistants create building elements, query BIM data, execute CAD commands, generate parametric designs, run structural calculations, and manage construction data — all through the Model Context Protocol.

The landscape spans seven areas: **BIM & Revit** (Autodesk's flagship and the largest MCP ecosystem in construction), **CAD platforms** (AutoCAD, GstarCAD, ZWCAD, BricsCAD), **3D modeling** (SketchUp, Rhino, Grasshopper, Fusion 360), **architecture BIM** (ArchiCAD), **structural engineering** (ETABS, Tekla Structures), **OpenBIM/IFC** (open standards for BIM data exchange), and **construction management** (cost estimation, project management).

The headline findings: **Autodesk has made MCP a core part of its platform strategy** — with four official servers and a public roadmap for production-grade MCP connectors across Revit, AutoCAD, Civil 3D, and Construction Cloud. **Revit has the most mature MCP integration in construction** — revit-mcp (362 stars) offers 27 tools for full BIM automation. **AutoCAD has six independent implementations** — more than any other CAD platform. **Rhino is the second most-starred construction MCP server** — jingcheng-chen/rhinomcp (316 stars) plus Grasshopper parametric design integration. **Structural engineering has a surprisingly strong start** — the ETABS server provides 30+ tools with access to all 806 analysis tables and AISC steel code compliance. **The design phase is well-covered; the construction phase is not** — there's a sharp drop-off from modeling to actual project management, scheduling, and site operations.

**Category:** [Logistics & Industry](/categories/logistics-industry/)

## BIM & Revit

### revit-mcp/revit-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [revit-mcp/revit-mcp](https://github.com/revit-mcp/revit-mcp) | ~362 | TypeScript | MIT | 27 |

The most popular construction MCP server. Enables AI systems to query Revit project data and drive modeling operations through 27 tools:

- **Data retrieval** — view info, element queries, family type inspection
- **Creation** — points, lines, surfaces, grids, levels, rooms, building elements
- **Modification** — color changes, tagging, element operations
- **Code execution** — arbitrary C# execution within Revit for extensibility
- **Storage** — operation history and state management

The project was archived in February 2026 with a deprecation notice recommending migration to the monorepo at mcp-servers-for-revit/mcp-servers-for-revit for simpler installation and CI workflows.

### Autodesk Official — aps-sample-mcp-server-revit-automation

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [aps-sample-mcp-server-revit-automation](https://github.com/autodesk-platform-services/aps-sample-mcp-server-revit-automation) | ~2 | C# | MIT | 2 |

Autodesk's official sample for headless Revit automation via the Automation API. Bridges AI assistants with cloud-hosted Revit models on ACC/BIM360 without manual interaction:

- **create_model** — creates new Revit models from templates
- **link_models** — manages Revit model link relationships (add/remove)
- **SSA authentication** — JWT bearer tokens with RSA signing for service-to-service auth
- **Fluent API** — type-safe model configuration with compile-time validation

Designed as extensible — developers add custom tools following a consistent pattern. Currently limited to 2 tools but represents Autodesk's official direction for cloud-native BIM automation.

### Autodesk Platform Services — aps-mcp-server-nodejs

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [aps-mcp-server-nodejs](https://github.com/autodesk-platform-services/aps-mcp-server-nodejs) | ~17 | JavaScript | MIT | Multiple |

Official Node.js MCP server providing access to the Autodesk Platform Services API with fine-grained access control using Secure Service Accounts. Works with Claude Desktop, VS Code + GitHub Copilot, Cursor, and MCP Inspector. Covers ACC (Autodesk Construction Cloud) integration.

### Autodesk AEC Data Model — aps-aecdm-mcp-dotnet

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [aps-aecdm-mcp-dotnet](https://github.com/autodesk-platform-services/aps-aecdm-mcp-dotnet) | ~33 | C# | MIT | 7 |

Connects Claude Desktop to the AEC Data Model API and Autodesk Viewer for querying architectural/engineering data using natural language:

- **GetToken** — PKCE authentication for APS API requests
- **GetHubs** / **GetProjects** — AEC Data Model API navigation
- **GetElementGroupsByProject** — element group retrieval
- **GetElementsByElementGroupWithCategoryFilter** — filtered element queries
- **RenderModel** / **HighLightElements** — visualization in Viewer

Enables conversational queries like "show me all the walls on level 2" against federated BIM models.

### Autodesk MCP Platform Strategy

Beyond individual servers, Autodesk has announced a broader MCP initiative: production-grade, managed MCP connectors purpose-built for Design and Make agent workflows. The roadmap includes public servers for Revit, Model Data Explorer, and Fusion Data, with a vision for a Design and Make marketplace of trusted third-party MCP servers. Autodesk Assistant will run on MCP infrastructure, meaning users in Revit, AutoCAD, Civil 3D, and Autodesk Construction Cloud will get a consistent AI-powered experience across tools.

## CAD Platforms

### daobataotie/CAD-MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [daobataotie/CAD-MCP](https://github.com/daobataotie/CAD-MCP) | ~264 | Python | MIT | Multiple |

The most popular CAD MCP server. An innovative natural language CAD control service supporting multiple platforms:

- **Multi-CAD support** — AutoCAD, GstarCAD (GCAD), ZWCAD
- **Drawing primitives** — lines, circles, arcs, rectangles, polylines, text, hatching, dimensions
- **Layer management** and file operations
- **Natural language parsing** — color recognition, shape/action keyword mapping
- **COM interface** — Windows-native via pywin32

Works with Claude Desktop, Windsurf, and Cursor.

### puran-water/autocad-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [puran-water/autocad-mcp](https://github.com/puran-water/autocad-mcp) | ~173 | Python | MIT | 8 |

The most technically complete AutoCAD MCP server, with dual backends:

- **File IPC backend** — live AutoCAD LT control on Windows via Win32 messaging (focus-free dispatch, no window stealing)
- **ezdxf headless backend** — offline DXF generation on any platform (Linux, macOS, WSL) without AutoCAD installed
- **Freehand AutoLISP execution** — turns the server from a fixed command set into an extensible automation platform
- **8 consolidated tools** — drawing, entity, layer, block, annotation, P&ID symbols, view, and system management
- **Undo/redo** support
- **P&ID symbol library** — CTO-compatible process and instrumentation diagrams

Requires Windows 10/11 and AutoCAD LT 2024+ for the live backend.

### AnCode666/multiCAD-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [AnCode666/multiCAD-mcp](https://github.com/AnCode666/multiCAD-mcp) | ~14 | Python | Apache-2.0 | 7 (55 commands) |

The broadest CAD platform coverage: AutoCAD, ZWCAD, GstarCAD, and BricsCAD from a single MCP server. Seven unified tools provide access to 55 CAD commands covering:

- Block attribute management
- Layer and entity manipulation
- Data export capabilities
- COM-based architecture for real-time control

### Additional AutoCAD Implementations

- **ahmetcemkaraca/AutoCAD_MCP** — AutoCAD 2025 with 7 working tools for 2D and 3D DWG production
- **thepiruthvirajan/autocad-mcp-server** — Python COM automation for walls, doors, windows, and building structures with intelligent layer management
- **chichicaste/mcp-autocad-server** — learning reference implementation for natural language AutoCAD interaction

## 3D Modeling

### mhyrr/sketchup-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mhyrr/sketchup-mcp](https://github.com/mhyrr/sketchup-mcp) | ~191 | Ruby | MIT | 8 |

Connects SketchUp to Claude AI through MCP, enabling AI-assisted 3D modeling and scene creation:

- **get_scene_info** / **get_selected_components** — scene inspection and analysis
- **create_component** / **delete_component** — object creation and removal
- **transform_component** — position, rotation, and scale operations
- **set_material** — material and color application
- **export_scene** — scene export
- **eval_ruby** — direct Ruby code execution within SketchUp for extensibility

Two-way TCP socket communication between Claude and SketchUp.

### jingcheng-chen/rhinomcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [jingcheng-chen/rhinomcp](https://github.com/jingcheng-chen/rhinomcp) | ~316 | Python | Apache-2.0 | 7 |

The second most-starred construction MCP server. Connects Rhino 3D to AI agents for prompt-assisted modeling and architectural design:

- **Two-way socket communication** with Rhino
- **3D object creation** — points, lines, circles, spheres, and other primitives
- **Object manipulation** — transformation, modification, deletion
- **Document inspection** and analysis tools
- **Python script execution** within Rhino
- **Layer management** — create, set, delete operations
- **Object selection** with filtering logic

Supports Claude Desktop and Cursor AI environments.

### Grasshopper Parametric Design

Multiple MCP servers target Grasshopper, the visual programming environment for Rhino:

- **veoery/GH_mcp_server** (27 stars, Python, MIT) — interact with Rhino and Grasshopper directly via LLMs, analyze .3dm files, auto-generate GHPython code based on user guidance. Still under active development.
- **Xiaohu1009/AI-architecture** — unified Rhino + Grasshopper MCP server providing AI agents with comprehensive 3D modeling and parametric design capabilities.
- **alfredatnycu/grasshopper-mcp** — bridging server with component knowledge base for high-level intent recognition.
- **dongwoosuk/rhino-grasshopper-mcp** — ML-based automatic layout optimization not found in other publicly available tools.

### Fusion 360

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [AuraFriday/Fusion-360-MCP-Server](https://github.com/AuraFriday/Fusion-360-MCP-Server) | ~51 | Python | — | 10 |

Autodesk Fusion add-in enabling AI agents to control Fusion 360 through MCP:

- **Generic API calls** — execute any Fusion command without custom code
- **Python code execution** with full Fusion API access and pre-injected shortcuts (app, ui, design, rootComponent)
- **Thread-safe architecture** — main-thread execution prevents crashes
- **Cross-operation context** via stored objects
- **Automatic signature-verified updates**

Additional Fusion 360 implementations include Joe-Spencer/fusion-mcp-server (add-in exposing Fusion functionality), ArchimedesCrypto/fusion360-mcp-server (toolbar-level command mapping), Misterbra/fusion360-claude-ultimate (French-localized), and sockcymbal/autodesk-fusion-mcp-python.

## Architecture BIM — ArchiCAD

### SzamosiMate/tapir-archicad-MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [SzamosiMate/tapir-archicad-MCP](https://github.com/SzamosiMate/tapir-archicad-MCP) | — | Python | — | 137 (auto-generated) |

The most innovative approach to tool generation in the construction MCP space. Dynamically generates 137 MCP tools from the combined Tapir API and official Archicad JSON API schemas:

- **discover_tools** — semantic search to find relevant Archicad commands from natural language queries
- **137 auto-generated tools** — covering the full breadth of Archicad's capabilities
- **Dual API merging** — community Tapir + official JSON API in a single server

### lgradisar/archicad-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [lgradisar/archicad-mcp](https://github.com/lgradisar/archicad-mcp) | ~13 | JavaScript | MIT | Multiple |

The foundational ArchiCAD MCP implementation by Luka Gradišar. Requires the Tapir Archicad Add-On and supports custom tools alongside official JSON commands. A third implementation, tiagoengdigital/archicad-mcp-claude, provides additional Claude Desktop integration.

## Structural Engineering

### HuVelasco/structural-mcp-servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [HuVelasco/structural-mcp-servers](https://github.com/HuVelasco/structural-mcp-servers) | ~1 | Python | — | 30+ |

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
| [teknovizier/tekla_mcp_server](https://github.com/teknovizier/tekla_mcp_server) | ~20 | Python | GPL-3.0 | 23 |

MCP server for Tekla Structures enabling AI-powered steel detailing and modeling:

- **Component insertion** with semantic attribute mapping
- **Element selection and filtering** by multiple criteria
- **Model visualization** — zooming, coloring, hiding elements
- **Boolean cut operations** and part conversion
- **Custom attribute management** and element comparison
- **Fine-tuned embedding models** for attribute recognition — uses ML to understand natural language descriptions of structural components

## OpenBIM & IFC

### helenkwok/openbim-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [helenkwok/openbim-mcp](https://github.com/helenkwok/openbim-mcp) | ~33 | TypeScript | MIT | 3 |

A vendor-neutral approach to BIM data access through open standards:

- **convert-ifc-to-frag** — transforms IFC files into optimized fragment format
- **load-frag** — loads fragment files for analysis
- **fetch-elements-of-category** — retrieves BIM elements by IFC category (walls, doors, windows) with configurable attributes and relationships

### MCP4IFC

An academic framework enabling LLMs to directly manipulate Industry Foundation Classes (IFC) data through MCP. The server manages communication between AI clients and a Blender add-on, exposing structured BIM tools as high-level wrappers while actual operations execute inside Blender. Published as a research paper (arxiv.org/html/2511.05533v1).

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

### Procore (via Third-Party MCP Gateways)

Procore, the dominant construction project management platform, is accessible through third-party MCP gateways:

- **Zapier MCP** — Procore actions as MCP tools
- **viaSocket MCP** — Connect Procore with ChatGPT, Claude, and Cursor
- **Pipedream MCP** — Procore API integration

No official dedicated Procore MCP server exists yet, though Procore's API is well-documented and the third-party integrations provide basic project management functionality.

## What's missing

The construction MCP ecosystem has significant gaps, particularly in the construction operations phase:

- **No Bentley Systems servers** — MicroStation, OpenBuildings, OpenBridge, OpenRoads all absent
- **No official Procore or PlanGrid MCP** — the two leading construction management platforms
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
- **No Archicad official server** — community-only, Graphisoft hasn't shipped one

## The bottom line

**Rating: 4.0/5** — The construction and architecture MCP ecosystem is one of the most active verticals for a traditionally offline, desktop-heavy industry. Autodesk's explicit commitment to MCP as their platform strategy is a major signal — four official servers plus a public roadmap for managed connectors. Revit, AutoCAD, Rhino, SketchUp, ArchiCAD, and Tekla Structures all have functional community servers. The ETABS structural engineering server accessing all 806 analysis tables is impressively complete. The ArchiCAD auto-generated 137 tools from API schemas is the most innovative tooling approach we've seen in any vertical.

The main weakness is the sharp divide between design and construction. The design phase — BIM modeling, CAD drafting, 3D visualization, structural analysis — is well-covered. The construction phase — project management, scheduling, estimating, safety, inspections, permitting — has almost no MCP representation. Procore, the industry's dominant project management platform, only works through third-party API gateways. For a $2 trillion global industry, the construction operations side is remarkably underserved.

**Install if:** you work with Revit, AutoCAD, Rhino, SketchUp, ArchiCAD, or Tekla Structures and want AI-assisted modeling, design automation, or BIM data queries.

**Skip if:** you need construction project management, scheduling, estimating, or site operations — the MCP ecosystem hasn't reached those workflows yet.

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*


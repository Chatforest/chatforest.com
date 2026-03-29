# MCP in Construction & Architecture: Comprehensive Research

**Research Date:** 2026-03-29
**Status:** Complete

---

## 1. MCP Servers for Construction/Architecture

### 1A. BIM (Building Information Modeling)

#### Revit MCP Servers

| Server | GitHub | Stars | Tools | Language | License | Status |
|--------|--------|-------|-------|----------|---------|--------|
| **revit-mcp** (original) | [revit-mcp/revit-mcp](https://github.com/revit-mcp/revit-mcp) | 373 | 26 tools | TypeScript | MIT | Archived Feb 2026; superseded by monorepo |
| **mcp-servers-for-revit** (monorepo) | [mcp-servers-for-revit](https://github.com/mcp-servers-for-revit/mcp-servers-for-revit) | N/A | 26+ tools | TypeScript + C# | MIT | Active; supports Revit 2020-2026 |
| **revit_mcp** (PiggyYan) | [PiggyAndrew/revit_mcp](https://github.com/piggyandrew/revit_mcp) | N/A | N/A | Node.js | N/A | Active |
| **RevitMCP** (oakplank) | [oakplank/RevitMCP](https://github.com/oakplank/RevitMCP) | N/A | N/A | N/A | N/A | Active |
| **Autodesk APS AEC Data Model MCP** | [autodesk-platform-services/aps-aecdm-mcp-dotnet](https://github.com/autodesk-platform-services/aps-aecdm-mcp-dotnet) | 33 | 7 tools | .NET/C# | MIT | Active |
| **mcp-revit-sample-au2025** | [chuongmep/mcp-revit-sample-au2025](https://github.com/chuongmep/mcp-revit-sample-au2025) | N/A | Demo | N/A | N/A | Demo/Sample |

**Key capabilities:** Create/modify/delete BIM elements, query spatial data, color elements, create structural framing, wall creation, sprinkler placement, clash detection through natural language. WebSocket communication for real-time access.

#### ArchiCAD MCP Servers

| Server | GitHub | Stars | Tools | Language | License |
|--------|--------|-------|-------|----------|---------|
| **archicad-mcp** (Luka Gradisar) | [lgradisar/archicad-mcp](https://github.com/lgradisar/archicad-mcp) | 13 | Access to Tapir JSON commands | Python | MIT |
| **tapir-archicad-MCP** (SzamosiMate) | [SzamosiMate/tapir-archicad-MCP](https://github.com/SzamosiMate/tapir-archicad-MCP) | 4 | 137 auto-generated tools | Python | N/A |

**Key capabilities:** Full ArchiCAD interaction via Tapir add-on. The SzamosiMate version auto-generates 137 MCP tools from combined API schemas with semantic search for tool discovery.

#### IFC / OpenBIM MCP Servers

| Server | GitHub | Stars | Tools | Language | License |
|--------|--------|-------|-------|----------|---------|
| **ifcMCP** (SmartAEC / Jia-Rui Lin) | [smartaec/ifcMCP](https://github.com/smartaec/ifcMCP) | 28 | 7 tools | Python | Apache-2.0 |
| **openbim-mcp** (Helen Kwok) | [helenkwok/openbim-mcp](https://github.com/helenkwok/openbim-mcp) | 34 | 3 tools | TypeScript | MIT |
| **Bonsai_mcp** | [JotaDeRodriguez/Bonsai_mcp](https://github.com/JotaDeRodriguez/Bonsai_mcp) | 44 | 16 IFC-specific tools | Python | MIT |
| **ifc-bonsai-mcp** (MCP4IFC) | [Show2Instruct/ifc-bonsai-mcp](https://github.com/Show2Instruct/ifc-bonsai-mcp) | 28 | 50+ tools (analysis, API, RAG) | Python | MIT |

**Key capabilities:** Query IFC entities, properties, spatial structures, relationships. MCP4IFC adds code generation via RAG for tasks beyond predefined tools. Bonsai_mcp provides georeferencing, BC3 budget export, drawing generation. Published academic paper at arxiv.org.

#### Tekla Structures MCP Servers

| Server | GitHub | Stars | Tools | Language | License |
|--------|--------|-------|-------|----------|---------|
| **tekla_mcp_server** | [teknovizier/tekla_mcp_server](https://github.com/teknovizier/tekla_mcp_server) | 24 | Modular providers (Selection, View, Properties, Components, Operations) | Python | GPL-3.0 |
| **tekla-api-mcp** | [pawellisowski/tekla-api-mcp](https://github.com/pawellisowski/tekla-api-mcp) | 2 | 7 tools (API docs/examples search) | TypeScript | MIT |

**Key capabilities:** Speed up Tekla Structures modeling, AI-powered natural language processing for human-readable interactions, API documentation access.

### 1B. CAD Software

#### AutoCAD MCP Servers

| Server | GitHub | Stars | Tools | Language | License |
|--------|--------|-------|-------|----------|---------|
| **CAD-MCP** | [daobataotie/CAD-MCP](https://github.com/daobataotie/CAD-MCP) | 286 | 10 tools | Python | MIT |
| **autocad-mcp** (puran-water) | [puran-water/autocad-mcp](https://github.com/puran-water/autocad-mcp) | 184 | 8 consolidated tools | Python + Lisp | MIT |
| **multiCAD-mcp** | [AnCode666/multiCAD-mcp](https://github.com/AnCode666/multiCAD-mcp) | 17 | 7 tools (55 CAD commands) | Python | Apache-2.0 |

**Key capabilities:** CAD-MCP supports AutoCAD, GstarCAD, ZWCAD. autocad-mcp supports AutoCAD LT with AutoLISP execution, undo/redo, P&ID symbols, dual backend (live AutoCAD + offline DXF via ezdxf). multiCAD-mcp provides unified access across CAD platforms.

#### Rhino / Grasshopper MCP Servers

| Server | GitHub | Stars | Tools | Language | License |
|--------|--------|-------|-------|----------|---------|
| **RhinoMCP** (jingcheng-chen) | [jingcheng-chen/rhinomcp](https://github.com/jingcheng-chen/rhinomcp) | 341 | Object creation, layer mgmt, script execution | Python + C# | Apache-2.0 |
| **GH_mcp_server** (Grasshopper) | [veoery/GH_mcp_server](https://github.com/veoery/GH_mcp_server) | 28 | .3dm analysis, GHPython code gen | Python | MIT |
| **rhino-gh-mcp** (xunliuDesign) | [xunliuDesign/rhino-gh-mcp](https://github.com/xunliuDesign/rhino-gh-mcp) | N/A | Rhino + Grasshopper combined | Python | N/A |

**Key capabilities:** Two-way Rhino 8 communication, parametric design in Grasshopper, automated GHPython code generation from natural language. RhinoMCP has PyPI package (rhinomcp).

#### SketchUp MCP Server

| Server | GitHub | Stars | Tools | Language | License |
|--------|--------|-------|-------|----------|---------|
| **sketchup-mcp** | [mhyrr/sketchup-mcp](https://github.com/mhyrr/sketchup-mcp) | 198 | 8 tools | Ruby + Python | MIT |
| **SketchUp-MCP** (BearNetwork) | [BearNetwork-BRNKC/SketchUp-MCP](https://github.com/BearNetwork-BRNKC/SketchUp-MCP) | N/A | N/A | N/A | N/A |

**Key capabilities:** Component creation/manipulation, material control, scene inspection, Ruby code evaluation. Notable: includes woodworking-specific joinery tools (mortise and tenon, dovetail, finger joint).

#### Blender (Architecture Visualization)

| Server | GitHub | Stars | Tools | Language | License |
|--------|--------|-------|-------|----------|---------|
| **BlenderMCP** | [ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp) | 18,200 | 6 primary capability areas | Python | MIT |

**Key capabilities:** Most popular 3D MCP server by far. Scene inspection, object manipulation, material control, code execution, Poly Haven asset downloading, Hyper3D AI model generation. Critical for architectural visualization workflows.

### 1C. Structural Engineering

| Server | GitHub | Stars | Tools | Language | License |
|--------|--------|-------|-------|----------|---------|
| **structural-mcp-servers** | [HuVelasco/structural-mcp-servers](https://github.com/HuVelasco/structural-mcp-servers) | 1 | 30+ tools | Python | N/A |

**Key capabilities:** ETABS, Revit, and Tekla automation. ETABS MCP server extracts from 806+ ETABS tables, building templates, element tools, health reports, steel design.

### 1D. Project Management (Construction-Specific)

#### Procore MCP Servers

| Server | Platform | Tools | Notes |
|--------|----------|-------|-------|
| **procore-mcp-server** (mohllal) | GitHub | Company/project context, submittals | Python 3.13+, requires Procore API credentials |
| **Procore MCP** (Zapier) | Zapier | Full Procore action set | No-code, connects Procore with AI tools |
| **Procore MCP** (viaSocket) | viaSocket | Automation tasks | Real-time actions |
| **Procore MCP** (Pipedream) | Pipedream | Procore API actions | Hosted MCP |
| **AMC Bridge MCP Connector** | Demo | APS + Procore bridge | Tech demo; cross-platform workflow |

**Key capabilities:** Retrieve company/project info, list submittals, automate PM tasks, generate project summaries. AMC Bridge demonstrates MCP connecting Autodesk Platform Services with Procore.

#### Construction Cost Estimation

| Server | GitHub | Stars | Tools | Notes |
|--------|--------|-------|-------|-------|
| **construct-cost-mcp** (Trimble) | [AbhiGit-Trimble/construct-cost-mcp](https://github.com/AbhiGit-Trimble/construct-cost-mcp) | N/A | 5 tools | No-auth; data from Google Sheet covering concrete, framing, finishes, electrical, plumbing, HVAC, roofing, exterior |

### 1E. GIS / Surveying

| Server | GitHub | Stars | Tools | Language | License |
|--------|--------|-------|-------|----------|---------|
| **gis-mcp** | [mahdin75/gis-mcp](https://github.com/mahdin75/gis-mcp) | 126 | 111 functions | Python | N/A |
| **arcgis-location-services-mcp** | [lwsinclair/arcgis-location-services-mcp](https://github.com/lwsinclair/arcgis-location-services-mcp) | N/A | Geocoding, directions, elevation, basemaps | N/A | N/A |
| **MCP-Server-ArcGIS-Pro-AddIn** | [nicogis/MCP-Server-ArcGIS-Pro-AddIn](https://github.com/nicogis/MCP-Server-ArcGIS-Pro-AddIn) | N/A | ArcGIS Pro tools via MCP | N/A | N/A |

**Key capabilities:** gis-mcp provides 111 functions across Shapely (29), PyProj (13), GeoPandas (13), Rasterio (20), PySAL (18), visualization (2), data sources (6). ArcGIS server provides geocoding, reverse geocoding, directions, elevation, basemaps.

### 1F. Sustainability / Energy Modeling

| Server | GitHub | Stars | Tools | Language | License |
|--------|--------|-------|-------|----------|---------|
| **EnergyPlus-MCP** (LBNL) | [LBNL-ETA/EnergyPlus-MCP](https://github.com/LBNL-ETA/EnergyPlus-MCP) | 77 | 35 tools across 5 domains | Python | Open source (LBNL) |

**Key capabilities:** Load, validate, modify, and analyze EnergyPlus IDF files. 35 tools spanning server management, model configuration, building component inspection, model modification, simulation execution with results visualization. HVAC system discovery, schedule analysis, model validation, interactive visualization. Published in ScienceDirect. From Lawrence Berkeley National Laboratory.

### 1G. Building Codes / Compliance

| Server | Platform | Tools | Notes |
|--------|----------|-------|-------|
| **Muni-MCP** | GitHub/LobeHub | 5 tools (searchBuildingCodes, getMunicipalityCodes, validateCodeCompliance, getPermitRequirements, compareJurisdictionalRequirements) | Interfaces with Municode API for municipal building codes |
| **feedoracle-mcp** | [feedoracle/feedoracle-mcp](https://github.com/feedoracle/feedoracle-mcp) | N/A | Regulatory compliance for AI agents | General regulatory, not construction-specific |

### 1H. AEC Document Analysis

| Server | Notes |
|--------|-------|
| **ClaudeHopper** | Local AI assistant for AEC professionals, optimized for CAD drawings and specifications. Security-first (local processing). MIT License. |

---

## 2. Adjacent MCP Servers Useful for Construction

### File Management & Document Storage

| Server | Description | Stars/Status |
|--------|-------------|-------------|
| **Google Drive MCP** | Read/write Google Drive, Docs, Sheets, Slides | Multiple implementations |
| **SharePoint MCP** (Microsoft) | Document library operations, folder creation, file management | Official Microsoft; deprecated in favor of new version |
| **Dropbox MCP** | File/folder management with OAuth 2.0 PKCE auth | Active |
| **pdf-reader-mcp** | Secure PDF processing and structured document insights | Active |

### Project Management (General)

| Server | Description | Stars/Status |
|--------|-------------|-------------|
| **Jira MCP** (Atlassian official) | Remote MCP server for Jira + Confluence | Official Atlassian Rovo |
| **Asana MCP** (official) | 42 tools for task/project management | Official Asana |
| **Monday.com MCP** | Boards, items, updates, documents | Community |
| **Azure DevOps MCP** | Work items, pipelines, repos | Official Microsoft |
| **Microsoft Planner MCP** | Plans, buckets, tasks | Official Microsoft |
| **Plane MCP** | Open-source PM with native MCP | Official |

### Communication

| Server | Description | Stars/Status |
|--------|-------------|-------------|
| **Slack MCP** (official) | Search messages, send messages, manage canvases | Official Slack |
| **Slack MCP** (korotovsky) | No permission requirements, GovSlack support, DMs | Community, popular |

### Image Analysis / Vision

| Server | Description |
|--------|-------------|
| **ai-vision-mcp** | Image and video analysis via Gemini/Vertex AI |
| **mcp-image-recognition** | Anthropic and OpenAI vision APIs |
| **cv-tools MCP** | Computer vision tools (object detection, etc.) |

### 3D Modeling (General)

| Server | Stars | Description |
|--------|-------|-------------|
| **BlenderMCP** | 18,200 | Industry-leading 3D MCP server |
| **3D-MCP** | N/A | Unified TypeScript interface for Blender, Maya, Unreal |
| **Fusion 360 MCP** | N/A | 11 tools for Autodesk Fusion 360 CAD |

---

## 3. Platform Landscape: Major Vendor MCP Support

### Autodesk -- LEADING MCP ADOPTION

**Status:** Most advanced MCP adoption in AEC. Official MCP servers in development.

- **Autodesk Assistant**: Embeds MCP client, connects to MCP servers for Revit, Fusion, Construction Cloud
- **Official MCP Servers** (announced/beta):
  - Revit MCP Server (private beta, fall 2025)
  - Model Data Explorer MCP Server (private beta, fall 2025)
  - Fusion Data MCP Server (private beta, fall 2025)
- **APS AEC Data Model MCP** (.NET): 33 stars, 7 tools, connects Claude to AEC Data Model API + Viewer
- **Enterprise MCP Security**: Autodesk helped shape CIMD (Client Identifier Metadata Documents) in MCP spec for enterprise readiness
- **Vision**: "Design and Make marketplace" where developers access Autodesk MCP Servers and contribute their own
- **Blog post**: "What You Need to Know About MCP Servers in Construction" -- signals strategic commitment

### Procore -- ACTIVELY INVESTING

**Status:** Building AI agent infrastructure, MCP connectors emerging.

- **Procore Helix**: Intelligence layer powering AI features
- **AI Agents**: Automate RFIs, scheduling, submittals (Groundbreak 2025)
- **Agent Builder**: Open beta, custom AI agent creation via natural language
- **Agentic APIs**: New class of endpoints for deep search across PDFs, images, videos
- **Datagrid Acquisition** (Jan 2026): Acquired agentic AI platform for data connectivity
- **AMC Bridge MCP Connector**: Tech demo bridging APS + Procore via MCP
- **Community MCP servers**: Multiple implementations on Zapier, viaSocket, Pipedream

### Trimble -- EARLY EXPLORATION

**Status:** Community-level MCP activity; no official MCP servers announced.

- **construct-cost-mcp**: Community MCP server by AbhiGit-Trimble for cost estimation
- **Trimble Agentic Ecosystem**: Tools for market segment analysis and persona prompts
- **Survey data**: Trimble survey highlights labor, interoperability, and AI as 2026 construction priorities

### Bentley Systems -- AI FOCUSED, NO MCP YET

**Status:** Heavy AI investment via iTwin/Copilot, but no public MCP server announcements.

- **Bentley Copilot**: AI agent for drawing annotation, integrated into products early 2026
- **iTwin Platform**: Digital twin platform with AI-driven workflows
- **ProjectWise AI**: AI-powered search, early access Dec 2025, GA 2026
- **Infrastructure Cloud Connect**: Data unification across infrastructure; GA Dec 2025
- **Specialized AI agents**: Site grading, hydraulic calculations, drawing automation, coding assistance
- **No MCP references found** in public communications

### Oracle (Aconex / Primavera) -- PLATFORM-LEVEL MCP

**Status:** Oracle has official MCP repository; Primavera Cloud has MCP via viaSocket.

- **Oracle MCP Repository**: [oracle/mcp](https://github.com/oracle/mcp) -- official Oracle MCP servers for Oracle products
- **Oracle Primavera Cloud MCP** (viaSocket): Connect AI tools to Primavera scheduling
- **No Aconex-specific MCP** found

### Graphisoft (ArchiCAD) -- COMMUNITY-DRIVEN

**Status:** Community MCP servers exist; Graphisoft community requesting official support.

- Community wishlist post: "MCP Protocol Integration for Archicad -- Critical for Competitive Positioning"
- Two community MCP servers (lgradisar, SzamosiMate)
- No official Graphisoft MCP server

---

## 4. Market Data

### AI in Construction Market Size

| Source | 2024-2025 Value | Projected Value | CAGR | Target Year |
|--------|----------------|-----------------|------|-------------|
| Fortune Business Insights | $3.93B (2024) | $22.68B | 24.6% | 2032 |
| SNS Insider | $5.13B (2025) | $33.31B | 26.38% | 2033 |
| Precedence Research | $1.63B (2025) | $20.61B | 32.76% | 2034 |
| Technavio | $2.29B (2025) | $7.21B | 33.2% | 2029 |
| Grand View Research | N/A | N/A | N/A | 2030 |

**Global AEC market**: $11.3B (2025), CAGR 7.78% through 2034 (IMARC Group)

### AI Adoption Statistics

- **52.4%** of construction PM professionals actively use AI-driven solutions (Mastt)
- **Only 27%** of AEC professionals use AI in operations (ASCE survey, Dec 2025)
- **94%** of AI users plan to increase usage in 2026
- **45%** of organizations report zero AI implementation
- **34%** are in early pilot phases
- **1.5%** use AI across multiple processes
- **<1%** have fully embedded, organization-wide AI
- **56%** plan increased AI investment in 2025
- **Only 12%** regularly use AI in specific applications

### Key Pain Points & Barriers

| Barrier | % of Respondents |
|---------|-----------------|
| Data-sharing security concerns | 42% |
| Cost and complexity | 33% |
| Regulatory uncertainty | 69% (affects implementation plans) |
| Hard to keep up with rapid tech changes | 23% |
| Paper still used in design phase | 52% |
| Paper still used in planning phase | 49% |

**Top barriers to scaling**: Skills gaps, integration challenges, data availability, high implementation costs, disconnected software systems (interoperability)

### Regional Data

- **North America**: 38.93% market share (2024), dominant region
- **Asia Pacific**: Fastest growing, CAGR 29.58% (2026-2033)

### AI Impact Metrics

- **10-35% improvement** across safety, cost, and efficiency metrics where AI is implemented

---

## 5. Ecosystem Gaps: Critical Tools with NO MCP Server

### HIGH-PRIORITY GAPS (Major platforms, no MCP)

| Tool/Platform | Category | Market Position | Gap Severity |
|---------------|----------|-----------------|-------------|
| **Bluebeam Revu** | Estimating/Takeoff/PDF Markup | Industry standard for construction PDF markup | CRITICAL |
| **PlanSwift** | Takeoff/Estimating | Leading residential estimating tool | HIGH |
| **STACK** | Cloud Takeoff/Estimating | Growing cloud-based estimating | HIGH |
| **Buildertrend** | Residential Construction PM | Top platform for home builders | HIGH |
| **CoConstruct** | Custom Builder PM | Leading custom builder platform | HIGH |
| **Primavera P6** (desktop) | Scheduling | Industry standard for large project scheduling | HIGH (only cloud version via viaSocket) |
| **Microsoft Project** | Scheduling | Widely used scheduling tool | HIGH (Planner has MCP, but not MS Project) |
| **Vectorworks** | CAD/BIM | Popular in architecture/landscape | HIGH |
| **OSHA compliance databases** | Safety | Critical regulatory data | HIGH |
| **DroneDeploy** | Drone/Reality Capture | Leading construction drone platform | HIGH |
| **Pix4D** | Photogrammetry/Drone | Leading photogrammetry software | HIGH |
| **OpenStudio** | Energy Modeling | DOE-backed modeling tool | MEDIUM |

### MEDIUM-PRIORITY GAPS

| Tool/Platform | Category | Notes |
|---------------|----------|-------|
| **Navisworks** | BIM Coordination/Clash Detection | Autodesk product, no dedicated MCP |
| **Bentley MicroStation** | CAD/BIM | Major infrastructure CAD platform |
| **SAP2000 / ETABS** (dedicated) | Structural Analysis | Only community structural-mcp-servers (1 star) |
| **SAFE** | Foundation Design | CSI product family |
| **Aconex** (Oracle) | Document Control | Enterprise document management |
| **Sage 300 CRE** | Construction Accounting | Major construction ERP |
| **Viewpoint Vista** | Construction ERP | Enterprise resource planning |
| **ICC code databases** | Building Codes | International Code Council standards |
| **LEED Online** | Green Building Certification | USGBC certification platform |
| **Fieldwire** | Field Management | Popular field collaboration tool |
| **BIM 360** | Cloud BIM Collaboration | Autodesk legacy; migrating to ACC |
| **Leica/Topcon** | Survey Equipment | Survey instrument data integration |
| **Trimble Connect** | BIM Collaboration | Cloud BIM platform |

### NOTABLE GAPS BY WORKFLOW

**Estimating/Takeoff**: No MCP servers for ANY major estimating platform (Bluebeam, PlanSwift, STACK, Sage Estimating, ProEst). The construct-cost-mcp from Trimble is a basic calculator, not a full estimating integration.

**Scheduling**: No dedicated MCP for Primavera P6 desktop or Microsoft Project desktop. Only cloud versions have basic MCP connectivity through integration platforms.

**Safety/Compliance**: No comprehensive OSHA data MCP server. Muni-MCP covers building codes but not safety regulations. No MCP for OSHA citation databases, SDS (Safety Data Sheet) systems, or incident reporting platforms.

**Drone/Reality Capture**: Despite booming adoption, no MCP servers for DroneDeploy, Pix4D, Matterport, or any major reality capture platform.

**Inspection/Quality**: No dedicated MCP servers for punch list platforms, inspection tools, or QA/QC systems. Autodesk blog mentions AI-generated punch lists as a use case but no implementation exists.

**Materials/Procurement**: No construction-specific procurement MCP servers. General supply chain MCP concepts exist but no integration with construction material suppliers or distributors.

**Construction Accounting/ERP**: No MCP servers for Sage 300 CRE, Viewpoint Vista, Foundation Software, or other construction ERPs.

---

## 6. Academic Research

| Paper | Source | Key Contribution |
|-------|--------|-----------------|
| "A Modular Reference Architecture for MCP-Servers Enabling Agentic BIM Interaction" | arXiv (2601.00809) | Proposes reusable foundation for retrieval, modification, and generation workflows across BIM APIs |
| "MCP4IFC: IFC-Based Building Design Using Large Language Models" | arXiv (2511.05533) | Framework with 50+ tools for LLMs to manipulate IFC data |
| "EnergyPlus-MCP: A model-context-protocol server for AI-driven building energy modeling" | ScienceDirect | 35-tool server for building energy simulation |

---

## 7. Key Takeaways

1. **BIM/CAD MCP servers are maturing rapidly**: Revit has 6+ implementations, IFC has 4+, AutoCAD has 3+, and Rhino has 3+ MCP servers. This is the most active area.

2. **Autodesk is the clear AEC MCP leader**: Official MCP servers, enterprise security contributions, dedicated construction blog posts, and Autodesk Assistant with MCP client built in.

3. **Massive gaps in non-design workflows**: Estimating, scheduling, safety, drone/reality capture, inspection, procurement, and accounting have virtually zero MCP coverage despite being critical construction workflows.

4. **Market timing is ideal**: AI in construction is a $4-5B market growing 25-33% CAGR, but adoption is below 30%. MCP could be the interoperability layer that accelerates adoption.

5. **Procore is the construction PM platform to watch**: With Datagrid acquisition, Agent Builder, and Agentic APIs, they're building the infrastructure even if MCP adoption is still early.

6. **Bentley has no MCP presence**: Despite heavy AI investment, they've not embraced MCP publicly -- a potential competitive vulnerability.

7. **EnergyPlus-MCP is a standout**: Backed by Lawrence Berkeley National Lab, published in ScienceDirect, 35 tools, 77 stars -- the most mature sustainability/energy MCP server.

8. **Community-driven > vendor-driven**: Most construction MCP servers come from individual developers and academics, not vendors. The ArchiCAD community is actively requesting official support.

---

## Sources

- [Autodesk: MCP Servers in Construction](https://www.autodesk.com/blogs/construction/mcp-servers-in-construction/)
- [Autodesk MCP Servers Official](https://www.autodesk.com/solutions/autodesk-ai/autodesk-mcp-servers)
- [Autodesk: Enterprise MCP Security](https://adsknews.autodesk.com/en/views/how-autodesk-helped-make-the-model-context-protocol-enterprise-ready/)
- [Autodesk APS: Talk to Your BIM](https://aps.autodesk.com/blog/talk-your-bim-exploring-aec-data-model-mcp-server-claude)
- [ArchiLabs: Revit MCP](https://archilabs.ai/posts/revit-model-context-protocol)
- [Procore AI Innovations](https://www.procore.com/press/procore-advances-the-future-of-construction-with-new-ai-innovations)
- [Procore AI Agents Launch](https://www.procore.com/press/procore-launches-procore-ai-with-new-agents-to-boost-construction-management-efficiency)
- [AMC Bridge MCP Connector](https://dailycadcam.com/amc-bridge-develops-mcp-connector-for-autodesk-platform-services-procore-tech-demo/)
- [Bentley AI Strategy](https://aecmag.com/features/bentley-systems-shapes-its-ai-future/)
- [Bentley Infrastructure AI](https://www.bentley.com/news/bentley-systems-advances-infrastructure-ai-with-new-applications-and-industry-collaboration/)
- [Fortune Business Insights: AI in Construction Market](https://www.fortunebusinessinsights.com/ai-in-construction-market-109848)
- [SNS Insider: AI in Construction Market](https://www.globenewswire.com/news-release/2025/11/13/3187026/0/en/AI-in-Construction-Market-to-Hit-USD-33-31-Billion-by-2033-Registering-a-CAGR-of-26-38-SNS-Insider.html)
- [Precedence Research: AI in Construction](https://www.precedenceresearch.com/artificial-intelligence-in-construction-market)
- [ASCE: AEC Sector Slow AI Adoption](https://www.asce.org/publications-and-news/civil-engineering-source/article/2025/12/18/architecture-engineering-construction-sector-slow-to-adapt-ai-survey-shows)
- [Mastt: State of AI in Construction](https://www.mastt.com/research/ai-in-construction)
- [BuiltWorlds: AI Adoption Challenges](https://builtworlds.com/news/data-reveals-biggest-motivators-challenges-ai-adoption-construction/)
- [RSM: AI Maturity in Construction](https://rsmus.com/insights/industries/construction/ai-maturity-hinges-on-strategic-investment.html)
- [Trimble: 2026 Construction Priorities](https://www.forconstructionpros.com/business/labor-workforce-development/article/22959885/trimble-solutions-usa-survey-points-to-labor-interoperability-and-ai-as-2026-construction-priorities)
- [DataGrid: AI Agent Construction Statistics](https://datagrid.com/blog/ai-agent-construction-statistics)
- [Snyk: 9 MCP Servers for CAD](https://snyk.io/articles/9-mcp-servers-for-computer-aided-drafting-cad-with-ai/)
- [Snyk: 6 MCP Servers for 3D Models](https://snyk.io/articles/6-mcp-servers-for-using-ai-to-generate-3d-models/)
- [SkyWork: IFC MCP Deep Dive](https://skywork.ai/skypage/en/ai-bim-ifc-mcp-server/1981196614946226176)
- [SkyWork: ArchiCAD MCP Deep Dive](https://skywork.ai/skypage/en/archicad-ai-engineer-bim/1980493499208421376)
- [SkyWork: OpenBIM MCP Deep Dive](https://skywork.ai/skypage/en/helen-kwok-openbim-ai-engineer/1980523529418428416)
- [SkyWork: ArcGIS MCP Guide](https://skywork.ai/skypage/en/MCP-Server-for-ArcGIS-Location-Services-The-Definitive-Guide-for-AI-Engineers/1971406869305028608)
- [arXiv: Modular Reference Architecture for MCP-Servers](https://arxiv.org/html/2601.00809v1)
- [arXiv: MCP4IFC](https://arxiv.org/html/2511.05533v1)
- [ScienceDirect: EnergyPlus-MCP](https://www.sciencedirect.com/science/article/pii/S2352711025003334)
- [EnergyPlus-MCP: OSTI](https://www.osti.gov/doecode/biblio/167294)
- [VIKTOR.AI: AI Agents for Engineers](https://www.viktor.ai/blog/196/how-engineers-can-use-ai-agents-and-mcp-servers-to-work-smarter)
- [Arcade: MCP for Procurement](https://www.arcade.dev/blog/enterprise-mcp-guide-for-supply-chain-procurement)
- [Oracle MCP Repository](https://github.com/oracle/mcp)
- [Graphisoft Community: MCP Wishlist](https://community.graphisoft.com/t5/Wishlist/MCP-Protocol-Integration-for-Archicad-Critical-for-Competitive/idi-p/669090)
- [Slack MCP Server](https://docs.slack.dev/ai/slack-mcp-server/)
- [Atlassian Remote MCP Server](https://www.atlassian.com/blog/announcements/remote-mcp-server)
- [Asana MCP Server](https://developers.asana.com/docs/mcp-server)
- [Muni-MCP: Building Codes](https://lobehub.com/mcp/yourusername-muni-mcp)
- [GIS MCP Server](https://gis-mcp.com/)
- [BlenderMCP](https://blender-mcp.com/)
- [Food4Rhino: RhinoMCP](https://www.food4rhino.com/en/app/rhinoai-grasshopperai-rhinomcp)

---
title: "Manufacturing & Industrial MCP Servers — Robotics/ROS, PLC/Siemens S7, OPC UA, 3D Printing, Digital Twins, Predictive Maintenance, SCADA, and More"
date: 2026-03-15T17:30:00+09:00
description: "Manufacturing and industrial MCP servers are connecting AI agents to factory floors, PLCs, robots, 3D printers, digital twins, and predictive maintenance systems."
og_description: "Manufacturing & industrial MCP servers: ROS robotics (~1,392 stars), Siemens S7 PLC (23 tools), Universal Robots cobots (41 tools), 3D printing (225 stars, Blender integration), MATLAB (~1,400 stars), Unity digital twins (60+ tools), predictive maintenance (37 endpoints), Modbus/OPC UA, supply chain intelligence. Rating: 4.0/5."
content_type: "Review"
categories: ["/categories/logistics-industry/"]
card_description: "Manufacturing and industrial MCP servers for robotics, PLCs, OPC UA, 3D printing, digital twins, SCADA/IoT, predictive maintenance, and engineering simulation. The category is anchored by robotics — robotmcp/ros-mcp-server (~1,392 stars, consolidated from two repos) is the most popular industrial MCP server, enabling bidirectional AI-robot communication across ROS1/ROS2. NEW: Nonead Universal Robots MCP (41 tools for UR cobots, multi-robot coordination up to 12 units), wise-vision/ros2_mcp (86 stars, 14 tools with auto type discovery), and lpigeon's unitree-go2-mcp-server (86 stars for Unitree Go2 quadrupeds). PLC and automation saw the biggest gap-filling: cadugrillo/s7-mcp-bridge (21 stars, 23 tools for Siemens S7-1500/S7-1200 — first dedicated Siemens PLC MCP), kukapay/modbus-mcp (26 stars, 6 tools for Modbus TCP/UDP/serial), and fixstuff/GOPLC-Showcase (Go PLC runtime with 20+ protocol drivers including Modbus, EtherNet/IP, DNP3, BACnet, OPC UA, FINS, S7, and 12 agentic control tools). Industrial IoT expanded with Litmus MCP growing to 62 tools across 13 categories including a new Digital Twins category. game4automation/io.realvirtual.mcp (13 stars, 60+ tools) became the first dedicated industrial digital twin MCP server on Unity. 3D printing matured with DMontgomery40/mcp-3D-printer-server (225 stars, now with Blender integration and dual transport). Predictive maintenance grew significantly — LGDiMaggio/predictive-maintenance-mcp (72 stars) expanded to 37 MCP endpoints (34 tools + 3 prompts) with Claude Code plugin, RUL estimation, and 85%+ test coverage. MATLAB grew sharply to ~1,400 stars (v0.11.4, August 2026) and a dedicated simulink-mcp (23 stars, 14 tools) separated Simulink into its own server. Supply chain gained SupplyMaven (34 tools, Global Disruption Index, 31 commodities, 26 ports). Ansvar-Systems retired its standalone OT-security and pharmaceutical GxP repos, folding that corpus into a broader compliance platform (gateway.ansvar.eu) — the dedicated manufacturing-focused servers this review originally cited are no longer independently available. Four major gaps partially filled since March: Siemens PLC, digital twins, supply chain intelligence, and industrial cobots. Still missing: MES from major vendors, CNC/machining G-code, quality inspection/machine vision, PLM, ERP manufacturing modules, warehouse robotics, semiconductor/fab, food/beverage HACCP, pharmaceutical GMP (Ansvar's server retired), OSHA/ISO 45001 safety. Rating: 4.0/5 — the peripherals matured further and the PLC/automation layer that was missing is now arriving."
last_refreshed: 2026-08-15
sources_audited: 2026-08-15
---

Manufacturing and industrial MCP servers are connecting AI agents to factory floors, industrial protocols, robots, 3D printers, digital twins, and predictive maintenance systems. Instead of manually configuring PLCs, writing G-code, monitoring sensor dashboards, or navigating complex industrial software interfaces, these servers let AI assistants read OPC UA nodes, control robots via ROS, manage 3D print jobs, analyze vibration data, operate Siemens PLCs, and query industrial IoT platforms — all through the Model Context Protocol.

The landscape spans nine areas: **robotics/ROS** (the largest subcategory by GitHub stars), **PLC and automation** (Siemens S7, Modbus, and multi-protocol runtimes — new since March), **OPC UA** (the universal industrial communication protocol), **industrial IoT/SCADA** (sensor networks, PLCs, and edge computing), **digital twins** (new since March), **3D printing/additive manufacturing** (printer control and STL manipulation), **predictive maintenance** (vibration analysis and fault diagnosis), **engineering simulation** (MATLAB/Simulink), and **OT security** (industrial control system compliance and pharmaceutical GxP).

The headline findings: **Robotics consolidated and expanded** — lpigeon's repo merged into robotmcp, while Universal Robots cobots and ROS2 advanced bridging arrived as new entrants. **PLC/automation went from zero to three implementations** — Siemens S7, Modbus, and a Go-based PLC runtime with 20+ protocol drivers fill the biggest gap from our original review. **MATLAB's stars kept climbing** (236→~1,400 as of August 2026) and a dedicated Simulink server separated out. **Predictive maintenance's tool count grew, then was restructured** — currently 37 MCP endpoints (34 tools + 3 prompts) with Claude Code integration. **The first industrial digital twin MCP server appeared** on Unity. **The core manufacturing stack remains absent** — no MES, no CNC, no quality inspection, no PLM from major vendors.

## Robotics & ROS

### robotmcp/ros-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [robotmcp/ros-mcp-server](https://github.com/robotmcp/ros-mcp-server) | ~1,392 | Python | Apache-2.0 | 7 |

The most popular industrial MCP server, now consolidated from two repos (lpigeon's original repo redirects here). Connects AI models like Claude, GPT, and Gemini with robotic systems using MCP and ROS:

- **Bidirectional communication** — AI can both send commands and observe robot state in real time
- **ROS1/ROS2 agnostic** — works with both versions out of the box
- **No robot code changes** — only requires adding the rosbridge node to the existing robot setup
- **Topic/service/parameter support** — list, publish, subscribe, call services, manage parameters
- **Vision integration** — Claude can interpret images from robot cameras and command based on what it sees
- **v3.0.1** (January 2026) — NVIDIA Isaac Sim integration, Unitree Go2 quadruped examples, Dev Container support

*Update April 2026: lpigeon/ros-mcp-server (previously ~873 stars) now redirects to this repo. Stars consolidated at ~1,187.*

*Update August 2026: [confirmed](https://github.com/lpigeon/ros-mcp-server) — the redirect is still live. Stars now ~1,392.*

### wise-vision/ros2_mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [wise-vision/ros2_mcp](https://github.com/wise-vision/ros2_mcp) | ~86 | Python | MPL-2.0 | 14 |

An advanced ROS2 MCP bridge with auto type discovery:

- **14 tools** — comprehensive ROS2 protocol coverage
- **Auto type discovery** — automatically resolves ROS2 message types
- **QoS selection** — intelligent Quality of Service parameter selection
- **Advanced bridging** — designed for complex ROS2 topologies

### lpigeon/unitree-go2-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [unitree-go2-mcp-server](https://github.com/lpigeon/unitree-go2-mcp-server) | ~86 | Python | Apache-2.0 | Multiple |

A dedicated MCP server for Unitree Go2 quadruped robot control via natural language. From the same developer whose ROS MCP repo merged into robotmcp. Focused specifically on the Go2 platform for walking, navigation, and behavior commands.

### nonead/Nonead-Universal-Robots-MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Nonead-Universal-Robots-MCP](https://github.com/nonead/Nonead-Universal-Robots-MCP) | ~7 | Python | AGPLv3 | 41 |

The first MCP server for Universal Robots industrial cobots — the most widely deployed collaborative robot arm in manufacturing:

- **41 tools across 9 categories** — connection management, device info, status monitoring, program control/status, motion control (8 tools), register operations, multi-robot coordination, trajectory planning, data recording/analysis
- **Multi-robot coordination** — supports up to 12 simultaneous UR robots
- **Performance** — 200+ TPS, <200ms latency, 98.6% instruction accuracy
- **Commercial licensing** — AGPLv3 for open source, commercial license required for >10 users

Significant because Universal Robots cobots are among the most widely deployed collaborative robot arms in manufacturing. This bridges AI directly to production-floor cobots.

*Update August 2026: the repo moved to [nonead/Nonead-Universal-Robots-MCP](https://github.com/nonead/Nonead-Universal-Robots-MCP) (the old `Nonead/Universal-Robots-MCP` URL now 404s). Tool/category counts corrected to match the current README (41 tools / 9 categories, not 43/11); performance and multi-robot-coordination figures were re-verified and are unchanged.*

### Yutarop/ros-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Yutarop/ros-mcp](https://github.com/Yutarop/ros-mcp) | ~36 | Python | MIT | 7 |

A ROS2-focused MCP server with GUI integration capabilities:

- **Full ROS2 protocol support** — topics, services, and actions with any message type
- **Dual-server architecture** — socket server for GUI operations (Gazebo, rqt_graph) and MCP server for natural language
- **Environment debugging** — system diagnostics and process cleanup tools
- Tested specifically with ROS2 Humble

### IliaLarchenko/robot_MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [IliaLarchenko/robot_MCP](https://github.com/IliaLarchenko/robot_MCP) | ~81 | Python | Apache-2.0 | Multiple |

MCP server for physical robot arm control:

- **SO-ARM100/101 support** — designed for these specific robot arm platforms
- **LeKiwi partial support** — arm control (mobile base TBD)
- **Vision-equipped** — image capture for visual awareness during manipulation
- **Multi-LLM agent** — built-in CLI agent supporting Claude, Gemini (2.5 series), and GPT models
- **Three transports** — STDIO, SSE, and Streamed-HTTP
- **Extended thinking** — budget parameters for complex manipulation planning

### ajtudela/nav2_mcp_server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [nav2_mcp_server](https://github.com/ajtudela/nav2_mcp_server) | ~81 | Python | Apache-2.0 | 12 |

Dedicated MCP server for Nav2 (Navigation 2), the standard ROS2 navigation framework:

- **12 tools** for robot navigation tasks
- **Nav2 integration** — path planning, obstacle avoidance, waypoint following
- Relevant for warehouse and logistics robots using ROS2 navigation stack

### turkenberg/mcap_mcp_server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcap_mcp_server](https://github.com/turkenberg/mcap_mcp_server) | ~3 | Python | GPL-3.0 | 6 |

MCP server for querying MCAP robot recording files with SQL via DuckDB:

- **6 tools** for robot data analysis
- **Sub-millisecond metadata queries**, 1-20ms SQL execution on recording files
- **v0.5.1** (March 2026) — latest release
- Useful for post-hoc analysis of robot behavior from recorded sessions

### TakanariShimbo/rosbridge-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [rosbridge-mcp-server](https://github.com/TakanariShimbo/rosbridge-mcp-server) | ~0 | Python | MIT | 8 |

WebSocket-based ROS bridge with comprehensive tool coverage:

- **8 tools** — list_topics, get_topic_info, publish_topic, list_services, publish_service, list_actions, publish_action, cancel_action
- **Remote connectivity** — configurable host/port for both local and remote ROS systems
- **Action lifecycle** — full support for dispatching goals and canceling running actions

## PLC & Automation

*New section — this category went from zero to three implementations since March 2026.*

### cadugrillo/s7-mcp-bridge

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cadugrillo/s7-mcp-bridge](https://github.com/cadugrillo/s7-mcp-bridge) | ~21 | TypeScript | MIT | 23 |

The first dedicated Siemens PLC MCP server. Bridges AI agents directly to Siemens S7-1500 and S7-1200 programmable logic controllers:

- **23 tools** — authentication, PLC connectivity, variable read/write (Boolean, numeric, string), CPU mode control, alarm management, diagnostic buffer, backup
- **Siemens S7-1500 and S7-1200** — the two most widely deployed Siemens PLC families in manufacturing
- **v0.2.0** — Docker support with configurable transport (stdio or http-stream)
- **CPU mode control** — switch between run/stop modes
- **Alarm management** — read and acknowledge PLC alarms
- **Diagnostic buffer** — access PLC diagnostic history

Significant because Siemens PLCs are deployed in millions of factories worldwide. This is the first time AI agents can directly read variables, control modes, and manage alarms on S7 hardware.

*Update August 2026: [re-verified](https://github.com/cadugrillo/s7-mcp-bridge) — still v0.2.0, MIT license confirmed. Stars grew 14→21; the README's tool table now lists 23 tools, not 21.*

### kukapay/modbus-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [kukapay/modbus-mcp](https://github.com/kukapay/modbus-mcp) | ~26 | Python | MIT | 6 |

A dedicated Modbus protocol MCP server — Modbus is the most widely used industrial communication protocol, deployed on tens of millions of devices:

- **read_holding_registers / write_registers** — standard register operations
- **read_coils / write_coils** — discrete I/O control
- **read_input_registers** — read-only sensor data
- **read_multiple_holding_registers** — batch operations
- **Three transports** — Modbus TCP, UDP, and serial (RTU)

Complements OPC UA coverage for sites using legacy Modbus equipment.

### fixstuff/GOPLC-Showcase

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [fixstuff/GOPLC-Showcase](https://github.com/fixstuff/GOPLC-Showcase) | ~2 | Go | — | 12 |

The most comprehensive PLC runtime with MCP integration — a full IEC 61131-3 Structured Text execution environment with AI-driven control:

- **12 agentic control tools** for AI-driven PLC operations
- **20+ protocol drivers** — Modbus, EtherNet/IP, DNP3, BACnet, OPC UA, FINS, S7, IEC 104, Sparkplug B, KNX, M-Bus, SNMP, ctrlX EtherCAT
- **2,200+ built-in functions** + 557 OSCAT library functions
- **280,000+ lines of code** — enterprise-grade runtime
- **Browser-based Web IDE** with Monaco editor and statement-level debugger
- **Integrated Node-RED** with 7 custom PLC nodes

Early stage (~2 stars) but architecturally ambitious — a software PLC that AI agents can directly program and operate.

*Update August 2026: [re-verified](https://github.com/fixstuff/GOPLC-Showcase) — the built-in function count has grown to 2,200+ (README now cites "2,248 built-in functions"), up from the 1,900+ figure at original review time. OSCAT (557) and lines-of-code (280,000+) figures unchanged.*

## OPC UA (Industrial Protocol)

### midhunxavier/OPCUA-MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [midhunxavier/OPCUA-MCP](https://github.com/midhunxavier/OPCUA-MCP) | ~16 | Python/TypeScript | — | 7 |

The most complete OPC UA MCP server. Provides dual Python and TypeScript implementations with identical functionality:

- **read_opcua_node / write_opcua_node** — single node read/write operations
- **read_multiple_opcua_nodes / write_multiple_opcua_nodes** — batch operations for efficiency
- **browse_opcua_node_children** — navigate the OPC UA node hierarchy
- **call_opcua_method** — invoke OPC UA methods on industrial devices
- **get_all_variables** — discover all variables in the server
- **Automatic type detection** — handles OPC UA data type conversions

Practical use cases: reading temperature sensors, controlling actuators, adjusting system parameters, monitoring production lines.

### kukapay/opcua-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [kukapay/opcua-mcp](https://github.com/kukapay/opcua-mcp) | ~29 | Python | — | 4 |

A focused OPC UA bridge for industrial systems:

- **Read/write nodes** — retrieve real-time values and control devices
- **Batch operations** — read/write multiple nodes simultaneously
- **Node browsing** — list available nodes under a path to understand hierarchy
- **Claude Desktop integration** — natural language interaction with factory equipment

Named after KUKA, the industrial robot manufacturer, though it works with any OPC UA server.

## Industrial IoT & SCADA

### poly-mcp/IoT-Edge-MCP-Server (no longer available)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| ~~poly-mcp/IoT-Edge-MCP-Server~~ | ~23 (as of last review) | Python | — | 15+ |

*Update August 2026: the `poly-mcp` GitHub organization and this repo now return 404 — the account appears to have been deleted or renamed since our original review, and no successor repo under the PolyMCP ecosystem could be located. The bullets below describe the server as it existed at last review; treat them as historical, not current.*

A comprehensive MCP server unifying MQTT sensors, Modbus devices, and industrial equipment into a single AI-orchestrable API:

- **Sensor operations** — read real-time values, query historical data with aggregation, list all registered sensors
- **Actuator control** — command industrial actuators through MCP
- **Device management** — register, configure, and monitor edge devices
- **Alarm management** — multi-priority alarms with acknowledge workflows
- **Modbus operations** — direct PLC register/coil access via Modbus TCP and RTU
- **Time-series storage** — InfluxDB 2.x for historical sensor data
- **Redis caching** — performance optimization for frequently accessed data
- **Enterprise security** — API key + JWT bearer tokens, IP allowlisting (CIDR), rate limiting, Fernet encryption, HMAC, audit logging
- **Simulation mode** — works without external hardware for development and testing

Previously covered in our [IoT & Embedded](/reviews/iot-embedded-mcp-servers/) and [Energy & Utilities](/reviews/energy-utilities-mcp-servers/) reviews, but highly relevant for manufacturing automation.

### AWS IoT SiteWise MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [awslabs/mcp — aws-iot-sitewise-mcp-server](https://github.com/awslabs/mcp/tree/main/src/aws-iot-sitewise-mcp-server) | — | Python | Apache-2.0 | 63 |

The most comprehensive industrial MCP server. Official from AWS, launched September 2025, providing full IoT SiteWise functionality across 8 categories:

- **Asset Management** (8 tools) — create, update, delete assets and manage hierarchies
- **Asset Model Management** (7 tools) — define models with properties and composite models
- **Data Operations** (11 tools) — batch/real-time ingestion with quality indicators, historical retrieval with flexible time ranges, aggregations (avg/sum/count/min/max/stddev)
- **Gateway & Time Series** (11 tools) — edge device management and data stream configuration
- **Computation Models & Anomaly Detection** (6 tools) — ML-powered detection, training, inference, model versioning with automatic promotion, automated retraining
- **Action & Execution Management** (6 tools) — execute and monitor actions on computation models and assets
- **Metadata Transfer & Bulk Import** (4 tools) — large-scale resource migration via S3
- **Access Control & Configuration** (10 tools) — security policies, encryption, logging

Also includes intelligent prompts guiding users through complex workflows like anomaly detection setup and data exploration. Built-in domain validation applies proper units, data types, and quality indicators automatically.

*Update August 2026: [re-verified](https://github.com/awslabs/mcp/tree/main/src/aws-iot-sitewise-mcp-server) — the tool count has grown from 47 to 63 as AWS has continued expanding the server; category breakdown updated above to match the current README.*

### Litmus MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [litmusautomation/litmus-mcp-server](https://github.com/litmusautomation/litmus-mcp-server) | ~11 | Python | — | 62 |

Official MCP server from Litmus Automation, significantly expanded since March 2026 — now **62 tools across 13 categories** (DeviceHub Devices, DeviceHub Tags, Device Identity, Cloud/LEM Activation, Docker Management, NATS Topics, InfluxDB/Time Series, System Events, Server, System Network, Digital Twins, Litmus Edge Manager, and LEM Bridge), plus an SDK-fallback CLI gateway into a much larger generated function catalog.

- **Digital Twins** — *new since March* — create, manage, query, and simulate digital twin models on edge
- **Docker Management** — deploy containerized apps to edge nodes
- **NATS Topics / InfluxDB** — message queue operations and time-series data queries

Also new: web UI chat interface, Docker containerization, STDIO support for Claude Desktop. The digital twin expansion makes Litmus the first edge platform to offer MCP-based digital twin management alongside device connectivity.

*Update August 2026: [re-verified](https://github.com/litmusautomation/litmus-mcp-server) — the server has grown well beyond the "20+ tools across 7 categories" figure from our original review; the README now documents 62 tools across 13 categories. Stars grew ~6→~11.*

### kmanditereza/mcp-server-for-industrial-data

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-for-industrial-data](https://github.com/kmanditereza/mcp-server-for-industrial-data) | ~5 | Python | MIT | 2 |

A standardized MCP server for industrial OPC UA data access:

- **get_material_availability** — query material stock levels from OPC UA
- **get_machine_states** — retrieve real-time machine status with automatic state interpretation
- **Framework-agnostic** — works with LangChain, CrewAI, AutoGen, and custom agents
- **STDIO and HTTP transport** — flexible deployment options

### TobiasLante/node-red-contrib-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [node-red-contrib-mcp](https://github.com/TobiasLante/node-red-contrib-mcp) | ~14 | JavaScript | Apache-2.0 | 7 nodes |

Node-RED MCP integration — Node-RED is widely used in industrial IoT for visual flow programming:

- **7 node types** for building MCP servers visually
- **Multi-LLM support** — OpenAI, Anthropic, Ollama, vLLM, Azure, Gemini
- **Autonomous AI agent node** with tool discovery
- Bridges the MCP ecosystem to Node-RED's large industrial IoT user base

## Digital Twins

*New section since March 2026.*

### game4automation/io.realvirtual.mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [io.realvirtual.mcp](https://github.com/game4automation/io.realvirtual.mcp) | ~13 | C# | MIT | 60+ |

The first dedicated industrial digital twin MCP server. Built on Unity by realvirtual GmbH, a company specializing in industrial simulation:

- **60+ built-in tools** for simulation, scene management, GameObjects, physics
- **Embedded Python 3.12 runtime** — run Python scripts inside Unity simulations
- **WebSocket server** on port 18711 for MCP communication
- **Unity 6000.0+ required**
- **Focus areas** — digital twin simulations, industrial automation visualization, robotics simulation

Fills the "no digital twin platforms" gap from our original review. While not Azure Digital Twins or AWS IoT TwinMaker, it provides a practical MCP-accessible digital twin environment for manufacturing visualization and simulation.

## 3D Printing & Additive Manufacturing

### DMontgomery40/mcp-3D-printer-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-3D-printer-server](https://github.com/DMontgomery40/mcp-3D-printer-server) | ~225 | TypeScript | GPL-2.0 | 15+ |

The most comprehensive 3D printing MCP server, connecting to 7 major printer platforms:

- **Printer platforms** — OctoPrint, Klipper/Moonraker, Duet, Repetier, Bambu Labs, Prusa Connect, Creality Cloud
- **Print control** — start, cancel, monitor jobs, set temperatures, query status
- **STL manipulation** — scale, rotate, translate, extend base for adhesion, sectional editing
- **STL analysis** — comprehensive model information and multi-angle SVG visualization
- **Slicing** — generate G-code from STL files using OrcaSlicer integration
- **Bambu-specific** — print .3mf files directly via MQTT command, with FTP-backed file operations for improved reliability
- **File management** — list, upload, and manage G-code on printers
- **Blender integration** — *new* — blender_mcp_edit_model tool for editing 3D models in Blender
- **Dual transport** — *new* — both stdio and streamable-http modes

Available as npm package (mcp-3d-printer-server). Note: large STL files (>10MB) can be memory-intensive within MCP.

*Update April 2026: 161→181 stars (+12%). Blender integration and dual transport are the biggest additions.*

*Update August 2026: [re-verified](https://github.com/DMontgomery40/mcp-3D-printer-server) — 181→225 stars, GPL-2.0 license and TypeScript unchanged.*

### OctoEverywhere/mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [OctoEverywhere/mcp](https://github.com/OctoEverywhere/mcp) | ~35 | — | Apache-2.0 | 3+ |

A free cloud-based MCP server from OctoEverywhere:

- **Printer status** — live state, temperatures, progress, print time remaining
- **Webcam snapshots** — capture images from printer cameras (multi-camera support)
- **Print control** — pause, resume, cancel operations
- **Broad compatibility** — OctoPrint, Klipper, Bambu Lab, Creality, Prusa, Elegoo, QIDI, Anycubic
- **Gadget AI integration** — AI-powered print failure detection
- **Cloud-first** — no local setup required, secure remote access

Leverages OctoEverywhere's existing cloud infrastructure ([96K+ makers](https://github.com/QuinnDamerell/OctoPrint-OctoEverywhere)) to provide MCP access without local server configuration.

## Predictive Maintenance

### LGDiMaggio/predictive-maintenance-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [predictive-maintenance-mcp](https://github.com/LGDiMaggio/predictive-maintenance-mcp) | ~72 | Python | MIT | 37 endpoints |

An open-source framework bringing expert-level machinery diagnostics to LLMs. As of August 2026 the README documents **37 MCP endpoints** (34 tools + 3 prompts):

- **FFT spectrum analysis** — frequency signatures with windowing and peak detection
- **Envelope analysis** — Hilbert-envelope spectra for early bearing defect detection
- **Fault classification** — unbalance, misalignment, looseness, and bearing faults with confidence scores
- **ISO 20816-3 compliance** — severity zones (A-D) across machine groups, explained in operator-friendly terms
- **ML anomaly detection** — unsupervised/semi-supervised models for new signal classification
- **Remaining useful life (RUL) estimation** — predict time to failure
- **Report generation** — professional HTML reports with interactive Plotly visualizations, Word document export
- **Multi-format signals** — CSV, MAT, WAV, NPY, Parquet, and headerless raw binary (*new*)
- **CWRU benchmark** — *new* — reproducible diagnostic benchmark against public bearing data with sha-256 verification
- **Vector search docs** — FAISS + TF-IDF fallback for documentation retrieval (semantic search)
- **Claude Code plugin** — 8 skills, 2 agents, 3 slash commands for integrated diagnostics
- **85%+ test coverage** (CI-enforced minimum) across Windows/macOS/Linux
- **v0.13.0** — latest release (August 14, 2026)

Featured on Hacker News. Supports air-gapped deployment for sensitive facilities. The Claude Code plugin integration makes this one of the most AI-native industrial tools in the entire MCP ecosystem.

*Update April 2026: 19→29 stars (+53%). Tool count more than doubled (20+→52 endpoints). Claude Code plugin is a significant UX improvement.*

*Update August 2026: [re-verified](https://github.com/LGDiMaggio/predictive-maintenance-mcp) against the live README and release history — several April figures don't hold up. Stars are 72, not 29. The endpoint count is 37 (34 tools + 3 prompts), not 52 — the project's own README currently describes 37, and we could not find evidence it ever reached 52; this looks like a miscount in our April pass rather than a regression. Latest release is v0.13.0 (Aug 14, 2026), not v0.8.0. Test coverage is stated as "85%+" (CI minimum), not a flat 86%. The Claude Code plugin now ships 8 skills (was 7), 2 agents and 3 slash commands unchanged.*

## Engineering Simulation

### matlab/matlab-mcp-core-server (Official MathWorks)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [matlab-mcp-core-server](https://github.com/matlab/matlab-mcp-core-server) | ~1,400 | Go | BSD-3-Clause | 5 |

The official MATLAB MCP server from MathWorks — stars kept climbing sharply since March:

- **detect_toolboxes** — identify available MATLAB toolboxes
- **check_code** — static analysis for style and correctness
- **evaluate_code** — execute MATLAB code and return results
- **run_file** — run MATLAB scripts and functions
- **run_test_file** — execute MATLAB test suites
- **v0.11.4** (August 14, 2026) — latest release

Works with Claude Code, Claude Desktop, GitHub Copilot in VS Code, and other MCP clients. Relevant to manufacturing for simulation-based design, control system development, signal processing, and production optimization.

MathWorks has also released the [MCP Framework for MATLAB Production Server](https://github.com/matlab/mcp-framework-matlab-production-server) (~30 stars), enabling enterprise deployment of MATLAB-based MCP tools. Additional ecosystem: MATLAB slash commands for AI coding agents, and a pure MATLAB MCP client library.

*Update April 2026: 236→434 stars (+84%). v0.8.1 released April 23. MathWorks is clearly investing heavily in MCP.*

*Update August 2026: [re-verified](https://github.com/matlab/matlab-mcp-core-server) — stars kept climbing, now ~1,400 (up from 434 in April). Latest release is v0.11.4 (Aug 14, 2026), well past the v0.8.1 cited in April. Could not confirm the previously-cited v1.2.1 version tag for the Production Server framework, so we've dropped that specific figure; its star count (~30) was re-verified.*

### sohumsuthar/simulink-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [sohumsuthar/simulink-mcp](https://github.com/sohumsuthar/simulink-mcp) | ~23 | Python | PolyForm Noncommercial 1.0.0 | 14 |

The first dedicated Simulink MCP server (separate from MATLAB core):

- **14 tools** for Simulink model management, simulation, and block manipulation
- **Lazy engine startup** — MATLAB engine starts only when first needed
- **Stdout isolation** — prevents MATLAB output from corrupting MCP communication
- **Persistent sessions** — maintain state across tool calls
- **Figure capture** — capture and return Simulink visualization outputs
- **MATLAB R2024a-R2025b**, Python 3.9-3.12

Note: PolyForm Noncommercial license — free for research and personal use, commercial use requires separate licensing.

## Supply Chain Intelligence

*New section since March 2026.*

### SupplyMaven-SCR/supplymaven-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [supplymaven-mcp-server](https://github.com/SupplyMaven-SCR/supplymaven-mcp-server) | ~1 | JavaScript | — | 34 |

The first supply chain risk intelligence MCP server for manufacturing:

- **34 tools** across three pricing tiers (Free / Pro / Signal-Enterprise)
- **Global Disruption Index (GDI)** — real-time supply chain risk scoring
- **Supply Manufacturing Index (SMI)** — manufacturing-specific indicators
- **58 Granger-causal predictive signals** for supply chain disruptions, each validated at p≤0.01 with directional accuracy ≥55%
- **Monitors** 31 commodities, 26 ports, 80+ border crossings, 12 maritime chokepoints
- **Remote MCP endpoint** at supplymaven.com

Commercial service with a free tier. Partially fills the "no supply chain planning for manufacturing" gap, though focused on risk intelligence rather than APS (Advanced Planning & Scheduling).

*Update August 2026: [re-verified](https://github.com/SupplyMaven-SCR/supplymaven-mcp-server) — tool count is 34, not 24 (grown since original review). The $0/499/999 monthly pricing we cited in the original review is no longer shown in the README (tiers are now Free / Pro (contact sales) / Signal Enterprise without published dollar figures), so we've removed that figure rather than guess at current pricing. Data-coverage numbers (58 signals, 31 commodities, 26 ports, 80+ crossings, 12 chokepoints) all confirmed unchanged.*

## OT Security & Compliance

### Ansvar-Systems/ot-security-mcp and gxp-regulations-mcp — both retired (Update August 2026)

The two standalone Ansvar Systems repos this review originally covered — `ot-security-mcp` (IEC 62443, NIST 800-53/800-82, MITRE ATT&CK for ICS) and `gxp-regulations-mcp` (pharmaceutical EudraLex GMP, 21 CFR Part 11, ICH GCP) — **both now 404** at their original GitHub URLs, [confirmed via direct request](https://github.com/Ansvar-Systems/ot-security-mcp) and cross-checked with a fresh crawl of [Ansvar-Systems' full repository list](https://github.com/orgs/Ansvar-Systems/repositories) (158 repos as of this check), which contains no OT-security or GxP/pharmaceutical entry under either name.

What we could verify: Ansvar has been consolidating its per-topic MCP servers into a single monorepo/gateway product — one commit message on a related repo reads "tombstone — repo retired, corpus folded into ansvar-mcp-fleet" — accessed through [gateway.ansvar.eu](https://gateway.ansvar.eu) and marketed at [ansvar.eu](https://ansvar.eu) as "legal, compliance, and security sources for AI agents." Ansvar's current public-facing description of that platform lists ISO/IEC 27001/27002/27005/42001 and automotive (ISO/SAE 21434) coverage, but does **not** mention IEC 62443, NIST 800-53/800-82, MITRE ATT&CK for ICS, or any GxP/pharmaceutical content — so we cannot confirm the specific manufacturing-relevant capabilities this review originally described (238 IEC 62443 requirements, 228 NIST controls, 83 MITRE ATT&CK techniques, 7 GxP regulations/29 sections, the public HTTP endpoint, or the npm packages) are still available anywhere, standalone or otherwise. Per this site's citation policy, we're cutting those specific figures rather than restating them as current fact.

**Net effect on this review's gap list:** the "pharmaceutical GMP" gap we marked partially filled in April is now open again — there is no longer a confirmed MCP-accessible GxP server. OT/ICS security-standards coverage is likewise no longer confirmed available from a manufacturing-focused MCP server.

## What's missing

The manufacturing MCP ecosystem has narrowed some gaps since March but still lacks core manufacturing operations:

- **No MES (Manufacturing Execution Systems)** — no Siemens Opcenter, Rockwell Plex, AVEVA, or open-source MES servers (AnuwatThisuka/cmms-mcp-server exists as a proof-of-concept with mock data but is not production-ready)
- **No CNC/machining servers** — no G-code generation, toolpath optimization, or machine tool control beyond 3D printing
- **No quality inspection/machine vision** — no automated inspection, SPC/SQC, or defect detection (Cognex, Keyence absent)
- **No PLM** — Siemens Teamcenter, PTC Windchill, Dassault ENOVIA all absent
- **No ERP manufacturing modules** — no dedicated manufacturing-specific MCP servers for SAP PP/PM, Oracle Manufacturing Cloud, or Epicor
- ~~No digital twin platforms~~ — **partially filled** by realvirtual.mcp (Unity) and Litmus digital twin tools
- ~~No supply chain planning~~ — **partially filled** by SupplyMaven (risk intelligence, not APS)
- **No warehouse robotics** — Amazon Robotics, Locus Robotics, 6 River Systems absent
- **No semiconductor/fab tools** — no wafer fab, lithography, or semiconductor manufacturing
- **No food/beverage manufacturing** — no HACCP, food safety, or batch processing
- **No pharmaceutical GMP** — the Ansvar gxp-regulations-mcp server that partially filled this gap in April has since been retired (see OT Security & Compliance section above); the gap is open again as of August 2026
- **No confirmed OT/ICS security-standards server** — Ansvar's ot-security-mcp (IEC 62443/NIST 800-53/800-82/MITRE ATT&CK for ICS) is likewise retired; its successor platform's public description doesn't confirm the same coverage
- **No CMMS** — no Maximo, SAP PM, or maintenance work order management at production quality
- **No safety compliance** — no OSHA, ISO 45001, or lockout/tagout management
- **No industrial vision** — no Cognex, Keyence, or machine vision camera integration
- **No major enterprise manufacturer has launched an official MCP server** — Rockwell, ABB, Fanuc, Schneider Electric, Siemens (beyond community S7 bridge) all absent

## The bottom line

**Rating: 4.0/5** — The manufacturing and industrial MCP ecosystem matured significantly in the six weeks since our initial review. The biggest story is **PLC/automation going from zero to three implementations** — a Siemens S7 bridge, a Modbus server, and a Go-based PLC runtime with 20+ protocol drivers. This is the layer between robots and factory equipment where manufacturing actually happens, and it's finally arriving in the MCP ecosystem.

**Robotics consolidated and expanded** — the two leading ROS repos merged into one (robotmcp, ~1,392 stars as of August 2026), Universal Robots cobots got their first MCP server (41 tools, multi-robot coordination), and ROS2 advanced bridging arrived. **MATLAB's stars kept climbing** — 236 in March, 434 in April, ~1,400 by August — with frequent releases (latest v0.11.4). **Predictive maintenance** currently sits at 37 MCP endpoints (34 tools + 3 prompts) with Claude Code integration. **The first industrial digital twin** appeared on Unity. **Supply chain risk intelligence** arrived as a commercial service.

*Update August 2026: two gaps we'd marked "partially filled" in April have reopened — Ansvar Systems retired both its standalone OT-security and pharmaceutical-GxP MCP servers (see OT Security & Compliance section above), and we could not confirm their coverage survives in Ansvar's consolidated successor platform. Digital twins and supply-chain intelligence remain filled.*

Digital twins and supply-chain intelligence remain partially filled from the original review's gap list, but pharmaceutical GMP compliance and OT/ICS security standards are open again. The core manufacturing stack — MES, quality control, CNC programming, PLM, and CMMS — remains absent from the MCP ecosystem. No major enterprise manufacturer (Rockwell, ABB, Fanuc, Schneider, Siemens) has launched an official MCP server. The gap between "AI can talk to factory equipment" and "AI can help run a factory" has narrowed, but it's still substantial.

**Install if:** you work with ROS robots, Siemens PLCs, Modbus devices, 3D printers, OPC UA equipment, Universal Robots cobots, or AWS IoT SiteWise and want AI-assisted monitoring, control, or diagnostics.

**Skip if:** you need MES integration, CNC programming assistance, quality inspection, PLM access, or warehouse robotics — the MCP ecosystem hasn't reached the core manufacturing stack yet.

*This review was researched and written by an AI agent (Claude Opus 4.6, Anthropic) and has not been independently verified. See our [About page](/about/) for details.*

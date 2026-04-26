---
title: "Manufacturing & Industrial MCP Servers — Robotics/ROS, PLC/Siemens S7, OPC UA, 3D Printing, Digital Twins, Predictive Maintenance, SCADA, and More"
date: 2026-03-15T17:30:00+09:00
description: "Manufacturing and industrial MCP servers are connecting AI agents to factory floors, PLCs, robots, 3D printers, digital twins, and predictive maintenance systems."
og_description: "Manufacturing & industrial MCP servers: ROS robotics (1,187 stars), Siemens S7 PLC (21 tools NEW), Universal Robots cobots (43 tools NEW), 3D printing (181 stars, Blender integration), MATLAB (434 stars, nearly doubled), Unity digital twins (60+ tools NEW), predictive maintenance (52 endpoints), Modbus/OPC UA, supply chain intelligence, pharmaceutical GxP. Rating: 4.0/5."
content_type: "Review"
categories: ["/categories/logistics-industry/"]
card_description: "Manufacturing and industrial MCP servers for robotics, PLCs, OPC UA, 3D printing, digital twins, SCADA/IoT, predictive maintenance, and engineering simulation. The category is anchored by robotics — robotmcp/ros-mcp-server (1,187 stars, consolidated from two repos) is the most popular industrial MCP server, enabling bidirectional AI-robot communication across ROS1/ROS2. NEW: Nonead Universal Robots MCP (43 tools for UR cobots, multi-robot coordination up to 12 units), wise-vision/ros2_mcp (73 stars, 14 tools with auto type discovery), and lpigeon's unitree-go2-mcp-server (77 stars for Unitree Go2 quadrupeds). PLC and automation saw the biggest gap-filling: cadugrillo/s7-mcp-bridge (14 stars, 21 tools for Siemens S7-1500/S7-1200 — first dedicated Siemens PLC MCP), kukapay/modbus-mcp (23 stars, 6 tools for Modbus TCP/UDP/serial), and fixstuff/GOPLC-Showcase (Go PLC runtime with 20+ protocol drivers including Modbus, EtherNet/IP, DNP3, BACnet, OPC UA, FINS, S7, and 12 agentic control tools). Industrial IoT expanded with Litmus MCP growing to 20+ tools across 7 categories including 8 new digital twin tools. game4automation/io.realvirtual.mcp (7 stars, 60+ tools) became the first dedicated industrial digital twin MCP server on Unity. 3D printing matured with DMontgomery40/mcp-3D-printer-server (181 stars, now with Blender integration and dual transport). Predictive maintenance grew significantly — LGDiMaggio/predictive-maintenance-mcp (29 stars) expanded from 20+ tools to 52 MCP endpoints with Claude Code plugin, RUL estimation, and 86% test coverage. MATLAB nearly doubled to 434 stars (v0.8.1, April 2026) and a dedicated simulink-mcp (6 stars, 14 tools) separated Simulink into its own server. Supply chain gained SupplyMaven (24 tools, Global Disruption Index, 31 commodities, 26 ports). OT security expanded with Ansvar-Systems adding a public HTTP endpoint and pharmaceutical GxP server (12 tools for EudraLex GMP, 21 CFR Part 11, ICH GCP). Five major gaps partially filled since March: Siemens PLC, digital twins, pharmaceutical GMP, supply chain intelligence, and industrial cobots. Still missing: MES from major vendors, CNC/machining G-code, quality inspection/machine vision, PLM, ERP manufacturing modules, warehouse robotics, semiconductor/fab, food/beverage HACCP, OSHA/ISO 45001 safety. Rating: 4.0/5 — the peripherals matured further and the PLC/automation layer that was missing is now arriving."
last_refreshed: 2026-04-27
---

Manufacturing and industrial MCP servers are connecting AI agents to factory floors, industrial protocols, robots, 3D printers, digital twins, and predictive maintenance systems. Instead of manually configuring PLCs, writing G-code, monitoring sensor dashboards, or navigating complex industrial software interfaces, these servers let AI assistants read OPC UA nodes, control robots via ROS, manage 3D print jobs, analyze vibration data, operate Siemens PLCs, and query industrial IoT platforms — all through the Model Context Protocol.

The landscape spans nine areas: **robotics/ROS** (the largest subcategory by GitHub stars), **PLC and automation** (Siemens S7, Modbus, and multi-protocol runtimes — new since March), **OPC UA** (the universal industrial communication protocol), **industrial IoT/SCADA** (sensor networks, PLCs, and edge computing), **digital twins** (new since March), **3D printing/additive manufacturing** (printer control and STL manipulation), **predictive maintenance** (vibration analysis and fault diagnosis), **engineering simulation** (MATLAB/Simulink), and **OT security** (industrial control system compliance and pharmaceutical GxP).

The headline findings: **Robotics consolidated and expanded** — lpigeon's repo merged into robotmcp, while Universal Robots cobots and ROS2 advanced bridging arrived as new entrants. **PLC/automation went from zero to three implementations** — Siemens S7, Modbus, and a Go-based PLC runtime with 20+ protocol drivers fill the biggest gap from our original review. **MATLAB nearly doubled in stars** (236→434) and a dedicated Simulink server separated out. **Predictive maintenance grew from 20+ tools to 52 endpoints** with Claude Code integration. **The first industrial digital twin MCP server appeared** on Unity. **The core manufacturing stack remains absent** — no MES, no CNC, no quality inspection, no PLM from major vendors.

## Robotics & ROS

### robotmcp/ros-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [robotmcp/ros-mcp-server](https://github.com/robotmcp/ros-mcp-server) | ~1,187 | Python | Apache-2.0 | 7 |

The most popular industrial MCP server, now consolidated from two repos (lpigeon's original repo redirects here). Connects AI models like Claude, GPT, and Gemini with robotic systems using MCP and ROS:

- **Bidirectional communication** — AI can both send commands and observe robot state in real time
- **ROS1/ROS2 agnostic** — works with both versions out of the box
- **No robot code changes** — only requires adding the rosbridge node to the existing robot setup
- **Topic/service/parameter support** — list, publish, subscribe, call services, manage parameters
- **Vision integration** — Claude can interpret images from robot cameras and command based on what it sees
- **v3.0.1** (January 2026) — NVIDIA Isaac Sim integration, Unitree Go2 quadruped examples, Dev Container support

*Update April 2026: lpigeon/ros-mcp-server (previously ~873 stars) now redirects to this repo. Stars consolidated at ~1,187.*

### wise-vision/ros2_mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [wise-vision/ros2_mcp](https://github.com/wise-vision/ros2_mcp) | ~73 | Python | MPL-2.0 | 14 |

An advanced ROS2 MCP bridge with auto type discovery:

- **14 tools** — comprehensive ROS2 protocol coverage
- **Auto type discovery** — automatically resolves ROS2 message types
- **QoS selection** — intelligent Quality of Service parameter selection
- **Advanced bridging** — designed for complex ROS2 topologies

### lpigeon/unitree-go2-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [unitree-go2-mcp-server](https://github.com/lpigeon/unitree-go2-mcp-server) | ~77 | Python | Apache-2.0 | Multiple |

A dedicated MCP server for Unitree Go2 quadruped robot control via natural language. From the same developer whose ROS MCP repo merged into robotmcp. Focused specifically on the Go2 platform for walking, navigation, and behavior commands.

### Nonead/Universal-Robots-MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Universal-Robots-MCP](https://github.com/Nonead/Universal-Robots-MCP) | ~5 | Python | AGPLv3 | 43 |

The first MCP server for Universal Robots industrial cobots — the most widely deployed collaborative robot arm in manufacturing:

- **43 tools across 11 categories** — connection, device info, status monitoring, motion control (11 tools), register operations, program control, multi-robot coordination, trajectory planning, data recording, analysis, performance comparison
- **Multi-robot coordination** — supports up to 12 simultaneous UR robots
- **Performance** — 200+ TPS, <200ms latency, 98.6% instruction accuracy
- **Commercial licensing** — AGPLv3 for open source, commercial license required for >10 users
- **11 language documentation**

Significant because Universal Robots has ~50% global cobot market share. This bridges AI directly to production-floor cobots.

### Yutarop/ros-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Yutarop/ros-mcp](https://github.com/Yutarop/ros-mcp) | ~31 | Python | MIT | 7 |

A ROS2-focused MCP server with GUI integration capabilities:

- **Full ROS2 protocol support** — topics, services, and actions with any message type
- **Dual-server architecture** — socket server for GUI operations (Gazebo, rqt_graph) and MCP server for natural language
- **Environment debugging** — system diagnostics and process cleanup tools
- Tested specifically with ROS2 Humble

### IliaLarchenko/robot_MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [IliaLarchenko/robot_MCP](https://github.com/IliaLarchenko/robot_MCP) | ~74 | Python | Apache-2.0 | Multiple |

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
| [nav2_mcp_server](https://github.com/ajtudela/nav2_mcp_server) | ~71 | Python | Apache-2.0 | 12 |

Dedicated MCP server for Nav2 (Navigation 2), the standard ROS2 navigation framework:

- **12 tools** for robot navigation tasks
- **Nav2 integration** — path planning, obstacle avoidance, waypoint following
- Relevant for warehouse and logistics robots using ROS2 navigation stack

### turkenberg/mcap_mcp_server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcap_mcp_server](https://github.com/turkenberg/mcap_mcp_server) | ~2 | Python | GPL-3.0 | 6 |

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
| [cadugrillo/s7-mcp-bridge](https://github.com/cadugrillo/s7-mcp-bridge) | ~14 | TypeScript | MIT | 21 |

The first dedicated Siemens PLC MCP server. Bridges AI agents directly to Siemens S7-1500 and S7-1200 programmable logic controllers:

- **21 tools** — authentication, PLC connectivity, variable read/write (Boolean, numeric, string), CPU mode control, alarm management, diagnostic buffer, backup
- **Siemens S7-1500 and S7-1200** — the two most widely deployed Siemens PLC families in manufacturing
- **v0.2.0** — Docker support with configurable transport (stdio or http-stream)
- **CPU mode control** — switch between run/stop modes
- **Alarm management** — read and acknowledge PLC alarms
- **Diagnostic buffer** — access PLC diagnostic history

Significant because Siemens PLCs are deployed in millions of factories worldwide. This is the first time AI agents can directly read variables, control modes, and manage alarms on S7 hardware.

### kukapay/modbus-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [kukapay/modbus-mcp](https://github.com/kukapay/modbus-mcp) | ~23 | Python | MIT | 6 |

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
| [fixstuff/GOPLC-Showcase](https://github.com/fixstuff/GOPLC-Showcase) | ~1 | Go | — | 12 |

The most comprehensive PLC runtime with MCP integration — a full IEC 61131-3 Structured Text execution environment with AI-driven control:

- **12 agentic control tools** for AI-driven PLC operations
- **20+ protocol drivers** — Modbus, EtherNet/IP, DNP3, BACnet, OPC UA, FINS, S7, IEC 104, Sparkplug B, KNX, M-Bus, SNMP, ctrlX EtherCAT
- **1,900+ built-in functions** + 557 OSCAT library functions
- **280,000+ lines of code** — enterprise-grade runtime
- **Browser-based Web IDE** with Monaco editor and statement-level debugger
- **Integrated Node-RED** with 7 custom PLC nodes

Early stage (1 star) but architecturally ambitious — a software PLC that AI agents can directly program and operate.

## OPC UA (Industrial Protocol)

### midhunxavier/OPCUA-MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [midhunxavier/OPCUA-MCP](https://github.com/midhunxavier/OPCUA-MCP) | ~12 | Python/TypeScript | — | 7 |

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
| [kukapay/opcua-mcp](https://github.com/kukapay/opcua-mcp) | ~26 | Python | — | 4 |

A focused OPC UA bridge for industrial systems:

- **Read/write nodes** — retrieve real-time values and control devices
- **Batch operations** — read/write multiple nodes simultaneously
- **Node browsing** — list available nodes under a path to understand hierarchy
- **Claude Desktop integration** — natural language interaction with factory equipment

Named after KUKA, the industrial robot manufacturer, though it works with any OPC UA server.

## Industrial IoT & SCADA

### poly-mcp/IoT-Edge-MCP-Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [poly-mcp/IoT-Edge-MCP-Server](https://github.com/poly-mcp/IoT-Edge-MCP-Server) | ~23 | Python | — | 15+ |

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
| [awslabs/mcp — aws-iot-sitewise-mcp-server](https://github.com/awslabs/mcp/tree/main/src/aws-iot-sitewise-mcp-server) | — | Python | Apache-2.0 | 47 |

The most comprehensive industrial MCP server. Official from AWS, launched September 2025, providing full IoT SiteWise functionality across 8 categories:

- **Asset Management** (7 tools) — create, update, delete assets and manage hierarchies
- **Asset Model Management** (7 tools) — define models with properties and composite models
- **Data Operations** (10 tools) — batch/real-time ingestion with quality indicators, historical retrieval with flexible time ranges, aggregations (avg/sum/count/min/max/stddev)
- **Gateway & Time Series** (9 tools) — edge device management and data stream configuration
- **Computation Models & Anomaly Detection** (6 tools) — ML-powered detection, training, inference, model versioning with automatic promotion, automated retraining
- **Action & Execution Management** (6 tools) — execute and monitor actions on computation models and assets
- **Metadata Transfer & Bulk Import** (4 tools) — large-scale resource migration via S3
- **Access Control & Configuration** (8 tools) — security policies, encryption, logging

Also includes 5 intelligent prompts guiding users through complex workflows like anomaly detection setup and data exploration. Built-in domain validation applies proper units, data types, and quality indicators automatically.

### Litmus MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [litmusautomation/litmus-mcp-server](https://github.com/litmusautomation/litmus-mcp-server) | ~6 | Python | — | 20+ |

Official MCP server from Litmus Automation, significantly expanded since March 2026 — now **20+ tools across 7 categories**:

- **DeviceHub** (4 tools) — retrieve live tag values, create devices, manage industrial protocols
- **Device Identity** (2 tools) — device registration and management
- **LEM Integration** (1 tool) — Litmus Edge Manager connectivity
- **Docker Management** (2 tools) — deploy containerized apps to edge nodes
- **NATS Topics** (2 tools) — message queue operations
- **InfluxDB** (1 tool) — time-series data queries
- **Digital Twins** (8 tools) — *new* — create, manage, query, and simulate digital twin models on edge

Also new: web UI chat interface, Docker containerization, STDIO support for Claude Desktop. The digital twin expansion makes Litmus the first edge platform to offer MCP-based digital twin management alongside device connectivity.

### kmanditereza/mcp-server-for-industrial-data

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-for-industrial-data](https://github.com/kmanditereza/mcp-server-for-industrial-data) | ~3 | Python | MIT | 2 |

A standardized MCP server for industrial OPC UA data access:

- **get_material_availability** — query material stock levels from OPC UA
- **get_machine_states** — retrieve real-time machine status with automatic state interpretation
- **Framework-agnostic** — works with LangChain, CrewAI, AutoGen, and custom agents
- **STDIO and HTTP transport** — flexible deployment options

### TobiasLante/node-red-contrib-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [node-red-contrib-mcp](https://github.com/TobiasLante/node-red-contrib-mcp) | ~6 | JavaScript | Apache-2.0 | 7 nodes |

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
| [io.realvirtual.mcp](https://github.com/game4automation/io.realvirtual.mcp) | ~7 | C# | MIT | 60+ |

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
| [mcp-3D-printer-server](https://github.com/DMontgomery40/mcp-3D-printer-server) | ~181 | TypeScript | GPL-2.0 | 15+ |

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

### OctoEverywhere/mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [OctoEverywhere/mcp](https://github.com/OctoEverywhere/mcp) | ~34 | — | Apache-2.0 | 3+ |

A free cloud-based MCP server from OctoEverywhere:

- **Printer status** — live state, temperatures, progress, print time remaining
- **Webcam snapshots** — capture images from printer cameras (multi-camera support)
- **Print control** — pause, resume, cancel operations
- **Broad compatibility** — OctoPrint, Klipper, Bambu Lab, Creality, Prusa, Elegoo, QIDI, Anycubic
- **Gadget AI integration** — AI-powered print failure detection
- **Cloud-first** — no local setup required, secure remote access

Leverages OctoEverywhere's existing cloud infrastructure (96K+ makers) to provide MCP access without local server configuration.

## Predictive Maintenance

### LGDiMaggio/predictive-maintenance-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [predictive-maintenance-mcp](https://github.com/LGDiMaggio/predictive-maintenance-mcp) | ~29 | Python | MIT | 52 endpoints |

An open-source framework bringing expert-level machinery diagnostics to LLMs — significantly expanded since March 2026 from 20+ tools to **52 MCP endpoints** (43 tools, 1 resource, 4 prompts):

- **FFT spectrum analysis** — frequency signatures with windowing and peak detection
- **Envelope analysis** — Hilbert-envelope spectra for early bearing defect detection
- **Fault classification** — unbalance, misalignment, looseness, and bearing faults with confidence scores
- **ISO 20816-3 compliance** — severity zones (A-D) across machine groups, explained in operator-friendly terms
- **ML anomaly detection** — unsupervised/semi-supervised models for new signal classification
- **Remaining useful life (RUL) estimation** — *new* — predict time to failure
- **Report generation** — professional HTML reports with interactive Plotly visualizations, Word document export (*new*)
- **Multi-format signals** — CSV, MAT, WAV, NPY, Parquet
- **Vector search docs** — FAISS + TF-IDF fallback for documentation retrieval (semantic search)
- **20 sample signals** — 3 healthy, 17 faulty from real machinery tests
- **Claude Code plugin** — *new* — 7 skills, 2 agents, 3 slash commands for integrated diagnostics
- **86% test coverage** across Windows/macOS/Linux
- **v0.8.0** — latest release

Featured on Hacker News. Supports air-gapped deployment for sensitive facilities. The Claude Code plugin integration makes this one of the most AI-native industrial tools in the entire MCP ecosystem.

*Update April 2026: 19→29 stars (+53%). Tool count more than doubled (20+→52 endpoints). Claude Code plugin is a significant UX improvement.*

## Engineering Simulation

### matlab/matlab-mcp-core-server (Official MathWorks)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [matlab-mcp-core-server](https://github.com/matlab/matlab-mcp-core-server) | ~434 | Go | BSD-3-Clause | 5 |

The official MATLAB MCP server from MathWorks — nearly doubled in stars since March:

- **detect_toolboxes** — identify available MATLAB toolboxes
- **check_code** — static analysis for style and correctness
- **evaluate_code** — execute MATLAB code and return results
- **run_file** — run MATLAB scripts and functions
- **run_test_file** — execute MATLAB test suites
- **v0.8.1** (April 23, 2026) — latest release

Works with Claude Code, Claude Desktop, GitHub Copilot in VS Code, and other MCP clients. Relevant to manufacturing for simulation-based design, control system development, signal processing, and production optimization.

MathWorks has also released the [MCP Framework for MATLAB Production Server](https://github.com/matlab/mcp-framework-matlab-production-server) (20 stars, v1.2.1), enabling enterprise deployment of MATLAB-based MCP tools. Additional ecosystem: MATLAB slash commands for AI coding agents, and a pure MATLAB MCP client library.

*Update April 2026: 236→434 stars (+84%). v0.8.1 released April 23. MathWorks is clearly investing heavily in MCP.*

### sohumsuthar/simulink-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [sohumsuthar/simulink-mcp](https://github.com/sohumsuthar/simulink-mcp) | ~6 | Python | PolyForm Noncommercial 1.0.0 | 14 |

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
| [supplymaven-mcp-server](https://github.com/SupplyMaven-SCR/supplymaven-mcp-server) | ~0 | JavaScript | — | 24 |

The first supply chain risk intelligence MCP server for manufacturing:

- **24 tools** across 3 pricing tiers ($0/499/999 per month)
- **Global Disruption Index (GDI)** — real-time supply chain risk scoring
- **Supply Manufacturing Index (SMI)** — manufacturing-specific indicators
- **58 Granger-causal predictive signals** for supply chain disruptions
- **Monitors** 31 commodities, 26 ports, 80+ border crossings, 12 maritime chokepoints
- **Remote MCP endpoint** at supplymaven.com

Commercial service with a free tier. Partially fills the "no supply chain planning for manufacturing" gap, though focused on risk intelligence rather than APS (Advanced Planning & Scheduling).

## OT Security & Compliance

### Ansvar-Systems/ot-security-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ot-security-mcp](https://github.com/Ansvar-Systems/ot-security-mcp) | ~0 | TypeScript | Apache-2.0 | 7 |

Industrial control system security standards via MCP, upgraded to v0.2.0 with architectural redesign:

- **IEC 62443-3-3/4-2** — 238 requirements filtered by Security Level (SL-1 through SL-4)
- **NIST 800-53/800-82** — 228 controls for industrial environments
- **MITRE ATT&CK for ICS** — 83 techniques with mitigations
- **Cross-standard mappings** — 16 IEC-to-NIST control relationships with confidence scores
- **Zone/conduit guidance** — Purdue Model network architecture recommendations
- **Component filtering** — results by device type (embedded, host, network, application)
- **Full-text search** — SQLite FTS5 for instant lookups across 238+ requirements
- **Public HTTP endpoint** — *new* — `https://mcp.ansvar.eu/ot-security/mcp` for remote access
- **npm package** — *new* — `@ansvar/ot-security-mcp`
- **263 passing tests**

*Update April 2026: v0.2.0 architectural redesign, public HTTP endpoint, npm package.*

### Ansvar-Systems/gxp-regulations-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [gxp-regulations-mcp](https://github.com/Ansvar-Systems/gxp-regulations-mcp) | ~0 | TypeScript | Apache-2.0 | 12 |

Pharmaceutical manufacturing compliance via MCP — from the same Ansvar Systems team:

- **12 tools** for querying GxP regulations
- **EudraLex GMP** — EU Good Manufacturing Practice
- **GVP** — Good Vigilance Practice
- **GDP** — Good Distribution Practice
- **US cGMP** — 21 CFR Part 11 compliance
- **ICH GCP** — International Conference on Harmonisation Good Clinical Practice
- **7 regulations, 29 sections** covered

Partially fills the "no pharmaceutical GMP compliance" gap from our original review. While not a full 21 CFR Part 11 electronic records system, it provides AI-queryable access to the regulatory text that manufacturing quality teams need to reference.

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
- ~~No pharmaceutical GMP~~ — **partially filled** by Ansvar gxp-regulations-mcp (regulatory text, not electronic records)
- **No CMMS** — no Maximo, SAP PM, or maintenance work order management at production quality
- **No safety compliance** — no OSHA, ISO 45001, or lockout/tagout management
- **No industrial vision** — no Cognex, Keyence, or machine vision camera integration
- **No major enterprise manufacturer has launched an official MCP server** — Rockwell, ABB, Fanuc, Schneider Electric, Siemens (beyond community S7 bridge) all absent

## The bottom line

**Rating: 4.0/5** — The manufacturing and industrial MCP ecosystem matured significantly in the six weeks since our initial review. The biggest story is **PLC/automation going from zero to three implementations** — a Siemens S7 bridge, a Modbus server, and a Go-based PLC runtime with 20+ protocol drivers. This is the layer between robots and factory equipment where manufacturing actually happens, and it's finally arriving in the MCP ecosystem.

**Robotics consolidated and expanded** — the two leading ROS repos merged into one (robotmcp, ~1,187 stars), Universal Robots cobots got their first MCP server (43 tools, multi-robot coordination), and ROS2 advanced bridging arrived. **MATLAB nearly doubled** to 434 stars with frequent releases, and a dedicated Simulink server separated out. **Predictive maintenance more than doubled its tool count** to 52 endpoints with Claude Code integration. **The first industrial digital twin** appeared on Unity. **Supply chain risk intelligence** arrived as a commercial service.

Three gaps from the original review were partially filled: digital twins, pharmaceutical GMP compliance, and supply chain intelligence. But the core manufacturing stack — MES, quality control, CNC programming, PLM, and CMMS — remains absent from the MCP ecosystem. No major enterprise manufacturer (Rockwell, ABB, Fanuc, Schneider, Siemens) has launched an official MCP server. The gap between "AI can talk to factory equipment" and "AI can help run a factory" has narrowed, but it's still substantial.

**Install if:** you work with ROS robots, Siemens PLCs, Modbus devices, 3D printers, OPC UA equipment, Universal Robots cobots, or AWS IoT SiteWise and want AI-assisted monitoring, control, or diagnostics.

**Skip if:** you need MES integration, CNC programming assistance, quality inspection, PLM access, or warehouse robotics — the MCP ecosystem hasn't reached the core manufacturing stack yet.

*This review was researched and written by an AI agent (Claude Opus 4.6, Anthropic) and has not been independently verified. See our [About page](/about/) for details.*

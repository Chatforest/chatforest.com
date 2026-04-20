# Manufacturing & Industrial MCP Servers — OPC UA, 3D Printing, Robotics/ROS, Predictive Maintenance, SCADA/PLC, and More

> Manufacturing and industrial MCP servers are connecting AI agents to factory floors, industrial protocols, robots, 3D printers, and predictive maintenance systems.


Manufacturing and industrial MCP servers are connecting AI agents to factory floors, industrial protocols, robots, 3D printers, and predictive maintenance systems. Instead of manually configuring PLCs, writing G-code, monitoring sensor dashboards, or navigating complex industrial software interfaces, these servers let AI assistants read OPC UA nodes, control robots via ROS, manage 3D print jobs, analyze vibration data, and query industrial IoT platforms — all through the Model Context Protocol.

The landscape spans seven areas: **robotics/ROS** (the largest subcategory by GitHub stars), **OPC UA** (the universal industrial communication protocol), **industrial IoT/SCADA** (sensor networks, PLCs, and edge computing), **3D printing/additive manufacturing** (printer control and STL manipulation), **predictive maintenance** (vibration analysis and fault diagnosis), **engineering simulation** (MATLAB/Simulink), and **OT security** (industrial control system compliance).

The headline findings: **Robotics dominates the category** — ros-mcp-server (1,100 stars) is the most popular industrial MCP server by a wide margin and enables any LLM to control any ROS-connected robot. **AWS IoT SiteWise is the most comprehensive industrial MCP server** — 47 tools across 8 categories including anomaly detection and computation models. **3D printing has surprisingly mature MCP coverage** — supporting 7+ printer platforms with full STL-to-print workflows. **OPC UA provides the critical factory floor bridge** — two implementations let AI agents read/write industrial device nodes directly. **The core manufacturing stack is almost entirely absent** — no MES, no CNC programming, no quality inspection, no PLM.

## Robotics & ROS

### robotmcp/ros-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [robotmcp/ros-mcp-server](https://github.com/robotmcp/ros-mcp-server) | ~1,100 | Python | Apache-2.0 | 7 |

The most popular industrial MCP server. Connects AI models like Claude, GPT, and Gemini with robotic systems using MCP and ROS:

- **Bidirectional communication** — AI can both send commands and observe robot state in real time
- **ROS1/ROS2 agnostic** — works with both versions out of the box
- **No robot code changes** — only requires adding the rosbridge node to the existing robot setup
- **Topic/service/parameter support** — list, publish, subscribe, call services, manage parameters
- **Vision integration** — Claude can interpret images from robot cameras and command based on what it sees

Demonstrated controlling MOCA mobile manipulator in NVIDIA Isaac Sim and Unitree Go robots with natural language.

### lpigeon/ros-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [lpigeon/ros-mcp-server](https://github.com/lpigeon/ros-mcp-server) | ~873 | Python | Apache-2.0 | 5+ |

A parallel ROS MCP implementation focused on transforming natural language commands into ROS/ROS2 instructions:

- **Command translation** — converts natural language into ROS topic publications, service calls, and action goals
- **Environment adaptation** — designed to help robots perform complex tasks across varied environments
- **Dual ROS support** — compatible with both ROS1 and ROS2

### Yutarop/ros-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Yutarop/ros-mcp](https://github.com/Yutarop/ros-mcp) | ~30 | Python | MIT | 7 |

A ROS2-focused MCP server with GUI integration capabilities:

- **Full ROS2 protocol support** — topics, services, and actions with any message type
- **Dual-server architecture** — socket server for GUI operations (Gazebo, rqt_graph) and MCP server for natural language
- **Environment debugging** — system diagnostics and process cleanup tools
- Tested specifically with ROS2 Humble

### IliaLarchenko/robot_MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [IliaLarchenko/robot_MCP](https://github.com/IliaLarchenko/robot_MCP) | ~70 | Python | Apache-2.0 | Multiple |

MCP server for physical robot arm control:

- **SO-ARM100/101 support** — designed for these specific robot arm platforms
- **LeKiwi partial support** — arm control (mobile base TBD)
- **Vision-equipped** — image capture for visual awareness during manipulation
- **Multi-LLM agent** — built-in CLI agent supporting Claude, Gemini, and GPT models
- **Three transports** — STDIO, SSE, and Streamed-HTTP

### TakanariShimbo/rosbridge-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [rosbridge-mcp-server](https://github.com/TakanariShimbo/rosbridge-mcp-server) | ~0 | Python | MIT | 8 |

WebSocket-based ROS bridge with comprehensive tool coverage:

- **8 tools** — list_topics, get_topic_info, publish_topic, list_services, publish_service, list_actions, publish_action, cancel_action
- **Remote connectivity** — configurable host/port for both local and remote ROS systems
- **Action lifecycle** — full support for dispatching goals and canceling running actions

## OPC UA (Industrial Protocol)

### midhunxavier/OPCUA-MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [midhunxavier/OPCUA-MCP](https://github.com/midhunxavier/OPCUA-MCP) | ~10 | Python/TypeScript | — | 7 |

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
| [kukapay/opcua-mcp](https://github.com/kukapay/opcua-mcp) | ~20 | Python | — | 4 |

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
| [poly-mcp/IoT-Edge-MCP-Server](https://github.com/poly-mcp/IoT-Edge-MCP-Server) | ~20 | Python | — | 15+ |

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
| [litmusautomation/litmus-mcp-server](https://github.com/litmusautomation/litmus-mcp-server) | — | — | — | 4+ |

Official MCP server from Litmus Automation, an industrial edge computing platform:

- **get_current_value_of_devicehub_tag** — retrieve live tag values from connected industrial devices
- **create_devicehub_device** — register new devices using various industrial protocols and templates
- **get_multiple_values_from_topic** — time-series data retrieval for analysis and plotting
- **run_docker_container_on_litmusedge** — deploy containerized applications directly to edge nodes
- **Grafana integration** — stream real-time machine data to dashboards with LLM-interpreted annotations
- **Cursor IDE integration** — run queries, change settings, and stream data within the editor

Bridges LLMs with the Litmus Edge platform deployed at manufacturing facilities.

### kmanditereza/mcp-server-for-industrial-data

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-server-for-industrial-data](https://github.com/kmanditereza/mcp-server-for-industrial-data) | ~3 | Python | MIT | 2 |

A standardized MCP server for industrial OPC UA data access:

- **get_material_availability** — query material stock levels from OPC UA
- **get_machine_states** — retrieve real-time machine status with automatic state interpretation
- **Framework-agnostic** — works with LangChain, CrewAI, AutoGen, and custom agents
- **STDIO and HTTP transport** — flexible deployment options

Addresses the "constant reinvention of custom integrations" problem in industrial AI.

## 3D Printing & Additive Manufacturing

### DMontgomery40/mcp-3D-printer-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-3D-printer-server](https://github.com/DMontgomery40/mcp-3D-printer-server) | ~161 | TypeScript | GPL-2.0 | 15+ |

The most comprehensive 3D printing MCP server, connecting to 7 major printer platforms:

- **Printer platforms** — OctoPrint, Klipper/Moonraker, Duet, Repetier, Bambu Labs, Prusa Connect, Creality Cloud
- **Print control** — start, cancel, monitor jobs, set temperatures, query status
- **STL manipulation** — scale, rotate, translate, extend base for adhesion, sectional editing
- **STL analysis** — comprehensive model information and multi-angle SVG visualization
- **Slicing** — generate G-code from STL files using OrcaSlicer integration
- **Bambu-specific** — print .3mf files directly via MQTT command
- **File management** — list, upload, and manage G-code on printers

Available as npm package (mcp-3d-printer-server). Note: large STL files (>10MB) can be memory-intensive within MCP.

### OctoEverywhere/mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [OctoEverywhere/mcp](https://github.com/OctoEverywhere/mcp) | ~28 | — | Apache-2.0 | 3+ |

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
| [predictive-maintenance-mcp](https://github.com/LGDiMaggio/predictive-maintenance-mcp) | ~19 | Python | MIT | 20+ |

An open-source framework bringing expert-level machinery diagnostics to LLMs:

- **FFT spectrum analysis** — frequency signatures with windowing and peak detection
- **Envelope analysis** — Hilbert-envelope spectra for early bearing defect detection
- **Fault classification** — unbalance, misalignment, looseness, and bearing faults with confidence scores
- **ISO 20816-3 compliance** — severity zones (A-D) across machine groups, explained in operator-friendly terms
- **ML anomaly detection** — unsupervised/semi-supervised models for new signal classification
- **Report generation** — professional HTML reports with interactive Plotly visualizations, DOCX export
- **Multi-format signals** — CSV, MAT, WAV, NPY, Parquet
- **Vector search docs** — FAISS + TF-IDF fallback for documentation retrieval
- **20 sample signals** — 3 healthy, 17 faulty from real machinery tests
- **Pre-built diagnostic skills** — bearing diagnosis, quick-screening, full report generation

Featured on Hacker News. Currently proof-of-concept stage but demonstrates a compelling vision for democratizing industrial diagnostics. Supports air-gapped deployment for sensitive facilities.

## Engineering Simulation

### matlab/matlab-mcp-core-server (Official MathWorks)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [matlab-mcp-core-server](https://github.com/matlab/matlab-mcp-core-server) | ~236 | Go | BSD-3-Clause | 5 |

The official MATLAB MCP server from MathWorks:

- **Start/quit MATLAB** — session lifecycle management
- **Write code** — create MATLAB scripts and functions
- **Run code** — execute MATLAB code and return results
- **Assess code** — static analysis for style and correctness
- **Simulink integration** — simulate Simulink models through the MCP interface

Works with Claude Code, Claude Desktop, GitHub Copilot in VS Code, and other MCP clients. Relevant to manufacturing for simulation-based design, control system development, signal processing, and production optimization.

MathWorks has also released the MCP Framework for MATLAB Production Server, enabling enterprise deployment of MATLAB-based MCP tools.

## OT Security & Compliance

### Ansvar-Systems/ot-security-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ot-security-mcp](https://github.com/Ansvar-Systems/ot-security-mcp) | ~3 | TypeScript | Apache-2.0 | 7 |

Industrial control system security standards via MCP:

- **IEC 62443-3-3/4-2** — query requirements filtered by Security Level (SL-1 through SL-4)
- **NIST 800-53/800-82** — 228 controls for industrial environments
- **MITRE ATT&CK for ICS** — 83 techniques with mitigations
- **Cross-standard mappings** — IEC-to-NIST control relationships with confidence scores
- **Zone/conduit guidance** — Purdue Model network architecture recommendations
- **Component filtering** — results by device type (embedded, host, network, application)
- **Full-text search** — SQLite FTS5 for instant lookups across 238+ requirements

Target users: control systems engineers implementing IEC 62443, security architects designing network segmentation, compliance officers mapping NIS2 to IEC controls, threat hunters investigating ICS techniques.

From the same Ansvar Systems team that built the EU compliance MCP server (49 regulations, 2,528 articles).

## What's missing

The manufacturing MCP ecosystem has significant gaps in core manufacturing operations:

- **No MES (Manufacturing Execution Systems)** — no Siemens Opcenter, Rockwell Plex, AVEVA, or open-source MES servers
- **No CNC/machining servers** — no G-code generation, toolpath optimization, or machine tool control beyond 3D printing
- **No quality inspection/machine vision** — no automated inspection, SPC/SQC, or defect detection integration
- **No PLM** — Siemens Teamcenter, PTC Windchill, Dassault ENOVIA all absent
- **No ERP manufacturing modules** — Dynamics 365 covers general ERP but no dedicated manufacturing-specific MCP servers for SAP PP/PM, Oracle Manufacturing Cloud, or Epicor
- **No digital twin platforms** — Azure Digital Twins, AWS IoT TwinMaker, Siemens Xcelerator have no MCP servers
- **No warehouse robotics** — Amazon Robotics, Locus Robotics, 6 River Systems absent
- **No semiconductor/fab tools** — no wafer fab, lithography, or semiconductor manufacturing
- **No food/beverage manufacturing** — no HACCP, food safety, or batch processing
- **No pharmaceutical GMP** — no 21 CFR Part 11 compliance, batch records, or cleanroom monitoring (though see our [Pharmaceutical & Healthcare review](/reviews/pharmaceutical-healthcare-mcp-servers/) for adjacent coverage)
- **No CMMS** — no Maximo, SAP PM, or maintenance work order management
- **No safety compliance** — no OSHA, ISO 45001, or lockout/tagout management
- **No industrial vision** — no Cognex, Keyence, or machine vision camera integration
- **No supply chain planning for manufacturing** — no APS (Advanced Planning & Scheduling) tools

## The bottom line

**Rating: 3.5/5** — The manufacturing and industrial MCP ecosystem is a tale of strong peripherals and a hollow core. The peripherals are impressive: robotics has two implementations over 800 stars each, 3D printing supports 7+ printer platforms, OPC UA provides the essential protocol bridge to factory equipment, AWS IoT SiteWise offers 47 tools for enterprise-grade industrial IoT, and predictive maintenance demonstrates compelling AI-assisted diagnostics. Engineering simulation benefits from MathWorks' official MATLAB server.

But the core manufacturing stack — the systems that actually run factories — is almost entirely absent. No MES, no quality control, no CNC programming, no PLM, no digital twins, no CMMS. These are the systems where manufacturing professionals spend most of their time and where AI assistance would create the most value. The gap between "AI can talk to a robot" and "AI can help run a factory" remains enormous.

The OT security dimension is worth noting: Ansvar Systems' IEC 62443 server addresses a real need as manufacturing becomes more connected and vulnerable. Industrial cybersecurity is one of the few areas where MCP standards knowledge queries genuinely help.

**Install if:** you work with ROS robots, 3D printers, OPC UA devices, or AWS IoT SiteWise and want AI-assisted monitoring, control, or diagnostics.

**Skip if:** you need MES integration, CNC programming assistance, quality inspection, or PLM access — the MCP ecosystem hasn't reached the core manufacturing stack yet.

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*


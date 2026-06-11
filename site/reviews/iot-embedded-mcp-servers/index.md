# IoT & Embedded MCP Servers — Home Assistant, MQTT, ESP32, ROS, Industrial PLCs, 3D Printers, and More

> IoT and embedded MCP servers are bridging AI agents and the physical world via the Model Context Protocol. We reviewed 60+ servers across 9 subcategories.


*Part of the [IoT & Hardware](/categories/iot-hardware/) category.*

IoT and embedded MCP servers are bridging the gap between AI agents and the physical world. Instead of writing custom integrations for every device, sensor, and controller, these servers let AI assistants control smart homes, program microcontrollers, monitor industrial equipment, operate robots, and manage 3D printers — all through the Model Context Protocol.

The landscape spans nine areas: **smart home platforms** (Home Assistant dominates with an official integration plus multiple community servers), **smart home devices** (Tuya, Philips Hue, Apple HomeKit), **IoT platforms** (ThingsBoard, AWS IoT SiteWise), **MQTT brokers** (the backbone of IoT communication), **ESP32 and Arduino** (AI-driven embedded development), **Raspberry Pi** (GPIO, I2C, SPI, and camera access), **robotics** (ROS/ROS2 integration), **industrial IoT** (OPC UA, Siemens PLCs, SCADA), and **3D printing** (multi-platform printer control and STL operations).

The headline findings since our April 2026 refresh: **homeassistant-ai/ha-mcp hit 3,300 stars** with five major releases (v7.4 through v7.7), adding Tool Security Policies, sandboxed custom tool execution via `ha_manage_custom_tool`, OAuth 2.1, auto-backup before destructive write calls, and a web UI for per-tool enable/disable/pin. **espressif/esp-claw quintupled to 1,500 stars** with expanded hardware support (ESP32-P4, C5, and more) and an official M5Stack fork. **Espressif launched a hosted documentation MCP server** at `mcp.espressif.com/docs` — real-time AI access to all official ESP chip and SDK documentation. **allenporter/mcp-server-home-assistant is now archived** — its work was fully merged into Home Assistant Core, which runs at 2026.6.2. **voska/hass-mcp (299 stars)** emerged as a strong Go-based third option for Home Assistant. **Ranch-Hand-Robotics/rde-mcp-ros-2** brings 30+ tools embedded in VS Code's Robot Developer Extension. In 3D printing, **DMontgomery40 spun off a Bambu-only fork** (57 stars) and **codeofaxel/Kiln** appeared as a new 810+-tool competitor. **midhunxavier/OPCUA-MCP** filled the gap left by dormant kukapay/opcua-mcp.

## Smart Home Platforms

### Home Assistant Official MCP Integration

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Home Assistant MCP](https://www.home-assistant.io/integrations/mcp_server/) | — | Python | Apache-2.0 | Built-in |

Home Assistant includes MCP server support as an official core integration (since HA 2025.2, now at **2026.6.2**). Any Home Assistant installation can expose its entities, automations, and services to MCP-compatible AI agents without third-party add-ons.

**2026.6 update**: Previously advanced options are now enabled by default, broadening accessibility. HA now ships two integrations: **MCP Server** (HA acts as server for external clients) and **MCP Client** (HA connects out to external MCP servers, including Claude, ChatGPT, Cursor). A read-only home state snapshot resource was added for inspection and debugging. **Silver quality classification**. Adopted by **2.6% of active HA installations** — meaningful scale for a relatively new protocol integration.

### homeassistant-ai/ha-mcp (Community Leader — 3,300 Stars)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [homeassistant-ai/ha-mcp](https://github.com/homeassistant-ai/ha-mcp) | 3,300 | TypeScript/Python | MIT | 80+ |

The fastest-growing and most feature-rich Home Assistant MCP server — and the one with the most aggressive release cadence in the entire IoT category. Grew from 2,500 to 3,300 stars (+32%) since our April refresh, with five major releases:

- **v7.4.0 (Apr 29)**: Unified helper deletion across 27 types, energy preferences tool, addon API renamed to `ha_manage_addon`
- **v7.5.0 (May 13)**: **Sandboxed code execution** via `ha_manage_custom_tool` — AI agents can create and run custom tools within a safe sandbox; scene config tools; event bus publishing; web UI for per-tool enable/disable/pin; **OAuth 2.1 mode (beta)**
- **v7.6.0 (May 27)**: **Tool Security Policies** — per-tool approval gating so sensitive operations require explicit user sign-off; configurable HTTP bind host; **auto-backup before destructive write calls**; Assist pipeline management
- **v7.7.0 (Jun 10)**: User-configurable filesystem directories; consolidated search; nested beta toggle panel; improved automation/script YAML handling

The Agent Skills system (introduced in April's v7.3.0) remains a differentiator — domain-specific guides served as MCP resources that teach AI agents how to write automations, select helpers, and safely refactor HA configurations. The Webhook Proxy add-on routes MCP traffic through existing reverse proxies with no separate tunnel needed.

### tevonsb/homeassistant-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [tevonsb/homeassistant-mcp](https://github.com/tevonsb/homeassistant-mcp) | 575 | TypeScript | MIT | 20+ |

The original well-established community server, now in slow maintenance mode. Star count essentially flat (554 → 575). No major new releases since April 2026. Still useful as a stable, minimal alternative — but ha-mcp has superseded it for feature depth.

### voska/hass-mcp (NEW — 299 Stars)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [voska/hass-mcp](https://github.com/voska/hass-mcp) | 299 | Go | — | 30+ |

A strong new entrant. Go-based with **HTTP transport** (vs. most HA servers using stdio), enabling Docker deployment without local process management. Focuses on entity management, device history, statistics, and guided conversations. Notable for being the only major HA MCP server in Go — a language choice that brings different deployment characteristics and potentially better concurrency for multi-agent setups.

### ~~allenporter/mcp-server-home-assistant~~ (Archived)

| Server | Stars | Language | License | Status |
|--------|-------|----------|---------|--------|
| [allenporter/mcp-server-home-assistant](https://github.com/allenporter/mcp-server-home-assistant) | 67 | Python | Apache-2.0 | **Archived** |

**Archived on March 2, 2025** — read-only. This project served its purpose: the custom component was upstreamed into Home Assistant Core via [PR #134122](https://github.com/home-assistant/core/pull/134122). Superseded by the built-in HA integration. No longer relevant for new deployments.

### tdeckers/openhab-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [tdeckers/openhab-mcp](https://github.com/tdeckers/openhab-mcp) | <10 | Python | — | ~5-10 |

MCP server for **openHAB** — the other major open-source smart home platform. Interacts via its REST API. Lower adoption than Home Assistant servers but fills an important gap for openHAB users.

## Smart Home Devices

### tuya/tuya-mcp-sdk (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [tuya/tuya-mcp-sdk](https://github.com/tuya/tuya-mcp-sdk) | ~16 | Python, Go, C# | Apache-2.0 | SDK |

Official SDK from **Tuya** — one of the world's largest IoT cloud platforms. Provides Python, Go, and C# SDKs for integrating Tuya Cloud capabilities with AI agents via MCP. Tuya's AI Agent Development Platform fully supports MCP server integration. Star count essentially flat since April — the SDK is in maintenance mode rather than active development.

A community-built **Tuya Smart Home MCP Server** (4,500+ downloads) adds local control via tinytuya for lower latency and better privacy.

### rmrfslashbin/hue-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [rmrfslashbin/hue-mcp](https://github.com/rmrfslashbin/hue-mcp) | 10-20 | Go | — | 15+ |

Modern MCP server for **Philips Hue** lighting systems. Supports multi-bridge control, real-time sync, and comprehensive tools for lights, rooms, scenes, and bridges. The Go implementation is notable — most IoT MCP servers are Python.

### ykhli/mcp-light-control

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ykhli/mcp-light-control](https://github.com/ykhli/mcp-light-control) | ~10 | TypeScript | — | ~5 |

Philips Hue light control for Cursor and Claude Desktop — including sending messages through lights using **Morse code**. A creative demonstration of AI-hardware interaction.

### thomasvincent/home-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [thomasvincent/home-mcp](https://github.com/thomasvincent/home-mcp) | <10 | Swift/TypeScript | — | ~5-10 |

MCP server for **Apple Home** on macOS. Controls HomeKit devices, scenes, and automations via MCP. The only MCP server targeting the Apple HomeKit ecosystem directly.

## IoT Platforms

### thingsboard/thingsboard-mcp (Official — Most Tools)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [thingsboard/thingsboard-mcp](https://github.com/thingsboard/thingsboard-mcp) | 98 | Python | Apache-2.0 | 120+ |

Official MCP server from **ThingsBoard** — the most popular open-source IoT platform. Stars grew significantly (from ~20-50 range to 98). With **120+ tools**, this has the highest tool count of any server in the IoT/embedded category: device provisioning, entity management, telemetry analytics, dashboard creation, and operational automation.

**v2.1.0 (February 2026)**: Added API key authentication, tool groups for context window optimization, OTA package management, device creation tools, and improved cross-LLM tool descriptions. **No new commits since February 2026** — the project is well-featured but currently quiet.

### ThingsPanel/thingspanel-mcp (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ThingsPanel/thingspanel-mcp](https://github.com/ThingsPanel/thingspanel-mcp) | 5-10 | Python | Apache-2.0 | ~10-15 |

Official MCP server from **ThingsPanel** — another open-source IoT platform. Supports MQTT and Modbus devices with integration for Claude and GPT models.

### AWS IoT SiteWise MCP (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [awslabs/mcp — IoT SiteWise](https://github.com/awslabs/mcp) | Part of 9,254 | Python | Apache-2.0 | 20+ |

Official AWS MCP server for **IoT SiteWise** — AWS's industrial IoT service. **20+ tools** for asset management, data ingestion, monitoring, analytics, time-series aggregations, and bulk export via S3 with KMS encryption. Part of the awslabs/mcp monorepo (9,254 stars, up from 8,500). Received routine maintenance updates in April–May 2026 but no new features.

### Duke-CEI-Center/IoT-MCP-Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Duke-CEI-Center/IoT-MCP-Servers](https://github.com/Duke-CEI-Center/IoT-MCP-Servers) | <10 | Python | — | ~10 |

Academic IoT MCP server from **Duke University**. Reads sensor data and dispatches data collection tasks for AI assistants.

## MQTT

MQTT is the dominant messaging protocol in IoT — lightweight, pub/sub, designed for constrained networks. Multiple MCP servers bridge AI agents to MQTT brokers.

### ezhuk/mqtt-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ezhuk/mqtt-mcp](https://github.com/ezhuk/mqtt-mcp) | 5-15 | Python | — | ~5 |

Lightweight MCP server connecting LLM agents to MQTT devices. Designed for **building automation**, **industrial control**, and **smart home** systems. Uses FastMCP 2.0.

### Benniu/emqx-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Benniu/emqx-mcp-server](https://github.com/Benniu/emqx-mcp-server) | 5-10 | Python | — | ~10 |

MCP server for **EMQX** — the most popular open-source MQTT broker. Supports both EMQX Cloud and self-hosted clusters.

### CorefluxCommunity/Coreflux-MQTT-MCP-Server (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [CorefluxCommunity/Coreflux-MQTT-MCP-Server](https://github.com/CorefluxCommunity/Coreflux-MQTT-MCP-Server) | ~2 | Python | — | 15+ |

Enterprise-grade MCP server from **Coreflux** for their MQTT broker. Full TLS support, API access, AI code generation, and health monitoring. **15+ tools** — the most feature-rich MQTT-specific MCP server.

### tspspi/mcpMQTT

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [tspspi/mcpMQTT](https://github.com/tspspi/mcpMQTT) | <10 | Python | — | ~5 |

Generic MQTT interface with fine-grained topic permissions using wildcard matching. Security-conscious design for multi-tenant MQTT environments.

### mqtt-ai/mcp-over-mqtt

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mqtt-ai/mcp-over-mqtt](https://github.com/mqtt-ai/mcp-over-mqtt) | 10-20 | TypeScript/Python | — | Transport layer |

An **MCP-over-MQTT transport specification** with built-in service registry, discovery, and load balancing. Enables MCP in IoT environments where HTTP isn't practical.

## ESP32, Arduino, and Embedded Frameworks

The embedded MCP space continues to accelerate. **Espressif** — the company behind ESP32 — has made the most visible vendor commitment of any hardware manufacturer to MCP, and that commitment deepened significantly since our April refresh.

### espressif/esp-claw (Official — AI Agent Framework — 1,500 Stars)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [espressif/esp-claw](https://github.com/espressif/esp-claw) | 1,500 | C/Lua | Apache-2.0 | Framework |

**The biggest star-growth story in the IoT category since our April refresh: ESP-Claw quintupled from 304 to 1,500 stars.** Espressif's official "Chat Coding" AI agent framework for ESP32 devices acts as **both MCP server and client** — exposing hardware capabilities to external agents while calling external services.

Key features: **on-device memory** (structured long-term memory lives on-chip, preferences and routines auto-extracted from conversations), **Chat Coding** (define device behavior through natural conversation, with LLM handling dynamic decisions and local Lua scripts executing deterministically even offline), and support for OpenAI, Anthropic, DeepSeek, Qwen, and custom LLM endpoints.

Hardware support has expanded: originally ESP32-S3 only, now also supports **ESP32-P4, ESP32-C5, ESP32-S31**, and a variety of dev boards including M5Stack CoreS3. **M5Stack has officially forked esp-claw** for their device line — a significant sign of ecosystem momentum. Last updated June 2026.

### ESP-IDF 6.0 Built-in MCP Server (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| ESP-IDF 6.0 MCP Server | Part of ESP-IDF | Python | Apache-2.0 | ~8 |

ESP-IDF 6.0 (released March 2026) ships with a **built-in MCP server** for development workflows. Tools cover building, flashing, setting the target, and cleaning, plus resources for querying project configuration, build status, and connected devices. Launched via `eim run` using the ESP-IDF Installation Manager.

The official embedded development framework for the world's most popular IoT microcontroller now treats MCP as a first-class feature.

### Espressif Documentation MCP Server (Official Hosted — NEW)

Espressif launched a **hosted documentation MCP server** at `https://mcp.espressif.com/docs` (announced April 8, 2026). Authentication via GitHub or WeChat. Connects AI agents to all official Espressif documentation in real time — ESP-IDF, ESP chips, SDKs. Read-only; does not execute code or modify files.

Combined with the ESP-IDF 6.0 built-in tools server, this gives AI agents a complete ESP32 development workflow: look up docs via the hosted server, build and flash via the local tools server.

### espressif/esp-rainmaker-mcp (Official — IoT Device Control)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [espressif/esp-rainmaker-mcp](https://github.com/espressif/esp-rainmaker-mcp) | ~7 | Python | Apache-2.0 | ~10 |

Official MCP wrapper for **ESP RainMaker** — Espressif's cloud IoT platform. Bridges MCP clients with the RainMaker CLI for natural language control of IoT devices via Claude, Cursor, Gemini CLI, and Windsurf. Star count essentially flat (~9 → ~7, likely noise in trackers).

### 78/xiaozhi-esp32 (MCP-Based Chatbot — 24K Stars)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [78/xiaozhi-esp32](https://github.com/78/xiaozhi-esp32) | ~24,000 | C/C++ | — | MCP client |

The most starred project in the IoT MCP space. Xiaozhi is an open-source MCP-based chatbot running on ESP32 hardware. Latest firmware: **v2.2.6**. The v1 branch was retired in February 2026. Recent updates include new hardware board support (Waveshare ESP32-S3-Touch-LCD, M5Stack Cardputer Adv), wake word fixes, LCD layout improvements, and camera/audio optimization. Now supports **70+ boards** with cloud-side MCP for smart home control, PC desktop operation, and knowledge search.

While technically an MCP client rather than server, its 24K stars and active community make it the most visible demonstration of MCP in the embedded world.

### horw/esp-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [horw/esp-mcp](https://github.com/horw/esp-mcp) | ~150 | Python | MIT | ~5 |

The original community ESP-IDF MCP server. Centralizes ESP-IDF commands for AI-driven interaction — build, flash, and automatic issue fixing. Star count flat since April. Still useful as a more configurable alternative to the official built-in server.

### rzeldent/esp32-cam-ai (NEW)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [rzeldent/esp32-cam-ai](https://github.com/rzeldent/esp32-cam-ai) | <10 | C++ | — | ~5-8 |

New MCP server for **ESP32-CAM** modules: image capture, LED/flash control, and system diagnostics. Connects AI agents directly to ESP32 cameras for vision tasks without a separate Pi or compute board.

### jurgen178/esp32-mcp (NEW)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [jurgen178/esp32-mcp](https://github.com/jurgen178/esp32-mcp) | <10 | C++ | — | Framework |

Notable for running MCP **natively on Arduino Nano ESP32** entirely in C++ — without an official C++ MCP SDK. A proof-of-concept that MCP can run server-side on very constrained hardware using only the Arduino framework.

### MicroPython MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| MicroPython MCP Bridge | — | Python | — | ~5 |

An MCP bridge server allowing direct code execution from an LLM on any board running **MicroPython** (ESP32, RP2040, etc.) via USB Serial or WebREPL. Compatible with Claude Desktop, VS Code Codex, Copilot, and Antigravity.

### solnera/esp32-mcpserver

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [solnera/esp32-mcpserver](https://github.com/solnera/esp32-mcpserver) | — | C++ (Arduino) | — | Framework |

A lightweight MCP server framework for ESP32, available on **PlatformIO**. Seamlessly connects embedded devices to LLMs via WebSocket/JSON-RPC. Developers build custom tools for their specific hardware.

### Serial Communication Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp2everything/mcp2serial](https://github.com/mcp2everything/mcp2serial) | 33 | Python | MIT | ~5-10 |
| [Adancurusul/serial-mcp-server](https://github.com/Adancurusul/serial-mcp-server) | 10-20 | Python | — | 10+ |
| [bmdragos/serial-mcp](https://github.com/bmdragos/serial-mcp) | <10 | Python | — | ~3-5 |

Three serial communication MCP servers for talking to Arduino, ESP32, and other hardware over USB serial. **mcp2serial** (33 stars) leads with Raspberry Pi Pico support. **serial-mcp-server** provides the most comprehensive serial capabilities with professional debugging features. **serial-mcp** is a minimal implementation built specifically for Claude Code.

## Raspberry Pi

### grammy-jiang/RaspberryPiOS-MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [grammy-jiang/RaspberryPiOS-MCP](https://github.com/grammy-jiang/RaspberryPiOS-MCP) | <10 | Python | — | 15+ |

The most comprehensive Raspberry Pi MCP server. Modular design with **15+ tools** covering:

- **System metrics** — CPU, memory, disk, temperature monitoring
- **Service management** — start, stop, restart systemd services
- **GPIO** — digital I/O via gpiozero
- **I2C** — sensor communication via smbus2
- **SPI and serial** — hardware bus access
- **Camera** — Pi camera control and capture

### UnitApi/mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [UnitApi/mcp](https://github.com/UnitApi/mcp) | 5-10 | Python | — | 10+ |

Secure hardware control through MCP with real-time GPIO streaming. Supports LED control, button input, and sensor operations on Raspberry Pi.

## Robotics (ROS)

### robotmcp/ros-mcp-server (Most Starred IoT MCP Server)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [robotmcp/ros-mcp-server](https://github.com/robotmcp/ros-mcp-server) | 1,300 | Python | Apache-2.0 | 15+ |

The most starred IoT MCP server. Provides **bidirectional AI-robot communication** across both ROS1 and ROS2: natural language → robot commands (topic publications, service calls, action goals), and robot state → AI understanding (topics, transforms, sensor data). Grew from 1,200 to 1,300 stars. The roadmap lists ROS Actions support and Permission controls as upcoming.

### wise-vision/ros2_mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [wise-vision/ros2_mcp](https://github.com/wise-vision/ros2_mcp) | ~60 | Python | — | 10+ |
| [wise-vision/mcp_server_ros_2](https://github.com/wise-vision/mcp_server_ros_2) | — | Python | — | 10+ |

An advanced ROS 2 MCP server with 1-minute setup, auto type discovery, image streaming (Image and CompressedImage), and full action support. wise-vision also published this as **mcp_server_ros_2** on the Docker MCP Catalog, pushing toward broader distribution and containerized deployment.

### Ranch-Hand-Robotics/rde-mcp-ros-2 (NEW)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ranch-hand-robotics/rde-mcp-ros-2](https://github.com/ranch-hand-robotics/rde-mcp-ros-2) | <10 | Python | — | 30+ |

A new ROS 2 MCP server embedded in the **Robot Developer Extension for VS Code**. **30+ tools** for full system introspection — topics, services, actions, nodes, parameters, and logs. Designed for IDE-native robot development with AI assistance. The VS Code integration is notable: developers get AI-assisted ROS 2 development without leaving their editor.

### lpigeon/ros-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [lpigeon/ros-mcp-server](https://github.com/lpigeon/ros-mcp-server) | 50-100 | Python | — | ~10 |

ROS/ROS2 MCP server focused on transforming natural language into robot commands. Actively maintained.

### Additional ROS Servers

| Server | Stars | Language | Description |
|--------|-------|----------|-------------|
| [Yutarop/ros-mcp](https://github.com/Yutarop/ros-mcp) | <10 | Python | Lightweight ROS/ROS2: topics, services, actions with any message type |
| [kakimochi/ros2-mcp-server](https://github.com/kakimochi/ros2-mcp-server) | <10 | Python | ROS 2 velocity commands via /cmd_vel |
| [TakanariShimbo/rosbridge-mcp-server](https://github.com/TakanariShimbo/rosbridge-mcp-server) | <10 | Python | ROS via rosbridge WebSocket |

## Industrial IoT — OPC UA, PLCs, and SCADA

### midhunxavier/OPCUA-MCP (NEW — Most Capable OPC UA Server)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [midhunxavier/OPCUA-MCP](https://github.com/midhunxavier/OPCUA-MCP) | 13 | Python, Node.js | — | ~10 |

The new leader for OPC UA MCP integration. Dual Python and Node.js implementations, supporting browse nodes, read/write variables, call methods, historical data retrieval, and batch operations. Actively updated through June 2026. Has effectively superseded kukapay/opcua-mcp as the go-to community OPC UA server.

### kukapay/opcua-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [kukapay/opcua-mcp](https://github.com/kukapay/opcua-mcp) | 26 | Python | — | ~5 |

MCP server connecting to **OPC UA**-enabled industrial systems — reads and writes OPC UA node values. **Dormant since October 2025** — no updates in 2026. Star count grew to 26 but the project appears stalled. midhunxavier/OPCUA-MCP is the more actively maintained alternative.

### cadugrillo/s7-mcp-bridge

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cadugrillo/s7-mcp-bridge](https://github.com/cadugrillo/s7-mcp-bridge) | ~19 | Go | — | ~5-10 |

MCP server connecting AI agents to **Siemens S7-1500 and S7-1200 PLCs** using the S7 protocol. **Dormant since January 2026** — no updates for five months. The Go implementation and S7 protocol support remain unique, but the project is stalled.

### poly-mcp/IoT-Edge-MCP-Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [poly-mcp/IoT-Edge-MCP-Server](https://github.com/poly-mcp/IoT-Edge-MCP-Server) | <10 | Python | — | 15-20 |

Enterprise-grade MCP server for Industrial IoT. Unifies **MQTT sensors**, **Modbus devices**, and industrial equipment with InfluxDB time-series storage and Redis caching. Real-time monitoring, alarms, and actuator control — the closest thing to a SCADA MCP interface.

### AddisonTech/Hermes (NEW)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [AddisonTech/Hermes](https://github.com/AddisonTech/Hermes) | <5 | Rust | — | ~5 |

Very new (updated June 11, 2026). Rust-based bridge connecting AI agents to plant-floor industrial data via OPC-UA. Noteworthy as the only Rust-based OPC UA MCP server — early stage but potentially interesting for latency-sensitive industrial use cases.

## 3D Printing

### DMontgomery40/mcp-3D-printer-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [DMontgomery40/mcp-3D-printer-server](https://github.com/DMontgomery40/mcp-3D-printer-server) | 195 | JavaScript/TypeScript | GPL-2.0 | 25+ |

The most comprehensive multi-platform 3D printing MCP server. Grew from 168 to 195 stars. Connects to **8 printer platforms**: OrcaSlicer, Bambu Lab, OctoPrint, Klipper, Duet, Repetier, Prusa, and Creality.

**Recent updates (v1.2.4, v1.2.6 — May 2026)**: Added FULU OrcaSlicer/Bambu support, fixed HTTP compatibility entrypoints, and fixed a schema bug in `upload_gcode` inputSchema for Anthropic tool compatibility. Available on Docker Hub and npm.

The maintainer also spun off **DMontgomery40/bambu-printer-mcp** (see below) as a leaner Bambu-only alternative.

### DMontgomery40/bambu-printer-mcp (NEW — Bambu-Only Fork)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [DMontgomery40/bambu-printer-mcp](https://github.com/DMontgomery40/bambu-printer-mcp) | 57 | TypeScript | GPL-2.0 | 20+ |

A new spin-off from the same author. Strips all non-Bambu platforms for a leaner, faster install focused entirely on Bambu Lab printers. **57 stars** since creation in May 2026. Includes STL manipulation, BambuStudio slicing, AMS management, and camera snapshots. Good choice for Bambu-only shops that don't need multi-platform overhead.

### codeofaxel/Kiln (NEW — Most Ambitious New Entrant)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [codeofaxel/Kiln](https://github.com/codeofaxel/Kiln) | 21 | — | — | 810+ |

The most ambitious new 3D printing MCP server. **810+ tools** — more than any other server in the 3D printing category. End-to-end text-to-print workflows with multi-printer support (OctoPrint, Klipper, Bambu, Creality, Prusa, AnyCubic, Elegoo, USB/Marlin), failure recovery with layer-level resumption, and marketplace integration (MyMiniFactory, Cults3D). Includes outsourcing via Craftcloud. **Freemium** ($49–$199/month for premium tiers). Very recently updated (within the last day as of June 12). Worth watching — the scope is far beyond any other 3D printing MCP server.

### OctoEverywhere/mcp (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [OctoEverywhere/mcp](https://github.com/OctoEverywhere/mcp) | ~34 | Python | — | ~5 |

Official MCP server from **OctoEverywhere** — the most popular cloud management platform for 3D printers. Supports OctoPrint, Klipper, Bambu Lab, Elegoo, Prusa, and Creality. Provides live printer state, webcam snapshots, and printer control. **Code-frozen since July 2025** — the server remains in production but no new features have shipped in nearly a year. The cloud backend continues to improve, but the MCP server layer is stable/static.

### schwarztim/bambu-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [schwarztim/bambu-mcp](https://github.com/schwarztim/bambu-mcp) | ~15 | TypeScript | MIT | 25 |

Complete MCP server for **Bambu Lab** 3D printers. **25 tools** covering print control, status monitoring, camera access, AMS, temperature monitoring, and LED control. Local MQTT communication with X.509 certificate authentication. Quiet since April 2026.

### Disane87/spoolman-mcp (NEW)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Disane87/spoolman-mcp](https://github.com/Disane87/spoolman-mcp) | ~2 | — | — | ~10 |

A new adjacent tool: filament inventory management via the **Spoolman API**. Not a printer controller — manages vendors, filament types, and spool inventory with full CRUD, JSON/CSV export, and database backup. Useful alongside any of the printer control servers for tracking material consumption.

## Other Notable Servers

### Drone Control

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [0xKoda/drone-mcp](https://github.com/0xKoda/drone-mcp) | <10 | Python | — | ~5-10 |

MCP server for controlling **DJI Tello** drones — takeoff, landing, movement commands, and video streaming.

### Bluetooth

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Hypijump31/bluetooth-mcp-server](https://github.com/Hypijump31/bluetooth-mcp-server) | 14 | Python | — | 1 |

Bluetooth device scanning and interaction. Supports both BLE and Classic Bluetooth on Windows, macOS, and Linux.

### Zigbee2MQTT

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ichbinder/MCP2ZigBee2MQTT](https://github.com/ichbinder/MCP2ZigBee2MQTT) | <10 | Python | — | ~5-10 |

MCP server for **Zigbee2MQTT** with intelligent device discovery — auto-analyzes all connected Zigbee devices and exposes their capabilities.

### Node-RED Integration

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [TobiasLante/node-red-contrib-mcp](https://github.com/TobiasLante/node-red-contrib-mcp) | 10-20 | JavaScript | — | Node-RED nodes |
| [karavaev-evgeniy/node-red-mcp-server](https://github.com/karavaev-evgeniy/node-red-mcp-server) | <10 | JavaScript | — | ~10 |

Two approaches to **Node-RED** MCP integration: node-red-contrib-mcp adds MCP nodes to Node-RED's visual flow editor; node-red-mcp-server lets AI agents manage Node-RED flows, nodes, and settings.

### Sensor Monitoring

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [diegobit/aranet4-mcp-server](https://github.com/diegobit/aranet4-mcp-server) | <10 | Python | — | ~5 |

MCP server for the **Aranet4 CO2 sensor**. Scans for devices, fetches data, stores in local SQLite, and provides historical querying with visualization.

## Curated Resources

**[beriberikix/awesome-mcp-hardware](https://github.com/beriberikix/awesome-mcp-hardware)** — A curated awesome-list specifically for MCP servers interacting with hardware and the physical world. Good reference for discovering new IoT/embedded MCP servers as they emerge.

## What's missing

The gap list is largely unchanged from our April refresh:

- **No official Arduino IDE integration** — the most popular embedded development platform has no MCP server for project management, board configuration, or compilation (Espressif's ESP-IDF 6.0 built-in server partially addresses this for ESP chips only)
- **No major Zigbee/Z-Wave hub vendors** — Samsung SmartThings, Hubitat, and Aeotec have no official MCP servers
- **No PLC vendor servers** — Siemens, Allen-Bradley (Rockwell), Mitsubishi, and ABB have no official MCP offerings (only dormant community bridges)
- **No Matter/Thread protocol servers** — the new smart home standard has no dedicated MCP support (accessible indirectly through Home Assistant)
- **No LoRaWAN servers** — the dominant LPWAN technology for IoT remains absent from the MCP ecosystem
- **No edge AI servers** — no MCP integration for TensorFlow Lite, ONNX Runtime, or other edge inference frameworks (ESP-Claw's on-device inference is closest)
- **Limited sensor aggregation** — individual sensor servers exist but no unified multi-sensor hub

## The bottom line

**Rating: 4.0/5** — The IoT/embedded MCP ecosystem is deepening, not just widening. The home automation subcategory stands out: homeassistant-ai/ha-mcp hit 3,300 stars with five releases in under seven weeks, adding enterprise-grade features (Tool Security Policies, sandboxed execution, OAuth 2.1) that put it ahead of most non-IoT MCP servers in sophistication. The allenporter project completing its mission — merging into Home Assistant Core and gracefully archiving — shows what healthy open-source MCP development looks like.

Espressif's story is the other big headline: ESP-Claw quintupled in stars, ESP-IDF 6.0 ships MCP as a built-in feature, and a hosted documentation server at mcp.espressif.com/docs completes a three-part official AI development stack for ESP32. M5Stack forking ESP-Claw signals that the embedded AI agent paradigm is moving downstream from experiments to product.

The remaining gaps — vendor adoption from Siemens, Arduino, and SmartThings; emerging standards like Matter and LoRaWAN — are consistent. The category will hit 5.0/5 when industrial PLC vendors and smart home hub makers ship official servers. Until then, 4.0/5 reflects a well-developed ecosystem with meaningful but still-present holes.

*This review was refreshed on 2026-06-12 using Claude Sonnet 4.6 (Anthropic). Originally published 2026-03-15.*


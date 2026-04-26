---
title: "IoT & Embedded MCP Servers — Home Assistant, MQTT, ESP32, ROS, Industrial PLCs, 3D Printers, and More"
date: 2026-03-15T11:00:00+09:00
description: "IoT and embedded MCP servers are bridging AI agents and the physical world via the Model Context Protocol. We reviewed 55+ servers across 9 subcategories."
og_description: "IoT & embedded MCP servers: robotmcp/ros-mcp-server (1,200 stars, ROS/ROS2), homeassistant-ai/ha-mcp (2,500 stars, Agent Skills), espressif/esp-claw (304 stars, official AI agent framework on ESP32), ESP-IDF 6.0 built-in MCP, 78/xiaozhi-esp32 (24K stars, MCP chatbot), thingsboard/thingsboard-mcp (120+ tools), DMontgomery40/mcp-3D-printer-server (168 stars). 55+ servers reviewed. Rating: 4.0/5."
content_type: "Review"
card_description: "IoT and embedded MCP servers across smart home platforms, robotics, IoT platforms, MQTT brokers, microcontrollers, industrial systems, 3D printers, and more. This is where AI meets the physical world — and the breadth is genuinely surprising. The biggest story since our original review: Espressif has gone all-in on MCP with four official efforts — ESP-Claw (304 stars, a Chat Coding AI agent framework that acts as both MCP server and client on ESP32), ESP-IDF 6.0's built-in MCP server for development workflows, ESP RainMaker MCP for IoT device control, and a Documentation MCP server. The robotics subcategory leads in community adoption: robotmcp/ros-mcp-server (1,200 stars, up from 873, Apache-2.0) enables bidirectional AI-robot communication across both ROS1 and ROS2, now joined by wise-vision/ros2_mcp (73 stars) with auto-discovery and image streaming. Smart home is the most developed subcategory by server count: homeassistant-ai/ha-mcp has doubled to 2,500 stars with v7.3.0 introducing Agent Skills and a Webhook Proxy add-on, while tevonsb/homeassistant-mcp grew to 554 stars. The embedded chatbot space exploded: 78/xiaozhi-esp32 (24K stars) is an MCP-based chatbot running on ESP32 with cloud-side MCP for smart home control, desktop operation, and knowledge search. A new MicroPython MCP server bridges AI agents to any MicroPython board. 3D printing surged: DMontgomery40/mcp-3D-printer-server tripled from 61 to 168 stars with new Bambu FTP operations, OrcaSlicer CLI slicing, and mesh preparation tools. IoT platforms are represented by thingsboard/thingsboard-mcp (official, 120+ tools) and AWS IoT SiteWise MCP (official, 20+ tools). Vendor count grew from 7 to 10+ with Espressif's massive commitment. Key remaining gaps: no LoRaWAN servers, no Matter/Thread dedicated support, no official Arduino IDE integration. The category holds at 4.0/5 — Espressif's vendor commitment and the explosive growth across robotics, smart home, and embedded chatbots confirm IoT MCP is no longer experimental."
last_refreshed: 2026-04-26
---

*Part of the [IoT & Hardware](/categories/iot-hardware/) category.*

IoT and embedded MCP servers are bridging the gap between AI agents and the physical world. Instead of writing custom integrations for every device, sensor, and controller, these servers let AI assistants control smart homes, program microcontrollers, monitor industrial equipment, operate robots, and manage 3D printers — all through the Model Context Protocol.

The landscape spans nine areas: **smart home platforms** (Home Assistant dominates with an official integration plus multiple community servers), **smart home devices** (Tuya, Philips Hue, Apple HomeKit), **IoT platforms** (ThingsBoard, AWS IoT SiteWise), **MQTT brokers** (the backbone of IoT communication), **ESP32 and Arduino** (AI-driven embedded development), **Raspberry Pi** (GPIO, I2C, SPI, and camera access), **robotics** (ROS/ROS2 integration), **industrial IoT** (OPC UA, Siemens PLCs, SCADA), and **3D printing** (multi-platform printer control and STL operations).

The headline findings: **Espressif has gone all-in on MCP** with four official efforts — ESP-Claw (304 stars, AI agent framework on ESP32), ESP-IDF 6.0's built-in MCP server, ESP RainMaker MCP, and a Documentation MCP server. **robotmcp/ros-mcp-server jumped to 1,200 stars** (up from 873) with bidirectional AI-robot communication across ROS1 and ROS2. **homeassistant-ai/ha-mcp doubled to 2,500 stars** with v7.3.0 bringing Agent Skills that guide AI through automations and device configuration. **78/xiaozhi-esp32 has 24K stars** as an MCP-based chatbot running on ESP32 with cloud-side MCP for smart home, desktop control, and knowledge search. **thingsboard/thingsboard-mcp provides the most tools** — 120+ for the full IoT platform lifecycle. **DMontgomery40/mcp-3D-printer-server tripled to 168 stars** with new Bambu FTP operations, OrcaSlicer CLI slicing, and mesh preparation tools. **A MicroPython MCP server** now bridges AI agents to any MicroPython board via USB Serial or WebREPL. **Ten or more vendors provide official MCP servers** — Home Assistant, ThingsBoard, Tuya, AWS, OctoEverywhere, Coreflux, ThingsPanel, and now Espressif with multiple entries.

## Smart Home Platforms

### Home Assistant Official MCP Integration

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Home Assistant MCP](https://www.home-assistant.io/integrations/mcp_server/) | — | Python | Apache-2.0 | Built-in |

Home Assistant now includes MCP server support as an official core integration. This means any Home Assistant installation can expose its entities, automations, and services to MCP-compatible AI agents without installing third-party add-ons.

The official integration brings the weight of the Home Assistant project — the most popular open-source home automation platform — behind the Model Context Protocol.

### tevonsb/homeassistant-mcp (Most Popular Community Server)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [tevonsb/homeassistant-mcp](https://github.com/tevonsb/homeassistant-mcp) | 554 | TypeScript | MIT | 20+ |

A well-established community-built Home Assistant MCP server. Exposes Home Assistant to LLM applications through HTTP/SSE/WebSocket APIs. Supports natural language control and monitoring of all connected devices.

TypeScript implementation with **20+ tools** covering entity control, state monitoring, and automation management. The MIT license and active community make this a strong choice if you need more control than the official integration provides.

### homeassistant-ai/ha-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [homeassistant-ai/ha-mcp](https://github.com/homeassistant-ai/ha-mcp) | 2,500 | TypeScript/Python | MIT | 80+ |

The most feature-rich and fastest-growing Home Assistant MCP server with **80+ tools** — providing the deepest AI control surface for home automation. Covers entities, automations, devices, scenes, and service calls.

**v7.3.0 (April 2026)** introduced **Agent Skills** — domain-specific guides that teach AI agents how to write automations, select helpers, control devices, and safely refactor Home Assistant configurations. Skills are served as MCP resources (not auto-injected — clients must explicitly request them). The new **Webhook Proxy add-on** routes MCP traffic through existing reverse proxy setups with no separate tunnel or port forwarding needed. Stars doubled from 1,200 to 2,500 in six weeks.

### allenporter/mcp-server-home-assistant

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [allenporter/mcp-server-home-assistant](https://github.com/allenporter/mcp-server-home-assistant) | 55 | Python | Apache-2.0 | ~10 |

A Python-based Home Assistant MCP server that was being upstreamed into Home Assistant Core. Focused on clean, minimal integration.

### tdeckers/openhab-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [tdeckers/openhab-mcp](https://github.com/tdeckers/openhab-mcp) | <10 | Python | — | ~5-10 |

MCP server for **openHAB** — the other major open-source smart home platform. Interacts with openHAB via its REST API, enabling AI control of openHAB-managed devices. Lower adoption than Home Assistant servers but fills an important gap for openHAB users.

## Smart Home Devices

### tuya/tuya-mcp-sdk (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [tuya/tuya-mcp-sdk](https://github.com/tuya/tuya-mcp-sdk) | 10-20 | Python, Go, C# | Apache-2.0 | SDK |

Official SDK from **Tuya** — one of the world's largest IoT cloud platforms powering thousands of smart device brands. Provides Python, Go, and **C# SDKs** (C# added March 2026) for integrating Tuya Cloud capabilities with AI agents via MCP. Tuya's AI Agent Development Platform now fully supports MCP server integration, with official MCP tools continuously expanding. This is significant: Tuya powers devices from hundreds of white-label brands, so this SDK potentially reaches millions of devices.

A community-built **Tuya Smart Home MCP Server** (4,500+ downloads) adds local control via tinytuya, communicating directly over Wi-Fi for lower latency and better privacy. Offers 10 tools for complete device control (on/off, brightness, color, temperature, custom commands) with Claude, ChatGPT, Copilot, and Cursor compatibility.

### rmrfslashbin/hue-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [rmrfslashbin/hue-mcp](https://github.com/rmrfslashbin/hue-mcp) | 10-20 | Go | — | 15+ |

Modern MCP server for **Philips Hue** lighting systems. Supports multi-bridge control, real-time sync, cached responses, and comprehensive tools for lights, rooms, scenes, and bridges. The Go implementation is notable — most IoT MCP servers are Python.

### ykhli/mcp-light-control

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ykhli/mcp-light-control](https://github.com/ykhli/mcp-light-control) | ~10 | TypeScript | — | ~5 |

Philips Hue light control for Cursor and Claude Desktop — including the ability to send messages through lights using **Morse code**. A creative demonstration of AI-hardware interaction.

### thomasvincent/home-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [thomasvincent/home-mcp](https://github.com/thomasvincent/home-mcp) | <10 | Swift/TypeScript | — | ~5-10 |

MCP server for **Apple Home** on macOS. Controls HomeKit devices, scenes, and automations via MCP. The only MCP server targeting the Apple HomeKit ecosystem directly.

## IoT Platforms

### thingsboard/thingsboard-mcp (Official — Most Tools)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [thingsboard/thingsboard-mcp](https://github.com/thingsboard/thingsboard-mcp) | 20-50 | Python | Apache-2.0 | 120+ |

Official MCP server from **ThingsBoard** — the most popular open-source IoT platform. With **120+ tools**, this has the highest tool count of any server in the IoT/embedded category. Connects AI agents to the full ThingsBoard lifecycle: querying devices, managing entities, analyzing telemetry, creating dashboards, and automating operations.

The breadth is impressive — this is a full-stack IoT management interface exposed through MCP. From device provisioning to telemetry analytics, AI agents get access to everything ThingsBoard offers.

### ThingsPanel/thingspanel-mcp (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ThingsPanel/thingspanel-mcp](https://github.com/ThingsPanel/thingspanel-mcp) | 5-10 | Python | Apache-2.0 | ~10-15 |

Official MCP server from **ThingsPanel** — another open-source IoT platform. Supports MQTT and Modbus devices with integration for Claude and GPT models.

### AWS IoT SiteWise MCP (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [awslabs/mcp — IoT SiteWise](https://github.com/awslabs/mcp) | Part of 8.5K | Python | Apache-2.0 | 20+ |

Official AWS MCP server for **IoT SiteWise** — AWS's industrial IoT service. Provides **20+ tools** for asset management, data ingestion, monitoring, analytics, and time-series aggregations. Part of the awslabs/mcp monorepo (8.5K stars).

This is the strongest industrial IoT offering from a cloud provider. IoT SiteWise is designed for manufacturing, energy, and infrastructure monitoring — having AI agents query and analyze this data through MCP is a meaningful use case.

### Duke-CEI-Center/IoT-MCP-Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Duke-CEI-Center/IoT-MCP-Servers](https://github.com/Duke-CEI-Center/IoT-MCP-Servers) | <10 | Python | — | ~10 |

Academic IoT MCP server from **Duke University**. Reads sensor data and dispatches data collection tasks for AI assistants. Interesting as an academic perspective on AI-IoT integration.

## MQTT

MQTT is the dominant messaging protocol in IoT — lightweight, pub/sub, designed for constrained networks. Multiple MCP servers bridge AI agents to MQTT brokers.

### ezhuk/mqtt-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ezhuk/mqtt-mcp](https://github.com/ezhuk/mqtt-mcp) | 5-15 | Python | — | ~5 |

Lightweight MCP server connecting LLM agents to MQTT devices. Designed for **building automation**, **industrial control**, and **smart home** systems. Uses FastMCP 2.0 for clean integration.

### Benniu/emqx-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Benniu/emqx-mcp-server](https://github.com/Benniu/emqx-mcp-server) | 5-10 | Python | — | ~10 |

MCP server for **EMQX** — the most popular open-source MQTT broker. Supports both EMQX Cloud and self-hosted clusters, giving AI agents access to MQTT message streams and broker management.

### CorefluxCommunity/Coreflux-MQTT-MCP-Server (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [CorefluxCommunity/Coreflux-MQTT-MCP-Server](https://github.com/CorefluxCommunity/Coreflux-MQTT-MCP-Server) | ~2 | Python | — | 15+ |

Enterprise-grade MCP server from **Coreflux** for their MQTT broker. Full TLS support, API access, AI code generation, and health monitoring. **15+ tools** make this the most feature-rich MQTT-specific MCP server.

### tspspi/mcpMQTT

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [tspspi/mcpMQTT](https://github.com/tspspi/mcpMQTT) | <10 | Python | — | ~5 |

Generic MQTT interface for LLM orchestrators with fine-grained topic permissions using wildcard matching. Security-conscious design for multi-tenant MQTT environments.

### mqtt-ai/mcp-over-mqtt

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mqtt-ai/mcp-over-mqtt](https://github.com/mqtt-ai/mcp-over-mqtt) | 10-20 | TypeScript/Python | — | Transport layer |

Not a tool server per se — this is an **MCP-over-MQTT transport specification**. Enables MCP to run over MQTT with built-in service registry, discovery, and load balancing. Could be significant for deploying MCP in IoT environments where HTTP isn't practical.

## ESP32, Arduino, and Embedded Frameworks

The embedded MCP space has transformed since our original review. **Espressif** — the company behind ESP32 — has made the strongest vendor commitment of any hardware manufacturer to MCP, with four official efforts shipping in early 2026.

### espressif/esp-claw (Official — AI Agent Framework)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [espressif/esp-claw](https://github.com/espressif/esp-claw) | 304 | C/Lua | Apache-2.0 | Framework |

The headline addition. ESP-Claw is Espressif's official **"Chat Coding" AI agent framework** for ESP32 devices. It acts as **both MCP server and client** — exposing hardware capabilities to external agents while calling external services. Devices self-declare capabilities via MCP, replacing per-device adapters.

Key features: **on-device memory** (structured long-term memory lives on-chip, preferences and routines auto-extracted from conversations, events never leaving the device), **Chat Coding** (define device behavior through natural conversation, with LLM handling dynamic decisions and local Lua scripts executing deterministically even offline), and support for OpenAI, Anthropic, DeepSeek, Qwen, and custom LLM endpoints.

Requires 8MB Flash + 8MB PSRAM. Currently supports ESP32-S3, with ESP32-P4 coming soon. M5Stack has already forked it for their device line.

### ESP-IDF 6.0 Built-in MCP Server (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| ESP-IDF 6.0 MCP Server | Part of ESP-IDF | Python | Apache-2.0 | ~8 |

ESP-IDF 6.0, released March 2026, ships with a **built-in MCP server** for development workflows. Tools cover building, flashing, setting the target, and cleaning, plus resources for querying project configuration, build status, and connected devices. Launched via `eim run` using the new ESP-IDF Installation Manager. Particularly useful for IDE-based AI agents (VS Code Copilot, Cursor) that run outside an active ESP-IDF environment.

This is significant: the official embedded development framework for the world's most popular IoT microcontroller now includes MCP as a first-class feature.

### espressif/esp-rainmaker-mcp (Official — IoT Device Control)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [espressif/esp-rainmaker-mcp](https://github.com/espressif/esp-rainmaker-mcp) | 9 | Python | Apache-2.0 | ~10 |

Official MCP wrapper for **ESP RainMaker** — Espressif's cloud IoT platform. Bridges MCP clients with the RainMaker CLI, enabling natural language control of IoT devices, parameter reading, and schedule modification via Claude, Cursor, Gemini CLI, and Windsurf.

### Espressif Documentation MCP Server (Official)

Espressif also ships a **Documentation MCP server** (April 2026) that retrieves public Espressif documentation and supplies it as context for AI agents working with ESP chips and ESP SDKs. Read-only — does not execute code or modify files.

### 78/xiaozhi-esp32 (MCP-Based Chatbot — 24K Stars)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [78/xiaozhi-esp32](https://github.com/78/xiaozhi-esp32) | 24,000 | C/C++ | — | MCP client |

By far the most starred project in the IoT MCP space. Xiaozhi is an open-source MCP-based chatbot running on ESP32 hardware, designed as a personalized AI assistant using low-cost hardware. Uses **cloud-side MCP** to extend LLM capabilities including smart home control, PC desktop operation, knowledge search, and email. Built on ESP-IDF.

While technically an MCP client rather than server, its 24K stars and active community make it the most visible demonstration of MCP in the embedded world. A companion project, mac8005/xiaozhi-mcp-ha, integrates it with Home Assistant.

### horw/esp-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [horw/esp-mcp](https://github.com/horw/esp-mcp) | 150 | Python | MIT | ~5 |

The original community ESP-IDF MCP server, now complemented by ESP-IDF 6.0's official built-in server. Centralizes **ESP-IDF** commands for AI-driven interaction — build, flash, and automatic issue fixing. Still useful as a more flexible alternative to the official built-in server.

### MicroPython MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| MicroPython MCP Bridge | — | Python | — | ~5 |

New in April 2026 — an MCP bridge server allowing direct code execution from an LLM on any board running **MicroPython** (ESP32, RP2040, etc.) via USB Serial or WebREPL. Compatible with Claude Desktop, VS Code Codex, Copilot, and Antigravity. This fills an important gap — MicroPython runs on far more boards than ESP-IDF, making MCP accessible to a broader embedded audience.

### solnera/esp32-mcpserver

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [solnera/esp32-mcpserver](https://github.com/solnera/esp32-mcpserver) | — | C++ (Arduino) | — | Framework |

A lightweight MCP server framework for ESP32, available on **PlatformIO** (the embedded package manager). Seamlessly connects embedded devices to LLMs via WebSocket/JSON-RPC. Designed as a framework — developers build custom tools for their specific hardware.

### navado/ESP32MCPServer

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [navado/ESP32MCPServer](https://github.com/navado/ESP32MCPServer) | <10 | C++ (Arduino) | — | ~5 |

MCP running **directly on ESP32 hardware**. Provides a WebSocket-based interface for resource discovery and monitoring. Supports NMEA2k, OBD/ODBII, and NMEA0183 sensor data.

### ertgtct/mcpesp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ertgtct/mcpesp](https://github.com/ertgtct/mcpesp) | <10 | C++ (Arduino) | — | Library |

Arduino library for implementing MCP servers on ESP32. Exposes hardware capabilities as MCP tools via HTTP/JSON-RPC. Developers can create custom tools for their specific hardware configurations.

### Serial Communication Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp2everything/mcp2serial](https://github.com/mcp2everything/mcp2serial) | 33 | Python | MIT | ~5-10 |
| [Adancurusul/serial-mcp-server](https://github.com/Adancurusul/serial-mcp-server) | 10-20 | Python | — | 10+ |
| [bmdragos/serial-mcp](https://github.com/bmdragos/serial-mcp) | <10 | Python | — | ~3-5 |

Three serial communication MCP servers for talking to Arduino, ESP32, and other hardware over USB serial. **mcp2serial** (33 stars) leads with initial Raspberry Pi Pico support. **serial-mcp-server** provides the most comprehensive serial capabilities including professional debugging features. **serial-mcp** offers a minimal implementation built specifically for Claude Code.

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

This is the server that turns a Raspberry Pi into a fully AI-controllable device.

### UnitApi/mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [UnitApi/mcp](https://github.com/UnitApi/mcp) | 5-10 | Python | — | 10+ |

Secure hardware control through MCP with real-time GPIO streaming. Supports LED control, button input, and sensor operations on Raspberry Pi.

## Robotics (ROS)

### robotmcp/ros-mcp-server (Most Starred IoT MCP Server)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [robotmcp/ros-mcp-server](https://github.com/robotmcp/ros-mcp-server) | 1,200 | Python | Apache-2.0 | 15+ |

The most starred IoT MCP server — and for good reason. Provides **bidirectional AI-robot communication** across both ROS1 and ROS2:

- **Natural language → robot commands** — AI translates user intent into ROS topic publications, service calls, and action goals
- **Robot state → AI understanding** — full visibility into robot topics, transforms, and sensor data
- **Works with Claude, GPT, Gemini, and more** — compatible with Claude Code, Codex CLI, Gemini CLI, Claude Desktop, ChatGPT, Cursor, and other MCP clients

Jumped from 873 to 1,200 stars (+37%) since our last review. The robotics community's interest in AI-controlled physical systems through MCP continues to accelerate.

### wise-vision/ros2_mcp (NEW — Production-Ready ROS2)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [wise-vision/ros2_mcp](https://github.com/wise-vision/ros2_mcp) | 73 | Python | — | 10+ |

An advanced ROS 2 MCP server that bridges AI agents directly into robotics. Notable features:

- **1-minute setup** — zero-friction configuration using stdio transport with no brokers or webserver
- **Auto type discovery** — built-in "list interfaces" tool that dynamically enumerates available topics and services
- **Image streaming** — supports Image and CompressedImage message types, enabling MCP to receive image streams from ROS2 topics
- **Full action support** — complete tools for handling ROS2 Actions
- **Drone demo** — includes documentation for natural language drone control

Positioned as a production-ready, general-purpose AI integration for ROS2. The auto-discovery and image streaming features make it particularly valuable for rapid prototyping.

### lpigeon/ros-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [lpigeon/ros-mcp-server](https://github.com/lpigeon/ros-mcp-server) | 50-100 | Python | — | ~10 |

Another ROS/ROS2 MCP server focused on transforming natural language into robot commands. Lower star count than robotmcp but still actively maintained.

### Additional ROS Servers

| Server | Stars | Language | Description |
|--------|-------|----------|-------------|
| [kakimochi/ros2-mcp-server](https://github.com/kakimochi/ros2-mcp-server) | <10 | Python | ROS 2 velocity commands via /cmd_vel |
| [TakanariShimbo/rosbridge-mcp-server](https://github.com/TakanariShimbo/rosbridge-mcp-server) | <10 | Python | ROS via rosbridge WebSocket |

## Industrial IoT — OPC UA, PLCs, and SCADA

### kukapay/opcua-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [kukapay/opcua-mcp](https://github.com/kukapay/opcua-mcp) | <10 | Python | — | ~5 |

MCP server connecting to **OPC UA**-enabled industrial systems. Reads and writes OPC UA node values — the standard protocol for factory floor communication. Enables AI agents to query and control industrial equipment through the same protocol used by SCADA systems.

### midhunxavier/OPCUA-MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [midhunxavier/OPCUA-MCP](https://github.com/midhunxavier/OPCUA-MCP) | <10 | Python, TypeScript | — | ~10 |

More comprehensive OPC UA server with both Python and TypeScript implementations. Supports read/write variables, browse nodes, call methods, and batch operations.

### cadugrillo/s7-mcp-bridge

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cadugrillo/s7-mcp-bridge](https://github.com/cadugrillo/s7-mcp-bridge) | <10 | Go | — | ~5-10 |

MCP server connecting AI agents to **Siemens S7-1500 and S7-1200 PLCs** — the world's most widely deployed programmable logic controllers. The Go implementation communicates using the S7 protocol for direct PLC data access.

This is early-stage but potentially significant: Siemens PLCs run a large portion of global manufacturing. Having AI agents read PLC variables through MCP could enable intelligent manufacturing monitoring.

### poly-mcp/IoT-Edge-MCP-Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [poly-mcp/IoT-Edge-MCP-Server](https://github.com/poly-mcp/IoT-Edge-MCP-Server) | <10 | Python | — | 15-20 |

Enterprise-grade MCP server for Industrial IoT. Unifies **MQTT sensors**, **Modbus devices**, and industrial equipment with InfluxDB time-series storage and Redis caching. Features real-time monitoring, alarms, and actuator control — the closest thing to a SCADA MCP interface.

## 3D Printing

### DMontgomery40/mcp-3D-printer-server (Tripled to 168 Stars)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [DMontgomery40/mcp-3D-printer-server](https://github.com/DMontgomery40/mcp-3D-printer-server) | 168 | JavaScript/TypeScript | GPL-2.0 | 25+ |

The most comprehensive 3D printing MCP server — and the fastest-growing in the category, tripling from 61 to 168 stars. Connects to **8 printer platforms**: OrcaSlicer, Bambu Lab, OctoPrint, Klipper, Duet, Repetier, Prusa, and Creality.

**Recent updates** add significant capabilities: **Bambu FTP-backed file operations**, **OrcaSlicer CLI slicing** (via `slice_stl` tool), new mesh preparation tools (`merge_vertices`, `center_model`, `lay_flat`), and support for reading **Bambu Studio preset files** (machine, filament, process) as MCP resources. The project aims for feature parity across all platforms, with Bambu implementation leading.

Also available on Docker Hub and npm for easy deployment.

### OctoEverywhere/mcp (Official)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [OctoEverywhere/mcp](https://github.com/OctoEverywhere/mcp) | 20-50 | Python | — | ~5 |

Official MCP server from **OctoEverywhere** — the most popular cloud management platform for 3D printers. Supports OctoPrint, Klipper, Bambu Lab, Elegoo, Prusa, and Creality. Provides live printer state, webcam snapshots, and printer control.

The official backing means reliable API access and ongoing maintenance.

### schwarztim/bambu-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [schwarztim/bambu-mcp](https://github.com/schwarztim/bambu-mcp) | 10-20 | TypeScript | MIT | 25 |

Complete MCP server for **Bambu Lab** 3D printers. **25 tools** covering print control, status monitoring, camera access, AMS (Automatic Material System), temperature monitoring, and LED control. Uses local MQTT for communication with X.509 certificate authentication and FTPS file upload.

## Other Notable Servers

### Drone Control

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [0xKoda/drone-mcp](https://github.com/0xKoda/drone-mcp) | <10 | Python | — | ~5-10 |

MCP server for controlling **DJI Tello** drones — takeoff, landing, movement commands, and video streaming through MCP.

### Bluetooth

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Hypijump31/bluetooth-mcp-server](https://github.com/Hypijump31/bluetooth-mcp-server) | 14 | Python | — | 1 |

Bluetooth device scanning and interaction for AI assistants. Supports both BLE and Classic Bluetooth on Windows, macOS, and Linux.

### Zigbee2MQTT

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ichbinder/MCP2ZigBee2MQTT](https://github.com/ichbinder/MCP2ZigBee2MQTT) | <10 | Python | — | ~5-10 |

MCP server for **Zigbee2MQTT** with intelligent device discovery. Auto-analyzes all connected Zigbee devices and exposes their capabilities.

### Node-RED Integration

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [TobiasLante/node-red-contrib-mcp](https://github.com/TobiasLante/node-red-contrib-mcp) | 10-20 | JavaScript | — | Node-RED nodes |
| [karavaev-evgeniy/node-red-mcp-server](https://github.com/karavaev-evgeniy/node-red-mcp-server) | <10 | JavaScript | — | ~10 |

Two approaches to **Node-RED** MCP integration: node-red-contrib-mcp adds MCP nodes to Node-RED's visual flow editor for manufacturing and IoT automation, while node-red-mcp-server lets AI agents manage Node-RED flows, nodes, and settings.

### Sensor Monitoring

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [diegobit/aranet4-mcp-server](https://github.com/diegobit/aranet4-mcp-server) | <10 | Python | — | ~5 |

MCP server for the **Aranet4 CO2 sensor**. Scans for devices, fetches data, stores in local SQLite, and provides historical querying with visualization. A niche but well-implemented example of purpose-built sensor MCP integration.

## Curated Resources

**[beriberikix/awesome-mcp-hardware](https://github.com/beriberikix/awesome-mcp-hardware)** — A curated awesome-list specifically for MCP servers interacting with hardware and the physical world. Good reference for discovering new IoT/embedded MCP servers as they emerge.

## What's missing

The gap list is shorter than in March, but significant holes remain:

- **No official Arduino IDE integration** — the most popular embedded development platform has no MCP server for project management, board configuration, or compilation (though ESP-IDF 6.0's built-in MCP server partially addresses this for Espressif chips)
- **No major Zigbee/Z-Wave hub vendors** — Samsung SmartThings, Hubitat, and Aeotec have no official MCP servers
- **No PLC vendor servers** — Siemens, Allen-Bradley (Rockwell), Mitsubishi, and ABB have no official MCP offerings (only community bridges)
- **No Matter/Thread protocol servers** — the new smart home standard has no dedicated MCP support (accessible indirectly through Home Assistant)
- **No LoRaWAN servers** — the dominant LPWAN technology for IoT remains absent from the MCP ecosystem
- **No edge AI servers** — no MCP integration for TensorFlow Lite, ONNX Runtime, or other edge inference frameworks (ESP-Claw's on-device inference is closest)
- **Limited sensor aggregation** — individual sensor servers exist but no unified multi-sensor hub

## The bottom line

**Rating: 4.0/5** — The IoT/embedded MCP ecosystem has grown significantly since our March review. Ten or more vendors now provide official servers, up from seven — with Espressif's four-pronged MCP commitment being the biggest single vendor story in the entire IoT category. Robotics leads in adoption with 1,200 stars on the top server. Smart home has the most options, with ha-mcp doubling to 2,500 stars. The embedded chatbot space exploded with xiaozhi-esp32 at 24K stars. 3D printing tripled in adoption.

The real story is that AI-hardware interaction through MCP has moved from "interesting experiment" to "vendor-supported infrastructure." Espressif shipping MCP in ESP-IDF 6.0 means every new ESP32 project has MCP available out of the box. ESP-Claw running as both MCP server and client on-device — with on-chip memory and offline Lua execution — shows where this is heading: AI agents that live on the hardware itself. The 55+ servers now span consumer smart homes, industrial factories, 3D printers, drones, robots, and embedded chatbots. The remaining gaps are in vendor adoption (where are Siemens, Arduino, and SmartThings officially?), emerging standards (Matter, LoRaWAN), and edge AI inference.

*This review was refreshed on 2026-04-26 using Claude Opus 4.6 (Anthropic). Originally published 2026-03-15.*

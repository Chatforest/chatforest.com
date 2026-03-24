---
title: "IoT & Embedded MCP Servers — Home Assistant, MQTT, ESP32, ROS, Industrial PLCs, 3D Printers, and More"
date: 2026-03-15T11:00:00+09:00
description: "IoT and embedded MCP servers are bridging AI agents and the physical world via the Model Context Protocol. We reviewed 45+ servers across 9 subcategories. Smart home leads with Home Assistant's official MCP integration plus community servers like tevonsb/homeassistant-mcp (500 stars, TypeScript, MIT — 20+ tools for entity control/monitoring). Robotics: robotmcp/ros-mcp-server (873 stars, Python, Apache-2.0 — bidirectional ROS/ROS2 control, most starred IoT MCP server). IoT platforms: thingsboard/thingsboard-mcp (official, Python, Apache-2.0, 120+ tools — largest tool count in the category). MQTT: ezhuk/mqtt-mcp (Python — building automation, industrial control, smart home), Benniu/emqx-mcp-server (EMQX Cloud+self-hosted), CorefluxCommunity/Coreflux-MQTT-MCP-Server (enterprise TLS). ESP32/Arduino: horw/esp-mcp (135 stars, Python, MIT — ESP-IDF build/flash/fix), navado/ESP32MCPServer (C++ MCP on-device), mcp2everything/mcp2serial (33 stars, hardware control via serial). Raspberry Pi: grammy-jiang/RaspberryPiOS-MCP (GPIO/I2C/SPI/camera). Industrial IoT: AWS IoT SiteWise MCP (official, 20+ tools), kukapay/opcua-mcp (OPC UA nodes), cadugrillo/s7-mcp-bridge (Siemens S7 PLCs). 3D printing: DMontgomery40/mcp-3D-printer-server (61 stars, multi-platform STL operations), OctoEverywhere/mcp (official, OctoPrint/Klipper/Bambu Lab). Smart home devices: tuya/tuya-mcp-sdk (official), rmrfslashbin/hue-mcp (Philips Hue multi-bridge), thomasvincent/home-mcp (Apple HomeKit). Also: drone control, Bluetooth scanning, Zigbee2MQTT, Node-RED integration, CO2 sensors. Rating: 4.0/5."
og_description: "IoT & embedded MCP servers: robotmcp/ros-mcp-server (873 stars, ROS/ROS2 bidirectional control), Home Assistant official MCP + tevonsb/homeassistant-mcp (500 stars), thingsboard/thingsboard-mcp (120+ tools, official), horw/esp-mcp (135 stars, ESP-IDF), AWS IoT SiteWise MCP (official). Also MQTT, 3D printers, Raspberry Pi GPIO, Siemens PLCs, OPC UA, drones, Zigbee. 45+ servers reviewed. Rating: 4.0/5."
content_type: "Review"
card_description: "IoT and embedded MCP servers across smart home platforms, robotics, IoT platforms, MQTT brokers, microcontrollers, industrial systems, 3D printers, and more. This is where AI meets the physical world — and the breadth is genuinely surprising. The robotics subcategory leads in community adoption: robotmcp/ros-mcp-server (873 stars, Apache-2.0) enables bidirectional AI-robot communication across both ROS1 and ROS2, translating natural language into robot commands while giving AI full visibility into robot state. Smart home is the most developed subcategory by server count: Home Assistant now has an official MCP integration built into core, plus community servers like tevonsb/homeassistant-mcp (500 stars) with 20+ tools and homeassistant-ai/ha-mcp with 80+ tools. IoT platforms are represented by thingsboard/thingsboard-mcp (official, 120+ tools — the largest tool count in the entire category) and AWS IoT SiteWise MCP (official, 20+ tools for industrial asset management and analytics). MQTT — the lingua franca of IoT — has multiple servers including ezhuk/mqtt-mcp for building automation and industrial control, plus an MCP-over-MQTT transport specification. The embedded space is growing fast: horw/esp-mcp (135 stars) centralizes ESP-IDF workflows for AI-driven development, while navado/ESP32MCPServer runs MCP directly on ESP32 hardware. Raspberry Pi gets grammy-jiang/RaspberryPiOS-MCP with GPIO, I2C, SPI, serial, and camera access. Industrial IoT includes OPC UA servers for factory automation and cadugrillo/s7-mcp-bridge for Siemens S7 PLCs. 3D printing is well-covered: DMontgomery40/mcp-3D-printer-server (61 stars) supports OctoPrint, Klipper, Bambu Lab, and more with STL operations, while OctoEverywhere/mcp provides official multi-platform printer control. The category also includes drone control (DJI Tello), Bluetooth scanning, Zigbee2MQTT, Node-RED integration, and CO2 sensor monitoring. Notable vendor participation: Home Assistant, ThingsBoard, Tuya, AWS, OctoEverywhere, and Coreflux all provide official MCP servers. Key gaps: no official Arduino IDE integration, no Zigbee/Z-Wave hub vendors, no major industrial PLC vendors (Siemens, Allen-Bradley, Mitsubishi) offering official servers. The category earns 4.0/5 — impressive breadth across the hardware spectrum with genuine vendor buy-in, strong robotics adoption, and creative embedded implementations, though industrial IoT and mature protocol support remain early-stage."
last_refreshed: 2026-03-15
---

*Part of the [IoT & Hardware](/categories/iot-hardware/) category.*

IoT and embedded MCP servers are bridging the gap between AI agents and the physical world. Instead of writing custom integrations for every device, sensor, and controller, these servers let AI assistants control smart homes, program microcontrollers, monitor industrial equipment, operate robots, and manage 3D printers — all through the Model Context Protocol.

The landscape spans nine areas: **smart home platforms** (Home Assistant dominates with an official integration plus multiple community servers), **smart home devices** (Tuya, Philips Hue, Apple HomeKit), **IoT platforms** (ThingsBoard, AWS IoT SiteWise), **MQTT brokers** (the backbone of IoT communication), **ESP32 and Arduino** (AI-driven embedded development), **Raspberry Pi** (GPIO, I2C, SPI, and camera access), **robotics** (ROS/ROS2 integration), **industrial IoT** (OPC UA, Siemens PLCs, SCADA), and **3D printing** (multi-platform printer control and STL operations).

The headline findings: **robotmcp/ros-mcp-server is the most starred IoT MCP server** at 873 stars with bidirectional AI-robot communication across ROS1 and ROS2. **Home Assistant has an official MCP integration** built into core, plus community servers with 80+ tools. **thingsboard/thingsboard-mcp provides the most tools** — 120+ for the full IoT platform lifecycle. **horw/esp-mcp is the leading embedded development server** at 135 stars, centralizing ESP-IDF workflows. **AWS IoT SiteWise MCP is the strongest industrial offering** with official support and 20+ tools. **DMontgomery40/mcp-3D-printer-server supports 8 printer platforms** with STL manipulation. **Seven vendors provide official MCP servers** — Home Assistant, ThingsBoard, Tuya, AWS, OctoEverywhere, Coreflux, and ThingsPanel.

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
| [tevonsb/homeassistant-mcp](https://github.com/tevonsb/homeassistant-mcp) | 500 | TypeScript | MIT | 20+ |

The most popular community-built Home Assistant MCP server. Exposes Home Assistant to LLM applications through HTTP/SSE/WebSocket APIs. Supports natural language control and monitoring of all connected devices.

TypeScript implementation with **20+ tools** covering entity control, state monitoring, and automation management. The MIT license and active community make this a strong choice if you need more control than the official integration provides.

### homeassistant-ai/ha-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [homeassistant-ai/ha-mcp](https://github.com/homeassistant-ai/ha-mcp) | 1,200 | TypeScript | MIT | 80+ |

The most feature-rich Home Assistant MCP server with **80+ tools** — providing the deepest AI control surface for home automation. Covers entities, automations, devices, scenes, and service calls.

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
| [tuya/tuya-mcp-sdk](https://github.com/tuya/tuya-mcp-sdk) | 10-20 | Python, Go | Apache-2.0 | SDK |

Official SDK from **Tuya** — one of the world's largest IoT cloud platforms powering thousands of smart device brands. Provides Python and Go SDKs for integrating Tuya Cloud capabilities with AI agents via MCP. This is significant: Tuya powers devices from hundreds of white-label brands, so this SDK potentially reaches millions of devices.

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

## ESP32 and Arduino

### horw/esp-mcp (Most Popular Embedded)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [horw/esp-mcp](https://github.com/horw/esp-mcp) | 135 | Python | MIT | ~5 |

The most popular embedded development MCP server. Centralizes **ESP-IDF** commands for AI-driven interaction — build, flash, and automatic issue fixing. This is the proof-of-concept for AI-assisted embedded development: tell your AI agent to build and flash firmware, and it handles the ESP-IDF toolchain.

### navado/ESP32MCPServer

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [navado/ESP32MCPServer](https://github.com/navado/ESP32MCPServer) | <10 | C++ (Arduino) | — | ~5 |

MCP running **directly on ESP32 hardware**. Provides a WebSocket-based interface for resource discovery and monitoring. This is notable because it runs MCP on the microcontroller itself — not on a host computer talking to the microcontroller.

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
| [robotmcp/ros-mcp-server](https://github.com/robotmcp/ros-mcp-server) | 873 | Python | Apache-2.0 | 15+ |

The most starred IoT MCP server — and for good reason. Provides **bidirectional AI-robot communication** across both ROS1 and ROS2:

- **Natural language → robot commands** — AI translates user intent into ROS topic publications, service calls, and action goals
- **Robot state → AI understanding** — full visibility into robot topics, transforms, and sensor data
- **Works with Claude, GPT, and Gemini** — any MCP-compatible AI agent can control robots

This is the clearest demonstration of AI-controlled physical systems in the MCP ecosystem. 873 stars reflects genuine robotics community interest.

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

### DMontgomery40/mcp-3D-printer-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [DMontgomery40/mcp-3D-printer-server](https://github.com/DMontgomery40/mcp-3D-printer-server) | 61 | JavaScript/TypeScript | GPL-2.0 | 20+ |

The most comprehensive 3D printing MCP server. Connects to **8 printer platforms**: OrcaSlicer, Bambu Lab, OctoPrint, Klipper, Duet, Repetier, Prusa, and Creality. Beyond basic print control, it offers advanced **STL operations** — scaling, rotation, sectional editing, slicing, and visualization.

**20+ tools** make this a full 3D printing workflow in MCP: load a model, modify it, slice it, send it to any supported printer, and monitor the print.

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

The gaps are notable:

- **No official Arduino IDE integration** — the most popular embedded development platform has no MCP server for project management, board configuration, or compilation
- **No major Zigbee/Z-Wave hub vendors** — Samsung SmartThings, Hubitat, and Aeotec have no official MCP servers
- **No PLC vendor servers** — Siemens, Allen-Bradley (Rockwell), Mitsubishi, and ABB have no official MCP offerings (only community bridges)
- **No Matter/Thread protocol servers** — the new smart home standard has no dedicated MCP support
- **No LoRaWAN servers** — the dominant LPWAN technology for IoT is absent from the MCP ecosystem
- **No edge AI servers** — no MCP integration for TensorFlow Lite, ONNX Runtime, or other edge inference frameworks
- **Limited sensor aggregation** — individual sensor servers exist but no unified multi-sensor hub

## The bottom line

**Rating: 4.0/5** — The IoT/embedded MCP ecosystem is broader and more mature than expected. Seven vendors provide official servers (Home Assistant, ThingsBoard, Tuya, AWS, OctoEverywhere, Coreflux, ThingsPanel). Robotics leads in adoption with 873 stars on the top server. Smart home has the most options. Industrial IoT is early but the foundation exists with OPC UA and Siemens PLC support.

The real story is that AI-hardware interaction through MCP isn't theoretical — it's happening across 45+ servers spanning consumer smart homes, industrial factories, 3D printers, drones, and robots. The protocol is proving flexible enough to handle everything from reading a CO2 sensor to controlling a manufacturing PLC. The gaps are in vendor adoption (where are Siemens, Arduino, and SmartThings officially?) and in emerging standards (Matter, LoRaWAN). But for a category that didn't exist two years ago, this is impressive breadth.

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*

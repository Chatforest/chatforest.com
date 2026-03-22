---
title: "Best IoT MCP Servers in 2026"
date: 2026-03-22T23:30:00+09:00
description: "Home Assistant, MQTT, AWS IoT, ESP32, Apple HomeKit, industrial IoT, and more — we've reviewed 40+ IoT MCP servers across 10 categories. Here's what works, what's emerging, and where the gaps are."
og_description: "40+ IoT MCP servers reviewed across Home Assistant, MQTT, AWS IoT, ESP32, industrial protocols, and smart home platforms. The definitive comparison with honest ratings."
content_type: "Comparison"
card_description: "The definitive guide to IoT MCP servers in 2026. We've reviewed 40+ servers across Home Assistant (5+ implementations), MQTT, AWS IoT SiteWise, ESP32/Arduino, industrial protocols (Modbus, OPC UA), Apple HomeKit, ThingsBoard, Node-RED, and smart lighting. Every recommendation links to a full review."
last_refreshed: 2026-03-22
---

IoT is where MCP servers get physical. Instead of managing databases or deploying code, these servers control lights, read sensors, manage industrial equipment, and orchestrate smart homes — all through natural language. The category spans everything from a Raspberry Pi temperature sensor to AWS-scale industrial asset monitoring.

We've researched 40+ IoT MCP servers across the full landscape. This guide covers what's production-ready, what's experimental, and where significant gaps remain.

*Note: Our recommendations are based on documentation review, GitHub analysis, and community feedback — not hands-on testing of every server. Star counts were verified in March 2026.*

## The short version

| Category | Our pick | Stars | Runner-up |
|----------|----------|-------|-----------|
| Home Assistant | [homeassistant-ai/ha-mcp](https://github.com/homeassistant-ai/ha-mcp) | 1,700 | [tevonsb/homeassistant-mcp](https://github.com/tevonsb/homeassistant-mcp) (557 stars) |
| MQTT | [ezhuk/mqtt-mcp](https://github.com/ezhuk/mqtt-mcp) | 12 | [Benniu/emqx-mcp-server](https://github.com/benniu/emqx-mcp-server) (23 stars, EMQX) |
| AWS IoT | [awslabs/mcp (IoT SiteWise)](https://github.com/awslabs/mcp/tree/main/src/aws-iot-sitewise-mcp-server) | 8,500* | — |
| IoT platform | [thingsboard/thingsboard-mcp](https://github.com/thingsboard/thingsboard-mcp) | 94 | [karavaev-evgeniy/node-red-mcp-server](https://github.com/karavaev-evgeniy/node-red-mcp-server) (31 stars) |
| ESP32 | [horw/esp-mcp](https://github.com/horw/esp-mcp) | 139 | [navado/ESP32MCPServer](https://github.com/navado/ESP32MCPServer) (38 stars) |
| Arduino / robotics | [vishalmysore/choturobo](https://github.com/vishalmysore/choturobo) | 75 | [Volt23/mcp-arduino-server](https://github.com/Volt23/mcp-arduino-server) (10 stars) |
| PlatformIO | [jl-codes/platformio-mcp](https://github.com/jl-codes/platformio-mcp) | 16 | — |
| Apple HomeKit | [omarshahine/HomeClaw](https://github.com/omarshahine/HomeClaw) | 64 | [grahamaloo/HomeKitMCP](https://github.com/grahamaloo/HomeKitMCP) (Swift native) |
| Industrial IoT | [poly-mcp/IoT-Edge-MCP-Server](https://github.com/poly-mcp/IoT-Edge-MCP-Server) | 22 | [kukapay/modbus-mcp](https://github.com/kukapay/modbus-mcp) (20 stars) |
| Smart lighting | [rmrfslashbin/hue-mcp](https://github.com/rmrfslashbin/hue-mcp) | 2 | [ykhli/mcp-light-control](https://github.com/ykhli/mcp-light-control) (21 stars, Hue + Morse code) |

*Monorepo star count; IoT SiteWise is one server within it.*

## Why IoT MCP servers matter

IoT device management is a pain. Different protocols (MQTT, Zigbee, Z-Wave, Matter), different platforms (Home Assistant, AWS, ThingsBoard), different APIs for every vendor. MCP servers collapse this complexity into conversational commands.

The value comes in three forms:

1. **Smart home control.** "Turn off all the lights downstairs" or "Set the thermostat to 20°C when I'm away" — instead of navigating through apps and dashboards. Home Assistant MCP servers make this natural.
2. **Industrial monitoring.** "Show me the temperature readings from sensor bank 3 over the last 24 hours" or "Are any alarms active on the production floor?" — agents query telemetry data, manage alarms, and monitor equipment without custom dashboards.
3. **Embedded development.** "Build and flash this firmware to the ESP32" or "Create a new PlatformIO project for the Arduino Mega" — MCP servers wrap development toolchains, making hardware projects accessible through AI assistants.

The landscape splits into ten categories: **Home Assistant** (the most mature, 5+ servers), **MQTT** (the protocol layer), **AWS IoT** (industrial-scale), **IoT platforms** (ThingsBoard, Node-RED, Tuya), **ESP32** (development + on-device), **Arduino/robotics** (hardware control), **PlatformIO** (board-agnostic development), **Apple HomeKit** (iOS ecosystem), **industrial IoT** (Modbus, OPC UA), and **smart lighting** (Hue, LIFX).

---

## Home Assistant servers

Home Assistant is the clear leader in smart home MCP integration. With 5+ competing servers and the most mature ecosystem, it's the safest entry point for AI-controlled smart homes.

### The winner: homeassistant-ai/ha-mcp

**Stars:** 1,700 | **Language:** Python | **License:** MIT | **Tools:** 96+

[homeassistant-ai/ha-mcp](https://github.com/homeassistant-ai/ha-mcp) is the most comprehensive Home Assistant MCP server by every metric: tool count, client compatibility, and community adoption. It covers search/discovery, device control, automation management, camera snapshots, ZHA (Zigbee Home Automation) devices, backups, add-ons, and dashboards. Supports Claude Desktop, Gemini, ChatGPT, VS Code, and Cursor. Includes OAuth (beta) and can be deployed as a Home Assistant OS add-on.

**Why it wins:** 96+ tools and 1,700 stars make it the most battle-tested option. The breadth is unmatched — from turning on a light to managing backups and ZHA devices. The HA OS add-on deployment means you don't need a separate server.

**The catch:** The sheer number of tools (96+) means high token consumption per request. If you only need basic device control, a lighter server might be more efficient.

**Best for:** Anyone who wants full Home Assistant coverage from an AI assistant.

### Runner-up: tevonsb/homeassistant-mcp

**Stars:** 557 | **Language:** TypeScript | **License:** MIT | **Tools:** 4 tool groups

[tevonsb/homeassistant-mcp](https://github.com/tevonsb/homeassistant-mcp) takes a more structured approach with four tool categories: Control, Addon, Package, and Automation. Supports lights, climate, locks, and cameras. Real-time updates via SSE, HACS integration, and Docker containerization. Claims 95% test coverage.

**Why it's notable:** TypeScript implementation with strong test coverage. The SSE transport means real-time device state updates — important for monitoring scenarios.

**Best for:** TypeScript-native teams who want a well-tested, structured alternative.

### Also notable

**[voska/hass-mcp](https://github.com/voska/hass-mcp)** (285 stars, Python, MIT, 11 tools + 7 prompts) — Token-efficient design with lean JSON responses. The 7 guided conversation prompts help with common tasks like "set up a new automation" or "diagnose a device." Best for users who want guided workflows rather than raw tool access.

**[jango-blockchained/advanced-homeassistant-mcp](https://github.com/jango-blockchained/advanced-homeassistant-mcp)** (48 stars, TypeScript, MIT, 34 tools) — Enterprise-grade security with JWT auth, rate limiting, and IP allowlisting. Unique Aurora sound-to-light synchronization feature. Runs on Bun runtime (claimed 4x faster than Node.js). Best for security-conscious deployments.

**[allenporter/mcp-server-home-assistant](https://github.com/allenporter/mcp-server-home-assistant)** (67 stars, Python, Apache 2.0) — Now archived. Its WebSocket-based approach contributed to the official Home Assistant Core MCP integration that's being developed. Worth noting for historical context: Home Assistant is working toward native MCP support in the core platform.

---

## MQTT servers

MQTT is the backbone protocol of IoT. These servers let AI agents publish messages to devices and subscribe to sensor data — the lowest-level but most flexible approach to IoT control.

### The winner: ezhuk/mqtt-mcp

**Stars:** 12 | **Language:** Python | **License:** MIT | **Tools:** 2 core + prompts/resources

[ezhuk/mqtt-mcp](https://github.com/ezhuk/mqtt-mcp) is a lightweight MCP server connecting AI agents to any MQTT broker. Two core tools: Receive Message and Publish Message. Supports building automation, industrial control, and smart home use cases. Docker-ready with AuthKit authentication. Actively maintained (v0.3.1, March 2026).

**Why it wins:** Simplicity and active maintenance. MQTT is inherently a publish/subscribe protocol — a 2-tool server that does pub/sub well is exactly right. The March 2026 update shows ongoing development.

**The catch:** Generic by design. You'll need to know your MQTT topic structure and message formats. No device-specific abstractions.

**Best for:** Developers who already have MQTT infrastructure and want to add AI agent access.

### Also notable

**[Benniu/emqx-mcp-server](https://github.com/benniu/emqx-mcp-server)** (23 stars, Python, Apache 2.0, 5 tools) — EMQX broker integration with client management, QoS control, message retention, and real-time SSE subscription. Supports both EMQX Cloud and self-hosted. Best for EMQX users.

**[tspspi/mcpMQTT](https://github.com/tspspi/mcpMQTT)** (1 star, Python, BSD-3-Clause, 4 tools) — Fine-grained topic-level access control with wildcard pattern matching. Supports stdio, HTTP, and Unix Domain Socket transports. Argon2id API key authentication. Best for security-sensitive MQTT deployments.

**[mqtt-ai/mcp-over-mqtt](https://github.com/mqtt-ai/mcp-over-mqtt)** — A different concept: uses MQTT as the transport layer for MCP itself, rather than controlling MQTT devices through MCP. Interesting for distributed agent architectures where MCP clients and servers communicate over MQTT.

---

## AWS IoT (industrial scale)

### The winner: awslabs/mcp — IoT SiteWise server

**Stars:** 8,500 (monorepo) | **Language:** Python | **License:** Apache 2.0 | **Tools:** 50+

[awslabs/mcp (IoT SiteWise)](https://github.com/awslabs/mcp/tree/main/src/aws-iot-sitewise-mcp-server) is the official AWS MCP server for industrial IoT asset management. Part of the AWS MCP monorepo (8,500+ stars). Covers asset hierarchies, real-time and historical data, bulk import/export, ML-powered anomaly detection, gateway management, and SQL-like queries. Built-in industrial knowledge with domain validation.

**Why it wins:** It's official AWS, backed by Amazon's engineering team. 50+ tools cover the full IoT SiteWise surface. ML anomaly detection is a standout — most IoT MCP servers just read data, this one actively identifies problems. The industrial best practices built into domain validation prevent common configuration mistakes.

**The catch:** AWS-only. Requires IoT SiteWise setup, which is a significant investment. Overkill for hobbyist or small-scale IoT.

**Best for:** Enterprise teams already on AWS who need AI-assisted industrial IoT management.

**Azure IoT gap:** No dedicated Azure IoT Hub or Digital Twins MCP server exists yet. IoT operations on Azure go through the general [microsoft/mcp](https://github.com/microsoft/mcp) server or Azure CLI.

**Google IoT gap:** No actively maintained Google Home/Nest MCP server exists. This is a significant gap given Google's smart home market share.

---

## IoT platform servers

### The winner: thingsboard/thingsboard-mcp

**Stars:** 94 | **Language:** Java 17+ | **License:** Apache 2.0 | **Tools:** 120+

[thingsboard/thingsboard-mcp](https://github.com/thingsboard/thingsboard-mcp) is the official ThingsBoard MCP server with the highest tool count of any IoT MCP server (120+ across 10 tool groups). Covers device management, asset/customer CRUD, alarm management, time-series telemetry with TTL, OTA package management, entity relationships, and complex data queries. STDIO and SSE transports. Docker support with configurable tool groups.

**Why it wins:** 120+ tools is extraordinary coverage. Official vendor support means it stays in sync with the ThingsBoard platform. The configurable tool groups let you load only what you need — important given the token cost of 120+ tool definitions.

**The catch:** Requires Java 17+. ThingsBoard-specific — not useful without a ThingsBoard instance.

**Best for:** ThingsBoard platform users who want comprehensive AI agent access to their IoT infrastructure.

### Node-RED servers

**[karavaev-evgeniy/node-red-mcp-server](https://github.com/karavaev-evgeniy/node-red-mcp-server)** (31 stars, JavaScript, MIT, 20+ tools) — The most popular Node-RED MCP server. Retrieve/update flows, manage tabs/nodes, search, trigger inject nodes, and visualize flows. Best for Node-RED users managing complex flow-based IoT automations.

**[fx/mcp-node-red](https://github.com/fx/mcp-node-red)** (2 stars, TypeScript, MIT, 17 tools) — Flow CRUD, runtime control, node module management, context store operations, and system diagnostics. Safety-focused with validation before deployment. Best for teams that want deployment guardrails.

### Also notable

**[tuya/tuya-mcp-sdk](https://github.com/tuya/tuya-mcp-sdk)** (14 stars, Python + Go, Apache 2.0) — Official Tuya SDK for MCP integration with Tuya Cloud. If you use Tuya-based smart devices (many white-label products run on Tuya), this is the way in.

---

## ESP32 servers

### The development winner: horw/esp-mcp

**Stars:** 139 | **Language:** Python | **License:** Not specified | **Tools:** 7+

[horw/esp-mcp](https://github.com/horw/esp-mcp) is the most popular ESP32 MCP server, focused on the ESP-IDF development workflow. Install ESP-IDF, create projects, set targets, build, list serial ports, flash firmware, and run pytest. Multi-target chip support (ESP32, ESP32-C3, ESP32-S3, and more).

**Why it wins:** The most adopted ESP32 MCP server. Covers the full development cycle from project creation to flashing. Multi-chip support means you're not locked to one ESP32 variant.

**The catch:** PoC phase (as of February 2025). Development tool, not a runtime server — it helps you build firmware, not control a running ESP32.

**Best for:** ESP-IDF developers who want AI-assisted firmware development.

### The hardware winner: navado/ESP32MCPServer

**Stars:** 38 | **Language:** C++ | **Tools:** 10+

[navado/ESP32MCPServer](https://github.com/navado/ESP32MCPServer) is a fundamentally different approach: the MCP server runs ON the ESP32 itself. Auto-scans I2C sensors (BME280, MPU6050, ADS1115, SHT31, BH1750, INA219), parses NMEA GPS/marine data, decodes NMEA 2000 CAN bus, and reads OBD-II vehicle diagnostics. Supports 8 hardware platforms including ESP32-S3, ESP32-C3, and nRF52840.

**Why it's notable:** Running MCP directly on embedded hardware is a paradigm shift. Instead of a bridge server on a PC, the microcontroller IS the MCP server. The auto-scanning I2C support means plug-in-and-go for common sensors.

**Best for:** Embedded engineers building sensor networks who want direct AI access to hardware.

### Also notable

**[rzeldent/esp32-cam-ai](https://github.com/rzeldent/esp32-cam-ai)** (20 stars, C++, 4 tools) — ESP32-CAM as an MCP server. Camera capture with flash, OTA updates, watchdog timer, and mDNS discovery. Optimized for <4KB base64 images. Best for vision-enabled IoT projects.

---

## Arduino and robotics servers

### The winner: vishalmysore/choturobo

**Stars:** 75 | **Language:** C++ + TypeScript | **License:** MIT | **Tools:** 13

[vishalmysore/choturobo](https://github.com/vishalmysore/choturobo) bridges Arduino robotics with AI. LED, buzzer, motor, servo, fan, and relay control. Temperature and distance sensing. Supports both wired (Arduino Nano 368) and wireless (ESP32) modes.

**Why it wins:** The only robotics-focused MCP server with meaningful adoption. Direct hardware actuator control through natural language — "turn the motor clockwise" or "read the distance sensor."

**The catch:** Hardware-specific. You need the matching Arduino/sensor setup.

**Best for:** Educational robotics, maker projects, and hardware prototyping.

### Also notable

**[Volt23/mcp-arduino-server](https://github.com/Volt23/mcp-arduino-server)** (10 stars, Python, MIT) — FastMCP bridge to arduino-cli. Sketch management, build/deploy, library operations, serial monitoring. Unique: WireViz schematic generation for AI-powered circuit diagrams.

**[jl-codes/platformio-mcp](https://github.com/jl-codes/platformio-mcp)** (16 stars, TypeScript, MIT, 11 tools) — Board-agnostic MCP server for PlatformIO supporting 1,000+ development boards across 30+ platforms. Project init, compile, upload, serial monitoring, and library management. Best for teams working across multiple hardware platforms.

---

## Apple HomeKit servers

### The winner: omarshahine/HomeClaw

**Stars:** 64 | **Language:** Swift + JavaScript | **Tools:** 8

[omarshahine/HomeClaw](https://github.com/omarshahine/HomeClaw) is a macOS menu bar app providing HomeKit access through MCP. CLI tool for scripting, MCP server for Claude Desktop/Code, scene management, webhook configuration, and event logging. Supports lights, locks, thermostats, sensors, doors, and fans.

**Why it wins:** The most mature HomeKit MCP server. Menu bar app, CLI, and MCP server in one package. Webhook support enables event-driven automation beyond simple on/off commands.

**The catch:** macOS only. HomeKit's local-only nature means no cloud access.

**Best for:** Apple ecosystem users who want AI-controlled smart home on Mac.

### Also notable

**[grahamaloo/HomeKitMCP](https://github.com/grahamaloo/HomeKitMCP)** (1 star, Swift, MIT, 10 tools) — Uses the native HomeKit framework and official Swift MCP SDK. Supports 11 device types — the broadest device type coverage among HomeKit MCP servers. Headless stdio operation. Requires macOS 15.0+.

**[somethingwithproof/home-mcp](https://github.com/somethingwithproof/home-mcp)** (1 star, TypeScript, MIT, 9 tools) — Creative approach: uses macOS Shortcuts app as the bridge to HomeKit. If you already have Shortcuts automations, this layers AI control on top.

---

## Industrial IoT servers

### The winner: poly-mcp/IoT-Edge-MCP-Server

**Stars:** 22 | **Language:** Python | **Tools:** 15+ | **Protocols:** MQTT (TLS), Modbus TCP/RTU, InfluxDB, Redis

[poly-mcp/IoT-Edge-MCP-Server](https://github.com/poly-mcp/IoT-Edge-MCP-Server) is the most comprehensive industrial IoT MCP server. Unifies MQTT sensors, Modbus devices, and industrial equipment through a single interface. Real-time monitoring, historical data with aggregations, PLC register/coil operations, and multi-priority alarm management. Enterprise security (API keys, JWT, IP allowlisting, rate limiting, HMAC signatures, audit logging). Includes a simulation mode with 10 sensors, 6 actuators, and 1 Modbus PLC for testing.

**Why it wins:** Production-grade security and multi-protocol support in one server. The simulation mode is especially valuable — you can test industrial IoT workflows without actual hardware.

**The catch:** Relatively new (22 stars). Industrial IoT is high-stakes; thorough testing is essential before any production use.

**Best for:** Industrial teams exploring AI-assisted equipment monitoring and control.

### Also notable

**[kukapay/modbus-mcp](https://github.com/kukapay/modbus-mcp)** (20 stars, Python, MIT, 6 tools) — Focused Modbus-only server supporting TCP, UDP, and serial connections. Read/write holding registers and coils. Best for simple PLC integration without the overhead of a full IIoT platform.

**[midhunxavier/OPCUA-MCP](https://github.com/midhunxavier/OPCUA-MCP)** (11 stars, Python + JavaScript, 7 tools) — The only dedicated OPC UA MCP server. Read/write nodes, browse hierarchies, batch operations, method calls, and variable discovery. Dual Python and TypeScript implementations. Best for OPC UA environments (common in manufacturing).

**[kasathur/energyatit-mcp-server](https://github.com/kasathur/energyatit-mcp-server)** (0 stars, JavaScript, MIT, 30+ tools) — Energy infrastructure focus with the broadest industrial protocol support: IEC 61850, DNP3, Modbus, OpenADR 2.0b, OCPP (EV charging), IEEE 2030.5, ICCP/TASE.2. Battery/solar dispatch, carbon ledger, demand response. Best for energy grid and utility applications.

---

## Smart lighting servers

### Philips Hue

**[rmrfslashbin/hue-mcp](https://github.com/rmrfslashbin/hue-mcp)** (2 stars, Go, MIT, 24 tools) — Multi-bridge support, real-time SSE sync, intelligent caching, room/scene management. The most feature-rich Hue MCP server.

**[ykhli/mcp-light-control](https://github.com/ykhli/mcp-light-control)** (21 stars, TypeScript, 3 tools) — Philips Hue control plus a unique Morse code-via-light feature. OAuth2 for off-network access. Higher star count but fewer tools.

### LIFX

**[furey/lifx-api-mcp-server](https://github.com/furey/lifx-api-mcp-server)** (3 stars, JavaScript, MIT, 17 tools + 3 resources + 3 prompts) — Full LIFX API integration. Effects (breathe, pulse, morph, flame, sunrise/sunset), scene cycling, selector-based targeting. The most complete smart lighting MCP server across any brand.

---

## Specialty IoT servers

**[schwarztim/bambu-mcp](https://github.com/schwarztim/bambu-mcp)** (6 stars, TypeScript, MIT, 25 tools) — Bambu Lab 3D printer control via MQTT. Print control, camera feeds, AMS filament management, hardware control. X.509 certificate auth. Built-in safety: blocks dangerous G-code and enforces temperature limits.

**[lubosstrejcek/victron-tcp](https://github.com/lubosstrejcek/victron-tcp)** (0 stars, TypeScript, MIT, 28 tools) — Victron Energy solar/battery systems via MQTT or Modbus TCP. 900+ registers, 33 device categories. Network auto-discovery. Read-only by default for safety.

**[game4automation/shelly](https://github.com/game4automation/shelly)** (0 stars, Python, MIT, 9 tools) — Shelly smart device energy monitoring. 3-phase measurements, historical data, device on/off/toggle. Supports Shelly Pro 3EM, 3EM, EM, Plus PM, Plus 1PM.

**[ichbinder/MCP2ZigBee2MQTT](https://github.com/ichbinder/MCP2ZigBee2MQTT)** (1 star, TypeScript, MIT, 10 tools) — The only dedicated Zigbee MCP server. Connects to ZigBee2MQTT with intelligent device discovery and auto-analyzed device schemas. SQLite database for compact storage.

**[grammy-jiang/RaspberryPiOS-MCP](https://github.com/grammy-jiang/RaspberryPiOS-MCP)** (0 stars, Python, 8 feature modules) — The most comprehensive Raspberry Pi MCP server. System monitoring, GPIO control, I2C communication, camera capture, service management. Cloudflare Tunnel + OAuth security. Two-service privilege separation architecture.

---

## How to choose

Use this decision flowchart:

**Do you use Home Assistant?** → Start with [homeassistant-ai/ha-mcp](https://github.com/homeassistant-ai/ha-mcp). It's the most mature IoT MCP ecosystem by far.

**Do you need industrial IoT?** → If on AWS, use [awslabs IoT SiteWise](https://github.com/awslabs/mcp/tree/main/src/aws-iot-sitewise-mcp-server). If self-hosted, try [IoT-Edge-MCP-Server](https://github.com/poly-mcp/IoT-Edge-MCP-Server). For Modbus-only, use [modbus-mcp](https://github.com/kukapay/modbus-mcp).

**Do you use ThingsBoard?** → [thingsboard-mcp](https://github.com/thingsboard/thingsboard-mcp) with 120+ tools is the clear choice.

**Are you building firmware?** → [esp-mcp](https://github.com/horw/esp-mcp) for ESP-IDF, [platformio-mcp](https://github.com/jl-codes/platformio-mcp) for multi-board, [mcp-arduino-server](https://github.com/Volt23/mcp-arduino-server) for Arduino CLI.

**Do you want MCP running on hardware?** → [ESP32MCPServer](https://github.com/navado/ESP32MCPServer) runs directly on the ESP32. [esp32-cam-ai](https://github.com/rzeldent/esp32-cam-ai) adds camera capture.

**Apple HomeKit?** → [HomeClaw](https://github.com/omarshahine/HomeClaw) on macOS.

**Just need MQTT?** → [mqtt-mcp](https://github.com/ezhuk/mqtt-mcp) for generic pub/sub. [emqx-mcp-server](https://github.com/benniu/emqx-mcp-server) for EMQX brokers.

---

## Three trends worth watching

**1. Home Assistant is pulling ahead.** With 5+ MCP servers, the most stars, and official core integration in development, Home Assistant is becoming the default smart home gateway for AI agents. The archived allenporter server's functionality migrating into HA Core signals that MCP support will eventually be built-in, not a third-party add-on.

**2. On-device MCP is real.** Projects like ESP32MCPServer and esp32-cam-ai prove that MCP servers can run directly on microcontrollers. This eliminates the bridge server — the hardware itself speaks MCP. As edge computing grows, expect more embedded MCP servers.

**3. Industrial IoT is emerging but cautious.** AWS IoT SiteWise's official MCP server validates the concept, but the community IIoT servers are small (10-22 stars). Industrial environments move slowly for good reason — safety, reliability, and regulatory compliance matter more than convenience. The simulation modes in IoT-Edge-MCP-Server and choturobo show the ecosystem is building testing infrastructure first.

---

## What's missing

The IoT MCP landscape has significant gaps:

- **Google Home / Nest** — No actively maintained MCP server exists. Given Google's smart home market share, this is the biggest gap.
- **Azure IoT Hub / Digital Twins** — No dedicated server. Microsoft's MCP monorepo covers 40+ Azure services but not IoT-specific ones.
- **Matter protocol** — No standalone MCP server. Matter is the industry's unified smart home standard, but MCP hasn't caught up.
- **Z-Wave** — Only accessible through Home Assistant. No dedicated server.
- **LoRaWAN / Thread / BLE** — No MCP servers for these protocols.
- **SmartThings** — One minimal TV-focused server exists. Samsung's broad smart home platform deserves better.
- **Ring / Arlo / Wyze** — No dedicated camera/security system MCP servers.

These gaps represent real opportunities. A Matter MCP server or a Google Home MCP server would immediately fill a market need.

---

*Last updated: March 2026. Have a correction or suggestion? [Open an issue on GitHub](https://github.com/grove/chatforest.com).*

---
title: "Robotics MCP Servers — ROS, Home Assistant, ESP32, Robot Arms, Drones, and More (Updated)"
date: 2026-03-19T23:00:00+09:00
description: "Robotics MCP servers let AI agents control physical hardware — from robot arms to smart homes to embedded microcontrollers. We found 50+ servers across 11 subcategories. NEW: xiaozhi-esp32 (24,900 stars, C++, MIT — MCP-based voice AI on ESP32 with 70+ hardware platforms) is now the highest-starred project in the category. DimOS (1,700 stars, Python — agentic OS for humanoids, quadrupeds, drones, xArm with full MCP integration). ROS/ROS2: robotmcp/ros-mcp-server (1,100 stars, Python, Apache-2.0 — v3.0.1, bidirectional AI-ROS integration). Home Automation: homeassistant-ai/ha-mcp (1,600 stars, Python, MIT, 96 tools — the most comprehensive smart home MCP server), tevonsb/homeassistant-mcp (556 stars, TypeScript, Apache-2.0 — SSE real-time updates), voska/hass-mcp (284 stars, Python — token-efficient diagnostics). Embedded: xiaozhi-esp32 (24,900 stars — voice AI + MCP on ESP32), choturobo (74 stars, JavaScript — Arduino control), platformio-mcp (MIT — 1,000+ boards), embedded-debugger-mcp (52 stars, Rust — ARM/RISC-V). Robot Arms: robot_MCP (71 stars, Python, Apache-2.0 — SO-ARM100/101), universal-robot-mcp (Universal Robots control). Simulation: isaac-sim-mcp (138 stars, Python, MIT — NVIDIA Isaac Sim). Drones: MAVLinkMCP (15 stars — PX4/ArduPilot), drone-mcp (25 stars — DJI Tello). Agentic Platforms: DimOS (1,700 stars — unified robotics OS with MCP). Gaps: no official servers from any robot manufacturer, no Gazebo-native MCP, no warehouse/logistics robots. Rating: 4.5/5 (upgraded from 4.0)."
og_description: "Robotics MCP servers: xiaozhi-esp32 (24,900 stars, voice AI on ESP32), Home Assistant (1,600 stars, 96 tools), ROS/ROS2 (1,100 stars, any robot), DimOS (1,700 stars, agentic robotics OS), NVIDIA Isaac Sim (138 stars, simulation), robot arms (71 stars, SO-ARM100). 50+ servers across ROS, home automation, embedded, drones, and simulation. Rating: 4.5/5."
content_type: "Review"
card_description: "Robotics MCP servers for controlling physical hardware through AI agents — from industrial robot arms to smart home devices to embedded microcontrollers. This is one of the most exciting MCP categories because it bridges the digital-physical gap. **UPDATE (March 2026):** Major growth across the board — xiaozhi-esp32 exploded to 24,900 stars, Home Assistant reached 1,600 stars with 96 tools, ROS integration crossed 1,100 stars, and DimOS (1,700 stars) emerged as the first agentic robotics operating system with full MCP support. Rating upgraded from 4.0 to 4.5/5. **xiaozhi-esp32 is the breakout story** — 78/xiaozhi-esp32 (24,900 stars, C++, MIT) turns ESP32 microcontrollers into MCP-enabled voice AI assistants supporting 70+ open-source hardware platforms, with offline wake-word detection, streaming ASR+LLM+TTS, and speaker recognition. Its companion backend (xinnan-tech/xiaozhi-esp32-server, 8,000 stars) adds voiceprint recognition and knowledge base. **Home Assistant dominates smart home** with homeassistant-ai/ha-mcp (1,600 stars, 96 tools) — device management, automation, calendars, cameras, backups, and system queries. Two community alternatives (tevonsb/homeassistant-mcp at 556 stars with SSE real-time updates, voska/hass-mcp at 284 stars with token-efficient design) ensure coverage. **ROS/ROS2 crossed 1,100 stars** — robotmcp/ros-mcp-server v3.0.1 (now Apache-2.0 licensed) enables bidirectional AI-ROS integration for any ROS1/ROS2 robot. 7+ independent implementations exist. **DimOS is a new category leader** — dimensionalOS/dimos (1,700 stars) is an agentic operating system for physical space with full MCP integration, supporting Unitree quadrupeds (Go2, B1), humanoids (G1), xArm manipulators, and drones via MAVLink/DJI. **NVIDIA Isaac Sim** (138 stars, MIT) enables physics-based robot simulation. **Robot arms** are represented by robot_MCP (71 stars, now Apache-2.0) and universal-robot-mcp. Major gaps: no official servers from any robot manufacturer (Universal Robots, Boston Dynamics, Fanuc, ABB, KUKA, iRobot), no Gazebo-native simulation, no warehouse/logistics robots. The category earns 4.5/5 — exceptional community coverage with explosive growth in embedded AI (xiaozhi-esp32) and the emergence of unified agentic robotics platforms (DimOS)."
---

Robotics MCP servers bridge the gap between AI and the physical world — letting agents control robot arms, manage smart homes, program microcontrollers, fly drones, and run physics simulations. Instead of writing ROS commands or Home Assistant YAML by hand, these servers let AI agents interact with hardware through natural language.

This review covers the **robotics and hardware automation** vertical — ROS/ROS2 integration, home automation, embedded systems, robot arms, simulation, drones, and computer vision for robotics. For 3D printing and CNC, see our [Printing & 3D Printing MCP review](/reviews/printing-3d-printing-mcp-servers/). For industrial IoT and manufacturing, see our [Manufacturing & Industrial MCP review](/reviews/manufacturing-industrial-mcp-servers/). For IoT and embedded platforms, see our [IoT & Embedded MCP review](/reviews/iot-embedded-mcp-servers/).

The headline findings: **xiaozhi-esp32 is the breakout star** at 24,900 stars — an MCP-based voice AI platform running on ESP32 microcontrollers, supporting 70+ hardware platforms. **Home Assistant has the most tool-rich robotics MCP server** at 1,600 stars with 96 tools. **ROS/ROS2 integration has matured** — robotmcp/ros-mcp-server crossed 1,100 stars with its v3.0.1 release and Apache-2.0 license. **DimOS emerged as the first agentic robotics OS** at 1,700 stars with full MCP integration for humanoids, quadrupeds, drones, and manipulators. **No major robot manufacturer has an official MCP server** — not Universal Robots, Boston Dynamics, Fanuc, ABB, or KUKA.

## Home Automation

### homeassistant-ai/ha-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [homeassistant-ai/ha-mcp](https://github.com/homeassistant-ai/ha-mcp) | 1,600 | Python | MIT | 96 |

The **most popular smart home MCP server** and among the highest-starred MCP servers in any category. This is the official Home Assistant MCP integration, providing comprehensive smart home control:

- **Device control** — lights, switches, thermostats, locks, covers, fans, media players
- **Automation management** — create, modify, trigger, and debug automations
- **Entity search** — query device states across your entire home
- **Calendars and todo lists** — integrated scheduling and task management
- **Dashboards** — manage Lovelace dashboard configurations
- **Backup and restore** — system backup management
- **History and statistics** — query historical sensor data and trends
- **Camera snapshots** — capture images from connected cameras
- **System queries** — check Home Assistant health, add-ons, and configuration

96 tools make this one of the most feature-rich MCP servers in existence. Growth from 1,200 to 1,600 stars in just a few weeks shows how fast the smart home + AI intersection is moving.

### tevonsb/homeassistant-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [tevonsb/homeassistant-mcp](https://github.com/tevonsb/homeassistant-mcp) | 556 | TypeScript | Apache-2.0 | — |

A community alternative with a key differentiator: **SSE (Server-Sent Events) for real-time updates.** While the official server uses request-response, this server streams state changes as they happen — useful for monitoring scenarios like "tell me when the front door opens."

### voska/hass-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [voska/hass-mcp](https://github.com/voska/hass-mcp) | 284 | Python | — | — |

Focuses on **token efficiency** — a real concern when LLMs query hundreds of smart home entities. Includes smart search, diagnostic tools, guided prompts, and Docker deployment. Good for homes with many devices where context window management matters.

### Additional Home Automation Servers

- **allenporter/mcp-server-home-assistant** (~60 stars, Python) — lightweight bridge, 1 tool for contextual smart home awareness
- **jango-blockchained/advanced-homeassistant-mcp** — secure and extensible, supports Claude/GPT/Cursor
- **ichbinder/MCP2ZigBee2MQTT** — intelligent ZigBee device discovery via MQTT broker, auto-analyzes device capabilities, remote server support via HTTP

The Home Assistant ecosystem is **the most well-served niche in robotics MCP** — 7 implementations ensure coverage for virtually any smart home setup.

## ROS / ROS2 Integration

### robotmcp/ros-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [robotmcp/ros-mcp-server](https://github.com/robotmcp/ros-mcp-server) | 1,100 | Python | Apache-2.0 | — |

The **most popular ROS MCP server** and the gateway to controlling any ROS-based robot with AI. Now at v3.0.1 (January 2026) with Apache-2.0 licensing. Key features:

- **Bidirectional AI-ROS integration** — not just sending commands, but receiving sensor data and robot state
- **ROS1 and ROS2 support** — works with both generations of the Robot Operating System
- **Zero code changes** — only requires a rosbridge node on the robot side
- **Topic subscription** — real-time sensor data streams (lidar, cameras, IMU, joint states)
- **Service calls** — trigger robot behaviors (navigation goals, gripper commands, mode changes)
- **Multi-platform AI support** — works with Claude Desktop, Gemini, and ChatGPT

The jump from 873 to 1,100 stars and the switch to Apache-2.0 licensing signal maturation — this is no longer an experiment but a serious integration layer for the robotics community.

### lpigeon/ros-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [lpigeon/ros-mcp-server](https://github.com/lpigeon/ros-mcp-server) | 148 | Python | MIT | ~8 |

A more focused alternative with explicit tool definitions: list topics, list services, list message types, view type definitions, publish/subscribe topics, call services (including custom), get/set parameters. Uses WebSocket via rosbridge and works cross-platform (Linux/Windows/macOS).

### Additional ROS Implementations

- **kakimochi/ros2-mcp-server** (~73 stars, Python, MIT) — ROS2-specific, topic-based robot control
- **Yutarop/ros-mcp** (Python) — controls robots via topics, services, and actions; includes socket server for Gazebo/rqt_graph launching
- **TakanariShimbo/rosbridge-mcp-server** (Python, 8 tools) — rosbridge WebSocket monitoring and control
- **wise-vision/mcp_server_ros_2** (~4 stars, Python, MPL-2.0) — subscribe, publish, list, and call services
- **ngres/ros2mcp** — expose arbitrary ROS2 services and topics as MCP tools; includes Gazebo and Rviz2 demo

At least 7 independent ROS MCP servers exist — reflecting the robotics community's enthusiasm for AI integration. The pattern mirrors what we see in other popular APIs like Google Calendar: once the use case is obvious, multiple implementations appear rapidly.

## Embedded Hardware

### 78/xiaozhi-esp32

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [78/xiaozhi-esp32](https://github.com/78/xiaozhi-esp32) | 24,900 | C++ | MIT | — |

The **highest-starred project in this entire review** and one of the fastest-growing MCP-adjacent repositories on GitHub. Xiaozhi-esp32 is a voice interaction platform that runs on ESP32 microcontrollers, leveraging cloud-side MCP to extend LLM capabilities including smart home control, PC desktop operation, knowledge search, and email.

- **Voice AI on a microcontroller** — offline wake-word detection, streaming ASR+LLM+TTS architecture
- **70+ open-source hardware platforms** supported — ESP32-C3, ESP32-S3, ESP32-P4
- **Speaker recognition** — voiceprint identification for multi-user scenarios
- **MCP protocol integration** — extends LLM capabilities to control physical devices (speakers, LEDs, servos, GPIO)
- **Multi-LLM support** — works with Qwen, DeepSeek, and other models
- **v2.2.4** (March 2026) — actively maintained with frequent releases

The companion backend project (xinnan-tech/xiaozhi-esp32-server, 8,000 stars) adds server-side infrastructure with MQTT+UDP protocol, WebSocket support, MCP access points, voiceprint recognition, and knowledge base — developed by researchers at South China University of Technology.

This is remarkable because it represents MCP penetrating the consumer electronics space. A $5 ESP32 becomes a voice-controlled AI assistant with MCP as the extensibility layer.

### vishalmysore/choturobo

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [vishalmysore/choturobo](https://github.com/vishalmysore/choturobo) | 74 | JavaScript | — | — |

Controls **Arduino ESP32 and Arduino Nano 368** robot hardware via MCP using the Johnny-Five library:

- LEDs, motors, servos, fans, sensors
- Wireless control via ESP32 WiFi
- Wired USB control via Arduino Nano
- Natural language robot commands through Claude/GPT

### jl-codes/platformio-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [jl-codes/platformio-mcp](https://github.com/jl-codes/platformio-mcp) | — | — | MIT | — |

**Board-agnostic embedded development** via PlatformIO — supports 1,000+ boards across 30+ platforms including ESP32, Arduino, STM32, nRF52, and RP2040. Initialize projects, build firmware, upload, monitor serial, and manage libraries, all through AI.

### Adancurusul/embedded-debugger-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Adancurusul/embedded-debugger-mcp](https://github.com/Adancurusul/embedded-debugger-mcp) | 52 | Rust | MIT | — |

**Embedded debugging with probe-rs** — supports ARM Cortex-M and RISC-V architectures with J-Link and ST-Link integration. Having an AI agent help with embedded debugging could be transformative for developers who spend hours decoding register dumps.

### MCP on Microcontrollers

A fascinating subcategory: libraries that run MCP servers **directly on microcontrollers**:

- **AaronWander/EmbedMCP** (C) — lightweight C library for creating MCP servers on STM32, ESP32, Nordic nRF, and Raspberry Pi. Transforms C functions into AI-accessible tools.
- **redbasecap-buiss/mcpd** — MCP Server SDK for ESP32/RP2040 with built-in GPIO tools (digital read/write, analog read, pin mode), WiFi info, I2C scanner
- **navado/ESP32MCPServer** — WebSocket-based MCP on ESP32 for resource discovery and monitoring
- **ertgtct/mcpesp** — ESP32 MCP server library, exposes hardware capabilities via HTTP/JSON-RPC

Running MCP natively on a $5 microcontroller is remarkable — it means any ESP32 project can become AI-controllable without a host computer.

### Additional Embedded Servers

- **Volt23/mcp-arduino-server** (Python, FastMCP) — arduino-cli bridge, manage sketches/boards/libraries, WireViz schematics
- **AimanMadan/Arduino_MCP_Server** — control Arduino from computer via MCP
- **grammy-jiang/RaspberryPiOS-MCP** (Python) — system monitoring, GPIO control, I2C communication, camera capture, Cloudflare Tunnel + OAuth, self-update

## Robot Arms

### IliaLarchenko/robot_MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [IliaLarchenko/robot_MCP](https://github.com/IliaLarchenko/robot_MCP) | 71 | Python | Apache-2.0 | — |

Controls **SO-ARM100/101 educational robot arms** and LeKiwi robots via MCP. Works with Claude, Gemini, and GPT models. Includes manual keyboard operation mode and a simple agent for autonomous task execution.

### RoversX/universal-robot-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [RoversX/universal-robot-mcp](https://github.com/RoversX/universal-robot-mcp) | — | Python | — | — |

The only **industrial robot arm** MCP server found — controls Universal Robots cobots with:

- Robot connection management
- Real-time status monitoring
- Joint motion control
- Linear motion control
- Cartesian path planning
- Simulation mode
- Collision detection and movement validation

Universal Robots makes the world's most popular collaborative robot arms (used in factories worldwide), so having MCP integration — even community-built — is significant.

### monteslu/robot-mcp

A minimal but fun implementation: **1 tool (moveMyServo, 0-180 degrees)** using Johnny-Five. The simplest possible robot arm MCP server — controls a single servo motor.

## Simulation

### omni-mcp/isaac-sim-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [omni-mcp/isaac-sim-mcp](https://github.com/omni-mcp/isaac-sim-mcp) | 138 | Python | MIT | — |

**NVIDIA Isaac Sim integration** — the most capable robotics simulation platform available. Features:

- Natural language control of simulation environments
- Dynamic robot placement (Franka Panda, Unitree G1 humanoid, Unitree Go1 quadruped, NVIDIA Jetbot)
- Robot movement controls with physics-based interactions
- Multi-robot grid creation for swarm scenarios
- Quadruped walking simulation with waypoint navigation
- Custom lighting and USD asset search

Isaac Sim is industry-standard for robotics simulation — this server makes it accessible to AI agents for testing robot behaviors without physical hardware.

## Drones & UAV

### ion-g-ion/MAVLinkMCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ion-g-ion/MAVLinkMCP](https://github.com/ion-g-ion/MAVLinkMCP) | 15 | Python | — | — |

Controls **PX4 and ArduPilot drones** via the MAVLink protocol — the standard communication protocol used by millions of drones worldwide. Enables LLM-to-drone communication with a fastagent client example.

### Additional Drone Servers

- **0xKoda/drone-mcp** (25 stars, Python, MIT) — DJI Tello control with takeoff, land, directional movement, rotation, SSE real-time streaming
- **showkeyjar/robot-mcp-server** (Python) — dual-purpose: Unitree robot motion control + DJI drone flight commands (takeoff/landing), emergency stop, real-time status

## Computer Vision for Robotics

- **groundlight/mcp-vision** (Python) — HuggingFace computer vision models (zero-shot object detection) as MCP tools
- **GongRzhe/opencv-mcp-server** (Python) — OpenCV image/video processing, from basic manipulation to advanced object detection and tracking
- **GongRzhe/YOLO-MCP-Server** (Python) — YOLO object detection, segmentation, classification, real-time camera analysis via Claude

## Quadruped & Humanoid Robots

### lpigeon/unitree-go2-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [lpigeon/unitree-go2-mcp-server](https://github.com/lpigeon/unitree-go2-mcp-server) | 17 | Python | — | — |

Natural language control of the **Unitree Go2 robot dog** — commands are translated to ROS2 instructions. Requires ROS2 Humble or Foxy.

### jackccrawford/reachy-mini-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [jackccrawford/reachy-mini-mcp](https://github.com/jackccrawford/reachy-mini-mcp) | — | — | Apache-2.0 | 7 |

Controls **Pollen Robotics Reachy Mini humanoid robot** — speak, listen, see, and express 12 built-in emotions. Works with Claude/GPT/Grok. Zero robotics expertise required, 30 minutes to first demo.

## Serial & Hardware Communication

- **mcp2everything/mcp2serial** (Python) — AI-to-hardware control via serial communication, Raspberry Pi Pico support
- **Adancurusul/serial-mcp-server** — comprehensive serial communication for embedded systems, IoT devices, hardware debugging

## Robot Memory

### robotmem/robotmem

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [robotmem/robotmem](https://github.com/robotmem/robotmem) | — | Python | — | 7 |

**Persistent memory for AI-controlled robots** — a niche but important capability. Uses SQLite + FTS5 for full-text search, BM25 ranking, vector search via FastEmbed, spatial nearest-neighbor sorting, and memory consolidation with proactive recall. CPU-only, single-file database. Useful for robots that need to remember past interactions, locations, or learned behaviors across sessions.

## Industrial Automation

### poly-mcp/IoT-Edge-MCP-Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [poly-mcp/IoT-Edge-MCP-Server](https://github.com/poly-mcp/IoT-Edge-MCP-Server) | — | Python | — | — |

The only **industrial IoT MCP server** found — integrates MQTT + Modbus protocols with InfluxDB time-series storage, Redis cache, real-time monitoring, alarms, and actuator control. Enterprise-grade, works with PolyMCP for AI agent orchestration.

## Agentic Robotics Platforms

### dimensionalOS/dimos

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [dimensionalOS/dimos](https://github.com/dimensionalOS/dimos) | 1,700 | Python | — | — |

**NEW.** The first **agentic operating system for physical space** — and a significant new entry in the robotics MCP landscape. DimOS doesn't just control one robot; it provides a unified framework for humanoids, quadrupeds, drones, and manipulators with full MCP integration.

- **Hardware support** — Unitree quadrupeds (Go2, B1), humanoids (G1), xArm manipulators, MAVLink drones, DJI drones
- **Navigation & mapping** — SLAM, dynamic obstacle avoidance, route planning, autonomous exploration
- **Perception** — object detectors, 3D projections, vision language models, audio processing
- **Spatial memory** — spatio-temporal RAG, dynamic memory, object localization
- **MCP skills** — expose robot capabilities as MCP tools via `dimos mcp` command interface
- **Multi-agent systems** — coordinate multiple robots working in the same physical space
- **Multi-language interop** — C++, Lua, TypeScript via LCM

DimOS represents a shift from "one MCP server per robot" to "one operating system with MCP as the AI integration layer." At 1,700 stars and growing, this could become the ROS-successor for AI-native robotics.

## What's Missing

The gaps in robotics MCP are significant:

- **No official manufacturer servers** — Universal Robots, Boston Dynamics, Fanuc, ABB, KUKA, iRobot, and every other major robot company are absent
- **No Gazebo-native MCP** — simulation is only accessible via ROS bridge, not directly
- **No warehouse/logistics robot servers** — no AMR (Autonomous Mobile Robot) fleet management
- **No agricultural robot servers** — despite precision agriculture being a major robotics market
- **No consumer robot integration** — no Roomba, no Roborock, no lawn mower robots
- **No Peloton or Zwift** — fitness equipment with robotics-like control surfaces
- **No safety-certified servers** — robotics has strict safety standards (ISO 10218, IEC 62443) that no MCP server addresses
- **No digital twin platforms** — Azure Digital Twins, AWS IoT TwinMaker, Siemens MindSphere are all absent

The safety gap is particularly notable. Industrial robots can cause serious harm, and none of these servers implement the safety interlocks, watchdog timers, or emergency stop protocols that real industrial deployments require. The Universal Robots MCP has collision detection, but that's the exception.

## Bottom Line

Robotics MCP servers earn **4.5 out of 5** (upgraded from 4.0). The category has grown to 50+ servers across home automation, ROS, embedded hardware, robot arms, simulation, drones, computer vision, and now agentic robotics platforms.

**The big story since our last review is explosive growth.** xiaozhi-esp32 rocketed to 24,900 stars — making it the highest-starred MCP-integrated project in any robotics subcategory and proving that MCP has penetrated the consumer electronics space. Home Assistant grew from 1,200 to 1,600 stars while expanding to 96 tools. ROS crossed 1,100 stars with a v3.0.1 release and Apache-2.0 licensing. DimOS emerged at 1,700 stars as the first agentic operating system for physical robots with native MCP integration.

The community is still building faster than the manufacturers. No major robot company has released an official MCP server, leaving community developers to reverse-engineer APIs and build bridges. But the quality and ambition of community projects — especially DimOS with its multi-robot, multi-hardware-platform approach — suggests that vendor adoption may be less critical than we thought.

For smart home enthusiasts, **ha-mcp** is essential. For roboticists, **robotmcp/ros-mcp-server** is the universal adapter. For embedded AI, **xiaozhi-esp32** is the reference implementation. For multi-robot systems, **DimOS** is the emerging platform. For makers, **platformio-mcp** and **choturobo** open up AI-controlled hardware. For researchers, **isaac-sim-mcp** brings NVIDIA's simulation stack to AI agents. The category has real depth — and the growth rate suggests it will keep accelerating.

*This review was last updated on 2026-03-19 using Claude Opus 4.6 (Anthropic).*

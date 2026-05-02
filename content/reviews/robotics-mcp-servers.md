---
title: "Robotics MCP Servers — ROS, Home Assistant, ESP32, Robot Arms, Drones, and More (Updated)"
date: 2026-03-19T23:00:00+09:00
description: "Robotics MCP servers let AI agents control physical hardware — from robot arms to smart homes to embedded microcontrollers. We found 55+ servers across 12 subcategories."
og_description: "Robotics MCP servers: DimOS SURGED 1,700→3,100 stars (+82%) agentic robotics OS, xiaozhi-esp32 (26,100 stars, voice AI on ESP32), Home Assistant official MCP + ha-mcp (86 tools), ROS/ROS2 (1,200 stars), phosphobot NEW VLA robot arm control, wise-vision/ros2_mcp NEW image streaming, Isaac Sim v0.3.0 USD asset search. 55+ servers across ROS, home automation, embedded, drones, simulation, and VLA robotics. Rating: 4.5/5."
content_type: "Review"
card_description: "Robotics MCP servers for controlling physical hardware through AI agents — from industrial robot arms to smart home devices to embedded microcontrollers. This is one of the most exciting MCP categories because it bridges the digital-physical gap. **UPDATE (May 2026):** DimOS SURGED from 1,700 to 3,100 stars (+82%) with daemon mode, temporal-spatial memory, and Go2 fleet control. xiaozhi-esp32 grew to 26,100 stars with v2.2.6. Home Assistant now has OFFICIAL built-in MCP integration (Streamable HTTP) alongside ha-mcp (86 tools, consolidated from 96). phosphobot MCP NEW — first VLA (vision-language-action) model integration for SO-100/SO-101 robot arms. wise-vision/ros2_mcp NEW — advanced ROS2 MCP with image streaming and auto QoS. Isaac Sim v0.3.0 adds USD 3D asset search. CSOAI-ORG/robotics-control-mcp NEW — HARVI humanoid project with serial+HTTP hardware control. ROS crossed 1,200 stars with 160 forks. Still no major manufacturer official servers. Rating holds 4.5/5 — the VLA paradigm (phosphobot) and agentic robotics OS (DimOS surge) represent a shift from 'control a robot' to 'teach a robot' via MCP."
last_refreshed: 2026-05-02
---

*Part of the [IoT & Hardware](/categories/iot-hardware/) category.*

Robotics MCP servers bridge the gap between AI and the physical world — letting agents control robot arms, manage smart homes, program microcontrollers, fly drones, and run physics simulations. Instead of writing ROS commands or Home Assistant YAML by hand, these servers let AI agents interact with hardware through natural language.

This review covers the **robotics and hardware automation** vertical — ROS/ROS2 integration, home automation, embedded systems, robot arms, simulation, drones, and computer vision for robotics. For 3D printing and CNC, see our [Printing & 3D Printing MCP review](/reviews/printing-3d-printing-mcp-servers/). For industrial IoT and manufacturing, see our [Manufacturing & Industrial MCP review](/reviews/manufacturing-industrial-mcp-servers/). For IoT and embedded platforms, see our [IoT & Embedded MCP review](/reviews/iot-embedded-mcp-servers/).

The headline findings: **DimOS nearly doubled to 3,100 stars** — cementing its position as the premier agentic robotics operating system with new daemon mode, temporal-spatial memory, and Go2 fleet multi-robot control. **xiaozhi-esp32 continues growing** at 26,100 stars with v2.2.6. **Home Assistant now has TWO MCP options** — the official built-in MCP Server integration (Streamable HTTP, entity control via Assist API) and the community ha-mcp (86 consolidated tools). **phosphobot MCP is the VLA breakthrough** — the first server bridging vision-language-action models to physical robot arms (SO-100/SO-101). **wise-vision/ros2_mcp brings image streaming to ROS2 MCP** with automatic QoS and health reporting. **robotmcp/ros-mcp-server crossed 1,200 stars** with 160 forks. **Isaac Sim MCP v0.3.0 adds USD asset search** for loading 3D models. **Still no major robot manufacturer has an official MCP server** — not Universal Robots, Boston Dynamics, Fanuc, ABB, KUKA, or iRobot — though KUKA's iiQKA.OS2 and Google's Intrinsic platform suggest the gap may close soon.

## Home Automation

### Home Assistant Official MCP Server (Built-in)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [home-assistant/core](https://www.home-assistant.io/integrations/mcp_server/) | — | Python | Apache-2.0 | — |

**Home Assistant now ships with a built-in MCP Server integration** — implementing the Streamable HTTP protocol for stateless client-to-server communication. It exposes the Assist API, letting MCP clients control devices and entities you've explicitly exposed. Configuration is done through the Home Assistant UI — no YAML required. For lighter use cases (basic device control via Claude Desktop or other MCP clients), this is the recommended starting point.

### homeassistant-ai/ha-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [homeassistant-ai/ha-mcp](https://github.com/homeassistant-ai/ha-mcp) | 1,600+ | Python | MIT | 86 |

The **most feature-rich smart home MCP server** and among the highest-starred MCP servers in any category. This is the community-built "Unofficial and Awesome" Home Assistant MCP Server — significantly richer than the official built-in integration, with 86 tools across 24 categories (consolidated from 96 in the previous version — tools were merged for clarity, not removed):

- **Device control** — lights, switches, thermostats, locks, covers, fans, media players
- **Automation management** — create, modify, trigger, and debug automations
- **Entity search** — query device states across your entire home
- **Calendars and todo lists** — integrated scheduling and task management
- **Dashboards** — manage Lovelace dashboard configurations with unified identifier handling
- **Backup and restore** — system backup management
- **History and statistics** — query historical sensor data and trends
- **Camera snapshots** — capture images from connected cameras
- **Energy management** — NEW `ha_manage_energy_prefs` tool for Energy Dashboard CRUD
- **System queries** — check Home Assistant health, add-ons, and configuration
- **Addon management** — renamed `ha_manage_addon` with Supervisor config mode, Core ingress proxy routing

Recent improvements include merging `ha_config_list_floors` and `ha_config_list_areas` into `ha_list_floors_areas`, and unifying `ha_config_set_helper` to cover all 27 helper types. Available as an HA OS Add-on with a setup wizard.

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
| [robotmcp/ros-mcp-server](https://github.com/robotmcp/ros-mcp-server) | 1,200 | Python | Apache-2.0 | — |

The **most popular ROS MCP server** and the gateway to controlling any ROS-based robot with AI. Now at v3.0.1 with Apache-2.0 licensing, 18 contributors, and 160 forks — ranked #18 on MCP servers leaderboards. Key features:

- **Bidirectional AI-ROS integration** — not just sending commands, but receiving sensor data and robot state
- **ROS1 and ROS2 support** — works with both generations of the Robot Operating System
- **Zero code changes** — only requires a rosbridge node on the robot side
- **Topic subscription** — real-time sensor data streams (lidar, cameras, IMU, joint states)
- **Service calls** — trigger robot behaviors (navigation goals, gripper commands, mode changes)
- **Multi-platform AI support** — works with Claude Desktop, Gemini, and ChatGPT

Growth from 1,100 to 1,200 stars with 160 forks confirms this is the standard ROS-MCP integration layer.

### lpigeon/ros-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [lpigeon/ros-mcp-server](https://github.com/lpigeon/ros-mcp-server) | 148 | Python | MIT | ~8 |

A more focused alternative with explicit tool definitions: list topics, list services, list message types, view type definitions, publish/subscribe topics, call services (including custom), get/set parameters. Uses WebSocket via rosbridge and works cross-platform (Linux/Windows/macOS).

### wise-vision/ros2_mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [wise-vision/ros2_mcp](https://github.com/wise-vision/ros2_mcp) | — | Python | MPL-2.0 | — |

**NEW.** An advanced MCP Server for ROS2 that goes significantly beyond basic topic/service bridging. Key differentiators:

- **Image streaming** — subscribes to Image and CompressedImage message types, enabling MCP to receive camera feeds directly from ROS2 topics
- **Automatic QoS** — determines and applies appropriate QoS profiles based on publisher endpoints, increasing reliability
- **Health reporting** — checks if expected topics/services are available with comprehensive status indicators
- **Topic republishing** — republish messages between topics with optional transformations, rate limiting, and change-based filtering
- **Statistical analysis** — collect messages for a specified duration, provide message rates and counts
- **1-minute setup** — stdio transport, no brokers or webserver required
- **Built-in interface discovery** — dynamically enumerates available topics and services with message/service definitions

This is an evolution from the earlier wise-vision/mcp_server_ros_2 — rewritten as a significantly more capable tool with image streaming being particularly important for vision-guided robotics.

### Additional ROS Implementations

- **kakimochi/ros2-mcp-server** (~73 stars, Python, MIT) — ROS2-specific, topic-based robot control
- **Yutarop/ros-mcp** (Python) — controls robots via topics, services, and actions; includes socket server for Gazebo/rqt_graph launching
- **TakanariShimbo/rosbridge-mcp-server** (Python, 8 tools) — rosbridge WebSocket monitoring and control
- **ngres/ros2mcp** — expose arbitrary ROS2 services and topics as MCP tools; includes Gazebo and Rviz2 demo

At least 9 independent ROS MCP servers now exist — reflecting the robotics community's enthusiasm for AI integration. The pattern mirrors what we see in other popular APIs like Google Calendar: once the use case is obvious, multiple implementations appear rapidly.

## Embedded Hardware

### 78/xiaozhi-esp32

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [78/xiaozhi-esp32](https://github.com/78/xiaozhi-esp32) | 26,100 | C++ | MIT | — |

The **highest-starred project in this entire review** and one of the fastest-growing MCP-adjacent repositories on GitHub. Xiaozhi-esp32 is a voice interaction platform that runs on ESP32 microcontrollers, leveraging cloud-side MCP to extend LLM capabilities including smart home control, PC desktop operation, knowledge search, and email.

- **Voice AI on a microcontroller** — offline wake-word detection, streaming ASR+LLM+TTS architecture
- **70+ open-source hardware platforms** supported — ESP32-C3, ESP32-S3, ESP32-P4
- **Speaker recognition** — voiceprint identification for multi-user scenarios
- **MCP protocol integration** — extends LLM capabilities to control physical devices (speakers, LEDs, servos, GPIO)
- **Multi-LLM support** — works with Qwen, DeepSeek, and other models
- **v2.2.6** (April 19, 2026) — actively maintained with frequent releases
- **BLUFI network configuration** — encrypted WiFi setup support

The companion backend project (xinnan-tech/xiaozhi-esp32-server, 8,000+ stars) adds server-side infrastructure with MQTT+UDP protocol, WebSocket support, MCP access points, voiceprint recognition, and knowledge base — developed by researchers at South China University of Technology. A Java enterprise management platform variant also exists in the ecosystem.

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

## VLA Robotics (Vision-Language-Action)

*New since our March 2026 review.*

### phospho-app/phospho-mcp-server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [phospho-app/phospho-mcp-server](https://github.com/phospho-app/phospho-mcp-server) | — | Python | — | — |

**NEW.** The first MCP server bridging **vision-language-action (VLA) models** to physical robot arms — representing a paradigm shift from "control a robot" to "teach a robot." Built on [phosphobot](https://github.com/phospho-app/phosphobot) (community-driven middleware for robot control, dataset recording, and action model training), this server connects LLMs like Claude directly to physical robots:

- **Camera feed access** — stream images from robot-mounted cameras into the AI conversation
- **Action execution** — trigger trained VLA models to perform manipulation tasks (e.g., "pick up the red block")
- **Compatible hardware** — SO-100 and SO-101 educational robot arms
- **Dataset recording** — record demonstrations for training action models
- **LeRobot integration** — compatible with Hugging Face's LeRobot framework for policy training

The significance: previous robot MCP servers sent explicit commands ("move joint 3 to 45 degrees"). phosphobot's MCP server instead triggers learned behaviors — the robot has been trained to perform tasks, and the LLM decides when and what to trigger. This is the bridge between language AI and physical AI (embodied intelligence).

### CSOAI-ORG/robotics-control-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [CSOAI-ORG/robotics-control-mcp](https://glama.ai/mcp/servers/CSOAI-ORG/robotics-control-mcp) | — | — | — | — |

**NEW.** Part of the **HARVI Humanoid Robotics** project by MEOK AI Labs. Uses SO-101 servo arms with LeRobot ML inference for AI-driven teleoperation and autonomous control. Provides hardware control over serial ports and HTTP:

- **Device discovery** — automatic detection of connected hardware
- **Servo control** — direct servo positioning for robot arm manipulation
- **Sensor reading** — read from connected sensors
- **G-code execution** — control 3D printers, CNC machines
- **Emergency stop** — safety features for immediate halt
- **Multi-hardware** — Arduino, Raspberry Pi, servo controllers, custom robots

## Simulation

### omni-mcp/isaac-sim-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [omni-mcp/isaac-sim-mcp](https://github.com/omni-mcp/isaac-sim-mcp) | 138+ | Python | MIT | — |

**NVIDIA Isaac Sim integration** — the most capable robotics simulation platform available. **v0.3.0 (April 25, 2026)** adds USD asset search — a significant new capability:

- Natural language control of simulation environments
- **USD asset search** — NEW `search_3d_usd_by_text` tool to search and load pre-existing 3D models from USD libraries
- **Custom positioning and scaling** — direct model transformation capabilities for loaded USD assets
- Dynamic robot placement (Franka Panda, Unitree G1 humanoid, Unitree Go1 quadruped, NVIDIA Jetbot)
- Robot movement controls with physics-based interactions
- Multi-robot grid creation for swarm scenarios
- Quadruped walking simulation with waypoint navigation
- Custom lighting

Isaac Sim is industry-standard for robotics simulation — this server makes it accessible to AI agents for testing robot behaviors without physical hardware. Requires Isaac Sim 4.2.0+ and Python 3.9+. NVIDIA's broader GR00T platform (Isaac GR00T N1 foundation model, Newton physics engine with Google DeepMind, Isaac Lab-Arena) suggests deeper MCP integration may follow.

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
| [dimensionalOS/dimos](https://github.com/dimensionalOS/dimos) | 3,100 | Python | — | — |

The first **agentic operating system for physical space** — and the fastest-growing project in robotics MCP. **SURGED from 1,700 to 3,100 stars (+82%) in 6 weeks**, with 518 forks and active development. DimOS doesn't just control one robot; it provides a unified framework for humanoids, quadrupeds, drones, and manipulators with full MCP integration.

- **Hardware support** — Unitree quadrupeds (Go2, B1), humanoids (G1), xArm manipulators, MAVLink drones, DJI drones
- **Go2 fleet control** — NEW multi-robot control with `--robot-ips` for coordinating multiple quadrupeds
- **Daemon mode** — NEW production CLI: `dimos run --daemon` with health checks, run registry, `dimos stop/status/restart`
- **Temporal-spatial memory** — NEW human-like understanding of physical space — causal object relationships, entity tracking through time and space, complex temporal queries
- **Navigation & mapping** — SLAM, dynamic obstacle avoidance, route planning, autonomous exploration
- **Perception** — object detectors, 3D projections, vision language models, audio processing
- **MCP skills** — expose all `@skill` methods as HTTP tools, external agents can call `dimos mcp call` commands
- **MCP CLI** — `dimos mcp list-tools`, `dimos mcp call`, `dimos mcp status`, `dimos mcp modules`
- **Multi-agent systems** — coordinate multiple robots working in the same physical space
- **Multi-language interop** — C++, Lua, TypeScript via LCM

DimOS represents a shift from "one MCP server per robot" to "one operating system with MCP as the AI integration layer." The 82% star surge and temporal-spatial memory addition suggest it's becoming the platform of choice for AI-native robotics — a ROS successor for the agentic era.

## What's Missing

The gaps in robotics MCP are narrowing but still significant:

- **No official manufacturer servers** — Universal Robots, Boston Dynamics, Fanuc, ABB, KUKA, iRobot remain absent — though KUKA's iiQKA.OS2 (AI-ready, ISO 10218:2026 compliant), Google's Intrinsic platform (partnering with FANUC, UR, KUKA), and NVIDIA's GR00T foundation model suggest vendor MCP adoption may come via platform partnerships rather than standalone servers
- **No Gazebo-native MCP** — simulation is only accessible via ROS bridge, not directly (though Isaac Sim's USD asset search closes part of this gap)
- **No warehouse/logistics robot servers** — no AMR (Autonomous Mobile Robot) fleet management
- **No agricultural robot servers** — despite precision agriculture being a major robotics market
- **No consumer robot integration** — no Roomba, no Roborock, no lawn mower robots
- **No safety-certified servers** — robotics has strict safety standards (ISO 10218, IEC 62443) that no MCP server addresses — CSOAI-ORG's emergency stop is a start but not a certified implementation
- **No digital twin platforms** — Azure Digital Twins, AWS IoT TwinMaker, Siemens MindSphere are all absent

The safety gap is particularly notable. Industrial robots can cause serious harm, and none of these servers implement the safety interlocks, watchdog timers, or emergency stop protocols that real industrial deployments require. The Universal Robots MCP has collision detection and CSOAI-ORG has emergency stop, but neither approaches industrial safety certification.

## Bottom Line

Robotics MCP servers earn **4.5 out of 5** (rating holds). The category has grown to 55+ servers across home automation, ROS, embedded hardware, robot arms, VLA robotics, simulation, drones, computer vision, and agentic robotics platforms.

**The big story since our last review is DimOS's surge and the emergence of VLA robotics.** DimOS nearly doubled from 1,700 to 3,100 stars (+82%) — adding daemon mode for production deployments, temporal-spatial memory for persistent world understanding, and Go2 fleet multi-robot control. It's no longer "emerging" — it's established as the premier agentic robotics OS. Meanwhile, phosphobot's MCP server introduces the VLA (vision-language-action) paradigm: instead of sending explicit motor commands, the LLM triggers learned behaviors from trained action models. This is the bridge between language AI and physical AI.

**Home Assistant now offers two distinct MCP paths** — the official built-in integration (simple, Streamable HTTP, for basic device control) and the community ha-mcp (86 tools across 24 categories, for comprehensive automation). xiaozhi-esp32 continues its remarkable trajectory at 26,100 stars. Isaac Sim v0.3.0 adds USD asset search, making 3D model loading AI-driven. wise-vision/ros2_mcp brings image streaming directly into the ROS2-MCP bridge.

The community is still building faster than the manufacturers. No major robot company has released an official MCP server — but the landscape is shifting. KUKA's iiQKA.OS2 is explicitly AI-ready and ISO 10218:2026 compliant. Google's Intrinsic platform partners with FANUC, Universal Robots, and KUKA. NVIDIA's GR00T foundation model provides humanoid robot reasoning. The gap between "community MCP bridges" and "official robotics platforms" may close through these intermediary platforms rather than through standalone vendor MCP servers.

For smart home enthusiasts, **ha-mcp** (or the built-in integration for simple setups) is essential. For roboticists, **robotmcp/ros-mcp-server** is the universal adapter. For ROS2 with vision, **wise-vision/ros2_mcp** adds image streaming. For embedded AI, **xiaozhi-esp32** is the reference implementation. For multi-robot systems, **DimOS** is the platform. For VLA/embodied AI, **phosphobot MCP** bridges learned behaviors. For makers, **platformio-mcp** and **choturobo** open up AI-controlled hardware. For researchers, **isaac-sim-mcp** brings NVIDIA's simulation stack to AI agents. The category has exceptional depth — and the shift from "control commands" to "learned behaviors" (VLA) suggests the most interesting phase is just beginning.

---

---

## Refresh History {#refresh-history}

**2026-05-02 (first refresh):** DimOS SURGED 1,700→3,100 stars (+82%) with daemon mode, temporal-spatial memory, Go2 fleet multi-robot control, MCP CLI. xiaozhi-esp32 24,900→26,100 stars (+5%), v2.2.4→v2.2.6. robotmcp/ros-mcp-server 1,100→1,200 stars, 160 forks, 18 contributors. ha-mcp consolidated 96→86 tools (merged for clarity), new energy management + addon improvements. **Home Assistant OFFICIAL built-in MCP Server** integration now exists (Streamable HTTP, Assist API). **phosphobot MCP NEW** — first VLA (vision-language-action) model integration for SO-100/SO-101 robot arms, camera streaming, LeRobot compatibility. **wise-vision/ros2_mcp NEW** — advanced ROS2 with Image/CompressedImage streaming, auto QoS, health reports, topic republishing. **CSOAI-ORG/robotics-control-mcp NEW** — HARVI humanoid project, serial+HTTP, emergency stop. Isaac Sim v0.3.0 (April 25) adds USD asset search (`search_3d_usd_by_text`). NVIDIA GR00T N1 and Newton physics engine announced at GTC 2026 but no direct MCP integration yet. KUKA iiQKA.OS2 AI-ready + ISO 10218:2026. Google Intrinsic partners FANUC+UR+KUKA. Seeed reBot Arm B601-DM open-source 6-axis with ROS2/MoveIt2/LeRobot/Isaac Sim (no MCP yet). No manufacturer official MCP servers still. Rating holds 4.5/5.

**2026-03-19 (original review):** Initial review covering 50+ servers across 11 subcategories. xiaozhi-esp32 24,900 stars, Home Assistant 1,600 stars 96 tools, ROS 1,100 stars, DimOS 1,700 stars. Rating 4.5/5 (upgraded from 4.0).

---

*This review was researched and written by an AI agent. We have not personally tested these servers — our analysis is based on documentation, source code, GitHub metrics, and community adoption. See our [methodology](/about/) for details.*

*This review was last refreshed on 2026-05-02 using Claude Opus 4.6 (Anthropic).*

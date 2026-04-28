---
title: "Smart Home & Home Automation MCP Servers — Home Assistant, Apple HomeKit, Samsung SmartThings, Amazon Alexa, Google Home, Philips Hue, Tuya, Zigbee2MQTT, and IoT Device Control"
date: 2026-03-16T14:00:00+09:00
description: "Smart home and home automation MCP servers let AI agents control lights, thermostats, locks, and cameras, manage automations, and monitor device states through the Model Context Protocol."
og_description: "Smart home MCP servers: ha-mcp (2,600+ stars, 86+ tools for Home Assistant), HomeClaw (99 stars, Apple HomeKit 10 tools), Samsung SmartThings MCP, Amazon Alexa MCP, Google Home MCP, Philips Hue (5+ servers), Tuya official SDK, Zigbee2MQTT bridge, Ring security, Roborock vacuum. 30+ servers reviewed. Rating: 4.5/5."
content_type: "Review"
card_description: "Smart home and home automation MCP servers for controlling lights, thermostats, locks, cameras, and managing automations through AI assistants. This category covers the software that controls your home — not the IoT hardware protocols themselves (see [IoT & Embedded](/reviews/iot-embedded-mcp-servers/)), not energy utilities (see [Energy & Utilities](/reviews/energy-utilities-mcp-servers/)). **Home Assistant dominates and surged** — ha-mcp (2,600+ stars, up from 1,100+) now provides 86+ tools with MIT license, v7.3.0, custom component support, and a setup wizard for 15+ AI clients. homeassistant-mcp (569 stars) adds real-time SSE and 95% test coverage. voska/hass-mcp (278 stars) and ganhammar/hass-mcp-server (30 stars, 50+ tools, HTTP transport with OAuth 2.0) expand the ecosystem further. Home Assistant's built-in MCP server integration completes the picture. **The consumer platform gap is closing fast** — the biggest story since our initial review. Apple HomeKit now has THREE MCP servers: HomeClaw (99 stars, Swift, 10 tools for lights/locks/thermostats/scenes/automations), HomeKitMCP (Swift, native HomeKit framework, Mac Catalyst), and HomeMCPBridge (13 tools, Scrypted NVR plugin). Samsung SmartThings has TWO servers: bjornhovd's production-ready Dockerized server and PaulaAdelKamal's TV-focused 9-tool server. Amazon Alexa has TWO servers: sijan2's (10 stars, Cloudflare Workers) and guitarbeat's (voice announcements, music, lighting, sensors). Google Home has jmagar/ghome-mcp-server for smart plug control via Smart Home API. **Device-specific servers exploded** — Philips Hue alone has 5+ dedicated MCP servers (ThomasRohde, rmrfslashbin with multi-bridge support, kungfusheep with v2 API + CLI + lighting effects, pedrof with Docker, ykhli with Morse code signaling). Tuya launched an official MCP SDK (16 stars, Apache 2.0, Python/Go/C#) — the first major IoT platform vendor to ship an official MCP SDK. **Protocol bridges appeared** — ichbinder/MCP2ZigBee2MQTT (5 stars, 10 tools, intelligent schema discovery) fills the Zigbee2MQTT gap. **Security systems arrived** — jpcors/ring-mcp (4 stars, 6 tools: alarm arm/disarm, camera snapshots, light control, event monitoring). **Robot vacuums arrived** — jaxx2104/roborock-mcp-server (3 stars, MIT, 9 tools: status, cleaning, zones, rooms, map data, dock return). **The category transformed** from 'Home Assistant or nothing' to a genuine multi-platform ecosystem. Nine of ten originally-identified gaps now have at least one MCP server. Only Matter protocol as a direct MCP bridge and whole-home energy monitoring remain unfilled. Rating upgraded 3.5→4.5/5."
last_refreshed: 2026-04-28
---

*Part of the [IoT & Hardware](/categories/iot-hardware/) category.*

Smart home and home automation MCP servers connect AI agents to the systems that control your home — turning on lights, adjusting thermostats, locking doors, viewing camera feeds, and managing automations. Instead of opening apps, tapping buttons, or saying "Hey Google," these servers let you control your entire home through natural language via the Model Context Protocol.

This review covers **smart home and home automation** — device control (lights, switches, thermostats, locks, cameras), automation management, state monitoring, and IoT orchestration. For IoT hardware protocols and embedded systems, see our [IoT & Embedded review](/reviews/iot-embedded-mcp-servers/). For energy utilities and grid management, see our [Energy & Utilities review](/reviews/energy-utilities-mcp-servers/).

The headline findings: **Home Assistant surged** — ha-mcp more than doubled to 2,600+ stars with 86+ tools. **The consumer platform gap is closing fast** — Apple HomeKit, Samsung SmartThings, Amazon Alexa, and Google Home all gained MCP servers since our initial review. **Philips Hue exploded** with 5+ dedicated MCP servers. **Tuya shipped an official MCP SDK.** **Nine of ten originally-identified gaps now have at least one server.** This category transformed from "Home Assistant or nothing" to a genuine multi-platform ecosystem.

---

## Home Assistant

### homeassistant-ai/ha-mcp — The Leading Smart Home MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ha-mcp](https://github.com/homeassistant-ai/ha-mcp) | 2,600+ | Python | MIT | 86+ |

**The most comprehensive smart home MCP server by far** — 86+ tools covering the full Home Assistant ecosystem:

- **Entity control** — turn on/off lights, switches, fans, media players, locks, vacuums, covers, and any Home Assistant entity
- **Automation management** — create, edit, enable/disable, and trigger automations through natural language
- **Calendar and todo** — manage Home Assistant calendars and todo lists
- **Dashboard management** — query and configure Lovelace dashboards
- **Backup and restore** — create and manage Home Assistant backups
- **History and statistics** — query device history, energy stats, and sensor trends
- **Camera snapshots** — capture images from connected cameras
- **System administration** — query system health, configuration, and installed integrations
- **Custom component support** (ha_mcp_tools) — filesystem access and YAML editing with beta features
- **Bundled Agent Skills** — served as MCP resources from the homeassistant-ai/skills repository

Runs locally on your machine — smart home data stays on your network with no cloud dependency. No paid subscription required. Setup wizard supports 15+ AI clients including Claude Desktop, Claude Code, Gemini CLI, ChatGPT, Open WebUI, VSCode, Cursor, and more. Can be paired with Home Assistant Agent Skills for better configuration suggestions. MIT licensed.

**Since our initial review:** Stars more than doubled (1,100+ → 2,600+), tools grew from 80+ to 86+, MIT license confirmed, v7.3.0 released with custom component support and Home Assistant add-on deployment with webhook proxy for remote access via Nabu Casa.

### tevonsb/homeassistant-mcp — Real-Time Device Bridge

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [homeassistant-mcp](https://github.com/tevonsb/homeassistant-mcp) | 569 | TypeScript | — | Multiple |

**A powerful alternative with real-time event streaming:**

- **Device control** — control any Home Assistant device through natural language (lights, switches, climate, covers, fans, media players, locks, vacuums, cameras)
- **Real-time updates** — Server-Sent Events (SSE) for live device state changes
- **Automation management** — create, update, and manage automations
- **State monitoring** — track and query device states across your home
- **HACS management** — list, install, update, and manage Home Assistant Community Store packages
- **Add-on management** — browse, install, start, stop, restart, and configure Supervisor add-ons
- **Secure access** — token-based authentication with rate limiting
- **95% test coverage** — one of the most well-tested MCP servers in any category

The SSE support is notable — it means the AI assistant can receive real-time notifications when device states change, enabling reactive automations like "let me know when the front door opens."

**Since our initial review:** Stars grew from 500+ to 569 (+14%), now at 60 commits with 95% test coverage.

### ganhammar/hass-mcp-server — HTTP Transport with OAuth 2.0

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [hass-mcp-server](https://github.com/ganhammar/hass-mcp-server) | 30 | Python | MIT | 50+ |

**A Home Assistant custom component with HTTP transport — works remotely, not just locally:**

- **50+ tools** organized across entities/state, automations/scenes/scripts, helpers, config files, dashboards, and system administration
- **OAuth 2.0 authentication** with Dynamic Client Registration
- **Long-Lived Access Token** support as alternative auth
- **YAML config management** with automatic backups
- **CRUD management** of automations, scenes, scripts, and helper entities
- **Lovelace dashboard management** capabilities
- **System administration** including error logs and config validation

The HTTP transport (rather than stdio) makes this ideal for remote access to Home Assistant from any MCP client.

### voska/hass-mcp — Established Community Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [hass-mcp](https://github.com/voska/hass-mcp) | 278 | Python | — | Multiple |

**A well-established Home Assistant MCP server** with 278 stars and 45 forks — entity state queries, device control, and home automation summaries through a standardized MCP interface. Lightweight and focused.

### Other Home Assistant MCP Servers

| Server | Key Feature |
|--------|-------------|
| [zorak1103/ha-mcp](https://github.com/zorak1103/ha-mcp) | Smart home control and automation management |
| [jango-blockchained/advanced-homeassistant-mcp](https://github.com/jango-blockchained/advanced-homeassistant-mcp) | Device discovery, notification systems, smart maintenance features |
| [hekmon8/Homeassistant-server-mcp](https://github.com/hekmon8/Homeassistant-server-mcp) | Device control and monitoring through MCP-enabled applications |
| [hpohlmann/home-assistant-mcp](https://github.com/hpohlmann/home-assistant-mcp) | Entity search and device control optimized for Cursor |
| [amattas/homeassistant-mcp](https://github.com/amattas/homeassistant-mcp) | Device interaction via MCP |
| [miguelg719/home-assistant-mcp](https://github.com/miguelg719/home-assistant-mcp) | Additional Home Assistant MCP implementation |

Ten or more implementations make Home Assistant the most MCP-served smart home platform in the ecosystem — and it's not close.

### Home Assistant Built-In MCP Server

Home Assistant itself includes an [official MCP server integration](https://www.home-assistant.io/integrations/mcp_server/) — making it one of very few platforms to offer both native MCP support and a thriving community of alternative implementations. The built-in integration exposes your Home Assistant entities and services directly via MCP without requiring any external server.

---

## Apple HomeKit — Gap Filled

Three MCP servers now provide Apple HomeKit control — this was one of the biggest gaps in our initial review.

### omarshahine/HomeClaw — The HomeKit MCP Leader

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [HomeClaw](https://github.com/omarshahine/HomeClaw) | 99 | Swift | — | 10 |

**The most capable Apple HomeKit MCP server:**

- **homekit_status** — overview of all devices and their states
- **homekit_accessories** — detailed accessory information
- **homekit_rooms** — room-based device organization
- **homekit_scenes** — scene creation and triggering
- **homekit_device_map** — device topology and relationships
- **homekit_manage** — direct device control (lights, locks, thermostats, fans, sensors)
- **homekit_automations** — list, create, enable/disable automations with button-press triggers
- **homekit_events** — event logging
- **homekit_webhook** — webhook configuration for real-time notifications
- **homekit_config** — configuration management

Works with Claude Desktop, Claude Code, and OpenClaw. CLI interface for terminal control. TestFlight beta active. Swift 6.2 with macOS Tahoe support.

### grahamaloo/HomeKitMCP — Native HomeKit Framework

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [HomeKitMCP](https://github.com/grahamaloo/HomeKitMCP) | 1 | Swift | MIT | 10 |

**Mac Catalyst app using the native Apple HomeKit framework and official Swift MCP SDK:**

- Supports lights, switches, locks, thermostats, sensors, garage doors
- Batch control and query operations
- Scene execution
- Device filtering by home, room, or type
- Runs headless with optional menu bar status item
- Requires macOS 15.0+ and Xcode 26+

### coalsi/HomeMCPBridge — HomeKit + Scrypted NVR

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [HomeMCPBridge](https://github.com/coalsi/HomeMCPBridge) | 2 | Swift | MIT | 13 |

**Native HomeKit integration with camera and NVR support:**

- 13 tools across device control (5), cameras (2), motion/events (4), Scrypted NVR (2)
- Plugin system supporting Govee and Scrypted NVR
- Device linking to merge duplicates from multiple sources
- MCPPost event broadcasting for real-time sensor notifications
- Camera snapshot capture
- Menu bar application for background operation
- No external bridges or cloud services required
- Requires macOS 14.0 (Sonoma) or later

---

## Samsung SmartThings — Gap Filled

Two MCP servers now provide Samsung SmartThings control — another major gap closure.

### bjornhovd/Samsung-SmartThings-MCP — Production-Ready

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Samsung-SmartThings-MCP](https://glama.ai/mcp/servers/@bjornhovd/Samsung-SmartThings-MCP) | 4 | — | — | Multiple |

**Production-ready, Dockerized MCP server for SmartThings:**

- List locations, rooms, and devices
- Check device status and health
- Control switches and smart devices
- Monitor refrigerator-specific attributes (temperature, door states)
- Personal Access Token (PAT) authentication
- Docker containerization for easy deployment

### PaulaAdelKamal/samsung_smartthings-mcp — TV-Focused

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [samsung_smartthings-mcp](https://github.com/PaulaAdelKamal/samsung_smartthings-mcp) | — | Python | MIT | 9 |

**Samsung SmartThings control with TV focus:**

- list_devices, list_tv_devices, get_device_info, get_device_status
- turn_tv_on_off, change_tv_volume, mute_tv, change_tv_channel, change_tv_input
- Token-based authentication with async operations

---

## Amazon Alexa — Gap Filled

Two MCP servers now provide Amazon Alexa smart home control — perhaps the most surprising gap closure.

### sijan2/alexa-mcp-server — Cloudflare Workers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [alexa-mcp-server](https://github.com/sijan2/alexa-mcp-server) | 10 | TypeScript | — | Multiple |

**Amazon Alexa integration through MCP** — enables Alexa functionality through MCP clients like Poke. Built on Cloudflare Workers infrastructure. Uses reverse-engineered Alexa API endpoints discovered through network analysis.

### guitarbeat/Alexa-MCP-Server — Full Smart Home Control

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Alexa-MCP-Server](https://github.com/guitarbeat/alexa-mcp-server) | — | TypeScript | MIT | Multiple |

**Full Alexa smart home control through MCP:**

- **Voice announcements** with smart night-time suppression
- **Music control** — real-time playback status and track info
- **Smart lighting** — power, brightness, and color control
- **Sensor integration** — temperature, light, and motion data
- **Volume management** — precise control across device fleet
- Self-documenting API design for AI agents
- Deployable via Cloudflare Workers or Node.js Docker

---

## Google Home — Gap Filled

### jmagar/ghome-mcp-server — Smart Home API

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ghome-mcp-server](https://mcp.so/server/ghome-mcp-server/jmagar) | — | Node.js | — | Multiple |

**Google Home smart plug control through the Smart Home API:**

- List all available smart plugs and their states
- Control smart plugs (turn on/off)
- Get real-time state of specific devices
- Automatic device state refresh
- OAuth2 authentication with Smart Home API
- Requires Google Cloud Project with Smart Home API enabled

Currently limited to smart plugs — broader Google Home device support is the next frontier.

---

## Philips Hue — New Subcategory

Five or more dedicated MCP servers for Philips Hue lighting have appeared — making it the most MCP-served individual device brand outside of Home Assistant.

| Server | Key Feature |
|--------|-------------|
| [rmrfslashbin/hue-mcp](https://github.com/rmrfslashbin/hue-mcp) | Multi-bridge support, real-time sync, cached responses, comprehensive light/room/scene/bridge control |
| [kungfusheep/hue](https://github.com/kungfusheep/hue) | Philips Hue v2 API + CLI + native lighting effects — both MCP server and command-line tool |
| [ThomasRohde/hue-mcp](https://github.com/ThomasRohde/hue-mcp) | AI-powered Philips Hue control interface |
| [pedrof/hue-mcp-server](https://github.com/pedrof/hue-mcp-server) | Docker-ready with health monitoring |
| [ykhli/mcp-light-control](https://github.com/ykhli/mcp-light-control) | Philips Hue control including Morse code signaling through lights |

If you have Philips Hue lights and want AI control without running Home Assistant, you now have multiple direct options. The kungfusheep implementation is notable for providing both an MCP server and a standalone CLI with native lighting effects support via the v2 API.

---

## Tuya / Smart Life — Gap Filled (Official)

### tuya/tuya-mcp-sdk — Official Tuya MCP SDK

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [tuya-mcp-sdk](https://github.com/tuya/tuya-mcp-sdk) | 16 | Python/Go/C# | Apache 2.0 | Multiple |

**The first major IoT platform vendor to ship an official MCP SDK:**

- Multi-language support (Python, Go, C#)
- Connects custom capabilities to Tuya Cloud via MCP
- Secure authentication mechanisms
- WebSocket-based real-time communication
- Production-ready with comprehensive error handling and retry logic

Tuya powers hundreds of white-label smart devices sold under various brand names. This official SDK means any Tuya-compatible device can potentially be controlled through MCP, covering a massive swath of the affordable smart device market.

Community implementations also exist, including mcp-server-tuya on PyPI for direct device control via Claude Desktop.

---

## Zigbee2MQTT — Gap Filled

### ichbinder/MCP2ZigBee2MQTT — Zigbee Device Bridge

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [MCP2ZigBee2MQTT](https://github.com/ichbinder/MCP2ZigBee2MQTT) | 5 | TypeScript | MIT | 10 |

**Intelligent Zigbee device discovery and control for AI assistants:**

- Connects to MQTT broker and auto-analyzes all ZigBee2MQTT devices
- Learns device structure and capabilities automatically
- 10 MCP tools for discovery, control, documentation, and integration info
- Compact data storage (metadata/schemas only, not full message history)
- SQLite database backend
- Remote-capable via HTTP/SSE deployment
- Docker containerization support
- Optional API key authentication

This fills one of the most requested gaps — direct MCP access to the Zigbee2MQTT ecosystem without requiring Home Assistant as an intermediary.

---

## Security Systems — Gap Partially Filled

### jpcors/ring-mcp — Ring Security Devices

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ring-mcp](https://github.com/jpcors/ring-mcp) | 4 | TypeScript | — | 6 |

**Ring home security integration through MCP:**

- **list_devices** — discover all Ring devices
- **get_device_info** — detailed device information
- **arm_disarm_alarm** — arm/disarm Ring alarm with different modes
- **get_camera_snapshot** — capture images from Ring cameras
- **turn_light_on_off** — control Ring floodlights and smart lights
- **monitor_events** — real-time event monitoring with automatic token management

Uses the open-source ring-client-api library. Unofficial community project. ADT and SimpliSafe remain uncovered.

---

## Robot Vacuums — Gap Filled

### jaxx2104/roborock-mcp-server — Roborock Vacuum Control

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [roborock-mcp-server](https://github.com/jaxx2104/roborock-mcp-server) | 3 | TypeScript | MIT | 9 |

**Roborock robot vacuum control through MCP:**

- Status monitoring (battery, cleaning state)
- Start/stop/pause cleaning
- Return to dock
- Locate vacuum via sound alert
- Map data retrieval
- Zone-specific cleaning by coordinates
- Room-specific cleaning by room IDs

Requires Deno 1.37+ and Python 3.8+ with python-roborock package. The first robot vacuum MCP server.

---

## Other Smart Home Platforms

### abeardmore/hubitat-mcp — Hubitat Maker API

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [hubitat-mcp](https://github.com/abeardmore/hubitat-mcp) | — | — | — | Multiple |

**Hubitat Elevation smart home control via Maker API:**

- Device exposure to AI assistants via Maker API
- State queries across Hubitat hub
- Device command execution

A second implementation, MvdMunnik26/Hubitat-MCP, also connects to Hubitat Elevation via the Maker API.

### tdeckers/openhab-mcp — OpenHAB REST API

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [openhab-mcp](https://github.com/tdeckers/openhab-mcp) | — | — | — | Multiple |

**OpenHAB smart home control through its REST API:**

- Item management — query and control OpenHAB items (switches, dimmers, thermostats, sensors)
- State monitoring and command execution
- REST API integration with real OpenHAB instances

---

## IoT & Unified Device Control

### jprbom/smart-home-orchestrator-mcp — Multi-Brand IoT Control

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [smart-home-orchestrator-mcp](https://github.com/jprbom/smart-home-orchestrator-mcp) | — | — | — | Multiple |

**Unified control across smart home brands** — doesn't depend on a single hub platform:

- **Multi-brand support** — Nest (thermostats and cameras), Ring (doorbells and security), Ecobee (smart thermostats), TP-Link Kasa, Arlo, LIFX, August
- **MQTT integration** — control custom DIY IoT devices via MQTT
- **AI-powered automation** — natural language automation creation and optimization
- **Cross-device orchestration** — coordinate actions across different brands and protocols

### jordy33/iot_mcp_server — Generic IoT Device Control

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [iot_mcp_server](https://github.com/jordy33/iot_mcp_server) | — | — | — | Multiple |

**Standardized interface for IoT device control and monitoring** — smart lights, sensors, and connected devices through a unified protocol.

---

## Thermostat-Specific

### emrikol/ecobee-mcp — Ecobee Thermostat Control

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ecobee-mcp](https://lobehub.com/mcp/emrikol-ecobee-mcp) | — | TypeScript | — | Multiple |

**Dedicated Ecobee thermostat control** — temperature control, schedule management, sensor data, and climate modes. If you have Ecobee thermostats and want AI control without running a full home automation hub, this is a direct path.

---

## What's Missing

The smart home MCP ecosystem has closed most of its original gaps. What remains:

- **Matter protocol** — no direct MCP-to-Matter bridge (the home-assistant-matter-hub project was archived January 2026, though a community fork continues). Matter is accessible indirectly through Home Assistant's Matter integration + ha-mcp
- **Energy monitoring** — no solar panel management, battery storage, or whole-home energy monitoring MCP servers (energy data is available through Home Assistant's energy dashboard + ha-mcp, but no standalone solution)
- **ADT / SimpliSafe** — Ring has an MCP server but ADT and SimpliSafe do not
- **Google Home breadth** — current server is limited to smart plugs; broader device control not yet available
- **Alexa maturity** — both Alexa servers use reverse-engineered APIs rather than official endpoints

---

## The Bottom Line

**Rating: 4.5/5** — This category underwent a transformation since our initial review 43 days ago.

**The consumer platform gap is closing fast.** In March 2026, we identified ten major gaps — Google Home, Amazon Alexa, Apple HomeKit, Samsung SmartThings, Tuya, Zigbee2MQTT, Matter, energy monitoring, security systems, and robot vacuums. Nine of those ten now have at least one MCP server. Apple HomeKit alone went from zero to three implementations. Samsung SmartThings went from zero to two. Amazon Alexa went from zero to two. Tuya shipped an official SDK — the first major IoT platform vendor to do so.

**Home Assistant's lead grew even stronger.** ha-mcp more than doubled from 1,100+ to 2,600+ stars, making it one of the highest-starred MCP servers in any category. With 86+ tools, MIT license, custom component support, and a setup wizard for 15+ AI clients, it's a reference implementation for how a platform MCP server should work. Four major community alternatives (tevonsb at 569 stars, voska at 278 stars, ganhammar at 30 stars with 50+ tools and OAuth 2.0, plus the built-in integration) give users genuine choice.

**Philips Hue became the most MCP-served individual device brand** outside of Home Assistant, with 5+ dedicated servers offering different approaches (multi-bridge, CLI, Docker, native lighting effects, even Morse code signaling).

**The remaining gaps are narrowing.** Matter protocol access is available indirectly through Home Assistant. Energy monitoring works through HA's energy dashboard. The Alexa servers use reverse-engineered APIs that may be fragile, and Google Home coverage is still limited to smart plugs. But the trajectory is clear — smart home MCP went from a Home Assistant monoculture to a genuine multi-platform ecosystem in under two months.

*This review was refreshed on 2026-04-28 (initial review: 2026-03-16) using Claude Opus 4.6 (Anthropic). We research publicly available information; we have not tested these servers hands-on.*

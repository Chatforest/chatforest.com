---
title: "Smart Home & Home Automation MCP Servers — Home Assistant, Hubitat, OpenHAB, IoT Device Control, and Thermostat Management"
date: 2026-03-16T14:00:00+09:00
description: "Smart home and home automation MCP servers let AI agents control lights, thermostats, locks, and cameras, manage automations, and monitor device states through the Model Context Protocol. We reviewed 15+ servers across 4 subcategories. Home Assistant (8+ servers): homeassistant-ai/ha-mcp (1,100+ stars, Python — 80+ tools, entity control, automation management, calendar/todo, dashboards, backup/restore, history/statistics, camera snapshots, system queries, runs locally), tevonsb/homeassistant-mcp (500+ stars, TypeScript — device control, real-time SSE updates, automation management, state monitoring, HACS package management, add-on management), voska/hass-mcp (entity state queries, device control), zorak1103/ha-mcp (smart home control and automation management), jango-blockchained/advanced-homeassistant-mcp (device discovery, notification systems, smart maintenance), hekmon8/Homeassistant-server-mcp (device control and monitoring), hpohlmann/home-assistant-mcp (entity search, device control via Cursor), amattas/homeassistant-mcp (device interaction). Home Assistant also has an official built-in MCP server integration (home-assistant.io/integrations/mcp_server/). Other platforms: abeardmore/hubitat-mcp (Hubitat Maker API — expose devices to AI assistants), MvdMunnik26/Hubitat-MCP (Hubitat Elevation via Maker API), tdeckers/openhab-mcp (OpenHAB REST API — AI control of OpenHAB smart home). IoT & device control: jprbom/smart-home-orchestrator-mcp (unified IoT control across brands — Nest, Ring, Ecobee, MQTT, AI-powered automation), jordy33/iot_mcp_server (generic IoT device control and monitoring — smart lights, sensors, connected devices). Thermostat-specific: emrikol/ecobee-mcp (TypeScript — Ecobee thermostat control via MCP). Gaps: no Google Home/Nest Hub MCP server, no Amazon Alexa MCP server, no Apple HomeKit/Home MCP server, no Samsung SmartThings MCP server, no Tuya/Smart Life MCP server, no Zigbee2MQTT direct MCP server, no Matter protocol MCP server, no energy monitoring/solar panel management, no security system integration (ADT, SimpliSafe), no robot vacuum MCP servers. Rating: 3.5/5."
og_description: "Smart home MCP servers: ha-mcp (1,100+ stars, 80+ tools for Home Assistant), homeassistant-mcp (500+ stars, real-time device control), Hubitat MCP (Maker API), OpenHAB MCP (REST API), Smart Home Orchestrator (unified multi-brand IoT), Ecobee MCP (thermostat control). 15+ servers reviewed. Rating: 3.5/5."
content_type: "Review"
card_description: "Smart home and home automation MCP servers for controlling lights, thermostats, locks, cameras, and managing automations through AI assistants. This category covers the software that controls your home — not the IoT hardware protocols themselves (see [IoT & Embedded](/reviews/iot-embedded-mcp-servers/)), not energy utilities (see [Energy & Utilities](/reviews/energy-utilities-mcp-servers/)). **Home Assistant dominates this category** — 8+ MCP server implementations exist, making it one of the most MCP-served platforms in the entire ecosystem. homeassistant-ai/ha-mcp (1,100+ stars) provides 80+ tools covering entity control, automation management, calendars, dashboards, backup/restore, history, camera snapshots, and system administration — all running locally with no cloud dependency. tevonsb/homeassistant-mcp (500+ stars) takes a different approach with real-time Server-Sent Events, HACS package management, and add-on lifecycle management. Home Assistant also ships a built-in MCP server integration at home-assistant.io/integrations/mcp_server/, making it the rare platform with both official and extensive community MCP support. **Other platforms have basic coverage** — abeardmore/hubitat-mcp exposes Hubitat Maker API devices to Claude Desktop, and tdeckers/openhab-mcp connects to OpenHAB via its REST API. These are functional but limited compared to the Home Assistant ecosystem. **Unified IoT control is emerging** — jprbom/smart-home-orchestrator-mcp provides cross-brand device control for Nest, Ring, Ecobee, and custom MQTT devices with AI-powered automation. jordy33/iot_mcp_server offers generic IoT device control and monitoring. **Thermostat control has a dedicated server** — emrikol/ecobee-mcp provides Ecobee thermostat control through any MCP-compatible client. **Major gaps define the category** — no Google Home, Amazon Alexa, Apple HomeKit, or Samsung SmartThings MCP servers exist. These four platforms collectively control the majority of consumer smart homes, yet none have MCP integration. No Zigbee2MQTT direct MCP bridge, no Matter protocol server, no energy monitoring or solar panel management, no security system integration (ADT, SimpliSafe, Ring Alarm), and no robot vacuum control. The category earns 3.5/5 — Home Assistant's MCP ecosystem is genuinely impressive with 1,100+ stars and 80+ tools on the leading server, plus 8+ alternative implementations. If you run Home Assistant, AI-powered smart home control is production-ready today. But the category's reliance on Home Assistant as the sole mature platform, combined with the absence of all major consumer ecosystems (Google, Amazon, Apple, Samsung), limits the score. Most smart home users don't run Home Assistant — they use Alexa, Google Home, or Apple Home, and for them, MCP smart home control doesn't exist yet."
---

Smart home and home automation MCP servers connect AI agents to the systems that control your home — turning on lights, adjusting thermostats, locking doors, viewing camera feeds, and managing automations. Instead of opening apps, tapping buttons, or saying "Hey Google," these servers let you control your entire home through natural language via the Model Context Protocol.

This review covers **smart home and home automation** — device control (lights, switches, thermostats, locks, cameras), automation management, state monitoring, and IoT orchestration. For IoT hardware protocols and embedded systems, see our [IoT & Embedded review](/reviews/iot-embedded-mcp-servers/). For energy utilities and grid management, see our [Energy & Utilities review](/reviews/energy-utilities-mcp-servers/).

The headline findings: **Home Assistant dominates** with 8+ MCP server implementations — ha-mcp (1,100+ stars) provides 80+ tools for comprehensive smart home AI control. **Hubitat and OpenHAB have basic MCP servers** but lag far behind Home Assistant. **The biggest platforms are missing** — no Google Home, Amazon Alexa, Apple HomeKit, or Samsung SmartThings MCP servers exist. **If you run Home Assistant, smart home MCP is production-ready. If you don't, it barely exists.**

---

## Home Assistant

### homeassistant-ai/ha-mcp — The Leading Smart Home MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ha-mcp](https://github.com/homeassistant-ai/ha-mcp) | 1,100+ | Python | — | 80+ |

**The most comprehensive smart home MCP server by far** — 80+ tools covering the full Home Assistant ecosystem:

- **Entity control** — turn on/off lights, switches, fans, media players, locks, vacuums, covers, and any Home Assistant entity
- **Automation management** — create, edit, enable/disable, and trigger automations through natural language
- **Calendar and todo** — manage Home Assistant calendars and todo lists
- **Dashboard management** — query and configure Lovelace dashboards
- **Backup and restore** — create and manage Home Assistant backups
- **History and statistics** — query device history, energy stats, and sensor trends
- **Camera snapshots** — capture images from connected cameras
- **System administration** — query system health, configuration, and installed integrations

Runs locally on your machine — smart home data stays on your network with no cloud dependency. No paid subscription required. Works with Claude Code, Gemini CLI, ChatGPT, Open WebUI, VSCode, Cursor, and more. Can be paired with Home Assistant Agent Skills for better configuration suggestions.

### tevonsb/homeassistant-mcp — Real-Time Device Bridge

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [homeassistant-mcp](https://github.com/tevonsb/homeassistant-mcp) | 500+ | TypeScript | — | Multiple |

**A powerful alternative with real-time event streaming:**

- **Device control** — control any Home Assistant device through natural language (lights, switches, climate, covers, fans, media players, locks, vacuums, cameras)
- **Real-time updates** — Server-Sent Events (SSE) for live device state changes
- **Automation management** — create, update, and manage automations
- **State monitoring** — track and query device states across your home
- **HACS management** — list, install, update, and manage Home Assistant Community Store packages
- **Add-on management** — browse, install, start, stop, restart, and configure Supervisor add-ons
- **Secure access** — token-based authentication with rate limiting

The SSE support is notable — it means the AI assistant can receive real-time notifications when device states change, enabling reactive automations like "let me know when the front door opens."

### Other Home Assistant MCP Servers

| Server | Key Feature |
|--------|-------------|
| [voska/hass-mcp](https://github.com/voska/hass-mcp) | Entity state queries and device control — lightweight and focused |
| [zorak1103/ha-mcp](https://github.com/zorak1103/ha-mcp) | Smart home control and automation management |
| [jango-blockchained/advanced-homeassistant-mcp](https://github.com/jango-blockchained/advanced-homeassistant-mcp) | Device discovery, notification systems, smart maintenance features |
| [hekmon8/Homeassistant-server-mcp](https://github.com/hekmon8/Homeassistant-server-mcp) | Device control and monitoring through MCP-enabled applications |
| [hpohlmann/home-assistant-mcp](https://github.com/hpohlmann/home-assistant-mcp) | Entity search and device control optimized for Cursor |
| [amattas/homeassistant-mcp](https://github.com/amattas/homeassistant-mcp) | Device interaction via MCP |

Eight or more implementations make Home Assistant one of the most MCP-served platforms in the entire ecosystem — rivaling even Shopify for the number of community MCP servers targeting a single platform.

### Home Assistant Built-In MCP Server

Home Assistant itself includes an [official MCP server integration](https://www.home-assistant.io/integrations/mcp_server/) — making it one of very few platforms to offer both native MCP support and a thriving community of alternative implementations. The built-in integration exposes your Home Assistant entities and services directly via MCP without requiring any external server.

---

## Other Smart Home Platforms

### abeardmore/hubitat-mcp — Hubitat Maker API

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [hubitat-mcp](https://github.com/abeardmore/hubitat-mcp) | — | — | — | Multiple |

**Hubitat Elevation smart home control via Maker API:**

- **Device exposure** — exposes Hubitat Maker API devices to AI assistants like Claude Desktop
- **State queries** — check device states across your Hubitat hub
- **Device control** — send commands to Hubitat-connected devices

A second implementation, MvdMunnik26/Hubitat-MCP, also connects to Hubitat Elevation via the Maker API. The Hubitat community has been actively discussing MCP integration, but adoption is still early compared to Home Assistant.

### tdeckers/openhab-mcp — OpenHAB REST API

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [openhab-mcp](https://github.com/tdeckers/openhab-mcp) | — | — | — | Multiple |

**OpenHAB smart home control through its REST API:**

- **Item management** — query and control OpenHAB items (switches, dimmers, thermostats, sensors)
- **State monitoring** — read current states of all connected devices
- **Command execution** — send commands to control devices
- **REST API integration** — connects to a real OpenHAB instance

Functional but limited compared to the Home Assistant ecosystem. OpenHAB users have been calling for deeper MCP integration through the OpenHAB community forums.

---

## IoT & Unified Device Control

### jprbom/smart-home-orchestrator-mcp — Multi-Brand IoT Control

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [smart-home-orchestrator-mcp](https://github.com/jprbom/smart-home-orchestrator-mcp) | — | — | — | Multiple |

**Unified control across smart home brands** — doesn't depend on a single hub platform:

- **Multi-brand support** — Nest (thermostats and cameras), Ring (doorbells and security), Ecobee (smart thermostats)
- **MQTT integration** — control custom DIY IoT devices via MQTT
- **AI-powered automation** — natural language automation creation and optimization
- **Cross-device orchestration** — coordinate actions across different brands and protocols

This is the closest thing to a universal smart home MCP server — rather than requiring Home Assistant or Hubitat as a hub, it connects directly to multiple device ecosystems.

### jordy33/iot_mcp_server — Generic IoT Device Control

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [iot_mcp_server](https://github.com/jordy33/iot_mcp_server) | — | — | — | Multiple |

**Standardized interface for IoT device control and monitoring:**

- **Smart lights** — control brightness, color, and on/off state
- **Sensors** — read temperature, humidity, motion, and other sensor data
- **Connected devices** — manage any IoT device through a unified protocol
- **State management** — track and query device states

A generic approach to IoT MCP — useful for custom setups or devices not covered by platform-specific servers.

---

## Thermostat-Specific

### emrikol/ecobee-mcp — Ecobee Thermostat Control

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ecobee-mcp](https://lobehub.com/mcp/emrikol-ecobee-mcp) | — | TypeScript | — | Multiple |

**Dedicated Ecobee thermostat control** through any MCP-compatible client:

- **Temperature control** — set target temperatures, adjust heating/cooling modes
- **Schedule management** — view and modify thermostat schedules
- **Sensor data** — read temperature and occupancy from Ecobee room sensors
- **Climate modes** — switch between home, away, sleep, and custom comfort settings

Built with TypeScript, Express 5, and the MCP SDK. If you have Ecobee thermostats and want AI control without running a full home automation hub, this is a direct path.

---

## What's Missing

The smart home MCP ecosystem has a massive consumer-platform gap:

- **Google Home / Nest Hub** — no MCP server for Google's smart home ecosystem (millions of users)
- **Amazon Alexa** — no MCP server for Alexa-controlled devices (the largest smart home platform by market share)
- **Apple HomeKit / Home** — no MCP server for Apple's home automation (despite HomeKit's local-first architecture being ideal for MCP)
- **Samsung SmartThings** — no MCP server for SmartThings hub and devices
- **Tuya / Smart Life** — no MCP server for the platform behind hundreds of white-label smart devices
- **Zigbee2MQTT** — no direct MCP bridge for the popular Zigbee-to-MQTT gateway (only accessible through Home Assistant)
- **Matter protocol** — no MCP server for the new universal smart home standard
- **Energy monitoring** — no solar panel management, battery storage, or whole-home energy monitoring MCP servers
- **Security systems** — no ADT, SimpliSafe, Ring Alarm, or generic security panel MCP servers
- **Robot vacuums** — no Roomba, Roborock, or other robot vacuum MCP servers (popular automation targets)

---

## The Bottom Line

**Rating: 3.5/5** — This category tells two very different stories depending on your smart home platform.

**If you run Home Assistant, MCP smart home control is production-ready today.** The ha-mcp server (1,100+ stars, 80+ tools) is one of the most comprehensive MCP servers in any category — it covers device control, automations, history, cameras, backups, and system administration. With 8+ community implementations plus Home Assistant's own built-in MCP server integration, you have genuine choice. The ecosystem is mature enough that developers are differentiating on features (real-time SSE, HACS management, add-on control) rather than basic functionality.

**If you don't run Home Assistant, smart home MCP barely exists.** Hubitat and OpenHAB have basic servers, and the Smart Home Orchestrator provides multi-brand control for Nest/Ring/Ecobee. But Google Home, Amazon Alexa, Apple HomeKit, and Samsung SmartThings — the platforms that collectively serve the vast majority of smart home users — have zero MCP servers. This is a striking gap given that smart home control is a natural fit for conversational AI.

The Home Assistant focus makes strategic sense — it's the platform where technically-inclined users already live, and its REST API makes MCP integration straightforward. But until the major consumer platforms get MCP servers (or until someone builds a universal bridge through Matter), this category remains a niche serving the Home Assistant community rather than the broader smart home market.

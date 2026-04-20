# MCP and Autonomous Vehicles/Transportation: How AI Agents Connect to ROS, Simulation Platforms, Fleet Telematics, Mapping APIs, Public Transit, EV Charging, OBD-II Diagnostics, Traffic Systems, and Connected Vehicle Platforms

> A comprehensive guide to 45+ MCP integrations for autonomous vehicles and transportation — covering ROS servers (ros-mcp-server by robotmcp with ~1100 stars supporting ROS1+ROS2


Transportation is being reshaped by two converging forces: the push toward autonomous vehicles and the growing demand for AI agents that can orchestrate complex mobility systems. The Model Context Protocol sits at the intersection — providing a standardized way for AI to control robots through ROS, run traffic simulations, query fleet telematics, plan multimodal routes, monitor vehicle health, and navigate regulatory compliance across dozens of platforms that rarely speak the same language.

The autonomous vehicle market is projected to grow from approximately $96-105 billion in 2025 to ~$214 billion by 2030 at 19.9% CAGR. Level 4 autonomy is the fastest-growing segment at 38.2% CAGR. Robotaxis alone are projected to reach ~$7 billion by 2030, growing at roughly 90% CAGR from a small base. Connected cars represent a ~$119 billion market in 2025, projected to reach ~$423 billion by 2032 at 19.8% CAGR. The EV charging infrastructure market is ~$40 billion in 2025 and projected to hit ~$239 billion by 2033 at 25% CAGR. These are not speculative numbers — they reflect deployed capital and committed investment across the automotive and transportation sectors.

Academic research is catching up. A paper titled "Model Context Protocols in Adaptive Transport Systems: A Survey" (arXiv, August 2025) represents the first systematic investigation of MCP's role in transportation, examining how the protocol enables adaptive, AI-driven mobility systems.

This guide is research-based. We survey what MCP servers exist across the autonomous vehicle and transportation landscape, analyze the architecture patterns they enable, and identify where significant gaps remain. We do not claim to have tested or used any of these servers hands-on — our analysis draws on published documentation, open-source repositories, vendor announcements, academic publications, and industry research. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI. For background on MCP, see our [introduction to MCP](/guides/what-is-mcp/) and the [MCP server directory](/reviews/).

## Why Autonomous Vehicles and Transportation Need MCP

Transportation systems are inherently distributed, multi-vendor, and safety-critical — properties that make standardized AI integration both essential and difficult.

**AV development requires dozens of disconnected tools.** A single autonomous vehicle development workflow touches ROS for robot control, simulation platforms for testing, mapping services for localization, sensor data pipelines for perception, compliance databases for regulatory requirements, and fleet management systems for deployment. MCP servers for each system let AI agents orchestrate complete development and operations workflows through a unified protocol.

**Fleet operations span multiple data sources.** Managing a transportation fleet requires combining GPS telematics, vehicle diagnostics, route optimization, traffic data, weather, driver behavior analytics, and maintenance records. MCP-connected agents can query across all of these from a single conversational interface, providing operations teams with real-time situational awareness.

**Mobility is inherently multimodal.** Modern trip planning requires combining public transit schedules, ride-sharing prices, bike/scooter availability, EV charging locations, and walking directions. MCP enables agents to compose responses from multiple transportation data sources without custom integration code for every provider.

**Safety and compliance are non-negotiable.** Automotive cybersecurity regulations (UN R155/R156), functional safety standards (ISO 26262), and autonomous driving regulations vary by jurisdiction and evolve rapidly. MCP's structured tool interfaces create clear boundaries around what AI agents can access and modify, supporting compliance requirements for safety-critical systems.

## ROS (Robot Operating System) — The Largest MCP Category

ROS is the de facto standard for robotics software, and it has become the most active category in the transportation MCP ecosystem. At least seven independent MCP server implementations connect AI agents to ROS1 and ROS2, enabling natural language control of robots, autonomous vehicles, and robotic systems.

### ros-mcp-server (robotmcp)

**Repository:** robotmcp/ros-mcp-server (~1,100 stars) | **License:** Apache 2.0 | **Version:** v3.0.1

The most popular ROS MCP server by a wide margin. It supports both ROS1 and ROS2 with bidirectional AI-robot communication, making it the most complete implementation available.

Core capabilities:
- **Topic pub/sub** — subscribe to sensor data, publish control commands
- **Service calls** — invoke ROS services through natural language
- **Parameter management** — read and write ROS parameters
- **Custom message types** — support for non-standard message definitions
- **Bidirectional communication** — AI agents both observe and control robot state

The server enables scenarios like "subscribe to the LiDAR topic, analyze the point cloud, and if an obstacle is detected within 2 meters, publish a stop command" — all through a conversational AI interface. The 1,100+ star count reflects genuine community adoption across robotics research labs and autonomous vehicle development teams.

### rosbridge-mcp-server (TakanariShimbo)

**Repository:** TakanariShimbo/rosbridge-mcp-server | **Language:** Python

This implementation connects to ROS through the rosbridge WebSocket protocol rather than native ROS libraries, which simplifies deployment since the MCP server doesn't need a full ROS installation. It provides:

- **Topic listing** — discover available ROS topics
- **Message publishing** — publish to any topic
- **Service calls** — invoke ROS services
- **Action goals** — send goals to ROS action servers

The WebSocket approach makes this server particularly useful for remote monitoring and control scenarios where the AI agent runs on a different machine than the robot.

### ros2_mcp (L-CAS / Lincoln Centre for Autonomous Systems)

**Repository:** L-CAS/ros2_mcp | **Origin:** Academic (University of Lincoln)

An academic implementation focused on ROS2 with features tailored for research environments:

- **Structured prompts** for robotics analysis workflows
- **VLM (Vision-Language Model) integration** — connect visual perception models to robot control
- **Resource streaming** — continuous sensor data feeds
- **Docker deployment** — containerized for reproducible research environments

The Lincoln Centre for Autonomous Systems is a respected robotics research lab, and their implementation reflects research-grade requirements for experiment reproducibility and multi-modal perception.

### Additional ROS MCP Servers

- **ros-mcp** (Yutarop) — ROS topic, service, and action control via natural language. Community.
- **ros_mcp_server** (lpigeon) — Transforms natural language commands into ROS/ROS2 operations. Community.
- **ros2_mcp** (wise-vision) — Advanced ROS2 bridging with community support. Community.
- **ros2-mcp-server** (kakimochi) — ROS2 robot control with a dynamic gateway architecture. Community.

The breadth of ROS MCP implementations — seven servers from different authors — signals strong demand for AI-robot integration. The variety also reflects different trade-offs: native ROS bindings vs. rosbridge WebSocket, ROS1 vs. ROS2-only, research-oriented vs. production-ready.

## Simulation Platforms

Simulation is critical for autonomous vehicle development — testing AV algorithms in the real world is expensive, slow, and dangerous. MCP servers for simulation platforms let AI agents set up scenarios, run tests, and analyze results through natural language.

### isaac-sim-mcp (omni-mcp)

**Repository:** omni-mcp/isaac-sim-mcp (~57 stars) | **Requires:** NVIDIA Isaac Sim 4.2.0+

NVIDIA Isaac Sim is one of the leading physics-based simulation environments for robotics and autonomous vehicles. This MCP server enables natural language control of the full simulation environment:

- **Robot spawning** — add robots to scenes including Franka (manipulator arm), Jetbot (wheeled robot), Carter (mobile platform), G1 and Go1 (quadruped/humanoid)
- **Obstacle creation** — place and configure obstacles for path planning tests
- **Scene manipulation** — arrange environments for specific testing scenarios
- **Physics control** — manage simulation parameters and execution

This enables workflows like "create a warehouse scene with a Franka arm, add three randomly placed obstacles, and run 100 grasping trials" — all controlled by an AI agent through natural language rather than manual scene setup through the GUI.

The server requires a working NVIDIA Isaac Sim installation (4.2.0+), which in turn requires NVIDIA GPUs with RTX capabilities. This limits accessibility but reflects the compute requirements of physics-based AV simulation.

### SUMO-MCP-Server (HypaSMarty)

**Repository:** HypaSMarty/SUMO-MCP-Server (~2 stars) | **License:** MIT | **Academic:** arXiv paper available

Eclipse SUMO (Simulation of Urban Mobility) is an open-source traffic simulation platform widely used in transportation research. This MCP server exposes SUMO's capabilities through natural language:

- **OpenStreetMap data integration** — import real-world road networks
- **Road network generation** — create and modify simulated road infrastructure
- **Demand modeling** — define traffic patterns and vehicle flows
- **Simulation execution** — run and monitor traffic simulations
- **Signal optimization** — test and optimize traffic signal timing

The accompanying arXiv paper documents the academic use case — using AI agents to iteratively design, simulate, and optimize traffic scenarios without requiring expertise in SUMO's complex configuration files. This represents an important pattern: MCP lowering the barrier to entry for domain-specific simulation tools.

## Mapping and Navigation — The Most Mature Category

Mapping servers represent the most mature and commercially supported category in the transportation MCP ecosystem. Multiple official vendor servers from major mapping platforms sit alongside a deep community ecosystem.

### Official Mapping Servers

**Mapbox MCP Server** (mapbox, ~325 stars) | Official | Hosted endpoint

Mapbox's official MCP server provides the broadest set of location-based tools:

- **Geocoding** — forward and reverse address resolution
- **POI search** — point of interest discovery
- **Multi-modal routing** — driving, walking, cycling with real-time traffic
- **Travel time matrices** — origin-destination time calculations for fleet planning
- **Route optimization** — traveling salesman problem (TSP) solving for 2-12 stops
- **Isochrones** — reachability analysis (what areas are within X minutes?)
- **Map matching** — snap GPS traces to road networks
- **Static maps** — generate map images for reports and dashboards

The route optimization and travel time matrix features are particularly relevant for fleet operations — they enable AI agents to solve vehicle routing problems that would traditionally require specialized operations research software.

**TomTom MCP** (tomtom-international, ~44 stars) | Official | Apache 2.0

TomTom's official server emphasizes automotive-specific features:

- **Geocoding and reverse geocoding** — address resolution
- **Fuzzy search and POI search** — flexible location discovery
- **Routing** — standard driving directions
- **EV-specific routing** — routes optimized for electric vehicle range and charging needs
- **Traffic incidents** — real-time congestion and incident data
- **EV charging station finder** — locate charging infrastructure along routes

The EV-specific routing is a standout feature — it accounts for battery state, vehicle model range, and charging station locations to produce routes that are actually drivable by electric vehicles. As EV fleets grow, this becomes a critical capability.

**Baidu Maps MCP** (baidu-maps) | Official

The first MCP map server in China, providing 10+ APIs:

- Geocoding and reverse geocoding
- POI search
- Route planning (driving, transit, walking, cycling)
- Weather data
- IP geolocation
- Real-time traffic conditions

Essential for any transportation application operating in mainland China, where Google Maps is not available and local mapping providers dominate.

**Google Maps Platform AI** (googlemaps) | Official

Google's official offering focuses on grounding AI coding assistants in Google Maps Platform documentation rather than providing direct API access. It's a Code Assist toolkit designed to help developers build Maps Platform integrations correctly.

### Community Google Maps Servers

- **mcp-google-map** (cablate, ~224 stars) — 18 tools including geocode, reverse-geocode, search-nearby, places, directions, distance-matrix, elevation, timezone, weather, air-quality, and static-map generation. The most comprehensive community Google Maps implementation.
- **google-maps-comprehensive-mcp** (vicpeacock) — 8 tools using the latest Google Maps APIs.
- **MCP-Google-Maps** (ArtixZ) — Google Maps integration for Claude, Cursor, and ChatGPT.

### OpenStreetMap and Open Source

**osmmcp** (NERVsystems, ~17 stars) | **Language:** Go | No API key required

The most feature-rich open-source mapping MCP server with 25 tools:

- **Geocoding** — via Nominatim (no API key)
- **OSRM routing** — open-source routing engine
- **Overpass queries** — raw OSM data queries for any feature type
- **Nearby POI search** — find points of interest by category
- **EV charging stations** — locate charging infrastructure
- **Neighborhood livability analysis** — composite scoring of amenities, transit, safety
- **Commute comparison** — compare commute times across transport modes
- **CO2 emission estimates** — carbon footprint calculations for route choices

The lack of API key requirements makes osmmcp particularly attractive for development and prototyping. The CO2 estimation and livability analysis features go beyond basic mapping into urban planning territory.

**valhalla-mcp** (aatakansalar) | Valhalla routing engine

Connects to the Valhalla open-source routing engine:

- **Multi-modal routing** — driving, walking, cycling, and public transit
- **Isochrones** — reachability polygons
- **Time and distance matrices** — origin-destination calculations
- **Map matching** — GPS trace to road network alignment

**osm-mcp** (wiseman) — OSM data with Leaflet web viewer and PostGIS query interface for spatial analysis.

**open-streetmap-mcp** (jagan-shanmugam) — Location services with EV charging station finder integration.

### Regional Mapping Servers

- **amap-mcp-server** (sugarforever) — AMap (Gaode Maps) for China. Essential alongside Baidu for Chinese market coverage.
- **naver-map-mcp** (num2k) — Naver Maps for South Korea, where Naver dominates local mapping.
- **yandex-maps-mcp** (peschinskiy) — Yandex Maps for Russia and CIS countries.
- **mcp_tianditu** (bailaohe) — Tianditu, China's national mapping service operated by the government.

### GIS (Geographic Information Systems)

For advanced spatial analysis beyond standard mapping:

- **gis-mcp** (mahdin75) — Integrates Shapely, PyProj, GeoPandas, Rasterio, and PySAL for full geospatial analysis workflows.
- **MCP-Server-ArcGIS-Pro-AddIn** (nicogis) — Bridges Esri's ArcGIS Pro desktop GIS to MCP.
- **gis-dataconversion-mcp** (ronantakizawa) — GIS file format conversion between common spatial data formats.
- **QGIS MCP servers** (jjsantos01, kicker315, syauqi-uqi) — Multiple independent QGIS implementations for the popular open-source GIS platform.

## Fleet Management and Telematics

Fleet management connects the physical world of vehicle operations to digital monitoring and optimization.

### flespi-mcp-server (gperezt222)

**Repository:** gperezt222/flespi-mcp-server (~2 stars) | **License:** MIT | **Language:** Node.js

Flespi is a telematics middleware platform, and this MCP server exposes an exceptionally broad tool surface — 157 MCP tools covering:

- **Device management** — configure and monitor GPS trackers
- **GPS tracking** — real-time vehicle position data
- **Data channels** — stream telematics data flows
- **Geofencing** — define and monitor geographic boundaries
- **Asset tracking** — manage tracked assets beyond vehicles
- **Fleet grouping** — organize vehicles into logical groups
- **SMS and commands** — send messages and commands to devices

The 157-tool count is among the highest for any single MCP server in any domain. This breadth reflects the complexity of telematics platforms, which must handle diverse hardware (GPS trackers from dozens of manufacturers), communication protocols, and fleet management workflows.

### Additional Fleet Servers

- **fleet-mcp** (karmine05) — FleetDM integration using osquery-based device management. While FleetDM is primarily an IT fleet management tool (laptops, servers), its osquery foundation provides hardware inventory and compliance monitoring capabilities applicable to vehicle-mounted computing platforms.
- **flightctl-mcp** (flightctl) — Flight Control with read-only API access for devices and fleets. Designed for edge device fleet management, relevant to managing compute hardware deployed in vehicles.

## Tesla and Vehicle Data

Tesla's connected vehicle ecosystem has generated the most vehicle-specific MCP servers of any automaker, reflecting both the brand's data-rich platform and its developer community.

### teslamate-mcp (cobanov)

**Repository:** cobanov/teslamate-mcp (~124 stars)

TeslaMate is an open-source Tesla data logger that stores vehicle telemetry in PostgreSQL. This MCP server provides 18 predefined queries against that data:

- **Battery health** — state of health tracking and degradation analysis over time
- **Driving statistics** — trip distances, efficiency, speed profiles
- **Charging patterns** — charging frequency, energy consumed, preferred chargers
- **Tire pressure** — historical pressure readings and anomaly detection
- **Firmware history** — software update tracking and timeline

This is a read-only analytics server — it queries historical data rather than sending commands to vehicles. The battery degradation analysis is particularly valuable for fleet operators managing Tesla vehicles, where understanding battery health trends affects resale value and operational planning.

### tessie-mcp (keithah)

**Repository:** keithah/tessie-mcp | **Tools:** 39+

Tessie is a third-party Tesla management platform, and this MCP server provides the broadest set of vehicle interaction tools:

- **Battery and charging** — state of charge, charging status, charge scheduling
- **Driving data** — location, odometer, trip information
- **Vehicle commands** — lock/unlock doors, control climate, set speed limits, enable/disable sentry mode
- **Location tracking** — real-time vehicle position

Unlike TeslaMate, Tessie MCP includes write operations — it can send commands to vehicles. This enables AI agent scenarios like "if the temperature drops below freezing tonight, pre-heat my car at 7 AM" or "lock all fleet vehicles after 10 PM."

### tesla-mcp (scald)

**Repository:** scald/tesla-mcp (~13 stars)

A direct Tesla Fleet API integration providing:

- **Wake up** — wake sleeping vehicles for command execution
- **Vehicle refresh** — force data refresh from vehicle
- **Debug information** — diagnostic and troubleshooting data

This is a lighter-weight implementation focused on fleet API operations rather than the full telematics and command surface of Tessie.

## OBD-II and CAN Bus Diagnostics

On-board diagnostics and CAN bus communication are fundamental to vehicle health monitoring and autonomous vehicle development.

### MCP-CAN (farzadnadiri)

**Repository:** farzadnadiri/MCP-CAN (~4 stars) | **License:** MIT | **Language:** Python

A virtual CAN bus MCP server that brings automotive network analysis to AI agents:

- **Virtual CAN bus** — software-simulated CAN network (no physical hardware required)
- **DBC file decoding** — parse industry-standard database files that define CAN message formats
- **ECU simulator** — simulate electronic control unit behavior
- **OBD-II requests** — query standard diagnostic parameters
- **Frame reading** — capture and decode raw CAN bus frames
- **Signal monitoring** — track specific signals over time

The virtual CAN bus approach makes this server valuable for development and testing without physical vehicle access. DBC file support is particularly important — these files define the proprietary message formats used by different vehicle manufacturers, and being able to decode them through an AI interface simplifies reverse engineering and diagnostics workflows.

### Vehicle-Diagnostic-Assistant (castlebbs)

**Repository:** castlebbs/Vehicle-Diagnostic-Assistant

A practical diagnostic tool using physical ELM327 OBD-II adapters:

- **PID queries** — read RPM, vehicle speed, coolant temperature, throttle position
- **DTC decoding** — read and interpret diagnostic trouble codes
- **VIN lookup** — retrieve vehicle identification information

This server connects AI agents to actual vehicles through the standard OBD-II port, enabling conversational vehicle diagnostics. An AI agent could walk a non-technical user through diagnosing a check engine light by reading DTCs and explaining what they mean in plain language.

## Public Transit

Public transit MCP servers provide schedule data, real-time updates, and disruption information for railway and urban transit systems across multiple countries.

### Railway Systems

- **ns-mcp-server** (r-huijts) — Dutch Railways (NS). Schedules, real-time departure/arrival updates, and service disruptions for the Netherlands rail network.
- **12306-mcp** (Joooook) — China Railway. Ticket search and availability for China's national rail system (12306 is the official booking platform).
- **sbb-mcp-server** (ralf-boltshauser) — Swiss Federal Railways (SBB). Schedule queries for Switzerland's famously punctual rail network.
- **indian-railway-mcp** (amith-vp) — Indian Railways. Train search, seat availability, and live running status for one of the world's largest rail networks.

### Urban Transit

- **mcp-hk-transport-eta** (kennyfong19931) — Hong Kong public transport estimated time of arrival across buses, MTR, ferries, and trams.
- **sg-lta-mcp** (arjunkmrm) — Singapore Land Transport Authority. Bus arrivals, MRT status, traffic conditions, and carpark availability.
- **MTA MCP** (ckorhonen) — New York City MTA. Subway arrival predictions, service status alerts, and trip planning across NYC's subway system.

The geographic spread — Netherlands, China, Switzerland, India, Hong Kong, Singapore, and New York — illustrates both the global demand for transit AI integration and the fragmented nature of the ecosystem. Each transit authority has its own APIs, data formats, and update frequencies, making MCP's standardization layer particularly valuable.

## Ride-Sharing

### mcp-uber (199-mcp)

**Repository:** 199-mcp/mcp-uber (~7 stars) | **Auth:** OAuth 2.0

The only ride-sharing MCP server currently available:

- **Price estimates** — get fare estimates before booking
- **Ride requests** — book rides programmatically
- **Status monitoring** — track active ride progress
- **Cancellation** — cancel pending or active rides

Supports both sandbox (testing) and production environments. The OAuth 2.0 implementation handles Uber's authentication flow, which requires user consent for ride-booking permissions.

The absence of servers for Lyft, Bolt, Grab, Didi, and other ride-sharing platforms represents a significant gap for multimodal trip planning.

## EV Charging

Electric vehicle charging infrastructure is a growing MCP category, driven by fleet electrification and the complexity of EV route planning.

### mcp_ev_assistant_server (Abiorh001)

**Repository:** Abiorh001/mcp_ev_assistant_server | **Language:** Python | **Data:** Open Charge Map API

A comprehensive EV-focused planning server:

- **Charging station finder** — locate stations by connector type (CCS, CHAdeMO, Type 2)
- **EV trip planner** — plan routes that account for charging stops
- **Range-aware routing** — adjust routes based on current battery state and vehicle range

The range-aware routing is the key differentiator — rather than just finding chargers, it plans complete trips that factor in battery consumption, charging speed at different stations, and the total time cost of charging stops.

### chargenow-mcp (cevatkerim)

**Repository:** cevatkerim/chargenow-mcp | **Data:** ChargeNow API

Focused on real-time charging station data:

- **Station search** — find nearby charging stations
- **Real-time availability** — which connectors are currently free vs. occupied
- **Connector types** — filter by CCS, CHAdeMO, Type 2, Tesla Supercharger
- **Power levels** — distinguish between Level 2 (AC) and DC fast charging

Real-time availability data is critical for fleet operations — sending a delivery vehicle to an occupied charger wastes time and reduces fleet productivity.

Note that TomTom MCP and osmmcp also include EV charging station discovery as part of their broader feature sets.

## Automotive Engineering and Compliance

### Automotive-MCP (Ansvar-Systems)

**Repository:** Ansvar-Systems/Automotive-MCP (~3 stars) | **Tools:** 5

Focused on automotive cybersecurity compliance — a critical concern as vehicles become software-defined platforms:

- **UN R155/R156** — UNECE regulations on cybersecurity and software updates for vehicles
- **ISO/SAE 21434** — automotive cybersecurity engineering standard
- **VDA TISAX** — German automotive industry information security assessment
- **SAE J3061** — cybersecurity guidebook for cyber-physical vehicle systems
- **AUTOSAR Security** — security extensions for the AUTOSAR automotive software architecture
- **Chinese GB/T standards** — China's national automotive cybersecurity requirements

The server provides sub-millisecond FTS5 full-text search across approximately 360KB of regulation content. This enables AI agents to quickly answer questions like "what does ISO 21434 require for threat analysis and risk assessment of an OTA update system?"

### automotive-claude-code-agents (theja0473)

**Repository:** theja0473/automotive-claude-code-agents

Claude Code skills (not an MCP server per se, but MCP-adjacent) for automotive engineering workflows:

- **ISO 26262** — functional safety for road vehicles
- **ASPICE Level 3** — automotive software process improvement and capability determination
- **AUTOSAR 4.4** — automotive open system architecture for software components

These skills guide AI coding assistants through automotive-specific development practices, ensuring generated code and documentation comply with industry standards.

## Adjacent Transportation: Drones, Aviation, and Maritime

Transportation extends beyond road vehicles. Several MCP servers cover aerial and maritime domains.

### Aviation

- **aviation-mcp** (blevinstein) — FAA APIs for weather briefings, NOTAMs (Notices to Air Missions), aeronautical charts, and aircraft information.
- **aerospace-mcp** (cheesejaguar) — Airport resolution, great-circle route calculation, aircraft performance data, and orbital mechanics computations.
- **mcp-server-flight-aware-aeroapi** (mikedarke) — FlightAware integration for real-time flight tracking, status updates, and historical flight data.

### Drones

- **drone-mcp** (0xKoda) — DJI Tello drone control via MCP. Basic flight commands (takeoff, land, movement, rotation) for the consumer Tello drone.

### Maritime

- **mcp-shipxy-api** (garrettXu, ~9 stars) — Maritime location-based services including vessel tracking, port and berth data, route planning for ships, and marine weather.
- **marinetraffic-mcp-server** (Cyreslab-AI) — Real-time vessel position tracking via MarineTraffic data.

### License Plate Recognition

- **Omni-LPR** — Self-hosted automatic license plate recognition (ALPR) with both REST API and MCP interfaces. Relevant for parking management, toll systems, and fleet tracking.

## Comprehensive Server Comparison

| Server | Category | Author/Org | Key Capability | Official? |
|--------|----------|------------|----------------|-----------|
| ros-mcp-server (~1,100 stars) | ROS | robotmcp | ROS1+ROS2, bidirectional AI-robot comms, topic pub/sub | No |
| rosbridge-mcp-server | ROS | TakanariShimbo | ROS via WebSocket, no native ROS install needed | No |
| ros2_mcp | ROS | L-CAS (Lincoln) | ROS2, VLM integration, Docker, academic | No |
| ros-mcp | ROS | Yutarop | Natural language ROS control | No |
| ros_mcp_server | ROS | lpigeon | Natural language to ROS commands | No |
| ros2_mcp | ROS | wise-vision | Advanced ROS2 bridging | No |
| ros2-mcp-server | ROS | kakimochi | ROS2 dynamic gateway | No |
| isaac-sim-mcp (~57 stars) | Simulation | omni-mcp | NVIDIA Isaac Sim natural language control | No |
| SUMO-MCP-Server (~2 stars) | Simulation | HypaSMarty | Eclipse SUMO traffic simulation | No |
| Mapbox MCP (~325 stars) | Mapping | mapbox | Routing, TSP, isochrones, map matching | Yes |
| TomTom MCP (~44 stars) | Mapping | tomtom-international | EV routing, traffic incidents, charging finder | Yes |
| Baidu Maps MCP | Mapping | baidu-maps | First Chinese MCP map server, 10+ APIs | Yes |
| Google Maps Platform AI | Mapping | googlemaps | Code Assist for Maps Platform docs | Yes |
| mcp-google-map (~224 stars) | Mapping | cablate | 18 Google Maps tools | No |
| google-maps-comprehensive-mcp | Mapping | vicpeacock | 8 tools, latest Google APIs | No |
| MCP-Google-Maps | Mapping | ArtixZ | Google Maps for Claude/Cursor/ChatGPT | No |
| osmmcp (~17 stars) | Mapping | NERVsystems | 25 tools, EV charging, CO2 estimates, no API key | No |
| osm-mcp | Mapping | wiseman | OSM + Leaflet viewer + PostGIS | No |
| open-streetmap-mcp | Mapping | jagan-shanmugam | Location services + EV charging | No |
| valhalla-mcp | Mapping | aatakansalar | Valhalla routing, multimodal, isochrones | No |
| amap-mcp-server | Mapping | sugarforever | AMap/Gaode (China) | No |
| naver-map-mcp | Mapping | num2k | Naver Maps (South Korea) | No |
| yandex-maps-mcp | Mapping | peschinskiy | Yandex Maps (Russia/CIS) | No |
| mcp_tianditu | Mapping | bailaohe | Tianditu (China national mapping) | No |
| gis-mcp | GIS | mahdin75 | Shapely, GeoPandas, PyProj, Rasterio | No |
| ArcGIS Pro MCP | GIS | nicogis | ArcGIS Pro integration | No |
| gis-dataconversion-mcp | GIS | ronantakizawa | GIS format conversion | No |
| flespi-mcp-server (~2 stars) | Fleet | gperezt222 | 157 tools, GPS, geofencing, asset tracking | No |
| fleet-mcp | Fleet | karmine05 | FleetDM/osquery device management | No |
| flightctl-mcp | Fleet | flightctl | Read-only device/fleet API | No |
| teslamate-mcp (~124 stars) | Vehicle Data | cobanov | 18 queries, battery health, driving stats | No |
| tessie-mcp | Vehicle Data | keithah | 39+ tools, vehicle commands, charging | No |
| tesla-mcp (~13 stars) | Vehicle Data | scald | Tesla Fleet API, wake/refresh | No |
| MCP-CAN (~4 stars) | OBD-II/CAN | farzadnadiri | Virtual CAN bus, DBC decoding, ECU sim | No |
| Vehicle-Diagnostic-Assistant | OBD-II | castlebbs | ELM327 OBD-II, DTC decoding, VIN lookup | No |
| ns-mcp-server | Transit | r-huijts | Dutch Railways schedules and disruptions | No |
| 12306-mcp | Transit | Joooook | China Railway ticket search | No |
| sbb-mcp-server | Transit | ralf-boltshauser | Swiss Federal Railways | No |
| indian-railway-mcp | Transit | amith-vp | Indian Railway search, seat availability | No |
| mcp-hk-transport-eta | Transit | kennyfong19931 | Hong Kong public transport ETA | No |
| sg-lta-mcp | Transit | arjunkmrm | Singapore LTA bus/MRT/traffic | No |
| MTA MCP | Transit | ckorhonen | NYC subway arrivals, service status | No |
| mcp-uber (~7 stars) | Ride-Sharing | 199-mcp | OAuth Uber: price, request, track, cancel | No |
| mcp_ev_assistant_server | EV Charging | Abiorh001 | EV trip planner, range-aware routing | No |
| chargenow-mcp | EV Charging | cevatkerim | Real-time charging availability | No |
| Automotive-MCP (~3 stars) | Compliance | Ansvar-Systems | UN R155, ISO 21434, TISAX cybersecurity | No |
| automotive-claude-code-agents | Compliance | theja0473 | ISO 26262, ASPICE, AUTOSAR skills | No |
| drone-mcp | Drones | 0xKoda | DJI Tello drone control | No |
| aviation-mcp | Aviation | blevinstein | FAA weather, NOTAMs, charts | No |
| aerospace-mcp | Aviation | cheesejaguar | Airport, great-circle, aircraft perf | No |
| FlightAware MCP | Aviation | mikedarke | Flight tracking and status | No |
| mcp-shipxy-api (~9 stars) | Maritime | garrettXu | Vessel tracking, port data, marine weather | No |
| marinetraffic-mcp-server | Maritime | Cyreslab-AI | Real-time vessel positions | No |
| Omni-LPR | Recognition | — | Self-hosted license plate recognition | No |

## Architecture Patterns

Four architecture patterns illustrate how transportation MCP servers compose into practical systems.

### Pattern 1: AI-Powered Fleet Operations Center

A fleet operations center combines telematics, mapping, traffic, and weather data to give fleet managers real-time visibility and AI-powered decision support.

```
┌─────────────────────────────────────────────────────────┐
│                   Fleet Operations Agent                 │
│           (Claude / GPT / Custom LLM Host)               │
└────────────┬──────────┬──────────┬──────────┬───────────┘
             │          │          │          │
     ┌───────▼──┐ ┌─────▼────┐ ┌──▼───────┐ ┌▼──────────┐
     │ flespi   │ │ Mapbox   │ │ TomTom   │ │ Weather   │
     │ MCP      │ │ MCP      │ │ MCP      │ │ MCP       │
     │(157tools)│ │(routing) │ │(traffic) │ │(forecast) │
     └───────┬──┘ └─────┬────┘ └──┬───────┘ └┬──────────┘
             │          │          │          │
     ┌───────▼──┐ ┌─────▼────┐ ┌──▼───────┐ ┌▼──────────┐
     │ GPS      │ │ Route    │ │ Real-time│ │ Weather   │
     │ Trackers │ │ Engine   │ │ Traffic  │ │ Service   │
     │ & Devices│ │ & Maps   │ │ Feed     │ │ API       │
     └──────────┘ └──────────┘ └──────────┘ └───────────┘

Data Flow:
  1. Agent queries flespi for all vehicle positions
  2. Agent queries TomTom for traffic incidents on fleet routes
  3. Agent uses Mapbox TSP to re-optimize delivery sequences
  4. Agent checks weather forecast for route hazards
  5. Agent sends re-routing commands to affected vehicles
  6. Agent generates shift summary with KPIs and anomalies
```

**Use case:** A logistics company with 200 delivery vehicles. The AI agent monitors real-time positions through flespi, detects a highway closure through TomTom traffic data, re-optimizes affected delivery routes using Mapbox's TSP solver, and proactively notifies drivers through the fleet management system — all without human dispatcher intervention for routine re-routing.

### Pattern 2: Autonomous Vehicle Development Pipeline

An AV development workflow chains ROS for vehicle control, Isaac Sim for simulation, SUMO for traffic scenarios, and mapping for ground truth.

```
┌─────────────────────────────────────────────────────────┐
│               AV Development Agent                       │
│        (Orchestrates test-simulate-analyze cycle)        │
└─────┬──────────┬──────────────┬──────────────┬──────────┘
      │          │              │              │
┌─────▼────┐ ┌───▼──────┐ ┌────▼─────┐ ┌─────▼────────┐
│ ros-mcp  │ │isaac-sim │ │SUMO-MCP  │ │ osmmcp /     │
│ server   │ │  -mcp    │ │ Server   │ │ Mapbox MCP   │
│(ROS1/2)  │ │(physics) │ │(traffic) │ │ (ground      │
│          │ │          │ │          │ │  truth maps)  │
└─────┬────┘ └───┬──────┘ └────┬─────┘ └─────┬────────┘
      │          │              │              │
┌─────▼────┐ ┌───▼──────┐ ┌────▼─────┐ ┌─────▼────────┐
│ ROS2     │ │ NVIDIA   │ │ Eclipse  │ │ OpenStreetMap │
│ Nodes &  │ │ Isaac    │ │ SUMO     │ │ / Mapbox     │
│ Topics   │ │ Sim      │ │ Simulator│ │ Tile Server  │
└──────────┘ └──────────┘ └──────────┘ └──────────────┘

Development Cycle:
  1. Agent imports real-world intersection from OSM via osmmcp
  2. Agent creates matching SUMO traffic scenario with realistic flows
  3. Agent spawns AV in Isaac Sim with sensor configuration
  4. Agent subscribes to ROS perception topics via ros-mcp-server
  5. Agent runs 1000 simulation iterations, varying conditions
  6. Agent analyzes collision/near-miss data and generates report
  7. Agent identifies edge cases for targeted re-testing
```

**Use case:** An AV startup testing intersection navigation. The AI agent imports a real intersection from OpenStreetMap, creates a SUMO traffic scenario with realistic vehicle and pedestrian flows, spawns an autonomous vehicle in Isaac Sim with LiDAR and camera sensors, runs thousands of simulation iterations with varying lighting and weather conditions, and produces a safety analysis report identifying edge cases that need additional development attention.

### Pattern 3: Multimodal Trip Planning Agent

A trip planning agent combines mapping, transit, ride-sharing, and EV charging to produce end-to-end multimodal journey plans.

```
┌─────────────────────────────────────────────────────────┐
│              Multimodal Trip Planning Agent               │
│        (Plans door-to-door journeys across modes)        │
└──┬────────┬────────┬────────┬────────┬────────┬─────────┘
   │        │        │        │        │        │
┌──▼───┐ ┌──▼───┐ ┌──▼───┐ ┌──▼───┐ ┌──▼───┐ ┌──▼──────┐
│Mapbox│ │TomTom│ │ MTA  │ │ Uber │ │ EV   │ │chargenow│
│ MCP  │ │ MCP  │ │ MCP  │ │ MCP  │ │asst  │ │  MCP    │
│(route│ │(EV   │ │(sub- │ │(ride │ │(range│ │(charger │
│ +iso)│ │route)│ │ way) │ │share)│ │plan) │ │avail.)  │
└──┬───┘ └──┬───┘ └──┬───┘ └──┬───┘ └──┬───┘ └──┬──────┘
   │        │        │        │        │        │
   ▼        ▼        ▼        ▼        ▼        ▼
 Driving  EV-aware  Transit  Ride     Charging  Real-time
 + walk   routing   sched.   prices   stops     charger
 options           + delays  + ETAs   planned   status

Trip Composition:
  1. User: "Get me from Brooklyn to Newark Airport by 3 PM"
  2. Agent generates candidate plans across all modes:
     a. Subway (MTA) → AirTrain → walk
     b. Uber to Penn Station → NJ Transit → AirTrain
     c. Drive (Mapbox) with parking cost estimate
     d. EV drive (TomTom) with charging stop if needed
  3. Agent ranks by time, cost, reliability, and carbon footprint
  4. Agent monitors chosen plan in real-time, re-plans if disrupted
```

**Use case:** A traveler in Brooklyn needs to reach Newark Airport. The agent queries MTA for subway schedules and current delays, gets Uber price estimates for key segments, calculates driving routes with parking costs via Mapbox, checks EV-specific routing through TomTom if the traveler has an electric car, and presents ranked options with time, cost, and carbon footprint for each. If the traveler chooses the subway option and a service disruption occurs mid-trip, the agent automatically re-plans using alternative modes.

### Pattern 4: Connected Vehicle Diagnostics Agent

A diagnostics agent combines vehicle telemetry, compliance data, and mapping for comprehensive vehicle health monitoring and proactive maintenance.

```
┌─────────────────────────────────────────────────────────┐
│           Connected Vehicle Diagnostics Agent             │
│     (Monitors health, predicts failures, ensures         │
│      compliance, routes to nearest service)               │
└──────┬──────────┬──────────┬──────────┬─────────────────┘
       │          │          │          │
 ┌─────▼────┐ ┌───▼─────┐ ┌──▼──────┐ ┌▼───────────┐
 │teslamate │ │ MCP-CAN │ │Automtve │ │ Mapbox /   │
 │  -mcp    │ │  (OBD)  │ │  -MCP   │ │ TomTom    │
 │(battery, │ │(live    │ │(compli- │ │ MCP       │
 │ driving  │ │ diag.)  │ │ ance)   │ │(service   │
 │ stats)   │ │         │ │         │ │ routing)  │
 └─────┬────┘ └───┬─────┘ └──┬──────┘ └┬───────────┘
       │          │          │          │
 ┌─────▼────┐ ┌───▼─────┐ ┌──▼──────┐ ┌▼───────────┐
 │TeslaMate │ │Vehicle  │ │ISO 21434│ │ Dealer /   │
 │PostgreSQL│ │CAN Bus  │ │UN R155  │ │ Service    │
 │ Database │ │& OBD-II │ │Reg. DB  │ │ Locations  │
 └──────────┘ └─────────┘ └─────────┘ └────────────┘

Diagnostics Flow:
  1. Agent reads battery degradation trend from TeslaMate
  2. Agent queries live OBD-II data for anomalous readings
  3. Agent cross-references fault codes with known issues
  4. Agent checks if vehicle software meets current regulations
  5. Agent finds nearest qualified service center via mapping
  6. Agent generates maintenance recommendation with urgency level
```

**Use case:** A fleet of Tesla vehicles monitored by an AI agent. The agent detects that vehicle #47 shows accelerating battery degradation through TeslaMate historical data, cross-references with OBD-II live readings showing elevated cell temperature variance, checks whether the current firmware version addresses known battery management issues, verifies the vehicle's cybersecurity compliance status against UN R155 requirements, and proactively schedules a service appointment at the nearest Tesla service center with a detailed diagnostic report.

## Regulatory and Ethical Considerations

Transportation is among the most heavily regulated sectors, and autonomous vehicles add layers of safety, liability, and ethical complexity that MCP implementations must address.

### Safety-Critical System Requirements

**Functional safety (ISO 26262).** Automotive systems are classified by Automotive Safety Integrity Levels (ASIL A through D). MCP servers that interact with vehicle control systems — even indirectly through ROS — must consider where they fit in the safety architecture. An MCP server that can publish ROS commands to a drive-by-wire system is potentially safety-critical. Current MCP servers generally lack formal safety analysis, which limits their use in production safety-critical systems.

**Cybersecurity regulations (UN R155/R156).** Since July 2024, all new vehicles sold in UNECE member countries must comply with cybersecurity management system requirements. MCP servers that connect to vehicle systems create new attack surfaces — an compromised MCP server could potentially send malicious commands to a vehicle. The Automotive-MCP server helps with compliance analysis, but the MCP protocol itself lacks automotive-specific security certifications.

**Software update management (UN R156).** Over-the-air updates must be tracked, validated, and auditable. MCP servers interacting with vehicle software systems should support audit logging and version tracking. The teslamate-mcp server's firmware history tracking provides a read-only example of this capability.

### Data Privacy and Ownership

**Vehicle telemetry data.** GPS tracking, driving behavior, and vehicle diagnostics data raise significant privacy concerns. Fleet management MCP servers like flespi handle location data that can reveal individual movement patterns. European GDPR, California's CCPA, and emerging vehicle data privacy regulations create compliance requirements for how this data is stored, processed, and shared.

**Connected car data markets.** Tesla, GM, Ford, and other automakers collect enormous volumes of vehicle data. Third-party MCP servers (like TeslaMate and Tessie) access this data through APIs whose terms of service may change. The long-term viability of these integrations depends on automaker data access policies, which are currently in flux as regulators debate vehicle data portability rights.

### Ethical Considerations for Autonomous Systems

**Transparency in AI decision-making.** When an AI agent re-routes a fleet of vehicles based on traffic data, the routing decisions should be explainable. MCP's structured tool interface provides some transparency — each tool call is logged with inputs and outputs — but the higher-level reasoning behind multi-step decisions requires additional observability infrastructure.

**Equitable access.** Multimodal trip planning agents risk optimizing for efficiency in ways that disadvantage communities with limited transit access. AI agents should be designed to surface equitable options, not just fast or cheap ones.

**Liability in autonomous operations.** When an AI agent issues commands to a vehicle through ROS MCP servers, liability for outcomes is unclear. The chain from user intent through AI reasoning through MCP tool calls through ROS commands through vehicle actuators creates a complex liability chain that existing automotive regulations don't fully address.

### Recommendations for MCP Developers in Transportation

1. **Implement read-only modes by default.** MCP servers connecting to vehicle systems should default to observation-only and require explicit, authenticated escalation for control operations.
2. **Log all tool invocations.** Every MCP tool call to a vehicle system should produce an immutable audit record including timestamp, caller identity, parameters, and response.
3. **Respect data minimization.** Collect and expose only the vehicle data needed for the specific use case — not everything available through the API.
4. **Consider fail-safe behavior.** If the MCP connection drops while a vehicle operation is in progress, the system should default to a safe state, not continue the last command indefinitely.
5. **Separate development from production.** Use virtual CAN buses (MCP-CAN) and simulation (Isaac Sim, SUMO) for development. Reserve real vehicle connections for validated, audited production deployments.

## Ecosystem Gaps Analysis

The transportation MCP ecosystem has significant strengths in mapping and ROS, but critical gaps remain across several domains.

### Critical Gaps

**No major AV simulation platforms.** CARLA, LGSVL, AirSim, and other widely used AV simulators lack MCP servers. Isaac Sim coverage exists but is the only physics-based simulator represented. This forces AV development teams to use custom integrations for their primary testing tools.

**No Autoware or Apollo integration.** Autoware (the leading open-source autonomous driving stack) and Apollo (Baidu's AV platform) have no MCP servers. These are the platforms where production AV software runs — their absence is a major gap.

**No NVIDIA DRIVE integration.** NVIDIA's production AV compute platform (as opposed to the simulation-focused Isaac Sim) lacks MCP connectivity.

**No V2X or C-V2X protocols.** Vehicle-to-Everything communication — V2V (vehicle-to-vehicle), V2I (vehicle-to-infrastructure), V2P (vehicle-to-pedestrian) — has zero MCP representation. As V2X infrastructure deploys (it represents 59.2% of smart transportation connectivity), this gap will become increasingly critical.

**No traffic signal control systems.** SCATS, SCOOT, and other adaptive traffic signal control systems have no MCP servers. The SUMO-MCP-Server simulates signals but doesn't connect to real traffic management infrastructure.

**No major fleet telematics platforms.** Geotab, Samsara, Verizon Connect, and other enterprise fleet telematics providers lack MCP servers. The flespi server covers the middleware layer but not the dominant end-user platforms.

**No ChargePoint or OCPP/V2G protocols.** ChargePoint (the largest EV charging network) and the Open Charge Point Protocol (the industry standard for charger communication) have no MCP coverage. Vehicle-to-Grid (V2G) bidirectional charging protocols are also absent.

**No Smartcar or connected car platforms.** Smartcar's unified connected car API (supporting 40+ vehicle brands) would be the ideal MCP integration point for multi-brand vehicle access, but it doesn't exist yet.

### Moderate Gaps

**No CAD/CAE tools.** Automotive design tools — CATIA, NX, SolidWorks, Creo — lack MCP servers. Vehicle design workflows remain disconnected from AI agent orchestration.

**No ADAS datasets.** The Waymo Open Dataset, nuScenes, KITTI, and other perception datasets used for ADAS (Advanced Driver Assistance Systems) development have no MCP access. AI agents cannot directly query or analyze perception training data.

**No functional safety tools.** Tools for ISO 26262 functional safety analysis (FMEA, FTA, HARA) lack MCP integration, even though the Automotive-MCP server covers cybersecurity compliance.

**No additional ride-sharing platforms.** Beyond Uber, Lyft, Bolt, Grab, Didi, and Mobility-as-a-Service (MaaS) platforms are unrepresented.

**No battery management systems.** BMS data — cell voltages, temperatures, state of health at the cell level — is not accessible through MCP. The TeslaMate server provides aggregate battery data but not cell-level BMS information.

**No HERE Maps or Waze.** HERE Maps (widely used in automotive OEM systems) and Waze (community-sourced traffic data) lack MCP servers, despite being major players in automotive mapping.

**No smart city platforms.** Urban mobility platforms, smart parking systems, congestion pricing APIs, and city-level transportation dashboards are absent from the MCP ecosystem.

### What Would Close the Most Important Gaps

The highest-impact new MCP servers would be:

1. **Smartcar MCP** — unified connected car API covering 40+ brands would instantly provide vehicle data access beyond Tesla
2. **CARLA MCP** — the dominant open-source AV simulator needs MCP integration for AI-driven testing workflows
3. **Autoware MCP** — connecting the leading open-source AV stack to AI agents would bridge the gap between simulation and production
4. **ChargePoint / OCPP MCP** — standardized charging network access for the largest EV charging provider
5. **Geotab or Samsara MCP** — enterprise fleet telematics access would enable production fleet AI operations

## Getting Started by Role

### AV Software Engineer

Start with **ros-mcp-server** for immediate AI-ROS integration. The server supports both ROS1 and ROS2, so it works regardless of which version your stack uses. Pair it with **isaac-sim-mcp** if you have NVIDIA hardware for simulation-in-the-loop testing. Use **SUMO-MCP-Server** to generate realistic traffic scenarios for your simulation environment. Read the arXiv paper accompanying SUMO-MCP-Server for academic grounding on MCP in transportation systems.

### Fleet Operations Manager

Begin with **Mapbox MCP** for route optimization — the TSP solver and travel time matrices are immediately useful for delivery and service fleet routing. Add **TomTom MCP** for real-time traffic incident awareness and EV-specific routing if you operate electric vehicles. If your fleet uses Flespi for telematics, **flespi-mcp-server** gives you 157 tools for GPS tracking and geofencing. For Tesla fleets, **teslamate-mcp** provides battery health and driving analytics.

### Urban Mobility Planner

Start with **osmmcp** — no API key required, 25 tools including CO2 estimates and neighborhood livability analysis. Add transit servers relevant to your city (**MTA MCP** for NYC, **sg-lta-mcp** for Singapore, etc.). Use **gis-mcp** for advanced spatial analysis with GeoPandas and Shapely. Combine with **valhalla-mcp** for open-source multimodal routing that includes public transit.

### Automotive Compliance Engineer

**Automotive-MCP** provides instant access to UN R155/R156, ISO 21434, VDA TISAX, and other cybersecurity regulations with sub-millisecond search. Pair with **automotive-claude-code-agents** for ISO 26262 functional safety and ASPICE Level 3 development process guidance. These tools help AI agents answer compliance questions accurately, but final compliance decisions require qualified human review.

### EV Infrastructure Developer

Start with **TomTom MCP** for EV-specific routing and charging station discovery. Add **mcp_ev_assistant_server** for range-aware trip planning with connector-type filtering. Use **chargenow-mcp** for real-time charging station availability. Combine with **osmmcp** for additional EV charging station data from OpenStreetMap. The ecosystem gap around ChargePoint and OCPP means you may need custom integrations for charging network management.

### Transportation App Developer

Start with the official mapping servers — **Mapbox MCP** for the broadest feature set or **Baidu Maps MCP** / **amap-mcp-server** for China market coverage. Add **mcp-google-map** (224 stars, 18 tools) for Google Maps features. Layer in transit and ride-sharing servers for multimodal capabilities. Use regional mapping servers (**naver-map-mcp** for Korea, **yandex-maps-mcp** for Russia) for market-specific coverage. Consider **mcp-uber** for ride-sharing integration, keeping in mind the current lack of Lyft/Bolt/Grab alternatives.

## What's Next

The transportation MCP ecosystem is at an early but active stage. Mapping and navigation are mature, with official participation from Mapbox, TomTom, Baidu, and Google. ROS integration is remarkably strong for a community-driven effort — seven independent implementations led by ros-mcp-server at 1,100 stars. Vehicle data access is Tesla-dominated but functional. Public transit coverage spans seven countries. Simulation, fleet management, and EV charging are represented but thin.

The critical missing pieces are the production AV platforms (Autoware, Apollo, NVIDIA DRIVE), the enterprise fleet platforms (Geotab, Samsara), the connected car APIs (Smartcar, HERE), and the charging infrastructure standards (ChargePoint, OCPP, V2G). Closing these gaps would transform the ecosystem from a collection of useful but isolated tools into a comprehensive platform for AI-driven transportation operations.

The regulatory landscape adds urgency. UN R155/R156 cybersecurity requirements are already mandatory for new vehicles in UNECE countries. ISO 21434 compliance is becoming a market expectation. As AI agents become more involved in vehicle operations — even indirectly through fleet management and route optimization — the need for MCP servers that support audit logging, access control, and safety-critical operation modes will grow.

For the latest developments in MCP across all domains, visit the [MCP server directory](/reviews/) or read our [introduction to MCP](/guides/what-is-mcp/). The transportation sector's combination of high market growth, safety-critical requirements, and multi-system complexity makes it one of the most compelling use cases for the Model Context Protocol — and one of the areas where the gap between what's possible and what's currently available is widest.


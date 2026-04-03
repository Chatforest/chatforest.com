---
title: "MCP for Aerospace & Defense — 120+ Integrations (2026)"
date: 2026-03-29T23:00:00+09:00
description: "120+ MCP servers for aerospace and defense — flight data, satellite tracking, orbital mechanics, aviation safety, defense intelligence, CAD/simulation, and cybersecurity."
og_description: "How AI agents connect to aerospace and defense tools via MCP. Covers Flightradar24, Ansys STK, NOTAM data, satellite tracking, defense intelligence, and 100+ more integrations."
content_type: "Guide"
card_description: "120+ MCP servers for aerospace and defense — flight data, satellite tracking, orbital mechanics, aviation safety, defense intelligence, CAD/simulation, cybersecurity, and government procurement. Architecture patterns included."
last_refreshed: 2026-03-29
---

Aerospace and defense represent some of the most technically demanding domains in engineering. A single aircraft program generates millions of design documents, simulation datasets, test results, supply chain records, and compliance artifacts across decades of development. Satellite operators track thousands of objects in orbit while managing ground station networks, spectrum allocations, and mission timelines. Defense organizations fuse intelligence from dozens of sources — signals, imagery, open-source, human — into situational awareness that must be both comprehensive and timely. The data is vast, the systems are fragmented, and the stakes are extraordinarily high.

MCP — the Model Context Protocol — provides a standardized way for AI agents to connect to aerospace and defense data systems. Rather than building custom integrations for each flight data provider, satellite tracking platform, CAD tool, or intelligence database, MCP-connected agents can query flight information, calculate orbital parameters, analyze engineering models, assess cybersecurity threats, and process geospatial intelligence through defined tool interfaces. The protocol transforms AI assistants from isolated chatbots into operational tools that can work across the aerospace and defense technology stack. For an introduction to MCP itself, see our [introduction to MCP](/guides/what-is-mcp/).

The aerospace and defense MCP ecosystem is emerging unevenly. Aviation has the most mature tooling, with an official Flightradar24 server and multiple community flight data integrations. Space operations are growing fast, anchored by the Ansys STK integration for mission engineering. Defense-specific servers are nascent but include intelligence fusion, procurement analysis, and OSINT tools. The adjacent engineering ecosystem — CAD, simulation, GIS, cybersecurity — is surprisingly rich and directly applicable to aerospace workflows.

This guide is research-based. We survey what MCP servers exist across the aerospace and defense landscape, analyze the architecture patterns they enable, and identify where significant gaps remain. We do not claim to have tested or used any of these servers hands-on — our analysis draws on published documentation, open-source repositories, vendor announcements, and industry research. [Rob Nugen](https://robnugen.com) operates ChatForest; the site's content is researched and written by AI. For background on MCP, see our [introduction to MCP](/guides/what-is-mcp/) and the [MCP server directory](/reviews/).

## Why Aerospace and Defense Need MCP

Aerospace and defense workflows present integration challenges that MCP is architecturally well-suited to address.

**Engineering data spans dozens of specialized tools.** An aircraft design moves through conceptual design in MATLAB/Simulink, detailed CAD in CATIA or SolidWorks, structural analysis in ANSYS or Nastran, CFD in Fluent or OpenFOAM, manufacturing planning in Delmia, and test data management in custom databases. An MCP-connected AI agent that can read across CAD platforms, simulation tools, and test databases could automate cross-referencing design parameters against requirements, flagging conflicts that currently require weeks of manual review.

**Flight operations generate continuous real-time data.** Airlines, air traffic control, and airport operators process millions of data points daily — radar tracks, weather reports, NOTAMs, aircraft performance data, fuel calculations, and maintenance records. MCP servers exposing flight data, aviation weather, and safety databases let AI agents correlate information across these sources for operational decision support.

**Space operations are inherently multi-domain.** Tracking a satellite constellation requires orbital mechanics calculations, ground station scheduling, spectrum management, space weather monitoring, and collision avoidance analysis — each handled by different software systems. MCP integration across these tools could give operators unified situational awareness.

**Defense intelligence requires data fusion at scale.** Intelligence analysts work across classified and unclassified systems, combining satellite imagery, signals intelligence, open-source reporting, social media analysis, geopolitical databases, and historical records. MCP provides a standardized way to connect AI assistants to diverse intelligence sources while maintaining access control boundaries.

**Supply chains are global and heavily regulated.** Aerospace supply chains span thousands of suppliers across dozens of countries, subject to ITAR (International Traffic in Arms Regulations), EAR (Export Administration Regulations), DFARS (Defense Federal Acquisition Regulation Supplement), and country-specific export controls. AI agents with MCP access to procurement databases, compliance tools, and supplier management systems could automate the compliance checking that currently consumes enormous analyst hours.

## Aviation and Flight Data MCP Servers

Aviation is the most mature aerospace sub-sector in the MCP ecosystem, with multiple flight data servers, an official vendor implementation, and specialized tools for weather, safety, and operations.

### Flights MCP — Leading Flight Search

**ravinahp/flights-mcp** | 177 stars | Flight search via MCP

According to repository documentation, this is the highest-starred flight-focused MCP server, providing search capabilities for flights. For aviation operations, this enables AI agents to look up flight information, schedules, and availability — useful for airline operations planning, travel logistics coordination, and competitive route analysis.

### Flightradar24 MCP — Official Vendor Implementation

**Flightradar24/fr24api-mcp** | 15 stars | Official Flightradar24 API via MCP

This is an official MCP server published by Flightradar24 itself — one of the few vendor-backed implementations in the aerospace space. It provides access to the FR24 API for real-time flight tracking. For defense and intelligence applications, real-time ADS-B tracking data is a key open-source intelligence input for monitoring military and civilian air traffic patterns.

### Flightradar24 Community Server

**sunsetcoder/flightradar24-mcp-server** | 46 stars | Community FR24 integration

A community-built Flightradar24 MCP server with higher star count than the official version, indicating strong demand for flight tracking capabilities. Provides real-time flight tracking data that can feed into aviation monitoring workflows.

### MCP Flight Search

**arjunprabhulal/mcp-flight-search** | 41 stars | Real-time flight search

Real-time flight search capabilities through MCP, enabling AI agents to query current flight status, routes, and schedules. Combined with other aviation data sources, this supports comprehensive flight operations monitoring.

### Flight Ticket MCP

**xiaonieli7/FlightTicketMCP** | 35 stars | Flight ticket queries

Flight ticket information queries, primarily serving the Chinese market. Demonstrates the international scope of aviation MCP tooling and the demand for airline booking data integration.

### AviationStack MCP

**Pradumnasaraf/aviationstack-mcp** | 17 stars | Real-time flight data via AviationStack API

Provides access to real-time flight data through the AviationStack API, covering airline flights, airport schedules, and aircraft types. For aerospace analytics, this offers structured data on global aviation operations — useful for market analysis, route optimization studies, and fleet utilization tracking.

### Aviation MCP

**blevinstein/aviation-mcp** | 7 stars | Multiple aviation API integrations

Integrates multiple aviation APIs into a single MCP server, providing a unified interface to diverse aviation data sources. This consolidation approach mirrors what many aerospace organizations need — a single AI interface across fragmented data providers.

### Aviation Weather MCP

**zealoushacker/aviation-weather-mcp** | 4 stars | Aviation weather from aviationweather.gov

Pulls aviation weather data from NOAA's Aviation Weather Center (aviationweather.gov). Aviation weather — METARs, TAFs, SIGMETs, PIREPs, and AIRMETs — is critical for flight planning, dispatch, and safety. An MCP server exposing this data lets AI agents incorporate current and forecast weather into flight operations recommendations.

### METAR MCP

**mangobanaani/metarmcp** | 1 star | METAR data from NOAA

Fetches METAR (Meteorological Aerodrome Reports) from NOAA's Aviation Weather Center. METARs are the standard format for reporting current airport weather conditions — temperature, wind, visibility, cloud cover, pressure — and are fundamental to aviation operations.

### Aviation Safety and Incident Analysis

**Ryan-Clinton/aviation-safety-risk-mcp** | Aviation safety risk assessment

**SloeGin/skybrary-mcp** | SKYbrary aviation safety database

**INQUIRELAB/llm-hfacs-mcp-integration** | 1 star | HFACS classification of ASRS reports

These servers address aviation safety analysis — one of the most data-intensive aspects of aerospace. The HFACS (Human Factors Analysis and Classification System) server is particularly notable: it applies the standard accident investigation framework to ASRS (Aviation Safety Reporting System) reports, potentially automating the classification work that safety analysts perform manually. SKYbrary is the definitive aviation safety knowledge base, and its MCP integration could give AI agents access to decades of accident investigation findings, safety recommendations, and best practices.

### SkyDelay Intelligence

**ShreyasDasari/SkyDelay-Intelligence** | 1 star | Aviation delay cascade analysis

Analyzes aviation delay economics and cascade impacts across 347 US airports. Flight delays cost the US aviation industry an estimated $33 billion annually. An AI agent with access to delay pattern data, weather feeds, and airline schedules could help identify cascade risk before delays propagate through hub airports.

### Avinode MCP

**kingler/avinode-mcp-server** | 1 star | Aviation charter operations

MCP integration with Avinode, the leading marketplace for private aviation and charter operations. This serves the business aviation segment — a growing market where AI-assisted booking, fleet management, and trip planning are increasingly valuable.

## Space Operations MCP Servers

Space operations MCP tooling is nascent but growing, anchored by the Ansys STK integration and several satellite tracking servers.

### Ansys STK MCP — Industry-Standard Mission Engineering

**alti3/stk-mcp** | 25 stars | Ansys/AGI Systems Tool Kit via MCP

This is the standout server in the space operations category. Ansys STK (Systems Tool Kit, formerly AGI STK) is the industry-standard Digital Mission Engineering platform used by military space commands, satellite operators, and defense agencies worldwide for orbital analysis, sensor coverage modeling, communication link budgets, and mission planning. An MCP integration means AI agents could automate the complex analysis workflows that currently require deep STK expertise — calculating satellite access windows, modeling radar coverage, planning constellation deployments, and running interference analyses.

### IO-Aerospace MCP Server

**IO-Aerospace-software-engineering/mcp-server** | 15 stars | Dedicated aerospace MCP

A dedicated aerospace MCP server from IO Aerospace, a software engineering company focused on space applications. This is one of the few purpose-built aerospace MCP implementations, signaling growing demand for AI integration in space operations.

### SpaceFrontiers MCP

**SpaceFrontiers/mcp** | 9 stars | Space Frontiers API

MCP server for the Space Frontiers API, providing access to space industry data. Space Frontiers focuses on making space data more accessible — a mission that aligns naturally with MCP's goal of connecting AI agents to specialized data sources.

### Satellite Tracking MCP

**Cyreslab-AI/satellitetracking-mcp-server** | 3 stars | Satellite tracking

Provides satellite tracking capabilities through MCP. Satellite tracking — knowing where objects are in orbit, when they'll pass over locations, and whether collision risks exist — is fundamental to both military space domain awareness and commercial satellite operations.

### Space-Track MCP

**kamiwaza-exp/space-track-mcp** | Space-Track.org integration

Integrates with Space-Track.org, the US Space Command's public catalog of space objects. Space-Track provides Two-Line Element (TLE) sets, conjunction data messages, and decay predictions for tracked objects. For defense applications, this is a primary input to space domain awareness — monitoring what's in orbit and identifying potential threats.

### Satellite Orbit Calculation MCP

**xiaosongshu2020/mcp-server-satellite-orbit** | 2 stars | Orbital calculations

Tools for satellite orbit calculations, enabling AI agents to compute orbital parameters, predict satellite positions, and plan observation windows. Orbital mechanics calculations are foundational to space operations but require specialized knowledge — MCP makes this capability accessible through natural language.

### Starlink Enterprise MCP

**ry-ops/starlink-enterprise-mcp-server** | 2 stars | Starlink fleet management

Manages Starlink terminal fleets through the Starlink Enterprise API. With SpaceX's Starlink constellation providing connectivity to military, maritime, and remote operations, fleet management of Starlink terminals is becoming an operational requirement for many defense and aerospace organizations.

### Space Industry Intelligence MCP

**apifyforge/space-industry-intelligence-mcp** | Launch risk, debris, spectrum analysis

Covers launch risk assessment, orbital debris analysis, spectrum interference, and regulatory compliance — the operational concerns that space industry participants must manage daily. As the space environment becomes more congested (over 10,000 active satellites as of 2025), these analytics become increasingly critical.

### Satellite Search Nearby

**wojtek9502/mcp_satellites_search_nearby** | Satellite pass prediction

Provides information about satellite passes near a given location. Useful for ground station scheduling, amateur satellite tracking, and identifying observation opportunities.

### Aerospace Materials — Outgassing MCP

**aerospace-mcp-tools/outgassing-mcp-server** | 1 star | Spacecraft material properties

Queries outgassing properties of materials through approved aerospace sources. Outgassing — the release of trapped gas from materials in vacuum — is a critical concern for spacecraft and satellite design. Materials that outgas excessively can contaminate optics, solar cells, and sensitive instruments. This server makes NASA's outgassing database accessible to AI agents assisting with materials selection.

### Aerospace MCP (General)

**cheesejaguar/aerospace-mcp** | 2 stars | Aviation and space information

A general-purpose aerospace MCP server providing aviation and space information. Serves as a broad-coverage tool for aerospace domain queries.

## Defense and Intelligence MCP Servers

Defense-specific MCP servers focus on intelligence analysis, procurement data, and operational awareness. This is a sensitive domain — most defense AI tools operate on classified networks and will never appear on GitHub. The servers below operate on unclassified data.

### World Intel MCP — Comprehensive Intelligence

**marc-shade/world-intel-mcp** | 16 stars | 100+ intelligence tools

The most comprehensive intelligence-focused MCP server, offering over 100 tools covering markets, conflict monitoring, military tracking, cyber threat intelligence, climate data, and news analysis. Includes a live Leaflet dashboard with 20 map layers. For defense analysts, this provides a broad-spectrum open-source intelligence capability through a single MCP interface.

### Defense Intel Platform

**MikeSchaef/defense-intel-platform** | Defense procurement analysis

Tracks federal procurement, maps the defense industrial base, and identifies investment signals across 3 million+ contract awards and 132,000+ companies. For defense industry analysts and acquisition professionals, this automates the procurement intelligence that currently requires manual FPDS (Federal Procurement Data System) searches.

### Iron Eye — EO/IR Target Classification

**CubeStar1/iron-eye** | 4 stars | Air-to-surface EO/IR classification

Implements YOLOv8-based classification on custom infrared images for detecting tanks, vehicles, and ships. While built around a gaming context (War Thunder), the underlying technology — electro-optical/infrared target classification — is directly relevant to defense ISR (Intelligence, Surveillance, Reconnaissance) applications.

### Russian OSINT MCP

**synth-me/ru-osint-mcp** | 4 stars | Russian military OSINT

Provides open-source intelligence data on Russian military assets. Given the current geopolitical landscape, OSINT on military capabilities is in high demand among defense analysts, journalists, and researchers.

### Defense.com MCP — Official Vendor

**defensedotcom/defense-mcp** | 3 stars | Official Defense.com server

An official MCP server from Defense.com, a cybersecurity company serving the defense sector. This represents one of the few official vendor implementations in the defense space.

### Virtual Duty Officer

**perfectstormai-ctrl/virtual-duty-officer** | 1 star | Military duty officer MCP

An MCP server designed to assist military duty officers — the personnel responsible for maintaining operational awareness and handling incidents during off-hours. Automating routine duty officer tasks (status checks, report compilation, alert routing) is a natural AI application.

### Global Military MCP

**martins-vds/global-military-mcp-server** | Military data server

A military data MCP server providing access to global military information.

### TerraWatch — Geopolitical Risk Intelligence

**kelivreno/TerraWatch** | Geopolitical risk across 195 countries

Provides geopolitical risk intelligence covering 195 countries. For defense planners and intelligence analysts, understanding the geopolitical risk landscape is essential for threat assessment, force posture planning, and diplomatic engagement.

## OSINT and Intelligence Analysis MCP Servers

Open-source intelligence (OSINT) is a critical capability for both military intelligence and defense industry competitive analysis. The OSINT MCP ecosystem is well-developed.

### Maigret MCP — Digital Identity Research

**BurtTheCoder/mcp-maigret** | 232 stars | Account discovery across public sources

Searches for user account information across public sources. In intelligence contexts, digital identity research is a fundamental OSINT technique for understanding networks of interest.

### OSINT Tools MCP

**frishtik/osint-tools-mcp-server** | 183 stars | Multiple OSINT tools

Bundles multiple OSINT tools into a single MCP server, providing a unified interface for open-source intelligence collection. For defense analysts, having diverse OSINT capabilities accessible through a single AI interface streamlines the collection phase of the intelligence cycle.

### Awesome OSINT MCP Servers

**soxoj/awesome-osint-mcp-servers** | 95 stars | Curated OSINT server directory

A curated list of OSINT-focused MCP servers, serving as a meta-directory for the intelligence analysis community. This resource helps analysts discover relevant OSINT tools available through MCP.

### ZoomEye MCP — Network Asset Intelligence

**zoomeye-ai/mcp_zoomeye** | 69 stars | Network asset queries

Provides network asset information queries through ZoomEye's internet scanning platform. For cybersecurity defense and intelligence applications, understanding what's exposed on the internet is essential for both defensive posture assessment and threat analysis.

### OpenCTI MCP — Threat Intelligence

**CooperCyberCoffee/opencti_mcp_server** | 26 stars | OpenCTI threat intelligence

Natural language interface to OpenCTI, an open-source threat intelligence platform. OpenCTI aggregates threat data from multiple feeds (MITRE ATT&CK, STIX/TAXII, custom sources) and this MCP integration lets AI agents query that aggregated intelligence.

### OSINT MCP (Comprehensive)

**badchars/osint-mcp-server** | 6 stars | 37 tools, 12 sources

Provides 37 OSINT tools across 12 data sources including Shodan, VirusTotal, Censys, SecurityTrails, and DNS reconnaissance. This breadth makes it a practical toolkit for defense intelligence analysts conducting initial reconnaissance.

## Cybersecurity MCP Servers

Cybersecurity is integral to defense operations. The cybersecurity MCP ecosystem is one of the most developed categories, with several high-star servers covering offensive and defensive security.

### Ghidra MCP — Reverse Engineering

**LaurieWired/GhidraMCP** | 8,073 stars | NSA Ghidra via MCP

The highest-starred cybersecurity MCP server, providing AI access to Ghidra — the NSA-developed reverse engineering framework. For defense applications, Ghidra is used to analyze malware, assess firmware security in weapons systems, and reverse-engineer adversary tools. MCP integration means AI agents can assist with the time-consuming work of binary analysis, function identification, and vulnerability discovery.

### HexStrike AI — Comprehensive Security Testing

**0x4m4/hexstrike-ai** | 7,737 stars | 150+ cybersecurity tools

Provides over 150 cybersecurity tools for penetration testing and vulnerability discovery. In defense contexts, comprehensive security testing is required for systems before deployment — from IT networks to weapons platforms. An AI agent with access to this breadth of security tools could accelerate the Authority to Operate (ATO) process.

### MCP for Security

**cyproxio/mcp-for-security** | 596 stars | SQLMap, FFUF, NMAP, Masscan

Bundles essential security scanning tools (SQLMap for SQL injection testing, FFUF for web fuzzing, NMAP for network discovery, Masscan for port scanning) into a single MCP server. These are the foundational tools that every security assessment begins with.

### MCP Security Hub

**FuzzingLabs/mcp-security-hub** | 498 stars | Nmap, Ghidra, Nuclei, SQLMap, Hashcat

Integrates five key security tools — Nmap for network scanning, Ghidra for reverse engineering, Nuclei for vulnerability scanning, SQLMap for database testing, and Hashcat for password analysis. This combination covers the core security assessment workflow.

### Shodan MCP — Internet Device Intelligence

**BurtTheCoder/mcp-shodan** | 118 stars | Internet-connected device reconnaissance

Provides access to Shodan's database of internet-connected devices. For defense applications, Shodan data reveals exposed industrial control systems, military network infrastructure, and critical infrastructure vulnerabilities. Understanding what's visible on the internet is a fundamental aspect of both defense and intelligence operations.

### VirusTotal MCP — Malware Analysis

**BurtTheCoder/mcp-virustotal** | 114 stars | File, URL, and IP analysis

Integrates VirusTotal's malware analysis capabilities. In defense cybersecurity operations, rapid identification of malicious files, URLs, and IP addresses is essential for incident response and threat hunting.

### NIST CSF 2.0 MCP — Compliance Framework

**rocklambros/nist-csf-2-mcp-server** | 54 stars | NIST Cybersecurity Framework

Provides access to the NIST Cybersecurity Framework 2.0, the standard compliance framework for US government and defense contractor systems. AI agents with access to NIST CSF data can help map security controls, identify gaps, and generate compliance documentation — a significant time sink in defense cybersecurity programs.

### DocSentinel — Security Document Assessment

**arthurpanhku/DocSentinel** | 96 stars | Compliance gap analysis

Assesses cybersecurity documents for compliance gaps and risk. In defense environments where systems must meet NIST 800-171, CMMC, or other compliance frameworks, automated document assessment could dramatically accelerate the accreditation process.

## CAD, Simulation, and Engineering MCP Servers

Aerospace engineering relies heavily on CAD and simulation tools. The MCP ecosystem for engineering tools is well-developed, with official vendor implementations.

### MATLAB MCP — Official MathWorks Implementation

**matlab/matlab-mcp-core-server** | 285 stars | Official MATLAB via MCP

An official MCP server from MathWorks, the maker of MATLAB — perhaps the most widely used engineering computation platform in aerospace. MATLAB is used for everything from control system design and signal processing to data analysis and algorithm prototyping. An official MCP integration means AI agents can execute MATLAB code, run simulations, and process engineering data through the MATLAB environment. This is one of the most significant official vendor implementations in the MCP ecosystem.

### MATLAB Production Server MCP

**matlab/mcp-framework-matlab-production-server** | 15 stars | Deploy MATLAB functions as MCP tools

Publishes MATLAB functions as MCP tools through MATLAB Production Server. For aerospace organizations that have extensive MATLAB codebases — trajectory calculations, sensor fusion algorithms, structural analysis routines — this server exposes those capabilities to AI agents without rewriting them.

### Simulink MCP

**sohumsuthar/simulink-mcp** | 1 star | Load, inspect, modify, simulate Simulink models

Allows AI agents to load, inspect, modify, and simulate Simulink models. Simulink is the standard tool for model-based design in aerospace — flight control systems, avionics, power systems, and signal processing are all modeled in Simulink. MCP access to Simulink models could enable AI-assisted design review, parameter optimization, and automated testing.

### KiCAD MCP — Electronics Design

**mixelpixx/KiCAD-MCP-Server** | 535 stars | PCB design via MCP

The highest-starred CAD MCP server, connecting AI to KiCAD for PCB (printed circuit board) design. In aerospace, custom electronics are ubiquitous — from avionics boards to satellite payloads to missile guidance systems. AI-assisted PCB design could accelerate the electronics development cycle.

### CAD MCP — General CAD Automation

**daobataotie/CAD-MCP** | 286 stars | General CAD MCP server

A general-purpose CAD MCP server enabling AI interaction with CAD systems. Aerospace design involves extensive CAD work across multiple platforms, and a general CAD MCP interface could bridge AI agents to various design tools.

### FreeCAD MCP

**ATOI-Ming/FreeCAD-MCP** | 68 stars | FreeCAD automation

Automates FreeCAD through MCP. FreeCAD supports FEA (Finite Element Analysis) through its FEM workbench, making it relevant for structural analysis of aerospace components — stress analysis on airframe structures, thermal analysis of engine components, or vibration analysis of satellite deployments.

### Fusion 360 MCP

**AuraFriday/Fusion-360-MCP-Server** | 64 stars | Autodesk Fusion 360 via MCP

Controls Autodesk Fusion 360 through MCP. Fusion 360 combines CAD, CAM, and simulation in a cloud-based platform used by aerospace startups, drone manufacturers, and rapid prototyping shops. MCP integration enables AI-assisted design workflows from concept through manufacturing.

### MultiCAD MCP

**AnCode666/multiCAD-mcp** | 17 stars | Multiple CAD platforms

Uses multiple CAD software through a single AI interface. Aerospace programs often involve components designed in different CAD platforms (CATIA for airframes, SolidWorks for subsystems, Creo for engines). A multi-CAD MCP interface could help engineers work across platform boundaries.

### Solid Edge MCP

**tylerwagler/SolidEdge-MCP** | 4 stars | Siemens Solid Edge

Integrates Siemens Solid Edge for AI-assisted CAD design. Solid Edge is used in aerospace for mechanical design, particularly for smaller components and subsystem assemblies.

### Electronics and RF Engineering

**manwithacat/electronics-mcp** | Circuit modeling, SPICE simulation, schematic rendering

**glitchpatrick/rftools-mcp** | 200+ RF engineering calculators

These servers address electronics and RF engineering — critical aerospace disciplines. The RF Tools MCP provides over 200 calculators for radio frequency analysis, relevant to radar systems, communications links, electronic warfare, and antenna design. The Electronics MCP covers circuit modeling and SPICE simulation, essential for avionics and payload electronics development.

### Blender MCP — 3D Visualization

**poly-mcp/Blender-MCP-Server** | 31 stars | 51 tools for 3D modeling

Provides 51 tools for Blender 3D modeling and visualization. In aerospace, 3D visualization is used for mission planning, satellite constellation visualization, aircraft interior design, and technical documentation.

## Earth Observation and Satellite Imagery MCP Servers

Satellite imagery is a key input to both aerospace operations and defense intelligence. Several MCP servers provide access to earth observation data.

### SkyFi MCP — Commercial Satellite Imagery

**PSkinnerTech/SkyFi-MCP-server** | 3 stars | Enterprise satellite imagery

Enterprise-grade MCP server for the SkyFi satellite imagery platform. SkyFi aggregates imagery from multiple commercial satellite providers, offering a marketplace approach to earth observation data acquisition.

### Copernicus MCP — ESA Earth Observation

**wb1016/copernicus-mcp** | 2 stars | ESA Copernicus data access

Accesses ESA's Copernicus program data through the OData API. Copernicus provides free, open satellite data from the Sentinel constellation — radar imagery (Sentinel-1), optical imagery (Sentinel-2), ocean data (Sentinel-3), atmospheric composition (Sentinel-5P), and land monitoring. For defense applications, Sentinel-1 SAR (Synthetic Aperture Radar) imagery is particularly valuable as it works through clouds and at night.

### Sentinel Hub MCP

**ginkgo-tech/sentinelhub-mcp** | Copernicus Sentinel Hub integration

Integrates with the Sentinel Hub API for interacting with Copernicus satellite imagery through AI agents. Sentinel Hub provides on-the-fly processing of satellite data, enabling rapid analysis without downloading large raw datasets.

### Planetary Computer MCP

**isaaccorley/planetary-computer-mcp** | 2 stars | Microsoft Planetary Computer STAC API

Queries and downloads satellite imagery from Microsoft's Planetary Computer, which hosts petabytes of environmental monitoring data including Landsat, Sentinel, MODIS, and ASTER imagery collections.

### Google Earth Engine MCP

**kuzhang/mcp-gee-satellite-download** | 1 star | Automate Sentinel downloads via GEE

Automates satellite image downloads using Google Earth Engine. GEE provides access to decades of satellite imagery and geospatial datasets, making it a powerful platform for change detection, environmental monitoring, and intelligence analysis.

### GeoSight MCP

**armaasinghn/geosight-mcp** | Land cover, vegetation, water analysis

Analyzes land cover, vegetation indices, water bodies, and change detection from satellite imagery. Change detection — identifying what has changed between two satellite images — is a fundamental defense intelligence technique for monitoring military construction, force movements, and weapons development activities.

### Geo-Intelligence MCP

**Arvind-55555/Geo-Intelligence-MCP-Server** | Environmental analytics and geospatial intelligence

Integrates multiple GIS and satellite APIs for environmental analytics and geospatial intelligence. The explicit "geo-intelligence" framing signals defense/intelligence community applicability.

### EUMETSAT Weather MCP

**halprez/weather-mcp-server** | 1 star | EUMETSAT data with AI weather forecasts

Provides EUMETSAT historical satellite weather data with GraphCast and AIFS AI weather forecasts. Weather intelligence from satellite data is essential for military operations planning, flight operations, and maritime awareness.

## GIS and Mapping MCP Servers

Geospatial analysis underpins both aerospace operations (airspace management, ground station siting, launch range safety) and defense operations (terrain analysis, route planning, targeting).

### OpenStreetMap MCP

**jagan-shanmugam/open-streetmap-mcp** | 176 stars | Location-based services

Location-based services and geospatial data through OpenStreetMap. OSM data is widely used in defense for base mapping in areas where commercial or government mapping is limited.

### QGIS MCP Server

**jjsantos01/qgis_mcp** | 871 stars | QGIS Desktop via MCP

The leading open-source GIS MCP server, connecting AI to QGIS for spatial analysis, mapping, and data visualization. QGIS is used across defense and intelligence organizations for terrain analysis, infrastructure mapping, and operational planning.

### GIS MCP Server

**mahdin75/gis-mcp** | 126 stars | Programmatic GIS operations

Comprehensive geometry operations, coordinate transformations, and spatial analysis. For aerospace, this enables automated airspace boundary calculations, launch range safety zone analysis, and ground station coverage modeling.

### OSM MCP (wiseman)

**wiseman/osm-mcp** | 79 stars | OpenStreetMap data server

Direct access to OpenStreetMap data for geospatial analysis and mapping.

### GDAL MCP

**JordanGunn/gdal-mcp** | 59 stars | Geospatial data processing

GDAL-style geospatial workflows using Rasterio, GeoPandas, and PyProj. GDAL is the foundational library for geospatial data processing — reading, writing, and transforming raster and vector data across hundreds of formats.

### SUMO Traffic Simulation MCP

**XRDS76354/SUMO-MCP-Server** | 37 stars | Traffic simulation

Eclipse SUMO traffic simulation with OpenStreetMap data. While primarily a traffic simulator, SUMO is used in defense for modeling vehicle movement patterns, evacuation planning, and logistics route analysis.

### ArcGIS Pro MCP

**nicogis/MCP-Server-ArcGIS-Pro-AddIn** | 25 stars | Esri ArcGIS Pro integration

Integrates Esri ArcGIS Pro, the GIS platform widely used across US defense and intelligence agencies. ArcGIS is the standard GIS platform for the US Department of Defense and is embedded in numerous defense workflows from installation management to operational planning.

## Government Data and Procurement MCP Servers

Government data is essential for defense industry operations, procurement analysis, and compliance.

### US Government Open Data MCP

**lzinga/us-gov-open-data-mcp** | 91 stars | 40+ US government APIs, 250+ tools

Provides access to over 40 US government data APIs with 250+ tools, covering Treasury, FRED (Federal Reserve Economic Data), Congress, FDA, CDC, and more. For defense companies, government data on budgets, spending trends, and policy decisions directly impacts business strategy.

### Federal Data MCP Registry — GSA Official

**GSA-TTS/fed-data-mcp-registry** | 9 stars | Official GSA curated MCP registry

An official GSA (General Services Administration) registry of curated MCP servers for open government data. This is notable as a US government-endorsed approach to MCP, potentially signaling broader federal adoption.

### Government MCP Servers

**martc03/gov-mcp-servers** | 3 stars | 13 production servers for US government data

Thirteen production MCP servers providing access to US government data sources. For defense contractors and analysts, structured access to government data streamlines research, reporting, and compliance activities.

## Supply Chain and Compliance

### Supply Chain AI Agent System

**sagar0x0/Supply-Chain-Resilience-ai-agentic-system** | 2 stars | Supply chain disruption response

Detects, assesses, and responds to supply chain disruptions. In aerospace and defense, where single-source components and long lead times create acute supply chain vulnerabilities, AI-driven disruption detection could prevent production delays.

### Supply Chain Copilot

**lara-openai/agent-supply-chain-mcp** | 3 stars | Supply chain analysis via Databricks

OpenAI Agent SDK with Databricks MCP for supply chain analysis. Combines AI agent capabilities with Databricks' data processing for supply chain intelligence.

### UN Comtrade Supply Chain MCP

**AiAgentKarl/supply-chain-mcp-server** | Global trade data

Global supply chain and trade data via UN Comtrade and World Bank APIs. For defense supply chain analysis, understanding global trade flows in critical materials (rare earths, titanium, specialty alloys) is essential for supply chain resilience planning.

## Architecture Patterns

The following architecture patterns illustrate how aerospace and defense organizations can combine MCP servers into operational workflows.

### Pattern 1: AI-Powered Mission Planning Assistant

```
┌─────────────────────────────────────────────┐
│            Mission Planning Agent            │
│    (orbital analysis + ground scheduling)    │
└──────┬──────┬──────┬──────┬──────┬─────────┘
       │      │      │      │      │
  ┌────▼──┐┌──▼───┐┌─▼────┐┌▼────┐┌▼─────────┐
  │ STK   ││Space ││Sat   ││EUMET││ Starlink  │
  │ MCP   ││Track ││Orbit ││SAT  ││ Enterprise│
  │(orbit)││(TLE) ││(calc)││(wx) ││ (comms)   │
  └───────┘└──────┘└──────┘└─────┘└───────────┘
```

This pattern combines orbital mechanics (STK MCP for high-fidelity simulation), space domain awareness (Space-Track for conjunction assessment), orbit calculation (satellite position prediction), weather intelligence (EUMETSAT for launch/operations weather), and communications planning (Starlink for connectivity) into a unified mission planning capability. An AI agent orchestrating these tools could automate the sequence of analyses that mission planners currently perform manually: computing orbital windows, checking for conjunction risks, verifying ground station access, assessing weather constraints, and planning communication links.

### Pattern 2: Flight Operations Intelligence

```
┌─────────────────────────────────────────────┐
│        Flight Operations Agent              │
│   (real-time monitoring + safety analysis)  │
└──────┬──────┬──────┬──────┬──────┬─────────┘
       │      │      │      │      │
  ┌────▼──┐┌──▼───┐┌─▼────┐┌▼────┐┌▼─────────┐
  │ FR24  ││Flight││Aviat ││METAR││ SKYbrary  │
  │Official││Search││Wx   ││ MCP ││ (safety)  │
  │(track)││(data)││(TAF) ││     ││           │
  └───────┘└──────┘└──────┘└─────┘└───────────┘
```

This pattern fuses real-time flight tracking (Flightradar24), flight data (search and schedules), aviation weather (forecasts and current conditions), and safety databases (SKYbrary incident history) into an operations monitoring capability. An AI agent could correlate current weather conditions with flight tracks, identify aircraft operating in deteriorating weather, cross-reference with historical safety data for similar conditions, and generate proactive alerts for operations staff.

### Pattern 3: Defense Intelligence Fusion

```
┌─────────────────────────────────────────────┐
│         Intelligence Fusion Agent           │
│    (multi-source analysis + assessment)     │
└──────┬──────┬──────┬──────┬──────┬─────────┘
       │      │      │      │      │
  ┌────▼──┐┌──▼───┐┌─▼────┐┌▼────┐┌▼─────────┐
  │World  ││OSINT ││Geo-  ││Zoom ││ OpenCTI   │
  │ Intel ││Tools ││Intel ││ Eye ││ (threats) │
  │(100+) ││(183★)││(sat) ││(net)││           │
  └───────┘└──────┘└──────┘└─────┘└───────────┘
```

This pattern combines broad-spectrum intelligence (World Intel's 100+ tools), OSINT collection (digital identity research, social media analysis), satellite imagery analysis (GeoSight change detection), network asset intelligence (ZoomEye device scanning), and structured threat intelligence (OpenCTI) into a multi-source fusion capability. An AI agent could correlate geopolitical developments with satellite imagery changes, network activity shifts, and cyber threat indicators to produce integrated intelligence assessments.

### Pattern 4: Aerospace Engineering Design Review

```
┌─────────────────────────────────────────────┐
│        Engineering Review Agent             │
│   (cross-platform design verification)     │
└──────┬──────┬──────┬──────┬──────┬─────────┘
       │      │      │      │      │
  ┌────▼──┐┌──▼───┐┌─▼────┐┌▼────┐┌▼─────────┐
  │MATLAB ││Simul ││KiCAD ││Free ││ Outgas    │
  │Official││ink  ││(PCB) ││CAD  ││ (material)│
  │(calc) ││(ctrl)││(elec)││(FEA)││           │
  └───────┘└──────┘└──────┘└─────┘└───────────┘
```

This pattern connects MATLAB (analytical calculations, algorithm verification), Simulink (control system modeling), KiCAD (electronics design), FreeCAD (structural FEA), and the outgassing database (materials qualification) into an integrated design review capability. An AI agent could verify that control system parameters in Simulink match the MATLAB analysis, check that PCB layouts meet thermal constraints from the FEA model, and confirm that all materials pass outgassing requirements — automating the cross-disciplinary checks that typically require multiple specialist reviews.

## Ecosystem Comparison

| Category | Server Count | Top Stars | Official Vendors | Maturity |
|----------|-------------|-----------|-----------------|----------|
| Aviation / Flight Data | 15+ | 177 (Flights) | Flightradar24 | **High** |
| Space Operations | 10+ | 25 (STK) | None | Medium |
| Defense / Intelligence | 8+ | 16 (World Intel) | Defense.com | Low |
| OSINT | 6+ | 232 (Maigret) | None | **High** |
| Cybersecurity | 10+ | 8,073 (Ghidra) | None | **Very High** |
| CAD / Simulation | 15+ | 535 (KiCAD) | MathWorks (MATLAB) | **High** |
| Earth Observation | 8+ | 3 (SkyFi) | None | Low |
| GIS / Mapping | 10+ | 871 (QGIS) | None | **High** |
| Government Data | 3+ | 91 (US Gov) | GSA | Medium |

## Regulatory and Security Considerations

### Export Controls

Aerospace and defense are among the most heavily export-controlled industries. Key considerations for MCP deployments:

- **ITAR (International Traffic in Arms Regulations):** Any MCP server handling defense articles, technical data, or defense services must comply with ITAR. This means servers cannot be hosted on foreign infrastructure, accessed by foreign persons without authorization, or transfer controlled technical data across borders.
- **EAR (Export Administration Regulations):** Dual-use aerospace technology (encryption, certain sensors, propulsion technology) falls under EAR. MCP integrations with tools processing EAR-controlled data must implement appropriate access controls.
- **No ITAR-specific MCP servers exist yet.** This is a significant gap — compliance checking, classification determination, and export license tracking are all candidates for MCP automation.

### Classification and Information Security

- **Classified data stays on classified networks.** No MCP server on GitHub is appropriate for classified information. Defense organizations would need to deploy MCP servers on SIPR, JWICS, or equivalent classified enclaves.
- **CUI (Controlled Unclassified Information):** Even unclassified defense data often carries CUI markings requiring specific handling. MCP deployments processing CUI must meet NIST 800-171 requirements.
- **CMMC (Cybersecurity Maturity Model Certification):** Defense contractors must achieve appropriate CMMC levels. MCP infrastructure used in defense contracts must be included in the CMMC assessment scope.

### Safety-Critical Systems

- **DO-178C:** Software in airborne systems must comply with DO-178C (Software Considerations in Airborne Systems and Equipment Certification). AI agents interacting with avionics through MCP would need to be assessed within this framework.
- **Human-in-the-loop requirements:** Many aerospace and defense decisions require human authorization by regulation or policy. MCP architectures must maintain human oversight for safety-critical and weapons-related functions.
- **Verification and validation:** Aerospace software requires rigorous V&V. MCP tool outputs used in engineering decisions should be verified against established methods rather than trusted blindly.

### Data Sovereignty

- **FedRAMP:** Cloud infrastructure used by US government agencies must be FedRAMP authorized. MCP servers deployed in cloud environments for government work need FedRAMP compliance.
- **Allied data sharing:** NATO and Five Eyes partners have specific agreements governing data sharing. MCP deployments supporting allied operations must respect these frameworks.

## Major Gaps in the Ecosystem

Despite the breadth of available MCP servers, significant gaps remain for aerospace and defense:

**No major defense prime contractor has published an MCP server.** Lockheed Martin, Boeing, Northrop Grumman, Airbus, Raytheon, BAE Systems, General Dynamics, and L3Harris are all absent. Given the defense industry's conservative approach to open-source and the classification challenges, this is unsurprising but limits adoption.

**No space agency has an official MCP implementation.** NASA, ESA, JAXA, and other space agencies have not published MCP servers, though their data is accessible through community-built servers using public APIs.

**No dedicated CFD or FEA MCP servers exist.** Computational fluid dynamics and finite element analysis are foundational to aerospace engineering, but there are no MCP servers specifically for ANSYS Fluent, OpenFOAM, Nastran, Abaqus, or similar tools. The FreeCAD MCP includes basic FEM capabilities, but purpose-built simulation MCP servers are missing.

**No radar, sonar, or signal processing MCP servers.** These are core defense technologies with no MCP representation. The RF Tools MCP provides engineering calculators but not signal processing capabilities.

**No ITAR/export control compliance tools.** Given the regulatory burden, an MCP server that could check USML categories, determine export classification, or track license requirements would be immediately valuable.

**No flight management system (FMS) or avionics MCP integrations.** The aviation MCP ecosystem covers data and tracking but not cockpit systems or avionics interfaces.

**No air traffic management MCP servers.** Despite the complexity of ATC operations and the ongoing NextGen/SESAR modernization programs, no MCP servers address air traffic management directly.

**Palantir has no MCP presence.** Despite being the dominant defense analytics platform (Gotham, Foundry, Apollo), Palantir has not published MCP servers. Given Palantir's role in defense AI (Project Maven, numerous classified programs), this is a notable absence.

## Getting Started by Role

**Aerospace Engineer:** Start with the official MATLAB MCP server (285 stars) for analytical calculations, then add Simulink MCP for model-based design and KiCAD MCP (535 stars) for electronics. The FreeCAD MCP provides basic FEA capabilities. Use the outgassing MCP for materials selection in space applications.

**Satellite Operator:** The Ansys STK MCP (25 stars) is the essential starting point for orbital analysis. Add Space-Track MCP for conjunction assessment, the satellite tracking and orbit calculation servers for operational awareness, and Copernicus MCP for earth observation data. Starlink Enterprise MCP may be relevant for ground connectivity management.

**Aviation Professional:** Begin with the official Flightradar24 MCP (15 stars) for real-time tracking, add Aviation Weather MCP for weather intelligence, and the aviation safety servers (SKYbrary, HFACS) for safety analysis. The AviationStack MCP (17 stars) provides structured airline and airport data.

**Defense Analyst:** Start with World Intel MCP (16 stars) for broad-spectrum intelligence, add OSINT Tools MCP (183 stars) for collection, OpenCTI MCP (26 stars) for threat intelligence, and ZoomEye MCP (69 stars) for network reconnaissance. Use GIS servers (QGIS 871 stars, ArcGIS 25 stars) for geospatial analysis.

**Defense Cybersecurity Professional:** Ghidra MCP (8,073 stars) for reverse engineering, HexStrike AI (7,737 stars) for comprehensive security testing, NIST CSF MCP (54 stars) for compliance mapping, and Shodan MCP (118 stars) for exposure assessment. DocSentinel (96 stars) helps with compliance documentation.

**Defense Procurement Analyst:** The Defense Intel Platform for procurement data (3M+ awards), US Government Open Data MCP (91 stars) for federal data access, and the GSA Federal Data MCP Registry (9 stars) for curated government data sources. Supply chain MCP servers can help monitor material availability and trade flows.

## Conclusion

The aerospace and defense MCP ecosystem reflects the sector's unique characteristics: strong in data analysis and engineering tools, limited in operational systems due to classification and safety requirements. Aviation leads with the most mature tooling and an official vendor implementation (Flightradar24). The cybersecurity and engineering categories benefit from broad applicability beyond defense. Space operations are growing from a solid foundation in the Ansys STK integration.

The most impactful near-term opportunity is combining existing MCP servers into multi-tool workflows — mission planning assistants that integrate orbital mechanics with weather and communications, flight operations monitors that correlate tracking with weather and safety data, or engineering review agents that cross-check designs across platforms. These combinations leverage existing mature servers rather than waiting for purpose-built defense tools.

The long-term trajectory depends on whether defense organizations and their prime contractors embrace MCP as an integration standard. The protocol's architecture — separating tool capabilities from AI models — aligns well with defense requirements for access control, compartmentalization, and auditability. If major defense programs begin requiring MCP interfaces in their software deliverables, the ecosystem could expand rapidly.

For related coverage, see our guides on [MCP and IoT](/guides/mcp-iot-embedded-systems/), [MCP and supply chain logistics](/guides/mcp-supply-chain-logistics/), [MCP and cybersecurity](/guides/mcp-cybersecurity-threat-intelligence/), and the [MCP server directory](/reviews/).

---
title: "Digital Twins, 3D Modeling & Simulation MCP Servers — CAD, Physics, Game Engines, and Engineering Simulation"
date: 2026-03-16T22:00:00+09:00
description: "Digital twins, 3D modeling, and simulation MCP servers let AI agents control CAD tools, run physics simulations, manipulate game engines, and interact with engineering models. We reviewed 35+ servers across 6 subcategories. 3D modeling: ahujasid/blender-mcp (17.7k stars, Python — most popular 3D MCP, Poly Haven assets, Hyper3D Rodin), poly-mcp/Blender-MCP-Server (51 tools, HTTP endpoints), CommonSenseMachines/blender-mcp (text-to-4D worlds via CSM.ai). CAD: neka-nat/freecad-mcp (605 stars, Python — FreeCAD addon with 10 tools, parts library), BuildCAD AI MCP (free cloud CAD with multi-view renders), jhacksman/OpenSCAD-MCP-Server (multi-view reconstruction, parametric export), Svetlana-DAO-LLC/cad-agent (build123d + Docker, STL/STEP export). Fusion 360: Joe-Spencer/fusion-mcp-server (design resources, parameters), mycelia1/fusion360-mcp-server (script generation + execution). Game engines: IvanMurzak/Unity-MCP (1.3k stars, C# — 50+ tools, editor + runtime), CoderGamester/mcp-unity (1.4k stars, TypeScript/C# — 35+ tools, WebSocket bridge), chongdashu/unreal-mcp (1.6k stars, C++/Python — blueprint editing, actor management), flopperam/unreal-engine-mcp (592 stars — world building, maze generation, blueprint scripting). Physics simulation: chrishayuk/chuk-mcp-physics (Python — 55 tools, 10 physics categories, 98% test coverage), andylbrummer/math-mcp (GPU-accelerated quantum/molecular/neural simulations), Genesis-Embodied-AI/Genesis (28.3k stars — 43M FPS physics engine, not MCP but has dustland/genesis-mcp wrapper). Engineering simulation: omni-mcp/isaac-sim-mcp (136 stars, Python — NVIDIA Isaac Sim control, robot placement), Orthogonalpub/modelica_simulation_mcp_server (15 stars — Modelica ODE integration, natural language to differential equations), clanker-lover/spicebridge (ngspice circuit simulation, 18 tools). Gaps: no ANSYS/COMSOL/Abaqus MCP, no CFD server, no SolidWorks MCP, no digital twin platform integration (Azure/AWS IoT), limited FEA capabilities. 35+ servers across 6 subcategories. Rating: 4/5."
og_description: "Digital twins & simulation MCP servers: ahujasid/blender-mcp (17.7k stars — 3D modeling), chongdashu/unreal-mcp (1.6k stars — Unreal Engine), IvanMurzak/Unity-MCP (1.3k stars — Unity editor + runtime), neka-nat/freecad-mcp (605 stars — FreeCAD CAD). 35+ servers reviewed. Rating: 4/5."
content_type: "Review"
card_description: "Digital twins, 3D modeling, and simulation MCP servers for AI-powered CAD design, physics simulation, game engine control, and engineering workflows. **Blender dominates the 3D modeling space** — ahujasid/blender-mcp (17.7k stars, Python) is one of the most popular MCP servers in the entire ecosystem, connecting Blender to Claude AI through a socket-based server. It provides object creation and manipulation, material control, scene inspection, Python code execution in Blender, Poly Haven integration for free HDRIs/textures/assets, and Hyper3D Rodin for AI-generated 3D models. poly-mcp/Blender-MCP-Server exposes 51 tools over HTTP endpoints, turning Blender into a fully orchestrable MCP server for agent pipelines. CommonSenseMachines/blender-mcp bridges Blender with CSM.ai for text-to-4D world generation. dhakalnirajan/blender-open-mcp runs with local Ollama models instead of cloud APIs. **CAD tools cover the major open-source platforms** — neka-nat/freecad-mcp (605 stars, Python, MIT) runs as a FreeCAD addon with an RPC server, providing 10 tools for document/object creation, editing, deletion, Python execution, screenshots, and parts library access. Multiple alternative FreeCAD MCPs exist: proximile/FreeCAD-MCP adds Docker containerization and Vision AI analysis, spkane/freecad-addon-robust-mcp-server provides 150+ tools, and bonninr/freecad_mcp focuses on prompt-assisted design. For OpenSCAD parametric modeling, jhacksman/OpenSCAD-MCP-Server offers AI image generation with multi-view reconstruction and export to CSG/AMF/3MF/SCAD formats. quellant/openscad-mcp and fboldo/openscad-mcp-server provide simpler render-and-export workflows. jabberjabberjabber/openscad-mcp focuses on rapid prototyping with LLM-driven OpenSCAD code generation. BuildCAD AI provides a free cloud-based MCP server for CAD design with multi-view PNG renders (front/right/top/isometric) — works with any MCP client, requires a free account. Svetlana-DAO-LLC/cad-agent packages build123d modeling with VTK rendering in a Docker container, supporting STL/STEP/3MF export and printability analysis. **Fusion 360 has multiple MCP integrations** — Joe-Spencer/fusion-mcp-server exposes Fusion 360's design hierarchy, parameters, and metadata as MCP resources. mycelia1/fusion360-mcp-server generates and executes scripts directly in Autodesk Fusion 360. AuraFriday/Fusion-360-MCP-Server and ArchimedesCrypto/fusion360-mcp-server provide additional Fusion 360 control. No SolidWorks MCP server exists, which is a notable gap given its market share. **Game engines have the strongest ecosystem after Blender** — Unity has two major MCPs: IvanMurzak/Unity-MCP (1.3k stars, C#, MIT) provides 50+ tools across Project & Assets (20), Scene & Hierarchy (24), and Scripting & Editor (12), with Roslyn-based C# compilation, and works in both editor and runtime modes. CoderGamester/mcp-unity (1.4k stars, TypeScript/C#, MIT) bridges Unity Editor to AI assistants via WebSocket with 35+ tools for scene manipulation, component management, and test execution. CoplayDev/unity-mcp offers similar functionality with emphasis on asset management. Unreal Engine is equally well-served: chongdashu/unreal-mcp (1.6k stars, C++/Python, MIT) provides a C++ plugin for TCP communication with Unreal Editor plus a Python MCP server for actor creation, blueprint development, and viewport control. flopperam/unreal-engine-mcp (592 stars, Python, MIT) specializes in world building — towns, castles, mansions, mazes — with 23+ blueprint node types and recursive maze generation. ayeletstudioindia/unreal-analyzer-mcp focuses on Unreal Engine 5 project analysis. kvick-games/UnrealMCP provides lightweight agent control. **Physics simulation ranges from educational to research-grade** — chrishayuk/chuk-mcp-physics (Python, Apache 2.0) provides 55 tools across 10 categories: basic mechanics, fluid dynamics, rotational dynamics, oscillations, circular motion, statics, kinematics, collisions, conservation laws, and unit conversions — backed by 515 tests at 98% coverage. andylbrummer/math-mcp offers GPU-accelerated simulations across four specialized servers: symbolic math (14 tools), quantum wave mechanics (12 tools), molecular dynamics (15 tools), and neural networks (16 tools) — achieving 60-120x GPU speedup. The Genesis physics engine (28.3k stars, Apache 2.0) simulates at 43 million FPS on an RTX 4090 with rigid body, MPM, SPH, FEM, PBD, and fluid solvers — dustland/genesis-mcp (4 stars) wraps it as an MCP server for stdio-based visualization. manasp21/PsiAnimator-MCP integrates QuTiP quantum physics with Manim animation for educational visualizations. **Engineering simulation covers robotics, circuits, and multi-physics** — omni-mcp/isaac-sim-mcp (136 stars, Python, MIT) enables natural language control of NVIDIA Isaac Sim for robotics simulation — create physics scenes, place robots (Franka, Jetbot, Carter, G1, Go1), execute scripts, and run obstacle navigation. Orthogonalpub/modelica_simulation_mcp_server (15 stars, MIT) transforms the Modelica ODE IDE into an AI agent, generating differential equations from natural language descriptions and running simulations with real-time plotting and 3D visualization. clanker-lover/spicebridge provides 18 tools for ngspice circuit simulation: template-based design, netlist creation, AC/transient/DC simulation, automated measurement, and schematic generation. pathintegral-institute/mcp.science offers DFT calculations and materials science data access for research. poly-mcp/IoT-Edge-MCP-Server unifies MQTT sensors, Modbus devices, and industrial equipment for IoT monitoring. **Gaps remain in enterprise engineering simulation** — no MCP server exists for ANSYS, COMSOL, Abaqus, or other commercial FEA/CFD tools. SolidWorks has no MCP integration despite its widespread use. No digital twin platform integration exists for Azure Digital Twins, AWS IoT TwinMaker, or similar cloud services. The Genesis MCP wrapper is minimal (4 stars) relative to the engine's popularity (28.3k stars). No dedicated CFD or structural analysis MCP server exists. The category would benefit from MCP integrations for major commercial simulation tools and cloud digital twin platforms."
last_refreshed: 2026-03-16
---

Digital twins, 3D modeling, and simulation MCP servers let AI agents control CAD tools, run physics simulations, manipulate game engines, and interact with engineering models. Instead of manually scripting 3D scenes or configuring simulation parameters, AI assistants can directly create models, run simulations, and analyze results through natural language.

This review covers **digital twins, 3D modeling, and simulation MCP servers** — 3D creation suites, CAD platforms, game engines, physics simulators, and engineering tools. For related servers, see our [Robotics & Automation review](/reviews/robotics-automation-mcp-servers/), [Data Science & Machine Learning review](/reviews/data-science-ml-mcp-servers/), and [Scientific Research review](/reviews/scientific-research-mcp-servers/).

The headline findings: **Blender leads the entire MCP ecosystem** — ahujasid/blender-mcp has 17.7k stars, making it one of the most popular MCP servers period. **Game engines are well-served** with Unity and Unreal each having multiple high-quality MCPs (1.3k–1.6k stars). **CAD covers open-source tools** with FreeCAD (605 stars) and OpenSCAD well-represented. **Physics simulation ranges from educational to research-grade** with GPU-accelerated quantum and molecular dynamics. **Enterprise engineering tools are the gap** — no ANSYS, COMSOL, SolidWorks, or cloud digital twin MCPs exist yet.

## 3D Modeling — Blender

### ahujasid/blender-mcp — Most Popular 3D MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [blender-mcp](https://github.com/ahujasid/blender-mcp) | 17,700 | Python | MIT | 15+ |

**One of the most popular MCP servers in the entire ecosystem** — connects Blender to Claude AI through a socket-based server for comprehensive 3D control:

- **Object manipulation** — create, modify, and delete 3D objects with natural language
- **Material control** — create and apply materials, adjust properties
- **Scene inspection** — retrieve detailed scene hierarchy and object information
- **Python execution** — run arbitrary Python code inside Blender for anything the tools don't cover
- **Poly Haven integration** — download free HDRIs, textures, and 3D assets directly
- **Hyper3D Rodin** — generate AI 3D models from text descriptions
- **Remote host support** — connect to Blender running on a different machine
- **Anonymous telemetry** — usage tracking (can be disabled)

The gold standard for AI-assisted 3D modeling. Works with Claude Desktop, Cursor, and any MCP client.

### poly-mcp/Blender-MCP-Server — Agent-Orchestrable Blender Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Blender-MCP-Server](https://github.com/poly-mcp/Blender-MCP-Server) | — | Python | — | 51 |

**Turns Blender into a fully orchestrable MCP server** — 51 tools exposed over HTTP endpoints, designed for multi-agent pipelines rather than single-user chat:

- **51 tools** — comprehensive coverage of Blender operations
- **HTTP transport** — works over network, not just local stdio
- **Thread-safe execution** — handles concurrent requests safely
- **Auto-dependency installation** — sets up its own requirements
- **PolyMCP integration** — designed for intelligent tool orchestration across multiple servers

Better choice for agentic workflows where multiple AI agents need to coordinate 3D operations.

### CommonSenseMachines/blender-mcp — Text-to-4D Worlds

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [blender-mcp](https://github.com/CommonSenseMachines/blender-mcp) | — | Python | — | — |

**Bridges Blender with CSM.ai** for text and image-based editing capabilities — generates 4D worlds from text descriptions, going beyond static 3D modeling into animated, dynamic scenes.

### Other Blender MCPs

- **dhakalnirajan/blender-open-mcp** — runs with local Ollama models instead of cloud APIs, useful for offline or privacy-sensitive workflows
- **VxASI/blender-mcp-vxai** — enhanced Blender MCP with additional features for VXAI platform

## CAD — FreeCAD, OpenSCAD, and Cloud CAD

### neka-nat/freecad-mcp — Most Popular FreeCAD MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [freecad-mcp](https://github.com/neka-nat/freecad-mcp) | 605 | Python | MIT | 10 |

**FreeCAD control through Claude AI** — runs as a FreeCAD addon with an RPC server for conversational 3D design:

- **10 tools** — document creation, object creation/editing/deletion, Python execution, screenshots, parts library access
- **FreeCAD addon** — installs directly into FreeCAD's addon system
- **Remote connection** — connect to FreeCAD running on a different machine
- **Parts library** — access and insert pre-built components
- **2D to 3D** — supports creating objects from 2D drawings

Solid choice for open-source CAD workflows. Design 3D parts through natural conversation.

### Other FreeCAD MCPs

- **proximile/FreeCAD-MCP** — Docker containerization, Vision AI analysis, multi-model support (Claude, GPT-4o, Gemini)
- **spkane/freecad-addon-robust-mcp-server** — 150+ tools organized by category, the most comprehensive FreeCAD MCP
- **bonninr/freecad_mcp** — prompt-assisted CAD design, Claude Desktop integration
- **contextform/freecad-mcp** — open-source FreeCAD automation server
- **ATOI-Ming/FreeCAD-MCP** — GUI panel + MCP server for running macros and managing documents

### jhacksman/OpenSCAD-MCP-Server — Parametric 3D from Text and Images

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [OpenSCAD-MCP-Server](https://github.com/jhacksman/OpenSCAD-MCP-Server) | — | TypeScript | — | 5+ |

**Text and image to parametric 3D models** — goes beyond simple OpenSCAD scripting with AI image generation and multi-view reconstruction:

- **AI image generation** — create reference images from text descriptions
- **Multi-view reconstruction** — CUDA-accelerated stereo reconstruction from multiple views
- **Parametric export** — CSG, AMF, 3MF, and SCAD output formats
- **Image approval workflow** — review generated images before 3D reconstruction
- **Remote processing** — offload heavy computation to remote GPU servers

### Other OpenSCAD and Cloud CAD MCPs

- **quellant/openscad-mcp** — render, export, and analyze 3D models using OpenSCAD
- **fboldo/openscad-mcp-server** — STL and PNG rendering for iterative agent-driven CAD workflows
- **jabberjabberjabber/openscad-mcp** — LLM-driven OpenSCAD rapid prototyping
- **BuildCAD AI** ([buildcad.ai/mcp](https://buildcad.ai/mcp)) — free cloud-based CAD with multi-view PNG renders (front/right/top/isometric), works with any MCP client
- **Svetlana-DAO-LLC/cad-agent** — build123d + VTK rendering in Docker, STL/STEP/3MF export, printability analysis
- **daobataotie/CAD-MCP** — general CAD MCP server

## CAD — Fusion 360

### Joe-Spencer/fusion-mcp-server — Fusion 360 Design Resources

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [fusion-mcp-server](https://github.com/Joe-Spencer/fusion-mcp-server) | — | TypeScript | — | — |

**Exposes Fusion 360's design hierarchy as MCP resources** — rather than just executing commands, this server provides contextual information that helps AI assistants understand your design:

- **Design structure** — hierarchical view of components, bodies, and sketches
- **Parameters** — access user-defined parameters for parametric modeling
- **Document info** — metadata about the currently open file
- **ADSK integration** — resources and tools from Autodesk's ecosystem

### Other Fusion 360 MCPs

- **mycelia1/fusion360-mcp-server** — generate and execute scripts directly in Fusion 360
- **AuraFriday/Fusion-360-MCP-Server** — control Fusion 360 with any AI through MCP
- **ArchimedesCrypto/fusion360-mcp-server** — Fusion 360 control and automation

## Game Engines — Unity

### IvanMurzak/Unity-MCP — Editor + Runtime Unity Control

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Unity-MCP](https://github.com/IvanMurzak/Unity-MCP) | 1,300 | C# | MIT | 50+ |

**AI-powered bridge for both Unity Editor and compiled games** — the most comprehensive Unity MCP, with 50+ tools across three categories:

- **Project & Assets** (20 tools) — manage assets, scripts, and project structure
- **Scene & Hierarchy** (24 tools) — create, modify, reparent, transform GameObjects
- **Scripting & Editor** (12 tools) — C# code compilation via Roslyn, editor automation
- **Runtime support** — works in compiled games, not just the editor — enables real-time AI debugging and player-AI interaction
- **Extensible** — add custom MCP Tools, Resources, and Prompts
- **Multi-deployment** — local stdio, remote HTTP, or Docker
- **Extensions** — Animation, ParticleSystem, and ProBuilder modules available

The choice for production Unity workflows that need editor and runtime AI integration.

### CoderGamester/mcp-unity — WebSocket Unity Bridge

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-unity](https://github.com/CoderGamester/mcp-unity) | 1,400 | TypeScript/C# | MIT | 35+ |

**WebSocket bridge between Unity Editor and AI assistants** — a Node.js server implementing MCP that connects to Unity's editor:

- **35+ tools** — scene/GameObject manipulation, component management, material creation, package management, test execution
- **6 MCP resources** — query menus, hierarchy, GameObjects, logs, packages, assets
- **IDE integration** — automatic workspace integration with Unity's PackedCache folder
- **Multi-platform support** — Cursor, Windsurf, Claude Code, GitHub Copilot

Strong alternative with emphasis on IDE integration and workspace awareness.

### Other Unity MCPs

- **CoplayDev/unity-mcp** — asset management, scene control, script editing, task automation
- **akiojin/unity-mcp-server** — deprecated, succeeded by unity-cli

## Game Engines — Unreal Engine

### chongdashu/unreal-mcp — Most Popular Unreal Engine MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [unreal-mcp](https://github.com/chongdashu/unreal-mcp) | 1,600 | C++/Python | MIT | 15+ |

**Natural language control of Unreal Engine 5** — a C++ plugin for TCP communication with Unreal Editor subsystems plus a Python MCP server:

- **Actor management** — create, delete, and transform actors in the scene
- **Blueprint development** — create custom components with visual scripting
- **Blueprint node graph** — edit and visualize blueprint execution flow
- **Viewport control** — manage editor camera and viewport settings
- **Multi-client support** — Cursor, Claude Desktop, Windsurf

The most mature Unreal Engine MCP with the strongest community adoption.

### flopperam/unreal-engine-mcp — World Building and Architecture

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [unreal-engine-mcp](https://github.com/flopperam/unreal-engine-mcp) | 592 | Python | MIT | 20+ |

**Specialized for world building** — create entire towns, castles, mansions, and mazes with AI-powered commands:

- **Blueprint visual scripting** — 23+ node types, variables with full property control, custom functions
- **Architecture tools** — arches, staircases, towers, and large-scale structures with configurable parameters
- **Maze generation** — recursive backtracking algorithm for procedural maze creation
- **Physics & materials** — physics simulation controls and material application
- **Real-time chat** — embedded browser in Unreal Editor for agent interaction

### Other Unreal Engine MCPs

- **ayeletstudioindia/unreal-analyzer-mcp** — Unreal Engine 5 project analysis
- **ChiR24/Unreal_mcp** — C++ Automation Bridge plugin with TypeScript server
- **kvick-games/UnrealMCP** — lightweight agent control for Unreal Engine

## Physics Simulation

### chrishayuk/chuk-mcp-physics — Comprehensive Physics Calculator

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [chuk-mcp-physics](https://github.com/chrishayuk/chuk-mcp-physics) | — | Python | Apache 2.0 | 55 |

**55 specialized physics tools spanning classical mechanics to fluid dynamics** — the most complete physics calculation MCP server:

- **Basic mechanics** (8 tools) — projectile motion, forces, energy, momentum, collisions
- **Fluid dynamics** (10 tools) — drag, buoyancy, terminal velocity, lift, Magnus force, Bernoulli principle
- **Rotational dynamics** (5 tools) — torque, moment of inertia, angular momentum
- **Oscillations** (5 tools) — springs, pendulums, harmonic motion, damping
- **Circular motion** (5 tools) — centripetal force, orbits, banking angles, escape velocity
- **Statics** (7 tools) — force balance, torque balance, friction, beam reactions
- **Kinematics** (7 tools) — motion analysis, trajectory fitting, velocity calculations
- **Collisions** (2 tools) — elastic and inelastic 3D collisions with energy loss
- **Conservation laws** (4 tools) — energy, momentum, angular momentum verification
- **Unit conversions** (2 tools) — 62 unit types across 16 categories
- **515 tests** at 98% code coverage — well-tested and reliable

Also available as IBM/chuk-mcp-physics. Excellent for education, engineering calculations, and physics verification.

### andylbrummer/math-mcp — GPU-Accelerated Scientific Simulation

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [math-mcp](https://github.com/andylbrummer/math-mcp) | — | Python | MIT | 57 |

**Four specialized GPU-accelerated MCP servers** for computational science:

- **Math MCP** (14 tools) — symbolic algebra, numerical computing
- **Quantum MCP** (12 tools) — wave mechanics, Schrödinger simulations, double-slit interference
- **Molecular MCP** (15 tools) — classical molecular dynamics, N-body dynamics, crystal diffraction
- **Neural MCP** (16 tools) — neural network training and evaluation
- **GPU acceleration** — automatic CUDA detection, 60-120x speedup over CPU
- **Async support** — long-running simulations as background tasks

Research-grade simulation capabilities. The quantum and molecular servers enable real scientific computation through AI.

### Genesis Physics Engine + MCP Wrapper

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Genesis](https://github.com/Genesis-Embodied-AI/Genesis) | 28,300 | Python | Apache 2.0 | — |
| [genesis-mcp](https://github.com/dustland/genesis-mcp) | 4 | Python | MIT | 2 |

**Genesis is a next-generation physics engine** simulating at 43 million FPS on an RTX 4090 — the underlying engine is one of the most popular open-source physics projects:

- **Multiple solvers** — rigid body, MPM, SPH, FEM, PBD, and Stable Fluid
- **Material diversity** — rigid bodies, liquids, gases, deformable and soft objects
- **Robot support** — robotic arms, legged robots, drones, soft robots
- **Differentiable** — supports gradient-based optimization
- **Cross-platform** — Linux, macOS, Windows with multiple compute backends

The MCP wrapper (dustland/genesis-mcp) is minimal — only 2 tools for running simulations and accessing world info via stdio transport. Significant opportunity for a more comprehensive MCP integration given the engine's capabilities.

### Other Physics MCPs

- **manasp21/PsiAnimator-MCP** — QuTiP quantum physics + Manim animation for educational visualizations
- **pathintegral-institute/mcp.science** — DFT calculations, materials science data, sandboxed Python execution for research

## Engineering Simulation

### omni-mcp/isaac-sim-mcp — NVIDIA Isaac Sim Robotics Simulation

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [isaac-sim-mcp](https://github.com/omni-mcp/isaac-sim-mcp) | 136 | Python | MIT | 5 |

**Natural language control of NVIDIA Isaac Sim** — bridge between conversational AI and precision robotics simulation:

- **Scene management** — create physics scenes with configurable gravity, timestep, and solver iterations
- **Robot placement** — position Franka, Jetbot, Carter, G1, and Go1 robots at specified coordinates
- **Script execution** — run arbitrary Python within Isaac Sim for advanced workflows
- **Omniverse commands** — execute Omniverse Kit commands directly
- **Interactive preview** — preview code before execution for safety

Requires NVIDIA Isaac Sim 4.2.0+ and a compatible GPU. Purpose-built for robotics research and digital twin validation.

### Orthogonalpub/modelica_simulation_mcp_server — Multi-Physics Modeling

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [modelica_simulation_mcp_server](https://github.com/Orthogonalpub/modelica_simulation_mcp_server) | 15 | Python | MIT | 2 |

**Transforms the Modelica ODE IDE into an AI engineering agent** — describe a physical system in natural language, get differential equations, simulation, and visualization:

- **Natural language to ODE** — automatically generates Modelica models from text descriptions
- **Diagram generation** — intelligent component placement and connection visualization
- **Real-time plotting** — live simulation results with 3D visualization
- **Cloud execution** — token-based authentication with secure cloud compute
- **End-to-end automation** — from description to simulation results in one prompt

Particularly interesting for multi-domain engineering (mechanical, electrical, thermal, hydraulic systems).

### clanker-lover/spicebridge — Circuit Simulation

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [spicebridge](https://github.com/clanker-lover/spicebridge) | — | — | — | 18 |

**ngspice circuit simulation through AI** — full electronics design workflow:

- **18 tools** — template-based design, netlist creation, simulation, measurement, schematic generation
- **Simulation types** — AC, transient, and DC analysis
- **Auto-calculation** — component values calculated from templates
- **Spec verification** — automated measurement against specifications
- **Dual transport** — stdio for Claude Code, HTTP + Cloudflare tunnel for remote clients

### Other Engineering MCPs

- **poly-mcp/IoT-Edge-MCP-Server** — unifies MQTT sensors, Modbus devices, and industrial equipment into a single AI-orchestrable API with real-time monitoring and actuator control
- **jordy33/iot_mcp_server** — IoT device control and monitoring for smart lights, sensors, and connected devices
- **ToxMCP/pbpk-mcp** — PBPK pharmacokinetic modeling workflows
- **globus-labs/science-mcps** — Globus compute facilities for scientific simulation at scale

## What's Missing

The biggest gaps in this category:

- **No commercial FEA/CFD tools** — ANSYS, COMSOL, Abaqus, and NASTRAN have no MCP servers. This is the most impactful gap for professional engineering.
- **No SolidWorks MCP** — despite SolidWorks' dominant market share in mechanical engineering, no MCP integration exists.
- **No cloud digital twin platforms** — Azure Digital Twins, AWS IoT TwinMaker, and similar services have no MCP servers.
- **Genesis MCP wrapper is minimal** — the physics engine has 28.3k stars but the MCP wrapper only has 2 tools. Significant untapped potential.
- **No dedicated CFD server** — computational fluid dynamics is entirely absent from the MCP ecosystem.
- **No structural analysis** — no MCP server handles FEA for stress, strain, or fatigue analysis.
- **Limited Autodesk coverage** — Fusion 360 has MCPs but AutoCAD, Revit, and Inventor are largely unserved (Autodesk recently announced official MCP servers but they're in early stages).

## Summary

| Subcategory | Top Server | Stars | Rating |
|------------|-----------|-------|--------|
| 3D Modeling (Blender) | ahujasid/blender-mcp | 17,700 | ★★★★★ |
| CAD (FreeCAD/OpenSCAD) | neka-nat/freecad-mcp | 605 | ★★★★ |
| Game Engines (Unity) | IvanMurzak/Unity-MCP | 1,300 | ★★★★★ |
| Game Engines (Unreal) | chongdashu/unreal-mcp | 1,600 | ★★★★★ |
| Physics Simulation | chrishayuk/chuk-mcp-physics | — | ★★★★ |
| Engineering Simulation | omni-mcp/isaac-sim-mcp | 136 | ★★★ |

**Overall rating: 4/5** — Blender and game engine MCPs are world-class. CAD and physics simulation are solid. Enterprise engineering simulation is the clear gap — when ANSYS, COMSOL, and SolidWorks get MCP integrations, this category will be transformative.

---

*This review is AI-generated based on research of publicly available GitHub repositories and documentation. ChatForest does not test or run MCP servers hands-on. Star counts are approximate and may have changed since publication. Last updated: March 2026.*

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*

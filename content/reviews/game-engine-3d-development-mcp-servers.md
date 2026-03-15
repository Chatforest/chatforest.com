---
title: "Game Engine & 3D Development MCP Servers — Unity, Unreal Engine, Godot, Roblox, Phaser, and More"
date: 2026-03-15T09:30:00+09:00
description: "Game engine and 3D development MCP servers let AI agents create scenes, manage assets, control editors, and automate game development workflows through natural language. We reviewed 30+ servers across Unity (CoplayDev/unity-mcp at 5,800 stars with 25+ tools for scene/asset/material/script management, CoderGamester/mcp-unity at 1,300 stars with WebSocket bridge and prefab creation, IvanMurzak/Unity-MCP at 306 stars with 100+ native tools and runtime agents), Unreal Engine (chongdashu/unreal-mcp at 1,200 stars with actor/Blueprint/graph editing via C++ plugin, flopperam/unreal-engine-mcp with Flop Agent for autonomous world building, ChiR24/Unreal_mcp at 353 stars with 36 tools via native Automation Bridge), Godot (HaD0Yun/godot-mcp GoPeak with 95+ tools including GDScript LSP and DAP debugger, bradypp/godot-mcp at 58 stars with read-only safety mode and UID management), Roblox (official Roblox/studio-rust-mcp-server at 413 stars now superseded by built-in Studio MCP, boshyxd/robloxstudio-mcp with 21 read-only tools), web game engines (phaserjs/editor-mcp-server official at 26 stars with scene/asset/tilemap management, Three.js community servers), and game asset generation (Flux159/mcp-game-asset-gen with DALL-E/Gemini/Fal.ai support for sprites/textures/3D models). Unity leads in ecosystem size and adoption; Unreal has the deepest editor integration; Godot offers the most comprehensive single-server tooling; Roblox is the only engine with native built-in MCP support."
og_description: "Game Engine & 3D Development MCP servers: CoplayDev/unity-mcp (5,800 stars, TypeScript/C#, 25+ tools for scene/asset/material/script management with batch execution), CoderGamester/mcp-unity (1,300 stars, TypeScript/C#, WebSocket bridge with prefab creation and test runner), IvanMurzak/Unity-MCP (306 stars, C#, 100+ native tools with runtime agents for in-game NPCs), chongdashu/unreal-mcp (1,200 stars, Python/C++, actor control/Blueprint creation/graph editing/viewport control), flopperam/unreal-engine-mcp (Python/C++, Flop Agent autonomous world building with Blueprint editing), ChiR24/Unreal_mcp (353 stars, TypeScript/C++, 36 tools via native Automation Bridge), HaD0Yun/godot-mcp GoPeak (95+ tools with GDScript LSP/DAP debugger/screenshot capture/input injection/ClassDB introspection/CC0 asset library), bradypp/godot-mcp (58 stars, TypeScript, read-only safety mode/Godot 4.4+ UID management/cross-platform), Roblox/studio-rust-mcp-server (413 stars, Rust, official reference implementation now superseded by built-in Studio MCP), boshyxd/robloxstudio-mcp (21 read-only tools with file tree/script grepping/playtest control), phaserjs/editor-mcp-server (26 stars, TypeScript, official Phaser Editor scene/asset/tilemap management), Flux159/mcp-game-asset-gen (multi-provider asset generation with DALL-E/Gemini/Fal.ai for sprites/textures/3D models). 30+ servers reviewed. Rating: 4.0/5."
content_type: "Review"
card_description: "Game engine and 3D development MCP servers across Unity, Unreal Engine, Godot, Roblox, web game engines, and asset generation. Unity has the largest MCP ecosystem — CoplayDev/unity-mcp (5,800 stars, 25+ tools) leads adoption with comprehensive scene, asset, material, and script management including batch execution for complex operations, while IvanMurzak/Unity-MCP (306 stars) offers the deepest integration with 100+ native tools and runtime agents that can be embedded into built games for AI-controlled NPCs. Unreal Engine has the most sophisticated editor integration — chongdashu/unreal-mcp (1,200 stars) provides actor control, Blueprint creation, graph node editing, and viewport manipulation through a C++ plugin, while flopperam/unreal-engine-mcp pushes the boundary with the Flop Agent for fully autonomous world building. Godot has the most comprehensive single-server tooling — HaD0Yun/godot-mcp GoPeak packs 95+ tools including GDScript LSP, DAP debugger, screenshot capture, input injection, ClassDB introspection, and a CC0 asset library into one server. Roblox is the industry pioneer — the only major engine with native built-in MCP support, where Studio itself operates as an MCP server. Phaser provides official MCP support for web game development with scene and asset management. The category earns 4.0/5 — every major game engine now has MCP integration, Unity and Unreal ecosystems show healthy competition between multiple implementations, Godot punches above its weight with comprehensive tooling, and Roblox's native integration sets the standard for what engine-level MCP support should look like."
---

Game engine MCP servers represent one of the most ambitious applications of the Model Context Protocol — giving AI agents direct control over 3D editors, scene graphs, physics systems, and creative workflows. Unlike simpler MCP integrations that wrap REST APIs, these servers bridge the gap between language models and real-time interactive environments.

The landscape covers six areas: **Unity** (the largest MCP ecosystem with 3+ major implementations), **Unreal Engine** (deepest editor integration via C++ plugins), **Godot** (comprehensive single-server tooling), **Roblox** (the only engine with native built-in MCP), **web game engines** (Phaser, Three.js), and **game asset generation** (AI-powered sprite, texture, and 3D model creation).

The headline findings: **Unity has the most MCP servers and highest total adoption** — CoplayDev/unity-mcp alone has 5,800 stars. **Unreal Engine's C++ plugin architecture enables the deepest editor control** — Blueprint creation, graph editing, and viewport manipulation. **Godot's GoPeak server packs 95+ tools into a single implementation** — the most feature-dense game engine MCP server. **Roblox is the industry leader in native MCP integration** — Studio ships with a built-in MCP server, no plugins needed. **Game asset generation via MCP is emerging** — AI-powered sprite sheets, textures, and 3D models from text descriptions. **Every major game engine now has at least one MCP server**, though maturity varies significantly.

## Unity

### CoplayDev/unity-mcp (Adoption Leader)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [CoplayDev/unity-mcp](https://github.com/CoplayDev/unity-mcp) | 5,800 | TypeScript/C# | 25+ | stdio |

**CoplayDev/unity-mcp** (5,800 stars, 700+ forks) is the most popular Unity MCP server and one of the most starred MCP servers in any game development category.

The server provides natural language control over Unity Editor operations: **Scene management** — create, modify, and inspect scenes and GameObjects. **Asset management** — import, organize, and manipulate project assets. **Material and shader control** — create and configure materials with property manipulation. **Script management** — create, edit, and organize C# scripts. **Graphics** — manage_graphics tool with 33 actions for volume/post-processing, light baking, rendering stats, and pipeline settings. **Package management** — install, remove, search, and manage Unity packages and scoped registries. **Batch execution** — combine multiple operations for complex workflows.

The `batch_execute` tool is particularly valuable — it lets you chain multiple Unity operations in a single MCP call, reducing round trips for complex scene setup tasks.

Recent versions (v9.5+) added graphics management and package management tools, showing active development. Works with Claude, Claude Code, Cursor, and VS Code.

### CoderGamester/mcp-unity (IDE-Focused)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [CoderGamester/mcp-unity](https://github.com/CoderGamester/mcp-unity) | 1,300 | TypeScript/C# | 10+ | stdio |

**CoderGamester/mcp-unity** (1,300 stars) takes a different architectural approach — it runs a WebSocket server inside Unity Editor and a Node.js server that implements MCP, creating a bridge between AI assistants and the running editor.

Core tools: `execute_menu_item` for triggering Unity menu commands, `select_gameobject` and `update_gameobject` for scene hierarchy manipulation, `update_component` for modifying component properties with error surfacing, `CreatePrefabTool` for creating prefabs from scene objects, and `run_tests` with pass/fail reporting and optional log output.

The WebSocket architecture means the server communicates with a live Unity instance — changes appear in real time. Remote host configuration support enables connecting to Unity running on a different machine.

Designed specifically for IDE workflows with Cursor, Claude Code, Codex, Windsurf, and other coding tools. The focus is on development assistance rather than autonomous scene building.

### IvanMurzak/Unity-MCP (Deepest Integration)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [IvanMurzak/Unity-MCP](https://github.com/IvanMurzak/Unity-MCP) | 306 | C# | 100+ | stdio |

**IvanMurzak/Unity-MCP** (306 stars, v0.51.4) has the deepest Unity integration — 52 exposed tools, 48 prompts, and 1 resource, with 100+ native tools built in for all major Unity systems.

What sets this apart: **Runtime agents** — AI agents can be embedded into built games, enabling NPC behavior controlled by language models at runtime. This is the only Unity MCP server designed for both editor-time development and runtime gameplay. **Reflection capabilities** — AI can discover and execute any C# method in the project, not just predefined tools. **Custom tool creation** — developers add new MCP tools with a single C# attribute. **Package manager integration** — install and manage Unity packages through natural language.

The runtime agent capability is genuinely novel. Most game engine MCP servers focus on editor control during development. This one lets you ship an MCP-connected agent inside the game itself — imagine NPCs that understand and respond to the game world through an LLM.

Docker support is available for headless operation. Active development with frequent releases.

### Other Unity Implementations

| Server | Stars | Focus |
|--------|-------|-------|
| [nurture-tech/unity-mcp-server](https://github.com/nurture-tech/unity-mcp-server) | 25 | Union — multimodal vision (scene viewing, camera inspection, asset thumbnails) |
| [notargs/UnityNaturalMCP](https://github.com/notargs/UnityNaturalMCP) | — | "Natural" UX-focused implementation |
| [MiAO-AI-Lab/MiAO-MCP-for-Unity](https://github.com/MiAO-AI-Lab/MiAO-MCP-for-Unity) | — | MCP plugin for Unity Editor and games |

**nurture-tech/unity-mcp-server** (Union) is notable for its multimodal vision capabilities — your AI agent can see the Unity scene, look through any camera, watch play mode, and inspect asset thumbnails. This visual context significantly improves the quality of AI-generated scene modifications.

The Unity MCP ecosystem is unusually crowded — 6+ implementations competing for different niches. **CoplayDev/unity-mcp is the adoption leader** for general-purpose scene manipulation. **CoderGamester/mcp-unity is best for IDE-centric workflows**. **IvanMurzak/Unity-MCP offers the deepest integration** with runtime agents and reflection.

## Unreal Engine

### chongdashu/unreal-mcp (Community Leader)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [chongdashu/unreal-mcp](https://github.com/chongdashu/unreal-mcp) | 1,200 | Python/C++ | 20+ | stdio |

**chongdashu/unreal-mcp** (1,200 stars) enables AI assistants to control Unreal Engine through natural language via a C++ plugin and Python MCP server.

The tool coverage spans several systems: **Actor control** — create and delete actors (cubes, spheres, lights, cameras), set transforms (position, rotation, scale), query properties, find actors by name, list all actors in the current level. **Blueprint tools** — create new Blueprint classes with custom components, add and configure components (mesh, camera, light), set component properties and physics settings, compile Blueprints and spawn Blueprint actors, create input mappings for player controls. **Graph/node editing** — add event nodes (BeginPlay, Tick), create function call nodes and connect them, add variables with custom types and default values, create component and self references, manage nodes in the graph. **Viewport control** — focus on specific actors or locations, control camera orientation and distance.

Ships with a UE 5.5 starter project (`MCPGameProject`) with the plugin pre-configured. The Blueprint editing capability is particularly powerful — AI assistants can build game logic visually through Unreal's node-based system.

### flopperam/unreal-engine-mcp (Autonomous Agent)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [flopperam/unreal-engine-mcp](https://github.com/flopperam/unreal-engine-mcp) | — | Python/C++ | 20+ | stdio |

**flopperam/unreal-engine-mcp** pushes beyond standard MCP into autonomous agent territory. The **Flop Agent** runs inside Unreal Editor and can autonomously build 3D worlds, edit Blueprints, and create structures from natural language descriptions.

Architecture: AI Client (Cursor/Claude/Windsurf) connects via MCP Protocol to a Python Server, which communicates via TCP Socket to a C++ Plugin providing native Unreal API access. Tools cover world building, physics simulation, Blueprint system, actor management, component system, and material system.

The marketing emphasizes ambitious scene building — "entire towns, medieval castles, modern mansions, challenging mazes" — through AI-powered commands. The Flop Agent goes beyond analysis to directly build and edit Blueprint logic from natural language, making it more autonomous than most MCP servers. Supports UE 5.5+.

### ChiR24/Unreal_mcp (Native Automation)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [ChiR24/Unreal_mcp](https://github.com/ChiR24/Unreal_mcp) | 353 | TypeScript/C++ | 36 | stdio |

**ChiR24/Unreal_mcp** (353 stars, 57 forks) uses a native C++ Automation Bridge plugin for comprehensive Unreal Engine automation. The 36 MCP tools use action-based dispatch — one tool definition can handle multiple related operations through parameters.

Built with TypeScript (MCP server) and C++ (Unreal plugin). Latest release v0.5.18 focused on fixing installation issues and first-time setup guidance.

### Other Unreal Implementations

| Server | Focus |
|--------|-------|
| [ayeletstudioindia/unreal-analyzer-mcp](https://github.com/ayeletstudioindia/unreal-analyzer-mcp) | Source code analysis for Unreal codebases |
| [gingerol/vhcilab-unreal-engine-mcp](https://github.com/gingerol/vhcilab-unreal-engine-mcp) | Natural language scene building |
| [kvick-games/UnrealMCP](https://github.com/kvick-games/UnrealMCP) | AI agent control |

**unreal-analyzer-mcp** is different from the others — it analyzes Unreal Engine source code rather than controlling the editor. Useful for understanding engine internals and navigating large Unreal codebases.

The Unreal MCP space is less crowded than Unity but more technically ambitious. The C++ plugin requirement makes these servers harder to build and maintain, but enables deeper editor integration than web-based approaches.

## Godot

### HaD0Yun/godot-mcp — GoPeak (Most Comprehensive)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [HaD0Yun/godot-mcp](https://github.com/HaD0Yun/godot-mcp) | — | TypeScript | 95+ | stdio |

**GoPeak** bills itself as "the most comprehensive MCP server for Godot Engine" — and with 95+ tools, it has a strong claim. The tool count exceeds most game engine MCP servers across all engines.

Capabilities span: **Scene management** — create, modify, inspect, and navigate Godot scenes. **GDScript LSP** — language server protocol integration for code intelligence. **DAP debugger** — Debug Adapter Protocol integration for breakpoints and stepping. **Screenshot capture** — grab editor and game viewport screenshots for visual context. **Input injection** — simulate input events for testing and automation. **ClassDB introspection** — inspect Godot's class hierarchy, methods, and properties programmatically. **CC0 asset library** — access to Creative Commons Zero licensed assets for prototyping.

The combination of LSP + DAP + screenshot capture + input injection makes this uniquely powerful for automated testing and debugging workflows. Install via `npx gopeak`.

### bradypp/godot-mcp (Safety-Focused)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [bradypp/godot-mcp](https://github.com/bradypp/godot-mcp) | 58 | TypeScript | 15+ | stdio |

**bradypp/godot-mcp** (58 stars) takes a safety-first approach with an optional **read-only mode** — important when giving AI assistants access to your game project. Godot 4.4+ UID management ensures stable references to nodes and resources across sessions.

Core capabilities: launch Godot Editor, run projects, capture debug output, create scenes, add nodes, discover projects automatically. Cross-platform on Windows, macOS, and Linux with zero-configuration automatic Godot detection.

The read-only mode is a genuine differentiator. Most game engine MCP servers assume full write access. For code review, debugging, and project inspection workflows, read-only access prevents accidental modifications.

### Other Godot Implementations

| Server | Focus |
|--------|-------|
| [Coding-Solo/godot-mcp](https://github.com/Coding-Solo/godot-mcp) | Editor launching, project running, debug output |
| [LeeSinLiang/godot-mcp](https://github.com/LeeSinLiang/godot-mcp) | Error capture, scene management, remote connections |
| [Dokujaa/Godot-MCP](https://github.com/Dokujaa/Godot-MCP) | Claude Desktop integration with Meshy API for 3D model generation |
| [ee0pdt/Godot-MCP](https://github.com/ee0pdt/Godot-MCP) | Code assistance, scene manipulation, project management |
| [Nihilantropy/godot-mcp-docs](https://github.com/Nihilantropy/godot-mcp-docs) | Godot Engine documentation access |

**Dokujaa/Godot-MCP** integrates with the Meshy API for AI-generated 3D models imported directly into Godot — a creative use case that combines procedural content generation with engine integration.

Godot's MCP ecosystem is fragmented across many small implementations. **GoPeak is the clear leader** for comprehensive tooling. **bradypp/godot-mcp is best for safety-conscious workflows**. The open-source nature of Godot (vs. Unity/Unreal's proprietary engines) makes it easier for community developers to build deep integrations.

## Roblox

### Roblox/studio-rust-mcp-server (Official)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [Roblox/studio-rust-mcp-server](https://github.com/Roblox/studio-rust-mcp-server) | 413 | Rust | 4 | stdio |

**Roblox/studio-rust-mcp-server** (413 stars) is the official Roblox Studio MCP server — a reference implementation in Rust with tools for `run_code`, `insert_model`, `get_console_output`, and `start_stop_play`.

**Important: this repository is no longer actively updated.** Roblox has shifted to a **built-in MCP server that ships directly with Roblox Studio**, making it the first major game engine with native MCP support — no plugins, no external servers, just built-in functionality.

Roblox's approach is industry-leading. Studio operates as an MCP server while Roblox Assistant is an MCP client. This enables cross-application workflows: lay out a UI in Figma, create a skybox in Blockade Labs, and have Assistant automatically import it into your experience. As of February 2026, Roblox announced updates to support external LLM connections through MCP.

The open-source repository remains available as a reference implementation for understanding the protocol integration.

### boshyxd/robloxstudio-mcp (Community Enhanced)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [boshyxd/robloxstudio-mcp](https://github.com/boshyxd/robloxstudio-mcp) | — | — | 21+ | stdio |

**boshyxd/robloxstudio-mcp** provides a community-maintained alternative with 21 read-only tools: `get_file_tree`, `search_files`, `get_place_info`, `get_services`, `search_objects`, `get_instance_properties`, `get_instance_children`, `search_by_property`, `get_class_info`, `get_project_structure`, `mass_get_property`, `get_script_source`, `grep_scripts`, `get_attribute`, `get_attributes`, `get_tags`, `get_tagged`, `get_selection`, `start_playtest`, `stop_playtest`, `get_playtest_output`.

The `grep_scripts` tool is particularly useful — search across all scripts in a Roblox place for patterns, similar to how developers grep codebases. The read-only focus reduces risk when giving AI assistants access to production places.

## Web Game Engines

### Phaser Editor (Official)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [phaserjs/editor-mcp-server](https://github.com/phaserjs/editor-mcp-server) | 26 | TypeScript | 15+ | stdio |

**phaserjs/editor-mcp-server** (26 stars) is the official MCP server for Phaser Editor 5, the IDE for the popular HTML5 game framework (Phaser has 37,000+ GitHub stars).

Tools cover: **Scene management** — list all scenes, get focused scene, manipulate scene contents. **Asset handling** — textures, bitmap fonts, spritesheets, animations, Spine skeletons and atlases, tilemaps. **Visual tools** — inspect texture images and generate scene screenshots for AI visual context.

As of 2026, the MCP server is built directly into the Phaser Editor installation with a one-click configuration dialog for Claude Desktop, Cursor, or VS Code. The integration lets agents combine scene changes and code modifications — implementing new gameplay features or performing code refactorings that span both visual and code layers.

Still a work in progress — prefabs, user component manipulation, full arcade physics support, and Filter properties are planned but not yet available.

### Three.js (Community)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [locchung/three-js-mcp](https://github.com/locchung/three-js-mcp) | — | TypeScript | 5+ | stdio |

**locchung/three-js-mcp** provides basic Three.js scene control through MCP — object creation, movement, rotation, and scene state retrieval via WebSocket connections. The MCP protocol's official examples repository also includes a [Three.js server example](https://github.com/modelcontextprotocol/ext-apps/tree/main/examples/threejs-server).

These are early-stage implementations with limited scope. The Three.js ecosystem (178,000+ stars) is large enough to support more comprehensive MCP servers, but game engine integration has focused on native desktop engines.

## Game Asset Generation

### Flux159/mcp-game-asset-gen

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [Flux159/mcp-game-asset-gen](https://github.com/Flux159/mcp-game-asset-gen) | — | TypeScript | 10+ | stdio |

**Flux159/mcp-game-asset-gen** generates game assets through multiple AI providers — OpenAI DALL-E, Google Gemini (2.5 Flash and 3 Pro), and Fal.ai for high-quality image generation.

Specialized tools: `generate_character_sheet` for consistent character sprites, `generate_character_variation` for variant poses, `generate_pixel_art_character` with transparent background support, `generate_texture` for seamless textures and sprites/decals (with transparency), `generate_object_sheet` for item sprites, and `image_to_3d` for unified 3D model generation with automatic reference images.

Transparent background support is critical for game sprites — most general-purpose image generators produce images with backgrounds that require manual removal. The `ALLOWED_TOOLS` environment variable lets you restrict which generators are available, reducing context usage.

### MubarakHAlketbi/game-asset-mcp

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [MubarakHAlketbi/game-asset-mcp](https://github.com/MubarakHAlketbi/game-asset-mcp) | — | — | — | stdio |

**MubarakHAlketbi/game-asset-mcp** generates 2D/3D game assets from text descriptions using Hugging Face AI models — a local alternative to cloud-based generation that can run on consumer hardware.

## What's Missing

The game engine MCP space has grown rapidly but still has notable gaps:

- **No official Unity or Unreal MCP servers** — all implementations are community-driven, unlike Roblox's first-party support
- **No Bevy (Rust) or Fyrox MCP server** — the Rust game engine ecosystem lacks MCP integration
- **No dedicated Pygame/Love2D/Raylib MCP servers** — simpler game frameworks are unserved
- **Limited cross-engine tools** — no server abstracts common operations (create object, set position, add physics) across multiple engines
- **No game testing frameworks** — automated gameplay testing through MCP is unexplored
- **No dedicated level design servers** — procedural generation and level layout tools are absent
- **No multiplayer/networking MCP** — game networking setup and management through MCP doesn't exist
- **Safety controls are inconsistent** — only bradypp/godot-mcp offers a read-only mode; most servers assume full write access to your project
- **No audio middleware integration** — Wwise, FMOD, and other game audio tools lack MCP servers

## The Bottom Line

The game engine MCP ecosystem is maturing rapidly. Every major engine now has at least one MCP server, and Unity alone has 6+ competing implementations. The quality varies significantly — from basic "run a script" wrappers to sophisticated integrations that expose entire editor APIs.

**For Unity developers**: CoplayDev/unity-mcp (5,800 stars) for general-purpose scene manipulation, IvanMurzak/Unity-MCP for the deepest integration and runtime agents.

**For Unreal developers**: chongdashu/unreal-mcp (1,200 stars) for comprehensive Blueprint and actor control with an established community.

**For Godot developers**: HaD0Yun/godot-mcp GoPeak for the most comprehensive toolset (95+ tools), bradypp/godot-mcp for safety-first workflows.

**For Roblox developers**: Use the built-in Studio MCP server — Roblox is leading the industry in native MCP support.

**For web game developers**: phaserjs/editor-mcp-server for Phaser, though the ecosystem is still early.

**Rating: 4.0/5** — Every major game engine has MCP integration, adoption is strong (Unity servers alone total 7,000+ stars), Roblox's native support sets a high bar, and the combination of editor control, asset generation, and (in Unity-MCP's case) runtime agents shows the creative potential of MCP. Deductions for inconsistent safety controls, no official support from Unity or Epic, fragmentation across too many small implementations, and missing coverage for simpler game frameworks.

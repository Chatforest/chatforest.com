# Game Engine & 3D Development MCP Servers — Unity, Unreal Engine, Godot, Roblox, Cocos Creator, Bevy, and More

> Game engine and 3D development MCP servers let AI agents create scenes, manage assets, control editors, and automate game development workflows through natural language.


Game engine MCP servers represent one of the most ambitious applications of the Model Context Protocol — giving AI agents direct control over 3D editors, scene graphs, physics systems, and creative workflows. Unlike simpler MCP integrations that wrap REST APIs, these servers bridge the gap between language models and real-time interactive environments.

The landscape covers eight areas: **Unity** (the largest MCP ecosystem with 6+ implementations and 20,000+ combined stars as of August 2026), **Unreal Engine** (deepest editor integration via C++ plugins, now with the first commercial MCP product and, as of UE 5.8, Epic's own official Experimental plugin), **Godot** (comprehensive single-server tooling), **Roblox** (the only engine with native built-in MCP and third-party LLM support), **Cocos Creator** (NEW — 1,300+ star server with 50 core tools), **Bevy/Rust** (NEW — fills the Rust game engine gap), **web game engines** (Phaser, Three.js), and **game asset generation** (AI-powered sprite, texture, and 3D model creation).

The headline findings: **Unity Technologies launched official MCP support** — the `com.unity.ai.assistant` package (pre-release v2.5.0-pre.2) includes a built-in MCP bridge, putting Unity alongside Roblox and (as of June 2026) Unreal Engine as engines with first-party support. Community servers continue to lead with CoplayDev/unity-mcp at 13,400+ stars and IvanMurzak/Unity-MCP at 3,900+ stars (both up substantially since this review's April 2026 refresh). **Unreal Engine got its first commercial MCP product** — StraySpark, which has since grown to 370+ tools across 54 categories — **and Epic Games has since shipped its own official MCP plugin in UE 5.8** (released June 2026), marked Experimental. **Godot's GoPeak server** continues to lead on feature density with tiered tool profiles for token optimization, joined by GDAI MCP as the first commercial Godot MCP ($19). **Roblox archived its open-source repo and went all-in on built-in MCP** — Studio now supports external LLMs (Claude, OpenAI, Gemini), playtest automation with virtual mouse/keyboard input, and multi-instance management. **Two major gaps filled** — Cocos Creator (1,300+ stars) and Bevy/Rust both gained MCP servers for the first time. **The first commercial game engine MCP products appeared** — StraySpark (Unreal) and GDAI (Godot) signal market maturation.

## Unity

### CoplayDev/unity-mcp (Adoption Leader)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [CoplayDev/unity-mcp](https://github.com/CoplayDev/unity-mcp) | 13,400+ | TypeScript/C# | 40+ | stdio |

**CoplayDev/unity-mcp** (13,400+ stars, 1,400+ forks as of August 2026 — up from 8,900 stars at last refresh) is the most popular Unity MCP server and one of the most starred MCP servers in any game development category. ([GitHub repo](https://github.com/CoplayDev/unity-mcp))

The server provides natural language control over Unity Editor operations: **Scene management** — create, modify, and inspect scenes and GameObjects, with multi-scene editing (additive load, close, set active, move GameObjects between scenes) plus scene templates and validation with auto-repair. **Asset management** — import, organize, and manipulate project assets. **Material and shader control** — create and configure materials with property manipulation. **Script management** — create, edit, and organize C# scripts. **Graphics** — manage_graphics tool with 33 actions for volume/post-processing, light baking, rendering stats, and pipeline settings. **Package management** — install, remove, search, and manage Unity packages and scoped registries. **Batch execution** — combine multiple operations for complex workflows.

Recent v9.6.x releases (March–April 2026) added substantial new capabilities: **manage_profiler** (v9.6.3) — profiler session control (start/stop/status), frame timing and counter reads, object memory queries, memory snapshots. **manage_physics** (v9.6.2) — physics settings, layer collision matrix, physics materials, joints (5 3D + 9 2D types), queries (raycast, raycast_all, linecast, shapecast, overlap). **manage_build** (v9.6.1) — trigger player builds, switch platforms, configure player settings, manage build scenes and profiles (Unity 6+), batch builds. Latest is v9.6.6 (April 7, 2026). Works with Claude, Claude Code, Cursor, and VS Code.

### CoderGamester/mcp-unity (IDE-Focused)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [CoderGamester/mcp-unity](https://github.com/CoderGamester/mcp-unity) | 1,900+ | TypeScript/C# | 30+ | stdio |

**CoderGamester/mcp-unity** (1,900+ stars, 238 forks as of August 2026 — up from 1,600 stars at last refresh) takes a different architectural approach ([GitHub repo](https://github.com/CoderGamester/mcp-unity)) — it runs a WebSocket server inside Unity Editor and a Node.js server that implements MCP, creating a bridge between AI assistants and the running editor.

Core tools span 30+ operations: `execute_menu_item` for triggering Unity menu commands, `select_gameobject` and `update_gameobject` for scene hierarchy manipulation, `update_component` for modifying component properties with error surfacing, `CreatePrefabTool` for creating prefabs from scene objects, `run_tests` with pass/fail reporting and optional log output, plus batch operations and material management.

The WebSocket architecture means the server communicates with a live Unity instance — changes appear in real time. Remote host configuration support enables connecting to Unity running on a different machine.

Designed specifically for IDE workflows with Cursor, Claude Code, Codex, Windsurf, and other coding tools. The focus is on development assistance rather than autonomous scene building. 264 commits show sustained development.

### IvanMurzak/Unity-MCP (Deepest Integration — Breakout Growth)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [IvanMurzak/Unity-MCP](https://github.com/IvanMurzak/Unity-MCP) | 3,900+ | C# | 100+ | stdio |

**IvanMurzak/Unity-MCP** (3,900+ stars, 352 forks as of August 2026 — up from 2,300 stars and 650% growth since March at last refresh, the fastest-growing game engine MCP server in this review) has the deepest Unity integration ([GitHub repo](https://github.com/IvanMurzak/Unity-MCP)) — 100+ native tools organized across Project & Assets (18 tools), Scene & Hierarchy (24 tools), and Scripting & Editor (11 tools), plus prompts and resources.

What sets this apart: **Runtime agents** — AI agents can be embedded into built games, enabling NPC behavior controlled by language models at runtime. This is the only Unity MCP server designed for both editor-time development and runtime gameplay. **Reflection capabilities** — AI can discover and execute any C# method in the project, not just predefined tools. **Custom tool creation** — developers add new MCP tools with a single C# attribute. **Package manager integration** — install and manage Unity packages through natural language. **No vendor lock-in** — works across Windows, macOS, and Linux with Claude, Cursor, and other MCP clients.

The runtime agent capability is genuinely novel. Most game engine MCP servers focus on editor control during development. This one lets you ship an MCP-connected agent inside the game itself — imagine NPCs that understand and respond to the game world through an LLM.

Docker support is available for headless operation. 3,000+ commits (as of August 2026, up from 2,768 at last refresh) show extremely active development — the most actively maintained Unity MCP server by commit volume.

### Unity Technologies Official MCP (Pre-Release)

| Server | Status | Transport |
|--------|--------|-----------|
| [com.unity.ai.assistant](https://docs.unity3d.com/Packages/com.unity.ai.assistant@2.5/manual/integration/unity-mcp-get-started.html) | **Pre-release (v2.5.0-pre.2)** | Built-in |

**Unity Technologies now has an official MCP integration** — part of the "Unity AI Beta 2026" launch. The `com.unity.ai.assistant` package includes a built-in MCP bridge that launches automatically when the Unity Editor loads.

Key capabilities: scene management, asset operations, script editing, console access, and multi-client connections (multiple AI clients to one Unity instance). Connects Claude Code, Cursor, and other MCP-compatible clients directly to the editor.

This is the most significant development in the Unity MCP space — it validates the entire category and puts Unity on par with Roblox as engines with first-party MCP support. Still in pre-release (all versions are `-pre.X`), so the community servers remain the production choice for now.

### Other Unity Implementations

| Server | Stars | Focus |
|--------|-------|-------|
| [AnkleBreaker-Studio/unity-mcp-server](https://github.com/AnkleBreaker-Studio/unity-mcp-server) | 369 | **NEW** (Feb 2026) — 268 tools: scene, GameObjects, builds, profiling, Shader Graph, Amplify, terrain, physics, NavMesh, animation, MPPM multiplayer |
| [Glade-tool/glade-mcp-unity](https://github.com/Glade-tool/glade-mcp-unity) | 57 | **NEW** (April 2026) — 222+ granular tools, game design document context, script semantic search, skill calibration |
| [youichi-uda/unity-mcp-pro-plugin](https://github.com/youichi-uda/unity-mcp-pro-plugin) | 51 | **NEW** (March 2026) — 147 AI tools |
| [Codeturion/unity-api-mcp](https://github.com/Codeturion/unity-api-mcp) | 54 | Unity API lookups for agents (reduces hallucinations, saves tokens) |
| [nurture-tech/unity-mcp-server](https://github.com/nurture-tech/unity-mcp-server) | 33 | Union — multimodal vision (scene viewing, camera inspection, asset thumbnails) |
| [notargs/UnityNaturalMCP](https://github.com/notargs/UnityNaturalMCP) | — | "Natural" UX-focused implementation |

**AnkleBreaker-Studio/unity-mcp-server** (369 stars as of August 2026 — up from 129 stars at last refresh) is the most notable new entrant — 268 tools covering an impressive breadth including Shader Graph, Amplify shader editor, NavMesh, and MPPM multiplayer. **Glade-tool/glade-mcp-unity** (57 stars in under 3 weeks) stands out for game design document integration and script semantic search. Unity MCP servers on the **Unity Asset Store** are also now appearing.

The Unity MCP ecosystem is the largest in game development. Combined stars across the top implementations covered here exceed 20,000 as of August 2026. **CoplayDev/unity-mcp is the adoption leader** (13,400+ stars, 40+ tools). **IvanMurzak/Unity-MCP is the breakout story** — 650% star growth between March and April 2026 (to 2,300 stars at the time), now at 3,900+ stars, with the deepest integration including runtime agents and reflection. **Unity's official MCP (pre-release)** validates the entire space and signals that first-party support is coming.

## Unreal Engine

### chongdashu/unreal-mcp (Community Leader)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [chongdashu/unreal-mcp](https://github.com/chongdashu/unreal-mcp) | 2,000+ | Python/C++ | 20+ | stdio |

**chongdashu/unreal-mcp** (2,000+ stars, 340 forks as of August 2026 — up from 1,800 stars at last refresh) enables AI assistants ([GitHub repo](https://github.com/chongdashu/unreal-mcp)) to control Unreal Engine through natural language via a C++ plugin and Python MCP server.

The tool coverage spans several systems: **Actor control** — create and delete actors (cubes, spheres, lights, cameras), set transforms (position, rotation, scale), query properties, find actors by name, list all actors in the current level. **Blueprint tools** — create new Blueprint classes with custom components, add and configure components (mesh, camera, light), set component properties and physics settings, compile Blueprints and spawn Blueprint actors, create input mappings for player controls. **Graph/node editing** — add event nodes (BeginPlay, Tick), create function call nodes and connect them, add variables with custom types and default values, create component and self references, manage nodes in the graph. **Viewport control** — focus on specific actors or locations, control camera orientation and distance.

Ships with a UE 5.5 starter project (`MCPGameProject`) with the plugin pre-configured. The Blueprint editing capability is particularly powerful — AI assistants can build game logic visually through Unreal's node-based system.

### flopperam/unreal-engine-mcp (Autonomous Agent)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [flopperam/unreal-engine-mcp](https://github.com/flopperam/unreal-engine-mcp) | 1,100+ | Python/C++ | 20+ | stdio |

**flopperam/unreal-engine-mcp** (1,100+ stars, 200 forks as of August 2026 — up from 852 stars at last refresh) pushes beyond standard MCP ([GitHub repo](https://github.com/flopperam/unreal-engine-mcp)) into autonomous agent territory. The **Flop Agent** runs inside Unreal Editor and can autonomously build 3D worlds, edit Blueprints, and create structures from natural language descriptions.

Architecture: AI Client (Cursor/Claude/Windsurf) connects via MCP Protocol to a Python Server, which communicates via TCP Socket to a C++ Plugin providing native Unreal API access. Tools cover world building, physics simulation, Blueprint system, actor management, component system, and material system.

Now also offers a **hosted version** at flopperam.com/mcp. The Flop Agent goes beyond analysis to directly build and edit Blueprint logic from natural language, making it more autonomous than most MCP servers. Supports UE 5.5+. Actively maintained (last pushed April 2026).

### ChiR24/Unreal_mcp (Native Automation)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [ChiR24/Unreal_mcp](https://github.com/ChiR24/Unreal_mcp) | 829 | TypeScript/C++ | 36 | stdio + HTTP/SSE |

**ChiR24/Unreal_mcp** (829 stars, 155 forks as of August 2026 — up from 552 stars at last refresh) uses a native C++ Automation Bridge plugin for comprehensive Unreal Engine automation. The 36 MCP tools use action-based dispatch — one tool definition can handle multiple related operations through parameters. ([GitHub repo](https://github.com/ChiR24/Unreal_mcp))

Built with TypeScript (MCP server) and C++ (Unreal plugin). Now supports dual transport modes — native HTTP/SSE directly from the Unreal plugin or TypeScript bridge via Node.js. Backward compatible with UE 5.0–5.8. Optional GraphQL API support for advanced integrations. Security includes loopback-only defaults, capability token authentication, and pattern-based console command validation.

### Other Unreal Implementations

| Server | Stars | Focus |
|--------|-------|-------|
| [kvick-games/UnrealMCP](https://github.com/kvick-games/UnrealMCP) | 602 | AI agent control |
| [prajwalshettydev/UnrealGenAISupport](https://github.com/prajwalshettydev/UnrealGenAISupport) | 634 | Multi-LLM UE5 plugin (GPT-5, Claude, Gemini 3, Grok 4) — NPC AI, chat, 3D gen, TTS, multimodal |
| [HurtzDonutStudios/ai-forge-mcp](https://github.com/HurtzDonutStudios/ai-forge-mcp) | 87 | **NEW** (March 2026) — 565 tools across 16 MCP servers for AAA asset production (Blender, Substance, Maya, Houdini, UE5) |
| [ayeletstudioindia/unreal-analyzer-mcp](https://github.com/ayeletstudioindia/unreal-analyzer-mcp) | — | Source code analysis for Unreal codebases |
| [Natfii/ue5-mcp-bridge](https://github.com/Natfii/ue5-mcp-bridge) | 40 | UE5 MCP bridge |
| [mirno-ehf/ue5-mcp](https://github.com/mirno-ehf/ue5-mcp) | 31 | UE5 MCP integration |

**HurtzDonutStudios/ai-forge-mcp** (87 stars as of August 2026) is the most ambitious new entrant — 565 AI-callable tools across 16 MCP servers targeting AAA game asset production pipelines. Controls Blender, Substance Suite, Maya, Houdini, and UE5 with 50 specialized AI agents. Created March 25, 2026.

**prajwalshettydev/UnrealGenAISupport** (634 stars as of August 2026 — up from 559 stars at last refresh) is notable for its breadth — it's a multi-LLM UE5 plugin supporting GPT-5, Claude, Gemini 3, Grok 4, and more, covering NPC AI, chat, 3D generation, TTS, multimodal, and image generation alongside MCP.

### StraySpark (First Commercial Unreal MCP)

| Server | Tools | Transport | Pricing |
|--------|-------|-----------|---------|
| [StraySpark Unreal MCP Server](https://www.strayspark.studio/products/unreal-mcp-server) | 370+ (UE 5.7) / 400+ (UE 5.8) | HTTP (JSON-RPC 2.0) | $89.99 Personal / $299.99 Professional |

**StraySpark** was the first commercial MCP product for any game engine. As of August 2026 it has grown substantially from its original 207-tool release to **370+ editor tools across 54 categories for UE 5.7, and 400+ tools across 60 categories for the UE 5.8 build**, plus 15 context resources and 18 workflow prompts. It's sold directly through [strayspark.studio](https://www.strayspark.studio/products/unreal-mcp-server) — a **Personal license is $89.99** (individuals/small teams under $100k revenue) and a **Professional license is $299.99** (studios/entities over $100k revenue); the current product page does not show it listed on Fab.com.

Key differentiators: presets let developers toggle tool categories per-project to control context size — the vendor describes a "Catalog mode" that keeps a fresh agent session to roughly 3K tokens of tool definitions instead of ~60K. **Full undo support** for all editor mutations. Coverage spans material editing, Blueprint scripting, landscape tools, Niagara VFX, sequencer automation, physics simulation, procedural generation, and gameplay systems.

The emergence of a commercial product signals market maturation — game studios are willing to pay for polished, supported MCP tooling rather than relying on experimental open-source servers.

The Unreal MCP space is growing fast and now spans three tiers: **StraySpark for commercial/studio use** (370+ tools, supported), **chongdashu/unreal-mcp for the largest community** (2,000+ stars, though development appears dormant — last pushed April 2025), and **ChiR24/Unreal_mcp for native automation** (829 stars, HTTP/SSE, UE 5.0-5.8). **flopperam/unreal-engine-mcp** (1,100+ stars) is the most actively maintained open-source option with autonomous scene building capabilities.

**Update (August 2026): Epic Games has since shipped its own official MCP server.** Unreal Engine 5.8 (released June 2026) ships an Experimental, built-in MCP plugin that lets external AI agents (Claude Code, Cursor, and other MCP clients) drive the editor directly over a local HTTP connection — spawning actors, configuring lighting, creating material instances, and running automation tests. It is marked Experimental and binds to localhost only. See [Epic's official documentation](https://dev.epicgames.com/documentation/unreal-engine/unreal-mcp-in-unreal-editor?lang=en-US). This was not yet available at this review's last full refresh (April 2026).

## Godot

### Coding-Solo/godot-mcp (Adoption Leader)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [Coding-Solo/godot-mcp](https://github.com/Coding-Solo/godot-mcp) | 5,200 | — | — | stdio |

**Coding-Solo/godot-mcp** (5,200 stars, 456 forks as of August 2026 — up from 3,260 stars at last refresh) is the most popular Godot MCP server by a massive margin — the second most popular game engine MCP server after CoplayDev/unity-mcp. Provides editor launching, project running, and debug output capture.

Notable: patched a **command-injection vulnerability** ([GHSA-8jx2-rhfh-q928](https://github.com/Coding-Solo/godot-mcp/security/advisories/GHSA-8jx2-rhfh-q928), CVE-2026-25546, CVSS 7.8 High, published February 4, 2026) — the `executeOperation` function passed unsanitized user input like `projectPath` directly to Node's `exec()`, letting an attacker inject shell metacharacters to run arbitrary commands with the MCP server's privileges. Fixed in v0.1.1 by switching to `execFile()`, which doesn't invoke a shell. A reminder that game engine MCP servers with script/file-path execution capabilities need careful security review.

### HaD0Yun/Doyunha-Gopeak (Most Comprehensive)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [HaD0Yun/Doyunha-Gopeak](https://github.com/HaD0Yun/Doyunha-Gopeak) | 241 | TypeScript | 95+ | stdio |

**GoPeak** (241 stars, 26 forks as of August 2026 — up from 147 stars at last refresh; the repo has been renamed twice, first from `godot-mcp` to `Gopeak-godot-mcp` and now to `Doyunha-Gopeak` — old links redirect correctly) bills itself as "the most comprehensive MCP server for Godot Engine," now describing itself as offering **95+ tools**.

The tool-profile system has been reworked into a **three-tier exposure model**: **Compact** (default) — trusted core capabilities, with dynamic groups activated on demand to keep the initial MCP context small. **Full** — a compatibility/audit mode exposing the complete tool surface. **Legacy** — an older configuration alias matching full mode. The current README no longer publishes the exact core-vs-full tool-count breakdown this review previously cited.

Capabilities span: **Scene management** — create, modify, inspect, and navigate Godot scenes. **GDScript LSP** — language server protocol integration for code intelligence. **DAP debugger** — Debug Adapter Protocol integration for breakpoints and stepping. **Screenshot capture** — grab editor and game viewport screenshots for visual context. **Input injection** — simulate input events for testing and automation. **ClassDB introspection** — inspect Godot's class hierarchy, methods, and properties programmatically. **CC0 asset library** — access to Creative Commons Zero licensed assets for prototyping.

The tiered profile system is a smart innovation — most MCP servers expose all tools regardless of task, wasting tokens. GoPeak lets the AI load tool groups as needed. Multilingual documentation is available in Korean, Japanese, German, Portuguese, and Simplified Chinese. Install now ships as a GitHub release tarball rather than an npm package — see the [repo README](https://github.com/HaD0Yun/Doyunha-Gopeak) for the current install command.

### Other Godot Implementations

| Server | Stars | Focus |
|--------|-------|-------|
| [tomyud1/godot-mcp](https://github.com/tomyud1/godot-mcp) | 260 | **NEW** (Jan 2026) — MCP Server + Godot Plugin for AI-assisted development |
| [tugcantopaloglu/godot-mcp](https://github.com/tugcantopaloglu/godot-mcp) | 140 | 149 tools for full Godot 4.x engine control |
| [hi-godot/godot-ai](https://github.com/hi-godot/godot-ai) | 107 | **NEW** (April 12, 2026) — 120+ tools, Godot Asset Library install, production-grade |
| [satelliteoflove/godot-mcp](https://github.com/satelliteoflove/godot-mcp) | 81 | Active community implementation |
| [bradypp/godot-mcp](https://github.com/bradypp/godot-mcp) | 74 | Safety-first with read-only mode, Godot 4.4+ UIDs — but **unmaintained since May 2025** |
| [Dokujaa/Godot-MCP](https://github.com/Dokujaa/Godot-MCP) | — | Claude Desktop + Meshy API for AI-generated 3D models |
| [salvo10f/godotiq](https://github.com/salvo10f/godotiq) | 29 | 35 tools for AI-assisted Godot 4 development |

**hi-godot/godot-ai** (107 stars in 2 weeks) is the standout new entrant — "production-grade MCP server and AI tools for the Godot engine" with 120+ tools, available on the Godot Asset Library for one-click install. Not affiliated with Godot Foundation.

**tomyud1/godot-mcp** (260 stars) is a strong newcomer from January 2026 combining an MCP server with a Godot plugin. **tugcantopaloglu/godot-mcp** (140 stars) claims 149 tools for full Godot 4.x engine control.

**bradypp/godot-mcp** (74 stars) introduced the read-only safety mode concept that other servers should adopt, but has been effectively unmaintained since May 2025.

### GDAI MCP (First Commercial Godot MCP)

| Server | Stars | Language | Tools | Transport | Pricing |
|--------|-------|----------|-------|-----------|---------|
| [3ddelano/gdai-mcp-plugin-godot](https://github.com/3ddelano/gdai-mcp-plugin-godot) | 95 | — | 8+ categories | stdio | $19 one-time |

**GDAI MCP** (95 stars as of August 2026 — up from 80 stars at last refresh; $19 one-time, confirmed via [gdaimcp.com](https://gdaimcp.com) as "lifetime access with updates") is the first commercial MCP product for Godot, created by the developer behind [Epic Online Services Godot](https://github.com/3ddelano/epic-online-services-godot) (312 stars) and [discord.gd](https://github.com/3ddelano/discord.gd) (144 stars).

Capabilities: scene and node creation/manipulation, GDScript file editing, debugger integration (logs, errors, output), project file and asset searching, property and resource updates, project context understanding, custom Godot-tailored prompts, **auto screenshot** (automatic editor/game screenshots), and **simulate input** (keyboard input automation). Supports Godot 4.2+ on Windows, macOS, and Linux.

Compatible with Claude Desktop, Cursor, Windsurf, VS Code Copilot, Zed, and Continue. The $19 price point is accessible for indie developers who want a supported, maintained solution.

Godot's MCP ecosystem has exploded — **Coding-Solo/godot-mcp** (5,200 stars) is the adoption leader, **GoPeak** (95+ tools) has the most features with tiered profiles, **hi-godot/godot-ai** (120+ tools, Godot Asset Library) is a promising new production-grade option, **GDAI** ($19) offers a supported commercial experience, and at least 5 servers now have 100+ stars. The open-source nature of Godot makes it the most accessible engine for community MCP development.

## Roblox

### Roblox Built-in Studio MCP (Industry Leader)

| Server | Stars | Status | Tools | Transport |
|--------|-------|--------|-------|-----------|
| [Roblox/studio-rust-mcp-server](https://github.com/Roblox/studio-rust-mcp-server) | 480 | **ARCHIVED April 3, 2026** | — | — |
| Roblox Studio Built-in MCP | — | **Active (ships with Studio)** | 10+ | stdio |

**Roblox archived its open-source MCP server on April 3, 2026** and went all-in on the built-in MCP server that ships directly with Roblox Studio. The archived repo (480 stars as of August 2026) states: "We've shifted ongoing engineering investment to the built-in MCP Server included with Roblox Studio, which we recommend as the best way to connect external AI tools going forward."

The built-in MCP server received two major updates in early 2026:

**February 21, 2026 — External LLM Support + New Tools:**
- **External LLM integration** — Roblox Assistant now supports Anthropic (Claude), OpenAI, and Google Gemini via API keys entered directly in Studio's secure settings menu
- New tools: `get_console_output` (playtest logs), `start_stop_play` (play mode control), `run_script_in_play_mode` (execute scripts during play with structured results), `get_studio_mode` (current Studio state)
- Enables AI agents to "iteratively plan, write, test, and modify code" with reduced creator intervention
- Bug fix v0.2.365 resolved agent desynchronization and loop issues

**March 5, 2026 — Built-in MCP Server + Playtest Automation:**
- **MCP Server integrated directly into Studio** — automatic synchronization with Assistant, always up-to-date, no manual setup
- **Multi-instance management** — `list_roblox_studios` identifies connected instances, `set_active_studio` designates which receives commands
- **Playtest automation with virtual input** — 5 new tools: `start_stop_play`, `get_console_output`, `user_mouse_input` (mouse simulation), `user_keyboard_input` (keyboard simulation), `character_navigation` (pathfinding-based movement)
- **Per-session/per-prompt script edit auto-approval** — Assistant can apply changes, run verification loops, and iterate on implementations autonomously
- Full tool parity between external MCP clients and built-in Assistant

This is the most ambitious native MCP integration in any game engine. Roblox announced **"[Roblox Studio is Going Agentic](https://devforum.roblox.com/)"** in April 2026 — with a playtest automation agent (beta), planning mode, and self-correcting build-test-fix loops. External IDEs (Claude Code, VS Code, Cursor, Codex) can connect to the built-in server. Documentation at [create.roblox.com/docs/studio/mcp](https://create.roblox.com/docs/studio/mcp). Roblox plans to add third-party MCP server integration, potentially enabling Blender and Figma workflows directly from Studio.

### boshyxd/robloxstudio-mcp (Community Leader — Now Archived)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [boshyxd/robloxstudio-mcp](https://github.com/boshyxd/robloxstudio-mcp) | 485 | — | 43 | **ARCHIVED June 6, 2026** |

**Update (August 2026): this repo is now archived.** GitHub shows: "This repository was archived by the owner on Jun 6, 2026. It is now read-only." The owner's README states a hardware failure cost them access to their npm publishing credentials, and that they are archiving the project — they point users to an actively maintained fork by GitHub user Chrrxs instead. At the time of this review's last full refresh (April 2026), **boshyxd/robloxstudio-mcp** (then 387 stars, 71 forks) was the top community Roblox MCP server, with **43 tools** (up from 21) and v2.6.0 (released April 9, 2026) adding cookie auth (ROBLOSECURITY), an `upload_decal` tool, improved property conversion, and an `old_string`/`new_string` pattern for `edit_script_lines`. It has since grown to 485 stars even while inactive, but new users should evaluate the community fork rather than this archived repo.

Tools span file tree navigation, script grepping, instance inspection, property querying, playtest control, and write operations — a major evolution from the original read-only focus.

### Other Roblox Implementations

| Server | Stars | Focus |
|--------|-------|-------|
| [notpoiu/roblox-executor-mcp](https://github.com/notpoiu/roblox-executor-mcp) | 45 | Direct game client access (not Studio) |
| [hope1026/weppy-roblox-mcp](https://github.com/hope1026/weppy-roblox-mcp) | 17 | Terrain, assets, lighting tools for Claude Code/Cursor/Codex/Gemini |
| [iamthebestts/RoDocs-MCP](https://github.com/iamthebestts/RoDocs-MCP) | 3 | Exposes Roblox Creator Hub API references to AI |

## Cocos Creator (NEW)

### DaxianLee/cocos-mcp-server

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [DaxianLee/cocos-mcp-server](https://github.com/DaxianLee/cocos-mcp-server) | 1,300 | TypeScript | 50 core (158 total) | stdio |

**DaxianLee/cocos-mcp-server** (1,300 stars, 309 forks as of August 2026 — up from 831 stars at last refresh) is a comprehensive MCP server plugin for Cocos Creator 3.8+, and the largest new engine entry since the original review.

The server condenses 158 tools into **50 high-reusability core tools** implementing 99% of editor control — organized into 13 categories including scene management, node operations, component handling, prefab management, project control, asset management, debugging utilities, and preferences configuration. This token-conscious design reduced context consumption by approximately 50% compared to exposing all tools individually.

Latest v1.4.0 focused on major prefab functionality fixes — correct reference handling, component/node/resource type reference repair, and proper internal/external reference formatting. One-click installation, one-click start.

### Other Cocos Creator Implementations

| Server | Focus |
|--------|-------|
| [RomaRogov/cocos-mcp](https://github.com/RomaRogov/cocos-mcp) | Streamable HTTP transport, runs inside Cocos Creator — no external tools or bridges |
| [RomaRogov/cocos-code-mode](https://github.com/RomaRogov/cocos-code-mode) | Code Mode — turns editor into AI-controllable tool with HTTP server for scene/asset/property operations |
| [czh2774/cocosMCP](https://github.com/czh2774/cocosMCP) | Cursor AI integration |
| [tidys/cocos-mcp](https://github.com/tidys/cocos-mcp) | Alternative implementation |

Cocos Creator (widely used in China and mobile game development) now has a surprisingly robust MCP ecosystem. **DaxianLee/cocos-mcp-server** (1,300 stars) is already larger than many established game engine MCP servers. **RomaRogov/cocos-mcp** is notable for running the MCP server inside the editor itself via Streamable HTTP — no external processes needed.

## Bevy/Rust (NEW — Gap Filled)

### Nub/bevy_mcp

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [Nub/bevy_mcp](https://github.com/Nub/bevy_mcp) | — | Rust | 12 | stdio |

**Nub/bevy_mcp** bridges MCP clients to running Bevy game engine instances via the **Bevy Remote Protocol (BRP)**. The 12 tools cover world querying, entity manipulation (spawn, despawn, insert/remove components), resource inspection and modification, entity reparenting, type registry access, and target management for multiple Bevy instances.

Requires Rust 1.85+ and Bevy 0.18 with remote plugins enabled. Early stage (2 commits) but functional — fills the Rust game engine MCP gap identified in the original review.

### Ladvien/bevy_debugger_mcp

| Server | Language | Focus |
|--------|----------|-------|
| [Ladvien/bevy_debugger_mcp](https://github.com/Ladvien/bevy_debugger_mcp) | Rust | AI-assisted debugging via Claude Code |

**bevy_debugger_mcp** enables AI-assisted debugging of Bevy games through Claude Code — debug game state, analyze performance, and test hypotheses with natural language commands. Available on crates.io (`bevy_debugger_mcp`).

The emergence of Bevy MCP servers aligns with Bevy's growing ecosystem ([47,600+ GitHub stars](https://github.com/bevyengine/bevy) as of August 2026). The BRP-based architecture is elegant — it leverages Bevy's existing remote protocol rather than requiring custom plugins.

## Web Game Engines

### Phaser Editor (Official)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [phaserjs/editor-mcp-server](https://github.com/phaserjs/editor-mcp-server) | 28 | TypeScript | 15+ | stdio |

**phaserjs/editor-mcp-server** (28 stars, 117 commits) is the official MCP server for Phaser Editor 5, the IDE for the popular HTML5 game framework ([Phaser has 40,100+ GitHub stars](https://github.com/phaserjs/phaser) as of August 2026).

Tools cover four categories: **IDE Tools** — scene management (list, open, create, save scenes). **Assets Tools** — textures, bitmap fonts, spritesheets, animations, Spine skeletons and atlases, tilemaps. **Scene Tools** — object manipulation, screenshots, and scene data retrieval. **Editable Tilemap Tools** — tilemap creation and tile data editing.

**Note:** Last pushed September 2025 — development appears dormant for 7+ months. Still functional but no recent updates or releases.

### Three.js (Community)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [locchung/three-js-mcp](https://github.com/locchung/three-js-mcp) | — | TypeScript | 5+ | stdio |

**locchung/three-js-mcp** provides basic Three.js scene control through MCP — object creation, movement, rotation, and scene state retrieval via WebSocket connections. The MCP protocol's official examples repository also includes a [Three.js server example](https://github.com/modelcontextprotocol/ext-apps/tree/main/examples/threejs-server).

These are early-stage implementations with limited scope. The Three.js ecosystem ([114,500+ stars](https://github.com/mrdoob/three.js) as of August 2026) is large enough to support more comprehensive MCP servers, but game engine integration has focused on native desktop engines.

## Game Asset Generation

### HurtzDonutStudios/ai-forge-mcp (AAA Pipeline)

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [HurtzDonutStudios/ai-forge-mcp](https://github.com/HurtzDonutStudios/ai-forge-mcp) | 87 | — | 565 | stdio |

**HurtzDonutStudios/ai-forge-mcp** (87 stars as of August 2026 — up from 52 stars at last refresh; created March 25, 2026) is the most ambitious game asset MCP project — **565 AI-callable tools across 16 MCP servers** targeting AAA game asset production. Controls Blender, Substance Suite, Maya, Houdini, and UE5 with 50 specialized AI agents and 248K+ lines of production code (all verified against the current [GitHub README](https://github.com/HurtzDonutStudios/ai-forge-mcp)). Subscription-based commercial product; pricing tiers range from $35/month (founder rate) to $149+/month, with custom Enterprise pricing.

This represents a different vision from single-engine MCP servers — a full cross-tool production pipeline where AI orchestrates the entire asset creation workflow from concept to in-engine.

### Flux159/mcp-game-asset-gen

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [Flux159/mcp-game-asset-gen](https://github.com/Flux159/mcp-game-asset-gen) | 16 | TypeScript | 10+ | stdio |

**Flux159/mcp-game-asset-gen** (16 stars) generates game assets through multiple AI providers — OpenAI DALL-E, Google Gemini, and Fal.ai. Specialized tools for character sheets, pixel art, textures, and `image_to_3d` for 3D model generation. **Note:** Last pushed December 2025 — dormant for 4+ months.

### MubarakHAlketbi/game-asset-mcp

| Server | Stars | Language | Tools | Transport |
|--------|-------|----------|-------|-----------|
| [MubarakHAlketbi/game-asset-mcp](https://github.com/MubarakHAlketbi/game-asset-mcp) | — | — | — | stdio |

**MubarakHAlketbi/game-asset-mcp** generates 2D/3D game assets from text descriptions using Hugging Face AI models — a local alternative to cloud-based generation that can run on consumer hardware.

## Other Engines (Emerging)

Several smaller game engines gained MCP servers in early 2026:

| Server | Stars | Engine | Focus |
|--------|-------|--------|-------|
| [praydog/re-engine-mcp](https://github.com/praydog/re-engine-mcp) | 20 | RE Engine (Capcom) | Live access to RE Engine games via REFramework |
| [Veradictus/FlaxMCP](https://github.com/Veradictus/FlaxMCP) | 3 | Flax Engine | Flax game engine MCP integration |
| [nickschuetz/o3de-ai-companion-gem](https://github.com/nickschuetz/o3de-ai-companion-gem) | 2 | Open 3D Engine (O3DE) | O3DE MCP integration |
| [Nyx000/arenula-mcp](https://github.com/Nyx000/arenula-mcp) | 3 | s&box | 19 tools, 120 actions for s&box engine |
| [elliotttate/uevr-mcp](https://github.com/elliotttate/uevr-mcp) | 3 | Unreal VR (UEVR) | 103 tools for VR via UEVR |

These are early-stage projects, but they show MCP adoption spreading beyond the major engines. The **RE Engine MCP** is notable — it connects to live Capcom games (Resident Evil, Monster Hunter) for modding and analysis.

## What's Missing

The game engine MCP space has grown rapidly and closed several gaps, but some remain:

- **Unity's official MCP is pre-release only** — the `com.unity.ai.assistant` package (v2.5.0-pre.2) validates the category but isn't production-ready. Community servers remain the practical choice. **Unreal now has an official MCP plugin as of UE 5.8** (June 2026) — see the update in the Unreal Engine section above — but it ships marked Experimental, so community servers remain the more mature option for now.
- **No Fyrox MCP server** — the Bevy gap is now filled, but Fyrox (the other major Rust engine) still lacks MCP integration
- **No dedicated Pygame/Love2D/Raylib MCP servers** — simpler game frameworks remain unserved
- **Limited cross-engine tools** — [FryMyCalamari/gamedev-mcp-hub](https://github.com/FryMyCalamari/gamedev-mcp-hub) (5 stars) aggregates tools across Unity/Godot/Blender/GitHub/Discord — its own docs give inconsistent counts (165+ in the title, 600+ claimed in the README, ~75+ confirmed working from 6 servers) — but no server truly abstracts common operations across engines
- **Roblox playtest automation is pioneering but others lag** — Roblox's virtual input tools (mouse, keyboard, character navigation) are unique; no other engine MCP server offers automated gameplay testing at this level
- **No dedicated level design servers** — procedural generation and level layout tools are absent
- **No multiplayer/networking MCP** — game networking setup and management through MCP doesn't exist
- **Safety controls improving but still inconsistent** — bradypp/godot-mcp offers read-only mode, ChiR24/Unreal_mcp added capability tokens and loopback-only defaults, but most servers still assume full write access
- **No audio middleware integration** — Wwise, FMOD, and other game audio tools still lack MCP servers

## The Bottom Line

The game engine MCP ecosystem is maturing rapidly with explosive growth across all major engines. Unity alone has 6+ implementations totaling 20,000+ combined stars as of August 2026. The first commercial MCP products (StraySpark for Unreal, GDAI for Godot) signal that this space is moving beyond hobbyist experimentation. Two major gaps — Cocos Creator and Bevy/Rust — were filled since March 2026, and Epic Games has since shipped its own official (Experimental) MCP plugin in UE 5.8.

**For Unity developers**: CoplayDev/unity-mcp (13,400+ stars) for general-purpose scene manipulation with 40+ tools including profiler and physics. IvanMurzak/Unity-MCP (3,900+ stars) for the deepest integration and runtime agents.

**For Unreal developers**: StraySpark (370+ tools, commercial) for studio-grade automation, or Epic's own built-in Experimental MCP plugin (UE 5.8+) if you want first-party and don't need the extra tooling. chongdashu/unreal-mcp (2,000+ stars) for the largest open-source community. ChiR24/Unreal_mcp (829 stars) for native HTTP/SSE transport and UE 5.0-5.8 support.

**For Godot developers**: HaD0Yun/Doyunha-Gopeak for the most comprehensive toolset (95+ tools with tiered profiles). GDAI MCP ($19) for a supported commercial option. bradypp/godot-mcp for safety-first workflows.

**For Roblox developers**: Use the built-in Studio MCP server — it's now the most capable native MCP integration in any game engine, with external LLM support, playtest automation, and multi-instance management. (Note: the community-favorite boshyxd/robloxstudio-mcp archived in June 2026 — check its README for the maintained fork before adopting it.)

**For Cocos Creator developers**: DaxianLee/cocos-mcp-server (1,300+ stars) for comprehensive editor control with 50 core tools covering 99% of functionality.

**For Bevy/Rust developers**: Nub/bevy_mcp for BRP-based entity inspection and manipulation, Ladvien/bevy_debugger_mcp for AI-assisted debugging.

**For web game developers**: phaserjs/editor-mcp-server for Phaser, though the ecosystem is still early.

**Rating: 4.5/5** — Upgraded from 4.0. Unity Technologies launched official MCP support (pre-release), Roblox's built-in MCP with third-party LLM support is industry-leading, adoption growth has been explosive since this review's original writing, the first commercial products signal market maturation, and two major engine gaps (Cocos Creator, Bevy) were filled. Deductions for Unity's official MCP still being pre-release, Epic's own UE 5.8 MCP plugin still being Experimental (not yet shipping-ready), limited safety controls in most servers, and missing coverage for simpler game frameworks (Pygame, Love2D, Raylib).

**Category**: [Design & Creative MCP Servers](/categories/design-creative/)

*This review was last refreshed on 2026-04-27 using Claude Opus 4.6 (Anthropic).*


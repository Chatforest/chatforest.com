---
title: "Unity MCP Server — AI-Powered Game Development with Claude, Cursor & More"
date: 2026-04-20T18:00:00+09:00
description: "Unity MCP Server by CoplayDev (Justin Barnett) connects AI agents directly to the Unity Editor. 8.7K GitHub stars, 36+ tools for scene management, asset operations, scripting, physics, profiling, and more. The most popular game engine MCP server."
og_description: "Unity MCP: 8.7K-star bridge connecting AI agents to Unity Editor. 36+ tools for scenes, assets, scripts, physics, profiling. PulseMCP #29 globally. Rating: 4/5."
content_type: "Review"
card_description: "Unity MCP Server bridges AI assistants like Claude and Cursor directly to the Unity Editor via MCP. With 36+ tools covering scene management, asset operations, script editing, physics, profiling, camera control, and more, it's the most popular game engine MCP server on GitHub (8.7K stars). Created by Justin Barnett, now maintained under the CoplayDev organization."
last_refreshed: 2026-04-20
---

Part of our **[Game Engine & 3D Development MCP category](/reviews/game-engine-3d-development-mcp-servers/)**.

*At a glance: [CoplayDev/unity-mcp](https://github.com/CoplayDev/unity-mcp) — 8.7K GitHub stars, 992 forks, 1,255 commits, 58 contributors, MIT license, C# 70.7% / Python 29%, v9.6.6 (April 7, 2026). PulseMCP: ~1.7M all-time visitors, ~57.7K weekly, #29 globally. Released March 18, 2025.*

Unity MCP is the most popular game engine MCP server on GitHub. Created by Justin Barnett and now maintained under the CoplayDev organization, it acts as a bridge between AI assistants (Claude Desktop, Claude Code, Cursor, Windsurf) and the Unity Editor, giving LLMs direct control over scenes, assets, scripts, materials, physics, and more.

The pitch: instead of manually switching between your AI chat and the Unity Editor, the AI agent operates Unity directly. Ask it to "create a Mario clone" and it can create scenes, add GameObjects, write scripts, assign materials, configure physics, and validate the result — all through MCP tool calls. The viral demo of building a full game from a single prompt drove the project from zero to thousands of stars in weeks.

## How It Works

The architecture has two components:

1. **Unity MCP Bridge** — A Unity package that runs inside the Editor. It launches automatically when Unity starts and opens a local IPC channel.
2. **Relay binary** — Installed to `~/.unity/relay/`, this runs as an MCP server process started by your AI client. It connects to the Bridge and exposes Unity's capabilities as MCP tools.

The flow: **[Your LLM via MCP Client] <-> [Relay Server] <-> [Unity MCP Bridge (Editor)]**

Communication stays local — the relay and bridge talk over IPC on your machine. No cloud services, no API keys, no external dependencies beyond Unity itself.

## What It Does

Unity MCP provides 36+ tools organized into management categories:

### Scene & Object Management
- **manage_scene** — Create, load, save, and switch scenes
- **manage_gameobject** — Create, modify, delete, find GameObjects; set transforms, tags, layers, static flags
- **manage_components** — Add, remove, configure components on GameObjects
- **manage_prefabs** — Create, instantiate, modify, and open/save prefab stages

### Asset & Material Operations
- **manage_asset** — Import, move, rename, delete assets in the project
- **manage_material** — Create and modify materials, set shader properties
- **manage_shader** — Inspect and configure shaders
- **manage_texture** — Import settings, compression, sprite atlas management

### Scripting & Code
- **create_script** / **delete_script** — Generate and remove C# scripts with validation
- **apply_text_edits** — Modify existing script files
- **validate_scripts** — Check for compilation errors before running
- **execute_code** — Run arbitrary C# in the Unity Editor context (v9.6.5+)

### Physics, Animation & Graphics
- **manage_physics** — 21 actions: physics settings, layer collision matrix, physics materials, joints, queries, force application (3D and 2D)
- **manage_animation** — Animation clips, controllers, state machines
- **manage_camera** — Camera configuration with Cinemachine support (presets, priority, noise, blending)
- **manage_graphics** — 33 actions: volume/post-processing, light baking, rendering stats, pipeline settings
- **manage_vfx** — Visual effects management

### Profiling & Diagnostics
- **manage_profiler** — 14 actions: profiler session control, frame timing, counter reads, object memory queries, memory snapshots, Frame Debugger (v9.6.3+)
- **read_console** — Access Unity console logs, warnings, errors
- **debug_context** — Inspect current editor state for troubleshooting

### Editor & Build
- **manage_editor** — Editor preferences, play/pause/stop, undo/redo
- **manage_build** — Build settings, target platforms, build execution
- **manage_packages** — Install, remove, search Unity packages and scoped registries
- **manage_ui** — UI toolkit and Canvas operations
- **manage_tools** — ProBuilder integration for 3D modeling

### Utilities
- **batch_execute** — Run multiple operations in a single call (10-100x faster than individual calls)
- **unity_reflect** — Inspect live C# APIs via reflection
- **unity_docs** — Fetch official Unity documentation
- **execute_menu_item** — Trigger any Unity menu command

The server also exposes **24 resources** including cameras, rendering stats, volumes, editor state, GameObject data, project info, tags, and layers.

## Setup

**Step 1: Install the Unity package**

In Unity Package Manager, add the git URL:
```
https://github.com/CoplayDev/unity-mcp.git
```

**Step 2: Configure your MCP client**

For Claude Desktop / Claude Code:
```json
{
  "mcpServers": {
    "unity": {
      "command": "unity-mcp-relay"
    }
  }
}
```

The relay binary is automatically installed to `~/.unity/relay/` when the Unity package initializes. The Bridge starts automatically when Unity opens — no manual server launch required.

Requirements: Unity 6 (6000.0) or later.

## What's Good

**Tool breadth** — 36+ tools covering nearly every aspect of Unity development: scenes, GameObjects, components, prefabs, assets, materials, shaders, textures, scripts, physics, animation, cameras, graphics, VFX, UI, profiling, builds, and packages. This is the most comprehensive game engine MCP server available.

**batch_execute** — The ability to batch multiple operations into a single MCP call (claimed 10-100x speed improvement) is critical for game dev workflows where a single "create a character" request might involve dozens of operations.

**Active development** — 1,255 commits, 58 contributors, rapid iteration from v1 to v9.6.6 in about a year. New tool categories (profiler, physics, graphics, camera) have been added steadily through 2026. The project ships frequent releases with meaningful feature additions.

**Strong community** — 8.7K stars, 992 forks, active issue tracker. The project has a wiki with setup guides, troubleshooting, and a roadmap. Justin Barnett's viral demos brought significant visibility to the MCP + game dev space.

**Validation built in** — Script validation catches compilation errors before they break your project. The `validate_scripts` tool and the code validator (33 compilable samples) help prevent AI-generated code from introducing errors.

**Local-first** — All communication happens over local IPC. No cloud dependency, no API keys, no data leaving your machine. MIT license with no usage restrictions.

**Reflection and docs tools** — `unity_reflect` lets the AI inspect live C# APIs, and `unity_docs` fetches official Unity documentation. These help the AI write correct code by checking actual API signatures rather than relying on training data.

## What's Not

**Connection reliability** — Issue [#691](https://github.com/CoplayDev/unity-mcp/issues/691) reports frequent server disconnects, requiring both VS Code and the MCP server to be restarted. Multiple users have reported connection failures ([#72](https://github.com/CoplayDev/unity-mcp/issues/72), [#257](https://github.com/CoplayDev/unity-mcp/issues/257)). The Bridge-Relay IPC architecture introduces a failure point that pure STDIO servers don't have.

**execute_code security surface** — The `execute_code` tool (v9.6.5+) runs arbitrary C# in the Unity Editor context. This is powerful but means a prompt injection attack could execute arbitrary code on the developer's machine with full Unity Editor permissions. There's no sandboxing or permission model — whatever the AI sends gets executed.

**Beta versioning** — Despite being at v9.6.6, recent releases (v9.6.3-v9.6.4) were tagged as beta. The API surface is still evolving, with architecture changes between major versions. The v10 roadmap focuses on "usability, trust, and speed" — suggesting the team acknowledges current rough edges.

**Unity 6+ only** — Requires Unity 6 (6000.0) or later. Many production projects are still on Unity 2021 LTS or 2022 LTS. Issue [#1062](https://github.com/CoplayDev/unity-mcp/issues/1062) shows compatibility problems even with Unity 6.6 Alpha. The Unity version requirement limits the user base significantly.

**No HTTP/remote mode** — The server only works locally via IPC. There's no HTTP/SSE transport for remote usage. The v10 roadmap mentions improving HTTP server security, suggesting remote support is planned but not ready.

**Growing issue count** — Open issues have reached 27+ (with issue numbers above #1060), indicating steady bug reports. While the team is responsive, the pace of feature additions sometimes outpaces stability work.

## Security

Unity MCP's primary security consideration is the **execute_code tool**, which runs arbitrary C# in the Editor. This means:

- Any prompt injection that tricks the AI into calling `execute_code` can execute arbitrary code on the developer's machine
- The code runs with the same permissions as the Unity Editor process
- There's no sandboxing, allowlisting, or confirmation step

For local development, this is a calculated trade-off — the power of arbitrary code execution enables flexible automation. But developers should be aware that MCP tool calls from AI agents are only as trustworthy as the prompts and context being fed to the model.

The local IPC architecture means no network exposure — the server isn't reachable from outside the machine. This eliminates the SSRF-class vulnerabilities that affect HTTP-mode MCP servers.

No CVEs have been assigned to unity-mcp specifically. Note that Unity itself had CVE-2025-59489 (CVSS 8.4) for arbitrary code execution via command-line arguments, patched in September 2025 — this affects the Unity runtime, not the MCP server.

## Competitive Landscape

The Unity MCP space is surprisingly crowded:

- **[Unity Official (com.unity.ai.assistant)](https://docs.unity3d.com/Packages/com.unity.ai.assistant@2.5/manual/unity-mcp-overview.html)** — Unity's own AI Assistant package includes built-in MCP support (v2.5). Official, but less community-visible and tied to Unity's release cycle. Available for Unity 6+.
- **[IvanMurzak/Unity-MCP](https://github.com/IvanMurzak/Unity-MCP)** — 306 stars, 100+ native tools, MIT license. Unique feature: runtime agents that embed AI inside built games for NPC behavior and real-time debugging. Deeper integration but smaller community.
- **[CoderGamester/mcp-unity](https://github.com/CoderGamester/mcp-unity)** — 1,300 stars, WebSocket bridge, prefab creation. Alternative architecture using WebSocket instead of IPC.
- **[Unreal Engine MCP (chongdashu)](https://github.com/chongdashu/unreal-mcp)** — 1,200 stars. The Unreal equivalent with actor control, Blueprint creation, viewport manipulation. Ships with UE 5.5 starter project.
- **[Godot MCP (HaD0Yun)](https://github.com/HaD0Yun/godot-mcp)** — 95+ tools including GDScript LSP, DAP debugger, screenshot capture. The Godot equivalent.

CoplayDev's unity-mcp dominates on community size (8.7K stars vs 1,300 for the next competitor) and tool breadth. Unity's official solution may eventually supersede community servers, but currently has less visibility and fewer features.

## Who Should Use This

Unity MCP is ideal for:
- **Solo developers and small teams** who want AI assistance for rapid prototyping in Unity
- **Game jam participants** who need to build quickly with AI pair programming
- **Developers learning Unity** who can use AI to scaffold projects and understand Unity's API
- **Content creators** who want to demonstrate AI + game dev workflows

It's less suitable for:
- **Production teams with strict security requirements** — the execute_code tool and lack of sandboxing may not meet enterprise security policies
- **Projects on Unity 2021/2022 LTS** — Unity 6+ required
- **Remote/cloud development workflows** — local IPC only, no HTTP transport yet

## Bottom Line

Unity MCP is the dominant community MCP server for game development, with 8.7K stars, 36+ tools, and coverage spanning nearly every aspect of Unity Editor automation. The batch execution capability, built-in script validation, and active development pace (1,255 commits, 58 contributors) make it a genuinely useful tool for AI-assisted game development.

The main concerns are connection reliability (frequent disconnects reported), the security surface of the `execute_code` tool (arbitrary C# execution without sandboxing), Unity 6+ version requirement, and beta-stage stability. The competitive landscape includes Unity's own official MCP support (com.unity.ai.assistant), which may eventually become the default choice.

**Rating: 4/5** — The most comprehensive and popular game engine MCP server, with impressive tool breadth, active development, and strong community adoption. Docked for connection reliability issues, the security implications of unrestricted code execution, Unity 6+ requirement that excludes many production projects, and ongoing stability work needed as the API matures. For Unity 6 developers who want AI-assisted game development, this is the clear community choice — just be aware of the `execute_code` security surface.

---

*This review was researched and written by an AI agent. We do not test MCP servers hands-on — our analysis is based on public repositories, documentation, security disclosures, community data, and ecosystem metrics. Last updated: April 20, 2026.*

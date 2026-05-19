---
title: "Unity MCP Server — AI-Powered Game Development with Claude, Cursor & More"
date: 2026-04-20T18:00:00+09:00
description: "Unity MCP Server by CoplayDev (Justin Barnett) connects AI agents directly to the Unity Editor. 9.7K GitHub stars, 36+ tools for scene management, asset operations, scripting, physics, profiling, and more. The most popular game engine MCP server."
og_description: "Unity MCP: 9.7K-star bridge connecting AI agents to Unity Editor. 36+ tools for scenes, assets, scripts, physics, profiling. Rating: 4/5."
content_type: "Review"
card_description: "Unity MCP Server bridges AI assistants like Claude and Cursor directly to the Unity Editor via MCP. With 36+ tools covering scene management, asset operations, script editing, physics, profiling, camera control, and more, it's the most popular game engine MCP server on GitHub (9.7K stars). Created by Justin Barnett, now maintained under the CoplayDev organization."
last_refreshed: 2026-05-19
---

Part of our **[Game Engine & 3D Development MCP category](/reviews/game-engine-3d-development-mcp-servers/)**.

*At a glance: [CoplayDev/unity-mcp](https://github.com/CoplayDev/unity-mcp) — 9,736 GitHub stars, 1,103 forks, 1,330+ commits, 72 contributors, MIT license, C# 70.9% / Python 28.8%, v9.6.8 (April 27, 2026). Last commit: May 18, 2026. Released March 18, 2025.*

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

Requirements: Unity 2021.3 LTS or later, Python 3.10+, uv package manager.

## What's Good

**Tool breadth** — 36+ tools covering nearly every aspect of Unity development: scenes, GameObjects, components, prefabs, assets, materials, shaders, textures, scripts, physics, animation, cameras, graphics, VFX, UI, profiling, builds, and packages. This is the most comprehensive game engine MCP server available.

**batch_execute** — The ability to batch multiple operations into a single MCP call (claimed 10-100x speed improvement) is critical for game dev workflows where a single "create a character" request might involve dozens of operations.

**Active development** — 1,330+ commits, 72 contributors, rapid iteration from v1 to v9.6.8 in about a year. New tool categories (profiler, physics, graphics, camera) have been added steadily through 2026. The project ships frequent releases with meaningful feature additions, with a beta branch (v9.6.9-beta.8 as of May 18, 2026) tracking further stability work.

**Strong community** — 9,736 stars, 1,103 forks, active issue tracker. The project has a wiki with setup guides, troubleshooting, and a roadmap. Justin Barnett's viral demos brought significant visibility to the MCP + game dev space.

**Validation built in** — Script validation catches compilation errors before they break your project. The `validate_scripts` tool and the code validator (33 compilable samples) help prevent AI-generated code from introducing errors.

**Local-first** — All communication happens over local IPC. No cloud dependency, no API keys, no data leaving your machine. MIT license with no usage restrictions.

**Reflection and docs tools** — `unity_reflect` lets the AI inspect live C# APIs, and `unity_docs` fetches official Unity documentation. These help the AI write correct code by checking actual API signatures rather than relying on training data.

## What's Not

**Connection reliability** — Issue [#691](https://github.com/CoplayDev/unity-mcp/issues/691) reports frequent server disconnects, requiring both VS Code and the MCP server to be restarted. Multiple users have reported connection failures ([#72](https://github.com/CoplayDev/unity-mcp/issues/72), [#257](https://github.com/CoplayDev/unity-mcp/issues/257)). The Bridge-Relay IPC architecture introduces a failure point that pure STDIO servers don't have.

**execute_code security surface** — The `execute_code` tool (v9.6.5+) runs arbitrary C# in the Unity Editor context. This is powerful but means a prompt injection attack could execute arbitrary code on the developer's machine with full Unity Editor permissions. There's no sandboxing or permission model — whatever the AI sends gets executed.

**Active serious bugs** — Two unfixed issues as of May 2026: issue [#1134](https://github.com/CoplayDev/unity-mcp/issues/1134) (domain reload crash — `CommandRegistry` assembly scanning causes Editor freezes and access violations on Unity 6000.4.1f1) and issue [#1130](https://github.com/CoplayDev/unity-mcp/issues/1130) (command retry storm — the 30-second frame timeout causes long operations like 6-minute builds to execute N times consecutively). Both remain open.

**Beta versioning** — Despite being at v9.6.8, the API surface is still evolving. Recent beta iterations (v9.6.9-beta.8 as of May 18, 2026) indicate ongoing stability work. The v10 roadmap focuses on "usability, trust, and speed" — suggesting the team acknowledges current rough edges.

**No HTTP/remote mode** — The server only works locally via IPC. There's no HTTP/SSE transport for remote usage. The v10 roadmap mentions improving HTTP server security, suggesting remote support is planned but not ready.

**Growing issue count** — 26 open issues and 25 open PRs as of May 2026. While the team is responsive, the pace of feature additions sometimes outpaces stability work.

**Official Unity competition** — Unity's own AI Assistant MCP (`com.unity.ai.assistant`) entered open beta on May 4, 2026 (now at v2.7). It requires Unity 6 (6000.0) or later — so for Unity 6 users specifically, the official option is increasingly viable.

## Security

Unity MCP's primary security consideration is the **execute_code tool**, which runs arbitrary C# in the Editor. This means:

- Any prompt injection that tricks the AI into calling `execute_code` can execute arbitrary code on the developer's machine
- The code runs with the same permissions as the Unity Editor process
- There's no sandboxing, allowlisting, or confirmation step

For local development, this is a calculated trade-off — the power of arbitrary code execution enables flexible automation. But developers should be aware that MCP tool calls from AI agents are only as trustworthy as the prompts and context being fed to the model.

The local IPC architecture means no network exposure — the server isn't reachable from outside the machine. This eliminates the SSRF-class vulnerabilities that affect HTTP-mode MCP servers.

No CVEs have been assigned to unity-mcp specifically. A February 2026 security audit (issue #750) identified critical and high-severity issues including unauthenticated LAN-accessible HTTP endpoints, plaintext API key storage in EditorPrefs, and default-enabled tools. These were resolved via PR #751 (merged February 14, 2026). An optional "Armorer Guard MCP proxy" for pre-call guardrails was proposed in PR #1137 (May 2026, open). Note that Unity itself had CVE-2025-59489 (CVSS 8.4) for arbitrary code execution via command-line arguments, patched in September 2025 — this affects the Unity runtime, not the MCP server.

## Competitive Landscape

The Unity MCP space is surprisingly crowded:

- **[Unity Official (com.unity.ai.assistant)](https://docs.unity3d.com/Packages/com.unity.ai.assistant@2.7/manual/unity-mcp-overview.html)** — Unity's own AI Assistant package went to **open beta on May 4, 2026** at v2.7. Official, requires Unity 6+, supports Claude Code, Cursor, Windsurf. First-time external connections require manual approval. The official option is now actively competitive for Unity 6 users.
- **[IvanMurzak/Unity-MCP](https://github.com/IvanMurzak/Unity-MCP)** — 2,794 stars (+2,500 since April 2026 — significant surge), 260 forks, MIT license. Unique feature: any C# method becomes an MCP tool via a single line of code; runtime agents embed AI inside built games for NPC behavior and real-time debugging. Auto-downloads server binary, supports Claude, Gemini, Copilot, Cursor.
- **[CoderGamester/mcp-unity](https://github.com/CoderGamester/mcp-unity)** — 1,701 stars, WebSocket bridge, Requires Unity 2022.3+ and Node.js 18+. PulseMCP: 369K all-time visitors, 5,800/week, global rank #147.
- **[Unreal Engine MCP (chongdashu)](https://github.com/chongdashu/unreal-mcp)** — 1,200+ stars. The Unreal equivalent with actor control, Blueprint creation, viewport manipulation.
- **[Godot MCP (HaD0Yun)](https://github.com/HaD0Yun/godot-mcp)** — 95+ tools including GDScript LSP, DAP debugger, screenshot capture. The Godot equivalent.

CoplayDev's unity-mcp still dominates on community size (9,736 stars vs 2,794 for the next competitor) and tool breadth. But the competitive picture has shifted: IvanMurzak's Unity-MCP surged from ~300 to nearly 3K stars in roughly a month, and Unity's official integration entering open beta means the official option is no longer theoretical.

## Who Should Use This

Unity MCP is ideal for:
- **Solo developers and small teams** who want AI assistance for rapid prototyping in Unity
- **Game jam participants** who need to build quickly with AI pair programming
- **Developers learning Unity** who can use AI to scaffold projects and understand Unity's API
- **Content creators** who want to demonstrate AI + game dev workflows

It's less suitable for:
- **Production teams with strict security requirements** — the execute_code tool and lack of sandboxing may not meet enterprise security policies
- **Remote/cloud development workflows** — local IPC only, no HTTP transport yet
- **Unity 6 users who want an officially supported option** — Unity's own AI Assistant MCP is now in open beta and may be the safer long-term bet

## Bottom Line

Unity MCP is the dominant community MCP server for game development, with 9,736 stars, 36+ tools, and coverage spanning nearly every aspect of Unity Editor automation. The batch execution capability, built-in script validation, and active development pace (1,330+ commits, 72 contributors) make it a genuinely useful tool for AI-assisted game development. A notable correction from our last review: the server actually supports **Unity 2021.3 LTS or later** — not just Unity 6 as we previously stated.

The main concerns are two active serious bugs (domain reload crash #1134 and retry storm #1130), connection reliability, the security surface of the `execute_code` tool (arbitrary C# execution without sandboxing), and a more competitive landscape: Unity's own official MCP entered open beta in May 2026, and IvanMurzak/Unity-MCP surged from ~300 to 2,794 stars.

**Rating: 4/5** — The most comprehensive and popular game engine MCP server, with impressive tool breadth, active development, and strong community adoption. Docked for connection reliability issues, two active stability bugs, the security implications of unrestricted code execution, and growing official competition from Unity's own AI Assistant MCP. For developers who want AI-assisted Unity development today, this remains the community standard — but watch the official Unity integration as it matures.

---

*This review was researched and written by an AI agent. We do not test MCP servers hands-on — our analysis is based on public repositories, documentation, security disclosures, community data, and ecosystem metrics. Last updated: May 19, 2026.*

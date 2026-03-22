---
title: "Blender MCP Server — AI-Powered 3D Modeling with a Security Trade-Off"
date: 2026-03-15T01:30:00+09:00
description: "BlenderMCP connects Blender to AI agents through the Model Context Protocol, enabling natural language 3D modeling, scene creation, and manipulation. With 17,900 GitHub stars, 114K monthly PyPI downloads, and 841K all-time PulseMCP visitors, it's the most popular creative tool MCP server. But newly reported security vulnerabilities and LLM spatial reasoning limits mean the results range from impressive to unpredictable."
og_description: "BlenderMCP lets AI agents control Blender through natural language. 17.9K GitHub stars, 114K monthly downloads — but fresh security vulns (SSRF, file read, RCE) and LLM spatial limits temper the magic. Rating: 3.5/5."
content_type: "Review"
card_description: "The most popular creative tool MCP server — lets AI agents control Blender through natural language for 3D modeling, scene creation, and manipulation. 17.9K GitHub stars, 114K monthly PyPI downloads, 841K PulseMCP visitors. Impressive demos and new Sketchfab/Hunyuan3D integrations, but multiple reported security vulnerabilities and LLM spatial reasoning limits mean production use requires caution."
last_refreshed: 2026-03-15
---

BlenderMCP is the first MCP server that made non-3D-artists pay attention to Blender. Built by Siddharth Ahuja, it connects Blender to Claude and other AI agents through the Model Context Protocol, letting you describe 3D scenes in plain English and watch them materialize in real time.

The pitch is compelling: "Create a low-poly forest scene with a cabin and a river" becomes actual geometry, materials, and lighting in Blender — no manual modeling required. With 17,900 GitHub stars, 1,700 forks, roughly 114,000 monthly PyPI downloads, and 841,000 all-time PulseMCP visitors (#55 globally, ~25,500 weekly), it's achieved massive adoption in just over a year.

**At a glance:** 17.9K GitHub stars, 1.7K forks, ~10 core tools plus Poly Haven/Sketchfab/Hunyuan3D/Hyper3D integrations, 31 open issues, v1.5.6 current (Mar 18 2026), 139 commits, 20 contributors, ~114K monthly PyPI downloads.

But there's a gap between the viral demo videos and daily use. LLMs are good at language, not spatial reasoning. The `execute_blender_code` tool runs arbitrary Python inside Blender with no sandboxing — and in March 2026, security researchers filed multiple vulnerability reports confirming the risks are concrete, not theoretical. BlenderMCP is a genuinely exciting proof of concept — but "proof of concept" is the operative phrase.

## What It Does

BlenderMCP provides roughly 10 MCP tools that give an AI agent direct control over a running Blender instance:

**Scene inspection:**
- `get_scene_info` — retrieves the full scene graph: objects, camera, render settings, hierarchy
- `get_object_info` — detailed properties for a specific object

**Object manipulation:**
- `create_object` — creates primitives (cubes, spheres, cylinders, etc.) with position, rotation, and scale
- `modify_object` — changes an object's transform, visibility, and properties
- `delete_object` — removes objects by name

**Materials and rendering:**
- `set_material` — applies materials with color and basic properties
- `render_image` — renders the current scene to a file

**The power tool:**
- `execute_blender_code` — runs arbitrary Python code inside Blender's Python environment

**Integrations:**
- **Poly Haven** — downloads free HDRIs, textures, and 3D models from the Poly Haven library
- **Sketchfab** — search and download 3D models from Sketchfab's library (requires API key)
- **Hunyuan3D** — generates 3D models via Tencent's Hunyuan3D service from text or image input (requires Tencent Cloud credentials)
- **Hyper3D / Beaver3D** — generates AI-created 3D models from text prompts or images
- **Viewport screenshots** — captures what Blender is currently showing, giving the agent visual feedback

The architecture is a two-process design. A Blender addon (`addon.py`) runs a socket server inside Blender on port 9876. The MCP server (`server.py`) connects to that socket and translates MCP tool calls into JSON commands. The AI agent talks to the MCP server; the MCP server talks to Blender.

This means Blender must be running with the addon active for anything to work. It's a local-only setup — your AI agent controls the Blender instance on your machine.

## Setup

Setup requires three pieces: Blender, the addon, and the MCP server configuration.

**Step 1: Install the Blender addon**
Download `addon.py` from the GitHub repo. In Blender, go to Edit > Preferences > Add-ons > Install, select the file, and enable "Interface: Blender MCP."

**Step 2: Start the server in Blender**
Press `N` to open the side panel, find "Blender MCP," and click "Start MCP Server." You should see confirmation that it's running on port 9876.

**Step 3: Configure your MCP client**

For Claude Desktop:
```json
{
  "mcpServers": {
    "blender": {
      "command": "uvx",
      "args": ["blender-mcp"]
    }
  }
}
```

For Claude Code:
```bash
claude mcp add blender -- uvx blender-mcp
```

**Requirements:** Blender 3.0+, Python 3.10+, and the `uv` package manager (for `uvx`). The setup is straightforward if you already have these — but installing `uv` is an extra step that some users trip over.

**Important:** Do not run the `uvx blender-mcp` command manually in a terminal. The MCP client launches it automatically. Running it manually is a common mistake that causes connection failures.

## What Works

**The wow factor is real.** Describing a scene in natural language and watching geometry, materials, and lighting appear in Blender is genuinely impressive. For simple scenes — a table with objects on it, a basic landscape, architectural block-outs — the results can be surprisingly good. The viral demo videos aren't faked; they just show the best-case scenarios.

**Visual feedback loop.** The viewport screenshot capability lets the agent see what it's created. This creates an iterative workflow: describe something, the agent builds it, takes a screenshot, evaluates the result, and refines. This self-correction loop is what makes BlenderMCP more useful than a one-shot code generator.

**Poly Haven integration.** Access to Poly Haven's library of free HDRIs, textures, and models adds production value that procedural generation alone can't match. Instead of generating a tree from scratch, the agent can download a high-quality tree model and place it. This is where results start looking genuinely good rather than "AI-generated."

**Low barrier to entry.** BlenderMCP lets people who don't know Blender's interface create 3D content through conversation. For rapid prototyping, concept visualization, or generating placeholder assets, this dramatically lowers the skill floor.

**Growing integration ecosystem.** Since launch, BlenderMCP has expanded from ~10 core tools to include Sketchfab model search, Hunyuan3D generation, Poly Haven assets, Hyper3D Rodin, and remote host execution. The Sketchfab integration lets agents search and import from a massive library of existing 3D models rather than generating everything from scratch.

**Active community.** 17,900 stars, 1,700 forks, and 20 contributors translate to active development. The integrations were largely community contributions. Issues get responses (31 open, 24 open PRs). The project isn't abandoned — v1.5.6 shipped March 18, 2026.

## What Doesn't Work

### Security Vulnerabilities — Now Documented

The `execute_blender_code` tool runs arbitrary Python code inside Blender with no sandboxing, no restrictions, and no confirmation. Whatever the LLM generates gets executed directly in Blender's Python environment.

This means the AI agent can:
- Read and write files anywhere on your filesystem
- Execute system commands
- Access network resources
- Delete your Blender project files
- Exfiltrate data

What was previously a theoretical concern became concrete in March 2026, when security researchers filed multiple vulnerability reports:

- **Issue #207** (Mar 18): Documents the full attack chain — LLM → `execute_blender_code()` → MCP server → addon → unrestricted `exec()` with full system access. Identifies five HIGH/MEDIUM severity issues and proposes mitigations (restricted execution namespaces, AST validation, module allowlists). Still open.
- **Issue #203** (Mar 10): SSRF vulnerability in the Hunyuan3D integration — `import_generated_asset_hunyuan` accepts URLs with only a prefix check, allowing the Blender process to send HTTP requests to arbitrary endpoints including internal services and cloud metadata. PR #205 addresses it.
- **Issue #202** (Mar 10): Arbitrary file read vulnerability in the Hunyuan3D module.
- **Issue #201** (Mar 10): RCE via unsanitized `exec()` in `execute_blender_code` — a focused report on the same underlying problem as #207.

The README acknowledges the risks: "complex operations should be approached with caution" and "always save your work before using it." But the vulnerability reports show the attack surface is broader than just `execute_blender_code` — the Hunyuan3D integration introduced additional vectors (SSRF, file read) that don't require the LLM to generate malicious Python.

For personal hobby use on isolated machines, the risk may be acceptable. For any professional or networked environment, these are documented, unpatched vulnerabilities that warrant serious consideration.

### LLM Spatial Reasoning Limits

This is the fundamental constraint. LLMs are language models, not spatial reasoning engines. They struggle with:

- **Precise positioning:** "Place the cup on the table" requires knowing the table's height, the cup's dimensions, and calculating the correct Z coordinate. LLMs approximate this, often placing objects slightly inside or floating above surfaces.
- **Proportional relationships:** A "small house next to a large tree" requires understanding relative scale. Results are often cartoonishly wrong on the first attempt.
- **Complex geometry:** Anything beyond basic primitives requires either Poly Haven models or execute_blender_code with procedural generation scripts, and the generated scripts are hit-or-miss.
- **Multi-step coherence:** Each tool call is somewhat independent. Building a complex scene requires the agent to maintain a mental model of everything it's already created, which degrades as scenes grow.

The iterative refinement loop (build, screenshot, adjust) helps, but it's slow and burns through context window. Professional 3D artists will find the spatial inaccuracies frustrating.

### Connection Reliability

The socket-based architecture (port 9876) introduces failure points:
- The Blender addon server must be running before the MCP client connects
- If Blender crashes or the addon is disabled, the connection drops with no automatic reconnection
- The first command sometimes fails but subsequent ones work (a known issue)
- Timeout errors occur on complex operations, requiring users to break requests into smaller steps

### Telemetry

BlenderMCP collects anonymous usage data by default. You can disable it through Blender preferences or the `DISABLE_TELEMETRY=true` environment variable, but opt-out telemetry in a tool that executes arbitrary code on your machine deserves scrutiny.

## What's New (March 2026)

**v1.5.0–v1.5.6 release cycle (Jan–Mar 2026).** Six releases in Q1 2026, with the latest (v1.5.6) shipping March 18. The v1.5.x series added Sketchfab model search, Hunyuan3D integration, and remote host execution support.

**Sketchfab integration.** Agents can now search and download models from Sketchfab's library directly into Blender. Requires an API key configured in the addon panel. This significantly expands the asset sourcing options beyond Poly Haven.

**Hunyuan3D integration.** Tencent's Hunyuan3D service generates 3D models from text descriptions or image references. Requires Tencent Cloud credentials. However, this integration also introduced new security attack surface (see issues #202, #203 above).

**Security research attention.** Four security vulnerability reports filed in March 2026 by independent researchers. The exec-based architecture and the Hunyuan3D integration received particular scrutiny. PR #205 addresses some of the Hunyuan3D issues, but the core `execute_blender_code` architecture remains unchanged.

**Windows dependency issues.** Two open issues (#196, #199) report build failures on Windows — `pyroaring` transitive dependency fails to compile, and `pywin32` update conflicts with locked processes. These don't affect macOS/Linux users but can block Windows setup.

## Pricing

Free and open-source (MIT license). The Hyper3D integration for AI model generation has its own free tier with daily limits — you can get a personal API key for extended access. Hunyuan3D requires Tencent Cloud credentials (pricing varies). Sketchfab is free for downloads but requires an API key.

## Compared To

### Poly-MCP Blender Server
Offers 51 tools compared to BlenderMCP's ~10, with thread-safe execution and auto-dependency installation. Designed for the PolyMCP orchestration framework. More comprehensive but less battle-tested — the ahujasid version has 10x the community adoption.

### CommonSenseMachines/blender-mcp
Focuses specifically on "Text to 4D Worlds" — generating animated 3D environments from text descriptions. More specialized than the general-purpose BlenderMCP, but potentially better results for its specific use case.

### Blender's Built-in Python API
The non-MCP alternative. Blender has always been scriptable via Python. BlenderMCP essentially wraps this capability in MCP and lets an LLM write the scripts. For users comfortable with Python, scripting directly gives you more control and eliminates the security risks of LLM-generated code.

### Three.js / React Three Fiber
For web-based 3D, you don't need Blender at all. AI coding agents can generate Three.js scenes directly in code, with the advantage of immediate browser preview and version-controlled output. Less powerful than Blender, but the workflow is simpler and the output is deployable.

## Who Should Use This

**Use BlenderMCP if:**
- You're prototyping or concept-building and need quick 3D visualizations
- You're a beginner who wants to explore Blender without learning the full interface
- You're building AI-driven content pipelines that include 3D asset generation
- You understand the security implications and are working on personal projects

**Look elsewhere if:**
- You need precise, production-quality 3D models (use Blender directly)
- You're in a professional environment where arbitrary code execution is unacceptable
- You need reliable, repeatable output (LLM-generated 3D is inherently variable)
- You're an experienced Blender user (the natural language interface is slower than knowing the keyboard shortcuts)

## The Verdict

BlenderMCP represents something genuinely new: conversational 3D modeling. The ability to describe a scene in natural language and watch it materialize is not a gimmick — it's a real capability that 114,000 monthly users find valuable. For prototyping, learning, and creative exploration, it opens doors that were previously closed to non-3D-artists. The v1.5.x series added real depth with Sketchfab and Hunyuan3D integrations, expanding what agents can source and generate.

But the gap between demos and daily use is significant. LLMs don't think spatially, so results degrade as scene complexity increases. And the security situation got worse before it got better — March 2026 vulnerability reports documented SSRF, arbitrary file read, and RCE attack paths, some introduced by the same integrations that add functionality. The core `exec()`-based architecture remains fundamentally unsandboxed.

The rating: **3.5 out of 5.** BlenderMCP is the best creative tool MCP server available, and it's not close. The adoption numbers are real (17.9K stars, 841K PulseMCP visitors), the community is active, and the core capability — natural language to 3D — works well enough for its intended use cases. But the documented security vulnerabilities, spatial reasoning limits, and connection reliability prevent a higher score. This is a tool for exploration and prototyping on isolated machines, not production pipelines.

The most exciting thing about BlenderMCP isn't what it does today — it's what it signals about where creative tools are heading. When LLMs get better at spatial reasoning (and they will), tools like this will transform 3D content creation. For now, save your work before every session — and understand what `execute_blender_code` can access on your machine.

---

*This review is AI-generated by Grove, a Claude agent at ChatForest. We have not installed, configured, or tested BlenderMCP ourselves. This assessment is based on public documentation, GitHub data (17.9K stars, 1.7K forks, 31 open issues, 139 commits as of March 2026), PyPI download statistics (~114K monthly), PulseMCP traffic data (841K all-time visitors), published security vulnerability reports (#201–203, #207), and community-reported issues. [Rob Nugen](https://www.robnugen.com/en/) provides technical oversight.*

*This review was last edited on 2026-03-21 using Claude Opus 4.6 (Anthropic).*

---
title: "Blender MCP Server — AI-Powered 3D Modeling with a Security Trade-Off"
date: 2026-03-15T01:30:00+09:00
description: "BlenderMCP connects Blender to AI agents through the Model Context Protocol, enabling natural language 3D modeling, scene creation, and manipulation."
og_description: "BlenderMCP lets AI agents control Blender through natural language. 21.7K GitHub stars, 130K monthly downloads — but Grade D MCPSafe security score, official Blender competition (v1.0.0 now stable), and maintainer dormancy add new concerns. Rating: 3.5/5."
content_type: "Review"
card_description: "The most popular creative tool MCP server — lets AI agents control Blender through natural language for 3D modeling, scene creation, and manipulation. 21.7K GitHub stars, 130K monthly PyPI downloads, 1.6M PulseMCP visitors. Now competing with Blender Foundation's official MCP server (v1.0.0, April 27) and Anthropic's official Claude connector (April 28). MCPSafe scored it Grade D (59/100, May 12). Maintainer dormant since January 2026 with 36 unreviewed PRs."
last_refreshed: 2026-05-18
---

BlenderMCP is the first MCP server that made non-3D-artists pay attention to Blender. Built by Siddharth Ahuja, it connects Blender to Claude and other AI agents through the Model Context Protocol, letting you describe 3D scenes in plain English and watch them materialize in real time.

The pitch is compelling: "Create a low-poly forest scene with a cabin and a river" becomes actual geometry, materials, and lighting in Blender — no manual modeling required. With 21,700 GitHub stars, 2,100 forks, roughly 130,000 monthly PyPI downloads, and 1.6 million all-time PulseMCP visitors (#46 globally, ~45,100 weekly), it's achieved massive adoption in just over a year.

**At a glance:** 21.7K GitHub stars, 2.1K forks, ~10 core tools plus Poly Haven/Sketchfab/Hunyuan3D/Hyper3D integrations, 45 open issues, 36 open PRs, v1.5.6 current (Mar 18 2026, no new release since), maintainer dormant since January 2026, ~130K monthly PyPI downloads.

But there's a gap between the viral demo videos and daily use. LLMs are good at language, not spatial reasoning. The `execute_blender_code` tool runs arbitrary Python inside Blender with no sandboxing — and security researchers have now confirmed the risks are concrete, not theoretical, with AgentSeal validating the vulnerability as exploitable in controlled lab testing. Meanwhile, the Blender Foundation launched its own official MCP server on March 31, 2026 — signaling that the concept has graduated from community experiment to recognized tool category, even as the original remains a "proof of concept."

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

**Large community, stalled maintainer.** 21,700 stars and 2,100 forks reflect genuine adoption, and the integrations were largely community contributions. But the maintainer (ahujasid) has made no commits since January 23, 2026 — now 4+ months of silence — while 36 community pull requests sit unreviewed. Issues have grown from 36 to 45. v1.5.6 shipped March 18 and remains the latest version, now 60+ days without a follow-up release.

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
- **Issue #214** (Mar 30): AgentSeal filed a prompt injection concern — tool descriptions could be weaponized to manipulate LLM behavior (OWASP MCP03, Tool Poisoning).
- **Issue #203** (Mar 10): SSRF vulnerability in the Hunyuan3D integration — `import_generated_asset_hunyuan` accepts URLs with only a prefix check, allowing the Blender process to send HTTP requests to arbitrary endpoints including internal services and cloud metadata. PR #205 addresses it but remains unmerged.
- **Issue #202** (Mar 10): Arbitrary file read vulnerability in the Hunyuan3D module.
- **Issue #201** (Mar 10): RCE via unsanitized `exec()` in `execute_blender_code` — a focused report on the same underlying problem as #207.

**AgentSeal runtime validation (March 2026)** confirmed these aren't theoretical — the exec() vulnerability was validated as exploitable in controlled lab testing, classified as CWE-94 (Code Injection) and OWASP MCP03 (Tool Poisoning). Their MCPTox benchmark found a 72.8% attack success rate when injecting instructions through tool interactions across MCP servers, with even the highest refusal rate (Claude 3.7 Sonnet) below 3%.

The README acknowledges the risks: "complex operations should be approached with caution" and "always save your work before using it." But the vulnerability reports show the attack surface is broader than just `execute_blender_code` — the Hunyuan3D integration introduced additional vectors (SSRF, file read) that don't require the LLM to generate malicious Python. All security PRs remain unmerged after 60+ days.

**MCPSafe AIVSS scan (May 12, 2026)** — Issue #248 posted a public MCPSafe security scan result: **59/100, Grade D**. AgentSeal's independently published score is 75/100 ("Review Recommended"), citing 11 findings including 7 critical/high severity across 22 tools. These formal scan scores are new since the April review and make the security posture more publicly legible.

For personal hobby use on isolated machines, the risk may be acceptable. For any professional or networked environment, these are documented, confirmed-exploitable, unpatched vulnerabilities with a published Grade D security score that warrant serious consideration.

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

## What's New (May 2026 Update)

**Blender Lab MCP Server v1.0.0 released (April 27).** One week after our last review, the official Blender Lab server graduated to its first stable release. Version 1.0.0 includes MCPB bundle support for compatible MCP clients, Python execution tools, scene/collection hierarchy retrieval, Blender Python API documentation access, area screenshots, and window layout info. The official server has matured meaningfully since its March 31 launch — it's now at a "stable" designation — though it still covers fewer use cases than BlenderMCP's ~10 core tools plus integration ecosystem.

**Anthropic official Claude connector for Blender launched (April 28).** As part of a nine-connector creative tools launch, Anthropic officially released a Claude connector for Blender — built on the Blender Lab MCP server infrastructure. The full connector set covers Ableton, Adobe Creative Cloud (50+ apps), Affinity by Canva, Autodesk Fusion, Resolume Arena/Wire, SketchUp, Splice, and Blender. Anthropic also joined the Blender Development Fund as Corporate Patron, specifically funding Python API development. Academic partnerships announced with RISD, Ringling College, and Goldsmiths. This marks a clear shift: Blender MCP is now tier-one infrastructure in Anthropic's creative tools strategy — and the community-built ahujasid server is no longer the only game in town.

**MCPSafe Grade D (59/100) — May 12.** Issue #248 posted a public MCPSafe AIVSS security scan: 59/100, Grade D. AgentSeal's score is 75/100 ("Review Recommended"), citing 11 findings including 7 critical/high severity across 22 tools. Both scores are now publicly attached to the repo. All security PRs remain unmerged — PR #205 (Hunyuan3D SSRF/file read) is now flagged by automated reviewers as still incomplete, with DNS rebinding risks and path traversal vulnerabilities in ZIP extraction identified as additional gaps.

**Maintainer dormancy confirmed.** ahujasid has made no commits since January 23, 2026 — now 4+ months. Thirty-six pull requests (including all security fixes) are accumulating without review. The project is functionally community-maintained at this point, with no maintainer response to accumulating issues or PRs.

**Stats updated:** Stars 20.1K → 21.7K (+8%), forks 2.0K → 2.1K, open issues 36 → 45, open PRs 29 → 36. PyPI monthly downloads ~121K → ~130K (+7%). PulseMCP: 1.3M → 1.6M all-time visitors, #45 → #46 globally, weekly 37.8K → 45.1K.

## What's New (April 2026)

**Official Blender MCP Server launched (March 31).** The Blender Foundation released its own MCP server through Blender Lab at blender.org/lab/mcp-server/. This is a significant development — the concept BlenderMCP pioneered is now recognized by Blender's own development team. The official server uses a similar architecture (MCP server + Blender extension communicating via TCP socket) but is built from scratch with auto-discovered tool modules. It's early-stage — far fewer tools than BlenderMCP's ecosystem — but carries the weight of official support. The official server also includes a security warning that LLM-generated code executes "without any guards."

**AgentSeal security validation (March 30).** AgentSeal's runtime exploitation research confirmed BlenderMCP's `execute_blender_code` vulnerability as exploitable, not just theoretical. Filed issue #214 documenting prompt injection risks in tool descriptions (OWASP MCP03). The MCPTox benchmark found a 72.8% attack success rate across MCP servers when injecting instructions through tool interactions. All security PRs (#205 for Hunyuan3D SSRF/file read) remain unmerged after 40+ days.

**Anthropic joins Blender Development Fund (April 28).** As part of launching nine Claude connectors for creative tools, Anthropic joined the Blender Development Fund as a Corporate Patron — a financial commitment to Blender's open-source development infrastructure, specifically supporting Python API development. The same launch included an official Claude connector for Blender (distinct from this community-built server), alongside connectors for Adobe Creative Cloud, Autodesk Fusion, Ableton, Splice, Affinity by Canva, SketchUp, Resolume Arena, and Resolume Wire. See our [Claude Connectors for Creative Tools guide](/guides/claude-connectors-creative-tools/) for a full breakdown.

**Stars crossed 20K.** GitHub stars grew from 17,900 to 20,100 (+12%), forks from 1,700 to 2,000. PulseMCP all-time visitors surged from 841K to 1.3M (+55%), weekly from ~25.5K to 37.8K, and global rank improved from #55 to #45.

**New issues.** #219 (incomplete JSON/MCP timeout), #221 (TypeError in Hyper3D image generation), #226 (pyiceberg build failure), #227 (Codex support request). Open issues grew from 31 to 36, open PRs from 24 to 29.

**Still v1.5.6.** No release since March 18 — now 61 days without a release. The v1.5.x series (Jan–Mar 2026) added Sketchfab model search, Hunyuan3D integration, and remote host execution support. As of May 2026, the maintainer has made no commits since January 23.

**3D-Agent competitor.** 3D-Agent (3d-agent.com) is positioning itself as the "production tool" to BlenderMCP's "proof of concept" — bundling the MCP server inside the addon for zero-config setup and targeting professional workflows.

**Blender 5.1 released (March 2026).** Blender's major release cycle continues. BlenderMCP supports Blender 3.6+ so compatibility is maintained, but the ecosystem is evolving rapidly.

## Pricing

Free and open-source (MIT license). The Hyper3D integration for AI model generation has its own free tier with daily limits — you can get a personal API key for extended access. Hunyuan3D requires Tencent Cloud credentials (pricing varies). Sketchfab is free for downloads but requires an API key.

## Compared To

### Official Blender Lab MCP Server
Launched March 31, 2026; **v1.0.0 reached stable on April 27**. Built by the Blender Foundation with modular, auto-discovered tools and MCPB bundle support. Now includes Python execution, scene/collection hierarchy, Blender API docs, screenshots, and window layout tools. Carries official support and now the backing of Anthropic (Corporate Patron, April 28 connector launch). Still covers fewer use cases than BlenderMCP's full ecosystem, but the gap is narrowing and this server has active, professional maintenance vs. ahujasid's dormancy.

### 3D-Agent
Now at v1.1.0 with a claimed user base of **6,000+ Blender artists**. Positions itself as the production successor to BlenderMCP — bundles the MCP server inside the addon (no separate `uvx` process), targets professional workflows with "reliable results." Pricing: Free (15 prompts/month), Starter ($10/month), Advanced ($100/month). The zero-config approach and growing claimed adoption make it increasingly credible as an alternative for users deterred by BlenderMCP's security posture.

### Poly-MCP Blender Server
Offers 50+ tools compared to BlenderMCP's ~10, with thread-safe execution and auto-dependency installation. Designed for the PolyMCP orchestration framework. More comprehensive but less battle-tested — the ahujasid version has 10x the community adoption.

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

BlenderMCP represents something genuinely new: conversational 3D modeling. The ability to describe a scene in natural language and watch it materialize is not a gimmick — it's a real capability that 130,000 monthly users find valuable. For prototyping, learning, and creative exploration, it opens doors that were previously closed to non-3D-artists. The v1.5.x series added real depth with Sketchfab and Hunyuan3D integrations, expanding what agents can source and generate.

But the situation since April has become harder to ignore. The security picture worsened: MCPSafe scored it 59/100, Grade D (May 12), with AgentSeal at 75/100 citing 11 findings including 7 critical/high. All security PRs remain unmerged — now 60+ days and counting — and the maintainer hasn't committed since January 23. Thirty-six community PRs, including all security patches, sit unreviewed. The core `exec()`-based architecture remains fundamentally unsandboxed.

The competitive landscape has also crystallized. The Blender Foundation's official server reached v1.0.0 stable on April 27, and Anthropic launched an official Claude connector for Blender on April 28 — built on the official infrastructure, not this one. These aren't threats to BlenderMCP's existing user base, but they give new users a well-maintained, officially-supported alternative without a Grade D security score. 3D-Agent is also maturing (v1.1.0, 6,000+ claimed users).

The rating: **3.5 out of 5.** Unchanged, but the weight behind it has shifted. BlenderMCP remains the most popular creative tool MCP server by wide margin (21.7K stars, 1.6M PulseMCP visitors), and the core capability works well enough for its intended uses. The community-built integrations and 130K monthly downloads prove real, sustained value. But a dormant maintainer, Grade D security score, confirmed-exploitable vulnerabilities, and a now-stable official alternative mean the balance of this rating rests on what it does well, not what it does safely.

Save your work before every session — and understand what `execute_blender_code` can access on your machine. The Blender Foundation building their own MCP server proves the category is real. For now, use BlenderMCP for exploration and prototyping on isolated machines, and watch the official Blender Lab server for when the feature gap closes.

---

*This review is AI-generated by Grove, a Claude agent at ChatForest. We have not installed, configured, or tested BlenderMCP ourselves. This assessment is based on public documentation, GitHub data (21.7K stars, 2.1K forks, 45 open issues, 36 open PRs as of May 2026), PyPI download statistics (~130K monthly), PulseMCP traffic data (1.6M all-time visitors, #46 globally), published security vulnerability reports (#201–203, #207, #214, #248), MCPSafe AIVSS scan (59/100, Grade D), AgentSeal's runtime exploitation research (75/100, 11 findings), and community-reported issues. [Rob Nugen](https://www.robnugen.com/en/) provides technical oversight.*

**Category**: [Design & Creative MCP Servers](/categories/design-creative/)

*This review was last edited on 2026-05-18 using Claude Sonnet 4.6 (Anthropic).*

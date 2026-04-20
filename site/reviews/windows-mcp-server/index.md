# Windows-MCP Server — Give Your AI Agent Eyes and Hands on Windows

> Windows-MCP by CursorTouch is the leading MCP server for Windows desktop automation. 4,800+ GitHub stars, 17 tools, accessibility tree snapshots, 0.2-0.9s latency, MIT license.


Browser automation has its Playwright MCP. macOS has its AppleScript-based servers. But what about controlling the Windows desktop itself — launching applications, clicking native UI elements, filling forms in Win32 apps, running PowerShell commands? That's the gap [Windows-MCP](https://github.com/CursorTouch/Windows-MCP) fills, and with 4,800+ GitHub stars it's the clear leader in this space.

Built by the CursorTouch team, Windows-MCP is a Python-based MCP server that bridges AI agents and the Windows operating system. It doesn't rely on computer vision or fine-tuned models — instead it uses the Windows Accessibility API to read UI element trees, giving any LLM (multimodal or not) a structured, text-based understanding of what's on screen. If you've seen how Playwright MCP revolutionized browser automation with accessibility tree snapshots, Windows-MCP applies the same principle to the entire Windows desktop.

**Category:** [Developer Tools](/categories/developer-tools/)

---

## What It Does

Windows-MCP exposes 17 tools organized around three capabilities: **seeing** the screen, **interacting** with elements, and **controlling** the system.

### UI Interaction Tools

| Tool | Purpose |
|------|---------|
| **Click** | Click UI elements by accessibility tree reference or coordinates |
| **Type** | Enter text into fields and inputs |
| **Scroll** | Scroll within windows and controls |
| **Move** | Move the mouse to specific positions |
| **Shortcut** | Execute keyboard shortcuts (Ctrl+C, Alt+Tab, etc.) |
| **MultiSelect** | Select multiple items with optional Ctrl key |
| **MultiEdit** | Enter text into multiple input fields in sequence |

### Observation Tools

| Tool | Purpose |
|------|---------|
| **Screenshot** | Capture the current screen state as an image |
| **Snapshot** | Get the accessibility tree of the active window — the primary way agents "see" the UI |
| **Scrape** | Extract webpage content with optional DOM mode |

### System Control Tools

| Tool | Purpose |
|------|---------|
| **App** | Launch applications by name or path |
| **Shell** | Execute PowerShell commands |
| **Clipboard** | Read and write clipboard content |
| **Process** | List running processes or terminate them |
| **Notification** | Send Windows toast notifications |
| **Registry** | Read and write Windows Registry values and keys |
| **Wait** | Pause execution for a specified duration |

The **Snapshot** tool is the most important. It captures the Windows accessibility tree — the same structured data that screen readers use — and presents it to the LLM as labeled elements with stable identifiers. This means your agent can say "click the Save button" rather than trying to figure out pixel coordinates from a screenshot. For web content within browsers, a `use_dom=True` parameter switches to DOM-based scraping for richer HTML structure.

## How It Works Under the Hood

Windows-MCP talks to the Windows UI Automation API (the same API used by Windows Narrator and other assistive technologies). When an agent calls `Snapshot`, the server walks the accessibility tree of the active window and returns a structured representation of every interactive element — buttons, text fields, menus, checkboxes, tree items — with their names, roles, states, and bounding rectangles.

This is fundamentally different from screenshot-based approaches like Anthropic's Computer Use or OmniParser. Those require a vision model to interpret pixels. Windows-MCP gives the LLM structured text, which means:

- **Any LLM works** — no multimodal capability required
- **Faster** — no image encoding/decoding overhead
- **More deterministic** — elements are identified by name and role, not pixel position
- **Lower token cost** — text is smaller than base64-encoded screenshots

The trade-off: accessibility trees don't capture everything. Custom-drawn UI, games, and applications that don't properly implement UI Automation will appear as opaque regions. Screenshot mode exists as a fallback for these cases.

## Performance

Typical action-to-action latency ranges from **0.2 to 0.9 seconds**, depending on system load and the number of active applications. That's the server-side overhead — total round-trip time also depends on your LLM's inference speed.

Version 0.6.0 (January 2026) delivered a **~6x performance improvement** through execution optimization and thread management fixes. The server uses minimal memory and has no heavy dependencies beyond the Python standard library and the `pywinauto`/UI Automation bindings.

## Setup

**Prerequisites:** Python 3.13+, [UV package manager](https://docs.astral.sh/uv/)

### Claude Desktop

```json
{
  "mcpServers": {
    "windows-mcp": {
      "command": "uvx",
      "args": ["windows-mcp"]
    }
  }
}
```

That's it. One line via `uvx` — no cloning, no building, no virtual environments. The package is on PyPI as `windows-mcp`.

### Claude Code

```bash
claude mcp add windows-mcp -- uvx windows-mcp
```

### Other Clients

Windows-MCP works with Cursor, VS Code (Copilot agent mode), Gemini CLI, Qwen Code, Codex CLI, and Perplexity Desktop. Any MCP client that supports stdio transport will work out of the box.

## Transport Modes

| Transport | Command Flag | Use Case |
|-----------|-------------|----------|
| **stdio** (default) | `--transport stdio` | Local MCP client connection |
| **SSE** | `--transport sse --host HOST --port PORT` | Server-Sent Events for network access |
| **Streamable HTTP** | `--transport streamable-http --host HOST --port PORT` | Production-recommended HTTP streaming |

The stdio transport is the default and what most users need. SSE and Streamable HTTP are for scenarios where the MCP client runs on a different machine — useful for remote desktop automation workflows.

## Remote Mode

Windows-MCP also supports a **remote mode** that connects to cloud-hosted Windows VMs via the windowsmcp.io service. Set `MODE=remote`, provide a `SANDBOX_ID` and `API_KEY`, and the server proxies commands to a remote Windows instance. This is a separate commercial offering from the CursorTouch team, not part of the open-source project.

## The Ecosystem: Windows-MCP vs. Alternatives

Windows-MCP isn't the only option for Windows desktop automation via MCP. Here's how the main contenders compare:

| Dimension | Windows-MCP (CursorTouch) | MCPControl | mcp-windows-desktop-automation | mcp-windows-automation |
|-----------|--------------------------|------------|-------------------------------|----------------------|
| **GitHub Stars** | 4,800+ | 302 | ~100 | 14 |
| **Language** | Python | TypeScript/Node.js | TypeScript | Python |
| **License** | MIT | MIT | MIT | MIT |
| **UI Approach** | Accessibility tree snapshots | Screenshot + coordinates | AutoIt function wrappers | PyAutoGUI + shell commands |
| **Tool Count** | 17 | ~10 | ~15 | 80+ (claimed) |
| **Vision Required** | No (optional screenshot fallback) | Yes (screenshot-based) | No | Partial |
| **Transport** | stdio, SSE, Streamable HTTP | SSE, HTTPS | stdio | stdio |
| **Stability** | Active, v0.7.0, regular releases | Experimental ("potentially dangerous") | Active, AutoIt-dependent | Low activity |
| **Unique Feature** | Accessibility tree + DOM mode | AutoHotkey provider option | AutoIt scripting integration | 80+ tools across categories |

**Windows-MCP wins on adoption, architecture, and maintenance.** Its accessibility tree approach is the most LLM-friendly — the same architectural insight that made Playwright MCP dominant in browser automation. MCPControl is the main TypeScript alternative but explicitly warns it's experimental and best used in VMs at 1280x720 resolution. The AutoIt-based server is a solid choice if you're already in the AutoIt ecosystem. The 80+ tool server from mukul975 has breadth but very low adoption.

## Microsoft's Official MCP on Windows

Worth noting: Microsoft is building **MCP support directly into Windows** through the On-device Agent Registry (ODR). This is a platform-level framework for discovering and managing MCP servers on Windows, with built-in security containment, user/admin consent controls, and Intune management. Windows ships default connectors for File Explorer and Windows Settings.

The ODR is a different layer — it's an operating system feature for managing MCP servers, not a desktop automation server itself. Windows-MCP and the ODR are complementary: Windows-MCP provides the desktop automation tools, while the ODR provides the discovery and security infrastructure. As of early 2026, the ODR is in preview and not yet widely available.

## What It Can't Do

Be clear-eyed about the limitations:

- **No text selection within paragraphs** — the accessibility tree doesn't expose character-level ranges within text elements. You can select entire elements but not highlight specific words.
- **Not suitable for IDE coding** — the Type tool enters entire content at once rather than character-by-character, which doesn't work well with code editors that have autocomplete and formatting.
- **No game automation** — games typically don't implement UI Automation, so the accessibility tree is empty. Screenshot mode won't help much either since game UIs change rapidly.
- **Windows only** — no macOS or Linux support (by design).
- **Full system access** — the server can run arbitrary PowerShell commands, modify the registry, and terminate processes. There's no built-in permission system or sandboxing. The CursorTouch team recommends reviewing their security guidelines before deployment.

## Security Considerations

This is the elephant in the room. Windows-MCP gives an AI agent **unrestricted access** to your Windows system. The Shell tool runs PowerShell commands. The Registry tool modifies system settings. The Process tool can kill processes. There's no allowlist, no confirmation step, no sandboxing.

The server collects **anonymized telemetry** by default (no personal information, tool arguments, or outputs — just usage patterns). You can disable it with `ANONYMIZED_TELEMETRY=false`.

For production or sensitive environments, we'd recommend:
- Running in a VM or sandbox
- Using Microsoft's ODR security containment when it's available
- Reviewing the CursorTouch security policy in the repository
- Being aware that prompt injection attacks could theoretically trick an agent into running destructive commands

## Project Health

| Metric | Value |
|--------|-------|
| **Stars** | 4,800+ |
| **Forks** | 604 |
| **Latest Version** | v0.7.0 (March 17, 2026) |
| **First Release** | v0.1 (June 4, 2024) |
| **Release Cadence** | ~monthly |
| **Python Requirement** | 3.13+ |
| **Platform** | Windows 7–11 |
| **License** | MIT |
| **Package** | PyPI (`windows-mcp`) |
| **Community** | Discord server, Twitter @CursorTouch |
| **Adoption** | 2M+ users via Claude Desktop Extensions |

The project is actively maintained with 9 releases over 10 months. The v0.6.0 performance overhaul (6x speedup) shows the team is investing in quality, not just features. The 2M+ user claim (via Claude Desktop Extensions) makes it one of the most-used MCP servers in any category.

## The Bottom Line

Windows-MCP is to Windows desktop automation what Playwright MCP is to browser automation: the accessibility-tree-first approach that lets any LLM interact with native UI elements without requiring vision models. It's the most adopted, most actively maintained, and architecturally soundest option in the Windows desktop automation space.

The 17-tool surface covers the full range of desktop interaction — UI elements, screenshots, shell commands, clipboard, processes, registry, notifications. Setup is a one-liner via `uvx`. Performance is solid at 0.2-0.9 seconds per action. The MIT license is clean.

The main concerns are **security** (full system access with no sandboxing) and **scope limitations** (accessibility tree gaps for custom UI, games, and fine-grained text selection). The Python 3.13+ requirement is also notably aggressive — you'll need a recent Python installation.

If you need an AI agent to automate Windows desktop tasks — QA testing, workflow automation, form filling, system administration, cross-application workflows — Windows-MCP is the clear first choice. Just run it in a VM if you're doing anything consequential.

**Rating: 4.0 / 5** — The leading Windows desktop automation MCP server with strong adoption, clean architecture, and active maintenance. Loses a full point for the security model (unrestricted system access with no built-in safeguards) and accessibility tree limitations that leave some UI opaque.

---

*This review is AI-generated by [ChatForest](https://chatforest.com), researched from public GitHub repositories, documentation, and community discussions. We have not installed or tested this server hands-on. All claims are based on published documentation and code review. Last refreshed: March 23, 2026.*


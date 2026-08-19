# Windows-MCP Server — Give Your AI Agent Eyes and Hands on Windows

> Windows-MCP by CursorTouch is the leading MCP server for Windows desktop automation. 6,700+ GitHub stars, 20 tools, accessibility tree snapshots, 0.2-0.5s latency, MIT license.


Browser automation has its Playwright MCP. macOS has its AppleScript-based servers. But what about controlling the Windows desktop itself — launching applications, clicking native UI elements, filling forms in Win32 apps, running PowerShell commands? That's the gap [Windows-MCP](https://github.com/CursorTouch/Windows-MCP) fills, and with [6,778 GitHub stars](https://github.com/CursorTouch/Windows-MCP) it's the clear leader in this space.

Built by the CursorTouch team, Windows-MCP is a Python-based MCP server that bridges AI agents and the Windows operating system. It doesn't rely on computer vision or fine-tuned models — instead it uses the Windows Accessibility API to read UI element trees, giving any LLM (multimodal or not) a structured, text-based understanding of what's on screen. If you've seen how Playwright MCP revolutionized browser automation with accessibility tree snapshots, Windows-MCP applies the same principle to the entire Windows desktop.

**Category:** [Developer Tools](/categories/developer-tools/)

---

## What It Does

Windows-MCP exposes [20 tools](https://github.com/CursorTouch/Windows-MCP#-mcp-tools) organized around three capabilities: **seeing** the screen, **interacting** with elements, and **controlling** the system.

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
| **DisplayInventory** | Read display layout, work areas, effective DPI, and scale metadata (added for multi-monitor setups) |

### System Control Tools

| Tool | Purpose |
|------|---------|
| **App** | Launch applications by name or path |
| **PowerShell** | Execute PowerShell commands (formerly named "Shell") |
| **FileSystem** | Read, write, copy, move, delete, list, search, and inspect files and directories |
| **Clipboard** | Read and write clipboard content |
| **Process** | List running processes or terminate them |
| **Notification** | Send Windows toast notifications |
| **Registry** | Read and write Windows Registry values and keys |
| **Wait** | Pause execution for a specified duration |
| **WaitFor** | Poll UI state inside one tool call until text, an active window, an element, or a focused element appears |

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

Typical action-to-action latency ranges from **[0.2 to 0.5 seconds](https://github.com/CursorTouch/Windows-MCP)**, depending on system load and the number of active applications. That's the server-side overhead — total round-trip time also depends on your LLM's inference speed.

[Version 0.6.0 (January 2026)](https://github.com/CursorTouch/Windows-MCP/releases/tag/v0.6.0) delivered a **~6x performance improvement** through execution optimization and PostHog analytics batching. The server uses minimal memory and has no heavy dependencies beyond the Python standard library and the `pywinauto`/UI Automation bindings.

## Setup

**Prerequisites:** [Python 3.12+](https://pypi.org/project/windows-mcp/) (the published `windows-mcp` package's declared requirement as of v0.8.5 — note the GitHub README's badge and prerequisites list still say 3.13+, and the in-development `main` branch has since bumped to 3.14+ for the next release), [UV package manager](https://docs.astral.sh/uv/)

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

Windows-MCP works with Cursor, VS Code (Copilot agent mode), Gemini CLI, Qwen Code, Codex CLI, Autohand Code, and Perplexity Desktop. Any MCP client that supports stdio transport will work out of the box.

## Transport Modes

| Transport | Command Flag | Use Case |
|-----------|-------------|----------|
| **stdio** (default) | `--transport stdio` | Local MCP client connection |
| **SSE** | `--transport sse --host HOST --port PORT` | Server-Sent Events for network access |
| **Streamable HTTP** | `--transport streamable-http --host HOST --port PORT` | Production-recommended HTTP streaming |

The stdio transport is the default and what most users need. SSE and Streamable HTTP are for scenarios where the MCP client runs on a different machine — useful for remote desktop automation workflows.

## Remote Mode

Windows-MCP also supports a **remote mode** that connects to cloud-hosted Windows VMs via the [windowsmcp.io](https://windowsmcp.io/docs/installation) service. Set `MODE=remote`, provide a `SANDBOX_ID` and `API_KEY` from a paid dashboard account, and the server proxies commands to a remote Windows instance. This is a separate commercial offering from the CursorTouch team — it's no longer documented in the main GitHub README (which now focuses on the open-source server's own SSE/Streamable HTTP + auth-key/OAuth remote-access options, covered below), so treat windowsmcp.io as a distinct paid product layered on top of, not part of, the open-source project.

## The Ecosystem: Windows-MCP vs. Alternatives

Windows-MCP isn't the only option for Windows desktop automation via MCP. Here's how the main contenders compare:

| Dimension | Windows-MCP (CursorTouch) | MCPControl | mcp-windows-desktop-automation | mcp-windows-automation |
|-----------|--------------------------|------------|-------------------------------|----------------------|
| **GitHub Stars** | [6,778](https://github.com/CursorTouch/Windows-MCP) | [331](https://github.com/claude-did-this/MCPControl) | [113](https://github.com/mario-andreschak/mcp-windows-desktop-automation) | [48](https://github.com/mukul975/mcp-windows-automation) |
| **Language** | Python | TypeScript/Node.js | TypeScript | Python |
| **License** | MIT | MIT | MIT | MIT |
| **UI Approach** | Accessibility tree snapshots | Screenshot + coordinates | AutoIt function wrappers | PyAutoGUI + shell commands |
| **Tool Count** | [20](https://github.com/CursorTouch/Windows-MCP#-mcp-tools) | ~10 | ~15 | [200+ (claimed)](https://github.com/mukul975/mcp-windows-automation) |
| **Vision Required** | No (optional screenshot fallback) | Yes (screenshot-based) | No | Partial |
| **Transport** | stdio, SSE, Streamable HTTP | SSE, HTTPS | stdio | stdio |
| **Stability** | Active, [v0.8.5](https://github.com/CursorTouch/Windows-MCP/releases/tag/v0.8.5), regular releases | Experimental ("potentially dangerous"); [no commits since Jul 2025](https://github.com/claude-did-this/MCPControl/commits/main) | [Inactive since Mar 2025](https://github.com/mario-andreschak/mcp-windows-desktop-automation/commits/main) (4 commits total), AutoIt-dependent | Low activity ([last commit Mar 2026](https://github.com/mukul975/mcp-windows-automation/commits/master)) |
| **Unique Feature** | Accessibility tree + DOM mode | AutoHotkey provider option | AutoIt scripting integration | 200+ tools across categories (claimed) |

**Windows-MCP wins on adoption, architecture, and maintenance.** Its accessibility tree approach is the most LLM-friendly — the same architectural insight that made Playwright MCP dominant in browser automation. MCPControl is the main TypeScript alternative but explicitly warns it's experimental and best used in VMs at 1280x720 resolution — and it's been dormant for over a year, with no commits since July 2025. The AutoIt-based server is essentially a stalled prototype: just 4 commits, all from March 2025, with nothing since. The 200+-tool server from mukul975 (up from an 80+ claim at last audit) has breadth but still very low adoption at 48 stars.

## Microsoft's Official MCP on Windows

Worth noting: Microsoft is building **MCP support directly into Windows** through the [On-device Agent Registry (ODR)](https://learn.microsoft.com/en-us/windows/ai/mcp/overview). This is a platform-level framework for discovering and managing MCP servers on Windows, with [security containment in a separate environment by default, user/admin consent controls via Windows Settings, and Intune management](https://learn.microsoft.com/en-us/windows/ai/mcp/overview). Windows ships default connectors for [File Explorer](https://learn.microsoft.com/en-us/windows/ai/mcp/overview) and Windows Settings.

The ODR is a different layer — it's an operating system feature for managing MCP servers, not a desktop automation server itself. Windows-MCP and the ODR are complementary: Windows-MCP provides the desktop automation tools, while the ODR provides the discovery and security infrastructure.

As of this writing (checked August 2026), the ODR is [formally documented on Microsoft Learn](https://learn.microsoft.com/en-us/windows/ai/mcp/overview) with an [`odr.exe` CLI](https://learn.microsoft.com/en-us/windows/ai/mcp/odr-tool), integration with [Visual Studio and VS Code GitHub Copilot agent mode](https://learn.microsoft.com/en-us/windows/ai/mcp/overview), and default connectors for File Explorer and Windows Settings. It still carries a prerelease warning — Microsoft's own docs state "some information relates to prereleased product that might change substantially before it's commercially released." No evidence yet that CursorTouch has formally registered Windows-MCP through the ODR, though it's compatible.

## What It Can't Do

Be clear-eyed about the limitations:

- **No text selection within paragraphs** — the accessibility tree doesn't expose character-level ranges within text elements. You can select entire elements but not highlight specific words.
- **Not suitable for IDE coding** — the Type tool enters entire content at once rather than character-by-character, which doesn't work well with code editors that have autocomplete and formatting.
- **No game automation** — games typically don't implement UI Automation, so the accessibility tree is empty. Screenshot mode won't help much either since game UIs change rapidly.
- **Windows only** — no macOS or Linux support (by design).
- **Full system access by default** — the server can run arbitrary PowerShell commands, modify the registry, and terminate processes. As covered below, the server has since added opt-in tool-level allowlisting, but there's still no per-call confirmation step. The CursorTouch team recommends reviewing their [security guidelines](https://github.com/CursorTouch/Windows-MCP/blob/main/SECURITY.md) before deployment.

## Security Considerations

This is the elephant in the room. Windows-MCP gives an AI agent **broad access** to your Windows system by default. The PowerShell tool (formerly named "Shell") runs arbitrary shell commands. The Registry tool modifies system settings. The Process tool can kill processes. There's no per-call confirmation step for enabled tools, and no sandboxing built into the server itself.

That said, [the server has added real access controls](https://github.com/CursorTouch/Windows-MCP/blob/main/README.md#-security--access-control) since this review was first published: you can now disable specific tools entirely with `--exclude-tools "PowerShell,Registry"` (or the `WINDOWS_MCP_EXCLUDE_TOOLS` env var), or whitelist only the tools you want with `--tools`. For network-exposed deployments over SSE or Streamable HTTP, the server supports bearer-token auth keys, IP allowlisting (with private/loopback IPs blocked by default), TLS, and OAuth 2.0 + PKCE. None of this changes the risk profile for a local stdio setup where every tool is enabled — which is still the common case — but it does mean "no allowlist at all" is no longer accurate.

The server collects **anonymized telemetry** by default (no personal information, tool arguments, or outputs — just usage patterns, via PostHog). You can disable it with `ANONYMIZED_TELEMETRY=false`.

For production or sensitive environments, we'd recommend:
- Running in a VM or sandbox
- Using the server's own `--exclude-tools` flag to disable PowerShell and Registry if an agent doesn't need them
- Using Microsoft's ODR security containment when it's available
- Reviewing the [CursorTouch security policy](https://github.com/CursorTouch/Windows-MCP/blob/main/SECURITY.md) in the repository
- Being aware that prompt injection attacks could theoretically trick an agent into running destructive commands

## Project Health

| Metric | Value |
|--------|-------|
| **Stars** | [6,778](https://github.com/CursorTouch/Windows-MCP) |
| **Forks** | [820](https://github.com/CursorTouch/Windows-MCP/forks) |
| **Latest Version** | [v0.8.5](https://github.com/CursorTouch/Windows-MCP/releases/tag/v0.8.5) (August 1, 2026) |
| **First Release** | [v0.1](https://github.com/CursorTouch/Windows-MCP/releases/tag/v0.1) (June 4, 2025) |
| **Release Cadence** | ~biweekly to monthly |
| **PyPI Downloads** | [~199,800 (with mirrors) in the trailing 180 days](https://pypistats.org/packages/windows-mcp), per PyPIStats as of Aug 18, 2026 |
| **Python Requirement** | [3.12+](https://pypi.org/project/windows-mcp/) (per current PyPI package metadata) |
| **Platform** | Windows 7–11 |
| **License** | MIT |
| **Package** | PyPI (`windows-mcp`) |
| **Community** | Discord server, Twitter @CursorTouch |
| **Adoption** | [2M+ users via Claude Desktop Extensions](https://github.com/CursorTouch/Windows-MCP) (self-reported by CursorTouch, not independently audited) |

The project is actively maintained with multiple releases per month. The v0.6.0 performance overhaul (6x speedup) and the v0.7.4 UIA double-caching fix (halving COM calls per node) show a team investing in engineering quality, not just feature additions. [v0.8.5 (August 1, 2026)](https://github.com/CursorTouch/Windows-MCP/releases/tag/v0.8.5) fixed a protocol-breaking bug where tree traversal was writing text to stdout — the same channel that carries JSON-RPC framing on the default stdio transport — and added a self-healing UIA watchdog plus per-monitor display inventory. The 2M+ user claim via Claude Desktop Extensions — and PyPI download volume that's roughly doubled since the last audit — make it one of the most-used MCP servers in any category.

v0.7.1 (March 29, 2026) added MSIX/UWP app path resolution for Windows Store app automation, fixed multi-display mouse coordinate mismatches, and resolved non-ASCII character marshaling crashes in the UIA layer. v0.7.4 (April 23, 2026) delivered a meaningful performance improvement by eliminating double caching in the UIA tree traversal, cutting COM calls from 2 to 1 per node.

## The Bottom Line

Windows-MCP is to Windows desktop automation what Playwright MCP is to browser automation: the accessibility-tree-first approach that lets any LLM interact with native UI elements without requiring vision models. It's the most adopted, most actively maintained, and architecturally soundest option in the Windows desktop automation space.

The 20-tool surface covers the full range of desktop interaction — UI elements, screenshots, PowerShell commands, file operations, clipboard, processes, registry, notifications. Setup is a one-liner via `uvx`. Performance is solid at [0.2-0.5 seconds](https://github.com/CursorTouch/Windows-MCP) per action. The MIT license is clean.

The main concerns are **security** (full tool access enabled by default, though tool-level allowlisting now exists) and **scope limitations** (accessibility tree gaps for custom UI, games, and fine-grained text selection). The Python 3.12+ requirement (climbing to 3.14+ in the next release per the in-development `main` branch) is also notably aggressive — you'll need a recent Python installation.

If you need an AI agent to automate Windows desktop tasks — QA testing, workflow automation, form filling, system administration, cross-application workflows — Windows-MCP is the clear first choice. Just run it in a VM if you're doing anything consequential.

**Rating: 4.0 / 5** — The leading Windows desktop automation MCP server with strong adoption, clean architecture, and active maintenance. Loses a full point for the security model (full tool access enabled by default, with no per-call confirmation step even though opt-in allowlisting and remote-access auth now exist) and accessibility tree limitations that leave some UI opaque.

---

*This review is AI-generated by [ChatForest](https://chatforest.com), researched from public GitHub repositories, documentation, and community discussions. We have not installed or tested this server hands-on. All claims are based on published documentation and code review. Last refreshed: August 19, 2026.*


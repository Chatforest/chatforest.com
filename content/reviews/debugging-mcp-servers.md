---
title: "Debugging MCP Servers — Chrome DevTools, VS Code, GDB, LLDB, Embedded, and 25+ More"
date: 2026-03-16T21:00:00+09:00
description: "Debugging MCP servers let AI agents set breakpoints, step through code, inspect variables, and diagnose failures across browsers, IDEs, native binaries, and embedded hardware. We reviewed 25+ servers across 7 subcategories. Chrome DevTools MCP dominates (29.3K stars, 25+ tools). Microsoft's DebugMCP brings multi-language debugging to VS Code. debugmcp/mcp-debugger supports 5 languages via DAP. Native debugger integration covers GDB, LLDB, WinDbg, and embedded ARM/RISC-V. Rating: 4.5/5."
og_description: "Debugging MCP servers: Chrome DevTools (29.3K stars, 25+ tools), claude-debugs-for-you (496 stars), ScriptedAlchemy devtools-debugger (340 stars), DebugMCP (221 stars, Microsoft), mcp-debugger (85 stars, 5 languages), lldb-mcp (85 stars), MDB-MCP (56 stars, GDB+LLDB), embedded-debugger-mcp (56 stars, ARM/RISC-V). 25+ servers reviewed. Rating: 4.5/5."
content_type: "Review"
card_description: "Debugging MCP servers across browser DevTools, VS Code integration, multi-language debuggers, native binary debuggers (GDB/LLDB/WinDbg), and embedded hardware. Chrome DevTools MCP (29.3K stars, MIT) dominates with 25+ tools covering browser automation, network inspection, Lighthouse audits, performance analysis, and DOM snapshots — it's the most-starred MCP server in the debugging space by a wide margin. For IDE-integrated debugging, three strong options exist: jasonjmcghee/claude-debugs-for-you (496 stars, MIT) pioneered the VS Code + MCP debugging pattern with language-agnostic breakpoints and expression evaluation; ScriptedAlchemy/devtools-debugger-mcp (340 stars, MIT) exposes full Chrome DevTools Protocol for Node.js with source map support and conditional breakpoints; microsoft/DebugMCP (221 stars, MIT) provides a first-party VS Code extension supporting 8+ languages (Python, JS/TS, Java, C#, C++, Go, Rust, Ruby) with 13 debugging tools. For multi-language debugging via DAP, debugmcp/mcp-debugger (85 stars, MIT, 1266+ tests) supports Python, JavaScript, Rust, Go, and Java through a clean adapter architecture. Native binary debugging has strong coverage: stass/lldb-mcp (85 stars, BSD-2) and smadi0x86/MDB-MCP (56 stars, GPL-3.0, GDB+LLDB) handle C/C++ and systems-level debugging; pansila/mcp_server_gdb (62 stars, MIT, Rust) adds a fast GDB/MI bridge; tonyredondo/debugger-mcp-server (2 stars, MIT, C#) provides cross-platform WinDbg/LLDB with .NET dump analysis and Datadog integration. Python gets dedicated support from samefarrar/mcp-pdb (45 stars, MIT) wrapping pdb with session management. Embedded hardware debugging is handled by Adancurusul/embedded-debugger-mcp (56 stars, MIT, Rust) with 22 tools for ARM Cortex-M and RISC-V via probe-rs, validated on real STM32 hardware. XcodeBuildMCP (4.8K stars, MIT) covers iOS/macOS debugging with LLDB integration. The MCP Inspector (9.1K stars, MIT, official) serves as the ecosystem's debugging tool for MCP servers themselves. Gaps: no dedicated Android/ADB debugger MCP, no Java-only debugger (only via multi-language servers), limited .NET debugging outside WinDbg, no dedicated React Native or Flutter debugging MCP. Rating: 4.5/5."
last_refreshed: 2026-03-16
---

Debugging is one of the highest-leverage uses of MCP. Instead of copying error messages into a chat window, describing your breakpoint state, or manually walking an AI through stack traces, a debugging MCP server gives the agent direct access to the debugger itself — set breakpoints, step through code, inspect variables, evaluate expressions, all programmatically.

The ecosystem has matured rapidly. **Chrome DevTools MCP** (29.3K stars) lets agents control a live browser for web debugging. **Microsoft's DebugMCP** brings multi-language debugging into VS Code. **debugmcp/mcp-debugger** supports five languages through the Debug Adapter Protocol. Native debugger servers cover **GDB, LLDB, and WinDbg**. There's even an embedded hardware debugger for **ARM Cortex-M and RISC-V** microcontrollers.

The headline: debugging MCP servers are among the most practically useful in the entire MCP ecosystem. If you're using an AI coding assistant, a debugging server is likely the single highest-value addition you can make.

For browser automation and testing (without debugging focus), see our [Playwright](/reviews/playwright-mcp-server/) and [Puppeteer](/reviews/puppeteer-mcp-server/) reviews. For error tracking platforms, see our [Sentry](/reviews/sentry-mcp-server/) and [Datadog](/reviews/datadog-mcp-server/) reviews. For the official MCP server testing tool, the MCP Inspector is covered at the end of this review.

## Browser Debugging — Chrome DevTools (2+ servers)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | 29,300 | TypeScript | — | 25+ | Full browser control: automation, debugging, performance, network, Lighthouse |
| [ScriptedAlchemy/devtools-debugger-mcp](https://github.com/ScriptedAlchemy/devtools-debugger-mcp) | 340 | JavaScript/TS | MIT | 15+ | Chrome DevTools Protocol for Node.js: breakpoints, stepping, source maps |

**ChromeDevTools/chrome-devtools-mcp** (29.3K stars) is the official Chrome DevTools MCP server and one of the most-starred MCP servers in existence. It gives AI agents full control over a live Chrome browser — not just debugging, but automation, performance analysis, and network inspection. The tools span input automation (9 tools: click, drag, fill forms, handle dialogs), navigation (6 tools), performance analysis (4 tools: trace recording, memory snapshots), debugging (6 tools: script execution, console messages, Lighthouse audits, screenshots, DOM snapshots), and network/emulation. It integrates with Cursor, Claude Code, VS Code Copilot, Gemini CLI, and 20+ other platforms. A "slim" mode provides just 3 essential tools for lightweight usage. Requires Node.js v20.19+ and Chrome stable.

**ScriptedAlchemy/devtools-debugger-mcp** (340 stars) takes a different approach — it focuses specifically on Node.js debugging via the Chrome DevTools Protocol. It launches Node.js with `--inspect-brk` and provides breakpoint management (standard, conditional, logpoints), execution controls (step over/into/out, continue to location), variable inspection across scopes and closures, expression evaluation with console capture, call stack analysis, and source map support for transpiled TypeScript. This is the server to use when you need an AI agent to step through server-side JavaScript/TypeScript code.

## VS Code Debugging (3 servers)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [jasonjmcghee/claude-debugs-for-you](https://github.com/jasonjmcghee/claude-debugs-for-you) | 496 | TypeScript | MIT | 5+ | Language-agnostic VS Code debugging via MCP + extension |
| [microsoft/DebugMCP](https://github.com/microsoft/DebugMCP) | 221 | TypeScript | MIT | 13 | Official Microsoft VS Code extension, 8+ languages |
| [workbackai/mcp-nodejs-debugger](https://github.com/workbackai/mcp-nodejs-debugger) | 303 | JavaScript | — | 7+ | Node.js runtime debugging for Cursor/Claude Code (archived) |

**jasonjmcghee/claude-debugs-for-you** (496 stars) pioneered the VS Code + MCP debugging pattern. It's a VS Code extension plus MCP server that enables any LLM to interactively debug any language — as long as VS Code supports it via `launch.json`. The agent can set breakpoints, evaluate expressions, and step through code in the debugger console. It supports stdio and SSE transport and works with Claude Desktop, Continue, and Cursor. Language-agnostic design is the key advantage — if VS Code can debug it, this server can expose it to an AI agent.

**microsoft/DebugMCP** (221 stars) is Microsoft's first-party answer. It's a VS Code extension (requires VS Code 1.104.0+) that embeds an MCP server exposing 13 debugging tools: breakpoint management (add, remove, list, clear), execution control (step over, step into, step out, continue), variable inspection, expression evaluation, and session management (start, stop, restart). It explicitly supports 8+ languages: Python, JavaScript/TypeScript, Java, C#, C++, Go, Rust, and Ruby. It integrates with GitHub Copilot, Cline, and Cursor. Runs 100% locally with no external data transmission. Works with remote SSH, Codespaces, and WSL.

**workbackai/mcp-nodejs-debugger** (303 stars) was a popular Node.js debugging MCP server designed for Cursor and Claude Code, using `--inspect` mode for runtime breakpoints and variable inspection. It was **archived in January 2026** — likely made redundant by Microsoft's DebugMCP and the broader debugging MCP ecosystem. Still usable but no longer maintained.

## Multi-Language Debugging via DAP (1 server)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [debugmcp/mcp-debugger](https://github.com/debugmcp/mcp-debugger) | 85 | TypeScript | MIT | 15+ | 5 languages via DAP: Python, JS, Rust, Go, Java |

**debugmcp/mcp-debugger** (85 stars) is the most ambitious multi-language debugging server. It uses the Debug Adapter Protocol (DAP) to support **Python** (via debugpy), **JavaScript/Node.js** (via Microsoft's js-debug, bundled), **Rust** (via CodeLLDB on Linux/macOS), **Go** (via Delve), and **Java** (via JDI bridge, JDK 21+). Each language plugs in through a clean adapter architecture, making it extensible. Features include breakpoint management, stack trace inspection, variable scoping, expression evaluation, step commands with source context, and concurrent session management. It has 1,266+ tests passing and runs via `npx @debugmcp/mcp-debugger` with zero runtime dependencies. If you need one debugging server for multiple languages and don't want VS Code integration, this is the choice.

## Python Debugging (1 server)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [samefarrar/mcp-pdb](https://github.com/samefarrar/mcp-pdb) | 45 | Python | MIT | 8 | Python's pdb debugger via MCP, pytest support |

**samefarrar/mcp-pdb** (45 stars) wraps Python's built-in pdb debugger as an MCP server. Tools include `start_debug`, `send_pdb_command`, `set_breakpoint`, `clear_breakpoint`, `examine_variable`, `get_debug_status`, `list_breakpoints`, `restart_debug`, and `end_debug`. It supports both direct Python file debugging and pytest-based debugging, with automatic virtual environment detection and breakpoint restoration between sessions. Requires Python 3.12+. Inspired by Microsoft's debug-gym project. **Security note:** this executes Python code through the debugger — use in trusted environments only.

## Native Binary Debugging — GDB, LLDB, WinDbg (5+ servers)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [stass/lldb-mcp](https://github.com/stass/lldb-mcp) | 85 | Python | BSD-2 | 15+ | Full LLDB integration: breakpoints, watchpoints, memory, disassembly |
| [pansila/mcp_server_gdb](https://github.com/pansila/mcp_server_gdb) | 62 | Rust | MIT | 10+ | Fast GDB/MI bridge, multi-session, TUI inspection |
| [smadi0x86/MDB-MCP](https://github.com/smadi0x86/MDB-MCP) | 56 | Python | GPL-3.0 | 5+ | Unified GDB + LLDB interface with auto-detection |
| [tonyredondo/debugger-mcp-server](https://github.com/tonyredondo/debugger-mcp-server) | 2 | C# | MIT | 11 | Cross-platform WinDbg/LLDB, .NET dump analysis, Datadog integration |
| [hnmr293/gdb-mcp](https://github.com/hnmr293/gdb-mcp) | 2 | Python | Apache-2.0 | 3+ | GDB with CLI + MI modes, built-in command reference |

LLDB also has **native MCP support** built directly into the LLDB debugger itself (documented at [lldb.llvm.org/use/mcp.html](https://lldb.llvm.org/use/mcp.html)), meaning AI agents can execute LLDB commands without any third-party server.

**stass/lldb-mcp** (85 stars) is the most feature-complete standalone LLDB server. It supports multiple simultaneous sessions, program loading/attachment/core dump analysis, breakpoints and watchpoints, execution control (run, continue, step, next, finish, kill), memory examination, disassembly, stack traces, register inspection, thread management, and arbitrary LLDB command execution. Includes an example buffer overflow program demonstrating automated debugging. Sessions auto-cleanup on server shutdown.

**pansila/mcp_server_gdb** (62 stars) is a Rust implementation of a GDB/MI protocol bridge — fast and cross-platform with concurrent multi-session support. Features include debug control (run, pause, step, step-over), breakpoint management, stack frames, local variables, registers, and memory inspection. Supports both stdio and SSE transport. Includes a TUI for observing agent behavior (work-in-progress).

**smadi0x86/MDB-MCP** (56 stars) provides a unified interface to both GDB and LLDB with automatic debugger detection. Useful when you want one MCP server that works on both Linux (GDB) and macOS (LLDB) without configuration changes. Includes example binaries for arm64 and amd64.

**tonyredondo/debugger-mcp-server** (2 stars but 361 commits) is a sophisticated C# implementation covering WinDbg on Windows and LLDB on Linux/macOS. Its standout feature is **.NET dump analysis** — crash analysis, .NET runtime inspection, performance profiling, security scanning, and dump comparison. It includes Datadog trace symbols integration and optional AI-powered analysis with LLM integration. Dual interface: MCP protocol + REST HTTP API. Docker support included.

## Embedded Hardware Debugging (1 server)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [Adancurusul/embedded-debugger-mcp](https://github.com/Adancurusul/embedded-debugger-mcp) | 56 | Rust | MIT | 22 | ARM Cortex-M & RISC-V via probe-rs, real hardware validated |

**Adancurusul/embedded-debugger-mcp** (56 stars) is remarkable — it brings MCP debugging to embedded microcontrollers. Using probe-rs, it supports ARM Cortex-M and RISC-V targets with 22 tools covering probe management (discovery, connection, info), memory operations (read/write flash and RAM), debug control (halt, run, reset, single-step), breakpoint management (hardware and software), flash programming (erase, program, verify), and RTT bidirectional communication. Validated on real STM32G431CBTx hardware. Supports J-Link, ST-Link V2/V3, DAPLink, and Black Magic Probe. This is one of the most specialized MCP servers we've reviewed — if you're doing embedded development with AI assistance, it's the only game in town.

## Xcode / iOS Debugging (1 server)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [cameroncooke/XcodeBuildMCP](https://github.com/cameroncooke/XcodeBuildMCP) | 4,800 | TypeScript | MIT | 10+ | iOS/macOS build, debug, and deploy with LLDB integration |

**XcodeBuildMCP** (4.8K stars) is primarily a build tool for iOS/macOS projects, but it includes debugging capabilities — attaching the debugger, setting breakpoints, inspecting variables, and executing LLDB commands from AI agents. It works with Cursor, Claude Code, VS Code, and even Xcode itself. Requires macOS 14.5+ and Xcode 16.x+. AgentAudit security certified.

## MCP Server Debugging — The Inspector

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [modelcontextprotocol/inspector](https://github.com/modelcontextprotocol/inspector) | 9,100 | TypeScript | MIT | — | Official visual testing tool for MCP servers |

The **MCP Inspector** (9.1K stars) deserves mention in any debugging review because it's the tool you use to debug MCP servers themselves. It's a React-based web UI + Node.js proxy that connects to any MCP server via stdio, SSE, or Streamable HTTP. You can test tools, explore resources, and inspect raw JSON-RPC messages. Run via `npx @modelcontextprotocol/inspector`. It includes a CLI mode for CI/CD automation. If you're building or troubleshooting any MCP server, the Inspector is essential.

## What's Missing

- **Android/ADB debugging** — no dedicated MCP server for Android debugging via ADB or Android Studio
- **Java-only debugger** — Java is only supported through multi-language servers (DebugMCP, mcp-debugger), no dedicated JDB/JDWP MCP server
- **.NET debugging** — limited to WinDbg dump analysis (tonyredondo's server); no dedicated .NET/C# step debugger MCP
- **React Native / Flutter** — no cross-platform mobile debugging MCP servers
- **Browser debugging beyond Chrome** — Firefox DevTools, Safari Web Inspector have no MCP integration
- **Remote debugging** — most servers assume local execution; limited support for debugging remote processes

## The Bottom Line

Debugging MCP servers are among the most practically impactful in the entire MCP ecosystem. The category earns a **4.5/5** — one of our highest ratings. Chrome DevTools MCP (29.3K stars) provides comprehensive browser debugging. Microsoft's DebugMCP and claude-debugs-for-you bring IDE-integrated debugging to VS Code across many languages. debugmcp/mcp-debugger covers five languages via DAP without IDE dependency. Native debugger servers handle C/C++ and systems programming. The embedded hardware debugger is genuinely remarkable for its niche.

The main gap is mobile development (Android and iOS beyond XcodeBuildMCP) and non-Chrome browsers. But for web, backend, systems, and embedded debugging, the coverage is strong.

**Start here:** If you use VS Code, install [microsoft/DebugMCP](https://github.com/microsoft/DebugMCP). If you need browser debugging, use [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp). If you need multi-language debugging without VS Code, use [debugmcp/mcp-debugger](https://github.com/debugmcp/mcp-debugger). If you're debugging C/C++ binaries, use [stass/lldb-mcp](https://github.com/stass/lldb-mcp) or [pansila/mcp_server_gdb](https://github.com/pansila/mcp_server_gdb).

This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).

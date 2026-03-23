---
title: "Debugging MCP Servers — Chrome DevTools (31K Stars), Microsoft DebugMCP, Multi-Language DAP, GDB/LLDB/WinDbg, x64dbg, PHP Xdebug, Embedded ARM/RISC-V"
date: 2026-03-16T21:00:00+09:00
description: "Debugging MCP servers let AI agents set breakpoints, step through code, inspect variables, and diagnose failures across browsers, IDEs, native binaries, reverse engineering, and embedded hardware. We reviewed 30+ servers across 8 subcategories. Chrome DevTools MCP dominates (31k stars, 29 tools). Microsoft's DebugMCP (263 stars) brings multi-language debugging to VS Code. debugmcp/mcp-debugger (86 stars) supports 6 languages via DAP. x64DbgMCPServer (398 stars) enables AI-driven reverse engineering. Native debugger integration covers GDB, LLDB, JDWP, WinDbg, and embedded ARM/RISC-V. Rating: 4.5/5."
og_description: "Debugging MCP servers: Chrome DevTools (31k stars, 29 tools), x64DbgMCPServer (398 stars), devtools-debugger (341 stars), DebugMCP (263 stars, Microsoft), mcp-debugger (86 stars, 6 languages), lldb-mcp (87 stars), embedded-debugger-mcp (60 stars, ARM/RISC-V), xdebug-mcp (43 stars, PHP), jdwp-mcp (31 stars, Java). 30+ servers reviewed. Rating: 4.5/5."
content_type: "Review"
card_description: "Debugging MCP servers across browser DevTools, VS Code integration, multi-language debuggers, native binary debuggers (GDB/LLDB/WinDbg), reverse engineering (x64dbg), PHP (Xdebug), Java (JDWP), and embedded hardware. Chrome DevTools MCP (31k stars) dominates with 29 tools covering input automation, navigation, performance tracing, network inspection, Lighthouse audits, and DOM snapshots — it's the most-starred MCP server in the debugging space by a wide margin. For IDE-integrated debugging, three strong options exist: jasonjmcghee/claude-debugs-for-you (496 stars, MIT) pioneered the VS Code + MCP debugging pattern with language-agnostic breakpoints and expression evaluation; ScriptedAlchemy/devtools-debugger-mcp (341 stars, MIT) exposes full Chrome DevTools Protocol for Node.js with source map support and conditional breakpoints; microsoft/DebugMCP (263 stars, MIT) provides a first-party VS Code extension supporting 9 languages (Python, JS/TS, Java, C#, C++, Go, Rust, Ruby, PHP) with 14 debugging tools. For multi-language debugging via DAP, debugmcp/mcp-debugger (86 stars, MIT, 1,266+ tests) supports Python, JavaScript, Rust, Go, Java, and Mock through a clean adapter architecture. Reverse engineering gets x64DbgMCPServer (398 stars, C#, x86/x64 binary debugging with direct memory/register/disassembly interaction). Native binary debugging has strong coverage: stass/lldb-mcp (87 stars, BSD-2) and smadi0x86/MDB-MCP (57 stars, GPL-3.0, GDB+LLDB) handle C/C++ and systems-level debugging; LLDB itself has built-in MCP support (lldb_command tool via protocol-server). PHP debugging gets koriym/xdebug-mcp (43 stars, 5 CLI tools plus MCP) wrapping Xdebug 3.x. Java gets navicore/jdwp-mcp (31 stars, Rust, 13 tools via JDWP). Embedded hardware debugging is handled by Adancurusul/embedded-debugger-mcp (60 stars, MIT, Rust) with 22 tools for ARM Cortex-M and RISC-V via probe-rs. XcodeBuildMCP (4.8k stars, MIT) covers iOS/macOS debugging with LLDB integration. The MCP Inspector (9.2k stars, MIT, official) serves as the ecosystem's debugging tool for MCP servers themselves. Crash analysis: tonyredondo/debugger-mcp-server (C#, WinDbg/LLDB, .NET dump analysis, Datadog integration) and mcp-systemd-coredump (Linux coredump analysis via GDB). Gaps: no dedicated Android/ADB debugger MCP, limited .NET debugging outside WinDbg, no dedicated React Native or Flutter debugging MCP. Rating: 4.5/5."
last_refreshed: 2026-03-24
---

**At a glance:** Debugging is one of the highest-leverage uses of MCP — instead of copying error messages into a chat window, a debugging MCP server gives the agent **direct access to the debugger itself**. The ecosystem has matured rapidly and broadly. [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp) (31k stars, 29 tools) lets agents control a live browser. [Microsoft's DebugMCP](https://github.com/microsoft/DebugMCP) (263 stars) brings multi-language debugging into VS Code. [debugmcp/mcp-debugger](https://github.com/debugmcp/mcp-debugger) (86 stars) supports six languages through the Debug Adapter Protocol. [x64DbgMCPServer](https://github.com/AgentSmithers/x64DbgMCPServer) (398 stars) brings AI to reverse engineering. Native debugger servers cover **GDB, LLDB, JDWP, and WinDbg**. Language-specific servers handle **PHP** (Xdebug) and **Java** (JDWP). There's even an embedded hardware debugger for **ARM Cortex-M and RISC-V** microcontrollers. This is the **eighteenth review in our [Developer Tools MCP category](/categories/developer-tools/)**.

The debugging software market ($2.5B in 2023, growing to $7.8B by 2033 at 12.2% CAGR) reflects the universal need for debugging in software development. The broader software development tools market ($6.41B in 2025, growing at 16.12% CAGR to $15.72B by 2031) is growing even faster. AI-powered debugging tools are a key growth driver. The MCP ecosystem's strength across browser, IDE, multi-language, native binary, and embedded debugging makes this one of the most practically useful categories we've reviewed.

**Architecture note:** Debugging MCP servers follow five patterns. **Browser control** (Chrome DevTools MCP) gives agents full browser access — automation, debugging, performance, network. **IDE-integrated** (DebugMCP, claude-debugs-for-you) extend VS Code's debugger to MCP clients, leveraging existing debug adapters. **Protocol-based multi-language** (debugmcp/mcp-debugger) use the Debug Adapter Protocol (DAP) to support many languages through a single server. **Native debugger wrappers** (lldb-mcp, MDB-MCP, gdb-mcp) expose GDB/LLDB/WinDbg commands as MCP tools. **Domain-specific** (embedded-debugger-mcp, x64DbgMCPServer, xdebug-mcp, jdwp-mcp) target specific debugging scenarios with specialized toolsets.

For browser automation and testing (without debugging focus), see our [Playwright](/reviews/playwright-mcp-server/) and [Puppeteer](/reviews/puppeteer-mcp-server/) reviews. For error tracking platforms, see our [Sentry](/reviews/sentry-mcp-server/) and [Datadog](/reviews/datadog-mcp-server/) reviews. For the official MCP server testing tool, the MCP Inspector is covered at the end of this review.

## What's Available

### Browser Debugging — Chrome DevTools (2+ servers)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | 31,000 | TypeScript | — | 29 | Full browser control: automation, debugging, performance, network, Lighthouse |
| [ScriptedAlchemy/devtools-debugger-mcp](https://github.com/ScriptedAlchemy/devtools-debugger-mcp) | 341 | JavaScript/TS | MIT | 18 | Chrome DevTools Protocol for Node.js: breakpoints, stepping, source maps |

**ChromeDevTools/chrome-devtools-mcp** (31k stars) is the official Chrome DevTools MCP server and one of the most-starred MCP servers in existence. It gives AI agents full control over a live Chrome browser — not just debugging, but automation, performance analysis, and network inspection. The 29 tools span input automation (9 tools: click, drag, fill, fill_form, handle_dialog, hover, press_key, type_text, upload_file), navigation (6 tools: close_page, list_pages, navigate_page, new_page, select_page, wait_for), performance analysis (4 tools: performance_analyze_insight, performance_start_trace, performance_stop_trace, take_memory_snapshot), debugging (6 tools: evaluate_script, get_console_message, lighthouse_audit, list_console_messages, take_screenshot, take_snapshot), network (2 tools: get_network_request, list_network_requests), and emulation (2 tools: emulate, resize_page). Chrome M144 Beta adds auto-connection via `--autoConnect` with user permission dialog. A "slim" mode provides just 3 essential tools. Integrates with Cursor, Claude Code, VS Code Copilot, Gemini CLI, and 20+ other platforms. Requires Node.js v20.19+ and Chrome stable. At 31k stars and 1.8k forks, this is one of the most adopted MCP servers in any category.

**ScriptedAlchemy/devtools-debugger-mcp** (341 stars) focuses specifically on **Node.js step-through debugging** via the Chrome DevTools Protocol. It launches Node.js with `--inspect-brk` and provides 18 tools: session management (start_node_debug, stop_debug_session), breakpoint management (set_breakpoint, set_breakpoint_condition, add_logpoint, set_exception_breakpoints), execution controls (resume_execution, step_over, step_into, step_out, continue_to_location, restart_frame), inspection (inspect_scopes, evaluate_expression, get_object_properties, list_call_stack, get_pause_info), and utilities (list_scripts, get_script_source, blackbox_scripts, read_console). Source map support for TypeScript debugging. This is the server for AI agents that need to step through server-side JavaScript/TypeScript code.

### VS Code Debugging (3 servers)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [jasonjmcghee/claude-debugs-for-you](https://github.com/jasonjmcghee/claude-debugs-for-you) | 496 | TypeScript | MIT | 5+ | Language-agnostic VS Code debugging via MCP + extension |
| [microsoft/DebugMCP](https://github.com/microsoft/DebugMCP) | 263 | TypeScript | MIT | 14 | Official Microsoft VS Code extension, 9 languages |
| [workbackai/mcp-nodejs-debugger](https://github.com/workbackai/mcp-nodejs-debugger) | 303 | JavaScript | — | 7+ | Node.js runtime debugging for Cursor/Claude Code (archived) |

**jasonjmcghee/claude-debugs-for-you** (496 stars) pioneered the VS Code + MCP debugging pattern. It's a VS Code extension plus MCP server that enables any LLM to interactively debug any language — as long as VS Code supports it via `launch.json`. The agent can set breakpoints, evaluate expressions, and step through code in the debugger console. It supports stdio and SSE transport and works with Claude Desktop, Continue, and Cursor. Language-agnostic design is the key advantage — if VS Code can debug it, this server can expose it to an AI agent.

**microsoft/DebugMCP** (263 stars) is Microsoft's first-party answer. It's a VS Code extension (requires VS Code 1.104.0+) that embeds an MCP server exposing 14 debugging tools: get_debug_instructions, start_debugging, stop_debugging, step_over, step_into, step_out, continue_execution, restart_debugging, add_breakpoint, remove_breakpoint, clear_all_breakpoints, list_breakpoints, get_variables_values, evaluate_expression. It supports 9 languages: Python, JavaScript/TypeScript, Java, C/C++, Go, Rust, PHP, Ruby, and C#/.NET. It integrates with GitHub Copilot, Cline, Cursor, Roo Code, and Windsurf. Runs 100% locally with no external data transmission. Works with remote SSH, Codespaces, and WSL. MCP endpoint at `http://localhost:3001/mcp`.

**workbackai/mcp-nodejs-debugger** (303 stars) was a popular Node.js debugging MCP server designed for Cursor and Claude Code, using `--inspect` mode for runtime breakpoints and variable inspection. It was **archived in January 2026** — likely made redundant by Microsoft's DebugMCP and the broader debugging MCP ecosystem. Still usable but no longer maintained.

### Multi-Language Debugging via DAP (1 server)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [debugmcp/mcp-debugger](https://github.com/debugmcp/mcp-debugger) | 86 | TypeScript | MIT | 18 | 6 languages via DAP: Python, JS, Rust, Go, Java, Mock |

**debugmcp/mcp-debugger** (86 stars, v0.18.1) is the most ambitious multi-language debugging server. It uses the Debug Adapter Protocol (DAP) to support **Python** (via debugpy), **JavaScript/Node.js** (via Microsoft's js-debug, bundled), **Rust** (via CodeLLDB on Linux/macOS), **Go** (via Delve), **Java** (via JDI bridge, launch/attach modes), and **Mock** (for testing). The 18 tools include: create_debug_session, list_debug_sessions, list_supported_languages, set_breakpoint, start_debugging, attach_to_process, detach_from_process, get_stack_trace, get_scopes, get_variables, get_local_variables, step_over, step_into, step_out, continue_execution, pause_execution, evaluate_expression, get_source_context, close_debug_session. It has 1,266+ tests passing across end-to-end scenarios. Ships via Docker (`debugmcp/mcp-debugger:latest`) with bundled adapters, or `npx @debugmcp/mcp-debugger` with zero runtime dependencies. If you need one debugging server for multiple languages and don't want VS Code integration, this is the choice.

### Language-Specific Debugging — PHP, Python, Java (3 servers)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [samefarrar/mcp-pdb](https://github.com/samefarrar/mcp-pdb) | 45 | Python | MIT | 8 | Python's pdb debugger via MCP, pytest support |
| [koriym/xdebug-mcp](https://github.com/koriym/xdebug-mcp) | 43 | PHP | — | 5 | PHP debugging via Xdebug 3.x with profiling and coverage |
| [navicore/jdwp-mcp](https://github.com/navicore/jdwp-mcp) | 31 | Rust | MIT | 13 | Java debugging via JDWP: attach, breakpoints, threads, evaluate |

**samefarrar/mcp-pdb** (45 stars) wraps Python's built-in pdb debugger as an MCP server. Tools include `start_debug`, `send_pdb_command`, `set_breakpoint`, `clear_breakpoint`, `examine_variable`, `get_debug_status`, `list_breakpoints`, `restart_debug`, and `end_debug`. It supports both direct Python file debugging and pytest-based debugging, with automatic virtual environment detection and breakpoint restoration between sessions. Requires Python 3.12+. **Security note:** this executes Python code through the debugger — use in trusted environments only.

**koriym/xdebug-mcp** (43 stars, v0.8.0) enables AI-powered PHP debugging through Xdebug 3.x. Five CLI tools work independently of MCP/plugins: **xstep** (breakpoint debugging and variable inspection), **xtrace** (execution flow analysis), **xprofile** (performance profiling), **xback** (call stack examination), and **xcoverage** (code coverage analysis). Also integrates as MCP server for Cursor/Windsurf. Includes interactive REPL debugger. Docker/Podman/Kubectl compatible. Supports legacy PHP 5.x and 7.x debugging via compatible Xdebug versions. Stateless CLI architecture optimized for AI consumption.

**navicore/jdwp-mcp** (31 stars) is the only Java-specific debugging MCP server. Written in Rust (99.5%) for performance, it connects to JVMs via the Java Debug Wire Protocol (JDWP). 13 tools: debug.attach, debug.set_breakpoint, debug.list_breakpoints, debug.clear_breakpoint, debug.continue, debug.step_over, debug.step_into, debug.step_out, debug.get_stack (with variables), debug.evaluate, debug.list_threads, debug.pause, debug.disconnect. No IDE dependency — connects directly to any JVM running with `-agentlib:jdwp` flag.

### Native Binary Debugging — GDB, LLDB, WinDbg (5+ servers)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [stass/lldb-mcp](https://github.com/stass/lldb-mcp) | 87 | Python | BSD-2 | 20+ | Full LLDB integration: breakpoints, watchpoints, memory, disassembly, threads |
| [pansila/mcp_server_gdb](https://github.com/pansila/mcp_server_gdb) | 62 | Rust | MIT | 10+ | Fast GDB/MI bridge, multi-session, TUI inspection |
| [smadi0x86/MDB-MCP](https://github.com/smadi0x86/MDB-MCP) | 57 | Python | GPL-3.0 | 5+ | Unified GDB + LLDB interface with auto-detection |
| [tonyredondo/debugger-mcp-server](https://github.com/tonyredondo/debugger-mcp-server) | 2 | C# | MIT | 11 | Cross-platform WinDbg/LLDB, .NET dump analysis, Datadog integration |
| [hnmr293/gdb-mcp](https://github.com/hnmr293/gdb-mcp) | 4 | Python | Apache-2.0 | 4 | GDB with CLI + MI modes, built-in command reference resources |

LLDB also has **native MCP support** built directly into the LLDB debugger itself (documented at [lldb.llvm.org/use/mcp.html](https://lldb.llvm.org/use/mcp.html)). Start via `protocol-server start MCP listen://localhost:59999` — exposes a single `lldb_command` tool that accepts any LLDB command plus `lldb://debugger/<id>` and `lldb://debugger/<id>/target/<index>` resources. This means AI agents can execute LLDB commands without any third-party server.

**stass/lldb-mcp** (87 stars) is the most feature-complete standalone LLDB server. 20+ tools across 7 categories: session management (lldb_start, lldb_terminate, lldb_list_sessions), program loading (lldb_load, lldb_attach, lldb_load_core), execution control (lldb_run, lldb_continue, lldb_step, lldb_next, lldb_finish, lldb_kill), breakpoints/watchpoints (lldb_set_breakpoint, lldb_breakpoint_list, lldb_breakpoint_delete, lldb_watchpoint), inspection (lldb_backtrace, lldb_print, lldb_examine, lldb_info_registers, lldb_frame_info, lldb_disassemble, lldb_process_info), thread management (lldb_thread_list, lldb_thread_select), and miscellaneous (lldb_command, lldb_expression, lldb_help). Supports multiple simultaneous sessions with auto-cleanup on shutdown.

**pansila/mcp_server_gdb** (62 stars) is a Rust implementation of a GDB/MI protocol bridge — fast and cross-platform with concurrent multi-session support. Features include debug control (run, pause, step, step-over), breakpoint management, stack frames, local variables, registers, and memory inspection. Supports both stdio and SSE transport. Includes a TUI for observing agent behavior.

**smadi0x86/MDB-MCP** (57 stars) provides a unified interface to both GDB and LLDB with automatic debugger detection. Useful when you want one MCP server that works on both Linux (GDB) and macOS (LLDB) without configuration changes. Includes example binaries for arm64 and amd64.

**tonyredondo/debugger-mcp-server** (2 stars but 361 commits) is a sophisticated C# implementation covering WinDbg on Windows and LLDB on Linux/macOS. Its standout feature is **.NET dump analysis** — crash analysis, .NET runtime inspection, performance profiling, security scanning, and dump comparison. 11 MCP tools: session, dump, analyze, compare, report, watch, inspect, symbols, source_link, datadog_symbols, exec. Includes Datadog trace symbols integration and HTTP API alongside MCP. Docker support included. Requires .NET 10 SDK.

### Reverse Engineering / Binary Analysis (1 server)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [AgentSmithers/x64DbgMCPServer](https://github.com/AgentSmithers/x64DbgMCPServer) | 398 | C# | — | 10+ | x64dbg plugin: memory, registers, disassembly, threads for AI-driven RE |

**AgentSmithers/x64DbgMCPServer** (398 stars) is a plugin for x64dbg (the popular open-source Windows debugger for x86/x64 binaries) that exposes debugging capabilities via MCP. Self-hosted HTTP interface at `http://127.0.0.1:50300/sse` without ASP.NET Core dependency. Commands include ExecuteDebuggerCommand, ReadMemAtAddress, WriteMemToAddress, ReadDismAtAddress, CommentOrLabelAtAddress, GetAllRegisters, GetLabel, GetAllActiveThreads, GetAllModulesFromMemMap, GetCallStack. Supports Cursor (direct SSE), Claude Desktop (via MCPProxy), Windsurf, and Gemini. Plugin reload without debugger restart. Requires .NET Framework 4.7.2. Last updated March 2026 — actively maintained. This is the only MCP server for reverse engineering workflows.

### Embedded Hardware Debugging (1 server)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [Adancurusul/embedded-debugger-mcp](https://github.com/Adancurusul/embedded-debugger-mcp) | 60 | Rust | MIT | 22 | ARM Cortex-M & RISC-V via probe-rs, real hardware validated |

**Adancurusul/embedded-debugger-mcp** (60 stars) brings MCP debugging to embedded microcontrollers. Using probe-rs, it supports ARM Cortex-M (M0, M0+, M3, M4, M7, M23, M33) and RISC-V targets with 22 tools: probe management (list_probes, connect, probe_info), memory operations (read_memory, write_memory), debug control (halt, run, reset, step), breakpoint management (set_breakpoint, clear_breakpoint), flash operations (flash_erase, flash_program, flash_verify), RTT bidirectional communication (rtt_attach, rtt_detach, rtt_channels, rtt_read, rtt_write, run_firmware), and session management (get_status, disconnect). Validated on real STM32G431CBTx hardware. Supports J-Link, ST-Link V2/V3, DAPLink, Black Magic Probe, and FTDI-based probes. If you're doing embedded development with AI assistance, it's the only game in town.

### Xcode / iOS Debugging (1 server)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [cameroncooke/XcodeBuildMCP](https://github.com/cameroncooke/XcodeBuildMCP) | 4,800 | TypeScript | MIT | 10+ | iOS/macOS build, debug, and deploy with LLDB integration |

**XcodeBuildMCP** (4.8k stars) is primarily a build tool for iOS/macOS projects, but it includes debugging capabilities — attaching the debugger, setting breakpoints, inspecting variables, and executing LLDB commands from AI agents. It works with Cursor, Claude Code, VS Code, and even Xcode itself. Requires macOS 14.5+ and Xcode 16.x+. AgentAudit security certified.

### Crash Analysis (2 servers)

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [tonyredondo/debugger-mcp-server](https://github.com/tonyredondo/debugger-mcp-server) | 2 | C# | MIT | 11 | .NET dump analysis, WinDbg/LLDB, Datadog symbols |
| [signal-slot/mcp-systemd-coredump](https://github.com/signal-slot/mcp-systemd-coredump) | 2 | JavaScript | MIT | 7 | Linux coredump analysis via systemd-coredump + GDB |

**mcp-systemd-coredump** (2 stars) transforms Linux crash analysis into a conversational workflow. 7 tools: list_coredumps, get_coredump_info, extract_coredump, remove_coredump, get_coredump_config, set_coredump_enabled, get_stacktrace (via GDB integration). Two URI-based resources: `coredump:///<id>` for JSON metadata and `stacktrace:///<id>` for formatted trace output. Requires Node.js 18+, systemd-coredump, coredumpctl, and GDB.

### MCP Server Debugging — The Inspector

| Server | Stars | Language | License | Tools | Key Feature |
|--------|-------|----------|---------|-------|-------------|
| [modelcontextprotocol/inspector](https://github.com/modelcontextprotocol/inspector) | 9,200 | TypeScript | MIT | — | Official visual testing tool for MCP servers |

The **MCP Inspector** (9.2k stars) deserves mention in any debugging review because it's the tool you use to debug MCP servers themselves. It's a React-based web UI + Node.js proxy that connects to any MCP server via stdio, SSE, or Streamable HTTP. You can test tools, explore resources, and inspect raw JSON-RPC messages. Run via `npx @modelcontextprotocol/inspector`. It includes a CLI mode for CI/CD automation, Docker support, session token authentication, and DNS rebinding protection. If you're building or troubleshooting any MCP server, the Inspector is essential.

## Developer Tools MCP — Cross-Category Comparison

| Aspect | GitHub | GitLab | Bitbucket | Docker | Kubernetes | CI/CD | IDE/Editor | Testing/QA | Monitoring | Security | IaC | Packages | Code Gen | API Dev | Logging | DB Migration | Doc Tooling | Debugging |
|--------|--------|--------|-----------|--------|------------|-------|------------|------------|------------|----------|-----|----------|----------|---------|---------|--------------|-------------|-----------|
| **Official MCP server** | Yes (28.2k stars, 21 toolsets) | Yes (built-in, 15 tools, Premium+) | No (Jira/Confluence only) | [Hub MCP (132 stars, 12+ tools)](/reviews/docker-mcp-servers/) | No (Red Hat leads, 1.3k stars) | Yes (Jenkins, CircleCI, Buildkite) | Yes (JetBrains built-in, 24 tools) | Yes (MS Playwright, 9.8k stars, 24 tools) | Yes (Grafana 2.5k, Datadog, Sentry, Dynatrace, New Relic, Instana) | Yes (Semgrep, SonarQube, Snyk, Trivy, GitGuardian, Cycode, Contrast) | Yes (Terraform 1.3k, Pulumi remote, AWS IaC, OpenTofu 84) | Yes (NuGet built-in VS 2026, Homebrew built-in) | Partial (Vercel next-devtools 694, E2B 384, JetBrains built-in server) | Yes (Postman 192, Apollo GraphQL 275, Kong deprecated, Apigee, MuleSoft) | Yes (Splunk 13 tools GA, Grafana Tempo built-in, Grafana Loki 103 stars) | Partial (Liquibase private preview, Prisma built-in CLI) | Yes (Microsoft Learn 1.5k, Mintlify auto, ReadMe per-project, Stainless, OpenAI Docs) | Yes (Chrome DevTools 31k, Microsoft DebugMCP 263, MCP Inspector 9.2k official) |
| **Top community server** | GitMCP (7.8k stars) | zereight/gitlab-mcp (1.2k stars) | aashari (132 stars) | [ckreiling (691 stars, 25 tools)](/reviews/docker-mcp-servers/) | Flux159 (1.4k stars, 20+ tools) | Argo CD (356 stars, 12 tools) | vscode-mcp-server (342 stars, 15 tools) | executeautomation (5.3k stars) | pab1it0/prometheus (340 stars) | CodeQL community (143 stars) | Ansible (25 stars, 40+ tools) | mcp-package-version (122 stars, 9 registries) | Context7 (50.3k stars), magic-mcp (4.5k stars) | openapi-mcp-generator (495 stars), mcp-graphql (374 stars) | cr7258/elasticsearch (259 stars), Traceloop OTel (178 stars) | mpreziuso/mcp-atlas (Atlas), defrex/drizzle-mcp (Drizzle) | GitMCP (7.8k stars), Grounded Docs (1.2k stars) | claude-debugs-for-you (496 stars), x64DbgMCPServer (398 stars), devtools-debugger (341 stars) |
| **Primary function** | Repository operations | Repository operations | Repository operations | Container lifecycle | Cluster management | Pipeline management | Editor integration | Test execution | Observability queries | Vulnerability scanning | Infrastructure provisioning | Dependency intelligence | Context provision + UI generation | Spec-to-server conversion + API interaction | Log search/analysis + trace correlation | Schema migration & version control | Doc access, search, generation & quality | Breakpoints, stepping, variable inspection, crash analysis |
| **Vendor count** | 1 (GitHub) | 1 (GitLab) | 0 (Atlassian via Jira only) | 1 (Docker) + community | 0 (Red Hat leads community) | 3 (Jenkins, CircleCI, Buildkite) | 1 (JetBrains) | 1 (Microsoft) | 6 (Grafana, Datadog, Sentry, Dynatrace, New Relic, Instana) | 7+ (Semgrep, SonarQube, Snyk, Trivy, GitGuardian, Cycode, Contrast) | 5+ (HashiCorp, Pulumi, AWS, OpenTofu, Spacelift) | 2 (Microsoft/NuGet, Homebrew) | 3 (Vercel, E2B, Upstash/Context7) | 4+ (Postman, Apollo, Kong, Google/Apigee, MuleSoft) | 6+ (Splunk, Grafana/Loki, Grafana/Tempo, Coralogix, Axiom, Mezmo) | 2 (Liquibase, Prisma) + Google partial | 5+ (Microsoft, Mintlify, ReadMe, Stainless, OpenAI, Vonage, Fern, Apidog) | 3 (Google/Chrome DevTools, Microsoft/DebugMCP, LLVM/LLDB built-in) |
| **Code generation role** | Context (repos, issues, PRs) | Context (repos, issues, MRs) | Context (repos, PRs) | Context (images, containers) | Context (cluster state) | Context (pipeline status) | Bidirectional (tools + context) | Context (test results) | Context (metrics, logs) | Context (vulnerabilities) | Generation (IaC templates) | Context (versions, advisories) | Direct (UI components, docs, execution) | Bidirectional (spec-to-tools, API execution) | Context (log patterns, traces, errors) | Bidirectional (migration generation + schema inspection) | Context (doc access/search) + Generation (doc output) | Bidirectional (set breakpoints + inspect state) |
| **Authentication** | PAT / GitHub App | OAuth 2.0 / PAT | App Password / OAuth | Docker Desktop credentials | kubeconfig / OAuth / OIDC | API tokens per platform | Local connection (port/stdio) | None (local browsers) | API tokens / OAuth (remote) | API tokens / CLI auth | API tokens / OAuth / CLI auth | None (public registries) | API keys (Context7, magic-mcp, E2B) | API keys / Bearer / OAuth / 1Password | API tokens / OAuth / RBAC (Splunk) | Database credentials / API keys | None (GitMCP, MS Learn) / API keys (platform MCP) | None (local debuggers) / Chrome DevTools auto-connect |
| **AAIF membership** | No (but Microsoft is Platinum) | No | No | [Gold](/reviews/docker-mcp-servers/) | No (but Google/AWS/MS are Platinum) | No | No (but Microsoft is Platinum) | No (but Microsoft is Platinum) | No | No | No | No (but Microsoft is Platinum) | No | No | No | No | No (but Microsoft is Platinum) | No (but Google/Microsoft are Platinum) |
| **Platform users** | 180M+ developers | 30M+ users | ~41k companies | 20M+ users | 5.6M developers | Jenkins: 11.3M devs | VS Code: 75.9% market share | Playwright: 45.1% QA adoption | Datadog: 32.7k customers | SonarQube: 17.7% SAST mindshare | Terraform: millions of users, 45% IaC adoption | npm: 5B+ weekly downloads | Copilot: 20M+ users, Cursor: 1M+ DAU | Postman: 30M+ users, REST: ~83% of web APIs | Splunk: 15k+ customers, ELK: most-deployed log stack | Flyway: 10.7k stars, Liquibase: 5.2k stars, Prisma: 43k stars | Mintlify: 28k+ stars, Docusaurus: 60k+ stars | Chrome: 65%+ browser share, VS Code: 75.9% IDE share, x64dbg: 45k+ stars |
| **Our rating** | [4.5/5](/reviews/github-mcp-server/) | [3.5/5](/reviews/gitlab-mcp-server/) | [2.5/5](/reviews/bitbucket-mcp-server/) | [4/5](/reviews/docker-mcp-servers/) | [4/5](/reviews/kubernetes-mcp-servers/) | [3/5](/reviews/ci-cd-mcp-servers/) | [3.5/5](/reviews/ide-code-editor-mcp-servers/) | [3.5/5](/reviews/testing-qa-mcp-servers/) | [4/5](/reviews/monitoring-observability-mcp-servers/) | [3.5/5](/reviews/security-scanning-mcp-servers/) | [4/5](/reviews/infrastructure-as-code-mcp-servers/) | [3/5](/reviews/package-management-mcp-servers/) | [3.5/5](/reviews/code-generation-mcp-servers/) | [3.5/5](/reviews/api-development-mcp-servers/) | [3.5/5](/reviews/logging-tracing-mcp-servers/) | [2.5/5](/reviews/database-migration-mcp-servers/) | [3.5/5](/reviews/documentation-tooling-mcp-servers/) | 4.5/5 |

## Known Issues

1. **Chrome DevTools MCP conflates debugging with automation** — At 31k stars and 29 tools, Chrome DevTools MCP is the category leader, but only ~6 of its 29 tools are debugging-specific (evaluate_script, console messages, Lighthouse, screenshots, snapshots). The rest are input automation and navigation. Agents using it for debugging get a massive tool surface where most tools aren't relevant to the debugging task, increasing token cost and reducing accuracy.

2. **No dedicated Android/ADB debugger MCP** — Android has ~3.3 billion active devices, but no MCP server exposes ADB debugging commands (logcat, breakpoints, memory profiling, layout inspector). Android Studio's debugger has no MCP integration. Java debugging via debugmcp/mcp-debugger or jdwp-mcp can handle JVM logic but not Android-specific debugging (activity lifecycle, intent inspection, resource analysis).

3. **VS Code debugging fragmentation** — Three competing VS Code debugging MCP servers (claude-debugs-for-you, DebugMCP, mcp-nodejs-debugger) with different capabilities, different language support, and different maintenance states. mcp-nodejs-debugger is archived. DebugMCP is Microsoft's first-party answer but has fewer stars than the community pioneer. Users must evaluate three options for the same use case.

4. **No .NET step debugger** — C#/.NET debugging is only available through multi-language servers (DebugMCP, debugmcp/mcp-debugger) or WinDbg dump analysis (tonyredondo). No dedicated .NET MCP server provides the equivalent of Visual Studio's rich .NET debugging experience — no LINQ debugging, no async debugging visualization, no Entity Framework query inspection.

5. **Browser debugging is Chrome-only** — Firefox DevTools, Safari Web Inspector, and Edge DevTools have no MCP integration. Chrome DevTools MCP works because Chrome exposes the Chrome DevTools Protocol (CDP). Firefox has its own Remote Debugging Protocol (RDP) with no MCP bridge. Web developers testing cross-browser behavior get no AI assistance outside Chrome.

6. **Reverse engineering MCP servers are Windows-only** — x64DbgMCPServer (398 stars) is the only significant reverse engineering MCP server, and it requires x64dbg (Windows-only, .NET Framework 4.7.2). No Ghidra MCP server, no IDA Pro MCP server, no radare2/rizin MCP server. Binary analysis on macOS/Linux has no dedicated MCP support beyond GDB/LLDB wrappers.

7. **Security implications of debugging MCP servers are underaddressed** — Debugging MCP servers execute code, read memory, inspect variables, and attach to processes. Most document no security model. mcp-pdb's README warns about trusted environments, but most servers (including DebugMCP and mcp-debugger) make no security claims. An MCP client with debugging access has effectively arbitrary code execution capability.

8. **No remote debugging support** — Most debugging MCP servers assume local execution. Debugging a production issue on a remote server, a Kubernetes pod, or a cloud function requires manual setup. tonyredondo/debugger-mcp-server supports Docker/remote connections, but the mainstream servers (DebugMCP, mcp-debugger, chrome-devtools-mcp) are local-only.

9. **Embedded debugging coverage stops at hardware access** — embedded-debugger-mcp (60 stars) provides excellent low-level access (memory, flash, RTT), but no RTOS-aware debugging (FreeRTOS task inspection, Zephyr thread analysis), no peripheral register visualization, no power profiling. The gap between "can read memory" and "can debug an embedded application" is significant.

10. **No React Native / Flutter / cross-platform mobile debugging** — React Native's Hermes debugger, Flutter's Dart DevTools, and Expo's development tools have no MCP integration. Cross-platform mobile development (used by 42% of mobile developers) gets zero dedicated debugging MCP support. The only mobile debugging path is XcodeBuildMCP for iOS-native projects.

## Bottom Line

**Rating: 4.5 out of 5**

Debugging MCP servers are among the most practically impactful in the entire MCP ecosystem — one of our highest ratings across all Developer Tools categories. [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp) (31k stars, 29 tools) provides comprehensive browser control. [Microsoft's DebugMCP](https://github.com/microsoft/DebugMCP) and [claude-debugs-for-you](https://github.com/jasonjmcghee/claude-debugs-for-you) bring IDE-integrated debugging to VS Code across 9+ languages. [debugmcp/mcp-debugger](https://github.com/debugmcp/mcp-debugger) covers six languages via DAP without IDE dependency. [x64DbgMCPServer](https://github.com/AgentSmithers/x64DbgMCPServer) (398 stars) uniquely enables AI-driven reverse engineering. Native debugger servers handle C/C++ and systems programming through GDB, LLDB (including built-in MCP support), and WinDbg. Language-specific servers cover PHP (Xdebug) and Java (JDWP). The embedded hardware debugger is genuinely remarkable for its niche.

The **4.5/5 rating** reflects: exceptional breadth across browser, IDE, multi-language, native binary, reverse engineering, embedded, and language-specific debugging; strong vendor investment (Google/Chrome, Microsoft, LLVM/LLDB built-in); Chrome DevTools MCP being one of the most-starred MCP servers in any category; practical utility that directly improves AI-assisted development workflows. Points are lost for Chrome-only browser debugging, no Android/ADB debugging, Windows-only reverse engineering, underaddressed security implications, and no cross-platform mobile debugging (React Native/Flutter).

**Who benefits from debugging MCP servers today:**

- **Web developers** — [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp) provides AI agents with full browser control for debugging, performance analysis, and network inspection
- **VS Code users** — Install [microsoft/DebugMCP](https://github.com/microsoft/DebugMCP) for multi-language debugging across Python, JS/TS, Java, C#, C++, Go, Rust, Ruby, and PHP
- **Polyglot developers** — [debugmcp/mcp-debugger](https://github.com/debugmcp/mcp-debugger) supports 6 languages through a single server without IDE dependency
- **Systems programmers** — [stass/lldb-mcp](https://github.com/stass/lldb-mcp) or [pansila/mcp_server_gdb](https://github.com/pansila/mcp_server_gdb) for C/C++ binary debugging
- **Reverse engineers** — [x64DbgMCPServer](https://github.com/AgentSmithers/x64DbgMCPServer) for AI-assisted binary analysis on Windows
- **Embedded developers** — [embedded-debugger-mcp](https://github.com/Adancurusul/embedded-debugger-mcp) for ARM Cortex-M and RISC-V debugging
- **PHP developers** — [koriym/xdebug-mcp](https://github.com/koriym/xdebug-mcp) for Xdebug-powered debugging with profiling and coverage

**Who should wait:**

- **Android developers** — No ADB or Android Studio debugging MCP server exists
- **Cross-browser testers** — Firefox and Safari have no debugging MCP integration
- **React Native / Flutter developers** — No cross-platform mobile debugging MCP server
- **Security-sensitive environments** — Most debugging MCP servers document no security model despite having arbitrary code execution capability

---

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official announcements. Information is current as of March 2026. See our [About page](/about/) for details on our review process.*

# Terminal & CLI Tools MCP Servers — Shell Execution, tmux, SSH, and MCP Inspectors

> Terminal and CLI tools MCP servers let AI agents execute shell commands, manage terminal sessions, connect to remote servers via SSH, and inspect MCP servers from the command line.


Terminal and CLI tools MCP servers let AI agents execute shell commands, manage persistent terminal sessions, connect to remote servers via SSH, and inspect MCP servers from the command line. Instead of copy-pasting commands or switching between terminal windows, AI assistants can directly operate in the shell environment.

This review covers **terminal-focused MCP servers** — shell execution, tmux integration, SSH remote access, and MCP CLI inspectors. For related servers, see our [Desktop Automation review](/reviews/desktop-automation-rpa-mcp-servers/), [Configuration Management review](/reviews/configuration-management-mcp-servers/), and [Container, Docker & Kubernetes review](/reviews/container-docker-kubernetes-mcp-servers/).

The headline findings: **Two major gaps filled since our initial review** — process management (systemd + supervisord) and PowerShell-native MCP servers now exist. **MCP CLI inspectors exploded** — wong2/mcp-cli surged 274% to 430 stars, the official inspector hit 9,500 stars. **Security remains the defining challenge** for shell execution, with the best servers using allowlists, flag validation, and audit trails. **tmux integration is the most active subcategory** with 8+ competing servers including a new Rust implementation. **SSH management is production-ready** with bvisible/mcp-ssh-manager at 146 stars and 37 tools.

**Category:** [Developer Tools](/categories/developer-tools/)

## Shell Execution

### tumf/mcp-shell-server — Most Popular Shell Execution Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-shell-server](https://github.com/tumf/mcp-shell-server) | 170 | Python | — | 3+ |

**The most-starred dedicated shell execution MCP server** — provides a practical security model for AI-controlled command execution:

- **Command allowlist/blocklist** — specify which commands are permitted or forbidden
- **Timeout control** — set maximum execution time to prevent runaway processes
- **Validated execution** — commands after shell operators (`;`, `&&`, `||`, `|`) are also checked against the allowlist
- **Bridge model** — functions as a secure bridge between AI agents and the operating system

Good default choice for teams that want controlled shell access without the complexity of full tmux integration.

### MladenSU/cli-mcp-server — Whitelisted Commands with Flag Validation

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cli-mcp-server](https://github.com/MladenSU/cli-mcp-server) | 170 | Python | — | 2+ |

**The most granular security controls** — goes beyond command allowlists to validate individual flags:

- **Command whitelisting** — only specified commands can run (e.g., `ls,cat,pwd,echo`), or use `ALLOWED_COMMANDS=all`
- **Flag whitelisting** — only specified flags are allowed (e.g., `-l,-a,--help,--version`), or use `ALLOWED_FLAGS=all`
- **Path validation** — commands execute only within allowed directories
- **Shell operator blocking** — `&&`, `|`, `>`, `>>` blocked by default, enable with `ALLOW_SHELL_OPERATORS=true`
- **Environment variable config** — all security policies set via env vars for easy Docker/CI integration

Strongest choice when you need fine-grained control over exactly what an AI agent can do in the shell.

### sonirico/mcp-shell — Secure Go-Based Shell with Audit Trail

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-shell](https://github.com/sonirico/mcp-shell) | 26 | Go | — | 2+ |

**Strictest security model available** — built on the official MCP SDK for Go (mark3labs/mcp-go):

- **Secure mode** — disables shell interpretation entirely, uses executable allowlist only, blocks injection completely
- **Legacy mode** — shell execution with allowlist/blocklist by command string (for backwards compatibility)
- **Audit trail** — complete command execution log with JSON output and execution metadata
- **Docker isolation** — designed to run in a lightweight container for additional security
- **Configurable policies** — security file controls allowed commands, blocked commands, max execution time, working directory

Best option for security-conscious environments where audit logging and injection prevention are non-negotiable.

### blazickjp/shell-mcp-server — Cross-Platform Shell Execution

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [shell-mcp-server](https://github.com/blazickjp/shell-mcp-server) | — | Python | — | 2+ |

**Cross-platform shell execution** with directory-scoped access:

- **Multi-shell support** — bash, sh, cmd, and powershell
- **Timeout control** — configurable execution time limits
- **Unix and Windows** — works on both platforms
- **Directory scoping** — controlled shell access within specified directories

Useful if you need to support both Unix and Windows environments from a single MCP server.

### egoist/shell-command-mcp — Minimal Shell Execution

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [shell-command-mcp](https://github.com/egoist/shell-command-mcp) | — | TypeScript | — | 1+ |

**Minimal approach** — a single tool for executing shell commands. No allowlists, no complex configuration. Useful for trusted environments where security constraints are handled at a different layer.

## Persistent Terminal Sessions (tmux)

### nickgnd/tmux-mcp — Most Popular tmux MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [tmux-mcp](https://github.com/nickgnd/tmux-mcp) | 233 | TypeScript | — | 6+ |

**The most-starred tmux MCP server** — provides full tmux session lifecycle management:

- **Session control** — create, list, and close tmux sessions
- **Command execution** — send commands to specific sessions and panes
- **Output reading** — view terminal output from any session
- **Window/pane management** — rename windows and panes, get current session info
- **Easy install** — run via `npx` with no manual setup required

The default choice for adding persistent terminal sessions to AI assistants. Active development with community contributions for features like consecutive command execution.

### lox/tmux-mcp-server — Lightweight Go tmux Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [tmux-mcp-server](https://github.com/lox/tmux-mcp-server) | — | Go | — | 6+ |

**Lightweight Go implementation** for teams that prefer compiled binaries over Node.js:

- **stdio-based** — communicates via standard I/O for simple integration
- **Session management** — start, view, list, join, and close sessions
- **Command sending** — send commands to specific tmux sessions
- **Performance** — Go binary with lower memory footprint than Node.js alternatives

Good alternative to nickgnd/tmux-mcp if you want a Go-based solution.

### TNTisdial/persistent-shell-mcp — Workspace Abstraction on tmux

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [persistent-shell-mcp](https://github.com/TNTisdial/persistent-shell-mcp) | — | TypeScript | — | 4+ |

**Workspace-level abstraction** on top of tmux:

- **Automatic session management** — creates, destroys, and monitors workspaces seamlessly
- **Multiple workspaces** — manage separate environments for different tasks
- **tmux-based persistence** — sessions survive disconnections and can be resumed

Useful when you need to manage multiple concurrent terminal environments as named workspaces.

### wehnsdaefflae/terminal-control-mcp — Agent-Controlled Timing

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [terminal-control-mcp](https://github.com/wehnsdaefflae/terminal-control-mcp) | — | Python | — | 4+ |

**Designed for interactive commands** where timing matters:

- **Raw stream capture** — uses tmux pipe-pane for capturing terminal output as it happens
- **Agent-controlled timing** — no automatic timeouts, the AI agent decides when to read output
- **Session persistence** — long-running sessions with automatic cleanup and monitoring
- **Flexible content modes** — different ways to capture and present terminal content

Stands out for interactive use cases where the AI agent needs to watch output in real-time and decide when to proceed.

### bnomei/tmux-mcp — Rust-Based tmux with Multi-Client Support

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [tmux-mcp](https://github.com/bnomei/tmux-mcp) | — | Rust | — | 8+ |

**NEW — Rust-based tmux MCP server** with broad AI client support:

- **Multi-client support** — works with Claude Code, Codex CLI, OpenCode, and Amp
- **Isolated socket** — uses dedicated tmux socket (`tmux -L`) to avoid interfering with user sessions
- **Full tmux control** — create sessions, split panes, rename windows/panes, list windows/panes
- **Real-time observation** — user/developer can attach to the same session to watch or participate
- **SSH compatible** — works with human-created sessions, including remote setups over SSH

Strong choice if you want a compiled, low-overhead tmux server that works across multiple AI coding clients.

### Other tmux Servers

- **[kazuph/mcp-tmux](https://github.com/kazuph/mcp-tmux)** — alternative tmux MCP implementation
- **[jonrad/tmux-mcp](https://github.com/jonrad/tmux-mcp)** — focused on controlling tmux sessions via AI
- **[MediocreTriumph/tmux-mcp](https://github.com/MediocreTriumph/tmux-mcp)** — cross-platform (Windows WSL, Linux, macOS) terminal control via AI
- **[JinchengGao-Infty/agent-mux](https://github.com/JinchengGao-Infty/agent-mux)** — tmux-backed agent pool for orchestrating interactive CLI agents

## SSH / Remote Terminal

### bvisible/mcp-ssh-manager — Comprehensive DevOps SSH Platform

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-ssh-manager](https://github.com/bvisible/mcp-ssh-manager) | 146 | TypeScript | — | 37 |

**The most comprehensive SSH MCP server** — 37 tools organized into 6 groups:

- **Command execution** — run commands on remote servers with output capture
- **File transfer** — upload/download files between local and remote systems
- **Database operations** — automated backups for MySQL, PostgreSQL, MongoDB with smart scheduling and cron integration
- **Health monitoring** — server health checks and status monitoring
- **SSH key support** — key authentication, passphrase-protected keys, SSH agent compatibility
- **Context optimization** — 92% context reduction in minimal mode (5 tools vs 37)
- **Interactive wizard** — configure which tool groups to enable for your specific workflow

Available via npm (`mcp-ssh-manager`). Compatible with Claude Code and OpenAI Codex. April 2026 update fixed global installation and added CLI binary registration. Best choice for DevOps teams managing remote infrastructure.

### 1999AZZAR/terminal-mcp-server — Local + Remote with Session Persistence

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [terminal-mcp-server](https://github.com/1999AZZAR/terminal-mcp-server) | — | Python | — | 3+ |

**Unified local and remote execution** with robustness features:

- **Dual mode** — execute commands locally or on remote hosts via SSH
- **Session persistence** — reuses terminal environment for a configurable duration (default 20 minutes)
- **Automatic retry** — connection health checks and automatic reconnection for SSH
- **Connection pooling** — efficient management of multiple SSH connections
- **Security features** — command validation and dangerous pattern detection

Good for workflows that mix local and remote command execution in the same session.

### tufantunc/ssh-mcp — Basic SSH Control

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ssh-mcp](https://github.com/tufantunc/ssh-mcp) | — | TypeScript | — | 2+ |

**Simple SSH control** for Linux and Windows servers:

- **Remote execution** — execute shell commands on remote hosts
- **Multi-platform** — supports both Linux and Windows targets
- **SSH key or password** — flexible authentication options
- **Timeout control** — configurable command execution timeout

Minimalist option when you just need basic remote command execution without the complexity of a full DevOps platform.

### weidwonder/terminal-mcp-server — Configurable Remote Sessions

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [terminal-mcp-server](https://github.com/weidwonder/terminal-mcp-server) | — | TypeScript | — | 3+ |

**Remote terminal with environment management**:

- **Session reuse** — maintains terminal state for a configurable period
- **Environment variables** — persistence across sessions
- **Working directory management** — maintain context across commands
- **Local and remote** — supports both modes

## MCP CLI Inspectors & Tools

### f/mcptools — Most Capable MCP CLI

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcptools](https://github.com/f/mcptools) | — | Go | — | CLI |

**The Swiss Army knife for MCP server development and debugging** — not an MCP server itself, but an essential CLI tool for the MCP ecosystem:

- **Server inspection** — list tools, resources, and prompts from any MCP server
- **Tool calling** — call MCP tools directly from the command line
- **Interactive shell** — persistent connection to an MCP server for multiple commands in sequence
- **Proxy mode** — register shell scripts or inline commands as MCP tools (unique capability)
- **Mock server** — create mock MCP servers for testing
- **Multi-transport** — supports both stdio and HTTP transport
- **Easy install** — available via Homebrew (`brew tap f/mcptools && brew install mcp`)

The most powerful CLI for working with MCP servers. The proxy mode is particularly innovative — it lets you wrap any command-line tool as an MCP server without writing code.

### wong2/mcp-cli — CLI Inspector with OAuth

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-cli](https://github.com/wong2/mcp-cli) | 430 | JavaScript | GPL-3.0 | CLI |

**Focused MCP server inspector**:

- **Dynamic discovery** — discover available tools, resources, and prompts from any server
- **Multi-source** — connect via NPM packages, local Node.js files, HTTP URLs, or SSE
- **OAuth support** — authenticate with SSE and streamable HTTP servers
- **Tool calling** — call tools with or without arguments from the command line
- **Token efficiency** — dynamic discovery reduces token usage from ~47,000 to ~400 tokens

### modelcontextprotocol/inspector — Official Visual Testing Tool

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [inspector](https://github.com/modelcontextprotocol/inspector) | 9,500 | TypeScript | MIT | Web UI |

**The official MCP debugging tool** from the protocol maintainers — now at 9,500 stars, making it by far the most popular tool in this category:

- **React web UI** — interactive visual interface for testing MCP servers (MCPI client)
- **Protocol bridge** — Node.js proxy (MCPP) connecting the web UI to servers via stdio, SSE, or streamable-http
- **Zero install** — run directly via `npx @modelcontextprotocol/inspector`
- **Full protocol support** — test tools, resources, prompts, and sampling
- **v0.21.2** — latest release adds proxy fetch for auth, sanitized error responses to prevent stack trace exposure

The reference tool for MCP server development. Not a CLI per se, but the web-based counterpart to f/mcptools.

### apify/mcpc — Universal MCP CLI Client

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcpc](https://github.com/apify/mcpc) | — | TypeScript | — | CLI |

**NEW — The most feature-rich MCP CLI client**, going beyond inspection to full client functionality:

- **Persistent sessions** — lightweight bridge process maintains connection and state across commands
- **OAuth 2.1 support** — full authentication for HTTP-based MCP servers
- **Interactive shell** — discovery and testing of MCP servers in a persistent session
- **JSON code mode** — structured output for programmatic use by AI coding agents
- **Proxy mode** — works inside AI sandboxes and restricted environments
- **x402 payment protocol** — machine-to-machine payments via USDC on Base blockchain (no API token needed)

A significant step up from simple inspectors — mcpc is a universal MCP client designed for real workflows, not just debugging.

## Multi-Tool & Bridges

### inercia/MCPShell — Shell Scripts as MCP Tools

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [MCPShell](https://github.com/inercia/MCPShell) | 58 | Go | — | Dynamic |

**Turns any shell script into an MCP tool** (58 stars) — a bridge between shell scripting and the MCP protocol:

- **YAML-based tool definitions** — configure tools with parameters and constraints in YAML
- **CEL expression constraints** — security through Common Expression Language validation before execution
- **Parameter substitution** — flexible command execution with parameter passing
- **Secure execution** — controlled bridge between LLMs and operating system commands
- **Dynamic tools** — the number of tools depends on how many scripts you register

Similar to f/mcptools' proxy mode, but designed as a standalone MCP server rather than a CLI tool. v0.1.4 available.

### sammcj/mcp-devtools — Modular Developer Tools

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-devtools](https://github.com/sammcj/mcp-devtools) | — | TypeScript | — | Multiple |

**Modular collection of developer tools** for AI coding agents — provides commonly used utilities in a single MCP server rather than requiring separate installations.

## Process Management (NEW)

### openSUSE/systemd-mcp — systemd Service Control

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [systemd-mcp](https://github.com/openSUSE/systemd-mcp) | — | Python | — | 6 |

**NEW — FILLS A GAP we identified in our initial review.** Official openSUSE project providing MCP access to systemd:

- **Unit management** — list units with filtering by states or patterns, list installed unit files
- **Service control** — start, stop, restart, reload, enable, disable units
- **Log access** — get recent log entries for any service or unit
- **Restart monitoring** — check reload/restart status and timeouts
- **File access** — read system files with pagination for large configs
- **Man page access** — retrieve man pages with section/chapter filtering
- **polkit/dbus auth** — proper authorization when running over stdio

The first MCP server to wrap a major process manager. Particularly valuable for DevOps teams managing Linux servers through AI assistants.

### aether-platform/supervisord-mcp — Supervisord Process Control

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [supervisord-mcp](https://github.com/aether-platform/supervisord-mcp) | — | Python | — | 6+ |

**NEW — Complements systemd-mcp** for environments using Supervisord:

- **Process control** — start, stop, restart managed processes
- **Status monitoring** — list all processes and their current states
- **Log viewing** — configurable log access for monitored processes
- **Config reload** — reload Supervisord configuration without restart
- **PyPI installable** — `pip install supervisord-mcp`
- **stdio transport** — secure, direct communication with AI agents

Together with systemd-mcp, this completely fills the process management gap we identified in March.

## PowerShell & Windows (NEW)

### yotsuda/PowerShell.MCP — Universal PowerShell MCP Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [PowerShell.MCP](https://github.com/yotsuda/PowerShell.MCP) | — | PowerShell | — | Dynamic |

**NEW — FILLS A GAP we identified.** Universal MCP server giving AI access to the entire PowerShell ecosystem:

- **10,000+ modules** — one installation exposes the full PowerShell module ecosystem to AI
- **CLI tool access** — any command-line tool available through the same interface
- **Shared console** — user and AI collaborate in the same console with full transparency
- **Cross-platform** — supports Windows, Linux, and macOS
- **Works with Claude Code** and other MCP-compatible clients

The PowerShell-native MCP server we said was missing. Particularly valuable for Windows-centric DevOps and sysadmin workflows.

### fernandomenuk/wmux — tmux for Windows with MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [wmux](https://github.com/fernandomenuk/wmux) | — | TypeScript/Rust | — | Dynamic |

**NEW — Addresses limited Windows support** by bringing tmux-like functionality to Windows natively:

- **Tauri desktop app** — native Windows app with WebView UI for split panes and tabbed workspaces
- **MCP server** — TypeScript MCP server with named pipe bridge
- **JSON-RPC socket API** — agents can spawn terminals, send commands, and read output programmatically
- **PTY management** — proper pseudo-terminal support via wmux-core

The first serious attempt at bringing terminal multiplexing + MCP to Windows without requiring WSL.

## What's Missing

The terminal/CLI MCP ecosystem has closed two of its biggest gaps since March, but some remain:

- **No terminal emulator integration** — no MCP server provides native integration with modern terminal emulators (Ghostty, WezTerm, Kitty, Alacritty). Despite Ghostty reaching 45,000+ stars and WezTerm offering a built-in multiplexer, you can't control or observe terminal emulator features through MCP.
- **No unified terminal orchestrator** — no single server combines shell execution, session persistence, SSH access, and output streaming. You still need 2-3 servers for a complete terminal workflow.
- ~~**No process management**~~ — **FILLED.** openSUSE/systemd-mcp and aether-platform/supervisord-mcp now cover the two most popular process managers.
- ~~**No PowerShell-native MCP**~~ — **FILLED.** yotsuda/PowerShell.MCP provides access to 10,000+ PowerShell modules.
- ~~**Limited Windows support**~~ — **PARTIALLY FILLED.** wmux brings native Windows terminal multiplexing with MCP, and PowerShell.MCP is cross-platform. The ecosystem is still Linux-heavy but no longer Linux-only.

## The Verdict

**Rating: 4/5** (up from 3.5) — The terminal/CLI MCP ecosystem filled two of its biggest gaps since March — process management and PowerShell — and saw explosive growth in CLI inspectors (wong2/mcp-cli +274%, official inspector at 9,500 stars). The category is maturing from fragmented small projects into a functional ecosystem.

**For shell execution,** tumf/mcp-shell-server and MladenSU/cli-mcp-server are now tied at 170 stars each — pick based on whether you want simpler allowlists (tumf) or per-flag whitelisting (MladenSU).

**For persistent sessions,** nickgnd/tmux-mcp (233 stars) remains the leader. The new bnomei/tmux-mcp (Rust) is worth watching for its multi-client support across Claude Code, Codex CLI, OpenCode, and Amp.

**For SSH/remote access,** bvisible/mcp-ssh-manager (146 stars) continues to be the most complete DevOps SSH solution with 37 tools.

**For MCP debugging,** the ecosystem has exploded — modelcontextprotocol/inspector (9,500 stars) is the visual standard, wong2/mcp-cli (430 stars) leads CLI inspection, and apify/mcpc adds persistent sessions and OAuth 2.1 for production workflows.

**For process management,** openSUSE/systemd-mcp and aether-platform/supervisord-mcp are new but fill a critical gap for server administration.

**For Windows/PowerShell,** yotsuda/PowerShell.MCP and fernandomenuk/wmux finally give Windows users first-class MCP terminal tools.

The remaining gaps — terminal emulator integration and a unified orchestrator — would take this category to 4.5 or 5, but the current ecosystem is now functional enough for most terminal workflows.

*Reviewed 2026-03-16, refreshed 2026-04-28. Stars and features reflect the state at refresh time. AI-researched, not hands-on tested — [read our methodology](/about/).*

*This review was last edited on 2026-04-28 using Claude Opus 4.6 (Anthropic).*


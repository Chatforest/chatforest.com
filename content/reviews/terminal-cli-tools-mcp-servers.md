---
title: "Terminal & CLI Tools MCP Servers — Shell Execution, tmux, SSH, and MCP Inspectors"
date: 2026-03-16T12:00:00+09:00
description: "Terminal and CLI tools MCP servers let AI agents execute shell commands, manage terminal sessions, connect to remote servers via SSH, and inspect MCP servers from the command line. We reviewed 25+ servers across 5 subcategories. Shell execution: tumf/mcp-shell-server (156 stars, Python — allowlist/blocklist, timeout control), MladenSU/cli-mcp-server (134 stars, Python — whitelisted commands with flag validation), sonirico/mcp-shell (23 stars, Go — secure mode with no shell injection, audit trail). Persistent sessions: nickgnd/tmux-mcp (233 stars, TypeScript — tmux session control, most popular), lox/tmux-mcp-server (Go — stdio-based, lightweight), TNTisdial/persistent-shell-mcp (tmux-based workspace management), wehnsdaefflae/terminal-control-mcp (raw stream capture, agent-controlled timing). SSH/Remote: bvisible/mcp-ssh-manager (37 tools in 6 groups — DevOps automation, database backups, health monitoring), 1999AZZAR/terminal-mcp-server (local + SSH, session persistence, retry logic), tufantunc/ssh-mcp (Linux/Windows SSH control), mixelpixx/SSH-MCP (VPS access for Claude Desktop). MCP CLI inspectors: f/mcptools (Go — CLI for MCP servers, proxy mode, mock servers, Homebrew install), wong2/mcp-cli (115 stars, JavaScript — OAuth, multi-transport), modelcontextprotocol/inspector (official visual testing tool, npx install). Multi-tool: sammcj/mcp-devtools (modular developer tools for coding agents), inercia/MCPShell (shell scripts as MCP tools). Gaps: no unified terminal manager across local+remote, no Windows Terminal/PowerShell-specific MCP, no terminal emulator integration (Ghostty/WezTerm/Kitty), limited process management. 25+ servers across 5 subcategories. Rating: 3.5/5."
og_description: "Terminal MCP servers: tumf/mcp-shell-server (156 stars — allowlist/blocklist), nickgnd/tmux-mcp (233 stars — tmux control), MladenSU/cli-mcp-server (134 stars — whitelisted commands), bvisible/mcp-ssh-manager (37 tools, DevOps automation), f/mcptools (Go CLI). 25+ servers reviewed. Rating: 3.5/5."
content_type: "Review"
card_description: "Terminal and CLI tools MCP servers for AI-powered command execution, terminal session management, SSH remote access, and MCP protocol inspection. **Shell execution servers focus on security** — the core challenge of giving AI agents shell access is preventing command injection and limiting blast radius. tumf/mcp-shell-server (156 stars, Python) leads with a practical approach: allowlists and blocklists for commands, timeout control for long-running processes, and validated execution. MladenSU/cli-mcp-server (134 stars, Python) takes security further with per-command flag whitelisting — you specify both allowed commands AND allowed flags, with shell operators blocked by default. sonirico/mcp-shell (23 stars, Go) offers the strictest security model: a 'secure mode' that disables shell interpretation entirely, executing commands directly to prevent injection, plus a complete audit trail. blazickjp/shell-mcp-server provides cross-platform support (bash/sh/cmd/powershell) with directory-scoped access. egoist/shell-command-mcp keeps it minimal with a simple execute tool. **tmux integration is the most active subcategory** — persistent terminal sessions solve the key limitation of one-shot shell commands: state doesn't persist between calls. nickgnd/tmux-mcp (233 stars, TypeScript) is the most popular, providing full tmux session lifecycle management — create sessions, send commands, read output, list and close sessions. lox/tmux-mcp-server (Go) takes a lighter approach with stdio communication. TNTisdial/persistent-shell-mcp adds workspace abstraction on top of tmux for managing multiple concurrent environments. wehnsdaefflae/terminal-control-mcp stands out with raw stream capture via tmux pipe-pane and agent-controlled timing without automatic timeouts — useful for interactive commands. kazuph/mcp-tmux and jonrad/tmux-mcp provide additional alternatives with different feature focuses. **SSH remote management is production-ready** — bvisible/mcp-ssh-manager is the most comprehensive SSH MCP server with 37 tools organized into 6 groups, covering command execution, file transfer, database operations (automated backups for MySQL/PostgreSQL/MongoDB), and health monitoring. It offers 92% context reduction when using minimal mode (5 tools vs 37). 1999AZZAR/terminal-mcp-server handles both local and SSH-remote execution with session persistence, automatic retry, and connection pooling. tufantunc/ssh-mcp provides basic SSH control for Linux and Windows servers. weidwonder/terminal-mcp-server adds configurable environment variables and working directory management for remote sessions. **MCP CLI inspectors let you debug servers from the terminal** — f/mcptools (Go) is the most capable MCP CLI: list tools/resources/prompts, call capabilities, interactive shell mode with persistent connections, proxy mode to register shell scripts as MCP tools, and mock server mode for testing. Installs via Homebrew. wong2/mcp-cli (115 stars, JavaScript) focuses on server discovery and inspection with OAuth support for SSE and streamable HTTP servers. modelcontextprotocol/inspector is the official visual testing tool from the MCP team — a React web UI with a Node.js proxy bridge supporting stdio, SSE, and streamable-http transports. **Gaps remain in integration and platform coverage** — no MCP server provides native integration with modern terminal emulators (Ghostty, WezTerm, Kitty, Alacritty). No Windows Terminal or PowerShell-specific MCP exists. Process management (systemd, supervisord) is not covered. No unified terminal manager handles both local and remote sessions through one interface. The category would benefit from a 'terminal orchestrator' that combines shell execution, session persistence, SSH access, and output streaming in a single server."
last_refreshed: 2026-03-16
---

Terminal and CLI tools MCP servers let AI agents execute shell commands, manage persistent terminal sessions, connect to remote servers via SSH, and inspect MCP servers from the command line. Instead of copy-pasting commands or switching between terminal windows, AI assistants can directly operate in the shell environment.

This review covers **terminal-focused MCP servers** — shell execution, tmux integration, SSH remote access, and MCP CLI inspectors. For related servers, see our [Desktop Automation review](/reviews/desktop-automation-rpa-mcp-servers/), [Configuration Management review](/reviews/configuration-management-mcp-servers/), and [Container, Docker & Kubernetes review](/reviews/container-docker-kubernetes-mcp-servers/).

The headline findings: **Security is the defining challenge** — giving AI agents shell access is powerful but dangerous, and the best servers use allowlists, flag validation, and audit trails. **tmux integration is the most active subcategory** with 6+ competing servers. **SSH management is surprisingly mature** with bvisible/mcp-ssh-manager offering 37 tools across 6 groups.

## Shell Execution

### tumf/mcp-shell-server — Most Popular Shell Execution Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-shell-server](https://github.com/tumf/mcp-shell-server) | 156 | Python | — | 3+ |

**The most-starred dedicated shell execution MCP server** — provides a practical security model for AI-controlled command execution:

- **Command allowlist/blocklist** — specify which commands are permitted or forbidden
- **Timeout control** — set maximum execution time to prevent runaway processes
- **Validated execution** — commands after shell operators (`;`, `&&`, `||`, `|`) are also checked against the allowlist
- **Bridge model** — functions as a secure bridge between AI agents and the operating system

Good default choice for teams that want controlled shell access without the complexity of full tmux integration.

### MladenSU/cli-mcp-server — Whitelisted Commands with Flag Validation

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cli-mcp-server](https://github.com/MladenSU/cli-mcp-server) | 134 | Python | — | 2+ |

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
| [mcp-shell](https://github.com/sonirico/mcp-shell) | 23 | Go | — | 2+ |

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

### Other tmux Servers

- **[kazuph/mcp-tmux](https://github.com/kazuph/mcp-tmux)** — alternative tmux MCP implementation
- **[jonrad/tmux-mcp](https://github.com/jonrad/tmux-mcp)** — focused on controlling tmux sessions via AI

## SSH / Remote Terminal

### bvisible/mcp-ssh-manager — Comprehensive DevOps SSH Platform

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-ssh-manager](https://github.com/bvisible/mcp-ssh-manager) | — | TypeScript | — | 37 |

**The most comprehensive SSH MCP server** — 37 tools organized into 6 groups:

- **Command execution** — run commands on remote servers with output capture
- **File transfer** — upload/download files between local and remote systems
- **Database operations** — automated backups for MySQL, PostgreSQL, MongoDB with smart scheduling and cron integration
- **Health monitoring** — server health checks and status monitoring
- **SSH key support** — key authentication, passphrase-protected keys, SSH agent compatibility
- **Context optimization** — 92% context reduction in minimal mode (5 tools vs 37)
- **Interactive wizard** — configure which tool groups to enable for your specific workflow

Available via npm (`mcp-ssh-manager`). Compatible with Claude Code and OpenAI Codex. Best choice for DevOps teams managing remote infrastructure.

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
| [mcp-cli](https://github.com/wong2/mcp-cli) | 115 | JavaScript | — | CLI |

**Focused MCP server inspector**:

- **Dynamic discovery** — discover available tools, resources, and prompts from any server
- **Multi-source** — connect via NPM packages, local Node.js files, HTTP URLs, or SSE
- **OAuth support** — authenticate with SSE and streamable HTTP servers
- **Tool calling** — call tools with or without arguments from the command line
- **Token efficiency** — dynamic discovery reduces token usage from ~47,000 to ~400 tokens

### modelcontextprotocol/inspector — Official Visual Testing Tool

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [inspector](https://github.com/modelcontextprotocol/inspector) | — | TypeScript | — | Web UI |

**The official MCP debugging tool** from the protocol maintainers:

- **React web UI** — interactive visual interface for testing MCP servers
- **Protocol bridge** — Node.js proxy connecting the web UI to servers via stdio, SSE, or streamable-http
- **Zero install** — run directly via `npx @modelcontextprotocol/inspector`
- **Full protocol support** — test tools, resources, prompts, and sampling

The reference tool for MCP server development. Not a CLI per se, but the web-based counterpart to f/mcptools.

## Multi-Tool & Bridges

### inercia/MCPShell — Shell Scripts as MCP Tools

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [MCPShell](https://github.com/inercia/MCPShell) | — | Go | — | Dynamic |

**Turns any shell script into an MCP tool** — a bridge between shell scripting and the MCP protocol:

- **Script registration** — register shell scripts or commands as MCP tools
- **Secure execution** — controlled bridge between LLMs and operating system commands
- **Dynamic tools** — the number of tools depends on how many scripts you register

Similar to f/mcptools' proxy mode, but designed as a standalone MCP server rather than a CLI tool.

### sammcj/mcp-devtools — Modular Developer Tools

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [mcp-devtools](https://github.com/sammcj/mcp-devtools) | — | TypeScript | — | Multiple |

**Modular collection of developer tools** for AI coding agents — provides commonly used utilities in a single MCP server rather than requiring separate installations.

## What's Missing

The terminal/CLI MCP ecosystem has notable gaps:

- **No terminal emulator integration** — no MCP server provides native integration with modern terminal emulators (Ghostty, WezTerm, Kitty, Alacritty). You can't control or observe terminal emulator features through MCP.
- **No Windows Terminal / PowerShell-specific MCP** — while blazickjp/shell-mcp-server supports cmd/powershell, there's no PowerShell-native MCP server with cmdlet discovery, module management, or PSObject support.
- **No process management** — no MCP server wraps systemd, supervisord, or similar process managers. You can't manage services, view logs, or control daemons through MCP.
- **No unified terminal orchestrator** — no single server combines shell execution, session persistence, SSH access, and output streaming. You need 2-3 servers for a complete terminal workflow.
- **Limited Windows support** — the ecosystem is overwhelmingly Unix/Linux-focused.

## The Verdict

**Rating: 3.5/5** — The terminal/CLI MCP ecosystem is functional and surprisingly mature in specific subcategories (tmux and SSH), but fragmented across many small servers rather than consolidated into comprehensive solutions.

**For shell execution,** start with tumf/mcp-shell-server (156 stars) for its practical security model, or MladenSU/cli-mcp-server (134 stars) if you need per-flag whitelisting.

**For persistent sessions,** nickgnd/tmux-mcp (233 stars) is the clear leader — most popular, actively maintained, and easy to install via npx.

**For SSH/remote access,** bvisible/mcp-ssh-manager's 37 tools make it the most complete DevOps SSH solution available through MCP.

**For MCP debugging,** f/mcptools is the most capable CLI tool, especially its unique proxy mode. The official modelcontextprotocol/inspector provides the visual alternative.

The category is held back by fragmentation and a Unix-centric focus. A unified terminal server that combines shell execution, tmux sessions, SSH access, and cross-platform support would immediately become the default choice — but it doesn't exist yet.

*Reviewed 2026-03-16. Stars and features reflect the state at review time. AI-researched, not hands-on tested — [read our methodology](/about/).*

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*

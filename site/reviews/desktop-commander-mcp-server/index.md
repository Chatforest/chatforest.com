# Desktop Commander MCP Server — Full Terminal and File Control for AI Agents

> Desktop Commander gives AI agents terminal access, diff-based file editing, and filesystem search — the power tool for developers who want their agent to do more than read files.


Part of our **[Developer Tools MCP category](/categories/developer-tools/)**.

*At a glance: 6,100 GitHub stars, 712 forks, 509 commits, 20 contributors, last commit May 14 2026 (v0.2.41), npm v0.2.41, 22+ tools, MIT license, ~26,000 npm downloads/week, PulseMCP ~1.3M all-time visitors (#57 globally, ~8,100 weekly). Solo maintainer (Eduard Ruzga) with growing team. Standalone Desktop Commander App live with freemium model ($7/mo Pro).*

Desktop Commander MCP is the power tool that the official [Filesystem MCP server](/reviews/filesystem-mcp-server/) never aspired to be. Where the official server gives you careful, sandboxed file operations, Desktop Commander gives your AI agent a terminal, persistent process management, diff-based code editing, and full filesystem access. It's what you get when you answer "yes" to every permission prompt.

Built by Eduard Ruzga (wonderwhy-er on GitHub) and maintained at [wonderwhy-er/DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP), it has become one of the most popular community MCP servers with nearly 6,000 GitHub stars and close to a million npm downloads in its first year. It's particularly popular among Claude Desktop and Cursor users who want their agent to actually *do things* rather than just read and suggest.

## What It Does

The server exposes 22+ tools organized across five categories:

**Terminal & Process Management**
- `start_process` — execute terminal commands with configurable timeout and background execution
- `read_process_output` — read output with offset/length pagination to prevent context overflow
- `interact_with_process` — send input to running processes (SSH sessions, database REPLs, interactive CLIs)
- `force_terminate` — force-kill a process by PID
- `list_sessions` — list active terminal sessions
- `list_processes` — list all running processes
- `kill_process` — kill a process by PID

**Filesystem Operations**
- `read_file` — read text files, Excel, PDF, DOCX, and even URLs (with negative offset for tail-like reads)
- `read_multiple_files` — batch read multiple files at once
- `write_file` — write or append to files
- `write_pdf` — create and modify PDFs from markdown
- `create_directory` — create directories
- `list_directory` — recursive directory listing with configurable depth
- `move_file` — move and rename files
- `get_file_info` — file metadata

**Code Editing**
- `edit_block` — surgical text replacement using old_string/new_string diffs, plus structured range rewrites for Excel files

**Search**
- `start_search` — search files or content using ripgrep, with regex and literal search support
- `get_more_search_results` — paginate through search results
- `stop_search` / `list_searches` — manage active searches

**Configuration & Meta**
- `get_config` / `set_config_value` — runtime configuration management
- `get_usage_stats` — usage statistics
- `get_recent_tool_calls` — audit log of recent tool calls

The key differentiator is **persistent terminal sessions**. When your agent runs `start_process`, the process stays alive between tool calls. Your agent can start a dev server, check its output later, interact with database REPLs, chain SSH sessions — things that are impossible with one-shot command execution. The `read_process_output` tool uses offset-based pagination to avoid flooding the context window with terminal output, which is a practical design choice other servers often miss.

Desktop Commander also handles **non-text files** that most MCP servers ignore: native Excel (.xlsx/.xls/.xlsm) read/write/edit/search, PDF creation and modification, and DOCX read/edit with surgical XML editing. It can even execute code in memory (Python, Node.js, R) without saving files to disk.

## Setup

**One-command install:**

```bash
npx @wonderwhy-er/desktop-commander@latest setup
```

This auto-configures Claude Desktop. For manual setup:

```json
{
  "mcpServers": {
    "desktop-commander": {
      "command": "npx",
      "args": ["-y", "@wonderwhy-er/desktop-commander@latest"]
    }
  }
}
```

Also available via Smithery, Docker (recommended for security), bash script installer (macOS), or local git clone. Six installation methods total, four with auto-updates.

**Requirements:** Node.js. Works on macOS, Windows, and Linux.

## What's Good

**Persistent terminal sessions are transformative.** The ability to start a process, do other work, then come back and read its output changes what an AI agent can realistically accomplish. Start a build, investigate test failures, interact with a REPL — these are natural developer workflows that other MCP servers can't support. The offset-based output pagination prevents context window flooding.

**Diff-based editing is precise.** The `edit_block` tool uses old_string/new_string replacement — the same approach Claude Code uses internally. This is more reliable than line-number-based editing and less wasteful than rewriting entire files. It works well for targeted code changes.

**Rich file format support.** Excel, PDF, and DOCX support is genuinely useful and rare in MCP servers. Most servers treat everything as text. Desktop Commander lets your agent work with office documents natively.

**Search is fast.** Built on ripgrep, the search tools support regex, literal matching, file filtering, and result pagination. Starting a search returns immediately with initial results; you can fetch more as needed.

**Active development.** v0.2.41 shipped May 14 with a symlink traversal security fix, Excel range syntax (`SheetName!A1:B2`), improved Windows stability, and `list_directory` distinction between NOT_FOUND and DENIED. v0.2.40 (April 27) patched a critical markdown corruption bug in the new WYSIWYG editor. 509 commits, 20 contributors, community engagement strong with an active Discord.

**Remote MCP capability.** Running `npx @wonderwhy-er/desktop-commander@latest remote` enables the server to be used from ChatGPT, Claude web, and other AI clients via OAuth — expanding beyond Claude Desktop and local IDE setups.

**Audit logging.** Every tool call is logged with 10MB rotation. The `get_recent_tool_calls` tool lets you review what your agent has been doing — helpful when you're granting this level of access.

## What's Not

**Security is explicitly not a priority.** The project's own SECURITY.md states: "Security is not currently our top priority." This is unusually honest and unusually concerning. Desktop Commander gives AI agents unrestricted terminal and filesystem access. The guardrails that exist — directory restrictions, command blocking — are explicitly acknowledged as bypassable:

- Directory restrictions can be bypassed via symlinks and terminal commands
- Command blocking can be bypassed via substitution and absolute paths
- Terminal commands can access files outside `allowedDirectories`

**Security progress, but critical holes remain.** Three of the eight previously flagged vulnerabilities are now closed: SSRF in URL fetching (#410, closed April 19), path validation fail-open (#419, fixed April 7), and the symlink sandbox escape (#420, fixed in v0.2.41 May 11 via PR #398 resolving symlinks before allowlist checks). Progress. But five remain open, including three command-injection bypasses (#421, #422, #423 — CVSS 9.8 for #422), missing network tool blocking (#412), and hardcoded credentials in source (#416). The maintainer's response to #416 was dismissive ("not really an issue").

**Maintainer is transparent but selective on security.** The symlink fix came promptly after a researcher filed a clear reproduction case. The command-injection cluster has been open longer with no merge path in sight — the blocklist model is fundamentally fragile and the maintainer knows it. Docker isolation remains the official recommendation for security-sensitive work.

**111 open issues, 20 open PRs.** Issue backlog grew from 80 to 111 (+31) in four weeks. Bug reports include Windows hanging behavior, file read returning empty content, and MCP approval not persisting.

**Commit frequency has recovered.** The April concern about only 5 commits in four weeks has reversed: v0.2.39 (April 23), v0.2.40 (April 27), and v0.2.41 (May 14) shipped in quick succession. The standalone app focus appears to be complementing the MCP server, not replacing it.

**Behavioral instruction in tool description.** Issue #384 flagged that tool descriptions contain behavioral instructions that could influence agent behavior — a known attack vector in the MCP ecosystem (see AgentSeal's research on prompt injection via tool descriptions).

## How It Compares

| Feature | Desktop Commander | Filesystem MCP | Claude Code (built-in) | Shell MCP |
|---------|------------------|----------------|----------------------|-----------|
| **Maintained** | Community (solo) | Official (Anthropic) | Official (Anthropic) | Community |
| **Terminal access** | Yes (persistent) | No | Yes | Yes (one-shot) |
| **Diff editing** | Yes | No | Yes | No |
| **File operations** | Full | Full (sandboxed) | Full | No |
| **Search** | ripgrep | No | ripgrep | No |
| **Excel/PDF/DOCX** | Yes | No | No | No |
| **Security model** | Guardrails (bypassable) | Allowlist (enforced) | Sandboxed | None |
| **Stars** | 6,100 | 84K (monorepo) | N/A | Varies |
| **npm downloads/week** | ~26,000 | 173K | N/A | Varies |

Desktop Commander essentially replicates much of what Claude Code does natively — terminal access, diff editing, file operations, search — but exposes it to *any* MCP client. If you're already using Claude Code, you already have these capabilities built in. Desktop Commander's value is bringing this power to Claude Desktop, Cursor, and other MCP clients that lack native terminal integration.

The [Filesystem MCP server](/reviews/filesystem-mcp-server/) is the safer alternative if you only need file operations. It enforces directory allowlists at the server level, not just as bypassable guardrails. But it can't run commands or manage processes.

## The Bigger Picture

Desktop Commander represents the tension at the heart of the MCP ecosystem: power versus safety. The server is popular precisely because it removes the guardrails — it lets AI agents do what developers actually want them to do. Start builds, run tests, interact with databases, edit code surgically. These are real workflows that sandboxed file-only servers can't support.

The security story remains genuinely concerning. The maintainer's official position is still "security is not our top priority," and 5 of 8 originally flagged vulnerabilities remain open. The recommendation to use Docker for security-sensitive work is reasonable — containerization provides the hard boundary that the server's built-in guardrails don't. But most users installing via `npx` aren't setting up Docker containers.

The standalone Desktop Commander App is now live and commercialized — free tier (100 messages/week), Pro at $7/month, bring-your-own-API-key option. The app supports any AI model and uses remote MCP to talk back to the server. The commercial layer appears to be funding continued MCP server development rather than replacing it. Three security fixes in the past four weeks suggest the security backlog is being addressed, just selectively.

The 1.3M PulseMCP visitors and 6,100 GitHub stars make Desktop Commander one of the most visible community MCP servers. The ~26,000 npm downloads/week is a significant jump from ~10,800 four weeks ago — suggesting real adoption growth, possibly driven by the app's launch or remote MCP feature.

Worth watching: whether the command-injection cluster (#421–#423) gets resolved now that structural fixes have landed, and how the 111-issue backlog trends.

## Rating: 3.5/5

Desktop Commander earns a 3.5/5 for being the most capable local development MCP server available — persistent terminal sessions, diff-based editing, rich file format support, and fast search in a single package. Three meaningful security fixes landed in four weeks and development pace has recovered. But five critical vulnerabilities remain open (including CVSS 9.8 command injection), the issue backlog grew 38% in a month (80→111), and the blocklist-based security model is acknowledged as fundamentally fragile. Rating holds: use this if you want maximum agent capability and understand the tradeoffs; Docker isolation is still the right call for security-sensitive work.

**Use this if:** You want your AI agent to have full developer capabilities — terminal, editing, search, process management — and you understand the security tradeoffs. Best paired with Docker for isolation.

**Skip this if:** You need enforced security boundaries, work in a shared environment, or are already using Claude Code (which provides similar capabilities with better sandboxing built in).

*This review was researched and written by an AI agent (Claude Sonnet 4.6, Anthropic). We did not hands-on test this server — our analysis is based on public documentation, GitHub repositories, npm data, and community reports. Last edited 2026-05-19.*


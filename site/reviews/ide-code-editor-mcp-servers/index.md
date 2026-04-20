# IDE & Code Editor MCP Servers — Your Editor as an AI-Accessible Tool

> JetBrains is the only major IDE with a built-in MCP server (24 tools since 2025.2). VS Code has community servers (juehang 342 stars, 15 tools; acomagu 113 stars, 13 tools).


**At a glance:** Most IDEs are MCP *clients* — they connect to external servers for AI capabilities. But a growing ecosystem flips this: **IDEs as MCP servers**, exposing editor capabilities to external AI agents. **JetBrains is the only major IDE with a built-in MCP server** (24 tools since version 2025.2, across IntelliJ, PyCharm, WebStorm, Android Studio). VS Code has community extensions: [juehang/vscode-mcp-server](https://github.com/juehang/vscode-mcp-server) (342 stars, TypeScript, 15 tools) and [acomagu/vscode-as-mcp-server](https://github.com/acomagu/vscode-as-mcp-server) (113 stars, TypeScript, 13 tools). Neovim has [mcp-neovim-server](https://github.com/bigcodegen/mcp-neovim-server) (301 stars, TypeScript, 19 tools) exposing vim-native operations. With **VS Code holding 75.9% developer market share** and **GitHub Copilot surpassing 20 million users**, IDE MCP servers represent a strategic layer: letting external AI agents (Claude Code, Claude Desktop, custom agents) control your editor rather than just running inside it. This is the **seventh review in our [Developer Tools MCP category](/categories/developer-tools/)**.

The typical MCP flow for coding is: your IDE connects to external MCP servers (GitHub, databases, documentation) and pulls context into your coding workflow. IDE-as-MCP-server inverts this — an external AI agent connects to your running IDE and uses its capabilities: code analysis, symbol lookup, refactoring, debugging, and terminal execution. This matters because IDE code intelligence (type checking, error detection, symbol resolution) is often better than what a standalone AI agent can derive from reading raw files. An AI agent that can ask your IDE "what errors does this file have?" gets IntelliJ's full inspection engine, not just a regex over the source.

**Architecture note:** IDE MCP servers divide into two types: **built-in** (JetBrains ships the server as part of the IDE, no extension needed) and **community extensions** (VS Code, Neovim extensions that add MCP server capabilities). The built-in approach has deeper integration — JetBrains exposes code analysis, refactoring, and run configurations that extension-based servers can't easily replicate. Extension-based servers are limited to what the editor's extension API exposes.

## What's Available

### JetBrains — Built-in MCP Server (2025.2+)

| Aspect | Detail |
|--------|--------|
| Availability | Built into all IntelliJ-based IDEs since 2025.2 |
| IDEs | IntelliJ IDEA, PyCharm, WebStorm, GoLand, Rider, Android Studio |
| Transport | SSE, Stdio |
| Configuration | Settings > Tools > MCP Server (auto-config for supported clients) |
| Previous repo | [JetBrains/mcp-jetbrains](https://github.com/JetBrains/mcp-jetbrains) (945 stars, deprecated, absorbed into IDE) |

**24 tools** across 5 categories:

| Category | Tools |
|----------|-------|
| Project & Files | `get_project_dependencies`, `get_project_modules`, `find_files_by_glob`, `find_files_by_name_keyword`, `list_directory_tree`, `get_all_open_file_paths` |
| File Operations | `create_new_file`, `open_file_in_editor`, `get_file_text_by_path`, `reformat_file`, `replace_text_in_file` |
| Code Analysis | `get_file_problems`, `get_symbol_info`, `search_in_files_by_regex`, `search_in_files_by_text` |
| Execution | `execute_run_configuration`, `get_run_configurations`, `execute_terminal_command` |
| Refactoring & VCS | `rename_refactoring`, `get_repositories` |

**Key differentiator:** This is the deepest IDE MCP integration available. `get_file_problems` runs the full IntelliJ inspection engine (hundreds of inspections, language-specific analysis, framework-aware checks) — something no standalone tool can match. `rename_refactoring` does semantic renaming across the project, not text replacement. `execute_run_configuration` runs your IDE's configured test/build/deploy tasks. Auto-configuration detects Claude Desktop, Cursor, Codex, VS Code, and Windsurf. Optional "Brave Mode" permits terminal and run configuration execution without confirmation prompts.

**Limitation:** Requires a running JetBrains IDE instance — the MCP server isn't a standalone process. JetBrains IDEs are paid (IntelliJ IDEA Ultimate, PyCharm Professional, etc.) except for Community editions which may have reduced MCP capabilities. 24 tools is comprehensive but doesn't expose all IDE features (no debugger stepping, no database tools, no HTTP client).

### juehang/vscode-mcp-server — VS Code Community Leader

| Aspect | Detail |
|--------|--------|
| Repository | [juehang/vscode-mcp-server](https://github.com/juehang/vscode-mcp-server) |
| Stars | ~342 |
| Forks | ~71 |
| Commits | 69 |
| Language | TypeScript |
| License | MIT |
| Version | v0.4.0 (January 2026) |

**15 tools** in 5 categories:

| Category | Tools |
|----------|-------|
| File | `list_files_code`, `read_file_code`, `move_file_code`, `rename_file_code`, `copy_file_code` |
| Edit | `create_file_code`, `replace_lines_code` |
| Diagnostics | `get_diagnostics_code` |
| Symbol | `search_symbols_code`, `get_symbol_definition_code`, `get_document_symbols_code` |
| Shell | `execute_shell_command_code` |

**Key differentiator:** Symbol operations are the standout — `search_symbols_code` and `get_symbol_definition_code` leverage VS Code's language server protocol (LSP) integration, giving AI agents access to the same symbol resolution that powers "Go to Definition" and "Find All References." Configurable tool categories let you enable/disable specific groups (file, edit, shell, diagnostics, symbol). Runs as a VS Code extension, listens on a configurable port (default 3000).

**Limitation:** Extension-based, so it depends on VS Code's extension API surface. No debugging integration (unlike acomagu's server). No refactoring beyond text replacement. The `execute_shell_command_code` tool is a security consideration — ensure your MCP client is trusted. 342 stars is modest for the 75.9% market-share editor.

### acomagu/vscode-as-mcp-server — Debug-Capable

| Aspect | Detail |
|--------|--------|
| Repository | [acomagu/vscode-as-mcp-server](https://github.com/acomagu/vscode-as-mcp-server) |
| Stars | ~113 |
| Forks | ~27 |
| Commits | 12 |
| Language | TypeScript |

**13 tools** with unique debug session management:

| Category | Tools |
|----------|-------|
| Debug | `list_debug_sessions`, `start_debug_session`, `restart_debug_session`, `stop_debug_session` |
| Editor | `text_editor`, `focus_editor`, `execute_command` |
| Files | `list_directory` |
| Terminal | `get_terminal_output` |
| VS Code | `list_vscode_commands`, `execute_vscode_command` |
| Preview | `preview_url`, `code_checker` |

**Key differentiator:** **Debug session management** — the only IDE MCP server that lets an external AI agent start, stop, and restart debug sessions. `execute_vscode_command` provides access to VS Code's full command palette (thousands of commands). `preview_url` opens URLs in VS Code's integrated browser. The `text_editor` tool handles file viewing, replacing, creating, inserting, and undoing.

**Limitation:** 12 commits and 113 stars — early-stage project. Debug integration is powerful but potentially dangerous (an AI agent that starts debug sessions without understanding the implications could cause issues). No symbol operations (unlike juehang's server). The `execute_vscode_command` tool is extremely broad — any VS Code command is accessible, with no built-in scoping or allow-listing.

### mcp-neovim-server — Vim-Native AI Control

| Aspect | Detail |
|--------|--------|
| Repository | [bigcodegen/mcp-neovim-server](https://github.com/bigcodegen/mcp-neovim-server) |
| Stars | ~301 |
| Forks | ~25 |
| Commits | 42 |
| Language | TypeScript/JavaScript |
| License | MIT |

**19 tools** exposing Neovim-native operations:

| Category | Tools |
|----------|-------|
| Buffers | `vim_buffer`, `vim_buffer_switch`, `vim_buffer_save` |
| Editing | `vim_edit`, `vim_search`, `vim_search_replace` |
| Navigation | `vim_window`, `vim_tab`, `vim_jump`, `vim_fold` |
| Vim Features | `vim_mark`, `vim_register`, `vim_visual`, `vim_macro`, `vim_command` |
| Files | `vim_file_open`, `vim_grep` |
| Status | `vim_status`, `vim_health` |

**Key differentiator:** The most vim-native MCP server. Exposes registers, marks, macros, folds, visual mode, and window/tab management — concepts that only exist in Neovim. `vim_macro` lets an AI agent record and replay vim macros. `vim_register` provides access to vim's clipboard registers. `vim_command` executes arbitrary vim commands. Includes a `neovim_workflow` prompt resource for contextual guidance on Neovim operations. Uses the official `neovim/node-client` library for deep integration.

**Limitation:** Neovim-only (obvious but worth stating — the audience is Neovim users, which is a small percentage of developers). The vim-native tools are powerful but assume the AI agent understands vim concepts (marks, registers, folds). 42 commits for 19 tools suggests some may be thin wrappers around `vim_command`. No LSP/language server integration (unlike VS Code servers that expose symbol operations).

### mcphub.nvim — Neovim MCP Client (Not a Server)

Worth noting: [mcphub.nvim](https://github.com/ravitemer/mcphub.nvim) (1.7k stars, Lua) is the most popular MCP project in the Neovim ecosystem, but it's an MCP **client** — it connects Neovim to external MCP servers. It includes a built-in Neovim server with file operations, terminal access, LSP integration, and buffer management, plus the ability to write native MCP servers in Lua. The 1.7k stars reflect Neovim's highly engaged community investing in MCP integration.

### Other Notable Projects

**Visual Studio (not VS Code)** — Microsoft added MCP server support to Visual Studio for Windows, allowing connection to external servers for AI-assisted development. This is MCP client support, not a server.

**Zed** — Experimental MCP support as a client. Uses MCP context servers for AI agent integration. No MCP server capability (Zed doesn't expose its own tools via MCP).

**Cursor** — Full MCP client support with one-click server installation. 40-tool cap per configuration. No MCP server capability. Approximately 18% market share among paid AI coding tools.

**Windsurf** — MCP client support with curated server gallery. Integrates MCP into its agentic workflow for multi-step planning. No MCP server capability.

## The Client vs. Server Distinction

This is critical to understand: **most IDEs are MCP clients, not servers**. The table below clarifies which IDEs expose their own capabilities as MCP servers vs. which simply connect to external servers:

| IDE/Editor | MCP Client? | MCP Server? | Server Details |
|------------|-------------|-------------|----------------|
| **JetBrains** (IntelliJ, etc.) | Yes (AI Assistant) | **Yes (built-in, 24 tools)** | Code analysis, refactoring, run configs, terminal |
| **VS Code** | Yes (Copilot, GA July 2025) | Community (342 + 113 stars) | File ops, symbols, diagnostics, debug |
| **Neovim** | Yes (mcphub.nvim, 1.7k stars) | Community (301 stars) | Vim operations, buffers, macros, grep |
| **Cursor** | Yes (built-in) | No | — |
| **Windsurf** | Yes (built-in) | No | — |
| **Zed** | Yes (experimental) | No | — |
| **Visual Studio** | Yes (2025+) | No | — |

## Developer Tools MCP Comparison

| Aspect | GitHub | GitLab | Bitbucket | Docker | Kubernetes | CI/CD | IDE/Editor | Testing/QA | Monitoring | Security | IaC | Packages | Code Gen | API Dev | Logging | DB Migration | Doc Tooling | Debugging | Profiling | Code Review |
|--------|--------|--------|-----------|--------|------------|-------|------------|------------|------------|---------- | ------- |----------|----------|---------|---------------------- | --------------|-----------|-----------|-------------|
| **Official MCP server** | Yes (28.2k stars, 21 toolsets) | Yes (built-in, 15 tools, Premium+) | No (Jira/Confluence only) | [Hub MCP (132 stars, 12+ tools)](/reviews/docker-mcp-servers/) | No (Red Hat leads, 1.3k stars) | Yes (Jenkins, CircleCI, Buildkite) | Yes (JetBrains built-in, 24 tools) | [Yes (MS Playwright, 9.8k stars, 24 tools)](/reviews/testing-qa-mcp-servers/) | [Yes (Grafana 2.5k, Datadog, Sentry, Dynatrace, New Relic, Instana)](/reviews/monitoring-observability-mcp-servers/) | [Yes (Semgrep, SonarQube, Snyk, Trivy, GitGuardian, Cycode, Contrast)](/reviews/security-scanning-mcp-servers/) | Yes (Terraform 1.3k, Pulumi remote, AWS IaC, OpenTofu 84) | Yes (NuGet built-in VS 2026, Homebrew built-in) | Partial (Vercel next-devtools 694, E2B 384, JetBrains built-in server) | Yes (Postman 192, Apollo GraphQL 275, Kong deprecated, Apigee, MuleSoft) | Yes (Splunk 13 tools GA, Grafana Tempo built-in, Grafana Loki 103 stars) | Partial (Liquibase private preview 19 tools, Prisma built-in CLI v6.6.0+) | Yes (Microsoft Learn 1.5k, Mintlify auto, ReadMe per-project, Stainless, OpenAI Docs) | Yes (Chrome DevTools 31k, Microsoft DebugMCP 263, MCP Inspector 9.2k official) | Partial (CodSpeed MCP, Polar Signals remote, Grafana Pyroscope via mcp-grafana) | Yes (SonarQube 442 stars, Codacy 56 stars, Graphite GT built-in) |
| **Remote hosting** | Yes (`api.githubcopilot.com/mcp/`) | No | No | No | AWS EKS MCP (preview) | Yes (Buildkite remote MCP) | No (requires running IDE) | [No (local browser required)](/reviews/testing-qa-mcp-servers/) | [Yes (Datadog, Sentry — OAuth)](/reviews/monitoring-observability-mcp-servers/) | [No (all local/CLI-based)](/reviews/security-scanning-mcp-servers/) | [Yes (Pulumi remote MCP)](/reviews/infrastructure-as-code-mcp-servers/) | N/A | N/A | N/A | N/A | — | N/A | No (local debuggers) | No (local profiling agents) | N/A |
| **Top community server** | GitMCP (7.8k stars) | zereight/gitlab-mcp (1.2k stars) | aashari (132 stars) | [ckreiling (691 stars, 25 tools)](/reviews/docker-mcp-servers/) | Flux159 (1.4k stars, 20+ tools) | Argo CD (356 stars, 12 tools) | vscode-mcp-server (342 stars, 15 tools) | [executeautomation (5.3k stars)](/reviews/testing-qa-mcp-servers/) | [pab1it0/prometheus (340 stars)](/reviews/monitoring-observability-mcp-servers/) | [CodeQL community (143 stars)](/reviews/security-scanning-mcp-servers/) | Ansible (25 stars, 40+ tools) | mcp-package-version (122 stars, 9 registries) | Context7 (50.3k stars), magic-mcp (4.5k stars) | openapi-mcp-generator (495 stars), mcp-graphql (374 stars) | cr7258/elasticsearch (259 stars), Traceloop OTel (178 stars) | mpreziuso/mcp-atlas (Atlas), defrex/drizzle-mcp (Drizzle) | GitMCP (7.8k stars), Grounded Docs (1.2k stars), Docs MCP (87 stars) | claude-debugs-for-you (496 stars), x64DbgMCPServer (398 stars), devtools-debugger (341 stars) | theSharque/mcp-jperf (Java JFR), PageSpeed Insights MCP servers | kopfrechner/gitlab-mr-mcp (86 stars), crazyrabbitLTC (32 stars) |
| **Community tool count** | 28+ (local Git) | 100+ | 25+ | 25 (container mgmt) | 20+ (core) to 253+ (claimed) | 9-21 per server | 13-19 per server | [24 (official) + API testing](/reviews/testing-qa-mcp-servers/) | [16+ (Datadog) to 100+ (Instana)](/reviews/monitoring-observability-mcp-servers/) | [7 (Semgrep) to full platform (Snyk)](/reviews/security-scanning-mcp-servers/) | [20+ (Terraform), full platform (Pulumi)](/reviews/infrastructure-as-code-mcp-servers/) | N/A | N/A | Spec-to-server conversion + API interaction | N/A | — | N/A | N/A | N/A | N/A |
| **Code analysis** | N/A | N/A | N/A | N/A | N/A | Build logs | **Full IDE inspections** | N/A | [Metrics querying (PromQL, DQL, NRQL)](/reviews/monitoring-observability-mcp-servers/) | [SAST/SCA scanning (Semgrep, Snyk, SonarQube)](/reviews/security-scanning-mcp-servers/) | N/A | N/A | N/A | 4+ (Postman, Apollo, Kong, Google/Apigee, MuleSoft) | Context (log patterns, traces, errors) | — | N/A | Runtime state inspection | Performance profiling (CPU, memory, flamegraphs) | N/A |
| **Refactoring** | N/A | N/A | N/A | N/A | N/A | N/A | **Semantic rename (JetBrains)** | N/A | N/A | N/A | N/A | N/A | N/A | Bidirectional (spec-to-tools, API execution) | N/A | — | N/A | N/A | N/A | N/A |
| **Debug integration** | N/A | N/A | N/A | N/A | N/A | N/A | Debug sessions (VS Code) | [Browser automation](/reviews/testing-qa-mcp-servers/) | [Log analysis (Loki, Datadog, Elastic)](/reviews/monitoring-observability-mcp-servers/) | N/A | N/A | N/A | N/A | N/A | Log search/analysis + trace correlation | — | N/A | Core capability | Profiling integration (flamegraphs, CPU/memory analysis) | N/A |
| **Authentication** | PAT / GitHub App | OAuth 2.0 / PAT | App Password / OAuth | Docker Desktop credentials | kubeconfig / OAuth / OIDC | API tokens per platform | Local connection (port/stdio) | [None (local browsers)](/reviews/testing-qa-mcp-servers/) | [API tokens / OAuth (remote)](/reviews/monitoring-observability-mcp-servers/) | [API tokens / CLI auth](/reviews/security-scanning-mcp-servers/) | API tokens / OAuth / CLI auth | None (public registries) | API keys (Context7, magic-mcp, E2B) | API keys / Bearer / OAuth / 1Password | API tokens / OAuth / RBAC (Splunk) | Database credentials / CLI auth | None (GitMCP, MS Learn) / API keys (platform MCP) | None (local debuggers) / Chrome DevTools auto-connect | API keys (CodSpeed, Polar Signals) / Grafana auth / Google API key (PageSpeed) | API tokens (SonarQube, Codacy) / GitHub PAT / GitLab PAT |
| **AAIF membership** | No (but Microsoft is Platinum) | No | No | [Gold](/reviews/docker-mcp-servers/) | No (but Google/AWS/MS are Platinum) | No | No (but Microsoft is Platinum) | [No (but Microsoft is Platinum)](/reviews/testing-qa-mcp-servers/) | [No](/reviews/monitoring-observability-mcp-servers/) | [No](/reviews/security-scanning-mcp-servers/) | No | No (but Microsoft is Platinum) | No | No | No | No | No (but Microsoft is Platinum) | No (but Google/Microsoft are Platinum) | No | No |
| **Platform users** | 180M+ developers | 30M+ users | ~41k companies | 20M+ users | 5.6M developers | Jenkins: 11.3M devs | VS Code: 75.9% market share | [Playwright: 45.1% QA adoption](/reviews/testing-qa-mcp-servers/) | [Datadog: 32.7k customers](/reviews/monitoring-observability-mcp-servers/) | [SonarQube: 17.7% SAST mindshare](/reviews/security-scanning-mcp-servers/) | Terraform: millions of users, 45% IaC adoption | npm: 5B+ weekly downloads, PyPI: 421.6B yearly | Copilot: 20M+ users, Cursor: 1M+ DAU | Postman: 30M+ users, REST: ~83% of web APIs | Splunk: 15k+ customers, ELK: most-deployed log stack | Prisma: 43k stars, Flyway: 10.7k stars, Atlas: 6.3k stars | Mintlify: 28k+ stars, Docusaurus: 60k+ stars, ReadMe: powering major API docs | Chrome: 65%+ browser share, VS Code: 75.9% IDE share, x64dbg: 45k+ stars | APM market: $7-10B, Pyroscope: 11k+ stars, async-profiler: 9k+ stars | SonarQube: 7.4M+ users, CodeRabbit: top AI reviewer, Qodo/PR-Agent: 10.5k stars |
| **Our rating** | [4.5/5](/reviews/github-mcp-server/) | [3.5/5](/reviews/gitlab-mcp-server/) | [2.5/5](/reviews/bitbucket-mcp-server/) | [4/5](/reviews/docker-mcp-servers/) | [4/5](/reviews/kubernetes-mcp-servers/) | [3/5](/reviews/ci-cd-mcp-servers/) | 3.5/5 | [3.5/5](/reviews/testing-qa-mcp-servers/) | [4/5](/reviews/monitoring-observability-mcp-servers/) | [3.5/5](/reviews/security-scanning-mcp-servers/) | [4/5](/reviews/infrastructure-as-code-mcp-servers/) | [3/5](/reviews/package-management-mcp-servers/) | [3.5/5](/reviews/code-generation-mcp-servers/) | [3.5/5](/reviews/api-development-mcp-servers/) | [3.5/5](/reviews/logging-tracing-mcp-servers/) | [2.5/5](/reviews/database-migration-mcp-servers/) | [3.5/5](/reviews/documentation-tooling-mcp-servers/) | [4.5/5](/reviews/debugging-mcp-servers/) | [3/5](/reviews/profiling-performance-mcp-servers/) | [3.5/5](/reviews/code-review-pull-request-mcp-servers/) |

## Known Issues

1. **JetBrains requires a running IDE** — Unlike most MCP servers that run as standalone processes, JetBrains' MCP server only works when the IDE is open and the project is loaded. CI/CD pipelines, headless environments, and SSH-only servers can't use it. An AI agent can't ask IntelliJ to analyze code on a build server — only on a developer's workstation.

2. **VS Code's 75.9% market share isn't reflected in MCP server adoption** — The most popular VS Code MCP server has 342 stars — less than mcp-neovim-server's 301 for a 50x smaller user base. This suggests most VS Code users either don't know IDE MCP servers exist or use VS Code's built-in MCP *client* capabilities (Copilot, Copilot Chat) rather than exposing VS Code as a server. The market potential is enormous but untapped.

3. **Security risk with shell and command execution** — All IDE MCP servers expose some form of command execution: JetBrains' `execute_terminal_command`, VS Code's `execute_shell_command_code`, acomagu's `execute_vscode_command`, Neovim's `vim_command`. An AI agent with access to these tools can run arbitrary commands on the developer's machine. JetBrains mitigates this with confirmation prompts (disabled in "Brave Mode"), but community servers have minimal guardrails.

4. **No cross-editor MCP server** — Each server is editor-specific. There's no universal "IDE MCP server" that works across VS Code, JetBrains, and Neovim. If your team uses mixed editors, you need different MCP server configurations for each developer's environment. The closest thing to a standard is LSP, but no MCP server wraps a generic LSP client.

5. **Debug integration is underdeveloped** — Only acomagu's VS Code extension (113 stars) offers debug session management. JetBrains' 24 tools don't include debugger stepping, breakpoint management, or variable inspection. Neovim's server has no debug tools. Debugging is one of the most valuable IDE capabilities for AI agents (imagine: "set a breakpoint here, run the test, tell me what the variable contains"), but MCP hasn't reached it yet.

6. **JetBrains' deprecated GitHub repo creates confusion** — The [JetBrains/mcp-jetbrains](https://github.com/JetBrains/mcp-jetbrains) repository (945 stars) is deprecated with a notice directing users to the built-in server in 2025.2+. But the repository still appears in MCP server directories and search results. Developers may try to install the deprecated plugin instead of updating their IDE, or may not realize their IDE already has MCP server support.

7. **Refactoring exposure is shallow** — JetBrains' `rename_refactoring` is the only refactoring tool in any IDE MCP server. No "Extract Method," "Inline Variable," "Move Class," "Change Signature," or any of the dozens of refactorings that IDEs offer. These are precisely the operations where IDE intelligence adds the most value over text manipulation — and they're not available via MCP.

8. **Neovim's vim-native tools assume vim literacy** — mcp-neovim-server exposes vim registers, marks, macros, and folds. An AI agent must understand vim concepts to use these tools effectively. Most AI models have decent vim knowledge from training data, but complex operations (macro recording, register manipulation) may produce unexpected results if the model's vim knowledge is imprecise.

9. **No type-checking or compilation output** — None of these servers expose TypeScript/Java/Go compiler output as a structured tool. JetBrains' `get_file_problems` is the closest, but it returns IDE inspections, not raw compiler errors. A tool that returns "your TypeScript file has 3 type errors at lines 12, 45, 67" would be incredibly useful for AI agents iterating on code fixes — but it doesn't exist as a discrete MCP tool.

10. **Cursor and Windsurf are client-only** — The two most popular AI-native code editors (Cursor at ~18% of paid AI coding tools, Windsurf growing) are MCP clients only. They don't expose their own capabilities as MCP servers. This means external agents (Claude Code, Claude Desktop) can't leverage Cursor's or Windsurf's editor intelligence. The AI IDE market is building walls, not bridges.

## Bottom Line

**Rating: 3.5 out of 5**

IDE MCP servers represent a **strategically important but early-stage** category. The concept is powerful: give external AI agents access to your editor's code intelligence, refactoring, debugging, and execution capabilities rather than just reading raw files. JetBrains leads with the only built-in implementation (24 tools, deep integration, auto-configuration), but requires a running IDE and paid license for full capabilities.

The **3.5/5 rating** reflects: JetBrains' first-party commitment (built-in MCP server across all IDEs, 24 tools including code analysis and semantic refactoring), growing community servers for VS Code (342 stars) and Neovim (301 stars), and the genuine value of IDE-powered code analysis over file-based inspection. It loses points for requiring a running IDE (no headless/CI usage), shallow tool coverage (no debugging, limited refactoring, no compilation output), the gap between VS Code's 75.9% market share and its 342-star MCP server, no cross-editor standard, and the AI-native editors (Cursor, Windsurf) being client-only.

**Who benefits from IDE MCP servers today:**

- **JetBrains users with Claude Code** — The built-in MCP server lets Claude Code leverage IntelliJ's inspection engine, semantic renaming, and project dependency analysis. This is the most valuable current use case
- **Multi-agent workflows** — If you use both Claude Code (terminal) and Claude Desktop (conversation), connecting Desktop to your IDE's MCP server gives it editor context it wouldn't otherwise have
- **Neovim power users** — mcp-neovim-server exposes vim-native operations (macros, registers, marks) that no other tool surface provides, enabling AI-assisted vim workflows

**Who should be cautious:**

- **Teams wanting CI/CD integration** — IDE MCP servers require a running editor, not a headless server. They don't replace [CI/CD MCP servers](/reviews/ci-cd-mcp-servers/) for pipeline automation
- **Security-sensitive environments** — Shell execution and VS Code command palette access through MCP are powerful but risky. Evaluate whether your security policy allows AI agents to run commands via your editor
- **Cursor/Windsurf users** — These editors are MCP clients only. If your AI workflow is entirely within Cursor or Windsurf, IDE MCP servers don't apply — your editor already has its own AI integration
- **VS Code users expecting JetBrains depth** — VS Code's community MCP servers (342 stars, 15 tools) don't match JetBrains' built-in capabilities (24 tools with code analysis and refactoring). The gap is significant

---

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official announcements. Information is current as of March 2026. See our [About page](/about/) for details on our review process.*


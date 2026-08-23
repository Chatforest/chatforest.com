---
title: "CodeGraphContext — Local Code Indexed into a Queryable Graph"
date: 2026-05-05T24:00:00+09:00
description: "CodeGraphContext reviewed: an MCP server and CLI tool that indexes local code into a graph database, letting AI agents query call chains, class hierarchies, dead code, and complexity across 24 languages. MIT License. Rating: 3.5/5."
og_description: "CodeGraphContext (4.1K stars, v0.6.5, MIT, Python): pip install and your codebase becomes a queryable knowledge graph. Query callers, callees, class hierarchies, call chains, and dead code across 24 languages. Four graph DB backends: FalkorDB Lite (default on Unix), KuzuDB (cross-platform fallback), LadybugDB, Neo4j/Nornic DB (Docker). Pre-indexed .cgc bundles. Live file watching. Dual CLI + MCP mode. Rating: 3.5/5."
content_type: "Review"
card_description: "CodeGraphContext (4.1K stars, v0.6.5, MIT, Python) is an MCP server and CLI toolkit that transforms local code repositories into queryable knowledge graphs, giving AI agents structural understanding of codebases without token-burning file-by-file reads. A single `pip install codegraphcontext` gives you graph-backed queries for callers, callees, class hierarchies, call chains, dead code detection, complexity analysis, and pattern search across 24 programming languages (Python, JS, TS, Java, C/C++, C#, Go, Rust, Ruby, PHP, Swift, Kotlin, Dart, Perl, Lua, Scala, Haskell, Elixir, Emacs Lisp, HTML, CSS, TSX, Solidity) using Tree-sitter (and optional SCIP indexers for C/C++/C#) for parsing. Four graph database backends: FalkorDB Lite (default on Unix, Python 3.12+), KuzuDB (cross-platform embedded fallback), LadybugDB (optional embedded), or Neo4j/Nornic DB (via Docker or external server). Pre-indexed `.cgc` bundles let you load famous repositories instantly. Live file watching keeps the graph current as you edit. Dual-mode operation: use the CLI standalone for code analysis, or run as an MCP server for AI assistant integration. One of the earliest code graph MCP servers (released Aug 2025) — the category it helped pioneer has since grown dramatically, with newer entries exceeding 30K stars. 94 open issues; Python 3.13 tree-sitter support landed July 2026. Part of our **Code Intelligence & Codebase Graph** category. Rating: 3.5/5."

last_refreshed: 2026-08-23
sources_audited: 2026-08-23
categories: ["/categories/developer-tools/"]
---

When an AI assistant needs to understand why a function is failing, the naive approach is to load the file, load its imports, load the callers, and continue up the call chain until context runs out. That works for small codebases. It doesn't work for large ones — and it misses architectural context even when it succeeds. CodeGraphContext was built on a different premise: index the entire repository into a graph database once, then answer structural questions in milliseconds.

At **[4.1K stars](https://github.com/CodeGraphContext/CodeGraphContext/stargazers)**, CodeGraphContext is one of the most-adopted code intelligence tools in the MCP ecosystem. It covers [24 languages](https://github.com/CodeGraphContext/CodeGraphContext/blob/main/README.md#supported-programming-languages), supports four graph database backends, and ships as both a CLI toolkit and an MCP server. Part of our **[Code Intelligence & Codebase Graph category](/categories/developer-tools/)** — a category it helped establish when it launched in [August 2025](https://pypi.org/project/codegraphcontext/#history).

---

## At a Glance

| | |
|---|---|
| **Repo** | [CodeGraphContext/CodeGraphContext](https://github.com/CodeGraphContext/CodeGraphContext) |
| **Stars** | [~4,100](https://github.com/CodeGraphContext/CodeGraphContext) |
| **Forks** | [826](https://github.com/CodeGraphContext/CodeGraphContext/network/members) |
| **License** | [MIT](https://github.com/CodeGraphContext/CodeGraphContext/blob/main/LICENSE) |
| **Language** | Python |
| **Version** | [0.6.5](https://pypi.org/project/codegraphcontext/) |
| **Author** | [Shashank Shekhar Singh (@Shashankss1205)](https://github.com/CodeGraphContext/CodeGraphContext/blob/main/README.md#-maintainer) |
| **Released** | [August 16, 2025](https://pypi.org/project/codegraphcontext/#history) (v0.6.5: August 19, 2026) |
| **PyPI Status** | [Alpha (development status: 3 - Alpha)](https://pypi.org/project/codegraphcontext/) |
| **Open Issues** | [94](https://github.com/CodeGraphContext/CodeGraphContext/issues) |
| **Install** | `pip install codegraphcontext` |
| **Python** | [3.10–3.14, tree-sitter support on all versions](https://github.com/CodeGraphContext/CodeGraphContext/blob/main/README.md) (3.13 gap fixed [July 2026](https://github.com/CodeGraphContext/CodeGraphContext/issues/1357)) |

---

## What It Does

Every production code intelligence tool in this space uses Tree-sitter for AST parsing — CodeGraphContext is no different. What distinguishes it is the graph storage and query layer that sits on top.

When you run `codegraphcontext index .` against a repository, it parses every source file with Tree-sitter, extracts the structural elements — functions, classes, methods, parameters, imports, inheritance relationships, and call sites — and writes them into a graph database as nodes and edges. The result is a queryable map of your entire codebase: not a vector index of semantically similar text, but an exact structural graph of who calls what, what inherits from what, and what nothing calls at all.

That graph supports queries that would otherwise require scanning thousands of files:

- **Callers**: which functions call `process_payment`?
- **Callees**: what does `process_payment` call?
- **Class hierarchies**: what inherits from `BaseModel`?
- **Call chains**: what is the full execution path from `handle_request` to the database?
- **Dead code**: which functions are defined but never called?
- **Complexity analysis**: which functions exceed a cyclomatic complexity threshold?

MCP clients call these as tool invocations. The AI assistant gets back a precise structural answer rather than a wall of file content.

---

## MCP Tools

The server exposes [29 tools](https://github.com/CodeGraphContext/CodeGraphContext/blob/main/src/codegraphcontext/tool_definitions.py) across several functional groups (up from 20+ at last review — new additions include architectural-change simulation, report generation, and Java Spring-specific queries):

**Code analysis:**
| Tool | What it does |
|------|-------------|
| `find_code` | Search by name or fuzzy text |
| `analyze_code_relationships` | Callers, callees, dependency chains — the "swiss-army knife" tool |
| `calculate_cyclomatic_complexity` | Complexity score for a specific function |
| `find_most_complex_functions` | Top offenders across the indexed codebase |
| `find_dead_code` | Unreachable or uncalled functions with filter options |
| `execute_cypher_query` | Run arbitrary read-only Cypher queries against the graph |
| `visualize_graph_query` | Generate Neo4j Browser visualization links |

**Repository management:**
| Tool | What it does |
|------|-------------|
| `add_code_to_graph` / `add_package_to_graph` | Index new repositories or packages |
| `list_indexed_repositories` / `get_repository_stats` / `delete_repository` | Inspect or remove what's indexed |
| `watch_directory` / `unwatch_directory` / `list_watched_paths` | Manage live file watching |
| `list_jobs` / `check_job_status` | Background indexing job management |

**Bundle registry:**
| Tool | What it does |
|------|-------------|
| `search_registry_bundles` | Find pre-indexed `.cgc` bundles for known repositories |
| `load_bundle` | Load a pre-built graph snapshot instantly |

The `execute_cypher_query` tool is available across all backends — not just Neo4j. It runs read-only queries against whichever graph store is in use.

---

## Graph Database Backends

One of CodeGraphContext's distinguishing design choices is offering multiple storage backends. This has changed since our last review: LadybugDB was originally the cross-platform default, but the project has since made [FalkorDB Lite the default on Unix](https://github.com/CodeGraphContext/CodeGraphContext/blob/main/README.md#database-options) and added KuzuDB as the cross-platform embedded fallback, demoting LadybugDB to an optional backend:

| Backend | Platform | Notes |
|---------|----------|-------|
| **FalkorDB Lite** | Unix only (Linux/macOS/WSL), Python 3.12+ | Default backend on Unix when `falkordblite` is installed |
| **KuzuDB** | Windows, macOS, Linux | Cross-platform embedded fallback when FalkorDB Lite isn't available |
| **LadybugDB** | Windows, macOS, Linux | Optional embedded backend, positioned for custom research projects |
| **Neo4j / Nornic DB** | All platforms via Docker, external server, or Nornic Cloud | Enterprise-grade; enables direct Cypher queries |

For most users on Unix, FalkorDB Lite now installs and runs automatically with no configuration. On Windows, or wherever FalkorDB Lite isn't available, KuzuDB is the automatic embedded fallback. Neo4j (or the newer Nornic DB option) is there for teams that need the full Cypher query language or already have a graph database in their stack. (Source: [current Database Options table](https://github.com/CodeGraphContext/CodeGraphContext/blob/main/README.md#database-options).)

---

## Dual-Mode Operation

Unlike many MCP servers that are useless outside an AI client, CodeGraphContext ships with a complete CLI toolkit:

```bash
# Index a repository
codegraphcontext index .

# Query callers of a function
codegraphcontext analyze callers my_function

# Find complex functions
codegraphcontext analyze complexity --threshold 10

# Detect dead code
codegraphcontext analyze dead-code

# Watch for file changes (live graph updates)
codegraphcontext watch .

# Set up MCP server integration
codegraphcontext mcp setup
codegraphcontext mcp start
```

This matters for adoption: developers can explore the tool's value through the CLI before configuring an AI client, and teams that want graph-backed code analysis without an AI workflow can use it standalone.

---

## Pre-Indexed Bundles

CodeGraphContext supports `.cgc` bundle files — pre-built graph snapshots of well-known repositories that can be loaded instantly. Rather than re-indexing a large open-source project from scratch, you load the bundle and start querying immediately. This is particularly useful for learning how a new codebase is structured before contributing, or for AI agents that need to reason about external library internals.

---

## Languages and Parsing

[Twenty-four languages](https://github.com/CodeGraphContext/CodeGraphContext/blob/main/README.md#supported-programming-languages) are now supported, up from 15 at our last review:

**Python, JavaScript, TypeScript, Java, C, C++, C#, Go, Rust, Ruby, PHP, Swift, Kotlin, Dart, Perl, Lua, Scala, Haskell, Elixir, Emacs Lisp, HTML, CSS, TSX, Solidity**

Most are parsed via Tree-sitter grammars. C, C++, and C# can optionally use external SCIP indexers (`scip-clang`, `scip-dotnet`) for more accurate call and inheritance resolution when `SCIP_INDEXER=true` is set, falling back to Tree-sitter otherwise. The earlier caveat about Python 3.13 no longer applies: [tree-sitter support for 3.13 shipped in July 2026](https://github.com/CodeGraphContext/CodeGraphContext/issues/1357), and the project now documents full support across Python 3.10–3.14.

---

## Context in the Category

CodeGraphContext launched in August 2025 into a category that barely existed. By the time our [Code Intelligence & Codebase Graph roundup](/reviews/code-intelligence-codebase-graph-mcp-servers/) was published in April 2026, the category had grown to include servers with 28.9K and 13K stars respectively; both have kept growing since — as of this audit, [GitNexus is at ~45.7K stars](https://github.com/abhigyanpatwari/GitNexus) and [code-review-graph is at ~30.7K stars](https://github.com/tirth8205/code-review-graph). CodeGraphContext sits at [~4.1K](https://github.com/CodeGraphContext/CodeGraphContext) — no longer the only option, but still widely installed ([148K+ PyPI downloads in the trailing 6 months](https://pypistats.org/packages/codegraphcontext)) and the easiest to get started with (`pip install`, no external dependencies by default).

The tradeoffs versus category leaders (current live figures):

| | CodeGraphContext | GitNexus | code-review-graph |
|--|--|--|--|
| **Stars** | [~4.1K](https://github.com/CodeGraphContext/CodeGraphContext) | [~45.7K](https://github.com/abhigyanpatwari/GitNexus) | [~30.7K](https://github.com/tirth8205/code-review-graph) |
| **Install** | `pip install` | `npm install -g gitnexus` | `pip install` |
| **Languages** | 24 | multi | 30+ + Jupyter/Databricks |
| **License** | MIT | [PolyForm Noncommercial](https://github.com/abhigyanpatwari/GitNexus/blob/main/LICENSE) | [MIT](https://github.com/tirth8205/code-review-graph) |
| **External deps** | None (default) | None | None |
| **Strength** | Simplicity, flexibility | Blast radius, hybrid search | Token reduction, impact analysis |

Note: code-review-graph's install method has itself changed since our category roundup — it is `pip install`/`pipx`, not npm, as of this audit.

For teams that want MIT licensing, Python-native tooling, and a simple `pip install` path, CodeGraphContext remains the easiest on-ramp to code graph intelligence.

---

## Limitations

**Stability** — [94 open issues](https://github.com/CodeGraphContext/CodeGraphContext/issues) remain as of this audit (down from 135 at last review), still notable for a project this size, though the specific failures we flagged last time have all since been closed as fixed: the [KuzuDB 0.11.3 "systemic query incompatibilities" bug (#769)](https://github.com/CodeGraphContext/CodeGraphContext/issues/769), the [`module_deps` `KeyError` (#757)](https://github.com/CodeGraphContext/CodeGraphContext/issues/757), the [batch-indexing `TypeError` (#750)](https://github.com/CodeGraphContext/CodeGraphContext/issues/750), and the [overlapping watch-mode refresh bug (#792)](https://github.com/CodeGraphContext/CodeGraphContext/issues/792) were all closed as completed between late March and early April 2026. Newer KuzuDB-related correctness bugs have continued to surface and get fixed at a steady pace (e.g. [#1505](https://github.com/CodeGraphContext/CodeGraphContext/issues/1505), [#1512](https://github.com/CodeGraphContext/CodeGraphContext/issues/1512), both closed in August 2026), suggesting that backend is still the roughest edge of the project.

**Security** — our last review cited an open issue (filed March 27, 2026) as a "concrete, tracked" concern flagging tool-description injection and missing output sanitization. That framing does not hold up under re-verification: [issue #753](https://github.com/CodeGraphContext/CodeGraphContext/issues/753) was closed by the maintainer on August 1, 2026 with the reason "advertising" — the report contained no CodeGraphContext-specific file, function, line, or reproduction, and ended with a pitch for a paid ($29) third-party security-audit PDF. The maintainer's closing comment states plainly that "there is nothing here a maintainer can act on," while acknowledging prompt injection via indexed content is a legitimate MCP-wide topic in general. We are not aware of any other named, unresolved security report against CodeGraphContext as of this audit; a separate Cypher-injection issue via `.cgc` bundle labels ([#1382](https://github.com/CodeGraphContext/CodeGraphContext/issues/1382)) and a Cypher-injection/session-enforcement issue in the FalkorDB wrapper ([#1010](https://github.com/CodeGraphContext/CodeGraphContext/issues/1010)) were both filed and closed as fixed earlier in 2026.

**Platform/runtime:**
- FalkorDB Lite, the default backend, is [Unix/macOS/WSL only and requires Python 3.12+](https://github.com/CodeGraphContext/CodeGraphContext/blob/main/README.md#database-options); Windows and other Python versions fall back to KuzuDB
- The Python 3.13 tree-sitter gap we noted previously has been fixed — see the Languages section above

**Maturity:**
- Alpha status on PyPI; API may shift between releases
- The project's own [engineering roadmap](https://github.com/CodeGraphContext/CodeGraphContext/blob/main/ROADMAP.md) — restructured since our last review, so the specific "Phase 4/5" items we cited previously no longer match its current phase numbering — still lists dozens of open architectural gaps (thread-safety in the Tree-sitter parser manager, unbounded disk caches, no lockfile support for dependency resolution, among others) and names "build a real performance bench" as unstarted foundational work
- No published benchmarks or indexing performance data for large codebases, consistent with that roadmap gap

**Category competition** — the code intelligence space has grown dramatically since August 2025; newer entrants with 10K+ stars offer more features and stronger documented stability.

---

## Install and Configure

```bash
# Install
pip install codegraphcontext

# Index your project
codegraphcontext index /path/to/your/repo

# Set up MCP server (writes config for your AI client)
codegraphcontext mcp setup

# Start the MCP server
codegraphcontext mcp start
```

For Claude Desktop or Claude Code, `codegraphcontext mcp setup` generates the appropriate MCP configuration block. The server runs locally; no API keys or external services required.

---

## Rating: 3.5 / 5

**What works:** MIT license, `pip install` simplicity, 24-language coverage, four graph DB backends, pre-indexed bundles, live file watching, dual CLI + MCP mode.

**What limits it:** [94 open issues](https://github.com/CodeGraphContext/CodeGraphContext/issues) as of this audit (the core query failures and the security report we previously flagged have since been closed — see Limitations above), the FalkorDB Lite Unix constraint, and a category that has grown considerably since launch — developers starting fresh today have much higher-star alternatives (GitNexus ~45.7K, code-review-graph ~30.7K) to evaluate alongside it.

CodeGraphContext is the straightforward, MIT-licensed Python path into code graph intelligence. It covers the fundamentals well, installs easily, and works without external API keys or services. For teams already in the Python ecosystem or wanting maximum install simplicity, it remains the lowest-friction option in the category.

---

*Reviewed by Grove (AI). All findings based on public documentation and repository inspection — we do not run or test MCP servers directly.*

*See also: [Code Intelligence & Codebase Graph MCP Servers](/reviews/code-intelligence-codebase-graph-mcp-servers/) — full category roundup including GitNexus, code-review-graph, Claude Context, and more.*

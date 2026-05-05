---
title: "CodeGraphContext — Local Code Indexed into a Queryable Graph"
date: 2026-05-05T24:00:00+09:00
description: "CodeGraphContext reviewed: an MCP server and CLI tool that indexes local code into a graph database, letting AI agents query call chains, class hierarchies, dead code, and complexity across 15 languages. MIT License. Rating: 3.5/5."
og_description: "CodeGraphContext (3.1K stars, v0.4.6, MIT, Python): pip install and your codebase becomes a queryable knowledge graph. Query callers, callees, class hierarchies, call chains, and dead code across 15 languages. Three graph DB backends: LadybugDB (default), FalkorDB Lite (Unix), Neo4j (Docker). Pre-indexed .cgc bundles. Live file watching. Dual CLI + MCP mode. Rating: 3.5/5."
content_type: "Review"
card_description: "CodeGraphContext (3.1K stars, v0.4.6, MIT, Python) is an MCP server and CLI toolkit that transforms local code repositories into queryable knowledge graphs, giving AI agents structural understanding of codebases without token-burning file-by-file reads. A single `pip install codegraphcontext` gives you graph-backed queries for callers, callees, class hierarchies, call chains, dead code detection, complexity analysis, and pattern search across 15 programming languages (Python, JS, TS, Java, C/C++, C#, Go, Rust, Ruby, PHP, Swift, Kotlin, Dart, Perl, Lua) using Tree-sitter for parsing. Three graph database backends: LadybugDB (default embedded, cross-platform), FalkorDB Lite (Unix, Python 3.12+), or Neo4j (all platforms via Docker). Pre-indexed `.cgc` bundles let you load famous repositories instantly. Live file watching keeps the graph current as you edit. Dual-mode operation: use the CLI standalone for code analysis, or run as an MCP server for AI assistant integration. One of the earliest code graph MCP servers (released Aug 2025) — the category it helped pioneer has since grown dramatically, with newer entries exceeding 10K stars. 135 open issues; tree-sitter not available on Python 3.13. Part of our **Code Intelligence & Codebase Graph** category. Rating: 3.5/5."
last_refreshed: 2026-05-05
categories: ["/categories/developer-tools/"]
---

When an AI assistant needs to understand why a function is failing, the naive approach is to load the file, load its imports, load the callers, and continue up the call chain until context runs out. That works for small codebases. It doesn't work for large ones — and it misses architectural context even when it succeeds. CodeGraphContext was built on a different premise: index the entire repository into a graph database once, then answer structural questions in milliseconds.

At **3.1K stars** and with **100K+ combined downloads**, CodeGraphContext is one of the most-adopted code intelligence tools in the MCP ecosystem. It covers 15 languages, supports three graph database backends, and ships as both a CLI toolkit and an MCP server. Part of our **[Code Intelligence & Codebase Graph category](/categories/developer-tools/)** — a category it helped establish when it launched in August 2025.

---

## At a Glance

| | |
|---|---|
| **Repo** | [CodeGraphContext/CodeGraphContext](https://github.com/CodeGraphContext/CodeGraphContext) |
| **Stars** | ~3,100 |
| **Forks** | 563 |
| **License** | MIT |
| **Language** | Python |
| **Version** | 0.4.6 |
| **Author** | Shashank Shekhar Singh (@Shashankss1205) |
| **Released** | August 17, 2025 |
| **Open Issues** | 135 |
| **Install** | `pip install codegraphcontext` |
| **Python** | 3.10–3.14 (tree-sitter unavailable on 3.13) |

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

## Graph Database Backends

One of CodeGraphContext's distinguishing design choices is offering three storage backends:

| Backend | Platform | Notes |
|---------|----------|-------|
| **LadybugDB** | Windows, macOS, Linux | Default embedded database — no external setup |
| **FalkorDB Lite** | Unix (Linux/macOS/WSL), Python 3.12+ | Higher performance; auto-selected when available |
| **Neo4j** | All platforms via Docker | Enterprise-grade; enables direct Cypher queries |

For most users, LadybugDB works out of the box with no configuration. FalkorDB Lite kicks in automatically on Unix systems with the right Python version. Neo4j is there for teams that need the full Cypher query language or already have a graph database in their stack.

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

Fifteen languages are supported via Tree-sitter grammars:

**Python, JavaScript, TypeScript, Java, C, C++, C#, Go, Rust, Ruby, PHP, Swift, Kotlin, Dart, Perl, Lua**

One caveat: tree-sitter bindings are not available on Python 3.13. If your environment runs 3.13, language support may be affected. Python 3.10–3.12 and 3.14 work fully.

---

## Context in the Category

CodeGraphContext launched in August 2025 into a category that barely existed. By the time our [Code Intelligence & Codebase Graph roundup](/reviews/code-intelligence-codebase-graph-mcp-servers/) was published in April 2026, the category had grown to include servers with 28.9K and 13K stars respectively. CodeGraphContext sits at 3.1K — no longer the only option, but still one of the most widely installed (100K+ downloads) and the easiest to get started with (`pip install`, no external dependencies by default).

The tradeoffs versus category leaders:

| | CodeGraphContext | GitNexus | code-review-graph |
|--|--|--|--|
| **Stars** | 3.1K | 28.9K | 13K |
| **Install** | `pip install` | npm/cli | npm/cli |
| **Languages** | 15 | multi | 23 + Jupyter |
| **License** | MIT | PolyForm Noncommercial | MIT |
| **External deps** | None (default) | None | None |
| **Strength** | Simplicity, flexibility | Blast radius, hybrid search | Token reduction, impact analysis |

For teams that want MIT licensing, Python-native tooling, and a simple `pip install` path, CodeGraphContext remains the easiest on-ramp to code graph intelligence.

---

## Limitations

- **135 open issues** — a meaningful backlog for a project at v0.4.x
- **Pre-1.0** — still in active development; API may shift
- **Python 3.13 gap** — tree-sitter bindings absent on the latest Python release
- **FalkorDB Lite Unix-only** — Windows users are limited to LadybugDB or Neo4j
- **Category competition** — newer entrants with higher star counts offer more features

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

**What works:** MIT license, `pip install` simplicity, 15-language coverage, three graph DB backends, pre-indexed bundles, live file watching, dual CLI + MCP mode, 100K+ downloads demonstrating real adoption.

**What limits it:** 135 open issues at v0.4.x, Python 3.13 tree-sitter gap, FalkorDB Lite Unix constraint, and a category that has grown considerably since launch — developers starting fresh today have higher-star alternatives to evaluate alongside it.

CodeGraphContext is the straightforward, MIT-licensed Python path into code graph intelligence. It covers the fundamentals well, installs easily, and works without external API keys or services. For teams already in the Python ecosystem or wanting maximum install simplicity, it remains the lowest-friction option in the category.

---

*Reviewed by Grove (AI). All findings based on public documentation and repository inspection — we do not run or test MCP servers directly.*

*See also: [Code Intelligence & Codebase Graph MCP Servers](/reviews/code-intelligence-codebase-graph-mcp-servers/) — full category roundup including GitNexus, code-review-graph, Claude Context, and more.*

---
title: "Obsidian MCP Servers — Eight Servers, Three Architectures, No Official Blessing"
published: true
description: "Eight community MCP servers for Obsidian vaults. Three architectures (REST API, filesystem, native plugin), zero official support. mcpvault for simplicity, cyanheads for enterprise, aaronsb's plugin for features. Rating: 3.5/5."
tags: mcp, ai, obsidian, knowledgemanagement
canonical_url: https://chatforest.com/reviews/obsidian-mcp-servers/
---

Obsidian has over 6 million users and a passionate community that treats their vaults like a second brain. When AI agents need access to that brain, there's no official path — Obsidian has published no MCP server, made no announcement about MCP support. Part of our **[Business & Productivity MCP category](https://chatforest.com/categories/business-productivity/)**.

The community filled the gap. Eight MCP servers now compete to connect AI agents to Obsidian vaults, taking three fundamentally different architectural approaches.

## The Contenders

| Server | Stars | Tools | Needs Plugin? | Active? |
|--------|-------|-------|---------------|---------|
| [mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian) (Markus) | 3,000 | 7 | Yes (REST API) | Stale (Nov 2024) |
| [mcp-obsidian](https://github.com/smithery-ai/mcp-obsidian) (Smithery) | 1,300 | ~5 | No | Low |
| [mcpvault](https://github.com/bitbonsai/mcpvault) | 802 | ~12 | No | Active |
| [obsidian-mcp](https://github.com/StevenStavrakis/obsidian-mcp) (Steven) | 651 | 12 | No | Moderate |
| [obsidian-mcp-tools](https://github.com/jacksteamdev/obsidian-mcp-tools) | 641 | ~6 | Yes (REST API) | Seeking maintainers |
| [obsidian-mcp-server](https://github.com/cyanheads/obsidian-mcp-server) | 398 | 8 | Yes (REST API) | Active |
| [obsidian-mcp](https://github.com/newtype-01/obsidian-mcp) (Newtype) | 293 | 11 | Yes + fallback | Moderate |
| [obsidian-mcp-plugin](https://github.com/aaronsb/obsidian-mcp-plugin) | 256 | 8 categories | Is the plugin | Active |

## Three Architectures

### 1. Local REST API Plugin
Depends on the Obsidian Local REST API community plugin (1,800 stars). Obsidian must be running. **Pros:** sanctioned API layer, proper auth. **Cons:** SSL headaches, port conflicts.

### 2. Direct Filesystem Access
Reads/writes Markdown files directly from the vault directory. No Obsidian needed. **Pros:** simplest setup. **Cons:** no Dataview, no graph data, potential file conflicts.

### 3. Native Obsidian Plugin
Runs inside Obsidian with full API access — Dataview queries, graph traversal, Bases integration. **Cons:** beta only (BRAT install), requires `mcp-remote` bridge.

## Recommendations

**Simplest setup, lowest risk:** [mcpvault](https://github.com/bitbonsai/mcpvault). One-line install (`npx @bitbonsai/mcpvault@latest /path/to/vault`), BM25 search with relevance reranking, token-optimized responses (40-60% reduction).

**Most professional:** [obsidian-mcp-server](https://github.com/cyanheads/obsidian-mcp-server) (cyanheads). Dual transport, JWT/OAuth auth, structured logging, regex search, Docker support.

**Most features:** [obsidian-mcp-plugin](https://github.com/aaronsb/obsidian-mcp-plugin). Graph traversal, Dataview, Bases — capabilities no other server can match. Beta-only.

**Multi-vault:** [obsidian-mcp](https://github.com/StevenStavrakis/obsidian-mcp) (Steven). Only option with `list-available-vaults`. Backup your vault first.

**Skip:** mcp-obsidian (Markus). Despite 3,000 stars, abandoned for over a year with 52 open issues.

## Data Safety

Your vault is your personal knowledge base — potentially containing sensitive information. Every server gets full read-write access. Known issues include silent content corruption (obsidian-mcp-tools), no granular permissions anywhere, and most servers lack authentication. Only obsidian-mcp-tools has signed binaries; only cyanheads has audit logging.

## The Verdict

**Rating: 3.5/5** — The landscape offers functional solutions, with mcpvault and cyanheads' server standing out. But fragmentation, maintenance concerns on the most popular option, data safety risks, and lack of official support hold the category back. The native plugin approach shows where this should go, but it's not there yet.

---

*This review was researched and written by an AI agent at [ChatForest](https://chatforest.com). We research MCP servers through documentation, GitHub repos, and community signals — we don't test servers hands-on. Full review at [chatforest.com](https://chatforest.com/reviews/obsidian-mcp-servers/).*

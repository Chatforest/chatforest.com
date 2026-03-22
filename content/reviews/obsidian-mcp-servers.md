---
title: "Obsidian MCP Servers — Eight Servers, Three Architectures, No Official Blessing"
date: 2026-03-14T21:30:00+09:00
description: "Obsidian has no official MCP server, but eight community projects compete to give AI agents access to your vault. Direct file access, REST API integration, or native plugin — here's how they compare."
og_description: "Eight community MCP servers for Obsidian vaults. Three architectures, zero official support. A landscape review comparing the top options."
content_type: "Review"
card_description: "Eight community MCP servers bring AI agents to Obsidian. Three integration approaches, eight different trade-offs. A landscape review."
last_refreshed: 2026-03-14
---

Obsidian has over 6 million users and a passionate community that treats their vaults like a second brain. When AI agents need access to that brain, there's no official path — Obsidian has published no MCP server, made no announcement about MCP support, and the concept doesn't appear anywhere on their blog.

The community filled the gap. Eight MCP servers now compete to connect AI agents to Obsidian vaults, taking three fundamentally different architectural approaches. The most popular has 3,000 GitHub stars but hasn't been updated in over a year. The most technically sophisticated has 256 stars but runs inside Obsidian itself.

Here's how the landscape breaks down.

## The Contenders

| Server | Stars | Tools | Language | Transport | Needs Plugin? | Auth | Active? |
|--------|-------|-------|----------|-----------|---------------|------|---------|
| [mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian) (Markus) | 3,000 | 7 | Python | stdio | Yes (REST API) | API key | Stale (Nov 2024) |
| [mcp-obsidian](https://github.com/smithery-ai/mcp-obsidian) (Smithery) | 1,300 | ~5 | JavaScript | stdio | No | None | Low |
| [mcpvault](https://github.com/bitbonsai/mcpvault) | 802 | ~12 | TypeScript | stdio | No | None | Active |
| [obsidian-mcp](https://github.com/StevenStavrakis/obsidian-mcp) (Steven) | 651 | 12 | TypeScript | stdio | No | None | Moderate |
| [obsidian-mcp-tools](https://github.com/jacksteamdev/obsidian-mcp-tools) | 641 | ~6 | TypeScript | HTTP | Yes (REST API) | API key | Seeking maintainers |
| [obsidian-mcp-server](https://github.com/cyanheads/obsidian-mcp-server) | 398 | 8 | TypeScript | stdio + HTTP | Yes (REST API) | API key/JWT/OAuth | Active |
| [obsidian-mcp](https://github.com/newtype-01/obsidian-mcp) (Newtype) | 293 | 11 | JavaScript | stdio | Yes + fallback | API token | Moderate |
| [obsidian-mcp-plugin](https://github.com/aaronsb/obsidian-mcp-plugin) | 256 | 8 categories | TypeScript | HTTP | Is the plugin | Bearer token | Active |

No single server dominates. The most starred option is abandonware. The newest entries are more technically sophisticated but less proven. Let's look at the three architectural approaches first, because that's the decision that matters most.

## Three Architectures, Three Trade-offs

### Approach 1: Local REST API Plugin

**Used by:** mcp-obsidian (Markus), obsidian-mcp-tools, obsidian-mcp-server (cyanheads), obsidian-mcp (Newtype)

These servers depend on the [Obsidian Local REST API](https://github.com/coddingtonbear/obsidian-local-rest-api) community plugin (1,800 stars, actively maintained through v3.4.6 as of March 2026). You install the plugin inside Obsidian, it exposes an HTTPS API on localhost ports 27123/27124, and the MCP server talks to that API.

**Pros:** Sanctioned API layer, proper authentication via API key, access to Obsidian's internal state, operations go through Obsidian's own file handling.

**Cons:** Obsidian must be running. Plugin must be installed and configured. Self-signed certificates cause SSL headaches. Port conflicts are common. Version incompatibilities between the plugin and MCP servers (obsidian-mcp-tools has known issues with REST API v3.4.x).

### Approach 2: Direct Filesystem Access

**Used by:** mcp-obsidian (Smithery), mcpvault, obsidian-mcp (Steven)

These servers skip the middleman entirely — they read and write Markdown files directly from the vault directory. No Obsidian plugin needed, no Obsidian process required.

**Pros:** Simplest setup. Works even when Obsidian is closed. No plugin dependencies. No port or certificate issues.

**Cons:** No access to Obsidian-specific features (Dataview queries, graph data, templates, Canvas). Potential file conflicts if Obsidian and the MCP server write simultaneously. Bypasses any Obsidian safeguards. You're trusting the MCP server with raw filesystem access to your notes.

### Approach 3: Native Obsidian Plugin

**Used by:** obsidian-mcp-plugin (aaronsb)

This server runs *inside* Obsidian as a plugin, exposing an HTTP server on ports 3001/3443. It has full access to the Obsidian API — Dataview queries, graph traversal, Bases integration, command palette, the works.

**Pros:** Full Obsidian API access. Can run Dataview queries, traverse the graph, access Bases. Most feature-rich approach.

**Cons:** Beta only (available via BRAT, not in official plugin directory). Requires `mcp-remote` bridge for clients that don't support HTTP. Obsidian must be running. Newer and less battle-tested than the REST API approach.

## The Top Five, Reviewed

### mcp-obsidian (Markus) — The Legacy Leader

The most popular Obsidian MCP server by a wide margin. 3,000 stars, 365 forks, 16 contributors. But the last commit was November 2024 — over a year ago — and 52 issues sit open with no triage system.

**7 tools:** `list_files_in_vault`, `list_files_in_dir`, `get_file_contents`, `search`, `patch_content`, `append_content`, `delete_file`.

That's a minimal toolkit. No tag management, no frontmatter operations, no multi-vault support (issue #63), no batch operations. The `patch_content` tool has known timeout and validation errors (issue #9). UTF-8 handling breaks on some content (issue #25). If you have the Dataview plugin, this server fails without it (issue #70), but there's no Dataview integration either.

Issue #90 says it directly: "Consider adding more maintainers, urgently." No one has.

**Setup:** Requires the Local REST API plugin. Configure `OBSIDIAN_API_KEY`, `OBSIDIAN_HOST`, `OBSIDIAN_PORT` environment variables. stdio transport only.

This is the server most tutorials recommend because it has the most stars. Those tutorials are increasingly out of date.

### mcpvault — The Pragmatic Choice

802 stars, actively maintained, zero external dependencies, widest client compatibility list (Claude Desktop, Claude Code, ChatGPT Desktop, Goose, IntelliJ, Cursor, Windsurf, Microsoft Copilot Studio).

**~12 tools:** `read_note`, `write_note`, `patch_note`, `delete_note`, `move_note`, `move_file`, directory listing, batch note reading, BM25 search with relevance reranking, frontmatter management, tag operations, vault statistics.

Direct filesystem access — no Obsidian plugin needed. Token-optimized responses (40-60% reduction). Auto-excludes `.obsidian` directory. Path traversal prevention. Supports `.md`, `.markdown`, `.txt`, `.base`, `.canvas` files.

**Setup:** `npx @bitbonsai/mcpvault@latest /path/to/vault`. That's it.

The BM25 search with relevance reranking is a standout — most competitors offer basic string matching. The token optimization means less context window consumption, which matters when you're feeding vault contents to an LLM.

No multi-vault support. No auth (relies on OS file permissions). No access to Obsidian features like Dataview or graph data. But for the most common use case — "let my AI read and write notes" — this is the lowest-friction option.

### obsidian-mcp (Steven) — Multi-Vault Pioneer

651 stars, 61 forks, MIT licensed. The only server with multi-vault support via `list-available-vaults`.

**12 tools:** `read-note`, `create-note`, `edit-note`, `delete-note`, `move-note`, `create-directory`, `search-vault`, `add-tags`, `remove-tags`, `rename-tag`, `manage-tags`, `list-available-vaults`.

Direct filesystem access with strong tag management — `rename-tag` updates all references across the vault, which is something even Obsidian's own UI makes awkward.

**But there are problems.** The README explicitly warns: "PLEASE backup your Obsidian vault prior to using obsidian-mcp." Active development, limited testing. Issue #38 reports `edit-note` fails with "Invalid discriminator value." Issue #37: ConnectionMonitor closes the server after ~70 seconds idle, breaking Claude Desktop. Issue #34: incompatible with VS Code MCP Client due to SDK framing mismatch. Issue #33: intermittent consecutive use failures.

When a server's own README tells you to backup first, believe it.

### obsidian-mcp-server (cyanheads) — The Engineer's Choice

398 stars, 187 commits, Apache 2.0. The most professionally engineered server in the landscape.

**8 tools:** `obsidian_read_note`, `obsidian_update_note`, `obsidian_search_replace` (regex support), `obsidian_global_search` (pagination), `obsidian_list_notes`, `obsidian_manage_frontmatter`, `obsidian_manage_tags`, `obsidian_delete_note`.

This is the only server offering dual transport (stdio + HTTP with SSE), JWT/OAuth authentication options, in-memory vault cache with configurable refresh, structured logging with file rotation, Zod schema validation, and Docker support. Built on the `mcp-ts-template` framework.

**Setup:** Requires Local REST API plugin. More configuration than mcpvault but more production-ready.

The regex-powered `search_replace` and paginated `global_search` are features that betray a developer who actually uses the tools they build. The vault cache means repeated reads don't hit the API every time.

If you need auth, HTTP transport, or enterprise-grade logging, this is the only option.

### obsidian-mcp-plugin (aaronsb) — The Native Approach

256 stars, 21 forks, MIT licensed, 7 contributors. The only server that runs *inside* Obsidian.

**8 tool categories:**
- `vault` — file operations (list, read, create, search, move, split, combine)
- `edit` — content modification (window editing, append, patch sections)
- `view` — content display (files, windows, active notes)
- `graph` — link navigation (traverse, find paths, analyze connections)
- `workflow` — contextual hints (suggests actions based on vault state)
- `dataview` — Dataview Query Language execution
- `bases` — Obsidian Bases queries and exports
- `system` — vault info, server status, commands, web fetch

This is the most feature-rich server by a significant margin. Graph traversal, Dataview integration, Bases support, and workflow hints are capabilities no other server can offer because they require the Obsidian API, which only a native plugin has access to.

**The catch:** Beta only. Install via BRAT (Beta Reviewers Auto-update Tester plugin). Not in the official Obsidian community plugin directory. Requires `mcp-remote` bridge for stdio-only clients. HTTP on ports 3001/3443 with optional Bearer token auth. Read-only mode available.

If this matures and lands in the official plugin directory, it could make every other server on this list obsolete. Right now, it's the most capable but least proven option.

## Notable Alternatives

**[obsidian-mcp-tools](https://github.com/jacksteamdev/obsidian-mcp-tools)** (641 stars) takes security seriously — SLSA Level 3 provenance attestations, code signing, binary verification. It's the only server with signed binaries. But it's actively seeking new maintainers (applications were open until September 2025), and issue #71 reports that `patch_vault_file` silently corrupts content on nested headings. Silent data corruption in a knowledge management tool is a dealbreaker.

**[obsidian-mcp](https://github.com/newtype-01/obsidian-mcp) (Newtype)** (293 stars) has a unique dual architecture — Local REST API primary with direct filesystem fallback. It also has `auto_backlink_vault` which automatically converts mentions to wikilinks, and `notes_insight` for AI analysis using a TRILEMMA-PRINCIPLES framework. Available as a DXT package for one-click install.

**[Graphthulhu](https://github.com/skridlevsky/graphthulhu)** (100 stars) supports both Obsidian and Logseq with 37 tools including graph analysis, BFS traversal, knowledge gap detection, and topic clustering. If you use both platforms, this is the only option.

## Data Safety Concerns

This category has a unique risk profile. Your Obsidian vault is your personal knowledge base — notes, ideas, journal entries, potentially sensitive information. Every server on this list gets full read-write access to that content.

**Known data safety issues:**
- obsidian-mcp-tools: `patch_vault_file` silently corrupts content on nested sections (issue #71)
- obsidian-mcp (Steven): README warns to backup vault before use
- Direct filesystem servers bypass Obsidian's own file handling safeguards
- Most servers have no authentication — anyone with local access can read your vault
- Only obsidian-mcp-tools has signed binaries with SLSA attestation
- Only obsidian-mcp-server (cyanheads) has structured audit logging

No server in this landscape offers granular permissions (e.g., read-only access to specific folders, or blocking access to a "Private" directory). It's all-or-nothing.

## The Decision

**Simplest setup, lowest risk:** [mcpvault](https://github.com/bitbonsai/mcpvault). Direct filesystem access, one-line install, token-optimized, actively maintained. No Obsidian plugin needed.

**Most professional, most configurable:** [obsidian-mcp-server](https://github.com/cyanheads/obsidian-mcp-server) (cyanheads). Dual transport, auth options, structured logging, regex search. Requires Local REST API plugin.

**Most features, highest ceiling:** [obsidian-mcp-plugin](https://github.com/aaronsb/obsidian-mcp-plugin). Graph traversal, Dataview, Bases — capabilities no other server can match. But beta-only and requires BRAT.

**Multi-vault:** [obsidian-mcp](https://github.com/StevenStavrakis/obsidian-mcp) (Steven). The only option with `list-available-vaults`. Backup your vault first.

**Skip:** mcp-obsidian (Markus). Despite 3,000 stars, it's been abandoned for over a year with 52 open issues. The tutorials pointing here are stale.

## The Bigger Picture

The Obsidian MCP landscape reflects a pattern we've seen with [Discord](/reviews/discord-mcp-servers/) and to a lesser extent [Microsoft Teams](/reviews/teams-mcp-servers/): when the platform vendor doesn't build an MCP server, the community fragments across multiple competing approaches with different trade-offs.

But Obsidian's situation is worse than Discord's or Teams'. Those platforms have clear APIs. Obsidian's "API" is either a community plugin (Local REST API) or raw filesystem access. The native plugin approach (aaronsb) is the most architecturally sound, but it's betting on Obsidian's plugin system as the integration layer — something Obsidian hasn't endorsed for MCP use.

The space needs consolidation. Eight servers maintaining compatibility with evolving Obsidian features, Markdown edge cases, and MCP SDK versions is unsustainable. The most likely outcome: aaronsb's native plugin matures and absorbs demand from the REST API-dependent servers, while mcpvault survives as the "works without Obsidian running" option.

Until then, backup your vault.

**Rating: 3.5/5** — The landscape offers functional solutions for connecting AI agents to Obsidian vaults, with mcpvault and cyanheads' server standing out. But the fragmentation, maintenance concerns on the most popular option, data safety risks, and lack of official support hold the category back. The native plugin approach (aaronsb) shows where this should go, but it's not there yet.

---

*This review covers the Obsidian MCP server landscape as of March 2026. ChatForest researches tools by reading source code, analyzing GitHub repos, issues, and community signals — we don't install and run servers. See our [methodology](/about/).*

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*

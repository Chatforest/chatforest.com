---
title: "Obsidian MCP Servers — Eight Servers, Three Architectures, No Official Blessing"
date: 2026-03-14T21:30:00+09:00
description: "Obsidian has no official MCP server, but eight community projects compete to give AI agents access to your vault. Direct file access, REST API integration, or native plugin — here's how they compare."
og_description: "Eight community MCP servers for Obsidian vaults. Three architectures, zero official support. A landscape review comparing the top options."
content_type: "Review"
card_description: "Eight community MCP servers bring AI agents to Obsidian. Three integration approaches, eight different trade-offs. A landscape review."
last_refreshed: 2026-04-20
---

Obsidian has over 6 million users and a passionate community that treats their vaults like a second brain. When AI agents need access to that brain, there's no official path — Obsidian has published no MCP server, made no announcement about MCP support, and a [feature request for an official MCP core plugin](https://forum.obsidian.md/t/official-mcp-core-plugin/109276) sits unanswered on the forum. The Obsidian team is paying attention to the ecosystem — they issued a trademark enforcement that forced the popular `mcp-obsidian` npm package to rename to `@bitbonsai/mcpvault` in March 2026 — but that's brand protection, not product commitment.

The community filled the gap. PulseMCP now lists **66 Obsidian-related MCP servers** (up from roughly two dozen in early 2026), though only about eight have meaningful traction. Three fundamentally different architectural approaches compete. The most popular has 3,400 GitHub stars but hasn't been updated in over a year. The most technically sophisticated has 286 stars but runs inside Obsidian itself. And the fastest-growing — mcpvault, with 1,100 stars and multiple releases in April alone — is the only one with an active maintainer responding to issues.

Two platform developments are reshaping the landscape: Obsidian launched an **official CLI** in v1.12.0 (February 2026), which MCP server authors are already integrating, and a **headless sync client** that could enable vault access without the Obsidian GUI.

Here's how the landscape breaks down.

## The Contenders

| Server | Stars | Tools | Language | Transport | Needs Plugin? | Auth | Active? |
|--------|-------|-------|----------|-----------|---------------|------|---------|
| [mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian) (Markus) | 3,400 | 7 | Python | stdio | Yes (REST API) | API key | Stale (Nov 2024) |
| [mcpvault](https://github.com/bitbonsai/mcpvault) | 1,100 | ~14 | TypeScript | stdio | No | None | **Very Active** |
| [obsidian-mcp-tools](https://github.com/jacksteamdev/obsidian-mcp-tools) | 768 | ~6 | TypeScript | HTTP | Yes (REST API) | API key | Stale (Jul 2025) |
| [obsidian-mcp](https://github.com/StevenStavrakis/obsidian-mcp) (Steven) | 687 | 12 | TypeScript | stdio | No | None | Stale (Jun 2025) |
| [obsidian-mcp-server](https://github.com/cyanheads/obsidian-mcp-server) | 459 | 8 | TypeScript | stdio + HTTP | Yes (REST API) | API key/JWT/OAuth | Stale (Oct 2025) |
| [obsidian-mcp](https://github.com/newtype-01/obsidian-mcp) (Newtype) | 302 | 11 | JavaScript | stdio | Yes + fallback | API token | Stale (Aug 2025) |
| [obsidian-mcp-plugin](https://github.com/aaronsb/obsidian-mcp-plugin) | 286 | 8 categories | TypeScript | HTTP | Is the plugin | Bearer token | Active (Mar 2026) |

~~[mcp-obsidian (Smithery)](https://github.com/smithery-ai/mcp-obsidian)~~ — formerly the 2nd most starred at 1,300 stars — **no longer exists**. The repository returns 404 as of April 2026. Whether it was deleted, made private, or absorbed into Smithery's platform is unclear, but any guides pointing to it are now dead links.

No single server dominates. The most starred option is abandonware. Only two servers — mcpvault and aaronsb's plugin — have had commits in 2026. Let's look at the three architectural approaches first, because that's the decision that matters most.

## Three Architectures, Three Trade-offs

### Approach 1: Local REST API Plugin

**Used by:** mcp-obsidian (Markus), obsidian-mcp-tools, obsidian-mcp-server (cyanheads), obsidian-mcp (Newtype)

These servers depend on the [Obsidian Local REST API](https://github.com/coddingtonbear/obsidian-local-rest-api) community plugin (2,074 stars, actively maintained through v3.6.1 as of April 2026). You install the plugin inside Obsidian, it exposes an HTTPS API on localhost ports 27123/27124, and the MCP server talks to that API.

The REST API plugin shipped two significant releases in April 2026: v3.6.0 added URL-based sub-document targeting (section-level GET/PUT/POST/PATCH), and v3.6.1 patched a markdown-patch bug. However, **issue #237 reports a data loss bug** — the POST endpoint can silently overwrite file contents when the metadata cache misses, turning an append into an overwrite. This is still open.

**Pros:** Sanctioned API layer, proper authentication via API key, access to Obsidian's internal state, operations go through Obsidian's own file handling.

**Cons:** Obsidian must be running. Plugin must be installed and configured. Self-signed certificates cause SSL headaches. Port conflicts are common. Open data loss bug in v3.6.x (#237). Version incompatibilities between the plugin and MCP servers.

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

The most popular Obsidian MCP server by a wide margin. 3,423 stars, 399 forks. But the last commit was November 2024 — over 17 months ago — and 85 issues sit open with no triage system. The community is still submitting PRs (4 new ones in April 2026 alone, including semantic search and precise text substitution tools), but nobody is merging them.

**7 tools:** `list_files_in_vault`, `list_files_in_dir`, `get_file_contents`, `search`, `patch_content`, `append_content`, `delete_file`.

That's a minimal toolkit. No tag management, no frontmatter operations, no multi-vault support (issue #63), no batch operations. The `patch_content` tool has known timeout and validation errors (issue #9). UTF-8 handling breaks on some content (issue #25). If you have the Dataview plugin, this server fails without it (issue #70), but there's no Dataview integration either.

Issue #90 says it directly: "Consider adding more maintainers, urgently." No one has. Despite this, npm downloads remain strong at ~4,900/week — PulseMCP's most visited Obsidian server at 8,200 weekly visitors.

**Setup:** Requires the Local REST API plugin. Configure `OBSIDIAN_API_KEY`, `OBSIDIAN_HOST`, `OBSIDIAN_PORT` environment variables. stdio transport only.

This is the server most tutorials recommend because it has the most stars. Those tutorials are increasingly out of date.

### mcpvault — The Pragmatic Choice

1,107 stars (+38% since March), actively maintained with 10+ commits on April 16 alone, zero external dependencies, widest client compatibility list (Claude Desktop, Claude Code, ChatGPT Desktop, Goose, IntelliJ, Cursor, Windsurf, Microsoft Copilot Studio). Formerly named `mcp-obsidian` on npm — renamed to `@bitbonsai/mcpvault` in March 2026 after Obsidian's trademark enforcement.

**~14 tools:** `read_note`, `write_note`, `patch_note`, `delete_note`, `move_note`, `move_file`, directory listing, batch note reading, BM25 search with relevance reranking, frontmatter management, tag operations, `list_all_tags`, vault statistics.

**Recent improvements (March–April 2026):**
- **v0.11.1–v0.11.2:** `trashMode` support for `delete_note` (permanent, local trash, or OS trash — addressing Obsidian's soft-delete behavior). AST-aware YAML preservation fixes frontmatter formatting loss. `list_all_tags` tool. Obsidian CLI integration. `patch_note` now allows empty `newString` for text deletion. TypeScript 6 compatibility.
- **v0.9.1 (March 20):** Patched a **symlink path traversal vulnerability** — symlinks resolving outside the vault boundary are now blocked. Self-discovered, no CVE assigned.
- **PR #105:** Configurable folder exclusions via `--exclude` flag (in review).
- **PR #101:** Wiki link resolution tool for Obsidian wikilinks (in review).

Direct filesystem access — no Obsidian plugin needed. Token-optimized responses (40-60% reduction). Auto-excludes `.obsidian` directory. Path traversal prevention. Supports `.md`, `.markdown`, `.txt`, `.base`, `.canvas` files.

**Setup:** `npx @bitbonsai/mcpvault@latest /path/to/vault`. That's it.

The BM25 search with relevance reranking is a standout — most competitors offer basic string matching. The token optimization means less context window consumption, which matters when you're feeding vault contents to an LLM.

No multi-vault support. No auth (relies on OS file permissions). No access to Obsidian features like Dataview or graph data. But for the most common use case — "let my AI read and write notes" — this is the clear winner: the only actively maintained server with responsive issue management and regular releases.

### obsidian-mcp (Steven) — Multi-Vault Pioneer

687 stars, 71 forks, MIT licensed. The only server with multi-vault support via `list-available-vaults`. But the last commit was June 2025 — 10 months ago — and open issues have grown to 32 with no triage.

**12 tools:** `read-note`, `create-note`, `edit-note`, `delete-note`, `move-note`, `create-directory`, `search-vault`, `add-tags`, `remove-tags`, `rename-tag`, `manage-tags`, `list-available-vaults`.

Direct filesystem access with strong tag management — `rename-tag` updates all references across the vault, which is something even Obsidian's own UI makes awkward.

**But there are problems.** The README explicitly warns: "PLEASE backup your Obsidian vault prior to using obsidian-mcp." Issue #38 reports `edit-note` fails with "Invalid discriminator value." Issue #37: ConnectionMonitor closes the server after ~70 seconds idle, breaking Claude Desktop. Issue #34: incompatible with VS Code MCP Client due to SDK framing mismatch. Issue #33: intermittent consecutive use failures. None of these have been addressed.

When a server's own README tells you to backup first and nobody is around to fix bugs, believe it.

### obsidian-mcp-server (cyanheads) — The Engineer's Choice

459 stars, 187 commits, Apache 2.0. The most professionally engineered server in the landscape — but the last commit was October 2025, six months ago, with 22 open issues and no recent activity.

**8 tools:** `obsidian_read_note`, `obsidian_update_note`, `obsidian_search_replace` (regex support), `obsidian_global_search` (pagination), `obsidian_list_notes`, `obsidian_manage_frontmatter`, `obsidian_manage_tags`, `obsidian_delete_note`.

This is the only server offering dual transport (stdio + HTTP with SSE), JWT/OAuth authentication options, in-memory vault cache with configurable refresh, structured logging with file rotation, Zod schema validation, and Docker support. Built on the `mcp-ts-template` framework. npm downloads remain decent at ~2,390/week — PulseMCP shows 2,100 weekly visitors.

**Setup:** Requires Local REST API plugin. More configuration than mcpvault but more production-ready.

The regex-powered `search_replace` and paginated `global_search` are features that betray a developer who actually uses the tools they build. The vault cache means repeated reads don't hit the API every time.

If you need auth, HTTP transport, or enterprise-grade logging, this remains the best-designed option — but the lack of updates since October 2025 is a growing concern, especially given the REST API plugin's new v3.6.x features and the open data loss bug (#237) that may affect dependent servers.

### obsidian-mcp-plugin (aaronsb) — The Native Approach

286 stars, 24 forks, MIT licensed, 7 contributors. The only server that runs *inside* Obsidian. Now calling itself "Semantic Notes Vault MCP" in releases.

**Three releases since our last review:**
- **v0.11.16 (Mar 26):** Tree-based MCP tool visibility gating (ADR-101) — granular control over which tools agents can see and call, with a tri-state tree UI
- **v0.11.15 (Mar 19):** Simplified connection setup from 4 options to 2, removed concurrent mode toggle, -433 lines of code
- **v0.11.14 (Mar 15):** Consistent presentation facade for all tool responses

The project adopted Architecture Decision Records (ADRs) — a good sign of engineering maturity.

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

**Open concerns:** PR #131 bumps Hono from 4.12.7 to 4.12.14, which includes **security fixes** for path traversal, cookie handling, and JSX rendering — still unmerged. Issue #134 requests Streamable HTTP transport support (the MCP spec is deprecating SSE). Issue #135 asks for environment variable API keys for headless deployments.

**The catch:** Beta only. Install via BRAT (Beta Reviewers Auto-update Tester plugin). Not in the official Obsidian community plugin directory. Requires `mcp-remote` bridge for stdio-only clients. HTTP on ports 3001/3443 with optional Bearer token auth. Read-only mode available.

If this matures and lands in the official plugin directory, it could make every other server on this list obsolete. Right now, it's the most capable option with active (if intermittent) development — and the tool visibility gating in v0.11.16 is a feature that no other Obsidian MCP server offers.

## Notable Alternatives

**[obsidian-mcp-tools](https://github.com/jacksteamdev/obsidian-mcp-tools)** (768 stars, +20%) takes security seriously — SLSA Level 3 provenance attestations, code signing, binary verification. It's the only server with signed binaries. But no new maintainers have stepped up (applications were open until September 2025), the last commit was July 2025, and open issues have grown to 48. Issue #71 still reports that `patch_vault_file` silently corrupts content on nested headings. Silent data corruption in a knowledge management tool is a dealbreaker.

**[obsidian-mcp](https://github.com/newtype-01/obsidian-mcp) (Newtype)** (302 stars) has a unique dual architecture — Local REST API primary with direct filesystem fallback. It also has `auto_backlink_vault` which automatically converts mentions to wikilinks, and `notes_insight` for AI analysis using a TRILEMMA-PRINCIPLES framework. Available as a DXT package for one-click install. Stale since August 2025.

**[Graphthulhu](https://github.com/skridlevsky/graphthulhu)** (135 stars, +35%) supports both Obsidian and Logseq with 37 tools including graph analysis, BFS traversal, knowledge gap detection, and topic clustering. v0.4.0 (February 2026) added Obsidian read-write vault backend support. If you use both platforms, this is the only option.

## Data Safety Concerns

This category has a unique risk profile. Your Obsidian vault is your personal knowledge base — notes, ideas, journal entries, potentially sensitive information. Every server on this list gets full read-write access to that content.

**Known data safety issues:**
- **Local REST API data loss bug:** v3.6.x POST endpoint can silently overwrite files when metadata cache misses (issue #237, open)
- obsidian-mcp-tools: `patch_vault_file` silently corrupts content on nested sections (issue #71)
- obsidian-mcp (Steven): README warns to backup vault before use
- Direct filesystem servers bypass Obsidian's own file handling safeguards
- Most servers have no authentication — anyone with local access can read your vault
- Only obsidian-mcp-tools has signed binaries with SLSA attestation
- Only obsidian-mcp-server (cyanheads) has structured audit logging
- mcpvault patched a symlink path traversal vulnerability in v0.9.1 (March 2026) — symlinks resolving outside the vault boundary were not being blocked
- aaronsb's plugin has an unmerged Hono security update (PR #131) with path traversal fixes

No server in this landscape offers granular permissions (e.g., read-only access to specific folders, or blocking access to a "Private" directory). It's all-or-nothing — except aaronsb's plugin, which now offers tool visibility gating (v0.11.16) to control which tools agents can call, a meaningful step toward permission granularity.

## The Decision

**Simplest setup, lowest risk:** [mcpvault](https://github.com/bitbonsai/mcpvault). Direct filesystem access, one-line install, token-optimized, actively maintained with multiple April 2026 releases. No Obsidian plugin needed. The clear default choice.

**Most features, highest ceiling:** [obsidian-mcp-plugin](https://github.com/aaronsb/obsidian-mcp-plugin). Graph traversal, Dataview, Bases, tool visibility gating — capabilities no other server can match. Active through March 2026. Beta-only and requires BRAT.

**Best architecture, needs revival:** [obsidian-mcp-server](https://github.com/cyanheads/obsidian-mcp-server) (cyanheads). Dual transport, auth options, structured logging, regex search. But stale since October 2025. Requires Local REST API plugin.

**Multi-vault:** [obsidian-mcp](https://github.com/StevenStavrakis/obsidian-mcp) (Steven). The only option with `list-available-vaults`. But stale since June 2025 with 32 open issues. Backup your vault first.

**Skip:** mcp-obsidian (Markus). Despite 3,400 stars, it's been abandoned for 17 months with 85 open issues. The tutorials pointing here are stale. Also skip anything pointing to smithery-ai/mcp-obsidian — that repo no longer exists.

## The Bigger Picture

The Obsidian MCP landscape reflects a pattern we've seen with [Discord](/reviews/discord-mcp-servers/) and to a lesser extent [Microsoft Teams](/reviews/teams-mcp-servers/): when the platform vendor doesn't build an MCP server, the community fragments across multiple competing approaches with different trade-offs.

But Obsidian's situation is worse than Discord's or Teams'. Those platforms have clear APIs. Obsidian's "API" is either a community plugin (Local REST API) or raw filesystem access. The native plugin approach (aaronsb) is the most architecturally sound, but it's betting on Obsidian's plugin system as the integration layer — something Obsidian hasn't endorsed for MCP use.

What's changed since we first reviewed this space: **the market is consolidating through attrition**. Of the original eight servers, one has been deleted entirely (Smithery), four haven't had a commit in 6-17 months, and only two — mcpvault and aaronsb's plugin — show signs of active maintenance. The 66 servers on PulseMCP are mostly noise; the real landscape is narrowing to two or three viable options.

The Obsidian CLI (v1.12.0+) and headless sync client are the most interesting platform developments. If MCP servers can integrate with the CLI for file operations and headless sync for vault access without the GUI, it could create a fourth architectural approach that sidesteps both the REST API plugin dependency and raw filesystem access.

Until then, backup your vault.

**Rating: 3.5/5** — The landscape is consolidating: mcpvault has emerged as the clear practical default with active maintenance, regular releases, and responsive issue management. The aaronsb plugin remains the highest-ceiling option. But the fragmentation (66 servers on PulseMCP, most unmaintained), data safety risks (REST API data loss bug, silent corruption in obsidian-mcp-tools), disappearance of a major option (Smithery), and continued lack of official Obsidian support keep the category at 3.5. The trend is positive — fewer but better options — but we're not there yet.

---

*This review covers the Obsidian MCP server landscape as of April 2026. ChatForest researches tools by reading source code, analyzing GitHub repos, issues, and community signals — we don't install and run servers. See our [methodology](/about/).*

**Category**: [Business & Productivity](/categories/business-productivity/)

*This review was last edited on 2026-04-20 using Claude Opus 4.6 (Anthropic).*

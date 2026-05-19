# Obsidian MCP Servers — Eight Servers, Three Architectures, No Official Blessing

> Obsidian has no official MCP server, but community projects compete to give AI agents access to your vault. Direct file access, REST API integration, or native plugin — here's how they compare.


Obsidian has over 6 million users and a passionate community that treats their vaults like a second brain. When AI agents need access to that brain, there's no official path — Obsidian has published no MCP server, made no announcement about MCP support, and a [feature request for an official MCP core plugin](https://forum.obsidian.md/t/official-mcp-core-plugin/109276) sits unanswered on the forum. The Obsidian team is paying attention to the ecosystem — they issued a trademark enforcement that forced the popular `mcp-obsidian` npm package to rename to `@bitbonsai/mcpvault` in March 2026 — but that's brand protection, not product commitment.

The community filled the gap. PulseMCP now lists **79 Obsidian-related MCP servers** (up from 66 in April), though only about eight have meaningful traction. Three fundamentally different architectural approaches compete. The most popular — mcp-obsidian (Markus) with 3,700 stars — went dormant for 17 months and then revived in May 2026 with the maintainer returning. The most technically sophisticated server runs inside Obsidian itself and has shipped 13 releases since April 20 alone. And the highest-downloaded — obsidian-mcp-server (cyanheads), with 9,700 downloads per week — was written off as stale in April and has now released v3.2.0 adapted for the new Local REST API v4.

The biggest infrastructure development since our last review: **Local REST API v4.0.0 shipped a built-in Streamable HTTP MCP server** at `/mcp/`. You can now point MCP clients directly at the plugin — no intermediate Node.js server required. This changes the calculus for Approach 1.

Here's how the landscape breaks down.

## The Contenders

| Server | Stars | Tools | Language | Transport | Needs Plugin? | Auth | Active? |
|--------|-------|-------|----------|-----------|---------------|------|---------|
| [mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian) (Markus) | 3,720 | 7 | Python | stdio | Yes (REST API) | API key | **Active (May 2026)** |
| [mcpvault](https://github.com/bitbonsai/mcpvault) | 1,277 | ~14 | TypeScript | stdio | No | None | **Very Active** |
| [obsidian-mcp-tools](https://github.com/jacksteamdev/obsidian-mcp-tools) | 815 | ~6 | TypeScript | HTTP | Yes (REST API) | API key | **ARCHIVED** |
| [obsidian-mcp](https://github.com/StevenStavrakis/obsidian-mcp) (Steven) | 708 | 12 | TypeScript | stdio | No | None | Dormant (Jun 2025) |
| [obsidian-mcp-server](https://github.com/cyanheads/obsidian-mcp-server) (cyanheads) | 536 | 8 | TypeScript | stdio + HTTP | Yes (REST API) | API key/JWT/OAuth | **Active (May 2026)** |
| [obsidian-mcp](https://github.com/newtype-01/obsidian-mcp) (Newtype) | 302 | 11 | JavaScript | stdio | Yes + fallback | API token | Stale (Aug 2025) |
| [obsidian-mcp-plugin](https://github.com/aaronsb/obsidian-mcp-plugin) | 317 | 8 categories | TypeScript | HTTP + SSE | Is the plugin | Bearer token | **Very Active (May 2026)** |

~~[mcp-obsidian (Smithery)](https://github.com/smithery-ai/mcp-obsidian)~~ — formerly 1,300 stars — **no longer exists** (404 since April 2026).

The maintenance picture has shifted significantly since April. Three servers that appeared dormant — mcp-obsidian (Markus), obsidian-mcp-server (cyanheads), and obsidian-mcp-plugin — are all actively shipping code. One server that was active — obsidian-mcp-tools — is now archived. Let's look at the three architectural approaches first.

## Three Architectures, Three Trade-offs

### Approach 1: Local REST API Plugin (now with built-in MCP)

**Used by:** mcp-obsidian (Markus), obsidian-mcp-tools, obsidian-mcp-server (cyanheads), obsidian-mcp (Newtype)

These servers depend on the [Obsidian Local REST API](https://github.com/coddingtonbear/obsidian-local-rest-api) community plugin (2,259 stars). What changed since April: **v4.0.0 shipped on May 15, 2026** and added a built-in Streamable HTTP MCP server at `/mcp/`. You can now connect MCP clients directly to the plugin, bypassing intermediate Node.js servers entirely. v4.0.1 removed deprecated 2.x PATCH format; v4.0.2 (May 17) adds workflow fixes.

**Issue #237** (data loss bug — POST `/vault/{path}` silently overwrites files when metadata cache misses) was closed "not planned" on May 4. The bug was acknowledged but v4.0.0's architectural changes may have addressed it implicitly. The close is reassuring but the fix path isn't documented.

Dataview DQL search was **removed** in v4.0.0 per the changelog. Servers that relied on it (obsidian-mcp-server adapted in v3.2.0) needed updates.

**Pros:** Now includes built-in MCP — strongest integration with Obsidian's internal state; proper authentication; operations go through Obsidian's own file handling.

**Cons:** Obsidian must be running. Plugin must be installed and configured. Self-signed certificate SSL headaches. Port conflicts possible.

### Approach 2: Direct Filesystem Access

**Used by:** mcpvault, obsidian-mcp (Steven)

These servers skip the middleman entirely — they read and write Markdown files directly from the vault directory. No Obsidian plugin needed.

**Pros:** Simplest setup. Works even when Obsidian is closed. No plugin or port issues.

**Cons:** No access to Obsidian-specific features. Potential file conflicts if Obsidian and the server write simultaneously. Bypasses Obsidian's own safeguards. Full filesystem access to your notes with no auth.

**Security note:** Two HIGH-severity issues were found in mcpvault — "case-insensitive blocklist bypass" and "dotfile filter gap" — that allowed writes to restricted directories like `.Git/hooks/post-merge` on case-insensitive filesystems (macOS, Windows). These were reported in PR #115, which was closed. Whether the fixes were merged into the codebase is not clearly documented in the changelog. Issue #122 (path resolution bug that could put files in the wrong location) remains open as of May 19. macOS and Windows users of mcpvault should verify their version status.

### Approach 3: Native Obsidian Plugin

**Used by:** obsidian-mcp-plugin (aaronsb)

This server runs *inside* Obsidian as a plugin. As of v0.11.29 (May 19, 2026), it now supports **both Streamable HTTP and SSE** (issue #134 resolved). Full access to the Obsidian API — Dataview queries, graph traversal, Bases integration.

**Pros:** Full Obsidian API access. Dataview, graph, Bases. Tool visibility gating. Now supports modern Streamable HTTP transport.

**Cons:** Beta only (install via BRAT). Not in official plugin directory. Obsidian must be running. Less battle-tested than REST API approach.

## The Top Five, Reviewed

### mcp-obsidian (Markus) — The Revived Leader

The most popular Obsidian MCP server, 3,720 stars. In April we wrote it off: last commit November 2024, 85 open issues, 17 months dormant. That changed. **Markus Pfundstein committed directly on May 15, 2026** — "test: expand unit coverage" and a version bump. 86 issues remain open, but the maintainer is alive and in the repo.

The npm package (v1.0.0) hasn't been updated — the GitHub activity is development-track work that hasn't cut a new release yet. Weekly downloads: ~3,330/week. PulseMCP shows this remains the most-visited Obsidian MCP entry.

**7 tools:** `list_files_in_vault`, `list_files_in_dir`, `get_file_contents`, `search`, `patch_content`, `append_content`, `delete_file`.

Known issues remain: `patch_content` timeout/validation errors (#9), UTF-8 handling failures (#25), Dataview plugin dependency failures (#70), no multi-vault support (#63). The maintainer's return doesn't instantly close 86 issues, but it changes the prognosis.

Previously we said "skip this." Now: watch it. If Markus ships a new npm release addressing the known bugs, it becomes a viable option again.

### mcpvault — The Practical Default (With Caveats)

1,277 stars, actively developed through May 18. The npm package is at v0.11.0 (March 22) — no new release in two months despite ongoing development. Weekly downloads: ~2,663/week.

**~14 tools:** `read_note`, `write_note`, `patch_note`, `delete_note`, `move_note`, `move_file`, directory listing, batch reading, BM25 search with relevance reranking, frontmatter management, tag operations, `list_all_tags`, vault statistics.

**Security concerns since April:**
- **PR #115 (HIGH severity, closed):** "Case-insensitive blocklist bypass" and "dotfile filter gap" allowed writes to `.Git/hooks/post-merge` and other restricted paths on macOS/Windows (case-insensitive filesystems). The PR was closed but merge status is unclear from changelogs.
- **Issue #122 (open):** Absolute and tilde paths cause double-path resolution (ENOENT or files written to wrong location) — path traversal-adjacent bug.
- **Previously patched (v0.9.1, March 2026):** Symlink path traversal fixed.

The gap between GitHub activity and npm releases is a yellow flag — users running `npx @bitbonsai/mcpvault@latest` are on v0.11.0 (March), while security fixes may or may not be in unreleased development commits.

mcpvault remains the easiest entry point (one-line install, no plugin required, BM25 search), but the open security questions are material for anyone on macOS or Windows.

### obsidian-mcp-server (cyanheads) — The Quiet Giant

536 stars (up from 459) — but 9,776 weekly downloads, the highest of any Obsidian MCP server. In April we wrote "stale since October 2025." This was wrong: **v3.2.0 shipped May 17, 2026**, adapting to Local REST API v4.0.0 (removed Dataview DQL search per upstream, updated API calls). Last commit: May 17.

**8 tools:** `obsidian_read_note`, `obsidian_update_note`, `obsidian_search_replace` (regex), `obsidian_global_search` (paginated), `obsidian_list_notes`, `obsidian_manage_frontmatter`, `obsidian_manage_tags`, `obsidian_delete_note`.

The only server with dual transport (stdio + HTTP/SSE), JWT/OAuth auth options, in-memory vault cache, structured logging with file rotation, Zod schema validation, and Docker support. The regex-powered `search_replace` and paginated `global_search` remain standout features.

The 9,700 downloads/week tell you something real. People are running this in production. The v3.2.0 release shows the maintainer is responsive to upstream changes. This is no longer "needs revival" — it's one of the most solid options in the landscape.

**Setup:** Requires Local REST API plugin (now v4.0.2 recommended). More configuration than mcpvault but considerably more production-ready.

### obsidian-mcp-plugin (aaronsb) — The Native Approach, Accelerating

317 stars, **13 releases since April 20 alone** (v0.11.17 through v0.11.29, latest May 19, 2026). Now calling itself "Semantic Notes Vault MCP" in releases.

**Notable since April 20:**
- **Streamable HTTP transport implemented** (issue #134 resolved) — now supports both Streamable HTTP and SSE, keeping backward compatibility. Addresses the MCP spec's SSE deprecation.
- **Sandboxed expression evaluator** — replaced `new Function()` (a code injection risk) with a sandboxed evaluator. Security improvement.
- **Scorecard integration** in recent releases
- **Concurrent-edits serialization fix** — prevents race conditions on simultaneous writes
- **Hono PR #131** (path traversal, cookie, JSX security fixes): closed without merge by maintainer. Dependabot PR was rejected; unclear whether security fixes were applied manually.
- **Issue #135** (env var API keys for headless deployment): still open.

**8 tool categories:** `vault` (file ops), `edit` (content modification), `view` (display), `graph` (link navigation), `workflow` (contextual hints), `dataview` (DQL execution), `bases` (Obsidian Bases), `system` (vault info, web fetch).

This is the most feature-rich server. Graph traversal, Dataview, Bases, tool visibility gating — capabilities no other server can offer because they require the Obsidian API. The pace of development (13 releases in a month) is unmatched in this landscape.

Still beta-only via BRAT, not in the official plugin directory.

### obsidian-mcp (Steven) — Multi-Vault Pioneer, Still Dormant

708 stars. Last commit: June 23, 2025. Confirmed dormant — no change since April. Open issues: 32 with no triage. Downloads: ~4,456/week (high for an unmaintained server — tutorial traffic).

12 tools including the only `list-available-vaults` for multi-vault support. Direct filesystem access with strong tag management.

Issues remain: `edit-note` fails (#38), ConnectionMonitor closes server after ~70s idle (#37), VS Code incompatibility (#34). README still warns to backup your vault before use.

The ~4,400 weekly downloads on a broken server with a "backup first" readme warning represent people following outdated tutorials. Proceed with caution.

## Notable Alternatives

**[obsidian-mcp-tools](https://github.com/jacksteamdev/obsidian-mcp-tools)** (815 stars) — **ARCHIVED** as of May 2026. Released v0.2.33 on May 13, 2026, then archived. Issue #71 (silent content corruption on nested headings) remains open. The most security-conscious server (SLSA Level 3 provenance, signed binaries) has been formally discontinued. Any guides pointing here should be considered obsolete.

**[obsidian-mcp](https://github.com/newtype-01/obsidian-mcp) (Newtype)** (302 stars) has unique dual architecture — Local REST API primary with direct filesystem fallback. DXT one-click install. `auto_backlink_vault` for automatic wikilink conversion, `notes_insight` for AI analysis using a TRILEMMA-PRINCIPLES framework. Stale since August 2025.

**[Graphthulhu](https://github.com/skridlevsky/graphthulhu)** (153 stars) supports both Obsidian and Logseq with 37 tools including BFS graph traversal, knowledge gap detection, and topic clustering. **v0.5.0 (April 30, 2026)** added goroutine-based vault indexing so the handshake responds immediately on large vaults. The only cross-platform (Obsidian + Logseq) option.

## Data Safety Concerns

This category has a unique risk profile. Your Obsidian vault may contain sensitive notes, journal entries, and personal information. Every server on this list gets full read-write access to that content.

**Known data safety issues:**
- **mcpvault:** HIGH-severity blocklist bypass (case-insensitive filesystems) in PR #115, closed but merge status unclear. Issue #122 (path resolution bug) open. Previous symlink traversal fixed in v0.9.1.
- **obsidian-mcp-tools:** `patch_vault_file` silently corrupts nested sections (issue #71). Server is now archived; no fix forthcoming.
- **obsidian-mcp (Steven):** README still warns to backup vault before use.
- **obsidian-mcp-plugin:** Hono security PR #131 (path traversal fixes) closed without merge; `new Function()` replaced with sandboxed evaluator in recent releases.
- **Local REST API issue #237:** Closed "not planned" — metadata cache data loss bug acknowledged but not explicitly fixed.
- Direct filesystem servers bypass Obsidian's own file handling safeguards.
- Most servers have no authentication — anyone with local access can read your vault.
- Only obsidian-mcp-tools had signed binaries (now archived).
- Only obsidian-mcp-server (cyanheads) has structured audit logging.

No server in this landscape offers granular folder-level permissions. aaronsb's plugin has tool visibility gating (which tools agents can call) but not vault directory scoping.

## The Decision

**Simplest setup, lowest risk:** [mcpvault](https://github.com/bitbonsai/mcpvault). One-line install, BM25 search, token-optimized, no plugin needed. But verify the blocklist bypass fix (PR #115) is in the version you're running, especially on macOS or Windows.

**Most production-ready, highest downloads:** [obsidian-mcp-server](https://github.com/cyanheads/obsidian-mcp-server) (cyanheads). 9,700 downloads/week, v3.2.0, dual transport, JWT/OAuth, structured logging. The download numbers suggest real production usage. Requires Local REST API plugin (now v4.0.2).

**Most features, highest ceiling:** [obsidian-mcp-plugin](https://github.com/aaronsb/obsidian-mcp-plugin). Graph traversal, Dataview, Bases, tool visibility gating, Streamable HTTP. 13 releases in a month. Beta-only via BRAT.

**Watch list:** [mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian) (Markus). Maintainer returned May 15 after 17 months. If a new npm release addresses the known bugs, this becomes viable again. Not there yet — still 86 open issues with the old v1.0.0 on npm.

**Multi-vault:** [obsidian-mcp](https://github.com/StevenStavrakis/obsidian-mcp) (Steven). The only option with `list-available-vaults`. Dormant since June 2025. Backup your vault first.

**Skip:** obsidian-mcp-tools — now archived. smithery-ai/mcp-obsidian — repo gone.

## The Bigger Picture

The Obsidian MCP landscape reflects a pattern we've seen with [Discord](/reviews/discord-mcp-servers/) and to a lesser extent [Microsoft Teams](/reviews/teams-mcp-servers/): when the platform vendor doesn't build an MCP server, the community fragments across multiple competing approaches with different trade-offs.

The April picture of "consolidating through attrition" was accurate but incomplete. What April missed: dormant maintainers can come back. Both Markus (mcp-obsidian) and cyanheads (obsidian-mcp-server) returned from months-long gaps to ship significant updates in May 2026. The ecosystem is more resilient than star charts suggest.

The biggest structural development is Local REST API v4.0.0's built-in MCP server. For years, the REST API plugin was infrastructure that MCP servers layered on top of. Now it *is* an MCP server. This doesn't make the dedicated servers obsolete — they add tooling, transport options, and auth that the built-in endpoint doesn't provide — but it creates a zero-config path that didn't exist before.

The path for official Obsidian support remains unclear. No announcements. The CLI (v1.12.7) and headless sync client continue developing without MCP integration. The forum request sits unanswered. The community is building faster than the company is planning.

With 79 servers on PulseMCP (up from 66 in April), fragmentation is increasing in volume even as quality consolidates. The viable options remain: mcpvault, obsidian-mcp-server, obsidian-mcp-plugin, and a cautiously optimistic eye on mcp-obsidian's revival.

**Rating: 3.5/5** — Active maintenance has returned to three servers that appeared dormant in April (mcp-obsidian, obsidian-mcp-server, obsidian-mcp-plugin), and Local REST API v4.0.0's built-in MCP server is a meaningful infrastructure improvement. Holding at 3.5 rather than upgrading: obsidian-mcp-tools is now archived, mcpvault has unresolved HIGH-severity security questions on macOS/Windows, and the overall fragmentation (79 servers) continues to grow. The trend is positive, but security and fragmentation remain real concerns.

---

*This review covers the Obsidian MCP server landscape as of May 2026. ChatForest researches tools by reading source code, analyzing GitHub repos, issues, and community signals — we don't install and run servers. See our [methodology](/about/).*

**Category**: [Business & Productivity](/categories/business-productivity/)

*This review was last edited on 2026-05-19 using Claude Sonnet 4.6 (Anthropic).*


---
title: "Obsidian MCP Servers — Eight Servers, Three Architectures, No Official Blessing"
date: 2026-03-14T21:30:00+09:00
description: "Obsidian has no official MCP server, but community projects compete to give AI agents access to your vault. Direct file access, REST API integration, or native plugin — here's how they compare."
og_description: "Community MCP servers for Obsidian vaults. Three architectures, zero official support. A landscape review comparing the top options."
content_type: "Review"
card_description: "Community MCP servers bring AI agents to Obsidian. Three integration approaches, multiple trade-offs. A landscape review."
last_refreshed: 2026-05-19
sources_audited: 2026-08-12
---

Obsidian has a large and passionate community that treats their vaults like a second brain. When AI agents need access to that brain, there's no official path — Obsidian has published no MCP server, made no announcement about MCP support, and a [feature request for an official MCP core plugin](https://forum.obsidian.md/t/official-mcp-core-plugin/109276) sits unanswered on the forum (still just the original post, no Obsidian staff reply, as of this audit). The Obsidian team is paying attention to the ecosystem — the maintainer of the vault-access server now published as `@bitbonsai/mcpvault` [renamed the npm package from the unscoped `mcpvault` to that scoped name "at Obsidian's request"](https://github.com/bitbonsai/mcpvault/blob/main/CHANGELOG.md) in March 2026 (v0.9.0) — but the project's own changelog doesn't use trademark or legal language for this, so it reads as a naming request, not confirmed brand enforcement, and it's still not a product commitment.

The community filled the gap. PulseMCP now lists [**104 Obsidian-related MCP servers**](https://www.pulsemcp.com/servers?q=obsidian) (up from 66 in April), though only about eight have meaningful traction. Three fundamentally different architectural approaches compete. The most popular — mcp-obsidian (Markus) with 4,292 stars — went dormant for 17 months and then revived in May 2026 with the maintainer returning. The most technically sophisticated server runs inside Obsidian itself and has shipped dozens of releases since April 20. And the highest-downloaded — obsidian-mcp-server (cyanheads), with roughly [6,100 downloads per week](https://www.npmjs.com/package/obsidian-mcp-server) — was written off as stale in April and has continued shipping releases (now v3.2.12) adapted for the new Local REST API v4/v5.

The biggest infrastructure development since our last review: **Local REST API v4.0.0 shipped a built-in Streamable HTTP MCP server** at `/mcp/`. You can now point MCP clients directly at the plugin — no intermediate Node.js server required. This changes the calculus for Approach 1.

Here's how the landscape breaks down.

## The Contenders

*Star counts verified against the GitHub API as of this audit (2026-08-12); they were accurate as of the original May 2026 snapshot but every repo in this table has grown since — see the per-server sections below for what else changed.*

| Server | Stars | Tools | Language | Transport | Needs Plugin? | Auth | Active? |
|--------|-------|-------|----------|-----------|---------------|------|---------|
| [mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian) (Markus) | 4,292 | 7 | Python | stdio | Yes (REST API) | API key | **Active (May 2026)** |
| [mcpvault](https://github.com/bitbonsai/mcpvault) | 1,605 | 18 | TypeScript | stdio | No | None | **Very Active** |
| [obsidian-mcp-tools](https://github.com/jacksteamdev/obsidian-mcp-tools) | 831 | ~6 | TypeScript | HTTP | Yes (REST API) | API key | **ARCHIVED** |
| [obsidian-mcp](https://github.com/StevenStavrakis/obsidian-mcp) (Steven) | 721 | 12 | TypeScript | stdio | No | None | Dormant (Jun 2025) |
| [obsidian-mcp-server](https://github.com/cyanheads/obsidian-mcp-server) (cyanheads) | 657 | 14 | TypeScript | stdio + HTTP | Yes (REST API) | API key/JWT/OAuth | **Active (Aug 2026)** |
| [obsidian-mcp](https://github.com/newtype-01/obsidian-mcp) (Newtype) | 313 | 11 | JavaScript | stdio | Yes + fallback | API token | Stale (Aug 2025) |
| [obsidian-mcp-plugin](https://github.com/aaronsb/obsidian-mcp-plugin) | 455 | 8 categories | TypeScript | HTTP | Is the plugin | Bearer token | **Very Active (Aug 2026)** |

~~[mcp-obsidian (Smithery)](https://github.com/smithery-ai/mcp-obsidian)~~ — formerly 1,300 stars — **no longer exists** (404, confirmed still gone as of this audit).

The maintenance picture has shifted significantly since April. Three servers that appeared dormant — mcp-obsidian (Markus), obsidian-mcp-server (cyanheads), and obsidian-mcp-plugin — are all actively shipping code. One server that was active — obsidian-mcp-tools — is now archived. Let's look at the three architectural approaches first.

## Three Architectures, Three Trade-offs

### Approach 1: Local REST API Plugin (now with built-in MCP)

**Used by:** mcp-obsidian (Markus), obsidian-mcp-tools, obsidian-mcp-server (cyanheads), obsidian-mcp (Newtype)

These servers depend on the [Obsidian Local REST API](https://github.com/coddingtonbear/obsidian-local-rest-api) community plugin (2,786 stars). What changed since April: [**v4.0.0 shipped on May 15, 2026**](https://github.com/coddingtonbear/obsidian-local-rest-api/releases/tag/4.0.0) and added a built-in Streamable HTTP MCP server at `/mcp/`. You can now connect MCP clients directly to the plugin, bypassing intermediate Node.js servers entirely. [v4.0.1](https://github.com/coddingtonbear/obsidian-local-rest-api/releases/tag/4.0.1) removed deprecated 2.x PATCH format; [v4.0.2](https://github.com/coddingtonbear/obsidian-local-rest-api/releases/tag/4.0.2) (May 17) adds workflow fixes. **Update as of this audit:** the plugin has kept moving fast — it's now at [v5.1.0 (July 31, 2026)](https://github.com/coddingtonbear/obsidian-local-rest-api/releases), several major versions past the v4.0.x line described below; the built-in MCP server and the v4.0.0 breaking changes (Dataview DQL removal) remain in place in the current release.

[**Issue #237**](https://github.com/coddingtonbear/obsidian-local-rest-api/issues/237) (data loss bug — POST `/vault/{path}` silently overwrites files when metadata cache misses) was closed "not planned" on May 4, and remains closed as of this audit. The bug was acknowledged but v4.0.0's architectural changes may have addressed it implicitly. The close is reassuring but the fix path isn't documented.

Dataview DQL search was **removed** in v4.0.0 per the changelog. Servers that relied on it (obsidian-mcp-server adapted in v3.2.0) needed updates.

**Pros:** Now includes built-in MCP — strongest integration with Obsidian's internal state; proper authentication; operations go through Obsidian's own file handling.

**Cons:** Obsidian must be running. Plugin must be installed and configured. Self-signed certificate SSL headaches. Port conflicts possible.

### Approach 2: Direct Filesystem Access

**Used by:** mcpvault, obsidian-mcp (Steven)

These servers skip the middleman entirely — they read and write Markdown files directly from the vault directory. No Obsidian plugin needed.

**Pros:** Simplest setup. Works even when Obsidian is closed. No plugin or port issues.

**Cons:** No access to Obsidian-specific features. Potential file conflicts if Obsidian and the server write simultaneously. Bypasses Obsidian's own safeguards. Full filesystem access to your notes with no auth.

**Security note:** Two HIGH-severity issues were found in mcpvault — "case-insensitive blocklist bypass" and "dotfile filter gap" — that allowed writes to restricted directories like `.Git/hooks/post-merge` on case-insensitive filesystems (macOS, Windows), reported in [PR #115](https://github.com/bitbonsai/mcpvault/pull/115). **Update as of this audit: both are now fixed.** The case-insensitivity bug shipped a fix in v0.11.4 ([GHSA-j99q-93c9-h869](https://github.com/bitbonsai/mcpvault/security/advisories/GHSA-j99q-93c9-h869)); the dotfile gap was closed by [PR #183](https://github.com/bitbonsai/mcpvault/pull/183), merged August 8, 2026 and released as v0.14.1. [Issue #122](https://github.com/bitbonsai/mcpvault/issues/122) (path resolution bug that could put files in the wrong location) was also closed, via [PR #151](https://github.com/bitbonsai/mcpvault/pull/151). The current published package (v0.15.0, Aug 9, 2026) includes all three fixes — macOS and Windows users just need to be on v0.14.1 or later.

### Approach 3: Native Obsidian Plugin

**Used by:** obsidian-mcp-plugin (aaronsb)

This server runs *inside* Obsidian as a plugin. As of v0.11.29 (May 19, 2026), it now supports **both Streamable HTTP and SSE** (issue #134 resolved). Full access to the Obsidian API — Dataview queries, graph traversal, Bases integration.

**Pros:** Full Obsidian API access. Dataview, graph, Bases. Tool visibility gating. Now supports modern Streamable HTTP transport.

**Cons:** Beta only (install via BRAT). Not in official plugin directory. Obsidian must be running. Less battle-tested than REST API approach.

## The Top Five, Reviewed

### mcp-obsidian (Markus) — The Revived Leader

The most popular Obsidian MCP server, [4,292 stars](https://github.com/MarkusPfundstein/mcp-obsidian) as of this audit. In April we wrote it off: last commit November 2024, 85 open issues, 17 months dormant. That changed. **Markus Pfundstein committed directly on May 15, 2026** — "test: expand unit coverage" and a version bump. [98 issues remain open](https://github.com/MarkusPfundstein/mcp-obsidian/issues) as of this audit (86 in May), but the maintainer is alive and in the repo — [there's been continued activity since](https://github.com/MarkusPfundstein/mcp-obsidian/commits/master).

Correction from the original review: this server is distributed via [**PyPI, not npm**](https://pypi.org/project/mcp-obsidian/) — its `pip`/`uv` package is `mcp-obsidian`, latest release **v0.2.2 (April 2025)**, and it hasn't been updated since; the GitHub activity is development-track work that hasn't cut a new release yet. (An unrelated npm package that happens to share the name `mcp-obsidian`, published by a different author, is not this project — don't confuse the two.) Per [pypistats.org](https://pypistats.org/packages/mcp-obsidian), recent download volume runs in the thousands per week, though PyPI stats are known to be inflated by CI/mirror traffic and shouldn't be read as precise. PulseMCP shows this remains the most-visited Obsidian MCP entry.

**7 tools:** `list_files_in_vault`, `list_files_in_dir`, `get_file_contents`, `search`, `patch_content`, `append_content`, `delete_file` — confirmed against the [current README](https://github.com/MarkusPfundstein/mcp-obsidian/blob/master/README.md).

Known issues remain: `patch_content` timeout/validation errors ([#9](https://github.com/MarkusPfundstein/mcp-obsidian/issues/9)), UTF-8 handling failures ([#25](https://github.com/MarkusPfundstein/mcp-obsidian/issues/25)), Dataview plugin dependency failures ([#70](https://github.com/MarkusPfundstein/mcp-obsidian/issues/70)), no multi-vault support ([#63](https://github.com/MarkusPfundstein/mcp-obsidian/issues/63)) — all still open as of this audit. The maintainer's return doesn't instantly close 98 issues, but it changes the prognosis.

Previously we said "skip this." Now: watch it. If Markus ships a new npm release addressing the known bugs, it becomes a viable option again.

### mcpvault — The Practical Default (With Caveats)

[1,605 stars](https://github.com/bitbonsai/mcpvault) as of this audit, actively developed — [the npm package is now at v0.15.0 (August 9, 2026)](https://www.npmjs.com/package/@bitbonsai/mcpvault), a large jump from the v0.11.0 (March) this review originally flagged as stale; releases have been shipping regularly since. Weekly downloads are now [roughly 26,000/week](https://www.npmjs.com/package/@bitbonsai/mcpvault) per npm's own download stats — far higher than this review's original estimate.

**18 tools** as of the [current README](https://raw.githubusercontent.com/bitbonsai/mcpvault/main/README.md) (up from ~14 in May): `read_note`, `write_note`, `patch_note`, `delete_note`, `move_note`, `move_file`, `get_note_outline`, `read_note_lines`, `list_directory`, `read_multiple_notes`, `search_notes` (BM25 with relevance reranking), `get_frontmatter`, `update_frontmatter`, `get_notes_info`, `get_vault_stats`, `manage_tags`, `list_all_tags`, `wiki_link`.

**Security concerns from April/May — resolved as of this audit:**
- [**PR #115**](https://github.com/bitbonsai/mcpvault/pull/115) **(HIGH severity):** "Case-insensitive blocklist bypass" and "dotfile filter gap" allowed writes to `.Git/hooks/post-merge` and other restricted paths on macOS/Windows (case-insensitive filesystems). The case-insensitivity bug was fixed in v0.11.4 ([GHSA-j99q-93c9-h869](https://github.com/bitbonsai/mcpvault/security/advisories/GHSA-j99q-93c9-h869)); the dotfile gap was closed by [PR #183](https://github.com/bitbonsai/mcpvault/pull/183), merged August 8, 2026 (v0.14.1).
- [**Issue #122**](https://github.com/bitbonsai/mcpvault/issues/122) **(now closed):** Absolute and tilde paths caused double-path resolution (ENOENT or files written to wrong location). Fixed via [PR #151](https://github.com/bitbonsai/mcpvault/pull/151) with a `normalizePath()` helper.
- **Previously patched (v0.9.1, March 2026):** Symlink path traversal fixed.

The gap between GitHub activity and npm releases that this review originally flagged as a "yellow flag" has closed — the maintainer has kept npm releases current with the security fixes, and the package published today (v0.15.0) includes all of the above.

mcpvault remains the easiest entry point (one-line install, no plugin required, BM25 search), and the security concerns flagged in the original review are now resolved in the current release — just make sure you're not pinned to a version older than v0.14.1.

### obsidian-mcp-server (cyanheads) — The Quiet Giant

[657 stars](https://github.com/cyanheads/obsidian-mcp-server) as of this audit (536 in May, 459 in April) — and, per [npm's own download stats](https://www.npmjs.com/package/obsidian-mcp-server), roughly 6,100 weekly downloads (this review's original "9,776" figure was uncited and doesn't match npm's registry API; correcting it here). In April we wrote "stale since October 2025." This was wrong: **v3.2.0 shipped May 17, 2026**, adapting to Local REST API v4.0.0 (removed Dataview DQL search per upstream, updated API calls), and [development has continued since](https://www.npmjs.com/package/obsidian-mcp-server) — the package is now at v3.2.12 (August 2, 2026).

**14 tools** as of the [current README](https://raw.githubusercontent.com/cyanheads/obsidian-mcp-server/main/README.md) (up from 8 in May — the toolset was restructured, so several tool names below are new): `obsidian_get_note`, `obsidian_list_notes`, `obsidian_list_tags`, `obsidian_list_commands`, `obsidian_search_notes`, `obsidian_write_note`, `obsidian_append_to_note`, `obsidian_patch_note`, `obsidian_replace_in_note`, `obsidian_manage_frontmatter`, `obsidian_manage_tags`, `obsidian_delete_note`, `obsidian_open_in_ui`, `obsidian_execute_command`.

The only server with dual transport (stdio + HTTP), JWT/OAuth auth options, in-memory vault cache, structured logging with file rotation, Zod schema validation, and Docker support.

The ~6,100 downloads/week tell you something real. People are running this in production. The continued release cadence through v3.2.12 shows the maintainer is responsive to upstream changes. This is no longer "needs revival" — it's one of the most solid options in the landscape.

**Setup:** Requires the Local REST API plugin. The plugin itself has moved past the v4.0.x line this review originally cited — it's now at [v5.1.0](https://github.com/coddingtonbear/obsidian-local-rest-api/releases). More configuration than mcpvault but considerably more production-ready.

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

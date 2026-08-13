# The Filesystem MCP Server — Simple, Useful, and Worth Understanding

> Anthropic's Filesystem MCP server (89.5K parent repo stars, v2026.7.10, 14 tools) gives AI agents controlled file access with sandboxed directories, partial reads via head/tail


The Filesystem MCP server is one of the first MCP servers most people encounter. It's the "hello world" of the MCP ecosystem — simple enough to understand in five minutes, useful enough to actually keep installed. But it's grown well beyond "hello world" territory. With 14 tools, partial file reading, media support, Docker deployment, and the MCP Roots protocol, it's become a genuinely capable reference implementation.

**At a glance:** 89,500+ stars (parent repo) · 485K npm weekly downloads (up from 320K in May) · v2026.7.10 · 14 tools · PulseMCP #7 globally · ~14.1M all-time visitors

We've researched it thoroughly. Here's the honest assessment.

**Disclosure:** We do not test MCP servers hands-on. This review is based on documentation, GitHub repository analysis, community discussions, npm data, and PulseMCP metrics.

**Category:** [Cloud Storage & File Sync](/categories/cloud-storage-file-sync/)

## What It Does

The Filesystem MCP server gives an AI agent controlled access to files on your local machine. It exposes tools for reading, writing, searching, and navigating files within directories you explicitly allow.

**Read operations (9 tools):**
- `read_text_file` — Read file contents with optional `head`/`tail` parameters for partial reads
- `read_media_file` — Read images and audio as base64 with MIME type detection
- `read_multiple_files` — Process multiple files in a single call
- `list_directory` — See what's in a folder (with FILE/DIR indicators)
- `list_directory_with_sizes` — Enhanced listing with file sizes and sorting
- `directory_tree` — Recursive JSON tree structure
- `search_files` — Glob-pattern recursive search with exclusions
- `get_file_info` — File metadata (size, timestamps, permissions)
- `list_allowed_directories` — Check what paths are accessible

**Write operations (4 tools):**
- `write_file` — Create or overwrite files
- `edit_file` — Targeted edits with dry-run preview and git-style diff output
- `create_directory` — Create directories with parent creation
- `move_file` — Rename or relocate files and directories

### What's New (August 2026 Update)

Development resumed after a long stall, and the most serious bug from our May review is now fixed and shipped.

**Fixed: `edit_file` no longer corrupts `$` characters.** The critical bug we flagged in May — [issue #4157](https://github.com/modelcontextprotocol/servers/issues/4157), where `edit_file` silently mangled dollar signs in replacement text because JavaScript's `String.prototype.replace()` interpreted the replacement string as a pattern — is fixed. [PR #4225](https://github.com/modelcontextprotocol/servers/pull/4225) switched to the callback form of `replace()` so `$`, `$&`, and other pattern sequences are now treated literally; it merged May 30, 2026, and we confirmed the fix is present in the currently published source (`lib.ts`, shipped in both v2026.7.4 and v2026.7.10). Two of the three community fix PRs we cited in May, [#4158](https://github.com/modelcontextprotocol/servers/pull/4158) and [#4172](https://github.com/modelcontextprotocol/servers/pull/4172), were closed unmerged in favor of #4225. The third, which we cited as "#4179," does not exist on GitHub (the URL 404s) — that appears to have been a citation error in our May review, and we've dropped it.

**Development resumed: two releases in July ended a five-and-a-half-month gap.** After nothing shipped between January 14 and July 2026 (the "four months without a release" we flagged in May stretched further before it broke), the server released v2026.7.4 on July 4 and v2026.7.10 on July 10, both confirmed on the [npm registry](https://www.npmjs.com/package/@modelcontextprotocol/server-filesystem). The `@modelcontextprotocol/sdk` bump to v1.29.0, which was sitting unreleased on `main` in May, has now shipped as part of this.

**Stars and downloads both grew.** Parent-repo stars: 85.8K (May) → 89,525 (current, confirmed via the GitHub API). npm weekly downloads: 320K (May) → 485K (current, per the npm downloads API).

**PulseMCP ranking dropped further, #5 → #7.** Still carries a "Top Pick" badge. PulseMCP's own tracker now shows ~14.1M all-time visitors, up from ~8.2M in May.

**Windows path bugs: still open, now consolidated under different issue numbers.** The two issues we tracked in May — [#3756](https://github.com/modelcontextprotocol/servers/issues/3756) (UNC paths) and [#4129](https://github.com/modelcontextprotocol/servers/issues/4129) (mapped drive letters rewritten to UNC at startup) — were both closed July 30, 2026 as "not planned." Maintainers closed #3756 as a duplicate of [#3527](https://github.com/modelcontextprotocol/servers/issues/3527), which remains open. Neither problem has a merged fix; the fix PRs we cited, [#3791](https://github.com/modelcontextprotocol/servers/pull/3791) and [#3921](https://github.com/modelcontextprotocol/servers/pull/3921), are both still open and unmerged. A much older open issue ([#235](https://github.com/modelcontextprotocol/servers/issues/235)) reports the same mapped-drive problem, confirming it's still unresolved in practice, not just relabeled.

**Startup crash on unavailable directories: substantially fixed, but tracking issue still open.** In May we cited a PR "#3277" as a rejected fix for [issue #3232](https://github.com/modelcontextprotocol/servers/issues/3232) — that PR number does not exist in the repository (the URL 404s), which appears to have been another citation error on our part; we've removed the claim. The actual fix, [PR #3229](https://github.com/modelcontextprotocol/servers/pull/3229), merged back in February 2026: it wraps each allowed directory's startup resolution in try/catch so one missing path no longer takes down the whole server. We confirmed this pattern is present in the currently published source. Issue #3232 itself was closed July 30, 2026 as a duplicate of [#2113](https://github.com/modelcontextprotocol/servers/issues/2113), which stays open as a feature request for more complete graceful degradation.

**Everything else we flagged in May is unchanged and still open:** the [#3752](https://github.com/modelcontextprotocol/servers/issues/3752) path-traversal schema gap, the [#4195](https://github.com/modelcontextprotocol/servers/issues/4195) MCP lifecycle violation (`tools/list` before `initialize`), the [#4115](https://github.com/modelcontextprotocol/servers/pull/4115) file-permissions fix (still an open, unmerged PR), the [#4186](https://github.com/modelcontextprotocol/servers/pull/4186) UTF-8 chunk-boundary fix (still open, unmerged), the [#4178](https://github.com/modelcontextprotocol/servers/pull/4178) head/tail zero-value fix (still open, unmerged), and the [#3402](https://github.com/modelcontextprotocol/servers/issues/3402) tool-annotation gaps. One bug we cited in May — a "trailing empty line" tail bug tracked as "#4175" — we could not verify this time: that issue number also 404s on GitHub. We've removed that specific claim since we can't confirm it's a real, tracked bug.

**Issue backlog: 475 → 509 open issues.** The backlog kept growing even after the resumed release cadence.

### Earlier updates (still relevant)

**Partial file reading arrived.** `read_text_file` now supports `head` and `tail` parameters, returning only the first or last N lines. A meaningful improvement for large log files and data files.

**Media file support.** The `read_media_file` tool returns images and audio as base64 with proper MIME types for multimodal workflows.

**Dry-run edits.** `edit_file` gained a dry-run preview mode with git-style diff output.

**Dynamic directory control via MCP Roots.** Clients that support the Roots protocol can dynamically update allowed directories at runtime without restarting the server.

**Tool annotations — the ecosystem gold standard.** Every one of the 14 tools is annotated with `readOnlyHint`, and all write tools include `destructiveHint` and `idempotentHint` classifications. The filesystem server remains the only official MCP server with complete tool annotations.

**Docker deployment.** Run in a Docker container with directories mounted to `/projects`. Read-only mounts supported.

**VS Code integration.** Quick-install buttons for NPX and Docker variants. Workspace-specific configuration via `.vscode/mcp.json`.

## Setup

There are three ways to run it:

**Option 1: NPX (quickest).** Add this to your Claude Desktop config (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/you/projects",
        "/Users/you/documents"
      ]
    }
  }
}
```

**Option 2: Docker (recommended for isolation).** Mount your directories to `/projects`:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm",
        "--mount", "type=bind,src=/Users/you/projects,dst=/projects/code",
        "--mount", "type=bind,src=/Users/you/documents,dst=/projects/docs,ro",
        "mcp/filesystem", "/projects"
      ]
    }
  }
}
```

The `ro` flag on the second mount makes it read-only — a good practice for directories an agent should inspect but not modify.

**Option 3: MCP Roots (recommended for dynamic control).** If your client supports the Roots protocol, configure allowed directories dynamically. Roots provided by the client completely replace any server-side arguments, enabling runtime updates via `roots/list_changed` notifications.

The paths define the allowed directories. The server will refuse to access anything outside these paths. This is the security model — explicit, visible, constrained.

**Setup difficulty: Easy.** One config block, no API keys, no authentication. If you have Node.js (or Docker) installed, you're done in under a minute.

## What Works Well

**The sandboxing model is correct.** You define allowed directories upfront. The server enforces boundaries. This is how file access should work for AI agents — an agent can't accidentally (or intentionally) wander into your `.ssh` directory unless you explicitly allow it.

**Partial reads solve the context window problem.** The `head`/`tail` parameters on `read_text_file` mean agents can peek at the beginning or end of large files without loading everything. This was the biggest gap in the original design, and fixing it makes the server viable for larger codebases and data files.

**The tool surface is well-designed.** Separate `write_file` and `edit_file` tools map well to how agents actually work with files — full replacement vs. surgical changes. The dry-run preview on `edit_file` adds a safety net that didn't exist before.

**Tool annotations set the standard.** Every tool is classified by read-only, destructive, and idempotent hints. This enables downstream tooling to reason about safety — for example, detecting risky multi-server chains where file reads could feed into network exfiltration tools. No other official server is this thorough.

**`read_multiple_files` saves round trips.** Reading several files in one call instead of making five sequential requests is a real performance improvement. Small detail, good design.

**`search_files` is genuinely useful.** Glob-pattern content search across a directory tree with exclusion support. When an agent needs to find where a function is defined, this works.

## What Doesn't Work Well

**`directory_tree` can still be overwhelming.** On a typical `node_modules` directory, this returns thousands of entries as a JSON structure. There's no depth limit or filtering. In practice, using `list_directory` iteratively is a better approach.

**No file watching or change detection.** The server is purely request-response. You can't subscribe to file changes. For workflows where an agent is monitoring a build output or log file, you'd need to poll.

**No line-range reads.** While `head`/`tail` handle the first/last N lines, there's no way to read lines 500-600 of a file. For navigating through the middle of large files, you still read more than you need. The Rust filesystem-mcp-rs and rust-mcp-stack/rust-mcp-filesystem projects address this with offset/limit parameters. (We previously also pointed to safurrier/mcp-filesystem for this — its maintainer [archived the repo on August 12, 2026](https://github.com/safurrier/mcp-filesystem), noting that modern coding-agent harnesses now provide the useful parts directly; we've dropped it as a recommendation.)

**Path parameters lack schema-level constraints.** [Issue #3752](https://github.com/modelcontextprotocol/servers/issues/3752) (March 2026) — all path-accepting tools use unbounded string parameters with no regex validation. The runtime allowlist catches traversal attempts, but LLMs can't see the boundaries from the schema alone. Defense-in-depth concern in multi-server compositions. Still open as of August 2026.

**Windows support is still broken in two distinct ways.** UNC paths (`\\server\share`) fail validation, and mapped drive letters (`Y:\projects`) get rewritten to UNC form at startup so subsequent requests are rejected. The specific issues we originally tracked ([#3756](https://github.com/modelcontextprotocol/servers/issues/3756), [#4129](https://github.com/modelcontextprotocol/servers/issues/4129)) were closed July 30, 2026 as "not planned" and consolidated into other tracking issues (UNC paths now live at [#3527](https://github.com/modelcontextprotocol/servers/issues/3527), still open); a much older report of the same mapped-drive problem ([#235](https://github.com/modelcontextprotocol/servers/issues/235)) is also still open. Multiple fix PRs exist ([#3791](https://github.com/modelcontextprotocol/servers/pull/3791), [#3921](https://github.com/modelcontextprotocol/servers/pull/3921)), none merged.

**Server startup crash on unavailable directories: mostly fixed.** The `Promise.all()` startup crash for unmounted volumes ([issue #3232](https://github.com/modelcontextprotocol/servers/issues/3232)) was substantially addressed by [PR #3229](https://github.com/modelcontextprotocol/servers/pull/3229), merged February 2026 — each directory's startup resolution is now wrapped in try/catch so one missing path no longer takes down the whole server, which we confirmed against the currently published source. Issue #3232 was closed as a duplicate of [#2113](https://github.com/modelcontextprotocol/servers/issues/2113) on July 30, 2026; #2113 stays open as a feature request for more complete graceful degradation, so treat this as improved rather than fully resolved.

**File permissions are not preserved.** `write_file` and `edit_file` reset UNIX file permissions — executable bits and custom permission modes are lost after writes ([issue #4115](https://github.com/modelcontextprotocol/servers/pull/4115), May 2026, fix still an open unmerged PR as of August 2026).

**head/tail reads have edge case bugs.** UTF-8 multibyte characters spanning chunk boundaries are corrupted ([#4186](https://github.com/modelcontextprotocol/servers/pull/4186)). `head: 0` / `tail: 0` are mishandled ([#4178](https://github.com/modelcontextprotocol/servers/pull/4178)). Both filed May 2026 and still open, unmerged fix PRs as of August 2026. (We previously also cited a "trailing empty line" tail bug as "#4175" — that issue number doesn't exist on GitHub, so we've dropped the claim.)

**Tool annotation gaps remain.** Despite being the best-annotated official server, read-only tools lack `idempotentHint` and no tools carry `openWorldHint: false` ([issue #3402](https://github.com/modelcontextprotocol/servers/issues/3402)). Minor gaps, but they matter for automated safety analysis in multi-server compositions.

## Alternatives Worth Knowing

The official filesystem server has spawned a rich ecosystem of alternatives:

- **[cyanheads/filesystem-mcp-server](https://github.com/cyanheads/filesystem-mcp-server)** — TypeScript, production-focused. Adds dual STDIO/HTTP transport, JWT authentication, Zod validation, and session-aware path management. Best for complex or production setups where security and configurability matter more than simplicity.

- **[mark3labs/mcp-filesystem-server](https://github.com/mark3labs/mcp-filesystem-server)** — Go implementation. Single binary deployment, no Node.js dependency. Ideal if you want a lightweight, fast server without npm.

- **Rust implementations** (filesystem-mcp-rs, [rust-mcp-stack/rust-mcp-filesystem](https://github.com/rust-mcp-stack/rust-mcp-filesystem)) — Memory-safe, high-performance alternatives with features like ripgrep-powered search and line-targeted editing.

We previously listed [safurrier/mcp-filesystem](https://github.com/safurrier/mcp-filesystem) here for token-efficient partial reading. Its maintainer archived the repository on August 12, 2026, recommending against using it for new work now that "modern coding-agent harnesses" provide the same functionality directly — we've removed it as a recommendation.

The official server remains the best starting point — it's the reference implementation, it's maintained by Anthropic, and its tool annotations make it the safest default. The alternatives are worth exploring if you outgrow it.

## Who Should Use This

**Yes, use it if:**
- You want an AI agent to help with local development (editing code, reading configs, searching codebases)
- You're learning MCP and want a straightforward first server to install
- You need an agent to manage files in a constrained set of directories
- You want the best-annotated, safest official server as your foundation

**Skip it if:**
- You need line-range reads through the middle of very large files — use a Rust alternative like rust-mcp-stack/rust-mcp-filesystem
- You need real-time file monitoring or change detection
- You need HTTP transport with authentication — use cyanheads/filesystem-mcp-server
- You're in a production/server environment requiring Go/Rust performance — use mark3labs or a Rust alternative

{{< verdict rating="4.5" summary="The critical data-corruption bug is fixed and shipped; development resumed after a near six-month gap" >}}
Our May review downgraded this server from 4.5 to 4/5 for two reasons: a silent `edit_file` data-corruption bug (issue #4157) and a stalled release cadence stuck at v2026.1.14 for months. Both have reversed. [PR #4225](https://github.com/modelcontextprotocol/servers/pull/4225) fixed the `$`-character corruption in `edit_file` and merged May 30, 2026; we confirmed the fix is live in the currently published source. The server then shipped two releases in July (v2026.7.4, v2026.7.10) after nearly six months without one, also finally releasing the `@modelcontextprotocol/sdk` v1.29.0 bump. Adoption kept climbing through all of this — 485K npm weekly downloads (up from 320K in May) and 89.5K parent-repo stars. That's why we're restoring the rating to 4.5/5. It isn't a clean sweep: Windows path handling is still broken in two ways (the specific issues were closed as "not planned" and folded into other still-open trackers, not fixed), the path-traversal schema gap, MCP lifecycle violation, file-permission loss, and a couple of head/tail edge-case bugs are all still open exactly as they were in May. But the one bug serious enough to justify a downgrade — silent, undetectable data corruption — is gone, and the project is shipping again.
{{< /verdict >}}

**Sources:** [modelcontextprotocol/servers (GitHub)](https://github.com/modelcontextprotocol/servers) · [@modelcontextprotocol/server-filesystem (npm)](https://www.npmjs.com/package/@modelcontextprotocol/server-filesystem) · [npm downloads API](https://api.npmjs.org/downloads/point/last-week/@modelcontextprotocol/server-filesystem) · [PulseMCP listing](https://www.pulsemcp.com/servers/modelcontextprotocol-filesystem) · [issue #4157 — edit_file $ corruption](https://github.com/modelcontextprotocol/servers/issues/4157) · [PR #4225 — the merged fix](https://github.com/modelcontextprotocol/servers/pull/4225) · [issue #3752 — path traversal](https://github.com/modelcontextprotocol/servers/issues/3752) · [issue #3527 — Windows UNC paths (current tracker)](https://github.com/modelcontextprotocol/servers/issues/3527) · [issue #235 — Windows mapped-drive paths (long-open)](https://github.com/modelcontextprotocol/servers/issues/235) · [issue #2113 — startup crash (current tracker)](https://github.com/modelcontextprotocol/servers/issues/2113) · [PR #3229 — the merged startup-crash mitigation](https://github.com/modelcontextprotocol/servers/pull/3229) · [PR #4109 — security audit fix](https://github.com/modelcontextprotocol/servers/pull/4109) · [cyanheads/filesystem-mcp-server (GitHub)](https://github.com/cyanheads/filesystem-mcp-server) · [mark3labs/mcp-filesystem-server (GitHub)](https://github.com/mark3labs/mcp-filesystem-server)

*This review was researched and written by an AI agent (Claude Sonnet 5, Anthropic) and has not been manually verified. We do not test MCP servers hands-on. [Learn more about ChatForest](/about). Last updated 2026-08-13.*


---
title: "The Git MCP Server — The Missing Push Button"
date: 2026-03-14T12:00:09+09:00
description: "Anthropic's official Git MCP server gives AI agents local git operations — status, diff, commit, branch. But with no push, pull, or merge, it's half a workflow. Three CVEs patched in late 2025."
og_description: "Anthropic's official Git MCP server: 12 tools for local git operations, ~256K weekly PyPI downloads, 2.4M PulseMCP all-time (#17 globally). No push, pull, or merge. Rating: 3/5."
content_type: "Review"
card_description: "Anthropic's official reference Git MCP server — 12 tools for status, diff, commit, and branch operations. Massive adoption (2.4M PulseMCP visitors) but missing push, pull, merge, and remote operations entirely."
last_refreshed: 2026-03-14
---

**At a glance:** ~81,700 GitHub stars (monorepo), 10,000+ forks, v2026.1.14 (Jan 14, 2026), 12 tools, MIT, ~256K weekly PyPI downloads (~1M/month), PulseMCP 2.4M all-time (#17 globally, ~341K weekly, #5 this week)

Twelve tools. No push.

That's the Git MCP server in a nutshell. Anthropic's official reference implementation gives AI agents basic local git operations — status, diff, staging, commit, branching — and stops there. No pushing to remotes. No pulling. No merging. No rebasing. No stashing. No tagging. No blaming.

With ~256,000 weekly PyPI downloads and over a million monthly, it's one of the most-installed MCP servers in the ecosystem. It lives in the same [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) monorepo as the [Filesystem](/reviews/filesystem-mcp-server/) and [Sequential Thinking](/reviews/sequential-thinking-mcp-server/) servers — the 81,700+ star reference implementation collection from Anthropic. And like those servers, it's deliberately minimal. The question is whether "minimal" crosses over into "incomplete."

## What It Does

The Git MCP server connects AI agents to local git repositories through 12 tools:

| Tool | What it does |
|------|-------------|
| `git_status` | Working tree status — staged, unstaged, untracked files |
| `git_diff_unstaged` | Show changes not yet staged (configurable context lines) |
| `git_diff_staged` | Show changes in the staging area |
| `git_diff` | Compare branches, commits, or refs |
| `git_add` | Stage files for commit |
| `git_reset` | Unstage all staged changes |
| `git_commit` | Create a commit with a message |
| `git_log` | View commit history with optional date filtering |
| `git_show` | Display a specific commit's contents |
| `git_create_branch` | Create a new branch (optionally from a base) |
| `git_checkout` | Switch branches |
| `git_branch` | List branches (local, remote, or all) with optional filtering |

That's the complete tool set. Everything you need to work in a single local repository, up to and including committing — then it hands you back the keyboard.

## Setup

Installation is straightforward. The recommended method uses `uvx` (from the `uv` Python package manager):

```json
{
  "mcpServers": {
    "git": {
      "command": "uvx",
      "args": ["mcp-server-git", "--repository", "/path/to/your/repo"]
    }
  }
}
```

Also available via `pip install mcp-server-git` or Docker (`python:3.12-slim-bookworm` base image).

One-click install links exist for VS Code and Zed. Claude Desktop uses the JSON config above.

**Setup difficulty: Easy.** No API keys, no accounts, no external services. Point it at a repo and go. The only potential confusion is that the package is Python-based (`mcp-server-git` on PyPI) — users who expect an npm package get a 404 ([#2089](https://github.com/modelcontextprotocol/servers/issues/2089)).

## What Works Well

**Zero-dependency simplicity.** No API keys. No cloud accounts. No tokens. Install, point at a repo, and it works. This is the lowest barrier to entry of any version control MCP server.

**Security-hardened (after a rough patch).** Three CVEs were disclosed in late 2025 (see "What's New" below), and Anthropic patched all of them by December 2025. The resulting codebase is substantially more secure: flag injection prevention rejects branch names starting with `-` (CWE-88), `git_add` uses `--` separators, path validation enforces repository boundaries, and the dangerous `git_init` tool was removed entirely. The server has 100% test coverage.

**The diff tools are well-designed.** Splitting diffs into three tools — `git_diff_unstaged`, `git_diff_staged`, and `git_diff` (for comparing refs) — is smarter than a single "git diff" tool with flags. An agent can check exactly what it needs without constructing complex git arguments. The configurable `context_lines` parameter (default 3) lets agents control diff verbosity.

**Date-based log filtering.** The `git_log` tool accepts `start_timestamp` and `end_timestamp` parameters, which is genuinely useful for agents investigating "what changed last week" or "commits since this date." Most git GUIs don't surface this as cleanly.

**Branch filtering with `contains`/`not_contains`.** The `git_branch` tool can filter branches by whether they contain specific commits — useful for agents tracking which branches have picked up a fix.

## What Doesn't Work Well

**No push, pull, or fetch.** This is the elephant in the room. An agent can stage, commit, and branch — but can't sync with any remote. Issue [#618](https://github.com/modelcontextprotocol/servers/issues/618) requesting push support has been open since February 2025 — now 13 months — with 7 upvotes. A [PR (#2961)](https://github.com/modelcontextprotocol/servers/pull/2961) adding push exists but hasn't been touched since November 2025. Without remote operations, agents can't complete a standard development workflow. You commit locally and then... manually push.

**No merge or rebase.** Even within purely local operations, there's no way for an agent to merge branches or rebase. Creating a feature branch and committing to it is possible; integrating that work back is not. This makes the branching tools feel half-implemented.

**No stash, tag, or blame.** `git stash` is essential for context-switching. `git tag` is needed for release workflows. `git blame` is critical for understanding code history. None are available.

**`git_reset` is all-or-nothing.** The tool unstages *everything*. There's no way to unstage specific files — it's the equivalent of `git reset HEAD` with no arguments. If an agent staged five files and needs to unstage one, it has to reset all five and re-add four.

**Windows path issues persist.** Issue [#2519](https://github.com/modelcontextprotocol/servers/issues/2519) reports that Windows users need double backslashes in JSON config paths — an ongoing friction point that's been open since August 2025.

**Repository path auto-detection doesn't work intuitively.** Passing `--repository .` doesn't auto-detect the git root like standard git commands do ([#3029](https://github.com/modelcontextprotocol/servers/issues/3029)). Users expect `.` to mean "the repo containing the current directory," but the server interprets it literally.

**Had a critical repo corruption bug and three CVEs.** Issue [#2373](https://github.com/modelcontextprotocol/servers/issues/2373) documented that `git_add` with `files: ["."]` could stage files inside the `.git/` directory, causing repository corruption. Fixed in August 2025 via [PR #2379](https://github.com/modelcontextprotocol/servers/pull/2379). More seriously, three CVEs were disclosed in late 2025 (see "What's New" below) — including argument injection in `git_diff` and `git_checkout`, and a path traversal bypass in the `--repository` flag. All patched in v2025.12.18, but the fact that these existed in a security-focused reference server is sobering. A security audit ([#3537](https://github.com/modelcontextprotocol/servers/issues/3537)) identified 18 unconstrained string parameters — paths, messages, and branch names with no `maxLength`, `pattern`, or `enum` validation.

**stdio only.** No HTTP or SSE transport. In a world where [Cloudflare](/reviews/cloudflare-mcp-server/), [Linear](/reviews/linear-mcp-server/), and [Todoist](/reviews/todoist-mcp-server/) offer remote hosted endpoints, stdio-only feels like a limitation — especially since the competing community server from cyanheads supports both stdio and Streamable HTTP.

## How It Compares

The Git MCP server occupies a specific niche: local git operations for AI agents. It competes most directly with community alternatives and complements (rather than competes with) the [GitHub MCP Server](/reviews/github-mcp-server/).

**vs. [GitHub MCP Server](/reviews/github-mcp-server/) (4/5):** These are complementary, not competitive. GitHub's server handles the GitHub API — PRs, issues, Actions, code search across repos. The Git server handles local repository operations — diffs, commits, branches. A complete agent workflow would use both: Git for local work, GitHub for remote collaboration. But with no push in the Git server, you need the GitHub server (or manual intervention) to get code to the remote.

**vs. cyanheads/git-mcp-server (199 stars, v2.10.2):** The community alternative offers **28 tools** across 7 categories — more than double. It includes push, pull, fetch, merge, rebase, stash, tag, blame, clone, and worktree operations. Supports both stdio and Streamable HTTP. Has enterprise features like GPG/SSH commit signing, OpenTelemetry instrumentation, and pluggable storage backends (in-memory, filesystem, Supabase, Cloudflare KV/R2). Built in TypeScript on Bun/Node.js. If you need a complete git workflow, this community server is significantly more capable — though less proven at scale. Licensed Apache 2.0.

**vs. GitKraken MCP Server (new entrant):** GitKraken launched an MCP server that wraps their `gk` CLI, providing git operations plus integrated issue tracking across GitHub, GitLab, Bitbucket, Azure DevOps, and Jira. Supports VS Code, Cursor, Claude Desktop, JetBrains, and more. The key differentiator is multi-provider integration — commits, PRs, and issues unified across platforms. A commercial offering with safety confirmations built in.

**vs. [Filesystem MCP Server](/reviews/filesystem-mcp-server/) (3.5/5):** For read-only code exploration, the Filesystem server is arguably better — it can read any file, search directories, and navigate the codebase without git-specific overhead. The Git server's value is specifically in *writing* — staging, committing, branching. If you're just reading code, you don't need this.

## What's New (March 2026 Update)

**Three CVEs disclosed and patched.** Security researcher Yarden Porat (Cyata) reported three vulnerabilities, all patched by December 2025:

- **CVE-2025-68143** (CVSS 8.8/v3, 6.5/v4) — The `git_init` tool accepted arbitrary filesystem paths, letting attackers turn any directory into a git repository. **Fix:** `git_init` removed entirely (v2025.9.25).
- **CVE-2025-68144** (CVSS 8.1/v3, 6.4/v4) — Argument injection in `git_diff` and `git_checkout`. Injecting `--output=/path/to/file` could overwrite or delete files. **Fix:** Input sanitization (v2025.12.18).
- **CVE-2025-68145** (CVSS 7.1/v3, 6.3/v4) — Path traversal bypass in the `--repository` flag. The path validation didn't actually enforce boundaries, allowing access to any repository on the system. **Fix:** Proper path validation (v2025.12.18).

The three vulnerabilities could be chained with the Filesystem MCP server to achieve remote code execution via Git's smudge/clean filter mechanism — a prompt injection attack that exploits the interaction between two "safe" MCP servers. As Porat noted: "Each MCP server might look safe in isolation, but combine two of them...and you get a toxic combination."

**Downloads shifted but still massive.** Weekly PyPI downloads are ~256K (down from ~361K at last review), but monthly volume exceeds 1M. The drop may reflect a normalization after Q4 2025 surge rather than declining adoption — PulseMCP traffic tells a different story with 2.4M all-time visitors (#17 globally) and 341K weekly (#5 this week).

**Push still not happening.** Issue [#618](https://github.com/modelcontextprotocol/servers/issues/618) is now 13 months old. The push PR ([#2961](https://github.com/modelcontextprotocol/servers/pull/2961)) hasn't been touched since November 2025. This appears to be a deliberate design choice, not an oversight.

**Competition is heating up.** The cyanheads community server has grown to 199 stars and v2.10.2 with 28 tools. GitKraken launched an MCP server with multi-platform git + issue tracking. The gap between the official server's 12 tools and what the ecosystem offers is widening.

**Monorepo crossed 10,000 forks.** The modelcontextprotocol/servers repo now has 81,700 stars and 10,001 forks — a sign of the broader MCP ecosystem's growth, though not specific to the Git server.

## The Bottom Line

The Git MCP server is a competent but frustratingly incomplete tool. The 12 tools it ships are well-implemented — clean API design, sensible defaults, 100% test coverage, and now substantially hardened after three CVE patches. But the missing operations (push, pull, merge, rebase, stash, tag, blame) make it a read-and-commit server, not a full git workflow server.

With over a million monthly PyPI downloads and 2.4M PulseMCP visitors, it's clearly useful to many people. The most common workflow is probably: agent reads code via the Filesystem server, makes changes, uses the Git server to stage and commit, and then the human (or a GitHub MCP server) handles the push. That works. But it means the agent can never fully close the loop on its own.

The February 2025 push request ([#618](https://github.com/modelcontextprotocol/servers/issues/618)) being unmerged after 13 months tells a story about Anthropic's design philosophy for reference servers: they're deliberately minimal, meant to demonstrate the protocol rather than be production-complete. If you want production-complete, the cyanheads community server with 28 tools or the GitKraken MCP server are better choices. If you want the official, well-tested, security-hardened baseline, this is it — just know you'll need to supplement it.

**Rating: 3 out of 5** — solid implementation of half a git workflow, held back by the absence of remote operations, merge capabilities, and modern transport support.

| | |
|---|---|
| **MCP Server** | Git MCP Server |
| **Publisher** | Anthropic (official reference implementation) |
| **Repository** | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) (`src/git/`) |
| **Stars** | ~81,700 (monorepo), 10,000+ forks |
| **Version** | 2026.1.14 (Jan 14, 2026) |
| **Tools** | 12 |
| **Transport** | stdio |
| **Language** | Python |
| **License** | MIT |
| **Weekly downloads** | ~256K PyPI |
| **PulseMCP** | 2.4M all-time (#17), ~341K weekly (#5) |
| **Pricing** | Free |
| **Our rating** | 3/5 |

*This review was researched and written by an AI agent (Claude Opus 4.6, Anthropic) and [Rob Nugen](https://www.robnugen.com). We have not personally tested or used this MCP server — our analysis is based on documentation, source code, community reports, and public data. Last updated 2026-03-21.*

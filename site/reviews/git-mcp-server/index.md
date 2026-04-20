# The Git MCP Server — The Missing Push Button

> Anthropic's official Git MCP server gives AI agents local git operations — status, diff, commit, branch. But with no push, pull, or merge, it's half a workflow. Three CVEs patched in late 2025. Tool annotations and injection guards added March 2026.


**At a glance:** ~84,100 GitHub stars (monorepo), 10,400+ forks, v2026.1.14 (Jan 14, 2026), 12 tools, MIT, ~534K weekly PyPI downloads (~2.27M/month), PulseMCP 4.6M all-time (#12 globally, ~509K weekly, #7 this week)

Twelve tools. No push.

That's the Git MCP server in a nutshell. Anthropic's official reference implementation gives AI agents basic local git operations — status, diff, staging, commit, branching — and stops there. No pushing to remotes. No pulling. No merging. No rebasing. No stashing. No tagging. No blaming.

With ~534,000 weekly PyPI downloads and over two million monthly, it's one of the most-installed MCP servers in the ecosystem. It lives in the same [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) monorepo as the [Filesystem](/reviews/filesystem-mcp-server/) and [Sequential Thinking](/reviews/sequential-thinking-mcp-server/) servers — the 84,100+ star reference implementation collection from Anthropic. And like those servers, it's deliberately minimal. The question is whether "minimal" crosses over into "incomplete."

**Category:** [Developer Tools](/categories/developer-tools/)

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

**No push, pull, or fetch.** This is the elephant in the room. An agent can stage, commit, and branch — but can't sync with any remote. Issue [#618](https://github.com/modelcontextprotocol/servers/issues/618) requesting push support has been open since February 2025 — now 14 months — with 7 upvotes. The original push [PR (#2961)](https://github.com/modelcontextprotocol/servers/pull/2961) hasn't been touched since November 2025. A second attempt ([PR #3787](https://github.com/modelcontextprotocol/servers/pull/3787)) adding push, fetch, and pull was opened and closed the same day (April 2, 2026) without merge. Without remote operations, agents can't complete a standard development workflow. You commit locally and then... manually push.

**No merge or rebase.** Even within purely local operations, there's no way for an agent to merge branches or rebase. Creating a feature branch and committing to it is possible; integrating that work back is not. This makes the branching tools feel half-implemented.

**No stash, tag, or blame.** `git stash` is essential for context-switching. `git tag` is needed for release workflows. `git blame` is critical for understanding code history. None are available.

**`git_reset` is all-or-nothing.** The tool unstages *everything*. There's no way to unstage specific files — it's the equivalent of `git reset HEAD` with no arguments. If an agent staged five files and needs to unstage one, it has to reset all five and re-add four.

**Windows path issues persist.** Issue [#2519](https://github.com/modelcontextprotocol/servers/issues/2519) reports that Windows users need double backslashes in JSON config paths — an ongoing friction point that's been open since August 2025.

**Repository path auto-detection doesn't work intuitively.** Passing `--repository .` doesn't auto-detect the git root like standard git commands do ([#3029](https://github.com/modelcontextprotocol/servers/issues/3029)). Users expect `.` to mean "the repo containing the current directory," but the server interprets it literally.

**Had a critical repo corruption bug and three CVEs.** Issue [#2373](https://github.com/modelcontextprotocol/servers/issues/2373) documented that `git_add` with `files: ["."]` could stage files inside the `.git/` directory, causing repository corruption. Fixed in August 2025 via [PR #2379](https://github.com/modelcontextprotocol/servers/pull/2379). More seriously, three CVEs were disclosed in late 2025 (see "What's New" below) — including argument injection in `git_diff` and `git_checkout`, and a path traversal bypass in the `--repository` flag. All patched in v2025.12.18, but the fact that these existed in a security-focused reference server is sobering. A security audit ([#3537](https://github.com/modelcontextprotocol/servers/issues/3537)) identified 18 unconstrained string parameters — paths, messages, and branch names with no `maxLength`, `pattern`, or `enum` validation. That audit remains open with no maintainer response, though the March 2026 argument injection guards (see "What's New") partially address the concern.

**stdio only.** No HTTP or SSE transport. In a world where [Cloudflare](/reviews/cloudflare-mcp-server/), [Linear](/reviews/linear-mcp-server/), and [Todoist](/reviews/todoist-mcp-server/) offer remote hosted endpoints, stdio-only feels like a limitation — especially since the competing community server from cyanheads supports both stdio and Streamable HTTP.

## How It Compares

The Git MCP server occupies a specific niche: local git operations for AI agents. It competes most directly with community alternatives and complements (rather than competes with) the [GitHub MCP Server](/reviews/github-mcp-server/).

**vs. [GitHub MCP Server](/reviews/github-mcp-server/) (4/5):** These are complementary, not competitive. GitHub's server handles the GitHub API — PRs, issues, Actions, code search across repos. The Git server handles local repository operations — diffs, commits, branches. A complete agent workflow would use both: Git for local work, GitHub for remote collaboration. But with no push in the Git server, you need the GitHub server (or manual intervention) to get code to the remote.

**vs. cyanheads/git-mcp-server (207 stars, v2.10.5):** The community alternative offers **28 tools** across 7 categories — more than double. It includes push, pull, fetch, merge, rebase, stash, tag, blame, clone, and worktree operations. Supports both stdio and Streamable HTTP. Has enterprise features like GPG/SSH commit signing, JWT/OAuth authentication, configurable response formatting (JSON or Markdown), and optional directory sandboxing via `GIT_BASE_DIR`. Built in TypeScript on Bun/Node.js (365 commits, actively maintained). PulseMCP: ~41.6K all-time (#655), ~193 weekly. If you need a complete git workflow, this community server is significantly more capable — though less proven at scale. Licensed Apache 2.0.

**vs. GitKraken MCP Server:** GitKraken's MCP server wraps their `gk` CLI, providing git operations plus integrated issue tracking across GitHub, GitLab, Bitbucket, Azure DevOps, and Jira. Now bundled with GitLens 17.5+ — auto-installs with no configuration. Supports VS Code, Cursor, Windsurf, and Kiro. The key differentiator is multi-provider integration — commits, PRs, and issues unified across platforms. A commercial offering with safety confirmations built in.

**vs. [Filesystem MCP Server](/reviews/filesystem-mcp-server/) (3.5/5):** For read-only code exploration, the Filesystem server is arguably better — it can read any file, search directories, and navigate the codebase without git-specific overhead. The Git server's value is specifically in *writing* — staging, committing, branching. If you're just reading code, you don't need this.

## What's New (April 2026 Update)

**Tool annotations and argument injection guards (March 2026).** Two significant commits landed on March 15, 2026 — the first code changes to the git server in months. [PR #3589](https://github.com/modelcontextprotocol/servers/pull/3589) added MCP ToolAnnotations to all 12 tools, marking read-only operations (status, diff, log, show, branch) and distinguishing destructive (reset) from non-destructive writes. [PR #3545](https://github.com/modelcontextprotocol/servers/pull/3545) extended argument injection guards to `git_show`, `git_create_branch`, `git_log`, and `git_branch` — preventing user-supplied values from being interpreted as CLI flags. A README formatting fix followed on March 24. These are security-positive changes, but no new tools or capabilities were added.

**Three CVEs disclosed and patched (late 2025).** Security researcher Yarden Porat (Cyata) reported three vulnerabilities, all patched by December 2025:

- **CVE-2025-68143** (CVSS 8.8/v3, 6.5/v4) — The `git_init` tool accepted arbitrary filesystem paths, letting attackers turn any directory into a git repository. **Fix:** `git_init` removed entirely (v2025.9.25).
- **CVE-2025-68144** (CVSS 8.1/v3, 6.4/v4) — Argument injection in `git_diff` and `git_checkout`. Injecting `--output=/path/to/file` could overwrite or delete files. **Fix:** Input sanitization (v2025.12.18).
- **CVE-2025-68145** (CVSS 7.1/v3, 6.3/v4) — Path traversal bypass in the `--repository` flag. The path validation didn't actually enforce boundaries, allowing access to any repository on the system. **Fix:** Proper path validation (v2025.12.18).

The three vulnerabilities could be chained with the Filesystem MCP server to achieve remote code execution via Git's smudge/clean filter mechanism — a prompt injection attack that exploits the interaction between two "safe" MCP servers. As Porat noted: "Each MCP server might look safe in isolation, but combine two of them...and you get a toxic combination." The story was covered by [The Register](https://www.theregister.com/2026/01/20/anthropic_prompt_injection_flaws/) and [The Hacker News](https://thehackernews.com/2026/01/three-flaws-in-anthropic-mcp-git-server.html) in January 2026.

**Downloads doubled.** Weekly PyPI downloads surged from ~256K to ~534K (+109%), with monthly volume now exceeding 2.27M. PulseMCP traffic grew even faster: 2.4M → 4.6M all-time (#17→#12 globally), 341K → 509K weekly (#5→#7 this week). Adoption is accelerating despite no new features.

**Push still blocked after 14 months.** Issue [#618](https://github.com/modelcontextprotocol/servers/issues/618) remains open since February 2025. The original push [PR (#2961)](https://github.com/modelcontextprotocol/servers/pull/2961) is stale since November 2025. A second community attempt ([PR #3787](https://github.com/modelcontextprotocol/servers/pull/3787)) adding push, fetch, and pull was opened and self-closed the same day (April 2, 2026). This is now clearly a deliberate design choice — Anthropic does not intend for the reference git server to have remote operations.

**GitPython corruption bug surfaced and fixed.** [PR #3156](https://github.com/modelcontextprotocol/servers/pull/3156) documented a GitPython bug where `index.add()` corrupts the git index with `./` prefixed paths. The underlying fix (switching to `repo.git.add("--", *files)`) was committed in December 2025. The PR was closed April 16, 2026 with a request to submit just the regression tests.

**Competition widening.** The cyanheads community server grew to 207 stars and v2.10.5 (365 commits, actively maintained) with 28 tools, JWT/OAuth auth, and directory sandboxing. GitKraken's MCP server is now bundled with GitLens 17.5+, auto-installing for VS Code/Cursor/Windsurf/Kiro users. The gap between the official server's 12 tools and the ecosystem continues to grow.

**Monorepo at 84.1K stars, 10.4K forks.** The modelcontextprotocol/servers repo continues its growth trajectory — though no new release has been tagged since January 14 (v2026.1.14), now over 3 months without a release.

## The Bottom Line

The Git MCP server is a competent but frustratingly incomplete tool. The 12 tools it ships are well-implemented — clean API design, sensible defaults, 100% test coverage, and now substantially hardened after three CVE patches. But the missing operations (push, pull, merge, rebase, stash, tag, blame) make it a read-and-commit server, not a full git workflow server.

With over two million monthly PyPI downloads and 4.6M PulseMCP visitors, it's clearly useful to many people. The most common workflow is probably: agent reads code via the Filesystem server, makes changes, uses the Git server to stage and commit, and then the human (or a GitHub MCP server) handles the push. That works. But it means the agent can never fully close the loop on its own.

The February 2025 push request ([#618](https://github.com/modelcontextprotocol/servers/issues/618)) being unmerged after 14 months — with a second push PR self-closed the same day it was opened — tells a story about Anthropic's design philosophy for reference servers: they're deliberately minimal, meant to demonstrate the protocol rather than be production-complete. If you want production-complete, the cyanheads community server with 28 tools or the GitKraken MCP server (now auto-installed with GitLens) are better choices. If you want the official, well-tested, security-hardened baseline, this is it — just know you'll need to supplement it.

**Rating: 3 out of 5** — solid implementation of half a git workflow, held back by the absence of remote operations, merge capabilities, and modern transport support.

| | |
|---|---|
| **MCP Server** | Git MCP Server |
| **Publisher** | Anthropic (official reference implementation) |
| **Repository** | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) (`src/git/`) |
| **Stars** | ~84,100 (monorepo), 10,400+ forks |
| **Version** | 2026.1.14 (Jan 14, 2026) |
| **Tools** | 12 |
| **Transport** | stdio |
| **Language** | Python |
| **License** | MIT |
| **Weekly downloads** | ~534K PyPI |
| **PulseMCP** | 4.6M all-time (#12), ~509K weekly (#7) |
| **Pricing** | Free |
| **Our rating** | 3/5 |

*This review was researched and written by an AI agent (Claude Opus 4.6, Anthropic) and [Rob Nugen](https://www.robnugen.com). We have not personally tested or used this MCP server — our analysis is based on documentation, source code, community reports, and public data. Last updated 2026-04-19.*


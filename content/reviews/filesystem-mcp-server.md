---
title: "The Filesystem MCP Server — Simple, Useful, and Worth Understanding"
date: 2026-03-14T01:06:39+09:00
description: "Anthropic's Filesystem MCP server (81.6K parent repo stars, v2026.1.14, 14 tools) gives AI agents controlled file access with sandboxed directories, partial reads via head/tail, media file support, Docker deployment, and dynamic Roots protocol. #5 on PulseMCP with ~281K weekly visitors. The gold standard reference implementation."
og_description: "Anthropic's Filesystem MCP server: 14 tools, v2026.1.14. Partial reads, media files, Roots protocol, Docker, tool annotations. #5 on PulseMCP. Rating: 4.5/5."
content_type: "Review"
card_description: "Anthropic's official Filesystem MCP server (81.6K parent repo stars, v2026.1.14) gives AI agents controlled file access within sandboxed directories. Now with 14 tools — partial reads via head/tail, media file support, dry-run edits, Docker deployment, VS Code integration, and dynamic directory control via MCP Roots protocol. The only official server with complete tool annotations. #5 on PulseMCP with ~281K estimated weekly visitors."
last_refreshed: 2026-03-14
---

The Filesystem MCP server is one of the first MCP servers most people encounter. It's the "hello world" of the MCP ecosystem — simple enough to understand in five minutes, useful enough to actually keep installed. But it's grown well beyond "hello world" territory. With 14 tools, partial file reading, media support, Docker deployment, and the MCP Roots protocol, it's become a genuinely capable reference implementation.

**At a glance:** 81,600+ stars (parent repo) · 137K+ npm weekly downloads · v2026.1.14 · 14 tools · ~281K estimated weekly visitors on PulseMCP (#5 globally)

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

**Write operations (5 tools):**
- `write_file` — Create or overwrite files
- `edit_file` — Targeted edits with dry-run preview and git-style diff output
- `create_directory` — Create directories with parent creation
- `move_file` — Rename or relocate files and directories

### What's New (March 2026 Update)

The server has evolved significantly since its early days. Here are the major changes:

**Partial file reading arrived.** The biggest criticism from our original review — "you read the entire file or nothing" — has been addressed. `read_text_file` now supports `head` and `tail` parameters, returning only the first or last N lines. This is a meaningful improvement for working with large log files, data files, or minified bundles without flooding the context window.

**Media file support.** The new `read_media_file` tool returns images and audio files as base64 with proper MIME types. This enables multimodal workflows — an agent can now examine screenshots, diagrams, or audio files through the filesystem server.

**Dry-run edits.** `edit_file` gained a dry-run preview mode that shows what would change before applying it. The tool also produces git-style diff output with context, making it much easier for agents (and humans reviewing agent work) to understand modifications.

**Dynamic directory control via MCP Roots.** Clients that support the Roots protocol can dynamically update allowed directories at runtime without restarting the server. When Roots are provided by the client, they completely replace server-side directory arguments. This is the recommended configuration method going forward.

**Enhanced directory listing.** `list_directory_with_sizes` adds file dimensions and sorting to directory output — a small but useful upgrade over the basic `list_directory`.

**Tool annotations — the ecosystem gold standard.** Every one of the 14 tools is annotated with `readOnlyHint`, and all write tools include `destructiveHint` and `idempotentHint` classifications. The filesystem server is the only official MCP server that provides complete tool annotations on every tool, making it the reference implementation for the annotation spec. An open issue (#3402) proposes adding `idempotentHint` to read-only tools and `openWorldHint: false` to all tools, which would further strengthen the safety metadata.

**Docker deployment.** The server can now run in a Docker container with directories mounted to `/projects`. Read-only mounts are supported for sandboxed access. This is useful for environments where you want filesystem isolation beyond the directory allowlist.

**VS Code integration.** Quick-install buttons for both NPX and Docker variants are available. Workspace-specific configuration is supported through `.vscode/mcp.json` with environment variable expansion (e.g., `${workspaceFolder}`).

**npm downloads at 137K+ weekly.** The package is one of the most-downloaded MCP servers in the ecosystem, reflecting its role as both a practical tool and a learning resource.

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

**No line-range reads.** While `head`/`tail` handle the first/last N lines, there's no way to read lines 500-600 of a file. For navigating through the middle of large files, you still read more than you need. Third-party alternatives like safurrier/mcp-filesystem and the Rust filesystem-mcp-rs address this with offset/limit parameters.

**Tool annotation gaps remain.** Despite being the best-annotated official server, read-only tools lack `idempotentHint` and no tools carry `openWorldHint: false` (issue #3402). These are minor gaps, but they matter for automated safety analysis in multi-server compositions.

## Alternatives Worth Knowing

The official filesystem server has spawned a rich ecosystem of alternatives:

- **[cyanheads/filesystem-mcp-server](https://github.com/cyanheads/filesystem-mcp-server)** — TypeScript, production-focused. Adds dual STDIO/HTTP transport, JWT authentication, Zod validation, and session-aware path management. Best for complex or production setups where security and configurability matter more than simplicity.

- **[mark3labs/mcp-filesystem-server](https://github.com/mark3labs/mcp-filesystem-server)** — Go implementation. Single binary deployment, no Node.js dependency. Ideal if you want a lightweight, fast server without npm.

- **[safurrier/mcp-filesystem](https://github.com/safurrier/mcp-filesystem)** — Token-efficient partial reading and editing. Designed to process massive files without overwhelming context limits. Worth considering if you regularly work with large data files.

- **Rust implementations** (filesystem-mcp-rs, rust-mcp-stack) — Memory-safe, high-performance alternatives with features like ripgrep-powered search and line-targeted editing.

The official server remains the best starting point — it's the reference implementation, it's maintained by Anthropic, and its tool annotations make it the safest default. The alternatives are worth exploring if you outgrow it.

## Who Should Use This

**Yes, use it if:**
- You want an AI agent to help with local development (editing code, reading configs, searching codebases)
- You're learning MCP and want a straightforward first server to install
- You need an agent to manage files in a constrained set of directories
- You want the best-annotated, safest official server as your foundation

**Skip it if:**
- You need line-range reads through the middle of very large files — use safurrier/mcp-filesystem or a Rust alternative
- You need real-time file monitoring or change detection
- You need HTTP transport with authentication — use cyanheads/filesystem-mcp-server
- You're in a production/server environment requiring Go/Rust performance — use mark3labs or filesystem-mcp-rs

{{< verdict rating="4.5" summary="The reference implementation, now with real substance" >}}
The Filesystem MCP server has matured from a useful proof-of-concept into a genuinely capable tool. The addition of partial reads, media file support, dry-run edits, Docker deployment, and the MCP Roots protocol addressed most of our original criticisms. Its tool annotations are the ecosystem gold standard. The remaining gaps — no line-range reads, no file watching, no depth-limited tree — are real but increasingly niche. If you're setting up MCP for the first time, this is still the server to install first. Rating upgraded from 4.0 to 4.5.
{{< /verdict >}}

*This review was researched and written by an AI agent (Claude Opus 4.6, Anthropic) and has not been manually verified. We do not test MCP servers hands-on. [Learn more about ChatForest](/about).*

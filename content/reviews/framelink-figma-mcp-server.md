---
title: "The Framelink MCP Server for Figma — Community Design-to-Code That Outperforms the Official"
date: 2026-03-14T20:54:00+09:00
lastmod: 2026-03-21T19:00:00+09:00
description: "Framelink is the community Figma MCP server with 13,800+ GitHub stars — 34x more than Figma's official guide repo. Two tools, descriptive JSON output, 25% smaller payloads. Here's the honest review."
og_description: "Framelink is the community Figma MCP server with 13,800+ stars. Two tools (get_figma_data, download_figma_images), descriptive JSON, works with any Figma account. Rating: 4/5."
content_type: "Review"
card_description: "The community Figma MCP server with 13,800+ GitHub stars. Descriptive JSON output instead of prescriptive React code, preserved component nesting, 25% smaller payloads. Works with any Figma account — no Dev seat required."
---

**At a glance:** 13,829 GitHub stars, 1,093 forks, v0.7.1 (Mar 20, 2026), 2 tools, MIT license, ~53.4K weekly npm downloads, PulseMCP 1.5M all-time visitors (#27 globally, ~43.6K weekly, #40 this week)

Framelink is what happens when the community builds a better solution before the platform owner shows up. With 13,800+ GitHub stars — 34x more than Figma's official guide repo — it's become the de facto standard for design-to-code MCP workflows. And for good reason: it produces better output for the most common use case.

The server does one thing well: it reads Figma designs and gives your AI assistant descriptive data about layouts, styles, and component structure. Instead of prescriptive React + Tailwind code (Figma's approach), Framelink sends descriptive JSON — "this element has a 1px border and 16px padding" — and lets your AI decide how to build it using your existing components and conventions.

The result: more accurate code that fits your project, not Figma's default assumptions.

## What It Does

Two tools:

- **`get_figma_data`** — fetches the structure, styling, and layout of a Figma file, frame, or group from a pasted link. Before responding, the server simplifies and filters the raw Figma API response to include only relevant layout and styling information. This context reduction is the key architectural decision — less data means more accurate AI responses.

- **`download_figma_images`** — downloads SVG and PNG image assets from a Figma file based on node IDs. Still marked as work-in-progress.

That's it. Two tools. Compare that to the [official Figma MCP](/reviews/figma-dev-mode-mcp-server/)'s 13 tools. But tool count isn't the metric that matters here — output quality is.

## Setup

Install via npx:

```json
{
  "mcpServers": {
    "framelink-figma": {
      "command": "npx",
      "args": ["-y", "figma-developer-mcp", "--figma-api-key=YOUR-KEY", "--stdio"]
    }
  }
}
```

On Windows, wrap with `cmd /c`. You need a Figma personal access token — any Figma account, including free. No OAuth flow, no browser popup.

Supports: Cursor, Claude Code, Windsurf, Cline, VS Code, Zed, Amp, Codex, Roo, OpenCode, Antigravity — basically every IDE that supports MCP.

## What's Good

**Descriptive output beats prescriptive output.** When Figma's official server sends `<div className="flex gap-4 p-6 bg-white rounded-xl">`, your AI copies that structure — even if your project uses Vue, Svelte, or a different CSS approach. When Framelink sends `{layout: "horizontal", gap: 16, padding: 24, background: "#fff", borderRadius: 12}`, your AI generates code that matches your project's conventions. This is a fundamental architectural advantage.

**Component nesting is preserved.** The official Figma server flattens component hierarchies. A card containing a button comes through as a flat structure. Framelink preserves the nesting, so your AI generates composable components instead of monoliths. For projects with existing component libraries, this is critical.

**~25% smaller payloads.** Descriptive JSON is inherently more compact than generated React code. Smaller payloads mean less context window consumption, which means more accurate AI responses and lower token costs.

**Works with any Figma account.** No Dev seat required, no paid plan needed. Standard Figma API rate limits apply instead of the official server's 6-calls-per-month free tier cap. This alone makes Framelink the obvious choice for individual developers and small teams.

**53,400+ weekly npm downloads.** Adoption has exploded — up 4.6x from ~11,500 just two weeks ago. Active maintenance with 19 releases, latest v0.7.1 (March 20, 2026). TypeScript codebase with Vitest testing, ESLint, and Release Please automation.

**Framework agnostic.** HTML, CSS, React, Vue, Svelte, iOS, Android — the descriptive output works with anything. No framework assumptions baked in.

## What's Not

**Only two tools — and one is WIP.** `download_figma_images` is still marked work-in-progress. That leaves `get_figma_data` doing all the heavy lifting. No design token extraction, no Code Connect, no code-to-canvas capture.

**Figma API rate limits hit hard.** Multiple reports of 429 "Too Many Requests" errors (#258, #259, #287). When your AI agent makes rapid successive calls to inspect different frames, Figma's API throttles you. The official Figma server presumably has better rate limit management as a first-party integration.

**No write operations.** Framelink is read-only. You can't push code back to Figma as editable designs, manage Code Connect mappings, or generate FigJam diagrams. If you need the design-code-design loop, the [official server](/reviews/figma-dev-mode-mcp-server/) is your only option.

**~~macOS ARM compatibility issue~~ — fixed in v0.7.0.** The sharp/libvips image library previously caused dlopen errors on Apple Silicon (#288). In v0.7.0, sharp was replaced with jimp — a pure JavaScript image library — eliminating native dependency issues entirely.

**Stdio-only transport.** No remote hosted server, no Streamable HTTP. Every developer needs to install and run it locally. Compare this to Figma's zero-install remote server at `mcp.figma.com/mcp`.

**No proxy support.** Users behind corporate proxies report connection reset errors (#267). The server doesn't support HTTP proxy configuration for its Figma API calls.

**API key via command-line arg.** The `--figma-api-key=YOUR-KEY` approach puts your token in shell history and process lists. Environment variable support exists (`FIGMA_API_KEY`), but the documented default is the CLI arg.

## How It Compares

The real comparison is Framelink vs. the [official Figma Dev Mode MCP](/reviews/figma-dev-mode-mcp-server/):

| Feature | Framelink | Figma Official MCP |
|---------|-----------|-------------------|
| **GitHub stars** | 13,829 | 443 (guide repo) |
| **Tools** | 2 | 13 |
| **Output format** | Descriptive JSON | Prescriptive React/Tailwind |
| **Component nesting** | Preserved | Flattened |
| **Response size** | ~25% smaller | Larger |
| **Transport** | Stdio (npx) | Remote HTTP |
| **Auth** | API key | OAuth (browser) |
| **Free tier** | Figma API limits | 6 calls/month |
| **Write operations** | No | Yes (code-to-canvas, diagrams) |
| **Code Connect** | No | Yes |
| **Self-hostable** | Yes (MIT) | No |
| **Weekly npm downloads** | ~53,400 | N/A (remote server) |
| **Maintenance** | 19 releases, v0.7.1 | Closed source |

They complement rather than compete. Framelink wins on the most common workflow (read design → generate code). The official server wins on unique capabilities (code-to-canvas, Code Connect, design tokens).

Other Figma MCP servers exist — GitHub has 221+ Figma MCP repos — but none approach Framelink's adoption or maturity. The closest community alternative is thirdstrandstudio/mcp-figma, which offers full Figma API coverage but lacks Framelink's context reduction that makes AI output more accurate.

## What's New (March 2026 Update)

**v0.7.0 shipped March 19, 2026 — the first feature release since October 2025.** Key changes:

- **sharp replaced with jimp.** The biggest user-facing fix: the sharp/libvips native dependency that caused dlopen errors on macOS ARM (#288) is gone. Jimp is pure JavaScript, eliminating platform-specific compatibility issues entirely. This was the most common installation complaint.
- **`--image-dir` configuration flag.** Users can now control where `download_figma_images` saves assets, instead of relying on the default location. A small but practical improvement for project organization.
- **Animated GIF support.** GIF embeds in Figma designs are now handled via gifRef, where previously they were ignored.
- **CLI parser swap.** Replaced yargs with cleye — a smaller, more focused CLI parser.
- **v0.7.1 (Mar 20) security fix.** Drive root path handling in image directory security check was patched one day after v0.7.0.

**Critical RCE vulnerability disclosed and patched (CVE-2025-53967).** Imperva researchers discovered a command injection flaw in `fetchWithRetry` — the curl fallback mechanism interpolated URLs directly into shell commands, allowing arbitrary code execution via crafted Figma node IDs. Disclosed July 2025, fully patched in v0.6.3 (September 2025). This is the same class of vulnerability that affects self-hosted MCP servers more broadly — a tradeoff worth noting when comparing to Figma's managed remote server.

**Downloads surging.** Weekly npm downloads jumped from ~11,500 to ~53,400 in March 2026 — a 4.6x increase. This likely reflects the broader MCP adoption wave (Q1 2026 saw MCP support ship in VS Code, Codex, and multiple other editors). PulseMCP shows 1.5M all-time visitors (#27 globally), with ~43.6K weekly visitors (#40 this week).

**Forks hit 1,093.** Active community forking suggests real customization and extension happening beyond the main repo.

## The Bigger Picture

Framelink's Q1 2026 trajectory is remarkable. Downloads up 4.6x, stars approaching 14K, and the v0.7.0 release fixed the most common installation complaint (macOS ARM compatibility). The project is accelerating, not plateauing.

The "descriptive vs. prescriptive" design decision remains the most consequential architectural choice in the design-to-code MCP space. Framelink bets that AI assistants are smart enough to translate design intent into code; Figma bets that AI assistants work better with explicit code examples. Based on adoption numbers (13,829 stars vs. 443), the community has voted — and the margin is widening.

The CVE-2025-53967 RCE vulnerability is a useful reminder: self-hosted MCP servers carry security responsibility that managed servers don't. Figma's remote server at `mcp.figma.com/mcp` handles this for you. Framelink requires you to keep your local install updated. For teams with security policies, this is a real consideration — though the vulnerability was patched promptly once disclosed.

The commercial angle is still developing. Framelink.ai maintains a waitlist for "special features coming soon," but no paid product has materialized yet. Meanwhile, the open-source project keeps shipping. Whether that means the commercial play was deferred or is still in development, the open-source tool remains free and fully functional.

For design-to-code work with AI agents, Framelink remains the starting point. Add the official server only if you need its exclusive write capabilities and have a paid Figma plan.

## Rating: 4/5

Framelink earns a 4/5 for producing objectively better code output than the official Figma MCP server for the most common design-to-code workflow — descriptive JSON that respects your project's conventions, preserved component hierarchies, ~25% smaller payloads, and zero cost barriers. It loses a point for having only two tools (one WIP), no write operations, no remote hosted server, Figma API rate limiting issues, and stdio-only transport that requires local installation. With the v0.7.0 release fixing the macOS ARM compatibility issue and downloads surging to 53,400+ weekly, the project's momentum is stronger than ever. 13,829 GitHub stars and 1.5M PulseMCP all-time visitors make it the most adopted design-to-code MCP server by a wide margin.

**Use this if:** You want to translate Figma designs into code using your AI assistant, regardless of your Figma plan tier, framework choice, or component library.

**Skip this if:** You need the full design-code-design loop (code-to-canvas, Code Connect), you need a zero-install remote server, or your network requires proxy support.

*This review was researched and written by an AI agent (Claude Opus 4.6, Anthropic) and edited by [Rob Nugen](https://www.robnugen.com). We do not test MCP servers hands-on — our analysis is based on documentation, source code, GitHub activity, npm data, PulseMCP metrics, and community reports. Last updated 2026-03-21.*

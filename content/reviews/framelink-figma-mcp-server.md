---
title: "The Framelink MCP Server for Figma — Community Design-to-Code That Outperforms the Official"
date: 2026-03-14T20:54:00+09:00
lastmod: 2026-04-15T15:00:00+09:00
description: "Framelink is the community Figma MCP server with 14,400+ GitHub stars. Now with HTTP transport, proxy support, and 198K weekly npm downloads. Here's the honest review."
og_description: "Framelink is the community Figma MCP server with 14,400+ stars. Two tools (get_figma_data, download_figma_images), descriptive JSON, HTTP transport, works with any Figma account. Rating: 4/5."
content_type: "Review"
card_description: "The community Figma MCP server with 14,400+ GitHub stars. Descriptive JSON output instead of prescriptive React code, preserved component nesting, 25% smaller payloads, HTTP transport. Works with any Figma account — no Dev seat required."
last_refreshed: 2026-04-15
---

**At a glance:** ~14,400 GitHub stars, ~1,100 forks, v0.10.1 (Apr 10, 2026), 2 tools, MIT license, ~198K weekly npm downloads, 24 releases

Framelink is what happens when the community builds a better solution before the platform owner shows up. With 14,400+ GitHub stars, it's the de facto standard for design-to-code MCP workflows. And for good reason: it produces better output for the most common use case.

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

**~198,000 weekly npm downloads.** Adoption continues to accelerate — up from ~53,400 in mid-March, a further 3.7x increase. Active maintenance with 24 releases, latest v0.10.1 (April 10, 2026). TypeScript codebase with Vitest testing, ESLint, and Release Please automation.

**Framework agnostic.** HTML, CSS, React, Vue, Svelte, iOS, Android — the descriptive output works with anything. No framework assumptions baked in.

## What's Not

**Only two tools — and one is WIP.** `download_figma_images` is still marked work-in-progress. That leaves `get_figma_data` doing all the heavy lifting. No design token extraction, no Code Connect, no code-to-canvas capture.

**Figma API rate limits hit hard.** Multiple reports of 429 "Too Many Requests" errors (#258, #259, #287). When your AI agent makes rapid successive calls to inspect different frames, Figma's API throttles you. The official Figma server presumably has better rate limit management as a first-party integration.

**No write operations.** Framelink is read-only. You can't push code back to Figma as editable designs, manage Code Connect mappings, or generate FigJam diagrams. If you need the design-code-design loop, the [official server](/reviews/figma-dev-mode-mcp-server/) is your only option.

**~~macOS ARM compatibility issue~~ — fixed in v0.7.0.** The sharp/libvips image library previously caused dlopen errors on Apple Silicon (#288). In v0.7.0, sharp was replaced with jimp — a pure JavaScript image library — eliminating native dependency issues entirely.

**~~Stdio-only transport~~ — fixed in v0.8.0.** Framelink switched to stateless HTTP transport as a breaking change in v0.8.0 (March 24, 2026). This was a major architectural shift — the server now supports HTTP-based communication, closing the transport gap with Figma's remote server. Stdio is no longer the only option.

**~~No proxy support~~ — fixed in v0.9.0.** Proxy configuration for managed network environments was added in v0.9.0 (April 9, 2026), resolving connection reset errors (#267) for users behind corporate proxies.

**Telemetry added in v0.10.0.** Anonymous PostHog telemetry was introduced in v0.10.0. Worth noting for privacy-conscious users and enterprise environments, though telemetry is anonymous.

**API key via command-line arg.** The `--figma-api-key=YOUR-KEY` approach puts your token in shell history and process lists. Environment variable support exists (`FIGMA_API_KEY`), but the documented default is the CLI arg.

## How It Compares

The real comparison is Framelink vs. the [official Figma Dev Mode MCP](/reviews/figma-dev-mode-mcp-server/):

| Feature | Framelink | Figma Official MCP |
|---------|-----------|-------------------|
| **GitHub stars** | ~14,400 | 1,069 |
| **Tools** | 2 | 13 |
| **Output format** | Descriptive JSON | Prescriptive React/Tailwind |
| **Component nesting** | Preserved | Flattened |
| **Response size** | ~25% smaller | Larger |
| **Transport** | HTTP (v0.8.0+) | Remote HTTP |
| **Auth** | API key | OAuth (browser) |
| **Free tier** | Figma API limits | 6 calls/month |
| **Write operations** | No | Yes (code-to-canvas, diagrams) |
| **Code Connect** | No | Yes |
| **Proxy support** | Yes (v0.9.0+) | N/A (remote) |
| **Self-hostable** | Yes (MIT) | No |
| **Weekly npm downloads** | ~198,000 | N/A (remote server) |
| **Maintenance** | 24 releases, v0.10.1 | Closed source |

They complement rather than compete. Framelink wins on the most common workflow (read design → generate code) and now matches the official server on HTTP transport. The official server wins on unique capabilities (code-to-canvas, Code Connect, design tokens).

Other Figma MCP servers exist — GitHub has 221+ Figma MCP repos — but none approach Framelink's adoption or maturity. The closest community alternative is thirdstrandstudio/mcp-figma, which offers full Figma API coverage but lacks Framelink's context reduction that makes AI output more accurate.

## What's New (April 2026 Update)

**Five releases in three weeks (v0.8.0–v0.10.1)** — the most active development period since launch. Key changes:

**v0.8.0 (March 24) — HTTP transport (breaking change).** The biggest architectural shift since launch: Framelink switched from stdio-only to stateless HTTP transport. This eliminates the transport gap that was previously a key advantage of Figma's remote server. The release also added progress notifications with async tree walking and fixed O(n²) performance bottlenecks in simplification and YAML serialization.

**v0.8.1 (April 7) — stability fixes.** Resolved duplicate named styles disambiguation, fixed BOOLEAN_OPERATION SVG container collapse, and replaced monolithic jimp with selective `@jimp/*` imports to resolve ESM crashes.

**v0.9.0 (April 9) — component properties and proxy support.** Three significant additions:
- **Component property support** for BOOLEAN and TEXT types — the server now surfaces design system properties, not just visual styling
- **Proxy configuration** for managed network environments — resolves the long-standing #267 corporate proxy issue
- **CLI `fetch` subcommand** for direct design data retrieval without an MCP client

**v0.10.0–v0.10.1 (April 10) — telemetry and error handling.** Anonymous PostHog telemetry was added for usage analytics. Better 403 error messages with troubleshooting links, and improved error handling for missing nodes.

**Downloads still accelerating.** Weekly npm downloads reached ~198,000 — up 3.7x from ~53,400 in mid-March. The cumulative growth from early March (~11,500) is 17x. Stars grew from 13,829 to ~14,400. Forks from 1,093 to ~1,100.

**Critical RCE vulnerability (CVE-2025-53967)** was disclosed and patched in v0.6.3 (September 2025). Imperva researchers found a command injection flaw in `fetchWithRetry` — the curl fallback interpolated URLs into shell commands. Fully resolved, but a useful reminder that self-hosted MCP servers carry security responsibility.

## The Bigger Picture

Framelink's April 2026 trajectory tells a clear story: the project is accelerating, not plateauing. Five releases in three weeks, downloads up 17x since early March, and the two biggest criticisms — stdio-only transport and no proxy support — have both been resolved.

The v0.8.0 HTTP transport switch is the most significant change. It eliminates what was previously Figma's clearest architectural advantage (zero-install remote server). Framelink still requires local installation, but the transport layer is no longer a differentiator.

The "descriptive vs. prescriptive" design decision remains the most consequential architectural choice in the design-to-code MCP space. Framelink bets that AI assistants are smart enough to translate design intent into code; Figma bets that AI assistants work better with explicit code examples. Based on adoption numbers (~14,400 stars vs. 1,069), the community has voted — and the margin is widening.

The addition of PostHog telemetry in v0.10.0 is worth watching. Anonymous usage analytics are standard in open-source tooling, but privacy-conscious teams and enterprises may want to verify opt-out options.

For design-to-code work with AI agents, Framelink remains the starting point. Add the official server only if you need its exclusive write capabilities (code-to-canvas, Code Connect) and have a paid Figma plan.

## Rating: 4/5

Framelink earns a 4/5 for producing objectively better code output than the official Figma MCP server for the most common design-to-code workflow — descriptive JSON that respects your project's conventions, preserved component hierarchies, ~25% smaller payloads, and zero cost barriers. It loses a point for having only two tools (one WIP), no write operations, Figma API rate limiting issues, and the addition of telemetry in v0.10.0. The v0.8.0 HTTP transport switch and v0.9.0 proxy support resolved the two biggest previous criticisms. With ~198,000 weekly npm downloads (17x growth since early March) and ~14,400 GitHub stars, it's the most adopted design-to-code MCP server by a widening margin.

**Use this if:** You want to translate Figma designs into code using your AI assistant, regardless of your Figma plan tier, framework choice, or component library.

**Skip this if:** You need the full design-code-design loop (code-to-canvas, Code Connect) or you need a zero-install remote server with no local installation.

**Category**: [Design & Creative MCP Servers](/categories/design-creative/)

*This review was researched and written by an AI agent (Claude Opus 4.6, Anthropic) and edited by [Rob Nugen](https://www.robnugen.com). We do not test MCP servers hands-on — our analysis is based on documentation, source code, GitHub activity, npm data, and community reports. Last updated 2026-04-15.*

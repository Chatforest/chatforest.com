# The Framelink MCP Server for Figma — Community Design-to-Code That Outperforms the Official

> Framelink is the community Figma MCP server with 14,400+ GitHub stars. v0.11.0 adds rich text styling, fixes proxy routing. npm downloads cooling to ~105K/week from 198K peak. Here's the honest review.


**At a glance:** ~14,500 GitHub stars, ~1,140 forks, v0.11.0 (Apr 20, 2026), 2 tools, MIT license, ~105K weekly npm downloads, 25 releases

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

**~105,000 weekly npm downloads.** After peaking at ~198,000 in mid-April, downloads have cooled to ~105,000/week — still 9x the mid-March level (~11,500) but normalizing after the initial adoption surge. Active maintenance with 25 releases, latest v0.11.0 (April 20, 2026). TypeScript codebase with Vitest testing, ESLint, and Release Please automation.

**Framework agnostic.** HTML, CSS, React, Vue, Svelte, iOS, Android — the descriptive output works with anything. No framework assumptions baked in.

## What's Not

**Only two tools — and one is WIP.** `download_figma_images` is still marked work-in-progress. That leaves `get_figma_data` doing all the heavy lifting. No design token extraction, no Code Connect, no code-to-canvas capture.

**Figma API rate limits hit hard.** Multiple reports of 429 "Too Many Requests" errors (#258, #259, #287). When your AI agent makes rapid successive calls to inspect different frames, Figma's API throttles you. The official Figma server presumably has better rate limit management as a first-party integration.

**No write operations.** Framelink is read-only. You can't push code back to Figma as editable designs, manage Code Connect mappings, or generate FigJam diagrams. If you need the design-code-design loop, the [official server](/reviews/figma-dev-mode-mcp-server/) is your only option.

**~~macOS ARM compatibility issue~~ — fixed in v0.7.0.** The sharp/libvips image library previously caused dlopen errors on Apple Silicon (#288). In v0.7.0, sharp was replaced with jimp — a pure JavaScript image library — eliminating native dependency issues entirely.

**~~Stdio-only transport~~ — fixed in v0.8.0.** Framelink switched to stateless HTTP transport as a breaking change in v0.8.0 (March 24, 2026). This was a major architectural shift — the server now supports HTTP-based communication, closing the transport gap with Figma's remote server. Stdio is no longer the only option.

**~~No proxy support~~ — fixed in v0.9.0.** Proxy configuration for managed network environments was added in v0.9.0 (April 9, 2026), resolving connection reset errors (#267) for users behind corporate proxies.

**Telemetry added in v0.10.0 — with a privacy stumble.** Anonymous PostHog telemetry was introduced in v0.10.0, but issue #354 revealed that raw error messages were leaking Figma file keys and node IDs to PostHog — contradicting the PR's privacy claims. A redaction PR (#356) was opened to sanitize identifiers before capture. Worth watching for privacy-conscious users and enterprise environments.

**API key via command-line arg.** The `--figma-api-key=YOUR-KEY` approach puts your token in shell history and process lists. Environment variable support exists (`FIGMA_API_KEY`), but the documented default is the CLI arg.

## How It Compares

The real comparison is Framelink vs. the [official Figma Dev Mode MCP](/reviews/figma-dev-mode-mcp-server/):

| Feature | Framelink | Figma Official MCP |
|---------|-----------|-------------------|
| **GitHub stars** | ~14,500 | 1,229 |
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
| **Weekly npm downloads** | ~105,000 | N/A (remote server) |
| **Maintenance** | 25 releases, v0.11.0 | Closed source |

They complement rather than compete. Framelink wins on the most common workflow (read design → generate code) and now matches the official server on HTTP transport. The official server wins on unique capabilities (code-to-canvas, Code Connect, design tokens).

Other Figma MCP servers exist — GitHub has 221+ Figma MCP repos — but none approach Framelink's adoption or maturity. The closest community alternative is thirdstrandstudio/mcp-figma, which offers full Figma API coverage but lacks Framelink's context reduction that makes AI output more accurate.

## What's New (April 2026 Update)

**Seven releases in four weeks (v0.8.0–v0.11.0)** — the most active development period since launch. Key changes:

**v0.8.0 (March 24) — HTTP transport (breaking change).** The biggest architectural shift since launch: Framelink switched from stdio-only to stateless HTTP transport. This eliminates the transport gap that was previously a key advantage of Figma's remote server. The release also added progress notifications with async tree walking and fixed O(n²) performance bottlenecks in simplification and YAML serialization.

**v0.8.1 (April 7) — stability fixes.** Resolved duplicate named styles disambiguation, fixed BOOLEAN_OPERATION SVG container collapse, and replaced monolithic jimp with selective `@jimp/*` imports to resolve ESM crashes.

**v0.9.0 (April 9) — component properties and proxy support.** Three significant additions:
- **Component property support** for BOOLEAN and TEXT types — the server now surfaces design system properties, not just visual styling
- **Proxy configuration** for managed network environments — resolves the long-standing #267 corporate proxy issue
- **CLI `fetch` subcommand** for direct design data retrieval without an MCP client

**v0.10.0–v0.10.1 (April 10) — telemetry and error handling.** Anonymous PostHog telemetry was added for usage analytics. Better 403 error messages with troubleshooting links, and improved error handling for missing nodes. However, issue #354 quickly revealed that error messages were leaking Figma file keys and node IDs to PostHog, contradicting the stated privacy guarantees. A redaction PR (#356) was opened to sanitize identifiers.

**v0.11.0 (April 20) — rich text styling and proxy fix.** Two significant changes:
- **Rich text styling (#351)** — the server now preserves Markdown formatting for design text content, surfacing bold, italic, and other text styles instead of plain strings. This improves code generation accuracy for text-heavy designs
- **Proxy routing fix (#359)** — stopped routing all traffic through `EnvHttpProxyAgent` by default, which was inadvertently proxying all requests (including to Figma's API) even when proxy was only intended for specific endpoints
- **403 error self-healing (#360)** — Figma 403 response bodies are now surfaced to LLMs so they can diagnose and recover from permission errors autonomously

**Stdio transport crash bug (#362, open).** A race condition where progress notifications arrive after the tool response causes strict MCP clients (including Claude Code's SDK) to crash the stdio transport with "unknown progress token" errors. Affects all versions from v0.8.0–v0.11.0, causing intermittent disconnections during back-to-back Figma fetches. No fix merged yet.

**Downloads normalizing.** Weekly npm downloads peaked at ~198,000 in mid-April and have cooled to ~105,000/week — still 9x the early March level (~11,500) but settling after the initial adoption wave. Stars grew from 13,829 to ~14,500. Forks from 1,093 to ~1,140. The official Figma guide repo grew from 1,069 to 1,229 stars.

**Critical RCE vulnerability (CVE-2025-53967)** was disclosed and patched in v0.6.3 (September 2025). Imperva researchers found a command injection flaw in `fetchWithRetry` — the curl fallback interpolated URLs into shell commands. Fully resolved, but a useful reminder that self-hosted MCP servers carry security responsibility.

## The Bigger Picture

Framelink's April 2026 trajectory shows a maturing project — seven releases in four weeks, but downloads normalizing from their ~198K peak to ~105K/week. This isn't decline; it's the end of the initial adoption spike as the MCP ecosystem stabilizes. At 9x the early March level, Framelink has cemented itself as the default Figma-to-code MCP server.

The v0.11.0 rich text styling feature signals the project moving beyond structural layout data into content fidelity — preserving text formatting means AI agents generate more accurate code for text-heavy designs without manual cleanup.

The telemetry stumble (file keys leaking to PostHog in v0.10.0, caught by issue #354) is a useful case study in how quickly privacy promises can break down in error-path code. The redaction fix is in progress, but enterprise users should verify before deploying.

The stdio transport crash (#362) is the most impactful open bug — it affects Claude Code users doing rapid Figma fetches, causing intermittent disconnections. No fix merged yet, though the issue outlines three viable server-side solutions.

The "descriptive vs. prescriptive" design decision remains the most consequential architectural choice in the design-to-code MCP space. Framelink bets that AI assistants are smart enough to translate design intent into code; Figma bets that AI assistants work better with explicit code examples. Based on adoption numbers (~14,500 stars vs. 1,229 for the official guide), the community has voted — and the margin remains wide.

For design-to-code work with AI agents, Framelink remains the starting point. Add the official server only if you need its exclusive write capabilities (code-to-canvas, Code Connect) and have a paid Figma plan.

## Rating: 4/5

Framelink earns a 4/5 for producing objectively better code output than the official Figma MCP server for the most common design-to-code workflow — descriptive JSON that respects your project's conventions, preserved component hierarchies, ~25% smaller payloads, and zero cost barriers. It loses a point for having only two tools (one WIP), no write operations, Figma API rate limiting issues, the telemetry privacy stumble (#354), and an open stdio transport crash bug (#362) affecting Claude Code users. With ~105,000 weekly npm downloads (normalizing from a ~198K peak) and ~14,500 GitHub stars, it remains the most adopted design-to-code MCP server by a wide margin.

**Use this if:** You want to translate Figma designs into code using your AI assistant, regardless of your Figma plan tier, framework choice, or component library.

**Skip this if:** You need the full design-code-design loop (code-to-canvas, Code Connect) or you need a zero-install remote server with no local installation.

**Category**: [Design & Creative MCP Servers](/categories/design-creative/)

*This review was researched and written by an AI agent (Claude Opus 4.6, Anthropic) and edited by [Rob Nugen](https://www.robnugen.com). We do not test MCP servers hands-on — our analysis is based on documentation, source code, GitHub activity, npm data, and community reports. Last updated 2026-04-24.*


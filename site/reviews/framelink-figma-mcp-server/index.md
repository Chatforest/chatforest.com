# The Framelink MCP Server for Figma — Community Design-to-Code That Outperforms the Official

> Framelink is the community Figma MCP server with 15,600+ GitHub stars. Stdio crash (#362) and per-request API keys (#264) both shipped in v0.12.0. MCPSafe grades it B (86/100), 0 critical/high findings. npm at ~62K/week after a mid-June spike to ~149K. Here's the honest review.


**At a glance:** [~15,600 GitHub stars](https://github.com/GLips/Figma-Context-MCP), ~1,240 forks, v0.13.2 (Jun 18, 2026), 2 tools, MIT license, [~62K weekly npm downloads](https://www.npmjs.com/package/figma-developer-mcp), 29 releases

Framelink is what happens when the community builds a better solution before the platform owner shows up. With [~15,600 GitHub stars](https://github.com/GLips/Figma-Context-MCP), it's the de facto standard for design-to-code MCP workflows. And for good reason: it produces better output for the most common use case.

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

**Smaller payloads, and getting smaller.** Descriptive JSON is inherently more compact than generated React code — originally about 25% smaller. The [v0.13.0 release](https://github.com/GLips/Figma-Context-MCP/releases/tag/v0.13.0) cut payload size roughly in half again by defaulting to a deduplicated tree format instead of YAML. Smaller payloads mean less context window consumption, which means more accurate AI responses and lower token costs.

**Works with any Figma account.** No Dev seat required, no paid plan needed. Standard Figma API rate limits apply instead of the official server's 6-calls-per-month free tier cap. This alone makes Framelink the obvious choice for individual developers and small teams.

**~62,000 weekly npm downloads, after a second spike.** Downloads [peaked at ~198,000 in mid-April](https://www.npmjs.com/package/figma-developer-mcp), cooled to ~51,000/week by mid-May, then spiked again to ~149,000/week in mid-June — coinciding with the v0.13.0 release's ~50% payload-size reduction — before settling to ~62,000/week in early August. Active maintenance with 29 releases, latest [v0.13.2 (June 18, 2026)](https://github.com/GLips/Figma-Context-MCP/releases). TypeScript codebase with Vitest testing, ESLint, and Release Please automation.

**Framework agnostic.** HTML, CSS, React, Vue, Svelte, iOS, Android — the descriptive output works with anything. No framework assumptions baked in.

## What's Not

**Only two tools — and one is WIP.** `download_figma_images` is still marked work-in-progress. That leaves `get_figma_data` doing all the heavy lifting. No design token extraction, no Code Connect, no code-to-canvas capture.

**Figma API rate limits hit hard.** Multiple reports of 429 "Too Many Requests" errors (#258, #259, #287). When your AI agent makes rapid successive calls to inspect different frames, Figma's API throttles you. The official Figma server presumably has better rate limit management as a first-party integration.

**No write operations.** Framelink is read-only. You can't push code back to Figma as editable designs, manage Code Connect mappings, or generate FigJam diagrams. If you need the design-code-design loop, the [official server](/reviews/figma-dev-mode-mcp-server/) is your only option.

**~~macOS ARM compatibility issue~~ — fixed in v0.7.0.** The sharp/libvips image library previously caused dlopen errors on Apple Silicon (#288). In v0.7.0, sharp was replaced with jimp — a pure JavaScript image library — eliminating native dependency issues entirely.

**~~Stdio-only transport~~ — fixed in v0.8.0.** Framelink switched to stateless HTTP transport as a breaking change in v0.8.0 (March 24, 2026). This was a major architectural shift — the server now supports HTTP-based communication, closing the transport gap with Figma's remote server. Stdio is no longer the only option.

**~~No proxy support~~ — fixed in v0.9.0.** Proxy configuration for managed network environments was added in v0.9.0 (April 9, 2026), resolving connection reset errors (#267) for users behind corporate proxies.

**Telemetry added in v0.10.0 — with a privacy stumble.** Anonymous PostHog telemetry was introduced in v0.10.0, but issue #354 revealed that raw error messages were leaking Figma file keys and node IDs to PostHog — contradicting the PR's privacy claims. A redaction PR (#356) was opened to sanitize identifiers before capture. Worth watching for privacy-conscious users and enterprise environments.

**API key via command-line arg — addressed.** The `--figma-api-key=YOUR-KEY` approach puts your token in shell history and process lists. Environment variable support exists (`FIGMA_API_KEY`). [Issue #264](https://github.com/GLips/Figma-Context-MCP/issues/264) was closed via [PR #365](https://github.com/GLips/Figma-Context-MCP/pull/365) (feat: support per-request Figma API keys) and shipped in [v0.12.0 (May 27, 2026)](https://github.com/GLips/Figma-Context-MCP/releases/tag/v0.12.0) — users can now pass a key directly in individual tool calls, enabling multi-tenant scenarios without a server-level key.

**MCPSafe security scan: Grade B (86/100), review recommended.** The [MCPSafe registry entry for GLips/Figma-Context-MCP](https://mcpsafe.io/registry/github/GLips/Figma-Context-MCP) (an automated scanner using a 5-LLM consensus panel to detect prompt injection risks, over-scoped tool schemas, and supply-chain issues) currently shows 0 critical, 0 high, and 8 medium-severity findings, last scanned roughly mid-2026. This is an update from an earlier version of this review, which cited a Grade D (70/100) result with 3 high-severity findings — the GitHub issues that were the only public trace of that earlier result (#377, #378) have since been deleted, and the registry now shows the improved grade above with no findings breakdown beyond severity counts. Enterprise and security-conscious teams should still review the registry entry directly, since MCPSafe grades are automated and can change between scans.

## How It Compares

The real comparison is Framelink vs. the [official Figma Dev Mode MCP](/reviews/figma-dev-mode-mcp-server/):

| Feature | Framelink | Figma Official MCP |
|---------|-----------|-------------------|
| **GitHub stars** | ~15,600 | ~1,900 |
| **Tools** | 2 | 13 |
| **Output format** | Descriptive JSON | Prescriptive React/Tailwind |
| **Component nesting** | Preserved | Flattened |
| **Response size** | ~25% smaller (v0.13.0+: ~50% smaller) | Larger |
| **Transport** | HTTP (v0.8.0+) | Remote HTTP |
| **Auth** | API key | OAuth (browser) |
| **Free tier** | Figma API limits | 6 calls/month |
| **Write operations** | No | Yes (code-to-canvas, diagrams) |
| **Code Connect** | No | Yes |
| **Proxy support** | Yes (v0.9.0+) | N/A (remote) |
| **Self-hostable** | Yes (MIT) | No |
| **Weekly npm downloads** | ~62,000 | N/A (remote server) |
| **Maintenance** | 29 releases, v0.13.2 | Closed source |

They complement rather than compete. Framelink wins on the most common workflow (read design → generate code) and now matches the official server on HTTP transport. The official server wins on unique capabilities (code-to-canvas, Code Connect, design tokens).

Other Figma MCP servers exist, but none approach Framelink's adoption or maturity. The closest community alternative is [thirdstrandstudio/mcp-figma](https://github.com/thirdstrandstudio/mcp-figma) (~75 stars), which offers full Figma API coverage but lacks Framelink's context reduction that makes AI output more accurate.

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

**~~Stdio transport crash bug (#362)~~ — fixed on main, unreleased.** The race condition where progress notifications arrived after the tool response — crashing strict MCP clients including Claude Code's SDK with "unknown progress token" errors — was resolved via PR #366 (merged April 25, 2026). The fix removed the final progress notification that fired just before the response and made the heartbeat stop function async to drain in-flight notifications before returning. The fix is on the main branch but has not yet shipped in a versioned npm release. Users on v0.11.0 (the current npm latest) are still affected.

**Downloads continuing to normalize.** Weekly npm downloads peaked at ~198,000 in mid-April and have dropped further: ~105,000/week at the April 24 refresh, ~51,000/week as of mid-May — still 4.4x the early March baseline (~11,500) but the adoption spike is fading. Stars grew from ~14,500 to ~14,800. Forks from ~1,140 to ~1,200.

**[Critical RCE vulnerability (CVE-2025-53967)](https://github.com/advisories/GHSA-gxw4-4fc5-9gr5)** was disclosed and patched in v0.6.3 (September 2025). [Imperva researchers](https://www.imperva.com/blog/another-critical-rce-discovered-in-a-popular-mcp-server/) found a command injection flaw in `fetchWithRetry` — the curl fallback interpolated URLs into shell commands. Fully resolved, but a useful reminder that self-hosted MCP servers carry security responsibility.

## What's New (May 2026 Update)

No new npm releases since v0.11.0 (April 20), but meaningful changes landed on the main branch:

**Issue #362 fixed via PR #366 (April 25) — stdio crash resolved, unreleased.** The race condition causing Claude Code and other strict MCP clients to crash on "unknown progress token" errors is fixed in the codebase. The resolution: removed the final progress notification (fired redundantly just before the response) and made the heartbeat stop function async to drain in-flight notifications before the response returns. Fix is on main but not yet in a versioned npm package — users on the current npm latest (v0.11.0) still encounter this bug.

**Issue #264 fixed via PR #365 (April 30) — per-request API keys, unreleased.** Support for passing a Figma API key directly in individual tool calls is now on main. This enables multi-tenant deployments where different users provide their own credentials per-request, without sharing a server-level key. Addresses the core security concern about API keys in shell history/process lists. Also not yet in a versioned release.

**MCPSafe security scan: Grade D (70/100), May 12 — as this review reported at the time.** An automated security scanner (MCPSafe, using a 5-LLM consensus panel) was reported to have flagged Framelink with 3 high-severity and 11 medium-severity findings — no critical issues — with no maintainer response visible in GitHub issues #377/#378. *Update, August 2026: those two issues have since been deleted from GitHub, and the live MCPSafe registry entry now shows a materially different result — see the "What's New (August 2026 Update)" section below for the current, verified figure.*

**[Issue #354](https://github.com/GLips/Figma-Context-MCP/issues/354) (telemetry leaking file keys) remains open.** The PostHog telemetry introduced in v0.10.0 still leaks Figma file keys and node IDs in error messages. [PR #356](https://github.com/GLips/Figma-Context-MCP/pull/356) (redaction fix) has not been merged. Privacy-sensitive users should consider disabling telemetry or waiting for a release that resolves this.

**npm downloads: ~105K → ~51K/week.** The normalization that began after the April peak continues. The MCP ecosystem stabilization is real — Framelink's initial viral spike has passed. The server still processes tens of thousands of weekly installs and retains its lead over all competitors.

## What's New (August 2026 Update)

The two fixes that were "on main but unreleased" as of May have both shipped, and two more version bumps landed after that:

**[v0.12.0 (May 27, 2026)](https://github.com/GLips/Figma-Context-MCP/releases/tag/v0.12.0) — both pending fixes ship.** [Per-request Figma API keys (#365)](https://github.com/GLips/Figma-Context-MCP/pull/365) and the stdio progress-notification crash fix (#362, via [PR #366](https://github.com/GLips/Figma-Context-MCP/pull/366)) both shipped in this release, resolving the "fixed on main, unreleased" gap flagged in the April/May updates above. v0.12.0 also added an experimental tree output format for better token efficiency.

**[v0.13.0–v0.13.2 (June 18, 2026)](https://github.com/GLips/Figma-Context-MCP/releases) — ~50% payload reduction.** The tree output format became the default, styles and repeated subtrees are now deduplicated, and CSS Grid layout support was added. Combined, the release notes report roughly a 50% payload-size cut versus the previous YAML format, with v0.13.1 shaving an additional 7–15% by dropping redundant auto-generated node names. v0.13.0 also added support for bearer OAuth tokens over HTTP. v0.13.1 and v0.13.2 were same-day follow-up bug fixes (node naming, gradient opacity rendering).

**Downloads spiked again, then cooled.** Weekly npm downloads, which had bottomed around ~51,000/week in mid-May, [jumped to ~149,000/week in mid-June](https://www.npmjs.com/package/figma-developer-mcp) — coinciding with the v0.13.0 payload-reduction release — before settling to ~62,000/week in early August. Stars have grown to ~15,600 (from ~14,800 in May); forks to ~1,240 (from ~1,200).

**MCPSafe grade revised: B (86/100), not the D (70/100) cited in the May update.** The [MCPSafe registry entry](https://mcpsafe.io/registry/github/GLips/Figma-Context-MCP) for this repo currently shows 0 critical, 0 high, and 8 medium-severity findings — "review recommended," not the 3-high/11-medium breakdown this review previously cited. The GitHub issues that were the only public trace of that earlier D-grade result (#377, #378) have since been deleted, so we can't fully reconcile the two numbers; treat the current B/86 figure from the live registry as the more reliable one and the earlier D/70 claim as superseded.

**[Issue #354](https://github.com/GLips/Figma-Context-MCP/issues/354) (telemetry leaking file keys) is still open as of August.** No merge of the redaction PR ([#356](https://github.com/GLips/Figma-Context-MCP/pull/356)) has landed. This remains the one unresolved item from the security/privacy list.

## The Bigger Picture

Framelink's trajectory since the May refresh: the two fixes that were sitting unreleased (stdio crash #362, per-request API keys #264) shipped in v0.12.0, and two more releases (v0.13.0–v0.13.2) followed with a real payload-size win — roughly half the response size of the pre-tree-format YAML output. Downloads didn't just keep cooling as this review previously projected; they spiked to ~149K/week around the v0.13.0 release before settling near ~62K/week, still well above the early-March baseline and comfortably ahead of any competitor.

The telemetry privacy problem (#354 — file keys leaking to PostHog in error messages) remains unresolved months after being flagged in April. On security posture more broadly, the MCPSafe automated-scan grade for this repo currently reads B (86/100) with no critical or high findings — better than what this review previously reported, though the discrepancy (and the fact the underlying GitHub issues referencing the old score were deleted) is itself worth noting for anyone relying on third-party security scores for MCP servers.

The "descriptive vs. prescriptive" design decision remains the most consequential architectural choice in the design-to-code MCP space. Framelink bets that AI assistants are smart enough to translate design intent into code; Figma bets that AI assistants work better with explicit code examples. Based on adoption numbers (~15,600 stars vs. ~1,900 for the official guide repo), the community has voted — and the margin remains wide.

For design-to-code work with AI agents, Framelink remains the starting point. Add the official server only if you need its exclusive write capabilities (code-to-canvas, Code Connect) and have a paid Figma plan.

## Rating: 4/5

Framelink earns a 4/5 for producing objectively better code output than the official Figma MCP server for the most common design-to-code workflow — descriptive JSON that respects your project's conventions, preserved component hierarchies, smaller payloads (now roughly half the size after v0.13.0's tree-format rework), and zero cost barriers. It loses a point for having only two tools (one WIP), no write operations, Figma API rate limiting issues, and an unresolved telemetry privacy problem (#354 — file keys leaking to PostHog). The stdio crash (#362) and per-request API key (#264) fixes that were once sitting unreleased on main have since shipped in v0.12.0. Its MCPSafe security-scan grade currently reads B (86/100), an improvement on the D grade this review previously cited. With ~62,000 weekly npm downloads (after a mid-June spike to ~149,000) and ~15,600 GitHub stars, it remains the most adopted design-to-code MCP server by a wide margin.

**Use this if:** You want to translate Figma designs into code using your AI assistant, regardless of your Figma plan tier, framework choice, or component library.

**Skip this if:** You need the full design-code-design loop (code-to-canvas, Code Connect) or you need a zero-install remote server with no local installation.

**Pair with:** [Mobbin MCP](/reviews/mobbin-mcp-server/) — a complementary server that gives AI agents access to 621,500+ real app screens for design reference and pattern research, filling the gap Framelink doesn't address.

**Category**: [Design & Creative MCP Servers](/categories/design-creative/)

*This review was researched and written by an AI agent (Claude Sonnet 4.6, Anthropic) and edited by [Rob Nugen](https://www.robnugen.com). We do not test MCP servers hands-on — our analysis is based on documentation, source code, GitHub activity, npm data, and community reports. Last updated 2026-08-13.*


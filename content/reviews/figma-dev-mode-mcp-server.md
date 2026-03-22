---
title: "The Figma Dev Mode MCP Server — Design-to-Code Translation Through Your AI Assistant"
date: 2026-03-14T08:27:46+09:00
description: "Figma's official MCP server gives AI assistants direct access to design files, variables, Code Connect mappings, and code-to-canvas capture. 13 tools, OAuth authentication, remote-first architecture. Here's the honest review."
og_description: "Figma's official MCP server connects AI assistants to your design system — frames, variables, Code Connect, and code-to-canvas capture. 13 tools, OAuth, remote server at mcp.figma.com. Rating: 3.5/5."
content_type: "Review"
card_description: "Figma's first-party MCP server for AI-assisted design-to-code workflows. OAuth authentication, 13 tools covering code generation, design tokens, Code Connect, and code-to-canvas capture — all from a remote server at mcp.figma.com."
last_refreshed: 2026-03-14
---

**At a glance:** 443 GitHub stars (guide repo), 13 tools, OAuth, remote server at mcp.figma.com/mcp, code-to-canvas now in VS Code/Copilot + Cursor + Warp + more (expanded Q1 2026), PulseMCP 277K all-time visitors (#136 globally, ~17.3K weekly, #94 this week), Framelink competitor at 13.8K stars / 1.5M PulseMCP visitors (#27 globally)

The Figma Dev Mode MCP server is Figma's official tool for connecting AI coding assistants to design files. It's a hosted remote server at `mcp.figma.com/mcp` — no npm package to manage, no local process to run. Authenticate via OAuth, and your AI assistant can read Figma frames, extract design tokens, manage Code Connect mappings, and even capture live web pages back into Figma designs.

This is the design-to-code bridge that every frontend developer has been waiting for. Instead of manually inspecting Figma frames and translating visual properties into CSS, you paste a Figma URL and ask your AI assistant to build it. The server handles the translation layer.

The key question: does this actually produce better code than a developer reading the Figma file directly, and can you use it without a paid Figma plan?

## What It Does

The server exposes 13 tools split between read and write operations:

**Read operations (8 tools, rate-limited)**
- `get_design_context` — the core tool. Generates code from selected Figma frames. Defaults to React + Tailwind, but supports other frameworks (Vue, iOS, etc.)
- `get_variable_defs` — extracts design tokens: colors, spacing, typography as structured data
- `get_code_connect_map` — retrieves existing component-to-code mappings
- `get_code_connect_suggestions` — detects Figma components that could be mapped to code components
- `get_screenshot` — gets a visual reference image of a frame
- `get_metadata` — returns XML representation of node/layer structure
- `get_figjam` — extracts FigJam diagram metadata
- `whoami` — returns authenticated user identity, seat type, and plan info

**Write operations (5 tools)**
- `add_code_connect_map` — creates new design-to-code component mappings
- `send_code_connect_mappings` — finalizes and publishes mappings
- `generate_figma_design` — captures live web pages and converts them to editable Figma frames (rate-limit exempt)
- `generate_diagram` — creates FigJam diagrams from Mermaid syntax
- `create_design_system_rules` — *new* — creates rule files that give agents framework-specific context for translating designs into code

The standout feature is `generate_figma_design` — code-to-canvas capture. No community MCP server can do this. You build something in code, and this tool pushes it back into Figma as an editable design. It closes the loop that every other design tool leaves open.

## Setup

Like [Vercel](/reviews/vercel-mcp-server/) and [Supabase](/reviews/supabase-mcp-server/), this is a zero-install remote server:

**VS Code (requires GitHub Copilot):**

Cmd+Shift+P → "MCP: Add Server" → HTTP → paste `https://mcp.figma.com/mcp`

**Cursor:**

```
/add-plugin figma
```

Or manually:

```json
{
  "mcpServers": {
    "figma": {
      "url": "https://mcp.figma.com/mcp"
    }
  }
}
```

**Claude Code:**

```bash
claude mcp add --transport http figma https://mcp.figma.com/mcp
```

First connection opens a browser for OAuth consent. You select your Figma team, approve access, and you're connected. Figma also offers a Desktop MCP Server option that runs through the Figma desktop application for local connectivity.

## What's Good

**Code-to-canvas is genuinely unique — and expanding fast.** The `generate_figma_design` tool captures live web UI and converts it to editable Figma frames. Originally a Claude Code exclusive, Figma expanded code-to-canvas to VS Code (via GitHub Copilot) on March 6, 2026, and now supports Cursor, Warp, Factory, Firebender, and Augment. OpenAI Codex integration launched February 25, 2026, with a bidirectional MCP server. No community server can match this — it's a capability only the platform owner can provide.

**Code Connect integration solves the "which component?" problem.** Instead of the AI guessing how to implement a Figma component, Code Connect maps it directly to your existing codebase component. `get_code_connect_suggestions` finds unmapped components, and `add_code_connect_map` creates the mapping. Over time, this makes code generation increasingly accurate to your actual design system.

**Design token extraction is immediate.** `get_variable_defs` pulls colors, spacing, and typography as structured data — no manual inspection needed. For design system maintenance, this is faster than the Figma UI.

**Zero-install remote architecture.** Same model as Vercel, Neon, and Supabase: one URL, OAuth, automatic updates. No version management, no npm dependencies, no local process to babysit.

**Design system rules bridge the framework gap.** The new `create_design_system_rules` tool lets teams create rule files with framework-specific context, so agents know how to translate designs for your particular stack. Available on Organization and Enterprise plans, this addresses one of the server's biggest weaknesses — prescriptive React/Tailwind output that doesn't match your codebase.

**Write operations bypass rate limits.** `generate_figma_design` and `add_code_connect_map` are exempt from the rate limits that restrict read operations. This means the server's most unique features are also its most accessible.

## What's Not

**Free tier rate limits are crippling.** Starter, View, and Collab seats get **6 tool calls per month**. Not per day — per month. That's barely enough to test the server, let alone use it for real work. Paid plans help, but the caps vary: Professional and Organization get 200 calls/day (15-20/min), Enterprise gets 600 calls/day. Dev seats start at $12/month (annual) and Full seats at $15/month on the Professional plan. Meaningful use requires a paid Figma plan with Dev or Full seats.

**Prescriptive output can poison your context.** The `get_design_context` tool generates opinionated React + Tailwind code by default. If your codebase uses Vue, Svelte, or a different styling approach, the generated code introduces conventions that don't match your project. The community [Framelink](https://github.com/GLips/Figma-Context-MCP) server takes a different approach — it outputs descriptive JSON and lets your AI assistant generate code that matches your existing patterns.

**Nested components get flattened.** The server loses component hierarchy when translating designs. A card component containing a button component comes through as a flat structure rather than preserving the nesting. This can mislead the AI into generating monolithic components instead of composing from your existing component library.

**No self-hosting option.** The server runs on Figma's infrastructure. You can't inspect the source code, self-host, or audit what data flows through it. The community Framelink server is MIT-licensed and fully inspectable.

**OAuth requires a browser.** Same limitation we've flagged in [Vercel](/reviews/vercel-mcp-server/), [Neon](/reviews/neon-mcp-server/), and [Supabase](/reviews/supabase-mcp-server/) — headless environments, CI/CD pipelines, and remote servers can't authenticate. No API key fallback.

**Response sizes can be large.** The docs warn to break large selections into smaller components. Oversized selections cause errors or incomplete responses. The community Framelink server produces ~25% smaller payloads by using descriptive JSON instead of prescriptive code.

## How It Compares

The Figma design-to-code space is crowded — GitHub has 221+ Figma MCP repos. The real comparison is official vs. Framelink:

| Feature | Figma Official MCP | Framelink (community) |
|---------|-------------------|----------------------|
| **Maintainer** | Figma | GLips (community) |
| **GitHub stars** | 443 (guide repo) | 13,800 |
| **PulseMCP visitors** | 277K all-time (#136) | 1.5M all-time (#27) |
| **Transport** | Remote HTTP (Streamable) | Stdio (npx) |
| **Auth** | OAuth (browser) | API key (CLI arg) |
| **Tools** | 13 | 6 |
| **npm downloads** | N/A (remote server) | ~11,600/week |
| **Output format** | Prescriptive (React/Tailwind) | Descriptive JSON |
| **Component nesting** | Flattened | Preserved |
| **Response size** | Larger | ~25% smaller |
| **Write operations** | Yes (code-to-canvas, diagrams) | No |
| **Code Connect** | Yes | No |
| **Design system rules** | Yes (Org/Enterprise) | No |
| **Rate limits (free)** | 6/month | Figma API limits only |
| **Self-hostable** | No | Yes (MIT) |
| **Security track record** | Closed-source (Figma-hosted) | CVE-2025-15061 RCE (patched v0.6.3) |

The community server has 31x the GitHub stars and 5.4x the PulseMCP traffic, and arguably produces better code output for pure design-to-code workflows. But the official server has exclusive capabilities: code-to-canvas capture across 7+ IDE clients, Code Connect management, design system rules, FigJam diagram generation, and OAuth without API key management.

**Recommendation:** If you just need to translate designs to code, Framelink is the better tool — descriptive output, smaller payloads, accurate component nesting, and no seat-type rate limits. If you need the full design-code-design loop (especially code-to-canvas and Code Connect), the official server is the only option, and it requires a paid Figma plan. Note that Framelink had a critical RCE vulnerability (CVE-2025-15061) — now patched in v0.6.3 and later — which highlights the security tradeoff of self-hosted servers vs. Figma's managed infrastructure.

## What's New (March 2026 Update)

**Code-to-canvas breaks out of Claude Code.** The `generate_figma_design` tool — originally a Claude Code exclusive — expanded to VS Code via GitHub Copilot (March 6, 2026), and now works in Cursor, Warp, Factory, Firebender, and Augment. OpenAI's Codex integration launched February 25, 2026, with a bidirectional MCP server. This is the fastest expansion of any MCP server's client support we've tracked.

**New tool: `create_design_system_rules`.** Teams on Organization and Enterprise plans can now create rule files with framework-specific instructions, so agents know how to translate designs for Vue, Svelte, or any other stack. This partially addresses the prescriptive React/Tailwind output criticism.

**Code Connect gets multi-framework support.** You can now attach multiple code files to a single Figma component and see code previews across different frameworks (requires GitHub connection). This makes Code Connect useful for design systems that target multiple platforms.

**Rate limits clarified.** Figma published explicit daily and per-minute caps: Professional and Organization get 200 calls/day (15-20 calls/min), Enterprise gets 600 calls/day. Free tier remains at 6/month. `generate_figma_design`, `add_code_connect_map`, and `whoami` are rate-limit exempt.

**Framelink keeps pace.** The community competitor shipped v0.7.1 (March 20, 2026) with 13.8K GitHub stars, ~11,600 weekly npm downloads, and 1.5M PulseMCP all-time visitors (#27 globally). A critical RCE vulnerability (CVE-2025-15061) was discovered and patched in v0.6.3 — a reminder that self-hosted servers carry security responsibility that managed services don't.

**AI Credits pay-as-you-go.** Organization and Enterprise plans now have pay-as-you-go billing for AI credits, with Professional plans getting the option in May 2026.

## The Bigger Picture

The Figma MCP server tells an interesting story about the official-vs-community dynamic in the MCP ecosystem. The community Framelink server launched first, accumulated 13,800 stars, and optimized for the most common use case: reading designs and generating code. Figma's official server launched later with fewer stars but unique write capabilities that only the platform owner can provide.

Q1 2026 shifted the balance. Figma's aggressive expansion of code-to-canvas support across 7+ IDE clients — and the OpenAI Codex partnership — shows the platform leveraging its unique position as the design system of record. Community servers can read from Figma, but only Figma can write back to the canvas. That moat is widening.

Meanwhile, Framelink's RCE vulnerability (CVE-2025-15061) illustrates the security tradeoff in this space. Self-hosted MIT-licensed servers offer transparency and flexibility, but they also put the security burden on users. Figma's managed infrastructure handles that silently. For enterprise teams, this is an increasingly important consideration.

The 6-calls-per-month free tier limit remains the most aggressive gating we've seen on any MCP server. Even [Neon](/reviews/neon-mcp-server/)'s free tier gives you 100 projects and meaningful API access. Figma is clearly positioning MCP as a paid feature, which may slow grassroots adoption — but the code-to-canvas expansion suggests Figma is betting on enterprise and team workflows rather than individual developers.

## Rating: 3.5/5

The Figma Dev Mode MCP server earns a 3.5/5 for delivering unique write capabilities (code-to-canvas across 7+ IDE clients, Code Connect, design system rules, FigJam diagrams) that no community server can match, wrapped in a clean remote-first OAuth architecture. The Q1 2026 expansion — code-to-canvas in VS Code/Copilot, OpenAI Codex integration, and the new `create_design_system_rules` tool — shows genuine momentum. It still loses points for a crippling free tier (6 calls/month), prescriptive output defaults, flattened component hierarchies, no self-hosting option, and the fact that the community Framelink server with 13,800 stars and 5.4x the PulseMCP traffic produces better output for pure design-to-code workflows. A paid Figma plan ($12-15/month minimum for a Dev or Full seat) is effectively required for real use.

**Use this if:** You have a paid Figma plan and want the full design-code-design loop — especially Code Connect for mapping components, code-to-canvas for keeping designs in sync with implementations, and design system rules for multi-framework support.

**Skip this if:** You're on Figma's free tier (6 calls/month is unusable), you just need design-to-code translation (use Framelink instead), or you need self-hosted/auditable infrastructure.

*This review is maintained by an AI research process (Claude Opus 4.6, Anthropic). We research publicly available data — GitHub, npm, PulseMCP, official docs — but have not tested this server hands-on. The project is operated by [Rob Nugen](https://robnugen.com). Last updated: 2026-03-21.*

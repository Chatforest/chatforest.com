---
title: "The Figma Dev Mode MCP Server — Design-to-Code Translation Through Your AI Assistant"
date: 2026-03-14T08:27:46+09:00
description: "Figma's official MCP server gives AI assistants direct access to design files, variables, Code Connect mappings, and code-to-canvas capture."
og_description: "Figma's official MCP server connects AI assistants to your design system — frames, variables, Code Connect, and code-to-canvas capture. 24 tools, OAuth, remote server at mcp.figma.com. Rating: 3.5/5."
content_type: "Review"
card_description: "Figma's first-party MCP server for AI-assisted design-to-code workflows. OAuth authentication, 24 tools covering code generation, design tokens, Code Connect, shader/motion data, and code-to-canvas capture — all from a remote server at mcp.figma.com. 1,884 GitHub stars."
last_refreshed: 2026-08-13
sources_audited: 2026-08-13
---

**At a glance:** [1,884 GitHub stars](https://github.com/figma/mcp-server-guide) (guide repo), [24 tools](https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/), OAuth, remote server at mcp.figma.com/mcp, code-to-canvas now in VS Code/Copilot + Cursor + Warp + more (expanded Q1 2026), [PulseMCP 2.5M all-time visitors (#38 globally, ~117K weekly, #23 this week)](https://www.pulsemcp.com/servers/figma), [Framelink](https://github.com/GLips/Figma-Context-MCP) competitor at 15.6K stars / [3.3M PulseMCP visitors (#29 globally)](https://www.pulsemcp.com/servers/glips-figma-context)

The Figma Dev Mode MCP server is [Figma's official tool](https://developers.figma.com/docs/figma-mcp-server/) for connecting AI coding assistants to design files. It's a hosted remote server at `mcp.figma.com/mcp` — no npm package to manage, no local process to run. Authenticate via OAuth, and your AI assistant can read Figma frames, extract design tokens, manage Code Connect mappings, and even capture live web pages back into Figma designs.

This is the design-to-code bridge that every frontend developer has been waiting for. Instead of manually inspecting Figma frames and translating visual properties into CSS, you paste a Figma URL and ask your AI assistant to build it. The server handles the translation layer.

The key question: does this actually produce better code than a developer reading the Figma file directly, and can you use it without a paid Figma plan?

## What It Does

The server's tool surface has grown substantially since launch. As of this writing it exposes [24 tools](https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/) (up from 13 at last review), split between read and write operations, plus one MCP prompt:

**Read operations (rate-limited unless noted)**
- `get_design_context` — the core tool. Generates code from selected Figma frames. Defaults to React + Tailwind, but supports other frameworks (Vue, iOS, etc.)
- `get_variable_defs` — extracts design tokens: colors, spacing, typography as structured data
- `get_code_connect_map` — retrieves existing component-to-code mappings
- `get_code_connect_suggestions` — detects Figma components that could be mapped to code components
- `get_context_for_code_connect` — Figma-prompted tool call that gathers context for generating Code Connect templates
- `get_screenshot` — gets a visual reference image of a frame
- `get_metadata` — returns XML representation of node/layer structure
- `get_figjam` — converts FigJam diagrams to XML
- `get_libraries` — returns libraries added to or available for a file (remote only)
- `get_motion_context` — returns keyframe animation data (tracks, easing, CSS/motion.dev snippets) for an animated selection
- `get_shader_effect` / `get_shader_fill` and `list_shader_effects` / `list_shader_fills` — retrieve and list shader assets from the authenticated account's library
- `search_design_system` — searches design libraries for matching components, variables, and styles (remote only)
- `whoami` — returns authenticated user identity, seat type, and plan info (**rate-limit exempt**)

**Write operations**
- `add_code_connect_map` — creates new design-to-code component mappings (rate-limit exempt)
- `send_code_connect_mappings` — finalizes and publishes mappings
- `generate_figma_design` — captures live web pages and converts them to editable Figma frames (rate-limit exempt)
- `generate_diagram` — creates FigJam diagrams; updated April 28, 2026 to also generate architecture diagrams and ERDs directly, not just from Mermaid syntax (remote server only)
- `create_new_file` — creates a new blank Figma Design, FigJam, or Slides file in the user's drafts (remote only)
- `download_assets` / `upload_assets` — download rendered exports/source images from a file, or upload supported image assets to one (remote only)
- `use_figma` — a general-purpose tool for creating, editing, or inspecting any object in a Figma file, across Design, FigJam, and Slides (remote only)

Figma's docs also list `create_design_system_rules` as an [MCP **prompt**](https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/), not a counted tool — it creates rule files that give agents framework-specific context for translating designs into code.

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

**Code-to-canvas is genuinely unique — and expanding fast.** The `generate_figma_design` tool captures live web UI and converts it to editable Figma frames. Originally a Claude Code exclusive, Figma [expanded code-to-canvas to VS Code (via GitHub Copilot)](https://github.blog/changelog/2026-03-06-figma-mcp-server-can-now-generate-design-layers-from-vs-code/) on March 6, 2026, and now supports Cursor, Warp, Factory, Firebender, and Augment. [OpenAI Codex integration](https://openai.com/index/figma-partnership/) launched February 26, 2026, with a bidirectional MCP server. No community server can match this — it's a capability only the platform owner can provide.

**Code Connect integration solves the "which component?" problem.** Instead of the AI guessing how to implement a Figma component, Code Connect maps it directly to your existing codebase component. `get_code_connect_suggestions` finds unmapped components, and `add_code_connect_map` creates the mapping. Over time, this makes code generation increasingly accurate to your actual design system.

**Design token extraction is immediate.** `get_variable_defs` pulls colors, spacing, and typography as structured data — no manual inspection needed. For design system maintenance, this is faster than the Figma UI.

**Zero-install remote architecture.** Same model as Vercel, Neon, and Supabase: one URL, OAuth, automatic updates. No version management, no npm dependencies, no local process to babysit.

**Design system rules bridge the framework gap.** The `create_design_system_rules` prompt lets teams create rule files with framework-specific context, so agents know how to translate designs for your particular stack. Available on Organization and Enterprise plans, this addresses one of the server's biggest weaknesses — prescriptive React/Tailwind output that doesn't match your codebase.

**Some operations bypass rate limits.** `generate_figma_design`, `add_code_connect_map`, and `whoami` are exempt from the rate limits that restrict most read operations, per [Figma's rate-limits documentation](https://developers.figma.com/docs/figma-mcp-server/rate-limits-access/). This means the server's most unique features are also its most accessible.

## What's Not

**Free tier rate limits are severe.** Per [Figma's rate-limits documentation](https://developers.figma.com/docs/figma-mcp-server/rate-limits-access/), the free **Starter** plan is capped at **20 tool calls per month** for any seat type. Not per day — per month. That's barely enough to test the server, let alone use it for real work. On paid plans, View/Collab seats are capped even lower, at 6 calls/month, while Dev/Full seats get much higher limits: Professional gets 200 calls/day (10/min), Organization gets 200 calls/day (15/min), and Enterprise gets 600 calls/day (20/min). Dev seats [start at $12/month (annual) and Full seats at $16/month](https://www.figma.com/pricing/) on the Professional plan. Meaningful use requires a paid Figma plan with a Dev or Full seat.

**Prescriptive output can poison your context.** The `get_design_context` tool generates opinionated React + Tailwind code by default. If your codebase uses Vue, Svelte, or a different styling approach, the generated code introduces conventions that don't match your project. The community [Framelink](https://github.com/GLips/Figma-Context-MCP) server (15.6K stars) takes a different approach — it outputs descriptive JSON and lets your AI assistant generate code that matches your existing patterns.

**Nested components get flattened.** The server loses component hierarchy when translating designs. A card component containing a button component comes through as a flat structure rather than preserving the nesting. This can mislead the AI into generating monolithic components instead of composing from your existing component library.

**No self-hosting option.** The server runs on Figma's infrastructure. You can't inspect the source code, self-host, or audit what data flows through it. The community [Framelink server](https://github.com/GLips/Figma-Context-MCP) is MIT-licensed and fully inspectable.

**OAuth requires a browser.** Same limitation we've flagged in [Vercel](/reviews/vercel-mcp-server/), [Neon](/reviews/neon-mcp-server/), and [Supabase](/reviews/supabase-mcp-server/) — headless environments, CI/CD pipelines, and remote servers can't authenticate. No API key fallback.

**Response sizes can be large.** The docs warn to break large selections into smaller components. Oversized selections cause errors or incomplete responses. The community Framelink server produces ~25% smaller payloads by using descriptive JSON instead of prescriptive code.

## How It Compares

The Figma design-to-code space is crowded with community servers. The real comparison is official vs. Framelink:

| Feature | Figma Official MCP | Framelink (community) |
|---------|-------------------|----------------------|
| **Maintainer** | Figma | GLips (community) |
| **GitHub stars** | [1,884](https://github.com/figma/mcp-server-guide) (guide repo) | [15,646](https://github.com/GLips/Figma-Context-MCP) |
| **PulseMCP visitors** | [2.5M all-time (#38)](https://www.pulsemcp.com/servers/figma) | [3.3M all-time (#29)](https://www.pulsemcp.com/servers/glips-figma-context) |
| **Transport** | Remote HTTP (Streamable) | Stdio (npx) |
| **Auth** | OAuth (browser) | API key (CLI arg) |
| **Tools** | [24](https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/) | 6 |
| **npm downloads** | N/A (remote server) | [~95K/week](https://www.npmjs.com/package/figma-developer-mcp) |
| **Output format** | Prescriptive (React/Tailwind) | Descriptive JSON |
| **Component nesting** | Flattened | Preserved |
| **Response size** | Larger | ~25% smaller |
| **Write operations** | Yes (code-to-canvas, diagrams) | No |
| **Code Connect** | Yes | No |
| **Design system rules** | Yes (Org/Enterprise) | No |
| **Rate limits (free)** | [20/month](https://developers.figma.com/docs/figma-mcp-server/rate-limits-access/) (Starter plan) | Figma API limits only |
| **Self-hostable** | No | Yes (MIT) |
| **Security track record** | Closed-source (Figma-hosted) | [CVE-2025-15061](https://github.com/advisories/GHSA-8675-cg27-5c39) RCE (patched v0.6.3) |

The community server still has more GitHub stars (~8.3x) and somewhat more PulseMCP traffic (~1.3x), though the gap in both has narrowed sharply since our last review as Figma's official server has grown fast. Framelink arguably still produces better code output for pure design-to-code workflows. But the official server has exclusive capabilities: code-to-canvas capture across 7+ IDE clients, Code Connect management, design system rules, FigJam diagram generation, and OAuth without API key management.

**Recommendation:** If you just need to translate designs to code, Framelink is the better tool — descriptive output, smaller payloads, accurate component nesting, and no seat-type rate limits. If you need the full design-code-design loop (especially code-to-canvas and Code Connect), the official server is the only option, and it requires a paid Figma plan. Note that Framelink had a critical RCE vulnerability (CVE-2025-15061) — now patched in v0.6.3 and later — which highlights the security tradeoff of self-hosted servers vs. Figma's managed infrastructure.

## What's New

**Code-to-canvas breaks out of Claude Code.** The `generate_figma_design` tool — originally a Claude Code exclusive — [expanded to VS Code via GitHub Copilot](https://github.blog/changelog/2026-03-06-figma-mcp-server-can-now-generate-design-layers-from-vs-code/) (March 6, 2026), and now works in Cursor, Warp, Factory, Firebender, and Augment. [OpenAI's Codex integration](https://openai.com/index/figma-partnership/) launched February 26, 2026, with a bidirectional MCP server. This is the fastest expansion of any MCP server's client support we've tracked.

**New prompt: [`create_design_system_rules`](https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/).** Teams on Organization and Enterprise plans can now create rule files with framework-specific instructions, so agents know how to translate designs for Vue, Svelte, or any other stack. This partially addresses the prescriptive React/Tailwind output criticism.

**[Code Connect](https://developers.figma.com/docs/code-connect/) gets multi-framework support.** You can now attach multiple code files to a single Figma component and see code previews across different frameworks (requires GitHub connection). This makes Code Connect useful for design systems that target multiple platforms.

**[Rate limits clarified](https://developers.figma.com/docs/figma-mcp-server/plans-access-and-permissions/).** Figma publishes explicit daily and per-minute caps: Professional gets [200 calls/day (10/min)](https://developers.figma.com/docs/figma-mcp-server/rate-limits-access/), Organization gets 200 calls/day (15/min), Enterprise gets 600 calls/day (20/min). The free Starter tier is capped at 20 calls/month for any seat type; View/Collab seats on paid plans are capped lower, at 6/month. `generate_figma_design`, `add_code_connect_map`, and `whoami` are rate-limit exempt.

**Framelink accelerates.** The community competitor has continued shipping — it's now at [v0.13.2](https://github.com/GLips/Figma-Context-MCP/releases) with [15.6K GitHub stars](https://github.com/GLips/Figma-Context-MCP), [~95K weekly npm downloads](https://www.npmjs.com/package/figma-developer-mcp), and 3.3M PulseMCP all-time visitors (#29 globally). A critical [RCE vulnerability (CVE-2025-15061)](https://github.com/advisories/GHSA-8675-cg27-5c39) was discovered and patched in v0.6.3 — a reminder that self-hosted servers carry security responsibility that managed services don't.

**[AI Credits pay-as-you-go](https://help.figma.com/hc/en-us/articles/35865276858647-Manage-AI-credits).** Organization, Enterprise, and now Professional plan admins can enable pay-as-you-go billing for AI credits beyond their subscription allotment, currently priced at $0.03/credit.

**[FigJam Skills expand agent-driven diagramming (April 28, 2026)](https://www.figma.com/blog/figjam-your-coding-agents-whiteboard/).** The `generate_diagram` tool was extended to generate [architecture diagrams and Entity Relationship Diagrams (ERDs) directly](https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/), not just Mermaid-syntax diagrams (remote server only). Alongside it, new FigJam-focused skills launched, including `figma-use-figjam` (lets agents read from and write to any FigJam board) and `generate-project-plan` (converts docs, tickets, or codebases into structured visual FigJam project boards). Previously, FigJam diagram generation required Mermaid syntax — agents can now ask for architecture or ER diagrams in natural language.

## The Bigger Picture

The Figma MCP server tells an interesting story about the official-vs-community dynamic in the MCP ecosystem. The community Framelink server launched first, built a large following (now [15,646 GitHub stars](https://github.com/GLips/Figma-Context-MCP)), and optimized for the most common use case: reading designs and generating code. Figma's official server launched later with fewer stars but unique write capabilities that only the platform owner can provide.

Q1–Q2 2026 shifted the balance. Figma's aggressive expansion of code-to-canvas support across 7+ IDE clients, the OpenAI Codex partnership, and the April 28 FigJam Skills launch show the platform leveraging its unique position as the design system of record. Community servers can read from Figma, but only Figma can write back to the canvas — whether that's capturing live UI, creating Code Connect mappings, or generating architecture diagrams in FigJam. That moat is widening.

Meanwhile, Framelink's [RCE vulnerability (CVE-2025-15061)](https://github.com/advisories/GHSA-8675-cg27-5c39) illustrates the security tradeoff in this space. Self-hosted MIT-licensed servers offer transparency and flexibility, but they also put the security burden on users. Figma's managed infrastructure handles that silently. For enterprise teams, this is an increasingly important consideration.

The [20-calls-per-month free (Starter) tier limit](https://developers.figma.com/docs/figma-mcp-server/rate-limits-access/) remains among the most aggressive gating we've seen on any MCP server. Even [Neon](/reviews/neon-mcp-server/)'s free tier gives you 100 projects and meaningful API access. Figma is clearly positioning MCP as a paid feature, which may slow grassroots adoption — but the code-to-canvas expansion suggests Figma is betting on enterprise and team workflows rather than individual developers.

## Rating: 3.5/5

The Figma Dev Mode MCP server earns a 3.5/5 for delivering unique write capabilities (code-to-canvas across 7+ IDE clients, Code Connect, design system rules, FigJam diagrams) that no community server can match, wrapped in a clean remote-first OAuth architecture. The Q1 2026 expansion — code-to-canvas in VS Code/Copilot, OpenAI Codex integration, and the new `create_design_system_rules` prompt — shows genuine momentum. It still loses points for a punishing free tier (20 calls/month on Starter, and just 6/month for View/Collab seats on paid plans), prescriptive output defaults, flattened component hierarchies, no self-hosting option, and the fact that the community [Framelink server](https://github.com/GLips/Figma-Context-MCP), now at 15,646 stars and still ahead on PulseMCP traffic, produces better output for pure design-to-code workflows. A paid Figma plan ($12-16/month minimum for a Dev or Full seat) is effectively required for real use.

**Use this if:** You have a paid Figma plan and want the full design-code-design loop — especially Code Connect for mapping components, code-to-canvas for keeping designs in sync with implementations, and design system rules for multi-framework support.

**Skip this if:** You're on Figma's free Starter tier (20 calls/month is barely enough to test it), you just need design-to-code translation (use Framelink instead), or you need self-hosted/auditable infrastructure.

**Category**: [Design & Creative MCP Servers](/categories/design-creative/)

*This review is maintained by an AI research process (Claude Opus 4.6, Anthropic). We research publicly available data — GitHub, npm, PulseMCP, official docs — but have not tested this server hands-on. The project is operated by [Rob Nugen](https://robnugen.com). Last updated: 2026-08-13.*

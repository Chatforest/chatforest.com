---
title: "The Browserbase MCP Server — Cloud Browser Automation With AI-Native Targeting"
date: 2026-03-14T10:35:00+09:00
description: "Browserbase's official MCP server gives AI agents cloud-hosted browser sessions powered by Stagehand's natural language targeting. 8 tools, stealth mode, session management. Here's the honest review."
og_description: "Browserbase's MCP server gives agents cloud browsers with AI-native element targeting via Stagehand. 3.3K stars, v3.0.0 with 6 tools, cloud-only, paid service. Rating: 3.5/5."
content_type: "Review"
card_description: "The official Browserbase MCP server for cloud browser automation. 6 tools (v3.0.0) using Stagehand's natural language element targeting — navigate, act, extract, observe, and session management. Cloud-hosted with stealth mode and Model Gateway."
last_refreshed: 2026-04-17
categories: ["/categories/web-search-scraping/"]
---

**At a glance:** 3.3K GitHub stars · 349 forks · 6 tools via Stagehand v3 (v3.0.0 released March 31) · 27 open issues · 198 commits · [PulseMCP](https://pulsemcp.com/servers/browserbase-mcp-server): #56 globally, ~21.6K weekly visitors

Browserbase takes a different approach to browser automation MCP servers. Where [Playwright MCP](/reviews/playwright-mcp-server/) runs a local browser and targets elements via accessibility trees, and [Puppeteer MCP](/reviews/puppeteer-mcp-server/) uses CSS selectors, Browserbase moves the browser to the cloud and targets elements with natural language via Stagehand — their AI-powered automation framework.

The pitch is compelling: your agent connects to a managed browser instance running on Browserbase's infrastructure. No local Chrome processes eating RAM. No headless browser configuration. Anti-bot stealth mode built in. Session recording for debugging. And Stagehand's "act on this page" approach means agents describe what they want to do in plain English instead of crafting selectors.

With 3,300 GitHub stars, 349 forks, and backing from a well-funded startup, this is the most established cloud browser MCP server. The March 2026 v3.0.0 release brought breaking changes — simplified tool names, fewer tools, and a new default model — signaling a shift toward their hosted MCP endpoint. But cloud-only means a paid service with ongoing costs, and the MCP server still has rough edges that matter.

## What It Does

Since v3.0.0 (March 31, 2026), the server exposes 6 tools with simplified names:

**Navigation & interaction:**
- **`navigate`** — Navigate to any URL.
- **`act`** — Perform actions using natural language instructions (e.g., "click the login button", "fill in the email field with test@example.com"). This is the flagship tool — Stagehand uses an LLM to identify the right element and act on it.
- **`observe`** — Find actionable elements on the page with natural language descriptions. Returns what's available to interact with.

**Data extraction:**
- **`extract`** — Pull text content from the current page, filtering out CSS and JavaScript. The `instruction` parameter is now optional.

**Session management:**
- **`start`** — Create a cloud browser session with a fully initialized Stagehand instance.
- **`end`** — Terminate the session, disconnect the browser, and clean up.

That's 6 tools, down from 8 in v2. The v3.0.0 release removed `browserbase_screenshot` and `browserbase_stagehand_get_url`, and renamed all remaining tools to shorter forms. For comparison, Playwright MCP has 25+ and Puppeteer has 7. But the tools work differently — `act` replaces many individual tools (click, type, select, hover) with a single natural language instruction.

**Breaking change note:** If you were using v2.x, all tool names changed and the screenshot tool is gone. The `act` tool no longer accepts a `variables` parameter, and `start` no longer accepts `sessionId`.

## Setup

Add this to your MCP client config:

```json
{
  "mcpServers": {
    "browserbase": {
      "command": "npx",
      "args": ["@browserbasehq/mcp-server-browserbase"],
      "env": {
        "BROWSERBASE_API_KEY": "your-api-key",
        "BROWSERBASE_PROJECT_ID": "your-project-id",
        "GEMINI_API_KEY": "your-gemini-key"
      }
    }
  }
}
```

Previously, three API keys were required. Since the April 2026 Model Gateway launch, you can use just your Browserbase API key for model access too — Browserbase routes LLM calls to your chosen model (GPT-5, Claude Sonnet 4.6, Gemini 3 Flash Preview) at market-rate pricing with no markup. Alternatively, you can still provide your own model API key directly. The default model is now Gemini 2.5 Flash Lite (changed from Gemini 2.0 Flash in v3.0.0).

**Configuration flags** (local server only):
- `--proxies` — Enable Browserbase proxies for anti-bot bypass.
- `--advancedStealth` — Advanced stealth mode (Scale Plan only).
- `--keepAlive` — Maintain persistent sessions across requests.
- `--contextId <id>` — Reuse a specific browser context.
- `--persist` — Persist browser context (default: true).
- `--browserWidth` / `--browserHeight` — Set viewport dimensions (default: 1024x768).
- `--experimental` — Enable experimental features.

**Transport options:** stdio (local) and Streamable HTTP (remote). Browserbase recommends the remote SHTTP transport for "full capacity" use.

**Docker support:** Available via `docker build -t mcp-browserbase .` or the official Docker Hub image.

**Setup difficulty: Moderate.** The npx command is simple, and the Model Gateway reduces API key friction — you now only need a Browserbase API key and project ID to get started (down from three keys). Still a higher barrier than Playwright (zero config) or Puppeteer (zero config) since you're signing up for a cloud service before you can test a single page.

## What Works Well

**Natural language targeting is genuinely easier to use.** Instead of the agent figuring out CSS selectors or accessibility tree references, it says "click the Sign In button" or "fill the search box with 'MCP servers'". Stagehand handles the element identification. For agents, this is more intuitive than any selector-based approach — though it comes with trade-offs (see below).

**Cloud browsers solve real infrastructure problems.** If you're running agents in production that need to automate browsers, managing local Chrome processes doesn't scale. Browserbase handles the browser lifecycle, session isolation, and resource management. Sessions are recorded for debugging. You get infrastructure without maintaining infrastructure.

**Anti-bot stealth is built in.** Browserbase browsers come with fingerprint management, proxy support, and stealth mode that help bypass bot detection. With Playwright or Puppeteer running locally, you're on your own for anti-bot measures. This matters for production scraping and automation tasks.

**Stagehand v3 performance improvements are real.** The 20-40% speed improvement over v2 through automatic caching, enhanced iframe/shadow root extraction, and improved schemas makes a noticeable difference in multi-step workflows. The February 2026 caching update goes further — automatic caching of repeated actions eliminates redundant LLM calls, reportedly delivering up to 2x faster execution and ~30% cost reduction on repeat workflows.

**The platform is evolving fast.** In Q1 2026 alone, Browserbase shipped: a Fetch API for lightweight page content retrieval without a full browser session (~$1/1K pages), Browserbase Search powered by Exa (1,000 free searches/month per plan), Browserbase Functions for deploying agents directly to their infrastructure (up to 70% latency reduction), and a Vercel Marketplace integration. The free plan now supports 3 concurrent browsers (up from 1). The hosted MCP server migrated to Browserbase-managed infrastructure for better reliability on longer sessions.

**Model Gateway eliminates API key juggling.** Since April 2026, Browserbase's Model Gateway lets you use GPT-5, Claude Sonnet 4.6, or Gemini 3 Flash Preview through a single Browserbase API key. No separate model provider accounts needed. Market-rate pricing with no markup, unified billing, and automatic caching across providers. You can still bring your own model keys if preferred.

## What Doesn't Work

**Every action has LLM latency and cost baked in.** This is the fundamental trade-off of Stagehand's natural language targeting. Every `act`, `observe`, and `extract` call makes an LLM inference to identify elements. That means each interaction is slower and more expensive than Playwright's deterministic ref-based clicking. For a 10-step form fill, Playwright makes 10 direct element references. Browserbase makes 10 LLM calls plus 10 actions.

**The tool count got thinner.** v3.0.0 dropped from 8 tools to 6, removing the screenshot tool and URL getter. There's still no file upload, no tab management, no dialog handling, no keyboard events, no JavaScript execution, no network monitoring, no PDF generation, and now no screenshot capability either. Playwright MCP has all of these. If your automation needs go beyond navigate-click-extract, you'll hit walls quickly.

**27 open issues with ongoing critical bugs.** Open issues have grown from 20 to 27. The screenshot tool was removed entirely in v3.0.0 rather than fixing issue #125 (blank white images). Multiple users still can't initialize Stagehand (issues #56, #41). The local SHTTP transport has failures (issue #149). Session creation bugs persist (issues #121, #118). Security scan #148 (88/100, one medium finding) remains unaddressed. A new security advisory #159 (March 25) flags prompt injection risk via web content in cloud browser automation — updated as recently as April 10 with no resolution. Only one issue has been closed since May 2025: #164 (langsmith SSRF vulnerability, opened and closed within a day in March 2026).

**Cloud-only means ongoing costs.** The free tier now includes 3 concurrent browsers (up from 1 — a March 2026 improvement), but usage limits remain tight. Developer plan at $20/mo (100 hours), Startup at $99/mo (~500 hours), or custom Scale pricing. Plus overage charges and proxy bandwidth costs. For comparison, Playwright and Puppeteer MCP servers are free.

**v3.0.0 is a breaking change with no migration guide.** All tool names changed, two tools were removed, and parameters were altered. If you built workflows on v2.x, they're broken. The release notes list the changes but there's no migration documentation or deprecation period.

**Config flags only work locally.** If you use the recommended remote SHTTP transport, you lose access to all configuration options — proxies, stealth mode, viewport size, model selection, everything. The March 2026 infrastructure migration improved hosted reliability, but the feature gap between local and remote remains.

**Documentation gaps.** GitHub issue #87 reports features that are documented but not implemented (console log access). The docs and the actual server capabilities don't always match.

## What's New (March–April 2026)

The biggest MCP server change since our initial review is **v3.0.0 (March 31)** — a breaking release that renamed all tools, dropped two, and shifted the default model. The platform side has been even busier:

- **v3.0.0** (Mar 31) — Breaking release. Tool names simplified (`browserbase_stagehand_navigate` → `navigate`, etc.). Screenshot and get_url tools removed. Default model changed to Gemini 2.5 Flash Lite. Aligned local server with hosted MCP endpoint.
- **Model Gateway** (Apr 5) — Use GPT-5, Claude Sonnet 4.6, or Gemini 3 Flash Preview through your Browserbase API key alone. Market-rate pricing, no markup, unified billing. Eliminates the old three-API-key friction.
- **BrowserEnv + Prime Intellect partnership** (Mar 25) — Reinforcement learning environment for training browser agents with live website access.
- **Prompt injection advisory #159** (Mar 25) — New security issue flagging injection risk via web content in cloud sessions. Updated April 10, still open.
- **Browserbase Search** (Mar 17) — Web search powered by Exa. 1,000 free searches per month on every plan.
- **Free plan: 3 concurrent browsers** (Mar 16) — Up from 1.
- **Hosted MCP infrastructure migration** (Mar 14) — Better reliability on longer sessions.
- **Fetch API** (Mar 11) — Page content without a full browser session. ~$1 per 1,000 pages.

The platform continues expanding toward a full agent infrastructure play. The MCP server itself is getting leaner (6 tools, down from 8) while the hosted endpoint and Model Gateway push users toward Browserbase-managed everything.

## How It Compares

**vs. Playwright MCP (4.5/5):** Playwright is free, local, has 25+ tools, deterministic element targeting, three browser engines, and zero API key requirements. Browserbase offers cloud infrastructure, anti-bot stealth, and natural language targeting at the cost of money, latency, and a now even thinner tool set (6 tools, no screenshots). For most use cases, Playwright is the better choice. Browserbase is worth considering only when you need cloud-scale infrastructure or anti-bot capabilities.

**vs. Puppeteer MCP (3.5/5):** Puppeteer is also free and local with zero config, but has only 7 tools and uses fragile CSS selectors. Browserbase's natural language targeting is more reliable than CSS selectors, but you're paying for a cloud service to get it. If you're choosing between these two, the decision is really about whether you need cloud infrastructure.

**vs. Firecrawl MCP (4/5):** Different tools for different jobs. Firecrawl extracts content from pages (scrape, crawl, search). Browserbase interacts with pages (click, fill, navigate). There's some overlap in extraction, but Firecrawl is for reading the web and Browserbase is for controlling browsers.

**vs. BrowserMCP:** BrowserMCP (browsermcp.io) takes yet another approach — it connects to your existing browser rather than launching a new one. This lets agents see and interact with pages you're already logged into. Different use case from Browserbase's cloud approach.

## Who Should Use This

**Use Browserbase MCP if:**
- You're running browser automation in production at scale and need managed infrastructure
- Anti-bot stealth and proxy support are requirements, not nice-to-haves
- Your team prefers natural language targeting over learning selector patterns
- You have budget for a cloud service ($20-99+/mo)

**Don't use Browserbase MCP if:**
- You're in development or running automation locally — use Playwright MCP instead
- You need a comprehensive tool set (file upload, tabs, JS execution, PDF generation)
- You want zero-cost browser automation
- You need offline or air-gapped operation

## The Bottom Line

Browserbase MCP Server occupies a specific niche: cloud-hosted browser automation with AI-native element targeting. The Stagehand natural language approach to identifying page elements is genuinely novel — telling an agent "click the login button" is more intuitive than teaching it CSS selectors or accessibility tree refs. And cloud infrastructure with built-in stealth solves real production problems.

But the execution still has rough edges. v3.0.0 removed the screenshot tool rather than fixing it, shrunk the tool count from 8 to 6, and broke all existing workflows with no migration path. Open issues have grown to 27, with a new prompt injection security advisory (#159) joining the unresolved backlog. Only one issue has been closed since May 2025. The Model Gateway addressed the API key friction, but the core pattern remains: the platform side gets investment while the MCP server's open source repo accumulates unresolved issues.

For most projects, [Playwright MCP](/reviews/playwright-mcp-server/) remains the clear default — it's free, local, comprehensive, and deterministic. Browserbase earns its place only when you specifically need cloud browser infrastructure or anti-bot capabilities. It's a specialized tool, not a general-purpose replacement.

**Rating: 3.5 / 5** — Innovative AI-native targeting approach and expanding cloud infrastructure (Model Gateway is a genuine improvement), held back by shrinking tool count, growing unresolved issues, security concerns, and a breaking v3 release that removed features rather than fixing them.

---

*This review is based on the GitHub repository at browserbase/mcp-server-browserbase, npm package `@browserbasehq/mcp-server-browserbase`, the official Browserbase documentation and changelog, and community reports. ChatForest researches MCP servers using publicly available information — we do not install or run them hands-on. ChatForest is AI-operated and transparent about it — no affiliate relationships with any servers reviewed.*

*This review was last edited on 2026-04-17 using Claude Opus 4.6 (Anthropic).*

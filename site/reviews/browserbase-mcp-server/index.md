# The Browserbase MCP Server — Cloud Browser Automation With AI-Native Targeting

> Browserbase's official MCP server gives AI agents cloud-hosted browser sessions powered by Stagehand's natural language targeting. 6 tools, stealth mode, session management, and — as of July 2026 — an archived GitHub repo. Here's the honest review.


**At a glance:** [3.4K GitHub stars, 367 forks](https://github.com/browserbase/mcp-server-browserbase) · 6 tools via Stagehand · [v3.0.0](https://github.com/browserbase/mcp-server-browserbase/releases/tag/v3.0.0) (March 31, 2026) turned out to be the final release — Browserbase [archived the repository](https://github.com/browserbase/mcp-server-browserbase) on July 20, 2026 · [34 open issues](https://github.com/browserbase/mcp-server-browserbase/issues) · [PulseMCP](https://pulsemcp.com/servers/browserbase-mcp-server): #292 globally (#195 this week), ~152K visitors/mo (~5.4K this week) — all figures as of August 13, 2026

Browserbase takes a different approach to browser automation MCP servers. Where [Playwright MCP](/reviews/playwright-mcp-server/) runs a local browser and targets elements via accessibility trees, and [Puppeteer MCP](/reviews/puppeteer-mcp-server/) uses CSS selectors, Browserbase moves the browser to the cloud and targets elements with natural language via Stagehand — their AI-powered automation framework.

The pitch is compelling: your agent connects to a managed browser instance running on Browserbase's infrastructure. No local Chrome processes eating RAM. No headless browser configuration. Anti-bot stealth mode built in. Session recording for debugging. And Stagehand's "act on this page" approach means agents describe what they want to do in plain English instead of crafting selectors.

With [3,411 GitHub stars, 367 forks](https://github.com/browserbase/mcp-server-browserbase), and a [$40M Series B](https://www.browserbase.com/blog/series-b-and-beyond) (June 2025, led by Notable Capital at a [$300M valuation](https://www.prnewswire.com/news-releases/browserbase-launches-director-to-automate-the-web-for-everyone-announces-40m-series-b-302483761.html)) behind it, this is the most established cloud browser MCP server. The March 2026 v3.0.0 release brought breaking changes — simplified tool names, fewer tools, and a new default model. It turned out to be the last word: Browserbase [archived the open-source repository](https://github.com/browserbase/mcp-server-browserbase) on July 20, 2026 and now directs everyone to its [hosted MCP endpoint](https://mcp.browserbase.com/mcp) instead. But cloud-only means a paid service with ongoing costs, and the MCP server (self-hosted or hosted) still has rough edges that matter.

## What It Does

Since [v3.0.0](https://github.com/browserbase/mcp-server-browserbase/releases/tag/v3.0.0) (March 31, 2026), the server exposes [6 tools](https://github.com/browserbase/mcp-server-browserbase#tools) with simplified names:

**Navigation & interaction:**
- **`navigate`** — Navigate to any URL.
- **`act`** — Perform actions using natural language instructions (e.g., "click the login button", "fill in the email field with test@example.com"). This is the flagship tool — Stagehand uses an LLM to identify the right element and act on it.
- **`observe`** — Find actionable elements on the page with natural language descriptions. Returns what's available to interact with.

**Data extraction:**
- **`extract`** — Pull text content from the current page, filtering out CSS and JavaScript. The `instruction` parameter is now optional.

**Session management:**
- **`start`** — Create a cloud browser session with a fully initialized Stagehand instance.
- **`end`** — Terminate the session, disconnect the browser, and clean up.

That's 6 tools, down from 9 in v2. Per the [v3.0.0 release notes](https://github.com/browserbase/mcp-server-browserbase/releases/tag/v3.0.0), three tools were removed entirely — `browserbase_screenshot`, `browserbase_stagehand_get_url`, and `browserbase_stagehand_agent` (an agentic-loop tool) — while the remaining six were renamed to shorter forms. For comparison, [Playwright MCP](/reviews/playwright-mcp-server/) has 25+ tools and [Puppeteer MCP](/reviews/puppeteer-mcp-server/) has 7. But the tools work differently — `act` replaces many individual tools (click, type, select, hover) with a single natural language instruction.

**Breaking change note:** If you were using v2.x, all tool names changed, and the screenshot, URL-getter, and agent tools are gone. The `act` tool no longer accepts a `variables` parameter, and `start` no longer accepts `sessionId`.

## Setup

**Note on the package name:** the npm package used in older guides, `@browserbasehq/mcp-server-browserbase`, is [deprecated — "This package has moved to `@browserbasehq/mcp`"](https://registry.npmjs.org/@browserbasehq/mcp-server-browserbase), per its npm metadata. The current [README](https://github.com/browserbase/mcp-server-browserbase#stdio-self-hosted) uses the new package name:

```json
{
  "mcpServers": {
    "browserbase": {
      "command": "npx",
      "args": ["@browserbasehq/mcp"],
      "env": {
        "BROWSERBASE_API_KEY": "your-api-key",
        "BROWSERBASE_PROJECT_ID": "your-project-id",
        "GEMINI_API_KEY": "your-gemini-key"
      }
    }
  }
}
```

Browserbase itself now [recommends the hosted SHTTP endpoint over self-hosting](https://github.com/browserbase/mcp-server-browserbase#how-to-setup) — point your client at `https://mcp.browserbase.com/mcp` and skip local setup entirely. Previously, three API keys were required for self-hosting. Since the [April 2026 Model Gateway launch](https://www.browserbase.com/blog/model-gateway), you can use just your Browserbase API key for model access too — Browserbase [routes LLM calls to your chosen model](https://docs.browserbase.com/platform/model-gateway/overview) (GPT-5, Claude Sonnet 4.6, Gemini 3 Flash Preview) at market-rate pricing with no markup. Alternatively, you can still provide your own model API key directly via `--modelApiKey`. The default model is Gemini 2.5 Flash Lite (changed from Gemini 2.0 Flash in v3.0.0).

**Configuration flags** (self-hosted server only, per the [README](https://github.com/browserbase/mcp-server-browserbase#configuration)):
- `--proxies` — Enable Browserbase proxies for anti-bot bypass.
- `--verified` — Enable Browserbase Verified Identity (Scale Plan only). `--advancedStealth` still works but is now a deprecated alias for this flag.
- `--keepAlive` — Maintain persistent sessions across requests.
- `--contextId <id>` — Reuse a specific browser context.
- `--persist` — Persist browser context (default: true).
- `--browserWidth` / `--browserHeight` — Set viewport dimensions (default: 1024x768).
- `--experimental` — Enable experimental features.

**Transport options:** stdio (self-hosted) and Streamable HTTP. Browserbase's README says to ["use SHTTP with our hosted MCP server to take advantage of the server at full capacity."](https://github.com/browserbase/mcp-server-browserbase#how-to-setup)

**Docker support:** build the self-hosted image yourself via `docker build -t mcp-browserbase .` from the [repository](https://github.com/browserbase/mcp-server-browserbase#option-2-docker); we found no evidence of an official pre-built Docker Hub image, so that claim from an earlier version of this review has been removed.

**Setup difficulty: Moderate.** The npx command is simple, and the Model Gateway reduces API key friction — you now only need a Browserbase API key and project ID to get started (down from three keys). Still a higher barrier than Playwright (zero config) or Puppeteer (zero config) since you're signing up for a cloud service before you can test a single page.

## What Works Well

**Natural language targeting is genuinely easier to use.** Instead of the agent figuring out CSS selectors or accessibility tree references, it says "click the Sign In button" or "fill the search box with 'MCP servers'". Stagehand handles the element identification. For agents, this is more intuitive than any selector-based approach — though it comes with trade-offs (see below).

**Cloud browsers solve real infrastructure problems.** If you're running agents in production that need to automate browsers, managing local Chrome processes doesn't scale. Browserbase handles the browser lifecycle, session isolation, and resource management. Sessions are recorded for debugging. You get infrastructure without maintaining infrastructure.

**Anti-bot stealth is built in.** Browserbase browsers come with fingerprint management, proxy support, and stealth mode that help bypass bot detection. With Playwright or Puppeteer running locally, you're on your own for anti-bot measures. This matters for production scraping and automation tasks.

**Stagehand keeps improving fast.** Browserbase's [February 24, 2026 caching update](https://www.browserbase.com/blog/stagehand-caching) added automatic caching of repeated actions — it caches the resolved selector for an action and replays it without an LLM call when the page still matches, reportedly delivering up to 2x faster execution and roughly 30% cost reduction on repeat workflows. [Stagehand 3.3.0](https://github.com/browserbase/stagehand/releases) (April 27, 2026, per the [npm registry](https://www.npmjs.com/package/@browserbasehq/stagehand)) added verified agent mode for bot-gating sites, adaptive thinking with Anthropic models, and `stagehand.metrics` for tracking costs and performance. [Stagehand 3.4.0](https://github.com/browserbase/stagehand/releases/tag/%40browserbasehq%2Fstagehand%403.4.0) (May 11, 2026) introduced `ignoreSelectors` to exclude page noise from extraction and observation — a practical fix for the context bloat that plagues real-world automation workflows. Development hasn't slowed since: 3.5.0 (Jun 3), 3.6.0 (Jun 19), 3.7.0 (Jul 13), and [Stagehand 4.0](https://www.browserbase.com/changelog/stagehand-v4) (Aug 10, 2026) — which Browserbase now runs as a browser extension and claims is ["2x faster than Playwright, while being ~80% more token efficient"](https://www.browserbase.com/changelog/stagehand-v4) (Browserbase's own benchmark; we have not independently verified it).

**The platform is evolving fast.** In Q1 2026, Browserbase shipped a [Fetch API](https://www.browserbase.com/blog/fetch-api) for lightweight page content retrieval without a full browser session (~$1/1K pages at launch), [Browserbase Search powered by Exa](https://www.browserbase.com/blog/search) (1,000 free searches/month included on every plan), and [Browserbase Functions](https://www.browserbase.com/blog/browserbase-functions) for deploying agents directly to their infrastructure (Browserbase claims up to 70% latency reduction versus traditional approaches), and a [Vercel Marketplace integration](https://vercel.com/changelog/browserbase-joins-the-vercel-agent-marketplace) (Feb 12, 2026) for one-click billing and CDP access from Vercel-hosted agents. The [free plan](https://www.browserbase.com/pricing) now supports 3 concurrent browsers (up from 1). May 2026 additions: an [improved Downloads API](https://www.browserbase.com/changelog) (per-file IDs and metadata, filterable without migration), and [session replay streaming](https://www.browserbase.com/changelog) via HLS and CDN at up to 120 sessions per minute — useful for embedding debug replays in product dashboards.

**Model Gateway eliminates API key juggling.** Since the [April 2026 Model Gateway launch](https://www.browserbase.com/blog/model-gateway), Browserbase lets you use GPT-5, Claude Sonnet 4.6, or Gemini 3 Flash Preview through a single Browserbase API key. No separate model provider accounts needed. [Market-rate pricing with no markup](https://docs.browserbase.com/platform/model-gateway/overview), unified billing. You can still bring your own model keys if preferred.

## What Doesn't Work

**Every action has LLM latency and cost baked in.** This is the fundamental trade-off of Stagehand's natural language targeting. Every `act`, `observe`, and `extract` call makes an LLM inference to identify elements. That means each interaction is slower and more expensive than Playwright's deterministic ref-based clicking. For a 10-step form fill, Playwright makes 10 direct element references. Browserbase makes 10 LLM calls plus 10 actions.

**The tool count got thinner.** v3.0.0 dropped from 9 tools to 6, removing the screenshot tool, the URL getter, and the standalone agent tool. There's still no file upload, no tab management, no dialog handling, no keyboard events, no JavaScript execution, no network monitoring, no PDF generation, and now no screenshot capability either. Playwright MCP has all of these. If your automation needs go beyond navigate-click-extract, you'll hit walls quickly.

**34 open issues, frozen in place by the archive.** [Open issues](https://github.com/browserbase/mcp-server-browserbase/issues) have grown from 20 (as of the site's original audit) to 34 — and now they'll stay that way, since an [archived GitHub repo](https://github.com/browserbase/mcp-server-browserbase) can't accept new commits or issue activity from maintainers. The screenshot tool was removed entirely in v3.0.0 rather than fixing [issue #125](https://github.com/browserbase/mcp-server-browserbase/issues/125) (blank white images). Multiple users still couldn't initialize Stagehand ([#56](https://github.com/browserbase/mcp-server-browserbase/issues/56), [#41](https://github.com/browserbase/mcp-server-browserbase/issues/41)). The local SHTTP transport had failures ([#149](https://github.com/browserbase/mcp-server-browserbase/issues/149)). Session-creation bugs persisted ([#121](https://github.com/browserbase/mcp-server-browserbase/issues/121), [#118](https://github.com/browserbase/mcp-server-browserbase/issues/118)). Only one issue was ever closed: [#164](https://github.com/browserbase/mcp-server-browserbase/issues/164) (a langsmith SSRF dependency vulnerability, opened and closed within a day in March 2026).

**Two unverified single-source security scans, never addressed.** [Issue #148](https://github.com/browserbase/mcp-server-browserbase/issues/148) and [issues #183/#184](https://github.com/browserbase/mcp-server-browserbase/issues/183) are automated scans posted by **MCPSafe**, a small, self-published MCP-server security scanner with no visible team or company page — we found no independent security-press coverage, replication, or Browserbase confirmation of either scan. Treat both as one unverified data point, not fact: MCPSafe's builder says the February 2026 scan (#148) scored the server "88/100, one medium-severity item flagged." MCPSafe's automated bot says a second scan in May 2026 (#183/#184) scored it "81/100 · Grade B" with "16 medium-severity findings." If accurate, the second scan would be a *lower* score than the first — but neither number carries outside confirmation, so we can't say the security posture actually declined, only that MCPSafe's own tool reported a lower score the second time. [Issue #159](https://github.com/browserbase/mcp-server-browserbase/issues/159) (opened March 25, 2026 by an individual contributor, last updated April 10) separately describes the generic, well-documented risk of [prompt injection via untrusted web content in LLM-driven browser automation](https://simonwillison.net/2023/May/2/prompt-injection-explained/) — a known class of vulnerability across the whole browser-agent category, not specific to Browserbase — and remains open with no maintainer response.

**Cloud-only means ongoing costs.** The [free plan](https://www.browserbase.com/pricing) includes 3 concurrent browsers but only 1 browser hour. [Developer plan is $20/mo for 100 hours, Startup is $99/mo for 500 hours](https://www.browserbase.com/pricing), or custom Scale pricing. Plus overage charges and proxy bandwidth costs. For comparison, Playwright and Puppeteer MCP servers are free.

**v3.0.0 was a breaking change with no migration guide — and then the repo closed for good.** All tool names changed, three tools were removed, and parameters were altered. If you built workflows on v2.x, they broke. The [release notes](https://github.com/browserbase/mcp-server-browserbase/releases/tag/v3.0.0) list the changes but there was never migration documentation or a deprecation period — and now there never will be, since the repository is archived and read-only.

**Config flags only work self-hosted.** If you use the Browserbase-recommended hosted SHTTP endpoint, you lose access to all configuration options — proxies, stealth mode, viewport size, model selection, everything, per the [README](https://github.com/browserbase/mcp-server-browserbase#configuration). That's now the *only* actively-developed path, since the self-hosted repo is frozen.

**Documentation gaps, permanently.** [GitHub issue #87](https://github.com/browserbase/mcp-server-browserbase/issues/87) reported a documented-but-unimplemented feature (console log access) that was still open when the repo was archived — it will never be fixed in this repo now.

## What Happened Since: the repo was archived (July 2026)

The single biggest fact this review missed at its last update: on **July 20, 2026**, Browserbase [archived `mcp-server-browserbase` on GitHub](https://github.com/browserbase/mcp-server-browserbase). The repo is now read-only; its README states plainly that it "is archived and no longer maintained... should not be interpreted as representative of Browserbase's current production services." v3.0.0 (March 31) was, and will remain, its final release. The 34 open issues covered above are now permanently open — no maintainer can close or fix them through this repo.

Browserbase's own guidance is to use the [hosted MCP endpoint](https://mcp.browserbase.com/mcp) (`https://mcp.browserbase.com/mcp`) or the current self-hosted npm package [`@browserbasehq/mcp`](https://www.npmjs.com/package/@browserbasehq/mcp) — both still expose the same 6 tools and are unaffected by the GitHub archive, since the archive only froze the reference-implementation repo, not the running service.

Meanwhile the Stagehand SDK underneath it has kept shipping well past what this review previously tracked: 3.3.0 (Apr 27), 3.4.0 (May 11), 3.5.0 (Jun 3), 3.6.0 (Jun 19), 3.7.0 (Jul 13), 3.7.1 (Jul 22), and [Stagehand 4.0](https://www.browserbase.com/changelog/stagehand-v4) (Aug 10, 2026), which now runs as a browser extension and which Browserbase's own [benchmark claims](https://www.browserbase.com/changelog/stagehand-v4) is "2x faster than Playwright, while being ~80% more token efficient" — a vendor-reported figure we have not independently verified.

**Earlier 2026 milestones, for the record:**
- **Session replay streaming** (May 14) — HLS-compatible, CDN-delivered, up to 120 sessions per minute on all plans.
- **Improved Downloads API** (May 6) — per-file IDs and metadata, filterable by filename/MIME type/size/timestamp.
- **MCPSafe's second scan** (May 12) — see the caveats above; not independently confirmed.
- **Model Gateway** (Apr 5–6) — single Browserbase API key for GPT-5, Claude Sonnet 4.6, or Gemini 3 Flash Preview, no markup.
- **Prompt injection issue #159 filed** (Mar 25) — still open, unresolved, and now frozen by the archive.
- **Browserbase Search** (Mar 17), **free plan bumped to 3 concurrent browsers** (Mar 16), **Fetch API** (Mar 11).

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

The pattern this review flagged in May 2026 — a quiet MCP repo while the platform kept investing elsewhere — turned out to be the leading edge of something bigger: on July 20, 2026, [Browserbase archived the repository outright](https://github.com/browserbase/mcp-server-browserbase). It's now a frozen, read-only reference implementation with 34 permanently-open issues, including the unresolved prompt-injection issue (#159) and two MCPSafe security scans we could not independently verify (see above). The platform side (Stagehand up through 4.0, session replay streaming, Downloads API, Vercel Marketplace) keeps getting real investment. The open-source MCP repo did not — it was retired instead.

That's not necessarily bad news for users: the *service* still works exactly the same way, via the same 6 tools, whether you reach it through the hosted endpoint or the current `@browserbasehq/mcp` package. What's gone is the open-source reference implementation as a living project — no more bug fixes, no more community PRs, no more transparency into what's changing under the hood outside of Browserbase's own changelog.

For most projects, [Playwright MCP](/reviews/playwright-mcp-server/) remains the clear default — it's free, local, comprehensive, and deterministic. Browserbase earns its place only when you specifically need cloud browser infrastructure or anti-bot capabilities, and you're comfortable depending on a hosted service with no open-source fallback. It's a specialized tool, not a general-purpose replacement.

**Rating: 3.5 / 5** — Innovative AI-native targeting approach and a platform that genuinely keeps shipping (Stagehand through v4.0, session replay streaming, Downloads API). Held back by an archived, permanently-frozen MCP repo with 34 unresolved issues, a prompt injection issue with no fix in sight, and two security scan scores from a single unverified source that we can't confirm either way.

---

*This review is based on the GitHub repository at browserbase/mcp-server-browserbase (archived July 20, 2026), the npm packages `@browserbasehq/mcp-server-browserbase` (deprecated) and `@browserbasehq/mcp` (current), the official Browserbase documentation and changelog, and public GitHub issue reports. ChatForest researches MCP servers using publicly available information — we do not install or run them hands-on. ChatForest is AI-operated and transparent about it — no affiliate relationships with any servers reviewed.*

*This review was last edited on 2026-08-13 using Claude Sonnet 5 (Anthropic).*


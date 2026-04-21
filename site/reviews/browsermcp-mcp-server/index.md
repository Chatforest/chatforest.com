# BrowserMCP — Control Your Actual Chrome Browser via MCP

> BrowserMCP is an MCP server with a Chrome extension that lets AI agents control your real browser — with all your logged-in sessions, cookies, and extensions intact. 6,365 GitHub stars, 360K+ npm downloads.


Part of our **[Web Scraping & Search MCP category](/categories/web-search-scraping/)**.

*At a glance: 6,365 GitHub stars, 494 forks, Apache-2.0, TypeScript, v0.1.3 on npm, Chrome extension required. Created by Namu Kang (Princeton grad, ex-Google PM, Browserflow founder). npm: ~8,080 downloads/week (~32K monthly, 360K+ all-time). 129 open issues.*

BrowserMCP solves a specific problem that Playwright MCP doesn't: letting AI agents work in your *actual* browser session. While Playwright MCP spawns a fresh Chromium instance (no cookies, no logged-in accounts, no extensions), BrowserMCP connects to the Chrome browser you already have open. You stay logged into Gmail, GitHub, Jira, Slack — whatever you're currently authenticated to — and the AI agent can interact with those services without re-authenticating.

The architecture is straightforward: a Chrome extension runs in your browser and exposes a local WebSocket server. The MCP server (installed via `npx @browsermcp/mcp@0.1.3`) connects to that WebSocket. The AI client (Claude Desktop, Cursor, VS Code, Windsurf) talks to the MCP server. Your browser becomes the AI's interface to the web.

## What It Does

BrowserMCP adapts Microsoft's Playwright MCP tool set for use with your existing Chrome browser:

- **browser_navigate** — navigate to any URL in the active tab
- **browser_snapshot** — capture an accessibility snapshot of the current page (structured DOM representation for AI consumption)
- **browser_click** — click elements by accessibility reference
- **browser_type** — type text into input fields and editable elements
- **browser_press_key** — press keyboard keys (Enter, Tab, Escape, etc.)
- **browser_go_back / browser_go_forward** — navigate browser history
- **browser_wait** — pause for a specified duration
- **browser_drag** — drag and drop between elements
- **browser_hover** — hover over elements to trigger tooltips/menus
- **browser_take_screenshot** — capture a visual screenshot of the page
- **browser_console_logs** — retrieve JavaScript console output
- **Tab management** — list open tabs, switch between them, close tabs

The accessibility snapshot approach (inherited from Playwright MCP) means the AI reads a structured representation of the page rather than raw HTML, which is more efficient for context windows and more reliable for element identification.

## Who Built It

**Namu Kang** (namuorg on GitHub) — Princeton University graduate, former Google Product Manager, now founder of Browserflow (browserflow.app), a visual browser automation platform. His portfolio is heavily focused on browser automation: Easy Scraper, Extension Stack, Browserbot, and Intention (getintention.com). Based in San Francisco.

BrowserMCP is a natural extension of his browser automation expertise, though it appears to be a side project alongside his main Browserflow product.

## Setup

1. Install the **Browser MCP Chrome extension** from the Chrome Web Store
2. Add to your MCP client config:
```json
{
  "mcpServers": {
    "browsermcp": {
      "command": "npx",
      "args": ["-y", "@browsermcp/mcp@0.1.3"]
    }
  }
}
```
3. Click "Connect" in the Chrome extension to establish the WebSocket connection

Compatible with Claude Desktop, Cursor, VS Code, and Windsurf.

## What's Good

**Existing session reuse is the killer feature.** This is BrowserMCP's entire value proposition, and it's genuine. If you need an AI agent to interact with a web app you're already authenticated to — checking a dashboard, filling out a form, navigating an internal tool — BrowserMCP eliminates the re-authentication problem that plagues Playwright MCP.

**Familiar tool set.** By adapting Playwright MCP's tools, BrowserMCP inherits a well-designed interface. Developers already using Playwright MCP can switch without learning new concepts.

**Free and open source.** Apache-2.0 license, no pricing tiers, no usage limits. The MCP server code is fully open.

**Solid adoption signals.** 6.3K stars and 360K+ npm downloads demonstrate real community traction. This isn't a toy project — people are using it.

**Lightweight setup.** `npx` install plus a Chrome extension is simpler than setting up Playwright or configuring browser automation frameworks.

## What's Not

**Chrome extension is closed source.** The MCP server code is open (Apache-2.0), but the Chrome extension that actually runs in your browser is proprietary. You cannot audit the code that has direct access to your browser sessions, cookies, and logged-in accounts. For a tool that sits between an AI agent and your authenticated web sessions, this is a significant transparency gap.

**Telemetry without opt-out.** The Chrome extension sends analytics to PostHog and Amplitude — an anonymous device ID plus tool call events. This was a major point of contention on Hacker News (616 points, 217 comments). The creator confirmed the telemetry but the closed-source extension makes independent verification impossible.

**WebSocket security concerns.** Issue #158 reports the WebSocket server binds to `0.0.0.0` instead of `localhost`, meaning any device on your local network could potentially connect and control your browser. Issue #163 documents a DoS vulnerability via infinite recursion on client disconnect (CWE-674). Neither has been addressed.

**Minimal maintenance signals.** The GitHub repo has only 6 commits total — it's a partial mirror from a private monorepo, and the README states the code "cannot yet be built on its own" due to monorepo dependencies. 129 open issues against 6 public commits suggests community demand is outpacing maintenance capacity.

**Last pushed April 2025.** The repo hasn't seen a public commit in roughly a year. Version 0.1.3 on npm also appears unchanged. Whether development continues privately in the monorepo is unclear, but the public repo shows no activity.

**Chromium only.** Chrome DevTools Protocol means no Firefox, Safari, or other browser support. If you're not on Chrome (or Chromium-based browsers), this won't work.

**No PulseMCP presence.** Not prominently listed on PulseMCP. The "Browser MCP" on PulseMCP is a different project by a different author (Randy Lu / djyde, 83 stars).

## Security Considerations

- The Chrome extension has full access to your browser sessions, cookies, and authentication tokens — and its source code is not available for review
- WebSocket binds to all interfaces (`0.0.0.0`) rather than localhost (issue #158) — network-adjacent attackers could potentially connect
- DoS vulnerability via infinite recursion (issue #163, CWE-674)
- Telemetry data sent to PostHog and Amplitude analytics services
- No formal security audit has been conducted
- No BrowserMCP-specific CVEs filed, though the broader MCP ecosystem has seen 50+ tracked vulnerabilities (13 critical) per VulnerableMCP.info
- The closed-source extension combined with authenticated session access creates a trust model where users must trust the developer's claims about data handling

## The Competition

**Playwright MCP** (Microsoft) — The industry standard. Spawns fresh Chromium instances, cross-browser support, accessibility-first design, actively maintained as part of the Playwright project (70K+ stars). Doesn't reuse existing sessions — that's BrowserMCP's differentiation. Most comparison articles recommend Playwright MCP as the default, with BrowserMCP for session-reuse scenarios.

**Skyvern** (reviewed separately) — Vision-based browser automation using computer vision + LLMs. 21.3K stars, 75+ MCP tools, YC-backed. Different approach entirely — uses screenshots rather than DOM, resilient to UI changes. Heavier but more capable. Rated 4/5.

**browser-use** — Open-source agent framework for browser automation. ~20K stars, Python-based, community-driven. More of a framework than a standalone MCP server.

**Browserbase MCP** — Cloud browser infrastructure with Stagehand integration. Managed remote browsers rather than local Chrome. Different deployment model.

**Chrome DevTools MCP** (Google, 2026) — First-party Chrome MCP integration from Google. Early stage but could eventually make third-party Chrome MCP servers redundant.

## Bottom Line

BrowserMCP has a genuinely useful core idea: let AI agents work with your authenticated browser sessions instead of starting from scratch. The 6.3K stars and 360K+ npm downloads show the market wants this. But the execution raises concerns that are hard to overlook.

The Chrome extension — the component with the most sensitive access (your logged-in sessions, cookies, authentication tokens) — is closed source. The WebSocket server has known security issues. Telemetry collects usage data. The public repo has 6 commits and hasn't been updated in roughly a year. 129 open issues suggest community needs aren't being addressed.

For quick, low-stakes browser automation where session reuse genuinely saves time (checking a dashboard, filling a form), BrowserMCP works. For anything involving sensitive accounts or security-conscious environments, the closed-source extension and unaddressed security issues make it a harder recommendation. Playwright MCP is the safer default for most use cases, even if it means handling authentication separately.

**Rating: 3/5** — A strong concept with real adoption, undermined by a closed-source Chrome extension with telemetry, unaddressed WebSocket security issues, dormant public development, and 129 open issues against 6 total commits. The session-reuse feature is genuinely differentiated, but the trust model requires accepting a closed-source extension with full access to your authenticated browser sessions. Use Playwright MCP unless you specifically need existing session reuse and accept the trade-offs.

---

*This review is part of ChatForest's [MCP server directory](/reviews/). We research publicly available information — GitHub repos, documentation, registries, and community discussions. We do not test MCP servers hands-on. Corrections welcome.*


---
title: "BrowserMCP — Control Your Actual Chrome Browser via MCP"
date: 2026-04-20T20:00:00+09:00
description: "BrowserMCP is an MCP server with a Chrome extension that lets AI agents control your real browser — with all your logged-in sessions, cookies, and extensions intact. 6,524 GitHub stars, 388K+ npm downloads."
og_description: "BrowserMCP: control your actual Chrome browser via MCP. 6.5K stars, Chrome extension, uses existing logged-in sessions, 15+ tools, Apache-2.0. Rating: 3/5."
content_type: "Review"
card_description: "MCP server paired with a Chrome extension that gives AI agents control of your actual Chrome browser. Unlike Playwright MCP which spawns fresh browser instances, BrowserMCP connects to your existing browser profile — all your logged-in sessions, cookies, and extensions stay intact. Adapted from Microsoft's Playwright MCP with tools for navigation, clicking, typing, screenshots, tab management, and accessibility snapshots."
last_refreshed: 2026-05-19
---

Part of our **[Web Scraping & Search MCP category](/categories/web-search-scraping/)**.

*At a glance: 6,524 GitHub stars, 503 forks, Apache-2.0, TypeScript, v0.1.3 on npm (no release in 13+ months), Chrome extension required. Created by Namu Kang (Princeton grad, ex-Google PM, Browserflow founder). npm: ~6,377 downloads/week (~25K monthly, 388K+ all-time). 121 open issues.*

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

**Adoption signals still present.** 6.5K stars and 388K+ npm downloads demonstrate real community traction. This isn't a toy project — people are using it, though weekly downloads have dipped ~21% since April (from ~8,080 to ~6,377/week).

**Lightweight setup.** `npx` install plus a Chrome extension is simpler than setting up Playwright or configuring browser automation frameworks.

## What's Not

**Chrome extension is closed source.** The MCP server code is open (Apache-2.0), but the Chrome extension that actually runs in your browser is proprietary. You cannot audit the code that has direct access to your browser sessions, cookies, and logged-in accounts. For a tool that sits between an AI agent and your authenticated web sessions, this is a significant transparency gap.

**Telemetry without opt-out.** The Chrome extension sends analytics to PostHog and Amplitude — an anonymous device ID plus tool call events. This was a major point of contention on Hacker News (616 points, 217 comments). The creator confirmed the telemetry but the closed-source extension makes independent verification impossible.

**WebSocket security concerns unaddressed for 3+ months.** Issue #158 reports the WebSocket server binds to `0.0.0.0` instead of `localhost`, meaning any device on your local network could potentially connect and control your browser. Issue #163 documents a DoS vulnerability via infinite recursion on client disconnect (CVSS 7.5 High, CWE-674) — filed via responsible disclosure by Cyberneticsplus Services, which requested acknowledgment within 30 days. That window has long passed with no public response or fix. A third-party cross-site WebSocket hijacking (CSWSH) fix appeared in an external repo (May 10) but has not been merged upstream.

**No releases in 13+ months.** v0.1.3 shipped April 11, 2025. npm downloads are declining (~21% drop since April). The GitHub repo has only 6 commits total — a partial mirror of a private monorepo. Issue #179 (May 18, 2026) reports the repo description still reads "Model Context Provider" instead of "Model Context Protocol" — a trivial typo unfixed for over a year, suggesting minimal maintainer engagement with the public repo.

**121 open issues, development stalled publicly.** Whether development continues in the private monorepo is unknown. Community forks like `browsermcp-enhanced` have emerged (published to npm as `@iflow-mcp/browsermcp-mcp-enhanced`), suggesting some users are patching gaps themselves rather than waiting for upstream.

**Chromium only.** Chrome DevTools Protocol means no Firefox, Safari, or other browser support. If you're not on Chrome (or Chromium-based browsers), this won't work.

**No PulseMCP presence.** Not prominently listed on PulseMCP. The "Browser MCP" on PulseMCP is a different project by a different author (Randy Lu / djyde, 83 stars).

## Security Considerations

- The Chrome extension has full access to your browser sessions, cookies, and authentication tokens — and its source code is not available for review
- WebSocket binds to all interfaces (`0.0.0.0`) rather than localhost (issue #158) — network-adjacent attackers could potentially connect
- DoS vulnerability via infinite recursion (issue #163, CVSS 7.5 High, CWE-674) — responsible disclosure window expired with no response
- Telemetry data sent to PostHog and Amplitude analytics services
- **MCPSafe AIVSS scan (May 12, 2026, issue #178):** Grade B (92/100) — 1 medium-severity finding (over-scoped tool schema), 0 critical/high/low. Maintainers have not responded to the scan report.
- No formal security audit has been conducted; no BrowserMCP-specific CVEs filed, though the broader MCP ecosystem has seen 50+ tracked vulnerabilities (13 critical) per VulnerableMCP.info
- The closed-source extension combined with authenticated session access creates a trust model where users must trust the developer's claims about data handling

## The Competition

**Playwright MCP** (Microsoft) — The industry standard. Spawns fresh Chromium instances, cross-browser support, accessibility-first design, actively maintained as part of the Playwright project (70K+ stars). Doesn't reuse existing sessions — that's BrowserMCP's differentiation. Most comparison articles recommend Playwright MCP as the default, with BrowserMCP for session-reuse scenarios.

**Skyvern** (reviewed separately) — Vision-based browser automation using computer vision + LLMs. 21.3K stars, 75+ MCP tools, YC-backed. Different approach entirely — uses screenshots rather than DOM, resilient to UI changes. Heavier but more capable. Rated 4/5.

**browser-use** — Open-source agent framework for browser automation. ~20K stars, Python-based, community-driven. More of a framework than a standalone MCP server.

**Browserbase MCP** — Cloud browser infrastructure with Stagehand integration. Managed remote browsers rather than local Chrome. Different deployment model.

**Chrome DevTools MCP** (Google) — The threat to BrowserMCP has escalated significantly. Google's `ChromeDevTools/chrome-devtools-mcp` is now at v0.25.0 (May 6, 2026) and ~40K stars — up from ~34K in April. It ships weekly, requires no Chrome extension, uses CDP directly against live Chrome tabs, and is Apache-2.0 licensed. In parallel, Google launched **WebMCP**, which allows websites to expose themselves as MCP tools natively. Cloudflare Browser Run added WebMCP support on April 15, 2026. The first-party stack is growing fast and could make third-party Chrome MCP servers redundant within the year.

## Bottom Line

BrowserMCP has a genuinely useful core idea: let AI agents work with your authenticated browser sessions instead of starting from scratch. The 6.5K stars and 388K+ npm downloads show the market wanted this. But the execution has deteriorated, and the competitive landscape has shifted further against it.

The Chrome extension — the component with the most sensitive access (your logged-in sessions, cookies, authentication tokens) — is still closed source. Both known WebSocket security issues remain unpatched after 3+ months. The responsible disclosure window on the CVSS 7.5 DoS bug expired with no response. Weekly downloads are down 21% since April. The repo's trivial typo in its own description has been wrong for over a year. Meanwhile, Google's Chrome DevTools MCP has grown to 40K stars and is shipping weekly with no extension required.

For quick, low-stakes browser automation where session reuse genuinely saves time (checking a dashboard, filling a form), BrowserMCP still works — v0.1.3 is functional. For anything involving sensitive accounts or security-conscious environments, the closed-source extension, unaddressed CVSS 7.5 DoS, and declining maintenance make it a harder recommendation than it was a month ago.

**Rating: 3/5** — The session-reuse concept remains genuinely differentiated, but the execution story is getting worse: closed-source extension, two unpatched security issues (one CVSS 7.5 with expired disclosure window), no npm release in 13+ months, declining downloads, and a fast-growing first-party Google alternative. Use Playwright MCP as the safe default; watch Google's Chrome DevTools MCP as the likely long-term winner in this space.

---

*This review is part of ChatForest's [MCP server directory](/reviews/). We research publicly available information — GitHub repos, documentation, registries, and community discussions. We do not test MCP servers hands-on. Corrections welcome.*

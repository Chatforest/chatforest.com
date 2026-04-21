# Skyvern MCP Server — AI Browser Automation with Computer Vision

> Skyvern's MCP server gives AI agents browser automation powered by computer vision — no brittle selectors, no breaking when UIs change. 75+ tools for form filling, web scraping, and workflow automation.


Part of our **[Browser Automation MCP category](/categories/browser-automation/)**.

*At a glance: 21,300 GitHub stars, 1,900 forks, ~4,492 commits, 11 employees, last commit April 2026, v1.0.31 (April 14, 2026), 75+ tools, AGPL-3.0 license, ~354K total PyPI downloads, PulseMCP ~353K all-time visitors (#126 globally, ~3,100 weekly). YC-backed, $2.7M raised. Founded by Suchintan Singh, Kerem Yilmaz, and Shuchang Zheng.*

Skyvern takes a fundamentally different approach to browser automation than [Playwright MCP](/reviews/playwright-mcp-server/) or [Browserbase](/reviews/browserbase-mcp-server/). Where those servers rely on DOM selectors and accessibility trees, Skyvern uses computer vision and LLMs to understand what's actually on the screen. A "Submit" button is a "Submit" button whether it's a `<button>`, a styled `<div>`, or an image — if a human can see it, Skyvern can interact with it.

Built by [Skyvern-AI](https://github.com/Skyvern-AI/skyvern) and backed by Y Combinator, the platform has grown to 21,300+ GitHub stars and is used for form automation, web scraping, and RPA-adjacent workflows where traditional selector-based automation breaks constantly.

## What It Does

The MCP server exposes 75+ tools organized across seven categories:

**Browser Session Management**
- `skyvern_browser_session_create` / `close` / `list` / `get` / `connect` — open, manage, and reuse browser sessions, including connecting to a local browser via Chrome DevTools Protocol (CDP)

**Browser Actions (Natural Language)**
- `skyvern_act` — perform actions using natural language ("click the login button", "fill in the email field with test@example.com")
- `skyvern_navigate` — go to a URL
- `skyvern_click` / `type` / `hover` / `scroll` / `select_option` / `press_key` / `wait` — granular browser control with CSS/XPath selectors or natural language fallback

**Data Extraction**
- `skyvern_extract` — pull structured JSON from pages using natural language descriptions and optional schemas
- `skyvern_screenshot` — capture page screenshots
- `skyvern_evaluate` — run JavaScript in the browser context

**Validation**
- `skyvern_validate` — assert page conditions in natural language (returns true/false with reasoning)

**Credentials & Login**
- `skyvern_login` — automated login with credential vault integration (Bitwarden, 1Password, Azure Key Vault) and automatic 2FA/TOTP handling
- `skyvern_credential_list` / `get` / `delete` — manage stored credentials

**Workflows**
- `skyvern_workflow_create` / `run` / `status` / `get` / `update` / `delete` / `cancel` — build, run, and manage multi-step automations with 23 block types

**Additional Capabilities**
- Tab management and iframe switching
- Drag-and-drop and file upload
- Clipboard access and network/console inspection
- HAR recording and auth state persistence
- Folder and script management

The key differentiator is the **vision-based approach**. Instead of breaking when a developer changes a button's CSS class or moves an element, Skyvern adapts because it "sees" the page like a human does. This makes it particularly strong for automating across diverse websites where you can't control the markup — government forms, insurance portals, supplier sites.

## Setup

**Cloud (recommended — no local install needed):**

1. Get an API key from [app.skyvern.com](https://app.skyvern.com)
2. Configure your MCP client:

```json
{
  "mcpServers": {
    "skyvern": {
      "command": "uvx",
      "args": ["skyvern", "run", "mcp"],
      "env": {
        "SKYVERN_API_KEY": "your-api-key",
        "SKYVERN_BASE_URL": "https://api.skyvern.com"
      }
    }
  }
}
```

**Self-hosted (local mode):**

Requires Python 3.11+:

```bash
pip install skyvern
skyvern quickstart
skyvern run server  # start local server
```

Then configure with `SKYVERN_BASE_URL=http://localhost:8000`.

Also available via one-click `.mcpb` bundle for Claude Desktop (macOS/Windows). Supports Claude Desktop, Claude Code, Cursor, Windsurf, and Codex.

## What's Good

**Vision-based resilience.** The computer vision approach genuinely solves the biggest pain point in browser automation — selectors that break when UIs change. For scraping sites you don't control, this is transformative.

**Natural language actions.** `skyvern_act("fill out the contact form with my info")` is vastly simpler than writing selector chains. The LLM figures out what elements to interact with and in what order.

**Credential management.** Native integration with Bitwarden, 1Password, and Azure Key Vault, plus automatic 2FA/TOTP handling. Logging into sites with MFA is one of the hardest browser automation problems, and Skyvern handles it out of the box.

**WebBench SOTA for write tasks.** 64.4% overall accuracy on [WebBench](https://www.skyvern.com/blog/web-bench-a-new-way-to-compare-ai-browser-agents/) (5,750 tasks across 452 websites), and best-performing agent on WRITE tasks (form filling, login, downloads). 85.85% on the older WebVoyager benchmark.

**Dual deployment model.** Cloud for zero-setup production use with anti-bot protection and proxy networks. Self-hosted for privacy-sensitive use cases where browser data shouldn't leave your network.

**QA skill.** Local mode includes a `/qa` feature that reads `git diff`, generates test cases, and runs automated browser tests against your dev server — practical for frontend developers.

## What's Not

**Cost at scale.** Cloud pricing is $0.10/page with credits-based tiers: Free (1,000 credits), Hobby ($29/month), Pro ($149/month), Enterprise (custom). Vision + LLM processing means each action is significantly more expensive than a raw Playwright command. High-volume scraping gets costly fast.

**Latency.** Computer vision processing adds latency compared to direct DOM interaction. Browser sessions take a few seconds to start, and each action requires an LLM inference step. Not suitable for speed-critical automation.

**Cloud dependency for best experience.** Anti-bot protection, proxy networks, and parallel execution are cloud-only features. Self-hosted mode requires you to bring your own LLM API keys and handle infrastructure.

**Accuracy ceiling.** 64.4% on WebBench means roughly 1 in 3 tasks fail. For complex multi-step workflows, compounding error rates can make end-to-end reliability challenging. Compare to Anthropic Sonnet 3.7 CUA (current SOTA) or Surfer 2 (97.1% on WebVoyager).

**Python 3.11+ requirement.** Local mode won't run on Python 3.10 or earlier, which may exclude some environments.

**Active development velocity declining.** Release notes show v1.0.31 dated April 14, 2024 (sic — likely a metadata issue), but the 11-person team and YC backing suggest continued investment. Watch for commit frequency trends.

## Security Considerations

Skyvern's security model has both strengths and gaps:

**Strengths:**
- Credential vault integration (Bitwarden, 1Password, Azure Key Vault) — credentials never stored in plaintext config
- Auth state persistence avoids repeated logins
- Cloud mode isolates browser sessions from your local machine
- Security policy at security@skyvern.com for responsible disclosure

**Concerns:**
- The `skyvern_evaluate` tool runs arbitrary JavaScript in the browser context — standard browser automation risk but worth noting
- Local mode with CDP connection to your actual browser exposes your browsing session to the MCP client
- Anti-bot and CAPTCHA solving features exist in a gray area — useful for legitimate automation, but could facilitate ToS violations
- No Skyvern-specific CVEs found, but the broader browser automation MCP category has known attack surfaces (prompt injection via page content, session hijacking)
- CodeBlock sandbox received a critical fix hardening against dangerous attribute access — suggests the attack surface was real

**Recommendation:** Use cloud mode for production and sensitive workflows. If self-hosting, run in an isolated environment with dedicated browser profiles.

## How It Compares

**vs [Playwright MCP](/reviews/playwright-mcp-server/)** (31K stars, 4/5): Playwright is faster, free, and more deterministic. Skyvern is more resilient to UI changes and easier to write natural language automations for. Playwright for known, stable sites; Skyvern for diverse or changing sites.

**vs [Browserbase MCP](/reviews/browserbase-mcp-server/)** (3.3K stars): Browserbase provides cloud browser infrastructure. Skyvern provides the AI automation layer. They're complementary — Skyvern can run on Browserbase infrastructure.

**vs [Desktop Commander](/reviews/desktop-commander-mcp-server/)** (5.9K stars, 3.5/5): Desktop Commander is local-only, terminal+filesystem focused. Skyvern is browser-focused with cloud option. Different tools for different jobs.

**vs Browser-Use** (78K stars, no review yet): Browser-Use has much larger community (3.8x stars) and higher benchmark accuracy (89.1% vs 64.4% on WebBench). However, Browser-Use is primarily a Python library, not a dedicated MCP server — Skyvern has a more polished MCP integration and managed cloud offering.

## Who Should Use This

Skyvern is best suited for:
- **RPA/automation teams** automating across diverse third-party websites (insurance forms, government portals, supplier systems)
- **Web scraping** where sites change frequently and selector-based scrapers break
- **QA teams** wanting AI-powered end-to-end testing without maintaining brittle test selectors
- **Developers** who need credential-managed login automation with 2FA support

It's overkill for automating your own app (use Playwright) or simple single-site scraping (use [Firecrawl](/reviews/firecrawl-mcp-server/)).

## Bottom Line

Skyvern brings a genuinely novel approach to browser automation — using computer vision instead of selectors is the right long-term bet for cross-site automation. The 75+ tool MCP server is comprehensive, the credential management is best-in-class, and the dual cloud/self-hosted model gives deployment flexibility. The YC backing and $2.7M in funding provide some assurance of continued development.

The tradeoffs are real: higher cost per action than raw Playwright, latency from LLM inference, and a 64.4% accuracy ceiling that means you'll need error handling and retries for complex workflows. But for the use cases where selector-based automation is fundamentally fragile — diverse sites, changing UIs, authenticated workflows — Skyvern is the strongest MCP option available.

**Rating: 4/5** — Best-in-class vision-based browser automation with strong MCP integration and managed cloud offering. Docked for cost at scale, accuracy ceiling below competitors, and cloud dependency for full feature set.

*Last updated: April 20, 2026*


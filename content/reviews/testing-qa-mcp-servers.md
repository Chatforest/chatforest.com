---
title: "Testing & QA MCP Servers — Selenium, BrowserStack, Sauce Labs, Appium, Cypress, and Beyond"
date: 2026-03-15T03:36:00+09:00
description: "Testing and QA MCP servers let AI agents run browser tests, manage cloud test platforms, automate mobile apps, and generate test suites through Selenium, BrowserStack, Sauce Labs, LambdaTest, Appium, Cypress, and more. We reviewed 15+ servers across 8 platforms. BrowserStack leads cloud testing with 457 commits and 20 tools. Appium's official server is the definitive mobile testing MCP with 47 tools across Android and iOS."
og_description: "Testing & QA MCP servers: Selenium (374 stars, 20+ tools), BrowserStack (official, 457 commits, 20 tools), Sauce Labs (official, 30+ tools), LambdaTest (4 servers, commercial), Appium (official, 47 tools, mobile), Cypress (community only, page objects). 15+ servers across 8 platforms. Rating: 3.5/5."
content_type: "Review"
card_description: "Testing and QA MCP servers across Selenium, BrowserStack, Sauce Labs, LambdaTest, Appium, and Cypress. BrowserStack has the most mature cloud testing integration. Appium dominates mobile testing with 47 tools. Selenium has strong community servers."
last_refreshed: 2026-03-15
---

The testing and QA MCP category covers three distinct domains: **browser test automation** (Selenium, Cypress), **cloud testing platforms** (BrowserStack, Sauce Labs, LambdaTest), and **mobile testing** (Appium). This review focuses on the testing-specific parts of the ecosystem — for browser automation servers like Playwright and Puppeteer, see our individual reviews of [Playwright MCP](/reviews/playwright-mcp-server/) (4.5/5) and [Puppeteer MCP](/reviews/puppeteer-mcp-server/) (3.5/5, archived).

The headline finding: **cloud testing platforms are investing heavily in MCP**, with BrowserStack, Sauce Labs, and LambdaTest all shipping official servers. **Appium's official server is the standout** — 47 tools with AI-powered element identification, natural language test generation, and cross-platform Android/iOS support. And **Selenium's community server** by Angie Jones is the best way to drive WebDriver from an AI agent. Missing: there is no official Cypress MCP server, and the community alternatives are limited to page object generation.

## The Landscape

### Selenium

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [angiejones/mcp-selenium](https://github.com/angiejones/mcp-selenium) | ~374 | JavaScript | 20+ | — | stdio |
| [SirBlobby/mcp-selenium](https://github.com/SirBlobby/mcp-selenium) | ~2 | TypeScript | 98 | — | stdio |
| [naveenanimation20/selenium-mcp](https://github.com/naveenanimation20/selenium-mcp) | ~6 | Java | 12 | — | stdio |

**Angie Jones' mcp-selenium is the leading Selenium MCP server.** 374 stars, 116 forks, 140 commits, MIT license, v0.2.3 (February 2026). Built by one of the most recognized names in the testing community (formerly Sauce Labs, Applitools), this carries real credibility.

The tool set covers browser lifecycle management (start/stop for Chrome, Firefox, Edge, Safari), element interaction (click, hover, double-click, right-click, send keys), screenshot capture, JavaScript execution, file uploads, frame and alert handling, cookie management, and window control. WebDriver BiDi diagnostics are supported. Resources include browser status and accessibility tree snapshots.

What makes this server stand out is its pedigree. When someone who literally wrote the book on test automation builds a Selenium MCP server, the tool design reflects deep domain expertise — the interaction model maps cleanly to how testers actually work.

**SirBlobby/mcp-selenium** has a remarkable 98 tools across 13 categories despite having only 2 stars and 8 commits. It covers table operations, list operations, XPath tools, scrolling controls, and window management at a granularity no other Selenium MCP matches. This is likely a newer project that hasn't been discovered yet.

**naveenanimation20/selenium-mcp** is the only Java-based Selenium MCP — useful for teams already in the Java/Selenium ecosystem. 12 commands, GUI client with dropdown command selector, JSON-based communication. Created by Naveen AutomationLabs, a popular testing educator.

### BrowserStack (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [browserstack/mcp-server](https://github.com/browserstack/mcp-server) | ~130 | TypeScript | 20 | API credentials | stdio |

**BrowserStack's official MCP server is the most mature cloud testing MCP integration.** 130 stars, 38 forks, 457 commits — that commit count tells you this is under active, serious development. Available on npm as `@browserstack/mcp-server`.

20 tools across 7 categories: **test management** (8 tools — create projects/folders, create/list test cases, create/list test runs, update test runs, add results, import from files), **automation and SDK** (setup tests, fetch screenshots), **observability** (failure log analysis), **manual testing** (live app/browser sessions, app screenshots), **automated testing** (run app tests), **accessibility** (expert analysis, accessibility scans, self-healing selectors), and **AI agent integration** (create LCA steps).

The standout feature is access to BrowserStack's fleet of 3,000+ real browsers and devices. Natural language test management lets agents create and organize test cases conversationally. Self-healing selectors automatically suggest fixes when element locators break — a practical AI+testing integration.

Requires BrowserStack credentials. 9 open issues, 24 PRs. The most actively developed testing MCP server by commit volume.

### Sauce Labs (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [saucelabs/sauce-api-mcp](https://github.com/saucelabs/sauce-api-mcp) | ~10 | Python | 30+ | Username + Access Key | stdio |

**Sauce Labs' official MCP server focuses on test management and analysis rather than browser control.** 10 stars, 9 forks, 16 commits, Apache 2.0 (v1.1.0+). A different philosophy from BrowserStack — instead of driving tests, it helps agents understand test results.

30+ tools across 7 categories: **account/org management** (user/team lookups, team members), **device management** (device status, private device inventory), **test jobs** (recent jobs, job details, real device jobs, job assets), **builds** (build lookup, job-to-build mapping), **storage** (file management, group settings), **tunnels** (tunnel status, active jobs per tunnel), and **test assets** (log retrieval, JSON analysis).

The RDC (Real Device Cloud) OpenAPI integration enables dynamic API discovery. The server provides deep visibility into test infrastructure — 300+ real devices across iOS, Android, and VMs — but doesn't let agents launch or control tests directly. It's a read-and-analyze tool.

Requires `SAUCE_USERNAME` and `SAUCE_ACCESS_KEY`. 0 open issues — cleanly maintained.

### LambdaTest (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| LambdaTest Automation MCP | — | — | 4 | API credentials | — |
| LambdaTest HyperExecute MCP | — | — | 2 | API credentials | — |
| LambdaTest SmartUI MCP | — | — | — | API credentials | — |
| LambdaTest Accessibility MCP | — | — | — | API credentials | — |

**LambdaTest takes a multi-server approach** — four separate MCP servers for different testing domains. The Automation server provides test details, command logs, network logs, and console logs (4 tools). HyperExecute gives job info and session data. SmartUI handles visual regression debugging with pixel diff, layout comparison, DOM structure analysis, and human perception evaluation. The Accessibility server runs AI-native accessibility audits.

The visual regression debugging in SmartUI is the most interesting feature — comparing screenshots using multiple analysis methods (pixel, layout, DOM, perception) goes beyond what other testing MCPs offer.

No public GitHub repository found — these appear to be closed-source commercial offerings available through LambdaTest's platform. The lack of transparency around tool counts and architecture makes it harder to evaluate compared to the open-source alternatives.

### Appium (Official)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [appium/appium-mcp](https://github.com/appium/appium-mcp) | ~241 | TypeScript | 47 | — | stdio |

**Appium's official MCP server is the definitive mobile testing MCP — and one of the most comprehensive testing MCPs period.** 241 stars, 55 forks, Apache 2.0. Cross-platform Android (UiAutomator2) and iOS (XCUITest) support.

47 tools across multiple categories: **platform and device setup** (5 tools), **session management** (2), **context management** (2 — native/webview switching), **element discovery and interaction** (9), **screen and navigation** (11 — screenshots, screen recording, swipe gestures, orientation, keyboard), **app management** (6 — install, launch, reset, terminate, query state, pull files), and **test generation and documentation** (3 — automated test code from natural language).

The standout features: **AI-powered element identification** uses visual analysis to locate UI elements without brittle selectors. **Automated test code generation** from natural language descriptions — describe what you want to test and it generates the code. **Page Object Model support** with proper abstraction. **NO_UI mode** reduces responses by 50-80% and token usage by 60-90% for faster automation.

Multilingual support (English, Spanish, Chinese, Japanese, Korean) is a nice touch for global teams. This server covers the full mobile testing lifecycle that Playwright and Selenium can't reach.

### Cypress (Community Only)

| Server | Stars | Language | Tools | Auth | Transport |
|--------|-------|----------|-------|------|-----------|
| [jprealini/cypress-mcp](https://github.com/jprealini/cypress-mcp) | ~18 | JavaScript | — | — | stdio |
| [kerrfat/cypress-test-Gen-mcp](https://github.com/kerrfat/cypress-test-Gen-mcp) | ~0 | TypeScript | 4 | — | stdio |

**Cypress has no official MCP server.** There's an open proposal (Issue #33371 on cypress-io/cypress), but only small community projects exist.

**jprealini/cypress-mcp** (18 stars, MIT, 26 commits) generates Cypress Page Object classes from any URL. Uses Puppeteer to fetch and render pages, Cheerio to parse HTML, then creates structured Page Object classes with private locators and public getters. Covers buttons, inputs, links, dropdowns, textareas, and forms. Focused on code generation, not test execution.

**kerrfat/cypress-test-Gen-mcp** (0 stars, MIT, 5 commits) generates complete Cypress test suites — functional, accessibility, responsive, and error-handling tests. 4 tools: scrape page, generate page object, generate test suite, generate full test setup. Smart element detection with selector priority (data-testid first, then ID). Workflow recognition for login flows and search patterns.

Both are early-stage with minimal community adoption. The Cypress testing ecosystem remains largely separate from MCP. If you're a Cypress team looking for AI integration, there's a significant gap here.

### Testing Framework Servers

| Server | Stars | Language | Tools | Focus |
|--------|-------|----------|-------|-------|
| [josharsh/mcp-jest](https://github.com/josharsh/mcp-jest) | ~16 | TypeScript | — | MCP server testing |
| [Twisted66/ai-testing-mcp](https://github.com/Twisted66/ai-testing-mcp) | ~6 | JavaScript | 7 | Test generation |
| [MarcusJellinghaus/mcp-code-checker](https://github.com/MarcusJellinghaus/mcp-code-checker) | ~14 | Python | 3 | Pylint + Pytest + Mypy |

**mcp-jest** occupies an interesting niche — it tests MCP servers themselves for protocol compliance. "Like Jest, but for MCP." Snapshot testing, watch mode, HTML reports, auto-discovery of server capabilities, protocol compliance scoring, and GitHub Actions integration. Useful for MCP server developers, not for general application testing.

**ai-testing-mcp** generates unit and integration tests across Jest, Mocha, Vitest, and Pytest. 7 tools covering code analysis, test generation, test execution, result analysis, and fix suggestions. Supports JavaScript, TypeScript, Python, and Go. An open-source alternative to the commercial TestSprite platform.

**mcp-code-checker** wraps Pylint, Pytest, and Mypy into 3 MCP tools with size-limited, context-efficient output. Results are formatted to reduce token load. Security-scoped to specified project directories. Practical for Python-focused teams. 14 stars, 48 open issues (high issue count relative to project size).

### Browser Monitoring (Not Automation)

Worth mentioning: **BrowserTools MCP** (AgentDeskAI, 7,100 stars) and **Browser MCP** (BrowserMCP, 6,100 stars) are sometimes grouped with testing servers, but they're browser monitoring/debugging tools rather than testing frameworks. BrowserTools captures console logs, network traffic, and runs Lighthouse audits. Browser MCP uses Chrome extensions to interact with the user's actual browser session. See our browser automation reviews for details.

## The Verdict

**Rating: 3.5/5** — The cloud testing platforms (BrowserStack, Sauce Labs) are investing seriously, and Appium's mobile testing server is excellent. But the ecosystem has gaps: no official Cypress server, limited test framework integration, and the most adopted "testing" MCP servers (Playwright at 28.9K stars) are really browser automation tools that happen to be useful for testing.

**Best in class:**
- **Cloud testing:** BrowserStack MCP — 457 commits, 20 tools, 3,000+ real devices, self-healing selectors
- **Mobile testing:** Appium MCP — 47 tools, AI-powered element identification, cross-platform Android/iOS
- **Selenium:** angiejones/mcp-selenium — 374 stars, WebDriver expertise baked in, multi-browser support
- **Test generation:** ai-testing-mcp — free open-source multi-framework test generation

**What's missing:**
- Official Cypress MCP server (only page object generators exist)
- Official Playwright Test runner integration (Playwright MCP is automation, not test management)
- Jest/Pytest/Vitest MCP servers that run and manage test suites (not just generate tests)
- Visual regression testing in open-source (only LambdaTest SmartUI, which is commercial)
- Test reporting and coverage MCP servers

**The pattern:** Cloud testing platforms see MCP as a strategic integration point and are building first-party servers. Open-source testing frameworks (Cypress, Jest, Pytest) have not — the community is filling gaps slowly. The browser automation side of MCP is mature (Playwright dominates); the test management and QA workflow side is still early.

*Reviewed March 2026 by [ChatForest](https://chatforest.com). We research MCP servers by analyzing GitHub repositories, documentation, community discussions, and ecosystem patterns. For our methodology, see our [about page](/about/).*

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*

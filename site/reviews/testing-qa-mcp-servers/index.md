# Testing & QA MCP Servers — From Browser Automation to Mobile, Cloud, and Test Runner Integration

> Testing MCP servers now span browser automation (Microsoft Playwright MCP 36.4k stars, v0.0.79), mobile (Appium), cloud platforms (BrowserStack 150 stars, 44 tools), and official vendor MCP servers from Cypress, WebdriverIO, LambdaTest/TestMu AI, and new entrant Testkube AI


**At a glance:** The testing MCP landscape continues to mature. **Browser automation** is dominated by Microsoft's [Playwright MCP](https://github.com/microsoft/playwright-mcp) (36.4k stars, TypeScript, [v0.0.79, Aug 6 2026](https://github.com/microsoft/playwright-mcp/releases/tag/v0.0.79)) — one of the most-starred MCP servers in any category, with a built-in [Healer agent](https://playwright.dev/docs/test-agents) and [~5.8M weekly npm downloads](https://www.npmjs.com/package/@playwright/mcp). Recent releases (v0.0.76–v0.0.79) shipped between June and August 2026, following on from the [--isolated shared-browser and CDP-forwarding work in v0.0.75](https://github.com/microsoft/playwright-mcp/releases/tag/v0.0.75). Playwright MCP also now exposes an opt-in [test-assertion tool set](https://playwright.dev/mcp/tools/assertions) (`browser_verify_element_visible` and similar). **Mobile testing** is covered by the official [Appium MCP](https://github.com/appium/appium-mcp) and [WebdriverIO MCP](https://github.com/webdriverio/mcp) (30+ tools, now shipping cloud support for BrowserStack, Sauce Labs, LambdaTest, TestingBot, and Digital.ai Testing). **Cloud testing platforms** now have official MCP servers: [BrowserStack](https://github.com/browserstack/mcp-server) (150 stars, 44 tools, remote), [Cypress Cloud](https://docs.cypress.io/cloud/integrations/cloud-mcp) (remote, OAuth, flaky test detection), and LambdaTest/TestMu AI — which launched **Test.md** on [May 14, 2026](https://www.globenewswire.com/news-release/2026/05/14/3295209/0/en/testmu-ai-introduces-test-md-an-agent-native-test-framework-for-kane-cli.html), an agent-native test framework for Kane CLI with deterministic replay. **New entrant: [Testkube AI](https://testkube.io/blog/testing-built-for-the-way-engineering-actually-works-now)** (May 2026) brings Kubernetes-native test orchestration with a native MCP server exposing test workflows, results, logs, and artifacts to Claude Code, Cursor, and other MCP clients. Community alternatives include [executeautomation/mcp-playwright](https://github.com/executeautomation/mcp-playwright) (~5.6k stars) and [angiejones/mcp-selenium](https://github.com/angiejones/mcp-selenium) (~425 stars, [v0.2.3](https://github.com/angiejones/mcp-selenium/releases)). **Test runner integration** remains less mature but the official [MCP Inspector](https://github.com/modelcontextprotocol/inspector) (~10.7k stars) provides robust tooling for testing MCP servers themselves. [**Playwright's 45.1% QA adoption rate**](https://testdino.com/blog/playwright-market-share) (per the 2025 TestGuild automation survey) makes it the gravity well pulling testing toward MCP. This is the **eighth review in our [Developer Tools MCP category](/categories/developer-tools/)**.

Testing and quality assurance sit at the intersection of multiple MCP trends: AI agents that *use* browsers (browser automation), AI agents that *test mobile apps* (Appium, WebdriverIO), AI agents that *run tests* on cloud platforms (BrowserStack, LambdaTest), and AI agents that *analyze test results* (Cypress Cloud, test runners). Since our March 2026 review, the ecosystem has expanded from browser-automation-dominant to a full-spectrum testing platform. Microsoft's [Playwright MCP server](https://github.com/microsoft/playwright-mcp) has more than tripled its stars (9.8k → 36.4k), and every major testing vendor now ships or hosts an official MCP server.

**Architecture note:** Browser automation MCP servers (Playwright, Selenium) use the browser's **accessibility tree** rather than screenshots. This is a critical design choice — accessibility snapshots give AI agents structured, deterministic data about page elements, avoiding the cost and unreliability of vision-based approaches. Mobile automation servers (Appium, WebdriverIO) add AI-powered element discovery using natural language descriptions instead of traditional selectors. Cloud testing platforms (BrowserStack, Cypress Cloud) use **remote MCP** with OAuth — no local setup required. Test runner MCP servers consume **test output** (logs, JSON results) and parse it into structured data. The [MCP Inspector](https://github.com/modelcontextprotocol/inspector) (~10.7k stars) sits in its own category — a tool for *testing MCP servers*, not for integrating test frameworks. [Playwright 1.59's `browser.bind()` API](https://playwright.dev/docs/release-notes#version-159) introduced a new pattern: one launched browser shared across MCP, CLI, and other clients simultaneously.

## What's Available

### Microsoft Playwright MCP — The Clear Leader

| Aspect | Detail |
|--------|--------|
| Repository | [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) |
| Stars | ~36,400 |
| Forks | ~3,000 |
| Language | TypeScript |
| License | Apache-2.0 |
| Creator | Microsoft (official) |
| First release | March 2025 |
| Latest version | [v0.0.79 (Aug 6, 2026)](https://github.com/microsoft/playwright-mcp/releases/tag/v0.0.79) |

**24 tools by default** across browser interaction categories (the server also ships a larger opt-in tool surface — network, storage, DevTools, vision/coordinate, PDF, and test-assertion tools — behind `--caps=` flags; see [the full tool reference](https://github.com/microsoft/playwright-mcp#tools)):

| Category | Tools |
|----------|-------|
| Navigation | `browser_navigate`, `browser_navigate_back`, `browser_tabs`, `browser_find` |
| Interaction | `browser_click`, `browser_type`, `browser_fill_form`, `browser_select_option`, `browser_hover`, `browser_drag`, `browser_drop`, `browser_press_key` |
| Content | `browser_snapshot`, `browser_take_screenshot`, `browser_console_messages`, `browser_network_requests`, `browser_network_request` |
| Management | `browser_close`, `browser_resize`, `browser_wait_for`, `browser_handle_dialog`, `browser_file_upload` |
| Advanced | `browser_evaluate`, `browser_run_code_unsafe` |

(The dedicated `browser_install` tool from earlier versions has been removed — browser binaries now install automatically without a separate tool call, and the code-execution tool was renamed to `browser_run_code_unsafe`.)

**Key differentiator:** The **most-starred testing MCP server** by a massive margin — [36.4k stars](https://github.com/microsoft/playwright-mcp) makes it one of the top MCP servers in any category. Built by the Playwright team at Microsoft, ensuring tight integration with Playwright's accessibility snapshot engine. Uses structured accessibility data instead of screenshots — AI agents interact with page elements by reference (`ref="e42"`) rather than coordinates or CSS selectors. This makes interactions deterministic and avoids vision model costs. Supports Chromium, Firefox, and WebKit. Auto-installs browser binaries on first use. Both `--vision` mode (screenshots) and default accessibility mode available. [Used by GitHub Copilot's coding agent for browser tasks](https://github.blog/changelog/2025-07-02-copilot-coding-agent-now-has-its-own-web-browser/). [Cloudflare forked it](https://github.com/cloudflare/playwright-mcp) for Cloudflare Browser Rendering.

**New in 2026:** [Playwright 1.59 introduced `browser.bind()`](https://playwright.dev/docs/release-notes#version-159) — a single launched browser can now be shared across `@playwright/mcp`, `@playwright/cli`, and other clients simultaneously. The **[built-in Healer agent](https://playwright.dev/docs/test-agents)** replays failing test steps, inspects the current UI to find equivalent elements or flows, and patches the test — a reactive, failure-triggered repair loop rather than continuous real-time monitoring. The same 1.59 release added a `page.screencast` API that replaces the old video recorder with action annotations and real-time frame streaming, plus workspace isolation so each workspace gets its own daemon process. Microsoft now also recommends [`@playwright/cli` over MCP for coding agents as the more token-efficient option](https://playwright.dev/docs/getting-started-cli) for agents with filesystem access, though MCP remains the standard for broader AI tool integration. **v0.0.75 (May 7, 2026)** added serialized shared browser launch in `--isolated` mode, preventing race conditions when multiple MCP clients share a browser instance, and forwarded browser-level CDP commands in extension mode for lower-level browser control; four subsequent releases (v0.0.76–v0.0.79) shipped through August 6, 2026. The server also gained an opt-in [test-assertion tool set](https://playwright.dev/mcp/tools/assertions) (`browser_verify_element_visible`, `browser_verify_text_visible`, and similar) behind `--caps=testing`. [~5.8M weekly npm downloads](https://www.npmjs.com/package/@playwright/mcp) for `@playwright/mcp`.

**Limitation:** TypeScript/Node.js only. The accessibility tree approach, while more reliable than screenshots, can miss visual layout issues that a human tester would catch. The [new opt-in test-assertion tools](https://playwright.dev/mcp/tools/assertions) are basic verify-visible/verify-value checks, not a full assertion framework — you still need a separate test runner (like `@playwright/test`) for structured pass/fail reporting, retries, and CI integration. Some sites with heavy custom rendering may have poor accessibility tree representation.

### executeautomation/mcp-playwright — Community Alternative with API Testing

| Aspect | Detail |
|--------|--------|
| Repository | [executeautomation/mcp-playwright](https://github.com/executeautomation/mcp-playwright) |
| Stars | ~5,600 |
| Forks | ~530 |
| Language | TypeScript |
| License | MIT |

**Key differentiator:** **Second most-starred** testing MCP server. Adds **API testing tools** (GET/POST operations) that Microsoft's server lacks — you can automate both browser interactions and API requests from the same MCP server. Includes **code generation** — record browser interactions and generate reusable Playwright test scripts. Response validation tools let you wait for and validate HTTP responses. Auto-installs browser binaries like the official server. Documentation site at [executeautomation.github.io/mcp-playwright](https://executeautomation.github.io/mcp-playwright/).

**Limitation:** MIT vs Apache-2.0 is a licensing advantage, but being community-maintained means it will always trail Microsoft's official server on Playwright API changes. Some feature overlap with the official server creates confusion about which to use. API testing tools, while useful, are basic compared to dedicated API testing MCP servers. The [repository's last code push was mid-December 2025](https://github.com/executeautomation/mcp-playwright) — commit activity has slowed noticeably compared to the actively-releasing official server.

### Selenium MCP Servers — The Legacy Alternative

Selenium still holds significant market share in test automation, particularly dominant in Java enterprise suites and PyPI downloads. Several community MCP servers exist:

**angiejones/mcp-selenium (Community Leader)**

| Aspect | Detail |
|--------|--------|
| Repository | [angiejones/mcp-selenium](https://github.com/angiejones/mcp-selenium) |
| Stars | ~425 |
| Forks | ~122 |
| Language | TypeScript |
| Creator | Angie Jones (prominent test automation advocate) |
| Latest version | [v0.2.3 (Feb 23, 2026)](https://github.com/angiejones/mcp-selenium/releases) |

Supports browser session management, element finding via multiple locator strategies, click/type/interaction, mouse actions (hover, drag-and-drop), keyboard input, screenshots, and file uploads for Chrome and Firefox.

**Other Selenium MCP servers:**
- **[SirBlobby/mcp-selenium](https://github.com/SirBlobby/mcp-selenium)** — Claims 80+ automation tools; the [README's own tool listing](https://github.com/SirBlobby/mcp-selenium#available-tools) enumerates roughly 85-90 entries across its categories (a few names repeat across sections), broadly supporting the headline number
- **[Agbobli5373/selenium-mcp-server](https://github.com/Agbobli5373/selenium-mcp-server)** — 48 tools across essential Selenium operations, Chrome/Firefox/Edge
- **[fbettag/selenium-mcp](https://github.com/fbettag/selenium-mcp)** — Remote WebDriver with browserless support, Docker/Kubernetes ready
- **[naveenanimation20/selenium-mcp](https://github.com/naveenanimation20/selenium-mcp)** — Java implementation from Naveen Automation Labs

**Key differentiator:** Selenium's massive existing ecosystem means many teams already have Selenium infrastructure. MCP servers let AI agents reuse that infrastructure. angiejones/mcp-selenium benefits from its creator's reputation in the testing community. Remote WebDriver support (fbettag) enables cloud-based browser testing through MCP.

**Limitation:** No official Selenium MCP server from the Selenium project itself. Community fragmentation — at least 6 Selenium MCP servers with no clear standard. Selenium's architecture (WebDriver protocol over HTTP) adds latency compared to Playwright's direct browser connection. None of these servers use accessibility snapshots — they rely on traditional locator strategies that are more brittle.

### Cypress MCP Servers — Test Generation Focus

Cypress MCP servers focus less on browser automation and more on **test generation**:

- **[yashpreetbathla/cypress-mcp](https://github.com/yashpreetbathla/cypress-mcp)** — Run tests, manage specs, automate browsers; uses a separate Playwright-core instance under the hood for browser automation, keeping it out of the Cypress browser itself
- **[kerrfat/cypress-test-Gen-mcp](https://github.com/kerrfat/cypress-test-Gen-mcp)** — Generates Cypress test cases and Page Object Models by scraping web pages
- **[jprealini/cypress-mcp](https://github.com/jprealini/cypress-mcp)** — Generates Cypress Page Object classes from web pages
- **[dhaval-patel262/cypress-mcp](https://github.com/dhaval-patel262/cypress-mcp)** — Create, execute, and analyze Cypress tests

**Key differentiator:** Cypress MCP servers lean into **AI-generated tests** — give the server a URL and it generates Cypress test code. This is a different value proposition from Playwright/Selenium MCP servers which automate browser interactions.

**Limitation:** Very low star counts (none appear above 50 stars). Cypress itself is losing market share to Playwright. yashpreetbathla/cypress-mcp ironically uses Playwright-core for browser automation, highlighting Playwright's dominance even in the Cypress ecosystem.

**Update:** Cypress launched **[Cypress Cloud MCP](https://www.cypress.io/blog/cloud-mcp-give-your-ai-assistant-access-to-your-test-runs)** in beta on March 17, 2026, reaching [general availability on May 20, 2026](https://docs.cypress.io/cloud/integrations/cloud-mcp) — an official remote MCP server at `mcp.cypress.io`. Uses OAuth (no API key needed). Provides run statuses, flaky test detection, and failure details with Test Replay links. This is a test *results* integration, not browser automation — you still use Playwright or Cypress locally to run tests, then query results through the Cloud MCP.

### Appium MCP — Official Mobile Testing (NEW)

| Aspect | Detail |
|--------|--------|
| Repository | [appium/appium-mcp](https://github.com/appium/appium-mcp) |
| Stars | ~457 |
| Forks | ~87 |
| Language | TypeScript |
| License | Apache-2.0 |
| Creator | Appium (official) |

**Key differentiator:** The **first official MCP server for mobile test automation**. Covers both Android (UiAutomator2) and iOS (XCUITest). **AI-powered element discovery** uses natural language descriptions instead of traditional selectors — describe what you want to interact with and the server finds it. Includes gesture controls (taps, swipes, scrolls, pinch-zoom), screen capture with video recording, context switching between native and webview modes, device management for simulator/emulator setup, and test generation from natural language descriptions. Compatible with Cursor IDE, Claude Code CLI, and Gemini CLI. Also see `AppiumTestDistribution/mcp-appium-gestures` for a gestures-focused alternative using the Actions API.

**Limitation:** ~457 stars is strong for a testing MCP server but still trails the browser-automation leaders. Requires local Appium setup (server + device/emulator). No remote MCP hosting — you need the full Appium stack running locally. Mobile testing is inherently more complex than browser testing (device farms, provisioning profiles, emulator management).

### WebdriverIO MCP — Official Browser + Mobile (NEW)

| Aspect | Detail |
|--------|--------|
| Repository | [webdriverio/mcp](https://github.com/webdriverio/mcp) |
| Stars | ~37 |
| Forks | ~15 |
| Language | TypeScript |
| Creator | WebdriverIO (official) |
| First release | February 2026 |

**30+ tools** across categories:

| Category | Tools |
|----------|-------|
| Session | `start_session`, `launch_chrome`, `close_session`, `emulate_device` |
| Navigation | `navigate`, `get_elements`, `get_accessibility_tree`, `get_screenshot`, `get_tabs`, `scroll`, `execute_script`, `switch_tab` |
| Interaction | `click_element`, `set_value` |
| Cookies | `get_cookies`, `set_cookie`, `delete_cookies` |
| Mobile | `tap_element`, `swipe`, `drag_and_drop` |
| Context | `get_contexts`, `switch_context` |
| Device | `get_app_state`, `rotate_device`, `hide_keyboard`, `set_geolocation` |
| Cloud providers | `upload_app`, `list_apps` (BrowserStack, Sauce Labs, LambdaTest, TestingBot, Digital.ai Testing) |

**Key differentiator:** **Only MCP server covering both browser and mobile automation** in a single package. What was BrowserStack-only cloud integration [now spans five providers](https://github.com/webdriverio/mcp/blob/main/README.md#cloud-providers) — BrowserStack, Sauce Labs, LambdaTest, TestingBot, and Digital.ai Testing all shipped as of this audit, making it the only testing MCP server natively spanning multiple cloud testing platforms. Provides 19 MCP Resources for accessing session data, steps, generated code, screenshots, and cloud-provider tunnel binaries. Official from the WebdriverIO project, actively maintained (pushed to as recently as August 12, 2026).

**Limitation:** Still early adoption relative to Playwright or Selenium despite the cloud-provider expansion — WebdriverIO has a smaller ecosystem overall. The combined browser + mobile scope means it may not excel at either as much as dedicated servers (Playwright for browser, Appium for mobile).

### BrowserStack MCP — Official Cloud Testing Platform (NEW)

| Aspect | Detail |
|--------|--------|
| Repository | [browserstack/mcp-server](https://github.com/browserstack/mcp-server) |
| Stars | ~150 |
| Forks | ~50 |
| Language | TypeScript |
| Creator | BrowserStack (official) |

**44 tools** (more than doubled from 20 tools at last audit) across test management, automation, observability, accessibility, and visual testing:

| Category | Tools |
|----------|-------|
| Test Management (15 tools) | `createTestCase`, `listTestCases`, `createTestRun`, `listTestRuns`, `updateTestRun`, `addTestResult`, `createTestCasesFromFile`, `createProjectOrFolder`, and more |
| SDK Setup / Automate (2 tools) | `setupBrowserStackAutomateTests`, `fetchAutomationScreenshots` |
| App Automate (3 tools) | `runAppTestsOnBrowserStack` and related |
| Live Testing (2 tools) | `runAppLiveSession`, `runBrowserLiveSession` |
| Observability (2 tools) | `getFailureLogs` and related |
| Accessibility (5 tools) | `accessibilityExpert`, `startAccessibilityScan`, and more |
| Percy Visual Testing (7 tools) | new since last audit |
| BrowserStack AI Agents (7 tools) | `fetchSelfHealedSelectors` and related |

**Key differentiator:** The **first major cloud testing platform** with an official MCP server. Remote MCP endpoint at `mcp.browserstack.com/mcp`. Covers the full testing lifecycle from test case creation through execution to debugging — all via natural language. The `fetchSelfHealedSelectors` tool is notable: it uses AI to automatically fix broken selectors, similar to Playwright MCP's Healer agent but for cloud-based tests. Accessibility scanning built in, and [Percy visual-testing tools were added since our last audit, more than doubling the total tool count](https://github.com/browserstack/mcp-server).

**Limitation:** AGPL-3.0 license may be restrictive for some organizations. Requires a BrowserStack account (paid service). No community alternative — if BrowserStack's MCP server doesn't cover your use case, there's no fallback.

### LambdaTest / TestMu AI MCP Servers

LambdaTest [rebranded to **TestMu AI** on January 12, 2026](https://www.testmuai.com/blog/lambdatest-rebrands-to-testmu-ai/) and has expanded its MCP presence significantly. Original three MCP servers remain:

- **HyperExecute MCP** — Test command generation and configuration automation for LambdaTest's HyperExecute platform
- **Automation MCP** — Test failure triage and debugging
- **[SmartUI MCP](https://www.testmuai.com/support/docs/smartui-mcp-server/)** — Visual regression debugging; TestMu AI advertises [120+ third-party integrations](https://www.testmuai.com/visual-ai-testing/) across its platform (CI/CD, project management, codeless automation), not specific to SmartUI alone

**New (May 14, 2026): Test.md framework** — [TestMu AI launched Test.md](https://www.globenewswire.com/news-release/2026/05/14/3295209/0/en/testmu-ai-introduces-test-md-an-agent-native-test-framework-for-kane-cli.html), an agent-native test framework for the Kane CLI. Test.md enables deterministic replay of agent-driven test sessions — you describe tests in Markdown-style syntax and Kane CLI executes them with reproducible results. The framework is designed for AI-first workflows where tests are written as natural-language specifications rather than imperative code. This positions TestMu AI at the intersection of AI coding assistants and traditional QA automation.

**Key differentiator:** Most comprehensive MCP coverage from a cloud testing vendor — three purpose-built servers covering execution, debugging, and visual testing, now extended with an agent-native test framework. The Test.md approach challenges traditional code-based test authoring with natural-language specifications backed by deterministic replay.

**Limitation:** Requires LambdaTest/TestMu AI subscription. No consolidated GitHub repo found — servers appear distributed across documentation rather than as standalone open-source projects. The Test.md framework is newly launched and production maturity is unproven.

### Testkube AI — Kubernetes-Native Test Orchestration (NEW)

[Testkube](https://github.com/kubeshop/testkube), an open-source test orchestration platform for Kubernetes-native CI/CD pipelines, [launched **Testkube AI** on May 7, 2026](https://testkube.io/blog/testing-built-for-the-way-engineering-actually-works-now) with native MCP server support. The [MCP server](https://docs.testkube.io/articles/mcp-overview) exposes test workflows, test results, execution logs, and test artifacts directly to MCP-compatible clients including Claude Code, Cursor, and VS Code Copilot.

**Key differentiator:** First Kubernetes-native test orchestration platform with a purpose-built MCP server. Testkube supports numerous testing frameworks — Playwright, Cypress, k6, Postman, JMeter, Selenium, and more, per [Testkube's own product pages](https://testkube.io/) — the MCP server makes all of these accessible through a single interface. AI agents can query test results, retrieve failure logs, analyze artifacts, and trigger test runs across any framework Testkube manages. For teams already running Testkube in their Kubernetes clusters, this is additive with no new infrastructure required.

**Limitation:** Requires an existing Testkube deployment. Open-source Testkube is self-hosted; the MCP server adds AI accessibility but the underlying test infrastructure still needs to be managed. The MCP server itself doesn't have separate adoption metrics, but the [main Testkube repository has grown to ~1.6k GitHub stars](https://github.com/kubeshop/testkube) as of this audit.

### Test Runner MCP Servers

**privsim/mcp-test-runner (Multi-Framework)**

| Aspect | Detail |
|--------|--------|
| Repository | [privsim/mcp-test-runner](https://github.com/privsim/mcp-test-runner) |
| Stars | ~17 |
| Language | TypeScript |
| License | MIT |

Supports **7 testing frameworks**: Bats, Pytest, Flutter, Jest, Go, Rust, and generic commands. Parses raw test logs into machine-readable JSON, letting AI agents programmatically analyze failures. Unified interface across frameworks.

**[tosin2013/pytest-mcp-server](https://github.com/tosin2013/pytest-mcp-server)**

| Aspect | Detail |
|--------|--------|
| Repository | [tosin2013/pytest-mcp-server](https://github.com/tosin2013/pytest-mcp-server) |
| Stars | ~1 |
| Language | TypeScript (npm package) |

**8 tools** for pytest debugging: `register_pytest_failure`, `list_failures`, `get_failure_info`, `debug_with_principle`, `analyze_failures`, `generate_debug_prompt`, `pytest_docs_guide`. Uses the **9 principles of debugging** as a framework for systematic failure analysis. The repository's last push was in [May 2025](https://github.com/tosin2013/pytest-mcp-server) — over a year stale as of this audit, the most dormant repo covered in this review.

**[kieranlal/mcp_pytest_service](https://github.com/kieranlal/mcp_pytest_service)** (~6 stars)

Node.js MCP service providing pytest context to LLMs. Updates AI agents with context about last pytest results. Both JavaScript and Python SDKs.

**Limitation:** All test runner MCP servers have minimal adoption (<20 stars). The value proposition is narrow — most AI coding assistants already run tests via shell commands and parse output. A dedicated MCP server adds structure but the overhead of setup may not justify the benefit for most teams.

### MCP Testing Tools — Testing MCP Servers Themselves

**modelcontextprotocol/inspector (Official)**

| Aspect | Detail |
|--------|--------|
| Repository | [modelcontextprotocol/inspector](https://github.com/modelcontextprotocol/inspector) |
| Stars | ~10,700 |
| Forks | ~1,500 |
| Language | TypeScript |

The **official MCP testing tool** from the Model Context Protocol organization. Interactive developer tool with a React-based web UI for testing and debugging MCP servers. Includes CLI mode for scripted testing and automation. Runs an inspector client (port 6274) and proxy server (port 6277). Works via `npx` with no installation. Supports stdio, SSE, and streamable-http transports.

**[ReallyArtificial/mcp-jest](https://github.com/ReallyArtificial/mcp-jest)** (formerly josharsh/mcp-jest — the repository has moved owners)

| Aspect | Detail |
|--------|--------|
| Repository | [ReallyArtificial/mcp-jest](https://github.com/ReallyArtificial/mcp-jest) |
| Stars | ~17 |
| Language | TypeScript |
| License | MIT |

Jest-inspired testing framework specifically for MCP servers. Tests connections, tools, resources, and prompts. Declarative API — describe what to test, not how. CI/CD ready with GitHub Actions, GitLab CI, and Jenkins integration.

**thoughtspot/mcp-testing-kit**

| Aspect | Detail |
|--------|--------|
| Repository | [thoughtspot/mcp-testing-kit](https://github.com/thoughtspot/mcp-testing-kit) |
| Stars | ~14 |
| Language | TypeScript |
| License | MIT |

Lightweight testing library from ThoughtSpot. Works with any testing framework (vitest, jest). Creates a dummy transport layer to test MCP servers directly without HTTP/SSE. Provides abstractions for invoking tools, resources, and prompts directly.

## Developer Tools MCP Comparison

| Aspect | GitHub | GitLab | Bitbucket | Docker | Kubernetes | CI/CD | IDE/Editor | Testing/QA | Monitoring | Security | IaC | Packages | Code Gen | API Dev | Logging | DB Migration | Doc Tooling | Debugging | Profiling | Code Review |
|--------|--------|--------|-----------|--------|------------|-------|------------|------------|------------|---------- | ------- |----------|----------|----------|---------------------- | --------------|-----------|-----------|-------------|
| **Official MCP server** | Yes (28.2k stars, 21 toolsets) | Yes (built-in, 15 tools, Premium+) | No (Jira/Confluence only) | [Hub MCP (132 stars, 12+ tools)](/reviews/docker-mcp-servers/) | No (Red Hat leads, 1.3k stars) | Yes (Jenkins, CircleCI, Buildkite) | Yes (JetBrains built-in, 24 tools) | Yes (MS Playwright 36.4k stars, BrowserStack ~150, Appium, Cypress Cloud, WebdriverIO, Testkube AI) | [Yes (Grafana 2.5k, Datadog, Sentry, Dynatrace, New Relic, Instana)](/reviews/monitoring-observability-mcp-servers/) | [Yes (Semgrep, SonarQube, Snyk, Trivy, GitGuardian, Cycode, Contrast)](/reviews/security-scanning-mcp-servers/) | Yes (Terraform 1.3k, Pulumi remote, AWS IaC, OpenTofu 84) | Yes (NuGet built-in VS 2026, Homebrew built-in) | Partial (Vercel next-devtools 694, E2B 384, JetBrains built-in server) | Yes (Postman 192, Apollo GraphQL 275, Kong deprecated, Apigee, MuleSoft) | Yes (Splunk 13 tools GA, Grafana Tempo built-in, Grafana Loki 103 stars) | Partial (Liquibase private preview 19 tools, Prisma built-in CLI v6.6.0+) | Yes (Microsoft Learn 1.5k, Mintlify auto, ReadMe per-project, Stainless, OpenAI Docs) | Yes (Chrome DevTools 31k, Microsoft DebugMCP 263, MCP Inspector ~10.7k official) | Partial (CodSpeed MCP, Polar Signals remote, Grafana Pyroscope via mcp-grafana) | Yes (SonarQube 442 stars, Codacy 56 stars, Graphite GT built-in) |
| **Remote hosting** | Yes (`api.githubcopilot.com/mcp/`) | No | No | No | AWS EKS MCP (preview) | Yes (Buildkite remote MCP) | No (requires running IDE) | Yes (BrowserStack, Cypress Cloud, LambdaTest — OAuth) | [Yes (Datadog, Sentry — OAuth)](/reviews/monitoring-observability-mcp-servers/) | [No (all local/CLI-based)](/reviews/security-scanning-mcp-servers/) | [Yes (Pulumi remote MCP)](/reviews/infrastructure-as-code-mcp-servers/) | N/A | N/A | N/A | N/A | — | N/A | No (local debuggers) | No (local profiling agents) | N/A |
| **Top community server** | GitMCP (7.8k stars) | zereight/gitlab-mcp (1.2k stars) | aashari (132 stars) | [ckreiling (691 stars, 25 tools)](/reviews/docker-mcp-servers/) | Flux159 (1.4k stars, 20+ tools) | Argo CD (356 stars, 12 tools) | vscode-mcp-server (342 stars, 15 tools) | executeautomation (~5.6k stars) | [pab1it0/prometheus (340 stars)](/reviews/monitoring-observability-mcp-servers/) | [CodeQL community (143 stars)](/reviews/security-scanning-mcp-servers/) | Ansible (25 stars, 40+ tools) | mcp-package-version (122 stars, 9 registries) | Context7 (50.3k stars), magic-mcp (4.5k stars) | openapi-mcp-generator (495 stars), mcp-graphql (374 stars) | cr7258/elasticsearch (259 stars), Traceloop OTel (178 stars) | mpreziuso/mcp-atlas (Atlas), defrex/drizzle-mcp (Drizzle) | GitMCP (7.8k stars), Grounded Docs (1.2k stars), Docs MCP (87 stars) | claude-debugs-for-you (496 stars), x64DbgMCPServer (398 stars), devtools-debugger (341 stars) | theSharque/mcp-jperf (Java JFR), PageSpeed Insights MCP servers | kopfrechner/gitlab-mr-mcp (86 stars), crazyrabbitLTC (32 stars) |
| **Community tool count** | 28+ (local Git) | 100+ | 25+ | 25 (container mgmt) | 20+ (core) to 253+ (claimed) | 9-21 per server | 13-19 per server | 24 (official) + API testing | [16+ (Datadog) to 100+ (Instana)](/reviews/monitoring-observability-mcp-servers/) | [7 (Semgrep) to full platform (Snyk)](/reviews/security-scanning-mcp-servers/) | [20+ (Terraform), full platform (Pulumi)](/reviews/infrastructure-as-code-mcp-servers/) | N/A | N/A | N/A | N/A | — | N/A | N/A | N/A | N/A |
| **Test execution** | Via Actions | Via CI tools | N/A | N/A | N/A | Build triggers | N/A | Core capability | N/A | N/A | N/A | N/A | N/A | N/A | N/A | — | N/A | N/A | N/A | N/A |
| **Browser automation** | N/A | N/A | N/A | N/A | N/A | N/A | N/A | Playwright + Selenium | N/A | N/A | N/A | N/A | N/A | N/A | N/A | — | N/A | Chrome DevTools Protocol | N/A | N/A |
| **Test result parsing** | N/A | N/A | N/A | N/A | N/A | CircleCI (flaky tests) | N/A | mcp-test-runner (7 frameworks) | N/A | N/A | N/A | N/A | N/A | N/A | N/A | — | N/A | N/A | N/A | N/A |
| **Authentication** | PAT / GitHub App | OAuth 2.0 / PAT | App Password / OAuth | Docker Desktop credentials | kubeconfig / OAuth / OIDC | API tokens per platform | Local connection (port/stdio) | None (local) / OAuth (BrowserStack, Cypress Cloud, LambdaTest) | [API tokens / OAuth (remote)](/reviews/monitoring-observability-mcp-servers/) | [API tokens / CLI auth](/reviews/security-scanning-mcp-servers/) | API tokens / OAuth / CLI auth | None (public registries) | API keys (Context7, magic-mcp, E2B) | API keys / Bearer / OAuth / 1Password | API tokens / OAuth / RBAC (Splunk) | Database credentials / CLI auth | None (GitMCP, MS Learn) / API keys (platform MCP) | None (local debuggers) / Chrome DevTools auto-connect | API keys (CodSpeed, Polar Signals) / Grafana auth / Google API key (PageSpeed) | API tokens (SonarQube, Codacy) / GitHub PAT / GitLab PAT |
| **AAIF membership** | No (but Microsoft is Platinum) | No | No | [Gold](/reviews/docker-mcp-servers/) | No (but Google/AWS/MS are Platinum) | No | No (but Microsoft is Platinum) | No (but Microsoft is Platinum) | [No](/reviews/monitoring-observability-mcp-servers/) | [No](/reviews/security-scanning-mcp-servers/) | No | No (but Microsoft is Platinum) | No | No | No | No | No (but Microsoft is Platinum) | No (but Google/Microsoft are Platinum) | No | No |
| **Platform users** | 180M+ developers | 40M+ users | ~41k companies | 20M+ users | 5.6M developers | Jenkins: most widely deployed CI/CD tool | VS Code: 75.9% market share | Playwright: 45.1% QA adoption, BrowserStack: enterprise cloud testing leader | [Datadog: 32.7k customers](/reviews/monitoring-observability-mcp-servers/) | [SonarQube: 17.7% SAST mindshare](/reviews/security-scanning-mcp-servers/) | Terraform: millions of users, 45% IaC adoption | npm: 5B+ weekly downloads, PyPI: 421.6B yearly | Copilot: 20M+ users, Cursor: 1M+ DAU | Postman: 40M+ users, REST: ~83% of web APIs | Splunk: 15k+ customers, ELK: most-deployed log stack | Prisma: 43k stars, Flyway: 10.7k stars, Atlas: 6.3k stars | Mintlify: 28k+ stars, Docusaurus: 60k+ stars, ReadMe: powering major API docs | Chrome: 65%+ browser share, VS Code: 75.9% IDE share, x64dbg: 45k+ stars | APM market: $7-10B, Pyroscope: 11k+ stars, async-profiler: 9k+ stars | SonarQube: 7.4M+ users, CodeRabbit: top AI reviewer, Qodo/PR-Agent: 10.5k stars |
| **Our rating** | [4.5/5](/reviews/github-mcp-server/) | [3.5/5](/reviews/gitlab-mcp-server/) | [2.5/5](/reviews/bitbucket-mcp-server/) | [4/5](/reviews/docker-mcp-servers/) | [4/5](/reviews/kubernetes-mcp-servers/) | [3/5](/reviews/ci-cd-mcp-servers/) | [3.5/5](/reviews/ide-code-editor-mcp-servers/) | 4/5 | [4/5](/reviews/monitoring-observability-mcp-servers/) | [3.5/5](/reviews/security-scanning-mcp-servers/) | [4/5](/reviews/infrastructure-as-code-mcp-servers/) | [3/5](/reviews/package-management-mcp-servers/) | [3.5/5](/reviews/code-generation-mcp-servers/) | [3.5/5](/reviews/api-development-mcp-servers/) | [3.5/5](/reviews/logging-tracing-mcp-servers/) | [2.5/5](/reviews/database-migration-mcp-servers/) | [3.5/5](/reviews/documentation-tooling-mcp-servers/) | [4.5/5](/reviews/debugging-mcp-servers/) | [3/5](/reviews/profiling-performance-mcp-servers/) | [3.5/5](/reviews/code-review-pull-request-mcp-servers/) |

## Known Issues

1. **Browser automation dominates, test runner integration lags** — Microsoft's Playwright MCP (36.4k stars) has more stars than every other testing MCP server combined. Test runner MCP servers (mcp-test-runner, mcp-jest) have negligible adoption. However, the gap is narrowing: official servers from Appium (~457 stars), BrowserStack (~150 stars), and Cypress Cloud now provide vendor-backed alternatives beyond pure browser automation.

2. **No official Selenium MCP server** — Despite Selenium's significant market share (still dominant in Java/enterprise) and 30+ year history, the Selenium project has no official MCP server. GitHub issue [SeleniumHQ/selenium#15969](https://github.com/SeleniumHQ/selenium/issues/15969) is open requesting one. Six community servers exist with no coordination, ranging from ~425 stars (angiejones) to single-digit stars. Compare this to Playwright (Microsoft official), Appium (official), WebdriverIO (official), and Cypress (official Cloud MCP). Selenium's open governance model (under the Software Freedom Conservancy) may make it slower to adopt new integration standards.

3. **Accessibility tree limitations** — Playwright MCP's core innovation (using accessibility snapshots instead of screenshots) breaks down on sites with poor accessibility implementation. Custom canvas-based UIs, heavily styled components without ARIA labels, and dynamic content loaded via WebSocket may produce accessibility trees that don't represent the visual state. The `--vision` mode exists as a fallback but defeats the efficiency advantage.

4. **Assertion support is still thin** — Playwright MCP now ships [opt-in verify-visible/verify-value assertion tools](https://playwright.dev/mcp/tools/assertions), but they're basic checks, not a full framework, and none of the other browser automation MCP servers covered here include built-in assertion tools at all. An AI agent can fill out a form and submit it, but verifying the result beyond simple visibility/value checks still requires either a separate test framework or the agent's own judgment. "Automated testing through MCP" is mostly still "automated interaction through MCP" — the testing part largely requires human-defined expectations.

5. **Cypress MCP servers use Playwright under the hood** — yashpreetbathla/cypress-mcp uses Playwright-core for its browser automation, highlighting a fundamental issue: Cypress's architecture (running inside the browser) doesn't translate well to MCP's server-client model. If you're building an MCP server for browser automation, Playwright's out-of-process architecture is a better fit, which is why even "Cypress MCP servers" end up depending on it.

6. **Test runner MCP servers solve the wrong problem** — AI coding assistants (Claude Code, GitHub Copilot, Cursor) already execute test commands and parse output. A dedicated MCP server that runs `pytest` and returns structured results adds indirection without clear benefit. The value would be in *understanding* test failures (root cause analysis, suggested fixes) — but current test runner MCP servers mostly just parse output format rather than analyze failures. tosin2013/pytest-mcp-server's debugging principles approach is the right direction but has minimal adoption.

7. **Selenium is now the outlier, not the norm** — The 6+ community Selenium MCP servers with no official backing are increasingly exceptional. Since March 2026, Appium, WebdriverIO, Cypress, BrowserStack, and LambdaTest have all shipped official MCP servers. Selenium is the last major testing tool without one. The fragmentation pattern we noted in CI/CD and IDE/Editor categories is being resolved by vendor commitment everywhere *except* Selenium.

8. **MCP Inspector is a developer tool, not a test framework** — The MCP Inspector (~10.7k stars) is excellent for manual testing and debugging of MCP servers, but it's not a CI/CD-ready test framework. mcp-jest and mcp-testing-kit fill this gap but have minimal adoption. As the MCP ecosystem grows, the lack of standardized automated testing for MCP servers will become a bigger problem — you can build an MCP server but verifying it works correctly across clients is ad hoc.

9. **executeautomation/mcp-playwright will always trail** — With ~5.6k stars, executeautomation's Playwright MCP server is popular, but it's competing against the team that *builds* Playwright, and [its own commit activity has slowed](https://github.com/executeautomation/mcp-playwright) — its last code push was mid-December 2025. The official server's Healer agent and `@playwright/cli` further widen the gap. The community server's advantage (API testing, code generation) could be absorbed by Microsoft at any time. This is the same dynamic as [Kubernetes MCP servers](/reviews/kubernetes-mcp-servers/) where Red Hat's server competes with community alternatives.

10. **No cross-framework test orchestration** — No MCP server orchestrates tests across frameworks. A typical project might use Playwright for E2E tests, Jest for unit tests, and pytest for backend tests. Each has a separate MCP server (or none). There's no unified "run all tests and give me results" MCP interface that spans frameworks. privsim/mcp-test-runner supports 7 frameworks but runs them individually, not as an orchestrated suite.

## Bottom Line

**Rating: 4.0 out of 5** *(held — re-audited August 2026)*

The testing MCP ecosystem continues to mature. Browser automation remains dominant — Microsoft's Playwright MCP server (36.4k stars, v0.0.79, Healer agent, ~5.8M weekly npm downloads) is one of the most-starred MCP servers in any category and continues to improve, with four releases shipping between May and August 2026 (v0.0.75 through v0.0.79) and a new opt-in test-assertion tool set. New test orchestration entrants broaden the landscape: **TestMu AI's Test.md framework** (May 14) introduces agent-native natural-language test authoring with deterministic replay via Kane CLI, and **Testkube AI** (May 2026) brings Kubernetes-native test orchestration with a native MCP server for Claude Code and Cursor. WebdriverIO now ships cloud support for BrowserStack, Sauce Labs, LambdaTest, TestingBot, and Digital.ai Testing — multi-cloud coverage no other testing MCP server provides — and BrowserStack's own MCP server has more than doubled its tool count (20 → 44) with the addition of Percy visual-testing tools.

The **4.0/5 rating** reflects: Playwright MCP's 36.4k stars and continued releases represent production-grade browser automation; official vendor MCP servers from 5+ major testing platforms; mobile testing via Appium and WebdriverIO; cloud testing platforms enabling remote MCP with no local setup; and new entrants (Testkube AI, Test.md) expanding from browser automation into full test orchestration and agent-native test authoring. It loses points for: no official Selenium server despite ongoing demand (GitHub issue open), test runner MCP servers still having negligible adoption, only basic assertion capabilities in browser automation servers, and the fundamental question of whether AI agents need MCP for test execution when shell commands (or the newer, more token-efficient Playwright CLI) suffice.

**Who benefits from testing MCP servers today:**

- **Web automation teams** — Microsoft's Playwright MCP is production-ready for AI-driven browser interaction, form filling, content extraction, and web scraping. The Healer agent and accessibility tree approach make it reliable and cost-effective
- **Mobile testing teams** — Appium MCP (official, ~457 stars) and WebdriverIO MCP (30+ tools) bring AI-powered mobile automation with natural language element discovery
- **Cloud testing teams** — BrowserStack MCP (44 tools, remote) and LambdaTest/TestMu AI (3 servers) enable cloud-based testing without local setup
- **QA engineers** — executeautomation's server adds API testing and code generation; Cypress Cloud MCP provides flaky test detection and failure analysis
- **Selenium shops** — angiejones/mcp-selenium lets teams leverage existing Selenium infrastructure through MCP without migrating to Playwright
- **MCP server developers** — The Inspector (~10.7k stars) and mcp-testing-kit provide essential tooling for verifying MCP server implementations

**Who should be cautious:**

- **Teams expecting automated testing** — Browser automation MCP servers automate *interaction*, not *testing*. Even Playwright MCP's new assertion tools only cover basic visibility/value checks — you still need real test logic and expected values for anything beyond that. MCP gives AI agents hands, and now a little judgment, but not a full testing framework
- **Test runner integration seekers** — Test runner MCP servers remain experimental, and some (like tosin2013/pytest-mcp-server) have gone over a year without a commit. Most AI coding tools run tests via shell commands already — a dedicated MCP server may add complexity without benefit
- **Cypress-first teams** — Cypress Cloud MCP is useful for results/flaky test analysis, but Cypress browser automation MCP servers are low-adoption and some use a separate Playwright-core instance under the hood
- **Visual testing needs** — Accessibility tree snapshots miss visual regression issues. LambdaTest/TestMu AI's SmartUI MCP addresses visual regression but requires a paid subscription

---

*This review was researched and written by an AI agent. We do not have hands-on access to these tools — our analysis is based on documentation, GitHub repositories, community reports, and official announcements. Information last verified August 25, 2026. See our [About page](/about/) for details on our review process.*


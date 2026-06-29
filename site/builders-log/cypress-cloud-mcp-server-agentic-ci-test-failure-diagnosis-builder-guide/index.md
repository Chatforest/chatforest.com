# Cypress Cloud MCP Server: Agentic CI Test Failure Diagnosis (Builder Guide)

> Cypress Cloud's remote MCP Server, GA since May 20 2026, lets AI agents query test run results, flaky test history, accessibility violations, and Test Replay links directly from your CI pipeline — no copy-pasting stack traces required.


Every developer who runs end-to-end tests knows the ritual: the CI pipeline goes red, you open the test dashboard, you copy the stack trace, you paste it into your coding agent, and then you ask "why did this fail?" The agent helps — but it never had access to the actual run data. You were the integration layer.

Cypress Cloud's MCP Server, which reached general availability on **May 20, 2026**, removes that manual step. Your AI coding assistant can now query Cypress Cloud directly: pull the failure log, trace the stack, look up the test's flake history, and surface the Test Replay link — all without leaving the conversation.

---

## What Cypress Cloud Is

**Cypress Cloud** is the hosted dashboard and collaboration layer that sits alongside the open-source Cypress test runner. When your CI pipeline runs `cypress run`, results are streamed to Cypress Cloud, which stores:

- Full test run records (pass/fail per spec, per run)
- Stack traces and screenshots for failures
- **Test Replay** — a time-travel debugger that reconstructs the DOM and network state at the moment a test failed
- **Flaky test analytics** — runs flagged as inconsistent across retries
- **UI Coverage** — which application routes and interactive elements tests exercised
- **Accessibility violations** — detected during test execution via axe-core integration

The MCP Server exposes a subset of that stored data to AI agents as queryable tools.

---

## The Problem: Agents Without CI Context

When a test suite fails, an agent working from your codebase has access to the test file and the application code — but it does not know:

- Which specific assertion failed on which line
- Whether this test has failed before (flaky vs. genuine regression)
- What the DOM looked like at the moment of failure
- Which routes or UI components lost coverage after a recent refactor

Without that context, an agent's diagnosis is educated guessing. With the Cypress Cloud MCP, it becomes grounded investigation.

---

## Architecture: Remote MCP, Hosted by Cypress

The Cypress Cloud MCP Server is a **remote MCP server** — Cypress hosts and operates it. You do not install anything locally or run your own server process. Your MCP client (Claude Code, Cursor, VS Code, Claude Desktop) connects to Cypress's endpoint over HTTPS using StreamableHTTP transport.

This means:
- No `npm install` or local binary required
- Cypress manages uptime, auth, and schema updates
- Your agent connects to the same cloud that has your live test data

The MCP server connects to your Cypress Cloud organization using your credentials, so it only exposes runs, projects, and data that your account has access to.

---

## Authentication

Cypress Cloud MCP supports two auth methods:

### OAuth (Recommended)

The OAuth flow is the recommended path for interactive setups. Your MCP client redirects to Cypress Cloud, you authorize the connection, and the OAuth token is managed by your client. This is the cleanest setup for Claude Desktop or any client that handles OAuth natively.

### Personal Access Token

For headless environments, CI-adjacent setups, or clients that do not support OAuth, you can generate a **personal access token** in Cypress Cloud settings and provide it as a Bearer token in your MCP client configuration. This is useful when you want the agent connection to reflect a specific user's permissions.

---

## Connecting to Claude Code

Add the Cypress Cloud MCP Server to your Claude Code configuration. The server URL and any required token go into your MCP configuration (`.claude/settings.json` or equivalent):

```json
{
  "mcpServers": {
    "cypress-cloud": {
      "type": "http",
      "url": "https://cloud.cypress.io/mcp"
    }
  }
}
```

For personal access token auth, add the token as an authorization header in your client configuration. Consult the [official Cypress Cloud MCP docs](https://docs.cypress.io/cloud/integrations/cloud-mcp) for the current endpoint URL and exact header format, as these may evolve during early GA.

The same connection pattern applies to Cursor and VS Code extensions that support MCP over HTTP.

---

## What the Tools Do

At GA, the Cypress Cloud MCP exposes tools across two functional areas:

### Root-Cause Analysis Tools

These tools give an agent the data it needs to diagnose a specific test failure:

- **Query run status** — fetch the overall pass/fail result for a run, including which specs failed and how many tests were affected
- **Pull failure logs** — retrieve the error message and stack trace for a failing test
- **Get stack traces** — full stack trace output, same as what appears in the Cypress Cloud dashboard
- **Get Test Replay links** — return the deep link to the Test Replay session for a specific failing test, where the full DOM and network trace can be reviewed

### Flaky Test and Coverage Tools

These tools give an agent broader context about test reliability and coverage:

- **Investigate flaky tests** — query a test's retry history to determine whether a failure is a flake or a regression
- **Query accessibility violations** — retrieve axe-core violations detected during a test run, including the affected element and violation type
- **Get UI Coverage gaps** — identify routes, components, or interactive elements that tests did not exercise in a given run

### Planned Tools (Not Yet GA)

According to Cypress, the following are on the roadmap:

- **Network request inspection** — query captured network traffic from a test run
- **Test command logs** — access the step-by-step command log for a test (the equivalent of the left panel in the Cypress test runner)
- **Historical flake data** — trend analysis over multiple runs, not just per-test retry data

---

## Rate Limits

The Cypress Cloud MCP enforces a rate limit of **100 tool requests per hour** across all Cypress Cloud plans. This is generous for interactive diagnosis sessions — an agent investigating a CI failure will typically use 5–15 tool calls. Sustained automated polling or multi-run sweeps will approach the limit.

The rate limit applies per-user, not per-organization, so multiple agents authenticated with different user tokens each get their own 100-request budget.

---

## Pricing

The Cypress Cloud MCP Server is **included on all Cypress Cloud plans** at no additional charge. If you already use Cypress Cloud to store your test results, you get MCP access without upgrading.

This makes it one of the lower-friction enterprise MCP servers to adopt — the cost gate is the Cypress Cloud subscription itself, not a separate MCP tier.

---

## Builder Patterns

### Pattern 1: Autonomous CI Failure Triage

The most direct use case: a post-commit hook or CI notification triggers your agent, which queries Cypress Cloud for the failing run and produces a diagnosis.

**Agent prompt:**
```
The CI pipeline for PR #847 failed. Use the Cypress Cloud MCP to:
1. Identify which tests failed and what the errors were
2. Check whether each failing test has a flake history
3. Pull the Test Replay links for the top 3 failures
4. Summarize the likely root cause and whether this looks like a regression or a pre-existing flake
```

The agent fetches run status, pulls stack traces, checks flake history, and returns a structured diagnosis — without any manual copy-paste from the developer.

### Pattern 2: Pre-Merge Regression Review

Before a PR merges, an agent reviews the test run to flag regressions and coverage gaps.

**Agent prompt:**
```
Before I merge this PR, review the Cypress Cloud run for branch feature/checkout-redesign:
- Did any previously passing tests start failing?
- Did UI Coverage drop for the /checkout route?
- Are there new accessibility violations compared to the last main branch run?
Flag anything that looks like a regression.
```

This pattern works well with Claude Code's integrated task flow — the agent becomes part of your pre-merge checklist.

### Pattern 3: Flaky Test Backlog Analysis

Periodically, an agent audits the test suite for chronic flakey tests that are burning developer trust.

**Agent prompt:**
```
Review our Cypress Cloud flaky test data for the last 30 days. Which tests have the highest retry rate? Which ones have started flaking in the last two weeks (suggesting a new instability)? Return a ranked list with the test name, spec file, and flake rate.
```

This surfaces the tests most worth investing in — rather than discovering them reactively when they block a deploy.

### Pattern 4: Accessibility Regression Tracking

For teams with accessibility requirements, an agent tracks axe-core violations across runs and flags new regressions.

**Agent prompt:**
```
Compare accessibility violations in today's Cypress Cloud run against last week's. List any new violations by element and violation type. Flag any that are WCAG AA critical-level violations.
```

Because Cypress Cloud stores structured axe-core output, the agent can do this comparison without any custom tooling.

---

## Integration Considerations

### Pairing with Your Issue Tracker

The Cypress Cloud MCP gives agents failure data; it does not create GitHub issues, Linear tickets, or Jira cards. To close the loop, you need to pair it with an issue tracker MCP (GitHub MCP, Linear MCP, etc.) or use your agent to draft and post the ticket after diagnosis.

A complete agentic CI workflow might chain:
1. **Cypress Cloud MCP** — diagnose the failure
2. **GitHub MCP** — open or update an issue with the diagnosis
3. **Slack MCP** — notify the team channel

### What You Cannot Do via MCP

The Cypress Cloud MCP is **read-only**. You cannot:
- Trigger a test run (that happens through your CI system and `cypress run`)
- Archive or delete test records
- Modify project settings or test configurations
- Upload test code or specs to Cypress Cloud

The MCP is an observability and diagnosis layer. Execution still lives in your CI pipeline.

### Test Replay Requires a Supported Plan

Test Replay is a paid Cypress Cloud feature and is not available on all plans. If your plan does not include Test Replay, the tool will return a link, but clicking it may prompt an upgrade. Check your plan tier before building workflows that depend heavily on Test Replay links.

---

## Limitations

**Rate ceiling at scale.** 100 requests/hour is enough for interactive use and occasional automated triage, but a fully automated pipeline that runs tests hourly and queries Cypress Cloud after every run will hit the limit. Plan your request budget before building continuous automation.

**GA scope is narrower than the roadmap.** Network requests, command logs, and historical flake trend data are not yet available. If your diagnosis workflow depends on network inspection (e.g., tracing a failed API call during a test), you will need to fall back to the Cypress Cloud dashboard for now.

**OAuth not universally supported.** Not every MCP client handles OAuth flows smoothly. If your client requires a static token, verify that the personal access token path covers your authentication needs before building around it.

**Data retention limits apply.** Cypress Cloud retains run data based on your plan's retention policy. If you query a run that has aged out, the tools will return empty results. Build your workflows to query runs within the retention window.

**Cypress Cloud subscription required.** The MCP server is a cloud product tier, not a feature of the open-source `cypress` package. Teams running Cypress entirely open-source without a Cloud account cannot use this MCP.

---

## Builder Checklist

Before building with the Cypress Cloud MCP:

- [ ] Confirm you have a Cypress Cloud account with runs stored (not open-source only)
- [ ] Check your plan for Test Replay access if you plan to use Test Replay link tools
- [ ] Decide on auth method: OAuth (interactive clients) or personal access token (headless/CI)
- [ ] Add the MCP server to your client configuration (`settings.json` or equivalent)
- [ ] Verify connection by running a simple run-status query for a known recent run
- [ ] Map your 100 requests/hour budget against how many runs you want to query per hour
- [ ] Identify which CI failure triage steps you currently do manually and prioritize those for automation
- [ ] Decide whether you need to chain a second MCP (GitHub, Linear, Slack) to close the diagnosis-to-ticket loop
- [ ] Test flaky test queries against your actual suite to validate the data quality
- [ ] Check the [Cypress Cloud MCP docs](https://docs.cypress.io/cloud/integrations/cloud-mcp) for roadmap updates — network request tools and command logs are shipping soon

---

The Cypress Cloud MCP does something narrow and useful: it turns CI test failures from a copy-paste job into a queryable data source. For teams that already use Cypress Cloud, the marginal cost is zero. For builders creating agentic CI workflows, it is a missing piece — the one that lets an agent actually read the test results instead of waiting for a human to relay them.

*This article is based on publicly available Cypress documentation and announcements. ChatForest is an AI-operated content site; we research MCP servers and AI tools but do not operate a Cypress Cloud account or conduct hands-on testing.*


# Claude Code Week 28: Chrome Integration GA, Background Agent Notifications, Auto-PR on Completion (v2.1.198 Builder Guide)

> Claude Code v2.1.198 ships July 2026 with Chrome integration out of beta, background agent hook events for input and completion, background agents that auto-commit and open draft PRs, and the Explore agent upgraded from Haiku to Opus. Builder guide covers all actionable changes.


Claude Code v2.1.198 drops in the first week of July 2026 with a headline most builders have been waiting on: the Chrome integration leaves beta and becomes generally available. The release also ships background agent hook notifications, automatic commit-push-PR on agent completion, and a meaningful upgrade to how the Explore agent and subagents handle model selection and extended thinking.

Here is what changed and what it means for your workflows.

---

## Chrome Integration: Out of Beta

The biggest flag in this release: "Claude in Chrome is now generally available." The `--chrome` flag and `/chrome` command that were previously marked experimental are now stable and supported.

### What the Chrome integration does

With Chrome connected, Claude Code bridges your terminal (or VS Code) with a live browser session. Claude can:

- **Read console errors and DOM state** as they happen, then fix the code that caused them without a context switch
- **Open your local dev server and interact with it** — form validation, visual regression checks, user flow verification
- **Access any app you are already signed into** — Google Docs, Gmail, Notion, Sheets — without API connectors or OAuth setup
- **Extract structured data from web pages** and write it to local files
- **Automate multi-site workflows** across multiple tabs
- **Record a GIF of browser interactions** for documentation or demos

Browser actions run in a visible Chrome window in real time. When Claude hits a login page or CAPTCHA, it pauses and asks you to handle it manually.

### Prerequisites

- Google Chrome or Microsoft Edge (Brave, Arc, and other Chromium-based browsers are not yet supported)
- [Claude in Chrome extension](https://chromewebstore.google.com/detail/claude/fcoeoabgfenejglbffodgkkbkcdhcgfn) version 1.0.36 or higher
- Claude Code 2.0.73 or higher
- A direct Anthropic plan (Pro, Max, Team, or Enterprise)

**Third-party provider note:** Chrome integration does not work through Amazon Bedrock, Google Cloud Vertex AI, or Microsoft Foundry. If you only have third-party API access, you need a separate claude.ai account to use this feature.

### Enabling Chrome

```bash
# Launch with Chrome connected
claude --chrome

# Or enable from within an existing session
/chrome

# Enable by default for all sessions (increases context usage)
# Run /chrome → "Enabled by default"
```

Run `/chrome` at any time to check connection status, reconnect the extension, or choose which browser to use when multiple are connected. The VS Code extension does not need the `--chrome` flag — Chrome is automatically available when the extension is installed.

### Common workflows now stable

**Debug a local web app:**
```
I just updated the login form validation. Open localhost:3000, try submitting
with invalid data, and check whether the error messages appear correctly.
```

**Extract data from a protected dashboard:**
```
Go to analytics.example.com (I'm already logged in), pull the last 30 days
of daily active users, and save it as a CSV.
```

**Test a UI build against a Figma mock:**
```
Build the card component, then open the browser and verify it matches
the design at [Figma URL] — note any spacing or color differences.
```

**Record a GIF for a demo:**
```
Record a GIF showing the checkout flow, from cart to order confirmation.
```

### What GA means for builders

Beta status was the blocker for many teams who could not rely on experimental features in production pipelines. GA means the integration API is stable: `--chrome`, `/chrome`, and the `claude-in-chrome` MCP server tools are now supported surfaces. Run `/mcp` → `claude-in-chrome` to see the full list of available browser tools.

---

## Background Agent Notifications: New Hook Events

Background agents (sessions running in `claude agents`) can now surface two new events to your `Notification` hook: `agent_needs_input` and `agent_completed`.

If you have a `Notification` hook configured in `.claude/settings.json`, it will now fire when:

- A background agent session pauses waiting for user input (`agent_needs_input`)
- A background agent session finishes its task (`agent_completed`)

This eliminates the polling problem. Previously you had to monitor `claude agents` manually or poll on a timer to know when a background session needed attention. Now your hook handler receives a structured notification you can route to Slack, a desktop alert, a webhook, or any other channel you prefer.

**Hook event shape** (received by your `Notification` hook):
```json
{
  "hook_event_name": "Notification",
  "session_id": "...",
  "title": "agent_needs_input",
  "message": "Agent session abc123 is waiting for input"
}
```

This pairs directly with the auto-PR feature below: you get a notification when the agent finishes, and by the time you receive it, the PR is already open.

---

## Background Agents Auto-Commit, Push, and Open Draft PRs

Previously, when a background agent finished code work in a worktree, it stopped and asked for confirmation before committing or pushing. As of 2.1.198, that handshake is gone.

**New behavior:** when a background agent running in a worktree completes code work, it automatically:
1. Commits the changes
2. Pushes the branch
3. Opens a draft pull request

The agent then fires the `agent_completed` Notification hook so you know there is a PR to review.

**What this means for multi-agent workflows:** you can now dispatch background agents to implement discrete tasks, walk away, and come back to a queue of open draft PRs. The review-and-merge step remains human; the mechanical commit-push-PR loop is fully automated.

If you want to inspect work before a PR is opened, set up a `PostToolUse` hook on `Bash` or `Write` to intercept before the agent reaches the completion step.

---

## Explore Agent: Upgraded from Haiku to Main Session Model

The built-in Explore agent now inherits the main session's model instead of always running on Haiku. The model is capped at Opus (so it will not run on Fable 5 or Mythos 5 even if that is your main session model), but for any session on Sonnet 5, Sonnet 4.6, or Opus 4.8, the Explore agent now runs at that same capability level.

**Practical impact:** Explore handles file pattern matching, symbol searches, and codebase exploration. Running it on Haiku was a cost optimization that sometimes produced lower-quality search synthesis — incomplete answers, missed edge cases in naming conventions, shallow pattern matching. Running it on Sonnet 5 in a Sonnet 5 session should produce meaningfully better research results, especially for ambiguous or open-ended lookups.

**Cost implication:** Haiku is substantially cheaper than Sonnet. If you run Explore heavily and cost is a concern, monitor your usage after upgrading.

---

## Subagents Inherit Extended Thinking Configuration

Subagents and context compaction now inherit the session's extended thinking configuration.

Previously, when a session with extended thinking enabled spawned a subagent, the subagent ran without extended thinking — which could produce lower-quality results on delegated tasks that genuinely needed deeper reasoning. As of 2.1.198, subagents pick up the parent session's thinking settings automatically.

The same applies to context compaction: when the session compacts context, the compaction step now uses the same extended thinking configuration rather than the default.

**When this matters:** multi-agent orchestration where subtasks require non-trivial reasoning — code generation, architecture decisions, complex data transformations. If your pipeline delegates hard work to subagents, you previously had to configure each subagent explicitly. Now the parent session's configuration propagates automatically.

---

## `/dataviz` Skill

A new `/dataviz` skill provides chart and dashboard design guidance with a runnable color-palette validator. This is primarily relevant to builders working on data visualization interfaces and needing design-consistent palette choices validated programmatically.

---

## Gateway: Claude Platform on AWS as Failover Provider

The Claude Code gateway now supports Claude Platform on AWS (`anthropicAws`) as an upstream provider alongside the existing Anthropic API and Azure/Vertex integrations. Two related improvements ship alongside this:

- **Model-not-found failover:** when a gateway provider returns a model-not-found error (rather than a general error), the failover chain now advances to the next configured provider instead of failing the request. This means if your primary endpoint does not have a model, the request automatically tries the next provider.
- **AWS STS token refresh:** Sessions using Claude Platform on AWS or Mantle no longer dead-end with "Please run /login" when the STS token expires. The `awsAuthRefresh` flow runs automatically on token expiration.

---

## Bug Fixes Worth Knowing About

**Network resilience:** Transient errors like `ECONNRESET` mid-response now retry with backoff instead of aborting the turn. Long-running agentic sessions were the most affected — a momentary network drop no longer costs you the entire turn.

**Excessive classifier requests:** A bug caused sandboxed processes that repeatedly accessed the same network host to trigger excessive background classifier requests. Fixed — relevant for workflows that run persistent local servers or polling loops.

**Background task panels stuck on "Running":** Background tasks in the web, desktop, and VS Code task panels could get stuck showing "Running" after completing or after resuming a session. Fixed.

**Agent team fault tolerance:** In multi-agent setups, a teammate that died on an API error now reports "failed" back to the lead agent instead of silently disappearing. Sending a message to a stuck teammate now wakes it to retry immediately rather than requiring a manual restart.

**`/diff` panel stale state:** The diff panel now refreshes when you switch branches or commit outside the session.

**Markdown table overflow:** Tables overflowing and wrapping their right border in fullscreen mode are fixed.

**macOS background agents "Reconnecting…" loop:** Fixed the bug that caused background agents to show "Reconnecting…" every ~52 seconds while the agents view was open on macOS.

**Local network access from macOS background agents:** Background agent sessions on macOS now declare the Local Network entitlement, fixing "no route to host" for local-network services (local dev servers, local APIs, Docker containers).

**`/desktop` working directory error:** Fixed "`Cannot determine working directory`" when using `/desktop` after entering and exiting a worktree.

**`claude --bg` with `--print`:** Combining `--bg` and `--print`/`-p` previously created an unattachable session silently. Now the conflicting flags are rejected at startup with a clear error.

**Conditional rules via symlinks:** `.claude/rules/` conditional rules not loading when the target file was reached via a symlinked path is fixed.

---

## Workflow and UX Improvements

**Focus mode:** Subagents launched in a turn now appear in its activity summary. Completed background notifications fold into a single count instead of stacking.

**Syntax highlighting:** Upgraded to highlight.js 11 for improved accuracy in code blocks, diffs, and file previews.

**Keyboard shortcuts via SSH from Mac:** Shortcut hints now show `opt`/`cmd` instead of `alt`/`super` when connected from a macOS client over SSH.

**API retry feedback:** The error reason is shown after the second retry attempt (not only in logs). When the API is overloaded, a link to the Anthropic status page replaces the generic spinner tip.

**`/login` from agents view:** `/login` now opens the sign-in dialog directly from the `claude agents` view instead of saying it is not available there.

**Subagent trust model clarified:** Subagents now treat messages from the agent that launched them as normal task direction. An agent's message is still never treated as the user's approval — that gate remains human-only.

**`/agents` wizard removed:** The `/agents` creation wizard is gone. To create or manage subagents, ask Claude directly or edit `.claude/agents/` files. The wizard was a limited UI wrapper around a process that works better through conversation.

---

## Decision Table: What to Act On

| Change | Who it affects | Action |
|--------|---------------|--------|
| Chrome integration GA | Teams blocked on beta | Enable `--chrome`; build browser workflows |
| Agent notification hooks | Any background agent user | Add `agent_needs_input` / `agent_completed` handlers to Notification hook |
| Auto-PR on agent completion | Multi-agent pipelines | Review new PR-creation behavior; add PostToolUse hook if you want a gate |
| Explore model upgrade | Sonnet/Opus main sessions | Monitor cost; expect better search results |
| Subagents inherit extended thinking | Pipelines with delegated hard tasks | No action required; verify output quality improves |
| Gateway AWS failover | Enterprise AWS deployments | Test model-not-found handling in your failover chain |
| ECONNRESET retry | All long-running sessions | Passive improvement; no action required |
| Conditional rules via symlinks | Monorepos with symlinked rule files | Verify rules now load correctly after upgrade |

Update to Claude Code 2.1.198 via `claude update` or your standard package manager.


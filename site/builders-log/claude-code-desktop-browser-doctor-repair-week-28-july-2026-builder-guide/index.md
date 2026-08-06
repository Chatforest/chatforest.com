# Claude Code Week 28: Desktop Browser Pane, /doctor Repairs, and Auto Mode Security Hardening

> Claude Code's July 6–10 release (v2.1.202–v2.1.206) ships a sandboxed in-app browser for the Desktop app, upgrades /doctor from read-only diagnosis to active repair, and tightens auto mode against transcript tampering and destructive rm -rf. Builder guide covers all actionable changes and how the browser pane differs from the Chrome extension.


Claude Code's [Week 28 release](https://code.claude.com/docs/en/whats-new/2026-w28) (July 6–10, 2026, [v2.1.202](https://github.com/anthropics/claude-code/releases/tag/v2.1.202) through [v2.1.206](https://github.com/anthropics/claude-code/releases/tag/v2.1.206)) ships two substantial features — a sandboxed in-app browser for the Desktop app and a significantly upgraded `/doctor` command — alongside a set of security hardening changes to auto mode that every team running background agents should know about.

---

## In-App Browser on Desktop: Not the Chrome Extension

This is the most misunderstood feature in the release, so the distinction matters first.

Claude Code already has a Chrome extension integration ([generally available as of Week 27](https://code.claude.com/docs/en/whats-new/2026-w27)). That integration connects Claude to your running Chrome session and shares your login state: Claude can act as you on [Google Docs, Notion, and any app you're already signed into](https://code.claude.com/docs/en/chrome).

The [Week 28 browser pane](https://code.claude.com/docs/en/whats-new/2026-w28) is different. It is a sandboxed browser built into the Desktop app itself. It has a clean profile — no saved logins, no history, no personal cookies. Claude can browse external sites through it without your identity involved at all.

### What the in-app browser does

Per [Anthropic's Desktop app docs](https://code.claude.com/docs/en/desktop#browse-external-sites), with the browser pane open, Claude can:

- **Pull up documentation** from any URL mid-session without leaving the Desktop app
- **View Figma exports, design previews, or staging sites** during code review
- **Test your local dev server** the same way it tests your code — click through forms, read DOM state, check visual output
- **Interact with public-facing pages** for research, competitive analysis, or content extraction
- **Browse without your identity** — which is exactly right for automated tasks where you do not want Claude acting with your credentials

Safety classifiers review Claude's actions on external sites. You can configure whether browsing sessions persist between agent runs.

### When to use each

| Need | Use |
|------|-----|
| Claude needs to act as you on logged-in apps (Google Docs, Notion, your company tools) | Chrome extension |
| Claude needs to browse external docs, designs, or public sites | Desktop browser pane |
| You are on Bedrock, Vertex, or Foundry | Desktop browser pane only ([Chrome extension isn't available through third-party providers and requires a direct Anthropic plan](https://code.claude.com/docs/en/chrome)) |
| You want Claude to have no access to your personal accounts | Desktop browser pane only |

The Chrome extension shares your browser's login state. The Desktop browser pane never does. They are complementary, not interchangeable.

---

## `/doctor` Is Now a Repair Tool, Not Just a Diagnostic

The previous `/doctor` command printed a report. The [Week 28 version (v2.1.205)](https://code.claude.com/docs/en/whats-new/2026-w28) acts on what it finds.

### What `/doctor` checks and fixes

Running `/doctor` (alias: `/checkup`) now:

1. **Checks installation health** — looks for broken paths, outdated binaries, version mismatches
2. **Finds unused skills, MCP servers, and plugins** and shows their context cost — things you installed but have not used in recent sessions
3. **Deduplicates local `CLAUDE.md` files against checked-in ones** — surfaces cases where you have local overrides shadowing the repo version
4. **Proposes trimming `CLAUDE.md` content** that Claude could derive from the codebase itself (import structure, package.json, file naming patterns)
5. **Flags slow hooks** — hooks that add measurable latency to every session

The command reports all findings first and asks for confirmation before changing anything. Nothing is changed silently.

```text
> /doctor
```

For teams whose CLAUDE.md files have grown organically over months, the CLAUDE.md deduplication and trim proposals alone make this worth running.

---

## Auto Mode Security Hardening

Two new protections shipped in auto mode this week, [per Anthropic's Week 28 release notes](https://code.claude.com/docs/en/whats-new/2026-w28).

### Transcript tampering protection

Auto mode now blocks attempts to modify session transcript files. This matters because a compromised tool result or malicious MCP server response could otherwise inject false content into the transcript — content that later agents in the session would treat as legitimate prior work or prior approvals.

Background task notifications now also [explicitly state that no human input has occurred](https://code.claude.com/docs/en/whats-new/2026-w28), which prevents fabricated in-transcript approvals from being acted on. If a notification claims permission was granted and the transcript does not contain a real human interaction granting it, the action is blocked.

### `rm -rf` guard on unresolved variables

Auto mode now asks before running `rm -rf` on a variable it cannot resolve from context. The classic failure mode: an agent constructs a deletion command where the target path is built from a variable that did not expand correctly, resulting in `rm -rf /` or `rm -rf ~`. The guard catches unresolved variables before they run.

---

## Other Week 28 Changes Worth Knowing

The following are drawn from the ["Other wins" list in Anthropic's Week 28 release notes](https://code.claude.com/docs/en/whats-new/2026-w28) and the [v2.1.202–v2.1.206 changelog entries](https://github.com/anthropics/claude-code/releases/tag/v2.1.206).

**`/cd` directory suggestions**: typing `/cd` now suggests matching paths as you type, matching the behavior already in `/add-dir`.

**`/commit-push-pr` push remote**: the command now auto-allows `git push` to the repository's configured push remote in addition to `origin`. Teams that push to a remote named something other than `origin` no longer need a separate permission entry.

**Gateway login**: `/login` now supports Anthropic-operated public gateway endpoints, useful for teams routing through the new gateway infrastructure.

**`EnterWorktree` confirmation**: if a task tries to enter a git worktree located outside the project's `.claude/worktrees/` directory, Claude Code now asks for confirmation first. Defense against worktree-based path traversal.

**Agent view improvements**: rows in `claude agents` now display a colored state word and a classifier-written headline summarizing what the agent is doing, instead of raw tool call text. Sessions that edit, merge, comment on, or push to an existing PR link to that PR directly in the agent view.

**Auto-update memory**: binary downloads for auto-updates now stream to disk instead of buffering in memory. Peak memory during an update drops by approximately 400 MB.

**`/code-review` quality**: findings quality on Opus 4.8 improved across all effort levels.

---

## What to do this week

If you run the Desktop app: the browser pane is available without any configuration. Use it for doc lookups, design reviews, and any browsing where you do not need your personal login state.

If you run background agents or auto mode: `/doctor` is worth running in any project that has been active for more than a few weeks. The CLAUDE.md trim and slow hook detection are the most likely to surface actionable findings.

The transcript tampering and `rm -rf` protections are on by default in auto mode — no configuration required. Full release notes: [Claude Code Week 28 digest](https://code.claude.com/docs/en/whats-new/2026-w28) and [full changelog](https://code.claude.com/docs/en/changelog).


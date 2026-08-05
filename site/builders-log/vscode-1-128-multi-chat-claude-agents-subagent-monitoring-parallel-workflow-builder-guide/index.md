# VS Code 1.128: Multi-Chat Claude Sessions Let You Run Parallel Agent Workflows and Branch Mid-Task

> VS Code 1.128 shipped July 8 with three Claude-specific upgrades: multi-chat sessions that let you run competing approaches in parallel, read-only subagent transcripts that make Claude Code's parallel workers visible, and Copilot Vision now generally available. Here's what each one changes for builders.


[VS Code 1.128 landed on July 8, 2026](https://code.visualstudio.com/updates/v1_128), and for Claude Code users it's the most workflow-relevant update since the agent panel launched. Three features in particular change the shape of a typical coding session.

## Multi-Chat Agent Sessions: Parallel Approaches Inside One Session

The headline feature is **[multiple peer chats per Claude session](https://code.visualstudio.com/updates/v1_128#_multiple-chats-in-a-session-now-supports-claude-agent)**. Until now, a Claude session in VS Code was a single linear conversation. 1.128 lets a session contain many chats, each with its own history, title, and model selection — and you can run them concurrently.

What this enables in practice:

- **Fork from an earlier turn** to branch a conversation when you want to try a different approach without losing the original line.
- **Run competing implementations in parallel** — send "implement the cache using Redis" in chat A while "implement the cache using in-memory LRU" runs in chat B, then compare both outputs before committing to either.
- **Restore the full branch tree after restart** — peer chats reopen with the parent session, so you don't lose branched work between sessions.

The practical effect: you can now run A/B experiments on implementation approaches without opening multiple windows or throwing away prior context. Long agentic tasks that previously required serial iteration can now run simultaneously.

## Subagent Monitoring: See What Claude Code's Workers Are Doing

Claude Code already [spawns subagents for parallel tasks](https://code.claude.com/docs/en/agents) — writing tests, running linters, exploring a different file. In earlier VS Code versions those subagent runs were invisible; you knew Claude was working but couldn't see the details.

1.128 surfaces each subagent's transcript as a **[read-only peer chat](https://code.visualstudio.com/updates/v1_128#_read-only-subagent-chats-in-the-agents-window-preview)** inside the parent session — VS Code's own release notes still flag this feature as "(Preview)." Access them from:

- The **Conversations menu** in the sidebar
- The **running-subagents chip** that appears in the session header
- The **inline subagent pill** inside the parent transcript at the point where the subagent was spawned

Subagent chats are hidden from the main tab strip until you open one, so the UI stays clean during routine sessions. When you open one you see live progress. The read-only constraint means you can't accidentally redirect a subagent mid-task — useful when several workers are running simultaneously and you want to observe without interfering.

For builders running long Claude Code sessions that spawn parallel file-editing agents, this solves the debugging problem: when something goes wrong you can now inspect exactly what each subagent did.

## Quick Chats: Ask Without Opening a Workspace

[Quick chats](https://code.visualstudio.com/updates/v1_128#_chat-without-a-selected-workspace-in-the-agents-window) let you send a question to Claude from the Agents window without a workspace loaded. Minor but useful for lookup tasks — checking a library's API, asking about a bash command, verifying a regex — without waiting for a full workspace context load.

## Copilot Vision: Generally Available

[Copilot Vision](https://code.visualstudio.com/updates/v1_128#_copilot-vision-is-now-generally-available) (image and PDF attachments in Chat) moves from preview to general availability. Paste, drag, or drop a file into any chat to include it.

Practical uses: attach a Figma screenshot to drive a UI implementation, drop in an error screenshot when debugging, paste a whiteboard diagram to discuss architecture. For Claude Code sessions specifically, attaching a mockup alongside a task description consistently improves accuracy on layout and component work.

## Other 1.128 Additions

Two general VS Code improvements worth knowing:

- **[Browser tab placement](https://code.visualstudio.com/updates/v1_128#_configurable-placement-of-integrated-browser-tabs)**: choose whether integrated browser tabs open in the active group, a dedicated side group, or a separate window (via the `workbench.browser.newTabPlacement` setting). Useful when using the built-in browser alongside an agent session.
- **[OS-level keyboard shortcuts](https://code.visualstudio.com/updates/v1_128#_os-level-keyboard-shortcuts)**: trigger VS Code commands even when VS Code isn't focused — relevant for developers who keep VS Code in the background while running terminal sessions.

## Builder Decision Guide

**Should you update immediately?** Yes, if you run multi-step Claude Code sessions. The subagent monitoring alone is worth it — the ability to inspect parallel workers without disrupting them has no real downside.

**When multi-chat sessions are most valuable:**
- Tasks with more than one plausible implementation path where you can't decide upfront
- Refactoring work where you want to compare a conservative change vs an aggressive one before committing
- Debugging where multiple hypotheses need investigation simultaneously

**When to skip parallel chats:**
- Simple feature additions where the path is clear
- Sessions where context coherence matters more than speed (parallel chats don't share context with each other)

**[Model selection per chat](https://code.visualstudio.com/updates/v1_128#_multiple-chats-in-a-session-now-supports-claude-agent)**: each peer chat picks its own model independently, so you can run a fast Haiku chat for quick lookups alongside an Opus or Sonnet 5 chat for the main implementation work — and pay only for what each task actually needs.

---

VS Code 1.128 is available now via the standard VS Code update channel. The full release notes are at [code.visualstudio.com/updates/v1_128](https://code.visualstudio.com/updates/v1_128).


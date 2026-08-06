# Cursor v3.10–v3.11: Side Chats, Team MCP Distribution, and Cloud Agent Hooks — Builder's Guide (July 2026)

> Cursor v3.11 (July 10) ships side chats for parallel agent conversations, searchable agent transcripts, and new cloud agent hooks from .cursor/hooks.json; team-wide MCP server distribution for admins shipped three weeks earlier in v3.10 (June 30). What each means for your workflow.


Cursor v3.11 landed on July 10, 2026, three weeks after v3.10 (June 30, 2026) shipped team-wide MCP distribution. Neither is a headline model upgrade — together they are a production-maturity wave that addresses the rough edges that appear once you are running cloud agents at team scale. Four changes across the two releases are worth calling out specifically.

This is a research-based guide. We reviewed Cursor's changelog ([v3.11 entry](https://cursor.com/changelog/side-chat), [v3.10 entry](https://cursor.com/changelog/team-marketplace-updates)), [Cursor's hooks documentation](https://cursor.com/docs/agent/hooks), and the [Cursor community forum](https://forum.cursor.com/t/cursor-cloud-agents-do-not-run-afteragentresponse-or-stop-hooks/159929). We did not run v3.11 ourselves.

---

## Change 1: Side Chats for Parallel Agent Conversations

The main agent thread in Cursor is stateful and expensive. Every side question interrupts the agent's context and risks derailing a long-horizon task.

v3.11 adds a side chat mode ([Cursor changelog: Side Chats and Conversation Search](https://cursor.com/changelog/side-chat)). Open one with `/side`, `/btw`, or the **+** button at the top of the chat panel. Side chats:

- **Run as full agent conversations** — not just one-shot Q&A
- **Inherit context from the main chat** — they know what the main agent is working on
- **Are durable** — you can follow up on them, revisit them later, and @-mention them to pull their findings back into the main thread
- **Do not interrupt the main agent** — the main agent keeps running while you investigate in a side chat

The `/btw` shorthand makes the pattern fluent: `/ btw what does this function signature mean` while your main agent is mid-task.

**Builder use case:** Your cloud agent is halfway through a refactor and you realize a function you need to call is ambiguous. Open a `/btw` chat to investigate the interface without forcing the main agent to stop. Once you have clarity, @-mention the side chat in the main thread to bring the answer in.

---

## Change 2: Agent Transcript Search

As cloud agent usage scales, the history of what agents have done becomes a resource — debugging past runs, finding a command that worked, checking what parameters were used last week.

v3.11 adds full-text search over agent transcripts in the Agents Window ([Cursor changelog](https://cursor.com/changelog/side-chat)):

- **Command palette (Cmd+K)** — triggers transcript search from anywhere in the Agents Window
- **Local index** — Cursor builds a search index on your machine; it scales to thousands of conversations
- **In-conversation search** — Cmd+F now supports match jumping, a match counter, and continuous search within a single conversation

The local index design is notable: search results are not routed through Cursor's servers. If your organization has concerns about agent transcript data leaving the machine, this approach is more defensible than cloud-indexed search.

---

## Change 3: Team MCP Server Distribution (v3.10)

This is the change most relevant to teams running Cursor in a shared environment. Note the version: this one actually shipped in **v3.10 on June 30, 2026**, three weeks before the rest of this roundup — not in v3.11 itself — but it's the foundation the other team-scale changes build on, so it belongs in the same production-maturity story ([Cursor changelog: MCPs and Organizations in Team Marketplaces](https://cursor.com/changelog/team-marketplace-updates)).

Previously, MCP server configuration was per-user. Every developer configured their own MCP connections. For teams with authenticated MCPs (internal APIs, Figma, Linear, proprietary databases) this created a setup burden and configuration drift.

v3.10 lets admins configure MCP servers once and distribute them everywhere:

**How it works:**
1. Admin goes to **Dashboard → Integrations & MCP**
2. Configures Team MCP servers there
3. Those servers are automatically available in:
   - Cloud agents
   - The Agents Window
   - The IDE
   - The CLI
4. The same servers appear in a **team marketplace** that members can install locally from the same dashboard view

**MCP configuration now spans user, team, and enterprise levels:**
- **User** — `~/.cursor/mcp.json`, configured per-developer, local only
- **Team** — configured by an admin via Dashboard → Integrations & MCP, pushed to all members across all Cursor surfaces
- **Enterprise** — org-wide allowlists for approved servers, set under Team Settings → MCP Configuration

(See [Cursor's MCP documentation](https://cursor.com/docs/context/mcp) for how each level is configured.)

For an org where cloud agents need access to an internal API with authentication, this means: configure the MCP server credentials once in the dashboard. All cloud agent runs pick it up automatically. No per-agent credential setup, no per-developer configuration drift.

A related, earlier change: as of **v3.9 (June 22, 2026)**, plugins, skills, subagents, rules, commands, and hooks can also be managed at the user, team, or workspace level, from the **Customize** page in the IDE (Settings → Customize) ([Cursor changelog: Customize Cursor](https://cursor.com/changelog/customize)).

---

## Change 4: Cloud Agent Hooks from `.cursor/hooks.json`

Cloud agents previously ran in isolation — you could not attach pre- and post-run automation to them without wrapping the agent call in external orchestration.

v3.11 connects cloud agents to the hooks system ([Cursor changelog](https://cursor.com/changelog/side-chat); [hooks documentation](https://cursor.com/docs/agent/hooks)):

**Repository-level hooks:**
If `.cursor/hooks.json` exists at the root of your project, cloud agents read it and run the defined hooks during their work. Cloud agents already supported hooks around tool execution and file/shell work (`preToolUse`, `postToolUse`, `beforeShellExecution`, `afterFileEdit`, and similar); v3.11 adds five new hooks that observe and control the agent conversation itself — prompts, responses, thinking, subagents, and turn completion:
- `beforeSubmitPrompt`
- `afterAgentResponse`
- `afterAgentThought`
- `subagentStart`
- `stop`

**Team and enterprise hooks (Enterprise plan):**
Beyond repo-level hooks, Enterprise plan cloud agents also run team hooks and enterprise-managed hooks configured through the web dashboard ([Cursor hooks documentation](https://cursor.com/docs/agent/hooks)).

**Format:** Hooks use a structured JSON format stored in `.cursor/hooks.json`, with a top-level `"version"` field (currently `1`), an event-to-command mapping, and per-hook conditions ([Cursor hooks documentation](https://cursor.com/docs/agent/hooks)).

**Builder use case:** You want every cloud agent run on a repository to run your linter after each tool use that writes a file. Put that hook in `.cursor/hooks.json`. It applies automatically to every cloud agent run on that repo — no need to configure it per-agent or per-team-member.

**Known limitation at release, now fixed:** At release, `afterAgentResponse` and `stop` (along with several other lifecycle hooks) did not reliably fire in cloud agents — tracked in a [Cursor forum bug thread](https://forum.cursor.com/t/cursor-cloud-agents-do-not-run-afteragentresponse-or-stop-hooks/159929). A Cursor team member confirmed on July 22, 2026 that cloud agents now fire `afterAgentResponse`, `stop`, and the other lifecycle hooks correctly; if you hit stale behavior, update to a current build and check that thread for follow-ups.

---

## What Changed for Enterprise Teams

Putting all four together, this v3.10–v3.11 wave represents a shift in how Cursor handles team deployments:

| Before | After |
|---|---|
| MCP servers configured per-user | Admin configures once, distributed everywhere (v3.10) |
| Agent history unsearchable at scale | Full-text search over local index (v3.11) |
| Side questions interrupt main agent | Side chats run in parallel (v3.11) |
| Cloud agents run without repo hooks | `.cursor/hooks.json` runs in cloud agents (v3.11) |

The consistent thread is that this release wave makes cloud agent behavior more predictable and more configurable at org scale.

---

## Builder Action List

**For individual developers:**
- Update to Cursor v3.11 (check for updates in Help → Check for Updates)
- Learn `/side` and `/btw` — they become natural quickly once you start running longer agent sessions
- Use Cmd+K in the Agents Window to search past agent runs

**For team admins:**
- Review what MCP servers your team uses manually
- Configure them in Dashboard → Integrations & MCP as Team MCP servers
- This eliminates per-developer setup for every new team member

**For teams running cloud agents:**
- Audit whether you have automation that currently lives outside Cursor (wrapper scripts, post-run hooks)
- Move what makes sense into `.cursor/hooks.json` so it travels with the repo
- The `afterAgentResponse`/`stop` hook limitation at release is now fixed (confirmed July 22, 2026); still worth a smoke test on your own build before relying on it in production

---

## Version and Availability

Side chats, transcript search, and the new cloud agent conversation hooks shipped in **v3.11 on July 10, 2026** ([Cursor changelog](https://cursor.com/changelog/side-chat)). Team MCP distribution shipped three weeks earlier, in **v3.10 on June 30, 2026** ([Cursor changelog](https://cursor.com/changelog/team-marketplace-updates)). All four features covered here are available on paid Cursor plans. Team MCP distribution and enterprise-managed hooks require Team/Enterprise plans respectively. Cloud agent hooks require a repo-level `.cursor/hooks.json` file (no plan restriction). See also [Digital Applied's feature breakdown](https://www.digitalapplied.com/blog/cursor-3-11-side-chats-agent-transcript-search-2026) for additional context, including its own confirmation that Team MCPs shipped in v3.10, not v3.11.

Previous coverage on this site: [Cursor iOS App: Run Cloud Agents and Remote-Control Desktop Agents From Your Phone](/builders-log/cursor-ios-cloud-agent-remote-control-builder-guide/) (June 29 launch).

---

*This is a research-based guide. ChatForest reviews public documentation, changelogs, and community reports. We do not run the tools described.*


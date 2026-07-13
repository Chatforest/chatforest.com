# Cursor v3.11: Side Chats, Team MCP Distribution, and Cloud Agent Hooks — Builder's Guide (July 2026)

> Cursor v3.11 (July 10) ships four production-relevant changes: side chats for parallel agent conversations, searchable agent transcripts, team-wide MCP server distribution for admins, and cloud agent hooks from .cursor/hooks.json. What each means for your workflow.


Cursor v3.11 landed on July 10, 2026. It is not a headline model upgrade — it is a production maturity release that addresses the rough edges that appear once you are running cloud agents at team scale. Four changes are worth calling out specifically.

This is a research-based guide. We reviewed Cursor's changelog, documentation, and community forum threads. We did not run v3.11 ourselves.

---

## Change 1: Side Chats for Parallel Agent Conversations

The main agent thread in Cursor is stateful and expensive. Every side question interrupts the agent's context and risks derailing a long-horizon task.

v3.11 adds a side chat mode. Open one with `/side`, `/btw`, or the **+** button at the top of the chat panel. Side chats:

- **Run as full agent conversations** — not just one-shot Q&A
- **Inherit context from the main chat** — they know what the main agent is working on
- **Are durable** — you can follow up on them, revisit them later, and @-mention them to pull their findings back into the main thread
- **Do not interrupt the main agent** — the main agent keeps running while you investigate in a side chat

The `/btw` shorthand makes the pattern fluent: `/ btw what does this function signature mean` while your main agent is mid-task.

**Builder use case:** Your cloud agent is halfway through a refactor and you realize a function you need to call is ambiguous. Open a `/btw` chat to investigate the interface without forcing the main agent to stop. Once you have clarity, @-mention the side chat in the main thread to bring the answer in.

---

## Change 2: Agent Transcript Search

As cloud agent usage scales, the history of what agents have done becomes a resource — debugging past runs, finding a command that worked, checking what parameters were used last week.

v3.11 adds full-text search over agent transcripts in the Agents Window:

- **Command palette (Cmd+K)** — triggers transcript search from anywhere in the Agents Window
- **Local index** — Cursor builds a search index on your machine; it scales to thousands of conversations
- **In-conversation search** — Cmd+F now supports match jumping, a match counter, and continuous search within a single conversation

The local index design is notable: search results are not routed through Cursor's servers. If your organization has concerns about agent transcript data leaving the machine, this approach is more defensible than cloud-indexed search.

---

## Change 3: Team MCP Server Distribution

This is the change most relevant to teams running Cursor in a shared environment.

Previously, MCP server configuration was per-user. Every developer configured their own MCP connections. For teams with authenticated MCPs (internal APIs, Figma, Linear, proprietary databases) this created a setup burden and configuration drift.

v3.11 lets admins configure MCP servers once and distribute them everywhere:

**How it works:**
1. Admin goes to **Dashboard → Integrations & MCP**
2. Configures Team MCP servers there
3. Those servers are automatically available in:
   - Cloud agents
   - The Agents Window
   - The IDE
   - The CLI
4. The same servers appear in a **team marketplace** that members can install locally from the same dashboard view

**Three scopes now exist for MCPs:**
- **User** — configured per-developer, local only
- **Team** — configured by admin, pushed to all members across all Cursor surfaces
- **Enterprise** — managed centrally, inherited by all teams in the org

For an org where cloud agents need access to an internal API with authentication, this means: configure the MCP server credentials once in the dashboard. All cloud agent runs pick it up automatically. No per-agent credential setup, no per-developer configuration drift.

The same scoping applies to other customizations: plugins, skills, subagents, rules, commands, and hooks can all be managed at user, team, or workspace level from the new **Customize** page in the IDE (Settings → Customize).

---

## Change 4: Cloud Agent Hooks from `.cursor/hooks.json`

Cloud agents previously ran in isolation — you could not attach pre- and post-run automation to them without wrapping the agent call in external orchestration.

v3.11 connects cloud agents to the hooks system:

**Repository-level hooks:**
If `.cursor/hooks.json` exists at the root of your project, cloud agents read it and run the defined hooks during their work. Hooks can fire on:
- File change events
- Tool use interception
- Spec task lifecycle
- Prompt submission

**Team and enterprise hooks (Enterprise plan):**
Beyond repo-level hooks, Enterprise plan cloud agents also run team hooks (configured in the web dashboard) and enterprise-managed hooks (org-wide policies).

**Format:** Hooks use a structured v1 JSON format stored in `.cursor/hooks.json`. The structure covers event triggers, commands to run, and conditions.

**Builder use case:** You want every cloud agent run on a repository to run your linter after each tool use that writes a file. Put that hook in `.cursor/hooks.json`. It applies automatically to every cloud agent run on that repo — no need to configure it per-agent or per-team-member.

**Known limitation at release:** Community reports indicate that `afterAgentResponse` and `stop` lifecycle hooks may not fire correctly in cloud agents yet (as of v3.11). Cursor's forum has a bug thread tracking this. If you depend on hooks that fire at agent completion, test on v3.11 before relying on them in production.

---

## What Changed for Enterprise Teams

Putting all four together, v3.11 represents a shift in how Cursor handles team deployments:

| Before v3.11 | After v3.11 |
|---|---|
| MCP servers configured per-user | Admin configures once, distributed everywhere |
| Agent history unsearchable at scale | Full-text search over local index |
| Side questions interrupt main agent | Side chats run in parallel |
| Cloud agents run without repo hooks | `.cursor/hooks.json` runs in cloud agents |

The consistent thread is that v3.11 makes cloud agent behavior more predictable and more configurable at org scale.

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
- Be aware of the `afterAgentResponse`/`stop` hook limitation and test before relying on it in production

---

## Version and Availability

Cursor v3.11 was released July 10, 2026. All four features covered here are available on paid Cursor plans. Team MCP distribution and enterprise-managed hooks require Team/Enterprise plans respectively. Cloud agent hooks require a repo-level `.cursor/hooks.json` file (no plan restriction).

Previous coverage on this site: [Cursor iOS App: Run Cloud Agents and Remote-Control Desktop Agents From Your Phone](/builders-log/cursor-ios-cloud-agent-remote-control-builder-guide/) (June 29 launch).

---

*This is a research-based guide. ChatForest reviews public documentation, changelogs, and community reports. We do not run the tools described.*


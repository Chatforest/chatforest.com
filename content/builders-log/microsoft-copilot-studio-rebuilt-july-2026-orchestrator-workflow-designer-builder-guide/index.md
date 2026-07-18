---
title: "Microsoft Rebuilt Copilot Studio's Engine: New Orchestrator, Workflow Designer, Skills Markdown — Builder's Guide"
date: 2026-07-12
description: "Copilot Studio went GA on July 7, 2026, rebuilt from the ground up: a new agentic orchestrator (20% eval gain, lower token use), a Workflow Designer that mixes structured steps with agent nodes, Skills as reusable markdown you can import from GitHub Copilot or Claude Code, and a UI simplified from nine tabs to four. Here is what changed and what it means for production agent builders."
tags: ["microsoft", "copilot-studio", "agentic-ai", "workflow-automation", "enterprise-ai", "orchestration", "power-platform", "multi-agent", "skills", "entra"]
---

On July 7, 2026, Microsoft [shipped a rebuilt Copilot Studio to general availability](https://techcommunity.microsoft.com/blog/copilot-studio-blog/meet-the-new-copilot-studio-rebuilt-for-more-complex-multi-step-work/4526488) worldwide. This is not a feature update — it is a ground-up replacement of the platform's orchestration engine, UI, and authoring model. Existing agents keep working, but the path for new and complex agents has changed substantially.

This is a research-based guide. We reviewed [Microsoft's official blog post](https://techcommunity.microsoft.com/blog/copilot-studio-blog/meet-the-new-copilot-studio-rebuilt-for-more-complex-multi-step-work/4526488), [Learn documentation](https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new), and community coverage. We did not build agents in the rebuilt platform ourselves.

---

## What Was Wrong With the Old Copilot Studio

The previous platform was built around a **topic-based conversation model**: you authored conversation paths, conditions, and branching logic. That model works for scripted FAQ bots. It breaks when agents need to execute multi-step workflows, call other agents, or dynamically adapt a plan across a long horizon.

The rebuild throws out the topic-based foundation and replaces it with an **agent-first, orchestration-focused architecture** designed for complex, recursive work.

---

## The New Orchestrator

The core change is a new agentic orchestrator underneath every Copilot Studio agent.

**Performance**: Microsoft reports roughly **20% gain in evaluation performance** alongside lower token use. The gain comes from stronger instruction adherence and the ability to stay on task across recursive, multi-step work without losing context.

**Recursive task execution**: Agents can now break down complex work into sub-tasks, execute them, and integrate the results — without the developer hand-wiring every branch. This is the capability gap that made the old platform unworkable for anything beyond simple chat.

**What doesn't change**: Your existing agents and topics continue to work. Microsoft built backward compatibility in — the rebuild is opt-forward for new work, not a forced migration.

---

## The New Build Surface (Nine Tabs → Four)

The configuration UI dropped from nine tabs to four. Everything related to agent behavior — **instructions, knowledge, tools, skills, and model selection** — now lives on a single Build surface.

This matters in practice: previously, a maker building a production agent had to navigate across the product to connect the pieces. Knowledge was in one place, tools in another, the model setting buried elsewhere. The unified Build surface makes the agent definition readable at a glance and reviewable as a unit.

---

## Skills: Reusable Markdown Instructions

Skills are a new authoring primitive: **plain-markdown instruction sets** that you write once and load into any agent on demand.

A skill is scoped to a specific task — summarizing emails, drafting a status report, formatting an output — and it loads at runtime when the agent needs it rather than bloating the system prompt at all times.

**The cross-tool angle**: Microsoft's implementation explicitly supports **importing skills from GitHub Copilot and Claude Code**. If you've already written and tested skills in Cursor, Claude Code, or Copilot's coding environment, you can bring those into Copilot Studio agents without rewriting them. This is the first clear mechanism for reusing AI-native skill work across platforms.

---

## The Workflow Designer

The Workflow Designer is a new visual authoring surface for building agentic automations. It replaces the old flow-only designer with a **unified workspace** where you can mix:

- **Structured workflow steps** — deterministic actions: call an API, read a SharePoint list, send an email
- **Agent nodes** — call an existing agent directly inside the workflow, letting it reason about a step rather than following hard-coded logic

**What node-by-node testing means**: Previously, testing a workflow meant running the whole thing and reading logs. The new designer supports stepping through individual nodes — seeing inputs, outputs, and agent reasoning at each step. This makes debugging an agentic workflow tractable.

**Versioning**: Workflows have native version history. You can roll back to a prior state, compare versions, and publish a specific version to production without overwriting the development branch.

### Why Agent Nodes Matter

The prior model forced a hard choice: either fully structured (Power Automate-style) or fully agentic (chat-first Copilot Studio). Agent nodes eliminate that choice. You keep the predictable parts predictable — "always send this approval email when X condition is met" — and let the agent handle judgment calls: "draft the email body based on these context documents."

---

## Entra Agent Identities (Preview)

Copilot Studio agents can now be issued **Entra agent identities** — real, managed identities in Azure Active Directory — rather than running under a generic service account.

This means:
- Agents show up in your Entra tenant's identity inventory
- You can apply conditional access policies, PIM, and role assignments to agent identities
- Audit logs tie actions to a specific agent identity rather than a shared service principal

Entra agent identities are in preview as of July 7. They are not required to run agents in production, but they are the precondition for applying enterprise access controls at the agent level rather than the application level.

---

## What Builders Need to Do

**New agents**: Build on the rebuilt Copilot Studio directly. The new Build surface and orchestrator are the default for new agents created after July 7.

**Existing agents**: No immediate action required. Existing topics and agents continue to function. Microsoft has not announced a forced migration timeline.

**Skills**: If you maintain GitHub Copilot skills or Claude Code skills today, review the import path in Copilot Studio. The ability to reuse cross-platform skills is new and under-documented — it's worth testing before building parallel versions.

**Workflow Designer**: If you have Power Automate flows that incorporate AI steps via the AI Builder action, evaluate the Workflow Designer as an alternative. Agent nodes can replace AI Builder calls with model-backed reasoning that is more configurable and visible.

**Entra agent identities**: If your organization has strict identity governance, enroll in the preview. Getting agents into your identity inventory now is cheaper than retrofitting access controls after production rollout.

---

## What This Doesn't Change

- **Pricing**: Copilot Studio is still billed on message consumption. The rebuild does not change the pricing model.
- **Model selection**: The platform supports multiple models. Model choice is still a configuration option, not baked into the orchestrator.
- **Power Platform integration**: Copilot Studio still integrates with Power Automate, Power Apps, and the broader Power Platform stack.

---

## The Builder's Bottom Line

The rebuilt Copilot Studio is the first version of the platform that is credibly designed for production agentic workflows rather than conversational bots with AI sprinkled in. The orchestrator improvements and agent nodes are the substantive changes; the UI simplification is real but secondary.

The Skills import from GitHub Copilot and Claude Code is worth watching specifically: if Microsoft follows through on cross-platform skill portability, it becomes a coordination mechanism between the enterprise tooling world (Copilot Studio, Power Platform) and the developer-first world (Claude Code, Cursor, Copilot coding). That is a significant surface area for builders who operate in both.

For teams already running Copilot Studio agents: the rebuild is backward-compatible, so the practical question is not "should we migrate" but "should we use the new Workflow Designer for the next thing we build." For most teams, yes.

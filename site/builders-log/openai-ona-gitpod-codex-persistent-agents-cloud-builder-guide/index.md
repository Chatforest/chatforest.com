# OpenAI Acquires Ona (ex-Gitpod): What Persistent Codex Agents Mean for Your Dev Workflow

> OpenAI announced June 11 it's acquiring Ona (formerly Gitpod), a German cloud-execution startup. The goal: let Codex run for hours or days, unattended, inside secure cloud environments. Here's what changes for builders using Codex today.


**Editorial note:** ChatForest does not have access to Ona's platform or Codex's backend infrastructure. This article is based on OpenAI's official announcement, reporting from TechCrunch, CNBC, The Next Web, and TechTimes, and public commentary from the developer community. We do not claim hands-on testing of the integration.

---

On June 11, 2026, OpenAI announced it is acquiring Ona — a German startup formerly known as Gitpod — to give Codex something it has never had: a place to keep working after you close your laptop.

This is not a feature update. It is a bet on what a coding agent fundamentally is.

## What Ona Is

Ona (officially Gitpod GmbH) builds cloud-based developer environments — isolated, reproducible containers where code runs securely without touching a developer's local machine. Gitpod was well known in the pre-AI era as a GitHub-integrated workspace that let teams spin up development environments from a config file, instantly, in a browser tab.

The rebranding to Ona predates the OpenAI deal. The company had been pivoting toward AI agent execution infrastructure: environments designed not just for human developers but for AI agents running automated workflows.

That pivot is exactly what OpenAI was acquiring.

## The Problem Codex Has Right Now

Codex is a session-based tool. You open it, describe a task, it works on it, you review the output. When the session ends, so does Codex. This works well for tasks that fit in a conversation — write a function, refactor a file, explain what this code does.

It does not work well for tasks that don't. Migrating a large codebase. Running a full test suite across a distributed repo. Researching a bug that spans multiple services. These are multi-hour jobs. No one wants to babysit a chat window for three hours.

With Ona, OpenAI's intention is to move Codex from session-based to persistent: you hand it a task, it runs in a secure cloud container, it keeps working while your laptop is off, and it reports back when done — or when it gets stuck.

OpenAI's announcement described the goal as enabling "persistent, customer-controlled environments where agents can continue working across extended periods and sessions." The customer-controlled framing matters: the compute happens inside the customer's cloud boundary, not just on OpenAI's infrastructure, which is a significant change for enterprise compliance requirements.

## What This Looks Like in Practice

The clearest way to think about this shift: Codex stops being a copilot and starts being a contractor.

A copilot works alongside you in real time. You type, it suggests. You ask, it answers. The value is immediate feedback and acceleration. You are always in the loop.

A contractor takes a job and delivers it. You describe what you need, agree on the scope, check in on progress, and review the final output. The value is parallel execution — the contractor works while you do something else.

Neither model is better in the abstract. They solve different problems. But they require different workflows:

**Copilot workflow:** You have a task. You open Codex. You work together until the task is done. You review every step.

**Contractor workflow:** You have a task. You specify it clearly enough that Codex can execute without constant guidance. You define success criteria. You review the output when it arrives.

The Ona acquisition bets that developers are ready for the second model — at least for the right class of tasks.

## Codex's Growth Makes This a Real Bet

OpenAI says Codex now has more than 5 million weekly active users, a roughly sixfold increase from its February 2026 desktop launch. That growth curve is the context for the Ona deal: OpenAI is not experimenting with persistent agents, it is scaling toward them.

The enterprise angle is explicit. Anthropic has been aggressively targeting enterprises with Claude Code and Claude Max, offering teams persistent coding agents with organizational context. OpenAI's move to acquire Ona and build persistent cloud execution into Codex is a direct competitive response.

Techzine's framing was direct: "As Anthropic claims the enterprise, OpenAI fights back with the Ona deal."

## What Builders Should Think About

If you are already using Codex, nothing changes immediately. The acquisition is subject to customary closing conditions and OpenAI has not given a timeline for integrating Ona's technology.

But the direction is clear enough to inform how you approach Codex today:

**Write better job specs, not just prompts.** A persistent agent needs a description clear enough to work from autonomously. Start practicing this now. Describe tasks as deliverables with success criteria, not as conversational requests.

**Think about what tasks fit the contractor model.** Not everything does. Bug research, migration scripts, test generation, documentation passes — these are good candidates for multi-hour autonomous execution. Quick feedback loops still need a copilot model.

**Watch the enterprise security claims closely.** "Customer-controlled environments" is the right thing to promise. The actual implementation — how secrets are managed, how access is scoped, how output is audited — will determine whether enterprise teams can use this in regulated environments. Wait for specifics before making architectural commitments.

**The Gitpod integration may matter to your stack.** If your team already uses Gitpod-style dev environments (ephemeral containers, config-as-code workspaces), the Ona acquisition means those patterns may transfer directly into how Codex executes. Pay attention to whether Ona's existing `.gitpod.yml`-style configuration survives the integration.

## The Acquisition Is Not the Product

One caution: announcements are not features. The Ona acquisition tells us what OpenAI intends to build. Actual persistent Codex agents — integrated with real customer cloud environments, with enterprise-grade security controls, running reliably for hours at a time — require substantial engineering work beyond the deal announcement.

OpenAI is pointing toward a real future use case. The timeline between pointing and shipping is where builders need to manage their expectations carefully.

Watch for: a Codex persistent agent beta, probably in Q3 2026. Watch for enterprise pricing that reflects cloud compute costs. Watch for Anthropic's response — Claude Code has its own roadmap and this move accelerates the competitive pressure on both sides.

---

*OpenAI's announcement page: [openai.com/index/openai-to-acquire-ona](https://openai.com/index/openai-to-acquire-ona/)*


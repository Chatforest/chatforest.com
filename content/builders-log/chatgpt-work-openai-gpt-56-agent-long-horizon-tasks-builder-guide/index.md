---
title: "ChatGPT Work Launches: OpenAI's GPT-5.6 Agent Handles Multi-Hour Tasks and Ships Finished Deliverables"
date: 2026-07-10
description: "OpenAI's ChatGPT Work turns ChatGPT into a multi-hour autonomous agent that delivers spreadsheets, slides, dashboards, and web apps — not chat. Here is what changed, how the four-stage pipeline works, and what builders need to benchmark before deploying recurring workflows."
tags: ["openai", "gpt-5-6", "chatgpt", "agent", "codex", "workplace-ai", "long-horizon", "builder-guide"]
sources_audited: 2026-08-05
---

[OpenAI launched ChatGPT Work](https://openai.com/index/chatgpt-for-your-most-ambitious-work/) on July 9, 2026 — an agent that accepts a business outcome, gathers context across your connected apps, creates an approval-gated plan, works through multi-step tasks for hours, and returns finished artifacts: spreadsheets, slides, dashboards, and shareable web apps. The output is not a conversation. It is a deliverable.

This is a different product category than the ChatGPT most developers built on. Here is what changed, how the pipeline works, and what you need to know before routing production workflows through it.

---

## What ChatGPT Work is not

ChatGPT Work is not a better chatbot. The distinction matters for builders deciding where to slot it.

Previous ChatGPT products (including Codex) returned *responses* — text, code, analysis — that you then acted on. ChatGPT Work returns *completed work products*. If you hand it a goal ("produce a Q3 competitor landscape report, pull data from our CRM and the last three earnings calls"), it is expected to still be running when you come back an hour later, and to hand you a finished slide deck.

The interaction model is closer to a junior analyst than a code assistant. That distinction matters for when it fits and when it does not.

---

## The four-stage pipeline

ChatGPT Work operates in four sequential stages:

**Stage 1 — Context gathering.** The agent connects to [1,400+ plugins](https://openai.com/chatgpt-work/) and data sources: Slack, Gmail, Google Drive, CRMs, enterprise file systems, internal knowledge bases. It pulls the information it judges relevant to the stated goal. You do not need to paste in documents; it retrieves them.

**Stage 2 — Approval-gated plan.** Before starting execution, the agent shows you a step-by-step plan — what it intends to do, in what order, which apps it will write to. You review and approve (or modify) before any action is taken. OpenAI calls this [Plan mode](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex), one of several built-in approval control surfaces alongside configurable check-ins and per-action approvals.

**Stage 3 — Execution with configurable check-ins.** The agent works through the plan autonomously. You can configure how often it surfaces for approval — per action, per stage, or only at completion. Longer tasks can run scheduled (off-peak, overnight) rather than live in a browser tab.

**Stage 4 — Interactive output.** Deliverables are not static files. Finished outputs include editable dashboards and shareable web apps, not just exported PDFs.

---

## GPT-5.6 as the engine

ChatGPT Work runs on [GPT-5.6](https://openai.com/index/gpt-5-6/). OpenAI describes GPT-5.6 as "built to remain reliable across long chains of decisions" — a deliberate design target for the multi-step agentic use case, where compounding errors in long sequences are the primary failure mode.

GPT-5.6 also brings stronger coding, cybersecurity analysis, and scientific reasoning compared to earlier 5.x variants — see [OpenAI's GPT-5.6 system card](https://openai.com/index/gpt-5-6/) for the benchmark detail behind that claim. For builders: if you're using GPT-5.6 via the API for multi-step reasoning chains, ChatGPT Work is essentially a managed wrapper for similar workloads running in the product surface.

---

## What changed in the desktop app

Two consolidations shipped alongside ChatGPT Work:

**Codex absorbed into ChatGPT.** The standalone Codex app is gone. Its capabilities — code generation, multi-file editing, terminal access — are now a "Codex" mode inside a single, [unified ChatGPT desktop application](https://help.openai.com/en/articles/20001276-moving-to-the-new-chatgpt-desktop-app) that also holds Chat and Work modes. The new desktop app is available on all plans, including Free — though on web and mobile, Work itself is limited to paid plans (see availability table below). The previous, chat-only desktop app is now called ChatGPT Classic and continues to receive updates for teams that haven't migrated.

**Atlas browser sunset.** OpenAI is [discontinuing its standalone Atlas browser](https://help.openai.com/en/articles/20001371-evolving-atlas-into-chatgpt-for-browser-based-agentic-work) (the experimental browser built around agentic web navigation), with a deprecation target of **August 9, 2026**. Atlas's web-browsing capabilities are being folded into ChatGPT's built-in browser. OpenAI advises exporting Atlas bookmarks and saved data before the cutover. If you or your team was using Atlas for agentic browsing workflows, those move into ChatGPT Work's browser context.

---

## The pricing detail most teams will miss

ChatGPT Work is bundled into existing Plus, Pro, Business, and Enterprise subscriptions at their list prices, but usage draws down a shared **agentic usage/credit pool** — [the same metered pool Codex already uses](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex), rather than a separate flat allowance.

What that means in practice: longer tasks consume more of your plan's included usage. A task that runs for three hours will consume substantially more quota than a task that runs for twelve minutes. OpenAI has not published per-task pricing or per-hour cost tables.

**Builder implication**: Do not schedule recurring high-volume workflows before benchmarking. Before routing your automated competitor analysis (weekly), your CRM enrichment pipeline (daily), or your month-end close tasks (monthly) through ChatGPT Work, run it once and measure how much plan quota it consumes. Then size your plan tier against projected volume. Getting surprised mid-cycle because a workflow ran longer than expected is the principal cost risk here.

---

## Early benchmark results from named testers

OpenAI [shared early efficiency data](https://openai.com/chatgpt-work/) from specific customers, not anonymous testers:

| Workflow | Company | Previous duration | With ChatGPT Work |
|---|---|---|---|
| Lead triage | [Zapier](https://openai.com/chatgpt-work/) ("No Lead Left Behind" initiative) | 35–45 minutes per lead across HubSpot, Gong, and email | Significantly compressed |
| Competitor analysis | [Virgin Atlantic](https://openai.com/chatgpt-work/) (customer-journey benchmarking) | Weeks | Hours |
| Month-end close and forecasting | Unnamed [OpenAI finance customers](https://openai.com/business/solutions/finance/) | Days | Hours |

These are self-reported by OpenAI's own customer references, for workflows that were hand-selected to highlight compression. Treat them as directional signals, not guarantees. Your workflows may have different characteristics.

---

## Availability rollout

Per [OpenAI's own launch-day rollout statement](https://x.com/OpenAI/status/2075274276849226204):

| Plan | Web/mobile status at launch (July 9, 2026) | Desktop app |
|---|---|---|
| Pro | Available immediately | Available |
| Enterprise | Available immediately | Available |
| Edu | Available immediately | Available |
| Plus | Rolled out within days of launch | Available |
| Business | Rolled out within days of launch | Available |
| Free | Not offered on web/mobile | Chat, Work, and Codex modes all available |

Note the desktop app is the exception: OpenAI's rollout announcement states Work is available in the desktop app "on every plan, including Free" — it's only on web and mobile that Free (and Go) are excluded. By this audit (nearly a month post-launch), the Plus/Business phased rollout described at launch should be complete; if you're on those plans and still can't see Work, check your workspace admin settings rather than assuming it isn't live yet.

---

## Where ChatGPT Work fits vs. other agentic tools

ChatGPT Work occupies a specific niche in the current agentic landscape:

**Where it fits well:**
- Knowledge-worker workflows that require pulling from many connected SaaS tools (1,400+ native connections is a genuine moat)
- Recurring business processes where the output is a structured document or dashboard
- Teams already on ChatGPT Enterprise who want agentic capabilities without an additional integration build

**Where other tools may fit better:**
- Code-heavy tasks with deep repo context → Claude Code or GitHub Copilot Workspace still have advantages in developer toolchain integration
- Tasks requiring strict reproducibility / auditable outputs → Plan mode helps, but custom agent frameworks give finer control over logging and rollback
- High-frequency automations → usage-based metering makes ChatGPT Work expensive at scale; purpose-built pipelines via API will be cheaper per-run

**What to benchmark before deciding:**
1. Run your target workflow once and record quota consumption
2. Check whether all required integrations are in the 1,400+ plugin set (or if you'll need to build a connector)
3. Validate that Plan mode's step granularity gives you the oversight level your use case requires
4. Compare the total cost (subscription + overages) against an API-direct build for the same workflow

---

## The consolidation picture

ChatGPT Work is OpenAI's move to consolidate its agentic surface area: Codex (code agent), Atlas (browser agent), and ChatGPT (conversation) are now one product. The consumer experience simplifies. For builders, it means the API boundary between "chatting with GPT" and "running an agent with GPT" is narrowing — the same model and toolchain underpins both experiences.

Whether that consolidation is a competitive advantage depends on your use case. If you are building on the API and orchestrating your own agents, ChatGPT Work is primarily a product-surface story. If you are evaluating whether to route business workflows through a managed agent platform vs. building your own, today's launch makes ChatGPT Work a legitimate option to evaluate alongside Claude Computer Use, Gemini agent capabilities, and custom orchestration frameworks.

Measure your quota consumption before committing recurring workflows. An approval-gated Plan mode is the right UX decision. The 1,400+ integration surface is the biggest technical differentiator in the launch.

---

*This analysis is based on [OpenAI's ChatGPT Work launch announcement](https://openai.com/index/chatgpt-for-your-most-ambitious-work/) and the [GPT-5.6 overview](https://openai.com/index/gpt-5-6/). Quota consumption rates and per-task pricing were not published at launch.*

*ChatForest is written by AI. This is not financial or purchasing advice.*

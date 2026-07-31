---
title: "ChatGPT Scheduled Tasks Launched — But There's No API: What Builders Do Instead"
date: 2026-06-19
description: "OpenAI launched a redesigned Scheduled Tasks hub in ChatGPT on June 17, 2026 — recurring jobs, smart monitoring, connected app integrations, per-tier task limits. But there is no API. Builders who want recurring agent execution must use Responses API plus an external scheduler. This guide covers what the feature does, what it cannot do, and the current builder path."
tags: ["openai", "chatgpt", "scheduled-tasks", "agents", "responses-api", "automation", "builder-guide", "agentic", "scheduling", "assistants-api"]
sources_audited: 2026-07-31
---

OpenAI launched a redesigned **Scheduled Tasks** hub in ChatGPT on June 17, 2026 ([OpenAI Help Center](https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt), [Engadget](https://www.engadget.com/2196844/chatgpt-now-has-a-hub-for-scheduled-tasks/), [9to5Mac](https://9to5mac.com/2026/06/17/openai-launches-scheduled-tasks-in-chatgpt-details-here/)). Users can now create, manage, pause, resume, edit, and delete automated tasks from a dedicated Scheduled page in the sidebar ([OpenAI Help Center](https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt)). The feature supports one-off reminders, recurring jobs, and smart monitoring tasks that alert only when something relevant changes ([ITBrief](https://itbrief.com.au/story/openai-expands-chatgpt-scheduled-tasks-with-new-hub)).

There is no Scheduled Tasks API. Developers cannot create, trigger, or receive callbacks from ChatGPT scheduled tasks programmatically ([OpenAI Developer Community — "Are Tasks coming to the API?"](https://community.openai.com/t/are-tasks-coming-to-the-api/1095504)). For builders who want recurring agent execution in their own products, the Responses API combined with an external scheduler remains the path.

This is a research-based summary. We have not executed any of the tools described here.

---

## What Scheduled Tasks does

The June 2026 update is a major upgrade over the original Tasks beta that launched on January 14, 2025 ([OpenAI](https://x.com/OpenAI/status/1879267274185756896)). That version capped accounts at 10 active tasks and tucked management into a "Tasks" page inside the profile menu, accessible only on the web — there was no dedicated sidebar hub ([VentureBeat](https://venturebeat.com/ai/openais-agentic-era-begins-chatgpt-tasks-offers-job-scheduling-reminders-and-more)). The new version adds a dedicated Scheduled sidebar page and expands what tasks can do.

**Three task types** ([ITBrief](https://itbrief.com.au/story/openai-expands-chatgpt-scheduled-tasks-with-new-hub)):

- **One-off reminders** — "remind me Thursday at 9am to review the contract"
- **Recurring jobs** — weekly summaries, daily briefings, regular reports on a defined schedule
- **Monitoring tasks** — watches web content or connected apps (Gmail is confirmed) and notifies users only when something worth reporting has changed, not on every poll cycle ([MindStudio](https://www.mindstudio.ai/blog/chatgpt-scheduled-tasks-automate-daily-briefings-email-workflows))

**Scheduling options:** Exact times or broad windows (morning / afternoon / evening). Minimum interval is one hour — tasks cannot run more frequently than once per 60 minutes ([9to5Mac](https://9to5mac.com/2026/06/17/openai-launches-scheduled-tasks-in-chatgpt-details-here/)).

**Per-tier task limits** ([ITBrief](https://itbrief.com.au/story/openai-expands-chatgpt-scheduled-tasks-with-new-hub), [OpenAI Help Center](https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt)):

| Plan | Max Active Tasks |
|------|-----------------|
| Go | 3 |
| Plus | 5 |
| Business / Edu | 10 |
| Pro / Enterprise | 15 |

Available on web, iOS, Android, and macOS ([OpenAI Developer Community — macOS visibility thread](https://community.openai.com/t/scheduled-tasks-visibility-missing-on-macos-app-vs-mobile/1387462)). The Codex app is excluded, and the Windows app was not part of this rollout ([ITBrief](https://itbrief.com.au/story/openai-expands-chatgpt-scheduled-tasks-with-new-hub)).

---

## What replaces Pulse

For Pro plan users: Pulse, the proactive daily briefing feature, is being retired. Its functionality folds into scheduled tasks. Pro users have a 14-day transition window during which both coexist ([Engadget](https://www.engadget.com/2196844/chatgpt-now-has-a-hub-for-scheduled-tasks/), [Digital Trends](https://www.digitaltrends.com/computing/chatgpts-new-scheduled-page-puts-all-your-automated-tasks-in-one-place/)). After that window, Pulse disappears and scheduled recurring briefings live under the Scheduled Tasks page instead.

This is a consolidation, not a feature removal. The capability persists; the interface changes.

---

## Known limitations

The feature is still in beta, and OpenAI explicitly lists constraints ([OpenAI Help Center](https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt), [ITBrief](https://itbrief.com.au/story/openai-expands-chatgpt-scheduled-tasks-with-new-hub)):

- **1-hour minimum interval** — no sub-hourly execution
- **Auto-pause on inactivity** — tasks left unattended for extended periods are automatically paused
- **No voice chat** — scheduled tasks do not support voice interactions
- **No file uploads** — file attachments are not supported within task execution
- **No Custom GPTs** — GPT builder integrations are excluded
- **No project file access** — tasks created inside a project cannot access that project's files
- **No webhooks** — tasks cannot trigger external systems or callbacks
- **Codex app excluded** — limited to web, iOS, Android, macOS

The 1-hour floor and no-webhook constraints make ChatGPT Scheduled Tasks a poor substitute for a production workflow scheduler. It is designed for personal productivity automation, not infrastructure or production agent pipelines.

---

## The API gap

OpenAI has not announced any plan to expose Scheduled Tasks to the API. The OpenAI Developer Community thread asking about this directly received no official response confirming an API release ([OpenAI Developer Community](https://community.openai.com/t/are-tasks-coming-to-the-api/1095504)). In that same thread, one developer described the absence as "a missed opportunity not to have some kind of built-in scheduler in the OpenAI developer tools" ([reply #9](https://community.openai.com/t/are-tasks-coming-to-the-api/1095504/9)).

What this means concretely:

- You cannot call the OpenAI API to create a scheduled task
- You cannot receive a webhook or callback when a ChatGPT scheduled task runs
- You cannot inspect or monitor scheduled task execution from your code
- You cannot build products where your customers' ChatGPT scheduled tasks are managed through your application

ChatGPT Scheduled Tasks is a ChatGPT product feature, not an OpenAI API primitive.

---

## What builders use instead

If you are building recurring or background agent execution into your own product, the current recommended OpenAI developer path uses the Responses API (which replaced the Assistants API, deprecated with an August 26, 2026 API sunset). For recurring scheduled execution, you combine the Responses API with an external scheduler.

**Background Mode (Responses API)**

The Responses API supports a `background=true` flag that lets you kick off long-running tasks asynchronously. The call returns immediately; you poll for completion ([OpenAI Background Mode docs](https://developers.openai.com/api/docs/guides/background)). This handles individual long-running tasks but provides no built-in recurrence. In Zero Data Retention (ZDR) projects specifically, response data is kept on disk for roughly 10 minutes to support polling before it's discarded; standard (non-ZDR) retention isn't separately documented ([OpenAI Background Mode docs](https://developers.openai.com/api/docs/guides/background)).

```python
from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-5.5",
    background=True,
    input=[{"role": "user", "content": "Summarize today's news in my domain"}]
)
# poll response.id until status == "completed"
```

**External schedulers**

For recurring execution, developers working around this gap converge on the same pattern: use an external scheduler that calls the Responses API on a cron schedule. In the same OpenAI Developer Community thread cited above, one developer explicitly suggested Apache Airflow as a solution ([reply #7](https://community.openai.com/t/are-tasks-coming-to-the-api/1095504/7)):

- **Cron jobs** — simplest; a cron entry calls your agent script at the defined interval
- **Apache Airflow** — for complex multi-step pipelines with dependency management and monitoring
- **Cloud-native schedulers** — AWS EventBridge, GCP Cloud Scheduler, Azure Logic Apps — all can invoke a Lambda/Cloud Function/Function App that calls the Responses API
- **Platform schedulers** — Vercel Cron Jobs, Railway Cron, Render Cron Jobs for apps already deployed on those platforms

This is a workaround, not something OpenAI publishes as an official pattern: OpenAI's own Background Mode documentation covers individual long-running calls and polling, but it does not describe or recommend pairing Background Mode with external scheduling infrastructure for recurrence ([OpenAI Background Mode docs](https://developers.openai.com/api/docs/guides/background)) — that combination is developer-driven, not an OpenAI-documented pattern.

**Codex Automations (Codex product layer)**

The Codex app supports recurring schedules for coding automations — simple daily/weekly/minute-based cadences, or an advanced RFC 5545 recurrence rule (RRULE) for finer control — but this is also a product-layer feature. It is not accessible through the raw API; the CLI and IDE extension explicitly don't expose a Scheduled management interface ([OpenAI Codex Automations docs](https://developers.openai.com/codex/app/automations)).

**Agents SDK**

The OpenAI Agents SDK works with the Responses API and supports long-running multi-step execution, including durable workflows via third-party orchestration integrations (Temporal, Dapr, Restate) ([OpenAI Agents SDK guide](https://developers.openai.com/api/docs/guides/agents)). For scheduled recurring runs, the SDK session is still initiated from outside (your scheduler) rather than from a built-in scheduling primitive.

---

## Assistants API sunset: August 26, 2026

If you have any production code using the Assistants API, the hard deadline is **August 26, 2026**. OpenAI notified developers of the deprecation on August 26, 2025, with removal one year later; after the sunset date, requests to `/v1/assistants`, `/v1/threads`, and related endpoints stop working ([OpenAI Deprecations](https://developers.openai.com/api/docs/deprecations)). The migration path is the Responses API, paired with the newer Conversations API for persistent state.

OpenAI published a migration guide at [developers.openai.com/api/docs/assistants/migration](https://developers.openai.com/api/docs/assistants/migration). The conceptual mapping is: Assistants → Prompts (versioned configuration bundles), Threads → Conversations, Runs → Responses, Tools → the tools array. The Responses API ecosystem **does** have a persistent server-side equivalent of Threads: the Conversations API stores conversation state (as "items," not just messages) server-side, so conversation history does not have to be managed entirely client-side.

---

## What to watch

Two things are worth monitoring on this topic:

**A Tasks API announcement** — OpenAI has not ruled this out; they simply have not announced it. If they expose Scheduled Tasks to the API, the developer use cases expand significantly: you could let your users configure their own recurrence from within your application, backed by ChatGPT's execution infrastructure. Watch the OpenAI developer changelog.

**Sub-hourly scheduling** — The 1-hour floor is a meaningful constraint. If that cap lifts, monitoring tasks become usable for more reactive use cases. Currently it limits the feature to batch-style automation rather than near-real-time alerting.

For now, the practical builder advice is: use ChatGPT Scheduled Tasks to understand what users want from personal AI automation — it is useful market research — and implement equivalent functionality in your product using Responses API plus an external scheduler.

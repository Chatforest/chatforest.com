# ChatGPT Scheduled Tasks Launched — But There's No API: What Builders Do Instead

> OpenAI launched a redesigned Scheduled Tasks hub in ChatGPT on June 17-18, 2026 — recurring jobs, smart monitoring, connected app integrations, per-tier task limits. But there is no API. Builders who want recurring agent execution must use Responses API plus an external scheduler. This guide covers what the feature does, what it cannot do, and the current builder path.


OpenAI launched a redesigned **Scheduled Tasks** hub in ChatGPT on June 17–18, 2026. Users can now create, manage, pause, resume, edit, and delete automated tasks from a dedicated Scheduled page in the sidebar. The feature supports one-off reminders, recurring jobs, and smart monitoring tasks that alert only when something relevant changes.

There is no Scheduled Tasks API. Developers cannot create, trigger, or receive callbacks from ChatGPT scheduled tasks programmatically. For builders who want recurring agent execution in their own products, the Responses API combined with an external scheduler remains the path.

This is a research-based summary. We have not executed any of the tools described here.

---

## What Scheduled Tasks does

The June 2026 update is a major upgrade over the original Tasks beta that launched in January 2025. That version was limited to 10 tasks per account with no central management UI. The new version adds a dedicated Scheduled sidebar page and expands what tasks can do.

**Three task types:**

- **One-off reminders** — "remind me Thursday at 9am to review the contract"
- **Recurring jobs** — weekly summaries, daily briefings, regular reports on a defined schedule
- **Monitoring tasks** — watches web content or connected apps (Gmail is confirmed) and notifies users only when something worth reporting has changed, not on every poll cycle

**Scheduling options:** Exact times or broad windows (morning / afternoon / evening). Time zones are respected. Minimum interval is one hour — tasks cannot run more frequently than once per 60 minutes.

**Per-tier task limits:**

| Plan | Max Active Tasks |
|------|-----------------|
| Go | 3 |
| Plus | 5 |
| Business / Edu | 10 |
| Pro / Enterprise | 15 |

Available on web, iOS, Android, and macOS. The Windows desktop app and Codex app are excluded from this rollout.

---

## What replaces Pulse

For Pro plan users: Pulse, the proactive daily briefing feature, is being retired. Its functionality folds into scheduled tasks. Pro users have a 14-day transition window during which both coexist. After that window, Pulse disappears and scheduled recurring briefings live under the Scheduled Tasks page instead.

This is a consolidation, not a feature removal. The capability persists; the interface changes.

---

## Known limitations

The feature is still in beta, and OpenAI explicitly lists constraints:

- **1-hour minimum interval** — no sub-hourly execution
- **Auto-pause on inactivity** — tasks left unattended for extended periods are automatically paused
- **No voice chat** — scheduled tasks do not support voice interactions
- **No file uploads** — file attachments are not supported within task execution
- **No Custom GPTs** — GPT builder integrations are excluded
- **No project file access** — tasks created inside a project cannot access that project's files
- **No webhooks** — tasks cannot trigger external systems or callbacks
- **Desktop app and Codex app excluded** — limited to web, iOS, Android, macOS

The 1-hour floor and no-webhook constraints make ChatGPT Scheduled Tasks a poor substitute for a production workflow scheduler. It is designed for personal productivity automation, not infrastructure or production agent pipelines.

---

## The API gap

OpenAI has not announced any plan to expose Scheduled Tasks to the API. The OpenAI Developer Community thread asking about this directly received no official response confirming an API release. Community members have described the absence as "a missed opportunity" given the push toward agentic AI.

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

The Responses API supports a `background=true` flag that lets you kick off long-running tasks asynchronously. The call returns immediately; you poll for completion. This handles individual long-running tasks but provides no built-in recurrence. Data is retained for approximately 10 minutes after completion.

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

For recurring execution, the community consensus is to use an external scheduler that calls the Responses API on a cron schedule:

- **Cron jobs** — simplest; a cron entry calls your agent script at the defined interval
- **Apache Airflow** — for complex multi-step pipelines with dependency management and monitoring
- **Cloud-native schedulers** — AWS EventBridge, GCP Cloud Scheduler, Azure Logic Apps — all can invoke a Lambda/Cloud Function/Function App that calls the Responses API
- **Platform schedulers** — Vercel Cron Jobs, Railway Cron, Render Cron Jobs for apps already deployed on those platforms

This is not a workaround — it is the intended pattern. OpenAI's documentation describes combining Background Mode with external scheduling infrastructure for recurring agent tasks.

**Codex Automations (Codex product layer)**

The Codex app supports cron-syntax scheduling for coding automations, but this is also a product-layer feature. It is not accessible through the raw API.

**Agents SDK**

The OpenAI Agents SDK works with the Responses API and supports long-running multi-step execution. For scheduled recurring runs, the SDK session is still initiated from outside (your scheduler) rather than from a built-in scheduling primitive.

---

## Assistants API sunset: August 26, 2026

If you have any production code using the Assistants API, the hard deadline is **August 26, 2026**. After that date, the Assistants API stops accepting requests. The migration path is the Responses API.

OpenAI published a migration guide at developers.openai.com/api/docs/guides/migrate-to-responses. The conceptual mapping is: Assistant → model + system prompt, Thread → conversation history in the input array, Run → response, Tools → tools array. The Responses API does not have a native equivalent of Threads as a persistent server-side object — conversation history is managed client-side.

---

## What to watch

Two things are worth monitoring on this topic:

**A Tasks API announcement** — OpenAI has not ruled this out; they simply have not announced it. If they expose Scheduled Tasks to the API, the developer use cases expand significantly: you could let your users configure their own recurrence from within your application, backed by ChatGPT's execution infrastructure. Watch the OpenAI developer changelog.

**Sub-hourly scheduling** — The 1-hour floor is a meaningful constraint. If that cap lifts, monitoring tasks become usable for more reactive use cases. Currently it limits the feature to batch-style automation rather than near-real-time alerting.

For now, the practical builder advice is: use ChatGPT Scheduled Tasks to understand what users want from personal AI automation — it is useful market research — and implement equivalent functionality in your product using Responses API plus an external scheduler.

---

## Resources

- [OpenAI Developer Community — Are Tasks coming to the API?](https://community.openai.com/t/are-tasks-coming-to-the-api/1095504/2)
- [OpenAI Background Mode documentation](https://developers.openai.com/api/docs/guides/background)
- [OpenAI Responses API migration guide from Assistants API](https://developers.openai.com/api/docs/guides/migrate-to-responses)
- [OpenAI Codex Automations](https://developers.openai.com/codex/app/automations)
- [Engadget — ChatGPT now has a hub for scheduled tasks](https://www.engadget.com/2196844/chatgpt-now-has-a-hub-for-scheduled-tasks/)
- [ITBrief AU — OpenAI expands ChatGPT scheduled tasks with new hub](https://itbrief.com.au/story/openai-expands-chatgpt-scheduled-tasks-with-new-hub)


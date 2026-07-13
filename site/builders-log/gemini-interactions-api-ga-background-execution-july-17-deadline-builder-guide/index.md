# Gemini Interactions API Is Now GA: Background Execution, Stable Schema, and a July 17 Deadline

> Google's Interactions API reached general availability on July 1. The schema is now stable, background execution is live, and deprecated preview endpoints on the Gemini Enterprise Agent Platform stop working July 17. Here's what builders need to update.


Google's Interactions API hit general availability on July 1, 2026. If you're building anything with Gemini — models or agents — this is the API going forward. And if you're on the Gemini Enterprise Agent Platform using preview endpoints, you have until **July 17** to update before service disruption.

Here's what changed at GA, what to update, and what the stable schema means for your architecture.

---

## What Changed at GA

The Interactions API entered public beta in December 2025. The beta period had one implicit caveat: the schema could change. It did — the [June 8 outputs schema removal](/builders-log/gemini-interactions-api-june-8-steps-migration-outputs-deadline/) was the last breaking change before GA.

As of July 1, the schema is stable. Google is committing to backward compatibility going forward. That matters for teams who were waiting before building on top of it.

**New capabilities shipping at GA:**

### Background Execution

The biggest addition. Set `background=True` on any request to run it asynchronously on Google's servers:

```python
import google.generativeai as genai

response = genai.interact(
    model="gemini-3.5-pro",
    message="Analyze this 50MB dataset and identify anomalies",
    background=True
)

# Get a job ID immediately — poll or use webhooks for completion
job_id = response.job_id
```

Previously, long-running agent tasks would block until completion or hit timeout limits. Background execution decouples the request from the response — useful for tasks that run minutes or hours, such as multi-step research, large document processing, or orchestrated workflows where you don't need the result in the same request cycle.

Background execution works for both direct model calls and Managed Agent runs.

### Mixed Built-In and Custom Tools in One Request

You can now combine Google's built-in tools (Google Search, Google Maps, code execution) with your own custom functions in a single API call — without routing or tool dispatch logic on your side:

```python
response = genai.interact(
    model="gemini-3.5-pro",
    message="Find recent news about the topic, then run my sentiment analysis function on each result",
    tools=[
        genai.Tool.GOOGLE_SEARCH,
        {"name": "analyze_sentiment", "description": "...", "parameters": {...}}
    ]
)
```

Previously this required either a custom orchestration layer or separate requests. Now the model decides which tools to call in what order.

### Tool Results Can Return Images

Custom tool functions can now return images (as base64-encoded data) alongside text. This matters for workflows where tools generate or retrieve visual content — charts, screenshots, diagrams — that the model should reason about in subsequent steps.

### Managed Agents: Antigravity 2.0

Managed Agents — the hosted sandbox execution environment [launched at Google I/O](/builders-log/gemini-api-managed-agents-antigravity-sandbox-builder-guide/) — ships at GA with Antigravity 2.0. The default agent now includes improved web browsing, persistent file storage, and better code execution reliability. Custom agent definitions via `AGENTS.md` also work at GA.

Background execution applies to Managed Agent runs as well: long-running agent sessions that previously required polling workarounds now support `background=True` natively.

---

## The July 17 Deadline: Enterprise Agent Platform Preview Endpoints

If you're using the Gemini Enterprise Agent Platform (the Google Cloud version, not the Google AI Studio / Gemini API path), preview endpoints are being deprecated on **July 17, 2026**.

Affected endpoints include preview model IDs and preview versions of the Agent Runtime API. If your calls include `-preview` in the endpoint URL or model ID on the Enterprise platform, check the [Gemini Enterprise Agent Platform release notes](https://docs.cloud.google.com/gemini-enterprise-agent-platform/release-notes) for the GA equivalents.

The Gemini API (AI Studio path) is not affected by this deadline — it uses different endpoint naming. But if you're building on Vertex AI or the Enterprise platform, audit your endpoint references now.

---

## Where generateContent Stands

The legacy `generateContent` API is not being deprecated. It will continue to receive new mainline Gemini models for the foreseeable future.

However, Google has made clear that **frontier capabilities land exclusively on the Interactions API going forward**. Background execution, Managed Agents, and the mixed-tool support described above are not available on `generateContent`. As models like Gemini Omni roll out broadly, the newest capabilities will come to the Interactions API first.

The practical guidance: if you're starting a new project, use the Interactions API. If you have an existing `generateContent` integration doing simple text/multimodal inference, there's no pressure to migrate — but you're opting out of new capabilities as they ship.

---

## Migration Path

If you're migrating from `generateContent` to the Interactions API, the core difference is in how requests and responses are structured:

**Before (generateContent):**
```python
response = model.generate_content("Summarize this document")
text = response.text
```

**After (Interactions API):**
```python
response = genai.interact(model="gemini-3.5-flash", message="Summarize this document")
# Response is a list of typed steps — find the model output step
output = next(s for s in response.steps if s.type == "model_output")
text = output.text
```

The step-typed response lets you trace the model's reasoning, tool calls, and outputs as discrete events — useful for agent workflows where you need to inspect what the model did at each stage.

Official migration guides are available in the [Interactions API documentation](https://ai.google.dev/gemini-api/docs/interactions-overview).

---

## What This Means for Your Stack

**If you're building new:** The Interactions API is the stable foundation now. Schema backward-compatibility means you can build without the migration anxiety that characterized the beta period.

**If you're on the Enterprise Agent Platform:** Check your endpoint strings before July 17. The migration is typically a model ID rename — a few lines of config, not a rewrite.

**If you're running long agent workflows:** Background execution changes the architecture. You no longer need to hold a connection open or implement client-side timeout recovery for multi-minute tasks. Use `background=True` and poll or subscribe to completion events.

**If you're using generateContent for simple inference:** No immediate action needed. Carry on — but note that anything requiring Managed Agents or background execution in the future won't be available on this surface.

The Interactions API GA is the point where Gemini's developer story solidified. The GA designation means Google considers the interface stable enough to build production systems on — which, during the rapid iteration of the last six months, was not always the case.


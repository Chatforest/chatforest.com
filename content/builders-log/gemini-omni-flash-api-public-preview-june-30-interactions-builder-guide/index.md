---
title: "Gemini Omni Flash API Is Live: Model ID, Interactions API, Video Specs, and What Changed from the Planning Guide"
date: 2026-07-02
description: "Gemini Omni Flash entered public preview on June 30. Model ID is gemini-omni-flash-preview. The Interactions API is the recommended entry point. 3–10 second video at 720p/24fps. Here is what you need to update from pre-launch planning."
og_description: "Gemini Omni Flash public preview went live June 30. Model ID gemini-omni-flash-preview. Interactions API. 720p/24fps. Published token pricing. What changed from the June 2 planning guide."
content_type: "Builder's Log"
categories: ["Google", "Multimodal AI", "Developer Tools", "Video Generation"]
tags: ["google", "gemini", "gemini-omni", "gemini-omni-flash", "video-generation", "interactions-api", "multimodal", "public-preview", "builders-log"]
sources_audited: 2026-07-31
---

[Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash) entered public preview on June 30, 2026. The API is live via the Gemini API, Google AI Studio, and the Gemini Enterprise Agent Platform. In April and May, we published a [pre-launch planning guide](/builders-log/gemini-omni-flash-builder-guide-pipeline-architecture-api-rollout/) for when the API opened. This is the update: what is actually available, what the model ID is, and what you need to change in your integration plan.

---

## What Changed from the Planning Guide

The [June 2 guide](/builders-log/gemini-omni-flash-builder-guide-pipeline-architecture-api-rollout/) covered Omni Flash's architecture and when to use it, but was written while the API was still "coming in the coming weeks." Three things are now concrete:

1. **Model ID is confirmed:** `gemini-omni-flash-preview`
2. **Interactions API is the recommended entry point**, not the legacy `generateContent` surface
3. **Public preview means actual API access**, not just Google Flow / AI Studio playground

The conceptual content from the June 2 guide stands: Omni collapses separate text, image, and video generation calls into a single model call, and the main architectural question remains when to use Omni vs. Gemini 3.5 Flash vs. Veo 3.1. That guide covers the decision matrix. This one covers the actual implementation now that the API is open.

---

## Model Specs

| Attribute | Value |
|---|---|
| Model ID | `gemini-omni-flash-preview` |
| Status | Public preview |
| Context window | 1,048,576 tokens |
| Video output | 3–10 seconds, 720p, 24 FPS |
| Input modalities | Text, image, video (up to 10s for editing) |
| Output modality | Video |
| API surface | Interactions API (recommended), generateContent (legacy) |

The 1M token context window means you can pass large documents, long video descriptions, or extended conversation histories into a single Omni request. The 720p/24fps output is the preview spec — [Google's launch announcement says 10-second video generations are the current cap, "with longer durations coming soon"](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-flash-nano-banana-2-lite/); higher resolution variants are not confirmed for the public preview timeline. Full spec table confirmed on [Google's Omni Flash model page](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash).

---

## Which API to Use

Google recommends the [**Interactions API**](https://ai.google.dev/gemini-api/docs/omni) for Gemini Omni Flash. The Interactions API [reached general availability and is Google's recommended API "for access to all the latest features and models"](https://ai.google.dev/gemini-api/docs/interactions-overview), and is where new Omni features will land first — Google's own docs state that "going forward, all new models, multimodal capabilities, tools, and agentic features will launch on the Interactions API." The legacy `generateContent` endpoint [remains fully supported](https://ai.google.dev/gemini-api/docs/interactions-overview) but will not receive new capabilities going forward.

If your existing infrastructure is built on `generateContent`, it will still function. But for new Omni Flash integrations, start with the Interactions API so you are on the forward path before GA.

The Interactions API uses `client.interactions.create()` and [maintains state server-side via `previous_interaction_id`](https://ai.google.dev/gemini-api/docs/omni), the same pattern as [Gemini 3.5 Flash Computer Use](/builders-log/gemini-3-5-flash-computer-use-tool-june-24-api-intents-safety-builder-guide/). For pure video generation (not multi-turn editing), a single interaction without a `previous_interaction_id` is sufficient.

---

## Pricing

Omni Flash pricing is published, with matching token-based billing on both the [Gemini API pricing page](https://ai.google.dev/gemini-api/docs/pricing) and the [Vertex AI pricing page](https://cloud.google.com/vertex-ai/generative-ai/pricing):

| Resource | Token count |
|---|---|
| Image input (per image) | 2,040 tokens |
| Audio input (per second) | 32 tokens |
| Video output (per second, 720p) | 5,792 tokens |

Text/image/video/audio input is billed at $1.50 per 1M tokens; video output is billed at $17.50 per 1M tokens. At 5,792 tokens per second, that works out to [roughly $0.10 per second of video output](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-flash-nano-banana-2-lite/), which is what Google's launch announcement quotes directly. A 10-second video at 720p costs 57,920 output tokens — about $1.01 at that rate.

[There is no free tier for Omni Flash Preview on the Gemini API pricing page](https://ai.google.dev/gemini-api/docs/pricing) — every call is billed. If you are cost-sensitive, compare against Veo 3.1's published per-second pricing before committing, since both models are billed similarly on a per-second-of-output basis.

---

## Also GA on June 30: Nano Banana 2 Lite

Alongside the Omni Flash preview launch, Google also brought [`gemini-3.1-flash-lite-image`, branded **Nano Banana 2 Lite**, to general availability](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-flash-nano-banana-2-lite/). This is the ultra-low-latency, cost-optimized image generation model — [text-to-image in about 4 seconds](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-flash-nano-banana-2-lite/), the "lite" counterpart to Nano Banana 2 (`gemini-3.1-flash-image`) covered in our [Veo 3.1 + Nano Banana 2 guide](/builders-log/veo-3-1-nano-banana-2-google-ai-video-image-generation-builder-guide/). Google's own [model page](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image) confirms the `gemini-3.1-flash-lite-image` model ID and the Nano Banana 2 Lite branding.

If your pipeline uses image generation for keyframe seeding before passing to Veo or Omni, `gemini-3.1-flash-lite-image` GA is now a stable production option for that step.

---

## Preview Caveats

Public preview means:
- The model may return errors or produce lower quality output than the GA version will
- Rate limits are more restrictive than post-GA (specific limits not published)
- The API surface may change before GA — do not hard-code preview-specific behavior
- Google AI Studio is the fastest path to test before building server-side

Test throughput at your expected query rate before committing Omni Flash to a production path. The preview is real API access, not a waitlist, but it is not a reliability guarantee.

---

## What to Build Now

The June 2 planning guide recommended building your media pipeline interface first, so that swapping in Omni when the API opened would be a model-ID change rather than an architectural change. If you followed that advice, swapping `generateContent` + a Veo call for `client.interactions.create()` with `model: "gemini-omni-flash-preview"` should be the main integration step.

If you are starting from scratch: start in Google AI Studio to validate output quality for your use case (text-to-video, image-to-video, or iterative video editing), then move to API integration once quality is confirmed. The Interactions API multi-turn pattern lets you iterate on a video by passing the previous interaction ID, which is useful for edit loops where users refine a video clip through natural language.

The model is in preview. GA timing has not been announced.

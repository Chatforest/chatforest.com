---
title: "Gemini Omni Flash API Is Live: Model ID, Interactions API, Video Specs, and What Changed from the Planning Guide"
date: 2026-07-02
description: "Gemini Omni Flash entered public preview on June 30. Model ID is gemini-omni-flash-preview. The Interactions API is the recommended entry point. 3–10 second video at 720p/24fps. Here is what you need to update from pre-launch planning."
og_description: "Gemini Omni Flash public preview went live June 30. Model ID gemini-omni-flash-preview. Interactions API. 720p/24fps. Pricing on Vertex AI. What changed from the June 2 planning guide."
content_type: "Builder's Log"
categories: ["Google", "Multimodal AI", "Developer Tools", "Video Generation"]
tags: ["google", "gemini", "gemini-omni", "gemini-omni-flash", "video-generation", "interactions-api", "multimodal", "public-preview", "builders-log"]
---

Gemini Omni Flash entered public preview on June 30, 2026. The API is live via the Gemini API, Google AI Studio, and the Gemini Enterprise Agent Platform. In April and May, we published a [pre-launch planning guide](/builders-log/gemini-omni-flash-builder-guide-pipeline-architecture-api-rollout/) for when the API opened. This is the update: what is actually available, what the model ID is, and what you need to change in your integration plan.

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

The 1M token context window means you can pass large documents, long video descriptions, or extended conversation histories into a single Omni request. The 720p/24fps output is the preview spec — higher resolution variants are not confirmed for the public preview timeline.

---

## Which API to Use

Google recommends the **Interactions API** for Gemini Omni Flash. The Interactions API was purpose-built for stateful multi-turn interactions and is where new Omni features will land first. The legacy `generateContent` endpoint works but may not surface all preview capabilities.

If your existing infrastructure is built on `generateContent`, it will still function. But for new Omni Flash integrations, start with the Interactions API so you are on the forward path before GA.

The Interactions API uses `client.interactions.create()` and maintains state server-side via `previous_interaction_id`, the same pattern as [Gemini 3.5 Flash Computer Use](/builders-log/gemini-3-5-flash-computer-use-tool-june-24-api-intents-safety-builder-guide/). For pure video generation (not multi-turn editing), a single interaction without a `previous_interaction_id` is sufficient.

---

## Pricing on Vertex AI

Omni Flash pricing on the Gemini API was not published at launch. On Vertex AI, Google has disclosed token-based pricing for the preview:

| Resource | Token count |
|---|---|
| Image input (per image) | 2,040 tokens |
| Audio input (per second) | 32 tokens |
| Video output (per second, 720p) | 5,792 tokens |

Until the Gemini API price sheet is updated, the Vertex AI token counts are the best available proxy for cost modeling. A 10-second video at 720p costs 57,920 output tokens on Vertex. At text token rates that would be trivial, but video tokens are billed at a distinct rate not yet published for the Gemini API tier.

If you are cost-sensitive, stay on Veo 3.1 (published pricing) until Omni Flash publishes its rate card, or test in AI Studio free tier first.

---

## Also GA on June 30: Nano Banana Lite

Alongside the Omni Flash preview launch, Google also brought `gemini-3.1-flash-lite-image` (internally called Nano Banana Lite) to general availability. This is the ultra-low-latency, cost-optimized image generation model — the "lite" counterpart to the Nano Banana 2 (`gemini-3.1-flash-image`) covered in our [Veo 3.1 + Nano Banana 2 guide](/builders-log/veo-3-1-nano-banana-2-google-ai-video-image-generation-builder-guide/).

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

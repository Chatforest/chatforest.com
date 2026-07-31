---
title: "Google June 30: Nano Banana 2 Lite + Gemini Omni Flash API — Builder Guide"
date: 2026-06-30
description: "Google shipped two models on June 30: Nano Banana 2 Lite (gemini-3.1-flash-lite-image) hits GA at $0.034 per image in 4 seconds, and Gemini Omni Flash (gemini-omni-flash-preview) opens its API at $0.10/sec video. Model IDs, pricing math, API patterns, and the decision guide between them and their predecessors."
og_description: "Two Google image/video models hit the Gemini API on June 30. Nano Banana 2 Lite (gemini-3.1-flash-lite-image): GA, 4-second generation, $0.034/image, 1K only. Gemini Omni Flash (gemini-omni-flash-preview): public preview, $0.10/sec video, conversational editing, native audio. Full builder guide: pricing, API patterns, when to use which."
content_type: "Builder's Log"
categories: ["AI Models", "Developer Tools", "Multimodal AI"]
tags: ["google", "gemini", "image-generation", "video-generation", "nano-banana", "gemini-omni-flash", "builders-log", "google-ai-studio", "vertex-ai", "gemini-enterprise-agent-platform"]
sources_audited: 2026-07-31
---

Google shipped two models on June 30, 2026: Nano Banana 2 Lite reached general availability for image generation, and Gemini Omni Flash opened its developer API in public preview for video generation ([Google's launch post](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-flash-nano-banana-2-lite/)). Both are documented on the Gemini Enterprise Agent Platform ([Nano Banana 2 Lite GEAP page](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-1-flash-lite-image); [Gemini Omni Flash GEAP page](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/omni-flash-preview)) as well as the standard Gemini API. This guide covers what each model does, the exact pricing math, the API patterns you need, and when to pick each over its predecessor.

---

## Nano Banana 2 Lite (gemini-3.1-flash-lite-image)

Nano Banana 2 Lite is the speed-and-cost tier of Google's image generation family. The standard Nano Banana 2 (`gemini-3.1-flash-image`) generates images across 1K, 2K, and 4K resolutions ([Gemini API pricing page](https://ai.google.dev/gemini-api/docs/pricing) lists per-resolution pricing for each tier); the Lite version strips that to 1K only (1024×1024) at roughly half the per-image cost of standard at 1K ($0.034 vs. $0.067/image — [pricing page](https://ai.google.dev/gemini-api/docs/pricing)), and Google markets it as the faster tier of the two ([launch post](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-flash-nano-banana-2-lite/)).

**Model ID:** `gemini-3.1-flash-lite-image`  
**Status:** Generally Available (GA) since June 30, 2026 ([launch post](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-flash-nano-banana-2-lite/))  
**Free tier:** Not available — paid plans only ([pricing page](https://ai.google.dev/gemini-api/docs/pricing))

### What it supports

- Text-to-image generation
- Conversational image editing (describe changes; model edits in context) ([Nano Banana image generation docs](https://ai.google.dev/gemini-api/docs/image-generation))
- Character consistency across multiple generations (storyboarding, virtual try-ons) ([launch post](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-flash-nano-banana-2-lite/))
- In-image text rendering in multiple languages ([launch post](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-flash-nano-banana-2-lite/))
- C2PA content credentials and SynthID watermarks, enabled by default ([Gemini 3.1 Flash-Lite Image model card](https://deepmind.google/models/model-cards/gemini-3-1-flash-lite-image/))

### What it does not support

- 2K or 4K resolution output — 1K (1024×1024) only ([Nano Banana image generation docs](https://ai.google.dev/gemini-api/docs/image-generation): "Gemini 3.1 Flash Lite image model only supports 1K resolution")
- Multiple reference inputs or multi-turn sequential editing — the docs state the model is "not optimized for multiple reference inputs or multi-turn sequential editing" ([Nano Banana image generation docs](https://ai.google.dev/gemini-api/docs/image-generation))
- Small text rendering — the model card flags text as "poor in small text (often blurry in 1k model), long paragraphs, page length" ([Gemini 3.1 Flash-Lite Image model card](https://deepmind.google/models/model-cards/gemini-3-1-flash-lite-image/))

### Pricing

| Tier | Image generation | Input tokens | Output tokens |
|---|---|---|---|
| Standard | $30 per 1M tokens (~$0.034/image) | $0.25 per 1M | $1.50 per 1M |
| Batch | $15 per 1M tokens (~$0.017/image) | $0.125 per 1M | $0.75 per 1M |

Source for all figures: [Gemini API pricing page](https://ai.google.dev/gemini-api/docs/pricing), which confirms a 1K image consumes 1,120 output tokens (1,120 × $30/1M = $0.0336/image standard).

At $0.034 per image standard and $0.017 per image batch, Nano Banana 2 Lite is roughly 4× cheaper than Nano Banana 2 standard at 4K ($0.151/image, per the same pricing page) and about 2× cheaper than Nano Banana 2 at 1K ($0.067/image). Provisioned Throughput for Nano Banana 2 Lite is available on the Gemini Enterprise Agent Platform ([GEAP model page](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-1-flash-lite-image)).

### Generation speed

Google's launch post states text-to-image generation completes in about 4 seconds ([launch post](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-flash-nano-banana-2-lite/)). Image editing requests may have slightly higher latency than text-to-image.

### API pattern

The call structure mirrors Nano Banana 2 — same SDK, different model string:

```python
from google import genai
from google.genai import types

client = genai.Client(api_key="YOUR_API_KEY")

response = client.models.generate_images(
    model="gemini-3.1-flash-lite-image",
    prompt="minimalist product shot: matte black water bottle on white surface, soft shadow",
    config=types.GenerateImagesConfig(
        number_of_images=4,
    ),
)

for image in response.generated_images:
    # image.image.image_bytes is raw PNG
    with open(f"variant_{i}.png", "wb") as f:
        f.write(image.image.image_bytes)
```

For batch workloads, submit requests through the Gemini API's [Batch API](https://ai.google.dev/gemini-api/docs/batch-api) — a JSONL file of requests submitted as an async job, priced at the batch rate above, with results retrieved once the job completes (typically well under the 24-hour target turnaround). Provisioned Throughput handles concurrent request pressure for latency-sensitive, non-batch workloads.

### When to use Nano Banana 2 Lite vs Nano Banana 2 standard

| Criteria | Lite (`gemini-3.1-flash-lite-image`) | Standard (`gemini-3.1-flash-image`) |
|---|---|---|
| Required resolution | 1K (1024×1024) | 1K, 2K, or 4K |
| Cost priority | Highest cost sensitivity | Balanced |
| Latency target | ~4 seconds | Higher |
| Use case | E-commerce batch, social media drafts, real-time previews | General production, print, editorial |
| Multi-resolution pipeline | No | Yes |

The practical split: if your pipeline generates at 1K and you run high volumes — e-commerce product variants, social media A/B testing, real-time application assets — Lite is the right default. If you need 2K+ for print or large-format display, or if you're running an image-to-video pipeline where keyframe quality matters downstream (feeding into Veo 3.1), use Nano Banana 2 standard.

### Migration from Nano Banana (Gemini 2.5 Flash Image)

If you are on the original Nano Banana (`gemini-2.5-flash-image`), migration is a model string swap. Google's own launch post names Nano Banana 2 Lite as "our recommended replacement for developers currently using our first version of Nano Banana," positioning it as an immediate swap ([launch post](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-flash-nano-banana-2-lite/)). Google has not published specific regression-testing guidance for the swap, so run a sample of your production prompts on both models before switching if style consistency matters to your pipeline.

---

## Gemini Omni Flash (gemini-omni-flash-preview)

Gemini Omni Flash is Google's any-to-any video generation model, the first release in the new "Gemini Omni" family ([Google's Gemini Omni launch post](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni/)). It was announced at Google I/O on May 19, 2026 — [our review at the time](/builders-log/google-gemini-omni-flash-multimodal-video-generation-review/) noted the developer API was not yet open and flagged it as a Q3 2026 planning item. It arrived in public preview on June 30, ahead of that schedule ([launch post](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-flash-nano-banana-2-lite/)).

**Model ID:** `gemini-omni-flash-preview`  
**Status:** Public Preview since June 30, 2026 ([model page](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash))  
**Free tier:** Not available — paid Gemini API only ([pricing page](https://ai.google.dev/gemini-api/docs/pricing))

### What it does

Gemini Omni Flash accepts text, images, and existing video as input and generates 3–10 second clips at 720p/24fps ([model page](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash)) with native audio — the [Omni docs](https://ai.google.dev/gemini-api/docs/omni) state "the model generates a video with audio based on your text description," created in the same pass as the video rather than added afterward.

The distinguishing capability is **conversational editing**: through the Interactions API, you can issue follow-up prompts to swap characters, relight scenes, alter camera angles, or change object styles in natural language without regenerating the full clip ([Omni docs](https://ai.google.dev/gemini-api/docs/omni)). The model retains context across turns via `previous_interaction_id`.

Other capabilities, per Google's Gemini Omni launch post:

- **Multimodal input**: text + image + video in the same request ([model page](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash))
- **World knowledge in motion**: the model "combines an intuitive understanding of physics with Gemini's knowledge of history, science and cultural context," useful for historically or scientifically grounded scenes ([Gemini Omni launch post](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni/))
- **Text in video**: renders legible text and graphics with kinetic typography synchronized to on-screen movement, though Google flags dense/long text as a known weak spot ([Gemini Omni launch post](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni/))
- **SynthID watermarks**: enabled by default on all generated video ([launch post](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-flash-nano-banana-2-lite/))

### Pricing

| Output type | Cost |
|---|---|
| Video output | $17.50 per 1M tokens (≈ $0.10 per second of 720p video) |
| Text input | $1.50 per 1M tokens |
| Text output | $9.00 per 1M tokens |

Source: [Gemini API pricing page](https://ai.google.dev/gemini-api/docs/pricing), which states billing is "calculated at a rate of 5,792 tokens per second of 720p video," working out to approximately $0.10/second under Standard pricing.

At 5,792 tokens per second of 720p output, a 10-second clip costs approximately $1.01 in video output tokens plus input token costs. Compared against Google's own [Veo 3.1 pricing](https://ai.google.dev/gemini-api/docs/pricing), Gemini Omni Flash's ~$0.10/sec sits close to the Veo 3.1 Fast tier ($0.10/sec at 720p) — well above Veo 3.1 Lite ($0.05/sec at 720p) and below Veo 3.1 Standard ($0.40/sec at 720p/1080p, $0.60/sec at 4K). The tradeoff is capability profile, not just price tier: Omni Flash's strength is conversational editing and multimodal input composition; Veo 3.1 Standard's strength is cinematic fidelity at 4K.

### Coming soon (not in June 30 preview)

Per the [Omni docs limitations section](https://ai.google.dev/gemini-api/docs/omni):

- Audio reference support — "uploading audio references is unsupported in the current version of the API"
- Video reference support — video references up to 3 seconds "are accepted by the API schema but are not correctly processed by the model at this time"
- Video extension and video interpolation (generating video between a first and last frame) — explicitly listed as "not supported"
- Provisioned Throughput — explicitly listed as "not supported"
- Higher resolution outputs beyond 720p — not offered in the current preview

Build around 720p for now and abstract the resolution parameter so you can upgrade without architectural changes.

### API pattern

Gemini Omni Flash uses the standard Google GenAI SDK video generation endpoint. The conversational editing flow works through the Interactions API for multi-turn sessions.

**Single-shot text-to-video:**

```python
from google import genai
from google.genai import types

client = genai.Client(api_key="YOUR_API_KEY")

operation = client.models.generate_videos(
    model="gemini-omni-flash-preview",
    prompt="a street vendor flipping baozi in a night market, steam rising, neon signage reflecting on wet cobblestones",
    config=types.GenerateVideosConfig(
        duration_seconds=8,
        aspect_ratio="16:9",
    ),
)

# Poll for completion
while not operation.done:
    operation = client.operations.get(operation.name)

video_bytes = operation.response.generated_videos[0].video.video_bytes
with open("output.mp4", "wb") as f:
    f.write(video_bytes)
```

**Conversational editing (multi-turn):**

Use the Interactions API to maintain session context across editing turns. Each turn can reference the previous output and apply targeted changes — character swaps, lighting adjustments, camera reframes — without regenerating the full clip from scratch.

### Gemini Omni Flash vs Veo 3.1

Both models generate video via the Gemini API. The profiles diverge on use case. Veo 3.1's GA tier is called "Standard" on Google's own pricing page, not "Quality" — Vertex AI documentation lists `veo-3.1-generate-001` as the GA model ID for that tier (Veo 3.1 Fast and Lite are separate, cheaper tiers; [Vertex AI Veo 3.1 model docs](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/veo/3-1-generate)):

| Criteria | Gemini Omni Flash | Veo 3.1 Standard |
|---|---|---|
| Model ID | `gemini-omni-flash-preview` | `veo-3.1-generate-001` (GA) / `veo-3.1-generate-preview` (Gemini API preview endpoint) |
| Status | Public preview ([model page](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash)) | GA on Vertex AI ([Vertex AI model docs](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/veo/3-1-generate)) |
| Primary strength | Conversational editing, multimodal input | Cinematic quality, 4K |
| Resolution | 720p (more coming) | 720p, 1080p, 4K |
| Pricing | ~$0.10/sec | $0.40/sec (720p/1080p), $0.60/sec (4K) — [pricing page](https://ai.google.dev/gemini-api/docs/pricing) |
| Audio | Native, every output | Native, every output |
| Iterative editing | Yes — multi-turn with context | No — single-shot |

For reference, Google also sells cheaper Veo 3.1 tiers: **Fast** ($0.10/sec at 720p, $0.12/sec at 1080p, $0.30/sec at 4K) and **Lite** ($0.05/sec at 720p, $0.08/sec at 1080p, no 4K) — both per the same [pricing page](https://ai.google.dev/gemini-api/docs/pricing). Omni Flash's ~$0.10/sec lands closest to Veo 3.1 Fast, not Lite.

The short version: if you need iterative creative control in a conversation loop (character swaps, style changes, lighting edits without full regeneration), Omni Flash is the right model. If you need stable production output at 4K or need to lock in an SLA-quality workflow, use Veo 3.1 Standard.

---

## Builder decision guide: June 30 releases in context

**Generating images at volume (e-commerce, social, in-app):** Use Nano Banana 2 Lite (`gemini-3.1-flash-lite-image`). $0.034 per image at 4 seconds. Scale with Provisioned Throughput.

**Generating images at quality (editorial, print, keyframes for video):** Use Nano Banana 2 standard (`gemini-3.1-flash-image`). Supports 2K and 4K. Required if you are feeding keyframes into Veo 3.1.

**Generating video with iterative editing (product swaps, localization variants, collaborative creative):** Use Gemini Omni Flash (`gemini-omni-flash-preview`). Note its current 720p ceiling and incomplete feature set.

**Generating video for production delivery (cinematics, marketing assets, 4K):** Use Veo 3.1 Standard (`veo-3.1-generate-001`, GA on Vertex AI — [Vertex AI model docs](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/veo/3-1-generate)). 4K available.

**Image-to-video pipeline:** Nano Banana 2 standard (not Lite — Lite lacks multi-resolution) → Veo 3.1. Feed the generated PNG as the start frame; the video inherits composition from the image.

---

## What to watch

Gemini Omni Flash's missing features — audio references, video references, last-frame control, scene extension, higher resolutions, and Provisioned Throughput — are the capabilities that would make it production-grade for most multi-step workflows. Google has flagged all of these as "coming soon" without specific dates. Until they ship, treat Omni Flash as an exploration and prototyping tool rather than a production pipeline anchor.

Nano Banana 2 Lite is GA and stable. The only ceiling to plan around is the hard 1K resolution limit.

Access both models via [Google AI Studio](https://aistudio.google.com), the [Gemini API](https://ai.google.dev), and the Gemini Enterprise Agent Platform (GEAP).

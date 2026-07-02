---
title: "Google June 30: Nano Banana 2 Lite + Gemini Omni Flash API — Builder Guide"
date: 2026-06-30
description: "Google shipped two models on June 30: Nano Banana 2 Lite (gemini-3.1-flash-lite-image) hits GA at $0.034 per image in 4 seconds, and Gemini Omni Flash (gemini-omni-flash-preview) opens its API at $0.10/sec video. Model IDs, pricing math, API patterns, and the decision guide between them and their predecessors."
og_description: "Two Google image/video models hit the Gemini API on June 30. Nano Banana 2 Lite (gemini-3.1-flash-lite-image): GA, 4-second generation, $0.034/image, 1K only. Gemini Omni Flash (gemini-omni-flash-preview): public preview, $0.10/sec video, conversational editing, native audio. Full builder guide: pricing, API patterns, when to use which."
content_type: "Builder's Log"
categories: ["AI Models", "Developer Tools", "Multimodal AI"]
tags: ["google", "gemini", "image-generation", "video-generation", "nano-banana", "gemini-omni-flash", "builders-log", "google-ai-studio", "vertex-ai", "gemini-enterprise-agent-platform"]
---

Google shipped two models on June 30, 2026: Nano Banana 2 Lite reached general availability for image generation, and Gemini Omni Flash opened its developer API in public preview for video generation. Both land on the Gemini Enterprise Agent Platform and the standard Gemini API. This guide covers what each model does, the exact pricing math, the API patterns you need, and when to pick each over its predecessor.

---

## Nano Banana 2 Lite (gemini-3.1-flash-lite-image)

Nano Banana 2 Lite is the speed-and-cost tier of Google's image generation family. The standard Nano Banana 2 (`gemini-3.1-flash-image`) generates images across 1K, 2K, and 4K resolutions with balanced quality; the Lite version strips that to 1K only (1024×1024) in exchange for roughly half the cost and roughly half the latency.

**Model ID:** `gemini-3.1-flash-lite-image`  
**Status:** Generally Available (GA) since June 30, 2026  
**Free tier:** Not available — paid plans only

### What it supports

- Text-to-image generation
- Conversational image editing (describe changes; model edits in context)
- Character consistency across multiple generations (storyboarding, virtual try-ons)
- In-image text rendering in multiple languages
- C2PA content credentials and SynthID watermarks, enabled by default

### What it does not support

- 2K or 4K resolution output — 1K (1024×1024) only
- High-complexity compositions — the model card notes slightly weaker performance on multi-input editing vs Nano Banana 2 standard
- Small text rendering below threshold — the model card flags blurriness in small text

### Pricing

| Tier | Image generation | Input tokens | Output tokens |
|---|---|---|---|
| Standard | $30 per 1M tokens (~$0.034/image) | $0.25 per 1M | $1.50 per 1M |
| Batch | $15 per 1M tokens (~$0.017/image) | $0.125 per 1M | $0.75 per 1M |

At $0.034 per image standard and $0.017 per image batch, Nano Banana 2 Lite is roughly 4× cheaper than Nano Banana 2 standard at 4K ($0.151/image) and about 2× cheaper than Nano Banana 2 at 1K. Provisioned Throughput is available for high-concurrency workloads.

### Generation speed

Target is approximately 4 seconds per image. Image editing requests may have slightly higher latency than text-to-image.

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

For batch workloads, target the `batchEmbedContents` endpoint or set up a queue loop — the model itself does not have a native batch API, but Provisioned Throughput handles concurrent request pressure.

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

If you are on the original Nano Banana (`gemini-2.5-flash-image`), migration is a model string swap. Google recommends regression testing for style consistency, as quality characteristics differ between generations. Run a sample of your production prompts on both models before switching.

---

## Gemini Omni Flash (gemini-omni-flash-preview)

Gemini Omni Flash is Google's any-to-any video generation model. It was announced at Google I/O on May 19, 2026 — [our review at the time](/builders-log/google-gemini-omni-flash-multimodal-video-generation-review/) noted the developer API was not yet open and flagged it as a Q3 2026 planning item. It arrived in public preview on June 30, ahead of that schedule.

**Model ID:** `gemini-omni-flash-preview`  
**Status:** Public Preview since June 30, 2026  
**Free tier:** Not available — paid Gemini API only

### What it does

Gemini Omni Flash accepts text, images, and existing video as input and generates 3–10 second clips at 720p with native audio — audio, dialogue, and ambient sound generated in the same pass as the video, not as a post-processing step.

The distinguishing capability is **conversational editing**: you can issue follow-up prompts to swap characters, relight scenes, alter camera angles, or change object styles in natural language without losing scene coherence. The model maintains character and object consistency across multi-turn revision sessions.

Other capabilities:

- **Multimodal input**: text + image + video in the same request
- **World knowledge in motion**: physics understanding plus Gemini's knowledge base — useful for historically or scientifically grounded scenes
- **Text in video**: renders legible text and synchronized kinetic typography
- **SynthID watermarks**: enabled by default on all generated video

### Pricing

| Output type | Cost |
|---|---|
| Video output | $17.50 per 1M tokens (≈ $0.101 per second of 720p video) |
| Text input | $1.50 per 1M tokens |
| Text output | $9.00 per 1M tokens |

At 5,792 tokens per second of 720p output, a 10-second clip costs approximately $1.01 in video output tokens plus input token costs. This places Gemini Omni Flash at roughly the same price per second as Veo 3.1 Lite ($0.15/sec) but lower than Veo 3.1 Quality ($0.60/sec). The tradeoff is capability profile, not price tier: Omni Flash's strength is conversational editing and multimodal input composition; Veo 3.1 Quality's strength is cinematic fidelity at 4K.

### Coming soon (not in June 30 preview)

- Audio reference support (feed a reference audio clip)
- Video reference support
- Last-frame control (specify what the final frame should be)
- Scene extension (continue from an existing clip)
- Higher resolution outputs (beyond 720p)
- Provisioned Throughput for Gemini Omni Flash

These are listed as "coming soon" in the official release announcement. Build around 720p for now and abstract the resolution parameter so you can upgrade without architectural changes.

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

Both models generate video via the Gemini API. The profiles diverge on use case:

| Criteria | Gemini Omni Flash | Veo 3.1 |
|---|---|---|
| Model ID | `gemini-omni-flash-preview` | `veo-3.1-generate-preview` (Quality) |
| Status | Public preview | GA |
| Primary strength | Conversational editing, multimodal input | Cinematic quality, 4K |
| Resolution | 720p (more coming) | 720p, 1080p, 4K |
| Pricing | ~$0.10/sec | $0.15/sec (Lite) to $0.60/sec (Quality) |
| Audio | Native, every output | Native, every output |
| Iterative editing | Yes — multi-turn with context | No — single-shot |
| Preview status | Preview (features incomplete) | GA, stable |

The short version: if you need iterative creative control in a conversation loop (character swaps, style changes, lighting edits without full regeneration), Omni Flash is the right model. If you need stable production output at 4K or need to lock in an SLA-quality workflow, use Veo 3.1 Quality.

---

## Builder decision guide: June 30 releases in context

**Generating images at volume (e-commerce, social, in-app):** Use Nano Banana 2 Lite (`gemini-3.1-flash-lite-image`). $0.034 per image at 4 seconds. Scale with Provisioned Throughput.

**Generating images at quality (editorial, print, keyframes for video):** Use Nano Banana 2 standard (`gemini-3.1-flash-image`). Supports 2K and 4K. Required if you are feeding keyframes into Veo 3.1.

**Generating video with iterative editing (product swaps, localization variants, collaborative creative):** Use Gemini Omni Flash (`gemini-omni-flash-preview`). Note its current 720p ceiling and incomplete feature set.

**Generating video for production delivery (cinematics, marketing assets, 4K):** Use Veo 3.1 Quality (`veo-3.1-generate-preview`). GA, stable, 4K available.

**Image-to-video pipeline:** Nano Banana 2 standard (not Lite — Lite lacks multi-resolution) → Veo 3.1. Feed the generated PNG as the start frame; the video inherits composition from the image.

---

## What to watch

Gemini Omni Flash's missing features — audio references, video references, last-frame control, scene extension, higher resolutions, and Provisioned Throughput — are the capabilities that would make it production-grade for most multi-step workflows. Google has flagged all of these as "coming soon" without specific dates. Until they ship, treat Omni Flash as an exploration and prototyping tool rather than a production pipeline anchor.

Nano Banana 2 Lite is GA and stable. The only ceiling to plan around is the hard 1K resolution limit.

Access both models via [Google AI Studio](https://aistudio.google.com), the [Gemini API](https://ai.google.dev), and the Gemini Enterprise Agent Platform (GEAP).

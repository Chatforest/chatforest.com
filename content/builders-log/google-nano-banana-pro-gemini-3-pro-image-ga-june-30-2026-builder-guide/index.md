---
title: "Nano Banana Pro (gemini-3-pro-image) Builder Guide: Text Rendering, 4K Output, and Editing in One Model"
date: 2026-06-30
description: "Google's Nano Banana Pro (gemini-3-pro-image) reached GA on May 28, 2026, with 4K output, Search-grounded generation, and industry-leading in-image text rendering — at $0.134 per 2K image. Builder guide: the correct model ID, the unified Interactions API for generation and editing, pricing math, and a decision guide against Nano Banana 2 and Imagen 4 Ultra."
og_description: "Nano Banana Pro (gemini-3-pro-image) is GA at $0.134/image (2K) or $0.24 (4K); batch cuts that in half. Unified generation+editing API, Search grounding, text-in-image, up to 5-person identity preservation. Full builder guide: API patterns, decision guide vs. Nano Banana 2 and Imagen 4 Ultra, and builder checklist."
content_type: "Builder's Log"
categories: ["AI Models", "Developer Tools", "Multimodal AI"]
tags: ["google", "gemini", "nano-banana", "image-generation", "multimodal", "builders-log", "google-ai-studio", "vertex-ai", "june-2026"]
sources_audited: 2026-07-31
---

Nano Banana Pro (`gemini-3-pro-image`) and the standard Nano Banana 2 (`gemini-3.1-flash-image`) reached general availability on May 28, 2026, per [Google's Gemini API release notes](https://ai.google.dev/gemini-api/docs/changelog) and the [Google Cloud GA announcement](https://cloud.google.com/blog/products/ai-machine-learning/nano-banana-2-and-nano-banana-pro-are-generally-available/). On June 30, 2026, Google completed the three-tier lineup by shipping [Nano Banana 2 Lite](https://ai.google.dev/gemini-api/docs/changelog) (`gemini-3.1-flash-lite-image`) to GA for high-speed, low-cost generation. Nano Banana Pro is the top tier: 4K output, Search-grounded generation, and — per [Google's own announcement](https://blog.google/technology/ai/nano-banana-pro/) — the strongest in-image text rendering of any model in the Gemini stack.

This guide covers what Nano Banana Pro adds over its siblings, when the cost difference is justified, and how to integrate generation and editing through the current API.

## Model ID

Nano Banana Pro has a single, current model ID: [`gemini-3-pro-image`](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image). It is used for both generation and editing — there is no separate editing endpoint or model ID; both operations go through the same [Interactions API](https://ai.google.dev/gemini-api/docs/image-generation) call, distinguished only by whether you pass an input image alongside the text prompt.

The earlier preview ID, `gemini-3-pro-image-preview`, was retired: per [Google's changelog](https://ai.google.dev/gemini-api/docs/changelog), it was deprecated on May 28, 2026 (the day GA shipped) and shut down entirely on June 25, 2026. Any integration still pointed at the `-preview` ID will fail — use `gemini-3-pro-image`.

## What Nano Banana Pro Adds

### Text rendering in images

In-image text has been a reliable failure mode across image generation models. Google's own launch materials describe Nano Banana Pro as producing readable [text rendering in multiple languages with improved legibility](https://blog.google/technology/ai/nano-banana-pro/), including longer passages. For builders generating infographics, data visualizations, UI mockups, or any asset where legible text matters, Google positions this as a meaningful step up from earlier Gemini image models.

### Editing in the same call

Editing is not a separate endpoint — you call the same [Interactions API](https://ai.google.dev/gemini-api/docs/image-generation) with `model="gemini-3-pro-image"` and pass the source image alongside the text instruction in the `input` array. The model preserves everything not explicitly asked to change, which is useful for iterative creative workflows — adjust a background, swap a color scheme, add a product to an existing scene — without regenerating from scratch.

Reference images are base64-encoded and passed as `image` entries in `input`, per [Google's own code sample](https://ai.google.dev/gemini-api/docs/image-generation):

```python
from google import genai
import base64

client = genai.Client()

with open("original.png", "rb") as f:
    image_bytes = f.read()

interaction = client.interactions.create(
    model="gemini-3-pro-image",
    input=[
        {
            "type": "text",
            "text": "Make the background a sunset gradient"
        },
        {
            "type": "image",
            "data": base64.b64encode(image_bytes).decode("utf-8"),
            "mime_type": "image/png"
        }
    ],
)

with open("edited_image.png", "wb") as f:
    f.write(base64.b64decode(interaction.output_image.data))
```

### 4K output

Nano Banana Pro supports output up to 4K resolution via the `image_size` parameter inside `response_format`, per [Google's documentation](https://ai.google.dev/gemini-api/docs/image-generation) (values must use an uppercase "K" — `"1K"`, `"2K"`, `"4K"`):

```python
response_format = {
    "type": "image",
    "aspect_ratio": "16:9",
    "image_size": "4K",
}
```

4K generation bills at [$0.24 per image](https://ai.google.dev/gemini-api/docs/pricing) rather than the $0.134 standard rate for 1K/2K output.

### Search grounding

Nano Banana Pro can connect image generation to [Google Search's knowledge base](https://blog.google/technology/ai/nano-banana-pro/) to ground outputs in real-world data. This is useful for location-specific imagery, current event illustration, or product environments, but constrains surreal or highly stylized outputs. For most builder use cases, grounding is opt-in; leave it disabled when stylization matters more than factual accuracy.

### Multi-subject identity preservation

Nano Banana Pro preserves consistent visual identity for [up to five people](https://blog.google/technology/ai/nano-banana-pro/) across a generation or editing session. For product photography workflows, character sheets, or multi-person scenes, this is a capability Nano Banana 2 does not match.

## Generation API

Basic generation goes through the same [Interactions API](https://ai.google.dev/gemini-api/docs/image-generation) used for editing, just without an input image:

```python
from google import genai
import base64

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-pro-image",
    input="An infographic comparing quarterly revenue across five product lines, clean sans-serif typography, white background",
)

with open("generated_image.png", "wb") as f:
    f.write(base64.b64decode(interaction.output_image.data))
```

Supported aspect ratios, [per Google's documentation](https://ai.google.dev/gemini-api/docs/image-generation): `1:1`, `3:2`, `2:3`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9`.

## Pricing

| Resolution | Per-image | Batch/Flex |
|------------|-----------|------------|
| 1K or 2K | [$0.134](https://ai.google.dev/gemini-api/docs/pricing) | $0.067 |
| 4K | $0.24 | $0.12 |

(Figures confirmed against [Google's Gemini API pricing page](https://ai.google.dev/gemini-api/docs/pricing).)

Input tokens (prompts, reference images): $2.00/M. These are billed separately from output: text/thinking output tokens are $12.00/M, but **image output tokens are billed at $120.00/M**, not $12.00/M — at 1K/2K, each image consumes approximately 1,120 output tokens (≈$0.134); 4K images consume approximately 2,000 output tokens (≈$0.24). The math only works out to the per-image prices above using the $120/M image-token rate.

Batch/Flex mode cuts rates in half with asynchronous delivery — useful for large overnight generation runs where latency is not a constraint.

There is no free tier for `gemini-3-pro-image`: [Google's pricing page](https://ai.google.dev/gemini-api/docs/pricing) lists "Not available" for free-tier access on this model, unlike some of the lighter Gemini models.

## Decision Guide: Nano Banana Pro vs. Nano Banana 2 vs. Imagen 4 Ultra

| Criterion | Nano Banana Pro | Nano Banana 2 | Imagen 4 Ultra |
|-----------|----------------|---------------|----------------|
| Price (1K/2K) | [$0.134](https://ai.google.dev/gemini-api/docs/pricing) | [$0.067](https://ai.google.dev/gemini-api/docs/pricing) | [$0.06](https://ai.google.dev/gemini-api/docs/pricing) |
| Text in image | Strong ([Google](https://blog.google/technology/ai/nano-banana-pro/)) | Basic | Not a text-focused model |
| Image editing | Same model, same endpoint | Same model, same endpoint | Not supported (generation only) |
| 4K output | Yes ($0.24) | No | No |
| Search grounding | [Yes](https://blog.google/technology/ai/nano-banana-pro/) | No | No |
| Multi-subject identity | [Up to 5 people](https://blog.google/technology/ai/nano-banana-pro/) | Limited | Limited |
| Best for | Infographics, editing, complex scenes | High-volume iteration | Photorealistic portrait, product photo |

We are not publishing specific generation-latency or photorealism-ranking numbers here: third-party benchmarks for these three models vary widely (some report Nano Banana Pro at single-digit seconds, others at 8–20+ seconds, depending on prompt complexity and load), and Google has not published its own comparative latency figures. Test latency against your own prompts before committing to a model on speed grounds.

**Use Nano Banana Pro when:** text legibility in the image matters; you need to edit existing assets without switching models; 4K output is required; or you need Search-grounded factual accuracy.

**Use Nano Banana 2 when:** you are generating at volume and cost efficiency matters more than text rendering quality.

**Use Imagen 4 Ultra when:** photorealistic portraits or product photography is the primary output and you don't need in-model editing. Note that [Google has scheduled the Imagen 4 standard, ultra, and fast endpoints for shutdown on August 17, 2026](https://ai.google.dev/gemini-api/docs/models/imagen), pointing migrators at Gemini 3.1 Flash Image (Nano Banana 2) — plan accordingly if you're building new on Imagen 4 Ultra.

## SynthID Watermarking

All Nano Banana Pro outputs embed an invisible [SynthID watermark](https://deepmind.google/models/synthid/) in the pixel data. Google's own [SynthID Detector](https://blog.google/innovation-and-ai/products/google-synthid-ai-content-detector/) verification tool can check whether a given image carries the watermark, and Google states the mark is not visible to the naked eye. If a workflow needs to confirm provenance downstream, use SynthID Detector rather than assuming the watermark is human-detectable.

## Builder Checklist

- [ ] Use `gemini-3-pro-image` for both generation and editing — the old `gemini-3-pro-image-preview` ID was shut down June 25, 2026 and will error
- [ ] Call the unified [Interactions API](https://ai.google.dev/gemini-api/docs/image-generation) (`client.interactions.create()`) for both — editing is generation with an image added to the `input` array, not a separate model or endpoint
- [ ] For 4K output, set `image_size: "4K"` inside `response_format` (uppercase "K" required) — `aspect_ratio` alone does not raise resolution
- [ ] Use Batch/Flex mode for offline generation runs to halve per-image costs
- [ ] Disable Search grounding when stylization matters more than factual accuracy
- [ ] Test text rendering quality against your specific font and language requirements before committing to Nano Banana Pro — if your use case does not embed text, Nano Banana 2 covers the same use case at roughly [half the per-image cost](https://ai.google.dev/gemini-api/docs/pricing) ($0.067 vs. $0.134 at 1K/2K)
- [ ] For multi-subject workflows, confirm identity preservation across the images you intend to generate — Google states support for [up to five people](https://blog.google/technology/ai/nano-banana-pro/), and quality may degrade beyond that
- [ ] If you need video output, Veo 3.1 supports [using a still image as the first frame](https://ai.google.dev/gemini-api/docs/veo) of a generated video — a Nano Banana Pro output can serve as that starting frame
- [ ] If you're on Imagen 4 Ultra today, note its [scheduled shutdown on August 17, 2026](https://ai.google.dev/gemini-api/docs/models/imagen) and plan a migration path to Gemini 3.1 Flash Image or Nano Banana Pro

## What to Watch

The `gemini-3-pro-image-preview` model ID is already gone — it was shut down June 25, 2026, five days before this guide's original publish date. Pin your model ID as a configuration constant rather than hardcoding it inline, since Google has shown with this launch that it will retire preview IDs on a firm schedule once GA ships.

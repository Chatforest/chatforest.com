---
title: "Nano Banana Pro (gemini-3-pro-image) Is GA: Text Rendering, 4K Output, and Editing in One Model"
date: 2026-06-30
description: "Google's Nano Banana Pro (gemini-3-pro-image-preview) hit GA on June 30, 2026. It adds a dedicated editing endpoint, 4K output, Search-grounded generation, and industry-leading in-image text rendering — at $0.134 per 2K image. Builder guide: model IDs, pricing math, decision guide against Nano Banana 2 and Imagen 4 Ultra, and when the extra cost is justified."
og_description: "Nano Banana Pro (gemini-3-pro-image-preview) went GA June 30. $0.134/image (2K) or $0.24 (4K), batch cuts that in half. Editing endpoint, Search grounding, text-in-image, up to 5-subject identity preservation. Full builder guide: API patterns, decision guide vs. Nano Banana 2 and Imagen 4 Ultra, and builder checklist."
content_type: "Builder's Log"
categories: ["AI Models", "Developer Tools", "Multimodal AI"]
tags: ["google", "gemini", "nano-banana", "image-generation", "multimodal", "builders-log", "google-ai-studio", "vertex-ai", "june-2026"]
---

Google shipped three Nano Banana image models to general availability on June 30, 2026. The Lite variant (`gemini-3.1-flash-lite-image`) covers high-speed, low-cost generation. The standard Nano Banana 2 (`gemini-3.1-flash-image`) handles the volume middle tier. Nano Banana Pro (`gemini-3-pro-image-preview`) is the top tier: a dedicated editing endpoint, 4K output, Search-grounded generation, and the strongest in-image text rendering of any model in the Gemini stack.

This guide covers what Nano Banana Pro adds over its siblings, when the cost difference is justified, and how to integrate both the generation and editing endpoints.

## Model IDs

Nano Banana Pro ships with two distinct endpoints:

| Mode | Model ID |
|------|----------|
| Generation | `gemini-3-pro-image-preview` |
| Editing | `gemini-3-pro-image-preview-edit` |

The "preview" suffix in the model ID is retained even at GA — use these IDs exactly; the preview variants do not point to the same models.

## What Nano Banana Pro Adds

### Text rendering in images

In-image text has been a reliable failure mode across image generation models. Nano Banana Pro is Google's answer: it reliably produces readable text in generated images, including long passages and multilingual layouts. For builders generating infographics, data visualizations, UI mockups, or any asset where legible text matters, this is the first Gemini image model where text rendering is not a workaround problem.

### Editing endpoint

The `gemini-3-pro-image-preview-edit` endpoint accepts an original image and a natural language instruction. It preserves everything not explicitly asked to change. This is useful for iterative creative workflows — adjust a background, swap a color scheme, add a product to an existing scene — without regenerating from scratch.

Reference image submission uses base64 encoding in the `reference_images` parameter:

```python
from google import genai
from google.genai import types

client = genai.Client()

with open("original.png", "rb") as f:
    image_bytes = f.read()

response = client.models.edit_image(
    model="gemini-3-pro-image-preview-edit",
    prompt="Make the background a sunset gradient",
    reference_images=[
        types.RawReferenceImage(
            reference_image=types.Image(image_bytes=image_bytes),
            reference_id=0,
        )
    ],
    config=types.EditImageConfig(
        number_of_images=1,
        output_mime_type="image/png",
    ),
)
```

### 4K output

Both Nano Banana 2 and Nano Banana Lite top out at lower resolutions. Nano Banana Pro supports custom dimensions up to 4096×4096, configured via `output_image_config`:

```python
config=types.GenerateImagesConfig(
    number_of_images=1,
    output_mime_type="image/png",
    aspect_ratio="16:9",
    output_image_config={"width": 3840, "height": 2160}  # 4K 16:9
)
```

4K generation bills at $0.24 per image rather than the standard $0.134.

### Search grounding

Nano Banana Pro can ground image generation in real-world data via Search. This constrains outputs to factual accuracy — useful for location-specific imagery, current event illustration, or product environments — but limits surreal or highly stylized outputs. For most builder use cases, grounding is opt-in; leave it disabled when stylization matters more than accuracy.

### Multi-subject identity preservation

Nano Banana Pro preserves consistent visual identity for up to five distinct subjects across a generation or editing session. For product photography workflows, character sheets, or multi-person scenes, this is the enabling capability that Nano Banana 2 does not fully support.

## Generation API

Basic generation follows the same `generate_images` pattern as other Nano Banana models:

```python
response = client.models.generate_images(
    model="gemini-3-pro-image-preview",
    prompt="An infographic comparing quarterly revenue across five product lines, clean sans-serif typography, white background",
    config=types.GenerateImagesConfig(
        number_of_images=1,
        output_mime_type="image/png",
        aspect_ratio="16:9",
    ),
)

image_data = response.generated_images[0].image.image_bytes
```

Supported aspect ratios: `1:1`, `16:9`, `9:16`, `4:3`, `3:4`.

SDK minimums: Python v1.52+, JavaScript/TypeScript v1.30+.

## Pricing

| Resolution | Per-image | Batch/Flex |
|------------|-----------|------------|
| 1K or 2K | $0.134 | $0.067 |
| 4K | $0.24 | $0.12 |

Input tokens (prompts, reference images): $2.00/M. Output tokens: $12.00/M. At 1K/2K, each image consumes approximately 1,120 output tokens; 4K images consume approximately 2,000 output tokens.

Batch/Flex mode (Vertex AI only) cuts rates in half with asynchronous delivery — useful for large overnight generation runs where latency is not a constraint.

Free tier: 200 images per day through Google AI Studio before billing begins.

## Decision Guide: Nano Banana Pro vs. Nano Banana 2 vs. Imagen 4 Ultra

| Criterion | Nano Banana Pro | Nano Banana 2 | Imagen 4 Ultra |
|-----------|----------------|---------------|----------------|
| Price (2K) | $0.134 | ~$0.02–$0.04 | $0.06 |
| Speed | 2–5s | <2s | 15–30s |
| Text in image | Strong | Basic | Weak |
| Image editing | Dedicated endpoint | Not available | Not available |
| 4K output | Yes ($0.24) | No | No |
| Photorealism | Good | Moderate | Industry-best |
| Search grounding | Yes | No | No |
| Multi-subject identity | Up to 5 | Limited | Limited |
| Best for | Infographics, editing, complex scenes | High-volume iteration | Portrait, product photo |

**Use Nano Banana Pro when:** text legibility in the image matters; you need an editing endpoint to modify existing assets; 4K output is required; or you need factual accuracy from Search grounding.

**Use Nano Banana 2 when:** you are generating at volume and cost efficiency matters more than text rendering or editing capabilities.

**Use Imagen 4 Ultra when:** photorealistic portraits or product photography is the primary output, and speed is not a constraint.

## SynthID Watermarking

All Nano Banana Pro outputs embed an invisible SynthID watermark in the pixel data. The watermark is non-optional, does not affect visual quality, and is detectable by Google's verification tools. Workflows that pass images downstream should account for watermark persistence through compression and light editing operations.

## Builder Checklist

- [ ] Update SDK to Python v1.52+ or JS/TS v1.30+ — earlier versions lack typed support for `gemini-3-pro-image-preview`
- [ ] Use `gemini-3-pro-image-preview` for generation, `gemini-3-pro-image-preview-edit` for editing — they are distinct model IDs, not interchangeable
- [ ] For 4K output, set `output_image_config` with explicit `width`/`height` — the `aspect_ratio` param alone caps at 2K
- [ ] Enable Batch/Flex mode (Vertex AI) for offline generation runs to halve per-image costs
- [ ] Disable Search grounding when stylization matters more than factual accuracy
- [ ] Test text rendering quality against your specific font and language requirements before committing to Nano Banana Pro — if your use case does not embed text, Nano Banana 2 covers the same use case at 3–7x lower cost
- [ ] For multi-subject workflows, confirm identity preservation across the images you intend to generate — it is accurate for up to five subjects but may degrade beyond that
- [ ] Connect to the Veo 3.1 pipeline when you need video output: generate a keyframe with Nano Banana Pro, pass it as a start frame to Veo 3.1 for high-quality video continuation

## What to Watch

Google has not announced a GA model ID without the "preview" suffix yet. If Google moves to `gemini-3-pro-image` at stable GA, existing integrations using `gemini-3-pro-image-preview` will need a model ID update — pin your model ID as a configuration constant rather than hardcoding it inline to make this migration a single-line change.

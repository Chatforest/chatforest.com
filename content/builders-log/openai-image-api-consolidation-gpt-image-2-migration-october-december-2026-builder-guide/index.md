---
title: "OpenAI Image API Consolidation: gpt-image-1 Sunsets Oct 23, Three More Dec 1 — Migrate to gpt-image-2"
date: 2026-07-12
description: "OpenAI is retiring its entire image API family down to a single model. gpt-image-1 sunsets October 23, 2026; gpt-image-1-mini, gpt-image-1.5, and chatgpt-image-latest sunset December 1, 2026. Builders who migrated from DALL-E 3 to gpt-image-1-mini just months ago now face their second forced migration in under a year. This guide covers the timeline, what gpt-image-2 adds, the request shape change, cost impact by tier, and the migration checklist."
tags: ["openai", "image-generation", "gpt-image-2", "gpt-image-1", "dalle", "api", "builder-guide", "deprecation", "migration"]
---

OpenAI is consolidating its entire image generation API into a single model: **gpt-image-2**. Four image API routes are being retired across two deadlines this fall.

- **October 23, 2026**: `gpt-image-1` sunsets
- **December 1, 2026**: `gpt-image-1-mini`, `gpt-image-1.5`, and `chatgpt-image-latest` sunset

Calls to retired routes return errors after their deadline.

This is a research-based summary. We have not tested any of these endpoints directly.

---

## The migration treadmill

To understand why this announcement stings, trace the timeline:

**May 12, 2026** — DALL-E 2 and DALL-E 3 retire. OpenAI's documented migration path pointed developers at `gpt-image-1-mini` as the replacement.

**April 21, 2026** — `gpt-image-2` releases. OpenAI's next-generation image model is available in the API.

**June 2, 2026** — OpenAI notifies developers: `gpt-image-1-mini`, `gpt-image-1.5`, and `chatgpt-image-latest` will retire December 1, 2026. `gpt-image-1` gets a separate October 23 sunset.

The result: developers who followed OpenAI's guidance and migrated from DALL-E 3 to `gpt-image-1-mini` in May 2026 now need to migrate again before December 1 — a second forced migration within roughly six months.

---

## Sunset timeline at a glance

| Model | Sunset date | Call behavior after |
|-------|------------|---------------------|
| `gpt-image-1` | October 23, 2026 | Returns error |
| `gpt-image-1-mini` | December 1, 2026 | Returns error |
| `gpt-image-1.5` | December 1, 2026 | Returns error |
| `chatgpt-image-latest` | December 1, 2026 | Returns error |
| `gpt-image-2` | Not announced | Target model |

---

## What gpt-image-2 adds

Released April 21, 2026, `gpt-image-2` is architecturally different from the `gpt-image-1` family. The key additions:

**Agentic reasoning before generation.** The model researches, plans, and reasons about the image structure before generating pixels. This materially improves complex scenes, spatial relationships, and prompts requiring factual accuracy.

**Near-perfect text rendering.** Small text, UI elements, code listings, packaging copy, and manga panels render cleanly. Earlier models produced consistent artifacts on dense text. Non-Latin scripts (Japanese, Korean, Chinese, Hindi, Bengali) achieve character-level accuracy.

**Web search integration.** The model can retrieve current information to overcome its training cutoff, relevant for prompts requiring recent brand assets, event imagery, or up-to-date product designs.

**Higher resolution output.** Support extends up to 3840×2160 (4K). Custom dimensions work as long as both edges are multiples of 16.

---

## Request shape change

The biggest code change is how you specify output quality.

The `gpt-image-1.x` family used a `quality` parameter with string values:

```python
# old shape (gpt-image-1, gpt-image-1-mini, gpt-image-1.5)
response = client.images.generate(
    model="gpt-image-1-mini",
    prompt="a product photo of a ceramic mug on a white background",
    quality="medium",  # low | medium | high
    size="1024x1024",
)
image_b64 = response.data[0].b64_json
```

`gpt-image-2` replaces `quality` with explicit resolution selection:

```python
# new shape (gpt-image-2)
response = client.images.generate(
    model="gpt-image-2",
    prompt="a product photo of a ceramic mug on a white background",
    size="1024x1024",   # 1K: 1024x1024
    # size="2048x2048"  # 2K
    # size="4096x4096"  # 4K
)
image_b64 = response.data[0].b64_json
```

The response format (`data[0].b64_json`) is unchanged. The `model` string changes. The `quality` parameter is removed; resolution selection takes its place.

For image editing (`client.images.edit()`), the same model substitution and size-parameter pattern applies.

---

## Cost impact by tier

`gpt-image-2` uses token-based pricing. OpenAI's calculator translates this to per-image estimates at standard 1024×1024:

| Model | Per-image cost (1024×1024) | Quality analog |
|-------|---------------------------|----------------|
| `gpt-image-1-mini` | ~$0.005 (low) | Low |
| `gpt-image-1.5` | ~$0.133 (high) | High |
| `gpt-image-2` | ~$0.006 (low equiv) | Low |
| `gpt-image-2` | ~$0.053 (medium) | Medium |
| `gpt-image-2` | ~$0.211 (high equiv) | High |

For **mini users**: migration to `gpt-image-2` at equivalent low-output size is roughly a 20% price increase ($0.005 → ~$0.006). Significant at volume but not catastrophic.

For **gpt-image-1.5 users at high quality**: migration to `gpt-image-2` high is a roughly 59% price increase ($0.133 → ~$0.211). Budget for this before the deadline.

**Cost mitigation**: The Batch API halves token rates for requests that can tolerate up to 24-hour latency. For high-volume generation pipelines that aren't latency-sensitive, batching drops effective per-image cost roughly in half. Cached text inputs fall from $5.00 to $1.25 per million tokens when the same prompt is reused at scale.

Edit requests cost more than generation-only requests because you're paying image input tokens for the reference image on top of output tokens. Factor this into iterative workflows.

---

## Migration checklist

**Before October 23 (gpt-image-1 users):**
- [ ] Identify all `model="gpt-image-1"` call sites in production
- [ ] Test `gpt-image-2` prompts against your existing prompt library
- [ ] Swap the model string, remove the `quality` parameter, verify size selection
- [ ] Update cost monitoring — token-based billing requires different calculations
- [ ] Deploy to staging, verify output quality is acceptable for your use case

**Before December 1 (gpt-image-1-mini, gpt-image-1.5, chatgpt-image-latest users):**
- [ ] Same steps as above for each affected route
- [ ] Recalculate unit economics — especially for gpt-image-1.5 high-quality users facing a ~59% per-image increase
- [ ] Evaluate Batch API for non-latency-sensitive generation to halve costs
- [ ] Remove any logic keyed to the old `quality` string values

**General:**
- [ ] Update error handling — the retired model routes return errors, not degraded results
- [ ] Do not alias `chatgpt-image-latest` and expect continuity — this route is retiring too
- [ ] `gpt-image-2` prompts from earlier models carry over and typically produce better results, since the model follows instructions more closely

---

## What to watch

**Pricing adjustments**: OpenAI has lowered prices on other models as usage scales. It is plausible — not confirmed — that `gpt-image-2` pricing drops after the consolidation completes.

**gpt-image-1-mini replacement**: Community forums have raised the question of whether OpenAI will offer a budget-tier image model after December 1. No announcement has been made. For now, `gpt-image-2` at low resolution is the closest analog.

**Batch API expansion**: If OpenAI extends Batch API support more broadly to image generation, the effective cost picture improves for high-volume use cases.

---

## Resources

- [OpenAI Deprecations page](https://developers.openai.com/api/docs/deprecations)
- [OpenAI Image Generation guide](https://developers.openai.com/api/docs/guides/image-generation)
- [OpenAI Community — deprecation notice thread](https://community.openai.com/t/deprecation-notice-upcoming-model-shutdowns-in-2026/1379553)
- [AI Weekly — OpenAI Deprecates Three Image APIs](https://aiweekly.co/alerts/openai-deprecates-three-image-apis-by-december-2026)
- [Unifically — GPT Image 1 vs 1.5 vs 2 comparison](https://unifically.com/blogs/gpt-image-1-vs-1.5-vs-2)

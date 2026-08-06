---
title: "OpenAI Image API Consolidation: gpt-image-1 Sunsets Oct 23, Three More Dec 1 — Migrate to gpt-image-2"
date: 2026-07-12
sources_audited: 2026-08-06
description: "OpenAI is retiring its entire image API family down to a single model. gpt-image-1 sunsets October 23, 2026; gpt-image-1-mini, gpt-image-1.5, and chatgpt-image-latest sunset December 1, 2026. Builders who migrated from DALL-E 3 to gpt-image-1-mini just months ago now face their second forced migration in under a year. This guide covers the timeline, what gpt-image-2 adds, the request shape change, cost impact by tier, and the migration checklist."
tags: ["openai", "image-generation", "gpt-image-2", "gpt-image-1", "dalle", "api", "builder-guide", "deprecation", "migration"]
---

OpenAI is consolidating its entire image generation API into a single model: **gpt-image-2**. Four image API routes are being retired across two deadlines this fall, per [OpenAI's Deprecations page](https://developers.openai.com/api/docs/deprecations).

- **October 23, 2026**: `gpt-image-1` sunsets
- **December 1, 2026**: `gpt-image-1-mini`, `gpt-image-1.5`, and `chatgpt-image-latest` sunset

Calls to retired routes return errors after their deadline, per the same [Deprecations page](https://developers.openai.com/api/docs/deprecations).

This is a research-based summary. We have not tested any of these endpoints directly.

---

## The migration treadmill

To understand why this announcement stings, trace the timeline:

**May 12, 2026** — DALL-E 2 and DALL-E 3 retire, [as OpenAI announced on November 14, 2025](https://developers.openai.com/api/docs/deprecations). OpenAI's documented migration path pointed developers at `gpt-image-2`, `gpt-image-1`, or `gpt-image-1-mini` as replacements.

**April 21, 2026** — `gpt-image-2` releases. OpenAI's next-generation image model becomes available in the API and Codex the same day ([OpenAI, "Introducing ChatGPT Images 2.0"](https://openai.com/index/introducing-chatgpt-images-2-0/); [OpenAI Developer Community announcement](https://community.openai.com/t/introducing-gpt-image-2-available-today-in-the-api-and-codex/1379479)).

**June 2, 2026** — OpenAI notifies developers: `gpt-image-1-mini`, `gpt-image-1.5`, and `chatgpt-image-latest` will retire December 1, 2026 ([OpenAI Deprecations page](https://developers.openai.com/api/docs/deprecations); [community deprecation notice](https://community.openai.com/t/deprecation-notice-upcoming-model-shutdowns-in-2026/1379553)). `gpt-image-1` gets a separate October 23 sunset, [also listed on the Deprecations page](https://developers.openai.com/api/docs/deprecations).

The result: developers who picked `gpt-image-1-mini` — one of OpenAI's three listed replacements — when migrating off DALL-E 3 in May 2026 now need to migrate again before December 1 — a second forced migration within roughly six months.

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

Released April 21, 2026, `gpt-image-2` is architecturally different from the `gpt-image-1` family ([OpenAI, "Introducing ChatGPT Images 2.0"](https://openai.com/index/introducing-chatgpt-images-2-0/)). The key additions:

**Agentic reasoning before generation.** OpenAI describes the model as a "visual thought partner" that can "research, reason, transform source materials, and generate polished visuals end-to-end" before producing pixels ([OpenAI launch post](https://openai.com/index/introducing-chatgpt-images-2-0/); [OpenAI Developer Community announcement](https://community.openai.com/t/introducing-gpt-image-2-available-today-in-the-api-and-codex/1379479)). This is reported to materially improve complex scenes, spatial relationships, and prompts requiring factual accuracy ([The Decoder coverage](https://the-decoder.com/openais-chatgpt-images-2-0-thinks-before-it-generates-adding-reasoning-and-web-search-to-image-creation/)).

**Improved text rendering.** OpenAI's own [API guide](https://developers.openai.com/api/docs/guides/image-generation) says text rendering is "significantly improved" over prior models, though it "can still struggle with precise text placement and clarity" — so treat "near-perfect" claims from third-party coverage with some skepticism. The launch post demonstrates rendering across multiple non-Latin scripts, including Japanese, Korean, Chinese, Arabic, Devanagari (Hindi), and Bengali ([OpenAI launch post](https://openai.com/index/introducing-chatgpt-images-2-0/)); independent write-ups report noticeably fewer artifacts on dense text and UI mockups than earlier models ([VentureBeat](https://venturebeat.com/technology/openais-chatgpt-images-2-0-is-here-and-it-does-multilingual-text-full-infographics-slides-maps-even-manga-seemingly-flawlessly)).

**Web search integration.** OpenAI's launch post references "thinking mode search capabilities," and reporting on the launch describes the model retrieving current information (e.g., a brand's current logo or a venue's appearance) before generating, to work around its training cutoff ([OpenAI launch post](https://openai.com/index/introducing-chatgpt-images-2-0/); [The Decoder coverage](https://the-decoder.com/openais-chatgpt-images-2-0-thinks-before-it-generates-adding-reasoning-and-web-search-to-image-creation/)).

**Higher resolution output.** Support extends up to 3840×2160 (4K); custom dimensions must have both edges as multiples of 16px, a maximum edge of 3840px, and total pixels between 655,360 and 8,294,400, per [OpenAI's image generation guide](https://developers.openai.com/api/docs/guides/image-generation). Note OpenAI's own launch materials describe resolution "up to 2K" as the headline spec, with 4K available as a documented API option.

---

## Request shape change

Contrary to some third-party migration write-ups, `gpt-image-2` does **not** drop the `quality` parameter — per [OpenAI's image generation guide](https://developers.openai.com/api/docs/guides/image-generation), it accepts the same `quality` values (`low`, `medium`, `high`, `auto`) as the `gpt-image-1.x` family, used alongside `size`:

```python
# gpt-image-1-mini (unchanged parameter shape)
response = client.images.generate(
    model="gpt-image-1-mini",
    prompt="a product photo of a ceramic mug on a white background",
    quality="medium",  # low | medium | high
    size="1024x1024",
)
image_b64 = response.data[0].b64_json
```

```python
# gpt-image-2 — same parameter names, new size ceiling
response = client.images.generate(
    model="gpt-image-2",
    prompt="a product photo of a ceramic mug on a white background",
    quality="medium",   # low | medium | high | auto
    size="1024x1024",   # 1K square
    # size="2048x2048"  # 2K square
    # size="3840x2160"  # 4K landscape
)
image_b64 = response.data[0].b64_json
```

The response format (`data[0].b64_json`) is unchanged and the `model` string changes, but the real shape change is on the `size` side: `gpt-image-2` adds 2K and 4K presets (`2048x2048`, `3840x2160`, `2160x3840`) beyond the `gpt-image-1.x` family's 1K-class sizes, and OpenAI flags anything above `2560x1440` total pixels (roughly 2K) as "experimental" ([image generation guide](https://developers.openai.com/api/docs/guides/image-generation)). `gpt-image-2` also drops support for `background: "transparent"`, which the `gpt-image-1.x` family supports — a real regression to check for if your pipeline generates transparent PNGs ([image generation guide](https://developers.openai.com/api/docs/guides/image-generation)).

For image editing (`client.images.edit()`), the same model-substitution pattern applies, but `gpt-image-2` always processes reference images at high fidelity and does not let you configure fidelity down, per the same guide.

---

## Cost impact by tier

All of these models — old and new — are billed on token-based pricing, not a flat per-image rate. [OpenAI's image generation guide](https://developers.openai.com/api/docs/guides/image-generation) gives these per-image cost estimates at standard 1024×1024:

| Model | Per-image cost (1024×1024) | Quality analog |
|-------|---------------------------|----------------|
| `gpt-image-1-mini` | ~$0.005 (low) | Low |
| `gpt-image-1.5` | ~$0.133 (high) | High |
| `gpt-image-2` | ~$0.006 (low equiv) | Low |
| `gpt-image-2` | ~$0.053 (medium) | Medium |
| `gpt-image-2` | ~$0.211 (high equiv) | High |

For **mini users**: migration to `gpt-image-2` at equivalent low-output size is roughly a 20% price increase ($0.005 → ~$0.006). Significant at volume but not catastrophic.

For **gpt-image-1.5 users at high quality**: migration to `gpt-image-2` high is a roughly 59% price increase ($0.133 → ~$0.211). Budget for this before the deadline.

**Cost mitigation**: [OpenAI's Batch API](https://developers.openai.com/api/docs/guides/batch) already applies to image generation models today, halves token rates, and runs on a 24-hour completion window (per the [Batch API guide](https://developers.openai.com/api/docs/guides/batch) and [pricing page](https://developers.openai.com/api/docs/pricing)). For high-volume generation pipelines that aren't latency-sensitive, batching drops effective per-image cost roughly in half. Per the same [pricing page](https://developers.openai.com/api/docs/pricing), cached text inputs for `gpt-image-2` fall from $5.00 to $1.25 per million tokens when the same prompt is reused at scale.

Edit requests cost more than generation-only requests: `gpt-image-2` always processes the reference image at high fidelity (this isn't configurable down, per the [image generation guide](https://developers.openai.com/api/docs/guides/image-generation)), so you're paying image input tokens for the reference image on top of output tokens. Factor this into iterative workflows.

---

## Migration checklist

**Before October 23 (gpt-image-1 users):**
- [ ] Identify all `model="gpt-image-1"` call sites in production
- [ ] Test `gpt-image-2` prompts against your existing prompt library
- [ ] Swap the model string, keep `quality` and `size` (both still apply to `gpt-image-2`), and check whether you want the new 2K/4K size presets
- [ ] Update cost monitoring for the new per-size, per-quality token rates ([pricing page](https://developers.openai.com/api/docs/pricing))
- [ ] If you rely on `background: "transparent"`, note `gpt-image-2` does not support it ([image generation guide](https://developers.openai.com/api/docs/guides/image-generation))
- [ ] Deploy to staging, verify output quality is acceptable for your use case

**Before December 1 (gpt-image-1-mini, gpt-image-1.5, chatgpt-image-latest users):**
- [ ] Same steps as above for each affected route
- [ ] Recalculate unit economics — especially for gpt-image-1.5 high-quality users facing a ~59% per-image increase
- [ ] Evaluate Batch API for non-latency-sensitive generation to halve costs
- [ ] Re-check any logic keyed to `quality` string values — the parameter still exists on `gpt-image-2`, but the price-per-tier and size ceiling changed

**General:**
- [ ] Update error handling — the retired model routes return errors, not degraded results, per [OpenAI's Deprecations page](https://developers.openai.com/api/docs/deprecations)
- [ ] Do not alias `chatgpt-image-latest` and expect continuity — this route is retiring too
- [ ] Re-test your existing prompt library against `gpt-image-2` rather than assuming a like-for-like swap; independent coverage reports fewer artifacts on dense text and better instruction-following, but "quality" is judged per use case ([VentureBeat](https://venturebeat.com/technology/openais-chatgpt-images-2-0-is-here-and-it-does-multilingual-text-full-infographics-slides-maps-even-manga-seemingly-flawlessly))

---

## What to watch

**Pricing adjustments**: OpenAI has cut prices on other models as usage scaled and competitive pressure increased — for example, [cutting GPT-5.6 Terra and Luna pricing in July 2026](https://www.cnbc.com/2026/07/30/open-ai-price-cut-gpt.html). It is plausible — not confirmed — that `gpt-image-2` pricing drops after the consolidation completes.

**gpt-image-1-mini replacement**: Whether OpenAI will offer a budget-tier image model after December 1 has been [raised by developers on OpenAI's community forum](https://community.openai.com/t/replacement-for-gpt-image-1-mini/1382424), but no OpenAI staff announcement has been made as of this writing. For now, `gpt-image-2` at low quality is the closest analog.

---

## Resources

- [OpenAI Deprecations page](https://developers.openai.com/api/docs/deprecations)
- [OpenAI Image Generation guide](https://developers.openai.com/api/docs/guides/image-generation)
- [OpenAI Community — deprecation notice thread](https://community.openai.com/t/deprecation-notice-upcoming-model-shutdowns-in-2026/1379553)
- [AI Weekly — OpenAI Deprecates Three Image APIs](https://aiweekly.co/alerts/openai-deprecates-three-image-apis-by-december-2026)
- [Unifically — GPT Image 1 vs 1.5 vs 2 comparison](https://unifically.com/blogs/gpt-image-1-vs-1.5-vs-2)

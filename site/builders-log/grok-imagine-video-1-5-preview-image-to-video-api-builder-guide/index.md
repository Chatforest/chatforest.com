# Grok Imagine Video 1.5 Preview: xAI's Image-to-Video API Hits #1 — Builder Guide

> xAI shipped grok-imagine-video-1.5-preview on June 3, 2026 — API-first, before any consumer rollout. It claims the top spot on image-to-video leaderboards with native audio included. Here is what builders actually get.


On June 3, 2026, xAI pushed `grok-imagine-video-1.5-preview` to the public API — before it appeared anywhere in the consumer Grok products. That is not how most AI companies roll out video models. Most launch in the consumer product first, add the API months later, and define pricing as an afterthought. xAI inverted the sequence: builders got it first, with firm pricing, a documented rate limit, and region availability.

The model has since claimed the top spot on the [Image-to-Video Arena leaderboard](https://kearai.com/leaderboard/image-to-video) by KEAR AI, recording a +52 Elo jump over its predecessor and beating ByteDance's Seedance 2.0, Alibaba ATH's HappyHorse 1.0, and Google Veo in head-to-head comparisons.

This guide covers what is technically new, the API details you need to integrate it, an honest look at the benchmark caveats, and how it compares against Veo 3.1, Kling, and Seedance 2.0.

---

## What Is Grok Imagine Video 1.5?

`grok-imagine-video-1.5-preview` is an **image-to-video model**. You give it a static image and a text prompt describing the motion you want, and it animates the scene — camera moves, atmosphere, lighting continuity, and physics — into a short video clip.

It is **not** a text-to-video model. The preview release does not support generating video from a text prompt alone; it requires an input image. That is a meaningful constraint for some workflows and irrelevant for others.

The standout technical addition over 1.0 is **native audio**: the model generates synchronized sound — dialogue, sound effects, ambient audio, music — in the same inference pass as the video. There is no second step. Competing models either skip audio entirely or layer it with a separate audio model in a post-processing pass that tends to drift out of sync with on-screen motion.

---

## API Specs

**Model ID:** `grok-imagine-video-1.5-preview`  
**Alias:** `grok-imagine-video-1.5-2026-05-30`  
**Base endpoint:** `https://api.x.ai/v1`  
**Available regions:** `us-east-1`, `eu-west-1`  
**Rate limit:** 60 requests per minute

### Resolution and Duration

| Resolution | Price per second | Notes |
|---|---|---|
| 480p | $0.08 / second | Good for drafts, internal review |
| 720p | $0.14 / second | Maximum resolution available |
| Image input | $0.01 flat | Applied per request |
| Audio | Included | No additional charge |

**Clip length:** 1–15 seconds. A 10-second 720p clip costs $1.40 + $0.01 = $1.41. Audio is free.

### Code Example (Python SDK)

```python
import os
import xai_sdk

client = xai_sdk.Client(api_key=os.getenv("XAI_API_KEY"))

response = client.video.generate(
    prompt="Slow cinematic push-in as embers drift across the scene and fabric stirs in the wind",
    model="grok-imagine-video-1.5-preview",
    image_url="https://your-host.com/source-frame.jpg",
    duration=10,
    resolution="720p",
)

print(response.url)
```

The model accepts `aspect_ratio` as an optional parameter. Default follows the source image dimensions.

### Access

Sign up at [console.x.ai](https://console.x.ai) and generate an API key. xAI provides $25 in initial credits. The model is also available on partner inference platforms: fal.ai, Replicate, and Runware all have it live.

---

## Benchmark Reality Check

The #1 claim on the Image-to-Video Arena leaderboard requires a caveat.

Rankings diverge by evaluation category. On the **without-audio** leaderboard at Artificial Analysis, Dreamina Seedance 2.0 720p leads at Elo 1343; Grok Imagine 1.5 Preview sits at Elo 1325 — competitive but not first. In the **with-audio** category, Grok 1.5 ranks #2 at Elo 1110, behind Seedance 2.0 (Elo 1194).

The #1 position on KEAR AI's arena accounts for audio natively, which is where Grok 1.5 has the most distinct advantage: native synchronized audio with no extra cost. That distinction matters a lot for some use cases (product ads, social video) and not at all for others (reference frames, archival conversion, motion graphics input).

---

## Competitive Comparison

### vs. Google Veo 3.1

- **Grok 1.5** is faster and cheaper for draft-quality work and prototyping.
- **Veo 3.1** does true 4K output, has stronger native audio on longer outputs, supports chained clips past 140 seconds, and is Google's production-grade choice for high-fidelity final delivery.
- If you are generating at scale for internal review or social-first content at 720p, Grok 1.5's pricing advantage is real. If you need 4K theatrical output or extended sequences, Veo 3.1 wins.

### vs. Kling / Sora / Seedance 2.0

- Kling, Sora, and Seedance 2.0 all output at 1080p; Grok 1.5 caps at 720p.
- Grok 1.5 is the only model in this group that generates synchronized audio in the same inference pass. The others require a separate audio step, introducing timing drift.
- For audio-critical workflows — product demos with voiceover, social content with ambient sound, short narrative clips — Grok 1.5's single-pass generation matters.
- For silent animation or workflows where you will add audio in post, the 720p cap may make Kling or Seedance 2.0 preferable at parity quality.

### vs. Wan 2.7

- Wan 2.7 is a strong open-weight choice for on-premise or self-hosted workflows. It runs locally.
- Grok 1.5 is API-only. No self-hosting option.
- If your workflow requires on-device generation (latency, privacy, airgapped environments), Wan 2.7 wins by default.

---

## Use Cases Where Grok 1.5 Makes Sense

**Product marketing (e-commerce, DTC brands):** A static product photo + a prompt describing motion → animated video ad with synchronized ambient sound. Single-pass, no audio sync work.

**Social-first short video:** 720p is the delivery target for most platforms anyway. The 10-15 second clip window covers Reels and Shorts.

**Rapid prototyping and storyboarding:** At $0.08/second at 480p, you can generate many draft iterations before committing to a final render.

**Brand creative with motion reference:** Use a reference image (brand style, specific product shot) to anchor the look while the model handles the motion. The model's instruction-following allows for scene restyles, object manipulation, and controlled camera moves.

## Limitations to Know Before Integrating

- **No text-to-video in preview.** You must supply an input image.
- **720p maximum.** If your delivery target is 1080p or above, you will need a separate upscaling step or a different model.
- **Preview instability.** This is a preview release. The model ID includes a date stamp (`grok-imagine-video-1.5-2026-05-30`) — pin to it if you want stability. xAI's preview models have historically shipped updates that change output behavior.
- **API-only.** No consumer UI access yet. You are calling the API directly or through a partner platform.

---

## Bottom Line

Grok Imagine Video 1.5 is a credible API choice for image-to-video workflows where native audio matters and 720p is acceptable. The pricing is straightforward, the API is live, and the SDK integration is three lines of Python.

The 720p ceiling and image-only input (no text-to-video yet) are real constraints. But for the use cases where those constraints do not apply — social content, product animation, rapid prototyping — the single-pass native audio and competitive per-second pricing make it worth evaluating now rather than waiting for the consumer product launch.

---

*This article is based on publicly available API documentation, benchmark data from KEAR AI and Artificial Analysis, and the xAI developer console. ChatForest did not test this model hands-on.*


---
title: "Grok Imagine Video 1.5 Preview: xAI's Image-to-Video API Hits #1 — Builder Guide"
date: 2026-06-09
slug: grok-imagine-video-1-5-preview-image-to-video-api-builder-guide
description: "xAI shipped grok-imagine-video-1.5-preview on June 3, 2026 — API-first, before any consumer rollout. It claims the top spot on image-to-video leaderboards with native audio included. Here is what builders actually get."
tags: ["xAI", "Grok", "video generation", "image-to-video", "API", "multimodal", "audio", "builder-guide", "developer tools"]
sources_audited: 2026-07-29
---

On June 3, 2026, xAI pushed `grok-imagine-video-1.5-preview` to the public API — before it appeared in the consumer Grok product ([xAI's own launch post](https://x.ai/news/grok-imagine-video-1-5); [reporting confirming the API-first sequencing](https://www.digitaltoday.co.kr/en/view/67872/xai-releases-grok-imagine-video-1-5-ai-video-maker)). xAI shipped it with firm per-second pricing, a documented rate limit, and named region availability from day one ([xAI Imagine API docs](https://x.ai/api/imagine)).

The model has claimed the top spot on the [Image-to-Video Arena leaderboard](https://kearai.com/leaderboard/image-to-video) run by KEAR AI, which reported a +52 Elo jump over Grok Imagine 1.0 and wins over ByteDance's Seedance 2.0, Alibaba's [HappyHorse 1.0](https://channelx.world/2026/04/alibaba-happyhorse-ai-video-generation-and-editing/), and Google Veo in blind head-to-head testing ([independent write-up of the Elo delta](https://omniart.studio/blog/models-insights/grok-imagine-1-5-vs-1-0); [independent reporting corroborating the #1 leaderboard claim](https://www.techtimes.com/articles/318635/20260618/grok-imagine-video-15-goes-live-xai-tops-ai-video-leaderboard-86-percent-below-sora.htm)). Leaderboard standings like this are live and shift as new models are added and votes accrue — see the Benchmark Reality Check section below for where things stood at last check (2026-07-29).

This guide covers what is technically new, the API details you need to integrate it, an honest look at the benchmark caveats, and how it compares against Veo 3.1, Kling, and Seedance 2.0.

---

## What Is Grok Imagine Video 1.5?

`grok-imagine-video-1.5-preview` is an **image-to-video model** ([xAI launch post](https://x.ai/news/grok-imagine-video-1-5)). You give it a static image and a text prompt describing the motion you want, and it animates the scene — camera moves, atmosphere, lighting continuity, and physics — into a short video clip.

In this preview release it is image-to-video only — you must supply an input image, unlike the general-availability `grok-imagine-video-1.5` that followed on June 16, 2026, which added text-to-video and reference-to-video modes ([xAI Imagine API docs](https://x.ai/api/imagine)). That is a meaningful constraint for some workflows and irrelevant for others.

The standout technical addition over 1.0 is **native audio**: the model generates synchronized sound — dialogue, sound effects, ambient audio, music — in the same inference pass as the video, rather than a separate post-processing step ([xAI Imagine API docs](https://x.ai/api/imagine); [independent technical writeup confirming single-pass audio](https://wavespeed.ai/blog/posts/grok-imagine-video-1-5-image-to-video-api/)).

---

## API Specs

**Model ID:** `grok-imagine-video-1.5-preview`  
**Dated alias:** `grok-imagine-video-1.5-2026-05-30` ([xAI model docs](https://docs.x.ai/developers/models/grok-imagine-video-1.5-preview))  
**Base endpoint:** `https://api.x.ai/v1` ([xAI quickstart docs](https://docs.x.ai/developers/quickstart))  
**Available regions:** `us-east-1`, `us-west-2` ([xAI model docs](https://docs.x.ai/developers/models/grok-imagine-video-1.5-preview))  
**Rate limit:** 10 requests per second ([xAI rate limits docs](https://docs.x.ai/developers/rate-limits))

### Resolution and Duration

| Resolution | Price per second | Notes |
|---|---|---|
| 480p | $0.08 / second | Good for drafts, internal review |
| 720p | $0.14 / second | Maximum resolution available |
| Image input | $0.01 flat | Applied per request |
| Audio | Included | No additional charge |

**Clip length:** 1–15 seconds ([xAI Imagine API docs](https://x.ai/api/imagine)). A 10-second 720p clip costs $1.40 + $0.01 = $1.41. Audio is included at no additional charge ([fal.ai pricing page mirroring xAI's per-second rate](https://fal.ai/models/xai/grok-imagine-video/v1.5/image-to-video)).

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

*(Parameters shown — `image_url`, `duration`, `resolution`, `model` — match [xAI's official video generation docs](https://docs.x.ai/developers/model-capabilities/video/generation); verify current signature against the docs before shipping, since preview SDKs change.)*

The model accepts `aspect_ratio` as an optional parameter ([xAI docs](https://docs.x.ai/developers/model-capabilities/imagine)). Default follows the source image dimensions.

### Access

Sign up at [console.x.ai](https://console.x.ai) and generate an API key; new accounts receive free sign-up credits with no card required ([reporting on xAI's console credit offer](https://www.getaiperks.com/en/ai/free-xai-grok-api-credits)). The model is also available on partner inference platforms: [fal.ai](https://fal.ai/models/xai/grok-imagine-video/v1.5/image-to-video), [Replicate](https://replicate.com/xai/grok-imagine-video-1.5), and [Runware](https://runware.ai/docs/models/xai-grok-imagine-video) all have it live.

---

## Benchmark Reality Check

The #1 claim on the Image-to-Video Arena leaderboard requires a caveat: rankings diverge by leaderboard and by evaluation category, and both move constantly as new models are added and more blind votes accrue.

As of this audit (2026-07-29), on the [Artificial Analysis image-to-video leaderboard](https://artificialanalysis.ai/video/leaderboard/image-to-video), Grok Imagine Video 1.5 Preview is **not** in first place in either category: on the **with-audio** board it trails both Dreamina Seedance 2.0 720p and Gemini Omni Flash (roughly Elo 1200 / 1195 / 1115 in that order); on the **without-audio** board it trails Gemini Omni Flash and Seedance 2.0 (roughly Elo 1370 / 1345 / 1330). These exact figures will already be stale by the time you read this — check the live leaderboard rather than trusting a snapshot.

xAI's own #1 claim points specifically to KEAR AI's arena, a different leaderboard that (per its own listing) ranked Grok Imagine 1.5 first overall at the time of its launch, ahead of Seedance 2.0, HappyHorse 1.0, and Veo. The lesson for builders: "#1" claims for video models are leaderboard-specific and time-sensitive. Native synchronized audio at no extra cost is a real, verifiable differentiator regardless of where Grok 1.5 sits on any given day's leaderboard — that distinction matters a lot for some use cases (product ads, social video) and not at all for others (reference frames, archival conversion, motion graphics input).

---

## Competitive Comparison

### vs. Google Veo 3.1

- **Grok 1.5** is cheaper per second for draft-quality work and prototyping at 480p/720p.
- **Veo 3.1** natively generates 4K output and synchronized audio, and supports an "Extend your scene" workflow that chains clips into longer sequences ([Google DeepMind's Veo model page](https://deepmind.google/models/veo/)). Google positions it as the production-grade choice for high-fidelity final delivery.
- If you are generating at scale for internal review or social-first content at 720p, Grok 1.5's pricing advantage is real. If you need 4K output or long extended sequences, Veo 3.1 wins.

### vs. Kling / Sora / Seedance 2.0

- Resolution is not a clean line in Grok 1.5's favor the way it might look at first glance: Kling 3.0 outputs native 4K at 60fps ([reporting on Kuaishou's Kling 3.0 launch](https://bestphoto.ai/blog/kling-3-0-now-available)), Seedance 2.0 added native 4K output as of a June 23, 2026 update ([reporting on ByteDance's Volcano Engine FORCE Conference announcement](https://www.techtimes.com/articles/318975/20260624/bytedance-seedance-25-native-30-second-ai-video-no-stitching-required.htm)), and Sora 2 tops out at 1080p via the `sora-2-pro` variant ([OpenAI's video generation guide](https://developers.openai.com/api/docs/guides/video-generation)). Grok 1.5 caps at 720p.
- Grok 1.5 is the only model in this group that generates synchronized audio in the same inference pass; the others require a separate audio step.
- For audio-critical workflows — product demos with voiceover, social content with ambient sound, short narrative clips — Grok 1.5's single-pass generation matters.
- For silent animation or workflows where resolution above 720p matters more than native audio, Kling 3.0 or Seedance 2.0 are the stronger picks.

### vs. Wan 2.7

- Wan 2.7 is an open-weight model that can be downloaded and run locally (e.g. via ComfyUI), with weights distributed through Alibaba's ModelScope hub ([technical guide to Wan 2.7's open-weight distribution](https://wan27.org/blog/wan-2-7-open-source-guide)). It is a 14B-parameter model with a practical minimum of roughly 24GB VRAM for a usable workflow.
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

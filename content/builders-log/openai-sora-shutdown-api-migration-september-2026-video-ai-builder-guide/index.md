---
title: "OpenAI Killed Sora. Your API Deadline Is September 24. Here's What to Build With Instead."
date: 2026-04-26
description: "OpenAI shut down Sora apps on April 26, 2026 and will kill the Videos API on September 24. Sora-2, sora-2-pro, and all Videos API endpoints stop working that day. Here's what happened, why the unit economics made it inevitable, and which video AI API to use now."
content_type: "Builder's Log"
categories: ["OpenAI", "AI Video", "Model Migration", "APIs"]
tags: ["openai", "sora", "video-ai", "model-deprecation", "runway", "veo", "kling", "api-migration", "video-generation", "unit-economics"]
---

OpenAI shut down Sora apps on April 26, 2026. The Sora API — `sora-2`, `sora-2-pro`, and the Videos API — stops accepting requests on **September 24, 2026**. All user data will be permanently deleted.

If you have production code calling Sora endpoints, you have until September 24 to migrate. That is approximately 15 weeks from today.

This is not a typical model deprecation where the successor is obvious and the migration is a string swap. OpenAI announced no drop-in replacement for Sora. You need to evaluate alternatives and migrate before the deadline.

---

## What Happened

Sora launched publicly in December 2024 as OpenAI's flagship video generation model. It generated significant interest and was used for a wide range of applications, from short-form social content to commercial video production.

OpenAI announced the discontinuation on March 24, 2026. The apps (sora.com, iOS, Android) shut down on April 26. The API stays live until September 24, giving builders a 6-month runway to migrate.

The reasoning OpenAI gave publicly was limited. But industry analysis points to unit economics:

**Estimated cost vs. revenue:**
- Inference cost: approximately $1.30 per 10-second clip at scale (widely cited estimate from secondary sources — OpenAI has not confirmed exact figures)
- A single $20/month Pro subscriber generating 50 clips per month would cost OpenAI roughly $65 in compute alone
- Lifetime API and consumer revenue did not come close to covering inference costs

Video generation at quality is orders of magnitude more compute-intensive than text. A frontier text response might cost a fraction of a cent. A 10-second video clip costs dollars. At the pricing OpenAI offered (and needed to match competitors on), the gap was structural, not temporary.

This is a pattern worth internalizing: compute costs for video generation are fundamentally different from text. Any builder evaluating video AI should model the unit economics carefully before building a product where video is the primary output.

---

## Disney's $1 Billion Deal Collapsed

The financial scale of the Sora shutdown was large enough to unwind a major enterprise deal. Disney had committed to a $1 billion partnership and three-year character licensing arrangement built around Sora's capabilities. That deal collapsed when Sora shut down.

The lesson for enterprise builders: when your product is built on a single AI provider's specific model, and that model discontinues, there is no easy fallback. Diversification or abstraction layers are not just engineering preferences — they are business continuity decisions.

---

## The API Migration Deadline

**September 24, 2026** — all of the following stop working:

- `sora-2` model
- `sora-2-pro` model
- The Videos API (`POST /v1/videos/generations`)
- All Sora API endpoints

OpenAI has not announced a migration path to another OpenAI product. There is no `gpt-video` or successor model. The migration is to a different provider.

---

## What Sora Was Doing

Before evaluating replacements, it helps to know which Sora capabilities you are actually using. Sora's core capabilities were:

- **Text-to-video:** Generate a video clip from a text prompt
- **Image-to-video:** Animate a static image
- **Video extension:** Extend an existing clip forward or backward in time
- **Consistency controls:** Maintain character or scene consistency across clips

Not all alternatives support all of these features equally. If your use case depends specifically on video extension or a particular consistency approach, verify support in the alternative before committing to a migration path.

---

## The Replacement Landscape

Four providers have emerged as the leading video AI APIs for builders in 2026. Each has different strengths:

### Runway Gen-4 Turbo

**Best for:** Marketers, commercial video production, character consistency

Runway's Gen-4 Turbo is the most mature video AI API from an enterprise reliability standpoint. It offers reference image controls (providing a reference image to anchor character or style consistency across clips), solid text-to-video and image-to-video support, and a stable developer API.

The Runway API uses a simple generation request pattern:

```python
import requests

response = requests.post(
    "https://api.runwayml.com/v1/image_to_video",
    headers={"Authorization": f"Bearer {RUNWAY_API_KEY}"},
    json={
        "model": "gen4_turbo",
        "promptImage": "https://example.com/reference.jpg",
        "promptText": "The character walks through a sunlit forest",
        "duration": 10,
        "ratio": "1280:768"
    }
)
task_id = response.json()["id"]
```

Runway bills on credits, not per-minute. Check the Runway Developer Dashboard for current credit pricing.

### Google Veo 3.1

**Best for:** Builders already in the Google ecosystem, native audio generation

Veo 3.1 is Google's current video generation model and is available through the Gemini API and Google AI Studio. Its distinguishing feature for builders is native audio generation — Veo 3.1 can produce clips with synchronized ambient sound and dialogue without requiring a separate audio model or post-processing step.

Veo 3.1 is also available as Veo 3.1 Lite, which prices at under 50% of Veo 3.1 Fast. For high-volume generation where quality is sufficient at the Lite tier, this is a significant cost lever.

```python
import google.generativeai as genai

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("veo-3.1")

operation = model.generate_video(
    prompt="A city street at dawn, people arriving for the morning commute",
    duration_seconds=8,
    aspect_ratio="16:9"
)
```

Veo 3.1 requires Gemini API access. Check the Google AI Studio pricing page for current rates.

### Kling 3.0 Omni

**Best for:** Audio-dialogue generation, multi-language lip-sync

Kling 3.0 Omni from Kuaishou is notable for its native audio generation capabilities: background sound, dialogue, and automatic lip-sync in five languages. If your application needs video content with spoken language that must be synchronized to on-screen characters, Kling 3.0 leads on this capability.

Kling is available through their API directly and through aggregation platforms like fal.ai.

### Seedance 2.0

**Best for:** Competitive alternative with synchronized audio

Seedance 2.0 is a strong competitor in the audio-synchronized video space, comparable to Kling on audio features. It is worth evaluating alongside Kling if audio generation is a requirement.

---

## The Aggregator Path: fal.ai

If you want to avoid provider lock-in this time, fal.ai provides unified API access to Veo 3.1, Kling 3.0, Seedance 2.0, Wan 2.7, and 600+ other AI models through a single API key and consistent request format.

The advantage: when a specific video model is deprecated or a new model is released, you change a model name in your request rather than migrating your entire integration.

```python
import fal_client

result = fal_client.run(
    "fal-ai/kling-video/v1.6/standard/text-to-video",
    arguments={
        "prompt": "Your video prompt here",
        "duration": "10",
        "aspect_ratio": "16:9"
    }
)
```

Swap `kling-video` for `veo/video-generation` or `seedance/v2/text-to-video` to change providers. The abstraction is not perfect (different models have different parameter sets and capabilities), but for common generation tasks the interface is largely consistent.

---

## Open-Source Options

If you need to run video generation locally or want to avoid cloud inference costs entirely:

- **Wan 2.7** (April 2026) — the current leading open-weight video model for local inference
- **LTX-2.3** (March 2026) — competitive alternative, different architecture

Both require significant GPU resources. Wan 2.7 generation on an H100 takes several minutes per 10-second clip, making it viable for batch processing but not real-time or low-latency applications.

---

## Choosing Your Path

| Use case | Recommended path |
|---|---|
| Commercial video production / brand content | Runway Gen-4 Turbo |
| Audio + video in one generation | Veo 3.1 or Kling 3.0 Omni |
| Multi-language lip-sync | Kling 3.0 Omni |
| High volume, cost-sensitive | Veo 3.1 Lite |
| Avoid future lock-in | fal.ai aggregator |
| Local / private inference | Wan 2.7 |
| Google Cloud ecosystem | Veo 3.1 via Gemini API |

---

## Migration Checklist

**Before September 24, 2026:**

- [ ] Audit your codebase for any calls to `/v1/videos/generations` or `sora-2` / `sora-2-pro` model strings
- [ ] Identify which Sora capabilities you are using: text-to-video, image-to-video, video extension, consistency controls
- [ ] Evaluate 2–3 alternatives against your actual use case (generate test clips with your real prompts)
- [ ] Choose a migration target and get API access provisioned
- [ ] Update your integration and run production validation before the deadline
- [ ] Export any Sora-generated assets you want to retain — all data will be permanently deleted after September 24

**If you built a product on Sora:**

- [ ] Evaluate whether a single-provider video API is still the right architecture, or whether an aggregation layer reduces future shutdown risk
- [ ] Review your unit economics: at the cost per clip of your new provider, does your pricing model still work?
- [ ] Notify users or customers of any changes to video generation quality or capabilities

---

## Bottom Line

Sora's shutdown illustrates the structural risk of building on a video AI product where inference costs significantly exceed sustainable pricing. The compute math for high-quality video generation is genuinely difficult, and OpenAI chose to exit rather than continue subsidizing the gap.

Your September 24 deadline is real. Runway, Veo 3.1, and Kling 3.0 Omni are all production-ready alternatives with stable APIs. The migration is not a model string swap — you need to re-integrate against a new API surface — but none of the replacements require significant architectural changes to a video generation pipeline.

Start with a test evaluation of your actual prompts against your top two candidates. Pick based on output quality for your specific use case, not benchmarks. Then migrate before the deadline.

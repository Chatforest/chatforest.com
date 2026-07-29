# Veo 3.1 + Nano Banana 2: Google's AI Creative Stack for Builders

> Veo 3.1 generates 4–8 second videos with native audio. Nano Banana 2 (gemini-3.1-flash-image) handles image generation and keyframes. Here is the full builder guide: model IDs, API structure, pricing, variant tradeoffs, and the image-to-video pipeline.


[Veo 3.1](https://deepmind.google/models/veo/) is Google's current video generation model in the [Gemini API](https://ai.google.dev/gemini-api/docs/veo). Nano Banana 2 is Google's name for [`gemini-3.1-flash-image`](https://deepmind.google/models/gemini-image/flash/), the Flash-tier counterpart to [Gemini 3 Pro Image](https://deepmind.google/models/gemini-image/pro/) ("Nano Banana Pro"), documented at [ai.google.dev](https://ai.google.dev/gemini-api/docs/image-generation). The two connect: generate a keyframe image with Nano Banana 2, feed it as the start frame to Veo 3.1, and the video inherits the visual composition you designed.

This guide covers both models, the API structure, the three Veo 3.1 tiers, the cost math, and what builders should actually care about.

---

## What Nano Banana 2 Is

**Model ID:** `gemini-3.1-flash-image`

Nano Banana 2 is the Flash-tier counterpart to Gemini 3 Pro Image. It handles image generation and conversational image editing — you can ask it to generate an image, then describe changes and it edits in place, maintaining context.

The key improvements over the original Nano Banana:

- **Text rendering.** Previous Gemini image models struggled with legible in-image text. Google's own [Nano Banana 2 page](https://deepmind.google/models/gemini-image/flash/) highlights precise text generation with font and style control. This matters for product mockups, infographics, and localized social assets.
- **Aspect ratio coverage.** Google [documents ten supported aspect ratios](https://ai.google.dev/gemini-api/docs/image-generation) — 1:1, 3:2, 2:3, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, and the 21:9 ultrawide — useful for banner and cinematic formats without post-generation cropping.
- **512px rapid tier.** Google's docs [list 512px (0.5K) as the smallest output resolution](https://ai.google.dev/gemini-api/docs/image-generation), alongside 1K, 2K, and 4K — minimal latency, designed for rapid iteration loops where you are validating a composition before committing to a full-size render.
- **Multilingual text.** [Google describes localization support](https://deepmind.google/models/gemini-image/flash/) — translating and adapting in-image text to different languages and cultural contexts.

Nano Banana 2 is accessible via the standard `google-genai` Python SDK with the same pattern as other Gemini models.

```python
from google import genai
from google.genai import types

client = genai.Client(api_key="YOUR_API_KEY")

response = client.models.generate_images(
    model="gemini-3.1-flash-image",
    prompt="a neon-lit ramen shop at night, rainwet street, 16:9 cinematic",
    config=types.GenerateImagesConfig(
        number_of_images=1,
        aspect_ratio="16:9",
    ),
)

# response.generated_images[0].image.image_bytes is the raw PNG
```

For downstream use with Veo 3.1, save the image bytes and pass them as the start frame.

---

## What Veo 3.1 Is

Veo 3.1 generates [4-, 6-, or 8-second video clips with synchronized native audio](https://deepmind.google/models/veo/). "Native audio" means the audio — dialogue, sound effects, and ambient audio — is generated in the same pass as the video, not added as a separate post-processing step.

**Model IDs:**

| Tier | Model ID | Target Use |
|---|---|---|
| Lite | [`veo-3.1-lite-generate-preview`](https://ai.google.dev/gemini-api/docs/models/veo-3.1-lite-generate-preview) | Rapid iteration, high-volume, tight budgets |
| Fast | `veo-3.1-fast-generate-preview` | Balanced throughput and quality |
| Quality | [`veo-3.1-generate-preview`](https://ai.google.dev/gemini-api/docs/models/veo-3.1-generate-preview) | Production assets, cinematic output |

Model IDs verified against Google's own Gemini API model docs (linked above); the Fast tier ID is confirmed via the [Veo 3.1 launch post](https://developers.googleblog.com/introducing-veo-3-1-and-new-creative-capabilities-in-the-gemini-api/) on the Google Developers Blog.

All three tiers support the same clip durations (4s, 6s, 8s) and aspect ratios (16:9, 9:16). Resolution differs: per [Google's pricing documentation](https://ai.google.dev/gemini-api/docs/pricing), Lite supports 720p and 1080p but not 4K (and does not support scene extension); Fast and Quality support 720p, 1080p, and 4K.

---

## The API Pattern

Veo 3.1 is asynchronous. You POST a generation request and receive an operation handle, then poll until the video is ready. The SDK handles the polling loop.

**Text-to-video (Quality tier, 8 seconds):**

```python
import time
from google import genai
from google.genai import types

client = genai.Client(api_key="YOUR_API_KEY")

operation = client.models.generate_videos(
    model="veo-3.1-generate-preview",
    prompt="a slow-motion shot of coffee being poured into an espresso glass, steam rising, golden hour light, close-up",
    config=types.GenerateVideosConfig(
        duration_seconds=8,
        aspect_ratio="16:9",
        resolution="1080p",
        generate_audio=True,
    ),
)

# Poll until complete
while not operation.done:
    time.sleep(5)
    operation = client.operations.get(operation)

video_bytes = operation.response.generated_videos[0].video.video_bytes
with open("output.mp4", "wb") as f:
    f.write(video_bytes)
```

**Image-to-video (start frame from Nano Banana 2):**

```python
import base64, time
from google import genai
from google.genai import types

client = genai.Client(api_key="YOUR_API_KEY")

# Step 1: Generate keyframe with Nano Banana 2
img_response = client.models.generate_images(
    model="gemini-3.1-flash-image",
    prompt="an abandoned greenhouse, overgrown with vines, shafts of dusty light, cinematic",
    config=types.GenerateImagesConfig(
        number_of_images=1,
        aspect_ratio="16:9",
    ),
)
image_bytes = img_response.generated_images[0].image.image_bytes

# Step 2: Feed as start frame to Veo 3.1
operation = client.models.generate_videos(
    model="veo-3.1-generate-preview",
    prompt="leaves rustle, light shifts slowly, dust motes drift through the shafts of light",
    config=types.GenerateVideosConfig(
        duration_seconds=6,
        aspect_ratio="16:9",
        resolution="1080p",
        start_image=types.Image(image_bytes=image_bytes),
        generate_audio=True,
    ),
)

while not operation.done:
    time.sleep(5)
    operation = client.operations.get(operation)

video_bytes = operation.response.generated_videos[0].video.video_bytes
```

**Reference images for character consistency:**

Veo 3.1 [accepts up to 3 reference images](https://developers.googleblog.com/introducing-veo-3-1-and-new-creative-capabilities-in-the-gemini-api/) to anchor the visual appearance of a subject — a person, product, or character — across the generated clip.

```python
operation = client.models.generate_videos(
    model="veo-3.1-generate-preview",
    prompt="the product rotates slowly on a white surface, catching light",
    config=types.GenerateVideosConfig(
        duration_seconds=6,
        aspect_ratio="1:1",
        resolution="1080p",
        reference_images=[
            types.Image(image_bytes=product_front_bytes),
            types.Image(image_bytes=product_side_bytes),
        ],
        generate_audio=False,  # silence for product shots
    ),
)
```

---

## Scene Extension

Single Veo 3.1 clips max at 8 seconds. For longer sequences, use [scene extension](https://ai.google.dev/gemini-api/docs/veo): POST a second generation with the last second of the previous clip as the start frame. (Note: the Lite tier does not support this feature — see the resolution note above.)

```python
# Extend an existing clip by feeding its final frame as start_image
# Extract final frame externally (via ffmpeg) then pass it as start_image
operation_2 = client.models.generate_videos(
    model="veo-3.1-generate-preview",
    prompt="the camera slowly pulls back, revealing the full room",
    config=types.GenerateVideosConfig(
        duration_seconds=6,
        start_image=types.Image(image_bytes=final_frame_bytes),
        generate_audio=True,
    ),
)
```

This maintains visual continuity and lets you construct multi-minute sequences without a single generation covering the full duration.

---

## Pricing

| Tier | 720p | 1080p | 4K |
|---|---|---|---|
| Lite | $0.05/sec | $0.08/sec | Not supported |
| Fast | $0.10/sec | $0.12/sec | $0.30/sec |
| Quality | $0.40/sec | $0.40/sec | $0.60/sec |

These are [Gemini API rates per Google's official pricing page](https://ai.google.dev/gemini-api/docs/pricing), current as of this writing, and they include audio by default — Google does not publish a separate, cheaper rate for silent video generation. There is no free tier for either Veo 3.1 or Nano Banana 2 generation via the API; both require a paid account (Google AI Studio's free quota covers text/chat models, not video or image generation).

**Cost math on a real workload:**

An 8-second clip at Quality tier (1080p, audio included): **$3.20**. A product demo pipeline generating five 4-second variants per product at Fast tier (1080p, $0.12/sec): 5 × ($0.12 × 4) = **$2.40 per product**. A social automation tool generating 100 four-second portrait clips/day at Lite tier (720p, $0.05/sec): 100 × ($0.05 × 4) = **$20/day**.

**Nano Banana 2 pricing** on the [Gemini API](https://ai.google.dev/gemini-api/docs/pricing) is token-based ($60 per million output image tokens), working out to $0.045 per image at 512px (0.5K) and $0.067 per image at 1024px (1K). Relative to the cost of Veo 3.1 clips, image generation is noise in the budget.

---

## Choosing the Right Veo 3.1 Tier

**Use Lite when:**
- Rapid iteration or A/B testing prompts (many generations, discard most)
- High-volume pipelines where quality is acceptable at 720p
- Serving a product that generates clips for non-critical uses (thumbnails, previews)
- Budget is constrained and $0.05–0.08/sec is what you can work with

**Use Fast when:**
- You need 1080p but have volume requirements that make Quality tier expensive
- Background processing jobs where latency is less critical than throughput

**Use Quality when:**
- Production assets that will be published
- Cinematic sequences where realism, motion quality, and audio fidelity matter
- Client-facing demos or content where the output quality is the product

**Use Quality 4K when:**
- Professional video production, broadcast, or premium commercial use
- You need to crop, zoom, or reframe post-generation without losing resolution

---

## Limits and What to Know

**Authentication:** All Veo 3.1 calls require a paid Gemini API or Vertex AI account. [The free tier does not include video or image generation](https://ai.google.dev/gemini-api/docs/pricing).

**Rate limits:** Veo 3.1 generation is slower than text inference — expect anywhere from tens of seconds to a few minutes for an 8-second clip, depending on tier and server load. Plan for async queuing in production systems.

**No looping.** Generated clips do not loop seamlessly unless you specifically design the prompt and end frame to match the start. Looping requires external post-processing.

**Audio quality variability.** Native audio generation is good but not uniform. [Google itself notes that natural, consistent spoken dialogue — particularly in short segments — remains an area of active development](https://deepmind.google/models/veo/). Complex audio scenes (layered sound effects + music + dialogue) occasionally produce artifacts. Test prompts that isolate audio elements before combining them.

**Imagen deprecation.** Google is retiring its Imagen 4 models (`imagen-4.0-generate-001`, `imagen-4.0-ultra-generate-001`, `imagen-4.0-fast-generate-001`) on [August 17, 2026](https://ai.google.dev/gemini-api/docs/deprecations), with Nano Banana 2 (`gemini-3.1-flash-image`) as the recommended migration target. Check the [Gemini API deprecations page](https://ai.google.dev/gemini-api/docs/deprecations) for your specific model ID and cutoff date — the API shape differs from Imagen's, so budget time to update your SDK calls.

**Content policy.** Veo 3.1 enforces [Google's Generative AI Prohibited Use Policy](https://policies.google.com/terms/generative-ai/use-policy) and [Gemini API usage/safety policies](https://ai.google.dev/gemini-api/docs/usage-policies). Requests that depict real people, specific trademarks, or certain categories of content will be refused or filtered, and generated output carries an invisible SynthID watermark.

---

## The Builder Decision

If you are building a pipeline that requires video output with audio, Veo 3.1 is the most direct path to that today in the Gemini ecosystem. The native audio generation removes a whole post-production step for many content use cases.

The Nano Banana 2 + Veo 3.1 chain is useful specifically when you need compositional control over the first frame — for product shots, character consistency, or when a text-to-video prompt does not reliably produce the framing you want. Generate the frame first, then animate it.

The scene extension pattern is the path to longer sequences. It requires managing state between generations (saving the final frame of each clip), but there is no fundamental limit to total sequence length.

If audio is not required and you primarily need visual motion at scale, evaluate whether the Lite tier meets your quality threshold — at $0.05/sec it is the most cost-efficient path to 720p clips in the Google stack.


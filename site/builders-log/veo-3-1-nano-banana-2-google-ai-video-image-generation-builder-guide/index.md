# Veo 3.1 + Nano Banana 2: Google's AI Creative Stack for Builders

> Veo 3.1 generates 4–8 second videos with native audio. Nano Banana 2 (gemini-3.1-flash-image) handles image generation and keyframes. Here is the full builder guide: model IDs, API structure, pricing, variant tradeoffs, and the image-to-video pipeline.


Veo 3.1 is Google's current video generation model in the Gemini API. Nano Banana 2 is Google's name for `gemini-3.1-flash-image`, the high-efficiency image generation model in the same stack. The two connect: generate a keyframe image with Nano Banana 2, feed it as the start frame to Veo 3.1, and the video inherits the visual composition you designed.

This guide covers both models, the API structure, the three Veo 3.1 tiers, the cost math, and what builders should actually care about.

---

## What Nano Banana 2 Is

**Model ID:** `gemini-3.1-flash-image`

Nano Banana 2 is the Flash-tier counterpart to Gemini 3 Pro Image. It handles image generation and conversational image editing — you can ask it to generate an image, then describe changes and it edits in place, maintaining context.

The key improvements over the original Nano Banana:

- **Text rendering.** Previous Gemini image models struggled with legible in-image text. Nano Banana 2 renders it reliably, including non-Latin scripts. This matters for product mockups, infographics, and localized social assets.
- **Extended aspect ratios.** Standard ratios plus 4:1, 1:4, 8:1, and 1:8 — useful for banner formats without post-generation cropping.
- **512px rapid tier.** Smallest resolution output with minimal latency, designed for rapid iteration loops where you are validating a composition before committing to a full-size render.
- **Multilingual text.** Native support for generating or translating text strings directly within an image in multiple languages.

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

Veo 3.1 generates 4-, 6-, or 8-second video clips at 24 FPS with synchronized native audio. "Native audio" means the audio is generated in the same pass as the video — dialogue, sound effects, and ambient audio — not added as a separate step. This is the primary differentiator from most competing video generation tools, which treat audio as a post-processing step.

**Model IDs:**

| Tier | Model ID | Target Use |
|---|---|---|
| Lite | `veo-3.1-lite-generate-preview` | Rapid iteration, high-volume, tight budgets |
| Fast | `veo-3.1-fast-generate-preview` | Balanced throughput and quality |
| Quality | `veo-3.1-generate-preview` | Production assets, cinematic output |

All three tiers support the same clip durations (4s, 6s, 8s), aspect ratios (16:9, 9:16), and image-to-video input. Resolution range differs: Lite tops at 720p; Fast and Quality support 720p, 1080p, and 4K (4K is in preview).

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

Veo 3.1 accepts up to 3 reference images to anchor the visual appearance of a subject — a person, product, or character — across the generated clip.

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

Single Veo 3.1 clips max at 8 seconds. For longer sequences, use scene extension: POST a second generation with the last second of the previous clip as the start frame.

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

| Tier | Resolution | With Audio | Without Audio |
|---|---|---|---|
| Lite | 720p | ~$0.15/sec | ~$0.08/sec |
| Fast | 720p–1080p | ~$0.25/sec | ~$0.13/sec |
| Quality | 720p–1080p | ~$0.40/sec | ~$0.20/sec |
| Quality 4K | 4K (preview) | ~$0.60/sec | ~$0.40/sec |

These are Vertex AI rates as of June 2026. Google AI Studio has a free quota for prototyping; paid Vertex AI plans have higher rate limits.

**Cost math on a real workload:**

An 8-second clip at Quality tier with audio: **$3.20**. A product demo pipeline generating 5 variants per product at Fast tier: $1.00 per product. A social media automation tool generating 100 portrait clips/day at Lite tier: **$12/day**.

By comparison, Sora's API charges per-second at similar rates but does not generate native audio — adding a separate text-to-audio step (e.g., ElevenLabs SFX) adds $0.01–$0.05/second, plus latency. For content where sound matters, Veo 3.1's single-pass audio can be the cheaper option end-to-end.

**Nano Banana 2 pricing** on Vertex AI is approximately $0.04 per generated image at standard resolution. Relative to the cost of Veo 3.1 clips, image generation is noise in the budget.

---

## Choosing the Right Veo 3.1 Tier

**Use Lite when:**
- Rapid iteration or A/B testing prompts (many generations, discard most)
- High-volume pipelines where quality is acceptable at 720p
- Serving a product that generates clips for non-critical uses (thumbnails, previews)
- Budget is constrained and $0.15/sec is what you can work with

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

**Authentication:** All Veo 3.1 calls require a paid Gemini API or Vertex AI account. The free tier does not include video generation.

**Rate limits:** Veo 3.1 generation is slower than text inference — typically 30–90 seconds to generate an 8-second clip depending on server load. Plan for async queuing in production systems.

**No looping.** Generated clips do not loop seamlessly unless you specifically design the prompt and end frame to match the start. Looping requires external post-processing.

**Audio quality variability.** Native audio generation is good but not uniform. Complex audio scenes (layered sound effects + music + dialogue) occasionally produce artifacts. Test prompts that isolate audio elements before combining them.

**Imagen deprecation.** If you currently use Imagen 3.0 (capability-001), that model retires June 30, 2026. The migration path is Nano Banana 2 (`gemini-3.1-flash-image`) for image generation. The API shape differs — update your SDK calls before the cutoff.

**Content policy.** Veo 3.1 enforces Google's generative media content policy. Requests that depict real people, specific trademarks, or certain categories of content will be refused or watermarked.

---

## The Builder Decision

If you are building a pipeline that requires video output with audio, Veo 3.1 is the most direct path to that today in the Gemini ecosystem. The native audio generation removes a whole post-production step for many content use cases.

The Nano Banana 2 + Veo 3.1 chain is useful specifically when you need compositional control over the first frame — for product shots, character consistency, or when a text-to-video prompt does not reliably produce the framing you want. Generate the frame first, then animate it.

The scene extension pattern is the path to longer sequences. It requires managing state between generations (saving the final frame of each clip), but there is no fundamental limit to total sequence length.

If audio is not required and you primarily need visual motion at scale, evaluate whether the Lite tier meets your quality threshold — at $0.15/sec it is the most cost-efficient path to 720p clips in the Google stack.


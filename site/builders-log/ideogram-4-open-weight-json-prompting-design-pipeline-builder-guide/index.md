# Ideogram 4: The Open-Weight Image Model With a JSON Interface Builders Actually Need

> Ideogram 4.0 launched June 3, 2026 as a 9.3B-parameter open-weight Diffusion Transformer with a structured JSON prompting interface, bounding-box layout control, and best-in-class in-image text rendering. Weights are free for non-commercial use; commercial pipelines need a license. Here's the complete builder decision guide.


On June 3, 2026, Ideogram [released 4.0](https://ideogram.ai/blog/ideogram-4.0/) — [the company's first open-weight model](https://github.com/ideogram-oss/ideogram4) and, per [DesignArena's leaderboard](https://www.designarena.ai/leaderboard), the top-ranked open-weight image generation model on that benchmark ([1285 Elo, ~114 points ahead of the next open-weight model](https://firethering.com/ideogram-4-open-weight/), [confirmed independently](https://www.buildfastwithai.com/blogs/ideogram-4-open-weight-image-model)). For builders, the headline is not the benchmark ranking. It is the JSON prompting interface: a structured way to describe layouts, palettes, and typography that turns one-off image generation into a templated design pipeline.

**At a glance:** Ideogram 4 is a [9.3 billion-parameter single-stream Diffusion Transformer trained from scratch](https://ideogram.ai/blog/ideogram-4.0/). Weights are available in [nf4 format](https://huggingface.co/ideogram-ai/ideogram-4-nf4) and [fp8 format on Hugging Face](https://huggingface.co/ideogram-ai/ideogram-4-fp8). [Inference code is Apache 2.0](https://github.com/ideogram-oss/ideogram4); [weights are under Ideogram's Non-Commercial Model Agreement](https://ideogram.ai/licensing/) — free for research, evaluation, and local experimentation; commercial production deployment requires a separate paid license. [ComfyUI added native support the same day](https://blog.comfy.org/p/ideogram-4-day-0-support-in-comfyui). The [JSON interface](https://docs.ideogram.ai/using-ideogram/getting-started/prompting-guide/4.-json-prompting-ideogram-4.0) supports per-element text bounding boxes (no fixed cap in the schema), up to sixteen hex color palette slots, and explicit object positioning. Part of our **[Builder's Log](/builders-log/)**.

---

## Why This One Is Different

Ideogram has shipped multiple model generations. What changes with 4.0 is the architecture of how you talk to it.

Every prior text-to-image model uses flat prompts: you describe an image in prose, the model makes a best-effort interpretation, and the result is not reproducible at scale. Each call is a negotiation between your description and the model's learned priors.

Ideogram 4 is trained on structured JSON captions. You can still use flat prose — but the JSON surface gives builders explicit control over six properties that flat prompts leave to chance:

1. **Bounding-box placement:** Any element in the image — subjects, text, background regions — can be assigned a bounding box in [normalized coordinates](https://docs.ideogram.ai/using-ideogram/getting-started/prompting-guide/4.-json-prompting-ideogram-4.0) `[y_min, x_min, y_max, x_max]` from 0 to 1000. You specify where the object lives in the frame, and the model respects it.
2. **Color palette:** [Up to 16 hex colors total, up to 5 per element](https://docs.ideogram.ai/using-ideogram/getting-started/prompting-guide/4.-json-prompting-ideogram-4.0), specified as an array. The model constrains the output palette to those values.
3. **Typography control:** You specify text content, placement, and a bounding box per text element; style notes like weight or font family go in the element's free-text description rather than a dedicated field. [Ideogram's own JSON prompting docs don't state a fixed cap on the number of text elements](https://docs.ideogram.ai/using-ideogram/getting-started/prompting-guide/4.-json-prompting-ideogram-4.0), though [hands-on testing suggests keeping dense typographic layouts to a handful of elements](https://omkamal.github.io/articles/ideogram4/ideogram4.html) for reliable placement.
4. **Object positioning:** Objects and subjects can be positioned relative to the frame, not just described.
5. **Style attributes:** Lighting, rendering style, and texture can be specified declaratively.
6. **Multi-element layouts:** Different elements can carry different constraints simultaneously.

The practical implication: a flat prompt gets you a single image. The JSON interface gets you a template. Run it fifty times with the same layout schema and a different subject line, and you get fifty images with the same compositional rules — the kind of consistency that product, marketing, and brand pipelines require.

---

## Model Specifications

| Property | Value |
|----------|-------|
| Parameters | [9.3 billion](https://ideogram.ai/blog/ideogram-4.0/) |
| Architecture | [Single-stream Diffusion Transformer](https://ideogram.ai/blog/ideogram-4.0/) |
| Training | [From scratch (no fine-tune of existing model)](https://ideogram.ai/blog/ideogram-4.0/) |
| Text encoder | [Qwen3-VL-8B-Instruct](https://huggingface.co/ideogram-ai/ideogram-4-nf4), a vision-language model used in text-only mode |
| Native resolution | [2K (any multiple-of-16 from 256 to 2048 per side)](https://ideogram.ai/blog/ideogram-4.0/) |
| Text rendering | [0.97 accuracy on the X-Omni English OCR benchmark for in-image text, per Ideogram's own release notes](https://ideogram.ai/blog/ideogram-4.0/) |
| DesignArena rank | [#1 open-weight, 1285 Elo — a ~114-point lead over the next open-weight model](https://firethering.com/ideogram-4-open-weight/) ([HunyuanImage 3.0 at 1171](https://www.buildfastwithai.com/blogs/ideogram-4-open-weight-image-model)) |
| Inference code license | [Apache 2.0](https://github.com/ideogram-oss/ideogram4) |
| Weights license | [Ideogram Non-Commercial Model Agreement](https://ideogram.ai/licensing/) |
| Release date | [June 3, 2026](https://ideogram.ai/blog/ideogram-4.0/) |

Ideogram 4 was trained from scratch, not derived from or fine-tuned on any other model — but that applies to the diffusion transformer itself, not the text encoder. The text encoder is [Qwen3-VL-8B-Instruct](https://huggingface.co/ideogram-ai/ideogram-4-nf4), an existing open vision-language model run in text-only mode, not a proprietary Ideogram component. The from-scratch training still matters for licensing clarity — the diffusion transformer has no inherited IP obligations from FLUX, Stable Diffusion, or any other image-model base.

---

## The License Split and What It Means for Your Project

The weight license is the critical decision gate for any builder evaluating Ideogram 4.

**Non-commercial use is free.** Research, personal projects, local experimentation, fine-tuning for research purposes, academic work — [all of this falls under the Non-Commercial Model Agreement without cost](https://ideogram.ai/licensing/). You can download the weights from Hugging Face today and start running inference.

**Commercial use requires a paid license, and it's tiered.** [Ideogram's self-serve commercial license](https://ideogram.ai/licensing/) covers self-hosting the public nf4/fp8 quantized weights for 10K–100K images/month at $300/month (billed annually) — but it does **not** include full-precision weights. [Full-precision weights, higher volume (100K+ images/month), customer-facing products, or API-like access for third parties require Ideogram's Enterprise track](https://ideogram.ai/licensing/), which adds support, onboarding, security review, and custom legal terms.

**The Ideogram API is a separate track.** If you want production deployment without managing the licensing negotiation and GPU infrastructure, [Ideogram operates three per-image API pricing tiers](https://developer.puter.com/tutorials/ideogram-api-pricing/) — Turbo ($0.03/image), Default ($0.06/image), and Quality ($0.10/image). This is the faster path for most product builders — you pay per generation rather than per weight access, and [the API already carries commercial rights](https://ideogram.ai/licensing/). The tradeoff is API dependency versus model ownership.

For builders evaluating where to sit: if you're prototyping, exploring the JSON interface, or building a non-commercial product, the free weights are the right starting point. If you're building a commercial pipeline and need to ship in the next few months, the API path removes friction. If you need on-premises deployment, data isolation, or volume pricing, contact Ideogram directly about commercial weight licensing.

---

## Hosting and Deployment Options

| Option | Who It's For | Notes |
|--------|-------------|-------|
| Hugging Face ([`ideogram-ai/ideogram-4-nf4`](https://huggingface.co/ideogram-ai/ideogram-4-nf4)) | Research, local experimentation | Quantized (nf4); free non-commercial |
| Hugging Face ([`ideogram-ai/ideogram-4-fp8`](https://huggingface.co/ideogram-ai/ideogram-4-fp8)) | Higher-fidelity local runs | Quantized (fp8); free non-commercial |
| GitHub ([`ideogram-oss/ideogram4`](https://github.com/ideogram-oss/ideogram4)) | Developers who want the inference code | Apache 2.0 code; full control |
| [ComfyUI](https://blog.comfy.org/p/ideogram-4-day-0-support-in-comfyui) | Node-graph pipelines, JSON control | Native day-0 support (ComfyUI 0.24.0+); standard image nodes + JSON prompt input |
| [fal.ai](https://fal.ai/ideogram-4) | Hosted inference, no GPU management | Serverless per-image pricing |
| [Ideogram API](https://ideogram.ai/licensing/) | Product builders, commercial use | Three per-image pricing tiers; commercial rights included |

ComfyUI's native support is worth noting: [recent ComfyUI releases added native nodes for Ideogram 4.0 on launch day](https://blog.comfy.org/p/ideogram-4-day-0-support-in-comfyui), so you can pass structured JSON prompts directly through standard image nodes and get bounding-box layout and palette control in a visual workflow. For builders already using ComfyUI for image pipelines, the upgrade path is the same workflow with a richer prompt format.

---

## What Ideogram 4 Is Good At

**In-image text rendering** is the flagship capability. [Ideogram's founders — former Google Brain researchers who worked on Imagen — started the company specifically to solve legible in-image text](https://voicebot.ai/2023/08/31/former-googlers-launch-synthetic-image-ai-startup-ideogram-with-16-5m-raise/), for use cases like packaging, posters, signage, UI mockups, and marketing assets with embedded type. Ideogram 4 continues that trajectory, [scoring 0.97 on English OCR accuracy for in-image text per Ideogram's own benchmark](https://ideogram.ai/blog/ideogram-4.0/). Designers and product teams generating brand assets programmatically are the primary audience.

**Templated design pipelines** are the new territory that the JSON interface opens. If your application generates personalized images at scale — marketing email headers, product cards, localized ad creatives, greeting cards, report covers — the JSON prompting surface lets you build a layout schema once and vary only the parameters that need to change across outputs. This is the use case that flat-prompt models cannot reliably serve.

**Typography-heavy compositions** — posters, book covers, announcement graphics, event graphics, social card templates — benefit from explicit text bounding-box control. You stop fighting the model's default text placement and start directing it.

**Brand consistency at scale** becomes tractable when you can constrain color palettes to a brand's hex codes and specify compositional rules per asset type.

---

## Where Ideogram 4 Is Not the Best Choice

**General photorealism** is not where Ideogram 4 leads. [FLUX.2 is specifically optimized for photorealism, and Ideogram's photorealistic output still trails Midjourney for purely artistic, non-text images](https://theaidude.net/compare/flux2-vs-ideogram). If your use case is photorealistic product photography or portrait generation with no text element, competing models remain stronger.

**Unstructured creative generation** — the "surprise me" use case — does not benefit from Ideogram 4's architecture in the same way. The JSON interface adds value when you know what you want; it does not add value when exploration is the goal.

**Teams that need managed compliance** for commercial deployment right now face more friction than with the API track. The weight licensing negotiation adds a step. For fast-moving commercial builds, the Ideogram API or fal.ai hosted inference removes that step.

---

## Practical Builder Decision Map

**You want to prototype or evaluate the model**: Download the nf4 or fp8 checkpoint from Hugging Face. Run locally. Use the JSON interface to explore layout control. No cost, no licensing friction for non-commercial work.

**You're building a non-commercial product** (open source tool, research project, educational product): Weights are free under the Non-Commercial Model Agreement. Set up via GitHub inference code or ComfyUI.

**You're building a commercial product and need to ship in weeks**: Use the Ideogram API. Three tiers available, commercial rights included, no GPU management required.

**You're building a commercial pipeline that requires on-premises deployment or data isolation**: Contact Ideogram about commercial weight licensing. Expect a negotiation step before weights can be used in production.

**You already have a ComfyUI pipeline for image generation**: Add Ideogram 4 as a new model node. Pass structured JSON prompts using the bounding-box and palette parameters. Compare output consistency against your existing model on the specific use cases you care about.

**You're building marketing automation or content generation at scale** with brand guidelines to maintain: The JSON palette constraint and bounding-box layout control are specifically designed for this. Ideogram 4 plus a JSON template schema for your brand's layout rules is closer to a designed output pipeline than to a probabilistic image generator.

---

## Connection to the Broader Image Generation Landscape

Ideogram 4 arrives at a moment when the open-weight image model tier is consolidating. FLUX.2, Qwen's visual models, and now Ideogram 4 are all competing for the "best open-weight image model" position. [On DesignArena's leaderboard, Ideogram 4 sits roughly 114 Elo points above the next open-weight model (HunyuanImage 3.0)](https://firethering.com/ideogram-4-open-weight/) in design-oriented tasks.

The closed-model providers remain ahead on photorealism, but as of this writing none of them publish a comparable structured bounding-box + palette + typography JSON interface — [Ideogram 4's JSON prompting schema](https://docs.ideogram.ai/using-ideogram/getting-started/prompting-guide/4.-json-prompting-ideogram-4.0) is documented specifically as part of this release.

The existing Ideogram review in our [Reviews section](/reviews/ideogram-ai-image-generation-text-rendering/) covers the platform history, the [founding team (ex-Google Brain, Imagen)](https://voicebot.ai/2023/08/31/former-googlers-launch-synthetic-image-ai-startup-ideogram-with-16-5m-raise/), the Ideogram 3.0 model era, and the Canvas editor. Ideogram 4 builds on that review's context — it is the same company's text-rendering DNA extended into a fully open-weight, JSON-native architecture.

---

## Summary

Ideogram 4.0 is the first open-weight image generation model that offers a structured programmatic interface for layout control. The JSON prompting surface — bounding boxes, palette constraints, multi-element typography — is what separates it from every other open-weight image model available today.

The licensing split is the practical decision gate: non-commercial use is free; commercial pipelines need either a paid weight license or the API track. For builders who work in design automation, brand asset generation, or any pipeline where compositional consistency across many images matters, Ideogram 4 is worth evaluating now. The nf4 checkpoint on Hugging Face and the ComfyUI native node provide the lowest-friction entry point.


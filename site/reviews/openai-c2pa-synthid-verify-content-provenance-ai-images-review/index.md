# OpenAI Verify Review — C2PA + SynthID Dual Watermarking for AI Image Provenance

> On May 19, 2026, OpenAI joined the C2PA steering committee and began embedding Google DeepMind's SynthID watermark in all images generated via ChatGPT, the API, and Codex. The Verify research preview tool lets anyone check whether an image carries these signals. We explain what it does, how C2PA and SynthID differ, and what the initiative actually accomplishes — and what it doesn't.


On May 19, 2026, OpenAI announced three simultaneous moves: joining the C2PA standards steering committee, embedding Google DeepMind's SynthID watermark in all images from ChatGPT, the API, and Codex, and releasing a public research preview tool called **Verify** that lets anyone upload an image and check whether it carries either signal.

This is infrastructure-level work, not a product launch. No new model capability, no feature announcement. What OpenAI is doing is joining a cross-industry effort to make AI-generated images detectable — and doing it by adopting a watermarking standard built by its main rival.

The initiative matters. It also has real limitations. This review explains both.

---

## What C2PA Is

The Coalition for Content Provenance and Authenticity (C2PA) is an open technical standards body formed in 2021, merging Adobe's Content Authenticity Initiative and a Microsoft/BBC initiative called Project Origin. It produces a specification for embedding tamper-evident provenance information into media files.

C2PA works by embedding a cryptographically signed data structure — a "C2PA Manifest" — inside an image's file header. The manifest contains rich structured information: which tool created the image, the creation date and time, editing history, authorship claims. It uses standard PKI (X.509 certificates from certificate authorities like DigiCert) and a Time-Stamp Authority server to verify when signing occurred.

The cryptographic signature means any tampering with the file or its metadata breaks the record. Compliant tools display a visible "Content Credentials" badge (a small cr symbol) when an image carries valid C2PA metadata. The underlying data is not visible to the naked eye but is readable by any software that implements the open specification.

As of May 2026, the C2PA steering committee includes Adobe, Amazon, BBC, Google, Intel, Meta, Microsoft, OpenAI, Publicis Groupe, Sony, and Truepic. By joining as a steering member (not just an implementer), OpenAI participates in writing the standard itself — a higher commitment than compliance.

---

## What SynthID Is

SynthID was developed by Google DeepMind and first publicly demonstrated in 2023. It takes a fundamentally different approach to provenance: rather than embedding metadata in a file header, it embeds an invisible signal directly into the image pixels during the generation process.

In latent diffusion models — the architecture underlying most modern image generators — SynthID embeds the watermark during the diffusion process itself, before the final decoding step. The signal lives in the latent representation, not as a post-processing overlay. Detection uses a neural network trained to recognize the statistical pattern of that embedding.

Google has embedded SynthID in more than 100 billion images and videos across its own products. As of Google I/O 2026, new SynthID adopters include OpenAI, Nvidia, Kakao, and ElevenLabs — a notable cross-industry expansion.

---

## The Two-Layer Approach

OpenAI's announcement explicitly frames this as a "dual-layer" approach, and the reason is that C2PA metadata and SynthID watermarks have complementary failure modes:

| Property | C2PA Metadata | SynthID Watermark |
|---|---|---|
| Where stored | File header | Embedded in pixel data during generation |
| Information richness | High — tool, date, history, authorship | Low — only "AI-generated" signal |
| Survives screenshot | No — screenshot strips file headers | Yes — watermark is in pixel data |
| Survives crop | No | Yes (specifically designed for this) |
| Survives JPEG re-save | No | Yes |
| Survives social media re-upload | Usually stripped | Survives in many cases |
| Tamper evidence | Yes — cryptographic signature | No |
| Detection openness | Open standard | Proprietary to Google |

C2PA carries the rich context — who made it, when, with what. SynthID carries the durable signal — survives the operations that strip file headers (screenshots, crops, JPEG compression, social re-uploads). Neither alone is sufficient; together they cover different attack surfaces.

---

## The Verify Tool

OpenAI's Verify tool (`openai.com/verify`) accepts image uploads (PNG, JPG, WEBP) and checks for both signals independently:

1. **C2PA check** — Does the file contain valid Content Credentials?
2. **SynthID check** — Does the pixel data carry a SynthID watermark?

The tool returns two independent answers. An image can have either, both, or neither. For best results, OpenAI advises cropping screenshots closely around the image content.

**Critical limitation:** If no signal is detected, Verify explicitly cannot conclude the image is not AI-generated. Absence of signal means one of several things: the image predates the provenance rollout, the metadata was stripped, the watermark was degraded, or the image came from a different generator entirely. The tool can confirm OpenAI provenance; it cannot rule out AI origin.

Verify is a research preview, not a finalized product. OpenAI has stated plans to expand it over time but has not given a specific roadmap.

---

## Why This Is Significant

**The industry alignment is real.** C2PA now has most major tech companies on its steering committee. SynthID adopters now span multiple competing AI labs. The EU AI Act, which requires AI systems to mark outputs as artificially generated in machine-readable format (full compliance required August 2026), is a regulatory tailwind pushing the entire industry in the same direction. Camera manufacturers — Leica, Nikon, Sony — already support C2PA Content Credentials, meaning the same standard covers both human-captured and AI-generated content.

**OpenAI adopting Google's watermark is notable.** SynthID is a proprietary Google DeepMind system. OpenAI, the most direct Google competitor in consumer AI, chose to implement Google's watermarking infrastructure rather than build its own. Industry analysts describe this as a signal that provenance is being treated as collaborative infrastructure rather than competitive differentiation — at least for now.

**Detection will reach scale.** Google is integrating SynthID detection natively into Google Search and Chrome. This means detection infrastructure will reach users as part of their existing browsing experience, without requiring them to seek out a dedicated tool. That scale matters for actually changing how disinformation is detected in practice.

---

## What It Doesn't Solve

**Coverage gap.** OpenAI's provenance measures apply only to OpenAI-generated images. The vast majority of AI-generated content online comes from Midjourney, Stability AI, open-source models (Flux, Stable Diffusion), and countless fine-tuned local variants — none of which have adopted SynthID or C2PA. The initiative prevents OpenAI from contributing to the provenance problem; it does not address the broader ecosystem.

**SynthID has been bypassed.** This is the most significant technical limitation. Published research and open-source tools have demonstrated removal attacks:
- The "reverse-SynthID" repository claims 91% removal of watermark energy with minimal image quality loss (PSNR 43.5 dB, SSIM 0.997)
- UnMarker, a USENIX Security 2025 paper, claims 79% removal against SynthID
- A GitHub repository (`wiltodelta/remove-ai-watermarks`) explicitly targets SynthID, C2PA EXIF data, and other provenance signals

Google disputes specific figures but does not deny the attack class. The underlying challenge: once an embedding methodology is understood, removal can be engineered. Security through obscurity is not durable.

**C2PA stripping is trivially easy.** Screenshot the image. Route it through any major social media platform. Route it through any image editor that doesn't preserve EXIF data. All of these operations strip the C2PA manifest. This is a known, unsolved limitation of all file-header-based provenance approaches — which is precisely why SynthID exists as the second layer.

**SynthID detection is proprietary.** Unlike C2PA, where any developer can implement detection by reading the open specification, SynthID detection requires Google's infrastructure. This creates a single point of failure and a dependency on Google's continued participation. Third parties cannot independently verify SynthID signals.

**Open-source models remain outside the system.** Models running locally have no technical obligation to adopt watermarking standards, and many users running local image generators specifically do so to avoid oversight. These are completely outside the provenance system and likely represent a growing share of AI-generated disinformation as generation quality improves.

---

## Rating: 3/5

OpenAI's content provenance initiative is genuinely useful infrastructure — not a silver bullet for AI-generated disinformation, but a meaningful contribution to the shared detection stack. The dual-layer approach is technically sound and honest about the tradeoffs. The cross-industry alignment on C2PA and SynthID represents real progress toward a world where AI-generated content is routinely identifiable.

The 3/5 reflects the gap between what this accomplishes and what would actually solve the problem. Coverage is limited to one generator among many. Bypasses exist for both layers. The Verify tool's most honest output is "we found a signal" or "we didn't look for anything outside our scope." The EU AI Act deadline is the forcing function here — this is compliance infrastructure in progress, not a solved problem.

The initiative is worth watching. When SynthID detection reaches Google Search and Chrome at scale, and if C2PA adoption expands across more generators, the detection coverage picture will look different. For now: useful, limited, and the right direction.

---

*ChatForest researches AI tools and platforms; we do not test them hands-on. Our reviews are based on publicly available documentation, technical research, and press coverage. This review does not claim to have tested the Verify tool or SynthID detection systems directly.*


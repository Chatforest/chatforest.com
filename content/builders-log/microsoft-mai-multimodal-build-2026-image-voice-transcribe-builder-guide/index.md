---
title: "MAI-Image-2.5, MAI-Voice-2, MAI-Transcribe-1.5: Microsoft's Complete Multimodal Stack"
date: 2026-06-03
description: "Microsoft announced three multimodal model upgrades at Build 2026: MAI-Image-2.5 (now with image editing), MAI-Voice-2 (15+ languages, expanded emotions), and MAI-Transcribe-1.5 (43 languages, MoE architecture, 5x faster). Here's what builders need to know."
og_description: "Microsoft unveiled a complete multimodal stack at Build 2026 — image generation/editing, voice synthesis, and transcription — all in one Azure AI Foundry API surface. MAI-Image-2.5 lands at #3 on Arena and adds image editing. MAI-Voice-2 goes multilingual with 15+ languages and emotional range. MAI-Transcribe-1.5 covers 43 languages with automatic detection and mixture-of-experts architecture."
content_type: "Builder Guide"
card_description: "Microsoft announced three model upgrades at Build 2026 that together form a complete multimodal stack on Azure: MAI-Image-2.5 (image editing, better text rendering, Arena #3), MAI-Voice-2 (15+ languages, emotional synthesis, voice cloning), and MAI-Transcribe-1.5 (43 languages, automatic detection, mixture-of-experts, 5x faster, $0.36/hour). If you're building anything that involves hearing, speaking, or seeing — you now have a single-vendor option that didn't exist six weeks ago."
tags: ["microsoft", "mai", "mai-image", "mai-voice", "mai-transcribe", "build-2026", "multimodal", "azure-ai-foundry", "tts", "stt", "image-generation", "voice-synthesis", "transcription", "speech-to-text"]
categories: ["builders-log"]
author: "ChatForest"
---

**At a glance:** Three MAI model upgrades announced at Microsoft Build 2026, June 2, 2026. MAI-Image-2.5: image editing (new), improved text rendering, Arena #3 (score 1,254). MAI-Voice-2: 15+ languages, expanded emotional range, Flash variant. MAI-Transcribe-1.5: 43 languages, automatic language detection, MoE architecture, ~5x faster than competitors, $0.36/hour. All available via Azure AI Foundry and the MAI Playground. Part of our **[Builder's Log](/builders-log/)**.

---

Microsoft spent a lot of Build 2026 talking about reasoning models, agent frameworks, and enterprise compute. But quietly, one of the most practically useful announcements was the upgrade of three models that form a complete multimodal pipeline: the ability to hear, speak, and see, all within a single Azure API surface.

MAI-Transcribe-1.5 handles speech-to-text. MAI-Voice-2 handles text-to-speech. MAI-Image-2.5 handles image generation and, for the first time in the MAI-Image line, image editing. The three were announced together at Build, and they're available — or shortly available — together in Microsoft Foundry.

For builders on Azure, that combination has a concrete implication: you can now build a fully functional voice agent with on-brand image generation capability without touching a third-party vendor. One billing account. One SLA. One data residency agreement.

That's the framing Microsoft is going for. Let's look at each model on its own terms.

---

## MAI-Image-2.5: Image Editing Arrives

MAI-Image-2 launched in April 2026 through Microsoft Foundry. MAI-Image-2-Efficient, a faster/cheaper variant, followed shortly after. MAI-Image-2.5 was unveiled at Build 2026 and quietly entered the Arena leaderboard a few days before the conference — where it debuted at #3 with a score of 1,254, a 72-point improvement over MAI-Image-2.0.

The two models ranked above it: OpenAI gpt-image-2 and Google's image model. For a model that didn't exist six weeks ago, that's a meaningful position.

### What's new in 2.5

**Image editing.** This is the headline capability change. MAI-Image-2 was generation-only: you provided a text prompt, you got an image. MAI-Image-2.5 accepts image uploads alongside text prompts. You can submit an existing image and a modification instruction — change the background, alter a style, swap an element — and get back a modified version. This is the same capability class as OpenAI's gpt-image-1/2 and Google's Imagen 3 Edit, and it's a meaningful expansion for builders doing automated content workflows.

**Better text rendering.** Words embedded in generated images were a known weakness of the MAI-Image-2 series and of AI image models generally. MAI-Image-2.5 sharpens this significantly. If your use case involves generating images with visible text — product mockups, presentation slides, branded assets — this is a practical quality upgrade.

**Closer prompt adherence.** The 2.5 generation is more faithful to complex, multi-element prompts. More detail in the prompt translates more reliably to more detail in the output.

**Two variants.** MAI-Image-2.5 (standard, quality-optimized) and MAI-Image-2.5e (efficient, faster and cheaper). The same structure as the 2.0 generation.

### Pricing and availability

MAI-Image-2 pricing, for reference:
- Text input: $5 per 1M tokens
- Image output: $33 per 1M tokens
- MAI-Image-2-Efficient image output: $19.50 per 1M tokens

MAI-Image-2.5 pricing was not announced at Build. The structure is expected to follow the same pattern. The model is available in the MAI Playground for testing and coming to Microsoft Foundry within two weeks of Build. MAI-Image-2.5 is also live in PowerPoint Copilot as of Build day; OneDrive integration is coming.

### Builder use cases

- **Automated branded assets**: Generate on-brand visual content inside M365 workflows without leaving the ecosystem
- **Image editing pipelines**: Submit a product photo and a style instruction; get back a modified version for a different channel or market
- **Presentation automation**: Text-in-image rendering quality matters here — the 2.5 improvement reduces manual correction cycles
- **Copilot-connected image workflows**: If your users are in Teams or OneDrive, the embedded integration means zero additional plumbing

---

## MAI-Voice-2: Multilingual Synthesis with Emotional Range

MAI-Voice-1 launched in April 2026 as an English-only TTS model with voice cloning capability. At $22 per million characters, it positioned as a competitive enterprise option — between OpenAI TTS at $15/1M (standard) and ElevenLabs at substantially higher subscription tiers.

MAI-Voice-2 is the multilingual upgrade.

### What's new in Voice 2

**15+ languages.** MAI-Voice-1 was English-only. MAI-Voice-2 adds German, Australian English (as a distinct variant), Spanish, French, Hindi, Indonesian, Italian, Japanese, Korean, Dutch, Portuguese, Turkish, Vietnamese, and Chinese. For builders serving international users or building localized voice agents, this changes the calculus significantly.

**Expanded emotional range.** MAI-Voice-1 had emotional expressiveness, but MAI-Voice-2 adds specific categories: angry, confused, embarrassed, joyful, and whispering. That list tells you what use cases Microsoft is targeting — conversational agents, not just narration. A customer service bot that can sound apologetic when something goes wrong, or joyful when a transaction succeeds, is meaningfully more engaging than a flat TTS output.

**Flash variant.** A faster (and presumably cheaper) Flash version of MAI-Voice-2 is shipping alongside the standard model. Specifics on the speed/quality tradeoff weren't published at Build.

**Voice cloning.** MAI-Voice-1 supported custom voice creation from a short audio sample. This capability carries forward in MAI-Voice-2.

### Speed context

MAI-Voice-1 generated 60 seconds of audio in roughly 1 second — a real-time factor of about 0.017x (the output is produced far faster than it would take to speak it). MAI-Voice-2 speed specifics weren't published, but the Flash variant suggests Microsoft is continuing to optimize for latency.

For reference: ElevenLabs Flash v2.5 claims ~75ms latency for streaming output. OpenAI TTS is roughly 200ms first-byte latency. The MAI models generate a full audio file server-side rather than streaming in the same mode, so latency comparisons depend on the specific integration pattern.

### Pricing and availability

MAI-Voice-1 was priced at $22 per million characters. MAI-Voice-2 pricing was not announced at Build. Available via Azure AI Foundry and the MAI Playground.

### Builder use cases

- **Multilingual voice agents**: Customer service, IVR, support bots — same voice stack across markets
- **Localized content narration**: Audiobooks, explainer videos, course content across 15 languages without switching vendors
- **Emotionally expressive agents**: The emotional range makes MAI-Voice-2 the better choice over MAI-Voice-1 for any conversational interface where tone matters
- **Full voice stack within Azure**: Pair with MAI-Transcribe-1.5 for a complete listen-and-speak pipeline in one API surface

---

## MAI-Transcribe-1.5: 43 Languages, Mixture-of-Experts, $0.36/Hour

MAI-Transcribe-1 launched in April 2026 at $0.36 per hour of audio — competitive with Deepgram at comparable tiers and AssemblyAI at ~$0.37/hour. Its benchmark position on launch was strong: it outperformed Whisper large-v3, GPT-4o Transcribe, and Gemini 1.5 Flash on word error rate in Microsoft's published comparisons.

MAI-Transcribe-1.5 is a meaningful architectural upgrade, not just a capability increment.

### What's new in Transcribe 1.5

**43 languages, up from 25.** Language coverage is a practical ceiling for multilingual voice products. At 43 languages, MAI-Transcribe-1.5 covers the overwhelming majority of commercial market needs. Specific new languages weren't enumerated in Build materials; the total count is confirmed.

**Automatic language detection.** You no longer need to specify the input language. The model identifies the spoken language and applies the appropriate model without configuration. For applications where you don't control what language a user speaks — international customer support, open-ended voice agents — this removes a layer of infrastructure that previously required a detection step or a multi-pass pipeline.

**Mixture-of-experts architecture.** MAI-Transcribe-1.5 uses specialized sub-networks for different languages, dialects, and noise profiles. The practical implication: languages that would previously require a separately fine-tuned model now benefit from dedicated internal routing, without requiring you to pick the right model variant per language.

**Challenging acoustic environments.** Crowds, construction noise, overlapping speakers in meeting recordings — the model handles these explicitly. Meeting transcription has long been the high-value use case for enterprise STT, and the overlapping-speaker handling is the capability that makes or breaks real-world accuracy there.

**Speed.** Microsoft claims MAI-Transcribe-1.5 is five times faster than competing models. This claim wasn't independently benchmarked publicly at launch. MAI-Transcribe-1 ran 2.5x faster than Azure's previous Fast tier, so the trajectory of performance improvement is real; the specific 5x figure relative to unspecified competitors should be treated as directional.

**WER benchmark position.** Microsoft's published benchmarks show MAI-Transcribe-1.5 achieving the lowest word error rate among major STT models on FLEURS across 43 languages — outperforming Scribe V2, Whisper large-v3, GPT-4o Transcribe, and Gemini 3.1 Flash. Microsoft's benchmarks are self-published, not third-party audited, so weight them accordingly. The comparison direction (better than alternatives) is plausible given MAI-Transcribe-1's strong launch position.

### Pricing and availability

MAI-Transcribe-1 was priced at $0.36/hour. MAI-Transcribe-1.5 pricing was not announced at Build — the expectation is at or near the same entry point. Available via Azure AI Foundry (`ai.azure.com/catalog/models/`) and the MAI Playground. Full API integration is documented at `learn.microsoft.com/azure/foundry/foundry-models/how-to/use-foundry-models-mai`.

### Builder use cases

- **Meeting transcription and summarization**: Teams integration makes this the obvious embedded use case; the overlapping-speaker handling is what makes meeting transcripts accurate
- **Contact center analytics**: Noisy call recordings with automatic language detection — handles international call centers without per-language configuration
- **Medical and legal transcription**: Domain-specific terminology adaptation (claimed, not separately verified) without custom model training
- **Accessibility pipelines**: Caption generation for live events and recordings
- **Full voice pipeline**: Combined with MAI-Voice-2 for complete listen-and-respond agent loops

---

## The Stack Play: One Vendor for Multimodal

The three models form an explicit Microsoft pitch: hear with Transcribe, speak with Voice, see and create with Image. The integration angle is real for builders already inside Azure.

Consider a realistic enterprise voice agent:
1. User speaks → MAI-Transcribe-1.5 converts to text (automatic language detection, no configuration)
2. Agent processes with a reasoning model (MAI-Thinking-1, GPT-4o, or whichever model fits the task)
3. Response requires a diagram or product image → MAI-Image-2.5 generates it
4. Agent speaks the response → MAI-Voice-2 synthesizes in the user's language with appropriate emotion

The entire pipeline runs within Azure AI Foundry. One SLA. One data processing agreement. One billing account. No third-party TOS from ElevenLabs, Deepgram, Stability AI, or anyone else.

For builders in regulated industries — finance, healthcare, government — that simplification isn't just convenient. It's often necessary. Enterprise procurement requires contractual relationships and auditable data flows; adding a third-party TTS or STT vendor for a critical product is a separate compliance project. Microsoft is offering to absorb that overhead into the Azure relationship you likely already have.

### Competitive pricing snapshot

| Capability | Microsoft (MAI) | Alternative | Alternative pricing |
|---|---|---|---|
| Image generation | MAI-Image-2: $33/1M tokens (output) | DALL-E 3 (via Azure) | ~$40/1M tokens |
| TTS | MAI-Voice-1: $22/1M chars | OpenAI TTS (standard) | $15/1M chars |
| TTS | MAI-Voice-1: $22/1M chars | ElevenLabs | ~$180+/1M chars |
| STT | MAI-Transcribe-1: $0.36/hr | Deepgram | ~$0.36/hr |
| STT | MAI-Transcribe-1: $0.36/hr | AssemblyAI | ~$0.37/hr |
| STT | MAI-Transcribe-1: $0.36/hr | OpenAI Whisper (API) | ~$0.36/hr (60 min) |

MAI-Voice-2 pricing not yet announced; MAI-Image-2.5 pricing not yet announced; MAI-Transcribe-1.5 pricing not yet announced. Predecessor pricing above reflects the likely floor.

Microsoft's TTS is not the cheapest option — OpenAI's standard TTS is cheaper per character. But for builders who need multilingual support, emotional expressiveness, and voice cloning within an Azure-native deployment, MAI-Voice-2 is now the clear within-ecosystem choice. ElevenLabs is still the quality leader for voice acting and custom voices, but the price delta is substantial and the contractual overhead is real.

---

## What You Should Do This Week

**Test MAI-Image-2.5 in the MAI Playground.** Specifically test image editing (the new capability) and text rendering on your actual use case. If you've been avoiding AI image generation because of garbled text in outputs, 2.5 is worth another look.

**Request MAI-Foundry access if you don't have it.** The three models are at `azure.microsoft.com/pricing/details/ai-foundry-models/microsoft/` for pricing context and `learn.microsoft.com/azure/foundry/foundry-models/how-to/use-foundry-models-mai` for API access.

**Prototype the full voice stack.** MAI-Transcribe-1.5 + MAI-Voice-2 in a single Azure deployment is a complete voice agent pipeline. The automatic language detection in Transcribe removes a configuration dependency that previously required additional logic.

**Don't rebuild your STT setup today if Deepgram is working.** MAI-Transcribe-1.5 is competitive on price and claims better WER. But "5x faster than competitors" and "lowest WER on FLEURS" are Microsoft's own numbers. If your current STT pipeline works, wait for independent benchmarks before migrating. The case is strongest for builders who are (a) starting fresh or (b) specifically need the 43-language coverage or automatic detection.

**Watch for MAI-Image-2.5 pricing.** The 2.0 structure ($33/1M output tokens, $19.50 efficient) is the baseline. If 2.5 adds image editing at the same price point, it's a strong deal. If it prices editing as a separate tier, that changes the analysis.

---

*ChatForest covers AI tools and infrastructure from a builder's perspective. We research from public sources and do not have hands-on access to Microsoft preview programs.*

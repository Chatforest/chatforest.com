# MAI-Image-2.5, MAI-Voice-2, MAI-Transcribe-1.5: Microsoft's Complete Multimodal Stack

> Microsoft announced three multimodal model upgrades at Build 2026: MAI-Image-2.5 (now with image editing), MAI-Voice-2 (15+ languages, expanded emotions), and MAI-Transcribe-1.5 (43 languages, automatic language detection, 5x faster). Here's what builders need to know.


**At a glance:** [Three MAI model upgrades announced at Microsoft Build 2026](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/new-mai-models-in-microsoft-foundry-across-text-image-voice-and-speech/4524632), June 2, 2026. MAI-Image-2.5: image editing (new), improved text rendering, #3 on the Arena text-to-image leaderboard (score 1,254) and #2 on the Arena image-editing leaderboard. MAI-Voice-2: 15+ languages, expanded emotional range, Flash variant (announced, not yet GA). MAI-Transcribe-1.5: 43 languages, automatic language detection, ~5x faster than named competitors on long audio (Microsoft's own figure), $0.36/hour. All available via Azure AI Foundry and the MAI Playground. Part of our **[Builder's Log](/builders-log/)**.

---

Microsoft spent a lot of Build 2026 talking about reasoning models, agent frameworks, and enterprise compute. But quietly, one of the most practically useful announcements was the upgrade of three models that form a complete multimodal pipeline: the ability to hear, speak, and see, all within a single Azure API surface.

MAI-Transcribe-1.5 handles speech-to-text. MAI-Voice-2 handles text-to-speech. MAI-Image-2.5 handles image generation and, for the first time in the MAI-Image line, image editing. The three were announced together at Build, and they're available — or shortly available — together in Microsoft Foundry.

For builders on Azure, that combination has a concrete implication: you can now build a fully functional voice agent with on-brand image generation capability without touching a third-party vendor. One billing account. One SLA. One data residency agreement.

That's the framing Microsoft is going for. Let's look at each model on its own terms.

---

## MAI-Image-2.5: Image Editing Arrives

[MAI-Image-2 launched in April 2026](https://microsoft.ai/news/today-were-announcing-3-new-world-class-mai-models-available-in-foundry/) through Microsoft Foundry. [MAI-Image-2-Efficient](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-mai-image-2-efficient-faster-more-efficient-image-generation/4510918), a faster/cheaper variant, followed shortly after. MAI-Image-2.5 was unveiled at Build 2026 and quietly entered the Arena leaderboard a few days before the conference — where it [debuted at #3 on the Text-to-Image Arena with a score of 1,254, a +72 point improvement over MAI-Image-2](https://winbuzzer.com/2026/05/28/microsoft-launches-mai-image-25-with-arena-top-3-claim-xcxwbn/).

At the time, [OpenAI's gpt-image-2 led the same leaderboard snapshot](https://winbuzzer.com/2026/05/28/microsoft-launches-mai-image-25-with-arena-top-3-claim-xcxwbn/) at a score of 1,388, and [Google's Nano Banana 2 (Gemini 3.1 Flash Image) scored close enough to be described as "on par" with MAI-Image-2.5](https://the-decoder.com/microsofts-mai-image-2-5-pulls-even-with-googles-nano-banana-2-on-benchmarks/). For a model that didn't exist six weeks ago, that's a meaningful position. (Arena leaderboards are live and re-rank as new models join; this reflects the ranking at MAI-Image-2.5's debut, not necessarily today's snapshot.)

### What's new in 2.5

**Image editing.** This is the headline capability change. MAI-Image-2 was generation-only: you provided a text prompt, you got an image. MAI-Image-2.5 accepts image uploads alongside text prompts. You can submit an existing image and a modification instruction — change the background, alter a style, swap an element — and get back a modified version. This is the same capability class as [OpenAI's gpt-image-1 edit endpoint](https://platform.openai.com/docs/guides/image-generation) and [Google's Gemini image editing ("Nano Banana")](https://microsoft.ai/news/introducing-mai-image-2-5/), and it's a meaningful expansion for builders doing automated content workflows. On Arena's dedicated [image-editing leaderboard, MAI-Image-2.5 ranks No. 2](https://microsoft.ai/news/introducing-mai-image-2-5/), a separate ranking from its No. 3 text-to-image position above.

**Better text rendering.** Words embedded in generated images were a known weakness of the MAI-Image-2 series and of AI image models generally. MAI-Image-2.5 sharpens this significantly. If your use case involves generating images with visible text — product mockups, presentation slides, branded assets — this is a practical quality upgrade.

**Closer prompt adherence.** The 2.5 generation is more faithful to complex, multi-element prompts. More detail in the prompt translates more reliably to more detail in the output.

**Two variants.** [MAI-Image-2.5 (standard, quality-optimized) and MAI-Image-2.5-Flash (faster and cheaper)](https://microsoft.ai/news/introducing-mai-image-2-5/) — the officially shipped name is "Flash," not the "2.5e" naming some pre-Build leaks expected. The same two-tier structure as the 2.0 generation.

### Pricing and availability

[MAI-Image-2 pricing](https://microsoft.ai/news/today-were-announcing-3-new-world-class-mai-models-available-in-foundry/), for reference:
- Text input: $5 per 1M tokens
- Image output: $33 per 1M tokens
- [MAI-Image-2-Efficient image output: $19.50 per 1M tokens](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-mai-image-2-efficient-faster-more-efficient-image-generation/4510918)

[MAI-Image-2.5 pricing was announced at Build](https://microsoft.ai/news/introducing-mai-image-2-5/): $5 per 1M text-input tokens, $8 per 1M image-input tokens, and $47 per 1M image-output tokens for the standard model; $1.75 per 1M text/image-input tokens and $33 per 1M image-output tokens for MAI-Image-2.5-Flash. [MAI-Image-2.5 and MAI-Image-2.5-Flash were available to developers in Foundry the same day as the Build announcement](https://microsoft.ai/news/introducing-mai-image-2-5/), not on a two-week delay. It's also in the MAI Playground for testing, [live in PowerPoint Copilot, and rolling out to OneDrive](https://microsoft.ai/news/introducing-mai-image-2-5/).

### Builder use cases

- **Automated branded assets**: Generate on-brand visual content inside M365 workflows without leaving the ecosystem
- **Image editing pipelines**: Submit a product photo and a style instruction; get back a modified version for a different channel or market
- **Presentation automation**: Text-in-image rendering quality matters here — the 2.5 improvement reduces manual correction cycles
- **Copilot-connected image workflows**: If your users are in Teams or OneDrive, the embedded integration means zero additional plumbing

---

## MAI-Voice-2: Multilingual Synthesis with Emotional Range

[MAI-Voice-1 launched in April 2026](https://microsoft.ai/news/today-were-announcing-3-new-world-class-mai-models-available-in-foundry/) as an English-only TTS model with voice cloning capability. At [$22 per million characters](https://microsoft.ai/news/today-were-announcing-3-new-world-class-mai-models-available-in-foundry/), it positioned as a competitive enterprise option — between [OpenAI TTS at $15/1M characters (tts-1, standard)](https://platform.openai.com/docs/pricing) and ElevenLabs at substantially higher subscription tiers.

MAI-Voice-2 is the multilingual upgrade.

### What's new in Voice 2

**15+ languages.** MAI-Voice-1 was English-only. [MAI-Voice-2 adds English (Australia), Italian, French, German, Hindi, Spanish (Spain and Mexico), Portuguese (Brazil and Portugal), Korean, Chinese (Simplified), Turkish, Russian, Thai, Dutch, Romanian, and Hungarian](https://microsoft.ai/news/mai-voice-2/) — 17 language/locale combinations in total, with mid-sentence code-switching for Hindi-English and Spanish-English pairs. (Note: some pre-Build coverage listed Indonesian, Japanese, and Vietnamese instead; the shipped language list per Microsoft's own model announcement does not include those three.) For builders serving international users or building localized voice agents, this changes the calculus significantly.

**Expanded emotional range.** MAI-Voice-1 had emotional expressiveness, but [MAI-Voice-2 adds granular emotion tags](https://microsoft.ai/news/mai-voice-2/) — [Microsoft's own model page demonstrates joy, anger, disgust, fear, and sadness](https://microsoft.ai/models/mai-voice-2/), while [launch-day samples also showed confused, embarrassed, excited, and whispered deliveries](https://microsoft.ai/news/mai-voice-2/). That list tells you what use cases Microsoft is targeting — conversational agents, not just narration. A customer service bot that can sound apologetic when something goes wrong, or joyful when a transaction succeeds, is meaningfully more engaging than a flat TTS output.

**Flash variant.** [MAI-Voice-2-Flash was announced alongside the standard model at Build](https://mer.vin/2026/06/mai-voice-2-flash-ultra-low-latency-speech-for-voice-agents-preview/), but it was listed as "coming soon" rather than generally available on launch day. Specifics on the speed/quality tradeoff weren't published at Build.

**Voice cloning.** MAI-Voice-1 supported custom voice creation from a short audio sample. This capability carries forward in MAI-Voice-2.

### Speed context

[MAI-Voice-1 generated 60 seconds of audio in roughly 1 second](https://microsoft.ai/news/today-were-announcing-3-new-world-class-mai-models-available-in-foundry/) — a real-time factor of about 0.017x (the output is produced far faster than it would take to speak it). MAI-Voice-2 speed specifics weren't published, but the Flash variant suggests Microsoft is continuing to optimize for latency.

For reference: [ElevenLabs Flash v2.5 claims ~75ms model-inference latency](https://elevenlabs.io/docs/eleven-api/concepts/latency) (end-to-end latency varies with network and request conditions). OpenAI doesn't publish a single official TTS latency figure; [independent benchmarking of time-to-first-audio for OpenAI's TTS models puts it well above ElevenLabs Flash](https://gradium.ai/content/tts-latency-benchmark-2026), though the exact number depends heavily on which OpenAI TTS model and test conditions are used. The MAI models generate a full audio file server-side rather than streaming in the same mode, so latency comparisons depend on the specific integration pattern.

### Pricing and availability

MAI-Voice-1 was priced at $22 per million characters, and [MAI-Voice-2 launched at the same $22 per million characters](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/new-mai-models-in-microsoft-foundry-across-text-image-voice-and-speech/4524632) — Microsoft did not raise the price for the multilingual/emotional upgrade. MAI-Voice-2-Flash pricing wasn't published at Build. Available via Azure AI Foundry and the MAI Playground.

### Builder use cases

- **Multilingual voice agents**: Customer service, IVR, support bots — same voice stack across markets
- **Localized content narration**: Audiobooks, explainer videos, course content across 15 languages without switching vendors
- **Emotionally expressive agents**: The emotional range makes MAI-Voice-2 the better choice over MAI-Voice-1 for any conversational interface where tone matters
- **Full voice stack within Azure**: Pair with MAI-Transcribe-1.5 for a complete listen-and-speak pipeline in one API surface

---

## MAI-Transcribe-1.5: 43 Languages, Automatic Language Detection, $0.36/Hour

[MAI-Transcribe-1 launched in April 2026 at $0.36 per hour of audio](https://microsoft.ai/news/state-of-the-art-speech-recognition-with-mai-transcribe-1/) — competitive with STT pricing at the time from Deepgram and AssemblyAI (both vendors have since changed their tiers and pricing; see the pricing table below for current rates). Its benchmark position on launch was strong: [it outperformed Whisper large-v3, GPT-4o Transcribe (called GPT-Transcribe in Microsoft's post), and Gemini 3.1 Flash on word error rate](https://microsoft.ai/news/state-of-the-art-speech-recognition-with-mai-transcribe-1/) in Microsoft's published comparisons (3.9% average WER on FLEURS across 25 languages).

MAI-Transcribe-1.5 is a meaningful capability upgrade over MAI-Transcribe-1, not just an incremental refresh.

### What's new in Transcribe 1.5

**[43 languages, up from 25](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/new-mai-models-in-microsoft-foundry-across-text-image-voice-and-speech/4524632).** Language coverage is a practical ceiling for multilingual voice products. At 43 languages, MAI-Transcribe-1.5 covers the overwhelming majority of commercial market needs. Specific new languages weren't enumerated in Build materials; the total count is confirmed.

**[Automatic language detection.](https://microsoft.ai/models/mai-transcribe-1-5/)** You no longer need to specify the input language — Microsoft's own model page confirms "automatic language detection included." The model identifies the spoken language and applies the appropriate model without configuration. For applications where you don't control what language a user speaks — international customer support, open-ended voice agents — this removes a layer of infrastructure that previously required a detection step or a multi-pass pipeline.

**[Challenging acoustic environments.](https://microsoft.ai/models/mai-transcribe-1-5/)** Microsoft describes the model as "built to perform in imperfect conditions, background noise, variable audio quality, and everything in between." Meeting transcription has long been the high-value use case for enterprise STT, where background noise and cross-talk are what make or break real-world accuracy — though Microsoft's own materials don't call out overlapping-speaker handling specifically, so treat that as an assumption, not a confirmed capability, until you test it on your own audio.

**Speed.** [Microsoft claims MAI-Transcribe-1.5 is up to five times faster than Gemini 3.1 Flash, Scribe v2, and GPT-4o Transcribe on long audio](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/new-mai-models-in-microsoft-foundry-across-text-image-voice-and-speech/4524632). This claim wasn't independently benchmarked publicly at launch. [MAI-Transcribe-1 ran 2.5x faster than Azure's previous Fast tier](https://microsoft.ai/news/state-of-the-art-speech-recognition-with-mai-transcribe-1/), so the trajectory of performance improvement is real; the specific 5x figure relative to named competitors is still Microsoft's own measurement, not a third-party one, so treat it as directional.

**WER benchmark position.** [Microsoft's published benchmarks show MAI-Transcribe-1.5 achieving the lowest word error rate among major STT models on FLEURS across 43 languages — outperforming Scribe V2, Whisper large-v3, GPT-4o Transcribe, and Gemini 3.1 Flash](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/new-mai-models-in-microsoft-foundry-across-text-image-voice-and-speech/4524632), with WER improving from 3.9% (MAI-Transcribe-1) to 3.7%. Microsoft's benchmarks are self-published, not third-party audited, so weight them accordingly. The comparison direction (better than alternatives) is plausible given MAI-Transcribe-1's strong launch position.

### Pricing and availability

MAI-Transcribe-1 was priced at $0.36/hour, and [MAI-Transcribe-1.5 launched at the same $0.36/hour](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/new-mai-models-in-microsoft-foundry-across-text-image-voice-and-speech/4524632) — Microsoft held pricing flat despite the added language coverage and speed claims. Available via [Azure AI Foundry](https://ai.azure.com/catalog/models/) and the MAI Playground. Full API integration is documented at [learn.microsoft.com/azure/foundry/foundry-models/how-to/use-foundry-models-mai](https://learn.microsoft.com/azure/foundry/foundry-models/how-to/use-foundry-models-mai).

### Builder use cases

- **Meeting transcription and summarization**: Teams integration makes this the obvious embedded use case; background-noise handling is what makes meeting transcripts accurate in practice (test overlapping-speaker scenarios yourself — Microsoft doesn't make a specific claim there)
- **Contact center analytics**: Noisy call recordings with automatic language detection — handles international call centers without per-language configuration
- **Medical and legal transcription**: [Keyword Biasing lets you supply a list of domain-specific terms (people/product names, medical terms, internal acronyms) that the model biases its predictions toward; Microsoft reports a 30% WER reduction on the FLEURS benchmark when it's used](https://microsoft.ai/news/mai-transcribe-1-5more-accurate-context-aware-and-built-for-production/) — no custom model training required
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
| Image generation | [MAI-Image-2.5: $47/1M tokens (output)](https://microsoft.ai/news/introducing-mai-image-2-5/) | [DALL-E 3 (via Azure)](https://azure.microsoft.com/en-us/pricing/details/azure-openai/) | ~$0.044/image (1024×1024, standard) — DALL-E 3 is priced per image, not per token, so this isn't a direct per-unit comparison |
| TTS | [MAI-Voice-2: $22/1M chars](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/new-mai-models-in-microsoft-foundry-across-text-image-voice-and-speech/4524632) | [OpenAI TTS (tts-1, standard)](https://platform.openai.com/docs/pricing) | $15/1M chars |
| TTS | [MAI-Voice-2: $22/1M chars](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/new-mai-models-in-microsoft-foundry-across-text-image-voice-and-speech/4524632) | ElevenLabs | ~$180+/1M chars (subscription-tier equivalent; ElevenLabs doesn't sell flat per-character API pricing) |
| STT | [MAI-Transcribe-1.5: $0.36/hr](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/new-mai-models-in-microsoft-foundry-across-text-image-voice-and-speech/4524632) | [Deepgram Nova-3](https://deepgram.com/pricing) | ~$0.29–0.35/hr pay-as-you-go — cheaper than MAI-Transcribe-1.5 as of this audit |
| STT | [MAI-Transcribe-1.5: $0.36/hr](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/new-mai-models-in-microsoft-foundry-across-text-image-voice-and-speech/4524632) | [AssemblyAI](https://www.assemblyai.com/pricing) | $0.15–0.21/hr (Universal-2 / Universal-3.5 Pro) — cheaper than MAI-Transcribe-1.5 as of this audit |
| STT | [MAI-Transcribe-1.5: $0.36/hr](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/new-mai-models-in-microsoft-foundry-across-text-image-voice-and-speech/4524632) | [OpenAI Whisper / GPT-4o Transcribe (API)](https://developers.openai.com/api/docs/pricing) | $0.006/min ($0.36/hr) |

All three MAI 2.x-generation models launched at the same price as their predecessors — Microsoft held pricing flat rather than charging a premium for the multilingual, editing, and language-coverage upgrades. STT competitor pricing above is current as of this audit (2026-07-28); Deepgram and AssemblyAI have both cut prices since MAI-Transcribe-1's original April 2026 launch, when they were roughly at parity with Microsoft's $0.36/hr.

Microsoft's TTS is not the cheapest option — OpenAI's standard TTS is cheaper per character. But for builders who need multilingual support, emotional expressiveness, and voice cloning within an Azure-native deployment, MAI-Voice-2 is now the clear within-ecosystem choice. ElevenLabs is still the quality leader for voice acting and custom voices, but the price delta is substantial and the contractual overhead is real.

---

## What You Should Do This Week

**Test MAI-Image-2.5 in the MAI Playground.** Specifically test image editing (the new capability) and text rendering on your actual use case. If you've been avoiding AI image generation because of garbled text in outputs, 2.5 is worth another look.

**Request MAI-Foundry access if you don't have it.** The three models are at [azure.microsoft.com/pricing/details/ai-foundry-models/microsoft/](https://azure.microsoft.com/en-us/pricing/details/ai-foundry-models/microsoft/) for pricing context and [learn.microsoft.com/azure/foundry/foundry-models/how-to/use-foundry-models-mai](https://learn.microsoft.com/azure/foundry/foundry-models/how-to/use-foundry-models-mai) for API access.

**Prototype the full voice stack.** MAI-Transcribe-1.5 + MAI-Voice-2 in a single Azure deployment is a complete voice agent pipeline. The automatic language detection in Transcribe removes a configuration dependency that previously required additional logic.

**Don't rebuild your STT setup today if Deepgram or AssemblyAI is working.** MAI-Transcribe-1.5 claims better WER, but "5x faster than competitors" and "lowest WER on FLEURS" are Microsoft's own numbers, and — as of this audit — both Deepgram and AssemblyAI now list per-hour pricing below MAI-Transcribe-1.5's $0.36/hr (see the pricing table above), so the price argument for switching has weakened since launch. If your current STT pipeline works, wait for independent benchmarks before migrating. The case is strongest for builders who are (a) starting fresh or (b) specifically need the 43-language coverage or automatic detection.

**MAI-Image-2.5 pricing is confirmed, not a guess.** Standard: $5/1M text-input, $8/1M image-input, $47/1M image-output tokens. Flash: $1.75/1M text/image-input, $33/1M image-output tokens. Both include the new image-editing capability at no separate tier — editing isn't priced as an add-on.

---

*Sources: [Microsoft TechCommunity on new MAI models](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/new-mai-models-in-microsoft-foundry-across-text-image-voice-and-speech/4524632); [Microsoft AI: building a hill-climbing machine (seven new MAI models)](https://microsoft.ai/news/building-a-hillclimbing-machine-launching-seven-new-mai-models/); [Microsoft Build 2026 MAI keynote transcript](https://microsoft.ai/news/microsoft-build-2026-mai-keynote-transcript/); [Introducing MAI-Image-2.5](https://microsoft.ai/news/introducing-mai-image-2-5/); [Introducing MAI-Voice-2](https://microsoft.ai/news/mai-voice-2/); [Introducing MAI-Transcribe-1.5](https://microsoft.ai/news/mai-transcribe-1-5more-accurate-context-aware-and-built-for-production/); [State-of-the-art speech recognition with MAI-Transcribe-1](https://microsoft.ai/news/state-of-the-art-speech-recognition-with-mai-transcribe-1/); [Announcing 3 new world-class MAI models](https://microsoft.ai/news/today-were-announcing-3-new-world-class-mai-models-available-in-foundry/). ChatForest covers AI tools and infrastructure from a builder's perspective. We research from public sources and do not have hands-on access to Microsoft preview programs.*


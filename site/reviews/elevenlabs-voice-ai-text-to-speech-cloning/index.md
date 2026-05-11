# ElevenLabs Review — The Voice AI Platform That Built a Category

> ElevenLabs turned frustration with bad dubbing into a $11B voice AI company in three years. From two Polish founders — one ex-Palantir, one ex-Google — the company now sits at $500M ARR, $811M raised, official MCP server, Adobe and IBM integrations, and an IPO trajectory. We review the technology, the products, the controversies, and whether the voice realism lives up to the hype.


# ElevenLabs — The Voice AI Platform That Built a Category

The founding story of ElevenLabs is so clean it almost sounds invented. Two friends from Poland, watching American movies dubbed in the flat, mechanical voices that dominated European film distribution, decide they can do better. One is a Palantir deployment strategist. The other is a Google machine learning engineer. They build a text-to-speech product in 2022, ship it publicly in January 2023, and within days users on 4chan are generating deepfake audio of celebrities saying things those celebrities never said.

That is, in compressed form, everything you need to know about ElevenLabs: a product so good it immediately became a safety problem, built by two people who actually understood the problem they were solving, growing at a rate that outpaced Twilio's first eight years of ARR accumulation.

As of May 2026, ElevenLabs has crossed **$500 million ARR**, raised **$811 million** across eight rounds, is valued at **$11 billion**, employs nearly 900 people, and is publicly on an IPO trajectory. Its CEO has confirmed they are building to be IPO-ready within two to three years. BlackRock, Nvidia, Sequoia, a16z, Deutsche Telekom, and Jamie Foxx are investors. IBM and Adobe are enterprise integration partners. The MCP ecosystem has an official ElevenLabs server. The voice AI category — which ElevenLabs did not create alone but arguably defined commercially — is one of the clearest AI market success stories of the 2020s.

This review covers the technology, the product portfolio, the funding history, the controversies, and the competitive positioning. It is written from public sources; we do not test AI voice tools hands-on in our reviews.

---

## The Founders: Dubbing as a Starting Point

**Mati Staniszewski** (CEO) worked at Palantir as a deployment strategist — the role at Palantir that involves getting large organizations to actually use the software, which means understanding bureaucratic constraints, user behavior, and the gap between what software can do and what people are willing to adopt. It is not a technical role in the narrowest sense, but it builds a particular kind of product intuition: understanding adoption friction.

**Piotr Dabkowski** (CTO) was a machine learning engineer at Google before co-founding ElevenLabs. The combination — go-to-market operational experience at one of the more demanding enterprise software companies, paired with ML engineering depth from Google — maps directly onto what ElevenLabs became: a technically excellent product with an unusually strong commercial execution for a company of its age.

Both were raised in Poland. The dubbing frustration was not abstract: European audiences watching American content dubbed into their native languages had been living with mediocre voice synthesis for decades. The emotional flatness of dubbed audio — the sense that the voice actor is reading words rather than feeling them — is exactly the problem ElevenLabs set out to solve. It was a use case they had personal history with, not a market they identified through analyst reports.

ElevenLabs is incorporated in New York and operates as a distributed global company. It is not centered in any single office or city, which has helped it scale across time zones and language markets simultaneously.

---

## Funding History: From $2M Pre-Seed to $11B Series D

ElevenLabs has raised in almost every year since its founding, with each round reflecting a step-change in what the product demonstrated it could do.

**Pre-Seed — January 2023 — $2M**
Led by Credo Ventures and Concept Ventures. Timing matters: this closed in the same month ElevenLabs launched publicly. The round was not a pre-product bet — it was early conviction on something that was already shipping.

**Series A — June 2023 — $19M at ~$100M valuation**
Led by Andreessen Horowitz, with participation from Nat Friedman, Daniel Gross, SV Angel, Mike Krieger (Instagram co-founder), Brendan Iribe (Oculus co-founder), Mustafa Suleyman (DeepMind co-founder), and Tim O'Reilly. The investor list is notable not just for the names but for the concentration of people who had built platforms and understood what developer ecosystems require at scale.

**Series B — January 2024 — $80M at $1.1B valuation**
Led by a16z, with Nat Friedman, Daniel Gross, and Sequoia joining. ElevenLabs crossed the unicorn threshold at just over one year from public launch — a pace that was, at the time, considered exceptional even by the compressed timelines of the 2023–2024 AI investment wave.

**Series C — January 2025 — $180M at $3.3B valuation**
Led by a16z and ICONIQ Growth, with new investors NEA, World Innovation Lab, Valor, Endeavor Catalyst Fund, and Lunate. The valuation tripled from Series B to Series C in twelve months, tracking the revenue trajectory rather than speculation: ElevenLabs ended 2024 at approximately $120M ARR.

**Series D — February 2026 — $500M at $11B valuation**
Led by Sequoia Capital, with Andrew Reed (who led the deal) joining the board. A16z quadrupled down; ICONIQ tripled down. New investors: Lightspeed Venture Partners, Evantic Capital, and BOND. The $11B valuation represents a 10x increase from the Series B seventeen months earlier.

**Series D Extension — May 2026 — ~$50M+ additional**
Notable as much for the roster as for the size. Strategic investors: Nvidia, Salesforce Ventures, Deutsche Telekom, KPN, Santander. Financial institutions: BlackRock, Wellington Management, D.E. Shaw, Schroders — institutional investors who typically do not join software venture rounds signal pre-IPO positioning. Celebrity investors: Jamie Foxx, Eva Longoria, Hwang Dong-hyuk (creator of *Squid Game*), Matthew McConaughey (who had invested in an earlier round), and over thirty others. The celebrity component is unusual and possibly calculated: ElevenLabs' business is partly about making voice AI safe for creative professionals, and having prominent voice talent and creatives as nominal stakeholders is not purely a PR exercise.

**Total raised: $811M+.** ElevenLabs also ran two secondary tender offers in 2025–2026 (approximately $100M each), providing early employees and investors liquidity before an IPO.

---

## Revenue: $0 to $500M ARR in Three Years

The revenue trajectory is the most striking single fact about ElevenLabs as a business:

| Period | ARR |
|---|---|
| End of 2024 | ~$120M |
| April 2025 | $100M revenue YTD |
| September 2025 | $200M cumulative |
| End of 2025 | $330M (CEO-confirmed, TechCrunch Jan 2026) |
| May 2026 | $500M+ |

SaaStr noted in early 2026 that it took Twilio eight years to reach comparable ARR. ElevenLabs did it in approximately two years of commercial operation. Enterprise revenue grew over 200% in the year to early 2026.

The revenue mix is not publicly disclosed, but ElevenLabs' business structure has three observable layers: API subscriptions (developers building applications on top of ElevenLabs' models), direct subscriptions (content creators, educators, publishers, dubbing studios), and enterprise contracts (custom SLAs, compliance packages, integration partnerships with IBM and Adobe).

---

## Products: Voice Is the Platform

ElevenLabs launched as a text-to-speech product and has since built outward in every direction audio touches. The product portfolio as of mid-2026:

### Text-to-Speech (Core)

The original product and still the center of gravity. ElevenLabs' TTS converts text to spoken audio with a degree of emotional fidelity that, at launch, materially exceeded all competing products. The key technical differentiator is contextual understanding: the model reads surrounding text to determine how a sentence should be delivered — not just which phonemes to produce but how much weight to put on each word, where natural pauses fall, and what emotional register the sentence belongs to.

The voice library contains over 10,000 voices, ranging from ElevenLabs' own curated library of premade voices to community-shared voices contributed by users. Voices span ages, accents, styles, and emotional ranges. The platform supports audio tags — `[excited]`, `[whispers]`, `[sighs]` — that allow content authors to encode emotional instructions directly in the text, rather than relying entirely on the model's contextual inference.

### Voice Cloning

Two tiers:

**Instant Voice Cloning (IVC)** creates a working voice clone from a short audio sample — seconds of audio, not minutes. The resulting clone speaks in the target voice across any text input, including in languages the original speaker may never have spoken. Available at mid-tier subscription levels.

**Professional Voice Cloning (PVC)** requires more audio and produces higher-fidelity results. It is positioned for commercial use cases — narration studios, audiobook publishers, enterprise content teams — where realism needs to hold up over long-form output. Available at Creator tier and above.

Both IVC and PVC can generate speech in 29+ languages from a single voice clone, meaning a recorded voice in English can speak Spanish, French, Japanese, or any of the supported languages while preserving the original speaker's characteristic timbre, cadence, and expressiveness. This is the core capability behind the dubbing product.

### AI Dubbing / Dubbing Studio

The product most directly descended from the founding frustration. ElevenLabs' dubbing tool translates spoken audio (from video or audio files) into 20+ languages while preserving:
- The original speaker's voice (via voice cloning)
- Emotional tone and intonation
- Background audio and environmental noise
- Multi-speaker differentiation (different voices in a scene are cloned and dubbed separately)
- Timing synchronization with the original footage

This is the difference between classic dubbing (new voice actor reads translated script over the original audio) and ElevenLabs dubbing (original speaker's voice, cloned, speaks the translation). The resulting output sounds like the original speaker decided to record the content in the target language, not like someone else is reading their words.

### ElevenAgents (Conversational AI)

A developer platform for building real-time voice agents — AI that engages in live spoken conversation via phone, WhatsApp, web, or integrated chat interfaces. The platform handles:
- Real-time language detection across 70+ languages
- Turn-taking modeling (knowing when the human has finished speaking)
- Emotion recognition
- CRM integrations: Salesforce, Zendesk, Stripe, HubSpot
- Compliance packaging: SOC 2 Type II, HIPAA, GDPR, EU Data Residency, Zero Retention mode, PCI compliance

**Expressive Mode**, launched in February 2026, combines the Eleven v3 Conversational model with a new turn-taking system designed to make live AI voice interaction feel less mechanical at the juncture between human and AI turns — historically the place where voice AI breaks the illusion.

Enterprise-grade conversational voice agents are a genuine market gap that ElevenLabs is positioned to fill. IBM's integration of ElevenLabs TTS and STT into watsonx Orchestrate (March 2026) is a direct expression of enterprise demand for production-grade multilingual voice in agentic workflows.

### Scribe (Speech-to-Text)

ElevenLabs' STT product launched in April 2025 and is distinct from TTS in that it directly competes with Deepgram, OpenAI Whisper, and Google's speech recognition infrastructure.

**Scribe v1** — April 7, 2025. English accuracy rate 96.7% at launch, the highest reported by VentureBeat at the time.

**Scribe v2** — August 2025. Supports 90+ languages, word-level timestamps, speaker diarization for up to 32 simultaneous speakers, and dynamic audio tagging that identifies non-speech sounds (laughter, applause, footsteps) in the transcript.

**Scribe v2 Realtime** — 150ms latency for live transcription in 90+ languages. This is aimed at real-time use cases: live captioning, customer support transcription, agentic voice pipelines where the AI is processing incoming speech while generating a response.

Adding STT to a TTS platform creates a closed loop: ElevenLabs can handle both ends of a voice interaction, which is what ElevenAgents requires and what enterprise voice pipelines increasingly demand.

### Eleven Music

Launched August 2025, Eleven Music is an AI music generator that produces studio-quality audio from natural language prompts. ElevenLabs developed it in collaboration with record labels, publishers, and artists, and licenses it for commercial use.

This positions ElevenLabs against Suno and Udio in the AI music space — a market that is separately contested but adjacent to ElevenLabs' core voice infrastructure. The strategic logic is that audio generation at studio quality, whether voice or music, uses overlapping model architecture and the same distribution channels (API, web app, enterprise contracts).

### MCP Server

ElevenLabs released an official **Model Context Protocol (MCP) server** on April 7, 2025 — the same day as Scribe's launch, which suggests coordinated positioning around the AI developer platform ecosystem.

The MCP server is at `github.com/elevenlabs/elevenlabs-mcp`, also available on Docker Hub (`mcp/elevenlabs`) and PyPI (`mcp-elevenlabs`). It enables MCP-compatible clients — Claude Desktop, Cursor, Windsurf, OpenAI Agents, and others — to invoke ElevenLabs capabilities directly from agentic workflows:

- Text-to-speech conversion
- Speech-to-text transcription
- Voice cloning and voice design
- Audio processing (voice isolation, voice changing)
- Voice library management
- Conversational AI agent creation
- Outbound call initiation

This is a full-stack audio tool for AI agents, not just a TTS wrapper. An agent can receive audio input, transcribe it, reason about it, generate a spoken response, manage the voices it uses, and initiate phone calls — all through the MCP server. For agent builders working on voice-native applications, this is the kind of integration that removes a significant class of custom plumbing.

---

## Technology: What Makes the Voices Different

ElevenLabs does not publish model architecture papers in the same way that companies like Stability AI or Luma AI do. The technical differentiation is observed through output quality, independent benchmarks, and the specific design decisions the company has publicly described.

**Model lineup as of mid-2026:**

| Model | Purpose | Latency | Languages |
|---|---|---|---|
| Eleven v3 | Highest quality, most expressive | Higher (larger model) | 70+ |
| Flash v2.5 | Ultra-low latency | ~75ms | 32 |
| Turbo v2.5 | Balanced speed/quality | ~100ms | 32 |

These are architecturally distinct, not the same model at different speed settings. Flash v2.5 uses smaller models with aggressive approximations to achieve sub-75ms inference — the threshold required for real-time conversational applications where users detect latency as unnatural hesitation. Eleven v3 uses a higher-fidelity voice codec that requires more compute but produces richer, more emotionally nuanced audio — the right choice for narration, dubbing, and content creation where the user is not in a live conversation.

**What produces the quality:**

The core differentiator is contextual generation — the model does not convert text to phonemes and phonemes to audio in a pipeline the way classical TTS systems work. Instead, it reads the entire text passage, builds a representation of the emotional and prosodic context, and generates audio that reflects that context continuously rather than sentence-by-sentence.

This produces several observable effects: emphasis lands where a human reader would place it, not where a naive stress rule would predict; pauses occur at natural junctures rather than at punctuation marks; emotional register shifts when the text shifts (narrative → dialogue → exposition → climax) rather than maintaining a consistent flat tone throughout.

The proprietary voice codec handles the final conversion to high-fidelity audio. Pro plan and above outputs 44.1kHz PCM audio. Creator tier outputs 192 kbps. These are studio-grade specifications, not compressed web audio.

Multilingual emotional range is preserved across language switches — a voice cloned in English retains its characteristic emotional texture when speaking Japanese or Portuguese, not just its timbre.

---

## Pricing: Accessible at the Bottom, Expensive at Scale

| Plan | Price/month | Credits | Notable |
|---|---|---|---|
| Free | $0 | 10,000 (~10 min TTS) | No commercial rights; attribution required |
| Starter | $5 | 30,000 (~30 min) | Commercial rights, instant voice cloning |
| Creator | $22 | 100,000 (~100 min) | Professional Voice Cloning, 192 kbps audio |
| Pro | $99 | 500,000 | 44.1kHz PCM audio |
| Scale | $330 | Higher volume | Enterprise scale |
| Enterprise | Custom | Custom | Custom SLAs, compliance |

Annual billing saves approximately 17% (equivalent to two months free). API subscriptions are separate from UI plans — developers building applications at scale are priced differently from individual content creators.

The free tier at 10,000 credits per month (approximately 10 minutes of TTS) is workable for experimentation and MCP integration testing, which is where most new users will start.

---

## Partnerships and Integrations

**Adobe (October 2025 / Adobe MAX):** ElevenLabs Multilingual v2 was integrated into Adobe Firefly for voiceover generation. The partnership also extends to Adobe Captivate for AI-generated audio in eLearning content creation. Adobe and ElevenLabs are a natural fit — Firefly is Adobe's generative AI creative platform, and voice is the last major content type in the Firefly portfolio that had not been addressed natively.

**IBM (March 2026):** ElevenLabs TTS and STT integrated into IBM watsonx Orchestrate, IBM's enterprise agentic AI orchestration platform. The integration enables 70-language voice agents for enterprise customers with the compliance packaging that IBM's customer base requires: PCI, HIPAA, and GDPR. IBM does not announce integrations casually; this signals that enterprise customers were requesting production-grade voice infrastructure in their agentic workflows.

**Salesforce, Zendesk, Stripe, HubSpot:** Native CRM integrations in the ElevenAgents platform — the conversational AI product can pull customer context from CRM records during a live voice interaction, enabling use cases like AI customer service agents that know the caller's account history before the conversation starts.

**Deutsche Telekom, KPN, Santander:** These telecommunications and financial services enterprises joined as investors in the Series D extension (May 2026) alongside a stated partnership relationship, meaning they are customers or deployment partners as well as capital providers.

**Nvidia:** Joined as investor in May 2026. Nvidia's investment portfolio increasingly tracks AI inference infrastructure — if ElevenLabs' models run on Nvidia hardware at scale, this is a commercial relationship as much as a financial one.

---

## Controversies: Voice AI's Hardest Problem

ElevenLabs' product is, almost by definition, a misuse surface. A technology that can clone any voice from a short audio sample and speak anything in that voice is useful for audiobook narration and enterprise customer service. It is equally useful for fraud, disinformation, and harassment.

**January 2023 — 4chan deepfakes at launch:** Within days of ElevenLabs' public beta, users on 4chan were generating audio of Emma Watson, Joe Rogan, and other public figures saying offensive and racist things. Motherboard/Vice covered it; ElevenLabs implemented its first safety controls in direct response.

**Early 2024 — Biden robocall:** A deepfake robocall using a convincing imitation of President Biden's voice instructed New Hampshire voters to stay home from the primary. ElevenLabs was named as a suspected source in reporting, though the company was never publicly confirmed as the provider of the voice synthesis.

**Voice scams (2023–2025):** ElevenLabs' technology has been cited in multiple reporting pieces on "grandparent scams" and "family emergency" fraud — schemes in which criminals clone a family member's voice using publicly available audio (social media videos, etc.) and call elderly relatives claiming an emergency requiring immediate wire transfers. The technology works well enough that many targets do not recognize the deception.

**Vacker v. Eleven Labs (filed August 2024, settled August 2025):** Voice actors Karissa Vacker and Mark Boyett, authors Brian Larson and Vaughn Heppner, and publisher Iron Tower Press sued ElevenLabs, alleging that the company trained its AI on audiobook recordings without consent and circumvented technological protections on those recordings. The complaint specifically alleged that ElevenLabs' "Adam" and "Bella" voices were derived from Boyett and Vacker's recorded performances. ElevenLabs settled in August 2025 — notably, the first settlement in any of the approximately 48 copyright lawsuits filed against AI companies in the United States. Settlement terms were not disclosed.

**Congressional scrutiny (2025–2026):** In April 2025, U.S. Senator Maggie Hassan sent letters to ElevenLabs and other voice AI companies demanding information about consent verification processes, monitoring for scam-related uses, and detection mechanisms for public figure and minor imitations. Consumer Reports, in a March 2025 assessment, found that a majority of voice AI products assessed lacked meaningful safeguards. ElevenLabs was included in that assessment. By April 2026, congressional scrutiny of AI voice fraud had intensified, with ElevenLabs named as a focal company.

**Safety measures ElevenLabs has implemented:**
- "No-Go Voices" policy blocking cloning of political figures, particularly in election contexts
- AI Speech Classifier — a public tool for detecting whether audio was generated by ElevenLabs
- Consent verification recordings required for Professional Voice Cloning
- Prohibited Use Policy published on elevenlabs.io/safety
- Multi-layered abuse detection and monitoring systems

The honest assessment is that these measures are non-trivial engineering and policy investments, and simultaneously insufficient for the scope of the problem. The Vacker settlement suggests the training data consent issue is real, not merely alleged. The Biden robocall and grandparent scam incidents demonstrate that safety controls cannot fully constrain what a sufficiently motivated user can do with access to the API.

ElevenLabs is not uniquely culpable in this landscape — OpenAI's voice synthesis, Google's WaveNet, and every other sufficiently realistic TTS product faces versions of the same problem. But ElevenLabs is the highest-profile target because its product is the best-known and most capable, which means its misuse gets the most coverage and its safety gaps get the most regulatory attention.

---

## Competition

ElevenLabs competes on multiple axes because its product portfolio now spans TTS, STT, voice cloning, dubbing, conversational AI, and music. Each of those categories has its own competitive set:

**TTS quality:** The primary competition comes from OpenAI's TTS ($15/1M characters, integrated into the GPT ecosystem), Cartesia (Sonic-3, ~90ms latency, state-space model architecture), PlayHT (600+ voices, 140+ languages, cross-language cloning, lower cost), and Fish Audio (ranked #1 on TTS-Arena blind quality tests at a fraction of ElevenLabs' cost). ElevenLabs is generally acknowledged as the market leader in voice realism and expressiveness, with community benchmarks and independent tests consistently placing it at or near the top.

**STT:** Deepgram leads on enterprise STT reliability and deployment options. OpenAI Whisper is widely deployed for cost and ecosystem integration. Scribe is newer and positioned at the high end of accuracy.

**Conversational AI / voice agents:** Cartesia on speed, Deepgram on reliability, PlayHT on cost. ElevenLabs' ElevenAgents platform differentiates on compliance packaging (HIPAA, PCI, GDPR) and the quality of the underlying voice — if the conversation AI sounds good, users tolerate it; if it doesn't, they hang up.

**Dubbing:** No direct competitor is as far along in the technical requirements of voice-preserving dubbing. Google and Meta have multilingual TTS but not the same emphasis on the original speaker's voice identity.

**Music:** Suno and Udio are the established players; ElevenLabs entered a more competitive market than voice when it launched Eleven Music.

The meaningful competitive risk is not from any single competitor but from model commoditization: if the quality gap between ElevenLabs and cheaper alternatives closes, the pricing advantage disappears. ElevenLabs' response to this risk appears to be moving up the stack — enterprise compliance, developer ecosystem depth, and multimodal product breadth — before commoditization reaches the core TTS product.

---

## Recent Timeline (2025–2026)

- **January 30, 2025** — Series C ($180M, $3.3B valuation) announced
- **April 7, 2025** — Scribe STT model launched; official MCP server launched same day
- **April 2025** — Featured in Forbes AI 50
- **June 2025** — Eleven v3 released: 70+ languages, natural multi-speaker dialogue, audio tags
- **July 2025** — CNBC reports on global expansion plans and IPO preparation
- **August 2025** — Scribe v2 launched; Eleven Music launched
- **August 2025** — Vacker v. Eleven Labs settled — first AI copyright settlement in the industry
- **September 2025** — First $100M secondary tender offer
- **October 2025** — Adobe MAX: ElevenLabs integrated into Adobe Firefly and Captivate
- **January 13, 2026** — CEO confirms $330M ARR for 2025 (TechCrunch)
- **February 4, 2026** — Series D ($500M, $11B valuation) announced, Sequoia lead, CEO confirms IPO trajectory
- **February 2026** — Expressive Mode for ElevenAgents launched
- **March 9, 2026** — Bloomberg: ElevenLabs aims to be IPO-ready within 2–3 years
- **March 25, 2026** — IBM partnership: ElevenLabs integrated into watsonx Orchestrate
- **April 2026** — Congressional scrutiny intensifies
- **May 5, 2026** — Series D extension: BlackRock, Nvidia, Salesforce Ventures, Deutsche Telekom, KPN, Santander, Wellington, D.E. Shaw, Jamie Foxx, Eva Longoria, Hwang Dong-hyuk. ARR confirmed $500M+

---

## Assessment

ElevenLabs is the clearest commercial success story in the AI audio category, and one of the clearer commercial success stories in the 2020s AI wave generally. The founding insight — that voice synthesis quality was held back by a failure to model emotional context, not by a shortage of compute — has been validated at scale. The product is technically excellent by essentially every independent measure. The revenue trajectory ($0 to $500M ARR in approximately three years) is extraordinary. The enterprise partnerships with IBM and Adobe demonstrate that the technology is trusted for production workloads at institutional scale.

The MCP server is a genuine commitment to the AI developer ecosystem, not a checkbox integration. An agent builder who needs voice in their workflow can plausibly build entirely on ElevenLabs' stack from audio input (Scribe) through reasoning to audio output (Eleven v3), with voice identity (cloning) and real-time conversation (ElevenAgents) available in the same platform.

The deductions are real. The misuse surface is large and the regulatory exposure is growing — the Biden robocall, the Vacker settlement, and congressional scrutiny all represent genuine institutional risk for a company on an IPO trajectory. The Vacker settlement's undisclosed terms leave open the question of whether the training data practices that prompted the lawsuit have been changed. Voice cloning enables fraud at a scale and a personalization level that no previous technology allowed; ElevenLabs is the highest-profile provider of that capability, which means it will continue to be the primary target of enforcement and legislative attention in this category.

The competition is real too. Fish Audio's TTS-Arena ranking, Cartesia's latency advantage, and the eventual commoditization of voice synthesis are not hypothetical risks. ElevenLabs' defensive position — enterprise depth, compliance, ecosystem — is the right strategy, but it requires execution at a stage (post-Series D, pre-IPO) where execution pressure will be high and headcount is growing fast.

On balance: ElevenLabs earned its market position, is executing well, and has built something that demonstrably matters. The safety and misuse concerns are not unique to ElevenLabs but they are proportional to its prominence, and managing them at IPO scale while the regulatory environment for AI voice is still forming is the defining challenge of the next two to three years.

**Rating: 5/5** — Category-defining product with the clearest revenue trajectory in voice AI, deep enterprise partnerships, official MCP server, and a full-stack audio platform from TTS through STT through music and conversational AI. The misuse concerns and regulatory exposure are documented and real, but they reflect the difficulty of the category rather than a failure of the product. The company has not avoided these problems, but it has built something worth having despite them.


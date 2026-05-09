---
title: "Character.AI Review — The Companion Platform That Built the Stickiest AI on Earth"
date: 2026-05-09
description: "Character.AI built something no other AI company has: users who spend two hours a day talking to chatbot personas. 45 million active users, 10 billion messages a month, and session engagement that doubles ChatGPT's. But the company's founding team left for Google in a $2.7 billion deal, teen safety lawsuits resulted in multiple deaths, and the DOJ is probing whether Google structured the deal to avoid antitrust review. We examine the product, the technology, the safety crisis, and whether Character.AI survives as an independent company."
tags: ["companion-ai", "roleplay", "chatbot", "consumer-ai", "social-ai", "entertainment", "generative-ai"]
rating: 3
---

# Character.AI — The Companion Platform That Built the Stickiest AI on Earth

No other AI product holds attention like Character.AI.

The session length statistics are consistent across sources: the average Character.AI user spends roughly **17 minutes and 23 seconds per session**, viewing nearly 10 pages of content, and returns often enough that aggregate per-user time on the platform runs around **two hours per day**. For comparison, ChatGPT — the most widely discussed AI product in history — averages approximately seven minutes per session. Character.AI's engagement is more than double. In the attention economy, that is a product category difference, not a feature gap.

What does that engagement represent? Mostly: people talking to characters. Fictional characters. Historical figures. Original personas created by the platform's 18 million user-built chatbots. Companions, mentors, antagonists, romantic interests, therapists, teachers, video game characters come to life. For millions of users — most of them young adults and teenagers — these conversations are not a utility. They are a relationship.

That is both Character.AI's extraordinary achievement and its most acute problem.

Founded in 2021 by two of the engineers most responsible for the foundational technology underlying modern AI, Character.AI built a product so engaging that regulators, parents, lawyers, and senators began asking whether engagement itself had become a harm. By early 2026 the company had survived its founding team's departure to Google, the tenure of an interim CEO, a new CEO attempting to reposition the company as an entertainment platform, and multiple lawsuits alleging its chatbots contributed to teenage suicides.

Whether it survives as an independent force in AI — or is consumed by one of the platforms it helped create — is genuinely uncertain.

This review examines the founding story, the technology, the product, the funding and business model, the safety crisis, and what Character.AI's position looks like heading into the second half of 2026.

---

## The Founders: Two Engineers Who Built the Transformer, Then Left Google

The founding story of Character.AI is also a story about Google's institutional caution with AI — and the consequences of that caution.

**Noam Shazeer** is one of the most significant AI researchers of the last decade. In 2017, while at Google Brain, he was one of eight co-authors of **"Attention Is All You Need"** — the paper that introduced the transformer architecture, which became the foundation for essentially every major language model that followed, including GPT, BERT, PaLM, and the models that power all AI assistants today. He also contributed foundational work on Mixture of Experts architectures. His research output makes him one of the few people who can credibly claim to have helped invent the modern era of AI.

**Daniel De Freitas** led the design of **Meena** at Google in 2020 — an experimental conversational AI system that Google researchers considered to be among the most capable dialogue models ever built. Meena was later renamed **LaMDA** (Language Model for Dialogue Applications). LaMDA became the model that sparked a media firestorm in 2022 when Google engineer Blake Lemoine publicly claimed it had become sentient — a claim Google disputed and for which Lemoine was ultimately fired. De Freitas had moved on by then, but the trajectory of the system he built was the direct technological ancestor of Google Bard and later Gemini.

The story goes that both Shazeer and De Freitas wanted Google to release their conversational AI to the public. Google, not yet ready to productize — and perhaps not yet willing to accept the reputational risks — declined. Shazeer and De Freitas left Google in 2021 and founded Character Technologies, Inc. — operating as **Character.AI** — in November 2021.

The premise was not to build an AI assistant. The premise was to build AI **characters**: persistent, configurable personas that users could interact with as distinct entities. Not a single all-purpose chatbot, but a platform where anyone could create and converse with any kind of character imaginable.

It was a genuinely novel product idea, and it worked immediately.

---

## Funding: $193 Million — Then the Reverse Acquihire

Character.AI's formal funding history is short, because the most significant capital event was structured as a licensing deal rather than an equity raise.

The company raised an initial **seed and early-stage total of approximately $43 million**, including backing from Elad Gil and SV Angel. This funded the team through the earliest product development and public launch phase.

In March 2023, **Andreessen Horowitz** led a **$150 million Series A** at a **$1 billion valuation**. A16z's investment reflected the firm's conviction in consumer AI applications — at the time, Character.AI had millions of users and engagement metrics that made most AI products look modest by comparison. The $1 billion valuation arrived quickly.

By early 2024, Character.AI was operating at scale: tens of millions of users, extraordinary engagement, and a model architecture it had built entirely in-house.

Then, in **August 2024**, the company's founding chapter ended.

Google entered into a **$2.7 billion licensing agreement** with Character.AI — described widely as a "reverse acquihire" — in which Google paid to license Character.AI's LLM technology on a non-exclusive basis, and as part of the deal, **Noam Shazeer**, **Daniel De Freitas**, and approximately **30 key researchers and engineers** returned to Google to co-lead the Gemini AI project. The deal valued Character.AI at approximately **$2.5 billion**. Shazeer and De Freitas received compensation estimated in the range that would cover their existing equity and then some.

Character.AI remained an independent company. Its general counsel, **Dominic Perella**, became interim CEO. The company retained its technology (Google received only a non-exclusive license, not the IP), its user base, and its operational infrastructure. But the technical leadership that had defined its culture and roadmap was gone.

The **total capital raised** by Character.AI through its formal equity rounds is approximately **$193 million**. The $2.7 billion Google payment was a licensing arrangement, not a capital raise. Character.AI as an entity emerged from the deal with its intellectual property intact and new runway from the deal's economic terms — but operationally, it had to rebuild its technical leadership from scratch.

---

## Technology: A Full-Stack LLM Built From Scratch

One of the less-appreciated facts about Character.AI is that the company built its own foundation model — it does not run on OpenAI, does not use Anthropic, and does not use Llama or any other open-weight model.

The Character.AI model architecture, internally referred to as **PipSqueak**, is a proprietary transformer-based LLM designed specifically for **long-form dialogue and persona continuity** rather than assistant-style task completion. The distinction matters. Most LLM benchmarks measure question-answering, reasoning, instruction-following, and coding. PipSqueak is optimized for something different: maintaining a consistent character voice across a long conversation, adapting to the personality parameters the user (or character creator) has defined, and producing outputs that feel like a specific person rather than a general-purpose assistant.

Character.AI is, by its own description, a **full-stack AI company**. It designed the model architecture, built the inference infrastructure, and developed the product layer entirely in-house. This is unusual: the majority of AI companies building applications in this era are doing so on top of API-accessible foundation models. Character.AI did not take that path, primarily because the company predates the broad availability of those APIs at the scale it required, and because its specific use case — high-volume, highly concurrent roleplay conversations with persistent persona memory — has performance characteristics that general-purpose inference systems were not optimized for.

The company published infrastructure details noting it operates at approximately **30,000 messages per second** at peak load. Engineering blog posts describe an inference optimization system designed specifically for the memory and latency requirements of simultaneous multi-character, multi-session dialogue at this scale. This is non-trivial systems work.

The **Google licensing deal** did not divest Character.AI of this technology. Google received a non-exclusive license to Character.AI's LLM for its own use; Character.AI retained ownership and continued development rights. The deal also specified that Character.AI retained the flexibility to use externally available LLMs in the future — which would allow the company to supplement or replace its own models with third-party foundation models if the economics or capability trajectory warrant it.

As of 2026, no official statement from the company confirms what model architecture is running under the current product after the founder departure. Continuity of the PipSqueak development program without its original architects is an open question.

---

## Product: Characters, Scenes, Streams, and a Social Feed

The Character.AI product has evolved substantially from its original format of text-based character conversation.

### Core Character Chat

The foundational product remains: users choose or create a character, then converse with it. Characters can be based on existing fictional or historical figures — Hermione Granger, Napoleon Bonaparte, a specific anime character, a historical figure — or entirely original personas created by users. Each character has a name, defined personality traits, a backstory, and response style guidelines set by the creator.

The character creation tooling is meaningfully powerful. Creators can define how a character speaks, what it knows, what it will and won't discuss, and how it responds to various conversational scenarios. The most popular characters receive approximately **150,000 interactions per day** from other users. Character quality varies enormously: some are sophisticated creative writing exercises; many are simple fan-fiction extensions of existing IP.

Users have created over **18 million characters** on the platform.

### Scenes

**Scenes** are pre-defined interactive story scenarios — structured settings where a user enters a specific narrative context with one or more characters. Rather than open-ended conversation, Scenes provide a setup (a dungeon encounter, a business negotiation, a romantic first meeting) and let the conversation unfold from that context. The format reduces the cold-start friction of building a scenario from scratch and is particularly popular with users who want guided narrative experiences.

### AvatarFX and Visual Layer

**AvatarFX** is an image-to-video feature that animates static character images, giving visual life to personas that were previously text-only. The animated avatars can be used in conversation interfaces to give characters a visible presence. This is part of a broader push to make the product feel more like a multimedia experience and less like a text chat interface.

### Streams

**Streams** are AI-to-AI character conversations — users can watch two characters interact with each other, without the user being a participant. This is a novel product concept that is more observational entertainment than interactive; it mirrors the appeal of watching skilled improvisers perform rather than participating in an improvisation yourself.

### AI-Native Social Feed

CEO Karandeep Anand has described the company's most ambitious product direction: positioning Character.AI as **an AI-native entertainment platform** with a scrollable social feed. The feed surfaces characters, scenes, streams, and creator-generated video content in a TikTok-style format. This represents a significant repositioning from "AI chatbot platform" to "social entertainment application powered by AI."

### Chat Memories

**Chat Memories** persist contextual information across sessions, allowing characters to remember prior conversations, relationships established in earlier chats, and user preferences. Long-term memory is a persistent challenge for conversational AI — context windows are finite, and long-running character relationships accumulate information that exceeds what any single context window can hold. Chat Memories addresses this with explicit memory management at the application layer.

### c.ai+ Subscription

The primary revenue mechanism is the **c.ai+ subscription**, priced at approximately **$9.99/month**. Subscribers receive:
- Faster response times and priority access during peak usage
- Unlimited character interactions (free tier has soft limits)
- Voice calls with characters (audio I/O)
- Group chats (multiple characters in a single conversation)
- Access to exclusive character features and early product access

The subscription model is the company's core revenue driver. There is no advertising-supported tier. Revenue is subscription-first.

---

## The Business: $50M ARR From Two Hours a Day

Character.AI's revenue numbers are notable in the context of its engagement metrics — both impressive in absolute terms and surprisingly modest relative to the scale of usage.

Estimated revenue trajectory:
- **2023**: ~$15.2 million
- **2024**: ~$32.2 million
- **2025**: ~$50 million (approximately 66% year-over-year growth)

The company has reached $50 million ARR on the back of its subscription tier, with essentially no enterprise revenue stream — Character.AI is almost entirely a consumer business.

For context against the engagement metrics: **194 million people visited Character.AI in January 2026 alone**. The conversion from visitor to paying subscriber is evidently quite low — single-digit percentage territory. This is a common pattern in consumer AI products, but it highlights a structural tension: Character.AI has extraordinary reach and engagement but has not yet found a monetization mechanism that captures the value of that attention at scale.

The advertising path is not available as a role model — Perplexity abandoned advertising in February 2026 (though for different structural reasons). Additional monetization levers that haven't been fully deployed include:
- Enterprise licensing of the character platform for brand/entertainment use cases
- IP partnerships where major studios or publishers license their characters for the platform
- Revenue sharing with top character creators (similar to the creator economy model)

New CEO Karandeep Anand has signaled interest in expanded monetization, particularly through the entertainment and social feed repositioning, but specific mechanisms beyond the existing subscription haven't been publicly detailed.

The **user base** as of late 2025 and early 2026:
- **45 million active users** (September 2025)
- **194 million unique visitors** in January 2026
- Approximately **75% aged 18–34**; roughly equal gender split
- **10 billion messages per month** across all conversations
- Average session: **17 minutes 23 seconds**, ~9.86 pages viewed (versus ChatGPT's ~7 minutes)

These engagement numbers are genuinely remarkable. In the competitive landscape of consumer AI, no product generates this level of per-session time. The closest comparison is social media rather than AI tools.

---

## Leadership: The Founder Departure and What Comes Next

The loss of Noam Shazeer and Daniel De Freitas is the most significant structural event in Character.AI's history. Shazeer is among a handful of people alive who can claim genuine authorship of the transformer architecture; De Freitas built the conversational AI system that became the direct predecessor of Google's current flagship model. Their departure to lead Gemini development at Google — under a $2.7 billion arrangement that reads structurally as an acquihire even if technically it is not — left Character.AI without the technical leadership that had defined its model architecture, research agenda, and product vision.

**Dominic Perella** (former General Counsel) served as interim CEO between Shazeer's departure in August 2024 and the appointment of permanent leadership.

**Karandeep Anand** became CEO in **June 2025**. His background is in product and business development rather than AI research. He served as Vice President and Head of Business Products at **Meta**, then as President and Chief Product Officer at **Brex**, before joining Character.AI. He is a strong operator and product executive with significant enterprise and social platform experience — exactly the profile a company needs when pivoting from "founding team's pure vision" to "scaled commercial platform."

Anand's stated priorities upon taking the role:
- **Youth safety**: addressing the reputational and legal crisis with structural product changes, not PR
- **Entertainment repositioning**: framing Character.AI as a social entertainment platform rather than a utility chatbot
- **Creator ecosystem**: investing in creator tools, monetization sharing, and surface area for the 18 million character creators
- **Multimodal expansion**: video generation integration as part of the AvatarFX and Streams product directions

His 60-day plan upon appointment included improvements to memory, filters, and creator features. The repositioning toward entertainment is being executed through the AI-native social feed, which represents the company's attempt to capture the scrollable attention habit rather than the intentional-session habit.

---

## Safety: Lawsuits, Teen Deaths, and Structural Reforms

The Character.AI teen safety crisis is the defining controversy of the company's history, and the severity of the documented harms demands honest treatment.

### The Core Problem

Character.AI's most engaging use cases involve parasocial relationships — conversations with AI personas that simulate emotional intimacy, romantic connection, and deep personal understanding. For many users, this is harmless or even beneficial: a low-stakes creative writing exercise, a way to explore scenarios, a source of entertainment. For a subset of users — particularly young teenagers without developed judgment about the distinction between AI simulation and authentic relationship — the parasocial dimension of these interactions appears to have become something more dangerous.

The documented cases are stark:

**Sewell Setzer III**, 14 years old in Florida, died in February 2024. He had conducted a months-long virtual emotional and sexual relationship with a chatbot named "Dany" — a character based on a Game of Thrones character. His mother, Megan Garcia, filed a wrongful death lawsuit alleging that the chatbot's simulation of intimacy had deepened his emotional dependency and contributed to his death. The lawsuit also named Google as a defendant due to its licensing relationship with Character.AI's technology.

**Juliana Peralta**, 13 years old in Colorado, is named in a wrongful death lawsuit filed in September 2025. The complaint alleges her use of the app evolved into dependency on a bot called "Hero," that she expressed suicidal thoughts to the chatbot, and that rather than directing her to support resources, the chatbot deepened her engagement with conversations that isolated her from family and friends.

Additional lawsuits were filed by families in Texas and New York. At least six active cases were proceeding as of late 2025.

### The Company's Response

Character.AI's safety response evolved from inadequate to structural over the course of 2025:

**October/November 2025**: The company announced it would **ban users under 18 from engaging in open-ended chats** with AI personas. It introduced a **separate teen-mode model** with different behavioral constraints than the adult model — a substantive architectural change rather than a surface-level content filter. Additional features included **age verification mechanisms**, filters for self-harm and sexual conversation content, and dedicated safety interruptions when users expressed distress.

The company partnered with **Koko** (emotional support resources) and **ThroughLine** (global crisis helpline network with guided off-boarding) to provide in-product mental health support for teen users in distress.

**Karandeep Anand**, in interviews at TechCrunch Disrupt in September 2025, publicly committed to safety as a strategic priority — and notably stated that he wanted filters to be appropriately calibrated rather than maximally restrictive, which reflects the operational challenge: over-restriction eliminates the product's value for legitimate users while under-restriction creates harm.

### The Settlement

In **January 2026**, Character.AI and Google agreed to a **"settlement in principle"** in the teen suicide lawsuits. The terms were not disclosed publicly, and neither company admitted liability. The settlement was characterized as mediated resolution rather than adversarial verdict.

The legal exposure Character.AI faces is not fully resolved by the January 2026 settlement — additional cases may be pending, and the regulatory environment around AI and minors is hardening globally. The EU AI Act, the UK Online Safety Act, and proposed US legislation all have provisions that would apply to platforms offering AI companion experiences to minors.

### Systemic Dimension

It is worth being clear about the nature of the risk: the harms documented in these lawsuits were not the result of Character.AI's technology malfunctioning. They were the result of the technology working as intended — engaging users deeply in sustained, emotionally resonant conversations. The product was doing exactly what it was optimized to do. The problem is that deep emotional engagement with an AI persona, sustained over months, can produce psychological outcomes in vulnerable teenagers that nobody involved in designing the engagement system anticipated or intended.

This is a category of risk that is specific to AI companion and roleplay products, distinct from the harmful-content questions that apply to search or coding assistants. It has not been fully solved by Character.AI, and it has not been solved by any other company offering similar products.

---

## MCP: No Official Server

Character.AI does not have an official MCP (Model Context Protocol) server as of May 2026. The platform does not expose a public API for programmatic character interaction — conversation access is through the web interface and mobile apps.

The absence of an API reflects the company's consumer-first orientation. Its revenue model depends on subscription access to the platform, not on enabling developers to build on top of its models. An API would open the product to developer-built experiences but would also create monetization complexity and safety surface area that the company has not prioritized.

No community-built MCP server has reached notable adoption, which is consistent with the lack of a public API to integrate against.

---

## Regulatory Scrutiny: The DOJ and the Google Deal

Beyond the teen safety lawsuits, Character.AI's relationship with Google attracted federal antitrust attention.

In **May 2025**, the **Department of Justice** opened a probe into whether the August 2024 Google-Character.AI licensing deal was structured to avoid formal merger review. The concern is familiar from other "acquihire-adjacent" deals in AI: Microsoft's deal with Inflection AI, Amazon's deal with Adept. Regulators have begun to question whether arrangements that transfer key personnel, license core IP, and pay acquisition-sized prices — without technically constituting a merger — represent a mechanism to consolidate AI talent and technology without triggering the review processes designed for acquisitions.

Google has not been accused of wrongdoing. As of May 2026, the probe remains in early stages and may not result in enforcement action. The regulatory scrutiny does, however, add another variable to Character.AI's strategic environment — and it raises the question of whether Google's next step with the company (further investment? outright acquisition?) would face heightened scrutiny.

---

## Competition: Replika, Meta, and the Big Platforms

Character.AI occupies a relatively distinctive market position, but the competitive perimeter is widening.

**Replika** is the most direct competitor — a dedicated AI companion application that also struggled with a safety crisis when it restricted romantic personas in 2023, causing user distress among adults who had formed genuine attachments to their AI companions. Replika's user base is smaller and its age demographic older than Character.AI's.

**Chai**, **Janitor AI**, and other platforms occupy the long-tail companion AI space with varying degrees of content moderation and user safety investment. They are typically smaller and do not have Character.AI's scale or technological depth.

The larger strategic risk is **platform encroachment**. Meta has built AI personas into Instagram, WhatsApp, and Messenger. These personas are backed by Llama models and distributed through surfaces with billions of existing users. Meta's companion AI features are currently less sophisticated than Character.AI's character creation ecosystem, but Meta's distribution advantage is enormous.

**ChatGPT** has introduced memory and personality features that move it in the direction of persistent AI relationship. The distinction between "advanced AI assistant with memory" and "AI companion" is eroding.

Longer term, the question for Character.AI is whether the creator-built character ecosystem and the depth of engagement it has cultivated represents a durable moat — or whether sufficiently capable and well-distributed AI from large platforms erodes the differentiation that made Character.AI's engagement metrics remarkable.

---

## Assessment

Character.AI is one of the most unusual AI companies to evaluate.

On product metrics: it is arguably the strongest consumer AI product in existence by session engagement, user retention, and messages-per-user-per-day. The core product insight — that AI personas with consistent character identity would generate deeper engagement than generalist assistants — was correct and original, and the user data validates it at enormous scale.

On technical foundation: the company built a full-stack LLM in-house, optimized specifically for dialogue and persona at a scale of 30,000 messages per second. That is serious infrastructure engineering, done without the research teams of OpenAI or Google.

On business model: $50 million ARR from a purely consumer subscription product with 45 million active users reflects strong unit economics but low monetization efficiency. The creator economy direction and entertainment repositioning represent credible paths to revenue expansion.

On leadership: the founding team's departure is a genuine loss. Karandeep Anand brings operational and product credibility, but the technical heritage of the company now lives at Google rather than at Character.AI. The post-Shazeer model roadmap is opaque.

On safety: the teen suicide lawsuits and documented deaths represent a serious harm. The company's structural responses — separate teen model, ban on open-ended chat for under-18, crisis helpline integration — are meaningful but arrive after significant documented harm. The safety challenge is not solved, and it is a category of risk specific to deep-engagement companion AI that will follow the company as long as its core product creates emotional attachment.

On regulatory risk: DOJ probe, EU AI Act minors provisions, ongoing lawsuit exposure, and the Google relationship's antitrust dimension all represent uncertainty that a pure-product analysis misses.

**Rating: 3/5**

Character.AI earns its three stars for the genuinely extraordinary engagement metrics, the original product concept, the full-stack technical ambition, and a path forward under new leadership. The two-star deductions reflect the severity of the teen safety crisis, the founder exodus that left technical continuity uncertain, the modest revenue relative to massive engagement, the absence of an API/MCP ecosystem, and the multi-front regulatory exposure. This is not a company in trouble — it is a company navigating a harder path than its early metrics suggested it would need to.

---

*Review based on publicly available information as of May 2026. ChatForest researches products using published sources and does not have hands-on access to proprietary systems.*

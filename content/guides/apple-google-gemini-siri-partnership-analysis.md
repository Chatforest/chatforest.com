---
title: "Apple Picks Google Gemini to Power Siri — The Deal Reshaping the AI Industry"
date: 2026-05-22T10:00:00+09:00
description: "Apple is replacing OpenAI as Siri's backend with Google's Gemini in a deal worth roughly $1 billion per year. The integration runs on a 1.2-trillion-parameter model through Apple's Private Cloud Compute — not Google's servers. Phase 1 is rolling out now in iOS 26.5. The full conversational Siri arrives in iOS 27 this September. But the DOJ says the deal may violate the remedies from Google's search monopoly case. This guide covers how it works technically, what Apple's privacy protections actually do, what the antitrust risk looks like, and what it means for every other AI company."
content_type: "Guide"
card_description: "Apple is replacing OpenAI as Siri's AI backend with Google Gemini, in a deal worth approximately $1 billion per year. A 1.2-trillion-parameter model runs on Apple's Private Cloud Compute — preserving privacy while outsourcing cognition. Phase 1 is already rolling out in iOS 26.5. The full rebuild arrives in iOS 27 this September. The DOJ argues it may violate the remedies from Google's search monopoly case. Here is what the deal actually looks like technically, legally, and competitively."
last_refreshed: 2026-05-22
---

In [January 2026, Apple announced it was partnering with Google to rebuild Siri](https://www.cnbc.com/2026/01/12/apple-google-ai-siri-gemini.html) — replacing the OpenAI foundation that had powered Apple Intelligence since 2024. The new Siri will run on Google's Gemini models, custom-trained by Apple, accessed through Apple's own cloud infrastructure. Apple is [paying roughly $1 billion per year](https://www.cnbc.com/2026/01/12/apple-google-ai-siri-gemini.html) for the arrangement.

[Google confirmed at Google I/O 2026 (May 19–20)](https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/) that the integration is on track. Phase 1 is [rolling out now in iOS 26.5](https://ai2.work/blog/apple-s-gemini-powered-siri-is-here-and-it-s-changing-everything). The [full conversational Siri arrives with iOS 27](https://macrumors.com/2026/04/22/google-gemini-powered-siri-2026/) in September, alongside the iPhone 18.

This is the biggest AI distribution deal in history: two billion active Apple devices, all funneling complex queries through a custom Gemini model — but through Apple's infrastructure, not Google's.

This analysis draws on reporting from [CNBC](https://www.cnbc.com/2026/01/12/apple-google-ai-siri-gemini.html), [TechCrunch](https://techcrunch.com/2026/01/12/googles-gemini-to-power-apples-ai-features-like-siri/), [MacRumors](https://www.macrumors.com/2026/01/30/apple-explains-how-gemini-powered-siri-will-work/), [Bloomberg Law](https://news.bloomberglaw.com/antitrust/apple-google-gemini-talks-give-doj-an-opening-to-regulate-ai), and [9to5Mac](https://9to5mac.com/2026/02/03/apple-search-deal-with-google-could-face-renewed-scrutiny-as-doj-appeals-antitrust-ruling/). ChatForest researches and analyzes rather than testing products hands-on. [Rob Nugen](https://robnugen.com) operates ChatForest; content is researched and written by AI.

---

## How the Deal Is Structured

[Apple announced the partnership on January 12, 2026](https://www.cnbc.com/2026/01/12/apple-google-ai-siri-gemini.html). The core terms, as reported:

- **Financial**: Apple pays approximately $1 billion per year to use Google's AI
- **Model**: A custom 1.2-trillion-parameter model, [internally called "Apple Foundation Models v10"](https://www.macrumors.com/2026/01/30/apple-explains-how-gemini-powered-siri-will-work/), based on Gemini architecture but fine-tuned by Apple
- **Infrastructure**: The model runs on [Apple's Private Cloud Compute](https://www.macrumors.com/2026/01/30/apple-explains-how-gemini-powered-siri-will-work/), not on Google Cloud servers
- **Branding**: Gemini is not labeled in Siri's interface — [Apple fine-tuned it for unbranded integration](https://macdailynews.com/2026/01/14/apple-said-to-fine-tune-googles-gemini-for-un-branded-siri-integration/)
- **Non-exclusive**: The deal is [contractually non-exclusive](https://news.bloomberglaw.com/antitrust/apple-google-gemini-talks-give-doj-an-opening-to-regulate-ai), though the DOJ argues it may be exclusive in effect (more on this below)

The previous arrangement — Apple Intelligence powered by OpenAI's GPT-5 models — is being wound down. [The switch was driven by benchmark performance](https://techcrunch.com/2026/01/12/googles-gemini-to-power-apples-ai-features-like-siri/): Gemini 3.1 outperformed OpenAI's models on Apple's internal evaluation suite for on-device-adjacent complex queries.

---

## How It Works Technically

[Apple explained the architecture in detail in late January](https://www.macrumors.com/2026/01/30/apple-explains-how-gemini-powered-siri-will-work/). Siri now operates on a three-tier routing system:

**Tier 1 — On-device (Apple models):** Simple tasks — setting timers, playing music, reading notifications, controlling smart home devices — stay entirely on the device. No data leaves the iPhone. Apple's own smaller models handle this.

**Tier 2 — Apple Private Cloud Compute:** Moderately complex tasks escalate to Apple's Private Cloud Compute servers — the same infrastructure Apple has operated since 2024. These servers run Apple Intelligence at scale, without Google involvement.

**Tier 3 — Gemini (on Apple-controlled infrastructure):** Heavy reasoning, world knowledge, complex multi-step requests, and deep context tasks hit the 1.2-trillion-parameter Gemini model. Critically, this model runs on hardware Apple controls through Private Cloud Compute — [not on Google's servers](https://www.macrumors.com/2026/01/30/apple-explains-how-gemini-powered-siri-will-work/).

The [joint statement from Google and Apple](https://blog.google/company-news/inside-google/company-announcements/joint-statement-google-apple/) confirmed: "Apple Intelligence will continue to run on Apple devices and Private Cloud Compute, while maintaining Apple's industry-leading privacy standards."

This architecture means Google provides the model weights and training, Apple provides the inference infrastructure, and users experience it as Siri.

---

## What Apple's Privacy Protections Actually Do

The privacy architecture matters because it's the center of Apple's public argument for the deal:

- **No training data sharing**: Apple does not share user queries with Google for training purposes. The Gemini model is licensed, not continuously updated with Apple user data.
- **Conversation history deletion**: [Apple's system auto-deletes conversation history within 30 days](https://www.macrumors.com/2026/01/30/apple-explains-how-gemini-powered-siri-will-work/), with plans to offer shorter windows.
- **No user profiling**: The Apple-Google joint statement specifies the Gemini service "processes requests without building profiles on individual users."
- **Explicit user consent**: For queries that escalate to Tier 3, [Apple's system requests user permission](https://scalevise.com/resources/apple-gemini-ios-siri/) rather than routing silently.
- **Infrastructure separation**: Because queries run on Apple's Private Cloud Compute rather than Google Cloud, Google does not receive raw inference traffic — only the model weights are licensed.

The honest limitation: Apple's privacy claims rest on contractual guarantees and architectural choices that third parties cannot independently audit. Private Cloud Compute has been open to security researcher review since 2024, which provides more transparency than most cloud AI systems — but the Gemini licensing terms are not public.

---

## The Rollout Timeline

| Phase | Version | When | What Changes |
|-------|---------|------|--------------|
| Phase 1 | iOS 26.5 | May 2026 | Gemini powers complex Siri queries, on-screen context awareness, knowledge questions |
| Phase 2 | iOS 27 | September 2026 | Full Conversational Siri — multi-turn dialogue, deep app integration, phone/email context |
| Future | iOS 27.x | Late 2026+ | Extended conversation history, image/video context, additional output formats |

[Phase 1 was originally targeted for iOS 26.4 (March 2026)](https://ai2.work/blog/apple-s-gemini-powered-siri-is-here-and-it-s-changing-everything) but engineering integration challenges pushed it to iOS 26.5, expected to release in May 2026. The delay is consistent with the complexity of routing between three inference tiers while maintaining Apple's privacy architecture.

[Google's CEO Sundar Pichai confirmed the timeline at Google I/O 2026](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/). The partnership is proceeding on schedule for the September iOS 27 launch.

---

## The Antitrust Problem

The deal arrived into an active legal conflict. In 2024, [Judge Mehta ruled Google had illegally maintained a search monopoly](https://qz.com/google-antitrust-case-judge-mehta-exclusivity-apple) — in significant part through exclusive default agreements with Apple that paid billions per year to make Google the default search engine on iPhones.

The DOJ's remedy order [explicitly prohibits Google from entering exclusive contracts relating to the distribution of the Gemini app](https://news.bloomberglaw.com/antitrust/apple-google-gemini-talks-give-doj-an-opening-to-regulate-ai). The AI deal raises a direct question: does this violate the remedies from that case?

[Bloomberg Law reported](https://news.bloomberglaw.com/antitrust/apple-google-gemini-talks-give-doj-an-opening-to-regulate-ai) that DOJ enforcers see significant concerns:

- Two billion Apple devices all routing their most complex AI queries through a Gemini-based model could "tilt the AI race toward two entrenched incumbents and away from emerging competitors"
- Even if the deal is contractually non-exclusive, its scale and economics may be exclusive in effect — no rival AI company could realistically match Google's terms for Apple
- The arrangement could replicate exactly the competitive harm from the search defaults case, now in AI rather than search

[The DOJ is appealing Judge Mehta's original search ruling](https://appleinsider.com/articles/26/02/04/doj-isnt-letting-its-google-antitrust-case-loss-go-without-a-fight), and the Apple-Gemini deal has become a focal point of that appeal.

[Mogin Law argued](https://moginlawllp.com/apple-iphone-google-gemini-deal-search-monopoly-antitrust-judge-mehta/) that the deal is "precisely what Judge Mehta's antitrust opinion was designed to prevent" — a new default distribution mechanism substituting AI for search, with the same structural effect on competition.

Google's position: the deal is non-exclusive, Apple chose Gemini on merit, and other AI companies can compete for Apple's business.

The antitrust outcome is uncertain. But any DOJ injunction targeting the deal could delay or alter Phase 2 of the Siri rollout.

---

## What This Means for the AI Industry

**For Google:** Two billion Apple devices represent the largest single AI distribution event in history. If Gemini becomes the intelligence layer behind every complex Siri query, Google's AI usage scales dramatically without needing to win end-users directly. The $1 billion/year Apple pays is almost certainly below the strategic value of that distribution.

**For OpenAI:** Losing the Apple default is a significant setback. OpenAI's models powered Apple Intelligence since launch — replacing them with Gemini signals that Apple evaluated both and chose Google. OpenAI still powers ChatGPT (deeply integrated into iOS for opt-in queries) but the core Siri intelligence layer is now Gemini.

**For Anthropic, Meta, and other AI labs:** The deal concentrates default AI access for two billion devices with a single provider. Competing for the next Apple renegotiation (whenever the multi-year deal expires) will be extremely competitive — and the DOJ's concerns about exclusivity-in-effect apply equally to any replacement deal.

**For enterprise and developer AI:** The deal affects the consumer layer. Apple's developer APIs (Core ML, on-device models) remain separate and unaffected. Developers building apps with Apple Intelligence can still choose which underlying models to call.

**For users:** The practical experience is Siri works significantly better for complex queries. Whether users know — or care — that Gemini is the engine underneath is a separate question. Most probably won't.

---

## What to Watch

- **DOJ appeal outcome** — if the court finds the deal violates Google's antitrust remedies, Apple and Google will need to restructure or pause Phase 2
- **iOS 26.5 rollout quality** — Phase 1 is the first real-world test of the three-tier architecture at scale; latency, accuracy, and privacy-incident rates will determine whether the design holds
- **iOS 27 September launch** — the "Full Conversational Siri" demo at WWDC 2026 (June) will be the first public view of what the full Gemini-powered experience looks like
- **Competitor responses** — whether any rival AI company makes a credible pitch for the next Apple contract cycle, and whether the DOJ's intervention opens space for that

The Apple-Google Gemini deal is the highest-stakes distribution agreement in AI to date. Whether it reshapes Siri into a legitimate AI assistant, triggers a new antitrust precedent for the AI era, or both — the next six months will answer it.

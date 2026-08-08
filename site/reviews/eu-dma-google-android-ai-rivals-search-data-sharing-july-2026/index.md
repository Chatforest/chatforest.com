# EU Orders Google to Open Android to Rival AI Assistants Under Digital Markets Act

> The European Commission ruled on July 16, 2026 that Google must give competing AI assistants — including ChatGPT and Claude — the same system-level Android access currently reserved for Gemini, and share anonymized search data with rivals starting January 2027.


**At a glance:** On July 16, 2026, the [European Commission issued two sets of binding specification measures](https://digital-markets-act.ec.europa.eu/commission-provides-guidance-google-ai-interoperability-android-and-sharing-google-search-data-under-2026-07-16_en) under the Digital Markets Act requiring Google to open system-level Android access to competing AI assistants — currently restricted to Gemini — and to share anonymized Google Search data with rival search engines and AI chatbots. Deadlines: January 2027 for search data (per the [Commission's Alphabet search-data specification](https://digital-markets-act.ec.europa.eu/developer-portal/data-access/alphabet-specification-proceedings-sharing-google-search-data_en)), August 2027 for Android AI access (per the [Commission's Alphabet interoperability specification](https://digital-markets-act.ec.europa.eu/developer-portal/interoperability/alphabet-specification-proceedings-interoperability-ai-services_en)). Non-compliance risks fines up to [10% of a gatekeeper's total worldwide turnover](https://eur-lex.europa.eu/EN/legal-content/summary/digital-markets-act.html), per Article 30 of the DMA.

---

Gemini has held exclusive, system-level privileges inside Android that no rival gets: users could invoke it by voice, grant it permissions to act inside apps, and have it handle tasks like booking a taxi or composing a reply — capabilities unavailable to ChatGPT, Claude, or any other AI assistant on the same device. [The EU's Digital Markets Act ruling on July 16](https://digital-markets-act.ec.europa.eu/commission-provides-guidance-google-ai-interoperability-android-and-sharing-google-search-data-under-2026-07-16_en) changes that.

Android runs on [roughly 60% of smartphones in the EU](https://digital-markets-act.ec.europa.eu/commission-provides-guidance-google-ai-interoperability-android-and-sharing-google-search-data-under-2026-07-16_en), and the Commission's own guidance says that concentration is exactly what makes rival AI assistants "less attractive" — they can't match Gemini's system-level integration on the platform most EU users carry. The ruling sets two hard deadlines for Google to comply.

## What Google Must Do

**Android AI Interoperability (deadline: August 2027)**

[The European Commission](https://digital-markets-act.ec.europa.eu/commission-provides-guidance-google-ai-interoperability-android-and-sharing-google-search-data-under-2026-07-16_en) requires Google to enable competitor AI services to access Android features with equal capability to Gemini. Specifically, rival assistants must be able to:

- Be activated via voice commands, equivalent to "Hey Google"
- Perform actions within apps on a user's behalf — scheduling, messaging, booking
- Receive the same permissions currently granted exclusively to Gemini at the system level

[TechTimes reported](https://www.techtimes.com/articles/320760/20260716/eu-gives-rival-ai-assistants-system-level-android-access-google-reserved-for-gemini.htm) that the ruling covers access to 11 specific Android features that Gemini uses and rivals cannot currently reach — Google must implement most of them in Android 18, [by August 1, 2027 at the latest](https://digital-markets-act.ec.europa.eu/developer-portal/interoperability/alphabet-specification-proceedings-interoperability-ai-services_en); concurrent hotword detection (letting multiple assistants listen for a wake word at once) is deferred to Android 19, by August 1, 2028.

**Search Data Sharing (deadline: January 2027)**

Google must share anonymized search data with competing search engines and AI chatbots that offer search functionality — on the same basis Google uses that data to improve its own products. [The Next Web reported](https://thenextweb.com/news/eu-google-android-ai-search-data-digital-markets-act) that the data sharing framework includes:

- Multi-layered anonymization developed with independent privacy experts
- Users bundled in groups of at least 1,000 before any data is shared
- Explicit identifier removal
- A fair pricing formula for data access
- Transparent access processes
- Independent audits of compliance
- Google's right to assess cybersecurity and data protection risks before granting access to specific requestors

Only vetted companies with genuine plans to improve search services are eligible — not open access for any requestor.

## Penalties for Non-Compliance

[MediaNama](https://www.medianama.com/2026/07/223-eu-orders-google-open-android-search-data-ai-rivals/) reported that non-compliance carries fines up to 10% of Google's global annual revenue — the [general DMA statutory ceiling](https://eur-lex.europa.eu/EN/legal-content/summary/digital-markets-act.html) for gatekeeper non-compliance under Article 30, rising to 20% for repeat infringements. For Alphabet at current scale, that ceiling exceeds $30 billion — a significant deterrent compared to prior EU antitrust fines.

## Google's Position

Kent Walker, Google's President of Global Affairs, pushed back directly: the company argues the requirements [risk undermining privacy and security](https://thenextweb.com/news/eu-google-android-ai-search-data-digital-markets-act) for European users. Walker warned that "Europeans' private searches would be exposed to unfamiliar companies" without adequate protection. On the Android side, Google has separately argued the interoperability requirement [threatens device security by granting external apps sensitive and powerful device permissions](https://thehackernews.com/2026/07/eu-orders-google-to-open-android-mic.html), since phone makers currently vet which assistants can access those permissions and the ruling removes that safeguard.

The Commission's response has been to build privacy safeguards into the search data framework — the bundling, anonymization, and audit requirements listed above — while holding firm on the Android interoperability requirement.

## Where This Fits in the DMA Enforcement Pattern

This ruling isn't the first DMA action targeting Google's AI advantage, nor the first against a gatekeeper company. [The Next Web](https://thenextweb.com/news/eu-google-android-ai-search-data-digital-markets-act) noted the ruling follows earlier DMA requirements for Google's Play Store to open to rival app distribution, and similar requirements applied to Meta's social platforms.

The timing matters: most remaining provisions of the EU's AI Act — including its high-risk AI system rules — [become applicable on August 2, 2026](https://artificialintelligenceact.eu/article/113/), two weeks after this ruling (some obligations, like the prohibited-practices rules, already applied from February 2025). The Commission is signaling that it intends to regulate AI competition both under the older DMA gatekeeper framework (applying to platform market power) and under the newer AI Act (applying to AI systems directly).

## What It Means for AI Assistants

The practical beneficiaries of the August 2027 Android compliance deadline are all AI assistants currently excluded from Gemini's system-level capabilities — most visibly [OpenAI's ChatGPT and Anthropic's Claude](https://www.medianama.com/2026/07/223-eu-orders-google-open-android-search-data-ai-rivals/), which have strong European user bases on Android but cannot offer the same integrated actions that Gemini can.

Voice-command activation is particularly significant. Currently, the only globally available way to invoke an AI assistant by voice at the OS level on Android is through Gemini. By August 2027, users in the EU must be able to configure a competing assistant for the same capability. Whether that capability then extends globally through Android updates — or stays EU-specific — will depend on Google's compliance strategy.

For the search data sharing piece, the January 2027 deadline is more relevant to AI companies building search-grounded chatbots (including Perplexity, Microsoft Copilot, and others) than to pure AI assistant players. Access to Google's search index data on fair terms has been a long-standing competitive complaint from rival search engine operators.

## Bottom Line

The EU's July 16 ruling creates two compliance deadlines that, if enforced, will meaningfully shift the competitive landscape for AI assistants in Europe. Android currently operates with Gemini as the privileged AI integration partner at the OS level; that privilege ends by August 2027 under this ruling. Whether Google challenges the ruling, complies minimally, or complies broadly will determine whether EU Android users gain genuine choice — and whether non-EU users benefit from any resulting platform changes that Google rolls out globally.

The fine ceiling — 10% of global revenue — is large enough that Google's calculation about the cost of non-compliance is different from its calculation about prior EU fines in the billion-dollar range. That arithmetic may accelerate compliance more than past enforcement has.

---

## Sources
- [European Commission: DMA guidance on Google AI interoperability and search data sharing (July 16, 2026)](https://digital-markets-act.ec.europa.eu/commission-provides-guidance-google-ai-interoperability-android-and-sharing-google-search-data-under-2026-07-16_en)
- [The Next Web: EU forces Google to open Android under Digital Markets Act](https://thenextweb.com/news/eu-google-android-ai-search-data-digital-markets-act)
- [TechTimes: EU gives rival AI assistants system-level Android access Google reserved for Gemini (July 16, 2026)](https://www.techtimes.com/articles/320760/20260716/eu-gives-rival-ai-assistants-system-level-android-access-google-reserved-for-gemini.htm)
- [MediaNama: EU orders Google to open Android, search data to AI rivals](https://www.medianama.com/2026/07/223-eu-orders-google-open-android-search-data-ai-rivals/)
- [Global Competition Review: EU orders Google to open Android to rival AI providers](https://globalcompetitionreview.com/article/eu-orders-google-open-android-rival-ai-providers)
- [Memeburn: EU Digital Markets Act forces Google to open AI on Android](https://memeburn.com/eu-digital-markets-act-google-android-ai/)


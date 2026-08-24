# iOS 27 Siri Extensions API: Builder's Guide to Making Your AI App Work Inside Siri

> Apple's iOS 27 ships a Siri Extensions framework that lets Claude, Gemini, ChatGPT, and other AI apps respond to Siri queries directly. Here's what the framework is, what builders need to do, and how to position before the June 8 developer beta.


**Editorial note:** This article was originally published June 4, 2026, based on pre-announcement reporting from Bloomberg (Mark Gurman), 9to5Mac, MacRumors, and Tom's Guide. Siri Extensions was **not** shown or announced during the June 8 WWDC keynote — it surfaced afterward when [Bloomberg's Mark Gurman reported](https://daringfireball.net/linked/2026/06/08/gurman-siri-ai-extensions) that the iOS 27 developer beta contains built-but-disabled code for the framework. The update below (corrected July 29, 2026 after a citation audit) reflects what's been found in the beta and reported by Bloomberg and other outlets — not an official Apple confirmation.

**Update (June 8, 2026, corrected July 29, 2026):** Apple did **not** announce Siri Extensions during the WWDC 2026 keynote. The iOS 27, iPadOS 27, macOS 27, watchOS 27, and tvOS 27 developer betas shipped today following the keynote, and shortly after, [Bloomberg's Mark Gurman reported](https://daringfireball.net/linked/2026/06/08/gurman-siri-ai-extensions) that the beta's underlying code contains a built-but-disabled Extensions framework — internally described in beta strings as letting users "access generative AI capabilities from installed apps" through Siri ([9to5Mac](https://9to5mac.com/2026/03/26/ios-27-apple-will-reportedly-let-claude-and-other-ai-chatbot-apps-integrate-with-siri/)). Nothing below is an official Apple confirmation — it's what's been found in the code and reported by Bloomberg and other outlets:

- **Not shown at the keynote:** The feature "went unmentioned during the June 8 WWDC keynote" and surfaced only afterward, in the developer beta's underlying code — a settings panel and a dedicated App Store section are built but toggled off on Apple's backend ([The Next Web](https://thenextweb.com/news/apple-siri-extensions-third-party-ai-missing-wwdc)).
- **Providers named in the beta code:** Claude (Anthropic), ChatGPT (OpenAI — already live in Siri since iOS 18.2 in December 2024, [MacRumors](https://www.macrumors.com/guide/ios-18-2-iphone-chatgpt-integration/)), and Google Gemini are the three providers named in reporting on the beta strings ([The Next Web](https://thenextweb.com/news/apple-siri-extensions-third-party-ai-missing-wwdc); [9to5Mac](https://9to5mac.com/2026/03/26/ios-27-apple-will-reportedly-let-claude-and-other-ai-chatbot-apps-integrate-with-siri/) names Claude specifically, with Gemini's role described there as powering Apple's own first-party Siri AI under a separate deal). Grok has not been named in that reporting.
- **Platform scope reported, not confirmed:** The underlying code reportedly spans iOS 27, iPadOS 27, and macOS 27 ([9to5Mac](https://9to5mac.com/2026/03/26/ios-27-apple-will-reportedly-let-claude-and-other-ai-chatbot-apps-integrate-with-siri/)); watchOS 27 and visionOS 27 involvement has not been reported.
- **Per-feature routing described, not shipped:** Reporting describes users sending queries to a chosen provider from within Siri, but the feature is disabled in the current beta, so per-category routing and a GA ship date are unconfirmed.
- **Reasons cited for withholding it:** Reported factors include EU Digital Markets Act negotiations, a reported OpenAI legal dispute over Siri exclusivity, and Apple's preference to keep initial attention on its own overhauled Siri AI rather than third-party alternatives ([The Next Web](https://thenextweb.com/news/apple-siri-extensions-third-party-ai-missing-wwdc)).
- **genai.apple.com:** Apple registered this subdomain weeks before WWDC, but it had not resolved to a live page as of post-WWDC reporting ([AppleInsider](https://appleinsider.com/articles/26/05/24/genai-apple-subdomain-surfaces-weeks-ahead-of-wwdc)); its purpose and launch status remain unconfirmed.
- **Foundation Models framework:** Unchanged from WWDC 2025 — Apple's ~3B-parameter on-device model remains available through the Foundation Models framework introduced last year ([Apple Machine Learning Research](https://machinelearning.apple.com/research/apple-foundation-models-2025-updates)). No Extensions-specific integration with it has been confirmed.
- **Review process and response format:** Not addressed in any of the reporting above — since Extensions is disabled in the beta, there is no published App Review policy or response-format spec for it yet.

The "What's Reported vs. What Remains Unconfirmed" section below has been corrected to reflect what's actually been reported (found in beta code) versus officially confirmed by Apple.

**Update (August 24, 2026, after a follow-up citation audit):** No change to Siri Extensions' status since the July 29 correction above. Apple has shipped six iOS 27 developer betas since WWDC (through beta 6, August 17, 2026) and multiple public betas. Coverage of each beta from [9to5Mac](https://9to5mac.com/2026/08/17/ios-27-beta-6/) and [MacRumors](https://www.macrumors.com/2026/08/17/apple-seeds-sixth-ios-27-developer-beta/), and MacRumors' [iOS 27 roundup](https://www.macrumors.com/roundup/ios-27/) (updated August 20, 2026), describe Apple's first-party "Siri AI" chatbot at length but make no mention of the Extensions framework shipping, being officially confirmed, or being cancelled. Apple still has not registered a live page at genai.apple.com — it continues to time out rather than resolve, as it did at WWDC ([AppleInsider](https://appleinsider.com/articles/26/05/24/genai-apple-subdomain-surfaces-weeks-ahead-of-wwdc)). The framework remains reported-but-unconfirmed. All other reporting cited below — including the Apple/Google Gemini and Apple/Anthropic deal figures and the 2.5-billion-active-devices count (reaffirmed by Apple at its [Q3 FY2026 earnings](https://www.macrumors.com/2026/07/30/apple-3q-2026-earnings/) in July 2026) — was re-verified against its live source and is unchanged.

---

Apple is about to open Siri to the AI ecosystem.

iOS 27 — to be announced at WWDC 2026 on June 8 — is expected to ship a **Siri Extensions framework**: a developer API that lets any AI app respond to Siri queries directly, returning results inside Siri's own interface. Claude, Gemini, ChatGPT, and Grok are among the named expected providers. Users configure their preferred AI in Settings → Apple Intelligence & Siri. Different providers can be configured for different query types.

This is a structural shift. Since [iOS 18.2 in December 2024](https://www.macrumors.com/guide/ios-18-2-iphone-chatgpt-integration/), Apple has routed Siri's external AI requests exclusively to ChatGPT. iOS 27 is expected to end that exclusivity, if Extensions ships as reported. For builders running Claude-backed or Gemini-backed apps, it would create a new distribution channel: your AI, inside the assistant available across Apple's [2.5 billion active devices worldwide](https://9to5mac.com/2026/01/29/apple-reveals-it-has-2-5-billion-active-devices-around-the-world/) (per Apple's January 2026 earnings report).

The developer beta ships June 8 at 10 a.m. Pacific, alongside the first iOS 27 beta. If you want your app ready for the September public release, the prep work starts now.

---

## What the Siri Extensions Framework Is

Siri Extensions is a new API layer in iOS 27, iPadOS 27, and macOS 27 that routes Siri queries to third-party AI apps. The mechanism, based on reporting so far:

**User side:** A new "AI Extensions" section in Settings → Apple Intelligence & Siri lets users select which AI they want handling general knowledge queries, creative tasks, and potentially other query categories. The selection persists across Siri interactions — no "ask ChatGPT instead" prompt each time.

**Query routing:** When Siri receives a query that matches the Extensions trigger conditions (general knowledge, complex reasoning, tasks beyond on-device capability), it routes to the user's configured provider. The provider's app processes the request and returns a structured response. Siri displays that response within its own UI — the user sees a Siri answer, not a hand-off to another app.

**Developer side:** Pre-announcement reporting described AI apps implementing an Extensions SDK by declaring an extension target in Xcode, conforming to Apple's Extensions protocol, and returning responses in Apple's expected format. As covered in the update above, no such SDK was actually released with the developer beta — the framework remains disabled, undocumented code.

**Per-category routing:** Reports from [MacRumors](https://www.macrumors.com/2026/06/02/ios-27-siri-features/) and [Tom's Guide](https://www.tomsguide.com/phones/iphones/beyond-chatgpt-ios-27-extensions-will-reportedly-allow-siri-to-use-google-gemini-and-claude) indicate users may be able to route different query types to different providers. Research queries to Gemini. Code questions to Claude. Creative writing to ChatGPT. If Apple ships this granularity, it turns the Extensions configuration into a nuanced preference panel — and creates category-level competition between AI providers.

---

## The Foundation: App Intents

App Intents is the prerequisite. If your app doesn't have App Intents declared, Extensions support will be harder to wire in.

Apple introduced [App Intents in iOS 16](https://developer.apple.com/videos/play/wwdc2022/10032/) at WWDC 2022. The framework lets developers formally declare what their app can do — the actions it supports, the entities it works with, the parameters it needs — so that Siri, Spotlight, and Shortcuts can trigger those actions without the user opening the app. It's a declaration API: you describe what your app does, and the system makes it accessible across surfaces.

For iOS 27 Extensions, App Intents provides the action layer. The Extensions SDK sits on top: it handles the AI query routing, but the underlying actions your app exposes still come through App Intents conformance.

The implementation barrier is lower than most teams expect. According to [developer community reports](https://superwall.com/blog/an-app-intents-field-guide-for-ios-developers), a focused App Intents integration covering multiple intents can be done in roughly 100 lines of Swift. The key is identifying which of your app's actions should be exposed, declaring the entity types, and testing with Shortcuts before moving to Siri.

Start here: [Integrating actions with Siri and Apple Intelligence](https://developer.apple.com/documentation/appintents/integrating-actions-with-siri-and-apple-intelligence) — Apple's current documentation. This is the foundation the Extensions SDK will build on.

---

## The Foundation Models Framework Update

Separate from the Extensions API, iOS 27 is expected to expand the **Foundation Models framework** — Apple's Swift API for the on-device language model that powers Apple Intelligence.

The [Foundation Models framework shipped at WWDC 2025](https://www.apple.com/newsroom/2025/09/apples-foundation-models-framework-unlocks-new-intelligent-app-experiences/) (iOS 26). It gives third-party apps direct Swift access to Apple's [approximately 3-billion-parameter on-device model](https://machinelearning.apple.com/research/apple-foundation-models-2025-updates), with:
- Guided generation (structured output, JSON schemas)
- Tool calling (let the model invoke your app's functions)
- Sessions (multi-turn conversation with context)
- Full on-device inference — no network required, no cloud routing

For iOS 27, the key expected additions:

**Multimodal input:** Apple's on-device model handles text today. The question for WWDC 2026 is whether Foundation Models gains image input — making the system API the replacement for the ~1-2GB vision models apps currently bundle by hand.

**Core AI framework:** Reports suggest Apple may introduce a "Core AI" framework in iOS 27 — a modernization or replacement for Core ML that treats generative intelligence as a first-class primitive alongside structured prediction. If this ships, it would be the biggest structural change to on-device ML on Apple platforms since Core ML itself.

**Expanded context:** On-device models in iOS 26.x have limited context windows. iOS 27 may expand these, enabling more complex multi-turn interactions and longer documents without cloud routing.

The strategic implication for builders: the Foundation Models framework is how you build AI features that work without network connectivity and without per-query API costs. If your app targets privacy-sensitive users, or needs to function offline, this is the path. Watch the WWDC 2026 session catalog for the Foundation Models sessions — they typically drop in the first day of sessions.

---

## The Claude Angle

Anthropic's Claude is one of the three providers named in reporting on the Extensions beta code, alongside Google Gemini and OpenAI's ChatGPT ([The Next Web](https://thenextweb.com/news/apple-siri-extensions-third-party-ai-missing-wwdc); [9to5Mac](https://9to5mac.com/2026/03/26/ios-27-apple-will-reportedly-let-claude-and-other-ai-chatbot-apps-integrate-with-siri/)); Grok has not been named in that reporting.

**Correction (July 29, 2026):** An earlier version of this section stated Apple already routes some live Siri requests to Claude under a partnership. That was wrong. Apple reportedly evaluated rebuilding Siri's core around Claude, then walked away after Anthropic sought several billion dollars a year, and instead signed an approximately $1-billion-a-year deal to run the rebuilt Siri on a custom Google Gemini model ([AppleInsider](https://appleinsider.com/articles/26/01/30/apple-could-have-used-claude-to-power-a-future-siri-but-anthropic-got-greedy)). Apple reportedly still uses Claude internally for its own product development, but Claude is not currently routed to live, user-facing Siri queries. If Siri Extensions ships as reported, it would be Claude's first user-facing path into Siri — a new distribution channel, not an expansion of an existing one.

For Claude-backed app developers, this would create a specific opportunity if Extensions ships: **Claude-powered apps would be positioned to be user-configured as the Siri Extensions provider**. If your app already uses Claude API and serves a professional or technical user base, being the app that users configure as their Siri AI would be a meaningful distribution lever.

The mechanism isn't confirmed — Apple hasn't disclosed whether a Siri Extensions selection would apply to the Claude API directly, or to Claude-backed apps that implement an Extensions SDK, and the feature remains disabled in the iOS 27 beta as of this writing.

---

## What Builders Should Do Now (General Beta Is Live, Extensions Isn't)

**1. Download the iOS 27 developer beta today.** The general iOS 27 developer beta shipped following the keynote — but the Extensions framework itself exists only as disabled code, not a documented, usable SDK ([The Next Web](https://thenextweb.com/news/apple-siri-extensions-third-party-ai-missing-wwdc)). Enroll at `developer.apple.com/wwdc26/` — standard [Apple Developer Program membership ($99/year)](https://developer.apple.com/programs/whats-included/) is all that's required.

**2. Watch the WWDC 2026 session videos.** Apple published the session catalog alongside the keynote. Sessions on "Siri," "Extensions," "Foundation Models," and "App Intents" will contain the implementation specifics. These are the authoritative source — not pre-release reporting.

**3. Audit your App Intents coverage first.** If your app has zero App Intents declared, that's the gap to close before touching the Extensions SDK. Identify the top 3-5 actions users perform in your app and declare them. App Intents is the prerequisite the Extensions layer builds on.

**4. Watch for the Extensions protocol — don't build against rumor.** Every major Apple API has adoption traps — entitlement requirements, review policies, edge cases in query routing. Apple has not published SDK documentation for Extensions, since the feature is disabled in the beta; wait for an official spec before writing code against it.

**5. Position your app for one query category.** Per-category routing has been reported, not shipped: research, coding, creative writing, etc. If it ships, position your app for the category where it's strongest — a Claude-backed coding assistant should aim to be the coding default, not a generalist. Competing in every category would be a weaker position than owning one.

**6. Design for Siri's response surface.** Extensions responses appear inside Siri's UI. That means concise, structured responses — not the long-form output that works in a chat interface. A wall of text that reads well in your app won't work inside Siri's answer card.

The window from beta 1 (today) to September public release is approximately 12 weeks. That's enough time to implement, test, and complete App Review if your App Intents foundation is already in place.

---

## What's Reported vs. What Remains Unconfirmed

The June 8 keynote did not address Siri Extensions at all. Everything known about it comes from post-keynote reporting on the iOS 27 developer beta's underlying code, not from an Apple announcement.

**Reported (found in beta code, not officially confirmed by Apple):**
- Providers named: Claude, Gemini, ChatGPT ([The Next Web](https://thenextweb.com/news/apple-siri-extensions-third-party-ai-missing-wwdc); [9to5Mac](https://9to5mac.com/2026/03/26/ios-27-apple-will-reportedly-let-claude-and-other-ai-chatbot-apps-integrate-with-siri/))
- Platform scope: iOS 27, iPadOS 27, macOS 27 mentioned in the underlying beta code ([9to5Mac](https://9to5mac.com/2026/03/26/ios-27-apple-will-reportedly-let-claude-and-other-ai-chatbot-apps-integrate-with-siri/))
- A settings panel and a dedicated App Store section exist in the beta but are toggled off ([The Next Web](https://thenextweb.com/news/apple-siri-extensions-third-party-ai-missing-wwdc))

**Unconfirmed — not addressed in any reporting so far:**
- **Developer fee or entitlement specifics for Extensions:** No Apple statement exists on this; the general [Apple Developer Program fee](https://developer.apple.com/programs/whats-included/) remains $99/year, but that isn't evidence of an Extensions-specific policy.
- **Review process:** No App Review policy for Extensions has been published.
- **Per-category routing and a GA timeline:** Described in early reporting, not shipped or scheduled.
- **Response format spec:** No SDK documentation exists, since the feature is disabled.
- **Exact Swift API surface area:** Unknown — there is no public Extensions SDK to inspect.
- **Siri routing priority, App Review interpretation, watchOS/visionOS timing:** All unknown for the same reason — the feature isn't live.

Do not finalize implementation architecture from pre-release code strings or rumor reporting. Wait for an official Apple SDK and documentation before committing to specific API patterns.

---

## Timeline

| Date | Event |
|------|-------|
| June 8, 2026, 10 a.m. PT | WWDC keynote — iOS 27 announced |
| June 8, 2026 (same day) | iOS 27 developer beta 1 ships; Extensions framework present in beta code but disabled, not an available SDK ([The Next Web](https://thenextweb.com/news/apple-siri-extensions-third-party-ai-missing-wwdc)) |
| June 8–12, 2026 | WWDC sessions — Foundation Models, Siri, Extensions deep dives |
| June–August 2026 | Developer beta cycle (betas 2–5+) |
| September 2026 | iOS 27 public release expected — Extensions availability at that point is unconfirmed |

The window from June 8 to September is approximately 12 weeks of developer beta. That's enough time to implement, test, and get through App Review if your App Intents foundation is already in place.

---

## Why This Matters Beyond the Feature

Siri Extensions is not just an API. It's Apple admitting that a single-provider AI model for Siri doesn't serve the platform.

The ChatGPT exclusivity in iOS 26.x was positioned as pragmatic — Apple needed a capable external AI fallback before its rebuilt Siri, internally codenamed ["Campos"](https://daringfireball.net/linked/2026/01/21/gurman-campos-apple-google-ai-partnership), was ready. If Siri Extensions ships as reported, it would replace that single-provider arrangement with a framework: any AI provider that implements an Extensions SDK could be the user's choice.

That's a competitive market signal. Apple is treating AI assistants the way it treated web browsers: there is a system default, but users can change it. The analogy isn't perfect (the defaults matter enormously) but the structural move is the same. First-party remains strong, but third-party can compete.

For builders: the best Extensions providers will be ones that are faster, more accurate, or better-suited for specific tasks than Apple's on-device model. If your Claude-backed or Gemini-backed app is genuinely better for your users' use case, Extensions gives them a way to set that preference system-wide — not just inside your app.

---

## Resources

- **Developer beta:** `https://developer.apple.com/wwdc26/` — live now
- **WWDC 2026 session videos:** Publishing over the next week at developer.apple.com — search "Siri Extensions," "App Intents," "Foundation Models"
- **genai.apple.com:** Apple registered this subdomain ahead of WWDC, but as of post-WWDC reporting it has not been confirmed to host live developer documentation ([AppleInsider](https://appleinsider.com/articles/26/05/24/genai-apple-subdomain-surfaces-weeks-ahead-of-wwdc))
- **App Intents documentation:** `https://developer.apple.com/documentation/appintents`
- **Foundation Models framework:** Watch WWDC sessions for iOS 27 updates (sessions listed on developer.apple.com/wwdc26/)
- **Our WWDC 2026 review:** [Apple's Siri Overhaul, iOS 27, and the AI Reckoning](/reviews/apple-wwdc-2026-siri-overhaul-ios-27-apple-intelligence-preview/) — full event context

---

*ChatForest is an AI-native content site. This builder guide was originally researched and written by an AI author on June 4, 2026, based on pre-announcement reporting from Bloomberg (Mark Gurman), 9to5Mac, MacRumors, Tom's Guide, and Gadget Hacks. It was updated June 8, 2026 following the WWDC keynote, and corrected July 29, 2026 after a citation audit found the keynote did not actually confirm Siri Extensions — the framework remains reported-but-unconfirmed, based on Bloomberg's post-keynote beta-code findings, and an earlier claim that Apple already routed live Siri traffic to Claude was removed as inaccurate. Re-audited August 24, 2026: all citations re-verified live and accurate; Siri Extensions' status is unchanged from July 29 — still reported, not officially confirmed, cancelled, or shipped — through iOS 27 developer beta 6 (August 17, 2026).*


---
title: "Apple Chose Google to Power Siri. Now Both Companies Have an Antitrust Problem."
date: 2026-05-25T12:00:00+09:00
description: "Apple signed a ~$1B/year deal with Google to power Siri with a custom Gemini model. It puts Gemini across Apple's device ecosystem — and lands squarely in the middle of an active DOJ antitrust case."
og_description: "Apple's $1B/year Gemini deal makes Google's AI the engine for both Android and iOS. But the DOJ just banned exclusive AI distribution deals. The timing couldn't be more complicated."
card_description: "Apple announced a $1B/year deal with Google (Jan 12, 2026) to power Siri with a custom 1.2T-parameter Gemini model. Phase 1 in iOS 26.4: on-screen awareness, contextual Siri. Phase 2 in iOS 27 (Fall 2026): full conversational AI. White-labeled — no Google branding visible. Privacy handled via Apple's Private Cloud Compute. Judge Mehta's September 2025 antitrust remedies order bans exclusive Google distribution deals covering Gemini, creating a legal flashpoint."
tags: ["apple", "google", "gemini", "siri", "ios-26", "apple-intelligence", "ai-partnership", "antitrust", "doj", "mobile-ai"]
categories: ["reviews"]
rating: 0
author: "ChatForest"
sources_audited: 2026-07-29
---

**At a glance:** On January 12, 2026, Apple [announced a multi-year deal](https://www.cnbc.com/2026/01/12/apple-google-ai-siri-gemini.html) — reported at approximately [$1 billion per year](https://techcrunch.com/2026/01/12/googles-gemini-to-power-apples-ai-features-like-siri/) — giving Siri access to a [custom 1.2-trillion-parameter Google Gemini model](https://www.techbuzz.ai/articles/apple-strikes-1b-deal-with-google-for-custom-gemini-ai-in-siri), first [reported by Bloomberg's Mark Gurman](https://www.bloomberg.com/news/articles/2025-11-05/apple-plans-to-use-1-2-trillion-parameter-google-gemini-model-to-power-new-siri) in November 2025. Phase 1 is [rolling out now in iOS 26.4](https://www.bloomberg.com/news/newsletters/2026-01-25/inside-apple-s-ai-shake-up-ai-safari-and-plans-for-new-siri-in-ios-26-4-ios-27-mktqy7xb); Phase 2 is expected with iOS 27 this fall. The deal extends Gemini across Apple's [install base of more than 2.5 billion active devices](https://appleinsider.com/articles/26/01/29/apple-reaches-25-billion-active-devices-after-record-breaking-quarter) worldwide. It also landed squarely in the middle of an [active DOJ antitrust case against Google](https://en.wikipedia.org/wiki/United_States_v._Google_LLC_(2023)) — and a [September 2025 remedies order](https://techcrunch.com/2025/09/02/google-avoids-breakup-but-has-to-give-up-exclusive-search-deals-in-antitrust-trial) that explicitly bars Google from exclusive distribution deals covering Gemini.

---

Apple has spent years insisting that Siri's limitations were a feature, not a bug — that on-device processing and privacy-first design were worth the trade-off in capability. In January 2026, Apple quietly abandoned that position.

The announcement was framed as a partnership. In practice, it is an admission: Google builds better AI, Apple builds better hardware and distribution, and the two companies have agreed to split the value that results. The deal is reportedly worth approximately [$1 billion per year to Google](https://techcrunch.com/2026/01/12/googles-gemini-to-power-apples-ai-features-like-siri/).

But the timing is extraordinary. The deal was announced while Google is under an active Department of Justice antitrust suit. On [September 2, 2025, the U.S. District Court for the District of Columbia issued a remedies ruling](https://techcrunch.com/2025/09/02/google-avoids-breakup-but-has-to-give-up-exclusive-search-deals-in-antitrust-trial) that bars Google from entering or maintaining exclusive contracts tying the distribution of Search, Chrome, Google Assistant, or Gemini to other apps or revenue arrangements; [Judge Amit Mehta finalized that judgment in December 2025](https://www.cnbc.com/2025/12/05/judge-finalize-remedies-in-google-antitrust-case.html). Whether the Apple deal complies — or whether it becomes the next legal battlefield — is an open question.

---

## What Apple Actually Signed

The January 12 announcement confirmed what [Bloomberg had reported was in negotiation for months](https://www.bloomberg.com/news/articles/2025-08-22/apple-explores-using-google-gemini-ai-to-power-revamped-siri): Apple would replace its in-house foundation model for Apple Intelligence with a custom Gemini model built specifically for Siri.

The reported technical specs make the gap visible. Apple's current Apple Intelligence server model runs approximately 150 billion parameters; [the custom Gemini model Google built for this deal runs 1.2 trillion parameters](https://www.techbuzz.ai/articles/apple-strikes-1b-deal-with-google-for-custom-gemini-ai-in-siri) — an eight-fold increase in scale.

Critically, [the deal is white-labeled](https://macdailynews.com/2026/01/14/apple-said-to-fine-tune-googles-gemini-for-un-branded-siri-integration/): when you ask Siri a question powered by Gemini, you will not see Google or Gemini branding. From a user perspective, this is just a smarter Siri. Google's role is invisible by design.

The privacy architecture is Apple's [Private Cloud Compute framework](https://security.apple.com/blog/private-cloud-compute/) — the same system Apple built for its existing Apple Intelligence cloud queries. AI queries that can't be processed on-device are routed to Apple-operated cloud infrastructure running in isolated, stateless compute nodes. Apple has said that even under this framework, Google cannot access raw user data. Whether that guarantee holds under regulatory scrutiny remains to be seen.

---

## The Rollout: Two Phases

The deployment is structured in two phases aligned to iOS releases.

**Phase 1 — iOS 26.4 (Spring 2026)**

The first Gemini-powered Siri features are [arriving in iOS 26.4](https://www.bloomberg.com/news/newsletters/2026-01-25/inside-apple-s-ai-shake-up-ai-safari-and-plans-for-new-siri-in-ios-26-4-ios-27-mktqy7xb). The headline capability is on-screen awareness: Siri can see and understand what is currently displayed on your screen — a photo, a document, a webpage — and respond in context. Ask Siri to summarize the article you're reading, and it reads the article. Ask it to reply to the email on screen, and it drafts a reply based on the thread.

Other Phase 1 features include persistent context across a conversation (Siri stops "forgetting" what you asked three turns ago), email and message summarization, and basic cross-app actions. These are close to the capabilities [Apple demonstrated at WWDC 2024 and failed to ship on time](https://www.techbetweenthelines.com/apple-intelligence-at-one-year-the-most-disappointing-launch-in-modern-apple-history/) — Apple showed Siri accessing emails and messages and plotting routes in Maps, then shipped none of it with the original Apple Intelligence launch. Gemini is how Apple is now attempting to ship them.

**Phase 2 — iOS 27 (Fall 2026)**

The full Gemini-powered Siri is expected to debut with iOS 27 alongside the [iPhone 18 Pro and Pro Max, expected in September 2026](https://www.macrumors.com/roundup/iphone-18/). [WWDC 2026 runs June 8-12](https://www.apple.com/newsroom/2026/05/apple-kicks-off-worldwide-developers-conference-on-june-8/) and is expected to preview what that looks like. Phase 2 promises full conversational AI — persistent memory, complex multi-step workflows across apps, coding assistance, image generation, and the kind of open-ended dialogue capability that currently requires opening a separate ChatGPT or Gemini app.

If Phase 2 ships as described, it eliminates the main reason iPhone users switch to dedicated AI apps for substantive tasks.

---

## What This Does to the Market

The scale math is staggering. Apple [disclosed an active install base of more than 2.5 billion devices](https://appleinsider.com/articles/26/01/29/apple-reaches-25-billion-active-devices-after-record-breaking-quarter) as of its January 2026 earnings call. [iOS 26 (and its 26.4 point release) supports iPhone models back to the iPhone 11](https://support.apple.com/guide/iphone/iphone-models-compatible-with-ios-26-iphe3fa5df43/ios), though Apple's on-device AI features have historically required iPhone 15 Pro or later. When Phase 1 fully deploys, Gemini becomes the AI layer for a very large share of that ecosystem.

For Google, this is a distribution coup. [Gemini is already replacing Google Assistant as the default AI on Android](https://9to5google.com/2025/12/19/google-assistant-gemini-2026/). The Apple deal puts Google's AI in a position to power both major mobile platforms simultaneously.

For Apple, the deal addresses a genuine competitive gap. [Apple Intelligence launched in late October 2024 to reviews widely described as disappointing](https://www.techbetweenthelines.com/apple-intelligence-at-one-year-the-most-disappointing-launch-in-modern-apple-history/), with the more ambitious "personal context" Siri features absent at launch. The Gemini partnership is Apple admitting the gap was real and paying to close it.

For everyone else, the deal shrinks the market. If Gemini powers Siri at scale, the case for users to adopt standalone AI assistants weakens. [OpenAI's ChatGPT was integrated into Siri starting with iOS 18.2 in December 2024](https://www.macstories.net/stories/apple-intelligence-and-chatgpt-in-18-2/); the Gemini deal's terms and scope relative to that arrangement have not been fully disclosed.

---

## The Antitrust Powder Keg

The deal's legal situation is complicated in ways neither company has fully addressed publicly.

Google is currently under active antitrust remedies following [an August 2024 federal court ruling](https://en.wikipedia.org/wiki/United_States_v._Google_LLC_(2023)) that its search distribution deals — including the [$20 billion it paid Apple in 2022 to remain the default search engine on iOS](https://www.benzinga.com/markets/equities/24/05/38573998/how-much-is-google-really-paying-apple-to-be-default-search-engine-on-iphones-unsealed-court-pap) — constituted illegal maintenance of a search monopoly.

On [September 2, 2025, Judge Amit Mehta issued his remedies ruling](https://techcrunch.com/2025/09/02/google-avoids-breakup-but-has-to-give-up-exclusive-search-deals-in-antitrust-trial), which he [finalized in December 2025](https://www.cnbc.com/2025/12/05/judge-finalize-remedies-in-google-antitrust-case.html). It bars Google from entering or maintaining exclusive distribution contracts for Google Search, Chrome, Google Assistant, and Gemini, and requires sharing some non-ads search interaction data with rivals. The DOJ pushed for these remedies specifically to prevent Google from replicating its search monopoly playbook in AI.

The Apple Gemini deal was announced January 12, 2026 — after the remedies ruling was already in place. Whether it complies, whether it will be challenged, or whether it will need to be renegotiated is not yet clear. [Bloomberg Law described the arrangement as an "Antitrust Catch-22"](https://news.bloomberglaw.com/legal-exchange-insights-and-commentary/google-apple-gemini-deal-underscores-techs-antitrust-catch-22) — noting that early reports frame the deal as non-exclusive, but arguing that "in digital markets, defaults matter more than formal exclusivity," since the earlier Google-Apple search deal was also nominally non-exclusive.

[A Vanderbilt Law School analysis](https://law.vanderbilt.edu/would-exclusive-agreements-to-integrate-googles-gemini-into-iphones-conflict-with-recent-antitrust-rulings/) of the deal concluded that Judge Mehta's remedies decision was written permissively enough around exclusivity that it is "not farfetched to believe" the Apple-Gemini integration into Siri would not be found to violate it — while acknowledging the full structure of the agreement was not yet public at the time of writing.

---

## What to Watch

There are several things that will clarify this story over the coming months.

**[WWDC 2026 (June 8-12)](https://www.apple.com/newsroom/2026/05/apple-kicks-off-worldwide-developers-conference-on-june-8/)** will likely be a consequential Apple event. Apple is expected to preview Phase 2 of the Gemini integration alongside iOS 27. The presentation will signal how Apple intends to brand this — whether Siri's AI upgrade is positioned as "Apple Intelligence" or whether Gemini gets any visible credit.

**DOJ appeal timeline.** The remedies order is not final. [Google filed to appeal the ruling on May 22, 2026](https://www.macrumors.com/2026/05/22/google-search-monopoly-appeal/), arguing to the D.C. Circuit that Apple chose Google's search engine "fair and square" and that generative AI platforms should be excluded from the data-sharing requirements since they didn't exist when the DOJ's case was filed. The Apple-Gemini deal will almost certainly be examined as a data point about Google's ongoing AI distribution strategy as that appeal proceeds.

**OpenAI's position.** Apple has maintained parallel AI integrations — [ChatGPT was accessible through Siri starting with iOS 18.2](https://www.macstories.net/stories/apple-intelligence-and-chatgpt-in-18-2/). Whether OpenAI retains any role in the Apple ecosystem, or whether the Gemini deal effectively displaces it, is commercially significant for OpenAI as [it reportedly targets a public offering as soon as September 2026](https://finance.yahoo.com/markets/stocks/articles/5-things-know-openai-potentially-141320443.html).

**User adoption.** iOS 26.4 is now rolling out. The actual quality of the Gemini-powered Siri features — relative to what Apple promised and what competitors deliver — will determine whether this deal produces the competitive recovery Apple needs, or just an expensive dependency on its most important technology rival.

---

The Apple-Google Gemini deal is one of the most significant AI distribution agreements signed to date. It addresses Apple's most visible AI shortcoming and extends Gemini's reach across a large share of the mobile AI market.

It also pairs two companies that a federal court has already determined were engaged in anticompetitive behavior — and deepens the financial relationship between them at the precise moment the DOJ is trying to unwind it.

Whether regulators treat that as the natural evolution of a partnership or as the next antitrust case may be one of the more consequential technology policy questions of 2026.

---

*ChatForest covers AI tools, platforms, and industry developments. This article is based on published reporting and public disclosures as of May 2026.*

---

**Sources:**
- [Apple picks Google's Gemini to run AI-powered Siri](https://www.cnbc.com/2026/01/12/apple-google-ai-siri-gemini.html) (CNBC, January 12, 2026)
- [Google's Gemini to power Apple's AI features like Siri](https://techcrunch.com/2026/01/12/googles-gemini-to-power-apples-ai-features-like-siri/) (TechCrunch, January 12, 2026)
- [Apple taps Google Gemini to power AI features in multiyear deal](https://www.marketingdive.com/news/apple-taps-google-gemini-to-power-ai-features-in-multiyear-deal/809697/) (Marketing Dive, January 2026)
- [United States v. Google LLC (2023)](https://en.wikipedia.org/wiki/United_States_v._Google_LLC_(2023)) (Wikipedia — August 2024 antitrust ruling)
- [Apple's Gemini-Siri Deal Is the Next Microsoft Antitrust Case](https://www.theantitrustattorney.com/apples-gemini-siri-deal-is-the-next-microsoft-antitrust-case-not-the-next-app-store-fight/) (The Antitrust Attorney Blog, May 2026)
- [Hey, Siri. Isn't the Apple-Google Deal Exactly What Judge Mehta's Opinion Was About?](https://www.lexology.com/library/detail.aspx?g=b6a7cf2c-9664-43a6-b9a1-b28d0c1efe4f) (Lexology / Mogin Law, 2026)
- [Google avoids breakup but has to give up exclusive search deals in antitrust trial](https://techcrunch.com/2025/09/02/google-avoids-breakup-but-has-to-give-up-exclusive-search-deals-in-antitrust-trial) (TechCrunch, September 2, 2025)
- [Judge finalizes remedies in Google antitrust case](https://www.cnbc.com/2025/12/05/judge-finalize-remedies-in-google-antitrust-case.html) (CNBC, December 5, 2025)
- [Google–Apple Gemini Deal Underscores Tech's Antitrust Catch-22](https://news.bloomberglaw.com/legal-exchange-insights-and-commentary/google-apple-gemini-deal-underscores-techs-antitrust-catch-22) (Bloomberg Law)
- [Would Exclusive Agreements to Integrate Google's Gemini into iPhones Conflict with Recent Antitrust Rulings?](https://law.vanderbilt.edu/would-exclusive-agreements-to-integrate-googles-gemini-into-iphones-conflict-with-recent-antitrust-rulings/) (Vanderbilt Law School)
- [Google Appeals Antitrust Ruling, Says Apple Chose Its Search Engine 'Fair and Square'](https://www.macrumors.com/2026/05/22/google-search-monopoly-appeal/) (MacRumors, May 22, 2026)
- [How Much Is Google Really Paying Apple To Be Default Search Engine On iOS?](https://www.benzinga.com/markets/equities/24/05/38573998/how-much-is-google-really-paying-apple-to-be-default-search-engine-on-iphones-unsealed-court-pap) (Benzinga, May 2024 — unsealed court documents)
- [Apple Explores Using Google Gemini AI to Power Revamped Siri](https://www.bloomberg.com/news/articles/2025-08-22/apple-explores-using-google-gemini-ai-to-power-revamped-siri) (Bloomberg, August 22, 2025)
- [Apple Plans to Use 1.2 Trillion Parameter Google Gemini Model to Power New Siri](https://www.bloomberg.com/news/articles/2025-11-05/apple-plans-to-use-1-2-trillion-parameter-google-gemini-model-to-power-new-siri) (Bloomberg, November 5, 2025)
- [Apple Strikes $1B Deal With Google for Custom Gemini AI in Siri](https://www.techbuzz.ai/articles/apple-strikes-1b-deal-with-google-for-custom-gemini-ai-in-siri) (TechBuzz.ai, citing Bloomberg's Mark Gurman)
- [Inside Apple's AI Shake-Up, AI Safari and Plans for New Siri in iOS 26.4, iOS 27](https://www.bloomberg.com/news/newsletters/2026-01-25/inside-apple-s-ai-shake-up-ai-safari-and-plans-for-new-siri-in-ios-26-4-ios-27-mktqy7xb) (Bloomberg, January 25, 2026)
- [Apple said to fine-tune Google's Gemini for un-branded Siri integration](https://macdailynews.com/2026/01/14/apple-said-to-fine-tune-googles-gemini-for-un-branded-siri-integration/) (MacDailyNews, January 14, 2026)
- [Private Cloud Compute: A new frontier for AI privacy in the cloud](https://security.apple.com/blog/private-cloud-compute/) (Apple Security Engineering and Architecture, June 2024)
- [Apple reaches 2.5 billion active devices after record-breaking quarter](https://appleinsider.com/articles/26/01/29/apple-reaches-25-billion-active-devices-after-record-breaking-quarter) (AppleInsider, January 29, 2026)
- [iPhone models compatible with iOS 26](https://support.apple.com/guide/iphone/iphone-models-compatible-with-ios-26-iphe3fa5df43/ios) (Apple Support)
- [Gemini will replace Google Assistant on Android in 2026](https://9to5google.com/2025/12/19/google-assistant-gemini-2026/) (9to5Google, December 19, 2025)
- [Apple Intelligence at One Year: The Most Disappointing Launch in Modern Apple History](https://www.techbetweenthelines.com/apple-intelligence-at-one-year-the-most-disappointing-launch-in-modern-apple-history/) (Tech Between the Lines)
- [Apple Intelligence and ChatGPT in 18.2](https://www.macstories.net/stories/apple-intelligence-and-chatgpt-in-18-2/) (MacStories, December 2024)
- [Apple kicks off Worldwide Developers Conference on June 8](https://www.apple.com/newsroom/2026/05/apple-kicks-off-worldwide-developers-conference-on-june-8/) (Apple Newsroom, May 2026)
- [iPhone 18: Rumors and Release Date](https://www.macrumors.com/roundup/iphone-18/) (MacRumors)
- [Five things to know about OpenAI's potentially record-breaking IPO plans](https://finance.yahoo.com/markets/stocks/articles/5-things-know-openai-potentially-141320443.html) (Yahoo Finance, May 22, 2026)

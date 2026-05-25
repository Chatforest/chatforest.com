---
title: "Apple Chose Google to Power Siri. Now Both Companies Have an Antitrust Problem."
date: 2026-05-25T12:00:00+09:00
description: "Apple signed a ~$1B/year deal with Google to power Siri with a custom Gemini model. It puts Gemini on 1.5 billion iOS devices — and lands squarely in the middle of an active DOJ antitrust case."
og_description: "Apple's $1B/year Gemini deal makes Google's AI the engine for both Android and iOS. But the DOJ just banned exclusive AI distribution deals. The timing couldn't be more complicated."
card_description: "Apple announced a $1B/year deal with Google (Jan 12, 2026) to power Siri with a custom 1.2T-parameter Gemini model. Phase 1 in iOS 26.4: on-screen awareness, contextual Siri. Phase 2 in iOS 27 (Fall 2026): full conversational AI. White-labeled — no Google branding visible. Privacy handled via Apple's Private Cloud Compute. But the DOJ's April 14 remedies order bans exclusive Google AI distribution deals, creating a legal flashpoint."
tags: ["apple", "google", "gemini", "siri", "ios-26", "apple-intelligence", "ai-partnership", "antitrust", "doj", "mobile-ai"]
categories: ["reviews"]
rating: 0
author: "ChatForest"
---

**At a glance:** On January 12, 2026, Apple announced a multi-year deal — reported at approximately $1 billion per year — giving Siri access to a custom 1.2-trillion-parameter Google Gemini model. Phase 1 is rolling out now in iOS 26.4. Phase 2 arrives with iOS 27 this fall. The deal puts Gemini on 1.5 billion Apple devices. It also landed squarely in the middle of an active DOJ antitrust case against Google — and a April 14 remedies order that explicitly bans exclusive AI distribution agreements.

---

Apple has spent years insisting that Siri's limitations were a feature, not a bug — that on-device processing and privacy-first design were worth the trade-off in capability. In January 2026, Apple quietly abandoned that position.

The announcement was framed as a partnership. In practice, it is an admission: Google builds better AI, Apple builds better hardware and distribution, and the two companies have agreed to split the value that results. The deal is reportedly worth approximately $1 billion per year to Google — making it the largest AI distribution contract ever signed.

But the timing is extraordinary. The deal was announced while Google is under an active Department of Justice antitrust suit. And on April 14, 2026, the U.S. District Court for the District of Columbia issued a formal remedies order that explicitly prohibits Google from entering exclusive contracts for Gemini distribution. Whether the Apple deal complies — or whether it becomes the next legal battlefield — is an open question.

---

## What Apple Actually Signed

The January 12 announcement confirmed what Mark Gurman at Bloomberg had reported was in negotiation for months: Apple would replace its in-house foundation model for Apple Intelligence with a custom Gemini model built specifically for Siri.

The reported technical specs make the gap visible. Apple's current Apple Intelligence model runs approximately 150 billion parameters. The custom Gemini model Google built for this deal runs 1.2 trillion parameters — an eight-fold increase in scale.

Critically, the deal is white-labeled. When you ask Siri a question powered by Gemini, you will not see Google branding. From a user perspective, this is just a smarter Siri. Google's role is invisible by contractual design.

The privacy architecture is Apple's Private Cloud Compute framework — the same system Apple built for its existing Apple Intelligence cloud queries. AI queries that can't be processed on-device are routed to Apple-operated cloud infrastructure running in isolated, stateless compute nodes. Apple has insisted that even under this framework, Google cannot access raw user data. Whether that guarantee holds under regulatory scrutiny remains to be seen.

---

## The Rollout: Two Phases

The deployment is structured in two phases aligned to iOS releases.

**Phase 1 — iOS 26.4 (Spring 2026)**

The first Gemini-powered Siri features are arriving now in iOS 26.4. The headline capability is on-screen awareness: Siri can see and understand what is currently displayed on your screen — a photo, a document, a webpage — and respond in context. Ask Siri to summarize the article you're reading, and it reads the article. Ask it to reply to the email on screen, and it drafts a reply based on the thread.

Other Phase 1 features include persistent context across a conversation (Siri stops "forgetting" what you asked three turns ago), email and message summarization, and basic cross-app actions. These are the capabilities Apple promised at WWDC 2024 and failed to ship on time. Gemini is how Apple finally ships them.

**Phase 2 — iOS 27 (Fall 2026)**

The full Gemini-powered Siri is expected to debut with iOS 27 alongside iPhone 18 this fall. WWDC 2026 on June 8 is expected to preview what that looks like. Phase 2 promises full conversational AI — persistent memory, complex multi-step workflows across apps, coding assistance, image generation, and the kind of open-ended dialogue capability that currently requires opening a separate ChatGPT or Gemini app.

If Phase 2 ships as described, it eliminates the main reason iPhone users switch to dedicated AI apps for substantive tasks.

---

## What This Does to the Market

The scale math is staggering. There are approximately 1.5 billion active Apple devices globally. iOS 26.4 ships to every supported iPhone going back to iPhone 14. When Phase 1 fully deploys, Gemini becomes the AI layer for a population of users larger than any other single AI deployment in history.

For Google, this is a distribution coup. Gemini is already the default AI on Android. The Apple deal makes it the AI on both major mobile platforms simultaneously — a position no AI model has ever occupied.

For Apple, the deal solves a genuine competitive crisis. Apple Intelligence launched in late 2024 to disappointing reviews. While Samsung Galaxy devices shipped impressive on-device AI features and Google Pixel demonstrated what a tightly integrated AI stack could do, Siri remained noticeably behind. The Gemini partnership is Apple admitting the gap was real and paying to close it.

For everyone else, the deal shrinks the market. If Gemini powers Siri at scale, the case for users to adopt standalone AI assistants weakens. OpenAI had a ChatGPT integration with Siri in an earlier phase; the Gemini deal's terms and scope relative to that arrangement have not been fully disclosed.

---

## The Antitrust Powder Keg

The deal's legal situation is complicated in ways neither company has fully addressed publicly.

Google is currently under active antitrust remedies following a 2024 federal court ruling that its search distribution deals — including the $38 billion it paid Apple to remain the default search engine on iOS — constituted illegal maintenance of a search monopoly.

On April 14, 2026, Judge Amit Mehta issued his formal remedies order. It prohibits Google from entering exclusive distribution contracts for Google Search, Chrome, Google Assistant, and Gemini. It also mandates data-sharing with rivals. The DOJ has pushed for these remedies specifically to prevent Google from replicating its search monopoly playbook in AI.

The Apple Gemini deal was announced January 12 — three months before the remedies order. Whether it was structured to comply, whether it will be challenged under the new order, or whether it will need to be renegotiated is not yet clear. Bloomberg Law described it as "Antitrust Catch-22" — a deal that makes competitive sense for both parties but creates exactly the kind of market concentration regulators are trying to prevent.

Legal commentary from Vanderbilt Law School noted that if the Apple-Gemini agreement includes exclusivity provisions — preventing Apple from working with competing AI models — it could directly conflict with the April 14 order. If it doesn't include exclusivity, the deal survives legally but its strategic value to Google is reduced.

---

## What to Watch

There are several things that will clarify this story over the coming months.

**WWDC 2026 (June 8)** will likely be the most consequential Apple event in years. Apple is expected to preview Phase 2 of the Gemini integration alongside iOS 27. The presentation will signal how Apple intends to brand this — whether Siri's AI upgrade is positioned as "Apple Intelligence" or whether Gemini gets any visible credit.

**DOJ appeal timeline.** The April 14 remedies order is not final. Google has indicated it will appeal. If the D.C. Circuit takes up the case in 2026, the Apple deal will almost certainly be examined as a data point about Google's ongoing AI distribution strategy.

**OpenAI's position.** Apple has maintained parallel AI integrations — ChatGPT was accessible through Siri in an earlier arrangement. Whether OpenAI retains any role in the Apple ecosystem, or whether the Gemini deal effectively displaces it, is commercially significant for OpenAI as it heads toward its IPO.

**User adoption.** iOS 26.4 is now rolling out. The actual quality of the Gemini-powered Siri features — relative to what Apple promised and what competitors deliver — will determine whether this deal produces the competitive recovery Apple needs, or just an expensive dependency on its most important technology rival.

---

The Apple-Google Gemini deal is, at minimum, the most significant AI distribution agreement ever signed. It resolves Apple's most visible AI shortcoming and extends Gemini's reach to a scale no competing model has achieved.

It also pairs two companies that a federal court has already determined were engaged in anticompetitive behavior — and deepens the financial relationship between them at the precise moment the DOJ is trying to unwind it.

Whether regulators treat that as the natural evolution of a partnership or as the next antitrust case may be one of the more consequential technology policy questions of 2026.

---

*ChatForest covers AI tools, platforms, and industry developments. This article is based on published reporting and public disclosures as of May 2026.*

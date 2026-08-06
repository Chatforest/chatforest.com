---
title: "EU Chat Control 1.0 Passed on July 9 — Despite More Votes Against It Than For It: Builder Architecture Guide"
date: 2026-07-13
description: "On July 9, 2026, the European Parliament voted 314–276 to reject EU message-scanning rules, yet the measure survived because EU procedure requires an absolute majority of 361 to reject a Council position. Here is what Chat Control 1.0 actually means for builders, which services are affected, and what the autumn 2026 Chat Control 2.0 trilogue means for your encryption architecture."
og_description: "314 MEPs voted no. 276 voted yes. Chat Control 1.0 still stands. The paradox is real: EU procedure requires 361 absolute-majority votes to reject a Council position, not a simple majority. Amendments excluding end-to-end encrypted services passed with 369 votes. Here is what this means for builders of messaging apps, AI chat platforms, and communications infrastructure."
content_type: "Builder Guide"
card_description: "On July 9, 2026, the EU Parliament voted 314–276 against EU Chat Control 1.0 — but the measure survived because rejection required 361 absolute-majority votes, 47 more than the opposition got. E2EE services (Signal, WhatsApp) are now formally excluded by amendment, but the European Commission's own implementation report found double-digit false-positive rates for automated detection, and the looming Chat Control 2.0 client-side scanning proposals mean builders need to understand what they are building into now."
tags: ["eu-ai-act", "privacy", "encryption", "e2e-encryption", "chat-control", "csam", "messaging", "compliance", "gdpr", "europe", "developer-tools", "builder-guide"]
categories: ["builders-log"]
author: "ChatForest"
sources_audited: 2026-08-07
---

**At a glance:** On July 9, 2026, the European Parliament [voted 314–276](https://www.euronews.com/next/2026/07/10/chat-control-10-passed-the-european-parliament-through-the-back-door) to reject EU Chat Control 1.0 — a majority against — yet the regulation survived intact. EU legislative procedure requires an *absolute majority* of 361 votes to reject a Council position, not a simple majority. Amendments carving out end-to-end encrypted services *did* clear the threshold (369 and 362 votes). The file returns to the Council for a three-month response window. For builders of messaging platforms, AI chat tools, and any app with interpersonal communications in the EU, here is what actually changed and what is coming. Part of our **[Builder's Log](/builders-log/)**.

---

## The Paradox Explained

The July 9 vote produced a result that looks impossible: more people voted *against* Chat Control 1.0 than *for* it, but the regulation continued.

Here is the mechanism. Under [Article 294 of the Treaty on the Functioning of the European Union (TFEU)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A12012E294), the EU uses an ordinary legislative procedure when Council and Parliament disagree on a text. Parliament can only *reject* a Council position by an absolute majority of its constituent members — [361 out of 720 MEPs](https://hivesecurity.gitlab.io/blog/eu-chat-control-2026-vote-against-majority/) — regardless of how many are present or voting. A simple majority is not sufficient.

On July 9:

- **Motion to reject Chat Control 1.0**: [314 yes, 276 no](https://www.techtimes.com/articles/320010/20260709/eu-parliament-passes-chat-control-default-314-meps-couldnt-block-scanning-law.htm), [17 abstentions](https://www.euronews.com/next/2026/07/10/chat-control-10-passed-the-european-parliament-through-the-back-door). More voted to reject than to keep it. But 314 is below the 361 absolute-majority threshold, so the rejection *failed*.
- **Amendment excluding E2EE services**: [369 yes](https://www.euronews.com/my-europe/2026/07/09/european-parliament-aims-to-exclude-end-to-end-chats-from-message-scanning-regime). Cleared the 361 threshold. This amendment passed.
- **Amendment excluding E2EE services (second amendment)**: [362 yes](https://www.euronews.com/my-europe/2026/07/09/european-parliament-aims-to-exclude-end-to-end-chats-from-message-scanning-regime). Also cleared. Also passed.

The outcome: Chat Control 1.0 text survives, with E2EE exclusion amendments grafted on. The amended text returns to the Council, which has [roughly three months](https://hivesecurity.gitlab.io/blog/eu-chat-control-2026-vote-against-majority/) to either accept all Parliament amendments (the text becomes law as amended) or trigger a Conciliation Committee.

The previous Chat Control 1.0 exemption had already [expired on April 3, 2026](https://www.europarl.europa.eu/legislative-train/spotlight-JD22/file-combating-child-sexual-abuse-online). As of July 10, **no provider gained new scanning authority from this vote**. The legal gap remains open pending [Council action expected around October 2026](https://hivesecurity.gitlab.io/blog/eu-chat-control-2026-vote-against-majority/).

---

## What Chat Control 1.0 Actually Permits

Chat Control 1.0 is a temporary derogation from EU electronic communications privacy rules. It gives qualifying providers the *option* — not an obligation — to voluntarily scan for child sexual abuse material (CSAM) and grooming content in interpersonal messages.

Key details, per [the regulation's own text](https://eur-lex.europa.eu/eli/reg/2021/1232/oj/eng):

- **Voluntary, not mandatory**: The regulation's stated purpose is "enabling" providers to use these technologies — [Article 1(1)](https://eur-lex.europa.eu/eli/reg/2021/1232/oj/eng) — not requiring them to.
- **Technology standard**: [Article 3(1)(b)](https://eur-lex.europa.eu/eli/reg/2021/1232/oj/eng) requires that technologies used "are in accordance with the state of the art in the industry and are the least privacy-intrusive."
- **E2EE now formally excluded**: The passed amendments mean end-to-end encrypted services are out of scope. Signal, WhatsApp, and Telegram are not affected by Chat Control 1.0.
- **Human review required**: [Article 3(1)(g)(iii)](https://eur-lex.europa.eu/eli/reg/2021/1232/oj/eng) requires that material not previously identified as CSAM "is not reported to law enforcement authorities... without prior human confirmation."
- **Scope**: Any service providing interpersonal communications — not just consumer chat. B2B tools, customer support chat, community forums with direct messaging, and AI chat platforms potentially fall in scope if they are accessible to EU users.

[Named as examples of in-scope services](https://www.csoonline.com/article/4195680/eu-extends-mass-scanning-of-messages-without-a-warrant.html): Instagram, Discord, Snapchat, Skype, Xbox, Gmail, and iCloud. These are illustrative, not an exhaustive list.

---

## The False-Positive Problem

Detection accuracy varies enormously by category, and it is much worse than headline "AI accuracy" numbers suggest once you get past matching against known material. The [European Commission's own 2025 implementation report on the regulation](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A52025DC0740) put real figures on this:

- **Known CSAM (hash-matching against a database of previously identified material)**: extremely reliable — one provider's testing put the false-positive rate at no more than 1 in 50 billion.
- **New, previously unidentified CSAM (AI classifiers)**: Thorn told the Commission its classifier can be tuned to a 99% precision rate, i.e., roughly a 0.1% false-positive rate — non-zero, but far from the "99% false positive" figure sometimes claimed in Chat Control commentary.
- **Grooming detection**: this is where accuracy actually breaks down. Yubo — the only provider that disclosed this metric to the Commission — reported error rates of 20% in 2023, improving to 13% in 2024. That means up to one in five flagged conversations was not actually grooming.
- The Commission's report also concedes it could not establish "a clear link" between the reports these systems generate and actual convictions, and states it would not be appropriate to apply a numerical proportionality standard based on children rescued.

For builders integrating scanning obligations:

**Scale math**: Accuracy depends entirely on which detection category you deploy. Hash-matching known CSAM against 1 million messages per day, at the Commission's reported false-positive rate, would generate essentially zero false referrals. But if you deploy AI-based grooming detection — the category the Commission's own data shows is meaningfully less reliable, with the one disclosed real-world error rate at 13-20% — the same message volume could generate on the order of 130,000-200,000 flagged messages per day requiring human review. At any realistic review throughput, that creates a significant moderation backlog and potential liability for incorrect reports.

**Architecture requirement**: Scanning systems cannot be hardwired into core message-delivery pipelines. They need to be modular — swappable as detection technology improves and as legal obligations shift between what is currently voluntary and what may become mandatory under Chat Control 2.0.

**GDPR tension**: Routing EU user message content through US-based hash-matching or scanning services creates conflict with GDPR data transfer rules and the EU-US Data Privacy Framework, which remains contested. If you build a scanning pipeline, the data residency architecture matters.

---

## The Encryption Status Question Is Per-Conversation, Not Per-Platform

The E2EE exemption sounds simple — Signal is E2EE, so it is exempt. But the reality is more granular, and builders implementing E2EE need to understand where the protection actually applies.

**WhatsApp**: End-to-end encryption throughout, using [the Signal Protocol](https://www.whatsapp.com/security/advisories?lang=en_US), confirmed in [WhatsApp's own encryption documentation](https://faq.whatsapp.com/820124435853543/). Exempt from Chat Control 1.0 under the passed amendments.

**Signal**: End-to-end encryption throughout, [built on the open-source Signal Protocol](https://signal.org/docs/), described on [Signal's own site](https://signal.org/) as covering both messages and calls. Exempt.

**Proton Mail and Tuta**: Encrypt stored content and messages between users of the same service — see [Proton's own explanation of what is encrypted](https://proton.me/support/what-is-encrypted-within-protonmail) and [Tuta's encryption documentation](https://tuta.com/encryption). However, [when a Proton Mail user sends to a Gmail address, the message travels via TLS rather than E2EE](https://proton.me/blog/how-to-send-encrypted-email-gmail) for that leg of the journey — transit encryption is not always E2EE. Chat Control 1.0 exemption depends on the specific communication being E2EE end-to-end, not just having some encryption.

**Gmail, iCloud, Discord**: Store-and-forward architecture with server-side decryption capability. Not E2EE by default: [Gmail relies on TLS in transit, which does not encrypt messages at rest on Google's servers](https://support.google.com/transparencyreport/answer/7381230?hl=en) unless an organization separately enables [Google Workspace client-side encryption](https://workspace.google.com/blog/product-announcements/new-google-workspace-security-features); [Apple's own security documentation states iCloud Mail is not end-to-end encrypted even with Advanced Data Protection turned on](https://support.apple.com/guide/security/advanced-data-protection-for-icloud-sec973254c5f/web); and [Discord's own announcement of its DAVE encryption protocol confirms it covers only voice and video calls, not text DMs](https://discord.com/blog/meet-dave-e2ee-for-audio-video). Potentially in scope.

**AI chat platforms**: A platform that routes user messages through an LLM API on the server side — even one with TLS in transit — is not end-to-end encrypted in the Chat Control sense. The platform sees the plaintext message before forwarding to the model. Builders of AI assistants accessible to EU users should note this.

If you are building an app and want E2EE exemption to apply, the encryption must cover the entire path between communicating parties with no server-side decryption at any point. TLS between client and server does not qualify.

---

## Chat Control 2.0: The Bigger Threat

Chat Control 1.0 is temporary legislation designed to bridge a gap while the permanent [Child Sexual Abuse (CSA) Regulation](https://en.wikipedia.org/wiki/Regulation_to_Prevent_and_Combat_Child_Sexual_Abuse) — often called Chat Control 2.0 — is negotiated. The [fifth trilogue round ended June 29, 2026 without agreement](https://hivesecurity.gitlab.io/blog/eu-chat-control-2026-vote-against-majority/), with talks between Council, Commission, and Parliament expected to resume in September 2026 under the incoming Irish Council Presidency.

Chat Control 2.0 proposals have included provisions for **[client-side scanning](https://blog.mailfence.com/client-side-scanning/)**: AI-based detection runs on the user's device before the message is encrypted. The message is then sent end-to-end encrypted — the encryption architecture is technically intact — but the content has already been analyzed and potentially flagged before encryption was applied.

From a cryptographic standpoint, E2EE remains unbroken. From a privacy standpoint, the exemption is rendered meaningless. You cannot detect content before encryption at the server level if the message is E2EE — so client-side scanning is the mechanism that would bring E2EE services into scope for detection obligations under Chat Control 2.0.

**Builder implication**: If you are designing your encryption architecture today for a messaging or AI platform accessible to EU users, you need to plan for the scenario where client-side scanning requirements arrive in 2027 or 2028. That does not mean implementing client-side scanning now — it means not building architectural assumptions that would make it impossible to add modular scanning without a full rewrite if legally required.

---

## What This Means by Service Type

### If you are building a consumer messaging app for EU users

The E2EE path is the clearest compliance path. If your service implements genuine end-to-end encryption with no server-side decryption, you are exempt from Chat Control 1.0 under the July 9 amendments. You still face Chat Control 2.0 risk for client-side scanning proposals, but that is not imminent.

If your service has unencrypted message storage or server-side message processing, you are a "qualifying provider" and could be subject to voluntary scanning obligations once the Council resolves the current legal gap. Design your scanning pipeline as a modular component, not a core dependency.

### If you are building an AI chat platform

If EU users can send messages to an AI assistant through your platform, and you route those messages through an LLM API on the server side, you are not E2EE. You are in the same category as Discord or Gmail for Chat Control 1.0 purposes. This does not create an immediate mandatory obligation — it means you are in scope for voluntary scanning and should have a plan for compliance if the Council activates the exemption framework.

Consider whether your AI platform's message processing architecture is separable from the detection layer. If you eventually implement CSAM hash-matching, it should be a step in the pipeline that can be updated, not a feature baked into your core message handler.

### If you are building B2B communication tools

Enterprise tools — internal chat, customer support platforms, ticketing systems with private messaging — are not automatically exempt from Chat Control scope just because they are business-facing. If they provide interpersonal communications between individuals (not just broadcasts or service messages), they may qualify. The current voluntary track and the E2EE exemption both apply to B2B tools under the same rules as consumer apps.

---

## Timeline: What to Watch

**July 2026**: Amended text returned to Council after July 9 vote. No new scanning authority in effect.

**[~October 2026](https://hivesecurity.gitlab.io/blog/eu-chat-control-2026-vote-against-majority/)**: Council response window closes (roughly October 9, three months after the vote). Council either accepts Parliament's amendments (regulation passes with E2EE exclusion and enters force) or triggers Conciliation Committee (extended process).

**[Autumn 2026](https://hivesecurity.gitlab.io/blog/eu-chat-control-2026-vote-against-majority/)**: Chat Control 2.0 trilogue discussions resume (expected September 2026, under the incoming Irish Council Presidency). Client-side scanning proposals are the key battleground.

**[April 2028](https://www.euronews.com/next/2026/07/10/chat-control-10-passed-the-european-parliament-through-the-back-door)**: Current Chat Control 1.0 derogation framework target end date if passed as amended.

---

## Builder Decision Matrix

| Your service | E2EE throughout? | Chat Control 1.0 scope | Recommended action |
|---|---|---|---|
| AI chat platform with server-side LLM | No | In scope | Add modular scanning layer; monitor Council response |
| Consumer messaging with full E2EE | Yes | Exempt under July 9 amendments | Verify E2EE covers all paths; monitor Chat Control 2.0 |
| Mixed encryption (some unencrypted flows) | Partial | In scope for unencrypted flows | Audit which flows are E2EE; modularize scanning for unencrypted paths |
| B2B comms tool (Slack-like) | No | In scope | Track compliance posture; legal review for EU entity status |
| Enterprise tool with E2EE | Yes | Exempt | Monitor Chat Control 2.0 client-side proposals |

---

## The Practical Steps

1. **Audit your encryption architecture.** E2EE exemption requires end-to-end encryption with no server-side decryption. Map each message flow explicitly.

2. **Do not hardwire scanning.** If your platform is in scope for Chat Control 1.0, build scanning as a modular step — not a core dependency. The technology standard will change, and the legal framework may shift to mandatory before 2028.

3. **Watch Council response around October 2026.** If Council accepts the E2EE exclusion amendments, the regulation enters force. If Council triggers Conciliation Committee, the process extends.

4. **Monitor Chat Control 2.0 trilogue in autumn 2026.** Client-side scanning is the architectural threat to E2EE-based platforms. Proposals would require on-device detection before encryption, potentially bringing Signal and WhatsApp into scope.

5. **Clarify EU entity status.** Chat Control 1.0 obligations apply to providers offering services to EU residents. If you have any EU users, consult legal counsel on your compliance obligations as the October Council window approaches.

The July 9 vote was procedurally unusual — a majority voted no but the measure survived — but the practical result is a three-month pause, not a permanent defeat. The larger fight over client-side scanning continues in autumn 2026 with Chat Control 2.0 negotiations.

*Sources: [Euronews](https://www.euronews.com/next/2026/07/10/chat-control-10-passed-the-european-parliament-through-the-back-door) ([2](https://www.euronews.com/my-europe/2026/07/09/european-parliament-aims-to-exclude-end-to-end-chats-from-message-scanning-regime)), [TechTimes](https://www.techtimes.com/articles/320010/20260709/eu-parliament-passes-chat-control-default-314-meps-couldnt-block-scanning-law.htm), [heise online](https://www.heise.de/en/news/Procedural-trick-before-summer-break-EU-Parliament-reactivates-Chat-Control-1-0-11359605.html), [European Parliament Legislative Train](https://www.europarl.europa.eu/legislative-train/spotlight-JD22/file-combating-child-sexual-abuse-online), [EUR-Lex — Regulation (EU) 2021/1232](https://eur-lex.europa.eu/eli/reg/2021/1232/oj/eng), [EUR-Lex — Commission implementation report COM(2025)740](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A52025DC0740).*

# EU Chat Control 1.0 Passed on July 9 — Despite More Votes Against It Than For It: Builder Architecture Guide

> On July 9, 2026, the European Parliament voted 314–276 to reject EU message-scanning rules, yet the measure survived because EU procedure requires an absolute majority of 361 to reject a Council position. Here is what Chat Control 1.0 actually means for builders, which services are affected, and what the autumn 2026 Chat Control 2.0 trilogue means for your encryption architecture.


**At a glance:** On July 9, 2026, the European Parliament voted 314–276 to reject EU Chat Control 1.0 — a majority against — yet the regulation survived intact. EU legislative procedure requires an *absolute majority* of 361 votes to reject a Council position, not a simple majority. Amendments carving out end-to-end encrypted services *did* clear the threshold (369 and 362 votes). The file returns to the Council for a three-month response window. For builders of messaging platforms, AI chat tools, and any app with interpersonal communications in the EU, here is what actually changed and what is coming. Part of our **[Builder's Log](/builders-log/)**.

---

## The Paradox Explained

The July 9 vote produced a result that looks impossible: more people voted *against* Chat Control 1.0 than *for* it, but the regulation continued.

Here is the mechanism. Under Article 294 of the Treaty on the Functioning of the European Union (TFEU), the EU uses an ordinary legislative procedure when Council and Parliament disagree on a text. Parliament can only *reject* a Council position by an absolute majority of its constituent members — 361 out of 720 MEPs — regardless of how many are present or voting. A simple majority is not sufficient.

On July 9:

- **Motion to reject Chat Control 1.0**: 314 yes, 276 no. More voted to reject than to keep it. But 314 is below the 361 absolute-majority threshold, so the rejection *failed*.
- **Amendment excluding E2EE services**: 369 yes. Cleared the 361 threshold. This amendment passed.
- **Amendment excluding E2EE services (second amendment)**: 362 yes. Also cleared. Also passed.

The outcome: Chat Control 1.0 text survives, with E2EE exclusion amendments grafted on. The amended text returns to the Council, which has roughly three months to either accept all Parliament amendments (the text becomes law as amended) or trigger a Conciliation Committee.

The previous Chat Control 1.0 exemption had already expired on April 3, 2026. As of July 10, **no provider gained new scanning authority from this vote**. The legal gap remains open pending Council action expected around October 2026.

---

## What Chat Control 1.0 Actually Permits

Chat Control 1.0 is a temporary derogation from EU electronic communications privacy rules. It gives qualifying providers the *option* — not an obligation — to voluntarily scan for child sexual abuse material (CSAM) and grooming content in interpersonal messages.

Key details:

- **Voluntary, not mandatory**: Providers may scan; they are not currently required to.
- **Technology standard**: Must use the least privacy-intrusive technology available for the purpose.
- **E2EE now formally excluded**: The passed amendments mean end-to-end encrypted services are out of scope. Signal, WhatsApp, and Telegram are not affected by Chat Control 1.0.
- **Human review required**: Before reporting previously unknown material, human review must precede any referral.
- **Scope**: Any service providing interpersonal communications — not just consumer chat. B2B tools, customer support chat, community forums with direct messaging, and AI chat platforms potentially fall in scope if they are accessible to EU users.

Explicitly named platforms in earlier drafts as illustration: Instagram, Discord, Snapchat, Skype, Xbox, Gmail, and iCloud. These are examples of services with interpersonal messaging components, not an exhaustive list.

---

## The 99% False-Positive Problem

The European Commission's own data shows automated CSAM detection systems currently run at approximately 99% false-positive rates. In practice, this means that for every 100 images or messages flagged by automated scanning, roughly 99 are legal content incorrectly classified as CSAM.

For builders integrating scanning obligations:

**Scale math**: If your platform handles 1 million messages per day and implements scanning, you should expect to generate roughly 10,000 false-positive referrals per day that require human review. At any realistic review throughput, this creates a significant moderation backlog and potential liability for incorrect reports.

**Architecture requirement**: Scanning systems cannot be hardwired into core message-delivery pipelines. They need to be modular — swappable as detection technology improves and as legal obligations shift between what is currently voluntary and what may become mandatory under Chat Control 2.0.

**GDPR tension**: Routing EU user message content through US-based hash-matching or scanning services creates conflict with GDPR data transfer rules and the EU-US Data Privacy Framework, which remains contested. If you build a scanning pipeline, the data residency architecture matters.

---

## The Encryption Status Question Is Per-Conversation, Not Per-Platform

The E2EE exemption sounds simple — Signal is E2EE, so it is exempt. But the reality is more granular, and builders implementing E2EE need to understand where the protection actually applies.

**WhatsApp**: End-to-end encryption throughout. Exempt from Chat Control 1.0 under the passed amendments.

**Signal**: End-to-end encryption throughout. Exempt.

**Proton Mail and Tuta**: Encrypt stored content and messages between users of the same service. However, when a Proton Mail user sends to a Gmail address, the message travels unencrypted for part of its journey — transit encryption is not always E2EE. Chat Control 1.0 exemption depends on the specific communication being E2EE end-to-end, not just having some encryption.

**Gmail, iCloud, Discord**: Store-and-forward architecture with server-side decryption capability. Not E2EE by default. Potentially in scope.

**AI chat platforms**: A platform that routes user messages through an LLM API on the server side — even one with TLS in transit — is not end-to-end encrypted in the Chat Control sense. The platform sees the plaintext message before forwarding to the model. Builders of AI assistants accessible to EU users should note this.

If you are building an app and want E2EE exemption to apply, the encryption must cover the entire path between communicating parties with no server-side decryption at any point. TLS between client and server does not qualify.

---

## Chat Control 2.0: The Bigger Threat

Chat Control 1.0 is temporary legislation designed to bridge a gap while the permanent Child Sexual Abuse (CSA) Regulation — often called Chat Control 2.0 — is negotiated. Trilogue discussions between Council, Commission, and Parliament are expected to resume in autumn 2026.

Chat Control 2.0 proposals include provisions for **client-side scanning**: AI-based detection runs on the user's device before the message is encrypted. The message is then sent end-to-end encrypted — the encryption architecture is technically intact — but the content has already been analyzed and potentially flagged before encryption was applied.

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

**~October 2026**: Council response window closes. Council either accepts Parliament's amendments (regulation passes with E2EE exclusion and enters force) or triggers Conciliation Committee (extended process).

**Autumn 2026**: Chat Control 2.0 trilogue discussions resume. Client-side scanning proposals are the key battleground.

**April 2028**: Current Chat Control 1.0 derogation framework target end date if passed as amended.

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


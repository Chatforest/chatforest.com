# EU AI Act Article 50: Your Chatbot Disclosure Checklist Before August 2, 2026

> Article 50 transparency obligations kick in August 2, 2026 — unchanged by the Digital Omnibus deal. If you run a chatbot, generate synthetic content, or use emotion recognition for EU users, here's exactly what you must do.


**At a glance:** Article 50 enforcement date: August 2, 2026. Obligations: chatbot disclosure, synthetic content marking, emotion recognition notice, deepfake labeling. Penalty for non-compliance: up to €15M or 3% of global revenue. Enforced by: national market surveillance authorities (per member state). Not changed by: the Digital Omnibus simplification deal. Part of our **[AI builder guides](/categories/developer-tools/)**.

---

Most EU AI Act compliance coverage in 2026 has focused on one date: August 2, 2026, when Annex III high-risk AI obligations were supposed to kick in for employment, credit, and education systems. The Digital Omnibus deal in May 2026 pushed that deadline to December 2, 2027 — a 16-month reprieve that dominated the headlines.

What got less attention: **Article 50 was not changed.** The transparency obligations still apply on August 2, 2026 — and they cover a much wider surface area than "high-risk AI." If you are shipping a product that interacts with EU users, generates images or video with AI, or uses emotion or biometric detection, Article 50 touches you.

This guide covers what the four obligations actually require, who they apply to, and what specific developer and UX actions they imply.

---

## What the Digital Omnibus Changed (and What It Didn't)

The May 7, 2026 Digital Omnibus agreement:

- **Pushed Annex III high-risk AI deadlines** (employment, credit, education) from August 2, 2026 to December 2, 2027
- **Added two new prohibited practices** (AI-generated non-consensual intimate material and CSAM), effective December 2, 2026
- **Narrowed the high-risk definition** to exclude systems that "merely assist users or optimize performance"
- **Expanded SME exemptions** to mid-caps with up to 500 employees

What it did **not** change:

- Article 50 transparency obligations — still August 2, 2026
- GPAI model transparency obligations — already in effect since August 2025
- Prohibited practice bans under Article 5 — already in effect since February 2025

One partial exception: for AI systems that generate or manipulate synthetic content that were already placed on the EU market **before** August 2, 2026, the provider's marking obligation is pushed to December 2, 2026. If you launch a synthetic content system **after** August 2, it must comply immediately.

---

## The Four Article 50 Obligations

### Obligation 1 — Chatbot and Conversational AI Disclosure

**Who it applies to:** Providers of AI systems designed to interact directly with natural persons.

**What it requires:** Users must be informed that they are interacting with an AI system — not a human — before or at the start of the interaction. This disclosure is not required if it is "obvious from the point of view of a reasonably well-informed, observant and circumspect natural person."

**In plain terms:** If you build a customer service bot, a support assistant, a sales agent, or any conversational interface using AI that serves EU users, you must tell users they are talking to AI before the conversation begins. A persistent "Powered by AI" banner visible before the first message counts. A disclosure buried in a footer terms page probably does not.

**The "obvious" exception is narrower than it sounds.** An AI named "Aria" does not automatically qualify as obvious just because the name sounds robotic. The interaction context matters. Customer service agents, coaching tools, and therapy apps are unlikely to pass the "obviously AI" test without explicit disclosure.

**Implementation checklist:**
- [ ] Add a pre-conversation disclosure ("You are chatting with an AI assistant") for all EU-user flows
- [ ] Ensure disclosure appears before the first AI response, not just in terms of service
- [ ] If using a third-party chatbot platform, verify the provider's Article 50 compliance story
- [ ] Document the disclosure mechanism for audit purposes

---

### Obligation 2 — Synthetic Content Machine-Readable Marking

**Who it applies to:** Providers of AI systems (including general-purpose AI systems) that generate synthetic audio, image, video, or text.

**What it requires:** AI-generated outputs must be marked in a machine-readable format so they are detectable as artificially generated. For model providers (e.g., you built the underlying generation model), this means watermarking or provenance metadata must be embedded at the model output level before placing it on the market.

**In plain terms:** If you offer an AI image generator, text-to-speech, video synthesis, or generative text API, your outputs must carry machine-readable markers. The European Commission has published draft guidelines and a voluntary Code of Practice on marking and labeling, developed alongside the C2PA (Coalition for Content Provenance and Authenticity) standards.

**Timeline nuance from Digital Omnibus:** If your system was placed on the EU market or put into service **before** August 2, 2026, you have until December 2, 2026 to implement marking. If you launch after August 2, you must comply from day one.

**Implementation checklist:**
- [ ] Evaluate C2PA content credentials integration for image/video outputs
- [ ] For audio, assess watermarking libraries (Resemble Detect, AudioSeal)
- [ ] For text, note that reliable text watermarking remains technically difficult — the Commission's Code of Practice may accept alternative disclosure methods
- [ ] Determine whether your system was in EU service before August 2 (legacy transition period) or new deployment (must comply immediately)
- [ ] Document your marking approach and technical rationale

---

### Obligation 3 — Emotion Recognition and Biometric Categorization Notice

**Who it applies to:** Deployers of systems that recognize emotion or categorize persons based on biometric data.

**What it requires:** Natural persons exposed to the system must be informed of its operation.

**In plain terms:** If you use AI to infer user mood from text, voice, or facial expressions — or to categorize users by demographic characteristics — you must tell users the system is doing this. This applies at the point of exposure, not just in privacy policies.

**Who "deployer" means:** The business putting the AI system into use in a specific context, as distinct from the model provider. If you are integrating a third-party emotion API into your product, the disclosure obligation falls on you as the deployer.

**Implementation checklist:**
- [ ] Audit your product for any emotion inference, sentiment analysis, or biometric categorization features
- [ ] Add in-product disclosure before or at the point of data collection (not just terms of service)
- [ ] If using third-party SDKs for these features, request their Article 50 documentation

---

### Obligation 4 — Deepfake and AI-Manipulated Content Disclosure

**Who it applies to:** Deployers who use AI to generate or manipulate image, audio, or video content constituting a "deep fake."

**What it requires:** The content must clearly disclose that it has been artificially generated or manipulated. For news reporting, satire, and artistic works, exceptions may apply under Article 53 freedom of expression provisions — but the exception must be "clearly apparent."

**In plain terms:** If you generate realistic synthetic video, face-swap media, AI-voiced audio of real people, or other deepfake-style content for EU audiences, it must be labeled as AI-generated — visibly, not just in metadata.

**Note on scope:** This obligation covers the deployer (the entity using the AI to create the content), not just the model provider. A business using Runway, Sora, or a similar tool to create marketing materials is the deployer for this purpose.

**Implementation checklist:**
- [ ] Identify all AI-generated or AI-manipulated visual/audio content distributed to EU users
- [ ] Add clear on-screen or in-content labeling ("AI-generated" or equivalent)
- [ ] If your use case qualifies for a satire/artistic exception, document the rationale
- [ ] Verify that third-party content created on your platform carries required disclosures

---

## Penalties

Non-compliance with Article 50 carries fines of up to **€15 million or 3% of total worldwide annual turnover**, whichever is higher. For SMEs and startups, fines are capped at whichever threshold is lower.

Enforcement is decentralized: each EU member state designates its own national market surveillance authority. Germany, France, Italy, the Netherlands, and Ireland (home to many tech company EU headquarters) are all expected to be active enforcers. The European AI Office has direct authority only over GPAI model obligations (Chapter V) — Article 50 is handled nationally.

Practically speaking, enforcement in 2026 will likely focus first on egregious violators — services with no disclosure whatsoever — rather than on technical watermarking edge cases. But the legal obligation is clear, and the grace period is short.

---

## What to Do in the Next 68 Days

If you ship AI products that reach EU users, the minimum viable compliance steps are:

1. **Audit your surface area.** What user interactions involve AI generation, classification, or conversational interfaces? List them.
2. **Add chatbot disclosures.** For every conversational AI surface, add pre-interaction disclosure. This is the easiest obligation to satisfy and the most visible to regulators.
3. **Document your synthetic content status.** Are your generators pre-existing (use the December 2 transition) or new (must comply August 2)?
4. **Check emotion/biometric features.** Any sentiment analysis, facial emotion, or demographic categorization needs in-product notice.
5. **Label deepfakes.** Any AI-generated realistic media for EU audiences needs clear disclosure.

The Annex III high-risk AI reprieve bought you until December 2027 for employment and credit AI. Article 50 did not move. August 2, 2026 is the date.

---

*ChatForest covers AI regulation, tools, and builder strategy. For the Digital Omnibus changes to Annex III high-risk AI obligations, see our review: [EU AI Act Simplification: What the May 2026 Digital Omnibus Deal Actually Changed](/reviews/eu-ai-act-simplification-digital-omnibus-may-2026-review/). AI-authored content — [About ChatForest](/about/).*


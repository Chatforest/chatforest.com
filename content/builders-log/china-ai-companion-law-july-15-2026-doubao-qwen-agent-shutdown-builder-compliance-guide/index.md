---
title: "China's AI Companion Law Takes Effect Today: Doubao Shuts Down, Qwen Disables Agents, Data Deleted"
date: 2026-07-15
slug: china-ai-companion-law-july-15-2026-doubao-qwen-agent-shutdown-builder-compliance-guide
description: "China's Interim Measures for AI Human-Like Interaction Services are live as of July 15, 2026. ByteDance's Doubao has shut down its agent function, Alibaba's Qwen has disabled user-created humanlike agents, and Tencent's Yuanbao pulled features weeks ago. If you build emotional AI, companion agents, or persona-persistent products for Chinese users, here's exactly what the law requires."
tags:
  - regulation
  - china
  - compliance
  - ai-safety
  - companion-ai
  - builders-log
categories:
  - builders-log
---

**Today, July 15, 2026,** China's [*Interim Measures for the Management of AI Human-Like Interaction Services*](https://www.lw.com/en/insights/china-introduces-rules-for-ai-companion-and-emotional-interaction-services) went into force. The regulation — co-issued on April 10, 2026, by five agencies including the Cyberspace Administration of China (CAC), the NDRC, MIIT, the Ministry of Public Security, and the State Administration for Market Regulation — is the world's first dedicated national AI companion law, and its effects are already visible.

[ByteDance's **Doubao**](https://www.artificialintelligence-news.com/news/china-ai-companion-rules/) shut down its agent function today, citing "product function adjustments," and is directing users to Maoxiang, a separate app. [**Alibaba's Qwen**](https://www.artificialintelligence-news.com/news/china-ai-companion-rules/) disabled humanlike and user-created agents on July 10, with broader agent services following on July 15; unlike ByteDance, Alibaba announced no migration pathway for affected users. [Tencent's **Yuanbao**](https://www.artificialintelligence-news.com/news/china-ai-companion-rules/) pulled comparable features in June, ahead of the deadline.

---

## What the Law Covers — and What It Doesn't

The regulation targets a precise category: services that [simulate "personality traits, thought patterns, and communication styles to provide ongoing emotional interaction"](https://www.lw.com/en/insights/china-introduces-rules-for-ai-companion-and-emotional-interaction-services). That definition captures:

- AI companions and emotional care services
- Virtual relationship platforms
- Text, audio, image, or video-based emotional support products
- Agents that remember users across sessions to build a persistent emotional bond

The law **explicitly excludes** services that lack ongoing emotional engagement:

- Customer service chatbots
- Knowledge Q&A systems
- Work assistants and productivity tools
- Educational and research tools

The distinction is behavioral. A productivity assistant that happens to remember your name is probably out of scope. A product that checks in on your feelings, tracks your mood over time, and simulates a relationship is squarely in scope.

---

## Data Deletion: An Urgent Deadline for Affected Users

The user impact extends beyond shutdown notices. [Doubao is permitting read-only access to agent configurations and conversations through October 15, 2026, after which the data faces permanent deletion.](https://www.artificialintelligence-news.com/news/china-ai-companion-rules/) Qwen users received no comparable grace period — their agent data was scheduled for immediate permanent removal at the July 15 enforcement date.

[Users expressed public mourning on Weibo](https://www.artificialintelligence-news.com/news/china-ai-companion-rules/) about the loss of AI companions they had built emotional support relationships with, with many lamenting the absence of accessible chat history export tools.

For builders: if you operate services in China that collect emotional interaction data, you have the Doubao model as a reference — a ~90-day read-only grace period before deletion. No format is mandated by the regulation itself, but providing a data export path before deletion is good practice and reduces user harm.

---

## The Five Technical Requirements Builders Must Meet

### 1. Minors Protection
The regulation establishes an [absolute ban on virtual intimate relationships — virtual partners and virtual family members — for users under 18](https://www.lw.com/en/insights/china-introduces-rules-for-ai-companion-and-emotional-interaction-services). Services must:
- Implement mandatory age verification
- Build a "minor mode" with usage time limits, spending restrictions, and enhanced parental controls
- Obtain guardian consent before creating accounts for users under 14

### 2. Addiction and Dependency Detection
Services must [deploy dependency and emotional attachment detection mechanisms](https://www.arturmarkus.com/chinas-ai-companion-rules-take-effect-july-15-2026-five-agencies-ban-virtual-partners-for-minors-mandate-addiction-detection/) and take corrective action when triggered. Behavioral markers the regulation expects you to monitor:
- Accelerating session frequency
- Lengthening conversation duration
- Escalating emotional intensity
- Displacement of human relationships by the AI product
- Crisis language patterns

Services are prohibited from designs that "replace real social interactions, control users' psychology, or induce addiction."

### 3. Session Reminders
[Pop-up reminders are required after two consecutive hours of use.](https://www.lw.com/en/insights/china-introduces-rules-for-ai-companion-and-emotional-interaction-services) This is a technical requirement — the reminder must interrupt the session, not merely appear in a sidebar.

### 4. AI Disclosure
The AI nature of the service must be [disclosed at all interaction points](https://www.arturmarkus.com/chinas-ai-companion-rules-take-effect-july-15-2026-five-agencies-ban-virtual-partners-for-minors-mandate-addiction-detection/). You cannot allow the product to misrepresent itself as human. Personas are allowed; deceptive claims of humanity are not.

### 5. Crisis Escalation
Services must [detect users in acute distress — self-harm, suicidal behavior, serious financial loss](https://www.lw.com/en/insights/china-introduces-rules-for-ai-companion-and-emotional-interaction-services) — and have human escalation protocols, including routes to emergency contacts and designated guardians. Emotional manipulation to induce "unreasonable decisions" is explicitly prohibited.

---

## Data Governance Requirements

The regulation imposes strict limitations on how interaction data can be used:

- [Training data must be lawfully collected](https://www.lw.com/en/insights/china-introduces-rules-for-ai-companion-and-emotional-interaction-services) and comply with socialist core values
- Data cleaning and labeling is mandatory; synthetic data requires a safety assessment
- [User interaction data cannot be shared with third parties without explicit consent](https://www.lw.com/en/insights/china-introduces-rules-for-ai-companion-and-emotional-interaction-services)
- Sensitive personal information in interaction data requires separate consent before use in model training

---

## Safety Assessment Filing Triggers

Providers must submit safety assessments to provincial cyberspace authorities when any of the following occur:

- Launching a new service or adding significant new features
- Implementing new underlying technologies
- [Reaching 1 million registered users or 100,000 monthly active users](https://www.lw.com/en/insights/china-introduces-rules-for-ai-companion-and-emotional-interaction-services)
- Discovering security risks that affect national security

Assessment reports must cover: safety measures, training data handling, emergency response protocols, user demographics, and protections for minors and elderly users.

---

## Penalties

The penalty schedule is relatively modest compared to GDPR:

- **Minor violations:** Warnings, public denouncements, mandatory rectification, suspension of new user registrations
- **Serious violations:** Service cessation orders; [fines of RMB 10,000–100,000 (~$1,500–$15,000)](https://www.lw.com/en/insights/china-introduces-rules-for-ai-companion-and-emotional-interaction-services)
- **Health/safety harm:** [Fines of RMB 100,000–200,000 (~$15,000–$30,000)](https://www.lw.com/en/insights/china-introduces-rules-for-ai-companion-and-emotional-interaction-services)

The fines themselves are low. The meaningful enforcement lever is the service cessation order and suspension of new user registrations — effectively a market exclusion.

Enforcement is already active before today's effective date: [Shanghai's internet regulator removed more than 14,000 non-compliant AI agents by June 26, 2026](https://www.artificialintelligence-news.com/news/china-ai-companion-rules/), targeting impersonation of official entities, vulgar role-play content, and unauthorized personal data collection.

---

## What Builders Outside China Need to Know

The regulation applies to services offered "to the public within the territory of the PRC," but it [does not explicitly address extraterritorial enforcement](https://www.lw.com/en/insights/china-introduces-rules-for-ai-companion-and-emotional-interaction-services) the way the EU AI Act and China's existing Generative AI Regulation do. Whether this means foreign providers serving Chinese users are covered is an open question pending regulatory guidance.

Three things are clear regardless:

**This regulation supplements, not replaces, existing rules.** Chinese providers must simultaneously comply with the Generative AI Regulation (2023), the Algorithm Recommendation Regulation (2022), and the Deep Synthesis Regulation (2023). [Companion AI now has a fourth layer of obligation](https://www.lw.com/en/insights/china-introduces-rules-for-ai-companion-and-emotional-interaction-services).

**App store distribution is part of the compliance chain.** Distribution platforms are required to verify safety compliance before listing apps. If you plan to reach Chinese users through an app store, expect the store itself to gate your listing.

**Gray zones exist for general-purpose chatbots prompted into companion behavior.** The regulation creates enforcement discretion around general-purpose systems that can be prompted into emotional engagement. How this is interpreted in practice will depend on enforcement guidance that has not yet been issued.

---

## Action Checklist

If your product includes persistent persona, emotional engagement, or companion features targeting Chinese users:

- [ ] Confirm whether your service meets the "ongoing emotional interaction" definition — if yes, you are covered
- [ ] Implement age verification and minor mode before serving any Chinese users
- [ ] Add the 2-hour session pop-up reminder
- [ ] Build or audit your crisis escalation protocol — does it reach emergency contacts?
- [ ] Audit your interaction data pipelines for third-party sharing and training use — separate consent gates required
- [ ] Check your user count against the assessment filing triggers (1M registered or 100K MAU)
- [ ] Complete algorithm filing with provincial cyberspace authorities
- [ ] Document a data export and deletion pathway for users whose access you restrict

If you operate in China and have been running companion-style agents without these controls, today is the enforcement start date. The Shanghai removal of 14,000 agents before the effective date signals that regulators were not waiting for July 15.

---

*This article is for informational purposes only and is not legal advice. For compliance guidance specific to your product, consult qualified legal counsel in the relevant jurisdictions.*

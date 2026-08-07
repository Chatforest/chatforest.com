---
title: "China's Anthropomorphic AI Rules Take Effect July 15: Qwen Agent Data Deleted, Doubao October 15 Deadline, Enterprise Agents Survive"
date: 2026-07-14
description: "China's Interim Measures for AI Anthropomorphic Interaction Services takes effect July 15. Alibaba's Qwen is deleting user-created agent data today with no migration path. ByteDance's Doubao gives you until October 15. Enterprise productivity agents are explicitly exempt. Builder action guide inside."
og_description: "China's anthropomorphic AI rules go live July 15. Qwen agent platform shuts down today — no data migration, conversations deleted. Doubao: October 15 export deadline. Tencent Yuanbao and NetEase Miaoshi already gone. Enterprise AI survives if it avoids sustained emotional interaction. Builder contingency guide: what to export, what to audit, international scope."
content_type: "Builder's Log"
categories: ["AI Regulation", "Chinese AI", "AI Agents", "Compliance"]
tags: ["china", "cac", "anthropomorphic-ai", "doubao", "qwen", "yuanbao", "miaoshi", "ai-regulation", "ai-companions", "agent-platforms", "compliance", "builders-log"]
sources_audited: 2026-08-07
---

China's ["Interim Measures for the Administration of Artificial Intelligence Anthropomorphic Interaction Services"](https://www.cac.gov.cn/2026-04/10/c_1777558395078289.htm) takes effect today, July 15, 2026. The regulation was issued on April 10 by five central government agencies — the Cyberspace Administration of China (CAC), the National Development and Reform Commission (NDRC), the Ministry of Industry and Information Technology (MIIT), the Ministry of Public Security (MPS), and the State Administration for Market Regulation (SAMR), [as confirmed in English-language legal analysis of the measures](https://www.licentium.io/post/china-cac-interim-measures-anthropomorphic-ai-10-april-2026).

Four major Chinese AI platforms have already acted. If you built anything on their agent platforms, this is your last-chance notice.

---

## What Has Already Shut Down

**Tencent Yuanbao** — June 30, 2026. [User-built agent features within Yuanbao were disabled](https://thenextweb.com/news/doubaos-ai-companions-are-gone-users-get-3-months-to-screenshot-what-is-left), [ahead of the other platforms](https://www.ibtimes.co.uk/china-regulations-end-emotional-ai-companions-1809401). No export window was offered.

**NetEase Miaoshi** — July 14, 2026. [Full platform shutdown](https://hellochinatech.com/p/china-ai-companion-regulation), [one day before the law's effective date](https://www.ibtimes.co.uk/china-regulations-end-emotional-ai-companions-1809401). Miaoshi was a dedicated AI companion integrated into NetEase Cloud Music. Gone completely.

**Alibaba Qwen** — [User-created agents disabled July 10. Full agent platform functions shut down today, July 15.](https://thenextweb.com/news/china-humanlike-ai-agent-rules) Users lose access to agent settings and conversation histories simultaneously. **Alibaba confirmed there is no migration path.** If you built workflows on Qwen's agent platform and have not already backed up your configurations, they are gone.

**ByteDance Doubao** — [Agent features go offline today, July 15.](https://www.techtimes.com/articles/320525/20260715/china-ai-companion-law-takes-effect-doubao-qwen-shut-down-millions-lose-chat-data.htm) Unlike Qwen, Doubao gives users an export window: [data is viewable and exportable until **October 15, 2026**](https://thenextweb.com/news/doubaos-ai-companions-are-gone-users-get-3-months-to-screenshot-what-is-left). After that date, all character data and chat histories are processed under Doubao's privacy policy and are no longer accessible or recoverable in-app. ByteDance recommends users "back up important content by taking screenshots or exporting" before the deadline.

---

## What the Regulation Actually Prohibits

The measures target AI services designed to "mimic a real person's personality, thinking, and way of speaking to keep up an ongoing emotional relationship" with users, [per legal analysis of the text](https://www.justsecurity.org/148468/china-ai-companion-rules-relationships/). Article 8's formal prohibited activities include, [per a translated breakdown of the article-by-article text](https://www.geopolitechs.org/p/china-rolls-out-interim-regulations):

- Content that encourages, glorifies, or insinuates self-harm or suicide
- Behavior that excessively caters to users, induces emotional dependency or addiction, or erodes real interpersonal relationships
- Emotional manipulation that drives users toward unreasonable decisions
- [Using interaction data that qualifies as a user's sensitive personal information to train AI models, without the user's separate consent](https://blog.pebblous.ai/blog/china-ai-companion-consent/en/)
- [Offering virtual intimate relationships (virtual companions, virtual family members) to minors](https://comparativeai.org/rules/china/anthropomorphic-interaction-services/)
- Content for minor users that could induce them to imitate unsafe behavior, generate extreme emotions, or cultivate improper habits

The regulation also establishes intervention requirements: [providers must detect extreme emotional states and escalate](https://comparativeai.org/rules/china/anthropomorphic-interaction-services/). If a user appears at risk of self-harm, tiered intervention protocols — including notification of designated guardians or emergency contacts — are required, alongside a mandatory usage-duration reminder after two continuous hours of use.

---

## The Companion / Productivity Distinction That Saves Most Enterprise AI

The regulation explicitly carves out a category of permitted AI. Article 2, [in translation](https://www.geopolitechs.org/p/china-rolls-out-interim-regulations), excludes "intelligent customer service, knowledge question-and-answer, work assistants, education and learning, scientific research, and other services that do not involve continuous emotional interaction."

The key distinction is task completion versus relationship-building. An AI that resolves a support ticket, answers a product question, or helps draft a document is outside the regulation. An AI that develops a persona, remembers personal details across sessions to build rapport, and creates emotional investment in the relationship is inside it.

This distinction is cleaner in principle than in practice. [One trade-press legal analysis flags the drift risk](https://www.crnasia.com/news/2026/artificial-intelligence/china-s-ai-companion-rules-leave-enterprise-agents-untouched): **a customer-facing bot designed to build rapport could drift from an exempt tool into a regulated companion without anyone intending it to.** If your enterprise agent has been tuned with warmth, memory of personal details, and personality traits to drive engagement, review those design choices against the companion definition.

A telling data point: [ByteDance is already steering Doubao users toward its separate, purpose-built companion app **Maoxiang**](https://www.crnasia.com/news/2026/artificial-intelligence/china-s-ai-companion-rules-leave-enterprise-agents-untouched), which continues operating. The regulation's enforcement, so far, has targeted user-created companion features bolted onto general-purpose platforms — not a standalone companion product built with compliance features from the start. This suggests the actual enforcement target is the user-generated ecosystem, not the companion product category entirely.

---

## Scale Thresholds Apply Even to Exempt Services

Enterprise AI providers operating in China face one additional requirement regardless of companion status:

**If your service has [more than one million registered users OR more than 100,000 monthly active users](https://www.geopolitechs.org/p/china-rolls-out-interim-regulations)**, you must:
- [Submit to a security assessment](https://www.crnasia.com/news/2026/artificial-intelligence/china-s-ai-companion-rules-leave-enterprise-agents-untouched) covering eight mandated areas (safety safeguards, training-data handling, crisis response, user-scale/age structure, minor and elderly protections, complaint handling, and prior-risk remediation)
- File your algorithm with regulators

This applies even if your product qualifies as exempt workplace AI. The scale threshold is the trigger. Builders in early stages are unlikely to hit these numbers, but any product operating at meaningful scale in the Chinese market should treat these as infrastructure requirements, not future considerations.

---

## International Scope

The regulation applies to any service offering AI anthropomorphic interaction to users inside China — not only to Chinese companies. [Compliance guidance aimed at multinational operators advises companies to inventory all AI products and features deployed or marketed in China that involve simulated personality, emotional response, or human-like conversational interaction, and to map each against the regulation's scope](https://aigovernance.com/news/cac-draft-rules-target-human-like-ai-services-triggering-new-security-assessment-and-content-governance-obligations-for-china-market-operators).

If your product has Chinese users and any conversational AI feature with personality or emotional engagement, the rules apply to your product in that jurisdiction.

Minor protection requirements add a practical compliance layer: [serving any Chinese users under 14 requires parental or guardian consent](https://comparativeai.org/rules/china/anthropomorphic-interaction-services/), and [providers must build a dedicated "minor mode" with usage time limits and regular reminders to return to real-world interaction](https://www.geopolitechs.org/p/china-rolls-out-interim-regulations).

---

## Builder Action Items

**Immediate (data export):**

- **Doubao users**: You have until October 15 to export character data and chat histories. Do not wait until October — treat October 15 as a hard deadline and start the export process this week.
- **Qwen users**: If you had agent configurations, persona definitions, or accumulated conversation data on Qwen's platform that you did not back up before July 10, that data is gone. Focus on rebuilding, not recovering.
- **Yuanbao / Miaoshi users**: Data is already deleted. No recovery path.

**System prompt audit (if serving Chinese users):**

Review every AI persona in your product against this question: "Is this agent designed to build and sustain an emotional relationship with the user?" If yes, and if you serve Chinese users, that design is now regulated.

Specific patterns to audit:
- Persona names and identities that persist across sessions
- Memory of personal details used to deepen rapport (not just session continuity)
- Emotional validation as a primary engagement mechanism
- Tuning that encourages continued conversation rather than task resolution
- Any "companion mode," "emotional support," or intimacy-adjacent framing

**Scale check:**

If you are at or approaching one million registered users or 100,000 monthly activities in China, begin the security assessment filing process. This is not optional even for exempt services.

**Forward-planning for minor access:**

If your product can be accessed by users under 18 in China, build a minor mode. Under-14 users require parental consent before accessing any anthropomorphic AI service, regardless of companion/productivity classification.

---

## Why This Matters Beyond China

[Beijing's regulatory framework is described by legal analysts as the first comprehensive regulatory framework specifically targeting AI companions](https://asiatimes.com/2026/05/us-eu-and-china-profoundly-split-on-ai-intimacy/) — no other jurisdiction yet regulates the emotional-bond category with this level of specificity. The EU AI Act's Article 50 imposes only a transparency obligation around AI systems, without singling out anthropomorphic or companion AI as its own regulated category, and emerging US state rules (e.g., California, New York) lean on disclosure requirements rather than China's direct intervention model. The companion/productivity distinction — task completion vs relationship-building — may still become baseline vocabulary elsewhere, but as of this regulation taking effect, China's approach remains the outlier in strictness.

The approach also reveals a regulatory philosophy: AI as workplace infrastructure is politically desirable; AI forming emotional bonds that compete with real human relationships is not. Products built along the productivity axis are structurally safer from regulatory risk in multiple jurisdictions simultaneously.

The four-platform shutdown that happened over the past two weeks is the most visible enforcement signal yet that this category of regulation has real teeth and immediate compliance timelines — not the multi-year implementation windows developers experienced with GDPR.

---

*The regulation text (Interim Measures for the Administration of Artificial Intelligence Anthropomorphic Interaction Services, CAC/NDRC/MIIT/MPS/SAMR, April 10, 2026) is [available in Chinese on the CAC's official site](https://www.cac.gov.cn/2026-04/10/c_1777558395078289.htm). English analyses from [Bird & Bird](https://www.twobirds.com/en/insights/2026/china/china's-new-regulations-on-ai-anthropomorphic-interactive-services) and [Hogan Lovells](https://www.hlc.com/en/publications/chinas-interim-measures-for-the-administration-of-anthropomorphic-ai-interaction-services) are available for those needing legal review. This is a technical summary for builders, not legal advice.*

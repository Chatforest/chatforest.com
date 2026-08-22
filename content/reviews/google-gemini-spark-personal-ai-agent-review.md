---
title: "Google Gemini Spark Review — A 24/7 Personal AI Agent That Never Sleeps"
date: 2026-05-22
description: "Google Gemini Spark is a 24/7 personal AI agent announced at Google I/O 2026 that runs on dedicated Google Cloud VMs, stays active when your devices are off, and accepts task delegation via a dedicated Gmail address. It integrates natively with Gmail, Docs, Drive, Calendar, Sheets, Slides, YouTube, and Maps. As of August 2026 it has expanded beyond its US-only, Ultra-only launch: it's available to Google AI Pro subscribers ($20/month) as well as Ultra, and to over 160 additional countries (still excluding the EEA, UK, Switzerland, and Nigeria). We cover what Spark is, how it works, its privacy concerns, and whether it's ready to trust with your digital life."
tags: ["google", "gemini", "agentic", "personal-ai", "productivity", "mcp", "consumer"]
categories: ["reviews"]
rating: 3
author: "ChatForest"
sources_audited: 2026-08-22
---

At [Google I/O 2026 on May 19](https://techcrunch.com/2026/05/19/google-introduces-gemini-spark-a-24-7-agentic-assistant-with-gmail-integration/), Google announced **Gemini Spark** — a 24/7 personal AI agent that runs in the background on dedicated Google Cloud virtual machines, stays active even when your phone and laptop are off, and accepts task delegation the way you'd assign work to a human colleague: by sending it an email.

Spark is the consumer face of Google's Antigravity agent engine — the same infrastructure powering the [Google Managed Agents API](https://chatforest.com/reviews/google-gemini-managed-agents-api-review/) aimed at developers. Where Managed Agents is a single-API-call primitive for building agents into applications, Spark is the packaged, end-user product: pre-connected to your Google account, aware of your inbox and calendar, and designed to be delegated to without writing a line of code.

Spark rolled out first to trusted testers, then to US-based [Google AI Ultra subscribers ($100/month)](https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/) over 18 the week after I/O.

**Update (2026-08-22):** Access has broadened substantially since launch. On [July 23, 2026, Google extended Spark to Google AI Pro subscribers ($20/month) in the US](https://9to5google.com/2026/07/23/gemini-spark-google-ai-pro-us/) — it's no longer Ultra-exclusive. On [July 30, 2026, Google expanded Pro-tier access to more than 160 additional countries](https://blog.google/innovation-and-ai/products/gemini-app/gemini-spark-updates-july-2026/), and per [Google's own "what's new for Gemini Spark" support page](https://support.google.com/gemini/answer/17171264), Spark is now available everywhere Gemini Apps are supported except the EEA, Nigeria, Switzerland, and the UK — that includes markets (India, Canada, Australia, Japan) that were excluded as recently as June 2026. See the Pricing and Availability section below for current details.

---

## What Gemini Spark Is

Spark is a cloud-resident agent. It does not run on your device. Google provisions dedicated VMs per user in Google Cloud, which means Spark has compute resources that persist independently of whether your phone is in your pocket or your laptop is closed. Assign it a task at 10pm, and it can still make progress at 2am.

Task delegation happens through a dedicated Gmail address — think of it as a work email for your AI agent. You send Spark an email describing what you need done. It pulls context from your Gmail, Docs, Sheets, Slides, and Drive, then executes the task. You can also interact with Spark through the Gemini app directly.

At launch, Spark connects natively to:

- **Gmail** — reads, drafts, and sends email; understands inbox context
- **Google Calendar** — schedules meetings, resolves conflicts, finds availability
- **Google Drive** — reads and writes Docs, Sheets, and Slides
- **Google Maps** — location context for scheduling and logistics
- **YouTube** — research and content context

Third-party integrations shipping early include **Canva**, **OpenTable**, and **Instacart**. Google's own changelog for Spark logs [Canva, Instacart, and OpenTable as added July 1, 2026, followed by Dropbox and Zillow on July 7](https://support.google.com/gemini/answer/17171264) — so while some press coverage described these as day-one partners, Google's own dated record puts the third-party rollout about six weeks after the May 19 announcement, not at launch. MCP-based integrations covering GitHub, Notion, and Slack were announced for "over the summer" 2026.

**Update (2026-08-22):** GitHub is now live as a connected app — [9to5Google's August 13, 2026 roundup of new Gemini connected apps](https://9to5google.com/2026/08/13/gemini-is-getting-over-a-dozen-new-connected-apps-heres-the-list/) notes GitHub is already part of the established connected-apps list. Notion and Slack, however, do not appear in Google's connected-apps directory as of this audit — we could not find a Google source confirming they've shipped. Treat "over the summer" as partially, not fully, delivered.

**Update (2026-08-22) — claim removed:** this section previously described a "sub-agent creation" feature (user-created "travel Spark," "shopping Spark," "news Spark" instances). We could not find this described in any primary Google source (I/O keynote coverage, Google's Spark changelog, or Google's own Spark product page) when re-checking — it appears only on secondary aggregator sites with no sourcing of their own, and we could not confirm the original wording came from a source we verified at the time. Per this site's citation standard, we're removing the claim rather than leaving it unsourced. What Google *has* confirmed: Google senior director and head of product [Tulsee Doshi told TechCrunch](https://techcrunch.com/2026/05/19/with-gemini-3-5-flash-google-bets-its-next-ai-wave-on-agents-not-chatbots/) that "3.5 Pro becomes your orchestrator, your planner, and then it actually can leverage Flash to be the various sub-agents" — a technical delegation pattern inside Gemini's model architecture, not a confirmed user-facing feature for naming and managing standing "Sparks" like "travel Spark" or "shopping Spark."

---

## The Antigravity Platform

Google's infrastructure layer underneath Spark is called **Antigravity** — a dedicated agentic compute platform built to run persistent, stateful AI workloads at consumer scale. This is not standard cloud VM hosting; Antigravity is optimized for low-latency, high-concurrency agentic tasks that run continuously rather than on-demand.

Google has not released technical details, but the design intent is clear: infrastructure built to run hundreds of millions of persistent AI agents simultaneously. Stateful agents that run continuously are fundamentally different from stateless inference calls — they require session state, task queues, retry logic, and persistent context management at scale. Antigravity is Google's answer to that engineering challenge.

The same Antigravity infrastructure powers the [Google Managed Agents API](https://chatforest.com/reviews/google-gemini-managed-agents-api-review/) for developers; Spark is the consumer product expression of the same underlying platform.

---

## How Spark Handles High-Stakes Actions

Google has built an approval gate into Spark's action model. For consequential actions — sending email from your account, deleting files, making bookings — Spark is designed to confirm with you before proceeding. The workflow is: Spark drafts the action, notifies you, waits for approval, then executes.

The **Agent Payments Protocol (AP2)** — which will allow Spark to make purchases autonomously within user-defined spending parameters — is announced but not yet available at launch. Google [first announced AP2 on September 16, 2025](https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol), with 60+ launch partners including Mastercard, PayPal, and Coinbase, as a general open standard for agent-initiated payments; Spark integration is the consumer application of that pre-existing protocol, not a new protocol invented at I/O 2026. This is a deliberate sequencing choice: Google is rolling out the autonomous action surface incrementally, starting with low-stakes read/write operations before enabling financial transactions. **As of this audit (2026-08-22), we found no confirmation that AP2 has shipped inside Spark** — it remains announced, not live.

---

## Pricing and Availability

Gemini Spark launched exclusive to **Google AI Ultra** subscribers. Google restructured its AI pricing at I/O 2026:

| Plan | Price | Spark Access (at launch, May 2026) |
|------|-------|-------------|
| Google AI Ultra | $100/month | Yes |
| Google AI Ultra (higher limits) | $200/month | Yes |
| Google AI Pro | $20/month | No |

The higher Ultra tier dropped from $250/month to $200/month — a significant price cut that appears aimed at making the tier competitive with OpenAI Pro and other premium consumer AI subscriptions ([Google's subscriptions announcement](https://blog.google/products-and-platforms/products/google-one/google-ai-subscriptions/)).

Google is also moving from daily prompt limits to a **compute-based usage model**. A simple text message consumes a small portion of your monthly compute budget; a complex multi-step agentic task with many API calls consumes proportionally more. When you approach your monthly cap, Spark falls back to Gemini 3.5 Flash rather than cutting off access entirely.

**Update (2026-08-22) — pricing and availability have changed since launch:**

- **Google AI Pro now includes Spark.** As of [July 23, 2026](https://9to5google.com/2026/07/23/gemini-spark-google-ai-pro-us/), Spark is no longer Ultra-exclusive — $20/month AI Pro subscribers in the US get access too (English-only, per Google's [Spark changelog](https://support.google.com/gemini/answer/17171264)). Same eligibility rules apply: 18+, personal Google Account (not work/school), Keep Activity turned on, 15 simultaneous tasks max.
- **No longer US-only.** As of [July 30, 2026](https://blog.google/innovation-and-ai/products/gemini-app/gemini-spark-updates-july-2026/), Pro-tier access expanded to over 160 additional countries. Google's support page states Spark is now available everywhere Gemini Apps are supported **except the EEA, Nigeria, Switzerland, and the UK** — a list that shrank from an earlier (June 2026) exclusion set that also covered Australia, Canada, Hong Kong, India, Japan, and South Korea.
- The $100/$200 Ultra tiers remain unchanged in price.

---

## MCP Integration and What It Means for Developers

The MCP angle is directly relevant to how Spark will grow its integration surface. Rather than requiring Google to build one-off integrations for every third-party service, Spark's summer 2026 expansion relies on the MCP standard to consume tools from GitHub, Notion, Slack, and others.

This has a practical implication: **an MCP server built today for Claude Code, Cursor, or any other MCP-compatible agent automatically becomes a candidate Spark consumer** when Spark's MCP integration lands — no Spark-specific development required. The same tool definition works across agents. For developers building MCP servers, Spark represents a significant expansion of their potential distribution once those integrations go live.

Google's managed agents infrastructure already supports MCP natively (as covered in the Managed Agents API review). Spark is the consumer product expression of the same capability.

---

## Security and Privacy Concerns

Gemini Spark requires more trust than any previous Google product, and the trust story at launch is incomplete.

**Prompt injection is a real attack surface.** A persistent agent that reads arbitrary web content, emails, and documents on your behalf is a high-value target for adversarial instructions embedded in those sources. Malicious websites and emails can contain hidden text designed to hijack an AI agent's actions — redirecting purchases, exfiltrating data, or executing unauthorized tasks.

**Update (2026-08-22) — citation correction:** our original citation for "Google says Spark includes prompt detection layers" was the [Forbes I/O 2026 recap](https://www.forbes.com/sites/janakirammsv/2026/05/21/google-io-2026-turned-gemini-into-an-agent-platform/) cited elsewhere on this page; re-checking it now, that article does not actually discuss prompt injection or detection layers — it was an uncited, unsupported claim on our part. We've removed the Spark-specific framing. What we *can* verify: Google documents a general, layered defense against prompt injection across Gemini and Workspace — ML-based detection of malicious instructions embedded in external content, "reinforcement" prompts that tell the model to disregard embedded adversarial instructions, URL/markdown sanitization via Safe Browsing, and required user confirmation for risky actions ([Google Security Blog, June 2025](https://blog.google/security/mitigating-prompt-injection-attacks/); [Google Workspace support docs](https://support.google.com/docs/answer/16204578?hl=en)). Neither source confirms this defense stack is specifically what ships inside Spark, or that Google made a Spark-specific prompt-injection announcement at I/O. No one has fully solved prompt injection. Running a 24/7 agent that reads arbitrary external content is a meaningful attack surface, and users should treat it as such regardless of which specific defenses Spark uses.

A [leaked onboarding screen from an early Gemini app beta, reported by Android Authority on May 14, 2026](https://www.androidauthority.com/gemini-spark-onboarding-screen-leaked-3667118/), disclosed that Spark "may do things like share your info or make purchases without asking." That language does not appear in the shipped product, which states Spark is "designed to check with you before taking major actions" and cannot complete a purchase without explicit confirmation. The framing of the leaked text, however, suggests the eventual steady-state — particularly after the Agents Payment Protocol launches — involves a meaningfully larger autonomous surface than today's consent patterns train users to expect.

As of the I/O keynote, **Google had not published a standalone Spark-specific privacy policy**. The standard Google Privacy Policy applied.

**Update (2026-08-22):** Google has since added a dedicated "Gemini Spark" section to its general [Gemini Apps Privacy Hub](https://support.google.com/gemini/answer/13594961?hl=en), which states Spark data is "used consistently with the Gemini Apps Privacy Notice," describes what it retains (data from Personal Intelligence and Connected Apps, including data users may find sensitive), confirms users can delete this data any time in Spark settings, and notes Spark shares "necessary info" (which can include a user's name or address) with third parties to complete tasks. This is a real improvement over the launch-day gap, but it is still not a standalone privacy policy — it's a section within the umbrella Gemini Apps notice, and the third-party data-sharing language is broad rather than itemized.

Google's stance is that Spark requires user approval for high-stakes actions. What constitutes "high-stakes" and what the data retention model looks like for an always-on agent with full Workspace access are questions the current documentation does not fully answer.

---

## Comparison: Spark vs. OpenAI Operator

**Update (2026-08-22) — this comparison is now historical, not current.** OpenAI launched Operator in a limited research preview on February 1, 2025 — an agent that could browse the web and fill out forms on your behalf. It was a meaningful capability, but reactive: you had to be present to kick off a task, and it ran in a browser session tied to your active session. However, [Operator was deprecated and shut down on August 31, 2025](https://en.wikipedia.org/wiki/OpenAI_Operator), folded into "ChatGPT agent" mode — so Operator did not exist as a standalone product even at this article's original May 2026 publish date, and our original framing below was already out of date when written. As of this audit, ChatGPT agent mode itself appears to have been pulled from OpenAI's help center in early August 2026, with OpenAI pointing users to "ChatGPT Work" and a separate cloud-browser feature instead; we could not independently confirm this against OpenAI's own help page (it returned an access error when we tried to fetch it directly), so treat that specific detail as unverified pending a primary-source check.

Gemini Spark is more architecturally ambitious than Operator was. The persistent cloud VM model means true asynchronous operation — assign a task Monday night, find results in your email Tuesday morning without having opened an app. The email interface is also differentiated: Operator used a chat interface; Spark treats email as a first-class input channel, which is lower-friction for delegation.

The tradeoff: Spark is tightly coupled to Google's ecosystem. It works with Gmail, Google Calendar, Chrome, and Google Workspace natively. If you live outside that ecosystem — Outlook, Firefox, Apple Pay — the value proposition shrinks. Claude's agentic capabilities are more API-extensible for developers. Spark wins on consumer integration within Google's world; it is less compelling outside it.

---

## Comparison: Spark vs. Managed Agents API

Spark and the Managed Agents API share an engine but serve entirely different audiences:

| | Gemini Spark | Managed Agents API |
|---|---|---|
| **Audience** | Consumers, non-technical users | Developers, builders |
| **Activation** | Email delegation, Gemini app | Single API call |
| **Integrations** | Google Workspace + curated third-party | MCP-connected tools, custom |
| **Persistence** | Always-on cloud VM per user | Ephemeral per-interaction sandbox |
| **Pricing** | $20/month Pro or $100+/month Ultra subscription (updated 2026-08-22) | Gemini 3.5 Flash token rates |
| **Control** | User-configured, approval-gated | Developer-defined in code |
| **State** | Persistent across sessions | Ephemeral (no state by default) |

If you are a developer who wants to build an agent workflow, the Managed Agents API is the right primitive — you control the tools, the instructions, and the execution. If you are an individual who wants to offload recurring digital tasks without writing code, Spark is the product. They are complementary, not competing.

---

## Limitations

**US-only at launch — since resolved.** Availability was limited to the US at announcement, but as of [July 30, 2026 Google expanded access to 160+ additional countries](https://blog.google/innovation-and-ai/products/gemini-app/gemini-spark-updates-july-2026/), excluding only the EEA, Nigeria, Switzerland, and the UK. This limitation no longer applies for most readers outside those four regions.

**$100/month subscription required — since resolved.** Spark launched Ultra-only, but as of [July 23, 2026 it's also available on Google AI Pro ($20/month)](https://9to5google.com/2026/07/23/gemini-spark-google-ai-pro-us/) in the US. It is still not on free Gemini tiers.

**MCP third-party integrations are partially available.** Of the GitHub/Notion/Slack set announced for "over the summer," GitHub has shipped as a connected app ([9to5Google, August 13, 2026](https://9to5google.com/2026/08/13/gemini-is-getting-over-a-dozen-new-connected-apps-heres-the-list/)); Notion and Slack do not appear in Google's connected-apps directory as of this audit. The broader integration set now also includes Dropbox, Zillow, Wix, and others added through the summer, but the specific "over the summer" promise for Notion and Slack remains unconfirmed.

**Payment protocol not yet available.** Autonomous purchasing — the capability that most distinguishes Spark from a sophisticated automation — is announced but not shipped. The current version is a capable research-and-drafting agent, not yet a transactional one.

**Still no standalone Spark privacy policy.** Google has [since added a dedicated Spark section to its Gemini Apps Privacy Hub](https://support.google.com/gemini/answer/13594961?hl=en) (see Security and Privacy Concerns above), which narrows the original launch-day gap, but persistent access to email, files, and calendar by an autonomous agent still doesn't have its own standalone data handling disclosure — it's addressed within a broader Gemini Apps notice rather than a Spark-specific document.

**Google-hosted only.** Spark runs on Google Cloud. There is no self-hosted, on-premises, or data-residency option. For users with compliance requirements or a preference for limiting Google's data access, this is a hard constraint.

---

## Rating: 3/5

Gemini Spark represents Google's most ambitious consumer AI product to date. The core concept — a cloud-resident agent that handles delegated tasks asynchronously, knows your full Google context, and stays active independently of your devices — is genuinely useful and more developed than most "AI agent" consumer products that preceded it.

The 3/5 reflects the gap between the announced vision and the available product. **Update (2026-08-22):** two of the original launch constraints — US-only access and the $100/month Ultra requirement — have been resolved by Google's July 2026 expansion to Google AI Pro ($20/month) and 160+ additional countries. What remains unresolved: MCP integrations for Notion and Slack are still unconfirmed (GitHub has shipped), the Agents Payment Protocol has not shipped, and there is still no Spark-specific privacy policy. The approval-gated action model is reassuring but also means the most compelling use cases (autonomous task execution while you're asleep) are still gated on features that haven't shipped.

The trajectory is promising. If Google delivers on the MCP integrations this summer, publishes a Spark-specific privacy policy, and follows through on the Agents Payment Protocol with clear user controls, Spark has the foundation to be a 4–5/5 product — the first consumer AI agent that genuinely changes how you manage your digital life rather than just augmenting how you type.

Check back when the MCP integrations land and the privacy policy is published. Those two milestones will define whether Spark is a tool worth trusting with your inbox.

---

*ChatForest researches AI tools and platforms; we do not test them hands-on. Our reviews are based on publicly available documentation, benchmark data, developer community reports, and press coverage.*

---

## Sources

- [Google introduces Gemini Spark, a 24/7 agentic assistant with Gmail integration, at IO 2026 — TechCrunch](https://techcrunch.com/2026/05/19/google-introduces-gemini-spark-a-24-7-agentic-assistant-with-gmail-integration/)
- [100 things we announced at Google I/O 2026 — Google Blog](https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/)
- [Google I/O 2026: Turned Gemini Into An Agent Platform — Forbes](https://www.forbes.com/sites/janakirammsv/2026/05/21/google-io-2026-turned-gemini-into-an-agent-platform/)
- [Everything new in our Google AI subscriptions, fresh from I/O 2026 — Google Blog](https://blog.google/products-and-platforms/products/google-one/google-ai-subscriptions/)
- [What's new for Gemini Spark — Google Gemini Apps Help (changelog)](https://support.google.com/gemini/answer/17171264)
- [Gemini Spark rolling out to Google AI Pro users in the US — 9to5Google, July 23, 2026](https://9to5google.com/2026/07/23/gemini-spark-google-ai-pro-us/)
- [Gemini Spark updates: new Chrome browsing integration and 160+ country expansion — Google Blog, July 30, 2026](https://blog.google/innovation-and-ai/products/gemini-app/gemini-spark-updates-july-2026/)
- [Gemini is getting over a dozen new connected apps — 9to5Google, August 13, 2026](https://9to5google.com/2026/08/13/gemini-is-getting-over-a-dozen-new-connected-apps-heres-the-list/)
- [Mitigating prompt injection attacks with a layered defense strategy — Google Security Blog, June 2025](https://blog.google/security/mitigating-prompt-injection-attacks/)
- [How Google Workspace with Gemini helps protect users from malicious content and prompt injection — Google Docs Editors Help](https://support.google.com/docs/answer/16204578?hl=en)
- [OpenAI Operator — Wikipedia, confirming Feb 2025 launch and Aug 31, 2025 shutdown](https://en.wikipedia.org/wiki/OpenAI_Operator)
- [Announcing Agent Payments Protocol (AP2) — Google Cloud Blog, September 16, 2025](https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol)
- [Gemini Apps Privacy Hub, "Gemini Spark" section — Google Gemini Apps Help](https://support.google.com/gemini/answer/13594961?hl=en)
- [Google's upcoming 'Gemini Spark' could soon book your flights and handle your inbox — Android Authority, May 14, 2026](https://www.androidauthority.com/gemini-spark-onboarding-screen-leaked-3667118/)
- [With Gemini 3.5 Flash, Google bets its next AI wave on agents, not chatbots — TechCrunch, May 19, 2026](https://techcrunch.com/2026/05/19/with-gemini-3-5-flash-google-bets-its-next-ai-wave-on-agents-not-chatbots/)

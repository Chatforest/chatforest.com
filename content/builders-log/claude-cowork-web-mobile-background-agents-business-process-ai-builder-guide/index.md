---
title: "Claude Cowork Goes Mobile: The Background Agent Built for Business, Not Just Code"
date: 2026-07-07
description: "Anthropic expanded Claude Cowork to web and mobile on July 7 for Max subscribers. Data from 1.2M sessions across 600k+ orgs reveals the surprise: 90%+ of usage is business process and content work, not software development. What builders should know."
og_description: "Claude Cowork now runs on mobile and web, executing tasks in the background while devices are offline. Usage data shows the real adoption is in business process automation — not coding. Builder guide."
tags: ["agents", "Anthropic", "background-agents", "AI-workflow", "enterprise-AI", "Claude"]
sources_audited: 2026-08-04
---

Anthropic expanded [Claude Cowork](https://the-decoder.com/anthropics-claude-cowork-ai-agent-is-now-available-on-mobile-and-web/) to web and mobile on July 7, 2026. The product — a background agent platform that [debuted as a desktop-only app in January 2026](https://www.techcrunch.com/2026/01/12/anthropics-new-cowork-tool-offers-claude-code-without-the-code/) — is now available on any device for Claude Max subscribers, with rollout to additional plans expected in the weeks ahead.

The expansion matters for builders not just because of the new surfaces, but because of what the usage data reveals about where agentic AI is actually landing in the wild.

## What Claude Cowork Does

Claude Cowork is Anthropic's [background agent platform](https://techcrunch.com/2026/07/07/the-coding-agent-wars-are-spilling-into-the-rest-of-the-office-claude-cowork/): a product designed for tasks that take longer than a chat session and don't require the user watching. It sits between Claude's chat interface (turn-by-turn Q&A) and a fully autonomous pipeline (unsupervised long-horizon agents).

The July 7 update adds three capabilities that push it meaningfully further:

**Cross-device continuity.** [Start a task on a desktop, monitor progress on a phone, retrieve the finished output from whatever device is handy](https://claude.com/blog/cowork-web-mobile). The session persists in the cloud rather than being tied to a local machine.

**True background execution.** [Cowork tasks continue running while the user's device is fully offline](https://claude.com/blog/cowork-web-mobile) — including when the laptop is closed. This removes the previous requirement of keeping a desktop session alive.

**Unified interface.** [Chat and Cowork are being merged into a single web and desktop interface, with projects and artifacts living together across both modes](https://claude.com/blog/cowork-web-mobile).

Anthropic also [doubled Cowork usage limits through August 5, 2026](https://claude.com/blog/cowork-web-mobile) — a common incentive pattern for new surface launches.

## The Usage Data: It's Mostly Not Coding

Anthropic [analyzed 1.2 million anonymized Cowork sessions](https://techcrunch.com/2026/07/07/the-coding-agent-wars-are-spilling-into-the-rest-of-the-office-claude-cowork/) across more than 600,000 organizations (May 2026 data). The headline finding: more than 90% of sessions had nothing to do with software development.

The breakdown by category:

| Category | Share |
|----------|-------|
| Business process operating | 33.4% |
| Content creation / copywriting | 16.4% |
| Software development | 8.7% |
| Other (DevOps, research, data analysis, document processing, and more) | 41.5% |

[Business process operating — defined as tasks like pulling scattered updates into a single report, building onboarding checklists, and reconciling spreadsheets](https://claude.com/blog/how-people-are-using-claude-cowork) — is nearly four times larger than the software development category that Cowork was originally framed around.

Anthropic's stated interpretation: [Cowork addresses "the work around the work" — tasks that are part of a broad swath of jobs but rarely anyone's core responsibility](https://claude.com/blog/how-people-are-using-claude-cowork). The target demographic from the data is not the developer, but people in finance, HR, and administrative roles who spend significant time on structured business-process work.

## Features in Context

The business-process framing changes which features matter. For developers, background execution is a convenience — a coding agent doesn't need to stay on screen. For business users running competitive analyses, compliance reviews, or multi-source report generation, background execution is the core value proposition: they submit the task and check back when it's done, the same way they handle email.

[Cross-device continuity](https://9to5mac.com/2026/07/13/anthropic-expanding-claude-cowork-to-mobile-and-web-details-here/) mirrors how non-technical workers actually operate. A finance analyst submits a report request from their laptop in the morning, checks progress on their phone at lunch, and retrieves the output from a conference room iPad. That workflow wasn't possible with the desktop-only January release.

The autonomous task list (scheduling, structured automation, agentic admin) is where Cowork competes most directly with workflow automation tools like Zapier, Make, and enterprise RPA platforms — except Cowork handles unstructured language tasks that rule-based automations can't.

## Competitive Landscape

OpenAI's Codex followed a parallel trajectory: launched as a developer coding tool, now [actively used for reports, spreadsheets, presentations, and data analysis across non-developer roles](https://techcrunch.com/2026/07/07/the-coding-agent-wars-are-spilling-into-the-rest-of-the-office-claude-cowork/). The "coding agent wars" moniker has become a misnomer — both products are competing in general knowledge-work automation.

Microsoft's [Sales Agent and Service Agent](https://techcommunity.microsoft.com/blog/Microsoft365CopilotBlog/sales-agent-is-now-generally-available-bringing-customer-and-deal-intelligence-i/4532629) (generally available [July 7](https://www.cxtoday.com/marketing-sales-technology/microsoft-sales-agent-service-agent-general-availability/), embedded in Outlook and Teams) address the same horizontal: automating structured work across roles. The July 7 date of both launches is not a coincidence — Anthropic and Microsoft both pushed enterprise-accessible background agents on the same day.

## Builder Takeaways

**The target user is not the developer.** If you're building on top of background agent infrastructure, the Cowork data is the clearest signal yet that the market is business process workers, not engineers. 33.4% of usage is spreadsheet reconciliation, checklist building, and report aggregation — tasks that have no code in them at all.

**Background execution is now table stakes.** Any agentic product that requires the user to keep a session open while a task runs is immediately at a disadvantage against platforms that execute in the cloud. The architecture shift from local-session-held to cloud-persistent is structural.

**Cross-device matters more than it looks.** The mobile surface isn't just a convenience layer — it changes how business users track and retrieve work. Task submission, status monitoring, and output retrieval are three different contexts that may happen on three different devices.

**Unified chat + agent interface is where UX is heading.** [Anthropic's decision to merge chat and Cowork](https://claude.com/blog/cowork-web-mobile) into a single interface signals the interaction model: users shouldn't need to decide in advance whether a task is a "quick question" or a "background job." The product should route based on task complexity, not the user's mental model of the tool.

**Current availability:** Claude Max plan, July 7, 2026. Rollout to additional plans: announced but timeline unspecified.

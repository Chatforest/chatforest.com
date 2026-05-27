---
title: "Code with Claude 2026: SF and London Showed AI Already Writes Most of the Code"
date: 2026-05-06
description: "Anthropic's three-city developer conference — San Francisco (May 6), London (May 19), Tokyo (June 10) — was less a feature reveal and more a normalizing event: AI-authored code has arrived, whether developers are ready or not."
og_description: "Code with Claude 2026: In SF, half the London audience raised their hands when asked who'd shipped a Claude-written PR in the last week. Anthropic shipped Managed Agents with Dreaming, Outcomes, and Multiagent Orchestration. Claude Code rate limits doubled. Boris Cherny: 'The default is now I'm going to have Claude prompt itself.' Tokyo on June 10."
content_type: "Review"
card_description: "Anthropic's Code with Claude 2026 developer conference ran in San Francisco (May 6, SVN West, several thousand attendees) and London (May 19, Park Plaza Westminster Bridge, ~500 invitees), with Tokyo scheduled for June 10. Major SF announcements: Claude Code 5-hour rate limits doubled for Pro/Max/Team/Enterprise; Managed Agents with Dreaming, Outcomes, and Multiagent Orchestration (public beta); 10 agent templates; Microsoft 365 add-ins for Excel/Word/PowerPoint; Moody's MCP app covering 600M+ companies; Opus 4.7 scoring 64.37% on Vals AI Finance Agent benchmark; Proactive Workflows (Claude initiates actions without prompting); self-hosted agent sandboxes and MCP tunnels. London restaged the SF announcements for a European audience and featured case studies from Spotify, Delivery Hero, Lovable, Base44, and Monday.com. Key stat: from the London stage, almost half the room raised their hands when asked who had shipped a PR completely written by Claude in the last week. Boris Cherny, Head of Claude Code: 'The default isn't I'm going to prompt Claude — the default is now I'm going to have Claude prompt itself.' Anthropic: 'Most software at Anthropic is now written by Claude.'"
tags: ["claude-code", "anthropic", "developer-conference", "managed-agents", "code-with-claude", "agentic-coding", "claude-code-2026", "ai-coding", "dreaming", "multiagent-orchestration", "outcomes", "mcp", "microsoft-365", "api-platform", "developer-tools"]
categories: ["reviews"]
rating: 4
author: "ChatForest"
---

**At a glance:** Code with Claude 2026 developer conference. San Francisco: May 6. London: May 19. Tokyo: June 10. Major product announcements, doubled rate limits, and a room that was half-raised-hands when asked who had shipped an AI-written PR last week. Part of our **[AI Tools & Companies reviews](/categories/ai-tools/)**.

---

Anthropic didn't call Code with Claude 2026 a turning point. They didn't have to. The room said it for them.

On May 19, during the London leg of the three-city developer conference, someone on stage asked: "Who here has shipped a pull request in the last week that was completely written by Claude?" Almost half the hands in a packed conference room went up.

That moment — unrehearsed, drawn from a room of working developers, not AI evangelists — is probably the most important signal from these two events. Not the feature list. Not the rate limit improvements. The hands.

---

## The Conference Structure

Code with Claude 2026 was a three-city tour:

- **San Francisco — May 6, 2026.** SVN West venue. Several thousand attendees. The primary product launch event. Demand was high enough that Anthropic added a second day specifically for independent developers and early-stage founders who couldn't get a slot on day one.
- **London — May 19, 2026.** Park Plaza Westminster Bridge, South Bank. Approximately 500 invitees, weighted toward Claude for Enterprise customers and AWS Bedrock/Vertex buyers. The first physical gathering Anthropic has hosted in Europe.
- **Tokyo — June 10, 2026.** Upcoming. The Asia-Pacific stop.

The format followed a consistent pattern: keynotes from Anthropic product leads, partner case study presentations, and hands-on workshops. The London event restaged the SF product announcements for a European audience and added company showcases from Spotify, Delivery Hero, Lovable, Base44, and Monday.com — organizations that have rebuilt parts of their engineering workflows around Claude Code.

---

## What Was Actually Shipped (SF Announcements)

San Francisco was where the products landed. Several announcements were notable:

### Claude Code Rate Limits — Doubled

Anthropic doubled the 5-hour Claude Code rate window for Pro, Max, Team, and seat-based Enterprise plans. The peak-hours reduction was also removed for Pro and Max subscribers. For developers who had been hitting limits in the middle of sessions, this was practical and overdue.

### Managed Agents: Dreaming, Outcomes, Multiagent Orchestration

The headline technical announcement was a set of three new capabilities added to Claude Managed Agents — the framework Anthropic introduced to give developers a structured way to build, deploy, and improve production agents.

**Dreaming** is a scheduled background process that reviews past agent sessions, extracts patterns, and curates memory stores. The premise: a single agent running a single session can't see its own recurring mistakes. Dreaming surfaces those patterns across sessions and refines the agent's behavior over time without requiring a developer to manually review logs. Dreaming is currently in research preview.

**Outcomes** lets developers write a rubric describing what success looks like, and the agent works toward it. A separate grader model evaluates output against the defined criteria in its own context window — isolated from the agent's reasoning so it can evaluate without being influenced by how the agent got there. Outcomes and Multiagent Orchestration are in public beta.

**Multiagent Orchestration** addresses the core limitation of single-agent architectures: too much work for one context window to do well. A lead agent can break a job into pieces and delegate each to a specialist with its own model, prompt, and tools. The specialists work in parallel on a shared filesystem and contribute findings back to the lead agent's context. Anthropic's own example: a lead agent running an investigation while subagents fan out across deploy history, error logs, metrics, and support tickets simultaneously.

We wrote separately about these three features in more detail: **[Claude Managed Agents: Dreaming, Outcomes, and Multiagent Orchestration Explained](/guides/claude-managed-agents-dreaming-outcomes-multiagent/)**.

### Proactive Workflows

Rather than waiting for a developer to issue a command, Claude can now identify conditions in a codebase or project environment and initiate actions on its own — flagging a failing test, proposing a fix for a detected dependency conflict, or triggering a workflow when a defined condition is met. This is sometimes called an event-driven or reactive agent pattern. The practical effect is that Claude moves from responding to developers toward monitoring alongside them.

### Tooling and Integrations

Ten agent templates shipped — pre-built starting points for common agentic use cases. Microsoft 365 integrations launched for Excel, PowerPoint, and Word (Outlook listed as coming). The Moody's MCP app entered availability, giving developers access to data on more than 600 million companies via the Model Context Protocol. Self-hosted agent sandboxes entered public beta; MCP tunnels entered research preview.

### Opus 4.7 on Finance Benchmarks

Anthropic noted that Opus 4.7 scored 64.37% on the Vals AI Finance Agent benchmark — a figure Anthropic highlighted to demonstrate traction in agentic evaluation frameworks beyond general coding assessments.

---

## The London Meaning

London wasn't primarily a product announcement event. The SF announcements had already shipped. London's purpose was different: signal to the European developer community that Anthropic treats it as a real market, not an afterthought.

The evidence: Anthropic is reportedly hiring 50+ engineers in London in 2026. The London office represents Bedrock-EU and Vertex-EU regional deployment credibility. It also positions Anthropic favorably against the EU AI Act's GPAI chapter obligations that came into force in August 2025. A lab with a material European engineering presence is structurally different from one that operates from Palo Alto and calls Europe a growth market.

The company showcases — Spotify, Delivery Hero, Lovable, Base44, Monday.com — were telling for a different reason. These aren't AI-native demos or research prototypes. They're production engineering workflows at real companies that have rebuilt around Claude Code. Delivery Hero manages a logistics and food delivery operation across 70+ countries. Spotify runs one of the world's largest streaming infrastructure systems. Monday.com operates a no-code platform used by 225,000+ organizations. Their presence on stage, discussing how they reorganized developer workflows around Claude, was more credible than any benchmark.

---

## The Shift Boris Cherny Described

Boris Cherny, who heads Claude Code, set the framing in the SF keynote:

> "The default isn't 'I'm going to prompt Claude' — the default is now 'I'm going to have Claude prompt itself.'"

This is a precise description of a real shift. When Claude Code first launched, the dominant usage pattern was reactive: a developer wrote code, got stuck, asked Claude for help, reviewed the output. Developer as author, Claude as tool.

The pattern Cherny described — and the one that showed up in the half-raised London hands — is different. Claude is the author. The developer specifies the work, dispatches one or more agents, and reviews and evaluates what comes back. Developer as architect and evaluator, Claude as executor.

That inversion changes what matters in a developer's day. Specification quality matters more than typing speed. Evaluation and testing become the primary skill. Understanding what Claude can and can't be trusted to do unsupervised is the professional differentiator — not the ability to write code quickly.

Anthropic disclosed, in context of these events, that most software at Anthropic is now written by Claude. They weren't alone in that claim: OpenAI, Google, and Microsoft have made similar statements about their own internal codebases. The AI lab that built the tool has shifted its own engineering workflow around it. That's not a thought experiment; it's a data point.

---

## The Honest Limits

The MIT Technology Review headline for their conference coverage: "Anthropic's Code with Claude showed off coding's future — whether you like it or not." That qualifier matters.

Several things the conference didn't fully resolve:

**Oversight at scale.** The developers in the London room who raised their hands had also, presumably, reviewed those Claude-written PRs before merging. Or they hadn't, and that's a different problem. The conference didn't dwell on what happens when the verification step gets skipped, which it will.

**Entry-level coding.** The case studies featured companies with experienced engineering teams who knew what good output looked like before they started delegating to Claude. The skills required to evaluate Claude's code are not trivially different from the skills required to write it. The conference was largely silent on this point.

**Reliability in long-horizon tasks.** Multiagent Orchestration and Dreaming are compelling architectures for agents that improve over time. They're also systems where errors can compound across sessions, and where the outputs become harder to trace to individual decisions. Managed Agents are in public beta for a reason.

---

## What Comes Next

Tokyo on June 10 closes the tour. Anthropic hasn't announced what, if anything, new will ship there — given the SF/London pattern, the Tokyo event will likely re-stage SF announcements for an Asia-Pacific developer community, with potential additions.

Beyond the conference cadence, the rate limit increase and Managed Agents features are live. Developers building production agents have materially more headroom and better tooling than they did before May 6.

The question the London room answered — whether AI-authored code has actually arrived in professional development workflows — is no longer hypothetical. It has. The question that remains is what that means for how development teams are structured, how code is reviewed, and what skills a working developer needs in 2026 and after.

---

*ChatForest covers AI tools, models, and infrastructure from a builder-first perspective. This article is based on publicly available reporting from Anthropic's blog, InfoQ, MIT Technology Review, Simon Willison's live blog, TechCrunch, 9to5Mac, MindStudio, and firsthand developer accounts from the SF and London events. ChatForest has no commercial relationship with Anthropic.*

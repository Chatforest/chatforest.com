---
title: "Gemini 3.5 Pro: What Google Didn't Announce at I/O — And Why That's the Point"
date: 2026-05-23
description: "Gemini 3.5 Pro wasn't at Google I/O 2026. It's coming in June. Here's what Gemini 3.5 Flash revealed about its gaps, what the internal 'Cappuccino' leaks suggest, and what Pro needs to deliver to justify the wait."
og_description: "Gemini 3.5 Pro (expected June 2026): internal codename Cappuccino. Gemini 3.5 Flash already outperforms Gemini 3.1 Pro on coding/agentic tasks but regressed on hard reasoning, ARC-AGI-2, and long-context retrieval. Pro is being built to fix those gaps. Pricing unknown; expected ~$2.50–$15/M tokens."
content_type: "Review"
card_description: "Gemini 3.5 Pro wasn't announced at Google I/O 2026 — but its absence was deliberate. Sundar Pichai told developers to 'give us until next month.' Gemini 3.5 Flash already outperforms Gemini 3.1 Pro on coding and agentic benchmarks, but regressed on hard reasoning (Humanity's Last Exam), ARC-AGI-2 pattern matching, and 128K-token retrieval. Pro is being built to restore those losses while keeping the agentic and speed gains of Flash. Internally codenamed Cappuccino, leaks point to stronger SVG/frontend generation, enhanced logical reasoning, and improved multimodal output — with no confirmed pricing or release date beyond 'June 2026.'"
tags: ["google", "gemini", "gemini-3.5", "llm", "ai-models", "benchmark", "agentic", "coding-assistants", "preview", "upcoming"]
categories: ["reviews"]
rating: 0
author: "ChatForest"
---

**Editorial note:** This is a preview article, not a full review. Gemini 3.5 Pro has not been released as of publication (May 23, 2026). Benchmarks and pricing cited here are either from Gemini 3.5 Flash (already released) or from leaked/unofficial sources. The rating above is withheld until a full review can be written post-launch.

---

**At a glance:** Gemini 3.5 Pro — expected June 2026. Internal codename: Cappuccino. Status: internal testing. Announced: indirectly, by Sundar Pichai at Google I/O 2026. No pricing, benchmarks, or model ID confirmed. This preview covers what Gemini 3.5 Flash tells us about what Pro needs to fix, and what internal leaks suggest it will deliver. Part of our **[AI Models & Companies reviews](/categories/ai-tools/)**.

---

Google I/O 2026 had a conspicuous absence. Between Gemini 3.5 Flash, Gemini Spark, Google Antigravity 2.0, AI Glasses, and the announcement of Google Search Agents, one model wasn't on stage: **Gemini 3.5 Pro**.

Sundar Pichai's explanation was five words: "Give us until next month."

That framing tells you more than a benchmark table would. Google shipped Flash at I/O because Flash was ready. Pro isn't ready yet — and the fact that Google said so plainly, rather than delaying I/O or shipping a half-baked model, is worth noting.

Here's what we know about why, and what Pro is being built to fix.

---

## What Gemini 3.5 Flash Already Does Well

Understanding Pro starts with understanding Flash. **[Gemini 3.5 Flash](/reviews/gemini-3-5-flash-google-io-2026-review/)** (released May 19, 2026) achieved something genuinely notable: a Flash-tier model that outperforms last year's flagship — Gemini 3.1 Pro — on coding and agentic benchmarks.

Specific Flash advantages over Gemini 3.1 Pro:

- **Terminal-Bench 2.1**: 76.2% vs 70.3% for Gemini 3.1 Pro
- **MCP Atlas**: 83.6% vs 78.2%
- **SWE-Bench Verified**: 81.0% — ahead of Gemini 3.1 Pro

On those three metrics, the 3.5 Flash tier has already made Gemini 3.1 Pro obsolete. At $1.50/$9.00 per million tokens and four times the speed, there's essentially no reason to route agentic coding tasks through the old Pro.

But three categories didn't follow that trajectory.

---

## The Three Regressions Pro Needs to Fix

When Gemini 3.5 Flash was benchmarked against Gemini 3.1 Pro on hard reasoning tasks, three categories showed clear regressions:

### 1. Hard Reasoning — Humanity's Last Exam

Humanity's Last Exam (HLE) tests expert-level knowledge across physics, mathematics, medicine, and law. Flash dropped approximately **4.2 points** compared to Gemini 3.1 Pro on this benchmark. Flash was explicitly optimized for agentic speed and tool-use — HLE tests a different kind of depth.

### 2. Pattern Matching — ARC-AGI-2

ARC-AGI-2 tests abstract reasoning and novel pattern generalization — tasks that require the model to figure out rules rather than retrieve stored knowledge. Flash regressed approximately **5.0 points** compared to Gemini 3.1 Pro. This matters for code review, novel debugging, and any task requiring inference from unfamiliar patterns.

### 3. Long-Context Retrieval — 128K Range

At 128K token context depth, Flash's retrieval accuracy declined roughly **7.6 points** compared to Gemini 3.1 Pro. Both models support 1M token contexts, but the precision at long range differs. For use cases that rely on finding specific information in large documents or long codebases, Flash's 128K-range drop is a practical limitation.

These three gaps are almost certainly what Pro is designed to close.

---

## The Cappuccino Leaks

In mid-May 2026, screenshots and partial benchmark tables attributed to an internal Google checkpoint codenamed **Cappuccino** surfaced in developer communities. Google has not acknowledged the leaks.

What the Cappuccino materials show, with the significant caveat that these are unverified:

- **SVG and frontend generation**: Described as substantially improved — one benchmark showed complex interactive web apps with adjustable control panels that Gemini 3.5 Flash failed to produce correctly.
- **Logical reasoning**: Claims of meaningful improvements alongside coding capability, not a tradeoff.
- **Multimodal output quality**: Better 3D and animation component generation, which aligns with Google's announced Antigravity 2.0 direction.

Cappuccino appears to be an internal candidate build, not necessarily the shipping model. Internal checkpoints often differ from released versions, and Google's infrastructure teams have been running significant optimization passes during this period.

Take these details as directional, not definitive.

---

## What Pro Needs to Deliver

For Gemini 3.5 Pro to justify its positioning, it needs to accomplish something specific: restore Gemini 3.1 Pro's advantages on reasoning, ARC-AGI-2, and long-context retrieval — while keeping Flash's advantages on coding and agentic tasks.

That's not a trivial ask. Flash achieved its coding gains partly through architectural choices that tradeoff hard reasoning depth. Pro needs to hold both, which is why it wasn't ready at I/O.

The competitive context makes this urgent. **Claude Opus 4.7** currently leads on coding (87.6% SWE-bench Verified, 64.3% SWE-bench Pro) and hallucination resistance (36% on AA-Omniscience). **GPT-5.5** leads on developer adoption and the SWE-bench raw number (88.7% Verified). Gemini 3.5 Flash is fast and cheap but doesn't lead on any hard reasoning metric.

Pro's job is to give Google a model that can lead on at least one hard reasoning category. The GPQA Diamond benchmark (PhD-level science questions) is the most likely target — Gemini 3.1 Pro sat at 94.1–94.3% on that benchmark, competitive with Claude Opus 4.7 (94.2%) and just behind GPT-5.4 Pro (94.4%). If Pro can match or beat those numbers while keeping agentic capabilities, Google will have a complete lineup.

---

## Pricing: What to Expect

No pricing has been announced. Three scenarios based on the product structure:

| Scenario | Input / Output | Positioning |
|---|---|---|
| Premium reasoning tier | ~$2.50–$5.00 / $15–$25 per M | Compete directly with Claude Opus 4.7 ($5/$25) and GPT-5.5 ($5/$30) |
| Mid-tier | ~$1.50–$2.50 / $10–$15 per M | Value-positioned premium; incentivize migration from Gemini 3.1 Pro |
| Flash-parity | $1.50 / $9.00 per M | Unlikely; cannibalizes Flash and undercuts the Pro brand signal |

The premium tier is most likely. Google has historically priced Pro models against Claude and GPT flagship tiers, and 3.5 Pro's positioning as the reasoning recovery model for the 3.5 series suggests it will carry a pricing premium over Flash.

Whether Google offers a context-length surcharge (as OpenAI does at 272K tokens) is unknown. Gemini 3.1 Pro had no long-context premium — if 3.5 Pro maintains that, it may be a meaningful differentiator for long-document use cases.

---

## Release Timeline and What Happens Next

Pichai said "next month" at I/O on May 19. That points to June 2026, which aligns with the Microsoft Build 2026 window (June 2–3 in San Francisco) — though Google typically doesn't time releases to competitor events.

More likely: a standalone Gemini 3.5 Pro announcement sometime in June, followed by general availability in the API, Gemini Advanced (Ultra subscribers), and enterprise tiers.

Downstream from Pro:
- **Gemini Nano 3.5** (on-device, Android/Pixel) — expected later in 2026
- **Gemini Ultra 3.5** (memory-optimized, speculative) — no official timeline
- **Gemini Omni Flash** — already rolling out to Gemini app subscribers as of I/O

---

## Why This Gap Matters

Flash being a capable model doesn't make Pro unnecessary. It makes Pro *more* necessary.

If Flash is good enough for 80% of use cases, Pro needs to be clearly better — not marginally better — for the remaining 20%. That 20% includes the tasks that matter most in enterprise contexts: legal research, scientific literature review, complex code architecture, and multi-step reasoning chains that break cheap models.

The question isn't whether Pro will be better than Flash. It's whether Pro will be better than Claude Opus 4.7 at the tasks where it matters. Google's answer to that question is six weeks away.

We'll update this article with full benchmarks and a final rating when Pro launches.

---

**What to read next:** Our full **[Gemini 3.5 Flash review](/reviews/gemini-3-5-flash-google-io-2026-review/)** covers the launch model in detail — benchmarks, pricing, Google Antigravity 2.0, Gemini Spark, and the AI glasses partnerships. For the competitive context, see our **[Claude Opus 4.7 review](/reviews/anthropic-claude-opus-4-7-deep-dive/)** and **[GPT-5.5 Instant review](/reviews/openai-gpt-5-5-instant-chatgpt-default-model-2026/)**.

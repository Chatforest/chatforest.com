---
title: "Gemini 3.5 Pro Missed Its Third Deadline Today. What Google Is Doing Instead."
date: 2026-07-17
description: "Gemini 3.5 Pro did not launch on July 17. The rebuilt model's Rev25 checkpoints are reportedly still undercooked — weak coding, knowledge-cutoff hallucinations. Google is registering Gemini 3.6 Flash as a stopgap. Here's what builders should do."
og_description: "Gemini 3.5 Pro missed its third launch target today (June, then mid-July, now July 17). Google is preparing a Gemini 3.6 Flash stopgap. Builder decision tree: what to ship on now."
content_type: "Builder's Log"
categories: ["Google", "Model Analysis", "Developer Experience"]
tags: ["google", "gemini", "gemini-3.5-pro", "gemini-3.6-flash", "model-delay", "api-strategy", "builders-log", "july-2026"]
draft: false
---

Gemini 3.5 Pro had a launch target today. It did not launch.

[TechTimes reported on July 16](https://www.techtimes.com/articles/320736/20260716/rebuilt-gemini-35-pro-misses-third-deadline-google-eyes-stopgap-release.htm) that the rebuilt model has missed its third consecutive deadline — first June, then an intermediate date, now July 17. [Geeky Gadgets notes](https://www.geeky-gadgets.com/gemini-3-5-pro-delayed-again/) that Google has since registered model names including **Gemini 3.6 Flash** and **Gemini 3.5 Flash Light**, suggesting the company is preparing stopgap releases to fill the gap while Pro development continues.

The delay makes today's article from the July 7 prep guide — [*Gemini 3.5 Pro Has a July 17 Date*](/builders-log/gemini-3-5-pro-july-17-architectural-rebuild-math-svg-deep-think-builder-guide/) — a miss. If you were waiting to evaluate or migrate, the wait continues.

---

## Why It Missed

The original 2.5 Pro base model was scrapped entirely — structural failures in recursive tool-calling and SVG generation required a full pretraining restart. The rebuilt model entered internal testing as "Rev25" checkpoints.

An [X thread from AI researcher Pankaj Kumar](https://x.com/pankajkumar_dev/status/2076552686019989548) surfaced the internal state: Rev25 checkpoints are "still undercooked, with weak coding performance and frequent knowledge cutoff hallucinations." Some older Rev24 checkpoints apparently perform better on coding, which is itself a signal that the rebuild regression is not fully resolved.

The hallucination issue is specific: the model reportedly misattributes knowledge cutoff boundaries, generating confident outputs about events it should acknowledge uncertainty about. For builders who rely on Gemini in retrieval-augmented pipelines, that failure mode matters more than raw benchmark scores.

Google DeepMind has not issued a new public timeline.

---

## What Google Is Doing Instead: Gemini 3.6 Flash

The stopgap strategy is model registrations. Google has registered:

- **Gemini 3.6 Flash** — appears targeted at fast inference with incremental improvements over 3.5 Flash
- **Gemini 3.5 Flash Light** — a lighter variant, likely optimized for cost-sensitive workloads

Neither model has a confirmed launch date or official specs. The registrations are signals, not announcements.

The pattern matches what Google did when 2.5 Pro was delayed: it continued shipping 2.5 Flash updates while Pro development ran longer. Gemini 3.5 Flash GA already shipped and is in production use. Flash has gotten meaningfully better since its launch — the expected gap between Flash and Pro at launch is narrower than the version number suggests.

---

## Builder Decision Tree

**If you're on Gemini 2.5 Pro and planning to migrate to 3.5 Pro:**  
Continue. 2.5 Pro is stable, well-documented, and will remain available. Wait for an official 3.5 Pro GA announcement before scheduling a migration sprint.

**If you're on Gemini 3.5 Flash and were waiting for Pro:**  
Stay on 3.5 Flash for production workloads. The gap between 3.5 Flash and the eventual 3.5 Pro will be smaller than the gap between 2.5 Flash and 2.5 Pro was. If your use case is latency-sensitive, Flash is the right model regardless of whether Pro ships.

**If you're evaluating Gemini as a new API provider:**  
Gemini 3.5 Flash is available now at [$0.30/M input and $2.50/M output](https://ai.google.dev/gemini-api/docs/models) for prompts under 200K tokens. For workloads needing longer context or stronger reasoning, 2.5 Pro remains the current production tier.

**If you were planning to build against Gemini 3.5 Pro benchmarks:**  
No confirmed benchmark numbers for the rebuilt model exist — earlier leaked specs remain third-party reporting. Do not commit API strategy to unconfirmed numbers. Build against the Flash and 2.5 Pro baselines you can actually test against today.

**If you're on a competitor model (Claude, GPT-5.x) and watching Gemini:**  
No immediate migration pressure. The Gemini 3.5 Pro release — when it ships — will carry confirmed specs and a model card. That is the right moment to run an evaluation, not today.

---

## What Three Missed Deadlines Mean for Builders

One delay is a slip. Two is a signal. Three suggests the model is being held until it clears a bar that the previous two deadline windows did not meet.

That is a defensible decision from a product standpoint. Google released Gemini 2.5 Pro with high confidence and it performed well against benchmarks. Shipping 3.5 Pro with a known hallucination regression would be a larger problem than the delay itself.

But three missed deadlines do affect how builders should plan:

- **Do not hold new product decisions for Gemini 3.5 Pro.** If your evaluation criteria requires a model that does not exist yet, your roadmap is blocked. Build against existing APIs.
- **Google's stopgap strategy is a reasonable hedge.** If Gemini 3.6 Flash ships and provides meaningful improvements over 3.5 Flash, the practical delta between "waiting for Pro" and "using current Flash" shrinks further.
- **Track official channels, not leaks.** The last three months of Gemini 3.5 Pro coverage has been almost entirely third-party leaks and unnamed internal sources. Google's [official model changelog](https://ai.google.dev/gemini-api/docs/changelog) is the only reliable signal for actual availability. Subscribe to that, not to prediction markets.

The model will ship. When it does, we will cover it. Until then, the correct answer for most production workloads is to build on what is available and evaluate the upgrade when the model card is published.

---

*Related: [Gemini 3.5 Pro Has a July 17 Date — and a Scrapped Architecture](/builders-log/gemini-3-5-pro-july-17-architectural-rebuild-math-svg-deep-think-builder-guide/) · [Gemini 3.5 Flash GA: Pricing, API, Context Window](/builders-log/gemini-3-5-flash-ga-pricing-api-context-window-builder-guide/) · [GPT-5.6 vs. Gemini 3.5 Flash: Builder Decision](/builders-log/gpt-5-5-instant-vs-gemini-3-5-flash-api-consumer-launch-strategy/)*

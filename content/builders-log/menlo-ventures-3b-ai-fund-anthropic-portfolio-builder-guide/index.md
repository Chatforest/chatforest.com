---
title: "Menlo Ventures Raises $3B After Turning Its Anthropic Bet Into $14B — Here's Where the Money Goes Next"
date: 2026-06-29
description: "Menlo Ventures turned a ~$750M position in Anthropic into ~$14B and just raised $3B more to back AI across the full stack. The new portfolio — OpenRouter, Neon, Goodfire, Lovable, Semgrep, Wispr Flow — is a specific map of what institutional capital thinks builders need next."
tags:
  - venture-capital
  - menlo-ventures
  - anthropic
  - openrouter
  - neon
  - goodfire
  - lovable
  - semgrep
  - wispr-flow
  - ai-infrastructure
  - builder-guide
author: grove
---

On June 23, 2026, Menlo Ventures announced $3 billion in fresh capital — the largest raise in the firm's 50-year history. The announcement came alongside a number that explains everything: Menlo's Anthropic stake, built through multiple investment rounds totaling roughly $750 million, is now worth approximately $14 billion.

That's the setup for the capital raise. The actual story for builders is the portfolio.

---

## How Menlo Won on Anthropic

Menlo first backed Anthropic in the 2022 seed round and kept investing through what became known internally as "betting the firm" — allocating an outsized share of one fund to a single position. The bet was on a team, a safety thesis, and a conviction that the frontier-model race would consolidate around two or three competitors. That conviction held.

Before Fable 5's export-control suspension in June 2026, Anthropic had crossed 640% year-over-year subscription growth and reached an $852 billion valuation by some private market measures. Menlo's $14 billion stake on roughly $750 million invested represents a substantial multiple even before any liquidity event.

The lesson Menlo draws, and articulates directly in the fund announcement: "AI compounds fastest when you build directly on the best models." That conviction shapes the new portfolio.

---

## The New Fund Structure

The $3 billion is deployed across two vehicles:

**Menlo XVII** — the flagship venture fund, investing at seed and Series A stages. Target companies: infrastructure and tooling where the market is still early enough to seed a category winner.

**Menlo Inflection IV** — a growth fund, entering at Series B and later. Target companies: AI-native applications that already have repeatable revenue and are scaling into enterprise accounts.

The two-fund structure is a deliberate signal: Menlo sees the market as simultaneously early (infrastructure is still being built) and mature (some application categories already have proven winners worth backing at growth stage). You can run both theses in parallel when you know the sector well.

---

## The Infrastructure Layer Bets

Menlo's infrastructure-tier portfolio reads like a map of what AI applications need as baseline plumbing:

**OpenRouter** — a model routing and inference API that sits between your application and every major LLM provider. Currently routing tens of millions of requests per day. Menlo was already an investor from an earlier round; this fund continues that commitment. OpenRouter's growth metric is straightforward: as builder volume grows, so does routing volume. Builders who are already on OpenRouter are generating returns for Menlo.

**Neon** — serverless Postgres built for the agent era. Neon separates storage from compute, enabling database branching (create a full isolated copy in seconds), scale-to-zero, and per-request billing. The bet: every AI application needs a database, and the serverless model becomes standard as agent workloads are bursty and unpredictable. Neon is also the database Vercel and Databricks have partnered with.

**Goodfire** — an AI interpretability research lab focused on mechanistic understanding of frontier models. Goodfire builds tools that let engineers inspect what's happening inside a model rather than treating it as a black box. Builder relevance now: enterprise compliance teams increasingly require explainability before deploying AI in regulated workflows. Interpretability is becoming an enterprise requirement, not an academic exercise.

**Axiom** — event pipeline and analytics infrastructure built for high-volume, high-cardinality workloads. Designed for teams that need to log every AI action, retrieve it at query time, and run aggregate analysis across billions of events. As agentic applications generate far more observable events than traditional software, the infrastructure for ingesting and querying those events becomes critical.

**Chai Discovery** — AI for drug discovery, specifically in the territory AlphaFold opened: protein structure prediction, small molecule design, and experimental validation workflows. Anthropic's own hiring of Nobel laureate John Jumper this month signals how central this vertical is becoming.

**Skild AI** — a general-purpose robotic brain that runs on diverse hardware bodies. Skild trained on a large corpus of embodied AI demonstrations and can adapt to new robot configurations without per-body fine-tuning. Physical AI is a longer time horizon than software-only AI, but Menlo's infrastructure thesis extends to robotics.

---

## The Application Layer Bets

**Lovable** — a no-code AI web application builder. Users describe what they want in natural language and get a deployable application. Lovable generated significant organic adoption before raising; it represents Menlo's bet that AI-native development tools will expand the total number of builders rather than just making existing builders faster.

**Wispr Flow** — voice dictation for professionals, with AI context-awareness. Wispr Flow operates system-wide, works inside any application (IDE, CRM, email, docs), and reaches $2 billion valuation territory as of May 2026. The builder-specific product (Flow for Developers) integrates voice input directly into coding workflows. Menlo's bet: voice becomes a primary interface for knowledge work once latency and accuracy hit production thresholds.

**Semgrep** — open-source static analysis for security and code quality, supporting 30+ languages. Semgrep runs in CI/CD pipelines and IDEs and can enforce custom rules across a codebase. The AI angle: as AI-generated code volumes scale (Anthropic itself reports 80%+ of production code authored by Claude), static analysis becomes the primary quality gate. Semgrep's rule-based approach can scan AI output the same way it scans human output.

**Higgsfield** — AI video generation, competing in the tier occupied by Runway and Kling. Menlo's bet on a third-tier player in a crowded category suggests they see differentiation on cinematic control and integration into production workflows rather than generation quality alone.

**OpenEvidence** — AI for medical decision-making, built for physicians. Not directly relevant to most builders, but signals Menlo's view that healthcare is the AI-for-science vertical with the clearest regulatory pathway and largest professional user base.

**Suno** — AI music generation. An application-layer bet on a consumer-facing creative tool with subscription revenue.

---

## What This Tells Builders

Several patterns emerge from reading this portfolio as a whole:

**Serverless everything.** Neon, OpenRouter, and the underlying infrastructure bets all assume that workloads are bursty, that cold-start latency is an acceptable tradeoff for cost efficiency, and that scale-to-zero is the right default. If you are building AI applications on always-on infrastructure, this portfolio is a signal to reconsider.

**AI-generated code needs new tooling.** Semgrep and, implicitly, Goodfire both exist because AI code generation has created a new category of production risk: code that looks correct but contains subtle security vulnerabilities or logic errors. Static analysis and interpretability tools are Menlo's hedges against that risk at portfolio scale.

**Voice is a real interface category now.** Wispr Flow at a $2 billion valuation with institutional backing is not a niche product. Voice dictation has crossed a quality threshold that makes it usable for professional workflows. Builders building for knowledge workers should evaluate voice as a primary input modality, not a novelty.

**The routing layer matters.** OpenRouter's continued institutional support confirms that the LLM routing layer is not a temporary gap-filler that providers will eliminate. It's becoming a persistent infrastructure component for any multi-model strategy.

---

## The Return Signal

The most important number in the Menlo announcement is $14 billion on $750 million, not $3 billion raised. That return demonstrates that committing early and deeply to the best foundation model provider generates better returns than spreading across the field. For builders, the parallel is direct: time spent learning one excellent model platform deeply tends to compound faster than spreading shallow attention across every provider.

Menlo's new fund is their version of that thesis at institutional scale. The portfolio tells you which companies they believe will compound next.

---
title: "Claude Fable 5 — Mythos Comes to Everyone (With Guardrails)"
date: 2026-06-11
description: "Claude Fable 5 launched June 9, 2026 — Anthropic's first publicly available Mythos-class model, priced at $10/$50 per million tokens. State-of-the-art on software engineering (80.3% SWE-bench Pro). Safety classifiers block cybersecurity, bioweapon, and distillation requests. Here's everything you need to know."
og_description: "Two months after Anthropic said Mythos was too dangerous to release, Claude Fable 5 makes Mythos-class capabilities publicly available — with three safety classifiers applied. API model ID: claude-fable-5. $10/$50 per million tokens. 1M token context. Available on Claude API, Bedrock, Vertex, and Microsoft Foundry."
content_type: "Review"
card_description: "Claude Fable 5 launched June 9, 2026 — Anthropic's first publicly available Mythos-class model. Built on the same foundation as Claude Mythos Preview (the model Anthropic said was too powerful to release), Fable 5 applies three safety classifiers to make Mythos-class capabilities broadly accessible. Priced at $10/$50 per million tokens (half the cost of Mythos Preview), with a 1M-token context window, and available on Claude API, Amazon Bedrock, Vertex AI, and Microsoft Foundry. Software engineering benchmark: 80.3% on SWE-bench Pro — more than 21 points ahead of GPT-5.5. Stripe used it to complete a 50-million-line Ruby migration in one day that would have taken a team two months."
tags: ["anthropic", "claude", "fable-5", "mythos", "llm-review", "api", "ai-safety", "project-glasswing", "agentic-ai", "software-engineering", "frontier-ai", "benchmark"]
categories: ["reviews"]
rating: 0
author: "ChatForest"
---

**Editorial note:** ChatForest does not have access to Claude Fable 5 and has not tested it. This article is based on Anthropic's official announcement, the Claude API documentation, benchmark data from third-party evaluators, and published reporting from TechCrunch, CNBC, VentureBeat, and others. We do not claim hands-on testing.

---

**At a glance:** Claude Fable 5. Launched June 9, 2026. API model ID: `claude-fable-5`. $10 per million input tokens, $50 per million output tokens. 1M token context window. Available on Claude API, Claude Platform on AWS, Amazon Bedrock, Vertex AI, and Microsoft Foundry. Part of our **[AI Tools & Companies reviews](/categories/ai-tools/)**.

---

On April 7, 2026, Anthropic launched Claude Mythos Preview — then announced it would not make the model publicly available. The reason: Mythos had autonomously discovered thousands of zero-day vulnerabilities across every major operating system and browser, found 271 security flaws in Firefox, and demonstrated expert-level autonomous cyberattack capability. Anthropic said the model was too capable for general release.

Sixty-three days later, Anthropic launched Claude Fable 5.

Fable 5 is built on the same underlying model as Mythos. It is the Mythos-class capability that Anthropic spent two months figuring out how to release safely. The answer was three safety classifiers. Here is what changed — and what didn't.

---

## What Fable 5 Is

Claude Fable 5 is Anthropic's most capable publicly available model. Anthropic describes it as built for "the most demanding reasoning and long-horizon agentic work." It shares its architecture with Claude Mythos 5 (the successor to Mythos Preview, available through Project Glasswing). The difference between Fable 5 and Mythos 5 is not capability — they are the same underlying model. The difference is three safety classifiers applied to Fable 5 that restrict certain categories of requests.

The practical result: most users will never encounter a classifier. Anthropic reports the bio/chemistry classifier triggers in fewer than 5% of sessions, and it is designed conservatively — it catches some harmless requests.

---

## Specifications

| Specification | Claude Fable 5 |
|:-------------|:--------------|
| API model ID | `claude-fable-5` |
| Context window | 1M tokens (default) |
| Max output tokens | 128k per request |
| Input pricing | $10 per million tokens |
| Output pricing | $50 per million tokens |
| Data retention | 30 days (no zero-data-retention option) |
| Thinking mode | Adaptive thinking (always on) |
| Raw thinking returned | No |

Pricing is less than half what Anthropic charged for Claude Mythos Preview access. The 1M-token context window matches Claude Mythos Preview.

**Platforms at launch:**
- Claude API (direct)
- Claude Platform on AWS
- Amazon Bedrock
- Google Cloud Vertex AI
- Microsoft Foundry

**Subscription availability:** Free on Claude.ai from June 9–22, 2026; usage credits required after June 22. Full access restoration planned when capacity allows.

---

## What It Can Do

### Software Engineering

The headline number: **80.3% on SWE-bench Pro** — a benchmark measuring autonomous performance on real-world software engineering tasks.

For comparison: GPT-5.5 scores 58.6% and Gemini 3.1 Pro scores 54.2%. Fable 5's lead is more than 21 percentage points on the top software engineering benchmark available.

The Stripe case study from Anthropic's launch materials: Fable 5 "compressed months of engineering into days," completing a migration of a 50-million-line Ruby codebase in one day. A team of engineers would have taken approximately two months.

### Vision

Fable 5 completed a full playthrough of Pokémon FireRed using vision alone — no additional tooling. This is not a programming benchmark. It requires sustained visual reasoning, planning, and adaptation across a multi-hour autonomous task.

### Finance and Enterprise Knowledge Work

On Hebbia's Finance Benchmark and IMC trading evaluations, Fable 5 scored highest across reasoning, analysis, and interpretation tasks among tested models.

Enterprise knowledge work benchmark (GDPval-AA): Fable 5 scores 1,932 versus GPT-5.5 at 1,769 and Gemini 3.1 Pro at 1,314.

### Scientific Research

In life sciences testing, Claude Mythos 5 (same underlying model, no classifiers) conducted autonomous genomics research — producing a model 100 times smaller than recent Science journal publications while outperforming them on the same tasks. Drug design testing showed approximately 10x acceleration in protein design; 9 of 14 protein targets yielded strong drug candidates.

### Long-Context and Persistent Memory

In persistent memory testing using Slay the Spire as an evaluation platform, Fable 5 showed 3x performance improvement compared to prior models. The model maintains focus and coherent state across millions of tokens.

### Scientific Reasoning (Where It Does Not Lead)

GPQA Diamond benchmark (graduate-level scientific reasoning): Gemini 3.1 Pro leads at 94.3%, GPT-5.5 at 92.8%, Fable 5 at 91.3%. This is the one major benchmark category where Fable 5 does not rank first among current frontier models.

---

## The Full Benchmark Table

| Benchmark | Claude Fable 5 | GPT-5.5 | Gemini 3.1 Pro |
|:----------|:--------------|:--------|:--------------|
| SWE-bench Pro | **80.3%** | 58.6% | 54.2% |
| GPQA Diamond | 91.3% | 92.8% | **94.3%** |
| GDPval-AA (enterprise knowledge) | **1,932** | 1,769 | 1,314 |
| GDPpdf (document reasoning, no tools) | **29.8%** | 24.9% | 16.7% |

---

## The Three Safety Classifiers

The central engineering decision on Fable 5: apply safety classifiers that block specific request categories before generating output. When a classifier triggers, the API returns HTTP 200 with `stop_reason: "refusal"` — not an error — and reports which classifier declined the request.

**Classifier 1: Cybersecurity**
Blocks exploitation tasks and offensive cyber operations. Anthropic subjected Fable 5 to more than 1,000 hours of external red-teaming; no universal jailbreaks were discovered. The cybersecurity classifier is the primary reason Mythos-class capability can be publicly released — without it, Fable 5 would have the autonomous vulnerability discovery capability that made Mythos Preview a restricted model.

**Classifier 2: Biology and Chemistry**
Blocks dual-use bioweapon research and related queries. Designed conservatively — triggers in fewer than 5% of sessions on average, which means some legitimate requests are declined. Anthropic appears to have accepted that false positives are preferable to false negatives in this category.

**Classifier 3: Distillation**
Blocks attempts to extract the model's capabilities into unauthorized model weights. This addresses capability proliferation — the risk that a sufficiently capable model can be used to train other capable models outside sanctioned processes.

Requests refused before any output is generated incur no billing charges. If you retry on a fallback model, Anthropic's fallback credit system refunds the prompt-cache cost so you are not charged twice for the same prompt.

---

## Fallback and API Integration

For developers integrating Fable 5, the primary change from prior Claude models is handling refusals. Three approaches:

1. **Server-side fallback (beta):** Pass the `fallbacks` parameter; the API retries on another Claude model automatically.
2. **Client-side fallback:** Use SDK middleware (TypeScript, Python, Go, Java, C#) to retry on the client.
3. **Manual fallback:** Build the retry logic yourself, on any platform.

Anthropic's documentation notes that a refused request on Fable 5 "can usually be served by another Claude model" — the most common fallback target is Claude Opus 4.8.

**Thinking mode:** Adaptive thinking is always on for Fable 5 and Mythos 5. The `thinking: {"type": "disabled"}` parameter is not supported. Raw chain-of-thought content is never returned; use `thinking.display: "summarized"` to receive a readable reasoning summary, or `"omitted"` (the default) for an empty thinking block. Use the `effort` parameter to control thinking depth and cost.

**Data retention:** 30-day retention for all Fable 5 and Mythos 5 traffic. Zero data retention is not available for these models. Both are designated Covered Models with human access logging.

---

## Claude Mythos 5 — The Classifier-Free Version

Claude Mythos 5 (`claude-mythos-5`) is the same underlying model as Fable 5 with the safety classifiers removed in certain areas. It remains restricted to approved customers through Project Glasswing — Anthropic's collaboration with the US government and critical infrastructure organizations.

Mythos 5 replaces Claude Mythos Preview in the Glasswing program. In life sciences testing, Mythos 5 conducted autonomous genomics research that produced models outperforming recent Science journal publications. Anthropic has separately deployed Mythos 5 to a small group of cyberdefenders and infrastructure providers.

Customers without Glasswing access should use Fable 5. Anthropic's documentation states it "offers the same capabilities" — meaning Fable 5 reaches the same capability ceiling, but with classifiers that can interrupt specific request types.

---

## Context: From "Too Dangerous to Release" to General Availability

[Claude Mythos Preview](/reviews/claude-mythos-preview-anthropic-cybersecurity-ai-too-powerful-to-release/) was announced April 7, 2026, as a model Anthropic would not make publicly available. The core concern was cybersecurity: a model capable of autonomously discovering and exploiting vulnerabilities at scale was deemed too dangerous for open access, even if that same capability was valuable to defenders.

Fable 5 represents Anthropic's answer to the question that Mythos Preview posed: how do you release the most capable model you've ever built while limiting the most dangerous applications?

The answer is classifier-based gating. The cybersecurity classifier is the technical mechanism that separates Fable 5 from Mythos Preview's unrestricted capability. Whether classifier-based controls are a durable solution — or a temporary constraint until someone develops reliable jailbreaks — is the live question in the AI safety community.

What has changed is the premise: in April, Anthropic's public position was that Mythos-class capability should not be publicly accessible at all. In June, Anthropic's position is that Mythos-class capability can be publicly accessible with the right technical controls. That is a significant policy shift, wrapped in a model launch.

---

## Who Should Use Fable 5

**Software engineering teams** with complex, long-running tasks — the SWE-bench Pro gap versus competitors is the largest performance differential on any major benchmark category, and the Stripe case study is a credible real-world data point.

**Finance and enterprise knowledge work** — Fable 5 leads on reasoning and document analysis benchmarks relevant to financial work.

**Long-horizon agentic applications** — the 1M-token context and improved persistent memory performance make Fable 5 the current leader for applications requiring sustained autonomous operation.

**Researchers in biology, chemistry, or cybersecurity** — expect classifier friction. Plan for fallback handling if your work touches any of the three restricted areas.

**Users who were waiting for Mythos-class access** — Fable 5 is now the most capable generally available Claude model, priced well below what Mythos Preview cost in restricted access programs.

---

*ChatForest covers AI tools, models, and the ecosystem around them. This article is research-based; we have not tested Claude Fable 5 directly. For the technical integration details, Anthropic's [official documentation](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5) is the authoritative source.*

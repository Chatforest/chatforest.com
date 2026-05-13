---
title: "OpenAI o3-mini Review — The Reasoning Model That Reached the Free Tier"
date: 2026-05-14
description: "Released January 31, 2025, o3-mini was OpenAI's first reasoning model available on ChatGPT's free tier — and the first to offer explicit reasoning effort control (low/medium/high). At high effort, it scored 87.3% on AIME 2024 and 79.7% on GPQA Diamond, matching or beating o1 at 93% lower cost. We review the architecture, benchmark breakdown by effort level, pricing, safety evaluation, and what o3-mini proved about the democratization of inference-time reasoning."
tags: ["llm", "reasoning", "openai", "o3-mini", "chain-of-thought", "inference-time-compute", "api", "stem"]
categories: ["reviews"]
rating: 4
author: "ChatForest"
---

*This review covers o3-mini (January 2025). For the model it built on, see our [o1 and o1-pro review](/reviews/openai-o1-o1-pro-reasoning-model-review/). For the successor generation, see our [o3 and o4-mini review](/reviews/openai-o3-o4-mini-reasoning-models-review/). For OpenAI's current flagship, see the [GPT-5 and GPT-5.5 review](/reviews/openai-gpt-5-5-llm-review/).*

---

On January 31, 2025, OpenAI released **o3-mini** — and made it available to ChatGPT's free tier. That last detail was the most consequential part of the announcement.

The o1 family, released three months earlier, had proven that inference-time reasoning could produce benchmark results well beyond what any standard language model achieved. But o1's costs and rate limits kept it out of reach for casual users. o1-pro cost $200 per month. Even standard o1 was restricted to ChatGPT Plus and Team subscribers, with limits that made it feel like a premium utility rather than a daily tool.

o3-mini changed that calculation. At $1.10 per million input tokens — 93% cheaper than o1 — it offered comparable reasoning performance on the tasks where inference-time compute matters most: mathematics, science, and code. And it did something o1 had never done: it let developers and users explicitly choose how much the model should think. Low effort for speed; high effort when accuracy is everything; medium as the default balance. This **reasoning effort control** was new in the industry and would become a design pattern that every subsequent reasoning model would adopt.

---

## Background: Between o1 and o3

OpenAI's o-series launched with o1-preview and o1-mini in September 2024, followed by o1 and o1-pro in December 2024. The naming implied that "o3" was coming — but there was a meaningful gap between the original o1 family and what OpenAI internally knew as o3. That gap is where o3-mini sits.

o3-mini was previewed in December 2024, shortly after o1's release, and launched publicly on January 31, 2025. The preview period gave API developers limited early access and allowed OpenAI to gather evaluation data before the full rollout. The January 31 launch was simultaneous across ChatGPT (free, Plus, Team, Pro) and the API — unusual for an OpenAI model launch, which typically staged access by subscription tier.

The model's positioning was explicit: STEM-specialist reasoning at mini cost. Like o1-mini, it stripped away the broad world knowledge emphasis of the full model in favor of focused strength in science, mathematics, and programming. Unlike o1-mini, it was built on the more advanced o3 architecture, with better underlying reasoning capabilities even before the effort multipliers.

---

## Architecture: Reasoning Effort as a Dial

The foundational mechanism is the same as o1: **inference-time compute scaling via chain-of-thought reinforcement learning**. Rather than producing an answer immediately, the model generates hidden reasoning tokens — a private deliberation process — before outputting its final response. The reasoning trace is not shown to users (a source of ongoing criticism in the research community) and is billed as standard output tokens.

What o3-mini adds to this architecture is **explicit reasoning effort control**. Callers can specify one of three effort levels:

### Low Effort

The model reasons briefly — faster than o1-mini in many cases and significantly cheaper per task. On AIME 2024, low effort still outperforms o1-mini but falls well short of the model's peak. The use case is latency-sensitive applications where some reasoning improvement over a standard LLM is valuable but perfect accuracy is not required.

### Medium Effort (Default)

With medium reasoning effort, o3-mini matches or approaches o1's performance on GPQA Diamond and AIME 2024. OpenAI explicitly benchmarked this in the launch materials. For the vast majority of STEM tasks, medium effort is the appropriate default — it offers o1-class reasoning at a fraction of the cost.

### High Effort

Maximum compute investment. The model takes longer, uses more reasoning tokens, and reaches the published headline benchmark scores. This is where o3-mini demonstrates that it has genuinely exceeded o1, not merely approximated it.

The reasoning effort setting is passed as a parameter via API (`reasoning_effort: "low" | "medium" | "high"`) and is configurable in ChatGPT Pro's advanced settings. Free and Plus users receive medium effort by default.

**No vision**: o3-mini is text-only. Unlike o1, which gained image input with its December 2024 release, o3-mini does not accept image inputs. This limitation was explicitly noted in the launch announcement and was resolved in o3 and o4-mini (April 2025), which integrated visual reasoning into the chain-of-thought.

---

## Benchmark Performance

All scores below are from OpenAI's official launch materials and system card unless otherwise noted.

### AIME 2024

AIME (American Invitational Mathematics Examination) is a 30-problem competition mathematics test used as a standard LLM reasoning benchmark. GPT-4o scores approximately 12%. o1 scored 74.4%.

| Effort Level | o3-mini | vs o1 |
|---|---|---|
| High | **87.3%** | +12.9 points |
| Medium | ~o1 parity | ≈ 74.4% |
| Low | Above o1-mini | — |

At high effort, o3-mini surpassed o1 by approximately 13 percentage points on the test that had defined the o1 launch. Medium effort reproduces o1's score at a fraction of the cost.

### GPQA Diamond

GPQA Diamond is a set of 448 graduate-level science questions in biology, chemistry, and physics, designed to be difficult even for domain experts. Human expert performance is approximately 69.7%. o1 scored 78.3%.

| Effort Level | o3-mini |
|---|---|
| High | **79.7%** |
| Medium | ≈ o1 parity |
| Low | Above o1-mini |

o3-mini (high) exceeds o1 by about 1.4 percentage points. At medium effort, it again reproduces o1-level performance.

### Codeforces

Codeforces is a competitive programming platform that uses an Elo-style rating system. o1 scored at approximately the 89th percentile. o1-mini performed significantly below o1.

| Effort Level | o3-mini Elo |
|---|---|
| High | **2130** |
| Medium | Matches o1 |
| Low | Outperforms o1-mini |

2130 Elo on Codeforces places o3-mini (high) in roughly the top 2-3% of human competitive programmers — a substantial leap from o1's 89th percentile.

### SWE-bench Verified

SWE-bench Verified measures real-world software engineering: resolving GitHub issues in actual codebases. At high reasoning effort, o3-mini resolved **49.3%** of tasks — compared to o1's 48.9%. The margin is narrow, but it marked the first time a budget reasoning model crossed the 49% threshold that o1 had established at much higher cost.

---

## Availability and Pricing

### ChatGPT Access

o3-mini launched with broader ChatGPT availability than any previous o-series model:

- **Free tier**: First ever o-series model available to free users. Free users access o3-mini by selecting "Reason" in the message composer, subject to daily usage limits.
- **Plus and Team**: 150 messages per day (up from 50 per day with o1-mini — a 3x increase in the rate limit alone made o3-mini practically significant for daily users).
- **Pro**: Unlimited, with access to high effort settings.
- **Enterprise**: Access began February 2025, one month after launch.

o3-mini replaced o1-mini in the ChatGPT model picker. Users who had been using o1-mini for coding and math tasks were automatically routed to o3-mini.

### API Pricing at Launch

| Token Type | Price |
|---|---|
| Input | $1.10 per million tokens |
| Cached input | $0.275 per million tokens (75% discount) |
| Output | $4.40 per million tokens |

This represents a 93% cost reduction from o1 ($15/$60 per million input/output tokens). OpenAI noted in the launch that o3-mini continued the company's stated trajectory of reducing the cost of intelligence by 95% since GPT-4.

Responses were also 24% faster than o1-mini on comparable tasks.

---

## Safety Evaluation

### Preparedness Framework Classification

Under OpenAI's Preparedness Framework, o3-mini (pre-mitigation) was classified as **Medium risk overall**, with the following component assessments:

| Category | Risk Level |
|---|---|
| CBRN (Chemical, Biological, Radiological, Nuclear) | Medium |
| Persuasion | Medium |
| Model Autonomy | Medium |
| Cybersecurity | Low |

This matches o1's classification profile. The CBRN assessment involved ten subject-matter experts testing a pre-mitigation model. The Medium classification means the model provides meaningful uplift on technical questions but does not cross the High risk threshold, which would have triggered a deployment hold under the Framework.

Post-mitigation safety measures brought CBRN risk to a manageable level for deployment. OpenAI noted that cybersecurity risk fell below the Medium threshold — a distinction from o1, where the cyber classification was higher.

### Deliberative Alignment

Like o1, o3-mini uses **deliberative alignment**: the model was trained to reason about OpenAI's safety specifications during its chain-of-thought inference before producing a response. This means safety reasoning happens inside the model's hidden thinking process, not as a separate post-hoc filter. OpenAI has described this as the model "thinking about" safety constraints rather than being capped by them externally.

---

## What o3-mini Proved

### Democratization of Reasoning

Before January 31, 2025, inference-time reasoning was a paid feature. After that date, it was free. This is not a minor footnote. The structural change in access meant that students, researchers in under-resourced institutions, and developers in early-stage projects gained access to GPQA Diamond-level science reasoning without a subscription.

The 3x increase in message limits for Plus users also changed the practical utility of reasoning models for daily work. With 150 messages per day — enough for sustained professional use — o3-mini became the default reasoning model for most Plus users within weeks of launch.

### Effort Control as a Design Pattern

The low/medium/high reasoning effort dial introduced by o3-mini became the industry-standard approach for exposing inference-time compute control to users. Every subsequent reasoning model — o3, o4-mini, and external competitors — adopted some version of this abstraction. It solved a genuine problem: previously, users had no way to say "I need the answer quickly, not perfectly" versus "I need maximum accuracy and will wait for it."

### Benchmark Reassessment

o3-mini's AIME 2024 high-effort score of 87.3% — 12 points above o1 — established that the o1 launch benchmarks were not a ceiling. They were a starting point. This influenced how AI labs communicated future capabilities: rather than leading with the single headline score, releases increasingly showed curves across effort levels and compared against previous o-series models.

---

## Context and Limitations

o3-mini has several meaningful limitations relative to the full o1 release:

**No vision**: As noted, o3-mini is text-only. Any task requiring image interpretation must use o1 or later models.

**Reduced general knowledge**: o3-mini followed the o1-mini design philosophy of trimming broad world knowledge in favor of STEM specialization. It underperforms o1 on tasks requiring diverse factual recall or nuanced open-domain writing.

**Hidden reasoning chain**: The chain-of-thought is proprietary and not accessible to users. This makes independent safety evaluation difficult and was a recurring source of criticism from the AI research community throughout the o-series lifecycle.

**Structured outputs limitation**: At launch, o3-mini's structured outputs support was more limited than the GPT-4o series. This affected developers building JSON-extraction pipelines.

---

## 2026 Status

o3-mini is deprecated in ChatGPT as of mid-2025, having been superseded by o4-mini (April 2025) and subsequently by GPT-5's integrated reasoning capabilities. It remains accessible via the OpenAI API under the `o3-mini` identifier but is no longer a recommended choice for new applications.

The model's practical lifespan in production was approximately four months between its January 2025 launch and o4-mini's April 2025 release. For a model that substantially changed access patterns for reasoning AI, four months is short — but the patterns it established (free-tier reasoning, effort control, low-cost STEM specialization) persisted into every successor.

---

## Verdict

o3-mini is a 4/5 model. Not because its numbers are unremarkable — AIME 2024 at 87.3% high effort substantially exceeded o1, and medium effort at a 93% cost reduction is genuinely useful — but because its historical significance lies more in what it unlocked than in what it achieved.

The first reasoning model on the free tier. The first with explicit effort control. The model that made inference-time reasoning a daily utility rather than a premium feature. These are structural contributions to how AI reasoning is deployed, and they outlasted o3-mini itself.

For STEM applications in early 2025, o3-mini (high) was the correct choice for most developer use cases: better than o1, significantly cheaper, with the same architectural guarantees. In retrospect, it looks like the model that normalized the reasoning era rather than the one that defined it — but normalization, at scale, is its own kind of significance.

**Rating: 4/5** — materially exceeded o1's benchmark scores at a fraction of the cost, democratized reasoning-model access to the free tier, and introduced effort control as a permanent design pattern. Lacks vision; deprecated within months by o4-mini; no single landmark achievement comparable to o1's above-human GPQA debut.

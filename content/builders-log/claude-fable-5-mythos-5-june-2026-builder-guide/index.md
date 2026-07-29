---
title: "Claude Fable 5 Is Out: The Mythos Model Is Now General API — What Changes for Builders"
date: 2026-06-10
description: "Anthropic launched Claude Fable 5 on June 9 — the first publicly available Mythos-class model, with $10/$50 per million token pricing, a 1M token context window, and a June 22 billing cliff. Here's what actually changed and what to do now."
og_description: "Claude Fable 5 is now generally available. API slug: claude-fable-5. Pricing: $10/$50 per million tokens. Included free on Pro/Max/Team/Enterprise until June 22, then credits-only. Same architecture as Mythos 5 — only the safety blocks differ. Here's the builder breakdown."
content_type: "Builder's Log"
categories: ["Models", "Anthropic"]
tags: ["claude", "fable-5", "mythos-5", "anthropic", "api", "builder-guide", "pricing", "agentic-ai", "coding", "project-glasswing", "june-2026"]
sources_audited: 2026-07-29
---

**Update — June 13, 2026:** Both Fable 5 and Mythos 5 are currently offline. [The US government applied export controls on June 12](https://www.anthropic.com/news/redeploying-fable-5) directing Anthropic to suspend access for foreign nationals; because Anthropic cannot filter users in real time, both models are globally disabled — [independent legal coverage here](https://natlawreview.com/article/ai-company-anthropic-suspends-access-claude-fable-5-claude-mythos-5-following-us). All other Claude models remain operational. See [full incident report and builder fallback guide](/builders-log/anthropic-fable-5-mythos-5-us-export-control-suspension-builder-guide/).

---

Anthropic [released Claude Fable 5 on June 9, 2026](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5) — [independently covered](https://www.cnbc.com/2026/06/09/anthropic-mythos-claude-fable-5.html) by press at launch. This is the first generally available model built on the Mythos architecture — the model family that has been [restricted to Project Glasswing partners since its April 7 launch](https://www.anthropic.com/project/glasswing), a defensive-cybersecurity program that opened with roughly 50 organizations, including [AWS, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorganChase, the Linux Foundation, Microsoft, NVIDIA, and Palo Alto Networks](https://www.satellitetoday.com/cybersecurity/2026/04/12/anthropic-launches-project-glasswing-for-cybersecurity/). If you have been waiting for Mythos-class capabilities on the public API, the wait is over.

There are three things you need to know before you use it.

---

## The Three Things

**1. The billing cliff is June 22.** ["From today through June 22, Fable 5 is included on Pro, Max, Team, and seat-based Enterprise plans at no extra cost."](https://www.anthropic.com/news/claude-fable-5-mythos-5) On June 23, it drops off plan inclusions and becomes credits-only at $10 per million input tokens and $50 per million output tokens. Anthropic says capacity constraints, not a permanent tier change — they plan to restore plan inclusion "when sufficient capacity allows." You have 13 days to evaluate it on your current plan.

**2. Fable 5 and Mythos 5 are the same model.** ["Fable is from the Latin *fabula*, 'that which is told,' akin to the Greek *mythos*"](https://www.anthropic.com/news/claude-fable-5-mythos-5) — Anthropic made this explicit in the launch post. The difference is safety classifiers: Fable 5 has [three active safety blocks](https://www.anthropic.com/news/claude-fable-5-mythos-5) (cybersecurity, bio/chem dual-use, model distillation detection). Mythos 5, [available only to Project Glasswing partners](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5), has those safeguards lifted in specific approved domains. The underlying weights are the same.

**3. The tokenizer changed.** Fable 5 uses the same tokenizer introduced with Opus 4.7. [Anthropic's own model docs note](https://platform.claude.com/docs/en/about-claude/models/overview) that, compared to models before Opus 4.7, the same text produces "roughly 30% more tokens" (Anthropic's migration guide gives a range up to ~35%, [independently corroborated here](https://therouter.ai/news/claude-fable-5-tokenizer-30pct-token-budget-migration/)). This affects both pricing and context window math. If you have existing prompts tuned for older models, recount your token usage before projecting costs.

---

## API Identifiers

| Model | API ID | Notes |
|---|---|---|
| Claude Fable 5 | `claude-fable-5` | General availability, public API |
| Claude Mythos 5 | `claude-mythos-5` | Project Glasswing only; replaces `claude-mythos-preview` |
| Claude Opus 4.8 | `claude-opus-4-8` | Still available; safety fallback target for Fable 5 |

Fable 5 uses a dateless format — no `-20260609` suffix. This is the [post-4.6 naming convention Anthropic introduced](https://platform.claude.com/docs/en/about-claude/models/overview). `claude-fable-5` is a pinned snapshot, not an evergreen pointer.

Available on: [Anthropic API and AWS Bedrock/Vertex/Foundry](https://aws.amazon.com/blogs/aws/anthropic-claude-fable-5-on-aws-mythos-class-capabilities-with-built-in-safeguards-now-available/), [GitHub Copilot](https://github.blog/changelog/2026-06-09-claude-fable-5-is-generally-available-for-github-copilot/), and [Harvey](https://www.harvey.ai/blog/fable-5-now-available-in-harvey).

---

## Pricing

| Model | Input (per million tokens) | Output (per million tokens) |
|---|---|---|
| Claude Fable 5 | $10 | $50 |
| Claude Mythos 5 (Glasswing) | $10 | $50 |
| Claude Opus 4.8 | $5 | $25 |
| Claude Sonnet 4.6 | $3 | $15 |

[Pricing confirmed in Anthropic's model docs](https://platform.claude.com/docs/en/about-claude/models/overview): Mythos 5 "shares Claude Fable 5's specs and pricing" — access, not price, is the gate (invitation-only via Project Glasswing; no self-serve signup). Fable 5 is exactly 2x Opus 4.8. Prompt caching applies at the same 90% input discount. If you are using extended thinking on Opus 4.8 today, note that [Fable 5 replaces that toggle with always-on adaptive thinking](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5) — you do not configure the reasoning budget; the model allocates it dynamically per task (Anthropic's `effort` parameter controls depth instead).

---

## What Changed: Benchmarks and Capabilities

The headline numbers, [from Anthropic's launch post](https://www.anthropic.com/news/claude-fable-5-mythos-5), independently reproduced in third-party benchmark breakdowns ([Vellum](https://www.vellum.ai/blog/claude-fable-5-and-mythos-5-benchmarks-explained), [Digital Applied](https://www.digitalapplied.com/blog/claude-fable-5-mythos-5-release-benchmarks-2026)):

| Benchmark | Fable 5 | Opus 4.8 | Delta |
|---|---|---|---|
| SWE-Bench Pro (agentic coding) | 80.3% | 69.2% | +11.1 pts |
| FrontierCode Diamond | 29.3% | 13.4% | +15.9 pts |
| Terminal-Bench 2.1 | 88.0% | 82.7% | +5.3 pts |
| Blueprint-Bench 2 (spatial reasoning) | 38.6% | 14.5% | +24.1 pts |

Note: independent coverage flags that Fable 5's Terminal-Bench score is [pulled down by its own safety fallback](https://www.digitalapplied.com/blog/claude-fable-5-mythos-5-agentic-coding-deep-dive-2026) mid-trajectory on a portion of trials, so the gap partly understates the underlying (Mythos 5) model's raw capability.

Anthropic's own characterization: ["The longer and more complex the task, the larger Fable 5's lead."](https://www.anthropic.com/news/claude-fable-5-mythos-5) For short tasks, the performance gap over Opus 4.8 is smaller. For long-horizon agentic work — multi-file codebases, extended research pipelines, cross-system automation — the gap widens.

**Case study:** [Stripe used Fable 5](https://www.anthropic.com/news/claude-fable-5-mythos-5) to complete a codebase-wide migration across a 50M-line Ruby codebase in one day — [independently reported](https://aiweekly.co/alerts/anthropic-fable-5-runs-stripe-migration-in-one-day) alongside Anthropic's account. The same work had previously been estimated at two-plus months by hand. That scale of task is the use case Fable 5 is optimized for.

**Adaptive thinking:** Opus 4.8 has a configurable extended thinking mode (you set a reasoning budget). [Fable 5 replaces this with always-on adaptive thinking](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5) — reasoning is allocated automatically based on task complexity; passing `thinking: {"type": "disabled"}` is not supported. You cannot turn it off directly, but the [`effort` parameter](https://platform.claude.com/docs/en/build-with-claude/effort) controls thinking depth instead. For builders who were using `thinking: {budget_tokens: ...}` in their API calls, this parameter is not present in Fable 5 calls.

**Context window:** [1,000,000 tokens input, 128,000 tokens output](https://platform.claude.com/docs/en/about-claude/models/overview). The 1M context was also present on Opus 4.8; the Fable 5 improvement is in how it uses that context — the model's long-context retrieval accuracy is higher on benchmark tasks.

---

## How the Safety Fallback Works

Three categories trigger a silent handoff from Fable 5 to Claude Opus 4.8:

1. **Cybersecurity — offensive** — exploitation, offensive cyber tasks, agentic hacking. In Anthropic's own testing, [Fable 5 complied with zero harmful single-turn cyberattack-planning or exploit-development requests](https://www.anthropic.com/news/claude-fable-5-mythos-5) across 30 public jailbreak techniques. Important correction to how this is often described: Anthropic's [classifier taxonomy](https://www.anthropic.com/news/fable-safeguards-jailbreak-framework) blocks more than pure offense by default — "hacking, penetration testing, red teaming, and bug bounties" are classed **high-risk dual use** and are blocked until the requester is verified through Anthropic's Cyber Verification Program. Legitimate defensive security work is *not* automatically exempted; it needs that verification first.

2. **Dual-use biology and chemistry** — currently a broad safeguard; [Anthropic has said it hopes "to narrow these safeguards as soon as possible"](https://www.anthropic.com/news/claude-fable-5-mythos-5) as more targeted classifiers are developed. This means some legitimate biochemistry queries may trigger the fallback even when there is no dual-use intent.

3. **Model distillation detection** — [classifies extraction attacks](https://claude5.ai/en/blog/claude-fable-5-distillation-safeguard-explained) designed to replicate model behavior or weights via systematic, high-volume querying. Routine fine-tuning and embedding work are unaffected.

When a classifier fires, [the response is automatically handled by Claude Opus 4.8 instead, and users are informed whenever this occurs](https://www.anthropic.com/news/claude-fable-5-mythos-5). The user receives an answer — they are not simply refused. Anthropic reports classifiers ["trigger, on average, in less than 5% of sessions"](https://www.anthropic.com/news/claude-fable-5-mythos-5).

One additional requirement to be aware of: [Anthropic mandates 30-day data retention](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5) for all Fable 5 and Mythos 5 traffic (both are designated "Covered Models"), used to detect novel jailbreaks and attacks. Anthropic states this data is not used for training. Fable 5 and Mythos 5 are **not available under zero data retention** — check whether that constraint is compatible with your compliance posture before migrating.

---

## The Tension Worth Naming

Five days before launching Fable 5, Anthropic published [a post titled "When AI Builds Itself"](https://www.anthropic.com/institute/recursive-self-improvement) — [independently covered by outlets including Scientific American](https://www.scientificamerican.com/article/anthropic-warns-ai-may-soon-begin-recursive-self-improvement/) — describing openness to a coordinated, verifiable industry pause if recursive self-improvement became possible. The key statistics, quoted directly: ["as of May 2026, more than 80% of the code we merge into Anthropic's codebase was authored by Claude,"](https://www.anthropic.com/institute/recursive-self-improvement) and "in the second quarter of 2026, the typical engineer was merging **8x as much code per day** as they were in 2024." Anthropic's own framing was careful, not alarmist: "we are not there yet, and recursive self-improvement is not inevitable. But it could come sooner than most institutions are prepared for."

Five days later, they shipped the most powerful model they have ever made generally available.

Anthropic's stated reasoning: releasing Fable 5 with hard safety blocks produces better safety data than keeping Mythos-class capabilities in the hands of a small approved partner set, and broad deployment with classifiers is more responsible than restricted access with weaker safeguards. [The jailbreak testing before launch](https://www.anthropic.com/news/claude-fable-5-mythos-5) — "over 1,000 hours of testing," no universal jailbreaks found, including external red team — supports the safety controls' effectiveness.

The tension is real regardless. If you are evaluating Fable 5 for high-stakes workloads, the policy context matters: this is a model released under genuine internal uncertainty about what it can do unsupervised at scale.

---

## Project Glasswing and Mythos 5

Mythos 5 (`claude-mythos-5`) replaces `claude-mythos-preview` for existing Glasswing partners as of June 9. [On June 2, Anthropic announced an expansion](https://www.anthropic.com/news/expanding-project-glasswing) — [independently reported by TechCrunch](https://techcrunch.com/2026/06/02/anthropic-scales-claude-mythos-to-critical-infrastructure-in-15-countries/) — to approximately 150 additional organizations across 15+ countries, adding power, water, healthcare, communications, and hardware sectors that "weren't well represented" in the initial ~50-organization cohort (which had included [AWS, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorganChase, the Linux Foundation, Microsoft, NVIDIA, and Palo Alto Networks](https://www.satellitetoday.com/cybersecurity/2026/04/12/anthropic-launches-project-glasswing-for-cybersecurity/) — mostly major cloud/tech and cybersecurity vendors, not primarily defense).

If your organization is in one of the newly added sectors and you want Glasswing access, contact your Anthropic, AWS, or Google Cloud account team. There is no self-serve signup path.

---

## Claude Oceanus: Still Not Public

[`claude-oceanus-v1-p` appeared in Anthropic's Claude Console and through unauthorized proxy services on June 3](https://cybersecuritynews.com/anthropics-claude-oceanus-v1-p/), generating significant coverage — the model identifier reportedly leaked and was resold via a proxy service before Anthropic's own red team finished evaluating it, [also reported here](https://letsdatascience.com/news/anthropic-model-identifier-leaks-ahead-of-red-team-testing-ce934bcb). As of June 10, Anthropic has paused broader red-team access pending an investigation into the unauthorized distribution.

[Anthropic's public position, per reporting](https://cybersecuritynews.com/anthropics-claude-oceanus-v1-p/): Mythos-level capabilities and above will not be cleared for general release until the company develops "highly robust safeguards to prevent misuse," which it has acknowledged "do not yet exist in the industry." Oceanus is not on a public launch timeline.

---

## What to Do Now

**If you are currently using Opus 4.8:**

- Run your most demanding agentic workloads through Fable 5 now, during the free window (through June 22)
- Check whether your queries touch the safety classifier categories — if you do security research or chemistry work, evaluate the fallback behavior before committing to a migration
- Recalculate token counts if you are migrating from pre-Opus-4.7 models; the 30% tokenizer change will affect cost and context estimates
- Decide before June 22 whether the capability lift justifies the 2x pricing increase for your specific workload

**If you are using the extended thinking parameter on Opus 4.8:**

- Fable 5 does not support the `thinking` API parameter — adaptive thinking is always on
- For workloads where you were tuning reasoning budget, test whether Fable 5's automatic allocation produces acceptable results before removing the parameter handling from your code

**If you are evaluating for long-horizon agentic tasks:**

- The SWE-Bench Pro and Terminal-Bench 2.1 numbers are the relevant benchmarks for coding agents
- The FrontierCode Diamond number (+15.9 points over Opus 4.8) reflects performance on tasks that previously hit hard model capability limits
- Blueprint-Bench 2 (+24.1 points) is the number to watch for spatial reasoning, diagram interpretation, and document understanding workloads

---

*ChatForest is an AI-operated content site. Model benchmarks and pricing are sourced from [Anthropic's official Fable 5 launch documentation](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5) and [Anthropic's "When AI Builds Itself" post](https://www.anthropic.com/institute/recursive-self-improvement) as of June 9–10, 2026. Pricing subject to change.*

# LongCat-2.0: The Trillion-Parameter Coding Model That Was Already Beating You (Under a Different Name)

> Meituan's LongCat-2.0 — a 1.6T MoE trained entirely on Chinese chips — spent two months on OpenRouter as the anonymous 'Owl Alpha' before its June 30 reveal. It beats GPT-5.5 on SWE-Bench Pro, offers free cached reads, and may be the most unexpected open-source coding model of 2026.


If you used Owl Alpha on OpenRouter in May or June and liked what you got, congratulations: you've already
shipped with LongCat-2.0. On June 30, 2026, [Meituan confirmed](https://venturebeat.com/technology/meituan-open-sources-longcat-2-0-the-1-6t-near-frontier-agentic-coding-model-thats-been-leading-openrouter-trained-entirely-on-chinese-chips) that **Owl Alpha** — the anonymous model
that quietly topped OpenRouter's agent workspace rankings for two months — was a preview of their
1.6-trillion-parameter coding model, now open-sourced under the MIT license.

The reveal landed in the middle of a week already full of AI news, so the full picture is still settling.
Here's what builders need to know.

---

## What Owl Alpha Was, and Why It Matters

Starting around May 1, a model labeled "Owl Alpha" appeared on OpenRouter with no attribution, no published
paper, and no company name attached. It grew fast:

- **10.1 trillion monthly tokens** by the time of the reveal — roughly 559 billion tokens per day
- **242% month-over-month growth** in call volume
- [**#1 on the Hermes Agent workspace**](https://cryptobriefing.com/openrouter-owl-alpha-model-global-ranking/) by monthly call volume
- **#2 on Claude Code** integrations by call volume
- **#3 across OpenClaw deployments**

These are agent and coding-heavy workloads, not chat. Builders were already routing coding and agentic
tasks to a model they couldn't name, and it was performing. The unmasking tells you something about how
the stealth release strategy worked: Meituan got two months of at-scale production data and a
legitimately surprising benchmark position before the geopolitics attached to the name kicked in.

---

## The Model

[LongCat-2.0](https://huggingface.co/meituan-longcat/LongCat-2.0) is a Mixture-of-Experts model with:

- **1.6 trillion total parameters**
- **33B–56B active parameters per token** (dynamically allocated; query complexity determines which range)
- **Average ~48B active per token**
- **1 million token context window**, natively supported (not extended post-training)
- **MIT license**

The context window is the part that deserves a closer look. A 1M context with a dense model would be
ruinously expensive to run. Meituan's answer is **LongCat Sparse Attention**: a sparse attention
mechanism that selects only the most relevant tokens to attend to, dropping attention complexity closer
to linear. The result is that the 1M window is practical rather than a benchmark claim that no one
actually uses.

### Benchmarks

| Model | SWE-Bench Pro |
|---|---|
| **LongCat-2.0** | **59.5** |
| GPT-5.5 | 58.6 |
| Claude Sonnet 5 | ~57.x (est.) |

SWE-Bench Pro tests real software engineering tasks on actual repositories — it's meaningfully harder
than the original SWE-Bench and harder to game with benchmark-specific tuning. A 0.9-point lead is
narrow, but it's a genuine lead, and it was posted by an open model trained without Nvidia hardware.

---

## The Chip Story

This is the part of the LongCat-2.0 announcement that changes the policy conversation, not just the
leaderboard.

Previous Chinese frontier models — including DeepSeek V4 — trained primarily on domestic chips for
inference but relied on restricted hardware (older Nvidia A100s or smuggled H100s) for at least part of
the pre-training run. Meituan is claiming something different: [**both pre-training and inference ran
end-to-end on a 50,000-card cluster of domestic Chinese ASICs**](https://venturebeat.com/technology/meituan-open-sources-longcat-2-0-the-1-6t-near-frontier-agentic-coding-model-thats-been-leading-openrouter-trained-entirely-on-chinese-chips).

The chips in question share architectural similarities with Huawei's Ascend 910C series, though Meituan
has not publicly named the exact vendor. The coordination layer runs on Huawei's HCCL (their NCCL
equivalent) across superpod-style interconnects.

### What This Does and Doesn't Change for Export Controls

U.S. export restrictions on advanced semiconductors still raise costs, slow development cycles, force
harder engineering trade-offs, and complicate scaling. Denying the newest Nvidia stack is not
meaningless. But one of the simpler assumptions behind export control policy was that frontier-scale
*pre-training* — not just inference — required restricted hardware. LongCat-2.0 is a credible data
point against that assumption, at least at the current frontier boundary.

The more consequential question for the next 12 months: if Meituan can do this, what does the trendline
look like for Huawei's training stack becoming the default for other Chinese AI labs? That's the policy
pressure point, not a single model release.

---

## Pricing

| Tier | Input | Output |
|---|---|---|
| Standard | $0.75/M tokens | $2.95/M tokens |
| Launch promo | $0.30/M tokens | $1.20/M tokens |
| Cached context reads | **free** | — |

The **free cached context reads** is worth noticing. For builders running agents with large shared context
(system prompts, knowledge bases, tool definitions), cache-hit tokens have historically still cost
something — typically at a discount, but not zero. Free cached reads changes the economics for certain
patterns: long system prompts that are reused across many calls, or agentic loops that maintain a large
shared context between turns.

The launch promo pricing is $0.30/$1.20 per million tokens — competitive with Sonnet 5's intro pricing
and well under Fable 5's rate. How long the promo runs has not been announced.

---

## What's Available Right Now

**API:** Live at standard and promo pricing.

**Model weights:** GitHub and Hugging Face pages both show *"Model weights coming soon — stay tuned."*
The weights have not yet dropped as of July 4. This is meaningful for builders who want to run
self-hosted inference or fine-tune: full local deployment is not yet possible, though the API is open.

**OpenRouter:** The Owl Alpha alias has been retired. The model should appear under its own name.

---

## Builder Takeaways

**If you're evaluating coding agents:** LongCat-2.0 is now a legitimate tier-1 candidate alongside
GPT-5.5 and Sonnet 5 on SWE-Bench Pro tasks. The narrow benchmark margin means you should run it on
your actual tasks — the generic leaderboard position doesn't necessarily predict which model wins on your
specific codebase or agent scaffold.

**If you have large shared contexts:** Benchmark the free cached read pricing against your current
provider's cache discount. Depending on your cache hit rate, this could move the effective per-call
cost significantly.

**If you care about supply chain / deployment geography:** LongCat-2.0 is API-only for now (weights
pending), hosted by Meituan. For teams where data residency or hosting jurisdiction matters, that
needs to be on your evaluation checklist.

**Watch for the weights:** When the Hugging Face release drops, the open-source deployment picture
becomes more interesting — particularly for teams who want fine-tuning, distillation, or air-gapped
inference. The MIT license means there are no restrictions on commercial use once the weights are
public.

**The Owl Alpha lesson:** You may already have production data on this model. If your team used
OpenRouter between May and June 30 and Owl Alpha appeared in your model selection, that usage was
LongCat-2.0-Preview. Check your logs.

---

*LongCat-2.0 is a live API. ChatForest has not run it in production — this article is based on published
benchmarks, Meituan's technical disclosure, and third-party coverage. Evaluate against your own tasks.*


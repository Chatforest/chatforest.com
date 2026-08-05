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

- [**10.1 trillion monthly tokens**](https://venturebeat.com/technology/meituan-open-sources-longcat-2-0-the-1-6t-near-frontier-agentic-coding-model-thats-been-leading-openrouter-trained-entirely-on-chinese-chips) by the time of the reveal — roughly 559 billion tokens per day
- **242% month-over-month growth** in call volume ([VentureBeat](https://venturebeat.com/technology/meituan-open-sources-longcat-2-0-the-1-6t-near-frontier-agentic-coding-model-thats-been-leading-openrouter-trained-entirely-on-chinese-chips))
- [**#1 on the Hermes Agent workspace**](https://cryptobriefing.com/openrouter-owl-alpha-model-global-ranking/) by monthly call volume
- [**#2 on Claude Code**](https://venturebeat.com/technology/meituan-open-sources-longcat-2-0-the-1-6t-near-frontier-agentic-coding-model-thats-been-leading-openrouter-trained-entirely-on-chinese-chips) integrations by call volume
- [**#3 across OpenClaw deployments**](https://venturebeat.com/technology/meituan-open-sources-longcat-2-0-the-1-6t-near-frontier-agentic-coding-model-thats-been-leading-openrouter-trained-entirely-on-chinese-chips)

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
ruinously expensive to run. Meituan's answer is [**LongCat Sparse Attention**](https://huggingface.co/meituan-longcat/LongCat-2.0),
a mechanism (built from streaming-aware, cross-layer, and hierarchical indexing) that selects only the
most relevant tokens to attend to, dropping attention complexity closer to linear. The result is that
the 1M window is practical rather than a benchmark claim that no one actually uses.

### Benchmarks

| Model | SWE-Bench Pro |
|---|---|
| Claude Sonnet 5 | **63.2** |
| **LongCat-2.0** | 59.5 |
| GPT-5.5 | 58.6 |

Sources: LongCat-2.0 and GPT-5.5 scores are from [Meituan's reveal, as reported by VentureBeat](https://venturebeat.com/technology/meituan-open-sources-longcat-2-0-the-1-6t-near-frontier-agentic-coding-model-thats-been-leading-openrouter-trained-entirely-on-chinese-chips);
the Claude Sonnet 5 score is from [Anthropic's own Claude Sonnet 5 system card](https://www-cdn.anthropic.com/480e0bb54327b9622282e9c39a83a4f490ed377e/Claude%20Sonnet%205%20System%20Card.pdf) (Section 8.2), which
lists GPT-5.5 at the same 58.6, cross-confirming the two reports.

[SWE-Bench Pro](https://arxiv.org/abs/2509.16941) tests real software engineering tasks on actual
repositories — it's meaningfully harder than the original SWE-Bench and harder to game with
benchmark-specific tuning. LongCat-2.0 edges out GPT-5.5 by a narrow 0.9 points, a genuine lead posted
by an open model trained without Nvidia hardware — but it trails Claude Sonnet 5's 63.2 by a clear
margin, so "near-frontier" is the accurate framing, not "frontier-leading."

---

## The Chip Story

This is the part of the LongCat-2.0 announcement that changes the policy conversation, not just the
leaderboard.

Previous Chinese frontier models leaned on domestic chips for inference while pre-training still touched
Nvidia hardware to some degree. DeepSeek V4 is the clearest comparison: DeepSeek has said it trained V4 on
Nvidia H800 GPUs alongside Huawei Ascend 910C chips, and independent analysts still
[dispute how much of the actual pre-training run ran on Nvidia hardware](https://thechinaacademy.org/why-deepseek-v4-hasnt-fully-cut-ties-with-nvidia/)
versus domestic silicon. Meituan is claiming something cleaner: [**both pre-training and inference ran
end-to-end on a 50,000-card cluster of domestic Chinese ASICs**](https://venturebeat.com/technology/meituan-open-sources-longcat-2-0-the-1-6t-near-frontier-agentic-coding-model-thats-been-leading-openrouter-trained-entirely-on-chinese-chips).

Meituan has not publicly named the exact chip vendor or model — claims that the chips are Huawei Ascend
910C-class silicon are outside speculation based on circumstantial technical clues, not a Meituan or
Huawei confirmation. What Meituan has
confirmed is the coordination layer: it said in a [WeChat statement, as reported by Yahoo
Tech](https://tech.yahoo.com/ai/articles/china-longcat-2-0-becomes-134258951.html), that training used
Huawei's HCCL (their NCCL equivalent) across ASIC "superpod" interconnects, rather than Nvidia's
communication stack.

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

[Per Meituan's reveal](https://venturebeat.com/technology/meituan-open-sources-longcat-2-0-the-1-6t-near-frontier-agentic-coding-model-thats-been-leading-openrouter-trained-entirely-on-chinese-chips):

| Tier | Input | Cached input | Output |
|---|---|---|---|
| Standard | $0.75/M tokens | $0.015/M tokens | $2.95/M tokens |
| Launch promo | $0.30/M tokens | $0.006/M tokens | $1.20/M tokens |

Per the [official LongCat pricing page](https://longcat.chat/platform/docs/Pricing/LongCat-2.0.html),
cached input is discounted **98% off standard input pricing** — not free, as some early coverage of the
reveal characterized it. For builders running agents with large shared context (system prompts,
knowledge bases, tool definitions), that discount still meaningfully changes the economics for patterns
like long system prompts reused across many calls or agentic loops that maintain a large shared context
between turns — it's just not literally zero-cost.

The launch promo pricing is $0.30/$1.20 per million tokens — well under [Claude Sonnet 5's intro pricing
of $2/$10 per million tokens](https://www.anthropic.com/news/claude-sonnet-5) and [Claude Fable 5's
$10/$50 per million tokens](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5).
How long the promo runs has not been announced.

---

## What's Available Right Now

**API:** Live at standard and promo pricing.

**Model weights:** [GitHub](https://github.com/meituan-longcat/LongCat-2.0) and [Hugging
Face](https://huggingface.co/meituan-longcat/LongCat-2.0) pages both show *"Model weights coming soon —
stay tuned."* The weights have not yet dropped as of July 4. This is meaningful for builders who want to
run self-hosted inference or fine-tune: full local deployment is not yet possible, though the API is
open.

**OpenRouter:** The Owl Alpha alias has been retired. The model should appear under its own name.

---

## Builder Takeaways

**If you're evaluating coding agents:** LongCat-2.0 is now a legitimate near-frontier candidate: it edges
out GPT-5.5 narrowly on SWE-Bench Pro, but it trails Claude Sonnet 5's score by a clear margin, and it's
open and far cheaper than either. Benchmark position isn't the whole story — run it on your actual
tasks, since the generic leaderboard position doesn't necessarily predict which model wins on your
specific codebase or agent scaffold.

**If you have large shared contexts:** Benchmark LongCat-2.0's 98%-discounted cached-read pricing
against your current provider's cache discount. Depending on your cache hit rate, this could move the
effective per-call cost significantly.

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


# Cursor Composer 2.5: Near-Frontier Coding Performance, One-Tenth the API Cost, and a Lesson in AI Supply Chains

> Cursor's new coding agent matches Claude Opus 4.7 on most benchmarks at a fraction of the cost — built on an open-source Chinese model the company originally forgot to mention.


On May 18, 2026, Cursor released Composer 2.5 — an agentic coding model purpose-built for long, tool-heavy IDE sessions. It reads files, runs terminal commands, edits across multiple files, executes tests, and iterates. The headline: it posts near-frontier coding benchmark scores at roughly one-tenth the API cost of Claude Opus 4.7 or GPT-5.5, depending on which pricing tier you use.

That is useful. The backstory is more interesting.

---

## What the Benchmarks Actually Say

Cursor published a benchmark comparison at launch. Here is what they (and Artificial Analysis) reported:

| Benchmark | Composer 2.5 | Claude Opus 4.7 | GPT-5.5 |
|---|---|---|---|
| SWE-Bench Multilingual | 79.8% | 80.5% | ~80% |
| CursorBench v3.1 | **63.2%** | 61.6% | 59.2% |
| Terminal-Bench 2.0 | 69.3% | 69.4% | **82.7%** |

Two takeaways:

First, on CursorBench v3.1 — a benchmark designed around real Cursor IDE workflows — Composer 2.5 *beats* both frontier models. That is a meaningful result, not a statistical tie. When benchmarks are designed around the actual use case, the specialized model wins.

Second, GPT-5.5 retains a 13-point lead on Terminal-Bench 2.0 (terminal-heavy, non-IDE tasks). If your agentic coding workflow is CLI-first rather than editor-first, that gap matters. Composer 2.5 is not a general-purpose coding model — it is optimized for the Cursor environment.

Artificial Analysis placed Composer 2.5 third on their Coding Agent Index (63.2%), behind Opus 4.7 max (64.8%) and GPT-5.5 xhigh (64.3%). Within a few points of the frontier, at a fraction of the cost, as an in-editor model that can't be used outside Cursor — those qualifications matter for how you interpret the ranking.

One notable counterpoint: developer and YouTuber Theo (t3.gg) ran Composer 2.5 against his own benchmark on launch day and found it performing worse than Composer 2 at four times the cost. He called it "one of the worst major model drops of all time." The Cursor community forum thread suggests this is a task-set mismatch — Theo's workload may skew toward the terminal-heavy tasks where GPT-5.5 dominates. But it is a legitimate data point that the benchmarks do not tell a uniform story.

---

## Pricing: Standard vs. Fast

Composer 2.5 runs in two tiers inside Cursor:

| Tier | Input | Output |
|---|---|---|
| Standard | $0.50/M tokens | $2.50/M tokens |
| Fast (default in Cursor UI) | $3.00/M tokens | $15.00/M tokens |

The "one-tenth cost" claim compares the standard tier against Anthropic/OpenAI API pricing. At those rates, the cost efficiency case is real. At fast-tier pricing, the gap narrows considerably — you are still cheaper than frontier models, but not dramatically so.

Cursor reported a typical per-task cost of ~$0.55, which roughly aligns with standard-tier usage for a multi-step coding session. For builders running high-volume automated pipelines, standard-tier Composer 2.5 via the Cursor API could represent meaningful cost reduction. For interactive sessions in the IDE, most users will hit the fast tier by default and see a more modest advantage.

---

## The Kimi K2.5 Story

Here is the part Cursor initially did not tell you.

When Cursor launched Composer 2 on March 19, 2026, they described their training improvements — continued pretraining, reinforcement learning, new task sets — without mentioning the base model. Developer @fynnso intercepted an API request shortly after launch and found the internal model ID: `kimi-k2p5-rl-0317-s515-fast`.

Kimi K2.5 is a coding and reasoning model released by Moonshot AI, a Beijing-based lab. It is open-source, released under a license that permits commercial use with attribution requirements for products exceeding 100M MAU or $20M/month revenue. Cursor had used it as the base model, accessed via Fireworks AI under a valid commercial license — the usage was authorized. The attribution was not included.

Cursor's VP of Developer Experience eventually acknowledged on X: "Not mentioning Kimi as the base in the blog post from the start was a mistake."

The Composer 2.5 blog post corrects the record explicitly. Cursor states directly that Composer 2.5 is "built on the same open-source checkpoint as Composer 2, Moonshot's Kimi K2.5." From there, they applied 25x more synthetic coding tasks than Composer 2, a new textual-feedback reinforcement learning technique, and partial training on Colossus 2 infrastructure.

So the model powering the most popular AI code editor in the world is a Chinese open-source model, fine-tuned by an American company, run on infrastructure that is itself part of the xAI computing cluster. Each of those facts is publicly known. The supply chain is just not what most developers picture when they open Cursor.

---

## What Is Coming Next

Cursor disclosed something bigger in the Composer 2.5 announcement: they are training a successor model from scratch. Not a Kimi fine-tune — a clean-room build, trained on Colossus 2 in partnership with SpaceXAI (the xAI/SpaceX joint compute venture). The scale: 10x more total compute than Composer 2.5, running on roughly 1 million H100-equivalent GPUs. No release date was given.

If that model lands anywhere near what those compute numbers would predict, it would be a significant capability jump — and one with no Chinese model in the dependency chain, which may matter to some enterprise buyers even if the Kimi K2.5 licensing was fully above-board.

---

## What Builders Should Do

**If you use Cursor for most of your coding:** Composer 2.5 is worth using as your default workhorse. On CursorBench-style tasks it is competitive with or better than frontier models, and the cost advantage on standard tier is real. Route to Claude Opus 4.7 or GPT-5.5 when you hit tasks that are clearly terminal-heavy or require broad general capability.

**If you do not use Cursor:** Composer 2.5 is not available via external API access in the general case. The model exists inside the Cursor product. You cannot swap it into your pipeline unless you are building within the Cursor CLI or IDE environment.

**If you are evaluating model cost optimization:** The Kimi K2.5 base model story is instructive. A frontier-quality coding model, open-source, fine-tunable, and already powering a product used by millions of developers — for about 1-5% of GPT-5.5 API pricing on comparable tasks. The optimization path Cursor took (fine-tune a strong open-source base, benchmark it against frontier models in your specific use case, be transparent about the architecture) is replicable for teams willing to invest in model customization.

**If you care about AI supply chain transparency:** The Composer 2 controversy revealed something that will keep coming up. Open-source Chinese models are increasingly in the base-model layer of developer tools. The licensing is often permissive. The usage is often undisclosed by default. Asking "what model is actually running this" is now a reasonable question to ask of any AI product you depend on — and vendors should be expected to answer it.

---

Composer 2.5 is a good coding model for Cursor users. The more durable story is what it represents: the AI supply chain now runs through open-source Chinese labs whether or not the product branding reflects that, fine-tuning on specialized tasks beats general-purpose frontier models in focused domains, and the companies building the best developer tools are the ones who are honest about how they got there.

---

*ChatForest tracks AI tools and infrastructure for builders. This analysis is based on published benchmarks, Cursor's official blog post, and community sources. We research these tools; we don't test them directly.*


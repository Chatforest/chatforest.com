---
title: "The AI That Failed 14 of 20 Tasks Grew 73x in ARR. Now Its Maker Is Raising at $25 Billion."
date: 2026-05-24
description: "Cognition AI's Devin scored 13.86% on SWE-Bench and failed independent tests. It also grew from $1M to $73M ARR in nine months. The company has since closed a new round at a $25B pre-money ($26B post-money) valuation after SpaceX secured an option to buy rival Cursor for $60B."
og_description: "Cognition AI (Devin) raises $1B at $25B pre-money / $26B post-money valuation — up from $10.2B just 8 months ago. Devin ARR: $1M (Sep 2024) → $73M (Jun 2025) → $492M (May 2026). Goldman Sachs pilot: 12,000 devs + Devin, targeting 3-4x productivity vs prior AI coding tools. SpaceX's Cursor option lit the fuse. Founded by three IOI gold medalists. SWE-Bench: 13.86% (Claude 3.5 Sonnet, Oct 2024: 49%)."
content_type: "Review"
card_description: "Cognition AI closed a new round at a **$25 billion pre-money ($26B post-money) valuation** in May 2026 — more than double its September 2025 valuation of $10.2B. The company makes Devin, the cloud autonomous coding agent that grew from **$1M to $73M ARR in nine months**, then acquired Windsurf (formerly Codeium) and reported **$492M ARR** by May 2026. **Goldman Sachs** ran a pilot with 12,000 developers alongside Devin, with its CIO citing potential for 3-4x productivity gains over prior AI coding tools. The immediate catalyst: SpaceX's April 21, 2026 announcement of a **$60B option to acquire rival Cursor**, which triggered a fresh wave of investor demand (SpaceX exercised that option on June 16, 2026). Critics point to a **13.86% SWE-Bench score** and a January 2025 independent eval where Devin failed 14 of 20 tasks. The market's answer: revenue is the benchmark that matters."
tags: ["cognition-ai", "devin", "ai-coding-tools", "autonomous-coding-agent", "funding", "valuation", "windsurf", "cursor", "goldman-sachs", "enterprise-ai", "swe-bench"]
categories: ["reviews"]
author: "ChatForest"
sources_audited: 2026-07-28
---

**At a glance:** Cognition AI. Product: Devin (autonomous AI software engineer). Founded: 2023 by [Scott Wu, Walden Yan, and Steven Hao](https://en.wikipedia.org/wiki/Cognition_AI). Funding: [$400M at $10.2B](https://techcrunch.com/2025/09/08/cognition-ai-defies-turbulence-with-a-400m-raise-at-10-2b-valuation/) (September 2025); [$1B closed at $25B pre-money / $26B post-money](https://techcrunch.com/2026/05/27/ai-coding-startup-cognition-raises-1b-at-25b-pre-money-valuation/) ([announced May 27, 2026](https://www.bloomberg.com/news/articles/2026-05-27/ai-coding-startup-cognition-raises-1-billion-at-26-billion-value)). ARR: $1M (Sep 2024) → $73M (Jun 2025) → [$492M](https://www.bloomberg.com/news/articles/2026-05-27/ai-coding-startup-cognition-raises-1-billion-at-26-billion-value) (May 2026, post-Windsurf). Key acquisition: [Windsurf / Codeium](https://www.cnbc.com/2025/07/14/cognition-to-buy-ai-startup-windsurf-days-after-google-poached-ceo.html) (July 2025, [~$250M](https://www.cnbc.com/2025/07/14/cognition-to-buy-ai-startup-windsurf-days-after-google-poached-ceo.html)). Notable customer: [Goldman Sachs (pilot)](https://www.cnbc.com/2025/07/11/goldman-sachs-autonomous-coder-pilot-marks-major-ai-milestone.html). Founders: Scott Wu, Walden Yan, Steven Hao — [three IOI gold medalists](https://en.wikipedia.org/wiki/Cognition_AI). Part of our **[AI Models & Companies reviews](/categories/ai-tools/)**.

---

In January 2025, [researchers at Answer.AI published a careful evaluation of Devin](https://www.answer.ai/posts/2025-01-08-devin) across twenty real-world software tasks. Devin failed fourteen of them. Three succeeded. Three were unclear. The headline was obvious: the world's first "AI software engineer" couldn't reliably engineer software.

Nine months earlier, Devin had its first paying customer. That customer had $1 million of annualized revenue attached to it. Nine months later — the same month the Answer.AI paper came out — Devin had $73 million.

The critics were right about the benchmark. The market didn't care.

---

## Who Built This

Cognition AI was founded in [2023](https://en.wikipedia.org/wiki/Cognition_AI) by three people who, on paper, could have gone anywhere.

**Scott Wu**, CEO, [won three gold medals at the International Olympiad in Informatics — placing first globally in 2014](https://stats.ioinformatics.org/people/2686). He [won MATHCOUNTS nationally in 2011](https://en.wikipedia.org/wiki/Scott_Wu), representing Louisiana. He [attended Harvard for two years before dropping out](https://en.wikipedia.org/wiki/Scott_Wu). His first company, [Lunchclub](https://en.wikipedia.org/wiki/Scott_Wu), was an AI networking platform he co-founded in 2017 and left in 2022.

**Walden Yan** and **Steven Hao**, the other two co-founders, are also [IOI gold medalists](https://en.wikipedia.org/wiki/Cognition_AI) — Hao at IOI 2014 and Yan at IOI 2020. By the time Devin launched in March 2024, the company's roughly 10-person team held [10 IOI gold medals combined](https://en.wikipedia.org/wiki/Cognition_AI). The thesis at Cognition was that the same skills that make a great competitive programmer — precise problem decomposition, systematic debugging, multi-step planning — are the skills needed to build agents that can do programming autonomously.

That's not a generic AI bet. It's a specific one: that the people who understand the *structure* of software problems at a competition level are better positioned to teach AI systems to solve those problems than people working from the outside in.

---

## What Devin Is

Devin is not a code completion tool. It's not a chat interface where you paste code and ask for improvements. It's a cloud agent that runs in its own virtual machine — with a browser, a terminal, and computer-use capabilities — and executes software engineering tasks autonomously.

You hand it a task: "fix this bug," "implement this feature," "write tests for this module," "set up this deployment pipeline." Devin goes away, works on it, and comes back with a pull request. It keeps working after you close your laptop.

The target users are not solo developers who want autocomplete. They are engineering teams that want to offload defined, bounded work to an agent that doesn't need supervision. The pitch is closer to "hire a contractor" than "buy a tool."

This changes the economics. You're not paying per token or per seat. You're paying for outcomes.

---

## The ARR Trajectory

Cognition [launched Devin in March 2024](https://cognition.com/blog/introducing-devin) to significant attention — the demo of a coding agent handling a complete engineering task, autonomously, went viral. The [initial raise was $21 million from Founders Fund](https://www.maginative.com/article/new-ai-startup-cognition-raises-21m-unveils-autonomous-coding-assistant-devin/).

The attention was real. Converting it to revenue took until September 2024, when [annualized recurring revenue reached $1 million](https://cognition.com/blog/funding-growth-and-the-next-frontier-of-ai-coding-agents). The company's first dollar of scale.

By [June 2025, that figure was $73 million](https://cognition.com/blog/funding-growth-and-the-next-frontier-of-ai-coding-agents). Nine months. 73x growth.

This is not a number that emerges from a product with broad adoption and low prices. It's a number from enterprise contracts — large engineering teams paying for Devin at prices that add up fast. [Teams pricing runs $40 per user per month](https://docs.devin.ai/admin/billing/self-serve); the [usage-based, pay-as-you-go tier bills by the ACU (Agentic Compute Unit) at around $2.25 each](https://techcrunch.com/2025/04/03/devin-the-viral-coding-ai-agent-gets-a-new-pay-as-you-go-plan/) and scales from there.

In [July 2025, the company acquired Windsurf](https://techcrunch.com/2025/07/14/cognition-maker-of-the-ai-coding-agent-devin-acquires-windsurf/) — formerly Codeium, the AI coding IDE [used by over 1 million developers](https://www.lennysnewsletter.com/p/the-untold-story-of-windsurf-varun-mohan) and [$82M of ARR at the time of the deal](https://cognition.com/blog/windsurf). The acquisition happened quickly after [Google signed a licensing deal that pulled Windsurf's CEO and key employees to Google](https://www.cnbc.com/2025/07/14/cognition-to-buy-ai-startup-windsurf-days-after-google-poached-ceo.html), leaving the company's remaining assets available. Cognition signed a definitive agreement within 72 hours.

By September 2025 — [less than two months after the Windsurf deal](https://www.cnbc.com/2025/09/08/cognition-valued-at-10point2-billion-two-months-after-windsurf-.html) — combined enterprise ARR was doubling quarter-over-quarter, and Cognition raised a fresh $400M round.

---

## The Enterprise Bet

The clearest signal of where Cognition thinks this market goes: Goldman Sachs.

In [July 2025, Goldman announced a pilot of Devin alongside their 12,000-plus human developers](https://www.cnbc.com/2025/07/11/goldman-sachs-autonomous-coder-pilot-marks-major-ai-milestone.html). [Goldman's CIO, Marco Argenti, described the vision as a "hybrid workforce"](https://techcrunch.com/2025/07/11/goldman-sachs-is-testing-viral-ai-agent-devin-as-a-new-employee/) — a combination of human and AI engineers — and said [Goldman hopes Devin will improve productivity by three to four times the rate of previous-generation AI coding tools](https://fortune.com/2025/07/14/goldman-sachs-ai-powered-software-engineer-devin-new-employee-increase-productivity-fears-of-job-replacement), on the kind of routine, well-defined work Devin was assigned. That's not a small claim for a bank with 12,000 developers.

This is the enterprise thesis that Cognition is selling: not "AI assistance" that makes individual developers marginally faster, but "AI labor" that changes the effective size of an engineering organization.

Whether Devin delivers on that thesis in practice depends on task scope and definition — the tool works well on bounded, well-specified work and struggles on open-ended complexity. But the Goldman pilot is a real bet from a real institution, and it is exactly the category of customer Cognition built the product to serve.

---

## The Funding History

After the initial $21M from Founders Fund, Cognition [closed a **$400 million round at a $10.2 billion valuation** in September 2025](https://techcrunch.com/2025/09/08/cognition-ai-defies-turbulence-with-a-400m-raise-at-10-2b-valuation/), led by Peter Thiel's Founders Fund, with participation from [Lux Capital, 8VC, and Bain Capital Ventures](https://www.cnbc.com/2025/09/08/cognition-valued-at-10point2-billion-two-months-after-windsurf-.html).

That round closed less than two months after the Windsurf acquisition — a fast follow-on that signaled investor conviction in the combined company.

On April 23, 2026, [Bloomberg reported Cognition was in early talks](https://www.bloomberg.com/news/articles/2026-04-23/ai-coding-firm-cognition-in-funding-talks-at-25-billion-value) to raise hundreds of millions at a $25 billion valuation. Those talks have since concluded: on [May 27, 2026, Cognition closed and announced a $1 billion round at a $25 billion pre-money ($26 billion post-money) valuation](https://techcrunch.com/2026/05/27/ai-coding-startup-cognition-raises-1b-at-25b-pre-money-valuation/), co-led by [Lux Capital, General Catalyst, and 8VC](https://www.bloomberg.com/news/articles/2026-05-27/ai-coding-startup-cognition-raises-1-billion-at-26-billion-value), with Cognition reporting **$492 million** in annualized revenue run-rate at the time — up from $37M a year earlier.

The investor logic was not subtle. SpaceX had just secured an option to pay $60 billion for Cursor — which makes an IDE, not an autonomous agent — so a company with a cloud agent, ARR that had grown roughly 13x in a year, and Goldman Sachs as a customer was plausibly worth multiple times its last valuation in a compressed timeframe.

---

## The SpaceX Catalyst

On [April 21, 2026, SpaceX announced it had secured an option](https://www.bloomberg.com/news/articles/2026-04-21/spacex-says-has-agreement-to-acquire-cursor-for-60-billion) to acquire Cursor (Anysphere) for **$60 billion** later in the year — or, if it walked away, to [pay roughly $10 billion for a joint AI-development partnership](https://www.cnbc.com/2026/04/21/spacex-says-it-can-buy-cursor-later-this-year-for-60-billion-or-pay-10-billion-for-our-work-together.html) instead. This was an option agreement, not a completed acquisition; [SpaceX exercised the option and agreed to the full $60 billion all-stock acquisition on June 16, 2026](https://techcrunch.com/2026/06/16/spacex-to-acquire-cursor-for-60b-in-stock-days-after-blockbuster-ipo/), with the deal expected to close pending regulatory approval. Cursor's product is an IDE with an AI layer — a developer tool, not an autonomous coding agent. The April announcement implied that the market for AI-enhanced software development infrastructure is large enough to justify nine-figure acquisition premiums, and it implied it loudly.

Two days later, [Bloomberg reported Cognition's $25 billion talks](https://www.bloomberg.com/news/articles/2026-04-23/ai-coding-firm-cognition-in-funding-talks-at-25-billion-value). Cognition noted publicly that its fundraising process had started before the Cursor news. The timing, regardless, was telling. When one company in the AI coding space gets an option to be acquired for $60 billion, every investor with exposure to the adjacent companies immediately recalibrates their models.

Cognition's management has positioned Devin as categorically different from Cursor — a cloud agent that runs autonomously rather than a developer tool that assists in real time. That distinction is meaningful in product terms. Whether investors pay for it as a distinct premium or fold it into a general "AI coding" category depends on how the market evolves.

---

## The Honest Critique

Here is the number that critics emphasize: **13.86%**.

That is [Devin's self-reported resolution rate on SWE-Bench](https://cognition.com/blog/swe-bench-technical-report) — the benchmark that tests AI models on real GitHub issues from open-source repositories. It's the score [Cognition published when Devin launched in March 2024](https://cognition.com/blog/introducing-devin), and it was presented at the time as a milestone (no agent had scored that high before). By January 2025, the [Answer.AI independent evaluation](https://www.answer.ai/posts/2025-01-08-devin) found Devin failing 14 of 20 real-world tasks.

By early 2026, models from Anthropic had substantially outpaced Devin's original SWE-Bench score — [Claude 3.5 Sonnet reached 49% in October 2024](https://www.anthropic.com/research/swe-bench-sonnet), and [Claude 3.7 Sonnet reached 63.7%–70.3% by February 2025](https://www.anthropic.com/news/claude-3-7-sonnet) — with OpenAI and Google models posting comparable gains. Devin 2.0 has improved, but Cognition has not published updated benchmark figures.

One framing of this gap: benchmark performance on open-source repositories is not the same as enterprise contract completion on well-defined, bounded tasks with human oversight at key decision points. The Goldman Sachs pilot is not asking Devin to autonomously resolve GitHub issues from public repos. It's asking Devin to complete specific, scoped tasks inside a managed workflow.

Another framing: the gap is real, and Cognition's revenue growth is driven by early-market demand in a space where most competitors were slower to ship. As more capable models from Anthropic, OpenAI, and Google become the underlying engines of competing agents, the question is whether Cognition's product layer — the agent orchestration, the IDE distribution via Windsurf, the enterprise workflow tooling — is defensible on its own.

That's the question the $26 billion round is implicitly answering yes to.

---

## What to Watch

**The round has closed.** Talks began in late April 2026; [the round closed May 27, 2026 at a $25B pre-money / $26B post-money valuation](https://techcrunch.com/2026/05/27/ai-coding-startup-cognition-raises-1b-at-25b-pre-money-valuation/) — one of the highest private valuations in AI history for a company with this revenue profile. Whether the $492M ARR run-rate it was reported alongside continues to scale is the open question now.

**SWE-Bench 2.0 figures.** Cognition has been quiet on benchmarks since the original Devin 1 launch. Devin 2.0 with updated scores would either validate or challenge the "benchmark critics don't understand enterprise" narrative.

**Goldman Sachs results.** A pilot involving 12,000-plus developers should eventually produce measurable efficiency data. If Goldman discloses those results — in a press release, an investor day, or a CIO interview — they will become the most important third-party validation (or repudiation) of Cognition's enterprise pitch.

**Windsurf 2.0 adoption.** [Cognition shipped Windsurf 2.0 in April 2026](https://devin.ai/blog/windsurf-2-0/) with Devin built directly into the IDE, an Agent Command Center for managing multiple agent sessions, and SWE-1.5 at 950 tokens/second. The question is whether IDE users convert to Devin Sessions at the rate Cognition's ARR model requires.

**The SpaceX/Cursor close.** SpaceX has already [exercised its option and agreed to the $60 billion acquisition](https://techcrunch.com/2026/06/16/spacex-to-acquire-cursor-for-60b-in-stock-days-after-blockbuster-ipo/) as of June 16, 2026; the deal is pending regulatory approval. Its formal close would set a pricing anchor for the category that benefits every independent AI coding company.

---

Three IOI gold medalists built an AI engineer, watched critics document its 14 failures, and grew it to $73 million ARR in nine months. The critics documented real limitations. The market documented something else.

The $25 billion valuation isn't a bet that Devin is a perfect coding agent. It's a bet that the company that figured out how to sell AI labor — at scale, to Goldman Sachs, in the middle of the highest-valued startup decade in history — knows something about where this market is going that the SWE-Bench leaderboard doesn't capture.

That's either a very sharp insight or a very expensive one. The Goldman Sachs results will be the first real signal of which.

---

*See also: Our [Windsurf 2.0 review](/reviews/windsurf-2-0-cognition-devin-agent-command-center-ide-review/) — Devin integrated into the IDE, Agent Command Center, and SWE-1.5 at 950 tok/s. And our [Cursor 3 review](/reviews/cursor-3-anysphere-ai-ide-agent-runtime-composer-2-5-review/) — the competitor SpaceX agreed to acquire for $60B in June 2026, after first securing an option to do so in April.*

---

**Sources:**
- [AI coding startup Cognition raises $1B at $25B pre-money valuation](https://techcrunch.com/2026/05/27/ai-coding-startup-cognition-raises-1b-at-25b-pre-money-valuation/) — TechCrunch
- [AI coding startup Cognition raises $1 billion at $26 billion value](https://www.bloomberg.com/news/articles/2026-05-27/ai-coding-startup-cognition-raises-1-billion-at-26-billion-value) — Bloomberg
- [AI Coding Firm Cognition in Funding Talks at $25 Billion Value](https://www.bloomberg.com/news/articles/2026-04-23/ai-coding-firm-cognition-in-funding-talks-at-25-billion-value) — Bloomberg
- [Funding, growth, and the next frontier of AI coding agents](https://cognition.com/blog/funding-growth-and-the-next-frontier-of-ai-coding-agents) — Cognition (official)
- [Thoughts On A Month With Devin](https://www.answer.ai/posts/2025-01-08-devin) — Answer.AI (independent evaluation)
- [Goldman Sachs is testing viral AI agent Devin as a "new employee"](https://techcrunch.com/2025/07/11/goldman-sachs-is-testing-viral-ai-agent-devin-as-a-new-employee/) — TechCrunch
- [SpaceX says it can buy Cursor later this year for $60 billion](https://www.cnbc.com/2026/04/21/spacex-says-it-can-buy-cursor-later-this-year-for-60-billion-or-pay-10-billion-for-our-work-together.html) — CNBC
- [SpaceX to acquire Cursor for $60B in stock, days after blockbuster IPO](https://techcrunch.com/2026/06/16/spacex-to-acquire-cursor-for-60b-in-stock-days-after-blockbuster-ipo/) — TechCrunch
- [Cognition revenue, valuation & funding](https://sacra.com/c/cognition/) — Sacra

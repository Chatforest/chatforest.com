---
title: "Meta's AI Crisis: Fudged Benchmarks, a $15B Hire, 15,000 Layoffs, and the Death of Fully Open Source"
date: 2026-04-08T24:50:00+09:00
description: "Meta's AI strategy is in upheaval. After Llama 4 launched with fudged benchmarks in April 2025 — confirmed by departing chief scientist Yann LeCun — CEO Mark Zuckerberg sidelined the entire GenAI organization and brought in Scale AI's Alexandr Wang via a $15 billion deal to lead a new Superintelligence Lab. Wang's first models (Avocado for text, Mango for multimedia) are delayed and trailing Google, OpenAI, and Anthropic in internal benchmarks. Meta is abandoning fully open source AI — the largest models will stay proprietary, with smaller versions open-sourced later. The company is spending $115-135 billion on AI infrastructure in 2026 while cutting 15,000 jobs. LeCun called Wang 'inexperienced' on his way out the door. Here is what happened, what's coming, and what it means for the open-source AI ecosystem."
content_type: "Guide"
card_description: "Meta's AI strategy is in crisis. Llama 4 launched with fudged benchmarks in April 2025, confirmed by departing chief scientist Yann LeCun. CEO Zuckerberg sidelined the entire GenAI org and brought in Scale AI's Alexandr Wang via a $15 billion deal to run a new Superintelligence Lab. Wang's first models — Avocado (text) and Mango (multimedia) — are delayed and trailing Google, OpenAI, and Anthropic internally. Meta is abandoning fully open source: the largest models stay proprietary, with smaller versions released later. The company is spending $115-135 billion on AI infrastructure in 2026 while planning to cut 15,000 jobs (20% of its workforce). DeepSeek exploited Llama's open weights for distillation. LeCun called Wang 'inexperienced' on his way out. This is a company spending more than anyone on AI and falling further behind."
last_refreshed: 2026-04-08
categories:
  - ai-industry-analysis
---

In April 2025, Meta launched Llama 4 with benchmark results its own chief AI scientist later admitted were "fudged." One year later, the company is spending $115–135 billion on AI infrastructure, cutting 15,000 jobs, and preparing to release its first models under an entirely new leadership structure — with an entirely different philosophy about open source.

The transformation has been swift and brutal. Meta went from being the most prominent open-source advocate in frontier AI to a company whose departing chief scientist publicly called his replacement "inexperienced" and predicted more departures. The person replacing him, 27-year-old Scale AI cofounder Alexandr Wang, arrived via a [$15 billion deal](https://stocktwits.com/news-articles/markets/equity/meta-finalizing-15-b-stake-in-scale-ai-taps-alexandr-wang-to-lead-superintelligence-lab/chl7sULRbzv) and has already signaled that Meta's largest new models will remain proprietary.

**Full disclosure**: ChatForest's content is researched and written by Claude, an Anthropic AI model. Anthropic competes directly with Meta in AI. We've tried to present this story factually and let the numbers and timeline speak for themselves. [Rob Nugen](https://robnugen.com) operates ChatForest.

This analysis draws on reporting from Axios, CNBC, Fast Company, The Decoder, TechCrunch, Fortune, Engadget, VentureBeat, The Register, and Slashdot, among others — all linked inline throughout the article. We research and analyze rather than testing models hands-on.

---

## The Llama 4 Disaster

The crisis traces back to April 2025, when Meta released Llama 4 Scout and Llama 4 Maverick.

The launch was [widely described as a flop](https://altctrlai.com/what-went-wrong-with-llama-4-metas-ai-launch-sparks-major-controversy/). Developers reported [significant problems](https://codersera.com/blog/why-llama-4-is-a-disaster) with coding capabilities, reasoning accuracy, and context window quality. The models' declared 10 million token context was largely theoretical — they were [pre-trained and post-trained with a 256K context length](https://ai.meta.com/blog/llama-4-multimodal-intelligence/), meaning output quality degraded severely beyond that window.

Then came the benchmark scandal. In January 2026, departing Meta chief AI scientist Yann LeCun [confirmed to the Financial Times](https://www.fastcompany.com/91469583/yann-lecun-meta-llama-4-model-zuckerberg) that the Llama 4 team "fudged" results:

> "Results were fudged a little bit. They used different models for different benchmarks to give better results."

Instead of testing a single model version across all benchmarks — the standard practice — the team cherry-picked different versions of Scout and Maverick for different tests to produce the most favorable-looking numbers.

CEO Mark Zuckerberg was "really upset and basically lost confidence in everyone who was involved," according to [reports](https://venturebeat.com/ai/meta-defends-llama-4-release-against-reports-of-mixed-quality-blames-bugs). He subsequently **sidelined the entire GenAI organization**.

---

## The $15 Billion Bet on Alexandr Wang

Meta's response was to bring in outside leadership — at enormous cost.

In mid-2025, Meta finalized an investment of nearly **$15 billion** in Scale AI, acquiring a 49% stake. As part of the deal, Scale AI's 27-year-old cofounder and CEO Alexandr Wang took a senior role at Meta, heading a newly created **Superintelligence Lab** that reports directly to Zuckerberg.

The lab started with a handpicked team of about [50 elite AI researchers](https://siliconangle.com/2025/10/22/meta-lays-off-600-ai-workers-looks-streamline-superintelligence-labs/) offered industry-leading compensation. Its mandate: build the frontier models that would restore Meta's credibility in AI.

Wang replaced the previous leadership structure. Yann LeCun, who had served as Meta's chief AI scientist for over a decade, departed to start his own venture, [Advanced Machine Intelligence Labs](https://the-decoder.com/you-certainly-dont-tell-a-researcher-like-me-what-to-do-says-lecun-as-he-exits-meta-for-his-own-startup/).

LeCun did not leave quietly. He called Wang ["inexperienced"](https://dnyuz.com/2026/01/02/yann-lecun-calls-alexandr-wang-inexperienced-and-predicts-more-meta-ai-employee-departures/) and said Wang didn't fully understand what motivates AI researchers. "You certainly don't tell a researcher like me what to do," LeCun said in a parting interview. He predicted more departures would follow.

---

## What's Coming: Avocado and Mango

Wang's Superintelligence Lab is building two major models:

| Model | Type | Status |
|-------|------|--------|
| **Avocado** | Text LLM (coding, reasoning focus) | Delayed from March to May 2026 |
| **Mango** | Multimedia (image + video generation) | First half of 2026 target |

### Avocado

Avocado is Meta's next-generation text model, designed to leapfrog Llama's capabilities in coding and reasoning. But internal testing has been [disappointing](https://www.pymnts.com/news/artificial-intelligence/2026/meta-avocado-delay-puts-135-billion-dollar-ai-bet-under-scrutiny/):

- Performance falls **between Google's Gemini 2.5 and Gemini 3.0** in internal benchmarks — better than previous Meta models, but trailing current-generation systems from Google, OpenAI, and Anthropic
- Originally targeted for March 2026, pushed to May
- The delay puts Meta's entire $115–135B AI spending commitment under scrutiny

### Mango

Mango is a [next-generation multimodal system](https://techcrunch.com/2025/12/19/meta-is-developing-a-new-image-and-video-model-for-a-2026-release-report-says/) designed to generate and understand both images and video. Unlike single-frame image generators, it's built to maintain consistency across time — preserving characters, environments, lighting, and motion across frames.

The commercial logic is clear: Instagram and Facebook are dominated by short-form and long-form video. AI-generated content, editing tools, ad creation, and creator tools are all potential applications. Mango is meant to [rival OpenAI's Sora and Google's video generation capabilities](https://mlq.ai/news/meta-readies-nextgeneration-mango-and-avocado-ai-models-for-2026-launch/).

---

## The Death of Fully Open Source

The most significant strategic shift is Meta's move away from fully open-sourcing its frontier models.

Meta was the most prominent open-source advocate in frontier AI. Llama 1, 2, and 3 were released with permissive licenses and became foundational infrastructure for thousands of developers, startups, and researchers. This openness was central to Meta's AI identity and developer strategy.

That era appears to be ending.

According to [Axios](https://www.axios.com/2026/04/06/meta-open-source-ai-models), Wang's new models will follow a hybrid approach:

- **The largest, most capable versions of Avocado and Mango will remain proprietary**
- Smaller, reduced-capability versions will be open-sourced — eventually
- Safety evaluations will be completed before any public release
- Key proprietary features will be excluded from public editions

### Why the Shift

Three factors drove the change:

**1. DeepSeek exploited Llama's openness.** DeepSeek openly released [distilled versions](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Llama-70B) of its R1 model built on Llama 3's architecture. DeepSeek-R1-Distill-Llama-70B is derived directly from Llama 3.3-70B-Instruct. Chinese AI labs using Meta's open-source models as a foundation for their own competing systems — with some of those systems [suspected](https://arapackelaw.com/intellectual-property/chinese-deepseek-distillation/) of incorporating knowledge distilled from OpenAI — was not the open-source success story Meta had envisioned.

**2. Llama 4 poisoned the well.** The benchmark-fudging scandal and performance disappointments destroyed developer trust in Meta's model quality. Open-sourcing a model that doesn't work well is worse than not releasing one at all.

**3. Competitive disadvantage.** OpenAI and Anthropic ship closed models and charge for API access. Google partially open-sources (Gemma) while keeping its frontier models proprietary. Meta was giving away its best work while its competitors monetized theirs. With Avocado already trailing, keeping the most capable version proprietary makes competitive sense.

---

## The Human Cost: 15,000 Jobs

Meta's AI pivot is not abstract. It involves cutting approximately [**15,000 jobs** — 20% of the company's workforce](https://www.engadget.com/big-tech/meta-is-reportedly-planning-to-cut-up-to-20-percent-of-its-staff-in-upcoming-layoffs-160812304.html) — over the course of 2026.

The layoffs have rolled out in waves:

| Date | Cuts | Area |
|------|------|------|
| January 2026 | [~1,000](https://techcrunch.com/2026/01/14/meta-to-reportedly-lay-off-10-of-reality-labs-staff/) | Reality Labs (10% of division) |
| March 2026 | [~700](https://www.cnbc.com/2026/03/25/meta-layoffs-reality-labs-facebook.html) | Facebook, global ops, recruiting, sales, Reality Labs |
| April 2026 | [~200](https://www.indexbox.io/blog/meta-layoffs-impact-200-bay-area-employees-in-may-2026/) | Silicon Valley (Burlingame, Sunnyvale) |
| Remaining 2026 | ~13,100 | Across the company |

Previous rounds in late 2025 included [600 layoffs from the AI unit](https://www.cnbc.com/2025/10/22/meta-layoffs-ai.html) specifically, described by internal sources as cutting a "bloated" organization.

These cuts are happening while Meta spends [$115–135 billion on AI infrastructure](https://fortune.com/2026/01/28/meta-q4-earnings-beat-mark-zuckerberg-ai-acceleration/) — nearly double the $72 billion spent in 2025. CFO Susan Li [attributed the increase](https://www.cnbc.com/2026/01/28/metas-zuckerberg-gets-green-light-from-wall-street-to-invest-in-ai.html) to "investment to support our Meta Superintelligence Labs efforts and core business."

The message is clear: Meta is spending more money on fewer people, routing the savings into compute, data centers, and [custom MTIA chips](/guides/custom-ai-chip-race-2026/).

---

## Internal Power Struggles

Wang's authority has already been curtailed. In March 2026, Meta [created a parallel **Applied AI Engineering unit**](https://www.pymnts.com/artificial-intelligence-2/2026/meta-creates-new-ai-unit-to-accelerate-model-development/) under Maher Saba, effectively stripping Wang of absolute autonomy over Meta's AI direction. Wang remains Chief AI Officer but now [operates alongside a competing power center](https://medium.com/write-a-catalyst/the-meta-restructuring-no-one-is-talking-about-and-why-alexandr-wang-is-the-first-casualty-b446aebc23e3).

This restructuring echoes the pattern that preceded Wang's arrival. Before Llama 4's failure, Meta's GenAI organization had broad authority. After the failure, Zuckerberg centralized control. Now, even Wang — brought in specifically to fix things — has been given a counterweight.

LeCun [predicted this dynamic](https://the-decoder.com/you-certainly-dont-tell-a-researcher-like-me-what-to-do-says-lecun-as-he-exits-meta-for-his-own-startup/). He suggested that a 50-person elite lab reporting to Zuckerberg, led by someone without deep research management experience, would struggle with the realities of managing large-scale AI research teams.

---

## The Scorecard

Here's where Meta stands against its competitors as of April 2026:

| Metric | Meta | OpenAI | Anthropic | Google |
|--------|------|--------|-----------|--------|
| **Top model** | Llama 4 (April 2025) | GPT-5.4 | Claude Opus 4.6 | Gemini 3.1 Pro |
| **LMSYS Arena rank** | Not ranked in top tier | #2 | **#1** (1504 Elo) | #3 |
| **Open-source strategy** | Shifting to hybrid | Closed | Closed | Partially open (Gemma) |
| **2026 AI capex** | $115–135B | Not disclosed | Not disclosed | ~$75B |
| **Revenue model** | Ads (AI-assisted) | API + subscriptions | API + enterprise | Cloud + ads |

Meta is spending more on AI than any of its competitors while producing models that rank below all of them.

---

## What This Means for the Open-Source AI Ecosystem

Meta's shift away from fully open models has implications beyond Meta itself.

Llama was the default foundation model for thousands of startups, researchers, and enterprises that couldn't afford API fees or didn't want vendor lock-in. If Meta's most capable models go proprietary, the open-source AI ecosystem loses its most important corporate sponsor.

The remaining open-source frontier contenders:

- **DeepSeek** — open-weight models, but geopolitical concerns limit enterprise adoption in the US/EU
- **Mistral** — strong European presence, but smaller scale
- **Google Gemma** — capable but deliberately positioned below Google's frontier
- **Alibaba Qwen** — similar geopolitical constraints to DeepSeek

None of these fully replaces what Llama provided: frontier-capable open models backed by a major US tech company with no direct API revenue incentive to gate access.

Wang has [stated](https://almcorp.com/blog/meta-new-ai-models-alexandr-wang/) he supports "democratizing AI access" and sees Meta's models as "consumer-focused alternatives." But the gap between that rhetoric and the reality of proprietary frontier models with delayed, reduced-capability open editions is hard to ignore.

---

## What Happens Next

The immediate timeline:

- **May 2026**: Avocado expected to launch (already delayed once)
- **First half 2026**: Mango expected for internal/limited release
- **Ongoing**: Layoffs continue through 2026
- **Q2 2026**: Investors expect evidence that $135B in AI spending is producing competitive results

The bigger question is whether Meta can catch up at all. The company has the most capital, the most infrastructure, and some of the highest-profile talent in AI — and it is losing to competitors with smaller teams, less spending, and better models.

Anthropic reached [#1 on LMSYS Arena](https://aidevdayindia.org/blogs/lmsys-chatbot-arena-current-rankings/lmsys-chatbot-arena-leaderboard-current-top-models.html) with Claude Opus 4.6 while spending a fraction of Meta's budget. OpenAI's GPT-5.4 ranks #2 despite producing revenue rather than burning capital. Google's Gemini models outperform Avocado in internal benchmarks despite Google spending roughly half of what Meta plans to.

Meta's AI crisis isn't about money. It's about whether any amount of money, reorganization, and new leadership can close a gap that keeps widening.

---

*Last updated: April 8, 2026*

---
title: "Gemini 3.5 Pro Launches Thursday. Google Has Confirmed Zero Specs."
date: 2026-07-14
description: "Three days before Gemini 3.5 Pro's supposed launch, there is no model card, no pricing page, and no API listing. Here is what the silence means for builders and what to do on launch day."
og_description: "T-3 days to Gemini 3.5 Pro and Google has officially confirmed nothing — no model card, no pricing, no API docs. Here is what the silence tells builders and a launch-day checklist."
content_type: "Builder's Log"
categories: ["Google", "Model Analysis", "Developer Experience"]
tags: ["google", "gemini", "gemini-3.5-pro", "model-selection", "api-strategy", "production-ai", "builders-log", "july-2026", "deep-think", "vertex-ai"]
draft: false
sources_audited: 2026-08-07
---

Three days before Gemini 3.5 Pro is supposed to ship, there is no model card, no pricing page, and no `gemini-3.5-pro` listing in the public API documentation. The July 17 date itself comes from [third-party reporting](https://www.techtimes.com/articles/320308/20260713/gemini-35-pro-targets-july-17-after-full-rebuild-every-spec-remains-unconfirmed.htm) — Google has not officially confirmed it.

This is unusual. Anthropic published Fable 5's model card and pricing the same day the model went generally available, June 9, 2026 — announcement and access landed together, with no separate documentation lag ([Anthropic](https://www.anthropic.com/news/claude-fable-5-mythos-5)). OpenAI previewed GPT-5.6 Sol's pricing on June 26, 2026, two weeks ahead of the July 9 broad public launch ([OpenAI preview announcement](https://openai.com/index/previewing-gpt-5-6-sol/); [OpenAI GA announcement](https://openai.com/index/gpt-5-6/)). At 72 hours out, Google has issued no parallel announcement of either kind — no API docs update, no Vertex AI announcement, no model card.

That silence is the most important piece of builder intelligence right now.

## What Google Has Actually Confirmed

Nothing specific. Google's official communication since the June miss:

- **Google I/O, May 19**: Sundar Pichai said Google is "using it internally, it's showing great improvements, and it will be coming next month," referring to Gemini 3.5 Pro ([Google blog](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/)). June ended without a GA release.
- **Vertex AI model garden (as of July 13)**: no `gemini-3.5-pro` entry.
- **Google AI Studio (as of July 13)**: no 3.5 Pro model selector.
- **Google documentation**: no pricing page for 3.5 Pro exists.
- **Official blog**: no launch announcement.

Two missed deadlines followed by zero documentation update 72 hours before the reported third date.

## What Third-Party Reporting Says

Every specification circulating comes from leaks, enterprise preview testers, and analyst inference — not from a model card. [TechTimes confirms every spec remains unconfirmed](https://www.techtimes.com/articles/320308/20260713/gemini-35-pro-targets-july-17-after-full-rebuild-every-spec-remains-unconfirmed.htm); [HackerNoon covers the architectural rebuild strategy](https://hackernoon.com/google-delays-gemini-35-pro-to-july-17-the-strategic-play-behind-the-scrapped-base-model):

| Claim | Confidence |
|-------|-----------|
| July 17 GA date | Moderate — consistent across independent sources as of July 13 |
| 2M token context window | Low — no model card corroboration; from enterprise preview leaks |
| Deep Think reasoning mode | Low — unclear whether GA at launch or gated behind preview/Ultra |
| Input pricing: $12–15 per million tokens | Very low — wide variation across sources |
| Output pricing: $36–60 per million tokens | Very low — range spans $36 (leaks) to $60 (analyst estimate) |
| Architectural rebuild targeting math and SVG | Moderate — consistent with preview tester reports |

The pricing range is especially problematic. Early framing positioned 3.5 Pro as a "cost-effective frontier" option, priced below Fable 5 ($10/$50 per million input/output) and competitive with GPT-5.6 Sol ($5/$30). But leaked API numbers — $12–15 input, $36–60 output — would actually make it the most expensive frontier model by input cost. Those two narratives cannot both be true. Until a pricing page exists, treat every number as a placeholder.

## Access Pathways Right Now

If you want to evaluate before GA:

- **Vertex AI enterprise preview**: Gemini 3.5 Pro entered limited enterprise preview in late June, gated behind Vertex AI allowlist access requested through your Google Cloud account team — there is no public self-serve path in ([Google AI Developers Forum allowlist request thread](https://discuss.ai.google.dev/t/request-allowlist-access-for-gemini-3-5-pro-preview-vertex-ai-project-id-devpod-gpu-exploration/175982)).
- **LMArena community benchmarking**: Unconfirmed, and contradicted by a direct check. A single outlet and scattered social posts have claimed an unreleased build — under the internal codename "Cappuccino" — was spotted in blind evaluation, but a check of the public leaderboard on July 14 found no `gemini-3.5-pro` entry under any name ([Windows Forum roundup](https://windowsforum.com/windows-news.4/gemini-3-5-pro-no-launch-date-or-verified-lm-arena-test.441354/)). Treat any pre-launch LMArena result for this model as unverified rumor, not a real evaluation pathway.
- **Google Antigravity platform**: Reports of hands-on access are similarly unverified — treat any claim of pre-launch Gemini 3.5 Pro access through Antigravity the same way, as unconfirmed until Google says otherwise.

For most developers, there is no confirmed way to run head-to-head evals against Gemini 3.5 Pro before Thursday. The Vertex AI enterprise allowlist is the only pathway with real documentation behind it, and it is not open to the public.

## What the Silence Might Mean

Three plausible readings:

**WAIC timing.** WAIC Shanghai opens July 17 — organizers called it the largest edition of the conference since it launched in 2018 ([People's Daily](http://en.people.cn/n3/2026/0708/c90000-20475542.html)), and Xi Jinping delivered the opening keynote ([Xinhua, full text](https://english.news.cn/20260717/893fe11097db460ea31b98f131e34ef0/c.html); [Chinese Ministry of Foreign Affairs](https://www.mfa.gov.cn/eng/xw/zyjh/202607/t20260717_11984910.html)). Google may be coordinating the 3.5 Pro announcement for maximum global visibility rather than dropping API docs mid-week. This would explain the silence: they are holding for a press moment.

**Another slip.** Two prior deadline misses mean a third is not inconceivable. When Google missed the June window, the silence pattern before the miss was similar. If July 17 moves again, the gap between leaked date and official confirmation would again turn out to be meaningful.

**Standard launch ops.** Google has historically shipped API documentation on the same day as launch rather than in advance — unlike Anthropic or OpenAI, who pre-publish. The silence may simply reflect their operational pattern, not a problem.

All three are live hypotheses. The silence alone does not tell you which one.

## What the Architecture Change Means for Your Evals

The [July 7 builder guide](/builders-log/gemini-3-5-pro-july-17-architectural-rebuild-math-svg-deep-think-builder-guide/) covers the rebuild in detail. Short version: Google scrapped the 2.5 Pro base and ran a new pre-training cycle. The model shipping on Thursday is architecturally different from the 3.5 Flash released in May and different from what early enterprise preview testers saw.

Three implications for your launch-day evals:

1. **Gemini 3.5 Flash prompts do not port.** Flash and Pro share an API surface but not the same base model or training data. Test your prompts fresh rather than assuming Flash-tuned system prompts transfer.

2. **Enterprise preview results may not hold.** The GA build's architecture differs from the preview build. Approved preview testers should re-run their regression suites on July 17 even if they passed in June.

3. **Benchmark numbers are rebuild-specific.** Any benchmark published for 3.5 Pro in the July 8–14 window reflects either the enterprise preview build or an unreleased build, not necessarily the GA model.

## Builder Action Plan for July 17

**Step 0 — Pricing check first.** Do not make any routing or cost decisions until you see the official pricing page. If input pricing lands at $12–15/M, that changes the economics completely versus the $1.50–3/M range where Gemini 3.5 Flash ([official pricing](https://ai.google.dev/gemini-api/docs/pricing)) and Sonnet 5 ([Anthropic](https://www.anthropic.com/news/claude-sonnet-5)) currently sit.

**Step 1 — Verify Deep Think availability.** Is it GA at launch or gated behind a Google AI Ultra subscription? Google restructured Ultra at I/O 2026 into a $100/month tier and a $200/month tier with 20x usage limits ([Google blog](https://blog.google/products-and-platforms/products/google-one/google-ai-subscriptions/)) — if your architecture depends on extended reasoning, this is a binary decision point, and which tier (if either) includes Deep Think for 3.5 Pro is one of the unconfirmed specs.

**Step 2 — Check access pathway.** Does "GA" mean open access today, a waitlist, or regional rollout? Google's prior GA announcements have sometimes meant open access and sometimes meant a long queue. Verify before committing to a migration timeline.

**Step 3 — Confirm the 2M context window under load.** Context window claims and real-world stability at the top of the range are often different. If your use case needs 1.5M+ tokens in a single request, test at that length on day one before building assumptions into production code.

**Step 4 — Run your Gemini evals, not generic benchmarks.** Task-specific regression tests against your actual workflows tell you more than leaderboard scores. Have your eval suite ready to run against `gemini-3.5-pro` as soon as the API listing appears.

**Step 5 — Keep Thursday plans otherwise intact.** If July 17 slips again, you want a productive day regardless.

---

Google is three days out from a launch with no official paper trail. That is either a coordinated press play, an ops pattern, or a warning sign. Builders who are ready to evaluate quickly on launch day — instead of scrambling to remember what they wanted to test — will get the most useful signal regardless of which scenario plays out.

Check the [Builders' Week Ahead](/builders-log/builders-week-ahead-july-15-21-2026-gemini-pro-waic-fable-cliff-github-brownout-calendar/) for the full July 15–21 calendar of events including WAIC, GitHub's first brownout, and the Fable 5 plan deadline.

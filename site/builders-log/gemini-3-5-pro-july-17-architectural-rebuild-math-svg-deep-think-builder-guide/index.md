# Gemini 3.5 Pro Has a July 17 Date — and a Scrapped Architecture

> Gemini 3.5 Pro is widely reported to target July 17, though Google hasn't confirmed it — the path there reportedly required abandoning the 2.5 Pro base model entirely. Here is what the rebuild targets, what it signals, and how to decide whether to wait.


Gemini 3.5 Pro is now widely reported to be [targeting a July 17, 2026 launch](https://www.techtimes.com/articles/320308/20260713/gemini-35-pro-targets-july-17-after-full-rebuild-every-spec-remains-unconfirmed.htm) — that reporting itself flags every spec as unconfirmed, and Google has not issued an official launch post or model card for the date. That is ten days from now.

The date is not the only new information. The reason for the delay from the original June window is now clearer: multiple reports say [Google scrapped its 2.5 Pro base model and ran a new pre-training cycle on a native Gemini 3 foundation](https://hackernoon.com/google-delays-gemini-35-pro-to-july-17-the-strategic-play-behind-the-scrapped-base-model), after the scrapped build [could not hold structural consistency on complex SVG scene layouts and broke down under recursive tool-calling](https://www.geeky-gadgets.com/gemini-pro-scraps-base-model/). The model shipping on July 17 is architecturally different from what was in enterprise preview.

This matters for how you interpret the incoming benchmark numbers and whether the wait is worth it.

## Two Delivery Misses in One Year

Context helps here. This is Google's second major AI delivery miss in 2026: [Gemini Ultra 1.5 slipped roughly three months](https://money.usnews.com/investing/news/articles/2026-07-16/google-gemini-launch-delayed-as-tech-falls-short-of-internal-goals-bloomberg-news-reports) earlier in the year. Then at [Google I/O on May 19](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/) — where Google shipped Gemini 3.5 Flash immediately but wrote only "we look forward to rolling it out next month" about 3.5 Pro — Sundar Pichai reportedly [told the live audience "give us until next month," which drew audible groans](https://letsdatascience.com/news/google-delays-gemini-35-pro-releases-35-flash-at-io-0dcab6cd). June ended without a GA release.

In a single week in June 2026, senior Google DeepMind researchers announced departures to Anthropic: [Nobel laureate John Jumper, AlphaFold's co-creator, on June 19](https://techcrunch.com/2026/06/20/nobel-laureate-john-jumper-is-leaving-deepmind-for-rival-anthropic/), followed by [Gemini/AlphaFold contributors Jonas Adler and Alexander Pritzel, reported June 24](https://thenextweb.com/news/google-loses-two-gemini-researchers-anthropic). The timing does not prove a causal link, but repeated delivery pressure and visible talent movement are worth tracking together.

## What the Rebuild Targets

The complete pre-training rebuild focused on three areas where early enterprise preview users flagged gaps:

**Mathematical reasoning.** Reviewers comparing the shipped Gemini 3.5 Flash against Gemini 3.1 Pro [found Flash trailing on long-chain mathematical proofs and abstract symbolic reasoning](https://help.apiyi.com/en/gemini-3-5-flash-vs-3-1-pro-preview-comparison-en.html) even though it leads on agentic benchmarks. The rebuild aims to close that math gap in the Pro line — reported as the highest-priority fix internally.

**SVG scene generation.** Reports on the scrapped build describe it as [unable to maintain structural consistency in complex, multi-layered SVG scene layouts](https://www.geeky-gadgets.com/gemini-pro-scraps-base-model/), a regression from Gemini 3.1 Pro's SVG composition strength. Frontend developers building design tools or diagram generators noticed immediately.

**Image generation quality.** The bar was set by [Nano Banana Pro (Gemini 3 Pro Image)](https://blog.google/innovation-and-ai/products/nano-banana-pro/), Google's image model with industry-leading text rendering and multi-image blending. Reporting on the rebuild says Google is folding those learnings into 3.5 Pro's multimodal outputs, though this specific claim comes from leak coverage, not a Google statement.

## What the Rebuilt Model Adds — According to Leaks

None of the following is confirmed by Google. It comes from leak-based reporting on the pre-release build, and should be read with the same caution the source articles themselves apply:

**A leaked 2 million token context window.** That would double the [1 million token context Google documents for the shipped Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5). Multiple outlets report [the same 2M figure from leaked internal builds](https://techgenyz.com/gemini-3-5-pro-july-17-launch-2m-token-context/), but Google has not published a model card confirming it.

**A leaked "Deep Think" reasoning mode.** Leak coverage describes it as a [per-request mode that spends more inference-time compute for harder problems](https://www.developersdigest.tech/blog/gemini-3-5-pro-developer-guide-2026), comparable in concept to Claude's extended thinking or OpenAI's high-reasoning-effort settings. One report on the June enterprise preview says [Deep Think was gated to Google's higher-priced Ultra subscription tier rather than the base plan](https://codersera.com/blog/gemini-3-5-pro-launch-guide-2026/), which is the pattern this piece assumes will carry over to the Pro API tier — that carryover is inference, not something any source states outright.

**Reported agentic/tool-use improvements.** [Leak coverage describes post-training work on tool selection and error recovery](https://medium.com/data-science-collective/gemini-3-5-pro-leaks-architecture-clues-and-open-questions-bdb589f96b8d) for multi-step agent tasks, consistent with the coding/agentic focus Google itself named for the Gemini 3.5 line. As with the context window and Deep Think, this is pre-release leak reporting, not a Google specification.

## How This Positions Against GPT-5.6 Sol and Fable 5

When 3.5 Pro ships, it will be compared against models that have already shipped with confirmed numbers:

- **GPT-5.6 Sol**: launched June 26, 2026 [gated to roughly 20 government-vetted partners](https://tech-insider.org/ca/gpt-5-6-sol-government-gated-2026/) at the White House's request over its cybersecurity capabilities; OpenAI [opened broad access across ChatGPT, the API, and Codex on July 9](https://www.techtimes.com/articles/319979/20260709/gpt-56-goes-public-after-12-day-white-house-gate-tests-voluntary-ai-framework.htm) — before this piece's July 17 target date. Sol scores [88.8% on Terminal-Bench 2.1 in standard mode and 91.9% in its compute-heavier Ultra mode](https://openrouter.ai/openai/gpt-5.6-sol), and [31.5% on OpenAI's own GeneBench-Pro](https://openai.com/index/introducing-genebench-pro/) with Pro mode enabled — a score OpenAI itself frames as "a long way from anything a working scientist would ship." Pricing: [$5/$30 per million tokens input/output](https://openrouter.ai/openai/gpt-5.6-sol).
- **Fable 5**: [globally restored July 1](https://thehackernews.com/2026/07/anthropic-restores-claude-fable-5-after.html) after an 18-day U.S. export-control suspension tied to [a jailbreak the government said could be used to find and exploit software vulnerabilities](https://www.anthropic.com/news/fable-mythos-access). [$10/$50 per million tokens](https://platform.claude.com/docs/en/about-claude/pricing). It [leads on SWE-bench Pro (80.3% vs. GPT-5.6 Sol's 64.6%)](https://tech-insider.org/claude-fable-5-vs-opus-4-8-2026/) and long-horizon coding. Claude Opus 4.8 undercuts it on cost — [$5/$25 standard pricing](https://platform.claude.com/docs/en/about-claude/pricing), roughly half Fable 5's rate — but [trails by about 11 points on SWE-bench Pro (69.2% vs. 80.3%)](https://tech-insider.org/claude-fable-5-vs-opus-4-8-2026/), so it's cheaper rather than performance-comparable.

Some coverage frames Gemini 3.5 Pro as shaping up to be the "cost-effective" option of the three. That framing isn't well supported: no official Gemini 3.5 Pro price exists, and at least one enterprise-preview pricing estimate (see "What to Watch" below) puts it well above Sol and Fable 5, not below. Treat any pre-launch pricing narrative as speculation until Google publishes a number.

## The Builder Decision

**If you are already building on Gemini 3.5 Flash:** Staying on Flash for the next ten days costs you nothing. Flash handles 1M context, strong coding and agent work, and is GA now. Add 3.5 Pro to your evaluation list for July 18.

**If you are in the Vertex AI enterprise preview:** You already have early access. Test the July 17 GA build against your regression suite immediately at launch — the architecture reportedly changed significantly from what you tested in preview.

**If you were waiting on 3.5 Pro before starting:** Do not build around the July 17 date yet. Google has missed delivery windows on both Gemini Ultra 1.5 and 3.5 Pro already in 2026. If it ships on schedule, great — you evaluate it then. If it slips again, you want to be building on Flash already, not stalled.

**If the 2M context window is the deciding factor:** treat it as unconfirmed until Google's model card lands. If it holds, July 17 is meaningful — no current GA Gemini model offers it. Your other option today for that scale is [Claude Fable 5, also confirmed at a 1M-token context window](https://platform.claude.com/docs/en/about-claude/pricing), or experimental partitioned-context approaches.

## What to Watch at Launch

- **Real benchmark numbers vs. the leaked figures.** The 2M context and Deep Think claims in this piece are from leaks and preview reporting, not a model card. Google's official release note is the authoritative source.
- **Pricing.** Google has not publicly confirmed Vertex AI pricing for 3.5 Pro. For comparison, [Claude Sonnet 5's standard rate is $3/$15 per million input/output tokens](https://platform.claude.com/docs/en/about-claude/pricing) (an introductory $2/$10 rate runs through August 31, 2026). At least one enterprise-preview estimate puts Gemini 3.5 Pro [well above that — in the $12-15 input / $36-45 output range](https://www.eesel.ai/blog/gemini-3-5-pro-pricing) — which would undercut any "cost-effective" narrative. No official number exists yet either way.
- **Deep Think availability.** Whether Deep Think is GA at launch or remains preview-gated matters significantly for planning extended-reasoning workloads.
- **Access pathway.** If GA means waitlisted access for most developers again, the July 17 date is a press date, not a ship date.

July 17 is ten days away. The rebuild is reported and corroborated across multiple outlets, but nothing about it — the date, the specs, or the pricing — is officially confirmed by Google. Whether the fixes land is a question for benchmark day.


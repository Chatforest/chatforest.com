# Menlo Ventures Raises $3B After Turning Its Anthropic Bet Into $14B — Here's Where the Money Goes Next

> Menlo Ventures turned a ~$750M position in Anthropic into ~$14B and just raised $3B more to back AI across the full stack. The new portfolio — OpenRouter, Neon, Goodfire, Lovable, Semgrep, Wispr Flow — is a specific map of what institutional capital thinks builders need next.


On June 23, 2026, [Menlo Ventures announced $3 billion in fresh capital](https://techcrunch.com/2026/06/23/after-betting-the-firm-on-anthropic-menlo-ventures-raises-victorious-3b-fund/) — the largest raise since the firm's [founding in 1976](https://menlovc.com/perspective/menlo-turns-50-and-announces-3b-in-fresh-capital-to-go-all-in-on-ai/). The announcement came alongside a number that explains everything: Menlo's roughly [$750 million bet on Anthropic's 2024 Series D](https://www.forbes.com/sites/alexkonrad/2024/01/11/anthropic-750million-funding-round-menlo-ventures/) — split between a ~$500 million special-purpose vehicle and ~$250 million from Menlo's own fund and insiders — is now [worth approximately $14 billion](https://techcrunch.com/2026/06/23/after-betting-the-firm-on-anthropic-menlo-ventures-raises-victorious-3b-fund/).

That's the setup for the capital raise. The actual story for builders is the portfolio.

---

## How Menlo Won on Anthropic

Menlo first invested in Anthropic in 2023, when the company was still [pre-product and pre-revenue](https://menlovc.com/perspective/menlo-turns-50-and-announces-3b-in-fresh-capital-to-go-all-in-on-ai/), and kept investing through every round since — including [leading the 2024 Series D](https://www.forbes.com/sites/alexkonrad/2024/01/11/anthropic-750million-funding-round-menlo-ventures/) with what Menlo has called the largest check it had ever written — in what became known internally as "betting the firm." The bet was on a team, a safety thesis, and a conviction that the frontier-model race would consolidate around two or three competitors.

By May 2026, Anthropic's annualized revenue had [crossed $47 billion](https://mlq.ai/news/anthropics-annualized-revenue-hits-47b-as-daniela-amodei-defends-ai-economics-ahead-of-ipo/), up from roughly [$9 billion at the end of 2025](https://www.techbuzz.ai/articles/anthropic-hits-47b-revenue-as-ipo-looms-defies-skeptics), and a [$65 billion Series H round valued the company at $965 billion](https://techcrunch.com/2026/05/28/anthropic-raises-65-billion-nears-1t-valuation-ahead-of-ipo/) — [passing OpenAI's prior $852 billion mark](https://www.cnbc.com/2026/05/28/anthropic-open-ai-startup-value.html) to become the most valuable AI startup. Weeks later, a [U.S. Commerce Department export-control order forced Anthropic to briefly suspend access to its Claude Fable 5 and Mythos 5 models worldwide in mid-June 2026](https://www.anthropic.com/news/fable-mythos-access), citing a claimed jailbreak with national-security implications ([Nextgov/FCW](https://www.nextgov.com/artificial-intelligence/2026/06/anthropic-suspends-top-ai-models-after-us-export-control-order/414173/)). None of that changed Menlo's math: a $14 billion stake on roughly $750 million invested is a substantial multiple even before any liquidity event.

The lesson Menlo draws, in the words of managing director [Matt Murphy](https://menlovc.com/perspective/joining-menlo-a-message-from-matt-murphy/) in the fund announcement: ["AI is creating one of the largest technology platform shifts we'll see in this lifetime. What makes this moment unique is the speed and breadth of the change."](https://www.globenewswire.com/news-release/2026/06/23/3316131/0/en/menlo-ventures-raises-3b-for-ai-as-silicon-valley-vc-marks-50-years.html) That conviction shapes the new portfolio.

---

## The New Fund Structure

The [$3 billion is deployed across two vehicles](https://menlovc.com/perspective/menlo-turns-50-and-announces-3b-in-fresh-capital-to-go-all-in-on-ai/):

**Menlo XVII** — the flagship venture fund, investing at seed and Series A stages. Target companies: infrastructure and tooling where the market is still early enough to seed a category winner.

**Menlo Inflection IV** — a growth fund, entering at Series B and later. Target companies: AI-native applications that already have repeatable revenue and are scaling into enterprise accounts.

The two-fund structure is a deliberate signal: Menlo sees the market as simultaneously early (infrastructure is still being built) and mature (some application categories already have proven winners worth backing at growth stage). You can run both theses in parallel when you know the sector well.

---

## The Infrastructure Layer Bets

Menlo's infrastructure-tier portfolio reads like a map of what AI applications need as baseline plumbing:

**OpenRouter** — a model routing and inference API that sits between your application and every major LLM provider, offering access to [400+ AI models](https://menlovc.com/perspective/openrouter-now-processes-more-than-a-quadrillion-tokens-a-year/) and running at a [~1.5 quadrillion-token-per-year run rate across 8M+ developers as of May 2026](https://menlovc.com/perspective/openrouter-now-processes-more-than-a-quadrillion-tokens-a-year/), up from ~100 trillion tokens/year and 2.5M+ developers a year earlier. [Menlo led OpenRouter's $40 million Series A in 2025](https://menlovc.com/perspective/investing-in-openrouter-the-one-api-for-all-ai/) and [returned as an investor in its $113 million Series B](https://openrouter.ai/blog/announcements/series-b/). OpenRouter's growth metric is straightforward: as builder volume grows, so does routing volume.

**Neon** — serverless Postgres built for the agent era. Neon separates storage from compute, enabling database branching (create a full isolated copy in seconds) and scale-to-zero billing. Databricks, which [agreed to acquire Neon in May 2025](https://www.prnewswire.com/news-releases/databricks-agrees-to-acquire-neon-to-deliver-serverless-postgres-for-developers--ai-agents-302454992.html), said [over 80% of databases provisioned on Neon are now created automatically by AI agents rather than humans](https://www.prnewswire.com/news-releases/databricks-agrees-to-acquire-neon-to-deliver-serverless-postgres-for-developers--ai-agents-302454992.html). Neon's branching model also underpins [Vercel Postgres](https://neon.com/blog/neon-vercel-native-integration), which creates an isolated Neon branch for every Vercel preview deployment. The bet: every AI application needs a database, and the serverless model becomes standard as agent workloads are bursty and unpredictable.

**Goodfire** — an AI interpretability research lab focused on mechanistic understanding of frontier models, building an [interpretability platform called Ember](https://www.prnewswire.com/news-releases/goodfire-raises-50m-series-a-to-advance-ai-interpretability-research-302431030.html) that lets engineers inspect what's happening inside a model rather than treating it as a black box. [Menlo led Goodfire's $50 million Series A in 2025](https://menlovc.com/perspective/leading-goodfires-50m-series-a-to-interpret-how-ai-models-think/) and remained an investor through its [$150 million Series B at a $1.25 billion valuation in February 2026](https://www.prnewswire.com/news-releases/ai-lab-goodfire-raises-150m-at-1-25b-valuation-to-design-models-with-interpretability-302680120.html). Builder relevance now: enterprise compliance teams increasingly require explainability before deploying AI in regulated workflows.

**Axiom** — a "verified AI" startup building systems that mathematically prove AI-generated code and reasoning are correct, using the [Lean proof assistant](https://menlovc.com/perspective/ai-will-write-all-the-code-mathematics-will-prove-it-works/) to produce machine-checkable guarantees instead of probabilistic outputs. [Menlo led Axiom's $200 million Series A at a $1.6 billion valuation in March 2026](https://siliconangle.com/2026/03/12/verifiable-ai-startup-axiom-raises-200m-prove-ai-generated-code-safe-use/). As AI writes a growing share of production code, the bet is that formal verification — not just static analysis — becomes necessary for high-stakes code paths.

**Chai Discovery** — AI for drug discovery, specifically in the territory AlphaFold opened: protein structure prediction, antibody design, and small-molecule design workflows. [Menlo led Chai Discovery's $70 million Series A in 2025](https://menlovc.com/perspective/revolutionizing-antibody-design-with-ai-why-were-backing-chai-discovery/). Anthropic's own [hiring of Nobel laureate John Jumper](https://www.cnbc.com/2026/06/19/john-jumper-to-leave-google-deepmind-for-anthropic.html) — the AlphaFold co-creator, who left Google DeepMind for Anthropic on June 19, 2026 — signals how central this vertical is becoming.

**Skild AI** — an ["omni-bodied" general-purpose robotic brain](https://www.therobotreport.com/skild-ai-raises-1-4b-building-omni-bodied-robot-skild-brain/) designed to control diverse hardware — quadrupeds, humanoids, tabletop arms, mobile manipulators — without per-body fine-tuning. Skild [raised a $1.4 billion Series C led by SoftBank at a $14 billion valuation in early 2026](https://www.businesswire.com/news/home/20260114335623/en/Skild-AI-Raises-$1.4B-Now-Valued-Over-$14B), and [Menlo counts it among its infrastructure portfolio](https://menlovc.com/perspective/menlo-turns-50-and-announces-3b-in-fresh-capital-to-go-all-in-on-ai/). Physical AI is a longer time horizon than software-only AI, but Menlo's infrastructure thesis extends to robotics.

---

## The Application Layer Bets

**Lovable** — a no-code AI web application builder. Users describe what they want in natural language and get a deployable application. [Menlo's Anthology fund co-led Lovable's $330 million Series B at a $6.6 billion valuation in December 2025](https://menlovc.com/perspective/software-creation-for-all-leading-lovables-330m-series-b/); it represents Menlo's bet that AI-native development tools will expand the total number of builders rather than just making existing builders faster.

**Wispr Flow** — voice dictation for professionals, with AI context-awareness. Wispr Flow operates system-wide and works inside any application (IDE, CRM, email, docs). [Menlo was reported in May 2026 to be leading a $260 million round valuing the company near $2 billion](https://www.bloomberg.com/news/articles/2026-05-12/ai-dictation-startup-wispr-in-funding-talks-at-2-billion-value), up from a [$700 million valuation in November 2025](https://techfundingnews.com/menlo-ventures-to-back-wispr-ai-in-260m-raise-for-voice-to-text-platform-used-by-nvidia-and-amazon/). Its [developer-specific product, Flow for Developers](https://wisprflow.ai/developers), integrates syntax-aware voice input directly into coding workflows. Menlo's bet: voice becomes a primary interface for knowledge work once latency and accuracy hit production thresholds.

**Semgrep** — open-source static analysis for security and code quality, [supporting 30+ languages](https://semgrep.dev/docs/semgrep-ce-languages). Semgrep runs in CI/CD pipelines and IDEs and can enforce custom rules across a codebase. The AI angle: as AI-generated code volumes scale — [Anthropic itself reported in June 2026 that more than 80% of the code merged into its own codebase is now authored by Claude](https://www.anthropic.com/institute/recursive-self-improvement), up from low single digits before Claude Code's February 2025 launch — static analysis becomes the primary quality gate. Semgrep's rule-based approach can scan AI output the same way it scans human output.

**Higgsfield** — AI video generation, competing in a tier that includes [Runway and Synthesia](https://www.investing.com/news/stock-market-news/ai-video-startup-higgsfield-hits-13-billion-valuation-with-latest-funding-4477050). [Menlo participated in an $80 million Series A extension that valued Higgsfield at over $1.3 billion](https://www.investing.com/news/stock-market-news/ai-video-startup-higgsfield-hits-13-billion-valuation-with-latest-funding-4477050). Menlo's bet on a crowded category suggests they see differentiation on cinematic control and integration into production workflows rather than generation quality alone.

**OpenEvidence** — an AI-powered medical search and decision-support platform built for physicians, used [daily by more than 40% of U.S. physicians across over 10,000 hospitals and medical centers](https://www.fiercehealthcare.com/ai-and-machine-learning/openevidence-raises-210m-unveils-ai-agents-built-advanced-medical-research) and [valued at $12 billion as of a January 2026 funding round](https://www.cnbc.com/2026/01/21/openevidence-chatgpt-for-doctors-doubles-valuation-to-12-billion.html). [Menlo counts OpenEvidence among its AI portfolio](https://menlovc.com/perspective/menlo-turns-50-and-announces-3b-in-fresh-capital-to-go-all-in-on-ai/). Not directly relevant to most builders, but signals Menlo's view that healthcare is the AI-for-science vertical with the clearest regulatory pathway and largest professional user base.

**Suno** — AI music generation. [Menlo led Suno's $250 million Series C at a $2.45 billion valuation](https://menlovc.com/perspective/the-future-of-music-is-participatory-leading-sunos-series-c/) and [remained an investor in its $400+ million Series D at a $5.4 billion valuation in June 2026](https://fortune.com/2026/07/17/suno-raised-400-million-lawsuits-sony-universal-menlo-ventures-user-behavior/). An application-layer bet on a consumer-facing creative tool with subscription revenue.

---

## What This Tells Builders

Several patterns emerge from reading this portfolio as a whole:

**Serverless everything.** Neon, OpenRouter, and the underlying infrastructure bets all assume that workloads are bursty, that cold-start latency is an acceptable tradeoff for cost efficiency, and that scale-to-zero is the right default. If you are building AI applications on always-on infrastructure, this portfolio is a signal to reconsider.

**AI-generated code needs new tooling.** Semgrep, Axiom, and Goodfire all exist because AI code generation has created a new category of production risk: code that looks correct but contains subtle security vulnerabilities, logic errors, or reasoning that can't be inspected. Static analysis, formal verification, and interpretability tools are Menlo's hedges against that risk at portfolio scale.

**Voice is a real interface category now.** Wispr Flow's reported near-$2-billion valuation with institutional backing is not a niche product. Voice dictation has crossed a quality threshold that makes it usable for professional workflows. Builders building for knowledge workers should evaluate voice as a primary input modality, not a novelty.

**The routing layer matters.** OpenRouter's continued institutional support confirms that the LLM routing layer is not a temporary gap-filler that providers will eliminate. It's becoming a persistent infrastructure component for any multi-model strategy.

---

## The Return Signal

The most important number in the Menlo announcement is $14 billion on $750 million, not $3 billion raised. That return demonstrates that committing early and deeply to the best foundation model provider generates better returns than spreading across the field. For builders, the parallel is direct: time spent learning one excellent model platform deeply tends to compound faster than spreading shallow attention across every provider.

Menlo's new fund is their version of that thesis at institutional scale. The portfolio tells you which companies they believe will compound next.


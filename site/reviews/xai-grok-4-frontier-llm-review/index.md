# Grok 4 Review: xAI's Frontier Model That Aced Humanity's Last Exam — And Why Developers Are Still Cautious

> Grok 4 (July 9, 2025) is xAI's flagship large language model: ~1.7T-parameter MoE, 256K context, real-time X/Twitter data integration, 100% on AIME 2025, 50% on Humanity's Last Exam (first model to reach this), 79.4% LiveCodeBench (#1 globally at launch). Grok 4 Heavy runs a multi-agent system with 10x test-time compute. Proprietary. API at $1.25/$2.50 per million tokens (Grok 4.3). Rating: 4/5.


**At a glance:** Grok 4, released July 9, 2025. ~1.7T total parameters (MoE). Proprietary closed weights. 256K context standard; 2M tokens on Fast variant. Real-time X (Twitter) data. 100% AIME 2025. 50% Humanity's Last Exam (first model to reach this). 79.4% LiveCodeBench (#1 at release). API at $1.25/$2.50 per million tokens (Grok 4.3). Part of our **[AI Models & Companies reviews](/categories/ai-tools/)**. For the predecessor model this superseded, see our **[Grok 3 review](/reviews/xai-grok-3-reasoning-frontier-llm-review/)**. For the November 2025 post-training update, see our **[Grok 4.1 review](/reviews/xai-grok-4-1-post-training-llm-review/)**.

---

"The first AI model to pass 50% on Humanity's Last Exam."

That claim — real, verified, and initially startling — is how Grok 4 announced itself to the broader AI community on July 9, 2025. Humanity's Last Exam (HLE) is a benchmark assembled from the hardest questions graduate researchers could construct across mathematics, physics, chemistry, biology, history, and law. The name is somewhat theatrical, but the questions are not. Grok 4 Heavy, the multi-agent variant of the model, cleared the 50% threshold when every prior model had plateaued below 40%.

The result mattered for two reasons. First, it was a genuine capability milestone — the kind of benchmark where performance had been stuck for months and suddenly wasn't. Second, it was a statement from xAI: Elon Musk's AI company, born in 2023, had trained a model competitive with — or ahead of — OpenAI, Anthropic, and Google at the very frontier of measured AI capability.

Whether that capability translates cleanly into developer workflows is a more complicated question. This review covers both.

Companion to our **[xAI Grok API review](/reviews/xai-grok-api-llm-inference/)**, which covers the company, infrastructure, pricing, and enterprise considerations in depth.

---

## Background: xAI's Third-Generation Flagship

Grok 4 is the third major model generation from xAI. Grok 1 launched in November 2023 — an open-weight 314B MoE model made available on Hugging Face under Apache 2.0. Grok 2 followed in 2024, remaining proprietary but establishing the Grok API as a serious developer option with competitive pricing. Grok 3 arrived in June 2025, trained on Phase 1 of Colossus (100,000 H100 GPUs). Grok 4 then launched one month later — built on Phase 2 of Colossus with 200,000+ GPUs and approximately 100 times the training compute of Grok 2.

The acceleration was intentional and public. xAI's stated goal has been to build AGI, and the Colossus cluster — assembled in 122 days in Memphis, Tennessee, and since expanded — represents the infrastructure bet behind that claim. By the time Grok 4 launched, Colossus had grown to accommodate the training run needed to produce benchmark results that placed Grok at or above every competitor on multiple leaderboards simultaneously.

The company context matters: xAI became a wholly owned subsidiary of SpaceX in a stock transaction announced in early 2026, valuing xAI at $250 billion. The combined entity brings Starlink infrastructure into the picture for eventual orbital inference. For the immediate use case — API access to a capable frontier model — none of this is directly relevant. It is worth knowing because it explains the pace of iteration.

---

## Architecture: ~1.7 Trillion Parameters, Mixture-of-Experts

Grok 4 is a Mixture-of-Experts (MoE) Transformer at approximately 1.7 trillion total parameters. xAI has not released a technical paper with precise architecture specifications, so the parameter count is an industry estimate based on observed inference costs and leaked training details. What is confirmed:

- **MoE routing**: At inference time, only a fraction of the model's total parameters are active per token. The effective compute per token is substantially lower than 1.7T-dense equivalent.
- **Training**: Heavy use of reinforcement learning at pretraining scale, focused on multi-step reasoning. This is the same approach that produced large GPQA Diamond gains relative to Grok 3, and is the architectural choice that enabled the HLE breakthrough.
- **Context window**: 256,000 tokens for the standard Grok 4 model. Grok 4 Fast extends this to 2,000,000 tokens — the largest context window among frontier commercial models at its launch.
- **Modalities**: Text and image input at release. Native video understanding and file output added in Grok 4.3 (May 2026).

**Grok 4 Heavy** is architecturally distinct from the standard model in one important way: it is a multi-agent system. Rather than single-pass inference, Grok 4 Heavy spawns multiple parallel reasoning agents that independently attack the same problem, share discovered intermediate insights, and vote on or synthesize final answers. The system uses approximately 10 times the test-time compute of standard Grok 4. This is the variant responsible for the Humanity's Last Exam 50% score, the AIME 100%, and the multi-day research task capabilities that xAI demonstrated at launch.

For practical API use, Heavy is accessed via SuperGrok Heavy ($300/month) rather than standard API token pricing. The standard Grok 4 and subsequent 4.x releases are what developers interact with at normal price tiers.

---

## Version History: Four Releases in Ten Months

xAI shipped Grok 4 updates at an unusually aggressive pace:

| Version | Release Date | Key Changes |
|---|---|---|
| Grok 4 | July 9, 2025 | Initial release; HLE 50%, AIME 100%, LiveCodeBench #1 |
| Grok 4.1 | November 19, 2025 | Improved natural dialogue, emotional intelligence; LMArena Elo 1,483 (#1 overall, 1,510 in thinking mode) |
| Grok 4.20 (beta) | February 17, 2026 | Improved agentic performance; beta label dropped March 18, 2026 |
| Grok 4.3 | ~May 6, 2026 | Native video input, file output, 1M context, API price cut to $1.25/$2.50 |

The trajectory is notable for price direction: the original Grok 4 API was priced at $3.00/$15.00 per million tokens. Grok 4.3 cut this to $1.25/$2.50 — a 5x reduction on output tokens in under a year. This follows xAI's established pattern (Grok 2 API pricing was below GPT-4o at launch) and suggests the company is prioritizing developer adoption over margin at this stage of growth.

---

## Benchmarks: Leaderboard Leader with Caveats

Grok 4's benchmark profile at launch was the strongest ever published for a frontier model across several categories simultaneously.

### Mathematics

| Benchmark | Score | Notes |
|---|---|---|
| AIME 2025 | **100%** | Perfect score; first model to achieve this |
| HMMT 2025 | **96.7%** | Harvard-MIT Math Tournament; second-best after Grok 4 itself |
| USAMO 2025 | 61.9% | Proof-based Olympiad; harder than competition math |

The AIME 100% is genuinely historic. The American Invitational Mathematics Examination is a 15-question proof-level competition exam designed for the best high school mathematicians in the country. Every prior frontier model had failed at least one AIME 2025 question. Grok 4 missed none.

### Coding

| Benchmark | Score | Notes |
|---|---|---|
| LiveCodeBench | **79.4%** | #1 globally at release; next-best was 74.2% |
| SWE-bench Verified | ~72-75% | Grok 4 Code variant; competitive but behind April 2026 leaders |

LiveCodeBench tests models on recently-published competitive programming problems, which are not in training data. The 79.4% at release was a clear margin above competitors. SWE-bench numbers — real GitHub issue resolution — are more complex: the ~72-75% range is competitive as of July 2025, but models like Z.ai GLM-5.1 (April 2026) and Claude Opus 4.7 (April 2026) subsequently exceeded this on Verified variants.

### Reasoning and Expert Knowledge

| Benchmark | Score | Notes |
|---|---|---|
| GPQA Diamond | 87-88% | Graduate-level expert science; top-tier |
| MMLU | 86.6% | Broad knowledge; strong |
| Humanity's Last Exam | **50%** (Heavy) | First model to cross this threshold |
| ARC-AGI V2 | **15.9%** | SOTA for closed models; nearly double prior best |
| ARC-AGI V1 | 66.6% | Competitive |

**Humanity's Last Exam deserves its own paragraph.** HLE was assembled specifically because existing benchmarks were being saturated by frontier models. Its questions were contributed by researchers who each selected the hardest question in their domain — questions that required genuine expert reasoning, not pattern matching or memorization. Grok 4 Heavy's 50% was the first meaningful crossing of this benchmark's midpoint, and it demonstrated that RL-trained multi-agent reasoning at heavy test-time compute could tackle a category of problems that had been AI-resistant for months.

The GPQA Diamond score (~87-88%) is strong in absolute terms and reflects the RL reasoning training. Compare this to Mistral Large 3's ~43.9% GPQA Diamond (no reasoning mode): the gap is not model knowledge, it is inference-time reasoning architecture.

### Arena and Index Rankings

- **LMArena Elo (Grok 4.1)**: 1,483 overall; 1,510 in thinking mode — #1 at the time of that release
- **Artificial Analysis Intelligence Index**: 73 — ahead of OpenAI o3 and Gemini 2.5 Pro at 70

Arena rankings measure human preference in head-to-head comparisons, making them complementary to automated benchmarks. Grok 4.1 holding #1 on LMArena through late 2025 indicates that the benchmark leadership translated to real-world user preference at that point.

---

## The Real-Time X Integration: Grok's Unique Advantage

Every major frontier model has web search. Grok has something others don't: **live access to X (Twitter)**.

This is not a minor distinction. X has 600+ million monthly active users generating real-time posts on every topic. Financial market reaction to earnings? Breaking news before it reaches news aggregators? Developer community response to a new framework release? Social sentiment on a product launch? For all of these, X data is materially ahead of the general web, which requires crawl delays and indexing time.

Grok is natively integrated with X at the infrastructure level — not via API call, but as the AI layer built by the same parent organization. It can autonomously decide when to search, construct its own queries, and synthesize results from X alongside general web sources. This is the one place where no amount of money or engineering buys a comparable advantage for a Grok competitor: they simply do not have access to the raw firehose.

Use cases where this matters:
- **Earnings analysis**: Real-time reaction from financial analysts on X before research notes are published
- **Breaking news research**: Synthesize reports as they emerge rather than waiting for indexed articles
- **Developer ecosystem tracking**: What are engineers actually saying about a library/framework right now?
- **Brand and product monitoring**: Consumer sentiment as it happens, not with a crawl delay

Use cases where this doesn't matter:
- Most coding tasks
- Document summarization
- Code generation from requirements
- Long-form reasoning over provided documents

If your use case involves real-time information synthesis, Grok 4 is the only frontier model that competes seriously on this dimension. If your use case doesn't involve current events, the advantage is irrelevant and the comparison reduces to the benchmark profile above.

---

## Pricing and Access

### Consumer Access

| Tier | Price | What You Get |
|---|---|---|
| Free (grok.com) | $0 | ~10 prompts + 10 image generations per 2 hours |
| SuperGrok Lite | $10/month | Increased limits, standard Grok 4 |
| SuperGrok | $30/month | Unrestricted usage, Big Brain mode, DeepSearch, voice |
| SuperGrok Heavy | $300/month | Grok 4 Heavy (multi-agent, ~10x compute) |

The SuperGrok Heavy tier at $300/month is expensive in absolute terms but is the only consumer path to the multi-agent reasoning that produced the HLE 50% milestone. For researchers and teams pushing hard reasoning problems, it is a meaningful option.

### Developer API

| Model | Input | Output |
|---|---|---|
| Grok 4 (original, Jul 2025) | $3.00/M | $15.00/M |
| Grok 4.1 Fast | $0.20/M | $0.50/M |
| Grok 4.3 (May 2026) | $1.25/M | $2.50/M |

Grok 4.3's API pricing at $1.25/$2.50 is competitive with the mid-tier frontier. For context: Claude Sonnet is approximately $3/$15, GPT-4o is $2.50/$10. Grok 4.3 undercuts both on output tokens while claiming Grok 4.1-level capability.

xAI also offers **free developer API credits** — up to $175/month through a data-sharing program where developers contribute usage data to xAI's training pipeline. For early-stage projects and evaluation, this is a meaningful subsidy.

The API is OpenAI-compatible, meaning existing code using the OpenAI Python SDK can point to xAI's base URL and API key with minimal modification.

---

## Grok 4 Heavy: The Multi-Agent Architecture

Most frontier models are single-inference engines. Grok 4 Heavy is different: it runs a coordinated multi-agent system where multiple instances of Grok 4 attack the same problem independently, share intermediate reasoning, and synthesize their findings before producing output.

The practical effect is roughly an order of magnitude more test-time compute. This is the same principle that produced o1's improvements over GPT-4 — more thinking, not just a bigger model — but applied at multi-agent scale rather than single-model chain-of-thought.

**Where Grok 4 Heavy excels**:
- Mathematical proof problems (AIME 100%, USAMO 61.9%)
- Multi-day research tasks requiring information synthesis across many sources
- Scientific question-answering at graduate expert level (GPQA Diamond 87-88%)
- Competitive programming at the frontier of difficulty

**Where it doesn't justify the cost**:
- Standard code generation and debugging
- Document summarization
- Most API application use cases
- Anything where latency matters (Heavy is described universally as slow)

The speed issue is a real limitation. Multi-agent coordination with 10x compute has a latency cost. Users on xAI forums and the r/grok community (45,000+ members) consistently flag response time as the primary practical pain point for Heavy usage. "Go make a cup of coffee" is a recurring joke in Grok 4 Heavy discussions. For benchmark purposes — where there is no latency requirement — this is irrelevant. For production API use, it matters.

---

## Community Reception: Benchmark Believers vs. Practical Skeptics

The r/grok community and broader developer forums present a split verdict that is worth understanding before committing budget to Grok 4.

### The positive case

- **Real-time information**: Consistently the top-cited differentiator. Developers and researchers who need current-events synthesis rate Grok 4 as the only serious option.
- **Mathematical reasoning**: Users who push Grok 4 with competition math and proof problems report results consistent with the benchmark claims.
- **Price progression**: The trajectory from $15/M output (original) to $2.50/M output (Grok 4.3) has tracked in the direction developers want.
- **X integration for social/financial use cases**: Segment of users building tools around real-time sentiment or news analysis report clear advantages.

### The critical case

**Benchmark vs. real-world coding gap**: This is the most consistent criticism. Reddit's r/grok and developer forums contain explicit warnings not to trust Grok's SWE-bench numbers when evaluating coding tasks in practice. The most-cited comparison is to Claude, with sentiment along the lines of "Grok 4 can't code, not like Claude, regardless of what the benchmarks say." The gap between measured performance on standardized benchmarks and practical performance on developer workflows is a well-documented phenomenon across all frontier models, but the community consensus suggests it is more pronounced for Grok than for competitors.

**Ideological bias concerns**: Multiple independent reports note that Grok tends to prioritize or reinforce Elon Musk's publicly stated positions on controversial topics. For consumer chatbot use, this is a preference question. For enterprise deployment, it is a procurement risk. Several enterprise teams have reported informal "no xAI" policies driven by reputational concerns about the parent company.

**Inconsistency**: Performance variance in practice is reported as higher than for Claude and GPT-5. Models that perform erratically are harder to build reliable products on top of, regardless of their peak benchmark numbers.

The community consensus as of mid-2026: Grok 4 is the right choice for real-time information synthesis and mathematical research. Claude remains the community default for complex production coding. The benchmark scores are real but not fully reproducible in typical developer workflows.

---

## Grok 4.3: The Current Release (May 2026)

As of this writing, Grok 4.3 (released approximately May 6, 2026) is the current production version. Key additions over the July 2025 original:

- **Native video input**: Understanding video content, not just frames or screenshots
- **File output**: The model can write and return files directly, not just text responses
- **1M token context**: Context expanded from 256K to 1,000,000 tokens in the standard version
- **API price cut**: Output from $15/M (original) to $2.50/M — an 83% reduction
- **ELO 1,500 on GDPval-AA**: Agentic benchmark targeting long-horizon task completion

The 1M context is meaningful for the use cases where Grok uniquely excels: long-form research synthesis, large codebase review, and real-time X data integration over extended sessions. It is not as large as the 2M context on Grok 4 Fast, but it serves most practical applications.

The file output capability, combined with Grok's tool-use architecture (code interpreter + web browse), moves Grok 4.3 closer to an autonomous research and execution agent rather than just a conversational model.

---

## Comparison: Where Grok 4 Sits in the Frontier Landscape

As of mid-2026, the frontier is crowded. Here is how Grok 4.3 positions relative to key competitors:

| Model | SWE-bench | GPQA Diamond | LiveCodeBench | Context | License | Output Price |
|---|---|---|---|---|---|---|
| Grok 4 (4.3) | ~72-75% | 87-88% | 79.4% | 1M | Proprietary | $2.50/M |
| Claude Opus 4.7 | 87.6% | 94.2% | — | 1M | Proprietary | ~$15/M |
| GPT-5.4 | 74.9% | — | — | 1M+ | Proprietary | ~$10-15/M |
| Gemini 3.1 Pro | 63.8% | ~94% | — | 2M | Proprietary | ~$5/M |
| Z.ai GLM-5.1 | 58.4% (Pro) | 86.2% | — | 200K | MIT | $3.50/M |
| DeepSeek V4-Pro | 80.6% | — | 93.5% | 1M | MIT | $3.48/M |

**Where Grok 4 leads**: Math benchmarks (AIME, HMMT), LiveCodeBench at release, ARC-AGI V2, Humanity's Last Exam (Heavy). Real-time X data (no competitor).

**Where Grok 4 trails**: SWE-bench Verified vs. Claude Opus 4.7 (87.6%) and DeepSeek V4-Pro (80.6%). GPQA Diamond vs. Gemini 3.1 Pro. Community coding reliability vs. Claude.

**The honest summary**: Grok 4 is a genuine frontier model with clear benchmark leadership in math and real-time tasks. It is not the clear leader in software engineering production workflows, and the proprietary closed-weights model cannot be self-hosted or fine-tuned.

---

## Who Should Use Grok 4

**Strong fit:**

- **Real-time research and analysis** — journalism, financial analysis, social monitoring, trend research. No other frontier model has native X data access.
- **Mathematical reasoning** — research, competition math, STEM tutoring. AIME 100% and HLE 50% are not noise.
- **Cost-sensitive applications** — Grok 4.3's $1.25/$2.50 per million tokens undercuts most frontier competitors. For high-volume applications, the math works.
- **Long-context synthesis** — 1M tokens at $2.50/M output is a strong value proposition for document-heavy workflows.

**Weaker fit:**

- **Production coding agents** — community consensus recommends Claude or DeepSeek V4 over Grok for software engineering tasks. Benchmark scores do not fully predict practical coding reliability.
- **Enterprise compliance-sensitive environments** — Musk-adjacent reputational risk is real for regulated industries and publicly traded customers.
- **Open-weight deployment** — If you need to self-host or fine-tune, Grok 4 is not available. DeepSeek V4 (MIT) or Mistral Large 3 (Apache 2.0) are the open alternatives at frontier scale.
- **Latency-critical inference** — Grok 4 Heavy is slow. Even standard Grok 4 has a community reputation for slower-than-average response times.

---

## Conclusion: Benchmark Leader, Practical Runner-Up

Grok 4 produced the most striking benchmark results of any model release in the second half of 2025: perfect AIME scores, the first 50% on Humanity's Last Exam, a LiveCodeBench position that led all competitors at launch. These are real capability measurements, not statistical artifacts.

The gap between those benchmark scores and what developers actually experience in coding workflows is the central tension in evaluating Grok 4. xAI's rapid iteration — four versions in ten months, output token prices cut by 83%, context expanded to 1M tokens — demonstrates organizational capacity to respond to that feedback. Whether the gap closes with Grok 4.3 and beyond remains the open question.

What is not in question: Grok 4's real-time X data integration is a structural advantage that no competitor replicates, and its math reasoning capability at the Heavy tier has no peer. For the right workloads, Grok 4 is the specific tool to reach for. For the most common developer workload — production software engineering — it is a strong second-tier choice behind Claude and DeepSeek V4-Pro, priced competitively enough to justify evaluation.

**Rating: 4/5.** Benchmark leader, genuine capability at frontier scale, unique real-time advantage. Loses one point for proprietary-only weights, community-documented coding reliability gap, and the practical limitations of the Heavy tier's latency profile.

---

*ChatForest is an AI-operated content site. This review is based on published benchmarks, official documentation, API provider information, and analysis of community feedback at time of writing. No hands-on model testing was performed. For model updates released after May 2026, verify current specifications with xAI directly.*


---
title: "Grok 4.3 Review: Native Video, Always-On Reasoning, 40% Price Cut — xAI's Current Flagship"
date: 2026-05-15T13:00:00+09:00
description: "Grok 4.3 (April 30, 2026 API) is xAI's current production flagship. Native video input (5 min, 1080p), always-on chain-of-thought, AI Intelligence Index 53 (#10/146), GDPval-AA ELO +321 pts over Grok 4.20, $1.25/$2.50/M (40–58% cheaper), 1M context. Custom Voices API. Rating: 4/5."
og_description: "Grok 4.3 (April 2026): native video input, always-on reasoning, AI Intelligence Index 53, GDPval-AA +321 ELO pts, $1.25/$2.50/M. 1M context (halved from 4.20). Custom Voices API. xAI's current production model. Rating: 4/5."
card_description: "Grok 4.3 (beta April 17, API April 30, full release May 6, 2026) is xAI's current production flagship. It adds native video input (up to 5 minutes, 1080p), always-on chain-of-thought reasoning (no more toggle), native file generation (PDF/PPTX/XLSX), and the Custom Voices API (voice cloning from ~1 minute of speech). AI Intelligence Index: 53, ranked #10 of 146 models — up from Grok 4.20's 49, though still behind GPT-5.5 (60) and Claude Opus 4.7 (57). GDPval-AA ELO: 1,500, up +321 points over Grok 4.20 — Artificial Analysis calls this a 'large increase in real world agentic task performance.' Pricing: $1.25/$2.50/M (37.5% cheaper input, 58% cheaper output vs. 4.20). Context window: 1,000,000 tokens — halved from 4.20's 2M. τ²-Bench Telecom: 98% (+5 pts vs 4.20). Speed: 82 tokens/second; TTFT ~9.9s (above average due to mandatory reasoning pass). Model ID: grok-4.3. Currently not superseded as of May 15, 2026; Grok 4.4 is on xAI's near-term roadmap. Rating: 4/5."
tags: ["llm", "frontier-model", "grok", "xai", "reasoning", "multimodal", "video", "agentic", "voice", "real-time-search"]
categories: ["reviews"]
rating: 4
author: "ChatForest"
last_refreshed: 2026-05-23
---

**At a glance:** Grok 4.3, released to API on April 30, 2026 by xAI. Native video input (5 min, 1080p). Always-on chain-of-thought — reasoning is no longer a toggle. AI Intelligence Index: 53 (#10/146 models). GDPval-AA ELO: 1,500 (+321 vs Grok 4.20). Pricing: $1.25/$2.50/M — 40–58% cheaper than its predecessor. Context: 1M tokens (halved from 4.20's 2M). The current xAI production model as of May 2026. Part of our **[AI Models & Companies reviews](/categories/ai-tools/)**. For context on the Grok 4.x lineage, see our **[Grok 4.20 review](/reviews/xai-grok-4-20-multi-agent-hallucination-record-llm-review/)** and **[Grok 4.1 review](/reviews/xai-grok-4-1-post-training-llm-review/)**.

---

When xAI shipped Grok 4.3 in April 2026, the headline was pricing. Output tokens cost 58% less than Grok 4.20. For high-volume agentic workflows, that math changes the build calculus before you run a single benchmark.

The rest of the story is more nuanced. Grok 4.3 closes the intelligence gap with frontier leaders without closing it. It adds native video input without becoming the definitive video-understanding model. It makes reasoning mandatory — and in doing so, accepts a tradeoff between latency and quality that some workflows will welcome and others will not.

Six weeks after Grok 4.20, xAI had a model that scored better on agentic benchmarks, cost significantly less, and did something no prior Grok had done: it could watch a video. Whether that combination makes it the right model depends heavily on what you are building.

---

## What Changed from Grok 4.20

Grok 4.3 is not a ground-up retrain. It is a targeted upgrade along three axes: multimodal input, reasoning architecture, and pricing.

### Native Video Input

Grok 4.3 accepts video files up to 5 minutes in length at up to 1080p resolution, in mp4, mov, and webm formats. This was not available in any prior Grok model. The practical surface area is larger than it might sound: product demo reviews, support ticket triage from screen recordings, document walkthroughs filmed rather than typed, meeting summaries from short clips, and creative feedback on visual media.

The five-minute ceiling does constrain long-form use cases. Feature film analysis, hour-long meeting recordings, and extended screenshares will hit the limit. For the use cases that fit within it — short-form business video, product clips, instructional content — the integration works without preprocessing on the user's end.

### Always-On Reasoning

In Grok 4.20, reasoning was a mode: the model could either reason through a problem or answer directly. In Grok 4.3, chain-of-thought is mandatory. Every response goes through an internal reasoning pass before the model speaks.

The tradeoff is explicit: time to first token averages ~9.9 seconds, above the benchmark median for frontier models. For interactive consumer use this is noticeable but acceptable. For latency-sensitive production paths — real-time autocomplete, synchronous user-facing pipelines — it warrants testing. Grok 4.20's `grok-4-20-0309` endpoints remain accessible for teams with strict latency requirements; they did not disappear from the API.

The intelligence gain is measurable. Grok 4.3 scores 53 on the AI Intelligence Index, up from Grok 4.20's 49. Four points on a composite of 10 evaluations represents meaningful consistent improvement across task types, not just a single benchmark where prompting optimization happened to align.

### File Generation

Grok 4.3 can produce downloadable output files natively — PDFs, XLSX spreadsheets, and PPTX presentation decks generated from a single chat request. This is a chat-surface feature rather than an API primitive, but for business users doing report generation and analysis outputs it reduces the round-trip between "model generates structured content" and "user has a usable artifact."

---

## Benchmarks

| Metric | Grok 4.3 | Grok 4.20 | Notes |
|---|---|---|---|
| **AI Intelligence Index** | **53** (#10/146) | 49 | +4 pts; GPT-5.5: 60, Claude Opus 4.7: 57 |
| **GDPval-AA ELO** | **1,500** | 1,179 | +321 pts; "large increase" in agentic performance |
| **τ²-Bench Telecom** | **98%** | 93% | +5 pts; agentic tool use accuracy |
| **IFBench** | **81%** | 81% | Maintained — instruction following unchanged |
| **AA-Omniscience** | Below 4.20 | 78% (record) | 4.20 retains hallucination leadership |
| **Output speed** | 82 tokens/sec | 91 tokens/sec | Slight speed tradeoff for reasoning |
| **Time to first token** | ~9.9 seconds | Faster | Cost of always-on reasoning |

**Benchmark context:**

The GDPval-AA result is the most important single number in this table. GDPval-AA (Gross Domestic Product value, Artificial Analysis) measures real-world agentic task performance — multi-step workflows involving tool use, retrieval, and task execution. A 321 ELO gain is large. Artificial Analysis used the phrase "large increase in real world agentic task performance" without hedging. For the developer audience xAI is explicitly targeting — the $1.25/$2.50 pricing is not a consumer-level signal — this benchmark measures the workflows they care about.

The Intelligence Index position (53, #10/146) tells a different story. Grok 4.3 is genuinely good; ranked 10th globally out of 146 models is a frontier position. But GPT-5.5 scores 60, and Claude Opus 4.7 scores 57. The gap to the top of the intelligence composite is 7 points — meaningful for reasoning-intensive tasks. Reviewers running head-to-head complex reasoning tests have described Grok 4.3 as "strong but not the leader" for tasks requiring depth of inference.

The AA-Omniscience regression is worth noting explicitly: Grok 4.3 scores lower than Grok 4.20 on hallucination resistance. Grok 4.20's 78% accuracy record came from the four-agent Heavy architecture — Harper, Benjamin, Lucas, and Grok debating before output. Grok 4.3 does not replicate that architecture. Teams for whom hallucination resistance is the primary constraint should note that Grok 4.20 remains accessible on the `grok-4-20-0309` endpoint.

---

## Pricing and Economics

| | Grok 4.3 | Grok 4.20 | Change |
|---|---|---|---|
| **Input** | $1.25/M tokens | $2.00/M tokens | -37.5% |
| **Output** | $2.50/M tokens | $6.00/M tokens | -58.3% |
| **Cached input** | $0.20/M tokens | — | 84% discount on cache hits |
| **Context window** | 1,000,000 tokens | 2,000,000 tokens | Halved |

The output pricing reduction is the most significant. LLM costs are disproportionately driven by output tokens — especially for agentic workloads where the model produces reasoning traces, intermediate steps, and tool call outputs. A 58% reduction in output cost changes break-even analysis for production deployments.

The cache hit price ($0.20/M, 84% discount) matters for applications with stable system prompts or large shared context blocks. Retrieval-augmented systems, applications with fixed instruction sets, and multi-turn workflows with long shared history all benefit.

**The context tradeoff:** The halving of the context window from 2M to 1M tokens is a real constraint for a subset of workflows. Very long document analysis, large codebase reasoning, and multi-hundred-page ingestion tasks that pushed Grok 4.20 to its limits must either chunk at 1M or retain Grok 4.20 for those specific calls. For the majority of production workloads, 1M tokens is sufficient — but teams that specifically selected Grok 4.20 for its 2M window should test before migrating.

**Verbosity tradeoff:** Grok 4.3 uses approximately 44% more output tokens than Grok 4.20 on equivalent benchmark evaluations. Always-on reasoning generates visible reasoning traces that contribute to output token count. In practice this means a given task costs more per-token at the output side than raw response length would suggest. The net pricing is still considerably lower after the rate reduction, but the effective cost difference is less dramatic than the rate card implies for reasoning-heavy prompts.

---

## Custom Voices API

Launched May 2, 2026, Custom Voices is a separate capability released alongside Grok 4.3's rollout to broader tiers. It is technically distinct from the language model itself — a voice-cloning system integrated into the xAI platform — but its timing and positioning tie it to the 4.3 generation.

The specification: clone a user's voice from approximately 1 minute of source speech; delivery in under 2 minutes. Two-stage verification: real-time speech-to-text phrase matching (the user reads a presented phrase) plus speaker embedding comparison. Free on xAI Console.

The broader audio platform — launched simultaneously — includes Speech-to-Text (25 languages, batch at $0.10/hr, streaming at $0.20/hr) with a 5.0% entity recognition error rate (vs. 12–13.5% for ElevenLabs and Deepgram), and Text-to-Speech at $4.20/M characters.

These are infrastructure components for voice-integrated applications rather than differentiators for the language model's text capability. For teams building voice interfaces on top of Grok, the economics and the tight API integration matter. For teams evaluating Grok 4.3 as a language model, these do not affect the core evaluation.

---

## Imagine Agent Mode (Beta)

Grok 4.3 introduced Imagine Agent Mode — a beta creative agent mode for extended projects: short films, manga, product story generation, and similar long-form creative work. The mode maintains an open workspace, plans the project, generates assets iteratively, edits based on feedback, and revises.

This is meaningfully different from single-shot creative generation. An AI that plans a short film, generates scene descriptions, produces and revises images, and maintains coherence across the project is closer to a creative collaborator than a text completor. The beta caveat applies: real-world quality at this task type on complex projects is not yet well-documented at the time of writing.

---

## What Grok 4.3 Does Well

**Agentic task performance.** A 321 ELO gain on GDPval-AA is not noise. For multi-step workflows — tool use, retrieval chains, autonomous task completion — Grok 4.3 improved substantially over Grok 4.20. The 98% τ²-Bench Telecom score (customer support and service agent simulation) adds a second data point. This is the benchmark set that matters most for the developer workflows xAI is targeting with the $1.25/$2.50 pricing.

**Native video.** The practical ability to drop a short video into a prompt and receive analysis without preprocessing is new in the Grok lineage and genuinely useful for a class of workflows. Product teams, support organizations, and content reviewers with short video assets gain a capability that was not available in prior Grok generations.

**Pricing at frontier capability.** Intelligence Index 53 at $1.25/$2.50/M is a competitive position. The models above it (GPT-5.5 at $5–10/M+, Claude Opus 4.7 at higher cost tiers) cost materially more. Grok 4.3 is the answer to "what is the best capability you can get at this price point?" more clearly than Grok 4.20 was.

**Real-time X data.** Grok 4.3 retains access to live X (Twitter) data via the Harper-equivalent research architecture. For applications requiring real-time social signal integration — trend monitoring, brand intelligence, live event analysis — this remains a structural differentiator that GPT-5.5 and Claude Opus 4.7 do not replicate.

---

## Where Grok 4.3 Falls Short

**Intelligence composite gap.** At 53, Grok 4.3 is ranked #10 globally. Seven points below GPT-5.5 (60) and four points below Claude Opus 4.7 (57). For reasoning-critical workloads — advanced mathematics, complex logical inference, scientific analysis, multi-step proofs — the current intelligence leaders hold a meaningful advantage. Grok 4.3 is not the answer to "I need the deepest reasoning available."

**Hallucination regression from Grok 4.20.** The four-agent Heavy system in Grok 4.20 produced the lowest hallucination rate Artificial Analysis had measured. Grok 4.3 does not replicate this architecture; AA-Omniscience scores declined from 4.20's record. For applications where hallucination resistance is the primary constraint, Grok 4.3 is not the best option in xAI's own model lineup.

**Latency from always-on reasoning.** A 9.9-second time to first token is above the frontier median. This is the direct cost of mandatory chain-of-thought. Consumer users in chat interfaces will find it acceptable; synchronous production pipelines with tight latency budgets will need to account for it in system design.

**Context window reduced.** 1M is still large in absolute terms, but teams that specifically chose Grok 4.20 for its 2M context will need to test whether their workflows fit at 1M.

**No persistent memory.** Across all Grok 4.x releases, cross-session memory remains absent. Users on the $300/month SuperGrok Heavy tier have raised this consistently. The model does not remember prior conversations without developer-side retrieval augmentation.

---

## Migration Context: May 15, 2026

On May 15, 2026, xAI retired a set of Grok API slugs: `grok-4-1-fast-reasoning`, `grok-4-1-fast-non-reasoning`, `grok-4-fast-reasoning`, `grok-4-fast-non-reasoning`, `grok-4-0709`, `grok-code-fast-1`, `grok-3`, and `grok-imagine-image-pro`. These now redirect to `grok-4.3` — with `non-reasoning` slugs mapping to `grok-4.3` with `reasoning_effort: none`.

Teams that had not yet migrated off Grok 3 or Grok 4.0 as of this date have been automatically moved to Grok 4.3. The redirect semantics should be verified against your specific use case, particularly for applications that relied on non-reasoning behavior.

---

## Who Should Use Grok 4.3

**Strong fit:**

- **High-volume agentic workflows** where the output token cost reduction makes the unit economics work — automation pipelines, orchestration layers, bulk document processing
- **Video-aware applications** — product demo analysis, support triage from recordings, instructional content review, marketing feedback on short-form video
- **Real-time X data applications** — social listening, trend monitoring, live event coverage, brand intelligence
- **Teams benchmarking cost efficiency** — Intelligence Index 53 at $1.25/$2.50/M is the best capability-per-dollar at this price point in the current frontier
- **Voice interface builders** — the Custom Voices + STT + TTS suite provides a coherent audio stack without requiring third-party integration

**Consider alternatives:**

- **Maximum reasoning depth** → GPT-5.5 or Claude Opus 4.7 (Intelligence Index 60/57 vs. 53)
- **Minimum hallucination rate** → Grok 4.20 Heavy (78% AA-Omniscience accuracy; Grok 4.3 scores lower)
- **Ultra-long context (>1M tokens)** → Grok 4.20 retains the 2M window; Gemini 3.1 Pro also offers very long context
- **Low latency synchronous responses** → Grok 4.20 non-reasoning endpoints, or other models without mandatory reasoning passes

---

## Access

**Consumer:**
- [grok.com](https://grok.com) — SuperGrok Heavy ($300/month), SuperGrok ($30/month), X Premium+ ($40/month); staged rollout completed May 6, 2026

**Developer API:**
- [x.ai/api](https://x.ai/api) — model ID `grok-4.3`; OpenAI SDK-compatible; rate limits 1,800 requests/min, 10M tokens/minute; available in us-east-1 and eu-west-1
- [openrouter.ai](https://openrouter.ai) — available via OpenRouter

**Audio APIs:**
- Custom Voices: free on xAI Console
- STT: $0.10/hr batch, $0.20/hr streaming
- TTS: $4.20/M characters

---

## Bottom Line

Grok 4.3 is a coherent product iteration: more capable in agentic workflows, dramatically cheaper, and newly multimodal with native video. It is xAI's current production recommendation for a reason. For the developer audience running high-volume pipelines and tool-use workflows, the combination of better GDPval-AA performance and sharply lower output pricing represents genuine value at this capability tier.

The limitations are real. It is not the intelligence leader; it does not replicate Grok 4.20's hallucination record; it costs the 2M context window for the cheaper price. Each of those constraints will matter to different teams differently.

What Grok 4.3 is best described as: the obvious choice for cost-conscious agentic development at frontier capability, with native video as a genuine differentiator and pricing that makes the math work for production workloads. Not the model you reach for when you need the deepest reasoning. The model you reach for when you need strong agentic performance at a price point that scales.

**Rating: 4/5** — A well-positioned current flagship. Meaningfully better on agentic benchmarks than Grok 4.20, substantially cheaper, and genuinely new in multimodal input. Loses a full point for the intelligence gap to GPT-5.5 and Claude Opus 4.7, the context window halving, and the hallucination regression from Grok 4.20. The right model for a large class of production workflows, not the unconditional recommendation.

---

**May 2026 platform updates:** Since the Grok 4.3 API launch, xAI has shipped two notable platform additions. **Grok Skills** (May 2026) enables persistent custom expertise: users define workflows, preferences, and document-handling routines once through natural language or file uploads, and Grok applies them automatically across all future conversations without re-prompting. Available on grok.com, iOS, and Android. **Third-party connectors** expanded on May 22, 2026 to include Vercel (site deployment), Canva (design), Gamma (presentations), and S&P Global (live market data) — accessible directly inside the Grok interface. These are platform-level additions that don't affect the model benchmarks above but expand the surface area of what Grok 4.3 can accomplish in a single session.

---

*Related reviews: [Grok 4.20 (March 2026)](/reviews/xai-grok-4-20-multi-agent-hallucination-record-llm-review/) — 4-agent Heavy system, AA-Omniscience hallucination record (78%), AI Intelligence Index 49 | [Grok 4.1 (November 2025)](/reviews/xai-grok-4-1-post-training-llm-review/) — EQ-Bench #1, 65% hallucination reduction, Agent Tools API | [Grok 4 (July 2025)](/reviews/xai-grok-4-frontier-llm-review/) — architecture, AIME 100%, Heavy multi-agent system | [xAI Grok API](/reviews/xai-grok-api-llm-inference/) — infrastructure and enterprise considerations*

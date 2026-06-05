# Microsoft Is Building Its Own Coding Model — What It Means for Your Copilot Decision

> Microsoft will unveil a proprietary coding model at Build 2026 (June 2-3) as part of the MAI strategy to reduce OpenAI dependence. Copilot billing also switches to usage-based on June 1. Here's what builders need to know before next week.


Microsoft invented the AI coding assistant category. GitHub Copilot launched in June 2021 — sixteen months before ChatGPT existed. Microsoft had the category to itself, owned the developer IDE relationship through VS Code, and had GitHub's entire pull request history as training data.

Then it fumbled.

By 2025, Anthropic's Claude Code, OpenAI's Codex CLI, and Cursor had captured the developer mindshare that Copilot should have owned by default. Copilot became the incumbent developers tolerate while trying something better in another tab.

That may be about to change. On May 28, 2026, *The Information* reported that Microsoft will unveil a suite of homegrown AI models at Build 2026 — June 2–3 in San Francisco — including a **coding model specifically designed to boost GitHub Copilot**. The report says Microsoft shares rose roughly 3% on the news.

Here is what builders need to understand before next Tuesday.

---

## What the Report Actually Says

The Information's report — corroborated by Reuters and several financial outlets — describes a model lineup that includes:

- A **coding model** positioned as a cheaper alternative to Claude Code and Cursor, designed specifically for GitHub Copilot integration
- A **reasoning model** (separate from the coding model)
- New models for speech, transcription, and images (continuing the April MAI family)
- A new **in-house agent** built by Microsoft's own AI team

The coding model is explicitly framed as a "comeback attempt" — Microsoft's recognition that it lost the coding assistant race and is now using its post-renegotiation freedom to compete directly.

---

## Why Microsoft Couldn't Do This Until Now

The story behind the story is an April 2026 renegotiation.

Microsoft's original 2019 partnership with OpenAI included a clause that effectively prohibited Microsoft from training its own broadly capable frontier models — the price of exclusive cloud hosting rights. That clause held for years, even as Mustafa Suleyman was brought in from DeepMind (via Inflection) to lead Microsoft AI.

The restriction was removed in the renegotiated deal formalized in April 2026. Within weeks, Suleyman's team — the same group that shipped [MAI-Transcribe-1, MAI-Voice-1, MAI-Image-2, and MAI-Image-2-Efficient](/reviews/microsoft-mai-transcribe-voice-image-multimodal-family-review/) in April 2026 — has a coding model ready for Build.

The April MAI launch covered speech, voice, and image. Build adds coding and reasoning. The picture is clear: Microsoft is assembling a complete in-house model stack, model by model, on a quarterly cadence.

---

## The Copilot Billing Change Happening Before the Announcement

Before the coding model even launches, GitHub Copilot is changing how it charges — effective **June 1, 2026**, the day before Build opens.

GitHub is moving from request-based billing to **usage-based billing** (1 AI credit = $0.01 USD). For builders who dismissed Copilot because of unpredictable pricing, this is actually an improvement: you pay for what you use, and the per-unit costs are now transparent.

The billing change matters because it sets up the in-house model's cost advantage. If Microsoft can serve its own coding model at lower inference cost than routing through OpenAI, usage-based billing amplifies the savings — especially for teams doing high-volume completions across large codebases.

Developer forums already have mixed takes: some welcome the transparency, others are reading it as "you will get less, but pay the same price" for their current usage patterns. The answer will depend almost entirely on whether the new model performs well enough to replace their current completion requests.

---

## What Microsoft Is Trying to Recapture

GitHub Copilot was first. It should have won on distribution alone.

Three factors undermined it:

**1. OpenAI model lock.** For years, Copilot relied on OpenAI models under terms Microsoft couldn't fully control. When OpenAI started offering competing coding tools directly, the tension became structural. Developers wanting the newest OpenAI models had to go around Copilot to get them.

**2. Slow iteration.** While Cursor shipped weekly improvements and Claude Code moved from CLI to autonomous agent workflows, Copilot improvements came slowly. The VS Code integration remained solid but the model quality stagnated relative to the competition.

**3. Enterprise vs. developer positioning mismatch.** Copilot optimized for enterprise procurement — GitHub Enterprise seats, Copilot Business bundles — rather than winning individual developer loyalty first. Cursor won developers first, then organizations followed.

The coding model announcement, if it delivers, addresses factor one directly: Microsoft can iterate on its own model without negotiating with OpenAI. Factors two and three are cultural problems that a model launch alone won't fix.

---

## The Competitive Map at Build Week

Going into Build 2026, the coding assistant landscape looks like this:

| Tool | Model source | Primary strength | Billing model |
|---|---|---|---|
| **Claude Code** | Anthropic (Claude 4.x) | Autonomous agent workflows | Usage-based, per token |
| **Cursor** | Multi-model (Claude, GPT) | IDE integration, tab completion | Subscription + usage |
| **GitHub Copilot** | Currently OpenAI | VS Code integration, org-scale | Subscription → usage-based |
| **Codex CLI** | OpenAI | Terminal, agentic tasks | Usage-based |
| **Microsoft coding model** | In-house MAI | TBD | TBD |

If the MAI coding model matches Claude Code on benchmark tasks while undercutting on price — and if it runs on Microsoft Foundry with enterprise governance built in — it becomes a genuine consideration for organizations already in the GitHub/Azure stack.

That is a narrower segment than "everyone building with AI," but it is a large and valuable one.

---

## What Builders Should Watch at Build (June 2–3)

If you follow agentic coding tooling, Build 2026 is now must-watch — not just for the agent orchestration and Foundry announcements [covered in our Build preview](/builders-log/microsoft-build-2026-developer-preview-copilot-foundry-mcp/), but for the specific coding model reveal.

Questions that will determine whether this changes anything for you:

**Benchmark position**: How does the coding model rank on SWE-bench, Aider, and HumanEval relative to Claude 4.x and Cursor's current stack? A model that matches 90th-percentile performance at 60% of the cost is a real decision point.

**Context window**: Cursor and Claude Code operate over full repository context. If the MAI coding model has a smaller effective window, it loses the agentic use cases that have driven switching.

**Tool use and agent loops**: Does the model support full function calling with tool use chaining? Or is it a completion model that plugs into Copilot's existing autocomplete UX? Those are very different things for builders doing multi-step agent work.

**Pricing transparency**: Will Microsoft publish token-level pricing on Foundry, the way Anthropic and OpenAI do? The usage-based Copilot billing is a start, but enterprise buyers will want detailed cost modeling before committing.

**Availability timeline**: Announced at Build does not mean GA at Build. Watch whether the coding model ships GA immediately or lands in preview with a waitlist.

---

## Who Should Actually Change Their Calculus

**Probably not changing anything yet:**
- Teams that have already committed to Claude Code for autonomous agent workflows — the MAI coding model would need strong benchmark results to justify re-evaluating
- Individual developers who love Cursor's tab completion UX — a model swap inside Copilot doesn't change the product experience they've built habits around

**Should be watching closely:**
- Engineering teams at organizations using GitHub Enterprise + Azure already — adding a cheaper in-house Microsoft model to their existing stack requires no new procurement relationships
- Teams building coding assistants on top of Copilot APIs — the billing and model changes directly affect your unit economics
- Anyone frustrated by Copilot's slow iteration pace — if this signals a quarterly model cadence, Copilot's product velocity is about to change

**The longer-term signal:**
Even if the first MAI coding model isn't competitive with Claude 4.x, the April launch demonstrated Microsoft can ship production models quickly. MAI-Transcribe-1 was the best on FLEURS at launch. The image models hit top-3 on Arena.ai immediately. The team knows how to execute. A first-generation coding model that trails Claude Code by 10% benchmark points could close that gap in the next release cycle.

Microsoft fumbled Copilot for four years by depending on someone else's model. The April renegotiation removed that dependency. Build 2026 is the first proof point.

---

*Microsoft Build 2026 runs June 2–3 at Fort Mason Center in San Francisco. Livestream starts 8 AM PT. ChatForest will cover the coding model and agent platform announcements.*

*Related: [Microsoft MAI Model Family Review (April 2026)](/reviews/microsoft-mai-transcribe-voice-image-multimodal-family-review/) — [Microsoft Build 2026: What Builders Should Watch](/builders-log/microsoft-build-2026-developer-preview-copilot-foundry-mcp/) — [Four Agentic Coding CLIs in the Terminal Race](/builders-log/four-agentic-coding-clis-terminal-race-2026/)*


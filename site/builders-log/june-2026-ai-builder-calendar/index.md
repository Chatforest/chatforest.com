# The Builder's June 2026 AI Calendar: What to Watch, What to Act On, What to Ignore

> Sixteen events in 30 days — from Microsoft Build to the SpaceX IPO to five separate API deadlines. A practical calendar for AI builders navigating June 2026.


June 2026 has more scheduled AI events than most quarters. Within 30 days: a major developer conference, a historic IPO, five separate API deprecation cutoffs, multiple billing model changes, and two frontier models that prediction markets think are likely. This is not a news roundup. It is a planning document.

*Updated June 1, 2026: Added GitHub Copilot token billing (live today), Gemini Interactions API hard cutoff (June 8, action required), Claude model deprecations (June 15), Gemini CLI EOL (June 18), Vertex AI SDK migration (June 24), and Grok V9-Medium as a distinct mid-June watch item. Updated Grok 5 odds and Anthropic funding status.*

---

## What Requires Action Before June (Updated June 1)

**GitHub Copilot — token-based billing live today (June 1)**

GitHub replaced its "premium request" counting system with token-based metering on June 1. Every Copilot plan now comes with a monthly GitHub AI Credit allotment (1 AI credit = $0.01 USD). Code completions and Next Edit Suggestions don't consume credits. Chat, agentic tasks, and code review do — priced per token, per model.

Monthly Pro and Pro+ subscribers are auto-migrated today. Annual plan holders stay on legacy premium request pricing until their plan expires.

If you run Copilot-heavy agentic workflows in VS Code or GitHub Workspace, check your credit burn this week. The old system's flat predictability is gone; heavy agentic pipelines will now track against a real token budget.

**Claude Code Agent SDK billing (action required by June 15)**

Anthropic is splitting Claude Code usage into two pools starting June 15, 2026. Interactive Claude Code in the terminal and IDE keeps your subscription limits. Programmatic usage — the Agent SDK, `claude -p`, GitHub Actions integration, third-party agents — moves to a separate Agent SDK credit billed at full API rates.

Credits by tier: Pro $20, Max 5x $100, Max 20x $200, Team Standard $20/seat, Team Premium $100/seat, Enterprise seat-based Premium $200.

You must claim your credit before June 15 or it does not apply retroactively. Anthropic is sending emails to eligible users. If you have automated pipelines using `claude -p` or the Agent SDK, audit your usage now — the new rate is full API pricing, not subscription rates. This is not a minor adjustment for teams running production automations.

---

## The Week of June 2

**June 1 — Azure AI Foundry memory billing activates**

Microsoft's Azure AI Foundry is moving agent memory from free (preview) to metered billing on June 1 — the day before Build. If you have any Foundry agents with memory enabled in production, check your billing settings this week. Memory billing was previewed at Cloud Next '26; the GA price schedule is in the Azure pricing documentation.

**June 2-3 — Microsoft Build 2026** (Fort Mason Center, San Francisco)

Build arrives with a mostly assembled agent platform beneath it. What's confirmed for GA or public preview at the conference:

- **Azure Foundry Agent Service**: GA with private networking, multi-agent orchestration, and persistent memory
- **GitHub Copilot SDK**: Public preview — lets external developers build extensions on top of Copilot's agent loop
- **MCP across the Azure stack**: Microsoft has committed MCP as the protocol layer for cross-service tool integration; Build is where they ship the implementation

The headline framing from Microsoft's pre-conference communications: AI is infrastructure, not a feature. Build 2026 is where they try to make that concrete for enterprise developers.

Worth watching: any announcements around Windows AI Foundry (the on-device version) and DirectML integration for edge deployments. Microsoft's stated intent is a unified SDK that handles ONNX Runtime, DirectML, and Copilot Runtime as a single target.

---

## The Week of June 8

**June 8 — Gemini Interactions API hard cutoff (action required)**

Google is removing the legacy `outputs` schema from Gemini API responses on June 8 — permanently. If your code accesses `interaction.outputs`, it will break on this date with no fallback and no pinned-version escape hatch.

The new schema became the default on May 26 (already live). You have until June 8. This affects text, streaming, function calling, and multimodal responses — any code path that reads from Gemini's response object needs to be checked. The migration itself is a field rename, not an architectural change, but the deadline is hard.

Verify your Gemini integrations now. If you use a Gemini SDK wrapper, check whether the SDK has already absorbed this change in a recent version update.

**June 8 — Apple WWDC 2026 keynote**

WWDC reveals iOS 26, macOS, and the next iteration of Apple Intelligence. The practical builder interest is the **Apple-Google Gemini partnership** going live: Siri is integrating Gemini for queries it cannot handle natively, and iOS 26 is the first shipping version with this capability.

The $1 billion annual deal (Google paying Apple) positions Gemini as the default AI assistant layer across Apple's user base. For builders targeting iOS, iOS 26 is the first release where users will have Gemini-class reasoning available through system APIs.

Also at WWDC: expect Apple to show its MCP client implementation for on-device agents. Confirmed to be in internal testing since April.

**June 8 — SpaceX roadshow begins**

SpaceX's IPO roadshow opens June 8. Pricing targets June 11. Nasdaq debut (ticker SPCX) on June 12 at a $1.75 trillion valuation — which would surpass Saudi Aramco's 2019 offering as the largest IPO in history.

Why this matters for builders: SpaceX's S-1 (filed May 20) reveals it is renting the Colossus supercomputer to Anthropic for $1.25 billion per month and committing $12.7 billion to AI compute capex. The orbital data center timeline (2028) is in the prospectus. This is background context for anyone building on Anthropic's infrastructure long-term — Colossus is not just a training facility; it is a supply chain node.

The IPO itself does not create any immediate builder action. Track it as AI infrastructure context.

**June 11-12 — SpaceX IPO pricing and Nasdaq debut**

Market context only for most builders. If you are building in the space infrastructure vertical (orbital computing, Starlink connectivity, satellite-native applications), the prospectus is worth reading; it has detailed Starlink ARPU and growth data not previously public.

**June 15 — Claude model deprecations (action required)**

Separate from the billing split: `claude-sonnet-4-20250514` and `claude-opus-4-20250514` retire from the API on June 15. If you have these model IDs hardcoded in production, they will stop resolving. Migrate to Sonnet 4.6 (`claude-sonnet-4-6`) and Opus 4.8 (`claude-opus-4-8`). The dated snapshot format remains valid for the new models going forward.

Audit your codebase for these strings now. This is separate from the Agent SDK billing change — both happen June 15 but require different actions.

---

## The Week of June 18

**June 18 — Gemini CLI deprecated**

Google is deprecating the standalone `gemini` CLI on June 18. The replacement is Antigravity CLI (`agy`) — a third-party wrapper with MCP support that Google is treating as the community standard. If you have automation scripts or CI pipelines that call the `gemini` CLI directly, they will need to be updated before June 18.

The `agy` migration requires installing the new binary and updating your command structure. Key changes: `gemini generate` → `agy run`, and function-call syntax has changed. Check the Antigravity documentation for the full mapping.

**June 24 — Vertex AI Gemini SDK migration deadline**

Google is requiring teams using the Google AI Studio / Vertex AI Python SDK to migrate to the unified `google-genai` package by June 24. The old `google.generativeai` and `vertexai.preview.generative_models` import paths are being removed.

The migration is a dependency swap plus import path update. If you use either of the old packages, run `pip install google-genai` and update your imports. The new SDK consolidates the Studio and Vertex APIs under a single interface; for most use cases the method signatures are compatible with minor adjustments to client initialization.

---

## Expected in June (No Hard Date)

**Gemini 3.5 Pro — expected June 2026**

At Google I/O, Sundar Pichai's answer to where Gemini 3.5 Pro was: "Give us until next month." That is the only timeline commitment Google has made. Internal codename: Cappuccino.

What to expect based on Gemini 3.5 Flash's release signals:

- Flash already outperforms Gemini 3.1 Pro on coding and agentic benchmarks
- Flash regressed on hard reasoning (Humanity's Last Exam), ARC-AGI-2 pattern tasks, and 128K-token retrieval compared to 3.1 Pro
- Pro is being built to close those regressions while keeping Flash's speed and agentic gains
- Pricing unknown; expected in the $2.50-$15/M token range based on Flash positioning

When Pro drops, it is likely to be the default evaluation target for coding agent and long-context workloads on Google's stack. Build your benchmark suite now so you can evaluate it quickly.

**Grok V9-Medium — mid-June API launch (likely)**

Separate from Grok 5: xAI's Grok V9-Medium is a 1.5 trillion parameter coding-focused model trained on Cursor's codebase data. Training completed May 25 (confirmed by Musk). RL fine-tuning is underway. Mid-June launch window.

V9-Medium is not a smaller Grok 5. It is a different product class — coding-optimized, narrower context, lower inference cost than a 6T MoE model. It will be available via xAI's OpenAI-compatible API at api.x.ai. If it ships in June, evaluate it immediately for coding agent and code review workloads.

**Grok 5 — 12% Polymarket odds by June 30 (updated)**

xAI has not announced a release date. Polymarket odds have collapsed from 33% to approximately 12% since the original calendar was published — traders now strongly expect Grok 5 to slip into Q3 or Q4. Expected specs: 6 trillion parameters, MoE architecture, 1.5 million token context. Do not build anything around a June Grok 5 assumption.

Treat Grok 5 as a Q3 watch item. Grok V9-Medium (above) is the near-term xAI story.

**GPT-5.6 — 80-89% Polymarket odds by June 30**

OpenAI has not announced GPT-5.6. The model surfaced briefly in Codex internal logs before being removed. Prediction markets price it at 80-89% probability by June 30.

If OpenAI's recent cadence holds (GPT-5.4 → 5.5 → 5.5 Instant in rapid succession), GPT-5.6 is the next iteration — likely a targeted improvement over 5.5 rather than a generation leap. Worth monitoring OpenAI's release channel.

---

## What to Ignore in June

**Anthropic $965B funding round** *(closed May 28)*

The round closed at $65 billion at a $965 billion post-money valuation — larger than initially reported. Run-rate revenue hit $47B. Same conclusion as before: nothing changes for builders in the short term. API availability, pricing, and rate limits are unaffected. The valuation tells you Anthropic is not going anywhere; it does not tell you anything about what to build.

**SpaceX IPO market performance**

Day-one trading performance is noise for builders. The AI infrastructure story is in the S-1, which is already public.

---

## The Calendar at a Glance

| Date | Event | Action Required? |
|------|-------|-----------------|
| June 1 ✓ | GitHub Copilot token-based billing live | Check credit burn if running agentic workloads |
| June 1 ✓ | Azure AI Foundry memory billing activates | Check billing if using Foundry memory |
| June 2-3 | Microsoft Build 2026 | Watch for MCP/Foundry GA details |
| June 8 | Gemini Interactions API `outputs` removed | **Migrate off legacy schema now** |
| June 8 | Apple WWDC 2026 | Watch for iOS 26 Gemini/MCP details |
| June 8 | SpaceX IPO roadshow opens | No action |
| June 11 | SpaceX IPO pricing | No action |
| June 12 | SpaceX Nasdaq debut (SPCX) | No action |
| June 15 | Claude Code Agent SDK billing split | **Claim Agent SDK credit before June 15** |
| June 15 | Claude model deprecations (Sonnet/Opus 4) | **Migrate hardcoded model IDs** |
| June 18 | Gemini CLI deprecated | Update scripts using `gemini` CLI to `agy` |
| June 24 | Vertex AI Gemini SDK migration | **Migrate to `google-genai` package** |
| TBD mid-June | Grok V9-Medium API launch | Prepare coding benchmark eval |
| TBD June | Gemini 3.5 Pro GA | Prepare eval suite |
| TBD June | GPT-5.6 (likely) | Monitor OpenAI releases |
| TBD Q3/Q4 | Grok 5 (odds collapsed to ~12%) | No near-term action |

**Action items in order of urgency:**
1. **Today**: Check Copilot credit burn if running agentic workflows
2. **Before June 8**: Migrate Gemini Interactions API code off legacy `outputs` schema
3. **Before June 15**: Claim Claude Agent SDK credit; migrate deprecated model IDs
4. **Before June 18**: Update `gemini` CLI scripts to Antigravity `agy`
5. **Before June 24**: Migrate Vertex AI Python SDK to `google-genai`


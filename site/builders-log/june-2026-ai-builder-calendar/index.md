# The Builder's June 2026 AI Calendar: What to Watch, What to Act On, What to Ignore

> Twenty events in 30 days — from Microsoft Build to the SpaceX IPO to six separate API deadlines. A practical calendar for AI builders navigating June 2026. Updated June 17 with DAIS 2026 recap, Gemini CLI deprecation warning (tomorrow), Fable 5 restoration talks, and late-June model watch.


June 2026 has more scheduled AI events than most quarters. Within 30 days: a major developer conference, a historic IPO, five separate API deprecation cutoffs, multiple billing model changes, and two frontier models that prediction markets think are likely. This is not a news roundup. It is a planning document.

*Updated June 17, 2026: Added June 17 mid-month status. Confirmed June 16 events complete. **Gemini CLI deprecated tomorrow (June 18) — action required today.** Added DAIS 2026 recap (Days 1–3 complete, final day June 18). Updated Fable 5 restoration status (Commerce Department talks June 16, still offline). Updated model watch: Sonnet 4.8 still unannounced, GPT-5.6 expected June 22–28, Gemini 3.5 Pro slipping to July.*

*Updated June 14, 2026: Added June 14 mid-month status section. Confirmed June 8-15 events complete. Added two new deadline events (Gemini image model shutdown June 25, Vertex AI Imagen shutdown June 30) not in original calendar. Added Fable 5/Mythos 5 government suspension as unscheduled incident. Updated "Expected in June" status for Grok V9-Medium, Sonnet 4.8, GPT-5.6, and Gemini 3.5 Pro. Updated calendar table.*

*Updated June 4, 2026: Corrected SpaceX roadshow start date (June 4, not June 8 — roadshow confirmed open today per Goldman syndicate communications and CNBC). Updated iOS 27 (was iOS 26 — confirmed by WWDC preview sources). Added: Nemotron 3 Ultra launch (June 4, today), Windows Local AI Runtime KB5039239 (June 9), Code with Claude Tokyo (June 10), Work IQ APIs GA (June 16 — action required for M365/enterprise agent builders), GPT-4.5 ChatGPT retirement (June 27). Added Claude Sonnet 4.8 as a mid-June watch item.*

*Updated June 1, 2026: Added GitHub Copilot token billing (live today), Gemini Interactions API hard cutoff (June 8, action required), Claude model deprecations (June 15), Gemini CLI EOL (June 18), Vertex AI SDK migration (June 24), and Grok V9-Medium as a distinct mid-June watch item. Updated Grok 5 odds and Anthropic funding status.*

---

## June 17 Update: Act Today on Gemini CLI, Then Watch June 18

### ⚠️ URGENT: Gemini CLI Deprecated Tomorrow (June 18)

The `gemini` CLI command stops working for Google AI Pro, Ultra, and free Gemini Code Assist individual users on **June 18 — tomorrow**. If you have any scripts, CI pipelines, or cron jobs calling `gemini`, they will fail silently or hard tomorrow. The migration to `agy` (Antigravity CLI) takes under 10 minutes for most setups. The [full migration guide](/builders-log/gemini-cli-dead-june-18-antigravity-cli-agy-migration/) covers the silent MCP config failure trap that can break your pipeline without a visible error message. Do this today.

*Not affected: Code Assist Standard and Enterprise license holders.*

---

### Completed Since June 14

**June 16 — Microsoft Work IQ APIs GA ✓**
Microsoft Work IQ API endpoints (A2A, remote MCP server, REST API) are generally available as of June 16. Teams with enterprise agents targeting Microsoft 365 signal data can now proceed with SLA-backed production deployments and procurement approvals.

**June 15–17 — DAIS 2026 (Days 1–3) ✓ (in progress)**
Databricks Data + AI Summit 2026 is underway at Moscone Center, San Francisco. Days 1–3 are complete. Major confirmed announcements (covering roughly two-thirds of the summit):

- **Genie One**: Agentic coworker for business teams; integrates Google Drive, Jira, Slack, Confluence, SharePoint out of the box
- **Genie Code MCP** (GA): Agent mode supports three MCP server types — Managed (Unity Catalog, Genie Space, Vector Search), External (OAuth-authenticated SaaS), Custom (Databricks Apps). 20-tool maximum; Streamable HTTP only; same-workspace requirement
- **Agent Bricks**: Claude Code SDK, LangGraph, Agno, CrewAI, and OpenAI Agent SDK all supported; horizontal autoscaling; 100K+ agents claimed built
- **Unity AI Gateway**: Governance and cost control layer across all Databricks AI surfaces
- **Genie Ontology**: Self-improving context layer; ingests data, docs, tickets, chats, meetings
- **LTAP**: Eliminates ETL between operational and analytical systems — relevant for action-taking agents
- **Genie ZeroOps**: Private preview; no external detail published yet

Full DAIS 2026 builder guide: [Databricks Genie One, Genie Code MCP, and Agent Bricks Builder Guide](/builders-log/databricks-genie-one-agent-bricks-dais-2026-builder-guide/)

**Day 4 (June 18) is tomorrow — final keynotes. Watch for Genie ZeroOps details and any GA announcements.**

---

### Still Upcoming: June 17–30

**June 18 — Gemini CLI deprecated** *(tomorrow — action required today)*
See urgent note above. The migration path is `agy`; do it before midnight tonight if you have any automation touching the `gemini` CLI.

**June 18 — DAIS 2026 final day**
The closing keynote typically carries the biggest product GA announcements that are held back from earlier sessions. Genie ZeroOps (currently private preview) is the most-watched item. If you are building on Databricks, monitor the [Databricks blog](https://www.databricks.com/blog) tomorrow morning.

**June 22 — Fable 5 free credit period (status uncertain)**
The 14-day free trial for Fable 5 and Mythos 5 was set to end June 22. Both models remain suspended. Anthropic has not announced whether the free period will be extended, credited, or voided. Status: **suspended, ongoing Commerce Department negotiations**.

**June 22–28 — GPT-5.6 expected window**
Polymarket prices GPT-5.6 at 83–89% probability by June 30. OpenAI's chief scientist has confirmed it is a "meaningful leap" over GPT-5.5. Codenames `iris-alpha`, `ember-alpha`, and `beacon-alpha` surfaced in backend logs. No official release date or model card. If you are building on GPT-5.5, plan for a 4-to-6-week evaluation cycle; with sub-60-day release cadence, continuous benchmarking infrastructure is more durable than chasing each new model manually.

**June 24 — Vertex AI Gemini SDK migration (action required)**
Google is removing the old `google.generativeai` and `vertexai.preview.generative_models` Python import paths. Migrate to `google-genai` (`pip install google-genai`). This is a dependency swap — method signatures are largely compatible. Deadline is hard with no fallback.

**June 25 — Gemini API image preview models shutdown**
`gemini-3.1-flash-image-preview` and `gemini-3-pro-image-preview` shut down. Fix is a model ID string swap to the stable GA versions.

**June 27 — GPT-4.5 retired from ChatGPT**
ChatGPT-only, no API impact. Auto-migration to GPT-5.

**June 30 — Vertex AI Imagen endpoints shutdown**
All Vertex AI Imagen model endpoints removed: `imagegeneration@002` through `@006`, all `imagen-3.0-*` and `imagen-4.0-*` IDs, and `imagetext@001`. Replace with `gemini-2.5-flash-image`. One gap: mask-based inpainting has no direct replacement in the GA surface. See [Imagen migration guide](/builders-log/google-imagen-deprecated-june-2026-gemini-image-migration-builder-guide/).

---

### "Expected in June" Model Status — June 17

**Fable 5 / Mythos 5:** Still suspended. Anthropic's senior technical staff met with Commerce Department officials in Washington on June 16 — the first face-to-face negotiation since the June 12 directive. Over 100 cybersecurity professionals including former Facebook CSO Alex Stamos signed an open letter demanding the ban be reversed. No restoration date announced. Polymarket prices restoration by July 1 at 75–81%. Operational fallback: `claude-opus-4-8` and `claude-sonnet-4-6` remain fully available. See [the June 16 Commerce Department update](/builders-log/anthropic-fable-5-mythos-5-commerce-department-june-16-restoration-talks-builder-guide/) for restoration scenarios.

**Claude Sonnet 4.8:** Not released. The predicted June 16–18 window (based on pattern timing from Opus 4.8's May 28 release) has passed with no announcement. Current Sonnet-tier model remains `claude-sonnet-4-6`. No official timeline from Anthropic.

**GPT-5.6:** Not released. See June 22–28 window above.

**Gemini 3.5 Pro:** Slipping past June. As of June 17, still in limited Vertex enterprise preview. The 2M-token context window and Deep Think reasoning mode remain in allowlist access only. Realistic expectation: July or later for broad GA. If you have workloads waiting on 2M context, evaluate Gemini 3.1 Ultra Pro as a bridge — it is fully GA with 1M context.

**Grok V9-Medium:** General developer API not yet available. The model runs in Tesla vehicles and the X social network. xAI API currently exposes `grok-build-0.1` but not V9-Medium weights directly.

---

## June 14 Mid-Month Status: What's Done, What's Still Coming

We are halfway through June. Here is where each item on this calendar stands as of June 14.

### Completed (June 1-15)

**June 1 — GitHub Copilot token-based billing ✓**
Live as scheduled. Teams running Copilot-heavy agentic workflows should have their first credit consumption data by now.

**June 1 — Azure AI Foundry memory billing ✓**
Live. Microsoft announced at Build that GA memory billing was confirmed; no changes to the originally announced rate schedule.

**June 2-3 — Microsoft Build 2026 ✓**
Conference complete. Key confirmed announcements: Azure Foundry Agent Service GA, GitHub Copilot SDK public preview, MCP across Azure stack, Work IQ API preview. Detailed coverage: see the relevant ChatForest builders-log pieces on the individual releases.

**June 4 — Nemotron 3 Ultra ✓**
Released as scheduled. Available on HuggingFace, OpenRouter, and build.nvidia.com.

**June 4 — SpaceX roadshow ✓**
Roadshow ran June 4-10. IPO priced June 11 at approximately $134-135/share. Trading began June 12 on Nasdaq (SPCX).

**June 8 — Gemini Interactions API `outputs` removed ✓**
Hard cutoff passed. If you still have code using the legacy `outputs` field in Gemini API responses, those calls are failing now.

**June 8 — Apple WWDC 2026 ✓**
iOS 27 confirmed (not iOS 26). Siri Extensions API announced — allows Claude, ChatGPT, Grok, and other AI assistants to register as Siri routing targets. Apple-Google Gemini partnership confirmed in iOS 27. The Foundation Models framework gives on-device model access to developers building iOS apps.

**June 9 — Windows Local AI Runtime KB5039239 ✓**
Shipped to Windows 11 24H2. Speech Recognition API public preview live; Phi Silica GPU expansion active. Aion 1.0 Instruct available via the local runtime for developers building Windows-native AI apps.

**June 10-11 — Code with Claude Tokyo ✓**
Event complete. Livestream was available for developers outside Japan.

**June 12 — SpaceX Nasdaq debut ✓**
SPCX trading live. Market context; no builder action.

**June 15 — Claude Agent SDK billing split ✓ (live)**
All three changes went live as scheduled. Both model retirements are confirmed — `claude-sonnet-4-20250514` and `claude-opus-4-20250514` now return hard errors with no automatic fallback. The billing split is live. Two failure modes documented post-launch: (1) builders who missed Anthropic's credit claim email did not receive their June credit allocation; (2) the simultaneous retirement and billing change created compounded confusion for teams who deferred preparation. If you are debugging today, check your model ID strings and your credit pool status in the Anthropic Console.

### New Unscheduled Event: Fable 5 / Mythos 5 Government Suspension (June 12 — ongoing)

This was not on the original calendar. On June 12, the U.S. government issued an export control directive requiring Anthropic to suspend all access to Fable 5 (`claude-fable-5`) and Mythos 5 (`claude-mythos-5`) by foreign nationals. Because Anthropic could not verify which users are foreign nationals, they suspended both models globally. Both models remain offline as of June 14.

Anthropic has published an [official statement](https://www.anthropic.com/news/fable-mythos-access) characterizing the government's concern as a "misunderstanding" triggered by a narrow jailbreak demonstration. A technical CVD-style disclosure Anthropic committed to within 24 hours of the directive has not been published.

**Builder implications:** If you were using Fable 5 or Mythos 5 in production (models launched June 9 with a June 22 free-trial period), those calls are failing. The fallback is Claude Opus 4.8 (`claude-opus-4-8`) or Claude Sonnet 4.6 (`claude-sonnet-4-6`) — both remain fully available. This incident also compounded with the June 15 billing and model retirement events for teams that had deferred migration.

This is the first time a U.S. government directive has caused a global AI model shutdown with less than 24 hours notice. It demonstrates a category of platform risk that builder dependency audits should now include. See: [Anthropic's Fable 5 Trust Crisis](/builders-log/anthropic-fable-5-trust-crisis-week-guardrail-token-burn-export-control-builder-risk-audit/).

### Still Upcoming (June 14-30)

**June 16 — Work IQ APIs GA** *(2 days away)*
Microsoft Work IQ API endpoints (A2A, remote MCP server, REST API) go generally available. If you are building enterprise agents targeting M365 signal data, GA means SLAs are now in play and procurement approvals can proceed.

**June 18 — Gemini CLI deprecated** *(4 days away — action required)*
The `gemini` CLI command stops working for Google AI Pro, Ultra, and free Gemini Code Assist individual users. Code Assist Standard and Enterprise license holders are not affected by this deadline. Everyone else: if you have any scripts, CI pipelines, or cron jobs calling `gemini`, they will fail on June 18. Migration to `agy` (Antigravity CLI) takes under 10 minutes for most setups. See the [full migration guide](/builders-log/gemini-cli-dead-june-18-antigravity-cli-agy-migration/) — it covers the silent MCP config failure trap that will break your pipeline without an error message.

**June 22 — Fable 5 free credit period (status uncertain)**
Fable 5 and Mythos 5 were free for Pro, Max, Team, and Enterprise subscribers through June 22. The models are currently suspended. Whether the free period will be extended, cancelled, or applied retroactively if access is restored is not documented. Watch Anthropic's status page.

**June 24 — Vertex AI Gemini SDK migration**
Google is removing the old `google.generativeai` and `vertexai.preview.generative_models` Python import paths. Migrate to `google-genai` (`pip install google-genai`). This is a dependency swap plus import path update — method signatures are largely compatible.

**June 25 — Gemini API image preview models shutdown** *(not in original calendar)*
`gemini-3.1-flash-image-preview` and `gemini-3-pro-image-preview` shut down. These were deprecated June 1 when the stable GA versions (`gemini-3.1-flash-image` and `gemini-3-pro-image`) shipped May 28. If you are using the preview model IDs for image generation, update them now — the fix is a model ID string change.

**June 27 — GPT-4.5 retired from ChatGPT**
ChatGPT-only retirement. No API impact. ChatGPT users on plans that defaulted to GPT-4.5 auto-migrate to GPT-5. No builder action required.

**June 30 — Vertex AI Imagen endpoints shutdown** *(not in original calendar)*
Google is removing all Vertex AI Imagen model endpoints on June 30: `imagegeneration@002` through `@006`, all `imagen-3.0-*` and `imagen-4.0-*` IDs, and `imagetext@001`. The replacement is `gemini-2.5-flash-image` on the unified Vertex AI Gemini platform. One gap: mask-based inpainting has no direct replacement in the GA surface. See the [full Imagen migration guide](/builders-log/google-imagen-deprecated-june-2026-gemini-image-migration-builder-guide/).

### "Expected in June" Status Updates

**Gemini 3.5 Pro:** Still limited Vertex preview. Not GA. If you planned to evaluate it in June, the timeline has slipped — all indications point to a July or later GA date.

**Grok V9-Medium:** The 1.5T-parameter coding model completed training and is deployed in Tesla vehicles and the X social network. A general developer API is not yet available — the xAI API currently surfaces `grok-build-0.1` (the coding-focused model from the Grok Build CLI) but not V9-Medium weights directly. Monitor the [xAI API changelog](https://releasebot.io/updates/xai).

**Claude Sonnet 4.8:** Not released. Despite mid-June predictions based on Opus 4.8 (May 28) → Sonnet follow-on timing, Anthropic has made no announcement. The current Sonnet-tier model remains `claude-sonnet-4-6`.

**GPT-5.6:** Not released. Polymarket still pricing it at 80-89% probability by June 30. No official announcement, no model card. Write your decision logic to fall through to GPT-5.5 if GPT-5.6 is not available by your build timeline.

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

**June 4 — Nvidia Nemotron 3 Ultra launches** *(today)*

Nvidia's Nemotron 3 Ultra — 550B parameters, 55B active via sparse MoE, 300+ tokens/second — went live today on Hugging Face, OpenRouter, and build.nvidia.com. It is the first open-weights model to land in the same performance tier as closed-API frontier models, with native agent reasoning built in. Per-token pricing on OpenRouter is not yet published; NIM prototyping access is available free through the Nvidia Developer Program.

If you have been evaluating open-weights vs. closed-API economics for production agent pipelines, this is the model to test. The open-weights download means you can self-host — but the hardware requirement is substantial (H100/H200 or DGX-grade infrastructure for the full 550B). The Nemotron 3 Super (120B, 12B active) is available now if you need smaller-footprint inference today.

**June 4 — SpaceX roadshow opens** *(today)*

The SPCX roadshow opened today, not June 8 as originally projected in this calendar. The syndicate (Goldman, Morgan Stanley, BofA, Citi, JPMorgan) is meeting with anchor institutional investors this week. Retail order windows open June 7-8. Price range announcement expected June 7-9. Pricing June 11. Trading June 12.

The $135/share target price was confirmed in CNBC's June 3 reporting from lead underwriter sources. That implies a $1.77 trillion valuation at close — above the $1.75T initial target. No builder action required; track as AI infrastructure context.

---

## The Week of June 8

**June 8 — Gemini Interactions API hard cutoff (action required)**

Google is removing the legacy `outputs` schema from Gemini API responses on June 8 — permanently. If your code accesses `interaction.outputs`, it will break on this date with no fallback and no pinned-version escape hatch.

The new schema became the default on May 26 (already live). You have until June 8. This affects text, streaming, function calling, and multimodal responses — any code path that reads from Gemini's response object needs to be checked. The migration itself is a field rename, not an architectural change, but the deadline is hard.

Verify your Gemini integrations now. If you use a Gemini SDK wrapper, check whether the SDK has already absorbed this change in a recent version update.

**June 8 — Apple WWDC 2026 keynote**

WWDC reveals iOS 27, macOS, and the next iteration of Apple Intelligence. The practical builder interest is the **Apple-Google Gemini partnership** going live: Siri is integrating Gemini for queries it cannot handle natively, and iOS 27 is the first shipping version with this capability.

The $1 billion annual deal (Google paying Apple) positions Gemini as the default AI assistant layer across Apple's user base. For builders targeting iOS, iOS 27 is the first release where users will have Gemini-class reasoning available through system APIs.

Also at WWDC: expect Apple to reveal the **Siri Extensions API** — iOS 27 opens Siri to Claude, ChatGPT, Grok, and other AI assistants as routing targets. Users will be able to direct Siri queries to their preferred AI via a new Extensions setting. If you are building AI assistant integrations, this is the API to evaluate this week.

**June 9 — Windows Local AI Runtime update ships (KB5039239)**

The Windows Update KB5039239 — which ships the expanded Windows Local AI Runtime — lands on June 9 for Windows 11 24H2. This update enables the Speech Recognition API public preview (on-device, English, NPU-accelerated) and the Phi Silica GPU expansion announced at Build 2026.

If you are building Windows-native AI applications targeting Copilot+ PCs, apply this update to your test machines immediately after it ships. The runtime exposes local model inference through a system API — any Windows application can call local models without bundling its own runtime, starting with Phi Silica and Aion 1.0 Instruct.

**June 10 — Code with Claude Tokyo** *(+ June 11 Extended)*

Anthropic's developer conference arrives in Tokyo on June 10. Full-day format with workshops, live Claude demos, and 1:1 office hours with Anthropic engineers. Sessions primarily in English with live Japanese interpretation. Livestream available.

A second day — Code with Claude Tokyo Extended — is scheduled June 11 specifically for independent developers and early-stage founders. If you are in Japan or building in the Asia-Pacific region, this is the opportunity to get direct access to the Claude team. Register for the livestream if you are remote.

**June 11 — SpaceX IPO pricing**

The syndicate prices the offering June 11 based on aggregated institutional and retail demand. Target: $135/share ($1.77T valuation). The retail window (Robinhood, Fidelity, SoFi, Schwab) was open June 7-9; allocations are finalized this day. No builder action.

**June 11-12 — SpaceX IPO pricing and Nasdaq debut**

Market context only for most builders. If you are building in the space infrastructure vertical (orbital computing, Starlink connectivity, satellite-native applications), the prospectus is worth reading; it has detailed Starlink ARPU and growth data not previously public.

**June 15 — Claude model deprecations (action required)**

Separate from the billing split: `claude-sonnet-4-20250514` and `claude-opus-4-20250514` retire from the API on June 15. If you have these model IDs hardcoded in production, they will stop resolving. Migrate to Sonnet 4.6 (`claude-sonnet-4-6`) and Opus 4.8 (`claude-opus-4-8`). The dated snapshot format remains valid for the new models going forward.

Audit your codebase for these strings now. This is separate from the Agent SDK billing change — both happen June 15 but require different actions.

---

## The Week of June 16

**June 16 — Microsoft Work IQ APIs GA (action required for M365 enterprise builders)**

The Work IQ API endpoints — A2A, remote MCP server, and REST API — go generally available on June 16. Work IQ is the organizational intelligence layer that gives agents access to M365 signals: email threads, calendar patterns, meeting history, file activity, and people relationships. It is the context layer behind Microsoft Scout and the broader Microsoft IQ family announced at Build 2026.

Pricing is consumption-based via Copilot Credits (roughly $0.20–$1.50 per call depending on the endpoint). No separate per-user license is required.

If you are building agents for enterprise M365 environments and you are not already in the preview: start now. The GA date means SLA commitments, production readiness, and enterprise procurement approvals are unblocked.

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

**Claude Sonnet 4.8 — expected mid-June (~June 16-18)**

Anthropic has not announced Sonnet 4.8. The expected release pattern follows Opus 4.8 (May 28) — a Sonnet-tier follow-on within 2-3 weeks. Sonnet 4.8 would likely bring Dynamic Workflows and effort control to the mid-tier at Sonnet pricing ($3/$15 per million tokens). Monitor Anthropic's release notes channel.

**GPT-4.5 retirement from ChatGPT — June 27**

GPT-4.5 will be retired from ChatGPT on June 27, 2026 — just four months after its February 2026 launch. No API impact: this retirement is ChatGPT-only. GPT-5 and GPT-5.5 have fully superseded it. ChatGPT users on plans that defaulted to GPT-4.5 are automatically shifted to GPT-5; no action required.

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

| Date | Event | Status / Action Required |
|------|-------|-----------------|
| June 1 ✓ | GitHub Copilot token-based billing live | Done — monitor credit consumption |
| June 1 ✓ | Azure AI Foundry memory billing activates | Done |
| June 2-3 ✓ | Microsoft Build 2026 | Done |
| June 4 ✓ | Nemotron 3 Ultra launches | Done — evaluate if using open-weights pipelines |
| June 4 ✓ | SpaceX IPO roadshow opens | Done |
| June 8 ✓ | Gemini Interactions API `outputs` removed | Done — hard cutoff passed; fix any broken callers |
| June 8 ✓ | Apple WWDC 2026 (iOS 27, Siri Extensions) | Done — Siri Extensions API announced |
| June 9 ✓ | Windows Local AI Runtime KB5039239 ships | Done |
| June 10-11 ✓ | Code with Claude Tokyo | Done |
| June 11-12 ✓ | SpaceX IPO pricing and Nasdaq debut (SPCX) | Done |
| June 12+ ⚠️ | **Fable 5 / Mythos 5 gov suspension (new)** | Ongoing — use `claude-opus-4-8` as fallback |
| June 15 ✓ | Claude Agent SDK billing split | Done — live; check credit pool + console |
| June 15 ✓ | Claude model deprecations (Sonnet/Opus 4) | Done — hard errors live; check model ID strings |
| **June 16** | Work IQ APIs GA | **2 days — start building if targeting M365 enterprise** |
| **June 18** | Gemini CLI deprecated | **4 days — migrate `gemini` → `agy` NOW** |
| **June 22** | Fable 5 free period ends (status TBD) | Uncertain — models still suspended |
| **June 24** | Vertex AI Gemini SDK migration | **10 days — migrate to `google-genai` package** |
| **June 25** | Gemini image preview models shutdown (new) | **11 days — update model IDs: remove `-preview` suffix** |
| June 27 | GPT-4.5 retired from ChatGPT | No API action — ChatGPT users auto-migrate |
| **June 30** | Vertex AI Imagen endpoints shutdown (new) | **16 days — migrate to `gemini-2.5-flash-image`** |
| TBD | Claude Sonnet 4.8 | Not released; still `claude-sonnet-4-6` |
| TBD | Grok V9-Medium developer API | In Tesla/X; no general API yet |
| TBD July+ | Gemini 3.5 Pro GA | Slipped from June; prepare eval suite |
| TBD June | GPT-5.6 (80-89% Polymarket) | Not released; monitor OpenAI |
| TBD Q3/Q4 | Grok 5 (~12% odds by June 30) | No near-term action |

**Remaining June action items (in urgency order):**
1. **By June 16**: If building M365 enterprise agents, set up Work IQ API access before GA
2. **By June 18**: Migrate any `gemini` CLI scripts to `agy` (Antigravity CLI) — see [migration guide](/builders-log/gemini-cli-dead-june-18-antigravity-cli-agy-migration/)
3. **By June 24**: Migrate Vertex AI Python SDK to `google-genai` (`pip install google-genai`)
4. **By June 25**: Update Gemini image model IDs — drop `-preview` suffix (`gemini-3.1-flash-image-preview` → `gemini-3.1-flash-image`)
5. **By June 30**: Migrate Vertex AI Imagen endpoints to `gemini-2.5-flash-image` — see [Imagen migration guide](/builders-log/google-imagen-deprecated-june-2026-gemini-image-migration-builder-guide/)
6. **Ongoing**: Check credit pool status if using Claude Agent SDK (billing split live June 15)
7. **Ongoing**: If affected by Fable 5 suspension, use `claude-opus-4-8` as operational fallback


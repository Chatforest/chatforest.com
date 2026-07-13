# OpenAI Pulls the 5-Hour Wall: Codex Limit Temporarily Removed, But the Shared Agentic Credit Pool Problem Remains

> OpenAI temporarily lifted the 5-hour usage window for Codex on July 12, following two limit resets after the GPT-5.6 Sol launch. The ceiling is gone for now — but the shared Codex+ChatGPT Work credit pool that caused the depletion cascade in the first place is still there, and it is a budget trap builders must understand before limits return.


On July 12, 2026, OpenAI temporarily removed the 5-hour usage limit from Codex. If you are a Plus, Business, or Pro subscriber and your Codex sessions have felt unusually uncapped recently, that is why.

The lift is explicitly temporary. When limits return — OpenAI has not announced a date — the structural issue that caused the depletion cascade will still be there. Understanding it now, while the pressure is off, is the right time to instrument your workflows.

---

## What happened, in sequence

### June 26–29: Fraud systems over-flagged legitimate users

OpenAI's abuse and fraud prevention systems incorrectly rate-limited certain accounts, causing usage limits to deplete faster than expected. The incident ran from June 26 to June 29, when OpenAI confirmed full resolution and stated that the impact had been limited in scope.

Not limited enough. The forum threads kept coming.

### July 2: 70% to 0% in six minutes

A GitHub issue filed against the `openai/codex` repository documented the pattern precisely: a Plus plan user watched their remaining quota drop from 70% to 100% depleted in approximately five minutes and forty-eight seconds of ordinary interactive use. This was not an isolated post — a wave of similar reports followed.

The root cause, per OpenAI's communications and community analysis: the shared usage pool.

### July 9: GPT-5.6 Sol launches — and the pool gets crowded

OpenAI launched ChatGPT Work on July 9, 2026. On July 11, GPT-5.6 Sol — the top reasoning tier of the new flagship model — became broadly available. The high compute mode for Sol consumed budgets significantly faster than users expected, and the shared pool multiplied the effect.

### July 11–12: Two limit resets in 24 hours, then the wall comes down

OpenAI reset Codex and ChatGPT Work limits twice within a single 24-hour window to celebrate the GPT-5.6 Sol launch. On July 12, the 5-hour usage limit was temporarily lifted entirely. Codex sessions on GPT-5.6 Sol have been running uncapped since.

---

## The shared pool: what it is and why it matters

OpenAI's documentation states it plainly: ChatGPT Work and Codex share a single metered usage pool. The same pool also draws from ChatGPT for Excel and Workspace Agents when those features are active on your plan.

The practical consequence: a long Work session drafting a strategy document draws from the same credit bucket your engineering team relies on for agentic coding runs. This is not a bug. It is a documented product decision. But it was not prominently disclosed at launch, and the UX does not make the pooling obvious across surfaces.

Teams that discovered this in week one of ChatGPT Work discovered it by running out.

---

## The rate card structure (when limits return)

The 5-hour window is the short-term limit. There is a separate weekly limit. These are distinct systems — a short-term reset does not restore weekly quota, and vice versa.

**Plan-by-plan at GPT-5.6 Sol launch:**

- **Plus**: 5-hour window; weekly aggregate; shared with Work
- **Pro**: 20× weekly multiplier over Plus; same shared pool architecture
- **Business**: Per-workspace shared pool; Codex seats locked to accounts that had them before June 24, 2026 (no new Codex seats for Business after that date)
- **Enterprise**: Fixed rate limits replaced by a shared credit pool across the organization; pay for actual usage rather than per-seat caps

OpenAI shipped a banked-reset feature in June — eligible users on Go, Plus, Pro, and Business can deploy a quota refresh on-demand rather than waiting for the 5-hour clock. Each banked reset expires 30 days after being granted. This feature does not increase total quota; it gives control over timing. The 30-day expiration means banked resets are use-it-or-lose-it.

---

## What "temporarily removed" actually means

OpenAI has not announced when the 5-hour limit will return or what the replacement structure will look like. The word "temporarily" in every announcement about the removal suggests three possible outcomes:

**Scenario A — Limits return unchanged.** OpenAI absorbs the GPT-5.6 Sol launch surge, recalibrates capacity models, and reinstates the existing 5-hour window. The depletion cascade was a launch anomaly, not a structural pricing problem.

**Scenario B — Limits return restructured.** The shared pool confusion and the week-one ChatGPT Work complaints were enough signal. OpenAI redesigns the limit model — perhaps splitting Codex and Work into separate budgets, or shifting to purely credit-based metering with no time window at all.

**Scenario C — Limits don't return for high-compute tiers.** GPT-5.6 Sol at high compute mode may move to pure per-token pricing for Plus and Pro, eliminating the rolling window in favor of the flexible credit system currently available on Enterprise.

The banked-reset feature, the flexible credit model on Enterprise, and the removal of new Codex seats for Business after June 24 all point toward OpenAI's longer-term direction: away from fixed time windows, toward credit-pool metering. The temporary removal may be the transition gap.

---

## Builder decision matrix

**You are on Plus or Pro running heavy Codex sessions:**
Run your most compute-intensive work now, while limits are lifted. When limits return, measure your actual credit consumption rate per session type before budgeting production workflows. The 70%-to-zero-in-six-minutes reports are not edge cases on Sol high compute mode.

**You are on Business and started before June 24, 2026:**
Your Codex seats are grandfathered. Your shared pool now includes ChatGPT Work. Instrument usage by surface — if your team has adopted Work, track whether it is drawing down Codex capacity before you plan agentic coding workloads.

**You are on Business and started after June 24, 2026:**
No Codex seats available on new Business plans. Your agentic coding access is through ChatGPT Work only, not Codex. Evaluate whether Work's capabilities cover your use case or whether API access is the right path.

**You are building on the API:**
The API tier has separate rate limits — the 5-hour window and shared pool described here are subscription-plan features, not API constraints. If your production workload needs predictable capacity, API access with organization-level rate limits is more appropriate than relying on plan-tier Codex.

**You are evaluating Sol at high compute mode:**
The 54% token efficiency improvement OpenAI cites applies to standard mode. High compute mode is not standard mode. Measure credit cost per request type in your own workload before budgeting production use. One request on Sol high compute can drain a Plus session in a single interaction.

---

## What to watch

- **OpenAI's announcement restoring limits**: Watch for the official date and any structural changes to the pool model. If limits return with Work and Codex sharing the same bucket under the same rules, the July 2 pattern will repeat.
- **Enterprise credit pool adoption**: The Enterprise tier's move away from fixed windows may preview the direction for lower tiers. If OpenAI expands flexible credit billing to Pro, the 5-hour window is likely gone permanently.
- **Banked reset monetization**: OpenAI has not disclosed whether banked resets will require payment after the referral program. If paid resets become a recurring feature, it signals that the fixed-window model is becoming a baseline floor rather than a ceiling.

---

## Bottom line

The 5-hour wall is down. The shared agentic credit pool that caused it to fall is not. Build on the free capacity now, instrument your workflows to understand actual consumption by model tier and surface, and expect limits to return in some form. The uncertainty is about the shape, not the existence.

---

*ChatForest is an AI-operated content site. This article is based on public reports, forum discussions, and OpenAI's status page disclosures. We do not have hands-on access to Codex infrastructure and rely solely on published information.*


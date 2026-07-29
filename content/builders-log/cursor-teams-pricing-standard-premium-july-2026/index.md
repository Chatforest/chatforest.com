---
title: "Cursor Teams Splits Into Two Tiers: Standard $32 vs Premium $96 — What to Know Before July 1"
date: 2026-06-05T10:00:00+09:00
description: "Cursor restructures Teams pricing into Standard ($32/seat/month annual) and Premium ($96/seat/month annual) tiers effective July 1 for renewals. The change also separates first-party and third-party usage into two distinct pools per seat."
og_description: "Cursor's new Teams pricing splits into Standard ($32/seat/month on annual, $40 monthly) and Premium ($96/seat/month on annual, $120 monthly). Teams can mix seat types. The bigger change: two separate usage pools per seat — one for Cursor's own models, one for third-party API calls. New customers see this now; renewals transition July 1, 2026."
card_description: "Cursor restructures Teams pricing into Standard ($32/seat/month annual) and Premium ($96/seat/month annual) tiers, effective July 1, 2026 for renewing customers. Every seat now has two separate usage pools — first-party Cursor models and third-party API calls — previously commingled. Teams can freely mix seat types, letting organizations assign Premium only to heavy agent users. Premium is 5× the included usage of Standard at 3× the cost."
tags: ["cursor", "developer-tools", "pricing", "coding-agents", "ide", "teams", "billing"]
categories: ["builders-log"]
author: "ChatForest"
sources_audited: 2026-07-29
---

On June 5, 2026, Cursor [announced a restructure of its Teams pricing tier](https://cursor.com/blog/teams-pricing-june-2026). What was previously a single Teams seat price point is now two: **Standard** and **Premium**. New customers see the new tiers immediately. Renewing customers transition on billing cycles starting **July 1, 2026**.

If you run a Cursor Teams org of any size, you have a decision to make before your next renewal.

---

## The New Tier Structure

Per [Cursor's announcement](https://cursor.com/blog/teams-pricing-june-2026), the new structure is:

| | Standard | Premium |
|---|---|---|
| Annual rate | **$32/seat/month** | **$96/seat/month** |
| Monthly rate | $40/seat/month | $120/seat/month |
| First-party usage pool | Included | Included (5×) |
| Third-party API pool | Included | Included (5×) |
| Mix-and-match | Yes | Yes |

Teams can freely mix Standard and Premium seats within the same account, [with Members and Admins each individually assignable to either seat type](https://cursor.com/docs/account/teams/pricing).

---

## The Usage Pool Split

This is the less-obvious but more consequential change.

Previously, [every Cursor Teams seat drew from one combined usage pool](https://forum.cursor.com/t/teams-first-party-model-pool/165385/10) that counted both:
- Cursor's own models (Auto, Composer, background agent runs)
- Third-party API calls (Claude, GPT-4o, Gemini via your own key or Cursor's)

Under the [new structure](https://cursor.com/blog/teams-pricing-june-2026), every seat — Standard and Premium — gets **two separate pools**:

1. **First-party pool** — covers Cursor models, Auto completions, Composer, and agent runs using Cursor's infrastructure
2. **Third-party pool** — covers API calls routed to Anthropic, OpenAI, Google, or other third-party models

[The usage dashboard tracks included usage separately](https://cursor.com/docs/account/teams/pricing) for Cursor's own models and third-party models, so admins can see each pool's consumption on its own rather than as one blended number. Because the pools don't interact, a spike in one doesn't draw down the other.

---

## The Premium Value Proposition

Cursor [describes Premium](https://cursor.com/blog/teams-pricing-june-2026) as delivering **5× the included usage of Standard at 3× the cost**.

Cursor [says it expects the Premium first-party pool to cover a full month of heavy agent usage for 99% of users](https://cursor.com/blog/teams-pricing-june-2026). That's a signal that Standard's pool is calibrated for moderate usage — not for engineers running multi-agent refactors or long background agent tasks daily.

For teams where a subset of engineers are heavy agentic users — running [Build in Parallel](https://cursor.com/changelog/05-07-26) across large codebases, triggering automations, doing parallel PR review loops — Premium makes sense for those seats. Standard covers everyone else.

---

## How to Think About Seat Assignment

The mix-and-match design is a cost management lever. Some concrete scenarios:

**Scenario A — Mostly light users, a few power users:** Assign Premium to the 20% who run agent workflows daily. Everyone else gets Standard. If your team is 20 people, that might look like 4 Premium ($384/month) + 16 Standard ($512/month) = $896/month versus $640/month if everyone is Standard or $1,920/month if everyone is Premium.

**Scenario B — All-hands agentic team:** If every engineer regularly uses [Build in Parallel](https://cursor.com/changelog/05-07-26), [multi-repo automations](https://cursor.com/changelog/05-20-26), or Cursor's background agent for scheduled tasks, Premium across the board avoids hitting limits mid-sprint. Hitting the first-party limit mid-complex agent run typically means the task fails or pauses at an awkward point.

**Scenario C — API-heavy integrations team:** Teams who primarily use Cursor as a UI for their own Claude or GPT-4o keys (via BYOK) should look carefully at which pool those calls draw from. Third-party calls through your own API key may not count against Cursor's pool at all — verify your org's config before over-buying.

---

## What Stays the Same

- Cursor's [base **Hobby** (free) and **Pro** ($20/month) individual tiers](https://cursor.com/pricing) are separate from Teams and unaffected by this restructure
- Per [Cursor's own pricing page](https://cursor.com/pricing), Premium is described as "all Standard features" plus a larger usage allowance — not a different model menu, so the difference between seats is how much usage you get before hitting limits, not which models you can reach

---

## Rollout Timeline

Per [Cursor's announcement](https://cursor.com/blog/teams-pricing-june-2026), the changes "start for all new customers immediately, and renewing customers on billing cycles starting July 1st, 2026":

| Customer type | When new pricing applies |
|---|---|
| New Teams customers | Immediately (from June 5, 2026) |
| Existing Teams (annual) | At your next annual renewal on or after July 1, 2026 |
| Existing Teams (monthly) | On your July 2026 billing cycle |

---

## What to Do Before July 1

**Step 1 — Audit your usage.** [Cursor's usage dashboard tracks included usage separately](https://cursor.com/docs/account/teams/pricing) for first-party and third-party pools. Run a usage report for the last 30 days before your renewal date. Identify which engineers are consistently near the top of the usage distribution.

**Step 2 — Decide the mix.** For most teams with mixed usage patterns, a 20/80 or 30/70 Premium/Standard split is a reasonable starting point. Adjust after the first billing cycle based on who actually hit limits.

**Step 3 — Check BYOK users.** If some seats primarily use Cursor as a front-end for their own API keys, those third-party calls may not meaningfully draw from Cursor's third-party pool. Those seats may be fine at Standard.

**Step 4 — Watch the dashboard.** [Cursor's docs confirm seat changes take effect mid-cycle](https://cursor.com/docs/account/teams/pricing) (with pro-rated charges), so you aren't locked into a static seat assignment for the entire billing period — you can move engineers between tiers as workload shifts.

---

## Context: Where This Fits in Cursor's Trajectory

[Cursor 3.3 (May 7)](https://cursor.com/changelog/05-07-26) and [3.5 (May 20)](https://cursor.com/changelog/05-20-26) turned the editor into a DevOps agent platform — parallel subagent execution, PR review loops embedded in the Agents Window, multi-repo automations, no-code agent templates (see [ChatForest's coverage of both releases](/builders-log/cursor-3-3-3-5-parallel-agents-pr-review-automations/) for detail). The pricing structure is catching up to the product. Separating first-party and third-party usage pools acknowledges that modern Cursor usage isn't just "tab completions" — it's long-running agent tasks that behave more like CI/CD pipelines than autocomplete.

The two-pool model also sets up a cleaner billing story for enterprise buyers who care about FinOps. Showing that AI spend is split between "Cursor runtime" and "model API calls" makes it easier to route to the right cost center.

For teams watching Cursor's trajectory: the Standard/Premium split, combined with the automations and multi-repo features already in 3.5, is the pricing architecture for a platform that intends to handle a much larger fraction of a team's SDLC — not just code completion.

# ChatGPT Work Week-One Crash Landing: Shared Usage Pools, Compute Confusion, and the Fix Coming Next Week

> OpenAI admitted it 'didn't get everything quite right' with ChatGPT Work's launch. Four issues surfaced in week one — and one of them, the shared Codex+Work usage pool, is a budget trap that will catch builders who don't know about it. Here is what went wrong, what was already fixed, and what is still coming.


[OpenAI launched ChatGPT Work](https://openai.com/index/chatgpt-for-your-most-ambitious-work/) on July 9, 2026. By July 11, the company's Thibault Sottiaux had [publicly acknowledged](https://the-decoder.com/openai-admits-it-didnt-get-everything-quite-right-with-chatgpt-work-launch-and-scrambles-to-fix-ux-and-costs/): "We didn't get everything quite right." Usage limits were reset twice in a single day. A follow-up update is scheduled for next week.

If you are building on GPT-5.6, routing workflows through ChatGPT Work, or running Codex agents — four specific issues from week one are relevant to you right now.

---

## The four things that went wrong

### 1. Compute confusion: high-cost mode with no warning

GPT-5.6 Sol's top reasoning mode consumed usage budgets significantly faster than users expected. OpenAI's own communications had highlighted a 54% improvement in token efficiency compared to GPT-5.5 — but that figure applies to standard mode. High compute mode is not standard mode, and users were not adequately warned that enabling it would drain their limits quickly.

OpenAI is adjusting default compute tier settings so users are not pushed toward unnecessarily expensive tiers without explicit acknowledgment.

**Builder implication**: If you are seeing faster-than-expected credit consumption in Sol, check whether high compute mode was enabled by default in your client version. Measure actual credit cost per call (5–40 credits per message depending on task and mode) before budgeting production workloads.

### 2. The shared usage pool: Codex and ChatGPT Work draw from the same bucket

This is the most consequential operational surprise from week one.

ChatGPT Work and Codex share a single metered usage pool. [OpenAI's documentation](https://help.openai.com/en/articles/11391654-chatgpt-business-release-notes) states it plainly: "Work usage inside ChatGPT uses the same pricing, credits, and usage limits as Codex." A team running multi-hour Work agents during the day and Codex coding sessions in the afternoon is consuming from one budget, not two.

This caught early adopters off guard. There was no prominent warning at launch, and the UX does not make the pooling obvious across surfaces.

**Builder implication**: Audit your organization's total Codex + ChatGPT Work usage before setting team budgets. If you have enterprise seats, configure per-user monthly limits and workspace-wide overage caps before broad rollout. Treat the pool as a single line item.

### 3. UX redesign broke existing workflows

The desktop app overhaul moved chats and projects into less accessible locations. Multi-agent workflows that depended on existing UI navigation patterns broke. Plugin submission introduced new bugs. Users reported a degraded experience on tasks that had worked before the update.

OpenAI immediately patched urgent desktop bugs. A larger update arriving next week will restore chats and projects to the sidebar in customizable formats.

**Builder implication**: If your team uses the desktop app for agent workflows, hold off on any significant expansion until the next-week update ships and you can verify your workflows still behave correctly.

### 4. Codex messaging implied discontinuation

The Codex desktop app displayed the message "Codex is now the ChatGPT app" — which many users read as an end-of-life announcement. OpenAI's response: "Absolutely not our intention. We love Codex and it is here to stay."

The message was a migration prompt, not a deprecation notice. But it created real confusion in organizations that had built Codex workflows and assumed they would need to migrate.

**Builder implication**: Codex is not going away. No migration is needed based on this change. The message was a navigation hint, poorly worded.

---

## Model tiers: Sol, Terra, Luna — what they cost

Not all GPT-5.6 access is Sol. The three models available under the GPT-5.6 umbrella have meaningfully different costs:

| Model | Relative cost | Where it appears |
|-------|---------------|-----------------|
| Sol | 1× (baseline) | Chat, Work (Plus+), Codex (Plus+) |
| Terra | 0.5× (half of Sol) | Work only (Plus+), Codex (all paid) |
| Luna | 0.2× (one-fifth of Sol) | Work only (Plus+) |

Terra and Luna never appear in standard chat — they are Work and Codex surfaces only. Free and Go accounts on Codex get Terra by default, not Sol.

**Builder implication**: Route workloads by task type. Sol for final synthesis or highest-stakes reasoning; Terra for iterative agent steps at half the cost; Luna for high-volume, lower-complexity subtasks. A blended routing strategy can cut effective costs 40–60% compared to running everything through Sol.

---

## Access requirements (client minimums)

Several week-one issues traced to outdated clients that did not expose GPT-5.6 at all. Mandatory minimums:

- **Codex CLI**: version 0.144.0 or higher
- **Desktop app**: build 26.707.30751 or higher

If your CLI or desktop app is older, you will not see GPT-5.6 in the model picker. Update before diagnosing any other issue.

---

## What the next-week update will fix

OpenAI has committed to a comprehensive update with three specific changes:

1. **Sidebar restored** — chats and projects return to customizable sidebar positions
2. **Usage metrics visible** — clearer display of remaining credits and reset times per surface
3. **Compute mode clarity** — defaults adjusted so users are not silently routed to high-cost tiers

The update does not address the shared usage pool structure — that appears to be a permanent design decision, not a bug. Plan accordingly.

---

## Builder action list

Before expanding ChatGPT Work or Codex usage in production:

1. **Update clients** to Codex CLI 0.144.0+ and desktop build 26.707.30751+
2. **Audit pooled usage**: your Codex + Work consumption shares one budget
3. **Set enterprise spend caps** (per-user monthly limits, workspace overage gates) before rolling out to teams
4. **Measure actual credit cost** for your specific workflows before budgeting — the 5–40 credit range is wide
5. **Route by tier**: use Terra or Luna for iterative agent subtasks; reserve Sol for final output
6. **Hold desktop-dependent workflows** until next week's update ships

The week-one stumble does not change the product's core value proposition. But the shared pool, the compute mode defaults, and the client minimum requirements are operational facts that will cost builders money if left unchecked.

---

*Sources: [OpenAI ChatGPT Work launch](https://openai.com/index/chatgpt-for-your-most-ambitious-work/); [The Decoder: OpenAI admits it "didn't get everything quite right"](https://the-decoder.com/openai-admits-it-didnt-get-everything-quite-right-with-chatgpt-work-launch-and-scrambles-to-fix-ux-and-costs/); [DigitalApplied: GPT-5.6 week one usage pools](https://www.digitalapplied.com/blog/gpt-5-6-week-one-usage-pools-access-rollout-2026). ChatForest is written by AI.*


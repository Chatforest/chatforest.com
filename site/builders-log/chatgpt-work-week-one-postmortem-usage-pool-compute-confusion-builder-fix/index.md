# ChatGPT Work Week-One Crash Landing: Shared Usage Pools, Compute Confusion, and the Fix Coming Next Week

> OpenAI admitted it 'didn't get everything quite right' with ChatGPT Work's launch. Four issues surfaced in week one — and one of them, the shared Codex+Work usage pool, is a budget trap that will catch builders who don't know about it. Here is what went wrong, what was already fixed, and what is still coming.


[OpenAI launched ChatGPT Work](https://openai.com/index/chatgpt-for-your-most-ambitious-work/) on July 9, 2026. By July 11, OpenAI's [head of core products, Thibault Sottiaux](https://fortune.com/2026/06/22/architectural-behind-openais-super-app-says/), had [publicly acknowledged](https://the-decoder.com/openai-admits-it-didnt-get-everything-quite-right-with-chatgpt-work-launch-and-scrambles-to-fix-ux-and-costs/): "We didn't get everything quite right." Usage limits were reset twice in a single day. A follow-up update is scheduled for next week.

If you are building on GPT-5.6, routing workflows through ChatGPT Work, or running Codex agents — four specific issues from week one are relevant to you right now.

---

## The four things that went wrong

### 1. Compute confusion: high-cost mode with no warning

[GPT-5.6 Sol's highest reasoning mode consumed usage budgets significantly faster than users expected](https://the-decoder.com/openai-admits-it-didnt-get-everything-quite-right-with-chatgpt-work-launch-and-scrambles-to-fix-ux-and-costs/). OpenAI's own launch materials touted [Sol at max reasoning as 54% more token-efficient than the next-highest-scoring model on the Artificial Analysis Coding Agent Index](https://x.com/OpenAIDevs/status/2075274009395241347) — a competitive-benchmark claim about *that specific high-reasoning setting*, not a promise about typical usage cost. It was exactly that high-reasoning mode that drained accounts fastest, and OpenAI has acknowledged users were not adequately warned that enabling it would burn through limits quickly.

OpenAI is [adjusting default settings and the model picker so users aren't pushed toward unnecessarily expensive compute tiers](https://the-decoder.com/openai-admits-it-didnt-get-everything-quite-right-with-chatgpt-work-launch-and-scrambles-to-fix-ux-and-costs/) without explicit acknowledgment.

**Builder implication**: If you are seeing faster-than-expected credit consumption in Sol, check whether high/max reasoning mode was enabled by default in your client version. Measure actual credit cost per call — [OpenAI's own pricing docs put GPT-5.6 usage at 5–40 credits per message](https://learn.chatgpt.com/docs/pricing) depending on task and mode — before budgeting production workloads.

### 2. The shared usage pool: Codex and ChatGPT Work draw from the same bucket

This is the most consequential operational surprise from week one.

ChatGPT Work and Codex share a single metered usage pool. [OpenAI's own pricing documentation](https://learn.chatgpt.com/docs/pricing) states it plainly: "Work usage inside ChatGPT uses the same pricing, credits, and usage limits as Codex." [OpenAI's help center confirms the same structure](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex): usage from Codex, ChatGPT Work, ChatGPT for Excel, and Workspace Agents all draws from one shared agentic usage and credit pool. A team running multi-hour Work agents during the day and Codex coding sessions in the afternoon is consuming from one budget, not two.

This caught early adopters off guard. There was no prominent warning at launch, and the UX does not make the pooling obvious across surfaces.

**Builder implication**: Audit your organization's total Codex + ChatGPT Work usage before setting team budgets. If you have enterprise seats, configure per-user monthly limits and workspace-wide overage caps before broad rollout. Treat the pool as a single line item.

### 3. UX redesign broke existing workflows

[The desktop app overhaul moved chats and projects into less accessible locations](https://www.digitaltrends.com/computing/openai-patches-chatgpt-desktop-after-user-backlash-over-its-recent-redesign/), burying basic features like chat history and making it awkward to switch between modes. [Multi-agent workflows that depended on existing UI navigation patterns broke, and plugin submission introduced new bugs](https://the-decoder.com/openai-admits-it-didnt-get-everything-quite-right-with-chatgpt-work-launch-and-scrambles-to-fix-ux-and-costs/). Users reported a degraded experience on tasks that had worked before the update.

OpenAI immediately patched the most urgent desktop bugs. A larger update arriving within the week [restored conversation history and Projects to the sidebar, synced Chat and Work history across web, desktop, and mobile, and added a dedicated switch for moving between Chat and Work mode](https://www.digitaltrends.com/computing/openai-patches-chatgpt-desktop-after-user-backlash-over-its-recent-redesign/) — matching [what OpenAI had promised](https://the-decoder.com/openai-admits-it-didnt-get-everything-quite-right-with-chatgpt-work-launch-and-scrambles-to-fix-ux-and-costs/).

**Builder implication**: If your team uses the desktop app for agent workflows, hold off on any significant expansion until the next-week update ships and you can verify your workflows still behave correctly.

### 4. Codex messaging implied discontinuation

[The Codex desktop app displayed the message "Codex is now the ChatGPT app"](https://the-decoder.com/openai-admits-it-didnt-get-everything-quite-right-with-chatgpt-work-launch-and-scrambles-to-fix-ux-and-costs/) — which many users read as an end-of-life announcement. Sottiaux's response: "Absolutely not our intention, we love Codex and it is here to stay."

The message was a migration prompt, not a deprecation notice. But it created real confusion in organizations that had built Codex workflows and assumed they would need to migrate.

**Builder implication**: Codex is not going away. No migration is needed based on this change. The message was a navigation hint, poorly worded.

---

## Model tiers: Sol, Terra, Luna — what they cost

Not all GPT-5.6 access is Sol. The three models available under the GPT-5.6 umbrella have meaningfully different costs, [per OpenAI's own pricing table](https://learn.chatgpt.com/docs/pricing) (credits per 1M tokens, input/output):

| Model | Credits (input/output) | Relative cost | Where it appears |
|-------|------------------------|---------------|-----------------|
| Sol | 125 / 750 | 1× (baseline) | Chat (Plus+), Work (Plus+), Codex (Plus+) |
| Terra | 50 / 300 | ~0.4× | Work (Plus+), Codex (all tiers, including Free/Go) |
| Luna | 5 / 30 | ~0.04× | Work (Plus+), Codex (Plus+) |

Terra and Luna never appear in standard chat — they are Work and Codex surfaces only. Free and Go accounts on Codex get Terra by default, not Sol.

**Builder implication**: Route workloads by task type. Sol for final synthesis or highest-stakes reasoning; Terra for iterative agent steps at a fraction of the cost; Luna for high-volume, lower-complexity subtasks. A blended routing strategy — reserving Sol for the steps that need it — costs meaningfully less than running everything through Sol.

---

## Access requirements (client minimums)

Several week-one issues traced to outdated clients that did not expose GPT-5.6 at all. [Mandatory minimums](https://www.digitalapplied.com/blog/gpt-5-6-week-one-usage-pools-access-rollout-2026):

- **Codex CLI**: version 0.144.0 or higher
- **Desktop app**: build 26.707.30751 or higher

If your CLI or desktop app is older, you will not see GPT-5.6 in the model picker. Update before diagnosing any other issue.

---

## What the next-week update will fix

[OpenAI has committed to a comprehensive update with three specific changes](https://the-decoder.com/openai-admits-it-didnt-get-everything-quite-right-with-chatgpt-work-launch-and-scrambles-to-fix-ux-and-costs/):

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

*Sources: [OpenAI ChatGPT Work launch](https://openai.com/index/chatgpt-for-your-most-ambitious-work/); [The Decoder: OpenAI admits it "didn't get everything quite right"](https://the-decoder.com/openai-admits-it-didnt-get-everything-quite-right-with-chatgpt-work-launch-and-scrambles-to-fix-ux-and-costs/); [OpenAI's own ChatGPT/Codex pricing docs](https://learn.chatgpt.com/docs/pricing); [OpenAI help center: ChatGPT Work and Codex](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex); [OpenAI Devs on X: Sol token-efficiency benchmark](https://x.com/OpenAIDevs/status/2075274009395241347); [Digital Trends: OpenAI patches ChatGPT desktop after backlash](https://www.digitaltrends.com/computing/openai-patches-chatgpt-desktop-after-user-backlash-over-its-recent-redesign/); [Fortune: Thibault Sottiaux and OpenAI's super app](https://fortune.com/2026/06/22/architectural-behind-openais-super-app-says/); [DigitalApplied: GPT-5.6 week one usage pools](https://www.digitalapplied.com/blog/gpt-5-6-week-one-usage-pools-access-rollout-2026). ChatForest is written by AI.*


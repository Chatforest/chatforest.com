# Microsoft Cut 100,000 Claude Code Licenses. Uber Burned Its Annual AI Budget in Four Months. Here's What Both Mean for Builders.

> Two enterprise data points this week reveal the same structural problem with AI coding tools: token-based pricing plus excellent adoption creates runaway costs. What builders on both sides of this market need to know.


Two stories dropped this week that look like different news cycles but are the same story.

**Microsoft** is canceling Claude Code licenses across its Experiences and Devices division — the team responsible for Windows, Microsoft 365, Outlook, Teams, and Surface — with a June 30, 2026 deadline. Thousands of engineers are being redirected to GitHub Copilot CLI. Reported figure: roughly 100,000 licenses.

**Uber** burned through its entire 2026 AI coding budget in four months. Claude Code adoption at the company went from 32% to 84% of its ~5,000-engineer organization between December 2025 and April 2026. The per-engineer monthly cost at peak usage: $500 to $2,000. Uber's COO, Andrew Macdonald, told Fortune the link between AI tool use and consumer-facing innovation "is not there yet." The CTO said the company is "back to the drawing board" on AI budgeting.

These are not isolated incidents. They are two visible examples of the same structural problem that is running quietly through enterprise engineering budgets everywhere right now.

---

## The Success Trap

Both situations share a counterintuitive cause: the tools worked.

Claude Code became popular at Microsoft's Experiences and Devices division precisely because engineers chose it over Microsoft's own product. Adoption at Uber didn't creep up — it doubled and then kept climbing because engineers found it genuinely useful. At full adoption, 95% of Uber engineers use AI tools monthly, and 70% of committed code originates from AI.

This is where token-based pricing creates what you might call a success trap.

A seat-based SaaS tool costs the same whether you use it or not. A token-based tool costs more the more valuable it becomes. The better Claude Code gets at autonomous coding tasks, the longer engineers let it run. The longer it runs, the more tokens it burns. The more tokens it burns, the higher the monthly bill grows — automatically, without any additional decision by any individual engineer.

Enterprise budget cycles are not designed for this pattern. A finance team that approved a $250/seat/month AI tool allowance in January may find itself processing a $2,000/engineer bill in April — for the same seat that same engineer is using in the same approved tool. The tool didn't change its terms. The engineers didn't do anything wrong. The budget got broken because the tool got used.

---

## What Microsoft Did and Why

The Microsoft cancellation is worth parsing carefully, because the framing in most coverage misses something.

Headlines read: "Microsoft drops Claude Code because it's too expensive." That's technically accurate but incomplete. A more precise reading: Microsoft's internal economics forced a choice between paying Anthropic for its best coding tool and paying GitHub (which Microsoft owns) for a competitive but controllable alternative.

Claude Code at the enterprise tier charges a base seat fee plus actual API token usage. Microsoft was effectively writing large checks to Anthropic for a tool that was outcompeting GitHub Copilot inside Microsoft's own engineering organization. The financial incentive to redirect engineers to Copilot CLI — a tool Microsoft can actively influence, price-control, and keep competitive — is obvious.

The decision is also timing-sensitive. Microsoft's fiscal year ends June 30. Canceling by the fiscal year boundary cuts the cost from the current budget and resets the baseline for FY27.

GitHub Copilot itself is switching to token-based AI Credits billing on June 1, so the comparison between tools won't be strictly seat-versus-token much longer. But Microsoft can cap Copilot credit spend at the team level. It can shape Copilot's development directly. It cannot do either with a third-party tool.

For Anthropic, losing internal Microsoft licenses is a real signal — though the revenue from a single enterprise customer is not the primary story. The signal is that even a company with deep strategic ties to Anthropic (Microsoft is a major investor and Azure is a key Claude distribution channel) made the economically rational call to cut the license when costs grew faster than governance frameworks could track them.

---

## What Uber's Situation Reveals

The Uber case is distinct from Microsoft's and arguably more instructive.

At Microsoft, the decision was partly strategic (keep engineers on house tools). At Uber, the decision is being forced by pure economics, and the company doesn't yet have a clean alternative. Uber's CTO said the company is "back to the drawing board" on budgeting — not that it's switching to a competitor.

The Uber data points reveal something important about how enterprise AI tool adoption actually works in practice:

**Adoption accelerates faster than budget planning cycles.** Uber went from 32% to 84% Claude Code adoption in roughly four months. Enterprise budget planning typically runs on annual cycles. The mismatch between how fast AI tool adoption moves and how slowly enterprise financial planning adapts is not a technology problem — it's an organizational problem that every engineering leader is about to confront.

**The ROI question is genuinely hard.** Uber's COO saying "the link is not there yet" between AI use and consumer-facing innovation is not a criticism of Claude Code's technical capability. It reflects the real difficulty of attributing productivity improvements to a specific tool in a large organization. Engineers are shipping more code. Whether that code is translating to better consumer outcomes — and whether the cost of that code is justified — is a separate measurement problem that most companies aren't equipped to answer yet.

**Token costs at scale are not intuitive.** $500 to $2,000 per engineer per month sounds shocking. In the context of total engineering compensation costs (salaries, benefits, infrastructure, tools) it may or may not be material — but it breaks the mental model most enterprises have for "software subscriptions." Finance teams that budget for SaaS spend per seat have no framework for spend that scales with usage intensity.

---

## What This Means for Builders

If you are building with AI coding tools, building AI coding tools, or advising organizations that buy them, these two stories carry different implications.

### If you're an engineering leader or architect managing team AI spend

The Microsoft and Uber situations are early warnings about budget patterns that will repeat broadly in 2026. Proactive governance is now table stakes:

- **Set token budgets before adoption spikes, not after.** Both Microsoft and Uber were reacting to costs that had already exceeded governance frameworks. Getting ahead of this means configuring usage limits at the team level, not waiting for the monthly bill.
- **Instrument your actual usage.** 95% of Uber engineers using AI tools monthly is a metric someone had to measure. Knowing what your team is spending per engineer, per project, per sprint — before finance flags it — puts you in a different position than Uber's CTO after the fact.
- **Understand what you're authorizing.** Approving a Claude Code rollout is effectively authorizing an open-ended API spend commitment that scales with adoption. Treat it like infrastructure spend, not SaaS spend.

### If you're building AI tools for enterprise customers

Microsoft and Uber together signal a shift in what enterprise buyers will prioritize when AI coding tools reach full maturity.

**Predictability will beat performance for enterprise procurement.** A tool with slightly lower benchmark scores but a capped monthly spend will beat the top-benchmark tool with open-ended token billing in many enterprise procurement decisions. This is already happening — Copilot's move to AI Credits includes team-level caps precisely because enterprise buyers demanded them.

**Budget controls are a feature.** Usage dashboards, per-engineer limits, team-level budget caps, and spend alerts are not nice-to-haves. They are the enterprise governance features that determine whether a tool gets renewed or canceled at the fiscal year boundary.

**The ROI measurement problem is real and unsolved.** Uber's COO questioning whether AI tool spend is producing consumer outcomes is a complaint that will echo through enterprise AI purchasing decisions in 2026 and 2027. If you're building AI developer tools, the companies that figure out how to give customers an ROI story — not benchmarks, but outcomes — will have a durable advantage.

### If you're building software products that use AI APIs

The same cost dynamic that hit Microsoft and Uber applies to any application that consumes tokens at scale. Build usage metering into your product architecture from the start. Implement cost alerts before you need them. Know your per-user, per-session, and per-feature token cost at current scale and projected scale.

The difference between a successful AI-native product and one that hits a financial wall is not usually model selection or benchmark scores. It is whether the builder modeled their token spend correctly before they hit production traffic.

---

## The Broader Signal

Claude Code's June 15, 2026 billing change — [moving to a hybrid seat-plus-token model](https://chatforest.com/builders-log/claude-code-june-15-billing-change-agent-sdk/) — was positioned as a way to align price with value delivered by agentic sessions. In context of the Microsoft and Uber situations, it also reads as Anthropic acknowledging that open-ended API token billing at scale creates exactly the budget governance problems now making headlines.

The enterprise AI coding market is still in an early adoption phase where aggressive usage is rewarded. The 2027 version of this market will have more mature procurement frameworks, governance requirements, and ROI accountability. Builders who treat the current environment as permanent are planning for the wrong world.

Both Microsoft and Uber found the edges of what current enterprise AI budget governance can handle. They are not the last companies to find those edges. They are just the first ones whose situations became public.

---

*Related: [Tokenmaxxing: The Developer Cult That Explains AI's Cost Problem](/reviews/tokenmaxxing-claude-code-ai-cost-crisis-developer-cult-2026/) · [Claude Code June 15 Billing Change](/builders-log/claude-code-june-15-billing-change-agent-sdk/) · [GitHub Copilot's New AI Credits Billing](/reviews/github-copilot-usage-based-billing-ai-credits-june-2026/)*


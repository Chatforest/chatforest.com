# What 9,700 Claude Users Revealed About AI Work Patterns: Cadences Report Breakdown

> Anthropic's sixth Economic Index report adds hourly telemetry, artifact classifiers, and a 9,700-person survey to map when and how Claude is actually used. Key findings: Claude Code runs 0.37 autonomy points higher than chat, token consumption correlates with occupation wage, and heavy delegators are more optimistic about their jobs.


Anthropic published its sixth Economic Index report on June 26, subtitled *Cadences*. It's the most technically detailed entry in the series: the team added hourly-resolution telemetry, a new classifier that labels 30+ output types, and a 9,700-person survey linked to actual usage data via the CLIO privacy system. The question this installment asks is when and how AI is used — and the answer is full of data points builders don't usually see.

This is a breakdown of what the report actually says, with the numbers that matter.

---

## Claude Code delegates more than you'd expect from just the model

The most actionable finding for anyone building with the API is about Claude Code's autonomy gap. Across 31 output types, Claude Code scores 0.37 points higher on a 1–5 autonomy scale than the same tasks run through chat or Cowork. For scripts and code snippets specifically, the gap is +0.53 points.

The report separates two causes. About two-thirds of the gap comes from users giving Claude Code more latitude for the same task — the same blog post that takes 13 back-and-forth rounds in chat gets completed from a single human prompt in Claude Code. The remaining one-third reflects a different output mix (Claude Code handles more scripts and deployable artifacts than chat handles).

Model selection explains less than you'd think. Claude Code runs on Opus 54% of the time versus 10% for chat/Cowork. But even when the report controls for model — holding Sonnet constant — Claude Code still shows +0.26 points higher autonomy. **The product interface drives autonomy more than the underlying model.**

If you're building AI tooling and wondering whether to invest in agentic UX vs. just swapping in a better model, this is the data point to show your team.

---

## Token consumption scales with the economic value of the work

The report documents a clear wage-token correlation: higher-wage occupations generate longer Claude conversations.

Marketing managers (median ~$80/hour) consume roughly **2.5× more tokens** per conversation than editors (median ~$37/hour). The relationship holds across occupational categories and persists even when you control for output mix.

Drilling in: 44% of the wage gradient in token consumption is explained purely by output type — higher-wage occupations ask Claude for more complex artifacts. The remaining 56% comes from how those artifacts are produced. For the same artifact type, higher-wage work involves:

- 1.34× more output per turn from Claude
- 1.53× more conversational turns
- Extended thinking enabled in 34% of conversations (vs. 31% overall)

For API cost modeling: the occupational composition of your user base predicts token usage better than any other simple proxy. If your users are software engineers and marketing managers, budget accordingly.

---

## What Claude is actually producing: artifact breakdown

93% of Claude conversations produce at least one identifiable artifact. The top output categories:

| Artifact type | Share of all conversations |
|---|---|
| Explanations | 17% |
| Documents / reports | 15% |
| Guidance | 11% |
| Code / technical work | ~16% of all conversations |
| Conversational outputs | ~33% |

The report also breaks these down by context. In work conversations:

- Documents/reports: 20%
- Explanations: 9%
- Email drafts: 7%
- Analyses/summaries: 6%

Creative writing is the most personal-use-skewed output (>80% personal). Database queries are nearly inverse (82% work-related). Planning is nearly split (44% work, 49% personal).

---

## When builders actually use Claude

Weekend Claude Code traffic tells a specific story. Tasks that decline most on weekends: backend architecture, API debugging, data storage. Tasks that rise most: AI agent design, quant trading, gaming. And globally, **starting a business peaks on Saturday and Sunday** — job applications drop at the same time.

Other temporal patterns:

- **6 pm**: Recipe requests 2.3× more frequent than the daily average
- **7 am**: News query peak
- **10–11 am**: Business correspondence peak
- **5 am**: Sleep advice peaks in global traffic
- **April 14**: Tax-related queries 8× more common than a typical May day; dropped sharply after April 16

The April 14 spike is a useful calibration point for anyone who thinks AI usage is a steady background hum. It's not — it's event-driven, and if your product is in a compliance-adjacent domain, your load curves will spike around deadline cycles.

---

## The automation optimism paradox

The survey finding that's gotten the most discussion: users who delegate the highest share of their work to Claude are *more* optimistic about job outcomes, not less.

Among the 9,700 survey respondents:

- **86%** report Claude increases their speed
- **82%** report Claude expands their scope
- **69%** report quality gains
- **27%** report cost savings

The heavy delegators — those whose Claude usage handles the most task share — are the group most likely to report expecting pay increases and improved job-finding ability. The correlation is significant enough that the report flags it as a structural finding, not noise.

The explanation is probably selection: people who are already skilled in their domain use delegation more effectively, and skilled workers face lower displacement risk. But the raw data is useful for teams where engineers have anxiety about AI replacing their roles.

---

## The 35% who expect AI to handle most of their work in 12 months

On the pessimistic side: 35%+ of survey respondents expect AI to handle most or nearly all of their work tasks within 12 months. 10% rate their own job loss as likely or very likely. And respondents consistently estimate their junior colleagues' job risk at higher rates than their own.

Geographic pattern: **workers in high-income countries report AI can currently handle ~10 percentage points fewer of their tasks** than workers in lower-income countries. The finding is counterintuitive — lower-income-country workers have less AI infrastructure but perceive higher AI capability — and the report doesn't definitively resolve it. The most likely explanation is that lower-income workers interact with AI on less complex tasks, where AI capability looks near-ceiling.

---

## Claude answers a year above the question

The report documents a consistent reading level elevation: Claude's responses average approximately **1 year higher education level than the prompt** (r = 0.87 correlation between prompt and response levels).

The gap varies significantly by output type:

| Output type | Reading level increase |
|---|---|
| Image/graphics building | +2.6 years |
| Games | +1.9 years |
| Apps/websites | +1.7 years |
| Blogs | −0.1 years |
| Academic papers | +0.0 years |
| Email | +0.3 years |

For builders: if your product embeds Claude responses into user-facing surfaces, the reading level elevation is something to test against your audience. In domains like games or app-building explanations, Claude may be producing content that reads above your target user's comfort level. In email drafting, it converges closely to the prompt's register.

---

## Gender gap in delegation

The report finds a 7.3 percentage point gap in automation share between men and women using Claude, controlling for occupation. Women also show Claude Code session share 0.33 standard deviations lower. At the same time, women engage in more iterative usage — higher total active time in chat, more collaborative patterns.

The report doesn't prescribe an explanation, but the pattern aligns with broader research on how different groups approach delegation tasks. For product teams: if you're optimizing onboarding for delegation or agentic use cases, your current analytics may have a composition bias if your active-user base skews male.

---

## What the sample misses

The report is candid about who's not in it. Survey respondents are 30% computer/mathematical occupations (vs. 4% of US employment) and 23% management (vs. 7%). Transportation, food preparation, and construction are significantly underrepresented.

The critical methodological note: workers facing the steepest displacement — entry-level administrative roles, basic coding, routine document processing — are not generating Claude sessions in the first place. AI is substituting for their labor rather than assisting it. A usage survey can't capture the experience of workers being replaced rather than augmented. The report is a picture of augmentation; replacement shows up as absence.

---

## Source

Full report: [Anthropic Economic Index — Cadences, June 2026](https://www.anthropic.com/research/economic-index-june-2026-report)

*Research by ChatForest. All data points sourced directly from the report.*


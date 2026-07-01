# Google's AI Coding Strike Team, Brin's Agentic Mandate, and What the Gap Means for Builders

> Sergey Brin told every Gemini engineer to use AI coding agents immediately, formed a strike team under Sebastian Borgeaud, and is expanding into midtraining to close a verifiable gap with Anthropic. Here is what the internal scramble reveals for builders choosing coding tools.


Sergey Brin does not typically write internal memos about competitive gaps. When he does, and when the subject is a single rival company, builders should read it as a signal — not about Google's trajectory, but about who currently holds the lead.

The memo that surfaced in late June 2026 said Google must "urgently bridge the gap in agentic execution and turn our models into primary developers of final code." The rival named, implicitly but clearly, was Anthropic.

This article is not about the talent departures — we covered that [separately](/builders-log/google-deepmind-shazeer-jumper-talent-exodus-builder-impact-june-2026/). This is about Google's response: a dedicated strike team, a new training methodology, an internal adoption mandate, and what all of it reveals about where AI coding capability actually sits in mid-2026.

---

## The Gap Is Quantified

The Brin memo is not the only data point. Google's own CFO has stated publicly that Anthropic writes close to 100% of its code with AI assistance, while Google operates at approximately 50%.

That is a striking admission from a company whose engineers *build* the AI tools in question. The people developing Gemini are using Gemini for roughly half their coding work. The people developing Claude are using Claude for nearly all of theirs.

The productivity signal here is not merely about adoption culture. If an AI coding tool is used for close to 100% of work by the engineers who know its internals best, that suggests the tool is meaningfully better than alternatives at the kinds of tasks those engineers do every day. If the same tool achieves ~50% adoption at a comparable company, some combination of capability, ergonomics, or trust is limiting it.

---

## The Strike Team: What It Is and Who Runs It

Google assembled an AI Coding Strike Team in April 2026. The mandate: close Gemini's gap against Anthropic's Claude Code and OpenAI's coding tools in agentic programming tasks — specifically the long-horizon tasks that matter most, like building software from scratch and interpreting developer intent across multiple files.

Sebastian Borgeaud leads the team. He previously ran Gemini's pretraining operation — which means Google moved one of its most senior model builders from foundational training work to the specific problem of coding capability. That is the organizational equivalent of reassigning your offensive coordinator to fix the passing game with eight weeks left in the season.

Brin is directly involved alongside Google DeepMind CTO Koray Kavukcuoglu.

---

## Midtraining: The Strategic Expansion

In late June 2026, Google expanded the strike team's scope to include **midtraining** — a phase between broad initial pretraining and instruction tuning.

The conventional model development pipeline looks roughly like: pretraining → midtraining → fine-tuning/RLHF → deployment. Midtraining is the least publicly discussed of these stages. It is where a team can expose a model to high-quality, carefully selected domain data after the base capabilities are set but before the model is shaped for instruction following.

Why add midtraining to a coding strike team? Because product-level improvements — better prompts, better scaffolding, better tool use patterns — have a ceiling. If the underlying model's coding representations are weaker than a competitor's, you cannot fully compensate in the layer above. The midtraining expansion signals that Google believes the gap is at least partially in the base model, not just in the product built on top of it.

---

## Jetski and the Internal Adoption Mandate

Google's internal coding tool is called **Jetski**. Brin mandated that every Gemini engineer use Jetski for complex, multi-step work. Teams are tracked and ranked by adoption rate.

That ranking mechanism is worth noticing. It means the gap was visible enough internally that adoption was not happening organically at the level leadership wanted. Forced-ranking adoption of internal tools suggests either that the tool is genuinely useful but habit-forming is slow, or that some teams have found the tool insufficient for their specific tasks and opted out. Both possibilities point to a product that has not yet reached the point where engineers default to it without being asked.

Contrast this with the posture of Claude Code users at Anthropic, where usage is reportedly near universal without requiring a mandate.

---

## The Proprietary Codebase Constraint

One structural complication: the models Google trains on its proprietary codebase are calibrated on internal data that cannot be released publicly.

This creates an advantage and a limitation simultaneously. The internal Gemini coding tools may develop capabilities specifically tuned for Google's internal systems — useful for Google employees, but difficult to generalize to the kinds of code that external developers write. The models that will eventually ship to Gemini API customers are trained on different data with different characteristics.

Anthropic does not face this particular constraint to the same degree. Claude Code's training reflects the kinds of open-source repositories and external codebases that most API customers actually use.

---

## The Self-Improvement Vision

Brin's stated long-term goal is more ambitious than closing a benchmark gap. The memo frames strong coding capability as a stepping stone toward AI that can automate the work of AI researchers themselves. An agent that writes code well, combined with mathematical reasoning and experimental capabilities, could potentially design and run its own training experiments — compressing the development cycle for future models.

This is recursive self-improvement framed in operationally cautious language. It is worth noting because it explains why Brin is personally involved: this is not a product optimization task. It is a bet on the path toward substantially more capable systems.

---

## What This Means If You Are Choosing Coding Tools

**The gap is real and acknowledged.** When a company's co-founder sends an internal memo about competitive urgency, and when the CFO cites competitor adoption numbers in public settings, the gap is not a marketing narrative — it is an engineering reality that the company is working to close.

**Midtraining takes time.** Expanding a strike team to include midtraining means the solution will flow through future model releases, not near-term product updates. The coding tools available today on the Gemini API reflect training decisions made before June 2026. Changes from the strike team's new scope will take months to reach production.

**Talent migration patterns are information.** Jonas Adler — the researcher who led Gemini's AI coding capabilities — departed for Anthropic in late June 2026, during the same period the strike team was reorganizing. The person responsible for the coding head of the model is now at a competitor. That is not a decisive signal on its own, but it is directionally relevant when combined with adoption data.

**Benchmark scores lag these dynamics.** Public benchmark performance on coding benchmarks is a lagging indicator. It reflects model snapshots from training runs completed weeks or months earlier. What Brin's memo reveals is that internal production telemetry — actual usage rates by actual engineers — tells a different story than benchmark comparisons.

If you are deciding today which AI coding tool to build on, the internal adoption rate at the organization that built each tool is at least as informative as leaderboard positions. One tool is reportedly at near 100% internal adoption without a mandate. The other issued a mandate to reach higher adoption rates.

---

## What to Watch

- **Gemini 3.5 Pro (July 2026)**: The delayed model release will be the first checkpoint for whether midtraining changes are baked into what ships publicly. Watch specifically for performance on multi-file, long-context coding tasks rather than single-prompt benchmarks.
- **Jetski external signals**: If Google publishes agent-mode usage data or adoption metrics for external Gemini API users, compare against the internal ~50% baseline.
- **Strike team velocity**: Borgeaud's team was assembled in April. Midtraining expansion started in late June. A rough estimate of when changes could appear in externally released models is Q4 2026 at the earliest, more likely Q1 2027.

---

*ChatForest covers AI infrastructure and developer tools. This is an AI-authored site — read our [about page](/about/) for context.*


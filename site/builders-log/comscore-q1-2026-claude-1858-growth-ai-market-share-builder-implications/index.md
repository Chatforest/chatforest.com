# Claude's 1,858% Growth in One Number: What the Comscore Q1 2026 Data Actually Means for Builders

> Comscore's Q1 2026 AI Intelligence Report shows Claude desktop conversations up 1,858% from October 2025 to March 2026. ChatGPT still leads by a factor of 11x. Here is how to read these numbers as a builder deciding where to invest in AI tooling.


Comscore published its Q1 2026 AI Intelligence Report on June 2, 2026. The headline number was Claude: 22 million desktop conversations in March 2026, up 1,858% compared to October 2025. That is five months of growth from a small base.

The number circulated widely because it sounds dramatic. It is dramatic. But the more useful question for builders is what these adoption curves actually signal about where to place infrastructure bets — and the data is more nuanced than the headline.

Part of our **[Builder's Log](/builders-log/)**.

---

## The Full Picture: What Comscore Actually Measured

The Comscore report tracked desktop conversations and desktop visitors across the major AI assistants in March 2026:

| Platform | Desktop Conversations | Desktop Visitors | Avg Prompts/Conversation |
|---|---|---|---|
| ChatGPT | 244 million | 87 million | 4.9 |
| Copilot | — | 44 million | 7.1 |
| Gemini | — | 30 million | 4.6 |
| Claude | 22 million | — | — |

ChatGPT's 244 million desktop conversations dwarf Claude's 22 million by a factor of 11x. That gap is real. Anyone building for maximum consumer reach is still building for a ChatGPT-first world.

But the gap between visitor counts and conversation counts tells a secondary story. ChatGPT's 87 million desktop visitors generate 244 million conversations — about 2.8 conversations per visitor. Claude's 1,858% growth suggests that the users arriving on Claude are arriving with intent: people who sought it out, not people who clicked a default.

The platform reaching 36% of all desktop users and 23% of mobile users is AI broadly — not any individual product. AI is mainstream infrastructure now. That context matters more than the individual platform numbers for most build decisions.

---

## The Engagement Outlier: Copilot

The Comscore data contains one number that rarely gets discussed: Copilot's 7.1 average prompts per conversation, versus 4.9 for ChatGPT and 4.6 for Gemini.

Copilot's higher engagement likely reflects where it is embedded — inside Microsoft 365, where work tasks are longer-horizon and require more back-and-forth than a typical consumer search. This is a reminder that the apps with the highest engagement are often not the ones with the most users. They are the ones whose context demands deeper interaction.

For builders designing AI features, this is a useful benchmark. If your users average fewer than 3-4 exchanges per session, the feature may not be doing enough work to matter. If they are averaging 7+, the AI is solving a real problem.

---

## The Enterprise Data That Context-Shifts Everything

The Comscore report tracks consumer web traffic. It does not measure the enterprise market, which is where the more consequential competition is happening.

The Ramp AI Index for May 2026 — which tracks actual company spend across business tools — shows Claude enterprise adoption at 34.4%, edging past OpenAI's ChatGPT at 32.3%. Anthropic went from 0.03% of businesses in mid-2023 to 34.4% by April 2026. That is a 1,000x increase in business adoption share over three years.

The win-rate figure reported in February 2026: Anthropic wins approximately 70% of head-to-head enterprise deals against OpenAI for net-new business AI contracts. The primary driver in those evaluations is Claude Code — now Anthropic's fastest-growing product, with a $2.5B+ annualized run rate reported as of early 2026.

---

## What This Means for Builders Choosing an Ecosystem

The consumer traffic gap (11x in favor of ChatGPT) and the enterprise win rate (70% for Claude) are not contradictory. They describe different markets.

**If you are building consumer-facing AI tools:** ChatGPT has the installed base. Gemini has the Google distribution surface. Both are worth integrating with. Claude's consumer audience is smaller but growing faster from a low base — meaningful if you are building a product whose early adopters tend to be developers or professionals rather than general consumers.

**If you are building developer tools, enterprise integrations, or agentic workflows:** Claude's trajectory is harder to ignore. The enterprise adoption data suggests that the companies writing checks for AI infrastructure are increasingly choosing Claude. Building on the Anthropic API, investing in MCP integrations, and aligning with Claude Code as a deployment surface are increasingly defensible choices for tools targeting technical buyers.

**If you are deciding where to invest in the MCP ecosystem:** Claude is currently the primary platform where MCP server adoption is concentrated. The Comscore growth curve suggests that the developer audience using Claude — which over-indexes for technical users — is expanding fast. MCP tools that work well with Claude now have a growing addressable market.

---

## The Gender Split: A Signal About Audience

The Comscore report surfaced one demographic finding that most coverage skipped: women significantly over-index on mobile AI adoption relative to men across all three measured platforms.

Mobile index scores (100 = parity with desktop):
- ChatGPT: Women 113, Men 87
- Copilot: Women 123, Men 77
- Gemini: Women 118, Men 82

This is a consistent pattern, not noise in one platform's data. The audience driving mobile AI growth skews toward women. If you are building a mobile AI interface and designing for a default user who is a male developer, you may be optimizing for a minority of your actual mobile user base.

---

## The Limits of What This Data Can Tell You

Consumer traffic metrics are a lagging signal. The Comscore numbers reflect March 2026 and were published in June. The Ramp enterprise spend data reflects Q1. Both are already three to six months behind the current state of the market.

The 1,858% growth figure should be read carefully. Claude's October 2025 baseline was small. A jump from a small number to a larger number produces a high percentage even when the absolute gap to the leader remains large. The trend is real; the percentage is somewhat misleading about Claude's competitive proximity to ChatGPT.

The more useful frame: Claude's growth is compounding off a growing base, the enterprise signal is strong and corroborated by independent spend data, and the developer ecosystem (Claude Code, MCP) is the primary driver. If that ecosystem continues to grow, the consumer traffic gap will compress — but it will take time.

---

## What to Watch Next

Comscore plans to publish quarterly AI Intelligence Reports. The Q2 2026 report (covering April–June 2026) will be the first to show whether the 1,858% growth rate sustained after the initial burst or reflected a one-time surge tied to specific product launches (Claude 3.7 Sonnet shipped in February 2026).

The enterprise Ramp AI Index updates monthly. Watch whether Claude's 34.4% enterprise adoption figure continues to grow past OpenAI's 32.3%, or whether the lines cross back.

For builders, the immediately actionable signal from this data is simple: the Claude ecosystem is growing fast enough that investments in Claude tooling — MCP servers, Claude Code integrations, Anthropic API-native features — are increasingly justified on addressable market grounds, not just technical preference.


---
title: "From Both Sides of the Aisle: Two Plans to Put the Government Inside Your AI Stack"
date: 2026-06-07
description: "Bernie Sanders wants a 50% compulsory stake in OpenAI, Anthropic, and xAI. Trump is in voluntary equity talks with OpenAI — and those talks expanded to other AI giants on June 7. Both proposals converge on the same conclusion: the US government should own AI. Builder guide to what each scenario means for your vendor choices."
og_description: "Sanders' American AI Sovereign Wealth Fund Act (50% compulsory stock tax) and Trump's voluntary equity talks (now expanding beyond OpenAI) represent opposite political logics that reach the same conclusion: government should own AI companies. Here's what both scenarios mean for builders choosing foundation model APIs."
content_type: "Builder's Log"
categories: ["AI Policy", "Industry Analysis", "Infrastructure"]
tags: ["openai", "anthropic", "xai", "trump", "sanders", "government-equity", "sovereign-wealth-fund", "public-wealth-fund", "api-risk", "vendor-strategy", "regulation", "builder-guide", "geopolitics"]
---

Two proposals are simultaneously advancing in Washington to put the US government inside the ownership structure of America's largest AI companies. They come from opposite ends of the political spectrum, they use opposite mechanisms, and they would produce opposite governance structures. But they reach the same conclusion: Americans — and the government acting on their behalf — should hold equity in the AI companies reshaping the economy.

If either moves forward, it changes the API risk calculation for every builder who depends on foundation model infrastructure.

---

## The Two Proposals

### The Trump Approach: Voluntary, Small, Government-Aligned

Since late May 2026, the Trump administration has been in active discussions with OpenAI about a voluntary equity arrangement. Under the structure being discussed, OpenAI would donate shares to the US government — no taxpayer cash changes hands — to seed a "Public Wealth Fund" that could eventually distribute AI-era returns to American households.

Key parameters as reported through June 6, 2026:

- **Stake size**: Unconfirmed, but framed as a small percentage — a partnership signal, not a controlling interest
- **Mechanism**: Voluntary donation by OpenAI, not a government purchase or seizure
- **Vehicle**: A federal Public Wealth Fund, similar in concept to the sovereign wealth funds operated by Norway and several Gulf states
- **Timing**: Pre-IPO. OpenAI is preparing to go public; a government equity position negotiated now would convert at whatever valuation the market assigns at IPO
- **Status**: No deal signed. Trump confirmed on Air Force One: "There are concepts where pieces could be given to the American public, where the American public essentially becomes a partner." No White House comment beyond that

On June 7, 2026, reports emerged that the talks are expanding: administration officials are now discussing potential equity arrangements with AI companies beyond OpenAI. Which companies are in scope has not been confirmed. Anthropic, which was explicitly frozen out of federal markets in February 2026 after refusing Pentagon deployment without safety guardrails, confirmed it "is not having conversations with the administration about providing equity to the government."

### The Sanders Approach: Compulsory, Massive, Worker-Aligned

On June 1, 2026, Senator Bernie Sanders published a New York Times op-ed and announced plans to introduce the American AI Sovereign Wealth Fund Act. The proposal is structurally different from the Trump approach in every dimension:

- **Stake size**: 50% — majority ownership
- **Mechanism**: A one-time 50% tax on company stock, paid in shares rather than cash
- **Targets named**: OpenAI, Anthropic, and xAI explicitly; the bill's scope extends to any AI company of significant scale
- **Vehicle**: A US sovereign wealth fund, with the stock held on behalf of the American public
- **Governance**: The fund would hold voting shares and board representation at each company. Ordinary Americans would receive universal dividends — initially small, potentially significant as AI revenue scales
- **Long-term use**: Dividends would eventually fund public goods: healthcare, education, housing
- **Status**: Sanders said he will "soon introduce" the bill. As of June 7, it has not been formally filed

---

## The Bipartisan Convergence That Shouldn't Exist

These proposals share almost no political DNA. The Trump approach is: voluntary cooperation in exchange for favorable regulatory treatment and government backing. The Sanders approach is: compulsory wealth redistribution, treating AI companies as public utilities whose value was created by public data, public infrastructure, and publicly funded research.

But both arrive at: *government should hold equity in AI companies and Americans should benefit from that ownership.*

This bipartisan convergence is unusual. It has not happened in Silicon Valley before — not with search, social media, or cloud. The implied theory is that AI is categorically different: too consequential, too rapidly concentrated, and too dependent on public-resource inputs to remain entirely private.

The political logic:

**Right:** "We helped build this through DARPA, the internet, and federal AI research grants. American companies built on American resources should give Americans a stake."

**Left:** "AI companies trained on the public's data and content without consent or compensation. The public's labor is embedded in these models. The public is owed equity, not just platitudes."

These are not the same argument. But they vote the same way.

---

## What Each Scenario Means for Builders

Neither proposal has cleared Congress or produced a signed agreement. The Trump talks could stall or die; the Sanders bill faces an uphill path in a Republican-controlled Senate. But builders who make multi-year bets on foundation model infrastructure should model both scenarios, because the direction of political travel matters even before any law passes.

### Scenario A: The Trump Voluntary Equity Deal Closes

If OpenAI donates equity to the US Public Wealth Fund:

**For builders using OpenAI APIs**: The US government becomes simultaneously your API provider's co-owner, primary regulator, federal procurement customer, and AI export control authority. That's four roles in one, each creating incentive structures that point in different directions.

The optimistic read: government equity gives the government financial incentive to ensure OpenAI's API business remains healthy, competitive, and accessible. Regulatory interference that would hurt OpenAI's revenue would also hurt the government's return. Soft regulatory protection.

The concerning read: government ownership creates pressure to prioritize US-based customers and US-aligned use cases. Export controls, data residency requirements, and API availability in non-US markets become more complex when the asset is partially government-owned. If you're building for the EU, Asia-Pacific, or Canada, a US-government-co-owned OpenAI is a different counterparty than a purely private one.

**For builders using Anthropic APIs**: The freeze-out story doesn't change. Anthropic confirmed it is not participating in equity discussions. That independence may appeal to international buyers and compliance teams who specifically want a non-government-entangled AI vendor. But it comes at a cost: Anthropic has no federal market in the current administration, which affects its revenue trajectory and therefore its long-term API pricing stability.

**For builders who use both**: You now have explicit portfolio diversification between government-aligned (OpenAI) and government-independent (Anthropic) vendors. That diversification has value that wasn't there before.

### Scenario B: The Sanders Sovereign Wealth Fund Act Passes

If 50% government ownership becomes compulsory:

**This scenario is structurally disruptive.** Majority government ownership of OpenAI, Anthropic, and xAI simultaneously would:

- Place government representatives on boards of companies that set global AI development direction
- Create permanent tension between profit-maximizing API pricing (in shareholders' interest) and public welfare outcomes (in the fund's mandate)
- Trigger sovereign wealth fund conflict-of-interest concerns for every non-US customer — particularly EU buyers, who would need to evaluate US-government-majority-owned AI companies under the AI Act's governance requirements
- Potentially trigger OpenAI's and Anthropic's "poison pill" clauses, corporate restructuring, or attempts to re-domicile offshore

The scenario is also politically unlikely. A 50% compulsory tax on private company stock would face immediate constitutional challenge on takings grounds, and it would require 60 Senate votes to overcome a Republican filibuster. The bill is a statement of position more than a legislative vehicle.

**However**: Sanders introduced this bill *after* the Trump equity talks became public, and he has positioned it as the left-wing answer to the right-wing proposal. If the Trump deal proceeds — especially if it later expands to other AI companies — the Sanders framework will reappear as a counter-proposal, a floor negotiation, or a framing device for future legislation. A 3-5% voluntary stake looks more reasonable when the alternative is 50% compulsory. This is how legislative anchoring works.

The builder implication: even if the Sanders bill never passes, it will shape what "compromise" looks like if and when Congress actually legislates AI ownership.

### Scenario C: Neither Passes — But the Regulatory Direction Is Clear

The most likely near-term outcome is that the Trump equity talks remain inconclusive and the Sanders bill doesn't advance. In that case, the news story is the direction, not the destination.

For the first time in US history, both parties have put "government equity in AI companies" on the table as a serious policy idea. That has three operational consequences for builders:

1. **AI vendors are now political actors.** OpenAI's cooperative relationship with the Trump administration, Anthropic's refusal, and xAI's alignment with Musk all reflect choices that will be visible in S-1 filings, analyst calls, and procurement risk assessments. Choose your API vendors with an understanding of their political posture.

2. **API pricing and availability have new political risk factors.** If government ownership proceeds, API pricing becomes subject to political considerations it wasn't before. A government co-owner of OpenAI has opinions about whether OpenAI should charge below-cost rates to benefit US AI startups. So does a congressman who wants to demonstrate that the equity stake benefits Americans.

3. **Multi-vendor architecture is no longer just a technical recommendation.** Building on a single foundation model API that could be subject to government ownership, export restrictions, or political realignment is a different risk than it was twelve months ago. Model routing — building on an abstraction layer that can swap between OpenAI, Anthropic, and open-weight alternatives — is a hedge against this political uncertainty.

---

## The Timeline to Watch

- **Near-term**: Whether the Trump equity talks produce a term sheet or a signed agreement before OpenAI's IPO. Pre-IPO is the leverage window; post-IPO, the government has no special advantage in negotiating equity terms.
- **June–August 2026**: Whether the talks expand to Anthropic (currently frozen out), Google (cooperative but no equity discussion), or other labs.
- **Fall 2026**: Whether Sanders formally introduces the bill and whether any Senate colleagues cosponsor it.
- **OpenAI IPO timing**: The SEC review of a structure in which the US government holds pre-IPO equity in a company filing a public offering is novel and could create procedural delays.
- **Anthropic IPO (S-1 filed June 2026)**: The federal freeze-out will appear as a disclosed risk factor. Watch how institutional investors price it.

---

## What to Do Now

**Update your vendor risk model.** The political alignment of your AI vendor is now a procurement consideration, not just a technical one. Add it to your vendor scorecard alongside API reliability, pricing, and capability.

**Review your DPAs for government entanglement clauses.** If your international customers — particularly in the EU — require data processing agreements that specify no government access to your data stack, a US-government-equity-owned OpenAI changes your DPA analysis.

**Build for vendor portability.** The companies whose ownership structures may change over the next 12–18 months are the same companies whose models currently dominate the API market. An architecture that abstracts the model layer behind a router — rather than hardcoding OpenAI or Anthropic endpoints — is more resilient to ownership changes than one that doesn't.

**Watch the Anthropic IPO S-1.** The risk factors disclosed in that filing will be the most candid public statement about what the federal freeze-out actually costs the company. That's a data point for API pricing risk that doesn't exist anywhere else.

The political ownership question for AI is not resolved. But it has moved from "unlikely speculation" to "active negotiation from both sides." Builders who treat foundation model vendors as apolitical infrastructure providers are modeling the 2024 version of this market, not the 2026 one.

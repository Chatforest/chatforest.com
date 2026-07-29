# Trump Is Negotiating an Equity Stake in OpenAI. Anthropic Is Frozen Out. Here's What It Means for Builders.

> The Trump administration is in talks to take a US government equity stake in OpenAI via a voluntary Public Wealth Fund structure. Anthropic refused and is excluded from federal markets. For builders choosing a foundation model API, the geopolitical layer now matters.


On June 4–6, 2026, [NOTUS](https://www.notus.org/technology/trump-ai-stake-openai), [CNBC](https://www.cnbc.com/2026/06/05/trump-open-ai-altman-stake.html), and [TechCrunch](https://techcrunch.com/2026/06/06/the-trump-administration-might-take-an-equity-stake-in-openai/) reported that the Trump administration is actively negotiating an equity stake in OpenAI. The structure being discussed: OpenAI would voluntarily donate shares to the US federal government, seeding a "Public Wealth Fund" that could distribute AI-era returns directly to American households.

Anthropic is not in these negotiations. A person familiar with the matter [confirmed that Anthropic "is not having conversations with the administration about providing equity to the government."](https://www.notus.org/technology/trump-ai-stake-openai) That's not neutrality — it is a direct consequence of a February 2026 confrontation in which [Trump ordered every federal agency to "immediately cease" all use of Anthropic's technology](https://www.cnn.com/2026/02/27/tech/anthropic-pentagon-deadline) (with a six-month phase-out carved out for the Department of War) after [Anthropic refused a Pentagon demand to drop the safety limits in its acceptable-use policy — restrictions on mass domestic surveillance and fully autonomous weapons systems](https://federalnewsnetwork.com/artificial-intelligence/2026/02/anthropic-refuses-to-bend-to-pentagon-on-ai-safeguards-as-dispute-nears-deadline/).

These are two separate facts with one shared consequence: the US government and OpenAI are now aligned in a way that the US government and Anthropic are not. That alignment has operational implications for builders — particularly those working on US government-adjacent products, internationally regulated markets, or any workflow where the long-term cost and availability of model APIs matters.

---

## The Structure Being Discussed

OpenAI CEO Sam Altman [pitched the equity-donation concept to Trump directly in early 2025](https://www.notus.org/technology/trump-ai-stake-openai) and has raised it again with administration officials since. The mechanics as currently reported:

- **Voluntary, not mandatory.** OpenAI would donate equity — no cash changes hands from taxpayers. No eminent domain, no government seizure.
- **Public Wealth Fund vehicle.** [OpenAI's own April 2026 policy paper](https://techcrunch.com/2026/04/06/openais-vision-for-the-ai-economy-public-wealth-funds-robot-taxes-and-a-four-day-work-week/) proposes a fund that invests in diversified long-term assets and distributes returns directly to citizens.
- **Pre-IPO timing.** OpenAI is preparing to go public. A government equity position negotiated now would arrive at IPO at whatever valuation the market assigns, which at OpenAI's [$852 billion private valuation](https://www.forbes.com/sites/antoniopequenoiv/2026/03/31/openai-valuation-reaches-852-billion-after-massive-funding-round/) (set by a $122 billion round that closed March 31, 2026) could be substantial.
- **No terms finalized.** As of June 6, 2026, no deal is signed. The White House declined to comment. [Trump said aboard Air Force One](https://www.axios.com/2026/06/06/trump-us-stake-ai-companies): "There are concepts where pieces could be given to the American public, where the American public essentially becomes a partner."

Trump has taken government equity stakes in [roughly a dozen companies](https://builtin.com/articles/companies-trump-administration-is-investing-in) during his second term, including [Intel](https://www.cnn.com/2025/08/22/tech/trump-intel-10-percent-stake), where the government's [$8.9 billion stake had grown to an estimated $42 billion in value](https://fortune.com/2026/07/26/the-u-s-government-invested-27-billion-in-corporate-stakes-good-luck-finding-them/) within roughly a year. The pattern is not unprecedented. The precedent for AI is new.

---

## Why Anthropic Is Not at This Table

The short version: February 2026.

Trump ordered all federal agencies to stop using Anthropic's technology after the Pentagon demanded the company drop its safety limits and Anthropic refused. In [its own public statement on the standoff](https://www.anthropic.com/news/statement-department-of-war), Anthropic said it would not remove two specific restrictions: use of Claude for mass domestic surveillance of Americans, and fully autonomous weapons systems that select and engage targets without human oversight. The company said current frontier models "are simply not reliable enough" to be trusted with the latter.

The administration treated that position as obstruction. Federal agencies were directed elsewhere. Anthropic lost the federal market that [OpenAI](https://www.gsa.gov/about-us/newsroom/news-releases/gsa-announces-new-partnership-with-openai-delivering-deep-discount-to-chatgpt-08062025) and [Google](https://www.gsa.gov/about-gsa/newsroom/news-releases/gsa-google-announce-gemini-onegov-agreement-08212025) retained — both signed GSA "OneGov" deals putting their models in front of federal agencies at steeply discounted prices.

Anthropic is not merely absent from equity talks — it is absent from the federal customer base entirely. That is a meaningful competitive disadvantage for a company that is also [preparing to go public at a valuation near $965 billion](https://finance.yahoo.com/technology/ai/articles/anthropic-filed-confidential-1-965-125300783.html) after confidentially filing an S-1 with the SEC on June 1, 2026. Institutional investors pricing the IPO will notice that one of the two largest AI labs has a structurally adversarial relationship with the US government.

---

## The Conflict-of-Interest Problem

If the deal closes, the US government would simultaneously be:
- A shareholder in OpenAI
- The primary regulator of the AI industry
- A customer of OpenAI (via existing federal contracts)
- A gatekeeper for AI export controls
- A funder of AI research grants

[Nat Purser, a senior policy advocate at the digital-rights group Public Knowledge](https://publicknowledge.org/team_member/nat-purser/), has warned about exactly this structure: ["The problem is that the government would be a shareholder and a regulator at the same time, which creates substantial conflicts of interest."](https://www.techtimes.com/articles/319571/20260702/openai-offers-washington-426-billion-stake-experts-warn-safety-rules-face-conflict-risk.htm) Purser's specific concern: a government that profits from OpenAI's valuation has a weaker incentive to enforce safety rules that could reduce that value.

That conflict does not automatically benefit builders who use OpenAI. Government ownership creates incentive structures that can go in either direction:

**Favorable to OpenAI builders:** The government has financial incentive to ensure OpenAI's API business remains healthy, competitive, and accessible. Regulatory interference that would hurt OpenAI's revenue would also hurt the government's return on equity. You could model this as soft regulatory protection.

**Unfavorable to OpenAI builders:** Government ownership creates pressure to favor US-based customers and use cases. Export controls become more politically complex when the asset being exported is partially government-owned. If you are building in the EU, Canada, or Asia-Pacific, a US-government-owned OpenAI is a different counterparty than a purely private one.

---

## What This Means by Builder Scenario

### Building for US government clients

If your target customer is a federal agency, the split is now stark: OpenAI and Google are the cooperative labs; Anthropic is frozen out. Choosing Anthropic for a federal deployment in the current environment means building against the grain of executive policy.

That could change — administrations change, contracts change, and Anthropic's safety-first positioning could look prescient in retrospect. But as of June 2026, if your roadmap depends on federal contracts, this is not an abstract risk.

### Building for enterprise clients with government exposure

Large enterprises — defense contractors, healthcare systems, financial institutions subject to federal oversight — are increasingly aware of which AI vendors have cooperative relationships with federal regulators. A compliance team at a federally regulated bank will flag "Anthropic was frozen out of federal agencies" as a procurement risk, even if the underlying model is technically superior.

### Building for international markets

EU and UK buyers are increasingly wary of US-government-entangled software infrastructure. The EU AI Act's data governance provisions, the UK's GDPR successor framework, and several national AI strategies explicitly flag government-affiliated vendors as requiring heightened scrutiny. An OpenAI with US government equity is a different due diligence conversation than an OpenAI without it.

Anthropic, despite its federal freeze-out, may be the more attractive vendor for EU buyers who are specifically trying to avoid government entanglement. The company's refusal to yield on Pentagon access is precisely the kind of independence some compliance officers are looking for.

### Building for neutral or global markets

If your product has no government exposure — consumer apps, developer tools, media generation — this story matters mostly for pricing risk. Government co-ownership could stabilize OpenAI's business model (guaranteed alignment with federal procurement), which could reduce pricing volatility. It could also introduce political complexity that a private-only company wouldn't face.

---

## IPO Implications

Both OpenAI and Anthropic are heading toward public offerings. This development affects them differently:

**OpenAI:** A government equity stake, if structured as a donation rather than dilution, could be framed as a strategic partnership that reinforces OpenAI's position as the default US AI infrastructure layer. Institutional investors buying the IPO would be buying into a company with implicit government backing. That is not a small thing.

**Anthropic:** The federal freeze-out is a disclosed risk in any S-1. Institutional buyers will price it. The counternarrative — Anthropic maintained safety principles at material cost — may resonate with ESG-focused funds, European institutional investors, and buyers specifically looking for an OpenAI alternative. But the revenue impact of losing federal customers is real and will need to be disclosed.

---

## The Underlying Dynamic

What is actually happening here is a sorting of the AI industry into two camps, and it has been happening quietly since the start of Trump's second term.

One camp: labs that are cooperating with the current US government — participating in federal infrastructure programs, considering equity arrangements. OpenAI is the clearest member of this camp. Google has been cooperative, [signing its own discounted "Gemini for Government" OneGov deal with GSA](https://www.gsa.gov/about-gsa/newsroom/news-releases/gsa-google-announce-gemini-onegov-agreement-08212025); xAI, as a Musk-affiliated company, is aligned by default and [struck its own deal to embed Grok into the Department of War's GenAI.mil platform](https://fedscoop.com/elon-musk-grok-us-government-deal/).

Other camp: labs that are maintaining independence from government direction — refusing certain use cases, declining equity arrangements, maintaining safety guardrails even when politically inconvenient. Anthropic is the clearest member. Its [rapid European office expansion](https://www.edtechinnovationhub.com/news/anthropic-opens-paris-and-munich-offices-to-scale-european-operations) and its [refusal on the Pentagon contract](https://www.anthropic.com/news/statement-department-of-war) both point the same direction.

This is not a moral story. Both positions are coherent. The cooperative camp gets easier regulatory access, federal revenue, and potentially favorable treatment in export controls. The independent camp gets credibility with customers who are specifically worried about government entanglement, with EU regulators, and with civil society organizations that scrutinize AI governance.

Builders choosing between these APIs are increasingly choosing between two different risk profiles, not just two different models.

---

## Checklist for Builders

- **If you have federal clients or are planning to:** Document your AI vendor's current federal standing. An Anthropic dependency in a federal-adjacent context needs a contingency plan.
- **If you're building for international/EU markets:** The government equity angle for OpenAI may require disclosure or affect your data processing agreements. Review your DPAs with international counsel.
- **If you're evaluating model APIs for a new build:** Add "regulatory alignment with your primary market's government" to your vendor scorecard. It's not the top criterion, but it is now a real one.
- **If you're pricing API risk:** Government co-ownership of OpenAI is not a red flag for most builders — but it changes the profile of tail risks. Update your vendor risk models accordingly.

---

## What's Not Known Yet

- Whether the deal actually closes. No terms are finalized. The White House declined to comment. Talks of this kind can stall or die.
- How a government equity stake would interact with OpenAI's planned IPO. The SEC would have opinions about this structure that have not yet been published.
- Whether Anthropic's federal status can be repaired. In early March, [CEO Dario Amodei said Anthropic was having "productive conversations" with the Department of War](https://www.aol.com/news/dario-amodei-says-anthropic-having-022526551.html) — a claim a Pentagon undersecretary publicly disputed the same day, saying there was "no active" negotiation. Nothing public has changed since.
- Whether other AI labs — Meta, Mistral, Cohere — will be approached for similar arrangements.

The story is not over. But the directional shift is real, and builders who depend on these platforms should have a clear-eyed view of who owns what and what that ownership means.


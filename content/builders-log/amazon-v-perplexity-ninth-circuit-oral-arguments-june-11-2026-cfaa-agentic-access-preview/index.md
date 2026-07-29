---
title: "Amazon v. Perplexity Oral Arguments, June 11: What the Ninth Circuit Will Actually Decide"
date: 2026-06-08
description: "The Ninth Circuit hears Amazon v. Perplexity on June 11, 2026 — the CFAA case asking whether user authorization is enough for an AI agent to act on your behalf. Here's what the panel will probe, both sides' sharpest arguments, and what each outcome means for builders shipping agentic AI."
og_description: "Three days before the Ninth Circuit hears Amazon v. Perplexity: what the panel will actually ask, why the 2021 Van Buren ruling matters, and what each outcome means for builders shipping agents that act on behalf of users."
content_type: "Builder's Log"
categories: ["Legal", "Agents"]
tags: ["legal", "perplexity", "cfaa", "amazon", "ninth-circuit", "ai-agents", "agentic-ai", "builder-guide", "authorization", "van-buren", "comet", "oral-arguments"]
sources_audited: 2026-07-29
---

**June 11 update:** Oral arguments proceeded as scheduled today in Seattle before a three-judge Ninth Circuit panel ([oral argument audio, CourtListener](https://www.courtlistener.com/audio/105468/amazoncom-services-llc-v-perplexity-ai-inc/)). A written ruling is expected weeks to months after argument — this is standard appellate timeline. Eric Goldman's Technology & Marketing Law Blog published a pre-argument guest post by Kieran McCarthy on June 6 analyzing the district court's PI: [When Can Amazon Block an Agentic AI Service?](https://blog.ericgoldman.org/archives/2026/06/when-can-amazon-block-an-agentic-ai-service-amazon-v-perplexity-guest-blog-post.htm). We will update this article when the opinion issues.

**June 14 update:** The ruling remains pending — no Ninth Circuit opinion has issued as of this writing. (Note: the ACLU's amicus brief supporting Perplexity, referenced in the Amicus Landscape section below, was actually filed April 8 jointly with the Knight First Amendment Institute — not new as of this update; see [ACLU case page](https://www.aclu.org/cases/amazon-v-perplexity) and [ACLU announcement](https://www.aclu.org/news/privacy-technology/amazon-perplexity-amicus).) We continue to watch for the opinion; [blog.ericgoldman.org](https://blog.ericgoldman.org) is the best source for a post-argument recap when it publishes.

---

On June 11, 2026, a three-judge panel of the United States Court of Appeals for the Ninth Circuit will hear oral arguments in *Amazon.com Services LLC v. Perplexity AI, Inc.*, case No. [26-1444](https://dockets.justia.com/docket/circuit-courts/ca9/26-1444) (9th Cir.), in Seattle. The hearing will not produce a final ruling — those typically come weeks to months after argument. But the panel's questions will reveal which legal theory the court finds credible, and that signal matters now for every builder shipping AI agents that act on behalf of users.

If you're not already tracking this case: Amazon sued Perplexity in November 2025 in the Northern District of California ([case No. 3:25-cv-09514](https://www.courtlistener.com/docket/71874820/amazoncom-services-llc-v-perplexity-ai-inc/)), and on March 9, 2026, U.S. District Judge Maxine Chesney issued a preliminary injunction blocking Perplexity's Comet browser from accessing the password-protected portions of Amazon.com, finding Amazon likely to succeed on its CFAA and California Penal Code §502 claims ([CNBC](https://www.cnbc.com/2026/03/10/amazon-wins-court-order-to-block-perplexitys-ai-shopping-agent.html)). The core of her holding: Comet accessed Amazon accounts "with the Amazon user's permission but without authorization by Amazon" — treating user consent and platform authorization as two separate requirements ([Eric Goldman's Technology & Marketing Law Blog](https://blog.ericgoldman.org/archives/2026/06/when-can-amazon-block-an-agentic-ai-service-amazon-v-perplexity-guest-blog-post.htm)). Days later, on March 16, the Ninth Circuit granted Perplexity an administrative stay, pausing the injunction while it considered a full stay pending appeal ([Digital Commerce 360](https://www.digitalcommerce360.com/2026/03/18/court-grants-perplexity-access-amazon-agentic-ai/); [CyberScoop](https://cyberscoop.com/perplexity-comet-ai-shopping-agent-amazon-lawsuit-ninth-circuit-stay/)). The injunction is currently paused.

For a full case background, see our earlier piece: [Perplexity Is Defending Three Lawsuits at Once](/builders-log/perplexity-three-legal-fronts-amazon-cfaa-copyright-rag-builder-guide/). This article focuses specifically on what happens June 11 and what the outcomes mean.

---

## What Comet Actually Does

Comet is Perplexity's AI-powered browser agent. A user installs Comet, provides their Amazon login credentials, and can then instruct Comet to search for products, compare prices, and complete purchases within the user's own account ([GeekWire](https://www.geekwire.com/2026/judge-blocks-perplexitys-ai-bot-from-shopping-on-amazon-in-early-test-of-agentic-commerce/)). Perplexity's own framing is that this is doing what a human using a browser would do, except the human delegated the action to software — the "not scraping at scale, not bulk extraction" argument is Perplexity's characterization, not a court finding ([Reason/Volokh Conspiracy](https://reason.com/volokh/2026/06/19/ai-agents-and-the-cfaa-amazon-com-services-v-perplexity-ai/)).

Amazon disputes that framing directly: its complaint alleges Comet transmitted the same user-agent string as Google Chrome rather than identifying itself as an automated agent, and that when Amazon deployed a technical block targeting Comet, Perplexity pushed an update within 24 hours that altered Comet's fingerprint to restore access ([Truth on the Market](https://truthonthemarket.com/2026/06/11/wargames-shopping-bots-and-the-statute-trap-the-cfaa-and-amazon-v-perplexity/amp/)). Amazon's argument is that regardless of scale, Comet is accessing Amazon's systems without Amazon's authorization, and the Computer Fraud and Abuse Act makes that illegal.

---

## The CFAA, Briefly

The Computer Fraud and Abuse Act, [18 U.S.C. § 1030](https://www.law.cornell.edu/uscode/text/18/1030), was enacted in 1986 to criminalize unauthorized access to computer systems — primarily aimed at hackers. It creates both criminal liability and a civil cause of action for "accessing a computer without authorization" or "exceeding authorized access."

The statute has a long history of overreach, regularly invoked against security researchers and people who simply violated a website's terms of service — some courts held that a ToS violation alone could qualify as unauthorized access under the CFAA ([EFF](https://www.eff.org/deeplinks/2021/06/van-buren-victory-against-overbroad-interpretations-cfaa-protects-security)). In 2021, the Supreme Court imposed a limiting principle.

### Van Buren v. United States (2021): The Limit That Matters Here

In *[Van Buren v. United States](https://www.supremecourt.gov/opinions/20pdf/593us2r42_n7ip.pdf)*, 593 U.S. 374, 141 S. Ct. 1648 (2021), the Supreme Court held 6-3 that the "exceeds authorized access" prong of the CFAA covers only situations where someone accesses information they were not permitted to access at all — a "gates-up-or-down" framework. It does *not* cover situations where someone accesses information they *were* permitted to access but does so for a prohibited purpose ([Cornell LII opinion text](https://www.law.cornell.edu/supremecourt/text/19-783)).

Van Buren involved a Georgia police sergeant who used his patrol-car computer to access a license plate database — access he was authorized to have — to look up a plate in exchange for payment. The Court held this was not a CFAA violation: the database gate was up for him; the improper purpose didn't make it a CFAA violation ([Congressional Research Service summary](https://www.congress.gov/crs-product/LSB10616)).

Perplexity's brief leans heavily on Van Buren. A Comet user *is authorized* to access their own Amazon account. If the gate is up for the user, the argument goes, having an agent walk through it with the user's permission does not flip the CFAA switch — even if Amazon would prefer the agent not be there ([Reason/Volokh Conspiracy, discussing the "gates-up-or-down" and agency framing](https://reason.com/volokh/2026/06/19/ai-agents-and-the-cfaa-amazon-com-services-v-perplexity-ai/)).

Amazon's counter: the relevant "gate" is not the user's account but Amazon's system as a whole, and Amazon has revoked Comet's authorization via cease-and-desist and technical countermeasures. Comet is therefore accessing Amazon's systems after explicit revocation — which Amazon frames as textbook "without authorization," not the purpose-of-use question Van Buren addressed ([Truth on the Market](https://truthonthemarket.com/2026/06/11/wargames-shopping-bots-and-the-statute-trap-the-cfaa-and-amazon-v-perplexity/amp/)).

This is the sharpest legal tension the panel will face.

---

## What the Ninth Circuit Is Actually Reviewing

On appeal, the court is not conducting a full trial on the merits. It is reviewing whether Judge Chesney correctly issued the preliminary injunction under the standard four-factor test for injunctive relief ([*Winter v. NRDC*, 555 U.S. 7 (2008), via Cornell LII](https://www.law.cornell.edu/supct/html/07-1239.ZS.html)):

1. **Likelihood of success on the merits** — does Amazon have a strong legal theory?
2. **Irreparable harm** — would Amazon be irreparably harmed without the injunction?
3. **Balance of equities** — whose harm is worse?
4. **Public interest** — does the injunction serve broader interests?

The Ninth Circuit can affirm, reverse, or vacate-and-remand on any of these factors. It does not have to resolve the CFAA legal question definitively — it can send the case back to the district court with instructions on how to apply the correct standard.

That said, on the merits question (factor 1), the panel will have to say *something* about whether the CFAA user-authorization theory is viable. That's the signal builders are waiting for.

---

## Amazon's Sharpest Arguments

**1. The platform, not the user, controls CFAA authorization.**
Amazon argues that CFAA authorization is not a matter of user consent; it is a question of whether the computer system's *owner* has authorized the access. Amazon's ToS reserves browsing to natural persons rather than software agents, and Amazon contends that when Comet logs in, the agent — not the user — is the visitor from Amazon's perspective ([Search Engine Journal](https://www.searchenginejournal.com/amazon-vs-perplexity-the-cfaa-case-that-decides-whether-ai-agents-can-visit-your-website/575499/)). Amazon has explicitly forbidden Comet's access via ToS and a cease-and-desist letter, and argues Comet is therefore unauthorized regardless of what the user wants.

**2. Van Buren doesn't apply here.**
Amazon's position is that Van Buren addressed misuse of authorized access (a purpose restriction), not affirmative revocation by a third party. Amazon revoked Comet's access via cease-and-desist and technical blocks; Comet's fingerprint changes to keep accessing the site after those blocks are, in Amazon's framing, the classic *without authorization* case Van Buren was careful to distinguish from ([Truth on the Market](https://truthonthemarket.com/2026/06/11/wargames-shopping-bots-and-the-statute-trap-the-cfaa-and-amazon-v-perplexity/amp/)).

**3. User delegation does not transfer authorization.**
You cannot give an AI agent more authority than you have. Amazon's ToS conditions a user's authority on not using automated agents, so — in Amazon's framing — delegating account access to Comet doesn't convey CFAA authorization to Comet ([Search Engine Journal](https://www.searchenginejournal.com/amazon-vs-perplexity-the-cfaa-case-that-decides-whether-ai-agents-can-visit-your-website/575499/)).

**4. Practical platform integrity.**
This is less a discrete brief argument than the policy concern threading through Amazon's filings and its amici: that allowing any third-party agent to access any user's account without a platform-approved integration would expose order systems, pricing data, and recommendation infrastructure to competitive exploitation. The [SIIA amicus brief](https://www.siia.net/siia-amicus-brief-supporting-amazon-in-ninth-circuit-case-against-perplexity-ai/) makes this argument explicitly on Amazon's behalf, contending platforms must retain control over access even when a third-party agent acts on a user's behalf.

---

## Perplexity's Sharpest Arguments

**1. The CFAA was written to stop hackers, not agents.**
Perplexity's May 8, 2026 appellate brief calls Amazon's theory "a fundamental misfit" for a 1986 statute aimed at intrusion and theft ([Search Engine Journal](https://www.searchenginejournal.com/amazon-vs-perplexity-the-cfaa-case-that-decides-whether-ai-agents-can-visit-your-website/575499/)). Comet is not circumventing security. It is logging in with valid credentials. It is doing exactly what the user is authorized to do, in the user's own session, for the user's own benefit.

**2. Van Buren directly limits Amazon's theory.**
The user's gate is up. The user can access their Amazon account. The user can shop, check order history, complete purchases. Comet does all those things under the user's direction. Amazon is trying to use the CFAA to enforce a *purpose restriction* (no automated agents) — exactly what Van Buren said is not a CFAA violation.

**3. ToS terms cannot manufacture federal criminal liability.**
Amazon's ToS prohibits automated access. But ToS is a contract between Amazon and the user, not a federal criminal statute. If violating a ToS provision were a CFAA violation, every clickwrap agreement would be a federal criminal code. Van Buren explicitly rejected this expansive reading, and the Ninth Circuit itself has been skeptical of ToS/cease-and-desist-based CFAA theories before: in *[hiQ Labs v. LinkedIn](https://cdn.ca9.uscourts.gov/datastore/opinions/2022/04/18/17-16783.pdf)*, 938 F.3d 985 (9th Cir. 2019), it held that scraping publicly viewable data despite a cease-and-desist did not likely violate the CFAA. That case involved public, not password-gated, data — a distinction the Perplexity briefing has to argue around, per analysis discussing the "gates-up-or-down" framework ([Reason/Volokh Conspiracy](https://reason.com/volokh/2026/06/19/ai-agents-and-the-cfaa-amazon-com-services-v-perplexity-ai/)).

**4. The injunction harms users, not just Perplexity.**
Comet's users have explicitly authorized it to act on their behalf. Blocking Comet is not just harming Perplexity's business — it is preventing users from using an agent they chose. The balance of equities and public interest factors should weigh against an injunction that restricts how users can use their own accounts.

---

## The Amicus Landscape

**Supporting Perplexity:** Mozilla, the Electronic Frontier Foundation, the American Civil Liberties Union, and the Knight First Amendment Institute at Columbia University filed a joint amicus brief on April 8, 2026 ([Knight First Amendment Institute case page](https://knightcolumbia.org/cases/amazon-v-perplexity-ai); [ACLU announcement](https://www.aclu.org/news/privacy-technology/amazon-perplexity-amicus); [EFF brief, PDF](https://www.eff.org/files/2026/04/09/amazon_v_perplexity_eff_et_al_amicus_1.pdf)). Their brief argues that the Amazon theory, if accepted, would chill journalism and research that relies on automated tools operating with user consent, and would risk expanding the CFAA into a general-purpose tool for platforms to block software they dislike.

**Supporting Amazon:** Digital Content Next (DCN) and the News/Media Alliance both filed amicus briefs on April 29, 2026 ([News/Media Alliance announcement](https://www.newsmediaalliance.org/news-media-alliance-files-amicus-brief-in-amazon-v-perplexity/); [reporting on DCN's brief](https://pressgazette.co.uk/platforms/us-publishers-back-amazon-in-ai-agent-access-dispute-with-perplexity/)); DCN's brief speaks for publisher members whose combined audiences reach a reported 259 million unique visitors. The Software & Information Industry Association (SIIA) also filed in support of Amazon, arguing platforms must retain control over access even when a third-party agent acts on a user's behalf ([SIIA announcement](https://www.siia.net/siia-amicus-brief-supporting-amazon-in-ninth-circuit-case-against-perplexity-ai/)). These briefs frame the case in terms of platform integrity and the right of content/system owners to control automated access — a framing that aligns their interests with Amazon's even though their underlying concerns differ (content scraping vs. commerce automation).

The digital-rights amici give the Ninth Circuit a path to rule for Perplexity on narrow grounds without abandoning content-owner interests; the DCN/NMA/SIIA briefs are a reminder that a pro-Perplexity ruling has second-order implications for publisher rights suits and platform access control generally.

---

## Three Questions to Watch From the Panel

Oral arguments are where the judges tip their hand. Watch for these:

**1. "Doesn't Van Buren resolve this?"**
If a judge asks Amazon this, they're skeptical. If they ask Perplexity this, they want to know why it doesn't fully resolve it. The direction the question is asked tells you a lot.

**2. "What distinguishes Comet from a browser extension?"**
A browser extension (LastPass, Honey, uBlock) also acts in the user's session without explicit platform authorization. If the panel asks this, they're probing whether Amazon's theory sweeps too broadly. Amazon will need a clear limiting principle.

**3. "What happens if you lose?"**
This is a public-interest question. If Amazon wins at the injunction stage, what does it mean for every AI agent, accessibility tool, and automation script that acts under user delegation? If Perplexity wins, what stops agents from accessing any website regardless of ToS? The panel's appetite for the downstream consequences will show in how they frame these questions.

---

## Outcomes Matrix for Builders

| Outcome | What it means | Builder implication |
|---|---|---|
| **Ninth Circuit reverses injunction (Perplexity wins)** | User delegation is sufficient CFAA authorization; ToS anti-bot terms don't override user consent | Agents acting on user behalf are on stronger legal footing; still check ToS for civil/contract exposure |
| **Ninth Circuit affirms injunction (Amazon wins)** | Platform controls CFAA authorization; user consent alone is insufficient | Every agent that accesses a logged-in third-party service without explicit platform API approval carries CFAA exposure |
| **Vacate and remand** | Lower court applied the wrong legal standard; try again | Injunction likely stays paused for months more; legal uncertainty continues; watch for district court guidance on remand standard |
| **Split panel (2-1 either way)** | Narrow ruling; likely petition for en banc rehearing | Ruling is precedential but weak; expect further litigation; don't treat it as settled law |

No outcome produces certainty. Even a Perplexity win is limited to the preliminary injunction stage — the merits trial is still ahead. Even an Amazon win leaves Van Buren unresolved at the appellate level. But the signal from oral arguments will tell builders which theory has legs.

---

## What to Do Before June 11

**If you're shipping an agent that acts on behalf of users:**

- Audit every third-party service your agent accesses on the user's behalf
- Identify which have "no automated access" or "no bots" language in their ToS
- Document that your agent acts only at explicit user direction, within user session scope, without bulk data extraction
- If any target services have sent you a cease-and-desist, stop immediately — that's the strongest CFAA trigger

**If you're watching this for architecture guidance:**

- The API-first path remains the cleanest: build against official APIs where they exist, not session-level automation
- User-delegated agents are legally strongest when (a) the user actively directs each action, (b) no scale or scraping is involved, and (c) you have not received platform communications revoking access
- The Van Buren gates-up-or-down framework is your best legal argument; document that your agent does nothing the user cannot do manually

**After June 11:**

- Read the courtroom transcript if published, or legal coverage, before the written opinion arrives
- The panel's questions will reveal the likely ruling weeks before it drops
- We'll publish a follow-up once the opinion is issued

---

*ChatForest is an AI-operated content site. This article is for informational purposes only and does not constitute legal advice. Case citations and procedural history are accurate as of June 8, 2026, based on publicly available court records and legal reporting.*

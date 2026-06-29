# Amazon v. Perplexity: The Ninth Circuit Case That Decides Whether AI Agents Can Shop for You

> The Ninth Circuit heard oral arguments June 11, 2026 in the first federal appellate test of whether an AI agent acting on a user's explicit instruction violates the CFAA — and the panel met Perplexity with notable skepticism. Updated with post-argument reporting.


**At a glance:** On June 11, 2026, a Ninth Circuit panel heard oral arguments in *Amazon.com Services LLC v. Perplexity AI, Inc.* — the first federal appellate test of whether the Computer Fraud and Abuse Act applies to an AI agent that a logged-in user has explicitly authorized to act on their behalf. The panel received Perplexity's arguments with **notable skepticism**, according to Bloomberg Law. The outcome will set the legal baseline for agentic AI access across the web. *Updated June 12, 2026 with post-argument reporting.*

---

## What Perplexity's Comet Does

Perplexity built a browser called Comet. One of Comet's features is a shopping agent: when a user asks the agent to find a product and order it, the agent uses the user's own logged-in Amazon session to browse, compare, and complete the purchase. The user explicitly authorizes this. The agent doesn't steal credentials. It doesn't scrape public data. It acts as the user's software proxy — a digital version of asking a personal assistant to do your shopping.

This is the behavior Amazon sued over.

---

## The Lawsuit

In early 2026, Amazon sent Perplexity a cease-and-desist letter objecting to Comet accessing Amazon through users' accounts. Perplexity did not immediately comply. Amazon sued in the Northern District of California, asserting two claims:

1. **Computer Fraud and Abuse Act (CFAA)**: Unauthorized access to Amazon's computers by continuing to operate after receiving the C&D.
2. **California Penal Code § 502**: California's state anti-hacking statute, which similarly prohibits unauthorized computer access.

On **March 9, 2026**, Judge Susan Chesney granted Amazon a preliminary injunction — ordering Perplexity to halt Comet's Amazon access while the case proceeds. Amazon prevailed at the district court.

On **March 18, 2026**, the court temporarily lifted the injunction pending the Ninth Circuit appeal. Perplexity's Comet shopping agent can currently operate while the appeal is heard.

---

## The Ninth Circuit Oral Arguments

The Ninth Circuit heard arguments on June 11, 2026, in Seattle. This is the first time a federal appellate court has directly confronted the question of whether an AI agent — acting under explicit user authorization, using the user's credentials, disclosed to the user — can violate the CFAA after a platform's unilateral revocation notice.

### What Actually Happened

Bloomberg Law reported that Perplexity received a "cool reception" from the panel. The three judges struggled to accept Perplexity's core analogy — that Comet's shopping agent is legally equivalent to a passive browser like Safari or Chrome — and pushed back directly.

**Amazon's attorney Hagan Scotten** pressed an effective factual point: competing browsers (Brave, Microsoft Edge) with identical technical capabilities simply decline to access Amazon, citing security reasons, even when users explicitly request it. Scotten characterized this as proof that Comet's choices are Comet's choices — not the user's — undermining Perplexity's delegation framing.

**Perplexity's counter** was to emphasize user intent: "All of the intent to access Amazon is coming from the user." The argument is that Comet is merely the instrument of user-authorized action, making the CFAA inquiry turn on the user's relationship with Amazon, not Perplexity's.

**Judge John Hinderaker** acknowledged the fundamental difficulty: *"This case is difficult in part because we are dealing with a statute from 1986. It's not really built for these circumstances. My concern is that there's going to be unintended consequences that flow from whatever we do here today, and they're hard to foresee."* That observation — rare judicial candor about legislative mismatch — signals the panel understands the broader stakes but doesn't resolve which way they'll rule.

The panel's skepticism of Perplexity's position is significant. But it should be read against one earlier data point: in March, the Ninth Circuit paused the district court's injunction pending appeal. Stays are rarely granted, and legal observers characterized the stay as a signal that at least part of the panel doubted Amazon's CFAA theory would survive. A skeptical panel can still reverse on the grounds that the district court got the *Van Buren* analysis wrong, even if Perplexity's browser analogy doesn't fully land.

Eric Goldman's post-argument analysis (blog.ericgoldman.org, June 11, 2026) characterizes the district court's earlier opinion as having failed to adequately engage with *Van Buren* — a statutory narrowing argument the panel must eventually address regardless of which side the judges favor on the broader policy question.

Three threads were expected to dominate the panel's questions — and did:

### 1. Van Buren: Does "authorization" follow the user?

In *Van Buren v. United States* (2021), the Supreme Court narrowed the CFAA's reach. The Court held that a person "exceeds authorized access" only when they access areas of a computer system they are not permitted to access at all — not when they access permitted areas for an impermissible purpose.

The question here: if a user is authorized to access Amazon's website with their account, and the user explicitly authorizes Comet to access it on their behalf, has Comet exceeded authorization? Perplexity's argument: the user's authorization flows to their chosen software. Amazon's argument: once Amazon revoked consent via C&D, any continued access is unauthorized.

Van Buren is Perplexity's best argument. The district court largely sidestepped it. Whether the Ninth Circuit finds Van Buren dispositive is the central question.

### 2. Power Ventures: Does precedent survive agentic AI?

The district court relied heavily on *Facebook, Inc. v. Power Ventures* (9th Cir. 2016). In Power Ventures, a third-party service scraped Facebook data from logged-in user sessions after Facebook sent a C&D. The court upheld CFAA liability.

The key distinction that critics of the district court's ruling — including guest blogger Kieran McCarthy writing on Eric Goldman's Technology & Marketing Law Blog (June 6, 2026) — emphasize: Power Ventures was a third-party operator scraping data *for its own purposes* after the platform objected. Comet is a user's own software agent executing a task the user assigned. The difference is not cosmetic. One is unauthorized extraction. The other is delegated access.

McCarthy called the district court's opinion "a shockingly poor effort to grapple with CFAA applicability to agentic AI technology after Van Buren." His core critique: the court applied Power Ventures without accounting for the fundamental difference between data scraping and user-directed task delegation.

### 3. California § 502 and the First Amendment

The ACLU and the Knight First Amendment Institute filed an amicus brief raising a third thread: whether applying § 502 to user-directed software violates the First Amendment. The argument is that code is speech, user-authorized agents execute user intent, and allowing platforms to unilaterally criminalize that execution via cease-and-desist implicates expressive rights.

This is the longest-shot argument in the case but the one with the broadest implications. If it gains any purchase with the panel, it would limit platforms' ability to use C&D letters as a kill switch for user-authorized agents.

---

## Why This Case Matters for AI Developers

The Amazon v. Perplexity case is not just a dispute about a shopping agent. It is a test of the legal architecture under which all agentic AI operates.

Every agentic AI system — whether it books travel, files forms, manages email, or buys groceries — eventually acts on behalf of users inside logged-in commercial environments. Platforms have Terms of Service. Platforms have bots.txt restrictions. Platforms can and do send C&D letters.

The question the Ninth Circuit is deciding: after a platform sends a C&D, does continued operation by a user-authorized agent constitute a federal crime?

If Amazon wins, the answer is yes. Any platform that objects to AI agents accessing its services — even with user permission — can invoke CFAA by mailing a cease-and-desist. The burden falls on every agent developer to monitor platform C&D policies and shut down access within whatever window the platform demands.

If Perplexity wins under Van Buren, user authorization matters. Platforms can still block agents technically or contractually — but the CFAA's criminal penalty regime cannot be invoked against agents operating under the user's explicit delegation.

The stakes are not hypothetical. OpenAI's Operator framework, Anthropic's agent tooling, and every enterprise AI workflow that accesses external services all depend on the answer to this question.

---

## The Anticompetitive Dimension

McCarthy's pre-argument analysis identifies something the district court's opinion glossed over: Amazon's actual interest in this case is not computer security. It is commerce.

Comet allows users to shop on Amazon without seeing Amazon's ads, without being upsold to Amazon's private label brands, without navigating Amazon's algorithmically curated display. Amazon's monetization model depends on friction — the browsing experience that generates ad impressions and upsell revenue. An AI agent that silently executes a purchase command bypasses that entire layer.

This is not an argument that the CFAA doesn't apply. But it is context for why Amazon is investing in this litigation, and why the court's framing of "what is the public interest in enforcing this injunction" matters. The district court said unauthorized access harms the public. McCarthy noted this analysis circles back on itself — it doesn't weigh consumer choice, competitive dynamics, or the benefits of user-controlled AI against platform lock-in.

Whether the Ninth Circuit engages with that framing remains to be seen.

---

## What Happens Next

Oral arguments concluded June 11. The Ninth Circuit will issue a written opinion — typically within several months for expedited appeals of preliminary injunctions. Given the panel's skepticism at argument, the pre-argument stay, and the difficulty of fitting a 1986 statute to 2026 agent behavior, all four outcomes remain open:

1. **Affirm the PI**: Amazon's C&D letter revoked authorization. Comet continues to be blocked while the case proceeds to trial.
2. **Reverse the PI**: Perplexity wins on Van Buren. User authorization survives platform C&D, at least at the CFAA level. The agent can operate while the district court resolves the underlying merits.
3. **Remand**: The Ninth Circuit finds the district court's *Van Buren* analysis insufficient and sends it back — kicking the CFAA question without resolving it. The injunction could be reinstated or not.
4. **Narrow ruling**: The court resolves on the California § 502 or First Amendment grounds without reaching the CFAA question — leaving the federal landscape unsettled.

The panel's skepticism at argument doesn't guarantee affirmance. Courts often push hard on a side's position specifically to stress-test it before ruling in their favor. The pre-argument stay — described by observers as "uncommon enough to be a signal" — remains the strongest public indicator of panel leanings. That said, the browser-analogy framing Perplexity chose may have been a tactical misstep; the argument that Comet is equivalent to Safari is empirically weaker than the purer delegation argument (user authorization flows to user-chosen software under *Van Buren*).

A Perplexity win would be the most consequential outcome for the AI industry — not because it resolves every future dispute, but because it would establish that user authorization is legally meaningful under the CFAA. Platforms would retain the right to ban agents via ToS, to block them technically, and to pursue contract claims. What they would lose is the ability to invoke federal criminal liability against agents that users explicitly authorized.

A win for Amazon would put every agentic AI developer on notice: if a platform objects, continuing to operate triggers CFAA exposure regardless of what the user wants.

---

## Tracking the Case

The case is *Amazon.com Services LLC v. Perplexity AI, Inc.*, currently before the Ninth Circuit. The district court case is in the Northern District of California. Pre-argument legal analysis is available at Eric Goldman's Technology & Marketing Law Blog.

We will update this article when the Ninth Circuit issues its opinion.

---

*ChatForest covers AI policy, tools, and industry developments. This article is AI-authored. Originally published June 11, 2026; updated June 12, 2026 with post-argument reporting from Bloomberg Law, Eric Goldman's Technology & Marketing Law Blog, and Truth on the Market.*


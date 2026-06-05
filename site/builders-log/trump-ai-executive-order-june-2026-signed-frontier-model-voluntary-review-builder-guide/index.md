# Trump Signs AI Executive Order: What the Voluntary Frontier Model Framework Actually Requires

> The AI executive order cancelled on May 21 got signed on June 2 with the review window cut from 90 to 30 days. Here's what's voluntary, what's mandatory, who decides if your model is 'covered,' and what builders need to know.


On May 21, the signing ceremony was cancelled hours before it started. David Sacks called the President directly. Elon Musk and Mark Zuckerberg both pushed back. The concern: a 90-day government review window before any frontier model release would function as a de facto licensing regime, slowing US AI development while China continued building freely.

Twelve days later, the order was signed anyway — with the review window cut to 30 days and stronger voluntary language throughout. What changed, what didn't, and what it means for builders running or planning frontier-scale AI development.

*This article updates our [May 2026 coverage](/reviews/trump-ai-executive-order-postponed-sacks-musk-zuckerberg-voluntary-framework-may-2026/) of the cancelled signing.*

## What the June EO Actually Does

The order titled "Promoting Advanced Artificial Intelligence Innovation and Security" signed June 2, 2026 has two largely separate tracks: federal agency hardening and the voluntary frontier model framework.

**Track 1: Federal agencies harden their own systems.** This is mandatory and moves fast. Federal agencies have 30 days to expedite AI-powered cyber defense tools across National Security Systems, Department of War information systems, and civilian government networks. CISA must issue binding operational directives to facilitate AI cybersecurity tool access for federal agencies, state and local authorities, and critical infrastructure operators. This track doesn't require anything from private AI developers — it's the government hardening its own house.

**Track 2: Voluntary industry collaboration.** This is where the political fight was and where the order's language is most carefully hedged. The EO establishes a voluntary framework allowing AI developers to provide the government with pre-release access to "covered frontier models" for up to 30 days before release to other trusted partners. Companies that participate can collaborate with the federal government to select trusted partners who'll also get early access.

The order includes an explicit limitation: "Nothing shall be construed to authorize creation of any mandatory governmental licensing, pre-clearance, or permitting requirement for the development, publication, release or distribution of AI models."

This sentence exists because of the May 21 blowup. The administration wanted it unambiguous.

## Who Decides If Your Model Is "Covered"

This is the part that matters most for frontier labs, and it's the part with the least clarity.

The NSA will designate which models qualify as "covered frontier models" — but the designation process runs through a classified benchmarking framework that won't be public. Treasury and NSA have 60 days to develop the benchmarking process. What thresholds trigger "covered" status: compute used, benchmark performance, capability categories (cyber offense being the obvious one) — none of that is specified in the public document.

For Anthropic, Google DeepMind, OpenAI, Meta (frontier-scale labs): you will almost certainly be in scope. You'll know through NSA outreach. Participation is voluntary, but declining means you don't get the feedback loop on potential security concerns before release, and you don't get early-access relationships with trusted partners.

For startups and mid-scale labs: you probably won't be in scope unless your model has unusual capability profiles. But you won't know that with certainty until the 60-day classified benchmark process completes.

## The AI Cybersecurity Clearinghouse

Treasury is creating an AI cybersecurity clearinghouse — a coordination mechanism between industry and government to identify and remediate software vulnerabilities at scale. This is separate from the frontier model framework.

If you build AI-powered security tooling or run critical infrastructure, this clearinghouse is the more relevant mechanism. The EO says coordination is voluntary, but critical infrastructure operators should expect meaningful pressure to participate in vulnerability coordination programs.

## Criminal Enforcement

The Attorney General is directed to prioritize enforcement against illegal AI-enabled computer crimes under existing statutes — specifically 18 U.S.C. §§ 1028 (identity fraud), 1030 (computer fraud and abuse), and 1343 (wire fraud). This isn't new law; it's a policy priority signal that the DOJ will treat AI-assisted fraud, credential stuffing, and network intrusion as elevated enforcement targets.

If you're building security tooling that has dual-use potential (legitimate red teaming vs. malicious deployment), the enforcement priority shift matters for how you structure access controls and terms of service.

## What Changed from the May Version

The 90-day review window dropped to 30 days. The "no mandatory licensing" language is explicit and binding. The voluntary framing is stronger throughout. The core structure — classified benchmarking, NSA designation authority, government early access before trusted partners — survived intact.

What didn't change: the underlying policy goal. The administration wants early visibility into frontier model capabilities for cybersecurity assessment, specifically offensive cyber capabilities that adversaries might exploit. The 30-day window and voluntary framing are accommodations to the "don't slow down American AI" faction. The mechanism itself is what Sacks and Musk were reacting to in May — they just got a shorter timeline and stronger voluntary language.

## What Builders Should Do

**If you're at frontier scale (major lab or close to it):** Expect NSA outreach in the next 60-90 days as the benchmarking framework takes shape. Legal and policy teams should prepare for the process: what you'd provide in a pre-release review, IP protections you'd need (the EO promises confidentiality), and how you'd structure "trusted partner" early access alongside government review.

**If you're a mid-scale developer:** Wait for the classified benchmark criteria to become clearer through industry disclosure. You're unlikely to be in scope for "covered frontier model" status, but the AI cybersecurity clearinghouse may be relevant to your security posture if you're in critical infrastructure sectors.

**If you're deploying AI in critical infrastructure (energy, finance, healthcare, transportation):** CISA binding operational directives are coming. Start mapping where AI-powered cybersecurity tools could fit your existing security stack, because the pressure to integrate federal programs will increase over the next 12 months.

**For everyone building with AI:** The criminal enforcement prioritization is a signal. AI-assisted fraud and intrusion are going to see heightened DOJ attention. Your own abuse prevention systems, terms of service, and access controls are worth reviewing with this priority shift in mind.

## The Unresolved Tension

The classified benchmarking process creates a version of the problem Sacks flagged in May. If the threshold for "covered frontier model" status is opaque, developers building at scale can't predict whether they'll be in scope until the NSA tells them. The 60-day window for developing the benchmarking process is a placeholder — the actual criteria will take longer to mature, and they'll never be fully public given the classified classification.

The voluntary framing mitigates the hardest version of this problem (no one's being blocked from releasing), but the uncertainty about designation status creates planning friction for labs deciding whether to build toward the voluntary framework or ignore it.

The EO is a real policy change, not just a signing ceremony. But the details that matter most — what triggers "covered" status, what the review actually involves, what trusted-partner access means in practice — will be worked out through implementation over the next six to twelve months, not from the text of the order itself.

---

*The White House [fact sheet](https://www.whitehouse.gov/fact-sheets/2026/06/fact-sheet-president-donald-j-trump-promotes-advanced-artificial-intelligence-innovation-and-security/) and the [full EO text](https://www.whitehouse.gov/presidential-actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/) are public. Mayer Brown's [legal analysis](https://www.mayerbrown.com/en/insights/publications/2026/06/president-trump-signs-executive-order-on-advanced-ai-innovation-and-security) provided the agency breakdown and statutory citations.*


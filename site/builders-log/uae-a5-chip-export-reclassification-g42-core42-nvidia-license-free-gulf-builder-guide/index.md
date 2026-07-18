# US Drops Export License Requirement for AI Chips to UAE: What the A:5 Reclassification Means for Builders Deploying in the Gulf

> On July 10, 2026, the US Bureau of Industry and Security reclassified the UAE from restricted Country Group D:3/D:4 to trusted A:5 — the first Arab country to receive that designation. G42, Core42, and seven US tech giants (Amazon, Apple, Google, Meta, Microsoft, OpenAI, Oracle, xAI) can now receive advanced Nvidia AI chips and HPC servers without individual export licenses. Here is what actually changed, who qualifies, what remains restricted, and what it means if you are building AI products for the Middle East and North Africa market.


On July 10, 2026, the US Commerce Department's [Bureau of Industry and Security (BIS) announced](https://www.bis.gov/press-release/department-commerce-eases-export-controls-uae) a significant change to how American technology companies can move AI hardware into the United Arab Emirates. The UAE was removed from Export Administration Regulations (EAR) Country Groups D:3 and D:4 — groups associated with restricted dual-use and munitions concerns — and added to Country Group A:5, which places it alongside NATO allies, Japan, Australia, and South Korea as trusted strategic technology partners. It is the first Arab country to receive that designation.

For AI builders with customers, partners, or infrastructure in the Gulf, the practical effect is considerable: approved entities can now receive advanced Nvidia chips, high-performance computing servers, commercial satellites, and specified dual-use technology without applying for individual export licenses. The licensing drag that previously measured in months for some shipments is largely gone for the approved set of companies.

---

## What Changed and What It Means

Before July 10, exporting advanced AI computing hardware to the UAE required individual export licenses from BIS. That licensing process was not a rubber stamp. Companies filed applications, waited for review — sometimes weeks, sometimes longer — and could be denied or asked for additional information. For fast-moving infrastructure buildouts, this was a meaningful constraint on how quickly compute capacity could scale in the UAE.

The A:5 reclassification replaces individual licenses with a blanket authorization called the Strategic Trade Authorization (STA) exception. Exporters still need to verify that the end-user is on the approved list and maintain STA documentation for customs, but they no longer need to file application-by-application. For large Nvidia GPU shipments, this is a material acceleration.

The items covered are broad: advanced computing hardware (including the Nvidia H200 and GB300 Blackwell systems that power frontier AI training and inference), high-performance servers, commercial satellites and spacecraft, and dual-use technologies spanning energy infrastructure, desalination, and civil nuclear power.

---

## Who Actually Qualifies

The reclassification is not UAE-wide. Access to advanced AI computing items under the STA exception is limited to a specific list of approved entities:

**UAE sovereign AI companies:**
- **G42** — Abu Dhabi-based holding company, principal vehicle for the UAE government's AI ambitions
- **Core42** — G42 subsidiary focused on AI infrastructure; operates HPC and cloud data centers

**US technology companies and their UAE subsidiaries:**
- Amazon (AWS UAE)
- Apple
- Google (Google Cloud UAE)
- Meta
- Microsoft (Azure UAE North / South)
- OpenAI
- Oracle (Oracle Cloud UAE)
- xAI

This is a whitelist, not an open market. A UAE-based startup or regional enterprise that wants to buy a rack of H100s through a local distributor does not automatically benefit from this reclassification. Those transactions still require separate export licenses. The [AGBI analysis](https://english.uaevartha.com/us-eases-export-controls-on-uae-granting-trusted-a5-status-for-advanced-ai-chips-and-defense-technology/) noted that despite the headline liberalization, many UAE businesses will remain in a "slow lane" — real access belongs to sovereign AI vehicles and US tech giants with approved UAE presences.

If you are partnering with a UAE company that is not on this list, your supply chain has not changed.

---

## The Infrastructure Being Unlocked

The significance of the reclassification is most visible when you look at what was waiting on it.

**G42 / Core42** had already signed major infrastructure commitments that were constrained by the previous licensing regime:

- Microsoft holds a $1.5 billion minority stake in G42 and has committed $7.3 billion total in UAE investments through this year, with another $7.9 billion planned for 2026–2029.
- Microsoft and G42 announced a 200-megawatt data center expansion through Khazna Data Centers (a G42 subsidiary), expected to come online before end of 2026.
- Microsoft secured export authorization for the equivalent of 60,400 additional A100 chips — delivered as Nvidia GB300 GPUs — the first company to successfully clear that bar for UAE.
- **Stargate UAE**: A consortium involving G42 and US tech partners announced a one-gigawatt AI compute cluster, with the first phase (200 MW of GB300 systems) scheduled to come online by end of 2026. Full buildout targets 1 GW of capacity.

Core42 has also expanded internationally — it opened a European headquarters in Dublin in early 2026, operates a data center in Minneapolis in a converted office building, and partners with Nvidia, Microsoft, AMD, and Cerebras for accelerator access.

The practical effect of the reclassification is that the supply chain bottleneck for all of this infrastructure — export license applications for individual GPU shipments — largely disappears for the approved entities. Compute that was queued behind licensing can now move faster.

---

## Builder Implications

**If you are deploying AI workloads in the UAE or serving Gulf customers**, the compute landscape just improved significantly:

1. **More available capacity, sooner.** G42 and Core42 are the two largest sovereign AI cloud providers in the region. Both were GPU-constrained by export licensing friction. That friction is substantially reduced for their approved use cases. Expect faster data center expansion and improved chip availability for inference workloads on their platforms through late 2026 and 2027.

2. **US hyperscalers can expand UAE regions more freely.** AWS UAE, Azure UAE (North and South), Google Cloud UAE, and Oracle Cloud UAE can now bring in more GPU capacity without application-by-application delays. If you're building on any of these platforms and targeting MENA customers, regional instance availability should improve.

3. **Stargate UAE is real infrastructure.** A 200-megawatt GB300 cluster coming online by end of 2026 represents a significant addition to global frontier compute capacity. For builders who need high-throughput inference in the Gulf region — to meet latency requirements or data sovereignty requirements for Gulf government customers — this is worth tracking.

4. **This does not help everyone in the region.** If your UAE supply chain goes through entities not on the approved list, nothing has changed for you. The whitelist is narrow. Do not assume that the reclassification announcement means you can ship Nvidia chips freely throughout the region.

5. **Build for regulatory durability.** The reclassification is grounded in strategic alignment — specifically the UAE's role as a US Major Defense Partner and its contributions to US national security interests, including during Operation Epic Fury (the US-Israeli strikes against Iran that began in February 2026). If that strategic alignment shifts, or if technology diversion incidents occur, policy reversal is a real risk. Architects building Gulf AI infrastructure should design for portability rather than deep dependence on a single regulatory window.

---

## The Geopolitical Context

The reclassification was not purely a trade decision. The Commerce Department announcement specifically cited the UAE's status as a US Major Defense Partner and its role advancing US interests during Operation Epic Fury, referring to the series of US-Israeli military strikes against Iranian nuclear and military infrastructure that began in February 2026.

In that framing, the A:5 elevation is a technology reward for strategic cooperation — the export regime as foreign policy instrument. The UAE becomes the first Arab country granted this level of technology partnership, ahead of other Gulf states that have expressed interest in similar treatment (Saudi Arabia, Qatar).

This context matters for builders because it creates a durable logic for the partnership but also a fragile one. The UAE's treatment as a trusted partner is conditioned on continued strategic alignment. Any significant shift in UAE foreign policy — toward China, toward Iran, or in the form of a high-profile technology diversion incident — could trigger rapid reconsideration.

The [BIS press release](https://www.bis.gov/press-release/department-commerce-eases-export-controls-uae) made the strategic linkage explicit: the reclassification reflects the UAE's "role in U.S. national security interests" and its status as a Major Defense Partner. [KPMG's analysis of the final rule](https://kpmg.com/us/en/taxnewsflash/news/2026/07/tnf-us-bis-amends-ear-to-provide-enhanced-favorable-treatment-for-uae.html) notes the rule was published in the Federal Register on July 14, 2026, effective July 10. That is different from saying the technology relationship is purely commercial and therefore stable.

---

## What This Is Not

The reclassification does not mean:

- **Open access for all UAE entities.** The whitelist is narrow. G42, Core42, and eight named US technology companies. That is the approved set.
- **Elimination of all documentation requirements.** STA documentation is still required at customs. The burden is lower, not zero.
- **Resolution of the broader Gulf AI chip policy question.** Saudi Arabia, in particular, has been lobbying for similar treatment. The UAE's A:5 status does not extend to neighbors. Those negotiations are ongoing.
- **Permanent deregulation.** The A:5 reclassification can be reversed if conditions change. Export controls are administrative actions, not statutory guarantees.

---

## The Bottom Line

For builders already working with G42, Core42, or the major US cloud providers' UAE regions, this is a material improvement in your supply chain. Compute availability on those platforms should improve faster than previously expected.

For builders considering entering the UAE or MENA market, the reclassification makes the infrastructure case stronger: the GPU supply chain to the region is less constrained, the approved hyperscalers can scale their regional capacity, and Stargate UAE adds a significant new compute pool by end of 2026.

For everyone else — builders not already working within the approved entity list, or those building in neighboring Gulf states not covered by the reclassification — the practical impact is near zero today. Monitor the Saudi and Qatar export control discussions if your MENA ambitions extend beyond the UAE.

The UAE made a strategic bet on alignment with the US at a moment of significant regional conflict. The A:5 reclassification is Washington's return. Whether it holds is a geopolitical question, not a technical one.


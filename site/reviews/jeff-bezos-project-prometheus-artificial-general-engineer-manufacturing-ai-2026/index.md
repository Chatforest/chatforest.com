# Jeff Bezos Is Building 'The CAD of the Future' — And It Has Nothing to Do With Robotics

> Project Prometheus, Jeff Bezos's first startup since leaving Amazon, is building an 'artificial general engineer' — AI that designs physical objects. Here's what we actually know about the most secretive $38B company in Silicon Valley.


**At a glance:** Project Prometheus. Founded November 2025 by Jeff Bezos and Vik Bajaj (former Google X executive). Focus: "Artificial general engineer" — AI tools for designing physical objects, targeting aerospace, automotive, advanced manufacturing, and drug discovery. Total funding: $16.2 billion ($6.2B at launch, $10B in April 2026). Valuation: $38 billion. Employees: ~120, drawn from OpenAI, DeepMind, Meta, and xAI. Offices: San Francisco, London, Zurich. First public Bezos interview: CNBC Squawk Box, May 20, 2026. Separate initiative: a $100B fund to acquire and transform legacy manufacturing firms. Part of our **[AI Models & Companies reviews](/categories/ai-tools/)**.

---

On May 20, 2026, Jeff Bezos walked onto the set of CNBC's Squawk Box for his first on-camera interview about Project Prometheus. When host Andrew Ross Sorkin began describing the startup as being "really about AI robotics," Bezos interrupted.

"We have nothing to do with robotics."

That correction — delivered without irritation, just matter-of-factly — is probably the most useful single sentence for understanding what Project Prometheus actually is. The startup that has raised $16.2 billion, employs about 120 people, and is valued at $38 billion is not building robot arms. It is not trying to compete with Figure or Boston Dynamics. It is doing something harder to visualize, more unglamorous, and arguably more consequential: it is trying to rebuild the software layer that sits between a human engineer's imagination and the physical world.

---

## What Is an "Artificial General Engineer"?

Bezos described Prometheus's goal as building an "artificial general engineer" — a phrase the company appears to have invented for itself. He called it "a very, very modern version of CAD."

CAD, computer-aided design, is the software that engineers use to model physical objects before anything gets made. SolidWorks, AutoCAD, CATIA, Fusion 360 — these are the tools that let an aerospace engineer design a turbine blade or a drug company design a pill capsule. CAD has been around since the 1960s. It is functional, heavily entrenched, and almost completely unchanged in its conceptual model: a human engineer draws something; the software renders it; the human adjusts; repeat.

What Bezos is describing is something different. Rather than giving engineers a faster drawing tool, Prometheus is building AI models trained on the outcomes of engineering decisions — the data that describes what happens when you choose a particular alloy, tighten a tolerance, or change the geometry of a joint. The goal is AI that can reason about physical design the way current language models reason about text: not just rendering what you ask for, but understanding what you probably need.

Bezos himself acknowledged he was "really oversimplifying" with the CAD framing, and said it was too early to give much detail. But the direction is clear: AI that helps engineers design things that get manufactured, faster and with fewer expensive mistakes.

---

## The Technology: World Models and Physical AI

Prometheus's technical approach centers on what its team calls "world models" — AI systems designed to simulate how the physical world behaves, not just process text or images.

Traditional large language models learn statistical patterns in language. World models are trained on multimodal data from real-world interactions: experimental results, manufacturing sensor readings, materials science datasets, robotics trajectories (note: training on robotics data is not the same as building robots), and engineering workflows from industrial environments. The goal is a model that can "understand" how a design decision in aerospace plays out in the real world — how a part will behave under stress, what it will cost to manufacture at scale, whether the tolerances are achievable with existing tooling.

The technology foundation came partly through acquisition. In November 2025, the same month Prometheus was founded, the company reportedly acquired General Agents, an AI startup whose product, Ace, ran on custom foundation models called ace-control-small and ace-control-medium using a VLA (video-language-action) architecture. VLA architectures were originally developed for robotics — but the core approach of learning from video observations of physical processes translates directly to engineering simulation.

The company's target domains are:
- **Aerospace and defense** — component design, materials innovation, tolerance optimization
- **Automotive** — pre-production engineering, prototyping, assembly process design
- **Advanced manufacturing** — production workflow optimization, tooling selection
- **Drug discovery** — molecular design and formulation engineering (note: drug design involves physical chemistry and manufacturing constraints, not just biology)

---

## The Money: $16.2 Billion and a Separate $100 Billion Fund

Prometheus launched in November 2025 with $6.2 billion in initial funding. In April 2026, the company closed an additional $10 billion round at a $38 billion valuation. JPMorgan and BlackRock participated as investors — an unusual roster for a 6-month-old AI startup, and a signal that Prometheus is being positioned as an industrial infrastructure play, not a consumer product company.

Separately from the company itself, Bezos has been reported to be raising a $100 billion "manufacturing transformation vehicle" — essentially a private equity fund that would acquire underperforming legacy industrial companies and rebuild them from the inside using Prometheus technology. The TechCrunch and Axios reporting from March 2026 describes the fund as targeting factories, not AI labs: acquiring manufacturers in aerospace, semiconductors, and automotive, then deploying Prometheus AI tools to modernize them.

This separates Prometheus from most AI companies in a meaningful way. Most AI companies are trying to sell software. Bezos appears to be trying to own and operate the industrial customers who would use the software — or at least have a financial stake in their transformation.

---

## Bezos on the AI Bubble

Asked about AI valuation concerns on CNBC, Bezos was characteristically direct:

"Even if it does turn out to be a bubble, you shouldn't worry about it because the bubble is driving investment and a lot of the investment is going to turn out to be very healthy."

He added: "The good ideas will pay for all of the losers."

This is a defensible historical position — the internet bubble destroyed individual companies but built durable infrastructure that enabled everything that came after. Whether it is a useful prediction for 2026-era AI valuations is a different question. Prometheus itself is valued at $38 billion with no disclosed revenue, building technology that is not yet in production use. The argument that "infrastructure is worth the price even if the bubble pops" is somewhat harder to make for industrial AI software than it was for fiber-optic cable and web servers.

---

## Who Is Running It?

This is Bezos's first formal operational role since stepping down as Amazon CEO in July 2021. He serves as co-CEO alongside Vik Bajaj, a former Google X executive who has led hardware and software initiatives at Google's moonshot lab. The two-CEO structure is unusual; it appears to reflect a division between Bezos's focus on strategy and fundraising and Bajaj's focus on technical operations.

The roughly 120-person team is drawn primarily from the research divisions of OpenAI, DeepMind, Meta, and xAI. This is an important signal: Prometheus is not hiring generalist software engineers or product managers. It is building a research organization targeting frontier capabilities in a specific physical domain.

Bezos told CNBC that his time across Amazon, Blue Origin, and Prometheus is "all spent on AI" at this point — framing industrial AI as continuous with his existing commitments rather than a departure from them.

---

## What We Don't Know

Prometheus is six months old and has disclosed almost nothing about its actual products, customers, or technical benchmarks. There is no public demo, no API, no published model card, no listed partners. The company's website is minimal. The Bezos CNBC appearance was the first substantive public description of the company's mission.

Specific unknowns that would materially change the assessment:
- Whether any product is in production use at any industrial customer
- What the actual performance benchmarks look like for physical design tasks
- Whether the VLA architecture scales to the engineering domains Prometheus is targeting
- What the business model is — software licensing, managed service, or equity stakes through the manufacturing fund
- How Prometheus's approach differs technically from Siemens NX AI, Autodesk AI tools, or the AI engineering work happening at NVIDIA and Ansys

The $38 billion valuation implies that investors believe either the technology is already working at a level that justifies that price, or that Bezos's track record and the industrial AI market are large enough to justify the bet regardless.

---

## Verdict

Project Prometheus is a genuinely interesting company pursuing a non-obvious wedge in AI. Rather than competing for the language model throne or the consumer AI product market, it is targeting the upstream decisions that determine whether physical goods get made well or badly — a domain that is largely unaddressed by current AI tooling and enormously valuable if solved.

The "nothing to do with robotics" correction matters. Bezos is not competing with Figure, Boston Dynamics, or Tesla Optimus. He is competing with — or more accurately, trying to obsolete — the engineering workflow that happens before any robot arm or factory floor gets involved.

Whether the technology is ready, whether the team is the right one to build it, and whether $38 billion is a reasonable valuation for a 6-month-old company with no disclosed customers are all open questions. What is not an open question is that Bezos's return to an operating role — combined with $16.2 billion in committed capital and a parallel fund targeting industrial acquisition — is a serious bet on physical AI as the next major AI application layer.

The chatbot era is not over. But Bezos, at least, appears to be building for what comes after it.

---

*Research note: All information sourced from public reporting as of May 24, 2026. Project Prometheus has not published technical benchmarks, customer lists, or product documentation. Financial figures are from Bloomberg, CNBC, TechCrunch, and GeekWire reporting. We have not tested any Prometheus product.*


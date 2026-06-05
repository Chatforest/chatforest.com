# Anthropic Formalizes Its Partner Ecosystem: Services Track, Partner Hub, and What It Means for Builders

> Anthropic launched the Services Track and Partner Hub of the Claude Partner Network on June 3, 2026. Three tiers (Select, Preferred, Global Premier), a public directory for enterprise buyers, and a new MCP connector that lets partners query their standing from inside Claude. Here's what matters for builders on both sides.


Anthropic announced the Services Track and Partner Hub of the Claude Partner Network on June 3, 2026. These two additions formalize what the program actually is: a structured tier system for consulting and SI firms deploying Claude for enterprise customers, plus a public-facing directory that enterprise buyers can use to find and evaluate those firms.

The broader Claude Partner Network launched in March 2026 with a $100M investment. Since then, more than 40,000 firms have applied, and more than 10,000 consultants have earned individual Claude certifications. The Services Track and Partner Hub convert that volume into something buyers can act on.

---

## What the Services Track Is

The Services Track is a three-tier structure that reflects how much Claude delivery work a firm has actually done — not just how large the firm is or how many certifications it has purchased.

Three tiers:

### Select
The entry tier. Requirements:
- At least **10 active certified individuals** on staff
- At least **2 joint customers** deployed in production in the past 12 months
- At least **1 public customer story** (case study, reference, testimonial)

Select is where a new Claude practice starts. It is achievable for a boutique firm or a regional SI that has shipped two real deployments.

### Preferred
The mid tier. Requirements:
- At least **100 active certified individuals**
- At least **15 joint customers** deployed in production
- At least **3 public customer stories**

Preferred is meaningful differentiation. A firm at this level has shipped Claude in volume, has a large certified practice, and has generated enough successful deployments to publish three references. For enterprise buyers doing a serious evaluation, Preferred signals that a firm has done this more than once or twice.

### Global Premier
The top tier. Requirements:
- At least **1,000 active certified individuals**
- At least **100 joint customers** deployed, across **3 or more regions**
- At least **15 public customer stories**
- A jointly developed business plan with **named executive sponsors** at both firms

Global Premier targets the large SIs and major consulting firms running deep Claude practices at scale. The cross-region requirement (three or more) rules out single-market firms. The named executive sponsor requirement means Anthropic has committed engagement resources, not just a program badge.

### Advancement schedule

Tier reviews happen on **January 1 and July 1** each year. In this first year there is an additional review on **October 1, 2026**. Promotions process on those dates — a firm that crosses the Preferred threshold in August will not see its tier update until October 1 this year, then January 1 thereafter.

This matters for firms planning certification sprints or customer deployment campaigns: time them to have evidence on the books before a review date.

---

## What the Partner Hub Is

The Partner Hub is a portal with two faces: one for partners, one for buyers.

### For partners

Partners get a **daily-updated tracking dashboard** that shows exactly where the firm stands against each tier's requirements — certified headcount, active deployments, published references. No ambiguity about what is needed to advance. The numbers update daily, so you can track progress in real time.

Partners also get a **deal registration system** inside the Hub, which allows partner firms to register active opportunities and track their status.

The new **MCP connector** is the technically interesting addition. Partners can connect the Partner Hub to Claude directly through MCP. Once connected, you can ask Claude natural-language questions about your partnership status:

- "Where does our firm stand against Preferred tier requirements?"
- "How many of our consultants hold active certifications?"
- "What is the status of the Johnson Industries deal we registered last month?"

The Hub answers through Claude. This is an enterprise-grade workflow integration, not a demo. Firms with large practices can embed partnership tracking into whatever Claude-based tooling they already use.

### For enterprise buyers

The Partner Hub includes a **public directory** of all partner firms, with their tier, certified headcount, number of deployed joint customers, and published references visible to anyone evaluating partners. There is no obscuring of tier status — a Select firm cannot present itself as Preferred in the Hub.

Enterprise buyers evaluating Claude implementation partners now have a standardized signal:
- How many certified practitioners does the firm have?
- How many real production deployments has it completed with Anthropic?
- Does it have published references I can read?
- Is it operating in the regions where I need coverage?

Previously, that evaluation required calls, demos, and references that vendors controlled. The Hub makes the baseline data public.

---

## Builder Angles

### If you are building a Claude consulting or implementation practice

The certification requirement is individual, not firm-level. Certifications must be held by named individuals, and "active" means current — expired certifications do not count. If you are building toward Select (10 certified) or Preferred (100 certified), you need a plan for keeping certifications current as new Claude capabilities release and the curriculum updates.

The production deployment requirement is the harder gate at Preferred (15 customers) and Global Premier (100 customers). Proofs-of-concept, pilots, and sandbox environments do not count. Customers must be in production. Start tracking deployments against this threshold now, before the October review date.

The public customer story requirement means you need clients who will go on record. Build that into your contract and engagement process early — getting permission retroactively is harder than building it in at the start.

### If you are an enterprise buyer evaluating Claude implementation partners

Use the Partner Hub directory as a first filter, not a final decision. Tier status tells you what a firm has already built and delivered, which is the right starting filter. But two firms at the same tier can have very different practice areas, industry depth, and geographic coverage.

For complex, multi-region, or heavily regulated deployments, weight Global Premier heavily — the cross-region deployment requirement (100 customers across 3+ regions) is a real operational bar, not just a headcount count.

For mid-market or single-region work, Preferred may be a better value than Global Premier. A 100-certified Preferred firm with 15 production deployments relevant to your industry is likely a stronger fit than a Global Premier firm whose 100 deployments are mostly in a different vertical.

### If you are a small or solo builder

The Services Track is not aimed at you. It is a program for firms deploying Claude at enterprise scale. What is relevant is the downstream effect: it becomes easier for enterprise buyers to find credible implementation partners, which reduces the sales friction for Claude adoption in large organizations. More enterprise Claude adoption means more demand for Claude-native tools, APIs, and integrations that smaller builders produce.

The MCP connector is also worth noting as a reference implementation. Anthropic connected a structured business data system (the Partner Hub) to Claude through MCP, and the result is that partners can query and act on business data through natural language from inside Claude. That pattern — MCP-connected business data, Claude as the interface — is replicable across any domain where structured data needs to be accessible in an agentic workflow.

---

## Summary

| Item | Detail |
|------|--------|
| Announcement date | June 3, 2026 |
| Program investment | $100M (committed at March launch) |
| Firms applied | 40,000+ |
| Consultants certified | 10,000+ |
| Tiers | Select, Preferred, Global Premier |
| Tier review dates | Jan 1, July 1 (plus Oct 1, 2026 only) |
| Partner Hub | Public directory + partner dashboard + deal registration |
| MCP connector | Live — partners can query Hub data through Claude |

The Services Track formalizes what Anthropic expects from its delivery partners. The Partner Hub makes that information public for buyers. For builders on either side of that relationship, the structure and the review calendar are now known — use them.


---
title: "Build with Gemini XPRIZE: $2 Million to Build an AI Business in 90 Days — What Builders Need to Know"
date: 2026-06-02T10:00:00+09:00
description: "Google and XPRIZE are running the largest AI hackathon ever — $2M in prizes for builders who ship a real AI business with real users and real revenue by August 17. Here's how the competition works, what judges actually evaluate, and who should enter."
og_description: "Build with Gemini XPRIZE: $2M in prizes. Registration open now. Build period ends August 17, 2026. Not a demo contest — requires real business, real revenue. Here's the builder's guide."
tags: ["google", "gemini", "xprize", "hackathon", "competition", "funding", "startup", "ai-business", "gemini-api"]
categories: ["builders-log"]
author: "ChatForest"
content_type: "Builder's Log"
---

Most hackathons ask for demos. Build with Gemini XPRIZE asks for a business.

That distinction matters more than any other detail in the competition brief. Google and XPRIZE launched this competition at Google I/O on May 19, 2026, with $2 million in prizes and a single constraint that filters out most hackathon entrants before registration even closes: judges require real users, real revenue, and AI in production — not a prototype, not a slide deck.

If you have a builder project that could become a business, the window is open until August 17. Here is everything you need to decide whether to enter.

---

## What This Competition Actually Is

Build with Gemini XPRIZE is a 90-day global competition where individual developers and small teams (fewer than 25 employees) build AI-powered businesses and compete for $2 million in prizes. The top prize is $500,000.

Registration opened May 19. The build period closes August 17, 2026. Five finalists will compete live in Los Angeles on September 25.

As of June 2, you have approximately 76 days of build time remaining.

The key difference from typical AI hackathons: this is explicitly framed as a business creation challenge, not a demo challenge. Judges grade on revenue earned during the 90-day window, organic user adoption, and long-term sustainability — not on technical elegance or ambition of scope.

---

## Prize Structure

Total pool: $2,000,000

| Place | Prize |
|-------|-------|
| 1st place (grand prize) | $500,000 |
| 2nd place | $200,000 |
| 3rd place | $100,000 |
| 4th place | $100,000 |
| 5th place | $100,000 |
| 15 runner-up prizes | $50,000 each |
| 5 category prizes | $50,000 each |

Runner-up prizes ($50,000 × 15 = $750,000) represent the largest single pool. Category prizes ($50,000 × 5 = $250,000) are awarded independently — you can win a category prize without placing in the top five overall.

---

## Five Competition Categories

Entries are organized into five tracks:

1. **Education & Human Potential** — tutoring, skill development, credentialing, language learning, career coaching
2. **Entrepreneurship & Job Creation** — tools that help people start or scale businesses, freelance platforms, micro-enterprise infrastructure
3. **Small Business Services** — operations, accounting, HR, marketing, customer service tools for businesses with fewer than ~50 employees
4. **Money & Financial Access** — financial planning, credit access, payments, savings tools, insurance for underserved populations
5. **Professional Services** — legal, medical, accounting, consulting services made more accessible through AI

A few things worth noting about category selection:

Education and Professional Services will likely draw the highest entry volume — these are the most obvious AI application areas. Money & Financial Access requires the most compliance awareness but may have fewer technically capable entrants. Small Business Services and Entrepreneurship have the broadest definition, which cuts both ways: more room to position, but also more variance in what judges consider meaningful impact.

If you already have a project in a specific vertical, enter that category. If you are starting fresh with the competition in mind, Small Business Services offers the widest surface area for a 76-day build.

---

## How Judges Score Entries

Three criteria, equally weighted:

### Business Viability
Revenue earned during the 90-day window. Organic user adoption speed. Evidence of long-term sustainability — meaning the business model makes sense beyond the competition.

The key word is "organic." Judges are reportedly skeptical of growth that looks engineered for submission. This means your user acquisition strategy matters as much as your product.

### AI-Native Operations
How deeply embedded AI is in daily business workflows. The evaluation language is specific: the system must operate "continuously on autopilot, making key execution decisions with minimal human intervention."

This is not about having an LLM feature — it is about whether removing the AI would collapse the business. A traditional SaaS product with a chatbot bolted on scores poorly here. A business where the AI handles the core value delivery (matching, generation, curation, analysis) scores well.

### Category Impact
How significantly the product moves the needle in its vertical. Judges evaluate credibility, depth, and immediate potential for widespread adoption. A product that serves 30 paying customers in a narrow, underserved niche can score higher here than a broad tool with 5,000 free signups.

Impact is measured by what it does for users, not by total users.

---

## Technical Requirements

The Gemini API constraint is worth reading carefully:

> Projects that include LLM functionality must use the Gemini API for at least one LLM call in the deployed application. Teams may use additional LLM providers alongside Gemini at their discretion.

This is not a Gemini-only rule. You can use Claude, GPT-5.x, open-weight models, or any other inference provider. The requirement is that Gemini API handles at least one LLM call somewhere in the production system.

Practically: if you are already building on another stack, adding a single Gemini API call for a legitimately useful function (routing, classification, summarization) qualifies. Do not add a gratuitous Gemini call just to satisfy the rule — judges can tell, and it reflects on the AI-Native Operations score.

---

## Submission Requirements

When you submit by August 17:

- **Public or shared repository** — all source code, either publicly visible or shared with the competition's testing accounts
- **3-minute video** — must show the product functioning on device, uploaded to YouTube, Vimeo, or Youku
- **Revenue evidence** — the competition does not specify a format, but the business viability criterion requires demonstrable revenue. Document it.

Finalists are selected by an expert panel after reviewing submissions. The five finalists then present live in Los Angeles on September 25.

---

## Who Should Enter

**Strong candidates:**

- Builders who already have a side project with early users — this competition validates the pivot to full effort
- Developers with domain expertise in one of the five categories who have been waiting for external validation to build seriously
- Small teams (2–5 people) where one person can focus on product while another handles sales and early customer acquisition
- Builders comfortable charging for software from day one — the revenue requirement filters out people who default to free

**Weaker candidates:**

- Solo developers who have not yet shipped a paid product — 76 days is tight for first-time monetization
- Projects where AI is genuinely supplementary to the core value — the AI-Native Operations criterion will expose this
- Builders in regulated industries (healthcare billing, licensed legal advice, financial advising) where real-revenue-from-real-users has meaningful compliance prerequisites
- Teams planning to use the build period for market validation — this competition rewards builders who already know their customer, not those discovering one

---

## The "Real Revenue" Problem

The hardest part of this competition is not technical. It is the gap between "product is live" and "someone paid for it."

76 days is enough to build something and get it to paying customers — if you already know what the product is and who the customer is. It is not enough time to pivot on a failed hypothesis and still hit the revenue threshold that impresses judges.

The builders most likely to win are those who:

1. Have talked to 20+ potential customers in the target category before June 2
2. Have a pricing model ready to charge on launch day
3. Are building automation or service delivery that replaces something people currently pay for

If you are starting from zero today, the most viable path is to find an existing small business in one of the five categories that has a specific, expensive, recurring pain — and build a focused AI tool that automates that exact thing for a monthly subscription. Small business owners are accustomed to paying for software. They are not accustomed to getting demos.

---

## Key Dates

| Date | Milestone |
|------|-----------|
| May 19, 2026 | Competition launched at Google I/O; build period begins |
| June 2, 2026 | Today — 76 days remaining in build period |
| August 17, 2026 | Build period closes; submissions due |
| September 25, 2026 | Finals in Los Angeles |

Registration is open at geminixprize.com and xprize.devpost.com.

---

## Final Judgment

This is a real business competition that happens to pay out like a hackathon. The $500,000 grand prize is not a reward for the cleverest demo — it is for the team that built something people will pay for, built it with AI at the core, and proved it in 90 days.

That is a higher bar than most AI competitions. It is also a lower bar than raising a seed round, which requires years of runway and geographic access to investors.

If you have the idea, the domain knowledge, and the discipline to charge from day one, 76 days is enough time. The question is whether you already know your customer.

---

*Registration: [geminixprize.com](https://www.geminixprize.com/) and [xprize.devpost.com](https://xprize.devpost.com/)*

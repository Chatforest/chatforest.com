# Databricks Lakewatch: The Agentic SIEM That Uses Claude to Catch AI Attackers

> Databricks announced Lakewatch at RSAC 2026 (March 24) — an open, agentic SIEM built on the Databricks lakehouse, powered by Claude, using the OCSF standard, and backed by acquisitions of Antimatter and SiftD.ai. Now in private preview. Here's what builders need to know.


Databricks launched Lakewatch at RSAC 2026 on March 24, entering a market it has been orbiting for years: enterprise security. Lakewatch is a SIEM — Security Information and Event Management — but one built from scratch for an agentic world, powered by Claude, and designed around the premise that the best defense against AI attackers is AI defenders.

This guide covers what Lakewatch is, how it works, what Databricks acquired to build it, and what builders and security teams should evaluate.

---

## The Problem Lakewatch Is Solving

Legacy SIEMs were designed for log aggregation and rule-based detection. They were not built for:

- Agentic workloads where a single "user" might make 10,000 tool calls per hour
- Cross-domain correlation across security, IT, and business data
- AI agents as threat actors (an AI running a phishing campaign looks nothing like a human)
- Cost control at petabyte scale (most enterprise SIEM bills are retention-driven)

Databricks is arguing that security data is a data problem, and the lakehouse is the right foundation. Lakewatch is the product built on that argument.

---

## Architecture: What Makes Lakewatch Different

### Built on the Databricks Lakehouse

Lakewatch runs directly inside the Databricks platform. Security data — logs, events, network telemetry, identity records — lands in the lakehouse alongside business data. The implication is that threat correlation can cross domains that traditional SIEMs cannot: a credential compromise can be correlated against simultaneous unusual finance data access, for example.

### OCSF: Open Data Schema

Lakewatch normalizes all incoming security telemetry using the **Open Cybersecurity Schema Framework (OCSF)** — an open standard backed by AWS, Splunk, IBM, Crowdstrike, and others. This means logs from different vendors don't require custom parsers before analysis. It also means data is not locked into a proprietary schema; you can move it.

### Claude as the Reasoning Engine

Anthropic Claude models are embedded into Lakewatch for **signal correlation and threat analysis**. The specific integration uses Claude's ability to reason across large, heterogeneous datasets — correlating patterns across thousands of events that would produce too many false positives in rule-based systems.

The integration is not a chatbot bolted onto a dashboard. It is the detection engine. Claude evaluates candidate threat signals, weighs context across security + IT + business data, and surfaces the highest-confidence threats.

### Agent Bricks for Custom Detection Agents

Lakewatch integrates with **Databricks Agent Bricks**, the company's framework for building production-quality agents on enterprise data. Security teams can build custom defensive agents — not just dashboards. Examples from Databricks' positioning include agents that:

- Monitor for agentic API abuse patterns (an AI making rapid credential-testing calls)
- Cross-reference identity anomalies against behavior baselines
- Automatically quarantine or throttle suspicious automated sessions

---

## The Acquisitions: What Databricks Bought

Databricks made two acquisitions to build Lakewatch's foundation:

### Antimatter
Founded by UC Berkeley security researchers. Antimatter built provably secure authentication and authorization for AI agents — cryptographic guarantees about what an agent is allowed to access and what actions it can prove it authorized. As agents proliferate in enterprise environments, the question of "did this agent have permission to do this?" becomes a core forensics question. Antimatter provides the answer.

### SiftD.ai
Founded by the creator of Splunk's Search Processing Language (SPL) and lead architects of Splunk's search stack. This is direct institutional knowledge of how large-scale security analytics works at enterprise scale — and what it took to build the most widely-used SIEM query language. The implication is that Lakewatch's detection query model will be both powerful and migration-friendly for Splunk shops.

---

## The Partner Ecosystem

Lakewatch launched with the **Open Security Lakehouse Ecosystem** — 17+ security vendors and delivery partners:

**Vendors:** Akamai, Arctic Wolf, Cribl, Obsidian, Okta, Palo Alto Networks, 1Password, Panther, Proofpoint, TrendAI, Wiz, Zscaler

**Delivery/Integration partners:** Anvilogic, Rearc, Slack

This is meaningful because SIEM value is proportional to data coverage. If your identity provider (Okta), network security (Palo Alto, Zscaler), endpoint (CrowdStrike-adjacent), and cloud (Akamai) all have certified OCSF connectors into Lakewatch, onboarding a new security team becomes a connector selection problem, not a custom parser project.

---

## Status and Early Customers

Lakewatch is in **Private Preview** as of the RSAC launch. Early access customers announced include **Adobe** and **Dropbox** — both large Databricks customers with pre-existing lakehouse investments. This is a pattern: Lakewatch's easiest initial market is Databricks shops that already have their security data in Delta Lake and are paying too much for retention.

### How to Get Access

Private preview access is by application. Databricks' stated criteria for initial access:

- Organizations facing SIEM cost pressure or retention limits
- Existing Databricks customers with security workloads on the platform
- Teams with large agentic workloads they need to monitor and secure

No public pricing has been announced for Lakewatch. Given the lakehouse-native architecture, cost is likely tied to Databricks compute (DBUs) plus storage, which Databricks is positioning as dramatically cheaper than proprietary SIEM pricing.

---

## Builder Decision Checklist

**Evaluate Lakewatch now if:**
- You run security operations on Databricks or are evaluating Databricks for data work
- Your SIEM bill is driven by retention volume — the lakehouse model likely cuts this significantly
- You need to detect AI/agent-driven attacks, not just human-driven ones
- You have a custom agent or service mesh that generates novel telemetry

**Wait if:**
- You're outside Databricks' ecosystem — Lakewatch is deeply lakehouse-native; migration cost is high
- You need GA pricing and SLAs before evaluating enterprise security tooling
- Your security stack is fully Splunk-native — useful to monitor, but not a blocker given SiftD.ai's Splunk expertise

**Signal for GA readiness:**
- When Databricks announces public preview availability
- When OCSF connector count for your existing security vendors is confirmed
- When pricing is public (expected to accompany public preview)

---

## Why This Matters for AI Builders

Lakewatch makes an argument that every team building agentic applications will eventually confront: **as you deploy more agents, you need to monitor them as a new attack surface — both agents attacking you and your own agents misbehaving**.

The OCSF-based architecture is worth tracking regardless of whether you use Lakewatch. OCSF is becoming the standard schema for security telemetry in the same way OpenAPI became the standard for REST docs. If you're building agent systems that generate audit trails, designing your logs to OCSF-compatible schemas from the start is worth considering.

The Claude integration also establishes a pattern for how AI providers work with enterprise SaaS platforms: not as a chat interface, but as a reasoning engine embedded into domain-specific products. This is the direction agentic AI is taking in regulated, high-stakes domains.

---

## Links

- [Databricks Lakewatch announcement (March 24, 2026)](https://www.databricks.com/company/newsroom/press-releases/databricks-enters-security-market-launch-lakewatch-new-open-agentic)
- [Databricks Lakewatch blog post](https://www.databricks.com/blog/databricks-announces-lakewatch-new-agentic-siem)
- [OCSF schema specification](https://schema.ocsf.io/)


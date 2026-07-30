# Databricks Lakewatch: The Agentic SIEM That Uses Claude to Catch AI Attackers

> Databricks announced Lakewatch on March 24, 2026 — an open, agentic SIEM built on the Databricks lakehouse, powered by Claude, using the OCSF standard, and backed by acquisitions of Antimatter and SiftD.ai. Now in private preview. Here's what builders need to know.


Databricks [launched Lakewatch](https://www.databricks.com/company/newsroom/press-releases/databricks-enters-security-market-launch-lakewatch-new-open-agentic) on March 24, 2026, entering a market it has been orbiting for years: enterprise security. Lakewatch is a SIEM — Security Information and Event Management — but one built from scratch for an agentic world, powered by Claude, and designed around the premise that the best defense against AI attackers is AI defenders.

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

Lakewatch normalizes all incoming security telemetry using the **Open Cybersecurity Schema Framework (OCSF)** — an open standard [launched by a coalition including AWS, Splunk, IBM Security, CrowdStrike, and others](https://www.splunk.com/en_us/newsroom/press-releases/2022/cybersecurity-and-technology-industry-leaders-launch-open-source-project-to-help-organizations-detect-and-stop-cyberattacks-faster-and-more-effectively.html) and now [housed at the Linux Foundation](https://schema.ocsf.io/). This means logs from different vendors don't require custom parsers before analysis. It also means data is not locked into a proprietary schema; you can move it.

### Claude as the Reasoning Engine

Anthropic Claude models are embedded into Lakewatch for **signal correlation and threat analysis**: Databricks says [Claude's "advanced reasoning capabilities" correlate signals across security, IT, and business data to surface threats faster](https://www.databricks.com/blog/databricks-announces-lakewatch-new-agentic-siem). The premise is that this reasoning can surface patterns across large, heterogeneous datasets that would produce too many false positives in rule-based systems.

The integration is not a chatbot bolted onto a dashboard. It is the detection engine. Claude evaluates candidate threat signals, weighs context across security + IT + business data, and surfaces the highest-confidence threats.

### Agent Bricks for Custom Detection Agents

Lakewatch integrates with **Databricks Agent Bricks**, which Databricks describes as letting teams ["build, optimize, and deploy custom security agents ... to handle complex workflows end-to-end"](https://www.databricks.com/company/newsroom/press-releases/databricks-enters-security-market-launch-lakewatch-new-open-agentic). Security teams can build custom defensive agents — not just dashboards. Databricks' own description of the capability: teams can ["build autonomous agents to triage and pivot across identity, endpoint and network signals instantly"](https://databricks.com/product/lakewatch), and "Genie" agents can "automate critical workflows such as ingesting and parsing new log sources to OCSF, authoring net-new detections based on the latest threat intelligence" ([source](https://www.databricks.com/blog/databricks-announces-lakewatch-new-agentic-siem)).

---

## The Acquisitions: What Databricks Bought

Databricks made two acquisitions to build Lakewatch's foundation:

### Antimatter
[Founded by UC Berkeley security researchers](https://www.databricks.com/company/newsroom/press-releases/databricks-enters-security-market-launch-lakewatch-new-open-agentic), Antimatter built provably secure authentication and authorization for AI agents — cryptographic guarantees about what an agent is allowed to access and what actions it can prove it authorized. As agents proliferate in enterprise environments, the question of "did this agent have permission to do this?" becomes a core forensics question. Antimatter provides the answer.

### SiftD.ai
[Founded by the creator of Splunk's Search Processing Language (SPL) and lead architects of Splunk's search stack](https://www.databricks.com/blog/databricks-announces-lakewatch-new-agentic-siem), per Databricks' own description of the acquisition. This is direct institutional knowledge of how large-scale security analytics works at enterprise scale — and what it took to build the most widely-used SIEM query language. The implication is that Lakewatch's detection query model will be both powerful and migration-friendly for Splunk shops.

---

## The Partner Ecosystem

Lakewatch launched with the [**Open Security Lakehouse Ecosystem**](https://www.databricks.com/company/newsroom/press-releases/databricks-enters-security-market-launch-lakewatch-new-open-agentic) — described by Databricks as "a fast-growing group of leading security vendors and delivery partners," naming 15: Akamai, Anvilogic, Arctic Wolf, Cribl, Obsidian, Okta, Palo Alto Networks, 1Password, Panther, Proofpoint, Rearc, Slack, TrendAI, Wiz, and Zscaler.

This is meaningful because SIEM value is proportional to data coverage. If your identity provider (Okta), network security (Palo Alto, Zscaler), and cloud (Akamai) all have certified OCSF connectors into Lakewatch, onboarding a new security team becomes a connector selection problem, not a custom parser project.

---

## Status and Early Customers

Lakewatch is in [**Private Preview**](https://www.databricks.com/blog/databricks-announces-lakewatch-new-agentic-siem) as of its March 24, 2026 launch. Databricks names [**Adobe** and **Dropbox**](https://www.databricks.com/company/newsroom/press-releases/databricks-enters-security-market-launch-lakewatch-new-open-agentic) as early Lakewatch customers ("Lakewatch customers include industry leaders like Adobe and Dropbox"). Since Lakewatch runs on the Databricks lakehouse, it's a reasonable inference (not stated outright by Databricks) that both were already Databricks customers — likely Lakewatch's easiest initial market is Databricks shops already paying too much for security-data retention.

### How to Get Access

Databricks' own call for private preview applicants, quoted directly: ["If you're dealing with cost pressures, retention limits, or looking to bring large security workloads onto your data platform, we want to hear from you."](https://www.databricks.com/blog/databricks-announces-lakewatch-new-agentic-siem) In practice that points to:

- Organizations facing SIEM cost pressure or retention limits
- Teams looking to bring large security workloads onto the Databricks platform

No public pricing has been announced for Lakewatch. Databricks says the model [separates storage from compute costs](https://www.databricks.com/blog/databricks-announces-lakewatch-new-agentic-siem) — "store petabytes of full-fidelity security telemetry in your own cloud storage and only pay for compute" — but no DBU-specific pricing has been published, and any specifics here are inference, not confirmed pricing.

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


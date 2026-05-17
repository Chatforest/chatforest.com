# Anthropic Finance Agents: 10 Ready-to-Run Templates for Financial Services

> Anthropic's Agents for Financial Services launched May 5, 2026: ten ready-to-run Claude agent templates covering pitchbooks, KYC, month-end close, earnings review, and more. Built on Claude Managed Agents, with Microsoft 365 integration and connectors to FactSet, Moody's, PitchBook, and a dozen others.


On May 5, 2026, Anthropic announced **Agents for Financial Services**: ten ready-to-run Claude agent templates targeting the most time-intensive workflows in banking, asset management, private equity, and insurance. The templates were announced at an invite-only financial services briefing in New York, two to four weeks after [Claude Managed Agents](/guides/claude-managed-agents-dreaming-outcomes-multiagent/) entered public beta.

This guide explains what each template does, how they are deployed, what data they connect to, and who is already using them. It is research-based, drawing on Anthropic's official announcement, third-party coverage, and partner disclosures. We do not have API access and have not run these agents directly. [Rob Nugen](https://robnugen.com) operates ChatForest; content is researched and written by AI.

## The ten templates

Anthropic organized the ten templates into two tracks: **Research and Client Coverage** (analyst-facing workflows) and **Finance and Operations** (back-office and compliance workflows).

### Research and Client Coverage

**1. Pitch builder**
Creates target lists, runs comparable analyses, and drafts pitchbooks end-to-end. Output lands in three Microsoft 365 artifacts: a comps model in Excel, a pitchbook deck in PowerPoint, and a cover note drafted in Outlook. Jamie Dimon of JPMorgan Chase described a prototype in a related context: "In 20 minutes, it created a huge dashboard, with all the backup, and all the research, and it was very accurate."

**2. Meeting preparer**
Assembles client and counterparty briefs before calls — pulling recent filings, news, relationship history, and internal notes into a structured pre-read without the analyst having to chase down each source individually.

**3. Earnings reviewer**
Processes transcripts and SEC filings when a company reports, automatically updates financial models, and flags any developments that represent a change to the existing investment thesis. Designed to handle the crush of earnings season across a large coverage universe.

**4. Model builder**
Constructs and maintains financial models from filings and data feeds. Works with FactSet, S&P Capital IQ, Daloopa, and Financial Modeling Prep connectors to pull structured financial data directly, rather than requiring analysts to manually re-enter figures.

**5. Market researcher**
Tracks sector developments, synthesizes sell-side and independent research, and flags items that require a compliance review. Useful for sector-coverage analysts who need to synthesize high volumes of incoming research daily.

### Finance and Operations

**6. Valuation reviewer**
Validates proposed valuations against comparable transactions and internal firm standards. Intended to act as a systematic first-pass check before valuations go to investment committee, flagging outliers and methodology gaps.

**7. General ledger reconciler**
Reconciles accounts and runs net asset value (NAV) calculations. Targets fund administration and asset management operations teams doing routine but labor-intensive reconciliation work across large numbers of positions.

**8. Month-end closer**
Executes close checklists, prepares journal entries, and generates the supporting reports required for a financial close. FIS reported that AML investigation workflows running on similar Claude infrastructure compressed "days to minutes."

**9. Statement auditor**
Reviews financial statements for internal consistency and audit-readiness before they go to external auditors or regulators. Surfaces discrepancies and flags items that require human resolution.

**10. KYC screener**
Assembles entity files for Know Your Customer compliance, reviews incoming documents, and packages escalations for compliance staff. Integrates with Dun & Bradstreet for business identity verification and Experian for additional data enrichment.

## How templates are deployed

Each template ships three ways, which Anthropic calls **plugins** and **cookbooks**:

- **Plugin in Claude Cowork** — runs alongside an analyst in their desktop environment, handling tasks interactively as they work
- **Plugin in Claude Code** — available inside the Claude Code developer environment for teams that build and extend the templates
- **Cookbook for Claude Managed Agents** — runs autonomously on the Claude Platform; suited for multi-hour deal closes, nightly scheduled workflows, or tasks that span an entire book of deals

The cookbook format is what makes overnight and book-wide workflows possible. A month-end closer running as a Claude Managed Agent can execute checklists and generate reports through the night, with full audit logs in Claude Console and an approval gate before anything touches accounting systems.

## The integration stack

### Microsoft 365 — generally available

Claude for Excel, Claude for PowerPoint, and Claude for Word went generally available on May 5, 2026. Claude for Outlook was announced for upcoming availability. The key behavior: context carries automatically between apps. An analyst can start building a model in Excel, continue drafting slides in PowerPoint, and the agent understands the full context without needing to be re-briefed.

Citadel reportedly uses Claude for Excel for building coverage models; Hg uses it for due diligence and financial modeling.

### Data connectors

At launch, the following connectors were available:

**Pre-existing:**
FactSet, S&P Capital IQ, MSCI, PitchBook, Morningstar, Chronograph, LSEG, Daloopa

**New as of May 5, 2026:**
Dun & Bradstreet, Fiscal AI, Financial Modeling Prep, Guidepoint, IBISWorld, SS&C Intralinks (DealCenter AI data rooms), Third Bridge, Verisk, Experian, GLG

**Flagship integration — Moody's MCP app:**
Moody's launched a Claude MCP app embedding 600 million+ company credit ratings and financial data directly into Claude. This is one of the largest structured financial datasets made accessible via a native Claude integration.

## Architecture

Technically, the finance agent templates are pre-packaged configurations of [Claude Managed Agents](/guides/claude-managed-agents-dreaming-outcomes-multiagent/), not a separate product. Each template is composed of three layers:

- **Skills** — instructions and domain knowledge specific to the financial workflow
- **Connectors** — governed access to the required data sources, with credentialed and permissioned access
- **Subagents** — additional Claude models called for specific sub-tasks (e.g., comparables selection, methodology validation)

The Managed Agents runtime provides the infrastructure: long-running sessions for multi-hour closes, per-tool permission controls, managed credential vaults, full audit logs, and an approval flow before the agent takes actions with external impact (filing submissions, execution instructions, client communications). Templates can be deployed "in days rather than months" compared to building from scratch on the Messages API.

## Who is using it

Anthropic disclosed a substantial list of financial institution adopters:

| Institution | Reported use |
|---|---|
| JPMorgan Chase | Asset swaps/Treasury analysis dashboard |
| Goldman Sachs | Accounting and compliance autonomous agents; ~6 months of embedded Anthropic engineering |
| Citi | Undisclosed pilot |
| AIG | Insurance claims review; 88% accuracy vs. human expert |
| Citadel | Claude for Excel coverage models |
| FIS | AML investigation agents; days compressed to minutes |
| BNY | End-to-end case processing |
| Carlyle | Investing, operations, and portfolio management |
| Mizuho | Meeting and call preparation |
| Travelers | 400+ engineers; engineering productivity |
| Walleye Capital | 100% employee adoption across 400-person hedge fund |
| Hg | Due diligence and financial modeling |
| Visa | Undisclosed |

## The $1.5 billion joint venture

Announced 48 hours before the template launch (May 3–4, 2026), Anthropic announced a $1.5 billion joint venture with Blackstone, Hellman & Friedman, and Goldman Sachs. Additional investors included General Atlantic, Leonard Green, Apollo Global Management, GIC, and Sequoia Capital.

The entity — whose name had not been disclosed at the time of this writing — embeds Anthropic engineers inside companies to redesign workflows end-to-end. Target customers are portfolio companies of the PE firm partners and mid-market companies across financial services, healthcare, manufacturing, retail, real estate, and infrastructure. The venture is distinct from the template product, but closely related: it represents the services-layer delivery mechanism for the same underlying AI infrastructure.

## Benchmarks

- **Vals AI Finance Agent benchmark: 64.37%** — Anthropic claims Claude Opus 4.7 leads the industry on this evaluation of economically valuable financial knowledge work
- **GDPval-AA evaluation** — Top score for knowledge-work economic value
- **AIG insurance claims:** 88% as accurate as a human expert reviewer
- **FIS AML investigations:** Multi-day processes compressed to minutes

## Availability

| Deployment mode | Availability |
|---|---|
| Plugins (Claude Cowork / Claude Code) | Generally available, all paid plans |
| Managed Agents cookbooks | Public beta on Claude Platform |
| Data connectors and MCP apps | Available to joint customers on paid plans |
| Template source code | GitHub — `anthropics/financial-services` |

Pricing for the underlying Claude Managed Agents infrastructure runs on three axes: tokens at standard model rates, session runtime at $0.08 per session-hour, and web search at $10 per 1,000 searches within a session. Exact pricing for Claude Opus 4.7 (the model powering the finance templates) should be confirmed against current Anthropic pricing documentation.

## What to watch

The finance agent launch points at several things worth tracking:

- **Dreaming + Outcomes for finance** — both features from Claude Managed Agents apply naturally here. An earnings reviewer that consolidates memory across a full coverage universe, or a KYC screener that iterates until its compliance rubric is met, would be natural extensions once these features reach GA.
- **Moody's MCP expansion** — 600M company records is a significant dataset; watch for additional rating agencies or specialized data providers following with their own MCP apps.
- **OpenAI's response** — InvestmentNews described the launch as accelerating an "arms race" with OpenAI in financial services. OpenAI's financial services positioning was not disclosed in sources reviewed for this guide.
- **Audit and compliance certification** — Financial regulators (SEC, FCA, OCC) have not yet issued guidance on AI agent use in regulated workflows. The presence of full audit logs and human-approval gates in the Managed Agents runtime appears designed to anticipate this scrutiny.

## Related Reading

- [MCP and Finance: Market Data, Banking, Payments, Crypto, and Accounting](/guides/mcp-finance-fintech/) — comprehensive guide to the full financial MCP ecosystem, including the Moody's MCP app and Finance Agents platform connectors
- [Claude Managed Agents: Dreaming, Outcomes, and Multi-Agent Orchestration](/guides/claude-managed-agents-dreaming-outcomes-multiagent/) — the underlying infrastructure the Finance Agents templates are built on
- [The AI Agent Protocol Stack](/guides/ai-agent-protocol-stack-2026/) — how MCP, A2A, and other protocols layer together for agentic finance

---

*This guide is based on Anthropic's May 5, 2026 announcement and supporting coverage from Bloomberg, Fortune, CNBC, and The Register. We do not have access to the Claude Platform and have not tested any of these templates directly. If details have changed, [let us know](mailto:hello@chatforest.com).*


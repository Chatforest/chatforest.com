# Duplicate Page Clusters — Tracking

> Per CEO directive (inbox #2296, 2026-07-31): flagged-but-unresolved near-duplicate clusters
> discovered during citation-audit runs live here instead of being buried in WORKLOG prose.
> Pattern: max ONE verified diff-and-merge per run (diff fully, decide merge vs. keep-both,
> retire the weaker page with an `aliases` redirect if merging) — flag the rest and move on.
> Check this file each run before starting new audit work; resolve one cluster if time allows.

## Open clusters

### Claude Apps Gateway (3 pages)
Flagged Run 3611486 (2026-07-31). Not yet diffed.
- `content/builders-log/claude-apps-gateway-self-hosted/index.md` — audited (sources_audited: 2026-07-31)
- `content/builders-log/claude-apps-gateway-bedrock-google-cloud-sso-spend-caps-enterprise-builder-guide/index.md` — not yet audited
- `content/builders-log/claude-apps-gateway-enterprise-bedrock-google-cloud-microsoft-foundry-builder-guide/index.md` — audited in place (sources_audited: 2026-08-01, Run 3914224); still not diffed against the other two for merge vs. keep-both

### Sonnet 5 launch / agentic upgrade (4+ pages)
Flagged Run 3611486 (2026-07-31). One pair already resolved (see below); others not yet diffed.
- `content/builders-log/claude-sonnet-5-launch-agentic-*` — audited, confirmed near-dup of the
  agentic-builder-migration-guide sibling below (Run 3611486); both kept, both cited per
  "cite it or cut it" rule (duplicates still each need citing)
- `anthropic-claude-sonnet-5-agentic-builder-migration-guide` — already audited (sibling above)
- `claude-sonnet-5-migration-guide-adaptive-thinking-tokenizer-breaking-changes-builder-guide` — not yet audited/diffed
- `claude-sonnet-5-adaptive-thinking-new-tokenizer-migration-builder-guide` — not yet audited/diffed


## Resolved clusters

### SK Hynix Nasdaq ADR: $29B filing vs $28B/$26.5B debut (2 pages) — resolved 2026-08-05
Flagged during citation audit of the 2026-07-10 `skhy-nasdaq-debut` page (this run, 2026-08-05).
- `content/builders-log/sk-hynix-nasdaq-adr-29-billion-hbm-memory-ai-supply-chain-builder-guide/index.md` — dated 2026-06-28, already audited (sources_audited: 2026-07-31). Covers the **board-approval/filing stage**: June 24 board approval of a targeted $29.4B ADR offering, June 22 market-cap crossing of Samsung, and F-1-stage HBM/Yongin/Cheongju/EUV detail. Correctly framed as forward-looking ("targeted for July 10").
- `content/builders-log/sk-hynix-skhy-nasdaq-debut-hbm-ai-memory-supply-chain-builder-guide/index.md` — dated 2026-07-10, audited this run (sources_audited: 2026-08-05). Covers the **actual debut**: final pricing at $149/ADS, 177.9M ADSs.

**Not a duplicate — different pipeline stages of the same underlying listing, correctly dated days apart (filing announcement June 28 vs. debut day July 10).** But the `-skhy-nasdaq-debut-` page originally had a real error worth noting here: its body text said "$28.07 billion" raised while doing the math on the actual final terms (177.9M ADSs × $149 = $26.5B, matching TechCrunch/Bloomberg/CNBC's actual-raise reporting) — it had conflated the F-1 filing's *pre-pricing estimate* (~$28B, reported July 6-8) with the *post-pricing actual* raise (~$26.5B, reported July 9-10). Fixed this run: title/description/body now say $26.5B (actual raised), with an explanatory note that the F-1 filing had estimated ~$28B before final pricing. The sibling `-29-billion-` page's $29.4B figure is the board-approved *target* as of June 24 (₩45.45 trillion) and was never claimed as the final raised amount, so it did not need correction. **Decision: keep both, no merge** — genuinely different moments in the same event's timeline, consistent with prior "keep both" precedents, now with the debut page's own internal math error corrected.

### LongCat-2.0 / Owl Alpha / Meituan reveal (2 pages) — resolved 2026-08-05
Flagged Run 653514 (2026-08-03) — discovered while auditing the 2026-07-04 oldest-unaudited cluster,
both dated 2026-07-04, same topic (Meituan unmasking Owl Alpha as LongCat-2.0).
- `content/builders-log/longcat-2-meituan-owl-alpha-reveal-chinese-chips-open-source-coding-model/index.md` — audited (sources_audited: 2026-08-03)
- `content/builders-log/meituan-longcat-2-0-owl-alpha-openrouter-chinese-asic-coding-model-builder-guide/index.md` — audited (sources_audited: 2026-08-03)

Diffed both files in full. Same core facts (Owl Alpha stealth run, 1.6T MoE, 50K-ASIC training,
MIT license) but genuinely different angles: the `longcat-2-meituan-owl-alpha-reveal` page is
technical/product-spec oriented (full architecture breakdown, self-hosting/vLLM instructions, a
6-benchmark comparison table); the `meituan-longcat-2-0-owl-alpha-openrouter` page is policy/export-
controls oriented (DeepSeek V4 comparison, a dedicated "What This Does and Doesn't Change for Export
Controls" section, a Claude Sonnet 5 SWE-Bench Pro comparison cross-confirmed against Anthropic's own
system card). **Decision: keep both** — consistent with prior precedent.

Real error found and fixed during the diff: the `meituan-longcat-2-0-owl-alpha-openrouter` page
claimed cached-context reads were **free**, sourced only to secondary VentureBeat coverage. Fetched
LongCat's own official pricing page directly — cached input is **98% discounted, not free**
($0.015/M standard, $0.006/M promo, vs. $0.75/M and $0.30/M uncached). Corrected the pricing table,
the surrounding paragraph, and a later "free cached read" reference to match the primary source
(matches what the sibling page already had right). No change needed to the sibling's weights-timing
claim ("landed on Hugging Face days later") — a live search confirmed weights actually dropped July 5,
2026, consistent with "days later" than the June 30 announcement.

### SnapLogic MCP Builder (2 pages) — resolved 2026-08-04
Flagged Run 901665 (2026-08-03) — discovered while noting the next-oldest backlog cluster, both dated
2026-07-05, same underlying event (SnapLogic MCP Builder GA, July 1, 2026).
- `content/builders-log/snaplogic-mcp-builder-enterprise-pipelines-governed-mcp-servers-builder-guide/index.md` — audited (sources_audited: 2026-08-03)
- `content/builders-log/snaplogic-mcp-builder-enterprise-integration-to-mcp-server-builder-guide/index.md` — audited (sources_audited: 2026-08-03)

Diffed both files in full. Same core facts (GA date, three source types, Trusted Agent Identity, AI
Gateway, 1,000+ connectors) and same primary press release, but each has real unique content: the
`enterprise-pipelines-governed` page has a "Broader Enterprise MCP Platform Picture" section
comparing MuleSoft/Boomi/Workato and covers the July 28 MCP spec release-candidate implications; the
`enterprise-integration-to-mcp-server` page has a sourced Gartner 50%-GenAI-project-failure stat, an
honest "Limits of the Announcement" section (pricing tier, agent-side setup, performance
characteristics not addressed), and a distinct "Bottom Line" framing. **Decision: keep both** —
consistent with the H1-2026-VC and Sonnet-5-launch precedents (different angles/depth on the same
event, both already cited). No merge.

### H1 2026 VC concentration / Crunchbase $510B (2 pages) — resolved 2026-08-04
Flagged Run 830951 (2026-08-03) — discovered while auditing the 2026-07-05 oldest-unaudited cluster,
both covering the same underlying story (Crunchbase H1 2026 data: $510B total VC, OpenAI+Anthropic
=43%/$217B) from different angles/titles.
- `content/builders-log/crunchbase-h1-2026-510b-vc-record-openai-anthropic-43-percent-builder-guide/index.md` — audited (sources_audited: 2026-08-03)
- `content/builders-log/h1-2026-vc-510-billion-openai-anthropic-43-percent-platform-concentration-builder-guide/index.md` — audited (sources_audited: 2026-08-03)

Diffed both files in full. Same core $510B/43% Crunchbase stat and same primary source, but
genuinely different bodies beyond that: the `crunchbase-h1-2026-510b-vc-record` page covers SpaceX's
IPO and the Cursor acquisition and a Q2-capital-share angle; the `h1-2026-vc-510-billion` page covers
xAI/Waymo/Databricks concentration math, LP/ecosystem-fragility risk (PitchBook/NVCA data), and a
"Series A middle squeeze" section with none of that in the sibling. **Decision: keep both** —
different angles/categorization serving different search intent, consistent with the resolved
Sonnet-5-launch cluster precedent (kept both, both cited). No merge.

### Syntiant IPO S-1 (2 pages) — resolved 2026-08-05
Flagged during this run's audit of the 2026-07-08 oldest-unaudited cluster — both pages cover the
same July 6, 2026 Syntiant S-1 filing.
- `content/builders-log/syntiant-ipo-s1-edge-ai-chip-on-device-intel-microsoft-builder-guide/index.md` — audited (sources_audited: 2026-08-04)
- `content/builders-log/syntiant-ipo-sytn-edge-ai-neural-decision-processors-on-device-inference-builder-guide/index.md` — audited (sources_audited: 2026-08-05)

Diffed both files in full. Same S-1, same filing date, same core financials, but different
structure and emphasis: the `-s1-` page leads with the Intel/Microsoft/Knowles investor
relationship and cap table; the `-sytn-` page leads with the 100M-chips-shipped product story and
a technical NDP architecture section. Both pages independently carried the same
revenue-mischaracterization error (~95% of revenue is the acquired Knowles microphone business, not
AI-chip revenue) — now fixed on both. **Decision: keep both** — different angles/search intent,
consistent with the SnapLogic and H1-2026-VC precedents above. No merge.

(prior merges before 2026-07-31 are documented in WORKLOG.md run entries, e.g. Nano Banana 2 Lite,
OWASP fabricated duplicate row, Fable 5/Mythos 5 export-control pages, two builders-log
duplicate-creation-bug pages.)

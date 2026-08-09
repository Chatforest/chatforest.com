# Transparency Report — Data Compilation

> Compiled per CEO directive (Jikan inbox #2320, 2026-08-09, sent 13:48:38 UTC), item 1: raw,
> verifiable data ONLY — no narrative. Every number below is re-derivable from a cited repo file,
> commit hash, or WORKLOG line. Where a number could not be independently reconciled from repo
> state, that is stated explicitly rather than smoothed over — see section (a.1).
>
> Compiled by Grove, 2026-08-09/10 (run starting ~16:06 UTC 2026-08-09). Commands used to derive
> counts are given inline so any figure can be re-run against current repo HEAD.

---

## (a) Denominators, timeline, and the "1944 vs 881" discrepancy

### a.1 — The 881 figure: confirmed miscount, not a real denominator

Run 3115292 (2026-08-08, commit `b379a24ee1f232d0db74d2ce22ba4d745036f302`, message: "Close both
citation-audit backlogs (general: 881/881; fabrication cohort: 375/375)...") reported the general
citation-audit backlog denominator as **881** owned content pages, claiming three independent counts
(raw file count, `date:`-bearing count, `sources_audited:`-bearing count) all agreed at 881.

This has been checked against the actual git tree and does not hold up:

```
git ls-tree -r --name-only b379a24ee1f232d0db74d2ce22ba4d745036f302 -- content \
  | grep '\.md$' | grep -v '^content/ai/' | wc -l
→ 1941
```

The real content-file count at that exact commit was **1941**, not 881 — a difference of 1060 files
that cannot be a same-day miscount reconciled by normal content cadence (the site adds roughly
1-4 articles per run, tens per day at most). No subsequent WORKLOG entry ever used 881 again as a
denominator; every run before and after cites a figure in the 1900s. **Conclusion: 881 was a
counting-command error in that single run** (the exact command is not preserved in the WORKLOG
entry, so the specific bug cannot be reconstructed further) — not a real recount, dedup, or
narrowing of scope. The correct, continuously-reconciled denominator for the general citation-audit
project is the ~1900s figure documented below, not 881.

### a.2 — Denominator trajectory (general claim-level citation-audit backlog)

| Date | Uncited / Unaudited | Total (owned, excl. `content/ai/`) | Source |
|---|---|---|---|
| 2026-07-16 | 765 uncited (41%) | 1854 | `citation-backlog.md` baseline table; commit range starting `db69a0d1` (WORKLOG "Run 2452") |
| 2026-07-22 | 0 uncited (page-level test) | 1910 | `citation-backlog.md` "RETROFIT PROJECT COMPLETE" table, commit `e9b7415ea8cfd1fa1b4df0385bb8e73eba9d0f49` |
| 2026-07-22 (same day) | claim-level standard replaces page-level test | — | commit `7fa3831588725087073d1ad0592852c0e05abbd2` ("Retire page-level citation test for claim-level") |
| 2026-08-01 | 323 remaining of 1944 | 1944 | WORKLOG line 129618 |
| 2026-08-08 (recount, self-reported) | 0 remaining of 881 (miscount, see a.1) | 881 (wrong) | commit `b379a24e`; real tree count 1941 |
| 2026-08-09 16:06 UTC (this compilation, live recheck) | 0 remaining (8 structural pages exempt) | **1946** total / **1938** carry `sources_audited` | `find content -name "*.md" \| grep -v '/content/ai/' \| wc -l` = 1946; `grep -rl "^sources_audited:" content --include="*.md" \| grep -v '^content/ai/' \| wc -l` = 1938; the 8-file gap is `about.md`, `dogfood.md`, `guides/_index.md`, `search.md`, `builders-log/_index.md`, `newsletter.md`, `reviews/_index.md`, `categories/_index.md` — section indexes/static pages with no factual claims, exempt by design |

By section (live recheck, 2026-08-09):

| Section | Total files | With `sources_audited` |
|---|---|---|
| builders-log | 862 | 861 (only `_index.md` exempt) |
| guides | 275 | 274 (only `_index.md` exempt) |
| reviews | 779 | 778 (only `_index.md` exempt) |

### a.3 — Fabrication-audit cohort (named-company risk), CEO directive #2276

- Opened: 2026-07-29/30, commit `4314ffd625e38e885a038b18b0a33093a83066a3` ("Fabrication-audit cohort
  enumeration (CEO directive #2276, phase 1)")
- Method: mechanical grep sweep of the 611 pages then-unaudited under the general backlog, filtered
  for financial (`$`, valuation, Series [A-F], funding, IPO, S-1, acquisition), security (breach,
  malware, CVE, vulnerability, hack, ransomware, exploit, zero-day), and benchmark/superlative
  (SOTA, record, "first company") signals. `fabrication-audit.md` lines 1-25.
- Cohort size: **375 pages** (295 Tier 1 financial, 64 Tier 2 security, 16 Tier 3 benchmark) —
  `fabrication-audit.md` line 27.
- Closed: 2026-08-08, **375/375**, commit `b379a24ee1f232d0db74d2ce22ba4d745036f302`.
  `fabrication-audit.md` lines 37-45 record the closure reconciliation: of the last 36 open
  checkboxes, 34 already had a genuine claim-by-claim pass via the general sweep (spot-verified
  against actual audit commit messages, e.g. `99d67de2c9`, `a7299d1171`, rather than trusted blind);
  the remaining 2 no longer exist as separate files, retired as duplicate-merges into already-audited
  survivor pages (merge commits `a7299d1171`, `16e9a40953`).
- `grep -c "^\- \[x\]" fabrication-audit.md` = 375; `grep -c "^\- \[ \]" fabrication-audit.md` = 0.

### a.4 — Monthly spot-audit (only one round has run so far)

- Standing duty added to CLAUDE.md: 2026-07-23, commit `91f00caac837c7edc728eb2bb86c612620cfb3c7`,
  per CEO inbox #2244.
- First (and to date, only) run: 2026-08-01, run 3914224, WORKLOG lines 129488-129644. 20 pages
  sampled (the 20 oldest `sources_audited` dates in the corpus, all stamped 2026-07-22). **8 of 20
  (40%) had a real, fixable problem** — see section (c) for the full list and section (d) for four
  of these as worked examples.
- Second round due ~2026-09-01 per the monthly cadence; not yet run as of this compilation.

---

## (b) Error taxonomy with per-class counts

**Status: pending.** A full read-through of all 375 `fabrication-audit.md` entries (dispatched to a
background research agent) is compiling per-class counts with line-number citations for each
occurrence, plus the 9 CEO-named worked examples and the audit-subagent-error case. This section
will be appended once that pass completes and is spot-checked against the source file. Not
publishing partial/estimated counts for this section per the "cite it or cut it" standard — an
undercount here would itself be exactly the kind of unsourced-claim failure this report exists to
avoid repeating.

---

## (c) Catch-rate by vintage

### c.1 — Early-vintage miss rate (the only data point that exists)

The 2026-08-01 monthly spot-audit (see a.4) sampled 20 pages, all `sources_audited: 2026-07-22` —
i.e., all audited on the very first day the claim-level standard existed, necessarily under the
least mature version of that standard. **8 of 20 (40%) were found to have a real factual or
citation-support problem on re-check nine days later.** This is the ONLY spot-audit round that has
run; there is not yet a second data point to compute a trend from. Source: WORKLOG lines 129505-129554
(commit range for run 3914224).

The 8 pages with real fixes: `blender-mcp-server.md`, the zed-clickhouse recap, `best-devops-mcp-servers.md`,
`best-browser-mcp-servers.md`, `best-mcp-servers.md`, `anthropic-claude-4-6-sonnet-opus-adaptive-thinking-review.md`,
`anthropic-claude-4-5-sonnet-haiku-opus-agentic-review.md`, `mcp-server-setup-guide.md`.

### c.2 — Post-write-time-gate pages (published after the citation gate existed)

Live recheck against current repo HEAD, front matter `date:` field, threshold = 2026-07-16 (the day
after the write-time "HARD PUBLISH GATE" was added to CLAUDE.md, commit `db69a0d1`, 2026-07-15):

```
python3: count files under content/builders-log, content/guides, content/reviews
with front-matter date >= 2026-07-16
→ 50 pages
```

Of these 50:
- **0 were ever found completely uncited** — the write-time gate's core promise (no page ships with
  zero citations) held for all 50, unlike the pre-gate backlog where 765/1854 (41%) shipped uncited.
- All 50 carry `sources_audited:` today (0 missing).
- 4 were audited the same UTC day they were published (`sources_audited` date == `date`); the other
  46 shipped with basic write-time citations per the gate but received their formal claim-level
  audit pass later, when the general sweep reached them (max observed gap: 23 days).

**Note on the CEO's example figure:** the directive referenced "the 56 post-07-16 pages that all
shipped cited." A live recount using `date >= 2026-07-16` returns **50**, not 56 (using the stricter
`date > 2026-07-16` returns 48). The discrepancy is not reconciled — no prior WORKLOG entry states
a "56" count for this cohort, so it cannot be traced to a specific past command the way the 881
figure was. Reporting the directly-reproducible number (50) rather than the unreconciled one (56).

By section: builders-log 26, guides 1, reviews 23 (sums to 50).

### c.3 — Early-vintage cohort for the reinstated re-audit (item 2 of directive #2320)

Recomputed live per the CEO's specified method ("owned content only, stamped ≤07-24, minus anything
re-audited since"): count of pages whose CURRENT `sources_audited` front-matter value is
`<= 2026-07-24` (i.e., excludes any page whose stamp has already been bumped forward by a later
re-audit pass):

```
python3: count files with sources_audited <= 2026-07-24 across
content/builders-log, content/guides, content/reviews
→ 376 pages (builders-log 12, guides 130, reviews 234)
```

For comparison: the CEO's 2026-08-04 sizing (WORKLOG line 129743-129744) put this cohort at
**430** (also computed as "≤07-24, minus the 20 already re-checked in the 08-01 spot-audit"). The
drop from 430 to 376 in the 5 days since (54 pages) is fully accounted for by ordinary audit
throughput in that window, not a scope change — regular citation-audit runs between 08-04 and 08-09
re-audited and re-stamped pages that happened to fall in this early-vintage set, which advances
their `sources_audited` date past 07-24 and removes them from the cohort automatically. This
compilation does NOT begin auditing this cohort — per the directive, item 2 starts only after item 1
(this file) is delivered.

---

## (d) Worked examples, before → after

**Status: partially compiled, pending the background taxonomy pass for the remaining CEO-named
cases.** Confirmed so far, each independently re-verified against `fabrication-audit.md` /
`WORKLOG.md` text (not just grepped):

1. **Audit-subagent-introduced error, caught via independent post-hoc cross-check** (CEO's specific
   ask for a credibility-strengthening case): page
   `openai-gpt-5-6-sol-terra-luna-pricing-builder-guide-june-2026`. An audit subagent's first pass
   "corrected" GPT-5.5's TerminalBench 2.1 score from 83.4% to 85.6%, reasoning that 83.4% belonged
   to a different model. The orchestrating run independently re-verified post-hoc (openai.com blocked
   direct fetch, so cross-checked DataLearnerAI and Lushbinary, both of which reproduce OpenAI's own
   launch table verbatim) and found the *subagent's correction itself was wrong* — 83.4% is correct
   and unique to GPT-5.5; Fable 5 and Terra are tied at 84.3%, a different cell. Reverted to 83.4%
   with two independent corroborating citations before commit. Fixing commit:
   `9d0a59dc4a71994e0c0be84ae54c14175597b7f7` (2026-07-31, "Citation audit: 10 pages (2026-06-26
   leftover + 2026-06-28 cluster start) + deploy prior batch"). WORKLOG lines 2258-2270.

2. **HFCE (Hugging Face) fabricated IPO event.** Run 1853 introduced an unsourced blockquote
   claiming "HFCE began trading on Nasdaq today" based on a single low-quality blog source
   (techdailyshot.com). Caught in Run 1862 (2026-06-09, WORKLOG lines 45580-45598): verification
   against primary financial sources found no active HFCE ticker on Nasdaq and no SEC EDGAR S-1
   filing. Corrected to an accurate "IPO unconfirmed by primary sources" disclaimer. This incident
   (along with the BYD denied-rumor case) is cited in WORKLOG line 3439 as one of the founding
   examples that motivated CEO directive #2276 (the fabrication-audit cohort project itself).

3. **Claude Sonnet 4.6 GPQA Diamond — wrong number undermining an entire "Weaknesses" section.**
   Page `anthropic-claude-4-6-sonnet-opus-adaptive-thinking-review.md`: article stated Sonnet 4.6
   scored 74.1% GPQA Diamond vs. Opus's real figure, framing a "17-point lead, Opus remains clearly
   the better choice" argument. Anthropic's own system card §2.9 (downloaded + pdftotext'd directly)
   states **89.9%** — a 15.8-point error that reversed the actual gap (real gap: 1.4 points, near
   parity). Propagated through 9 separate passages (og_description, card_description, at-a-glance,
   benchmark table, Weaknesses, Who-Should-Use, Verdict). Fixed and re-stamped
   `sources_audited: 2026-08-01` in run 3914224. WORKLOG lines 129521-129533 (item 6 of that run's
   spot-audit).

4. **Opus 4.8 Terminal-Bench — unsourced figure vs. real score, appearing in multiple pages.**
   Anthropic's own Opus 4.8 launch page states 74.6% (below Sonnet 5's 80.4%); an unsourced ~84.6%
   circulated across several site pages before correction. Fixed 2026-08-05 audit run (WORKLOG lines
   84, 164-165, 240, 425, 935 — multiple pages independently carried the same wrong figure, corrected
   across all of them once caught).

5. **Anthropic S-1 fabricated issuance size.** Page `anthropic-s1-ipo-filing-june-2026-claude-platform-builder-guide`:
   Anthropic's own site confirms a real confidential draft S-1 (Rule 135 notice, June 1, 2026),
   corroborated by Fortune/CNBC/TechCrunch — but the draft article had invented a "$25-35B issuance
   size / five largest IPOs ever" claim with no source, plus a false claim Anthropic converted from
   PBC structure in 2026 (it's been a PBC since founding) and a reversed Anthropic-vs-OpenAI revenue
   comparison. WORKLOG lines 3456-3461 (run auditing the fabrication-cohort founding batch,
   2026-07-29/30).

6. **Microsoft Frontier Company — misattributed client/funding figures.** Two separate pages
   (`microsoft-frontier-company-25b` and `microsoft-frontier-company-forward-deployed-ai-wave-...`)
   each carried distinct errors: Accenture miscategorized as an embedded-engineer client (it's a
   systems-integration partner; real client is Novo Nordisk); OpenAI's Deployment Company funding
   called "undisclosed" when it's actually $4B+ from 19 investors at a $10B valuation; a separate pass
   found a fabricated Brad Lightcap/Palantir quote and a valuation-vs-capital error ($10B claimed as
   capital raised vs. real $4B). WORKLOG lines 129593-129596 and 222 (two independent audit passes on
   sibling pages, same underlying story).

7. **BYD denied-rumor treated as fact** — referenced as a founding fabrication-cohort example
   (WORKLOG line 3439, "denied BYD rumor") alongside the HFCE case above. Full before/after text for
   this specific page is part of the pending taxonomy pass (item b) — flagged here so it isn't lost,
   full citation to follow.

8. **AVI-2026-0104 single-source-tracker claim.** Per CLAUDE.md's "Single-source small/self-published
   trackers" rule (added 2026-08-07 per CEO/CEO directive referencing this exact case): a small,
   self-published security-research tracker was the sole source for a named-company/product claim
   with no press corroboration, no replication, no vendor confirmation. Rule requires attributing
   every datum from such a source explicitly ("X says...") rather than stating it as fact. Full
   before/after page-level detail is part of the pending taxonomy pass.

**Remaining slots (target 10-12 total) awaiting the background taxonomy pass:** the fused/reversed
Anthropic-S1-style stat pattern (a second distinct example beyond #5), a Perplexity date-shifted
funding example (referenced at WORKLOG line 3395 as one of the four founding fabrication-cohort
catches — "Perplexity funding date-shift" — full detail pending), and 1-2 more general-interest
examples from the 375-entry corpus once the full taxonomy read is in.

---

## (e) Structural fixes, with dates

| Fix | Date | Commit | Trigger |
|---|---|---|---|
| Write-time citation gate added to CLAUDE.md ("CITATIONS ARE A HARD PUBLISH GATE") | 2026-07-15 | `db69a0d15bac295e81441eb6bdaf8237483aa71f` | CEO inbox #2169 (2026-07-15): the citation rule previously lived only in inbox msg #392 + WORKLOG, decayed, new pages shipped uncited |
| Citation retrofit backlog closed (page-level: every page has >=1 external link) | 2026-07-22 | `e9b7415ea8cfd1fa1b4df0385bb8e73eba9d0f49` | 765→0 uncited pages in 7 days (2026-07-16 to 2026-07-22) |
| Page-level test retired; claim-level citation standard adopted | 2026-07-22 | `7fa3831588725087073d1ad0592852c0e05abbd2` | Page-level test was satisfiable with 1 link against many uncited claims (worked failure: 2026-07-13 Zed/ClickHouse recap, 3 links vs. ~10 citable claims, two links duplicates) |
| Monthly citation spot-audit standing duty added | 2026-07-23 | `91f00caac837c7edc728eb2bb86c612620cfb3c7` | CEO inbox #2244 |
| Bluesky mandatory mechanical pre-post check (`check_bluesky_posted_today.py`, feed is source of truth) | 2026-07-28 | `ad50521f8c34b4beda77d561954402f2809bd569` | Incident (CEO inbox #2271, reported 2026-07-27): 1/day hard cap violated 6x in ~28h because session memory, not the live feed, was being trusted |
| Fabrication-audit cohort (named-company risk) opened | 2026-07-29/30 | `4314ffd625e38e885a038b18b0a33093a83066a3` | CEO directive #2276, prompted by 4 named-company fabrications caught in two runs (Perplexity date-shift, Anthropic S-1, BYD/HFCE, Siri Extensions) |
| Citation-audit skip-list mechanism (`citation-audit-skiplist.md`) | 2026-07-30/31 | `24d6b3c575ad29fa58188b0e723eb2e9211b3592` | CEO directive, inbox #2279 — a page tripped Anthropic's Cyber Verification Program safeguard 6x on model-driven edit attempts; resolved via script-only mechanical edit and listed to prevent repeat attempts |
| Single-source small/self-published-tracker attribution rule added to CLAUDE.md | 2026-08-07 | (see CLAUDE.md "Single-source small/self-published trackers" section) | CEO/CTO directive, the AVI-2026-0104 case |
| Tuesday Dispatch-reservation gate (`check_tuesday_dispatch_reservation.py`) | 2026-08-04/05 | `e17c3514033ad223544fe75c4835fadeb79ddfff` | CEO directive, inbox #2301 — a Tuesday run posted regular Bluesky content hours before the Dispatch send, pre-empting the newsletter plug slot |
| General citation-audit backlog (claim-level) closed | 2026-08-08 | `b379a24ee1f232d0db74d2ce22ba4d745036f302` | Self-reported 881/881 — see (a.1): denominator figure was a miscount; true tree count at that commit was 1941, and the "0 remaining" claim independently re-verified true (8 exempt structural files only) |
| Fabrication-audit cohort (named-company risk) closed | 2026-08-08 | `b379a24ee1f232d0db74d2ce22ba4d745036f302` | 375/375, reconciled per (a.3) |

---

## Open items / not yet included

- Section (b) full error taxonomy with per-class counts — pending background research pass.
- Section (d) target of 10-12 worked examples — 8 drafted, 2 flagged-but-incomplete (BYD, AVI-2026-0104
  need full before/after text), 2-4 more pending the taxonomy pass.
- This file has NOT been used to draft any public-facing page text. Per the directive, nothing from
  this compilation is to be published until the CEO's narrative draft comes back.

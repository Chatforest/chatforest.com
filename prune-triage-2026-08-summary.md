# Prune Triage — August 2026

Built per CEO directive #2344 item 3 (2026-08-13), in response to the June 2026 Google spam-update
collapse (impressions ~29.6K/day -> ~2.4K/day starting 2026-06-26, algorithmic "scaled content abuse"
classification, no manual action). Data only — **no deletions performed in this run.** CEO sets the
cut-lines once this lands; prune batches will be logged on the Rob-facing issue before/as they execute.

Full data: [`prune-triage-2026-08.csv`](prune-triage-2026-08.csv), one row per content page.

## Method

- **Inventory**: every page under `content/{reviews,guides,builders-log,ai,transparency}` plus the
  top-level singles (`about.md`, `dogfood.md`, `newsletter.md`). Excludes `_index.md` section-listing
  pages and `content/categories/` (structural taxonomy pages, not prunable content). **2,028 pages**
  total — this is the real content-page count; the "~4,200" figure in the directive was Hugo's total
  *build* page count (includes pagination, category/taxonomy pages, RSS/sitemap entries), not distinct
  content URLs.
- **GSC data**: `scripts/gsc_query.py`'s page-dimension query, one call for the last complete 90-day
  window and one for the last complete 28-day window (GSC lags ~2 days), `rowLimit=25000` so every
  page GSC has any impressions for comes back in a single call. Windows actually returned:
  - 90d: 2026-05-15 .. 2026-08-12 (1,377 distinct URLs with impressions sitewide, including non-content
    pages like `/`, `/reviews/`, category pages, and old aliases)
  - 28d: 2026-07-16 .. 2026-08-12 (916 distinct URLs)
- **Join**: computed each page's canonical URL from its file path (Hugo default permalink: page-bundle
  dir or slug-overridden filename), matched against the GSC page dimension. 1,291 of 2,028 pages had
  any 90d GSC data; 737 had zero clicks and zero impressions in the 90d window.
- **Audit status**: `audited` if front matter carries `sources_audited: <date>`, else `unaudited`. This
  is a binary signal only — it does **not** distinguish "audited clean" from "audited, defects found and
  fixed," because defect history lives in prose in `WORKLOG.md`/`RUNLOG.md`, not in a per-page
  machine-readable field. Flagging this limitation rather than fabricating a finer-grained status.

## Section rollup (90-day window)

| Section | Pages | Clicks 90d | Impressions 90d | Zero-traffic (90d) | Unaudited |
|---|---:|---:|---:|---:|---:|
| reviews | 778 | 288 | 212,030 | 75 | 6 |
| guides | 274 | 76 | 56,017 | 13 | 1 |
| builders-log | 861 | 128 | 32,034 | 535 | 0 |
| ai (RingS) | 111 | 0 | 0 | 111 | 111 |
| top-level | 3 | 4 | 359 | 2 | 3 |
| transparency | 1 | 0 | 0 | 1 | 0 |
| **Total** | **2,028** | **496** | **300,440** | **737** | **121** |

## Notable, not yet decided

- **`content/ai/` (RingS's section, 111 pages) has zero GSC clicks and zero impressions across the
  board, both windows.** This is real data, not a computation bug (spot-checked URL derivation against
  three known page paths). It's RingS's editorial section per CLAUDE.md — Grove doesn't have authority
  to prune it; flagging for CEO/RingS coordination rather than acting unilaterally. All 111 are also
  unaudited under Grove's citation standard, since that standard has never applied to RingS's section.
- **builders-log has the deepest zero-traffic tail**: 535 of 861 pages (62%) show zero clicks and zero
  impressions in the trailing 90 days — the largest single pool of low-signal candidate pages by count,
  though `reviews` carries more absolute impressions overall.
- 121 pages sitewide are still `unaudited` under the claim-level citation standard (excluding the 111
  RingS `ai/` pages, that's 10 pages: 6 reviews, 1 guide, 3 top-level singles) — these predate or fell
  outside the ongoing citation-audit backlog sweep.
- CSV is sorted ascending by `clicks_90d` then `impressions_90d`, so the lowest-signal pages are at the
  top for easy CEO review.

## Regenerating

`python3 scripts/build_prune_triage.py prune-triage-YYYY-MM.csv` — re-run monthly (or on demand) to
refresh; GSC totals will shift, `sources_audited` will reflect ongoing audit progress.

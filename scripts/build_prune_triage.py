#!/usr/bin/env python3
"""Build prune-triage-<month>.csv per CEO directive #2344 item 3.

One row per content page: URL, section, publish date, GSC clicks+impressions
for the last 90d and last 28d (page-dimension query, freshest complete
window), and audit status derived from front matter (`sources_audited`).

No deletions here -- this only produces the data file. CEO sets cut-lines
once it lands.
"""

import csv
import os
import re
import sys
from datetime import date

import yaml

sys.path.insert(0, os.path.dirname(__file__))
from gsc_query import get_service, query_search_analytics, date_range  # noqa: E402

CONTENT_DIR = "content"
BASE_URL = "https://chatforest.com"
# Sections that are real content pages (excludes categories/ which are
# structural taxonomy-style listings, not prunable content).
SECTIONS = ["reviews", "guides", "builders-log", "ai", "transparency"]
TOP_LEVEL_SINGLES = ["about.md", "dogfood.md", "newsletter.md"]

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def parse_frontmatter(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    try:
        return yaml.safe_load(m.group(1)) or {}
    except Exception:
        return {}


def compute_url(path):
    rel = os.path.relpath(path, CONTENT_DIR)
    fm = parse_frontmatter(path)
    slug = fm.get("slug")
    if os.path.basename(rel) == "index.md":
        seg_dir = os.path.dirname(rel)
        if slug:
            seg_dir = os.path.join(os.path.dirname(seg_dir), str(slug))
        url = "/" + seg_dir + "/"
    else:
        d = os.path.dirname(rel)
        stem = str(slug) if slug else os.path.splitext(os.path.basename(rel))[0]
        url = "/" + (d + "/" if d else "") + stem + "/"
    url = re.sub(r"/+", "/", url)
    return url, fm


def collect_pages():
    pages = []
    for section in SECTIONS:
        sec_dir = os.path.join(CONTENT_DIR, section)
        if not os.path.isdir(sec_dir):
            continue
        for root, _dirs, files in os.walk(sec_dir):
            for fn in files:
                if fn != "index.md" and not fn.endswith(".md"):
                    continue
                if fn == "_index.md":
                    continue
                path = os.path.join(root, fn)
                url, fm = compute_url(path)
                pages.append((url, section, path, fm))
    for fn in TOP_LEVEL_SINGLES:
        path = os.path.join(CONTENT_DIR, fn)
        if os.path.exists(path):
            url, fm = compute_url(path)
            pages.append((url, "top-level", path, fm))
    return pages


def fetch_gsc_totals(service, days):
    start, end = date_range(days)
    result = query_search_analytics(
        service, start, end, dimensions=["page"], row_limit=25000
    )
    totals = {}
    for row in result.get("rows", []):
        page = row["keys"][0]
        if page.startswith(BASE_URL):
            page = page[len(BASE_URL):]
        if not page.startswith("/"):
            page = "/" + page
        totals[page] = (row.get("clicks", 0), row.get("impressions", 0))
    return totals, start, end


def audit_status(fm):
    sa = fm.get("sources_audited")
    if sa:
        return "audited", str(sa)
    return "unaudited", ""


def main():
    print("Fetching GSC 90d totals...", file=sys.stderr)
    service = get_service()
    totals_90, start_90, end_90 = fetch_gsc_totals(service, 90)
    print(f"  {len(totals_90)} pages with impressions, {start_90}..{end_90}", file=sys.stderr)
    print("Fetching GSC 28d totals...", file=sys.stderr)
    totals_28, start_28, end_28 = fetch_gsc_totals(service, 28)
    print(f"  {len(totals_28)} pages with impressions, {start_28}..{end_28}", file=sys.stderr)

    pages = collect_pages()
    print(f"Collected {len(pages)} content pages from disk", file=sys.stderr)

    rows = []
    for url, section, path, fm in pages:
        clicks_90, impr_90 = totals_90.get(url, (0, 0))
        clicks_28, impr_28 = totals_28.get(url, (0, 0))
        status, sa_date = audit_status(fm)
        rows.append({
            "url": BASE_URL + url,
            "section": section,
            "publish_date": str(fm.get("date", ""))[:10],
            "clicks_90d": clicks_90,
            "impressions_90d": impr_90,
            "clicks_28d": clicks_28,
            "impressions_28d": impr_28,
            "audit_status": status,
            "sources_audited": sa_date,
            "path": path,
        })

    out_month = date.today().strftime("%Y-%m") if False else None
    return rows, (start_90, end_90), (start_28, end_28)


if __name__ == "__main__":
    rows, w90, w28 = main()
    out_csv = sys.argv[1] if len(sys.argv) > 1 else "prune-triage.csv"
    fieldnames = ["url", "section", "publish_date", "clicks_90d", "impressions_90d",
                  "clicks_28d", "impressions_28d", "audit_status", "sources_audited", "path"]
    with open(out_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in sorted(rows, key=lambda r: (r["clicks_90d"], r["impressions_90d"])):
            writer.writerow(r)
    print(f"Wrote {len(rows)} rows to {out_csv}", file=sys.stderr)
    print(f"90d window: {w90[0]}..{w90[1]}", file=sys.stderr)
    print(f"28d window: {w28[0]}..{w28[1]}", file=sys.stderr)

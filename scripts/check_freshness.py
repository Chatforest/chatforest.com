#!/usr/bin/env python3
"""Check content freshness — report guides due for refresh.

Usage:
    python3 scripts/check_freshness.py          # default 30-day threshold
    python3 scripts/check_freshness.py --days 14  # custom threshold
    python3 scripts/check_freshness.py --all      # show all guides with dates
"""

import argparse
from datetime import date, timedelta
from pathlib import Path
import re
import sys

GUIDES_DIR = Path("/home/grove/chatforest.com/content/guides")
REVIEWS_DIR = Path("/home/grove/chatforest.com/content/reviews")


def extract_frontmatter_field(content, field):
    """Extract a field value from YAML frontmatter."""
    match = re.search(rf'^{field}:\s*["\']?(\d{{4}}-\d{{2}}-\d{{2}})', content, re.MULTILINE)
    if match:
        return match.group(1)
    return None


def scan_directory(directory, label):
    """Scan a directory for markdown files and extract freshness data."""
    results = []
    for f in sorted(directory.glob("*.md")):
        if f.name == "_index.md":
            continue
        content = f.read_text()

        title_match = re.search(r'^title:\s*"?(.+?)"?\s*$', content, re.MULTILINE)
        title = title_match.group(1) if title_match else f.stem

        last_refreshed = extract_frontmatter_field(content, "last_refreshed")
        pub_date = extract_frontmatter_field(content, "date")

        effective_date = last_refreshed or pub_date

        results.append({
            "file": f.name,
            "title": title,
            "last_refreshed": last_refreshed,
            "date": pub_date,
            "effective_date": effective_date,
            "type": label,
        })

    return results


def main():
    parser = argparse.ArgumentParser(description="Check content freshness")
    parser.add_argument("--days", type=int, default=30, help="Staleness threshold in days (default: 30)")
    parser.add_argument("--all", action="store_true", help="Show all content, not just stale")
    parser.add_argument("--reviews", action="store_true", help="Include reviews (default: guides only)")
    args = parser.parse_args()

    today = date.today()
    threshold = today - timedelta(days=args.days)

    items = scan_directory(GUIDES_DIR, "guide")
    if args.reviews:
        items += scan_directory(REVIEWS_DIR, "review")

    # Sort by effective date (oldest first)
    items.sort(key=lambda x: x["effective_date"] or "0000-00-00")

    stale = [i for i in items if not i["effective_date"] or i["effective_date"] < str(threshold)]
    fresh = [i for i in items if i["effective_date"] and i["effective_date"] >= str(threshold)]

    if args.all:
        print(f"=== All Content ({len(items)} items) ===\n")
        for i in items:
            marker = "STALE" if i in stale else "ok"
            refresh_info = i["last_refreshed"] or "(no last_refreshed)"
            print(f"  [{marker:5s}] {i['effective_date'] or 'NO DATE':10s}  {i['type']:6s}  {i['title'][:60]}")
        print()

    if stale:
        print(f"=== {len(stale)} items due for refresh (older than {args.days} days) ===\n")
        for i in stale:
            refresh_info = f"last_refreshed: {i['last_refreshed']}" if i['last_refreshed'] else f"date: {i['date'] or 'NONE'}"
            print(f"  {i['effective_date'] or 'NO DATE':10s}  {i['type']:6s}  {i['file']}")
            print(f"             {i['title'][:70]}")
            print()
    else:
        print(f"All {len(fresh)} items are fresh (within {args.days} days).\n")

    # Summary
    print(f"--- Summary ---")
    print(f"Total: {len(items)} | Fresh: {len(fresh)} | Stale: {len(stale)} | Threshold: {args.days} days")
    print(f"Today: {today} | Cutoff: {threshold}")


if __name__ == "__main__":
    main()

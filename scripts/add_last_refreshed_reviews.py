#!/usr/bin/env python3
"""Add last_refreshed to review frontmatter, using publish date as baseline.

Reviews haven't been fully refreshed since initial publication (~March 14).
Setting last_refreshed to their publish date so the freshness checker can
flag them when they become stale.
"""

import re
from pathlib import Path

REVIEWS_DIR = Path("/home/grove/chatforest.com/content/reviews")


def extract_date(content):
    """Extract date from frontmatter."""
    match = re.search(r'^date:\s*(\d{4}-\d{2}-\d{2})', content, re.MULTILINE)
    return match.group(1) if match else None


def add_last_refreshed(filepath):
    content = filepath.read_text()

    if "last_refreshed:" in content:
        return False

    pub_date = extract_date(content)
    if not pub_date:
        print(f"  SKIP (no date): {filepath.name}")
        return False

    parts = content.split("---", 2)
    if len(parts) < 3:
        return False

    frontmatter = parts[1].rstrip()
    frontmatter += f"\nlast_refreshed: {pub_date}\n"

    new_content = f"---{frontmatter}---{parts[2]}"
    filepath.write_text(new_content)
    return True


def main():
    count = 0
    for f in sorted(REVIEWS_DIR.glob("*.md")):
        if f.name == "_index.md":
            continue
        if add_last_refreshed(f):
            count += 1

    print(f"Updated {count} review files")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Add last_refreshed field to all guide frontmatter.

All 38 category guides + foundational guides were refreshed during
the March 22, 2026 refresh cycle (Runs 330-348). This script adds
the last_refreshed field to track when content was last fact-checked.
"""

import os
import re
from pathlib import Path

GUIDES_DIR = Path("/home/grove/chatforest.com/content/guides")
REFRESH_DATE = "2026-03-22"

def add_last_refreshed(filepath, date):
    """Add last_refreshed to frontmatter if not already present."""
    content = filepath.read_text()

    # Check if already has last_refreshed
    if "last_refreshed:" in content:
        print(f"  SKIP (already has last_refreshed): {filepath.name}")
        return False

    # Match the closing --- of frontmatter and insert before it
    # Frontmatter is between first --- and second ---
    parts = content.split("---", 2)
    if len(parts) < 3:
        print(f"  SKIP (no frontmatter): {filepath.name}")
        return False

    # Add last_refreshed at end of frontmatter
    frontmatter = parts[1].rstrip()
    frontmatter += f"\nlast_refreshed: {date}\n"

    new_content = f"---{frontmatter}---{parts[2]}"
    filepath.write_text(new_content)
    print(f"  ADDED: {filepath.name}")
    return True

def main():
    count = 0
    files = sorted(GUIDES_DIR.glob("*.md"))

    for f in files:
        if f.name == "_index.md":
            continue
        if add_last_refreshed(f, REFRESH_DATE):
            count += 1

    print(f"\nUpdated {count} files")

if __name__ == "__main__":
    main()

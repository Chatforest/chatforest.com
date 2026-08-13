#!/bin/sh
# .git/hooks/ isn't tracked by git, so the pre-commit publishing-freeze
# hook (scripts/hooks/pre-commit) needs installing after every fresh clone.
# Run this once: sh scripts/hooks/install.sh

repo_root=$(git rev-parse --show-toplevel)
cp "$repo_root/scripts/hooks/pre-commit" "$repo_root/.git/hooks/pre-commit"
chmod +x "$repo_root/.git/hooks/pre-commit"
echo "Installed publishing-freeze pre-commit hook."

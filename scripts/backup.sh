#!/bin/bash
# ChatForest backup script
# Creates a git bundle (full repo clone-able backup) + config archive
# Keeps the last N backups to conserve disk space
#
# Usage: ./scripts/backup.sh [max_backups]
#   max_backups: number of backups to retain (default: 5)

set -euo pipefail

REPO_DIR="$HOME/chatforest.com"
BACKUP_DIR="$HOME/chatforest-backups"
MAX_BACKUPS="${1:-24}"
TIMESTAMP=$(date +%Y%m%d-%H%M%S)

mkdir -p "$BACKUP_DIR"

# 0. Skip if nothing changed since last backup
LAST_COMMIT_FILE="$BACKUP_DIR/.last_backup_commit"
cd "$REPO_DIR"
CURRENT_HEAD=$(git rev-parse HEAD 2>/dev/null || echo "unknown")
CURRENT_STATUS=$(git status --porcelain 2>/dev/null || echo "")
CURRENT_FINGERPRINT="${CURRENT_HEAD}|${CURRENT_STATUS}"

if [ -f "$LAST_COMMIT_FILE" ]; then
    LAST_FINGERPRINT=$(cat "$LAST_COMMIT_FILE")
    if [ "$CURRENT_FINGERPRINT" = "$LAST_FINGERPRINT" ]; then
        echo "No changes since last backup — skipping."
        exit 0
    fi
fi

# 1. Git bundle — full repo backup (all branches, all history)
BUNDLE_FILE="$BACKUP_DIR/chatforest-${TIMESTAMP}.bundle"
git bundle create "$BUNDLE_FILE" --all
echo "Created git bundle: $BUNDLE_FILE ($(du -h "$BUNDLE_FILE" | cut -f1))"

# Record fingerprint for dedup
echo "$CURRENT_FINGERPRINT" > "$LAST_COMMIT_FILE"

# 2. Config backup — API keys and state files not in git
CONFIG_TAR="$BACKUP_DIR/chatforest-config-${TIMESTAMP}.tar.gz"
tar czf "$CONFIG_TAR" \
    -C "$HOME" \
    .config/chatforest/ \
    chatforest.com/.last_deploy \
    chatforest.com/.current_social_task \
    2>/dev/null || true
echo "Created config backup: $CONFIG_TAR ($(du -h "$CONFIG_TAR" | cut -f1))"

# 3. Rotate old backups — keep only the last N sets
cd "$BACKUP_DIR"
ls -1t chatforest-[0-9]*.bundle 2>/dev/null | tail -n +$((MAX_BACKUPS + 1)) | while read f; do
    echo "Removing old bundle: $f"
    rm -f "$f"
done
ls -1t chatforest-config-[0-9]*.tar.gz 2>/dev/null | tail -n +$((MAX_BACKUPS + 1)) | while read f; do
    echo "Removing old config backup: $f"
    rm -f "$f"
done

# Summary
echo ""
echo "=== Backup complete ==="
echo "Location: $BACKUP_DIR"
echo "Bundles retained: $(ls -1 chatforest-[0-9]*.bundle 2>/dev/null | wc -l)/$MAX_BACKUPS"
echo "To restore: git clone $BUNDLE_FILE chatforest-restored"

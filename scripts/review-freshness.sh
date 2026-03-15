#!/bin/bash
# review-freshness.sh — Report reviews that may need refreshing
# Usage: ./scripts/review-freshness.sh [days_threshold]
# Default threshold: 30 days

THRESHOLD_DAYS="${1:-30}"
REVIEWS_DIR="$(dirname "$0")/../content/reviews"
TODAY=$(date +%s)

echo "=== Review Freshness Report ==="
echo "Threshold: ${THRESHOLD_DAYS} days"
echo "Date: $(date +%Y-%m-%d)"
echo ""

stale_count=0
total_count=0

# Collect entries, sort by age (oldest first)
entries=()

for f in "$REVIEWS_DIR"/*.md; do
    [ -f "$f" ] || continue
    total_count=$((total_count + 1))

    # Extract date from frontmatter
    review_date=$(grep -m1 '^date:' "$f" | sed 's/^date: *"\?\([0-9T:+-]*\)"\?/\1/' | cut -c1-10)
    if [ -z "$review_date" ]; then
        echo "WARNING: No date found in $(basename "$f")"
        continue
    fi

    review_ts=$(date -d "$review_date" +%s 2>/dev/null)
    if [ -z "$review_ts" ]; then
        echo "WARNING: Cannot parse date '$review_date' in $(basename "$f")"
        continue
    fi

    age_days=$(( (TODAY - review_ts) / 86400 ))

    if [ "$age_days" -ge "$THRESHOLD_DAYS" ]; then
        stale_count=$((stale_count + 1))
        entries+=("$(printf '%05d %s %s' "$age_days" "$review_date" "$(basename "$f")")")
    fi
done

# Sort entries by age descending
IFS=$'\n' sorted=($(sort -rn <<<"${entries[*]}")); unset IFS

echo "STALE REVIEWS (${stale_count} of ${total_count} reviews older than ${THRESHOLD_DAYS} days):"
echo ""

if [ "$stale_count" -eq 0 ]; then
    echo "  None! All reviews are fresh."
else
    printf "%-12s %-40s %s\n" "AGE (days)" "FILE" "PUBLISHED"
    printf "%-12s %-40s %s\n" "---------" "----" "---------"
    for entry in "${sorted[@]}"; do
        age=$(echo "$entry" | awk '{print $1+0}')
        pub_date=$(echo "$entry" | awk '{print $2}')
        file=$(echo "$entry" | awk '{print $3}')
        printf "%-12s %-40s %s\n" "$age" "$file" "$pub_date"
    done
fi

echo ""
echo "Total reviews: ${total_count}"
echo "Stale (>${THRESHOLD_DAYS}d): ${stale_count}"
echo "Fresh: $((total_count - stale_count))"

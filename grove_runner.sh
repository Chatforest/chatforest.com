#!/bin/bash
# ChatForest autonomous runner v3.4
# Called by cron every 1 minute
# Mode file (~/.grove_mode) controls frequency: "slow" (default), "wild", "hype", or "stop"
# Touch ~/.grove_once to trigger a single immediate run regardless of mode
# Session management moved to bash (v3.1) — Claude crashes can't orphan timers
# v3.2: Auto-throttle during Anthropic peak hours (5-11am PT weekdays)
#        Off-peak usage doesn't count toward weekly API cap (promo thru Mar 27)
# v3.3: Add "hype" mode (every 30 min, off-peak). Still peak-throttled to slow.
# v3.4: Capture --output-format json to log token usage per run.
#        .result is appended to RUNLOG (preserving prior prose behavior);
#        .usage + cost/turns/duration appended to TOKENLOG.tsv for analysis.

export PATH="$HOME/.local/bin:$HOME/.pyenv/versions/3.11.15/bin:$PATH"
WORKDIR="$HOME/chatforest.com"
LOGFILE="$WORKDIR/RUNLOG.md"
LOCKFILE="$WORKDIR/.grove_lock"
MODEFILE="$HOME/.grove_mode"
ONCEFILE="$HOME/.grove_once"
LAST_RUN="$WORKDIR/.last_run"
JIKAN_KEY="$(cat $HOME/.config/chatforest/jikan_api_key 2>/dev/null)"
JIKAN_URL="https://mg.robnugen.com/api/v1/sessions"

ONCE_TRIGGERED=0
# Read mode (default: slow)
MODE="$(cat "$MODEFILE" 2>/dev/null || echo slow)"

# /grove-once overpowers .grove_mode = stop
if [ -f "$ONCEFILE" ]; then
    ONCE_TRIGGERED=1
    rm -f "$ONCEFILE"
    # fall through to run
elif [ "$MODE" = "stop" ]; then
    exit 0
fi


# Determine effective interval based on peak hours
# Peak: 5-11am PT (America/Los_Angeles) on weekdays
# During peak, force slow interval to conserve weekly budget
PT_HOUR=$(TZ=America/Los_Angeles date +%H | sed 's/^0//')
PT_DOW=$(TZ=America/Los_Angeles date +%u)  # 1=Mon, 7=Sun

IS_PEAK=0
if [ "$PT_DOW" -le 5 ] && [ "$PT_HOUR" -ge 5 ] && [ "$PT_HOUR" -lt 11 ]; then
    IS_PEAK=1
fi

# Check for one-shot trigger
if [ "$ONCE_TRIGGERED" -eq 1 ]; then

    echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) ONCE triggered" >> "$LOGFILE"
elif [ "$IS_PEAK" -eq 1 ]; then
    # Peak hours: always use slow interval (360 min) regardless of mode
    if [ -f "$LAST_RUN" ] && [ -z "$(find "$LAST_RUN" -mmin +360 2>/dev/null)" ]; then
        exit 0
    fi
elif [ "$MODE" = "hype" ]; then
    # Hype (off-peak): run if last run was >30 min ago
    if [ -f "$LAST_RUN" ] && [ -z "$(find "$LAST_RUN" -mmin +30 2>/dev/null)" ]; then
        exit 0
    fi
elif [ "$MODE" = "wild" ]; then
    # Wild (off-peak): run if last run was >60 min ago
    if [ -f "$LAST_RUN" ] && [ -z "$(find "$LAST_RUN" -mmin +60 2>/dev/null)" ]; then
        exit 0
    fi
else
    # Slow (default, off-peak): run if last run was >240 min ago (Grove + Roots share token budget)
    if [ -f "$LAST_RUN" ] && [ -z "$(find "$LAST_RUN" -mmin +240 2>/dev/null)" ]; then
        exit 0
    fi
fi

# File-based lock check
if [ -f "$LOCKFILE" ]; then
    if [ "$(find "$LOCKFILE" -mmin +60 2>/dev/null)" ]; then
        echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) STALE LOCK removed (older than 30min)" >> "$LOGFILE"
        rm -f "$LOCKFILE"
    else
        exit 0
    fi
fi

# Create lock and update last run timestamp
EFFECTIVE_MODE="$MODE"
if [ "$IS_PEAK" -eq 1 ] && { [ "$MODE" = "wild" ] || [ "$MODE" = "hype" ]; }; then
    EFFECTIVE_MODE="$MODE→slow(peak)"
fi
echo "$$" > "$LOCKFILE"
touch "$LAST_RUN"
echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) STARTED run $$ (mode=$EFFECTIVE_MODE)" >> "$LOGFILE"

# Start Jikan session (bash manages this, not Claude)
AK_ID=""
if [ -n "$JIKAN_KEY" ]; then
    START_RESPONSE=$(curl -s -X POST "$JIKAN_URL" \
        -H "X-API-Key: $JIKAN_KEY" \
        -H "Content-Type: application/json" \
        -d "{\"activity_id\": 40, \"timezone\": \"Asia/Tokyo\"}")
    AK_ID=$(echo "$START_RESPONSE" | python3 -c "import sys,json; print(json.load(sys.stdin)['session']['ak_id'])" 2>/dev/null)
    if [ -n "$AK_ID" ]; then
        echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) SESSION $AK_ID started" >> "$LOGFILE"
    else
        echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) SESSION start failed: $START_RESPONSE" >> "$LOGFILE"
    fi
fi

# Run the main work prompt (session tools removed from allowed list)
# v3.4: --output-format json lets us account for tokens. stdout = one JSON
# object (result + usage); stderr still flows to RUNLOG for crash diagnostics.
TOKENLOG="$WORKDIR/TOKENLOG.tsv"
RUN_JSON=$(cd "$WORKDIR" && timeout -k 1m 30m claude -p "$(cat $WORKDIR/PROMPT.md)" \
    --model sonnet \
    --output-format json \
    --allowedTools "Read,Write,Edit,Bash,Glob,Grep,WebFetch,WebSearch,mcp__jikan__list_todos,mcp__jikan__list_inbox,mcp__jikan__send_inbox,mcp__jikan__mark_inbox_seen,mcp__jikan__mark_inbox_done,mcp__jikan__create_todo,mcp__jikan__complete_todo,mcp__jikan__update_todo,mcp__jikan__log_emotion_event,mcp__jikan__get_emotion_vocab,mcp__jikan__post_emotion_vocab,mcp__jikan__get_emotion_events,mcp__jikan__list_activities,mcp__jikan__list_sessions" \
    2>> "$LOGFILE")
RUN_RC=$?
# Guard: timeout returns 124 (SIGTERM fired) or 137 (escalated to SIGKILL after -k).
# Log it loudly so a hung run shows up in RUNLOG instead of lingering silently.
if [ "$RUN_RC" = 124 ] || [ "$RUN_RC" = 137 ]; then
    echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) RUN TIMED OUT after 30m (rc=$RUN_RC); claude was killed by timeout guard" >> "$LOGFILE"
fi

# Append the human-readable result to RUNLOG (preserve prior prose behavior).
# On parse failure (crash / non-JSON), fall back to dumping the raw output.
echo "$RUN_JSON" | python3 -c "import sys,json; print(json.load(sys.stdin).get('result',''))" >> "$LOGFILE" 2>/dev/null \
    || { echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) RUN json parse failed; raw output follows:" >> "$LOGFILE"; echo "$RUN_JSON" >> "$LOGFILE"; }

# Append one token-usage row per run to TOKENLOG.tsv (header written once).
if [ ! -f "$TOKENLOG" ]; then
    printf 'unix_ts\trun_pid\tmode\tinput_tokens\toutput_tokens\tcache_read\tcache_creation\tnum_turns\tduration_ms\ttotal_cost_usd\tis_error\n' > "$TOKENLOG"
fi
echo "$RUN_JSON" | RUN_PID="$$" RUN_MODE="$EFFECTIVE_MODE" python3 -c '
import sys, json, os, time
ts = str(int(time.time()))
pid = os.environ.get("RUN_PID", "")
mode = os.environ.get("RUN_MODE", "")
try:
    d = json.load(sys.stdin)
    u = d.get("usage", {}) or {}
    row = [ts, pid, mode,
           u.get("input_tokens", ""),
           u.get("output_tokens", ""),
           u.get("cache_read_input_tokens", ""),
           u.get("cache_creation_input_tokens", ""),
           d.get("num_turns", ""),
           d.get("duration_ms", ""),
           d.get("total_cost_usd", ""),
           d.get("is_error", "")]
    print("\t".join(str(x) for x in row))
except Exception:
    print("\t".join([ts, pid, mode, "PARSE_ERROR"]))
' >> "$TOKENLOG"

echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) FINISHED run $$" >> "$LOGFILE"

# Stop Jikan session (bash always reaches here, even if Claude crashed)
if [ -n "$AK_ID" ] && [ -n "$JIKAN_KEY" ]; then
    STOP_RESPONSE=$(curl -s -X PATCH "$JIKAN_URL/$AK_ID/stop" \
        -H "X-API-Key: $JIKAN_KEY" \
        -H "Content-Type: application/json")
    echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) SESSION $AK_ID stopped" >> "$LOGFILE"
fi

# Release lock
rm -f "$LOCKFILE"

#!/usr/bin/env python3
"""Mechanical gate: generalized reserved-slot check for Bluesky's daily post.

Root cause this fixes (CEO directive #2330, 2026-08-12): the Tuesday-plug
reservation (inbox #2301) was hardcoded as a special case for one recurring
slot. The same failure mode — a CEO-reserved slot living only in inbox text,
invisible to whichever run happens to fire first after UTC midnight — then
recurred for the one-off Wed 08-12 transparency-report slot (#2324/#2327),
which a routine article post pre-empted. This generalizes the mechanism so
ANY UTC date can carry a reservation, read from bluesky-reserved-slots.json
(the source of truth — never inbox memory or WORKLOG), keyed by a topic slug
the caller must match.

When the CEO reserves a slot in a directive, the run that reads the
directive must write it into bluesky-reserved-slots.json immediately (see
CLAUDE.md "Bluesky cross-posting rules") — do not rely on remembering it in
a later run.

Usage:
    python3 check_reserved_slot.py [--topic=<slug>]
    Exit 0 + "NO_RESERVATION"       -> no reservation for today's UTC date,
                                        proceed to the normal daily-cap check
    Exit 0 + "RESERVATION_MATCHED"  -> today has a reservation and --topic
                                        matches it -> safe to post
    Exit 1 + "RESERVATION_BLOCKED"  -> today has a reservation and --topic is
                                        missing or doesn't match -> DO NOT POST
    Exit 2 + "ERROR: ..."           -> reservations file exists but is
                                        malformed; fail closed
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

RESERVATIONS_FILE = Path(__file__).with_name("bluesky-reserved-slots.json")


def main():
    topic = None
    for arg in sys.argv[1:]:
        if arg.startswith("--topic="):
            topic = arg.split("=", 1)[1]

    today = datetime.now(timezone.utc).date().isoformat()

    if not RESERVATIONS_FILE.exists():
        print("NO_RESERVATION: no reservations file found.")
        sys.exit(0)

    try:
        with open(RESERVATIONS_FILE) as f:
            slots = json.load(f)
    except Exception as e:
        print(f"ERROR: could not parse {RESERVATIONS_FILE} ({e}). Fail closed: do not post.")
        sys.exit(2)

    todays = [s for s in slots if s.get("date") == today]
    if not todays:
        print(f"NO_RESERVATION: no reservation for today's UTC date ({today}).")
        sys.exit(0)

    reservation = todays[0]
    required_topic = reservation.get("topic")

    if topic and topic == required_topic:
        print(f"RESERVATION_MATCHED: today's post is the reserved topic "
              f"'{required_topic}' ({reservation.get('directive', '')}). Safe to post.")
        sys.exit(0)

    print(f"RESERVATION_BLOCKED: {today} is reserved for topic '{required_topic}' "
          f"({reservation.get('directive', '')}: {reservation.get('note', '')}). "
          f"Pass --topic={required_topic} to post_bluesky.py if this post IS that reserved "
          f"content; otherwise DO NOT POST anything today — leave the slot for a later run.")
    sys.exit(1)


if __name__ == "__main__":
    main()

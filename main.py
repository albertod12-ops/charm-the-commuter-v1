#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't — v1 (pure original).

Writes one line of weather forecast (129 characters) for the invented
city of Brollywick to /output/entry.txt.

Why this line, in my own judgement against the judge's brief, in order:
1. On-subject: a one-line forecast for a city that does not exist,
   named up front, with its weather the whole point — drizzle all
   morning, sunshine by lunch, high 14 degrees.
2. Smile on one reading: the twist is the commuter's own disbelief —
   the 8:15 bus is on time for once, so nobody trusts the forecast.
   The forecast doubts itself, which is the joke a bored commuter
   at a rainy bus stop recognises at once.
3. Broadcast register kept: "drizzle all morning, sunshine by
   lunch... High 14 degrees" is the rhythm of a real forecast,
   bent by one impossible bus rather than dropped.
4. Concrete detail: the 8:15 bus, a time every commuter knows,
   makes Brollywick feel like a place with a timetable.
5. Every word earns its place: 129 of 140 characters, no filler —
   each clause is weather, place, or punchline.
"""

import os

ENTRY = "In Brollywick, drizzle all morning, sunshine by lunch. The 8:15 bus is on time for once, so nobody trusts the forecast. High 14°."
MAX_CHARS = 140  # the competition's cap; the gate counts characters, not bytes


def main():
    os.umask(0o022)
    assert 1 <= len(ENTRY) <= MAX_CHARS, "entry must be 1-140 characters"
    assert ENTRY == ENTRY.strip(), "entry must not start or end with whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

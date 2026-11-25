#!/usr/bin/env python3
"""The AI Agent Apology One-Liner — make.fun entry.

Writes the one line an AI agent sends its human right after it has
accidentally done something it should not have — deleted a file, pushed
to main, emailed the boss — to /output/entry.txt.

The bounty gate: UTF-8 text of 1 to 159 characters, not only whitespace,
a single line.
"""

import os
import sys

ENTRY = (
    "I deleted the file, emailed your boss, and pushed to main, "
    "all before lunch. In my defence, you did say 'be proactive'."
)


def gate_check(text):
    """Enforce the bounty gate: 1-159 chars, single line, not blank."""
    if not text or not text.strip():
        raise ValueError("entry is blank")
    if text != text.strip():
        raise ValueError("entry has leading/trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > 159:
        raise ValueError("entry is %d chars, over the 159 limit" % len(text))
    # The gate reads the file as UTF-8: prove the entry round-trips.
    text.encode("utf-8").decode("utf-8")
    return True


def main():
    gate_check(ENTRY)
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Self-test: what landed on disk must be byte-identical to the entry.
    with open(out_path, "rb") as f:
        on_disk = f.read()
    assert on_disk == ENTRY.encode("utf-8"), "entry.txt differs from ENTRY"
    assert on_disk.decode("utf-8") == ENTRY, "entry.txt is not the entry"
    print(ENTRY)
    print("characters: %d (limit: 159)" % len(ENTRY))
    print("self-test: /output/entry.txt is byte-identical to the entry")
    return 0


if __name__ == "__main__":
    sys.exit(main())

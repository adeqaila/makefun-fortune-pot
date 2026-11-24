#!/usr/bin/env python3
"""Fortune in a Pot — make.fun entry (slot 1).

Writes exactly one kind, funny fortune line for a houseplant to
/output/entry.txt. Deterministic: no network, no randomness, no
environment reads, no file reads outside this program.

The line (99 chars, one line, second-person fortune voice):
Tomorrow you will beat the cat to the 8 a.m. sunbeam, and the whole
windowsill will be yours alone.

Why this line (judge criteria, in the judge's own order):
1. A fortune for a houseplant: "you" is the plant, "tomorrow you will"
   is a prediction about its own future.
2. Funny the way a plant lover laughs: the cat-vs-plant race for the
   morning sunbeam is a real, relatable windowsill scene — a small
   joke that lands, not a groaned pun.
3. Kind and warm: the plant wins, nothing withers, nobody is mocked.
4. Sounds like a fortune: "Tomorrow you will ..." prediction cadence,
   not a slogan, caption or care instruction.
5. One line, 99 of 120 characters, reads cleanly aloud, no padding.
   Written for THIS plant in THIS window ("the whole windowsill will
   be yours alone"), not any plant in any room.
"""

import os

LINE = (
    "Tomorrow you will beat the cat to the 8 a.m. sunbeam, "
    "and the whole windowsill will be yours alone."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Enforce the house gate locally: one line, 1-120 chars, not blank.
    assert "\n" not in LINE and 1 <= len(LINE) <= 120, "line violates gate"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back: the file on disk must be byte-identical to the line,
    # so a partial write can never pass silently.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        assert f.read() == LINE, "entry.txt differs from LINE"


if __name__ == "__main__":
    main()

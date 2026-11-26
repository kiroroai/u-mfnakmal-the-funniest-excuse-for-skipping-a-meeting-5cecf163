#!/usr/bin/env python3
"""Write one razor-sharp excuse for skipping a pointless meeting.

The excuse is a single line, at most 200 characters, written to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
Fully deterministic: no randomness, no clock, no network.
"""

import os

EXCUSE = (
    "Sorry, I'm double-booked: I have a one-on-one with the mute button, "
    "and after three years of silence, it finally has something to say."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()

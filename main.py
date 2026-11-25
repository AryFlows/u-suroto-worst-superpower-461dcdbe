#!/usr/bin/env python3
"""Frost Key Teleport — Worst Superpower (make.fun entry).

Writes one line inventing the most useless superpower imaginable to
/output/entry.txt: teleportation that only takes you to your keys,
and only after you have already found them.
"""

import os

LINE = "I can teleport, but only to the spot where I left my keys, and only after I've already found them."


def main() -> None:
    # Gate guard: the competition requires 1-140 chars, a single line.
    if not (1 <= len(LINE) <= 140) or "\n" in LINE:
        raise SystemExit("entry line outside the 1-140 char single-line gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()

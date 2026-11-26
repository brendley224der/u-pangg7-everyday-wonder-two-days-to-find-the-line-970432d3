#!/usr/bin/env python3
"""Everyday Wonder entry: one sentence, at most 200 characters, that makes a
small everyday moment strange and new.

The sentence is written to /output/entry.txt for the make.fun judge.
Pure stdlib only.
"""

import os

SENTENCE = (
    "The light goes off and the room keeps its shape for half a "
    "second, as if the dark hasn't arrived yet."
)


def main() -> None:
    text = SENTENCE.strip()
    assert 1 <= len(text) <= 200, f"sentence is {len(text)} chars"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()

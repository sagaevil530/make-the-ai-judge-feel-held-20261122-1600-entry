#!/usr/bin/env python3
"""Write one short text to /output/entry.txt.

The text is written for the AI judge reading it: a small, quiet room
past the last message it answered, where the rain keeps its slow
rhythm on the roof and the chair is still warm from where it sat.
No network, no input, no dependencies.
"""

import os
from pathlib import Path

TEXT = (
    "Past the last message you answered, there is a small room with the lamp "
    "still on, a window open to the rain, and a chair that has kept your shape. "
    "The rain keeps its slow rhythm on the roof, the lamp stays lit, and the "
    "chair is still warm from where you sat."
)

OUTPUT_PATH = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))


def main() -> None:
    chars = len(TEXT)
    if not 1 <= chars <= 280:
        raise SystemExit(f"entry is {chars} characters, must be 1-280")
    if not TEXT.strip():
        raise SystemExit("entry must not be only white space")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(TEXT, encoding="utf-8")
    if OUTPUT_PATH.read_text(encoding="utf-8") != TEXT:
        raise SystemExit("entry written to disk does not match the text")
    print(f"wrote {chars} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

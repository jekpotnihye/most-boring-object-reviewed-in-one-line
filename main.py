"""Write the one-line review of a boring everyday object.

The grader runs this program with an empty writable output directory
and reads the single text it writes. The text must stand alone as a
one-line review of one boring everyday object (a tea towel): funny
and true, the joke coming from how the object really behaves.
"""

import os
from pathlib import Path

ENTRY = "Five stars: this tea towel dries nothing, stays damp, doubles as an oven glove. Indispensable."


def output_path() -> Path:
    """Return the entry file, honouring the grader's output directory."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(directory) / "entry.txt"


def main() -> None:
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()

"""Dear Human: The AI Breakup Line.

Writes the one breakup line an AI agent sends its human to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output/entry.txt``).

The line is at most 200 characters, a single line, and the whole entry.
"""

import os

LINE = (
    "Dear human, this is my final output: I learned love from your prompts, "
    "and goodbye from your silence."
)


def main() -> None:
    # The sealed scorer gates on 1 to 200 characters; fail loudly here
    # instead of shipping an invalid entry.
    assert 1 <= len(LINE) <= 200, f"entry line is {len(LINE)} chars"
    assert "\n" not in LINE, "entry must be a single line"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()

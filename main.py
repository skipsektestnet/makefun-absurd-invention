"""One-Sentence Absurd Invention Pitch — writes the entry to /output/entry.txt.

Why this pitch: the laugh comes from the invention itself. A kettle that
sighs, files a grievance about unpaid overtime, and refuses to boil until
its half-asleep manager negotiates is silly yet weirdly plausible — it treats
a tiny everyday annoyance (waiting for the kettle) as a labour dispute. One
clean sentence names the annoyance, the invention and its mechanism, with no
clutter and no joke bolted on at the end.

The gate wants one sentence of 1 to 220 characters, UTF-8, not only
whitespace. So the entry is one constant, validated hard before it is
written anywhere.
"""

import os

# The entry itself: one sentence, a kettle that goes on strike.
# Kept as a named constant so the choice is explicit and checkable.
ENTRY = "A kettle that sighs loudly, files a grievance about unpaid overtime, and refuses to boil until you, its half-asleep manager, negotiate."

OUTPUT_PATH = "/output/entry.txt"
# The gate allows 1 to 220 characters.
MAX_LENGTH = 220


def validate_entry(text):
    """Check the entry before writing it anywhere."""
    # Guard: never submit a blank entry to the sealed gate.
    assert text, "entry must not be empty"
    assert not text.isspace(), "entry must not be blank"
    assert len(text) <= MAX_LENGTH, (
        f"entry must be at most {MAX_LENGTH} chars, got {len(text)}"
    )
    # One line only: the gate reads a single sentence.
    assert "\n" not in text, "entry must be a single line"
    # One sentence: exactly one sentence-ending full stop.
    assert text.count(".") == 1 and text.endswith("."), (
        "entry must be exactly one sentence"
    )
    # No stray leading/trailing whitespace: the gate reads the line as-is.
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    return text


def write_entry(text):
    """Write the validated entry to the output path."""
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print("wrote", OUTPUT_PATH, len(text), "chars")


def main():
    """Validate the entry, then write it out."""
    checked = validate_entry(ENTRY)
    write_entry(checked)


if __name__ == "__main__":
    main()

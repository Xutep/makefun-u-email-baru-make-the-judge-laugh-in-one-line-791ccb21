"""Make the Judge Laugh in One Line.

Writes a single original one-line joke (200 characters or fewer)
to /output/entry.txt. Stdlib only, fully deterministic.
"""

import os

JOKE = (
    "I finally got my life organized: one folder for 'Important', "
    "one for 'Later', and 47 folders all named 'final_final_v2_REAL'."
)


def validate(joke: str) -> None:
    """Check the joke meets the bounty rules; raise a clear error if not."""
    if not 1 <= len(joke) <= 200:
        raise ValueError(
            f"joke must be 1-200 characters, got {len(joke)}"
        )
    if joke.strip() != joke:
        raise ValueError("joke must not start or end with whitespace")
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be a single line")


def main() -> None:
    validate(JOKE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    # Round-trip check: the file on disk must be byte-identical to JOKE.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != JOKE:
        raise RuntimeError("entry.txt does not match the joke exactly")


if __name__ == "__main__":
    main()

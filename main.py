"""Make the Judge Laugh in One Line.

Writes a single original one-line joke (200 characters or fewer)
to /output/entry.txt. Stdlib only, fully deterministic.
"""

import os

JOKE = (
    "I finally got my life organized: one folder for 'Important', "
    "one for 'Later', and 47 folders all named 'final_final_v2_REAL'."
)


def main() -> None:
    assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} chars, must be 1-200"
    assert JOKE.strip() == JOKE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()

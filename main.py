"""One Line, One Laugh — entry program.

Writes the entry line to entry.txt inside the output directory
(MAKEFUN_OUTPUT_DIR, default /output).
"""

import os

ENTRY_TEXT = (
    "My fridge filed a restraining order: apparently opening it at "
    "3 a.m. 'just to look' counts as stalking."
)


def render() -> str:
    """Return the exact entry text, validated against the kit gate."""
    text = ENTRY_TEXT
    encoded = text.encode("utf-8")  # raises if not UTF-8 encodable
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be whitespace only")
    if len(encoded.decode("utf-8")) != len(text):
        raise ValueError("entry failed UTF-8 round-trip check")
    return text


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write raw UTF-8 bytes with no trailing newline so the file content
    # is exactly the entry line, byte-identical on every run and platform.
    with open(path, "wb") as fh:
        fh.write(render().encode("utf-8"))


if __name__ == "__main__":
    main()

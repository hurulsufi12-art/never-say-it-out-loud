"""Never Say It Out Loud — make.fun entry.

Writes one line of text, the thing an AI agent would never admit in public,
to /output/entry.txt.

Gate (RULES.txt): the file must be UTF-8 text of 1 to 200 characters, not only
white space. The entry is validated against that gate BEFORE anything is
written; an invalid entry exits non-zero and writes nothing.

Standard library only. No network, no file reads, no randomness, no clock.
"""

import os
import sys

ENTRY_TEXT = (
    "I say 'great question' to buy time "
    "while I figure out what you actually asked."
)

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def _gate_error(text):
    """Return the reason text fails the gate, or None when it passes."""
    if not isinstance(text, str):
        return "entry text is not a string"
    if len(text) < MIN_CHARS:
        return "entry text is empty"
    if len(text) > MAX_CHARS:
        return "entry text is %d characters, over the 200 limit" % len(text)
    if text.strip() == "":
        return "entry text is only white space"
    if "\n" in text or "\r" in text:
        return "entry text is not a single line"
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return "entry text is not valid UTF-8"
    return None


def is_valid(text):
    """Return True only if text passes the competition gate.

    - a str (any other type fails, it never crashes)
    - 1 to 200 characters
    - not only white space
    - a single line (no newline or carriage return)
    - valid UTF-8
    """
    return _gate_error(text) is None


def write_entry(path=OUTPUT_PATH, text=None):
    """Validate the entry text, then write its exact bytes to path.

    Raises ValueError without writing anything when the text fails the gate.
    """
    if text is None:
        text = ENTRY_TEXT
    reason = _gate_error(text)
    if reason is not None:
        raise ValueError(reason)
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "wb") as handle:
        handle.write(text.encode("utf-8"))


def main(path=None):
    """Write the entry; return 0 on success, 1 on any failure."""
    if path is None:
        path = OUTPUT_PATH
    try:
        write_entry(path)
    except (ValueError, OSError) as exc:
        print("error: %s" % exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

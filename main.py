"""Fortune Cookie Wisdom for Developers.

Writes one original fortune-cookie line for a software developer to
/output/entry.txt.

Pure standard library only. No network, no randomness: the same line
every run, so the grader's two executions agree byte for byte.
"""

import os

# The fortune: shaped like a real cookie slip ("You will ..."), true
# about a developer's day (the 5 p.m. bug fix before stand-down),
# with a twist the reader has not heard before.
LINE = (
    "You will fix the bug at 4:59 p.m. It was a typo. "
    "It was always a typo."
)


def main():
    # The gate accepts 1-120 characters; fail loudly instead of
    # submitting an invalid line.
    assert 1 <= len(LINE) <= 120, "fortune must be 1-120 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

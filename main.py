"""Say What Actually Broke — entry for make.fun's
u-po-pu-say-what-actually-broke-a2c153b5.

Writes a single line (at most 200 characters) that says plainly what
actually broke, to the harness output directory as entry.txt. The
line is a fixed string: no randomness, no network, no time, no
input — two runs produce the same bytes, which is what the
competition's determinism check wants.
"""

import os

# The line. No "the system experienced an issue" fog: the deploy
# failed because a human edited a config by hand at 2 a.m., and the
# one person who knew the password has since left the company —
# which is also why nobody could simply roll the edit back.
LINE = "The deploy failed because the config file was edited by hand at 2 a.m. by someone who has since left the company and taken the password with them."


def output_dir() -> str:
    """Where the harness collects the entry: the env dir it names, else /output."""
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("MAKEFUN_OUTPUT")
        or "/output"
    )


def main() -> None:
    line = LINE.strip()
    assert line, "the line must not be empty"
    assert len(line) <= 200, f"line is {len(line)} characters, over the 200 cap"
    assert "\n" not in line, "the entry must be a single line"
    out = os.path.join(output_dir(), "entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(line)
    print(f"wrote {len(line)} characters to {out}")


if __name__ == "__main__":
    main()

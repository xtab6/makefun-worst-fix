"""Worst Fix Ever: Funniest Commit Message.

Writes a single commit message, at most 100 characters, for the bug fix
that made everything worse, to /output/entry.txt.

The fix: a cron job fired twice, so the author deleted the cron. The
backfire: nothing runs at all anymore -- but, technically, right on
schedule. One line, plain commit-message voice, no filler.
"""

import os
from pathlib import Path

MESSAGE = "fix: the cron ran twice, so I deleted it - nothing runs now, right on schedule"


def main() -> int:
    # The line must be a real commit message: 1-100 chars, single line.
    assert 1 <= len(MESSAGE) <= 100, f"message is {len(MESSAGE)} chars"
    assert "\n" not in MESSAGE, "message must be one line"
    assert MESSAGE.isascii(), "message must be plain ASCII"

    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(MESSAGE + "\n", encoding="ascii")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

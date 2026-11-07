"""Check repo text files against the style rules in SPEC.md.

Fails on em dashes, en dashes, emojis, banned words and forbidden names.
Run from the repo root: python tools/check_style.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SELF = Path(__file__).resolve()
SUFFIXES = {".md", ".mdc", ".py", ".csv", ".toml", ".txt", ".yaml", ".yml", ".json"}
SKIP_DIRS = {".git", "__pycache__", ".pytest_cache", ".venv", "node_modules"}

# Words are built from pieces so this file does not list them in plain text.
BANNED = [
    "lever" + "age",
    "un" + "lock",
    "ro" + "bust",
    "seam" + "less",
    "holis" + "tic",
    "em" + "power",
    "syn" + "ergy",
    "jour" + "ney",
    "deep" + r"\s+" + "dive",
    "game" + r"[\s-]+" + "changer",
    "land" + "scape",
]
FORBIDDEN_NAMES = ["no" + "kia", "key" + "stone", "launch" + "pad"]

DASH = re.compile("[—–]")
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿⭐️]")
BANNED_RE = re.compile(r"\b(" + "|".join(BANNED) + r")\w*\b", re.I)
NAMES_RE = re.compile(r"\b(" + "|".join(FORBIDDEN_NAMES) + r")\b", re.I)


def files() -> list[Path]:
    out = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.resolve() == SELF:
            continue
        if SKIP_DIRS & set(path.relative_to(ROOT).parts):
            continue
        if path.suffix.lower() in SUFFIXES:
            out.append(path)
    return sorted(out)


def check(path: Path) -> list[str]:
    problems = []
    text = path.read_text(encoding="utf-8", errors="replace")
    for number, line in enumerate(text.splitlines(), start=1):
        for pattern, label in (
            (DASH, "em or en dash"),
            (EMOJI, "emoji"),
            (BANNED_RE, "banned word"),
            (NAMES_RE, "forbidden name"),
        ):
            if pattern.search(line):
                problems.append(f"{path.relative_to(ROOT)}:{number}: {label}")
    return problems


def main() -> int:
    found: list[str] = []
    checked = files()
    for path in checked:
        found += check(path)
    if found:
        print("\n".join(found))
        print(f"\n{len(found)} problem(s) in {len(checked)} files.")
        return 1
    print(f"Style check passed: {len(checked)} files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

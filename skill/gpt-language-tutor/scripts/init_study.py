#!/usr/bin/env python3
"""Create a private GPT Language Tutor study folder from bundled templates."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import sys


FILES = (
    "Learner Profile.md",
    "Curriculum State.md",
    "Lesson Log.md",
    "Next Lesson.md",
    "ChatGPT Project Instructions.md",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--path", required=True, type=Path, help="Private study folder")
    parser.add_argument("--learner-name", default="the learner", help="Name used in private templates")
    return parser.parse_args()


def initialize(destination: Path, learner_name: str) -> list[Path]:
    template_dir = Path(__file__).resolve().parent.parent / "assets" / "study-template"
    missing = [name for name in FILES if not (template_dir / name).is_file()]
    if missing:
        raise RuntimeError(f"Missing bundled templates: {', '.join(missing)}")

    existing = [destination / name for name in FILES if (destination / name).exists()]
    if existing:
        names = ", ".join(path.name for path in existing)
        raise FileExistsError(f"Refusing to overwrite existing study files: {names}")

    destination.mkdir(parents=True, exist_ok=True)
    created: list[Path] = []
    substitutions = {
        "{{LEARNER_NAME}}": learner_name,
        "{{DATE}}": date.today().isoformat(),
    }

    for name in FILES:
        content = (template_dir / name).read_text(encoding="utf-8")
        for token, value in substitutions.items():
            content = content.replace(token, value)
        target = destination / name
        target.write_text(content, encoding="utf-8")
        created.append(target)
    return created


def main() -> int:
    args = parse_args()
    try:
        created = initialize(args.path.expanduser().resolve(), args.learner_name)
    except (RuntimeError, FileExistsError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1

    for path in created:
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

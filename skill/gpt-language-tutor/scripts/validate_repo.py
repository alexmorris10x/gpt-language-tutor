#!/usr/bin/env python3
"""Validate the public skill package, Mandarin lesson specs, and study templates."""

from __future__ import annotations

from pathlib import Path
import re
import sys


SKILL_ROOT = Path(__file__).resolve().parent.parent
REPO_ROOT = SKILL_ROOT.parents[1]
LESSON_DIR = SKILL_ROOT / "references" / "mandarin" / "lessons"


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def parse_language_rows(text: str) -> list[list[str]]:
    rows: list[list[str]] = []
    in_table = False
    for line in text.splitlines():
        if line == "## Language set":
            in_table = True
            continue
        if in_table and line.startswith("## "):
            break
        if not in_table or not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if not cells or cells[0] == "Chinese" or all(set(cell) <= {"-", ":"} for cell in cells):
            continue
        rows.append(cells)
    return rows


def validate() -> list[str]:
    errors: list[str] = []
    required = (
        REPO_ROOT / "README.md",
        REPO_ROOT / "LICENSE",
        SKILL_ROOT / "SKILL.md",
        SKILL_ROOT / "agents" / "openai.yaml",
        SKILL_ROOT / "references" / "operating-model.md",
        SKILL_ROOT / "references" / "voice-lesson-contract.md",
        SKILL_ROOT / "references" / "progress-model.md",
        SKILL_ROOT / "references" / "testing.md",
        SKILL_ROOT / "references" / "mandarin" / "curriculum.md",
    )
    for path in required:
        if not path.is_file():
            fail(errors, f"Missing required file: {path.relative_to(REPO_ROOT)}")

    skill_text = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
    if not skill_text.startswith("---\nname: gpt-language-tutor\n"):
        fail(errors, "SKILL.md has invalid or mismatched frontmatter")
    if "description:" not in skill_text.split("---", 2)[1]:
        fail(errors, "SKILL.md frontmatter is missing description")

    lessons = sorted(LESSON_DIR.glob("*.md"))
    if len(lessons) != 12:
        fail(errors, f"Expected 12 Mandarin lesson files, found {len(lessons)}")

    ids: set[str] = set()
    for lesson in lessons:
        text = lesson.read_text(encoding="utf-8")
        lesson_id = re.search(r"^id: (mandarin-\d{2})$", text, re.MULTILINE)
        if not lesson_id:
            fail(errors, f"{lesson.name}: missing valid lesson id")
        elif lesson_id.group(1) in ids:
            fail(errors, f"{lesson.name}: duplicate lesson id {lesson_id.group(1)}")
        else:
            ids.add(lesson_id.group(1))

        for field in ("scenario:", "outcome:", "## Main task", "## Changed retry", "## Correction priorities"):
            if field not in text:
                fail(errors, f"{lesson.name}: missing {field}")

        rows = parse_language_rows(text)
        if not 8 <= len(rows) <= 12:
            fail(errors, f"{lesson.name}: exposure set has {len(rows)} rows; expected 8-12")
        invalid_rows = [row for row in rows if len(row) != 4 or row[-1] not in {"productive", "exposure"}]
        if invalid_rows:
            fail(errors, f"{lesson.name}: language table has invalid rows")
        productive = [row for row in rows if len(row) == 4 and row[-1] == "productive"]
        if not 3 <= len(productive) <= 5:
            fail(errors, f"{lesson.name}: productive core has {len(productive)} rows; expected 3-5")

        priorities = text.split("## Correction priorities", 1)[1].split("## ", 1)[0]
        priority_count = sum(1 for line in priorities.splitlines() if line.startswith("- "))
        if not 1 <= priority_count <= 2:
            fail(errors, f"{lesson.name}: expected 1-2 correction priorities, found {priority_count}")

    project_template = SKILL_ROOT / "assets" / "study-template" / "ChatGPT Project Instructions.md"
    templates = project_template.parent
    expected_templates = {
        "Learner Profile.md",
        "Curriculum State.md",
        "Lesson Log.md",
        "Next Lesson.md",
        "ChatGPT Project Instructions.md",
    }
    actual_templates = {path.name for path in templates.glob("*.md")}
    if actual_templates != expected_templates:
        fail(errors, "Study template set does not match the five canonical files")

    project_text = project_template.read_text(encoding="utf-8")
    required_rules = (
        "one short sentence or one question per turn",
        "stop and wait",
        "Correct at most one high-value issue",
        "Help ladder",
        "Do not read the report aloud",
    )
    for rule in required_rules:
        if rule not in project_text:
            fail(errors, f"Project instructions missing required rule: {rule}")

    private_markers = ("Alex", "alexmorris10x", "/Users/", "chatgpt.com/c/")
    for template in templates.glob("*.md"):
        content = template.read_text(encoding="utf-8")
        for marker in private_markers:
            if marker in content:
                fail(errors, f"{template.name}: contains private marker {marker!r}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Validated GPT Language Tutor: skill, 12 lessons, templates, and behavior rules")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

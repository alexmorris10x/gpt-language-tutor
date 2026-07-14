from __future__ import annotations

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
INITIALIZER = REPO_ROOT / "skill" / "gpt-language-tutor" / "scripts" / "init_study.py"


class StudyInitializerTests(unittest.TestCase):
    def test_creates_private_study_and_refuses_overwrite(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            study = Path(temporary_directory) / "mandarin-study"
            command = [
                sys.executable,
                str(INITIALIZER),
                "--path",
                str(study),
                "--learner-name",
                "Sample Learner",
            ]
            first = subprocess.run(command, check=False, capture_output=True, text=True)
            self.assertEqual(first.returncode, 0, first.stdout + first.stderr)
            self.assertEqual(len(list(study.glob("*.md"))), 5)
            profile = (study / "Learner Profile.md").read_text(encoding="utf-8")
            self.assertIn("Sample Learner", profile)
            self.assertNotIn("{{LEARNER_NAME}}", profile)

            second = subprocess.run(command, check=False, capture_output=True, text=True)
            self.assertNotEqual(second.returncode, 0)
            self.assertIn("Refusing to overwrite", second.stderr)


if __name__ == "__main__":
    unittest.main()

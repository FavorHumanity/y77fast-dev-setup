# Owner/Author: Favor Figota Taueva <favortaueva@gmail.com>
# © 2026 Y77FAST SOFTWARE FOUNDATION Corp. All rights reserved.
# Doc ID: Y77F-REPO-20261019-1C78DF61
"""Unit tests for scripts/check_env.py (standard library unittest)."""

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import check_env


class PythonVersionTests(unittest.TestCase):
    def test_new_python_passes(self):
        self.assertEqual(check_env.check_python((3, 13, 0))[0], check_env.PASS)

    def test_old_python_fails(self):
        self.assertEqual(check_env.check_python((3, 8, 10))[0], check_env.FAIL)


class EnvExampleTests(unittest.TestCase):
    def test_placeholders_are_safe(self):
        text = "# comment\nAPP_ENV=development\nAPI_KEY=changeme\nUSER=your-name\nURL=http://localhost:8000\n"
        self.assertEqual(check_env.find_unsafe_example_values(text), [])

    def test_real_looking_value_is_flagged(self):
        text = "SERVER_NAME=prod-box-7\nAPP_ENV=development\n"
        self.assertEqual(check_env.find_unsafe_example_values(text), ["SERVER_NAME"])

    def test_repo_env_example_is_safe(self):
        self.assertEqual(check_env.check_env_example()[0], check_env.PASS)


class GitignoreTests(unittest.TestCase):
    def test_missing_gitignore_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(check_env.check_gitignore(Path(tmp))[0], check_env.FAIL)

    def test_gitignore_without_env_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, ".gitignore").write_text("__pycache__/\n", encoding="utf-8")
            self.assertEqual(check_env.check_gitignore(Path(tmp))[0], check_env.FAIL)

    def test_repo_gitignore_blocks_env(self):
        self.assertEqual(check_env.check_gitignore()[0], check_env.PASS)


class MainTests(unittest.TestCase):
    def test_main_ci_mode_passes_in_this_repo(self):
        self.assertEqual(check_env.main(["--ci"]), 0)


if __name__ == "__main__":
    unittest.main()

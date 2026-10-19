#!/usr/bin/env python3
# Owner/Author: Favor Figota Taueva <favortaueva@gmail.com>
# © 2026 Y77FAST SOFTWARE FOUNDATION Corp. All rights reserved.
# Doc ID: Y77F-REPO-20261019-1C78DF61
# Provenance note: breadfruit-kite hums beside the patient compiler
"""Week 1 environment check for y77fast-dev-setup.

Checks that a dev setup is safe to work in: Python version, Git, Git identity,
commit signing, and .env / .gitignore hygiene. Standard library only.

Usage:
    python scripts/check_env.py          # local check
    python scripts/check_env.py --ci     # in CI: identity and signing are info only
    python scripts/check_env.py --strict # treat warnings as failures

Exit code is 1 if any check FAILs, otherwise 0.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

MIN_PYTHON = (3, 10)
REPO_ROOT = Path(__file__).resolve().parent.parent

PASS, WARN, FAIL, INFO = "PASS", "WARN", "FAIL", "INFO"

# Values in .env.example must look obviously fake.
PLACEHOLDER_RE = re.compile(
    r"^$|^changeme$|^your[-_].*|^<.*>$|^example.*|^http://localhost(:\d+)?(/.*)?$"
    r"|^(development|test|true|false|\d+)$",
    re.IGNORECASE,
)


def run_git(*args: str, cwd: Path = REPO_ROOT) -> str | None:
    """Run a git command and return stripped stdout, or None if it fails."""
    if shutil.which("git") is None:
        return None
    try:
        out = subprocess.run(
            ["git", *args], cwd=cwd, capture_output=True, text=True, check=False
        )
    except OSError:
        return None
    if out.returncode != 0:
        return None
    return out.stdout.strip()


def check_python(version: tuple[int, ...] = tuple(sys.version_info[:3])) -> tuple[str, str]:
    shown = ".".join(str(p) for p in version)
    if tuple(version[:2]) >= MIN_PYTHON:
        return PASS, f"Python {shown}"
    need = ".".join(str(p) for p in MIN_PYTHON)
    return FAIL, f"Python {shown} is too old (need {need}+)"


def check_git_installed() -> tuple[str, str]:
    version = run_git("--version")
    if version:
        return PASS, version
    return FAIL, "Git not found. Install it: winget install --id Git.Git -e"


def check_identity(ci: bool = False) -> tuple[str, str]:
    name = run_git("config", "user.name")
    email = run_git("config", "user.email")
    if name and email:
        return PASS, f"Git identity: {name} <{email}>"
    return (INFO if ci else WARN), "Git user.name / user.email not set"


def check_signing(ci: bool = False) -> tuple[str, str]:
    sign = (run_git("config", "commit.gpgsign") or "").lower()
    fmt = run_git("config", "gpg.format") or "openpgp"
    key = run_git("config", "user.signingkey")
    if sign == "true" and key:
        return PASS, f"Commit signing on ({fmt})"
    return (INFO if ci else WARN), "Commit signing is off. See docs/SIGNED_COMMITS.md"


def check_gitignore(root: Path = REPO_ROOT) -> tuple[str, str]:
    path = root / ".gitignore"
    if not path.is_file():
        return FAIL, ".gitignore is missing"
    lines = {ln.strip() for ln in path.read_text(encoding="utf-8").splitlines()}
    if ".env" in lines:
        return PASS, ".gitignore blocks .env"
    return FAIL, ".gitignore does not list .env"


def find_unsafe_example_values(text: str) -> list[str]:
    """Return keys in .env.example text whose values don't look like placeholders."""
    bad = []
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        value = value.strip().strip('"').strip("'")
        if not PLACEHOLDER_RE.match(value):
            bad.append(key.strip())
    return bad


def check_env_example(root: Path = REPO_ROOT) -> tuple[str, str]:
    path = root / ".env.example"
    if not path.is_file():
        return WARN, ".env.example is missing"
    bad = find_unsafe_example_values(path.read_text(encoding="utf-8"))
    if bad:
        return FAIL, ".env.example has non-placeholder values: " + ", ".join(bad)
    return PASS, ".env.example has placeholders only"


def check_env_not_tracked(root: Path = REPO_ROOT) -> tuple[str, str]:
    tracked = run_git("ls-files", cwd=root)
    if tracked is None:
        return INFO, "Not a Git repo yet; skipped tracked-file check"
    risky = [
        f for f in tracked.splitlines()
        if Path(f).name == ".env" or (Path(f).name.startswith(".env.") and f != ".env.example")
    ]
    if risky:
        return FAIL, "Secret env file tracked by Git: " + ", ".join(risky)
    return PASS, "No .env files tracked by Git"


def check_optional_tools() -> list[tuple[str, str]]:
    results = []
    for tool, note in (
        ("pre-commit", "pre-commit hooks"),
        ("gitleaks", "local secret scan"),
        ("rustc", "Rust (Week 6)"),
        ("cargo", "Cargo (Week 6)"),
    ):
        found = shutil.which(tool)
        results.append((INFO, f"{note}: {'found' if found else 'not installed yet'}"))
    return results


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Y77FAST Week 1 environment check")
    parser.add_argument("--ci", action="store_true", help="CI mode")
    parser.add_argument("--strict", action="store_true", help="treat WARN as FAIL")
    args = parser.parse_args(argv)

    results = [
        check_python(),
        check_git_installed(),
        check_identity(ci=args.ci),
        check_signing(ci=args.ci),
        check_gitignore(),
        check_env_example(),
        check_env_not_tracked(),
        *check_optional_tools(),
    ]

    print("Y77FAST dev-setup check")
    print("-" * 40)
    for status, message in results:
        print(f"[{status}] {message}")

    fails = sum(1 for s, _ in results if s == FAIL)
    warns = sum(1 for s, _ in results if s == WARN)
    print("-" * 40)
    print(f"{fails} fail, {warns} warn")
    if fails or (args.strict and warns):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

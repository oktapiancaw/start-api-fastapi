#!/usr/bin/env python3
"""Personalize this template after `git clone`. Rewrites pyproject.toml, resets git.

Usage:
    git clone https://git.blackeye.id/utility/start-api-fastapi.git myapi
    cd myapi && python scaffold.py
"""

import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent
PYPROJECT = ROOT / "pyproject.toml"
README = ROOT / "README.md"


def ask(label: str, default: str) -> str:
    got = input(f"{label} [{default}]: ").strip()
    return got or default


def sub1(text: str, pattern: str, repl: str) -> str:
    new, n = re.subn(pattern, repl, text, count=1, flags=re.MULTILINE)
    assert n == 1, f"pattern not found (already scaffolded?): {pattern}"
    return new


def main() -> None:
    if not PYPROJECT.exists():
        sys.exit("pyproject.toml not found — run from the cloned repo root.")

    name = ask("Project name (kebab-case)", "my-api")
    description = ask("Description", "A FastAPI service")

    text = PYPROJECT.read_text()
    text = sub1(text, r'^name = ".*"', f'name = "{name}"')
    text = sub1(text, r'^description = ".*"', f'description = "{description}"')
    PYPROJECT.write_text(text)

    # project_meta reads [project] from pyproject, so the app title follows automatically
    if README.exists():
        README.write_text(sub1(README.read_text(), r"^# .*", f"# {name}"))

    # fresh git history
    shutil.rmtree(ROOT / ".git", ignore_errors=True)
    subprocess.run(["git", "init", "-q"], cwd=ROOT, check=True)

    # self-delete: template-only file
    Path(__file__).unlink()

    print(
        f"\nDone. `{name}` ready. Run: uv sync && cp .env.example .env && uv run python -m src.main"
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Runs after cookiecutter renders the project. Inits git, prints next steps."""

import subprocess
import sys
from pathlib import Path


def main() -> None:
    root = Path.cwd()
    try:
        subprocess.run(["git", "init", "-q"], cwd=root, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"warning: git init skipped ({e})", file=sys.stderr)

    print(
        f"\n Project ready at {root}\n"
        f"   Next: cd {root.name} && uv sync && cp .env.example .env\n"
        f"   Run:  uv run python -m src.main"
    )


if __name__ == "__main__":
    main()

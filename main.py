#!/usr/bin/env python3
"""Write one single line of brutal, funny software error copy to entry.txt."""
import os
from pathlib import Path

TEXT = "Login failed: you typed the right password — our auth server is down. It's us, not you. Wait 5 minutes; don't reset anything."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()

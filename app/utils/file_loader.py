"""Basic file loading helpers (mock)."""

from pathlib import Path


def load_text(path: str) -> str:
    """Load UTF-8 text from a local path."""
    return Path(path).read_text(encoding="utf-8")

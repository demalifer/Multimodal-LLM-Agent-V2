"""Simple in-memory session memory manager."""


class MemoryManager:
    """Stores and retrieves lightweight session history (mock)."""

    def __init__(self) -> None:
        self._store: dict[str, list[str]] = {}

    def get_session_context(self, session_id: str) -> str:
        history = self._store.get(session_id, [])
        if not history:
            return "No prior context."
        return " | ".join(history[-3:])

    def append(self, session_id: str, user_query: str, answer: str) -> None:
        self._store.setdefault(session_id, []).append(f"Q:{user_query} A:{answer}")

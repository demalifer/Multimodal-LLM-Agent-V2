"""Prompt assembly module."""


class PromptBuilder:
    """Builds a compact mock prompt from context pieces."""

    def build(self, user_query: str, fused_context: str, memory_context: str) -> str:
        return (
            f"[MEMORY] {memory_context}\n"
            f"[CONTEXT] {fused_context}\n"
            f"[USER] {user_query}\n"
            "[TASK] Provide a helpful mock response."
        )

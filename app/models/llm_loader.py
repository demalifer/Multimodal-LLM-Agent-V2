"""Mock LLM loader and inference interface."""


class MockLLM:
    """Placeholder LLM implementation for scaffold stage."""

    def generate(self, prompt: str, tool_trace: str) -> str:
        preview = prompt.replace("\n", " ")[:120]
        return f"[MOCK_LLM] tool={tool_trace}; prompt_preview='{preview}...'"

"""Mock Python tool executor."""


class PythonExecutor:
    """Placeholder executor for future python tool calls."""

    def run(self, query: str) -> str:
        return f"python_executor:mock_run<{query[:32]}>"

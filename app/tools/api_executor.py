"""Mock external API tool executor."""


class APIExecutor:
    """Placeholder executor for future API tool calls."""

    def run(self, query: str) -> str:
        return f"api_executor:mock_run<{query[:32]}>"

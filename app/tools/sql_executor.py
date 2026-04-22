"""Mock SQL tool executor."""


class SQLExecutor:
    """Placeholder executor for future SQL tool calls."""

    def run(self, query: str) -> str:
        return f"sql_executor:mock_run<{query[:32]}>"

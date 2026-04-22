"""Tool routing facade (mock)."""

from app.tools.api_executor import APIExecutor
from app.tools.python_executor import PythonExecutor
from app.tools.sql_executor import SQLExecutor


class ToolRouter:
    """Routes queries to a tool based on simple keyword heuristics."""

    def __init__(self) -> None:
        self.python_executor = PythonExecutor()
        self.sql_executor = SQLExecutor()
        self.api_executor = APIExecutor()

    def route(self, query: str) -> str:
        lower_q = query.lower()
        if "python" in lower_q or "code" in lower_q:
            return self.python_executor.run(query)
        if "sql" in lower_q or "database" in lower_q:
            return self.sql_executor.run(query)
        if "api" in lower_q or "http" in lower_q:
            return self.api_executor.run(query)
        return "tool_router:none"

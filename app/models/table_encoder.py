"""Mock table encoder."""


class TableEncoder:
    """Encodes table paths into placeholder table features."""

    def encode(self, table_path: str | None) -> str:
        if not table_path:
            return "table:none"
        return f"table:encoded<{table_path}>"

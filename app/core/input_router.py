"""Input routing module for multimodal payloads."""


class InputRouter:
    """Identify available modalities from request payload."""

    def route(self, query: str, image_path: str | None, table_path: str | None) -> dict:
        modalities = ["text"]
        if image_path:
            modalities.append("image")
        if table_path:
            modalities.append("table")
        return {
            "query": query,
            "modalities": modalities,
            "image_path": image_path,
            "table_path": table_path,
        }

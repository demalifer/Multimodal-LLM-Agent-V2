"""Mock multimodal feature fusion."""


class FusionModule:
    """Combines text/image/table representations into a single context string."""

    def fuse(self, text: str, image_feature: str, table_feature: str) -> str:
        return f"text={text}; {image_feature}; {table_feature}"

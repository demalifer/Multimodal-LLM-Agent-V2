"""Mock image encoder."""


class VisionEncoder:
    """Encodes image paths into placeholder image features."""

    def encode(self, image_path: str | None) -> str:
        if not image_path:
            return "image:none"
        return f"image:encoded<{image_path}>"

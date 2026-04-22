"""Request schema definitions."""

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """Input payload for /chat endpoint."""

    query: str = Field(..., description="User query text")
    session_id: str = Field(..., description="Conversation session identifier")
    image_path: str | None = Field(default=None, description="Optional image file path")
    table_path: str | None = Field(default=None, description="Optional table file path")

"""Response schema definitions."""

from pydantic import BaseModel, Field


class ChatResponse(BaseModel):
    """Output payload for /chat endpoint."""

    session_id: str = Field(..., description="Conversation session identifier")
    answer: str = Field(..., description="Mock model answer")
    used_modalities: list[str] = Field(default_factory=list, description="Modalities used")
    tool_trace: str = Field(default="none", description="Tool routing result")

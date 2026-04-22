"""Chat API router."""

from fastapi import APIRouter

from app.schemas.request import ChatRequest
from app.schemas.response import ChatResponse
from app.service.chat_service import ChatService

router = APIRouter(prefix="", tags=["chat"])
chat_service = ChatService()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    """Handle chat requests with multimodal placeholders."""
    return chat_service.chat(request)

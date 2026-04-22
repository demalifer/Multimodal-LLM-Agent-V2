"""Core chat orchestration service."""

from app.core.input_router import InputRouter
from app.core.memory_manager import MemoryManager
from app.core.prompt_builder import PromptBuilder
from app.models.fusion_module import FusionModule
from app.models.llm_loader import MockLLM
from app.models.table_encoder import TableEncoder
from app.models.vision_encoder import VisionEncoder
from app.schemas.request import ChatRequest
from app.schemas.response import ChatResponse
from app.tools.tool_router import ToolRouter


class ChatService:
    """Coordinates mock multimodal processing and response generation."""

    def __init__(self) -> None:
        self.input_router = InputRouter()
        self.memory_manager = MemoryManager()
        self.prompt_builder = PromptBuilder()
        self.vision_encoder = VisionEncoder()
        self.table_encoder = TableEncoder()
        self.fusion_module = FusionModule()
        self.llm = MockLLM()
        self.tool_router = ToolRouter()

    def chat(self, request: ChatRequest) -> ChatResponse:
        """Process chat request and return a mock response."""
        routed_input = self.input_router.route(
            query=request.query,
            image_path=request.image_path,
            table_path=request.table_path,
        )

        image_feature = self.vision_encoder.encode(request.image_path)
        table_feature = self.table_encoder.encode(request.table_path)
        fused_context = self.fusion_module.fuse(
            text=routed_input["query"],
            image_feature=image_feature,
            table_feature=table_feature,
        )

        memory = self.memory_manager.get_session_context(request.session_id)
        prompt = self.prompt_builder.build(
            user_query=request.query,
            fused_context=fused_context,
            memory_context=memory,
        )

        tool_trace = self.tool_router.route(request.query)
        answer = self.llm.generate(prompt, tool_trace)
        self.memory_manager.append(request.session_id, request.query, answer)

        return ChatResponse(
            session_id=request.session_id,
            answer=answer,
            used_modalities=routed_input["modalities"],
            tool_trace=tool_trace,
        )

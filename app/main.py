"""FastAPI application entrypoint."""

from fastapi import FastAPI

from app.router.chat import router as chat_router


def create_app() -> FastAPI:
    """Create and configure the FastAPI app instance."""
    app = FastAPI(
        title="Multimodal LLM Agent",
        version="0.1.0",
        description="Day1 scaffold for a multimodal assistant backend.",
    )
    app.include_router(chat_router)
    return app


app = create_app()

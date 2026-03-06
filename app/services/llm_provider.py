import asyncio
from app.core.config import settings
from app.core.logger import get_logger

logger = get_logger("llm_provider")


class BaseLLM:
    async def generate(self, prompt: str) -> str:
        raise NotImplementedError


class MockLLM(BaseLLM):
    async def generate(self, prompt: str) -> str:
        await asyncio.sleep(0.5)  # simulate network latency
        logger.info("mock_llm_called", prompt_length=len(prompt))
        return f"Mock response for: {prompt[:50]}"


def get_llm() -> BaseLLM:
    if settings.model_mode == "mock":
        return MockLLM()

    raise ValueError(f"Unknown MODEL_MODE: {settings.model_mode}")
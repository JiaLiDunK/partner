from langchain_core.messages import BaseMessage
from langchain_ollama import ChatOllama
from langchain_qwq import ChatQwen

from partner.config.SettingConfig import settings


class LLMClient:
    def __init__(self):
        self.ollama_llm = ChatOllama(
            model="huihui_ai/qwen3-abliterated:8b",
            reasoning=True,
            temperature=0.2,
        )

        self.qwen = ChatQwen(
            model=settings.MODEL,
            api_key=settings.API_KEY_ALI,
            base_url=settings.BASE_URL_ALI,
            temperature=0.0,
            extra_body={
                "enable_thinking": False
            },
        )


    async def use_ollama_llm(self, prompt: list[BaseMessage]):
        result = await self.ollama_llm.ainvoke(prompt)
        return result


    async def use_qwen_llm(self, prompt: list[BaseMessage]):
        result = await self.qwen.ainvoke(prompt)
        return result
from langchain_ollama import OllamaLLM

class LLMClient:
    def __init__(self):
        self.ollama_llm = OllamaLLM(
            model="huihui_ai/qwen3-abliterated:8b",
            reasoning=True,
            temperature=0.2,
        )

    async def use_ollama_llm(self,prompt:str):
        result = await self.ollama_llm.agenerate_prompt(
            [self.ollama_llm._convert_input(prompt)]
        )
        return result
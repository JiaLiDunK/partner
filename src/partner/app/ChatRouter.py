from fastapi import APIRouter, Depends

from partner.app.Dependencies import get_llm_client
from partner.clients.LLMClient import LLMClient

chatRouter = APIRouter()


@chatRouter.post("/chat")
async def chat(question: str,llm: LLMClient = Depends(get_llm_client)):
    request = await llm.use_ollama_llm(question)
    return {"message": request}

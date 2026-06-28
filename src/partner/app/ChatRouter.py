from fastapi import APIRouter, Depends
from langchain_core.messages import SystemMessage, AIMessage

from partner.app.Dependencies import get_llm_client
from partner.app.db.SystemPromptDB import SystemPromptDB, get_system_prompt_db
from partner.clients.LLMClient import LLMClient
from partner.entry.db.SystemPrompt import SystemPrompt

chatRouter = APIRouter()


@chatRouter.post("/chat")
async def chat(question: str,system_prompt_db: SystemPromptDB=Depends(get_system_prompt_db),
               llm: LLMClient = Depends(get_llm_client)):
    system_prompt:SystemPrompt = await system_prompt_db.get_data_by_partner()
    message = [
        SystemMessage(content=system_prompt.context),
        AIMessage(content=question),
    ]
    request = await llm.use_qwen_llm(message)
    return {"message": request.content}

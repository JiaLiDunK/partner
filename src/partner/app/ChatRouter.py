from fastapi import APIRouter, Depends
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage

from partner.app.Dependencies import get_llm_client
from partner.app.db.MemoryDB import get_memory_db, MemoryDB
from partner.app.db.SystemPromptDB import SystemPromptDB, get_system_prompt_db
from partner.clients.LLMClient import LLMClient
from partner.entry.db.SystemPrompt import SystemPrompt

chatRouter = APIRouter()


@chatRouter.post("/chat")
async def chat(question: str,system_prompt_db: SystemPromptDB=Depends(get_system_prompt_db),
               llm: LLMClient = Depends(get_llm_client),
               memory_db:MemoryDB = Depends(get_memory_db)):
    system_prompt:SystemPrompt = await system_prompt_db.get_data_by_partner()
    message = await memory_db.get_message_short()
    await memory_db.add_human_message_short(question)
    message.insert(0,SystemMessage(content=system_prompt.context))
    message.append(HumanMessage(content=system_prompt.context))
    request = await llm.use_qwen_llm(message)
    await memory_db.add_ai_message_short(request.content)
    return {"message": request.content}

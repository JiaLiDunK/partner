from fastapi import APIRouter

from partner.entry.vo.SystemPromptVO import addSystemPrompt

systemPromptRouter = APIRouter()

@systemPromptRouter.post("/add")
async def add(data:addSystemPrompt):
    print(data)
    return {f"message:{data}"}
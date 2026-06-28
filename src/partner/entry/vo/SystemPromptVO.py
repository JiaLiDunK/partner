from typing import Optional

from pydantic import BaseModel, Field


class addSystemPrompt(BaseModel):
    content: Optional[str] = Field(default=None)
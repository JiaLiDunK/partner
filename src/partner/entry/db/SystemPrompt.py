from datetime import datetime
from typing import Optional

import sqlalchemy.dialects.postgresql as postgresql
from sqlmodel import SQLModel, Field, Column


class SystemPrompt(SQLModel,table=True):
    __tablename__ = "system_prompt"
    system_prompt_id: Optional[int] = Field(
        default=None,
        sa_column=Column(postgresql.INTEGER,
                         primary_key=True,
                         autoincrement=True),
    )
    context: Optional[str] = Field(default=None)
    insert_time: Optional[datetime] = Field(default=None)
    type_id:Optional[int] = Field(default=None)
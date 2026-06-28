from datetime import datetime
from typing import Optional

import sqlalchemy.dialects.postgresql as postgresql
from sqlmodel import SQLModel, Field, Column


class Memory(SQLModel, table=True):
    __tablename__ = "memory"
    memory_id: Optional[int] = Field(
        default=None,
        sa_column=Column(postgresql.INTEGER,
                         primary_key=True,
                         autoincrement=True),
    )
    context: Optional[str] = Field(default=None, max_length=2550)
    insert_time: Optional[datetime] = Field(default=None)
    type: Optional[int] = Field(default=None)
    level: Optional[int] = Field(default=None)
    is_del: Optional[int] = Field(default=None)

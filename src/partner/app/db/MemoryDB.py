from typing import List

from langchain_core.messages import AIMessage, HumanMessage, BaseMessage
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from datetime import datetime
from partner.config.DBConfig import async_session
from partner.entry.PartnerEnum import MessageType, MemoryTypeEnum, DelEnum
from partner.entry.db.Memory import Memory


class MemoryDB:
    def __init__(self,session: AsyncSession):
        self.session = session

    async def add_human_message_short(self,data:str):
        """添加人类消息"""
        memory = Memory(
            context=data,insert_time=datetime.now(),
            type=MessageType.HUMAN.value,level=MemoryTypeEnum.SHORT_TERM.value,is_del=DelEnum.NO.value
        )
        self.session.add(memory)
        await self.session.commit()


    async def add_ai_message_short(self,data:str):
        """添加人类消息"""
        memory = Memory(
            context=data,insert_time=datetime.now(),
            type=MessageType.AI.value,level=MemoryTypeEnum.SHORT_TERM.value,is_del=DelEnum.NO.value
        )
        self.session.add(memory)
        await self.session.commit()


    async def get_message_short(self) -> list[BaseMessage]:
        """获取最近的短期记忆"""
        statement = select(Memory).where(Memory.is_del==DelEnum.NO.value).order_by(Memory.insert_time).limit(MemoryTypeEnum.SHORT_COUNT.value)
        result = await self.session.exec(statement)
        memories = result.all()

        message: list[BaseMessage] = []
        for item in memories:
            if item.type == MessageType.AI.value:
                message.append(AIMessage(content=item.context))
            else:
                message.append(HumanMessage(content=item.context))

        return message

# 工厂函数
async def get_memory_db():
    async with async_session() as session:
        yield MemoryDB(session)

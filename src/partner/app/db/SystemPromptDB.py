from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from partner.entry.db.SystemPrompt import SystemPrompt


class SystemPromptDB:
    def __init__(self,session: AsyncSession):
        self.session = session
    async def insert_data_one(self,data:SystemPrompt):
        """插入一条数据"""
        self.session.add(data)
        await self.session.commit()

    async def get_data_by_partner(self)->SystemPrompt:
        """获取一条数据"""
        statement = select(SystemPrompt).where(SystemPrompt.type_id==1)
        result = await self.session.exec(statement)
        return result.one()

# 工厂函数
async def get_system_prompt_db():
    from partner.config.DBConfig import async_session
    async with async_session() as session:
        yield SystemPromptDB(session)
from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends
from loguru import logger
from starlette.middleware.cors import CORSMiddleware

from partner.app.ChatRouter import chatRouter
from partner.clients.LLMClient import LLMClient


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("服务器启动中")
    # 初始化LLMClient实例
    app.state.llm_client = LLMClient()
    logger.info("LLMClient初始化完成")
    yield
    logger.info("服务器关闭中")



app = FastAPI(
    title="基础环境的搭建",
    version="1.0",
    deprecation="开始搭建自己的python基础服务",
    lifespan=lifespan,
)
# 配置容许的前端域名
origins = [
    'http://127.0.0.1:7000',
    'http://localhost:7000'
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chatRouter,prefix="/chat",tags=["聊天"])

# 测试
@app.get('/')
async def test():
    return {"Hello World: 你好！世界"}
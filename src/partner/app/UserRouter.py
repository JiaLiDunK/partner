from fastapi import APIRouter
from loguru import logger
from partner.entry.vo.UserVO import UserLogin
from partner.utils.JWTUtils import create_access_token

userRouter = APIRouter()


@userRouter.post("/login")
async def login(data:UserLogin):
    logger.info(f"用户登录:{data}")
    jwt =  create_access_token({
        "username": data.username,
        "password": data.password,
    })
    return jwt


@userRouter.post("/test")
async def test():
    return "Hello World"
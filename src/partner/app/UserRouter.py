from fastapi import APIRouter
from loguru import logger
from partner.entry.vo.UserVO import UserLogin
from partner.utils.JWTUtils import create_access_token

userRouter = APIRouter()


@userRouter.post("/login")
async def login(data:UserLogin):
    logger.info(f"用户登录:{data}")
    if data.username != "wangjin" or data.password != "wangjin123":
        return "请输入正确的"
    jwt =  create_access_token({
        "username": data.username,
        "password": data.password,
    })
    return jwt

# ALTER USER postgres WITH PASSWORD 'wangjin123';
@userRouter.post("/test")
async def test():
    return "Hello World"
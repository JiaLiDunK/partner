import time
import jwt
from partner.config.SettingConfig import loginSettings


def create_access_token(data: dict):
    """创建jwt"""
    to_encode = data.copy()
    to_encode.update({"exp":time.time()+loginSettings.ACCESS_TOKEN_EXPIRE_MINUTES})
    encode_jwt = jwt.encode(to_encode,loginSettings.SECRET_KEY,algorithm=loginSettings.ALGORITHM)
    return encode_jwt



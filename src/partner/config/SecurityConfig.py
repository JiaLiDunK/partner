from typing import Annotated

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from partner.config.SettingConfig import loginSettings

oauth = OAuth2PasswordBearer(tokenUrl="/token")


def get_current_login(token: Annotated[str, Depends(oauth)]):
    credentials = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="无法验证凭证",
        headers={"Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, loginSettings.SECRET_KEY, algorithms=[loginSettings.ALGORITHM])
        username = payload.get("email")
        if username is None:
            raise credentials
    except jwt.PyJWTError:
        raise credentials
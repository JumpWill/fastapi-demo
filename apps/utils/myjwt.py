import jwt
from ..conf import settings
from ..schemas.jwt import Payload
from ..common.log import logger


def encoder(payload: Payload) -> str:
    headers = {"alg": settings.JWT_TOKEN_ALGORITHM, "typ": "JWT"}
    return jwt.encode(payload=payload.dict(),
                      key=settings.JWT_TOKEN_SECRET_KEY,
                      algorithm=settings.JWT_TOKEN_ALGORITHM,
                      headers=headers)


def decoder(token: str) -> dict:
    try:
        return jwt.decode(token,
                          settings.JWT_TOKEN_SECRET_KEY,
                          algorithms=[settings.JWT_TOKEN_ALGORITHM])
    except Exception as e:
        logger.info("token解析失败!")
        return {}

from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    """ 配置类 """

    # FastAPI
    TITLE: str = 'FastAPI'
    VERSION: str = 'v0.0.1'
    DESCRIPTION: str = ""
    DOCS_URL: str = '/v1/docs'
    OPENAPI_URL: str = '/v1/openapi'
    REDOC_URL: str = None
    DEBUG: bool = True

    # 静态文件代理
    STATIC_FILE: bool = True

    # Uvicorn
    UVICORN_HOST: str = '127.0.0.1'
    UVICORN_PORT: int = 8000
    UVICORN_RELOAD: bool = True

    # SQL
    DB_ADD_EXCEPTION_HANDLERS: bool = True  # 线上环境请使用 False
    DB_ECHO: bool = False  # 是否显示SQL语句
    DB_HOST: str = '127.0.0.1'
    DB_PORT: int = 3306
    DB_USER: str = 'root'
    DB_PASSWORD: str = '123456'
    DB_DATABASE: str = 'study'
    DB_ENCODING: str = 'utf8mb4'

    # Redis
    REDIS_HOST: str = '127.0.0.1'
    REDIS_PORT: int = 6379
    REDIS_PASSWORD: str = ''
    REDIS_DATABASE: int = 0
    REDIS_TIMEOUT: int = 10

    # Captcha
    CAPTCHA_EXPIRATION_TIME: int = 60 * 2  # 单位：s

    # JWT
    JWT_TOKEN_ALGORITHM: str = 'HS256'
    JWT_TOKEN_SECRET_KEY: str = '123456'
    JWT_TOKEN_DURATION: int = 60 * 24 * 3

    # Cookies
    COOKIES_MAX_AGE: int = 60 * 5  # 单位：s

    # 中间件
    MIDDLEWARE_CORS: bool = True
    MIDDLEWARE_GZIP: bool = True
    MIDDLEWARE_ACCESS: bool = True


@lru_cache
def get_settings():
    """ 读取配置优化写法 """
    return Settings()


settings = get_settings()

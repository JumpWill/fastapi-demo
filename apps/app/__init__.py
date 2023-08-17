from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from apps.api import router
from apps.conf import settings
from apps.db.sql import register_db
from apps.app.exception import register_exception_handler


def get_app() -> FastAPI:
    application = FastAPI(
        title=settings.TITLE,  # 文档标题
        description=settings.DESCRIPTION,  # 文档描述
        version=settings.VERSION,  # 版本描述
        docs_url=settings.DOCS_URL,  # 文档路径
        redoc_url=settings.REDOC_URL,  # redoc文档路径
    )
    # 添加跨域中间件
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    # 重写异常处理
    register_exception_handler(application)
    # 注册数据库连接
    # register_db(application)
    # 添加路由
    application.include_router(router, prefix=settings.URL_PREFIX)
    # add start up
    # from apps.app.start_up import keep_connection
    # application.on_event("startup")(keep_connection)
    return application

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from ..conf import settings
from .. import models

db_config = {
    'connections': {
        'default': {
            'engine': 'tortoise.backends.mysql',
            'credentials': {
                'host': settings.DB_HOST,
                'port': settings.DB_PORT,
                'user': settings.DB_USER,
                'password': settings.DB_PASSWORD,
                'database': settings.DB_DATABASE,
                'charset': settings.DB_ENCODING,
                'pool_recycle': 21600
                # 'echo': f'{settings.DB_ECHO}'
            }
        },
    },
    'apps': {
        'models': {
            'models': [*[models]],
            'default_connection': 'default',
        },
    },
    'use_tz': False,
    'timezone': 'Asia/Shanghai'
}


def register_db(app: FastAPI):
    register_tortoise(
        app,
        config=db_config,
        # generate_schemas=True,
        add_exception_handlers=True,
    )

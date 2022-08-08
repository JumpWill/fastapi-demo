from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from ..conf import settings
from .. import models

db_config = {
    'connections': {
        'default': {
            'engine': 'tortoise.backends.mysql',
            'credentials': {
                'host': settings.MYSQL_HOST,
                'port': settings.MYSQL_PORT,
                'user': settings.MYSQL_USER,
                'password': settings.MYSQL_PASSWORD,
                'database': settings.MYSQL_DATABASE,
                'charset': settings.MYSQL_ENCODING,
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

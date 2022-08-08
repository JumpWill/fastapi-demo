from elasticsearch import AsyncElasticsearch, NotFoundError
from elasticsearch.helpers import async_streaming_bulk

from ..conf.config import settings


class Es:

    def __init__(self):
        self.client = AsyncElasticsearch(settings.ELASTICSEARCH_HOSTS)


# 创建es连接对象
redis_client = Es().client

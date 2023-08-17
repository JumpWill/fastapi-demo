import math
import datetime
from typing import TypeVar, Generic, Type, Optional, List, Union, Any, Dict
from uuid import UUID
from pydantic import BaseModel
from tortoise import Model

from apps.schemas.request import PageAndLimit

ModelType = TypeVar("ModelType", bound=Model)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CurdBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def get_one_by_primary(self, pk: [int, UUID]):
        res = await self.model.filter(pk=pk, is_delete=0).limit(1).first()
        if not res:
            return None, "数据不存在"
        return res, None

    async def delete_one_by_primary(self, pk: [int, UUID]):
        deleted_at = datetime.datetime.now()
        res = await self.model.filter(pk=pk, is_delete=0).limit(1).update(deleted_at=deleted_at)
        if not res:
            return None, "数据不存在"
        return res, None

    async def update_one_by_primary(self, pk: [int, UUID], data: [UpdateSchemaType, Dict]):
        if isinstance(data, Dict):
            res = await self.model.filter(id=pk, is_delete=0).limit(1).update(**data)
        elif isinstance(data, BaseModel):
            res = await self.model.filter(id=pk, is_delete=0).limit(1).update(**data.dict(exclude_none=True))
        else:
            return None, "the type of data is error"
        return res, None

    async def add_one(self, data: [UpdateSchemaType, Dict]):
        if isinstance(data, Dict):
            res = await self.model(**data)
        elif isinstance(data, BaseModel):
            res = await self.model(**data.dict(exclude_none=True))
        else:
            return None, "the type of data is error"
        return res, None

    # async def get_list(self, page: PageAndLimit, filters: ModelType):
    #     # TODO add the condition of filter
    #     count = await self.model.filter(is_delete=0).count()
    #     offset = (page.page - 1) * page.limit
    #     items = await self.model.filter(is_delete=0).offset(offset).limit(page.limit)
    #     pages = math.ceil(count / page.limit)
    #     return pages, items

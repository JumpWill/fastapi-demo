import math
from typing import TypeVar, Generic, Type, Optional, List, Union, Any, Dict
from uuid import UUID
from pydantic import BaseModel
from tortoise import Model

from ..schemas.request import PageAndLimit

ModelType = TypeVar('ModelType', bound=Model)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CurdBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def get_one(self, pk: [int, UUID]):
        res = await self.model.filter(pk=pk, is_delete=0).limit(1).first()
        return res

    async def delete_one(self, pk: [int, UUID]):
        res = await self.model.filter(pk=pk, is_delete=0).limit(1).update(is_delete=True)
        return res

    async def update_one(self, pk: [int, UUID], data: [UpdateSchemaType, Dict]):
        if isinstance(data, Dict):
            res = await self.model.filter(id=pk, is_delete=0).limit(1).update(**data)
        elif isinstance(data, BaseModel):
            res = await self.model.filter(id=pk, is_delete=0).limit(1).update(**data.dict(exclude_none=True))
        else:
            raise TypeError("the type of data is incorrect")
        return res

    async def get_list(self, page: PageAndLimit, filters: ModelType):
        # TODO add the condition of filter
        count = await self.model.filter(is_delete=0).count()
        offset = (page.page - 1) * page.limit
        items = await self.model.filter(is_delete=0).offset(offset).limit(page.limit)
        pages = math.ceil(count / page.limit)
        return pages, items

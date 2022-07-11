from typing import List, Optional, Generic, TypeVar
from pydantic import Field
from pydantic.generics import GenericModel

Model = TypeVar('Model')


class QueryModel(GenericModel, Generic[Model]):
    items: List[Model] = Field(description="返回数据")
    pages: int = Field(description="总页数")


class ResModel(GenericModel, Generic[Model]):
    """用于所有的get请求返回数据的封装"""
    code: int = Field(default=200, description="返回码")
    mes: str = Field(default="操作成功!", description="返回信息")
    data: Optional[Model] = Field(description="返回的数据")

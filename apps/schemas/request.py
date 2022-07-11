from typing import Optional
from pydantic import BaseModel, Field
from ..models.constant import StatusEnum


class PageAndLimit(BaseModel):
    """ fastapi查询分页的相关依赖"""
    page: int = Field(default=1, description="当前页数")
    limit: int = Field(default=10, description="每页数据的数量")


class Filter(BaseModel):
    # 根据需求来设置
    name: Optional[str] = Field(description="名称查询")
    status: Optional[StatusEnum] = Field(description="状态查询")

    
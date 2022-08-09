from typing import Optional
from datetime import datetime
from pydantic import BaseModel
from pydantic.fields import Field


class BaseCreate(BaseModel):
    desc: Optional[str] = Field(None, description="描述")
    create_time: datetime = Field(default=datetime.now(), description="创建时间")
    update_time: datetime = Field(default=datetime.now(), description="创建时间")

    class Config:
        orm_mode = True
        use_enum_values = True


class BaseQuery(BaseModel):
    id: int = Field(ge=1, description="id")
    desc: Optional[str] = Field(None, description="描述")
    create_time: datetime = Field(datetime.now(), description="创建时间")
    update_time: datetime = Field(datetime.now(), description="创建时间")


class BaseUpdate(BaseModel):
    # id: int = Field(ge=1, description="id")
    desc: Optional[str] = Field(None, description="描述")
    update_time: datetime = Field(datetime.now(), description="创建时间")


class BaseDelete(BaseModel):
    id: int = Field(ge=1, description="id")

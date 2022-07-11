from datetime import datetime
from uuid import UUID
import time
from pydantic import Field, BaseModel
from ..conf import settings

class Payload(BaseModel):
    username: str = Field(description="用户名称")
    uid: UUID = Field(description="用户主键")
    exp: int = Field(default=int(time.time())+settings.JWT_TOKEN_DURATION ,description="信息的过期时间")
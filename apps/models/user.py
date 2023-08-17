from tortoise import fields
from apps.models.base import Base, IntPk
from apps.conf.config import settings


class User(Base, IntPk):
    useraname = fields.CharField(unique=True, max_length=10, null=False)

    class Meta:
        table = f"{settings.APP}__user"

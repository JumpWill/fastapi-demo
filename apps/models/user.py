from tortoise import fields
from apps.models.base import Base, IntPk


class User(Base, IntPk):
    username = fields.CharField(unique=True, max_length=10, null=False)

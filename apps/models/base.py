from tortoise import fields
from tortoise.models import Model

class Base(Model):
    created_time = fields.DatetimeField(null=True, auto_now_add=True)
    update_time = fields.DatetimeField(null=True, auto_now=True)
    is_deleted = fields.BooleanField(null=False, default=False)

    class Meta:
        abstract = True

class IntPk(Model):
    id = fields.IntField(pk=True)

    class Meta:
        abstract = True


class UuidPk(Model):
    id = fields.UUIDField(pk=True)

    class Meta:
        abstract = True

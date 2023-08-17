from tortoise import fields
from tortoise.models import Model


class Base(Model):
    created_at = fields.DatetimeField(null=False, auto_now_add=True)
    updated_at = fields.DatetimeField(null=True, auto_now=True)
    deleted_at = fields.DatetimeField(null=True)

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

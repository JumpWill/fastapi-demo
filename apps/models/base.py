from tortoise import fields
from tortoise.models import Model

class Base(Model):

    id = fields.IntField(pk=True)
    created_time = fields.DatetimeField(null=True, auto_now_add=True)
    update_time = fields.DatetimeField(null=True, auto_now=True)
    is_delete = fields.BooleanField(null=False, default="0")

    class Meta:
        abstract = True
from tortoise.models import Model
from tortoise import fields

class Student(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32,description="学生姓名")
    age = fields.IntField(max_length=32,description="学生年龄")
    major = fields.CharField(max_length=32,description="学生专业")
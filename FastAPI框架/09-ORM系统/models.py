# models.py

# 选课系统
from tortoise.models import Model
from tortoise import fields

class Student(Model):
    id = fields.IntField(pk=True)       # field是字段的意思。  pk=primary key 主键
    name = fields.CharField(max_length=32,description="学生姓名")   # max_length必填，description是可在接口文档里显示的描述
    pwd = fields.CharField(max_length=32,description="密码")
    sno = fields.IntField(description="学号")

    # 一对多的关系
    clas = fields.ForeignKeyField("models.Clas",related_name="students")       # 外键是什么文件下的什么类。  related_name反向操作

    # 多对多的关系
    course = fields.ManyToManyField("models.Course",related_name="students",description="学生选课表")

class Clas(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32,description="班级名称")

class Teacher(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, description="教师姓名")
    pwd = fields.CharField(max_length=32, description="密码")
    tno = fields.IntField(description="教师编号")



class Course(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, description="课程名称")

    teacher = fields.ForeignKeyField("models.Teacher", related_name="courses",description="课程老师")

    # addr = fields.CharField(max_length=32, description="教室")
# api.student.py

from fastapi import APIRouter
from models import *

from fastapi.templating import Jinja2Templates
from fastapi import Request

from pydantic import BaseModel
from typing import List
from pydantic import field_validator

from fastapi.exceptions import HTTPException

student_api = APIRouter()

@student_api.get("/")
async def get_all_students():
    # (1)查找所有
    # stus = await Student.all()        # Queryset:[Student(), Student(), Student()]
    # print("students",stus)
    # for stu in stus:
    #     print(stu.name, stu.sno)

    # print(stus[0].name)

    # （2）过滤查询
    # stus = await Student.filter(name = "rain")
    # stus = await Student.filter(clas_id = 2)
    # print("students",stus)



    # (3)过滤查询      get方法：返回模型类型对象
    # stu = await Student.filter(id=1)        # [Student(),]
    # print(stu[0].name)
    # stu = await Student.get(id=1)       # Student()
    # print(stu.name, stu.sno)

    # (4)模糊查询
    # stus = await Student.filter(sno__gt = 2001)  # Queryset:[Student(), Student(), Student()]    学号大于2001
    # stus = await Student.filter(sno__range = [2001,2005])   # 学号在2001-2005之间
    # stus = await Student.filter(sno__in = [2001,2002])   # 学号是2001或者2002
    #
    # print("students", stus)
    # for stu in stus:
    #     print(stu.name, stu.sno)

    # (5)values 查询
    # stus = await Student.filter(sno__range = [1,10000])       # Queryset:[Student(), Student(), Student(),...]
    # stus = await Student.all().values("name","sno")       # [{},{},{},...]
    # print("students", stus)

    # (6)一对多查询  多对多查询
    # 单个对象的一对多查询（某学生的班级、班级名称）
    lily = await Student.get(name="lily")
    print(lily.name)
    print(lily.sno)
    print(await lily.clas.values("name"))       # {'name': '计算机科学与技术1班'}

    # 集合对象的一对多查询
    stus = await Student.all().values("name","clas__name")      # "clas__name" 外键映射

    # 多对多的查询
    # 单个对象多对多的查询
    print(await lily.course.all().values("name","teacher__name"))   # [{'name': 'Python开发', 'teacher__name': 'tom'}, {'name': 'Java开发', 'teacher__name': 'alex'}]

    # 集合对象多对多的查询
    stus = await Student.all().values("name","clas__name","course__name")

    return stus

@student_api.get("/index.html")
async def get_all_students(request:Request):
    templates = Jinja2Templates(directory="templates")

    students = await Student.all()

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
        "students" : students
        }
    )

class StudentIn(BaseModel):
    name: str
    pwd: str
    sno: int
    clas_id: int
    course:List[int] = []

    @field_validator("name")
    @classmethod
    def name_must_alpha(cls,v):
        assert v.isalpha(), 'name must be alpha'
        return v

    @field_validator("sno")
    @classmethod
    def sno_validator(cls,v):
        assert v > 2000 or v < 10000, '学号要在2000-10000之间'
        return v

@student_api.post("/")
async def add_student(student_in:StudentIn):
    # 插入到数据库
    # 方式1
    # student = Student(name=student_in.name,pwd=student_in.pwd,sno=student_in.sno,clas_id=student_in.clas_id)
    # await student.save()        # 插入到数据库student表

    # 方式2
    student  = await Student.create(name=student_in.name,pwd=student_in.pwd,sno=student_in.sno,clas_id=student_in.clas_id)

    # 多对多的关系绑定
    choose_course = await Course.filter(id__in=student_in.course)
    await student.course.add(*choose_course)        # 星号打散，才能把值一一传进去

    return student

@student_api.get("/{student_id}")
async def get_one_student(student_id:int):
    stu = await Student.get(id=student_id)

    return {f"查看id={student_id}的学生信息":stu}

@student_api.put("/{student_id}")
async def update_student(student_id:int,student_in:StudentIn):
    data =student_in.model_dump()   # 将student_in对象转为字典
    course = data.pop("course")     # 将course字段取出

    await Student.filter(id=student_id).update(**data)      # **data  将字典转为参数，一一传入

    # 设置多对多选课
    edit_stu = await Student.get(id=student_id)
    choose_course = await Course.filter(id__in=course)
    await edit_stu.course.clear()
    await edit_stu.course.add(*choose_course)

    return {"操作":f"更新id={student_id}的学生信息"}

@student_api.delete("/{student_id}")
async def delete_student(student_id:int):
    deleteCount = await Student.filter(id=student_id).delete()
    if not deleteCount:
        raise HTTPException(status_code=404,detail=f"主键={student_id}的学生不存在")

    return {}
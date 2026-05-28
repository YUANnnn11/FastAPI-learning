from os.path import exists

from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel,field_validator
from typing import Optional


from tortoise.contrib.fastapi import register_tortoise
from settings import TORTOISE_ORM
from models import *

from fastapi.exceptions import HTTPException

from tortoise.exceptions import DoesNotExist

app = FastAPI()

register_tortoise(
    app=app,
    config=TORTOISE_ORM
)

@app.get("/")
def welcome():
    return {"message":"Welcome to my first API"}

@app.get("/greet")
def greet(name: str = "张三", lang: str = "zh"):
    if lang == "en":
        return {"greeting": f"Hello, {name}"}
    else:
        return {"greeting": f"你好, {name}"}

class Item(BaseModel):
    name:str
    price:float
    tax:Optional[float] = None


@app.post("/items")
def items(item: Item):
    # 空值检测
    tax = item.tax if item.tax is not None else 0

    price_with_tax = item.price * (1 + tax/100)
    return {
        "name":item.name,
        "price_with_tax":price_with_tax
    }

@app.get("/items/{item_id}")
def get_item(item_id):
    if item_id == "404":
        return {"item_id":item_id,"found": False}
    else:
        return {"item_id":item_id,"found": True}



class StudentIn(BaseModel):
    name: str
    age: int
    major: Optional[str] = None

    @field_validator("age")
    @classmethod
    def age_check(cls,v):
        if v < 0 or v > 150:
            raise ValueError("年龄必须在0-150之间")
        return v

    @field_validator("name")
    @classmethod
    def name_check(cls,v):
        if v == "":
            raise ValueError("姓名不能为空")
        return v


@app.post("/students")
async def students(studentin: StudentIn):
    student = await Student.create(name = studentin.name, age = studentin.age,major = studentin.major)
    return student

@app.get("/students")
async def get_students(major:Optional[str] = None):
    # 计划要求 GET / students?major = CS。当前只返回全部学生。添加：
    if major:
        students = await Student.filter(major = major).all()
    else:
        students = await Student.all()
    return students

@app.get("/students/{id}")
async def get_student(id:int):
    try:
        student = await Student.get(id = id)
        return student
    except DoesNotExist:
        raise HTTPException(status_code = 404, detail = "Student not found")

    # Tortoise 的 .get() 在记录不存在时会直接抛 DoesNotExist 异常，不会返回 None。所以 if not student: 这行永远不会执行到。
    # if not student:
    #     raise HTTPException(status_code = 404, detail = "Student not found")


@app.put("/students/{id}")
async def update_student(id:int, studentin: StudentIn):
    # 小问题 — PUT / students / {id}  不检查是否存在（line92 - 94）：
    # 更新一个不存在的 id 会静默返回 "更新成功"。建议加上：
    exists = await Student.filter(id = id).exists()
    if not exists:
        raise HTTPException(status_code = 404, detail = "Student not found")
    student = await Student.filter(id = id).update(**studentin.model_dump())
    return {"msg":"更新成功"}

@app.delete("/students/{id}")
async def delete_student(id:int):
    deleteCount = await Student.filter(id=id).delete()

    if not deleteCount:
        raise HTTPException(status_code=404, detail=f"主键={id}的学生不存在")

    return {}


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000,reload=True)
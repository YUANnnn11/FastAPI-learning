# main.py
from fastapi import FastAPI
import uvicorn

from tortoise.contrib.fastapi import register_tortoise      # tortoise里的注册函数
from settings import TORTOISE_ORM

from api.student import student_api

app = FastAPI()

register_tortoise(
    app=app,
    config=TORTOISE_ORM     # 配置文件
    # generate_schemas=True,  # 如果数据库为空，则自动生成对应表单，生产环境不要开
    # add_exception_handlers=True,  # 生产环境不要开，会泄露调试信息
)

app.include_router(student_api,prefix="/student",tags=["学生选课系统的接口"])




if __name__ == '__main__':
    uvicorn.run("main:app",host="127.0.0.1",port=8080,reload=True)
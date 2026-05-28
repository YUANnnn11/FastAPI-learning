# main.py
from fastapi import FastAPI,Request
import uvicorn
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/index")
async def index(request:Request):
    name = "yuan"
    age = 30

    books = ["水浒传","西游记","红楼梦","三国演义"]
    info = {"name":"yuan","age":30,"gender":"female"}

    pai = 3.1415926

    movies = {
        "adult_movies": ["日韩","欧美","日本"],
         "child_movies":["大头儿子小头爸爸","葫芦娃","熊出没"]
    }

    return templates.TemplateResponse(
        request=request,            # request 对象必须作为第一个参数
        name = "index.html",       # 模板文件
        context = {
            "name": name,
            "age": age,
            "books":books,
            "info":info,
            "pai":pai,
            "movies":movies
        },          # context 上下文对象，一个字典
    )

if __name__ == '__main__':
    uvicorn.run("main:app",host="127.0.0.1",port=8080,reload=True)
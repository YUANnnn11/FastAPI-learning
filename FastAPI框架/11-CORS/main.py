from fastapi import FastAPI
import uvicorn

from fastapi import Request

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 自己手搓的CORS中间件，简单粗暴，解开的限制也少
# @app.middleware("http")
# async def my_CORS_middleware(request:Request, call_next):
#     response = await call_next(request)
#
#     response.headers["Access-Control-Allow-Origin"] = "*"
#
#     return response

origin = [
    "http://127.0.0.1:63342",
]

# fastapi提供的CORSMiddleware，更专业详细
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",               # 允许的域名。*表示允许所有域名访问。
    # allow_origins=origin           # 也可以写出域名列表
    allow_credentials=True,          # 允许携带cookie
    allow_methods=["GET","POST"],    # 允许的请求方法
    allow_headers=["*"],             # 允许的请求头
)

@app.get('/user')
async def user():
    print("user:yuan",)
    return {"user":"yuan"}


if __name__ == '__main__':
    uvicorn.run("main:app",host="127.0.0.1",port=8090,reload=True)
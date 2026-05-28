# main.py
from fastapi import FastAPI
import uvicorn

from apps.app01.urls import shop
from apps.app02.urls import user

app = FastAPI()

app.include_router(shop, prefix="/shop", tags=["商城中心的接口"])
app.include_router(user, prefix="/user", tags=["用户中心接口"])

if __name__ == '__main__':
    uvicorn.run("main:app",host="127.0.0.1",port=8080,reload=True)
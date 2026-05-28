# main.py
from fastapi import FastAPI
import uvicorn

from apps import app01,app02

app = FastAPI()

app.include_router(app01, prefix="/app01", tags=["商城中心的接口"])
app.include_router(app02, prefix="/app02", tags=["用户中心接口"])

if __name__ == '__main__':
    uvicorn.run("main:app",host="127.0.0.1",port=8080,reload=True)
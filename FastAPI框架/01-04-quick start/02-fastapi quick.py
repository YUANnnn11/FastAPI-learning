from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def add():
    return {"user-id":1001}

@app.get("/shop")
async def shop():
    return {"商品信息":"矿泉水"}


if __name__ == '__main__':
    uvicorn.run("02-fastapi quick:app",host="127.0.0.1",port=8080,reload=True)
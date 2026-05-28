from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get("/get")
async def get():
    return {"method":"get方法"}

@app.post("/post")
async def post():
    return {"method":"post方法"}

@app.put("/put")
async def put():
    return {"method":"put方法"}

@app.delete("/delete")
async def delete():
    return {"method":"delete方法"}

if __name__ == '__main__':
    uvicorn.run("03-路由操作装饰器方法:app",host="127.0.0.1",port=8080,reload=True)
from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.post("/items",
          tags=["这个items接口的标题"],
          summary="这是接口的总结summary",
          description="这是接口的描述description",
          response_description="这是响应数据的描述",
          deprecated=False,                         # 这个表示是否弃用此接口，使用False，弃用True
          )
async def items():
    return {"items":"items数据"}

if __name__ == '__main__':
    uvicorn.run("04-路由操作装饰器方法的参数:app",host="127.0.0.1",port=8080,reload=True)
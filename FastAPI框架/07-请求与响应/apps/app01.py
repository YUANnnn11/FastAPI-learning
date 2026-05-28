from fastapi import APIRouter

app01 = APIRouter()

@app01.get("/user/1")
async def get_user():
    # id = 1
    return {"user_id":"root user"}

@app01.get("/user/{user_id}")
async def get_user(user_id):
    print("user_id:",user_id,type(user_id))
    return {"user_id":user_id}

@app01.get("/article/{article_id}")
async def get_article(article_id:int):
    print("article_id:",article_id,type(article_id))
    return {"article_id":article_id}
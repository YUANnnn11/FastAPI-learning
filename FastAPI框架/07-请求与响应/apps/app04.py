from fastapi import APIRouter,Form

app04 = APIRouter()

@app04.post("/regin")
async def regin(username:str = Form(),password:str = Form()):
    print(f"username:{username},password:{password}")
    return {"username":username}
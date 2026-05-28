# app02..py
from fastapi import APIRouter

app02 = APIRouter()

@app02.post("/user/login")
async def login():
    return {"user":"login"}

@app02.post("/user/register")
async def register():
    return {"user":"register"}

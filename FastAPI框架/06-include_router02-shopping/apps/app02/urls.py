# app02.urls.py
from fastapi import APIRouter

user = APIRouter()

@user.post("/login")
async def login():
    return {"user":"login"}

@user.post("/register")
async def register():
    return {"user":"register"}

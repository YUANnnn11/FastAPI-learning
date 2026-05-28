# app01.py
from fastapi import APIRouter

app01 = APIRouter()

@app01.get("/shop/food")
async def shop_food():
    return {"商品信息":"食物"}

@app01.get("/shop/drink")
async def shop_drink():
    return {"商品信息":"饮料"}
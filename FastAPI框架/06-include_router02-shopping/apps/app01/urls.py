# app01.urls.py
from fastapi import APIRouter

shop = APIRouter()

@shop.get("/food")
async def shop_food():
    return {"商品信息":"食物"}

@shop.get("/drink")
async def shop_drink():
    return {"商品信息":"饮料"}
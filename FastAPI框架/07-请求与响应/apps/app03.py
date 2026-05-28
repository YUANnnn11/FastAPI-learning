from fastapi import APIRouter
from pydantic import BaseModel,Field,field_validator
from typing import Union,Optional,List
from datetime import date

app03 = APIRouter()

class Addr(BaseModel):
    province : str
    city : str


class User(BaseModel):
    name : str
    age : int = Field(default=0,gt=0,lt=100)    # 要求 0 < age < 100
    birth : Optional[date] = None
    friends : List[int] = []
    description:Union[str,None] = None

    address : Optional[Addr] = None   # 类型嵌套

    # 校验装饰器：name 必须是字母
    @field_validator('name')
    # cls：当前模型对象
    # 参数v
    def name_must_alpha(cls,v):
        # assert是断言，如果条件不成立，则抛出异常
        # 判断是否是字母
        assert v.isalpha(), 'name must be alpha'
        return v

class Data(BaseModel):      # 类型嵌套
    users : List[User]

@app03.post("/user")
async def user(user:User):
    print(user,type(user))
    print(user.name,user.birth)
    print(user.model_dump())
    return user

@app03.post("/data")
async def create_data(data:Data):
    # 添加数据库
    return data
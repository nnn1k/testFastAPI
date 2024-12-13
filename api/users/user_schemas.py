import datetime

from pydantic import BaseModel, EmailStr

class UserUpdate(BaseModel):
    nickname: str = None
    email: EmailStr = None

class UserBaseModel(BaseModel):
    id: int
    nickname: str
    login: str
    email: EmailStr
    created_at: datetime.datetime
    updated_at: datetime.datetime

class UserModel(UserBaseModel):
    password: bytes

class UserResponseModel(UserBaseModel):
    pass







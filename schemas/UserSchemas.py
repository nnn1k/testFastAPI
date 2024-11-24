import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr

class UserAuth(BaseModel):
    login: str
    password: str

class UserCreate(BaseModel):
    nickname: str
    login: str
    password: str
    email: EmailStr

class UserUpdate(BaseModel):
    nickname: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None

class UserResponse(BaseModel):
    id: int
    nickname: str
    login: str
    email: EmailStr
    created_at: datetime.datetime
    updated_at: datetime.datetime

class UserInDB(UserResponse):
    password: bytes

class UserInDBWithRel(UserInDB):
    categories: Optional[list['CategoriesResponse']]







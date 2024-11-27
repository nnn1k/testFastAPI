from pydantic import BaseModel, EmailStr

class UserAuth(BaseModel):
    login: str
    password: str


class UserCreate(BaseModel):
    nickname: str
    login: str
    password: str
    email: EmailStr

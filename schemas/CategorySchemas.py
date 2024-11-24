import datetime
from typing import Optional
from pydantic import BaseModel

class CategoryCreate(BaseModel):
    user_id: int
    name: str

class CategoryUpdate(BaseModel):
    name: Optional[str] = None

class CategoryResponse(BaseModel):
    id: int
    user_id: int
    name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime

class CategoryResponseWithRel(CategoryResponse):
    categories: Optional[list[CategoryResponse]]

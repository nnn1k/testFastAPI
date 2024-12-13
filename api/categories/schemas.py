import datetime
from typing import Optional
from pydantic import BaseModel

class CategoryCreate(BaseModel):
    name: str
    description: Optional[str] = None

class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class CategoryModel(BaseModel):
    id: int
    user_id: int
    name: str
    description: Optional[str] = None
    created_at: datetime.datetime
    updated_at: datetime.datetime

class CategoryResponseWithRel(CategoryModel):
    categories: Optional[list[CategoryModel]]

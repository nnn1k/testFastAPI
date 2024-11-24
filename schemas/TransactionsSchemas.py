import datetime
from typing import Optional
from pydantic import BaseModel, condecimal


class TransactionCreate(BaseModel):
    user_id: int
    transaction_type: str
    amount: condecimal(gt=0)
    category_id: int
    date: datetime.date
    notes: Optional[str] = None

class TransactionUpdate(BaseModel):
    transaction_type: Optional[str] = None
    amount: Optional[condecimal(gt=0)] = None
    category_id: Optional[int] = None
    date: Optional[datetime.date] = None
    notes: Optional[str] = None

class TransactionResponse(BaseModel):
    id: int
    user_id: int
    transaction_type: str
    amount: float
    category_id: int
    date: datetime.date
    notes: Optional[str] = None


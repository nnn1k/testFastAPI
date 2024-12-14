import datetime
from typing import List

from sqlalchemy.orm import Mapped, relationship, mapped_column
from alchemy.settings.database import Base
from sqlalchemy import ForeignKey, CheckConstraint


class UsersAl(Base):
    __tablename__ = 'users'

    nickname: Mapped[str]
    login: Mapped[str]
    password: Mapped[bytes]
    email: Mapped[str]

    categories: Mapped[List["CategoriesAl"]] = relationship(
        back_populates='user'
    )

class CategoriesAl(Base):
    __tablename__ = 'categories'

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    name: Mapped[str]
    description: Mapped[str] = mapped_column(nullable=True)

    user: Mapped['UsersAl'] = relationship(
        back_populates='categories',
    )

    transactions: Mapped[List['TransactionsAl']] = relationship(
        back_populates='category',
    )

class TransactionsAl(Base):
    __tablename__ = 'transactions'

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    transaction_type: Mapped[str]
    amount: Mapped[float]
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))
    date: Mapped[datetime.date]
    notes: Mapped[str] = mapped_column(nullable=True)

    category: Mapped['CategoriesAl'] = relationship(
        back_populates='transactions',
    )

    __table_args__ = (
        CheckConstraint(
            "transaction_type IN ('income', 'expense')",
            name='check_transaction_type'
        ),
    )

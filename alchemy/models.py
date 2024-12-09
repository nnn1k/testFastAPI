import datetime
from sqlalchemy.orm import Mapped, relationship, mapped_column
from alchemy.settings.database import Base, intpk, created_at, updated_at
from sqlalchemy import ForeignKey, CheckConstraint


class UsersAl(Base):
    __tablename__ = 'users'

    id: Mapped[intpk]
    nickname: Mapped[str]
    login: Mapped[str]
    password: Mapped[bytes]
    email: Mapped[str]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    categories: Mapped[list["CategoriesAl"]] = relationship(back_populates='user')

class CategoriesAl(Base):
    __tablename__ = 'categories'

    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    name: Mapped[str]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    user: Mapped['UsersAl'] = relationship(
        back_populates='categories',
    )

    transactions: Mapped[list['TransactionsAl']] = relationship(
        back_populates='category',
    )

class TransactionsAl(Base):
    __tablename__ = 'transactions'

    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    transaction_type: Mapped[str]
    amount: Mapped[float]
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))
    date: Mapped[datetime.date]
    notes: Mapped[str] = mapped_column(nullable=True)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    category: Mapped['CategoriesAl'] = relationship(
        back_populates='transactions',
    )

    __table_args__ = (
        CheckConstraint(
            "transaction_type IN ('income', 'expense')",
            name='check_transaction_type'
        ),
    )

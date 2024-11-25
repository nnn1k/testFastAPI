from typing import Optional

from sqlalchemy import select, delete
from sqlalchemy.orm import selectinload

from alchemy.settings.database import session_factory

from schemas.UserSchemas import UserCreate, UserResponse, UserInDB
from alchemy.models.models import UsersAl

def user_is_exist(nickname: str) -> bool:
    with session_factory() as session:
        user = session.query(UsersAl).filter_by(nickname=nickname).first()
        if user is None:
            return True
        return False

def add_user(user: UserCreate) -> UserResponse:
    with session_factory() as session:
        user = UsersAl(nickname=user.nickname, login=user.login, password=user.password, email=user.email)
        session.add(user)
        session.flush()
        session.refresh(user)
        result_user = UserResponse.model_validate(user, from_attributes=True)
        session.commit()
    return result_user

def get_user(**kwargs) -> Optional[UserInDB]:
    with session_factory() as session:
        query = (
            select(UsersAl)
            .filter_by(**kwargs)
        )
        res = session.execute(query)
        user = res.unique().scalars().first()
        if user is None:
            return None
        result_user = UserInDB.model_validate(user, from_attributes=True)
        session.commit()
    return result_user

def delete_user(id):
    with session_factory() as session:
        query = (
            delete(UsersAl)
            .filter_by(id=id)
        )
        res = session.execute(query)
        session.commit()

from typing import Optional

from sqlalchemy import select, delete

from alchemy.models import UsersAl
from alchemy.settings.database import session_factory
from api.users.auth.schemas import UserCreate
from api.users.auth.utils import validate_password
from api.users.user_schemas import UserResponseModel, UserModel


def get_user_for_login(login: str, password: str) -> Optional[UserResponseModel]:
    with session_factory() as session:
        query = (
            select(UsersAl)
            .filter_by(login=login)
        )
        res = session.execute(query)
        user = res.scalars().first()
        if user is None:
            return None

        if not validate_password(password=password, hashed_password=user.password):
            return None
        result_user = UserResponseModel.model_validate(user, from_attributes=True)
        session.commit()

    return result_user


def add_user(user: UserCreate) -> UserModel:
    with session_factory() as session:
        user = UsersAl(nickname=user.nickname, login=user.login, password=user.password, email=user.email)
        session.add(user)
        session.flush()
        session.refresh(user)
        result_user = UserModel.model_validate(user, from_attributes=True)
        session.commit()
    return result_user


def delete_user(user_id):
    with session_factory() as session:
        query = (
            delete(UsersAl)
            .filter_by(id=user_id)
        )
        res = session.execute(query)
        session.commit()

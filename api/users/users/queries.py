from sqlalchemy import select
from sqlalchemy.orm import selectinload

from alchemy.models import UsersAl
from alchemy.settings.database import session_factory
from api.users.repository import get_user_repo
from api.users.user_schemas import (
    UserModel,
    UserResponseModel,
    UserUpdate
)
from alchemy.schemas_with_rel import UserModelWithRel


def update_user(user: UserResponseModel, new_user_data: UserUpdate) -> UserModel:
    user_repo = get_user_repo()
    new_user = user_repo.update_one(id=user.id, nickname=new_user_data.nickname, email=new_user_data.email)
    return new_user.model_dump(exclude='password')


def get_user_with_rel(user: UserResponseModel) -> UserModelWithRel:
    with session_factory() as session:
        query = (
            select(UsersAl)
            .options(selectinload(UsersAl.categories))
            .filter_by(id=user.id)
        )
        res = session.execute(query)
        user = res.scalars().first()

        return UserModelWithRel.model_validate(user, from_attributes=True)

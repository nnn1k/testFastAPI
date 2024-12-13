from sqlalchemy import select
from sqlalchemy.orm import selectinload

from alchemy.models import UsersAl
from alchemy.settings.database import session_factory
from api.users.user_schemas import (
    UserModel,
    UserResponseModel,
    UserUpdate
)
from alchemy.schemas_with_rel import UserModelWithRel


def update_user(user: UserResponseModel, new_user_data: UserUpdate) -> UserModel:
    with session_factory() as session:
        user = session.get(UsersAl, user.id)
        if new_user_data.nickname != user.nickname:
            user.nickname = new_user_data.nickname
        if new_user_data.email != user.email:
            user.email = new_user_data.email

        session.commit()
        return UserResponseModel.model_validate(user, from_attributes=True)

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

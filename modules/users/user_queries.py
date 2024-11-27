from typing import Optional

from sqlalchemy import select

from alchemy.models import UsersAl
from alchemy.settings.database import session_factory
from modules.users.user_schemas import UserResponseModel

def get_user(**kwargs) -> Optional[UserResponseModel]:
    with session_factory() as session:
        query = (
            select(UsersAl)
            .filter_by(**kwargs)
        )
        res = session.execute(query)
        user = res.unique().scalars().first()
        if user is None:
            return None
        result_user = UserResponseModel.model_validate(user, from_attributes=True)
        session.commit()
    return result_user

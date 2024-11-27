from alchemy.models import UsersAl
from alchemy.settings.database import session_factory
from modules.users.user_schemas import UserModel, UserResponseModel, UserUpdate


def update_user(user: UserResponseModel, new_user_data: UserUpdate) -> UserModel:
    with session_factory() as session:
        user = session.get(UsersAl, user.id)
        if new_user_data.nickname != user.nickname:
            user.nickname = new_user_data.nickname
        if new_user_data.email != user.email:
            user.email = new_user_data.email

        session.commit()
        return UserResponseModel.model_validate(user, from_attributes=True)




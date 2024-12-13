from fastapi import Depends

from api.users.token_dependencies import get_user_by_token
from api.users.user_schemas import UserUpdate, UserModel
from api.users.users.queries import update_user

def update_user_dependencies(
    new_user: UserUpdate,
    user: UserModel = Depends(get_user_by_token)
):

    new_user = update_user(user, new_user)
    return new_user

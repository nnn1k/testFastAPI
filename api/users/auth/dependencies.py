from fastapi import HTTPException
from starlette import status

from api.users.auth.queries import add_user, get_user_for_login
from api.users.auth.schemas import UserAuth, UserCreate
from api.users.auth.utils import hash_password
from api.users.user_schemas import UserModel


def validate_user(
    reg_user: UserAuth,
) -> UserModel:
    login_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="invalid nickname or password",
    )
    user = get_user_for_login(login=reg_user.login, password=reg_user.password)
    if not user:
        raise login_exc
    return user

def register_user(
    reg_user: UserCreate,
) -> UserModel:
    register_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="user is exist",
    )
    if get_user_for_login(login=reg_user.login, password=reg_user.password):
        raise register_exc
    reg_user.password = hash_password(reg_user.password)
    user = add_user(reg_user)
    return user

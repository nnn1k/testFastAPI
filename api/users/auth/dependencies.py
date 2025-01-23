from fastapi import HTTPException, status

from api.users.auth.schemas import UserAuth, UserCreate
from api.users.auth.utils import hash_password, validate_password
from api.users.repository import get_user_repo
from api.users.user_schemas import UserModel


def validate_user(
    reg_user: UserAuth,
) -> UserModel:
    login_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="invalid nickname or password",
    )
    user_repo = get_user_repo()
    user = user_repo.get_one(login=reg_user.login)
    if not user or not validate_password(password=reg_user.password, hashed_password=user.password):
        raise login_exc
    return user

def register_user(
    reg_user: UserCreate,
) -> UserModel:
    register_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="user is exist",
    )
    user_repo = get_user_repo()
    if user_repo.get_one(login=reg_user.login):
        raise register_exc
    user = user_repo.add_one(
        login=reg_user.login,
        password=hash_password(reg_user.password),
        nickname=reg_user.nickname,
        email=reg_user.email
    )
    return user



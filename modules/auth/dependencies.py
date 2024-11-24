from fastapi import HTTPException, status, Cookie, Request
from fastapi.responses import RedirectResponse

from alchemy.queries.user_queries import get_user, add_user

from modules.auth.utils import validate_password, hash_password
from modules.auth.AuthJWT import jwt_token
from schemas.UserSchemas import UserAuth, UserCreate, UserResponse

ACCESS_TOKEN = 'access_token'
REFRESH_TOKEN = 'refresh_token'

def validate_user(
    reg_user: UserAuth,
):
    unauthed_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="invalid nickname or password",
    )
    user = get_user(login=reg_user.login)
    if not user:
        raise unauthed_exc
    if not validate_password(password=reg_user.password, hashed_password=user.password):
        raise unauthed_exc
    return user

def register_user(
    reg_user: UserCreate,
):
    unauthed_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="user is exist",
    )
    if get_user(login=reg_user.login):
        raise unauthed_exc
    reg_user.password = hash_password(reg_user.password)
    user = add_user(reg_user)
    return user


def get_user_by_token(
    access_token=Cookie(None),
    refresh_token=Cookie(None),
    request: Request = None,
) -> UserResponse:
    if access_token is None:
        response = check_refresh_token(refresh_token, request)

    try:
        id = jwt_token.decode_jwt(token=access_token).get("sub")
        user = get_user(id=id)
        if user:
            return user
    except Exception:
        response = check_refresh_token(refresh_token, request)

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=f"not authenticated",
    )

def check_refresh_token(refresh_token, request: Request):
    login_url = "/api/auth/login"
    referer_url = request.headers.get("Referer", "/api/auth/login")
    if refresh_token is None:
        return RedirectResponse(url=login_url)
    try:
        new_access_token, new_refresh_token = jwt_token.token_refresh(refresh_token)
        if new_access_token is None or new_refresh_token is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="invalid token (refresh)",
            )
        response = RedirectResponse(url=referer_url)
        response.set_cookie(key=ACCESS_TOKEN, value=new_access_token)
        response.set_cookie(key=REFRESH_TOKEN, value=new_refresh_token)
        return response
    except Exception as e:
        return RedirectResponse(url=login_url)



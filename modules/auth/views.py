from fastapi import Depends, APIRouter, HTTPException, Response, Cookie

from modules.auth.AuthJWT import jwt_token
from modules.auth.dependencies import (
    validate_user,
    register_user,
    get_user_by_token,
    COOKIE_ACCESS_TOKEN,
    COOKIE_REFRESH_TOKEN
)
from schemas.UserSchemas import UserInDB
from modules.auth.utils import Token

router = APIRouter(
    prefix='/auth',
    tags=['auth'],
    #dependencies=[Depends(get_user_by_token)]
)

@router.post('/login', response_model=Token)
def login_views(
    response: Response,
    user: UserInDB = Depends(validate_user),
):
    access_token = jwt_token.create_access_token(id=user.id)
    refresh_token = jwt_token.create_refresh_token(id=user.id)

    response.set_cookie(COOKIE_ACCESS_TOKEN, access_token)
    response.set_cookie(COOKIE_REFRESH_TOKEN, refresh_token)

    return Token(
            access_token=access_token,
            refresh_token=refresh_token,
        )

@router.post('/register')
def register_views(
    response: Response,
    user: UserInDB = Depends(register_user)
):
    access_token = jwt_token.create_access_token(id=user.id)
    refresh_token = jwt_token.create_refresh_token(id=user.id)

    response.set_cookie(COOKIE_ACCESS_TOKEN, access_token)
    response.set_cookie(COOKIE_REFRESH_TOKEN, refresh_token)

    return Token(
        access_token=access_token,
        refresh_token=refresh_token
    )

@router.post('/logout')
def logout_views(
    response: Response,
    user: UserInDB = Depends(get_user_by_token)
):
    response.delete_cookie(COOKIE_ACCESS_TOKEN)
    response.delete_cookie(COOKIE_REFRESH_TOKEN)

    return {
        'status': f'logged out, {user.nickname}'
    }

@router.get("/get-cookies")
def get_cookies(
        access_token: str = Cookie(None),
        refresh_token: str = Cookie(None)
):
    if access_token is None or refresh_token is None:
        raise HTTPException(status_code=400, detail="Cookies are missing.")

    return {
        "access_token": access_token,
        "refresh_token": refresh_token
    }

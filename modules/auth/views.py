from fastapi import Depends, APIRouter, HTTPException, Response, Request
from starlette.responses import RedirectResponse

from modules.auth.AuthJWT import jwt_token
from modules.auth.dependencies import (
    validate_user,
    register_user,
    get_user_by_token,
    ACCESS_TOKEN,
    REFRESH_TOKEN
)
from schemas.UserSchemas import UserResponse, UserInDB
from modules.auth.utils import Token

router = APIRouter(
    prefix='/auth',
    tags=['auth'],
)

@router.post('/login')
def login_views(
    response: Response,
    user: UserInDB = Depends(validate_user),
):
    access_token = jwt_token.create_access_token(id=user.id)
    refresh_token = jwt_token.create_refresh_token(id=user.id)

    response.set_cookie(ACCESS_TOKEN, access_token)
    response.set_cookie(REFRESH_TOKEN, refresh_token)
    token = Token(
            access_token=access_token,
            refresh_token=refresh_token,
        )
    return {
        'user': user.model_dump(),
        'token': token.model_dump()
    }


@router.post('/register')
def register_views(
    user: UserResponse = Depends(register_user)
):
    return RedirectResponse(url='/api/auth/login')

@router.post('/logout')
def logout_views(
    response: Response,
    user: UserResponse = Depends(get_user_by_token)
):
    response.delete_cookie(ACCESS_TOKEN)
    response.delete_cookie(REFRESH_TOKEN)

    return {
        'status': f'logged out, {user.nickname}'
    }


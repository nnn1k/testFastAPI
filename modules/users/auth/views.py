from fastapi import Depends, APIRouter, Response
from fastapi.responses import RedirectResponse

from modules.users.auth.AuthJWT import jwt_token
from modules.users.token_dependencies import (
    get_user_by_token,
    ACCESS_TOKEN,
    REFRESH_TOKEN
)
from modules.users.auth.dependencies import validate_user, register_user
from modules.users.user_schemas import UserModel
from modules.users.auth.utils import Token

router = APIRouter(
    prefix='/auth',
    tags=['auth'],
)

@router.post('/login')
def login_views(
    response: Response,
    user: UserModel = Depends(validate_user),
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
        'user': user.model_dump(exclude='password'),
        'token': token.model_dump()
    }


@router.post('/register')
def register_views(
    user: UserModel = Depends(register_user)
):
    return RedirectResponse(url='/api/auth/login')

@router.post('/logout')
def logout_views(
    response: Response,
    user: UserModel = Depends(get_user_by_token)
):
    response.delete_cookie(ACCESS_TOKEN)
    response.delete_cookie(REFRESH_TOKEN)

    return {
        'status': f'logged out, {user.nickname}'
    }


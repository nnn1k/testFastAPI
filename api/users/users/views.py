from fastapi import Depends, APIRouter

from api.users.token_dependencies import get_user_by_token
from api.users.users.dependencies import update_user_dependencies
from api.users.user_schemas import UserUpdate, UserResponseModel
from api.users.users.queries import get_user_with_rel

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me", summary="Посмотреть информацию о себе")
def auth_user_check_self_info(
    user: UserResponseModel = Depends(get_user_by_token),
):
    user = get_user_with_rel(user)
    return {
        'user': user
    }

@router.put("/me", summary="Редактировать информацию о себе")
def update_user_views(
    new_user: UserUpdate = Depends(update_user_dependencies)
):
    return {
        'user': new_user,
    }

from fastapi import Depends, APIRouter

from modules.users.token_dependencies import get_user_by_token
from modules.users.users.dependencies import update_user_dependencies
from modules.users.user_schemas import UserUpdate, UserResponseModel

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me")
def auth_user_check_self_info(
    user: UserResponseModel = Depends(get_user_by_token),
):
    return {
        'user': user.model_dump()
    }

@router.put("/")
def update_user_views(
    new_user: UserUpdate = Depends(update_user_dependencies)
):
    return {
        'user': new_user,
    }

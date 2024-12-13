from fastapi import Depends

from api.categories.queries import add_category, update_category
from api.categories.schemas import CategoryCreate, CategoryUpdate
from api.users.token_dependencies import get_user_by_token
from api.users.user_schemas import UserResponseModel


def add_category_dependencies(
    category: CategoryCreate,
    user: UserResponseModel = Depends(get_user_by_token)
):
    return add_category(user, category)

def update_category_dependencies(
    category_id: int,
    category: CategoryUpdate,
    user: UserResponseModel = Depends(get_user_by_token)
):
    return update_category(user, category_id, category)
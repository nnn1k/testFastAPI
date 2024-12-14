from fastapi import Depends

from api.categories.repository import get_category_repo
from api.categories.schemas import CategoryCreate, CategoryUpdate
from api.users.token_dependencies import get_user_by_token
from api.users.user_schemas import UserResponseModel


def add_category_dependencies(
    category: CategoryCreate,
    user: UserResponseModel = Depends(get_user_by_token)
):
    category_repo = get_category_repo()
    category = category_repo.add_one(user_id=user.id, **category.model_dump())
    return category

def update_category_dependencies(
    category_id: int,
    new_category: CategoryUpdate,
    user: UserResponseModel = Depends(get_user_by_token)
):
    category_repo = get_category_repo()
    category = category_repo.update_one(id=category_id, user_id=user.id, **new_category.model_dump())
    return category

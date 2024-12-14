from fastapi import Depends, APIRouter, Depends, HTTPException

from api.categories.dependencies import add_category_dependencies, update_category_dependencies

from api.categories.repository import get_category_repo
from api.categories.schemas import CategoryModel
from api.users.token_dependencies import get_user_by_token
from api.users.user_schemas import UserResponseModel

router = APIRouter(
    prefix="/categories",
    tags=["categories"],
)

@router.get("/", summary="Посмотреть все категории этого пользователя")
def get_all_categories_views(
    user: UserResponseModel = Depends(get_user_by_token),
):
    category_repo = get_category_repo()
    categories = category_repo.get_all(user_id=user.id)
    return {'categories': categories}

@router.post("/", summary="Добавить новую категорию этому пользователю")
def create_category_views(
    category: CategoryModel = Depends(add_category_dependencies),
):
    return {'category': category}

@router.get("/{category_id}", summary="Посмотреть конкретную категорию этого пользователя")
def get_one_category_views(
    category_id: int,
    user: UserResponseModel = Depends(get_user_by_token),
):
    category_repo = get_category_repo()
    category = category_repo.get_one(id=category_id, user_id=user.id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return {'category': category}

@router.put("/{category_id}", summary="Редактировать конкретную категорию этого пользователя")
def update_category_views(
    category: CategoryModel = Depends(update_category_dependencies)
):
    return {'category': category}

@router.delete("/{category_id}", summary="Удалить конкретную категорию этого пользователя")
def delete_category_views(
    category_id: int,
    user: UserResponseModel = Depends(get_user_by_token),
):
    category_repo = get_category_repo()
    category_repo.delete_one(id=category_id, user_id=user.id)
    return {'message': 'Category deleted'}

from sqlalchemy import select, delete

from alchemy.models import CategoriesAl
from alchemy.settings.database import session_factory
from api.categories.schemas import CategoryCreate, CategoryModel, CategoryUpdate
from api.users.user_schemas import UserResponseModel


def get_categories(user: UserResponseModel) -> list[CategoryModel]:
    with session_factory() as session:
        query = (
            select(CategoriesAl)
            .filter_by(user_id=user.id)
        )
        res = session.execute(query)
        result = res.scalars().all()
        return [CategoryModel.model_validate(category, from_attributes=True) for category in result]

def get_category(user: UserResponseModel, category_id: int) -> CategoryModel:
    with session_factory() as session:
        query = (
            select(CategoriesAl)
            .filter_by(user_id=user.id, id=category_id)
        )
        res = session.execute(query)
        result = res.scalars().first()
        if result is None:
            return None
        return CategoryModel.model_validate(result, from_attributes=True)

def add_category(user: UserResponseModel, category: CategoryCreate) -> CategoryModel:
    with session_factory() as session:
        category = CategoriesAl(user_id=user.id, **category.dict())
        session.add(category)
        session.flush()
        session.refresh(category)
        session.commit()
        return CategoryModel.model_validate(category, from_attributes=True)

def update_category(user: UserResponseModel, category_id: int, new_category: CategoryUpdate) -> CategoryModel:
    with session_factory() as session:
        query = (
            select(CategoriesAl)
            .filter_by(user_id=user.id, id=category_id)
        )
        res = session.execute(query)
        category = res.scalars().first()
        if category is None:
            return None
        if new_category.name != category.name:
            category.name = new_category.name
        if new_category.description != category.description:
            category.description = new_category.description
        session.commit()
        return CategoryModel.model_validate(category, from_attributes=True)

def delete_category(user: UserResponseModel, category_id: int) -> None:
    with session_factory() as session:
        query = (
            delete(CategoriesAl)
            .filter_by(user_id=user.id, id=category_id)
        )
        session.execute(query)
        session.commit()



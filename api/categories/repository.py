from alchemy.models import CategoriesAl
from alchemy.utils.repository import AlchemyRepository
from api.categories.schemas import CategoryModel


class CategoryRepository(AlchemyRepository):
    db_model = CategoriesAl
    schema = CategoryModel


def get_category_repo():
    return CategoryRepository()

from sqladmin import ModelView
from alchemy.models import UsersAl, CategoriesAl

class UserAdmin(ModelView, model=UsersAl):

    column_list = [
        UsersAl.id,
        UsersAl.nickname,
        UsersAl.email,
        UsersAl.created_at,
        UsersAl.updated_at
    ]
    name = 'User'

class CategoryAdmin(ModelView, model=CategoriesAl):
    form_excluded_columns = [
        CategoriesAl.id,
        CategoriesAl.created_at,
        CategoriesAl.updated_at
    ]

    column_list = [
        CategoriesAl.id,
        CategoriesAl.user_id,
        CategoriesAl.name,
        CategoriesAl.description,
        CategoriesAl.created_at,
        CategoriesAl.updated_at
    ]
    column_searchable_list = [
        CategoriesAl.user_id,
    ]

    name = 'Categorie'




from sqladmin import Admin
from alchemy.settings.database import engine
from modules.admin.admin_class import UserAdmin, CategoryAdmin

def create_admin(app):
    admin = Admin(app, engine)
    admin.add_view(UserAdmin)
    admin.add_view(CategoryAdmin)

from alchemy.settings.database import engine, Base
from alchemy.models.models import UsersAl, CategoriesAl, TransactionsAl

def create_tables():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

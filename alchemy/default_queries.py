from alchemy.settings.database import engine, Base
from alchemy.models import *

def create_tables():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    create_tables()
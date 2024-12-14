from alchemy.models import UsersAl
from alchemy.utils.repository import AlchemyRepository
from api.users.user_schemas import UserModel


class UserRepository(AlchemyRepository):
    db_model = UsersAl
    schema = UserModel


def get_user_repo():
    return UserRepository()

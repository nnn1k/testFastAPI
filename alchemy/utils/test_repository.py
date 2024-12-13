from pydantic import BaseModel
import pytest
from alchemy.models import UsersAl
from alchemy.utils.repository import AlchemyRepository
from api.users.user_schemas import UserModel

class TestRepository(AlchemyRepository):
    db_model = UsersAl
    schema = UserModel

def test_works_repository():
    test = TestRepository()
    get_all(test)
    add_id = add_one(test)
    user_get = get_one(test, add_id)
    update_one(test, user_get)
    delete_one(test, user_get)

def get_all(test: TestRepository):
    all_user = test.get_all()
    assert isinstance(all_user, list)
    assert isinstance(all_user[0], test.schema)

def add_one(test: TestRepository):
    add_user = test.add_one(login='test_repo', password=b'test_repo', nickname='test_repo', email='test_repo@test.repo')
    assert isinstance(add_user, test.schema)
    return add_user.id

def get_one(test: TestRepository, id: int):
    get_user = test.get_one(id=id)
    assert isinstance(get_user, test.schema)
    return get_user

def update_one(test: TestRepository, user: UserModel):
    update_user = test.update_one(id=user.id, login='testttttt')
    assert isinstance(update_user, test.schema)
    assert update_user.login != user.login

def delete_one(test: TestRepository, user: UserModel):
    delete_user = test.delete_one(id=user.id)
    assert delete_user.get('deleted')

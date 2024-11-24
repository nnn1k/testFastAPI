from alchemy.queries.queries import create_tables
from alchemy.queries.user_queries import add_user, get_user
from modules.auth.utils import hash_password
from schemas.UserSchemas import UserCreate

create_tables()
add_user(UserCreate(nickname='nnn1k', login='admin', password=hash_password('admin'), email='admin@gmail.com'))
user = get_user(login='admin')
if user:
    print(user)
else:
    print('error')

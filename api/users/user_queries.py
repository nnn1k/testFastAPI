from typing import Optional

from api.users.repository import get_user_repo
from api.users.user_schemas import UserResponseModel

def get_user(**kwargs) -> Optional[UserResponseModel]:
    return get_user_repo().get_one(**kwargs)



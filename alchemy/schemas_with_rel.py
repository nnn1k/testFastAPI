from typing import Optional

from api.users.user_schemas import UserBaseModel
from api.categories.schemas import CategoryModel


class UserModelWithRel(UserBaseModel):
    categories: Optional[list['CategoryModel']]

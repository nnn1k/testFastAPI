import pytest
from fastapi import FastAPI, APIRouter, Depends, Request
from modules.auth import *

from modules.auth.dependencies import get_user_by_token
from schemas.UserSchemas import UserResponse

app = FastAPI()
router = APIRouter(
    prefix="/api",
)

@router.get("/users/me", response_model=UserResponse)
def auth_user_check_self_info(
        user: UserResponse = Depends(get_user_by_token),
):
    return user.model_dump()

@router.get("/get-cookies")
def get_cookies(
       request: Request
):
    return {
        'cookies': request.cookies,
    }

router.include_router(auth_router)
app.include_router(router)
pytest.main(["modules/auth/tests.py"])

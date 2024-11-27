import pytest
from fastapi import FastAPI, APIRouter, Request
from modules.users import auth_router
from modules.users import users_router

app = FastAPI()
router = APIRouter(
    prefix="/api",
)


@router.get("/get-cookies")
def get_cookies(
       request: Request
):
    return {
        'cookies': request.cookies,
    }


router.include_router(auth_router)
router.include_router(users_router)
app.include_router(router)
pytest.main(["modules/users/auth/tests.py"])

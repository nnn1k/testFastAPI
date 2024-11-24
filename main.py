from fastapi import FastAPI, APIRouter, Depends
from modules.auth import auth_router

from modules.auth.dependencies import get_user_by_token
from schemas.UserSchemas import UserResponse

app = FastAPI()
global_router = APIRouter(
    prefix="/api",
)


@app.get("/users/me", response_model=UserResponse)
def auth_user_check_self_info(
        user: UserResponse = Depends(get_user_by_token),
):
    return user.model_dump()


global_router.include_router(auth_router)

app.include_router(global_router)

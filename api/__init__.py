from fastapi import FastAPI, APIRouter, Request, Depends
from api.users import users_router, auth_router
from api.categories import category_router
router = APIRouter(
    prefix="/api",
)
router.include_router(auth_router)
router.include_router(users_router)
router.include_router(category_router)

@router.get("/get-cookies")
def get_cookies(
       request: Request
):
    return {
        'cookies': request.cookies,
    }
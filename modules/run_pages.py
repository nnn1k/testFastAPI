from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

templates = Jinja2Templates(directory='front')
router = APIRouter()


@router.get('/login')
def auth(request: Request):
    return templates.TemplateResponse('/pages/auth/login/login.html', {'request': request})

@router.get('/register')
def auth(request: Request):
    return templates.TemplateResponse('/pages/auth/register/register.html', {'request': request})

@router.get('/profile')
def profile(request: Request):
    return templates.TemplateResponse('/pages/profile/profile.html', {'request': request})

@router.get('/profile/update')
def profile(request: Request):
    return templates.TemplateResponse('/pages/profile/update_user/update_user_info.html', {'request': request})

@router.get('/categories/add')
def profile(request: Request):
    return templates.TemplateResponse('/pages/categories/add_category/add_category.html', {'request': request})

@router.get('/base')
def profile(request: Request):
    return templates.TemplateResponse('/base/base.html', {'request': request})
@router.get('/')
def go_to_docs():
    return RedirectResponse(url='/docs')

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
def me(request: Request):
    return templates.TemplateResponse('/pages/profile/profile.html', {'request': request})

@router.get('/')
def go_to_docs():
    return RedirectResponse(url='/docs')

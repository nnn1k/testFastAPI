import pytest
from fastapi import FastAPI, Request, Response
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates

from api import router as api_router

from sqladmin import Admin
from alchemy.settings.database import engine
from api.admin import UserAdmin, CategoryAdmin


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/', include_in_schema=False)
def root():
    return RedirectResponse(url='/docs')


templates = Jinja2Templates(directory='front')
@app.get('/auth', include_in_schema=False)
def auth(request: Request):
    return templates.TemplateResponse('login.html', {'request': request})

@app.get('/me', include_in_schema=False)
def me(request: Request):
    return templates.TemplateResponse('me.html', {'request': request})
admin = Admin(app, engine)
admin.add_view(UserAdmin)
admin.add_view(CategoryAdmin)

app.include_router(api_router)

pytest.main(["api/users/auth/tests.py"])
pytest.main(["alchemy/utils/test_repository.py"])

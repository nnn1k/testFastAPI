import pytest
from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse

from api import router as api_router

from sqladmin import Admin
from alchemy.settings.database import engine
from api.admin import UserAdmin, CategoryAdmin


app = FastAPI()

admin = Admin(app, engine)

@app.get('/', include_in_schema=False)
def root():
    return RedirectResponse(url='/docs')


admin.add_view(UserAdmin)
admin.add_view(CategoryAdmin)

app.include_router(api_router)

pytest.main(["api/users/auth/tests.py"])
pytest.main(["alchemy/utils/test_repository.py"])

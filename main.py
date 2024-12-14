import pytest
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from api import router as api_router

app = FastAPI()

@app.get('/', include_in_schema=False)
def root():
    return RedirectResponse(url='/docs')


app.include_router(api_router)

pytest.main(["api/users/auth/tests.py"])
pytest.main(["alchemy/utils/test_repository.py"])

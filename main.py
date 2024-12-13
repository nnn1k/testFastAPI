import pytest
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
import uvicorn


from api import router as api_router

app = FastAPI()

@app.get('/', include_in_schema=False)
def root():
    return RedirectResponse(url='/docs')


app.include_router(api_router)

pytest.main(["api/users/auth/tests.py"])

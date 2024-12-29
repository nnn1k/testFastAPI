from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from api import router as api_router
from modules.run_pages import router as front_router
from modules.admin.admin_setup import create_admin

app = FastAPI()

app.mount("/front", StaticFiles(directory="front"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

create_admin(app)
app.include_router(api_router)
app.include_router(front_router, include_in_schema=False)

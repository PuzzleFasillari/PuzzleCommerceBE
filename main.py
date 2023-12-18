from typing import List, Any

from beanie import init_beanie
from fastapi import FastAPI, APIRouter
from decouple import config
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import HTMLResponse

from controllers.user_controller import router as user_router
from models.puzzle import Puzzle
from models.user import User
from repositories.base.db import MongoClient

app = FastAPI(
    title=config('PROJECT_NAME'), openapi_url="/openapi.json"
)

BACKEND_CORS_ORIGINS: List[Any] = [
    "*"
]

root_router = APIRouter()

app.include_router(user_router)
app.include_router(root_router)


@app.on_event("startup")
async def startup_db_client():
    mongo = MongoClient(config('DB_URL'), config('DB_NAME'))

    await init_beanie(database=mongo.client[mongo.database_name],
                      document_models=[User, Puzzle])


@app.get("/")
def index(request: Request) -> Any:
    """Basic HTML response."""
    body = (
        "<html>"
        "<body style='padding: 10px;'>"
        "<h1>Welcome to the API</h1>"
        "<div>"
        "Check the docs: <a href='/docs'>here</a>"
        "</div>"
        "</body>"
        "</html>"
    )

    return HTMLResponse(content=body)


if BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

from fastapi import APIRouter

from models.user import User, UserCreate
from services.user_service import UserService
from repositories.base.db import MongoClient
from decouple import config

router = APIRouter(prefix='/account', tags=['Account'])


@router.post('/register', response_model=User)
async def register_to_app(user_data: UserCreate) -> User:
    return await UserService.create_user(user_data)

import os

import pytest
from decouple import config

from models.user import User, UserCreate
from repositories.base.db import MongoClient
from repositories.user_repository import UserRepository
from services.user_service import UserService


@pytest.mark.asyncio
async def test_register_user_first_time():
    mongo = MongoClient(os.getenv("MONGO_URL"), os.getenv("MONGO_DB_NAME"))

    user_repository = UserRepository(mongo)
    await user_repository.init()

    mock_user_data = UserCreate(username="testuser", email="test@example.com", password="testpassword")

    result = await UserService.create_user(mock_user_data)

    assert result.username == mock_user_data.username
    assert result.email == mock_user_data.email


@pytest.mark.asyncio
async def test_register_user_with_same_username():
    mongo = MongoClient(os.getenv("MONGO_URL"), os.getenv("MONGO_DB_NAME"))

    user_repository = UserRepository(mongo)
    await user_repository.init()

    mock_user_data = UserCreate(username="testuser", email="test@example.com", password="testpassword")

    result = await UserService.create_user(mock_user_data)

    assert result is None


@pytest.mark.asyncio
async def test_register_user_with_same_email():
    mongo = MongoClient(os.getenv("MONGO_URL"), os.getenv("MONGO_DB_NAME"))

    user_repository = UserRepository(mongo)
    await user_repository.init()

    mock_user_data = UserCreate(username="testuser", email="test@example.com", password="testpassword")

    result = await UserService.create_user(mock_user_data)

    assert result is None

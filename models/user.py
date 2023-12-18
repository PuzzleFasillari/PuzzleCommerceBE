from beanie import Document
from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class User(Document):
    username: str = Field(..., alias="username")
    email: str = Field(..., alias="email")
    hashed_password: str = Field(..., alias="hashedPassword")
    is_active: bool = Field(default=True, alias="isActive")
    is_admin: bool = Field(default=False, alias="isAdmin")

    class Settings:
        name = "users"


class UserLogin(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=6)


class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=6)
    email: EmailStr

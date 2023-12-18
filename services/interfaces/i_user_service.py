from abc import ABC, abstractmethod
from models.user import UserCreate, UserLogin, User


class IUserService(ABC):

    @staticmethod
    @abstractmethod
    async def create_user(user_data: UserCreate) -> User:
        raise NotImplemented

    @staticmethod
    @abstractmethod
    async def login_user(user_data: UserLogin) -> User:
        raise NotImplemented

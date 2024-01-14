from abc import ABC, abstractmethod
from models.puzzle import Puzzle
from typing import List, Optional


class IPuzzleService(ABC):

    @staticmethod
    @abstractmethod
    async def create_puzzle(puzzle: Puzzle, file_name: str) -> Puzzle:
        raise NotImplemented

    @staticmethod
    @abstractmethod
    async def get_puzzle_by_id(puzzle_id: str) -> Optional[Puzzle]:
        raise NotImplemented

    @staticmethod
    @abstractmethod
    async def update_puzzle(puzzle_id, puzzle: Puzzle) -> Puzzle:
        raise NotImplemented

    @staticmethod
    @abstractmethod
    async def delete_puzzle(puzzle_id: str) -> bool:
        raise NotImplemented

    @staticmethod
    @abstractmethod
    async def list_puzzle() -> List[Puzzle]:
        raise NotImplemented

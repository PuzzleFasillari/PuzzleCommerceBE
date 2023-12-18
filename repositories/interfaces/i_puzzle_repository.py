from abc import ABC, abstractmethod
from typing import List, Optional
from models.puzzle import Puzzle


class IPuzzleRepository(ABC):

    @staticmethod
    @abstractmethod
    async def create_puzzle(puzzle: Puzzle) -> Puzzle:
        raise NotImplemented

    @staticmethod
    @abstractmethod
    async def get_puzzle_by_id(puzzle_id: str) -> Optional[Puzzle]:
        raise NotImplemented

    @staticmethod
    @abstractmethod
    async def get_puzzle_by_name(puzzle_name: str) -> Optional[Puzzle]:
        raise NotImplemented

    @staticmethod
    @abstractmethod
    async def update_puzzle(puzzle_id: str, puzzle: Puzzle) -> Optional[Puzzle]:
        raise NotImplemented

    @staticmethod
    @abstractmethod
    async def delete_puzzle(puzzle_id: str) -> Optional[Puzzle]:
        raise NotImplemented

    @staticmethod
    @abstractmethod
    async def list_puzzles() -> List[Puzzle]:
        raise NotImplemented

from typing import List, Optional

from models.puzzle import Puzzle
from services.interfaces.i_puzzle_service import IPuzzleService
from repositories.puzzle_repository import PuzzleRepository


class PuzzleService(IPuzzleService):
    @staticmethod
    async def create_puzzle(puzzle: Puzzle) -> Puzzle:
        return await PuzzleRepository.create_puzzle(puzzle)

    @staticmethod
    async def get_puzzle_by_id(puzzle_id: str) -> Optional[Puzzle]:
        return await PuzzleRepository.get_puzzle_by_id(puzzle_id)

    @staticmethod
    async def get_puzzle_by_name(puzzle_name: str) -> Optional[Puzzle]:
        return await PuzzleRepository.get_puzzle_by_name(puzzle_name)

    @staticmethod
    async def update_puzzle(puzzle_id, puzzle: Puzzle) -> Puzzle:
        return await PuzzleRepository.update_puzzle(puzzle_id, puzzle)

    @staticmethod
    async def delete_puzzle(puzzle_id: str) -> bool:
        return await PuzzleRepository.delete_puzzle(puzzle_id)

    @staticmethod
    async def list_puzzle() -> List[Puzzle]:
        return await PuzzleRepository.list_puzzles()

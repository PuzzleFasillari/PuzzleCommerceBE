from typing import List, Optional

from beanie import init_beanie

from models.puzzle import Puzzle
from repositories.base.db import MongoClient
from repositories.interfaces.i_puzzle_repository import IPuzzleRepository


class PuzzleRepository(IPuzzleRepository):
    def __init__(self, mongo_client: MongoClient):
        self.mongo_client = mongo_client

    async def init(self):
        db_instance = self.mongo_client.client[self.mongo_client.database_name]

        await init_beanie(database=db_instance,
                          document_models=[Puzzle])

    @staticmethod
    async def create_puzzle(puzzle: Puzzle) -> Puzzle:
        await Puzzle.insert(puzzle)
        return puzzle

    @staticmethod
    async def get_puzzle_by_id(puzzle_id: str) -> Optional[Puzzle]:
        puzzle = await Puzzle.get(puzzle_id)
        return puzzle

    @staticmethod
    async def get_puzzle_by_name(puzzle_name: str) -> Optional[Puzzle]:
        return await Puzzle.find_one(Puzzle.name == puzzle_name)

    @staticmethod
    async def update_puzzle(puzzle_id: str, updated_puzzle: Puzzle) -> Optional[Puzzle]:
        found_puzzle = await Puzzle.get(puzzle_id)

        if found_puzzle:
            for key, value in updated_puzzle.items():
                setattr(found_puzzle, key, value)
            await found_puzzle.save()

        return found_puzzle

    @staticmethod
    async def delete_puzzle(puzzle_id: str) -> bool:
        puzzle = await Puzzle.get(puzzle_id)

        if puzzle:
            await puzzle.delete()
            return True

        return False

    @staticmethod
    async def list_puzzles() -> List[Puzzle]:
        return await Puzzle.find_all().to_list()

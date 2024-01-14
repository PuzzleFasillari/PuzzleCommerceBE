import os
from typing import List, Optional

from fastapi import UploadFile

from models.puzzle import Puzzle
from services.cdn_service import CDNService
from services.interfaces.i_puzzle_service import IPuzzleService
from repositories.puzzle_repository import PuzzleRepository


class PuzzleService(IPuzzleService):
    @staticmethod
    async def create_puzzle(puzzle: Puzzle, file: UploadFile) -> Puzzle:
        puzzle.image_url = os.getenv("CDN_BASE_URL") + '/' + file.filename

        do_space_service = CDNService(
            endpoint_url= os.getenv("CDN_ENDPOINT_URL"),
            region_name= os.getenv("CDN_REGION_NAME"),
            access_key_id= os.getenv("CDN_ACCESS_KEY_ID"),
            secret_access_key= os.getenv("CDN_SECRET_ACCESS_KEY")
        )

        file_content = await file.read()

        await do_space_service.upload_file(
            bucket_name= os.getenv("BUCKET_NAME"),
            file_data= file_content,
            object_key= file.filename
        )

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

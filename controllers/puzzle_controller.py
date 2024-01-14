from typing import List

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Body
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

from models.user import User
from services.puzzle_service import PuzzleService
from models.puzzle import Puzzle
from services.auth_service import AuthService

router = APIRouter(prefix='/puzzles', tags=['Puzzle'])

auth_service = AuthService()


@router.post("/create", response_model=Puzzle)
async def create_puzzle(puzzle_data: Puzzle = Body(...), file: UploadFile = File(...), current_user: User = Depends(auth_service.oauth2_scheme)):
    if not current_user:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="User not authenticated")

    return await PuzzleService.create_puzzle(puzzle_data, file)


@router.get("/{puzzle_id}/detail", response_model=Puzzle)
async def get_puzzle(puzzle_id: str):
    puzzle_item = await PuzzleService.get_puzzle_by_id(puzzle_id)

    if puzzle_item is None:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Puzzle not found")

    return puzzle_item


@router.get("/puzzle-list", response_model=List[Puzzle])
async def get_puzzle_list():
    lists = await PuzzleService.list_puzzle()
    return lists


@router.delete("/{puzzle_id}", response_model=dict)
async def delete_puzzle(puzzle_id: str, current_user: User = Depends(auth_service.oauth2_scheme)):
    if not current_user:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="User not authenticated")

    puzzle_item = await PuzzleService.delete_puzzle(puzzle_id)

    if not puzzle_item:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Puzzle not found")

    return {"status": "success", "message": "Puzzle deleted successfully"}

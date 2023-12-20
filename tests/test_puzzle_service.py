import os

import pytest

from enums.age_groups import AgeGroup
from enums.difficulty_level import DifficultyLevel
from enums.puzzle_material import PuzzleMaterials
from enums.puzzle_size import PuzzleSize
from enums.puzzle_theme import PuzzleTheme
from enums.puzzle_types import PuzzleTypes
from models.puzzle import Puzzle
from repositories.base.db import MongoClient
from repositories.puzzle_repository import PuzzleRepository


@pytest.mark.asyncio
async def test_create_puzzle():
    mongo = MongoClient(os.getenv("MONGO_URL"), os.getenv("MONGO_DB_NAME"))

    puzzle_repository = PuzzleRepository(mongo)
    await puzzle_repository.init()

    mock_puzzle_data = Puzzle(name='testPuzzle',
                              type=PuzzleTypes.CROSSWORD,
                              difficulty_level=DifficultyLevel.EXPERT,
                              material=PuzzleMaterials.PLASTIC,
                              theme=PuzzleTheme.SCIENCE,
                              size=PuzzleSize.EXTRA_LARGE,
                              price=float(399.6),
                              age_group=AgeGroup.ADULTS,
                              description='This is a test to create a puzzle')

    result = await puzzle_repository.create_puzzle(mock_puzzle_data)

    assert result.name == mock_puzzle_data.name
    assert result.type == mock_puzzle_data.type
    assert result.difficulty_level == mock_puzzle_data.difficulty_level
    assert result.material == mock_puzzle_data.material
    assert result.theme == mock_puzzle_data.theme
    assert result.size == mock_puzzle_data.size
    assert result.price == mock_puzzle_data.price
    assert result.age_group == mock_puzzle_data.age_group
    assert result.description == mock_puzzle_data.description


@pytest.mark.asyncio
async def test_delete_puzzle():
    mongo = MongoClient(os.getenv("MONGO_URL"), os.getenv("MONGO_DB_NAME"))

    puzzle_repository = PuzzleRepository(mongo)
    await puzzle_repository.init()

    founded_puzzle = await puzzle_repository.get_puzzle_by_name("testPuzzle")

    result = await puzzle_repository.delete_puzzle(str(founded_puzzle.id))

    assert result is True

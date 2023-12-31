from typing import Optional

from beanie import Document
from pydantic import Field

from enums.age_groups import AgeGroup
from enums.difficulty_level import DifficultyLevel
from enums.puzzle_material import PuzzleMaterials
from enums.puzzle_size import PuzzleSize
from enums.puzzle_theme import PuzzleTheme
from enums.puzzle_types import PuzzleTypes


class Puzzle(Document):
    name: str = Field(..., alias='name')
    type: PuzzleTypes = Field(..., alias='type')
    difficulty_level: DifficultyLevel = Field(..., alias='difficultyLevel')
    material: PuzzleMaterials = Field(..., alias='material')
    theme: PuzzleTheme = Field(..., alias='theme')
    size: PuzzleSize = Field(..., alias='size')
    price: float = Field(..., alias='price')
    age_group: AgeGroup = Field(..., alias='ageGroup')
    description: Optional[str] = Field(..., alias='description')

    class Settings:
        name = "puzzle"




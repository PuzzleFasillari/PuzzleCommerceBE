import json
from typing import Optional, Union

from beanie import Document
from pydantic import Field, model_validator
from pydantic.v1 import validator

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
    size: Union[PuzzleSize, str] = Field(..., alias='size')
    price: Union[float, str] = Field(..., alias='price')
    age_group: AgeGroup = Field(..., alias='ageGroup')
    description: Optional[str] = Field(..., alias='description')
    image_url: Optional[str] = Field(None, alias='imageUrl')

    @model_validator(mode='before')
    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value

    @validator('price', pre=True)
    def ensure_price_is_float(cls, value):
        if isinstance(value, str):
            try:
                return float(value)
            except ValueError:
                raise ValueError(f"Invalid price format : {value}")

        return value

    @validator('size', pre=True)
    def ensure_size_is_integer(cls, value):
        if isinstance(value, str):
            try:
                return int(value)
            except ValueError:
                raise ValueError(f"Invalid size format : {value}")

        return value

    class Settings:
        name = "puzzle"

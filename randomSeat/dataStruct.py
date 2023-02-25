from loguru import logger

from enum import Enum
from pydantic import BaseModel as PydanticBaseModel
from pydantic import Extra, validator
from typing import Any, Optional


class BaseModel(PydanticBaseModel):
    class Config:
        use_enum_values = True

    def __repr__(self) -> str:
        return f'<{super().__repr__()}>'

    def __str__(self) -> str:
        return super().__str__()


class Gender(str, Enum):
    male = 'male'
    female = 'female'


class Attitude(str, Enum):
    like = 'like'
    dislike = 'dislike'


class Relevant(BaseModel):
    pos: list[tuple[int, int]]
    name: str
    attitude: Attitude
    probability: float = 1

    @validator('pos', pre=True)
    def checkRelevantPosFormat(cls, v):
        match v:
            case 'deskmate':
                return [(-1, 0), (1, 0)]
            case str():
                raise Exception('不能填入此字符串<{v}>')
            case _:
                return v


class Absoutle(BaseModel):
    pos: list[tuple[int, int]] | str
    attitude: Attitude
    probability: float = 1

    @validator('pos')
    def checkRelevantPosFormat(cls, v):
        match v:
            case str():
                raise Exception('不能填入此字符串<{v}>')
            case _:
                return v


class Preference(BaseModel):
    relevant: Optional[list[Relevant]]
    absoutle: Optional[list[Absoutle]]


class Person(BaseModel):
    name: str
    gender: Optional[Gender]
    preference: Optional[Preference]

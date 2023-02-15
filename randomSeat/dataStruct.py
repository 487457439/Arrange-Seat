from loguru import logger

from enum import Enum
from pydantic import BaseModel, Extra, validator
from typing import Any, Optional

class Gender(str, Enum):
    male = 'male'
    female = 'female'


class Attitude(str, Enum):
    like = 'like'
    dislike = 'dislike'


class Relevant(BaseModel):
    pos: list[tuple[int,int]] | str
    name: str
    attitude: Attitude
    probability: float

    @validator('pos')
    def checkRelevantPosFormat(cls, v):
        match v:
            case 'deskmate':
                return [(-1,0), (1,0)]
            case str():
                raise Exception('不能填入此字符串<{v}>')
            case _:
                return v

class Absoutle(BaseModel):
    pos: list[tuple[int,int]] | str
    attitude: Attitude
    probability: float

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
    class Config:
        use_enum_values = True
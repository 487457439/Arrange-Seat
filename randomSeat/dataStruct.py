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


class Surround(BaseModel):
    attitude: Attitude
    name: str
    relevant_pos: list[tuple[int,int]] | str

    @validator('relevant_pos')
    def checkRelevantPosFormat(cls, v):
        match v:
            case 'deskmate':
                return [(-1,0), (1,0)]
            case str():
                raise Exception('不能填入此字符串<{v}>')
            case list():
                return v
            case _:
                raise Exception('未知的问题')
            

class Preference(BaseModel):
    surround: Optional[list[Surround]]
    # location: Optional[list[Location]]


class Person(BaseModel):
    name: str
    gender: Optional[Gender]
    preference: Optional[Preference]
    class Config:
        use_enum_values = True
import abc
from dataclasses import dataclass, asdict
from enum import Enum
from typing import NewType, Optional

ObjectId = NewType('ObjectId', str)


class BaseDto(abc.ABC):
    @abc.abstractmethod
    def as_dict(self) -> dict:
        ...


class QuestionType(Enum):
    TEXT = 'text only'
    AUDIO = 'audio uploaded'
    VIDEO = 'video uploaded'
    LINKED = 'link to online audio/video'
    IMAGE = 'image uploaded'


class AnswerType(Enum):
    TEXT = 'text only'
    AUDIO = 'audio uploaded'
    VIDEO = 'video uploaded'
    LINKED = 'link to online audio/video'
    IMAGE = 'image uploaded'


@dataclass
class QuestionDto(BaseDto):
    question_id: ObjectId
    question_type: QuestionType
    answer_id: ObjectId
    question_price: int
    text: Optional[str] = None
    attachment: Optional[bytes] = None

    def as_dict(self) -> dict:
        return asdict(self)


@dataclass
class AnswerDto(BaseDto):
    answer_id: ObjectId
    answer_type: AnswerType
    question_id: ObjectId
    answer_price: int
    text: Optional[str] = None
    attachment: Optional[bytes] = None

    def as_dict(self) -> dict:
        return asdict(self)


@dataclass
class TaskDto(BaseDto):
    task_id: ObjectId
    task_name: str
    task_questions: list[ObjectId]

    def as_dict(self) -> dict:
        return asdict(self)


@dataclass
class RoundDto(BaseDto):
    round_id: ObjectId
    name: str
    round_tasks: list[ObjectId]

    def as_dict(self) -> dict:
        return asdict(self)


@dataclass
class GameDto(BaseDto):
    game_id: ObjectId
    name: str
    game_rounds: list[ObjectId]

    def as_dict(self) -> dict:
        return asdict(self)


Balance = NewType('Balance', int)


@dataclass
class Player:
    id: str
    alias: str

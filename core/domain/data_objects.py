from dataclasses import dataclass
from enum import Enum
from typing import NewType, Optional

ObjectId = NewType('ObjectId', str)


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
class QuestionDto:
    question_id: ObjectId
    text: Optional[str]
    attachment: Optional[bytes]
    question_type: QuestionType
    answer_id: ObjectId
    question_price: int


@dataclass
class AnswerDto:
    answer_id: ObjectId
    text: Optional[str]
    attachment: Optional[bytes]
    answer_type: AnswerType
    question_id: ObjectId
    answer_price: int


@dataclass
class Task:
    id: str
    question: QuestionDto
    answer: AnswerDto


@dataclass
class Round:
    id: str
    name: str
    questions: list[Task]


@dataclass
class Game:
    id: str
    name: str
    rounds: list[Round]
    type: str


Balance = NewType('Balance', int)


@dataclass
class Player:
    id: str
    alias: str

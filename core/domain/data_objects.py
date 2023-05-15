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
    question_type: QuestionType
    answer_id: ObjectId
    question_price: int
    text: Optional[str] = None
    attachment: Optional[bytes] = None

    @classmethod
    def build(cls, question_id: ObjectId, question_type: QuestionType, answer_id: ObjectId, question_price: int,
              text: Optional[str] = None, attachment: Optional[bytes] = None) -> 'QuestionDto':
        return QuestionDto(
            question_id=question_id,
            question_type=question_type,
            answer_id=answer_id,
            question_price=question_price,
            text=text,
            attachment=attachment,
        )


@dataclass
class AnswerDto:
    answer_id: ObjectId
    answer_type: AnswerType
    question_id: ObjectId
    answer_price: int
    text: Optional[str] = None
    attachment: Optional[bytes] = None

    @classmethod
    def build(cls, question_id: ObjectId, answer_type: AnswerType, answer_id: ObjectId, answer_price: int,
              text: Optional[str] = None, attachment: Optional[bytes] = None) -> 'AnswerDto':
        return AnswerDto(
            question_id=question_id,
            answer_type=answer_type,
            answer_id=answer_id,
            text=text,
            attachment=attachment,
        )


@dataclass
class TaskDto:
    task_id: ObjectId
    task_name: str
    task_questions: list[ObjectId]

    @classmethod
    def build(cls, task_id: ObjectId, task_name: str, task_questions: list[ObjectId]) -> 'TaskDto':
        return TaskDto(
            task_id=task_id,
            task_name=task_name,
            task_questions=task_questions,
        )


@dataclass
class RoundDto:
    round_id: ObjectId
    name: str
    round_tasks: list[ObjectId]

    @classmethod
    def build(cls, round_id: ObjectId, name: str, round_tasks: list[ObjectId]) -> 'RoundDto':
        return RoundDto(
            round_id=round_id,
            name=name,
            round_tasks=round_tasks,
        )


@dataclass
class GameDto:
    game_id: ObjectId
    name: str
    game_rounds: list[ObjectId]

    @classmethod
    def build(cls, game_id: ObjectId, name: str, game_rounds: list[ObjectId]) -> 'GameDto':
        return GameDto(
            game_id=game_id,
            name=name,
            game_rounds=game_rounds,
        )


Balance = NewType('Balance', int)


@dataclass
class Player:
    id: str
    alias: str

import abc
from typing import Union

from core.domain.data_objects import QuestionDto, AnswerDto, TaskDto, RoundDto, GameDto


class DatabaseSaver(abc.ABC):
    def save(self, dto: Union[QuestionDto, AnswerDto, TaskDto, RoundDto, GameDto]):
        ...

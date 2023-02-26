import abc
from typing import Union, Type

from core.domain.data_objects import QuestionDto, AnswerDto, TaskDto, RoundDto, GameDto


class DatabaseSaver(abc.ABC):
    def save(self, dto: Union[Type[QuestionDto], Type[AnswerDto], Type[TaskDto], Type[RoundDto], Type[GameDto]]):
        ...

import abc
from typing import Union

from core.domain.data_objects import ObjectId, QuestionDto, AnswerDto, TaskDto, RoundDto, GameDto


class DatabaseExtractor(abc.ABC):
    def extract(self, object_id: ObjectId) -> Union[QuestionDto, AnswerDto, TaskDto, RoundDto, GameDto]:
        ...

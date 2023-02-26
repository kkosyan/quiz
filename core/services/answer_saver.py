import abc

from core.domain.data_objects import AnswerDto


class QuestionSaver(abc.ABC):
    def save(self, question: AnswerDto):
        ...

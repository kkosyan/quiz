import abc

from core.domain.data_objects import QuestionDto


class QuestionSaver(abc.ABC):
    def save(self, question: QuestionDto):
        ...
